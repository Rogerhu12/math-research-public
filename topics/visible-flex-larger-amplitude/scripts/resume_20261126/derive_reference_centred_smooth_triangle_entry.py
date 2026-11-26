#!/usr/bin/env python3
"""Pure complete-source R715 derivation; no scientific module is imported.

The complete new calibration helper and the complete normal source deriver
are byte-bound source inputs. Every other full body is derived from its exact
published R711 predecessor. Outputs never overwrite the repository.
"""
import argparse
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import pprint
import sys

COMPONENT_SHA = '3d12c0fcfba4e9477bb989f55917e3cd3d5d720338b297854e97800299a20040'
COMPONENT = 'derive_reference_centred_smooth_triangle_normal.py'
HELPER_SHA = 'a8e849068b12ffe2876c07ec2518947890c9f09614da2a9882b53e268e3ba873'
HELPER = 'reference_centred_smooth_triangle_calibration.py'
ORIGINAL = {
    'normal': ('so3_supported_smooth_triangle_normal_lift_operator.py',
        '66e81e439a2545134549b4527e68a2480a9d8010679dcf9cfa23ca5e48c15d68'),
    'geometry': ('so3_supported_smooth_triangle_normal_lift_geometry.py',
        'ef46386e2313cd1e53c971ea8d6ee63a7c6d630074a8feb45ebb9103ec0e52f3'),
    'driver': ('fullclosed_supported_smooth_triangle_normal_lift_so3_qp.py',
        'fd95d91abe9525cbfa34d55bd576be7dfba1fe25fcafb73bdaaea40e003ad65f'),
    'launcher': ('launch_supported_smooth_triangle_normal_lift_so3_actions.py',
        '8dc81890440e744bd846e71b4d33848566dfdf76bcf9d30c47c59664a5823339'),
    'reader': ('read_supported_smooth_triangle_normal_lift_so3_report.py',
        '3914004ac39b838c33411bd11660bb8fbec1372630c3569f3ea4ad5ae16c0f97')}
NEW = {
    'normal': 'so3_reference_centred_smooth_triangle_normal_lift_operator.py',
    'geometry': 'so3_reference_centred_smooth_triangle_normal_lift_geometry.py',
    'driver': 'fullclosed_reference_centred_smooth_triangle_normal_lift_so3_qp.py',
    'launcher': 'launch_reference_centred_smooth_triangle_normal_lift_so3_actions.py',
    'reader': 'read_reference_centred_smooth_triangle_normal_lift_so3_report.py'}
NORMAL_SCHEMA = 'complete-R711-reference-centred-SO3-fixed-normal-plane-six-control-layer-v1'
GEOMETRY_SCHEMA = 'complete-R711-reference-centred-normal-SO3-world-geometry-and-original-192-amplitude-rows-v1'
REPORT_SCHEMA = 'complete-R711-reference-centred-fixed-normal-plane-SO3-QP-v1'
SNAPSHOT_SCHEMA = 'actual-reference-centred-normal-current-point-snapshot-v1'
READY_INPUT = 'smooth-triangle-fixed-reference-normal-full-history-run05-ready.json'
READY_INPUT_SHA = '7d967cdb4e145f20bc7e9d14a25e20c1ae9c310508db858cc670665eb966cec9'
READY_OUTPUT = 'reference-centred-smooth-triangle-normal-full-history-run05-ready.json'


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def read_bound(path, expected):
    text = path.read_text()
    if digest(text) != expected:
        raise ValueError('Changed COMPLETE source input: '+str(path))
    return text


def once(text, old, new):
    if text.count(old) != 1:
        raise ValueError('Need one complete original source fragment: '+old[:120])
    return text.replace(old,new,1)


def assignment(text, name, value):
    tree = ast.parse(text)
    found = [n for n in tree.body if isinstance(n,ast.Assign)
        and any(isinstance(v,ast.Name) and v.id == name for v in n.targets)]
    if len(found) != 1:
        raise ValueError('Need one literal source assignment: '+name)
    n = found[0]
    lines = text.splitlines(keepends=True)
    return ''.join(lines[:n.lineno-1])+name+' = '+pprint.pformat(value,sort_dicts=False,width=100)+'\n'+''.join(lines[n.end_lineno:])


def literal(text, name):
    found = [n for n in ast.parse(text).body if isinstance(n,ast.Assign)
        and any(isinstance(v,ast.Name) and v.id == name for v in n.targets)]
    if len(found) != 1:
        raise ValueError('Need one original literal assignment: '+name)
    return ast.literal_eval(found[0].value)


def docstring(text, content):
    node = ast.parse(text).body[0]
    if not isinstance(node,ast.Expr) or not isinstance(node.value,ast.Constant):
        raise ValueError('The complete original module documentation changed')
    lines = text.splitlines(keepends=True)
    return ''.join(lines[:node.lineno-1])+'"""'+content+'"""\n'+''.join(lines[node.end_lineno:])


def check(text, name):
    tree = ast.parse(text)
    compile(tree,name,'exec')
    for node in ast.walk(tree):
        if isinstance(node,ast.Dict):
            keys = [v.value for v in node.keys if isinstance(v,ast.Constant) and isinstance(v.value,str)]
        elif isinstance(node,ast.Call):
            keys = [v.arg for v in node.keywords if v.arg is not None]
        else:
            continue
        if len(keys) != len(set(keys)):
            raise ValueError('Duplicate literal/keyword key in '+name)
    if len(text.encode()) >= 100000:
        raise ValueError('Each complete auditable source must remain below 100KB: '+name)
    if any(line.rstrip() != line for line in text.splitlines()):
        raise ValueError('Trailing source whitespace: '+name)


def functions(text, cls=None):
    tree = ast.parse(text)
    if cls is not None:
        tree = next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name == cls)
    return {n.name:ast.dump(n,include_attributes=False) for n in tree.body
        if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))}


def unchanged(old, new, allowed, cls=None):
    before,after = functions(old,cls),functions(new,cls)
    changed = [name for name in before if name not in after or before[name] != after[name]]
    if any(name not in allowed for name in changed):
        raise ValueError('Unexpected complete-body change: '+repr(changed))
    return dict(changed_original_functions=changed,
        unchanged_original_functions=len(before)-len(changed),
        added_functions=sorted(set(after)-set(before)))


def derive_geometry(text, normal_sha):
    text = docstring(text,'''Complete R715 reference-centred field geometry and original full rows.

All original world sixjet scans, both witness signs, permanent positions,
full 192-prefix selection and complete parameter transposes are retained.
The new physical field includes its complete current raw closure lift.
Working Fs is not labelled unit. No previous-field certificate is inherited.
''')
    text = assignment(text,'SCHEMA',GEOMETRY_SCHEMA)
    text = assignment(text,'OPERATOR_SCHEMA',NORMAL_SCHEMA)
    text = assignment(text,'ENDPOINT_SOURCE_SHA256',normal_sha)
    text = once(text,"KEYS = ('F', 'Fs', 'Fphi', 'Fss', 'Fsphi', 'Fphiphi')",
        "REFERENCE_CENTERING_SOURCE_SHA256 = "+repr(HELPER_SHA)+"\nKEYS = ('F', 'Fs', 'Fphi', 'Fss', 'Fsphi', 'Fphiphi')")
    text = once(text,"                or model.get('radial_Gram_error_identically_zero') is not True",
        "                or model.get('radial_Gram_error_identically_zero') is not False\n                or model.get('accurate_zero_root_radial_Gram_error_identically_zero') is not True")
    text = once(text,'        normal_nodes = tuple(Fraction(value) for value in problem.normal_step_nodes)',
        '''        calibration = problem.reference_calibration
        definition = model.get('reference_centering_definition')
        if (not isinstance(definition,dict) or definition != calibration.definition
                or definition.get('schema') != 'R715-fixed-reference-centred-working-normal-definition-v1'
                or definition.get('source_sha256') != REFERENCE_CENTERING_SOURCE_SHA256
                or definition.get('endpoint_source_sha256') != ENDPOINT_SOURCE_SHA256
                or definition.get('original_reference_point_sha256') != array_sha(problem.base.initial())
                or definition.get('base_model_identity_sha256') != problem.base.identity
                or definition.get('fixed_supported_reference_identity_sha256') != problem.base.parent_jet.model_identity
                or definition.get('nodewise_difference_before_original_complete_cumsum') is not True
                or definition.get('all_normal_stages_and_full_upstream_parameter_jets_retained') is not True
                or definition.get('numerical_current_raw_closure_defect_omitted') is not False
                or definition.get('numerical_radial_Gram_error_identically_zero') is not False
                or calibration.field_identity != problem.identity):
            raise ValueError('Bind the complete SAME frozen-reference calibration and physical raw-defect lift')
        for name in ('reference_data','observe_field','current_record'):
            if sha(getattr(calibration,name).__func__.__code__.co_filename) != REFERENCE_CENTERING_SOURCE_SHA256:
                raise ValueError('The actual complete calibration helper changed: '+name)
        normal_nodes = tuple(Fraction(value) for value in problem.normal_step_nodes)''')
    text = once(text,'            operator_source_sha256=self.operator_sha256,\n            fixed_supported_unit_seed_identity_sha256=canonical(seed),',
        '''            operator_source_sha256=self.operator_sha256,
            reference_centering_source_sha256=REFERENCE_CENTERING_SOURCE_SHA256,
            reference_centering_definition=definition,
            complete_current_raw_closure_lift_and_all_derivatives_read=True,
            working_radial_Gram_identity_claimed=False,
            fixed_supported_unit_seed_identity_sha256=canonical(seed),''')
    return text


def derive_driver(text, normal_sha, geometry_sha):
    text = docstring(text,'''Complete R715 reference-centred R711 normal-plane SO3 optimization.

Every original free coordinate, positive Gram row, complete geometry row,
Phase-I/common-slack rule and actual nonlinear trial screen is retained.
Only the root equation is centred at the fixed original reference, while
all six physical jets retain the complete CURRENT raw closure lift. Working
radial Gram is actually read. All 32 default stages and every upstream
normal-frame/target parameter and angular derivative remain in J/J*.
''')
    text = assignment(text,'SCHEMA',REPORT_SCHEMA)
    pins = literal(text,'SOURCE_PINS')
    pins['endpoint'] = ('scripts/resume_20261126/'+NEW['normal'],normal_sha)
    pins['geometry'] = ('scripts/resume_20261126/'+NEW['geometry'],geometry_sha)
    pins['reference_calibration'] = ('scripts/resume_20261126/'+HELPER,HELPER_SHA)
    text = assignment(text,'SOURCE_PINS',pins)
    text = assignment(text,'ROOT_SNAPSHOT_SCHEMA',SNAPSHOT_SCHEMA)
    text = assignment(text,'ROOT_SNAPSHOT_KEYS',literal(text,'ROOT_SNAPSHOT_KEYS')+('current_reference_calibration',))
    text = once(text,"    endpoint = load('_so3_independent_frozen_moment_zero_endpoint', paths['endpoint'])",
        "    endpoint = load('_so3_independent_frozen_moment_zero_endpoint', paths['endpoint'])\n    calibration = load('_so3_complete_reference_centred_calibration',paths['reference_calibration'])")
    text = once(text,"        new_input_binder=(new_moment_binding if args.moment_input_binding == 'supported-smooth-triangle-reference' else None))",
        "        new_input_binder=(new_moment_binding if args.moment_input_binding == 'supported-smooth-triangle-reference' else None),\n        reference_centering_module=calibration)")
    text = once(text,'        representation=q.model, coordinate_norm=coordinates.record,',
        '''        representation=q.model, coordinate_norm=coordinates.record,
        reference_centering_definition=q.reference_calibration.definition,
        reference_centering_source=file_record(paths['reference_calibration']),
        frozen_original_reference_point_sha256=q.reference_point_sha256,
        complete_current_raw_closure_lift_and_all_sixjet_derivatives_retained=True,
        raw_quadrature_defect_is_not_the_centred_root_residual=True,
        all_normal_stages_retained_at_literal_reference_zero=True,''')
    text = once(text,'        final_original_physical_closure_is_separately_checked=True,',
        '''        final_original_physical_closure_is_separately_checked=False,
        final_reference_centred_closure_is_separately_checked=True,
        raw_physical_closure_is_retained_in_complete_lift=True,''')
    text = once(text,"        radial_metric_error_identically_zero=True,\n        radial_identity_scope='exact unit-rotation integral definition; finite evaluation errors unpaid',\n        radial_Gram_uses_complete_hprime_Delta=False,",
        "        radial_metric_error_identically_zero=False,\n        accurate_zero_root_radial_metric_identity=True,\n        radial_identity_scope='only exact reference and complete final implicit roots; WORKING Fs includes the actual complete raw lift',\n        radial_Gram_uses_complete_hprime_Delta=True,")
    return text


def derive_launcher(text, driver_sha):
    text = docstring(text,'''Prepare the complete R715 centred R711 normal-plane SO3 QP.

Pure argv preparation does not evaluate a field. All scientific execution
remains public Actions. The exact reference source, original point, complete
history and all numerical/geometry budgets stay explicitly bound.
''')
    text = assignment(text,'DRIVER_SHA',driver_sha)
    text = text.replace(ORIGINAL['driver'][0],NEW['driver'])
    text = once(text,"schema='public-actions-complete-supported-smooth-triangle-normal-plane-SO3-command-v1'",
        "schema='public-actions-complete-R711-reference-centred-normal-plane-SO3-command-v1'")
    text = once(text,'        unit_T_is_exact_final_Fs=True, numerical_unit_and_integral_errors_certified=False,',
        '''        unit_T_is_exact_final_Fs=False, numerical_unit_and_integral_errors_certified=False,
        accurate_unit_identity_requires_exact_reference_and_final_normal_roots=True,
        physical_sixjets_retain_complete_current_raw_closure_lift=True,
        reference_centering_helper_sha256=records['reference_calibration']['sha256'],
        nodewise_centred_root_difference_and_raw_physical_defect_are_separate=True,''')
    return text


READER_FUNCTIONS = r'''
def calibration_snapshot(value, point=None, definition=None):
    """Only own-point recorded raw/centred maxima; missing values stay missing."""
    keys = {'reference_point_sha256','current_full_point_sha256','raw_value_max',
        'raw_phi_max','raw_phiphi_max','centered_value_max','centered_phi_max',
        'centered_phiphi_max','working_radial_identity','complete_raw_defect_lift',
        'equation_scope'}
    if not isinstance(value,dict) or set(value) != keys:
        raise ValueError('Keep the complete explicit current reference-calibration readout')
    for name in ('reference_point_sha256','current_full_point_sha256'):
        word = value[name]
        if word is None and name == 'current_full_point_sha256':
            continue
        if not isinstance(word,str) or len(word) != 64 or any(c not in '0123456789abcdef' for c in word):
            raise ValueError('The actual full point digest is not a complete SHA256')
    if point != value['current_full_point_sha256']:
        raise ValueError('Do not backfill another current point calibration')
    if definition is not None and value['reference_point_sha256'] != definition['original_reference_point_sha256']:
        raise ValueError('The frozen ORIGINAL reference point changed')
    for name in ('raw_value_max','raw_phi_max','raw_phiphi_max',
                 'centered_value_max','centered_phi_max','centered_phiphi_max'):
        number = value[name]
        if number is not None and (isinstance(number,bool) or not isinstance(number,(int,float))
                or not math.isfinite(number) or number < 0):
            raise ValueError('Keep actual finite nonnegative recorded norms or null')
    if (value['working_radial_identity'] is not False or value['complete_raw_defect_lift'] is not True
            or value['equation_scope'] != 'reference-centred complete equation; distinct raw quadrature defect'):
        raise ValueError('A centred root cannot remove the full physical raw-defect lift')
    return dict(value)


def centering_binding(report, model, roles):
    """Pure source/model/original-point binding; no reference integral is recomputed."""
    value = model.get('reference_centering_definition')
    base = model['base_complete_model']
    seed = base['fixed_supported_unit_seed_model']
    if (not isinstance(value,dict)
            or value.get('schema') != 'R715-fixed-reference-centred-working-normal-definition-v1'
            or value.get('source_sha256') != roles['reference_calibration']
            or value.get('endpoint_source_sha256') != roles['endpoint']
            or value.get('original_complete_normal_source_sha256') !=
                '66e81e439a2545134549b4527e68a2480a9d8010679dcf9cfa23ca5e48c15d68'
            or value.get('original_reference_point_sha256') != report['actual_reference_initial_full_point_sha256']
            or value.get('original_reference_point_sha256') != report.get('frozen_original_reference_point_sha256')
            or value.get('original_height_hex') != seed['initial_height_hex']
            or value.get('base_model_identity_sha256') != model['base_model_identity_sha256']
            or value.get('fixed_supported_reference_identity_sha256') != canonical(seed)
            or value.get('mesh_sha256') != model['mesh_sha256']
            or value.get('integration_order') != report['working_evaluation']['integration_order']
            or report.get('reference_centering_definition') != value
            or report.get('reference_centering_source',{}).get('sha256') != roles['reference_calibration']):
        raise ValueError('The fixed centering definition must bind this complete original reference and exact working rule')
    for name in ('nodewise_difference_before_original_complete_cumsum',
                 'exact_equality_to_original_closure_requires_exact_reference_closure',
                 'all_normal_stages_and_full_upstream_parameter_jets_retained'):
        if value.get(name) is not True:
            raise ValueError('Keep the full reference-centred mathematical/numerical contract: '+name)
    for name in ('numerical_current_raw_closure_defect_omitted',
                 'numerical_radial_Gram_error_identically_zero'):
        if value.get(name) is not False:
            raise ValueError('A numerical defect cannot be promoted to an identity: '+name)
    for name in ('gauss_nodes_sha256','gauss_weights_sha256'):
        word = value.get(name)
        if not isinstance(word,str) or len(word) != 64 or any(c not in '0123456789abcdef' for c in word):
            raise ValueError('Retain the actual complete fixed integration-carrier digest')
    for name in ('complete_current_raw_closure_lift_and_all_sixjet_derivatives_retained',
                 'raw_quadrature_defect_is_not_the_centred_root_residual',
                 'all_normal_stages_retained_at_literal_reference_zero',
                 'final_reference_centred_closure_is_separately_checked',
                 'raw_physical_closure_is_retained_in_complete_lift'):
        if report.get(name) is not True:
            raise ValueError('The current complete field omits a centering/lift responsibility: '+name)
    if report.get('final_original_physical_closure_is_separately_checked') is not False:
        raise ValueError('The root tolerance applies to the centred equation, not a separately zero raw quadrature defect')
    return dict(definition=value,definition_identity_sha256=canonical(value),
        source_sha256=roles['reference_calibration'],
        original_reference_point_sha256=value['original_reference_point_sha256'],
        raw_physical_closure_and_centred_root_residual_are_distinct=True,
        exact_reference_and_working_fees_certified=False)


def calibration_metadata(value, model, roles):
    """Bind actual frozen batches and own-point lift statistics without raw recomputation."""
    definition = model['reference_centering_definition']
    actual = value.get('reference_centering')
    if (not isinstance(actual,dict)
            or actual.get('schema') != 'complete-R715-frozen-reference-working-calibration-v1'
            or actual.get('source_sha256') != roles['reference_calibration']
            or actual.get('definition') != definition
            or actual.get('model_identity_sha256') != canonical(model)
            or actual.get('reference_point_sha256') != definition['original_reference_point_sha256']):
        raise ValueError('The actual reference calibration belongs to another complete field')
    for name in ('physical_field_uses_complete_current_raw_defect_lift',
                 'lift_includes_all_current_parameter_and_angular_derivatives'):
        if actual.get(name) is not True:
            raise ValueError('The current physical lift must remain complete: '+name)
    for name in ('baseline_reselected_from_current_outer_point','raw_reference_defect_forced_to_zero',
                 'numerical_radial_Gram_identity_claimed','accurate_reference_or_quadrature_or_geometry_certified'):
        if actual.get(name) is not False:
            raise ValueError('The actual calibration may not assert '+name)
    current = calibration_snapshot(actual.get('current'),value['current_full_point_sha256'],definition)
    if value.get('current_reference_calibration') != current:
        raise ValueError('Keep the SAME current-point raw/centred calibration in metadata and snapshots')
    records = actual.get('actual_reference_records')
    if not isinstance(records,list) or actual.get('fixed_endpoint_angle_batches') != len(records):
        raise ValueError('Keep every actual completed frozen-reference angle batch')
    angles = 0
    for record in records:
        count = record.get('angle_count')
        if (isinstance(count,bool) or not isinstance(count,int) or count < 1
                or not isinstance(record.get('path'),str)
                or not isinstance(record.get('bytes'),int) or record['bytes'] <= 0
                or set(record.get('arrays_sha256',{})) != {'phi','core','cap','delta'}):
            raise ValueError('The actual frozen-reference batch record is incomplete')
        for word in [record.get('angle_list_sha256'),record.get('sha256'),*record['arrays_sha256'].values()]:
            if not isinstance(word,str) or len(word) != 64 or any(c not in '0123456789abcdef' for c in word):
                raise ValueError('Keep complete actual calibration array/file identities')
        numbers = record.get('maximum_defect_norms')
        if not isinstance(numbers,list) or len(numbers) != 3 or any(
                isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v) or v < 0 for v in numbers):
            raise ValueError('The complete fixed-reference defect has all three angular readouts')
        angles += count
    maxima = actual.get('maximum_fixed_reference_defect_norms')
    if maxima != [max((r['maximum_defect_norms'][j] for r in records),default=None) for j in range(3)]:
        raise ValueError('The reported calibration maxima must match their actual completed batch records')
    if (value.get('working_radial_Gram_error_identically_zero') is not False
            or value.get('complete_current_raw_defect_lift_in_physical_sixjets') is not True
            or value.get('endpoint_residual_scope') != 'centred equation; raw quadrature closure defect is reported separately'):
        raise ValueError('The actual operator must distinguish the raw physical lift from centred roots')
    return dict(source_sha256=roles['reference_calibration'],
        definition_identity_sha256=canonical(definition),
        original_reference_point_sha256=definition['original_reference_point_sha256'],
        completed_fixed_reference_angle_batches=len(records),
        recorded_angle_occurrences_across_batches=angles,
        reference_batch_records_sha256=canonical(records),
        fixed_defect_value_max=maxima[0],fixed_defect_phi_max=maxima[1],fixed_defect_phiphi_max=maxima[2],
        current=current,physical_sixjet_raw_lift_complete=True,
        working_radial_identity=False,raw_reference_files_recomputed=False,
        continuous_reference_root_quadrature_or_geometry_certified=False)

'''


def derive_reader(text, driver_sha):
    text = docstring(text,'''Pure complete R715 reference-centred R711 normal-chain attribution.

All original normal snapshots, Phase I, full geometry/metric/history and
source/model guards remain. Raw quadrature closure and the centred root
equation have separate own-point records. A complete physical sixjet lift is
mandatory; working radial identity is never asserted. No F/J, root, integral
or scientific array is recomputed by this pure reader.
''')
    text = assignment(text,'DRIVER_SHA',driver_sha)
    text = assignment(text,'REPORT_SCHEMA',REPORT_SCHEMA)
    text = assignment(text,'OPERATOR_SCHEMA',NORMAL_SCHEMA)
    text = assignment(text,'ROOT_SNAPSHOT_SCHEMA',SNAPSHOT_SCHEMA)
    text = assignment(text,'ROOT_SNAPSHOT_KEYS',literal(text,'ROOT_SNAPSHOT_KEYS')+('current_reference_calibration',))
    text = text.replace(ORIGINAL['driver'][0],NEW['driver'])
    text = once(text,'def normal_dimensions(value, model=None):',READER_FUNCTIONS+'\ndef normal_dimensions(value, model=None):')
    text = once(text,'    result = {key:value[key] for key in ROOT_SNAPSHOT_KEYS}',
        '''    calibration_snapshot(value['current_reference_calibration'],value['current_full_point_sha256'])
    result = {key:value[key] for key in ROOT_SNAPSHOT_KEYS}''')
    text = once(text,'        first_and_second_angular_endpoint_residuals_are_physical_length_units=True)',
        '''        first_and_second_angular_endpoint_residuals_are_physical_length_units=True,
        those_endpoint_residuals_are_the_centred_equation=True,
        raw_quadrature_closure_is_separately_in_the_complete_physical_lift=True)''')
    text = once(text,'            endpoint_roots(value)\n            count += 1',
        '''            endpoint_roots(value)
            calibration_snapshot(value['current_reference_calibration'],value['current_full_point_sha256'],
                model['reference_centering_definition'])
            count += 1''')
    text = once(text,'    current = endpoint_roots(value)\n    seed_actual =',
        '    current = endpoint_roots(value)\n    calibrated = calibration_metadata(value,model,source_by_role)\n    seed_actual =')
    text = once(text,'        fixed_supported_unit_seed=seed_actual,',
        '        fixed_supported_unit_seed=seed_actual,reference_calibration=calibrated,')
    text = once(text,"            or model.get('radial_Gram_error_identically_zero') is not True",
        "            or model.get('radial_Gram_error_identically_zero') is not False\n            or model.get('accurate_zero_root_radial_Gram_error_identically_zero') is not True")
    text = once(text,"            or report.get('radial_metric_error_identically_zero') is not True\n            or report.get('radial_Gram_uses_complete_hprime_Delta') is not False",
        "            or report.get('radial_metric_error_identically_zero') is not False\n            or report.get('accurate_zero_root_radial_metric_identity') is not True\n            or report.get('radial_Gram_uses_complete_hprime_Delta') is not True")
    text = once(text,"        raise ValueError('Keep the exact zero-closure definition, same fixed target, and complete numerical Gram')",
        "        raise ValueError('Keep the exact fixed target and full WORKING physical lift in every numerical Gram row')\n    centered_binding = centering_binding(report,model,roles)")
    text = text.replace("model.get('schema') != 'complete-supported-smooth-triangle-reference-SO3-fixed-normal-plane-six-control-zero-layer-v1'",
        "model.get('schema') != "+repr(NORMAL_SCHEMA))
    text = once(text,"    if report.get('final_original_physical_closure_is_separately_checked') is not True:\n        raise ValueError('A normalized plane residual cannot replace the final original physical closure tolerance')",
        "    if report.get('final_reference_centred_closure_is_separately_checked') is not True:\n        raise ValueError('A normalized stage residual cannot replace the final complete centred closure tolerance')")
    text = once(text,"schema='actual-complete-supported-smooth-triangle-fixed-normal-plane-SO3-scalar-readout-v1'",
        "schema='actual-complete-R711-reference-centred-normal-plane-SO3-scalar-readout-v1'")
    text = once(text,"        model_identity_sha256=report['model_identity_sha256'],",
        "        model_identity_sha256=report['model_identity_sha256'],\n        reference_centering=centered_binding,\n        reference_calibration_diagnostics=None if endpoint is None else endpoint['reference_calibration'],")
    text = once(text,'        radial_Gram_uses_complete_hprime_Delta=False,',
        '''        radial_Gram_uses_complete_hprime_Delta=True,
        working_radial_metric_error_identically_zero=False,
        exact_radial_identity_requires_exact_reference_and_final_implicit_roots=True,
        raw_quadrature_defect_is_not_the_centred_root_residual=True,''')
    return text


def derive_ready(text, records, driver):
    if digest(text) != READY_INPUT_SHA:
        raise ValueError('Bind the complete published original R711 ready parameters')
    before = json.loads(text)
    olddir = 'smooth-triangle-fixed-normal-lift-first'
    newdir = 'reference-centred-smooth-triangle-normal-lift-first'
    # Only this selected fresh output directory and entry paths are renamed.
    # All ten actually required history inputs remain literal identical words.
    ready = json.loads(text.replace(olddir,newdir))
    ready['schema'] = 'complete-R715-reference-centred-R711-normal-full-history-run05-ready-v1'
    ready['scope'] = ('Complete R715 reference-centred R711 twelve-piece smooth-triangle fixed reference, '
        'all original free core/omega/H, all positive Gram rows and the full common 32-stage normal map. '
        'Every closure/target angular jet subtracts the original reference nodewise. All physical sixjets '
        'retain the complete CURRENT raw closure lift and its full parameter/angle derivatives. '
        'The raw quadrature defect is distinct from the centred root residual; working radial Gram is really read. '
        'The complete original geometry, 192-plus-amplitude rows, Phase I and real trial screens remain.')
    ready['history_scope'] = ('The SAME ten published history inputs remain: nine earlier actual inputs and '
        'the genuinely running first five-piece supported seed report. That actual report must exist '
        'before admission; it is not an empty-address contribution. An unexecuted plain R711 ready is '
        'NOT an additional dependency and need not run. Every later same-target scientific report that '
        'actually executes before admission must be explicitly appended, including direct SOC if it precedes this entry.')
    ready['unexecuted_plain_R711_report_required'] = False
    ready['plain_R711_scientific_replay_required'] = False
    ready['prior_plain_R711_ready_sha256'] = READY_INPUT_SHA
    ready['prior_plain_R711_ready_is_parameter_source_not_scientific_predecessor'] = True
    ready['source_sha256'] = {Path(relative).name:sha for relative,sha in literal(driver,'SOURCE_PINS').values()}
    ready['source_sha256'].update({name:record['sha256'] for name,record in records.items()})
    ready['steps'][0]['id'] = 'complete-r715-reference-centred-r711-normal-full-history-first-20261126-05'
    ready['steps'][1]['id'] = 'actual-r715-reference-centred-r711-normal-full-history-first-20261126-05'
    ready['steps'][0]['script'] = 'topics/visible-flex-larger-amplitude/scripts/resume_20261126/'+NEW['launcher']
    ready['steps'][1]['script'] = 'topics/visible-flex-larger-amplitude/scripts/resume_20261126/'+NEW['reader']
    ready['steps'][0]['scope'] = ready['scope']
    ready['steps'][1]['scope'] = ('Pure complete new-source/model/fixed-reference attribution of the actual entire returned report. '
        'Retain every original normal snapshot and its own raw/centred calibration values. '
        'No F/J, root, integral or scientific array is recomputed. Initial failure remains incomplete.')
    science_summary = ready['steps'][0]['summary'][newdir+'/report.json']
    pure_summary = ready['steps'][1]['summary']['postprocess/'+newdir+'-readout.json']
    for summary in (science_summary,pure_summary):
        summary['final_centred_endpoint_reread'] = summary.pop('final_original_endpoint_reread')
        summary['final_centred_endpoint_passed'] = summary.pop('final_original_endpoint_passed')
    science_summary.update({
        'calibration_source':'source_sha256_by_role.reference_calibration',
        'original_reference_point':'frozen_original_reference_point_sha256',
        'working_radial_identity':'radial_metric_error_identically_zero',
        'complete_raw_lift':'radial_Gram_uses_complete_hprime_Delta',
        'raw_distinct_from_centred':'raw_quadrature_defect_is_not_the_centred_root_residual',
        'all_stages_retained':'all_normal_stages_retained_at_literal_reference_zero',
        'reference_calibration_batches':'latest_operator_metadata.reference_centering.fixed_endpoint_angle_batches',
        'fixed_raw_delta_value':'latest_operator_metadata.reference_centering.maximum_fixed_reference_defect_norms.0',
        'fixed_raw_delta_phi':'latest_operator_metadata.reference_centering.maximum_fixed_reference_defect_norms.1',
        'fixed_raw_delta_phiphi':'latest_operator_metadata.reference_centering.maximum_fixed_reference_defect_norms.2'})
    for name in ('raw_value_max','raw_phi_max','raw_phiphi_max','centered_value_max','centered_phi_max','centered_phiphi_max'):
        science_summary['current_'+name] = 'latest_operator_metadata.current_reference_calibration.'+name
        pure_summary['current_'+name] = 'reference_calibration_diagnostics.current.'+name
    pure_summary.update({
        'calibration_source':'reference_centering.source_sha256',
        'calibration_definition':'reference_centering.definition_identity_sha256',
        'original_reference_point':'reference_centering.original_reference_point_sha256',
        'working_radial_identity':'working_radial_metric_error_identically_zero',
        'complete_raw_lift':'radial_Gram_uses_complete_hprime_Delta',
        'reference_calibration_batches':'reference_calibration_diagnostics.completed_fixed_reference_angle_batches',
        'fixed_raw_delta_value':'reference_calibration_diagnostics.fixed_defect_value_max',
        'fixed_raw_delta_phi':'reference_calibration_diagnostics.fixed_defect_phi_max',
        'fixed_raw_delta_phiphi':'reference_calibration_diagnostics.fixed_defect_phiphi_max'})
    ready['implementation_note'] = 'notes/2026-11-26-R715-reference-centred-smooth-triangle-full-normal-entry.md'
    ready['published_reference_centring_result'] = 'results/R715-reference-centred-normal-sixjets-and-error-ledger.md'
    ready['reference_centring'] = dict(
        fixed_baseline='the actual original complete base.initial() point, never reselected from current x',
        endpoint_baseline='same complete current-source Torch core/cap method at the frozen original point',
        integration_baseline='same bound reference tensors, same query, nodes, weights and cumsum',
        root_difference='subtract each reference node BEFORE complete integration reduction',
        physical_field='complete current raw closure lift in F,Fs,Fphi,Fss,Fsphi,Fphiphi',
        working_radial_identity=False,all_stage_roots_and_upstream_jets_retained=True,
        raw_reference_defect_zeroed=False,accurate_error_or_geometry_certificate_inherited=False,
        continuous_reference_and_quadrature_fees_not_yet_paid=True)
    ready['narrow_normal_cost_change'] = dict(
        same_41_original_normal_methods_and_all_stage_solves=True,
        all_root_frames_and_implicit_matrices_retained=True,
        R714_C1_repeated_frame_cache_used=False,actual_speedup_claimed=False)
    before_args = before['steps'][0]['args']
    expected_args = [word.replace(olddir,newdir) for word in before_args]
    if ready['steps'][0]['args'] != expected_args:
        raise ValueError('No original scientific input or numerical parameter may change silently')
    manifests = [word for i,word in enumerate(ready['steps'][0]['args'])
        if i and ready['steps'][0]['args'][i-1] == '--manifest']
    expected_history = ['{work}/'+word for word in before['required_actual_history_reports']]
    if manifests != expected_history or len(manifests) != 10:
        raise ValueError('Retain the exact complete ten-input physical history without a fictitious dependency')
    if ready['steps'][1]['parent_bundle'] != before['steps'][1]['parent_bundle']:
        raise ValueError('Keep the existent original reference parent so a failed initial field remains readable')
    ready['complete_source_and_parameter_closure_ready'] = True
    ready['complete_scientific_entry_executed'] = False
    ready['actual_scientific_outcome_inferred'] = False
    ready['entry_admitted_or_executed'] = False
    return ready


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--component-directory',type=Path,default=Path(__file__).resolve().parent)
    p.add_argument('--out-dir',type=Path,required=True)
    a = p.parse_args()
    repo,out = a.repo.resolve(),a.out_dir.resolve()
    if out == repo or repo in out.parents:
        raise ValueError('Pure generated sources must be staged outside the repository')
    src = repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261126'
    before = {role:read_bound(src/name,sha) for role,(name,sha) in ORIGINAL.items()}
    helper = read_bound(a.component_directory/HELPER,HELPER_SHA)
    component = a.component_directory/COMPONENT
    read_bound(component,COMPONENT_SHA)
    spec = importlib.util.spec_from_file_location('_pure_reference_centred_normal_deriver',component)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    result = {'normal':module.derive_normal(before['normal'])}
    result['geometry'] = derive_geometry(before['geometry'],digest(result['normal']))
    result['driver'] = derive_driver(before['driver'],digest(result['normal']),digest(result['geometry']))
    result['launcher'] = derive_launcher(before['launcher'],digest(result['driver']))
    result['reader'] = derive_reader(before['reader'],digest(result['driver']))
    audits = dict(normal=unchanged(before['normal'],result['normal'],
        {'__init__','_select_point','_detach_data','_subset_data','_closure_jets','_meridian_data','fields_torch','metadata'},
        'ZeroClosureOperator'),
        geometry=unchanged(before['geometry'],result['geometry'],{'__init__'},'GeometryScreen'),
        driver=unchanged(before['driver'],result['driver'],{'main'}),
        launcher=unchanged(before['launcher'],result['launcher'],{'main'}),
        reader=unchanged(before['reader'],result['reader'],
            {'endpoint_roots','bind_snapshots','endpoint_metadata','read_report'}))
    suffix = '    def save_report():\n'
    if before['driver'].split(suffix,1)[1] != result['driver'].split(suffix,1)[1]:
        raise ValueError('The complete original save/report/PhaseI/QP/real-trial body must remain byte-identical')
    audits['original_driver_complete_loop_suffix_sha256'] = digest(suffix+before['driver'].split(suffix,1)[1])
    out.mkdir(parents=True,exist_ok=True)
    records = {}
    for role,text in result.items():
        check(text,NEW[role])
        path = out/NEW[role]
        path.write_text(text)
        records[NEW[role]] = dict(sha256=digest(text),bytes=len(text.encode()))
    check(helper,HELPER)
    (out/HELPER).write_text(helper)
    records[HELPER] = dict(sha256=digest(helper),bytes=len(helper.encode()))
    ready_text = read_bound(repo/'topics/visible-flex-larger-amplitude/computations'/READY_INPUT,READY_INPUT_SHA)
    ready = derive_ready(ready_text,records,result['driver'])
    ready_bytes = json.dumps(ready,indent=2)+'\n'
    (out/READY_OUTPUT).write_text(ready_bytes)
    report = dict(schema='complete-R715-reference-centred-R711-source-derivation-v1',
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        original_complete_sources={name:sha for name,sha in ORIGINAL.values()},
        complete_normal_deriver_source_sha256=COMPONENT_SHA,calibration_helper_source_sha256=HELPER_SHA,
        sources=records,static_audits=audits,scientific_modules_imported=False,
        F_or_J_or_root_or_integral_evaluated=False,complete_sources_not_patches=True,
        ready_input_sha256=READY_INPUT_SHA,
        ready_output=dict(path=READY_OUTPUT,bytes=len(ready_bytes.encode()),sha256=digest(ready_bytes)),
        ready_keeps_all_ten_actual_history_inputs=True,
        unexecuted_plain_R711_is_not_a_scientific_prerequisite=True)
    (out/'reference-centred-source-lock-table.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
