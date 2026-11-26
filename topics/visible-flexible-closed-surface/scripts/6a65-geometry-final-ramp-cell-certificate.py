#!/usr/bin/env python3
"""Consume the accurate coast port on the complete last ramp Hermite cell.

The saved terminal polynomial is only a proof proxy. The certified actual
field replaces all right endpoint P/V/A by the same accurate R137 port, with
all theta derivatives paid by the independent full-domain port certificate.
"""
from __future__ import annotations
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
from pathlib import Path
from types import SimpleNamespace
import time


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def module(p,n):
    s=importlib.util.spec_from_file_location(n,p)
    m=importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def hermite_norm(co,order,subdivisions=64):
    values=[Q(x,2) for x in co]
    for unused in range(order):
        values=[j*values[j] for j in range(1,len(values))]
    degree=len(values)-1
    largest=Q(0)
    for k in range(subdivisions):
        lo,span=Q(k,subdivisions),Q(1,subdivisions)
        for i in range(degree+1):
            control=sum((values[j]*sum((Q(math.comb(j,m)*math.comb(i,m),math.comb(degree,m))
                *lo**(j-m)*span**m for m in range(min(i,j)+1)),Q(0))
                for j in range(degree+1)),Q(0))
            largest=max(largest,abs(control))
    return largest


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--master',type=Path,required=True)
    ap.add_argument('--gram-report',type=Path,required=True)
    ap.add_argument('--first15-report',type=Path,required=True)
    ap.add_argument('--port-report',type=Path,required=True)
    ap.add_argument('--scripts-dir',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--metric-threshold',default='1/1000000')
    ap.add_argument('--curvature-threshold',default='1000/97')
    args=ap.parse_args()
    if args.output.exists():
        raise FileExistsError("Fresh actual final-cell proof result required")
    start=time.monotonic()
    gp=args.scripts_dir/'6a65-geometry-ramp-native-gram-certificate.py'
    cp=args.scripts_dir/'6a65-geometry-ramp-native-curvature-certificate.py'
    pp=args.scripts_dir/'6a65-geometry-ramp-normalization-primitive.py'
    hp=args.scripts_dir/'6a65-m12-r137-continuous-domain.py'
    gram=module(gp,'actual_last_cell_gram')
    curvature=module(cp,'actual_last_cell_curvature')
    primitive=module(pp,'actual_last_cell_primitive')
    cert=module(hp,'actual_last_cell_integer')
    I=cert.I
    prior=json.loads(args.gram_report.read_text())
    first15=json.loads(args.first15_report.read_text())
    port=json.loads(args.port_report.read_text())
    master_hash=sha(args.master)
    if (prior.get('allFirst15PolynomialCellsProved') is not True
        or first15.get('allFirst15PolynomialCellsProved') is not True
        or port.get('fullAngularDomainCertified') is not True
        or any(x['source']['masterSHA256']!=master_hash for x in (prior,first15,port))
        or first15['source']['gramReportSHA256']!=sha(args.gram_report)
        or port['source']['gramReportSHA256']!=sha(args.gram_report)):
        raise ValueError("Same actual master and complete input certificates required")

    class PolynomialProxy(gram.ActualRamp):
        def cell(self,index):
            if index<15:
                return super().cell(index)
            if index!=15:
                raise ValueError("Only the actual last saved-polynomial proof proxy is added")
            left,right=self.port(15),self.port(16)
            sx0=Q.from_float(float(self.sx[15]))
            L=Q.from_float(float(self.sx[16]))-sx0
            if Q.from_float(float(self.sx[16]-self.sx[15]))!=L:
                raise ArithmeticError("Physical terminal cell subtraction is not exact")
            lb=gram.dyadic_bits(L)
            bits=self.input_bits+2*lb+1
            ports=[left[0],left[1],left[2],right[0],right[1],right[2]]
            factors=[1<<(bits-self.input_bits),
                L.numerator<<(bits-self.input_bits-lb),
                L.numerator**2<<(bits-self.input_bits-2*lb)]*2
            out=[]
            for j in range(6):
                row=[]
                for d in range(3):
                    pair=[]
                    for part in range(2):
                        values=[]
                        for k in range(2*self.degree+1):
                            numerator=sum(gram.H2[p][j]*factors[p]*ports[p][d][part][k] for p in range(6))
                            if numerator%2:
                                raise ArithmeticError("Terminal proxy coefficient is not at the declared exact dyadic scale")
                            values.append(numerator//2)
                        pair.append(values)
                    row.append(pair)
                out.append(row)
            return out,bits,L,sx0

    model=PolynomialProxy(args.master)
    arc=tuple(map(Q,prior['exactEllipticArcRadiusInterval']))
    target_box=(min(arc[0],model.a0),max(arc[1],model.a0))
    proxy,unused=gram.check_cell(model,15,95,target_box)
    C,bits,L,sx0=model.cell(15)
    delta_ports={key:[Q(x['rational']) for x in val] for key,val in port['actualCentralAngleCompletePortDerivativeBounds'].items()}
    weights={(i,p):L**(p-i)*hermite_norm(gram.H2[3+p],i) for i in range(3) for p in range(3)}
    perturb={(i,j):sum((weights[i,p]*delta_ports[name][j] for p,name in enumerate(('P','V','A'))),Q(0))
        for i in range(3) for j in range(3)}
    U=gram.angular(C,model.degree)
    MU=[gram.vector_bernstein_l1(U,bits,L,j) for j in range(3)]
    raw=proxy['completeRawNativeGramBounds']
    epsE,epsF=(Q(raw[key]['rational']) for key in ('Eminus1','F'))
    r=[Q(x['rational']) for x in raw['GminusTarget']]
    MS=I(1+epsE).sqrt().upper()
    ds=perturb[1,0]
    du=[perturb[j,1] for j in range(3)]
    deltaE=2*MS*ds+ds**2
    deltaF=MS*du[0]+MU[0]*ds+ds*du[0]
    deltaG=[sum((Q(math.comb(j,k))*(MU[k]*du[j-k]+du[k]*MU[j-k]+du[k]*du[j-k])
        for k in range(j+1)),Q(0)) for j in range(3)]
    actual=copy.deepcopy(proxy)
    actual_raw=dict(Eminus1=gram.upper(epsE+deltaE),F=gram.upper(epsF+deltaF),
        GminusTarget=[gram.upper(x+y) for x,y in zip(r,deltaG)],
        normalizedF=gram.upper((epsF+deltaF)/model.B),
        relativeG=gram.upper((r[0]+deltaG[0])/model.B**2),
        spectralRelativeMetric=gram.upper(max(epsE+deltaE,(r[0]+deltaG[0])/model.B**2)+(epsF+deltaF)/model.B))
    actual['completeRawNativeGramBounds']=actual_raw
    actual['rightPortIsAccurateR137NotPolynomialProxy']=True
    combined=copy.deepcopy(prior)
    combined['rows'].append(actual)
    facade=SimpleNamespace(**{k:v for k,v in vars(gram).items() if not k.startswith('__')})
    facade.ActualRamp=PolynomialProxy
    whole=curvature.WholeDomain(facade,cert,model,combined,95)

    class ActualLastCell(curvature.Cell):
        def jets(self,index,count,lo,hi):
            result=super().jets(index,count,lo,hi)
            for i,j,name in ((1,0,'S'),(0,1,'U'),(2,0,'SS'),(1,1,'SU'),(0,2,'UU')):
                error=I(-perturb[i,j],perturb[i,j])
                result[name]=[x+error for x in result[name]]
            return result

    cell=ActualLastCell(whole,15)
    for name,ij in dict(X=(0,0),Xs=(1,0),Xss=(2,0),Xtheta=(0,1),Xstheta=(1,1),Xthetatheta=(0,2)).items():
        cell.full_bounds[name]+=perturb[ij]
    bound=I(0)
    area=None
    leaves=0
    splits=0
    proofhash=hashlib.sha256()
    def consume(index,count,lo,hi,depth):
        nonlocal bound,area,leaves,splits
        try:
            values=cell.geometry(index,count,lo,hi)
            if values['curvature'].hi>=I(Q(10)).lo:
                raise ArithmeticError("Actual last-cell box exceeds the declared curvature cap")
        except ArithmeticError:
            if depth>=8:
                raise
            splits+=1
            if depth%2==0:
                consume(2*index,2*count,lo,hi,depth+1)
                consume(2*index+1,2*count,lo,hi,depth+1)
            else:
                mid=(lo+hi)/2
                consume(index,count,lo,mid,depth+1)
                consume(index,count,mid,hi,depth+1)
            return
        bound=cert.max_upper(bound,values['curvature'])
        area=cert.lower_i(values['area']) if area is None else I.raw(min(area.lo,values['area'].lo),min(area.lo,values['area'].lo))
        proofhash.update((json.dumps(dict(index=index,count=count,lo=str(lo),hi=str(hi),
            bounds={key:[value.lo,value.hi] for key,value in values.items()}),sort_keys=True)+'\n').encode())
        leaves+=1
    for k in range(64):
        consume(k,64,Q(0),Q(1),0)
    crow=dict(index=15,curvatureUpper=bound.display(),
        exactWholeCellCartesianNormBounds={key:gram.upper(value) for key,value in cell.full_bounds.items()})
    print(json.dumps(dict(event='actual-nonpolynomial-last-cell-raw-certified',
        rawMetric=actual_raw['spectralRelativeMetric'],ownCurvature=bound.display(),
        leaves=leaves,splits=splits,seconds=time.monotonic()-start)),flush=True)
    # The complete proxy angular primitive is computed on all its saved modes.
    ellipse=primitive.ellipse_fourier(model.A,model.B,arc)
    proxy_primitive=primitive.actual_cell(model,15,proxy,gram,cert,ellipse,arc)
    proxyW=Q(proxy_primitive['exactBounds']['actualAngularInverseTangentialSpeed']['rational'])
    proxyM=Q(proxy_primitive['exactBounds']['exactMeanE']['rational'])
    Umax=model.v/arc[0]
    qp=I(model.B**2-r[0]).sqrt().lower()
    qa=I(model.B**2-r[0]-deltaG[0]).sqrt().lower()
    rhoP=r[0]/(qp+model.B)
    rhoA=(r[0]+deltaG[0])/(qa+model.B)
    ap,aa=arc[0]-rhoP,arc[0]-rhoA
    pmax=1+model.v*model.ramp/(2*arc[0])
    qPmax=I((pmax*model.A)**2+r[0]).sqrt().upper()
    deltaq=deltaG[0]/(qa+qp)
    delta_density=deltaq/aa*(1+qPmax/ap)
    proxy_numerator=r[1]+2*Umax*r[0]
    delta_e=(deltaG[1]+2*Umax*deltaG[0])/(2*qa)
    delta_e+=proxy_numerator*deltaG[0]/(2*qa*qp*(qa+qp))
    meanActual=proxyM+delta_e
    Wactual=proxyW+cert.pi_interval().upper()*((1+qPmax/ap)*delta_e+delta_density*meanActual)
    final_primitive=dict(exactBounds=dict(exactMeanE=gram.upper(meanActual),
        actualAngularInverseTangentialSpeed=gram.upper(Wactual)))
    normalized=primitive.normalization_row(15,actual,crow,final_primitive,model,prior,cert)
    metric=Q(normalized['normalizedSpectralMetric']['hi'])
    kappa=Q(normalized['normalizedOwnCurvature']['hi'])
    allmetric=max(metric,Q(first15['maximumNormalizedSpectralMetric']['rational']))
    allkappa=max(kappa,Q(first15['maximumNormalizedOwnCurvature']['rational']))
    passed=allmetric<Q(args.metric_threshold) and allkappa<Q(args.curvature_threshold)
    out=dict(schema='6a65-actual-entire-ramp-with-accurate-nonpolynomial-coast-port-certified-v1',
        source=dict(masterSHA256=master_hash,gramReportSHA256=sha(args.gram_report),
            first15NormalizationReportSHA256=sha(args.first15_report),accuratePortReportSHA256=sha(args.port_report),
            gramCheckerSHA256=sha(gp),curvatureCheckerSHA256=sha(cp),primitiveCheckerSHA256=sha(pp),
            integerArithmeticSHA256=sha(hp),entrySHA256=sha(__file__)),
        rightEndpointDefinition='same accurate Gamma95 R137 P,V,A functions in exact central material angle',
        savedTerminalPolynomialUsedOnlyAsProofProxy=True,
        lastCellPhysicalLength=str(L),lastCellRelativePhysicalDomain=[str(sx0),str(sx0+L)],
        exactHermiteWeights={str(key):gram.upper(value) for key,value in weights.items()},
        completeNonpolynomialPerturbationBounds={str(key):gram.upper(value) for key,value in perturb.items()},
        proxyGram=proxy['completeRawNativeGramBounds'],actualLastCellGram=actual_raw,
        actualRawLastCellCurvature=bound.display(),actualRawLastCellAreaLower=area.display(),
        actualLastCellCurvatureLeaves=leaves,actualLastCellCurvatureSplits=splits,
        actualLastCellIntegerGeometrySHA256=proofhash.hexdigest(),
        actualLastCellCartesianNorms=crow['exactWholeCellCartesianNormBounds'],
        proxyFullFrequencyPrimitive=proxy_primitive,
        nonpolynomialPrimitiveTransfer={key:gram.upper(value) for key,value in dict(
            actualVersusProxyE=delta_e,actualVersusProxySpeed=deltaq,
            normalizedSpeedDensityDifference=delta_density,
            exactMeanE=meanActual,actualAngularInverseTangentialSpeed=Wactual).items()},
        actualLastCellNormalized=normalized,
        maximumEntireRampNormalizedSpectralMetric=gram.upper(allmetric),
        maximumEntireRampNormalizedOwnCurvature=gram.upper(allkappa),
        metricThreshold=args.metric_threshold,curvatureThreshold=args.curvature_threshold,
        allSixteenRawCellsCertified=True,allSixteenNormalizedCellsCertified=passed,
        accurateCoastC2SeamFromIdenticalWholeEndpointFunctions=True,
        literalFloatingQuadratureNormalizationCertified=False,
        exactIsometryClaimed=False,wholeClosedReachCertified=False,
        seconds=time.monotonic()-start,OSExitCode=None,externalExitReceiptRequired=True)
    args.output.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(event='actual-entire-ramp-complete',
        reportSHA256=sha(args.output),allSixteenNormalizedCellsCertified=passed,
        metric=out['maximumEntireRampNormalizedSpectralMetric'],
        curvature=out['maximumEntireRampNormalizedOwnCurvature'],
        lastCellMetric=normalized['normalizedSpectralMetric'],
        lastCellCurvature=normalized['normalizedOwnCurvature'],seconds=out['seconds'])),flush=True)
    if not passed:
        raise SystemExit(2)


if __name__=='__main__':
    main()

