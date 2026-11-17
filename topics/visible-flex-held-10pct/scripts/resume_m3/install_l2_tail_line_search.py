#!/usr/bin/env python3
"""Use weighted L2 only to select Newton steps, preserving the original gate.

All equations, row scales, local D/S/A conditions, Jacobians and final weighted
L-infinity convergence checks are unchanged. The original strict decrease of
weighted L-infinity is replaced by strict decrease of weighted L2 in the
finite line search. This is an explicitly different Newton globalization,
not a relaxation of the accepted residual.
"""
import argparse
import hashlib
import json
from pathlib import Path

p=argparse.ArgumentParser()
p.add_argument('--source-topic',type=Path,required=True)
a=p.parse_args()
file=a.source_topic/'scripts/950f-tail-stage-core.mjs'
before=file.read_text();after=before
changes=[
 ('let norm=0,minA=Infinity,minD=Infinity;',
  'let norm=0,norm2Squared=0,minA=Infinity,minD=Infinity;'),
 ('norm=Math.max(norm,...Array.from(r,v=>Math.abs(v)/scales[n]));flows.push(f);residuals.push(r);',
  'norm=Math.max(norm,...Array.from(r,v=>Math.abs(v)/scales[n]));for(const v of r){const z=v/scales[n];norm2Squared+=z*z;}flows.push(f);residuals.push(r);'),
 ('norm=Math.max(norm,Math.abs(end[j])/scales[depth]);}',
  'norm=Math.max(norm,Math.abs(end[j])/scales[depth]);norm2Squared+=(end[j]/scales[depth])**2;}'),
 ('for(let j=0;j<M;j++)norm=Math.max(norm,Math.abs(states[0][j]-target[j])/scales[0]);',
  'for(let j=0;j<M;j++){const z=(states[0][j]-target[j])/scales[0];norm=Math.max(norm,Math.abs(z));norm2Squared+=z*z;}'),
 ('return {flows,residuals,end,norm,minA,minD};',
  'return {flows,residuals,end,norm,norm2:Math.sqrt(norm2Squared),minA,minD};'),
 ('history.push({iteration:it,norm:ev.norm,minA:ev.minA,minD:ev.minD});',
  'history.push({iteration:it,norm:ev.norm,norm2:ev.norm2,minA:ev.minA,minD:ev.minD});'),
 ('if(test.norm<ev.norm){states=trial;',
  'if(test.norm2<ev.norm2){states=trial;')
]
for old,new in changes:
    if after.count(old)!=1:raise ValueError('Unexpected core source marker: '+old)
    after=after.replace(old,new)
after='// Optional L2 line search; original L-infinity final acceptance unchanged.\n'+after
file.write_text(after)
print(json.dumps(dict(scope=__doc__,before_sha256=hashlib.sha256(before.encode()).hexdigest(),
                      after_sha256=hashlib.sha256(after.encode()).hexdigest()),indent=2))
