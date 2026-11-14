#!/usr/bin/env python3
"""Correlated Taylor outer domains for full ordinary reference time segments.

The moving-frame D, M, W and their physical-angle derivatives have no D
division.  A larger time disk supplies coarse modulus bounds for these
entire germ invariants.  Their true time jets plus a complete Cauchy tail
then enclose a smaller disk sharply.  A separate physical-state Taylor
expansion pays an angular tube.  Only after D and -K are separated from zero
are field, f_theta and f_theta2 bounds formed.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
import math
from pathlib import Path
import time

import numpy as np
from flint import arb, acb, acb_series, ctx

from fourfold_phase_beta_interval import (
    series_constant, array_derivative, vector_dot, primitive_fourier_budget, ball_record,
)
from fourfold_phase_beta_bulk_interval import exact_arb, complex_pad
from fourfold_phase_beta_affine import AffineBulkTarget, sha
from fourfold_phase_field_time_taylor import (
    polynomial, polynomial_bound, pad_series, phase_evaluation, record_complex,
)
from fourfold_phase_field_time_germ_union import radial_cover
from fourfold_phase_field_time_refined_root import prepare_refined_root, RefinedGermTimeModel
from fourfold_phase_reference_time_sample import load_segment, reference_time_coefficients
from fourfold_time_angle_jets import TimeAngleJet


def frame_invariants(X, a, ar, beta, gamma, beta_r, gamma_r,
                     beta_t, gamma_t, beta_tt, gamma_tt,
                     beta_ttt, gamma_ttt, beta_rt, gamma_rt,
                     beta_rtt, gamma_rtt):
    """The exact frozen frame formulas, without any curvature or D inverse."""
    sb, cb, s, c = beta.sin(), beta.cos(), gamma.sin(), gamma.cos()
    h, v, z = -sb*X[0]+cb*X[1], -cb*X[0]-sb*X[1], X[2]
    Q, R = c*z-s*h, c*h+s*z
    P, u, p, q = 1+beta_t, gamma_t, beta_r, gamma_r
    P1, P2, u1, u2 = beta_tt, beta_ttt, gamma_tt, gamma_ttt
    p1, p2, q1, q2 = beta_rt, beta_rtt, gamma_rt, gamma_rtt
    Q1 = a*q-P*s*v-u*R
    R1 = ar+P*c*v+u*Q
    v1 = a*c*p-P*h
    h1 = ar*c-a*s*q+P*v
    Q2 = a*q1-P1*s*v-P*c*u*v-P*s*v1-u1*R-u*R1
    v2 = a*(-s*u*p+c*p1)-P1*h-P*h1
    D, M, W = P*c*Q-u*v, p*c*Q-q*v, Q*Q+v*v
    D1 = P1*c*Q-P*s*u*Q+P*c*Q1-u1*v-u*v1
    M1 = p1*c*Q-p*s*u*Q+p*c*Q1-q1*v-q*v1
    W1 = 2*(Q*Q1+v*v1)
    D2 = (P2*c*Q+2*P1*(-s*u*Q+c*Q1)
          +P*((-c*u*u-s*u1)*Q-2*s*u*Q1+c*Q2)
          -u2*v-2*u1*v1-u*v2)
    M2 = (p2*c*Q+2*p1*(-s*u*Q+c*Q1)
          +p*((-c*u*u-s*u1)*Q-2*s*u*Q1+c*Q2)
          -q2*v-2*q1*v1-q*v2)
    W2 = 2*(Q1*Q1+Q*Q2+v1*v1+v*v2)
    return dict(D=D, D1=D1, D2=D2, M=M, M1=M1, M2=M2, W=W, W1=W1, W2=W2)


def true_time_X(model, theta_coefficients):
    ctx.cap = model.work_precision
    values, _, _, error = model.image_and_X_error(theta_coefficients)
    theta = polynomial(values, model.precision)
    X = [series_constant(0, model.precision) for _ in range(3)]
    for k, frequency in enumerate(model.target.frequency):
        phase = (acb(0, frequency)*theta).exp()
        for component in range(3):
            X[component] += model.X_coefficient[k, component]*phase
    X = [pad_series(value, error, model.outer, real=all(v.imag == 0 for v in values)) for value in X]
    return X, theta, error


def true_time_invariants(model, theta_coefficients):
    X, theta, error = true_time_X(model, theta_coefficients)
    phases = phase_evaluation(model.beta, model.gamma, model.beta_r, model.gamma_r, theta)
    return frame_invariants(X, model.a, model.ar, *phases), error


def physical_state_invariants(model, theta_coefficients, state_precision):
    """True rectangular jets in time u and physical-angle offset s.

    Only the s=0 primitive is summed.  The exact identity
      d_s X = (a_r*T+a*T_r)-Jrot*X
    generates its remaining state coefficients; no angular derivative of a
    truncated primitive is substituted for the true tangent.
    """
    Xzero, theta, error = true_time_X(model, theta_coefficients)
    m, n = model.precision, int(state_precision)
    kw = dict(time_precision=m, angle_precision=n)
    wrap = lambda value: TimeAngleJet.from_time_series(value, **kw)
    zero = series_constant(0, m)
    phase_rows = [[zero for _ in range(n+3)] for _ in range(4)]
    for k, values in enumerate(zip(model.beta, model.gamma, model.beta_r, model.gamma_r), 1):
        frequency = 4*k
        sine, cosine = (frequency*theta).sin(), (frequency*theta).cos()
        periodic = [sine, cosine, -sine, -cosine]
        factor = acb(1)
        for j in range(n+3):
            if j:
                factor = factor*frequency/j
            for v, value in enumerate(values):
                phase_rows[v][j] = phase_rows[v][j]+value*periodic[j%4]*factor
    def phase(v, derivative=0):
        rows=[]
        for j in range(n):
            multiplier=math.factorial(j+derivative)//math.factorial(j)
            rows.append([multiplier*phase_rows[v][j+derivative][i] for i in range(m)])
        return TimeAngleJet(rows, **kw)
    beta, gamma, br, gr = [phase(v) for v in range(4)]
    sb, cb = beta.sin_cos();sg, cg = gamma.sin_cos()
    a, ar = wrap(model.a), wrap(model.ar)
    T = [-cg*sb, cg*cb, sg]
    Tr = [-cg*cb*br+sg*sb*gr, -cg*sb*br-sg*cb*gr, cg*gr]
    H = [ar*T[j]+a*Tr[j] for j in range(3)]
    rows = [[[Xzero[j][i] for i in range(m)]] for j in range(3)]
    for order in range(n-1):
        hx = [H[0].coefficient(i,order) for i in range(m)]
        hy = [H[1].coefficient(i,order) for i in range(m)]
        hz = [H[2].coefficient(i,order) for i in range(m)]
        rows[0].append([(hx[i]+rows[1][order][i])/(order+1) for i in range(m)])
        rows[1].append([(hy[i]-rows[0][order][i])/(order+1) for i in range(m)])
        rows[2].append([hz[i]/(order+1) for i in range(m)])
    X = [TimeAngleJet(value, **kw) for value in rows]
    phases = [beta,gamma,br,gr,phase(0,1),phase(1,1),phase(0,2),phase(1,2),
              phase(0,3),phase(1,3),phase(2,1),phase(3,1),phase(2,2),phase(3,2)]
    result = frame_invariants(X,a,ar,*phases)
    # Check the independently formed first/second state derivatives against
    # normalized coefficients of D/M/W.  This is a finite algebra check,
    # not a substitute for the analytic remainder below.
    if n >= 3:
        for name in ('D','M','W'):
            for derivative in (1,2):
                for i in range(m):
                    lhs = math.factorial(derivative)*result[name].coefficient(i,derivative)
                    rhs = result[name+str(derivative)].coefficient(i,0)
                    if not (lhs-rhs).contains(0):
                        raise AssertionError('state recurrence and physical derivative formulas disagree')
    return result,error


def coarse_outer_invariants(model, theta_coefficients, outer_time_radius, state_radius):
    """True outer moduli without dividing by D or taking sqrt(-K)."""
    S, A = exact_arb(outer_time_radius), exact_arb(state_radius)
    if not S > model.outer or not A > 0:
        raise ValueError('strictly larger time circle and positive state circle required')
    old_cap, ctx.cap = ctx.cap, 4
    try:
        theta_fee = polynomial_bound(theta_coefficients, S, first=1)
        theta = complex_pad(theta_coefficients[0], theta_fee+A)
        radial_fee = (abs(model.root)*((abs(model.h)*S).exp()-1)).upper()
        radial = complex_pad(acb(model.center), radial_fee)
        budget = model.target.analytic_input_budget(radial, model.R0, model.sigma, model.RE)
        coefficient, radius = model.target.primitive(radial, 1)
        beta, gamma, _, height = model.target.scalars(radial, 1)
        phases = phase_evaluation([v[0] for v in beta], [v[0] for v in gamma],
            [v[1] for v in beta], [v[1] for v in gamma], theta)
        angular_width = (4*abs(theta.imag)).upper()
        if not angular_width < model.sigma:
            raise ValueError('larger-circle state image leaves the paid primitive Fourier strip')
        # Bound the TRUE Fourier coefficients of X directly.  FFT balls at a
        # wide complex-r box have nearly uniform high-mode uncertainty; after
        # e^(4 k Im(theta)) this is useless even though the true coefficients
        # decay exponentially.  If H=(a*T)_r, its kth coefficient is bounded
        # by H1*exp(-sigma*|k|).  In the cylindrical primitive the two horizontal
        # multipliers have total modulus 1/(4|k|-1), and the vertical multiplier
        # has modulus 1/(4|k|).  The k=0 terms are H_y, 0, Z_r.
        Xchoices = []
        for sigma_fraction in (Fraction(1,8), Fraction(4,25), Fraction(1,5), Fraction(8,25), Fraction(1,2)):
            sigma = exact_arb(sigma_fraction)
            if not sigma > angular_width:
                continue
            imaginary_phase, derivative_phase = arb(0), arb(0)
            for k in range(model.target.modes):
                sh, ch = (sigma*(k+1)).sinh(), (sigma*(k+1)).cosh()
                for phase in (beta, gamma):
                    imaginary_phase += abs(phase[k][0].real)*sh+abs(phase[k][0].imag)*ch
                    derivative_phase += abs(phase[k][1])*ch
            M_Xsrc = ((abs(radius[1])+abs(radius[0])*derivative_phase)*imaginary_phase.exp()).upper()
            decay = (-(sigma-angular_width)).exp()
            logarithmic_sum = -(1-decay).log()
            horizontal_nonzero = (2*M_Xsrc*logarithmic_sum/3).upper()
            candidate = [(M_Xsrc+horizontal_nonzero).upper(), horizontal_nonzero,
                         (abs(height[1])+M_Xsrc*logarithmic_sum/2).upper()]
            Xchoices.append((sigma_fraction, M_Xsrc, candidate))
        if not Xchoices:
            raise ValueError('no true Fourier coefficient circle encloses the state image')
        # Every candidate is independently a rigorous upper bound.  Selecting
        # any one by its displayed floating midpoint cannot invalidate it.
        Xbounds = [min((row[2][j] for row in Xchoices), key=lambda q:float(q)) for j in range(3)]
        X = [complex_pad(acb(0), value) for value in Xbounds]
        rows = frame_invariants(X, radius[0], radius[1], *phases)
        bounds = {key:abs(value).upper() for key, value in rows.items()}
        first = array_derivative(coefficient)
        Efinite = sum((vector_dot(first[k], first[(-k) % model.nodes]) for k in range(model.nodes)), series_constant(0))
        E = [complex_pad(Efinite[j], budget['E_error']/model.RE**j) for j in range(2)]
        analytic_K = bool(radius[0].abs_lower() > 0 and E[0].abs_lower() > 0)
        Kbound = None
        if analytic_K:
            K = (radius[1]*E[1]-4*radius[2]*E[0])/(2*radius[0]*E[0]**2)
            if not K.is_finite():
                analytic_K = False
            else:
                Kbound = abs(K).upper()
        info = dict(radial_displacement=radial_fee, theta_imaginary_upper=abs(theta.imag).upper(),
                    true_X_radial_component_modulus=Xbounds[0],
                    true_X_azimuthal_component_modulus=Xbounds[1],
                    true_X_vertical_component_modulus=Xbounds[2],
                    radius_modulus_lower=radius[0].abs_lower(), E_modulus_lower=E[0].abs_lower(),
                    E_infinite_error=budget['E_error'])
        info['true_X_selected_decay_strip'] = exact_arb(min(Xchoices,key=lambda q:float(sum(q[2])))[0])
        return bounds, Kbound, analytic_K, info
    finally:
        ctx.cap = old_cap


def time_disk_range(value, inner, outer, modulus):
    if not outer > inner > 0 or value.prec < 1:
        raise ValueError('invalid time Cauchy disk')
    ratio = inner/outer
    tail = (modulus*ratio**value.prec/(1-ratio)).upper()
    fee = sum((abs(value[j])*inner**j for j in range(1, value.prec)), arb(0))+tail
    return complex_pad(value[0], fee), tail


class TaylorOuterGate:
    def __init__(self, model, theta_coefficients, *, larger_time_radius=4,
                 state_cauchy_radius=Fraction(1, 50)):
        self.model = model
        self.theta = theta_coefficients
        self.S, self.A = exact_arb(larger_time_radius), exact_arb(state_cauchy_radius)
        self.jets, self.Xfee = true_time_invariants(model, theta_coefficients)
        self.moduli, self.Kmodulus, self.K_analytic, self.coarse = coarse_outer_invariants(
            model, theta_coefficients, larger_time_radius, state_cauchy_radius)
        self.ranges, self.tails, self.base_bounds = {}, {}, {}
        for key, value in self.jets.items():
            self.ranges[key], self.tails[key] = time_disk_range(value, model.outer, self.S, self.moduli[key])
            self.base_bounds[key] = abs(self.ranges[key]).upper()
        self.Krange = self.Ktail = None
        if self.K_analytic:
            self.Krange, self.Ktail = time_disk_range(model.K, model.outer, self.S, self.Kmodulus)

    def bound(self, state_tube):
        d = exact_arb(state_tube)
        if not 0 < d < self.A:
            raise ValueError('full state tube is not strictly inside the paid physical-angle circle')
        q = d/self.A
        values, fees = {}, {}
        for name in ('D', 'M', 'W'):
            zero, one, two = self.base_bounds[name], self.base_bounds[name+'1'], self.base_bounds[name+'2']
            tail0 = self.moduli[name]*q**3/(1-q)
            tail1 = self.moduli[name+'1']*q**2/(1-q)
            tail2 = self.moduli[name+'2']*q/(1-q)
            fees[name] = (d*one+d*d*two/2+tail0).upper()
            values[name] = (zero+fees[name]).upper()
            values[name+'1'] = (one+d*two+tail1).upper()
            values[name+'2'] = (two+tail2).upper()
        Dlower = (self.ranges['D'].abs_lower()-fees['D']).lower()
        if not Dlower > 0:
            raise ValueError('Taylor time/state estimate does not separate D from zero')
        if not self.K_analytic or not (-self.Krange).real > 0:
            raise ValueError('Taylor curvature is not on the negative-real branch on the inner disk')
        kappa = abs(self.Krange).sqrt().upper()
        N = [(values['M'+suffix]+kappa*values['W'+suffix]).upper() for suffix in ('', '1', '2')]
        tau = complex_pad(acb(self.model.tau0), abs(self.model.h)*self.model.outer)
        speed = abs(self.model.root*tau.cos()).upper()
        f = speed*N[0]/Dlower
        ft = speed*(N[1]/Dlower+N[0]*values['D1']/Dlower**2)
        ftt = speed*(N[2]/Dlower+(2*N[1]*values['D1']+N[0]*values['D2'])/Dlower**2
                     +2*N[0]*values['D1']**2/Dlower**3)
        return dict(f=f.upper(), f_theta=ft.upper(), f_theta2=ftt.upper(),
                    D_modulus_lower=Dlower, minus_K_real_lower=(-self.Krange).real.lower(),
                    physical_state_tube=d, time_D_tail=self.tails['D'], state_D_variation=fees['D'],
                    K_time_tail=self.Ktail, kappa_modulus_upper=kappa,
                    D_base_disk_modulus_lower=self.ranges['D'].abs_lower())

    def record(self):
        return dict(larger_time_radius=ball_record(self.S), state_cauchy_radius=ball_record(self.A),
            coarse_outer_moduli={key:ball_record(value) for key, value in self.moduli.items()},
            coarse_outer_geometry={key:ball_record(value) for key, value in self.coarse.items()},
            coarse_K_analytic=self.K_analytic,
            coarse_K_modulus=None if self.Kmodulus is None else ball_record(self.Kmodulus),
            correlated_time_ranges={key:record_complex(value) for key, value in self.ranges.items()},
            complete_time_tails={key:ball_record(value) for key, value in self.tails.items()},
            correlated_K_range=None if self.Krange is None else record_complex(self.Krange),
            K_time_tail=None if self.Ktail is None else ball_record(self.Ktail),
            initial_X_infinite_time_error=ball_record(self.Xfee))


def rectangular_disk_range(value, R, S, d, A, modulus):
    """Whole bidisk from a true Taylor rectangle and two Cauchy complements.

    First truncate in state s at n.  On |u|<=R its remainder is paid directly
    by modulus*(d/A)^n/(1-d/A).  Each retained state coefficient has modulus
    <=modulus/A^j on |u|<=S; its complete time tail is then summed for j<n.
    This splitting avoids treating the unknown time/state corner twice.
    """
    if not S > R > 0 or not A > d > 0:
        raise ValueError('strictly nested time/state disks are required')
    qt, qs = R/S, d/A
    time_tail = modulus*qt**value.m/(1-qt)*(1-qs**value.n)/(1-qs)
    state_tail = modulus*qs**value.n/(1-qs)
    fee = sum((abs(value.coefficient(i,j))*R**i*d**j
               for j in range(value.n) for i in range(value.m) if i or j), arb(0))
    return complex_pad(value.coefficient(0,0),fee+time_tail+state_tail),time_tail.upper(),state_tail.upper()


class StateTaylorOuterGate:
    """High-order physical-state refinement of the same outer-domain proof."""
    def __init__(self, model, theta_coefficients, *, larger_time_radius=4,
                 state_cauchy_radius=Fraction(1,50), state_precision=21):
        self.model,self.theta=model,theta_coefficients
        self.S,self.A=exact_arb(larger_time_radius),exact_arb(state_cauchy_radius)
        self.state_precision=int(state_precision)
        self.jets,self.Xfee=physical_state_invariants(model,theta_coefficients,self.state_precision)
        self.moduli,self.Kmodulus,self.K_analytic,self.coarse=coarse_outer_invariants(
            model,theta_coefficients,larger_time_radius,state_cauchy_radius)
        self.Krange=self.Ktail=None
        if self.K_analytic:
            self.Krange,self.Ktail=time_disk_range(model.K,model.outer,self.S,self.Kmodulus)

    def bound(self,state_tube):
        d=exact_arb(state_tube)
        if not 0<d<self.A:
            raise ValueError('full state tube is not strictly inside the paid physical-angle circle')
        ranges,timetails,statetails={}, {}, {}
        for name,value in self.jets.items():
            ranges[name],timetails[name],statetails[name]=rectangular_disk_range(
                value,self.model.outer,self.S,d,self.A,self.moduli[name])
        Dlower=ranges['D'].abs_lower()
        if not Dlower>0:
            raise ValueError('rectangular time/state Taylor estimate does not separate D from zero')
        if not self.K_analytic or not (-self.Krange).real>0:
            raise ValueError('Taylor curvature is not on the negative-real branch on the inner disk')
        values={name:abs(value).upper() for name,value in ranges.items()}
        kappa=abs(self.Krange).sqrt().upper()
        N=[(values['M'+s]+kappa*values['W'+s]).upper() for s in ('','1','2')]
        tau=complex_pad(acb(self.model.tau0),abs(self.model.h)*self.model.outer)
        speed=abs(self.model.root*tau.cos()).upper()
        f=speed*N[0]/Dlower
        ft=speed*(N[1]/Dlower+N[0]*values['D1']/Dlower**2)
        ftt=speed*(N[2]/Dlower+(2*N[1]*values['D1']+N[0]*values['D2'])/Dlower**2
                   +2*N[0]*values['D1']**2/Dlower**3)
        return dict(f=f.upper(),f_theta=ft.upper(),f_theta2=ftt.upper(),D_modulus_lower=Dlower,
                    minus_K_real_lower=(-self.Krange).real.lower(),physical_state_tube=d,
                    time_D_tail=timetails['D'],state_D_tail=statetails['D'],K_time_tail=self.Ktail,
                    kappa_modulus_upper=kappa)

    def record(self):
        return dict(larger_time_radius=ball_record(self.S),state_cauchy_radius=ball_record(self.A),
            state_precision=self.state_precision,
            coarse_outer_moduli={key:ball_record(value) for key,value in self.moduli.items()},
            coarse_outer_geometry={key:ball_record(value) for key,value in self.coarse.items()},
            coarse_K_analytic=self.K_analytic,
            coarse_K_modulus=None if self.Kmodulus is None else ball_record(self.Kmodulus),
            correlated_K_range=None if self.Krange is None else record_complex(self.Krange),
            K_time_tail=None if self.Ktail is None else ball_record(self.Ktail),
            initial_X_infinite_time_error=ball_record(self.Xfee),
            D_time_coefficients_at_state_center=[record_complex(self.jets['D'].coefficient(i,0))
                                                for i in range(self.model.precision)],
            state_recurrence_derivative_check=True)


def reference_fourier_power(real, imag, left, right):
    center, half = (left+right)/2, (right-left)/2
    matrix = []
    for j in range(8):
        matrix.append([exact_arb(sum((Fraction(math.comb(7,j)*math.comb(7-j,r-j)*(-1)**(r-j)*math.comb(r,i))
                                      *center**(r-i)*half**i for r in range(max(i,j),8)), Fraction(0)))
                       for i in range(8)])
    K = real.shape[-1]-1
    data = [[acb(0) for _ in range(K+1)] for _ in range(8)]
    for i in range(8):
        for k in range(K+1):
            data[i][k] = sum((acb(arb(float(real[j,0,k])),arb(float(imag[j,0,k])))*matrix[j][i]
                              for j in range(8)),acb(0))
    return data


def outer_angle_variation(data, label, halfwidth, angle_radius, time_radius):
    width = abs(exact_arb(halfwidth))*exact_arb(angle_radius)
    result = width/4
    for k in range(1, len(data[0])):
        norm = sum((abs(data[i][k])*time_radius**i for i in range(8)), arb(0))
        result += 2*norm*(k*abs(label.imag)).cosh()*((k*width).exp()-1)
    return result.upper()


def exact_upper_fraction(value):
    return Fraction(str(value.upper().fmpq()))


def point_residual(model, theta, L, domain):
    (f, ft, _, _), _ = model.time_field(theta)
    first = polynomial([(j+1)*theta[j+1]/model.h for j in range(len(theta)-1)],model.precision)-f
    second = polynomial([(j+1)*L[j+1]/model.h for j in range(len(L)-1)],model.precision)-ft
    tails = [domain[key]*model.outer**(-model.precision)/(1-1/model.outer) for key in ('f','f_theta')]
    return dict(e0_bound=(sum((abs(first[j]) for j in range(model.precision)),arb(0))+tails[0]).upper(),
                e1_bound=(sum((abs(second[j]) for j in range(model.precision)),arb(0))+tails[1]).upper(),
                e0_time_tail=tails[0].upper(),e1_time_tail=tails[1].upper())


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest',type=Path,required=True)
    parser.add_argument('--object',type=Path,required=True)
    parser.add_argument('--root-certificate',type=Path,required=True)
    parser.add_argument('--segment',type=int,default=419)
    parser.add_argument('--sub-left',default='0');parser.add_argument('--sub-right',default='1')
    parser.add_argument('--label-real',default='1/2');parser.add_argument('--label-imag',default='1/512')
    parser.add_argument('--angle-halfwidths',default='1/4096,1/1024,1/256,1/64')
    parser.add_argument('--angle-outer-radius',default='4')
    parser.add_argument('--time-outer-radius',default='3')
    parser.add_argument('--larger-time-radius',default='4')
    parser.add_argument('--state-cauchy-radius',default='1/50')
    parser.add_argument('--state-tube',default='1/65536')
    parser.add_argument('--time-order',type=int,default=40)
    parser.add_argument('--state-order',type=int,default=20,
                        help='nonnegative physical-state order; zero keeps the older second-derivative gate')
    parser.add_argument('--quarter-nodes',type=int,default=512)
    parser.add_argument('--bits',type=int,default=160)
    parser.add_argument('--max-germs',type=int,default=16)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();started=time.monotonic();ctx.prec=args.bits;ctx.cap=max(21,args.time_order+4)
    manifest,shard,shard_path,real,imag,a,b=load_segment(args.manifest,args.segment)
    ident=manifest['trace_identity']
    if ident['angular_scale']!=4 or ident['sign'] not in (-1,1):raise ValueError('wrong state convention')
    if sha(args.object)!=ident['source_sha256'] or sha(args.root_certificate)!=ident['root_certificate_sha256']:
        raise ValueError('reference/object/root identity mismatch')
    left,right=Fraction(args.sub_left),Fraction(args.sub_right)
    if not 0<=left<right<=1:raise ValueError('invalid time subspan')
    ta,tb=a+(b-a)*left,a+(b-a)*right;center,half=(ta+tb)/2,(tb-ta)/2
    root=prepare_refined_root(args.object,args.root_certificate,nodes=args.quarter_nodes)
    target=AffineBulkTarget(args.object,args.quarter_nodes,args.quarter_nodes,exact_arb(Fraction(3,1000)),
                            exact_arb(Fraction(1,400)),exact_arb(Fraction(8,25)))
    radial,cover,cells,crossed=radial_cover(target,root.root,center,half)
    if len(cells)>args.max_germs:raise ValueError('germ budget exceeded; none may be omitted')
    label=acb(exact_arb(Fraction(args.label_real)),exact_arb(Fraction(args.label_imag)))
    theta,L=reference_time_coefficients(real,imag,label,left,right)
    data=reference_fourier_power(real,imag,left,right)
    widths=[Fraction(q) for q in args.angle_halfwidths.split(',')]
    if any(q<=0 for q in widths) or not Fraction(args.angle_outer_radius)>1:
        raise ValueError('positive angular halfwidths and outer radius greater than one required')
    R=exact_arb(Fraction(args.time_outer_radius));state=exact_arb(Fraction(args.state_tube))
    variations={str(width):outer_angle_variation(data,label,width,Fraction(args.angle_outer_radius),R)
                for width in widths}
    report=dict(kind='correlated_time_Taylor_outer_domains_on_complete_common_germ_union',complete=False,
        source_sha256=sha(__file__),object_sha256=sha(args.object),root_certificate_sha256=sha(args.root_certificate),
        exact_delta_fraction=str(root.exact_delta),root_refinement=root.provenance,
        reference_manifest=str(args.manifest),reference_manifest_sha256=sha(args.manifest),
        reference_shard_sha256=sha(shard_path),segment=args.segment,
        exact_time_endpoints=list(map(str,(ta,tb))),normalized_time_subspan=list(map(str,(left,right))),
        label_center=dict(real=args.label_real,imag=args.label_imag),angle_outer_radius=args.angle_outer_radius,
        time_outer_radius=args.time_outer_radius,larger_time_radius=args.larger_time_radius,
        state_cauchy_radius=args.state_cauchy_radius,state_tube=args.state_tube,
        time_order=args.time_order,state_order=args.state_order,bits=args.bits,nodes=args.quarter_nodes,
        dependency_sha256={name:sha(Path(__file__).parent/name) for name in
            ('fourfold_phase_field_time_taylor.py','fourfold_phase_field_time_germ_union.py',
             'fourfold_phase_field_time_refined_root.py','fourfold_time_angle_jets.py')},
        required_common_spans=[list(map(str,cell)) for cell in cells],
        exact_radial_enclosure=list(map(str,cover)),guaranteed_crossed_knots=list(map(str,crossed)),
        reference_outer_angle_variations={key:ball_record(value) for key,value in variations.items()},
        accepted_germs=[],failed_germs=[],
        limitations=['Outer-domain success certifies the true germ extensions, not a complete angle residual',
                     'Base-label residuals use a germ union; off-span extensions can overestimate true errors',
                     'Failed gates are failures of the stated bounds, not proofs of a genuine pole',
                     'No complete branch/initial-circle/Wiener certificate is asserted'])
    args.out.parent.mkdir(parents=True,exist_ok=True)
    def save():
        report['elapsed_seconds']=time.monotonic()-started
        args.out.write_text(json.dumps(report,indent=2)+'\n')
    save()
    for index,cell in enumerate(cells):
        try:
            model=RefinedGermTimeModel(args.object,args.root_certificate,center,half,
                refined_root=root,cell=cell,nodes=args.quarter_nodes,order=args.time_order,
                outer_radius=Fraction(args.time_outer_radius),branch_sign=int(ident['sign']))
            if args.state_order<0:
                raise ValueError('state order must be nonnegative')
            if args.state_order:
                gate=StateTaylorOuterGate(model,theta,larger_time_radius=Fraction(args.larger_time_radius),
                    state_cauchy_radius=Fraction(args.state_cauchy_radius),state_precision=args.state_order+1)
            else:
                gate=TaylorOuterGate(model,theta,larger_time_radius=Fraction(args.larger_time_radius),
                                     state_cauchy_radius=Fraction(args.state_cauchy_radius))
            row=dict(index=index,common_span=list(map(str,cell)),gate=gate.record(),arcs={})
            for width in widths:
                d=variations[str(width)]+state
                try:
                    domain=gate.bound(exact_upper_fraction(d))
                    row['arcs'][str(width)]=dict(proved=True,domain={key:ball_record(value) for key,value in domain.items()})
                except Exception as exc:
                    row['arcs'][str(width)]=dict(proved=False,reason=str(exc),required_state_tube=ball_record(d))
            try:
                point_domain=gate.bound(Fraction(args.state_tube))
                row['base_label_point_residual']={key:ball_record(value) for key,value in point_residual(model,theta,L,point_domain).items()}
            except Exception as exc:
                row['base_label_point_residual_failure']=str(exc)
            report['accepted_germs'].append(row)
            print(json.dumps(dict(stage='outer Taylor gate',germ=index,
                                  arcs={key:value['proved'] for key,value in row['arcs'].items()},
                                  point=row.get('base_label_point_residual',{}))),flush=True)
        except Exception as exc:
            report['failed_germs'].append(dict(index=index,common_span=list(map(str,cell)),reason=str(exc)))
            print(json.dumps(dict(stage='failed germ',germ=index,reason=str(exc))),flush=True)
        save()
    report['complete']=not report['failed_germs'] and len(report['accepted_germs'])==len(cells)
    report['complete_arc_domain_proofs']={str(width):report['complete'] and
        all(row['arcs'][str(width)]['proved'] for row in report['accepted_germs']) for width in widths}
    save()
    print(json.dumps(dict(complete=report['complete'],arc_domains=report['complete_arc_domain_proofs'],
                          elapsed_seconds=report['elapsed_seconds']),indent=2),flush=True)


if __name__=='__main__':main()
