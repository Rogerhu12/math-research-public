#!/usr/bin/env python3
"""Whole-core target type for the exact affine R57 family on a real parameter box.

Uses the frozen correlation-preserving affine spline evaluator and a common
monotone root collar. It does not identify a rounded predictor with a point
of the exact family, or transfer a root certificate to an independent box.
"""
from __future__ import annotations

import argparse
from collections import deque
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time

import numpy as np

from fourfold_phase_parameter_root_interval import make_affine_target
from fourfold_phase_root_interval import Box


def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs',type=Path,required=True)
    ap.add_argument('--frozen-direction',type=Path,required=True)
    ap.add_argument('--root-certificate',type=Path,required=True)
    ap.add_argument('--parameter-left',type=float)
    ap.add_argument('--parameter-right',type=float)
    ap.add_argument('--right',type=float,default=.24)
    ap.add_argument('--quarter-nodes',type=int,default=256)
    ap.add_argument('--minimum-width',type=float,default=1e-6)
    ap.add_argument('--max-attempts',type=int,default=10000)
    ap.add_argument('--resume',action='store_true')
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    root=json.loads(args.root_certificate.read_text())
    origin_sha,direction_sha=digest(args.inputs),digest(args.frozen_direction)
    if not root['proved'] or root['origin_inputs_sha256']!=origin_sha or root['frozen_direction_sha256']!=direction_sha:
        raise ValueError('a proved common root for the same exact affine family is required')
    whole_parameter=root['exact_parameter_interval']
    parameter=[whole_parameter[0] if args.parameter_left is None else args.parameter_left,
               whole_parameter[1] if args.parameter_right is None else args.parameter_right]
    if not whole_parameter[0]<=parameter[0]<=parameter[1]<=whole_parameter[1]:
        raise ValueError('requested parameter interval lies outside the common-root proof')
    collar=root['rows'][2];cl,cr=collar['x'];rl,rr=root['root_bracket']
    if not 0<cl<=rl<=rr<=cr<args.right:raise ValueError('root collar must lie inside the positive core')
    if collar['a'][0]<=0 or collar['E'][0]<=0 or collar['Kprime'][0]<=0:
        raise ValueError('positive metric and strict common-collar Kprime are required')
    with np.load(args.inputs,allow_pickle=False) as saved:
        frozen={key:saved[key].copy() for key in saved.files}
    with np.load(args.frozen_direction,allow_pickle=False) as saved:
        direction={key:saved[key].copy() for key in saved.files}
    metadata=json.loads(str(direction['metadata']))
    if metadata['origin_inputs_sha256']!=origin_sha:raise ValueError('direction origin hash differs')
    if (direction['phase_direction_coefficients'].shape!=frozen['phase_coefficients'].shape
        or direction['alpha_direction'].shape!=frozen['alpha'].shape):
        raise ValueError('direction dimensions differ from exact origin')
    dependencies={name:digest(Path(__file__).with_name(name)) for name in [
        'fourfold_phase_parameter_root_interval.py','fourfold_phase_core_N_interval.py',
        'fourfold_phase_root_interval.py','fourfold_phase_uniform_tail.py','fourfold_interval_scalar.py']}
    config=dict(origin_inputs_sha256=origin_sha,frozen_direction_sha256=direction_sha,
        common_root_certificate_sha256=digest(args.root_certificate),source_sha256=digest(Path(__file__)),
        dependency_sha256=dependencies,exact_parameter_interval=parameter,right=args.right,
        quarter_nodes=args.quarter_nodes,minimum_width=args.minimum_width)
    target=make_affine_target(frozen,direction,parameter,args.quarter_nodes)
    cuts=np.unique(np.concatenate([np.array([0.,cl,cr,args.right])]+[
        np.r_[value,-value] for key,value in frozen.items() if key.endswith('_knots')]))
    cuts=cuts[(cuts>=0)&(cuts<=args.right)]
    queue=deque()
    for left,right in zip(cuts[:-1],cuts[1:]):
        if right<=cl:queue.append([float(left),float(right),'negative'])
        elif left>=cr:queue.append([float(left),float(right),'positive'])
    initial=len(queue);rows=[];failures=[];attempts=0;elapsed_previous=0.
    if args.resume and args.out.exists():
        old=json.loads(args.out.read_text())
        if old['configuration']!=config:raise ValueError('resume family/source/dependency configuration changed')
        queue=deque(old['pending']);rows=old['cells'];failures=old['failed_cells']
        attempts=old['attempts'];elapsed_previous=old['elapsed_seconds']
    started=time.monotonic()
    def exact_cover(sign,left,right):
        selected=sorted((r for r in rows if r['required_sign']==sign),key=lambda r:r['x'][0])
        cursor=Fraction.from_float(float(left));end=Fraction.from_float(float(right))
        for row in selected:
            lo,hi=map(lambda value:Fraction.from_float(float(value)),row['x'])
            if lo!=cursor or not lo<hi<=end:return False
            cursor=hi
        return cursor==end
    def save():
        neg=[r for r in rows if r['required_sign']=='negative']
        pos=[r for r in rows if r['required_sign']=='positive']
        covered=exact_cover('negative',0.,cl) and exact_cover('positive',cr,args.right)
        complete=bool(not queue and not failures and covered)
        report=dict(kind='continuous_whole_core_target_type_for_exact_affine_R57_family',
            configuration=config,family=metadata['family'],radial_core=[-args.right,args.right],
            common_positive_root_bracket=[rl,rr],common_monotone_collar=[cl,cr],
            common_collar_Kprime=collar['Kprime'],initial_outside_collar_cells=initial,
            attempts=attempts,elapsed_seconds=elapsed_previous+time.monotonic()-started,
            pending=list(queue),cells=rows,failed_cells=failures,
            exact_dyadic_outside_collar_coverage=covered,complete=complete,
            proved_exactly_two_target_roots_for_every_parameter=complete,
            negative_side_C_upper=max((r['C'][1] for r in neg),default=None),
            negative_side_K_upper=max((r['K'][1] for r in neg),default=None),
            positive_side_C_lower=min((r['C'][0] for r in pos),default=None),
            positive_side_K_lower=min((r['K'][0] for r in pos),default=None),
            minimum_a=min([collar['a'][0]]+[r['a'][0] for r in rows]),
            minimum_E=min([collar['E'][0]]+[r['E'][0] for r in rows]),
            conclusion=('For every exact delta in the reported interval, K0(delta)<0 for |x|<t(delta) and K0(delta)>0 for t(delta)<|x|<=right; exactly two simple target roots'
                        if complete else None),
            limitations=['Exact affine controls and mean parameters, not the larger independent control box',
                'A rounded checkpoint is not identified with an exact affine-family point by this proof',
                'Target K0 of the output radial metric is classified; actual Gaussian curvature remains separate',
                'Only the specified real core; no complex parameter tube, cap, PDE inverse, or closed isometric family'])
        args.out.parent.mkdir(parents=True,exist_ok=True)
        tmp=args.out.with_suffix(args.out.suffix+'.tmp')
        tmp.write_text(json.dumps(report,indent=2)+'\n');tmp.replace(args.out)
        return report
    while queue and attempts<args.max_attempts:
        left,right,sign=queue.popleft();attempts+=1
        try:
            value=target.evaluate(Box(left,right));value['required_sign']=sign
            passed=(value['a'][0]>0 and value['E'][0]>0 and
                    (value['C'][1]<0 if sign=='negative' else value['C'][0]>0))
            value['passed']=bool(passed)
        except (ValueError,ZeroDivisionError) as error:
            passed=False;value=dict(x=[left,right],required_sign=sign,passed=False,error=str(error))
        if passed:rows.append(value)
        elif right-left>args.minimum_width:
            middle=float((Fraction.from_float(left)+Fraction.from_float(right))/2)
            if left<middle<right:
                queue.appendleft([middle,right,sign]);queue.appendleft([left,middle,sign])
            else:failures.append(value)
        else:failures.append(value)
        if attempts%10==0 or not passed or not queue:
            report=save()
            print(json.dumps(dict(attempts=attempts,accepted=len(rows),pending=len(queue),failed=len(failures),
                x=[left,right],required_sign=sign,C=value.get('C'),elapsed_seconds=report['elapsed_seconds'])),flush=True)
    report=save()
    print(json.dumps({key:value for key,value in report.items() if key not in ['pending','cells','failed_cells']},indent=2),flush=True)
    if not report['complete']:raise SystemExit('affine core type proof incomplete; inspect failures or resume pending cells')


if __name__=='__main__':main()
