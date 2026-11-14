#!/usr/bin/env python3
"""Full regional six-jet comparison for the explicit target-metric rr field."""
import argparse
import json
from pathlib import Path
import exact_20261114_regional_common_grid as regional
from exact_20261114_source_knot_rr_probe import TargetLayer


def main():
    p=argparse.ArgumentParser(add_help=False);p.add_argument('--out',type=Path,required=True)
    a,_=p.parse_known_args();here=Path(__file__).resolve().parent
    hashes={str(q):regional.core.sha(q)for q in [Path(__file__),here/'exact_20261114_source_knot_rr_probe.py',here/'exact_20261114_regional_common_grid.py']}
    original=regional.core.Layer;layers=[]
    def create(*args,**kwargs):
        layer=TargetLayer(*args,**kwargs);layers.append(layer);return layer
    regional.core.Layer=create
    try:regional.main()
    finally:regional.core.Layer=original
    result=json.loads(a.out.read_text());result['schema']='fixed-g-target-metric-rr-regional-six-jet-comparison-v1'
    result['source_sha256_at_start'].update(hashes)
    result['target_metric_rr']=dict(rule='Frr=Gamma Fr + ((urr-Gamma ur)/nz) n at genuine nodes; n uses actual cardinal Ftheta.',
        layers={q.label:dict(nodes=len(q.tail.r),verified_raw_nodes=len(q.tail.verified_nodes),diagnostics=q.tail.diag)for q in layers},
        old_closed_outputs_unchanged=True)
    result['limitations'].append('Both layers use the explicit target-metric rr finite interpolation rule; this does not replace the prior difference-rr outputs or assert exact ODE Cartesian rr.')
    a.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(event='target_metric_six_jet_complete',out=str(a.out))),flush=True)


if __name__=='__main__':main()
