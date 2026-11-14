#!/usr/bin/env python3
"""Freeze the finitely many source calibration outputs as geometry constants.

These constants need not solve a hidden exact calibration equation. The
infinite source from n=160 onward keeps its separate reviewed definition.
The global radial-width multiplier remains an exact integral-defined value.
"""
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path

ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('bookkeeping');ap.add_argument('out')
ap.add_argument('checkpoints',nargs='+')
args=ap.parse_args()
bkpath=Path(args.bookkeeping);bk=json.loads(bkpath.read_text())
rows=bk['rows']
if len(rows)!=160 or [x['n'] for x in rows]!=list(range(160)):
    raise ValueError('expected the finite cells 0 through 159')
keys=['delta0','R','a','etaPower','etaRatioAtN0','prefixR','prefixEnd',
      'prefixReturnStart','prefixRByCell','calibrationSteps','rejoinR20At','rejoinIndexOffset']
frozen=None;checked=[]
for name in args.checkpoints:
    path=Path(name);obj=json.load(gzip.open(path,'rt') if path.suffix=='.gz' else path.open())
    r=obj.get('response',obj);cp=r.get('checkpoint',r)
    p={k:cp['parameters'].get(k) for k in keys}
    if frozen is None:frozen=p
    elif p!=frozen:raise ValueError('source calibration parameters changed: '+name)
    checked.append({'path':str(path.resolve()),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                    'modes':cp['parameters']['modes'],'steps':cp['parameters']['steps'],
                    'shootingParts':cp['parameters']['shootingParts'],'physicalDepth':cp['parameters']['physicalDepth']})
constants=[{'n':x['n'],'value':x['calibrationAlpha'],'hex':float(x['calibrationAlpha']).hex()} for x in rows]
lo=min(Fraction(x['value']) for x in constants);hi=max(Fraction(x['value']) for x in constants)
root=Path(__file__).resolve().parent.parent
sources=[root/'scripts/closing_recalibrated_tail.mjs',root/'scripts/closing_weighted_tail.mjs',
         root/'repro/source-root/topics/large-amplitude-twist-flex/scripts/tailnext_balanced_tail.mjs',
         root/'repro/source-root/topics/large-amplitude-twist-flex/scripts/general_root_smooth_tail_cells.cjs']
report={'status':'frozen-finite-source-geometry-constants','scope':__doc__,
        'scriptSHA256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'bookkeepingSHA256':hashlib.sha256(bkpath.read_bytes()).hexdigest(),
        'sourceHashes':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
        'calibrationParameters':frozen,'candidateParameterEqualityVerified':True,'checkedCandidates':checked,
        'minimumExact':str(lo),'maximumExact':str(hi),'allAtLeastOneHalf':lo>=Fraction(1,2),
        'allAtMostTwo':hi<=2,'constants':constants,
        'infiniteSourceBeginsAt':160,'globalRadialAlphaIsNotThisTable':True}
Path(args.out).write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'output':args.out,'sha256':hashlib.sha256(Path(args.out).read_bytes()).hexdigest(),
                  'candidatesChecked':len(checked),'count':len(constants),'min':float(lo),'max':float(hi),
                  'allAtLeastOneHalf':report['allAtLeastOneHalf'],'allAtMostTwo':report['allAtMostTwo']}))
