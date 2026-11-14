#!/usr/bin/env python3
"""Independent frozen endpoint-plan identity/node check; no profile or flow evaluation."""
import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import struct

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
BASE_SHA = '89307bf2ca1b191c9a6850227d597325ec3c1923e2b8067a20bea58991f82175'
SOURCE_SHA = '993dc6a180b917132d8284fae6c6366b45dddd883f9c09ab50b2b1dcf87f593b'
INPUT_SHA = '07db124d2da380171b99e6d577255b43d4f5496fbd6d982d5dea1a6df873c2e5'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def node_hash(values):
    return hashlib.sha256(b''.join(struct.pack('<d', value) for value in values)).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--author-plan', type=Path, required=True)
    parser.add_argument('--replay-plan', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    base = HERE/'db6f-tail-critical-increment-export.mjs'
    source = HERE/'db6f-prefix-endpoint-critical-increment-export.mjs'
    assert sha(base) == BASE_SHA and sha(source) == SOURCE_SHA
    a, b = base.read_text(), source.read_text()
    critical_start = 'function criticalLayers(profile){'
    grid_start = 'function makeGrid(profile,rawCell){'
    assert a[a.index(critical_start):a.index(grid_start)] == b[b.index(critical_start):b.index(grid_start)]
    assert a[a.index(grid_start):a.index('const plans=stages.cells.map(cell=>{')] == b[b.index(grid_start):b.index('// Grid proposal only:')]
    boundary = 'const view=new DataView'
    assert b[b.index(boundary):].replace('report.settings.endpointRatio=endpointRatio;\n', '', 1) == a[a.index(boundary):]
    assert args.author_plan.read_bytes() == args.replay_plan.read_bytes()
    plan = json.loads(args.replay_plan.read_text())
    assert plan['status'] == 'numerical-grid-proposal-only'
    assert 'finished' not in plan and 'files' not in plan
    assert plan['scriptSHA256'] == SOURCE_SHA
    assert plan['inputSHA256'] == INPUT_SHA == sha(plan['input'])
    for filename, digest in plan['planningSourceSHA256'].items():
        assert sha(filename) == digest
    rows = plan['gridPlan']
    assert len(rows) == 576
    assert [r['stage'] for r in rows] == list(range(576))
    selected = [r for r in rows if (r['rawCell'], r['rawSegment'], r['rawLeft']) == (0, 7, 0)]
    assert len(selected) == 1 and selected[0]['stage'] == 15
    changed = [r for r in rows if r['nodeAudit']['nodeSHA256'] != r['nodeAudit']['legacyNodeSHA256']]
    assert changed == selected
    for row in rows:
        check = row['nodeAudit']
        assert row['nodes'] == check['nodes']
        assert check['addedNodes'] == check['nodes'] - check['legacyNodes']
        assert check['legacySubset'] is True and check['exactEndpoints'] is True
        assert check['allFinite'] is True and check['strictlyIncreasing'] is True
        assert math.isfinite(check['minStageSpan']) and check['minStageSpan'] > 0
        if row not in selected:
            assert row['endpointLayers'] == [] and check['addedNodes'] == 0
    assert len(plan['endpointNodes']) == 1
    packet = plan['endpointNodes'][0]
    assert packet['stage'] == 15
    old, new = packet['legacyNodes'], packet['nodes']
    assert len(old) == 65 and len(new) == 168
    assert old[0] == new[0] == 0 and old[-1] == new[-1] == 1
    for nodes in (old, new):
        assert all(math.isfinite(x) and 0 <= x <= 1 for x in nodes)
        assert all(Fraction(x) < Fraction(y) for x, y in zip(nodes, nodes[1:]))
    assert set(old) <= set(new)
    audit = selected[0]['nodeAudit']
    assert node_hash(old) == audit['legacyNodeSHA256']
    assert node_hash(new) == audit['nodeSHA256']
    layer = selected[0]['endpointLayers'][0]
    assert layer['initialCurvature'] < .5 and layer['thresholdCurvature'] == 3
    assert layer['searchStart'] == 2**-24 and layer['bisections'] == 45
    lo, hi = layer['finalBracket']
    assert lo <= layer['widthScale'] <= hi
    assert layer['bracketCurvatures'][0] < 3 <= layer['bracketCurvatures'][1]
    assert 1e-10 < layer['widthScale'] < .25 and layer['ratio'] == .025
    old_manifest = TOPIC/'notes/2026-11-09-db6f-tail-int2-flat17-m8-q10-n8-s32-manifest.json'
    old_meta = json.loads(old_manifest.read_text())
    assert canonical(plan['physicalStats']) == canonical(old_meta['physicalStats'])
    source_old = {Path(k).name: v for k, v in old_meta['sourceSHA256'].items()}
    source_new = {Path(k).name: v for k, v in plan['planningSourceSHA256'].items()}
    common_sources = sorted(set(source_old) & set(source_new))
    assert all(source_old[name] == source_new[name] for name in common_sources)
    p, q = plan['parameters'], old_meta['parameters']
    differences = [k for k in sorted(set(p)|set(q))
                   if k not in p or k not in q or canonical(p[k]) != canonical(q[k])]
    expected = ['depth', 'farPadding', 'initialCheckpoint', 'iterationCheckpointFile',
                'maxIterations', 'modes', 'physicalDepth', 'sharedEngines',
                'shootingParts', 'traceFile', 'trialDiagnosticFile', 'trialStatePrefix']
    assert differences == expected
    total = 1 + sum(r['nodes']-1 for r in rows)
    assert total == 21031
    report = dict(status='INDEPENDENT_FROZEN_ENDPOINT_PLAN_CHECK_PASS',
        script_sha256=sha(__file__), source_sha256=SOURCE_SHA, frozen_base_sha256=BASE_SHA,
        author_plan=dict(file=str(args.author_plan), sha256=sha(args.author_plan)),
        replay_plan=dict(file=str(args.replay_plan), sha256=sha(args.replay_plan)),
        independent_actual_plan_run_exit_code=0, replay_byte_identical=True,
        source_stages=len(rows), total_source_nodes=total, changed_source_stage=15,
        unchanged_source_x_hashes=575, selected_old_nodes=len(old), selected_new_nodes=len(new),
        selected_binary_nodes_rehashed=True, selected_exact_fraction_gaps_positive=True,
        selected_legacy_nodes_are_subset=True, numerical_layer_width=layer['widthScale'],
        original_critical_functions_byte_identical=True,
        original_math_after_dyadic_byte_identical_except_metadata=True,
        physical_stats_exactly_equal_to_old_m8=True,
        common_physical_source_hashes={k: source_old[k] for k in common_sources},
        source_parameter_differences=differences, planning_source_hashes=plan['planningSourceSHA256'],
        angular_root_calls=0, RK_calls=0, full_map_exports=0,
        normalized_physical_grid_constructed=False,
        scope='One actual quarter-warm grid proposal only. The replay recomputed finite positive unscaled increments before plan-only exit. Unchanged other-stage source-x hashes do not assert unchanged normalized physical r, integrated coefficients, or a new geometry certificate.')
    with args.out.open('x') as handle:
        json.dump(report, handle, indent=2, allow_nan=False)
        handle.write('\n')
    print(json.dumps(dict(status=report['status'], source_stages=len(rows), total_source_nodes=total,
        output_sha256=sha(args.out), angular_root_calls=0, RK_calls=0)))


if __name__ == '__main__':
    main()
