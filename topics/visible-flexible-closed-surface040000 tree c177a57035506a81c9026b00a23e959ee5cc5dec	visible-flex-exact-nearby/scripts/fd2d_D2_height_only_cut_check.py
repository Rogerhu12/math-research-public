"""Finite checks of R135: proper alignment, a discrete flip, and a tilt."""
from __future__ import annotations
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,hashlib,json,time
from pathlib import Path
import numpy as np
from fd2d_D2_height_only_cut import height_only_cut_diagnostic
from fd2d_positive_flat_developable_family import PositiveFlatDevelopableFamily


def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def scalar(v):
    if isinstance(v,np.ndarray):return v.tolist()
    if isinstance(v,np.floating):return float(v)
    if isinstance(v,np.integer):return int(v)
    if isinstance(v,np.bool_):return bool(v)
    raise TypeError(type(v).__name__)


def transformed(tail,u,R,t):
    port=tail.cut_port(u)
    out={k:np.asarray(port[k])@R.T+(t if k=='X' else 0)
         for k in ('X','e1','e2','N','X_s','X_u','X_ss','X_su','X_uu')}
    out.update({k:port[k] for k in ('l','m','n')})
    return out


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    start=time.monotonic();u=2*np.pi*np.arange(128)/128
    axes=np.array([0.,np.pi/2,np.pi,3*np.pi/2])
    tail=PositiveFlatDevelopableFamily(np.full(8,1.0),plane_height=1.25)
    angle=.17
    Ry=np.array([[np.cos(angle),0,np.sin(angle)],[0,1.,0],[-np.sin(angle),0,np.cos(angle)]])
    definitions=[('vertical',np.eye(3),np.array([0.,0.,-.15])),
                 ('x_halfturn',np.diag([1.,-1.,-1.]),np.array([0.,0.,2.5])),
                 ('tilt',Ry,np.array([0.,0.,0.]))]
    rows=[]
    for name,R,t in definitions:
        cut=transformed(tail,u,R,t);axis=transformed(tail,axes,R,t)['X']
        result=height_only_cut_diagnostic(tail,u,cut,axis)
        result.update(name=name,known_rotation_max_error=float(np.max(abs(result['unconstrained_proper_registration']['rotation']-R))))
        rows.append(result)
    passed=(max(rows[0]['height_only_full_sample_vector_errors'].values())<1e-12 and
            abs(rows[0]['actual_Z_candidate']-1.1)<1e-12 and
            rows[0]['ordered_axis_signs_positive_given_error_bounds'] and
            not rows[1]['ordered_axis_signs_positive_given_error_bounds'] and
            max(rows[2]['axis_mirror_defects'].values())>.1 and
            all(q['known_rotation_max_error']<1e-12 for q in rows))
    here=Path(__file__).resolve().parent
    report=dict(schema='fd2d-r135-finite-registration-check-v1',passed=bool(passed),
        actual_execution=True,cases=rows,seconds=time.monotonic()-start,
        source_sha256={q.name:digest(q) for q in (Path(__file__),here/'fd2d_D2_height_only_cut.py',here/'fd2d_flat_core_geometry_recovery.py')},
        scope='Three rigidly transformed exact-tail fixtures; not an actual solved nonround prefix or continuous certificate.')
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2,default=scalar,allow_nan=False)+'\n')
    print(json.dumps(report,default=scalar,allow_nan=False))
    if not passed:raise SystemExit(1)
if __name__=='__main__':main()
