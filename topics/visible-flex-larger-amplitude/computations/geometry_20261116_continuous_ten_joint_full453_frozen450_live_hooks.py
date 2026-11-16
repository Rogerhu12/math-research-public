#!/usr/bin/env python3
"""Request203 joint-provider live ten hooks for actual complete453 and complete450.

The original complete-band/core solver bodies and their native/FD/RMS/BC/audit
criteria remain untouched. This module binds the actual ten-family flow and
current boundary, captures the original main's live objects, and leaves its
accepted JSON source/profile/metric fields unannotated for the R400 writer.
The original core close() only ends a phase lease: the independent driver
owns final shutdown of the one real current-C worker.
"""
from __future__ import annotations
import hashlib
import os
from pathlib import Path
import sys

LEGACY_SHA = "c71d616936cf33e43965906c7cc99face01d06a12433420474b688b8d76b946d"

def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()

def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Scientific execution is confined to the public repository Actions")

def solve(d, args, problem, binding, seed_path, port_path, output, lease, *, legacy, driver_source):
    """Run the original complete-band/core body with an actual k=3 or k=0 owner."""
    require_actions()
    if sha(legacy.__file__) != LEGACY_SHA:
        raise ValueError("The frozen full453 source used for hooks changed")
    if problem.flow.k not in (0, 3) or problem.flow.dimension != 450 + problem.flow.k:
        raise ValueError("Keep all 338 physical, 112 core and actual active rows")
    restore_attributes = legacy.restore_attributes
    bound_original_preflight = legacy.bound_original_preflight
    curve_with_exact_nodes = legacy.curve_with_exact_nodes
    np, core, continuation = d.np, d.core, d.banded.continuation
    plain_write, previous_seam = core.write, core.final_height_seam
    context = dict(flow=None, boundary=None, separated=None, cut_audit=None,
        statistics_active_parameters=None, original_result_written=False,
        source_sha256=sha(driver_source), dimension=problem.flow.dimension,
        active_parameter_count=problem.flow.k)
    final_preflight = bound_original_preflight(d, output, plain_write)
    prepared_at = curve_with_exact_nodes(d, problem.mesh, problem.values, problem.rhs)
    original_band_write = d.banded.write

    def band_write(path, data, *positional, **keywords):
        if isinstance(data, dict) and Path(path).name == 'complete-banded-intent.json':
            data.update(mathematical_BC_changed=True, equation_row_permutation_only=False,
                linear_backend_is_only_row_permutation_of_current_physical_test=True,
                new_scalar_and_explicit_lambda_are_bound_by_independent_adapter=True,
                current_C_full112_implementation=binding,
                actual_state_dimension=problem.flow.dimension,
                actual_active_parameter_count=problem.flow.k,
                actual_native_client_source_sha256=args.expected_tail_client_sha256,
                original_finite_current_C_native_policy_preserved=True,
                old_finite_tail_reused_or_relabelled=False)
            data.pop('native_tail_changed', None)
        return original_band_write(path, data, *positional, **keywords)

    def scalar_spec(profile, port, active, accepted_sha):
        if profile is not problem.view or accepted_sha != binding['input_sha256']['accepted']:
            raise ValueError('The actual continuous-ten scalar owner/source changed')
        # The R400 live writer consumes exactly this actual runtime specification.
        # Current producer identity belongs to a separate companion manifest.
        return profile.export_specification(active)

    def make_profile(source, port, peak, source_modes):
        if (source_modes != 96 or peak != args.legacy_peak_curvature_argument
                or port != problem.current_port or source != problem.accepted):
            raise ValueError('The original constructor metadata or actual current port identity changed')
        return problem.view

    def constructor(core_values, M, N, velocity, length, k0):
        if (M, N) != (96, 1024) or not np.array_equal(core_values, problem.accepted['core']['coefficients']):
            raise ValueError('The genuine accepted96 source was reclassified')
        law = problem.accepted['original_metric_identity']['law']
        if (velocity, length, k0) != (law['velocity'], law['length'], law['k0']):
            raise ValueError('The original physical source law changed')
        return problem.q

    def flow_constructor(probe,profile,workers):
        if probe is not problem.q or profile is not problem.view or workers!=args.jac_workers:
            raise ValueError("The current original physical flow owner changed")
        result = problem.target_owner.flow(d.actual_augmented,probe,profile,workers)
        context["flow"] = result
        return result

    def boundary(profile, old_target, rhs, jacobian, affine, *, angular):
        if (profile is not problem.view or angular != args.material_angles
                or not np.array_equal(old_target, problem.original_targets)):
            raise ValueError('Retain the original source target before the explicit current target')
        flow = context["flow"]
        if flow is None or rhs != flow.point_rhs or jacobian != flow.point_jacobian:
            raise ValueError("The original main must create this actual complete flow")
        result = problem.target_owner.boundary(d.actual_boundary, profile,
            problem.target, flow, affine, height_sign=problem.boundary.eh,
            material_angles=angular, physical_angles=args.physical_angles)
        context['boundary'] = result
        return result

    def separated_constructor(boundary_):
        if boundary_ is not context["boundary"]:
            raise ValueError("The separated boundary must retain the actual current owner")
        result = d.SeparatedBoundary(boundary_)
        if (result.k != problem.flow.k
                or result.left_count != 338 + problem.flow.k):
            raise ValueError("Keep every current left row and all 112 right rows")
        context["separated"] = result
        return result

    def initial_guess(source, profile, flow, extension_step, taper_fraction):
        if profile is not problem.view or flow.dimension != problem.flow.dimension:
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
        return lease

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
        # Do not replace the core source, schema, profile or metric fields.
        # The live R400 writer binds this unannotated original acceptance.
        result = plain_write(path, data)
        if Path(path).name == "actual.json.gz":
            context["original_result_written"] = True
        return result

    def enter_core():
        # banded.main has installed this frozen closure, including the original
        # released_newton call and its read-only trial wrapper.
        continuation.install_qr_diagnostics(output, 112, plain_write)
        return core.main()

    old_argv = sys.argv
    argv = [str(driver_source), '--accepted', str(args.accepted), '--port', str(port_path),
        '--out', str(output), '--work', str(args.work), '--warm', str(seed_path),
        '--tail-client', str(args.tail_client), '--tail-config', str(args.tail_config),
        '--tail-source-root', str(args.tail_source_root), '--peak-curvature',
        str(args.legacy_peak_curvature_argument),
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
                    ('FullDNBoundary', boundary), ('AugmentedFlow',flow_constructor),
                    ('SeparatedBoundary', separated_constructor),
                    ('prepared_guess', initial_guess),
                    ('preflight', final_preflight), ('load_client', load_client),
                    ('final_height_seam', final_seam), ('write', write)):
                replace(core, name, value)
            replace(core.original_solver.native.outward, 'FullCoreProbe', constructor)
            replace(d.banded, 'write', band_write)
            replace(continuation, 'main', enter_core)
            sys.argv = argv
            status = d.banded.main()
            return status, context
    finally:
        sys.argv = old_argv


