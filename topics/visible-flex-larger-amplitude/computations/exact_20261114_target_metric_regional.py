#!/usr/bin/env python3
"""Compare full finite-tail metric samples with an explicit target-metric rr rule.

The selected layers use the already defined Gauss-Weingarten completion at
each genuine node. Other layers retain the original nonuniform difference
completion. Both use the same fixed source background, raw nodes, full H,
prefix anchor and width-.01 cut correction. This is a comparison of finite
interpolation rules, not adoption of a new closed field or an exact solution.
"""
import argparse
import json
from pathlib import Path
import sys

import exact_20261114_regional_metric as regional
from exact_20261114_source_knot_rr_probe import TargetLayer

HERE = Path(__file__).resolve().parent


class TargetFirstJetLayer(regional.FirstJetLayer):
    def __init__(self, *args, **kwargs):
        TargetLayer.__init__(self, *args, **kwargs)


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--target-labels', required=True,
                        help='Comma-separated existing layer labels using target-metric rr.')
    options, remaining = parser.parse_known_args()
    target_labels = set(options.target_labels.split(','))
    check = argparse.ArgumentParser(add_help=False)
    check.add_argument('--labels', required=True)
    check.add_argument('--out', type=Path, required=True)
    selection, _ = check.parse_known_args(remaining)
    if not target_labels <= set(selection.labels.split(',')) or '' in target_labels:
        raise ValueError('Every selected target-metric label must be a named layer')
    hashes = {str(path): regional.core.sha(path) for path in (
        Path(__file__), HERE/'exact_20261114_source_knot_rr_probe.py',
        HERE/'exact_20261114_regional_metric.py')}
    argv = sys.argv.copy()
    old_layer = regional.FirstJetLayer
    layers = {}

    def choose_layer(*args, **kwargs):
        label = args[1] if len(args) > 1 else kwargs['label']
        layer = (TargetFirstJetLayer if label in target_labels else old_layer)(*args, **kwargs)
        layers[label] = layer
        return layer

    regional.FirstJetLayer = choose_layer
    sys.argv = [argv[0]] + remaining
    try:
        regional.main()
    finally:
        regional.FirstJetLayer = old_layer
        sys.argv = argv
    result = json.loads(selection.out.read_text())
    result['schema'] = 'fixed-g-target-metric-rr-regional-comparison-v1'
    result['source_sha256_at_start'].update(hashes)
    result['original_argv'] = argv
    result['rr_rules'] = {label: dict(
        rule='Gauss-Weingarten target-metric completion' if label in target_labels
             else 'original nonuniform radial difference completion',
        verified_raw_nodes=len(layer.tail.verified_nodes),
        total_nodes=len(layer.tail.r),
        diagnostics=getattr(layer.tail, 'diag', None)) for label, layer in layers.items()}
    result['definition'] = __doc__
    result['adopted_in_closed_assembly'] = False
    result['limitations'].append(
        'Target-metric rr is an explicitly different finite interpolation rule; '
        'the old field is retained in all previously archived closed outputs.')
    selection.out.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(event='target_metric_rr_complete', out=str(selection.out),
                          selected_labels=sorted(target_labels))), flush=True)


if __name__ == '__main__':
    main()
