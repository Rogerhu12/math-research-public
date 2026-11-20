#!/usr/bin/env python3
"""Portable public-Actions entry for one complete-field Phi inequality batch.

Only constructs paths from --repo and caller-supplied data paths.  No old
bundle hash is substituted for a new reconstruction.  --print-command is
read-only; an actual scientific subprocess requires GitHub Actions.
"""
import argparse
import json
import os
from pathlib import Path
import shlex
import subprocess
import sys


R22 = ('.30,.60,.83,.99,.995,1.0,1.02,1.05,1.077134370991557,1.097,'
       '1.20,1.35,1.55,1.75,1.95,2.020292089293148,2.100560831276262,'
       '2.15,2.2410311297467116,2.26,2.301232686234047,2.321299871729826')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--work', type=Path, required=True)
    parser.add_argument('--bundle', type=Path, required=True)
    parser.add_argument('--carrier', type=Path, required=True)
    parser.add_argument('--manifest', type=Path, action='append', required=True)
    parser.add_argument('--outdir', type=Path)
    parser.add_argument('--damping', type=float, required=True)
    parser.add_argument('--maxiter', type=int, default=256)
    parser.add_argument('--directions', type=int, default=1)
    parser.add_argument('--active-rows', type=int, default=192)
    parser.add_argument('--qp-rtol', type=float, default=1e-6)
    parser.add_argument('--qp-atol', type=float, default=1e-12)
    parser.add_argument('--coarse-centers', default=R22)
    parser.add_argument('--print-command', action='store_true')
    args = parser.parse_args()
    repo, work = args.repo.resolve(), args.work.resolve()
    topic = repo/'topics/visible-flex-larger-amplitude'
    scripts, notes = topic/'scripts', topic/'notes'
    source = scripts/'resume_20261120'
    out = args.outdir.resolve() if args.outdir else work/'full-phi-inequality-v2'
    paths = {
        'operator': notes/'2026-11-17-parallel-geometry-fullclosed-gram-operator.py',
        'implementation': source/'gauss_observed_closed_gram.py',
        'base-batch-source': scripts/'resume_20261120_batched_closed_gram.py',
        'basis-source': scripts/'resume_20261120_physical_subspace.py',
        'coarse-source': scripts/'resume_20261120_physical_subspace_v3.py',
        'helpers': source/'fullclosed_lm.py',
        'coordinate-source': notes/'2026-11-17-parallel-root-fullclosed-integrated-coordinates.py',
        'scale-source': scripts/'integrated_l2_scale_20261120.py',
        'geometry-source': scripts/'resume_20261120_curvature_qp.py',
        'geometry-observed-source': scripts/'resume_20261120_curvature_qp_v3.py',
        'point-source': source/'fullclosed_point_cotangent_working.py',
        'height-source': source/'physical_height_coordinates.py',
        'angular-source': source/'angular_h2_coordinates.py',
        'qp-source': source/'fullspace_feasible_active_cg_v2.py',
        'inequality-source': source/'fullclosed_point_inequalities_v2.py',
        'spectral-source': source/'positive_spectral_gram_weights.py',
        'spectral-hessian-source': source/'positive_spectral_gram_hessian.py',
    }
    command = [sys.executable, '-u', str(source/'fullclosed_gauss_inequality_qp.py'),
        '--repo', str(repo), '--bundle', str(args.bundle.resolve()),
        '--observations', str(args.carrier.resolve()), '--outdir', str(out)]
    for key, path in paths.items():
        command.extend(['--'+key, str(path)])
    for manifest in args.manifest:
        command.extend(['--witness-input', str(manifest.resolve()),
                        '--radius-witness-input', str(manifest.resolve())])
    command.extend(['--objective', 'spectral', '--spectral-p', '8',
        '--spectral-epsilon', '.001', '--spectral-scale', '.05',
        '--angular-transition', '24', '--angles', '2048', '--stage-block', '64',
        '--legacy-fraction', '.5', '--low-modes', '12',
        '--coarse-centers', args.coarse_centers,
        '--reach-ratio', '.03', '--reach-safety-factor', '.992',
        '--active-max-rows', str(args.active_rows), '--active-block-columns', '32768',
        '--active-band', '.025', '--active-top-curvature', '16', '--active-top-radius', '2',
        '--max-directions', str(args.directions), '--maxiter', str(args.maxiter),
        '--damping', str(args.damping), '--qp-rtol', str(args.qp_rtol),
        '--qp-atol', str(args.qp_atol), '--qp-feasibility-tolerance', '2e-11',
        '--qp-row-rank-tolerance', '2e-12', '--line-trials', '15', '--target', '5e-7'])
    if args.print_command:
        print(shlex.join(command))
        return
    if os.environ.get('GITHUB_ACTIONS') != 'true':
        raise SystemExit('Topic README requires scientific computation in public GitHub Actions; use --print-command for preparation only.')
    for path in [source/'fullclosed_gauss_inequality_qp.py', *paths.values(),
                 args.bundle.resolve(), args.carrier.resolve(),
                 *(p.resolve() for p in args.manifest)]:
        if not path.is_file():
            raise FileNotFoundError(path)
    if out.exists():
        raise FileExistsError('Use a new output directory for a new actual batch')
    work.mkdir(parents=True, exist_ok=True)
    plan = dict(schema='public-actions-complete-Phi-QP-command-v1', command=command,
        github_run_id=os.environ.get('GITHUB_RUN_ID'),
        github_sha=os.environ.get('GITHUB_SHA'),
        parent_bundle=str(args.bundle.resolve()), output=str(out),
        actual_parent_values_reused_from_old_reports=False,
        normalization='mean Phi half gradient/exact residual Hessian, external 1600/C0; damping in the same mean units',
        step_norm='positive nu_c=24 complete integrated/physical-height norm with redundant same-norm coarse columns',
        zero_QP_start_must_pass_all_actual_permanent_points=True)
    plan_path = work/(out.name+'-command.json')
    if plan_path.exists():
        raise FileExistsError(plan_path)
    plan_path.write_text(json.dumps(plan, indent=2)+'\n')
    env = os.environ.copy()
    env.update(PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='1',
               OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')
    subprocess.run(command, env=env, cwd=repo, check=True)


if __name__ == '__main__':
    main()
