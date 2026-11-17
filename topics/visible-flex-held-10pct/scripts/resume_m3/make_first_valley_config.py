#!/usr/bin/env python3
"""Build an explicit first-valley physical design config for modes 2 or 3."""
import argparse
import json
from pathlib import Path

p=argparse.ArgumentParser()
p.add_argument('--input',type=Path,required=True)
p.add_argument('--out',type=Path,required=True)
p.add_argument('--beta0',type=float,required=True)
p.add_argument('--spacing',type=int,choices=[2,3],required=True)
p.add_argument('--modes',type=int,default=8)
p.add_argument('--quadrature',type=int,default=128)
a=p.parse_args()
if a.quadrature<=4*a.modes*a.spacing:
    raise ValueError('Original quadrature orthogonality gate is not satisfied')
j=json.loads(a.input.read_text())
for k in ['initialCheckpoint','designInitialCheckpoint','secantCheckpoint','traceFile','geometricAmplitudePredictor']:
    j.pop(k,None)
if not j.get('valleyControls'):
    raise ValueError('Expected full original valley controls')
j['valleyControls'][0]=a.beta0
j['spacing']=a.spacing;j['modes']=a.modes;j['quadrature']=a.quadrature
a.out.parent.mkdir(parents=True,exist_ok=True)
a.out.write_text(json.dumps(j,indent=2)+'\n')
