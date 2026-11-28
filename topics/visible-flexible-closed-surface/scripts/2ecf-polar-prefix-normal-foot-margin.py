#!/usr/bin/env python3
"""Rational angular margin for nearest-ellipse projection of the accurate strong prefix."""
import argparse,json,hashlib
from fractions import Fraction as Q
from pathlib import Path

p=argparse.ArgumentParser()
p.add_argument('--envelope',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
a=p.parse_args()
d=json.loads(a.envelope.read_text())
assert d['schema']=='certified-accurate-R233-R232-prefix-envelope-v1'
v={k:Q(x) for k,x in d['exactRationalBounds'].items()}
rho=v['B']**2/v['A'];h=v['entireMeridionalPathUpper'];c=v['verticalTangentProjectionLower']
t=h/rho
assert t<Q('.71503') and c>Q('.71795')
cos_delta=Q('.699');sin_phi=Q('.6962')
assert cos_delta**2<1-t*t and sin_phi**2>1-c*c
coorientation=c*cos_delta-t*sin_phi
assert coorientation>Q('.004')
out=dict(schema='sharp-ellipse-Gauss-turn-and-accurate-prefix-margin-v1',
         envelopeSHA256=hashlib.sha256(a.envelope.read_bytes()).hexdigest(),ellipseReach=str(rho),
         normalFootSinUpper=str(t),positiveProjectionCoorientationLower=str(coorientation),
         ballRadiusSlack=str(rho*c-h),globalInjectivityNotClaimed=True)
with a.output.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(float(t),float(c),float(coorientation),float(rho*c-h))
