#!/usr/bin/env python3
"""Execute complete normalized-parent cached interior restoration and all-row SOC.

--print-command is pure stdlib argv preparation, never a field fixture.
--install-torch executes the official pinned CPU pip command only in public
Actions. The complete actual parent and all history are bound by the driver.
"""
import argparse
import ast
import hashlib
import json
import math
import os
from pathlib import Path
import shlex
import subprocess
import sys

DRIVER_SHA = '892f349b140f9a77fde37fc490d7cbb078cfdb21f8b31b7743e50ec6cf5712a8'
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
    for name in ('repo', 'parent-bundle', 'parent-report', 'carrier', 'node-report', 'scalar-input', 'outdir'):
        p.add_argument('--'+name, type=Path, required=True)
    p.add_argument('--manifest', type=Path, action='append', required=True)
    p.add_argument('--restart-checkpoint', type=Path)
    p.add_argument('--restart-report', type=Path)
    p.add_argument('--reference-cache', type=Path)
    p.add_argument('--reference-cache-report', type=Path)
    p.add_argument('--eta-start-node', type=int, required=True)
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
    p.add_argument('--restoration-interior-margin', type=float, default=1.e-8)
    p.add_argument('--line-trials', type=int, default=15)
    p.add_argument('--soc-rounds', type=int, default=8)
    p.add_argument('--soc-tau', type=float, default=0.)
    p.add_argument('--soc-inward-fraction', type=float, default=.125)
    p.add_argument('--soc-feasibility-tolerance', type=float, default=2.e-11)
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
    p.add_argument('--scalar-admission-seconds', type=float, default=300.)
    p.add_argument('--scalar-integral-tolerance', default='1e-18')
    p.add_argument('--scalar-tail-cutoff', default='1/8')
    p.add_argument('--install-torch', action='store_true')
    p.add_argument('--print-command', action='store_true')
    a = p.parse_args()
    if (not 1 <= a.soc_rounds <= 8 or any(not math.isfinite(v) or v < 0
            for v in (a.soc_tau, a.soc_inward_fraction, a.soc_feasibility_tolerance))):
        raise ValueError('Declare one-to-eight complete SOC rounds and finite nonnegative inward/readback parameters')
    if bool(a.reference_cache) != bool(a.reference_cache_report):
        raise ValueError('An explicit retained cache needs its actual completed producer report')
    if bool(a.restart_checkpoint) != bool(a.restart_report):
        raise ValueError('A true SO3 restart needs both its own complete checkpoint and report')
    if (min(a.directions, a.maxiter, a.line_trials, a.stage_block, a.angle_block,
            a.restoration_maxiter, a.active_rows, a.active_block_columns) < 1
            or a.restoration_directions < 0 or a.active_rows != 192
            or not 1 <= a.torch_threads <= 4 or a.angles%4 or a.angles < 2048
            or not 0 < a.legacy_fraction < 1 or a.spectral_p < 2 or a.spectral_p%2
            or not 0 < a.reach_safety_factor < 1
            or not 0 < a.active_band < a.reach_safety_factor
            or any(not math.isfinite(v) or v <= 0 for v in (
                a.damping, a.restoration_damping, a.target, a.spectral_epsilon,
                a.spectral_scale, a.radial_norm_length, a.angular_transition,
                a.inverse_root_tolerance, a.qp_rtol, a.reach_ratio,
                a.restoration_interior_margin))):
        raise ValueError('Use explicit valid full-space/fixed-target numerical parameters')
    for name in ('repo', 'parent_bundle', 'parent_report', 'carrier', 'node_report',
                 'scalar_input', 'outdir', 'restart_checkpoint', 'restart_report',
                 'reference_cache', 'reference_cache_report'):
        if getattr(a, name) is not None:
            setattr(a, name, getattr(a, name).resolve())
    a.manifest = [path.resolve() for path in a.manifest]
    if a.reference_cache_report is not None and a.reference_cache_report not in a.manifest:
        # Every supplied actual cache donor also contributes all its permanent locations.
        a.manifest.append(a.reference_cache_report)
    return a


def main():
    args = parse_args()
    source = args.repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261126'
    driver = source/'fullclosed_so3_cached_interior_separation_soc.py'
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
    inputs = [args.parent_bundle, args.parent_report, args.carrier, args.node_report,
        args.scalar_input, *args.manifest]
    if args.restart_checkpoint is not None:
        inputs.extend([args.restart_checkpoint, args.restart_report])
    if args.reference_cache is not None and not args.reference_cache.is_dir():
        raise FileNotFoundError(args.reference_cache)
    for path in inputs:
        if not path.is_file():
            raise FileNotFoundError(path)
    plan = args.outdir.with_name(args.outdir.name+'-command.json')
    if args.outdir.exists() or plan.exists():
        raise FileExistsError('Use a new actual solve and command path')
    plan.parent.mkdir(parents=True, exist_ok=True)
    install = [sys.executable, *TORCH_INSTALL] if args.install_torch else None
    record = dict(schema='public-actions-complete-normalized-parent-cached-interior-separated-SOC-command-v1',
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
        unit_T_is_final_Fs_claimed=False,
        phase_I_common_slack_is_physical_feasibility_claimed=False,
        restoration_interior_margin=args.restoration_interior_margin,
        interior_margin_changes_original_nonlinear_acceptance=False,
        reference_cache_directory=None if args.reference_cache is None else str(args.reference_cache),
        reference_cache_report=None if args.reference_cache_report is None else str(args.reference_cache_report),
        cache_full_identity_and_bytes_verified_by_actual_driver=True,
        cache_checksums_claimed_to_exist_in_legacy_report=False,
        original_234ac_and_d3f25_methods_unchanged=True,
        no_scientific_fixture_or_probe=True, old_field_certificates_inherited=False)
    plan.write_text(json.dumps(record, indent=2, allow_nan=False)+'\n')
    if install is not None:
        subprocess.run(install, check=True)
    env = os.environ.copy()
    env.update(PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='1',
        OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')
    actual = subprocess.run(command, env=env, cwd=args.repo, check=False)
    if actual.returncode:
        raise SystemExit(actual.returncode)


if __name__ == '__main__':
    main()
