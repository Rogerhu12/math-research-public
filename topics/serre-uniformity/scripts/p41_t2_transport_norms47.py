#!/usr/bin/env python3
"""Actual CM T2 principal-transport norms on the original first Abel frames.

This evaluates the published numerator and denominator sections at the exact
54 moving points.  A nonunit denominator is reported instead of divided by.
"""
import argparse
import ctypes
import gc
import gzip
import hashlib
import json
from pathlib import Path
import resource
import sys
import time


def read(path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw), hashlib.sha256(raw).hexdigest()


def release():
    gc.collect()
    try:
        ctypes.CDLL(None).malloc_trim(0)
    except AttributeError:
        pass


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir', type=Path, required=True)
    parser.add_argument('--jets', type=Path, default=Path('/tmp/p41_t2_first_family_cubic47_checkpoint.json.gz'))
    parser.add_argument('--output', type=Path, default=Path('/tmp/p41_t2_transport_norms47_checkpoint.json.gz'))
    args = parser.parse_args()
    folder = args.script_dir.resolve()
    sys.path.insert(0, str(folder))
    import numpy as np
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources, make_model
    from p41_hecke3_hessian47 import section_jets
    from p41_cm4_divisor47 import kernel
    from p41_poincare_norms47 import pair_mul, pair_inverse
    from p41_formal47_multiply import write_checkpoint
    start = time.monotonic()
    jets, jsha = read(args.jets)
    points = jets['points_1based']
    source_sha = jets['source_sha256']
    original_bases_sha = jets['original_abel_bases_sha256']
    source_cubic_sha = jets['source_cubic_sha256']
    W = [r.from_json(a) for a in jets['source_jets']['evaluation_coefficients']]
    # f0 units at all T2 target constants are needed for later local norms.
    target0 = [r.from_json(t['evaluation_coefficients'][0]) for t in jets['targets']]
    del jets
    release()
    cm, cmsha = read(folder/'data/p41_cm_formal_endpoints47_checkpoint.json.gz')
    assert cm['source_sha256'] == source_sha
    assert cm['input_sha256']['p41_source_cubic47_checkpoint.json.gz'] == source_cubic_sha
    assert cm['input_sha256']['p41_hecke3_abel_bases_checkpoint.json.gz'] == original_bases_sha
    targets = {}
    for discriminant in [12, 7]:
        target = cm['targets']['x'+str(discriminant)]['targets']['m']['exponentials'][0]
        assert target['family_index'] == 0
        targets[discriminant] = {'parameters': target['parameters'], 'point_sha256': target['point_sha256']}
    del target, cm
    release()
    transports = {}
    input_hashes = {'first_family_cubic': jsha, 'CM_formal_endpoints': cmsha}
    for discriminant in [12, 7]:
        tr, trsha = read(folder/('data/p41_t2_cm'+str(discriminant)+'_formal_transport47_checkpoint.json.gz'))
        assert tr['source_sha256'] == source_sha
        assert tr['class_name'] == 'x'+str(discriminant)
        transports[discriminant] = tr['transport']
        input_hashes['T2_CM'+str(discriminant)+'_transport'] = trsha
        del tr
        release()
    sources, hashes = load_sources(folder/'data')
    M = make_model(sources)
    assert hashes == source_sha
    assert r.equal(W[0], r.rows(M['W'], [i-1 for i in points]))
    V2, V3 = section_jets(W, sources, M, r)
    assert r.equal(V3[0], r.rows(M['V3'], [i-1 for i in points]))
    d = sources[1]
    K = r.from_json(kernel(73, d['cusp_rank_columns_1based'], d['cusp_free_columns_1based'], d['canonical_kernel_block']))
    fc = r.mm(K, r.column(d['canonical_coefficients']))
    target_f0_nonunits = []
    for branch, values in enumerate(target0):
        units = r.units(r.mm(values, fc))[:, 0]
        target_f0_nonunits.extend({'branch_index_0based': branch, 'point_index_1based': points[i]} for i in range(54) if not units[i])
    assert not target_f0_nonunits, target_f0_nonunits
    A3 = M['A3']
    del target0, sources, M, W, V2, d, K, fc
    release()

    def product(values):
        assert np.all(r.units(values))
        result = [1, 0]
        for i in range(54):
            result = pair_mul(result, [int(values[0][i, 0]), int(values[1][i, 0])])
        return result

    def logarithm(a):
        assert a % 47 == 1
        z = (a-1) % r.Q
        return (z-z*z*pow(2, -1, r.Q)+z*z*z*pow(3, -1, r.Q)) % r.Q

    records = []
    for discriminant in [12, 7]:
        record = targets[discriminant]
        parameters = r.from_json(record['parameters'])
        t = parameters[0].T, parameters[1].T
        assert all(np.all(a % 47 == 0) for a in t)
        shifted = r.zeros(54, 325)
        for a in reversed(V3):
            shifted = r.add(r.mul(shifted, t), a)
        section_norms = {}
        values_saved = {}
        for name in ['numerator', 'denominator']:
            coefficient = r.from_json(transports[discriminant][name+'_coefficients'])
            assert r.equal(r.mm(A3, r.conjugate(coefficient)), coefficient)
            original = r.mm(V3[0], coefficient)
            moving = r.mm(shifted, coefficient)
            bad = [points[i] for i in range(54) if not r.units(original)[i, 0]]
            assert not bad, (discriminant, name, 'nonunit values require local cancellation', bad)
            ratio = pair_mul(product(moving), pair_inverse(product(original)))
            assert ratio[1] == 0 and ratio[0] % 47 == 1
            section_norms[name] = ratio[0]
            values_saved[name] = {'constant_values': r.to_json(original), 'moving_values': r.to_json(moving)}
        norm = section_norms['numerator']*pow(section_norms['denominator'], -1, r.Q) % r.Q
        log = logarithm(norm)
        assert log == (logarithm(section_norms['numerator'])-logarithm(section_norms['denominator'])) % r.Q
        records.append({'discriminant': -discriminant, 'family_index': 0,
                        'first_formal_point_sha256': record['point_sha256'],
                        'parameters': record['parameters'], 'actual_section_norms': section_norms,
                        'actual_rho_T_norm': norm, 'log_actual_rho_T_norm': log,
                        'section_values': values_saved, 'all_108_section_values_units': True,
                        'formula': 'rho_T[A0(mC)]=product_i rho_T(P_i(t_i))/rho_T(P_i(0))',
                        'principal_divisor': 'T2(A_S(mC))-A_S(T2mC)'})
        print('ACTUAL T2 TRANSPORT NORM', discriminant, 'rho', norm, 'log', log, flush=True)
    out = {'level': 41, 'auxiliary_prime': 47, 'precision': 4,
           'source_sha256': hashes, 'input_sha256': input_hashes,
           'first_family_points_1based': points, 'all_162_T2_target_f0_values_units': True,
           'records': records, 'generating_source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'status': 'actual CM T2 principal-transport norms on both first formal Abel frames; all denominators units; no complete global height claimed'}
    sha, size = write_checkpoint(args.output, out)
    print('ACTUAL T2 TRANSPORT NORMS SAVED', size, sha, 'seconds', round(time.monotonic()-start, 2),
          'peak_MiB', round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024, 2), flush=True)


if __name__ == '__main__':
    main()
