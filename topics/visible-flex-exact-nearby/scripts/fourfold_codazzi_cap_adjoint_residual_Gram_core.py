#!/usr/bin/env python3
"""Complete physical-adjoint ordinary residual Grams from cached scalar jets.

All matrix off-diagonal signs and the independent even mean are retained.
No intrinsic target is evaluated. This module only encloses known finite
Hermite trials; it does not assert an adjoint inverse or a global cap bound.
"""
from __future__ import annotations
import hashlib,json,math
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from flint import arb
from fourfold_phase_beta_bulk_box import Box,CBox,zeros,arb_box,reduce_box,DirectedFFT
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_codazzi_physical_cap_coefficient_jets import PhysicalCapCoefficientJets,ffrac
from fourfold_codazzi_physical_cap_matrix_residual_packed_v5 import (
    hermite_series,radial_legendre,coefficient_samples,truncate_scalar,lift)
from fourfold_codazzi_reciprocal_continuous_residual_v3 import (
    add,mul,scale,scalar_budget,target_model,BudgetPolynomial)
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_final_continuous_value_repair import iter_repair

M,COLS,ANGLE,CUTOFF=128,97,1024,128
CURRENT='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
CENTRE='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
BACKGROUND='35db98d4124d50ef3bd69f3ec3aa6906289e3f6083c3ba91c8197da7547830ff'
LOCAL='bf42a295c892ec3bc606efaa9a94f2870609b73226f2034a9cbc172f187186bd'
POINT='41156aa8ac5b124b2ccca96e2f52b210edf1a3f5c170fdf839e66bf0602725b8'
LEFT,RIGHT=Fraction(9,10),Fraction(25,8)


def positive(value):
    v=box_from_record(value) if isinstance(value,dict) else arb(value)
    v=v.upper()
    if not v.is_finite() or v<0:raise ArithmeticError('a complete nonnegative scalar budget is invalid')
    return v


def scale_matrix(A,value):return Box.coerce(A)*arb_box(arb(value))


def transpose(A):return Box(A.lo.T,A.hi.T)


def zero(n=COLS):return Box(np.zeros((n,n)))


def matrix_trace(A):
    v=reduce_box(Box(np.diag(A.lo),np.diag(A.hi)))
    result=arb(float(v.hi)).upper()
    if not result.is_finite() or result<0:raise ArithmeticError('a Gram trace upper bound is invalid')
    return result


def gram_rows(values):
    """Directed exact dot products, without a heuristic BLAS error model."""
    X=Box.coerce(values)
    if X.lo.ndim!=2 or X.lo.shape[1]!=COLS:raise ValueError('all97 input columns are required')
    out=zero()
    for first in range(0,len(X.lo),16):
        row=X[first:first+16];count=len(row.lo)
        # Each multiplication and pairwise reduction is an original directed
        # Box operation. Signed cross-column terms are never replaced by abs.
        out=out+reduce_box(row.reshape(count,COLS,1)*row.reshape(count,1,COLS),0)
    return out


def gram_polynomial(values,length,weights):
    """Full angular Parseval Gram and exact radial Legendre integration."""
    if length<=0:raise ValueError('a true positive radial measure is required')
    weights=Box.coerce(weights)
    result=zero()
    for k,coefficient in enumerate(radial_legendre(values)):
        if coefficient.lo.shape[0]!=weights.lo.shape[0]:
            raise ValueError('the complete output Gram has wrong angular weights')
        # weights is used as a square weight directly. Do not take an
        # approximate square root or lose the independent mean weight1.
        rows=coefficient;part=zero()
        for first in range(0,len(rows.lo),16):
            row=rows[first:first+16];count=len(row.lo)
            w=weights[first:first+16].reshape(count,1,1)
            part=part+reduce_box(w*row.reshape(count,COLS,1)*row.reshape(count,1,COLS),0)
        result=result+scale_matrix(part,exact_arb(length)/int(2*k+1))
    return result


def pair_Gram(odd,even,length):
    if not odd or not even:raise ValueError('both complete adjoint components are required')
    ob=odd[0].lo.shape[0];ec=even[0].lo.shape[0]
    wb=Box(np.full(ob,.5));wc=Box(np.r_[1.,np.full(ec-1,.5)])
    return gram_polynomial(odd,length,wb)+gram_polynomial(even,length,wc)


def field_Grams(values,length):
    """Known B,C and both angular derivatives, including the full C mean."""
    if any(v.lo.shape!=(257,97) for v in values):
        raise ValueError('the exact full257 by97 Hermite coefficients are required')
    B=[v[:M] for v in values];C=[v[M:] for v in values]
    f=Box(4*np.arange(1,M+1,dtype=float)).reshape(M,1)
    fp=Box(np.r_[0.,4*np.arange(1,M+1,dtype=float)]).reshape(M+1,1)
    BP=[v*f for v in B];CP=[v*fp for v in C]
    return dict(B=gram_polynomial(B,length,Box(np.full(M,.5))),
        C=gram_polynomial(C,length,Box(np.r_[1.,np.full(M,.5)])),
        Btheta=gram_polynomial(BP,length,Box(np.full(M,.5))),
        Ctheta=gram_polynomial(CP,length,Box(np.r_[1.,np.full(M,.5)])))


def cauchy_Gram(terms):
    """Fixed positive scalar weights, valid for all97 inputs simultaneously."""
    active=[];alphas=[]
    for name,coefficient,G in terms:
        c=positive(coefficient)
        if c==0:continue
        trace=(c*c*matrix_trace(G)).upper()
        if trace==0:continue
        chosen=float(trace.sqrt())
        if not math.isfinite(chosen):raise ArithmeticError('a Cauchy weight selection overflowed')
        if chosen<=0:chosen=math.ldexp(1.,-1022)
        alpha=exact_arb(Fraction.from_float(chosen))
        active.append((name,c,G,alpha));alphas.append(alpha)
    if not active:return zero(),[]
    total=sum(alphas,arb(0));out=zero();audit=[]
    for name,c,G,alpha in active:
        out=out+scale_matrix(G,total*c*c/alpha)
        audit.append(dict(name=name,positive_weight_binary64_hex=float(alpha).hex(),
            complete_coefficient_upper=record(c),physical_Gram_trace_upper=record(matrix_trace(G))))
    return out,audit


def covariance_enclosure(A,key,arrays):
    """A true signed PSD upper matrix; entrywise uppers are not a Gram."""
    n=A.lo.shape[0]
    if A.lo.shape!=(n,n):raise ValueError('a complete square covariance is required')
    lo=np.maximum(A.lo,A.lo.T);hi=np.minimum(A.hi,A.hi.T)
    if np.any(lo>hi):raise ArithmeticError('the exact symmetric Gram enclosures disagree')
    chosen=lo/2+hi/2
    for i in range(n):
        for j in range(i):chosen[i,j]=chosen[j,i]
    radius=(Box(lo,hi)-Box(chosen)).abs_upper()
    row_sum=reduce_box(Box(radius),1)
    slack=float(np.max(row_sum.hi))
    if not math.isfinite(slack) or slack<0:raise ArithmeticError('the full symmetric rounding radius is invalid')
    # For the true symmetric matrix H, ||H-chosen||2 <= max row abs sum.
    # Thus chosen+slack I is a Loewner upper, with the exact dyadic slack.
    ii=np.triu_indices(n);arrays[key+'_triangle']=np.asarray(chosen[ii],dtype='<f8')
    exact_upper=Box(chosen)+Box(np.eye(n)*slack)
    receipt=dict(dimension=n,array_key=key+'_triangle',
        exact_diagonal_slack_binary64_hex=slack.hex(),
        complete_symmetric_error_row_sum_upper=record(arb(slack)),
        trace_upper=record(matrix_trace(exact_upper)),
        full_signed_cross_column_covariance_kept=True,
        bound='exact(saved symmetric dyadic)+exact(saved dyadic slack)*I')
    return exact_upper,receipt


class CachedCoefficientProvider:
    """Original directed coefficient algorithm, with zero target construction."""
    def __init__(self,candidate,repair):
        p=PhysicalCapCoefficientJets.__new__(PhysicalCapCoefficientJets)
        p.candidate=Path(candidate);p.repair_report=Path(repair);p.object_path=None
        if hashlib.sha256(p.candidate.read_bytes()).hexdigest()!=CURRENT:
            raise ValueError('the original complete moving candidate index changed')
        p.width=Fraction(1,16);p.N=ANGLE;p.cutoff=CUTOFF;p.half_width=Fraction(0)
        p.saved=load_candidate(candidate);meta=json.loads(str(p.saved['metadata']))
        p.alpha=Fraction(meta['exact_float_amplitude']);p.nu=Fraction(meta['exact_float_nu'])
        if int(meta['modes'])!=32 or p.saved['piece_coefficients'].shape!=(4,6144,65):
            raise ValueError('the original complete65-slot moving centre is required')
        p.mc=32;p.knots=list(map(ffrac,p.saved['radial_nodes']))
        import gzip
        d=json.loads(gzip.decompress(Path(repair).read_bytes()))
        encoded=(json.dumps(d['definition'],sort_keys=True,separators=(',',':'))+'\n').encode()
        if (not d.get('complete') or d.get('derived_definition_sha256')!=CENTRE
            or hashlib.sha256(encoded).hexdigest()!=CENTRE):
            raise ValueError('the exact actual continuous centre is required')
        h=hashlib.sha256();lower=[];upper=[]
        for piece,offset,_ in iter_repair(p.saved,p.alpha):
            h.update((json.dumps(dict(piece=piece,physical_offset=list(map(str,offset))),
                sort_keys=True,separators=(',',':'))+'\n').encode())
            row=[arb_box(exact_arb(v)) for v in offset]
            lower.append([float(v.lo) for v in row]);upper.append([float(v.hi) for v in row])
        if h.hexdigest()!=d['definition']['offset_sequence_sha256']:
            raise ValueError('one exact full repair offset changed')
        p.offsets=Box(np.asarray(lower),np.asarray(upper));p.target=None
        p.fft=DirectedFFT();seed=zeros((ANGLE,32))
        for j in range(32):seed[j+1,j]=1.
        p.roots=p.fft.fft(seed,inverse=True)*ANGLE
        p.freq=4*np.arange(1,33);p.cosfreq=np.r_[0,p.freq]
        self.provider=p;self.old_target_calls=0

    def from_saved(self,row):
        p=self.provider;left,right=map(Fraction,row['interval']);mid=(left+right)/2;half=(right-left)/2
        piece=bisect_right(p.knots,left)-1
        if not p.knots[piece]<=left<right<=p.knots[piece+1]:
            raise ValueError('the cached complete quarter crosses an original centre cubic')
        whole={k:box_from_record(v) for k,v in row['all_original_target_coefficients'].items()}
        centre={k:box_from_record(v) for k,v in row['intrinsic_midpoint_jets'].items()}
        original_germ=tuple(map(Fraction,row['actual_scalar_germ']))
        if not original_germ[0]<=left<right<=original_germ[1]:
            raise ValueError('the exact original scalar germ no longer contains this quarter')
        wholejets=p.local_jets(piece,left,right,whole);centjets=p.local_jets(piece,mid,mid,centre)
        analytic=p.analytic_bounds(wholejets);dft,sample=p.inverse_samples(centjets,analytic)
        models={name:p.fourier_model(dft,analytic[name],half,j) for j,name in enumerate(('QB','QC'))}
        scalar={name:target_model(centre,whole,name,half) for name in ('gamma','beta','K','s')}
        return dict(models=models,scalar=scalar,whole=whole,centre=centre,analytic=analytic,
            sample=sample,piece=piece,germ=original_germ,left=left,right=right,half=half,
            original_cached_quarter_request=row['request'],new_intrinsic_target_calls=0)



def affine_restriction(values,offset,ratio):
    """Enclose the same exact polynomial on a true closed subinterval."""
    if not Fraction(0)<ratio<=1 or abs(offset)+ratio>1:
        raise ValueError('the new affine interval must be contained in the old quarter')
    out=[values[0]*0 for _ in values]
    for k,value in enumerate(values):
        for j in range(k+1):
            out[j]=out[j]+value*arb_box(exact_arb(
                Fraction(math.comb(k,j))*offset**(k-j)*ratio**j))
    return out


def restrict_coefficient(coefficient,left,right):
    left,right=Fraction(left),Fraction(right)
    if not coefficient['left']<=left<right<=coefficient['right']:
        raise ValueError('a restricted coefficient model escaped its original complete quarter')
    out=dict(coefficient);mid=(coefficient['left']+coefficient['right'])/2
    offset=((left+right)/2-mid)/coefficient['half']
    ratio=(right-left)/(2*coefficient['half'])
    # The underlying exact polynomial is restricted, never resampled.  Since
    # |offset|+ratio<=1, its true coefficient l1 norm cannot increase.
    # All old uniform errors therefore remain valid without differentiation.
    models={}
    for name,model in coefficient['models'].items():
        models[name]=SimpleNamespace(coefficients=affine_restriction(model.coefficients,offset,ratio),
            norm=model.norm,error=model.error,analytic_taylor_norms=model.analytic_taylor_norms,
            detailed_error=model.detailed_error)
    scalar={}
    for name,value in coefficient['scalar'].items():
        p=value if isinstance(value,BudgetPolynomial) else scalar_budget(value)
        scalar[name]=BudgetPolynomial(affine_restriction(p.coefficients,offset,ratio),p.norm,p.error)
    out.update(models=models,scalar=scalar,left=left,right=right,half=(right-left)/2,
        exact_affine_restriction=dict(offset=str(offset),ratio=str(ratio),
            source_interval=list(map(str,(coefficient['left'],coefficient['right'])))))
    return out


def hermite_subinterval(nodes,state,dleft,dright,left,right):
    nodes=[Fraction(v) for v in nodes];left,right=Fraction(left),Fraction(right)
    piece=bisect_right(nodes,left)-1
    if piece<0 and LEFT<=left<nodes[0]:piece=0
    if not ((nodes[piece]<=left or piece==0 and LEFT<=left<nodes[0])
        and left<right<=nodes[piece+1]):
        raise ValueError('a true Hermite intersection or the first exact9/10 extension failed')
    value,derivative=hermite_series(state[piece],state[piece+1],
        dleft[piece],dright[piece],nodes[piece],nodes[piece+1],left,right)
    return value,derivative,piece


def synthesize(values,N,fft,angular=False):
    block=zeros((N,len(values),COLS))
    modes=np.r_[np.arange(N//2),np.arange(-N//2,0)]
    multiplier=CBox(0.,Box(4*modes).reshape(N,1))
    for j,value in enumerate(values):
        pair=lift(value,M,N);b=pair[:,0];c=pair[:,1]
        if angular:b=b*multiplier;c=c*multiplier
        block[:,j]=b+CBox(-c.imag,c.real)
    f=fft.fft(block,inverse=True)*N
    return [f.real[:,j] for j in range(len(values))],[f.imag[:,j] for j in range(len(values))]


def finite_residual_coefficients(B,C,fft,N,support):
    degree=max(len(B),len(C));block=zeros((N,degree,COLS))
    null=Box(np.zeros((N,COLS)))
    for j in range(degree):block[:,j]=CBox(B[j] if j<len(B) else null,C[j] if j<len(C) else null)
    F=fft.fft(block)/N;modes=np.r_[np.arange(N//2),np.arange(-N//2,0)]
    outside=abs(modes)>support;odd=[];even=[]
    for j in range(degree):
        row=F[:,j]
        if not (np.all((row.real.lo<=0)&(row.real.hi>=0))
            and np.all((row.imag.lo[outside]<=0)&(row.imag.hi[outside]>=0))):
            raise ArithmeticError('the complete exact odd/even finite support was lost')
        y=row.imag;indices=np.arange(1,support+1)
        odd.append(y[-indices]-y[indices])
        even.append(Box(np.vstack((y.lo[0],(y[indices]+y[-indices]).lo)),
                        np.vstack((y.hi[0],(y[indices]+y[-indices]).hi))))
    return odd,even


def coefficient_product_error(scalar,coefficient):
    return (positive(scalar.error)*positive(coefficient.norm)
        +(positive(scalar.norm)+positive(scalar.error))*positive(coefficient.error)).upper()


def adjoint_cell_Grams(cached,coefficient,values,derivative):
    p=cached.provider;N=p.N
    if N<=2*(M+p.cutoff):raise ValueError('all finite physical products must remain resolved')
    B,C=synthesize(values,N,p.fft);Br,Cr=synthesize(derivative,N,p.fft)
    BP,CP=synthesize(values,N,p.fft,angular=True)
    qb,qc=[coefficient['models'][name] for name in ('QB','QC')]
    QB=coefficient_samples(qb,N,p.fft);QC=coefficient_samples(qc,N,p.fft)
    g,b,K,s=[coefficient['scalar'][name] if isinstance(coefficient['scalar'][name],BudgetPolynomial)
        else scalar_budget(coefficient['scalar'][name]) for name in ('gamma','beta','K','s')]
    ell=K*s*s;a=truncate_scalar(g*ell);e=truncate_scalar(b*(ell+1))
    RB=add(scale(Br,-1),scale(mul(b.coefficients,B),2))
    RB=add(add(RB,mul(g.coefficients,mul(QB,BP))),mul(g.coefficients,CP))
    RB=add(RB,scale(mul(b.coefficients,mul(QB,C)),-1))
    RC=add(scale(Cr,-1),mul(g.coefficients,mul(QC,BP)))
    RC=add(add(RC,scale(mul(a.coefficients,BP),-1)),scale(mul(b.coefficients,mul(QC,C)),-1))
    RC=add(RC,mul(e.coefficients,C))
    fb,fc=finite_residual_coefficients(RB,RC,p.fft,N,M+p.cutoff)
    length=coefficient['right']-coefficient['left']
    finite=pair_Gram(fb,fc,length);fields=field_Grams(values,length)
    gb,bb=coefficient_product_error(g,qb),coefficient_product_error(b,qb)
    gc,bc=coefficient_product_error(g,qc),coefficient_product_error(b,qc)
    EB,weightsB=cauchy_Gram([
        ('2 beta error times B',2*positive(b.error),fields['B']),
        ('gamma QB full error times Btheta',gb,fields['Btheta']),
        ('gamma full error times Ctheta',positive(g.error),fields['Ctheta']),
        ('beta QB full error times C',bb,fields['C'])])
    EC,weightsC=cauchy_Gram([
        ('gamma QC and gamma ell full errors times Btheta',gc+positive(a.error),fields['Btheta']),
        ('beta QC and beta ell plus1 full errors times C',bc+positive(e.error),fields['C'])])
    return dict(finite=finite,coefficient_remainder=EB+EC,fields=fields,
        finite_support=M+p.cutoff,full_coefficient_tail_retained=True,
        independent_mean_retained=True,new_target_calls=0,
        complete_error_coefficients={k:record(v) for k,v in (
            ('beta',positive(b.error)),('gamma',positive(g.error)),('gammaQB',gb),('betaQB',bb),
            ('gammaQC',gc),('betaQC',bc),('gammaell',positive(a.error)),
            ('betaellplus1',positive(e.error)))},
        remainder_cauchy_weights=dict(B=weightsB,C=weightsC),
        finite_radial_degree=max(len(fb),len(fc))-1)


def actual_Hessian_coefficients(point,background,local):
    if (point.get('complete_local_rows')!=1341 or len(point.get('rows',[]))!=1341
        or not point.get('complete') or point.get('failure')
        or point.get('derived_continuous_centre_definition_sha256')!=CENTRE
        or local.get('derived_definition_sha256')!=CENTRE or not local.get('complete')
        or point.get('exact_affine_offset')!='0'):
        raise ValueError('the complete same-centre original Hessian inputs are required')
    C=positive(background['bounds']['physical_C_A_1over64'])
    result=[]
    for i,(row,original) in enumerate(zip(point['rows'],local['rows'])):
        audit=row.get('merged_residual')
        if (row.get('local_source_row')!=i or row.get('interval')!=original.get('interval')
            or not audit or not audit.get('ordinary_zero_order')
            or len(audit.get('complete_physical_pointwise_A0',[]))!=2):
            raise ValueError('one complete native-point centre-residual coefficient row is missing')
        RV=positive(audit['complete_physical_pointwise_A0'][1])
        z={k:positive(v) for k,v in audit['ordinary_zero_order'].items()}
        if set(z)!={'ZBB','ZBC','ZCC'}:raise ValueError('the complete triangular Hessian zero-order rows are required')
        result.append(dict(interval=list(map(Fraction,row['interval'])),local_index=i,
            Einf=(arb.pi()*C*RV/8).upper(),E1=(2*C*RV).upper(),**z))
    if (result[0]['interval'][0]!=LEFT or result[-1]['interval'][1]!=RIGHT
        or any(a['interval'][1]!=b['interval'][0] for a,b in zip(result,result[1:]))):
        raise ValueError('the complete1341 Hessian cells have a gap')
    return result


def Hessian_Gram(coefficients,fields):
    r=coefficients
    B,a=cauchy_Gram([('Einf times Btheta',r['Einf'],fields['Btheta']),
        ('E1 plus ZBB times B',r['E1']+r['ZBB'],fields['B'])])
    C,b=cauchy_Gram([('Einf times Ctheta',r['Einf'],fields['Ctheta']),
        ('ZBC times B',r['ZBC'],fields['B']),
        ('E1 plus ZCC times C',r['E1']+r['ZCC'],fields['C'])])
    return B+C,dict(B=a,C=b)


def saved_model_arrays(coefficient,arrays):
    for name,model in coefficient['models'].items():
        for j,value in enumerate(model.coefficients):
            if not (np.array_equal(value.real.lo,value.real.hi)
                and np.array_equal(value.imag.lo,value.imag.hi)):
                raise ValueError('the selected finite physical coefficient is not exactly dyadic')
            arrays[f'coefficient_{name}_{j}_real']=value.real.lo
            arrays[f'coefficient_{name}_{j}_imag']=value.imag.lo


def algebra_gates():
    """Public-run checks of the real normalization and signed covariance."""
    x=np.zeros((257,COLS));x[0,0]=1.;x[0,1]=-2.;x[M,2]=3.
    h=Fraction(1,3)
    G=pair_Gram([Box(x[:M])],[Box(x[M:])],h)
    expected={(0,0):Fraction(1,6),(1,1):Fraction(2,3),
        (0,1):Fraction(-1,3),(1,0):Fraction(-1,3),(2,2):Fraction(3)}
    for ij,value in expected.items():
        exact=arb_box(exact_arb(value))
        if not (G.lo[ij]<=exact.lo<=exact.hi<=G.hi[ij]):
            raise ArithmeticError('the signed Parseval Gram normalization failed')
    linear=pair_Gram([Box(x[:M]*0),Box(x[:M])],
        [Box(x[M:]*0),Box(x[M:])],h)
    for ij,value in expected.items():
        exact=arb_box(exact_arb(value/Fraction(3)))
        if not (linear.lo[ij]<=exact.lo<=exact.hi<=linear.hi[ij]):
            raise ArithmeticError('the exact radial Legendre measure failed')
    derivatives=field_Grams([Box(x)],h)
    if not derivatives['Ctheta'].lo[2,2]<=0<=derivatives['Ctheta'].hi[2,2]:
        raise ArithmeticError('the independent even mean acquired an angular derivative')
    expected16=arb_box(exact_arb(Fraction(8,3)))
    if not (derivatives['Btheta'].lo[0,0]<=expected16.lo
        <=expected16.hi<=derivatives['Btheta'].hi[0,0]):
        raise ArithmeticError('the physical angular derivative is not4j')
    return dict(exact_signed_nonmean_Parseval=True,independent_even_mean_weight_one=True,
        exact_radial_Legendre_measure=True,physical_4j_derivative_and_mean_zero=True)
