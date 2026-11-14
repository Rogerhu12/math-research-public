#!/usr/bin/env python3
"""Define shared finite physical two-jets at one outer cell's ten nodes.

Uses the saved complete internal shooting states at original segment
boundaries and the true R26 radii. No Node, radial integration, or BVP.
The finite momentum root is only a binary candidate constructor. R48
will use these common physical two-jets in a new piecewise exact height.
At the actual outer cut all saved binary cutHeight entries are retained.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import resource
import time

from flint import arb, ctx
from closure_real_head_source_enclosure import exact_q, ball_record
from closure_real_head_green_enclosure import ball
from closure_real_outer_radius import OuterCell
from closure_split_joint_io import read, digest
from tail_r33_middle_ordered_physical import SourceValues
from tail_outer_weighted_compatible import intersection
from tail_outer_weighted_endpoint import finite_saved_endpoint
from tail_outer_finite_momentum_root import PureFiniteMomentumRoot
from tail_r41_connection_polynomial import fields, candidate_K, certify


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ("cell-manifest", "radius-ledger", "response", "ready", "out"):
        p.add_argument("--"+name, type=Path, required=True)
    p.add_argument("--tau", default="1/64")
    p.add_argument("--inverse-degree", type=int, default=8)
    p.add_argument("--rss-limit-mib", type=int, default=40)
    args = p.parse_args()
    if args.out.exists():
        raise FileExistsError("Use a fresh actual ten-node output")
    if digest(Path(__file__).with_name("tail_outer_saved_port_norms.py")) != "663e2f06db45ae701d6d04907231ad557d939951ec93db86f18a014ce2739e2e":
        raise ValueError("The finite-equation reference source changed")
    ctx.prec = 192
    began = time.monotonic()
    def memory_gate(stage):
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 1024*args.rss_limit_mib:
            raise MemoryError("The owned ten-node candidate exceeded its RSS cap at "+stage)
    paths = [args.cell_manifest, args.radius_ledger, args.response, args.ready]
    hashes = {str(path): digest(path) for path in paths}
    data, ledger, packet, ready = map(read, paths)
    memory_gate("inputs")
    if (not all(data["checks"].values()) or not ledger["complete_outer_radius"]
            or not packet["response"]["converged"]):
        raise ValueError("Complete actual real-source and successful finite input packages are required")
    for key in (str(args.radius_ledger), str(args.ready)):
        if hashes[key] not in data["original_metadata"]["input_hashes"].values():
            raise ValueError("The real moment/radius identity changed")
    if ledger["ready_sha256"] != hashes[str(args.ready)]:
        raise ValueError("The radius ledger uses another source")
    other_ready = packet["ready"]
    for key in ("frozenWarpAlpha", "exactSourceConstants"):
        if ready["rationalDeepModel"][key] != other_ready["rationalDeepModel"][key]:
            raise ValueError("The actual source differs at "+key)
    if ready["shallowSourceParameters"]["cells"] != other_ready["shallowSourceParameters"]["cells"]:
        raise ValueError("The complete 160-cell shallow table changed")
    geometric = ("rCut", "wCut", "width", "curvatureBound", "delta0", "R", "a",
        "orientation", "prefixR", "prefixEnd", "prefixReturnStart", "protectCell",
        "slopeCap", "capTransition", "capMode", "valleyControls", "pulseCaps",
        "valleyCaps", "warpWeightLevels", "rCuff", "oldCut", "epsilonScale", "prefixRByCell")
    for key in geometric:
        if (ready["rationalDeepModel"]["physicalParameters"].get(key) !=
                other_ready["rationalDeepModel"]["physicalParameters"].get(key)):
            raise ValueError("The physical source differs at "+key)
    cp = packet["response"]["checkpoint"]
    cfg = cp["parameters"]
    M, parts, spacing = cfg["modes"], cfg["shootingParts"], cfg["spacing"]
    stride = 9*parts
    if (M != 20 or cfg["physicalDepth"] != 12 or cfg["orientation"] != 1
            or cp["rawNode"] != [n*stride for n in range(13)]
            or len(cp["states"]) != 12*stride+1
            or cp["rawStates"] != [cp["states"][n] for n in cp["rawNode"]]
            or any(len(row) != 2*M for row in cp["states"])):
        raise ValueError("The full saved physical shooting grid is not the expected one")
    n = data["cell"]
    if not 0 <= n <= 11:
        raise ValueError("An actual outer cell is required")
    head = SourceValues(ready)
    head.params = ready["rationalDeepModel"]["physicalParameters"]
    cell = OuterCell(head, n)
    radius_row = next(row for row in ledger["cells"] if row["cell"] == n)
    widths = [ball(row["width"]) for row in radius_row["segments"]]
    if [row["segment"] for row in radius_row["segments"]] != list(range(9)):
        raise ValueError("All nine real segment widths are required")
    inner, outer = (ball(data["original_metadata"][key]) for key in ("inner_radius", "outer_radius"))
    prefix, suffix = [arb(0)], [arb(0)]*10
    for width in widths:
        prefix.append(prefix[-1]+width)
    for j in range(8, -1, -1):
        suffix[j] = suffix[j+1]+widths[j]
    radii = [intersection(inner+prefix[j], outer-suffix[j]) for j in range(10)]
    radii[0], radii[9] = inner, outer
    root = PureFiniteMomentumRoot(M, spacing, cfg["quadrature"], cfg["projectionFloor"])
    modes = [spacing*(j+1) for j in range(M)]
    tau = F(args.tau)
    if tau < 0:
        raise ValueError("The fixed outer strip cannot be negative")
    weights = {m: ((1+m)*(exact_q(tau)*m).exp()).upper() for m in modes}
    mu = head.eps_phys*(head.a*(head.d0*arb(2)**(-n)).log()).exp()
    rho = (head.a*head.log2).exp()
    rows, failure = [], None
    try:
        memory_gate("finite-Fourier-table")
        for point in range(10):
            j, x = (0, F(0)) if point == 0 else (point-1, F(1))
            segment, radius = cell.segments[j], radii[point]
            kind = cell.classify(segment, x, x)
            if kind is None:
                raise ArithmeticError("A real segment endpoint branch is unresolved")
            logw, ell = cell.profile(segment, exact_q(x), kind[0])
            w = logw.exp()
            rx = cell.integrand(segment, exact_q(x), kind[0], kind[1])
            if not w > 0 or not rx > 0:
                raise ArithmeticError("A real shared endpoint is not regular")
            index = n*stride+(9-point)*parts
            state = cp["states"][index]
            multiplier = rho if point == 9 else arb(1)
            Pi = [multiplier*exact_q(v) for v in state[M:]]
            if n == 0 and point == 9:
                H = [exact_q(v) for v in cp["cutHeight"]]
                Q = [h/radius**4 for h in H]
                convention = "Complete saved binary cutHeight at the exact real Rout"
            else:
                Q = [exact_q(v) for v in state[:M]]
                H = [radius**4*q for q in Q]
                convention = "The complete saved binary Q at this exact real source point"
            float_state = [float(q.mid()) for q in Q]+[float(v.mid()) for v in Pi]
            L, diagnostic = root.solve(float_state, radius=float(radius.mid()),
                                       w=float(w.mid()), mu=float(mu.mid()))
            jet = finite_saved_endpoint(Q, L, radius=radius, radius_x=rx, w=w,
                log_w_x=ell, spacing=spacing, tau=tau, inverse_degree=args.inverse_degree)
            R = sum((weights[m]*(abs(m*jet["H"][m]/(radius*w)).upper()+
                                  abs(jet["Hr"][m]/w).upper()) for m in modes), arb(0)).upper()
            P, G = fields(H, Pi, modes, radius, w, mu, cfg["orientation"])
            root_report = certify(P, G, w, tau, candidate_K(H, L, modes, radius, w))
            rows.append(dict(point=point, state_index=index, source_cell=n,
                source_segment=j, source_x=str(x), exact_height_convention=convention,
                saved_height_parameters=(cp["cutHeight"] if n == 0 and point == 9 else state[:M]),
                saved_momentum_parameters=state[M:], local_momentum_multiplier=ball_record(multiplier),
                radius=ball_record(radius), w=ball_record(w), wr=ball_record(w*ell/rx),
                radius_x=ball_record(rx), log_w_x=ball_record(ell), mu=ball_record(mu),
                candidate_L_orthonormal_cosine=L, finite_root_diagnostic=diagnostic,
                shared_physical_jets={name:{str(m):ball_record(value) for m,value in jet[name].items()}
                                      for name in ("H", "Hr", "Hrr")},
                finite_endpoint_definition=jet["report"], candidate_R_tau=ball_record(R),
                complete_connection_point_certificate=root_report))
            memory_gate("shared-endpoint")
            print(json.dumps(dict(event="true_segment_candidate_node", cell=n, point=point,
                state_index=index, R_tau=str(R), complete_connection_gate=root_report["full_connection_root_gate"],
                peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                seconds=time.monotonic()-began)), flush=True)
    except (ArithmeticError, ValueError, MemoryError) as error:
        failure = dict(type=type(error).__name__, message=str(error), completed_points=len(rows))
    result = dict(status="Shared finite two-jets at all ten true segment endpoints" if failure is None else
        "Incomplete ten-node candidate; actual failed gate retained", author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",
        cell=n, modes=modes, tau=str(tau), inverse_degree=args.inverse_degree, rows=rows, failure=failure,
        complete_original_segment_node_cover=len(rows)==10 and failure is None,
        saved_cut_height_exactly_preserved=n != 0 or (len(rows)==10 and failure is None),
        candidate_second_derivative_semantics="One specified finite endpoint physical jet, used identically by both adjacent R48 pieces; it is not an exact radial-solution derivative",
        finite_root_semantics="Binary candidate coefficients from the original finite angular equations with standard-library arithmetic; no projected-root or quadrature certificate is asserted",
        new_radial_flow=False, node_process_started=False, new_BVP=False,
        continuous_radial_defect_paid=False, true_radial_solution_claimed=False,
        input_hashes=hashes, source_hashes={name:digest(Path(__file__).with_name(name)) for name in (
            Path(__file__).name, "tail_outer_finite_momentum_root.py", "tail_outer_weighted_endpoint.py",
            "tail_outer_weighted_compatible.py", "tail_r41_connection_polynomial.py",
            "closure_real_outer_radius.py", "tail_r33_middle_ordered_physical.py")},
        finite_equations_reference_sha256="663e2f06db45ae701d6d04907231ad557d939951ec93db86f18a014ce2739e2e",
        elapsed_seconds=time.monotonic()-began,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    args.out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(dict(event="complete" if failure is None else "failed", output=str(args.out),
                          failure=failure, points=len(rows))), flush=True)
    if failure is not None:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
