#!/usr/bin/env python3
"""True formal Poincare values for (mC,3mD_P), reusing the first inverse.

Only the new second inverse is constructed.  Both Abel frames, both
principal functions and the actual Hecke bilinear correction are retained.
This does not by itself perform the nonformal Miller transport.
"""
import argparse
import ctypes
import gc
import gzip
import hashlib
import json
from pathlib import Path
import random
import resource
import sys
import time


def read(path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw), hashlib.sha256(raw).hexdigest()


def digest(value):
    return hashlib.sha256(json.dumps(value, separators=(',', ':')).encode()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir', type=Path, required=True)
    parser.add_argument('--target', choices=['12', '7', 'common'], required=True)
    parser.add_argument('--endpoints', type=Path)
    parser.add_argument('--bases', type=Path)
    parser.add_argument('--jets', type=Path)
    parser.add_argument('--first-inverses', type=Path)
    parser.add_argument('--hessian', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    folder = args.script_dir.resolve()
    sys.path.insert(0, str(folder))
    import numpy as np
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources, make_model
    from p41_hecke3_hessian47 import section_jets
    from p41_poincare_formal47 import principal_inverse
    from p41_poincare_norms47 import pair_mul, pair_inverse
    from p41_formal47_multiply import point_hash, write_checkpoint
    started = time.monotonic()
    inputs = {}
    endpoints, inputs['actual_second_endpoints'] = read(args.endpoints or folder/'data/p41_translation_formal_endpoints47_checkpoint.json.gz')
    target_name = 'three_m_D_b' if args.target == 'common' else 'three_m_D'+args.target
    item = endpoints['targets'][target_name]['exponentials']
    positive = {key: item['positive'][key] for key in ['point_coordinates', 'point_frobenius', 'point_sha256', 'parameters', 'target_logarithm']}
    negative = {key: item['negative'][key] for key in ['point_coordinates', 'point_frobenius', 'point_sha256', 'target_logarithm']}
    hashes = endpoints['source_sha256']
    original_bases_sha = endpoints['input_sha256']['original_Abel_bases']
    original_jets_sha = endpoints['input_sha256']['source_cubic_jets']
    multiplier = endpoints['target_multiplier']
    assert endpoints['integer_factor'] == 3 and endpoints['family_index'] == 1
    del endpoints, item
    bases, inputs['original_Abel_bases'] = read(args.bases or folder/'data/p41_hecke3_abel_bases_checkpoint.json.gz')
    assert inputs['original_Abel_bases'] == original_bases_sha and bases['source_sha256'] == hashes
    families = [{key: family[key] for key in ['points_1based', 'v_coefficients']} for family in bases['families']]
    del bases
    first, inputs['actual_first_inverse_functions'] = read(args.first_inverses or folder/'data/p41_cm_mixed_formal_height47_checkpoint.json.gz')
    assert first['source_sha256'] == hashes
    first_records = [rec for rec in first['records'] if args.target == 'common' or rec['discriminant'] == -int(args.target)]
    assert len(first_records) == (2 if args.target == 'common' else 1)
    del first
    hessian, inputs['actual_Hecke_correction'] = read(args.hessian or folder/'data/p41_hecke3_hessian47_compact.json.gz')
    assert hessian['source_sha256'] == hashes
    correction = r.from_json(hessian['hecke_correction_matrix'])
    del hessian
    jets, inputs['actual_source_cubic'] = read(args.jets or folder/'data/p41_source_cubic47_full_saved.json.gz')
    assert inputs['actual_source_cubic'] == original_jets_sha
    families_W = []
    for family in families:
        rows = [i-1 for i in family['points_1based']]
        families_W.append([r.from_json([matrix[i] for i in rows]) for matrix in jets['evaluation_coefficients']])
    del jets
    gc.collect()
    sources, source_hashes = load_sources(folder/'data')
    assert hashes == source_hashes
    M = make_model(sources)
    spaces = []
    for W in families_W:
        V2, unused = section_jets(W, sources, M, r)
        spaces.append({1: W, 2: V2})
        del unused
    del sources, families_W
    Kplus, Aplus = r.from_json(positive.pop('point_coordinates')), r.from_json(positive.pop('point_frobenius'))
    Kminus, Aminus = r.from_json(negative.pop('point_coordinates')), r.from_json(negative.pop('point_frobenius'))
    assert point_hash(Kplus, Aplus) == positive['point_sha256']
    assert point_hash(Kminus, Aminus) == negative['point_sha256']
    for point, action in [(Kplus, Aplus), (Kminus, Aminus)]:
        assert r.equal(r.mm(M['A2'], r.conjugate(point)), r.mm(point, action))
    zQ = r.from_json(positive['target_logarithm'])
    assert r.equal(r.neg(zQ), r.from_json(negative['target_logarithm']))
    vs = [r.mm(M['W'], r.from_json(family['v_coefficients'])) for family in families]
    gc.collect()
    try:
        ctypes.CDLL(None).malloc_trim(0)
    except AttributeError:
        pass
    second_coeff, second_proof = principal_inverse(Kplus, Kminus, vs[1], vs[0], M, r,
                                                   random.Random(4104718400+(0 if args.target == 'common' else int(args.target))))
    compact = {key: value for key, value in second_proof.items() if key not in ['product_basis_inverse', 'colon_kernel_block']}
    compact['omitted_rebuildable_matrix_sha256'] = {key: digest(second_proof[key]) for key in ['product_basis_inverse', 'colon_kernel_block']}
    del second_proof, Kplus, Kminus, Aplus, Aminus, M, vs
    gc.collect()

    def raw_norm(coefficient, degree, family, parameters):
        values = [r.mm(v, coefficient) for v in spaces[family][degree]]
        par = r.from_json(parameters)
        t = par[0].T, par[1].T
        value = r.zeros(54, 1)
        for v in reversed(values):
            value = r.add(r.mul(value, t), v)
        assert np.all(r.units(values[0])) and np.all(r.units(value))
        ratios = r.mul(value, r.inverse_values(values[0]))
        out = [1, 0]
        for i in range(54):
            out = pair_mul(out, [int(ratios[0][i, 0]), int(ratios[1][i, 0])])
        assert out[1] == 0
        return out

    def inverse_norm(coefficient, inverse_family, parameters):
        other_family = 1-inverse_family
        a = raw_norm(coefficient, 2, other_family, parameters)
        b = raw_norm(r.from_json(families[inverse_family]['v_coefficients']), 1, other_family, parameters)
        return pair_mul(a, pair_inverse(pair_mul(b, b)))

    records = []
    for first_record in first_records:
        coefficient = r.from_json(first_record['actual_first_inverse_function']['numerator_coefficients'])
        first_norm = inverse_norm(coefficient, 0, positive['parameters'])
        second_norm = inverse_norm(second_coeff, 1, first_record['negative_parameters'])
        delta = pair_mul(first_norm, pair_inverse(second_norm))
        assert delta[1] == 0 and delta[0] % 47**3 == 1
        logarithm = (delta[0]-1) % r.Q
        half = logarithm*pow(2, -1, r.Q) % r.Q
        zP = r.from_json(first_record['first_logarithm'])
        bilinear = r.mm(r.mm(zP, correction), (zQ[0].T, zQ[1].T))
        assert bilinear[1][0, 0] == 0 and int(bilinear[0][0, 0]) % 47**2 == 0
        b = int(bilinear[0][0, 0])
        value = (half+b) % r.Q
        records.append({'discriminant': first_record['discriminant'],
                        'first_formal_point_sha256': first_record['positive_formal_point_sha256'],
                        'negative_first_formal_point_sha256': first_record['negative_formal_point_sha256'],
                        'actual_first_inverse_proof_sha256': digest(first_record['actual_first_inverse_function']),
                        'first_inverse_degree_zero_norm': first_norm, 'second_inverse_degree_zero_norm': second_norm,
                        'double_inverse_unit': delta, 'log_double_inverse_unit': logarithm,
                        'half_log_double_inverse': half, 'actual_Hecke_bilinear_correction': b,
                        'actual_Hecke_local_log': value, 'first_logarithm': first_record['first_logarithm'],
                        'second_logarithm': positive['target_logarithm']})
        print('ACTUAL CM TRANSLATION FORMAL VALUE', args.target, first_record['discriminant'],
              'first', first_norm, 'second', second_norm, 'half', half, 'bilinear', b, 'value', value, flush=True)
    result = {'level': 41, 'auxiliary_prime': 47, 'precision': 4, 'source_sha256': hashes,
              'input_sha256': inputs, 'target_multiplier': multiplier, 'target_name': target_name,
              'generating_source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'actual_second_inverse_function': compact,
              'positive_second_formal_point_sha256': positive['point_sha256'],
              'negative_second_formal_point_sha256': negative['point_sha256'],
              'records': records,
              'status': 'actual Hecke-compatible local Poincare value in the original R141 family0/family1 frames, retaining true first/second inverse functions; not yet a nonformal global-section value'}
    output = args.output or Path('/tmp/p41_cm'+args.target+'_translation_formal_height47_certificate.json.gz')
    sha, size = write_checkpoint(output, result)
    print('ACTUAL CM TRANSLATION FORMAL SAVED', size, sha, 'seconds', round(time.monotonic()-started, 2),
          'peak_MiB', round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024, 2), flush=True)


if __name__ == '__main__':
    main()
