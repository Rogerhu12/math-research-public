#!/usr/bin/env python3
"""Actual signed3mD_b and signed3mD_P endpoints in the fixed second Abel family."""
import argparse
import gc
import gzip
import hashlib
import json
from pathlib import Path
import sys


def read(path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw), hashlib.sha256(raw).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir', type=Path, required=True)
    parser.add_argument('--bases', type=Path, default=Path('/tmp/p41_hecke3_abel_bases_checkpoint.json.gz'))
    parser.add_argument('--jets', type=Path)
    parser.add_argument('--output', type=Path, default=Path('/tmp/p41_translation_formal_endpoints47_checkpoint.json.gz'))
    args = parser.parse_args()
    folder = args.script_dir.resolve()
    sys.path.insert(0, str(folder))
    import numpy as np
    import p41_r2_matrix as r
    from p41_cm_height_calibration47 import matmul
    from p41_group_operations47 import load_sources, make_model
    from p41_cm4_divisor47 import kernel
    from p41_formal47_exponential import construct_point
    from p41_formal47_multiply import write_checkpoint, point_hash
    cm, cm_sha = read(folder/'data/p41_cm_formal_endpoints47_checkpoint.json.gz')
    basis = cm['T3_power_basis_matrix']
    inverse = cm['inverse_T3_power_basis_matrix']
    cm_source = cm['source_sha256']
    input_hashes = cm['input_sha256']
    m = cm['target_multiplier']
    assert m % 47 == 9
    old_logs = {name: r.from_json(cm['targets'][name]['log_of_class']) for name in ('x12', 'x7')}
    del cm
    small, small_sha = read(folder/'data/p41_small_hecke_cm_transport47_certificate.json.gz')
    assert input_hashes['p41_small_hecke_cm_transport47_certificate.json.gz'] == small_sha
    polynomials = {}
    for name in ('x12', 'x7', 'kappa_2', 'D12_2', 'D7_2'):
        co = small['coordinates'][name]
        coefficients = [v*pow(co['denominator'], -1, r.Q) % r.Q for v in co['numerators']]
        field_coordinates = matmul([coefficients], small['basis_matrix_mod47_4'], r.Q)[0]
        polynomial = matmul([field_coordinates], inverse, r.Q)[0]
        assert matmul([polynomial], basis, r.Q)[0] == field_coordinates
        polynomials[name] = polynomial
    del small, basis, inverse
    log, log_sha = read(folder/'data/p41_formal47_log_compact.json.gz')
    assert input_hashes['p41_formal47_log_compact.json.gz'] == log_sha
    assert log['formal_input_multiplier'] == m and log['formal_input_sign'] == 1
    lb = r.from_json(log['log_of_B_minus4'])
    del log
    hecke, hecke_sha = read(folder/'data/p41_hecke47_compact.json.gz')
    assert input_hashes['p41_hecke47_compact.json.gz'] == hecke_sha
    T2 = r.from_json(hecke['operators']['2']['canonical_operator'])
    T3 = r.from_json(hecke['operators']['3']['canonical_operator'])
    del hecke

    def scale(A, value):
        return tuple(a*(int(value) % r.Q) % r.Q for a in A)

    def logarithm(poly):
        result = r.zeros(1, 54)
        for c in reversed(poly):
            result = r.add(r.mm(result, T3), scale(lb, c))
        return result

    logs = {name: logarithm(poly) for name, poly in polynomials.items()}
    for name in ('x12', 'x7'):
        assert r.equal(logs[name], old_logs[name])
    for name, dname in [('x12', 'D12_2'), ('x7', 'D7_2')]:
        expected = r.sub(r.add(scale(r.mm(logs[name], T2), 27), scale(logs[name], 4)), logs['kappa_2'])
        assert r.equal(expected, logs[dname])
    targets = {'three_m_D_b': scale(logs['kappa_2'], -3*m),
               'three_m_D12': scale(logs['D12_2'], 3*m),
               'three_m_D7': scale(logs['D7_2'], 3*m)}
    del old_logs, lb, T2, T3
    base, base_sha = read(args.bases)
    assert base_sha == input_hashes['p41_hecke3_abel_bases_checkpoint.json.gz']
    assert base['source_sha256'] == cm_source
    record = base['families'][1]
    labels = record['points_1based']
    del base
    full_jets, jets_sha = read(args.jets or folder/'data/p41_source_cubic47_full_saved.json.gz')
    assert jets_sha == input_hashes['p41_source_cubic47_checkpoint.json.gz']
    positions = [full_jets['point_indices_1based'].index(label) for label in labels]
    jets = {'point_indices_1based': labels,
            'evaluation_coefficients': [[matrix[j] for j in positions] for matrix in full_jets['evaluation_coefficients']]}
    del full_jets
    gc.collect()
    sources, hashes = load_sources(folder/'data')
    assert hashes == cm_source
    M = make_model(sources)
    divs = sources[1]
    del sources
    gc.collect()
    AK = r.from_json(divs['canonical_frobenius_matrix'])
    results = {}
    for name, target in targets.items():
        assert r.equal(r.mm(target, AK), r.conjugate(target))
        assert all(np.all(a % 47 == 0) for a in target)
        witnesses = {}
        for sign, label in [(1, 'positive'), (-1, 'negative')]:
            signed = scale(target, sign)
            point, F, witness = construct_point(signed, record, jets, divs, M, r, kernel)
            witness['point_sha256'] = point_hash(point, F)
            witness['family_index'] = 1
            witnesses[label] = witness
            print('COMMON TRANSLATION ACTUAL ENDPOINT', name, label, witness['point_sha256'], flush=True)
        results[name] = {'logarithm': r.to_json(target), 'exponentials': witnesses}
    output = {'level': 41, 'auxiliary_prime': 47, 'precision': 4, 'source_sha256': hashes,
              'input_sha256': {'CM_formal_endpoints': cm_sha, 'small_Hecke_coordinates': small_sha,
                               'formal_B_log': log_sha, 'compact_Hecke': hecke_sha,
                               'original_Abel_bases': base_sha, 'source_cubic_jets': jets_sha},
              'target_multiplier': m, 'integer_factor': 3, 'family_index': 1,
              'T3_polynomials_ascending': polynomials, 'targets': results,
              'class_relations': {'D_b': '-kappa_2', 'D12': '(27*T2+4)*x12-kappa_2', 'D7': '(27*T2+4)*x7-kappa_2'},
              'formality_reason': 'm=#J(F47) kills the actual rational reduction; R162 integer torsion-cleared identities identify these logarithms; the formal logarithm is injective',
              'generating_source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'status': 'all six signed3mD_b/signed3mD_P actual full Makdisi ideals in fixed family1; no principal transport or height inferred from logarithms alone'}
    digest, size = write_checkpoint(args.output, output)
    print('COMMON TRANSLATION FORMAL ENDPOINTS SAVED', size, digest, flush=True)


if __name__ == '__main__':
    main()
