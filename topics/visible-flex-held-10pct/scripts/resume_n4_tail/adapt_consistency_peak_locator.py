#!/usr/bin/env python3
"""Adapt an exact full replay plus named peak readout to the original candidate API.

The largestResidual list contains one proven globally maximizing row, not a
newly generated complete ranking. No state or solve is synthesized or changed.
"""
import argparse
import json
from pathlib import Path
import struct
import sys
from record_fixed_actual import load, scalar_tree, sha


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('input', 'comparison', 'comparison-source', 'peak', 'peak-resource', 'out'):
        p.add_argument('--' + key, type=Path, required=True)
    a = p.parse_args()
    native, cmp, peak = load(a.input), load(a.comparison), load(a.peak)
    resource = load(a.peak_resource)
    if not native['response'].get('failed') or native['config']['solveTolerance'] != 2e-9:
        raise ValueError('An original complete failed state is required')
    if not cmp['input_sha256'] == peak['input_sha256'] == sha(a.input):
        raise ValueError('Inputs differ')
    if not (cmp['normalized_variational_residual'] == peak['expectedFullResidual'] ==
            native['response']['lastIteration']['norm']):
        raise ValueError('Complete original stopping residual differs')
    if peak['full_map_comparison_sha256'] != sha(a.comparison):
        raise ValueError('Named row used a different full comparison')
    if peak['statesChanged'] or peak['solverInvoked']:
        raise ValueError('Named row readout must be read-only')
    if resource['status'] != 'observed_terminal' or resource['child_returncode'] != 0:
        raise ValueError('Named readout needs its actual terminal')
    row = peak['rows'][-1]
    if row['stage'] != peak['selectedStage'] or row['stage'] != cmp['worst_variational_residual']['stage']:
        raise ValueError('Row is not the already identified global maximizer')
    if row['normalizedResidual'] != cmp['normalized_variational_residual']:
        raise ValueError('Local original replay does not attain the full stopping maximum')
    cp = native['response']['checkpoint']
    if not 0 < row['stage'] < len(cp['states']) - 1:
        raise ValueError('Only an internal free node is eligible')
    if cp['states'][row['stage']][row['residualComponent']] != row['stateValue']:
        raise ValueError('The original node component differs')
    if row['absoluteResidualInUlps'] != 1 or abs(row['flowValue']-row['stateValue']) != row['componentUlp']:
        raise ValueError('This adapter is only for a diagnosed single adjacent binary64 value')
    pack = lambda v: struct.pack('<' + 'd' * len(v), *v)
    if pack(cp['cutHeight']) != pack(native['request']['height']):
        raise ValueError('Whole original physical target differs')
    sources = dict(peak['source_sha256'])
    sources[str(a.comparison_source.resolve())] = sha(a.comparison_source)
    for name, digest in sources.items():
        if sha(name) != digest:
            raise ValueError('Original source changed: ' + name)
    sources[str(Path(__file__).resolve())] = sha(__file__)
    named = {k: row[k] for k in ('stage', 'rawCell', 'rawSegment', 'rawLeft', 'rawRight',
                                 'physicalMode', 'stateValue', 'flowValue', 'signedResidual',
                                 'normalizedResidual', 'componentUlp', 'minA', 'minD')}
    named.update(component=row['residualComponent'], componentKind=row['kind'],
                 normalizationScale=row['scale'], residualInComponentUlps=row['absoluteResidualInUlps'])
    result = dict(
        scope=__doc__, command=sys.argv, adapter_sha256=sha(__file__),
        input=str(a.input.resolve()), input_sha256=sha(a.input), inputAccepted=False,
        inputFailure=native['response']['failed'], inputLastIteration=native['response']['lastIteration'],
        replayNormalizedResidual=cmp['normalized_variational_residual'], originalGate=2e-9,
        minA=native['response']['lastIteration']['minA'], minD=native['response']['lastIteration']['minD'],
        largestResidual=[named], upstream_named_row=peak['rows'][0],
        ranking_scope='One global maximum established by the original full comparison, plus its independently checked upstream row. No complete sorted table is claimed.',
        modes=native['config']['modes'], spacing=native['config']['spacing'],
        stages=len(cp['states'])-1, source_sha256=sources,
        full_comparison_sha256=sha(a.comparison), named_readout_sha256=sha(a.peak),
        named_resource=scalar_tree(resource), named_resource_sha256=sha(a.peak_resource),
        named_actual_command=resource['command'], complete_target_unchanged=True,
        states_changed=False, solver_invoked=False,
        scope_of_adapter='Metadata compatibility only. Any future one-point initial guess must still pass the original complete DN solve, analytic Jacobian and audit.')
    a.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(dict(bytes=a.out.stat().st_size, sha256=sha(a.out))))


if __name__ == '__main__':
    main()
