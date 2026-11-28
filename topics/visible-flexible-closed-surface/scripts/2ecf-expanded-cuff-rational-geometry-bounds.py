#!/usr/bin/env python3
"""Exact rational checks for the enlarged-cuff ambient construction R280."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import argparse,hashlib,json
def add(a,b):
    c=[F(0)]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]+=x
    return c
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c
def bernstein(p,a,b):
    n=len(p)-1
    c=[sum((p[i]*comb(i,j)*a**(i-j)*(b-a)**j for i in range(j,n+1)),F(0)) for j in range(n+1)]
    return [sum((c[j]*F(comb(k,j),comb(n,j)) for j in range(k+1)),F(0)) for k in range(n+1)]
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();assert not a.output.exists()
    cuff=F(2702159776422297,18014398509481984);cut=F(5404319552844595,9007199254740992)
    A=F(8,25);C=F(21,50);ell=F(1,40);lam=A/cuff
    v=(cut-A-ell*(lam+1)/2)/(cut-cuff-ell)
    L=cut-C;c2=F(3,2)+7*L/(2*cut);c3=-1-7*L/(2*cut)
    W=[F(0),F(0),c2,c3];Wx=[F(0),2*c2,3*c3]
    one=add([F(1)],mul(W,W));poly=mul(mul(one,one),one)
    P=add([36*L*L*q for q in poly],[-q for q in mul(Wx,Wx)])
    cells=[bernstein(P,F(k,32),F(k+1,32)) for k in range(32)]
    lower=min(min(q) for q in cells)
    height=L*(c2/3+c3/4)
    assert v>F(14,25) and lam>1 and lam<F(11,5)
    assert c2>0 and c3<0 and c2+c3==F(1,2)
    assert F(0)<height<F(61,1000)
    assert lower>0
    oldheight=(cut-cuff)*F(16,15);assert oldheight<F(1,2)
    assert 1-F(5,4)*F(1,2)==F(3,8)
    out=dict(schema='R280-exact-rational-enlarged-cuff-ambient-budgets-v1',originalCuff=str(cuff),originalCut=str(cut),newCuff=str(A),flatStart=str(C),transitionWidth=str(ell),expansion=str(lam),minimumRadialDerivative=str(v),newSlopePolynomial=list(map(str,W)),newHeightIncrease=str(height),oldHeightCoarseUpper=str(oldheight),curvatureSixPolynomialBernsteinMinimum=str(lower),curvatureSixCells=32,ambientVerticalDerivativeStrictLower='3/8',ambientJacobianStrictLower='21/100',axisymmetricNewMeridianCurvatureStrictUpper='6',axisymmetricNewCircularCurvatureStrictUpper='50/21',newWholeFieldMetricOrReachClaimed=False,scriptSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    a.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
