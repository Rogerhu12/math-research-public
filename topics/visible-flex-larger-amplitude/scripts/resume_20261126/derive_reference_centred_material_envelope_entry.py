#!/usr/bin/env python3
"""Pure full-source derivation of the independent complete material-envelope entry.

Every dependency is pinned by its complete actual source. Never imports a
scientific module or executes a field.
"""
import argparse
import ast
import copy
import hashlib
import json
from pathlib import Path
import pprint

PARENT_SOURCE_PINS = {
    'fullclosed_reference_centred_c1_smooth_triangle_normal_lift_so3_qp.py':
        'f075257aaea0930f60d905c9b02ac5cfcff61bc42d7daf337912c8a287d0f347',
    'launch_reference_centred_c1_smooth_triangle_normal_lift_so3_actions.py':
        '509daaab85537ae1a905eaab9f18e51b2b10a008eaf0a93714bbbe95e8782de5',
    'read_reference_centred_c1_smooth_triangle_normal_lift_so3_report.py':
        '3803a72570aed98eb797f03aca6696055b299ad43e1b06673c482c1a6b25a907',
}
ADDITIONAL_SOURCE_PINS = {
    'envelope_memory': ('complete_material_envelope_memory.py', 'c79c7f7ec1febf0ab6dca30d28a91b1566745972342c7336a3a9a106f56b3152'),
    'envelope_rows': ('complete_material_envelope_rows.py', '729910dc27b0dc4fb5b1b019635f8dc606dcb2965fcbd3c47dc380b7a028c8d7'),
    'geometry': ('so3_reference_centred_c1_material_envelope_geometry.py', 'bd1a2d439e2d83326dc59aa8dd9cdb28dccdbc453ab6f980f281475d44e0471f'),
}
REPORT_SCHEMA = 'complete-R711-reference-centred-C1-material-envelope-fixed-normal-plane-SO3-QP-v1'
READOUT_SCHEMA = 'actual-complete-R711-reference-centred-C1-material-envelope-normal-plane-SO3-scalar-readout-v1'
LOOP_SUFFIX_SHA = '9b05f8e00c483491ffd9259b2d675af940c6f0b8a8104d6bfcd70ffb0e31b4ee'
READY_PARENT_SHA = '02a6f468c65ee20a7d5dbd8ace284ab2ebbddac946614b5b42feb7783fe570dc'
OUTPUT_NAMES = {
    'driver': 'fullclosed_reference_centred_c1_material_envelope_so3_qp.py',
    'launcher': 'launch_reference_centred_c1_material_envelope_so3_actions.py',
    'reader': 'read_reference_centred_c1_material_envelope_so3_report.py',
}

EXPECTED_OUTPUT_SHA256 = {'fullclosed_reference_centred_c1_material_envelope_so3_qp.py': 'cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5', 'launch_reference_centred_c1_material_envelope_so3_actions.py': 'b93af9809adaf42a3eee9328c6ca857156c38609f40db975a92c3bea5f5af991', 'read_reference_centred_c1_material_envelope_so3_report.py': '104e014062f29969c0c94884bf810b6f9b23999ad8cc902238f981a9b0ad35f7'}

ALL_LOCATIONS = r'''
def all_locations(args, preparation, q, history, restart=None, source_report_path=None, *, envelope_memory):
    """Explicit new permanent-envelope policy with the original complete known-history walker."""
    return envelope_memory.load_memory(args,preparation,q,history,
        restart=restart,source_report_path=source_report_path)
'''

READER_ADDITION = r'''
def material_envelope_binding(topic, report, roles, driver):
    """Bind the new finite responsibility and working-row policy without scientific recomputation."""
    relative, expected_source = load_pins(driver)['envelope_memory']
    path = topic/relative
    if sha(path) != expected_source or roles.get('envelope_memory') != expected_source:
        raise ValueError('Keep the complete independent material-envelope memory source')
    name = '_actual_complete_material_envelope_reader_'+expected_source
    spec = importlib.util.spec_from_file_location(name,path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    for function in (module.definition,module.validate_report_metadata,module.validate_scan_metadata):
        if sha(function.__code__.co_filename) != expected_source:
            raise ValueError('Use the actual whole-source pure envelope validators')
    cap = report.get('material_envelope_near_active_rows')
    if type(cap) is not int or cap < 1:
        raise ValueError('The independently declared near-active candidate cap must be positive')
    expected = module.definition(near_active_rows=cap)
    actual = report.get('material_envelope')
    if (not isinstance(actual,dict) or actual.get('definition') != expected
            or report.get('material_envelope_definition') != expected
            or report.get('material_envelope_source',{}).get('sha256') != expected_source
            or report.get('material_envelope_rows_source',{}).get('sha256') != roles['envelope_rows']
            or report.get('material_envelope_new_working_set_policy') is not True
            or report.get('unknown_historical_protected_labels_reconstructed') is not False
            or report.get('old_protected_required_priority_equivalence_claimed') is not False
            or report.get('full_material_envelope_nonlinear_responsibility') is not True):
        raise ValueError('Do not call the new complete envelope an unchanged old protected-row policy')
    validated = module.validate_report_metadata(actual,
        model_identity=report['model_identity_sha256'],
        carrier_sha256=report['observation_carrier_sha256'])
    if not isinstance(validated,dict):
        raise ValueError('The complete pure envelope attribution must return its actual validated summary')
    binding = dict(definition=expected,definition_identity_sha256=canonical(expected),
        source_sha256=expected_source,rows_source_sha256=roles['envelope_rows'],
        actual_metadata=validated,old_unknown_protected_tags_reconstructed=False,
        old_required_row_priority_equivalence_claimed=False,
        nonlinear_responsibility_is_complete_permanent_envelope=True,
        continuous_geometry_or_metric_certificate=False)
    def validate_scan(value):
        checked = module.validate_scan_metadata(value,model_identity=report['model_identity_sha256'],
            carrier_sha256=report['observation_carrier_sha256'])
        if checked.get('definition') != expected or checked.get('definition_identity_sha256') != canonical(expected):
            raise ValueError('Every actual scan must retain this report exact same complete envelope policy')
        return checked
    def validate_rows(rows, starting_geometry):
        if not isinstance(rows,dict) or not isinstance(starting_geometry,dict):
            raise ValueError('Every completed direction has its own complete row preparation and starting scan')
        checked_scan = validate_scan(starting_geometry.get('material_envelope'))
        prefix = rows.get('known_geometry_and_amplitude_prefix_rows')
        total = rows.get('selected_rows')
        columns = rows.get('coordinate_size')
        added = rows.get('appended_envelope_rows')
        if (any(type(v) is not int or v < 0 for v in (prefix,total,columns,added))
                or columns < 1 or columns != report['original_variables']):
            raise ValueError('Use actual nonnegative row counts and every positive full coordinate column')
        before = rows.get('known_prefix_sha256')
        if (not isinstance(before,str) or len(before) != 64
                or any(c not in '0123456789abcdef' for c in before)
                or rows.get('known_prefix_after_append_sha256') != before
                or rows.get('known_prefix_bytes') != prefix*columns*8
                or rows.get('row_cache_bytes') != total*columns*8
                or rows.get('known_prefix_rewritten') is not False
                or rows.get('envelope_rows_start_index') != prefix
                or rows.get('current_full_point_sha256') != starting_geometry.get('current_full_point_sha256')
                or checked_scan.get('complete') is not True):
            raise ValueError('The measured original prefix and complete current coordinate cache must be retained')
        typed = rows.get('material_envelope_rows',{})
        selection = typed.get('selection',{})
        if (typed.get('source_sha256') != roles['envelope_rows']
                or typed.get('current_full_point_sha256') != rows['current_full_point_sha256']
                or typed.get('actual_model_identity_sha256') != report['model_identity_sha256']
                or typed.get('policy_identity_sha256') != canonical(expected)
                or typed.get('actual_appended_typed_count') != added
                or typed.get('actual_new_rows_sha256') != canonical(rows['rows'][prefix:])
                or typed.get('permanent_typed_rows_not_capped') is not True
                or typed.get('all_original_free_coordinates_retained') is not True
                or typed.get('original_common_slack_includes_all_appended_rows') is not True
                or typed.get('original_nonlinear_thresholds_unchanged') is not True
                or typed.get('continuous_geometry_certified') is not False
                or selection.get('new_near_active_row_cap') != cap
                or selection.get('active_band') != report.get('material_envelope_active_band')):
            raise ValueError('The complete appended typed rows need their own actual policy/source/point and full pullback')
        memory = module.validate_report_metadata(rows.get('material_envelope'),
            model_identity=report['model_identity_sha256'],carrier_sha256=report['observation_carrier_sha256'])
        if (memory.get('definition_identity_sha256') != canonical(expected)
                or typed.get('actual_permanent_typed_count') != memory['actual_separation_memory_count']):
            raise ValueError('The actual appended-row snapshot must retain the complete uncapped separation memory')
        return dict(source_sha256=roles['envelope_rows'],policy_identity_sha256=canonical(expected),
            current_full_point_sha256=rows['current_full_point_sha256'],
            measured_prefix_sha256=before,measured_prefix_unchanged=True,
            actual_appended_typed_count=added,
            actual_permanent_typed_count=typed['actual_permanent_typed_count'],
            actual_new_rows_sha256=typed['actual_new_rows_sha256'],
            actual_envelope_row_seconds=typed.get('elapsed_seconds'),
            selection=typed.get('selection'),continuous_geometry_certified=False)
    return binding,validate_scan,validate_rows
'''


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def checked(path, expected):
    raw=Path(path).read_bytes()
    if expected is None or hashlib.sha256(raw).hexdigest() != expected:
        raise ValueError('Bind the complete actual input source before derivation: '+str(path))
    return raw.decode()


def replace(text, old, new, count=1):
    if text.count(old) != count:
        raise ValueError('Counted full-source substitution mismatch: '+old[:120])
    return text.replace(old,new)


def literal(text, name):
    nodes=[n for n in ast.parse(text).body if isinstance(n,ast.Assign)
        and any(isinstance(t,ast.Name) and t.id == name for t in n.targets)]
    if len(nodes) != 1:
        raise ValueError('Exactly one complete assignment required: '+name)
    return ast.literal_eval(nodes[0].value)


def assign(text, name, value):
    nodes=[n for n in ast.parse(text).body if isinstance(n,ast.Assign)
        and any(isinstance(t,ast.Name) and t.id == name for t in n.targets)]
    if len(nodes) != 1:
        raise ValueError('Exactly one complete assignment required: '+name)
    n=nodes[0];lines=text.splitlines(keepends=True)
    lines[n.lineno-1:n.end_lineno]=[name+' = '+pprint.pformat(value,sort_dicts=False,width=110)+'\n']
    return ''.join(lines)


def function(text, name, transform):
    nodes=[n for n in ast.parse(text).body if isinstance(n,ast.FunctionDef) and n.name == name]
    if len(nodes) != 1:
        raise ValueError('Exactly one complete function required: '+name)
    n=nodes[0];lines=text.splitlines(keepends=True)
    lines[n.lineno-1:n.end_lineno]=[transform(''.join(lines[n.lineno-1:n.end_lineno]))]
    return ''.join(lines)



def thread_calls(body, names, *, keyword='envelope_check'):
    """Add one explicit pure-validator keyword without rewriting the other function text."""
    tree=ast.parse(body);raw=body.encode();lines=raw.splitlines(keepends=True)
    offsets=[0]
    for line in lines:offsets.append(offsets[-1]+len(line))
    patches=[]
    for node in ast.walk(tree):
        if isinstance(node,ast.Call) and isinstance(node.func,ast.Name) and node.func.id in names:
            if any(k.arg==keyword for k in node.keywords):
                raise ValueError('The full source already has a different envelope scope')
            begin=offsets[node.lineno-1]+node.col_offset
            end=offsets[node.end_lineno-1]+node.end_col_offset
            piece=raw[begin:end].decode()
            if not piece.endswith(')'):
                raise ValueError('Preserve the exact complete source call')
            patches.append((begin,end,(piece[:-1]+', '+keyword+'='+keyword+')').encode()))
    if not patches:
        raise ValueError('Expected actual pure geometry/direction calls are missing')
    ordered=sorted(patches)
    if any(a[1]>b[0] for a,b in zip(ordered,ordered[1:])):
        raise ValueError('Do not silently overwrite nested source-call patches')
    for begin,end,text in reversed(ordered):raw=raw[:begin]+text+raw[end:]
    return raw.decode()


def audit_functions(before, after, allowed):
    def bodies(text):
        return {n.name:ast.dump(n,include_attributes=False) for n in ast.parse(text).body
            if isinstance(n,ast.FunctionDef)}
    a,b=bodies(before),bodies(after)
    if not set(a) <= set(b):
        raise ValueError('An original complete function was lost')
    changed={key for key in a if a[key] != b[key]}
    if changed != set(allowed):
        raise ValueError('Unexpected complete-function changes: '+repr(changed))
    return dict(changed_original_functions=sorted(changed),
        unchanged_original_functions=len(a)-len(changed),
        added_functions=sorted(set(b)-set(a)))


def construct(parents):
    old_driver,old_launch,old_read=list(PARENT_SOURCE_PINS)
    driver=assign(parents[old_driver],'SCHEMA',REPORT_SCHEMA)
    pins=literal(driver,'SOURCE_PINS')
    for role,(name,source_sha) in ADDITIONAL_SOURCE_PINS.items():
        if (not isinstance(source_sha,str) or len(source_sha) != 64
                or any(c not in '0123456789abcdef' for c in source_sha)):
            raise ValueError('The envelope scientific source closure must be completely locked')
        pins[role]=('scripts/resume_20261126/'+name,source_sha)
    driver=assign(driver,'SOURCE_PINS',pins)
    driver=function(driver,'all_locations',lambda body:ALL_LOCATIONS.strip()+'\n')
    def parse(body):
        body=replace(body,
            "    p.add_argument('--manifest', type=Path, action='append', required=True)\n",
            "    p.add_argument('--manifest', type=Path, action='append', required=True)\n"
            "    p.add_argument('--material-envelope-binding', type=Path)\n"
            "    p.add_argument('--envelope-near-active-rows', type=int, default=32)\n")
        body=replace(body,
            "    a.manifest = [path.resolve() for path in a.manifest]\n",
            "    if a.envelope_near_active_rows < 1:\n"
            "        raise ValueError('The new whole-grid near-active candidate cap is positive and never caps separation memory')\n"
            "    if a.material_envelope_binding is not None:\n"
            "        a.material_envelope_binding = a.material_envelope_binding.resolve()\n"
            "    a.manifest = [path.resolve() for path in a.manifest]\n")
        return body
    driver=function(driver,'parse_args',parse)
    driver=replace(driver,
        "    history = load('_so3_complete_address_history', paths['history'])\n",
        "    history = load('_so3_complete_address_history', paths['history'])\n"
        "    envelope_memory = load('_so3_complete_material_envelope_memory',paths['envelope_memory'])\n")
    driver=replace(driver,
        "    witnesses, radius_witnesses, history_record = all_locations(\n"
        "        args, preparation, q, history, address_parent, address_parent_path)\n",
        "    witnesses, radius_witnesses, history_record, envelope = all_locations(\n"
        "        args, preparation, q, history, address_parent, address_parent_path,\n"
        "        envelope_memory=envelope_memory)\n")
    driver=replace(driver,
        "    screen = geometry_module.GeometryScreen(q, args.repo, budgets,\n",
        "    screen = geometry_module.GeometryScreen(q, args.repo, budgets,envelope=envelope,\n")
    driver=replace(driver,
        "        normal_frame_C1_source=file_record(paths['frame_C1']),\n",
        "        normal_frame_C1_source=file_record(paths['frame_C1']),\n"
        "        material_envelope_definition=envelope.definition,\n"
        "        material_envelope=envelope.metadata(),\n"
        "        material_envelope_source=file_record(paths['envelope_memory']),\n"
        "        material_envelope_rows_source=file_record(paths['envelope_rows']),\n"
        "        material_envelope_near_active_rows=args.envelope_near_active_rows,\n"
        "        material_envelope_active_band=args.active_band,\n"
        "        material_envelope_new_working_set_policy=True,\n"
        "        full_material_envelope_nonlinear_responsibility=True,\n"
        "        unknown_historical_protected_labels_reconstructed=False,\n"
        "        old_protected_required_priority_equivalence_claimed=False,\n")
    refresh="        report['material_envelope'] = envelope.metadata()\n"
    driver=replace(driver,
        "    def save_report():\n        report['latest_operator_metadata'] = q.metadata()\n",
        "    def save_report():\n        report['latest_operator_metadata'] = q.metadata()\n"+refresh)
    suffix=driver[driver.index('    def save_report():'):]
    if digest(replace(suffix,refresh,'')) != LOOP_SUFFIX_SHA:
        raise ValueError('Only the explicit envelope snapshot refresh may change the full original scientific loop')
    launch=assign(parents[old_launch],'DRIVER_SHA',digest(driver))
    launch=function(launch,'parse_args',parse)
    launch=replace(launch,old_driver,OUTPUT_NAMES['driver'])
    read=assign(parents[old_read],'DRIVER_SHA',digest(driver))
    read=assign(read,'REPORT_SCHEMA',REPORT_SCHEMA)
    read=replace(read,old_driver,OUTPUT_NAMES['driver'])
    read=replace(read,
        "schema='actual-complete-R711-reference-centred-C1-normal-plane-SO3-scalar-readout-v1'",
        "schema="+repr(READOUT_SCHEMA))
    read=replace(read,'def calibration_snapshot(',READER_ADDITION+'\ndef calibration_snapshot(')
    read=replace(read,
        "    frame_binding = frame_reuse_binding(report,model,roles,topic/load_pins(driver)['frame_C1'][0])\n",
        "    frame_binding = frame_reuse_binding(report,model,roles,topic/load_pins(driver)['frame_C1'][0])\n"
        "    envelope_binding,envelope_check,envelope_row_check = material_envelope_binding(topic,report,roles,driver)\n")
    read=replace(read,
        "        normal_frame_C1_binding=frame_binding,\n",
        "        normal_frame_C1_binding=frame_binding,\n"
        "        material_envelope_binding=envelope_binding,\n"
        "        material_envelope_diagnostics=envelope_binding['actual_metadata'],\n")
    def geometric(body):
        body=replace(body,'def geometric(value):','def geometric(value, *, envelope_check):')
        body=replace(body,"    complete = value.get('complete') is True\n",
            "    complete = value.get('complete') is True\n"
            "    scope = value.get('material_envelope')\n"
            "    checked_scope = envelope_check(scope)\n"
            "    if complete and (not isinstance(scope,dict) or scope.get('complete') is not True\n"
            "            or scope.get('current_full_point_sha256') != value.get('current_full_point_sha256')):\n"
            "        raise ValueError('A complete current scan needs its own complete material-envelope read')\n")
        body=replace(body,'    return result\n',
            "    result['material_envelope'] = checked_scope\n    return result\n")
        return body
    read=function(read,'geometric',geometric)
    def direction(body):
        body=replace(body,'def direction(value, profile):',
            'def direction(value, profile, *, envelope_check, envelope_row_check):')
        body=replace(body,"    rows = value['complete_selected_inequalities']\n",
            "    rows = value['complete_selected_inequalities']\n"
            "    checked_rows = envelope_row_check(rows,value.get('starting_geometry'))\n")
        body=replace(body,"        original_geometry_rows=rows['original_prefix_rows'],\n",
            "        material_envelope_rows=checked_rows,\n"
            "        original_geometry_rows=rows['original_prefix_rows'],\n")
        body=replace(body,
            "            or rows['original_prefix_rows']+rows['appended_amplitude_rows'] != rows['selected_rows']\n",
            "            or rows['original_prefix_rows']+rows['appended_amplitude_rows']+rows['appended_envelope_rows'] != rows['selected_rows']\n"
            "            or rows.get('known_geometry_and_amplitude_prefix_rows') != rows['original_prefix_rows']+rows['appended_amplitude_rows']\n"
            "            or rows.get('envelope_rows_start_index') != rows['known_geometry_and_amplitude_prefix_rows']\n"
            "            or rows.get('known_prefix_rewritten') is not False\n")
        body=replace(body,
            "        amplitude_rows=rows['appended_amplitude_rows'], total_rows=rows['selected_rows'],\n",
            "        amplitude_rows=rows['appended_amplitude_rows'], envelope_rows=rows['appended_envelope_rows'],\n"
            "        known_geometry_and_amplitude_prefix_rows=rows['known_geometry_and_amplitude_prefix_rows'],\n"
            "        known_prefix_bytes=rows['known_prefix_bytes'],known_prefix_rewritten=False,\n"
            "        total_rows=rows['selected_rows'],\n")
        return thread_calls(body,{'geometric'})
    read=function(read,'direction',direction)
    read=function(read,'read_report',lambda body:thread_calls(
        thread_calls(body,{'geometric','direction'}),{'direction'},keyword='envelope_row_check'))
    # The complete scan metadata is appended only after the independent geometry
    # has locked its exact scope keys; it may not be guessed by this derivation.
    generated={OUTPUT_NAMES['driver']:driver,OUTPUT_NAMES['launcher']:launch,OUTPUT_NAMES['reader']:read}
    audits=dict(driver=audit_functions(parents[old_driver],driver,('all_locations','parse_args','main')),
        launcher=audit_functions(parents[old_launch],launch,('parse_args','main')),
        reader=audit_functions(parents[old_read],read,('geometric','direction','read_report')))
    for name,text in generated.items():
        compile(text,name,'exec')
        if len(text.encode()) >= 100000:
            raise ValueError('Every complete published source stays below 100KB')
        if any(line.rstrip()!=line for line in text.splitlines()):
            raise ValueError('Trailing source whitespace')
    return generated,audits



READY_NAME = 'reference-centred-c1-material-envelope-normal-run07-ready.json'
BINDING_RELATIVE = 'run05-actual-observation-carrier-restored/material-envelope-carrier-binding.json'
BINDING_ACTUAL_SHA256 = 'aaa65a5ecac807e97cf771a08dd57d2ac26b48adf6acc9592025c0c706581c8e'
BINDING_PRODUCER_SHA256 = 'ef67425800ae9de626a7f8f48fd89deb125fbf0e4d6af72cf79741d1e254664e'
BINDING_REPORT_SHA256 = '926db461a4efce0fa40ab539b9df28143f8664cca25ec96e95ebe1d7aa83dcdf'


def construct_ready(parent_ready, generated, *, draft=False):
    """Complete real run07 parameters, with the proved new responsibility policy.

    The run05 ready is only a declared numeric/source ancestor. Its unavailable
    report paths are replaced by actual run07 P0 input plus complete envelope
    binding, never by fabricated empty records.
    """
    if digest(parent_ready) != READY_PARENT_SHA:
        raise ValueError('Use the complete corrected parameter/source ancestor')
    previous=json.loads(parent_ready)
    steps=copy.deepcopy(previous['steps'])
    if len(steps)!=2:
        raise ValueError('Preserve the complete scientific entry and pure attribution pair')
    source_directory='topics/visible-flex-larger-amplitude/scripts/resume_20261126/'
    old_output='reference-centred-c1-smooth-triangle-normal-lift-first'
    new_output='reference-centred-c1-material-envelope-normal-lift-first'
    manifest='{work}/axisymmetric-R690-reference-v2-first/locations.json'
    words=steps[0]['args'];kept=[];old_manifests=[]
    i=0
    while i<len(words):
        if words[i]=='--manifest':
            if i+1>=len(words):raise ValueError('Complete declared manifest argument required')
            old_manifests.append(words[i+1]);i+=2
        else:
            kept.append(words[i].replace(old_output,new_output));i+=1
    if manifest not in old_manifests:
        raise ValueError('The actual preparation location input must not be dropped')
    kept.extend(['--manifest',manifest,'--material-envelope-binding','{work}/'+BINDING_RELATIVE,
        '--envelope-near-active-rows','32'])
    steps[0]['args']=kept
    steps[0]['id']='complete-material-envelope-cached-normal-first-20261126-07'
    steps[0]['script']=source_directory+OUTPUT_NAMES['launcher']
    steps[0]['scope']=('Complete same fixed cached-centred normal field and original all-variable metric/Phase-I budgets, '
        'with a separately declared complete old/current literal material-envelope nonlinear responsibility. '
        'Known P0 original192/amplitude prefix is preserved; extra near-active and uncapped actual typed separation rows are explicit new policy. '
        'No unavailable run05 report, unknown protected ordering, old field value or certificate is fabricated.')
    steps[1]['id']='actual-material-envelope-cached-normal-first-20261126-07'
    steps[1]['script']=source_directory+OUTPUT_NAMES['reader']
    steps[1]['scope']=('Pure complete source/model/reference/C1/current-point attribution, all actual envelope scans, '
        'original+amplitude+envelope row equality, measured original prefix bytes and complete typed separation state; no F/J/root/integral.')
    for index,step in enumerate(steps):
        if index==1:step['args']=[w.replace(old_output,new_output) for w in step['args']]
        step['outputs']=[w.replace(old_output,new_output) for w in step['outputs']]
        step['summary']={name.replace(old_output,new_output):values for name,values in step['summary'].items()}
        if 'cleanup_generated_patterns' in step:
            step['cleanup_generated_patterns']=[w.replace(old_output,new_output) for w in step['cleanup_generated_patterns']]
    science=steps[0]['summary'][new_output+'/report.json']
    science.update(envelope_source='source_sha256_by_role.envelope_memory',
        envelope_rows_source='source_sha256_by_role.envelope_rows',
        envelope_policy='material_envelope.definition_identity_sha256',
        envelope_old_carrier='material_envelope.historical_address_binding.origin_carrier.record.sha256',
        envelope_current_carrier='material_envelope.current_carrier_sha256',
        envelope_radial_word_sets_equal='material_envelope.historical_address_binding.old_current_radial_word_sets_equal',
        envelope_old_current_arrays_read='material_envelope.historical_address_binding.old_and_current_entire_arrays_actually_read',
        envelope_current_radial_entries='material_envelope.implicit_grid.current_radial_entry_count',
        envelope_extra_radial='material_envelope.implicit_grid.extra_historical_radial_count',
        envelope_union_radial='material_envelope.implicit_grid.union_unique_radial_count',
        envelope_literal_angles='material_envelope.implicit_grid.angular_count',
        envelope_unique_material_locations='material_envelope.implicit_grid.unique_implicit_material_locations',
        envelope_initial_explicit_locations='material_envelope.known_explicit_history.initial_unique_locations',
        envelope_original_p0_preserved='material_envelope.known_explicit_history.complete_original_p0_preserved',
        envelope_complete_eleven_payloads='material_envelope.known_explicit_history.complete_eleven_payloads_preserved',
        envelope_scan_attempts='material_envelope.counters.scan_attempts',
        envelope_complete_scans='material_envelope.counters.complete_scans',
        envelope_incomplete_scans='material_envelope.counters.incomplete_scans',
        envelope_typed_memory='material_envelope.actual_separation_memory.count',
        envelope_typed_memory_hash='material_envelope.actual_separation_memory.sha256',
        envelope_working_row_builds='material_envelope.counters.working_row_builds',
        envelope_appended_rows_total='material_envelope.counters.appended_rows_total',
        envelope_near_active_cap='material_envelope_near_active_rows',
        envelope_unknown_protected_order_reconstructed='unknown_historical_protected_labels_reconstructed',
        envelope_old_required_priority_equivalence='old_protected_required_priority_equivalence_claimed',
        initial_envelope_complete='initial_geometry.material_envelope.complete',
        final_envelope_complete='final_geometry.material_envelope.complete')
    for phase in ('metric','restoration'):
        stem=phase+'_directions.0.complete_selected_inequalities.'
        for label,path in (('original_rows','original_prefix_rows'),('amplitude_rows','appended_amplitude_rows'),
                          ('envelope_rows','appended_envelope_rows'),('all_rows','selected_rows'),
                          ('prefix_bytes','known_prefix_bytes'),('prefix_sha','known_prefix_sha256'),
                          ('prefix_after_sha','known_prefix_after_append_sha256'),
                          ('prefix_rewritten','known_prefix_rewritten'),('row_cache_bytes','row_cache_bytes')):
            science[phase+'_'+label]=stem+path
    pure=steps[1]['summary']['postprocess/'+new_output+'-readout.json']
    pure.update(envelope_source='material_envelope_diagnostics.source_sha256',
        envelope_policy='material_envelope_diagnostics.definition_identity_sha256',
        envelope_old_carrier='material_envelope_diagnostics.historical_origin_carrier_sha256',
        envelope_current_carrier='material_envelope_diagnostics.current_carrier_sha256',
        envelope_extra_radial='material_envelope_diagnostics.implicit_grid.extra_historical_radial_count',
        envelope_union_radial='material_envelope_diagnostics.implicit_grid.union_unique_radial_count',
        envelope_material_locations='material_envelope_diagnostics.implicit_grid.unique_implicit_material_locations',
        envelope_scan_attempts='material_envelope_diagnostics.counters.scan_attempts',
        envelope_complete_scans='material_envelope_diagnostics.counters.complete_scans',
        envelope_incomplete_scans='material_envelope_diagnostics.counters.incomplete_scans',
        envelope_typed_memory='material_envelope_diagnostics.actual_separation_memory_count',
        envelope_typed_memory_hash='material_envelope_diagnostics.actual_separation_memory_sha256',
        envelope_responsibility='material_envelope_diagnostics.all_old_current_locations_in_permanent_nonlinear_responsibility',
        envelope_unknown_protected_order_reconstructed='material_envelope_diagnostics.unknown_historical_protected_order_reconstructed',
        initial_envelope_complete='initial_geometry.material_envelope.complete',
        final_envelope_complete='final_geometry.material_envelope.complete')
    for phase in ('metric','restoration'):
        stem='actual_'+phase+'_directions.0.'
        for label,path in (('alpha','accepted_alpha'),('qp_status','qp_status'),('qp_advances','actual_advances'),
                          ('qp_Pg','final_face_projected_gradient_norm'),('qp_tolerance','qp_tolerance'),
                          ('original_rows','original_geometry_rows'),('amplitude_rows','amplitude_rows'),
                          ('envelope_rows','envelope_rows'),('all_rows','total_rows'),
                          ('prefix_bytes','known_prefix_bytes'),('prefix_rewritten','known_prefix_rewritten'),
                          ('row_cache_bytes','row_cache_bytes'),
                          ('actual_typed_memory','material_envelope_rows.actual_permanent_typed_count'),
                          ('actual_row_seconds','material_envelope_rows.actual_envelope_row_seconds')):
            pure[phase+'_'+label]=stem+path
    runtime={Path(path).name:source_sha for path,source_sha in literal(generated[OUTPUT_NAMES['driver']],'SOURCE_PINS').values()}
    runtime.update({name:digest(text) for name,text in generated.items()})
    runtime['derive_reference_centred_material_envelope_entry.py']=digest(Path(__file__).read_text())
    return dict(schema='complete-material-envelope-cached-normal-run07-ready-v1',
        executed=False,entry_admitted_or_executed=False,unlocked_source_review_only=draft,
        complete_source_and_parameter_closure_ready=not draft,
        scope=steps[0]['scope'],source_sha256=runtime,
        source_construction_parent_sha256=PARENT_SOURCE_PINS,
        previous_complete_parameter_ready_sha256=READY_PARENT_SHA,
        original_numeric_field_and_QP_arguments_preserved=True,
        prior_parameter_file_is_not_a_claim_that_its_unavailable_history_reports_exist=True,
        actual_new_reference_sha256=None,actual_new_scalar_identity_sha256=None,
        current_reference_mathematical_identity_must_come_from_actual_complete_inputs=True,
        old_reference_byte_identity_or_mathematical_g_equivalence_assumed=False,
        origin_parameter_file_sha256=previous['origin_parameter_file_sha256'],
        origin_definition_sha256=previous['origin_definition_sha256'],
        material_envelope=dict(new_working_set_policy=True,
            complete_old_current_grid_nonlinear_responsibility=True,
            known_explicit_P0_prefix_preserved=True,original_amplitude_prefix_preserved=True,
            unknown_old_protected_tags_or_order_reconstructed=False,
            old_required_row_priority_equivalence_claimed=False,
            near_active_row_cap=32,actual_typed_separation_memory_capped=False,
            binding_relative_path=BINDING_RELATIVE,
            actual_run07_binding_sha256=BINDING_ACTUAL_SHA256,
            actual_binding_producer_sha256=BINDING_PRODUCER_SHA256,
            actual_binding_report_sha256=BINDING_REPORT_SHA256,
            consumer_rehashes_complete_origin_and_current_arrays=True,
            binding_true_flags_are_not_substitutes_for_complete_actual_array_reads=True,
            full_grid_is_not_a_continuous_certificate=True),
        required_existing_current_history_inputs=['axisymmetric-R690-reference-v2-first/locations.json'],
        unavailable_run05_report_paths_supplied=[],
        source_ancestor_manifests_not_read_or_claimed_present=old_manifests[1:],
        complete_original_eleven_payload_source_roles_required_to_be_actually_reconstructed=True,
        normal_selection=previous['normal_selection'],supported_seed=previous['supported_seed'],
        reference_centring=previous['reference_centring'],
        R714_same_graph_frame_and_independent_detached_values_retained=True,
        detached_stage_matrix_reuse_implemented=False,
        first_report_contains_actual_pending_envelope_state=True,
        each_save_refreshes_independent_actual_envelope_snapshot=True,
        original_scientific_suffix_after_removing_only_snapshot_refresh_sha256=LOOP_SUFFIX_SHA,
        original_entire_save_report_suffix_byte_identity_claimed=False,
        no_new_scientific_fixture_required_or_executed=True,
        scientific_execution_permitted_only_in_public_Actions=True,
        pure_reader_parent_is_actual_reference_not_conditional_final_bundle=True,
        steps=steps,scientific_outcome_inferred=False)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--parent-directory',type=Path)
    p.add_argument('--parent-ready',type=Path)
    p.add_argument('--dependencies-directory',type=Path,required=True)
    p.add_argument('--outdir',type=Path,required=True)
    p.add_argument('--verify-existing',action='store_true',
        help='Compare the entire already-generated sources and complete ready without rewriting them')
    args=p.parse_args()
    repo=args.repo.resolve();out=args.outdir.resolve()
    if out == repo or repo in out.parents:
        raise ValueError('All source construction remains in scratch')
    sources=repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261126'
    parentdir=sources if args.parent_directory is None else args.parent_directory
    parents={name:checked(parentdir/name,expected) for name,expected in PARENT_SOURCE_PINS.items()}
    for role,(name,expected) in ADDITIONAL_SOURCE_PINS.items():
        checked(args.dependencies_directory/name,expected)
    generated,audits=construct(parents)
    for name,text in generated.items():
        if digest(text) != EXPECTED_OUTPUT_SHA256[name]:
            raise ValueError('The full derived body differs from its locked output identity: '+name)
    out.mkdir(parents=True,exist_ok=True)
    ready_path=(repo/'topics/visible-flex-larger-amplitude/computations'/
        'reference-centred-c1-smooth-triangle-normal-full-history-run05-ready.json'
        if args.parent_ready is None else args.parent_ready)
    ready=construct_ready(checked(ready_path,READY_PARENT_SHA),generated,draft=False)
    artifacts=dict(generated)
    artifacts[READY_NAME]=json.dumps(ready,indent=2,ensure_ascii=False,allow_nan=False)+'\n'
    for name,text in artifacts.items():
        if args.verify_existing:
            if (out/name).read_bytes()!=text.encode():
                raise ValueError('The complete stored artifact differs from the full derivation: '+name)
        else:
            (out/name).write_text(text)
    print(json.dumps(dict(verify_existing=args.verify_existing,sources={name:dict(bytes=len(text.encode()),sha256=digest(text))
        for name,text in generated.items()},static_audits=audits,scientific_execution=False),indent=2))


if __name__ == '__main__':
    main()

