#!/usr/bin/env python3
"""Unit-speed planar core defined by tangent angle phi(theta).

phi(theta)=theta+sum_j b_j sin(m*j*theta), gamma_theta=i exp(i phi).
For integer m>=2 all Fourier frequencies are 1 mod m, so the mean tangent
vanishes and the curve closes exactly. If sum m*j*|b_j|<1 it is strictly
convex. q_eff is m*b_1/(m*m-1), a first-order radial amplitude, NOT a support
coefficient. Bessel convolution gives the antiderivative and its Jacobian.
"""
import os
for n in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[n]='1'
import argparse,json,math,sys
from pathlib import Path
import numpy as np
from scipy.special import jv

class PlanarTangentCore:
    def __init__(self,q=.01,corrections=(),base_mode=3,arc_nodes=2048):
        self.base_mode=int(base_mode)
        if self.base_mode<2 or self.base_mode!=base_mode:raise ValueError('Integer base mode >=2 required')
        self.q_eff=float(q);self.support_amplitude=self.q_eff # Internal legacy interface only; reports rename this quantity.
        self.primary_to_angle=(self.base_mode**2-1)/self.base_mode
        self.corrections=tuple(float(x)for x in corrections)
        self.coefficients=np.r_[self.primary_to_angle*q,np.asarray(corrections,float)]
        self.frequencies=self.base_mode*np.arange(1,len(self.coefficients)+1)
        self.a0=1.;self.arc_nodes=max(1024,int(arc_nodes))
        l1lo=float(1-np.sum(self.frequencies*abs(self.coefficients)))
        l1hi=float(1+np.sum(self.frequencies*abs(self.coefficients)))
        grid=2*np.pi*np.arange(max(4096,self.arc_nodes))/max(4096,self.arc_nodes)
        ks=1+np.cos(grid[:,None]*self.frequencies)@(self.frequencies*self.coefficients)
        allowance=math.pi/len(grid)*float(np.sum(self.frequencies**2*abs(self.coefficients)))
        self.curvature_lower_bound=max(l1lo,float(ks.min()-allowance))
        self.curvature_upper_bound=min(l1hi,float(ks.max()+allowance))
        if self.curvature_lower_bound<=1e-7:raise FloatingPointError('Tangent-angle convexity bound is nonpositive')
        self.rho_lower=1/self.curvature_upper_bound;self.rho_upper=1/self.curvature_lower_bound
        # Jacobi-Anger coefficients. The l1 norm of exp(i*b*sin) is <=exp(|b|).
        # The retained Bessel tail is bounded by its defining factorial series.
        A=np.array([1.]);offset=0;tail_error=0.;self.bessel_cutoffs=[]
        total_angle=float(np.sum(abs(self.coefficients)))
        target=2e-20/max(1,len(self.coefficients))/math.exp(total_angle)
        for j,b in enumerate(self.coefficients,start=1):
            if b==0:self.bessel_cutoffs.append(0);continue
            x=abs(b)/2;K=max(0,int(x));bound=math.inf
            while bound>target:
                if K+2>x:
                    bound=2*math.exp(b*b/4+(K+1)*math.log(x)-math.lgamma(K+2))/(1-x/(K+2))
                if bound>target:K+=1
            ks=np.arange(-K,K+1);B=np.zeros(2*j*K+1);B[j*(ks+K)]=jv(ks,b)
            A=np.convolve(A,B);offset+=j*K;tail_error+=bound
            self.bessel_cutoffs.append(K)
        self.phase_indices=np.arange(-offset,offset+1,dtype=int);self.phase_coefficients=A
        self.spectral_tail_bound=float(math.exp(total_angle)*tail_error)
        self.coordinate_frequencies=1+self.base_mode*self.phase_indices
        if np.any(self.coordinate_frequencies==0):raise AssertionError('Rotational symmetry lost closure')
        self.coordinate_coefficients=A/self.coordinate_frequencies
        self.radius_upper_bound=float(np.sum(abs(self.coordinate_coefficients))+self.spectral_tail_bound)
        at0=float(self.coordinate_coefficients[offset])
        self.radius_lower_bound=float(abs(at0)-(np.sum(abs(self.coordinate_coefficients))-abs(at0))-self.spectral_tail_bound)
        odd=self.phase_indices%2!=0
        self.phase_support_gap_at_phi0=float(2*abs(np.sum(self.coordinate_coefficients[odd])))
        self.phase_support_gap_lower=max(0,self.phase_support_gap_at_phi0-2*self.spectral_tail_bound)
        theta=2*np.pi*np.arange(self.arc_nodes)/self.arc_nodes;g=self.evaluate(theta)
        self.minimum_sampled_curvature=float(g['kappa'].min());self.maximum_sampled_curvature=float(g['kappa'].max())
        radii=np.linalg.norm(g['F'][:,:2],axis=1);self.radius_min_sample=float(radii.min());self.radius_max_sample=float(radii.max())
        # Width is sampled at uniform normal angles with a rigorous analytic
        # second-derivative interpolation allowance (floating error not enclosed).
        normals=2*np.pi*np.arange(self.arc_nodes)/self.arc_nodes
        inverse=self.invert_normal(np.r_[normals,normals+np.pi]);z=self.evaluate(inverse)['F'][:,:2]
        normal_vec=np.c_[np.cos(np.r_[normals,normals+np.pi]),np.sin(np.r_[normals,normals+np.pi])]
        h=np.sum(z*normal_vec,axis=1);width=h[:self.arc_nodes]+h[self.arc_nodes:]
        self.width_min_sample=float(width.min());self.width_max_sample=float(width.max())
        second_bound=2/self.curvature_lower_bound+2*self.radius_upper_bound
        self.width_sampling_allowance=float(second_bound*(2*np.pi/self.arc_nodes)**2/8+2*self.spectral_tail_bound)
        self.width_defect_bound=float(max(abs(width-2))+self.width_sampling_allowance)
        self.constant_width_exact=bool(np.all(self.coefficients==0))
        self.support_monotone=None
        self._jac_coefficients=None

    def angle(self,theta):
        theta=np.asarray(theta,float);phase=theta[...,None]*self.frequencies
        phi=theta+np.sin(phase)@self.coefficients
        kappa=1+np.cos(phase)@(self.frequencies*self.coefficients)
        return phi,kappa

    def invert_normal(self,phi):
        phi=np.asarray(phi,float);theta=phi.copy();period=2*np.pi/self.base_mode
        lo=np.floor(phi/period)*period;hi=lo+period
        for it in range(64):
            value,k=self.angle(theta);r=value-phi;done=abs(r)<=8*np.finfo(float).eps*np.maximum(1,abs(phi))
            if np.all(done):break
            lo=np.where((r<0)&~done,theta,lo);hi=np.where((r>0)&~done,theta,hi)
            new=theta-r/k;new=np.where((new<=lo)|(new>=hi)|~np.isfinite(new),(lo+hi)/2,new);theta=np.where(done,theta,new)
        if float(abs(self.angle(theta)[0]-phi).max())>3e-13*max(1,float(abs(phi).max())):raise FloatingPointError('Normal-angle inverse failed')
        return theta

    @staticmethod
    def _evaluate_coefficients(theta,freq,coeff):
        theta=np.asarray(theta,float);flat=theta.ravel();z=np.empty(flat.shape,complex)
        for first in range(0,len(flat),2048):z[first:first+2048]=np.exp(1j*flat[first:first+2048,None]*freq[None,:])@coeff
        return z.reshape(theta.shape)

    def evaluate(self,theta):
        theta=np.asarray(theta,float);phi,kappa=self.angle(theta)
        z=self._evaluate_coefficients(theta,self.coordinate_frequencies,self.coordinate_coefficients)
        n=np.exp(1j*phi);t=1j*n;second=-kappa*n
        vec=lambda v:np.stack((v.real,v.imag,np.zeros_like(v.real)),axis=-1)
        return dict(F=vec(z),Ft=vec(t),Ftt=vec(second),phi=phi,kappa=kappa,
            arc_residual=np.zeros(theta.shape),arc_iterations=0)

    def parameter_coefficient_derivatives(self):
        if self._jac_coefficients is None:
            out=[];off=(len(self.phase_coefficients)-1)//2;A=self.phase_coefficients
            for j in range(1,len(self.coefficients)+1):
                ks=np.arange(-off-j,off+j+1);der=np.zeros(len(ks))
                for sign,shift in [(1,j),(-1,-j)]:
                    ix=ks-shift+off;valid=(ix>=0)&(ix<len(A));der[valid]+=sign*.5*A[ix[valid]]
                freq=1+self.base_mode*ks;der=der/freq
                if j==1:der*=self.primary_to_angle
                out.append((ks,freq,der))
            self._jac_coefficients=out
        return self._jac_coefficients

    def parameter_derivatives(self,theta):
        values=[]
        for _,freq,c in self.parameter_coefficient_derivatives():
            z=self._evaluate_coefficients(theta,freq,c);values.append(np.stack((z.real,z.imag,np.zeros_like(z.real)),axis=-1))
        return np.asarray(values)

    @staticmethod
    def cylindrical_coefficients(obj,indices,values):
        out=np.zeros(obj.n);coeff=dict(zip(indices,values));out[0]=coeff.get(0,0.)
        for j in range(1,obj.M+1):
            plus=coeff.get(j,0.);minus=coeff.get(-j,0.)
            out[j]=plus+minus;out[obj.M+j]=plus-minus
        return out

    def inlet_jacobian(self,obj):
        return np.column_stack([self.cylindrical_coefficients(obj,ix,c)for ix,freq,c in self.parameter_coefficient_derivatives()])

    def inlet(self,obj,angular=2048):
        theta=2*np.pi*np.arange(angular)/angular;g=self.evaluate(theta);B,B1,B2=obj.basis(angular)
        C=self.cylindrical_coefficients(obj,self.phase_indices,self.coordinate_coefficients)
        pos=obj.values(C[:,None],B)[0];first=obj.values(C[:,None],B1)[0];second=obj.values(C[:,None],B2)[0]
        metric=np.sum(first*first,axis=1)-1
        return C,dict(core_kind='planar_tangent_angle',base_mode=self.base_mode,tangent_q_eff=self.q_eff,
            angle_coefficients=self.coefficients.tolist(),corrections=list(self.corrections),exact_perimeter=2*math.pi,
            constant_width_exact=self.constant_width_exact,width_defect_bound=self.width_defect_bound,
            width_min_sample=self.width_min_sample,width_max_sample=self.width_max_sample,width_sampling_allowance=self.width_sampling_allowance,
            curvature_radius_lower=self.rho_lower,curvature_radius_upper=self.rho_upper,curvature_lower_bound=self.curvature_lower_bound,curvature_upper_bound=self.curvature_upper_bound,
            coordinate_projection_error=float(np.linalg.norm(pos-g['F'],axis=1).max()),
            first_jet_projection_error=float(np.linalg.norm(first-g['Ft'],axis=1).max()),second_jet_projection_error=float(np.linalg.norm(second-g['Ftt'],axis=1).max()),
            metric_projection_error=float(abs(metric).max()),metric_projection_l1=float(np.sum(abs(np.fft.fft(metric)/angular))),
            exact_arclength_metric_error=float(abs(np.sum(g['Ft']**2,axis=1)-1).max()),radial_fundamental=float(C[1]),
            vertical_coefficients_max=float(abs(C[obj.iz:]).max()),minimum_sampled_curvature=self.minimum_sampled_curvature,maximum_sampled_curvature=self.maximum_sampled_curvature,
            initial_speed_limit=self.curvature_lower_bound,radius_max_sample=self.radius_max_sample,radius_upper_bound=self.radius_upper_bound,
            spectral_coefficient_tail_l1_bound=self.spectral_tail_bound,phase_pi_over_base_mode_support_gap_lower=self.phase_support_gap_lower)

    def summary(self):
        return dict(core_kind='planar_tangent_angle',base_mode=self.base_mode,q_eff=self.q_eff,b1=float(self.coefficients[0]),
            coefficient_kind='tangent-angle sine',coefficients=self.coefficients.tolist(),frequencies=self.frequencies.tolist(),
            exact_perimeter=2*math.pi,constant_width_exact=self.constant_width_exact,width_defect_bound=self.width_defect_bound,
            width_min_sample=self.width_min_sample,width_max_sample=self.width_max_sample,width_sampling_allowance=self.width_sampling_allowance,
            curvature_lower_bound=self.curvature_lower_bound,curvature_upper_bound=self.curvature_upper_bound,
            radius_upper_bound=self.radius_upper_bound,radius_lower_bound=self.radius_lower_bound,radius_max_sample=self.radius_max_sample,radius_min_sample=self.radius_min_sample,
            phase_pi_over_base_mode_support_gap_lower=self.phase_support_gap_lower,phase_pi_over_base_mode_support_gap_at_phi0=self.phase_support_gap_at_phi0,
            bessel_cutoffs=self.bessel_cutoffs,spectral_coefficient_tail_l1_bound=self.spectral_tail_bound,
            tail_bound_scope='Analytic omitted Bessel coefficient bound, excluding floating-point evaluation/convolution error.')

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source-root',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    sys.path.insert(0,str(a.source_root/'topics/large-amplitude-twist-flex/scripts'))
    from curve_stable_prefix_bvp import CylindricalPrefix
    from types import SimpleNamespace
    rows=[]
    for q in [.001,.01,.04,.06,.08,.09]:
        core=PlanarTangentCore(q)
        for M in [2,4,6,8,12]:
            obj=SimpleNamespace(M=M,n=3*M+1,iz=2*M+1,even=3*np.arange(1,M+1));obj.basis=lambda N,o=obj:CylindricalPrefix.basis(o,N);obj.project=CylindricalPrefix.project;obj.values=CylindricalPrefix.values
            C,metrics=core.inlet(obj);rows.append(dict(modes=M,**metrics))
        print(json.dumps(dict(**core.summary(),projection_at_m8=rows[-2]['metric_projection_l1'])),flush=True)
    a.out.write_text(json.dumps(dict(scope=__doc__,rows=rows),indent=2)+'\n')

if __name__=='__main__':main()
