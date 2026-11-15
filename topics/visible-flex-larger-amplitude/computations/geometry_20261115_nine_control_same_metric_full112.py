#!/usr/bin/env python3
"""Independent all-nine-frozen same-metric M=T112 complete physical-DN entry.

Input is a genuine future accepted nine-control full112 field or an accepted
own-schema450 field, explicitly SHA-bound by the caller. No candidate, field,
nine coefficients, lambda or run is selected by this source. All nine final
scalar coefficients and both original finite evaluator paths are frozen.
K=k=0: physical338 plus all112 constant core rows gives450 unknowns, with
left338/right112 and no three low-core targets. Original complete RHS/J,
physical FD, same-owner native solves, full-band Newton, seventeen trials,
RMS/BC acceptance, final native fullJ and actual audit remain required.

The actual parent mesh is bisected and every literal scalar knot is included.
--max-nodes is required and checked against the real new mesh, so an old699
mesh can genuinely become1397 plus additional knots. Regenerable data stays
under RUNNER_TEMP. Scientific evaluation is public repository Actions only.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import traceback
import types

HERE = Path(__file__).resolve().parent
ENTRY = Path(__file__).name
SCHEMA = 'nine-control-all-frozen-same-metric450-complete-physical-DN-v1'
RECIPE_SCHEMA = 'explicit-nine-control-frozen-same-metric450-recipe-v1'
PARAMETER_ORDER = ['p1', 'p2', 'p3', 'theta1', 'theta2', 'theta3', 'eta1', 'eta2', 'eta3']
ACTIVE_INDICES = []
FROZEN_INDICES = list(range(9))
# Filled only from the actual frozen source bytes; not from numerical output.
PINS = {
    "geometry_20261114_banded_collocation.py": "0780dcc4e331f6cde64141b0fa9ebdd1325eec2af87d94fc455e72405a0524f1",
    "geometry_20261114_constrained_trust_warm.py": "5378b7d732dc768f154849a1138ea59a2571f1128cc507932d38d4f8bfb115f2",
    "geometry_20261114_fft_frenet.py": "973898fcea1e8706d0ff9f87bbe72cde3576bc0055149af0a2e2058b144ac401",
    "geometry_20261114_full_dn_augmented.py": "f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e",
    "geometry_20261114_full_dn_boundary.py": "4517274cc4e79a7264d5980e79bbd209d73761f86ae7b015a2fa5671cca35ca2",
    "geometry_20261114_full_dn_prefix_controls.py": "7bb30855e5f0f5111ef55bbf9fafad8f6f0e8cdc26243780eda5b96600a3255a",
    "geometry_20261114_full_dn_response.py": "38d21971b3b0d462f8cf1b8f0a1cd174a28db3dcba450e89d0d0baecc5e26e74",
    "geometry_20261114_full_dn_solve.py": "c6a1f4d8025508ee49fe9324b3401440a2de88329d0b78ef0d0814860c2d3162",
    "geometry_20261114_lifted_modes_banded_full_dn.py": "390387db4700f64302b76ee684f9a810a611c57c6617eb67d4597a9fa18905c4",
    "geometry_20261114_lifted_modes_full_dn.py": "d885ebc8de5ebd02f006c4104d8b67e856047b4e58f0e125651b38187fb251a5",
    "geometry_20261114_lifted_modes_prepare.py": "9a1ae018d71e38ff901c4b9156b23502a4efde44f812c1ff4e03323878b659db",
    "geometry_20261114_lifted_modes_profile.py": "13cd479d91590a6ce7a82e6461d6cd2c1561d7303264680621e9cbe438b7cee5",
    "geometry_20261114_physical_test_boundary.py": "3975eb0daf8941516962a46d33efef614aa1f9759a979165e7cc0f83a2838681",
    "geometry_20261114_physical_test_cut_audit.py": "7a548961ff0bd3e5171db18f1133d42f606be19e65e5d2e919432514042ba420",
    "geometry_20261114_physical_test_response.py": "83ce387778fb90209e841fc841a81ed3d99e15181d6e86210ec1244fde017e79",
    "geometry_20261114_projected_core_bvp.py": "2326720f124d2edc40e63089f8e07d6671e053ff108281efb59091d919f15c5b",
    "geometry_20261114_separated_qr_bvp.py": "c76bde190ff67a9e148d230c8e5e7d7a7899324c055e67faac6679b8fba10e39",
    "geometry_20261114_small_core_resonance.py": "3b9c45abed425a92be662c3547d088a3074ebcc5923c23ac2ef7aaf003124bd5",
    "geometry_20261115_small_core_four_control_family.py": "9222390b73abbd2e8bc4a1f8e9d8b861cd66b4a927b21629deb2e6b70073dd11",
    "geometry_20261115_small_core_six_control_family.py": "79464f9c6af8863d3c65254701a858f067881b22ca80dba24bacf2bfea484acf",
    "geometry_20261115_small_core_nine_control_family.py": "086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629",
    "geometry_20261115_nine_control_full112.py": "00e4d2c3413cfa6c1df915b9d85050bf375ab88c04e8756149d4ea0533ef3bd8",
    "geometry_20261115_nine_control_same_metric_profile.py": "070b9b35c3d31c5073cd7da5b7afbdaa1150a38a94861c70eea60a39f0c85647"
}


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as handle:
        for block in iter(lambda: handle.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('The complete scientific adapter may run only in public repository Actions')


def runtime():
    require_actions()
    for name, expected in PINS.items():
        if sha(HERE/name) != expected:
            raise ValueError('A frozen mathematical or explicit reconstruction source differs: '+name)
    import geometry_20261115_nine_control_full112 as full112
    import geometry_20261115_nine_control_same_metric_profile as frozen
    d = full112.runtime()
    d.full112, d.frozen = full112, frozen
    for name, expected in frozen.checked_sources().items():
        if name in d.closure and d.closure[name] != expected:
            raise ValueError('Two complete scalar-source responsibilities disagree: '+name)
        d.closure[name] = expected
    d.closure[ENTRY] = sha(__file__)
    d.FrozenFlow = frozen.frozen_flow_class(d)
    return d


def read_recipe(path, expected_sha):
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected_sha:
        raise ValueError('The actual explicit parent/refinement recipe bytes differ')
    value = json.loads(raw)
    if (value.get('schema') != RECIPE_SCHEMA
            or value.get('parameter_order') != PARAMETER_ORDER
            or value.get('active_parameter_indices') != ACTIVE_INDICES
            or value.get('frozen_parameter_indices') != FROZEN_INDICES
            or value.get('field_modes') != 112 or value.get('field_angular_quadrature') != 2048
            or value.get('initial_guess_kind') != 'complete-accepted-parent-physical338-core112'
            or value.get('mesh_refinement') != 'all-parent-nodes-plus-one-bisection-and-all-scalar-knots'):
        raise ValueError('Use the explicit all-nine-frozen450 parent and mesh contract')
    parent_sha = value.get('parent_sha256')
    if (not isinstance(parent_sha, str) or len(parent_sha) != 64
            or any(c not in '0123456789abcdef' for c in parent_sha)):
        raise ValueError('Supply the actual whole complete parent file SHA256')
    if any(name in value for name in ('lambda_target', 'initial_nine_parameters',
                                      'fixed_low_core_targets', 'target_core')):
        raise ValueError('No new scalar coefficients or three fixed core targets belong to this K=k=0 problem')
    return value, dict(file=path.name, bytes=len(raw), sha256=expected_sha,
        recipe_is_not_an_accepted_field_or_native_parent=True,
        coefficients_will_be_read_only_from_actual_complete_parent=True)


def temporary_paths(args):
    root = Path(os.environ['RUNNER_TEMP']).resolve()
    out, work = args.out.resolve(), args.work.resolve()
    if root not in out.parents or root not in work.parents:
        raise ValueError('Regenerable output and factors must remain under the actual RUNNER_TEMP')
    if out == work or out in work.parents or work in out.parents:
        raise ValueError('Keep complete-band temporary factors separate from result/FD temporaries')
    for path in (out, work):
        path.mkdir(parents=True, exist_ok=True)
        if any(path.iterdir()):
            raise ValueError('Use a fresh independent temporary directory: '+str(path))
    return out, work


class ResourceBudgetError(RuntimeError):
    """A declared node allowance cannot hold the real requested refinement."""


def curve_with_exact_nodes(d, mesh, values, rhs):
    curve = d.CubicHermiteSpline(mesh, values, rhs, axis=0)
    np = d.np

    def at(points):
        points = np.asarray(points)
        result = curve(points)
        index = np.searchsorted(mesh, points)
        safe = np.minimum(index, len(mesh)-1)
        saved = (index < len(mesh)) & (mesh[safe] == points)
        result[saved] = values[index[saved]]
        return result

    return at


def bound_original_preflight(d, output, writer):
    # The frozen helper calls original.preflight internally. Preserve that
    # exact preflight function even when core.main is given this full RMS layer.
    proxy = types.SimpleNamespace(preflight=d.core.preflight,
                                  original_solver=d.core.original_solver)
    globals_ = dict(d.preparation.complete_preflight.__globals__)
    globals_.update(original=proxy, write=writer)
    copied = types.FunctionType(d.preparation.complete_preflight.__code__, globals_,
        name='original_complete_RMS_preflight', argdefs=d.preparation.complete_preflight.__defaults__)

    def run(mesh, initial_at, flow, max_nodes):
        return copied(mesh, initial_at, flow, max_nodes, output)

    return run


def prepare_problem(d, args, recipe, inputs, output):
    np, core = d.np, d.core
    accepted = core.read(args.accepted)
    parent = core.read(args.parent)
    parent_receipt = dict(file=args.parent.name, bytes=args.parent.stat().st_size, sha256=inputs['parent'])
    if recipe['parent_sha256'] != inputs['parent']:
        raise ValueError('The whole complete parent is not the actual recipe input')
    view, parent_mesh, retained, parent_binding = d.frozen.freeze_parent(d, parent, parent_receipt, accepted)
    core.write(output/'frozen-nine-scalar.json', view.specification)
    core.write(output/'parent-source-binding.json', parent_binding)
    design_spec = view.specification['frozen_design_scalar_profile']['original_three_parameter_specification']
    full_p = view.frozen_parameters.copy()
    source_targets = np.asarray(accepted['core']['coefficients'], float)[:3]
    target = np.empty(0)
    original_targets = source_targets  # only verifies the unmodified core.main call site; never imposed
    core_seed = np.asarray(parent['core']['coefficients'], float).copy()
    law = accepted['original_metric_identity']['law']
    constructor = core.original_solver.native.outward.FullCoreProbe
    q = constructor(core_seed, 112, 2048, law['velocity'], law['length'], law['k0'])
    q.profile = view.profile
    core.original_solver.fixed.fft.enable_fft(q)
    flow = d.FrozenFlow(q, view, args.jac_workers)
    affine = core.AffineTail(112)
    parent_cut = parent['physical_test_final_cut_audit']
    if (parent_cut.get('schema') != 'actual-physical-test-complete-cut-audit-v1'
            or parent_cut.get('field_modes') != 112 or parent_cut.get('tail_modes') != 112
            or parent_cut.get('height_sign') not in (-1, 1) or parent_cut.get('radial_sign') not in (-1, 1)
            or parent_cut.get('original_material_angles') != args.material_angles
            or parent_cut.get('actual_physical_test_angles') != args.physical_angles):
        raise ValueError('Retain the actual parent physical orientation and original finite boundary rules')
    boundary = d.PhysicalTestBoundary(view, target, flow.point_rhs, flow.point_jacobian, affine,
        height_sign=parent_cut['height_sign'], radial_sign=parent_cut['radial_sign'],
        angular=args.material_angles, physical_angles=args.physical_angles)
    separated = d.SeparatedBoundary(boundary)
    if ((flow.dimension, flow.n, flow.M, flow.k) != (450, 338, 112, 0)
            or (boundary.K, boundary.k, boundary.left_count, separated.left_count, boundary.T) !=
               (0, 0, 226, 338, 112)):
        raise ValueError('The genuine all-core-free K=k=0 square dimensions differ')
    midpoint = (parent_mesh[:-1]+parent_mesh[1:])/2
    knots = np.asarray(view.knots, float)
    if (knots.ndim != 1 or not np.all(np.isfinite(knots))
            or np.any(knots < 0) or np.any(knots > view.end)):
        raise ValueError('Retain the actual complete original scalar knot list')
    mesh = np.unique(np.r_[parent_mesh, midpoint, knots])
    mesh_plan = dict(schema='all-parent-nodes-bisection-literal-knots450-v1',
        parent_nodes=len(parent_mesh), requested_parent_midpoints=len(midpoint),
        original_scalar_knot_entries=len(knots), actual_initial_refined_nodes=len(mesh),
        explicit_max_nodes=args.max_nodes, every_parent_node_retained=bool(np.all(np.isin(parent_mesh, mesh))),
        every_original_scalar_knot_retained=bool(np.all(np.isin(knots, mesh))),
        node_budget_can_hold_initial_mesh=bool(args.max_nodes >= len(mesh)),
        low_node_budget_is_a_resource_limit_not_nonexistence=True)
    core.write(output/'refinement-mesh-plan.json', mesh_plan)
    if args.max_nodes < len(mesh):
        raise ResourceBudgetError('The actual bisected parent plus literal knots exceeds --max-nodes')
    # All retained parent words are unchanged; the old variable-p RHS is not
    # relabelled. Re-evaluate the original finite field at the final frozen nine.
    parent_current_rhs = flow(parent_mesh, retained.T).T
    if not np.all(np.isfinite(parent_current_rhs)):
        raise FloatingPointError('The actual parent field fails the original nodal domain at its final frozen scalar')
    at = curve_with_exact_nodes(d, parent_mesh, retained, parent_current_rhs)
    preflight = bound_original_preflight(d, output, core.write)
    mesh, values, rhs, residual, additions = preflight(mesh, at, flow, args.max_nodes)
    specification = d.frozen.serialize(view, design_spec['complete_original_port'],
                                       np.empty(0), inputs['accepted'])
    guess = dict(kind=recipe['initial_guess_kind'], parent=parent_binding, mesh_refinement=mesh_plan,
        preflight_added_nodes=additions, actual_preflight_nodes=len(mesh),
        parent_acceptance_not_inherited_as_new_acceptance=True,
        retained_field_modes=112, retained_core_unknowns=112,
        fixed_low_core_targets=[], active_scalar_parameters=[],
        fresh_original_RHS_at_frozen_nine_before_interpolation=True,
        independent_original_RMS_preflight_preserved=True)
    record = dict(schema=SCHEMA, scope=__doc__, M=112, N=2048,
        mesh=mesh.tolist(), states=values.tolist(), rhs=rhs.tolist(),
        complete_scalar_profile=specification, field_representation=d.field_spec(112, 2048),
        state_layout='all physical338 then constant free core112; no scalar-control rows',
        initial_collocation_max=core.finite_max(residual), preflight_added_nodes=additions,
        initial_guess=guess, success=False, new_coupled_finite_acceptance=False,
        complete_closed_surface=False, true_nonzero_native_parent_claimed=False)
    return types.SimpleNamespace(**locals())


def actual_boundary_fd(d, problem, response, initial_height, output, binding, seed_path):
    """The original three perturbations, direction set and Richardson helper."""
    np, flow, boundary = d.np, problem.flow, problem.boundary
    problem.affine.set(initial_height, response)
    separated = d.SeparatedBoundary(boundary)
    ya, yb = problem.values[0].copy(), problem.values[-1].copy()
    yb[boundary.iz+1] += 1e-5
    yb[boundary.iz+32] += 1e-9
    yb[boundary.iz+flow.M] += 1e-10
    yb[flow.core_slice] = ya[1:flow.M+1]
    pa, pb, controls = ya[:flow.n].copy(), yb[:flow.n].copy(), yb[flow.parameter_slice].copy()
    direct_directions, augmented_directions = d.response.make_directions(flow, boundary)
    A, B, P = boundary.jacobian(pa, pb, controls)
    direct = d.refined_directional_check(
        lambda v, h: boundary(pa+h*v['ya'], pb+h*v['yb'], controls+h*v['p']),
        lambda v: A@v['ya']+B@v['yb']+P@v['p'], direct_directions)
    AA, BB = separated.jacobian(ya, yb)
    augmented = d.refined_directional_check(
        lambda v, h: separated(ya+h*v['ya'], yb+h*v['yb']),
        lambda v: AA@v['ya']+BB@v['yb'], augmented_directions)
    augmented.update(right_rows_depend_only_on_right_endpoint=True,
        left_right_jacobian_offblock_max=float(max(np.max(abs(AA[separated.left_count:])),
                                                  np.max(abs(BB[:separated.left_count])))))
    groups = (direct, augmented)
    coarse = max(v['relative_error'] for g in groups for item in g['directions'] for v in item['levels'])
    worst = max(v['relative_error'] for g in groups for item in g['directions'] for v in item['fourth_order_levels'])
    contracts = all(g['second_order_truncation_contracts'] for g in groups)
    passed = bool(np.isfinite(worst) and worst <= 5e-5 and contracts)
    record = dict(schema=SCHEMA, physical_test_schema=d.PHYSICAL_SCHEMA,
        direct_boundary=direct, separated_boundary=augmented,
        maximum_relative_directional_error=worst, maximum_second_order_relative_directional_error=coarse,
        maximum_fourth_order_relative_directional_error=worst,
        verification_threshold=5e-5, verification_estimator='two fourth-order Richardson levels',
        second_order_truncation_contracts=contracts, implementation_check_passed=passed,
        physical_test=boundary.description(), nine_control_same_metric450_implementation=binding,
        prepared_sha256=sha(seed_path), native_anchor_response_sha256=sha(output/'initial-actual-H-tail.json.gz'),
        native_anchor_height=initial_height.tolist(), actual_current_H_solved_before_this_FD=True,
        FD_perturbed_states_use_explicit_affine_map=True,
        zero_anchor_J_not_relabelled_as_current_H_J=True,
        original_three_perturbations_steps_and_threshold_unchanged=True,
        original_direction_constructor_with_actual_k0_used=True,
        frozen_scalar_control_directions_are_absent_not_projected=True,
        same_live_client_will_be_retained_if_FD_passes=passed,
        full_BVP_solved=False, full_Cartesian_closed_surface=False)
    d.core.write(output/'response-check.json', d.response.clean(record))
    return passed, record


class SharedNativeClient:
    """One genuine client owner, including original full-DN final audit/close."""
    def __init__(self, client):
        self.client, self.closed, self.calls = client, False, []
        self.close_attempted, self.close_exception = False, None

    def __getattr__(self, name):
        return getattr(self.client, name)

    def solve(self, height, *, jacobian, audit):
        if self.close_attempted:
            raise RuntimeError('The original live native owner has already begun closing')
        self.calls.append(dict(jacobian=bool(jacobian), audit=bool(audit), completed=False))
        result = self.client.solve(height, jacobian=jacobian, audit=audit)
        if (result.get('actual_nonlinear_solve') is not True or result.get('converged') is not True
                or result.get('failed', False)
                or result.get('checkpoint', {}).get('cutHeight') != [float(v) for v in height]):
            raise ValueError('The actual complete tail protocol did not return the current requested H')
        self.calls[-1]['completed'] = True
        return result

    def close(self):
        if not self.close_attempted:
            self.close_attempted = True
            try:
                self.client.close()
                self.closed = True
            except Exception as error:
                self.close_exception = repr(error)
                raise


@contextmanager
def restore_attributes():
    saved = []
    def replace(obj, name, value):
        saved.append((obj, name, getattr(obj, name)))
        setattr(obj, name, value)
    def preserve(obj, name):
        saved.append((obj, name, getattr(obj, name)))
    try:
        yield replace, preserve
    finally:
        for obj, name, value in reversed(saved):
            setattr(obj, name, value)


def original_full_solve(d, args, problem, binding, seed_path, port_path, output, owner):
    """Keep the original complete-band and core main bodies unmodified."""
    np, core, continuation = d.np, d.core, d.banded.continuation
    plain_write, previous_seam = core.write, core.final_height_seam
    context = dict(boundary=None, cut_audit=None, statistics_active_parameters=None)
    final_preflight = bound_original_preflight(d, output, plain_write)
    prepared_at = curve_with_exact_nodes(d, problem.mesh, problem.values, problem.rhs)
    original_band_write = d.banded.write

    def band_write(path, data, *positional, **keywords):
        if isinstance(data, dict) and Path(path).name == 'complete-banded-intent.json':
            data.update(mathematical_BC_changed=True, equation_row_permutation_only=False,
                linear_backend_is_only_row_permutation_of_current_physical_test=True,
                all_nine_scalar_coefficients_frozen_by_independent_adapter=True,
                fixed_core_targets_removed_K0_and_empty_active_k0=True,
                nine_control_same_metric450_implementation=binding,
                actual_native_client_source_sha256=args.expected_tail_client_sha256,
                native_tail_math_configuration_unchanged=True)
            data.pop('native_tail_changed', None)
        return original_band_write(path, data, *positional, **keywords)

    def scalar_spec(profile, port, active, accepted_sha):
        if profile is not problem.view or accepted_sha != binding['input_sha256']['accepted']:
            raise ValueError('The complete already-frozen nine-control scalar owner/source changed')
        return d.frozen.serialize(profile, port, active, accepted_sha)

    def make_profile(source, port, peak, source_modes):
        if (source_modes != 96 or peak != problem.design_spec['peak_curvature']
                or port != problem.design_spec['complete_original_port']):
            raise ValueError('The original source scalar/physical port identity changed')
        return problem.view

    def constructor(core_values, M, N, velocity, length, k0):
        if (M, N) != (96, 1024) or not np.array_equal(core_values, problem.accepted['core']['coefficients']):
            raise ValueError('The genuine accepted96 source was reclassified')
        law = problem.accepted['original_metric_identity']['law']
        if (velocity, length, k0) != (law['velocity'], law['length'], law['k0']):
            raise ValueError('The original physical source law changed')
        return problem.q

    def boundary(profile, old_target, rhs, jacobian, affine, *, angular):
        if (profile is not problem.view or angular != args.material_angles
                or not np.array_equal(old_target, problem.original_targets)):
            raise ValueError('Bind the unmodified source call before explicitly removing every fixed core target')
        result = d.PhysicalTestBoundary(profile, problem.target, rhs, jacobian, affine,
            height_sign=problem.boundary.eh, radial_sign=problem.boundary.er,
            angular=angular, physical_angles=args.physical_angles)
        context['boundary'] = result
        return result

    def initial_guess(source, profile, flow, extension_step, taper_fraction):
        if profile is not problem.view or flow.dimension != 450:
            raise ValueError('The complete initial guess layout/scalar changed')
        return problem.mesh.copy(), prepared_at, dict(problem.guess,
            actual_preflight_warm_sha256=sha(seed_path), source_accepted_prefix_not_reclassified=True)

    def load_client(module_path, config, sources, prefix, heap):
        if (Path(module_path).resolve() != args.tail_client.resolve()
                or Path(config).resolve() != args.tail_config.resolve()
                or Path(sources).resolve() != args.tail_source_root.resolve()
                or Path(prefix).resolve() != (output/'true-tail').resolve()
                or heap != args.node_heap):
            raise ValueError('The original full-DN call must retain the exact actual-H FD client owner')
        return owner

    def final_seam(boundary_, flow, q, endpoint, actual):
        result = previous_seam(boundary_, flow, q, endpoint, actual)
        active = np.array(endpoint[flow.parameter_slice], copy=True)
        context['statistics_active_parameters'] = active
        q.profile = lambda s: flow.profile.profile(s, active)
        cut = d.audit_cut(boundary_, flow, endpoint, actual,
                          angular_levels=(args.material_angles, 2*args.material_angles))
        context['cut_audit'] = cut
        plain_write(output/'physical-test-final-cut-audit.json', cut)
        result.update(old_material_test_not_the_acceptance_gate=True,
            finite_boundary_scheme='physical-phi-complete-DN-v1',
            physical_test_final_cut_audit_file='physical-test-final-cut-audit.json',
            physical_test_final_cut_audit_sha256=sha(output/'physical-test-final-cut-audit.json'))
        return result

    def write(path, data):
        if isinstance(data, dict):
            name = Path(path).name
            if name in ('driver-status.json', 'prepared.json.gz', 'actual.json.gz') or name.endswith('-pending.json.gz'):
                data.update(schema=SCHEMA, scope=__doc__, source_sha256=sha(__file__),
                    unchanged_full_DN_core_source_sha256=PINS['geometry_20261114_full_dn_solve.py'],
                    field_representation=d.field_spec(112, 2048),
                    finite_boundary_scheme='physical-phi-complete-DN-v1',
                    nine_control_same_metric450_implementation=binding,
                    active_parameter_indices=ACTIVE_INDICES, frozen_parameter_indices=FROZEN_INDICES,
                    fixed_modes=0, active_scalar_parameters=0, physical_state_dimension=338,
                    state_dimension=450, left_rows=338, right_rows=112,
                    canonical_scalar_identity_sha256=problem.view.canonical_scalar_identity_sha256,
                    no_fixed_low_core_targets=True,
                    parent_design_acceptance_not_inherited_as_new_acceptance=True)
                if 'complete_scalar_profile' in data:
                    data['complete_nine_scalar_parameters'] = data['complete_scalar_profile']['frozen_design_parameters']
            if name == 'actual.json.gz':
                if context['cut_audit'] is None or context['statistics_active_parameters'] is None:
                    raise RuntimeError('Keep the original physical-test cut measurement and frozen-p statistics')
                data['original_source_metric_identity'] = data.pop('original_metric_identity')
                data['original_metric_identity'] = dict(schema='frozen-nine-same-material-metric-v1',
                    scalar_specification=data['complete_scalar_profile'],
                    canonical_scalar_identity_sha256=problem.view.canonical_scalar_identity_sha256,
                    core_coefficients=data['core']['coefficients'],
                    material_coordinate='common theta; ds^2+a(s;all nine frozen)^2*dtheta^2',
                    same_g_as_origin_nine_design=True, same_g_as_original_accepted96_claimed=False)
                data['sampled_geometry_scalar_parameters'] = context['statistics_active_parameters'].tolist()
                data['sampled_geometry_frozen_nine_parameters'] = problem.full_p.tolist()
                data['empty_active_drift_is_not_a_missing_scalar_coefficient'] = True
                data['physical_test_final_cut_audit'] = context['cut_audit']
                data['scope'] = __doc__
                data['message'] = 'New finite all-nine-frozen450 physical-phi DN accepted by the original complete gates; closed assembly remains open.'
                data['same_metric_refinement'] = True
            if name == 'driver-status.json' and data.get('new_coupled_finite_acceptance'):
                data['new_coupled_finite_acceptance_refers_to'] = SCHEMA
        return plain_write(path, data)

    def enter_core():
        # banded.main has installed this frozen closure, including the original
        # released_newton call and its read-only trial wrapper.
        continuation.install_qr_diagnostics(output, 112, plain_write)
        return core.main()

    old_argv = sys.argv
    argv = [ENTRY, '--accepted', str(args.accepted), '--port', str(port_path),
        '--out', str(output), '--work', str(args.work), '--warm', str(seed_path),
        '--tail-client', str(args.tail_client), '--tail-config', str(args.tail_config),
        '--tail-source-root', str(args.tail_source_root), '--peak-curvature',
        str(problem.design_spec['peak_curvature']),
        '--jac-workers', str(args.jac_workers), '--max-nodes', str(args.max_nodes),
        '--material-angles', str(args.material_angles), '--node-heap', str(args.node_heap),
        '--tol', '1e-6', '--outer-iterations', str(args.outer_iterations)]
    try:
        with restore_attributes() as (replace, preserve):
            for obj, name in ((continuation, 'install_qr_diagnostics'),
                    (core.original_solver, 'released_newton'), (core.original_solver, 'original_splu'),
                    (core.original_qr, 'enable'), (core.original_qr, 'DiskQRFactor'),
                    (d.backend, 'prepare_sys'), (d.backend, 'solve_newton')):
                preserve(obj, name)
            for name, value in (('scalar_spec', scalar_spec), ('CompleteProfile', make_profile),
                    ('AugmentedFlow', d.FrozenFlow),
                    ('FullDNBoundary', boundary), ('prepared_guess', initial_guess),
                    ('preflight', final_preflight), ('load_client', load_client),
                    ('final_height_seam', final_seam), ('write', write)):
                replace(core, name, value)
            replace(core.original_solver.native.outward, 'FullCoreProbe', constructor)
            replace(d.banded, 'write', band_write)
            replace(continuation, 'main', enter_core)
            sys.argv = argv
            return d.banded.main()
    finally:
        sys.argv = old_argv


def main():
    require_actions()
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('recipe', 'accepted', 'parent', 'tail-config', 'out', 'work'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--expected-recipe-sha256', required=True)
    parser.add_argument('--tail-client', type=Path)
    parser.add_argument('--expected-tail-client-sha256')
    parser.add_argument('--tail-source-root', type=Path)
    parser.add_argument('--prepare-only', action='store_true')
    parser.add_argument('--jac-workers', type=int, default=2)
    parser.add_argument('--max-nodes', type=int, required=True)
    parser.add_argument('--material-angles', type=int, default=4096)
    parser.add_argument('--physical-angles', type=int, default=4096)
    parser.add_argument('--node-heap', type=int, default=1536)
    parser.add_argument('--outer-iterations', type=int, default=8)
    args = parser.parse_args()
    recipe, recipe_identity = read_recipe(args.recipe, args.expected_recipe_sha256)
    if args.max_nodes < 2:
        raise ValueError('Supply the actual allowed full-mesh node resource budget')
    if not args.prepare_only and any(x is None for x in (
            args.tail_client, args.expected_tail_client_sha256, args.tail_source_root)):
        raise ValueError('A real complete live tail implementation and its actual source SHA are required')
    d = runtime()
    inputs = {name: sha(getattr(args, name)) for name in ('accepted', 'tail_config', 'parent')}
    expected = {name: d.family.EXPECTED[name] for name in ('accepted', 'tail_config')}
    if ({name: inputs[name] for name in expected} != expected
            or recipe.get('source_input_sha256') != expected
            or recipe['parent_sha256'] != inputs['parent']):
        raise ValueError('Keep the exact actually consumed original source inputs and complete parent')
    out, work = temporary_paths(args)
    owner = None
    session = dict(schema=SCHEMA, phase='preparing', success=False,
        new_coupled_finite_acceptance=False, full_Cartesian_closed_surface=False,
        recipe=recipe_identity, input_sha256=inputs, consumed_source_sha256=d.closure,
        no_future_accepted_field_parameters_lambda_or_run_selected_by_source=True)
    d.core.write(out/'adapter-status.json', session)
    try:
        seed_dir, fd_dir, full_dir = out/'initial-guess', out/'actual-H-response', out/'full-DN'
        for path in (seed_dir, fd_dir, full_dir):
            path.mkdir()
        problem = prepare_problem(d, args, recipe, inputs, seed_dir)
        binding = dict(schema=SCHEMA, source_sha256=sha(__file__), consumed_source_sha256=d.closure,
            input_sha256=inputs, recipe=recipe_identity,
            source_accepted_prefix=dict(M=96, N=1024, sha256=inputs['accepted']),
            source_parent=problem.parent_binding,
            ancestral_original_four_input_sha256={name: d.family.EXPECTED[name]
                for name in ('accepted','prepared','tail_anchor','tail_config')},
            ancestral_prepared_and_zero_anchor_payloads_not_loaded_by_this_entry=True,
            frozen_scalar_schema=d.frozen.SCHEMA,
            frozen_scalar_specification_canonical_sha256=d.frozen.canonical_sha(problem.view.specification),
            canonical_scalar_identity_sha256=problem.view.canonical_scalar_identity_sha256,
            frozen_nine_parameters=problem.full_p.tolist(),
            frozen_nine_float64le=d.frozen.words(problem.full_p.tolist()),
            scalar_support_float64le=problem.view.specification['scalar_support_float64le'],
            finite_scalar_assembly=problem.view.specification['finite_assembly'],
            source_three_targets_only_provenance=problem.original_targets.tolist(),
            current_fixed_low_core_targets=[], current_active_scalar_parameters=[],
            active_parameter_indices=ACTIVE_INDICES, frozen_parameter_indices=FROZEN_INDICES,
            parameter_order=PARAMETER_ORDER, state_dimension=450, physical_state_dimension=338,
            field_modes=112, tail_modes=112, core_unknowns=112, free_core_unknowns=112,
            left_rows=338, right_rows=112, all_native_slope_columns_and_rows_retained=True,
            old_scalar_schema_or_failed_native_source_relabelled=False,
            same_g_450_refers_to_exact_final_nine_scalar_of_bound_design=True,
            same_g_as_original_accepted96_claimed=False,
            true_current_H_native_and_full_J_required=True, boundary_schema=d.PHYSICAL_SCHEMA,
            explicitly_selected_native_client_file=None if args.tail_client is None else args.tail_client.name,
            explicitly_selected_native_client_sha256=args.expected_tail_client_sha256,
            native_client_execution_requested=not args.prepare_only,
            original_complete_FD_threshold=5e-5, original_inner_trial_count=17,
            original_collocation_and_frozen_RMS_tolerance=1e-6, original_BC_tolerance=1e-11,
            true_final_native_full_J_and_audit_required=True,
            low_mode_or_high_mode_proof_not_an_added_numerical_gate=True,
            new_continuous_scalar_domain_C2_Fourier_seam_reach_certificate=False,
            mesh_refinement=problem.mesh_plan, explicit_max_nodes=args.max_nodes,
            regenerable_raw_is_temporary_only=True)
        problem.record['nine_control_same_metric450_implementation'] = binding
        seed_path = seed_dir/'prepared.json.gz'
        d.core.write(seed_path, problem.record)
        port_path = seed_dir/'original-port.json'
        d.core.write(port_path, problem.design_spec['complete_original_port'])
        session.update(phase='prepared-unaccepted-same-metric450-field', implementation=binding,
            prepared_sha256=sha(seed_path), initial_collocation_max=problem.record['initial_collocation_max'])
        d.core.write(out/'adapter-status.json', session)
        if args.prepare_only:
            print(json.dumps(dict(event='nine-frozen450-prepared-only', schema=SCHEMA,
                canonical_scalar_identity_sha256=problem.view.canonical_scalar_identity_sha256,
                prepared_sha256=sha(seed_path), success=False, native_called=False),
                allow_nan=False), flush=True)
            return 0
        if sha(args.tail_client) != args.expected_tail_client_sha256:
            raise ValueError('The explicitly selected live native source identity differs')
        config = d.core.read(args.tail_config)
        if (int(config['modes']), int(config['spacing'])) != (112, 2):
            raise ValueError('The complete actual tail must retain112 even material modes')
        for name, expected_value in problem.design_spec['complete_original_port']['parameters'].items():
            if config.get(name) != expected_value:
                raise ValueError('The actual original physical tail parameter differs: '+name)
        owner = SharedNativeClient(d.core.load_client(args.tail_client, args.tail_config,
            args.tail_source_root, full_dir/'true-tail', args.node_heap))
        for name in ('radius', 'E', 'Ep', 'backgroundSlope', 'backgroundSecond'):
            if not d.np.isclose(float(owner.cut[name]), float(problem.view.cut[name]), rtol=2e-11, atol=2e-13):
                raise ValueError('The actual live native cut differs: '+name)
        H = d.core.true_height(problem.boundary, problem.values[-1])
        actual = owner.solve(H, jacobian=True, audit=False)
        if (actual.get('actual_nonlinear_solve') is not True or actual.get('converged') is not True
                or actual.get('failed', False)
                or not d.np.array_equal(d.np.asarray(actual['checkpoint']['cutHeight']), H)):
            raise ValueError('Only a truly completed current-H response can anchor the original FD')
        d.core.write(fd_dir/'initial-actual-H-tail.json.gz', actual)
        passed, report = actual_boundary_fd(d, problem, actual, H, fd_dir, binding, seed_path)
        session.update(phase='actual-current-H-FD-completed', actual_current_H=H.tolist(),
            response_check_sha256=sha(fd_dir/'response-check.json'), original_boundary_FD_passed=passed,
            maximum_boundary_FD_relative_error=report['maximum_relative_directional_error'],
            actual_tail_client_source_sha256=args.expected_tail_client_sha256)
        d.core.write(out/'adapter-status.json', d.response.clean(session))
        if not passed:
            return 2
        status = original_full_solve(d, args, problem, binding, seed_path, port_path, full_dir, owner)
        final = d.core.read(full_dir/'driver-status.json')
        session.update(phase='original-full-DN-returned', original_full_DN_exit_status=status,
            original_full_DN_phase=final.get('phase'),
            new_coupled_finite_acceptance=final.get('new_coupled_finite_acceptance') is True,
            original_driver_status_sha256=sha(full_dir/'driver-status.json'))
        session['success'] = bool(status == 0 and session['new_coupled_finite_acceptance'])
        return status
    except ResourceBudgetError as error:
        session.update(phase='resource-budget-insufficient-for-refined-mesh', exception=repr(error),
            mathematical_nonexistence_or_native_failure_inferred=False)
        return 3
    except Exception as error:
        session.update(phase='exception', exception=repr(error), traceback=traceback.format_exc(),
            mathematical_nonexistence_or_global_failure_inferred=False)
        raise
    finally:
        if owner is not None:
            try:
                owner.close()
            except Exception as error:
                session['native_close_exception'] = repr(error)
            finally:
                session['native_live_calls'] = owner.calls
                session['native_owner_close_attempted'] = owner.close_attempted
                session['native_owner_closed'] = owner.closed
                session['native_owner_close_exception'] = owner.close_exception
        d.core.write(out/'adapter-status.json', d.response.clean(session))
        print(json.dumps(d.response.clean(dict(event='nine-frozen450-adapter-returned',
            schema=SCHEMA, phase=session['phase'], success=session['success'],
            new_coupled_finite_acceptance=session['new_coupled_finite_acceptance'],
            actual_parent_sha256=inputs['parent'],
            canonical_scalar_identity_sha256=session.get('implementation', {}).get('canonical_scalar_identity_sha256'),
            original_full_DN_phase=session.get('original_full_DN_phase'),
            maximum_boundary_FD_relative_error=session.get('maximum_boundary_FD_relative_error'),
            native_live_calls=session.get('native_live_calls'), exception=session.get('exception'),
            adapter_status_sha256=sha(out/'adapter-status.json'))), allow_nan=False), flush=True)


if __name__ == '__main__':
    raise SystemExit(main())
