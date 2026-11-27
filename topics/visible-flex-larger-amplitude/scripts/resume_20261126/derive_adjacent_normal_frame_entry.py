#!/usr/bin/env python3
"""Pure full-source derivation of the independent adjacent-frame entry.

Only standard-library source parsing, literal replacement, hashes and
compilation occur here.  This program neither imports nor runs science.
The entire preceding matrix-cache package remains immutable.
"""
import argparse
import ast
import hashlib
from pathlib import Path
import pprint
import py_compile
import json


PARENT = {
 'reference_centred_stage_cached_smooth_triangle_calibration.py':'803ff897445b390ec2ba96ed84a0c7598d49ff9756e38077556074d025cce15d',
 'so3_reference_centred_stage_cached_smooth_triangle_normal_lift_operator.py':'d461f660063bfa2aeecc724050d71c6ef98143b9129f7cfe34f22e4043488a7f',
 'so3_reference_centred_stage_cached_material_envelope_geometry.py':'bdf212da59c48dfdee86160178e4b8f91177796f4a62fca7f4a1ce9510b9a9f5',
 'transfer_material_envelope_memory.py':'d5e74a6ee160e7ee5a70f53fb96b497e2ff1eacef070757f32ccf8d9226da3eb',
 'fullclosed_reference_centred_stage_cached_material_envelope_so3_qp.py':'1d1530c3a613d5b0721470139bce338ba950eaf561f51f921b562fb774cbedb2',
 'launch_reference_centred_stage_cached_material_envelope_so3_actions.py':'0625733b252205e20e98c53b372bfaf27fdae5cd421c6b38551a9d538d1025e5',
 'read_reference_centred_stage_cached_material_envelope_so3_report.py':'954721008b83c8550b4e0016cf0ec5351e46572dcccccca96f20b180f3cb5f0b',
}
NAMES = {
 name:(name.replace('stage_cached','adjacent_frame') if name!='transfer_material_envelope_memory.py'
       else 'transfer_material_envelope_memory_to_adjacent_frames.py') for name in PARENT}
OLD_OPERATOR_SCHEMA='complete-R711-reference-centred-C1-stage-matrix-reuse-SO3-fixed-normal-plane-six-control-layer-v1'
OPERATOR_SCHEMA='complete-R711-reference-centred-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1'
OLD_DRIVER_SCHEMA='complete-R711-reference-centred-stage-matrix-reuse-material-envelope-fixed-normal-plane-SO3-QP-v1'
DRIVER_SCHEMA='complete-R711-reference-centred-adjacent-frame-material-envelope-fixed-normal-plane-SO3-QP-v1'
OLD_READ_SCHEMA='actual-complete-R711-reference-centred-stage-matrix-reuse-material-envelope-normal-plane-SO3-scalar-readout-v1'
READ_SCHEMA='actual-complete-R711-reference-centred-adjacent-frame-material-envelope-normal-plane-SO3-scalar-readout-v1'
HELPER_NAME='adjacent_normal_frame_matrices.py'
MEMORY_NAME='complete_material_envelope_memory_current_restorer.py'
MEMORY_PARENT_SHA='c79c7f7ec1febf0ab6dca30d28a91b1566745972342c7336a3a9a106f56b3152'
CURRENT_RESTORER_SHA='8c1e2d8f71bb08b33f99f9c187dbed2994776fc64b7114e1cea921a4fecff449'


def sha(value):
    return hashlib.sha256(value.encode() if isinstance(value,str) else value).hexdigest()


def once(source,old,new):
    if source.count(old)!=1:
        raise ValueError('Expected exactly one complete source phrase: '+repr(old[:110]))
    return source.replace(old,new,1)


def assignment(source,name,value):
    tree=ast.parse(source)
    found=[n for n in tree.body if isinstance(n,ast.Assign) and len(n.targets)==1
        and isinstance(n.targets[0],ast.Name) and n.targets[0].id==name]
    if len(found)!=1:raise ValueError('Expected one full literal assignment: '+name)
    old=ast.get_source_segment(source,found[0])
    return once(source,old,name+' = '+pprint.pformat(value,width=100,sort_dicts=False))


def literals(source):
    answer={}
    for node in ast.parse(source).body:
        if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name):
            try:answer[node.targets[0].id]=ast.literal_eval(node.value)
            except (ValueError,TypeError):pass
    return answer


def methods(source,cls):
    classes=[n for n in ast.parse(source).body if isinstance(n,ast.ClassDef) and n.name==cls]
    if len(classes)!=1:raise ValueError('Expected one complete class '+cls)
    return {n.name:ast.dump(n,include_attributes=False) for n in classes[0].body if isinstance(n,ast.FunctionDef)}


def common(source):
    for old,new in ((OLD_OPERATOR_SCHEMA,OPERATOR_SCHEMA),(OLD_DRIVER_SCHEMA,DRIVER_SCHEMA),
                    (OLD_READ_SCHEMA,READ_SCHEMA)):
        source=source.replace(old,new)
    for old,new in NAMES.items():source=source.replace(old,new)
    return source


def independent_memory_mode(source):
    """Add an explicit fresh branch without weakening the terminal-transfer path."""
    source=assignment(source,'SCHEMA','strict-prior-envelope-transfer-or-explicit-independent-adjacent-branch-v1')
    source=once(source,'        fresh_entry_requires_actual_terminal_prior_envelope_report=True,',
        "        fresh_entry_requires_actual_terminal_prior_envelope_report=False,\n"
        "        default_strict_entry_requires_actual_terminal_prior_envelope_report=True,\n"
        "        explicit_independent_branch_uses_original_full_P0_and_both_material_grids=True,\n"
        "        independent_branch_uses_frozen_original_reference_free_point=True,\n"
        "        pending_peer_values_or_typed_priority_inherited=False,\n"
        "        actual_later_peer_addresses_and_typed_memory_remain_a_binding_and_merge_obligation=True,")
    marker="    if not paths and restart is None:\n        raise ValueError('A fresh matrix-reuse continuation requires its actual prior envelope report')"
    source=once(source,marker,"""    independent=getattr(args,'independent_envelope_branch',False)
    pending=list(getattr(args,'pending_parallel_envelope_run',[]))
    if (type(independent) is not bool or len(pending)!=len(set(pending))
            or any(not isinstance(v,str) or len(v.split('/'))!=2
                or any(not w.isdigit() or int(w)<1 or str(int(w))!=w for w in v.split('/')) for v in pending)):
        raise ValueError('Use explicit canonical run/attempt identities for unread parallel obligations')
    if independent and (paths or restart is not None or source_report_path is not None
            or any(getattr(args,key,None) is not None for key in ('restart_checkpoint',
                'restart_report','seed_so3_checkpoint','seed_so3_report',
                'material_envelope_seed_checkpoint','material_envelope_seed_report'))):
        raise ValueError('An independent fresh branch uses the original reference, without an unknown prior final')
    if pending and not independent:
        raise ValueError('Pending peer declarations belong only to the explicit independent fresh branch')
    if not paths and restart is None and not independent:
        raise ValueError('The default strict continuation still requires its actual prior terminal report')""")
    marker='    initial_rows = envelope.separation_rows()'
    source=once(source,marker,"""    branch_origin=(None if prior_transfer is None else copy.deepcopy(prior_transfer.get('independent_branch_origin')))
    if independent:
        branch_origin=dict(schema='explicit-independent-complete-material-envelope-origin-v1',
            actual_origin_model_identity_sha256=q.identity,
            actual_origin_driver_sha256=caller_record['sha256'],
            actual_origin_carrier_sha256=current_carrier_sha,
            frozen_original_reference_point_sha256=q.reference_point_sha256,
            original_complete_memory_source_sha256=MEMORY_SOURCE_SHA256,
            complete_original_P0_and_old_current_G_responsibility=True,
            independent_initial_point_is_original_reference=True,
            pending_parallel_runs=pending,pending_parallel_driver_sha256=ORIGINAL_DRIVER_SHA256,
            pending_parallel_terminal_reports_read=False,
            pending_parallel_final_or_typed_discovery_words_inherited=False,
            later_actual_addresses_and_typed_memory_require_bound_merge=True,
            unknown_typed_priority_equivalence_claimed=False)
"""+marker)
    marker='        actual_parent_reports=parent_records,'
    source=once(source,marker,marker+"\n        independent_branch_origin=branch_origin,\n"
        "        current_invocation_memory_mode=('explicit-independent-branch' if independent else\n"
        "            'same-source-restart' if restart is not None else 'strict-terminal-transfer'),")
    marker="    if not isinstance(parents,list) or not parents:\n        raise ValueError('Preserve the actual predecessor evidence through every same-source restart')"
    source=once(source,marker,"""    if not isinstance(parents,list):
        raise ValueError('Preserve every actual predecessor evidence list')
    branch=value.get('independent_branch_origin')
    mode=value.get('current_invocation_memory_mode')
    if mode not in ('explicit-independent-branch','same-source-restart','strict-terminal-transfer'):
        raise ValueError('State the actual independent, restart or strict-terminal mode')
    if branch is not None:
        if (not isinstance(branch,dict)
                or branch.get('schema')!='explicit-independent-complete-material-envelope-origin-v1'
                or branch.get('actual_origin_model_identity_sha256')!=canonical(model)
                or branch.get('actual_origin_driver_sha256')!=caller_source_sha256
                or branch.get('actual_origin_carrier_sha256')!=carrier_sha256
                or branch.get('frozen_original_reference_point_sha256')
                    !=model['reference_centering_definition']['original_reference_point_sha256']
                or branch.get('original_complete_memory_source_sha256')!=MEMORY_SOURCE_SHA256
                or branch.get('pending_parallel_driver_sha256')!=ORIGINAL_DRIVER_SHA256):
            raise ValueError('Bind the complete actual independent branch and frozen original reference')
        for key in ('complete_original_P0_and_old_current_G_responsibility',
                'independent_initial_point_is_original_reference','later_actual_addresses_and_typed_memory_require_bound_merge'):
            if branch.get(key) is not True:raise ValueError('Independent responsibility is incomplete: '+key)
        for key in ('pending_parallel_terminal_reports_read',
                'pending_parallel_final_or_typed_discovery_words_inherited','unknown_typed_priority_equivalence_claimed'):
            if branch.get(key) is not False:raise ValueError('Unknown parallel state was promoted: '+key)
        pending=branch.get('pending_parallel_runs')
        if (not isinstance(pending,list) or len(pending)!=len(set(pending))
                or any(not isinstance(v,str) or len(v.split('/'))!=2
                    or any(not w.isdigit() or int(w)<1 or str(int(w))!=w for w in v.split('/')) for v in pending)):
            raise ValueError('Keep canonical declared unread peer run identities, not fabricated reports')
    elif not parents or mode=='explicit-independent-branch':
        raise ValueError('A strict branch still needs complete actual terminal predecessor evidence')""")
    marker="    if restart is None:\n        if count == 0 or value.get('prior_transfer_identity_sha256') is not None:\n            raise ValueError('A fresh entry must actually bind its nonempty prior envelope input')"
    source=once(source,marker,"""    if restart is None:
        if value.get('prior_transfer_identity_sha256') is not None:
            raise ValueError('A fresh branch cannot invent a same-source restart')
        if mode=='explicit-independent-branch':
            if branch is None or count!=0 or parents:
                raise ValueError('An explicit fresh branch does not pretend to have terminal predecessors')
        elif mode!='strict-terminal-transfer' or count==0 or branch is not None:
            raise ValueError('The original strict fresh branch retains its nonempty terminal-input requirement')""")
    marker="    else:\n        _digest(restart.get('sha256'))\n        _digest(value.get('prior_transfer_identity_sha256'))"
    source=once(source,marker,"""    else:
        if mode!='same-source-restart':
            raise ValueError('An actual same-source restore must retain its declared mode')
        _digest(restart.get('sha256'))
        _digest(value.get('prior_transfer_identity_sha256'))""")
    marker="    core_keys = [_typed_key(row) for row in rows]"
    source=once(source,marker,"""    if mode=='explicit-independent-branch' and rows:
        raise ValueError('A fresh independent origin cannot prefill unknown actual typed discoveries')
"""+marker)
    marker='        same_source_restart_used=restart is not None,'
    source=once(source,marker,marker+"\n        current_invocation_memory_mode=mode,independent_branch_origin=copy.deepcopy(branch),\n"
        "        pending_parallel_report_values_or_priority_inherited=False,")
    return source


def independent_parser(source):
    marker="    p.add_argument('--material-envelope-parent-report', type=Path, action='append', default=[])"
    source=once(source,marker,marker+"\n    p.add_argument('--independent-envelope-branch', action='store_true')\n"
        "    p.add_argument('--pending-parallel-envelope-run', action='append', default=[])")
    marker='    a.manifest = [path.resolve() for path in a.manifest]'
    source=once(source,marker,"""    if (a.independent_envelope_branch and (a.material_envelope_parent_report
            or a.restart_checkpoint is not None or a.restart_report is not None
            or a.material_envelope_seed_checkpoint is not None or a.material_envelope_seed_report is not None
            or a.seed_so3_checkpoint is not None or a.seed_so3_report is not None)):
        raise ValueError('Explicit independent mode starts from the original reference, without a prior final or restart')
    if (a.pending_parallel_envelope_run and not a.independent_envelope_branch
            or len(a.pending_parallel_envelope_run)!=len(set(a.pending_parallel_envelope_run))
            or any(len(v.split('/'))!=2 or any(not w.isdigit() or int(w)<1 or str(int(w))!=w
                for w in v.split('/')) for v in a.pending_parallel_envelope_run)):
        raise ValueError('Use canonical run/attempt declarations only for unread independent-branch obligations')
"""+marker)
    return source


def dual_memory_sources(source, memory_sha):
    """Select two explicit whole sources without altering the old strict path."""
    source=once(source,"MEMORY_SOURCE_SHA256 = '"+MEMORY_PARENT_SHA+"'",
        "MEMORY_SOURCE_SHA256 = '"+MEMORY_PARENT_SHA+"'\nCURRENT_MEMORY_SOURCE_SHA256 = '"+memory_sha+"'")
    source=once(source,'        default_strict_entry_requires_actual_terminal_prior_envelope_report=True,',
        '        default_strict_entry_requires_actual_terminal_prior_envelope_report=True,\n'
        '        explicit_independent_memory_source_sha256=CURRENT_MEMORY_SOURCE_SHA256,\n'
        '        strict_terminal_transfer_memory_source_sha256=MEMORY_SOURCE_SHA256,\n'
        '        new_current_restorer_source_sha256='+repr(CURRENT_RESTORER_SHA)+',\n'
        '        original_memory_math_history_scans_and_rows_unchanged=True,')
    source=once(source,'    if (sha(memory.__file__) != MEMORY_SOURCE_SHA256',
        '    actual_memory_sha=sha(memory.__file__)\n'
        '    if (actual_memory_sha not in (MEMORY_SOURCE_SHA256,CURRENT_MEMORY_SOURCE_SHA256)')
    source=once(source,'        if sha(function.__code__.co_filename) != MEMORY_SOURCE_SHA256:',
        '        if sha(function.__code__.co_filename) != actual_memory_sha:')
    source=once(source,"            or pins.get('envelope_memory',(None,None))[1] != MEMORY_SOURCE_SHA256",
        "            or pins.get('envelope_memory',(None,None))[1] != MEMORY_SOURCE_SHA256\n"
        "            or pins.get('independent_envelope_memory',(None,None))[1] != CURRENT_MEMORY_SOURCE_SHA256")
    marker="    if not paths and restart is None and not independent:\n        raise ValueError('The default strict continuation still requires its actual prior terminal report')"
    source=once(source,marker,marker+"""
    expected_memory=(CURRENT_MEMORY_SOURCE_SHA256 if independent else
        restart.get('material_envelope',{}).get('source_sha256') if restart is not None else MEMORY_SOURCE_SHA256)
    if expected_memory!=actual_memory_sha or (paths and actual_memory_sha!=MEMORY_SOURCE_SHA256):
        raise ValueError('Keep original strict c79 transfer separate from the complete new-restorer independent input')
""")
    source=once(source,'            original_complete_memory_source_sha256=MEMORY_SOURCE_SHA256,',
        '            original_complete_memory_source_sha256=actual_memory_sha,')
    source=once(source,'        actual_current_carrier_sha256=current_carrier_sha,',
        '        actual_current_carrier_sha256=current_carrier_sha,\n'
        '        actual_memory_source_sha256=actual_memory_sha,')
    marker='    expected = definition()\n    if (not isinstance(value,dict) or value.get(\'schema\') != SCHEMA'
    source=once(source,marker,"""    expected = definition()
    actual_memory_sha=value.get('actual_memory_source_sha256') if isinstance(value,dict) else None
    if (not isinstance(value,dict) or value.get('schema') != SCHEMA""")
    source=once(source,"            or envelope.get('source_sha256') != MEMORY_SOURCE_SHA256):",
        "            or actual_memory_sha not in (MEMORY_SOURCE_SHA256,CURRENT_MEMORY_SOURCE_SHA256)\n"
        "            or envelope.get('source_sha256') != actual_memory_sha):")
    source=once(source,"                or branch.get('original_complete_memory_source_sha256')!=MEMORY_SOURCE_SHA256",
        "                or branch.get('original_complete_memory_source_sha256')!=actual_memory_sha\n"
        "                or actual_memory_sha!=CURRENT_MEMORY_SOURCE_SHA256")
    marker="    elif not parents or mode=='explicit-independent-branch':\n        raise ValueError('A strict branch still needs complete actual terminal predecessor evidence')"
    source=once(source,marker,marker+"\n    if branch is None and actual_memory_sha!=MEMORY_SOURCE_SHA256:\n"
        "        raise ValueError('The strict previous-terminal path retains its original complete memory source')")
    source=once(source,'        actual_current_model_identity_sha256=canonical(model),\n        actual_parent_report_count=',
        '        actual_current_model_identity_sha256=canonical(model),\n'
        '        actual_memory_source_sha256=actual_memory_sha,\n        actual_parent_report_count=')
    return source


READER_ADDITION = '''def read_adjacent_frame_policy(path):
    """Read only the complete pinned helper's pure standard-library interface."""
    tree=ast.parse(Path(path).read_text())
    names={'SCHEMA','FRAME_C1_SOURCE_SHA256','STAGE_MATRIX_SOURCE_SHA256',
        'PARENT_OPERATOR_SOURCE_SHA256','BASE_SOURCE_SHA256','COUNTER_KEYS'}
    wanted={'sha','canonical','definition','_copy','_digest','validate_metadata'}
    body=[];seen_names=set();seen_functions=set()
    for node in tree.body:
        if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name):
            name=node.targets[0].id
            if name in names:
                ast.literal_eval(node.value);body.append(node);seen_names.add(name)
        if isinstance(node,ast.FunctionDef) and node.name in wanted:
            body.append(node);seen_functions.add(node.name)
    if seen_names!=names or seen_functions!=wanted:
        raise ValueError('Retain the entire source-bound adjacent-frame pure contract')
    namespace=dict(Path=Path,hashlib=hashlib,json=json,math=math,__file__=str(path))
    exec(compile(ast.Module(body=body,type_ignores=[]),'<bound adjacent-frame metadata>','exec'),namespace)
    return namespace['definition'](),namespace['validate_metadata']


def adjacent_frame_binding(report,model,roles,path):
    if sha(path)!=roles['adjacent_matrices']:
        raise ValueError('Bind the whole actual adjacent-frame producer source')
    expected,validator=read_adjacent_frame_policy(path)
    if (model.get('adjacent_normal_frame_matrices')!=expected
            or report.get('adjacent_normal_frame_matrix_definition')!=expected
            or report.get('adjacent_normal_frame_matrix_source',{}).get('sha256')!=roles['adjacent_matrices']
            or report.get('adjacent_matrix_rounding_is_independent') is not True
            or report.get('adjacent_matrix_acceleration_or_error_certified') is not False):
        raise ValueError('Keep the independent working products and original complete root/field responsibilities')
    binding=dict(definition=expected,definition_identity_sha256=canonical(expected),
        source_sha256=roles['adjacent_matrices'],original_root_Newton_J3_and_active_chain_retained=True,
        old_higher_order_roots_not_discarded=True,prior_plain_run_required=False,
        actual_matrix_origin_separate_from_root_success=True,acceleration_or_error_certificate=False)
    def read_metadata(value):
        if value is None or value=={}:return None
        if not isinstance(value,dict):raise ValueError('Keep actual complete operator metadata or absence')
        answer=validator(value.get('adjacent_normal_frame_matrices'),
            model_identity=canonical(model),operator_source_sha256=roles['endpoint'],
            expected_definition=expected)
        last=answer.get('last_call')
        answer['last_call_point_matches_latest_operator_point']=(None if last is None else
            last['current_full_point_sha256']==value.get('current_full_point_sha256'))
        return answer
    return binding,read_metadata


'''


def derive(parent,helper,memory_parent):
    output={HELPER_NAME:helper}
    helper_sha=sha(helper)
    if sha(memory_parent)!=MEMORY_PARENT_SHA:
        raise ValueError('Preserve the entire original c79 memory source')
    memory=assignment(memory_parent,'RESTORER_SHA',CURRENT_RESTORER_SHA)
    output[MEMORY_NAME]=memory;memory_sha=sha(memory)
    cal_old='reference_centred_stage_cached_smooth_triangle_calibration.py'
    cal=common(parent[cal_old]);output[NAMES[cal_old]]=cal;cal_sha=sha(cal)
    op_old='so3_reference_centred_stage_cached_smooth_triangle_normal_lift_operator.py'
    op=common(parent[op_old])
    op=assignment(op,'REFERENCE_CENTERING_SOURCE_SHA256',cal_sha)
    marker="STAGE_MATRIX_SOURCE_SHA256 = '375059dc973633a1639ceddd3105fc34fe8b37eec4c9e61a55ce3959a0b9fc59'"
    op=once(op,marker,marker+"\nADJACENT_FRAME_SOURCE_SHA256 = '"+helper_sha+"'")
    op=once(op,'frame_c1_module=None, stage_matrix_module=None):',
        'frame_c1_module=None, stage_matrix_module=None, adjacent_matrix_module=None):')
    marker='        self.reference_calibration = reference_centering_module.FrozenReferenceCalibration('
    op=once(op,marker,"""        if (adjacent_matrix_module is None or sha(adjacent_matrix_module.__file__) != ADJACENT_FRAME_SOURCE_SHA256
                or sha(adjacent_matrix_module.AdjacentNormalFrameMatrices.__init__.__code__.co_filename)
                    != ADJACENT_FRAME_SOURCE_SHA256):
            raise ValueError('Bind the entire independent adjacent total-frame matrix producer')
"""+marker)
    op=once(op,'            detached_stage_matrix_reuse=stage_matrix_module.definition(),',
        '            detached_stage_matrix_reuse=stage_matrix_module.definition(),\n'
        '            adjacent_normal_frame_matrices=adjacent_matrix_module.definition(),')
    marker='        self.stage_matrices = stage_matrix_module.CompleteDetachedStageMatrices(self,frame_c1_module=frame_c1_module)'
    op=once(op,marker,marker+'\n        self.adjacent_frames = adjacent_matrix_module.AdjacentNormalFrameMatrices(self,\n'
        '            frame_c1_module=frame_c1_module,stage_matrix_module=stage_matrix_module)')
    op=once(op,'        all_stages = []\n        with torch.no_grad(),',
        '        all_stages = []\n        frame_context = self.adjacent_frames.frame_context(data,keys,order)\n'
        '        with torch.no_grad(),')
    marker="                if not bool(torch.isfinite(frame).all()):\n                    self._fail('Nonfinite complete preceding normal frame',\n                        normal_stage_index=index,state=previous[:,0])"
    op=once(op,marker,marker+'\n                frame_provenance = self.adjacent_frames.capture_frame_inputs(\n'
        '                    frame_context,previous,frame,index-1,old_stages=old_stage)')
    op=once(op,'                    J=matrix.detach().cpu().numpy().copy(),records=records))',
        '                    J=matrix.detach().cpu().numpy().copy(),records=records,frame_provenance=frame_provenance))')
    op=once(op,"                record=item['records'][j],jacobian=None,jacobian_order=0) for item in all_stages]",
        "                record=item['records'][j],frame_provenance=item['frame_provenance'][j],\n"
        '                jacobian=None,jacobian_order=0) for item in all_stages]')
    old='''                zero = tensor(np.stack([item['zero'] for item in selected]))
                previous = torch.zeros((len(needed),3,CONTROL_DIMENSION),dtype=torch.float64)
                with self.stage_matrices.scope(subset,[keys[i] for i in needed],order,
                        'complete_angular_J6_J9') as stage_matrices:
                    for index in range(self.normal_stage_count):
                        stages = [item['stages'][index] for item in selected]
                        frame = tensor(np.stack([item['frame'] for item in stages]))
                        eta = tensor(np.stack([item['eta'] for item in stages]))
                        try:
                            matrix = stage_matrices.angular(eta,previous,frame,zero,
                                self.normal_step_carriers[index+1],index,order)
                        except (EndpointRootFailure,RuntimeError) as error:
                            self._fail('Actual full current-stage implicit matrix unavailable: '+str(error),
                                normal_stage_index=index+1,incremental_state=eta[:,0])
                        for j,item in enumerate(stages):
                            item['jacobian'] = matrix[j].cpu().numpy().copy()
                            item['jacobian'].setflags(write=False)
                            item['jacobian_order'] = order
                        previous = tensor(np.stack([item['controls'] for item in stages]))'''
    op=once(op,old,'''                self.adjacent_frames.populate(subset,[keys[i] for i in needed],selected,order)''')
    op=once(op,'            detached_stage_matrix_reuse=self.stage_matrices.metadata(),',
        '            detached_stage_matrix_reuse=self.stage_matrices.metadata(),\n'
        '            adjacent_normal_frame_matrices=self.adjacent_frames.metadata(),')
    output[NAMES[op_old]]=op;op_sha=sha(op)
    geo_old='so3_reference_centred_stage_cached_material_envelope_geometry.py'
    geo=common(parent[geo_old])
    geo=assignment(geo,'SCHEMA','complete-R715-adjacent-frame-material-envelope-world-geometry-and-preserved-prefix-rows-v1')
    geo=assignment(geo,'ENDPOINT_SOURCE_SHA256',op_sha)
    geo=assignment(geo,'REFERENCE_CENTERING_SOURCE_SHA256',cal_sha)
    geo=once(geo,"MATERIAL_ENVELOPE_MEMORY_SHA256 = '"+MEMORY_PARENT_SHA+"'",
        "MATERIAL_ENVELOPE_MEMORY_SHA256 = '"+MEMORY_PARENT_SHA+"'\n"
        "CURRENT_MATERIAL_ENVELOPE_MEMORY_SHA256 = '"+memory_sha+"'")
    geo=once(geo,'        if envelope is None or sha(type(envelope).__init__.__code__.co_filename) != MATERIAL_ENVELOPE_MEMORY_SHA256:',
        '        self.envelope_memory_source_sha256=(None if envelope is None else sha(type(envelope).__init__.__code__.co_filename))\n'
        '        if self.envelope_memory_source_sha256 not in (MATERIAL_ENVELOPE_MEMORY_SHA256,CURRENT_MATERIAL_ENVELOPE_MEMORY_SHA256):')
    geo=once(geo,'            material_envelope_memory_source_sha256=MATERIAL_ENVELOPE_MEMORY_SHA256,',
        '            material_envelope_memory_source_sha256=self.envelope_memory_source_sha256,')
    marker="STAGE_MATRIX_SOURCE_SHA256 = '375059dc973633a1639ceddd3105fc34fe8b37eec4c9e61a55ce3959a0b9fc59'"
    geo=once(geo,marker,marker+"\nADJACENT_FRAME_SOURCE_SHA256 = '"+helper_sha+"'")
    marker="        self.operator_sha256 = model['source_sha256']"
    geo=once(geo,marker,"""        adjacent=problem.adjacent_frames
        if (adjacent.q is not problem or adjacent.model_identity!=problem.identity
                or adjacent.operator_source!=ENDPOINT_SOURCE_SHA256
                or model.get('adjacent_normal_frame_matrices')!=adjacent.definition
                or adjacent.definition.get('source_sha256')!=ADJACENT_FRAME_SOURCE_SHA256
                or sha(adjacent.__init__.__func__.__code__.co_filename)!=ADJACENT_FRAME_SOURCE_SHA256
                or adjacent.definition.get('all_original_stage_equations_roots_Newton_J3_and_angular_solves_retained') is not True
                or adjacent.definition.get('original_active_residual_and_all_upstream_parameter_edges_retained') is not True):
            raise ValueError('The adjacent-frame producer cannot replace roots, stages or the active field chain')
"""+marker)
    output[NAMES[geo_old]]=geo;geo_sha=sha(geo)
    trans_old='transfer_material_envelope_memory.py';trans=common(parent[trans_old])
    trans=assignment(trans,'SCHEMA','strict-prior-envelope-address-and-typed-memory-transfer-to-adjacent-frames-v1')
    trans=trans.replace('into the independent matrix-reuse model.','into the independent adjacent-frame model.')
    trans=once(trans,"changed_model_fields='only schema/source, complete detached_stage_matrix_reuse, and calibration source/endpoint source',",
        "changed_model_fields='only schema/source, full detached_stage_matrix_reuse, adjacent_normal_frame_matrices, and calibration source/endpoint source',")
    marker="    for value in (before,after):\n        for key in ('schema','source_sha256'):"
    trans=once(trans,marker,"""    adjacent=after.pop('adjacent_normal_frame_matrices',None)
    if (not isinstance(adjacent,dict) or adjacent.get('source_sha256')!=current_pins['adjacent_matrices'][1]
            or adjacent.get('complete_detached_matrix_source_sha256')!=current_pins['stage_matrices'][1]
            or adjacent.get('complete_frame_C1_source_sha256')!=current_pins['frame_C1'][1]
            or adjacent.get('complete_base_source_sha256')!=current_pins['meridian'][1]
            or adjacent.get('all_original_stage_equations_roots_Newton_J3_and_angular_solves_retained') is not True
            or adjacent.get('original_active_residual_and_all_upstream_parameter_edges_retained') is not True
            or adjacent.get('block_products_have_independent_working_rounding_definition') is not True):
        raise ValueError('Only the explicitly bound complete adjacent-frame working producer may be added')
"""+marker)
    trans=independent_memory_mode(trans)
    trans=dual_memory_sources(trans,memory_sha)
    output[NAMES[trans_old]]=trans;trans_sha=sha(trans)
    driver_old='fullclosed_reference_centred_stage_cached_material_envelope_so3_qp.py'
    driver=common(parent[driver_old]);pins=literals(driver)['SOURCE_PINS']
    for role,digest in (('endpoint',op_sha),('geometry',geo_sha),('reference_calibration',cal_sha),('envelope_transfer',trans_sha)):
        pins[role]=(pins[role][0],digest)
    pins['adjacent_matrices']=('scripts/resume_20261126/'+HELPER_NAME,helper_sha)
    pins['independent_envelope_memory']=('scripts/resume_20261126/'+MEMORY_NAME,memory_sha)
    driver=assignment(driver,'SOURCE_PINS',pins)
    marker="    stage_matrices = load('_actual_complete_detached_stage_matrices',paths['stage_matrices'])"
    driver=once(driver,marker+"\n",marker+"\n    adjacent_matrices = load('_actual_complete_adjacent_frame_matrices',paths['adjacent_matrices'])\n")
    marker="    envelope_memory = load('_so3_complete_material_envelope_memory',paths['envelope_memory'])"
    driver=once(driver,marker,marker+"\n    independent_envelope_memory = load('_so3_complete_current_restorer_envelope_memory',paths['independent_envelope_memory'])")
    marker='    address_parent = restart if restart is not None else seed_report'
    driver=once(driver,marker,"""    if (args.independent_envelope_branch or (restart is not None
            and restart.get('material_envelope',{}).get('source_sha256')==SOURCE_PINS['independent_envelope_memory'][1])):
        envelope_memory=independent_envelope_memory
"""+marker)
    driver=once(driver,"        material_envelope_source=file_record(paths['envelope_memory']),",
        "        material_envelope_source=file_record(envelope_memory.__file__),")
    driver=once(driver,'reference_centering_module=calibration,frame_c1_module=frame_c1,stage_matrix_module=stage_matrices)',
        'reference_centering_module=calibration,frame_c1_module=frame_c1,stage_matrix_module=stage_matrices,\n'
        '        adjacent_matrix_module=adjacent_matrices)')
    marker="        detached_stage_matrix_source=file_record(paths['stage_matrices']),"
    driver=once(driver,marker,marker+"\n        adjacent_normal_frame_matrix_definition=q.adjacent_frames.definition,\n"
        "        adjacent_normal_frame_matrix_source=file_record(paths['adjacent_matrices']),\n"
        '        adjacent_matrix_rounding_is_independent=True,\n'
        '        adjacent_matrix_acceleration_or_error_certified=False,')
    driver=independent_parser(driver)
    output[NAMES[driver_old]]=driver;driver_sha=sha(driver)
    launch_old='launch_reference_centred_stage_cached_material_envelope_so3_actions.py'
    launch=independent_parser(assignment(common(parent[launch_old]),'DRIVER_SHA',driver_sha))
    launch=once(launch,'        if isinstance(value, list):',
        '        if isinstance(value, bool):\n            if value: command.append(flag)\n'
        '        elif isinstance(value, list):')
    output[NAMES[launch_old]]=launch
    reader_old='read_reference_centred_stage_cached_material_envelope_so3_report.py'
    reader=assignment(common(parent[reader_old]),'DRIVER_SHA',driver_sha)
    reader=once(reader,'def transferred_envelope_binding(',READER_ADDITION+'def transferred_envelope_binding(')
    marker="    matrix_binding,matrix_read = detached_matrix_binding(report,model,roles,topic/load_pins(driver)['stage_matrices'][0])"
    reader=once(reader,marker,marker+"\n    adjacent_binding,adjacent_read = adjacent_frame_binding(report,model,roles,topic/load_pins(driver)['adjacent_matrices'][0])")
    marker='        detached_stage_matrix_diagnostics=matrix_read(metadata),'
    reader=once(reader,marker,marker+'\n        adjacent_normal_frame_matrix_binding=adjacent_binding,\n'
        '        adjacent_normal_frame_matrix_diagnostics=adjacent_read(metadata),')
    marker="    seed = module.validate_seed_metadata(report.get('prior_envelope_final_variable_seed'),"
    reader=once(reader,marker,"""    raw_transfer=report['material_envelope_transfer']
    if raw_transfer.get('current_invocation_memory_mode')=='explicit-independent-branch':
        original=model['reference_centering_definition']['original_reference_point_sha256']
        if (report.get('initial_full_variable_point_sha256')!=original
                or report.get('actual_reference_initial_full_point_sha256')!=original
                or report.get('prior_envelope_final_variable_seed') is not None):
            raise ValueError('The independent branch must really start from its complete original reference point')
"""+marker)
    marker="    relative, expected_source = load_pins(driver)['envelope_memory']\n    path = topic/relative\n    if sha(path) != expected_source or roles.get('envelope_memory') != expected_source:"
    reader=once(reader,marker,"""    actual_source=report.get('material_envelope_source',{}).get('sha256')
    candidates=[role for role in ('envelope_memory','independent_envelope_memory')
        if roles.get(role)==actual_source]
    if len(candidates)!=1:
        raise ValueError('Bind one explicit complete original or current-restorer memory source')
    role=candidates[0]
    relative, expected_source = load_pins(driver)[role]
    path = topic/relative
    if sha(path) != expected_source or roles.get(role) != expected_source:""")
    output[NAMES[reader_old]]=reader
    # The entire protected physics and solver suffix must remain identical.
    old,new=methods(parent[op_old],'ZeroClosureOperator'),methods(op,'ZeroClosureOperator')
    changed=[name for name in old if old[name]!=new.get(name)]
    if sorted(changed)!=sorted(['__init__','_run_chain','_get_roots','metadata']):
        raise ValueError('Unexpected normal method changes: '+repr(changed))
    old,new=methods(parent[geo_old],'GeometryScreen'),methods(geo,'GeometryScreen')
    if [name for name in old if old[name]!=new.get(name)]!=['__init__']:
        raise ValueError('A complete geometry/row method changed')
    suffix='    def save_report():\n'
    if driver[driver.index(suffix):]!=parent[driver_old][parent[driver_old].index(suffix):]:
        raise ValueError('The complete original reporting/optimization suffix changed')
    return output


def validate_source(name,value):
    raw=value.encode()
    if len(raw)>=100000:raise ValueError('Keep each complete source under100KB: '+name)
    tree=ast.parse(value,filename=name);compile(tree,name,'exec')
    for node in ast.walk(tree):
        if isinstance(node,ast.Dict):
            keys=[n.value for n in node.keys if isinstance(n,ast.Constant)
                and isinstance(n.value,(str,int,float))]
            if len(keys)!=len(set(keys)):raise ValueError('Duplicate literal dictionary key in '+name)
        if isinstance(node,ast.Call):
            keys=[n.arg for n in node.keywords if n.arg is not None]
            if len(keys)!=len(set(keys)):raise ValueError('Duplicate keyword in '+name)
    if any(line!=line.rstrip() for line in value.splitlines()):raise ValueError('Trailing whitespace '+name)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--parent-directory',type=Path,required=True)
    p.add_argument('--helper-source',type=Path,required=True)
    p.add_argument('--memory-parent-source',type=Path,required=True)
    p.add_argument('--current-restorer-source',type=Path,required=True)
    p.add_argument('--outdir',type=Path,required=True)
    p.add_argument('--verify-existing',action='store_true')
    args=p.parse_args();parent={}
    for name,digest in PARENT.items():
        raw=(args.parent_directory/name).read_bytes()
        if sha(raw)!=digest:raise ValueError('The entire immutable parent source differs: '+name)
        parent[name]=raw.decode()
    helper=args.helper_source.read_text()
    if sha(args.current_restorer_source.read_bytes())!=CURRENT_RESTORER_SHA:
        raise ValueError('Use the complete actual current-run restorer, not the old hard-coded run07 source')
    outputs=derive(parent,helper,args.memory_parent_source.read_text())
    args.outdir.mkdir(parents=True,exist_ok=True)
    records=[]
    for name,source in outputs.items():
        validate_source(name,source);path=args.outdir/name
        if args.verify_existing:
            if path.read_bytes()!=source.encode():raise ValueError('Complete derived bytes differ: '+name)
        else:path.write_text(source)
        py_compile.compile(str(path),doraise=True)
        records.append(dict(name=name,bytes=len(source.encode()),sha256=sha(source)))
    print(json.dumps(dict(science_executed=False,complete_sources=records),indent=2))


if __name__=='__main__':main()
