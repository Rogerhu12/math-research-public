#!/usr/bin/env python3
"""Bind a native failed-tail record to the local-relaxation probe's contract.

Only already observed metadata keys are adapted. The complete state, equations,
solver settings, and source files are never modified. Exact full-Jacobian
replay of the recorded stopping residual must already have succeeded.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('tail-record','locator','run-summary','source-topic','out'):
        parser.add_argument('--'+key,type=Path,required=True)
    a=parser.parse_args()
    record=json.loads(gzip.decompress(a.tail_record.read_bytes()))
    located=json.loads(a.locator.read_text())
    run=json.loads(a.run_summary.read_text())
    response=record['response']
    assert response.get('failed') and not response.get('converged')
    assert response['checkpoint']['states']
    assert not run['solver_success']
    assert located['input_sha256']==sha(a.tail_record)
    assert not located['inputAccepted']
    assert located['replayNormalizedResidual']==response['lastIteration']['norm']
    assert located['originalGate']==record['config']['solveTolerance']==2e-9
    sources=dict(located['source_sha256'])
    for name,digest in record['source_sha256'].items():
        path=a.source_topic/'scripts'/name
        assert sha(path)==digest
        sources[str(path.resolve())]=digest
    for name,digest in run['periodic_engine_sha256'].items():
        path=a.source_topic/'scripts/periodic-quadrature'/name
        assert sha(path)==digest
        sources[str(path.resolve())]=digest
    for name,digest in sources.items():
        assert sha(name)==digest
    result=dict(scope=__doc__,adapter_sha256=sha(__file__),
                output_record_sha256=sha(a.tail_record),
                originalSolverConverged=False,
                last_original_iteration=response['lastIteration'],
                source_sha256=sources,locator_sha256=sha(a.locator),
                run_summary_sha256=sha(a.run_summary),
                observed_original_gate=record['config']['solveTolerance'],
                scope_of_adapter='Generic probe metadata only. No claimed neighboring-state attempt or convergence is synthesized.')
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(sha256=sha(a.out),bytes=a.out.stat().st_size)))


if __name__=='__main__':
    main()
