#!/usr/bin/env python3
"""Independent six-control full112 adapter with same-worker current R273 H(s).

No scalar parameters, positive homotopy amplitude, native parent, or successful
field are supplied by this source. A future explicit recipe chooses lambda and
all six coefficients. Theta1/theta2/theta3 are held fixed; p1/p2/p3 remain the
three active design coordinates of the original square full problem.

This adapter constructs an unaccepted fresh circle/low-three initial guess or
reads its own complete-field continuation guess. It then requires the supplied
original live tail client to reach actual current H through a declared complete112
height path with a genuine zero request and actual endpoint J, then runs
the original complete physical-boundary FD, and invokes the unchanged original
full-DN main through the unchanged complete-band wrapper. All original field,
core and active-parameter rows, 17 inner trials, nonlinear tail updates, RMS/BC
and final native J/audit remain. No failed native source or circle is an anchor.
The native correction uses current full-system R273 eta1 and with-J uses
the separately declared original64 finite successful root-trace tangent.
The noJ primal, original cold/warm predictor algorithm, evaluate body, ten
noJ trials, guards and endpoint/final sensitivity/audit paths remain. The first confirmed positive-height refusal stops
this experiment instead of retrying progressively smaller heights.
Only public Actions may import scientific dependencies or execute this source.
All regenerable numerical output belongs to the caller's temporary workspace.
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
SCHEMA = 'six-control-finite-trace-r273-height-path-three-active-nonzero112-physical-DN-v1'
RECIPE_SCHEMA = 'explicit-six-control-finite-trace-r273-height-path-nonzero112-recipe-v1'
PARAMETER_ORDER = ['p1', 'p2', 'p3', 'theta1', 'theta2', 'theta3']
ACTIVE_INDICES = [0, 1, 2]
FROZEN_INDICES = [3, 4, 5]
# Filled only from the actual frozen source bytes; not from numerical output.
PINS = {
    "geometry_20261115_six_control_r273_height_full112.py": "d1f21025a91234252c856cb15bf26ce48e2628e8fa92352a9d98ffd53b14a69d",
    "geometry_20261115_original_r273_tail_client.py": "2fe2c25233061de0fd89b7af72cba5ddd2e2d144889492ec42156f781c4828a9",
    "geometry_20261115_original_r273_height_path.py": "73c62d94a60eb1ee2fd50d68c14d6af29c590729fcdb764c5c4036ca963305ed",
    "exact_20261115_original64_finite_trace_tail_base.py": "4f22690b9b72c8b2eaee919200b5329cd74342a9394ec8aaa49c0e8e10e18999",
    "geometry_20261115_finite_trace_r273_tail_client_hook.mjs": "53d614393600affd5e4778c4966b94de0cf3dde14883d4b9bb616e33d604e123",
    "exact_20261115_finite_trace_r273_current576_system.py": "e78b220aa620c45fbc6c4719915a89af61e8afeb3599b272575e999de374d27c",
    "exact_20261115_finite_trace_r273_current576_chain_qr.py": "c0997c9eee50ca96f2e50785251dec966cb5560a541dfc15c9fedd423911d309",
    "geometry_20261115_original64_finite_trace_loader.mjs": "55b2a4a344ae2eb7d78f26b7954b20f9cbe4e4969588bf3a236e7828d6f299ae",
    "geometry_20261115_original64_finite_trace_flow.mjs": "a7a90668a7d2f4df93e0bd03d665f439dab2fb2461bedf544725cd01c2a7b470",
    "geometry_20261115_original64_finite_trace_variation.mjs": "742ab15a2168084167eeab9879a074ee1cd586d33f324e837223134a8cbf9705",
    "geometry_20261115_six_control_height_continuation_full112.py": "557f3aab83116c1d8eef83e4c83306e8058749ccdb56b2ec8808effd2e16bf21",
    "geometry_20261115_finite_trace_r273_tail_client.py": "b5dd4d8171e1f7452eba036d0c6518b76176bcc4420ba84c4e8d7357a143a2c8",
    "geometry_20261115_six_control_full112.py": "807f6a35e0d66aee7a2f324e4573bd2b9e9be8feab1972e4b073aa8ee91ed7a2",
    "geometry_20261115_finite_trace_r273_height_path.py": "1194400acb9060e913e1fd8746b8fefa631b4e5cdd17c030564cafa1166d55af",
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
    "geometry_20261115_small_core_six_control_family.py": "79464f9c6af8863d3c65254701a858f067881b22ca80dba24bacf2bfea484acf"
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
            raise ValueError('A frozen mathematical source differs: '+name)
    for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
        os.environ[key] = '1'
    import numpy as np
    from scipy.interpolate import CubicHermiteSpline
    import scipy.integrate._bvp as backend
    import geometry_20261115_small_core_six_control_family as family
    import geometry_20261115_finite_trace_r273_height_path as height_path
    import geometry_20261114_full_dn_solve as core
    import geometry_20261114_lifted_modes_banded_full_dn as banded
    import geometry_20261114_lifted_modes_prepare as preparation
    import geometry_20261114_physical_test_response as response
    from geometry_20261114_full_dn_augmented import AugmentedFlow, SeparatedBoundary
    from geometry_20261114_physical_test_boundary import PhysicalTestBoundary, SCHEMA as PHYSICAL_SCHEMA
    from geometry_20261114_physical_test_cut_audit import audit_cut
    from geometry_20261114_lifted_modes_profile import field_spec
    from geometry_20261114_full_dn_response import refined_directional_check
    closure = dict(core.FROZEN_SOURCES)
    for table in (family.checked_sources(), PINS):
        for name, expected in table.items():
            if name in closure and closure[name] != expected:
                raise ValueError('Two source responsibilities disagree: '+name)
            if sha(HERE/name) != expected:
                raise ValueError('A consumed mathematical source differs: '+name)
            closure[name] = expected
    closure[ENTRY] = sha(__file__)
    return types.SimpleNamespace(**locals())


def read_recipe(path, expected_sha):
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected_sha:
        raise ValueError('The actual explicit parameter/target recipe bytes differ')
    value = json.loads(raw)
    if (value.get('schema') != RECIPE_SCHEMA
            or value.get('parameter_order') != PARAMETER_ORDER
            or value.get('active_parameter_indices') != ACTIVE_INDICES
            or value.get('frozen_parameter_indices') != FROZEN_INDICES):
        raise ValueError('Use the explicit six-coefficient and three-active coordinate contract')
    parameters = value.get('initial_six_parameters')
    if (not isinstance(parameters, list) or len(parameters) != 6
            or any(type(p) not in (int, float) or not math.isfinite(p) for p in parameters)):
        raise ValueError('Supply the six actual finite initial coefficients, without implicit defaults')
    lam = value.get('lambda_target')
    if type(lam) not in (int, float) or not math.isfinite(lam) or not 0 < lam <= 1:
        raise ValueError('The declared straight target path requires one explicit 0 < lambda <= 1')
    if value.get('initial_guess_kind') not in ('fresh-circle-low-three-linear', 'same-family-complete-field'):
        raise ValueError('State exactly which unaccepted initial guess is to be used')
    if value.get('field_modes') != 112 or value.get('field_angular_quadrature') != 2048:
        raise ValueError('Retain the entire original M112/N2048 physical field')
    if sha(HERE/'geometry_20261115_finite_trace_r273_height_path.py') != PINS['geometry_20261115_finite_trace_r273_height_path.py']:
        raise ValueError('The explicit height-path helper source differs')
    from geometry_20261115_finite_trace_r273_height_path import POLICY
    if value.get('height_continuation') != POLICY:
        raise ValueError('Declare the complete original height-path policy in the actual recipe')
    return value, dict(file=path.name, bytes=len(raw), sha256=expected_sha,
                       recipe_is_not_an_accepted_field_or_native_parent=True)


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


def active_profile(d, designed, odd):
    """Same exact six-control formula, with one declared finite assembly path."""
    np = d.np
    frozen = d.family.OddCoefficientsFrozenProfile(designed, odd)

    class ThreeActiveView:
        parameter_count = 3

        def __getattr__(self, name):
            return getattr(frozen, name)

        def base_jet(self, s):
            return frozen.base_jet(s)

        def control_jets(self, s):
            return frozen.control_jets(s)

        def profile(self, s, parameters=None):
            p = np.zeros(3) if parameters is None else np.asarray(parameters)
            if p.shape != (3,):
                raise ValueError('All three active p coordinates are required')
            jet = self.base_jet(s)+self.control_jets(s)@p
            if (not np.all(np.isfinite(jet)) or jet[0].real <= 0 or abs(jet[1].real) >= 1):
                raise FloatingPointError('The unchanged scalar domain a>0, |ap|<1 failed')
            return tuple(jet)

        def description(self):
            result = dict(designed.description())
            result.update(scope='Three-active square view of the actual six-control scalar; all three odd coefficients are fixed',
                adapter_schema=SCHEMA, active_parameter_count=3,
                scalar_parameters=3, complete_scalar_coefficient_count=6,
                active_parameter_indices=ACTIVE_INDICES, frozen_parameter_indices=FROZEN_INDICES,
                actual_frozen_odd_coefficients=np.asarray(odd).tolist(),
                finite_scalar_assembly='base + frozen odd additions in theta2,theta1,theta3 order, then all three active even controls',
                six_control_search_summation_order_claimed_byte_identical=False,
                identical_exact_real_six_control_formula=True,
                three_active_design_search_is_not_same_g_refinement=True)
            return result

    return ThreeActiveView()


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
    np, core, family = d.np, d.core, d.family
    accepted, prepared, anchor = (core.read(getattr(args, name)) for name in ('accepted', 'prepared', 'tail_anchor'))
    designed, old_flow, old_boundary = family.setup(accepted, prepared, anchor,
                                                   args.material_angles, args.jac_workers)
    full_p = np.asarray(recipe['initial_six_parameters'], float)
    odd = full_p[3:].copy()
    view = active_profile(d, designed, odd)
    original_targets = np.asarray(accepted['core']['coefficients'], float)[:3]
    target = float(recipe['lambda_target'])*original_targets
    core_seed = np.zeros(112); core_seed[:3] = target
    law = accepted['original_metric_identity']['law']
    constructor = core.original_solver.native.outward.FullCoreProbe
    q = constructor(core_seed, 112, 2048, law['velocity'], law['length'], law['k0'])
    q.profile = view.profile
    core.original_solver.fixed.fft.enable_fft(q)
    flow = d.AugmentedFlow(q, view, args.jac_workers)
    affine = core.AffineTail(112)
    boundary = d.PhysicalTestBoundary(view, target, flow.point_rhs, flow.point_jacobian, affine,
        height_sign=old_boundary.eh, radial_sign=old_boundary.er,
        angular=args.material_angles, physical_angles=args.physical_angles)
    if (flow.dimension, flow.n, flow.M, flow.k) != (453, 338, 112, 3):
        raise ValueError('The complete original square dimensions changed')
    parent = None
    if recipe['initial_guess_kind'] == 'fresh-circle-low-three-linear':
        if args.continuation is not None:
            raise ValueError('A fresh circle recipe does not consume an unrelated complete field')
        mesh = np.asarray(prepared['mesh'], float)
        J0 = np.asarray(anchor['heightJetJacobian'], float).reshape(338, 112)[:112]
        reference = family.CircleReference(designed, mesh, J0, original_targets,
                                            boundary.eh, boundary.cut_scale)
        circle = reference.evaluate(full_p)
        values = np.zeros((len(mesh), 453))
        values[:, 0], values[:, boundary.iz] = circle['radius'], circle['height']
        values[:, flow.core_slice] = core_seed
        values[:, flow.parameter_slice] = full_p[:3]
        for j, frequency in enumerate((2., 4., 6.)):
            U, H = circle['modes'][:, j, 0], circle['modes'][:, j, 1]
            values[:, j+1] = target[j]*U
            values[:, flow.M+1+j] = target[j]*((1-frequency*frequency)*circle['radius']-U)/frequency
            values[:, boundary.iz+j+1] = target[j]*H
        guess = dict(kind=recipe['initial_guess_kind'], lambda_target=float(recipe['lambda_target']),
            zero_tail_J_complete_source_sha256=inputs['tail_anchor'],
            full_zero_tail_J_is_measured_diagonal=reference.exactly_diagonal,
            original_circle_low_three_unit_equations=circle['equation'].tolist(),
            all_112_linear_right_rows_of_low_three_seed=circle['full_right'].tolist(),
            low_three_linear_transfer_used_only_as_an_initial_guess=True,
            high109_initial_core_zero_but_still_free_unknowns=True,
            high109_nonresonance_or_Schur_elimination_claimed=False,
            full_nonlinear_zero_or_nonzero_BVP_acceptance=False,
            exact_source_circle_and_full_RHS_summation_paths_claimed_identical=False)
    else:
        if args.continuation is None:
            raise ValueError('Supply the actual same-family complete continuation file')
        digest = sha(args.continuation)
        if recipe.get('continuation_sha256') != digest:
            raise ValueError('The complete continuation file must match its explicit recipe SHA')
        parent = core.read(args.continuation)
        if (parent.get('schema') != SCHEMA or parent.get('M') != 112 or parent.get('N') != 2048
                or parent.get('field_representation') != d.field_spec(112, 2048)
                or parent.get('six_control_full112_implementation', {}).get('input_sha256') != inputs):
            raise ValueError('Only this explicit complete-field schema may supply the continuation guess')
        spec = parent['complete_scalar_profile']
        if (spec.get('schema') != family.SCALAR_SCHEMA
                or spec.get('profile_source_sha256') != PINS[Path(family.__file__).name]
                or spec.get('parameter_order') != PARAMETER_ORDER
                or not np.array_equal(np.asarray(spec['frozen_design_parameters'], float), full_p)):
            raise ValueError('Keep the actual six-coordinate scalar identity of the continuation field')
        mesh = np.asarray(parent['mesh'], float)
        values = np.asarray(parent.get('augmented_states', parent.get('states')), float)
        if values.shape != (len(mesh), 453):
            raise ValueError('Retain all 338 physical, 112 core and three active rows')
        if not np.array_equal(values[-1, flow.parameter_slice], full_p[:3]):
            raise ValueError('The new recipe does not name the actual terminal active controls')
        guess = dict(kind=recipe['initial_guess_kind'], continuation_sha256=digest,
            parent_lambda_target=parent['six_control_full112_implementation']['lambda_target'],
            lambda_target=float(recipe['lambda_target']), parent_success_flag=parent.get('success'),
            parent_is_only_an_initial_guess_for_the_new_target=True,
            all_physical_core_and_active_values_read_without_inlet_reclassification=True,
            parent_rhs_not_relabelled_as_fresh_current_rhs=True)
    if (mesh.ndim != 1 or len(mesh) < 2 or mesh[0] != 0 or np.any(np.diff(mesh) <= 0)
            or abs(mesh[-1]-view.end) > 1e-12 or not np.all(np.isfinite(values))):
        raise ValueError('The actual full interval/initial field layout is invalid')
    # Fresh original RHS is required before Hermite interpolation. It is not a
    # declared nonlinear solution; the unchanged node/mid/RMS preflight follows.
    rhs = flow(mesh, values.T).T
    if not np.all(np.isfinite(rhs)):
        raise FloatingPointError('The complete initial guess failed the original nodal physical domain')
    at = curve_with_exact_nodes(d, mesh, values, rhs)
    preflight = bound_original_preflight(d, output, core.write)
    mesh, values, rhs, residual, additions = preflight(mesh, at, flow, args.max_nodes)
    specification = family.scalar_spec(designed, prepared['complete_scalar_profile']['complete_original_port'],
                                       np.r_[values[-1, flow.parameter_slice], odd], inputs['accepted'])
    record = dict(schema=SCHEMA, scope=__doc__, M=112, N=2048,
        mesh=mesh.tolist(), states=values.tolist(), rhs=rhs.tolist(),
        complete_scalar_profile=specification, field_representation=d.field_spec(112, 2048),
        state_layout='all physical338, constant core112, constant active p1/p2/p3',
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
        physical_test=boundary.description(), six_control_full112_implementation=binding,
        prepared_sha256=sha(seed_path), native_anchor_response_sha256=sha(output/'initial-actual-H-tail.json.gz'),
        native_anchor_height=initial_height.tolist(), actual_current_H_solved_before_this_FD=True,
        FD_perturbed_states_use_explicit_affine_map=True,
        zero_anchor_J_not_relabelled_as_current_H_J=True,
        original_three_perturbations_directions_steps_and_threshold_unchanged=True,
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
                new_scalar_and_explicit_lambda_are_bound_by_independent_adapter=True,
                six_control_full112_implementation=binding,
                actual_native_client_source_sha256=args.expected_tail_client_sha256,
                native_tail_math_configuration_unchanged=True)
            data.pop('native_tail_changed', None)
        return original_band_write(path, data, *positional, **keywords)

    def scalar_spec(profile, port, active, accepted_sha):
        if profile is not problem.view or accepted_sha != binding['input_sha256']['accepted']:
            raise ValueError('The new six-control scalar owner/source changed')
        return d.family.scalar_spec(problem.designed, port, np.r_[active, problem.odd], accepted_sha)

    def make_profile(source, port, peak, source_modes):
        if (source_modes != 96 or peak != problem.prepared['complete_scalar_profile']['peak_curvature']
                or port != problem.prepared['complete_scalar_profile']['complete_original_port']):
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
            raise ValueError('The source target must remain original before applying the explicit lambda')
        result = d.PhysicalTestBoundary(profile, problem.target, rhs, jacobian, affine,
            height_sign=problem.boundary.eh, radial_sign=problem.boundary.er,
            angular=angular, physical_angles=args.physical_angles)
        context['boundary'] = result
        return result

    def initial_guess(source, profile, flow, extension_step, taper_fraction):
        if profile is not problem.view or flow.dimension != 453:
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
                    six_control_full112_implementation=binding,
                    active_parameter_indices=ACTIVE_INDICES, frozen_parameter_indices=FROZEN_INDICES,
                    original_large_target_scaled_only_by_explicit_lambda=True,
                    source_prefix_or_circle_acceptance_not_inherited=True)
                if 'complete_scalar_profile' in data:
                    data['complete_six_scalar_parameters'] = data['complete_scalar_profile']['frozen_design_parameters']
            if name == 'actual.json.gz':
                if context['cut_audit'] is None or context['statistics_active_parameters'] is None:
                    raise RuntimeError('Keep the original physical-test cut measurement and frozen-p statistics')
                data['original_source_metric_identity'] = data.pop('original_metric_identity')
                data['original_metric_identity'] = dict(schema='six-control-material-metric-v1',
                    scalar_specification=data['complete_scalar_profile'],
                    core_coefficients=data['core']['coefficients'],
                    material_coordinate='common theta; ds^2+a(s)^2*dtheta^2',
                    same_g_as_original_source_claimed=False)
                data['sampled_geometry_scalar_parameters'] = context['statistics_active_parameters'].tolist()
                data['physical_test_final_cut_audit'] = context['cut_audit']
                data['scope'] = __doc__
                data['message'] = 'New finite six-control, three-active physical-phi DN accepted by the original complete gates; closed assembly remains open.'
                data['same_metric_refinement'] = False
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
        str(problem.prepared['complete_scalar_profile']['peak_curvature']),
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
    for name in ('recipe', 'accepted', 'prepared', 'tail-anchor', 'tail-config', 'out', 'work'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--expected-recipe-sha256', required=True)
    parser.add_argument('--continuation', type=Path)
    parser.add_argument('--tail-client', type=Path)
    parser.add_argument('--expected-tail-client-sha256')
    parser.add_argument('--tail-source-root', type=Path)
    parser.add_argument('--prepare-only', action='store_true')
    parser.add_argument('--jac-workers', type=int, default=2)
    parser.add_argument('--max-nodes', type=int, default=1200)
    parser.add_argument('--material-angles', type=int, default=4096)
    parser.add_argument('--physical-angles', type=int, default=4096)
    parser.add_argument('--node-heap', type=int, default=6144)
    parser.add_argument('--outer-iterations', type=int, default=8)
    args = parser.parse_args()
    recipe, recipe_identity = read_recipe(args.recipe, args.expected_recipe_sha256)
    if not args.prepare_only and any(x is None for x in (
            args.tail_client, args.expected_tail_client_sha256, args.tail_source_root)):
        raise ValueError('A real complete live tail implementation and its actual source SHA are required')
    d = runtime()
    inputs = {name: sha(getattr(args, name)) for name in ('accepted', 'prepared', 'tail_anchor', 'tail_config')}
    expected = {name: d.family.EXPECTED[name] for name in inputs}
    if inputs != expected or recipe.get('source_input_sha256') != inputs:
        raise ValueError('Keep the exact original complete mathematical input tuple')
    out, work = temporary_paths(args)
    owner = None
    session = dict(schema=SCHEMA, phase='preparing', success=False,
        new_coupled_finite_acceptance=False, full_Cartesian_closed_surface=False,
        recipe=recipe_identity, input_sha256=inputs, consumed_source_sha256=d.closure,
        no_current_candidate_or_native_parent_assumed=True)
    d.core.write(out/'adapter-status.json', session)
    try:
        seed_dir, fd_dir, full_dir = out/'initial-guess', out/'actual-H-response', out/'full-DN'
        for path in (seed_dir, fd_dir, full_dir):
            path.mkdir()
        problem = prepare_problem(d, args, recipe, inputs, seed_dir)
        binding = dict(schema=SCHEMA, source_sha256=sha(__file__), consumed_source_sha256=d.closure,
            input_sha256=inputs, recipe=recipe_identity,
            source_accepted_prefix=dict(M=96, N=1024, sha256=inputs['accepted']),
            lambda_target=float(recipe['lambda_target']), original_low_core_targets=problem.original_targets.tolist(),
            current_fixed_low_core_targets=problem.target.tolist(), original_core_target_file_unchanged=True,
            initial_six_parameters=problem.full_p.tolist(), actual_frozen_odd_coefficients=problem.odd.tolist(),
            active_parameter_indices=ACTIVE_INDICES, frozen_parameter_indices=FROZEN_INDICES,
            parameter_order=PARAMETER_ORDER, state_dimension=453, physical_state_dimension=338,
            field_modes=112, tail_modes=112, core_unknowns=112, high_core_free_unknowns=109,
            left_rows=341, right_rows=112, all_native_slope_columns_and_rows_retained=True,
            old_scalar_schema_or_failed_native_source_relabelled=False,
            boundary_schema=d.PHYSICAL_SCHEMA, true_current_H_native_and_full_J_required=True,
            explicitly_selected_native_client_file=None if args.tail_client is None else args.tail_client.name,
            explicitly_selected_native_client_sha256=args.expected_tail_client_sha256,
            native_client_execution_requested=not args.prepare_only,
            original_complete_FD_threshold=5e-5, original_inner_trial_count=17,
            original_collocation_and_frozen_RMS_tolerance=1e-6, original_BC_tolerance=1e-11,
            true_final_native_full_J_and_audit_required=True,
            low_mode_threshold_or_high_mode_proof_is_not_an_added_numerical_gate=True,
            regenerable_raw_is_temporary_only=True)
        binding.update(original_807f_adapter_baseline_sha256=PINS['geometry_20261115_six_control_full112.py'],
            height_path_policy=recipe['height_continuation'],
            height_path_helper_sha256=PINS['geometry_20261115_finite_trace_r273_height_path.py'],
            same_original_tail_worker_for_height_path_FD_fullDN_and_final_audit=True,
            intermediate_height_convergence_not_full_DN_acceptance=True,
            original_124_adapter_baseline_sha256=PINS['geometry_20261115_six_control_height_continuation_full112.py'],
            native_correction_implementation_file='geometry_20261115_finite_trace_r273_tail_client.py',
            native_correction_implementation_sha256=PINS['geometry_20261115_finite_trace_r273_tail_client.py'],
            original_warm_predictor_and_ten_trial_and_final_gates_retained=True,
            current_full_J_r_cut_far_sigma_R273_eta1=True,
            first_positive_mathematical_refusal_ends_this_height_path=True,
            original_145_full_DN_baseline_sha256=PINS['geometry_20261115_six_control_r273_height_full112.py'],
            current_tangent_implementation='original64-noJ-primal-finite-root-loop-variation-v1',
            finite_trace_variation_sha256=PINS['geometry_20261115_original64_finite_trace_variation.mjs'],
            noJ_matched_variation_flow_sha256=PINS['geometry_20261115_original64_finite_trace_flow.mjs'],
            original_root_and_noJ_primal_arithmetic_retained=True,
            successful_fixed_trace_real_linearisation_only=True,
            IEEE_rounding_map_derivative_or_branch_stability_not_claimed=True)
        problem.record['six_control_full112_implementation'] = binding
        seed_path = seed_dir/'prepared.json.gz'
        d.core.write(seed_path, problem.record)
        port_path = seed_dir/'original-port.json'
        d.core.write(port_path, problem.prepared['complete_scalar_profile']['complete_original_port'])
        session.update(phase='prepared-unaccepted-full-field', implementation=binding,
                       prepared_sha256=sha(seed_path), initial_collocation_max=problem.record['initial_collocation_max'])
        d.core.write(out/'adapter-status.json', session)
        if args.prepare_only:
            print(json.dumps(dict(event='six-control-finite-trace-r273-height-path-full112-prepared-only', schema=SCHEMA,
                lambda_target=binding['lambda_target'], prepared_sha256=sha(seed_path),
                success=False, native_called=False), allow_nan=False), flush=True)
            return 0
        if (args.tail_client.name != 'geometry_20261115_finite_trace_r273_tail_client.py'
                or args.expected_tail_client_sha256 != PINS['geometry_20261115_finite_trace_r273_tail_client.py']
                or sha(args.tail_client) != args.expected_tail_client_sha256):
            raise ValueError('Use this explicitly bound original-worker current R273 client')
        config = d.core.read(args.tail_config)
        if (int(config['modes']), int(config['spacing'])) != (112, 2):
            raise ValueError('The complete actual tail must retain112 even material modes')
        for name, expected_value in problem.prepared['complete_scalar_profile']['complete_original_port']['parameters'].items():
            if config.get(name) != expected_value:
                raise ValueError('The actual original physical tail parameter differs: '+name)
        owner = SharedNativeClient(d.core.load_client(args.tail_client, args.tail_config,
            args.tail_source_root, full_dir/'true-tail', args.node_heap))
        for name in ('radius', 'E', 'Ep', 'backgroundSlope', 'backgroundSecond'):
            if not d.np.isclose(float(owner.cut[name]), float(problem.view.cut[name]), rtol=2e-11, atol=2e-13):
                raise ValueError('The actual live native cut differs: '+name)
        H = d.core.true_height(problem.boundary, problem.values[-1])
        session.update(phase='original-same-worker-height-path', actual_current_H=H.tolist(),
            height_path_policy=recipe['height_continuation'])
        d.core.write(out/'adapter-status.json', d.response.clean(session))
        actual, path_receipt = d.height_path.continue_complete_height(
            owner, H, recipe['height_continuation'], out/'height-path', binding)
        session.update(height_path_status=path_receipt, height_path_endpoint_completed=True)
        binding['completed_height_path_status'] = path_receipt
        # These are the existing actual-tail protocol responsibilities, not a
        # replacement residual criterion or permission to fabricate an anchor.
        if (actual.get('actual_nonlinear_solve') is not True or actual.get('converged') is not True
                or actual.get('failed', False)
                or not d.np.array_equal(d.np.asarray(actual['checkpoint']['cutHeight']), H)):
            raise ValueError('Only a truly completed response at the exact current H can anchor the original FD')
        d.core.write(fd_dir/'initial-actual-H-tail.json.gz', actual)
        passed, report = actual_boundary_fd(d, problem, actual, H, fd_dir, binding, seed_path)
        session.update(phase='actual-current-H-FD-completed', actual_current_H=H.tolist(),
            response_check_sha256=sha(fd_dir/'response-check.json'),
            original_boundary_FD_passed=passed,
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
    except d.height_path.HeightPathStopped as error:
        session.update(phase='height-path-stopped', height_path_outcome=error.outcome,
            height_path_status=error.receipt, height_path_resource_partial=error.resource_partial,
            height_path_endpoint_completed=False, exception=repr(error),
            original_FD_or_full_DN_entered_after_height_path_stop=False)
        return 75 if error.resource_partial else 3
    except Exception as error:
        session.update(phase='exception', exception=repr(error), traceback=traceback.format_exc())
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
        print(json.dumps(d.response.clean(dict(event='six-control-finite-trace-r273-height-path-full112-adapter-returned',
            schema=SCHEMA, phase=session['phase'], success=session['success'],
            new_coupled_finite_acceptance=session['new_coupled_finite_acceptance'],
            lambda_target=recipe['lambda_target'],
            original_full_DN_phase=session.get('original_full_DN_phase'),
            maximum_boundary_FD_relative_error=session.get('maximum_boundary_FD_relative_error'),
            native_live_calls=session.get('native_live_calls'), exception=session.get('exception'),
            height_path_outcome=session.get('height_path_outcome'),
            height_path_endpoint_completed=session.get('height_path_endpoint_completed'),
            height_path_status=session.get('height_path_status'),
            adapter_status_sha256=sha(out/'adapter-status.json'))), allow_nan=False), flush=True)


if __name__ == '__main__':
    raise SystemExit(main())
