#!/usr/bin/env python3
"""Bind the actual coarse-v7 terminal mu to the unchanged original full QP.

Adapter flags: --coarse-report PATH [--launcher PATH] [--print-command].
All other flags pass literally to launch_full_phi_qp_actions.py. Supply
explicit --directions and --qp-atol; the intended continuation is six
directions and zero absolute QP gradient tolerance. A copied --damping is
not accepted: the returned report and the actual parent bundle are bound.

Preparation imports no field code and reads only JSON and file bytes.
Actual scientific execution requires this repository's public Actions.
This adapter never rewrites a permanent-position manifest or a model.
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


COARSE_SCHEMA = 'fullclosed-coarse-exact-spectral-residual-Hessian-physical-H2-curvature-QP-v7'


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as source:
        for block in iter(lambda: source.read(1024*1024), b''):
            digest.update(block)
    return digest.hexdigest()


def value(argv, flag):
    if argv.count(flag) != 1:
        raise ValueError('Supply exactly one explicit '+flag+' VALUE')
    index = argv.index(flag)
    if index+1 == len(argv) or argv[index+1].startswith('--'):
        raise ValueError('Missing value after '+flag)
    return argv[index+1]


def main():
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument('--coarse-report', type=Path, required=True)
    parser.add_argument('--launcher', type=Path)
    parser.add_argument('--print-command', action='store_true')
    args, forward = parser.parse_known_args()
    if any(v == '--damping' or v.startswith('--damping=') for v in forward):
        raise ValueError('Use the actual returned final_damping, never a copied constant')
    if any(v.startswith('--tail-') or v.startswith('--exact-tail-') for v in forward):
        raise ValueError('This independent adapter continues the original model, with no tail migration')
    required = ('--repo', '--work', '--bundle', '--carrier', '--outdir',
                '--directions', '--qp-atol')
    supplied = {flag: value(forward, flag) for flag in required}
    if '--manifest' not in forward:
        raise ValueError('Supply the full permanent-position --manifest, repeatable without rewriting')
    directions, atol = int(supplied['--directions']), float(supplied['--qp-atol'])
    if directions < 1 or not math.isfinite(atol) or atol < 0:
        raise ValueError('Need a positive direction count and a finite nonnegative QP atol; zero is allowed')
    report_path = args.coarse_report.resolve()
    raw_report = report_path.read_bytes()
    report_sha = hashlib.sha256(raw_report).hexdigest()
    report = json.loads(raw_report)
    if report.get('schema') != COARSE_SCHEMA:
        raise ValueError('Need the returned original coarse-v7 report with actual terminal mu')
    mu = report.get('final_damping')
    if (isinstance(mu, bool) or not isinstance(mu, (int, float))
            or not math.isfinite(mu) or mu <= 0):
        raise ValueError('The returned final_damping must be finite and positive')
    bundle = Path(supplied['--bundle']).resolve()
    actual_bundle_sha = sha(bundle)
    if report.get('output_bundle_sha256') != actual_bundle_sha:
        raise ValueError('The actual bundle SHA disagrees with report.output_bundle_sha256')
    repo, work = Path(supplied['--repo']).resolve(), Path(supplied['--work']).resolve()
    output = Path(supplied['--outdir']).resolve()
    launcher = (args.launcher or repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261120/launch_full_phi_qp_actions.py').resolve()
    invocation = [sys.executable, str(launcher), *forward, '--damping', repr(float(mu))]
    prepared = subprocess.run([*invocation, '--print-command'], text=True,
                              capture_output=True, check=True)
    command = shlex.split(prepared.stdout.strip())
    if (len(command) < 3 or value(command, '--damping') != repr(float(mu))
            or int(value(command, '--max-directions')) != directions
            or float(value(command, '--qp-atol')) != atol
            or Path(value(command, '--bundle')).resolve() != bundle):
        raise ValueError('The unchanged launcher must retain the bound parent, mu, direction count and atol')
    if (float(value(command, '--reach-safety-factor')) != .992
            or float(value(command, '--active-band')) != .025):
        raise ValueError('This continuation uses the declared original .992/.025 branch')
    if args.print_command:
        print(shlex.join(command))
        return
    if (os.environ.get('GITHUB_ACTIONS', '').lower() != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise SystemExit('Actual scientific execution belongs in this public repository Actions.')
    files = {Path(__file__).resolve(), launcher, Path(command[2]).resolve()}
    path_flags = {'--operator', '--implementation', '--helpers', '--bundle',
                  '--observations', '--witness-input', '--radius-witness-input'}
    for index, flag in enumerate(command[:-1]):
        if flag.startswith('--') and (flag.endswith('-source') or flag in path_flags):
            files.add(Path(command[index+1]).resolve())
    for path in files:
        if not path.is_file():
            raise FileNotFoundError(path)
    if output.exists():
        raise FileExistsError('Use a new actual output directory')
    plan_path = work/(output.name+'-original-from-coarse-command.json')
    if plan_path.exists():
        raise FileExistsError(plan_path)
    work.mkdir(parents=True, exist_ok=True)
    plan = dict(schema='public-actions-original-full-Phi-from-returned-coarse-v7-v1',
        github_run_id=os.environ.get('GITHUB_RUN_ID'), github_sha=os.environ.get('GITHUB_SHA'),
        coarse_report=str(report_path), coarse_report_sha256=report_sha,
        coarse_source_sha256=report.get('source_sha256'), coarse_schema=report['schema'],
        coarse_status=report.get('status'), actual_parent_bundle=str(bundle),
        actual_parent_bundle_sha256=actual_bundle_sha, output_bundle_sha256_matched=True,
        actual_final_damping=float(mu), requested_directions=directions, qp_atol=atol,
        qp_rtol=float(value(command, '--qp-rtol')),
        qp_stopping_rule='atol + rtol*initial_gradient_norm; atol=0 retains the relative criterion and finite inner budget',
        damping_origin='coarse_report.final_damping; no hardcoded or fallback mu',
        damping_scope='Same normalized-Phi units; this scalar does not equate coarse and full redundant step norms',
        initial_damping_only=True,
        later_damping_rule='Unchanged full driver: halve only after accepted full step with actual/predicted decrease > .75; multiply by four if no trial is accepted',
        margin=.992, active_band=.025, original_physical_model=True,
        permanent_manifests_forwarded_literally=True, fields_or_points_removed=False,
        continuous_acceptance_inherited=False, actual_first_direction_required=True,
        later_directions_continue_accepted_state_and_accumulated_permanent_memory=True,
        launcher_invocation=invocation, full_scientific_command=command,
        file_sha256={str(path): sha(path) for path in sorted(files)},
        report_input_parsing_only=True, field_code_imported_by_adapter=False,
        scope='Actual .992 full-field continuation from the returned coarse parent; old pair scalars are not substituted for any new direction')
    plan_path.write_text(json.dumps(plan, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(event='original_full_actual_coarse_mu_bound',
        plan=str(plan_path), plan_sha256=sha(plan_path), parent_sha256=actual_bundle_sha,
        damping=float(mu), directions=directions, qp_atol=atol)), flush=True)
    subprocess.run(invocation, cwd=repo, check=True)


if __name__ == '__main__':
    main()
