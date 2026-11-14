#!/usr/bin/env python3
"""Exact rational finite-collar bound for the target-metric rr terminal jet."""
import argparse
import json
from pathlib import Path
import exact_20261114_finite_collar_bound as collar
from exact_20261114_source_knot_rr_probe import TargetMetricTail


def main():
    p=argparse.ArgumentParser(add_help=False);p.add_argument('--out',type=Path,required=True)
    a,_=p.parse_known_args();here=Path(__file__).resolve().parent
    hashes={str(q):collar.sha(q)for q in [Path(__file__),Path(collar.__file__),here/'exact_20261114_source_knot_rr_probe.py']}
    original=collar.RefinedTail;collar.RefinedTail=TargetMetricTail
    try:collar.main()
    finally:collar.RefinedTail=original
    result=json.loads(a.out.read_text());result['target_metric_rr']=dict(source_sha256_at_start=hashes,
        rule='The binary Fourier terminal coefficients use the Gauss-Weingarten rr completion.',
        bound_scope='Same exact rational finite-collar calculation, applied to these actual new terminal coefficients.')
    a.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(event='target_metric_collar_complete',out=str(a.out))),flush=True)


if __name__=='__main__':main()
