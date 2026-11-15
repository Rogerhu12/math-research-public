#!/usr/bin/env python3
"""Read actual94's five published originals; stdlib bytes/JSON/source only.

No mathematical source is imported.  Do not run this draft against another
run renamed as actual94.  The actual future artifact tuple must be supplied
by the caller after the official artifact exists.  Original scalar results
are copied, never recomputed or selected by a new scientific threshold.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import traceback

RUN=43674854261
SOURCE_COMMIT='b75f41fa32b8ead9bb5121b725a0afe1a2f5ae5c'
JOB=132692676503
WARM_DIR='twenty-eight-condensed-warm'
PARENT_DIR='twenty-six-condensed-warm'
PARENT_WARM_SHA='8985f7a5f146f0e98af04d5b1fc3d86648c7e6007403d9be54b1ed8ca4143fc9'
PARENT_STATUS_SHA='c78528682d239d941ccc1391df004c8da3b51d60b6315c6d30334828d0204540'
SCHEMA='exact-constraint-twenty-eight-query-condensed-complete-H-warm-v1'
ENTRY_KEY='twenty_eight_query_projection_entry'
ENTRY_PINS={
    'geometry_20261114_twenty_eight_query_domain_operator.py':'25767045b9a26764bfdb89881832ec7da01de1ac86ebc491402c7b9801175cd0',
    'geometry_20261114_twenty_eight_query_condensed_warm.py':'990029102808ede1134bd9e6a163b6da84ae0d9189857f49af216ba64bfa188c',
    'geometry_20261114_twenty_eight_query_condensed_response.py':'3a3d5f2888b4d826c69e2949ae9ec5ef896c54cb04f9b2283a71051221d7c5d9',
    'geometry_20261114_twenty_eight_query_collocation_observer_warm.py':'fc5a3e4b35557a7056d96cd7ade6756b861f3667e44aea83d51e4f5cd59c7dfc',
}
LEFT=(465,466,467,468,469,470,471,472,473,475,477,479,480,481,482,484,485,487)
MID=(473,475,477,479,480,481,482,484,485,487)
EXPECTED_QUERY_SPECS=tuple(dict(kind='left-RMS',interval=j,fraction=0.17267316464601146) for j in LEFT)+tuple(
    dict(kind='collocation-midpoint',interval=j,fraction=.5) for j in MID)
EXPECTED_B_NODES=tuple(range(465,489))
EXPECTED_C_NODES=tuple(range(471,483))
EXPECTED_OUTSIDE_C_NODES=(465,466,467,468,469,470,483,484,485,486,487,488)
OMIT={'source_entry','resume_producer',ENTRY_KEY,'condensed_QP_entry',
      'read_only_collocation_observer_entry','original_source_and_parent_entry'}

def digest(raw):return hashlib.sha256(raw).hexdigest()

def read(path):
    raw=Path(path).read_bytes()
    decoded=gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw
    return json.loads(decoded),raw,decoded

def subset(a,b):return isinstance(a,dict) and isinstance(b,dict) and all(k in b and v==b[k] for k,v in a.items())

def safe_path(root,relative):
    part=PurePosixPath(relative)
    if part.is_absolute() or '..' in part.parts or not part.parts:
        raise ValueError('Use a safe original relative file path')
    path=root/str(part)
    if not path.is_file() or path.is_symlink() or not path.resolve().is_relative_to(root.resolve()):
        raise ValueError('Original regular file missing or outside its root: '+relative)
    return path

def original_json_path(directory,stem):
    choices=[p for p in (directory/stem,directory/(stem+'.gz')) if p.is_file()]
    if not choices:raise ValueError('Missing original JSON/transparent gzip: '+str(directory/stem))
    if len(choices)==2 and read(choices[0])[2]!=read(choices[1])[2]:
        raise ValueError('Two original aliases contain different decoded bytes')
    return choices[0]

def write(path,value,compressed=False):
    raw=(json.dumps(value,ensure_ascii=False,sort_keys=True,indent=2,allow_nan=False)+'\n').encode()
    data=gzip.compress(raw,mtime=0) if compressed else raw
    path.write_bytes(data)
    return dict(file=path.name,bytes=len(data),sha256=digest(data))

def prune(value):
    if isinstance(value,dict):return {k:prune(v) for k,v in value.items() if k not in OMIT}
    if isinstance(value,list):return [prune(v) for v in value]
    return value

def scalars(value):
    return {k:v for k,v in value.items() if v is None or isinstance(v,(bool,int,float,str))} if isinstance(value,dict) else {}

def selected_original_trial(row,index):
    result=dict(index=index,original_scalars=scalars(row),
        actual_merit_present='actual_fixed_weight_merit' in row,
        complete_original_RMS_report_present='complete_original_RMS_query_domain' in row,
        independent_actual_directional_check_present='independent_actual_directional_check' in row,
        missing_fields_not_invented=True,rejection_cause_not_inferred_from_missing_fields=True)
    structured_keys=('selected_linear_beta_squared','all_selected_linear_reserve_slack','domain',
        'actual_selected_original_angles','selected_angle_values','complete_original_RMS_query_domain',
        'independent_actual_directional_check')
    for key in structured_keys:
        if key in row:result[key]=prune(row[key])
    result['other_original_structured_fields']={k:prune(v) for k,v in row.items()
        if k not in structured_keys and isinstance(v,(list,dict))}
    actual_angles=row.get('actual_selected_original_angles')
    result['original_selected_query487_reports']=[prune(v) for v in actual_angles
        if isinstance(v,dict) and v.get('interval')==487] if isinstance(actual_angles,list) else None
    result['original_trial_field_names']=list(row)
    return result

def extract_support(model,qp):
    """Copy existing fields; equality checks here compare declared metadata only."""
    b=model.get('full_angle_operator',{})
    projection=model.get('local_projection',{})
    entry=model.get('condensed_QP_entry',{})
    actual=entry.get('actual_current_B_C_layout')
    qentry=qp.get('original_source_and_parent_entry',{})
    qactual=qentry.get('actual_current_B_C_layout')
    condensation=qp.get('condensation_report')
    local=qp.get('local_QP_report')
    checks={
        'complete_B_shape_and_local_shape_match_configuration':b.get('shape')==[57344,236036] and b.get('local_shape')==[57344,8115],
        'complete_B_actual_endpoints_are_465_through488':b.get('actual_query_endpoint_nodes')==list(EXPECTED_B_NODES),
        'declared_B_layout_matches_same_endpoints':b.get('declared_contiguous_local_nodes')==list(EXPECTED_B_NODES),
        'declared_and_saved_B_union_dimensions_8115':b.get('declared_contiguous_local_dimension')==8115 and b.get('actual_block_column_union_dimension')==8115,
        'zero_layout_nodes_empty':b.get('zero_layout_nodes')==[],
        'original_C_return_declares_full_B8115_C4059_rows57344':projection.get('full_compiled_B_local_dimension')==8115 and projection.get('local_dimension')==4059 and projection.get('constraint_rows')==57344,
        'original_C_return_nodes471_through482':projection.get('correction_physical_nodes')==list(EXPECTED_C_NODES),
        'new_query_specs_in_original_B_description':b.get('query_specs')==list(EXPECTED_QUERY_SPECS),
        'complete_B_outside_C_nodes_includes487_and488':entry.get('complete_B_outside_C_nodes')==list(EXPECTED_OUTSIDE_C_NODES),
        'new_runtime_layout_object_present':isinstance(actual,dict),
        'runtime_layout_copy_in_model_and_QP_summary_equal':actual==qactual and isinstance(actual,dict),
    }
    if isinstance(actual,dict):
        checks.update(runtime_dimensions_equal_the_original_C_return=(
            actual.get('full_B_local_dimension')==projection.get('full_compiled_B_local_dimension')
            and actual.get('C_projection_dimension')==projection.get('local_dimension')
            and actual.get('constraint_rows')==projection.get('constraint_rows')),
            runtime_C_support_is_original_return_copy=actual.get('original_C_support')==projection.get('correction_support'),
            runtime_C_nodes_are_original_return_copy=actual.get('original_C_physical_nodes')==projection.get('correction_physical_nodes'),
            runtime_B_nodes_are_original_capture_nodes=actual.get('actual_query_endpoint_nodes')==b.get('actual_query_endpoint_nodes'),
            runtime_layout_declares_no_added_evaluation=actual.get('additional_projection_or_operator_calls')==0,
            runtime_layout_declares_actual_original_projection=actual.get('dimensions_read_from_the_current_original_projection') is True)
    optional_checks={}
    if isinstance(condensation,dict):
        optional_checks['H_condensation_saved_layout']=dict(
            local_dimension=condensation.get('local_dimension'),
            retained_physical_nodes=condensation.get('retained_physical_nodes'),
            first_retained_physical_node=condensation.get('first_retained_physical_node'),
            last_retained_physical_node=condensation.get('last_retained_physical_node'),
            original_local_indices=condensation.get('original_local_indices'),
            matches_B8115_and_all24_nodes=(condensation.get('local_dimension')==8115
                and condensation.get('retained_physical_nodes')==24
                and condensation.get('first_retained_physical_node')==465
                and condensation.get('last_retained_physical_node')==488),
            retained_physical_nodes_is_original_count_not_index_list=True,
            schema=condensation.get('schema'),model_identity_sha256=condensation.get('model_identity_sha256'),
            complete=condensation.get('complete'),status=condensation.get('status'))
    if isinstance(local,dict):
        optional_checks['local_QP_saved_layout']=dict(
            local_coordinate_count=local.get('local_coordinate_count'),
            original_inequality_row_count=local.get('original_inequality_row_count'),
            original_full_coordinate_count=local.get('original_full_coordinate_count'),
            local_indices=local.get('local_indices'),
            matches_B8115_rows57344_full236036=(local.get('local_coordinate_count')==8115
                and local.get('original_inequality_row_count')==57344
                and local.get('original_full_coordinate_count')==236036))
    return dict(scope='Existing original JSON descriptors and scalar/layout values only; no array payload or model action audit',
        configured_layout=dict(full_coordinates=236036,B_rows=57344,B_H_local_coordinates=8115,
            B_endpoint_nodes=list(EXPECTED_B_NODES),C_projection_coordinates=4059,
            C_physical_nodes=list(EXPECTED_C_NODES),B_outside_C_nodes=list(EXPECTED_OUTSIDE_C_NODES),
            added_nodes=[487,488],added_node487_global_columns_half_open=[164268,164606],
            added_node488_global_columns_half_open=[164606,164944],global_p_columns_half_open=[236033,236036]),
        observed_original_B_description=prune(b),
        observed_original_C_projection_report=prune(projection),
        observed_actual_current_B_C_layout=actual,
        observed_complete_QP_entry=entry,
        observed_complete_QP_summary_entry=qentry,
        original_condensation_report=prune(condensation),original_local_QP_report=prune(local),
        original_optional_helper_failure=prune(qp.get('comparison',{}).get('optional_optimization_failure')),
        metadata_matches=checks,optional_existing_H_QP_metadata=optional_checks,
        helper_completion_or_small_posterior_not_required=True,
        actual_array_payload_read_or_verified=False)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('published-directory','parent-directory','source-directory','out'):
        parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--artifact-id',type=int,required=True)
    parser.add_argument('--artifact-bytes',type=int,required=True)
    parser.add_argument('--artifact-sha256',required=True)
    args=parser.parse_args()
    if args.artifact_id<=0 or args.artifact_bytes<=0 or re.fullmatch('[0-9a-f]{64}',args.artifact_sha256) is None:
        raise ValueError('Supply the real official actual94 artifact tuple after it exists')
    root,parent,src,out=args.published_directory,args.parent_directory,args.source_directory,args.out
    if out.resolve() in (root.resolve(),parent.resolve(),src.resolve()):
        raise ValueError('Use a separate readback output directory')
    out.mkdir(parents=True,exist_ok=False)
    result=dict(schema='actual94-published-primary-readback-execution-v1',completed=False,
        source_reader_sha256=digest(Path(__file__).read_bytes()),run_id=RUN,source_commit=SOURCE_COMMIT,job_id=JOB,
        mathematical_computation_performed=False,full_array_payload_audit_performed=False)
    try:
        receipt,receipt_raw,_=read(root/'published-original-fetch.json')
        if receipt['science_run']!=RUN or receipt['science_source']!=SOURCE_COMMIT:
            raise ValueError('Only the genuine actual94 published-original receipt is accepted')
        docs={};originals={};files=[]
        for desc in receipt['files']:
            path=safe_path(root,desc['file']);obj,raw,decoded=read(path)
            if len(raw)!=desc['bytes'] or digest(raw)!=desc['sha256']:
                raise ValueError('Original published file identity mismatch: '+desc['file'])
            if 'original_sha256' in desc:
                if len(decoded)!=desc['original_bytes'] or digest(decoded)!=desc['original_sha256']:
                    raise ValueError('Transparent decoded-original identity mismatch: '+desc['file'])
                original_name=desc['original_file']
                files.append(dict(file=original_name,bytes=len(decoded),sha256=digest(decoded),
                    scope='Exact original bytes recovered from transparent gzip; not reserialized'))
            else:original_name=desc['file']
            files.append(dict(file=desc['file'],bytes=len(raw),sha256=digest(raw)))
            if original_name in originals and originals[original_name]['decoded']!=decoded:
                raise ValueError('Conflicting published aliases for the same original')
            originals[original_name]=dict(obj=obj,raw=raw,decoded=decoded,descriptor=desc)
            docs[desc['file']]=obj
        files.append(dict(file='published-original-fetch.json',bytes=len(receipt_raw),sha256=digest(receipt_raw)))
        def role(stem):
            for key in (stem,stem+'.gz'):
                if key in originals:return originals[key]
            raise ValueError('Required genuine original missing: '+stem)
        sr=role(WARM_DIR+'/driver-status.json');mr=role(WARM_DIR+'/model-000.json')
        qr=role(WARM_DIR+'/condensed-QP-summary.json');wr=role(WARM_DIR+'/warm-001.json.gz')
        fr=role('physical-response/response-check.json')
        s,m,q,w,f=[r['obj'] for r in (sr,mr,qr,wr,fr)]
        warm_sha=digest(wr['raw'])
        # Save the complete current values before cross-file/source checks.
        # A failed identity readback must not erase observed original output.
        provisional=dict(schema='actual94-original-literal-provisional-readout-v1',run_id=RUN,
            status=prune({k:v for k,v in s.items() if k not in ('identity','iterations')}),
            original_model=prune(m),original_QP_summary=prune(q),
            FD={k:v for k,v in f.items() if k!='optimization_warm'},
            identity_checks_not_yet_completed=True,mathematical_computation_performed=False)
        result['literal_original_readout']=write(out/'2026-11-15-actual94-original-readout.json.gz',provisional,True)
        pw,pwb,_=read(parent/PARENT_DIR/'warm-001.json.gz')
        ps_path=original_json_path(parent/PARENT_DIR,'driver-status.json');ps,psb,psraw=read(ps_path)
        ph,psh=digest(pwb),digest(psraw)
        files.extend([dict(file='actual89/warm-001.json.gz',bytes=len(pwb),sha256=ph),
            dict(file='actual89/original-decoded-driver-status.json',bytes=len(psraw),sha256=psh)])
        entries=[s[ENTRY_KEY],m[ENTRY_KEY],w[ENTRY_KEY]]
        trials=m.get('trials',[])
        accepted_indices=[i for i,t in enumerate(trials) if t.get('accepted') is True]
        accepted=[trials[i] for i in accepted_indices]
        accepted_binding=(len(accepted)==1 and accepted_indices[-1]==len(trials)-1
            and s.get('accepted_warm_steps')==1
            and accepted[0].get('actual_fixed_weight_merit')==w['optimization_warm'].get('actual_fixed_weight_merit')) if accepted else s.get('accepted_warm_steps')==0
        checks={
            'original_parent_warm_sha256':ph==PARENT_WARM_SHA and s['identity'].get('resume_sha256')==ph and all(e.get('actual_resume_sha256')==ph for e in entries),
            'original_parent_status_sha256':psh==PARENT_STATUS_SHA and all(e.get('actual_parent_status_sha256')==psh for e in entries),
            'parent_status_identity_is_parent_producer_subset':subset(ps.get('identity'),pw.get('optimization_warm')),
            'parent_status_binds_parent_warm':ps.get('latest_warm_sha256')==ph,
            'complete_parent_producer_retained':w['optimization_warm'].get('resume_producer')==pw.get('optimization_warm'),
            'actual_new_warm_bytes_match_status':s.get('latest_warm_sha256')==warm_sha,
            'status_identity_is_new_producer_subset':subset(s.get('identity'),w.get('optimization_warm')),
            'status_iteration_is_original_model_subset':len(s.get('iterations',[]))==1 and subset(s['iterations'][0],m),
            'FD_binds_actual_new_warm':f.get('prepared_sha256')==warm_sha,
            'FD_whole_producer_matches_new_warm':f.get('optimization_warm')==w.get('optimization_warm'),
            'mesh_preserved':w.get('mesh')==pw.get('mesh'),
            'status_original_decoded_bytes_bound':digest(sr['decoded'])==sr['descriptor'].get('original_sha256',sr['descriptor']['sha256']),
            'FD_original_decoded_bytes_bound':digest(fr['decoded'])==fr['descriptor'].get('original_sha256',fr['descriptor']['sha256']),
            'current_schema_binds_all_reports':s.get('schema')==w['optimization_warm'].get('schema')==f['optimization_warm'].get('schema')==SCHEMA and all(e.get('optimizer_schema')==SCHEMA for e in entries),
            'original_scientific_flag_fields_retained_as_booleans':all(type(v) is bool for v in (s.get('success'),s.get('new_coupled_finite_acceptance'),w.get('success'),w.get('new_coupled_finite_acceptance'),f.get('full_BVP_solved'),f.get('nonlinear_native_at_current_H_solved'))),
            'accepted_original_trial_and_saved_warm_relation':accepted_binding,
            'published_original_fetch_manifest_matches_actual_files':True,
        }
        if len(checks)!=17:raise ValueError('Keep all seventeen current/parent report relations explicit')
        source_ledgers=[s['identity']['source_sha256'],f['consumed_source_sha256']]
        claimed={}
        for ledger in source_ledgers:
            for name,expected in ledger.items():
                if name in claimed and claimed[name]!=expected:raise ValueError('Conflicting original source SHA: '+name)
                claimed[name]=expected
        verified=[]
        for name,expected in sorted(claimed.items()):
            if Path(name).name!=name or re.fullmatch('[0-9a-f]{64}',expected) is None:raise ValueError('Unsafe original source identity')
            path=safe_path(src,name);raw=path.read_bytes()
            if digest(raw)!=expected:raise ValueError('Original consumed source changed: '+name)
            verified.append(dict(name=name,bytes=len(raw),sha256=expected,local_file=str(path)))
        required_entries=[]
        for name,expected in ENTRY_PINS.items():
            raw=safe_path(src,name).read_bytes()
            if digest(raw)!=expected:raise ValueError('Frozen actual28 entry changed: '+name)
            required_entries.append(dict(name=name,bytes=len(raw),sha256=expected))
        wrapper='geometry_20261114_twenty_eight_query_collocation_observer_warm.py'
        wrapper_sha=ENTRY_PINS[wrapper]
        wrapper_bound=all(doc.get('execution_wrapper_source_sha256')==wrapper_sha for doc in (s,m,w))
        data_shape=(len(w['mesh'])==len(w['states'])==len(w['rhs'])==699
            and all(len(row)==453 for row in w['states']+w['rhs']))
        query_checks=dict(
            model_query_order_matches_frozen28=m.get('query_specs')==list(EXPECTED_QUERY_SPECS),
            status_query_order_matches_frozen28=s.get('query_specs')==list(EXPECTED_QUERY_SPECS),
            warm_query_order_matches_frozen28=w.get('query_specs')==list(EXPECTED_QUERY_SPECS),
            original_selected_row_count_is57344=s.get('selected_angle_row_count')==57344,
            current_state_dimensions_699_by453=data_shape,original_observer_wrapper_bound=wrapper_bound)
        support=extract_support(m,q)
        chain=[];current=w['optimization_warm']
        while isinstance(current,dict):
            chain.append(dict(schema=current.get('schema'),resume_sha256=current.get('resume_sha256'),source_count=len(current.get('source_sha256',{}))))
            current=current.get('resume_producer')
        original_flags={
            'status':{k:s.get(k) for k in ('success','new_coupled_finite_acceptance','optimization_progress','accepted_warm_steps')},
            'warm':{k:w.get(k) for k in ('success','new_coupled_finite_acceptance','complete_closed_surface')},
            'FD':{k:f.get(k) for k in ('full_BVP_solved','nonlinear_native_at_current_H_solved')}}
        identity=dict(schema='actual94-published-primary-byte-and-producer-readback-v1',run_id=RUN,source_commit=SOURCE_COMMIT,job_id=JOB,
            artifact_id=args.artifact_id,artifact_bytes=args.artifact_bytes,artifact_sha256=args.artifact_sha256,
            artifact_identity_scope='Official tuple supplied by root; complete ZIP not downloaded in this primary readback',
            files=files,parent_and_report_checks=checks,typed_query_checks=query_checks,
            support_metadata_checks=support['metadata_matches'],original_scientific_flags=original_flags,
            source_count=len(verified),mathematical_producer_source_count=len(source_ledgers[0]),FD_source_count=len(source_ledgers[1]),
            verified_sources=verified,frozen_four_entry_files=required_entries,additional_observer_wrapper=required_entries[-1],
            producer_chain=chain,unresolved_sources=[],
            complete_scientific_artifact_downloaded_in_this_local_readback=False,
            complete_array_byte_audit_performed_in_this_primary_readback=False,full_QR_factor_files_independently_audited=False,
            mathematical_computation_performed=False)
        identity_receipt=write(out/'2026-11-15-actual94-primary-identity-readback.json',identity)
        support_receipt=write(out/'2026-11-15-actual94-original-B-C-H-support-readout.json.gz',support,True)
        trial_views=[selected_original_trial(row,i) for i,row in enumerate(trials)]
        nearest=[]
        for index in accepted_indices:
            preceding=[i for i in range(index) if trials[i].get('accepted') is not True]
            nearest.append(dict(accepted_trial_index=index,
                previous_rejected_trial_index=preceding[-1] if preceding else None,
                original_previous_rejected_trial=trial_views[preceding[-1]] if preceding else None))
        quick=dict(schema='actual94-original-trial-and-support-quick-readout-v1',run_id=RUN,
            status_original_scalars=scalars(s),model_original_scalars=scalars(m),
            original_before=prune(m.get('before')),query_specs=list(EXPECTED_QUERY_SPECS),
            all_trials=trial_views,accepted_original_trial_indices=accepted_indices,
            accepted_original_trials=[trial_views[i] for i in accepted_indices],nearest_previous_rejections=nearest,
            original_C_H_comparison=prune(q.get('comparison')),original_QP_report=prune(q.get('local_QP_report')),
            original_QP_last_saved_stage=prune(q.get('last_saved_local_stage')),
            original_FD={k:v for k,v in f.items() if k!='optimization_warm'},
            support_readout=support_receipt,identity_readback=identity_receipt,
            missing_actual_merit_or_RMS_not_filled_in=True,no_new_merit_norm_ratio_or_argmin_computed=True,
            no_next_query_or_budget_selection_performed=True)
        quick_receipt=write(out/'2026-11-15-actual94-original-quick-readout.json.gz',quick,True)
        provisional.update(schema='actual94-original-report-literal-readout-v1',identity_checks_not_yet_completed=False,
            identity_readback=identity_receipt,support_readout=support_receipt,
            actual_native_height=w['optimization_warm'].get('actual_native_height'),
            actual_global_scalar_parameters=w['optimization_warm'].get('actual_global_scalar_parameters'),
            actual_selected_original_angles_after=prune(w['optimization_warm'].get('actual_selected_original_angles_after')),
            actual_current_projection_entry=w.get(ENTRY_KEY),actual_current_condensed_entry=w.get('condensed_QP_entry'))
        result['literal_original_readout']=write(out/'2026-11-15-actual94-original-readout.json.gz',provisional,True)
        # Metadata mismatches are reported after all actual scalar views have
        # been preserved; they do not reclassify the original science result.
        binding_passed=all(checks.values()) and all(query_checks.values()) and all(support['metadata_matches'].values())
        result.update(completed=True,identity_checks_passed=binding_passed,
            identity=identity_receipt,support=support_receipt,quick=quick_receipt,
            original_status_flags=original_flags,accepted_original_trial_indices=accepted_indices,
            original_scientific_result_not_reclassified=True)
        return_code=0 if binding_passed else 2
    except Exception as error:
        result.update(completed=False,error_type=type(error).__name__,error=repr(error),
            original_scientific_result_not_reclassified=True)
        (out/'readback-error.txt').write_text(traceback.format_exc())
        return_code=2
    finally:
        write(out/'actual94-readback-result.json',result)
        print(json.dumps(result,ensure_ascii=False,allow_nan=False,indent=2),flush=True)
    return return_code

if __name__=='__main__':raise SystemExit(main())
