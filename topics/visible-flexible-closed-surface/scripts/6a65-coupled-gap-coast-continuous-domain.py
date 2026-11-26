#!/usr/bin/env python3
"""Continuous integer enclosures for the actual gap1.05/v.045 Gamma95 coast.

The mathematical target f0 uses the exact original ellipse perimeter.
Its rigorous interval also contains the finite consumer's binary64 f0;
neither the midpoint of that interval nor the raw curve's perimeter defines g.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    result=importlib.util.module_from_spec(spec);spec.loader.exec_module(result);return result
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def emit(x):print(json.dumps(x,allow_nan=False),flush=True)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--scripts-dir',type=Path,required=True)
    ap.add_argument('--prefix-report',type=Path,required=True)
    ap.add_argument('--coast-master',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--cells',type=int,default=2048)
    ap.add_argument('--max-depth',type=int,default=8)
    ap.add_argument('--curvature-cap',default='19/2')
    ap.add_argument('--denominator-floor',default='9/10')
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError('Fresh certificate report required')
    if not 64<=args.cells<=32768 or not 0<=args.max_depth<=12:raise ValueError('Bounded angular enclosure refinement required')
    start=time.monotonic();report=json.loads(args.prefix_report.read_text())
    if report['schema']!='6a65-new-coupled-gap105-v045-actual-Cauchy-R137-prefix-v1':raise ValueError('The actual new prefix is required')
    if report['coast']['masterSHA256']!=sha(args.coast_master):raise ValueError('Actual coast master identity mismatch')
    if report['seed']['exactCentralDefinition']!='P(A,B)=P(7/5,1/2), A-B=21/20; unique positive solution':
        raise ValueError('Unknown exact central definition')
    wrapper_path=args.scripts_dir/'6a65-m12-ramp-coast-continuous-domain.py'
    checker_path=args.scripts_dir/'6a65-m12-r137-continuous-domain.py'
    budget_path=args.scripts_dir/'6a65-geometry-central-gap-held-budget.py'
    wrapper=load('new_gap_local_fourier_enclosures',wrapper_path);cert=wrapper.cert;I=cert.I
    budget=load('new_gap_exact_perimeter_definition',budget_path)
    with np.load(args.coast_master,allow_pickle=False) as d:
        modes=d['curve_modes'].copy();coeff=d['curve_coefficients'].copy()
        degree=int(d['degree']);numerical_f0=float(d['exact_target_radius'])
        numerical_v=float(d['v']);numerical_length=float(d['length'])
    if degree!=95 or modes.shape!=(191,) or coeff.shape!=(191,3):raise ValueError('Actual Gamma95 complete complex Fourier coefficients required')
    if set(map(int,modes))!=set(range(-degree,degree+1)):raise ValueError('Incomplete Fourier curve')
    if numerical_v!=.045 or numerical_length!=.02:raise ValueError('Wrong actual finite coast parameters')
    if not np.all(np.isfinite(coeff)):raise ValueError('Nonfinite curve')
    lookup={int(k):row for k,row in zip(modes,coeff)}
    co=[[Q.from_float(float(z.real)) for z in lookup[0]]];si=[[Q(0)]*3]
    # Re(sum c_k exp(ik theta)) is represented exactly as a real Fourier
    # curve, even if the two saved complex coefficients are not conjugate.
    # These sums/differences are rational, never rounded back to binary64.
    asymmetry=Q(0)
    for k in range(1,degree+1):
        positive,negative=lookup[k],lookup[-k]
        co.append([Q.from_float(float(a.real))+Q.from_float(float(b.real)) for a,b in zip(positive,negative)])
        si.append([Q.from_float(float(b.imag))-Q.from_float(float(a.imag)) for a,b in zip(positive,negative)])
        for a,b in zip(positive,negative):
            asymmetry=max(asymmetry,abs(Q.from_float(float(a.real))-Q.from_float(float(b.real))),
                          abs(Q.from_float(float(a.imag))+Q.from_float(float(b.imag))))
    a0=I(budget.P0[0]/2,budget.P0[1]/2)
    exact_v=Q(9,200);exact_ramp=Q(3,50);exact_length=Q(1,50)
    exact_f0=a0+I(exact_v*exact_ramp/2)
    f0=cert.hull(exact_f0,I(Q.from_float(numerical_f0)))
    v=cert.hull(I(exact_v),I(Q.from_float(numerical_v)))
    length=cert.hull(I(exact_length),I(Q.from_float(numerical_length)))
    cap=I(Q(args.curvature_cap));floor=I(Q(args.denominator_floor))
    source={'prefixReportSHA256':sha(args.prefix_report),'coastMasterSHA256':sha(args.coast_master),
            'scriptSHA256':sha(__file__),'localCurveEnclosureSHA256':sha(wrapper_path),
            'integerGeometrySHA256':sha(checker_path),'exactPerimeterSourceSHA256':sha(budget_path)}
    emit({'event':'exact-new-coast-definition','degree':degree,'initial_cells':args.cells,
          'f0':f0.display(),'v':v.display(),'length':length.display(),'source':source})
    cells,arc,quadrature,refine=wrapper.local_curve_cells(co,si,args.cells)
    center=[I(x) for x in co[0]];bounds={};row_hash=hashlib.sha256()
    leaves=0;splits=0;depth_used=0
    def consume(index,count,depth,cell):
        nonlocal leaves,splits,depth_used
        try:
            g=cert.geometry(cell,arc,f0,v,length,center)
            if g['nonzero_principal_curvature'].hi>=cap.lo or g['D'].lo<=floor.hi:
                raise ArithmeticError('Need sharper enclosure for the declared new coast')
        except ArithmeticError as e:
            if depth>=args.max_depth:raise ArithmeticError(f'Actual new coast cell {index}/{count}: {e}') from e
            splits+=1
            for child in (2*index,2*index+1):consume(child,2*count,depth+1,refine(child,2*count))
            return
        for key,value in g.items():bounds[key]=value if key not in bounds else cert.hull(bounds[key],value)
        row_hash.update((json.dumps({'index':index,'subdivisions':count,
            'bounds':{key:[val.lo,val.hi] for key,val in sorted(g.items())}},sort_keys=True)+'\n').encode())
        leaves+=1;depth_used=max(depth_used,depth)
    for j,cell in enumerate(cells):
        consume(j,args.cells,0,cell)
        if (j+1)%256==0:emit({'event':'continuous-cells-covered','coarse':j+1,'total':args.cells,'leaves':leaves,'splits':splits})
    ratio=I.raw(bounds['ratio'].absupper(),bounds['ratio'].absupper())
    ruling=cert.upper_i(length*(1+ratio.square()).sqrt());lower=cert.lower_i(bounds['nonzero_principal_curvature'])
    if lower.lo<=0:raise ArithmeticError('No strictly positive full-coast principal curvature lower bound')
    if any(sha(path)!=source[key] for path,key in [(wrapper_path,'localCurveEnclosureSHA256'),
            (checker_path,'integerGeometrySHA256'),(budget_path,'exactPerimeterSourceSHA256')]):raise RuntimeError('Source changed during actual proof')
    out={'schema':'6a65-new-gap105-v045-Gamma95-entire-coast-integer-domain-v1','source':source,
         'curveDefinition':'Real part of the saved complete Gamma95 complex Fourier sum; rational coefficient pairing, no floating symmetrization',
         'sourceCoefficientConjugacyDefectMaximum':str(asymmetry),'degree':degree,'integerBits':cert.BITS,
         'exactMetricDefinition':'a0=P(7/5,1/2)/(2*pi); f0=a0+(9/200)*(3/50)/2; f(sigma)=f0+(9/200)*sigma',
         'exactPhysicalSlope':str(exact_v),'exactPhysicalLength':str(exact_length),
         'exactTargetRadiusInterval':exact_f0.display(),'certifiedParameterIntervals':{'f0':f0.display(),'v':v.display(),'length':length.display()},
         'parameterIntervalsAlsoEncloseFiniteConsumerBinary64Values':True,'rawArcRadius':arc.display(),'arcProof':quadrature,
         'initialAngularCells':args.cells,'provedAngularLeaves':leaves,'binarySplits':splits,'maximumSubdivisionDepth':depth_used,
         'provedCurvatureCap':args.curvature_cap,'provedDenominatorFloor':args.denominator_floor,
         'wholeDomainBounds':{key:value.display() for key,value in bounds.items()},'rulingLengthUpper':ruling.display(),
         'GreenBounds':{'C0':cert.upper_i(ruling.square()/(2*lower)).display(),
                        'rulingC1':cert.upper_i(ruling/lower).display(),'rulingC2':cert.upper_i(1/lower).display()},
         'allAngularIntegerRowsSHA256':row_hash.hexdigest(),'wholeAngularAndRulingDomainCertified':True,
         'oldR221CertificateInherited':False,'approximateRampMetricContinuouslyCertified':False,
         'wholeClosedReachCertified':False,'wholeClosedSurfaceConstructed':False,
         'seconds':time.monotonic()-start,'OSExitCode':None,'externalExitReceiptRequired':True}
    args.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    emit({'event':'actual-continuous-coast-complete','outputSHA256':sha(args.out),'leaves':leaves,'splits':splits,
          'D':bounds['D'].display(),'Ut':bounds['material_derivative'].display(),
          'curvature':bounds['nonzero_principal_curvature'].display(),'seconds':out['seconds']})

if __name__=='__main__':main()
