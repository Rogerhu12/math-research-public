#!/usr/bin/env python3
"""Pure complete reproduction of immutable-root-packet entry hooks.

No scientific module is imported or executed. The original full entry source,
all physical methods, every QP/Phase-I step, and the complete true line screening
are preserved after removing only the explicit read-only packet statements.
"""
import argparse
import ast
import copy
import hashlib
import json
from pathlib import Path

PARENTS = json.loads("{\"driver\":{\"path\":\"scripts/resume_20261126/fullclosed_reference_centred_independent_chart_material_envelope_so3_qp.py\",\"sha256\":\"95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9\",\"bytes\":75152},\"launcher\":{\"path\":\"scripts/resume_20261126/launch_reference_centred_independent_chart_material_envelope_so3_actions.py\",\"sha256\":\"10422033f229649aa2e8237c25880670219d618d24690d429025347fd73f039b\",\"bytes\":20746},\"reader\":{\"path\":\"scripts/resume_20261126/read_reference_centred_independent_chart_material_envelope_so3_report.py\",\"sha256\":\"f382bedb07fdf43e3fd94ac411c4a072519494dd2a16ec19ab627492d9606470\",\"bytes\":98389}}")
EXPECTED = json.loads("{\"driver\":{\"path\":\"scripts/resume_20261126/fullclosed_reference_centred_independent_chart_root_packets_so3_qp_v2.py\",\"sha256\":\"86b12daa9401bfdd79ab61e44814d1596633835504e5b4f966b3e9308d9b6ba7\",\"bytes\":76471},\"launcher\":{\"path\":\"scripts/resume_20261126/launch_reference_centred_independent_chart_root_packets_so3_actions_v2.py\",\"sha256\":\"114841d141e7a8eee4f3c0719eace929292432b23147ae109228d63b9ebf3872\",\"bytes\":20744},\"reader\":{\"path\":\"scripts/resume_20261126/read_reference_centred_independent_chart_root_packets_so3_report_v2.py\",\"sha256\":\"3d99c6097e329a0f3bd03845403566654531657604b8f533002575a2e548284b\",\"bytes\":99080}}")
HELPER = json.loads("{\"path\":\"scripts/resume_20261126/immutable_normal_root_packets_with_entry_binding_v2.py\",\"sha256\":\"ef0d00b4e07b34283b0c73591fb985b7879a4f221f74895eff7a11a0d2db06b1\",\"bytes\":65063}")
PATCHES = json.loads("{\"driver\":[{\"old\":\"SCHEMA = 'complete-R711-reference-centred-independent-chart-material-envelope-fixed-normal-plane-SO3-QP-v1'\",\"new\":\"SCHEMA = 'complete-R711-reference-centred-independent-chart-root-packets-SO3-QP-v2'\",\"count\":1},{\"old\":\"SOURCE_PINS = {\",\"new\":\"SOURCE_PINS = {'root_packets': ('scripts/resume_20261126/immutable_normal_root_packets_with_entry_binding_v2.py',\\n                   'ef0d00b4e07b34283b0c73591fb985b7879a4f221f74895eff7a11a0d2db06b1'), \",\"count\":1},{\"old\":\"    qp = load('_so3_complete_QPv3', paths['qp'])\\n\",\"new\":\"    qp = load('_so3_complete_QPv3', paths['qp'])\\n    root_packets = load('_actual_immutable_normal_root_packets', paths['root_packets'])\\n\",\"count\":1},{\"old\":\"    initial_envelope_metadata=envelope.metadata()\\n\",\"new\":\"    packet_recorder = root_packets.NormalRootPacketRecorder(q,repo=args.repo,\\n        outdir=args.outdir/'immutable-normal-root-packets',caller_source=__file__,source_paths=paths)\\n    initial_envelope_metadata=envelope.metadata()\\n\",\"count\":1},{\"old\":\"        complete=False, independent_preparation_report=file_record(args.preparation_report),\\n\",\"new\":\"        complete=False, independent_preparation_report=file_record(args.preparation_report),\\n        normal_root_packet_source=file_record(paths['root_packets']),\\n        normal_root_packet_definition=root_packets.definition(),normal_root_packet_record_only=True,\\n        normal_root_packets=packet_recorder.metadata(),normal_root_packet_latest_entry_capture=None,\\n\",\"count\":1},{\"old\":\"        report['latest_operator_metadata'] = q.metadata()\\n\",\"new\":\"        report['latest_operator_metadata'] = q.metadata()\\n        report['normal_root_packet_latest_entry_capture'] = packet_recorder.capture_entry(\\n            report['latest_operator_metadata'],outer_full_point_sha256=meridian.array_sha(x),\\n            witnesses=witnesses,radius_witnesses=radius_witnesses,label='actual-report-save')\\n        report['normal_root_packets'] = packet_recorder.metadata()\\n\",\"count\":1},{\"old\":\"        record['actual_QP_operator_counts'] = {key: q.counts[key]-qp_counts_before[key] for key in q.counts}\\n\",\"new\":\"        record['actual_QP_operator_counts'] = {key: q.counts[key]-qp_counts_before[key] for key in q.counts}\\n        record['normal_root_packet_at_QP_return'] = packet_recorder.capture_entry(q.metadata(),\\n            outer_full_point_sha256=meridian.array_sha(x),witnesses=witnesses,\\n            radius_witnesses=radius_witnesses,label=phase+'-QP-return-'+str(record['serial']))\\n\",\"count\":1}],\"launcher\":[{\"old\":\"DRIVER_SHA = '95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9'\",\"new\":\"DRIVER_SHA = '86b12daa9401bfdd79ab61e44814d1596633835504e5b4f966b3e9308d9b6ba7'\",\"count\":1},{\"old\":\"fullclosed_reference_centred_independent_chart_material_envelope_so3_qp.py\",\"new\":\"fullclosed_reference_centred_independent_chart_root_packets_so3_qp_v2.py\",\"count\":1}],\"reader\":[{\"old\":\"DRIVER_SHA = '95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9'\",\"new\":\"DRIVER_SHA = '86b12daa9401bfdd79ab61e44814d1596633835504e5b4f966b3e9308d9b6ba7'\",\"count\":1},{\"old\":\"REPORT_SCHEMA = 'complete-R711-reference-centred-independent-chart-material-envelope-fixed-normal-plane-SO3-QP-v1'\",\"new\":\"REPORT_SCHEMA = 'complete-R711-reference-centred-independent-chart-root-packets-SO3-QP-v2'\",\"count\":1},{\"old\":\"fullclosed_reference_centred_independent_chart_material_envelope_so3_qp.py\",\"new\":\"fullclosed_reference_centred_independent_chart_root_packets_so3_qp_v2.py\",\"count\":1},{\"old\":\"\\ndef read_report(repo, report_path, *, verify_final_bundle=False):\",\"new\":\"\\ndef root_packet_binding(report, path):\\n    expected=report['source_sha256_by_role']['root_packets']\\n    if sha(path)!=expected:raise ValueError('Changed complete immutable packet recorder source')\\n    spec=importlib.util.spec_from_file_location('_actual_root_packet_reader_'+expected,path)\\n    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)\\n    if sha(module.validate_entry_report.__code__.co_filename)!=expected:\\n        raise ValueError('Use the complete source-bound pure packet validator')\\n    return module.validate_entry_report(report,reread_packets=True,reread_arrays=True)\\n\\n\\ndef read_report(repo, report_path, *, verify_final_bundle=False):\",\"count\":1},{\"old\":\"    independent_target=independent_chart_binding(report,envelope_binding)\\n\",\"new\":\"    independent_target=independent_chart_binding(report,envelope_binding)\\n    root_packets=root_packet_binding(report,topic/load_pins(driver)['root_packets'][0])\\n\",\"count\":1},{\"old\":\"schema='actual-complete-R711-reference-centred-independent-chart-material-envelope-normal-plane-SO3-scalar-readout-v1'\",\"new\":\"schema='actual-complete-R711-reference-centred-independent-chart-root-packets-SO3-scalar-readout-v2'\",\"count\":1},{\"old\":\"        reference_centering=centered_binding,\\n\",\"new\":\"        reference_centering=centered_binding, normal_root_packets=root_packets,\\n\",\"count\":1}]}")

KEYS = ('driver','launcher','reader')
TOPIC = 'topics/visible-flex-larger-amplitude'
ORIGINAL_SCIENTIFIC_SUFFIX_SHA256 = '3a34eeb13a52579aacafb1598c52a94a42f8db2cfab03a3fef0d64c2b88937d5'
REPORT_KEYS = {'normal_root_packet_source','normal_root_packet_definition',
    'normal_root_packet_record_only','normal_root_packets','normal_root_packet_latest_entry_capture'}
HOOK_TARGETS = REPORT_KEYS | {'normal_root_packet_at_QP_return'}

def sha_text(value):
    return hashlib.sha256(value.encode()).hexdigest()

def read_source(path,expected):
    raw=Path(path).read_bytes()
    if len(raw)!=expected['bytes'] or hashlib.sha256(raw).hexdigest()!=expected['sha256']:
        raise ValueError('Changed whole source '+str(path))
    return raw.decode('utf-8')

def replace_all(key,source,reverse=False):
    changes=list(PATCHES[key])
    if reverse:changes.reverse()
    for change in changes:
        old,new=(change['new'],change['old']) if reverse else (change['old'],change['new'])
        if source.count(old)!=change['count']:
            raise ValueError('The complete declared replacement is not unique: '+key)
        source=source.replace(old,new)
    return source

def functions(source):
    return {node.name:node for node in ast.parse(source).body
            if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef))}

def dump(node):
    return ast.dump(node,include_attributes=False)

class RemoveOnlyReadOnlyHooks(ast.NodeTransformer):
    def visit_Assign(self,node):
        for target in node.targets:
            if isinstance(target,ast.Name) and target.id in {'root_packets','packet_recorder'}:
                return None
            if (isinstance(target,ast.Subscript) and isinstance(target.value,ast.Name)
                    and target.value.id in {'report','record'} and isinstance(target.slice,ast.Constant)
                    and target.slice.value in HOOK_TARGETS):
                return None
        return self.generic_visit(node)

    def visit_keyword(self,node):
        if node.arg in REPORT_KEYS:return None
        return self.generic_visit(node)

def verify_preservation(key,before,after):
    if replace_all(key,after,reverse=True)!=before:
        raise ValueError('Inverse patches must restore every original source byte')
    old,new=functions(before),functions(after)
    if key=='driver':
        if set(old)!=set(new):raise ValueError('No original complete driver function may be replaced')
        for name in old:
            actual=RemoveOnlyReadOnlyHooks().visit(copy.deepcopy(new[name])) if name=='main' else new[name]
            if dump(actual)!=dump(old[name]):
                raise ValueError('A scientific driver AST changed beyond the explicit packet statements: '+name)
        original=before[before.index('    def save_report():'):]
        restored=replace_all(key,after,reverse=True)
        if (sha_text(original)!=ORIGINAL_SCIENTIFIC_SUFFIX_SHA256
                or restored[restored.index('    def save_report():'):]!=original):
            raise ValueError('Preserve the entire scientific suffix around the two actual read-only hooks')
    elif key=='reader':
        if set(new)!=set(old)|{'root_packet_binding'}:
            raise ValueError('Keep every complete pure source/geometry/normal-chain validator')
        for name in old:
            if name!='read_report' and dump(new[name])!=dump(old[name]):
                raise ValueError('An existing pure validator changed: '+name)
    elif key=='launcher':
        if dump(old['parse_args'])!=dump(new['parse_args']):
            raise ValueError('Keep every original scientific argument and budget')

def literal_pins(source):
    values=[ast.literal_eval(n.value) for n in ast.parse(source).body if isinstance(n,ast.Assign)
            and len(n.targets)==1 and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='SOURCE_PINS']
    if len(values)!=1:raise ValueError('Exactly one complete literal source registry is required')
    return values[0]

def build(repo,*,helper_source=None):
    topic=Path(repo).resolve()/TOPIC
    helper_path=Path(helper_source).resolve() if helper_source is not None else topic/HELPER['path']
    helper=read_source(helper_path,HELPER)
    ast.parse(helper)
    result={};original={}
    for key in KEYS:
        original[key]=read_source(topic/PARENTS[key]['path'],PARENTS[key])
        value=replace_all(key,original[key])
        if len(value.encode())!=EXPECTED[key]['bytes'] or sha_text(value)!=EXPECTED[key]['sha256']:
            raise ValueError('The entire new entry differs from its final locked source '+key)
        ast.parse(value);verify_preservation(key,original[key],value)
        result[key]=value
    old_pins=literal_pins(original['driver']);new_pins=literal_pins(result['driver'])
    expected=dict(old_pins,root_packets=(HELPER['path'],HELPER['sha256']))
    if new_pins!=expected:
        raise ValueError('Preserve every physical source role and add only the actual root-packet source')
    for role,(relative,digest) in old_pins.items():
        if hashlib.sha256((topic/relative).read_bytes()).hexdigest()!=digest:
            raise ValueError('The full unchanged scientific dependency differs: '+role)
    for key in ('reader','launcher'):
        values=[ast.literal_eval(n.value) for n in ast.parse(result[key]).body if isinstance(n,ast.Assign)
            and len(n.targets)==1 and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='DRIVER_SHA']
        if values!=[EXPECTED['driver']['sha256']]:
            raise ValueError('The complete reader/launcher must bind the real new driver')
    if EXPECTED['reader']['bytes']>=100000:raise ValueError('Keep the full reader below the repository file cap')
    result['helper']=helper
    return result

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--outdir',type=Path,required=True)
    p.add_argument('--helper-source',type=Path)
    p.add_argument('--verify-existing',action='store_true')
    args=p.parse_args()
    values=build(args.repo,helper_source=args.helper_source)
    args.outdir.mkdir(parents=True,exist_ok=True)
    for key,source in values.items():
        expected=HELPER if key=='helper' else EXPECTED[key]
        output=args.outdir/Path(expected['path']).name
        if args.verify_existing:
            if not output.is_file() or output.read_bytes()!=source.encode():
                raise ValueError('The entire existing generated source differs: '+str(output))
        else:
            if output.exists() and output.read_bytes()!=source.encode():
                raise FileExistsError('Never replace different source bytes: '+str(output))
            output.write_bytes(source.encode())
        print(json.dumps(dict(key=key,path=str(output),bytes=len(source.encode()),sha256=sha_text(source),
            whole_source_reproduced=True,scientific_module_imports=0,scientific_evaluations=0),sort_keys=True))

if __name__=='__main__':
    main()
