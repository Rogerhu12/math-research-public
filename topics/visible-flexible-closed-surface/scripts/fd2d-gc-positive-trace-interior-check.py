#!/usr/bin/env python3
"""One immutable-field check of new pointwise Gauss/curvature row derivatives."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,datetime,json,resource,time,traceback
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity,load_npz
from fd2d_gc_raw_bump_positive_trace import PositiveTraceRawBumpDAE
from fd2d_gc_positive_trace_interior_merit import interior_gauss_curvature

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('field','candidate','radius-packet','reference-inlet','out-prefix'):ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--reference-cache',type=Path);args=ap.parse_args();stem=args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):raise FileExistsError('Use a fresh prefix')
    start=time.monotonic();here=Path(__file__).resolve().parent
    report=dict(schema='fd2d-selected-interior-actual-Gauss-curvature-JVP-v1',source=identity(__file__),
        helper=identity(here/'fd2d_gc_positive_trace_interior_merit.py'),input=identity(args.field),candidate=identity(args.candidate),
        started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),completed=False,no_BVP=True,continuous_certificate=False)
    def save():
        report.update(seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        stem.with_name(stem.name+'-report.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    save()
    try:
        a=load_npz(args.field);proof=json.loads(args.radius_packet.read_text())
        if not proof['passed'] or proof['candidate_sha256']!=report['candidate']['sha256']:raise ValueError('Radius proof identity mismatch')
        p=PositiveTraceRawBumpDAE(args.candidate,modes=int(a['modes']),max_step=.04,gap=.9,
            reference_inlet=args.reference_inlet,reference_cache=args.reference_cache,base_lower_bound='4/5',
            base_lower_provenance={**identity(args.radius_packet),'candidate_sha256':proof['candidate_sha256']},radius_floor=.1,minimum_active_n=.05)
        if not np.array_equal(a['mesh'],p.x):raise ValueError('Actual mesh mismatch')
        for key in ('angular_atlas_definition','gauss_l_definition','positive_trace_definition'):
            if json.loads(str(a[key]))!=getattr(p,key):raise ValueError('Actual field identity mismatch')
        z=np.r_[a['corrections'].ravel(),a['parameters']];out=interior_gauss_curvature(p,z,jacobian=True)
        report['actual']=out['info'];directions=[]
        v=np.zeros(p.size);v[:p.N*p.q]=.03*np.sin(.7+np.arange(p.N*p.q)*.43);directions.append(('two_endpoint_state_columns',v))
        v=np.zeros(p.size);off=p.N*p.q
        v[off+p.tail_parameter_slice.start:off+p.tail_parameter_slice.stop]=.02*np.cos(.2+np.arange(p.tail_parameter_slice.stop-p.tail_parameter_slice.start)*.71)
        v[off+p.profile_parameter_slice.start:off+p.profile_parameter_slice.stop]=.0003*np.sin(.5+np.arange(p.profile_parameter_slice.stop-p.profile_parameter_slice.start)*.87)
        directions.append(('all_tail_and_nonzero_physical_profile_columns',v));checks=[]
        for name,v in directions:
            for step in (2e-5,1e-5):
                plus=interior_gauss_curvature(p,z+step*v,jacobian=False);minus=interior_gauss_curvature(p,z-step*v,jacobian=False)
                for group in ('retained','high','curvature'):
                    exact=out[group+'_jacobian']@v
                    if plus[group+'_residual'].shape!=exact.shape or minus[group+'_residual'].shape!=exact.shape:raise ValueError('Curvature active labels changed')
                    fd=(plus[group+'_residual']-minus[group+'_residual'])/(2*step);error=fd-exact
                    checks.append(dict(direction=name,step=step,group=group,rows=len(exact),analytic_norm=float(np.linalg.norm(exact)),
                        absolute_maximum=float(np.max(abs(error),initial=0)),relative_L2=float(np.linalg.norm(error)/max(np.linalg.norm(exact),1e-12))))
        report.update(completed=True,checks=checks,maximum_relative_L2=max(c['relative_L2'] for c in checks));save()
        print(json.dumps({'completed':True,'actual':report['actual'],'maximum_relative_L2':report['maximum_relative_L2']}),flush=True)
    except Exception as exc:
        report['exception']=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc());save();raise

if __name__=='__main__':main()
