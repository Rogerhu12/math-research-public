#!/usr/bin/env python3
"""Whole true-inner-tail mean branch and cap-integral outward budgets.

Pure source, no actual q/input/workflow. Scientific calls belong to a later
declared public Actions scope. The caller's complete exact-germ/source-error
evidence remains necessary; finite-M/ODE observations are not certificates.
No old DtN, seed ODE or geometry is replayed by this algebraic helper.

Formulas and full continuous-domain proof:
notes/2026-11-27-r618-true-tail-mean-anchor-bounds.md.
All original/new coefficients must be supplied, including ones whose float
evaluation underflows. A zero-centered integral enclosure is not zero tail
continuation. The real mean height remains the integral from the true cap.
"""
from collections import defaultdict
import hashlib
import os
from pathlib import Path

BACKEND_SHA = 'eb18fb8c5bc5d44ce16aa8cfe3708197e72167e0c6885deb128816e96a902c5f'
path = Path(__file__).with_name('r611_circular_reference_global_geometry_20261127.py')
if hashlib.sha256(path.read_bytes()).hexdigest() != BACKEND_SHA:
    raise RuntimeError('the outward interval backend changed')
from r611_circular_reference_global_geometry_20261127 import I,exp_i,sqrt_i

COUNTS = defaultdict(int)
KEYS = ('r','q','t')


def public_only():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('whole-tail scientific arithmetic requires the declared public Actions scope')


def intervals(*values):
    if not all(isinstance(value,I) for value in values):
        raise TypeError('outward input intervals, including literal real parameters, are required')


def positive(*values):
    intervals(*values)
    if any(value.lo <= 0 for value in values):
        raise ArithmeticError('required positive whole-tail input is unresolved')


def nonnegative(*values):
    intervals(*values)
    if any(value.lo < 0 for value in values):
        raise ArithmeticError('required nonnegative whole-tail majorant is unresolved')


def upper(value):
    """The exact represented quantity is proved nonnegative at each call."""
    return I(0,max(0.,value.hi))


def total(values):
    answer = I(0)
    for value in values:
        nonnegative(value)
        answer += value
    return upper(answer)


def empty_budget():
    return {'scaled':{key:I(0) for key in KEYS},
            'integral':{key:I(0) for key in KEYS}}


def add_budgets(budgets):
    public_only()
    result = empty_budget()
    for budget in budgets:
        for kind in ('scaled','integral'):
            if set(budget[kind]) != set(KEYS):
                raise ValueError('all three complete height-derivative budgets are required')
            for key in KEYS:
                nonnegative(budget[kind][key])
                result[kind][key] = upper(result[kind][key]+budget[kind][key])
        COUNTS['complete_response_budget_columns'] += 1
    return result


def normalized_old_mode_ratio(*,mode,display_log,normalization_abs):
    """(24): exact infinite germ, all u>=108 and radial orders0,1,2.

    display_log and normalization_abs refer to the SAME mathematical field,
    not an unvalidated replacement of an ODE/core output by an exact value.
    The finite-M and dense evaluation errors remain caller-owned inputs.
    """
    public_only()
    if not isinstance(mode,int) or not 2 <= mode <= 32:
        raise ValueError('this paid finite-set bound covers exactly2<=j<=32')
    intervals(display_log);positive(normalization_abs)
    COUNTS['exact_old_germ_ratio_bounds'] += 1
    return upper(exp_i(I(750)-display_log)/normalization_abs)


def old_mode_response_budget(*,mode,coefficient_abs,ratio_bound,rc,mouth,W_upper):
    """Complete old cosine column, with its genuine nonzero tail integral."""
    public_only()
    if not isinstance(mode,int) or not 2 <= mode <= 32:
        raise ValueError('old mode outside its existing proved range')
    nonnegative(coefficient_abs,ratio_bound,W_upper)
    positive(rc,mouth-rc)
    true_rc,true_ell = I(11)/50,I(1)/5
    if (not rc.lo <= true_rc.lo <= true_rc.hi <= rc.hi
            or (true_ell/(mouth-true_rc)).lo < 108):
        raise ArithmeticError('the original normalized-germ bound only covers its true rc and u>=108')
    value = upper(coefficient_abs*ratio_bound)
    integral = upper((mouth-rc)*W_upper*value)
    return {'scaled':{'r':value,'q':upper(mode*value),'t':upper(mode*mode*value)},
            'integral':{'r':integral,'q':upper(mode*integral),'t':upper(mode*mode*integral)}}


def gaussian_column_bounds(*,rc,ell,A,mouth,denominator,cutoff_left,cutoff_right,
                           degree,mode):
    """(13)--(18), without a sampled tail or an underflow-to-zero rule.

    Interval U is the actual mouth coordinate. Its lower endpoint supplies
    a conservative common infinite window; no material points are removed.
    The combined exponent in T/W is formed directly, never as T*exp(3U).
    """
    public_only()
    if (not isinstance(degree,int) or degree < 0
            or not isinstance(mode,int) or mode < 1):
        raise ValueError('actual integer radial degree and angular mode required')
    positive(rc,ell,A,mouth-rc,denominator,cutoff_left-rc,cutoff_right-cutoff_left)
    intervals(mouth,cutoff_left,cutoff_right)
    if denominator.hi > 40 or mouth.hi > cutoff_left.lo:
        raise ArithmeticError('whole window must have the original cutoff identically one and a<=40')
    u_interval = ell/(mouth-rc)
    if u_interval.lo < 100:
        raise ArithmeticError('Gaussian monotonicity window u>=100 not covered')
    U = I(u_interval.lo)
    ua = ell/(cutoff_left-rc)
    coefficient = (ell/(cutoff_right-rc))**degree*U**(-degree)
    exponential = (ua**2-U**2)/denominator
    F0 = upper(coefficient*exp_i(exponential))
    K0 = upper(coefficient*exp_i(exponential+3*U)/A)
    d1 = (2*U**3/denominator+degree*U)/ell
    d2 = (4*U**6/denominator**2+(4*degree+6)*U**4/denominator
          +(degree*degree+degree)*U**2)/ell**2
    F1,F2 = upper(d1*F0),upper(d2*F0)
    K1,K2 = upper(d1*K0),upper(d2*K0)
    J = upper(denominator*ell/(2*U**3)*F0)
    log_W_derivative_polynomial = (3*U**2+U**3)/ell
    source_W = upper(mouth*F2+log_W_derivative_polynomial*(mouth*F1+mode*mode*F0))
    source_W2 = upper(mouth*K2+log_W_derivative_polynomial*(mouth*K1+mode*mode*K0))
    COUNTS['true_Gaussian_tail_column_bounds'] += 1
    return {'mode':mode,'degree':degree,'whole_u_lower':U.lo,
        'absolute_threejet_upper':(F0,F1,F2),'over_W_threejet_upper':(K0,K1,K2),
        'integral_absolute_value_upper':J,'integral_absolute_r_derivative_upper':F0,
        'L_j_over_W_upper':source_W,'L_j_over_W_squared_upper':source_W2,
        'unbounded_log_W_derivative_handled_inside_each_decreasing_product':True,
        'source_not_claimed_to_solve_the_nonlinear_required_forcing':True}


def gaussian_response_budget(column,coefficient_abs):
    public_only()
    nonnegative(coefficient_abs)
    j = column['mode'];K0,K1,_ = column['over_W_threejet_upper']
    F0 = column['integral_absolute_r_derivative_upper']
    J = column['integral_absolute_value_upper']
    return {'scaled':{'r':upper(coefficient_abs*K1),
            'q':upper(j*coefficient_abs*K0),'t':upper(j*j*coefficient_abs*K0)},
        'integral':{'r':upper(coefficient_abs*F0),
            'q':upper(j*coefficient_abs*J),'t':upper(j*j*coefficient_abs*J)}}


def original_envelope_bounds(*,seed_ratio_bounds,height_scales,envelope_scale,
        rc,ell,A,mouth,R,p,gamma,W_upper):
    """(26)--(27), retaining the old positive quartic-exponential term."""
    public_only()
    if len(seed_ratio_bounds) != 4 or len(height_scales) != 4:
        raise ValueError('all four original pre-tanh seed norms are required')
    positive(rc,ell,A,mouth-rc,R-mouth,p,gamma,envelope_scale,*height_scales)
    nonnegative(W_upper,*seed_ratio_bounds)
    if (R-rc).hi > 1:
        raise ArithmeticError('the declared old envelope proof uses0<R-rc<=1')
    u = ell/(mouth-rc)
    if u.lo < 108:
        raise ArithmeticError('all original germ bounds require the common u>=108 window')
    U = I(u.lo)
    if (5/U-4*gamma*U**3/ell**4+3).hi >= 0:
        raise ArithmeticError('whole quartic-exponential derivative envelope unresolved')
    G0 = upper(exp_i(-gamma*U**4/ell**4+3*U)/A)
    G1 = upper((4*gamma*U**5/ell**5+p/(R-mouth))*G0)
    sum_squares = total([upper((c/m)**2) for c,m in zip(seed_ratio_bounds,height_scales)])
    B0 = upper((W_upper*sum_squares+G0)/envelope_scale)
    B1 = upper((2*W_upper*sum_squares+G1)/envelope_scale)
    COUNTS['original_complete_envelope_bounds'] += 1
    return {'value_over_W':B0,'radial_derivative_over_W':B1,
            'quartic_value_over_W':G0,'quartic_radial_derivative_over_W':G1}


def original_reference_scaled_jets(*,seed_ratio_bounds,seed_coefficient_abs,
        bulk_coefficient_abs,basis_value_bounds,basis_derivative_bounds,
        envelope,post_scaled_budget,W_upper,saturation):
    """(28)--(29): actual canonical512 reference, all original coefficients.

    post_scaled_budget includes the actual old q's homogeneous corrections
    and the complete fixed forced-j4 tail coefficient. It cannot be omitted.
    This function does not replace the original canonical mean functional.
    """
    public_only()
    modes = (2,4,6,8)
    if (len(seed_ratio_bounds) != 4 or len(seed_coefficient_abs) != 4
            or len(bulk_coefficient_abs) != 4
            or len(basis_value_bounds) != len(basis_derivative_bounds)
            or any(len(row) != len(basis_value_bounds) for row in bulk_coefficient_abs)
            or set(post_scaled_budget) != set(KEYS)):
        raise ValueError('complete original four-mode/B-spline/forced dictionaries required')
    nonnegative(W_upper,*seed_ratio_bounds,*seed_coefficient_abs,
                *basis_value_bounds,*basis_derivative_bounds,*post_scaled_budget.values())
    positive(saturation)
    B0,B1 = envelope['value_over_W'],envelope['radial_derivative_over_W']
    nonnegative(B0,B1)
    vr,vq,vt = [],[],[]
    for j,C,a,coefficients in zip(modes,seed_ratio_bounds,seed_coefficient_abs,bulk_coefficient_abs):
        nonnegative(*coefficients)
        value = upper(a*C+total([upper(b*B0*P) for b,P in zip(coefficients,basis_value_bounds)]))
        radial = upper(a*C+total([upper(b*(B1*P+B0*Q))
                    for b,P,Q in zip(coefficients,basis_value_bounds,basis_derivative_bounds)]))
        vr.append(radial);vq.append(upper(j*value));vt.append(upper(j*j*value))
        COUNTS['original_reference_coefficients_bound'] += 1+len(coefficients)
    Vr,Vq,Vt = total(vr),total(vq),total(vt)
    return {'r':upper(2*Vr+post_scaled_budget['r']),
        'q':upper(Vq+post_scaled_budget['q']),
        't':upper(Vt+2*W_upper/saturation*Vq**2+post_scaled_budget['t'])}


def uniform_mean_branch(*,rc,mouth,W_upper,E_lower,E_upper,L,
                        reference_scaled,response_budget):
    """(4)--(12), including the same reference E's whole-tail bracket.

    Failure is explicit. Merely checking endpoint root signs, finiteness of
    the response, or Gaussian flatness does not satisfy this whole box.
    source-error certification is NOT created by these positive arithmetic
    inequalities; it remains part of the caller's actual bound provenance.
    """
    public_only()
    positive(rc,mouth-rc,E_lower,E_upper,L)
    nonnegative(W_upper)
    if set(reference_scaled) != set(KEYS):
        raise ValueError('all reference derivative norms, including the fixed force, are required')
    nonnegative(*reference_scaled.values(),*response_budget['scaled'].values())
    Ar,Aq,At = [upper(reference_scaled[k]+response_budget['scaled'][k]) for k in KEYS]
    if (L+Ar).hi >= 1:
        raise ArithmeticError('inner negative-slope branch is not covered')
    P = 1+L+Ar
    beta2 = 1-(W_upper*Aq/rc)**2
    positive(beta2)
    beta = sqrt_i(beta2)
    nminus = 1-W_upper**2*P*At/(rc*beta**3)
    nplus = 1/beta+W_upper**2*P*At/(rc*beta**3)
    vminus2 = E_lower-W_upper**2*P**2/beta2
    Cminus = rc*(1-L-Ar)-E_upper*At
    positive(nminus,vminus2,Cminus)
    vminus = sqrt_i(vminus2)
    kappa = Cminus/(mouth*E_upper*sqrt_i(E_upper))
    positive(kappa)
    low_reference_margin = nminus**2-E_lower
    high_reference_margin = E_upper-W_upper**2*P**2/beta2-nplus**2
    positive(low_reference_margin,high_reference_margin)
    lr = At/(vminus*rc*beta**3)+nplus*P/(vminus**3*beta2)
    lt = P/(vminus*rc*beta**3)
    lq = (Aq/(vminus*rc**2*beta**3)
          +3*W_upper**2*P*At*Aq/(vminus*rc**3*beta**5)
          +nplus*W_upper**2*P**2*Aq/(vminus**3*rc**2*beta**4))
    ell = dict(zip(KEYS,(upper(lr),upper(lq),upper(lt))))
    displacement = total([upper(ell[k]*response_budget['scaled'][k]) for k in KEYS])
    margin = kappa*L-displacement
    positive(margin)
    COUNTS['whole_true_tail_mean_branch_boxes'] += 1
    result = {'kappa':kappa,'ell':ell,'lambda_radius_upper':upper(displacement/kappa),
        'strict_branch_margin':margin,'beta_squared':beta2,'N_lower':nminus,
        'speed_squared_lower':vminus2,'pointwise_C_over_W_negative_margin':Cminus,
        'reference_root_lower_sign_margin':low_reference_margin,
        'reference_root_upper_sign_margin':high_reference_margin,
        'same_reference_E_enclosure':I(E_lower.lo,E_upper.hi),
        'all_radial_points_below_the_original_mouth_and_all_angles_covered':True,
        'source_error_certification_supplied_by_this_arithmetic':False}
    result['mean_height_integral_radius'] = mean_integral_radius(result,response_budget)
    return result


def mean_integral_radius(branch,direction_budget):
    """(12) for the response itself or one actual full parameter direction."""
    public_only()
    if set(direction_budget['integral']) != set(KEYS):
        raise ValueError('all actual direction integral norms required')
    nonnegative(*direction_budget['integral'].values())
    positive(branch['kappa'])
    COUNTS['true_cap_to_mouth_mean_or_parameter_integral_bounds'] += 1
    return upper(total([upper(branch['ell'][k]*direction_budget['integral'][k])
                        for k in KEYS])/branch['kappa'])


