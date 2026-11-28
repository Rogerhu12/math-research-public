#!/usr/bin/env python3
"""Exact radial-clock orientation bound from the actually stored dyadic controls."""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

p=argparse.ArgumentParser()
p.add_argument('--state',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
a=p.parse_args();rows=json.loads(a.state.read_bytes())
if rows['schema']!='H65-HF64M80-same-g-true-radial-material-clock-v1':
    raise ValueError('The actual frozen clock state is required')
knots=list(map(Q,rows['radialKnots']));freq=rows['frequencies'];n=len(freq)
c=list(map(Q,rows['coefficients']))
if c.__len__()%n or knots.count(knots[0])!=6 or knots.count(knots[-1])!=6:
    raise ValueError('Malformed clamped quintic')
zero=[Q(0)]*n;cs=[zero]*3+[c[i:i+n] for i in range(0,len(c),n)]+[zero]*3
if len(cs)!=len(knots)-6:raise ValueError('Coefficient and knot count mismatch')
bound=max(sum(abs(5*(y-x)/(knots[i+6]-knots[i+1])) for x,y in zip(left,right))
          for i,(left,right) in enumerate(zip(cs[:-1],cs[1:])))
if bound>=1:raise ArithmeticError('Clock not certified')
out=dict(schema='entire-dyadic-HF64-radial-clock-orientation-v1',
    stateSHA256=hashlib.sha256(a.state.read_bytes()).hexdigest(),
    entrySHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),absHsUpper=str(bound),
    radialClockDerivativeLower=str(1-bound),trueQuinticEndpointTwoJetIsIdentity=True)
with a.output.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(out)
