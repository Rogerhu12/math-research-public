#!/usr/bin/env python3
"""Add exact binary64 component spacing to the read-only stage diagnostic."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import numpy as np

p=argparse.ArgumentParser()
p.add_argument('--record',type=Path,required=True)
p.add_argument('--diagnostic',type=Path,required=True)
p.add_argument('--out',type=Path,required=True)
a=p.parse_args()
d=json.loads(a.diagnostic.read_text())
if hashlib.sha256(a.record.read_bytes()).hexdigest()!=d['input_sha256']:
    raise ValueError('Diagnostic and checkpoint input hash differ')
states=json.load(gzip.open(a.record,'rt'))['response']['checkpoint']['states']
for row in d['largestResidual']:
    value=states[row['stage']][row['component']]
    row['residualComponentStateValue']=value
    row['residualComponentUlp']=abs(float(np.spacing(value)))
    row['residualComponentUlpDividedByScale']=row['residualComponentUlp']/row['normalizationScale']
    row['residualInComponentUlps']=row['normalizedResidual']/row['residualComponentUlpDividedByScale']
d['ulp_annotation']=dict(scope=__doc__,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                         diagnostic_sha256=hashlib.sha256(a.diagnostic.read_bytes()).hexdigest())
a.out.write_text(json.dumps(d,indent=2)+'\n')
