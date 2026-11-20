#!/usr/bin/env python3
"""Continue the identical nonzero R671 model from an actual full-QP report.

Reuses the R676 stdlib terminal-mu and complete-history location helpers.
The same canonical lambda, physical eta, scalar, mesh, observations,
objective, step norm and .992/.025 margin are retained. keep-q is mandatory;
this is not another migration or a new nodal projection. A new
driver is derived by the already published manifest-only AST transform;
the original driver bytes remain untouched. --qp-source explicitly selects
a solver module; the default retains the actual parent's module bytes.
Default batch: one direction.

--print-command prepares source/JSON provenance and argv without reading
scientific arrays. Actual stage resolution and solving require public Actions.
"""
import argparse
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import shlex
import subprocess
import sys
import time


HISTORY_SHA = '4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60'
DERIVATION_SHA = '100e57c66e1f5b592fe22570c6c7894a6ab75e082b714edfff42514098d5c622'
DRIVER_SHA = 'b1b0725acffde7958d9a4ad245057ea243d4319bde15bd9a7778ade3b0f844e8'
LAUNCHER_SHA = 'c9ba1d73db3e3608dffa1dbc9aeeda2a355d2ff4c2b9fc8eed2140c985869ec7'
ORIGINAL_LAUNCHER_SHA = '6f021d459c24d5cb5a07853628d6a6a297332d51ad561beab2d09e50e2b34d63'
FACTORY_SHA = '2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216'
POSITION_SCHEMA = 'immutable-curvature-history-locations-v1'


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def source_sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                    allow_nan=False).encode()).hexdigest()


def argument(command, flag):
    if command.count(flag) != 1:
        raise ValueError('Expected one explicit scientific argument '+flag)
    return command[command.index(flag)+1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('repo', 'work', 'parent-report', 'bundle', 'carrier',
                'node-report', 'scalar-input', 'outdir'):
        parser.add_argument('--'+key, type=Path, required=True)
    parser.add_argument('--manifest', type=Path, action='append', required=True)
    for key in ('parent-source', 'history-source', 'derivation-source', 'source-launcher', 'qp-source'):
        parser.add_argument('--'+key, type=Path)
    parser.add_argument('--directions', type=int, default=1)
    parser.add_argument('--maxiter', type=int, default=256)
    parser.add_argument('--active-rows', type=int)
    parser.add_argument('--stage-block', type=int, default=64)
    parser.add_argument('--qp-atol', type=float, default=0.)
    parser.add_argument('--qp-rtol', type=float)
    parser.add_argument('--print-command', action='store_true')
    args = parser.parse_args()
    if (args.directions < 1 or args.maxiter < 1 or args.stage_block < 1
            or not math.isfinite(args.qp_atol) or args.qp_atol < 0):
        raise ValueError('Need positive counts and a finite nonnegative absolute QP tolerance')
    for key in ('repo', 'work', 'parent_report', 'bundle', 'carrier',
                'node_report', 'scalar_input', 'outdir'):
        setattr(args, key, getattr(args, key).resolve())
    args.manifest = [path.resolve() for path in args.manifest]
    source_dir = args.repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261120'
    history_path = (args.history_source or source_dir/'launch_refinement_from_full_report.py').resolve()
    if source_sha(history_path) != HISTORY_SHA:
        raise ValueError('Use the stated complete-history and terminal-mu helper')
    history = load('completed_full_phi_history', history_path)
    derivation_path = (args.derivation_source or source_dir/'launch_fixed_g_refinement_qp.py').resolve()
    if history.sha(derivation_path) != DERIVATION_SHA:
        raise ValueError('Use the stated manifest-only AST derivation')
    derivation = load('completed_full_phi_manifest_derivation', derivation_path)
    launcher = (args.source_launcher or source_dir/'launch_full_phi_exact_tail_actions.py').resolve()
    original_launcher = source_dir/'launch_full_phi_qp_actions.py'
    factory = source_dir/'exact_reference_tail_lift.py'
    frozen_driver = source_dir/'fullclosed_gauss_exact_tail_inequality_qp.py'
    if (history.sha(launcher) != LAUNCHER_SHA or history.sha(frozen_driver) != DRIVER_SHA
            or history.sha(original_launcher) != ORIGINAL_LAUNCHER_SHA
            or history.sha(factory) != FACTORY_SHA):
        raise ValueError('The complete R671 driver/factory and both original launchers remain frozen')
    report = json.loads(args.parent_report.read_text())
    parent_source = history.bound_parent_source(report, source_dir, args.parent_source)
    damping = history.terminal_damping(report)
    original_base = parent_source.get('declared_derivation', {}).get('frozen_driver_sha256',
                                                                     parent_source['sha256'])
    if original_base != DRIVER_SHA:
        raise ValueError('This continuation needs an actual completed R671 parent, not an original-lift field')
    if report.get('final_bundle_sha256') != history.sha(args.bundle):
        raise ValueError('The parent report final_bundle_sha256 does not match the actual bundle')
    if report.get('observation_carrier_sha256') != history.sha(args.carrier):
        raise ValueError('Keep this parent model exact observation carrier')
    context = report.get('exact_tail_context_final')
    if not isinstance(context, dict) or not isinstance(context.get('definition'), dict):
        raise ValueError('The completed R671 parent must retain its actual canonical model definition')
    model = context['definition']
    model_sha = canonical_sha(model)
    fixed_lambda = model.get('lambda_value')
    eta_start, eta_end = model.get('eta_start_node'), model.get('eta_end_node')
    if (model.get('schema') != 'R671-exact-reference-tail-lift-v1'
            or model.get('source_sha256') != FACTORY_SHA
            or context.get('model_identity_sha256') != model_sha
            or report.get('exact_tail_context', {}).get('definition') != model
            or isinstance(fixed_lambda, bool) or not isinstance(fixed_lambda, (int, float))
            or not math.isfinite(fixed_lambda) or not 0 < fixed_lambda <= 1
            or report.get('exact_tail_lambda') != fixed_lambda
            or not isinstance(eta_start, int) or not isinstance(eta_end, int)
            or not 0 < eta_start < eta_end < report['J']-1
            or report.get('exact_tail_eta_start_node') != eta_start):
        raise ValueError('Keep the same nonzero canonical lambda and exact physical eta definition')
    if (model.get('original_observation_carrier_sha256') != history.sha(args.carrier)
            or model.get('node_report_sha256') != history.sha(args.node_report)
            or model.get('scalar_input_sha256') != history.sha(args.scalar_input)
            or report.get('exact_tail_node_report_sha256') != history.sha(args.node_report)
            or report.get('exact_tail_scalar_input_sha256') != history.sha(args.scalar_input)):
        raise ValueError('The same canonical node/scalar/carrier identities are required')
    if (report.get('objective') != 'spectral'
            or report.get('numerical_reach_safety_factor') != .992
            or report.get('requested_reach_ratio') != .03
            or report.get('active_band') != .025
            or report.get('radial_weights', {}).get('legacy_fraction') != .5
            or report.get('angular_norm', {}).get('nu_c') != 24):
        raise ValueError('Continue the declared R671 p8/radial-mixture/nu_c24/.992/.025 model')
    parent_spectral = report.get('current', report.get('initial', {})).get('spectral', {})
    if any(parent_spectral.get(key) != expected for key, expected in
           dict(p=8, epsilon=.001, scale=.05).items()):
        raise ValueError('Retain the actual fixed p8/epsilon/scale objective')
    shape = history.budget(report)
    points = history.Locations(shape['parent_J'], shape['parent_radial_observations'],
                               shape['parent_full_angles'])
    points.walk(report)
    caller_records, direct_manifests = [], []
    carrier_sha = history.sha(args.carrier)
    for index, path in enumerate(args.manifest):
        payload = json.loads(path.read_text())
        declared = payload.get('carrier_sha256', payload.get('observation_carrier_sha256'))
        if declared is not None and declared != carrier_sha:
            raise ValueError('A caller manifest declares another observation carrier')
        points.walk(payload, path=('caller_manifest', index))
        pure = payload.get('schema') == POSITION_SCHEMA
        if pure:
            direct_manifests.append(path)
        caller_records.append(dict(**history.file_record(path), passed_unchanged=pure,
            all_recognized_locations_also_in_union=True,
            noncanonical_format_rule=None if pure else 'All positions are retained through the same complete-history extractor and the canonical union, without changing their binary values'))
    initial_points = points.summary()
    active_rows = report['active_max_rows'] if args.active_rows is None else args.active_rows
    rtol = report['qp_rtol'] if args.qp_rtol is None else args.qp_rtol
    if active_rows < 1 or not math.isfinite(rtol) or rtol < 0:
        raise ValueError('Need a positive working-row cap and a finite nonnegative relative tolerance')
    if args.outdir.exists():
        raise FileExistsError('Use a fresh output directory for this actual continuation')
    inputs_dir = args.work/(args.outdir.name+'-continuation-inputs')
    inputs_dir.mkdir(parents=True, exist_ok=True)
    derived = derivation.derive_driver(frozen_driver, inputs_dir/'derived-R671-full-phi-exact-positions.py')
    supplement = inputs_dir/'complete-parent-and-caller-locations.json'
    plan_path = inputs_dir/'continuation-plan.json'
    centers = report.get('requested_coarse_centers')
    invocation = [sys.executable, str(launcher), '--repo', str(args.repo), '--work', str(args.work),
        '--bundle', str(args.bundle), '--carrier', str(args.carrier), '--outdir', str(args.outdir),
        '--source-launcher', str(original_launcher), '--exact-tail-source', str(factory),
        '--node-report', str(args.node_report), '--scalar-input', str(args.scalar_input),
        '--eta-start-node', str(eta_start), '--lambda-value', repr(float(fixed_lambda)),
        '--source-lambda', repr(float(fixed_lambda)), '--migration', 'keep-q',
        '--damping', repr(damping['terminal_damping']), '--maxiter', str(args.maxiter),
        '--directions', str(args.directions), '--active-rows', str(active_rows),
        '--qp-atol', repr(args.qp_atol), '--qp-rtol', repr(rtol)]
    if centers is not None:
        invocation.extend(['--coarse-centers', ','.join(repr(float(v)) for v in centers)])
    for path in [*direct_manifests, supplement]:
        invocation.extend(['--manifest', str(path)])
    prepared = subprocess.run([*invocation, '--print-command'], check=True, capture_output=True, text=True)
    command = shlex.split(prepared.stdout.strip())
    command[2] = derived['path']
    if args.qp_source is not None:
        qp_source = args.qp_source.resolve()
    else:
        candidates = [source_dir/'fullspace_feasible_active_cg_v2.py',
                      source_dir/'fullspace_feasible_active_cg_v3.py']
        recorded_qp_path = report.get('source_paths', {}).get('qp')
        if recorded_qp_path:
            candidates.append(Path(recorded_qp_path))
        matching = [path.resolve() for path in candidates if path.is_file()
                    and history.sha(path) == report.get('source_sha256_by_role', {}).get('qp')]
        if not matching:
            raise ValueError('Supply --qp-source explicitly or retain the actual parent QP module bytes')
        qp_source = matching[0]
    derivation.replace(command, '--qp-source', qp_source)
    derivation.replace(command, '--angles', shape['parent_full_angles'])
    derivation.replace(command, '--low-modes', report['coarse_low_modes'])
    derivation.replace(command, '--stage-block', args.stage_block)
    derivation.replace(command, '--target', report['target'])
    derivation.replace(command, '--active-block-columns', report['active_block_columns'])
    derivation.replace(command, '--active-top-curvature', report['active_top_curvature'])
    derivation.replace(command, '--active-top-radius', report['active_top_radius'])
    derivation.replace(command, '--line-trials', report['max_line_trials'])
    derivation.replace(command, '--qp-feasibility-tolerance', report['qp_feasibility_tolerance'])
    derivation.replace(command, '--qp-row-rank-tolerance', report['qp_row_rank_tolerance'])
    command.extend(['--active-rank-tolerance', str(report['active_rank_tolerance'])])
    if report.get('sampled_curvature_cap') is not None:
        command.extend(['--curvature-cap', str(report['sampled_curvature_cap'])])
    if centers is None:
        at = command.index('--coarse-centers')
        del command[at:at+2]
    roles = dict(operator='--operator', implementation='--implementation', basis='--basis-source',
        coarse='--coarse-source', helpers='--helpers', coordinates='--coordinate-source',
        scale='--scale-source', geometry='--geometry-source', point='--point-source',
        observed_geometry='--geometry-observed-source', base_batch='--base-batch-source',
        height='--height-source', angular='--angular-source', inequalities='--inequality-source',
        spectral='--spectral-source', spectral_hessian='--spectral-hessian-source',
        exact_tail='--exact-tail-source', tail_scalar='--tail-scalar-source',
        tail_integer='--tail-integer-source', tail_hold='--tail-hold-source')
    dependencies = {}
    for role, flag in roles.items():
        path = Path(argument(command, flag)).resolve()
        actual = history.file_record(path)
        if report.get('source_sha256_by_role', {}).get(role) != actual['sha256']:
            raise ValueError('The frozen physical/objective/norm dependency changed: '+role)
        dependencies[role] = actual
    canonical_roles = dict(scalar_source='tail_scalar', integer_source='tail_integer',
                           hold_source='tail_hold', observed_source='implementation')
    for canonical_role, role in canonical_roles.items():
        if model.get('source_sha256s', {}).get(canonical_role) != dependencies[role]['sha256']:
            raise ValueError('The canonical physical source identity changed: '+canonical_role)
    for canonical_role, role in dict(dense='operator', batch='base_batch', observed='implementation').items():
        if model.get('operator_source_sha256s', {}).get(canonical_role) != dependencies[role]['sha256']:
            raise ValueError('The canonical complete operator identity changed: '+canonical_role)
    qp_record = history.file_record(qp_source)
    records = {key: history.file_record(getattr(args, key)) for key in
               ('parent_report', 'bundle', 'carrier', 'node_report', 'scalar_input')}
    sources = {key: history.file_record(path) for key, path in dict(
        adapter=Path(__file__), history_helper=history_path, manifest_derivation=derivation_path,
        R671_launcher=launcher, original_launcher=original_launcher,
        frozen_driver=frozen_driver, canonical_factory=factory).items()}
    plan = dict(schema='actual-complete-full-Phi-report-to-identical-R671-model-continuation-v1',
        inputs=records, parent_driver=parent_source, actual_terminal_damping=damping,
        caller_manifests=caller_records, input_location_summary=initial_points,
        derived_driver=derived, QP_source=qp_record,
        parent_QP_sha256=report.get('source_sha256_by_role', {}).get('qp'),
        QP_solver_changed_explicitly=qp_record['sha256'] != report.get('source_sha256_by_role', {}).get('qp'),
        frozen_dependencies=dependencies, sources=sources,
        requested_directions=args.directions, maxiter=args.maxiter, qp_atol=args.qp_atol, qp_rtol=rtol,
        actual_working_row_cap=active_rows, default_one_direction=True,
        original_mesh_M_scalar_and_all_residual_rows_preserved=True,
        original_mean_Phi_and_physical_step_norm_preserved=True,
        canonical_model_identity_sha256=model_sha, canonical_model_definition=model,
        fixed_lambda=fixed_lambda, physical_eta_start=model['eta_start_symbolic'],
        physical_eta_end=model['eta_end_symbolic'], seed_transfer='keep-q',
        actual_source_lambda_equals_target_lambda=True,
        seed_physical_field_changed_or_nodal_projection_performed=False,
        factory_native_observed_sixjet_point_and_height_consumers_preserved=True,
        numerical_safety=.992, active_band=.025,
        manifest_input_changes=derived['derivation'],
        exact_distinct_binary_positions_retained=True, old_numerical_geometry_values_inherited=False,
        canonical_union_path=str(supplement), source_preparation_launcher_argv=invocation,
        full_scientific_command=command, output=str(args.outdir),
        scientific_arrays_read=False, scientific_execution_started=False,
        scope='The identical nonzero R671 physical representation is retained through every context consumer; manifest-only AST changes and any explicit QP choice are separately recorded')
    if plan_path.exists():
        prior = json.loads(plan_path.read_text())
        if (prior.get('scientific_execution_started') or prior.get('inputs') != records
                or prior.get('sources') != sources or prior.get('full_scientific_command') != command):
            raise FileExistsError('Use a fresh continuation-input directory for another actual plan')
    history.write_json(plan_path, plan)
    if args.print_command:
        print(shlex.join(command))
        return
    history.require_actions()
    plan.update(scientific_execution_started=True,
        execution={key: os.environ.get(key) for key in
                   ('GITHUB_REPOSITORY', 'GITHUB_RUN_ID', 'GITHUB_RUN_ATTEMPT', 'GITHUB_SHA')})
    history.write_json(plan_path, plan)
    resolved = points.resolve_grid(args.carrier)
    union = dict(schema=POSITION_SCHEMA, bundle_sha256=records['bundle']['sha256'],
        carrier_sha256=records['carrier']['sha256'], parent_report=records['parent_report'],
        source_sha256=sources['adapter']['sha256'], history_helper_sha256=HISTORY_SHA,
        **points.arrays(), values_inherited=False, decimal_position_rounding=False,
        recovered_parent_grid_points=resolved, extraction=points.summary(),
        caller_sources=caller_records)
    history.write_json(supplement, union, compact=True)
    plan.update(scientific_arrays_read=True, complete_position_union=history.file_record(supplement),
                resolved_position_counts=points.summary())
    history.write_json(plan_path, plan)
    print(json.dumps(dict(event='identical_R671_full_Phi_continuation_started',
        plan=history.file_record(plan_path), parent_sha256=records['bundle']['sha256'],
        damping=damping['terminal_damping'], QP_sha256=qp_record['sha256'],
        model_identity_sha256=model_sha, fixed_lambda=fixed_lambda,
        directions=args.directions, complete_locations=points.summary())), flush=True)
    environment = os.environ.copy()
    environment.update(PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='1',
                       OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')
    started = time.monotonic()
    returned = subprocess.run(command, env=environment, cwd=args.repo)
    result = dict(returncode=returned.returncode, seconds=time.monotonic()-started)
    returned_report = args.outdir/'report.json'
    if returned_report.is_file():
        result['report'] = history.file_record(returned_report)
    if returned.returncode == 0:
        outcome = json.loads(returned_report.read_text())
        final_bundle = args.outdir/'final.npz'
        if (outcome.get('complete') is not True
                or outcome.get('source_sha256') != derived['sha256']
                or outcome.get('source_sha256_by_role', {}).get('qp') != qp_record['sha256']
                or outcome.get('final_bundle_sha256') != history.sha(final_bundle)
                or outcome.get('exact_tail_context_final', {}).get('definition') != model
                or outcome.get('exact_tail_context_final', {}).get('model_identity_sha256') != model_sha
                or outcome.get('exact_tail_migration', {}).get('mode') != 'keep-q'
                or outcome.get('exact_tail_migration', {}).get('physical_field_unchanged') is not True):
            raise ValueError('The actual returned continuation identity is incomplete or inconsistent')
        result.update(final_bundle=history.file_record(final_bundle),
            actual_direction_count=len(outcome.get('directions', [])),
            accepted_directions=sum(bool(v.get('accepted')) for v in outcome.get('directions', [])),
            terminal_damping=history.terminal_damping(outcome),
            unchanged_canonical_model_identity_sha256=model_sha,
            final_known_point_filter=outcome.get('final_curvature_filter'))
    plan.update(scientific_execution_returned=True, actual_return=result)
    history.write_json(plan_path, plan)
    print(json.dumps(dict(event='identical_R671_full_Phi_continuation_returned',
        plan=history.file_record(plan_path), **result), allow_nan=False), flush=True)
    if returned.returncode:
        raise SystemExit(returned.returncode)


if __name__ == '__main__':
    main()
