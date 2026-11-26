#!/usr/bin/env python3
"""Prepare or execute the complete independent zero-closure SO3 QP, with explicit CPU runtime.

--print-command is pure stdlib argv preparation, never a field fixture.
--install-torch executes the official pinned CPU pip command only in public
Actions. The complete actual independent reference and all supplied history are bound by the driver.
"""
import argparse
from fractions import Fraction
import ast
import hashlib
import json
import math
import os
from pathlib import Path
import shlex
import subprocess
import sys

DRIVER_SHA = '9649ed99b614c468258646145948d7c06feb356c72806c73727728ea498ed88e'
TORCH_INSTALL = ['-m', 'pip', 'install', '--disable-pip-version-check', '--no-input',
    'torch==2.5.1', '--index-url', 'https://download.pytorch.org/whl/cpu']


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def parse_args():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'reference-bundle', 'preparation-report', 'carrier', 'node-report', 'scalar-input', 'outdir'):
        p.add_argument('--'+name, type=Path, required=True)
    p.add_argument('--manifest', type=Path, action='append', required=True)
    p.add_argument('--restart-checkpoint', type=Path)
    p.add_argument('--restart-report', type=Path)
    p.add_argument('--angles', type=int, default=2048)
    p.add_argument('--stage-block', type=int, default=64)
    p.add_argument('--angle-block', type=int, default=8)
    p.add_argument('--integration-order', type=int, default=8)
    p.add_argument('--inverse-root-iterations', type=int, default=18)
    p.add_argument('--inverse-root-tolerance', type=float, default=2.e-12)
    p.add_argument('--norm-kind', choices=('jet-sum', 'integral'), default='jet-sum')
    p.add_argument('--radial-norm-length', type=float, default=.05)
    p.add_argument('--angular-transition', type=float, default=24.)
    p.add_argument('--torch-threads', type=int, default=4)
    p.add_argument('--damping', type=float, required=True)
    p.add_argument('--directions', type=int, default=2)
    p.add_argument('--maxiter', type=int, default=64)
    p.add_argument('--restoration-directions', type=int, default=4)
    p.add_argument('--restoration-damping', type=float, default=.01)
    p.add_argument('--restoration-maxiter', type=int, default=64)
    p.add_argument('--line-trials', type=int, default=15)
    p.add_argument('--qp-atol', type=float, default=0.)
    p.add_argument('--qp-rtol', type=float, default=1.e-6)
    p.add_argument('--qp-feasibility-tolerance', type=float, default=2.e-11)
    p.add_argument('--qp-rank-tolerance', type=float, default=2.e-12)
    p.add_argument('--active-rows', type=int, default=192)
    p.add_argument('--active-block-columns', type=int, default=32768)
    p.add_argument('--active-band', type=float, default=.025)
    p.add_argument('--reach-ratio', type=float, default=.03)
    p.add_argument('--reach-safety-factor', type=float, default=.992)
    p.add_argument('--marked-diameter-budget', type=float, default=4.2)
    p.add_argument('--witness-lower-budget', type=float, default=.9)
    p.add_argument('--amplitude-height-floor', type=float, default=1.01)
    p.add_argument('--amplitude-top-radius', type=int, default=2)
    p.add_argument('--amplitude-top-distance', type=int, default=4)
    p.add_argument('--spectral-p', type=int, default=4)
    p.add_argument('--spectral-epsilon', type=float, default=.001)
    p.add_argument('--spectral-scale', type=float, default=.05)
    p.add_argument('--legacy-fraction', type=float, default=.5)
    p.add_argument('--target', type=float, required=True)
    p.add_argument('--panels', type=int, default=128)

    for i in (1, 2):
        for position in ('left', 'middle', 'right'):
            p.add_argument('--endpoint-bubble-'+str(i)+'-'+position, required=True)
    p.add_argument('--endpoint-root-tolerance', type=float, default=2.e-12)
    p.add_argument('--endpoint-root-iterations', type=int, default=24)
    p.add_argument('--endpoint-root-backtracks', type=int, default=18)
    p.add_argument('--endpoint-root-armijo', type=float, default=1.e-4)
    p.add_argument('--endpoint-root-branch-radius', type=float, default=.5)
    p.add_argument('--endpoint-continuation-initial-step', type=float, default=.25)
    p.add_argument('--endpoint-continuation-minimum-step', type=float, default=1./65536)
    p.add_argument('--endpoint-continuation-growth', type=float, default=1.5)
    p.add_argument('--endpoint-continuation-shrink', type=float, default=.5)
    p.add_argument('--endpoint-continuation-stage-attempts', type=int, default=64)
    p.add_argument('--endpoint-continuation-predictor', type=int, choices=(0,1), default=1)
    p.add_argument('--seed-so3-checkpoint', type=Path)
    p.add_argument('--seed-so3-report', type=Path)
    moment_choice = p.add_mutually_exclusive_group(required=True)
    moment_choice.add_argument('--moment-trace-report', type=Path)
    moment_choice.add_argument('--moment-input', type=Path)
    p.add_argument('--moment-trace-report-sha256')
    p.add_argument('--moment-failed-report', type=Path)
    p.add_argument('--moment-input-sha256')
    p.add_argument('--moment-definition-sha256')
    p.add_argument('--install-torch', action='store_true')
    p.add_argument('--print-command', action='store_true')
    a = p.parse_args()
    if a.moment_trace_report is not None:
        if a.moment_failed_report is None or a.moment_trace_report_sha256 is None or a.moment_input_sha256 is not None:
            raise ValueError('The actual-trace route needs its complete recorded failure and trace SHA; no small-file SHA is mixed in')
    elif (a.moment_input_sha256 is None or a.moment_definition_sha256 is None
            or a.moment_trace_report_sha256 is not None or a.moment_failed_report is not None):
        raise ValueError('The small fixed-parameter route needs its file SHA and the SAME complete definition identity')
    for digest in (a.moment_trace_report_sha256, a.moment_input_sha256, a.moment_definition_sha256):
        if digest is not None and (len(digest) != 64 or any(c not in '0123456789abcdef' for c in digest)):
            raise ValueError('Use complete explicit SHA256 input identities')
    if bool(a.restart_checkpoint) != bool(a.restart_report):
        raise ValueError('A true SO3 restart needs both its own complete checkpoint and report')

    if bool(a.seed_so3_checkpoint) != bool(a.seed_so3_report):
        raise ValueError('A zero-closure seed needs the actual complete base checkpoint and report')
    if a.restart_checkpoint is not None and a.seed_so3_checkpoint is not None:
        raise ValueError('Choose a true zero-closure continuation or a new-field base seed, not both')
    for i in (1, 2):
        row = [Fraction(getattr(a, 'endpoint_bubble_'+str(i)+'_'+position))
            for position in ('left', 'middle', 'right')]
        if not 0 < row[0] < row[1] < row[2] < 1:
            raise ValueError('Declare complete strictly interior exact quintic bubble triples')
    if Fraction(a.endpoint_bubble_1_right) >= Fraction(a.endpoint_bubble_2_left):
        raise ValueError('The two complete bubble supports must be disjoint')
    if (a.endpoint_root_iterations < 1 or a.endpoint_root_backtracks < 1
            or not 0 < a.endpoint_root_armijo < 1
            or any(not math.isfinite(v) or v <= 0 for v in (
                a.endpoint_root_tolerance, a.endpoint_root_branch_radius))):
        raise ValueError('Use explicit finite positive numerical endpoint-root parameters')
    if (min(a.directions, a.maxiter, a.line_trials, a.stage_block, a.angle_block,
            a.restoration_maxiter, a.active_rows, a.active_block_columns) < 1
            or a.restoration_directions < 0 or a.active_rows != 192
            or not 1 <= a.torch_threads <= 4 or a.angles != 2048 or a.panels < 1
            or not 0 < a.legacy_fraction < 1 or a.spectral_p < 2 or a.spectral_p%2
            or not 0 < a.reach_safety_factor < 1
            or not 0 < a.active_band < a.reach_safety_factor
            or any(not math.isfinite(v) or v <= 0 for v in (
                a.damping, a.restoration_damping, a.target, a.spectral_epsilon,
                a.spectral_scale, a.radial_norm_length, a.angular_transition,
                a.inverse_root_tolerance, a.qp_rtol, a.reach_ratio))):
        raise ValueError('Use explicit valid full-space/fixed-target numerical parameters')
    for name in ('repo', 'reference_bundle', 'preparation_report', 'carrier', 'node_report',
                 'scalar_input', 'outdir', 'restart_checkpoint', 'restart_report',
                 'seed_so3_checkpoint', 'seed_so3_report', 'moment_trace_report',
                 'moment_failed_report', 'moment_input'):
        if getattr(a, name) is not None:
            setattr(a, name, getattr(a, name).resolve())
    a.manifest = [path.resolve() for path in a.manifest]
    return a


def main():
    args = parse_args()
    source = args.repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261126'
    driver = source/'fullclosed_zero_moment_continuation_so3_qp.py'
    command = [sys.executable, '-u', str(driver)]
    for name, value in vars(args).items():
        if name in ('install_torch', 'print_command') or value is None:
            continue
        flag = '--'+name.replace('_', '-')
        if isinstance(value, list):
            for item in value:
                command.extend([flag, str(item)])
        else:
            command.extend([flag, str(value)])
    if args.print_command:
        print(shlex.join(command))
        return
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise SystemExit('The full scientific entry and pinned CPU install require public repository Actions')
    if args.outdir == args.repo or args.repo in args.outdir.parents:
        raise ValueError('Scientific raw outputs stay outside the repository')
    if sha(driver) != DRIVER_SHA:
        raise ValueError('The actual complete SO3 driver differs from the frozen source')
    tree = ast.parse(driver.read_text())
    pins = [ast.literal_eval(n.value) for n in tree.body if isinstance(n, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == 'SOURCE_PINS' for t in n.targets)]
    if len(pins) != 1:
        raise ValueError('The complete driver source must have one literal closed source registry')
    topic = args.repo/'topics/visible-flex-larger-amplitude'
    records = {}
    for role, (relative, expected) in pins[0].items():
        path = topic/relative
        if sha(path) != expected:
            raise ValueError('Changed complete scientific dependency '+role)
        records[role] = dict(repo_relative_path=str(path.relative_to(args.repo)),
            sha256=expected, bytes=path.stat().st_size)
    inputs = [args.reference_bundle, args.preparation_report, args.carrier, args.node_report,
        args.scalar_input, *args.manifest]
    if args.restart_checkpoint is not None:
        inputs.extend([args.restart_checkpoint, args.restart_report])
    if args.seed_so3_checkpoint is not None:
        inputs.extend([args.seed_so3_checkpoint, args.seed_so3_report])
    if args.moment_trace_report is not None:
        inputs.extend([args.moment_trace_report, args.moment_failed_report])
    else:
        inputs.append(args.moment_input)
    for path in inputs:
        if not path.is_file():
            raise FileNotFoundError(path)
    plan = args.outdir.with_name(args.outdir.name+'-command.json')
    if args.outdir.exists() or plan.exists():
        raise FileExistsError('Use a new actual solve and command path')
    plan.parent.mkdir(parents=True, exist_ok=True)
    install = [sys.executable, *TORCH_INSTALL] if args.install_torch else None
    record = dict(schema='public-actions-complete-frozen-Q-endpoint-continuation-SO3-command-v1',
        command=command, source_sha256=sha(__file__), driver_sha256=DRIVER_SHA,
        source_commit=subprocess.check_output(['git', '-C', str(args.repo), 'rev-parse', 'HEAD'], text=True).strip(),
        workflow_trigger_commit=os.environ.get('GITHUB_SHA'),
        github_run_id=os.environ.get('GITHUB_RUN_ID'), closed_source_records=records,
        actual_input_records=[dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size)
            for path in inputs], python_version=sys.version,
        optional_pinned_CPU_install_command=install,
        official_install_documentation='https://pytorch.org/get-started/previous-versions/',
        full_variables_and_original_positive_rows_preserved=True,
        original_192_geometry_selection_preserved=True,
        full_true_permanent_geometry_and_amplitude_screens=True,
        unit_T_is_exact_final_Fs=True, numerical_unit_and_integral_errors_certified=False,
        endpoint_root_implicit_derivative_separate_from_iterations=True,
        complete_uniform_IFT_conditions_verified=False,
        phase_I_common_slack_is_physical_feasibility_claimed=False,
        no_scientific_fixture_or_probe=True, old_field_certificates_inherited=False)
    plan.write_text(json.dumps(record, indent=2, allow_nan=False)+'\n')
    if install is not None:
        subprocess.run(install, check=True)
    env = os.environ.copy()
    env.update(PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='1',
        OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')
    subprocess.run(command, env=env, cwd=args.repo, check=True)


if __name__ == '__main__':
    main()
