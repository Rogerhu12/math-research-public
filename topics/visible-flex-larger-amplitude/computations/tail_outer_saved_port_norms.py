#!/usr/bin/env python3
"""Expose complete saved strong-tail states on the true real outer ports.

The fixed real metric comes from the completed R26 radius ledger and its
exact source formulas.  A small NumPy finite momentum root is evaluated
at each saved state; this is NOT a new BVP or a radial flow.  Its returned
binary L coefficients define a nearby finite polynomial two-jet candidate.
Arb then bounds that specified candidate's complete angular first norm.
No root, radial discretization, or unrepresented-mode error is declared0.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

import numpy as np
from flint import arb, ctx
from closure_real_head_source_enclosure import exact_q, ball_record
from closure_real_head_green_enclosure import load_json, ball
from closure_real_outer_radius import OuterCell
from tail_r33_middle_ordered_physical import SourceValues


class FiniteMomentumRoot:
    """Same finite angular-connection equations, with NumPy arithmetic."""
    def __init__(self, modes, spacing, quadrature, floor):
        self.M, self.N, self.floor = modes, quadrature, floor
        self.mode = spacing*np.arange(1, modes+1)
        theta = 2*np.pi*np.arange(quadrature)/quadrature
        self.cs = np.column_stack((np.ones(quadrature),
            np.sqrt(2)*np.cos(theta[:, None]*self.mode)))
        self.sn = np.sqrt(2)*np.sin(theta[:, None]*self.mode)

    def solve(self, state, *, radius, w, mu):
        M, N = self.M, self.N
        Q = np.asarray(state[:M], dtype=float)
        p = -self.mode*radius**3*Q/(np.sqrt(2)*w)
        pt = self.mode*p
        P, Pt = self.sn@p, self.cs[:, 1:]@pt
        E, w2 = 1+w*w, w*w
        target = np.r_[0., np.sqrt(12)*mu/(np.sqrt(2)*radius**4*w2)*
                       np.asarray(state[M:2*M])]

        def evaluate(L, jacobian):
            Lv = self.cs@L
            K = Lv-Pt
            T = 2*K+K*K+E*P*P
            u = w2*T
            D, S, A = 1-u, 1-w2*P*P, 1+Lv+w2*Pt
            if min(np.min(D), np.min(S), np.min(A)) <= self.floor:
                raise ArithmeticError("The actual finite momentum branch was rejected")
            sd = np.sqrt(D)
            fc = u*(2+sd)/(2*sd*(1+sd)**2)
            gc = w2*(P*P+S*T/(1+sd))/(S*sd)
            q = .5*(K*K+E*P*P)+K*Pt+T*fc+(1+K)*Pt*gc
            residual = L+self.cs.T@q/N-target
            scale = max(1e-300, np.max(np.abs(q)), np.max(np.abs(target)))
            B = None
            if jacobian:
                am = Lv+w2*Pt
                bm = am+(1+am)*np.expm1(-1.5*np.log1p(-u))
                B = np.eye(M+1)+self.cs.T@(bm[:, None]*self.cs)/N
            return residual, B, scale, (float(np.min(A)), float(np.min(D)),
                                       float(np.min(S)))
        L = target.copy()
        for iteration in range(30):
            residual, B, scale, minima = evaluate(L, True)
            error = float(np.max(np.abs(residual)))
            if error <= 8e-14*scale:
                return L, dict(iterations=iteration, relative_residual=error/scale,
                               sampled_minA=minima[0], sampled_minD=minima[1],
                               sampled_minS=minima[2])
            step = np.linalg.solve(B, residual)
            accepted = False
            for trial in range(20):
                candidate = L-2.**(-trial)*step
                try:
                    rr, _, _, _ = evaluate(candidate, False)
                except ArithmeticError:
                    continue
                if np.max(np.abs(rr)) < error:
                    L = candidate
                    accepted = True
                    break
            if not accepted:
                if error <= 5e-12*scale:
                    return L, dict(iterations=iteration, relative_residual=error/scale,
                        roundoff_fallback=True, sampled_minA=minima[0],
                        sampled_minD=minima[1], sampled_minS=minima[2])
                raise ArithmeticError("The saved-state finite root did not converge")
        raise ArithmeticError("The saved-state finite root reached its iteration limit")


def point_profile(cell, segment, fraction):
    x = exact_q(fraction)
    kind = cell.classify(segment, fraction, fraction)
    if kind is None:
        raise ArithmeticError("A saved port coincides with an undecided source branch")
    branch, sign = kind
    logw, logwx = cell.profile(segment, x, branch)
    drdx = cell.integrand(segment, x, branch, sign)
    if not drdx > 0:
        raise ArithmeticError("The true real radial coordinate is singular")
    w = logw.exp()
    return w, w*logwx/drdx, dict(branch=branch, log_w=ball_record(logw),
                               log_w_x=ball_record(logwx), dr_dx=ball_record(drdx))


def angular_candidate(Q, L, mode, radius, w):
    """Bounds only the explicitly specified real-port candidate."""
    p, k = [], []
    for j, m in enumerate(mode):
        q = exact_q(float(Q[j]))
        p.append((abs(m*radius**3*q/w)).upper())
        k.append((abs(arb(2).sqrt()*exact_q(float(L[j+1]))+
                      m*m*radius**3*q/w)).upper())
    def norm(tau):
        tau = exact_q(tau)
        return sum(((1+int(m))*(tau*int(m)).exp()*(p[j]+k[j])
                    for j, m in enumerate(mode)), arb(0)).upper()
    r0, r1 = norm(Fraction(0)), norm(Fraction(1, 64))
    accepted = Fraction(0)
    if r0 < arb(1)/64:
        lower, upper = Fraction(0), Fraction(2)
        if norm(upper) < arb(1)/64:
            lower = upper
        else:
            for unused in range(32):
                mid = (lower+upper)/2
                if norm(mid) < arb(1)/64:
                    lower = mid
                else:
                    upper = mid
        accepted = lower
    K = abs(exact_q(float(L[0])))+sum(k, arb(0))
    P = sum(p, arb(0))
    E = 1+w*w
    leading_radius = sum((abs(arb(2).sqrt()*exact_q(float(L[j+1]))-
        w*int(m)**2*radius**3*exact_q(float(Q[j])))
        for j, m in enumerate(mode)), arb(0))
    leading = (1+exact_q(float(L[0]))-leading_radius).lower()
    delta = (1-w*w*(2*K+K*K+E*P*P)).lower()
    S = (1-w*w*P*P).lower()
    return dict(R_tau0=ball_record(r0), R_tau_1_over64=ball_record(r1),
        R33_working_domain_at_tau0=bool(r0 < arb(1)/64),
        R33_mean_domain_at_tau0=bool(r0 < arb(1)/32),
        proved_candidate_tau_to_cap2=str(accepted),
        proved_candidate_R_at_tau=ball_record(norm(accepted)),
        all_angle_leading_lower=ball_record(leading),
        all_angle_D_lower=ball_record(delta), all_angle_S_lower=ball_record(S),
        nonmean_P_sine_abs=[ball_record(v) for v in p],
        nonmean_K_cosine_abs=[ball_record(v) for v in k])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("response", "radius-ledger", "ready-reference", "source-topic", "out"):
        parser.add_argument("--"+name, type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = 192
    started = time.monotonic()
    packet, raw = load_json(args.response)
    radius_data, rraw = load_json(args.radius_ledger)
    old_ready, oraw = load_json(args.ready_reference)
    ready = packet["ready"]
    if not packet["response"]["converged"] or radius_data["status"] != "complete":
        raise ValueError("A completed actual response and completed true radius ledger are required")
    if hashlib.sha256(oraw).hexdigest() != radius_data["ready_sha256"]:
        raise ValueError("The radius ledger belongs to another source")
    for key in ("physicalParameters", "frozenWarpAlpha", "exactSourceConstants"):
        # Solver/runtime fields in physicalParameters have no geometric role.
        if key != "physicalParameters" and ready["rationalDeepModel"][key] != old_ready["rationalDeepModel"][key]:
            raise ValueError("The actual real model differs")
    if ready["shallowSourceParameters"]["cells"] != old_ready["shallowSourceParameters"]["cells"]:
        raise ValueError("The160 true shallow calibration parameters differ")
    head = SourceValues(ready)
    head.params = ready["rationalDeepModel"]["physicalParameters"]
    geometric = ["rCut", "wCut", "width", "curvatureBound", "delta0", "R",
        "a", "orientation", "prefixR", "prefixEnd", "prefixReturnStart",
        "protectCell", "slopeCap", "capTransition", "capMode", "valleyControls",
        "pulseCaps", "valleyCaps", "warpWeightLevels", "rCuff", "oldCut",
        "epsilonScale", "prefixRByCell"]
    for key in geometric:
        if head.params.get(key) != old_ready["rationalDeepModel"]["physicalParameters"].get(key):
            raise ValueError("The captured real geometry differs at "+key)
    radii = {12: ball(radius_data["node12"])}
    widths = {r["cell"]: ball(r["width"]) for r in radius_data["cells"]}
    for n in range(11, -1, -1):
        radii[n] = radii[n+1]+widths[n]
    checkpoint = packet["response"]["checkpoint"]
    cfg = checkpoint["parameters"]
    if cfg["physicalDepth"] != 12 or len(checkpoint["rawStates"]) != 13:
        raise ValueError("This real-source comparison requires all13 outer ports")
    root = FiniteMomentumRoot(cfg["modes"], cfg["spacing"], cfg["quadrature"],
                              cfg["projectionFloor"])
    rho = (head.a*head.log2).exp()
    rows = []
    for node in range(13):
        n = max(0, node-1)
        cell = OuterCell(head, n)
        j, x = (8, Fraction(1)) if node == 0 else (0, Fraction(0))
        w, wr, source = point_profile(cell, cell.segments[j], x)
        mu = head.eps_phys*(head.a*(head.d0*arb(2)**-n).log()).exp()
        state = list(checkpoint["rawStates"][node])
        if node == 0:
            state[root.M:] = [float(rho.mid())*v for v in state[root.M:]]
        L, diagnostic = root.solve(state, radius=float(radii[node].mid()),
                                  w=float(w.mid()), mu=float(mu.mid()))
        candidate = angular_candidate(state[:root.M], L, root.mode, radii[node], w)
        row = dict(physical_node=node, source_cell=n, source_segment=j,
            source_x=str(x), radius=ball_record(radii[node]), w=ball_record(w),
            wr=ball_record(wr), mu=ball_record(mu), geometry=source,
            finite_root=diagnostic, candidate_L_orthonormal_cosine=L.tolist(),
            candidate=candidate)
        if node == 0:
            saved = packet["response"]["jets"]
            h = float(radii[node].mid())**4*np.asarray(state[:root.M])
            slope = np.sqrt(2)*float(w.mid())*L[1:]+root.mode**2*float(radii[node].mid())**3*np.asarray(state[:root.M])
            row["comparison_to_saved_cut"] = dict(
                height_l1=float(np.sum(np.abs(h-np.asarray(saved["height"])))),
                slope_l1=float(np.sum(np.abs(slope-np.asarray(saved["slope"])))),
                mean_slope_correction=float(w.mid())*float(L[0])-saved["meanSlopeCorrection"],
                radius_midpoint_minus_saved=float(radii[node].mid())-saved["radius"])
        rows.append(row)
    result = dict(status="Complete13 saved ports evaluated on the true real metric; angular certificates concern the explicit candidate only",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)", rows=rows,
        actual_finite_response_residual=packet["response"]["residual"],
        actual_modes=cfg["modes"], all_modes_of_saved_response_retained=True,
        new_radial_flow_or_BVP=False, node_process_started=False,
        exact_real_source_used=True,
        finite_root_arithmetic="NumPy evaluation of the same finite angular-connection equations. Operation ordering differs from the source JavaScript; the root is a floating diagnostic, not a root enclosure.",
        candidate_definition="Saved binary Q and newly returned binary L define finite angular fields at the rigorous real r,w port. All R, leading,D,S intervals bound this candidate on every real angle.",
        scope_limits=["No interval enclosure of the projected momentum root or its quadrature error is claimed.",
            "No radial interval between the13 ports is certified by this report.",
            "No exact solution is asserted to have no further Fourier modes.",
            "The complete mean root existence gate is only applicable when the stated R<=1/32 condition holds; it does not identify the saved finite mean."],
        input_hashes={str(args.response):hashlib.sha256(raw).hexdigest(),
            str(args.radius_ledger):hashlib.sha256(rraw).hexdigest(),
            str(args.ready_reference):hashlib.sha256(oraw).hexdigest()},
        source_hashes={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
            for name in [Path(__file__).name, "closure_real_outer_radius.py",
                         "closure_real_head_source_enclosure.py", "tail_r33_middle_ordered_physical.py"]},
        translated_root_source_sha256=hashlib.sha256((args.source_topic/"scripts/78718-tail-fourier-root-momentum.mjs").read_bytes()).hexdigest(),
        elapsed_seconds=time.monotonic()-started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    args.out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(dict(output=str(args.out), rows=[
        dict(node=r["physical_node"],R0=r["candidate"]["R_tau0"]["display"],
             tau=r["candidate"]["proved_candidate_tau_to_cap2"],
             leading=r["candidate"]["all_angle_leading_lower"]["display"])
        for r in rows], seconds=result["elapsed_seconds"],
        RSS_KiB=result["peak_RSS_KiB"])), flush=True)


if __name__ == "__main__":
    main()
