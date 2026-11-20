#!/usr/bin/env python3
"""Read a returned coarse-v7 mu and launch the existing R671 Actions entry.

Adapter flags: --coarse-report PATH [--launcher PATH] [--print-command].
All other flags pass literally to launch_full_phi_exact_tail_actions.py.
Explicit --repo/--work/--bundle/--carrier/--manifest/--outdir and the tail
model/input flags are required. A caller-supplied --damping is rejected:
the actual returned final_damping and matching bundle SHA are mandatory.

Preparation reads JSON and hashes bytes only; no field module is imported.
An actual child requires public Actions and writes a separate provenance plan.
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
        raise ValueError('Damping must come from the returned report, never a copied constant')
    required = ('--repo', '--work', '--bundle', '--carrier', '--outdir',
        '--node-report', '--scalar-input', '--eta-start-node', '--lambda-value', '--migration')
    supplied = {flag: value(forward, flag) for flag in required}
    if '--manifest' not in forward:
        raise ValueError('Supply at least one explicit permanent-position --manifest')
    report_path = args.coarse_report.resolve()
    raw_report = report_path.read_bytes()
    report_sha = hashlib.sha256(raw_report).hexdigest()
    report = json.loads(raw_report)
    if report.get('schema') != COARSE_SCHEMA:
        raise ValueError('Need the returned coarse-v7 report with its actual terminal mu')
    mu = report.get('final_damping')
    if (isinstance(mu, bool) or not isinstance(mu, (int, float))
            or not math.isfinite(mu) or mu <= 0):
        raise ValueError('The returned final_damping must be finite and positive')
    bundle = Path(supplied['--bundle']).resolve()
    actual_bundle_sha = sha(bundle)
    if report.get('output_bundle_sha256') != actual_bundle_sha:
        raise ValueError('The actual bundle SHA disagrees with report.output_bundle_sha256')
    repo = Path(supplied['--repo']).resolve()
    work = Path(supplied['--work']).resolve()
    output = Path(supplied['--outdir']).resolve()
    launcher = (args.launcher or repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261120/launch_full_phi_exact_tail_actions.py').resolve()
    invocation = [sys.executable, str(launcher), *forward, '--damping', repr(float(mu))]
    prepared = subprocess.run([*invocation, '--print-command'], text=True,
        capture_output=True, check=True)
    command = shlex.split(prepared.stdout.strip())
    if len(command) < 3 or value(command, '--damping') != repr(float(mu)):
        raise ValueError('Prepared full-QP command did not retain the actual returned damping')
    if Path(value(command, '--bundle')).resolve() != bundle:
        raise ValueError('Prepared full-QP command changed the verified parent bundle')
    if args.print_command:
        print(shlex.join(command))
        return
    if os.environ.get('GITHUB_ACTIONS') != 'true':
        raise SystemExit('Actual scientific child requires public GitHub Actions; --print-command is preparation only.')
    original_launcher = (Path(value(forward,'--source-launcher')).resolve()
        if '--source-launcher' in forward else
        repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261120/launch_full_phi_qp_actions.py')
    files = {Path(__file__).resolve(), launcher, original_launcher, Path(command[2]).resolve()}
    path_flags = {'--operator', '--implementation', '--helpers', '--bundle',
        '--observations', '--witness-input', '--radius-witness-input',
        '--tail-node-report', '--tail-scalar-input'}
    for index, flag in enumerate(command[:-1]):
        if flag.startswith('--') and (flag.endswith('-source') or flag in path_flags):
            files.add(Path(command[index+1]).resolve())
    for path in files:
        if not path.is_file():
            raise FileNotFoundError(path)
    if output.exists():
        raise FileExistsError('Use a new actual output directory')
    plan_path = work/(output.name+'-from-coarse-command.json')
    if plan_path.exists():
        raise FileExistsError(plan_path)
    work.mkdir(parents=True, exist_ok=True)
    plan = dict(schema='public-actions-R671-damping-from-returned-coarse-v7-v1',
        github_run_id=os.environ.get('GITHUB_RUN_ID'), github_sha=os.environ.get('GITHUB_SHA'),
        coarse_report=str(report_path), coarse_report_sha256=report_sha,
        coarse_schema=report['schema'], coarse_status=report.get('status'),
        actual_parent_bundle=str(bundle), actual_parent_bundle_sha256=actual_bundle_sha,
        output_bundle_sha256_matched=True, actual_final_damping=float(mu),
        damping_origin='coarse_report.final_damping; no hardcoded or fallback mu',
        damping_scope='Same normalized-Phi units; reusing this scalar does not equate the coarse and full redundant step norms',
        coarse_known_point_flag_recorded_only=report.get('final_known_point_safety_pass'),
        inherited_field_acceptance=False, inherited_continuous_certificate=False,
        launcher_invocation=invocation, full_scientific_command=command,
        file_sha256={str(path): sha(path) for path in sorted(files)},
        report_input_parsing_only=True, field_code_imported_by_adapter=False,
        scope='Actual byte-bound parent and mu; new tail migration and all true acceptance checks remain in the unchanged R671 driver')
    plan_path.write_text(json.dumps(plan, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(event='R671_actual_coarse_mu_bound',
        plan=str(plan_path), plan_sha256=sha(plan_path),
        parent_sha256=actual_bundle_sha, damping=float(mu))), flush=True)
    subprocess.run(invocation, cwd=repo, check=True)


if __name__ == '__main__':
    main()
