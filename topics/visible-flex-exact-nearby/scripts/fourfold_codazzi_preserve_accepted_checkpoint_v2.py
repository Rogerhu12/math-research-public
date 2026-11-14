#!/usr/bin/env python3
"""Preserve one actual accepted nodal checkpoint as complete cubic shards.

No equation is solved and no solver outcome is inferred. In particular, an
unavailable execution handle and an unfinished original process record do
not establish an exit code, an allocation failure, or BVP convergence.
"""
from __future__ import annotations
import argparse,json,time
from pathlib import Path
import numpy as np
import scipy.integrate._bvp as bvp
from fourfold_codazzi_candidate_shards import save_candidate
from fourfold_phase_local_correction_probe import sha


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--checkpoint',type=Path,required=True)
    ap.add_argument('--original-process',type=Path,required=True)
    ap.add_argument('--original-log',type=Path,required=True)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--observed-session',type=int,required=True)
    ap.add_argument('--observed-exit-code',type=int)
    ap.add_argument('--observed-exit-message',default='No final solver result was available')
    args=ap.parse_args();tick=time.monotonic()
    if args.candidate.exists() or args.out.exists():raise FileExistsError('preserve earlier actual outcomes')
    with np.load(args.checkpoint,allow_pickle=False) as data:
        arrays={name:data[name].copy() for name in data.files}
    x=arrays['radial_nodes'];y=arrays['state'];dy=arrays['radial_derivative']
    meta=json.loads(str(arrays['metadata']))
    if y.shape!=dy.shape or y.shape[1]!=len(x) or np.any(np.diff(x)<=0):
        raise ValueError('incomplete accepted nodal data')
    if not all(np.all(np.isfinite(z)) for z in (x,y,dy)):
        raise ValueError('nonfinite saved accepted state')
    polynomial=bvp.create_spline(y,dy,x,np.diff(x))
    # This reproduces exactly the interpolation used by the original solver
    # for this particular accepted step. It is not its unobserved final step.
    meta.update(kind='complete_cubic_from_actual_accepted_checkpoint_without_final_solver_outcome',
        original_checkpoint_sha256=sha(args.checkpoint),original_metadata_kind=meta.get('kind'),
        final_solver_outcome_known=False,finite_BVP_success=False,mathematical_certificate=False)
    save_candidate(args.candidate,radial_nodes=x,piece_coefficients=polynomial.c,
        initial_state=y[:,0],metadata=np.array(json.dumps(meta)))
    original=json.loads(args.original_process.read_text())
    report=dict(kind='lossless_preservation_of_last_observed_complete_accepted_checkpoint',
        original_process_sha256=sha(args.original_process),original_process_complete=original.get('complete'),
        original_process_status=original.get('status'),original_process_record_unmodified=True,
        original_log_sha256=sha(args.original_log),checkpoint_sha256=sha(args.checkpoint),
        checkpoint_bytes=args.checkpoint.stat().st_size,original_checkpoint=str(args.checkpoint),
        radial_nodes=len(x),state_dimension=y.shape[0],full_cubic_shape=list(polynomial.c.shape),
        every_saved_state_and_derivative_used=True,source_sha256=sha(__file__),
        candidate_path=str(args.candidate),candidate_sha256=sha(args.candidate),
        observed_session=args.observed_session,session_handle_observation=args.observed_exit_message,
        actual_exit_code=args.observed_exit_code,actual_exit_cause=None,finite_BVP_convergence_not_established=True,
        this_preservation_does_not_resume_or_repeat_the_failed_session=True,
        mathematical_certificate=False,wall_seconds=time.monotonic()-tick)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(report,indent=2),flush=True)


if __name__=='__main__':main()
