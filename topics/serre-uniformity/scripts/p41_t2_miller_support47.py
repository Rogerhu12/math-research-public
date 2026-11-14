#!/usr/bin/env python3
"""Locate precisely the nonunit Miller germs on the actual162 T2 first-family discs."""
import argparse
import ctypes
import gc
import gzip
import hashlib
import json
from pathlib import Path
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
    values = [(a % 47, b % 47) for a, b in row]
    a, b = next((a, b) for a, b in values if a or b)
    n = pow((a*a+b*b) % 47, -1, 47)
    u, v = a*n % 47, -b*n % 47
    return tuple(((a*u-b*v) % 47, (a*v+b*u) % 47) for a, b in values)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir', type=Path, required=True)
    parser.add_argument('--jets', type=Path, default=Path('/tmp/p41_t2_first_family_cubic47_checkpoint.json.gz'))
    parser.add_argument('--miller', type=Path, action='append', required=True)
    parser.add_argument('--endpoint', type=Path, action='append', default=[])
    parser.add_argument('--output', type=Path, default=Path('/tmp/p41_t2_miller_support47_checkpoint.json.gz'))
    args = parser.parse_args()
    folder = args.script_dir.resolve()
    sys.path.insert(0, str(folder))
    import numpy as np
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources, make_model
    from p41_hecke3_hessian47 import section_jets
    from p41_cm4_divisor47 import kernel
    from p41_formal47_multiply import write_checkpoint
    data, jsha = read(args.jets)
    source_hashes = data['source_sha256']
    points = data['points_1based']
    W = [r.from_json([row for target in data['targets'] for row in target['evaluation_coefficients'][k]]) for k in range(4)]
    point_keys = [key(row) for row in r.to_json(W[0])]
    labels = [{'label': 'T2_'+str(branch)+'_P'+str(point), 'branch_index_0based': branch,
               'first_family_position_0based': pos, 'source_point_index_1based': point}
              for branch in range(3) for pos, point in enumerate(points)]
    del data
    release()
    markers = {}
    for name, label, field, nested in [
        ('p41_cm3_makdisi47_certificate.json', 'P_minus3', 'coarse_evaluation_coefficients', False),
        ('p41_cm12_hecke47_verified.json.gz', 'P_minus12', 'weight2_evaluation_coefficients', False),
        ('p41_cm7_q2_support47_verified.json.gz', 'P_minus7', 'weight2_evaluation_coefficients', True)]:
        obj, sha = read(folder/'data'/name)
        row = obj[field][0][0] if nested else obj[field][0]
        markers[label] = {'source_file': name, 'source_sha256': sha, 'target_intersections': [labels[i]['label'] for i, v in enumerate(point_keys) if v == key(row)]}
        assert not markers[label]['target_intersections'], markers[label]
        del obj
    sections = {1: [], 2: [], 3: []}
    metadata = {1: [], 2: [], 3: []}
    inputs = {'target_cubic': jsha}

    def add_section(encoded, degree, label):
        sha = hashlib.sha256(json.dumps(encoded, separators=(',', ':')).encode()).hexdigest()
        sections[degree].append(r.from_json(encoded))
        metadata[degree].append({'label': label, 'coefficient_sha256': sha, 'degree': degree})

    initial, isha = read(folder/'data/p41_cm_based_points47_checkpoint.json.gz')
    assert initial['source_sha256'] == source_hashes
    add_section(initial['f_b_coefficients'], 1, 'initial_h_numerator')
    inputs['initial_CM'] = isha
    del initial
    base, bsha = read(folder/'data/p41_t2_cm_abel_base47_checkpoint.json.gz')
    assert base['source_sha256'] == source_hashes
    add_section(base['family']['v_coefficients'], 1, 'new_S_frame')
    inputs['new_S_base'] = bsha
    del base
    for path in args.miller:
        slp, sha = read(path)
        assert slp['source_sha256'] == source_hashes and slp['initial_source_sha256'] == isha
        label = slp['point_label']
        inputs[path.name] = sha
        add_section(slp['negative_quadratic_coefficients'], 2, label+'_negative')
        for index, step in enumerate(slp['steps'], 1):
            encoded = step['principal_section_coefficients']
            assert hashlib.sha256(json.dumps(encoded, separators=(',', ':')).encode()).hexdigest() == step['principal_coefficient_sha256']
            add_section(encoded, step.get('principal_section_degree', 3), label+'_step'+str(index))
        del slp
        release()
    for path in args.endpoint:
        endpoint, sha = read(path)
        assert endpoint['source_sha256'] == source_hashes
        inputs[path.name] = sha
        tr = endpoint['transport']
        for field, degree in [('new_section_coefficients', 2), ('old_section_coefficients', 2), ('v1_coefficients', 1)]:
            add_section(tr[field], degree, path.stem+'_'+field)
        del endpoint
        release()
    sources, hashes = load_sources(folder/'data')
    assert hashes == source_hashes
    M = make_model(sources)
    V2, V3 = section_jets(W, sources, M, r)
    values = {1: W, 2: V2, 3: V3}
    d = sources[1]
    K = r.from_json(kernel(73, d['cusp_rank_columns_1based'], d['cusp_free_columns_1based'], d['canonical_kernel_block']))
    f0 = r.mm(K, r.column(d['canonical_coefficients']))
    assert np.all(r.units(r.mm(W[0], f0)))
    del sources, M, d, K, f0
    release()
    collisions = [[] for _ in labels]
    section_count = 0
    max_known = 0
    for degree in [1, 2, 3]:
        if not sections[degree]:
            continue
        C = r.hcat(*sections[degree])
        germs = [r.mm(v, C) for v in values[degree]]
        units = [r.units(v) for v in germs]
        section_count += len(metadata[degree])
        for column, meta in enumerate(metadata[degree]):
            for point in range(162):
                if units[0][point, column]:
                    continue
                e = next((k for k in range(1, 4) if units[k][point, column]), None)
                max_known = max(max_known, e or 4)
                collisions[point].append({**meta, 'residual_order_from_cubic_anchor': e,
                                          'minimum_required_last_jet': 4*(e or 4)+3})
        del C, germs, units
    records = [{**meta, 'nonunit_sections': hits} for meta, hits in zip(labels, collisions) if hits]
    out = {'level': 41, 'auxiliary_prime': 47, 'precision': 4, 'source_sha256': hashes,
           'input_sha256': inputs, 'all_162_f0_constants_units': True,
           'actual_CM_support_disjointness': markers, 'sections_checked': section_count,
           'nonunit_discs': len(records), 'maximum_anchor_order_lower_bound': max_known,
           'records': records, 'generating_source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'status': 'exact nonunit-disc inventory for the supplied actual Miller prefixes and endpoint sections; complete coefficients remain in their source certificates'}
    sha, size = write_checkpoint(args.output, out)
    print('ACTUAL T2 MILLER SUPPORT', section_count, 'sections', len(records), 'nonunit discs',
          'max_anchor_order', max_known, size, sha, 'peak_MiB', round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024, 2), flush=True)


if __name__ == '__main__':
    main()
