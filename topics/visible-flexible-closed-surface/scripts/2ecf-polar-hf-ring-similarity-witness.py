#!/usr/bin/env python3
"""Exact quotient obstruction for all independent similarities and angular clocks on a physical HF64 ring."""
import argparse
from fractions import Fraction as Q
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import time
for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[k]="1"
import numpy as np
from scipy.interpolate import BSpline
from scipy.optimize import linprog


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def dot(a,b):return sum(x*y for x,y in zip(a,b))

def cross(x,y):return [x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0]]

def real(x):return Q(float(x))

def native_basis(t,kn,s):
    elem=[Q(int(a<=s<b)) for a,b in zip(kn,kn[1:])]
    for p in range(1,t+1):
        prev=elem;elem=[]
        for i in range(len(prev)-1):
            l=kn[i+p]-kn[i];r=kn[i+p+1]-kn[i+1]
            elem.append(((s-kn[i])*prev[i]/l if l else 0)+((kn[i+p+1]-s)*prev[i+1]/r if r else 0))
    return elem

def radial_weights(kn,s):
    b4=native_basis(4,kn,s);b5=native_basis(5,kn,s);d5=[]
    for i in range(len(b5)):
        l=kn[i+5]-kn[i];r=kn[i+6]-kn[i+1]
        d5.append((5*b4[i]/l if l else 0)-(5*b4[i+1]/r if r else 0))
    return b5[3:-3],d5[3:-3]

def channels(n):
    values=[]
    for d in range(3):
        values.append((d,0,0))
        for k in range(1,(n//3-1)//2+1):values.extend(((d,k,0),(d,k,1)))
    assert len(values)==n
    return values

def trig_table(n,tag):
    if tag is None:x,y=Q(-1),Q(0)
    else:
        t=Q(tag);x,y=(1-t*t)/(1+t*t),2*t/(1+t*t)
    a,b=Q(1),Q(0);out=[]
    for i in range(n):out.append((a,b));a,b=a*x-b*y,a*y+b*x
    return out

def exact_row(cf,tr):
    p=[];ps=[];t=[];u2=[]
    for d in range(3):
        r,i=cf[0][d];dr,di=cf[1][d]
        f=[r[k]*a-i[k]*b for k,(a,b) in enumerate(tr)]
        p.append(sum(f));ps.append(sum(dr[k]*a-di[k]*b for k,(a,b) in enumerate(tr)))
        t.append(sum(k*(-r[k]*b-i[k]*a) for k,(a,b) in enumerate(tr)))
        u2.append(-sum(k*k*v for k,v in enumerate(f)))
    g=dot(t,t);projection=dot(t,u2)/g
    kvec=[(v-projection*w)/g for v,w in zip(u2,t)]
    return [*kvec,*cross(p,kvec),dot(p,kvec),Q(1),dot(ps,kvec)]

def determinant(a):
    # Fraction-free Bareiss on integer-scaled rows. Removed denominators recover the exact rational determinant.
    mat=[];den=1
    for row in a:
        l=math.lcm(*(x.denominator for x in row));mat.append([int(l*x) for x in row]);den*=l
    sign=1;old=1;n=len(mat)
    for j in range(n-1):
        k=next((i for i in range(j,n) if mat[i][j]),None)
        if k is None:return Q()
        if k!=j:mat[k],mat[j]=mat[j],mat[k];sign=-sign
        a0=mat[j][j]
        for i in range(j+1,n):
            for h in range(j+1,n):
                numer=mat[i][h]*a0-mat[i][j]*mat[j][h]
                mat[i][h],rest=divmod(numer,old)
                if rest:raise ArithmeticError("Inexact determinant division")
        old=a0
    return Q(sign*mat[-1][-1],den)

def prospect(field,knots,co,ww,tags):
    z=np.asarray(field['physicalW']);wt=field['Wknots'];nb=z.shape[0]
    sp=BSpline(wt,np.eye(len(wt)-6),5)
    mm=[sp(knots,nu=i)[:,3:-3]@z for i in range(2)]
    freq=np.arange(co.shape[2]);ch=channels(z.shape[1]);phase=np.exp(1j*np.array([np.pi if t is None else 2*np.arctan(float(Q(t))) for t in tags])[:,None]*freq)
    best=None
    for i in range(1,len(knots)-1):
        cc=co[i,:2].copy()
        for j,(d,k,kind) in enumerate(ch):
            cc[:,k,d]+=np.array([r[i,j] for r in mm])*(-1j if kind else 1)
        p=(phase@cc[0]).real;v=(phase@cc[1]).real;t=(phase@((1j*freq[:,None])*cc[0])).real
        dd=(phase@((-freq[:,None]**2)*cc[0])).real
        g=np.sum(t*t,axis=1,keepdims=True)
        k=(dd-t*np.sum(dd*t,axis=1,keepdims=True)/g)/g
        a=np.column_stack((k,np.cross(p,k),np.sum(p*k,axis=1),np.ones(len(tags))))
        b=np.sum(v*k,axis=1);ones=-np.ones((len(tags),1))
        lp=linprog(np.r_[np.zeros(8),1],A_ub=np.r_[np.c_[a,ones],np.c_[-a,ones]],b_ub=np.r_[b,-b],
                   bounds=[(None,None)]*8+[(0,None)],method='highs')
        if not lp.success:continue
        dual=lp.ineqlin.marginals[:len(tags)]-lp.ineqlin.marginals[len(tags):]
        ix=np.flatnonzero(abs(dual)>2e-9)
        if len(ix)>9:continue
        if len(ix)<9:
            extra=[j for j in np.argsort(-np.abs(b-a@lp.x[:8])) if j not in ix]
            ix=np.r_[ix,extra[:9-len(ix)]].astype(int)
        if best is None or best[0]<lp.fun:best=(lp.fun,i,ix)
    if best is None:raise ArithmeticError("No witness support")
    return best

def main():
    ap=argparse.ArgumentParser()
    for k in ('field','field-report','output'):ap.add_argument('--'+k,type=Path,required=True)
    args=ap.parse_args();tick=time.monotonic();r=json.loads(args.field_report.read_text())
    if sha(args.field)!=r['fieldSHA256']:raise ValueError("Complete physical field required")
    f=np.load(args.field);knots=f['knots'];co=f['coefficients'];w=f['physicalW']
    tags=list(dict.fromkeys(None if j==40 else str(Q(float(np.tan(np.pi*j/80))).limit_denominator(24)) for j in range(80)))
    bound,i,ix=prospect(f,knots,co,w,tags)
    print("selected physical knot",i,float(knots[i]),"conditional residual",bound,flush=True)
    s=real(knots[i]);rad=radial_weights([real(x) for x in f['Wknots']],s)
    n=co.shape[2];cf=[[[[real(v) for v in co[i,p,:,d].real],[real(v) for v in co[i,p,:,d].imag]] for d in range(3)] for p in range(2)]
    for p in range(2):
        for j,(d,k,b) in enumerate(channels(w.shape[1])):
            delta=sum(real(w[l,j])*x for l,x in enumerate(rad[p]) if x)
            cf[p][d][b][k]+=delta*(-1 if b else 1)
    selected=[tags[j] for j in ix];M=[exact_row(cf,trig_table(n,t)) for t in selected]
    A=[r[:8] for r in M];v=[r[8] for r in M]
    # Exact alternating eight-column minors give a left annihilator; only their ratios matter.
    dual=[(-1)**j*determinant(A[:j]+A[j+1:]) for j in range(9)]
    if not any(dual):raise ArithmeticError("Eight-column rank not proved")
    size=sum(map(abs,dual));dual=[q/size for q in dual]
    if any(sum(dual[j]*A[j][k] for j in range(9)) for k in range(8)):raise ArithmeticError("Failed exact annihilation")
    floor=abs(dot(dual,v))
    assert floor>0
    lower=Q((floor*10**10).__floor__(),10**10)
    # Compact, exact verification: the nine material angles and full input determine all row/minor arithmetic.
    # Only the final downward rational decimal is persisted; arbitrarily long cofactors are never decimal-stringified.
    out=dict(schema='exact-HF64-ring-similarity-radial-curvature-compatibility-witness-v1',
        hfReportSHA256=sha(args.field_report),fieldSHA256=sha(args.field),entrySHA256=sha(__file__),
        physicalRadialKnotIndex=int(i),exactPhysicalS=str(s),halfAngleTangents=selected,
        exactRows=9,exactColumns=8,exactTestRankAugmented=9,eightColumnRank=8,
        l1DualNormalizedExactly=True,allEightDualAnnihilationsExactlyZero=True,
        curvatureResidualLower=str(lower),lowerDisplay=float(lower),normUnit='absolute material normal curvature velocity derivative per material meridian length',
        numericalSearchOnlyForSelectingFixedNineWitnesses=float(bound),seconds=time.monotonic()-tick)
    with args.output.open('x') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out),flush=True)
if __name__=='__main__':main()
