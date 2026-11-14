#!/usr/bin/env python3
"""Hash the complete mathematical content of a regenerable inner DQ source.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Only volatile timings, command paths and storage metadata are excluded.
Every source coefficient, input centre cap, true strip, domain, window,
support partition and singleton mode remains in the mathematical digest.
This is a storage/reproduction identity, not another mathematical proof.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import platform
import flint

KEYS = ['schema','modes_center','cells','windows_out','windows_in','rows',
    'parameter_domain','normalization','low_singleton_input_modes',
    'low_singleton_matrix_shape','unreduced_coefficients','exact_ell_reduction',
    'positive_sum_difference_formula','membership_partition','membership_intervals',
    'endpoint_maximization_proof','operator_contract','low_singleton_contract',
    'material_units_clarification','no_input_window_mode_count_multiplier',
    'all_reference_positive_modes_retained','actual_difference_weights_recomputed_at_translated_tau']


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--resource',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise FileExistsError(a.out)
    with gzip.open(a.input,'rt') as stream:data=json.load(stream)
    resource=json.loads(a.resource.read_text())
    if (not data['all_gates'] or not all(data['gates'].values()) or
            resource['exitcode']!=0 or not resource['wait4_observed'] or
            resource['peak_rss_kib']>98304):
        raise ValueError('Use the completed source with the actual 96MiB resource budget')
    digest=hashlib.sha256()
    for chunk in json.JSONEncoder(sort_keys=True,separators=(',',':'),ensure_ascii=True).iterencode({k:data[k] for k in KEYS}):
        digest.update(chunk.encode('utf-8'))
    result=dict(schema='complete-inner-DQ-mathematical-reproduction-digest-v1',
        source_sha256=sha(__file__),primary_path=str(a.input),primary_sha256=sha(a.input),
        primary_bytes=a.input.stat().st_size,resource_path=str(a.resource),resource_sha256=sha(a.resource),
        mathematical_payload_keys=KEYS,mathematical_payload_sha256=digest.hexdigest(),
        canonical_json_encoding='JSONEncoder(sort_keys=True,separators=(comma,colon),ensure_ascii=True), UTF-8, no final newline',
        producer_sha256=data['source_sha256'],input_identities=data['input_identities'],
        exact_parameter_domain=data['parameter_domain'],normalization=data['normalization'],
        shifted_P1_input_domain=data['shifted_P1_input_domain'],
        row_count=len(data['rows']),windows_out=data['windows_out'],windows_in=data['windows_in'],
        kernel_shape=[213,2,13,15],low_singleton_matrix_shape=data['low_singleton_matrix_shape'],
        all_saved_gates=True,saved_gate_count=len(data['gates']),
        actual_material_domination_comparisons=data['actual_material_domination_comparisons'],
        precision_bits=data['precision_bits'],coefficient_storage_significant_bits=data['coefficient_storage_significant_bits'],
        python_version=platform.python_version(),python_flint_version=flint.__version__,
        actual_owned_exitcode=resource['exitcode'],actual_wall_seconds=resource['wall_seconds'],
        actual_peak_rss_kib=resource['peak_rss_kib'],derived_primary_stays_in_scratch=True,
        original_primary_byte_hash_is_immutable_but_regenerated_timing_fields_may_differ=True,
        full_mathematical_digest_is_required_for_same_version_reproduction=True,
        ODE_Node_Green_calls=0)
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(out=str(a.out),sha256=sha(a.out),mathematical_payload_sha256=digest.hexdigest())),flush=True)


if __name__=='__main__':main()
