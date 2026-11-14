#!/usr/bin/env python3
"""Choose a genuine CM second Abel chart disjoint from first-frame T2 data.

Each of the three published actual target branches is decoded separately.
Only normalized projective keys are retained during support selection.
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


def read(path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw), hashlib.sha256(raw).hexdigest()


def release():
    gc.collect()
    try:
        ctypes.CDLL(None).malloc_trim(0)
    except AttributeError:
        pass


def key(row):
    vals = [(int(a) % 47, int(b) % 47) for a, b in row]
    a, b = next((a, b) for a, b in vals if a or b)
    inverse = pow((a*a+b*b) % 47, -1, 47)
    u, v = a*inverse % 47, -b*inverse % 47
    return bytes(c for x, y in vals for c in ((x*u-y*v) % 47, (x*v+y*u) % 47))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir', type=Path, required=True)
    parser.add_argument('--data-dir', type=Path, help='optional immutable copy during concurrent ordinary rebase')
    parser.add_argument('--selection', type=Path, default=Path('/tmp/p41_t2_cm_abel_select47_checkpoint.json.gz'))
    parser.add_argument('--restricted', type=Path, default=Path('/tmp/p41_t2_cm_restricted_cubic47_checkpoint.json.gz'))
    args = parser.parse_args()
    folder = args.script_dir.resolve()
    data = args.data_dir.resolve() if args.data_dir else folder/'data'
    sys.path.insert(0, str(folder))
    import p41_r2_matrix as r
    from p41_cm4_divisor47 import kernel
    from p41_formal47_multiply import write_checkpoint
    source_names = ['p41_makdisi47_certificate.json.gz', 'p41_cusp_divisors47_certificate.json.gz',
                    'p41_cm4_divisor47_certificate.json', 'p41_group47_checkpoint.json.gz']
    hashes = {name: hashlib.sha256((data/name).read_bytes()).hexdigest() for name in source_names}
    model, model_sha = read(data/source_names[0])
    W = r.from_json(model['evaluation_matrix'])
    A1 = r.from_json(model['frobenius_basis_matrix'])
    keys = [key(row) for row in model['evaluation_matrix']]
    tau = [j-1 for j in model['frobenius_permutation_1based']]
    del model
    assert len(set(keys)) == 820
    assert all(tau[tau[j]] == j for j in range(820))
    assert r.equal(r.conjugate(r.mm(W, A1)), r.rows(W, tau))
    divisors, divisor_sha = read(data/source_names[1])
    K = r.from_json(kernel(73, divisors['cusp_rank_columns_1based'],
                           divisors['cusp_free_columns_1based'], divisors['canonical_kernel_block']))
    Omega = r.mm(W, K)
    del divisors, W, K
    base, base_sha = read(data/'p41_hecke3_formal_height47_compact.json.gz')
    assert base['source_sha256'] == hashes
    first = [j-1 for j in base['families'][0]['points_1based']]
    original_base_sha = base['input_sha256']['p41_hecke3_abel_bases_checkpoint.json.gz']
    del base
    parts, parts_sha = read(data/'p41_hecke2_cubic47_parts.json')
    header = parts['header']
    assert header['status'].endswith('PASS')
    assert header['input_sha256'][source_names[0]] == model_sha
    permutation = [j-1 for j in header['necklace_transport_1based']]
    assert sorted(permutation) == list(range(820))
    target_keys = []
    target_frobenius_keys = []
    for index, meta in enumerate(parts['parts']):
        part, digest = read(data/meta['file'])
        assert digest == meta['sha256'] and part['target_index_0based'] == index
        rows = part['target']['evaluation_coefficients'][0]
        target_keys.append([key(rows[permutation[j]]) for j in range(820)])
        V = r.rows(r.from_json(rows), permutation)
        target_frobenius_keys.append([key(row) for row in r.to_json(r.conjugate(r.mm(V, A1)))])
        del rows, part, V
        release()
    lookup = {value: j for j, value in enumerate(keys)}
    matches = [[lookup.get(value, -1) for value in branch] for branch in target_keys]
    footprints = [{keys[j], *(branch[j] for branch in target_keys)} for j in range(820)]
    assert all({keys[tau[j]], *(branch[j] for branch in target_frobenius_keys)} == footprints[tau[j]] for j in range(820))
    first_support = {keys[j] for j in first}
    first_T2 = {branch[j] for branch in target_keys for j in first}
    orbits = [[j, tau[j]] for j in range(820) if j < tau[j]]
    seed = 4104717901
    rng = random.Random(seed)
    rng.shuffle(orbits)
    selected, used = [], set()
    rejected = {'internal_collision': 0, 'first_support': 0, 'first_T2': 0, 'rank': 0}
    for orbit in orbits:
        support = set().union(*(footprints[j] for j in orbit))
        if len(support) != 8 or support & used:
            rejected['internal_collision'] += 1
            continue
        if support & first_support:
            rejected['first_support'] += 1
            continue
        if {keys[j] for j in orbit} & first_T2:
            rejected['first_T2'] += 1
            continue
        proposed = selected+orbit
        if len(r.rank_pivots(r.rows(Omega, proposed))[0]) != len(proposed):
            rejected['rank'] += 1
            continue
        selected, used = proposed, used | support
        if len(selected) == 54:
            break
    assert len(selected) == 54 and len(used) == 216, (len(selected), rejected)
    assert {tau[j] for j in selected} == set(selected)
    second_support = {keys[j] for j in selected}
    second_T2 = {branch[j] for branch in target_keys for j in selected}
    disjoint = {'S_intersect_first': len(second_support & first_support),
                'T2S_intersect_first': len(second_T2 & first_support),
                'S_intersect_T2first': len(second_support & first_T2),
                'S_intersect_T2S': len(second_support & second_T2)}
    assert not any(disjoint.values())
    O = r.rows(Omega, selected)
    Oi = r.inverse_matrix(O)
    assert r.equal(r.mm(O, Oi), r.eye(54))
    source_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    out = {'level': 41, 'auxiliary_prime': 47, 'precision': 4, 'source_sha256': hashes,
           'target_parts_sha256': parts_sha, 'raw_target_cubic_sha256': parts['original_sha256'],
           'raw_hecke_sha256': header['input_sha256']['p41_hecke47_checkpoint.json.gz'],
           'first_family_compact_sha256': base_sha, 'original_abel_bases_sha256': original_base_sha,
           'first_family_points_1based': [j+1 for j in first], 'selection_seed': seed,
           'points_1based': [j+1 for j in selected], 'all_216_supports_distinct_mod47': True,
           'disjoint_support_counts': disjoint, 'rejected_orbit_counts': rejected,
           'source_frobenius_permutation_1based': [selected.index(tau[j])+1 for j in selected],
           'target_to_source_index_1based': [[j+1 if j >= 0 else 0 for j in branch] for branch in matches],
           'canonical_evaluation_inverse': r.to_json(Oi), 'generating_source_sha256': source_sha,
           'status': 'actual Frobenius-stable54-point CM second Abel chart;216 distinct source/T2 supports; S,T2S avoid first and S avoids T2first'}
    selection_sha, size = write_checkpoint(args.selection, out)
    print('CM T2 CHART SELECTED', size, selection_sha, disjoint, flush=True)
    del Omega, O, Oi, footprints, target_keys, target_frobenius_keys, A1, keys, matches, lookup, used
    release()
    target_rows = [permutation[j] for j in selected]
    targets = []
    for index, meta in enumerate(parts['parts']):
        part, digest = read(data/meta['file'])
        assert digest == meta['sha256'] and part['target_index_0based'] == index
        target = part['target']
        saved = {k: target[k] for k in ('kernel_x', 'kernel_jets', 'P_jets', 'Q_jets')}
        saved['evaluation_coefficients'] = [[matrix[j] for j in target_rows] for matrix in target['evaluation_coefficients']]
        targets.append(saved)
        del part, target, saved
        release()
    full, jet_sha = read(data/'p41_source_cubic47_full_saved.json.gz')
    assert jet_sha == header['input_sha256']['p41_source_cubic47_checkpoint.json.gz']
    positions = [full['point_indices_1based'].index(j+1) for j in selected]
    jets = {'point_indices_1based': [j+1 for j in selected],
            'evaluation_coefficients': [[matrix[j] for j in positions] for matrix in full['evaluation_coefficients']]}
    del full
    release()
    compact = {'level': 41, 'auxiliary_prime': 47, 'precision': 4,
               'selection_sha256': selection_sha, 'target_parts_sha256': parts_sha,
               'raw_target_cubic_sha256': parts['original_sha256'], 'source_cubic_sha256': jet_sha,
               'points_1based': jets['point_indices_1based'], 'source_jets': jets, 'targets': targets,
               'full_fibre_checks': header['status'], 'cubic_generating_source_sha256': header['generating_source_sha256'],
               'target_input_sha256': header['input_sha256'], 'prefix_generation_history': header.get('prefix_generation_history', []),
               'generating_source_sha256': source_sha,
               'status': 'all54 CM second-chart source and162 actual T2-target cubic jets retained exactly'}
    compact_sha, compact_size = write_checkpoint(args.restricted, compact)
    print('CM T2 CUBIC COMPACT SAVED', compact_size, compact_sha,
          'peak_MiB', round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024, 2), flush=True)


if __name__ == '__main__':
    main()
