#!/usr/bin/env python3
"""Extract the actual three T2 cubic branches over the fixed first Abel chart.

Only restriction of published exact coefficients is performed.  The source
labels, necklace permutation and every compressed input hash are retained.
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
    parser.add_argument('--output', type=Path, default=Path('/tmp/p41_t2_first_family_cubic47_checkpoint.json.gz'))
    args = parser.parse_args()
    folder = args.script_dir.resolve()
    data = folder/'data'
    sys.path.insert(0, str(folder))
    from p41_formal47_multiply import write_checkpoint
    base, bsha = read(data/'p41_hecke3_formal_height47_compact.json.gz')
    points = base['families'][0]['points_1based']
    original_bases_sha = base['input_sha256']['p41_hecke3_abel_bases_checkpoint.json.gz']
    source_sha = base['source_sha256']
    del base
    parts, psha = read(data/'p41_hecke2_cubic47_parts.json')
    header = parts['header']
    assert header['status'].endswith('PASS')
    perm = header['necklace_transport_1based']
    assert sorted(perm) == list(range(1, 821))
    target_rows = [perm[j-1]-1 for j in points]
    targets = []
    for index, meta in enumerate(parts['parts']):
        part, digest = read(data/meta['file'])
        assert digest == meta['sha256'] and part['target_index_0based'] == index
        target = part['target']
        saved = {k: target[k] for k in ('kernel_x', 'kernel_jets', 'P_jets', 'Q_jets')}
        saved['evaluation_coefficients'] = [[matrix[j] for j in target_rows] for matrix in target['evaluation_coefficients']]
        assert len(saved['evaluation_coefficients']) == 4
        assert all(len(matrix) == 54 for matrix in saved['evaluation_coefficients'])
        targets.append(saved)
        del part, target, saved
        release()
    full, jsha = read(data/'p41_source_cubic47_full_saved.json.gz')
    assert jsha == header['input_sha256']['p41_source_cubic47_checkpoint.json.gz']
    positions = [full['point_indices_1based'].index(j) for j in points]
    jets = {'point_indices_1based': points,
            'evaluation_coefficients': [[matrix[j] for j in positions] for matrix in full['evaluation_coefficients']]}
    del full
    release()
    out = {'level': 41, 'auxiliary_prime': 47, 'precision': 4,
           'source_sha256': source_sha, 'first_family_compact_sha256': bsha,
           'original_abel_bases_sha256': original_bases_sha,
           'target_parts_sha256': psha, 'raw_target_cubic_sha256': parts['original_sha256'],
           'source_cubic_sha256': jsha, 'points_1based': points,
           'source_jets': jets, 'targets': targets,
           'full_fibre_checks': header['status'],
           'cubic_generating_source_sha256': header['generating_source_sha256'],
           'target_input_sha256': header['input_sha256'],
           'generating_source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'status': 'exact restriction of published source54 and actual162 T2-target cubic jets to the first Abel family; no new torsion computation'}
    sha, size = write_checkpoint(args.output, out)
    print('ACTUAL T2 FIRST-FAMILY CUBIC JETS', size, sha,
          'peak_MiB', round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024, 2), flush=True)


if __name__ == '__main__':
    main()
