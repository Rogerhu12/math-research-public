#!/usr/bin/env python3
"""Exact integer expansion including both actual initial moving V2 functions.

The result retains honest section factors with signed integer exponents.
Its formal divisor is checked over Z, before any47-adic reduction, and
its logarithmic derivatives are compared with the independent forward DAG.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path

Q = 47**4


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def save(path, data):
    raw = (json.dumps(data, sort_keys=True, separators=(',', ':'))+'\n').encode()
    temp = path.with_suffix(path.suffix+'.new')
    temp.write_bytes(gzip.compress(raw, mtime=0))
    temp.replace(path)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--transport-directory', type=Path, required=True)
    ap.add_argument('--second-kind-certificate', type=Path, required=True)
    ap.add_argument('--bases', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    manifest_path = args.transport_directory/'transport_manifest47.json'
    run_path = args.transport_directory.parent/'run_manifest47.json'
    manifest, run, second = read(manifest_path), read(run_path), read(args.second_kind_certificate)
    bases = read(args.bases)
    assert second['input_sha256'][args.bases.name] == sha(args.bases)
    assert manifest['complete_all454_multiplication_principal_functions']
    assert manifest['complete_two_actual_initial_moving_flips'] and manifest['nonformal_principal_function_count']==457
    assert second['complete_actual54_second_kind_center_integrals']
    assert manifest['disk_id'] == second['disk_id']
    assert second['principal_chain']['transport_manifest_sha256'] == sha(manifest_path)
    functions, entries = [], {}
    for entry in manifest['functions']:
        if entry['phase'] == 'formal_extraction':
            continue
        path = args.transport_directory/entry['filename']
        assert sha(path) == entry['sha256']
        rec = read(path)
        functions.append(rec)
        entries[rec['label']] = entry
    functions.sort(key=lambda rec: (-3+rec['moving_order_0based'],0) if rec['phase'].startswith('initial_moving_') else (-1, 0) if rec['phase'] == 'initial_negative'
                   else (rec['bit'], 0 if rec['operation'] == 'double_addflip' else 1))
    assert len(functions) == 457 and sum(f['line_bundle_power']==2 for f in functions)==3 and sum(f['line_bundle_power']==3 for f in functions)==454
    outputs = [f['output_node']['point_sha256'] for f in functions]
    assert len(set(outputs)) == len(outputs)
    initial, final = manifest['initial_node']['point_sha256'], manifest['final_node']['point_sha256']
    assert initial not in outputs
    scale = manifest['final_node']['scalar_coefficient_of_C']
    adjoint = {final: -1}
    exponents = {}
    for rec in reversed(functions):
        node = rec['output_node']['point_sha256']
        coefficient = adjoint.pop(node, 0)
        exponents[rec['label']] = coefficient
        for parent in rec['input_nodes']:
            key = parent['point_sha256']
            adjoint[key] = adjoint.get(key, 0)-coefficient
    assert all(v == 0 for k, v in adjoint.items() if k != initial)
    initial_exponent = adjoint[initial]
    assert initial_exponent == -scale
    divisor = {initial: initial_exponent, 'C=P_center-P_minus3': -initial_exponent}
    factors = []
    total_weight = initial_exponent
    for rec in functions:
        exponent = exponents[rec['label']]
        total_weight += rec['line_bundle_power']*exponent
        for node in rec['input_nodes']+[rec['output_node']]:
            key = node['point_sha256']
            divisor[key] = divisor.get(key, 0)+exponent
        if exponent:
            factors.append({'label': rec['label'], 'line_bundle_power': rec['line_bundle_power'],
                            'signed_integer_exponent': exponent,
                            'source_function_filename': entries[rec['label']]['filename'],
                            'source_function_sha256': entries[rec['label']]['sha256']})
    divisor = {k: v for k, v in divisor.items() if v}
    assert divisor == {'C=P_center-P_minus3': scale, final: -1}
    # An independent direct integer weighted sum matches the forward recurrence.
    chain = second['principal_chain']
    first = chain['initial_log_norm_derivative_f_b_over_f0'][0]
    derivatives = {r['label']: r['log_norm_derivative_at_family2'][0] for r in chain['function_log_norm_derivatives']}
    answer = [[initial_exponent*x % Q for x in pair] for pair in first]
    for label, exponent in exponents.items():
        row = derivatives[label]
        for j in range(54):
            for c in range(2):
                answer[j][c] = (answer[j][c]+exponent*row[j][c]) % Q
    expected = chain['log_norm_derivative_of_sign_mC_minus_Dfinal_principal_function'][0]
    assert answer == expected
    endpoint = second['endpoint']
    assert bases['families'][0]['points_1based'] == endpoint['family1_points_1based']
    extra = endpoint['terminal_transport_log_norm_derivative_at_family2_mod47four'][0]
    combined = [[(answer[j][c]+extra[j][c]) % Q for c in range(2)] for j in range(54)]
    tiny = endpoint['actual_second_kind_tiny_integrals_at_family1_mod47four'][0]
    actual = second['actual54_second_kind_integrals_of_C_mod47four'][0]
    assert all((scale*actual[j][c]-tiny[j][c]-combined[j][c]) % Q == 0 for j in range(54) for c in range(2))
    output = {
        'level': 41, 'auxiliary_prime': 47, 'precision': 4, 'modulus': Q,
        'disk_id': manifest['disk_id'],
        'complete_exact_integer_principal_function_expression': True,
        'complete_two_actual_initial_moving_flips_in_integer_SLP':True,
        'nonformal_principal_function_count':457,
        'moving_f_integer_exponent':exponents[next(f['label'] for f in functions if f['phase']=='initial_moving_first')],
        'moving_h_integer_exponent':exponents[next(f['label'] for f in functions if f['phase']=='initial_moving_second')],
        'formal_divisor_identity_checked_over_Z': True,
        'formal_divisor': divisor,
        'function_formula': 'f_b^e_b * f0^e_0 * product(F_step^e_step)',
        'f_b_integer_exponent': initial_exponent,
        'f0_integer_exponent': -total_weight,
        'f_b_coefficients': run['f_b_weight2_coefficients'],
        'f0_coefficients': run['f0_weight2_coefficients'],
        'section_factors': factors,
        'total_section_weight_zero': initial_exponent-total_weight+sum(f['line_bundle_power']*f['signed_integer_exponent'] for f in factors) == 0,
        'direct_weighted_log_norm_derivative_at_family2_mod47four': [answer],
        'independent_forward_and_reverse_SLPS_match_all54_derivatives': True,
        'combined_function_to_actual_A1_t': {
            'formula': 'f_b^e_b * f0^(e_0-1) * product(F_step^e_step) * v1 * F_terminal / G_terminal',
            'formal_divisor': {'C=P_center-P_minus3': scale, 'A1(t)': -1},
            'f_b_integer_exponent': initial_exponent,
            'f0_integer_exponent': -total_weight-1,
            'v1_weight2_coefficients': bases['families'][0]['v_coefficients'],
            'F_terminal_V2_coefficients': endpoint['terminal_transport_numerator_V2'],
            'G_terminal_V2_coefficients': endpoint['terminal_transport_denominator_V2'],
            'actual_A1_physical_parameters': endpoint['family1_physical_parameters_mod47four'],
            'log_norm_derivative_at_family2_mod47four': [combined],
            'all54_principal_norm_plus_tiny_equal_scale_times_actual_integral': True,
        },
        'input_sha256': {manifest_path.name: sha(manifest_path), run_path.name: sha(run_path),
                         args.second_kind_certificate.name: sha(args.second_kind_certificate), args.bases.name: sha(args.bases)},
        'source_sha256': sha(__file__),
    }
    assert output['total_section_weight_zero']
    assert output['moving_f_integer_exponent']==scale and output['moving_h_integer_exponent']==-scale
    save(args.output, output)
    print('PASS exact integer divisor cancellation and complete principal expression', manifest['disk_id'],
          'nonzero step factors', len(factors), 'SHA', sha(args.output), flush=True)


if __name__ == '__main__':
    main()
