#!/usr/bin/env python3
"""Read-only invariants for the M15-quarter background endpoint-grid plan.

No background factory, angular root, RK, or numerical surface is evaluated.
This checks the closed source-x proposal and frozen code/input identities.
"""
import argparse
import gzip
import hashlib
import json
import math
import struct
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
NOTES = TOPIC / 'notes'
STEM = NOTES / '2026-11-09-db6f-prefix-endpoint-grid-m15-quarter-p8-r0025'


def read(path):
    path = Path(path)
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def bind(path):
    path = Path(path).resolve()
    return dict(path=str(path), bytes=path.stat().st_size,
                sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def node_hash(nodes):
    return hashlib.sha256(struct.pack('<'+'d'*len(nodes), *nodes)).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    plan_path = Path(str(STEM)+'-grid-plan.json')
    plan = read(plan_path)
    script = HERE/'db6f-prefix-endpoint-critical-increment-export.mjs'
    old_script = HERE/'db6f-tail-critical-increment-export.mjs'
    if bind(script)['sha256'] != plan['scriptSHA256']:
        raise ValueError('Plan producer changed')
    if bind(old_script)['sha256'] != '89307bf2ca1b191c9a6850227d597325ec3c1923e2b8067a20bea58991f82175':
        raise ValueError('Frozen original exporter changed')
    old_source, new_source = old_script.read_text(), script.read_text()
    old_grid = old_source[old_source.index('function criticalLayers('):old_source.index('const plans=')]
    new_grid = new_source[new_source.index('function criticalLayers('):new_source.index('// Grid proposal only:')]
    if old_grid != new_grid:
        raise ValueError('Original critical/uniform/Chebyshev node functions changed')
    old_map = old_source[old_source.index('const view=new DataView'):]
    new_map = new_source[new_source.index('const view=new DataView'):]
    if new_map.replace('report.settings.endpointRatio=endpointRatio;\n', '') != old_map:
        raise ValueError('Post-plan map/integration/Fourier code changed')
    for name, digest in plan['planningSourceSHA256'].items():
        if bind(name)['sha256'] != digest:
            raise ValueError('Planning source changed: '+name)
    input_path = Path(plan['input'])
    if bind(input_path)['sha256'] != plan['inputSHA256']:
        raise ValueError('Input response identity changed')
    response = read(input_path)
    p = response['response']['checkpoint']['parameters']
    if p != plan['parameters']:
        raise ValueError('Plan parameter record differs from real quarter input')
    if p['modes'] != 15 or p['shootingParts'] != 8 or p['steps'] != 32:
        raise ValueError('Unexpected quarter numerical layout')
    old_plan_path = NOTES/'2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-grid-plan.json'
    old_plan = read(old_plan_path)
    if plan['physicalStats'] != old_plan['physicalStats']:
        raise ValueError('Frozen background construction scalars differ from M12')
    old_cp_path = NOTES/'2026-11-09-db6f-prefix-flat-v17v18-fixed-m12-d12-p4-s64_tail_0018.json.gz'
    old_p = read(old_cp_path)['response']['checkpoint']['parameters']
    physical_keys = ['rCut', 'wCut', 'width', 'curvatureBound', 'delta0', 'R', 'a',
        'etaPower', 'etaRatioAtN0', 'orientation', 'prefixR', 'prefixEnd',
        'prefixReturnStart', 'protectCell', 'calibrationSteps', 'warpSteps',
        'quadratureTolerance', 'slopeCap', 'capTransition', 'capMode',
        'cuspAwareQuadrature', 'valleyControls', 'pulseCaps', 'valleyCaps',
        'warpWeightLevels', 'rCuff', 'epsilonScale']
    for key in physical_keys:
        if (key in p) != (key in old_p) or p.get(key) != old_p.get(key):
            raise ValueError('Physical background parameter differs: '+key)
    rows = plan['gridPlan']
    if len(rows) != response['response']['checkpoint']['rawNode'][plan['settings']['depth']]:
        raise ValueError('Stage plan does not match the original staged checkpoint')
    selected = [row for row in rows if row['rawCell'] == 0 and row['rawSegment'] == 7 and row['rawLeft'] == 0]
    if len(selected) != 1:
        raise ValueError('Restoration label is not unique')
    chosen = selected[0]
    changed = [row for row in rows if row['nodeAudit']['legacyNodeSHA256'] != row['nodeAudit']['nodeSHA256']]
    if changed != selected:
        raise ValueError('A different source-x stage changed')
    for row in rows:
        audit = row['nodeAudit']
        if not all(audit[key] is True for key in ['legacySubset', 'exactEndpoints', 'allFinite', 'strictlyIncreasing']):
            raise ValueError('Producer reported a failed source-grid invariant')
        if audit['nodes'] != row['nodes'] or audit['nodes']-audit['legacyNodes'] != audit['addedNodes']:
            raise ValueError('Node counts disagree')
        if not math.isfinite(audit['minStageSpan']) or audit['minStageSpan'] <= 0:
            raise ValueError('Invalid source-x span')
    if len(plan['endpointNodes']) != 1 or plan['endpointNodes'][0]['stage'] != chosen['stage']:
        raise ValueError('Missing complete selected-stage node packet')
    nodes = plan['endpointNodes'][0]['nodes']
    legacy = plan['endpointNodes'][0]['legacyNodes']
    if not (nodes[0] == legacy[0] == 0 and nodes[-1] == legacy[-1] == 1):
        raise ValueError('Endpoints changed')
    if not all(math.isfinite(x) and 0 <= x <= 1 for x in nodes+legacy):
        raise ValueError('Nonfinite/outside selected-stage node')
    if not all(a < b for a, b in zip(nodes, nodes[1:])) or not set(legacy).issubset(nodes):
        raise ValueError('Selected-stage order or exact legacy subset failed')
    audit = chosen['nodeAudit']
    if node_hash(nodes) != audit['nodeSHA256'] or node_hash(legacy) != audit['legacyNodeSHA256']:
        raise ValueError('Independent little-endian node hash differs')
    layer = chosen['endpointLayers']
    if len(layer) != 1 or layer[0]['x'] != 0 or layer[0]['ratio'] != .025:
        raise ValueError('Unexpected endpoint policy')
    layer = layer[0]
    if not (0 < layer['widthScale'] < .25 and layer['initialCurvature'] < .5
            and layer['bracketCurvatures'][0] < 3 <= layer['bracketCurvatures'][1]):
        raise ValueError('Numerical threshold bracket is not recorded consistently')
    if any(STEM.parent.glob(STEM.name+'-manifest.json')) or any(STEM.parent.glob(STEM.name+'*.f64.gz')) or Path(str(STEM)+'-collar.json').exists():
        raise ValueError('This proposal unexpectedly has geometric export files')
    inputs = {Path(__file__).resolve(), plan_path, script, old_script, input_path, old_plan_path, old_cp_path}
    result = dict(status='PASS-BACKGROUND-SOURCE-GRID-PLAN-ONLY', scope=__doc__,
        plan_process_observed_exit_code=0, angular_root_calls=0, RK_calls=0,
        full_export_calls=0, geometry_manifest_created=False,
        legacy_grid_functions_byte_identical=True,
        post_plan_map_code_identical_except_endpoint_setting=True,
        physical_parameter_keys_identical_to_M12=len(physical_keys),
        background_construction_stats_bitwise_equal_to_M12=True,
        planned_stages=len(rows), planned_unique_nodes=1+sum(row['nodes']-1 for row in rows),
        changed_source_x_stages=[row['stage'] for row in changed],
        endpoint_label={key:chosen[key] for key in ['stage', 'rawCell', 'rawSegment', 'rawLeft', 'rawRight']},
        endpoint_width_scale=layer['widthScale'], endpoint_ratio=layer['ratio'],
        old_selected_nodes=len(legacy), new_selected_nodes=len(nodes),
        added_selected_nodes=len(nodes)-len(legacy),
        independent_selected_node_sha256=node_hash(nodes),
        physical_map_scope='Only source-x proposals are compared. New subdivision may change the exact global beta via numerical local integrals; post-plan exact-r normalization and any actual finite map have not run.',
        bound_files=[bind(path) for path in sorted(inputs)])
    with args.output.open('x') as handle:
        json.dump(result, handle, indent=2, allow_nan=False)
        handle.write('\n')
    print(json.dumps({key:result[key] for key in ['status', 'planned_stages', 'planned_unique_nodes',
        'changed_source_x_stages', 'endpoint_width_scale', 'added_selected_nodes', 'full_export_calls']}))


if __name__ == '__main__':
    main()
