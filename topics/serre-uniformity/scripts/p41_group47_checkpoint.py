#!/usr/bin/env python3
"""Regenerate the partial V3/negative-B4/principal-norm research checkpoint."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

from p41_cm4_divisor47 import kernel


SOURCE_NAMES = ['p41_makdisi47_certificate.json.gz', 'p41_cusp_divisors47_certificate.json.gz',
                'p41_cm4_divisor47_certificate.json', 'p41_local47_torsion_certificate.json']
NAMES = ['cubic_selected_pairs_1based', 'cubic_extra_rows_1based', 'cubic_extra_inverse',
         'cubic_pivot_rows_1based', 'negative_rank_rows_1based', 'negative_rank_columns_1based',
         'negative_free_columns_1based', 'negative_kernel_block', 'negative_frobenius_matrix',
         'negative_flip_section_seeds_and_coefficients', 'negative_unit_minor_mod47',
         'norm_section_seeds_and_coefficients', 'norm_cusp_values', 'norm_CM4_values',
         'cusp_norm_ratio', 'CM4_norm_ratio', 'principal_B4_norm', 'principal_B4_log47']


def make_input(data_dir):
    raw = [(data_dir/n).read_bytes() for n in SOURCE_NAMES]
    m, d, z, t = [json.loads(gzip.decompress(b) if n.endswith('.gz') else b)
                  for n, b in zip(SOURCE_NAMES, raw)]
    K1 = kernel(73, d['cusp_rank_columns_1based'], d['cusp_free_columns_1based'], d['canonical_kernel_block'])
    KI = kernel(199, d['K_rank_columns_1based'], d['K_free_columns_1based'], d['K_kernel_block'])
    KZ = kernel(93, z['restriction_rank_columns_1based'], z['restriction_free_columns_1based'], z['point_kernel_block'])
    values = [m['evaluation_matrix'], m['frobenius_basis_matrix'], m['frobenius_permutation_1based'],
              K1, d['canonical_coefficients'], d['square_basis_monomials_1based'], d['square_basis_inverse'],
              d['square_pivot_rows_1based'], KI, KZ, z['point_frobenius_basis_matrix'], d['cusp_values'],
              z['coarse_point_values'], t['field_polynomial_ascending'], t['frobenius_lift'],
              m['sqrt_minus_one_lift']]
    return values, {n: hashlib.sha256(b).hexdigest() for n, b in zip(SOURCE_NAMES, raw)}


def main():
    script = Path(__file__).resolve()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--gp', default=shutil.which('gp') or '/tmp/pari-2.19.0/gp')
    parser.add_argument('--stack', type=int, default=1073741824)
    parser.add_argument('--write-input', type=Path, help='only write the reproducible GP input and stop')
    parser.add_argument('--output', type=Path, default=script.with_name('data')/'p41_group47_checkpoint.json.gz')
    args = parser.parse_args()
    inputs, hashes = make_input(script.with_name('data'))
    input_text = 'group_input='+json.dumps(inputs, separators=(',', ':'))+';\n'
    if args.write_input:
        args.write_input.write_text(input_text)
        return
    with tempfile.TemporaryDirectory(prefix='serre-p41-group47-checkpoint-') as temporary:
        temporary = Path(temporary)
        input_path, output_path = temporary/'input.gp', temporary/'output.json'
        input_path.write_text(input_text)
        code = '\n'.join([f'read({json.dumps(str(script.with_name(n)))});' for n in
                          ['p41_local47_torsion.gp', 'p41_makdisi47.gp', 'p41_cusp_divisors47.gp',
                           'p41_group47_checkpoint.gp']] + [f'read({json.dumps(str(input_path))});',
                          'G=p41g_checkpoint(group_input);N=G[7];V=p41n_run(group_input);',
                          'write('+json.dumps(str(output_path))+',[vector(126,j,G[1][G[3][3][j]]),G[3][2],p41m_encode(G[3][4]),G[5],N[1][1],N[1][2],N[1][3],p41m_encode(vecextract(N[1][4],N[1][2],"..")),p41m_encode(N[2]),vector(2,j,[p41d_qvec(N[j+2][1]),p41d_qvec(N[j+2][2])]),[lift(polcoef(N[1][5].pol,0)),lift(polcoef(N[1][5].pol,1))],vector(2,j,[p41d_qvec(V[1][j][1][1]),p41d_qvec(V[1][j][1][2])]),vector(2,j,vector(20,k,p41l_vec(V[1][j][3][k]))),vector(2,j,p41d_qvec(V[1][j][4])),p41l_vec(V[2]),p41m_pair(V[3]),lift(V[4]),lift(V[5])]);',
                          'quit;'])
        proc = subprocess.Popen([args.gp, '-fq', '-s', str(args.stack)], stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        proc.stdin.write(code)
        proc.stdin.close()
        output = []
        for line in proc.stdout:
            print(line.rstrip(), flush=True)
            output.append(line)
        if proc.wait() or '***' in ''.join(output) or not output_path.exists():
            raise RuntimeError('Partial checkpoint replay failed; the existing checkpoint was not changed')
        payload = json.loads(output_path.read_text())
    assert len(payload) == len(NAMES)
    result = dict(zip(NAMES, payload))
    result.update(level=41, auxiliary_prime=47, precision=4, modulus=47**4,
                  status='intermediate checkpoint; V3, negative B4 and principal norm verified in GP; no completed double or nonprincipal height',
                  source_sha256=hashes)
    raw = (json.dumps(result, sort_keys=True, separators=(',', ':'))+'\n').encode()
    compressed = gzip.compress(raw, mtime=0)
    args.output.write_bytes(compressed)
    print('Raw bytes', len(raw), 'gzip bytes', len(compressed), 'SHA256', hashlib.sha256(compressed).hexdigest())


if __name__ == '__main__':
    main()
