#!/usr/bin/env python3
"""Full-frequency zero-mean angular primitive on the actual first15 ramp cells.

The mean correction is q/a, not a constant in native theta. Exact integer
Fourier convolution retains every saved position mode; weighted Bernstein
bounds retain 1/|k| before taking absolute sums. Analytic ellipse tails and
target-radius parameter enclosures are explicit.
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


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


def upperq(q,bits=192):
    if q<0:
        raise ValueError("Nonnegative upper bound required")
    scale=1<<bits
    return Q((q.numerator*scale+q.denominator-1)//q.denominator,scale)


def roundq(q,bits):
    scale=1<<bits
    return (2*q.numerator*scale+q.denominator)//(2*q.denominator)


def ellipse_fourier(A,B,abox,terms=64,bits=180):
    """Exact analytic factorization; finite coefficients and full Wiener tail."""
    if not A>B>0:
        raise ValueError("Actual noncircular ellipse with A>B>0 required")
    center=(A+B)/2
    z=(A-B)/(A+B)
    inv=[Q(1)]
    ell=[Q(1)]
    for n in range(1,terms+2):
        inv.append(inv[-1]*z*Q(2*n-1,2*n))
        ell.append(ell[-1]*z*Q(2*n-3,2*n))
    invsum=sum(inv[:terms+1],Q(0))
    ellsum=sum(map(abs,ell[:terms+1]),Q(0))
    invtail=abs(inv[terms+1])/(1-z)
    elltail=abs(ell[terms+1])/(1-z)
    inv_tail_product=(2*invsum*invtail+invtail**2)/center
    ell_tail_product=center*(2*ellsum*elltail+elltail**2)
    invexact=[]
    ellexact=[]
    for k in range(terms+1):
        invexact.append(sum((inv[m+k]*inv[m] for m in range(terms-k+1)),Q(0))/center)
        ellexact.append(center*sum((ell[m+k]*ell[m] for m in range(terms-k+1)),Q(0)))
    amid=Q(roundq((abox[0]+abox[1])/2,192),1<<192)
    parameter_inverse_error=max(abs(1/amid-1/abox[0]),abs(1/amid-1/abox[1]))
    inverse=[0]*(4*terms+1)
    normalized=[0]*(4*terms+1)
    inv_round_error=Q(0)
    norm_round_error=Q(0)
    ell_finite_norm=abs(ellexact[0])+2*sum(map(abs,ellexact[1:]),Q(0))
    for k in range(terms+1):
        ir=roundq(invexact[k],bits)
        nr=roundq(ellexact[k]/amid,bits)
        weight=1 if k==0 else 2
        inv_round_error+=weight*abs(invexact[k]-Q(ir,1<<bits))
        norm_round_error+=weight*abs(ellexact[k]/amid-Q(nr,1<<bits))
        inverse[2*terms+2*k]=inverse[2*terms-2*k]=ir
        normalized[2*terms+2*k]=normalized[2*terms-2*k]=nr
    # The exact Fourier constant of ell/a_ellipse is one. Replacing this
    # coefficient by its exact value removes its error; the full previous
    # bound remains conservative.
    normalized[2*terms]=1<<bits
    return dict(inverse=inverse,normalized=normalized,bits=bits,degree=2*terms,
        inverseError=upperq(inv_tail_product+inv_round_error),
        normalizedError=upperq(ell_tail_product/abox[0]+ell_finite_norm*parameter_inverse_error+norm_round_error),
        inverseNorm=1/B,
        normalizedNorm=upperq((ell_finite_norm+ell_tail_product)/abox[0]),
        inverseTail=upperq(inv_tail_product),
        normalizedTail=upperq(ell_tail_product/abox[0]),
        terms=terms,gapRatio=z)


def real_laurent_product(poly,real,gram):
    maximum=max(abs(x).bit_length() for row in poly for part in row for x in part)
    realmax=max(abs(x).bit_length() for x in real)
    packing_bits=maximum+realmax+len(real).bit_length()+3
    packed_real=gram.pack(real,packing_bits)
    count=len(poly[0][0])+len(real)-1
    result=[]
    for row in poly:
        result.append([gram.unpack(gram.pack(part,packing_bits)*packed_real,packing_bits,count) for part in row])
    return result,packing_bits


def primitive_bernstein_l1(poly,bits,L):
    """Exact sup_t sum_{k!=0} |Fourier coefficient|/|k|, full frequencies."""
    radial_degree=len(poly)-1
    fourier_degree=(len(poly[0][0])-1)//2
    denominator=math.lcm(*(math.comb(radial_degree,j) for j in range(radial_degree+1)))
    freqden=math.lcm(*range(1,fourier_degree+1))
    weights=[0 if k==0 else freqden//abs(k) for k in range(-fourier_degree,fourier_degree+1)]
    largest=0
    for i in range(radial_degree+1):
        row=[[0]*len(weights),[0]*len(weights)]
        for j in range(i+1):
            weight=math.comb(i,j)*(denominator//math.comb(radial_degree,j))
            for part in range(2):
                for k,value in enumerate(poly[j][part]):
                    row[part][k]+=weight*value
        if row[0][fourier_degree] or row[1][fourier_degree]:
            raise ArithmeticError("The native-theta mean must vanish exactly")
        value=sum(abs(row[part][k])*weights[k] for part in range(2) for k in range(len(weights)))
        largest=max(largest,value)
    return Q(largest,denominator*freqden*(1<<bits))/L


def actual_cell(model,index,gr,gram,cert,ellipse,abox):
    start=time.monotonic()
    C,bits,L,sx0=model.cell(index)
    U=gram.angular(C,model.degree)
    maximum=max(abs(x).bit_length() for row in U for pair in row for part in pair for x in part)
    # Full 769-mode real representation, all six radial coefficients and xyz.
    operations=12*3*len(U)*(2*model.degree+1)
    gram_packing_bits=2*maximum+operations.bit_length()+3
    G=gram.packed_gram(U,U,gram_packing_bits,True)
    gbits=2*bits
    Gdegree=(len(G[0][0])-1)//2
    p,pbits,perror,pbounds=gram.target_ratio(sx0,L,model.ramp,model.v,abox)
    # N=p G_s-2 p_s G = p r_s-2 p_s r. Keep the exact cancellation before
    # taking any Fourier l1 norm or applying the primitive weight.
    N=[[[0]*len(G[0][0]) for _ in range(2)] for _ in range(len(G)+len(p)-2)]
    for i,row in enumerate(G):
        for j,pj in enumerate(p):
            n=i+j-1
            if n<0 or not pj or i==2*j:
                continue
            weight=(i-2*j)*pj
            for part in range(2):
                for k,value in enumerate(row[part]):
                    N[n][part][k]+=weight*value
    nbits=gbits+pbits
    Gnorm=upperq(gram.bernstein_l1(G,gbits))
    Gsnorm=upperq(gram.bernstein_l1(G,gbits,L,1))
    Nnorm=upperq(gram.bernstein_l1(N,nbits)/L)
    deltaN=upperq(upperq(perror[0])*Gsnorm+2*upperq(perror[1])*Gnorm)
    R,product_bits=real_laurent_product(N,ellipse['inverse'],gram)
    rbits=nbits+ellipse['bits']
    degree=Gdegree+ellipse['degree']
    if len(R[0][0])!=2*degree+1:
        raise ArithmeticError("Incorrect exact full-frequency Laurent support")
    Rzero=[[[row[0][degree]],[row[1][degree]]] for row in R]
    RzeroBound=upperq(gram.bernstein_l1(Rzero,rbits)/L)
    T=[[[x<<ellipse['bits'] for x in part] for part in row] for row in R]
    offset=degree-ellipse['degree']
    for n,row in enumerate(R):
        for j,hj in enumerate(ellipse['normalized']):
            if not hj:
                continue
            for part in range(2):
                T[n][part][offset+j]-=hj*row[part][degree]
    tbits=rbits+ellipse['bits']
    if any(row[part][degree] for row in T for part in range(2)):
        raise ArithmeticError("Weighted native-theta mean subtraction failed")
    weighted=upperq(primitive_bernstein_l1(T,tbits,L))
    deltaR=upperq(deltaN*ellipse['inverseNorm']+Nnorm*ellipse['inverseError'])
    deltaT=upperq((1+ellipse['normalizedNorm'])*deltaR+ellipse['normalizedError']*RzeroBound)
    # p>=1 throughout this expanding ramp. No rounded p replaces this fact.
    pmin=Q(1)
    pmax,pfirst=map(upperq,pbounds[:2])
    gb=gr['completeRawNativeGramBounds']
    r0,r1,r2=(Q(row['rational']) for row in gb['GminusTarget'])
    qmin=cert.I(model.B**2-r0).sqrt().lower()
    rho=upperq(r0/(qmin+model.B))
    amin=abox[0]-rho
    if amin<=0:
        raise ArithmeticError("No positive exact perimeter lower bound")
    n_sup=upperq(pmax*r1+2*pfirst*r0)
    e_difference=upperq(n_sup*r0/(2*pmin*qmin*model.B*(qmin+model.B)))
    m0=upperq((RzeroBound+deltaR)/(2*pmin**2))
    mean_e=upperq(m0+e_difference)
    h_sup=model.A/abox[0]
    density_difference=upperq(rho/amin*(1+h_sup))
    Hremainder=upperq((1+h_sup)*e_difference+density_difference*mean_e)
    piup=cert.pi_interval().upper()
    primitive_remainder=upperq(piup*Hremainder)
    # H and H0 have zero theta mean; a shortest complementary arc gives pi,
    # and the Fourier primitive itself retains every 1/|k| denominator.
    W=upperq((weighted+deltaT)/pmin**2+primitive_remainder)
    return dict(index=index,fullRealPositionFourierDegree=model.degree,
        fullGramFourierDegree=Gdegree,fullPrimitiveFourierDegree=degree,
        retainedAllSavedHighFrequencies=True,nativeWeightedMeanExactlyZero=True,
        gramPackingBits=gram_packing_bits,ellipseProductPackingBits=product_bits,
        exactBounds={key:gram.upper(value) for key,value in dict(
            GFourierNorm=Gnorm,GsFourierNorm=Gsnorm,
            numeratorFourierNorm=Nnorm,numeratorParameterError=deltaN,
            Rzero=RzeroBound,RapproximationError=deltaR,TapproximationError=deltaT,
            fullWeightedPrimitive=weighted,actualVersusEllipticE=e_difference,
            exactMeanE=mean_e,normalizedSpeedDensityDifference=density_difference,
            zeroMeanRemainderPrimitive=primitive_remainder,
            actualAngularInverseTangentialSpeed=W).items()},
        exactIdentity='q*theta_s=-primitive[e-(q/a)*mean(e)]; H0=[N/ell-(ell/a_ellipse)*mean(N/ell)]/(2*p^2)',
        seconds=time.monotonic()-start)


def normalization_row(index,gr,cr,pr,model,g,cert):
    I,up,lo=cert.I,cert.upper_i,cert.lower_i
    B=I(model.B)
    fmin=lo(I(Q(g['exactEllipticArcRadiusInterval'][0])))
    U=up(I(model.v)/fmin)
    U1=up(I(model.v/model.ramp)*Q(630,256)/fmin+U.square())
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
    mean_e=I(Q(pr['exactBounds']['exactMeanE']['rational']))
    angular_speed=I(Q(pr['exactBounds']['actualAngularInverseTangentialSpeed']['rational']))
    rho=up(r0/(qmin+B))
    amin=lo(fmin-rho)
    dilation_error=up(rho/amin)
    lambda_min=lo(1-dilation_error)
    lambda_max=up(1+dilation_error)
    lambda_first=up(lambda_max*mean_e/amin)
    # m_s is still bounded by the complete eta1; only actual m and W are refined.
    lambda_second=up(lambda_max*(2*mean_e.square()/amin.square()+U*mean_e/amin+eta1/amin))
    M0=norms['X']
    M1=up((1+epsE).sqrt())
    Mss=norms['Xss']
    Q0=up(2*M0)
    C1=up(M1+Q0*eta/amin)
    C2=up(Mss+(2*(M1+C1)*eta+U*Q0*eta+Q0*eta1)/amin)
    velocity_error=up(dilation_error*(M1+C1)+lambda_max*angular_speed+lambda_first*Q0)
    normalized_E=up(epsE+2*M1*velocity_error+velocity_error.square())
    normalized_F=up(epsF/qmin+velocity_error)
    normalized_metric=up(normalized_E/2+((normalized_E/2).square()+normalized_F.square()).sqrt())
    sigma=lo((1-delta).sqrt())
    tau=up((dilation_error*C1+lambda_first*Q0)/lambda_min)
    alpha=up(tau/sigma)
    if alpha.hi>=I(1).lo:
        raise ArithmeticError("No positive normalized immersion margin")
    normal_difference=up(2*alpha)
    ambient_second=up((cert.max_upper(Mss,norms['Xthetatheta']/B.square())
        +norms['Xstheta']/B)/(1-delta))
    remainder_ss=up(2*lambda_first*(M1+C1)+dilation_error*C2+lambda_second*Q0)
    remainder=up((remainder_ss+lambda_first*norms['Xtheta']/B)/(1-delta))
    normalized_curvature=up((lambda_max*raw_kappa+lambda_max*normal_difference*ambient_second+remainder)
        /(lambda_min.square()*(1-alpha).square()))
    values=dict(rawKappa=raw_kappa,rawRelativeMetric=delta,
        eBound=eta,eRadialDerivativeBound=eta1,refinedMeanE=mean_e,
        refinedAngularInverseTangentialSpeed=angular_speed,
        dilationError=dilation_error,dilationFirst=lambda_first,dilationSecond=lambda_second,
        positionFromMean=Q0,meanFirst=C1,meanSecond=C2,
        completeNormalizedRadialVelocityError=velocity_error,
        normalizedEError=normalized_E,normalizedFOverf=normalized_F,
        normalizedSpectralMetric=normalized_metric,
        normalizedOwnCurvature=normalized_curvature)
    return {key:value.display() for key,value in values.items()}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--master',type=Path,required=True)
    ap.add_argument('--gram-report',type=Path,required=True)
    ap.add_argument('--curvature-report',type=Path,required=True)
    ap.add_argument('--scripts-dir',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--cell',type=int,action='append')
    ap.add_argument('--ellipse-terms',type=int,default=64)
    ap.add_argument('--metric-threshold',default='1/1000000')
    ap.add_argument('--curvature-threshold',default='1000/97')
    args=ap.parse_args()
    if args.output.exists():
        raise FileExistsError("Fresh actual full-frequency primitive certificate required")
    start=time.monotonic()
    gram_path=args.scripts_dir/'6a65-geometry-ramp-native-gram-certificate.py'
    helper=args.scripts_dir/'6a65-m12-r137-continuous-domain.py'
    gram=module(gram_path,'actual_primitive_gram')
    cert=module(helper,'actual_primitive_integer_arithmetic')
    gram.convolution_fixture()
    model=gram.ActualRamp(args.master)
    g=json.loads(args.gram_report.read_text())
    c=json.loads(args.curvature_report.read_text())
    master_hash=sha(args.master)
    if (g.get('allFirst15PolynomialCellsProved') is not True or c.get('allFirst15PolynomialCellsProved') is not True
        or g['source']['masterSHA256']!=master_hash or c['source']['masterSHA256']!=master_hash
        or c['source']['gramReportSHA256']!=sha(args.gram_report)):
        raise ValueError("Actual complete same-master certificates required")
    selected=list(range(15)) if args.cell is None else args.cell
    if not selected or len(set(selected))!=len(selected) or any(not 0<=j<15 for j in selected):
        raise ValueError("Distinct actual cells 0..14 required")
    abox=tuple(map(Q,g['exactEllipticArcRadiusInterval']))
    ellipse=ellipse_fourier(model.A,model.B,abox,args.ellipse_terms)
    print(json.dumps(dict(event='exact-ellipse-factorization-ready',
        terms=args.ellipse_terms,inverseError=gram.upper(ellipse['inverseError']),
        normalizedError=gram.upper(ellipse['normalizedError']),seconds=time.monotonic()-start)),flush=True)
    rows=[]
    for j in selected:
        gr,cr=g['rows'][j],c['rows'][j]
        if gr['index']!=j or cr['index']!=j:
            raise ValueError("Complete ordered certificate rows required")
        row=actual_cell(model,j,gr,gram,cert,ellipse,abox)
        row['normalization']=normalization_row(j,gr,cr,row,model,g,cert)
        row['passed']=(Q(row['normalization']['normalizedSpectralMetric']['hi'])<Q(args.metric_threshold)
            and Q(row['normalization']['normalizedOwnCurvature']['hi'])<Q(args.curvature_threshold))
        rows.append(row)
        print(json.dumps(dict(event='actual-full-frequency-primitive-cell',index=j,
            W=row['exactBounds']['actualAngularInverseTangentialSpeed'],
            meanE=row['exactBounds']['exactMeanE'],
            metric=row['normalization']['normalizedSpectralMetric'],
            curvature=row['normalization']['normalizedOwnCurvature'],
            passed=row['passed'],seconds=time.monotonic()-start)),flush=True)
    if sha(args.master)!=master_hash:
        raise RuntimeError("Master changed during exact proof")
    maximum_metric=max(Q(row['normalization']['normalizedSpectralMetric']['hi']) for row in rows)
    maximum_curvature=max(Q(row['normalization']['normalizedOwnCurvature']['hi']) for row in rows)
    out=dict(schema='6a65-actual-first15-full-frequency-weighted-native-mean-primitive-normalization-v1',
        source=dict(masterSHA256=master_hash,gramReportSHA256=sha(args.gram_report),
            rawCurvatureReportSHA256=sha(args.curvature_report),gramCheckerSHA256=sha(gram_path),
            integerArithmeticSHA256=sha(helper),entrySHA256=sha(__file__)),
        ellipseFactorization=dict(terms=args.ellipse_terms,roundedDyadicBits=ellipse['bits'],
            gapRatio=str(ellipse['gapRatio']),
            bounds={k:gram.upper(ellipse[k]) for k in ('inverseError','normalizedError','inverseNorm','normalizedNorm','inverseTail','normalizedTail')}),
        normalizedFieldDefinition='exact perimeter-weighted center and lambda=f/a, exact angular inverse; exact elliptic a_ellipse initial f',
        nativeMeanSubtraction='H=e-(q/a)*mean(e), H0=[N/ell-(ell/a_ellipse)*mean(N/ell)]/(2*p^2)',
        allFourierPrimitiveWeightsRetained=True,allSavedCoefficientsConsumed=True,
        meanERefinedBeforeDilationDerivative=True,
        maximumNormalizedSpectralMetric=gram.upper(maximum_metric),
        maximumNormalizedOwnCurvature=gram.upper(maximum_curvature),
        metricThreshold=args.metric_threshold,curvatureThreshold=args.curvature_threshold,
        selectedCellIndices=selected,rows=rows,
        allFirst15PolynomialCellsProved=selected==list(range(15)) and all(row['passed'] for row in rows),
        literalFloatingQuadratureNormalizationCertified=False,
        finalExactCoastPortCellExcluded=True,wholeRampCertified=False,
        exactIsometryClaimed=False,wholeClosedReachCertified=False,
        seconds=time.monotonic()-start,OSExitCode=None,externalExitReceiptRequired=True)
    args.output.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(event='actual-primitive-complete',reportSHA256=sha(args.output),
        maximumNormalizedSpectralMetric=out['maximumNormalizedSpectralMetric'],
        maximumNormalizedOwnCurvature=out['maximumNormalizedOwnCurvature'],
        allFirst15PolynomialCellsProved=out['allFirst15PolynomialCellsProved'],seconds=out['seconds'])),flush=True)
    if not all(row['passed'] for row in rows):
        raise SystemExit(2)


if __name__=='__main__':
    main()

