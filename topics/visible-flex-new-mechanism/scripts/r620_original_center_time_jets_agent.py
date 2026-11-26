#!/usr/bin/env python3
"""R620 exact finite-width center chart and original full-feedback input.

Pure interface only: no new scientific request, seed execution or solver.
Every time-jet coefficient is itself the original parameter Jet, so all
mixed parameter/time chains, true M, rho and full potential are preserved.
Scientific use belongs only to the named public repository's Actions.
"""
from __future__ import annotations

from dataclasses import dataclass
import time

import numpy as np

import r612_r614_reduced_function_map_agent as reduced

original = reduced.original
paid, LD, Jet = original.paid, original.LD, original.Jet


@dataclass
class TimeJet2:
    """Physical time value/first/second, each with the full parameter Jet."""
    v: Jet
    d1: Jet
    d2: Jet

    __array_priority__ = 20000

    @classmethod
    def constant(cls, value):
        if not isinstance(value, Jet):
            raise TypeError("A constant time jet retains an explicit original parameter Jet.")
        zero = value*0
        return cls(value, zero, zero)

    @property
    def value(self):
        return self.v.value

    @property
    def derivative(self):
        # Original multiply_position uses this only to decide whether an
        # out-of-basis coefficient is identically zero. Include every lane.
        return np.r_[self.v.derivative, self.d1.value, self.d1.derivative,
                     self.d2.value, self.d2.derivative]

    def coerce(self, other):
        return other if isinstance(other, TimeJet2) else self.constant(self.v.coerce(other))

    def __add__(self, other):
        other = self.coerce(other)
        return TimeJet2(self.v+other.v, self.d1+other.d1, self.d2+other.d2)

    __radd__ = __add__

    def __neg__(self):
        return TimeJet2(-self.v, -self.d1, -self.d2)

    def __sub__(self, other):
        return self+-self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other)+-self

    def __mul__(self, other):
        other = self.coerce(other)
        return TimeJet2(self.v*other.v,
                        self.d1*other.v+self.v*other.d1,
                        self.d2*other.v+2*self.d1*other.d1+self.v*other.d2)

    __rmul__ = __mul__

    def __pow__(self, power):
        if not isinstance(power, int):
            raise TypeError("The original center uses integer monomial powers only.")
        if power == 0:
            return self.coerce(1)
        if power == 1:
            return self
        first = power*self.v**(power-1)
        return TimeJet2(self.v**power, first*self.d1,
                        power*(power-1)*self.v**(power-2)*self.d1*self.d1+first*self.d2)

    def __truediv__(self, other):
        return self*self.coerce(other)**-1

    def __rtruediv__(self, other):
        return self.coerce(other)*self**-1


class OriginalCoefficientTimeJets:
    """Same original monomial matrix, exact product-chain time two-jets.

    No derivative is obtained by finite differences or by replaying an old
    directional gate. Zero-valued k/eta/history coordinates use integer
    powers directly; no monomial/value division loses their derivatives.
    """
    def __init__(self, coefficients):
        reduced.require_public_science()
        self.source = coefficients
        self.exponents = np.asarray(coefficients.gkeys, int)
        self.matrix = coefficients.coefficients
        self.unique = [np.unique(self.exponents[:, index])
                       for index in range(self.exponents.shape[1])]
        self.evaluations = 0
        self.seconds = 0.

    def evaluate(self, geometry, history):
        reduced.require_public_science()
        started = time.monotonic()
        self.evaluations += 1
        try:
            zero = geometry[0]*0
            fields = list(geometry)+[zero, zero]+list(history)
            count = self.exponents.shape[0]
            dimension = len(fields[0].v.derivative)
            value, first, second = np.ones(count, dtype=LD), np.zeros(count, dtype=LD), np.zeros(count, dtype=LD)
            vp = np.zeros((count, dimension), dtype=LD)
            fp, sp = vp.copy(), vp.copy()
            for index, field in enumerate(fields):
                powers = {int(power):field**int(power) for power in self.unique[index]}
                selected = [powers[int(power)] for power in self.exponents[:, index]]
                lanes = []
                for name in ("v", "d1", "d2"):
                    rows = [getattr(item, name) for item in selected]
                    lanes.append(paid.values_and_jacobian(rows))
                (f0, p0), (f1, p1), (f2, p2) = lanes
                next_vp = vp*f0[:, None]+value[:, None]*p0
                next_fp = (fp*f0[:, None]+first[:, None]*p0
                           +vp*f1[:, None]+value[:, None]*p1)
                next_sp = (sp*f0[:, None]+second[:, None]*p0
                           +2*(fp*f1[:, None]+first[:, None]*p1)
                           +vp*f2[:, None]+value[:, None]*p2)
                value, first, second = (value*f0, first*f0+value*f1,
                                        second*f0+2*first*f1+value*f2)
                vp, fp, sp = next_vp, next_fp, next_sp
            outputs = [(self.matrix@values, self.matrix@jacobian)
                       for values, jacobian in ((value, vp), (first, fp), (second, sp))]
            return [TimeJet2(*(Jet(values[i], jacobian[i]) for values, jacobian in outputs))
                    for i in range(len(outputs[0][0]))]
        finally:
            self.seconds += time.monotonic()-started


class OriginalPotentialTimeJets:
    """The same untruncated positive Gram, including both mixed time terms."""
    def __init__(self, potential):
        reduced.require_public_science()
        self.source = potential
        self.image_calls = self.pair_calls = self.center_difference_calls = 0

    def image(self, vector):
        self.image_calls += 1
        outputs = []
        for name in ("v", "d1", "d2"):
            values, jacobian = paid.values_and_jacobian([getattr(item, name) for item in vector])
            outputs.append((self.source.factor@(self.source.scales*values),
                            self.source.factor@(self.source.scales[:, None]*jacobian)))
        return outputs

    @staticmethod
    def dot(left, right):
        lv, lp = left
        rv, rp = right
        return Jet(lv@rv, lp.T@rv+rp.T@lv)

    def pair(self, left, right):
        self.pair_calls += 1
        a, b = self.image(left), self.image(right)
        return TimeJet2(self.dot(a[0], b[0]),
                        self.dot(a[1], b[0])+self.dot(a[0], b[1]),
                        self.dot(a[2], b[0])+2*self.dot(a[1], b[1])+self.dot(a[0], b[2]))

    def weighted_pair(self, left, right, h, d):
        eleft = paid.multiply_position(left, [d, h])
        eright = paid.multiply_position(right, [d, h])
        return self.pair(left, right)+self.pair(eleft, eright)

    def center_difference(self, geometry, history, center_geometry, center_history):
        self.center_difference_calls += 1
        h, k, eta, _, _ = geometry
        hc, d = center_geometry[0], h*eta-k
        current, _, _ = paid.profile_vectors(geometry, history)
        centered, fc, hac = paid.profile_vectors(center_geometry, center_history)
        first = self.weighted_pair(paid.vector_add(current, centered, -1),
                                   paid.vector_add(current, centered), h, d)
        deltaq = [h*0, -2*h*d, hc*hc*d*d+(hc-h)*(hc+h)]
        return (first-4*self.pair(paid.multiply_position(fc, deltaq), hac))/(64*h)


def build_center_chart(parameters, coefficients, potential, derivatives=True):
    """[H,v,p0c,p2c,s1c,r0c,a0,j0,f0,L] -> full original center and zeta.

    The output retains the parameter Jets for the original physical RHS.
    No trajectory, numerical fit, center rank experiment or new request is
    run here; the finite-model residual observations accompany its definition.
    """
    reduced.require_public_science()
    started = time.monotonic()
    parameters = np.asarray(parameters, dtype=LD)
    if parameters.shape != (10,) or not np.all(np.isfinite(parameters)):
        raise ValueError("The original center chart has exactly ten finite physical parameters.")
    dimension = 10 if derivatives else 0
    identity = np.eye(10, dtype=LD) if derivatives else None
    jets = [Jet(value, identity[i] if derivatives else np.zeros(0))
            for i, value in enumerate(parameters)]
    H, v, p0c, p2c, s1c, r0c, a0, j0, f0, length = jets
    if not (LD('.8')<H.value<3 and abs(v.value)<6 and LD('2.1')<=length.value<=LD('7.9')):
        raise ValueError("The declared original center or physical length box is violated.")
    if v.value == 0 or (a0-H*v*v/4).value == 0:
        raise ValueError("R620 requires the explicit v!=0 and beta_second!=0 center patch.")
    zero = H*0
    center_geometry = [H, zero, zero, zero, v]
    center_history = [p0c, zero, p2c, zero, zero, s1c, zero, r0c]
    geometry = [TimeJet2(H, zero, a0), TimeJet2(zero, v, zero),
                TimeJet2(zero, v/(2*H), zero), TimeJet2(zero, a0, zero),
                TimeJet2(v, zero, j0)]
    acceleration, curvature_acceleration = TimeJet2(a0, zero, f0), TimeJet2(zero, j0, zero)
    density = paid.density(geometry)
    history = [TimeJet2(value, rate.v, rate.d1) for value, rate in zip(center_history, density)]
    negative_geometry = [geometry[0], -geometry[1], -geometry[2], -geometry[3], geometry[4]]
    negative_history = [sign*value for sign, value in zip(original.JPAR, history)]
    evaluator = OriginalCoefficientTimeJets(coefficients)
    op = evaluator.evaluate(geometry, history)
    om = evaluator.evaluate(negative_geometry, negative_history)
    if not (op[1].value<0 and om[1].value<0 and op[2].value>0 and om[2].value>0):
        raise FloatingPointError("Original center Ch/Ck domain did not hold in actual arithmetic.")
    d = geometry[0]*geometry[2]-geometry[1]
    q = 1+d*d
    rates_plus = [(op[3+3*j]+acceleration*op[4+3*j]
                   +curvature_acceleration*op[5+3*j])/q**2 for j in range(3)]
    rates_minus = [-(om[3+3*j]+acceleration*om[4+3*j]
                    -curvature_acceleration*om[5+3*j])/q**2 for j in range(3)]
    rho_plus = [TimeJet2(zero, rate.v, rate.d1) for rate in rates_plus]
    rho_minus = [TimeJet2(zero, rate.v, rate.d1) for rate in rates_minus]
    center_g = [TimeJet2.constant(value) for value in center_geometry]
    center_a = [TimeJet2.constant(value) for value in center_history]
    wc = paid.weights(center_g)[0].v
    zeta0 = (op[0].v+op[1].v*a0)/(2*wc)
    potential_jets = OriginalPotentialTimeJets(potential)
    dependent = [TimeJet2.constant(zeta0), TimeJet2.constant(zero), TimeJet2.constant(zero)]
    base_plus = (op[0]+op[1]*acceleration+op[2]*curvature_acceleration
                 -4*paid.dot(paid.weights(geometry), rho_plus)
                 -4*potential_jets.center_difference(geometry, history, center_g, center_a)
                 -2*original.previous.center_pairing(geometry, center_g, dependent))
    base_minus = (om[0]+om[1]*acceleration-om[2]*curvature_acceleration
                  -4*paid.dot(paid.weights(negative_geometry), rho_minus)
                  -4*potential_jets.center_difference(negative_geometry, negative_history, center_g, center_a)
                  -2*original.previous.center_pairing(negative_geometry, center_g, dependent))
    height = geometry[0]
    beta = ((height-center_g[0])*(height+center_g[0])-center_g[0]**2*d*d)/(2*height)
    zeta1 = base_plus.d1/d.d1
    after_first = base_plus-d*TimeJet2.constant(zeta1)
    zeta2 = after_first.d2/beta.d2
    positive = after_first-beta*TimeJet2.constant(zeta2)
    negative = base_minus+d*TimeJet2.constant(zeta1)-beta*TimeJet2.constant(zeta2)
    gauge = [zeta0, zeta1, zeta2]
    initial = center_geometry+center_history+[zero]*6
    initial_value, initial_jacobian = paid.values_and_jacobian(initial)
    gauge_value, gauge_jacobian = paid.values_and_jacobian(gauge)
    residual_rows = [[float(getattr(row, lane).value) for lane in ("v", "d1", "d2")]
                     for row in (positive, negative)]
    receipt = {
        "parameter_order":["H", "v", "p0c", "p2c", "s1c", "r0c", "a0", "j0", "f0", "L"],
        "physical_parameters":np.asarray(parameters, float).tolist(),
        "actual_global_zeta":np.asarray(gauge_value, float).tolist(),
        "actual_center_d_first":float(d.d1.value),
        "actual_center_beta_second":float(beta.d2.value),
        "complete_R1":float((base_plus.d1-op[2].v*j0).value),
        "complete_R2":float((base_plus.d2-op[1].v*f0).value),
        "actual_triangular_diagonal":[float((op[1].v/(2*wc)).value),
                                      float((op[2].v/d.d1).value), float((op[1].v/beta.d2).value)],
        "original_plus_minus_center_time_two_jets":residual_rows,
        "parameter_derivative_dimension":dimension,
        "coefficient_time_parameter_evaluations":evaluator.evaluations,
        "coefficient_time_parameter_seconds":evaluator.seconds,
        "potential_time_jet_image_calls":potential_jets.image_calls,
        "potential_time_jet_pair_calls":potential_jets.pair_calls,
        "potential_time_jet_center_difference_calls":potential_jets.center_difference_calls,
        "full_M_rho_potential_and_mixed_parameter_time_chains":True,
        "old_identity_or_directional_gate_replayed":False,
        "floating_observations_are_not_strict_error_bounds":True,
        "seconds":time.monotonic()-started,
        "full_return_or_README_completion_claim":False}
    return {"parameters":parameters.copy(), "parameter_dimension":dimension,
            "center_geometry":center_geometry, "center_history":center_history,
            "global_gauge":gauge, "physical_length":length, "initial_jets":initial,
            "initial_value":initial_value, "initial_parameter_jacobian":initial_jacobian,
            "gauge_value":gauge_value, "gauge_parameter_jacobian":gauge_jacobian,
            "ruling_time_jets":(positive, negative), "receipt":receipt}


class FullPhysicalFeedback:
    """Original nineteen physical states with the complete ten-parameter chain.

    Time is x=s/L. A future shooting/BVP must solve all eight terminal A and
    both terminal velocities. No independent history nodes are introduced.
    """
    def __init__(self, chart, coefficients, potential):
        reduced.require_public_science()
        self.chart, self.coefficients, self.potential = chart, coefficients, potential
        self.evaluations = self.derivative_evaluations = 0
        self.seconds = 0.

    @staticmethod
    def embed(value, dimension):
        derivative = np.zeros(dimension, dtype=LD)
        if dimension:
            if len(value.derivative)!=10:
                raise ValueError("The center chart must retain all ten parameter derivatives.")
            derivative[19:] = value.derivative
        return Jet(value.value, derivative)

    def evaluate(self, state, derivatives=False):
        reduced.require_public_science()
        started = time.monotonic()
        self.evaluations += 1
        self.derivative_evaluations += int(derivatives)
        try:
            state = np.asarray(state, dtype=LD)
            if state.shape!=(19,) or not np.all(np.isfinite(state)):
                raise ValueError("The original full state has nineteen finite physical coordinates.")
            if not (LD('.8')<state[0]<3 and abs(state[1])<2 and abs(state[2])<1
                    and np.max(np.abs(state[3:5]))<6):
                raise FloatingPointError("The actual full-feedback path left its original physical box.")
            dimension = 29 if derivatives else 0
            identity = np.eye(29, dtype=LD) if derivatives else None
            ys = [Jet(value, identity[i] if derivatives else np.zeros(0)) for i, value in enumerate(state)]
            center_g = [self.embed(value, dimension) for value in self.chart["center_geometry"]]
            center_a = [self.embed(value, dimension) for value in self.chart["center_history"]]
            gauge = [self.embed(value, dimension) for value in self.chart["global_gauge"]]
            length = self.embed(self.chart["physical_length"], dimension)
            geometry, history = ys[:5], ys[5:13]
            negative_g = [geometry[0], -geometry[1], -geometry[2], -geometry[3], geometry[4]]
            negative_a = [sign*value for sign, value in zip(original.JPAR, history)]
            op = self.coefficients.evaluate_jets(geometry, history)
            om = self.coefficients.evaluate_jets(negative_g, negative_a)
            hp, kp, hm, km = op[1], op[2], om[1], om[2]
            determinant = -hp*km-hm*kp
            if not (hp.value<0 and hm.value<0 and kp.value>0 and km.value>0 and determinant.value>0):
                raise FloatingPointError("The actual original Ch/Ck matrix left its proved domain.")
            plus = (op[0]-4*paid.dot(paid.weights(geometry), ys[13:16])
                    -4*self.potential.center_difference(geometry, history, center_g, center_a)
                    -2*original.previous.center_pairing(geometry, center_g, gauge))
            minus = (om[0]-4*paid.dot(paid.weights(negative_g), ys[16:19])
                     -4*self.potential.center_difference(negative_g, negative_a, center_g, center_a)
                     -2*original.previous.center_pairing(negative_g, center_g, gauge))
            acceleration = (km*plus+kp*minus)/determinant
            curvature_acceleration = (hm*plus-hp*minus)/determinant
            h, k, eta, gamma, upsilon = geometry
            q = 1+(h*eta-k)**2
            rows = [gamma, upsilon, upsilon/(2*h), acceleration, curvature_acceleration]
            rows.extend(paid.density(geometry))
            rows.extend((op[3+3*j]+acceleration*op[4+3*j]
                         +curvature_acceleration*op[5+3*j])/q**2 for j in range(3))
            rows.extend(-(om[3+3*j]+acceleration*om[4+3*j]
                          -curvature_acceleration*om[5+3*j])/q**2 for j in range(3))
            values, jacobian = paid.values_and_jacobian([length*value for value in rows])
            reconstructed = [plus+hp*acceleration+kp*curvature_acceleration,
                             minus+hm*acceleration-km*curvature_acceleration]
            return {"value":values,
                    "state_jacobian":jacobian[:, :19] if derivatives else None,
                    "parameter_jacobian":jacobian[:, 19:] if derivatives else None,
                    "physical_accelerations":[acceleration.value, curvature_acceleration.value],
                    "cached_original_ruling_reassembly":[value.value for value in reconstructed],
                    "reassembly_is_not_a_strict_error_certificate":True}
        finally:
            self.seconds += time.monotonic()-started

    @staticmethod
    def terminal_rows(state):
        reduced.require_public_science()
        state = np.asarray(state, dtype=LD)
        if state.shape!=(19,):
            raise ValueError("Terminal rows belong to the same nineteen-state physical path.")
        indices = [*range(5, 13), 3, 4]
        jacobian = np.zeros((10, 19), dtype=LD)
        jacobian[np.arange(10), indices] = 1
        return state[indices].copy(), jacobian

