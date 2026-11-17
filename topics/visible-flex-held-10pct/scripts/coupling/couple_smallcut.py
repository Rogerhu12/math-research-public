#!/usr/bin/env python3
"""Mode-two ShortBridge prefix coupled to the original actual nonlinear DN.

The TailMixin, analytic boundary sign, affine-inner/true-outer method, and
seam audit are imported from the immutable db6f coupling source. Only the
already recorded mode-two prefix loader and a named physical tail worker
are selected. Every true tail response is retained outside the repository.
This is a finite Fourier/depth computation, not an infinite closure proof.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[name]='1'
import argparse,gzip,hashlib,importlib.util,json,math,sys,time,types
from pathlib import Path
from types import SimpleNamespace
import numpy as np


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('source-topic','prefix-driver','coupler-source','worker','profile','chart','port','tail-config','restart','out'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--amplitude',type=float,required=True);p.add_argument('--modes',type=int,default=8)
    p.add_argument('--warp-reference',type=float);p.add_argument('--angular',type=int,default=256)
    p.add_argument('--audit-angular',type=int,default=512);p.add_argument('--nodes',type=int,default=401)
    p.add_argument('--max-nodes',type=int,default=2400);p.add_argument('--tol',type=float,default=2e-7)
    p.add_argument('--bc-tol',type=float,default=1e-7);p.add_argument('--physical-bc-tol',type=float,default=2e-9)
    p.add_argument('--fixed',action='store_true');p.add_argument('--probe-only',action='store_true')
    p.add_argument('--relax-linear',action='store_true',help='Solve the finite linear-DN prefix at the requested q before querying the actual tail; never accepted as a nonlinear coupled result.')
    p.add_argument('--actual-every-query',action='store_true');p.add_argument('--node-heap',type=int,default=2304)
    p.add_argument('--warmup-scales',type=float,nargs='*',default=[.0001,.001,.003,.01,.03,.1,.3,1.])
    p.add_argument('--warmup-kind',choices=['full-vector','mode-powers'],default='full-vector')
    a=p.parse_args();a.out.mkdir(parents=True,exist_ok=False);begin=time.monotonic()
    a.warp_reference=a.amplitude if a.warp_reference is None else a.warp_reference
    a.lagged_tail=not a.actual_every_query
    source=a.source_topic.resolve();driver=load('smallcut_coupled_driver',a.prefix_driver.resolve())
    adaptive=driver.load(source)
    backend=driver.source_module('smallcut_coupled_fourier_jacobian',source/'scripts/78718-prefix-fourier-jacobian.py');backend.install(adaptive)
    coupling=driver.source_module('smallcut_original_coupling',a.coupler_source.resolve(),[
        ("adaptive=module('adaptive_coupled',S/'950f-prefix-adaptive-chart-bvp-v2.py')","adaptive=sys.modules['numerical_mode2_adaptive']"),
        ("client=module('weighted_client',S/'950f-tail-client-v3.py')","client=None")])
    cfg=json.loads(a.profile.read_text());chart=json.loads(a.chart.read_text());port=json.loads(a.port.read_text());tcfg=json.loads(a.tail_config.read_text())
    port['_sha256']=sha(a.port)
    if tcfg['spacing']!=2 or tcfg['modes']!=a.modes:raise ValueError('Actual tail spacing/mode count mismatch')
    if port['modes'][:a.modes]!=list(2*np.arange(1,a.modes+1)):raise ValueError('Actual physical DN frequencies mismatch')
    if cfg.get('prefix_bridge'):
        short=driver.source_module('smallcut_coupled_bridge',a.prefix_driver.resolve().with_name('root_short_bridge.py'));short.install()
        port['cut']={**port['cut'],'_prefix_bridge':cfg['prefix_bridge']}
    _,Base=adaptive.build_classes(chart)
    class BVP(coupling.TailMixin,Base):pass
    obj=BVP(cfg,port,a.amplitude,a.modes,a.angular,a.fixed,a.warp_reference)
    if hasattr(obj.bridge,'breakpoints'):
        f=obj.flow(0.);obj.chart_breaks=np.unique(np.r_[obj.chart_breaks,obj.inverse_chart(f.prefix_end+obj.bridge.breakpoints,0.)])
    obj.restart_remesh=a.nodes;obj.bcweights=np.full(obj.M,a.physical_bc_tol/a.bc_tol)
    x,y,par=obj.restart(a.restart)
    # Preserve the reviewed persistent protocol. Worker selection and source
    # hash lookup locations are the two exact, recorded client transforms.
    client_path=source/'scripts/db6f-prefix-tail-trial-client.py';client_source=client_path.read_text()
    substitutions=[("worker=Path(__file__).with_name('db6f-prefix-tail-trial-worker.mjs')","worker=Path("+repr(str(a.worker.resolve()))+")"),
        ("worker.with_name(name).read_bytes()","Path(__file__).with_name(name).read_bytes()")]
    for old,new in substitutions:
        if client_source.count(old)!=1:raise ValueError('Unexpected actual-tail client source')
        client_source=client_source.replace(old,new)
    client=types.ModuleType('smallcut_actual_tail_client');client.__file__=str(client_path);exec(compile(client_source,str(client_path),'exec'),client.__dict__)
    os.environ['VISIBLE_FLEX_SOURCE_TOPIC']=str(source)
    tcfg['traceFile']=str((a.out/'worker-trace.jsonl').resolve());tcfg['trialDiagnosticFile']=str((a.out/'trial-diagnostics.jsonl').resolve());tcfg['iterationCheckpointFile']=str((a.out/'iteration-recovery.json.gz').resolve())
    config_path=a.out/'effective-tail-config.json';config_path.write_text(json.dumps(tcfg,indent=2)+'\n')
    summary=dict(scope=__doc__,solver_success=False,arguments={k:str(v)if isinstance(v,Path)else v for k,v in vars(a).items()},
        source_transforms=driver.TRANSFORMS,client_transforms=substitutions,client_sha256=sha(client_path),worker_sha256=sha(a.worker),prefix_checkpoint_sha256=sha(a.restart),port_sha256=sha(a.port),tail_config=tcfg,warmups=[],
        sign_convention='sigma=-1; worker input H=sigma*q*y_z; physical tail z=sigma*z_worker+constant; prefix z_s=P_worker/sqrt(E); boundary J subtracts sigma*q*DP/sqrt(E).')
    tail=None
    def save_summary():
        summary['seconds']=time.monotonic()-begin
        (a.out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    try:
        if a.relax_linear:
            from scipy.integrate import solve_bvp
            from f6curve_domain_newton import install
            from curve_stable_prefix_bvp import save_checkpoint
            linear=Base(cfg,port,a.amplitude,a.modes,a.angular,a.fixed,a.warp_reference)
            linear.chart_breaks=obj.chart_breaks.copy();linear.bcweights=obj.bcweights.copy()
            install();print(json.dumps(dict(event='linear_seed_relaxation',q=a.amplitude,nodes=len(x))),flush=True)
            seed=solve_bvp(linear.fun,linear.bc,x,y,par,tol=a.tol,bc_tol=a.bc_tol,max_nodes=a.max_nodes,fun_jac=linear.fun_jac,bc_jac=linear.bc_jac,verbose=2)
            summary['linear_seed_relaxation']=dict(success=bool(seed.success),nodes=len(seed.x),max_rms=float(np.max(seed.rms_residuals)),message=seed.message)
            if not seed.success:raise FloatingPointError('Preliminary linear-DN prefix did not converge')
            x,y,par=seed.x,seed.y,seed.p;lf=linear.flow(par[0]);linear.initial(par)
            ps=SimpleNamespace(x=linear.chart(x,par[0])[0],y=y,p=par);ps.sol=lf.c2_interpolant(ps)
            lr=dict(angular_chart='frozen-spline-adaptive-v1',chart=chart,warp_reference_q=a.warp_reference,
                config=dict(modes=linear.M,base_mode=2,core_kind='adaptive_warped_support',angular=linear.nt,fixed_metric=a.fixed,actual_nonlinear_tail=False),
                frozen_profile=cfg if a.fixed else{**cfg,'delta':cfg['delta']+float(par[0])},gauge_amplitude=linear.q,actual_primary_amplitude=linear.support_amplitude,meridian_length=lf.end,
                physical_port_sha256=sha(a.port),physical_tail_parameters=port['parameters'],physical_tail_cut=port['cut'],parameters=par.tolist(),central_correction_scales=linear.pscale.tolist(),
                solver_success=True,mesh=ps.x.tolist(),pp_coefficients=ps.sol.c,source_transforms=driver.TRANSFORMS)
            save_checkpoint(a.out/'linear-seed.json.gz',lr)
            summary['linear_seed_relaxation']['physical_height']=(linear.q*y[linear.iz:,-1]).tolist();save_summary()
        tail=client.WeightedTailPort(config_path,source/'repro/source-root',a.out/'response',node_heap=a.node_heap);obj.tail=tail
        for key,value in port['parameters'].items():
            if tail.ready['parameters'].get(key)!=value:raise ValueError('Actual worker physical parameter mismatch: '+key)
        for key in ('radius','backgroundSlope','backgroundSecond','E','Ep'):
            if abs(tail.cut[key]-port['cut'][key])>2e-11:raise ValueError('Actual worker physical cut mismatch: '+key)
        if not np.allclose(tail.linearD,port['linearSlope'][:a.modes],rtol=2e-5,atol=1e-8):raise ValueError('Actual worker linear DN differs from supplied port')
        summary['linear_ready_max_difference']=float(abs(tail.linearD-np.asarray(port['linearSlope'][:a.modes])).max())
        H=obj.bridge.sigma*obj.q*y[obj.iz:,-1];summary['initial_worker_height']=H.tolist();summary['initial_prefix_height']=(-H).tolist()
        save_summary();print(json.dumps(dict(event='ready',worker_height=H.tolist(),linear_dn_difference=summary['linear_ready_max_difference'])),flush=True)
        for scale in a.warmup_scales:
            target=H*scale if a.warmup_kind=='full-vector' else H*scale**np.arange(1,obj.M+1)
            started=time.monotonic();result=tail.solve(target,jacobian=False,audit=False)
            history=result.get('history')or[];last=history[-1]if history else{}
            row=dict(scale=scale,kind=a.warmup_kind,residual=result['residual'],seconds=time.monotonic()-started,tail_call=tail.calls,height=target.tolist(),minA=last.get('minA'),minD=last.get('minD'))
            summary['warmups'].append(row);save_summary();print(json.dumps(dict(event='warmup',**row)),flush=True)
        if a.probe_only:
            r=tail.solve(H,jacobian=True,audit=True);summary.update(probe_only=True,tail_converged=r['converged'],tail_residual=r['residual'],tail_jets=r['jets'],tail_audit=r.get('audit'),tail_calls=tail.calls)
            return
        from f6curve_domain_newton import install,STATS
        from curve_stable_prefix_bvp import save_checkpoint
        install();print(json.dumps(dict(event='start_coupled',q=a.amplitude,modes=a.modes,nodes=len(x),lagged_tail=a.lagged_tail)),flush=True)
        sol,outer=coupling.solve_with_actual_tail(obj,tail,x,y,par,a)
        f=obj.flow(sol.p[0]);obj.initial(sol.p);physical=SimpleNamespace(x=obj.chart(sol.x,sol.p[0])[0],y=sol.y,p=sol.p);physical.sol=f.c2_interpolant(physical)
        frozen=cfg if a.fixed else{**cfg,'delta':cfg['delta']+float(sol.p[0])}
        record=dict(scope=__doc__,angular_chart='frozen-spline-adaptive-v1',chart=chart,warp_reference_q=a.warp_reference,
            config=dict(modes=obj.M,base_mode=2,core_kind='adaptive_warped_support',angular=obj.nt,tol=a.tol,bc_tol=a.bc_tol,physical_bc_tol=a.physical_bc_tol,fixed_metric=a.fixed,actual_nonlinear_tail=True),
            frozen_profile=frozen,gauge_amplitude=obj.q,actual_primary_amplitude=obj.support_amplitude,meridian_length=f.end,physical_port_sha256=sha(a.port),physical_tail_parameters=port['parameters'],physical_tail_cut=port['cut'],tail_config=tcfg,
            parameters=sol.p.tolist(),central_correction_scales=obj.pscale.tolist(),nodes=len(sol.x),solver_success=bool(sol.success),message=sol.message,max_rms_collocation_residual=float(np.max(sol.rms_residuals)),newton_domain_audit=dict(STATS),mesh=physical.x.tolist(),pp_coefficients=physical.sol.c,
            actual_outer_checks=outer,source_transforms=driver.TRANSFORMS,worker_sha256=sha(a.worker))
        save_checkpoint(a.out/'prefix.json.gz',record)
        record['summary']=adaptive.audit(obj,physical,a.audit_angular)
        if sol.success:record['tail_seam']=obj.seam_audit(physical)
        record['tail_calls']=tail.calls;record['seconds']=time.monotonic()-begin;save_checkpoint(a.out/'prefix.json.gz',record)
        summary.update({k:v for k,v in record.items()if k not in ('mesh','pp_coefficients')})
        print(json.dumps(dict(event='result',success=sol.success,metric=record['summary']['metric_l1'],delta=frozen['delta'],tail_calls=tail.calls)),flush=True)
    except Exception as error:
        summary['error']=repr(error);summary['tail_calls']=tail.calls if tail else 0
        if tail:
            path=a.out/f'response_{tail.calls:04d}.json.gz'
            if path.exists():
                response=json.loads(gzip.decompress(path.read_bytes()))['response']
                summary['last_tail_response']={k:response.get(k)for k in ('failed','converged','residual','lastIteration','history','jets')}
        print(json.dumps(dict(event='failure',error=repr(error),tail_calls=summary['tail_calls'])),flush=True)
    finally:
        if tail:tail.close()
        save_summary()


if __name__=='__main__':main()
