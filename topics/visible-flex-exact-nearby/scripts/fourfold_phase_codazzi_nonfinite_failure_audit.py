#!/usr/bin/env python3
"""Make an explicit strict-JSON audit of the preserved log-chart overflow.

The v1 runner's success flag was false, but max(0, NaN) left misleading
zero initialized residual fields. They are not bounds and are not retained
as such. This audit preserves identities and invalidates those diagnostics.
"""
from __future__ import annotations
import argparse,gzip,hashlib,io,json,math
from pathlib import Path
import numpy as np


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def sanitize(value):
    if isinstance(value,float) and not math.isfinite(value):return None
    if isinstance(value,dict):return {k:sanitize(v) for k,v in value.items()}
    if isinstance(value,list):return [sanitize(v) for v in value]
    return value


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--raw-report',type=Path,default=Path('notes/2026-11-13-codazzi-logC-direct-m24-raw-failure.txt'))
    p.add_argument('--candidate',type=Path,default=Path('notes/2026-11-13-codazzi-logC-direct-m24-candidate.npz.gz'))
    p.add_argument('--out',type=Path,required=True);args=p.parse_args()
    old=json.loads(args.raw_report.read_text())
    if old['success'] or any(a['success'] for a in old['attempts']):raise ValueError('this is not the preserved failed run')
    failed_source=Path(__file__).with_name('fourfold_phase_codazzi_log_curvature_bvp_probe_v1_failed.py')
    if sha(failed_source)!=old['source_sha256']:raise ValueError('preserved v1 source identity mismatch')
    with np.load(io.BytesIO(gzip.decompress(args.candidate.read_bytes())),allow_pickle=False) as saved:
        finite=bool(np.all(np.isfinite(saved['piece_coefficients'])))
        nonfinite=int(np.size(saved['piece_coefficients'])-np.count_nonzero(np.isfinite(saved['piece_coefficients'])))
    doc=dict(kind='explicit_preserved_nonfinite_Codazzi_BVP_failure_audit',success=False,certified=False,
        source_sha256=sha(__file__),raw_report_path=str(args.raw_report),raw_report_sha256=sha(args.raw_report),
        failed_source_path=str(failed_source),failed_source_sha256=sha(failed_source),
        candidate_path=str(args.candidate),candidate_sha256=sha(args.candidate),
        candidate_coefficients_finite=finite,nonfinite_candidate_coefficient_count=nonfinite,
        original_object_sha256=old['object_sha256'],solver_attempts=sanitize(old['attempts']),
        diagnostics_valid=False,finite_PDE_residual=None,full_B_residual=None,full_C_residual=None,
        diagnosis='The log-chart Newton iterate overflowed/underflowed and the collocation solve stopped. V1 initialized maxima stayed at zero when compared with NaN. None of these zero fields is a residual bound.',
        correction='The main log-chart runner now rejects nonfinite diagnostics and writes null, with valid=false; nonfinite candidates cannot be used as guesses.',
        corrected_runner_sha256=sha(Path(__file__).with_name('fourfold_phase_codazzi_log_curvature_bvp_probe.py')),
        scope='A preserved floating failure only. This does not affect any R120-R129 directed proof or assert surface nonexistence.')
    args.out.write_text(json.dumps(doc,indent=2,allow_nan=False)+'\n')
    print(dict(diagnostics_valid=False,candidate_coefficients_finite=finite,nonfinite_coefficients=nonfinite))


if __name__=='__main__':main()
