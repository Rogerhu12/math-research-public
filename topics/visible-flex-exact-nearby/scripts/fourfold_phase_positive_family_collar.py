#!/usr/bin/env python3
"""Uniform actual root-to-quarter positive collar for the true affine family.

A previously proved larger parameter root tube is used only after exact
parameter containment and frozen source/dependency verification.  Every
member has its own actual root; neither endpoint is a frozen radial root.
"""
from __future__ import annotations

import argparse
from collections import deque
from fractions import Fraction
import json
from pathlib import Path
import time
import numpy as np
from flint import arb,ctx

from fourfold_phase_positive_family_outer import StablePositiveFamily
from fourfold_phase_actual_positive_cap import PositiveCapTarget,aggregate
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_parameter_germ import provenance,sha


class PositiveFamilyCollar(StablePositiveFamily):
    evaluate_cap=PositiveCapTarget.evaluate_cap


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--center-object',type=Path,required=True)
    ap.add_argument('--root-tube',type=Path,required=True)
    ap.add_argument('--half-width',type=Fraction,default=Fraction(1,2000000))
    ap.add_argument('--cut',type=Fraction,default=Fraction(1,4))
    ap.add_argument('--normalized-strip',type=Fraction,default=Fraction(1,128))
    ap.add_argument('--max-cell-width',type=Fraction,default=Fraction(1,4096))
    ap.add_argument('--quarter-nodes',type=int,default=256)
    ap.add_argument('--angles',type=int,default=512)
    ap.add_argument('--bits',type=int,default=160)
    ap.add_argument('--max-depth',type=int,default=12)
    ap.add_argument('--max-attempts',type=int,default=1000)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=args.bits;ctx.cap=4
    started=time.monotonic()
    target=PositiveFamilyCollar(args.center_object,args.half_width,args.quarter_nodes,args.angles,
                               arb('.003'),arb('.0025'),arb('.32'))
    tube=json.loads(args.root_tube.read_text())
    here=Path(__file__).parent
    if (tube.get('kind')!='uniform_affine_germ_Arb_root' or not tube.get('proved')
        or tube['source_sha256']!=sha(here/'fourfold_phase_beta_parameter_germ.py')
        or tube['origin_inputs_sha256']!=target.parameter_definition['origin_inputs']['sha256']
        or tube['direction_sha256']!=target.parameter_definition['direction']['sha256']):
        raise ValueError('the root tube is not a proved tube of the same exact family')
    for name,digest in tube['dependency_sha256'].items():
        if sha(here/name)!=digest:raise ValueError('root tube dependency changed: '+name)
    outer=list(map(Fraction,tube['exact_parameter_interval']))
    inner=target.parameter_interval
    if not outer[0]<=inner[0]<=inner[1]<=outer[1]:
        raise ValueError('requested parameter box is not contained in the true root tube')
    lower=arb(tube['root']['lower']).lower()
    upper=arb(tube['root']['upper']).upper()
    roots=[Fraction.from_float(float(np.nextafter(float(lower),-np.inf))),
           Fraction.from_float(float(np.nextafter(float(upper),np.inf)))]
    if not exact_arb(roots[0])<lower or not exact_arb(roots[1])>upper:
        raise ValueError('binary root envelope failed to be outward')
    cut=args.cut;sigma=exact_arb(args.normalized_strip)
    if not 0<roots[0]<roots[1]<cut<=3 or not sigma>0 or not args.max_cell_width>0:
        raise ValueError('invalid physical collar')
    monotone_cut=min(cut,roots[1]+Fraction(1,4096))
    knots={roots[0],cut,monotone_cut}
    for key,values in target.frozen.items():
        if key.endswith('_knots'):
            knots.update(q for q in (abs(Fraction.from_float(float(x))) for x in values) if roots[0]<q<cut)
    points=sorted(knots);initial=list(zip(points,points[1:]))
    queue=deque()
    for a,b in initial:
        count=max(1,-(-(b-a)//args.max_cell_width))
        queue.extend((a+(b-a)*j/count,a+(b-a)*(j+1)/count,0) for j in range(count))
    rows=[];failures=[];attempts=0
    identity=provenance(target,args.center_object);identity.pop('dependency_sha256')
    report=dict(kind='uniform_true_affine_root_to_regular_positive_collar',complete=False,**identity,
        root_tube_path=str(args.root_tube),root_tube_sha256=sha(args.root_tube),
        wider_root_parameter_interval=list(map(str,outer)),
        root_interval=list(map(str,roots)),physical_regular_cut=str(cut),
        monotone_root_collar_cut=str(monotone_cut),initial_original_spans=len(initial),
        normalized_angle_strip=str(args.normalized_strip),maximum_initial_cell_width=str(args.max_cell_width),
        quarter_nodes=args.quarter_nodes,angular_boxes=args.angles,bits=args.bits,
        dependency_sha256={name:sha(here/name) for name in [
            'fourfold_phase_positive_family_outer.py','fourfold_phase_actual_positive_cap.py',
            'fourfold_phase_beta_parameter_germ.py','fourfold_phase_beta_parameter_root.py',
            'fourfold_phase_beta_affine.py','fourfold_phase_beta_interval.py',
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_beta_bulk_box.py',
            'fourfold_phase_root_interval.py','fourfold_phase_uniform_tail.py','fourfold_interval_scalar.py']},
        cells=rows,failed_cells=failures,
        scope=['Each parameter uses its own genuine root t(delta) in the proved wider tube.',
               'The interval below the true root is used only for the common derivative/geometry bounds.',
               'Complete source and both full ports, with angular mean and cross, are retained.',
               'No closed cap, exterior beyond r=3, or fixed open H is asserted.'])
    report['source_sha256']=sha(__file__)
    def save():
        report['attempts']=attempts;report['pending']=[[str(a),str(b),d] for a,b,d in queue]
        report['elapsed_seconds']=time.monotonic()-started
        args.out.parent.mkdir(parents=True,exist_ok=True)
        temporary=args.out.with_suffix(args.out.suffix+'.tmp')
        temporary.write_text(json.dumps(report,indent=2)+'\n');temporary.replace(args.out)
    while queue and attempts<args.max_attempts:
        a,b,depth=queue.popleft();attempts+=1;target.set_cell(a,b)
        try:
            row=target.evaluate_cap(a,b,sigma,roots,monotone_cut);rows.append(row)
            print(json.dumps(dict(attempt=attempts,accepted=len(rows),pending=len(queue),
                                  interval=[float(a),float(b)],Kprime=row['Kprime'])),flush=True)
        except (ValueError,ZeroDivisionError) as exc:
            if depth<args.max_depth:
                mid=(a+b)/2;queue.appendleft((mid,b,depth+1));queue.appendleft((a,mid,depth+1))
            else:failures.append(dict(interval=[str(a),str(b)],reason=str(exc)))
            print(json.dumps(dict(attempt=attempts,refinement=depth,reason=str(exc))),flush=True)
        save()
    rows.sort(key=lambda row:Fraction(row['radial_interval'][0]));cursor=roots[0]
    for row in rows:
        a,b=map(Fraction,row['radial_interval'])
        if a!=cursor:break
        cursor=b
    report['exact_radial_cover']=bool(cursor==cut and not queue and not failures)
    if report['exact_radial_cover']:
        report['operator_constants']=aggregate(rows,roots,cut,sigma);report['complete']=True
    save()
    print(json.dumps(dict(complete=report['complete'],accepted=len(rows),failed=len(failures),
                         elapsed_seconds=report['elapsed_seconds']),indent=2),flush=True)
    if not report['complete']:raise SystemExit('the uniform moving-root collar is not yet certified')


if __name__=='__main__':main()
