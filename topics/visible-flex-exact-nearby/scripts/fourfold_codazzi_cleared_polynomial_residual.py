#!/usr/bin/env python3
"""Complete Codazzi residuals after exact finite denominator clearing.

The actual target is unchanged. Complete radial/Fourier candidate polynomials
are multiplied without aliasing before any radial or angular absolute bound.
Quadratic scalar target models pay their full second-derivative variation on
each actual germ. All target infinite tails and parameter uncertainty remain.
The output supplies the direct R134 weighted-error fields; no PDE existence
is inferred by this producer alone.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import math
from pathlib import Path
from types import SimpleNamespace
import time
import numpy as np
from flint import arb, ctx
from fourfold_phase_beta_bulk_box import DirectedFFT
from fourfold_phase_codazzi_coefficients import CodazziCoefficientTarget
from fourfold_phase_codazzi_continuation_validate import (
    ExactCandidate, complex_box, positive_to_full, angular_cells_taylor, maxabs)
from fourfold_phase_newton_source_centered import CenteredPolynomial
from fourfold_phase_two_jet_newton_source import (
    Box, CBox, zeros, arb_box, square_box, record, save, sha)
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_codazzi_piecewise_barrier import read_json, up


def p_add(a, b):
    zero = a[0]*0
    return [(a[j] if j < len(a) else zero)+(b[j] if j < len(b) else zero)
            for j in range(max(len(a), len(b)))]


def p_scale(a, c):
    return [v*c for v in a]


def p_mul(a, b):
    zero = a[0]*b[0]*0
    return [sum((a[j]*b[n-j] for j in range(max(0, n-len(b)+1),
                min(len(a)-1, n)+1)), zero) for n in range(len(a)+len(b)-1)]


def p_derivative(a, scale):
    return [j*a[j]*scale for j in range(1, len(a))]


def p_eval(a, value):
    result = a[-1]
    for coefficient in reversed(a[:-1]):
        result = result*value+coefficient
    return result


def parameter(x):
    return (Fraction(int(x['numerator']), int(x['denominator']))
            if isinstance(x, dict) else Fraction(x))


def actual_ball(row):
    value = arb(row['lower']).lower().union(arb(row['upper']).upper())
    if not value.is_finite():
        raise ValueError('nonfinite target coefficient')
    return value


def candidate_radial_series(candidate, piece, left, right):
    """All eight exact finite Fourier coefficients in u=(r-mid)/halfwidth."""
    lo, hi = candidate.times[piece:piece+2]
    if not lo <= left < right <= hi:
        raise ValueError('radial polynomial crosses its exact stored join')
    mid, half = (left+right)/2, (right-left)/2
    x = [CBox(arb_box(exact_arb((mid-lo)/(hi-lo)))),
         CBox(arb_box(exact_arb(half/(hi-lo))))]
    omx = [1-x[0], -x[1]]
    L, R = complex_box(candidate.ends[piece]), complex_box(candidate.ends[piece+1])
    cc = [complex_box(c) for c in candidate.corrections[piece]]
    value = [cc[5]]
    for j in range(4, -1, -1):
        value = p_add([cc[j]], p_mul(value, x if j % 2 == 0 else omx))
    value = p_add(p_add([L], p_scale(x, R-L)), p_mul(value, p_mul(x, omx)))
    if len(value) != 8:
        raise ValueError('the complete degree-seven dense polynomial is required')
    return value, half


def real_sample_series(candidate, coefficients):
    """Full B,C,Btheta,Ctheta radial series on an unaliased angular grid."""
    nr, grid = len(coefficients), candidate.grid
    block = zeros((grid, 4*nr))
    angular = CBox(0., Box(candidate.frequencies[:, None]))
    for j, value in enumerate(coefficients):
        full = positive_to_full(value, grid)
        block[:, 4*j:4*j+2] = full
        block[:, 4*j+2:4*j+4] = full*angular
    values = candidate.target.polynomial_fft.fft(block, inverse=True)*grid
    if not np.all((values.imag.lo <= 0) & (values.imag.hi >= 0)):
        raise ValueError('exact real finite candidate lost its imaginary zero')
    return [[values.real[:, 4*j+k] for j in range(nr)] for k in range(4)]


def derivative_polynomial(poly, order):
    """The entire rounding error has known finite support, so pay Bernstein."""
    modes = 4*np.asarray([j if j < poly.grid//2 else j-poly.grid
                          for j in range(poly.grid)])
    c = poly.c
    for _ in range(order):
        c = c*CBox(0., Box(modes))
    error = poly.error*arb(4*poly.degree)**order
    return CenteredPolynomial(c, error, poly.degree, poly.fft)


def numerator_polynomials(series, candidate, degree):
    """Every exact Fourier coefficient of the full radial numerator."""
    if not 2*degree < candidate.grid:
        raise ValueError('finite angular product would alias')
    block = zeros((candidate.grid, len(series)))
    for j, values in enumerate(series):
        block[:, j] = CBox(values)
    coefficients = candidate.target.polynomial_fft.fft(block)/candidate.grid
    # Only mathematically absent modes are reset by CenteredPolynomial.
    # All interval Fourier roundoff is retained on the actual support.
    return [CenteredPolynomial(coefficients[:, j], arb(0), degree,
                               candidate.target.polynomial_fft)
            for j in range(len(series))]


def radial_collapse(polys, order=0):
    # Differentiate BEFORE paying radial variation as a common Fourier error.
    # Only actual finite-support arithmetic error receives the Bernstein fee.
    differentiated = [derivative_polynomial(p, order) for p in polys]
    u = Box(-1., 1.)
    total = p_eval([p.c for p in differentiated], u)
    error = sum((p.error for p in differentiated), arb(0)).upper()
    return CenteredPolynomial(total, error, polys[0].degree, polys[0].fft)


def scalar_model(mid, full, name, half):
    """Taylor with a chosen dyadic quadratic coefficient and exact remainder."""
    derivative = (mid['a2']/mid['a']-mid['beta']**2
                  if name == 'beta' else mid[name+'1'])
    second = full[name+'2']
    h = exact_arb(half)
    coefficients = [mid[name], h*derivative, h*h*second/2]
    chosen = [float(value.mid()) for value in coefficients]
    # All three model coefficients are explicit exact dyadics. Parameter and
    # rounding uncertainty stays in the scalar remainder, never duplicated
    # into unrelated Fourier modes by an interval FFT of a common scalar.
    model = [Box(value) for value in chosen]
    remainder = sum((abs(value-arb(q)) for value,q in zip(coefficients,chosen)),arb(0)).upper()
    return model, remainder


def row_budget(candidate, target, native, angles):
    left, right = map(Fraction, native['interval'])
    piece = int(native['piece'])
    full = {key:actual_ball(value) for key, value in native['true_target_coefficients'].items()}
    if not full['K'] < 0:
        raise ValueError('true target is not strictly negatively curved')
    mid = target.coefficients((left+right)/2, (left+right)/2)
    if list(map(str, target.cell)) != native['actual_scalar_germ']:
        raise ValueError('actual target germ identity differs')
    coefficients, half = candidate_radial_series(candidate, piece, left, right)
    B, C, Bt, Ct = real_sample_series(candidate, coefficients)
    Br = p_derivative(B, arb_box(1/exact_arb(half)))
    Cr = p_derivative(C, arb_box(1/exact_arb(half)))
    km, ek = scalar_model(mid, full, 'K', half)
    gm, eg = scalar_model(mid, full, 'gamma', half)
    bm, eb = scalar_model(mid, full, 'beta', half)
    B2, C2 = p_mul(B, B), p_mul(C, C)
    v = p_add(km, B2)
    T = p_add(p_scale(p_mul(p_mul(B, Bt), C), 2), p_scale(p_mul(v, Ct), -1))
    NB = p_add(p_add(p_mul(C2, Br), p_scale(p_mul(gm, T), -1)),
               p_scale(p_mul(bm, p_mul(B, C2)), 2))
    NC = p_add(p_add(p_mul(C, Cr), p_scale(p_mul(gm, p_mul(C, Bt)), -1)),
               p_scale(p_mul(bm, p_add(v, p_scale(C2, -1))), -1))
    nb = numerator_polynomials(NB, candidate, 3*candidate.degree)
    nc = numerator_polynomials(NC, candidate, 2*candidate.degree)
    collapsed = [[radial_collapse(p, q) for q in range(2)] for p in (nb,nc)]
    numerators = [[angular_cells_taylor(p, angles) for p in row] for row in collapsed]

    # Denominators and products use actual full closed angular/radial cells.
    cp = candidate.polynomials(piece, left, right)
    b, c, bt, ct, btt, ctt = [angular_cells_taylor(cp[key], angles)
                             for key in ('B','C','Bt','Ct','Btt','Ctt')]
    if not np.all(c.hi < 0):
        raise ValueError('complete candidate denominator has no negative chart')
    ka = p_eval(km, Box(-1., 1.))
    v0 = ka+square_box(b)
    t0 = 2*b*bt*c-v0*ct
    t1 = 2*(square_box(bt)+b*btt)*c-v0*ctt
    absbox = lambda v: Box(v.abs_upper())
    errb0 = (arb_box(eg)*absbox(t0)+arb_box(abs(full['gamma'])*ek)*absbox(ct)
             +2*arb_box(eb)*absbox(b*square_box(c)))
    errb1 = (arb_box(eg)*absbox(t1)+arb_box(abs(full['gamma'])*ek)*absbox(ctt)
             +2*arb_box(eb)*absbox(bt*square_box(c)+2*b*c*ct))
    errc0 = (arb_box(eg)*absbox(c*bt)+arb_box(eb)*absbox(v0-square_box(c))
             +arb_box(abs(full['beta'])*ek))
    errc1 = (arb_box(eg)*absbox(ct*bt+c*btt)
             +arb_box(eb)*absbox(2*b*bt-2*c*ct))
    nB,nBt,nC,nCt = [value+Box(-fee.hi, fee.hi) for value,fee in
                     zip((*numerators[0],*numerators[1]),(errb0,errb1,errc0,errc1))]
    c2 = square_box(c)
    RB, RC = nB/c2, nC/c
    RBt, RCt = nBt/c2-2*nB*ct/(c2*c), nCt/c-nC*ct/c2
    k = arb_box(full['k'])
    P,Q = (b+k)/c,(b-k)/c
    Pt,Qt = bt/c-(b+k)*ct/c2,bt/c-(b-k)*ct/c2
    Ptt = btt/c-2*bt*ct/c2-(b+k)*ctt/c2+2*(b+k)*square_box(ct)/(c2*c)
    Qtt = btt/c-2*bt*ct/c2-(b-k)*ctt/c2+2*(b-k)*square_box(ct)/(c2*c)
    RP,RQ = (RB-P*RC)/c,(RB-Q*RC)/c
    RPt = (RBt-Pt*RC-P*RCt)/c-(RB-P*RC)*ct/c2
    RQt = (RBt-Qt*RC-Q*RCt)/c-(RB-Q*RC)*ct/c2
    d = 2*k/c
    SU,SV = d*(RPt-(RC/c)*Pt), d*(RQt-(RC/c)*Qt)
    S1 = 2*(bt/c-b*ct/c2)
    W0 = maxabs(d*Pt,d*Qt)
    W1 = maxabs(d*(Ptt-Pt*ct/c),d*(Qtt-Qt*ct/c))
    bounds = dict(Mhat=maxabs(P,Q), D1=maxabs(Pt,Qt), D2=maxabs(Ptt,Qtt),
        S1=maxabs(S1), What0=W0, What1=W1,
        rho0=maxabs(RP,RQ), rho1=maxabs(RPt,RQt), rhoW=maxabs(SU,SV),
        BCrho0=maxabs(RB,RC), BCrho1=maxabs(RBt,RCt),
        gamma=full['gamma'].upper(), beta=abs(full['beta']).upper(),
        kappa=abs(full['kappa']).upper(), k_lower=full['k'].lower(),
        candidate_gap=(2*full['k'].lower()/maxabs(c)).lower(),
        C_abs_lower=arb(float(np.min(-c.hi))), C_abs_upper=maxabs(c))
    return bounds,dict(K=ek,gamma=eg,beta=eb),dict(
        NB=maxabs(nB),NBtheta=maxabs(nBt),NC=maxabs(nC),NCtheta=maxabs(nCt),
        finite_NB_Wiener=(collapsed[0][0].norm()+collapsed[0][0].error).upper(),
        finite_NC_Wiener=(collapsed[1][0].norm()+collapsed[1][0].error).upper())


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--cover',type=Path,default=Path('notes/2026-11-13-Codazzi-joint-Taylor-r005-compact-native.json.gz'))
    ap.add_argument('--candidate',type=Path,default=Path('notes/2026-11-13-codazzi-dense-r005-n512-candidate.npz.gz'))
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--producer',type=Path,default=Path('scripts/fourfold_codazzi_residual_taylor_compact.py'))
    ap.add_argument('--grid',type=int,default=2048)
    ap.add_argument('--angles',type=int,default=4096)
    ap.add_argument('--rows',type=int)
    ap.add_argument('--bits',type=int,default=192)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args();ctx.prec=a.bits;ctx.cap=4
    if a.out.exists():raise FileExistsError('new output path required')
    data=read_json(a.cover)
    if (not data.get('complete') or data.get('failure') is not None
        or data['covered_interval']!=data['exact_requested_interval']
        or not data.get('whole_affine_parameter_interval')
        or not data.get('whole_real_angular_circle')):
        raise ValueError('complete original high-target cover required')
    for p,key in ((a.candidate,'candidate_sha256'),(a.object,'object_sha256'),(a.producer,'source_sha256')):
        if sha(p)!=data[key]:raise ValueError('original input changed: '+str(p))
    if data['coefficient_provider_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_high_target_jets.py')):
        raise ValueError('original high target provider changed')
    for name,digest in data['dependency_sha256'].items():
        if sha(Path(__file__).with_name(name))!=digest:raise ValueError('original dependency changed: '+name)
    if a.grid & (a.grid-1) or a.angles & (a.angles-1) or a.angles<a.grid:
        raise ValueError('power-of-two complete Fourier and angular grids required')
    target=CodazziCoefficientTarget(a.object,Fraction(data['parameter_half_width']),data['primitive_nodes'],a.angles)
    candidate=ExactCandidate(a.candidate,SimpleNamespace(product_grid=a.grid,polynomial_fft=DirectedFFT()))
    if a.grid<=6*candidate.degree:raise ValueError('grid does not retain all cubic Fourier products')
    if parameter(candidate.metadata['exact_center_parameter'])!=parameter(data['exact_center_parameter']):
        raise ValueError('exact candidate center changed')
    rows=data['rows'] if a.rows is None else data['rows'][:a.rows]
    started=time.monotonic()
    out=dict(kind='actual_complete_Codazzi_cleared_polynomial_residual_for_R134',
        complete=False,failure=None,continuation_certified=False,closed_surface_complete=False,
        whole_affine_parameter_interval=True,whole_real_angular_circle=True,
        source_sha256=sha(__file__),inputs={str(p):sha(p) for p in (a.cover,a.candidate,a.object,a.producer)},
        candidate_sha256=sha(a.candidate),object_sha256=sha(a.object),
        exact_center_parameter=data['exact_center_parameter'],parameter_half_width=data['parameter_half_width'],
        exact_requested_interval=['0',rows[-1]['interval'][1]],
        complete_input_interval=data['exact_requested_interval'],
        actual_initial_error=data['initial_error'],
        original_target_dependencies=data['dependency_sha256'],
        dependencies={n:sha(Path(__file__).with_name(n)) for n in (
            'fourfold_phase_codazzi_coefficients.py','fourfold_codazzi_high_target_jets.py',
            'fourfold_phase_codazzi_continuation_validate.py','fourfold_phase_beta_bulk_box.py',
            'fourfold_phase_newton_source_centered.py','fourfold_phase_two_jet_newton_source.py')},
        bits=a.bits,original_primitive_nodes=data['primitive_nodes'],finite_convolution_grid=a.grid,
        angular_closed_cells=a.angles,maximum_angular_product_degree=3*candidate.degree,
        exact_denominator_clearing=True,full_target_quadratic_remainder=True,rows=[])
    cursor=Fraction(0)
    try:
        for i,native in enumerate(rows):
            left,right=map(Fraction,native['interval'])
            if left!=cursor:raise ValueError('noncontiguous exact radial cover')
            bounds,remainders,nums=row_budget(candidate,target,native,a.angles)
            out['rows'].append(dict(piece=native['piece'],interval=native['interval'],
                actual_scalar_germ=native['actual_scalar_germ'],
                bounds={k:record(v) for k,v in bounds.items()},
                scalar_quadratic_remainders={k:record(v) for k,v in remainders.items()},
                numerator_bounds={k:record(v) for k,v in nums.items()},
                true_target_coefficients=native['true_target_coefficients']))
            cursor=right;out['covered_interval']=['0',str(cursor)]
            out['wall_seconds']=time.monotonic()-started;save(a.out,out)
            print(dict(row=i,right=str(right),rho0=bounds['rho0'].str(10),
                rho1=bounds['rho1'].str(10),rhoW=bounds['rhoW'].str(10),
                S1=bounds['S1'].str(10),seconds=out['wall_seconds']),flush=True)
        if str(cursor)!=out['exact_requested_interval'][1]:raise ValueError('requested endpoint missing')
        out['complete']=True
    except Exception as exc:
        out['failure']=repr(exc)
    out['wall_seconds']=time.monotonic()-started;save(a.out,out)
    print(dict(complete=out['complete'],failure=out['failure'],rows=len(out['rows'])),flush=True)


if __name__=='__main__':main()
