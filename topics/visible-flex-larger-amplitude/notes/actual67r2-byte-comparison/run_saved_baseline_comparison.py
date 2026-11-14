#!/usr/bin/env python3
"""Read/hash actual67 bytes and compare with the already verified actual66 receipt.
Pure standard-library array bytes only; no mathematical operations.
"""
from pathlib import Path
import gzip,hashlib,importlib.util,json,sys,traceback
HERE=Path(__file__).resolve().parent
SOURCE=HERE/'exact_20261114_compare_actual66_67_model_bytes.py'
BASE=HERE/'verified66-baseline.json.gz'
OUT=HERE/'actual67r2-byte-comparison'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()=='28292fe1611efa18373f7a9419e3ee3a22867e6ac6de5ffd197e0a57948dc072'
assert hashlib.sha256(BASE.read_bytes()).hexdigest()=='74cb59651a3908ba2dea664775ff76fde2bcb9f7e268579d4c80c366f5bca6aa'
spec=importlib.util.spec_from_file_location('frozen_byte_comparison',SOURCE)
M=importlib.util.module_from_spec(spec);spec.loader.exec_module(M)
OUT.mkdir(exist_ok=False)
s={"schema":"actual66-67-same-base-model-byte-comparison-v2","no_scientific_modules_imported":True,"no_norm_matrix_action_or_Fraction_computed":True,"actual66_verified_baseline_receipt_reused":{"file":BASE.name,**M.sha_file(BASE)},"original_byte_reader_source":{"file":SOURCE.name,**M.sha_file(SOURCE)},"new_scientific_acceptance_gate":False}
try:
 base=json.loads(gzip.decompress(BASE.read_bytes()))
 assert base['parent']['actual_parent_warm_sha256']==M.PARENT_WARM
 assert base['parent']['actual_parent_status_sha256']==M.PARENT_STATUS
 assert base['parent']['entry_source_sha256']==M.BASE_SOURCE
 assert base['damping']==270.0
 changed=M.read_model('/tmp/visible-larger-recovery-2207/actions-debug/visible-followup-condensedqp-43652955632-1/twenty-lambda27-condensed-warm',M.CHANGED_SOURCE,M.CHANGED_SCHEMA,27.0)
 comp=M.comparison(base,changed)
 body={"baseline":base,"changed":changed,"comparison":comp}
 dst=OUT/'complete-byte-detail.json.gz'
 dst.write_bytes(gzip.compress((json.dumps(body,separators=(',',':'),allow_nan=False)+'\n').encode(),mtime=0))
 s.update(completed=True,detail={"file":dst.name,**M.sha_file(dst)},B_file_count=comp['B_file_count'],B_array_count=comp['B_array_count'],all_verified_B_payloads_equal=comp['all_verified_B_payloads_equal'],all_original_b_g_c_payloads_equal=all(v['same_actual_complete_raw_sha256']for v in comp['original_arrays'].values()),all_scientific_binding_records_equal=all(v['equal']for v in comp['scientific_binding_records'].values()),all_original_full_A_input_records_equal=all(v['equal']for v in comp['original_full_A_input_records'].values()),B_base_identity_equal=comp['B_base_identity_equal'],B_query_specs_equal=comp['B_query_specs_equal'],metadata_B_model_SHA=comp['metadata_B_model_SHA'],expected_changed_C=comp['expected_changed_C'],changed_condensed_root_raw_array_count=len(changed['verified_condensed_root_arrays']),original_complete_A_and_QR_factor_payloads_not_exported=True)
except Exception as e:
 s.update(completed=False,error=repr(e),traceback=traceback.format_exc())
s['invocation_source']={"file":Path(__file__).name,**M.sha_file(__file__)}
(OUT/'summary.json').write_text(json.dumps(s,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
print(json.dumps(s,ensure_ascii=False))
sys.exit(0 if s.get('completed') else 1)
