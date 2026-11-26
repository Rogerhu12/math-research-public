#!/usr/bin/env python3
"""R237 exact-form compact-window angular-speed lower bound.

This pays the mathematical natural-perimeter inverse for the explicitly
bound zero-coefficient Cauchy source plus the R233 accurate prefix.
It does not transfer the bound to a literal rounded oracle evaluation or
to any later Cartesian-corrected field. All decisions use rational/I96
bounds, including both exact central ellipse perimeter integrals.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np

HASHES={
 "initial":"1e3ae25e984fd4ac166022644cb5cbc248976e749ca391859d08ac1d45a7aced",
 "baseline":"f0d8a17bb512632e8e57ba2802be378e6f7ee6867251055a842f3d535d9e5cff",
 "ramp":"0e2865ed7fd2fa5e1061718cc96b8be691f5f7d1a5b9460cf11d564d799f38e7",
 "raw":"c8f43da932ec21d9925e358b1a025c1e38df067a4ed96e3384d9eeb6c53af48e",
 "primitive":"fa374672e0c876b618b24980472d438ab59832476a0eba49f802388216c69881",
 "last":"9e16f7da5211c425b1fb8d6414e521c99f57d40f7c5cdf8b465a55b974c1ad24",
 "coast":"88b4cc19139143fdb1e85f446750f3daea70d978a139171702bb3fe6381adc89",
 "outlet":"ec0e8c0de4d2841fbb5775990cff71838f806ed776c0fbd4b3a8ba1e3cebe295"
}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def load(p,n):
    sp=importlib.util.spec_from_file_location(n,p)
    m=importlib.util.module_from_spec(sp)
    sys.modules[n]=m
    sp.loader.exec_module(m)
    return m


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--scripts",type=Path,required=True)
    p.add_argument("--work",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args()
    if args.output.exists():
        raise FileExistsError("Fresh exact-form window certificate required")
    started=time.monotonic()
    names=dict(initial="gap105-window-ownzero01-initial.json",
        baseline="gap105-window-ownzero-fullvalue01-report.json",
        ramp="gap105-v045-prefix-replay03-ramp-master.npz",
        raw="gap105-native-curvature-replay03-report.json",
        primitive="gap105-normalization-primitive-first15-01-report.json",
        last="gap105-final-cell-entire01-report.json",
        coast="gap105-final-port-entire01-report.json",
        outlet="gap105-coast-outlet-derivative01-report.json")
    for key,name in names.items():
        if sha(args.work/name)!=HASHES[key]:
            raise ValueError("Actual bound source/certificate changed: "+key)
    data={k:json.loads((args.work/n).read_text()) for k,n in names.items() if k!="ramp"}
    cert=load(args.scripts/"6a65-m12-r137-continuous-domain.py","window_q_integer")
    I=cert.I
    pi=cert.pi_interval()
    upper=lambda x:I.raw(x.hi,x.hi)
    absolute=lambda x:I.raw(x.absupper(),x.absupper())
    record=lambda x:dict(lo=str(x.lower()),hi=str(x.upper()),display=x.display())
    value=lambda x:I(Q(x["rational"]))
    bound=lambda x:I(Q(x["lo"]),Q(x["hi"]))
    saved=data["initial"]
    z=saved["z"]
    if len(z)!=1788 or any(x!=0 for j,x in enumerate(z) if j not in (874,1787)):
        raise ValueError("Only this actual zero-free-coefficient source is certified")
    source=data["baseline"]["source"]
    if source["originalSource"]["sourceStateSHA256"]!=HASHES["initial"]:
        raise ValueError("Baseline did not consume this actual own INITIAL")
    old=source["originalSource"]
    design=saved["actualDesign"]
    Aq=Q.from_float(old["centralA"]);Bq=Q.from_float(old["centralB"])
    with np.load(args.work/names["ramp"],allow_pickle=False) as r:
        An=Q.from_float(float(r["centralA"]));Bn=Q.from_float(float(r["centralB"]))
        central=Q.from_float(float(r["centralLength"]))
        ramp=Q.from_float(float(r["ramp"]));vn=Q.from_float(float(r["v"]))
    coast=Q.from_float(saved["cauchyDesign"]["coastLength"])
    if coast!=Q.from_float(.02) or ramp!=Q.from_float(saved["cauchyDesign"]["rampLength"]):
        raise ValueError("Same physical ramp/coast lengths required")
    vo=Q.from_float(design["v"]);a0=Q.from_float(design["a0"])
    right=Q.from_float(design["rightLength"])
    end=Q.from_float(old["S"])
    h=Q.from_float(source["window"])
    b=central+ramp+coast
    amp=I(Q.from_float(old["amplitude"]))
    if (saved["options"]["gap"]!=1 or source["centralGap"]<1.049 or
        amp.upper()>=Q(7,8) or vo!=Q.from_float(.05) or h!=Q.from_float(.2)):
        raise ValueError("This certificate is for the explicitly bound window/source only")

    def ellipse_arc(A,B,terms=64):
        center=I((A+B)/2)
        ratio=I((A-B)/(A+B))
        coeff=I(1)
        total=I(1)
        for n in range(1,terms+1):
            coeff=coeff*ratio*Q(2*n-3,2*n)
            total+=coeff.square()
        nxt=coeff*ratio*Q(2*terms-1,2*(terms+1))
        tail=upper(center*nxt.square()/(1-ratio.square()))
        return center*total+I(0,tail.upper())

    ao=ellipse_arc(Aq,Bq)
    an=ellipse_arc(An,Bn)
    if ao.lower()<=1 or an.lower()<=1:
        raise ArithmeticError("Exact central arc radii must exceed one")
    deltaa=absolute(an-ao)
    amin=I(min(an.lower(),ao.lower()))
    axis_delta=I(max(abs(An-Aq),abs(Bn-Bq)))
    density=upper(axis_delta/amin+I(Aq)*deltaa/(an*ao))
    # Every normalized ellipse has the same material quarter-angle.
    phase=upper(pi*density/4)
    oldTu=upper(ao*I(Aq/Bq**2))
    tangent_at_same_native_angle=I(abs(Aq*Bn-Bq*An)/(2*min(Aq,An)*min(Bq,Bn)))
    central_tangent=upper(tangent_at_same_native_angle+oldTu*phase)

    normrows=[row["exactWholeCellCartesianNormBounds"] for row in data["raw"]["rows"]]
    normrows.append(data["last"]["actualLastCellCartesianNorms"])
    nrows=[row["normalization"] for row in data["primitive"]["rows"]]
    nrows.append(data["last"]["actualLastCellNormalized"])
    ms=I(max(Q(row["Xstheta"]["rational"]) for row in normrows))
    mtt=I(max(Q(row["Xthetatheta"]["rational"]) for row in normrows))
    eta=I(max(Q(row["eBound"]["hi"]) for row in nrows))
    W=I(max(Q(row["refinedAngularInverseTangentialSpeed"]["hi"]) for row in nrows))
    rawmetric=I(max(Q(row["rawRelativeMetric"]["hi"]) for row in nrows))
    qmin=I(Q(403,1000))
    if rawmetric.upper()>=Q(1,1000000) or Bn**2*(1-Q(1,1000000))<=qmin.upper()**2:
        raise ArithmeticError("All sixteen exact raw cells must imply q>.403")
    U=I(vn)/an
    rampTs=upper(ms/qmin+U+eta/qmin+2*mtt*W/qmin.square())
    # R232 full-coast rank-one principal-curvature bound is strictly <8.893.
    # This is also rechecked in the actual exit certificate but the whole
    # coast bound, not its exit value, is used for the transport integral.
    if (data["coast"]["fullAngularDomainCertified"] is not True or
        data["last"]["allSixteenNormalizedCellsCertified"] is not True or
        data["last"]["accurateCoastC2SeamFromIdenticalWholeEndpointFunctions"] is not True):
        raise ValueError("Complete exact prefix/seam certificates required")
    coastk=I(Q(8893,1000))
    if Q(data["coast"]["newTargetWholeCoastBounds"]["nonzero_principal_curvature"]["hi"])>=coastk.lower():
        raise ArithmeticError("Published full-coast curvature bound was not paid")
    prefixT=upper(I(ramp)*rampTs+I(coast)*coastk/2)

    t=I(b-central)/I(end-central)
    chi=t**3*(10+t*(-15+6*t))
    chis=30*t.square()*(1-t).square()/I(end-central)
    chiss=60*t*(1-t)*(1-2*t)/I(end-central).square()
    sn,cs=cert.sincos(pi*chi)
    q=(1+cs)/2
    r=sn/2
    qs=-sn*pi*chis/2
    rs=cs*pi*chis/2
    qss=-cs*(pi*chis).square()/2-sn*pi*chiss/2
    rss=-sn*(pi*chis).square()/2+cs*pi*chiss/2
    H=I(2).sqrt()
    cp=(1-2*r.square()).sqrt()
    if cp.lower()<=0:
        raise ArithmeticError("Original reference spherical chart not proved")
    as0=upper(H*(absolute(qs)+absolute(rs))/cp)
    ass0=upper(H*(absolute(qss)+absolute(rss))/cp+
        2*(H*qs/cp).square()+2*absolute(qs*rs)/cp.square())

    _,cosA=cert.sincos(amp)
    cosA=I(cosA.lower())
    if cosA.lower()<=0:
        raise ArithmeticError("Original tail chart has no positive cos(A)")
    azimuth_bound=upper((1-cosA)/(2*cosA.sqrt()))
    B0=upper(azimuth_bound+amp)
    alpha_s=upper(amp/I(Q(46,100))*I(Q(630,256))*I(vo))
    alpha_ss=upper(amp/I(Q(46,100)).square()*I(Q(2520,64))*I(vo).square())
    B1=upper(2*alpha_s/cosA)
    B2=upper(2*(alpha_ss+alpha_s.square())/cosA+3*alpha_s.square()/cosA.square())
    As=upper(as0+absolute(chis)*B0+absolute(chi)*B1)
    Ass=upper(ass0+absolute(chiss)*B0+2*absolute(chis)*B1+absolute(chi)*B2)
    refdist=upper(H*(absolute(1-q)+absolute(r))+absolute(chi)*B0)

    # On this whole window the reflection-odd raw phi has positive cosine,
    # so its exact mean phase and both radial derivatives are zero.
    tmax=I(b+h-central)/I(end-central)
    chimax=tmax**3*(10+tmax*(-15+6*tmax))
    if chimax.upper()>=Q(1,2):
        raise ArithmeticError("Whole-window phase bound needs chi<1/2")
    snmax,_=cert.sincos(pi*chimax)
    whole_phi=upper(pi*H*snmax/4+chimax*amp)
    if whole_phi.upper()>=pi.lower()/2:
        raise ArithmeticError("Original exact mean phase may be singular")

    f_old=I(a0+vo*ramp/2+vo*coast)
    f_new=an+I(vn*ramp/2+vn*coast)
    P=upper(absolute(f_new-f_old)+f_old*(central_tangent+prefixT+refdist))
    oldVu=upper(I(vo)+f_old*As)
    oldAu=upper(2*I(vo)*As+f_old*(Ass+As.square()))
    V=upper(value(data["outlet"]["derivativeUpper"]["Vu"])+oldVu)
    A=upper(value(data["outlet"]["derivativeUpper"]["Au"])+oldAu)

    tx=I(h/right)
    step=tx**5*(126+tx*(-420+tx*(540+tx*(-315+70*tx))))
    if not 0<=step.lower()<=step.upper()<1:
        raise ArithmeticError("Actual compact window exceeds scalar turn interval")
    if design["power"]!=7 or not 0<=design["beta"]<=1:
        raise ValueError("Actual original scalar tail shape changed")
    radial_derivative=I(vo)-(1+I(vo))*step**7
    if radial_derivative.lower()<=0 or f_old.lower()<=1:
        raise ArithmeticError("Cannot prove original radius >=1 throughout the window")
    correction=upper(P+I(h)*Q(16,81)*V+I(h*h)*Q(54,3125)*A)
    lower_speed=I(1)-correction
    if lower_speed.lower()<=0:
        raise ArithmeticError("Actual endpoint budgets do not certify angular regularity")
    values=dict(
        oldExactEllipseArc=ao,newExactEllipseArc=an,centralArcDifference=deltaa,
        normalizedCentralSpeedDifference=density,centralMaterialPhaseDifference=phase,
        centralTangentDifference=central_tangent,rawRampAngularSpeedLower=qmin,
        rawRampMixedDerivative=ms,rawRampAngularSecondDerivative=mtt,
        normalizedRampUnitTDerivative=rampTs,entirePrefixUnitTChange=prefixT,
        originalPortChi=chi,originalReferenceToCentralUnitT=refdist,
        wholeWindowRawPhiBound=whole_phi,
        oldAngleFirst=As,oldAngleSecond=Ass,
        oldPortXs_u=oldVu,oldPortXss_u=oldAu,
        endpointPositionAngularDifference=P,endpointVelocityAngularDifference=V,
        endpointAccelerationAngularDifference=A,
        oldWindowScalarDerivativeLower=radial_derivative,
        wholeWindowAngularCorrectionUpper=correction,
        wholeWindowAngularSpeedLower=lower_speed)
    output=dict(schema="6a65-accurate-gap105-compact-window-continuous-angular-regularity-v1",
        inputs={k:dict(path=names[k],SHA256=HASHES[k]) for k in names},
        entrySHA256=sha(__file__),
        sourceDefinitionSHA256=source["sourceDefinitionSHA256"],
        exactDefinitionScope="accurate integral and exact Hermite seams; zero-free-coefficient Cauchy source",
        exactFormalPhysicalDomain=dict(c=str(central),b=str(b),h=str(h),stop=str(b+h),S=str(end)),
        allSixteenR233CellsConsumed=True,wholeCoastBoundConsumed="R232 kappa<8893/1000",
        completeActualExitDerivativeReportConsumed=True,
        allDecisionsUseIntegerRationalBounds=True,finiteAngleMaximaUsed=False,
        exactEllipticArcTerms=64,integerBits=cert.BITS,
        bounds={k:record(v) for k,v in values.items()},
        exactHermiteSuprema=dict(H0="1",H1="16/81",H2="54/3125"),
        fullWindowAngularRegularityCertified=True,
        formalNaturalPerimeterMetricAndC2InverseWellDefined=True,
        formalSeamTwoJetsPreserved=True,literalFloatingConsumerErrorCertified=False,
        laterCartesianCorrectionsCovered=False,wholeWindowImmersionCertified=False,
        wholeClosedReachCertified=False,seconds=time.monotonic()-started,
        OSExitCode=None,externalExitReceiptRequired=True)
    args.output.write_text(json.dumps(output,indent=2)+"\n")
    print(json.dumps(dict(event="actual_whole_window_q_certificate",reportSHA256=sha(args.output),
        qLower=float(lower_speed.lower()),correctionUpper=float(correction.upper()),
        P=float(P.upper()),V=float(V.upper()),A=float(A.upper()),seconds=output["seconds"])),flush=True)


if __name__=="__main__":
    main()

