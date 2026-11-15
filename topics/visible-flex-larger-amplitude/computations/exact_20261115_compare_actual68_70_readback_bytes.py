#!/usr/bin/env python3
"""Compare completed actual68/70 byte receipts and unchanged original reports.

Pure standard-library metadata/byte reader.  It compares the complete saved
array SHA records already verified by the two public Actions readers.  It does
not independently download or re-read the original large scientific payloads,
and does not import scientific code or compute norms, actions, ratios or models.
Cross-run differences are observations, never a scientific acceptance gate.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import traceback

PARENT_WARM = '80b4590f476cf782d63cbc1680a4c205713bf6a533e544472219b6fef85a3cf6'
PARENT_STATUS = '04ace7953961b3905d2b72639976025dc9c4efd0bef7b932585cf21f8249bcd4'
DOMAIN_SOURCE = '0007a3dd345cb60172c75ef6490fa3f0bbcfdc178be90e532120302fc6c15a65'
BASE_AUDIT_SHA = '2e5b678efa113789649c15b893e07d93fdd94fef4ab44086e308a1d11e0e8abb'
BASE_SOURCE = 'b7956525ce484c4ed17724c2d84c04b6080688e2d0afc8367c5ba46cbf8626f2'
CHANGED_SOURCE = 'a8dd293b4b10ab45a2e69dd1e3e37a2032e4af3eb4d5f21eefa556277cb0d64c'
BASE_READER = '0feeb16e350d06ed03abb93c8ff80dd6e9e10a2703d47135f3c36ee3c289ea3a'
BASE_SCHEMA = 'exact-constraint-twenty-one-query-condensed-complete-H-warm-v1'
CHANGED_SCHEMA = 'exact-constraint-twenty-one-query-lambda27-condensed-complete-H-warm-v1'
BASE_AUDIT_SCHEMA = 'completed-twenty-one-prefix-artifact-readback-and-byte-audit-v1'
CHANGED_AUDIT_SCHEMA = 'completed-twenty-one-lambda27-prefix-artifact-readback-and-byte-audit-v1'
BASE_RUN = 43653811809
CHANGED_RUN = 43656059206
INPUT_NAMES = ('L','R','P','BY','BC','BP','inlet','S','Wr')
ARRAY_KEYS = ('shape','dtype','bytes','sha256','raw_sha256')


def require(value, label):
    if not value:
        raise ValueError(label)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def read_path(root, relative):
    require(isinstance(relative,str) and '\\' not in relative, 'Relative POSIX path required')
    part=PurePosixPath(relative)
    require(not part.is_absolute() and part.parts and
        all(item not in ('','.','..') for item in part.parts), 'No escaping receipt path')
    root=Path(root).resolve(); path=(root/relative).resolve()
    require(path.is_relative_to(root) and path.is_file(), 'Missing bound file: '+relative)
    raw=path.read_bytes()
    data=json.loads(gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw)
    return data,dict(file=relative,bytes=len(raw),sha256=digest(raw))


def checked(root, description, name_key='file'):
    data,record=read_path(root,description[name_key])
    require(record['bytes']==description['bytes'] and record['sha256']==description['sha256'],
        'Receipt byte identity differs: '+description[name_key])
    return data,record


def unique(rows, key, label):
    out={}
    for row in rows:
        name=row[key]
        require(name not in out,'Duplicate '+label+': '+str(name))
        out[name]=row
    return out


def array_identity(item):
    require(all(key in item for key in ARRAY_KEYS), 'Complete verified array identity required')
    for key in ('sha256','raw_sha256'):
        require(isinstance(item[key],str) and re.fullmatch(r'[0-9a-f]{64}',item[key]),
            'An actual complete array SHA256 is required')
    return {key:item[key] for key in ARRAY_KEYS}


def read_model(directory, changed):
    reader,reader_file=read_path(directory,'completed-prefix-readback.json')
    expected_schema=CHANGED_AUDIT_SCHEMA if changed else BASE_AUDIT_SCHEMA
    require(reader['schema']==expected_schema and reader['completed'] is True
        and reader['byte_audit_completed'] is True,'Use the completed matching public Actions reader')
    require(reader['mathematical_computation_performed'] is False,'This is a byte-only completed reader')
    require(reader['original_artifact_pin']['run_id']==(CHANGED_RUN if changed else BASE_RUN),
        'Read the actual requested numerical run')
    require(reader['requested_parent_warm_sha256']==PARENT_WARM and
        reader['requested_parent_status_sha256']==PARENT_STATUS,'Both runs start from actual66')
    require(reader['parent_warm']['sha256']==PARENT_WARM and
        reader['original_parent_status_decoded_sha256']==PARENT_STATUS,'Actual restored parent receipts agree')
    if not changed:
        require(reader['source_sha256']==BASE_READER,'Known completed baseline reader source')
    audit,audit_file=checked(directory,reader['complete_byte_audit_artifact'])
    require(audit['schema']==expected_schema,'Complete receipt schema')
    require(audit['original_artifact_pin']==reader['original_artifact_pin'] and
        audit['original_source_commit']==reader['original_source_commit'],'Whole audit binds the same original run')
    require(audit['no_scientific_module_imported'] is True,'Original reader scope')
    if not changed:
        require(audit_file['sha256']==BASE_AUDIT_SHA,'Use the actually completed baseline full receipt')
    reports=unique(reader['unchanged_original_reports_in_readback_artifact'],'original_file','original report')
    warm='twenty-one-lambda27-condensed-warm' if changed else 'twenty-one-condensed-warm'
    qp,qp_file=checked(directory,reports[warm+'/condensed-QP-summary.json'],'artifact_file')
    model,model_file=checked(directory,reports[warm+'/model-000.json'],'artifact_file')
    status,status_file=checked(directory,reports[warm+'/driver-status.json'],'artifact_file')
    entry=qp['condensed_QP_entry']
    require(entry['schema']==(CHANGED_SCHEMA if changed else BASE_SCHEMA),'Original producer schema')
    require(entry['entry_source_sha256']==(CHANGED_SOURCE if changed else BASE_SOURCE),
        'Original mathematical producer bytes')
    require(entry['actual_parent_warm_sha256']==PARENT_WARM and
        entry['actual_parent_status_sha256']==PARENT_STATUS,'Unchanged true parent of the original model')
    require(entry['twenty_one_query_operator_source_sha256']==DOMAIN_SOURCE,
        'Both models use the same frozen twenty-one query mathematics')
    require(status['schema']==entry['schema'],'Complete original status belongs to this producer')
    require(qp['condensation_report']['damping']==(27.0 if changed else 270.0),
        'Read each actual requested damping, do not relabel a model')
    full_inputs=qp['condensation_report']['original_factor_input_arrays']
    require(set(full_inputs)==set(INPUT_NAMES),'All complete chain input identities retained')
    require(qp['condensation_report']['last_recovery']['factor_solve_report']['input_arrays']==full_inputs,
        'The original recovery binds its own complete factor model')
    sources=unique(audit['source_files'],'source','source receipt')
    domain_source=sources['geometry_20261114_twenty_one_query_domain_operator.py']
    require(domain_source['sha256']==DOMAIN_SOURCE and domain_source['verified'] is True,
        'Completed byte reader actually checked the shared domain source')
    B_files=unique(audit['domain']['files'],'file','B payload')
    require(len(B_files)==audit['domain']['file_count'],'Complete B file count')
    complete_arrays=unique(audit['condensed']['complete_array_byte_combinations'],'label','condensed full array')
    original_arrays={name:array_identity(complete_arrays[name])
        for name in ('original_b','original_g','original_c')}
    return dict(reader_file=reader_file,audit_file=audit_file,original_QP_summary_file=qp_file,
        original_model_file=model_file,original_status_file=status_file,
        run=reader['original_artifact_pin'],source_commit=reader['original_source_commit'],
        reader_source_sha256=reader['source_sha256'],parent_warm_sha256=PARENT_WARM,
        parent_status_sha256=PARENT_STATUS,entry=entry,
        damping=qp['condensation_report']['damping'],
        B_model_sha256=audit['domain']['model_sha256'],B_files=B_files,
        B_groups=unique(audit['domain']['complete_group_byte_combinations'],'label','complete B group'),
        original_arrays=original_arrays,full_A_input_identities=full_inputs,
        root_arrays=unique(audit['root_raw']['files'],'name','condensed root raw array'),
        raw_complete_QR_payloads_independently_verified=False,
        original_QR_factor_payloads_not_exported=reader['full_factor_array_files_not_exported_by_original_producer'],
        copied_original_scalars=dict(status=reader['original_status'],
            model=reader['original_model_scalars'],accepted_trial=reader['accepted_trial'],
            nearest_rejected_trial=reader['nearest_previous_rejected_trial'],
            QP_comparison=reader['original_QP_comparison_scalars'],
            QP_last_unrepaired=reader['original_QP_last_unrepaired'],
            QP_local_radial=reader['original_QP_local_radial'],
            QP_global_radial=reader['original_QP_global_radial'],
            FD=reader['original_FD_summary']))


def compare_arrays(base, changed):
    rows=[]
    for name in sorted(set(base)|set(changed)):
        left=base.get(name);right=changed.get(name)
        both=left is not None and right is not None
        a=array_identity(left) if left is not None else None
        b=array_identity(right) if right is not None else None
        rows.append(dict(name=name,present_in_both=both,baseline=a,changed=b,
            same_verified_complete_raw_SHA=bool(both and a==b)))
    return rows


def comparison(base, changed):
    files=[];arrays=[]
    for name in sorted(set(base['B_files'])|set(changed['B_files'])):
        a=base['B_files'].get(name);b=changed['B_files'].get(name)
        both=a is not None and b is not None
        rows=compare_arrays(a['arrays'] if a else {},b['arrays'] if b else {})
        for row in rows:
            arrays.append(dict(file=name,**row))
        files.append(dict(file=name,present_in_both=both,
            compressed_file_bytes_and_SHA_equal=bool(both and a['bytes']==b['bytes'] and a['sha256']==b['sha256']),
            all_verified_NPY_array_identities_equal=bool(both and all(r['same_verified_complete_raw_SHA'] for r in rows))))
    inputs={name:dict(baseline=base['full_A_input_identities'][name],changed=changed['full_A_input_identities'][name],
        equal=base['full_A_input_identities'][name]==changed['full_A_input_identities'][name]) for name in INPUT_NAMES}
    roots=[]
    for name in sorted(set(base['root_arrays'])|set(changed['root_arrays'])):
        a=base['root_arrays'].get(name);b=changed['root_arrays'].get(name)
        both=a is not None and b is not None
        # These raw files use a byte SHA, rather than the shape-prefixed NPY SHA.
        keys=('shape','dtype','bytes','raw_sha256')
        roots.append(dict(name=name,present_in_both=both,
            baseline={k:a[k] for k in keys} if a else None,
            changed={k:b[k] for k in keys} if b else None,
            same_complete_raw_SHA=bool(both and all(a[k]==b[k] for k in keys))))
    return dict(B_file_count=len(files),B_array_count=len(arrays),B_files=files,B_arrays=arrays,
        all_verified_B_arrays_equal=all(row['same_verified_complete_raw_SHA'] for row in arrays),
        all_B_file_sets_and_payloads_equal=all(row['all_verified_NPY_array_identities_equal'] for row in files),
        complete_B_groups=compare_arrays(base['B_groups'],changed['B_groups']),
        original_b_g_c=compare_arrays(base['original_arrays'],changed['original_arrays']),
        full_A_input_identity_records=inputs,
        full_A_input_records_all_equal=all(value['equal'] for value in inputs.values()),
        full_A_payloads_not_exported_or_recomputed_here=True,
        full_A_equality_scope='The original Actions raw-SHA records for all L/R/P/BY/BC/BP/inlet/S/Wr inputs; no independent local full-chain A payload audit',
        B_query_specs_equal=base['entry']['query_specs']==changed['entry']['query_specs'],
        B_metadata_SHA=dict(baseline=base['B_model_sha256'],changed=changed['B_model_sha256'],
            equal=base['B_model_sha256']==changed['B_model_sha256'],
            metadata_difference_alone_is_not_a_scientific_array_difference=True),
        complete_condensed_root_raw_files=roots,
        roots_and_column_preconditioner_expected_to_be_rebuilt_for_actual_damping=True,
        cross_run_equality_is_not_a_scientific_acceptance_gate=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--baseline-readback',type=Path,required=True)
    p.add_argument('--changed-readback',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    require(not args.out.exists(),'Use a fresh byte-comparison output directory')
    args.out.mkdir(parents=True)
    summary=dict(schema='actual68-70-same-parent-completed-byte-receipt-comparison-v1',
        scientific_arrays_recomputed=False,scientific_modules_imported=False,
        norms_actions_ratios_or_optimizations_computed=False,
        complete_large_payloads_verified_by_original_Actions_readers=True,
        those_payloads_not_reaudited_locally_by_this_tool=True,
        cross_run_difference_is_not_an_acceptance_gate=True)
    code=0
    try:
        base=read_model(args.baseline_readback,False)
        changed=read_model(args.changed_readback,True)
        compared=comparison(base,changed)
        detail=dict(baseline=base,changed=changed,comparison=compared)
        raw=(json.dumps(detail,separators=(',',':'),allow_nan=False)+'\n').encode()
        packed=gzip.compress(raw,mtime=0)
        (args.out/'complete-byte-comparison.json.gz').write_bytes(packed)
        summary.update(completed=True,detail=dict(file='complete-byte-comparison.json.gz',
            bytes=len(packed),sha256=digest(packed)),
            B_file_count=compared['B_file_count'],B_array_count=compared['B_array_count'],
            all_verified_B_arrays_equal=compared['all_verified_B_arrays_equal'],
            all_B_file_sets_and_payloads_equal=compared['all_B_file_sets_and_payloads_equal'],
            original_b_g_c_equal=all(row['same_verified_complete_raw_SHA'] for row in compared['original_b_g_c']),
            full_A_input_records_all_equal=compared['full_A_input_records_all_equal'],
            full_A_payload_equality_scope=compared['full_A_equality_scope'],
            B_query_specs_equal=compared['B_query_specs_equal'],
            B_metadata_SHA=compared['B_metadata_SHA'],
            original_runs=dict(baseline=base['run'],changed=changed['run']),
            original_dampings=dict(baseline=base['damping'],changed=changed['damping']))
    except Exception as error:
        summary.update(completed=False,exception=repr(error),traceback=traceback.format_exc())
        code=1
    source=Path(__file__).read_bytes()
    summary['comparison_source']=dict(file=Path(__file__).name,bytes=len(source),sha256=digest(source))
    (args.out/'summary.json').write_text(json.dumps(summary,indent=2,allow_nan=False)+'\n')
    print(json.dumps(summary,allow_nan=False))
    return code


if __name__=='__main__':
    raise SystemExit(main())
