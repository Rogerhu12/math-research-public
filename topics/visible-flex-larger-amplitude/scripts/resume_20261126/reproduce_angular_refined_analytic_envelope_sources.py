#!/usr/bin/env python3
"""Replay all complete N4096 / independent-chart / analytic-J3 / packet sources.

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

SCHEMA='complete-N4096-independent-chart-analytic-J3-source-replay-v1'
EXPECTED = {'angular_observation_refinement.py': {'bytes': 11045,
                                       'sha256': '8506eb861bb8650ddfd0c5db5c268e8bb0a71b38e48ebb551767b45d2d339ab3'},
 'angular_refined_analytic_adjacent_matrices.py': {'bytes': 36734,
                                                   'sha256': '032c69fad6425c7b70d75d288884fff293eaa76b2e1fdfb822b87f2d2b9febfd'},
 'angular_refined_analytic_calibration.py': {'bytes': 11890,
                                             'sha256': '186798d2d31924941f7917c32afb856d584ca13dfea8602798e5206e0489af93'},
 'angular_refined_analytic_frame_c1.py': {'bytes': 35625,
                                          'sha256': 'aeda86f6c10054f79758174d978356fc046881b5f3aba9aea91c4b2b50617f35'},
 'angular_refined_analytic_history_transfer.py': {'bytes': 74332,
                                                  'sha256': '26e40b278a83a93fc3214af05656f2a3a8b5148f94a6a0f01619eed83a714918'},
 'angular_refined_analytic_normal_stage_jacobian.py': {'bytes': 24218,
                                                       'sha256': 'f497452ff23188bca80556773f7493418e3f60b94108af5e5c92956c82e544b7'},
 'angular_refined_analytic_source_binding.py': {'bytes': 22857,
                                                'sha256': '48fecda3f3da2fda7eee3dc37e120ba89448bde7539d2f90c89f4b6791587ef5'},
 'angular_refined_analytic_stage_matrices.py': {'bytes': 47673,
                                                'sha256': '0ac33e262d4bb95f84f548b630c955e481430d2cf4b899ec7829bafea845ab3d'},
 'angular_refined_independent_chart_memory.py': {'bytes': 51425,
                                                 'sha256': '9cf973b75c108ecfee4a5beef792ab81b682e8ba71cf667b2d068bb0c33f0f2e'},
 'angular_refined_smooth_triangle_literal_zero_moment_input.py': {'bytes': 30940,
                                                                  'sha256': 'a4a53ff3ff92bb4fdbf8db2da048c717437d945423932e2b3d69cfc1cc06035d'},
 'fullclosed_angular_refined_analytic_envelope_so3_qp.py': {'bytes': 83420,
                                                            'sha256': 'fbabe2dc44f5f7f406549aaea567892809e139d07eadea4fccbd8f0e6e9dc819'},
 'immutable_angular_refined_analytic_root_packets.py': {'bytes': 67590,
                                                        'sha256': 'fa1f8b0219610602e8c695482e3303c1df6dee7ac3402648e7579ff1f988688c'},
 'launch_angular_refined_analytic_envelope_so3_actions.py': {'bytes': 21572,
                                                             'sha256': 'bf460b1a103b394874b2a898ab9f84eefb1abf1fdb57cfc87334135249ea34c3'},
 'read_angular_refined_analytic_envelope_so3_report.py': {'bytes': 97700,
                                                          'sha256': '820274bec9f54c017e9473f1f0db2ec5bc38f7a1a91be8b9b6162b76ef39d692'},
 'so3_angular_refined_analytic_envelope_geometry.py': {'bytes': 68907,
                                                       'sha256': 'd04ed9db9756610ab725bcef6e4199611c46cbcc2d7a7e3cf69bd80803eaeefd'},
 'so3_angular_refined_analytic_normal_lift.py': {'bytes': 96877,
                                                 'sha256': '361df1bcd7034616d3c0830a20444896dd3992a0d1295ec01ab690f94a61262b'},
 'so3_angular_refined_smooth_triangle_meridian_operator.py': {'bytes': 41592,
                                                              'sha256': '1ba446d9283891cfbb8d3af319a27804b4889f4b7f5f2891dea0b101aa042529'}}
PARENTS = {'analytic_j3_adjacent_normal_frame_matrices.py': {'bytes': 36734,
                                                   'sha256': '8a63cc1817fd0853c2b7ee69b64e3083de22106c239b62acc602ad9b69698787'},
 'analytic_j3_detached_normal_stage_matrix_reuse.py': {'bytes': 47673,
                                                       'sha256': '5db725b423db4e97229a697ff6ce712b9183236070000e8ed66ed45cbe1767c1'},
 'analytic_j3_normal_frame_c1_reuse.py': {'bytes': 35625,
                                          'sha256': '8e6c3f255a6acbd27aa1291c1a8b0555eeaaeb869a58fde6a49b3fc5d16361f8'},
 'analytic_j3_source_and_report_binding.py': {'bytes': 14308,
                                              'sha256': 'f34fcafc06b50594b7a651a90e38553ea8ae3da5b6ac8b6ca4ea691d2ab9f14f'},
 'analytic_normal_stage_jacobian.py': {'bytes': 24240,
                                       'sha256': '64b39a8be75ee976dbf4b49768e4ebaf37a372f77dba397a439a054cc4e7465d'},
 'angular_observation_refinement.py': {'bytes': 11045,
                                       'sha256': '8506eb861bb8650ddfd0c5db5c268e8bb0a71b38e48ebb551767b45d2d339ab3'},
 'angular_refined_smooth_triangle_literal_zero_moment_input.py': {'bytes': 30940,
                                                                  'sha256': 'a4a53ff3ff92bb4fdbf8db2da048c717437d945423932e2b3d69cfc1cc06035d'},
 'complete_material_envelope_memory_independent_chart.py': {'bytes': 48544,
                                                            'sha256': '4d92ca2387523a76bbea0a3444e0665c306369dd0351c3354c998a09884e043b'},
 'freeze_run08_fixed_chart_and_restore_run05_carrier.py': {'bytes': 61371,
                                                           'sha256': '105289ba7c454f671c8eae086b31a4ea01b06978101503cd0ef283320fc85361'},
 'fullclosed_reference_centred_analytic_j3_material_envelope_so3_qp.py': {'bytes': 78907,
                                                                          'sha256': '0dfb96e53fa92e741e2d94819636486b45c49e341006370d1c6864ce70c36b51'},
 'fullclosed_reference_centred_independent_chart_material_envelope_so3_qp.py': {'bytes': 75152,
                                                                                'sha256': '95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9'},
 'immutable_analytic_normal_root_packets_v2.py': {'bytes': 67095,
                                                  'sha256': '1e0656b19de4eb78937a9f8305569d7c1cce59f48614fb7a279738942bcd622e'},
 'launch_reference_centred_analytic_j3_material_envelope_so3_actions.py': {'bytes': 21366,
                                                                           'sha256': '6228512d27d54027edf6985b640d74edac9a79c8ddb5e386b0b064e362bdb797'},
 'read_reference_centred_analytic_j3_material_envelope_so3_report.py': {'bytes': 99527,
                                                                        'sha256': 'c2a6039633dbb397bdb6f56358153a362ed4e34c8e035a6a739eb23d5a1b785e'},
 'read_reference_centred_independent_chart_material_envelope_so3_report.py': {'bytes': 98389,
                                                                              'sha256': 'f382bedb07fdf43e3fd94ac411c4a072519494dd2a16ec19ab627492d9606470'},
 'reference_centred_analytic_j3_smooth_triangle_calibration.py': {'bytes': 11911,
                                                                  'sha256': '4c3fb7a6d19a9c214e2dc69428456b62bc406c8329bc60083e1f5f8be3ff3d6d'},
 'so3_angular_refined_smooth_triangle_meridian_operator.py': {'bytes': 41592,
                                                              'sha256': '1ba446d9283891cfbb8d3af319a27804b4889f4b7f5f2891dea0b101aa042529'},
 'so3_reference_centred_analytic_j3_material_envelope_geometry.py': {'bytes': 68945,
                                                                     'sha256': '781778dc41303e5c8555df46e774e74e6c96fe2fa4ab3cb2bc3d4d0dccaae50a'},
 'so3_reference_centred_analytic_j3_smooth_triangle_normal_lift_operator.py': {'bytes': 96906,
                                                                               'sha256': '04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e'},
 'so3_supported_smooth_triangle_meridian_operator.py': {'bytes': 40771,
                                                        'sha256': '6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865'},
 'supported_smooth_triangle_literal_zero_moment_input.py': {'bytes': 30950,
                                                            'sha256': '307ebae301db059f30ff1cc5fda024b09e9c2730c9f6bffbd82f0821d2a727a7'},
 'transfer_material_envelope_memory_to_analytic_j3.py': {'bytes': 62891,
                                                         'sha256': '0d2a5e9c9f5651e149d53da859ac42ced1c3b44709f9a5a3416a82c8d8702608'}}
CONSTRUCTION = {'angular_refined_analytic_binding_additions.py': {'bytes': 9790,
                                                   'sha256': '0a083f3b9b13f2bc4f0348bc921da79cf3d3e6fb6d1c80f827f81d1e58269441'},
 'angular_refined_analytic_transfer_additions.py': {'bytes': 9293,
                                                    'sha256': 'cb93ac26c815d1ef63b1e0189d9fc6b676830e2b1433ccbe63addec55897d93b'},
 'derive_angular_refined_analytic_binding.py': {'bytes': 4055,
                                                'sha256': 'dfb2d2827d92425221c074225c8276f97f1eeed19c70437064bb9ca661fac5dd'},
 'derive_angular_refined_analytic_core.py': {'bytes': 7939,
                                             'sha256': '7589244c33cfb2a50eb6b4de591eac5d32e2d006c2813f7fb4b44b950328de20'},
 'derive_angular_refined_analytic_entry.py': {'bytes': 12093,
                                              'sha256': 'e7297df79517eafbae6bb5732dff80c88aeb52c495bac280e5d6ae3bf1f1f2ca'},
 'derive_angular_refined_analytic_transfer.py': {'bytes': 16738,
                                                 'sha256': '1cb77244f50273b2c6a127a5ae7065975af74ec0e3fe2168aeceeb758339d3e8'},
 'derive_angular_refined_independent_chart_memory.py': {'bytes': 9689,
                                                        'sha256': '1531b66b87787b02c1a94bbf0610366e978856b008824f86551c5e01e97ddfaf'}}


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
    core=load(construction,'derive_angular_refined_analytic_core.py')
    memory=load(construction,'derive_angular_refined_independent_chart_memory.py')
    binding=load(construction,'derive_angular_refined_analytic_binding.py')
    transfer=load(construction,'derive_angular_refined_analytic_transfer.py')
    entry=load(construction,'derive_angular_refined_analytic_entry.py')
    with tempfile.TemporaryDirectory(prefix='complete-N4096-source-only-') as temporary:
        output=Path(temporary)
        values=core.derive(directory,directory)
        for name,text in values.items():(output/name).write_text(text)
        name='angular_refined_independent_chart_memory.py'
        values[name]=memory.derive((directory/'complete_material_envelope_memory_independent_chart.py').read_text(),
            (output/'angular_observation_refinement.py').read_text())
        (output/name).write_text(values[name])
        name='angular_refined_analytic_source_binding.py'
        values[name]=binding.derive((directory/'analytic_j3_source_and_report_binding.py').read_text(),
            (directory/'read_reference_centred_analytic_j3_material_envelope_so3_report.py').read_text(),
            (construction/'angular_refined_analytic_binding_additions.py').read_text(),output)
        (output/name).write_text(values[name])
        name='angular_refined_analytic_history_transfer.py'
        values[name]=transfer.derive((directory/'transfer_material_envelope_memory_to_analytic_j3.py').read_text(),
            (construction/'angular_refined_analytic_transfer_additions.py').read_text(),output)
        (output/name).write_text(values[name])
        values.update(entry.derive(directory,output))
        if set(values)!=set(EXPECTED):raise ValueError('The complete runtime inventory changed')
        for name,text in values.items():
            check_source(text,name)
            actual=dict(bytes=len(text.encode()),sha256=hashlib.sha256(text.encode()).hexdigest())
            if actual!=EXPECTED[name]:raise ValueError('The exact complete derived body differs: '+name)
        driver=ast.parse(values['fullclosed_angular_refined_analytic_envelope_so3_qp.py'])
        pins=None
        for node in driver.body:
            if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='SOURCE_PINS' for t in node.targets):
                pins=ast.literal_eval(node.value)
        if not isinstance(pins,dict) or len(pins)!=64:raise ValueError('Keep all 64 actual source roles')
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
        complete_actual_runtime_source_role_count=64,complete_parent_source_count=len(PARENTS),
        complete_construction_source_count=len(CONSTRUCTION),source_only_AST_and_compile=True,
        scientific_modules_imported=False,scientific_or_fixture_execution=False,
        verify_existing=args.verify_existing,complete_runtime_sources=EXPECTED),sort_keys=True))


if __name__=='__main__':main()
