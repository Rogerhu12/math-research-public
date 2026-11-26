#!/usr/bin/env python3
"""Actual exact-integral normalization budget from complete ramp certificates.

This pays the s-dependent angular inverse, scalar dilation, and genuine
Cartesian curvature perturbation. It does not certify the literal finite
quadrature implementation, the last coast-repair cell, or a closed surface.
The coarse angular primitive 2*pi*||e|| is explicitly identified; a later
weighted-Fourier primitive can replace this one bound without changing Y.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import time
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--master',type=Path,required=True)
    ap.add_argument('--gram-report',type=Path,required=True)
    ap.add_argument('--curvature-report',type=Path,required=True)
    ap.add_argument('--scripts-dir',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--metric-threshold',default='1/100000')
    ap.add_argument('--curvature-threshold',default='1000/97')
    args=ap.parse_args()
    if args.output.exists():
        raise FileExistsError('Fresh actual normalization certificate required')
    start=time.monotonic()
    g=json.loads(args.gram_report.read_text())
    c=json.loads(args.curvature_report.read_text())
    if (g.get('allFirst15PolynomialCellsProved') is not True or c.get('allFirst15PolynomialCellsProved') is not True
        or g['source']['masterSHA256']!=sha(args.master) or c['source']['masterSHA256']!=sha(args.master)
        or c['source']['gramReportSHA256']!=sha(args.gram_report)):
        raise ValueError('Same actual complete raw Gram and curvature certificates required')
    helper=args.scripts_dir/'6a65-m12-r137-continuous-domain.py'
    spec=importlib.util.spec_from_file_location('normalization_integer_arithmetic',helper)
    cert=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cert)
    I,up,lo=cert.I,cert.upper_i,cert.lower_i
    pi=cert.pi_interval()
    with np.load(args.master,allow_pickle=False) as m:
        v=I(Q.from_float(float(m['v'])))
        ramp=I(Q.from_float(float(m['ramp'])))
    B=I(Q(g['centralBExactDyadic']))
    # Exact integral definition: this choice makes normalization the identity
    # at the exact central cylinder. The stored numerical a0 is not substituted.
    fmin=lo(I(Q(g['exactEllipticArcRadiusInterval'][0])))
    U=up(v/fmin)
    U1=up(v/ramp*Q(630,256)/fmin+U.square())
    metric_cap=I(Q(args.metric_threshold))
    curvature_cap=I(Q(args.curvature_threshold))
    rows=[]
    max_metric=I(0)
    max_curvature=I(0)
    for j,(gr,cr) in enumerate(zip(g['rows'],c['rows'])):
        if gr['index']!=j or cr['index']!=j:
            raise ValueError('Complete ordered actual cell rows required')
        gb=gr['completeRawNativeGramBounds']
        epsE=I(Q(gb['Eminus1']['rational']))
        epsF=I(Q(gb['F']['rational']))
        r0,r1,r2=(I(Q(row['rational'])) for row in gb['GminusTarget'])
        delta=I(Q(gb['spectralRelativeMetric']['rational']))
        norms={key:I(Q(value['rational'])) for key,value in cr['exactWholeCellCartesianNormBounds'].items()}
        raw_kappa=I(Q(cr['curvatureUpper']['hi']))
        qmin=lo((B.square()-r0).sqrt())
        eta=up((r1+2*U*r0)/(2*qmin))
        eta1=up((r2+2*U1*r0+2*U*r1)/(2*qmin)+eta*(U+eta/qmin))
        rho=up(r0/(qmin+B))
        amin=lo(fmin-rho)
        dilation_error=up(rho/amin)
        lambda_min=lo(1-dilation_error)
        lambda_max=up(1+dilation_error)
        lambda_first=up(lambda_max*eta/amin)
        lambda_second=up(lambda_max*(2*eta.square()/amin.square()+U*eta/amin+eta1/amin))
        M0=norms['X']
        M1=up((1+epsE).sqrt())
        Mss=norms['Xss']
        Q0=up(2*M0)
        C1=up(M1+Q0*eta/amin)
        C2=up(Mss+(2*(M1+C1)*eta+U*Q0*eta+Q0*eta1)/amin)
        # The exact angular map satisfies q*theta_s = u*mean(e)-int_0^theta e.
        # The coefficients u/(2*pi),1-u/(2*pi) are both in [0,1].
        angular_speed=up(2*pi*eta)
        velocity_error=up(dilation_error*(M1+C1)+lambda_max*angular_speed+lambda_first*Q0)
        normalized_E=up(epsE+2*M1*velocity_error+velocity_error.square())
        normalized_F=up(epsF/qmin+velocity_error)
        normalized_metric=up(normalized_E/2+((normalized_E/2).square()+normalized_F.square()).sqrt())
        # Z=C+lambda*(Y-C), before the pure angular reparameterization.
        sigma=lo((1-delta).sqrt())
        tau=up((dilation_error*C1+lambda_first*Q0)/lambda_min)
        alpha=up(tau/sigma)
        if alpha.hi>=I(1).lo:
            raise ArithmeticError('No positive relative immersion margin after dilation')
        normal_difference=up(2*alpha)
        ambient_second=up((cert.max_upper(Mss,norms['Xthetatheta']/B.square())
                           +norms['Xstheta']/B)/(1-delta))
        remainder_ss=up(2*lambda_first*(M1+C1)+dilation_error*C2+lambda_second*Q0)
        remainder=up((remainder_ss+lambda_first*norms['Xtheta']/B)/(1-delta))
        normalized_curvature=up((lambda_max*raw_kappa+lambda_max*normal_difference*ambient_second+remainder)
            /(lambda_min.square()*(1-alpha).square()))
        values=dict(rawKappa=raw_kappa,rawRelativeMetric=delta,qMinimum=qmin,
            eBound=eta,eRadialDerivativeBound=eta1,perimeterRadiusError=rho,
            normalizationRadiusMinimum=amin,dilationError=dilation_error,
            dilationFirst=lambda_first,dilationSecond=lambda_second,
            positionFromMean=Q0,meanFirst=C1,meanSecond=C2,
            actualAngularInverseTangentialSpeed=angular_speed,
            completeNormalizedRadialVelocityError=velocity_error,
            normalizedEError=normalized_E,normalizedFOverf=normalized_F,
            normalizedSpectralMetric=normalized_metric,normalDifference=normal_difference,
            completeAmbientSecondRelativeNorm=ambient_second,
            normalizedOwnCurvature=normalized_curvature)
        passed=normalized_metric.hi<metric_cap.lo and normalized_curvature.hi<curvature_cap.lo
        rows.append(dict(index=j,bounds={key:value.display() for key,value in values.items()},
                         normalizedGEqualsfSquaredExactly=True,passed=passed))
        max_metric=cert.max_upper(max_metric,normalized_metric)
        max_curvature=cert.max_upper(max_curvature,normalized_curvature)
    out=dict(schema='6a65-actual-first15-exact-integral-normalization-complete-metric-curvature-v1',
        source=dict(masterSHA256=sha(args.master),gramReportSHA256=sha(args.gram_report),
            rawCurvatureReportSHA256=sha(args.curvature_report),integerArithmeticSHA256=sha(helper),entrySHA256=sha(__file__)),
        normalizationDefinition='C=mean(Y*|Ytheta|)/a; a=mean|Ytheta|; lambda=f/a; exact arc inverse; f(0)=exact arc radius of the frozen dyadic central ellipse',
        angularPrimitiveMethod='coarse but complete 2*pi*sup|q_s-(f_s/f)q|; no s-dependent inverse term omitted',
        actualCentralC2IdentityUsesExactEllipsePerimeter=True,
        literalFloatingQuadratureNormalizationCertified=False,
        maximumNormalizedSpectralMetric=max_metric.display(),maximumNormalizedOwnCurvature=max_curvature.display(),
        metricThreshold=args.metric_threshold,curvatureThreshold=args.curvature_threshold,
        allFirst15PolynomialCellsProved=len(rows)==15 and all(row['passed'] for row in rows),rows=rows,
        finalExactCoastPortCellExcluded=True,wholeRampCertified=False,
        exactIsometryClaimed=False,wholeClosedReachCertified=False,
        seconds=time.monotonic()-start,OSExitCode=None,externalExitReceiptRequired=True)
    args.output.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(event='actual-full-normalization-budget',reportSHA256=sha(args.output),
        maximumNormalizedSpectralMetric=out['maximumNormalizedSpectralMetric'],
        maximumNormalizedOwnCurvature=out['maximumNormalizedOwnCurvature'],
        allFirst15PolynomialCellsProved=out['allFirst15PolynomialCellsProved'],seconds=out['seconds'])),flush=True)
    if not out['allFirst15PolynomialCellsProved']:
        raise SystemExit(2)


if __name__=='__main__':
    main()
