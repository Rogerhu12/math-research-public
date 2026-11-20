#!/usr/bin/env python3
"""Tighten only radius cells exceeding a new exact diameter target.

Consumes a complete R663 first-jet report for exactly the same bundle and
nodes, retains every other previously proved cell bound, and uses the
unchanged R658 position-only kernel for selected cells. Raw report only.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,name):
    spec=importlib.util.spec_from_file_location(name,p)
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod)
    return mod


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('bundle','node-report','interval-source','geometry-source','radius-source','paid-cover','out'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--target-diameter',default='4.0965')
    p.add_argument('--levels',default='16384:16,65536:64')
    a=p.parse_args()
    if a.out.exists():raise FileExistsError(a.out)
    np.seterr(over='raise',invalid='raise',divide='raise',under='ignore')
    start=time.monotonic();old=json.loads(a.paid_cover.read_text())
    if not old['complete_scope'] or old['metadata']['bundle_sha256']!=sha(a.bundle) or old['metadata']['node_report_sha256']!=sha(a.node_report):
        raise ValueError('The old complete bound must concern exactly this candidate and node set')
    records=old['records'];J=old['metadata']['J']
    if [r['cell']for r in records]!=list(range(J-1)):raise ValueError('Missing paid original cells')
    target=F(a.target_diameter);limit=target*target/4
    if target<=0:raise ValueError('Positive exact target required')
    best={r['cell']:r['maximum_radius_squared_upper']for r in records}
    kernel=load(a.geometry_source,'refine_geometry');radius=load(a.radius_source,'refine_radius')
    attempts=[];metadata=[]
    for Q,sub in [tuple(map(int,v.split(':')))for v in a.levels.split(',')]:
        reader=kernel.Reader(a.bundle,a.node_report,a.interval_source,angles=Q,radial_subdivisions=sub,beta='1/4',witness=False)
        metadata.append(reader.metadata())
        for cell in [i for i in best if F(best[i])>limit]:
            r=radius.cover_cell(reader,cell);r.update(angles=Q,radial_subdivisions=sub)
            attempts.append(r);best[cell]=min(best[cell],r['radius_squared_upper'])
            print(json.dumps(dict(event='radius_refined',cell=cell,angles=Q,radial_subdivisions=sub,
                radius_squared_upper=best[cell],seconds=time.monotonic()-start)),flush=True)
    maximum=max(old['cap_bounds']['maximum_radius_squared_upper'],*best.values())
    diameter=float(reader.I.scale(reader.I.sqrt(reader.I.exact(maximum)),2.)[1])
    report=dict(schema='complete-radius-refinement-from-paid-cover-v1',source_sha256=sha(__file__),
        input_cover_sha256=sha(a.paid_cover),bundle_sha256=sha(a.bundle),node_report_sha256=sha(a.node_report),
        geometry_source_sha256=sha(a.geometry_source),radius_source_sha256=sha(a.radius_source),
        target_diameter_exact=str(target),metadata=metadata,attempts=attempts,best_radius_squared=best,
        complete_scope=True,covered_original_cells=J-1,maximum_radius_squared_upper=maximum,
        diameter_upper=diameter,target_paid=F(diameter)<=target,seconds=time.monotonic()-start,
        target_unpaid_cells=[i for i in best if F(best[i])>limit],reach_certified=False,metric_certified=False)
    a.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items()if k not in ('metadata','attempts','best_radius_squared')}),flush=True)
    print(json.dumps(dict(report_sha256=sha(a.out))),flush=True)


if __name__=='__main__':main()
