#!/usr/bin/env python3
"""Classify the entire real core of one exact symmetric target metric.

All cells outside an already certified monotone root collar are evaluated
with the same infinite-primitive, direct-interval-DFT target evaluator. The
collar is kept whole, so a true root is never chased by repeated zero-width
subdivision. This classifies K0 of the chosen output radial metric, not the
actual nonradial Gaussian curvature of F.
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

from fourfold_phase_core_interval import CoreTarget
from fourfold_phase_root_interval import Box


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs',type=Path,required=True)
    ap.add_argument('--root-certificate',type=Path,required=True)
    ap.add_argument('--right',type=float,default=.25)
    ap.add_argument('--quarter-nodes',type=int,default=256)
    ap.add_argument('--minimum-width',type=float,default=1e-6)
    ap.add_argument('--max-attempts',type=int,default=10000)
    ap.add_argument('--resume',action='store_true')
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    root=json.loads(args.root_certificate.read_text())
    inputs_sha=hashlib.sha256(args.inputs.read_bytes()).hexdigest()
    if root['inputs_sha256']!=inputs_sha or not root['sign_and_simple_root_gate']:
        raise ValueError('a passed local root certificate for these same exact inputs is required')
    collar=root['optional_collar_evaluation']
    if collar is None: raise ValueError('the root certificate must include a real collar')
    cl,cr=collar['x'];rl,rr=root['isolating_interval']
    if not 0<cl<=rl<=rr<=cr<args.right:
        raise ValueError('positive root collar must lie strictly inside the requested core')
    if min(collar['a'])<=0 or min(collar['E'])<=0:
        raise ValueError('positive target metric on the collar is required')
    if collar['Cprime'][0]<=0 and collar['Kprime'][0]<=0:
        raise ValueError('the complete root collar needs a strict monotonicity certificate')
    dependencies={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
        for name in ['fourfold_phase_core_interval.py','fourfold_phase_root_interval.py',
                     'fourfold_phase_uniform_tail.py','fourfold_interval_scalar.py']}
    config=dict(inputs_sha256=inputs_sha,root_certificate_sha256=hashlib.sha256(args.root_certificate.read_bytes()).hexdigest(),
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),dependency_sha256=dependencies,
        right=args.right,quarter_nodes=args.quarter_nodes,minimum_width=args.minimum_width)
    with np.load(args.inputs,allow_pickle=False) as saved:
        frozen={key:saved[key].copy() for key in saved.files}
    target=CoreTarget(frozen,args.quarter_nodes,max(512,2*args.quarter_nodes))
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
        if old['configuration']!=config:raise ValueError('resume input/source/dependency configuration changed')
        queue=deque(old['pending']);rows=old['cells'];failures=old['failed_cells']
        attempts=old['attempts'];elapsed_previous=old['elapsed_seconds']
    started=time.monotonic()
    def exact_cover(sign,left,right):
        selected=sorted((r for r in rows if r['required_sign']==sign),key=lambda r:r['x'][0])
        cursor=Fraction.from_float(float(left));end=Fraction.from_float(float(right))
        for row in selected:
            lo,hi=map(lambda v:Fraction.from_float(float(v)),row['x'])
            if lo!=cursor or not lo<hi<=end:return False
            cursor=hi
        return cursor==end
    def save():
        negative=[r for r in rows if r['required_sign']=='negative']
        positive=[r for r in rows if r['required_sign']=='positive']
        coverage=exact_cover('negative',0.,cl) and exact_cover('positive',cr,args.right)
        complete=bool(not queue and not failures and coverage)
        report=dict(kind='continuous_full_core_target_type_classification_for_exact_symmetric_infinite_R33',
            configuration=config,source_checkpoint_sha256=json.loads(str(frozen['metadata']))['checkpoint_sha256'],
            radial_core=[-args.right,args.right],positive_root_isolator=[rl,rr],
            monotone_root_collar=[cl,cr],root_collar_Cprime=collar['Cprime'],root_collar_Kprime=collar['Kprime'],
            initial_outside_collar_cells=initial,attempts=attempts,
            elapsed_seconds=elapsed_previous+time.monotonic()-started,
            pending=list(queue),cells=rows,failed_cells=failures,
            exact_dyadic_outside_collar_coverage=coverage,complete=complete,
            proved_exactly_two_target_roots_in_core=complete,
            negative_side_C_upper=max((r['C'][1] for r in negative),default=None),
            negative_side_K_upper=max((r['K'][1] for r in negative),default=None),
            positive_side_C_lower=min((r['C'][0] for r in positive),default=None),
            positive_side_K_lower=min((r['K'][0] for r in positive),default=None),
            minimum_a=min([collar['a'][0]]+[r['a'][0] for r in rows]),
            minimum_E=min([collar['E'][0]]+[r['E'][0] for r in rows]),
            conclusion=('K0<0 for |x|<t and K0>0 for t<|x|<=right; exactly two simple target roots +/-t'
                        if complete else None),
            limitations=['Only target K0 of E=<Fx dot Fx>, a² is classified; actual nonradial Gaussian curvature is a separate quantity',
                'Only the specified core, not all outer body or caps, is classified',
                'The input is explicitly symmetric and uses the infinite angular primitive; no transfer to an old approximate-mirror ray or another parameter point',
                'No exact radial metric equation or closed isometric family follows from this certificate'])
        args.out.parent.mkdir(parents=True,exist_ok=True)
        temporary=args.out.with_suffix(args.out.suffix+'.tmp')
        temporary.write_text(json.dumps(report,indent=2)+'\n');temporary.replace(args.out)
        return report
    while queue and attempts<args.max_attempts:
        left,right,sign=queue.popleft();attempts+=1
        try:
            value=target.evaluate(Box(left,right))
            value['required_sign']=sign
            passed=(value['a'][0]>0 and value['E'][0]>0
                    and (value['C'][1]<0 if sign=='negative' else value['C'][0]>0))
            value['passed']=bool(passed)
        except (ValueError,ZeroDivisionError) as error:
            passed=False
            value=dict(x=[left,right],required_sign=sign,passed=False,error=str(error))
        if passed:rows.append(value)
        elif right-left>args.minimum_width:
            middle=float((Fraction.from_float(left)+Fraction.from_float(right))/2)
            if left<middle<right:
                queue.appendleft([middle,right,sign]);queue.appendleft([left,middle,sign])
            else:failures.append(value)
        else:failures.append(value)
        if attempts%10==0 or not passed or not queue:
            progress=save()
            print(json.dumps(dict(attempts=attempts,accepted=len(rows),pending=len(queue),failed=len(failures),
                x=[left,right],required_sign=sign,C=value.get('C'),
                elapsed_seconds=progress['elapsed_seconds'])),flush=True)
    report=save()
    print(json.dumps({key:value for key,value in report.items()
                      if key not in ['pending','cells','failed_cells']},indent=2),flush=True)
    if not report['complete']:raise SystemExit('core target classification incomplete; inspect failures or resume pending cells')


if __name__=='__main__':main()
