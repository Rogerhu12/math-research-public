#!/usr/bin/env python3
"""A finite control compiler for the actual zero-period geometry of R37.

All geometric design/ODE evaluation belongs in the public repository's Actions.
The --toy-check path checks only elementary algebra and numerical interfaces.
The stored controls are frozen before quadrature/frame refinement.  A small
residual is not an exact zero operator, an embedded band, or a finite flex.
"""
from __future__ import annotations

import argparse
import copy
from functools import lru_cache
import hashlib
import json
import math
import os
from pathlib import Path
import time

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import least_squares
from scipy.special import expit


I3 = np.eye(3)
E1 = np.array([1., 0., 0.])
G1 = np.diag([1., -1., -1.])
G2 = np.diag([-1., 1., -1.])
WORD = (1, 2, 1, 2, 2, 1, 2, 1)
STATES = ((1., 0.), (1., 1.), (1., -1.), (2., 0.))
A_CIRCLE = math.sqrt((9.+math.sqrt(33.))/8.)
COORDINATES = [(i, j) for i in range(3) for j in range(3) if (i, j) != (2, 2)]


def cross_matrix(axis):
    x, y, z = np.asarray(axis, dtype=float)
    return np.array([[0., -z, y], [z, 0., -x], [-y, x, 0.]])


def rotation_vector(vector):
    """Rodrigues, without projecting or normalizing a computed frame."""
    vector = np.asarray(vector, dtype=float)
    angle = float(np.linalg.norm(vector))
    K = cross_matrix(vector)
    if angle < 1e-5:
        x = angle*angle
        sinc = 1-x/6+x*x/120-x*x*x/5040
        cosc = .5-x/24+x*x/720-x*x*x/40320
    else:
        sinc = math.sin(angle)/angle
        cosc = (1-math.cos(angle))/(angle*angle)
    return I3+sinc*K+cosc*(K@K)


def axis(k):
    return np.array([-1., 0., float(k)])


def constant_motion(k, h, length, complete_turns=None):
    """Exact constant-control rotation and centerline displacement.

    Complete periods use the proved identity, not an ODE followed by a reset.
    Their nonzero axial displacement is retained.
    """
    a = axis(k)
    frequency = float(np.linalg.norm(a))
    unit = a/frequency
    parallel = unit*unit[0]
    if complete_turns is not None:
        length = complete_turns*2*math.pi/frequency
        return I3.copy(), h*h*length*parallel, float(length)
    angle = frequency*length
    R = rotation_vector(a*length)
    tangent_integral = (length*parallel + math.sin(angle)/frequency*(E1-parallel)
                        + (1-math.cos(angle))/frequency*np.cross(unit, E1))
    return R, h*h*tangent_integral, float(length)


def smooth_step(t):
    """A C-infinity flat step, with its first derivative in normalized time."""
    t = np.asarray(t, dtype=float)
    interior = (t > 0) & (t < 1)
    safe = np.where(interior, t, .5)
    r = 1/(1-safe)-1/safe
    value = expit(r)
    derivative = value*(1-value)*(1/safe**2+1/(1-safe)**2)
    value = np.where(t <= 0, 0., np.where(t >= 1, 1., value))
    derivative = np.where(interior, derivative, 0.)
    return value, derivative


def scalar_values(segment, t):
    t = np.asarray(t, dtype=float)
    if segment['kind'] == 'constant':
        ones = np.ones_like(t)
        return (ones*segment['k'], ones*segment['h'], ones*segment['omega'],
                np.zeros_like(t), np.zeros_like(t))
    S, Sp = smooth_step(t)
    left, right = segment['k0'], segment['k1']
    dk = right-left
    b0, bend, eta = segment['b0'], segment['b_end'], segment['eta']
    b = b0*(1-S)+bend*S+eta*S*(1-S)
    bs = (bend-b0+eta*(1-2*S))*Sp/segment['duration']
    k = left+dk*S
    h = 1/(2*b)
    omega = segment['omega0']+dk*(b0*S+(bend-b0)*S*S/2+eta*(S*S/2-S*S*S/3))
    return k, h, omega, dk*Sp/segment['duration'], -bs/(2*b*b)


def scalar_endpoint(segment):
    if segment['kind'] == 'constant':
        return (segment['k'], segment['h'], segment['omega'])
    b0, bend, eta = segment['b0'], segment['b_end'], segment['eta']
    omega = segment['omega0']+(segment['k1']-segment['k0'])*((b0+bend)/2+eta/6)
    return float(segment['k1']), float(1/(2*bend)), float(omega)


def scalar_bounds(segment):
    """Algebraic extrema of the monotone k/omega and quadratic positive b.

    Values are floating evaluations of the exact formulas, not interval bounds.
    Their definition does not depend on a validation sampling grid.
    """
    if segment['kind'] == 'constant':
        return dict(h_min=segment['h'], h_max=segment['h'], omega_min=segment['omega'],
                    omega_max=segment['omega'], k_abs_max=abs(segment['k']), b_positive=True)
    b0, bend, eta = segment['b0'], segment['b_end'], segment['eta']
    points = [0., 1.]
    if eta != 0 and 0 < (bend-b0+eta)/(2*eta) < 1:
        points.append((bend-b0+eta)/(2*eta))
    bs = [b0*(1-t)+bend*t+eta*t*(1-t) for t in points]
    if min(bs) <= 0:
        raise ValueError('quadratic reciprocal speed is not positive')
    end_omega = scalar_endpoint(segment)[2]
    return dict(h_min=1/(2*max(bs)), h_max=1/(2*min(bs)),
                omega_min=min(segment['omega0'], end_omega),
                omega_max=max(segment['omega0'], end_omega),
                k_abs_max=max(abs(segment['k0']), abs(segment['k1'])), b_positive=True)


def control_scalar_bounds(controls):
    all_bounds = []
    for connector in all_connectors(controls):
        all_bounds.extend(scalar_bounds(segment) for segment in connector['segments'])
    for item in controls['common']:
        if item['kind'] == 'bulk':
            all_bounds.append(dict(h_min=item['h'], h_max=item['h'], omega_min=item['omega'],
                                   omega_max=item['omega'], k_abs_max=abs(item['k']), b_positive=True))
    return dict(h_min=min(item['h_min'] for item in all_bounds),
                h_max=max(item['h_max'] for item in all_bounds),
                omega_min=min(item['omega_min'] for item in all_bounds),
                omega_max=max(item['omega_max'] for item in all_bounds),
                k_abs_max=max(item['k_abs_max'] for item in all_bounds),
                bounds_from_algebraic_extrema=True, interval_certified=False)


def matrix_density(k, h, omega, ks, hs):
    """Actual L|P2 matrix after integration by parts on flat-end segments.

    These are the low-derivative A1/Bj formulas of the published Volterra note.
    No fitting of polynomial coefficients and no trace correction are used.
    """
    k, h, omega, ks, hs = np.broadcast_arrays(k, h, omega, ks, hs)
    d = h*omega-k
    oms = ks/(2*h)
    ds = hs*omega-ks/2
    qs0, qs1 = oms/h-omega*hs/h**2, -hs/h**2
    K00 = k*omega**2-(k*k+1)*omega/h
    K01 = 2*k*omega-(k*k+1)/h
    p0, p1, p2 = -k*(1+d*d)/(2*h), -k*d, -k*h/2
    f = (1+d*d)/h
    fs = 2*d*ds/h-(1+d*d)*hs/h**2
    r0, r1 = (K00*f+fs*qs0)/8, (K01*f+fs*qs1)/8
    s0, s1 = (K00*d+ds*qs0)/4, (K01*d+ds*qs1)/4
    t0, t1 = (K00*h+hs*qs0)/8, (K01*h+hs*qs1)/8
    rows = [np.stack((p0, 2*r1, -4*r0), axis=-1),
            np.stack((p1, 2*s1, -4*s0), axis=-1),
            np.stack((p2, 2*t1, -4*t0), axis=-1)]
    return np.stack(rows, axis=-2)


def constant_density(k, h, omega):
    d = h*omega-k
    w = np.array([(d*d+1)/(4*h), d/2, h/4])
    ell = np.array([-2*k, (k*k+2*k*d-1)/h, -2*(d+k)*(k*d-1)/h**2])
    return np.outer(w, ell)


@lru_cache(maxsize=16)
def gauss_rule(n):
    x, w = leggauss(n)
    return (x+1)/2, w/2


def segment_matrix(segment, quadrature_n):
    if segment['kind'] == 'constant':
        return segment['duration']*constant_density(segment['k'], segment['h'], segment['omega'])
    t, weights = gauss_rule(quadrature_n)
    return segment['duration']*np.einsum('n,nij->ij', weights,
                                                      matrix_density(*scalar_values(segment, t)))


def ramp_cf4(k0, k1, duration, left, step):
    """Right frame equation: early-weight exponential is multiplied first."""
    root3 = math.sqrt(3.)
    t = left+step*np.array([.5-root3/6, .5+root3/6])
    S, _ = smooth_step(t)
    k = k0+(k1-k0)*S
    a1, a2 = (3-2*root3)/12, (3+2*root3)/12
    ds = duration*step
    X = ds*(a2*axis(k[0])+a1*axis(k[1]))
    Y = ds*(a1*axis(k[0])+a2*axis(k[1]))
    return rotation_vector(X)@rotation_vector(Y)


@lru_cache(maxsize=4096)
def ramp_rotation(k0, k1, duration, frame_n):
    F = I3.copy()
    for j in range(frame_n):
        F = F@ramp_cf4(k0, k1, duration, j/frame_n, 1/frame_n)
    return F


def segment_rotation(segment, frame_n):
    if segment['kind'] == 'constant':
        return rotation_vector(axis(segment['k'])*segment['duration'])
    return ramp_rotation(segment['k0'], segment['k1'], segment['duration'], frame_n)


def segment_motion(segment, frame_n):
    if segment['kind'] == 'constant':
        R, displacement, _ = constant_motion(segment['k'], segment['h'], segment['duration'])
        return R, displacement
    F, position = I3.copy(), np.zeros(3)
    root3 = math.sqrt(3.)
    fractions = [.5-root3/6, .5+root3/6]
    for j in range(frame_n):
        left, step = j/frame_n, 1/frame_n
        # Two Gauss nodes; their frames are propagated from this step's left end.
        # This is fourth-order position quadrature with the same CF4 frame rule.
        for fraction in fractions:
            Rnode = ramp_cf4(segment['k0'], segment['k1'], segment['duration'],
                            left, step*fraction)
            _, h, _, _, _ = scalar_values(segment, np.array([left+step*fraction]))
            position += segment['duration']*step*.5*float(h[0])**2*(F@Rnode@E1)
        F = F@ramp_cf4(segment['k0'], segment['k1'], segment['duration'], left, step)
    return F, position


class ConnectorBuilder:
    def __init__(self, start):
        self.state = tuple(map(float, start))
        self.segments = []

    def constant(self, duration, name, variable=None):
        k, h, omega = self.state
        segment = dict(kind='constant', name=name, k=k, h=h, omega=omega,
                       duration=float(duration))
        if variable is not None:
            segment['angle_coordinate'] = int(variable)
        self.segments.append(segment)

    def ramp(self, k1, b1, duration, name, eta=0.):
        k0, h0, omega0 = self.state
        b0 = 1/(2*h0)
        # Linear endpoint interpolation plus a nonnegative S(1-S) gate.
        segment = dict(kind='ramp', name=name, k0=k0, k1=float(k1),
                       b0=float(b0), b_end=float(b1), omega0=omega0,
                       duration=float(duration), eta=float(eta))
        self.segments.append(segment)
        self.state = scalar_endpoint(segment)


def connector_skeleton(start, end, target_name, args):
    """Compile scalar controls, leaving three positive platform times variable."""
    kin, hin, omin = map(float, start)
    kout, hout, omout = map(float, end)
    if target_name == 'I' and np.array_equal(np.asarray(start), np.asarray(end)):
        return [], dict(start=list(start), target=list(end), omega_gate_delta=0.,
                        eta_plus=0., eta_minus=0., omitted_identical_connector=True)
    builder = ConnectorBuilder(start)
    builder.constant(args.end_pad, 'left_constant_germ')
    builder.ramp(0., .5, args.ramp_duration, 'input_cap')
    input_increment = -kin*(1/(2*hin)+.5)/2
    output_increment = kout*(.5+1/(2*hout))/2
    delta = omout-omin-input_increment-output_increment
    center = args.gate_eta_floor+3*math.sqrt(delta*delta+args.gate_smoothing**2)
    eta_plus, eta_minus = center+3*delta, center-3*delta
    builder.ramp(1., .5, args.gate_duration, 'omega_up', eta_plus)
    builder.ramp(0., .5, args.gate_duration, 'omega_down', eta_minus)

    def X(angle, name, variable=None):
        builder.constant(angle, name, variable)

    def Z(angle, name, variable=None):
        builder.ramp(1., .5, args.ramp_duration, name+'_up1')
        builder.constant(math.pi/math.sqrt(2.), name+'_half1')
        builder.ramp(0., .5, args.ramp_duration, name+'_down1')
        X(angle, name+'_x', variable)
        builder.ramp(1., .5, args.ramp_duration, name+'_up2')
        builder.constant(math.pi/math.sqrt(2.), name+'_half2')
        builder.ramp(0., .5, args.ramp_duration, name+'_down2')

    # At zero ramp length this is I. Its three endpoint derivatives span so(3).
    X(2*math.pi, 'free_alpha', 0)
    Z(5*math.pi/2, 'free_beta', 1)
    X(2*math.pi, 'free_gamma', 2)
    Z(3*math.pi/2, 'fixed_inverse_z')
    if target_name == 'g1':
        X(math.pi, 'target_g1')
    elif target_name == 'g2':
        X(3*math.pi/2, 'target_g2_left_x')
        Z(math.pi, 'target_g2_z')
        X(math.pi/2, 'target_g2_right_x')
    elif target_name != 'I':
        raise ValueError(target_name)
    builder.ramp(kout, 1/(2*hout), args.ramp_duration, 'output_cap')
    builder.constant(args.end_pad, 'right_constant_germ')
    metadata = dict(start=list(map(float, start)), target=list(map(float, end)),
                    target_frame=target_name, omega_gate_delta=delta,
                    gate_center=center, eta_plus=eta_plus, eta_minus=eta_minus,
                    input_cap_increment=input_increment, output_cap_increment=output_increment,
                    gate_increment_identity=(eta_plus-eta_minus)/6,
                    scalar_end_before_frame_fit=list(builder.state),
                    scalar_target_error=(np.asarray(builder.state)-np.asarray(end)).tolist(),
                    omitted_identical_connector=False)
    return builder.segments, metadata


def fit_connector(start, end, target_name, args):
    skeleton, metadata = connector_skeleton(start, end, target_name, args)
    target = {'I': I3, 'g1': G1, 'g2': G2}[target_name]
    if not skeleton:
        return dict(segments=[], metadata=metadata, end_state=list(map(float, start)),
                    frame_fit=dict(success=True, nfev=0, full_matrix_residual=0.,
                                   offsets=[0., 0., 0.], singular_values=[1., 1., 1.]))
    fixed = [None if 'angle_coordinate' in segment else segment_rotation(segment, args.frame_n)
             for segment in skeleton]

    def endpoint(offsets, with_jacobian=False):
        F = I3.copy()
        derivatives = np.zeros((3, 3, 3))
        for segment, rotation in zip(skeleton, fixed):
            coordinate = segment.get('angle_coordinate')
            if coordinate is not None:
                rotation = rotation_vector(axis(segment['k'])*(segment['duration']+offsets[coordinate]))
            old = F
            if with_jacobian:
                derivatives = np.einsum('aij,jk->aik', derivatives, rotation)
                if coordinate is not None:
                    derivatives[coordinate] += old@rotation@cross_matrix(axis(segment['k']))
            F = old@rotation
        if with_jacobian:
            return (F-target).ravel(), derivatives.reshape(3, 9).T
        return (F-target).ravel()

    fit = least_squares(endpoint, np.zeros(3), jac=lambda x: endpoint(x, True)[1],
                        bounds=(-np.full(3, math.pi-.03), np.full(3, math.pi-.03)),
                        xtol=2e-13, ftol=2e-13, gtol=2e-13,
                        max_nfev=args.frame_max_nfev)
    segments = copy.deepcopy(skeleton)
    for segment in segments:
        coordinate = segment.pop('angle_coordinate', None)
        if coordinate is not None:
            segment['duration'] += float(fit.x[coordinate])
        if segment['duration'] <= 0:
            raise ValueError('nonpositive platform time')
    residual = float(np.linalg.norm(endpoint(fit.x)))
    analytic_jacobian = endpoint(fit.x, True)[1]
    finite_jacobian = absolute_jacobian(endpoint, fit.x, 2e-6)
    jac_error = float(np.linalg.norm(analytic_jacobian-finite_jacobian)
                      /max(np.linalg.norm(finite_jacobian), 1e-30))
    return dict(segments=segments, metadata=metadata, end_state=list(scalar_endpoint(segments[-1])),
                frame_fit=dict(success=bool(fit.success), nfev=int(fit.nfev),
                    full_matrix_residual=residual, offsets=fit.x.tolist(),
                    singular_values=np.linalg.svd(analytic_jacobian, compute_uv=False).tolist(),
                    analytic_jacobian_relative_difference=jac_error,
                    within_numeric_gate=bool(residual < args.frame_gate)))


def matrix8(M):
    return np.array([M[i, j] for i, j in COORDINATES])


def bulk_preconditioner():
    a = A_CIRCLE
    cA = 4*math.pi*a*(a*a+3)/(1+a*a)**1.5
    cB = 4*math.pi/(1+a*a)**1.5
    columns = []
    for h, d in STATES:
        w = np.array([(d*d+1)/(4*h), d/2, h/4])
        A = np.array([0., 1/h, -2*d/h**2])
        B = np.array([-2., 2*d/h, -2*(d*d-1)/h**2])
        columns.extend([matrix8(cA*np.outer(w, A)), matrix8(cB*np.outer(w, B))])
    J = np.column_stack(columns)
    return J, np.linalg.inv(J)


def compile_controls(parameters, args):
    """Only this design-time function solves the 3-angle frame controls."""
    common, state = [], (0., 1., 0.)
    for i, (h, d) in enumerate(STATES):
        alpha, beta = parameters[2*i:2*i+2]
        for branch, k in [('zero', 0.), ('plus', A_CIRCLE+alpha+beta),
                          ('minus', -A_CIRCLE-alpha+beta)]:
            desired = (float(k), h, float((d+k)/h))
            connector = fit_connector(state, desired, 'I', args)
            common.append(dict(kind='connector', name=f'state{i}_{branch}_entry', **connector))
            # Preserve the scalar endpoint actually obtained by the antiderivative.
            # No independent omega gauge is inserted at a bulk circle.
            state = tuple(connector['end_state'])
            common.append(dict(kind='bulk', name=f'state{i}_{branch}_circles',
                               k=state[0], h=state[1], omega=state[2], turns=int(args.turns),
                               prescribed_state=list(desired)))
    last = fit_connector(state, (0., 1., 0.), 'I', args)
    common.append(dict(kind='connector', name='common_return', **last))
    state = tuple(last['end_state'])
    bridges = {str(j): dict(kind='connector', name=f'bridge_g{j}',
                           **fit_connector(state, (0., 1., 0.), f'g{j}', args)) for j in (1, 2)}
    controls = dict(format='R37-flat-ramp-controls-v1', parameters=list(map(float, parameters)),
                    turns=int(args.turns), common=common, bridges=bridges,
                    word=list(WORD), start_state=[0., 1., 0.],
                    scalar_formula='k=k0+(k1-k0)S; b=b0*(1-S)+b_end*S+eta*S*(1-S); omega=omega0+dk*integral_0^S b',
                    omega_global_definition='unique primitive from the single starting value; per-segment omega0 values are floating caches, not new gauges',
                    flat_step='expit(1/(1-t)-1/t), extended by 0 and 1',
                    complete_period_rule='turns*2*pi/sqrt(1+k^2); exact identity frame, retained axial displacement')
    return controls


def connector_matrix(connector, quadrature_n):
    answer = np.zeros((3, 3))
    for segment in connector['segments']:
        answer += segment_matrix(segment, quadrature_n)
    return answer


def controls_matrix(controls, quadrature_n):
    bulk, common = np.zeros((3, 3)), np.zeros((3, 3))
    for item in controls['common']:
        if item['kind'] == 'bulk':
            period = 2*math.pi/math.sqrt(1+item['k']**2)
            bulk += period*constant_density(item['k'], item['h'], item['omega'])
        else:
            common += connector_matrix(item, quadrature_n)
    bridges = [connector_matrix(controls['bridges'][str(j)], quadrature_n) for j in (1, 2)]
    normalized = bulk+(common+(bridges[0]+bridges[1])/2)/controls['turns']
    total = 8*controls['turns']*normalized
    return dict(bulk_per_turn=bulk, common_connectors=common, bridge_matrices=bridges,
                normalized=normalized, total=total)


def all_connectors(controls):
    return ([item for item in controls['common'] if item['kind'] == 'connector']
            + list(controls['bridges'].values()))


def connector_motion(connector, frame_n):
    F, position, length = I3.copy(), np.zeros(3), 0.
    for segment in connector['segments']:
        R, displacement = segment_motion(segment, frame_n)
        position += F@displacement
        F = F@R
        length += segment['duration']
    return F, position, float(length)


def connector_centerline_length(connector, quadrature_n):
    length = 0.
    t, weights = gauss_rule(quadrature_n)
    for segment in connector['segments']:
        if segment['kind'] == 'constant':
            length += segment['duration']*segment['h']**2
        else:
            _, h, _, _, _ = scalar_values(segment, t)
            length += segment['duration']*float(weights@(h*h))
    return length


def translate_matrix(M, shift):
    plus = np.array([[1., shift, shift*shift], [0., 1., 2*shift], [0., 0., 1.]])
    minus = np.array([[1., -shift, shift*shift], [0., 1., -2*shift], [0., 0., 1.]])
    return plus@M@minus


def frozen_diagnostic(controls, quadrature_n, frame_n, inverse, previous=None):
    """Re-evaluate one immutable control object; never fit/reset any endpoint."""
    matrices = controls_matrix(controls, quadrature_n)
    motions, centerline_lengths, summaries = {}, {}, []
    min_h, max_h = math.inf, 0.
    min_omega, max_omega, max_abs_k = math.inf, -math.inf, 0.
    sample_t = np.linspace(0., 1., max(257, 2*quadrature_n+1))
    derivative_relation_error = 0.
    max_scalar_join = 0.
    for connector in all_connectors(controls):
        motion = connector_motion(connector, frame_n)
        motions[connector['name']] = motion
        centerline_lengths[connector['name']] = connector_centerline_length(connector, quadrature_n)
        target = {'I': I3, 'g1': G1, 'g2': G2}.get(connector['metadata'].get('target_frame', 'I'))
        frame_error = float(np.linalg.norm(motion[0]-target))
        start = np.array(connector['metadata']['start'])
        actual = np.array(connector['end_state'])
        summaries.append(dict(name=connector['name'], frame_error=frame_error,
            frame_orthogonality=float(np.linalg.norm(motion[0].T@motion[0]-I3)),
            scalar_target_error=(actual-np.array(connector['metadata']['target'])).tolist(),
            omega_increment=float(actual[2]-start[2]), displacement=motion[1].tolist(),
            sphere_arclength=motion[2], centerline_arclength=centerline_lengths[connector['name']],
            frame_fit=connector['frame_fit']))
        running = start
        for segment in connector['segments']:
            if segment['kind'] == 'constant':
                initial = np.array([segment['k'], segment['h'], segment['omega']])
            else:
                initial = np.array([segment['k0'], 1/(2*segment['b0']), segment['omega0']])
            max_scalar_join = max(max_scalar_join, float(np.linalg.norm(initial-running)))
            running = np.array(scalar_endpoint(segment))
            k, h, omega, ks, hs = scalar_values(segment, sample_t)
            min_h, max_h = min(min_h, float(np.min(h))), max(max_h, float(np.max(h)))
            min_omega, max_omega = min(min_omega, float(np.min(omega))), max(max_omega, float(np.max(omega)))
            max_abs_k = max(max_abs_k, float(np.max(abs(k))))
            if segment['kind'] == 'ramp':
                S, Sp = smooth_step(sample_t)
                b0, bend, eta = segment['b0'], segment['b_end'], segment['eta']
                omega_s = ((segment['k1']-segment['k0'])/segment['duration']
                           * (b0*(1-S)+bend*S+eta*S*(1-S))*Sp)
                derivative_relation_error = max(derivative_relation_error,
                                                   float(np.max(abs(omega_s-ks/(2*h)))))
    F, position, common_length, common_centerline_length = I3.copy(), np.zeros(3), 0., 0.
    for item in controls['common']:
        if item['kind'] == 'bulk':
            R, displacement, length = constant_motion(item['k'], item['h'], 0., item['turns'])
            common_centerline_length += item['h']**2*length
            min_h, max_h = min(min_h, item['h']), max(max_h, item['h'])
            min_omega, max_omega = min(min_omega, item['omega']), max(max_omega, item['omega'])
            max_abs_k = max(max_abs_k, abs(item['k']))
        else:
            R, displacement, length = motions[item['name']]
            common_centerline_length += centerline_lengths[item['name']]
        position += F@displacement
        F = F@R
        common_length += length
    path_frames, path_positions, path_lengths, path_matrices, omega_increments = {}, {}, {}, {}, {}
    for j in (1, 2):
        bridge = controls['bridges'][str(j)]
        R, displacement, length = motions[bridge['name']]
        path_frames[j] = F@R
        path_positions[j] = position+F@displacement
        path_lengths[j] = common_length+length
        path_matrices[j] = (controls['turns']*matrices['bulk_per_turn']
                            + matrices['common_connectors']+matrices['bridge_matrices'][j-1])
        omega_increments[j] = float(bridge['end_state'][2]-controls['start_state'][2])
    # 1. Natural frame propagation gives a single continuous approximate ODE path.
    # 2. Exact group placement cancels positions but leaves the reported seam errors.
    natural_frame, natural_position, group = I3.copy(), np.zeros(3), I3.copy()
    placed_position = np.zeros(3)
    continuous_matrix, omega_offset = np.zeros((3, 3)), 0.
    omega_prefix_offsets = [0.]
    seams, scalar_seams, total_length, total_centerline_length = [], [], 0., 0.
    for j in WORD:
        target = G1 if j == 1 else G2
        seams.append(float(np.linalg.norm(group@path_frames[j]-group@target)))
        scalar_seams.append(abs(omega_increments[j]))
        natural_position += natural_frame@path_positions[j]
        natural_frame = natural_frame@path_frames[j]
        placed_position += group@path_positions[j]
        continuous_matrix += translate_matrix(path_matrices[j], omega_offset)
        omega_offset += omega_increments[j]
        omega_prefix_offsets.append(omega_offset)
        group = group@target
        total_length += path_lengths[j]
        total_centerline_length += common_centerline_length+centerline_lengths[controls['bridges'][str(j)]['name']]
    preconditioned = inverse@matrix8(matrices['normalized'])
    # The physical strip was selected once, before any validation.  It is not refit.
    xi_left, xi_right = controls['physical_strip_xi']
    exact_formula_bounds = controls['scalar_extrema']
    omega_prefix_max = max(map(abs, omega_prefix_offsets))
    physical_gap = xi_left+exact_formula_bounds['omega_min']-omega_prefix_max
    physical_u_bounds = [exact_formula_bounds['h_min']/(xi_right+exact_formula_bounds['omega_max']+omega_prefix_max),
                         exact_formula_bounds['h_max']/physical_gap]
    data = dict(quadrature_n=int(quadrature_n), frame_steps_per_ramp=int(frame_n),
        normalized_matrix=matrices['normalized'].tolist(), total_matrix=matrices['total'].tolist(),
        bulk_per_turn=matrices['bulk_per_turn'].tolist(),
        common_connector_matrix=matrices['common_connectors'].tolist(),
        bridge_matrices=[m.tolist() for m in matrices['bridge_matrices']],
        total_matrix_frobenius=float(np.linalg.norm(matrices['total'])),
        normalized_matrix_frobenius=float(np.linalg.norm(matrices['normalized'])),
        preconditioned_eight_l2=float(np.linalg.norm(preconditioned)),
        trace_without_correction=float(np.trace(matrices['total'])),
        common_frame_error=float(np.linalg.norm(F-I3)),
        path_frame_errors={str(j): float(np.linalg.norm(path_frames[j]-(G1 if j == 1 else G2))) for j in (1, 2)},
        natural_full_frame_error=float(np.linalg.norm(natural_frame-I3)),
        natural_full_frame_orthogonality=float(np.linalg.norm(natural_frame.T@natural_frame-I3)),
        natural_alpha_closure=natural_position.tolist(),
        natural_alpha_closure_norm=float(np.linalg.norm(natural_position)),
        natural_alpha_closure_over_sphere_arclength=float(np.linalg.norm(natural_position)/total_length),
        natural_alpha_closure_over_centerline_arclength=float(np.linalg.norm(natural_position)/total_centerline_length),
        ideal_Klein_position_sum=placed_position.tolist(),
        ideal_Klein_frame_seam_errors=seams, ideal_Klein_omega_seam_errors=scalar_seams,
        continuously_carried_omega_closure=omega_offset,
        continuously_carried_omega_prefix_offsets=omega_prefix_offsets,
        continuously_carried_omega_prefix_max=omega_prefix_max,
        continuously_carried_omega_total_matrix=continuous_matrix.tolist(),
        omega_carry_matrix_difference=float(np.linalg.norm(continuous_matrix-matrices['total'])),
        scalar_segment_join_max=max_scalar_join,
        omega_derivative_identity_max_sample=derivative_relation_error,
        sphere_arclength=total_length, centerline_arclength=total_centerline_length,
        h_min_sample=min_h, h_max_sample=max_h,
        omega_min_sample=min_omega, omega_max_sample=max_omega, max_abs_curvature_sample=max_abs_k,
        physical_strip_xi=[xi_left, xi_right],
        physical_strip_omega_gap_from_algebraic_extrema=physical_gap,
        physical_strip_u_bounds_from_algebraic_extrema=physical_u_bounds,
        physical_strip_interval_certified=False, physical_strip_frozen=True,
        connectors=summaries, frozen_controls_refit=False,
        exact_finite_N_zero_operator_certified=False,
        exact_frozen_bridge_closure_certified=False,
        embedding_checked=False, embedded_certified=False, reach_lower_certified=False, finite_isometric_family=False,
        task_complete=False)
    if previous is not None:
        data['fixed_control_changes_from_previous'] = dict(
            total_matrix_frobenius=float(np.linalg.norm(matrices['total']-np.array(previous['total_matrix']))),
            natural_alpha_closure=float(np.linalg.norm(natural_position-np.array(previous['natural_alpha_closure']))),
            natural_full_frame_error_difference=abs(data['natural_full_frame_error']-previous['natural_full_frame_error']))
    return data


class BudgetExceeded(RuntimeError):
    pass


def absolute_jacobian(function, x, step):
    columns = []
    for j in range(len(x)):
        increment = step*max(1., abs(x[j]))
        plus, minus = np.array(x, copy=True), np.array(x, copy=True)
        plus[j] += increment
        minus[j] -= increment
        columns.append((function(plus)-function(minus))/(2*increment))
    return np.column_stack(columns)


def design(args):
    start = time.monotonic()
    J0, inverse = bulk_preconditioner()
    x0 = np.zeros(8)
    cache, best = {}, {}
    calls = 0

    def evaluate(x, enforce_budget=True, consider_best=True):
        nonlocal calls
        key = tuple(map(float, x))
        if key in cache:
            return cache[key]
        if enforce_budget and time.monotonic()-start > args.design_seconds and best:
            raise BudgetExceeded('design wall budget reached; retained best actually evaluated controls')
        controls = compile_controls(np.asarray(x, dtype=float), args)
        matrices = controls_matrix(controls, args.quadrature_n)
        residual = inverse@matrix8(matrices['normalized'])
        frame_max = max(connector['frame_fit']['full_matrix_residual'] for connector in all_connectors(controls))
        value = dict(controls=controls, residual=residual, matrices=matrices,
                     norm=float(np.linalg.norm(residual)), frame_max=frame_max)
        calls += 1
        # Invalid frame fits cannot masquerade as the best compiled candidate.
        if consider_best and frame_max < args.frame_gate and (not best or value['norm'] < best['value']['norm']):
            best.update(x=np.asarray(x, dtype=float).copy(), value=value)
        if len(cache) > 80:
            cache.clear()
        cache[key] = value
        return value

    initial = evaluate(x0)
    if not best:
        best.update(x=x0.copy(), value=initial)
    solver = dict(success=False, message='not started')
    try:
        def residual(x):
            value = evaluate(x)
            if value['frame_max'] > args.frame_gate:
                raise RuntimeError('inner frame fit failed; no closure reset is permitted')
            return value['residual']
        fit = least_squares(residual, x0,
            jac=lambda x: absolute_jacobian(residual, x, args.jacobian_step),
            bounds=(-np.full(8, args.parameter_bound), np.full(8, args.parameter_bound)),
            max_nfev=args.max_nfev, xtol=2e-12, ftol=2e-12, gtol=2e-12, x_scale='jac')
        evaluate(fit.x)
        solver = dict(success=bool(fit.success), message=str(fit.message), nfev=int(fit.nfev),
                      optimality=float(fit.optimality), reported_parameters=fit.x.tolist())
    except (BudgetExceeded, RuntimeError, ValueError) as error:
        solver = dict(success=False, message=f'{type(error).__name__}: {error}')
    candidate = best['value']
    controls = candidate['controls']
    derivative_check = dict(completed=False, reason='not attempted')
    try:
        check_point = best['x'].copy()
        check_function = lambda x: evaluate(x, consider_best=False)['residual']
        Jcheck = absolute_jacobian(check_function, check_point, args.jacobian_step)
        direction = np.random.default_rng(20261114).normal(size=8)
        direction /= np.linalg.norm(direction)
        directional_step = 2e-6
        observed = (check_function(check_point+directional_step*direction)
                    -check_function(check_point-directional_step*direction))/(2*directional_step)
        derivative_check = dict(completed=True, at_parameters=check_point.tolist(),
            column_step_floor=args.jacobian_step, directional_step=directional_step,
            relative_difference=float(np.linalg.norm(Jcheck@direction-observed)/max(np.linalg.norm(observed), 1e-30)),
            singular_values=np.linalg.svd(Jcheck, compute_uv=False).tolist())
    except (BudgetExceeded, RuntimeError, ValueError) as error:
        derivative_check = dict(completed=False, reason=str(error))
    # Select all physical domain parameters exactly once, before validation.
    extrema = control_scalar_bounds(controls)
    omega_drift = sum(abs(controls['bridges'][str(j)]['end_state'][2]) for j in WORD)
    xi_left = 1.+max(0., -extrema['omega_min']+omega_drift)
    controls['scalar_extrema'] = extrema
    controls['physical_strip_xi'] = [xi_left, xi_left+1.]
    controls['global_normalization'] = 'none; the four h states and every duration retain their defined values'
    serialized = json.dumps(controls, sort_keys=True, separators=(',', ':'), allow_nan=False)
    identity = hashlib.sha256(serialized.encode()).hexdigest()
    frozen_at = time.monotonic()
    validation = []
    for multiplier in args.validation_multipliers:
        validation.append(frozen_diagnostic(controls, multiplier*args.quadrature_n,
                          multiplier*args.frame_n, inverse, validation[-1] if validation else None))
    # Only the frozen candidate is evaluated below; no design call follows freeze.
    return dict(schema='R37-finite-N-instance-v1', research_executed_in_actions=bool(os.environ.get('GITHUB_ACTIONS')),
        github=dict(run_id=os.environ.get('GITHUB_RUN_ID'), run_attempt=os.environ.get('GITHUB_RUN_ATTEMPT'),
                    source_sha=os.environ.get('GITHUB_SHA')),
        source_script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        design_identity_sha256=identity, controls=controls,
        settings={k: str(v) if isinstance(v, Path) else v for k, v in vars(args).items()},
        preconditioner=dict(bulk_jacobian=J0.tolist(), inverse=inverse.tolist(),
                            condition_number=float(np.linalg.cond(J0)), frozen_from_exact_bulk=True),
        initial=dict(parameters=x0.tolist(), normalized_matrix=initial['matrices']['normalized'].tolist(),
                     preconditioned_eight_l2=initial['norm'], max_frame_fit_error=initial['frame_max']),
        final_parameters=best['x'].tolist(), best_preconditioned_eight_l2=candidate['norm'],
        selected_frame_fit_max=candidate['frame_max'],
        selected_frame_numeric_gate_passed=bool(candidate['frame_max'] < args.frame_gate),
        all_design_evaluations=calls,
        derivative_method=dict(method='absolute central columns',
                               step_formula='step*max(1,abs(parameter))', step=args.jacobian_step),
        final_directional_derivative_check=derivative_check,
        solver=solver, design_seconds=frozen_at-start,
        validation_seconds=time.monotonic()-frozen_at, validation=validation,
        exact_R37_existence_theorem_separate_from_this_numerical_candidate=True,
        frozen_finite_N_root_certified=False, full_period_profile_constructed=False,
        third_order_range_checked=False, finite_isometric_family=False, task_complete=False)


def toy_check():
    # These are formula/interface tests only, not the 12-circle geometric design.
    k, h, omega = .3, 1.7, -.4
    density_error = float(np.max(abs(matrix_density(k, h, omega, 0., 0.)-constant_density(k, h, omega))))
    trace_error = float(abs(np.trace(matrix_density(k, h, omega, .7, -.2))))
    delta, center = -.7, 3.1
    eta_plus, eta_minus = center+3*delta, center-3*delta
    omega_error = abs((eta_plus-eta_minus)/6-delta)
    R, displacement, length = constant_motion(k, h, 0., 3)
    axis_ = axis(k)
    parallel = axis_*axis_[0]/(axis_@axis_)
    full_circle_error = float(np.linalg.norm(displacement-h*h*length*parallel))
    ordinary_R, _, _ = constant_motion(k, h, .7)
    raw = I3.copy()
    for j in range(8):
        raw = raw@ramp_cf4(k, k, .7, j/8, 1/8)
    constant_cf4_error = float(np.linalg.norm(raw-ordinary_R))
    group, starts = I3.copy(), {1: [], 2: []}
    for j in WORD:
        starts[j].append(group.copy())
        group = group@(G1 if j == 1 else G2)
    klein_error = float(max(np.linalg.norm(sum(starts[j], np.zeros((3, 3)))) for j in (1, 2)))
    X = lambda angle: rotation_vector(np.array([-angle, 0., 0.]))
    half = rotation_vector(axis(1.)*math.pi/math.sqrt(2.))
    Z = lambda angle: half@X(angle)@half
    identity_prefix_error = float(np.linalg.norm(X(2*math.pi)@Z(5*math.pi/2)@X(2*math.pi)@Z(3*math.pi/2)-I3))
    g2_word_error = float(np.linalg.norm(X(3*math.pi/2)@Z(math.pi)@X(math.pi/2)-G2))
    # Differentiate a three-platform product, including right-acting convention.
    x = np.array([.2, -.3, .5])
    axes = [np.array([1., 0., 0.]), np.array([0., 0., 1.]), np.array([1., 0., 0.])]
    def product(y):
        answer = I3.copy()
        for a, angle in zip(axes, y):
            answer = answer@rotation_vector(a*angle)
        return answer.ravel()
    analytic = []
    rotations = [rotation_vector(a*angle) for a, angle in zip(axes, x)]
    for j in range(3):
        answer = I3.copy()
        for i in range(3):
            answer = answer@rotations[i]
            if i == j:
                answer = answer@cross_matrix(axes[i])
        analytic.append(answer.ravel())
    jac_error = float(np.max(abs(absolute_jacobian(product, x, 2e-6)-np.array(analytic).T)))
    output = dict(toy_check=True, no_research_geometry_evaluation=True, no_optimization=True,
        constant_density_error=density_error, pointwise_trace_error=trace_error,
        omega_gate_identity_error=omega_error, complete_circle_displacement_error=full_circle_error,
        constant_CF4_error=constant_cf4_error, Klein_word_error=klein_error,
        identity_prefix_error=identity_prefix_error, g2_word_error=g2_word_error,
        rotation_product_jacobian_error=jac_error)
    if max(density_error, trace_error, omega_error, full_circle_error, constant_cf4_error,
           klein_error, identity_prefix_error, g2_word_error, jac_error) > 2e-9:
        raise AssertionError(output)
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path)
    parser.add_argument('--toy-check', action='store_true')
    parser.add_argument('--turns', type=int, default=16384)
    parser.add_argument('--quadrature-n', type=int, default=64)
    parser.add_argument('--frame-n', type=int, default=96)
    parser.add_argument('--validation-multipliers', type=int, nargs='+', default=[1, 2, 4])
    parser.add_argument('--ramp-duration', type=float, default=.06)
    parser.add_argument('--gate-duration', type=float, default=.25)
    parser.add_argument('--end-pad', type=float, default=.02)
    parser.add_argument('--gate-eta-floor', type=float, default=.05)
    parser.add_argument('--gate-smoothing', type=float, default=.25)
    parser.add_argument('--frame-max-nfev', type=int, default=50)
    parser.add_argument('--frame-gate', type=float, default=2e-9)
    parser.add_argument('--parameter-bound', type=float, default=.2)
    parser.add_argument('--jacobian-step', type=float, default=2e-5)
    parser.add_argument('--max-nfev', type=int, default=32)
    parser.add_argument('--design-seconds', type=float, default=900.)
    args = parser.parse_args()
    if args.toy_check:
        result = toy_check()
    else:
        if os.environ.get('GITHUB_ACTIONS') != 'true':
            raise SystemExit('Research design runs only in public GitHub Actions; use --toy-check locally.')
        if os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public':
            raise SystemExit('Research design is restricted to Rogerhu12/math-research-public Actions.')
        if args.out is None:
            raise SystemExit('Research runs require --out; the full control definition is written to a small file.')
        if args.turns < 1 or min(args.quadrature_n, args.frame_n) < 8:
            raise SystemExit('positive complete turns and at least eight integration nodes are required')
        if min(args.ramp_duration, args.gate_duration, args.end_pad,
               args.gate_eta_floor, args.gate_smoothing) <= 0:
            raise SystemExit('all segment durations and gate positivity parameters must be positive')
        result = design(args)
    encoded = json.dumps(result, indent=2, allow_nan=False)+'\n'
    if len(encoded.encode()) >= 5_000_000:
        raise RuntimeError('report exceeds repository 5 MB limit')
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(encoded)
        print(json.dumps(dict(output=str(args.out), bytes=len(encoded.encode()),
                              sha256=hashlib.sha256(encoded.encode()).hexdigest(),
                              task_complete=False)))
    else:
        print(encoded)


if __name__ == '__main__':
    main()
