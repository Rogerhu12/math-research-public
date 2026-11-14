#!/usr/bin/env python3
"""Check only newly exposed tail derivative columns and unchanged raw F/J."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse,json,time
from pathlib import Path
import numpy as np
from fd2d_gc_raw_bump_dae import RawBumpDAE
from fd2d_gc_raw_bump_dae_check01_snapshot import RawBumpDAE as Previous
from fd2d_gc_archive_arrays import load_npz,identity


def mx(x):
    return float(np.max(abs(np.asarray(x)),initial=0.))


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--arrays',type=Path,required=True);ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--radius-packet',type=Path,required=True);args=ap.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    start=time.monotonic();a=load_npz(args.arrays);K=int(a['modes'])
    model=RawBumpDAE(args.candidate,modes=K)
    old=Previous(args.candidate,modes=K)
    if not np.array_equal(model.x,a['mesh']):raise ValueError('Wrong actual warm grid')
    vector=np.r_[a['corrections'].ravel(),a['parameters']]
    F,J,data=model.evaluate(vector,jacobian=True)
    of,oj,od=old.evaluate(vector,jacobian=True)
    diff=J-oj
    unchanged=dict(raw_F=mx(F-of),raw_J=mx(diff.data),fields=mx(data['fields']-od['fields']))
    del old,od,oj
    _,p=model.unpack(vector);delta=p[model.profile_slice];b=p[model.tail_slice]
    rng=np.random.default_rng(131016);direction=rng.standard_normal(K+1);direction/=np.linalg.norm(direction)
    rows=[]
    for h in (1e-5,1e-6):
        plus=model.lifting(delta,b+h*direction);minus=model.lifting(delta,b-h*direction)
        for key in ('values','x','xi'):
            jac=data['lift']['parameters' if key=='values' else key+'_parameters']
            exact=jac@direction;finite=(plus[key]-minus[key])/(2*h);err=finite-exact
            rows.append(dict(step=h,field=key,absolute_maximum=mx(err),
                relative_l2=float(np.linalg.norm(err)/max(1.,np.linalg.norm(exact)))))
    packet=json.loads(args.radius_packet.read_text())
    if not packet['passed'] or packet['candidate_sha256']!=model.profile.source_identity['sha256']:
        raise ValueError('The supplied proved radius packet does not bind this candidate')
    provenance=dict(**identity(args.radius_packet),candidate_sha256=packet['candidate_sha256'])
    positive=model.profile.check_positive(base_lower_bound='4/5',base_lower_provenance=provenance,
        radius_floor=.1)
    report=dict(schema='fd2d-bump-added-tail-derivative-columns-check-v1',
        source=identity(__file__),current_source=identity(Path(__file__).with_name('fd2d_gc_raw_bump_dae.py')),
        prior_source=identity(Path(__file__).with_name('fd2d_gc_raw_bump_dae_check01_snapshot.py')),
        candidate=identity(args.candidate),arrays=identity(args.arrays),
        unchanged_original=unchanged,tail_derivative_checks=rows,
        positive_domain_bound=positive,seconds=time.monotonic()-start,
        scope='Only exposed derivative fields and the identified scalar positivity domain; no BVP or geometry certificate')
    report['passed']=max(unchanged.values())==0 and max(r['relative_l2'] for r in rows)<2e-7
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(report=str(args.out),passed=report['passed'],seconds=report['seconds'],
        unchanged=unchanged,maximum_tail_relative_l2=max(r['relative_l2'] for r in rows))),flush=True)
    return 0 if report['passed'] else 1


if __name__=='__main__':raise SystemExit(main())
