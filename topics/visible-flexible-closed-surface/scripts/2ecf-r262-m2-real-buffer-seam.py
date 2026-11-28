#!/usr/bin/env python3
"""Check the actual flat-slope neighborhood of the new finite/infinite m2 material seam."""
import argparse,hashlib,importlib.util,json,sys
from fractions import Fraction as F
from pathlib import Path
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--scripts',type=Path,required=True);ap.add_argument('--primitive',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();S=a.scripts.resolve();sys.path.insert(0,str(S));p=S/'db6f-tail-background-packet-totalwidth.py';q=importlib.util.spec_from_file_location('m2_original_bg_bounds',p);m=importlib.util.module_from_spec(q);q.loader.exec_module(m);cal=S.parent/'notes/2026-11-09-db6f-tail-finite-source-calibrations.json';b=m.Background(a.primitive,cal)
    lo,hi=F(1,4)-F(1,65536),F(1,4)+F(1,65536);choices=b.candidates(lo,hi)
    assert len(choices)==1 and (choices[0].n,choices[0].j)==(2,6);p=choices[0];x=p.inverse_cover(lo,hi);v=b.source.evaluate(2,6,m.Jet.variable(x,1));w=v['w'];der=v['wd'];bounds=lambda i:[str(F(float(i.lo))),str(F(float(i.hi)))];out=dict(entry=sha(__file__),primitive=sha(a.primitive),calibration=sha(cal),radius=[str(lo),str(hi)],nativeCell=[2,6],nativeX=bounds(x),slope=bounds(w.c[0]),nativeSlopeDerivative=bounds(der.c[0]),slopeJetDerivative=bounds(w.c[1]));assert bounds(der.c[0])==['0','0'] and bounds(w.c[1])==['0','0'];assert F(out['slope'][0])==F(out['slope'][1])==F(.02)
    with a.out.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps(out))
if __name__=='__main__':main()
