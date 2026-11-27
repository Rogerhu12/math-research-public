#!/usr/bin/env python3
"""Replay every complete actual-public09 N4096 analytic-frame/J3/packet source.

This is source construction only. It imports only the seven pinned stdlib
construction bodies, never the scientific bodies that they emit.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile

SCHEMA='complete-public09-N4096-analytic-frame-source-replay-v1'
EXPECTED = {'angular_observation_refinement.py': {'bytes': 11045,
                                       'sha256': '8506eb861bb8650ddfd0c5db5c268e8bb0a71b38e48ebb551767b45d2d339ab3'},
 'angular_refined_public_reference_adjacent_matrices.py': {'bytes': 36761,
                                                           'sha256': '5d8bc302e0bbbb48de1c47b7c7470a6904cc09c9dcda84a71c5f93455d8e9602'},
 'angular_refined_public_reference_calibration.py': {'bytes': 11886,
                                                     'sha256': 'dffb102d4daed36735a34f69e920c10fc41f5e8fb2aa606a0d86acda9cf6eeb9'},
 'angular_refined_public_reference_frame_c1.py': {'bytes': 35894,
                                                  'sha256': '65b3c988178c766c3715cd08c8200b93816067e316cd260ee7da254b890fada4'},
 'angular_refined_public_reference_history_transfer.py': {'bytes': 75765,
                                                          'sha256': 'bb47e4dcbaf4ae159d6ad04b5d1715a0093b934ba7b9896b4820f474febb78ce'},
 'angular_refined_public_reference_memory.py': {'bytes': 52209,
                                                'sha256': '74bd35b283434fca103b62f6dbaf93dc3a710fd7a962f239b67c6c3916aca385'},
 'angular_refined_public_reference_normal_frame.py': {'bytes': 33669,
                                                      'sha256': 'a3afa4762a0573a8eb3de026d56a0922977c6b5359b7567f322fa4c866f51aff'},
 'angular_refined_public_reference_source_binding.py': {'bytes': 28014,
                                                        'sha256': '0e00f37b2a504b05d5d7b5535e2bf06085f9715bd7f0992df2ad4589af85e140'},
 'angular_refined_public_reference_stage_jacobian.py': {'bytes': 24225,
                                                        'sha256': '7257ff8cb625ada848a41b1ce0d37bf88a0e095196dfb7ab072f210c3da030c4'},
 'angular_refined_public_reference_stage_matrices.py': {'bytes': 47775,
                                                        'sha256': '29c20d6831f15abac6b6701d4b471d75154b915c6739d9a0df84c79438c2928b'},
 'angular_refined_smooth_triangle_literal_zero_moment_input.py': {'bytes': 30940,
                                                                  'sha256': 'a4a53ff3ff92bb4fdbf8db2da048c717437d945423932e2b3d69cfc1cc06035d'},
 'fullclosed_angular_refined_public_reference_so3_qp.py': {'bytes': 86720,
                                                           'sha256': '3ff2a0bfd2c49847c0d17514842ee9542fccca050f0a054c4ee75a24cf33a9c5'},
 'immutable_angular_refined_public_reference_root_packets.py': {'bytes': 69730,
                                                                'sha256': 'ac34e4a1ded37726545fc743ca002706a8f40a1d5e3cf153472b9429559644cb'},
 'launch_angular_refined_public_reference_so3_actions.py': {'bytes': 21571,
                                                            'sha256': 'a4f36f7f89adc5b487bdaca683bec3518df5aa22cc18faf075165f93103c19da'},
 'read_angular_refined_public_reference_so3_report.py': {'bytes': 97289,
                                                         'sha256': '44053d738dd3b08525130487c2e2eb33c4839adc17bfb4ec294d16155e6523bb'},
 'so3_angular_refined_public_reference_envelope_geometry.py': {'bytes': 68856,
                                                               'sha256': 'a243377b5dccfdb6787d0053d6e835df8ca46697dddcd26a756f5b51559bc24b'},
 'so3_angular_refined_public_reference_normal_lift.py': {'bytes': 96515,
                                                         'sha256': 'ceaaab5f05c9faaddaff8174be9f97e9aa5b0936b9cf586990877433a9cce100'},
 'so3_angular_refined_smooth_triangle_meridian_operator.py': {'bytes': 41592,
                                                              'sha256': '1ba446d9283891cfbb8d3af319a27804b4889f4b7f5f2891dea0b101aa042529'}}
PARENTS = {'actual_public_reference_input_binding.py': {'bytes': 44907,
                                              'sha256': '306b5f86e0d287ea0c6cf9abb0f326f0eec869640b52daa59cf76db1492e382a'},
 'analytic_frame_adjacent_normal_matrices.py': {'bytes': 36761,
                                                'sha256': '3788b809c986668042e1c02f927afb85bf45434c4ff69607f9aaa2e2bf142695'},
 'analytic_frame_c1_reuse.py': {'bytes': 35894,
                                'sha256': 'f1c74928089b60fb8f5350084ace0805fa956f4b06ac0de3f6a11357dd1aa2fb'},
 'analytic_frame_detached_normal_stage_matrix_reuse.py': {'bytes': 47775,
                                                          'sha256': 'fa06705ebe19153edf455151a19c4217e42b8ab81ae3ffa4c1815701ec135255'},
 'analytic_frame_local_stage_jacobian.py': {'bytes': 24261,
                                            'sha256': '894efd3b277b8a8c1fbd4abcd68b573fb09ee10a706a90ded7b2e1894fe3b866'},
 'analytic_normal_frame_jets.py': {'bytes': 33705,
                                   'sha256': '4ed6dfb93bb15b864d79c227b852421bc69b888a32923b98a21fe816da5be3d8'},
 'angular_observation_refinement.py': {'bytes': 11045,
                                       'sha256': '8506eb861bb8650ddfd0c5db5c268e8bb0a71b38e48ebb551767b45d2d339ab3'},
 'angular_refined_smooth_triangle_literal_zero_moment_input.py': {'bytes': 30940,
                                                                  'sha256': 'a4a53ff3ff92bb4fdbf8db2da048c717437d945423932e2b3d69cfc1cc06035d'},
 'complete_material_envelope_memory_public_reference.py': {'bytes': 49349,
                                                           'sha256': '2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb'},
 'freeze_run09_public_reference_and_restore_run05_carrier.py': {'bytes': 47041,
                                                                'sha256': '9e3d0590c6d37eb07da094128df9e3b82fc03a7e9cf784cea1831b4ab0d39a18'},
 'fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py': {'bytes': 80726,
                                                                   'sha256': 'ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5'},
 'immutable_analytic_frame_normal_root_packets.py': {'bytes': 69148,
                                                     'sha256': '094ca6a87213a8677b46aa9b0ad4c5a4b12f8c4c80437d7b640c47f7793b40f0'},
 'launch_run09_public_reference_analytic_frame_actions_v2.py': {'bytes': 21359,
                                                                'sha256': 'c1888457b67c85185aebe6c91d2bd4942ccc2d2074407e17f7f54a2825927d23'},
 'read_run09_public_reference_analytic_frame_so3_report_v2.py': {'bytes': 97351,
                                                                 'sha256': 'aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32'},
 'reference_centred_analytic_frame_smooth_triangle_calibration.py': {'bytes': 11921,
                                                                     'sha256': 'fe422dbf2eac68bbc4f54e8fe290ba0e5d1b7a080f12f1d148cffe834957dba0'},
 'run09_public_reference_analytic_frame_binding.py': {'bytes': 26393,
                                                      'sha256': '15f6393acb1f069e3c5dee62708f9350b3e329b877b19fc8a69868365a45a592'},
 'so3_angular_refined_smooth_triangle_meridian_operator.py': {'bytes': 41592,
                                                              'sha256': '1ba446d9283891cfbb8d3af319a27804b4889f4b7f5f2891dea0b101aa042529'},
 'so3_reference_centred_analytic_frame_smooth_triangle_normal_lift_operator.py': {'bytes': 96558,
                                                                                  'sha256': '3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc'},
 'so3_run09_public_reference_analytic_frame_geometry_v2.py': {'bytes': 68903,
                                                              'sha256': 'e89dcfa368da67d6522a9df7dd5b49e58915db89bbc8152e15bc0a7a7c557a13'},
 'transfer_run09_public_reference_analytic_frame_memory.py': {'bytes': 64221,
                                                              'sha256': '6deeeaa1dcbbb0fbfd968d0b31443798909536a55a7ea498f661e08496a27707'}}
CONSTRUCTION = {'derive_public_reference_angular_binding.py': {'bytes': 4375,
                                                'sha256': 'f791d0834ad49f4dd38cf658d285b5a80a51a6359926640aae31c0de8ef32c0a'},
 'derive_public_reference_angular_entry.py': {'bytes': 11991,
                                              'sha256': 'a36ed844fd11075c46de490719e0731ea9652b3e57798941667e9faf7c2599ea'},
 'derive_public_reference_angular_refined_core.py': {'bytes': 8234,
                                                     'sha256': '86fb688fb826939c90e9fcd949394ed17d1aedca264fc35774ead3eabbccd057'},
 'derive_public_reference_angular_refined_memory.py': {'bytes': 9664,
                                                       'sha256': 'e0a744d05b520098d54cd4aa4235da7e493cdcfe2f7152091d0788e93cc2a3a9'},
 'derive_public_reference_angular_transfer.py': {'bytes': 17701,
                                                 'sha256': '0da7f43a9099c2c1e7be9ac9cc1ce47d64b8a0f6c48f478566680c5f4ff4a434'},
 'public_reference_angular_binding_additions.py': {'bytes': 7217,
                                                   'sha256': 'ab6d03bddd6a72b45faf965e4c2ead2eebcbccf3349fd1e5e28011c18562859c'},
 'public_reference_angular_transfer_additions.py': {'bytes': 9290,
                                                    'sha256': 'fc461a3c2448198157c4c329fcd6147f093f70622572a61d10022d71e418f640'}}


def record(path):
    value=Path(path).read_bytes()
    return dict(bytes=len(value),sha256=hashlib.sha256(value).hexdigest())


def source(path, expected):
    if record(path)!=expected:
        raise ValueError('The whole source differs: '+str(path))
    return Path(path).read_text()


def load(directory,name):
    path=directory/name
    text=source(path,CONSTRUCTION[name])
    # These are complete source constructors. No emitted scientific module is
    # imported, and the two additions files are read as source text only.
    for node in ast.walk(ast.parse(text)):
        if isinstance(node,(ast.Import,ast.ImportFrom)):
            names=[v.name for v in node.names] if isinstance(node,ast.Import) else [node.module or '']
            if any(v.split('.')[0] in ('numpy','torch','scipy') for v in names):
                raise ValueError('A source constructor must remain pure stdlib')
    module_name='_whole_source_replay_'+CONSTRUCTION[name]['sha256']
    spec=importlib.util.spec_from_file_location(module_name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[module_name]=module
    spec.loader.exec_module(module)
    return module


def check_source(text,name):
    tree=ast.parse(text,filename=name)
    compile(tree,name,'exec')
    if len(text.encode())>=100000 or any(v.rstrip()!=v for v in text.splitlines()):
        raise ValueError('Source size or whitespace contract: '+name)
    for node in ast.walk(tree):
        if isinstance(node,ast.Dict):
            values=[v.value for v in node.keys if isinstance(v,ast.Constant) and isinstance(v.value,(str,int))]
            if len(values)!=len(set(values)):
                raise ValueError('Duplicate literal dictionary key: '+name)
        elif isinstance(node,ast.Call):
            values=[v.arg for v in node.keywords if v.arg is not None]
            if len(values)!=len(set(values)):
                raise ValueError('Duplicate literal keyword: '+name)


def replay(topic,construction):
    directory=topic/'scripts/resume_20261126'
    for name,expected in PARENTS.items():source(directory/name,expected)
    for name,expected in CONSTRUCTION.items():source(construction/name,expected)
    core=load(construction,'derive_public_reference_angular_refined_core.py')
    memory=load(construction,'derive_public_reference_angular_refined_memory.py')
    binding=load(construction,'derive_public_reference_angular_binding.py')
    transfer=load(construction,'derive_public_reference_angular_transfer.py')
    entry=load(construction,'derive_public_reference_angular_entry.py')
    with tempfile.TemporaryDirectory(prefix='complete-N4096-source-only-') as temporary:
        output=Path(temporary)
        values=core.derive(directory,directory)
        for name,text in values.items():(output/name).write_text(text)
        name='angular_refined_public_reference_memory.py'
        values[name]=memory.derive((directory/'complete_material_envelope_memory_public_reference.py').read_text(),
            (output/'angular_observation_refinement.py').read_text())
        (output/name).write_text(values[name])
        name='angular_refined_public_reference_source_binding.py'
        values[name]=binding.derive((directory/'run09_public_reference_analytic_frame_binding.py').read_text(),
            (directory/'read_run09_public_reference_analytic_frame_so3_report_v2.py').read_text(),
            (construction/'public_reference_angular_binding_additions.py').read_text(),output)
        (output/name).write_text(values[name])
        name='angular_refined_public_reference_history_transfer.py'
        values[name]=transfer.derive((directory/'transfer_run09_public_reference_analytic_frame_memory.py').read_text(),
            (construction/'public_reference_angular_transfer_additions.py').read_text(),output)
        (output/name).write_text(values[name])
        values.update(entry.derive(directory,output))
        if set(values)!=set(EXPECTED):raise ValueError('The complete runtime inventory changed')
        for name,text in values.items():
            check_source(text,name)
            actual=dict(bytes=len(text.encode()),sha256=hashlib.sha256(text.encode()).hexdigest())
            if actual!=EXPECTED[name]:raise ValueError('The exact complete derived body differs: '+name)
        driver=ast.parse(values['fullclosed_angular_refined_public_reference_so3_qp.py'])
        pins=None
        for node in driver.body:
            if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='SOURCE_PINS' for t in node.targets):
                pins=ast.literal_eval(node.value)
        if not isinstance(pins,dict) or len(pins)!=75:raise ValueError('Keep all 75 actual source roles')
        for role,(relative,expected) in pins.items():
            if relative=='scripts/resume_20261126/'+Path(relative).name and Path(relative).name in values:
                actual=hashlib.sha256(values[Path(relative).name].encode()).hexdigest()
            else:actual=record(topic/relative)['sha256']
            if actual!=expected:raise ValueError('A complete runtime role differs: '+role)
    return values


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--topic-directory',type=Path,required=True)
    parser.add_argument('--construction-directory',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--output-directory',type=Path,required=True)
    parser.add_argument('--verify-existing',action='store_true')
    args=parser.parse_args()
    values=replay(args.topic_directory.resolve(),args.construction_directory.resolve())
    if not args.verify_existing:args.output_directory.mkdir(parents=True,exist_ok=True)
    for name,text in values.items():
        path=args.output_directory/name
        if args.verify_existing:
            if path.read_text()!=text:raise ValueError('The complete existing runtime source differs: '+name)
        else:path.write_text(text)
    print(json.dumps(dict(schema=SCHEMA,complete_runtime_source_count=len(values),
        complete_actual_runtime_source_role_count=75,complete_parent_source_count=len(PARENTS),
        complete_construction_source_count=len(CONSTRUCTION),source_only_AST_and_compile=True,
        scientific_modules_imported=False,scientific_or_fixture_execution=False,
        verify_existing=args.verify_existing,complete_runtime_sources=EXPECTED),sort_keys=True))


if __name__=='__main__':main()
