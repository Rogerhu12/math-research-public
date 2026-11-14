#!/usr/bin/env python3
"""True fixed-physical-tau parameter sources on a complete real core.

The two parameter derivatives are analytic derivatives of the exact affine
R33 graph. The target curvature includes the full infinite primitive mean.
Positive real-r cells are closed exact common spline spans; symmetry covers
the other side. At the turn, the proved R58 Q,Qp,Qpp enclosure is used before
any square root is differentiated. This is a coefficient-domain certificate,
not a parameter derivative of a validated flow or a twist certificate.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import json
import math
from pathlib import Path
import time

import numpy as np
from flint import arb, acb, ctx

from fourfold_phase_beta_interval import (
    series_constant, series_array, series_real, array_derivative,
    series_derivative, vector_dot, primitive_fourier_budget,
    add_real_cauchy_error, ball_record,
)
from fourfold_phase_beta_bulk_interval import exact_arb, real_interval
from fourfold_phase_beta_parameter_derivative import ParameterDerivativeTarget
from fourfold_phase_beta_parameter_germ import provenance
from fourfold_phase_beta_affine import load_definition
from fourfold_mixed_jet_algebra import Jet


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    path = Path(path); raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == ".gz" else raw)


def save(path, document):
    path = Path(path); raw = (json.dumps(document, indent=2)+"\n").encode()
    if len(raw) > 1_000_000 and path.suffix != ".gz":
        raise ValueError("large report requires gzip")
    data = gzip.compress(raw, mtime=0) if path.suffix == ".gz" else raw
    if len(data) > 5_000_000:
        raise ValueError("split reports above 5MB")
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name+".writing"); tmp.write_bytes(data); tmp.replace(path)


def binary(value):
    return Fraction.from_float(float(value))


def exact_endpoint(value):
    value = arb(value)
    if value.rad() != 0:
        raise ValueError("exact Arb endpoint required")
    m, e = value.man_exp()
    return Fraction(int(m))*Fraction(2)**int(e)


def interval(row):
    return arb(float(row[0])).union(arb(float(row[1])))


def absup(value):
    return abs(value).upper()


class ParameterSecondTarget(ParameterDerivativeTarget):
    """True first and second p derivatives, at fixed physical r."""

    def parameter_input_budget2(self, center, radial_radius, sigma, E_radius):
        base, first = self.parameter_input_budget(center, radial_radius, sigma, E_radius)
        v = first["beta_direction_bound"]+first["gamma_direction_bound"]
        effective = (2*first["true_radius_direction_bound"]*v
                     +base["radius_bound"]*v*v).upper()
        errors, finite = primitive_fourier_budget(
            self.nodes, sigma, arb(0), radial_radius, effective, arb(0),
            base["tangent_bound"])
        gap = radial_radius-E_radius
        e, ep, epp = base["field_errors"][0]/gap, first["field_errors"][0]/gap, errors[0]/gap
        M, Mp, Mpp = base["finite_field_bounds"][0]/gap, first["finite_field_bounds"][0]/gap, finite[0]/gap
        # Epp = 2 <Xp.Xp + X.Xpp>. Each primitive bound is per Cartesian
        # component, hence the factor 6 includes 3 components and the 2.
        error = (6*(2*Mp*ep+ep*ep+M*epp+Mpp*e+e*epp)).upper()
        second = dict(radial_radius=radial_radius, E_radius=E_radius,
            sigma_normalized_x=sigma, radius_bound=effective, height_bound=arb(0),
            tangent_bound=base["tangent_bound"], field_errors=errors,
            finite_field_bounds=finite, E_error=error,
            E_full_bound=(6*((Mp+ep)**2+(M+e)*(Mpp+epp))).upper())
        return base, first, second

    def primitive_parameter2(self, center, direction):
        beta, gamma, a, Z = self.scalars(center, direction)
        bp, gp, ap, Zp = self.direction_scalars(center, direction)
        T, Tp, Tpp = (series_array((self.nodes, 3)) for _ in range(3))
        for k in range(self.nodes):
            b = sum((beta[j]*self.sines[j, k] for j in range(self.modes)), series_constant(0))
            g = sum((gamma[j]*self.sines[j, k] for j in range(self.modes)), series_constant(0))
            b1 = sum((bp[j]*self.sines[j, k] for j in range(self.modes)), series_constant(0))
            g1 = sum((gp[j]*self.sines[j, k] for j in range(self.modes)), series_constant(0))
            sb, cb, sg, cg = b.sin(), b.cos(), g.sin(), g.cos()
            T[k] = [-cg*sb, cg*cb, sg]
            Tp[k] = [sg*g1*sb-cg*cb*b1, -sg*g1*cb-cg*sb*b1, cg*g1]
            q, cross = b1*b1+g1*g1, 2*b1*g1
            Tpp[k] = [cg*sb*q+sg*cb*cross, -cg*cb*q+sg*sb*cross, -sg*g1*g1]
        P, Pp, Ppp = (self._primitive_operator(v) for v in (T, Tp, Tpp))
        F, Fp, Fpp = (series_array(P.shape) for _ in range(3))
        for key in np.ndindex(P.shape):
            F[key] = a*P[key]
            Fp[key] = ap*P[key]+a*Pp[key]
            Fpp[key] = 2*ap*Pp[key]+a*Ppp[key]
        F[0, 2] += Z; Fp[0, 2] += Zp
        return F, Fp, Fpp, a, ap

    def parameter_target2(self, center, scale, budgets):
        if acb(center).imag != 0:
            raise ValueError("real r and real p are required for the E projection")
        F, Fp, Fpp, a, ap = self.primitive_parameter2(center, -scale)
        X, Xp, Xpp = (array_derivative(v, -scale) for v in (F, Fp, Fpp))
        def pair(U, V):
            return sum((vector_dot(U[k], V[(-k) % self.nodes]) for k in range(self.nodes)), series_constant(0))
        finite = pair(X, X), 2*pair(X, Xp), 2*(pair(Xp, Xp)+pair(X, Xpp))
        E, Ep, Epp = (add_real_cauchy_error(series_real(v), budget["E_error"],
                         scale, budget["E_radius"]) for v, budget in zip(finite, budgets))
        if not a[0].real > 0 or not E[0].real > 0:
            raise ValueError("positive a,E not proved on this closed physical cell")
        ar, arr = series_derivative(a, -scale), series_derivative(a, -scale, 2)
        apr, appr = series_derivative(ap, -scale), series_derivative(ap, -scale, 2)
        Er, Epr, Eppr = (series_derivative(v, -scale) for v in (E, Ep, Epp))
        C = ar*Er-2*arr*E
        Cp = apr*Er+ar*Epr-2*appr*E-2*arr*Ep
        Cpp = 2*apr*Epr+ar*Eppr-4*appr*Ep-2*arr*Epp
        denominator = 2*a*E**2
        K = C/denominator
        logarithmic = ap/a+2*Ep/E
        logarithmic_p = -(ap/a)**2+2*Epp/E-2*(Ep/E)**2
        Kp = Cp/denominator-K*logarithmic
        Kpp = Cpp/denominator-2*Kp*logarithmic-K*(logarithmic**2+logarithmic_p)
        return dict(a=a, E=E, Ep=Ep, Epp=Epp, C=C, Cp=Cp, Cpp=Cpp,
                    K=K, Kp=Kp, Kpp=Kpp)


class NormJet(Jet):
    # Only third radial derivatives and two actual parameter derivatives
    # enter geometric D/M/W sources. Higher orders are not requested.
    nx = 3


def majorant_scalars(target, center, width):
    beta, gamma, a, height = target.scalars(center, 1)
    bp, gp, ap, hp = target.direction_scalars(center, 1)
    weights = [(4*(k+1)*width).cosh() for k in range(target.modes)]
    sine_weights = [(4*(k+1)*width).sinh() for k in range(target.modes)]
    def modes(v0, v1, angular=0):
        out = NormJet()
        for i in range(4):
            for j, values in enumerate((v0, v1)):
                out[i, j] = sum((absup(v[i])*weights[k]*(4*(k+1))**angular
                                 for k, v in enumerate(values)), arb(0)).upper()
        return out
    def scalar(v0, v1):
        out = NormJet()
        for i in range(4):
            out[i, 0], out[i, 1] = absup(v0[i]), absup(v1[i])
        return out
    B, G = modes(beta, bp), modes(gamma, gp)
    Bt, Gt = modes(beta, bp, 1), modes(gamma, gp, 1)
    A = scalar(a, ap)
    # Exact height primitive: X contains height_r, with full mixed jets.
    Zr = scalar(height.derivative(), hp.derivative())
    imaginary = (width+sum((absup(b[0])*w for b, w in zip(beta, sine_weights)), arb(0))
                 +sum((absup(g[0])*w for g, w in zip(gamma, sine_weights)), arb(0))).upper()
    increment = B+G; increment[0, 0] = 0
    T = increment.exp(lambda _: imaginary.exp().upper())
    Tr = T*(B.derivative()+G.derivative())
    Ttheta = T*(1+Bt+Gt)
    # Cartesian zero-mean periodic primitive has L-infinity operator norm
    # <= pi/2, on each complex horizontal line as well as the real circle.
    X = (A*T).derivative()*(arb.pi()/2)+Zr
    C = X*T
    return dict(D=C*Ttheta, M=C*Tr, W=C*C, radius=A,
                T=T, X=X, tangent_imaginary_bound=imaginary)


def composed_norm(value, rp, rpp):
    """Normalized p orders 0,1,2 of v(r(p),p), using |rp|,|rpp|."""
    return [arb(value[0, 0]).upper(),
            (value[0, 1]+rp*value[1, 0]).upper(),
            (value[0, 2]+rp*value[1, 1]+rp*rp*value[2, 0]+rpp*value[1, 0]/2).upper()]


def multiply(a, b):
    return [sum((a[j]*b[i-j] for j in range(i+1)), arb(0)).upper() for i in range(3)]


def quotient_norm(A, D, denominator, zeroth):
    out = [min((A[0]/denominator).upper(), zeroth)]
    for i in (1, 2):
        out.append(((A[i]+sum((out[j]*D[i-j] for j in range(i)), arb(0)))/denominator).upper())
    return out


def geometry_source_bounds(target, radial, width, root, tp, tpp, s, Q, Qp, Qpp,
                           nmin, drift0, wave0):
    if not Q > 0:
        raise ValueError("the deflated real curvature is not strictly positive")
    scalar = majorant_scalars(target, acb(radial), width)
    r1, r2 = absup(s*tp), absup(s*tpp)
    D, M, W = (composed_norm(scalar[name], r1, r2) for name in ("D", "M", "W"))
    radius = scalar["radius"][0, 0]
    Dmin = (nmin/(radius*radius)).lower()
    if not Dmin > 0:
        raise ValueError("R73 denominator was not preserved")
    drift = quotient_norm(M, D, Dmin, drift0)
    wave = quotient_norm(W, D, Dmin, wave0)
    square = [Q.sqrt().upper(),
              (absup(Qp)/(2*Q.sqrt().lower())).upper(),
              (absup(Qpp)/(4*Q.sqrt().lower())
               +absup(Qp)**2/(8*Q.lower()**(arb(3)/2))).upper()]
    # cos(tau) >= 0 on the actual physical sine branch.
    cosine = (1-s.lower()**2).sqrt().upper()
    inner = [drift[j]+cosine*v for j, v in enumerate(multiply(square, wave))]
    tjet = [root.upper(), absup(tp), absup(tpp)/2]
    field = [cosine*v for v in multiply(tjet, inner)]
    field = [v.upper() for v in field]
    if not all(v.is_finite() for v in field):
        raise ValueError("nonfinite physical parameter bound")
    return dict(physical_field_upper=ball_record(min(field[0], arb(5))),
        physical_field_parameter_first_upper=ball_record(field[1]),
        physical_field_parameter_second_upper=ball_record(2*field[2]),
        normalized_geometric_D_parameter_bounds=list(map(ball_record, D)),
        normalized_geometric_M_parameter_bounds=list(map(ball_record, M)),
        normalized_geometric_W_parameter_bounds=list(map(ball_record, W)),
        normalized_drift_parameter_bounds=list(map(ball_record, drift)),
        normalized_wave_parameter_bounds=list(map(ball_record, wave)),
        D_modulus_lower=ball_record(Dmin), radius_upper=ball_record(radius),
        cosine_upper=ball_record(cosine), tangent_imaginary_bound=ball_record(scalar["tangent_imaginary_bound"]))


def ordinary_cell(target, left, right, context):
    radial = real_interval(left, right)
    root, tp, tpp = context["root"], context["tp"], context["tpp"]
    s0 = context["s0"]
    slo = max(arb(0), (exact_arb(left)/root.upper()).lower())
    shi = min(exact_arb(s0), (exact_arb(right)/root.lower()).upper())
    if not slo <= shi:
        raise ValueError("empty actual fixed-time slice")
    s = slo.union(shi)
    denominator = 1-s*s
    if not denominator > 0:
        raise ValueError("ordinary normalized slice touches the root")
    R0, RE, sigma, scale = arb(".003"), arb(".0025"), arb(".32"), exact_arb(Fraction(1, 4096))
    budgets = target.parameter_input_budget2(radial, R0, sigma, RE)
    fields = target.parameter_target2(radial, scale, budgets)
    K, Kp, Kpp = fields["K"], fields["Kp"], fields["Kpp"]
    values = dict(K=K[0].real, Kr=(-K[1]/scale).real,
                  Krr=(2*K[2]/scale**2).real, Kp=Kp[0].real,
                  Krp=(-Kp[1]/scale).real, Kpp=Kpp[0].real)
    rp, rpp = s*tp, s*tpp
    total1 = values["Kp"]+rp*values["Kr"]
    total2 = (values["Kpp"]+2*rp*values["Krp"]+rp*rp*values["Krr"]+rpp*values["Kr"])
    Q, Qp, Qpp = -values["K"]/denominator, -total1/denominator, -total2/denominator
    if not Q > 0:
        raise ValueError("ordinary actual Q positivity not proved; refine this closed cell")
    result = geometry_source_bounds(target, radial, context["width"], root, tp, tpp, s,
        Q, Qp, Qpp, context["nmin"], context["drift0"], context["wave0"])
    result.update(exact_radial_interval=[str(left), str(right)], fixed_s_interval=ball_record(s),
        Q=ball_record(Q), Q_parameter_first=ball_record(Qp), Q_parameter_second=ball_record(Qpp),
        true_fixed_r_curvature_jets={name:ball_record(v) for name, v in values.items()},
        infinite_E_parameter_error_budgets=[ball_record(b["E_error"]) for b in budgets],
        minimum_a=ball_record(fields["a"][0].real.lower()), minimum_E=ball_record(fields["E"][0].real.lower()),
        method="true affine first/second scalar parameter derivatives; full infinite primitive and target; fixed-tau chain rule")
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__); base = Path("data/phase_ring_continuation")
    p.add_argument("--object", type=Path, default=base/"type_fixed_step02_d5_exact_affine_step5_object.json")
    p.add_argument("--local-root-jets", type=Path, default=base/"type_fixed_step02_d5_step5_local_parameter_root_jets_h5e7.json")
    p.add_argument("--global-root-jets", type=Path, default=base/"type_fixed_step02_d5_parameter_root_jets.json")
    p.add_argument("--strip-certificate", type=Path, default=base/"type_fixed_step02_d5_step5_small_parameter_modulus_1over56.json.gz")
    p.add_argument("--existence-inputs", type=Path, default=base/"type_fixed_step02_d5_step5_real_parameter_return_existence.json")
    p.add_argument("--half-width", type=Fraction, default=Fraction(1, 2000000))
    p.add_argument("--width", type=Fraction, default=Fraction(1, 56))
    p.add_argument("--quarter-nodes", type=int, default=256)
    p.add_argument("--bits", type=int, default=192); p.add_argument("--series-precision", type=int, default=7)
    p.add_argument("--indices", help="optional exact common-cell indices, without an all-core claim")
    p.add_argument("--max-depth", type=int, default=8); p.add_argument("--resume", action="store_true")
    p.add_argument("--out", type=Path, required=True); args = p.parse_args()
    ctx.prec, ctx.cap = args.bits, args.series_precision
    if ctx.cap < 6:
        raise ValueError("at least six radial coefficients needed for the curvature jets")
    started, cpu = time.monotonic(), time.process_time()
    definition, origin, direction, center = load_definition(args.object)
    local, global_jets, strip, existence = map(read, (
        args.local_root_jets, args.global_root_jets, args.strip_certificate, args.existence_inputs))
    origin_sha, direction_sha = sha(origin), sha(direction)
    for d in (local, global_jets):
        if not d.get("proved") or d["origin_inputs_sha256"] != origin_sha or d["frozen_direction_sha256"] != direction_sha:
            raise ValueError("actual moving-root jet family differs")
    if local["object_sha256"] != sha(args.object) or local["global_root_jets_sha256"] != sha(args.global_root_jets):
        raise ValueError("local moving-root identity differs")
    for d, sourcekey, source in ((local, "source_sha256", "fourfold_phase_local_parameter_root_jets.py"),
            (global_jets, "run_source_sha256", "fourfold_phase_parameter_root_jets.py")):
        if d[sourcekey] != sha(Path(__file__).with_name(source)):
            raise ValueError("moving-root executable source differs")
        for name, digest in d["dependency_sha256"].items():
            if sha(Path(__file__).with_name(name)) != digest:
                raise ValueError("moving-root dependency differs: "+name)
    if (not strip.get("proved_uniform_denominator_nonzero") or not strip["complete_radial_coverage"]
        or strip["status"] != "complete" or not all(r["passed"] for r in strip["cells"])
        or strip["target_center_object_sha256"] != sha(args.object)):
        raise ValueError("completed same-object R73 denominator required")
    if (not existence.get("proved") or existence["target_object_sha256"] != sha(args.object)
        or existence["strip_certificate_sha256"] != sha(args.strip_certificate)):
        raise ValueError("same-object R75 existence/continuity input required")
    parameter = center-args.half_width, center+args.half_width
    containers = [list(map(Fraction, local["exact_parameter_interval"])),
                  list(map(binary, global_jets["exact_parameter_interval"])),
                  list(map(binary, strip["exact_parameter_interval"])),
                  list(map(Fraction, existence["exact_parameter_interval"]))]
    if any(not lo <= parameter[0] < parameter[1] <= hi for lo, hi in containers):
        raise ValueError("requested true parameter tube leaves a proved predecessor")
    if not 0 < args.width <= Fraction(existence["physical_theta_strip"]):
        raise ValueError("requested angular strip is too wide")
    root, tp, tpp = map(interval, (local["root_interval"], local["root_parameter_first"], local["root_parameter_second"]))
    s0 = Fraction(999, 1000)
    if not binary(global_jets["fixed_s_interval"][0]) <= s0 < 1:
        raise ValueError("R58 endpoint range does not cover the selected split")
    nmin = exact_arb(min(binary(row["Nraw_modulus_lower"]) for row in strip["cells"]))
    drift0 = exact_arb(max(binary(row["drift_derivative_bounds"][0]) for row in strip["cells"]))
    wave0 = exact_arb(max(binary(row["wave_factor_derivative_bounds"][0]) for row in strip["cells"]))
    context = dict(root=root, tp=tp, tpp=tpp, s0=s0, width=exact_arb(args.width),
                   nmin=nmin, drift0=drift0, wave0=wave0)
    target = ParameterSecondTarget(args.object, args.half_width, args.quarter_nodes, args.quarter_nodes,
                                  arb(".003"), arb(".0025"), arb(".32"))
    cut = binary(local["root_interval"][1])*s0
    knots = {Fraction(0), cut}
    all_knots = set()
    for key, values in target.frozen.items():
        if key.endswith("_knots"):
            all_knots.update(binary(v) for v in values)
            all_knots.update(-binary(v) for v in values)
    knots.update(k for k in all_knots if 0 < k < cut)
    points = sorted(knots); cells = list(zip(points, points[1:]))
    requested = list(range(len(cells))) if args.indices is None else list(map(int, args.indices.split(",")))
    if requested != sorted(set(requested)) or any(i < 0 or i >= len(cells) for i in requested):
        raise ValueError("ordered unique valid common-cell indices required")
    family_identity = provenance(target, args.object)
    family_identity["germ_source_sha256"] = family_identity.pop("source_sha256")
    common = dict(kind="actual_fixed_tau_true_parameter_first_second_source_bounds",
        source_sha256=sha(__file__), object_sha256=sha(args.object), **family_identity,
        actual_source_sha256=sha(__file__), local_root_jets_sha256=sha(args.local_root_jets),
        global_root_jets_sha256=sha(args.global_root_jets), strip_certificate_sha256=sha(args.strip_certificate),
        existence_inputs_sha256=sha(args.existence_inputs), physical_theta_strip=str(args.width),
        requested_indices=requested, total_common_cells=len(cells),
        exact_positive_bulk_radial_cover=["0", str(cut)], fixed_s_turn_split=str(s0),
        bits=args.bits, series_precision=args.series_precision, quarter_nodes=args.quarter_nodes,
        actual_dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            "fourfold_phase_beta_parameter_derivative.py", "fourfold_mixed_jet_algebra.py",
            "fourfold_phase_beta_parameter_germ.py", "fourfold_phase_beta_interval.py",
            "fourfold_phase_beta_bulk_interval.py")})
    # The inherited germ source and this executable are recorded separately.
    report = dict(**common, complete=False, rows=[], attempts=[], completed_indices=[],
        root_interval=ball_record(root), root_parameter_first=ball_record(tp), root_parameter_second=ball_record(tpp),
        global_Nraw_modulus_lower=ball_record(nmin), global_drift_upper=ball_record(drift0),
        global_wave_upper=ball_record(wave0), limitations=[
            "Real tau and real actual affine parameter, complex theta only.",
            "The output metric g0(p) varies synchronously with the actual graph.",
            "This certifies coefficient sources, not a flow, parameter twist, KAM or PDE inverse."])
    if args.resume and args.out.exists():
        old = read(args.out)
        for key, value in common.items():
            if old.get(key) != value:
                raise ValueError("resume identity differs: "+key)
        report = old
    def checkpoint():
        report["elapsed_seconds"] = time.monotonic()-started
        report["cpu_seconds"] = time.process_time()-cpu
        save(args.out, report)
    checkpoint()
    def enclose(left, right, depth, index):
        try:
            target.set_cell(left, right)
            row = ordinary_cell(target, left, right, context)
            row.update(common_cell_index=index, subdivision_depth=depth, proved=True)
            return [row]
        except ValueError as error:
            report["attempts"].append(dict(common_cell_index=index, depth=depth,
                interval=[str(left), str(right)], error=str(error)))
            checkpoint()
            if depth >= args.max_depth:
                raise
            middle = (left+right)/2
            return enclose(left, middle, depth+1, index)+enclose(middle, right, depth+1, index)
    done = report["completed_indices"]
    if done != requested[:len(done)]:
        raise ValueError("completed common cells are not a requested prefix")
    for index in requested[len(done):]:
        left, right = cells[index]
        rows = enclose(left, right, 0, index)
        report["rows"].extend(rows); report["completed_indices"].append(index); checkpoint()
        if index % 8 == 0 or index == requested[-1]:
            print(json.dumps(dict(common_cell=index, completed=len(report["completed_indices"]),
                f_p=max(float(arb(r["physical_field_parameter_first_upper"]["upper"]).upper()) for r in rows),
                f_pp=max(float(arb(r["physical_field_parameter_second_upper"]["upper"]).upper()) for r in rows),
                elapsed=report["elapsed_seconds"])), flush=True)
    # One actual common root germ; all s in [s0,1] are handled at once.
    turn_left, turn_right = binary(local["root_interval"][0])*s0, binary(local["root_interval"][1])
    if any(turn_left < k < turn_right for k in all_knots):
        raise ValueError("the full parameter turn collar crosses a scalar knot")
    target.set_cell(turn_left, turn_right)
    turn = geometry_source_bounds(target, real_interval(turn_left, turn_right), context["width"],
        root, tp, tpp, exact_arb(s0).union(arb(1)),
        interval(global_jets["Q"]), interval(global_jets["Q_parameter_first"]),
        interval(global_jets["Q_parameter_second"]), nmin, drift0, wave0)
    turn.update(exact_radial_envelope=[str(turn_left), str(turn_right)], fixed_s_interval=[str(s0), "1"],
                Q_source="complete R58 s-dependent endpoint quotient; derivatives taken before square root",
                global_root_jets_sha256=sha(args.global_root_jets), proved=True)
    report["turn"] = turn
    complete = requested == list(range(len(cells)))
    report["complete"] = True; report["complete_real_core_parameter_source_proved"] = complete
    fields = report["rows"]+[turn]
    report["global_bounds"] = {key:ball_record(max(arb(row[key]["upper"]).upper() for row in fields))
        for key in ("physical_field_upper", "physical_field_parameter_first_upper",
                    "physical_field_parameter_second_upper")}
    report["negative_half_and_both_branch_signs_included_by_exact_reflection"] = complete
    report["all_closed_bulk_cells_exactly_covered"] = complete
    checkpoint()
    print(json.dumps(dict(complete=True, full_core=complete, rows=len(report["rows"]),
                          bounds=report["global_bounds"], sha256=sha(args.out))), flush=True)


if __name__ == "__main__":
    main()
