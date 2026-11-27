#!/usr/bin/env python3
"""Reproduce all five complete independent-chart entry sources from real parents.

Pure source text/AST only. No numerical module, scientific array, F/J/root,
preflight fixture or field is imported or evaluated. This is an optional
complete-source reproduction tool, not a new gate before the science.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path

PARENTS = json.loads("{\"geometry\":{\"path\":\"scripts/resume_20261126/so3_reference_centred_compatible_frame_material_envelope_geometry.py\",\"sha256\":\"ba98027d88f2949e902af90bc9fe19cb0e18c0e758512c18382798e1a050425b\",\"bytes\":68275,\"blob\":\"8cf309bff99484e0e495aedfcb73203de512f9e1\"},\"transfer\":{\"path\":\"scripts/resume_20261126/transfer_material_envelope_memory_to_compatible_frames.py\",\"sha256\":\"f3264400100cabbf717c4e07cae70d7cabca8403bc6c8b4c46c726da3eb6f10a\",\"bytes\":55758,\"blob\":\"9a455377464e30e257accf52ca6bdbd2ad06129c\"},\"driver\":{\"path\":\"scripts/resume_20261126/fullclosed_reference_centred_compatible_frame_material_envelope_so3_qp.py\",\"sha256\":\"5c5c2c944c030682bc85470089590a4d3f1536049942d6a3de6cf79e38ed2191\",\"bytes\":74542,\"blob\":\"d1465a44df2f6db6a3df89302f3d32fa83167a91\"},\"launcher\":{\"path\":\"scripts/resume_20261126/launch_reference_centred_compatible_frame_material_envelope_so3_actions.py\",\"sha256\":\"a52e4b54d7785b226a255c5d938892198164858907795e93337c529a8b2c625e\",\"bytes\":20745,\"blob\":\"10da3889d88f0476a45867c7f65b7afab039586d\"},\"reader\":{\"path\":\"scripts/resume_20261126/read_reference_centred_compatible_frame_material_envelope_so3_report.py\",\"sha256\":\"475fa6d8505611d8198debc97f5bb4101fb18c10312835178d486e3c366a927e\",\"bytes\":95632,\"blob\":\"0eb931055c4f52acff1e77bb27757cf48c058308\"}}")
EXPECTED = json.loads("{\"geometry\":{\"path\":\"scripts/resume_20261126/so3_reference_centred_independent_chart_material_envelope_geometry.py\",\"sha256\":\"1bccece84925523a5a4a54b4ba021b119a10d4c90a693fe89565200f440fbbd3\",\"bytes\":68275,\"name\":\"so3_reference_centred_independent_chart_material_envelope_geometry.py\",\"parent\":{\"sha256\":\"ba98027d88f2949e902af90bc9fe19cb0e18c0e758512c18382798e1a050425b\",\"bytes\":68275,\"blob\":\"8cf309bff99484e0e495aedfcb73203de512f9e1\"}},\"transfer\":{\"path\":\"scripts/resume_20261126/transfer_material_envelope_memory_to_independent_chart.py\",\"sha256\":\"182a4a5401c959c983ebd8c544bdae58c02d5df942c4491b14c89f83880f8590\",\"bytes\":58387,\"name\":\"transfer_material_envelope_memory_to_independent_chart.py\",\"parent\":{\"sha256\":\"f3264400100cabbf717c4e07cae70d7cabca8403bc6c8b4c46c726da3eb6f10a\",\"bytes\":55758,\"blob\":\"9a455377464e30e257accf52ca6bdbd2ad06129c\"}},\"driver\":{\"path\":\"scripts/resume_20261126/fullclosed_reference_centred_independent_chart_material_envelope_so3_qp.py\",\"sha256\":\"95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9\",\"bytes\":75152,\"name\":\"fullclosed_reference_centred_independent_chart_material_envelope_so3_qp.py\",\"parent\":{\"sha256\":\"5c5c2c944c030682bc85470089590a4d3f1536049942d6a3de6cf79e38ed2191\",\"bytes\":74542,\"blob\":\"d1465a44df2f6db6a3df89302f3d32fa83167a91\"}},\"launcher\":{\"path\":\"scripts/resume_20261126/launch_reference_centred_independent_chart_material_envelope_so3_actions.py\",\"sha256\":\"10422033f229649aa2e8237c25880670219d618d24690d429025347fd73f039b\",\"bytes\":20746,\"name\":\"launch_reference_centred_independent_chart_material_envelope_so3_actions.py\",\"parent\":{\"sha256\":\"a52e4b54d7785b226a255c5d938892198164858907795e93337c529a8b2c625e\",\"bytes\":20745,\"blob\":\"10da3889d88f0476a45867c7f65b7afab039586d\"}},\"reader\":{\"path\":\"scripts/resume_20261126/read_reference_centred_independent_chart_material_envelope_so3_report.py\",\"sha256\":\"f382bedb07fdf43e3fd94ac411c4a072519494dd2a16ec19ab627492d9606470\",\"bytes\":98389,\"name\":\"read_reference_centred_independent_chart_material_envelope_so3_report.py\",\"parent\":{\"sha256\":\"475fa6d8505611d8198debc97f5bb4101fb18c10312835178d486e3c366a927e\",\"bytes\":95632,\"blob\":\"0eb931055c4f52acff1e77bb27757cf48c058308\"}}}")
DEPENDENCIES = json.loads("{\"memory\":{\"path\":\"scripts/resume_20261126/complete_material_envelope_memory_independent_chart.py\",\"sha256\":\"4d92ca2387523a76bbea0a3444e0665c306369dd0351c3354c998a09884e043b\"},\"producer\":{\"path\":\"scripts/resume_20261126/freeze_run08_fixed_chart_and_restore_run05_carrier.py\",\"sha256\":\"105289ba7c454f671c8eae086b31a4ea01b06978101503cd0ef283320fc85361\"}}")
PATCHES = json.loads("{\"geometry\":[{\"old\":\"1e2ca9ec89d407d6d187ed60fe94406820f098dfca7c2b70c4f0645ea9bcdfa9\",\"new\":\"4d92ca2387523a76bbea0a3444e0665c306369dd0351c3354c998a09884e043b\",\"count\":1}],\"transfer\":[{\"old\":\"1e2ca9ec89d407d6d187ed60fe94406820f098dfca7c2b70c4f0645ea9bcdfa9\",\"new\":\"4d92ca2387523a76bbea0a3444e0665c306369dd0351c3354c998a09884e043b\",\"count\":1},{\"old\":\"SCHEMA = 'strict-prior-envelope-transfer-or-explicit-independent-adjacent-branch-v1'\",\"new\":\"SCHEMA = 'strict-prior-envelope-transfer-or-explicit-independent-fixed-chart-branch-v1'\",\"count\":1},{\"old\":\"new_current_restorer_source_sha256='8c1e2d8f71bb08b33f99f9c187dbed2994776fc64b7114e1cea921a4fecff449',\",\"new\":\"new_current_restorer_source_sha256='105289ba7c454f671c8eae086b31a4ea01b06978101503cd0ef283320fc85361',\\n        independent_chart_is_a_separately_frozen_complete_target=True,\\n        strict_terminal_model_relationship_is_not_relaxed_for_new_chart=True,\",\"count\":1},{\"old\":\"        changed_model_fields='only schema/source, full detached_stage_matrix_reuse, adjacent_normal_frame_matrices, and calibration source/endpoint source',\",\"new\":\"        changed_model_fields='strict terminal transfer only: schema/source, full detached_stage_matrix_reuse, adjacent_normal_frame_matrices, and calibration source/endpoint source',\",\"count\":1},{\"old\":\"explicit-independent-complete-material-envelope-origin-v1\",\"new\":\"explicit-independent-fixed-chart-complete-material-envelope-origin-v1\",\"count\":2},{\"old\":\"    if independent:\\n        branch_origin=dict(schema='explicit-independent-fixed-chart-complete-material-envelope-origin-v1',\",\"new\":\"    if independent:\\n        target=envelope.metadata()['historical_address_binding']['actual_path_binding']['fixed_target_definition']\\n        reference=q.base.model['complete_axisymmetric_reference_model']\\n        if (target['complete_current_reference_model']!=reference\\n                or target['complete_current_reference_bundle_sha256']!=sha(args.reference_bundle)\\n                or target['fixed_chart_core_array_record']['sha256']!=reference['fixed_chart_core_sha256']):\\n            raise ValueError('Bind this actual new fixed target before creating its independent origin')\\n        branch_origin=dict(schema='explicit-independent-fixed-chart-complete-material-envelope-origin-v1',\",\"count\":1},{\"old\":\"            actual_origin_model_identity_sha256=q.identity,\",\"new\":\"            independent_fixed_target_definition_identity_sha256=canonical(target),\\n            actual_origin_reference_model_identity_sha256=canonical(reference),\\n            actual_origin_reference_bundle_sha256=target['complete_current_reference_bundle_sha256'],\\n            actual_origin_fixed_chart_core_sha256=reference['fixed_chart_core_sha256'],\\n            same_original_fixed_chart=False,same_original_g_claimed=False,\\n            same_mathematical_g_claimed=False,old_values_or_certificates_inherited=False,\\n            actual_origin_model_identity_sha256=q.identity,\",\"count\":1},{\"old\":\"    if branch is not None:\\n        if (not isinstance(branch,dict)\",\"new\":\"    if branch is not None:\\n        target=envelope['historical_address_binding']['actual_path_binding']['fixed_target_definition']\\n        reference=model['base_complete_model']['complete_axisymmetric_reference_model']\\n        if (target['complete_current_reference_model']!=reference\\n                or target['complete_current_reference_bundle_sha256']!=model['base_complete_model']['initial_reference_bundle_sha256']\\n                or target['fixed_chart_core_array_record']['sha256']!=reference['fixed_chart_core_sha256']):\\n            raise ValueError('The independent origin must retain the whole current reference and target')\\n        if (not isinstance(branch,dict)\",\"count\":1},{\"old\":\"                or branch.get('actual_origin_model_identity_sha256')!=canonical(model)\",\"new\":\"                or branch.get('independent_fixed_target_definition_identity_sha256')!=canonical(target)\\n                or branch.get('actual_origin_reference_model_identity_sha256')!=canonical(reference)\\n                or branch.get('actual_origin_reference_bundle_sha256')!=target['complete_current_reference_bundle_sha256']\\n                or branch.get('actual_origin_fixed_chart_core_sha256')!=reference['fixed_chart_core_sha256']\\n                or branch.get('same_original_fixed_chart') is not False\\n                or branch.get('same_original_g_claimed') is not False\\n                or branch.get('same_mathematical_g_claimed') is not False\\n                or branch.get('old_values_or_certificates_inherited') is not False\\n                or branch.get('actual_origin_model_identity_sha256')!=canonical(model)\",\"count\":1}],\"driver\":[{\"old\":\"so3_reference_centred_compatible_frame_material_envelope_geometry.py\",\"new\":\"so3_reference_centred_independent_chart_material_envelope_geometry.py\",\"count\":1},{\"old\":\"ba98027d88f2949e902af90bc9fe19cb0e18c0e758512c18382798e1a050425b\",\"new\":\"1bccece84925523a5a4a54b4ba021b119a10d4c90a693fe89565200f440fbbd3\",\"count\":1},{\"old\":\"transfer_material_envelope_memory_to_compatible_frames.py\",\"new\":\"transfer_material_envelope_memory_to_independent_chart.py\",\"count\":1},{\"old\":\"f3264400100cabbf717c4e07cae70d7cabca8403bc6c8b4c46c726da3eb6f10a\",\"new\":\"182a4a5401c959c983ebd8c544bdae58c02d5df942c4491b14c89f83880f8590\",\"count\":1},{\"old\":\"complete_material_envelope_memory_compatible_current.py\",\"new\":\"complete_material_envelope_memory_independent_chart.py\",\"count\":1},{\"old\":\"1e2ca9ec89d407d6d187ed60fe94406820f098dfca7c2b70c4f0645ea9bcdfa9\",\"new\":\"4d92ca2387523a76bbea0a3444e0665c306369dd0351c3354c998a09884e043b\",\"count\":1},{\"old\":\"restore_actual_run05_carrier_for_compatible_current_run08.py\",\"new\":\"freeze_run08_fixed_chart_and_restore_run05_carrier.py\",\"count\":1},{\"old\":\"6cc95526e5305fa0265b96f66d322bbba612b8702d5ebcc5ec48a9fb29639d19\",\"new\":\"105289ba7c454f671c8eae086b31a4ea01b06978101503cd0ef283320fc85361\",\"count\":1},{\"old\":\"SCHEMA = 'complete-R711-reference-centred-adjacent-frame-material-envelope-fixed-normal-plane-SO3-QP-v1'\",\"new\":\"SCHEMA = 'complete-R711-reference-centred-independent-chart-material-envelope-fixed-normal-plane-SO3-QP-v1'\",\"count\":1},{\"old\":\"    report = dict(schema=SCHEMA, source_sha256=sha(__file__), source_commit=source_commit,\",\"new\":\"    initial_envelope_metadata=envelope.metadata()\\n    independent_target_validation=history_record.get('independent_fixed_target_validation')\\n    independent_target=(initial_envelope_metadata['historical_address_binding']['actual_path_binding']['fixed_target_definition']\\n        if independent_target_validation is not None else None)\\n    report = dict(schema=SCHEMA, source_sha256=sha(__file__), source_commit=source_commit,\",\"count\":1},{\"old\":\"        material_envelope=envelope.metadata(),\",\"new\":\"        material_envelope=initial_envelope_metadata,\\n        independent_fixed_target_definition=independent_target,\\n        independent_fixed_target_definition_identity_sha256=(None if independent_target is None else canonical(independent_target)),\\n        independent_fixed_target_validation=independent_target_validation,\",\"count\":1}],\"launcher\":[{\"old\":\"fullclosed_reference_centred_compatible_frame_material_envelope_so3_qp.py\",\"new\":\"fullclosed_reference_centred_independent_chart_material_envelope_so3_qp.py\",\"count\":1},{\"old\":\"5c5c2c944c030682bc85470089590a4d3f1536049942d6a3de6cf79e38ed2191\",\"new\":\"95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9\",\"count\":1}],\"reader\":[{\"old\":\"fullclosed_reference_centred_compatible_frame_material_envelope_so3_qp.py\",\"new\":\"fullclosed_reference_centred_independent_chart_material_envelope_so3_qp.py\",\"count\":1},{\"old\":\"5c5c2c944c030682bc85470089590a4d3f1536049942d6a3de6cf79e38ed2191\",\"new\":\"95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9\",\"count\":1},{\"old\":\"REPORT_SCHEMA = 'complete-R711-reference-centred-adjacent-frame-material-envelope-fixed-normal-plane-SO3-QP-v1'\",\"new\":\"REPORT_SCHEMA = 'complete-R711-reference-centred-independent-chart-material-envelope-fixed-normal-plane-SO3-QP-v1'\",\"count\":1},{\"old\":\"def read_report(repo, report_path, *, verify_final_bundle=False):\",\"new\":\"def independent_chart_binding(report, envelope_binding):\\n    checked=envelope_binding['actual_metadata'].get('independent_fixed_target_validation')\\n    target=report.get('independent_fixed_target_definition')\\n    identity=report.get('independent_fixed_target_definition_identity_sha256')\\n    if checked is None:\\n        if target is not None or identity is not None or report.get('independent_fixed_target_validation') is not None:\\n            raise ValueError('The original strict transfer cannot claim an unbound independent chart')\\n        return None\\n    path=report['material_envelope']['historical_address_binding']['actual_path_binding']\\n    base=report['representation']['base_complete_model']\\n    reference=base['complete_axisymmetric_reference_model']\\n    if (not isinstance(target,dict) or target!=path.get('fixed_target_definition')\\n            or identity!=canonical(target) or identity!=path.get('fixed_target_definition_identity_sha256')\\n            or identity!=checked.get('fixed_target_definition_identity_sha256')\\n            or checked!=report.get('independent_fixed_target_validation')\\n            or target.get('complete_current_reference_model')!=reference\\n            or target.get('current_reference_model_identity_sha256')!=canonical(reference)\\n            or checked.get('actual_current_model_identity_sha256')!=canonical(reference)\\n            or target.get('complete_current_reference_bundle_sha256')!=report['bundle_sha256']\\n            or target.get('complete_current_reference_bundle_sha256')!=base['initial_reference_bundle_sha256']\\n            or target.get('fixed_chart_core_array_record',{}).get('sha256')!=reference['fixed_chart_core_sha256']\\n            or base['fixed_chart_core_sha256']!=reference['fixed_chart_core_sha256']\\n            or checked.get('current_fixed_chart_core_sha256')!=reference['fixed_chart_core_sha256']\\n            or target.get('same_original_fixed_chart') is not False\\n            or target.get('same_mathematical_g_claimed') is not False):\\n        raise ValueError('The verified full target, all chart words and actual report reference must be identical')\\n    return dict(definition_identity_sha256=identity,\\n        actual_reference_model_identity_sha256=canonical(reference),\\n        actual_reference_bundle_sha256=report['bundle_sha256'],\\n        actual_fixed_chart_core_sha256=reference['fixed_chart_core_sha256'],\\n        complete_target_and_actual_report_reference_equal=True,\\n        actual_full_chart_words_verified=True,same_original_fixed_chart=False,\\n        same_mathematical_g_claimed=False,old_values_or_certificates_inherited=False)\\n\\n\\ndef read_report(repo, report_path, *, verify_final_bundle=False):\",\"count\":1},{\"old\":\"    transfer_binding,prior_final_seed = transferred_envelope_binding(topic,report,model,roles,driver)\",\"new\":\"    transfer_binding,prior_final_seed = transferred_envelope_binding(topic,report,model,roles,driver)\\n    independent_target=independent_chart_binding(report,envelope_binding)\",\"count\":1},{\"old\":\"schema='actual-complete-R711-reference-centred-adjacent-frame-material-envelope-normal-plane-SO3-scalar-readout-v1'\",\"new\":\"schema='actual-complete-R711-reference-centred-independent-chart-material-envelope-normal-plane-SO3-scalar-readout-v1'\",\"count\":1},{\"old\":\"        material_envelope_binding=envelope_binding,\",\"new\":\"        material_envelope_binding=envelope_binding,\\n        independent_fixed_target_binding=independent_target,\",\"count\":1}]}")
DRIVER_SCIENTIFIC_SUFFIX_SHA256 = '3a34eeb13a52579aacafb1598c52a94a42f8db2cfab03a3fef0d64c2b88937d5'
KEYS = ('geometry','transfer','driver','launcher','reader')
ALLOWED_FUNCTION_CHANGES = {
    'geometry': set(),
    'transfer': {'definition','load_memory','validate_metadata'},
    'driver': {'main'},
    'launcher': {'main'},
    'reader': {'read_report'},
}
ADDED_FUNCTIONS = {'reader': {'independent_chart_binding'}}
ALLOWED_ASSIGNMENTS = {
    'geometry': {'CURRENT_MATERIAL_ENVELOPE_MEMORY_SHA256'},
    'transfer': {'SCHEMA','CURRENT_MEMORY_SOURCE_SHA256'},
    'driver': {'SCHEMA','SOURCE_PINS'},
    'launcher': {'DRIVER_SHA'},
    'reader': {'DRIVER_SHA','REPORT_SCHEMA'},
}

def sha_bytes(raw):
    return hashlib.sha256(raw).hexdigest()

def checked_source(path, expected, size=None):
    raw=Path(path).read_bytes()
    if sha_bytes(raw)!=expected or (size is not None and len(raw)!=size):
        raise ValueError('The entire actual source differs: '+str(path))
    return raw.decode('utf-8')

def function_nodes(tree):
    return {node.name: node for node in tree.body
        if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef))}

def declaration_body(tree, excluded):
    answer=[]
    for node in tree.body:
        if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)):
            continue
        if (isinstance(node,ast.Assign) and len(node.targets)==1
                and isinstance(node.targets[0],ast.Name) and node.targets[0].id in excluded):
            continue
        answer.append(ast.dump(node,include_attributes=False))
    return answer

def literal_assignment(source,name):
    values=[ast.literal_eval(node.value) for node in ast.parse(source).body
        if isinstance(node,ast.Assign) and len(node.targets)==1
        and isinstance(node.targets[0],ast.Name) and node.targets[0].id==name]
    if len(values)!=1:
        raise ValueError('Require one entire actual literal assignment '+name)
    return values[0]

def function_text(source,name):
    marker='def '+name+'('
    begin=source.find(marker)
    if begin<0:
        raise ValueError('Missing complete function '+name)
    next_function=source.find('\ndef ',begin+1)
    return source[begin:] if next_function<0 else source[begin:next_function]

def verify_ast(key,before,after):
    old=ast.parse(before);new=ast.parse(after)
    old_functions,new_functions=function_nodes(old),function_nodes(new)
    if len(old_functions)!=sum(isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)) for node in old.body):
        raise ValueError('Duplicate original top-level function/class name')
    if len(new_functions)!=sum(isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)) for node in new.body):
        raise ValueError('Duplicate new top-level function/class name')
    if set(new_functions)!=set(old_functions)|ADDED_FUNCTIONS.get(key,set()):
        raise ValueError('Unexpected removed/added complete function '+key)
    preserved=0
    for name,node in old_functions.items():
        if name not in ALLOWED_FUNCTION_CHANGES[key]:
            if ast.dump(node,include_attributes=False)!=ast.dump(new_functions[name],include_attributes=False):
                raise ValueError('An unchanged complete function/class differs: '+key+'/'+name)
            preserved+=1
    if declaration_body(old,ALLOWED_ASSIGNMENTS[key])!=declaration_body(new,ALLOWED_ASSIGNMENTS[key]):
        raise ValueError('An unrelated import/declaration changed: '+key)
    compile(after,EXPECTED[key]['path'],'exec')
    return preserved

def build(repo):
    topic=Path(repo).resolve()/'topics/visible-flex-larger-amplitude'
    for value in DEPENDENCIES.values():
        checked_source(topic/value['path'],value['sha256'])
    outputs={};record={}
    for key in KEYS:
        parent=PARENTS[key]
        before=checked_source(topic/parent['path'],parent['sha256'],parent['bytes'])
        after=before
        for change in PATCHES[key]:
            if after.count(change['old'])!=change['count']:
                raise ValueError('The complete exact parent fragment is not unique: '+key)
            after=after.replace(change['old'],change['new'])
        raw=after.encode()
        expected=EXPECTED[key]
        if len(raw)!=expected['bytes'] or sha_bytes(raw)!=expected['sha256']:
            raise ValueError('The entire derived body differs: '+key)
        preserved=verify_ast(key,before,after)
        if key=='driver':
            marker='    def save_report():'
            if before.count(marker)!=1 or after.count(marker)!=1:
                raise ValueError('The complete scientific suffix is not unique')
            original_suffix=before[before.index(marker):]
            actual_suffix=after[after.index(marker):]
            if (actual_suffix!=original_suffix
                    or sha_bytes(actual_suffix.encode())!=DRIVER_SCIENTIFIC_SUFFIX_SHA256):
                raise ValueError('All original complete scientific loops must stay byte-identical')
        if key=='transfer':
            for name in ('_compatible_models','seed_from_complete_prior_final','validate_seed_metadata'):
                if function_text(before,name)!=function_text(after,name):
                    raise ValueError('The original strict complete-source/model/seed guard changed')
        if key=='reader' and len(raw)>=100000:
            raise ValueError('The complete pure reader must remain under 100000 bytes')
        outputs[Path(expected['path']).name]=after
        record[key]=dict(parent=parent,output=dict(path=expected['path'],
            bytes=len(raw),sha256=sha_bytes(raw)),actual_entire_body_match=True,
            unchanged_complete_functions_and_classes=preserved)
    pins=literal_assignment(outputs[Path(EXPECTED['driver']['path']).name],'SOURCE_PINS')
    for role,(relative,digest) in pins.items():
        name=Path(relative).name
        if name in outputs:
            actual=sha_bytes(outputs[name].encode())
        else:
            actual=sha_bytes((topic/relative).read_bytes())
        if actual!=digest:
            raise ValueError('The complete recursive source-role closure differs: '+role)
    return outputs,dict(schema='complete-independent-fixed-chart-five-source-derivation-v1',
        source_sha256=sha_bytes(Path(__file__).read_bytes()),
        entire_sources=record,complete_source_role_count=len(pins),
        driver_scientific_suffix_sha256=DRIVER_SCIENTIFIC_SUFFIX_SHA256,
        all_original_physics_and_full_scientific_suffix_unchanged=True,
        old_strict_model_and_prior_final_seed_guards_byte_identical=True,
        explicit_new_fixed_chart_and_whole_target_binding=True,
        scientific_evaluations=0)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,required=True)
    parser.add_argument('--outdir',type=Path,required=True)
    parser.add_argument('--verify-existing',action='store_true')
    args=parser.parse_args()
    outputs,record=build(args.repo)
    if args.verify_existing:
        for name,text in outputs.items():
            path=args.outdir/name
            if path.read_bytes()!=text.encode():
                raise ValueError('The existing entire generated source differs: '+str(path))
    else:
        args.outdir.mkdir(parents=True,exist_ok=True)
        for name,text in outputs.items():
            path=args.outdir/name
            if path.exists() and path.read_bytes()!=text.encode():
                raise ValueError('Never overwrite another complete source: '+str(path))
            path.write_text(text,encoding='utf-8')
    print(json.dumps(record,sort_keys=True,allow_nan=False))

if __name__=='__main__':
    main()
