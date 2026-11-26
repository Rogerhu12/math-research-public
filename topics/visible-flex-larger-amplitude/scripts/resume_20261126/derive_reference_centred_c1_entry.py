#!/usr/bin/env python3
"""Pure complete-source derivation of the R714 cached R715 normal entry.

No scientific module is imported.  Every complete parent source and helper
is pinned before the counted substitutions; all generated bodies are emitted
in full and statically compiled.  The original optimization suffix is exact.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import pprint


PARENTS = {
    'reference_centred_smooth_triangle_calibration.py': 'a8e849068b12ffe2876c07ec2518947890c9f09614da2a9882b53e268e3ba873',
    'so3_reference_centred_smooth_triangle_normal_lift_operator.py': 'b2597012ec8ee063fabbb49a758b592d10f607de55ded3becaa8b62b6a50118d',
    'so3_reference_centred_smooth_triangle_normal_lift_geometry.py': '6536a71b9db5858d258ecdf71ada39611772f4ff28fe857887fef142386376cf',
    'fullclosed_reference_centred_smooth_triangle_normal_lift_so3_qp.py': '92233b4ffb0aaff1644e0c4bc9e7357a8eae37bd68e6d02ef0c6e0dcfbb31b81',
    'launch_reference_centred_smooth_triangle_normal_lift_so3_actions.py': '68a6979d35fe7a953975c5a191928668765ddde7b4018fc7a8dee353138475dc',
    'read_reference_centred_smooth_triangle_normal_lift_so3_report.py': '7fc213c108245cb2c555d573a52961fd07f1b941d85411e8e6e8d8c22f20a5bb',
}
HELPER_NAME = 'normal_frame_c1_reuse.py'
HELPER_SHA = 'ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9'
PARENT_READY = 'reference-centred-smooth-triangle-normal-full-history-run05-ready.json'
PARENT_READY_SHA = 'db99d87e07974848ac61b6b93bb294cb1fbeb28faf7187edc8f072ce6d8b8934'
READY_NAME = 'reference-centred-c1-smooth-triangle-normal-full-history-run05-ready.json'
OPERATOR_SCHEMA = 'complete-R711-reference-centred-C1-reuse-SO3-fixed-normal-plane-six-control-layer-v1'
REPORT_SCHEMA = 'complete-R711-reference-centred-C1-reuse-fixed-normal-plane-SO3-QP-v1'
SNAPSHOT_SCHEMA = 'actual-reference-centred-C1-normal-current-point-snapshot-v1'
LOOP_SUFFIX_SHA = '9b05f8e00c483491ffd9259b2d675af940c6f0b8a8104d6bfcd70ffb0e31b4ee'
EXPECTED_OUTPUT_SHA256 = {
    'normal_frame_c1_reuse.py': 'ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9',
    'reference_centred_c1_smooth_triangle_calibration.py': '3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991',
    'so3_reference_centred_c1_smooth_triangle_normal_lift_operator.py': 'a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd',
    'so3_reference_centred_c1_smooth_triangle_normal_lift_geometry.py': '353196a4faadc7537d04d6be139c9d9d8f47ee7e25e1f007e33588ac48cfa0ff',
    'fullclosed_reference_centred_c1_smooth_triangle_normal_lift_so3_qp.py': 'f075257aaea0930f60d905c9b02ac5cfcff61bc42d7daf337912c8a287d0f347',
    'launch_reference_centred_c1_smooth_triangle_normal_lift_so3_actions.py': '509daaab85537ae1a905eaab9f18e51b2b10a008eaf0a93714bbbe95e8782de5',
    'read_reference_centred_c1_smooth_triangle_normal_lift_so3_report.py': '8b5a638bbd8e5ec90489a512e0c734985c845d64d8de4745268d7ebc91639f2d',
}


READER_ADDITION = r'''
def read_frame_reuse_policy(path):
    """Evaluate only three explicitly selected stdlib policy/shape functions."""
    tree = ast.parse(Path(path).read_text())
    names = {'SCHEMA','ORIGINAL_CENTERED_SOURCE','METHOD_AST'}
    functions = {'sha','definition','_new_counts'}
    body = []
    seen_names,seen_functions = set(),set()
    for node in tree.body:
        if isinstance(node,ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0],ast.Name):
            name = node.targets[0].id
            if name in names:
                ast.literal_eval(node.value)
                body.append(node)
                seen_names.add(name)
        if isinstance(node,ast.FunctionDef) and node.name in functions:
            body.append(node)
            seen_functions.add(node.name)
    if seen_names != names or seen_functions != functions:
        raise ValueError('The complete source-bound C1 policy is not independently readable')
    namespace = {'Path':Path,'hashlib':hashlib,'__file__':str(path)}
    exec(compile(ast.Module(body=body,type_ignores=[]),'<bound pure C1 policy>','exec'),namespace)
    return namespace['definition'](),set(namespace['_new_counts']())


def frame_reuse_binding(report,model,roles,helper_path):
    if sha(helper_path) != roles['frame_C1']:
        raise ValueError('Bind the complete independent C1 helper bytes')
    expected,count_keys = read_frame_reuse_policy(helper_path)
    if (model.get('normal_frame_C1_reuse') != expected
            or report.get('normal_frame_C1_reuse_definition') != expected
            or report.get('normal_frame_C1_source',{}).get('sha256') != roles['frame_C1']
            or expected['source_sha256'] != roles['frame_C1']
            or expected['minimum_generic_full_batch_repetitions'] != 8
            or expected['complete_zero_control_jet_analytic_template_enabled'] is not True):
        raise ValueError('Keep the complete declared same-graph/zero-template policy and source')
    if (report.get('all_normal_stage_equations_and_matrices_retained_with_frame_reuse') is not True
            or report.get('frame_reuse_speedup_or_rounding_certified') is not False):
        raise ValueError('A frame cache may not delete stage equations or claim unobserved performance')
    return dict(definition=expected,definition_identity_sha256=canonical(expected),
        source_sha256=roles['frame_C1'],counter_keys=sorted(count_keys),
        all_original_outer_variables_and_all_normal_stages_retained=True,
        no_prior_plain_centred_scientific_run_required=True,
        actual_speedup_or_rounding_certificate=False)


def frame_reuse_metadata(value,model,roles,binding):
    actual = value.get('normal_frame_C1_reuse')
    if (not isinstance(actual,dict)
            or actual.get('schema') != binding['definition']['schema']
            or actual.get('source_sha256') != roles['frame_C1']
            or actual.get('definition') != binding['definition']
            or actual.get('actual_operator_source_sha256') != roles['endpoint']
            or actual.get('actual_model_identity_sha256') != canonical(model)):
        raise ValueError('The recorded C1 counters belong to another complete field or source')
    counter_keys = set(binding['counter_keys'])
    def counts(record):
        if (not isinstance(record,dict) or set(record) != counter_keys
                or any(type(v) is not int or v < 0 for v in record.values())):
            raise ValueError('Keep every actual nonnegative C1 counter, without missing-zero backfills')
        return dict(record)
    total = counts(actual.get('actual_counts'))
    for name in ('scopes_started','scopes_closed','value_scopes_started','value_scopes_closed'):
        if type(actual.get(name)) is not int or actual[name] < 0:
            raise ValueError('Keep actual integer scope counts')
    if (actual['scopes_closed'] > actual['scopes_started']
            or actual['value_scopes_closed'] > actual['value_scopes_started']):
        raise ValueError('More scopes cannot finish than were actually started')
    seconds = actual.get('scope_seconds')
    if (isinstance(seconds,bool) or not isinstance(seconds,(int,float))
            or not math.isfinite(seconds) or seconds < 0):
        raise ValueError('Keep actual finite elapsed time, not an assumed saving')
    for key in ('active_graphs_stored_in_kernel','duplicate_rate_or_acceleration_claimed',
            'complete_parameter_Hessian_supported','arithmetic_errors_enclosed'):
        if actual.get(key) is not False:
            raise ValueError('No stronger caching or numerical claim is authorized: '+key)
    for key in ('scope_seconds_include_the_owning_stage_chain',
            'scope_seconds_exclude_later_external_backward'):
        if actual.get(key) is not True:
            raise ValueError('Do not relabel the actual timing scope: '+key)
    summaries = {}
    for name,started in (('last_scope','scopes_started'),('last_value_scope','value_scopes_started')):
        record = actual.get(name)
        if record is None:
            summaries[name] = None
            continue
        if not isinstance(record,dict) or not isinstance(record.get('binding'),dict):
            raise ValueError('Keep the actual own-scope complete record or null')
        b = record['binding']
        if (b.get('actual_model_identity_sha256') != canonical(model)
                or b.get('normal_stage_count') != model['normal_stage_count']
                or b.get('angular_order') not in (1,2)
                or type(b.get('literal_angle_count')) is not int or b['literal_angle_count'] < 1
                or b.get('complete_control_jet_shape') != [b['literal_angle_count'],3,6]
                or type(b.get('scope_serial')) is not int
                or not 1 <= b['scope_serial'] <= actual[started]):
            raise ValueError('The full cached scope/shape/partition changed')
        for key in ('actual_full_free_point_sha256','literal_phi_words_sha256'):
            word = b.get(key)
            if not isinstance(word,str) or len(word) != 64 or any(c not in '0123456789abcdef' for c in word):
                raise ValueError('Keep the complete actual point/angle digest')
        current = counts(record.get('counts'))
        if any(v > total[k] for k,v in current.items()):
            raise ValueError('A recorded scope cannot exceed its cumulative actual counters')
        completed = record.get('stage_requests_completed')
        if (type(completed) is not int or not 0 <= completed <= model['normal_stage_count']
                or record.get('all_stage_frame_requests_completed') is not (completed == model['normal_stage_count'])
                or record.get('scientific_success_inferred') is not False):
            raise ValueError('A partial frame scope cannot imply a complete physical field')
        elapsed = record.get('scope_seconds')
        if (isinstance(elapsed,bool) or not isinstance(elapsed,(int,float))
                or not math.isfinite(elapsed) or elapsed < 0):
            raise ValueError('Keep the actual own-scope elapsed time')
        if name == 'last_scope':
            if (b.get('same_invocation_graph_only') is not True
                    or b.get('working_frames_anchored_by_original_stage') is not True
                    or record.get('graph_released_from_scope') is not True
                    or record.get('numerical_template_or_AD_rounding_enclosed') is not False):
                raise ValueError('The active C1 scope lost its full upstream/rounding contract')
        else:
            if (b.get('all_stage_roots_matrices_residual_rereads_and_trace_retained') is not True
                    or b.get('outer_parameter_derivatives_obtained_from_this_cache') is not False
                    or record.get('derivative_graph_borrowed_by_active_scope') is not False
                    or record.get('unexecuted_AD_reread_words_claimed_equal') is not False):
                raise ValueError('Detached numerical values cannot replace the active derivative chain')
        summaries[name] = dict(binding=b,counts=current,stage_requests_completed=completed,
            all_stage_frame_requests_completed=record['all_stage_frame_requests_completed'],
            scope_seconds=elapsed,
            point_is_current_metadata_point=b['actual_full_free_point_sha256']==value['current_full_point_sha256'],
            own_point_values_backfilled_from_current_point=False,
            optional_failures=record.get('template_failures',record.get('optional_cache_failures',[])))
    return dict(source_sha256=roles['frame_C1'],definition=binding['definition'],
        actual_counts=total,scopes_started=actual['scopes_started'],scopes_closed=actual['scopes_closed'],
        value_scopes_started=actual['value_scopes_started'],value_scopes_closed=actual['value_scopes_closed'],
        scope_seconds=seconds,**summaries,
        costs_include_failed_or_rejected_attempts=True,scope_records_keep_their_own_point=True,
        later_outer_backward_is_not_included_in_scope_timer=True,
        actual_speedup_or_rounding_certified=False,outer_parameter_Hessian_supported=False)

'''


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def checked(path, expected):
    raw = Path(path).read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected:
        raise ValueError('Changed complete parent source: '+str(path))
    return raw.decode()


def replace(text, old, new, count=1):
    if text.count(old) != count:
        raise ValueError('Counted full-source replacement mismatch: '+old[:120])
    return text.replace(old,new)


def assign(text, name, value):
    tree = ast.parse(text)
    found = [n for n in tree.body if isinstance(n,ast.Assign)
        and any(isinstance(t,ast.Name) and t.id == name for t in n.targets)]
    if len(found) != 1:
        raise ValueError('One complete assignment required: '+name)
    n = found[0]
    lines = text.splitlines(keepends=True)
    lines[n.lineno-1:n.end_lineno] = [name+' = '+pprint.pformat(value,sort_dicts=False,width=110)+'\n']
    return ''.join(lines)


def literal(text, name):
    nodes = [n for n in ast.parse(text).body if isinstance(n,ast.Assign)
        and any(isinstance(t,ast.Name) and t.id == name for t in n.targets)]
    if len(nodes) != 1:
        raise ValueError('One complete literal registry required: '+name)
    return ast.literal_eval(nodes[0].value)


def method(text, classname, name, transform):
    classes = [n for n in ast.parse(text).body if isinstance(n,ast.ClassDef) and n.name == classname]
    if len(classes) != 1:
        raise ValueError('One complete class required')
    nodes = [n for n in classes[0].body if isinstance(n,ast.FunctionDef) and n.name == name]
    if len(nodes) != 1:
        raise ValueError('One complete method required: '+name)
    node = nodes[0]
    first = min([node.lineno]+[d.lineno for d in node.decorator_list])
    lines = text.splitlines(keepends=True)
    original = ''.join(lines[first-1:node.end_lineno])
    lines[first-1:node.end_lineno] = [transform(original)]
    return ''.join(lines)


def function(text, name, transform):
    nodes = [n for n in ast.parse(text).body if isinstance(n,ast.FunctionDef) and n.name == name]
    if len(nodes) != 1:
        raise ValueError('One complete top-level function required: '+name)
    node = nodes[0]
    lines = text.splitlines(keepends=True)
    lines[node.lineno-1:node.end_lineno] = [transform(''.join(lines[node.lineno-1:node.end_lineno]))]
    return ''.join(lines)


def renamed(name):
    return name.replace('reference_centred_','reference_centred_c1_')


def audit_functions(before, after, classname, allowed):
    def functions(text):
        tree = ast.parse(text)
        body = tree.body if classname is None else next(n.body for n in tree.body
            if isinstance(n,ast.ClassDef) and n.name == classname)
        return {n.name:ast.dump(n,include_attributes=False) for n in body if isinstance(n,ast.FunctionDef)}
    a,b = functions(before),functions(after)
    if not set(a) <= set(b):
        raise ValueError('A complete original function was lost')
    changed = {name for name in a if a[name] != b[name]}
    if changed != set(allowed):
        raise ValueError('Unexpected full-function changes: '+repr(changed))
    return dict(changed_original_functions=sorted(changed),
        unchanged_original_functions=len(a)-len(changed),added_functions=sorted(set(b)-set(a)))


def construct(parents, helper):
    if digest(helper) != HELPER_SHA:
        raise ValueError('The complete R714 helper is immutable')
    generated = {HELPER_NAME:helper}
    old_cal,old_op,old_geo,old_driver,old_launch,old_read = list(PARENTS)
    cal = assign(parents[old_cal],'ENDPOINT_SCHEMA',OPERATOR_SCHEMA)
    generated[renamed(old_cal)] = cal
    cal_sha = digest(cal)

    op = assign(parents[old_op],'SCHEMA',OPERATOR_SCHEMA)
    op = assign(op,'REFERENCE_CENTERING_SOURCE_SHA256',cal_sha)
    op = replace(op,"JET_KEYS = ('F', 'Fs', 'Fphi', 'Fss', 'Fsphi', 'Fphiphi')",
        'FRAME_C1_SOURCE_SHA256 = '+repr(HELPER_SHA)+"\nJET_KEYS = ('F', 'Fs', 'Fphi', 'Fss', 'Fsphi', 'Fphiphi')")
    def init(body):
        body = replace(body,'reference_centering_module=None):','reference_centering_module=None, frame_c1_module=None):')
        marker='        self.reference_calibration = reference_centering_module.FrozenReferenceCalibration(\n'
        inserted=('        if (frame_c1_module is None or sha(frame_c1_module.__file__) != FRAME_C1_SOURCE_SHA256\n'
            '                or sha(frame_c1_module.definition.__code__.co_filename) != FRAME_C1_SOURCE_SHA256\n'
            '                or sha(frame_c1_module.NormalFrameC1Kernel.__init__.__code__.co_filename) != FRAME_C1_SOURCE_SHA256):\n'
            "            raise ValueError('Bind the entire same-graph C1/frame-value helper source')\n")
        body = replace(body,marker,inserted+marker)
        body = replace(body,'        self.model = dict(schema=SCHEMA, source_sha256=sha(__file__),\n',
            '        self.model = dict(schema=SCHEMA, source_sha256=sha(__file__),\n'
            '            normal_frame_C1_reuse=frame_c1_module.definition(),\n')
        body = replace(body,'        self.reference_calibration.bind_field(self.model,self.identity)\n',
            '        self.reference_calibration.bind_field(self.model,self.identity)\n'
            '        self.frame_c1 = frame_c1_module.NormalFrameC1Kernel(self)\n')
        return body
    op = method(op,'ZeroClosureOperator','__init__',init)
    def run_chain(body):
        body = replace(body,'        with torch.no_grad():\n',
            '        with torch.no_grad(), self.frame_c1.value_scope(data,keys,order) as frame_values:\n')
        return replace(body,'                frame[:,:order+1] = self._normal_frame_jets(previous,data,order)\n',
            '                frame[:,:order+1] = frame_values.frame(previous,index-1)\n')
    op = method(op,'ZeroClosureOperator','_run_chain',run_chain)
    def implicit(body):
        body = replace(body,'            frame_computed = self._normal_frame_jets(previous,data,order)\n',
            '            frame_computed = frame_scope.frame(previous,index)\n')
        marker='        for index in range(self.normal_stage_count):\n'
        start=body.index(marker)
        end=body.rindex('        return previous\n')
        loop=body[start:end]
        loop=''.join('    '+line if line.strip() else line for line in loop.splitlines(keepends=True))
        return body[:start]+'        with self.frame_c1.scope(x,data,phi,order,items) as frame_scope:\n'+loop+body[end:]
    op = method(op,'ZeroClosureOperator','_implicit_jet_value',implicit)
    op = method(op,'ZeroClosureOperator','metadata',lambda body:replace(body,
        '            reference_centering=self.reference_calibration.metadata(),\n',
        '            reference_centering=self.reference_calibration.metadata(),\n'
        '            normal_frame_C1_reuse=self.frame_c1.metadata(),\n'))
    generated[renamed(old_op)] = op
    op_sha = digest(op)

    geo = assign(parents[old_geo],'SCHEMA',
        'complete-R711-reference-centred-C1-normal-SO3-world-geometry-and-original-192-amplitude-rows-v1')
    geo = assign(geo,'OPERATOR_SCHEMA',OPERATOR_SCHEMA)
    geo = assign(geo,'ENDPOINT_SOURCE_SHA256',op_sha)
    geo = assign(geo,'REFERENCE_CENTERING_SOURCE_SHA256',cal_sha)
    geo = method(geo,'GeometryScreen','__init__',lambda body:replace(body,
        "        self.operator_sha256 = model['source_sha256']\n",
        "        policy = model.get('normal_frame_C1_reuse')\n"
        "        if (not isinstance(policy,dict) or policy != problem.frame_c1.definition\n"
        "                or policy.get('source_sha256') != "+repr(HELPER_SHA)+"\n"
        "                or policy.get('original_normal_stages_and_implicit_matrices_retained') is not True\n"
        "                or policy.get('original_stage_primal_frame_anchors_required') is not True\n"
        "                or policy.get('complete_second_outer_parameter_derivative_supported') is not False):\n"
        "            raise ValueError('The C1 cache must retain all stages, anchors and original free-point transposes')\n"
        "        self.operator_sha256 = model['source_sha256']\n"))
    generated[renamed(old_geo)] = geo
    geo_sha = digest(geo)

    driver = assign(parents[old_driver],'SCHEMA',REPORT_SCHEMA)
    driver = assign(driver,'ROOT_SNAPSHOT_SCHEMA',SNAPSHOT_SCHEMA)
    pins = literal(driver,'SOURCE_PINS')
    for role,name,dgst in (('endpoint',old_op,op_sha),('geometry',old_geo,geo_sha),
            ('reference_calibration',old_cal,cal_sha)):
        pins[role] = ('scripts/resume_20261126/'+renamed(name),dgst)
    pins['frame_C1'] = ('scripts/resume_20261126/'+HELPER_NAME,HELPER_SHA)
    driver = assign(driver,'SOURCE_PINS',pins)
    driver = replace(driver,"    calibration = load('_so3_complete_reference_centred_calibration',paths['reference_calibration'])\n",
        "    calibration = load('_so3_complete_reference_centred_calibration',paths['reference_calibration'])\n"
        "    frame_c1 = load('_so3_complete_same_graph_frame_C1',paths['frame_C1'])\n")
    driver = replace(driver,'        reference_centering_module=calibration)\n',
        '        reference_centering_module=calibration,frame_c1_module=frame_c1)\n')
    driver = replace(driver,"        reference_centering_source=file_record(paths['reference_calibration']),\n",
        "        reference_centering_source=file_record(paths['reference_calibration']),\n"
        "        normal_frame_C1_reuse_definition=q.frame_c1.definition,\n"
        "        normal_frame_C1_source=file_record(paths['frame_C1']),\n"
        "        all_normal_stage_equations_and_matrices_retained_with_frame_reuse=True,\n"
        "        frame_reuse_speedup_or_rounding_certified=False,\n")
    generated[renamed(old_driver)] = driver
    driver_sha = digest(driver)

    launch = assign(parents[old_launch],'DRIVER_SHA',driver_sha)
    launch = replace(launch,old_driver,renamed(old_driver))
    generated[renamed(old_launch)] = launch

    read = assign(parents[old_read],'DRIVER_SHA',driver_sha)
    read = assign(read,'REPORT_SCHEMA',REPORT_SCHEMA)
    read = assign(read,'OPERATOR_SCHEMA',OPERATOR_SCHEMA)
    read = assign(read,'ROOT_SNAPSHOT_SCHEMA',SNAPSHOT_SCHEMA)
    read = replace(read,old_driver,renamed(old_driver))
    read = replace(read,"schema='actual-complete-R711-reference-centred-normal-plane-SO3-scalar-readout-v1'",
        "schema='actual-complete-R711-reference-centred-C1-normal-plane-SO3-scalar-readout-v1'")
    read = replace(read,'def calibration_snapshot(',READER_ADDITION+'\ndef calibration_snapshot(')
    read = replace(read,'def endpoint_metadata(value, model, source_by_role, working_evaluation, supported):',
        'def endpoint_metadata(value, model, source_by_role, working_evaluation, supported, frame_binding):')
    read = replace(read,'        fixed_supported_unit_seed=seed_actual,reference_calibration=calibrated,\n',
        '        fixed_supported_unit_seed=seed_actual,reference_calibration=calibrated,\n'
        '        normal_frame_C1_reuse=frame_reuse_metadata(value,model,source_by_role,frame_binding),\n')
    read = replace(read,"    roles = report['source_sha256_by_role']\n",
        "    roles = report['source_sha256_by_role']\n"
        "    frame_binding = frame_reuse_binding(report,model,roles,topic/load_pins(driver)['frame_C1'][0])\n")
    # The one final full-metadata reader call retains its original current point.
    read = replace(read,'    endpoint = endpoint_metadata(metadata, model, roles, working, supported)\n',
        '    endpoint = endpoint_metadata(metadata, model, roles, working, supported, frame_binding)\n')
    read = replace(read,'        reference_centering=centered_binding,\n',
        '        reference_centering=centered_binding,\n'
        '        normal_frame_C1_binding=frame_binding,\n'
        "        normal_frame_C1_diagnostics=None if endpoint is None else endpoint['normal_frame_C1_reuse'],\n")
    generated[renamed(old_read)] = read

    audits = dict(calibration=audit_functions(parents[old_cal],cal,'FrozenReferenceCalibration',()),
        normal=audit_functions(parents[old_op],op,'ZeroClosureOperator',
            ('__init__','_run_chain','_implicit_jet_value','metadata')),
        geometry=audit_functions(parents[old_geo],geo,'GeometryScreen',('__init__',)),
        driver=audit_functions(parents[old_driver],driver,None,('main',)),
        launcher=audit_functions(parents[old_launch],launch,None,('main',)),
        reader=audit_functions(parents[old_read],read,None,('endpoint_metadata','read_report')))
    suffix=driver[driver.index('    def save_report():'):]
    if digest(suffix) != LOOP_SUFFIX_SHA:
        raise ValueError('The full physical optimization/Phase-I/line-screen loop was changed')
    for name,text in generated.items():
        compile(text,name,'exec')
        if len(text.encode()) >= 100000 or any(line.rstrip() != line for line in text.splitlines()):
            raise ValueError('Keep each full source under 100KB and without trailing whitespace: '+name)
        for node in ast.walk(ast.parse(text)):
            if isinstance(node,ast.Dict):
                keys=[k.value for k in node.keys if isinstance(k,ast.Constant) and isinstance(k.value,(str,int))]
                if len(keys) != len(set(keys)):
                    raise ValueError('Duplicate literal dictionary key')
            if isinstance(node,ast.Call):
                keys=[k.arg for k in node.keywords if k.arg is not None]
                if len(keys) != len(set(keys)):
                    raise ValueError('Duplicate explicit keyword')
    return generated,audits


def make_ready(value,generated):
    value=json.loads(json.dumps(value))
    replacements={name:renamed(name) for name in PARENTS}
    replacements.update({
        'reference-centred-smooth-triangle-normal-lift-first':'reference-centred-c1-smooth-triangle-normal-lift-first',
        'complete-r715-reference-centred-r711-normal-full-history-first-20261126-05':
            'complete-r714-reference-centred-c1-r711-normal-full-history-first-20261126-05',
        'actual-r715-reference-centred-r711-normal-full-history-first-20261126-05':
            'actual-r714-reference-centred-c1-r711-normal-full-history-first-20261126-05'})
    def walk(v):
        if isinstance(v,str):
            for old,new in replacements.items():v=v.replace(old,new)
            return v
        if isinstance(v,list):return [walk(x) for x in v]
        if isinstance(v,dict):return {walk(k):walk(x) for k,x in v.items()}
        return v
    value=walk(value)
    value['schema']='complete-R714-C1-cached-R715-R711-normal-full-history-run05-ready-v1'
    value['scope']=('Independent complete cached R715 field with R714 same-graph full C1 and zero-control '
        'analytic templates, plus strictly separate same-invocation no-grad frame values. Every original '
        'outer variable, all 32 common stages, original matrices/solves, full physical sixjet lift, '
        'all positive Gram/mean/cross rows, full 192-prefix/amplitude and Phase I remain.')
    value['history_scope']=('The same TEN actual source reports/locations are retained. The supported-unit '
        'seed report must really exist; no unexecuted plain R711 or plain centred report is required. '
        'If a direct successor or any other same-target scientific branch actually runs first, append '
        'its real complete report before admission (eleven histories for one such successor).')
    value['implementation_note']='notes/2026-11-26-R714-cached-reference-centred-complete-entry.md'
    value['R714_implementation_appendix']='notes/2026-11-26-R714-complete-frame-cache-and-zero-template-implementation.md'
    value['prior_plain_centred_ready_sha256']=PARENT_READY_SHA
    value['unexecuted_plain_centred_report_required']=False
    value['plain_centred_scientific_replay_required']=False
    value['complete_scientific_entry_executed']=False
    value['entry_admitted_or_executed']=False
    value['narrow_normal_cost_change']=dict(
        R714_C1_repeated_frame_cache_used=True,complete_zero_control_jet_analytic_template=True,
        no_grad_same_call_exact_word_value_cache=True,all_stage_roots_and_matrices_retained=True,
        active_upstream_graph_reattached_at_all_stages=True,outer_parameter_Hessian_supported=False,
        actual_speedup_claimed=False,working_reordering_bitwise_original_AD_claimed=False)
    driver=generated['fullclosed_reference_centred_c1_smooth_triangle_normal_lift_so3_qp.py']
    pins=literal(driver,'SOURCE_PINS')
    value['source_sha256']={Path(path).name:dgst for path,dgst in pins.values()}
    value['source_sha256'].update({name:digest(text) for name,text in generated.items()})
    value['source_sha256'][Path(__file__).name]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    count_functions=[node for node in ast.parse(generated[HELPER_NAME]).body
        if isinstance(node,ast.FunctionDef) and node.name == '_new_counts']
    if (len(count_functions) != 1 or len(count_functions[0].body) != 1
            or not isinstance(count_functions[0].body[0],ast.Return)):
        raise ValueError('Read every actual counter from the complete pinned helper')
    counter_call=count_functions[0].body[0].value
    if (not isinstance(counter_call,ast.Call) or not isinstance(counter_call.func,ast.Name)
            or counter_call.func.id != 'dict' or counter_call.args
            or any(item.arg is None or ast.literal_eval(item.value) != 0
                for item in counter_call.keywords)):
        raise ValueError('Only the complete literal counter registry is read by this pure derivation')
    names=tuple(item.arg for item in counter_call.keywords)
    for index,step in enumerate(value['steps']):
        step['scope']=value['scope'] if index == 0 else (
            'Pure complete source/model/current-point attribution with explicit same-graph and '
            'no-grad actual counters. No F/J, root, integral or scientific fixture is run.')
        for output,selectors in step.get('summary',{}).items():
            prefix=('latest_operator_metadata.normal_frame_C1_reuse.' if index == 0 else
                'normal_frame_C1_diagnostics.')
            for name in names:selectors['frame_C1_'+name]=prefix+'actual_counts.'+name
            for name in ('scopes_started','scopes_closed','value_scopes_started','value_scopes_closed','scope_seconds'):
                selectors['frame_C1_'+name]=prefix+name
    manifests=[value['steps'][0]['args'][i+1] for i,v in enumerate(value['steps'][0]['args']) if v=='--manifest']
    expected=['{work}/'+path for path in value['required_actual_history_reports']]
    if len(manifests) != 10 or set(manifests) != set(expected):
        raise ValueError('Keep all TEN real history arguments in this initial plan')
    if any('reference-centred-' in x or 'smooth-triangle-fixed-normal' in x for x in manifests):
        raise ValueError('An unexecuted plain field became a false scientific prerequisite')
    return value


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--parent-directory',type=Path)
    p.add_argument('--helper-source',type=Path)
    p.add_argument('--ready-source',type=Path)
    p.add_argument('--outdir',type=Path,required=True)
    args=p.parse_args()
    repo=args.repo.resolve();out=args.outdir.resolve()
    if out == repo or repo in out.parents:
        raise ValueError('Pure derivation outputs stay in an explicit scratch directory')
    source=repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261126'
    parents_directory=source if args.parent_directory is None else args.parent_directory
    parents={name:checked(parents_directory/name,expected) for name,expected in PARENTS.items()}
    helper=checked(source/HELPER_NAME if args.helper_source is None else args.helper_source,HELPER_SHA)
    ready_path=(repo/'topics/visible-flex-larger-amplitude/computations'/PARENT_READY
        if args.ready_source is None else args.ready_source)
    ready=json.loads(checked(ready_path,PARENT_READY_SHA))
    generated,audits=construct(parents,helper)
    if {name:digest(text) for name,text in generated.items()} != EXPECTED_OUTPUT_SHA256:
        raise ValueError('The complete reproduced output bytes differ from this published source closure')
    out.mkdir(parents=True,exist_ok=True)
    for name,text in generated.items():(out/name).write_text(text)
    parameter=make_ready(ready,generated)
    (out/READY_NAME).write_text(json.dumps(parameter,ensure_ascii=False,indent=2)+'\n')
    table=dict(schema='complete-R714-cached-R715-source-derivation-v1',
        derivation_source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        complete_parent_sources=PARENTS,helper_source_sha256=HELPER_SHA,
        sources={name:dict(bytes=len(text.encode()),sha256=digest(text)) for name,text in generated.items()},
        static_audits=audits,original_complete_driver_loop_suffix_sha256=LOOP_SUFFIX_SHA,
        all_scientific_modules_unimported=True,all_sources_written_complete=True,
        raw_scientific_execution_performed=False)
    (out/'reference-centred-c1-source-lock-table.json').write_text(json.dumps(table,indent=2)+'\n')
    print(json.dumps(table,sort_keys=True))


if __name__ == '__main__':
    main()
