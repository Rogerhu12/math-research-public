#!/usr/bin/env python3
"""Represent the actual CM divisor class B_minus4 on X_ns^+(41), modulo47^4."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile


def kernel(n, columns, free, block):
    result = [[[0, 0] for _ in free] for _ in range(n)]
    for j, index in enumerate(free):
        result[index-1][j] = [1, 0]
    for index, row in zip(columns, block):
        result[index-1] = row
    return result


def main():
    script = Path(__file__).resolve()
    data_dir = script.with_name('data')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--gp', default=shutil.which('gp') or '/tmp/pari-2.19.0/gp')
    parser.add_argument('--output', type=Path, default=data_dir/'p41_cm4_divisor47_certificate.json')
    args = parser.parse_args()
    source_names = ['p41_local47_torsion_certificate.json', 'p41_makdisi47_certificate.json.gz',
                    'p41_cusp_divisors47_certificate.json.gz']
    raw_sources = [(data_dir/name).read_bytes() for name in source_names]
    torsion, model, divisors = [json.loads(gzip.decompress(raw) if name.endswith('.gz') else raw)
                               for name, raw in zip(source_names, raw_sources)]
    reference = next(c for c in torsion['curves'] if c['label'] == 'Makdisi_j9_fibre')
    K1 = kernel(73, divisors['cusp_rank_columns_1based'], divisors['cusp_free_columns_1based'],
                divisors['canonical_kernel_block'])
    KI = kernel(199, divisors['K_rank_columns_1based'], divisors['K_free_columns_1based'],
                divisors['K_kernel_block'])
    inputs = [torsion['field_polynomial_ascending'], torsion['frobenius_lift'], reference['weil_pairing'],
              model['sqrt_minus_one_lift'], model['basis_pairs'], model['basis_inverse'],
              model['frobenius_basis_matrix'], model['necklaces'], model['sl2_representatives'],
              model['sl2_normalizer_mod_signs'], K1, divisors['canonical_coefficients'],
              divisors['square_basis_monomials_1based'], divisors['square_basis_inverse'], KI,
              divisors['K_free_columns_1based'], divisors['square_pivot_rows_1based'],
              model['evaluation_matrix'], model['frobenius_permutation_1based']]
    with tempfile.TemporaryDirectory(prefix='serre-p41-cm4-divisor47-') as temporary:
        temporary = Path(temporary)
        input_path, result_path = temporary/'input.gp', temporary/'result.json'
        input_path.write_text('cm4_input='+json.dumps(inputs, separators=(',', ':'))+';\n')
        code = '\n'.join([f'read({json.dumps(str(script.with_name(name)))});' for name in
                          ['p41_local47_torsion.gp', 'p41_makdisi47.gp', 'p41_cm3_makdisi47.gp',
                           'p41_cusp_divisors47.gp', 'p41_cm4_divisor47.gp']] +
                         [f'read({json.dumps(str(input_path))});',
                          f'p41_cm4_divisor47(cm4_input,{json.dumps(str(result_path))});', 'quit;'])
        proc = subprocess.Popen([args.gp, '-q', '-f', '-s', '1073741824'], stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        proc.stdin.write(code)
        proc.stdin.close()
        output = []
        for line in proc.stdout:
            print(line.rstrip(), flush=True)
            output.append(line)
        if proc.wait() != 0 or '***' in ''.join(output) or not result_path.exists():
            raise RuntimeError('Actual CM4 divisor construction failed; see output above')
        raw = json.loads(result_path.read_text())
    names = ['precision', 'P_constant', 'Q_old_constant', 'old_Weil_pairing', 'pairing_adjustment',
             'CM_unit_matrix', 'frobenius_torsion_matrix', 'P_jets', 'Q_jets',
             'elliptic_necklace_indices_1based', 'elliptic_frobenius_permutation_1based',
             'coarse_point_values', 'canonical_point_values', 'restriction_rank_rows_1based',
             'restriction_rank_columns_1based', 'restriction_free_columns_1based',
             'point_kernel_block', 'restriction_unit_minor_mod47', 'point_free_coordinates_1based',
             'point_frobenius_basis_matrix']
    assert len(raw) == len(names)
    result = dict(zip(names, raw))
    result.update({'level': 41, 'auxiliary_prime': 47, 'modulus': 47**4, 'curve_A': 1, 'curve_B': 0,
                   'stack_family': 'y^2=x^3+x+B', 'coarse_parameter': 't=B^2',
                   'coarse_trivialization': 'weight-two value divided by B',
                   'effective_divisor': 'K_f + Z_minus4', 'base_divisor': 'K_f + D',
                   'Jacobian_class_convention': '[effective_divisor - base_divisor] = B_minus4',
                   'source_sha256': {name: hashlib.sha256(raw).hexdigest()
                                     for name, raw in zip(source_names, raw_sources)},
                   'result': 'actual integral CM divisor class; no local-height or QC-root claim'})
    encoded = (json.dumps(result, sort_keys=True, separators=(',', ':'))+'\n').encode()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(encoded)
    print('Bytes', len(encoded), 'SHA256', hashlib.sha256(encoded).hexdigest())


if __name__ == '__main__':
    main()
