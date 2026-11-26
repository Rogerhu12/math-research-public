#!/usr/bin/env python3
"""Exact Fourier/Bernstein Gram bounds for the first 15 actual ramp cells.

All 768 saved Fourier modes are consumed. A declared low part is convolved
exactly by integer Kronecker packing; every remaining coefficient is retained
through weighted exact l1 Bernstein bounds. This certifies the raw native
theta field, not the last exact-coast repair cell, an ODE, or normalization.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import numpy as np


H2 = ((2,0,0,-20,30,-12), (0,2,0,-12,16,-6), (0,0,1,-3,3,-1),
      (0,0,0,20,-30,12), (0,0,0,-8,14,-6), (0,0,0,1,-2,1))
JCOEFF = {6:Q(21),7:Q(-60),8:Q(135,2),9:Q(-35),10:Q(7)}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def dyadic_bits(q):
    d=q.denominator
    if d & (d-1):
        raise ArithmeticError("An exact dyadic coefficient was required")
    return d.bit_length()-1


def scaled(q,bits):
    return q.numerator << (bits-dyadic_bits(q))


def upper(q,bits=96):
    if q<0:
        raise ValueError("Nonnegative bound required")
    den=1 << bits
    val=Q((q.numerator*den+q.denominator-1)//q.denominator,den)
    return dict(rational=str(val), display=float(val))


def pack(row,bits):
    result=0
    for value in reversed(row):
        result=(result << bits)+value
    return result


def unpack(value,bits,count):
    radix=1 << bits
    mask=radix-1
    half=radix >> 1
    out=[]
    for _ in range(count):
        digit=value & mask
        if digit>=half:
            digit-=radix
        out.append(digit)
        value=(value-digit) >> bits
    if value:
        raise ArithmeticError("Kronecker packing overflow or incorrect length")
    return out


def cmul(a,b):
    p=a[0]*b[0]
    q=a[1]*b[1]
    return p-q,(a[0]+a[1])*(b[0]+b[1])-p-q


def convolution_fixture():
    ar,ai=[-7,2,0,-3,11],[5,-2,9,1,-4]
    br,bi=[3,-8,4],[-1,6,2]
    bits=20
    packed=cmul((pack(ar,bits),pack(ai,bits)),(pack(br,bits),pack(bi,bits)))
    got=[unpack(x,bits,len(ar)+len(br)-1) for x in packed]
    want=[[0]*(len(ar)+len(br)-1) for _ in range(2)]
    for i in range(len(ar)):
        for j in range(len(br)):
            want[0][i+j]+=ar[i]*br[j]-ai[i]*bi[j]
            want[1][i+j]+=ar[i]*bi[j]+ai[i]*br[j]
    if got!=want:
        raise ArithmeticError("Independent signed-complex convolution fixture failed")
    return True


def derivative(poly,order):
    out=poly
    for _ in range(order):
        out=[[[ (j+1)*x for x in channel] for channel in out[j+1]] for j in range(len(out)-1)]
    return out


def bernstein_l1(poly,bits,physical_length=Q(1),order=0):
    """poly[radial power][real/imag][Fourier index], exact common 2^bits."""
    p=derivative(poly,order)
    degree=len(p)-1
    denominator=math.lcm(*(math.comb(degree,j) for j in range(degree+1)))
    width=len(p[0][0])
    largest=0
    for i in range(degree+1):
        row=[[0]*width,[0]*width]
        for j in range(i+1):
            weight=math.comb(i,j)*(denominator//math.comb(degree,j))
            for part in range(2):
                for k,value in enumerate(p[j][part]):
                    row[part][k]+=weight*value
        largest=max(largest,sum(abs(v) for part in row for v in part))
    return Q(largest,denominator*(1 << bits))/physical_length**order


def vector_bernstein_l1(poly,bits,L,order=0,indices=None):
    """Coordinate l1 dominates vector norm; no omitted Fourier coefficient."""
    maximum=Q(0)
    degree=len(poly)-1-order
    denominator=math.lcm(*(math.comb(degree,j) for j in range(degree+1)))
    width=len(poly[0][0][0])
    choose=range(width) if indices is None else indices
    for i in range(degree+1):
        total=0
        for d in range(3):
            for part in range(2):
                for k in choose:
                    value=0
                    for j in range(i+1):
                        falling=math.factorial(j+order)//math.factorial(j)
                        value+=poly[j+order][d][part][k]*falling*math.comb(i,j)*(denominator//math.comb(degree,j))
                    total+=abs(value)
        maximum=max(maximum,Q(total,denominator*(1 << bits))/L**order)
    return maximum


class ActualRamp:
    def __init__(self,master):
        with np.load(master,allow_pickle=False) as a:
            self.sx=a['sx'].copy()
            self.raw=a['coefficients'].copy()
            self.wave=a['wave'].copy()
            self.A,self.B,self.c,self.ramp,self.v,self.a0=(Q.from_float(float(a[key])) for key in
                ('centralA','centralB','centralLength','ramp','v','a0'))
        if self.raw.shape!=(17,768,3,3) or self.sx.shape!=(17,):
            raise ValueError("Actual 17-node/768-mode complete P,V,A master required")
        if set(map(int,self.wave))!=set(range(-384,384)) or not np.all(self.wave==np.round(self.wave)):
            raise ValueError("Actual full native Fourier index set required")
        if not np.all(np.isfinite(self.raw)):
            raise ValueError("Finite complete saved coefficients required")
        if self.ramp!=Q.from_float(.06) or self.v!=Q.from_float(.045):
            raise ValueError("Actual new coupled-gap prefix parameters required")
        self.degree=384
        self.index={int(k):j for j,k in enumerate(self.wave)}
        raw_bits=max(dyadic_bits(Q.from_float(float(value))) for part in (self.raw.real,self.raw.imag) for value in part.ravel())
        # One extra bit pays exact real-part pairing of unequal complex halves.
        self.input_bits=max(raw_bits,dyadic_bits(self.A),dyadic_bits(self.B),dyadic_bits(self.c))+1
        self.port_cache={}

    def port(self,node):
        if node in self.port_cache:
            return self.port_cache[node]
        D=self.degree
        result=[[[[0]*(2*D+1) for _ in range(2)] for _ in range(3)] for _ in range(3)]
        if node==0:
            # The actual WarmMaster overrides the saved initial FFT by this port.
            result[0][0][0][D-1]=result[0][0][0][D+1]=scaled(self.A/2,self.input_bits)
            result[0][1][1][D-1]=scaled(self.B/2,self.input_bits)
            result[0][1][1][D+1]=-scaled(self.B/2,self.input_bits)
            result[0][2][0][D]=scaled(self.c,self.input_bits)
            result[1][2][0][D]=1 << self.input_bits
        else:
            for p in range(3):
                for d in range(3):
                    result[p][d][0][D]=scaled(Q.from_float(float(self.raw[node,self.index[0],p,d].real)),self.input_bits)
                    for k in range(1,D+1):
                        positive=self.raw[node,self.index[k],p,d] if k in self.index else 0j
                        negative=self.raw[node,self.index[-k],p,d] if -k in self.index else 0j
                        re=(Q.from_float(float(positive.real))+Q.from_float(float(negative.real)))/2
                        im=(Q.from_float(float(positive.imag))-Q.from_float(float(negative.imag)))/2
                        r,j=scaled(re,self.input_bits),scaled(im,self.input_bits)
                        result[p][d][0][D+k]=result[p][d][0][D-k]=r
                        result[p][d][1][D+k],result[p][d][1][D-k]=j,-j
        self.port_cache[node]=result
        for old in list(self.port_cache):
            if old<node-1:
                del self.port_cache[old]
        return result

    def cell(self,index):
        if not 0<=index<15:
            raise ValueError("The exact-coast nonpolynomial final cell is excluded")
        left,right=self.port(index),self.port(index+1)
        sx0=Q.from_float(float(self.sx[index]))
        L=Q.from_float(float(self.sx[index+1]))-sx0
        # Sterbenz subtraction is exact for these saved cell endpoints.
        if Q.from_float(float(self.sx[index+1]-self.sx[index]))!=L:
            raise ArithmeticError("Saved physical cell-length subtraction is not exact")
        lb=dyadic_bits(L)
        bits=self.input_bits+2*lb+1
        ports=[left[0],left[1],left[2],right[0],right[1],right[2]]
        factors=[1 << (bits-self.input_bits),
                 L.numerator << (bits-self.input_bits-lb),
                 L.numerator**2 << (bits-self.input_bits-2*lb)]*2
        out=[]
        for j in range(6):
            row=[]
            for d in range(3):
                pair=[]
                for part in range(2):
                    values=[]
                    for k in range(2*self.degree+1):
                        numerator=sum(H2[p][j]*factors[p]*ports[p][d][part][k] for p in range(6))
                        if numerator%2:
                            raise ArithmeticError("Exact quintic coefficient was not dyadic at the selected scale")
                        values.append(numerator//2)
                    pair.append(values)
                row.append(pair)
            out.append(row)
        return out,bits,L,sx0


def angular(poly,degree):
    return [[[[(-k)*p[d][1][k+degree] for k in range(-degree,degree+1)],
               [k*p[d][0][k+degree] for k in range(-degree,degree+1)]] for d in range(3)] for p in poly]


def radial_t(poly):
    return [[[[ (j+1)*x for x in part] for part in poly[j+1][d]] for d in range(3)]
            for j in range(len(poly)-1)]


def select(poly,indices):
    return [[[[part[k] for k in indices] for part in row] for row in p] for p in poly]


def packed_gram(a,b,bits,square=False):
    pa=[[(pack(row[0],bits),pack(row[1],bits)) for row in p] for p in a]
    pb=pa if square else [[(pack(row[0],bits),pack(row[1],bits)) for row in p] for p in b]
    out=[[0,0] for _ in range(len(a)+len(b)-1)]
    for i in range(len(a)):
        for j in range(i if square else 0,len(b)):
            factor=2 if square and i!=j else 1
            for d in range(3):
                re,im=cmul(pa[i][d],pb[j][d])
                out[i+j][0]+=factor*re
                out[i+j][1]+=factor*im
    count=len(a[0][0][0])+len(b[0][0][0])-1
    return [[unpack(part,bits,count) for part in row] for row in out]


def target_ratio(sx0,L,ramp,v,a0box,bits=200):
    qlo,qhi=v*ramp/a0box[1],v*ramp/a0box[0]
    qmid=(qlo+qhi)/2
    exact=[Q(0)]*11
    exact[0]=1
    J=[Q(0)]*11
    for n,coef in JCOEFF.items():
        for j in range(n+1):
            J[j]+=coef*math.comb(n,j)*sx0**(n-j)*L**j/ramp**n
    for j in range(11):
        exact[j]+=qmid*J[j]
    scale=1 << bits
    rounded=[(2*x.numerator*scale+x.denominator)//(2*x.denominator) for x in exact]
    errors=[]
    globals_J=[Q(1,2),1/ramp,Q(630,256)/ramp**2]
    for r in range(3):
        error=sum(abs(exact[j]-Q(rounded[j],scale))*(math.factorial(j)//math.factorial(j-r))
                  for j in range(r,11))/L**r
        error+=(qhi-qlo)/2*globals_J[r]
        errors.append(error)
    bounds=[1+qhi/2,qhi/ramp,qhi*Q(630,256)/ramp**2]
    return rounded,bits,errors,bounds


def check_cell(model,index,cutoff,a0box):
    C,bits,L,sx0=model.cell(index)
    T=radial_t(C)
    U=angular(C,model.degree)
    low=list(range(model.degree-cutoff,model.degree+cutoff+1))
    high=list(range(0,model.degree-cutoff))+list(range(model.degree+cutoff+1,2*model.degree+1))
    lowT,lowU=select(T,low),select(U,low)
    maximum=max(abs(x).bit_length() for poly in (lowT,lowU) for row in poly for pair in row for part in pair for x in part)
    # Covers all coordinate/radial-pair sums in a single packed coefficient.
    operations=12*3*max(len(lowT),len(lowU))*(2*cutoff+1)
    packing_bits=2*maximum+operations.bit_length()+3
    E=packed_gram(lowT,lowT,packing_bits,True)
    F=packed_gram(lowT,lowU,packing_bits)
    G=packed_gram(lowU,lowU,packing_bits,True)
    center=2*cutoff
    E[0][0][center]-=scaled(L*L,2*bits)
    q,qbits,target_error,target_bound=target_ratio(sx0,L,model.ramp,model.v,a0box)
    sq=[sum(q[j]*q[n-j] for j in range(max(0,n-10),min(10,n)+1)) for n in range(21)]
    h0=(model.A**2+model.B**2)/2
    h2=(model.B**2-model.A**2)/4
    hbits=max(dyadic_bits(h0),dyadic_bits(h2))
    gbits=max(2*bits,2*qbits+hbits)
    shift=gbits-2*bits
    G=[[[x << shift for x in part] for part in row] for row in G]
    G.extend([[[0]*len(G[0][0]) for _ in range(2)] for _ in range(21-len(G))])
    for j in range(21):
        for k,h in ((center,h0),(center-2,h2),(center+2,h2)):
            G[j][0][k]-=sq[j]*scaled(h,hbits)*(1 << (gbits-(2*qbits+hbits)))
    Ms=vector_bernstein_l1(T,bits,L,indices=low)/L
    ds=vector_bernstein_l1(T,bits,L,indices=high)/L
    Mu=[vector_bernstein_l1(U,bits,L,r,low) for r in range(3)]
    du=[vector_bernstein_l1(U,bits,L,r,high) for r in range(3)]
    E_low=bernstein_l1(E,2*bits)/L**2
    F_low=bernstein_l1(F,2*bits)/L
    E_tail=2*Ms*ds+ds**2
    F_tail=Ms*du[0]+Mu[0]*ds+ds*du[0]
    G_low=[]
    G_tail=[]
    G_target=[]
    for r in range(3):
        G_low.append(bernstein_l1(G,gbits,L,r))
        G_tail.append(sum(math.comb(r,j)*(Mu[j]*du[r-j]+du[j]*Mu[r-j]+du[j]*du[r-j]) for j in range(r+1)))
        G_target.append(model.A**2*sum(math.comb(r,j)*target_error[j]*(2*target_bound[r-j]+target_error[r-j]) for j in range(r+1)))
    Ebound,Fbound=E_low+E_tail,F_low+F_tail
    Gbound=[a+b+c for a,b,c in zip(G_low,G_tail,G_target)]
    metric=max(Ebound,Gbound[0]/model.B**2)+Fbound/model.B
    row=dict(index=index,relativePhysicalDomain=[str(sx0),str(sx0+L)],physicalLength=str(L),
        positionDyadicBits=bits,packingBits=packing_bits,lowFourierCutoff=cutoff,fullRealFourierDegree=model.degree,
        weightedHighFrequencyBounds=dict(Xs=upper(ds),Xtheta=upper(du[0]),Xstheta=upper(du[1]),Xsstheta=upper(du[2])),
        lowPartVectorBounds=dict(Xs=upper(Ms),Xtheta=upper(Mu[0])),
        exactLowGramBounds=dict(Eminus1=upper(E_low),F=upper(F_low),GminusTarget=[upper(x) for x in G_low]),
        highFrequencyGramContributions=dict(Eminus1=upper(E_tail),F=upper(F_tail),GminusTarget=[upper(x) for x in G_tail]),
        targetParameterAndDyadicEnclosureContributions=[upper(x) for x in G_target],
        completeRawNativeGramBounds=dict(Eminus1=upper(Ebound),F=upper(Fbound),GminusTarget=[upper(x) for x in Gbound],
            normalizedF=upper(Fbound/model.B),relativeG=upper(Gbound[0]/model.B**2),spectralRelativeMetric=upper(metric)),
        retainedAllSavedHighFrequencies=True,polynomialCellProvedContinuously=True)
    return row,metric


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--master',type=Path,required=True)
    ap.add_argument('--scripts-dir',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--cutoff',type=int,default=95)
    ap.add_argument('--cell',type=int,action='append')
    ap.add_argument('--threshold',default='1/1000000')
    args=ap.parse_args()
    if args.output.exists():
        raise FileExistsError('Fresh exact certificate output required')
    if not 2<=args.cutoff<=384:
        raise ValueError('Declared real Fourier cutoff in [2,384] required')
    start=time.monotonic()
    fixture=convolution_fixture()
    model=ActualRamp(args.master)
    budget_path=args.scripts_dir/'6a65-geometry-central-gap-held-budget.py'
    spec=importlib.util.spec_from_file_location('actual_ramp_ellipse_perimeter_box',budget_path)
    budget=importlib.util.module_from_spec(spec);spec.loader.exec_module(budget)
    pell=budget.perimeter_over_pi(model.A,model.B,terms=32)
    ellipse_box=(pell[0]/2,pell[1]/2)
    # Include the finite consumer scalar as well as the exact integral radius.
    a0box=(min(ellipse_box[0],model.a0),max(ellipse_box[1],model.a0))
    selected=list(range(15)) if args.cell is None else args.cell
    if not selected or any(type(j) is not int or j<0 or j>=15 for j in selected) or len(set(selected))!=len(selected):
        raise ValueError('Distinct actual polynomial cell indices 0..14 required')
    input_sha=sha(args.master)
    rows=[];worst=Q(0)
    for j in selected:
        row,metric=check_cell(model,j,args.cutoff,a0box)
        row['passedThreshold']=metric<Q(args.threshold)
        worst=max(worst,metric);rows.append(row)
        print(json.dumps(dict(event='exact-native-gram-cell',index=j,
            spectralRelativeMetric=upper(metric),weightedHighFrequencyBounds=row['weightedHighFrequencyBounds'],
            passedThreshold=row['passedThreshold'],seconds=time.monotonic()-start)),flush=True)
    if sha(args.master)!=input_sha:
        raise RuntimeError('Actual master changed during the proof')
    complete=selected==list(range(15))
    out=dict(schema='6a65-actual-coupled-gap-first15-raw-native-ramp-Fourier-Bernstein-Gram-v1',
        source=dict(masterSHA256=input_sha,entrySHA256=sha(__file__),perimeterSourceSHA256=sha(budget_path)),
        actualSourceArrayShape=list(model.raw.shape),savedWaveRange=[-384,383],
        realPartCurveDegree=384,allSavedCoefficientsConsumed=True,lowFourierCutoff=args.cutoff,
        originalShapeODEModeCountIsNotPositionCutoff=True,
        nativeTargetMetric='ds^2+(f(s)/a_ellipse)^2*(A^2 sin(theta)^2+B^2 cos(theta)^2) dtheta^2',
        centralAExactDyadic=str(model.A),centralBExactDyadic=str(model.B),
        exactEllipticArcRadiusInterval=[str(x) for x in ellipse_box],
        targetRadiusIntervalAlsoIncludesFiniteConsumerA0=True,
        targetRatioEnclosure='each local polynomial coefficient rounded to 2^-200, with exact coefficient and radius-parameter error bounds',
        firstPortIsExplicitExactCentralCylinder=True,
        lastCoastRepairCellExcluded=True,certifiedCellIndices=selected,
        integerSignedComplexConvolutionFixturePassed=fixture,
        allFirst15PolynomialCellsProved=complete and all(r['passedThreshold'] for r in rows),
        threshold=args.threshold,wholeCertifiedPartSpectralRelativeMetric=upper(worst),rows=rows,
        rawNativeFieldOnly=True,normalizedFieldCertified=False,curvatureCertified=False,
        ODEErrorCertified=False,wholeRampCertified=False,wholeClosedSurfaceCertified=False,
        seconds=time.monotonic()-start,OSExitCode=None,externalExitReceiptRequired=True)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(event='exact-native-gram-complete',reportSHA256=sha(args.output),
        allFirst15PolynomialCellsProved=out['allFirst15PolynomialCellsProved'],
        spectralRelativeMetric=upper(worst),seconds=out['seconds'])),flush=True)
    if not all(r['passedThreshold'] for r in rows):
        raise SystemExit(2)


if __name__=='__main__':
    main()
