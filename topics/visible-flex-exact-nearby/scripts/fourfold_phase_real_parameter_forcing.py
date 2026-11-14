#!/usr/bin/env python3
"""True f,fp,fpp at real fixed tau and arbitrary finite complex angles.

The reference is independent of the actual affine parameter. This module
therefore also supplies g0=(h*f-Yu)/q, g1=h*fp/q, g2=h*fpp/q at real time.
Every chosen Fourier mode and the true infinite primitive fee are kept.
There is no finite difference, time interpolation, or claim that finite
angle samples already prove a continuous integral or a nonzero twist.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
import time

import numpy as np
from flint import arb, acb, acb_series, ctx

from fourfold_phase_fixed_tau_parameter_bounds import (
    ParameterSecondTarget, sha, read, save, interval, binary, absup,
)
from fourfold_phase_beta_affine import load_definition
from fourfold_phase_beta_bulk_interval import exact_arb, complex_pad
from fourfold_phase_beta_interval import primitive_fourier_budget, series_derivative, ball_record
from fourfold_phase_field_time_turn_collar import PiTime
from fourfold_phase_unified_scalar_time_circle import exact_time, complex_record, UnifiedScalarTimeCircleField
from fourfold_phase_uniform_field_time_grid_fast import f_invariants
from fourfold_native_series_fft import NativeSeriesFFT
from fourfold_exact_fourier_multipoint import evaluate_fourier_batch
from fourfold_complete_reference_segment import CompleteReferenceSegment
from fourfold_retarget_reference_jets import RetargetReference


def exact_fraction(value):
    m, e = value.man_exp()
    return Fraction(int(m))*Fraction(2)**int(e)


def parameter_series(values):
    return acb_series(list(map(acb, values)), prec=3)


def normalized_total(value, derivative, second, scale, rp, rpp, radial_order=0):
    """Parameter orders 0,1,2 of the requested physical radial derivative."""
    base = series_derivative(value, -scale, radial_order)
    first = series_derivative(derivative, -scale, radial_order)
    second = series_derivative(second, -scale, radial_order)
    br = series_derivative(base, -scale)
    brr = series_derivative(base, -scale, 2)
    pr = series_derivative(first, -scale)
    return [base[0], first[0]+rp*br[0],
            (second[0]+2*rp*pr[0]+rp*rp*brr[0]+rpp*br[0])/2]


class CapturedTarget(ParameterSecondTarget):
    def primitive_parameter2(self, center, direction):
        values = super().primitive_parameter2(center, direction)
        self.last_primitive = values
        return values


class RealParameterFamily:
    """An exact real parameter tube around the saved delta5 object."""
    def __init__(self, object_path, point_root_path, local_root_jets_path,
                 global_root_jets_path, *, half_width=Fraction(1, 10**14),
                 nodes=512, physical_strip=Fraction(1, 56)):
        self.object_path, self.point_root_path = Path(object_path), Path(point_root_path)
        self.local_root_jets_path, self.global_root_jets_path = Path(local_root_jets_path), Path(global_root_jets_path)
        definition, origin, direction, center = load_definition(self.object_path)
        local, global_jets, point = map(read, (self.local_root_jets_path, self.global_root_jets_path, self.point_root_path))
        if (not local.get("proved") or not global_jets.get("proved") or not point.get("proved")
            or local["object_sha256"] != sha(self.object_path)
            or local["point_root_sha256"] != sha(self.point_root_path)
            or local["global_root_jets_sha256"] != sha(self.global_root_jets_path)
            or Fraction(point["exact_delta_fraction"]) != center):
            raise ValueError("exact parameter/root identities differ")
        for row in (local, global_jets, point):
            if row["origin_inputs_sha256"] != sha(origin) or row["frozen_direction_sha256"] != sha(direction):
                raise ValueError("actual root does not belong to the same affine family")
        lo, hi = map(Fraction, local["exact_parameter_interval"])
        half_width = Fraction(half_width)
        if not 0 < half_width or not lo <= center-half_width < center+half_width <= hi:
            raise ValueError("requested parameter interval leaves the certified root derivatives")
        if not 0 < physical_strip <= Fraction(1, 56):
            raise ValueError("this entry uses the completed physical-angle domain at width 1/56")
        self.half_width, self.center, self.nodes = half_width, center, nodes
        self.strip = Fraction(physical_strip)
        self.tp, self.tpp = interval(local["root_parameter_first"]), interval(local["root_parameter_second"])
        self.root = interval(point["root_interval"])+arb(0, (absup(self.tp)*exact_arb(half_width)).upper())
        self.global_Q = [interval(global_jets[k]) for k in ("Q", "Q_parameter_first", "Q_parameter_second")]
        self.target = CapturedTarget(self.object_path, half_width, nodes, nodes,
                                    arb(".003"), arb(".0025"), arb(".32"))
        self.target.fourier = NativeSeriesFFT()
        knots = set()
        for key, values in self.target.frozen.items():
            if key.endswith("_knots"):
                knots.update(binary(v) for v in values)
                knots.update(-binary(v) for v in values)
        points = sorted(knots); self.cells = list(zip(points, points[1:]))
        self.identity = dict(object_sha256=sha(self.object_path), point_root_sha256=sha(self.point_root_path),
            local_root_jets_sha256=sha(self.local_root_jets_path), global_root_jets_sha256=sha(self.global_root_jets_path),
            origin_inputs_sha256=sha(origin), direction_sha256=sha(direction), exact_center_parameter=str(center),
            exact_parameter_half_width=str(half_width),
            exact_parameter_interval=[str(center-half_width), str(center+half_width)], primitive_nodes=nodes,
            physical_theta_strip=str(self.strip), root=ball_record(self.root),
            root_parameter_first=ball_record(self.tp), root_parameter_second=ball_record(self.tpp),
            source_sha256=sha(__file__),
            dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
                "fourfold_phase_fixed_tau_parameter_bounds.py", "fourfold_native_series_fft.py",
                "fourfold_exact_fourier_multipoint.py", "fourfold_phase_beta_parameter_derivative.py",
                "fourfold_phase_beta_parameter_germ.py", "fourfold_phase_uniform_field_time_grid_fast.py")})

    def snapshot(self, tau, branch_sign=-1):
        return RealParameterSnapshot(self, tau, branch_sign)


class GermSnapshot:
    def __init__(self, family, tau, sign, cell, radial):
        started, cpu = time.monotonic(), time.process_time()
        self.family, self.cell, self.radial = family, cell, radial
        target = family.target; target.set_cell(*cell)
        self.scale = scale = exact_arb(Fraction(1, 4096))
        s, c = tau.ball().sin(), tau.ball().cos()
        s = s.intersection(arb(0).union(arb(1)))
        if not c > 0:
            raise ValueError("a nonendpoint real physical time must have positive cosine")
        self.s, self.cosine = s, c
        rp, rpp = s*family.tp, s*family.tpp
        R0, RE, sigma = arb(".003"), arb(".0025"), arb(".32")
        budgets = target.parameter_input_budget2(radial, R0, sigma, RE)
        data = target.parameter_target2(radial, scale, budgets)
        F, Fp, Fpp, a, ap = target.last_primitive
        coefficients = np.empty((family.nodes, 3, 3), object)
        for k in range(family.nodes):
            for component in range(3):
                coefficients[k, component] = normalized_total(F[k, component], Fp[k, component],
                    Fpp[k, component], scale, rp, rpp, radial_order=1)
        self.X_coefficients = coefficients
        self.beta, self.gamma, _, _ = target.scalars(acb(radial), -scale)
        self.bp, self.gp, _, _ = target.direction_scalars(acb(radial), -scale)
        zero = acb_series([0], prec=ctx.cap)
        self.phases = []
        for base, first in ((self.beta, self.bp), (self.gamma, self.gp)):
            self.phases.append([parameter_series(normalized_total(v, vp, zero, scale, rp, rpp))
                                for v, vp in zip(base, first)])
        for base, first in ((self.beta, self.bp), (self.gamma, self.gp)):
            self.phases.append([parameter_series(normalized_total(v, vp, zero, scale, rp, rpp, radial_order=1))
                                for v, vp in zip(base, first)])
        K, Kp, Kpp = data["K"], data["Kp"], data["Kpp"]
        total_K = normalized_total(K, Kp, Kpp, scale, rp, rpp)
        if c.lower() >= exact_arb(Fraction(1, 10000)) and (-total_K[0]).real > 0:
            self.wave = (-parameter_series(total_K)).sqrt()
            self.curvature_mode = "ordinary true K with the fixed-tau root chain rule"
        else:
            if not s.lower() >= exact_arb(Fraction(999, 1000)):
                raise ValueError("ordinary negative curvature failed outside the proved turn region")
            Q, Qp, Qpp = family.global_Q
            self.wave = c*parameter_series([Q, Qp, Qpp/2]).sqrt()
            self.curvature_mode = "R58 root-deflated Q,Qp,Qpp before square root"
        self.rtau = parameter_series([family.root*c, family.tp*c, family.tpp*c/2])
        self.sign = sign
        self.budgets, self.R0, self.sigma = budgets, R0, sigma
        self.rp, self.rpp = rp, rpp
        self.info = dict(actual_common_span=list(map(str, cell)), radial_interval=ball_record(radial),
            curvature_mode=self.curvature_mode, normalized_total_K=list(map(complex_record, total_K)),
            E_infinite_parameter_errors=[ball_record(b["E_error"]) for b in budgets],
            wall_seconds=time.monotonic()-started, cpu_seconds=time.process_time()-cpu)

    def sample(self, thetas):
        thetas = list(map(acb, thetas))
        width = max(abs(t.imag).upper() for t in thetas)
        if not width <= exact_arb(self.family.strip):
            raise ValueError("requested angle leaves the completed physical strip")
        errors = []
        for budget in self.budgets:
            err, _ = primitive_fourier_budget(self.family.nodes, self.sigma, 4*width, self.R0,
                budget["radius_bound"], budget["height_bound"], budget["tangent_bound"])
            errors.append(err[0])
        e0, e1, e2 = errors
        rp, rpp, R0 = absup(self.rp), absup(self.rpp), self.R0
        fees = [(e0/R0).upper(),
                (e1/R0+rp*2*e0/R0**2).upper(),
                ((e2/R0+2*rp*2*e1/R0**2+rp*rp*6*e0/R0**3+rpp*2*e0/R0**2)/2).upper()]
        values = np.empty((len(thetas), 3, 3), object)
        evaluations = []
        K = self.family.nodes//2-1
        for component in range(3):
            for order in range(3):
                row = [self.X_coefficients[k % self.family.nodes, component, order] for k in range(-K, K+1)]
                output, info = evaluate_fourier_batch(row, thetas, guard_bits=96)
                for j, value in enumerate(output):
                    values[j, component, order] = complex_pad(value, fees[order])
                evaluations.append(dict(component=component, normalized_parameter_order=order, **info))
        result = np.empty((len(thetas), 3), object)
        minimum_D = None
        for j, theta in enumerate(thetas):
            sine = [(4*(k+1)*theta).sin() for k in range(len(self.beta))]
            cosine = [(4*(k+1)*theta).cos() for k in range(len(self.beta))]
            phase = [sum((v*s for v, s in zip(row, sine)), parameter_series([0, 0, 0]))
                     for row in self.phases]
            phase.extend(sum((v*c*(4*(k+1)) for k, (v, c) in enumerate(zip(row, cosine))),
                             parameter_series([0, 0, 0])) for row in self.phases[:2])
            X = [parameter_series(values[j, component]) for component in range(3)]
            D, M, W = f_invariants(X, phase)
            if D[0].contains(0):
                raise ValueError("point enclosure of the actual D denominator contains zero")
            bound = abs(D[0]).lower()
            minimum_D = bound if minimum_D is None else min(minimum_D, bound)
            field = -self.rtau*(M+self.sign*self.wave*W)/D
            result[j] = [field[0], field[1], 2*field[2]]
            if not all(v.is_finite() for v in result[j]):
                raise ValueError("nonfinite true parameter value")
        return result, dict(full_infinite_X_normalized_parameter_fees=list(map(ball_record, fees)),
            full_finite_Laurent_evaluations=evaluations, minimum_point_D_modulus_lower=ball_record(minimum_D))


class RealParameterSnapshot:
    def __init__(self, family, tau, branch_sign=-1):
        if branch_sign not in (-1, 1):
            raise ValueError("branch sign must be +1 or -1")
        if isinstance(tau, (int, Fraction)):
            tau = PiTime(Fraction(tau))
        self.family, self.original_tau, self.branch_sign = family, exact_time(tau), branch_sign
        halfpi = PiTime(Fraction(0), Fraction(1, 2))
        if not (self.original_tau+halfpi).nonnegative() or not (halfpi-self.original_tau).nonnegative():
            raise ValueError("real time leaves the physical monotone sine branch")
        self.endpoint = (self.original_tau-halfpi).is_zero() or (self.original_tau+halfpi).is_zero()
        self.reflected = not self.original_tau.nonnegative()
        tau = -self.original_tau if self.reflected else self.original_tau
        self.tau = tau
        self.germs = []
        if self.endpoint:
            return
        radial = family.root*tau.ball().sin()
        lo, hi = exact_fraction(radial.lower()), exact_fraction(radial.upper())
        candidates = [(a, b) for a, b in family.cells if b > 0 and a <= hi and lo <= b]
        if not candidates or not candidates[0][0] <= lo <= hi <= candidates[-1][1]:
            raise ValueError("actual parameter radial image has incomplete common-germ coverage")
        sign = -branch_sign if self.reflected else branch_sign
        for cell in candidates:
            a, b = cell
            part = radial.intersection(exact_arb(a).union(exact_arb(b)))
            self.germs.append(GermSnapshot(family, tau, sign, cell, part))

    def sample(self, thetas):
        thetas = list(map(acb, thetas))
        if not thetas:
            raise ValueError("at least one exact angle ball required")
        if self.endpoint:
            values = np.empty((len(thetas), 3), object); values.fill(acb(0))
            return values, dict(exact_zero_at_actual_turn=True, time=self.original_tau.record())
        all_values, diagnostics = [], []
        for germ in self.germs:
            values, info = germ.sample(thetas); all_values.append(values)
            diagnostics.append(dict(**germ.info, evaluation=info))
        result = all_values[0].copy()
        for extra in all_values[1:]:
            for key in np.ndindex(result.shape):
                result[key] = acb(result[key].real.union(extra[key].real), result[key].imag.union(extra[key].imag))
        if self.reflected:
            result = -result
        return result, dict(time=self.original_tau.record(), branch_sign=self.branch_sign,
            exact_negative_tau_reflection=self.reflected, actual_germs=len(self.germs), germs=diagnostics,
            derivative_semantics="orders 0,1,2 are actual f,fp,fpp at fixed physical tau and theta; no factorial remains")

    def sample_uniform(self, angles, imaginary_theta=Fraction(0)):
        return self.sample([acb(arb.pi()*j/(2*angles), exact_arb(imaginary_theta)) for j in range(angles)])


def reference_parameter_forcing(family, reference, u, angles, label_width=Fraction(0)):
    """At one real time, including the full fixed finite reference exactly."""
    u = Fraction(u); width = Fraction(label_width)
    if not -1 <= u <= 1:
        raise ValueError("real normalized reference time must lie in [-1,1]")
    if (reference.identity["target_object_sha256"] != sha(family.object_path)
        or reference.identity["target_root_sha256"] != sha(family.point_root_path)
        or Fraction(reference.identity["target_exact_delta_fraction"]) != family.center):
        raise ValueError("the fixed reference and varied actual family have different centers")
    a, b = map(exact_time, reference.identity["exact_segment_time_rows"])
    a, b = a+(b-a)*reference.left, a+(b-a)*reference.right
    tau = (a+b)/2+(b-a)*u/2
    snapshot = family.snapshot(tau, reference.identity["branch_sign"])
    Y, Yu, q = reference.grid(acb(exact_arb(u)), angles, width)
    fields, details = snapshot.sample(Y)
    forcing = np.empty(fields.shape, object)
    for j in range(angles):
        if q[j].contains(0):
            raise ValueError("finite reference q enclosure contains zero")
        forcing[j] = [(reference.h*fields[j, 0]-Yu[j])/q[j],
                      reference.h*fields[j, 1]/q[j], reference.h*fields[j, 2]/q[j]]
    return fields, forcing, dict(fixed_reference_identity=reference.identity, physical_time=tau.record(),
        normalized_reference_time=str(u), initial_label_width=str(width), angle_nodes=angles,
        true_source=details, h_included_exactly_once=True,
        parameter_independent_reference=True,
        point_values_only_not_a_continuous_integral=True)


def main():
    p = argparse.ArgumentParser(description=__doc__); base = Path("data/phase_ring_continuation")
    p.add_argument("--object", type=Path, default=base/"type_fixed_step02_d5_exact_affine_step5_object.json")
    p.add_argument("--root", type=Path, default=base/"type_fixed_step02_d5_exact_affine_step5_root_tight.json")
    p.add_argument("--local-root-jets", type=Path, default=base/"type_fixed_step02_d5_step5_local_parameter_root_jets_h5e7.json")
    p.add_argument("--global-root-jets", type=Path, default=base/"type_fixed_step02_d5_parameter_root_jets.json")
    p.add_argument("--descriptor", type=Path, default=base/"step5_retargeted_reference/descriptor.json")
    p.add_argument("--domain419", type=Path, default=base/"step5_sharp_time_domain_R6_order40/forward_0419_r.json.gz")
    p.add_argument("--half-width", type=Fraction, default=Fraction(1, 10**14))
    p.add_argument("--primitive-nodes", type=int, default=512)
    p.add_argument("--angles", type=int, default=64); p.add_argument("--bits", type=int, default=256)
    p.add_argument("--label-width", type=Fraction, default=Fraction(1, 512))
    p.add_argument("--out", type=Path, required=True); args = p.parse_args()
    ctx.prec, ctx.cap = args.bits, 7
    wall, cpu = time.monotonic(), time.process_time()
    family = RealParameterFamily(args.object, args.root, args.local_root_jets, args.global_root_jets,
                                 half_width=args.half_width, nodes=args.primitive_nodes)
    ref = CompleteReferenceSegment(RetargetReference(args.descriptor), "forward", 419)
    report = dict(kind="true_real_time_parameter_forcing_interface_probe", complete=False,
                  source_sha256=sha(__file__), actual_family=family.identity, cases=[],
                  limitations=["Finite actual real-time angle values, not continuous time or label integrals.",
                               "No discrete angular average is declared to be the twist.",
                               "No complex-time parameter derivative domain is supplied by this real-time entry."])
    save(args.out, report)
    for u in (Fraction(-1, 2), Fraction(0), Fraction(1, 2)):
        fields, forcing, info = reference_parameter_forcing(family, ref, u, args.angles, args.label_width)
        row = dict(**info, true_fields=[[complex_record(z) for z in values] for values in fields],
                   actual_forcing=[[complex_record(z) for z in values] for values in forcing],
                   observed_discrete_forcing_mean=[complex_record(sum(forcing[:, k], acb(0))/args.angles) for k in range(3)])
        report["cases"].append(row); save(args.out, report)
        print(json.dumps(dict(u=str(u), maximum_fp=ball_record(max(absup(z) for z in fields[:, 1])),
                             maximum_fpp=ball_record(max(absup(z) for z in fields[:, 2])))), flush=True)
    # Independent f0 comparison against the already paid scalar native field,
    # on its own true uniform physical grid at the identical actual time.
    scalar = UnifiedScalarTimeCircleField(args.descriptor, args.domain419,
        nodes=args.primitive_nodes, root_nodes=1024)
    comparison_angles = max(args.angles, args.primitive_nodes)
    direct, _ = scalar.sample(arb(0), comparison_angles)
    snapshot = family.snapshot(scalar.exact_tau0, scalar.sign)
    values, info = snapshot.sample_uniform(comparison_angles)
    if not all(a.real.overlaps(b.real) and a.imag.overlaps(b.imag) for a, b in zip(values[:, 0], direct)):
        raise ValueError("independent true f0 scalar and parameter entry disagree")
    report["independent_uniform_f0_comparison"] = dict(all_nodes_overlap=True, nodes=comparison_angles,
                                                      time=scalar.exact_tau0.record(), details=info)
    for side in (-1, 1):
        endpoint, _ = family.snapshot(PiTime(Fraction(0), Fraction(side, 2)), -1).sample_uniform(4)
        if any(z != 0 for z in endpoint.flat):
            raise ValueError("exact turn zero identity failed")
    report.update(complete=True, actual_first_and_second_parameter_node_values_enclosed=True,
                  exact_both_turn_parameter_zeros_checked=True, elapsed_seconds=time.monotonic()-wall,
                  cpu_seconds=time.process_time()-cpu)
    save(args.out, report)
    print(json.dumps(dict(complete=True, sha256=sha(args.out), elapsed=report["elapsed_seconds"])), flush=True)


if __name__ == "__main__":
    main()
