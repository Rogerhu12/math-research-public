#!/usr/bin/env python3
"""One same-p/g actual-objective comparison of the explicit R162 initial field.

Both fields use the frozen current provider. The proposed node fade changes
raw coefficients; it is neither exact re-expression nor another BVP.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,datetime,json,resource,time,traceback
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity,load_npz,save_npz
from fd2d_gc_raw_bump_positive_trace import PositiveTraceRawBumpDAE
from fd2d_gc_existing_tail_reference import zero_tail_plateau_corrections
from fd2d_gc_positive_trace_value_objective import actual_finite_objective


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('field','candidate','radius-packet','reference-inlet','out-prefix'):ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--reference-cache',type=Path);ap.add_argument('--fade-start',type=float,default=1.3)
    args=ap.parse_args();stem=args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):raise FileExistsError('Use a fresh stem')
    start=time.monotonic();here=Path(__file__).resolve().parent
    report=dict(schema='fd2d-R162-same-physical-parameters-complete-objective-choice-v1',source=identity(__file__),
        helpers={n:identity(here/n) for n in ('fd2d_gc_existing_tail_reference.py','fd2d_gc_positive_trace_value_objective.py','fd2d_gc_raw_bump_positive_trace.py','fd2d_gc_positive_trace_interior_merit.py')},
        input=identity(args.field),candidate=identity(args.candidate),started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        completed=False,no_BVP=True,no_Jacobian=True,continuous_certificate=False)
    def save():
        report.update(seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        stem.with_name(stem.name+'-report.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    save()
    try:
        a=load_npz(args.field);proof=json.loads(args.radius_packet.read_text())
        if not proof['passed'] or proof['candidate_sha256']!=report['candidate']['sha256']:raise ValueError('Radius packet mismatch')
        problem=PositiveTraceRawBumpDAE(args.candidate,modes=int(a['modes']),max_step=.04,gap=.9,
            reference_inlet=args.reference_inlet,reference_cache=args.reference_cache,base_lower_bound='4/5',
            base_lower_provenance={**identity(args.radius_packet),'candidate_sha256':proof['candidate_sha256']},radius_floor=.1,minimum_active_n=.05)
        if not np.array_equal(a['mesh'],problem.x):raise ValueError('Saved mesh mismatch')
        for key in ('angular_atlas_definition','coast_reference_definition','gauss_l_definition','positive_trace_definition'):
            if json.loads(str(a[key]))!=getattr(problem,key):raise ValueError('Actual definition differs: '+key)
        transformed=zero_tail_plateau_corrections(a['mesh'],a['corrections'],fade_start=args.fade_start,plateau_start=problem.trace_ramp_stop)
        new=dict(a);new['corrections']=transformed['corrections']
        new['explicit_initial_field_change']=np.array(json.dumps(dict(kind='R162 same-provider nodal raw fade',input_sha256=report['input']['sha256'],source_sha256=report['helpers']['fd2d_gc_existing_tail_reference.py']['sha256'],definition=transformed['info']),sort_keys=True))
        report['new_field']=save_npz(stem.with_name(stem.name+'-field.npz'),**new)
        report['change']=dict(definition=transformed['info'],actual_field_changed=True,physical_g_changed=False,physical_parameters_bytes_preserved=bool(np.array_equal(a['parameters'],new['parameters'])),
            other_original_arrays_bytes_preserved=all(a[k].dtype==new[k].dtype and a[k].shape==new[k].shape and a[k].tobytes()==new[k].tobytes() for k in a if k!='corrections'),
            maximum_raw_coefficient_change=float(np.max(abs(new['corrections']-a['corrections']))))
        oldz=np.r_[a['corrections'].ravel(),a['parameters']];newz=np.r_[new['corrections'].ravel(),new['parameters']]
        report['old']=actual_finite_objective(problem,oldz);save()
        report['new']=actual_finite_objective(problem,newz)
        report['new_objective_smaller']=report['new']['objective_squared']<report['old']['objective_squared']
        report['automatic_replace_live_state']=False;report['completed']=True;save()
        print(json.dumps({'completed':True,'old_objective_norm':report['old']['objective_norm'],'new_objective_norm':report['new']['objective_norm'],
            'old_raw':report['old']['raw_maximum'],'new_raw':report['new']['raw_maximum'],'new_objective_smaller':report['new_objective_smaller'],'new_field':report['new_field']}),flush=True)
    except Exception as exc:
        report['exception']=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc());save();raise


if __name__=='__main__':main()
