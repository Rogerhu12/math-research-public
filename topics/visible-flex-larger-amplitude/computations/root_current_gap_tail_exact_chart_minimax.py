#!/usr/bin/env python3
"""Run the unchanged current full-gap/tail model with its exact-order reader.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Only the explicitly verified outer-entry identity bridge is installed.
All nineteen arrays, all five row families, full-core objective/tail rows,
complete finite-row replay and original solver remain unchanged.
"""
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
PINS = {
    'root_current_complete_core_gap_tail_minimax_v2.py':
        '0154e56b27907d2467a963ec0eb02b5e79528b25982ae7ec38ad40dc761ac6b9',
    'root_geometry_anchor_current_reader.py':
        'b69abdc1f615a9d96b65fb187f2e87831bf975f5b2752303db4c10c37f9c3b84',
    'root_geometry_current_exact_chart_reader.py':
        '167de07932c93a60fda5f5a1c51d32933027f108fdb73171f908db30228224cf',
    'root_actual_current_geometry_exact_chart_order.py':
        '2a5ddc83127566cdf88d3709ec328235379b5083b6c069d51927b3defc0eb1a2',
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    for name, expected in PINS.items():
        if sha(HERE / name) != expected:
            raise ValueError('A frozen actual current model dependency changed: ' + name)
    import root_geometry_anchor_current_reader as original_reader
    import root_geometry_current_exact_chart_reader as exact_reader
    import root_current_complete_core_gap_tail_minimax_v2 as model
    previous = original_reader.verify
    if previous is not exact_reader.FROZEN_VERIFY:
        raise ValueError('Install the bridge only over the original unmodified reader function')
    original_reader.verify = exact_reader.verify
    try:
        model.main()
    finally:
        original_reader.verify = previous
    preparation_only = '--prepare-source-only' in sys.argv
    flag = '--prepare-source-only' if preparation_only else '--out'
    path = Path(sys.argv[sys.argv.index(flag) + 1])
    value = json.loads(path.read_text())
    record = dict(source_sha256=sha(__file__), pinned_sources=PINS,
        exact_order_entry_and_reader_explicit=True,
        original_gap_tail_objective_constraints_and_full_row_replay_unchanged=True,
        original_all_nineteen_field_samples_unchanged=True,
        no_new_geometry_field_or_BVP_started=True)
    if not preparation_only:
        bridge = value['actual_anchor_current_geometry_bridge']
        actual = json.loads(Path(bridge['path']).read_text())
        if (actual['source_sha256'] != PINS['root_geometry_current_exact_chart_reader.py']
                or not actual['all_identity_gates']):
            raise ValueError('The actual completed current reader provenance changed')
        bridge['source_sha256'] = actual['source_sha256']
        bridge['original_reader_source_sha256'] = PINS['root_geometry_anchor_current_reader.py']
        bridge['actual_exact_chart_order_reader_adapter'] = actual['actual_exact_chart_order_reader_adapter']
        known = {r['path'] for r in value['inputs']}
        for proof in actual['actual_exact_chart_order_reader_adapter']['actual_field_proofs']:
            for key in ('proof', 'original_failed_report', 'original_failed_resource'):
                if proof[key] not in known:
                    value['inputs'].append(dict(path=proof[key], sha256=sha(proof[key])))
                    known.add(proof[key])
        for prediction in value['predictions']:
            if prediction.get('success') and not prediction['predicted_max_twice_norm'] > 0:
                raise ArithmeticError('A positive size model is required before reporting a gap/size ratio')
        record['actual_reader_sha256'] = sha(bridge['path'])
        record['all_successful_predicted_sizes_strictly_positive'] = True
    value['current_exact_chart_reader_frontend'] = record
    temporary = path.with_name(path.name + '.current-exact-reader.tmp')
    temporary.write_text(json.dumps(value, indent=2) + '\n')
    temporary.replace(path)
    print(json.dumps(dict(event='current_exact_reader_model_complete', path=str(path),
        sha256=sha(path), source_preparation_only=preparation_only)), flush=True)


if __name__ == '__main__':
    main()
