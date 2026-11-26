#!/usr/bin/env python3
# Explicit complete held-amplitude augmentation of R688:
# {"all_current_grid_and_permanent_locations_screened_before_acceptance": true, "all_original_inequalities_and_variables_retained": true, "appended_point_and_cap_height_inequalities": true, "both_witness_signs": true, "complete_R688_base_sha256": "bf25c6d70b6ae4c92e08162b8c75969edcd301ba44d00554f8a55fc806f056bc", "complete_current_mean_objective_preserved": true, "complete_free_core_witness_derivative": true, "new_scientific_execution_by_authoring_script": false, "original_R688_source_deriver_sha256": "b57ab303682f708c6d205cf0d527df2ec16aa2cfa1762a59070599abcade6d75", "schema": "complete-amplitude-augmentation-of-R688-source-v1"}
"""R684 NEW rotational-metric design with the complete observed J/J*.

The actual R671 field, original free variables, H2-type mother norm,
positive radial/orbit rows, and permanent physical inequality memory remain.
The target is explicitly changed to g_x=Ebar_x(s) ds^2+Cbar_x(s) dtheta^2.
Every target-normalization and, for material averaging, rho-weight derivative
is included by MeanMetricOperator. The residual-Hessian bridge calls this
complete wrapper; no old physical angular-moment Jacobian is reused.

This is moving-target DESIGN, never fixed-g convergence. Every trial uses
its own declared mean metric, actual true Phi, and actual six-jet geometry.
A final metric must subsequently be frozen and refined independently.
Additional fixed Dmarked/L/Hmin point inequalities use the complete moving
witness derivative and true all-grid/all-permanent-location screening.
Every original geometry row remains; finite screens do not prove continuous
amplitude, embedding or reach. No scientific result is claimed by this
source alone. Run in public Actions.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import resource
import os
import subprocess
import numpy as np
from scipy.sparse.linalg import LinearOperator
from scipy.linalg import solve_triangular
MEAN_COARSE_EXPECTED_SOURCES = {'mean_coarse': '9e7ca6ba0cf3821ab8498226354d8422c2cfacee1ef07dafb8fc5868968fb9e3', 'coarse_frame': '324513a115a61800e105f340bd070eb50931bbe16dd66d3a8643bfe11298f2da', 'coarse_qp_v3': 'fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4', 'qp': '76b27520a433d85a52c3037ed5d519860b1002b0fb137378c855dad2993855e8', 'mean_transform': 'b7eb35d5e7c1d32baf8d4e94c0c9651d46d5cbfea65a6c1c098ae24d42f0b624', 'spectral_hessian': '29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4', 'spectral': 'e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91'}
MEAN_CENTERED_SOURCE_SHA = '5e5798e3fd46535ef91db5171c885701caf23f3a17a47f28d4dad9e557ce2a01'

def _mean_coarse_sources(args, paths):
    if args.objective != 'spectral':
        raise ValueError('R688 consumes the declared current spectral mean-metric bridge')
    if args.coarse_moment_stage_block < 1:
        raise ValueError('Use a positive mean-moment radial block size')
    paths.update(mean_coarse=args.mean_coarse_source.resolve(), coarse_frame=args.coarse_frame_source.resolve(), coarse_qp_v3=args.coarse_v3_source.resolve())
    records = {}
    for role, digest in MEAN_COARSE_EXPECTED_SOURCES.items():
        path = paths[role]
        if not path.is_file() or path.stat().st_size > 100000 or sha(path) != digest:
            raise ValueError('Unexpected R688 source identity: ' + role)
        records[role] = dict(path=str(path), sha256=digest, bytes=path.stat().st_size)
    frame = load('R688_complete_original_coarse_frame', paths['coarse_frame'])
    moments = load('R688_complete_current_mean_coarse_moments', paths['mean_coarse'])
    centered = None
    if args.centered_loss_source is not None:
        paths['centered_loss'] = args.centered_loss_source.resolve()
        if sha(paths['centered_loss']) != MEAN_CENTERED_SOURCE_SHA:
            raise ValueError('The optional centered statistic source differs from R687')
        centered = load('R688_optional_R687_centered_statistics', paths['centered_loss'])
        records['centered_loss'] = dict(path=str(paths['centered_loss']), sha256=MEAN_CENTERED_SOURCE_SHA, bytes=paths['centered_loss'].stat().st_size)
    selected = 'centered_phi_normalized' if centered is not None else 'phi_normalized'
    return (frame, moments, centered, selected, dict(schema='R688-current-mean-coarse-face-PCG-source-binding-v1', source_records=records, mean_moment_stage_block=args.coarse_moment_stage_block, all_mean_normalization_derivatives_retained=True, material_weight_chain_retained_in_full_J=True, coarse_zero_core_contract_checked_by_bound_source=True, no_old_target_Gram_used=True, selected_scalar_objective_key=selected, same_Phi_up_to_fixed_constant=centered is not None, original_phi_normalized_field_retained=True, true_gradient_Hessian_and_damping_units_unchanged=True, near_zero_unit_rescaling_used=False, small_SPD_or_declared_coarse_layout_unavailable='Explicit original full-mean v3 solve before any PCG iteration', within_PCG_application_failure='Truthful v5 truncated status; no automatic retry or metric replacement', expected_extra_J_calls=0, actual_extra_J_calls_not_yet_measured=True))

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

def event(**values):
    print(json.dumps(values), flush=True)

def point_geometry(problem, x, amplitude, prepared):
    """Actual common-quintic six jets at every declared observation angle."""
    p = prepared
    maximum = -1.0
    where = None
    minimum_area = float('inf')
    maximum_radius = 0.0
    radius_where = None
    for stage in range(problem.P):
        z = problem.six_jets(p, stage)
        amplitude.add_grid(stage,z['F'])
        radius = np.linalg.norm(z['F'], axis=1)
        kr = int(np.argmax(radius))
        if radius[kr] > maximum_radius:
            maximum_radius = float(radius[kr])
            radius_where = dict(stage=stage, s=float(problem.times[stage]), phi=float(problem.phi[kr]))
        V, d = (z['Fs'], z['Fphi'])
        normal = np.cross(V, d)
        area = np.linalg.norm(normal, axis=1)
        minimum_area = min(minimum_area, float(area.min()))
        if not np.isfinite(area).all() or np.any(area <= 0):
            return dict(complete=False, first_invalid_stage=stage, min_area=minimum_area)
        normal /= area[:, None]
        E = np.sum(V * V, axis=1)
        F = np.sum(V * d, axis=1)
        G = np.sum(d * d, axis=1)
        e = np.sum(z['Fss'] * normal, axis=1)
        f = np.sum(z['Fsphi'] * normal, axis=1)
        g = np.sum(z['Fphiphi'] * normal, axis=1)
        determinant = area * area
        trace = (e * G + g * E - 2 * f * F) / determinant
        gauss = (e * g - f * f) / determinant
        k = (np.abs(trace) + np.sqrt(np.maximum(0.0, trace * trace - 4 * gauss))) / 2
        if not np.isfinite(k).all():
            return dict(complete=False,first_invalid_stage=stage,min_area=minimum_area,reason='Nonfinite actual principal curvature')
        loc = int(np.argmax(k))
        if k[loc] > maximum:
            maximum = float(k[loc])
            where = dict(stage=stage, s=float(problem.times[stage]), phi=float(problem.phi[loc]))
    return dict(complete=True, maximum_absolute_principal_curvature=maximum, closed_body_diameter_point_lower=2 * maximum_radius, maximum_radius_point=radius_where, diameter_scope='Reflected closed body with pi symmetry and the declared axial phase family; D0 lower bound from actual +/-F point pairs, not a replacement by current Ft diameter', worst=where, min_area=minimum_area, evaluated_points=problem.P * problem.N, original_full_orbit_points=problem.P * getattr(problem, 'full_N', problem.N), scope='All declared original and Gauss observations, augmented by separately recorded actual point witnesses; no continuous maximum or reach certificate')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--bundle', type=Path, required=True)
    parser.add_argument('--outdir', type=Path, required=True)
    parser.add_argument('--operator', type=Path)
    parser.add_argument('--implementation', type=Path, required=True)
    parser.add_argument('--basis-source', type=Path)
    parser.add_argument('--coarse-source', type=Path)
    parser.add_argument('--helpers', type=Path)
    parser.add_argument('--coordinate-source', type=Path)
    parser.add_argument('--scale-source', type=Path)
    parser.add_argument('--geometry-source', type=Path)
    parser.add_argument('--geometry-observed-source', type=Path, required=True)
    parser.add_argument('--observations', type=Path, required=True)
    parser.add_argument('--exact-tail-source', type=Path, required=True)
    parser.add_argument('--tail-node-report', type=Path, required=True)
    parser.add_argument('--tail-scalar-input', type=Path, required=True)
    parser.add_argument('--tail-scalar-source', type=Path, required=True)
    parser.add_argument('--tail-integer-source', type=Path, required=True)
    parser.add_argument('--tail-hold-source', type=Path, required=True)
    parser.add_argument('--tail-eta-start-node', type=int, required=True)
    parser.add_argument('--tail-lambda', type=float, required=True)
    parser.add_argument('--tail-parent-lambda', type=float)
    parser.add_argument('--tail-migration', choices=('keep-q', 'nodal-projection'), required=True)
    parser.add_argument('--base-batch-source', type=Path)
    parser.add_argument('--legacy-fraction', type=float, default=0.5)
    parser.add_argument('--point-source', type=Path)
    parser.add_argument('--height-source', type=Path)
    parser.add_argument('--angular-source', type=Path)
    parser.add_argument('--angular-transition', type=float, default=24.0)
    parser.add_argument('--qp-source', type=Path)
    parser.add_argument('--inequality-source', type=Path)
    parser.add_argument('--mean-transform-source', type=Path, required=True)
    parser.add_argument('--mean-averaging', choices=('material', 'physical'), required=True)
    parser.add_argument('--objective', choices=('jw', 'spectral'), default='spectral')
    parser.add_argument('--spectral-source', type=Path)
    parser.add_argument('--spectral-hessian-source', type=Path)
    parser.add_argument('--spectral-p', type=int, default=4)
    parser.add_argument('--spectral-epsilon', type=float, default=0.001)
    parser.add_argument('--spectral-scale', type=float, default=0.05)
    parser.add_argument('--qp-atol', type=float, default=1e-12)
    parser.add_argument('--qp-rtol', type=float, default=1e-06)
    parser.add_argument('--qp-feasibility-tolerance', type=float, default=2e-11)
    parser.add_argument('--qp-row-rank-tolerance', type=float, default=2e-12)
    parser.add_argument('--witness-input', type=Path, action='append', required=True)
    parser.add_argument('--radius-witness-input', type=Path, action='append', required=True)
    parser.add_argument('--active-band', type=float, default=0.025)
    parser.add_argument('--active-max-rows', type=int, default=192)
    parser.add_argument('--active-block-columns', type=int, default=32768)
    parser.add_argument('--active-rank-tolerance', type=float, default=1e-10)
    parser.add_argument('--active-top-curvature', type=int, default=16)
    parser.add_argument('--active-top-radius', type=int, default=2)
    parser.add_argument('--angles', type=int, default=2048)
    parser.add_argument('--stage-block', type=int, default=64)
    parser.add_argument('--low-modes', type=int, default=3)
    parser.add_argument('--coarse-centers', type=str)
    parser.add_argument('--curvature-cap', type=float)
    parser.add_argument('--reach-ratio', type=float)
    parser.add_argument('--reach-safety-factor', type=float, default=0.99)
    parser.add_argument('--max-directions', type=int, default=8)
    parser.add_argument('--maxiter', type=int, default=256)
    parser.add_argument('--damping', type=float, default=0.01)
    parser.add_argument('--line-trials', type=int, default=15)
    parser.add_argument('--target', type=float, default=5e-07)
    parser.add_argument('--mean-coarse-source', type=Path, required=True)
    parser.add_argument('--coarse-frame-source', type=Path, required=True)
    parser.add_argument('--coarse-v3-source', type=Path, required=True)
    parser.add_argument('--coarse-moment-stage-block', type=int, default=8)
    parser.add_argument('--centered-loss-source', type=Path)
    parser.add_argument('--amplitude-rows-source',type=Path,required=True)
    parser.add_argument('--amplitude-screen-source',type=Path,required=True)
    parser.add_argument('--marked-diameter-budget',type=float,required=True)
    parser.add_argument('--witness-lower-budget',type=float,required=True)
    parser.add_argument('--amplitude-height-floor',type=float,required=True)
    parser.add_argument('--amplitude-top-radius',type=int,default=2)
    parser.add_argument('--amplitude-top-distance',type=int,default=4)
    parser.add_argument('--amplitude-active-band',type=float,default=.025)
    parser.add_argument('--amplitude-budget-evidence',type=Path)
    args = parser.parse_args()
    if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public':
        raise SystemExit('Scientific R684 mean-metric design runs only in Rogerhu12/math-research-public GitHub Actions.')
    repo = args.repo.resolve()
    topic = repo / 'topics/visible-flex-larger-amplitude'
    original_sources = topic / 'scripts/resume_20261120'
    source_commit = subprocess.check_output(['git', '-C', str(repo), 'rev-parse', 'HEAD'], text=True).strip()
    args.bundle = args.bundle.resolve()
    args.outdir = args.outdir.resolve()
    paths = dict(operator=args.operator or topic / 'notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py', implementation=args.implementation or topic / 'scripts/resume_20261120_batched_closed_gram.py', basis=args.basis_source or topic / 'scripts/resume_20261120_physical_subspace.py', coarse=args.coarse_source or topic / 'scripts/resume_20261120_physical_subspace_v2.py', helpers=args.helpers or original_sources / 'fullclosed_lm.py', coordinates=args.coordinate_source or topic / 'notes/2026-11-17-parallel-root-fullclosed-integrated-coordinates.py', scale=args.scale_source or topic / 'scripts/integrated_l2_scale_20261120.py', geometry=args.geometry_source or topic / 'scripts/resume_20261120_curvature_qp.py', point=args.point_source or original_sources / 'fullclosed_point_cotangent_working.py', observed_geometry=args.geometry_observed_source, base_batch=args.base_batch_source or topic / 'scripts/resume_20261120_batched_closed_gram.py', height=args.height_source or original_sources / 'physical_height_coordinates.py', angular=args.angular_source or original_sources / 'angular_h2_coordinates.py', qp=args.qp_source or original_sources / 'fullspace_feasible_active_cg_v3.py', inequalities=args.inequality_source or original_sources / 'fullclosed_point_inequalities_v2.py', mean_transform=args.mean_transform_source, exact_tail=args.exact_tail_source, tail_scalar=args.tail_scalar_source, tail_integer=args.tail_integer_source, tail_hold=args.tail_hold_source)
    if args.objective == 'spectral':
        if args.spectral_source is None or args.spectral_hessian_source is None:
            raise ValueError('The spectral target needs both explicit frozen sources')
        paths.update(spectral=args.spectral_source, spectral_hessian=args.spectral_hessian_source)
    paths = {key: path.resolve() for key, path in paths.items()}
    paths.update(amplitude_rows=args.amplitude_rows_source.resolve(),
        amplitude_screen=args.amplitude_screen_source.resolve())
    amplitude_expected=dict(amplitude_rows='d06920f34b566cf6ccc4ebd0dace1a08463bee8b3f95f8b1933cdf22c15fa154',
        amplitude_screen='d9cd7ef55a92526a7cf7d9ed4a90a964fb0915713562f550cfcbe3970125d64f')
    for role,digest in amplitude_expected.items():
        if sha(paths[role])!=digest:raise ValueError('Changed complete amplitude source: '+role)
    amplitude_rows_module=load('complete_original_free_amplitude_rows',paths['amplitude_rows'])
    amplitude_screen_module=load('complete_sampled_amplitude_screen',paths['amplitude_screen'])
    if min(args.amplitude_top_radius,args.amplitude_top_distance)<1 or not np.isfinite(args.amplitude_active_band) or args.amplitude_active_band<=0:
        raise ValueError('Use positive declared amplitude working-row limits and active band')
    amplitude_evidence=(None if args.amplitude_budget_evidence is None else
        dict(path=str(args.amplitude_budget_evidence.resolve()),sha256=sha(args.amplitude_budget_evidence),
            scope='Explicit budget-selection evidence provenance, not an automatically inherited certificate'))
    mean_frame_module, mean_moments_module, centered_loss_module, mean_objective_key, mean_coarse_binding = _mean_coarse_sources(args, paths)
    if args.max_directions < 1 or args.maxiter < 1 or args.line_trials < 1 or (args.damping <= 0) or (args.target <= 0):
        raise ValueError('Invalid declared full-space numerical parameters')
    if args.curvature_cap is not None and args.curvature_cap <= 0:
        raise ValueError('A requested sampled curvature cap must be positive')
    if not 0 < args.legacy_fraction < 1:
        raise ValueError('Every original and added radial row needs positive quadrature weight')
    if args.reach_ratio is None:
        raise ValueError('This active-geometry experiment requires an explicit reach ratio')
    if not 0 < args.active_band < args.reach_safety_factor or args.active_max_rows < 1 or (not 0 < args.active_rank_tolerance < 1):
        raise ValueError('Invalid declared tangent-row selection or numerical rank cutoff')
    if args.reach_ratio is not None and args.reach_ratio <= 0:
        raise ValueError('A requested reach ratio must be positive')
    if not 0 <= args.tail_lambda <= 1 or args.tail_eta_start_node < 1:
        raise ValueError('Need a declared tail lambda in [0,1] and an interior eta start node')
    if args.tail_parent_lambda is not None and (not 0 <= args.tail_parent_lambda <= 1):
        raise ValueError('The explicit source-model lambda must lie in [0,1]')
    if not 0 < args.reach_safety_factor < 1:
        raise ValueError('The numerical reach-screening safety factor must lie between zero and one')
    centers = None if args.coarse_centers is None else [float(t) for t in args.coarse_centers.split(',')]
    if centers is not None and (not centers or not np.isfinite(centers).all()):
        raise ValueError('Coarse centers must be a finite nonempty list')
    if args.outdir.exists():
        raise FileExistsError('Choose a new output directory; do not overwrite a prior numerical budget')
    args.outdir.mkdir(parents=True)
    helper = load('integrated_h2_full_gram_helpers', paths['helpers'])
    implementation = load('integrated_h2_full_gram_implementation', paths['implementation'])
    coarse_module = load('integrated_h2_full_gram_coarse', paths['coarse'])
    geometry_module = load('full_free_active_geometry', paths['geometry'])
    point_module = load('full_free_point_cotangent', paths['point'])
    height_module = load('complete_physical_height_coordinates', paths['height'])
    angular_module = load('complete_angular_h2_coordinates', paths['angular'])
    qp_module = load('complete_feasible_active_set_cg', paths['qp'])
    inequality_module = load('complete_actual_margin_geometry_rows', paths['inequalities'])
    spectral_module = None
    spectral_hessian = None
    spectral_parameters = None
    if args.objective == 'spectral':
        spectral_module = load('complete_positive_spectral_objective', paths['spectral'])
        spectral_hessian = load('complete_positive_spectral_residual_hessian', paths['spectral_hessian'])
        spectral_parameters = spectral_module.Parameters(p=args.spectral_p, epsilon=args.spectral_epsilon, scale=args.spectral_scale)
    base_batch = load('observed_full_free_base_batch', paths['base_batch'])
    exact_tail = load('complete_reference_tail_context', paths['exact_tail'])
    mean_module = load('complete_mean_metric_transform', paths['mean_transform'])
    args.observations = args.observations.resolve()

    def load_witnesses(paths, kind):
        points = []
        sources = []
        for witness_path in paths:
            witness_path = witness_path.resolve()
            payload = json.loads(witness_path.read_text())
            if payload.get('carrier_sha256', sha(args.observations)) != sha(args.observations):
                raise ValueError('A supplied witness belongs to a different scalar carrier')
            manifest_key = 'curvature_points' if kind == 'curvature' else 'radius_points'
            if manifest_key in payload:
                protected = {tuple(v) for v in payload.get('protected_curvature_points', [])}
                values = [dict(cell=v[0], u=v[1], phi=v[2], protected=kind == 'curvature' and tuple(v) in protected) for v in payload[manifest_key]]
            elif 'searches' in payload:
                values = [search['final'] for search in payload['searches'] if search['kind'] == kind]
            else:
                values = [payload['final']] if 'final' in payload else payload['witnesses']
            locations = [dict(**{k: value[k] for k in ('cell', 'u', 'phi')}, protected=bool(value.get('protected', False))) for value in values]
            points.extend(locations)
            sources.append(dict(path=str(witness_path), sha256=sha(witness_path), original_bundle_sha256=payload.get('bundle_sha256'), locations=locations, kind=kind))
        seen = {}
        unique = []
        for value in points:
            key = (int(value['cell']), float(value['u']).hex(), float(value['phi']).hex())
            if key not in seen:
                seen[key] = len(unique)
                unique.append(value)
            elif value.get('protected', False):
                unique[seen[key]]['protected'] = True
        return (unique, sources)
    witnesses, witness_sources = load_witnesses(args.witness_input, 'curvature')
    radius_witnesses, radius_sources = load_witnesses(args.radius_witness_input, 'diameter')
    if not witnesses or not radius_witnesses:
        raise ValueError('Need both actual curvature and actual radius witness locations')
    data = np.load(args.bundle, allow_pickle=False)
    M = (data['qjets'].shape[-1] - 2) // 3
    tagged_parent_lambda = float(data['reference_tail_lambda']) if 'reference_tail_lambda' in data.files else float(data['exact_tail_lambda']) if 'exact_tail_lambda' in data.files else 0.0
    if 'reference_tail_lambda' in data.files and 'exact_tail_lambda' in data.files and (float(data['reference_tail_lambda']) != float(data['exact_tail_lambda'])):
        raise ValueError('Conflicting canonical and supplemental tail-lambda bundle tags')
    parent_lambda = tagged_parent_lambda if args.tail_parent_lambda is None else args.tail_parent_lambda
    if parent_lambda != tagged_parent_lambda:
        raise ValueError('The declared parent lambda disagrees with the actual bundle model tag')
    if parent_lambda != 0 and 'exact_tail_eta_start_node' in data.files and (int(data['exact_tail_eta_start_node']) != args.tail_eta_start_node):
        raise ValueError('A nonzero-lambda seed with another eta needs an explicit profile-to-profile migration')
    context = exact_tail.TailLiftContext.from_files(bundle=args.bundle, carrier=args.observations, node_report=args.tail_node_report.resolve(), scalar_input=args.tail_scalar_input.resolve(), scalar_source=paths['tail_scalar'], integer_source=paths['tail_integer'], hold_source=paths['tail_hold'], observed_source=paths['implementation'], eta_start_node=args.tail_eta_start_node, lambda_value=args.tail_lambda)
    problem, native = context.create_pair(paths['operator'], base_batch, N=args.angles, stage_block=args.stage_block, quarter=True)
    point_module = exact_tail.point_adapter(point_module)
    geometry_module.fields_block = exact_tail.fields_block_observed
    tail_profile_path = args.outdir / 'exact-tail-lift-profiles.npz'
    tail_profile_json = args.outdir / 'exact-tail-lift-profiles.json'
    tail_profile_record = context.save_carrier(tail_profile_path, tail_profile_json)
    x, parent_coordinate_check = problem.pack(data['qjets'], float(data['Hcap']), require_affine=True)
    x, migration = context.transfer_seed(problem, x, source_lambda=parent_lambda, mode=args.tail_migration)
    affine = problem.affine_diagnostics(x)
    terminal_stage = 2 * (problem.J - 1)
    terminal_lift = problem.lift_scalar[terminal_stage]
    affine.update(terminal_node_stage=terminal_stage, lift_terminal_radial_three_jets=terminal_lift[3:6].tolist(), lift_terminal_height_multiplier_three_jets=terminal_lift[:3].tolist(), lift_terminal_fixed_height_three_jets=problem.lift_scalar9[terminal_stage, 6:].tolist() if hasattr(problem, 'lift_scalar9') else [0.0, 0.0, 0.0])
    field_problem = problem
    problem = mean_module.MeanMetricOperator(field_problem, averaging=args.mean_averaging)
    amplitude_budgets=amplitude_rows_module.Budgets(
        args.marked_diameter_budget,args.witness_lower_budget,float(problem.R),args.amplitude_height_floor)
    amplitude_point_source=amplitude_rows_module.validate_point_source(point_module)
    options = dict(low_modes=args.low_modes)
    if centers is not None:
        options['desired_centers'] = centers
    basis = coarse_module.make_space(paths['basis'], native, **options)
    coordinate_module = load('h2_full_gram_coordinates', paths['coordinates'])
    scale_module = load('h2_full_gram_scale', paths['scale'])
    norm_scale, angular_metadata = angular_module.make_scale(problem, scale_module, height_module, args.angular_transition)
    coordinates = coordinate_module.DoubleIntegrated(problem, scale=norm_scale)
    height_map = height_module.PhysicalHeight(coordinates, basis)
    if not np.isfinite(norm_scale).all() or not np.all(norm_scale > 0):
        raise ValueError('The declared complete H2-type scale must be finite and positive')
    coarse_diagonal, coarse_chol, coarse_metadata = angular_module.coarse_norm(basis, coordinates, height_map, args.angular_transition)

    def coarse_lift(v):
        coefficients = solve_triangular(coarse_chol.T, v, lower=False) / coarse_diagonal
        return basis.free_direction(coefficients)

    def coarse_transpose(g):
        return solve_triangular(coarse_chol, basis.transpose_free(g) / coarse_diagonal, lower=True)

    def lift(v):
        return height_map.lift(v[:coordinates.size]) + coarse_lift(v[coordinates.size:])

    def transpose(g):
        return np.r_[height_map.pullback(g), coarse_transpose(g)]
    full_N = getattr(problem, 'full_N', problem.N)
    stage_weights = problem.mixed_stage_weights(args.legacy_fraction)
    if not np.all(stage_weights > 0):
        raise ValueError('Some retained or added radial rows have no positive objective weight')
    radial_mass = float(np.sum(stage_weights))
    normalizer = radial_mass * full_N
    weight = np.sqrt(stage_weights)[:, None, None] * np.array([1.0, np.sqrt(2), 1.0])[None, None, :] / np.sqrt(normalizer)

    def statistics(point, error, state):
        result = helper.statistics(problem, point, error)
        old = state.raw
        old_e, old_f, old_d = (old[..., 0], old[..., 1], old[..., 2])
        old_max = np.max((np.abs(old_e + old_d) + np.sqrt((old_e - old_d) ** 2 + 4 * old_f * old_f)) / 2)
        result.update(metric_target_mode='moving rotational mean metric DESIGN', final_metric_frozen=False, mean_averaging=args.mean_averaging, target_radial_E_min=float(np.min(state.radial)), target_radial_E_max=float(np.max(state.radial)), target_azimuthal_C_over_original_a2_min=float(np.min(state.angular)), target_azimuthal_C_over_original_a2_max=float(np.max(state.angular)), old_fixed_metric_max_diagnostic=float(old_max), old_fixed_metric_diagnostic_is_the_optimized_target=False)
        cost = np.sum(error[:, :, 0] ** 2 + 2 * error[:, :, 1] ** 2 + error[:, :, 2] ** 2, axis=1)
        weighted = float(stage_weights @ cost)
        result.update(all_raw_frobenius_sse=float(cost.sum()), legacy_raw_frobenius_sse=float(cost[:problem.legacy_P].sum()), radial_weighted_frobenius_sse=weighted, radial_weighted_mean_sse=weighted / normalizer)
        old = error[:problem.legacy_P] / problem.sqrt_multiplicity[None, :, None]
        e, f, g = (old[..., 0], old[..., 1], old[..., 2])
        result['legacy_max_relative_gram'] = float(np.max((np.abs(e + g) + np.sqrt((e - g) ** 2 + 4 * f * f)) / 2))
        if spectral_module is not None:
            raw = problem.unweight(error).reshape(problem.P, problem.N, 3)
            result['spectral'] = spectral_module.statistics(raw, stage_weights, problem.multiplicity, spectral_parameters)
            if centered_loss_module is not None:
                result['spectral'] = centered_loss_module.augment_statistics(raw, stage_weights, problem.multiplicity, spectral_parameters, result['spectral'], stage_block=args.stage_block)
        return result

    def objective_value(stats):
        return stats['spectral'][mean_objective_key] if args.objective == 'spectral' else stats['radial_weighted_mean_sse']
    shape = (problem.P, problem.N, 3)
    n = problem.free_size
    ni = coordinates.size
    nc = int(basis.dimension)
    physical_height_metadata = height_map.metadata()
    physical_height_metadata.pop('physical_equations_changed', None)
    physical_height_metadata.update(actual_column='Literal nodal B_H=(q_Z=b-h_lambda,H=1), using native._lift_scalar from the same R671 context', native_and_observed_height_profile_identical=True, h_piecewise_quintic_on_original_mesh=True, original_bending_normalization_retained=True, original_free_coordinates_preserved=True, coordinate_map_scope='Invertible direction map within the unchanged R671 h/f/k physical representation; every original physical variable remains. The mean-metric design target explicitly changes')
    report = dict(schema='complete-mean-design-with-held-amplitude-budgets-v1', source_commit=source_commit, workflow_trigger_commit=os.environ.get('GITHUB_SHA'), github_run_id=os.environ.get('GITHUB_RUN_ID'), mean_metric_design=dict(averaging=args.mean_averaging, finite_angles=full_N, orbit_multiplicities='exact physical reflection/pi orbit counts', mean_weights='m*rho/sum(m*rho)' if args.mean_averaging == 'material' else 'fixed m/sum(m)', material_Haar_quadrature=args.mean_averaging == 'material', mean_cross_component='exact full-circle zero by reflection parity; every actual cross row is retained', target='Ebar_x(s) ds^2+Cbar_x(s) dtheta^2', target_evaluated_from_current_field_at_every_trial=True, all_mean_normalization_derivatives_included=True, material_rho_weight_derivative_included=args.mean_averaging == 'material', complete_wrapper_J_and_transpose_used=True, old_angular_moment_preconditioner_used=False, old_fixed_metric_preserved=False, final_metric_frozen=False, design_stage_only=True, fixed_metric_refinement_evidence=False), initial_permanent_position_counts=dict(curvature=len(witnesses), radius=len(radius_witnesses)), permanent_position_identity='cell and exact binary64 u/phi; no decimal rounding or arbitrary byte cap', source_sha256=sha(__file__), source_paths={k: str(v) for k, v in paths.items()}, source_sha256_by_role={k: sha(v) for k, v in paths.items()}, diameter_diagnostic_source=str(Path(__file__).resolve()), diameter_diagnostic_sha256=sha(__file__), diameter_diagnostic_scope='This driver point_geometry uses the context-owned six_jets including k; the old standalone field reader is not used', bundle_sha256=sha(args.bundle), input_bundle=str(args.bundle), exact_tail_context=context.metadata(), required_operator_factory='TailLiftContext.create_pair', factory_context_required=True, scientific_model='Unchanged q+f_lambda*er(Theta)+(h_lambda*H+k_lambda)*ez. Original a*rho is only an intermediate Gram normalization; objective residual is relative to the current declared rotational mean metric', exact_tail_lambda=args.tail_lambda, exact_tail_parent_lambda=parent_lambda, exact_tail_eta_start_node=args.tail_eta_start_node, exact_tail_migration=migration, parent_coordinate_check=parent_coordinate_check, affine_diagnostic_scope='Actual migrated q/H coordinates and new context-owned core/cap lift jets', old_field_acceptance_inherited=False, old_continuous_certificates_inherited=False, parent_scope='Actual q/H coordinates from the named parent; changing lambda or projecting nodal seed is a new field read below', exact_tail_profile_carrier=str(tail_profile_path), exact_tail_profile_carrier_sha256=sha(tail_profile_path), exact_tail_profile_manifest=str(tail_profile_json), exact_tail_profile_manifest_sha256=sha(tail_profile_json), exact_tail_profile_output=tail_profile_record, exact_tail_node_report=str(args.tail_node_report.resolve()), exact_tail_node_report_sha256=sha(args.tail_node_report), exact_tail_scalar_input=str(args.tail_scalar_input.resolve()), exact_tail_scalar_input_sha256=sha(args.tail_scalar_input), recorded_compatibility_source_roles_not_loaded=['observed_geometry'], M=M, N=full_N, J=problem.J, original_variables=n, coarse_variables=nc, integrated_variables=ni, augmented_variables=ni + nc, original_full_rows=3 * problem.legacy_P * full_N, all_full_rows=3 * problem.P * full_N, observation_metadata=problem.observation_metadata(), observation_carrier=str(args.observations), observation_carrier_sha256=sha(args.observations), radial_weights=dict(legacy_fraction=args.legacy_fraction, quadrature_mass=radial_mass, minimum=float(stage_weights.min()), maximum=float(stage_weights.max()), all_positive=True, formula='mixed_stage_weights(t)=t*legacy_composite_Simpson+(1-t)*additional_Gauss', row_formula='sqrt(w_s)/(sqrt(sum(w_s)*full_N))*(1,sqrt(2),1); angular orbit weight already in operator'), coarse_basis_scope='The original node/midpoint structural layout with the new context-owned native h/f/k profiles builds B/B^T; every objective and geometric read uses the new observed field', evaluated_orbit_rows=3 * problem.P * problem.N, affine=affine, minimum_mesh_cell=float(np.min(np.diff(problem.mesh))), maximum_mesh_cell=float(np.max(np.diff(problem.mesh))), coordinate_map='T(zi,zc)=A DoubleIntegrated.lift(zi)+B R zc; A=I+vq e_H^T is invertible and retains every original variable', adjoint_map='T^T(g)=(DoubleIntegrated.pullback(A^T g),R^T B^T g)', objective=args.objective, quadratic_model='.5*||A z+v||^2+.5*mu^2||z||^2 subject to literal C z<=b; virtual RHS norm need not equal the actual objective', spectral_model='When spectral: A=sqrt(k/(scale^2*C0))*sqrt(radial)*B*J_mean*T, with complete mean/density/normalization chain in J_mean; B is the exact positive residual-Hessian factor at the NEW residual, and v uses B^{-T} primitive_gradient. No old angular moments or frozen-old-g residual are substituted', projection_scope='Only current active inequalities define a temporary CG face. Inactive rows retain positive margins; negative face multipliers release rows. Every original field variable remains', numerical_linear_safety=args.reach_safety_factor, extra_linear_margin=0.0, phase_I_restoration_implemented=False, active_band=args.active_band, active_max_rows=args.active_max_rows, active_block_columns=args.active_block_columns, active_rank_tolerance=args.active_rank_tolerance, active_top_curvature=args.active_top_curvature, active_top_radius=args.active_top_radius, step_norm_note='The previous physical-height norm is strengthened per mode by sigma=sqrt(1+(nu/nu_c)^2) on all A/E/D/core coordinates; H is unchanged. Coarse whitening uses this same new norm. This is not the original LM norm or an exact geometric bending energy', scale_formula='Previous physical-height A/E/D/core scales divided by sigma=sqrt(1+(nu/nu_c)^2); H unchanged', angular_norm=angular_metadata, coordinate_preparation=coordinates.metadata(), coarse_norm=coarse_metadata, physical_height_map=physical_height_metadata, arbitrary_witness_sources=witness_sources, arbitrary_radius_sources=radius_sources, witness_memory_policy='All supplied and subsequently found locations remain in every true line search; no LRU eviction. Bounded working inequalities keep actual positive margins; protected only means selected, never forced tangent', coarse_low_modes=args.low_modes, requested_coarse_centers=centers, actual_coarse_center_nodes=basis.center_nodes, sampled_curvature_cap=args.curvature_cap, requested_reach_ratio=args.reach_ratio, numerical_reach_safety_factor=args.reach_safety_factor, necessary_reference_diameter_lower_bound='max(2,2*abs(H),2*max_sample|F|); actual body +/-F pairs under pi symmetry plus mirror, inherited by the declared axial phase family', curvature_cap_scope='Additional numerical pointwise trial filter only. This is not a continuous curvature or reach certificate. The theorem uses D of the reference family member, not each current surface diameter', row_scope='Every original node/midpoint row plus every same-scalar Gauss row, all with positive radial weight and exact quarter-orbit multiplicity', objective_change='NEW moving rotational mean target with explicit averaging and spectral parameters. Only values with identical averaging/p/epsilon/scale/radial weights can be compared. This is not a decrease for old fixed g or a fixed-g refinement sequence', max_directions=args.max_directions, max_qp_hessian_advances=args.maxiter, initial_damping=args.damping, qp_atol=args.qp_atol, qp_rtol=args.qp_rtol, qp_feasibility_tolerance=args.qp_feasibility_tolerance, qp_row_rank_tolerance=args.qp_row_rank_tolerance, target=args.target, max_line_trials=args.line_trials, directions=[], continuous_geometry_certified=False, closed_isometry_accepted=False, mean_coarse_driver_derivation={'schema': 'R688-complete-mean-metric-face-PCG-driver-derivation-v1', 'base_driver_sha256': '2d44a097e614f917fa133b1042e0fc7c6cdcb32a10b72d1bc2ac6362d54a94c3', 'source_deriver_sha256': 'b57ab303682f708c6d205cf0d527df2ec16aa2cfa1762a59070599abcade6d75', 'expected_runtime_source_sha256': {'mean_coarse': '9e7ca6ba0cf3821ab8498226354d8422c2cfacee1ef07dafb8fc5868968fb9e3', 'coarse_frame': '324513a115a61800e105f340bd070eb50931bbe16dd66d3a8643bfe11298f2da', 'coarse_qp_v3': 'fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4', 'qp': '76b27520a433d85a52c3037ed5d519860b1002b0fb137378c855dad2993855e8', 'mean_transform': 'b7eb35d5e7c1d32baf8d4e94c0c9651d46d5cbfea65a6c1c098ae24d42f0b624', 'spectral_hessian': '29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4', 'spectral': 'e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91'}, 'optional_centered_statistics_sha256': '5e5798e3fd46535ef91db5171c885701caf23f3a17a47f28d4dad9e557ce2a01', 'whole_base_body_retained': True, 'current_mean_target_changed': False, 'original_free_variables_changed': False, 'physical_norm_or_geometry_rows_changed': False, 'optional_centered_loss_is_only_fixed_constant_subtraction': True, 'new_current_mean_coarse_Gram': True, 'face_metric': 'R685 constrained inverse', 'new_scientific_execution_by_deriver': False}, mean_coarse_source_binding=mean_coarse_binding, selected_scalar_objective_key=mean_objective_key)
    report['amplitude_design_constraints']=dict(
        schema='fixed-marked-diameter-and-held-witness-budget-v1',budgets=amplitude_budgets.metadata(),
        budget_selection_evidence=amplitude_evidence,point_source=amplitude_point_source,
        scalar_cap_and_height_rows_always_appended=True,
        original_geometry_working_row_cap_unchanged=args.active_max_rows,
        maximum_additional_point_rows=args.amplitude_top_radius+2*args.amplitude_top_distance,
        maximum_additional_rows_including_cap_and_height=args.amplitude_top_radius+2*args.amplitude_top_distance+2,
        all_original_rows_and_variables_and_mean_target_retained=True,
        every_potentially_accepted_trial_reads_all_current_grid_and_known_arbitrary_points=True,
        objective_rejected_trials_need_not_be_screened_or_claimed_feasible=True,
        both_witness_signs_kept=True,all_free_core_witness_derivatives_retained=True,
        budget_scope='Selected sufficient D/L certificate budgets, not all possible held-amplitude witnesses',
        full_continuous_amplitude_or_reach_certified=False,
        new_directional_fixture_automatically_run=False,
        squared_SOC_implemented=False,
        inherited_R688_base_driver_sha256='bf25c6d70b6ae4c92e08162b8c75969edcd301ba44d00554f8a55fc806f056bc')
    output = args.outdir / 'report.json'

    def save():
        report['process_peak_rss_KiB'] = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        report['process_memory_scope'] = 'Actual Linux process ru_maxrss in KiB, including row factorization and solve so far'
        output.write_text(json.dumps(report, indent=2) + '\n')

    def save_bundle(path, point):
        arrays = context.bundle_arrays(problem, point)
        arrays.update(field_representation=np.array('R671-exact-reference-tail-v1'), exact_tail_lambda=np.array(args.tail_lambda), exact_tail_eta_start_node=np.array(args.tail_eta_start_node, dtype=np.int64), exact_tail_source_sha256=np.array(sha(paths['exact_tail'])), exact_tail_profile_carrier_sha256=np.array(sha(tail_profile_path)), exact_tail_profile_manifest_sha256=np.array(sha(tail_profile_json)), exact_tail_scalar_input_sha256=np.array(sha(args.tail_scalar_input)))
        arrays.update(mean_metric_design_json=np.array(json.dumps(dict(schema='R684-moving-mean-target-design-v1', averaging=args.mean_averaging, finite_angles=full_N, mean_weights='m*rho/sum(m*rho)' if args.mean_averaging == 'material' else 'fixed m/sum(m)', final_metric_frozen=False, source_commit=source_commit, solver_sha256=sha(__file__), transform_sha256=sha(paths['mean_transform'])), sort_keys=True)))
        np.savez_compressed(path, **arrays)

    def curvature_filter(point, curvature):
        _, height, _ = problem.unpack(point)
        diameter_lower = max(2.0, 2 * abs(float(height)), curvature.get('closed_body_diameter_point_lower', 0.0))
        cap = args.curvature_cap
        if args.reach_ratio is not None:
            dynamic = args.reach_safety_factor / (args.reach_ratio * diameter_lower)
            cap = dynamic if cap is None else min(cap, dynamic)
        value = curvature.get('maximum_absolute_principal_curvature', float('inf'))
        passed = bool(curvature['complete'] and (cap is None or value <= cap))
        return dict(passed=passed, height=float(height), reference_diameter_lower_bound=diameter_lower, applied_curvature_cap=cap, sampled_curvature=value, necessary_reach_product=None if args.reach_ratio is None else args.reach_ratio * diameter_lower * value, scope='Necessary numerical point screen for the declared mirrored phase family only; no continuous reach certification')

    def geometry(point):
        prepared=problem.prepare(point)
        amplitude=amplitude_screen_module.Accumulator(problem,prepared,amplitude_rows_module,
            amplitude_budgets,top_radius=args.amplitude_top_radius,
            top_distance=args.amplitude_top_distance,active_band=args.amplitude_active_band)
        result=point_geometry(problem,point,amplitude,prepared)
        result['observation_grid_worst']=result.get('worst')
        result['observation_grid_maximum_curvature']=result.get('maximum_absolute_principal_curvature')
        result['arbitrary_witnesses']=[]
        result['amplitude_screen']=dict(complete=False,passed=False,reason='Full physical read not completed')
        if not result['complete']:return result
        for witness in witnesses+radius_witnesses:
            value=point_module.witness_geometry(problem,prepared,witness,geometry_module,implementation)
            result['arbitrary_witnesses'].append(value)
            if (not value['complete'] or not np.isfinite(value.get('principal_curvatures',[])).all()
                    or not np.isfinite(value.get('radius',float('nan')))):
                result['complete']=False
                result['actual_read_error']='Incomplete or nonfinite arbitrary physical geometry'
                return result
            fields=point_module.fields_at(problem,prepared,int(witness['cell']),
                float(witness['u']),float(witness['phi']),implementation)
            amplitude.add_arbitrary(witness,fields['F'])
            if value['maximum_absolute_principal_curvature']>result['maximum_absolute_principal_curvature']:
                result['maximum_absolute_principal_curvature']=value['maximum_absolute_principal_curvature']
                result['worst']=dict(kind='arbitrary_witness',**{k:value[k] for k in ('cell','u','phi','s')})
            if 2*value['radius']>result['closed_body_diameter_point_lower']:
                result['closed_body_diameter_point_lower']=2*value['radius']
                result['maximum_radius_point']=dict(kind='arbitrary_witness',**{k:value[k] for k in ('cell','u','phi','s')})
            result['min_area']=min(result['min_area'],value['area'])
        result['additional_witness_point_count']=len(witnesses)+len(radius_witnesses)
        result['amplitude_screen']=amplitude.finish(expected_arbitrary_locations=witnesses+radius_witnesses)
        result['memory_counts_at_complete_read']=dict(curvature=len(witnesses),radius=len(radius_witnesses))
        return result

    def add_actual_location(location, destination):
        if location is None:
            return None
        if 'stage' in location:
            stage = int(location['stage'])
            value = dict(cell=int(problem.observation_cells[stage]), u=float(problem.observation_u[stage]), phi=float(location['phi']))
        else:
            value = {key: location[key] for key in ('cell', 'u', 'phi')}
        key = (int(value['cell']), float(value['u']).hex(), float(value['phi']).hex())
        if any((key == (int(old['cell']), float(old['u']).hex(), float(old['phi']).hex()) for old in destination)):
            return None
        destination.append(value)
        return value

    def remember_amplitude(readout):
        new_curvature=[];new_radius=[]
        if readout is not None:
            screen=readout.get('amplitude_screen',{})
            for location in screen.get('newly_observed_extreme_and_selected_locations',[]):
                value=add_actual_location(location,witnesses)
                if value is not None:new_curvature.append(value)
                value=add_actual_location(location,radius_witnesses)
                if value is not None:new_radius.append(value)
            # These additions were actually read in this same full screen.
            if readout.get('complete') and screen.get('complete'):
                readout['memory_counts_at_complete_read']=dict(curvature=len(witnesses),radius=len(radius_witnesses))
        return dict(curvature=new_curvature,radius=new_radius,
            rule='Every new amplitude extreme/selected location retained exactly in both original permanent sets; future screens always read both distance signs')

    def compact_geometry(value):
        if value is None:
            return None
        compact = {key: item for key, item in value.items() if key != 'arbitrary_witnesses'}
        compact['arbitrary_witnesses_in_full_report'] = len(value.get('arbitrary_witnesses', []))
        return compact
    initial_state = problem._state(x)
    residual = initial_state.result * problem.sqrt_multiplicity[None, :, None]
    report['initial'] = statistics(x, residual, initial_state)
    del initial_state
    report['initial_curvature_points'] = geometry(x)
    report['initial_curvature_filter'] = curvature_filter(x, report['initial_curvature_points'])
    report['initial_amplitude_filter']=report['initial_curvature_points'].get('amplitude_screen',dict(passed=False))
    report['initial_new_permanent_amplitude_locations']=remember_amplitude(report['initial_curvature_points'])
    current_geometry=report['initial_curvature_points']
    save()
    event(event='mean_metric_design_initial', statistics=report['initial'], curvature_points=compact_geometry(report['initial_curvature_points']))
    damping = args.damping
    for index in range(args.max_directions):
        if not report['initial_curvature_filter']['passed']:
            report['stopped_before_linear_iteration'] = 'Initial point fails the declared necessary curvature filter; select an actually qualifying parent'
            break
        if not report['initial_amplitude_filter'].get('passed',False):
            report['stopped_before_linear_iteration']='Initial point fails the actual necessary D/L amplitude screen; this branch does not implement restoration or prove the true field globally infeasible'
            break
        current = report.get('current', report['initial'])
        if current['max_relative_gram'] <= args.target:
            break
        started = time.monotonic()
        known_counts=dict(curvature=len(witnesses),radius=len(radius_witnesses))
        if current_geometry.get('memory_counts_at_complete_read')!=known_counts:
            current_geometry=geometry(x)
            current_added=remember_amplitude(current_geometry)
        else:current_added=dict(curvature=[],radius=[])
        current_curvature_filter=curvature_filter(x,current_geometry)
        if (not current_curvature_filter['passed']
                or not current_geometry.get('amplitude_screen',{}).get('passed',False)):
            report['stopped_before_linear_iteration']='The current actual field fails the complete current curvature/amplitude memory read; no feasible-origin claim, global infeasibility proof or silent witness deletion'
            report['actual_current_curvature_read']=current_curvature_filter
            report['actual_current_amplitude_read']=current_geometry.get('amplitude_screen')
            save()
            break
        cache = problem.set_base(x)
        active_rows, active_bounds, active_metadata = inequality_module.build_inequality_rows(problem, x, geometry_module, point_module, transpose, ni + nc, reach_ratio=args.reach_ratio, safety=args.reach_safety_factor, active_band=args.active_band, max_rows=args.active_max_rows, top_curvature=args.active_top_curvature, top_radius=args.active_top_radius, witnesses=witnesses, radius_witnesses=radius_witnesses, observed_module=implementation, matrix_workdir=args.outdir / f'inequality-rows-{index:03d}', block_columns=args.active_block_columns)
        original_prefix_rows=len(active_bounds)
        original_prefix_cache_bytes=active_metadata['row_cache_bytes']
        active_rows,active_bounds,active_metadata=amplitude_rows_module.build_selected_rows(
            problem,x,point_module,implementation,transpose,ni+nc,budgets=amplitude_budgets,
            selections=current_geometry['amplitude_screen']['amplitude_row_selections'],
            matrix_workdir=args.outdir/f'all-geometry-amplitude-rows-{index:03d}',
            block_columns=args.active_block_columns,prefix=(active_rows,active_bounds,active_metadata))
        report['last_inequality_preparation']={key:active_metadata[key] for key in
            ('selected_rows','eligible_rows','protected_inequalities','row_cache_bytes','lazy_full_free_radius_covectors')}
        report['last_inequality_preparation'].update(original_prefix_rows=original_prefix_rows,
            original_prefix_cache_bytes=original_prefix_cache_bytes,
            total_scratch_row_cache_bytes=original_prefix_cache_bytes+active_metadata['row_cache_bytes'],
            appended_amplitude_rows=active_metadata['amplitude']['appended_rows'],
            no_original_row_removed=True)
        if index == 0:
            report['new_augmented_map_check'] = angular_module.new_map_check(problem, coordinates, lift, transpose, ni + nc)
            save()
        event(event='mean_metric_design_rows_ready', direction=index, rows=active_metadata['selected_rows'], minimum_bound=float(np.min(active_bounds, initial=0.0)), metadata=report['last_inequality_preparation'], peak_rss_KiB=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
        bridge = None
        counts = dict(jvp=0, vjp=0)
        if args.objective == 'spectral':
            bridge = spectral_hessian.NativeLinearization(problem, x, stage_weights, spectral_parameters, spectral_module=spectral_module)
            outer_factor = spectral_parameters.k / (spectral_parameters.scale ** 2 * normalizer)
            root_factor = np.sqrt(outer_factor)
            model_residual = root_factor * bridge.residual

            def matvec(v):
                counts['jvp'] += 1
                return root_factor * bridge.operator.matvec(lift(v))

            def rmatvec(v):
                counts['vjp'] += 1
                return root_factor * transpose(bridge.operator.rmatvec(v))
            model_metadata = dict(kind='positive_exact_new_mean_residual_Hessian_pullback', complete_mean_metric_chain_in_J_and_Jstar=True, bridge=bridge.metadata(), outer_half_hessian_factor=outer_factor, outer_square_root_factor=root_factor, virtual_rhs_squared_norm_is_actual_objective=False)
        else:
            model_residual = (residual * weight).ravel()

            def matvec(v):
                counts['jvp'] += 1
                return (problem.jvp(x, lift(v)) * weight).ravel()

            def rmatvec(v):
                counts['vjp'] += 1
                return transpose(problem.vjp(x, v.reshape(shape) * weight))
            model_metadata = dict(kind='new_mean_metric_radial_Frobenius_Gauss_Newton', complete_mean_metric_chain_in_J_and_Jstar=True, virtual_rhs_squared_norm_is_actual_objective=True)
        A = LinearOperator((model_residual.size, ni + nc), matvec=matvec, rmatvec=rmatvec, dtype=np.float64)

        def qp_progress(value):
            event(direction=index, **value)
        mean_parent_sha = next((item['accepted_bundle_sha256'] for item in reversed(report['directions']) if item.get('accepted') and item.get('accepted_bundle_sha256')), report['bundle_sha256'])
        mean_provenance = dict(direction=index, parent_bundle_sha256=mean_parent_sha, mean_averaging=args.mean_averaging, current_spectral_parameters=dict(p=spectral_parameters.p, epsilon=spectral_parameters.epsilon, scale=spectral_parameters.scale), selected_scalar_objective_key=mean_objective_key, whole_driver_derivation=report['mean_coarse_driver_derivation'])
        mean_outer_counts_before = counts.copy()
        mean_preconditioner, mean_preconditioner_detail = mean_moments_module.prepare_current_mean_preconditioner(mean_frame_module, coordinates, height_map, basis, coarse_diagonal, coarse_chol, bridge, damping, stage_block=args.coarse_moment_stage_block, provenance=mean_provenance, progress=lambda value: event(direction=index, **value))
        mean_preconditioner_detail['outer_A_entry_counts_during_preparation'] = {key: counts[key] - mean_outer_counts_before[key] for key in counts}
        mean_preconditioner_kwargs = dict(preconditioner=mean_preconditioner, preconditioner_metadata=mean_preconditioner_detail.get('fixed_metadata', mean_preconditioner_detail), v3_source=paths['coarse_qp_v3'])
        event(event='mean_metric_current_preconditioner_prepared', direction=index, status=mean_preconditioner_detail['status'], seconds=mean_preconditioner_detail['construction_seconds'], actual_operator_entry_calls=mean_preconditioner_detail['actual_operator_entry_calls'], fallback_to_v3=mean_preconditioner_detail.get('fallback_to_frozen_v3'))
        coordinate_step, qp_report = qp_module.solve(A, model_residual, active_rows, active_bounds, damping=damping, block_columns=args.active_block_columns, parameters=qp_module.Parameters(maxiter=args.maxiter, atol=args.qp_atol, rtol=args.qp_rtol, feasibility_tolerance=args.qp_feasibility_tolerance, rank_tolerance=args.qp_row_rank_tolerance), callback=qp_progress, **mean_preconditioner_kwargs)
        mean_preconditioner_detail['actual_QP_schema'] = qp_report.get('schema')
        mean_preconditioner_detail['actual_QP_status'] = qp_report.get('status')
        mean_preconditioner_detail['automatic_retry_or_changed_target'] = False
        mean_preconditioner_kwargs.clear()
        mean_preconditioner = None
        mean_preconditioner_detail['frame_and_factor_released_after_solve'] = True
        qp_operator_counts = counts.copy()
        step = lift(coordinate_step)
        djet, dheight, _ = problem.unpack(step, tangent=True)
        model_step = A.matvec(coordinate_step)
        old_merit = objective_value(current)
        slope = float(model_residual @ model_step)
        predicted_change = 2 * slope + float(model_step @ model_step)
        linear_merit = old_merit + predicted_change
        integrated_point = coordinates.scale * coordinates.project(coordinate_step[:ni])
        projected_endpoint_error = float(np.max(np.abs(coordinates.endpoint(integrated_point))))
        physical_linear_products=[];amplitude_linear_values=[];all_linear_inequalities=[]
        for row,value in zip(active_metadata['rows'],qp_report['normalized_row_values']):
            actual=row['current_product']+row['gradient_coordinate_norm']*value
            kind=row.get('constraint_kind','curvature_reach_product')
            all_linear_inequalities.append(dict(index=row['index'],kind=kind,linear_value=float(actual),
                upper_bound=0. if 'constraint_kind' in row else args.reach_safety_factor))
            (amplitude_linear_values if 'constraint_kind' in row else physical_linear_products).append(float(actual))
        record = dict(index=index, damping=damping, projected_endpoint_error=projected_endpoint_error, active_geometry=active_metadata, qp=qp_report, quadratic_model=model_metadata, maximum_selected_linear_product=float(max(physical_linear_products, default=0.0)), selected_linear_products=physical_linear_products, coordinate_norm=float(np.linalg.norm(coordinate_step)), initial_QP_point='z=0 checked feasible against actual margins; no additional linear margin or Phase-I claim', cache=cache, inner_counts=qp_operator_counts, outside_inner_calls=dict(postsolve_model_matvec=1, spectral_bridge_base_residual=int(args.objective == 'spectral'), spectral_bridge_base_vjp=int(args.objective == 'spectral')), old_merit=old_merit, half_objective_slope=slope, quadratic_predicted_actual_objective=linear_merit, quadratic_predicted_actual_change=predicted_change, virtual_rhs_squared_norm=float(model_residual @ model_residual), nodal_jet_step_max_by_Y_U_A=np.max(np.abs(djet), axis=(0, 2)).tolist(), height_step=float(dheight), accepted=False, trials=[], preparation_and_linear_seconds=time.monotonic() - started, mean_coarse_preconditioner=mean_preconditioner_detail)
        record.update(amplitude_current_screen=current_geometry['amplitude_screen'],
            current_newly_remembered_amplitude_locations=current_added,
            all_selected_linear_inequalities=all_linear_inequalities,
            selected_linear_amplitude_values=amplitude_linear_values,
            maximum_selected_linear_amplitude_value=max(amplitude_linear_values,default=None),
            original_geometry_rows_retained=original_prefix_rows,
            original_geometry_row_cache_bytes=original_prefix_cache_bytes,
            total_scratch_row_cache_bytes=original_prefix_cache_bytes+active_metadata['row_cache_bytes'],
            appended_amplitude_rows=active_metadata['amplitude']['appended_rows'],
            linear_product_alias_excludes_amplitude_g_values=True)
        checkpoint = args.outdir / f'direction-{index:03d}.npz'
        np.savez_compressed(checkpoint, step=step, augmented_step=coordinate_step, integrated_scale=coordinates.scale, coarse_diagonal=coarse_diagonal, coarse_cholesky=coarse_chol)
        record['direction_sha256'] = sha(checkpoint)
        del model_step, A, model_residual, djet, integrated_point, coordinate_step, active_rows, active_bounds
        event(event='mean_metric_design_direction_ready', direction=index, qp_status=qp_report['status'], advances=qp_report['advances'], old_merit=old_merit, predicted_merit=linear_merit, slope=slope, maximum_selected_linear_product=record['maximum_selected_linear_product'])
        alpha = 1.0
        for trial_index in range(args.line_trials):
            point = x + alpha * step
            error = None
            try:
                trial_state = problem._state(point)
                trial_residual = trial_state.result * problem.sqrt_multiplicity[None, :, None]
                finite = bool(np.isfinite(trial_residual).all())
                stats = statistics(point, trial_residual, trial_state) if finite else {}
                del trial_state
            except (FloatingPointError, OverflowError, ValueError) as exception:
                trial_residual = None
                finite = False
                stats = {}
                error = repr(exception)
            merit = objective_value(stats) if finite else float('inf')
            feasible = finite and stats['rho_sample_min'] > 0 and (stats['min_relative_E'] > 0) and (stats['min_relative_determinant'] > 0)
            descent = merit < old_merit and (slope >= 0 or merit <= old_merit + 0.0002 * alpha * slope)
            curvature = None
            curvature_feasible = True
            filter_result = None
            if feasible and descent and (args.curvature_cap is not None or args.reach_ratio is not None):
                try:
                    curvature=geometry(point)
                    filter_result=curvature_filter(point,curvature)
                except (FloatingPointError,OverflowError,ValueError) as exception:
                    curvature=dict(complete=False,amplitude_screen=dict(complete=False,passed=False),
                        actual_read_error=repr(exception))
                    filter_result=dict(passed=False,actual_read_error=repr(exception),
                        scope='Numerical trial read failure, not a global geometric infeasibility proof')
                curvature_feasible=filter_result['passed']
            amplitude_filter=None if curvature is None else curvature.get('amplitude_screen')
            amplitude_feasible=bool(amplitude_filter is not None and amplitude_filter.get('passed',False))
            trial = dict(index=trial_index, alpha=alpha, merit=merit, finite=finite, feasible=feasible, descent=descent, curvature_feasible=curvature_feasible, curvature_points=curvature, curvature_filter=filter_result, statistics=stats, arithmetic_error=error)
            trial.update(amplitude_filter=amplitude_filter,amplitude_feasible=amplitude_feasible,
                amplitude_not_read_reason=None if curvature is not None else 'Already rejected by objective/domain before any acceptance')
            if curvature is not None:
                trial['new_permanent_amplitude_locations']=remember_amplitude(curvature)
                remembered_curvature = []
                remembered_radius = []
                for location in (curvature.get('observation_grid_worst'), curvature.get('worst')):
                    value = add_actual_location(location, witnesses)
                    if value is not None:
                        remembered_curvature.append(value)
                value = add_actual_location(curvature.get('maximum_radius_point'), radius_witnesses)
                if value is not None:
                    remembered_radius.append(value)
                trial['new_permanent_curvature_locations'] = remembered_curvature
                trial['new_permanent_radius_locations'] = remembered_radius
                if curvature.get('complete') and curvature.get('amplitude_screen',{}).get('complete'):
                    curvature['memory_counts_at_complete_read']=dict(curvature=len(witnesses),radius=len(radius_witnesses))
            record['trials'].append(trial)
            event_trial = dict(trial)
            event_trial['curvature_points'] = compact_geometry(curvature)
            event(event='mean_metric_design_actual_trial', direction=index, **event_trial)
            if feasible and descent and curvature_feasible and amplitude_feasible:
                x = point
                residual = trial_residual
                record.update(accepted=True, accepted_alpha=alpha, new_merit=merit)
                report['current'] = stats
                current_geometry=curvature
                record['accepted_amplitude_filter']=amplitude_filter
                record['accepted_curvature_points'] = curvature if curvature is not None else geometry(x)
                record['accepted_curvature_filter'] = curvature_filter(x, record['accepted_curvature_points'])
                candidate = args.outdir / f'accepted-{index:03d}.npz'
                save_bundle(candidate, x)
                record.update(accepted_bundle=str(candidate), accepted_bundle_sha256=sha(candidate))
                predicted = old_merit - linear_merit
                ratio = (old_merit - merit) / predicted if predicted > 0 else None
                record['actual_to_full_step_predicted_decrease'] = ratio
                if alpha == 1 and ratio is not None and (ratio > 0.75):
                    damping = max(1e-08, damping / 2)
                break
            alpha /= 2
        if not record['accepted']:
            damping *= 4
        record['damping_after_direction'] = damping
        record['seconds'] = time.monotonic() - started
        report['directions'].append(record)
        save()
        problem.clear_base()
        del step, bridge
    report['final_curvature_memory'] = witnesses
    report['final_radius_memory'] = radius_witnesses
    report['final_permanent_position_counts'] = dict(curvature=len(witnesses), radius=len(radius_witnesses))
    report['final_damping'] = damping
    report['final_statistics'] = report.get('current', report['initial'])
    report['complete'] = True
    report['sample_target_reached'] = report.get('current', report['initial'])['max_relative_gram'] <= args.target
    report['sample_target'] = report['sample_target_reached']
    final_geometry = report['directions'][-1].get('accepted_curvature_points') if report['directions'] else None
    if final_geometry is None:
        final_geometry = geometry(x)
    final_known=dict(curvature=len(witnesses),radius=len(radius_witnesses))
    if final_geometry.get('memory_counts_at_complete_read')!=final_known:
        final_geometry=geometry(x)
    report['final_new_permanent_amplitude_locations']=remember_amplitude(final_geometry)
    report['final_curvature_filter'] = curvature_filter(x, final_geometry)
    report['final_amplitude_filter']=final_geometry.get('amplitude_screen',dict(passed=False))
    report['final_curvature_points']=final_geometry
    report['final_curvature_memory']=witnesses
    report['final_radius_memory']=radius_witnesses
    report['final_permanent_position_counts']=dict(curvature=len(witnesses),radius=len(radius_witnesses))
    report['actual_direction_count']=len(report['directions'])
    report['actual_accepted_direction_count']=sum(bool(record.get('accepted')) for record in report['directions'])
    report['exact_tail_context_final'] = context.metadata()
    report['limitations'] = 'NEW moving rotational mean target design on the unchanged R671 field. This does not optimize the old fixed metric and is not fixed-final-g refinement. All original/Gauss angular fluctuations and all cross rows remain, with finite sampled metric/curvature plus permanent arbitrary witnesses. No continuous metric maximum, reach, held/E3, all-t, exact closed isometry, or fixed-g mesh/frequency convergence certificate follows. After design, freeze an explicit continuous radial target formula and start a separate fixed-target refinement branch.'
    report['limitations']+=' Additional Dmarked/L/Hmin inequalities preserve only the selected necessary point budgets under the true all-known/grid trial screen; continuous amplitude, embedding, reach and Euclidean nontriviality still require same-field certificates. No original geometric row is removed and no squared SOC is implemented here.'
    final = args.outdir / 'final.npz'
    save_bundle(final, x)
    report.update(final_bundle=str(final), final_bundle_sha256=sha(final))
    save()
    event(event='mean_metric_design_numerical_batch_complete', report=str(output), final_bundle=str(final), sample_target=report['sample_target'], statistics=report.get('current', report['initial']))
if __name__ == '__main__':
    main()
