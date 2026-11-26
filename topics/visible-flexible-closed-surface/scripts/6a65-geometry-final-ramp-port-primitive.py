#!/usr/bin/env python3
"""Accurate terminal arc, partial-arc primitive, and refined full port bounds.

Consumes the actual full-domain port certificate. No new angular sampling or
port approximation is introduced. The exact small squared-speed residual is
expanded against the exact ellipse, with all Fourier tails paid.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import time
import numpy as np


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def module(p,n):
    s=importlib.util.spec_from_file_location(n,p)
    m=importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def upq(x,bits=192):
    s=1<<bits
    return Q((x.numerator*s+x.denominator-1)//x.denominator,s)


def ellipse_derivative(ellipse,A,B,abox,primitive):
    M=ellipse['terms']
    c=(A+B)/2
    z=(A-B)/(A+B)
    a=[Q(1)]
    b=[Q(1)]
    for n in range(1,M+2):
        a.append(a[-1]*z*Q(2*n-1,2*n))
        b.append(b[-1]*z*Q(2*n-3,2*n))
    def moments(seq):
        S0=sum(map(abs,seq[:M+1]),Q(0))
        S1=sum((n*abs(seq[n]) for n in range(M+1)),Q(0))
        T0=abs(seq[M+1])/(1-z)
        T1=abs(seq[M+1])*(Q(M+1)/(1-z)+z/(1-z)**2)
        return S0,S1,T0,T1
    sa,ma,ta,ua=moments(a)
    sb,mb,tb,ub=moments(b)
    inverse_tail1=4*(ma*ta+sa*ua+ta*ua)/c
    ell_tail1=4*c*(mb*tb+sb*ub+tb*ub)
    amid=Q(primitive.roundq((abox[0]+abox[1])/2,192),1<<192)
    inverse_parameter=max(abs(1/amid-1/abox[0]),abs(1/amid-1/abox[1]))
    inverse_round1=Q(0)
    h_round1=Q(0)
    ell_finite1=Q(0)
    for k in range(1,M+1):
        iv=sum((a[m+k]*a[m] for m in range(M-k+1)),Q(0))/c
        ev=c*sum((b[m+k]*b[m] for m in range(M-k+1)),Q(0))
        ivhat=Q(ellipse['inverse'][2*M+2*k],1<<ellipse['bits'])
        hvhat=Q(ellipse['normalized'][2*M+2*k],1<<ellipse['bits'])
        inverse_round1+=4*k*abs(iv-ivhat)
        h_round1+=4*k*abs(ev/amid-hvhat)
        ell_finite1+=4*k*abs(ev)
    return dict(inverseError1=upq(inverse_tail1+inverse_round1),
        normalizedError1=upq(ell_tail1/abox[0]+ell_finite1*inverse_parameter+h_round1),
        inverseNorm1=upq(4*(sa+ta)*(ma+ua)/c),
        normalizedNorm1=upq(4*c*(sb+tb)*(mb+ub)/abox[0]))


def squared_speed_polynomial(co,si,model,abox,gram):
    D=len(co)-1
    bits=max(gram.dyadic_bits(x/2) for row in co+si for x in row)
    C=[[[[0]*(2*D+1) for unused in range(2)] for unused in range(3)]]
    for d in range(3):
        C[0][d][0][D]=gram.scaled(co[0][d],bits)
        for k in range(1,D+1):
            re=gram.scaled(co[k][d]/2,bits)
            im=gram.scaled(-si[k][d]/2,bits)
            C[0][d][0][D+k]=C[0][d][0][D-k]=re
            C[0][d][1][D+k],C[0][d][1][D-k]=im,-im
    U=gram.angular(C,D)
    maximum=max(abs(x).bit_length() for row in U for pair in row for part in pair for x in part)
    packing=2*maximum+(12*3*(2*D+1)).bit_length()+3
    G=gram.packed_gram(U,U,packing,True)[0]
    pbox=(1+model.v*model.ramp/(2*abox[1]),1+model.v*model.ramp/(2*abox[0]))
    pbits=200
    mid=(pbox[0]+pbox[1])/2
    pmid=Q((2*mid.numerator*(1<<pbits)+mid.denominator)//(2*mid.denominator),1<<pbits)
    delta_p2=max(abs(pmid**2-pbox[0]**2),abs(pmid**2-pbox[1]**2))
    target=[pmid**2*(model.A**2+model.B**2)/2,pmid**2*(model.B**2-model.A**2)/4]
    outbits=max(2*bits,*(gram.dyadic_bits(x) for x in target))
    R=[[x<<(outbits-2*bits) for x in part] for part in G]
    for k,h in ((2*D,target[0]),(2*D-2,target[1]),(2*D+2,target[1])):
        R[0][k]-=gram.scaled(h,outbits)
    return [R],outbits,pbox,delta_p2


def weighted_norm(poly,bits,order):
    D=(len(poly[0][0])-1)//2
    return Q(sum(abs(k)**order*(abs(poly[0][0][k+D])+abs(poly[0][1][k+D])) for k in range(-D,D+1)),1<<bits)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--master',type=Path,required=True)
    ap.add_argument('--coast-master',type=Path,required=True)
    ap.add_argument('--gram-report',type=Path,required=True)
    ap.add_argument('--port-report',type=Path,required=True)
    ap.add_argument('--port-source',type=Path,required=True)
    ap.add_argument('--scripts-dir',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    if args.output.exists():
        raise FileExistsError("Fresh actual terminal primitive certificate required")
    start=time.monotonic()
    pp=args.scripts_dir/'6a65-geometry-ramp-normalization-primitive.py'
    gp=args.scripts_dir/'6a65-geometry-ramp-native-gram-certificate.py'
    hp=args.scripts_dir/'6a65-m12-r137-continuous-domain.py'
    primitive=module(pp,'terminal_arc_primitive')
    gram=module(gp,'terminal_arc_gram')
    cert=module(hp,'terminal_arc_integer')
    port=module(args.port_source,'terminal_full_port_source')
    I=cert.I
    prior=json.loads(args.port_report.read_text())
    if (prior.get('fullAngularDomainCertified') is not True
        or prior['source']['masterSHA256']!=sha(args.master)
        or prior['source']['coastMasterSHA256']!=sha(args.coast_master)
        or prior['source']['gramReportSHA256']!=sha(args.gram_report)
        or prior['source']['entrySHA256']!=sha(args.port_source)):
        raise ValueError("Actual complete same-source port certificate required")
    model=gram.ActualRamp(args.master)
    gr=json.loads(args.gram_report.read_text())
    abox=tuple(map(Q,gr['exactEllipticArcRadiusInterval']))
    f0=I(abox[0],abox[1])+I(model.v*model.ramp/2)
    with np.load(args.coast_master,allow_pickle=False) as c:
        co,si=port.real_curve(c['curve_modes'],c['curve_coefficients'])
    ellipse=primitive.ellipse_fourier(model.A,model.B,abox)
    ed=ellipse_derivative(ellipse,model.A,model.B,abox,primitive)
    r,rbits,pbox,delta_p2=squared_speed_polynomial(co,si,model,abox,gram)
    rnorm=[upq(weighted_norm(r,rbits,j)) for j in range(2)]
    delta_r=[upq(delta_p2*model.A**2),upq(delta_p2*(model.A**2-model.B**2))]
    rfull=[rnorm[j]+delta_r[j] for j in range(2)]
    qmin=I((pbox[0]*model.B)**2-rfull[0]).sqrt().lower()
    R,packing=primitive.real_laurent_product(r,ellipse['inverse'],gram)
    Rbits=rbits+ellipse['bits']
    D=(len(R[0][0])-1)//2
    if R[0][1][D]:
        raise ArithmeticError("Real exact Fourier mean has an imaginary part")
    Rzero=Q(R[0][0][D],1<<Rbits)
    delta_R=upq(delta_r[0]*ellipse['inverseNorm']+rnorm[0]*ellipse['inverseError'])
    delta_R1=upq(delta_r[1]*ellipse['inverseNorm']+delta_r[0]*ed['inverseNorm1']
        +rnorm[1]*ellipse['inverseError']+rnorm[0]*ed['inverseError1'])
    T=[[[x<<ellipse['bits'] for x in part] for part in row] for row in R]
    offset=D-ellipse['degree']
    for k,hk in enumerate(ellipse['normalized']):
        T[0][0][offset+k]-=hk*R[0][0][D]
        T[0][1][offset+k]-=hk*R[0][1][D]
    Tbits=Rbits+ellipse['bits']
    if T[0][0][D] or T[0][1][D]:
        raise ArithmeticError("The exact ellipse-weighted native mean must vanish")
    delta_T=upq((1+ellipse['normalizedNorm'])*delta_R+ellipse['normalizedError']*abs(Rzero))
    delta_T1=upq(delta_R1+ed['normalizedNorm1']*delta_R+ed['normalizedError1']*abs(Rzero))
    Tnorm=[upq(weighted_norm(T,Tbits,j)) for j in range(2)]
    weighted=upq(primitive.primitive_bernstein_l1(T,Tbits,Q(1)))
    bmin=pbox[0]*model.B
    pmin,pmax=pbox
    curve=port.Fourier(co,si,cert)
    gamma_bounds=[sum(row,Q(0)) for row in curve.absolute[:4]]
    qprime=gamma_bounds[2]
    qsecond=gamma_bounds[2]**2/qmin+gamma_bounds[3]
    ellprime=(model.A**2-model.B**2)/(2*model.B)
    bprime=pmax*ellprime
    remainder0=upq(rfull[0]**2/(2*bmin*(qmin+bmin)**2))
    remainder1=upq(rfull[0]*rfull[1]/(bmin*(qmin+bmin)**2)
        +rfull[0]**2*(bprime/(2*bmin**2*(qmin+bmin)**2)
        +(qprime+bprime)/(bmin*(qmin+bmin)**3)))
    mean=I(Rzero-delta_R,Rzero+delta_R)/(2*I(pmin,pmax))+I(-remainder0,0)
    old_arc=prior['sharpenedAccurateRawArc']
    arc0=f0+mean
    arc=I(max(arc0.lower(),Q(old_arc['lo'])),min(arc0.upper(),Q(old_arc['hi'])))
    hsup=model.A/abox[0]
    hprime=ellprime/abox[0]
    zero_speed=upq((Tnorm[0]+delta_T)/(2*pmin)+(1+hsup)*remainder0)
    zero_speed1=upq((Tnorm[1]+delta_T1)/(2*pmin)+remainder1+hprime*remainder0)
    primitive_bound=upq((weighted+delta_T)/pmin+cert.pi_interval().upper()*(1+hsup)*remainder0)
    angle=upq(primitive_bound/qmin)
    angle1=upq((zero_speed+qprime*angle)/qmin)
    angle2=upq((zero_speed1+qsecond*angle+(2*angle1+angle1**2)*qprime)/qmin)
    delta_a=Q(mean.absupper(),cert.SCALE)
    alpha_error=upq(delta_a/arc.lower())
    alpha_max=1+alpha_error
    P0=model.port(16)[0]
    oldD=model.degree
    scale=1<<model.input_bits
    P_same=[]
    for j in range(3):
        value=Q(0)
        for d in range(3):
            if j==0:
                value+=abs(co[0][d]-Q(P0[d][0][oldD],scale))
            for k in range(1,oldD+1):
                a=co[k][d] if k<len(co) else Q(0)
                b=si[k][d] if k<len(si) else Q(0)
                value+=k**j*(abs(a-Q(2*P0[d][0][oldD+k],scale))
                    +abs(b+Q(2*P0[d][1][oldD+k],scale)))
        centerfree=gamma_bounds[j]-(sum(map(abs,co[0]),Q(0)) if j==0 else 0)
        P_same.append(upq(value+alpha_error*centerfree))
    complete={}
    for name in ('P','V','A'):
        source=P_same if name=='P' else [Q(x['rational']) for x in prior['sameNativeAnglePortDerivativeBounds'][name]]
        deriv=[alpha_max*x for x in gamma_bounds] if name=='P' else [Q(x['rational']) for x in prior['actualCoastPortGlobalNativeDerivativeBounds'][name]]
        complete[name]=[
            upq(source[0]+deriv[1]*angle),
            upq(source[1]+deriv[2]*angle+deriv[1]*angle1),
            upq(source[2]+deriv[3]*angle+deriv[2]*(2*angle1+angle1**2)+deriv[1]*angle2)]
    values=dict(squaredSpeedResidual=rfull[0],squaredSpeedResidualDerivative=rfull[1],
        inverseEllDerivativeApproximationError=ed['inverseError1'],
        normalizedEllDerivativeApproximationError=ed['normalizedError1'],
        RapproximationError=delta_R,RDerivativeApproximationError=delta_R1,
        TapproximationError=delta_T,TDerivativeApproximationError=delta_T1,
        nonlinearSpeedRemainder=remainder0,nonlinearSpeedDerivativeRemainder=remainder1,
        exactZeroMeanSpeed=zero_speed,exactZeroMeanSpeedDerivative=zero_speed1,
        exactPartialArcPrimitive=primitive_bound,
        thetaDifference=angle,firstDerivativeMinusOne=angle1,secondDerivative=angle2,
        alphaMinusOne=alpha_error)
    out=dict(schema='6a65-actual-terminal-accurate-arc-and-native-mean-primitive-port-refinement-v1',
        source=dict(masterSHA256=sha(args.master),coastMasterSHA256=sha(args.coast_master),
            gramReportSHA256=sha(args.gram_report),completePortReportSHA256=sha(args.port_report),
            completePortSourceSHA256=sha(args.port_source),primitiveSourceSHA256=sha(pp),
            gramCheckerSHA256=sha(gp),integerArithmeticSHA256=sha(hp),entrySHA256=sha(__file__)),
        completeInputPortDomainAlreadyCertified=True,allSavedCoefficientsConsumed=True,
        exactTargetDefinition=prior['exactTargetDefinition'],exactTargetRadius=f0.display(),
        exactPerimeterDifferenceFromTarget=mean.display(),accurateRawArc=arc.display(),
        exactNativeSquaredSpeedResidualFourierDegree=190,ellipseTerms=64,
        weightedPrimitiveFourierDegree=D,meanFreeConstantExactlyZero=True,
        numericalQuadratureUsed=False,sourceCurveChanged=False,
        sameNativeAnglePositionBounds=[gram.upper(x) for x in P_same],
        bounds={key:gram.upper(value) for key,value in values.items()},
        actualCentralAngleCompletePortDerivativeBounds={key:[gram.upper(x) for x in val] for key,val in complete.items()},
        fullAngularDomainCertified=True,finalHermiteCellCertified=False,
        wholeRampCertified=False,exactIsometryClaimed=False,wholeClosedReachCertified=False,
        seconds=time.monotonic()-start,OSExitCode=None,externalExitReceiptRequired=True)
    args.output.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(event='actual-terminal-primitive-refinement',
        reportSHA256=sha(args.output),arc=out['accurateRawArc'],
        mean=out['exactPerimeterDifferenceFromTarget'],bounds=out['bounds'],
        completePort=out['actualCentralAngleCompletePortDerivativeBounds'],seconds=out['seconds'])),flush=True)


if __name__=='__main__':
    main()

