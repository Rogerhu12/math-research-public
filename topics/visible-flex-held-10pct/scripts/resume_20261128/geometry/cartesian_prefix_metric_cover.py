#!/usr/bin/env python3
"""Check the complete exact leaf cover and bind it to the same R73 map.

This does not replace interval evaluation. It checks that its saved leaves
cover the entire declared domain, obey an exact rational budget, and use
every literal defining array of the already covered geometric map unchanged.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--metric-report',type=Path,required=True)
    parser.add_argument('--geometry-report',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    a=parser.parse_args()
    p,g=a.metric_report.resolve(),a.geometry_report.resolve()
    r,geom=(json.loads(x.read_text()) for x in (p,g))
    if (r.get('metric_certified') is not True
            or r.get('status')!='continuous_new_cartesian_prefix_metric_certified'
            or geom.get('status')!='continuous_new_prefix_geometry_certified'
            or geom.get('failed_boxes')!=0
            or r['source_run_sha256']!=geom['source_run_sha256']):
        raise ValueError('Require actual complete metric and geometry covers of one source')
    for record in (r,geom):
        for name,digest in record['source_hashes'].items():
            if sha(name)!=digest:
                raise ValueError('A bound evaluation source changed: '+name)
    table=Path(r['table_report'])
    if sha(table)!=r['table_report_sha256']:
        raise ValueError('The bound complete angular table changed')
    leaves=p.parent/'complete-leaves.jsonl'
    if sha(leaves)!=r['complete_leaves_sha256']:
        raise ValueError('Complete leaves differ from the returned interval certificate')
    rows=[json.loads(line) for line in leaves.read_text().splitlines()]
    budget=Q(99,10**8)
    if (len(rows)!=r['accepted'] or Q(rows[0]['left'])!=0
            or Q(rows[-1]['right'])!=Q(r['full_radial_range'][1])
            or any(Q(x['right'])!=Q(y['left']) for x,y in zip(rows[:-1],rows[1:]))
            or any(not Q(row['left'])<Q(row['right']) for row in rows)
            or any(not 0<=Q.from_float(row['bound'])<budget for row in rows)
            or max(row['bound'] for row in rows)!=r['peak']):
        raise ValueError('The exact full-domain cover or rational metric budget failed')
    old=g.parent/'actual-prefix-exact-defining-jets.npz'
    new=Path(r['defining_jets']['path'])
    if sha(old)!=geom['defining_jets_sha256'] or sha(new)!=r['defining_jets']['sha256']:
        raise ValueError('The literal common-map defining data changed')
    with np.load(old,allow_pickle=False) as before,np.load(new,allow_pickle=False) as after:
        same={key:bool(np.array_equal(before[key],after[key])) for key in before.files}
    if not all(same.values()):
        raise ValueError('Metric and R73 geometry must use exactly the same finite map')
    result=dict(status='complete_exact_leaf_cover_and_R73_same_map_binding_verified',
        source_sha256=sha(__file__),metric_report=str(p),metric_report_sha256=sha(p),
        geometry_report=str(g),geometry_report_sha256=sha(g),metric_complete=True,
        radial_leaves=len(rows),angular_sector_boxes=r['angular_boxes_per_sector'],
        sector_boxes=len(rows)*r['angular_boxes_per_sector'],
        full_circle_equivalent_boxes=3*len(rows)*r['angular_boxes_per_sector'],
        exact_cover=True,radial_left_exact=rows[0]['left'],radial_right_exact=rows[-1]['right'],
        maximum_binary_upper_exact=str(Q.from_float(r['peak'])),
        exact_rational_metric_budget=str(budget),
        exact_remaining_margin=str(budget-Q.from_float(r['peak'])),
        R73_defining_file=dict(path=str(old),sha256=sha(old)),
        new_defining_file=dict(path=str(new),sha256=sha(new)),
        every_R73_defining_array_identical=same,chart_is_additional_definition=True,
        tail_or_cut_lift_included=False,closed_surface=False)
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
