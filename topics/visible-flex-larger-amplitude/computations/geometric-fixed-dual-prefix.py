#!/usr/bin/env python3
"""Fixed-physical-metric refinement of a saved two-control m2 prefix.

The metric profile, tail port, general-core reference, and physical length
remain frozen. All planar support coefficients become boundary unknowns;
the ODE has zero parameter Jacobian. The linear tail DN condition remains
only a finite prefix condition, not a nonlinear closed-surface construction.
"""
from __future__ import annotations
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
from types import SimpleNamespace
import numpy as np
from scipy.integrate import solve_bvp
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent


def module(name,path):
    sp=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(sp);sys.modules[name]=obj;sp.loader.exec_module(obj)
    return obj


def canonical(value):return json.dumps(value,sort_keys=True,separators=(',',':')).encode()
def digest(value):return hashlib.sha256(canonical(value)).hexdigest()


def verify_port(meta,path,frozen_path=None):
    """Permit only an exact prefix-preserving extension of one physical port."""
    port=json.loads(path.read_text());port['_sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
    if port['_sha256']==meta['physical_port_sha256']:
        return port,dict(kind='identical_file',sha256=port['_sha256'])
    if frozen_path is None:
        raise ValueError('Port file differs: provide --frozen-port for an exact old-prefix extension')
    old=json.loads(frozen_path.read_text());oldhash=hashlib.sha256(frozen_path.read_bytes()).hexdigest()
    if oldhash!=meta['physical_port_sha256']:raise ValueError('Frozen port does not match the input checkpoint')
    for key in ('parameters','cut'):
        if canonical(port[key])!=canonical(old[key]):raise ValueError('Physical tail '+key+' changed')
    n=len(old['linearSlope'])
    if port['linearSlope'][:n]!=old['linearSlope']or port['modes'][:n]!=old['modes']:
        raise ValueError('Previously frozen DN modes changed')
    if len(port['linearSlope'])<n:raise ValueError('The new port is not an extension')
    return port,dict(kind='exact_prefix_preserving_extension',frozen_file=str(frozen_path),
        frozen_sha256=oldhash,extended_sha256=port['_sha256'],preserved_modes=n,
        old_mode_values_identical=True,physical_parameters_and_cut_canonical_bytes_identical=True)


def diagnose(saved,angular=1024):
    """Separate PPoly radial residual from Fourier velocity projection."""
    start=time.time();f=saved.flow;pp=saved.sol.sol
    nodes=np.asarray(saved.sol.x);mid=(nodes[:-1]+nodes[1:])/2
    ss=np.unique(np.r_[nodes,mid,np.linspace(0,f.end,151)])
    is_node=np.min(abs(ss[:,None]-nodes[None,:]),axis=1)<2e-13
    B,B1,B2=f.basis(angular)
    quantities=('metric_pp_E','metric_pp_F','metric_G','metric_rhs_E','metric_rhs_F',
                'radial_interpolant_velocity_defect','fourier_projection_velocity_defect',
                'angular_quadrature_velocity_difference')
    out={group:{name:dict(value=0.,s=None)for name in quantities}
         for group in ('all','nodes','between_nodes')}
    for first in range(0,len(ss),24):
        sl=slice(first,first+24);s=ss[sl];Y=pp(s);Yp=pp(s,1)
        fr=f.frame(s,f.q*Y,B1,B2);g=fr['geo'];a=fr['a']
        rhs=f.fun(s,Y,saved.sol.p)
        rhs_high=f.project(fr['V']-g['s1'],B)/f.q
        def velocity(state):
            W=g['s1']+f.q*f.values(state,B)
            W[:,:,2]+=np.mean(fr['V'][:,:,2],axis=1)[:,None]
            return W-g['v'][:,:,None]*fr['d']
        Vpp=velocity(Yp);Vrhs=velocity(rhs_high);Ft=fr['d']/g['rho'][:,:,None]
        def l1(values):return np.sum(abs(np.fft.fft(values,axis=1)/angular),axis=1)
        vals=dict(metric_pp_E=l1(np.sum(Vpp*Vpp,axis=2)-1),
                  metric_pp_F=l1(np.sum(Vpp*Ft,axis=2)/a[:,None]),
                  metric_G=l1(np.sum(Ft*Ft,axis=2)/a[:,None]**2-1),
                  metric_rhs_E=l1(np.sum(Vrhs*Vrhs,axis=2)-1),
                  metric_rhs_F=l1(np.sum(Vrhs*Ft,axis=2)/a[:,None]),
                  radial_interpolant_velocity_defect=np.linalg.norm(f.q*f.values(Yp-rhs,B),axis=2).max(axis=1),
                  fourier_projection_velocity_defect=np.linalg.norm(Vrhs-fr['Vnormal'],axis=2).max(axis=1),
                  angular_quadrature_velocity_difference=np.linalg.norm(f.q*f.values(rhs-rhs_high,B),axis=2).max(axis=1))
        for group,mask in [('all',np.ones(len(s),bool)),('nodes',is_node[sl]),('between_nodes',~is_node[sl])]:
            if not np.any(mask):continue
            inds=np.flatnonzero(mask)
            for name,v in vals.items():
                i=int(inds[np.argmax(v[mask])]);value=float(v[i])
                if value>out[group][name]['value']:out[group][name]=dict(value=value,s=float(s[i]))
    return dict(samples=len(ss),nodes=len(nodes),angular=angular,rhs_angular=f.nt,
        profile_sha256=digest(saved.rec['frozen_profile']),groups=out,seconds=time.time()-start,
        scope='Finite angular FFT l1 metric diagnostics; not a continuous-angle enclosure. Original saved PPoly is unchanged.')


def make_fixed(dual,adaptive,charts,chart,reference,reference_frequencies):
    Dual=dual.make_dual(adaptive,charts,chart)
    from fixed_metric_mode3_core import PlanarSupportCore
    from fixed_metric_mode3_bvp import merge_profile_mesh

    class FixedBVP(Dual):
        def __init__(self,cfg,port,q,M,angular):
            super().__init__(cfg,port,q,M,angular)
            self.ref_coeff=np.asarray(reference,float).copy()
            self.ref_frequencies=list(reference_frequencies)
            self.fixed=True;self._flow=None;self._flow_key=None
            self._core_key=None;self._initial=None
            self.pscale=np.maximum(q**np.arange(2,M+1),1e-9)
            self._special_layout='p0=log(actual_q/gauge_q); p1=(q4-reference_q4)/gauge_q^2; p2..=higher support/recorded scale'

        def make_flow(self,*args,**kwargs):
            kwargs.pop('warp_q',None)
            Flow,_=adaptive.build_classes(chart)
            f=Flow(*args,warp_q=0.,**kwargs)
            charts.attach_to_adaptive_flow(f,self.ref_coeff,self.ref_frequencies,reference='core-blend')
            return f

        def flow(self,p0=0.):
            if self._flow is None:
                self._flow=self.Flow(self.cfg,self.port,self.M,self.q,self.nt,self.base_mode,self.bridge)
                self._flow_key='frozen'
            return self._flow

        def initial(self,p):
            key=tuple(np.asarray(p,float))
            if key!=self._core_key:
                qa=self.q*math.exp(float(p[0]))
                if not 1e-7<qa<.48:raise FloatingPointError('Actual core amplitude left the search domain')
                corrections=np.asarray(p[1:])*self.pscale
                corrections[0]+=self.ref_coeff[1]
                core=PlanarSupportCore(qa,corrections,self.base_mode)
                f=self.flow();N=max(2048,128*self.M);gi=f.general_core_chart.inlet_geometry(N)
                exact=core.evaluate(gi['theta']);B,B1,B2=f.basis(N)
                self._initial=f.project((exact['F']-gi['pos'])[None,:,:],B)[:,0]/self.q
                J=f.project(core.parameter_derivatives(gi['theta']),B)
                self._initial_jac=np.zeros((self.n,self.M))
                self._initial_jac[:,0]=qa*J[:,0]/self.q
                self._initial_jac[:,1:]=J[:,1:]*self.pscale[None,:]/self.q
                first=gi['p1']+self.q*f.values(self._initial[:,None],B1)[0]
                second=gi['p2']+self.q*f.values(self._initial[:,None],B2)[0]
                mapped=gi['pos']+self.q*f.values(self._initial[:,None],B)[0]
                true1=exact['Ft']*gi['rho'][:,None]
                true2=exact['Ftt']*gi['rho'][:,None]**2+exact['Ft']*gi['rhop'][:,None]
                error=np.sum(first*first,axis=1)/gi['rho']**2-1
                self._inlet_metrics=dict(position=float(np.linalg.norm(mapped-exact['F'],axis=1).max()),
                    first=float(np.linalg.norm(first-true1,axis=1).max()),second=float(np.linalg.norm(second-true2,axis=1).max()),
                    metric_l1=float(np.sum(abs(np.fft.fft(error)/N))))
                self._core=core;self._core_key=key;self.support_amplitude=qa
            return self._initial

        def fun(self,t,y,p):
            f=self.flow();s,ds=self.chart(t,0.)
            return ds[None,:]*f.fun(s,y,p)

        def fun_jac(self,t,y,p):
            f=self.flow();s,ds=self.chart(t,0.);J,_=f.fun_jac(s,y,p)
            return ds[None,None,:]*J,np.zeros((self.n,self.M,len(t)))

        def bc_jac(self,ya,yb,p):
            A=np.zeros((self.n+self.M,self.n));A[:self.n]=np.eye(self.n)
            B=np.zeros_like(A);P=np.zeros((self.n+self.M,self.M))
            self.initial(p);P[:self.n]=-self._initial_jac;f=self.flow()
            J,_=f.fun_jac(np.array([f.end]),yb.astype(np.longdouble)[:,None],p)
            T=self.q*J[self.iz:,:,0]
            T[:,self.iz:]-=self.q*self.bridge.sigma*self.Dmatrix/math.sqrt(self.port['cut']['E'])
            B[self.n:]=T/self.bcweights[:,None]
            return A,B,P

        def restart_fixed(self,saved,pullback,nodes=0):
            old=saved.rec
            if canonical(old['frozen_profile'])!=canonical(self.cfg):raise ValueError('Physical profile changed')
            if old['physical_tail_parameters']!=self.port['parameters']or old['physical_tail_cut']!=self.port['cut']:
                raise ValueError('Physical tail metric changed')
            if old['chart_reference_coefficients']!=self.ref_coeff.tolist()or old['chart_reference_frequencies']!=self.ref_frequencies:
                raise ValueError('Fixed reference chart changed')
            c=np.asarray(old['core']['coefficients']);p=np.zeros(self.M)
            p[0]=math.log(c[0]/self.q);p[1]=(c[1]-self.ref_coeff[1])/self.pscale[0]
            for j in range(2,min(self.M,len(c))):p[j]=c[j]/self.pscale[j-1]
            f=self.flow()
            if f.end!=saved.flow.end:raise ValueError('Physical length changed')
            grid=self.inverse_chart(np.asarray(saved.sol.x),0.)
            if nodes>0:grid=np.r_[grid,np.linspace(0,1,nodes)]
            t=merge_profile_mesh(grid,self.chart_breaks);s,_=self.chart(t,0.)
            arrays,record=pullback.convert(saved,f.general_core_chart,self.M,self.q,s,
                angular=max(512,32*(2*self.M+1)),height_angular=128)
            y=arrays['y'];correction=self.initial(p)-y[:,0]
            y+=correction[:,None]*np.maximum(0,1-s/(f.Tu/2))[None,:]**3
            record.update(boundary_correction_max=float(abs(correction).max()),amplitude_scaling='none',
                metric_profile_identical=True,profile_sha256=digest(self.cfg),
                height_mean_disposition='Same physical angle and reference: correction is recorded. Solved mean height is integrated from its own solved velocity; no s-dependent height translation is applied.')
            return t,y,p,record

    return FixedBVP


def compare_shape(saved,obj,sol,angular=512):
    f=obj.flow();old=saved.flow
    # Quintic endpoint corrections have zero second derivative at endpoints
    # and at the midpoint, but extrema at these two interior fractions.
    # Include them for BOTH saved meshes; this is still a sample comparison.
    fractions=np.array([.5,(3-np.sqrt(3))/6,(3+np.sqrt(3))/6])
    def interior(mesh):
        mesh=np.asarray(mesh)
        return (mesh[:-1,None]+np.diff(mesh)[:,None]*fractions).ravel()
    ss=np.unique(np.r_[np.linspace(0,f.end,201),sol.x,saved.sol.x,
                       interior(sol.x),interior(saved.sol.x)])
    H=f.height_integral(sol,ss,angular,6);Ho=old.height_integral(saved.sol,ss,angular,6)
    B,B1,B2=f.basis(angular);Bo,Bo1,Bo2=old.basis(angular)
    peak=dict(distance=0.,s=0.,psi=0.);total=0.;count=0
    jet_peaks={key:dict(value=0.,s=0.,psi=0.)for key in ('s','theta','ss','s_theta','theta_theta')}
    def jets(flow,pp,s,BB,BB1,BB2):
        Y=pp(s);Yp=pp(s,1);Ypp=pp(s,2)
        fr,Fsp,dW=flow.velocity_s(s,Y,Yp,BB1,BB2);g=fr['geo']
        rho=g['rho'];v=g['v']
        Fsc=g['s1']+flow.q*flow.values(Yp,BB)
        Fsc[:,:,2]+=np.mean(fr['V'][:,:,2],axis=1)[:,None]
        Fssc=g['s2']+flow.q*flow.values(Ypp,BB)
        Fssc[:,:,2]+=np.mean(dW[:,:,2],axis=1)[:,None]
        return dict(s=Fsc-v[:,:,None]*fr['d'],theta=fr['d']/rho[:,:,None],
            ss=Fssc-2*v[:,:,None]*Fsp+v[:,:,None]**2*fr['dd']+(v*g['vp']-g['vs'])[:,:,None]*fr['d'],
            s_theta=(Fsp-g['vp'][:,:,None]*fr['d']-v[:,:,None]*fr['dd'])/rho[:,:,None],
            theta_theta=fr['dd']/rho[:,:,None]**2-fr['d']*g['rhop'][:,:,None]/rho[:,:,None]**3)
    for first in range(0,len(ss),32):
        sl=slice(first,first+32);s=ss[sl]
        new=f.geo(s,angular)['pos']+f.q*f.values(sol.sol(s),B)
        prior=old.geo(s,angular)['pos']+old.q*old.values(saved.sol.sol(s),Bo)
        new[:,:,2]+=H[sl,None];prior[:,:,2]+=Ho[sl,None]
        ds=np.linalg.norm(new-prior,axis=2);ij=np.unravel_index(np.argmax(ds),ds.shape)
        if ds[ij]>peak['distance']:peak=dict(distance=float(ds[ij]),s=float(s[ij[0]]),psi=float(2*np.pi*ij[1]/angular))
        total+=float(np.sum(ds*ds));count+=ds.size
        current_jets=jets(f,sol.sol,s,B,B1,B2);prior_jets=jets(old,saved.sol.sol,s,Bo,Bo1,Bo2)
        for key in jet_peaks:
            dsj=np.linalg.norm(current_jets[key]-prior_jets[key],axis=2)
            ij=np.unravel_index(np.argmax(dsj),dsj.shape)
            if dsj[ij]>jet_peaks[key]['value']:
                jet_peaks[key]=dict(value=float(dsj[ij]),s=float(s[ij[0]]),psi=float(2*np.pi*ij[1]/angular))
    return dict(maximum_material_point_displacement_sample=peak,rms_point_displacement_sample=math.sqrt(total/count),
                mean_height_difference_max=float(abs(H-Ho).max()),radial_samples=len(ss),angular=angular,
                interior_interval_fractions=fractions.tolist(),
                physical_material_jet_differences_max_sample=jet_peaks,
                scope='Physical points and two jets at identical fixed material angle theta and physical s, including height mean jets; sample comparison, not a Hausdorff or continuum error certificate.')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('input','source-topic','port','out-prefix'):p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--frozen-port',type=Path,help='Exact old port, required only for a prefix-preserving mode extension')
    p.add_argument('--modes',type=int,default=24);p.add_argument('--angular',type=int,default=512)
    p.add_argument('--nodes',type=int,default=0);p.add_argument('--max-nodes',type=int,default=4000)
    p.add_argument('--tol',type=float,default=2e-7);p.add_argument('--bc-tol',type=float,default=1e-9)
    p.add_argument('--diagnostic-angular',type=int,default=1024)
    p.add_argument('--diagnostic-only',action='store_true');p.add_argument('--check-only',action='store_true')
    args=p.parse_args();start=time.time();args.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    pullback=module('geometric_fixed_pullback',HERE/'geometric-checkpoint-core-pullback.py')
    with (gzip.open(args.input,'rt')if args.input.suffix=='.gz'else open(args.input))as h:meta=json.load(h)
    port,port_verification=verify_port(meta,args.port,args.frozen_port)
    saved,loader=pullback.load_saved(args.input,args.source_topic,args.port,angular=meta['config']['angular'])
    out=dict(scope=__doc__,input_file=str(args.input),input_sha256=hashlib.sha256(args.input.read_bytes()).hexdigest(),
        solver_success=False,frozen_profile=saved.rec['frozen_profile'],profile_sha256=digest(saved.rec['frozen_profile']),
        port_verification=port_verification)
    diag=diagnose(saved,args.diagnostic_angular);out['input_diagnostic']=diag
    args.out_prefix.with_name(args.out_prefix.name+'-input-diagnostic.json').write_text(json.dumps(diag,indent=2)+'\n')
    print(json.dumps(dict(event='input_diagnostic',groups=diag['groups'],seconds=diag['seconds'])),flush=True)
    if args.diagnostic_only:return
    adaptive=loader.load(args.source_topic)
    jac=loader.source_module('geometric_fixed_fourier',args.source_topic/'scripts/78718-prefix-fourier-jacobian.py');jac.install(adaptive)
    charts=module('geometric_fixed_chart',HERE/'geometric-general-core-chart.py')
    dual=module('geometric_fixed_dual',HERE/'root_dual_core_bvp.py')
    chart=dict(knots=[0.,1.],values=[1.,1.],final_derivative=0.)
    Fixed=make_fixed(dual,adaptive,charts,chart,saved.rec['chart_reference_coefficients'],saved.rec['chart_reference_frequencies'])
    obj=Fixed(saved.rec['frozen_profile'],port,saved.q,args.modes,args.angular);obj.bcweights=np.ones(obj.M)*.01
    from f6curve_domain_newton import install,STATS
    from curve_stable_prefix_bvp import save_checkpoint
    try:
        x,y,par,warm=obj.restart_fixed(saved,pullback,args.nodes);out['warm_start']=warm
        out.update(parameter_layout=obj._special_layout,modes=obj.M,gauge_amplitude=obj.q,
            angular_chart='general-support-core-blend-v1',chart_reference_coefficients=obj.ref_coeff.tolist(),
            chart_reference_frequencies=obj.ref_frequencies,physical_port_sha256=port['_sha256'],
            physical_tail_parameters=port['parameters'],physical_tail_cut=port['cut'],
            source_transforms=loader.TRANSFORMS,source_git_head=loader.source_revision(args.source_topic),
            interface_hashes={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()for name in
                ('geometric-fixed-dual-prefix.py','geometric-checkpoint-core-pullback.py','geometric-general-core-chart.py','root_dual_core_bvp.py')})
        if args.check_only:
            i=np.linspace(0,len(x)-1,min(9,len(x)),dtype=int);test=x[i];Y=y[:,i]
            J,P=obj.fun_jac(test,Y,par);v=np.random.default_rng(20261110).normal(size=Y.shape)
            cs=obj.fun(test,Y.astype(complex)+1e-25j*v,par).imag/1e-25
            step=2e-6;direc=np.random.default_rng(20261111).normal(size=obj.M)
            fd=(obj.initial(par+step*direc)-obj.initial(par-step*direc))/(2*step);obj.initial(par)
            out.update(jacobian_relative=float(abs(cs-np.einsum('ijk,jk->ik',J,v)).max()/max(1.,abs(cs).max())),
                parameter_jacobian_max=float(abs(P).max()),inlet_jacobian_direction_error=float(abs(fd-obj._initial_jac@direc).max()),
                inlet=obj._inlet_metrics,bc_initial_max=float(abs(obj.bc(y[:,0],y[:,-1],par)).max()))
            print(json.dumps({k:out[k]for k in ('jacobian_relative','parameter_jacobian_max','inlet_jacobian_direction_error','bc_initial_max')}),flush=True)
            return
        install();print(json.dumps(dict(event='start_fixed',M=obj.M,nodes=len(x),tol=args.tol,profile_sha256=out['profile_sha256'])),flush=True)
        sol=solve_bvp(obj.fun,obj.bc,x,y,par,tol=args.tol,bc_tol=args.bc_tol,max_nodes=args.max_nodes,
            fun_jac=obj.fun_jac,bc_jac=obj.bc_jac,verbose=2)
        f=obj.flow();obj.initial(sol.p)
        physical=SimpleNamespace(x=obj.chart(sol.x,0.)[0],y=sol.y,p=sol.p);physical.sol=f.c2_interpolant(physical)
        out.update(config=dict(modes=obj.M,base_mode=2,core_kind='fixed_dual_support_general_chart',angular=obj.nt,
            tol=args.tol,bc_tol=args.bc_tol,actual_nonlinear_tail=False,fixed_metric=True),
            actual_primary_amplitude=obj.support_amplitude,parameters=sol.p.tolist(),
            central_correction_scales=obj.pscale.tolist(),mesh=physical.x.tolist(),pp_coefficients=physical.sol.c,
            nodes=len(sol.x),solver_success=bool(sol.success),message=sol.message,
            max_rms_collocation_residual=float(sol.rms_residuals.max()),newton_domain_audit=dict(STATS),
            core=obj._core.summary(),meridian_length=f.end,physical_profile_byte_identical=canonical(obj.cfg)==canonical(saved.rec['frozen_profile']),
            actual_primary_change=obj.support_amplitude-saved.rec['core']['coefficients'][0])
        if sol.success:
            out['summary']=adaptive.audit(obj,physical,max(512,16*(2*obj.M+1)))
            out['shape_comparison']=compare_shape(saved,obj,physical,512)
        out['seconds']=time.time()-start;save_checkpoint(args.out_prefix.with_suffix('.json.gz'),out)
        print(json.dumps(dict(event='fixed_result',success=sol.success,actual_q=obj.support_amplitude,
            primary_change=out['actual_primary_change'],metric=out.get('summary',{}).get('metric_l1'),
            shape=out.get('shape_comparison'),seconds=out['seconds'])),flush=True)
    except Exception as e:
        out['error']=repr(e);print(json.dumps(dict(event='error',error=repr(e))),flush=True)
        raise
    finally:
        out['seconds']=time.time()-start
        args.out_prefix.with_name(args.out_prefix.name+'-summary.json').write_text(json.dumps({k:v for k,v in out.items()if k not in ('mesh','pp_coefficients')},indent=2)+'\n')


if __name__=='__main__':main()
