#!/usr/bin/env python3
"""Continuous R125 primitive bounds for an actual shared native GC field.

All finite Fourier coefficients are combined before bounds. Exact scalar
profile packets and the exact chart Fourier error are consumed. A radial
polynomial auxiliary P uses a finite geometric expansion of 1/q about a
common angular denominator for each original native cell. Its primitive
has one common cell mean even across internal phase branches. Every
truncation and every reciprocal/exponential remainder is paid.

The physical X is the fixed-material ODE definition using the separately
calibrated exact clock packet, not a relabeling of old floating body data.
No BVP, frame ODE, or tail solve is performed here.
"""
from __future__ import annotations
import argparse
import bisect
from fractions import Fraction as Q
import gzip
import hashlib
import json
import math
from pathlib import Path
import time
import numpy as np

from fd2d_gc_native_log_field import NativeLogField, identity, locate_near, log_codazzi_numerators
import fd2d_gc_interval_models as M

I, P, TM, qb = M.I, M.P, M.TM, M.qb
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def load_json(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if Path(path).suffix == '.gz' else raw)


def zero(phase):
    return TM.zero(phase).p


def ipow(value, exponent):
    out = I(1.)
    for _ in range(exponent):
        out = out*value
    return out


def psum(values, phase):
    out = zero(phase)
    for value in values:
        out = out+value
    return out


def maximum_abs(value):
    return float(np.max(value.abs().hi))


def vector_bound(a, b, c=None):
    value = a.square()+b.square()
    if c is not None:
        value = value+c.square()
    return float(np.max(value.sqrt().hi))


def pack_real(cosine, sine):
    degree, count = cosine.lo.shape
    K = count-1
    lo = np.zeros((degree, 2*K+1)); hi = lo.copy()
    lo[:, K], hi[:, K] = cosine.lo[:, 0], cosine.hi[:, 0]
    if K:
        half = cosine[:, 1:]/2
        lo[:, K+1:], hi[:, K+1:] = half.lo, half.hi
        lo[:, :K], hi[:, :K] = half.lo[:, ::-1], half.hi[:, ::-1]
    even = P(I(lo, hi), -K, 0)
    lo = np.zeros_like(lo); hi = lo.copy()
    if K:
        half = sine[:, 1:]/2
        lo[:, :K], hi[:, :K] = half.lo[:, ::-1], half.hi[:, ::-1]
        lo[:, K+1:], hi[:, K+1:] = -half.hi, -half.lo
    return even, P(I(lo, hi), -K, 1)


def exact_matrix(rows):
    lo = np.empty((len(rows), len(rows[0]))); hi = lo.copy()
    for j, row in enumerate(rows):
        for k, value in enumerate(row):
            v = qb(value)
            lo[j, k], hi[j, k] = v.lo, v.hi
    return I(lo, hi)


class ActualNative:
    def __init__(self, path):
        self.field = NativeLogField(path)
        self.mesh = [Q(float(v)) for v in self.field.nodes]
        self.cache = {}

    def power(self, cell):
        if cell in self.cache:
            return self.cache[cell]
        f = self.field; h = self.mesh[cell+1]-self.mesh[cell]
        rows = [[] for _ in range(4)]
        for j in range(f.dimension):
            a, b = Q(float(f.values[cell, j])), Q(float(f.values[cell+1, j]))
            c, d = Q(float(f.first_s[cell, j])), Q(float(f.first_s[cell+1, j]))
            values = (a, h*c, 3*(b-a)-h*(2*c+d), 2*(a-b)+h*(c+d))
            for k, value in enumerate(values):
                rows[k].append(value)
        self.cache = {cell: rows}
        return rows

    def models(self, cell, left, right):
        h = self.mesh[cell+1]-self.mesh[cell]
        a, b = ((left+right)/2-self.mesh[cell])/h, (right-left)/(2*h)
        rows = self.power(cell)
        transformed = []
        for derivative in range(2):
            degree = 3-derivative
            source = [[Q(math.factorial(j)//math.factorial(j-derivative))*v/h**derivative
                       for v in rows[j]] for j in range(derivative, 4)]
            coeff = [[sum((Q(math.comb(j, k))*a**(j-k)*b**k*source[j][m]
                           for j in range(k, degree+1)), Q())
                      for m in range(self.field.dimension)] for k in range(degree+1)]
            array = exact_matrix(coeff); count = self.field.K+1
            blank = I(np.zeros((degree+1, count)))
            cosine = array[:, :count]
            sine = I(np.concatenate((np.zeros((degree+1, 1)), array.lo[:, count:]), axis=1),
                     np.concatenate((np.zeros((degree+1, 1)), array.hi[:, count:]), axis=1))
            transformed.append((TM(pack_real(cosine, blank)[0]), TM(pack_real(blank, sine)[1])))
        eta, zeta = transformed[0]
        eta_x, zeta_x = transformed[1]
        return dict(eta=eta, zeta=zeta, eta_x=eta_x, zeta_x=zeta_x,
                    eta_xi=TM(M.angular_derivative(eta.p)), zeta_xi=TM(M.angular_derivative(zeta.p)))


class ExactProfile:
    def __init__(self, path, native_path):
        self.path = Path(path); self.packet = load_json(path)
        if self.packet['schema'] != 'fd2d-exact-physical-profile-calibrated-clock-v1':
            raise ValueError('Wrong accurate physical profile packet')
        if self.packet['native_field']['sha256'] != identity(native_path)['sha256']:
            raise ValueError('Accurate clock was not defined for this actual native field')
        for name, row in (('native', self.packet['native_field']), ('moments', self.packet['exact_moments']),
                          ('target', self.packet['target_input'])):
            locate_near(path, row)
        self.pieces = self.packet['pieces']
        self.breaks = [Q(self.pieces[0]['x_left_exact'])]+[Q(p['x_right_exact']) for p in self.pieces]
        self.cache = {}

    def index(self, left, right):
        j = min(bisect.bisect_right(self.breaks, left)-1, len(self.pieces)-1)
        if j < 0 or right > self.breaks[j+1]:
            raise ValueError('Native cell crosses an accurate physical piece boundary')
        return j

    def parts(self, left, right):
        j = self.index(left, right); p = self.pieces[j]
        if p['kind'] == 'hermite':
            return [(left, right, j, None)]
        cuts = {left, right}
        for branch in p['branches']:
            for row in branch['branch_x_cuts']:
                for key in ('x_lower_exact', 'x_upper_exact'):
                    q = Q(row[key])
                    if left < q < right:
                        cuts.add(q)
        cuts = sorted(cuts); result = []
        for lo, hi in zip(cuts[:-1], cuts[1:]):
            branch_id = 'root_bracket'
            for k, branch in enumerate(p['branches']):
                lower = Q(branch['branch_x_cuts'][0]['x_upper_exact'])
                upper = Q(branch['branch_x_cuts'][1]['x_lower_exact'])
                if lo >= lower and hi <= upper:
                    branch_id = k
                    break
            result.append((lo, hi, j, branch_id))
        return result

    def models(self, index, branch_index, left, right):
        p = self.pieces[index]
        x0, h = Q(p['x_left_exact']), Q(p['x_width_exact'])
        L = M.record_interval(p['physical_length'])
        t = M.variable(((left+right)/2-x0)/h, (right-left)/(2*h))
        W = t**3*(10+t*(-15+6*t))
        local_s = t*qb(h)+(TM.scalar(L)-qb(h))*W
        J = 1+(TM.scalar(L)/qb(h)-1)*30*t*t*(1-t)*(1-t)
        tau = local_s/L
        if p['kind'] == 'hermite':
            c = [M.record_interval(v) for v in p['radius_polynomial_in_physical_tau']]
            a = M.polynomial_model(c, tau)
            ap = M.polynomial_model([j*c[j] for j in range(1, len(c))], tau)/L
            app = M.polynomial_model([j*(j-1)*c[j] for j in range(2, len(c))], tau)/(L*L)
        else:
            branch = p['branches'][branch_index]
            lo, hi = map(Q, branch['physical_tau_interval_exact'])
            y = (2*tau-qb(lo+hi))/qb(hi-lo)
            def read(name):
                return [M.record_interval(v) for v in branch[name]]
            a = M.polynomial_model(read('radius_polynomial_in_y'), y)
            a.error = M.error_sum(a.error, float(qb(Q(branch['radius_uniform_remainder_upper_exact'])).hi))
            ap = M.polynomial_model(read('sine_polynomial_in_y'), y)
            cosine = M.polynomial_model(read('cosine_polynomial_in_y'), y)
            rem = float(qb(Q(branch['sine_cosine_uniform_remainder_upper_exact'])).hi)
            ap.error = M.error_sum(ap.error, rem); cosine.error = M.error_sum(cosine.error, rem)
            phase = read('phase_polynomial_in_y')
            phase_s = M.polynomial_model([j*phase[j] for j in range(1, len(phase))], y)*qb(2/(hi-lo))/L
            app = cosine*phase_s
        return dict(a=a, ap=ap, app=app, J=J)


class ExactChart:
    def __init__(self, path, modes, native):
        self.path = Path(path); self.packet = load_json(path)
        if self.packet['schema'] != 'fd2d-exact-balanced-material-chart-C4-Fourier-tail-v1':
            raise ValueError('Wrong accurate chart Fourier remainder package')
        means_path = locate_near(path, self.packet['means']); means = load_json(means_path)
        if self.packet['moments']['sha256'] != native.meta['initial_geometry']['exact_moments']['sha256']:
            raise ValueError('Angular chart and initial geometry use different exact seed moments')
        self.means_path = means_path
        mu = [M.exact_midpoint(row['material_weighted_mean']) for row in means['rows']]
        if not 1 <= modes <= len(mu):
            raise ValueError('Invalid finite chart approximation order')
        self.modes = modes
        d = [Q()]+[2*v for v in mu[:modes]]
        V = [Q()]+[v/Q(j) for j, v in enumerate(mu[:modes], 1)]
        cosine = exact_matrix([d]); sine = exact_matrix([V]); blank = I(np.zeros_like(cosine.lo))
        self.d = pack_real(cosine, blank)[0]
        self.V = pack_real(blank, sine)[1]
        self.d_xi = M.angular_derivative(self.d)
        errors = {r['derivative_order']:M.bound_upper(r['total_uniform_error']) for r in self.packet['rows']}
        self.d_error = M.error_sum(errors[1], float(qb(2*sum(map(abs, mu[modes:]), Q())).hi))
        self.V_error = M.error_sum(errors[0], float(qb(sum((abs(v)/Q(j) for j, v in enumerate(mu[modes:], modes+1)), Q())).hi))
        self.left, self.right = map(lambda v:Q(float(v)), native.meta['angular_chart']['blend_interval'])

    def blend_value(self, x):
        if x <= self.left:
            return Q(1)
        if x >= self.right:
            return Q()
        t = (x-self.left)/(self.right-self.left)
        return 1-t**3*(10-15*t+6*t*t)

    def blend_models(self, left, right):
        if right <= self.left:
            return TM.scalar(1.), TM.scalar(0.)
        if left >= self.right:
            return TM.scalar(0.), TM.scalar(0.)
        if left < self.left or right > self.right:
            raise ValueError('Split at the exact binary angular blend boundaries')
        h = self.right-self.left
        t = M.variable(((left+right)/2-self.left)/h, (right-left)/(2*h))
        b = 1-t**3*(10+t*(-15+6*t))
        first = -30*t*t*(1-t)*(1-t)/qb(h)
        return b, first


def auxiliary_models(native, scalars, b, bx, chart, b0, order, exp_order):
    eta, zeta = native['eta'], native['zeta']
    a, ap, app, J = (scalars[k] for k in ('a', 'ap', 'app', 'J'))
    q = 1+b*TM(chart.d, chart.d_error)
    Ux = bx*TM(chart.V, chart.V_error)
    eplus = M.exp_model(eta, order=exp_order)
    eminus = M.exp_model(-eta, order=exp_order)
    minus2 = M.exp_model(-2*eta, order=exp_order, minus_one=True)
    values = log_codazzi_numerators(a, ap, app, J, q, Ux, eta, zeta,
        native['eta_x'], native['zeta_x'], native['eta_xi'], native['zeta_xi'],
        eminus, 1+minus2, minus2)
    v2 = 1-ap*ap
    reciprocal = M.inverse_power_model(a)*M.inverse_power_model(v2, square_root=True)
    N = [-eplus*values['Pn']*reciprocal, values['Pm']*reciprocal]
    delta = b-qb(b0)
    power = TM.scalar(1.)
    auxiliaries = [[] for _ in range(2)]
    for j in range(order+1):
        for axis in range(2):
            auxiliaries[axis].append(TM(N[axis].p)*power)
        power = power*delta
    return dict(N=N, auxiliary=auxiliaries, native=native, scalar=scalars,
                b=b, bx=bx, delta=delta, eplus=eplus)


def cell_angles(chart, b0, order, trig):
    d = M.range_polynomial(chart.d, trig)
    dp = M.range_polynomial(chart.d_xi, trig)
    V = M.range_polynomial(chart.V, trig)+I(-chart.V_error, chart.V_error)
    qmid = 1+qb(b0)*d
    if np.any(qmid.lo <= 0):
        raise ArithmeticError('Common angular denominator is not proved positive')
    C, Cp = [], []
    for j in range(order+1):
        C.append(ipow(-d, j)/ipow(qmid, j+1))
        derivative = -(j+1)*ipow(-d, j)*qb(b0)*dp/ipow(qmid, j+2)
        if j:
            derivative = derivative-j*ipow(-d, j-1)*dp/ipow(qmid, j+1)
        Cp.append(derivative)
    return dict(d=d, d_xi=dp, V=V, qmid=qmid, C=C, Cp=Cp)


def scalar_ranges(context):
    s = {key:M.range_model(value) for key, value in context['scalar'].items()}
    if s['a'].lo <= 0 or s['J'].lo <= 0:
        raise ArithmeticError('Physical profile/clock lost positivity in a restricted model')
    s['v2'] = 1-s['ap'].square()
    if s['v2'].lo <= 0:
        raise ArithmeticError('Physical radial speed needs a smaller continuous box')
    return s


def nonthin_enclosure(context, angles, chart, order, trig):
    s = scalar_ranges(context)
    b = M.range_model(context['b']); bx = M.range_model(context['bx'])
    delta = M.range_polynomial(context['delta'].p)
    qapprox = angles['qmid']+delta*angles['d']
    qerr = (I(chart.d_error)*b.abs()+I(context['b'].error)*angles['d'].abs()).hi
    qtrue = qapprox+I(-qerr, qerr)
    if np.any(qapprox.lo <= 0) or np.any(qtrue.lo <= 0):
        raise ArithmeticError('Moving angular chart needs a smaller continuous radial box')
    quotient = (delta*angles['d']/angles['qmid']).abs()
    remainder, H = [], []
    for axis in range(2):
        N = context['N'][axis]
        Nbound = M.range_polynomial(N.p, trig).abs()
        error = I(N.error)/I(qtrue.lo)
        error = error+Nbound*I(qerr)/(I(qtrue.lo)*I(qapprox.lo))
        error = error+Nbound*ipow(quotient, order+1)/I(qapprox.lo)
        for j, model in enumerate(context['auxiliary'][axis]):
            error = error+I(model.error)*angles['C'][j].abs()
        remainder.append(error.hi)
        H.append((Nbound+I(N.error))/I(qtrue.lo))
    zeta = M.range_model(context['native']['zeta'], trig)
    eplus = M.range_model(context['eplus'], trig)
    if np.any(eplus.lo <= 0):
        raise ArithmeticError('Native exponential enclosure lost positivity')
    v = s['v2'].sqrt()
    alpha_x = s['J']*v*zeta/s['a']
    alpha_y = -s['J']*(s['v2']*zeta.square()-s['a']*s['app'])/(s['a']*v*eplus)
    w = bx*angles['V']/qtrue
    return dict(scalar=s, remainder=remainder, H=H, alpha=(alpha_x, alpha_y), w=w,
                angular_q_lower=float(np.min(qtrue.lo)), geometric_ratio_upper=maximum_abs(quotient))


def thin_enclosure(profile, index, native, b, bx, chart, angles, exp_order, trig):
    """No auxiliary approximation in the tiny uncertain analytic-cut bracket."""
    packet = profile.pieces[index]
    s = {key:M.record_interval(packet['physical_jet_bounds'][source])
         for key, source in (('a', 'a'), ('ap', 'a_s'), ('app', 'a_ss'))}
    s['J'] = M.record_interval(packet['J_range']); s['v2'] = 1-s['ap'].square()
    bval, bxval = M.range_model(b), M.range_model(bx)
    q = 1+bval*(angles['d']+I(-chart.d_error, chart.d_error))
    Ux = bxval*angles['V']; w = Ux/q
    v = s['v2'].sqrt()
    values = {name:M.range_model(value, trig) for name, value in native.items()}
    eplus = M.range_model(M.exp_model(native['eta'], order=exp_order), trig)
    eminus = M.range_model(M.exp_model(-native['eta'], order=exp_order), trig)
    minus2 = M.range_model(M.exp_model(-2*native['eta'], order=exp_order, minus_one=True), trig)
    numerator = log_codazzi_numerators(s['a'], s['ap'], s['app'], s['J'], q, Ux,
        values['eta'], values['zeta'], values['eta_x'], values['zeta_x'],
        values['eta_xi'], values['zeta_xi'], eminus, 1+minus2, minus2)
    H = [(-eplus*numerator['Pn']/(s['a']*q*v)).abs(),
         (numerator['Pm']/(s['a']*q*v)).abs()]
    alpha_x = s['J']*v*values['zeta']/s['a']
    alpha_y = -s['J']*(s['v2']*values['zeta'].square()-s['a']*s['app'])/(s['a']*v*eplus)
    return dict(scalar=s, remainder=[v.hi for v in H], H=H, alpha=(alpha_x, alpha_y), w=w,
                angular_q_lower=float(np.min(q.lo)), geometric_ratio_upper=None)


def consume_cell(index, actual, profile, chart, order, exp_order, trig):
    left, right = actual.mesh[index:index+2]
    b0 = chart.blend_value((left+right)/2)
    angles = cell_angles(chart, b0, order, trig)
    parts = []
    def prepare(lo, hi, piece, branch, depth=0):
        native = actual.models(index, lo, hi)
        b, bx = chart.blend_models(lo, hi)
        if branch == 'root_bracket':
            enclosure = thin_enclosure(profile, piece, native, b, bx, chart, angles, exp_order, trig)
            parts.append(dict(left=lo, right=hi, piece=piece, branch=branch,
                              context=None, enclosure=enclosure,
                              auxiliary=[[zero(axis) for _ in range(order+1)] for axis in range(2)]))
            return
        try:
            scalars = profile.models(piece, branch, lo, hi)
            context = auxiliary_models(native, scalars, b, bx, chart, b0, order, exp_order)
            enclosure = nonthin_enclosure(context, angles, chart, order, trig)
        except ArithmeticError:
            if depth >= 12:
                raise
            mid = (lo+hi)/2
            prepare(lo, mid, piece, branch, depth+1)
            prepare(mid, hi, piece, branch, depth+1)
            return
        parts.append(dict(left=lo, right=hi, piece=piece, branch=branch,
                          context=context, enclosure=enclosure,
                          auxiliary=[[v.p for v in axis] for axis in context['auxiliary']]))
    for part in profile.parts(left, right):
        prepare(*part)
    total = [[zero(axis) for _ in range(order+1)] for axis in range(2)]
    for part in parts:
        h = part['right']-part['left']
        for axis in range(2):
            for j in range(order+1):
                total[axis][j] = total[axis][j]+M.integrate_polynomial(part['auxiliary'][axis][j], h)
    means = [[value*qb(1/(right-left)) for value in axis] for axis in total]
    mean_values = []
    for axis in range(2):
        value = I(np.zeros(trig[0].lo.shape[1]))
        for j in range(order+1):
            value = value+M.range_polynomial(means[axis][j], trig)*angles['C'][j]
        mean_values.append(value)
    before = [[zero(axis) for _ in range(order+1)] for axis in range(2)]
    result = []
    for part in parts:
        h = part['right']-part['left']; enclosure = part['enclosure']
        Q_values, Q_first = [], []
        for axis in range(2):
            value = I(np.zeros(trig[0].lo.shape[1])); first = I(np.zeros_like(value.lo))
            for j in range(order+1):
                primitive = M.primitive_polynomial(part['auxiliary'][axis][j], h, before[axis][j],
                    means[axis][j], part['left']-left)
                v = M.range_polynomial(primitive, trig)
                dv = M.range_polynomial(M.angular_derivative(primitive), trig)
                value = value+v*angles['C'][j]
                first = first+dv*angles['C'][j]+v*angles['Cp'][j]
                before[axis][j] = before[axis][j]+M.integrate_polynomial(part['auxiliary'][axis][j], h)
            Q_values.append(value); Q_first.append(first)
        errors = []
        for axis in range(2):
            radius = enclosure['remainder'][axis]
            errors.append(mean_values[axis]+I(-radius, radius)+enclosure['w']*Q_first[axis])
        commutator = Q_values[0]*enclosure['alpha'][1]-Q_values[1]*enclosure['alpha'][0]
        bbound = vector_bound(errors[0], errors[1], commutator)
        pbound = maximum_abs(Q_values[1])
        qbound = vector_bound(Q_values[0], Q_values[1])
        abs_H = vector_bound(enclosure['H'][0], enclosure['H'][1])
        result.append(dict(left_exact=str(part['left']), right_exact=str(part['right']),
            profile_piece=part['piece'], phase_branch=part['branch'],
            complete_radial_and_angular_coverage=True, all_actual_angular_modes_or_remainders_paid=True,
            mean_vector_upper=vector_bound(mean_values[0], mean_values[1]),
            primitive_Q_upper=qbound, primitive_Qe1_upper=pbound,
            primitive_Qxi_upper=vector_bound(Q_first[0], Q_first[1]),
            true_H_minus_auxiliary_upper=vector_bound(I(enclosure['remainder'][0]), I(enclosure['remainder'][1])),
            transformed_residual_upper=bbound, original_H_upper=abs_H,
            chart_drift_contribution_upper=vector_bound(enclosure['w']*Q_first[0], enclosure['w']*Q_first[1]),
            commutator_upper=maximum_abs(commutator),
            a_lower=float(enclosure['scalar']['a'].lo), J_upper=float(enclosure['scalar']['J'].hi),
            angular_q_lower=enclosure['angular_q_lower'], geometric_reciprocal_ratio_upper=enclosure['geometric_ratio_upper']))
    return dict(cell=index, left_exact=str(left), right_exact=str(right),
                one_common_auxiliary_mean=True, primitive_both_native_endpoints_exactly_zero=True,
                subpieces=result)


def advance(row, d, k, absolute_d, absolute_k):
    maximum_metric, absolute_metric = 0., 0.
    maximum_D = 0.
    for part in row['subpieces']:
        h = Q(part['right_exact'])-Q(part['left_exact'])
        b, p, J, a = (I(part[key]) for key in ('transformed_residual_upper', 'primitive_Qe1_upper', 'J_upper', 'a_lower'))
        length = qb(h)
        k = k+J*(length*d+qb(h*h/2)*b+length*p)
        d = d+length*b
        defect = k/a
        maximum_metric = max(maximum_metric, float((2*defect+defect.square()).hi))
        maximum_D = max(maximum_D, float((d+I(part['primitive_Q_upper'])).hi))
        H = I(part['original_H_upper'])
        absolute_k = absolute_k+J*(length*absolute_d+qb(h*h/2)*H)
        absolute_d = absolute_d+length*H
        relative = absolute_k/a
        absolute_metric = max(absolute_metric, float((2*relative+relative.square()).hi))
    row['posterior_after_cell'] = dict(d_upper=float(d.hi), k_upper=float(k.hi),
        metric_upper_on_this_cell=maximum_metric, frame_angular_defect_upper_on_this_cell=maximum_D,
        absolute_residual_metric_upper_on_this_cell=absolute_metric)
    return I(float(d.hi)), I(float(k.hi)), I(float(absolute_d.hi)), I(float(absolute_k.hi))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--field', type=Path, required=True)
    parser.add_argument('--profile', type=Path, required=True)
    parser.add_argument('--chart', type=Path, default=ROOT/'notes/2026-11-12-fd2d-balanced-chart-fourier-tail-01.json')
    parser.add_argument('--inlet', type=Path, default=ROOT/'notes/2026-11-12-fd2d-metric-gc-p148-small01-native-bounds-01.json')
    parser.add_argument('--chart-modes', type=int, default=160)
    parser.add_argument('--arcs', type=int, default=1024)
    parser.add_argument('--degree', type=int, default=16)
    parser.add_argument('--exp-order', type=int, default=8)
    parser.add_argument('--reciprocal-order', type=int, default=5)
    parser.add_argument('--start', type=int, default=0)
    parser.add_argument('--stop', type=int)
    parser.add_argument('--stopfile', type=Path)
    parser.add_argument('--rows', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.rows.exists() or args.out.exists():
        raise FileExistsError('Keep every actual continuous run immutable')
    if args.rows.suffix != '.gz':
        raise ValueError('Write complete compressed per-cell checkpoint members')
    if args.degree < 8 or args.exp_order < 1 or args.reciprocal_order < 0:
        raise ValueError('Invalid finite auxiliary polynomial choice')
    M.DEGREE = args.degree
    started = time.monotonic()
    actual = ActualNative(args.field)
    profile = ExactProfile(args.profile, args.field)
    chart = ExactChart(args.chart, args.chart_modes, actual.field)
    inlet = load_json(args.inlet)
    if inlet['field']['sha256'] != identity(args.field)['sha256']:
        raise ValueError('Inlet belongs to another actual field')
    stop = len(actual.mesh)-1 if args.stop is None else args.stop
    if not 0 <= args.start < stop <= len(actual.mesh)-1:
        raise ValueError('Invalid actual native cell range')
    # Covers every possible retained mode before paid auxiliary shortening.
    table_modes = 2*args.exp_order*actual.field.K+args.chart_modes+2*actual.field.K
    print(json.dumps(dict(stage='building complete angular arcs', modes=table_modes,
                          arcs=args.arcs, native_cells=stop-args.start)), flush=True)
    trig = M.trigonometry(table_modes, args.arcs)
    d0 = float(qb(Q(inlet['inlet']['frame_angular_defect_d0_upper_exact'])).hi)
    d, k = I(d0), I(0.)
    absolute_d, absolute_k = I(d0), I(0.)
    maximum_metric = 0.; maximum_absolute = 0.; done = []; stopped = False
    for cell in range(args.start, stop):
        if args.stopfile and args.stopfile.exists():
            stopped = True
            break
        cell_started = time.monotonic()
        row = consume_cell(cell, actual, profile, chart, args.reciprocal_order, args.exp_order, trig)
        d, k, absolute_d, absolute_k = advance(row, d, k, absolute_d, absolute_k)
        row['seconds'] = time.monotonic()-cell_started
        encoded = (json.dumps(row, separators=(',', ':'), allow_nan=False)+'\n').encode()
        with args.rows.open('ab') as stream:
            stream.write(gzip.compress(encoded, mtime=0))
            stream.flush()
        done.append(cell)
        maximum_metric = max(maximum_metric, row['posterior_after_cell']['metric_upper_on_this_cell'])
        maximum_absolute = max(maximum_absolute, row['posterior_after_cell']['absolute_residual_metric_upper_on_this_cell'])
        print(json.dumps(dict(cell=cell, subpieces=len(row['subpieces']),
            metric_upper=maximum_metric, d_upper=float(d.hi), seconds=row['seconds'],
            mean=max(v['mean_vector_upper'] for v in row['subpieces']),
            remainder=max(v['true_H_minus_auxiliary_upper'] for v in row['subpieces']))), flush=True)
    complete = bool(done) and done == list(range(args.start, stop))
    report = dict(schema='fd2d-continuous-native-cell-primitive-posterior-v1', scope=__doc__,
        source=identity(__file__), interval_models=identity(HERE/'fd2d_gc_interval_models.py'),
        interval_polynomial_backend=identity(HERE/'db6f-audit-metric-polynomial.py'),
        interval_elementary_backend=identity(HERE/'db6f-audit-continuous-hermite.py'),
        normal_range_adapter=identity(HERE/'fd2d-metric-normal-interval-arithmetic.py'),
        field=identity(args.field), actual_native_arrays=actual.field.meta['actual_arrays'],
        accurate_profile=identity(args.profile), chart=identity(args.chart), means=identity(chart.means_path), inlet=identity(args.inlet),
        requested_cells=[args.start, stop], completed_cells=done, complete_requested_interval=complete,
        whole_prefix=complete and args.start == 0 and stop == len(actual.mesh)-1,
        radial_domain_exact=[str(actual.mesh[args.start]), str(actual.mesh[stop])],
        all_angles_covered=True, material_coordinate='physical u; scalar x clock and moving xi chart exactly as bound input packets',
        field_definition_unchanged=True, new_calibrated_clock_finite_X=True, old_body_samples_not_used=True,
        auxiliary_approximation=dict(radial_degree=args.degree, native_exponential_order=args.exp_order,
            reciprocal_q_order=args.reciprocal_order, finite_chart_modes=args.chart_modes, angular_arcs=args.arcs,
            angular_chart_value_error_upper=chart.V_error, angular_chart_first_error_upper=chart.d_error,
            auxiliary_outer_coefficient_compaction_budget=M.COMPACT_BUDGET,
            every_removed_coefficient_is_in_uniform_remainder=True, exact_common_native_cell_mean=True,
            primitive_zero_at_native_endpoints=True, fixed_xi_drift_wQxi_included=True,
            piecewise_AC_primitive_identity_used=True),
        initial_frame_angular_defect_upper=d0, initial_position_tangency_defect_exact=0,
        continuation_posterior_requires_true_inlet=(args.start != 0),
        metric_operator_upper=(maximum_metric if args.start == 0 else None),
        local_zero_inlet_metric_upper=(maximum_metric if args.start != 0 else None),
        absolute_residual_metric_operator_upper=(maximum_absolute if args.start == 0 else None),
        final_d_upper=float(d.hi), final_k_upper=float(k.hi), rows=identity(args.rows),
        stopfile_observed=stopped, actual_metric_tolerance_passed=(complete and args.start == 0 and maximum_metric <= 1e-6),
        nonlinear_tail_matched=False, closed_surface=False, seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(complete=complete, whole_prefix=report['whole_prefix'],
        metric_upper=report['metric_operator_upper'], final_d=float(d.hi), final_k=float(k.hi),
        seconds=report['seconds'])), flush=True)


if __name__ == '__main__':
    main()
