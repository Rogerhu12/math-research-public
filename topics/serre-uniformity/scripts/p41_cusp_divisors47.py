#!/usr/bin/env python3
"""Construct actual cusp and canonical divisor ideals in the R102 model."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile


NAMES = [
    'precision', 'cusp_representatives_1based', 'necklace_to_cusp_1based',
    'cusp_frobenius_permutation_1based', 'cusp_values',
    'cusp_rank_rows_1based', 'cusp_rank_columns_1based', 'cusp_free_columns_1based',
    'canonical_kernel_block', 'canonical_frobenius_matrix',
    'canonical_trace_seed', 'canonical_coefficients', 'canonical_cusp_leading_values',
    'canonical_CM_value', 'cusp_unit_minor_mod47',
    'square_basis_monomials_1based', 'square_pivot_rows_1based', 'square_basis_inverse',
    'D_rank_rows_1based', 'D_rank_columns_1based', 'D_free_columns_1based', 'D_kernel_block',
    'second_canonical_trace_seed', 'second_canonical_coefficients',
    'K_rank_rows_1based', 'K_rank_columns_1based', 'K_free_columns_1based', 'K_kernel_block',
    'K_unit_minor_mod47', 'square_CM_values',
]


def inputs_from_sources(data_dir):
    names = ['p41_local47_torsion_certificate.json', 'p41_makdisi47_certificate.json.gz',
             'p41_cm3_makdisi47_certificate.json']
    raw = [(data_dir / name).read_bytes() for name in names]
    torsion, model, cm = [json.loads(gzip.decompress(b) if n.endswith('.gz') else b)
                         for n, b in zip(names, raw)]
    ref = next(c for c in torsion['curves'] if c['label'] == 'Makdisi_j9_fibre')
    inputs = [torsion['field_polynomial_ascending'], torsion['frobenius_lift'],
              ref['weil_pairing'], model['sqrt_minus_one_lift'], model['basis_pairs'],
              model['basis_inverse'], model['frobenius_basis_matrix'], model['evaluation_matrix'],
              model['necklaces'], model['sl2_representatives'], model['sl2_normalizer_mod_signs'],
              cm['coarse_evaluation_coefficients'][0]]
    return inputs, {n: hashlib.sha256(b).hexdigest() for n, b in zip(names, raw)}


def save_result(raw, hashes, path):
    assert len(raw) == len(NAMES)
    result = dict(zip(NAMES, raw))
    result.update({'level': 41, 'auxiliary_prime': 47, 'modulus': 47 ** 4,
                   'source_sha256': hashes,
                   'line_bundle': 'K_X + D', 'canonical_divisor_degree': 106,
                   'Tate_Weil_convention': 'beta(c,d)=q_41^c*zeta^(-d); zeta is the PARI pairing',
                   'result': 'actual cusp, canonical, and CM divisor inputs; no QC root certificate'})
    encoded = (json.dumps(result, sort_keys=True, separators=(',', ':')) + '\n').encode()
    compressed = gzip.compress(encoded, mtime=0)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(compressed)
    print('Raw bytes', len(encoded), 'gzip bytes', len(compressed),
          'SHA256', hashlib.sha256(compressed).hexdigest())


def main():
    script = Path(__file__).resolve()
    data_dir = script.with_name('data')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--gp', default=shutil.which('gp') or '/tmp/pari-2.19.0/gp')
    parser.add_argument('--output', type=Path, default=data_dir/'p41_cusp_divisors47_certificate.json.gz')
    args = parser.parse_args()
    inputs, hashes = inputs_from_sources(data_dir)
    with tempfile.TemporaryDirectory(prefix='serre-p41-divisors47-') as temporary:
        temporary = Path(temporary)
        input_path = temporary / 'input.gp'
        result_path = temporary / 'result.json'
        input_path.write_text('cusp_input=' + json.dumps(inputs, separators=(',', ':')) + ';\n')
        code = '\n'.join([
            f'read({json.dumps(str(script.with_name("p41_local47_torsion.gp")))});',
            f'read({json.dumps(str(script.with_name("p41_makdisi47.gp")))});',
            f'read({json.dumps(str(script.with_suffix(".gp")))});',
            f'read({json.dumps(str(input_path))});',
            f'p41_cusp_divisors47(cusp_input,{json.dumps(str(result_path))});', 'quit;'])
        proc = subprocess.Popen([args.gp, '-q', '-f', '-s', '1073741824'],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, text=True)
        proc.stdin.write(code)
        proc.stdin.close()
        output = []
        for line in proc.stdout:
            print(line.rstrip(), flush=True)
            output.append(line)
        if proc.wait() != 0 or '***' in ''.join(output) or not result_path.exists():
            raise RuntimeError('Cusp/divisor construction did not complete; see output above')
        save_result(json.loads(result_path.read_text()), hashes, args.output)


if __name__ == '__main__':
    main()
