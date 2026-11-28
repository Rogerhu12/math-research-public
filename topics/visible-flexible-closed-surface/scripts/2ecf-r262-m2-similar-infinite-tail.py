#!/usr/bin/env python3
"""Transport the entire original infinite m2 solution by exact similarity; generate its finite observed jets and seam for new external geometry."""
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
import numpy as np
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    p=argparse.ArgumentParser()
    for k in ('source','table','proof','manifest','out','new-table'):p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--scale',type=F,required=True);a=p.parse_args();l=float(a.scale);s=json.loads(a.source.read_bytes());receipt=json.loads(a.proof.read_bytes());assert receipt['slopeJetDerivative']==['0','0'];q=next(x for x in s['finite'][-1]['anchors'] if x['r']==.25);foot=json.loads(a.manifest.read_bytes());c=F(foot['parameters']['rCuff']);new=dict(r=l*q['r'],w=q['w'],wr=q['wr']/l,H=l*q['H'],Hr=q['Hr'],cell=q['cell'],profile=q['profile'],x=q['x'],innerShapePerUnitH=q['innerShapePerUnitH']/l**2)
    with np.load(a.table) as t:d={k:t[k].copy() for k in t.files};d['r']*=l;d['wr']/=l;d['meridian']*=l;d['height']*=l;d['linear']*=np.array([l,l,1,1,1/l,1/l])[:,None];np.savez_compressed(a.new_table,**d)
    out=dict(schema='exact-similarity-of-actual-R262-entire-infinite-m2-tail-finite-observation-table-v1',entry=sha(Path(__file__)),source=sha(a.source),oldTable=sha(a.table),plateau=sha(a.proof),oldManifest=sha(a.manifest),newTable=sha(a.new_table),scale=str(a.scale),exactOldCuff=str(c),exactNewCuff=str(c*a.scale),exactInnerSeam=str(F(1,4)*a.scale),exactPlateau=[str(F(x)*a.scale) for x in receipt['radius']],finite=[dict(anchors=[new])]);
    with a.out.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print(out)
if __name__=='__main__':main()
