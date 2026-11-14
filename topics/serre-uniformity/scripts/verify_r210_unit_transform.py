#!/usr/bin/env python3
"""Verify the integral short-unit identity needed in R210.

Input is the already published small_robert_norm_target_certificate.json.
Only integer arithmetic is used.  This does not calculate a norm preimage,
the ray class group of L, or the secondary scalar L.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path


def verify(path):
    raw = Path(path).read_bytes()
    source = json.loads(raw)
    coeffs = [int(x) for x in source['factors'][0]['coefficients']]
    n = len(coeffs) - 1
    assert n == 44 and coeffs[0] == coeffs[-1] == 1
    assert coeffs == coeffs[::-1]
    # T_k = i^k c_k.  The integer Gaussian coefficient representation
    # is the pair [real part, imaginary part].
    target = []
    transformed = [[0, 0] for _ in range(n + 1)]
    for k, a in enumerate(coeffs):
        z = [(a, 0), (0, a), (-a, 0), (0, -a)][k % 4]
        target.append(list(z))
        # (1-X)^44 f(i(1+X)/(1-X)).
        for j in range(k + 1):
            for ell in range(n - k + 1):
                scalar = math.comb(k, j) * math.comb(n-k, ell) * (-1)**ell
                for c in (0, 1):
                    transformed[j+ell][c] += scalar * z[c]
    exact_factor = -(2**22)
    assert all(transformed[k][c] == exact_factor * target[k][c]
               for k in range(n+1) for c in (0, 1))
    assert target[0] == target[-1] == [1, 0]
    content = math.gcd(*(abs(x) for row in transformed for x in row))
    assert content == 2**22
    # Exact conversion of the old low-weight scalar to the new residue.
    residues = []
    for low_L in range(43):
        rho = (low_L + 3) % 43
        v = (-4 * low_L - 12) % 43
        omega_positive = (10 - low_L) % 43
        assert v == -4 * rho % 43
        assert (rho == 0) == (low_L == 40) == (v == 0)
        assert (rho == 0) == (omega_positive == 13)
        assert (omega_positive == 0) == (rho == 13)
        residues.append([low_L, rho, v, omega_positive])
    return {
        'status': 'PASS',
        'source_sha256': hashlib.sha256(raw).hexdigest(),
        'degree': n,
        'fz_coefficients_ascending': [str(a) for a in coeffs],
        'unit_polynomial_gaussian_coefficients_ascending': [[str(a), str(b)] for a,b in target],
        'identity_factor': exact_factor,
        'raw_transform_content': content,
        'integral_monic': True,
        'constant_unit': True,
        'all_45_gaussian_coefficient_identities': True,
        'scalar_table_lowL_rho_v_omega': residues,
        'actual_norm_preimage_computed': False,
        'actual_ray_length_computed': False,
        'actual_L_computed': False,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('source')
    ap.add_argument('--certificate')
    ap.add_argument('--check')
    a = ap.parse_args()
    output = verify(a.source)
    if a.check:
        assert json.loads(Path(a.check).read_text()) == output
    if a.certificate:
        Path(a.certificate).write_text(json.dumps(output, ensure_ascii=False, separators=(',', ':')) + '\n')
    print(json.dumps({k:v for k,v in output.items() if k not in {
        'fz_coefficients_ascending', 'unit_polynomial_gaussian_coefficients_ascending',
        'scalar_table_lowL_rho_v_omega'}}, ensure_ascii=False, separators=(',', ':')))


if __name__ == '__main__':
    main()
