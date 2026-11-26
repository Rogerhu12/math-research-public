#!/usr/bin/env python3
"""Strict total perimeter and uniform normalization for the actual Gamma95.

The Simpson remainder uses a continuous J'''' enclosure from whole-cell
Fourier derivative bounds. Exact dyadic arithmetic makes all decisions.
This does not certify numerical angular inverse maps or complete C2 jets.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(name,p):
    spec=importlib.util.spec_from_file_location(name,p);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
def emit(x):print(json.dumps(x,allow_nan=False),flush=True)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--scripts-dir',type=Path,required=True)
    ap.add_argument('--prefix-report',type=Path,required=True)
    ap.add_argument('--coast-master',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--derivative-cells',type=int,default=2048)
    ap.add_argument('--target-half-width',default='1/1000000000000')
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError('Fresh actual perimeter certificate required')
    if not 64<=args.derivative_cells<=8192:raise ValueError('Bounded derivative-cell request required')
    target=Q(args.target_half_width)
    if not Q(1,10**18)<=target<=Q(1,10**6):raise ValueError('Bounded exact tolerance required')
    start=time.monotonic();record=json.loads(args.prefix_report.read_text())
    if record['schema']!='6a65-new-coupled-gap105-v045-actual-Cauchy-R137-prefix-v1':raise ValueError('Wrong actual prefix source')
    if record['coast']['masterSHA256']!=sha(args.coast_master):raise ValueError('Coast source identity mismatch')
    wrapper_path=args.scripts_dir/'6a65-m12-ramp-coast-continuous-domain.py'
    integer_path=args.scripts_dir/'6a65-m12-r137-continuous-domain.py'
    budget_path=args.scripts_dir/'6a65-geometry-central-gap-held-budget.py'
    wrap=load('strict_perimeter_curve_cells',wrapper_path);cert=wrap.cert;I=cert.I
    budget=load('strict_perimeter_target_definition',budget_path)
    with np.load(args.coast_master,allow_pickle=False) as d:
        modes=d['curve_modes'].copy();raw=d['curve_coefficients'].copy();degree=int(d['degree'])
        finite_arc=Q.from_float(float(d['unnormalized_radius']))
        finite_target=Q.from_float(float(d['exact_target_radius']))
    if degree!=95 or set(map(int,modes))!=set(range(-95,96)) or raw.shape!=(191,3):raise ValueError('Full actual Gamma95 curve required')
    if not np.all(np.isfinite(raw)):raise ValueError('Nonfinite exact coefficients')
    by_mode={int(k):a for k,a in zip(modes,raw)}
    co=[[Q.from_float(float(v.real)) for v in by_mode[0]]];si=[[Q(0)]*3]
    for k in range(1,degree+1):
        co.append([Q.from_float(float(a.real))+Q.from_float(float(b.real)) for a,b in zip(by_mode[k],by_mode[-k])])
        si.append([Q.from_float(float(b.imag))-Q.from_float(float(a.imag)) for a,b in zip(by_mode[k],by_mode[-k])])
    source={'scriptSHA256':sha(__file__),'prefixReportSHA256':sha(args.prefix_report),'coastMasterSHA256':sha(args.coast_master),
            'localCurveEnclosureSHA256':sha(wrapper_path),'integerArithmeticSHA256':sha(integer_path),'exactPerimeterDefinitionSHA256':sha(budget_path)}
    emit({'event':'strict-perimeter-start','derivativeCells':args.derivative_cells,'targetHalfWidth':str(target),'source':source})
    cells,old_arc,old_quad,unused=wrap.local_curve_cells(co,si,args.derivative_cells)
    fifth_bound=[sum((k**5*(abs(co[k][d])+abs(si[k][d])) for k in range(1,degree+1)),Q(0)) for d in range(3)]
    fifth=[I(-b,b) for b in fifth_bound]
    fourth_bound=I(0);speed_min=None;rows=hashlib.sha256()
    for j,cell in enumerate(cells):
        unused,p,q,r,s=cell;J=cert.norm2(p).sqrt()
        if J.lo<=0:raise ArithmeticError('No positive whole-cell speed')
        speed_min=cert.lower_i(J) if speed_min is None else I.raw(min(speed_min.lo,J.lo),min(speed_min.lo,J.lo))
        E1=2*cert.dot(p,q)
        E2=2*(cert.norm2(q)+cert.dot(p,r))
        E3=6*cert.dot(q,r)+2*cert.dot(p,s)
        E4=6*cert.norm2(r)+8*cert.dot(q,s)+2*cert.dot(p,fifth)
        J4=E4/(2*J)-E1*E3/(J**3)-3*E2.square()/(4*J**3)+9*E1.square()*E2/(4*J**5)-15*(E1**4)/(16*J**7)
        absolute=J4.absupper();fourth_bound=I.raw(max(fourth_bound.hi,absolute),max(fourth_bound.hi,absolute))
        rows.update((json.dumps({'cell':j,'J4':[J4.lo,J4.hi],'speed':[J.lo,J.hi]},sort_keys=True)+'\n').encode())
    pi=cert.pi_interval();N=args.derivative_cells
    while True:
        remainder=cert.upper_i(fourth_bound*(pi/N)**4/180)
        if remainder.upper()<target/2:break
        N*=2
        if N>65536:raise ArithmeticError('Declared rigorous Simpson tolerance exceeds this bounded run')
    emit({'event':'whole-speed-fourth-derivative-proved','fourthDerivativeAbsoluteUpper':fourth_bound.display(),
          'speedLower':speed_min.display(),'simpsonPairs':N,'quadratureNodes':2*N,'remainder':remainder.display()})
    trig={j:cert.sincos(pi*Q(j if j<=N else j-2*N,N)) for j in range(2*N)}
    terms=[]
    for d in range(3):
        terms.append([(k,I(k*si[k][d]),I(-k*co[k][d])) for k in range(1,degree+1) if co[k][d] or si[k][d]])
    even,odd=I(0),I(0)
    for j in range(2*N):
        p=[]
        for d in range(3):
            value=I(0)
            for k,a,b in terms[d]:
                sn,cs=trig[(k*j)%(2*N)];value+=a*cs+b*sn
            p.append(value)
        speed=cert.norm2(p).sqrt()
        if j%2:odd+=speed/N
        else:even+=speed/N
        if (j+1)%2048==0:emit({'event':'simpson-nodes-covered','done':j+1,'total':2*N})
    mean=(even+2*odd)/3;arc=mean+I.raw(-remainder.hi,remainder.hi)
    half_width=(arc.upper()-arc.lower())/2
    if half_width>=target:raise ArithmeticError('Actual directed arithmetic width did not reach declared tolerance')
    numerical_arc_error=arc-I(finite_arc)
    exact_target=I(budget.P0[0]/2,budget.P0[1]/2)+I(Q(9,200)*Q(3,50)/2)
    scale=exact_target/arc;finite_scale=I(finite_target)/I(finite_arc)
    relative_scale=scale/finite_scale-1
    radius_components=[I(sum((abs(co[k][d])+abs(si[k][d]) for k in range(1,degree+1)),Q(0))) for d in range(3)]
    raw_radius=cert.upper_i(cert.norm2(radius_components).sqrt())
    absolute_scale=scale-finite_scale
    scale_difference=I.raw(absolute_scale.absupper(),absolute_scale.absupper())
    set_distance=cert.upper_i(scale_difference*raw_radius)
    for key,p in [('localCurveEnclosureSHA256',wrapper_path),('integerArithmeticSHA256',integer_path),('exactPerimeterDefinitionSHA256',budget_path)]:
        if sha(p)!=source[key]:raise RuntimeError('Dependency changed during proof')
    out={'schema':'6a65-gap105-Gamma95-strict-total-perimeter-Simpson-v1','source':source,'integerBits':cert.BITS,
         'curveDefinition':'Exact real part of complete saved complex Fourier sum; rational real coefficient pairing as R224',
         'derivativeCells':args.derivative_cells,'speedLower':speed_min.display(),'speedFourthDerivativeAbsoluteUpper':fourth_bound.display(),
         'fourthDerivativeIntegerRowsSHA256':rows.hexdigest(),'simpsonPairs':N,'quadratureNodes':2*N,
         'compositeSimpsonMean':mean.display(),'provedMeanIntegralRemainder':remainder.display(),
         'arcRadius':arc.display(),'actualArcHalfWidthExact':str(half_width),'requestedHalfWidthExact':str(target),
         'finiteConsumerArcExact':str(finite_arc),'finiteConsumerArcError':numerical_arc_error.display(),
         'exactTargetRadius':exact_target.display(),'accurateNormalizationScale':scale.display(),
         'finiteConsumerNormalizationScale':finite_scale.display(),'relativeNormalizationScaleDifference':relative_scale.display(),
         'rawCurveDistanceFromConstantUpper':raw_radius.display(),'normalizedCurveSetHausdorffUpper':set_distance.display(),
         'wholeTotalPerimeterCertified':True,'uniformNormalizationCertified':True,
         'angularNumericalInverseErrorCertified':False,'completeC2ConsumerErrorCertified':False,
         'wholeClosedSurfaceConstructed':False,'seconds':time.monotonic()-start,'OSExitCode':None,'externalExitReceiptRequired':True}
    args.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    emit({'event':'strict-perimeter-complete','outputSHA256':sha(args.out),'arcRadius':arc.display(),
          'halfWidthExact':str(half_width),'normalizedCurveSetHausdorffUpper':set_distance.display(),'seconds':out['seconds']})

if __name__=='__main__':main()
