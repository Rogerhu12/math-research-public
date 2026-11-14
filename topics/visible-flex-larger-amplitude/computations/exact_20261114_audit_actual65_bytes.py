#!/usr/bin/env python3
"""Read/hash existing actual65 bytes only. No scientific imports or arithmetic."""
import argparse
import ast
import gzip
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import struct
import zipfile


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        while block := f.read(1024*1024):
            h.update(block)
    return h.hexdigest()


def read(path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)


def safe(root, name):
    p = PurePosixPath(name)
    assert not p.is_absolute() and '..' not in p.parts and '\\' not in name
    q = root.joinpath(*p.parts)
    assert not q.is_symlink() and q.resolve().is_relative_to(root.resolve())
    return q


def descriptor(root, d):
    p = safe(root, d['file'])
    digest = sha(p)
    assert p.stat().st_size == d['bytes'] and digest == d['sha256'], str(p)
    return {'file': d['file'], 'bytes': p.stat().st_size, 'sha256': digest}


def archived_bytes(root, ref):
    parts = []
    for part in ref['parts']:
        p = safe(root, part['file'])
        assert sha(p) == part['sha256'] and p.stat().st_size == part['bytes']
        with zipfile.ZipFile(p) as z:
            names = z.namelist()
            assert len(names) == 1 and names[0].endswith('.npy')
            b = z.read(names[0])
        assert b[:6] == b'\x93NUMPY'
        v = b[6]
        n = int.from_bytes(b[8:10 if v == 1 else 12], 'little')
        start = (10 if v == 1 else 12) + n
        h = ast.literal_eval(b[(10 if v == 1 else 12):start].decode('latin1'))
        assert h['descr'] == '<f8' and h['fortran_order'] is False
        payload = b[start:]
        ident = part['array']
        pref = str(tuple(ident['shape'])).encode()+b'\0'+ident['dtype'].encode()+b'\0'
        assert hashlib.sha256(pref+payload).hexdigest() == ident['sha256']
        parts.append(payload)
    payload = b''.join(parts)
    ident = ref['array_identity']
    pref = str(tuple(ident['shape'])).encode()+b'\0'+ident['dtype'].encode()+b'\0'
    assert hashlib.sha256(pref+payload).hexdigest() == ident['sha256']
    return payload


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory', type=Path, required=True)
    parser.add_argument('--original63', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    a = parser.parse_args()
    root, old = a.directory, a.original63
    summary = read(root/'summary.json')
    assert summary['completed'] is True
    receipts = [descriptor(root, summary['result']), descriptor(root, summary['array_manifest'])]
    result = read(root/summary['result']['file'])
    manifest = read(root/summary['array_manifest']['file'])
    assert result['source_sha256'] == '5033b8866dcc1fd158a7affda7305e1af90ece588ab1eca7d56dba4612ecb742'
    raw = {}
    for d in manifest['arrays']:
        receipts.append(descriptor(root, d))
        assert d['sha256'] == d['raw_sha256'] and d['order'] == 'C'
        count = 1
        for dimension in d['shape']:
            count *= dimension
        assert d['dtype'] == '<f8' and d['bytes'] == 8*count
        assert d['name'] not in raw
        raw[d['name']] = safe(root,d['file']).read_bytes()
    def json_outputs(obj):
        if isinstance(obj, dict):
            if isinstance(obj.get('file'), str) and obj['file'].startswith('large-arrays/') and obj['file'].endswith('.json.gz'):
                return [obj]
            return [x for v in obj.values() for x in json_outputs(v)]
        if isinstance(obj,list):
            return [x for v in obj for x in json_outputs(v)]
        return []
    jsons = {d['file']: d for d in json_outputs(result)}
    loaded = {}
    for name,d in jsons.items():
        receipts.append(descriptor(root,d)); loaded[name] = read(root/name)
    assert set(p.name for p in (root/'large-arrays').iterdir()) == set(Path(d['file']).name for d in receipts if d['file'].startswith('large-arrays/'))
    original_ledger = loaded[result['original_file_byte_ledger']['file']]
    source_receipts = []
    for name,d in original_ledger.items():
        assert d['file'] == name
        source_receipts.append(descriptor(old,d))
    number_count = 0
    rational_count = 0
    def records(obj):
        nonlocal number_count,rational_count
        if isinstance(obj,dict):
            if 'float64le_hex' in obj:
                h = obj['float64le_hex']; assert re.fullmatch(r'[0-9a-f]{16}',h)
                assert struct.pack('<d',obj['value']).hex() == h
                number_count += 1
            if set(obj)=={'numerator','denominator'}:
                assert re.fullmatch(r'-?\d+',obj['numerator'])
                assert re.fullmatch(r'[1-9]\d*',obj['denominator'])
                rational_count += 1
            for v in obj.values(): records(v)
        elif isinstance(obj,list):
            for v in obj: records(v)
    records(result)
    for obj in loaded.values(): records(obj)
    old_data = read(old/'eighteen-condensed-warm/condensed-QP-result.json.gz')
    old_b = archived_bytes(old/'eighteen-condensed-warm',old_data['original_b'])
    old_g = archived_bytes(old/'eighteen-condensed-warm',old_data['original_g'])
    local_desc = old_data['condensation_report']['output_arrays']['local-indices']
    lp = safe(old/'eighteen-condensed-warm/condensed-root',local_desc['file'])
    assert sha(lp) == local_desc['raw_sha256']
    local_indices = lp.read_bytes()
    ledger = loaded[result['local_rhs_construction']['exact_addition_error']['exact_ledger']['file']]
    assert len(ledger)==5749
    for j,row in enumerate(ledger):
        i = struct.unpack_from('<q',local_indices,8*j)[0]
        assert row['local_index']==j and row['global_index']==i
        assert row['saved_rhs']['float64le_hex'] == raw['original-recovery-rhs'][8*i:8*i+8].hex()
        assert row['saved_g']['float64le_hex'] == old_g[8*i:8*i+8].hex()
        assert row['nominal_force']['float64le_hex'] == raw['nominal-local-force'][8*j:8*j+8].hex()
        assert len(row['rounded_components'])==1
        assert row['rounded_components'][0]['float64le_hex'] == raw['solve-rhs-addition-error-0-rhs'][8*i:8*i+8].hex()
        assert row['unrepresented_remainder']=={'numerator':'0','denominator':'1'}
    rows = loaded[result['interval461_complete_row_table']['file']]
    assert len(rows)==338 and rows[1]==result['focus_row']==summary['focus_row']
    terms = list(result['focus_row']['action_terms'])
    for j,row in enumerate(rows):
        i = 461*338+j
        assert row['interval']==461 and row['physical_component']==j and row['global_row']==i
        assert row['original_b']['float64le_hex']==old_b[8*i:8*i+8].hex()
        assert list(row['action_terms'])==terms
        for name,record in row['action_terms'].items():
            assert record['float64le_hex']==raw['A-'+name][8*i:8*i+8].hex()
        for field,name in [('saved_recovered_Az','A-saved-recovered'),('saved_selected_Az','A-saved-selected'),('rebuilt_selected_Az','A-saved-selected')]:
            assert row[field]['float64le_hex']==raw[name][8*i:8*i+8].hex()
    fact = loaded[result['reconstructed_factor_report']['file']]
    for name,row in result['factor_reconstruction']['complete_factor_sha_comparison'].items():
        assert row['expected']==row['reconstructed']==fact['factor_arrays'][name]
        assert row['expected']['file'] is None and row['byte_digest_matches'] is True
    audit = {'schema':'actual65-output-and-consumed-input-byte-audit-v1','passed':True,
        'scope':'Existing bytes, descriptors, stored number bits and record order only; no matrix/norm/Fraction arithmetic',
        'result':summary['result'],'array_manifest':summary['array_manifest'],
        'new_raw_arrays':len(raw),'new_raw_bytes':sum(len(v) for v in raw.values()),
        'new_json_gzip_outputs':len(jsons),'new_output_descriptors':receipts,
        'original_consumed_files':len(source_receipts),'original_consumed_file_descriptors':source_receipts,
        'stored_number_records_bit_matched':number_count,'stored_rational_records_syntax_only':rational_count,
        'all_5749_RHS_records_original_operand_bits_matched':True,
        'all_338_row_records_original_b_and_named_action_bits_matched':True,
        'factor_arrays_were_memory_only_not_independently_file_hashed':True,
        'producer_factor_digest_comparisons_bound_to_complete_report':True,
        'no_scientific_module_imported':True,'no_numerical_quantity_recomputed':True,
        'no_new_acceptance_gate':True}
    a.out.mkdir(parents=True,exist_ok=True)
    detail=(json.dumps(audit,ensure_ascii=False,indent=2)+'\n').encode()
    (a.out/'audit.json').write_bytes(detail)
    scalars={'schema':'actual65-original-reported-model-response-readback-v1',
        'source_result':summary['result'],'source_summary_sha256':sha(root/'summary.json'),
        'original_input_binding':summary['input_binding'],
        'focus_row':result['focus_row'],'focus_L_R_P_contributions':result['focus_L_R_P_contributions'],
        'inverse_summary':result['inverse_summary'],'focus_precision_diagnostics':result['focus_precision_diagnostics'],
        'original_saved_recovery_replay':result['original_saved_recovery_replay'],
        'original_local_center_vs_complete_center_restriction':result['original_local_center_vs_complete_center_restriction'],
        'B_center_slack':summary['B_center_slack'],
        'new_computation_accounting':result['new_computation_accounting'],
        'elapsed_seconds':result['elapsed_seconds'],'maximum_RSS_kib':result['maximum_RSS_kib'],
        'numerical_readback_scope':'Values copied from the actual Actions report; no new local numerical calculation'}
    (a.out/'original-scalars.json').write_text(json.dumps(scalars,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'passed':True,'arrays':len(raw),'raw_bytes':audit['new_raw_bytes'],
        'json_gzip':len(jsons),'original_files':len(source_receipts),'number_records':number_count,
        'rational_records_syntax_only':rational_count,'audit_sha256':sha(a.out/'audit.json'),
        'scalars_sha256':sha(a.out/'original-scalars.json')}))


if __name__ == '__main__':
    main()
