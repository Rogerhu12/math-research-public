#!/usr/bin/env python3
"""Prepare the complete R715 centred R711 normal-plane SO3 QP.

Pure argv preparation does not evaluate a field. All scientific execution
remains public Actions. The exact reference source, original point, complete
history and all numerical/geometry budgets stay explicitly bound.
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

DRIVER_SHA = "9db39cd1b4c2812f5fc1b8fc2619efc4cd30271ba6b43f06bfde65004f131699"
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
    p.add_argument('--material-envelope-binding', type=Path)
    p.add_argument('--material-envelope-parent-report', type=Path, action='append', default=[])
    p.add_argument('--independent-envelope-branch', action='store_true')
    p.add_argument('--pending-parallel-envelope-run', action='append', default=[])
    p.add_argument('--pending-parallel-envelope-source', action='append', default=[])
    p.add_argument('--material-envelope-seed-checkpoint', type=Path)
    p.add_argument('--material-envelope-seed-report', type=Path)
    p.add_argument('--envelope-near-active-rows', type=int, default=32)
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
    p.add_argument('--seed-boundary-total-length', default='1/16')
    p.add_argument('--seed-profile-delta', default='1/128')
    p.add_argument('--seed-radial-quadrature-order', type=int, default=8)
    p.add_argument('--seed-profile-quadrature-order', type=int, default=16)
    p.add_argument('--seed-mean-maxiter', type=int, default=128)
    p.add_argument('--seed-mean-tolerance', type=float, default=2.e-12)
    p.add_argument('--seed-mean-backtracks', type=int, default=24)
    p.add_argument('--seed-mean-armijo', type=float, default=1.e-4)
    p.add_argument('--seed-scalar-iterations', type=int, default=64)

    for i in (1, 2):
        for position in ('left', 'middle', 'right'):
            p.add_argument('--endpoint-bubble-'+str(i)+'-'+position, required=True)
    p.add_argument('--endpoint-root-tolerance', type=float, default=2.e-12)
    p.add_argument('--endpoint-root-iterations', type=int, default=24)
    p.add_argument('--endpoint-root-backtracks', type=int, default=18)
    p.add_argument('--endpoint-root-armijo', type=float, default=1.e-4)
    p.add_argument('--endpoint-control-radius', type=float, default=2.)
    p.add_argument('--normal-stages', type=int, default=32)
    p.add_argument('--gamma-left', default='1/16')
    p.add_argument('--gamma-middle', default='1/8')
    p.add_argument('--gamma-right', default='3/16')
    p.add_argument('--seed-so3-checkpoint', type=Path)
    p.add_argument('--seed-so3-report', type=Path)
    moment_choice = p.add_mutually_exclusive_group(required=True)
    moment_choice.add_argument('--moment-trace-report', type=Path)
    moment_choice.add_argument('--moment-input', type=Path)
    p.add_argument('--moment-trace-report-sha256')
    p.add_argument('--moment-failed-report', type=Path)
    p.add_argument('--moment-input-sha256')
    p.add_argument('--moment-definition-sha256')
    p.add_argument('--moment-input-binding', choices=('supported-smooth-triangle-reference',), default='supported-smooth-triangle-reference')
    p.add_argument('--install-torch', action='store_true')
    p.add_argument('--print-command', action='store_true')
    a = p.parse_args()
    if a.moment_trace_report is not None or a.moment_input is None:
        raise ValueError('The supported-smooth-triangle representation adopts the complete published parameter file through its new twelve-key binder')
    if a.seed_so3_checkpoint is not None or a.seed_so3_report is not None:
        raise ValueError('A prior 7f or different-reference field cannot be relabelled as this frozen supported-smooth-triangle seed; use the original full initial point or an actual same-source restart')
    boundary, profile_delta = Fraction(a.seed_boundary_total_length), Fraction(a.seed_profile_delta)
    if (str(boundary) != a.seed_boundary_total_length
            or str(profile_delta) != a.seed_profile_delta
            or not 0 < boundary < Fraction(7,8) or not 0 < profile_delta < Fraction(1,8)
            or min(a.seed_radial_quadrature_order, a.seed_profile_quadrature_order,
                   a.seed_mean_maxiter, a.seed_mean_backtracks, a.seed_scalar_iterations) < 1
            or not math.isfinite(a.seed_mean_tolerance) or a.seed_mean_tolerance <= 0
            or not math.isfinite(a.seed_mean_armijo) or not 0 < a.seed_mean_armijo < 1):
        raise ValueError('Use the complete exact supported seed and explicit positive working root/quadrature parameters')
    if a.moment_input_binding == 'supported-smooth-triangle-reference' and a.moment_trace_report is not None:
        raise ValueError('The explicit new-reference mode adopts the published literal parameter input; it does not relabel an old trace as current')
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
    gamma = [Fraction(getattr(a, 'gamma_'+position)) for position in ('left','middle','right')]
    if (not 0 < gamma[0] < gamma[1] < gamma[2] < 1
            or not any(Fraction(getattr(a,'endpoint_bubble_'+str(i)+'_left')) < gamma[0]
                < gamma[2] < Fraction(getattr(a,'endpoint_bubble_'+str(i)+'_right')) for i in (1,2))):
        raise ValueError('The complete independent gamma support must lie strictly inside an original bubble support')
    if (a.normal_stages < 1 or a.endpoint_root_iterations < 1 or a.endpoint_root_backtracks < 1
            or not 0 < a.endpoint_root_armijo < 1
            or any(not math.isfinite(v) or v <= 0 for v in (
                a.endpoint_root_tolerance, a.endpoint_control_radius))):
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
    if a.envelope_near_active_rows < 1:
        raise ValueError('The new whole-grid near-active candidate cap is positive and never caps separation memory')
    if a.material_envelope_binding is not None:
        a.material_envelope_binding = a.material_envelope_binding.resolve()
    a.material_envelope_parent_report = [path.resolve() for path in a.material_envelope_parent_report]
    if bool(a.material_envelope_seed_checkpoint) != bool(a.material_envelope_seed_report):
        raise ValueError('An explicit old complete final variable seed requires both actual files')
    if a.material_envelope_seed_checkpoint is not None:
        a.material_envelope_seed_checkpoint = a.material_envelope_seed_checkpoint.resolve()
        a.material_envelope_seed_report = a.material_envelope_seed_report.resolve()
        if (a.restart_checkpoint is not None or a.seed_so3_checkpoint is not None
                or a.material_envelope_seed_report not in a.material_envelope_parent_report):
            raise ValueError('The explicit final belongs to a fully transferred prior envelope and cannot be mixed with another seed/restart')
    if (a.independent_envelope_branch and (a.material_envelope_parent_report
            or a.restart_checkpoint is not None or a.restart_report is not None
            or a.material_envelope_seed_checkpoint is not None or a.material_envelope_seed_report is not None
            or a.seed_so3_checkpoint is not None or a.seed_so3_report is not None)):
        raise ValueError('Explicit independent mode starts from the original reference, without a prior final or restart')
    if (a.pending_parallel_envelope_run and not a.independent_envelope_branch
            or len(a.pending_parallel_envelope_run)!=len(set(a.pending_parallel_envelope_run))
            or any(len(v.split('/'))!=2 or any(not w.isdigit() or int(w)<1 or str(int(w))!=w
                for w in v.split('/')) for v in a.pending_parallel_envelope_run)):
        raise ValueError('Use canonical run/attempt declarations only for unread independent-branch obligations')
    pending_sources={}
    for value in a.pending_parallel_envelope_source:
        parts=value.split('=')
        if (len(parts)!=2 or parts[0] in pending_sources or len(parts[1])!=64
                or any(c not in '0123456789abcdef' for c in parts[1])):
            raise ValueError('Use one complete explicit driver digest per pending run')
        pending_sources[parts[0]]=parts[1]
    if set(pending_sources)!=set(a.pending_parallel_envelope_run):
        raise ValueError('Every pending peer requires its exact run-to-source declaration')
    a.manifest = [path.resolve() for path in a.manifest]
    return a


def main():
    args = parse_args()
    source = args.repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261126'
    driver = source/'fullclosed_fixed_fejer_restoration_continuation_so3_qp.py'
    command = [sys.executable, '-u', str(driver)]
    for name, value in vars(args).items():
        if name in ('install_torch', 'print_command') or value is None:
            continue
        flag = '--'+name.replace('_', '-')
        if isinstance(value, bool):
            if value: command.append(flag)
        elif isinstance(value, list):
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
        args.scalar_input, *args.manifest, *args.material_envelope_parent_report]
    if args.material_envelope_seed_checkpoint is not None:
        inputs.extend([args.material_envelope_seed_checkpoint,args.material_envelope_seed_report])
    if args.material_envelope_binding is not None:
        inputs.append(args.material_envelope_binding)
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
    record = dict(schema='public-actions-complete-fixed-fejer-restoration-continuation-SO3-command-v1',
        command=command, source_sha256=sha(__file__), driver_sha256=DRIVER_SHA,
        source_commit=subprocess.check_output(['git', '-C', str(args.repo), 'rev-parse', 'HEAD'], text=True).strip(),
        workflow_trigger_commit=os.environ.get('GITHUB_SHA'),
        github_run_id=os.environ.get('GITHUB_RUN_ID'), closed_source_records=records,
        actual_input_records=[dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size)
            for path in inputs], python_version=sys.version,
        optional_pinned_CPU_install_command=install,
        official_install_documentation='https://pytorch.org/get-started/previous-versions/',
        fixed_supported_unit_seed=True,
        seed_reference_source_sha256=records['seed_reference']['sha256'],
        seed_mean_source_sha256=records['seed_mean']['sha256'],
        exact_relative_boundary_total_length=args.seed_boundary_total_length,
        exact_profile_delta=args.seed_profile_delta,
        current_outer_point_not_used_to_rebuild_seed=True,
        seed_mean_inverse_not_a_normal_control_inverse_certificate=True,
        full_variables_and_original_positive_rows_preserved=True,
        detached_stage_matrix_reuse_declared=True,
        complete_same_chain_detached_closure_values_declared=True,
        closure_value_source_sha256=records['closure_values']['sha256'],
        detached_meridian_value_source_sha256=records['detached_meridian_values']['sha256'],
        complete_missing_angle_geometry_source_sha256=records['geometry']['sha256'],
        original_full_implicit_calls_query_jets_and_partial_integrals_retained=True,
        only_missing_literal_angle_roots_batched_under_original_angle_block=True,
        all_original_stage_final_and_endpoint_closure_integrals_retained=True,
        active_parameter_J_and_transpose_use_original_closure=True,
        mutable_scalar_progress_path=str(args.outdir/'actual-normal-evaluation-progress.json'),
        progress_observer_does_not_evaluate_scientific_values=True,
        selected_local_J3_and_all_stage_equations_retained=True,
        old_envelope_transferred_as_addresses_and_types_only=True,
        measured_cache_hit_rate_or_speedup_claimed=False,
        original_192_geometry_selection_preserved=True,
        full_true_permanent_geometry_and_amplitude_screens=True,
        unit_T_is_exact_final_Fs=False, numerical_unit_and_integral_errors_certified=False,
        accurate_unit_identity_requires_exact_reference_and_final_normal_roots=True,
        physical_sixjets_retain_complete_current_raw_closure_lift=True,
        reference_centering_helper_sha256=records['reference_calibration']['sha256'],
        nodewise_centred_root_difference_and_raw_physical_defect_are_separate=True,
        endpoint_root_implicit_derivative_separate_from_iterations=True,
        implicit_control_dimension=6,normal_increment_dimension=3,implicit_dimension_per_stage=9,
        normal_stage_count=args.normal_stages,
        exact_normal_step_nodes=[str(Fraction(i,args.normal_stages)) for i in range(args.normal_stages+1)],
        complete_first_angular_implicit_dimension=6*args.normal_stages,
        complete_second_angular_implicit_dimension=9*args.normal_stages,
        common_partition_for_all_angles_and_free_points=True,per_angle_adaptive_normal_partition=False,
        stationary_KKT_selection_used=False,continuous_horizontal_ODE_solution_claimed=False,
        previous_normal_frame_and_zero_target_full_chain_retained=True,
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
