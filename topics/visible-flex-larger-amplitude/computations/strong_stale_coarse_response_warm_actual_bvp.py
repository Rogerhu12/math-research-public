#!/usr/bin/env python3
"""Explicitly transport a saved old response only as a new initial guess.

AI-assisted research workflow, strong_recovery, 2026-11-13.
The current complete M32 field must itself be genuinely accepted. Its original
owned acceptance and, when used, unchanged fixed-view conversion are verified.
The M28 response stays bound to its own old accepted baseline. Allowed prefix
profile differences and numerical-mesh interpolation are reported explicitly;
the saved vector is never called a derivative at the current point or an M32
Jacobian. All original new-H, full-J, Newton, RMS, domain and audit gates remain.
"""
from __future__ import annotations
import ast
import hashlib
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ORIGINAL_NAME = 'strong_coarse_response_warm_actual_bvp.py'
_ORIGINAL_SHA = 'ff5acad191d51544bfebaf46902f7e58f89a2e4575130f9b33932aa25ef8972c'
_NEW_SCOPE = __doc__


def _verify_current_origin(options, current_path, current, current_raw, now,
                           current_tail_path, sources):
    import numpy as np
    from strong_actual_fixed_control_response import raw_flat
    original_path = options.current_original_accepted
    resource_path = options.current_owned_resource
    if original_path is None or resource_path is None:
        raise ValueError('Give the real current original accepted primary and owned resource')
    original, resource = read(original_path), read(resource_path)
    if (not original.get('solver_success') or original.get('audit_pending', True)
            or not original['config'].get('actual_nonlinear_tail')
            or resource.get('exitcode') != 0 or not resource.get('wait4_observed')
            or int(original['modes']) != 32):
        raise ValueError('The current original full actual acceptance is missing')
    if not str(original_path).endswith('.json.gz'):
        raise ValueError('Use the original accepted gzip primary')
    actual_prefix = str(original_path)[:-8]
    if resource.get('task_prefix') != actual_prefix:
        raise ValueError('The owned exit belongs to a different current original primary')
    command = resource['command']
    if argument(command, '--out-prefix') != actual_prefix:
        raise ValueError('The original owned command has a different output identity')
    if (str(current_tail_path) != original['actual_tail']['final_response']
            or canonical(original['actual_tail']) != canonical(current['actual_tail'])):
        raise ValueError('The current fixed view changed the original real tail identity')
    original_raw_path = Path(original['raw_collocation_checkpoint']['file'])
    if sha(original_raw_path) != original['raw_collocation_checkpoint']['sha256']:
        raise ValueError('The current original raw header hash differs')
    original_raw = read(original_raw_path)
    if not original_raw.get('solver_success') or original_raw.get('physical_surface') is not False:
        raise ValueError('An actually accepted original raw checkpoint is required')
    changed_view = sha(current_path) != sha(original_path)
    if changed_view:
        view = current.get('frozen_design_view', {})
        gates = ('complete_H_bitwise_equal', 'raw_x_y_cubic_unchanged',
                 'physical_quintics_unchanged', 'all_core_coefficients_unchanged',
                 'gauge_unchanged', 'original_numerical_reference_unchanged',
                 'eight_physical_data_unchanged')
        if (not all(view.get(name) is True for name in gates)
                or view.get('nonlinear_solve_run') or view.get('tail_worker_started')
                or view.get('source_sha256', {}).get(str(original_path)) != sha(original_path)
                or view.get('source_sha256', {}).get(str(original_raw_path)) != sha(original_raw_path)):
            raise ValueError('The actual fixed-view proof is not bound to this original primary/raw')
        edited = {'scope', 'config', 'base_profile', 'parameters', 'parameter_layout',
            'raw_collocation_checkpoint', 'fixed_metric_provenance', 'frozen_design_view',
            'actual_augmented_continuation', 'prescribed_actual_core', 'original_design_provenance'}
        for key in set(original)-edited:
            if key not in current or canonical(current[key]) != canonical(original[key]):
                raise ValueError('A physical field changed in the declared fixed view: '+key)
        for key in ('actual_augmented_continuation', 'prescribed_actual_core'):
            if key in original and current.get('original_design_provenance', {}).get(key) != original[key]:
                raise ValueError('The original design provenance was not retained: '+key)
        oc = {k:v for k,v in original['config'].items() if k != 'fixed_metric'}
        cc = {k:v for k,v in current['config'].items() if k != 'fixed_metric'}
        if canonical(oc) != canonical(cc) or current['base_profile'] != original['frozen_profile']:
            raise ValueError('The fixed view changed original configuration or physical profile')
    for name in ('x', 'y', 'p'):
        values = np.asarray(raw_flat(original_raw_path, original_raw, name, sources))
        values = values.reshape(original_raw['arrays'][name]['shape'])
        if name == 'p':
            if values.shape not in ((32,), (35,)):
                raise ValueError('Unexpected current original parameter layout')
            values = values[:32]
        if values.shape != now[name].shape or values.tobytes() != now[name].tobytes():
            raise ValueError('The current fixed view changed complete raw bits: '+name)
    sources.update({str(p):sha(p) for p in (original_path, original_raw_path, resource_path)})
    return dict(original_primary=str(original_path), original_primary_sha256=sha(original_path),
        original_raw=str(original_raw_path), original_raw_sha256=sha(original_raw_path),
        owned_resource=str(resource_path), owned_resource_sha256=sha(resource_path),
        original_owned_exitcode=0, fixed_view_used=changed_view,
        complete_original_physical_fields_and_raw_bits_verified=True)


def _build_stale_transport_source():
    path = _HERE/_ORIGINAL_NAME
    original = path.read_text()
    if hashlib.sha256(path.read_bytes()).hexdigest() != _ORIGINAL_SHA:
        raise ValueError('The frozen original same-g warm source differs')
    source, changes = original, []

    def edit(before, after):
        nonlocal source
        if source.count(before) != 1:
            raise ValueError('The explicit stale-warm source site is not unique: '+before[:100])
        source = source.replace(before, after, 1)
        changes.append((before, after))

    node = ast.parse(original).body[0]
    doc = ''.join(original.splitlines(keepends=True)[node.lineno-1:node.end_lineno])
    edit(doc, repr(_NEW_SCOPE)+'\n')
    edit("            'chart_reference_frequencies', 'frozen_profile', 'physical_tail_parameters',\n",
         "            'chart_reference_frequencies', 'physical_tail_parameters',\n")
    before = """    if (coarse['numerical_meridian_chart']['reference_t'] != current['numerical_meridian_chart']['reference_t']
            or coarse['numerical_meridian_chart']['physical_s'] != current['numerical_meridian_chart']['physical_s']
            or coarse['central_correction_scales'] != current['central_correction_scales'][:27]
            or (coarse['config']['angular'], current['config']['angular']) != (1024, 1280)):
        raise ValueError('Original knots, core units or declared angular representations differ')
"""
    after = """    if (coarse['numerical_meridian_chart']['reference_t'] != current['numerical_meridian_chart']['reference_t']
            or (coarse['config']['angular'], current['config']['angular']) != (1024, 1280)):
        raise ValueError('The common material reference knots or declared angular representations differ')
    permitted = set(PRIMARY+EXTERNAL)
    profile_changes = {}
    for key in set(coarse['frozen_profile']) | set(current['frozen_profile']):
        left, right = coarse['frozen_profile'].get(key), current['frozen_profile'].get(key)
        if canonical(left) != canonical(right):
            if key not in permitted:
                raise ValueError('An undeclared prefix-family property changed: '+key)
            profile_changes[key] = dict(old=left, current=right)
    old_scales = np.asarray(coarse['central_correction_scales'], dtype=np.float64)
    current_scales = np.asarray(current['central_correction_scales'], dtype=np.float64)
    if (old_scales.shape != (27,) or current_scales.shape != (31,)
            or not np.isfinite(old_scales).all() or not np.isfinite(current_scales).all()
            or np.any(old_scales <= 0.) or np.any(current_scales <= 0.)):
        raise ValueError('Complete positive physical core parameter units are required')
    for surface in (coarse, current):
        physical = np.asarray(surface['numerical_meridian_chart']['physical_s'], dtype=np.float64)
        if not np.isfinite(physical).all() or not np.all(np.diff(physical) > 0.):
            raise ValueError('An accepted physical meridian chart is not strictly oriented')
"""
    edit(before, after)
    edit("""    if old['x'].tobytes() != now['x'].tobytes():
        raise ValueError('This initial-guess adapter requires the same complete raw mesh; no interpolation is hidden')
""", """    same_mesh = old['x'].tobytes() == now['x'].tobytes()
    for mesh in (old['x'], now['x']):
        if mesh[0] != 0. or mesh[-1] != 1. or not np.all(np.diff(mesh) > 0.):
            raise ValueError('The complete original numerical meshes must span oriented [0,1]')
""")
    first = source.index("    if not str(current_path).endswith('.json.gz'):\n")
    last = source.index("    if (response.get('schema') != 'fixed-actual-to-three-control-response-v1'\n", first)
    edit(source[first:last], """    current_origin = _verify_current_origin(options, current_path, current, current_raw,
        now, current_tail_path, sources)
""")
    before = """    field = np.zeros_like(now['y'])
    field[mapping] = combined[:old['y'].size].reshape(old['y'].shape, order='F')
    parameters = np.zeros(32)
    parameters[:28] = combined[old['y'].size:]
    extra = sorted(set(range(97))-set(map(int, mapping)))
    if (field[mapping].tobytes() != combined[:old['y'].size].reshape(old['y'].shape, order='F').tobytes()
            or not np.all(field[extra] == 0.) or not np.all(parameters[28:] == 0.)):
        raise ValueError('The complete lower-spectrum increment was not exactly embedded')
"""
    after = """    old_field = combined[:old['y'].size].reshape(old['y'].shape, order='F')
    if same_mesh:
        transported_field = old_field.copy()
    else:
        from scipy.interpolate import CubicSpline
        transported_field = CubicSpline(old['x'], old_field, axis=1)(now['x'])
    if transported_field.shape != (85, len(now['x'])) or not np.isfinite(transported_field).all():
        raise ValueError('The explicitly interpolated complete initial-guess vector is invalid')
    field = np.zeros_like(now['y'])
    field[mapping] = transported_field
    parameters = np.zeros(32)
    old_parameters = combined[old['y'].size:]
    parameters[0] = old_parameters[0]*coarse['core']['coefficients'][0]/current['core']['coefficients'][0]
    parameters[1:28] = old_parameters[1:]*old_scales/current_scales[:27]
    extra = sorted(set(range(97))-set(map(int, mapping)))
    if (field[mapping].tobytes() != transported_field.tobytes()
            or not np.all(field[extra] == 0.) or not np.all(parameters[28:] == 0.)):
        raise ValueError('The declared complete initial-guess embedding differs')
"""
    edit(before, after)
    edit("        coarse_modes=28, actual_modes=32, complete_original_mesh_bits_identical=True,\n"
         "        original_material_chart_and_physical_metric_identical=True,\n",
         "        coarse_modes=28, actual_modes=32, complete_original_mesh_bits_identical=same_mesh,\n"
         "        original_material_chart_and_physical_metric_identical=(not profile_changes),\n"
         "        current_original_acceptance=current_origin,\n"
         "        explicitly_stale_response=True, current_point_derivative_claim=False,\n"
         "        permitted_prefix_profile_changes=profile_changes,\n"
         "        physical_s_identical=(coarse['numerical_meridian_chart']['physical_s']==current['numerical_meridian_chart']['physical_s']),\n"
         "        numerical_direction_transport=dict(kind='exact same-grid copy' if same_mesh else 'CubicSpline in original common numerical t',\n"
         "            old_nodes=len(old['x']), current_nodes=len(now['x']), no_mode_or_node_subsampling=True,\n"
         "            current_mesh_and_current_baseline_unchanged=True, derivative_at_current_point_claim=False),\n"
         "        parameter_unit_transport=dict(old_complete_scales=old_scales.tolist(),\n"
         "            current_complete_scales=current_scales.tolist(),\n"
         "            log_q_factor=coarse['core']['coefficients'][0]/current['core']['coefficients'][0],\n"
         "            first_three_targets_still_enforced_by_original_warm=True),\n"
         "        stale_transport_source=_STALE_TRANSPORT_PROVENANCE,\n")
    edit("    parser.add_argument('--coarse-reference', type=Path)\n",
         "    parser.add_argument('--current-original-accepted', type=Path)\n"
         "    parser.add_argument('--current-owned-resource', type=Path)\n"
         "    parser.add_argument('--coarse-reference', type=Path)\n")
    if source.count('strong_coarse_response_warm_actual_bvp') != 3:
        raise ValueError('Unexpected original warm module-name sites')
    before = 'strong_coarse_response_warm_actual_bvp'
    after = 'strong_stale_coarse_response_warm_actual_bvp'
    source = source.replace(before, after)
    changes.append((before, after, 3))
    tail = "\nif __name__ == '__main__':\n    main()\n"
    edit(tail, '\n# Original main invocation is deferred to this explicit adapter entry.\n')
    reverse = source
    for item in reversed(changes):
        before, after = item[:2]
        count = item[2] if len(item) == 3 else 1
        if len(item) == 3:
            if reverse.count(after) != count:
                raise ValueError('The module-name reverse identity differs')
            reverse = reverse.replace(after, before)
        else:
            if reverse.count(after) != 1:
                raise ValueError('An explicit transport reverse source site differs')
            reverse = reverse.replace(after, before, 1)
    if reverse != original:
        raise ValueError('The transport changed an undeclared original production site')
    ast.parse(source, filename='<explicit-stale-response-initial-guess>')
    return source, dict(original_sameg_warm_source=_ORIGINAL_NAME,
        original_sameg_warm_source_sha256=_ORIGINAL_SHA,
        stale_adapter_source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        transformed_initial_guess_source_sha256=hashlib.sha256(source.encode()).hexdigest(),
        exact_reverse_recovers_frozen_sameg_warm_source=True,
        original_ODE_Newton_RMS_trueH_fullJ_and_audit_sources_unchanged=True,
        every_math_MJS_unchanged=True, old_response_not_relabelled_at_current_point=True)


_STALE_SOURCE, _STALE_TRANSPORT_PROVENANCE = _build_stale_transport_source()
exec(compile(_STALE_SOURCE, '<explicit-stale-response-initial-guess>', 'exec'), globals())

if __name__ == '__main__':
    main()
