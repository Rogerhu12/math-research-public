#!/usr/bin/env python3
"""Actual first jets at the820 level41 evaluation points, modulo47^4."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile


def main():
    script = Path(__file__).resolve()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--gp', default=shutil.which('gp') or '/tmp/pari-2.19.0/gp')
    parser.add_argument('--output', type=Path,
                        default=script.with_name('data')/'p41_evaluation_jets47_checkpoint.json.gz')
    args = parser.parse_args()
    names = ['p41_local47_torsion_certificate.json', 'p41_makdisi47_certificate.json.gz']
    raw = [(script.with_name('data')/name).read_bytes() for name in names]
    torsion, model = [json.loads(gzip.decompress(b) if name.endswith('.gz') else b)
                      for b, name in zip(raw, names)]
    curve = next(c for c in torsion['curves'] if c['label'] == 'Makdisi_j9_fibre')
    inputs = [torsion['field_polynomial_ascending'], torsion['frobenius_lift'], curve['P'], curve['Q'],
              curve['weil_pairing'], model['sqrt_minus_one_lift'], model['basis_pairs'], model['basis_inverse'],
              model['sl2_representatives'], model['sl2_normalizer_mod_signs'], model['frobenius_basis_matrix'],
              model['frobenius_permutation_1based'], model['evaluation_matrix']]
    with tempfile.TemporaryDirectory(prefix='serre-p41-evaluation-jets47-') as folder:
        folder = Path(folder)
        ipath, opath = folder/'input.gp', folder/'output.json'
        ipath.write_text('jet_input='+json.dumps(inputs, separators=(',', ':'))+';\n')
        code = '\n'.join([f'read({json.dumps(str(script.with_name(name)))});' for name in
                          ['p41_local47_torsion.gp', 'p41_makdisi47.gp', 'p41_cm3_makdisi47.gp',
                           'p41_cusp_divisors47.gp', 'p41_cm4_divisor47.gp', 'p41_evaluation_jets47.gp']] +
                         [f'read({json.dumps(str(ipath))});',
                          f'p41_evaluation_jets47(jet_input,{json.dumps(str(opath))});', 'quit;'])
        proc = subprocess.Popen([args.gp, '-q', '-f', '-s', '1073741824'], stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        proc.stdin.write(code)
        proc.stdin.close()
        output = []
        for line in proc.stdout:
            print(line.rstrip(), flush=True)
            output.append(line)
        if proc.wait() != 0 or '***' in ''.join(output) or not opath.exists():
            raise RuntimeError('Actual evaluation jets did not complete; see output above')
        record = json.loads(opath.read_text())
    data = {'level': 41, 'auxiliary_prime': 47, 'precision': 4, 'modulus': 47**4,
            'source_sha256': {n: hashlib.sha256(b).hexdigest() for n, b in zip(names, raw)},
            'family': 'y^2=x^3+x+32+t', 'parameter': 't=B-32',
            'P_jets': record[0], 'Q_jets': record[1], 'evaluation_derivatives': record[2],
            'status': 'actual GP computation and constant-term/Frobenius checks; independent verification pending'}
    encoded = (json.dumps(data, sort_keys=True, separators=(',', ':'))+'\n').encode()
    packed = gzip.compress(encoded, mtime=0)
    assert len(packed) < 5_000_000
    args.output.write_bytes(packed)
    print('Saved', len(packed), 'bytes; SHA256', hashlib.sha256(packed).hexdigest(), flush=True)


if __name__ == '__main__':
    main()
