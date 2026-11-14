#!/usr/bin/env python3
"""One R2 core cut to an asymmetric exact-flat-tail port, with full two jets.

This is a design-stage finite BVP. A finite residual never certifies an exact
connector, a closed surface, reach, or completion of the topic. The current
implementation uses the complete E/F/G residual; it does not divide by II_uu.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import time
from pathlib import Path
import numpy as np
from numpy.polynomial import polynomial as poly
from scipy.interpolate import BSpline
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares, brentq
from scipy.special import ellipe, ellipeinc
from mixed_mode_gc_flow import initial_field, rhs, background, diagnostics


HCOEF = np.array([
    [1,0,0,-10,15,-6], [0,1,0,-6,8,-3], [0,0,.5,-1.5,1.5,-.5],
    [0,0,0,10,-15,6], [0,0,0,-4,7,-3], [0,0,0,.5,-1,.5],
], dtype=float)
SCOEF = np.array([0,0,0,0,0,126,-420,540,-315,70.], dtype=float)


def fourier(theta, modes, derivative=0):
    cols = [np.ones_like(theta) if derivative == 0 else np.zeros_like(theta)]
    for k in range(1, modes+1):
        cols.extend([k**derivative*np.cos(k*theta+derivative*np.pi/2),
                     k**derivative*np.sin(k*theta+derivative*np.pi/2)])
    return np.stack(cols, axis=-1)


def hermite(u, derivative=0):
    return np.stack([poly.polyval(u, poly.polyder(c, derivative)) for c in HCOEF], axis=-1)


def interp_periodic(values, theta, derivative=0):
    """The same real trigonometric polynomial at an independent angular grid."""
    n = values.shape[-1]
    coeff = np.fft.rfft(values, axis=-1)/n
    out = np.zeros(values.shape[:-1]+(len(theta),))
    if derivative == 0:
        out += coeff[..., 0, None].real
    top = len(coeff[0]) if coeff.ndim == 2 else coeff.shape[-1]
    for k in range(1, top):
        if n % 2 == 0 and k == n//2:
            out += coeff[..., k, None].real*k**derivative*np.cos(k*theta+derivative*np.pi/2)
        else:
            out += 2*np.real(coeff[..., k, None]*(1j*k)**derivative*np.exp(1j*k*theta))
    return out


def step(t, derivative=0):
    z = np.clip(t, 0., 1.)
    answer = poly.polyval(z, poly.polyder(SCOEF, derivative))
    if derivative:
        answer = np.where((t > 0) & (t < 1), answer, 0.)
    else:
        answer = np.where(t <= 0, 0., np.where(t >= 1, 1., answer))
    return answer


class UnitMeridian:
    """Exact unit-speed revolution background; quadrature evaluates its integrals."""
    def __init__(self,a0,ap0,app0,length,cut_radius,center,quadrature,wiggle=0.):
        self.length=length
        self.a0=a0
        self.center=np.asarray(center)
        self.gl,self.gw=np.polynomial.legendre.leggauss(quadrature)
        beta0=np.arccos(ap0)
        zp=np.sqrt(1-ap0*ap0)
        betap=-app0/zp
        betapp=-ap0*betap*betap/zp  # inlet a'''=0.
        self.beta_coeff=HCOEF.T@np.array([beta0,length*betap,length*length*betapp,np.pi,0,0])
        self.bump_coeff=np.array([0.,0,0,64,-192,192,-64,0.])
        self.beta_coeff=np.r_[self.beta_coeff,0.,0.]
        # This odd-about-the-midpoint polynomial has exact maximum absolute value 1.
        wave=poly.polymul(self.bump_coeff[:-1],[-1.,2.])*(343*np.sqrt(7)/216)
        self.beta_coeff+=wiggle*wave
        self.wiggle=wiggle
        def closure(value):
            beta=poly.polyval((self.gl+1)/2,self.beta_coeff+value*self.bump_coeff)
            return a0+length/2*np.dot(self.gw,np.cos(beta))-cut_radius
        scan=np.linspace(-6,6,241)
        candidates=[(lo,hi) for lo,hi in zip(scan[:-1],scan[1:]) if closure(lo)*closure(hi)<=0]
        if not candidates:
            raise ValueError('No scalar reference-meridian closure in the fixed [-6,6] search')
        lo,hi=min(candidates,key=lambda pair:abs(sum(pair)))
        self.control=brentq(closure,lo,hi,xtol=2e-14)
        self.beta_coeff+=self.control*self.bump_coeff
        self.closure_error=float(closure(0.))  # closure now uses the finalized coefficients.

    def beta(self,u,derivative=0):
        return poly.polyval(u,poly.polyder(self.beta_coeff,derivative))

    def evaluate(self,u):
        u=np.asarray(u)
        nodes=u[:,None]*(self.gl[None,:]+1)/2
        beta=self.beta(nodes)
        ar=self.a0+self.length*u/2*(np.cos(beta)@self.gw)
        zz=self.center[2]+self.length*u/2*(np.sin(beta)@self.gw)
        beta=self.beta(u)
        bp=self.beta(u,1)/self.length
        return ([ar,np.cos(beta),-np.sin(beta)*bp],
                [zz,np.sin(beta),np.cos(beta)*bp])

    def jet(self,u,theta,rd=0,td=0):
        aa,zz=self.evaluate(u)
        x=aa[rd][:,None]*np.sin(theta[None,:]+td*np.pi/2)
        y=-aa[rd][:,None]*np.cos(theta[None,:]+td*np.pi/2)
        z=np.broadcast_to(zz[rd][:,None] if td==0 else np.zeros((len(u),1)),x.shape).copy()
        if rd==0 and td==0:
            x+=self.center[0];y+=self.center[1]
        return np.stack((x,y,z),axis=-1)

    def diagnostics(self):
        u=np.linspace(0,1,1001)
        aa,zz=self.evaluate(u)
        beta=self.beta(u)
        bp=self.beta(u,1)/self.length
        curve=np.column_stack((aa[0],zz[0]))
        a,b=curve[:-1],curve[1:]
        count=0
        def cross2(x,y):
            return x[:,0]*y[:,1]-x[:,1]*y[:,0]
        for i in range(len(a)-2):
            ids=np.arange(i+2,len(a))
            lo=np.maximum(np.minimum(a[i],b[i]),np.minimum(a[ids],b[ids]))
            hi=np.minimum(np.maximum(a[i],b[i]),np.maximum(a[ids],b[ids]))
            ids=ids[np.all(lo<=hi,axis=1)]
            if len(ids):
                ab=np.broadcast_to(b[i]-a[i],(len(ids),2))
                cd=b[ids]-a[ids]
                c1=cross2(ab,a[ids]-a[i]);c2=cross2(ab,b[ids]-a[i])
                c3=cross2(cd,a[i]-a[ids]);c4=cross2(cd,b[i]-a[ids])
                count+=int(np.count_nonzero((c1*c2<0)&(c3*c4<0)))
        maxk=float(np.max(np.maximum(np.abs(bp),np.abs(np.sin(beta)/aa[0]))))
        diameter_box=float(np.sqrt((2*np.max(aa[0]))**2+np.ptp(zz[0])**2))
        dz=zz[0][None,:]-zz[0][:,None]
        normal_chord=np.inf
        for sign in (1.,-1.):
            dr=sign*aa[0][None,:]-aa[0][:,None]
            distance2=dr*dr+dz*dz
            denominator=2*np.abs(-np.sin(beta)[:,None]*dr+np.cos(beta)[:,None]*dz)
            valid=(distance2>1e-20)&(denominator>1e-20)
            normal_chord=min(normal_chord,float(np.min(distance2[valid]/denominator[valid])))
        return {'beta_wiggle':self.wiggle,'beta_range':[float(beta.min()),float(beta.max())],
                'radius_range':[float(aa[0].min()),float(aa[0].max())],
                'height_range':[float(zz[0].min()),float(zz[0].max())],
                'interior_hoop_normal_curvature_sign_changes':int(np.count_nonzero(np.sin(beta[1:-2])*np.sin(beta[2:-1])<0)),
                'sample_polyline_proper_self_intersections':count,
                'sample_max_principal_curvature':maxk,
                'diameter_box_upper':diameter_box,
                'sample_curvature_times_003_diameter_box':maxk*.03*diameter_box,
                'sample_min_normal_chord_radius':normal_chord,
                'sample_min_normal_chord_radius_over_diameter_box':normal_chord/diameter_box,
                'continuous_injectivity_certified':False,'reach_certified':False}


class FoldedMeridian(UnitMeridian):
    """Two smooth angle transitions, then an exact flat radial segment."""
    def __init__(self,a0,ap0,app0,length,cut_radius,center,quadrature,minimum=-.2,first_fraction=.33):
        self.a0=a0;self.length=length;self.center=np.asarray(center)
        self.gl,self.gw=np.polynomial.legendre.leggauss(quadrature)
        self.wiggle=0.
        self.minimum=minimum;self.first_fraction=first_fraction
        self.beta0=np.arccos(ap0)
        zp=np.sqrt(1-ap0*ap0)
        self.betap=-app0/zp
        self.betapp=-ap0*self.betap*self.betap/zp
        def closure(active):
            self.set_active(active)
            aa,_=self.evaluate(np.array([1.]))
            return aa[0][0]-cut_radius
        scan=np.linspace(.02*length,.995*length,100)
        brackets=[(lo,hi) for lo,hi in zip(scan[:-1],scan[1:]) if closure(lo)*closure(hi)<=0]
        if not brackets:
            raise ValueError('Folded reference has no positive final-flat-segment closure')
        self.control=brentq(closure,*brackets[0],xtol=2e-14)
        self.set_active(self.control)
        self.closure_error=float(self.evaluate(np.array([1.]))[0][0][0]-cut_radius)

    def set_active(self,active):
        self.u2=active/self.length
        self.u1=self.first_fraction*self.u2
        first_length=self.u1*self.length
        self.first_coef=HCOEF.T@np.array([self.beta0,first_length*self.betap,
                                         first_length*first_length*self.betapp,self.minimum,0,0])
        self.second_coef=HCOEF.T@np.array([self.minimum,0,0,np.pi,0,0])

    def beta(self,u,derivative=0):
        u=np.asarray(u)
        first=poly.polyval(u/self.u1,poly.polyder(self.first_coef,derivative))/self.u1**derivative
        second=poly.polyval((u-self.u1)/(self.u2-self.u1),poly.polyder(self.second_coef,derivative))/(self.u2-self.u1)**derivative
        return np.where(u<=self.u1,first,np.where(u<=self.u2,second,np.pi if derivative==0 else 0.))

    def evaluate(self,u):
        u=np.asarray(u)
        ia=np.zeros_like(u,dtype=float);iz=np.zeros_like(u,dtype=float)
        for left,right in ((0.,self.u1),(self.u1,self.u2)):
            width=np.maximum(np.minimum(u,right)-left,0)
            nodes=left+width[:,None]*(self.gl[None,:]+1)/2
            beta=self.beta(nodes)
            ia+=width/2*(np.cos(beta)@self.gw)
            iz+=width/2*(np.sin(beta)@self.gw)
        ia-=np.maximum(u-self.u2,0)
        ar=self.a0+self.length*ia
        zz=self.center[2]+self.length*iz
        beta=self.beta(u);bp=self.beta(u,1)/self.length
        return ([ar,np.cos(beta),-np.sin(beta)*bp],
                [zz,np.sin(beta),np.cos(beta)*bp])


class InwardMeridian(FoldedMeridian):
    """Nonexpanding reference: pi/2 -> pi+eta -> pi -> exact plane.

    With the exact cylindrical inlet, every intermediate cosine is nonpositive.
    Unlike the earlier negative-angle fold, this introduces one internal change
    of hoop normal curvature without an outward radial excursion.
    """
    def __init__(self,a0,ap0,app0,length,cut_radius,center,quadrature,
                 overshoot=.2,first_fraction=.7):
        if abs(ap0)>1e-12 or abs(app0)>1e-12:
            raise ValueError('Inward reference requires a cylindrical inlet; use --core-profile ellipse')
        if not 0<overshoot<np.pi/2 or not 0<first_fraction<1:
            raise ValueError('Need 0 < inward overshoot < pi/2 and 0 < first fraction < 1')
        self.a0=a0;self.length=length;self.center=np.asarray(center)
        self.gl,self.gw=np.polynomial.legendre.leggauss(quadrature)
        self.wiggle=0.;self.minimum=np.pi+overshoot
        self.first_fraction=first_fraction
        self.beta0=np.pi/2;self.betap=0.;self.betapp=0.
        self.set_active(length)
        full_drop=a0-self.evaluate(np.array([1.]))[0][0][0]
        mean_drop=full_drop/length
        delta=a0-cut_radius
        active=(length-delta)/(1-mean_drop)
        if not 0<active<length:
            raise ValueError(f'Inward closure requires {delta:.12g} < length < '
                             f'{delta/mean_drop:.12g}; got {length:.12g}')
        self.control=active
        self.set_active(active)
        self.closure_error=float(self.evaluate(np.array([1.]))[0][0][0]-cut_radius)


def ellipse_inlet(theta,major,minor,height,derivative=0):
    """Exact arc-length-gauge elliptic cylinder jets at arbitrary angles."""
    if not 0<minor<=major:
        raise ValueError('Need 0 < ellipse minor <= major')
    theta=np.asarray(theta)
    m=1-(minor/major)**2
    a0=2*major*ellipe(m)/np.pi
    phase=theta.copy()
    for _ in range(24):
        speed=np.sqrt(major*major*np.cos(phase)**2+minor*minor*np.sin(phase)**2)
        step=(major*ellipeinc(phase,m)-a0*theta)/speed
        phase-=np.clip(step,-.5,.5)
        if np.max(np.abs(step))<4e-15:
            break
    error=float(np.max(np.abs(major*ellipeinc(phase,m)-a0*theta)))
    if error>3e-13*major:
        raise RuntimeError(f'Ellipse arc-length inversion failed: {error}')
    sp,cp=np.sin(phase),np.cos(phase)
    speed=np.sqrt(major*major*cp*cp+minor*minor*sp*sp)
    tp=a0/speed
    tpp=-a0*a0*(minor*minor-major*major)*sp*cp/speed**4
    ans=np.zeros((3,len(theta),3))
    if derivative==0:
        ans[0]=np.column_stack((major*sp,-minor*cp,np.full_like(sp,height)))
        ans[1,:,2]=1.
    elif derivative==1:
        ans[0]=np.column_stack((major*cp*tp,minor*sp*tp,np.zeros_like(sp)))
    elif derivative==2:
        ans[0]=np.column_stack((-major*sp*tp*tp+major*cp*tpp,
                                minor*cp*tp*tp+minor*sp*tpp,np.zeros_like(sp)))
    else:
        raise ValueError('Only angular derivatives 0, 1, 2 are needed')
    return ans,a0,error


class Problem:
    def __init__(self, args):
        self.args = args
        self.J, self.K = args.radial_free, 2*args.modes+1
        self.np = 3*self.J*self.K
        self.na = self.J if args.design_metric else 0
        self.size = self.np+self.na+4  # A+, A-, Cy, Cz.
        count = self.J+6
        self.knots = np.r_[np.zeros(6), np.arange(1,self.J+1)/(self.J+1), np.ones(6)]
        self.spline = BSpline(self.knots, np.eye(count), 5)
        self.core_profile=getattr(args,'core_profile','mixed')
        if self.core_profile=='ellipse':
            theta=np.arange(args.inlet_angles)*2*np.pi/args.inlet_angles
            inp,self.a0,inv_error=ellipse_inlet(theta,args.ellipse_major,args.ellipse_minor,args.inlet_s)
            self.inlet=inp.transpose(0,2,1)
            self.ap0=0.;self.app0=0.
            xt=ellipse_inlet(theta,args.ellipse_major,args.ellipse_minor,args.inlet_s,1)[0][0]
            self.inlet_solver={'method':'exact_elliptic_cylinder_analytic_jets',
                               'arc_length_inversion_max_error':inv_error}
            rho_min=args.ellipse_minor**2/args.ellipse_major
            rho_max=args.ellipse_major**2/args.ellipse_minor
            self.inlet_report={'s':args.inlet_s,'radius_metric':self.a0,
                'center':[0.,0.,args.inlet_s],
                'sample_relative_metric_op':float(np.max(np.abs(np.sum(xt*xt,axis=-1)/self.a0**2-1))),
                'sample_position_frame_compatibility':0.,'sample_frame_orthogonality':0.,
                'sample_abs_principal_curvature':1/rho_min,
                'sample_min_N':self.a0**2/rho_max,
                'sample_circle_radial_spread':args.ellipse_major-args.ellipse_minor,
                'sample_section_height_spread':0.,'sample_max_abs_M':0.,
                'sample_GC_N_spread':self.a0**2*(1/rho_min-1/rho_max),
                'exact_ellipse_perimeter_radius':self.a0}
        else:
            theta, state = initial_field(args.inlet_angles, args.amp2, args.amp3)
            if args.inlet_state:
                data = np.load(args.inlet_state)
                state = data['state'][:,-1].reshape(14,args.inlet_angles)
                if abs(float(data['s'][-1])-args.inlet_s) > 1e-12:
                    raise ValueError('Inlet state does not have the requested endpoint')
                self.inlet_solver = {'loaded':str(args.inlet_state)}
            else:
                sol = solve_ivp(lambda s,y:rhs(s,y,args.inlet_angles,args.curvature),
                                (0,args.inlet_s),state.ravel(),method='DOP853',
                                rtol=2e-12,atol=2e-14,max_step=.004)
                if not sol.success:
                    raise RuntimeError(sol.message)
                state = sol.y[:,-1].reshape(14,args.inlet_angles)
                self.inlet_solver = {'success':True,'nfev':sol.nfev}
            self.a0,self.ap0,self.app0 = background(args.inlet_s,args.curvature)
            ell = (state[0]**2-self.a0*self.app0)/state[1]
            self.inlet = np.stack((state[2:5],state[5:8],ell*state[11:14]))
            self.inlet_report = diagnostics(args.inlet_s,state,args.curvature)
        gl,gw = np.polynomial.legendre.leggauss(args.quadrature)
        self.gl,self.gw = gl,gw
        self.reference=None
        if args.background=='unit':
            self.reference=UnitMeridian(self.a0,self.ap0,self.app0,args.length,args.cut_radius,
                                        self.inlet[0].mean(axis=1),args.quadrature,args.beta_wiggle)
        elif args.background=='folded':
            self.reference=FoldedMeridian(self.a0,self.ap0,self.app0,args.length,args.cut_radius,
                                          self.inlet[0].mean(axis=1),args.quadrature,
                                          args.fold_min,args.fold_first_fraction)
        elif args.background=='inward':
            self.reference=InwardMeridian(self.a0,self.ap0,self.app0,args.length,args.cut_radius,
                                          self.inlet[0].mean(axis=1),args.quadrature,
                                          args.inward_overshoot,args.inward_first_fraction)

    def radial(self,u,derivative=0):
        return self.spline(u,nu=derivative)[:,3:-3]/self.args.length**derivative

    def prepare(self, radial, angular):
        u = np.asarray(radial)
        theta = np.arange(angular)*2*np.pi/angular
        f = [fourier(theta,self.args.modes,d) for d in range(3)]
        r = [self.radial(u,d) for d in range(3)]
        h = [hermite(u,d)/self.args.length**d for d in range(3)]
        if self.core_profile=='ellipse':
            inlet=[ellipse_inlet(theta,self.args.ellipse_major,self.args.ellipse_minor,
                                 self.args.inlet_s,d)[0] for d in range(3)]
        else:
            inlet = [interp_periodic(self.inlet,theta,d).transpose(0,2,1) for d in range(3)]
        avec = np.array([self.a0,self.args.length*self.ap0,self.args.length**2*self.app0,
                         self.args.cut_radius,-self.args.length,0.])
        abase = [hh@avec for hh in h]
        ref=None;ref_end=None
        if self.reference is not None:
            abase=self.reference.evaluate(u)[0]
            ref=[[self.reference.jet(u,theta,rd,td) for td in range(3)] for rd in range(3)]
            ends=np.array([0.,1.])
            ref_end=[np.stack([self.reference.jet(ends,theta,rd,td) for rd in range(3)])
                     for td in range(3)]
        return dict(u=u,theta=theta,f=f,r=r,h=h,inlet=inlet,abase=abase,ref=ref,ref_end=ref_end)

    def alpha(self,y,aplus,aminus,derivative=0):
        width = self.args.cut_radius-self.args.flat_start
        t = (np.abs(y)-self.args.flat_start)/width
        if derivative == 0:
            amp = np.where(y >= 0,aplus,-aminus)
        else:
            amp = np.where(y >= 0,aplus,(-1)**(derivative+1)*aminus)
        return amp*step(t,derivative)/width**derivative

    def tail(self,theta,params):
        ap,am,cy,cz = params
        r = self.args.cut_radius
        angle = theta-np.pi/2
        p,q = np.sin(angle),np.cos(angle)
        y = r*p
        nodes = y[:,None]*(self.gl[None,:]+1)/2
        al = self.alpha(nodes,ap,am)
        yy = y/2*(np.cos(al)@self.gw)
        ww = y/2*(np.sin(al)@self.gw)
        al = self.alpha(y,ap,am)
        k,kp,kpp = [self.alpha(y,ap,am,d) for d in (1,2,3)]
        ex = np.tile([1.,0.,0.],(len(theta),1))
        ty = np.column_stack((np.zeros_like(y),np.cos(al),-np.sin(al)))
        ny = np.column_stack((np.zeros_like(y),-np.sin(al),-np.cos(al)))
        scale = lambda z:z[:,None]
        x = np.column_stack((r*q,yy+cy,cz-ww))
        xs = -scale(q)*ex-scale(p)*ty
        xss = scale(p*p*k)*ny
        xt = r*(-scale(p)*ex+scale(q)*ty)
        xtt = -r*(scale(q)*ex+scale(p)*ty)+scale(r*r*q*q*k)*ny
        xst = scale(p)*ex-scale(q)*ty-scale(r*p*q*k)*ny
        xstt = scale(q)*ex+scale(p+r*r*p*q*q*k*k)*ty
        xstt -= scale(r*(2*q*q-p*p)*k+r*r*p*q*q*kp)*ny
        kk = p*p*k
        kkt = 2*p*q*k+r*p*p*q*kp
        kktt = 2*(q*q-p*p)*k+r*(4*p*q*q-p**3)*kp+r*r*p*p*q*q*kpp
        xsst = scale(kkt)*ny-scale(kk*k*r*q)*ty
        xsstt = scale(kktt-kk*k*k*r*r*q*q)*ny
        xsstt += scale(-2*kkt*k*r*q-kk*kp*r*r*q*q+kk*k*r*p)*ty
        return [np.stack((x,xs,xss)),np.stack((xt,xst,xsst)),np.stack((xtt,xstt,xsstt))]

    def unpack(self,z):
        xyz = z[:self.np].reshape(3,self.J,self.K)
        aa = z[self.np:self.np+self.na] if self.na else np.zeros(self.J)
        return xyz,aa,z[-4:]

    def geometry(self,z,grid,second=False):
        cc,aa,tailparams = self.unpack(z)
        tail = self.tail(grid['theta'],tailparams)
        length = self.args.length
        factors = np.array([1,length,length*length])[:,None,None]
        if grid['ref'] is None:
            endpoints=[np.concatenate((grid['inlet'][d]*factors,tail[d]*factors),axis=0)
                       for d in range(3)]
        else:
            endpoints=[np.concatenate(((grid['inlet'][d]-grid['ref_end'][d][:,0])*factors,
                                        (tail[d]-grid['ref_end'][d][:,1])*factors),axis=0)
                       for d in range(3)]
        def base(rd,td):
            ans=np.einsum('rh,huc->ruc',grid['h'][rd],endpoints[td])
            if grid['ref'] is not None:
                ans=ans+grid['ref'][rd][td]
            return ans
        free = lambda rd,td:np.einsum('rj,cjk,uk->ruc',grid['r'][rd],cc,grid['f'][td])
        xx = base(0,0)+free(0,0)
        xs = base(1,0)+free(1,0)
        xt = base(0,1)+free(0,1)
        a = grid['abase'][0]+grid['r'][0]@aa
        result = dict(x=xx,xs=xs,xt=xt,a=a)
        if second:
            result.update(xss=base(2,0)+free(2,0),xst=base(1,1)+free(1,1),
                          xtt=base(0,2)+free(0,2),ap=grid['abase'][1]+grid['r'][1]@aa,
                          app=grid['abase'][2]+grid['r'][2]@aa)
        return result

    def residual(self,z,grid):
        g = self.geometry(z,grid)
        e = np.sum(g['xs']**2,axis=-1)
        f = np.sum(g['xs']*g['xt'],axis=-1)
        gg = np.sum(g['xt']**2,axis=-1)
        a = g['a'][:,None]
        core = np.stack((e-1,np.sqrt(2)*f/a,gg/(a*a)-1),axis=-1)
        bound = self.args.radius_weight*np.sqrt(len(grid['theta']))*np.stack(
            (np.maximum(self.args.radius_floor-g['a'],0),
             np.maximum(g['a']-self.args.radius_ceiling,0)),axis=-1)
        return np.r_[core.ravel(),bound.ravel()]

    def jacobian(self,z,grid):
        g = self.geometry(z,grid)
        nr,nu = g['xs'].shape[:2]
        r0,r1 = grid['r'][:2]
        f0,f1 = grid['f'][:2]
        bs = (r1[:,None,:,None]*f0[None,:,None,:]).reshape(nr,nu,-1)
        bt = (r0[:,None,:,None]*f1[None,:,None,:]).reshape(nr,nu,-1)
        a = g['a'][:,None,None]
        j = np.zeros((nr,nu,3,self.size))
        nblock = self.J*self.K
        for c in range(3):
            sl = slice(c*nblock,(c+1)*nblock)
            j[:,:,0,sl] = 2*g['xs'][:,:,c,None]*bs
            j[:,:,1,sl] = np.sqrt(2)*(g['xt'][:,:,c,None]*bs+g['xs'][:,:,c,None]*bt)/a
            j[:,:,2,sl] = 2*g['xt'][:,:,c,None]*bt/(a*a)
        if self.na:
            ff = np.sum(g['xs']*g['xt'],axis=-1)
            gg = np.sum(g['xt']**2,axis=-1)
            j[:,:,1,self.np:self.np+self.na] = -np.sqrt(2)*ff[:,:,None]*r0[:,None,:]/(a*a)
            j[:,:,2,self.np:self.np+self.na] = -2*gg[:,:,None]*r0[:,None,:]/(a*a*a)
        bound = np.zeros((nr,2,self.size))
        if self.na:
            fac = self.args.radius_weight*np.sqrt(nu)
            bound[:,0,self.np:self.np+self.na] = -fac*(g['a']<self.args.radius_floor)[:,None]*r0
            bound[:,1,self.np:self.np+self.na] = fac*(g['a']>self.args.radius_ceiling)[:,None]*r0
        out = np.vstack((j.reshape(-1,self.size),bound.reshape(-1,self.size)))
        for k in range(self.size-4,self.size):
            delta = 2e-6*max(1.,abs(z[k]))
            zp,zm = z.copy(),z.copy()
            zp[k] += delta; zm[k] -= delta
            out[:,k] = (self.residual(zp,grid)-self.residual(zm,grid))/(2*delta)
        return out

    def seed(self):
        z = np.zeros(self.size)
        height=self.args.tail_height
        if height is None:
            height=float(self.reference.evaluate(np.array([1.]))[1][0][0]) if self.reference else .9
        z[-4:] = [self.args.tail_plus,self.args.tail_minus,0.,height]
        return z

    def audit(self,z,radial,angular):
        grid = self.prepare(np.linspace(0,1,radial),angular)
        g = self.geometry(z,grid,True)
        xs,xt,a = g['xs'],g['xt'],g['a'][:,None]
        e = np.sum(xs*xs,axis=-1)
        f = np.sum(xs*xt,axis=-1)
        gg = np.sum(xt*xt,axis=-1)
        mat = np.empty((*e.shape,2,2))
        mat[:,:,0,0] = e-1
        mat[:,:,0,1] = mat[:,:,1,0] = f/a
        mat[:,:,1,1] = gg/(a*a)-1
        cross = np.cross(xs,xt)
        det = np.sum(cross*cross,axis=-1)
        normal = cross/np.sqrt(np.maximum(det,1e-300))[:,:,None]
        h11,h12,h22 = [np.sum(normal*g[key],axis=-1) for key in ('xss','xst','xtt')]
        hh = (gg*h11+e*h22-2*f*h12)/(2*np.maximum(det,1e-300))
        kk = (h11*h22-h12*h12)/np.maximum(det,1e-300)
        curvature = np.abs(hh)+np.sqrt(np.maximum(hh*hh-kk,0))
        vt = np.sqrt(gg)
        tangent = xt/vt[:,:,None]
        dt = (g['xtt']-tangent*np.sum(tangent*g['xtt'],axis=-1)[:,:,None])/vt[:,:,None]
        curve_k = np.linalg.norm(dt,axis=-1)
        nc = dt/np.maximum(curve_k,1e-300)[:,:,None]
        bc = np.cross(tangent,nc)
        psi = np.arctan2(np.sum(xs*bc,axis=-1),np.sum(xs*nc,axis=-1))
        tail = self.tail(grid['theta'],z[-4:])[0]
        start = grid['inlet'][0]
        jets = np.stack((g['x'][[0,-1]],g['xs'][[0,-1]],g['xss'][[0,-1]]))
        expected = np.stack((start,tail),axis=1)
        return {'radial_points':radial,'angular_points':angular,
                'relative_metric_operator_sample_max':float(np.max(np.abs(np.linalg.eigvalsh(mat)))),
                'E_error_sample_max':float(np.max(np.abs(e-1))),
                'F_normalized_error_sample_max':float(np.max(np.abs(f/a))),
                'G_error_sample_max':float(np.max(np.abs(gg/(a*a)-1))),
                'endpoint_two_jet_matching_sample_max':float(np.max(np.abs(jets-expected))),
                'radius_range':[float(g['a'].min()),float(g['a'].max())],
                'radius_derivative_range':[float(g['ap'].min()),float(g['ap'].max())],
                'radius_second_derivative_range':[float(g['app'].min()),float(g['app'].max())],
                'min_area_density_sample':float(np.sqrt(det).min()),
                'min_section_turning_speed_sample':float(curve_k.min()),
                'max_abs_principal_curvature_sample':float(curvature.max()),
                'signed_frenet_angle_range':[float(psi.min()),float(psi.max())],
                'coordinate_min':g['x'].min(axis=(0,1)).tolist(),
                'coordinate_max':g['x'].max(axis=(0,1)).tolist(),
                'continuous_error_bound':False,'embeddedness_checked':False,'reach_proved':False}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--radial-free',type=int,default=3)
    p.add_argument('--modes',type=int,default=4)
    p.add_argument('--angular',type=int,default=40)
    p.add_argument('--radial-gauss',type=int,default=4)
    p.add_argument('--inlet-angles',type=int,default=128)
    p.add_argument('--inlet-s',type=float,default=.15)
    p.add_argument('--inlet-state')
    p.add_argument('--core-profile',choices=['mixed','ellipse'],default='mixed')
    p.add_argument('--ellipse-major',type=float,default=1.)
    p.add_argument('--ellipse-minor',type=float,default=.3)
    p.add_argument('--amp2',type=float,default=.25)
    p.add_argument('--amp3',type=float,default=.2)
    p.add_argument('--curvature',type=float,default=.6)
    p.add_argument('--length',type=float,default=1.2)
    p.add_argument('--cut-radius',type=float,default=.6)
    p.add_argument('--flat-start',type=float,default=.34)
    p.add_argument('--cuff-radius',type=float,default=.3)
    p.add_argument('--tail-plus',type=float,default=.3)
    p.add_argument('--tail-minus',type=float,default=.15)
    p.add_argument('--tail-plus-min',type=float,default=-1.3)
    p.add_argument('--tail-minus-min',type=float,default=-1.3)
    p.add_argument('--tail-angle-max',type=float,default=1.3)
    p.add_argument('--tail-height',type=float)
    p.add_argument('--tail-height-min',type=float,default=.2)
    p.add_argument('--tail-height-max',type=float,default=1.8)
    p.add_argument('--background',choices=['unit','folded','inward','hermite'],default='unit')
    p.add_argument('--beta-wiggle',type=float,default=0.)
    p.add_argument('--fold-min',type=float,default=-.2)
    p.add_argument('--fold-first-fraction',type=float,default=.33)
    p.add_argument('--inward-overshoot',type=float,default=.2)
    p.add_argument('--inward-first-fraction',type=float,default=.7)
    p.add_argument('--design-metric',action=argparse.BooleanOptionalAction,default=True)
    p.add_argument('--radius-floor',type=float,default=.3)
    p.add_argument('--radius-ceiling',type=float,default=1.8)
    p.add_argument('--radius-weight',type=float,default=20.)
    p.add_argument('--quadrature',type=int,default=48)
    p.add_argument('--max-nfev',type=int,default=100)
    p.add_argument('--warm')
    p.add_argument('--out',required=True)
    args=p.parse_args()
    if not 0<args.cuff_radius<args.flat_start<args.cut_radius:
        p.error('Need cuff_radius < flat_start < cut_radius')
    if args.core_profile=='ellipse' and args.inlet_state:
        p.error('The exact ellipse inlet does not accept a mixed-mode --inlet-state')
    started=time.perf_counter()
    prob=Problem(args)
    gl,_=np.polynomial.legendre.leggauss(args.radial_gauss)
    breaks=np.linspace(0,1,args.radial_free+2)
    radial=np.concatenate([lo+(hi-lo)*(gl+1)/2 for lo,hi in zip(breaks[:-1],breaks[1:])])
    grid=prob.prepare(radial,args.angular)
    seed=prob.seed()
    if args.warm:
        previous=json.loads(Path(args.warm).read_text())
        oldj=previous['discretization']['radial_free']
        oldk=2*previous['discretization']['modes']+1
        old=np.asarray(previous['coefficients'])
        oldnp=3*oldj*oldk
        oldxyz=old[:oldnp].reshape(3,oldj,oldk)
        oldknots=np.r_[np.zeros(6),np.arange(1,oldj+1)/(oldj+1),np.ones(6)]
        sample=np.linspace(0,1,max(101,8*(oldj+args.radial_free)))
        oldr=BSpline(oldknots,np.eye(oldj+6),5)(sample)[:,3:-3]
        newr=prob.radial(sample)
        transfer=np.linalg.lstsq(newr,oldr,rcond=None)[0]
        newxyz=np.zeros((3,prob.J,prob.K))
        keep=min(oldk,prob.K)
        newxyz[:,:,:keep]=np.einsum('ij,cjk->cik',transfer,oldxyz[:,:,:keep])
        seed[:prob.np]=newxyz.ravel()
        if prob.na and previous['definition']['design_metric']:
            seed[prob.np:prob.np+prob.na]=transfer@old[oldnp:oldnp+oldj]
        seed[-4:]=old[-4:]
    lower=np.full(prob.size,-4.)
    upper=np.full(prob.size,4.)
    if prob.na:
        lower[prob.np:prob.np+prob.na]=-.5
        upper[prob.np:prob.np+prob.na]=.5
    lower[-4:]=[args.tail_plus_min,args.tail_minus_min,-.6,args.tail_height_min]
    upper[-4:]=[args.tail_angle_max,args.tail_angle_max,.6,args.tail_height_max]
    seed=np.maximum(np.minimum(seed,upper-1e-10),lower+1e-10)
    first=prob.residual(seed,grid)
    progress={'last':time.perf_counter(),'calls':0}
    def fun(z):
        r=prob.residual(z,grid)
        progress['calls']+=1
        if time.perf_counter()-progress['last']>15:
            print(json.dumps({'event':'iterate','calls':progress['calls'],
                              'rms':float(np.sqrt(np.mean(r*r))),'tail':z[-4:].tolist()}),flush=True)
            progress['last']=time.perf_counter()
        return r
    fit=least_squares(fun,seed,jac=lambda z:prob.jacobian(z,grid),bounds=(lower,upper),
                      max_nfev=args.max_nfev,x_scale='jac',ftol=2e-10,xtol=2e-10,gtol=2e-10)
    final=prob.residual(fit.x,grid)
    payload={'status':'finite_design_bvp_candidate_not_an_exact_connector',
             'task_complete':False,'closed_surface':False,'double_circular_collars':False,
             'exact_isometry_proved':False,'same_metric_refinement':False,
             'definition':{'core':('exact elliptic cylindrical inlet' if prob.core_profile=='ellipse'
                                   else 'R2 mixed-mode GC inlet'),
                           'core_profile':prob.core_profile,
                           'ellipse_major':args.ellipse_major,'ellipse_minor':args.ellipse_minor,
                           'amp2':args.amp2,'amp3':args.amp3,
                           'curvature':args.curvature,'inlet_s':args.inlet_s,'length':args.length,
                           'tail_cut_radius':args.cut_radius,'tail_flat_start':args.flat_start,
                           'tail_cuff_radius':args.cuff_radius,'design_metric':args.design_metric,
                           'background':args.background,
                           'reference_control':prob.reference.control if prob.reference else None,
                           'beta_wiggle':args.beta_wiggle,
                           'fold_min':args.fold_min,'fold_first_fraction':args.fold_first_fraction,
                           'inward_overshoot':args.inward_overshoot,
                           'inward_first_fraction':args.inward_first_fraction,
                           'tail_height_bounds':[args.tail_height_min,args.tail_height_max],
                           'tail_lower_bounds':[args.tail_plus_min,args.tail_minus_min],
                           'tail_angle_upper_bound':args.tail_angle_max,
                           'tail_angle_shift':-np.pi/2,
                           'tail_final':dict(zip(('A_plus','A_minus','C_y','C_z'),fit.x[-4:].tolist()))},
             'discretization':{'radial_free':args.radial_free,'modes':args.modes,
                               'angular':args.angular,'radial_gauss':args.radial_gauss,
                               'inlet_angles':args.inlet_angles,'unknowns':prob.size,
                               'residuals':len(final),'tail_quadrature':args.quadrature},
             'inlet':prob.inlet_report,'inlet_solver':prob.inlet_solver,
             'reference_geometry':prob.reference.diagnostics() if prob.reference else None,
             'solver':{'success':bool(fit.success),'status':fit.status,'message':fit.message,
                       'nfev':fit.nfev,'njev':fit.njev,'optimality':float(fit.optimality),
                       'initial_rms':float(np.sqrt(np.mean(first*first))),
                       'final_rms':float(np.sqrt(np.mean(final*final))),
                       'initial_max':float(np.max(np.abs(first))),
                       'final_max':float(np.max(np.abs(final))),
                       'elapsed_seconds':time.perf_counter()-started},
             'audits':[prob.audit(fit.x,41,128),prob.audit(fit.x,81,256)],
             'coefficients':fit.x.tolist(),
             'limitations':['Finite residual is not an exact connector or a closed surface.',
                            'Metric controls were designed; this is not fixed-g refinement.',
                            'Mixed inlet uses numerical GC jets; ellipse inlet uses analytic elliptic-cylinder jets; tail uses its stated quadrature.',
                            'No continuous embeddedness or reach certificate is claimed.'],
             'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    out=Path(args.out);out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(payload,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'out':str(out),'success':bool(fit.success),'rms':payload['solver']['final_rms'],
                      'fine_metric':payload['audits'][-1]['relative_metric_operator_sample_max'],
                      'endpoint_jets':payload['audits'][-1]['endpoint_two_jet_matching_sample_max'],
                      'tail':payload['definition']['tail_final'],
                      'seconds':payload['solver']['elapsed_seconds']}),flush=True)


if __name__=='__main__':
    main()
