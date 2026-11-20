#!/usr/bin/env python3
"""Cover every original closed-field cell with R656 and refine unpaid curvature bounds.

The threshold is a certificate target, never a numerical acceptance test.
No curvature value from another candidate or an uncovered cell is imported.
All attempted covers remain in the raw report; each paid cell may use its
smallest valid complete bound. This driver alone makes no metric/reach claim.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
from fractions import Fraction

import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path):
    spec=importlib.util.spec_from_file_location('adaptive_curvature_kernel',path)
    mod=importlib.util.module_from_spec(spec);sys.modules[spec.name]=mod
    spec.loader.exec_module(mod)
    return mod


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('bundle','node-report','interval-source','geometry-source','out'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--levels',default='2048:1,8192:8,32768:32')
    p.add_argument('--target',default='8.1')
    p.add_argument('--beta',default='1/4')
    a=p.parse_args()
    if a.out.exists():raise FileExistsError('Retain each previous curvature cover')
    levels=[tuple(map(int,v.split(':')))for v in a.levels.split(',')]
    target=Fraction(a.target)
    if target<=0:raise ValueError('Positive exact target required')
    np.seterr(over='raise',invalid='raise',divide='raise',under='ignore')
    start=time.monotonic();mod=load(a.geometry_source)
    report=dict(schema='fullclosed-adaptive-continuous-curvature-v1',source_sha256=sha(__file__),
        bundle_sha256=sha(a.bundle),node_report_sha256=sha(a.node_report),
        geometry_source_sha256=sha(a.geometry_source),interval_source_sha256=sha(a.interval_source),
        levels=levels,target_exact=str(target),beta_exact=a.beta,attempts=[],best={},
        complete_scope=False,target_certified=False,reach_certified=False,metric_certified=False)
    best={};allcells=None
    for level,(angles,radial) in enumerate(levels):
        reader=mod.Reader(a.bundle,a.node_report,a.interval_source,
            angles=angles,radial_subdivisions=radial,beta=a.beta,witness=False)
        if allcells is None:
            allcells=list(range(reader.J-1));report['metadata']=reader.metadata()
        if len(allcells)!=reader.J-1:raise ValueError('Carrier changed between levels')
        pending=[i for i in allcells if i not in best or Fraction(best[i]['curvature_upper'])>target]
        print(json.dumps(dict(event='curvature_level_start',level=level,angles=angles,
            radial_subdivisions=radial,pending=len(pending),seconds=time.monotonic()-start)),flush=True)
        for count,cell in enumerate(pending,1):
            r=reader.certify(cell)
            r.update(level=level,angles=angles,radial_subdivisions=radial)
            report['attempts'].append(r)
            if r['all_radial_and_angular_points_covered'] and r['curvature_upper'] is not None:
                if cell not in best or r['curvature_upper']<best[cell]['curvature_upper']:
                    best[cell]=r
            if count%32==0 or count==len(pending):
                report['best']={str(k):v for k,v in best.items()}
                report['seconds']=time.monotonic()-start
                report['paid_cell_count']=len(best)
                report['target_paid_cell_count']=sum(Fraction(v['curvature_upper'])<=target for v in best.values())
                a.out.write_text(json.dumps(report,indent=2)+'\n')
                print(json.dumps(dict(event='curvature_progress',level=level,level_done=count,
                    level_total=len(pending),paid=len(best),target_paid=report['target_paid_cell_count'],
                    maximum_paid_bound=max((v['curvature_upper']for v in best.values()),default=None),
                    seconds=report['seconds'])),flush=True)
        if all(i in best and Fraction(best[i]['curvature_upper'])<=target for i in allcells):break
    complete=sorted(best)==allcells
    maximum=max((v['curvature_upper']for v in best.values()),default=None)
    report.update(best={str(k):v for k,v in best.items()},complete_scope=complete,
        covered_original_cells=len(best),total_original_cells=len(allcells),
        curvature_upper=maximum if complete else None,
        flat_caps_curvature_upper=0.,reflection_and_axial_phases_preserve_curvature=True,
        target_certified=bool(complete and Fraction(maximum)<=target),
        remaining_above_target=[i for i in allcells if i not in best or Fraction(best[i]['curvature_upper'])>target],
        seconds=time.monotonic()-start)
    a.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items()if k not in ('attempts','best','metadata')}),flush=True)
    print(json.dumps(dict(event='curvature_cover_complete',report_sha256=sha(a.out))),flush=True)


if __name__=='__main__':main()
