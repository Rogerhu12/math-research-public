#!/usr/bin/env python3
"""Prepare or run the independent R671 complete-field QP in public Actions.

The frozen old launcher supplies its full argv through --print-command only.
This file replaces that driver's path and explicitly supplies the new tail
context. It never imports a field module. Actual migration, field evaluation
and solving require GITHUB_ACTIONS=true. No old field acceptance is inherited.
"""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import shlex
import subprocess
import sys


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as source:
        for block in iter(lambda: source.read(1024*1024), b''):
            digest.update(block)
    return digest.hexdigest()


def replace_flag(command, flag, value):
    if command.count(flag) != 1:
        raise ValueError('Expected one literal flag: '+flag)
    command[command.index(flag)+1] = str(value)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--work', type=Path, required=True)
    parser.add_argument('--bundle', type=Path, required=True)
    parser.add_argument('--carrier', type=Path, required=True)
    parser.add_argument('--manifest', type=Path, action='append', required=True)
    parser.add_argument('--node-report', type=Path, required=True)
    parser.add_argument('--scalar-input', type=Path, required=True)
    parser.add_argument('--eta-start-node', type=int, required=True)
    parser.add_argument('--lambda-value', type=float, required=True)
    parser.add_argument('--source-lambda', type=float)
    parser.add_argument('--migration', choices=('keep-q', 'nodal-projection'), required=True)
    parser.add_argument('--outdir', type=Path)
    parser.add_argument('--source-launcher', type=Path)
    parser.add_argument('--driver', type=Path)
    parser.add_argument('--exact-tail-source', type=Path)
    parser.add_argument('--damping', type=float, required=True)
    parser.add_argument('--maxiter', type=int, default=256)
    parser.add_argument('--directions', type=int, default=1)
    parser.add_argument('--active-rows', type=int, default=192)
    parser.add_argument('--qp-rtol', type=float, default=1e-6)
    parser.add_argument('--qp-atol', type=float, default=1e-12)
    parser.add_argument('--reach-safety-factor', type=float, default=.992)
    parser.add_argument('--active-band', type=float, default=.025)
    parser.add_argument('--coarse-centers')
    parser.add_argument('--print-command', action='store_true')
    args = parser.parse_args()
    if (not math.isfinite(args.lambda_value) or not 0 <= args.lambda_value <= 1
            or args.eta_start_node < 1):
        raise ValueError('Supply an interior original eta node and fixed lambda in [0,1]')
    if args.source_lambda is not None and (not math.isfinite(args.source_lambda)
            or not 0 <= args.source_lambda <= 1):
        raise ValueError('A declared source lambda must lie in [0,1]')
    if (not math.isfinite(args.damping) or args.damping <= 0
            or args.maxiter < 1 or args.directions < 1 or args.active_rows < 1
            or not 0 < args.active_band < args.reach_safety_factor < 1):
        raise ValueError('Invalid explicit full-QP numerical parameters')
    repo, work = args.repo.resolve(), args.work.resolve()
    topic = repo/'topics/visible-flex-larger-amplitude'
    source = topic/'scripts/resume_20261120'
    notes = topic/'notes'
    original = (args.source_launcher or source/'launch_full_phi_qp_actions.py').resolve()
    driver = (args.driver or source/'fullclosed_gauss_exact_tail_inequality_qp.py').resolve()
    factory = (args.exact_tail_source or source/'exact_reference_tail_lift.py').resolve()
    output = args.outdir.resolve() if args.outdir else work/'exact-tail-full-phi'
    prepare = [sys.executable, str(original), '--repo', str(repo), '--work', str(work),
        '--bundle', str(args.bundle.resolve()), '--carrier', str(args.carrier.resolve()),
        '--outdir', str(output), '--damping', str(args.damping),
        '--maxiter', str(args.maxiter), '--directions', str(args.directions),
        '--active-rows', str(args.active_rows), '--qp-rtol', str(args.qp_rtol),
        '--qp-atol', str(args.qp_atol), '--print-command']
    for manifest in args.manifest:
        prepare.extend(['--manifest', str(manifest.resolve())])
    if args.coarse_centers is not None:
        prepare.extend(['--coarse-centers', args.coarse_centers])
    prepared = subprocess.run(prepare, text=True, capture_output=True, check=True)
    command = shlex.split(prepared.stdout.strip())
    if len(command) < 3 or Path(command[2]).name != 'fullclosed_gauss_inequality_qp.py':
        raise ValueError('The frozen launcher did not return its declared complete-field driver')
    command[2] = str(driver)
    replace_flag(command, '--reach-safety-factor', args.reach_safety_factor)
    replace_flag(command, '--active-band', args.active_band)
    additions = {
        'exact-tail-source': factory,
        'tail-node-report': args.node_report.resolve(),
        'tail-scalar-input': args.scalar_input.resolve(),
        'tail-scalar-source': notes/'2026-11-17-parallel-model-full-hold-oracle.py',
        'tail-integer-source': notes/'2026-11-17-parallel-inward-integral-enclosure.py',
        'tail-hold-source': topic/'scripts/parallel_20261117_negative_hold_profile_ivp.py',
        'tail-eta-start-node': args.eta_start_node,
        'tail-lambda': args.lambda_value,
        'tail-migration': args.migration,
    }
    if args.source_lambda is not None:
        additions['tail-parent-lambda'] = args.source_lambda
    for flag, value in additions.items():
        command.extend(['--'+flag, str(value)])
    if args.print_command:
        print(shlex.join(command))
        return
    if os.environ.get('GITHUB_ACTIONS') != 'true':
        raise SystemExit('Scientific R671 construction and solving require public GitHub Actions; --print-command only prepares argv.')
    files = {driver, original, Path(__file__).resolve()}
    explicit_paths = {'--operator', '--implementation', '--helpers', '--bundle',
        '--observations', '--witness-input', '--radius-witness-input',
        '--tail-node-report', '--tail-scalar-input'}
    for index, value in enumerate(command[:-1]):
        if value.startswith('--') and (value.endswith('-source') or value in explicit_paths):
            files.add(Path(command[index+1]).resolve())
    for path in files:
        if not path.is_file():
            raise FileNotFoundError(path)
    if output.exists():
        raise FileExistsError('Use a new output directory for every actual new-model batch')
    plan_path = work/(output.name+'-command.json')
    if plan_path.exists():
        raise FileExistsError(plan_path)
    work.mkdir(parents=True, exist_ok=True)
    plan = dict(schema='public-actions-R671-complete-Phi-QP-command-v1',
        command=command, original_command_preparation=prepare,
        github_run_id=os.environ.get('GITHUB_RUN_ID'), github_sha=os.environ.get('GITHUB_SHA'),
        file_sha256={str(path): sha(path) for path in sorted(files)},
        parent_bundle=str(args.bundle.resolve()), output=str(output),
        eta_start_node=args.eta_start_node, fixed_lambda=args.lambda_value,
        explicit_source_lambda=args.source_lambda, migration=args.migration,
        same_target_metric=True, original_free_coordinates_preserved=True,
        physical_representation='q+f_lambda*er(Theta)+(h_lambda*H+k_lambda)*ez',
        inherited_parent_acceptance=False, inherited_continuous_certificates=False,
        all_new_field_consumers_require_tail_context=True,
        normalization='mean Phi half gradient/exact residual Hessian, external 1600/C0; explicit damping in mean units',
        step_norm='positive nu_c=24 integrated/physical-height norm; B_H uses b-h_lambda and coarse columns use the same norm',
        initial_QP_scope='Migrated field is fully read before z=0 feasibility; no Phase-I or automatic acceptance is claimed')
    plan_path.write_text(json.dumps(plan, indent=2, allow_nan=False)+'\n')
    env = os.environ.copy()
    env.update(PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='1',
        OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')
    subprocess.run(command, env=env, cwd=repo, check=True)


if __name__ == '__main__':
    main()
