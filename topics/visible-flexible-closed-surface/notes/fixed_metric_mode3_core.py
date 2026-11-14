#!/usr/bin/env python3
"""Exact arclength planar support-function inlet for integer rotational symmetry.

For base_mode=3 and no corrections this is the constant-width curve
h(phi)=1+q*cos(3phi), theta=phi-(8q/3)*sin(3phi), perimeter 2pi.
Higher support coefficients are optional design variables. Even frequencies
change width, and their presence is explicitly reported. No closed-surface claim.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import argparse,json,math
from pathlib import Path
import numpy as np

class PlanarSupportCore:
    def __init__(self,q=.01,corrections=(),base_mode=3,arc_nodes=8192):
        if int(base_mode)!=base_mode or base_mode<2:
            raise ValueError('Base mode must be an integer at least 2')
        if not np.isfinite(q) or q<0:
            raise ValueError('Core support amplitude must be nonnegative')
        self.base_mode=int(base_mode);self.support_amplitude=float(q)
        self.corrections=tuple(float(c) for c in corrections)
        self.coefficients=np.r_[q,np.asarray(corrections,float)]
        self.frequencies=self.base_mode*np.arange(1,len(self.coefficients)+1)
        self.a0=1.;self.arc_nodes=max(int(arc_nodes),64*len(self.coefficients))
        phi=2*np.pi*np.arange(self.arc_nodes)/self.arc_nodes
        geom=self.normal_geometry(phi);rho=geom['rho']
        derivative_bound=float(np.sum(abs(self.frequencies*(1-self.frequencies**2)*self.coefficients)))
        slack=math.pi/self.arc_nodes*derivative_bound
        self.rho_min_sample=float(rho.min());self.rho_max_sample=float(rho.max())
        self.rho_lower=float(rho.min()-slack);self.rho_upper=float(rho.max()+slack)
        if len(self.coefficients)==1:
            self.rho_lower=1-(self.base_mode**2-1)*abs(q)
            self.rho_upper=1+(self.base_mode**2-1)*abs(q)
        if self.rho_lower<=1e-8:
            raise FloatingPointError('Support core convexity is not verified: lower rho '+str(self.rho_lower))
        self.minimum_sampled_curvature=1/self.rho_max_sample
        self.maximum_sampled_curvature=1/self.rho_min_sample
        self.curvature_upper_bound=1/self.rho_lower
        self.curvature_lower_bound=1/self.rho_upper
        even=self.frequencies%2==0
        self.constant_width_exact=not np.any(self.coefficients[even]!=0)
        self.width_defect_bound=float(2*np.sum(abs(self.coefficients[even])))
        width=2+2*(np.cos(phi[:,None]*self.frequencies[None,even])@self.coefficients[even])
        self.width_min_sample=float(width.min());self.width_max_sample=float(width.max())
        self.radius_max_sample=float(np.linalg.norm(geom['F'][:,:2],axis=1).max())
        self.radius_min_sample=float(np.linalg.norm(geom['F'][:,:2],axis=1).min())
        odd_index=np.arange(1,len(self.coefficients)+1)%2==1
        self.phase_support_gap_at_phi0=float(2*abs(np.sum(self.coefficients[odd_index])))
        self.phase_support_gap_lower=float(max(0,2*abs(q)-2*np.sum(abs(self.coefficients[1:][odd_index[1:]]))))
        self.support_monotone=float(q-np.sum(np.arange(2,len(self.coefficients)+1)**2*abs(self.coefficients[1:])))>0
        self.radius_upper_bound=float(1+np.sum(self.coefficients) if self.support_monotone else 1+np.sum(abs(self.coefficients)))
        self.radius_lower_bound=float(1+np.sum((-1.)**np.arange(1,len(self.coefficients)+1)*self.coefficients) if self.support_monotone else 1-np.sum(abs(self.coefficients)))

    def normal_geometry(self,phi):
        phi=np.asarray(phi,dtype=float)
        angle=phi[...,None]*self.frequencies
        co=np.cos(angle);si=np.sin(angle);c=self.coefficients;m=self.frequencies
        h=1+co@c;hp=-si@(m*c);hpp=-co@(m*m*c)
        rho=h+hpp
        er=np.stack((np.cos(phi),np.sin(phi),np.zeros_like(phi)),axis=-1)
        et=np.stack((-np.sin(phi),np.cos(phi),np.zeros_like(phi)),axis=-1)
        F=h[...,None]*er+hp[...,None]*et
        return dict(F=F,h=h,hp=hp,rho=rho,er=er,et=et)

    def arc(self,phi):
        phi=np.asarray(phi,dtype=float)
        return phi+np.sin(phi[...,None]*self.frequencies)@((1-self.frequencies**2)*self.coefficients/self.frequencies)

    def evaluate(self,theta):
        theta=np.asarray(theta,dtype=float);phi=theta.copy()
        period=2*np.pi/self.base_mode
        lo=np.floor(theta/period)*period;hi=lo+period
        residual=np.zeros_like(theta)
        for it in range(80):
            g=self.normal_geometry(phi);residual=self.arc(phi)-theta
            done=abs(residual)<=8*np.finfo(float).eps*np.maximum(1,abs(theta))
            if np.all(done):break
            lo=np.where((residual<0)&~done,phi,lo);hi=np.where((residual>0)&~done,phi,hi)
            new=phi-residual/g['rho']
            bad=(new<=lo)|(new>=hi)|~np.isfinite(new)
            new=np.where(bad,(lo+hi)/2,new);phi=np.where(done,phi,new)
        g=self.normal_geometry(phi)
        residual=self.arc(phi)-theta
        if np.max(abs(residual))>3e-13*max(1,float(np.max(abs(theta)))):
            raise FloatingPointError('Arc inversion did not converge')
        return dict(F=g['F'],Ft=g['et'],Ftt=-g['er']/g['rho'][...,None],
                    phi=phi,kappa=1/g['rho'],arc_residual=residual,
                    arc_iterations=it+1)

    def parameter_derivatives(self,theta):
        """dF/dc at fixed arclength, including the moving normal-angle frame."""
        g=self.evaluate(theta);phi=g['phi'];m=self.frequencies[:,None]
        er=np.stack((np.cos(phi),np.sin(phi),np.zeros_like(phi)),axis=-1)
        et=np.stack((-np.sin(phi),np.cos(phi),np.zeros_like(phi)),axis=-1)
        return np.cos(m*phi[None,:])[:,:,None]*er[None,:,:]-(np.sin(m*phi[None,:])/m)[:,:,None]*et[None,:,:]

    def inlet(self,obj,angular=2048):
        theta=2*np.pi*np.arange(angular)/angular;g=self.evaluate(theta)
        B,B1,B2=obj.basis(angular);C=obj.project(g['F'][None,:,:],B)[:,0]
        pos=obj.values(C[:,None],B)[0];first=obj.values(C[:,None],B1)[0];second=obj.values(C[:,None],B2)[0]
        metric=np.sum(first*first,axis=1)-1
        return C,dict(core_kind='planar_support',base_mode=self.base_mode,
            support_amplitude=self.support_amplitude,corrections=list(self.corrections),
            exact_perimeter=2*math.pi,constant_width_exact=self.constant_width_exact,
            width_defect_bound=self.width_defect_bound,width_min_sample=self.width_min_sample,width_max_sample=self.width_max_sample,
            curvature_radius_lower=self.rho_lower,curvature_radius_upper=self.rho_upper,
            curvature_upper_bound=self.curvature_upper_bound,
            coordinate_projection_error=float(np.linalg.norm(pos-g['F'],axis=1).max()),
            first_jet_projection_error=float(np.linalg.norm(first-g['Ft'],axis=1).max()),
            second_jet_projection_error=float(np.linalg.norm(second-g['Ftt'],axis=1).max()),
            metric_projection_error=float(abs(metric).max()),
            metric_projection_l1=float(np.sum(abs(np.fft.fft(metric)/angular))),
            exact_arclength_metric_error=float(abs(np.sum(g['Ft']**2,axis=1)-1).max()),
            arc_inversion_residual=float(abs(g['arc_residual']).max()),arc_iterations=g['arc_iterations'],
            radial_fundamental=float(C[1]),vertical_coefficients_max=float(abs(C[obj.iz:]).max()),
            minimum_sampled_curvature=self.minimum_sampled_curvature,
            maximum_sampled_curvature=self.maximum_sampled_curvature,
            initial_speed_limit=self.curvature_lower_bound,
            initial_speed_limit_sample=self.minimum_sampled_curvature,
            radius_max_sample=self.radius_max_sample,radius_min_sample=self.radius_min_sample,
            radius_upper_bound=self.radius_upper_bound,radius_lower_bound=self.radius_lower_bound,support_monotone=self.support_monotone,
            phase_pi_over_base_mode_support_gap_at_phi0=self.phase_support_gap_at_phi0,phase_pi_over_base_mode_support_gap_lower=self.phase_support_gap_lower)

    def summary(self):
        return dict(base_mode=self.base_mode,support_amplitude=self.support_amplitude,
            coefficients=self.coefficients.tolist(),frequencies=self.frequencies.tolist(),
            exact_perimeter=2*math.pi,constant_width_exact=self.constant_width_exact,
            width_defect_bound=self.width_defect_bound,width_min_sample=self.width_min_sample,width_max_sample=self.width_max_sample,
            curvature_radius_lower=self.rho_lower,curvature_radius_upper=self.rho_upper,
            curvature_lower_bound=self.curvature_lower_bound,curvature_upper_bound=self.curvature_upper_bound,
            radius_max_sample=self.radius_max_sample,radius_min_sample=self.radius_min_sample,
            radius_upper_bound=self.radius_upper_bound,radius_lower_bound=self.radius_lower_bound,support_monotone=self.support_monotone,
            phase_pi_over_base_mode_support_gap_at_phi0=self.phase_support_gap_at_phi0,phase_pi_over_base_mode_support_gap_lower=self.phase_support_gap_lower)


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source-root',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--amplitudes',type=float,nargs='+',default=[.001,.01,.03,.05,.075,.10]);p.add_argument('--modes',type=int,nargs='+',default=[4,8,12,16,24,32,48,64]);a=p.parse_args()
    import sys
    sys.path.insert(0,str(a.source_root/'topics/large-amplitude-twist-flex/scripts'))
    from curve_stable_prefix_bvp import CylindricalPrefix
    from types import SimpleNamespace
    rows=[]
    for q in a.amplitudes:
        core=PlanarSupportCore(q)
        for M in a.modes:
            # Only the general basis/project methods are used; no reflected-core
            # initializer or its mode-class guard is changed or invoked.
            obj=SimpleNamespace(M=M,n=3*M+1,iz=2*M+1,even=3*np.arange(1,M+1))
            obj.basis=lambda N,o=obj:CylindricalPrefix.basis(o,N)
            obj.project=CylindricalPrefix.project;obj.values=CylindricalPrefix.values
            C,metrics=core.inlet(obj,max(2048,64*M))
            rows.append(dict(modes=M,**metrics))
        print(json.dumps({k:v for k,v in rows[-1].items() if k in ['modes','support_amplitude','metric_projection_error','second_jet_projection_error','curvature_upper_bound','coordinate_projection_error']}),flush=True)
    a.out.write_text(json.dumps(dict(scope=__doc__,rows=rows),indent=2)+'\n')

if __name__=='__main__':main()
