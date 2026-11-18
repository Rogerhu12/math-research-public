#!/usr/bin/env python3
"""Compact compile-only/native-baseline entry evidence without loading a library."""
import argparse
import json
from pathlib import Path
import struct
import hashlib
from record_fixed_actual import load, sha


def ident(path):
    return dict(path=str(Path(path).resolve()),sha256=sha(path))


def checked(ref):
    if sha(ref['path'])!=ref['sha256']:
        raise ValueError('An entry source/input changed: '+ref['path'])
    return load(ref['path'])


def packed_hash(values):
    return hashlib.sha256(struct.pack('<'+'d'*len(values),*values)).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('build','plan','out'):
        p.add_argument('--'+key,type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise ValueError('Preserve prior entry record')
    build,plan=load(a.build),load(a.plan)
    if build['status']!='compile_success_no_execution' or not build['no_new_flow_or_Jacobian']:
        raise ValueError('This entry is compilation only')
    if build['mathematical_executable_invoked'] or build['shared_library_loaded']:
        raise ValueError('No mathematical execution is part of this entry')
    if plan['files']['build_record']!=ident(a.build):raise ValueError('Plan/build identity mismatch')
    for ref in plan['files'].values():
        if sha(ref['path'])!=ref['sha256']:raise ValueError('Frozen plan reference changed')
    for name,ref in build['sources'].items():
        if ref!=plan['files'][name] or Path(ref['path']).stat().st_size>=100000:
            raise ValueError('Source identity/size mismatch')
    for run in build['compile_results'].values():
        if run['returncode']!=0:raise ValueError('Compiler did not finish successfully')
        for key in ('stdout','stderr'):
            if sha(run[key]['path'])!=run[key]['sha256']:raise ValueError('Compiler output identity changed')
    for key in ('library','batch_executable'):
        if build[key]!=plan['files'][key]:raise ValueError('Compiled artifact identity differs')
    command=plan['command']
    if command[command.index('--mode')+1]!='float-baseline':raise ValueError('Entry must plan only the double baseline')
    if plan['expected_output_count']!=126 or plan['expected_event_count']!=116608:
        raise ValueError('The exact validation scope changed')
    cs=checked(plan['files']['capsule_summary'])
    capsule,reference=checked(cs['coefficients']),checked(cs['reference'])
    stages={}
    for fixture,row in zip(capsule['fixtures'],reference['rows'],strict=True):
        if fixture['stage']!=row['stage']:raise ValueError('Original reference stage mismatch')
        stages[str(fixture['stage'])]=dict(stage=fixture['stage'],initial42_sha256=packed_hash(fixture['initial42']),
            original_output42_sha256=packed_hash(row['state']),original_trace_events=len(row['events']))
    if sum(v['original_trace_events']for v in stages.values())!=116608:
        raise ValueError('Original trace reference count differs')
    source_map={}
    for key in ('source_sha256','additional_original_root_sources'):
        for path,digest in cs[key].items():
            if sha(path)!=digest:raise ValueError('A bound original mathematical source changed')
            source_map[path]=digest
    output=dict(scope=__doc__,collector=ident(__file__),helper=ident(Path(__file__).with_name('record_fixed_actual.py')),
        build_record=ident(a.build),frozen_execution_plan=ident(a.plan),sources=build['sources'],
        source_sizes_bytes={name:Path(ref['path']).stat().st_size for name,ref in build['sources'].items()},
        compiler=build['compiler'],compiler_version=build['compiler_version'],flags=build['flags'],
        actual_compile_results=build['compile_results'],compiled_library=build['library'],compiled_batch_cli=build['batch_executable'],
        proposed_double_command=plan['command'],proposed_observer_command=plan['observer_command'],
        original_entry_files={key:ref for key,ref in plan['files'].items()if key not in build['sources'] and key not in ('library','batch_executable','build_record')},
        original_capsule_coefficients=cs['coefficients'],original_capsule_reference=cs['reference'],
        original_source_sha256=source_map,planned_reference_stages=stages,
        planned_exact_output_count=126,planned_exact_event_count=116608,
        compiler_warning_scope=plan['compile_warning'],
        source_scope='Original formed-moment root and ordinary RK; no shifted-root or compensated-state rewrite. Literal implicit Jacobian source derives B_exact separately and checks its own positive finite pivots. It is evaluated at approximate roots and is not AD of Newton stopping branches.',
        double_validation_scope='Existing V8 root_rows/sqrt callbacks; exact original126 output bytes and116608 recorded events are required. No tolerance waiver. This entry records their planned scope only.',
        binary_protocol_scope='Self-contained whole-evaluate payload and same-kernel CLI source. Token binds payload only; source/build identity is checked separately by the outer manifest. No native batch has been run or connected to Node.',
        outstanding=dict(native_double_exact_baseline=True,longdouble_state_only_vs_fullJac_identity=True,
            native_longdouble_flow_accuracy=True,native_full40Jacobian_independent_MP_reference=True,
            native_runtime_math_library_identity=True,actual_native_performance=True,
            whole_2304_batch_and_original_boundary_norm=True,original_DN_and_final_audit=True),
        shared_library_loaded=False,new_flow_executed=False,new_Jacobian_executed=False,
        production_installed=False,new_tail_accepted=False,
        data_policy='Publish sources, compiler commands, identities and planned validation scalars only; compiled binaries and full mathematical capsules remain scratch-only.')
    encoded=json.dumps(output,ensure_ascii=False,indent=2)+'\n'
    if len(encoded.encode())>=100000:raise ValueError('Entry must remain compact')
    a.out.write_text(encoded)
    print(json.dumps(dict(bytes=a.out.stat().st_size,sha256=sha(a.out))))


if __name__=='__main__':main()
