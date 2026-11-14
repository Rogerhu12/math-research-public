#!/usr/bin/env python3
"""Nonlinear two-control prefix at an m2/m4 double linear resonance.

The first support coefficient q and a specified second support coefficient
are fixed. Delta and either vd or boost_length replace the corresponding
matching constraints; higher support modes remain unknown. All
outputs are finite LINEAR-tail-DN prefixes, never complete closed surfaces.
"""
from __future__ import annotations
import os
for _k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_k]='1'
import argparse
import hashlib
import importlib.util
import json
import math
import sys
import time
import types
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.integrate import solve_bvp
from scipy.interpolate import PPoly
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec)
    sys.modules[name]=obj
    spec.loader.exec_module(obj)
    return obj


def make_dual(adaptive,chart_module,chart,secondary_law='linear',secondary_scale=.2,meridian_chart='all-knots',second_control='vd'):
    Flow,BaseBVP=adaptive.build_classes(chart)
    from fixed_metric_mode3_core import PlanarSupportCore
    from fixed_metric_mode3_bvp import merge_profile_mesh
    neck_chart=module('root_dual_multiknot_chart',HERE/'root_neck_chart.py')

    class DualBVP(BaseBVP):
        def __init__(self,cfg,port,q,M,angular):
            self.second_control=second_control
            if second_control!='vd' and cfg.get('ramp_law')!='hermite_boost_neck':
                raise ValueError('The boost-length control requires the finite-neck provider')
            self.controls=np.zeros(M)
            q4=-q/(10*math.sqrt(2)) if secondary_law=='linear' else -secondary_scale*q*q
            self.ref_coeff=np.array([q,q4])
            super().__init__(cfg,port,q,M,angular,False,0.)
            self.Flow=self.make_flow
            self._flow_key=None;self._flow=None
            self._core_key=None;self._initial=None
            self.pscale=np.maximum(q**np.arange(2,M+1),1e-9)
            self._special_layout=f'p0=delta offset; p1={second_control} offset; p2..=support modes 6,8,...'
            self._neck_knots=None
            if cfg.get('ramp_law')=='hermite_boost_neck' and meridian_chart=='all-knots':
                reference=self.flow(0.)
                self._neck_knots=np.asarray(reference.breaks)/reference.end
                self.chart_breaks=self._neck_knots.copy()
            elif hasattr(self.bridge,'breakpoints'):
                f=self.flow(0.)
                self.chart_breaks=np.unique(np.r_[self.chart_breaks,self.inverse_chart(f.prefix_end+self.bridge.breakpoints,0.)])

        def chart(self,t,p0):
            if getattr(self,'_neck_knots',None) is None:return super().chart(t,p0)
            f=self.flow(p0)
            return neck_chart.NeckChart(self._neck_knots,f.breaks).evaluate(t)

        def inverse_chart(self,s,p0):
            if getattr(self,'_neck_knots',None) is None:return super().inverse_chart(s,p0)
            f=self.flow(p0)
            return neck_chart.NeckChart(self._neck_knots,f.breaks).inverse(s)

        def make_flow(self,*args,**kwargs):
            kwargs.pop('warp_q',None)
            f=Flow(*args,warp_q=0.,**kwargs)
            chart_module.attach_to_adaptive_flow(f,self.ref_coeff,[2,4],reference='core-blend')
            if hasattr(f.bridge,'breakpoints'):
                f.breaks=np.unique(np.r_[f.breaks,f.prefix_end+f.bridge.breakpoints])
            return f

        def select(self,p):
            self.controls=np.asarray(p,float).copy()

        def flow(self,p0):
            p1=float(self.controls[1]) if hasattr(self,'controls') else 0.
            key=(float(p0),p1)
            if self._flow_key!=key:
                delta=self.cfg['delta']+key[0]
                physical={**self.cfg,'delta':delta,second_control:self.cfg[second_control]+key[1]}
                vd=physical['vd']
                # The legacy .97 speed guard is not a geometric condition.
                # A finite neck provider permits either side of loop_speed;
                # actual positive lengths, square-root and embedding domains
                # are still checked by the provider and nonlinear flow.
                vd_upper=1. if self.cfg.get('ramp_law')=='hermite_boost_neck' else .97
                if not .002<delta<1 or not .03<vd<vd_upper:
                    raise FloatingPointError(f'Dual meridian design left its physical domain: delta={delta:.17g}, vd={vd:.17g}')
                if physical.get('ramp_law')=='hermite_boost_neck' and physical['boost_length']<=0:
                    raise FloatingPointError('The physical boost length became nonpositive')
                self._flow=self.Flow(physical,self.port,
                                    self.M,self.q,self.nt,self.base_mode,self.bridge)
                self._flow_key=key
            return self._flow

        def initial(self,p):
            self.select(p)
            key=tuple(np.asarray(p[2:],float))
            if key!=self._core_key:
                corr=np.asarray(p[1:])*self.pscale
                corr[0]=self.ref_coeff[1]
                core=PlanarSupportCore(self.q,corr,2)
                f=self.flow(p[0]);N=max(2048,128*self.M)
                gi=f.general_core_chart.inlet_geometry(N)
                exact=core.evaluate(gi['theta']);B,B1,B2=f.basis(N)
                self._initial=f.project((exact['F']-gi['pos'])[None,:,:],B)[:,0]/self.q
                deriv=core.parameter_derivatives(gi['theta']);J=f.project(deriv,B)
                self._initial_jac=np.zeros((self.n,self.M))
                if self.M>2:self._initial_jac[:,2:]=J[:,2:]*self.pscale[None,1:]/self.q
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
            self.select(p)
            f=self.flow(p[0]);s,ds=self.chart(t,p[0])
            return ds[None,:]*f.fun(s,y,p)

        def fun_jac(self,t,y,p):
            self.select(p)
            f=self.flow(p[0]);s,ds=self.chart(t,p[0]);J,_=f.fun_jac(s,y,p)
            PJ=np.zeros((self.n,self.M,len(t)))
            for j in (0,1):
                step=1e-6*max(.1,abs(self.cfg['delta']+p[0]) if j==0 else abs(self.cfg[second_control]+p[1]))
                plus=p.copy();minus=p.copy();plus[j]+=step;minus[j]-=step
                PJ[:,j]=(self.fun(t,y,plus)-self.fun(t,y,minus))/(2*step)
            self.select(p);self.flow(p[0])
            return ds[None,None,:]*J,PJ

        def terminal(self,y,p):
            self.select(p)
            return super().terminal(y,p)

        def bc(self,ya,yb,p):
            self.select(p)
            return np.r_[ya-self.initial(p),self.terminal(yb,p)]

        def bc_jac(self,ya,yb,p):
            self.select(p)
            A,B,P=super().bc_jac(ya,yb,p)
            # The fixed physical cut has no design derivative. Compute the
            # tiny numerical derivative explicitly rather than assuming it.
            for j in (0,1):
                step=2e-6*max(.1,abs(self.cfg['delta']+p[0]) if j==0 else abs(self.cfg[second_control]+p[1]))
                pp=p.copy();pm=p.copy();pp[j]+=step;pm[j]-=step
                P[:,j]=(self.bc(ya,yb,pp)-self.bc(ya,yb,pm))/(2*step)
            self.select(p);self.flow(p[0]);self.initial(p)
            return A,B,P

        def seed(self,nodes):
            p=np.zeros(self.M);self.select(p);f=self.flow(0.)
            t=merge_profile_mesh(np.linspace(0,1,nodes),self.chart_breaks)
            s,_=self.chart(t,0.)
            N=max(2048,64*self.M);g=f.geo(s,N);theta=g['theta']
            er=np.stack((np.cos(theta),np.sin(theta),np.zeros_like(theta)),axis=-1)
            et=np.stack((-np.sin(theta),np.cos(theta),np.zeros_like(theta)),axis=-1)
            point=f.profile(s)[0][:,None,None]*er
            for j,qj in enumerate(self.ref_coeff):
                m=2*(j+1);line=f.backward_line(j);fg=np.empty((2,len(s)))
                for k,(lo,hi,sol,scale) in enumerate(line.segments):
                    mask=(s>=lo)&((s<hi) if k+1<len(line.segments) else (s<=hi))
                    if np.any(mask):fg[:,mask]=sol(s[mask])*math.exp(scale-line.logscale)/line.core[0]
                point+=qj*fg[0,:,None,None]*(np.cos(m*theta)[:,:,None]*er-np.sin(m*theta)[:,:,None]*et/m)
                point[:,:,2]+=qj*fg[1,:,None]*np.cos(m*theta)
            BB,_,_=f.basis(N);y=f.project(point-g['pos'],BB)/self.q
            difference=self.initial(p)-y[:,0]
            y+=difference[:,None]*np.maximum(0,1-s/(f.Tu/2))[None,:]**3
            return t,y,p

        def restart_from(self,saved,pullback,nodes,scale='linear'):
            """Pull back the old image, then explicitly deform it as a warm guess.

            The first conversion retains the old physical image and its height
            mean. Amplitude scaling and inlet correction are subsequent guess
            changes, not coordinate identities and not new isometric solutions.
            The new BVP recomputes its own height mean from its solved velocity.
            """
            from fixed_metric_mode3_bvp import merge_profile_mesh
            old=saved.rec;oldcfg=old['frozen_profile']
            for key in sorted((set(oldcfg)|set(self.cfg))-{'delta',second_control}):
                if oldcfg.get(key)!=self.cfg.get(key):
                    raise ValueError('Warm restart requires the same uncontrolled profile: '+key)
            p=np.zeros(self.M)
            p[0]=oldcfg['delta']-self.cfg['delta'];p[1]=oldcfg[second_control]-self.cfg[second_control]
            ratio=self.q/saved.q
            coeff=np.asarray(old.get('core',old.get('summary',{}).get('core',{}))['coefficients'])
            for j in range(2,min(self.M,len(coeff))):
                exponent=j+1 if secondary_law=='quadratic' else math.ceil((j+1)/2)
                p[j]=coeff[j]*(ratio**exponent if scale=='linear' else 1.)/self.pscale[j-1]
            self.select(p);f=self.flow(p[0])
            if abs(f.end-saved.flow.end)>2e-12*max(1.,f.end):
                raise ValueError('Warm physical meridian length changed unexpectedly')
            t=merge_profile_mesh(np.linspace(0,1,nodes),self.chart_breaks)
            s,_=self.chart(t,p[0])
            arrays,record=pullback.convert(saved,f.general_core_chart,self.M,self.q,s,
                angular=max(512,32*(2*self.M+1)),height_angular=128)
            y=arrays['y']
            if scale=='linear':
                N=max(512,32*(2*self.M+1));g=f.geo(s,N);theta=g['theta']
                radial=np.stack((np.cos(theta),np.sin(theta),np.zeros_like(theta)),axis=-1)
                background=f.profile(s)[0][:,None,None]*radial
                B,_,_=f.basis(N)
                y=ratio*y+(ratio-1)*f.project(g['pos']-background,B)/self.q
            correction=self.initial(p)-y[:,0]
            y+=correction[:,None]*np.maximum(0,1-s/(f.Tu/2))[None,:]**3
            record.update(amplitude_scaling=scale,amplitude_ratio=ratio,
                boundary_correction_max=float(np.max(abs(correction))),
                higher_core_guess_scaling=('q ratio to harmonic order' if secondary_law=='quadratic' else 'q ratio to ceil(harmonic order/2)')if scale=='linear' else 'unchanged',
                height_mean_disposition='The conversion records the preserved mean; the subsequent warm deformation is not claimed to preserve the old image. The solved BVP independently integrates its own mean velocity.',
                final_scope='Deformed warm initial guess only; a fresh nonlinear solve is required.')
            return t,y,p,record

    return DualBVP


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('source-topic','port','out-prefix'):p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--profile',type=Path)
    p.add_argument('--restart',type=Path)
    p.add_argument('--raw-collocation-restart',type=Path)
    p.add_argument('--postprocess-only',action='store_true')
    p.add_argument('--warm-scale',choices=['linear','none'],default='linear')
    p.add_argument('--q',type=float,default=.04);p.add_argument('--modes',type=int,default=6)
    p.add_argument('--secondary-law',choices=['linear','quadratic'],default='linear')
    p.add_argument('--secondary-scale',type=float,default=.2)
    p.add_argument('--meridian-chart',choices=['legacy','all-knots'],default='all-knots')
    p.add_argument('--newton-backend',choices=['source','refresh'],default='source')
    p.add_argument('--second-control',choices=['vd','boost_length'],default='vd')
    p.add_argument('--angular',type=int,default=128);p.add_argument('--nodes',type=int,default=181)
    p.add_argument('--max-nodes',type=int,default=2000);p.add_argument('--tol',type=float,default=2e-6)
    p.add_argument('--check-only',action='store_true')
    a=p.parse_args();start=time.time();a.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    if a.postprocess_only and not a.raw_collocation_restart:
        raise ValueError('--postprocess-only requires a raw collocation recovery manifest')
    loader=module('root_dual_mode2',HERE/'numerical-m2-prefix.py')
    adaptive=loader.load(a.source_topic)
    jac=loader.source_module('root_dual_fourier',a.source_topic/'scripts/78718-prefix-fourier-jacobian.py');jac.install(adaptive)
    charts=module('root_dual_charts',HERE/'geometric-general-core-chart.py')
    chart=dict(knots=[0.,1.],values=[1.,1.],final_derivative=0.)
    cfg=json.loads(a.profile.read_text()) if a.profile else dict(direction='outward',vu=.55,
      vd=.44634731358817764,delta=.15848094366013005,ramp=.4,ramp_eta=.05,ramp_law='flat',cycles=1)
    port=json.loads(a.port.read_text());port['_sha256']=hashlib.sha256(a.port.read_bytes()).hexdigest()
    if cfg.get('prefix_bridge'):
        bridges=module('root_dual_short_bridge',HERE/'root_short_bridge.py');bridges.install()
        port['cut']={**port['cut'],'_prefix_bridge':cfg['prefix_bridge']}
    provider_names=[]
    if cfg.get('ramp_law')=='hermite_boost_neck':
        neck=module('root_dual_neck_provider',HERE/'alternative-neck-provider.py')
        neck.install();port=neck.tagged_port(port,cfg)
        provider_names=['alternative-neck-provider.py','alternative-neck-flatturn.py',
                        'alternative-neck-excursion.py','alternative-angle-plateau-connector.py',
                        'alternative-direct-tail-connector.py']
    Dual=make_dual(adaptive,charts,chart,a.secondary_law,a.secondary_scale,a.meridian_chart,a.second_control);obj=Dual(cfg,port,a.q,a.modes,a.angular)
    obj.bcweights=np.ones(obj.M)*.01
    from f6curve_domain_newton import install,STATS
    if a.newton_backend=='refresh':
        newton=module('root_owned_domain_newton',HERE/'root_domain_newton.py')
        install,STATS=newton.install,newton.STATS
    from curve_stable_prefix_bvp import save_checkpoint
    out=dict(scope=__doc__,solver_success=False,base_profile=cfg,requested_q=a.q,modes=a.modes,
             source_git_head=loader.source_revision(a.source_topic),
             secondary_law=a.secondary_law,secondary_scale=a.secondary_scale,
             requested_meridian_chart=a.meridian_chart,
             second_design_control=a.second_control,
             interface_hashes={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                for name in ['root_dual_core_bvp.py','root_neck_chart.py','geometric-general-core-chart.py','numerical-m2-prefix.py','root_short_bridge.py']+provider_names})
    try:
        raw_solution=None
        if a.raw_collocation_restart:
            import root_raw_collocation
            raw_solution,raw_record=root_raw_collocation.read(a.raw_collocation_restart,obj,a)
            x,y,par=raw_solution.x,raw_solution.y,raw_solution.p
            out['raw_recovery']=dict(file=str(a.raw_collocation_restart),
                sha256=hashlib.sha256(a.raw_collocation_restart.read_bytes()).hexdigest(),
                postprocess_only=a.postprocess_only,previous_solver_success=raw_solution.success)
            if a.postprocess_only and not raw_solution.success:
                raise ValueError('Cannot skip Newton for a failed raw collocation result')
        elif a.restart:
            pullback=module('root_dual_pullback',HERE/'geometric-checkpoint-core-pullback.py')
            saved,_=pullback.load_saved(a.restart,a.source_topic,a.port,angular=max(512,a.angular))
            x,y,par,warm=obj.restart_from(saved,pullback,a.nodes,a.warm_scale)
            out['warm_start']=dict(checkpoint=str(a.restart),metadata_sha256=hashlib.sha256(a.restart.read_bytes()).hexdigest(),
                checkpoint_solver_success=bool(saved.rec.get('solver_success',False)),conversion=warm)
        else:x,y,par=obj.seed(a.nodes)
        if a.check_only:
            test=np.linspace(.02,.98,7);f=obj.flow(0.)
            # The real seed is interpolated only for a local Jacobian check.
            Y=np.vstack([np.interp(test,x,row) for row in y]);J,P=obj.fun_jac(test,Y,par)
            rng=np.random.default_rng(20261110);v=rng.normal(size=Y.shape)
            cs=obj.fun(test,Y.astype(complex)+1e-25j*v,par).imag/1e-25
            out.update(jacobian_relative=float(np.max(abs(cs-np.einsum('ijk,jk->ik',J,v)))/max(1.,np.max(abs(cs)))),
                       parameter_jacobian_max=float(np.max(abs(P))),initial=obj._inlet_metrics)
            print(json.dumps(out));return
        install();print(json.dumps(dict(event='start',q=a.q,M=a.modes,nodes=len(x))),flush=True)
        solver=getattr(obj,'solve_coupled',solve_bvp)
        sol=raw_solution if a.postprocess_only else solver(obj.fun,obj.bc,x,y,par,tol=a.tol,bc_tol=1e-7,max_nodes=a.max_nodes,
                      fun_jac=obj.fun_jac,bc_jac=obj.bc_jac,verbose=2)
        import root_raw_collocation
        out['raw_collocation_checkpoint']=root_raw_collocation.write(
            a.out_prefix.with_name(a.out_prefix.name+'-raw-collocation.json.gz'),sol,obj,a,
            dict(initial_record=out,fixed_metric=getattr(obj,'fixed_metric_provenance',None),
                 newton_stats=dict(STATS)))
        print(json.dumps(dict(event='raw_collocation_saved',**out['raw_collocation_checkpoint'])),flush=True)
        root_raw_collocation.release_memory('after_raw_checkpoint_before_physical_interpolant')
        obj.select(sol.p);f=obj.flow(sol.p[0]);obj.initial(sol.p)
        physical=SimpleNamespace(x=obj.chart(sol.x,sol.p[0])[0],y=sol.y,p=sol.p)
        print(json.dumps(dict(event='physical_interpolant_begin',nodes=len(sol.x))),flush=True)
        physical.sol=f.c2_interpolant(physical)
        # The physical flow is authoritative. Optional fixed-metric adapters
        # use p0/p1 for core coefficients instead of meridian design controls.
        frozen=dict(f.cfg)
        out.update(config=dict(modes=obj.M,base_mode=2,core_kind='dual_support_general_chart',
            angular=obj.nt,tol=a.tol,actual_nonlinear_tail=False,fixed_metric=bool(getattr(obj,'fixed',False))),
            parameter_layout=obj._special_layout,angular_chart='general-support-core-blend-v1',
            chart_reference_coefficients=obj.ref_coeff.tolist(),chart_reference_frequencies=list(getattr(obj,'ref_frequencies',[2,4])),
            source_transforms=loader.TRANSFORMS,frozen_profile=frozen,
            physical_tail_parameters=port['parameters'],physical_tail_cut=port['cut'],physical_port_sha256=port['_sha256'],
            gauge_amplitude=obj.q,actual_primary_amplitude=float(obj.support_amplitude),parameters=sol.p.tolist(),
            central_correction_scales=obj.pscale.tolist(),mesh=physical.x.tolist(),
            pp_coefficients=physical.sol.c,nodes=len(sol.x),solver_success=bool(sol.success),
            message=sol.message,max_rms_collocation_residual=float(np.max(sol.rms_residuals)),
            newton_backend=a.newton_backend,
            worst_collocation_intervals=[dict(index=int(i),t_left=float(sol.x[i]),t_right=float(sol.x[i+1]),
                s_left=float(physical.x[i]),s_right=float(physical.x[i+1]),rms=float(sol.rms_residuals[i]))
                for i in np.argsort(sol.rms_residuals)[-8:][::-1]],
            newton_domain_audit=dict(STATS),core=obj._core.summary(),meridian_length=f.end)
        if a.postprocess_only:
            out['newton_domain_audit']=raw_record['provenance'].get('newton_stats',{})
        if a.newton_backend=='refresh':
            out['newton_backend_sha256']=hashlib.sha256((HERE/'root_domain_newton.py').read_bytes()).hexdigest()
        if hasattr(obj,'fixed_metric_provenance'):
            out['fixed_metric_provenance']=obj.fixed_metric_provenance
        if hasattr(obj,'design_provenance'):
            out['design_provenance']=obj.design_provenance
        if obj._neck_knots is not None:
            nc=module('root_saved_neck_chart',HERE/'root_neck_chart.py').NeckChart(obj._neck_knots,f.breaks)
            out['numerical_meridian_chart']=dict(kind='C2-all-physical-knots-v1',
                reference_t=obj._neck_knots.tolist(),physical_s=f.breaks.tolist(),
                positive_derivative_control_min=nc.bernstein_min,
                scope='Numerical coordinate only; frozen_profile is the physical metric.')
        out['audit_pending']=True
        if hasattr(obj,'prepare_recovery_output'):obj.prepare_recovery_output(out)
        save_checkpoint(a.out_prefix.with_suffix('.json.gz'),out)
        print(json.dumps(dict(event='physical_checkpoint_saved',audit_pending=True,nodes=len(sol.x))),flush=True)
        root_raw_collocation.release_memory('before_physical_audit')
        if sol.success:out['summary']=adaptive.audit(obj,physical,max(512,16*(obj.M*2+1)))
        if hasattr(obj,'finalize_output'):obj.finalize_output(out,physical)
        out['audit_pending']=False
        out['seconds']=time.time()-start
        save_checkpoint(a.out_prefix.with_suffix('.json.gz'),out)
        print(json.dumps(dict(event='result',success=out['solver_success'],profile=frozen,core=out['core'],summary=out.get('summary'),seconds=out['seconds'])),flush=True)
    except Exception as e:
        out['error']=repr(e);print(json.dumps(dict(event='error',error=repr(e))),flush=True)
    finally:
        out['seconds']=time.time()-start
        a.out_prefix.with_name(a.out_prefix.name+'-summary.json').write_text(json.dumps({k:v for k,v in out.items()if k not in ('mesh','pp_coefficients')},indent=2)+'\n')


if __name__=='__main__':main()
