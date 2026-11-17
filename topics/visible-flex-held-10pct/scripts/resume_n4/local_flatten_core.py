"""Local C4 flattening of a bimodal core with exact defining circle arc.

Pass the existing integral-defined PlateauSupportCore to make_core_class.
Its position, arc inversion and fixed-material parameter Jacobian are reused.
Only the control functions, their actual derivatives and positivity bounds
are replaced. This module does not modify a BVP or its acceptance gates.
"""
import math
import numpy as np
from complementary_moment_basis import ComplementaryMomentBasis
from functools import lru_cache
ComplementaryMomentBasis=lru_cache(maxsize=32)(ComplementaryMomentBasis)


def make_core_class(ReferencePlateauCore):
    class ComplementaryPlateauCore(ReferencePlateauCore):
        def __init__(self,q=.025,corrections=(),base_mode=3,*,halfwidth=.20,
                     transition=.10,homotopy=1.,center=0.,arc_nodes=4096,
                     control_transition=None,lock_fundamental=False,
                     coefficient_precision=80,positivity_grid_max=32768,bimodal_eta=.15):
            if int(base_mode)!=base_mode or base_mode<2:
                raise ValueError('Integral base mode >=2 required')
            self.base_mode=int(base_mode);self.T=2*np.pi/self.base_mode
            self.factor=self.base_mode**2-1;self.q=float(q);self.support_amplitude=self.q
            self.bimodal_eta=float(bimodal_eta)
            if not 0<=self.bimodal_eta<=1:raise ValueError("Local flattening eta must lie in [0,1]")
            actual=np.asarray(corrections,float).copy()
            if len(actual):actual[0]=0.
            self.corrections=tuple(float(c) for c in actual);self.c=actual
            self.a=float(halfwidth);self.transition=float(transition);self.lam=float(homotopy)
            self.center=float(center)%self.T
            if min(abs(self.center),abs(self.center-self.T/2))>1e-12:
                raise ValueError('Reflection-preserving center must be 0 or pi/base_mode')
            if not 0<self.a<self.a+self.transition<self.T/2 or not 0<=self.lam<=1 or q<=0:
                raise ValueError('Invalid plateau geometry')
            self.sign=-1 if abs(self.center)<1e-12 else 1
            self.mean_chi=(2*self.a+self.transition)/self.T
            self._prepare_local_flatten()
            self.L=self.T-2*self.a
            self.control_transition=self.transition if control_transition is None else float(control_transition)
            self.lock_fundamental=bool(lock_fundamental)
            self.basis=None if len(self.c)==0 else ComplementaryMomentBasis(
                base_mode=self.base_mode,modes=len(self.c)+1,halfwidth=self.a,
                transition=self.control_transition,center=self.center,
                lock_fundamental=self.lock_fundamental,precision=coefficient_precision)
            self._basis_cache_phi=None;self._basis_cache_value=None
            if self.basis is None:
                rb=db=np.zeros(0);control_error=0.
            else:
                rb,db,_=self.basis.homotopy_rho_bounds(self.lam)
                ce=self.basis.coefficient_evaluation_error_bounds
                err=self.lam*(ce[0]+ce[2])+(1-self.lam)*(self.base_mode**2-1)*self.basis.fundamental_evaluation_error
                control_error=float(np.sum(abs(self.c)*err))
            self.control_rho_bounds=rb;self.Dnorm=db
            triangle=float(np.sum(abs(self.c)*rb))
            low=1+self.q*((1-self.lam)*(-self.factor*self._bimodal_peak)+self.lam*self.target_min)-triangle
            high=1+self.q*((1-self.lam)*self.factor*(1+2*self.bimodal_eta)+self.lam*self.target_max)+triangle
            self.rho_triangle_lower=math.nextafter(low,-math.inf)
            self.rho_triangle_upper=math.nextafter(high,math.inf)
            base_prime=self.q*(self.factor*self.base_mode*(1+3*self.bimodal_eta)+self.lam*self._flatten_prime_bound)
            self.rho_derivative_bound=math.nextafter((base_prime+float(np.sum(abs(self.c)*db)))*(1+128*np.finfo(float).eps),math.inf)
            # Coefficient uncertainty is certified by rational moment intervals.
            # The additional allowance is numerical evaluation roundoff, not an
            # interval certificate for an embedded surface or a libm theorem.
            self.rho_value_roundoff_allowance=control_error+1e-12*(1+self.q*self.factor/(1-self.mean_chi)+triangle)
            self.rho_triangle_lower=math.nextafter(self.rho_triangle_lower-self.rho_value_roundoff_allowance,-math.inf)
            self.rho_triangle_upper=math.nextafter(self.rho_triangle_upper+self.rho_value_roundoff_allowance,math.inf)
            count=512;maximum=int(positivity_grid_max)
            if maximum<512:raise ValueError('Do not reduce the original positivity grid ceiling')
            while True:
                grid=self.T*np.arange(count)/count
                rr=1+self.q*self.unit_rho(grid)
                if self.basis is not None:
                    b,_,bpp=self.basis.support_jets(grid,2,self.lam)
                    rr+=self.c@(b+bpp)
                slack=self.T/(2*count)*self.rho_derivative_bound+self.rho_value_roundoff_allowance
                self.rho_lower=max(self.rho_triangle_lower,float(rr.min()-slack))
                self.rho_upper=min(self.rho_triangle_upper,float(rr.max()+slack))
                self.positivity_grid_per_sector=count
                if self.rho_lower>1e-5:break
                if rr.min()<=1e-5:
                    raise FloatingPointError('Core rho sampled positivity failed: '+str((float(rr.min()),self.rho_lower,count)))
                if count>=maximum:
                    raise FloatingPointError('Core rho guard unable to certify at its grid ceiling: '+str((float(rr.min()),self.rho_lower,count)))
                count=min(2*count,maximum)
            # The remaining initialization is the original integral core's
            # position/arc construction, without a Fourier substitution.
            self.gx,self.gw=np.polynomial.legendre.leggauss(32)
            marks=[0.,self.T,self.center]
            for v in (-self.a-self.transition,-self.a,self.a,self.a+self.transition):
                marks.append((self.center+v)%self.T)
            self.breaks=np.unique(np.array(marks));self.cum=np.zeros((len(self.breaks),3))
            for i,(lo,hi) in enumerate(zip(self.breaks[:-1],self.breaks[1:])):
                self.cum[i+1]=self.cum[i]+self._quad(lo,np.array([hi]))[0]
            self.period_integral_roundoff=float(self.cum[-1,0]);self.cum[-1,0]=0.
            R=np.array([[math.cos(self.T),-math.sin(self.T)],[math.sin(self.T),math.cos(self.T)]])
            self.unit_origin=np.linalg.solve(R-np.eye(2),self.cum[-1,1:])
            f,_,f2,_=self._basis(np.array([0.]));self.f0=f[:,0];self.f20=f2[:,0]
            phi=2*np.pi*np.arange(arc_nodes)/arc_nodes;g=self.normal_geometry(phi);rho=g['rho']
            self.rho_min_sample=float(rho.min());self.rho_max_sample=float(rho.max())
            self.minimum_sampled_curvature=1/self.rho_max_sample;self.maximum_sampled_curvature=1/self.rho_min_sample
            self.curvature_upper_bound=1/self.rho_lower;self.curvature_lower_bound=1/self.rho_upper
            self.radius_max_sample=float(np.linalg.norm(g['F'],axis=1).max());self.radius_min_sample=float(np.linalg.norm(g['F'],axis=1).min())
            self.radius_upper_bound=self.radius_max_sample+2*np.pi/arc_nodes*self.rho_upper
            self.radius_lower_bound=max(0,self.radius_min_sample-2*np.pi/arc_nodes*self.rho_upper)
            self.constant_width_exact=False;self.width_defect_bound=math.nan
            width=g['h']+self.normal_geometry(phi+np.pi)['h'];self.width_min_sample=float(width.min());self.width_max_sample=float(width.max())
            self.support_monotone=False;self.coefficients=np.r_[q,self.c]
            self.frequencies=self.base_mode*np.arange(1,len(self.c)+2)
            self._last_theta=None;self._last_evaluation=None

        def _basis(self,phi):
            flat=np.asarray(phi,float).ravel()
            if self.basis is None:return tuple(np.empty((0,len(flat))) for _ in range(4))
            if self._basis_cache_phi is not None and np.array_equal(flat,self._basis_cache_phi):
                return self._basis_cache_value
            value=tuple(v.copy()for v in self.basis.primitive_jets(flat,3,self.lam))
            for v in value:v[0]=0. # Ignored c8 slot: all parameter jets must vanish.
            self._basis_cache_phi=flat.copy();self._basis_cache_value=value
            return value

        def chi(self,phi):
            d=np.abs((np.asarray(phi)-self.center+self.T/2)%self.T-self.T/2)
            t=np.clip((d-self.a)/self.transition,0.,1.)
            return 1-t**5*(126+t*(-420+t*(540+t*(-315+70*t))))

        def _smooth_jets(self,phi):
            phi=np.asarray(phi);n=self.base_mode;eta=self.bimodal_eta
            x=n*phi;f=self.factor
            return (-f*((1+eta)*np.cos(x)-eta*np.cos(2*x)),
                    f*n*((1+eta)*np.sin(x)-2*eta*np.sin(2*x)),
                    f*n*n*((1+eta)*np.cos(x)-4*eta*np.cos(2*x)))

        def _prepare_local_flatten(self):
            if self.center!=0.:raise ValueError('Local flattening currently uses center zero')
            eta=self.bimodal_eta
            self._bimodal_peak=1. if eta<=1/3 else eta+(1+eta)**2/(8*eta)
            gx,gw=np.polynomial.legendre.leggauss(64)
            total=0.
            for lo,hi in ((0.,self.a),(self.a,self.a+self.transition)):
                x=(hi+lo)/2+(hi-lo)/2*gx
                total+=(hi-lo)/2*float(gw@(self.chi(x)*(-self.factor-self._smooth_jets(x)[0])))
            self.local_flatten_beta=-(2/self.T)*total/(1-self.mean_chi)
            beta=self.local_flatten_beta
            self.target_min=min(-self.factor,-self.factor*self._bimodal_peak+beta)
            self.target_max=max(-self.factor,self.factor*(1+2*eta)+beta)
            lo=math.cos(self.base_mode*(self.a+self.transition));hi=math.cos(self.base_mode*self.a)
            xs=[lo,hi]
            if eta>0 and lo<=(1+eta)/(4*eta)<=hi:xs.append((1+eta)/(4*eta))
            difference=max(abs(self.factor-self.factor*((1+eta)*y-eta*(2*y*y-1))+beta) for y in xs)
            self._flatten_prime_bound=math.nextafter((630/256)/self.transition*difference,math.inf)

        def unit_rho(self,phi):
            smooth=self._smooth_jets(phi)[0];chi=self.chi(phi)
            return smooth+self.lam*(chi*(-self.factor-smooth)+self.local_flatten_beta*(1-chi))

        def rho_material_jets(self,theta):
            g=self.evaluate(theta);phi=g['phi'];rho=1/g['kappa']
            d=(phi-self.center+self.T/2)%self.T-self.T/2
            t=np.clip((abs(d)-self.a)/self.transition,0.,1.)
            chi=self.chi(phi)
            chip=-630*t**4*(1-t)**4*np.sign(d)/self.transition
            chipp=-2520*t**3*(1-t)**3*(1-2*t)/self.transition**2
            smooth,sp,spp=self._smooth_jets(phi)
            delta=self.factor+smooth+self.local_flatten_beta
            rp=self.q*(sp+self.lam*(-chi*sp-chip*delta))
            rpp=self.q*(spp+self.lam*(-chi*spp-2*chip*sp-chipp*delta))
            if self.basis is not None:
                b=self.basis.support_jets(phi,4,self.lam)
                rp+=self.c@(b[1]+b[3]);rpp+=self.c@(b[2]+b[4])
            return dict(**g,rho=rho,rho_u=rp/rho,rho_uu=(rpp*rho-rp*rp)/rho**3,
                        rho_phi=rp,rho_phiphi=rpp,
                        normal=np.c_[np.cos(phi),np.sin(phi),np.zeros_like(phi)])

        def summary(self):
            out=super().summary()
            out.update(control_family='C4 complementary controls with fixed c8=0 and two-harmonic primary',
                       bimodal_eta=self.bimodal_eta,ignored_correction_index=0,
                       local_flatten_beta=self.local_flatten_beta,
                       target_family='C4 local circle flattening of the double harmonic, with complementary mean correction',
                       control_transition=self.control_transition,lock_fundamental=self.lock_fundamental,
                       control_homotopy='lambda compact + (1-lambda) identical represented low support moments',
                       control_projection_order=len(self.c)+1,
                       rho_triangle_upper=self.rho_triangle_upper,
                       rho_value_roundoff_allowance=self.rho_value_roundoff_allowance,
                       control_certificate=None if self.basis is None else self.basis.summary())
            return out

    ComplementaryPlateauCore.__name__='ComplementaryPlateauCore'
    return ComplementaryPlateauCore
