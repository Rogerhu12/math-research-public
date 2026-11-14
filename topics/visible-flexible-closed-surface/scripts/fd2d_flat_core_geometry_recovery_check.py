"""Actual finite check of the reconstructed R133 consumer, never a full certificate."""
from __future__ import annotations
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,hashlib,json,time
from pathlib import Path
import numpy as np
from fd2d_flat_core_geometry_recovery import (
    central_geometry,register_tail_from_actual_cut,flat_disk_cross_normal_balls,
    tail_budget_at_registered_height)
from fd2d_positive_flat_developable_family import PositiveFlatDevelopableFamily
from fd2d_flat_cut_prefix_candidate import FlatCutCandidate


def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def scalar(x):
    if isinstance(x,np.ndarray):return x.tolist()
    if isinstance(x,np.floating):return float(x)
    if isinstance(x,np.integer):return int(x)
    if isinstance(x,np.bool_):return bool(x)
    raise TypeError(type(x).__name__)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    root=Path(__file__).resolve().parent.parent
    parser.add_argument('--candidate',type=Path,default=root/'notes/2026-11-12-fd2d-flat-cut-prefix-v1-coast-compatible-candidate.json')
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    started=time.monotonic()
    candidate=FlatCutCandidate(json.loads(args.candidate.read_text()))
    u=2*np.pi*np.arange(64)/64
    ref=candidate.reference(np.full(len(u),candidate.end),u)
    flat=PositiveFlatDevelopableFamily(np.zeros(8),plane_height=1.25)
    registration=register_tail_from_actual_cut(flat,u,ref)
    central=central_geometry(np.zeros(7),samples=256)
    bent=PositiveFlatDevelopableFamily(np.ones(8),plane_height=1.25)
    port=bent.cut_port(u)
    az,ax=.23,.17
    Rz=np.array([[np.cos(az),-np.sin(az),0],[np.sin(az),np.cos(az),0],[0,0,1.]])
    Rx=np.array([[1.,0,0],[0,np.cos(ax),-np.sin(ax)],[0,np.sin(ax),np.cos(ax)]])
    R=Rz@Rx;t=np.array([.2,-.1,.37])
    actual={k:(v@R.T+(t if k=='X' else 0)) for k,v in port.items()
            if k in ('X','e1','e2','N','X_s','X_u','X_ss','X_su','X_uu')}
    actual.update({k:port[k] for k in ('l','m','n')})
    recovered=register_tail_from_actual_cut(bent,u,actual)
    rho=.136;Z=candidate.background_cut_height
    p=np.array([[0,0,Z+3*rho],[0,0,Z],[0,0,Z]])
    n=np.array([[0,0,1.],[0,0,1.],[1.,0,0]])
    cross=flat_disk_cross_normal_balls(p,n,flat,registration,angle_nodes=1025)
    maxjet=max(registration['full_sample_vector_errors'].values())
    rigid_error=max(np.max(abs(recovered['rotation']-R)),np.max(abs(recovered['translation']-t)))
    passed=(maxjet<1e-12 and rigid_error<1e-12 and
            abs(registration['actual_plane_height']-Z)<1e-12 and
            cross['covered_by_conditional_bound'][0] and
            not cross['covered_by_conditional_bound'][1] and
            np.min(cross['sampled_minimum_distances'][2])<1e-12)
    report=dict(schema='fd2d-r133-recovery-finite-check-v1',passed=bool(passed),
        actual_execution=True,candidate_sha256=digest(args.candidate),
        central=central['summary'],rotational_cut_height=Z,
        rotational_registration=registration,known_rigid_recovery=recovered,
        known_rigid_recovery_max_error=float(rigid_error),cross_probes=cross,
        conditional_tail_budget=tail_budget_at_registered_height(flat,registration,central['summary']['A']),
        sources={p.name:digest(p) for p in [Path(__file__),root/'scripts/fd2d_flat_core_geometry_recovery.py']},
        seconds=time.monotonic()-started,
        scope="Separate central and rotational fixtures. No nonround prefix, no interval evaluation certificate, no strong target.")
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2,default=scalar,allow_nan=False)+'\n')
    print(json.dumps(report,default=scalar,allow_nan=False))
    if not passed:raise SystemExit(1)
if __name__=='__main__':main()
