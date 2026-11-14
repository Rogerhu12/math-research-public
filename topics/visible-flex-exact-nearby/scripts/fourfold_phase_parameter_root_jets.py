#!/usr/bin/env python3
"""Directed mixed jets of the exact R57 affine family and its moving root.

Normalized x orders 0..5 and parameter orders 0..2 are computed by a finite
nilpotent jet algebra. Direct interval DFT, infinite primitive tails, and every
mean-inner-product tail term are included. No finite-difference derivative is
used. This does not certify an ODE flow or an isometric solution.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from fourfold_interval_scalar import floor_float, ceiling_float, interval_exp
from fourfold_phase_root_interval import Box, stack, sum_box, interval_dot, sincos
from fourfold_phase_parameter_root_interval import make_affine_target
from fourfold_phase_uniform_tail import add_up, mul_up, exp_up, exact_iv, endpoint_up, weighted_sum_up
from fourfold_mixed_jet_algebra import Jet, exact_algebra_check


def box(value):
    return value if isinstance(value, Box) else Box(value)


def scalar_jet(spline, x, order=5):
    raw = spline.jets(x, order=order)
    result = Jet()
    for i in range(order+1):
        result[i, 0] = raw[i]/math.factorial(i)
    return result


def coefficient_map(value, operation):
    result = Jet()
    for i in range(6):
        for j in range(3):
            result[i, j] = operation(box(value[i, j]))
    return result


class AffineMixedTarget:
    def __init__(self, frozen, direction, parameter_interval, nodes=256):
        self.target = make_affine_target(frozen, direction, parameter_interval, nodes)
        self.frozen, self.direction = frozen, direction
        self.nodes, self.keep = nodes, nodes//2-1
        self.parameter = Box(*parameter_interval)
        self.alpha = []
        for a, w in zip(frozen["alpha"], direction["alpha_direction"]):
            entry = Jet.constant(Box(a)+self.parameter*w)
            entry[0, 1] = Box(w)
            self.alpha.append(entry)

    def one_side(self, x):
        base = scalar_jet(self.target.base, x)
        source = self.target.phase
        original = source.base.jets(x, order=5)
        variation = source.direction.jets(x, order=5)
        raw = [Jet(), Jet()]
        for i in range(6):
            for component in range(2):
                raw[component][i, 0] = (original[i, :, component]
                    +self.parameter*variation[i, :, component])/math.factorial(i)
                raw[component][i, 1] = variation[i, :, component]/math.factorial(i)
        beta, gamma = raw[0]*(base**3), raw[1]*(base**2)
        radius = base+scalar_jet(self.target.shift, x)
        for alpha, spline in zip(self.alpha, self.target.means):
            radius = radius+alpha*scalar_jet(spline, x)
        slope = scalar_jet(self.target.slopes[0], x, 4)
        for alpha, spline in zip(self.alpha, self.target.slopes[1:]):
            slope = slope+alpha*scalar_jet(spline, x, 4)
        return beta, gamma, radius, slope

    def scalars(self, x):
        plus, minus = self.one_side(x), self.one_side(-x)
        result = []
        for component, (p, m) in enumerate(zip(plus, minus)):
            value = Jet()
            parity = -1 if component == 1 else 1
            for i in range(6):
                for j in range(3):
                    value[i, j] = (p[i, j]+parity*(-1)**i*m[i, j])/2
            result.append(value)
        return result

    def tangent(self, beta, gamma):
        def angular(value):
            if value.lo.ndim == 0:
                return Box(np.zeros(self.nodes))+value
            return interval_dot(self.target.phase_sine, value.reshape(-1, 1)).reshape(self.nodes)
        b = coefficient_map(beta, angular)
        g = coefficient_map(gamma, angular)
        sb, cb = b.sincos(sincos)
        sg, cg = g.sincos(sincos)
        return -cg*sb, cg*cb, sg

    def primitive(self, tangent):
        result = Jet()
        n = 4*np.arange(1, self.keep+1)
        for i in range(6):
            for j in range(3):
                samples = stack([box(component[i, j]) for component in tangent], axis=-1)
                ss = interval_dot(self.target.sine, samples)*(Box(2)/self.nodes)
                cc = interval_dot(self.target.cosine, samples)*(Box(2)/self.nodes)
                aa, bb, zz = ss[:, 0], cc[:, 1], ss[:, 2]
                modes = stack([-(n*aa+bb)/(n*n-1), (aa+n*bb)/(n*n-1), -zz/n], axis=-1)
                average = sum_box(samples[:, 1])/self.nodes
                mean = stack([average, Box(0), Box(0)]).reshape(1, 3)
                result[i, j] = Box(np.concatenate([mean.lo, modes.lo]),
                                   np.concatenate([mean.hi, modes.hi]))
        return result

    def tail_errors(self, beta, gamma, radius):
        candidates = []
        for sigma, factors in self.target.tail_factors.items():
            weights = []
            for mode in 4*np.arange(1, self.target.modes+1):
                value = exact_iv(sigma)*int(mode)
                weights.append(endpoint_up((interval_exp(value)+interval_exp(-value))/2))
            def majorant(value):
                result = Jet()
                for i in range(6):
                    for j in range(3):
                        coefficient = box(value[i, j]).abs_upper()
                        bound = (float(weighted_sum_up(coefficient, weights)) if coefficient.ndim
                                 else float(coefficient))
                        result[i, j] = Box(0., bound)
                return result
            b, g = majorant(beta), majorant(gamma)
            exp_constant = lambda value: Box(0., exp_up(float(value.hi)))
            tangent_majorant = 2*(sigma+b+g).exp(exp_constant)+g.exp(exp_constant)
            primitive_error = tangent_majorant*Box(float(factors[0]))
            radius_majorant = coefficient_map(radius, lambda value: Box(0., value.abs_upper()))
            geometry_error = (radius_majorant*primitive_error).derivative()
            errors = np.array([[float(box(geometry_error[i, j]).hi) for j in range(3)]
                               for i in range(5)])
            candidates.append((float(errors.max()), sigma, errors))
        _, sigma, errors = min(candidates, key=lambda row:row[0])
        return sigma, errors

    def evaluate(self, x):
        beta, gamma, radius, slope = self.scalars(x)
        primitive = self.primitive(self.tangent(beta, gamma))
        fx = (radius*primitive).derivative()
        for i in range(5):
            for j in range(3):
                value = box(fx[i, j])
                lo, hi = value.lo.copy(), value.hi.copy()
                z = Box(lo[0, 2], hi[0, 2])+box(slope[i, j])
                lo[0, 2], hi[0, 2] = z.lo, z.hi
                fx[i, j] = Box(lo, hi)
        sigma, errors = self.tail_errors(beta, gamma, radius)
        norms = np.array([[float(sum_box(sum_box(Box(box(fx[i, j]).abs_upper()), axis=1), axis=0).hi)
                           for j in range(3)] for i in range(5)])
        weights = np.r_[1., np.full(self.keep, .5)][:, None]
        pair = lambda a, b: sum_box(sum_box(a*b*weights, axis=1), axis=0)
        E, corrections = Jet(), np.zeros((5, 3))
        for i in range(5):
            for j in range(3):
                value, pad = Box(0), 0.
                for k in range(i+1):
                    for ell in range(j+1):
                        r, s = i-k, j-ell
                        value = value+pair(box(fx[k, ell]), box(fx[r, s]))
                        correction = add_up(add_up(mul_up(norms[k, ell], errors[r, s]),
                                                    mul_up(norms[r, s], errors[k, ell])),
                                            mul_up(errors[k, ell], errors[r, s]))
                        pad = float(add_up(pad, correction))
                E[i, j] = value+Box(-pad, pad)
                corrections[i, j] = pad
        if float(box(radius[0, 0]).lo) <= 0 or float(box(E[0, 0]).lo) <= 0:
            raise ValueError("radius or mean E positivity not proved")
        C = radius.derivative()*E.derivative()-2*radius.derivative().derivative()*E
        K = C/(2*radius*E*E)
        def derivative(jet, i, j):
            return box(jet[i, j])*math.factorial(i)*math.factorial(j)
        C_names = dict(C=(0,0), Cx=(1,0), Cp=(0,1), Cxx=(2,0), Cxp=(1,1), Cpp=(0,2))
        K_names = dict(K=(0,0), Kx=(1,0), Kxx=(2,0), Kxxx=(3,0),
                       Kxp=(1,1), Kxxp=(2,1), Kxpp=(1,2))
        c = {name:derivative(C,*index) for name,index in C_names.items()}
        k = {name:derivative(K,*index) for name,index in K_names.items()}
        report = dict(radial_interval=x.pair(), a=box(radius[0,0]).pair(), E=box(E[0,0]).pair(),
                      C_derivatives={name:value.pair() for name,value in c.items()},
                      K_derivatives={name:value.pair() for name,value in k.items()},
                      tail_sigma=sigma, normalized_Fx_jet_tail_alias_upper=errors.tolist(),
                      normalized_E_jet_tail_corrections=corrections.tolist())
        return c, k, report


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", type=Path, required=True)
    parser.add_argument("--frozen-direction", type=Path, required=True)
    parser.add_argument("--root-certificate", type=Path, required=True)
    parser.add_argument("--parameter-radius", type=float, default=.01)
    parser.add_argument("--quarter-nodes", type=int, default=256)
    parser.add_argument("--s-minimum", type=float, default=.999)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    assert exact_algebra_check()
    with np.load(args.inputs, allow_pickle=False) as data:
        frozen = {key:data[key].copy() for key in data.files}
    with np.load(args.frozen_direction, allow_pickle=False) as data:
        direction = {key:data[key].copy() for key in data.files}
    root = json.loads(args.root_certificate.read_text())
    parameter = [-args.parameter_radius, args.parameter_radius]
    if not root["proved"] or root["exact_parameter_interval"] != parameter:
        raise ValueError("common-family root certificate/parameter mismatch")
    if root["origin_inputs_sha256"] != digest(args.inputs) or root["frozen_direction_sha256"] != digest(args.frozen_direction):
        raise ValueError("root certificate is for another affine family")
    target = AffineMixedTarget(frozen, direction, parameter, args.quarter_nodes)
    root_box = Box(*root["root_bracket"])
    collar = Box(*root["outward_binary_collar"])
    s = Box(args.s_minimum, 1.)
    whole_x = root_box*s
    if float(whole_x.lo) < float(collar.lo) or float(whole_x.hi) > float(collar.hi):
        raise ValueError("moving endpoint segment leaves the certified collar")
    c, _, root_report = target.evaluate(root_box)
    if float(c["Cx"].lo) <= 0:
        raise ValueError("implicit root derivative denominator not positive")
    t1 = -c["Cp"]/c["Cx"]
    t2 = -(c["Cpp"]+2*c["Cxp"]*t1+c["Cxx"]*t1*t1)/c["Cx"]
    _, k, collar_report = target.evaluate(collar)
    xi = s
    I0 = k["Kx"]
    I1 = k["Kxx"]*xi*t1+k["Kxp"]
    I2 = (k["Kxxx"]*xi*xi*t1*t1+2*k["Kxxp"]*xi*t1
          +k["Kxx"]*xi*t2+k["Kxpp"])
    Q = root_box*I0/(1+s)
    Q1 = (t1*I0+root_box*I1)/(1+s)
    Q2 = (t2*I0+2*t1*I1+root_box*I2)/(1+s)
    result = dict(kind="directed_actual_affine_root_and_fixed_s_quotient_parameter_jets",
                  proved=bool(float(Q.lo)>0), origin_inputs_sha256=digest(args.inputs),
                  frozen_direction_sha256=digest(args.frozen_direction),
                  common_root_certificate_sha256=digest(args.root_certificate),
                  run_source_sha256=digest(Path(__file__)),
                  dependency_sha256={name:digest(Path(__file__).with_name(name)) for name in
                    ("fourfold_mixed_jet_algebra.py", "fourfold_phase_parameter_root_interval.py",
                     "fourfold_phase_core_N_interval.py", "fourfold_phase_root_interval.py",
                     "fourfold_phase_uniform_tail.py", "fourfold_interval_scalar.py")},
                  exact_parameter_interval=parameter, quarter_nodes=args.quarter_nodes,
                  root_interval=root_box.pair(), common_collar=collar.pair(), fixed_s_interval=s.pair(),
                  root_parameter_first=t1.pair(), root_parameter_second=t2.pair(),
                  Q_definition="-K0(t(parameter)*s,parameter)/(1-s*s), continuous at s=1",
                  Q=Q.pair(), Q_parameter_first=Q1.pair(), Q_parameter_second=Q2.pair(),
                  root_evaluation=root_report, collar_evaluation=collar_report,
                  exact_algebra_all_18_coefficients_checked=True,
                  limitations=["exact affine family only; no rounded-checkpoint identification",
                    "fixed-s parameter derivatives include both moving-root derivatives",
                    "endpoint normalization only, not a whole ODE/return-map Taylor certificate",
                    "no exact PDE solution, cap, held, or reach conclusion"])
    args.out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key:result[key] for key in ("proved", "root_parameter_first", "root_parameter_second",
                                                "Q", "Q_parameter_first", "Q_parameter_second")}), flush=True)
    if not result["proved"]:
        raise SystemExit("endpoint quotient positivity not proved")


if __name__ == "__main__":
    main()
