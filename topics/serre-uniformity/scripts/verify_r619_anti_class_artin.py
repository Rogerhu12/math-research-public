#!/usr/bin/env python3
"""Small arithmetic check for R619, reusing the actual published R198 rows."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path


def read(path):
    raw = path.read_bytes()
    if path.suffix == '.gz':
        raw = gzip.decompress(raw)
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


def mul(a, b):
    return [(a[0]*b[0]-a[1]*b[1]) % 43,
            (a[0]*b[1]+a[1]*b[0]) % 43]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('r198', type=Path)
    ap.add_argument('--output', type=Path, required=True)
    ap.add_argument('--check', type=Path)
    args = ap.parse_args()
    old, digest = read(args.r198)
    assert digest == 'e1666e118c7f10d991cf4aa0107ebbe8b68683cd7c9b3e08a587aab390e86d00'
    assert old['expected']['status'] == 'PASS'
    assert old['anti_p_step'] == 21 and old['tame_correction'] == 11
    rows = old['expected']['rows']
    assert len(rows) == 44
    w = [1, 0]
    base = [0, 0]
    deriv = [0, 0]
    for j, row in enumerate(rows):
        assert row['index'] == j and row['norm_ratio'] == '1'
        base = [(base[c] + w[c]*row['base_unit_log']) % 43 for c in range(2)]
        deriv = [(deriv[c] + w[c]*row['derivative_log']) % 43 for c in range(2)]
        w = mul(w, [8, 25])
    assert w == [1, 0] and base == [0, 0] and deriv == [0, 13]
    q = int(old['q'])
    assert (q*q-1) % 43 == 0 and ((q*q-1)//43) % 43 == 21
    assert (q-1) % 43 != 0
    A_prime = [(-a) % 43 for a in deriv]
    h_log = A_prime
    C_t = mul([0, (-pow(32, -1, 43)) % 43], h_log)
    assert A_prime == [0, 30] and C_t == [9, 0]
    artin_q = 44*32 % 43
    artin_D = mul([0, -44 % 43], h_log)
    assert artin_q != 0 and artin_D == [30, 0]
    assert mul(C_t, [artin_q, 0]) == artin_D
    out = {
        'status': 'PASS', 'p': 43,
        'r198_uncompressed_sha256': digest,
        'actual_44_row_base_power_log': base,
        'actual_44_row_D_T_u_t_power_log': deriv,
        'A_ell_derivative_at_1': A_prime,
        'local_norm_obstruction_length': 42,
        'ramified_character_divisor_length': 43,
        'ordinary_Gamma_invariant_class_length': 43-42,
        'genus_artin_on_marked_q_class': [artin_q, 0],
        'h_t_power_log': h_log,
        'genus_artin_on_D_t': artin_D,
        'auxiliary_anti_p_C_t': C_t,
        'direct_mu_index_from_power_log_factor': pow(21, -1, 43),
        'large_Robert_evaluations_repeated': False,
        'original_scalar_C_computed': False,
        'original_J_computed': False,
        'original_b_lambda_n_computed': False,
        'original_L_computed': False,
        'full_layer_class_length_43_restored': False,
        'full_mixed_unit_lattice_restored': False,
    }
    if args.check:
        prior, _ = read(args.check)
        assert prior == out
    args.output.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out))


if __name__ == '__main__':
    main()
