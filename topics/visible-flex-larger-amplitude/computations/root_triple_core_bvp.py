#!/usr/bin/env python3
"""Three prescribed core harmonics with three genuine meridian controls.

The first support coefficient q, the existing q4 law, and --third-support
(frequency 6) are prescribed. Delta, boost_length, and boost_speed are
unknown physical design controls. Modes 8 and higher remain core unknowns.
A successful output is a finite linear-DN prefix; it is neither a fixed-g
refinement nor a closed surface. A successful prior checkpoint is required
as an explicitly deformed initial guess.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import math
from pathlib import Path
import sys
import numpy as np
import root_radial_batching as radial

HERE=Path(__file__).resolve().parent


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);sys.modules[name]=obj
    spec.loader.exec_module(obj);return obj


def main():
    parser=argparse.ArgumentParser(add_help=False)
    parser.add_argument('--third-support',type=float,required=True)
    options,remaining=parser.parse_known_args()
    if '--restart' not in remaining:
        raise ValueError('A saved solved prefix is required as the design initial guess')
    if '--second-control' in remaining:
        if remaining[remaining.index('--second-control')+1]!='boost_length':
            raise ValueError('The three controls are delta, boost_length, boost_speed')
    else:
        remaining+=['--second-control','boost_length']
    if '--newton-backend' not in remaining:
        remaining+=['--newton-backend','refresh']
    root=module('root_triple_dual',HERE/'root_dual_core_bvp.py')
    original=root.make_dual

    def make_triple(adaptive,charts,chart,secondary_law='linear',secondary_scale=.2,
                    meridian_chart='all-knots',second_control='boost_length'):
        Base=original(adaptive,charts,chart,secondary_law,secondary_scale,meridian_chart,second_control)
        Flow,_=adaptive.build_classes(chart)
        from fixed_metric_mode3_core import PlanarSupportCore
        from fixed_metric_mode3_bvp import merge_profile_mesh

        class Triple(Base):
            control_names=('delta','boost_length','boost_speed')

            def __init__(self,cfg,port,q,M,angular):
                if cfg.get('ramp_law')!='hermite_boost_neck' or M<4:
                    raise ValueError('The triple-core design requires a finite neck and M>=4')
                q4=-q/(10*math.sqrt(2)) if secondary_law=='linear' else -secondary_scale*q*q
                self.prescribed=np.array([q,q4,options.third_support],float)
                self.ref_frequencies=[2,4,6]
                super().__init__(cfg,port,q,M,angular)
                self.ref_coeff=self.prescribed.copy()
                self._core_key=None;self._initial=None
                self._special_layout='p0=delta offset; p1=boost_length offset; p2=boost_speed offset; p3..=support modes 8,10,...'
                self.design_provenance=dict(
                    controls=list(self.control_names),prescribed_support=self.prescribed.tolist(),
                    prescribed_frequencies=self.ref_frequencies,
                    adapter_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                    radial_batching_sha256=hashlib.sha256((HERE/'root_radial_batching.py').read_bytes()).hexdigest(),
                    radial_batch_size=48,
                    scope=__doc__)

            def make_flow(self,*args,**kwargs):
                kwargs.pop('warp_q',None)
                flow=Flow(*args,warp_q=0.,**kwargs)
                charts.attach_to_adaptive_flow(flow,self.prescribed,self.ref_frequencies,reference='core-blend')
                if hasattr(flow.bridge,'breakpoints'):
                    flow.breaks=np.unique(np.r_[flow.breaks,flow.prefix_end+flow.bridge.breakpoints])
                return flow

            def flow(self,p0):
                key=tuple(float(x) for x in self.controls[:3])
                key=(float(p0),)+key[1:]
                if self._flow_key!=key:
                    physical={**self.cfg,**{name:self.cfg[name]+key[j] for j,name in enumerate(self.control_names)}}
                    if not(.002<physical['delta']<1 and physical['boost_length']>0
                           and .03<physical['boost_speed']<1 and .03<physical['vd']<1):
                        raise FloatingPointError('Triple meridian design left its physical domain')
                    try:
                        self._flow=self.Flow(physical,self.port,self.M,self.q,self.nt,self.base_mode,self.bridge)
                    except ValueError as exc:
                        raise FloatingPointError('Invalid physical triple-design profile: '+str(exc)) from exc
                    self._flow_key=key
                return self._flow

            def initial(self,p):
                self.select(p)
                key=tuple(np.asarray(p[3:],float))
                if key!=self._core_key:
                    corrections=np.zeros(self.M-1)
                    corrections[:2]=self.prescribed[1:]
                    corrections[2:]=np.asarray(p[3:])*self.pscale[2:]
                    core=PlanarSupportCore(self.q,corrections,2)
                    f=self.flow(p[0]);N=max(2048,128*self.M)
                    gi=f.general_core_chart.inlet_geometry(N)
                    exact=core.evaluate(gi['theta']);B,B1,B2=f.basis(N)
                    self._initial=f.project((exact['F']-gi['pos'])[None,:,:],B)[:,0]/self.q
                    J=f.project(core.parameter_derivatives(gi['theta']),B)
                    self._initial_jac=np.zeros((self.n,self.M))
                    self._initial_jac[:,3:]=J[:,3:]*self.pscale[None,2:]/self.q
                    first=gi['p1']+self.q*f.values(self._initial[:,None],B1)[0]
                    second=gi['p2']+self.q*f.values(self._initial[:,None],B2)[0]
                    mapped=gi['pos']+self.q*f.values(self._initial[:,None],B)[0]
                    true1=exact['Ft']*gi['rho'][:,None]
                    true2=exact['Ftt']*gi['rho'][:,None]**2+exact['Ft']*gi['rhop'][:,None]
                    error=np.sum(first*first,axis=1)/gi['rho']**2-1
                    self._inlet_metrics=dict(position=float(np.linalg.norm(mapped-exact['F'],axis=1).max()),
                        first=float(np.linalg.norm(first-true1,axis=1).max()),
                        second=float(np.linalg.norm(second-true2,axis=1).max()),
                        metric_l1=float(np.sum(abs(np.fft.fft(error)/N))))
                    self._core=core;self._core_key=key;self.support_amplitude=self.q
                return self._initial

            def fun(self,t,y,p):
                self.select(p);f=self.flow(p[0]);s,ds=self.chart(t,p[0])
                return ds[None,:]*radial.value(f,s,y,p)

            def fun_jac(self,t,y,p):
                self.select(p);f=self.flow(p[0]);s,ds=self.chart(t,p[0])
                J=radial.state_jacobian(f,s,y,p);PJ=np.zeros((self.n,self.M,len(t)))
                for j,name in enumerate(self.control_names):
                    step=1e-6*max(.1,abs(self.cfg[name]+p[j]))
                    plus=p.copy();minus=p.copy();plus[j]+=step;minus[j]-=step
                    PJ[:,j]=(self.fun(t,y,plus)-self.fun(t,y,minus))/(2*step)
                self.select(p);self.flow(p[0])
                return ds[None,None,:]*J,PJ

            def bc_jac(self,ya,yb,p):
                self.select(p);self.initial(p);f=self.flow(p[0])
                A=np.zeros((self.n+self.M,self.n));A[:self.n]=np.eye(self.n)
                B=np.zeros_like(A);P=np.zeros((self.n+self.M,self.M));P[:self.n]=-self._initial_jac
                J,_=f.fun_jac(np.array([f.end]),np.asarray(yb,np.longdouble)[:,None],p)
                T=self.q*J[self.iz:,:,0]
                T[:,self.iz:]-=self.q*self.bridge.sigma*self.Dmatrix/math.sqrt(self.port['cut']['E'])
                B[self.n:]=T/self.bcweights[:,None]
                for j,name in enumerate(self.control_names):
                    step=2e-6*max(.1,abs(self.cfg[name]+p[j]))
                    plus=p.copy();minus=p.copy();plus[j]+=step;minus[j]-=step
                    P[:,j]=(self.bc(ya,yb,plus)-self.bc(ya,yb,minus))/(2*step)
                self.select(p);self.flow(p[0]);self.initial(p)
                return A,B,P

            def restart_from(self,saved,pullback,nodes,scale='linear'):
                old=saved.rec;oldcfg=old['frozen_profile']
                if not old.get('solver_success',False):
                    raise ValueError('Triple design must start from a successfully solved checkpoint')
                for key in sorted((set(oldcfg)|set(self.cfg))-set(self.control_names)):
                    if oldcfg.get(key)!=self.cfg.get(key):
                        raise ValueError('Uncontrolled physical profile changed: '+key)
                p=np.zeros(self.M)
                for j,name in enumerate(self.control_names):p[j]=oldcfg[name]-self.cfg[name]
                ratio=self.q/saved.q;coeff=np.asarray(old['core']['coefficients'])
                for j in range(3,min(self.M,len(coeff))):
                    exponent=j+1 if secondary_law=='quadratic' else math.ceil((j+1)/2)
                    p[j]=coeff[j]*(ratio**exponent if scale=='linear' else 1.)/self.pscale[j-1]
                self.select(p);f=self.flow(p[0])
                if abs(f.end-saved.flow.end)>2e-12*max(1.,f.end):
                    raise ValueError('Initial design profile length unexpectedly changed')
                grid=(self.inverse_chart(np.asarray(saved.sol.x),p[0]) if nodes<=0
                      else np.linspace(0,1,nodes))
                t=merge_profile_mesh(grid,self.chart_breaks)
                s,_=self.chart(t,p[0])
                arrays,record=pullback.convert(saved,f.general_core_chart,self.M,self.q,s,
                    angular=max(512,32*(2*self.M+1)),height_angular=128)
                y=arrays['y']
                if scale=='linear':
                    N=max(512,32*(2*self.M+1));g=f.geo(s,N);theta=g['theta']
                    radial=np.stack((np.cos(theta),np.sin(theta),np.zeros_like(theta)),axis=-1)
                    background=f.profile(s)[0][:,None,None]*radial;B,_,_=f.basis(N)
                    y=ratio*y+(ratio-1)*f.project(g['pos']-background,B)/self.q
                correction=self.initial(p)-y[:,0]
                y+=correction[:,None]*np.maximum(0,1-s/(f.Tu/2))[None,:]**3
                record.update(amplitude_scaling=scale,amplitude_ratio=ratio,
                    previous_support=coeff.tolist(),prescribed_support=self.prescribed.tolist(),
                    boundary_correction_max=float(abs(correction).max()),
                    design_controls=list(self.control_names),
                    height_mean_disposition='Preserved conversion mean is recorded; after the inlet/shape warm deformation, the new BVP integrates its own physical mean velocity.',
                    final_scope='Three-control design initial guess only; a fresh nonlinear BVP is required.')
                return t,y,p,record

        return Triple

    root.make_dual=make_triple
    sys.argv=[sys.argv[0]]+remaining
    root.main()


if __name__=='__main__':
    main()
