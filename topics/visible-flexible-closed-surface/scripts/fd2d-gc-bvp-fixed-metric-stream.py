#!/usr/bin/env python3
"""Angular refinement with the original physical coast T held exactly fixed.

The original native field supplies T. The last parameter is now auxiliary:
it has zero ODE derivative and the last boundary equation is T_aux-T_fixed.
The central gap is free and measured. All other central/tail equations and
the original collocation tolerances/acceptance rules are unchanged. The tail
is still the explicitly labelled finite linear starter.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import gzip, importlib.util, io, json, resource, sys, threading, time
from pathlib import Path
import numpy as np
import fd2d_gc_archive_arrays as archive
import fd2d_gc_stream_csc as streaming

HERE=Path(__file__).resolve().parent


def main():
    arguments=sys.argv[1:]
    anchor=Path(arguments[arguments.index('--warm-field')+1])
    stem=Path(arguments[arguments.index('--out-prefix')+1])
    anchor_data=archive.load_npz(anchor)
    fixed_T=float(anchor_data['parameters'][-1]); del anchor_data
    source=HERE/'fd2d-gc-bvp-design-warm.py'
    spec=importlib.util.spec_from_file_location('fd2d_fixed_metric_warm_target',source)
    warm=importlib.util.module_from_spec(spec); spec.loader.exec_module(warm)
    Parent=warm.Problem
    class FixedMetricProblem(Parent):
        def activate(self,p):
            self.flow.candidate.set_parameter(fixed_T)
        def fun_jac(self,x,y,p):
            self.runtime['phase']='analytic_jacobian_fixed_metric'; self.activate(p)
            return self.flow.jacobian(x,y),np.zeros((self.q,len(p),y.shape[1]))
        def bc(self,ya,yb,p):
            value=super().bc(ya,yb,p); value[-1]=p[-1]-fixed_T
            return value
        def bc_jac(self,ya,yb,p):
            left,right,parameter=super().bc_jac(ya,yb,p)
            left[-1]=0.; right[-1]=0.; parameter[-1]=0.; parameter[-1,-1]=1.
            return left,right,parameter
        def diagnostics(self,x,y,p):
            value=super().diagnostics(x,y,p)
            value.update(actual_physical_T=fixed_T, gap_constraint_active=False,
                same_physical_metric_at_every_iteration=True)
            return value
    warm.Problem=FixedMetricProblem
    warm.save_npz=archive.save_npz
    warm.__doc__=__doc__
    warm.__file__=__file__
    record=stem.parent/'stream-resources'/(stem.name+'.jsonl')
    if record.exists():
        raise FileExistsError(record)
    record.parent.mkdir(parents=True,exist_ok=True)
    started=time.monotonic(); stop=threading.Event()
    def snapshot(event):
        return dict(event=event,utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
            seconds=time.monotonic()-started,
            maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            streaming=dict(streaming.STATUS),newton=dict(warm.newton.STATS),fixed_T=fixed_T)
    def append(item):
        with record.open('a') as f:
            f.write(json.dumps(item,allow_nan=False)+'\n')
    def heartbeat():
        while not stop.wait(5.):
            append(snapshot('heartbeat'))
    thread=threading.Thread(target=heartbeat,daemon=True)
    first=snapshot('start'); first.update(source=archive.identity(__file__),
        parent_source=archive.identity(source),archive_source=archive.identity(archive.__file__),
        anchor=archive.identity(anchor),physical_metric_is_fixed=True,
        last_ODE_parameter_column_exactly_zero=True,central_gap_is_free=True)
    append(first); streaming.install(); thread.start()
    try:
        warm.main()
    finally:
        stop.set(); thread.join(timeout=1.); append(snapshot('wrapper_exit'))
        report_path=stem.with_name(stem.name+'-report.json')
        if report_path.exists():
            report=json.loads(report_path.read_text())
            report.update(schema='fd2d-fixed-metric-angular-refinement-v1',scope=__doc__,
                physical_metric_frozen_for_refinement=True,fixed_physical_T=fixed_T,
                gap_constraint_active=False,parent_frontend=archive.identity(source),
                archive_source=archive.identity(archive.__file__),streaming_source=archive.identity(streaming.__file__))
            if 'parameters' in report and report['parameters']['T']!=fixed_T:
                report['fixed_T_storage_mismatch']=True
                report['physical_parameter_in_report_before_normalization']=report['parameters']['T']
                report['parameters']['T']=fixed_T
            report_path.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
        print(json.dumps(snapshot('fixed_metric_wrapper_done')),flush=True)


if __name__=='__main__':
    main()
