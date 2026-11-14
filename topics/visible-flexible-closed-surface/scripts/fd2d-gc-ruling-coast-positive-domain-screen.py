#!/usr/bin/env python3
"""Actual saved-field positive-n screen restricted to the chosen coast window.
Finite samples only: this does not infer continuous positivity or reject
geometric solutions outside the selected future representation domain.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,json,time,resource
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity
from fd2d_gc_ruling_atlas_native_field import RulingAtlasRawBumpNativeField
from fd2d_gc_raw_bump_coast_reference import coast_window


def main():
    ap=argparse.ArgumentParser()
    for k in ('field','candidate','reference-inlet','out-prefix'):ap.add_argument('--'+k,type=Path,required=True)
    ap.add_argument('--reference-cache',type=Path);ap.add_argument('--angles',type=int,default=512)
    args=ap.parse_args();stem=args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):raise FileExistsError('Fresh stem required')
    start=time.monotonic();field=RulingAtlasRawBumpNativeField(args.field,args.candidate,
        reference_inlet=args.reference_inlet,reference_cache=args.reference_cache)
    e,f=field.angular_atlas.entry_s,field.angular_atlas.exit_s
    mesh=field.nodes;indices=np.flatnonzero((mesh[:-1]>=e)&(mesh[1:]<=f))
    fractions=np.array([0.,.125,.25,.5,.75,.875,1.])
    positions=np.unique(np.concatenate([mesh[j]+fractions*(mesh[j+1]-mesh[j]) for j in indices]))
    xi=2*np.pi*np.arange(args.angles)/args.angles;rows=[]
    for s in positions:
        q=field.evaluate_native(np.full_like(xi,s),xi)
        w,_=coast_window([s],e,f-e,.12)
        j=int(np.argmin(q['n']))
        rows.append(dict(s=float(s),w=float(w[0]),n_min=float(q['n'][j]),n_max=float(np.max(q['n'])),
            xi_of_min=float(xi[j]),material_u_of_min=float(q['u'][j]),
            maximum_abs_n_xi=float(np.max(abs(q['n_xi']))),maximum_abs_n_x=float(np.max(abs(q['n_x'])))))
    active=[r for r in rows if r['w']>0]
    report=dict(schema='fd2d-coast-only-positive-n-actual-finite-domain-screen-v1',source=identity(__file__),
        field=identity(args.field),candidate=identity(args.candidate),reference_inlet=identity(args.reference_inlet),
        provider=identity(Path(__file__).parent/'fd2d_gc_ruling_atlas_native_field.py'),
        angles=args.angles,radial_samples=len(rows),coast=[e,f],cell_indices=indices.tolist(),rows=rows,
        minimum_on_active_samples=min(r['n_min'] for r in active),minimum_on_closed_coast_samples=min(r['n_min'] for r in rows),
        proposed_exact_representation_domain='n(s,xi)>0 for every point with fixed coast weight w(s)>0; no division or condition outside this window',
        continuous_positive_certificate=False,nonlinear_solve_performed=False,tail_n_zero_not_excluded=True,
        seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    p=stem.with_name(stem.name+'-report.json');p.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(report=identity(p),minimum_active=report['minimum_on_active_samples'],minimum_closed=report['minimum_on_closed_coast_samples'],seconds=report['seconds'])),flush=True)
if __name__=='__main__':main()
