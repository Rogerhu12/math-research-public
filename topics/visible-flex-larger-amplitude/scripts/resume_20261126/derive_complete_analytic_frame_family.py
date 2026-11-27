#!/usr/bin/env python3
"""Pure source-only derivation of the complete analytic-frame normal family."""
import argparse
import ast
import difflib
import hashlib
import json
from pathlib import Path

PARENT_RECORDS = {'analytic_normal_stage_jacobian.py': {'bytes': 24240,
                                       'sha256': '64b39a8be75ee976dbf4b49768e4ebaf37a372f77dba397a439a054cc4e7465d'},
 'analytic_j3_normal_frame_c1_reuse.py': {'bytes': 35625,
                                          'sha256': '8e6c3f255a6acbd27aa1291c1a8b0555eeaaeb869a58fde6a49b3fc5d16361f8'},
 'analytic_j3_detached_normal_stage_matrix_reuse.py': {'bytes': 47673,
                                                       'sha256': '5db725b423db4e97229a697ff6ce712b9183236070000e8ed66ed45cbe1767c1'},
 'analytic_j3_adjacent_normal_frame_matrices.py': {'bytes': 36734,
                                                   'sha256': '8a63cc1817fd0853c2b7ee69b64e3083de22106c239b62acc602ad9b69698787'},
 'reference_centred_analytic_j3_smooth_triangle_calibration.py': {'bytes': 11911,
                                                                  'sha256': '4c3fb7a6d19a9c214e2dc69428456b62bc406c8329bc60083e1f5f8be3ff3d6d'},
 'so3_reference_centred_analytic_j3_smooth_triangle_normal_lift_operator.py': {'bytes': 96906,
                                                                               'sha256': '04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e'},
 'analytic_j3_source_and_report_binding.py': {'bytes': 14308,
                                              'sha256': 'f34fcafc06b50594b7a651a90e38553ea8ae3da5b6ac8b6ca4ea691d2ab9f14f'},
 'transfer_material_envelope_memory_to_analytic_j3.py': {'bytes': 62891,
                                                         'sha256': '0d2a5e9c9f5651e149d53da859ac42ced1c3b44709f9a5a3416a82c8d8702608'},
 'so3_reference_centred_analytic_j3_material_envelope_geometry.py': {'bytes': 68945,
                                                                     'sha256': '781778dc41303e5c8555df46e774e74e6c96fe2fa4ab3cb2bc3d4d0dccaae50a'},
 'fullclosed_reference_centred_analytic_j3_material_envelope_so3_qp.py': {'bytes': 78907,
                                                                          'sha256': '0dfb96e53fa92e741e2d94819636486b45c49e341006370d1c6864ce70c36b51'},
 'launch_reference_centred_analytic_j3_material_envelope_so3_actions.py': {'bytes': 21366,
                                                                           'sha256': '6228512d27d54027edf6985b640d74edac9a79c8ddb5e386b0b064e362bdb797'},
 'read_reference_centred_analytic_j3_material_envelope_so3_report.py': {'bytes': 99527,
                                                                        'sha256': 'c2a6039633dbb397bdb6f56358153a362ed4e34c8e035a6a739eb23d5a1b785e'},
 'immutable_analytic_normal_root_packets_v2.py': {'bytes': 67095,
                                                  'sha256': '1e0656b19de4eb78937a9f8305569d7c1cce59f48614fb7a279738942bcd622e'}}
EXPECTED_RUNTIME = {'analytic_frame_adjacent_normal_matrices.py': {'bytes': 36761, 'sha256': '3788b809c986668042e1c02f927afb85bf45434c4ff69607f9aaa2e2bf142695'}, 'analytic_frame_c1_reuse.py': {'bytes': 35894, 'sha256': 'f1c74928089b60fb8f5350084ace0805fa956f4b06ac0de3f6a11357dd1aa2fb'}, 'analytic_frame_detached_normal_stage_matrix_reuse.py': {'bytes': 47775, 'sha256': 'fa06705ebe19153edf455151a19c4217e42b8ab81ae3ffa4c1815701ec135255'}, 'analytic_frame_local_stage_jacobian.py': {'bytes': 24261, 'sha256': '894efd3b277b8a8c1fbd4abcd68b573fb09ee10a706a90ded7b2e1894fe3b866'}, 'analytic_frame_source_and_report_binding.py': {'bytes': 20897, 'sha256': '78aada58801198f9d3e29696e88f8834658286686728ac8f1b9ab369f827d94f'}, 'analytic_normal_frame_jets.py': {'bytes': 33705, 'sha256': '4ed6dfb93bb15b864d79c227b852421bc69b888a32923b98a21fe816da5be3d8'}, 'fullclosed_reference_centred_analytic_frame_material_envelope_so3_qp.py': {'bytes': 80009, 'sha256': '55af1d0feadeec46aab81ce72c027fdc25a60bf17fa92a5ee1d02aa358821a06'}, 'immutable_analytic_frame_normal_root_packets.py': {'bytes': 69148, 'sha256': '094ca6a87213a8677b46aa9b0ad4c5a4b12f8c4c80437d7b640c47f7793b40f0'}, 'launch_reference_centred_analytic_frame_material_envelope_so3_actions.py': {'bytes': 21369, 'sha256': 'f429905e37a4dcb41a1cb6a70afb6d55c41ae9553b39ffe4fdfc3c8f753926cb'}, 'read_reference_centred_analytic_frame_material_envelope_so3_report.py': {'bytes': 97308, 'sha256': 'a9f4f27c46c1f870c276c35613ad71a1e411ac6e2d95556415b5daee31cb6a76'}, 'reference_centred_analytic_frame_smooth_triangle_calibration.py': {'bytes': 11921, 'sha256': 'fe422dbf2eac68bbc4f54e8fe290ba0e5d1b7a080f12f1d148cffe834957dba0'}, 'so3_reference_centred_analytic_frame_material_envelope_geometry.py': {'bytes': 68945, 'sha256': '755f9b7d2250f3d5dfa294ca9e862bf0bdf1786781747d3727e6ce5b750d9f60'}, 'so3_reference_centred_analytic_frame_smooth_triangle_normal_lift_operator.py': {'bytes': 96558, 'sha256': '3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc'}, 'transfer_material_envelope_memory_to_analytic_frame.py': {'bytes': 63666, 'sha256': 'a9eed46389ce5f4262d6547a10ec42b6200072b185bd747cbb3814c008d81842'}}
HELPER_SHA256 = '4ed6dfb93bb15b864d79c227b852421bc69b888a32923b98a21fe816da5be3d8'
NAMES = {
 'analytic_normal_stage_jacobian.py':'analytic_frame_local_stage_jacobian.py',
 'analytic_j3_normal_frame_c1_reuse.py':'analytic_frame_c1_reuse.py',
 'analytic_j3_detached_normal_stage_matrix_reuse.py':'analytic_frame_detached_normal_stage_matrix_reuse.py',
 'analytic_j3_adjacent_normal_frame_matrices.py':'analytic_frame_adjacent_normal_matrices.py',
 'reference_centred_analytic_j3_smooth_triangle_calibration.py':'reference_centred_analytic_frame_smooth_triangle_calibration.py',
 'so3_reference_centred_analytic_j3_smooth_triangle_normal_lift_operator.py':'so3_reference_centred_analytic_frame_smooth_triangle_normal_lift_operator.py',
 'analytic_j3_source_and_report_binding.py':'analytic_frame_source_and_report_binding.py',
 'transfer_material_envelope_memory_to_analytic_j3.py':'transfer_material_envelope_memory_to_analytic_frame.py',
 'so3_reference_centred_analytic_j3_material_envelope_geometry.py':'so3_reference_centred_analytic_frame_material_envelope_geometry.py',
 'fullclosed_reference_centred_analytic_j3_material_envelope_so3_qp.py':'fullclosed_reference_centred_analytic_frame_material_envelope_so3_qp.py',
 'launch_reference_centred_analytic_j3_material_envelope_so3_actions.py':'launch_reference_centred_analytic_frame_material_envelope_so3_actions.py',
 'read_reference_centred_analytic_j3_material_envelope_so3_report.py':'read_reference_centred_analytic_frame_material_envelope_so3_report.py',
 'immutable_analytic_normal_root_packets_v2.py':'immutable_analytic_frame_normal_root_packets.py',
}
OLD_OPERATOR_SCHEMA = 'complete-R711-reference-centred-analytic-J3-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1'
OPERATOR_SCHEMA = 'complete-R711-reference-centred-analytic-frame-and-J3-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1'
OLD_REPORT_SCHEMA = 'complete-R711-reference-centred-analytic-J3-independent-chart-material-envelope-fixed-normal-plane-SO3-QP-v1'
REPORT_SCHEMA = 'complete-R711-reference-centred-analytic-frame-independent-chart-material-envelope-fixed-normal-plane-SO3-QP-v1'
OLD_SNAPSHOT_SCHEMA = 'actual-reference-centred-analytic-J3-normal-current-point-snapshot-v1'
SNAPSHOT_SCHEMA = 'actual-reference-centred-analytic-frame-normal-current-point-snapshot-v1'
OLD_FRAME_AST = 'ee015776b374f6cdcf2711b49e2d25e5cfe78b38b3f7d3886d8596a21b1b0cfc'
FRAME_AST = '458f00cb02abc6d279cd4e45feedc21d3e3f34f9168dd497d1f090ad1bc2a8f5'
WRAPPER = '    def _normal_frame_jets(self, previous, data, order):\n        return self.analytic_normal_frame.frame(previous, data, order)\n'

def sha(value):
    return hashlib.sha256(value.encode() if isinstance(value,str) else value).hexdigest()

def literal(source,name):
    nodes=[node for node in ast.parse(source).body if isinstance(node,ast.Assign)
        and len(node.targets)==1 and isinstance(node.targets[0],ast.Name)
        and node.targets[0].id==name]
    if len(nodes)!=1:
        raise ValueError('Use one complete literal assignment: '+name)
    return ast.literal_eval(nodes[0].value)

def stable_literal(value):
    # ast.unparse keeps dict insertion order; explicitly sort every set.
    # Python hash randomization must never change a complete source SHA.
    tree=ast.parse(repr(value),mode='eval')
    for node in ast.walk(tree):
        if isinstance(node,ast.Set):
            node.elts.sort(key=lambda item:ast.dump(item,include_attributes=False))
    return ast.unparse(tree)

def set_assignment(source,name,value):
    tree=ast.parse(source)
    nodes=[node for node in tree.body if isinstance(node,ast.Assign)
        and len(node.targets)==1 and isinstance(node.targets[0],ast.Name)
        and node.targets[0].id==name]
    if len(nodes)!=1:raise ValueError('One assignment required: '+name)
    node=nodes[0];lines=source.splitlines(keepends=True)
    lines[node.lineno-1:node.end_lineno]=[name+' = '+stable_literal(value)+'\n']
    return ''.join(lines)

def replace(source,old,new,count=1):
    if source.count(old)!=count:
        raise ValueError('Exact replacement count differs: '+repr(old[:120])+' '+str(source.count(old)))
    return source.replace(old,new)

def replace_function(source,name,replacement,*,class_name=None):
    tree=ast.parse(source)
    body=tree.body if class_name is None else next(node.body for node in tree.body
        if isinstance(node,ast.ClassDef) and node.name==class_name)
    nodes=[node for node in body if isinstance(node,ast.FunctionDef) and node.name==name]
    if len(nodes)!=1:raise ValueError('One complete function required: '+name)
    node=nodes[0];lines=source.splitlines(keepends=True)
    lines[node.lineno-1:node.end_lineno]=[replacement.rstrip()+'\n']
    return ''.join(lines)

def get_function(source,name,*,class_name=None):
    tree=ast.parse(source)
    body=tree.body if class_name is None else next(node.body for node in tree.body
        if isinstance(node,ast.ClassDef) and node.name==class_name)
    node=next(node for node in body if isinstance(node,ast.FunctionDef) and node.name==name)
    return '\n'.join(source.splitlines()[node.lineno-1:node.end_lineno])+'\n'

def check_source(name,source):
    if len(source.encode())>=100000:raise ValueError('Keep each complete source below 100000 bytes: '+name)
    tree=ast.parse(source)
    compile(tree,name,'exec')
    for node in ast.walk(tree):
        if isinstance(node,ast.Dict):
            keys=[key.value for key in node.keys if isinstance(key,ast.Constant)
                and isinstance(key.value,(str,int,float))]
            if len(keys)!=len(set(keys)):raise ValueError('Duplicate dictionary key: '+name)
    if any(line.rstrip()!=line for line in source.splitlines()):
        raise ValueError('Trailing whitespace: '+name)

def derive(source_directory,helper_source):
    directory=Path(source_directory)
    parent={}
    for name,record in PARENT_RECORDS.items():
        raw=(directory/name).read_bytes()
        if len(raw)!=record['bytes'] or sha(raw)!=record['sha256']:
            raise ValueError('The complete source parent differs: '+name)
        parent[name]=raw.decode()
    helper=Path(helper_source).read_text()
    if sha(helper)!=HELPER_SHA256:raise ValueError('The complete new analytic-frame helper differs')
    check_source('analytic_normal_frame_jets.py',helper)
    outputs={'analytic_normal_frame_jets.py':helper}
    changes={}
    def put(old,new):
        name=NAMES[old];check_source(name,new);outputs[name]=new
        changes[name]=''.join(difflib.unified_diff(parent[old].splitlines(keepends=True),
            new.splitlines(keepends=True),fromfile=old,tofile=name))
        return sha(new)
    def current(source,*,names=True):
        # Complete CURRENT source aliases only. Historical parent-family
        # records are inserted after this pass and retain their original bytes.
        for old,new in NAMES.items():
            if names and old in source:source=source.replace(old,new)
            if new in outputs:
                source=source.replace(PARENT_RECORDS[old]['sha256'],sha(outputs[new]))
        source=source.replace(OLD_OPERATOR_SCHEMA,OPERATOR_SCHEMA)
        source=source.replace(OLD_REPORT_SCHEMA,REPORT_SCHEMA)
        source=source.replace(OLD_SNAPSHOT_SCHEMA,SNAPSHOT_SCHEMA)
        return source

    # Six complete lower sources. Every normal-frame wrapper guard changes
    # explicitly; mathematical AD/template/matrix bodies remain intact.
    old='analytic_normal_stage_jacobian.py'
    s=current(parent[old]).replace(OLD_FRAME_AST,FRAME_AST)
    s=set_assignment(s,'SCHEMA','complete-analytic-full-frame-working-Rodrigues-normal-plane-J3-v1')
    j3sha=put(old,s)
    old='analytic_j3_normal_frame_c1_reuse.py'
    s=current(parent[old]).replace(OLD_FRAME_AST,FRAME_AST)
    s=set_assignment(s,'SCHEMA','complete-analytic-full-frame-compatible-normal-frame-C1-reuse-v1')
    s=s.replace('original complete _normal_frame_jets under no_grad',
        'complete current analytic-frame producer or its full AD fallback under no_grad')
    s=replace(s,'        original_frame_and_active_template_methods_retained=True,',
        '        original_frame_and_active_template_methods_retained=False,\n'
        '        complete_current_frame_and_original_active_template_methods_retained=True,\n'
        "        original_frame_evaluations_counter_scope='complete current frame method calls, not asserted AD calls',")
    s=replace(s,"no_grad_value_scope='one complete original _run_chain; exact words; original AD on first read'",
        "no_grad_value_scope='one complete original _run_chain; exact words; current full analytic frame or its full AD fallback on first read'")
    s=replace(s,'optional_value_cache_copy_failure_uses_original_complete_frame=True,',
        'optional_value_cache_copy_failure_uses_current_complete_frame=True,')
    s=replace(s,'extra_template_failure_falls_back_to_original_full_frame=True,',
        'extra_template_failure_falls_back_to_current_full_frame=True,')
    c1sha=put(old,s)
    old='analytic_j3_detached_normal_stage_matrix_reuse.py'
    s=current(parent[old]).replace(OLD_FRAME_AST,FRAME_AST)
    s=set_assignment(s,'SCHEMA','complete-analytic-full-frame-compatible-same-call-detached-normal-stage-matrix-reuse-v1')
    s=replace(s,'original_nine_frame_helper_method_guards_unchanged=True,',
        'original_nine_frame_helper_method_guards_unchanged=False,\n'
        '        complete_current_frame_wrapper_guard_and_eight_original_method_guards_retained=True,')
    stagesha=put(old,s)
    old='analytic_j3_adjacent_normal_frame_matrices.py'
    s=current(parent[old]).replace(OLD_FRAME_AST,FRAME_AST)
    s=set_assignment(s,'SCHEMA','complete-analytic-full-frame-compatible-adjacent-total-angular-frame-normal-stage-matrices-v1')
    s=replace(s,"last_A_origin='one complete original no-grad _normal_frame_jets at actual final controls'",
        "last_A_origin='one complete current no-grad analytic frame or its full AD fallback at actual final controls'")
    adjsha=put(old,s)
    old='reference_centred_analytic_j3_smooth_triangle_calibration.py'
    s=current(parent[old])
    calsha=put(old,s)
    old='so3_reference_centred_analytic_j3_smooth_triangle_normal_lift_operator.py'
    s=current(parent[old])
    s=replace(s,"ANALYTIC_STAGE_SOURCE_SHA256 = '"+j3sha+"'",
        "ANALYTIC_STAGE_SOURCE_SHA256 = '"+j3sha+"'\nANALYTIC_FRAME_SOURCE_SHA256 = '"+HELPER_SHA256+"'")
    s=replace(s,'adjacent_matrix_module=None, analytic_stage_module=None):',
        'adjacent_matrix_module=None, analytic_stage_module=None, analytic_frame_module=None):')
    guard="""        if (analytic_frame_module is None
                or sha(analytic_frame_module.__file__) != ANALYTIC_FRAME_SOURCE_SHA256
                or sha(analytic_frame_module.definition.__code__.co_filename) != ANALYTIC_FRAME_SOURCE_SHA256
                or sha(analytic_frame_module.AnalyticNormalFrame.__init__.__code__.co_filename)
                    != ANALYTIC_FRAME_SOURCE_SHA256):
            raise ValueError('Bind the complete six-control analytic frame and original full AD fallback')
"""
    s=replace(s,'        self.reference_calibration = reference_centering_module.FrozenReferenceCalibration(',
        guard+'        self.reference_calibration = reference_centering_module.FrozenReferenceCalibration(')
    s=replace(s,'            analytic_stage_jacobian=analytic_stage_module.definition(),',
        '            analytic_stage_jacobian=analytic_stage_module.definition(),\n            analytic_normal_frame=analytic_frame_module.definition(),')
    s=replace(s,'        self.analytic_stage_jacobian = analytic_stage_module.AnalyticNormalStageJacobian(self)',
        '        self.analytic_stage_jacobian = analytic_stage_module.AnalyticNormalStageJacobian(self)\n        self.analytic_normal_frame = analytic_frame_module.AnalyticNormalFrame(self)')
    s=replace_function(s,'_normal_frame_jets',WRAPPER,class_name='ZeroClosureOperator')
    s=replace(s,'            analytic_stage_jacobian=self.analytic_stage_jacobian.metadata(),',
        '            analytic_stage_jacobian=self.analytic_stage_jacobian.metadata(),\n            analytic_normal_frame=self.analytic_normal_frame.metadata(),')
    normalsha=put(old,s)

    # Source-bound pure policies and complete parent model relation.
    old='analytic_j3_source_and_report_binding.py'
    s=current(parent[old])
    s=set_assignment(s,'SCHEMA','complete-analytic-full-frame-source-model-and-report-binding-v1')
    s=replace(s,'Pure complete source/model/report binding for the analytic local-J3 family.',
        'Pure complete source/model/report binding for the full analytic-frame and local-J3 family.')
    bindings=literal(s,'SOURCE_BINDINGS')
    bindings['analytic_frame']=('analytic_normal_frame_jets.py',HELPER_SHA256)
    s=set_assignment(s,'SOURCE_BINDINGS',bindings)
    keys=literal(s,'POLICY_KEYS');keys['analytic_frame']='analytic_normal_frame'
    s=set_assignment(s,'POLICY_KEYS',keys)
    constants=literal(s,'POLICY_CONSTANTS')
    constants['analytic_frame']={'SCHEMA','ENDPOINT_SCHEMA','BASE_SOURCE_SHA256',
        'PARENT_NORMAL_SOURCE_SHA256','ORIGINAL_FRAME_AST_SHA256','METHOD_AST',
        'COUNTER_KEYS','OBSERVED_COUNTER_KEYS'}
    s=set_assignment(s,'POLICY_CONSTANTS',constants)
    s=replace(s,"        if role=='analytic_J3':\n            functions|=",
        "        if role in ('analytic_J3','analytic_frame'):\n            functions|=")
    s=replace(s,"        if role=='analytic_J3':\n            result['actual_validator']=namespace['validate_metadata']",
        "        if role in ('analytic_J3','analytic_frame'):\n            result['actual_validator' if role=='analytic_J3' else 'frame_actual_validator']=namespace['validate_metadata']")
    # Explicitly add the complete 04f1/0dfb/c2a parent; do not relax old routes.
    oldnormal=PARENT_RECORDS['so3_reference_centred_analytic_j3_smooth_triangle_normal_lift_operator.py']['sha256']
    oldcal=PARENT_RECORDS['reference_centred_analytic_j3_smooth_triangle_calibration.py']['sha256']
    insertion="""    elif original=='%s':
        old_schema,old_calibration=%r,%r
        old_keys=['normal_frame_C1_reuse','detached_stage_matrix_reuse',
            'adjacent_normal_frame_matrices','analytic_stage_jacobian']
"""%(oldnormal,OLD_OPERATOR_SCHEMA,oldcal)
    marker="    else:\n        raise ValueError('This explicit transfer supports only its two whole declared parent families')"
    s=replace(s,marker,insertion+"    else:\n        raise ValueError('Use one of the three complete explicitly declared parent families')")
    # The legacy two branches retain their original policy checks. The new
    # branch binds every actual old J3-family definition under new role names.
    policy_lines=[]
    parent_policy_sources={
      'normal_frame_C1_reuse':('analytic_j3_normal_frame_c1_reuse.py','frame_parent_C1'),
      'detached_stage_matrix_reuse':('analytic_j3_detached_normal_stage_matrix_reuse.py','frame_parent_stage_matrices'),
      'adjacent_normal_frame_matrices':('analytic_j3_adjacent_normal_frame_matrices.py','frame_parent_adjacent_matrices'),
      'analytic_stage_jacobian':('analytic_normal_stage_jacobian.py','frame_parent_J3')}
    parent_constants=literal(parent[old],'POLICY_CONSTANTS')
    role_for_key={'normal_frame_C1_reuse':'frame_C1','detached_stage_matrix_reuse':'stage_matrices',
        'adjacent_normal_frame_matrices':'adjacent_matrices','analytic_stage_jacobian':'analytic_J3'}
    for key,(name,role) in parent_policy_sources.items():
        policy_lines.append(repr(key)+': ('+repr(name)+','+repr(PARENT_RECORDS[name]['sha256'])+','
            +stable_literal(parent_constants[role_for_key[key]])+','+repr(role)+')')
    replacement="    if original=="+repr(oldnormal)+":\n        original_policies={"+",\n            ".join(policy_lines)+"}\n"
    s=replace(s,"    for key,(name,digest,constants,role) in original_policies.items():",
        replacement+"    for key,(name,digest,constants,role) in original_policies.items():")
    s=s.replace('Strict cc0a/104e or 95559/f382 relation, after the whole original reader.',
        'Strict cc0a/104e, 95559/f382 or 0dfb/c2a relation after each complete original reader.')
    s=s.replace('only_explicit_source_schema_and_matrix_working_policy_fields_changed=True',
        'only_explicit_source_schema_and_frame_matrix_working_policy_fields_changed=True')
    # Keep the entire old J3 readout shape and append full new-frame validation.
    s=replace(s,"    validator=policies['actual_validator']",
        "    frame_expected=policies['analytic_normal_frame']\n"
        "    if (report.get('analytic_normal_frame_definition')!=frame_expected\n"
        "            or report.get('analytic_normal_frame_source',{}).get('sha256')!=roles['analytic_frame']\n"
        "            or report.get('analytic_normal_frame_full_six_columns_and_active_graph_retained') is not True\n"
        "            or report.get('analytic_normal_frame_speedup_or_rounding_certified') is not False):\n"
        "        raise ValueError('Bind the complete six-control derivative without borrowing a cost or certificate')\n"
        "    frame_validator=policies['frame_actual_validator']\n"
        "    validator=policies['actual_validator']")
    oldcall="                validator(value.get('analytic_stage_jacobian'),model=model,source_by_role=roles,\n                    current_full_point_sha256=value.get('current_full_point_sha256'))"
    newcall=oldcall+"\n                frame_validator(value.get('analytic_normal_frame'),model=model,source_by_role=roles,\n                    current_full_point_sha256=value.get('current_full_point_sha256'))"
    s=replace(s,oldcall,newcall,2)
    s=replace(s,"    actual=None\n","    actual=None\n    frame_actual=None\n")
    oldcall="        actual=validator(latest.get('analytic_stage_jacobian'),model=model,source_by_role=roles,\n            current_full_point_sha256=latest.get('current_full_point_sha256'))"
    s=replace(s,oldcall,oldcall+"\n        frame_actual=frame_validator(latest.get('analytic_normal_frame'),model=model,source_by_role=roles,\n            current_full_point_sha256=latest.get('current_full_point_sha256'))")
    s=replace(s,"        latest_actual_diagnostics=actual,",
        "        latest_actual_diagnostics=actual,\n"
        "        analytic_normal_frame=dict(source_sha256=roles['analytic_frame'],\n"
        "            actual_operator_source_sha256=roles['endpoint'],\n"
        "            actual_model_identity_sha256=canonical(model),definition=frame_expected,\n"
        "            definition_identity_sha256=canonical(frame_expected),\n"
        "            actual_bound_snapshot_count=count,actual_bound_full_metadata_count=metadata_count,\n"
        "            latest_actual_diagnostics=frame_actual,snapshot_values_backfilled_from_latest=False,\n"
        "            full_six_columns_and_all_upstream_J_retained=True,\n"
        "            current_scientific_values_recomputed=False),")
    # Move the entire unchanged cross-object chart proof from the near-100KB
    # reader to this complete pure module, not a weakened abbreviated copy.
    chart_function=get_function(parent['read_reference_centred_analytic_j3_material_envelope_so3_report.py'],
        'independent_chart_binding')
    s=s.rstrip()+'\n\n\n'+chart_function
    bindsha=put(old,s)

    # Packet: old registry entries remain literal; append the new full family.
    old='immutable_analytic_normal_root_packets_v2.py'
    s=parent[old]
    s=set_assignment(s,'SCHEMA','immutable-current-analytic-full-frame-normal-root-packets-v1')
    spec=repr(normalsha)+": dict(schema="+repr(OPERATOR_SCHEMA)+",\n"
    spec+="        base='6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865',\n"
    spec+="        adjacent="+repr(adjsha)+",calibration="+repr(calsha)+",\n"
    spec+="        analytic="+repr(j3sha)+",analytic_frame="+repr(HELPER_SHA256)+"),\n"
    s=replace(s,'NORMALS = {\n','NORMALS = {\n    '+spec)
    s=replace(s,"    if 'analytic' in spec:value['analytic_stage_jacobian']=q.analytic_stage_jacobian.counts",
        "    if 'analytic' in spec:value['analytic_stage_jacobian']=q.analytic_stage_jacobian.counts\n"
        "    if 'analytic_frame' in spec:value['analytic_normal_frame']=q.analytic_normal_frame.counts")
    marker="        self.partition=[str(v) for v in q.normal_step_nodes]"
    addition="""        self.analytic_frame_functions={}
        if 'analytic_frame' in self.spec:
            actual=q.analytic_normal_frame
            if (self.roles.get('analytic_frame')!=self.spec['analytic_frame']
                    or actual.definition!=q.model.get('analytic_normal_frame')
                    or actual.definition.get('source_sha256')!=self.spec['analytic_frame']):
                raise ValueError('Bind the complete actual analytic six-control frame source and model')
            for name in ('frame','metadata'):
                function=getattr(actual,name).__func__
                if sha(function.__code__.co_filename)!=self.spec['analytic_frame']:
                    raise ValueError('The actual full-frame producer/metadata source differs')
                self.analytic_frame_functions[name]=function
"""
    s=replace(s,marker,addition+marker)
    marker="            raise ValueError('Do not replace the bound actual analytic-J3 implementation during capture')"
    s=replace(s,marker,marker+"\n        if self.analytic_frame_functions and any(getattr(q.analytic_normal_frame,n).__func__ is not f\n"
        "                for n,f in self.analytic_frame_functions.items()):\n"
        "            raise ValueError('Do not replace the complete analytic-frame producer during capture')")
    marker="""            if ('analytic' in self.spec and metadata.get('analytic_stage_jacobian',{}).get(
                    'actual_counts')!=before['analytic_stage_jacobian']):
"""
    at=s.index(marker);end=s.index('\n',s.index('raise ',at))
    existing=s[at:end]
    s=replace(s,existing,existing+"\n            if ('analytic_frame' in self.spec and metadata.get('analytic_normal_frame',{}).get(\n"
        "                    'actual_counts')!=before['analytic_normal_frame']):\n"
        "                raise ValueError('Actual full-frame metadata must retain its own unchanged counters')")
    packetsha=put(old,s)

    # Complete source-to-source transfer, retaining all literal prior families.
    old='transfer_material_envelope_memory_to_analytic_j3.py'
    s=current(parent[old])
    s=set_assignment(s,'SCHEMA','strict-prior-envelope-transfer-or-independent-fixed-chart-analytic-frame-branch-v1')
    olddriver='fullclosed_reference_centred_analytic_j3_material_envelope_so3_qp.py'
    oldreader='read_reference_centred_analytic_j3_material_envelope_so3_report.py'
    prior="    "+repr(PARENT_RECORDS[olddriver]['sha256'])+": dict(\n"
    prior+="        report_schema="+repr(OLD_REPORT_SCHEMA)+",\n"
    prior+="        reader_sha256="+repr(PARENT_RECORDS[oldreader]['sha256'])+",\n"
    prior+="        reader_relative="+repr('scripts/resume_20261126/'+oldreader)+",\n"
    prior+="        operator_sha256="+repr(oldnormal)+",operator_schema="+repr(OLD_OPERATOR_SCHEMA)+",\n"
    prior+="        memory_sha256=CURRENT_MEMORY_SOURCE_SHA256),\n"
    s=replace(s,'PARENT_FAMILIES = {\n','PARENT_FAMILIES = {\n'+prior)
    s=s.replace('C1/detached/adjacent/analytic-J3 policies',
        'C1/detached/adjacent/analytic-J3/complete-six-control-frame policies')
    s=replace(s,'        same_frozen_current_target_95559_final_transfer_supported=True,',
        '        same_frozen_current_target_95559_final_transfer_supported=True,\n'
        '        complete_analytic_J3_0dfb_final_transfer_supported=True,')
    transfersha=put(old,s)

    old='so3_reference_centred_analytic_j3_material_envelope_geometry.py'
    s=current(parent[old])
    s=set_assignment(s,'SCHEMA','complete-reference-centred-analytic-frame-material-envelope-world-geometry-v1')
    s=replace(s,"policy.get('source_sha256') != 'ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9'",
        "policy.get('source_sha256') != "+repr(c1sha))
    geosha=put(old,s)

    # Complete current source map plus every historical source needed by the
    # third strict parent route. All original roles remain present.
    old='fullclosed_reference_centred_analytic_j3_material_envelope_so3_qp.py'
    s=current(parent[old])
    pins=literal(s,'SOURCE_PINS')
    pins['analytic_frame']=('scripts/resume_20261126/analytic_normal_frame_jets.py',HELPER_SHA256)
    parent_roles={'frame_parent_driver':olddriver,'frame_parent_reader':oldreader,
        'frame_parent_endpoint':'so3_reference_centred_analytic_j3_smooth_triangle_normal_lift_operator.py',
        'frame_parent_calibration':'reference_centred_analytic_j3_smooth_triangle_calibration.py',
        'frame_parent_J3':'analytic_normal_stage_jacobian.py',
        'frame_parent_C1':'analytic_j3_normal_frame_c1_reuse.py',
        'frame_parent_stage_matrices':'analytic_j3_detached_normal_stage_matrix_reuse.py',
        'frame_parent_adjacent_matrices':'analytic_j3_adjacent_normal_frame_matrices.py'}
    for role,name in parent_roles.items():
        pins[role]=('scripts/resume_20261126/'+name,PARENT_RECORDS[name]['sha256'])
    s=set_assignment(s,'SOURCE_PINS',pins)
    snapshot=literal(s,'ROOT_SNAPSHOT_KEYS')
    s=set_assignment(s,'ROOT_SNAPSHOT_KEYS',snapshot+('analytic_normal_frame',))
    s=replace(s,"    analytic_stage = load('_actual_complete_analytic_local_J3',paths['analytic_J3'])",
        "    analytic_stage = load('_actual_complete_analytic_local_J3',paths['analytic_J3'])\n"
        "    analytic_frame = load('_actual_complete_six_control_analytic_frame',paths['analytic_frame'])")
    s=replace(s,'        adjacent_matrix_module=adjacent_matrices,analytic_stage_module=analytic_stage)',
        '        adjacent_matrix_module=adjacent_matrices,analytic_stage_module=analytic_stage,\n'
        '        analytic_frame_module=analytic_frame)')
    s=replace(s,'        analytic_stage_J3_speedup_or_rounding_certified=False,',
        '        analytic_stage_J3_speedup_or_rounding_certified=False,\n'
        '        analytic_normal_frame_definition=q.analytic_normal_frame.definition,\n'
        "        analytic_normal_frame_source=file_record(paths['analytic_frame']),\n"
        '        analytic_normal_frame_full_six_columns_and_active_graph_retained=True,\n'
        '        analytic_normal_frame_speedup_or_rounding_certified=False,')
    driversha=put(old,s)
    old='launch_reference_centred_analytic_j3_material_envelope_so3_actions.py'
    s=current(parent[old]);launchsha=put(old,s)
    old='read_reference_centred_analytic_j3_material_envelope_so3_report.py'
    s=current(parent[old])
    snapshot=literal(s,'ROOT_SNAPSHOT_KEYS')
    s=set_assignment(s,'ROOT_SNAPSHOT_KEYS',snapshot+('analytic_normal_frame',))
    s=replace_function(s,'independent_chart_binding','')
    s=replace(s,'def extra_bindings(report,topic,driver):','def extra_bindings(report,topic,driver,envelope_binding):')
    marker="        fn=getattr(module,function)\n"
    s=replace(s,marker,marker+"        if role=='analytic_J3_binding':\n"
        "            chart=module.independent_chart_binding\n"
        "            if sha(chart.__code__.co_filename)!=expected:raise ValueError('Changed complete chart binding')\n"
        "            answer['independent_fixed_target']=chart(report,envelope_binding)\n")
    s=replace(s,"    independent_target=independent_chart_binding(report,envelope_binding)\n"
        "    extra=extra_bindings(report,topic,driver)",
        "    extra=extra_bindings(report,topic,driver,envelope_binding)\n"
        "    independent_target=extra['independent_fixed_target']")
    s=replace(s,"        reference_centering=centered_binding,analytic_stage_jacobian=extra['analytic_J3_binding'],",
        "        reference_centering=centered_binding,analytic_stage_jacobian=extra['analytic_J3_binding'],\n"
        "        analytic_normal_frame=extra['analytic_J3_binding']['analytic_normal_frame'],")
    s=s.replace('actual-complete-R711-reference-centred-analytic-J3-packet-envelope-SO3-scalar-readout-v1',
        'actual-complete-R711-reference-centred-analytic-frame-packet-envelope-SO3-scalar-readout-v1')
    readersha=put(old,s)
    if not set(literal(parent[olddriver],'SOURCE_PINS'))<=set(pins):
        raise ValueError('A prior complete role was removed')
    # The driver science suffix, including the two old readonly packet hooks,
    # is unchanged byte-for-byte after the complete setup.
    suffix='    def save_report('
    if outputs[NAMES[olddriver]][outputs[NAMES[olddriver]].index(suffix):] != parent[olddriver][parent[olddriver].index(suffix):]:
        raise ValueError('The complete original scientific suffix changed')
    # Cross-object chart proof moved literally to the small binding module.
    if get_function(outputs[NAMES['analytic_j3_source_and_report_binding.py']],'independent_chart_binding') != chart_function:
        raise ValueError('The complete cross-object chart validation was altered while moving')
    if set(outputs)!=set(EXPECTED_RUNTIME):
        raise ValueError('The complete fourteen-source output set changed')
    for name,text in outputs.items():
        actual=dict(bytes=len(text.encode()),sha256=sha(text))
        if actual!=EXPECTED_RUNTIME[name]:
            raise ValueError('The complete independently locked source output differs: '+name)
    return outputs,changes,pins

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-directory',required=True,type=Path)
    parser.add_argument('--helper-source',required=True,type=Path)
    parser.add_argument('--out',required=True,type=Path)
    parser.add_argument('--verify-existing',action='store_true')
    args=parser.parse_args()
    outputs,changes,pins=derive(args.source_directory,args.helper_source)
    args.out.mkdir(parents=True,exist_ok=True)
    records=[]
    for name,text in outputs.items():
        path=args.out/name;raw=text.encode()
        if args.verify_existing:
            if path.read_bytes()!=raw:raise ValueError('Complete generated bytes differ: '+name)
        else:path.write_bytes(raw)
        records.append(dict(filename=name,bytes=len(raw),sha256=sha(raw)))
    report=dict(schema='complete-analytic-frame-source-family-reproduction-v1',
        source_sha256=sha(Path(__file__).read_bytes()),scientific_modules_imported=False,
        scientific_computations_executed=False,complete_byte_reproduction=True,
        original_source_roles_retained=True,full_source_role_count=len(pins),
        complete_old_scientific_suffix_including_readonly_packet_hooks_unchanged=True,
        cross_object_chart_validation_moved_byte_identically_to_complete_small_binding=True,
        runtime=records,source_pins=pins)
    if not args.verify_existing:
        (args.out/'source-reproduction.json').write_text(json.dumps(report,indent=2)+'\n')
        for name,diff in changes.items():(args.out/(name+'.diff')).write_text(diff)
    print(json.dumps(report,indent=2))

if __name__=='__main__':
    main()

