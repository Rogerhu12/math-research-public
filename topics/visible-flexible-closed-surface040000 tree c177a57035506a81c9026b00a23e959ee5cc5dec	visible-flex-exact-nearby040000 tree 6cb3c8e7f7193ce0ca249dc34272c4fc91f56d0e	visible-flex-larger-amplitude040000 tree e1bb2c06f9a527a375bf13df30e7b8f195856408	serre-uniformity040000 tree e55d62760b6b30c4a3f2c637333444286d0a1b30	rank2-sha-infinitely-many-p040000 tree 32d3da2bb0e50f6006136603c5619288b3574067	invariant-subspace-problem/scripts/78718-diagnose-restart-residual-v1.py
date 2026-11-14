#!/usr/bin/env python3
"""Read-only W14 residual of the next actual saved-mesh restart initial guess.

No Newton, BVP solve, Jacobian/LU, nonlinear tail request, or new geometric
certificate is performed.  This is not a recovery of the lost old weighted
cubic; it evaluates the unchanged original restart followed by the original
SciPy collocation/RMS formulas on the newly reconstructed initial guess.
"""
from __future__ import annotations

import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
from datetime import datetime,timezone
import gzip
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import resource
import sys
import time
import traceback


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def identity(path):
    path=Path(path).resolve();raw=path.read_bytes()
    return {'path':str(path),'bytes':len(raw),'sha256':sha(raw)}


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    result=importlib.util.module_from_spec(spec);spec.loader.exec_module(result)
    return result


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--launch',type=Path,required=True)
    ap.add_argument('--checkpoint',type=Path,required=True)
    ap.add_argument('--mode',choices=('pilot','full'),required=True)
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--data-cap-bytes',type=int,default=2_147_483_648)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    proposed=args.out.with_name(args.out.stem+'-intervals.npz.gz')
    if proposed.exists():raise FileExistsError(proposed)
    inherited=resource.getrlimit(resource.RLIMIT_DATA)
    finite=[v for v in inherited if v!=resource.RLIM_INFINITY]
    cap=min([args.data_cap_bytes,*finite])
    if cap<=0:raise ValueError('Invalid DATA cap')
    resource.setrlimit(resource.RLIMIT_DATA,(cap,cap))
    report={'schema':'78718-next-restart-weighted-residual-diagnostic-v1',
        'status':'STARTED_READ_ONLY_RESTART_DIAGNOSTIC','mode':args.mode,
        'observed_start_utc':datetime.now(timezone.utc).isoformat(),
        'script':identity(__file__),'launch':identity(args.launch),
        'failed_checkpoint':identity(args.checkpoint),'sys_executable':sys.executable,
        'sys_version':sys.version,'effective_DATA':list(resource.getrlimit(resource.RLIMIT_DATA)),
        'BVP_Newton_DN_calls':0,'Jacobian_or_LU_constructions':0,
        'recovers_old_final_weighted_cubic':False,'certificate_or_solver_success_claimed':False}
    start=time.monotonic();code=2
    try:
        import numpy as np
        from scipy.integrate import _bvp
        launch=json.loads(args.launch.read_text())
        if sys.executable!=launch['command'][0]:raise ValueError('Interpreter differs from launch')
        settings=launch['settings']
        if not (settings['modes']==14 and settings['angular']==512 and settings['tol']==2e-9):
            raise ValueError('This diagnostic is fixed to the original M14/N512/tol')
        script_dir=Path(launch['command'][1]).parent
        audit=module('restart_diagnostic_frozen_auditor',script_dir/'db6f-prefix-audit-spectral-true-m14-direct-csc.py')
        context=audit.c.validate_inputs(launch)
        failed=audit.read(args.checkpoint)
        if failed['solver_success'] is not False:raise ValueError('Expected the preserved failed CP')
        for key in audit.FIXED_FIELDS:
            audit.equal(failed[key],context['seed'][key],'Changed fixed physical definition: '+key)
        # Verify the saved coefficient closure, but do not call a source flow.
        _,chunks,_=audit.polynomial_endpoint(failed,context)
        report['coefficient_files']=chunks
        argv=launch['delegated_parser_argv']
        option=lambda key:argv[argv.index(key)+1]
        source_root=Path(option('--source-root'))
        profile_path=Path(option('--profile'));chart_path=Path(option('--chart'))
        port_path=Path(option('--linear-port'))
        runner=module('restart_diagnostic_original_flat',script_dir/'db6f-prefix-flat-coupled.py').m
        runner.adaptive.old.install_source(source_root)
        cfg=json.loads(profile_path.read_text());chart=json.loads(chart_path.read_text())
        port=json.loads(port_path.read_text());port['_sha256']=sha(port_path.read_bytes())
        _,Base=runner.adaptive.build_classes(chart)
        class DiagnosticBVP(runner.TailMixin,Base):
            pass
        obj=DiagnosticBVP(cfg,port,failed['gauge_amplitude'],14,512,True,failed['warp_reference_q'])
        obj.restart_remesh=settings['nodes']
        obj.bcweights=np.full(obj.M,settings['physical_bc_tol']/settings['bc_tol'])
        class NoNewTail:
            def solve(self,*a,**k):
                raise RuntimeError('A new tail solve is forbidden in this diagnostic')
        obj.tail=NoNewTail()
        restart=module('restart_diagnostic_original_preserve',script_dir/'db6f-prefix-preserve-restart.py')
        spectral=module('restart_diagnostic_original_weights',script_dir/'db6f-root-spectral-collocation-v2.py')
        for name,callback in [('fun',obj.fun),('initial',obj.initial),('chart',obj.chart),('restart',restart.restart)]:
            audit.c.h.check_callback(callback,launch['callbacks'][name])
        x,y,p,restart_info=restart.restart(obj,args.checkpoint,chart)
        flow=obj.flow(p[0]);audit.c.h.check_callback(flow.fun,launch['callbacks']['physical_fun'])
        w=spectral.power2_weights(14)
        if w.tolist()!=launch['weights']:raise ValueError('Original W14 weights differ')
        u=w[:,None]*y
        if not np.array_equal(u/w[:,None],y):raise ValueError('Original power-of-two round trip failed')
        report.update(settings={k:settings[k]for k in ('modes','angular','tol','bc_tol','physical_bc_tol')},
            restart=restart_info,actual_restart_nodes=len(x),state_components=obj.n,
            old_saved_nodes=failed['nodes'],fixed_physical_fields_unchanged=True,
            setup_seconds=time.monotonic()-start,
            frozen_RHS=launch['callbacks']['fun'],frozen_physical_RHS=launch['callbacks']['physical_fun'],
            frozen_restart=launch['callbacks']['restart'],
            scipy_source=identity(Path(_bvp.__file__)),
            original_spectral_weights_source=identity(script_dir/'db6f-root-spectral-collocation-v2.py'))
        # Exactly the original v2 diagonal-conjugacy RHS formula.
        def weighted_fun(xx,uu,pp):
            return w[:,None]*obj.fun(xx,uu/w[:,None],pp)
        indexes=np.unique(np.linspace(0,len(x)-1,64,dtype=int))
        before=time.monotonic();values=weighted_fun(x[indexes],u[:,indexes],p)
        pilot_seconds=time.monotonic()-before
        if not np.all(np.isfinite(values)):raise ValueError('Nonfinite pilot RHS')
        pilot={'radial_points':len(indexes),'selection':'64 evenly distributed saved-restart indices',
            'RHS_seconds':pilot_seconds,'outputs_finite':True,
            'peak_RSS_bytes':int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)*1024,
            'estimated_full_RHS_radial_evaluations':4*len(x)-3,
            'linear_time_estimate_seconds':pilot_seconds*(4*len(x)-3)/len(indexes),
            'estimate_is_not_a_time_upper_bound':True}
        report['pilot']=pilot
        print(json.dumps({'event':'pilot_complete',**pilot}),flush=True)
        if args.mode=='full':
            stages=[]
            def measured_fun(xx,uu,pp):
                before=time.monotonic();value=weighted_fun(xx,uu,pp)
                row={'call':len(stages)+1,'radial_points':len(xx),'seconds':time.monotonic()-before}
                stages.append(row);print(json.dumps({'event':'full_RHS_sweep',**row}),flush=True)
                return value
            h=np.diff(x)
            before=time.monotonic()
            col_res,y_middle,f,f_middle=_bvp.collocation_fun(measured_fun,u,p,x,h)
            r_middle=1.5*col_res/h
            sol=_bvp.create_spline(u,f,x,h)
            rms=_bvp.estimate_rms_residuals(measured_fun,sol,x,h,p,r_middle,f_middle)
            if not np.all(np.isfinite(rms)):raise ValueError('Nonfinite full weighted RMS')
            tol=settings['tol']
            insert_1,=np.nonzero((rms>tol)&(rms<100*tol))
            insert_2,=np.nonzero(rms>=100*tol)
            added=len(insert_1)+2*len(insert_2)
            storage=io.BytesIO();np.savez(storage,restart_mesh=x,weighted_rms=rms)
            blob=gzip.compress(storage.getvalue(),mtime=0)
            if len(blob)>=5_000_000:raise ValueError('Diagnostic interval file exceeds size limit')
            with proposed.open('xb')as stream:stream.write(blob)
            report['full']={'full_RHS_sweeps':stages,'RHS_radial_evaluations':sum(r['radial_points']for r in stages),
                'calculation_seconds':time.monotonic()-before,'weighted_RMS_max':float(np.max(rms)),
                'intervals':len(rms),'intervals_requiring_one_new_node':len(insert_1),
                'intervals_requiring_two_new_nodes':len(insert_2),'requested_additional_nodes':added,
                'next_mesh_nodes_from_this_initial_guess':len(x)+added,'original_max_nodes':settings['max_nodes'],
                'would_exceed_original_max_nodes':len(x)+added>settings['max_nodes'],
                'interval_data':identity(proposed),
                'scope':'Original SciPy estimates on the next restart initial guess, before any Newton. Not the previous run final cubic and not a solver convergence prediction.'}
            if len(stages)!=4:raise ValueError('Expected exactly four full original RHS sweeps')
        report['status']='COMPLETED_READ_ONLY_RESTART_RESIDUAL_DIAGNOSTIC'
        code=0
    except Exception as exc:
        report.update(status='FAILED_READ_ONLY_RESTART_DIAGNOSTIC',error=repr(exc),traceback=traceback.format_exc())
    report['seconds']=time.monotonic()-start
    report['observed_end_utc']=datetime.now(timezone.utc).isoformat()
    report['peak_RSS_bytes']=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)*1024
    raw=(json.dumps(report,indent=2,ensure_ascii=False,allow_nan=False)+'\n').encode()
    if len(raw)>=100_000:raise ValueError('Unexpectedly large diagnostic summary')
    with args.out.open('xb')as stream:stream.write(raw)
    print(json.dumps({'status':report['status'],'mode':args.mode,'seconds':report['seconds'],
        'report_bytes':len(raw),'report_sha256':sha(raw),'BVP_Newton_DN_calls':0,
        **({'error':report['error']}if'error'in report else{}),
        **({'requested_additional_nodes':report['full']['requested_additional_nodes'],
            'next_mesh_nodes_from_this_initial_guess':report['full']['next_mesh_nodes_from_this_initial_guess'],
            'weighted_RMS_max':report['full']['weighted_RMS_max']}if'full'in report else{})}),flush=True)
    return code


if __name__=='__main__':raise SystemExit(main())
