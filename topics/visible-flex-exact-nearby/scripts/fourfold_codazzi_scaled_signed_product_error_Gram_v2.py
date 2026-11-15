#!/usr/bin/env python3
"""Scaled exact dyadics and signed output-side errors for fixed matrix products.

Only finite Arb enclosures enter. Binary64 arrays choose normalized exact
dyadic centres; no positive weight, slack or scale is converted to float.
Old binary64 receipts remain readable, unchanged.
"""
from __future__ import annotations
from fractions import Fraction
import numpy as np
from flint import arb,arb_mat
import fourfold_codazzi_complete_directional_matrix_Green as matrix
import fourfold_codazzi_complete_same97_cap_posterior as cap

q,norm,exact,eye,zero=matrix.q,matrix.norm,matrix.exact,matrix.eye,matrix.zero
transpose,sym,record=matrix.transpose,matrix.sym,matrix.record
positive,sqrt_upper=matrix.nonnegative,matrix.sqrt_upper
REPRESENTATION='exact_power_of_two_scaled_two_dyadic_signed_covariance_v1'

def power2(exponent):
    exponent=int(exponent)
    if abs(exponent)>2**30:
        raise ArithmeticError('a finite dyadic scale exceeded the explicit arithmetic resource range')
    return arb(2)**exponent if exponent>=0 else arb(1)/(arb(2)**(-exponent))

def upper_exponent(value):
    """The least integer e with value<=2**e; zero has no finite exponent."""
    value=positive(value)
    if value.is_zero():return None
    if value==1:return 0
    if value>1:
        lo,hi=0,1
        while power2(hi)<value:lo,hi=hi,2*hi
    else:
        lo,hi=-1,0
        while power2(lo)>value:hi,lo=lo,2*lo
        if power2(lo)==value:return lo
    while hi-lo>1:
        middle=(lo+hi)//2
        if power2(middle)>=value:hi=middle
        else:lo=middle
    if not power2(hi)>=value:
        raise ArithmeticError('the exact dyadic exponent failed its directed comparison')
    return hi

def upper_dyadic(value):
    exponent=upper_exponent(value)
    if exponent is None:return arb(0),dict(mantissa=0,binary_exponent=0)
    result=power2(exponent)
    return result,dict(mantissa=1,binary_exponent=exponent)

def read_dyadic(receipt):
    if receipt.get('mantissa')==0 and receipt.get('binary_exponent')==0:return arb(0)
    if receipt.get('mantissa')!=1 or type(receipt.get('binary_exponent')) is not int:
        raise ValueError('a positive arbitrary-exponent dyadic receipt changed')
    return power2(receipt['binary_exponent'])

def finite_matrix(A):
    if not all(A[i,j].is_finite() for i in range(A.nrows()) for j in range(A.ncols())):
        raise ArithmeticError('a signed matrix contains a genuinely nonfinite Arb entry')

def choose_centres(A):
    """Choose the original exact binary64 centres without an unused norm.

    Entry order, float(mid) conversion, dtype and exact reconstruction are
    the immutable pilot's choose() implementation. Finiteness is checked
    explicitly; the caller still pays its complete used rounding bound.
    """
    finite_matrix(A)
    values=np.array([[float(A[i,j].mid()) for j in range(A.ncols())]
                     for i in range(A.nrows())],dtype='<f8')
    if not np.isfinite(values).all():
        raise ArithmeticError('a new exact dyadic matrix is nonfinite')
    return values,exact(values)

def choose_scaled(A,key,arrays,symmetric=False):
    finite_matrix(A)
    if symmetric:
        if A.nrows()!=A.ncols():raise ValueError('a signed covariance is not square')
        A=sym(A)
    scale_exponent=upper_exponent(norm(A))
    if scale_exponent is None:scale_exponent=0
    scale=power2(scale_exponent);normalized=A/scale
    hi,H=choose_centres(normalized)
    lo,L=choose_centres(normalized-H)
    if symmetric:
        for i in range(A.nrows()):
            for j in range(i):
                hi[i,j]=hi[j,i];lo[i,j]=lo[j,i]
    if not np.isfinite(hi).all() or not np.isfinite(lo).all():
        raise ArithmeticError('a normalized chosen dyadic centre is nonfinite')
    normalized_selected=exact(hi)+exact(lo)
    selected=normalized_selected*scale
    arrays[key+'_hi']=matrix.pack_symmetric(hi) if symmetric else hi
    arrays[key+'_lo']=matrix.pack_symmetric(lo) if symmetric else lo
    receipt=dict(rows=A.nrows(),columns=A.ncols(),symmetric_triangles=symmetric,
        hi_array_key=key+'_hi',lo_array_key=key+'_lo',
        exact_binary_scale_exponent=scale_exponent,
        exact_definition='2**scale_exponent*(exact(hi)+exact(lo)); no floating addition or scale')
    return selected,receipt,norm(A-selected).upper(),normalized,normalized_selected

def read_selected(arrays,receipt):
    nr,nc=receipt['rows'],receipt['columns']
    hi,lo=arrays[receipt['hi_array_key']],arrays[receipt['lo_array_key']]
    if receipt['symmetric_triangles']:
        if nr!=nc:raise ValueError('a packed scaled matrix is not square')
        hi,lo=matrix.unpack_symmetric(hi,nr),matrix.unpack_symmetric(lo,nr)
    if hi.shape!=(nr,nc) or lo.shape!=(nr,nc):
        raise ValueError('a complete scaled dyadic matrix lost its dimensions')
    if not np.isfinite(hi).all() or not np.isfinite(lo).all():
        raise ValueError('a saved normalized centre is nonfinite')
    return (exact(hi)+exact(lo))*power2(receipt['exact_binary_scale_exponent'])

def covariance_bound(A,key,arrays):
    A=sym(A);n=A.nrows()
    selected,centre,rounding,normalized,normalized_selected=choose_scaled(A,key,arrays,True)
    normalized_rounding=norm(normalized-normalized_selected).upper()
    slack,slack_receipt=upper_dyadic(normalized_rounding)
    scale=power2(centre['exact_binary_scale_exponent'])
    upper=sym(selected+eye(n)*(scale*slack))
    finite_matrix(upper)
    receipt=dict(representation=REPRESENTATION,dimension=n,centre=centre,
        exact_normalized_diagonal_slack=slack_receipt,
        full_signed_rounding_upper=record(rounding),
        complete_trace_upper=record(positive(matrix.trace(upper))),
        exact_bound='2**scale*(exact(hi)+exact(lo)+exact(normalized_slack)*I)',
        all_signed_correlations_and_independent_mean_kept=True)
    return upper,receipt

def read_covariance(arrays,receipt):
    if receipt.get('representation')!=REPRESENTATION:
        return matrix.read_covariance(arrays,receipt)
    n=receipt['dimension'];centre=receipt['centre']
    if centre['rows']!=n or centre['columns']!=n or not centre['symmetric_triangles']:
        raise ValueError('one complete scaled covariance changed its representation')
    value=read_selected(arrays,centre)
    slack=read_dyadic(receipt['exact_normalized_diagonal_slack'])
    return sym(value+eye(n)*(power2(centre['exact_binary_scale_exponent'])*slack))

def selected_product_step(Di,E,W,key,arrays):
    """True Enew-Eselected has output-side covariance bounded by Wnew."""
    if Di.nrows()!=Di.ncols() or Di.ncols()!=E.nrows() or W.nrows()!=E.nrows() or W.ncols()!=E.nrows():
        raise ValueError('the full product/error dimensions differ')
    candidate=Di*E
    selected,centre,rounding,unused,unused2=choose_scaled(candidate,key+'_E',arrays)
    propagated=sym(Di*W*transpose(Di))
    radius=positive(rounding);propagated_norm=positive(norm(propagated))
    eta=arb(0);eta_receipt=dict(mantissa=0,binary_exponent=0)
    if radius.is_zero():
        bound=propagated
    elif propagated_norm.is_zero():
        bound=eye(Di.nrows())*(radius*radius)
    else:
        eta,eta_receipt=upper_dyadic((radius/propagated_norm.sqrt()).upper())
        if not eta>0:raise ArithmeticError('the product-error Young weight is not strictly positive')
        bound=sym(propagated*(1+eta)+eye(Di.nrows())*((1+1/eta)*radius*radius))
    output,wr=covariance_bound(bound,key+'_W',arrays)
    receipt=dict(selected_product=centre,complete_output_error_Gram=wr,
        complete_candidate_rounding_upper=record(radius),
        propagated_signed_error_norm_upper=record(propagated_norm),
        exact_positive_Young_weight=eta_receipt,
        complete_selected_product_norm_upper=record(norm(selected).upper()),
        complete_product_error_norm_upper=record(sqrt_upper(norm(output))),
        true_Di_interval_used_in_both_candidate_and_congruence=True,
        exact_error_identity='Delta_new=Di_true*Delta_old+(Di_true*Eselected_old-Eselected_new)',
        no_product_error_is_a_physical_state_jump=True)
    return selected,output,receipt

def sandwich(E,W,J):
    """A true full-input Gram bound, retaining signed E^* J E."""
    n=E.ncols()
    if (E.nrows(),W.nrows(),W.ncols(),J.nrows(),J.ncols())!=(n,n,n,n,n):
        raise ValueError('the complete product sandwich lost a coordinate or mean')
    main=sym(transpose(E)*J*E)
    noise=positive(matrix.dot_trace(J,W))
    main_norm=positive(norm(main))
    eta=arb(0);eta_receipt=dict(mantissa=0,binary_exponent=0)
    if noise.is_zero():result=main
    elif main_norm.is_zero():result=eye(n)*noise
    else:
        eta,eta_receipt=upper_dyadic((noise/main_norm).sqrt().upper())
        if not eta>0:raise ArithmeticError('the sandwich Young weight is not strictly positive')
        result=sym(main*(1+eta)+eye(n)*((1+1/eta)*noise))
    finite_matrix(result)
    return result,dict(signed_error_objective_trace_upper=record(noise),
        selected_Gram_norm_upper=record(main_norm),exact_positive_Young_weight=eta_receipt,
        output_side_error_Gram_used=True,
        normalization_requires_full_Cstar_H_C=True)

def weighted_add(accum,weight_sum,component):
    size=positive(norm(component))
    if size.is_zero():return accum,weight_sum,arb(0)
    alpha,receipt=upper_dyadic(size.sqrt().upper())
    if not alpha>0:raise ArithmeticError('a nonzero Gram needs a strictly positive exact weight')
    return sym(accum+component/alpha),(weight_sum+alpha).upper(),alpha

def weighted_pair(A,B):
    accum=zero(A.nrows(),A.ncols());weight=arb(0);chosen=[]
    for component in (A,B):
        accum,weight,alpha=weighted_add(accum,weight,component)
        chosen.append(dict(exact_power_of_two_weight=upper_dyadic(alpha)[1]))
    return sym(accum*weight),dict(exact_positive_weights=chosen,
        positive_weight_sum_upper=record(weight),two_terms_not_declared_orthogonal=True)

def weighted_cap_Gram(terms,H):
    active=[];weight_sum=arb(0)
    for name,c,G in terms:
        c=positive(c)
        if c==0:continue
        T=sym(G*(c*c));tr=positive(matrix.trace(T))
        if tr==0:continue
        objective=matrix.dot_trace(H,T)
        objective_for_choice=max(positive(objective),(tr*power2(-160)).upper())
        alpha,encoded=upper_dyadic(objective_for_choice.sqrt().upper())
        if not alpha>0:raise ArithmeticError('a nonzero cap Gram lost its positive exact weight')
        active.append((name,T,alpha,encoded,objective,tr));weight_sum+=alpha
    if not active:return zero(97,97),[]
    result=zero(97,97);receipt=[]
    for name,T,alpha,encoded,objective,tr in active:
        result+=T*(weight_sum/alpha)
        receipt.append(dict(name=name,strictly_positive_exact_weight=encoded,
            objective_trace_upper=record(objective),complete_PSD_trace_upper=record(tr),
            zero_directional_objective_does_not_delete_a_nonzero_matrix=True))
    return sym(result),receipt

def whole_cap_candidates(G,constants,H,output,key):
    kappa=matrix.up(constants['full_repaired_cap_kappa'])
    cstar=matrix.up(constants['actual_true_left_complete_even_map_norm_squared']).sqrt().upper()
    result={};diagnostics={}
    for group,terms in cap.complete_groups(G,constants).items():
        E,weights=weighted_cap_Gram(terms,H)
        E,er=covariance_bound(sym(E*kappa*kappa),key+'_'+group+'_error',output)
        nested,nested_weights=weighted_cap_Gram([
            ('complete_infinite_trial_high',arb(1),G['W_T']),
            ('complete_same_input_adjoint_error',cstar,E)],H)
        nested,nr=covariance_bound(nested,key+'_'+group+'_nested',output)
        direct,direct_weights=weighted_cap_Gram(
            [('complete_infinite_trial_high',arb(1),G['W_T'])]
            +[(name,(cstar*kappa*c).upper(),T) for name,c,T in terms],H)
        direct,dr=covariance_bound(direct,key+'_'+group+'_direct',output)
        for form,W,receipt,ww in (('nested',nested,nr,nested_weights),
                ('one_complete_Cauchy',direct,dr,direct_weights)):
            name=group+'_'+form;result[name]=W
            diagnostics[name]=dict(complete_Wcap=receipt,complete_Werr=er,
                full_cap_operator_upper=record(cap.norm_upper(W).sqrt().upper()),
                signed_objective_trace_upper=record(matrix.dot_trace(H,W)),
                actual_error_weights=weights,actual_complete_cap_weights=ww,
                complete_body_choice=group,complete_Young_choice=form,
                all97_directions_and_mean_retained=True)
    selected=min(result,key=lambda name:positive(matrix.dot_trace(H,result[name])))
    return result,diagnostics,selected
