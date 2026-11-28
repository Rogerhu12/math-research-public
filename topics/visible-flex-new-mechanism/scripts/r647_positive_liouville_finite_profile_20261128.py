#!/usr/bin/env python3
"""Public-Actions-only finite inputs for R647's positive Liouville factor.

Every candidate uses the new rational pair (j,N)=(2,3),(3,5), with
s=11/5, eta^2=37/100 and B=3/100.  The same left-regular psi1 and
exact psi2/psi3 are used across all sigma candidates.  Core heights
are normalized before geometry is read.
All quadrature and sampled extrema here are exploratory, not certificates.
No flat-tail attachment or nonlinear finite-angle root is inferred.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import json
import os
import platform
import subprocess
import time
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path

import mpmath as mp


def emit(kind, **fields):
    print(json.dumps({"kind": kind, **fields}, sort_keys=True, allow_nan=False),
          flush=True)


def ratio(value):
    q = Fraction(value)
    return mp.mpf(q.numerator) / q.denominator


def main():
    if not (
        os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY", "").lower()
        == "rogerhu12/math-research-public"
        and os.environ.get("GITHUB_RUN_ID", "").isdigit()
    ):
        raise SystemExit("Scientific evaluation requires public math-research-public Actions.")

    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, default=50)
    parser.add_argument("--max-seconds", type=float, default=240)
    parser.add_argument("--eval-limit", type=int, default=100000)
    parser.add_argument("--grid-intervals", type=int, default=512)
    parser.add_argument("--core-height", default="1/2")
    args = parser.parse_args()
    if args.dps < 30 or args.grid_intervals < 32 or args.grid_intervals % 2:
        raise ValueError("Use at least 30 digits and an even geometry grid >=32.")
    mp.mp.dps = args.dps
    started = time.perf_counter()
    counts = {
        "reference_formula_evaluations": 0,
        "hyperu_actual_calls": 0,
        "candidate_formula_evaluations": 0,
        "physical_profile_formula_evaluations": 0,
        "quadrature_callback_calls": 0,
        "sample_jet_envelope_evaluations": 0,
        "port_formula_evaluations": 0,
    }
    completed_fractions = []

    def guard():
        if time.perf_counter() - started > args.max_seconds:
            raise RuntimeError("scientific wall budget reached; remaining candidates uncomputed")
        if counts["reference_formula_evaluations"] >= args.eval_limit:
            raise RuntimeError("actual reference-formula evaluation budget reached")

    def num(value):
        if not mp.isfinite(value):
            raise ArithmeticError("nonfinite actual scalar")
        return mp.nstr(value, args.dps)

    s = mp.mpf(11) / 5
    eta = mp.sqrt(37) / 10
    bm = mp.mpf(3) / 100
    beta = mp.sqrt(eta * eta + bm)
    ua = beta - s / 2 + mp.mpf("0.5")
    ub = 1 + 2 * beta
    alpha2 = s - mp.mpf("1.5")
    alpha3 = (3 * s - 5) / 2
    disc = mp.sqrt(1 - 4 * bm / (s*s))
    t_left, t_right = (1 + disc) / 2, (1 - disc) / 2
    xl, xr = -mp.log(t_left), -mp.log(t_right)
    height_target = ratio(args.core_height)
    if height_target <= 0:
        raise ValueError("positive finite core height required")
    buffer = mp.mpf("0.25")
    cut_l, cut_r = xl - buffer, xr + buffer
    ref_l, ref_r = -mp.log(16), 20 * mp.log(2)
    kernel_nodes = [-mp.log((6+mp.sqrt(10))/22), -mp.log(mp.mpf(3)/11),
                    -mp.log((6-mp.sqrt(10))/22)]

    @functools.lru_cache(maxsize=100000)
    def reference(x):
        guard()
        counts["reference_formula_evaluations"] += 1
        t = mp.exp(-x)
        z = 2 * s * t
        counts["hyperu_actual_calls"] += 1
        u0 = mp.hyperu(ua, ub, z)
        counts["hyperu_actual_calls"] += 1
        u1 = mp.hyperu(ua + 1, ub + 1, z)
        psi = mp.exp(-z / 2) * z**beta * u0
        u = z / 2 - beta + ua * z * u1 / u0
        pref2 = t**alpha2 * mp.exp(-2 * s * t)
        poly2 = 2*s-2-4*s*t
        psi2 = pref2 * poly2
        psi2x = pref2 * ((-alpha2+2*s*t)*poly2+4*s*t)
        pref3 = t**alpha3 * mp.exp(-3 * s * t)
        z3 = 6*s*t
        poly3 = (z3*z3-2*(3*s-3)*z3+(3*s-4)*(3*s-3))/2
        psi3 = pref3 * poly3
        psi3x = pref3 * ((-alpha3+3*s*t)*poly3-z3*(z3-(3*s-3)))
        rho = s*s * (t - t * t) - bm
        return psi, u, psi2, psi2x, psi3, psi3x, rho

    def quadrature(function, points):
        def callback(x):
            guard()
            counts["quadrature_callback_calls"] += 1
            return function(x)
        value, error = mp.quad(callback, points, method="gauss-legendre",
                               error=True, maxdegree=8)
        return value, error

    try:
        head = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
        emit("provenance", utc=datetime.now(timezone.utc).isoformat(), git_head=head,
             source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             python=platform.python_version(), mpmath=mp.__version__, dps=args.dps,
             github_run_id=os.environ["GITHUB_RUN_ID"], certified=False,
             max_seconds=args.max_seconds, eval_limit=args.eval_limit,
             previous_run_preserved=46121291838,
             scope="New excited rational Morse pair and positive sigma; no old Morse/Cauchy scan replay.")

        psi_r, u_r, *_ = reference(xr)
        _, _, psi2_0, _, psi3_0, _, _ = reference(mp.mpf(0))
        a_max = min(eta, u_r)
        emit("fixed_morse_data", s="11/5", eta_squared="37/100", B_M_exact="3/100",
             kernel_levels=[[2,3],[3,5]], eta=num(eta), B_M=num(bm), beta_M=num(beta),
             X_L=num(xl), X_R=num(xr), psi1_R=num(psi_r), u_R=num(u_r),
             sigma_log_slope_upper=num(a_max), core_height_target=num(height_target),
             finite_cuts=[num(cut_l), num(cut_r)],
             reference_port_cuts=[num(ref_l), num(ref_r)],
             reference_port_t_interval=["1/1048576", "16"],
             interlacing_kernel_nodes_X=[num(x) for x in kernel_nodes],
             exact_global_radial_lower="u+eta >= s*exp(-X)+(sqrt(37)-6)/10 > 0",
             mode_normalization="f2(X=0)=f3(X=0)=1; r(X_R)=1",
             actual_call_counts=dict(counts))

        for fraction_text in ("0", "1/2", "4/5", "19/20"):
            fraction = ratio(fraction_text)
            a_r = -eta + fraction * (eta + a_max)
            nu_r = u_r - a_r
            if not nu_r > 0 or not (-eta <= a_r < eta):
                raise ArithmeticError("inadmissible sigma slope; no candidate made")

            @functools.lru_cache(maxsize=100000)
            def base(x):
                guard()
                counts["candidate_formula_evaluations"] += 1
                psi, u, p2, p2x, p3, p3x, rho = reference(x)
                y = eta * (x - xr)
                # Pure exponential at the baseline avoids cancellation in cosh-sinh.
                if fraction == 0:
                    sigma = psi_r * mp.exp(-y)
                    a = -eta
                else:
                    positive = (1 + a_r / eta) * mp.exp(y)
                    negative = (1 - a_r / eta) * mp.exp(-y)
                    sigma = psi_r * (positive + negative) / 2
                    a = eta * (positive - negative) / (positive + negative)
                nu = u - a
                if nu <= 0:
                    raise ArithmeticError("nonpositive computed radial speed")
                radius = psi / sigma
                wronskian = sigma * psi * nu
                return (sigma, a, nu, radius, wronskian, psi, p2, p2x, p3, p3x, rho)

            raw_height, raw_height_error = quadrature(
                lambda x: base(x)[5]**2 * base(x)[2]**2, [xl, *kernel_nodes, xr])
            if raw_height <= 0:
                raise ArithmeticError("nonpositive core height integral")
            scale = height_target / raw_height
            sigma0 = base(mp.mpf(0))[0]
            f_scale, g_scale = sigma0 / psi2_0, sigma0 / psi3_0

            @functools.lru_cache(maxsize=100000)
            def profile(x):
                counts["physical_profile_formula_evaluations"] += 1
                sigma, a, nu, radius, wronskian, psi, p2, p2x, p3, p3x, rho = base(x)
                w = scale * wronskian
                f, g = f_scale * p2 / sigma, g_scale * p3 / sigma
                fx = f_scale * (p2x - a * p2) / sigma
                gx = g_scale * (p3x - a * p3) / sigma
                fr, gr = fx / (radius * nu), gx / (radius * nu)
                e = 1 + w*w
                kr = -scale * sigma*sigma * rho / (nu * e**mp.mpf("1.5"))
                kt = w / (radius * mp.sqrt(e))
                k_boundary = w * (
                    mp.mpf(9)/2 * fr*g/radius
                    - mp.mpf(4)/3 * f*gr/radius - 6*f*g/(radius*radius))
                return dict(r=radius, w=w, nu=nu, f=f, g=g, fr=fr, gr=gr,
                            k_r=kr, k_theta=kt, boundary_K=k_boundary,
                            sigma=sigma, sigma_X=a*sigma, psi1=psi,
                            psi1_X=(nu+a)*psi, r_X=radius*nu,
                            w_X=-scale*rho*sigma*psi, rho=rho)

            def port(x):
                counts["port_formula_evaluations"] += 1
                p = profile(x)
                j0 = (p["r"]*p["fr"]*p["gr"] - 9*p["fr"]*p["g"]
                      - 4*p["f"]*p["gr"] + 12*p["f"]*p["g"]/p["r"])/2
                return -j0 * p["nu"] / (p["w"] * p["r"])

            geometry = []
            for label, left, right in (("negative_component", xl, xr),
                                       ("with_quarter_buffers", cut_l, cut_r)):
                sampled = []
                for index in range(args.grid_intervals + 1):
                    guard()
                    counts["sample_jet_envelope_evaluations"] += 1
                    x = left + (right-left) * index / args.grid_intervals
                    p = profile(x)
                    angular = 2*abs(p["f"])+3*abs(p["g"])
                    radial = abs(p["fr"])+abs(p["gr"])
                    e = 1+p["w"]**2
                    q_den = abs(p["fr"]-4*e*p["f"]/p["r"])
                    q_den += abs(p["gr"]-9*e*p["g"]/p["r"])
                    q_q = p["w"]/(2*q_den) if q_den else mp.inf
                    quad_den = radial**2+e*(angular/p["r"])**2
                    q_d = (mp.mpf("0.5") / (p["w"]*radial
                           + mp.sqrt((p["w"]*radial)**2+mp.mpf("0.5")*quad_den))
                           if quad_den else mp.inf)
                    sampled.append((x, p, min(q_q, q_d)))
                height = height_target
                error = raw_height_error * scale
                if label != "negative_component":
                    lh, le = quadrature(lambda x: base(x)[5]**2*base(x)[2]**2,
                                        [left, xl])
                    rh, re = quadrature(lambda x: base(x)[5]**2*base(x)[2]**2,
                                        [xr, right])
                    height += scale*(lh+rh)
                    error += scale*(le+re)
                left_state, right_state = profile(left), profile(right)
                diameter_bound = mp.sqrt((2*right_state["r"])**2+height**2)

                def extrema(rows):
                    kr_row = max(rows, key=lambda row: abs(row[1]["k_r"]))
                    kt_row = max(rows, key=lambda row: abs(row[1]["k_theta"]))
                    q_row = min(rows, key=lambda row: row[2])
                    return {
                        "max_abs_meridional_curvature": num(abs(kr_row[1]["k_r"])),
                        "max_abs_meridional_curvature_X": num(kr_row[0]),
                        "max_abs_azimuthal_curvature": num(abs(kt_row[1]["k_theta"])),
                        "max_abs_azimuthal_curvature_X": num(kt_row[0]),
                        "minimum_linear_jet_amplitude_envelope": num(q_row[2]),
                        "minimum_linear_jet_amplitude_X": num(q_row[0]),
                        "curvature_times_axisymmetric_diameter_upper": num(
                            max(abs(kr_row[1]["k_r"]), abs(kt_row[1]["k_theta"]))
                            * diameter_bound),
                    }

                geometry.append({
                    "region": label, "X_interval": [num(left), num(right)],
                    "r_interval": [num(left_state["r"]), num(right_state["r"])],
                    "radius_ratio": num(right_state["r"]/left_state["r"]),
                    "height": num(height), "height_quad_error_estimate": num(error),
                    "axisymmetric_diameter_upper": num(diameter_bound),
                    "sampled_fine": extrema(sampled), "sampled_coarse": extrema(sampled[::2]),
                    "sample_intervals": args.grid_intervals,
                    "end_data": [{"X": num(x), **{key: num(val) for key,val in profile(x).items()}}
                                 for x in (left, right)],
                    "qualification": "Sample extrema only; no continuous curvature/reach claim. "
                                     "Jet envelope pays sampled Q>=w/2 and D>=1/2 for h+qPhi only; "
                                     "it is not a nonlinear existence radius.",
                })

            knots = sorted(set([ref_l, cut_l, xl, *kernel_nodes, xr, cut_r, ref_r]))
            portions = []
            total = mp.mpf(0)
            total_error = mp.mpf(0)
            core = mp.mpf(0)
            for left, right in zip(knots[:-1], knots[1:]):
                value, error = quadrature(port, [left, right])
                total += value
                total_error += error
                if left >= cut_l and right <= cut_r:
                    core += value
                portions.append({"X_interval": [num(left), num(right)],
                                 "beta0_piece": num(value),
                                 "quadrature_error_estimate": num(error)})
            boundary = -(profile(cut_r)["boundary_K"]-profile(cut_l)["boundary_K"])/2
            port_output = {
                "beta0_truncated_reference": num(total),
                "quadrature_error_estimate": num(total_error),
                "beta0_finite_buffer_core_contribution": num(core),
                "beta_w2_finite_buffer_boundary_contribution": num(boundary),
                "beta_total_finite_buffer_core_contribution": num(core+boundary),
                "pieces": portions,
                "qualification": "Ordinary quadrature; omitted infinite tails not enclosed. "
                                 "Finite boundary term retained; no true-flat-tail port inferred. "
                                 "This is the new excited pair; no old R637 sign is transferred.",
            }
            completed_fractions.append(fraction_text)
            emit("candidate", fraction=fraction_text, a_R=num(a_r), nu_R=num(nu_r),
                 sigma_R=num(psi_r), lambda_height_scale=num(scale),
                 mode_scales=[num(f_scale), num(g_scale)],
                 raw_height_integral=num(raw_height), raw_height_error_estimate=num(raw_height_error),
                 geometry=geometry, port=port_output,
                 elapsed_seconds=time.perf_counter()-started,
                 actual_call_counts_cumulative=dict(counts),
                 finite_geometry_seed={"fraction": fraction_text,
                                       "core_height": args.core_height,
                                       "left_buffer_X_width": "1/4", "right_buffer_X_width": "1/4"},
                 actual_nonlinear_branch_solved=False, actual_flat_tail_attached=False)
            base.cache_clear()
            profile.cache_clear()

        emit("completed", completed_fractions=completed_fractions,
             elapsed_seconds=time.perf_counter()-started, actual_call_counts=dict(counts),
             certified=False, actual_nonlinear_branch_solved=False,
             README_completion_claim=False)
    except Exception as exc:
        emit("incomplete", reason=str(exc), error_type=type(exc).__name__,
             completed_fractions=completed_fractions,
             elapsed_seconds=time.perf_counter()-started,
             actual_call_counts=dict(counts), certified=False)
        raise


if __name__ == "__main__":
    main()
