#!/usr/bin/env python3
"""One genuine M-only complete-field continuation, public Actions only.

The original observation NPZ is reused byte for byte.  No radial restriction,
new quadrature, a interpolation, angular-grid change, or lambda migration is
performed.  Preparation reads completed reports and source metadata only.
--execute materializes zero-padded coordinates and runs one full QP batch in
the public repository's Actions.  Zero padding is not an error decrease.
"""
import argparse
import copy
from fractions import Fraction
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


SCHEMA = 'same-g-M-only-complete-Phi-continuation-v1'
HISTORY_SHA = '4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60'
DERIVATION_SHA = '100e57c66e1f5b592fe22570c6c7894a6ab75e082b714edfff42514098d5c622'
TRANSFER_HELPER_SHA = '2e8ae99813c105982b10b896606538c1c42baf0abf089457412b32e265d4411a'
ORIGINAL_DRIVER_SHA = '5ef7e26834b55d97d2c2dfc2d82f0113b2e072b2f46d3d54f04978177ce0629a'
TAIL_DRIVER_SHA = 'b1b0725acffde7958d9a4ad245057ea243d4319bde15bd9a7778ade3b0f844e8'
ORIGINAL_LAUNCHER_SHA = '6f021d459c24d5cb5a07853628d6a6a297332d51ad561beab2d09e50e2b34d63'
TAIL_LAUNCHER_SHA = 'c9ba1d73db3e3608dffa1dbc9aeeda2a355d2ff4c2b9fc8eed2140c985869ec7'
POSITION_SCHEMA = 'immutable-curvature-history-locations-v1'


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for part in iter(lambda: stream.read(1 << 20), b''):
            digest.update(part)
    return digest.hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def argument(command, flag):
    if command.count(flag) != 1:
        raise ValueError('Expected one literal argument '+flag)
    return command[command.index(flag)+1]


def finite_float(value, name):
    result = float(value)
    if not math.isfinite(result):
        raise ValueError('Need a finite value: '+name)
    return result


def source_inputs(folder):
    return dict(history=folder/'launch_refinement_from_full_report.py',
        derivation=folder/'launch_fixed_g_refinement_qp.py',
        transfer_helper=folder/'refine_fixed_g_fullclosed.py',
        original_launcher=folder/'launch_full_phi_qp_actions.py',
        tail_launcher=folder/'launch_full_phi_exact_tail_actions.py',
        original_driver=folder/'fullclosed_gauss_inequality_qp.py',
        tail_driver=folder/'fullclosed_gauss_exact_tail_inequality_qp.py')


def dimensions(report, modes):
    J, old, N = (int(report[key]) for key in ('J', 'M', 'N'))
    for key, value in (('J', J), ('M', old), ('N', N)):
        if report[key] != value:
            raise ValueError('Nonintegral parent dimension: '+key)
    M = 2*old if modes is None else modes
    rows = int(report['all_full_rows'])
    if (J < 2 or old < 3 or M <= old or N % 4 or N <= 4*M
            or rows != report['all_full_rows'] or rows % (3*N)):
        raise ValueError('Need Mnew>old M and the UNCHANGED full N>4*Mnew, divisible by four; angular refinement is a separate interface')
    P = rows//(3*N)
    if P < 2*J-1 or report['original_full_rows'] != 3*(2*J-1)*N:
        raise ValueError('The actual report has no complete original radial prefix')
    old_free, old_integrated = int(report['original_variables']), int(report['integrated_variables'])
    if old_integrated-old_free != 2*(3*old+2):
        raise ValueError('This bound parent is not the stated complete integrated coordinate layout')
    delta = M-old
    return dict(J=J, old_M=old, new_M=M, full_N=N, quarter_N=N//4+1,
        radial_observations=P, original_variables=old_free,
        new_original_variables=old_free+(9*J-15)*delta,
        integrated_variables=old_integrated,
        new_integrated_variables=old_integrated+9*(J-1)*delta,
        coarse_variables=int(report['coarse_variables']),
        added_original_variables=(9*J-15)*delta,
        residual_values_unchanged=rows,
        one_complete_quarter_residual_bytes=8*3*P*(N//4+1),
        new_qjet_carrier_bytes=8*J*3*(3*M+2),
        process_peak_memory_estimated=False,
        scope='Algebraic storage counts only; no field, array, runtime or convergence experiment')


def bound_objective(report):
    spectral = report.get('current', report.get('initial', {})).get('spectral', {})
    required = dict(p=8, epsilon=.001, scale=.05)
    if (report.get('objective') != 'spectral'
            or any(spectral.get(key) != value for key, value in required.items())
            or report.get('radial_weights', {}).get('legacy_fraction') != .5
            or report.get('angular_norm', {}).get('nu_c') != 24
            or report.get('numerical_reach_safety_factor') != .992
            or report.get('requested_reach_ratio') != .03
            or report.get('active_band') != .025):
        raise ValueError('This interface preserves the declared p8/.001/.05, original half-mixture, nu_c24 and .992/.025 complete-QP model')
    return dict(**required, legacy_fraction=.5, angular_transition=24.,
        normalization=spectral['normalization'], original_carrier_reused=True,
        old_and_new_M_functionals_identical_on_the_included_subspace=True)


def select_qp(report, folder, explicit, history):
    if explicit is not None:
        return explicit.resolve()
    candidates = [folder/'fullspace_feasible_active_cg_v2.py',
                  folder/'fullspace_feasible_active_cg_v3.py']
    actual_path = report.get('source_paths', {}).get('qp')
    if actual_path:
        candidates.append(Path(actual_path))
    wanted = report.get('source_sha256_by_role', {}).get('qp')
    for path in candidates:
        if path.is_file() and history.sha(path) == wanted:
            return path.resolve()
    raise ValueError('Retain the actual parent QP module or select another one explicitly with --qp-source')


def prepare(args):
    folder = args.repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261120'
    paths = source_inputs(folder)
    pins = dict(history=HISTORY_SHA, derivation=DERIVATION_SHA,
        transfer_helper=TRANSFER_HELPER_SHA, original_launcher=ORIGINAL_LAUNCHER_SHA,
        tail_launcher=TAIL_LAUNCHER_SHA, original_driver=ORIGINAL_DRIVER_SHA,
        tail_driver=TAIL_DRIVER_SHA)
    for key, expected in pins.items():
        if sha(paths[key]) != expected:
            raise ValueError('Changed published dependency: '+key)
    history = load('M_only_complete_history', paths['history'])
    derivation = load('M_only_manifest_derivation', paths['derivation'])
    report = json.loads(args.parent_report.read_text())
    parent_source = history.bound_parent_source(report, folder, args.parent_source)
    damping = history.terminal_damping(report)
    if report.get('final_bundle_sha256') != sha(args.bundle):
        raise ValueError('The supplied field is not the naturally completed report final bundle')
    carrier_sha = sha(args.carrier)
    if report.get('observation_carrier_sha256') != carrier_sha:
        raise ValueError('Use the literal actual parent observation carrier')
    objective = bound_objective(report)
    shape = dimensions(report, args.modes)
    base = parent_source.get('declared_derivation', {}).get('frozen_driver_sha256',
                                                          parent_source['sha256'])
    if base not in (ORIGINAL_DRIVER_SHA, TAIL_DRIVER_SHA):
        raise ValueError('Unsupported completed full-QP parent')
    is_tail = base == TAIL_DRIVER_SHA
    if is_tail:
        if (report.get('exact_tail_node_report_sha256') != sha(args.node_report)
                or report.get('exact_tail_scalar_input_sha256') != sha(args.scalar_input)):
            raise ValueError('The current R671 node/scalar sources must belong to this actual parent')
        lam = finite_float(report['exact_tail_lambda'], 'parent lambda')
        eta = int(report['exact_tail_eta_start_node'])
        if not 0 <= lam <= 1 or eta != report['exact_tail_eta_start_node'] or eta < 1:
            raise ValueError('Invalid actual R671 report model')
    else:
        lam, eta = 0., None
    points = history.Locations(shape['J'], shape['radial_observations'], shape['full_N'])
    points.walk(report)
    caller_records, direct_manifests = [], []
    for index, path in enumerate(args.manifest):
        payload = json.loads(path.read_text())
        declared = payload.get('carrier_sha256', payload.get('observation_carrier_sha256'))
        if declared is not None and declared != carrier_sha:
            raise ValueError('A supplied manifest declares another radial observation carrier')
        points.walk(payload, path=('caller_manifest', index))
        pure = payload.get('schema') == POSITION_SCHEMA
        if pure:
            direct_manifests.append(path)
        caller_records.append(dict(**history.file_record(path), passed_unchanged=pure,
            complete_recognized_location_union=True,
            noncanonical_format_rule=None if pure else 'Every recognized complete-history position enters the exact binary tuple union; geometric values are not inherited'))
    active_rows = int(report['active_max_rows']) if args.active_rows is None else args.active_rows
    rtol = finite_float(report['qp_rtol'] if args.qp_rtol is None else args.qp_rtol, 'qp rtol')
    if active_rows < 1 or rtol < 0:
        raise ValueError('Invalid explicit continuation solver parameters')
    inputs = {key: history.file_record(getattr(args, key)) for key in
              ('parent_report', 'bundle', 'carrier', 'node_report', 'scalar_input')}
    plan_path = args.outdir/'frequency-plan.json'
    if plan_path.exists() and json.loads(plan_path.read_text()).get('scientific_execution_started'):
        raise FileExistsError('An actual attempt already owns this output directory')
    if (args.outdir/'solve').exists() or (args.outdir/'frequency-seed.npz').exists():
        raise FileExistsError('Use a fresh directory for another actual M-only attempt')
    args.outdir.mkdir(parents=True, exist_ok=True)
    derived = derivation.derive_driver(paths['tail_driver' if is_tail else 'original_driver'],
                                      args.outdir/'derived-full-phi-exact-positions.py')
    seed = args.outdir/'frequency-seed.npz'
    new_nodes = args.outdir/'same-nodes-new-M.json'
    union = args.outdir/'complete-permanent-locations.json'
    solver_out = args.outdir/'solve'
    launcher = paths['tail_launcher' if is_tail else 'original_launcher']
    invocation = [sys.executable, str(launcher), '--repo', str(args.repo), '--work', str(args.work),
        '--bundle', str(seed), '--carrier', str(args.carrier), '--outdir', str(solver_out),
        '--damping', repr(damping['terminal_damping']), '--maxiter', str(args.maxiter),
        '--directions', str(args.directions), '--active-rows', str(active_rows),
        '--qp-atol', repr(args.qp_atol), '--qp-rtol', repr(rtol)]
    centers = report.get('requested_coarse_centers')
    if centers is not None:
        invocation.extend(['--coarse-centers', ','.join(repr(float(v)) for v in centers)])
    if is_tail:
        invocation.extend(['--node-report', str(new_nodes), '--scalar-input', str(args.scalar_input),
            '--eta-start-node', str(eta), '--lambda-value', repr(lam),
            '--source-lambda', repr(lam), '--migration', 'keep-q'])
    for path in [*direct_manifests, union]:
        invocation.extend(['--manifest', str(path)])
    prepared = subprocess.run([*invocation, '--print-command'], check=True,
                              capture_output=True, text=True)
    command = shlex.split(prepared.stdout.strip())
    command[2] = derived['path']
    qp_source = select_qp(report, folder, args.qp_source, history)
    derivation.replace(command, '--qp-source', qp_source)
    overrides = {'--angles': shape['full_N'], '--low-modes': report['coarse_low_modes'],
        '--stage-block': args.stage_block, '--target': report['target'],
        '--active-block-columns': report['active_block_columns'],
        '--active-top-curvature': report['active_top_curvature'],
        '--active-top-radius': report['active_top_radius'],
        '--line-trials': report['max_line_trials'],
        '--qp-feasibility-tolerance': report['qp_feasibility_tolerance'],
        '--qp-row-rank-tolerance': report['qp_row_rank_tolerance']}
    for flag, value in overrides.items():
        derivation.replace(command, flag, value)
    command.extend(['--active-rank-tolerance', repr(report['active_rank_tolerance'])])
    if report.get('sampled_curvature_cap') is not None:
        command.extend(['--curvature-cap', repr(report['sampled_curvature_cap'])])
    if centers is None:
        at = command.index('--coarse-centers')
        del command[at:at+2]
    roles = dict(operator='--operator', implementation='--implementation', basis='--basis-source',
        coarse='--coarse-source', helpers='--helpers', coordinates='--coordinate-source',
        scale='--scale-source', geometry='--geometry-source', point='--point-source',
        observed_geometry='--geometry-observed-source', base_batch='--base-batch-source',
        height='--height-source', angular='--angular-source', inequalities='--inequality-source',
        spectral='--spectral-source', spectral_hessian='--spectral-hessian-source')
    if is_tail:
        roles.update(exact_tail='--exact-tail-source', tail_scalar='--tail-scalar-source',
                     tail_integer='--tail-integer-source', tail_hold='--tail-hold-source')
    dependencies = {}
    for role, flag in roles.items():
        actual = history.file_record(Path(argument(command, flag)).resolve())
        if actual['sha256'] != report.get('source_sha256_by_role', {}).get(role):
            raise ValueError('Changed frozen complete objective/field/norm dependency: '+role)
        dependencies[role] = actual
    if int(report['coarse_low_modes']) > shape['old_M']:
        raise ValueError('The unchanged coarse basis must be contained in the parent mode space')
    qp_record = history.file_record(qp_source)
    sources = {key: history.file_record(path) for key, path in paths.items()}
    sources['entry'] = history.file_record(__file__)
    plan = dict(schema=SCHEMA, inputs=inputs, source_sha256=sha(__file__), sources=sources,
        parent_driver=parent_source, parent_terminal_damping=damping,
        dimensions=shape, objective=objective, is_R671=is_tail,
        unchanged_lambda=lam, unchanged_eta_start_node=eta,
        caller_manifests=caller_records, complete_history_summary=points.summary(),
        derived_driver=derived, frozen_dependencies=dependencies, QP_source=qp_record,
        parent_QP_sha256=report.get('source_sha256_by_role', {}).get('qp'),
        QP_solver_changed_explicitly=qp_record['sha256'] != report.get('source_sha256_by_role', {}).get('qp'),
        requested_directions=args.directions, maxiter=args.maxiter, qp_atol=args.qp_atol,
        qp_rtol=rtol, actual_working_row_cap=active_rows,
        source_preparation_launcher_argv=invocation, full_scientific_command=command,
        outputs=dict(seed=str(seed), node_report=str(new_nodes), observations=str(args.carrier),
                     permanent_locations=str(union), solver_directory=str(solver_out)),
        original_observation_file_reused=True, same_radial_nodes=True,
        same_every_a_value_and_radial_weight=True, same_full_N_and_angular_weights=True,
        original_objective_restricted_to_old_subspace_unchanged=True,
        complete_step_norm_restricted_to_old_subspace_unchanged=True,
        all_permanent_locations_retained=True, old_geometry_values_inherited=False,
        preparation_scope='Completed-report/source binding and argv only; actual arrays, exact node/scalar identity and padding are checked only by the Actions execution below',
        scientific_arrays_read=False, scientific_execution_started=False,
        zero_padding_improvement_claimed=False, frequency_convergence_demonstrated=False,
        continuous_metric_certified=False, continuous_geometry_certified=False,
        topic_completion_certified=False)
    if plan_path.exists():
        prior = json.loads(plan_path.read_text())
        for key in ('inputs', 'sources', 'full_scientific_command', 'dimensions', 'caller_manifests'):
            if prior.get(key) != plan[key]:
                raise FileExistsError('Use a fresh directory for a different M-only preparation')
    history.write_json(plan_path, plan)
    return dict(history=history, report=report, plan=plan, plan_path=plan_path,
                points=points, paths=paths, seed=seed, new_nodes=new_nodes,
                union=union, command=command)


def affine_input(np, jets, fixed):
    """The published exact affine layout, without a field evaluation."""
    J, _, n = jets.shape
    M = (n-2)//3
    if jets.shape != (J, 3, 3*M+2) or not np.isfinite(jets).all():
        raise ValueError('Invalid actual qjet array')
    core = jets[0, 0, 1:M+1]
    expected = jets.copy()
    expected[0, 0] = 0.
    expected[0, 0, 0] = 1.
    expected[0, 0, 1:M+1] = core
    expected[0, 0, M+1:2*M+1] = -2*np.arange(1, M+1)*core
    expected[0, 1] = 0.
    expected[0, 1, 2*M+1] = 1.
    expected[0, 2, 2*M+1:] = 0.
    expected[-1] = 0.
    if not np.array_equal(core[:len(fixed)], fixed) or not np.array_equal(expected, jets):
        raise ValueError('The actual parent/seed is outside the published exact affine interface')


def array_identity(np, left, right):
    return (left.dtype == right.dtype and left.shape == right.shape
            and left.tobytes(order='C') == right.tobytes(order='C'))


def materialize(args, state):
    history, plan, report = state['history'], state['plan'], state['report']
    history.require_actions()
    # No numerical package or field/scalar source is imported before this guard.
    import numpy as np
    helper = load('M_only_R676_layout_helpers', state['paths']['transfer_helper'])
    paths = helper.sources(args.repo)
    for key, path in paths.items():
        if sha(path) != helper.EXPECTED[key]:
            raise ValueError('Changed published coordinate/model helper dependency: '+key)
    observed = helper.load('M_only_observation_plan', paths['observed'])
    factory = helper.load('M_only_reference_tail_factory', paths['factory'])
    with np.load(args.bundle, allow_pickle=False) as raw:
        data = {key: np.array(raw[key], copy=True) for key in raw.files}
    with np.load(args.carrier, allow_pickle=False) as raw:
        carrier = {key: np.array(raw[key], copy=True) for key in raw.files}
    shape = plan['dimensions']
    J, old, M, N, P = (shape[key] for key in
                        ('J', 'old_M', 'new_M', 'full_N', 'radial_observations'))
    if data['qjets'].shape != (J, 3, 3*old+2) or data['mesh'].shape != (J,):
        raise ValueError('Actual parent arrays differ from its complete report dimensions')
    for key in ('mesh', 'a_stages', 'radius', 'width', 'fixed_core_first3'):
        if not array_identity(np, data[key], carrier[key]):
            raise ValueError('Parent and original observation carrier differ: '+key)
    if (not np.isfinite(data['mesh']).all() or not np.all(np.diff(data['mesh']) > 0)
            or data['a_stages'].shape != (2*J-1,)):
        raise ValueError('Invalid original radial carrier')
    observation_plan = observed.ObservationPlan.from_arrays(carrier)
    if (len(observation_plan.cells) != P or observation_plan.legacy_count != 2*J-1
            or carrier['a_observations'].shape != (P,)):
        raise ValueError('The original complete observation plan differs from the parent report')
    recorded_N = carrier.get('observation_default_full_angles',
                             data.get('refinement_evaluation_full_angles'))
    # A carrier's default-N label is not an angular observation array.  The
    # actual completed driver report binds the N used here, even when that
    # driver explicitly overrode an older carrier's default.
    old_report = json.loads(args.node_report.read_text())
    if old_report.get('input_sha256') != sha(args.scalar_input):
        raise ValueError('Keep the original exact scalar source input')
    nodes = [(Fraction(v['S_coefficient']), Fraction(v['constant']))
             for v in old_report['true_scalar_nodes']]
    anchors = old_report['true_a_stage_boxes']
    if (len(nodes) != J or nodes[0] != (Fraction(0), Fraction(0))
            or nodes[-1] != (Fraction(1), Fraction(0)) or len(anchors) != 2*J-1
            or float(old_report['S_carrier']) != float(data['mesh'][-1])
            or float(old_report['radius_carrier']) != float(data['radius'])):
        raise ValueError('Actual field and supplied complete symbolic node/anchor definition differ')
    if 'M' in old_report and int(old_report['M']) != old:
        raise ValueError('The supplied current node report has another mode-carrier identity')
    for anchor in anchors:
        lo, hi = Fraction(anchor['lower_exact']), Fraction(anchor['upper_exact'])
        if lo <= 0 or hi < lo:
            raise ValueError('Need the existing positive true node/midpoint a enclosures')
    model = helper.model_definition(data, nodes, paths, args.node_report,
                                   args.carrier, args.scalar_input, factory)
    if (model['definition'] is not None) != plan['is_R671']:
        raise ValueError('The actual original/R671 representation differs from its completed report')
    if model['lambda_value'] != plan['unchanged_lambda']:
        raise ValueError('The actual source lambda differs from the completed report')
    if plan['is_R671'] and int(model['definition']['eta_start_node']) != plan['unchanged_eta_start_node']:
        raise ValueError('The actual source eta differs from the completed report')
    affine_input(np, data['qjets'], data['fixed_core_first3'])
    jets = helper.pad_modes(data['qjets'], old, M)
    # unpack derives core T=-nu*c, hence -0 in the added core-T slots.
    # Match that representation without modifying any old coefficient.
    jets[0, 0, M+old+1:2*M+1] = -0.
    affine_input(np, jets, data['fixed_core_first3'])
    slices = [(slice(0, old+1), slice(0, old+1)),
              (slice(old+1, 2*old+1), slice(M+1, M+old+1)),
              (slice(2*old+1, 3*old+2), slice(2*M+1, 2*M+old+2))]
    if not all(array_identity(np, data['qjets'][..., a], jets[..., b]) for a, b in slices):
        raise ArithmeticError('Zero padding must copy every old physical coefficient exactly')
    new_report = dict(schema='fixed-radial-carrier-new-frequency-identity-v1',
        source_sha256=sha(__file__), input_path=str(args.scalar_input),
        input_sha256=sha(args.scalar_input), scalar_source_path=str(paths['scalar']),
        scalar=copy.deepcopy(old_report['scalar']),
        S_carrier=float(data['mesh'][-1]), radius_carrier=float(data['radius']),
        M=M, n=3*M+2, J=J, cells=J-1, stages=2*J-1, observation_rows=P,
        suggested_operator_N=N, Hcap=float(data['Hcap']),
        width_exact=str(Fraction(float(data['width']))), width_carrier=float(data['width']),
        true_scalar_nodes=copy.deepcopy(old_report['true_scalar_nodes']),
        true_a_stage_boxes=copy.deepcopy(anchors),
        scalar_anchor_source=history.file_record(args.node_report),
        observation_carrier=history.file_record(args.carrier),
        exact_radial_node_definition_unchanged=True,
        actual_target_a_values_unchanged=True, scalar_oracle_requery_for_new_nodes=False,
        anchor_reuse_reason='Identical exact alpha*S+beta nodes and their original midpoint positions, same FullHold and original a; only the angular coefficient-space dimension changed',
        source_bundle=history.file_record(args.bundle), source_M=old, target_M=M,
        field_definition='Old binary free coefficients copied exactly into R/T/Z slots, added modes zero; exact derived core T slots and the same analytic lift',
        numerical_operator_scope='The exact same ordinary observation carrier/weights/a and angular grid; not a continuous metric or geometry certificate',
        old_candidate_certificates_inherited=False,
        nonlinear_solve=False, metric_accepted=False, embedding_certified=False,
        reach_certified=False)
    for key in ('maximum_a_carrier_error_upper', 'maximum_stage_time_carrier_error_upper'):
        if key in old_report:
            new_report[key] = old_report[key]
    history.write_json(state['new_nodes'], new_report)
    keys = ('mesh', 'a_stages', 'radius', 'width', 'fixed_core_first3',
            'a_stage_absolute_error', 'stage_time_absolute_error')
    arrays = {key: np.array(data[key], copy=True) for key in keys if key in data}
    arrays.update(qjets=jets, Hcap=np.array(data['Hcap'], copy=True),
                  core_coefficients=jets[0, 0, 1:M+1].copy(),
                  refinement_evaluation_full_angles=np.array(N))
    profile = None
    if plan['is_R671']:
        # Validate the old definition above, then explicitly create the new
        # same-field model identity.  The old cross-M transfer_seed guard is
        # never bypassed or relabelled as a migration within the same model.
        panels = int(old_report['scalar']['simpson_panels_per_ramp'])
        if panels != 128:
            raise ValueError('This frozen R671 full driver uses 128 oracle panels; another carrier policy needs an explicit matching driver')
        provisional = args.outdir/'zero-padded-coordinate-carrier.npz'
        np.savez_compressed(provisional, **arrays)
        context = factory.TailLiftContext.from_files(bundle=provisional, carrier=args.carrier,
            node_report=state['new_nodes'], scalar_input=args.scalar_input,
            scalar_source=paths['scalar'], integer_source=paths['integer'],
            hold_source=paths['hold'], observed_source=paths['observed'],
            eta_start_node=plan['unchanged_eta_start_node'],
            lambda_value=plan['unchanged_lambda'], panels=panels)
        problem, _ = context.create_pair(paths['dense'], paths['batch'],
            N=N, stage_block=args.stage_block, quarter=True)
        definition = context.definition()
        for key in ('eta_start_node', 'eta_end_node', 'eta_start_symbolic', 'eta_end_symbolic',
                    'lambda_value', 'mesh_sha256', 'scalar_input_sha256',
                    'original_observation_carrier_sha256', 'source_sha256',
                    'source_sha256s', 'operator_source_sha256s'):
            if definition[key] != model['definition'][key]:
                raise ArithmeticError('M-only rebind changed a physical R671 identity: '+key)
        if definition['M'] != M or definition['node_report_sha256'] != sha(state['new_nodes']):
            raise ArithmeticError('The new R671 model did not bind the new M carrier')
        if not array_identity(np, context.a_observations, carrier['a_observations']):
            raise ArithmeticError('R671 cannot replace the original target a values')
        profile = context.save_carrier(args.outdir/'same-tail-new-M-profiles.npz',
                                       args.outdir/'same-tail-new-M-profiles.json')
        x, affine = problem.pack(jets, float(data['Hcap']), require_affine=True)
        final_arrays = context.bundle_arrays(problem, x)
        final_arrays.update(field_representation=np.array('R671-exact-reference-tail-v1'),
            exact_tail_lambda=np.array(plan['unchanged_lambda']),
            exact_tail_eta_start_node=np.array(plan['unchanged_eta_start_node'], dtype=np.int64),
            exact_tail_source_sha256=np.array(sha(paths['factory'])),
            exact_tail_scalar_input_sha256=np.array(sha(args.scalar_input)),
            exact_tail_profile_carrier_sha256=np.array(profile['sha256']),
            exact_tail_profile_manifest_sha256=np.array(profile['report_sha256']),
            refinement_evaluation_full_angles=np.array(N))
        if not array_identity(np, final_arrays['qjets'], jets):
            raise ArithmeticError('Canonical R671 materialization changed a copied free coefficient')
        arrays = final_arrays
        model_record = definition
    else:
        affine = dict(exact_affine_input=True, method='The literal published affine layout checked before and after the channelwise zero copy')
        model_record = dict(kind='original_polynomial_lift', lambda_value=0., M=M)
    for key in keys:
        if key in data and not array_identity(np, arrays[key], data[key]):
            raise ArithmeticError('M-only materialization changed a radial/scalar carrier: '+key)
    if not array_identity(np, arrays['Hcap'], data['Hcap']):
        raise ArithmeticError('M-only materialization changed the cap height')
    np.savez_compressed(state['seed'], **arrays)
    resolved = state['points'].resolve_grid(args.carrier)
    locations = dict(schema=POSITION_SCHEMA, bundle_sha256=sha(state['seed']),
        carrier_sha256=sha(args.carrier), source_sha256=sha(__file__),
        parent_bundle_sha256=sha(args.bundle), parent_report=history.file_record(args.parent_report),
        history_helper_sha256=HISTORY_SHA, caller_sources=plan['caller_manifests'],
        **state['points'].arrays(), extraction=state['points'].summary(),
        recovered_parent_grid_points=resolved, decimal_position_rounding=False,
        radial_or_angular_location_mapping='Identity: original cells, binary u and phi, and full N unchanged',
        values_inherited=False, all_recognized_permanent_positions_retained=True,
        core_Theta_unchanged_at_transfer=True)
    history.write_json(state['union'], locations, compact=True)
    if sha(args.carrier) != plan['inputs']['carrier']['sha256']:
        raise ArithmeticError('The original observation carrier changed during materialization')
    transfer = dict(schema=SCHEMA+'-transfer', source_sha256=sha(__file__),
        inputs=plan['inputs'], dimensions=shape, exact_affine_seed=affine,
        outputs=dict(seed=history.file_record(state['seed']),
                     node_report=history.file_record(state['new_nodes']),
                     observations=history.file_record(args.carrier),
                     permanent_locations=history.file_record(state['union'])),
        parent_model=model['definition'] or dict(kind=model['kind'], lambda_value=0.),
        new_model=model_record, new_reference_profile=profile,
        helper_dependencies={key: history.file_record(path) for key, path in paths.items()},
        old_physical_coefficients_bitwise_unchanged=True, added_modes_exactly_zero=True,
        same_exact_quintic_polynomials=True, same_exact_analytic_lift=True,
        exact_sixjet_transfer_difference_zero=True,
        zero_padding_uses_floating_arithmetic_on_old_free_coefficients=False,
        literal_affine_T_reconstruction_checked=True,
        original_observation_carrier_bytes_unchanged=True,
        same_ObservationPlan_and_every_scalar_value_and_weight=True,
        original_carrier_default_full_angles=(int(recorded_N) if recorded_N is not None else None),
        actual_full_angles_from_completed_report=N,
        original_node_midpoint_true_a_boxes_retained_at_identical_exact_points=True,
        original_target_a_interpolated_or_recomputed=False,
        reference_tail_profile_rebound_to_new_M=plan['is_R671'],
        finite_field_readout_performed=False, bitwise_residual_evaluation_identity_claimed=False,
        complete_position_summary=state['points'].summary(),
        nonlinear_solve_performed=False, zero_padding_improvement_claimed=False,
        frequency_convergence_demonstrated=False, topic_completion_certified=False,
        old_candidate_certificates_inherited=False)
    path = args.outdir/'frequency-transfer.json'
    history.write_json(path, transfer)
    return path


def statistics_snapshot(stats):
    spectral = stats.get('spectral', {})
    return dict(mean_Phi=spectral.get('phi_normalized'),
        normalization=spectral.get('normalization'),
        max_relative_Gram=stats.get('max_relative_gram'),
        original_weighted_mean_sse=spectral.get('original_weighted_mean_sse'),
        original_weighted_sse=spectral.get('original_weighted_sse'))


def execute(args, state):
    history, plan = state['history'], state['plan']
    history.require_actions()
    plan.update(scientific_execution_started=True,
        execution={key: os.environ.get(key) for key in
                   ('GITHUB_REPOSITORY', 'GITHUB_RUN_ID', 'GITHUB_RUN_ATTEMPT', 'GITHUB_SHA')},
        stage='materializing_exact_zero_padding')
    history.write_json(state['plan_path'], plan)
    transfer_path = materialize(args, state)
    plan.update(scientific_arrays_read=True, transfer_report=history.file_record(transfer_path),
        actual_seed=history.file_record(state['seed']),
        complete_permanent_locations=history.file_record(state['union']),
        complete_position_summary=state['points'].summary(), stage='full_QP_started')
    history.write_json(state['plan_path'], plan)
    print(json.dumps(dict(event='M_only_full_QP_started', plan=history.file_record(state['plan_path']),
        old_M=plan['dimensions']['old_M'], new_M=plan['dimensions']['new_M'],
        unchanged_carrier_sha256=plan['inputs']['carrier']['sha256'],
        same_finite_objective=True, zero_padding_improvement_claimed=False)), flush=True)
    environment = os.environ.copy()
    environment.update(PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='1',
                       OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')
    started = time.monotonic()
    returned = subprocess.run(state['command'], env=environment, cwd=args.repo)
    result = dict(returncode=returned.returncode, seconds=time.monotonic()-started,
        naturally_complete=False, additional_field_evaluation_for_attribution=False)
    report_path = args.outdir/'solve/report.json'
    if report_path.is_file():
        result['report'] = history.file_record(report_path)
    if returned.returncode == 0:
        outcome = json.loads(report_path.read_text())
        final_bundle = args.outdir/'solve/final.npz'
        dim = plan['dimensions']
        if (outcome.get('complete') is not True
                or outcome.get('source_sha256') != plan['derived_driver']['sha256']
                or outcome.get('source_sha256_by_role', {}).get('qp') != plan['QP_source']['sha256']
                or outcome.get('bundle_sha256') != sha(state['seed'])
                or outcome.get('observation_carrier_sha256') != plan['inputs']['carrier']['sha256']
                or outcome.get('final_bundle_sha256') != sha(final_bundle)
                or any(outcome.get(key) != value for key, value in
                       dict(M=dim['new_M'], J=dim['J'], N=dim['full_N'],
                            all_full_rows=dim['residual_values_unchanged'],
                            original_variables=dim['new_original_variables'],
                            integrated_variables=dim['new_integrated_variables'],
                            coarse_variables=dim['coarse_variables']).items())):
            raise ValueError('The naturally returned M-only full batch has inconsistent actual identities')
        objective = bound_objective(outcome)
        if objective['normalization'] != plan['objective']['normalization']:
            raise ValueError('The same observation functional unexpectedly changed normalization')
        if plan['is_R671'] and (outcome.get('exact_tail_lambda') != plan['unchanged_lambda']
                or outcome.get('exact_tail_eta_start_node') != plan['unchanged_eta_start_node']
                or outcome.get('exact_tail_node_report_sha256') != sha(state['new_nodes'])
                or outcome.get('exact_tail_scalar_input_sha256') != plan['inputs']['scalar_input']['sha256']):
            raise ValueError('The actual returned R671 solve changed the declared same-field model parameters')
        parent = statistics_snapshot(state['report'].get('current', state['report']['initial']))
        initial = statistics_snapshot(outcome['initial'])
        final = statistics_snapshot(outcome.get('current', outcome['initial']))
        comparisons = dict(parent=parent, zero_padded_initial=initial, after_actual_solve=final,
            same_radial_and_angular_functional=True,
            differences_are_ordinary_finite_evaluations_not_outward_certificates=True,
            new_only_observation_rows=0, angular_grid_changed=False,
            zero_padding_improvement_claimed=False, frequency_convergence_demonstrated=False)
        for name, left, right in (
                ('binary_evaluation_shift_at_zero_padding', parent, initial),
                ('same_grid_Phi_change_from_actual_solve', initial, final),
                ('same_grid_parent_to_final_Phi_change', parent, final)):
            a, b = left['mean_Phi'], right['mean_Phi']
            comparisons[name] = (float(b)-float(a) if a is not None and b is not None
                                 and math.isfinite(float(a)) and math.isfinite(float(b)) else None)
        result.update(naturally_complete=True, final_bundle=history.file_record(final_bundle),
            actual_direction_count=len(outcome.get('directions', [])),
            accepted_directions=sum(bool(value.get('accepted')) for value in outcome.get('directions', [])),
            actual_terminal_damping=history.terminal_damping(outcome),
            final_known_point_filter=outcome.get('final_curvature_filter'),
            same_functional_attribution=comparisons)
    plan.update(scientific_execution_returned=True,
        stage='naturally_complete' if result['naturally_complete'] else 'solver_failed_or_incomplete',
        actual_return=result, frequency_convergence_demonstrated=False,
        continuous_metric_certified=False, continuous_geometry_certified=False,
        topic_completion_certified=False)
    history.write_json(state['plan_path'], plan)
    print(json.dumps(dict(event='M_only_full_QP_returned',
        plan=history.file_record(state['plan_path']), **result), allow_nan=False), flush=True)
    if returned.returncode:
        raise SystemExit(returned.returncode)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('repo', 'work', 'parent-report', 'bundle', 'carrier', 'node-report', 'scalar-input', 'outdir'):
        parser.add_argument('--'+key, type=Path, required=True)
    parser.add_argument('--manifest', type=Path, action='append', required=True)
    parser.add_argument('--parent-source', type=Path)
    parser.add_argument('--qp-source', type=Path)
    parser.add_argument('--modes', type=int, help='Mnew; default twice the actual completed parent M')
    parser.add_argument('--directions', type=int, default=1)
    parser.add_argument('--maxiter', type=int, default=256)
    parser.add_argument('--stage-block', type=int, default=64)
    parser.add_argument('--active-rows', type=int)
    parser.add_argument('--qp-rtol', type=float)
    parser.add_argument('--qp-atol', type=float, default=0.)
    parser.add_argument('--execute', action='store_true')
    args = parser.parse_args()
    if (args.directions < 1 or args.maxiter < 1 or args.stage_block < 1
            or not math.isfinite(args.qp_atol) or args.qp_atol < 0):
        raise ValueError('Need positive counts and finite nonnegative absolute QP tolerance')
    for key in ('repo', 'work', 'parent_report', 'bundle', 'carrier', 'node_report', 'scalar_input', 'outdir'):
        setattr(args, key, getattr(args, key).resolve())
    args.manifest = [path.resolve() for path in args.manifest]
    if args.parent_source is not None:
        args.parent_source = args.parent_source.resolve()
    state = prepare(args)
    if not args.execute:
        print(json.dumps(dict(event='M_only_prepared_not_executed',
            plan=state['history'].file_record(state['plan_path']),
            dimensions=state['plan']['dimensions'],
            scientific_arrays_read=False, scientific_execution_started=False,
            command=state['command']), allow_nan=False), flush=True)
        return
    try:
        execute(args, state)
    except Exception as error:
        state['plan'].update(stage='exception_no_completion_claim',
            exception=dict(type=type(error).__name__, message=str(error)),
            frequency_convergence_demonstrated=False, topic_completion_certified=False)
        state['history'].write_json(state['plan_path'], state['plan'])
        raise


if __name__ == '__main__':
    main()

