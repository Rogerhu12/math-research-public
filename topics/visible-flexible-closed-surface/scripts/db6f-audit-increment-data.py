#!/usr/bin/env python3
"""Stream an increment export and independently audit its exact interfaces.

No IntegratedTail reader or numerical solver is used. Only one gzip block
is held at a time. This proves data/anchor/interface invariants of the
declared finite polynomial map, not its metric or convergence to an ODE.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path
import resource
import numpy as np


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def resolve(name, manifest):
    path = Path(name)
    if path.exists():
        return path
    path = manifest.parent/path.name
    if not path.exists():
        raise FileNotFoundError(name)
    return path


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('manifest', type=Path)
    ap.add_argument('out', type=Path)
    ap.add_argument('--same-checkpoint-reference', type=Path)
    args = ap.parse_args()
    meta = json.loads(args.manifest.read_text())
    assert meta['finished'] is True
    assert meta['status'] == 'finite-C2-increment-integrated-explicit-tail-with-sampled-audit'
    fmt, radial = meta['format'], meta['radialGeometry']
    pm, hm = fmt['planarModes'], fmt['heightModes']
    assert all(type(m) is int for m in pm+hm)
    assert len(set(pm)) == len(pm) and len(set(hm)) == len(hm)
    assert all(m % 3 == 1 for m in pm)
    assert all(m >= 0 and m % 3 == 0 for m in hm)
    C = fmt['coefficientCount']
    assert C == len(pm)+len(hm)
    assert fmt['dtype'] == 'little-endian float64'
    assert len(fmt['columns']) == fmt['stride'] == 3+4*C
    modes = ['planar-exp-i'+str(m)+'theta' for m in pm]
    modes += ['height-cos-'+str(m)+'theta' for m in hm]
    labels = ['r', 'rotational-height-above-cuff-approx']
    for prefix in ['derived-value-approx', 'r-derivative', 'rr-derivative',
                   'previous-span-mid-r-derivative']:
        labels += [prefix+':'+mode for mode in modes]
    labels.append('previous-span-radial-integral-unscaled')
    assert fmt['columns'] == labels
    source_bindings = []
    for name, expected in meta['sourceSHA256'].items():
        source = resolve(name, args.manifest)
        assert sha(source) == expected
        source_bindings.append(dict(file=str(source), sha256=expected))
    checkpoint = resolve(meta['input'], args.manifest)
    assert sha(checkpoint) == meta['inputSHA256']

    total, spans, nodes, shared = Q(0), 0, 0, 0
    last = None
    files = []
    for info in meta['files']:
        path = resolve(info['path'], args.manifest)
        payload = path.read_bytes()
        assert len(payload) == info['bytes'] < 5_000_000
        assert hashlib.sha256(payload).hexdigest() == info['sha256']
        raw = gzip.decompress(payload)
        assert info['columns'] == fmt['stride'] and info['rows'] >= 2
        assert len(raw) == info['rows']*info['columns']*8
        data = np.frombuffer(raw, dtype='<f8').reshape(info['rows'], info['columns'])
        assert np.isfinite(data).all()
        if last is not None:
            assert data[0].tobytes() == last
            shared += 1
        unique = data if last is None else data[1:]
        # The very first row has no preceding span. Every other unique row
        # stores the increment ending at that node in its last column.
        lengths = unique[1:, -1] if last is None else unique[:, -1]
        for value in lengths:
            exact = Q(float(value))
            assert exact > 0
            total += exact
        spans += len(lengths)
        nodes += len(unique)
        last = data[-1].tobytes()
        files.append(dict(file=str(path), sha256=info['sha256'], bytes=len(payload),
                          rows=info['rows'], finite_data=True))
    assert nodes == spans+1 == meta['totalUniqueNodes']
    assert spans == radial['spanCount']
    saved = radial['unscaledSum']
    advertised = Q(int(saved['numerator']))*Q(2)**saved['binaryExponent']
    assert total == advertised
    beta = Q(int(radial['normalization']['numerator']), int(radial['normalization']['denominator']))
    inner, outer = Q(radial['innerAnchor']), Q(radial['outerAnchor'])
    cuff, cut = Q(meta['parameters']['rCuff']), Q(meta['parameters']['rCut'])
    assert 0 < cuff < inner < outer == cut
    assert beta == (outer-inner)/total > 0
    assert inner+beta*total == outer
    reference = None
    if args.same_checkpoint_reference:
        prior = json.loads(args.same_checkpoint_reference.read_text())
        assert meta['inputSHA256'] == prior['inputSHA256']
        assert meta['parameters'] == prior['parameters']
        assert meta['sourceSHA256'] == prior['sourceSHA256']
        assert meta['format'] == prior['format']
        assert radial['innerAnchor'] == prior['radialGeometry']['innerAnchor']
        assert radial['outerAnchor'] == prior['radialGeometry']['outerAnchor']
        reference = dict(file=str(args.same_checkpoint_reference), sha256=sha(args.same_checkpoint_reference),
            identical_checkpoint_parameters_source_and_format=True,
            identical_inner_and_outer_anchors=True,
            settings_different_keys=[key for key in sorted(set(meta['settings']) | set(prior['settings']))
                                     if meta['settings'].get(key) != prior['settings'].get(key)])
    report = dict(status='PASS-exact-increment-and-byte-interface-audit', scope=__doc__,
        manifest=str(args.manifest), manifest_sha256=sha(args.manifest),
        script_sha256=sha(Path(__file__)), nodes=nodes, spans=spans, coefficients=C,
        data_files=files, data_file_count=len(files), byte_identical_interfaces=shared,
        source_bindings=source_bindings, checkpoint_sha256=meta['inputSHA256'],
        every_unique_increment_strictly_positive=True,
        exact_unscaled_sum_matches_manifest=True, exact_beta_matches_anchor_ratio=True,
        exact_outer_anchor_equality=True, cuff_and_cut_domain_verified=True,
        threefold_frequency_conditions_verified=True, same_checkpoint_reference=reference,
        largest_compressed_file_bytes=max(d['bytes'] for d in files),
        peak_process_rss_bytes=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)*1024,
        not_certified=['metric', 'curvature or reach', 'source ODE convergence',
                       'complete closed surface', 'G5 or README completion'])
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({key: report[key] for key in (
        'status', 'nodes', 'spans', 'data_file_count', 'byte_identical_interfaces',
        'exact_outer_anchor_equality', 'largest_compressed_file_bytes', 'peak_process_rss_bytes')}))


if __name__ == '__main__':
    main()
