#!/usr/bin/env python3
"""Every-material-angle endpoint chord length for the actual R267 prefix and both exact R273/R282 port rectangles."""
import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def run(args):
    path=args.scripts/'6a65-m12-r137-continuous-domain.py'
    sp=importlib.util.spec_from_file_location('true_chord_int',path);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
    I=m.I
    assert sha(args.ramp)=='6f06a6a54577e81b08d4e46339d457506a211da8a4d1eb2a25bc0191bf4234a1'
    with np.load(args.ramp) as d:A,B=[I(Q.from_float(float(d[k]))) for k in ('centralA','centralB')]
    pi=m.pi_interval();step=pi/(2*args.cells)
    nodes=[m.sincos(k*step) for k in range(args.cells+1)]
    # Speed is nondecreasing in native first-quadrant angle. Exact arclength inferred by Riemann brackets.
    ell=[((A*s).square()+(B*c).square()).sqrt() for s,c in nodes]
    prefix=[I(0)]
    for left,right in zip(ell,ell[1:]):
        prefix.append(prefix[-1]+I.raw(left.lo,right.hi)*step)
    a0=prefix[-1]*2/pi
    limit=Q(0);where=0;receipt=hashlib.sha256()
    edge_height=Q(83,200);h0=Q(18078,100000);h1=Q(18175,100000)
    gap=I(edge_height-Q(28,1000)-h1,edge_height+Q(108901,1000000)-h0)
    dx0=I(-Q(112,10000),Q(112,10000))
    cmin=Q(13,25);amax=Q(85,100)
    for j in range(args.cells):
        s0,c0=nodes[j];s1,c1=nodes[j+1]
        s=m.hull(s0,s1);c=m.hull(c0,c1)
        ul=prefix[j]/a0;ur=prefix[j+1]/a0
        ls,lc=m.sincos(ul);rs,rc=m.sincos(ur)
        # True material u is in [0,pi/2]. Evaluating interval endpoints around
        # a true quadrant can encompass the maximum at pi/2; clip that last region explicitly.
        sinu=I.raw(max(0,ls.lo),m.SCALE if ur.hi>=pi.lo//2 else max(ls.hi,rs.hi))
        cosu=I.raw(0 if ur.hi>=pi.lo//2 else max(0,min(lc.lo,rc.lo)),min(m.SCALE,max(lc.hi,rc.hi)))
        x0=A*c+dx0;y0=B*s+dx0
        x1=Q(4,5)*cosu;y=Q(4,5)*sinu
        y1=I(y.lower()-max(Q(0),y.upper()-cmin)*amax**2/2,y.upper())
        v=((x1-x0).square()+(y1-y0).square()+gap.square()).sqrt()
        receipt.update(f'{j} {v.upper()}\n'.encode())
        if v.upper()>limit:limit,where=v.upper(),j
    b=Q.from_float(.1815625);S=Q.from_float(.9772364498716914);L=S-b
    assert limit<Q(18,25) and L>Q(79,100)
    out=dict(sourceSHA256=sha(__file__),intervalSHA256=sha(path),rampSHA256=sha(args.ramp),coastBoundaryGraphSHA256=sha(args.graph),newPortBudgetSHA256=sha(args.new_budget),cells=args.cells,A=str(A.lower()),B=str(B.lower()),ellipseTrueMeanRadius=a0.display(),upperBoundOnAllMaterialChords=str(limit),worstNativeCell=where,actualConnectorLength=str(L),minimumLengthSlack=str(L-limit),maximumRequiredNormalizedMean=str(limit/L),allBoundsSHA256=receipt.hexdigest(),portFamilies=['all R273','all R282'])
    graph=json.loads(args.graph.read_text());g=json.loads(args.new_budget.read_text())
    assert Q(graph['exactLower']['height'])>h0 and Q(graph['exactUpper']['height'])<h1 and Q(g['minimumH'])>=-Q(28,1000) and Q(g['maximumH'])<Q(108901,1000000)
    with args.output.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print(float(limit),float(L-limit),float(limit/L),where,flush=True)
if __name__=='__main__':
    a=argparse.ArgumentParser()
    for k in ('scripts','ramp','graph','new-budget','output'):a.add_argument('--'+k,type=Path,required=True)
    a.add_argument('--cells',type=int,default=384)
    run(a.parse_args())
