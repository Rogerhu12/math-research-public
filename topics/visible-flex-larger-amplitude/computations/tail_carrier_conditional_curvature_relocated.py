#!/usr/bin/env python3
"""Apply R95/R99 to the actual complete carrier, on every original leaf.

The reference here is the new carrier, not the original R48 candidate.
Its own actual Hrr, complete mean, all finite J coefficients and exact
same-leaf wJ/L are retained. A true same-g full-frequency field error is
an external hypothesis. The other seven R102 reference parts are unchanged.
Only exact rational arithmetic and local primary reads are performed.

Author: tail_refinement (original mathematics), geometry_audit (archive relocation), AI-assisted, 2026-11-13.
This is a fresh archive-relocated consumer, not the missing original output.
Only original absolute paths are resolved to identical SHA-checked archive files;
all source, physical and arithmetic gates and compute() remain unchanged.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

from tail_outer_legacy_schema_reader import digest, plain_read, dyadic, interval, directed

EXPECTED_SUMMARY = "0ac4b1e14ec34a86035add63e6250660924537c54acc834e497c6ebdd396ae12"
EXPECTED_RESOURCE = "dee1cef1a748f4459e00a5428dd4b6b1602c3eb442498091b29bd88e0ea1c865"
EXPECTED_BACKGROUND = "27e9cac085dd4913cdf14526fec847613bede8fae5367ae72cc143f25b254083"
EXPECTED_R102 = "d01b7310f9d76fa5d5d56f44805c67fedf7be776a78435803943edcda424bc6f"
READY = "notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json"


def upper(value):
    return directed(value, True, 96)


def lower(value):
    return directed(value, False, 96)


def absolute(value):
    return max(map(abs, interval(value)))


def compute(row, modes, eps):
    rlo, rhi = interval(row["source"]["radius"])
    wlo, w = interval(row["source"]["w"])
    if interval(row["source"]["radius_x"]) != (Q(1), Q(1)):
        raise ValueError("The actual carrier radial derivative is not physical r")
    if not (0 < wlo <= w <= Q(3, 25) and rlo > Q(1, 20)):
        raise ValueError("The paid real-background range is not satisfied on this leaf")
    z, E = w*w, 1+w*w
    rootE, target = 1+z/2, Q(33, 4)
    connection = 8*w*rootE
    wr = min(w*absolute(row["source"]["log_w_x"]), 8*E*rootE)
    bounds = {key: dyadic(value) for key, value in row["bounds_upper"].items()}
    if any(x < 0 for x in bounds.values()):
        raise ValueError("A recorded norm has become negative")
    c = bounds["complete_mean_abs"]
    jets = row["actual_nonmean_jet_cosine_intervals"]
    if any(len(jets[key]) != len(modes) for key in ("H", "Kbar", "Kbar_r")):
        raise ValueError("The complete saved nonmean field is absent")
    H = list(map(absolute, jets["H"]))
    K = list(map(absolute, jets["Kbar"]))
    k0 = c+sum(K, Q(0))
    p0 = sum((m*h for m, h in zip(modes, H)), Q(0))/(rlo*wlo)
    t0 = min(sum((m*m*h for m, h in zip(modes, H)), Q(0))/(rlo*wlo),
        bounds["P_theta_W1"]/3)
    u0 = min(sum((m*k for m, k in zip(modes, K)), Q(0))+p0,
        bounds["K_theta_minus_P_W1"]/3)
    d0, e0 = w*k0, w*p0
    A0 = bounds["signed_actual_nonmean_Hrr_l1"]+bounds["mean_physical_hrr_minus_background_abs"]+connection*d0
    B0, C0 = (w/rlo)*u0, (w/rlo)*(k0+t0)

    # Exact physical residual of this same candidate. R77 keeps the scalar
    # mean and the complete finite support through twice the height cutoff.
    J = list(map(absolute, row["full_J_cosine_intervals"]))
    Jperp = sum(J[1:], Q(0))
    Lmin = dyadic(row["gates_lower"]["real_L_lower"])
    Dmin = min(Q(1), dyadic(row["gates_lower"]["real_D_lower"]))
    multiplier = Q(3, 2)*E**2*bounds["full_D_nonconstant_W1"]/Dmin**3
    Jmean = min(J[0], multiplier*Jperp)
    Jfull = min(sum(J, Q(0)), bounds["complete_J_l1"], Jmean+Jperp)
    dH = w*Jfull/Lmin

    # R99 mean-root continuation box and its full four-field derivative.
    p, k, t, u = p0+eps/3, k0+4*eps/3, t0+eps, u0+4*eps/3
    vD = z*(2*k+k*k+E*p*p)
    a, d, l, y = 1-z*p*p, 1-vD, 1-k-E*t, 1-k
    if min(a, d, l, y) <= 0:
        raise ArithmeticError("The common real mean/root branch has no positive margin")
    orient = 1-z*(1+k)*t/a
    if orient <= 0:
        raise ArithmeticError("The complete mean numerator branch failed")
    CK = (k+E*t)/d**2+Q(3, 2)*vD/d**3
    CT = (k+z*p*p)/(a*d)+vD/(2*d**2)
    CP = E*p*(1+z*(1+k)*t/a)/d**2+2*z*p*(1+k)*t/(a*a*d)
    scale = E**2/l
    aK, aP, aT = scale*CK, scale*CP, scale*CT
    Cm = (aK+aP)/3+aT
    if Cm >= 1:
        raise ArithmeticError("The full mean root does not continue inside its stated epsilon box")
    ec, deltaK = Cm*eps, eps/3+Cm*eps
    N = wr*(1+z*((1+k)*t+p*p))+(E*w/rlo)*u*u
    FK = wr*z*t/l+N/l**2
    FU = 2*E*w*u/(rlo*l)
    FP = 2*wr*z*p/l+FU
    FT = wr*z*(1+k)/l+E*N/l**2
    phi = FK*deltaK+FP*eps/3+FT*eps+FU*eps
    dr, angular = w*deltaK, w*eps/3
    A = A0+phi+connection*dr+dH
    B = B0+(w/rlo)*4*eps/3
    C = C0+(w/rlo)*(eps+deltaK)
    omega = 2*w*(d0+dr)+(d0+dr)**2+E*(e0+angular)**2
    if omega >= 1:
        raise ArithmeticError("The true surface positive vertical projection margin failed")
    curvature = (8+rootE*(max(A, C)+B))/(1-omega)
    formal_omega = 2*w*d0+d0*d0+E*e0*e0
    formal = (8+rootE*(max(A0, C0)+B0))/(1-formal_omega)
    cap = (target*(1-omega)-8)/rootE-B-(A0+phi+connection*dr)
    matrix = [
        [w*(1+aK), w*aP, w*aT, Q(0)],
        [Q(0), rhi*w, Q(0), Q(0)],
        [FK*(1+aK), FP+FK*aP, FT+FK*aT, FU],
        [Q(0), Q(0), Q(0), w],
        [Q(0), Q(0), rhi*w, Q(0)],
    ]
    locator = {key: row[key] for key in ("part", "panel", "source_left", "source_right")}
    return dict(**locator, candidate_formal_curvature_upper=upper(formal),
        conditional_true_curvature_upper=upper(curvature),
        conditional_target_passed=curvature < target and dH < cap,
        same_leaf_actual_physical_dH_upper=upper(dH),
        available_dH_open_lower=lower(cap),
        complete_mean_difference_upper=upper(ec), mean_continuation_coefficient_upper=upper(Cm),
        real_domain_lowers={key: lower(value) for key, value in
            dict(A=a, D=d, L=l, y=y, N=orient).items()},
        true_vertical_normal_squared_lower=lower((1-omega)/E),
        actual_candidate_bounds={key: upper(value) for key, value in
            dict(p=p0, k=k0, t=t0, u=u0, radial_gradient=d0, angular_gradient=e0,
                A=A0, B=B0, C=C0, abs_w_r=wr).items()},
        five_physical_jet_positive_matrix=[[upper(v) for v in row] for row in matrix],
        hrr_additive_candidate_defect_upper=upper(dH)), curvature, formal, dH


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ("topic", "math-directory", "carrier-summary", "carrier-resource", "background", "r102-budget", "out"):
        ap.add_argument("--"+name, type=Path, required=True)
    ap.add_argument("--epsilon", default="1/512")
    ap.add_argument("--rss-limit-mib", type=int, default=96)
    args = ap.parse_args()
    if args.out.exists() or Q(args.epsilon) != Q(1, 512):
        raise ValueError("Use a fresh output for the stated common R102 epsilon")
    started = time.monotonic()
    eps = Q(args.epsilon)
    inputs = {}

    def check(path, expected):
        path = Path(path)
        if digest(path) != expected:
            raise ValueError("A formal mathematical input changed: " + str(path))
        inputs[str(path)] = expected

    for path, expected in ((args.carrier_summary, EXPECTED_SUMMARY), (args.carrier_resource, EXPECTED_RESOURCE),
            (args.background, EXPECTED_BACKGROUND), (args.r102_budget, EXPECTED_R102)):
        check(path, expected)
    summary, usage, background, old = map(plain_read,
        (args.carrier_summary, args.carrier_resource, args.background, args.r102_budget))
    if (usage["exitcode"] != 0 or usage["termination_signal"] is not None
            or not all(x is True for x in summary["gates"].values())
            or summary["mode"] != "carrier" or summary["panels"] != 111
            or summary["cell"] != 0 or summary["segment"] != 7
            or [x["part"] for x in summary["parts"]] != [0]
            or summary["modes"] != list(range(2, 41, 2))):
        raise ValueError("The complete actual carrier execution is required")
    command = usage["command"]
    recorded_summary = Path(command[command.index("--out-prefix")+1]+"-summary.json")
    if recorded_summary.name != args.carrier_summary.name:
        raise ValueError("The formal resource belongs to a different carrier")
    # Both summary and resource above were checked against their original full SHA.
    # File location is allowed to change; scientific bytes and formal result are not.
    relocation = {}
    def archive_path(original, expected):
        original = Path(original)
        local = original if original.is_file() else args.topic/"notes"/original.name
        check(local, expected)
        relocation[str(original)] = dict(path=str(local), sha256=expected)
        return local
    for name, expected in summary["input_hashes"].items():
        p = Path(name)
        archive_path(p if p.is_absolute() else args.topic/p, expected)
    for name, expected in summary["source_hashes"].items():
        check(args.math_directory/Path(name).name, expected)
    if (not background["real_background_curvature_paid"]
            or background["all_cells_background_curvature_bound"] != 8):
        raise ValueError("The identical real background curvature is not paid")
    candidate = plain_read(args.topic/"notes/2026-11-12-tail-outer-cell0-seg7-substage-r1.json.gz")
    if candidate["input_hashes"].get(READY) != background["input_hashes"][READY]:
        raise ValueError("The actual carrier and proved background use different metrics")
    if not all(v is True for v in old["gates"].values()):
        raise ValueError("The other seven original conditional parts are unpaid")
    untouched = [p for p in old["chosen"] if p["part"] != 0]
    if len(untouched) != 7 or not all(p["existing_coarse_defect_budget_passed"] for p in untouched):
        raise ValueError("The fixed other seven original parts do not meet the same epsilon")
    part = summary["parts"][0]
    path = archive_path(part["path"], part["sha256"])
    rows = []
    header = trailer = False
    at = Q(0)
    max_curvature, max_formal, max_defect = Q(0), Q(0), Q(0)
    with gzip.open(path, "rt") as stream:
        for line in stream:
            row = json.loads(line)
            if row["kind"] == "header":
                if (header or rows or row["mode"] != "carrier"
                        or row["input_hashes"] != summary["input_hashes"]
                        or row["source_hashes"] != summary["source_hashes"]
                        or row["complete_J_cosine_modes"] != list(range(0, 81, 2))):
                    raise ValueError("The complete carrier primary header changed")
                header = True
                continue
            if row["kind"] == "trailer":
                if trailer or not row["complete"] or row["panels"] != len(rows):
                    raise ValueError("The complete carrier trailer changed")
                trailer = True
                continue
            if (not header or trailer or row["kind"] != "complete_new_physical_substage_R64_J_R77_leaf"
                    or not row["complete_mean"] or row["panel"] != len(rows)
                    or Q(row["source_left"]) != at or not at < Q(row["source_right"]) <= Q(1, 8)
                    or len(row["full_J_cosine_intervals"]) != 41
                    or any(dyadic(v) <= 0 for v in row["gates_lower"].values())):
                raise ValueError("The complete original leaf/frequency/mean cover is absent")
            record, curvature, formal, defect = compute(row, summary["modes"], eps)
            rows.append(record)
            max_curvature, max_formal, max_defect = max(max_curvature, curvature), max(max_formal, formal), max(max_defect, defect)
            at = Q(row["source_right"])
            if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 1024*args.rss_limit_mib:
                raise MemoryError("Owned exact curvature consumer exceeded its observed RSS")
    if not (header and trailer and at == Q(1, 8) and len(rows) == 111):
        raise ValueError("Not all 111 actual carrier leaves were consumed")
    others = max(dyadic(p["existing_coarse_defect_curvature_upper"]) for p in untouched)
    result = dict(schema="actual-carrier-own-reference-R95-R99-curvature-relocated-v1",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",
        status="Exact conditional geometry budget, not an actual solution error certificate",
        input_hashes=inputs, source_sha256=digest(__file__),
        original_consumer_sha256="7f4a8c1269ee7b4df3ecab75b4a173f8e89d02bc28e38f030c81ff13048e6d0c",
        archive_relocation=relocation, original_pending_output_recovered=False,
        epsilon=str(eps), actual_carrier_leaves=111, unchanged_original_parts=list(range(1, 8)),
        candidate_formal_curvature_upper=upper(max_formal),
        carrier_same_leaf_actual_physical_defect_upper=upper(max_defect),
        conditional_carrier_curvature_upper=upper(max_curvature),
        conditional_mixed_reference_whole_seg7_curvature_upper=upper(max(max_curvature, others)),
        target_curvature="33/4", every_carrier_leaf_target_passed=all(r["conditional_target_passed"] for r in rows),
        matrix_column_order=["K_nonmean", "P", "P_theta", "K_theta"],
        matrix_row_order=["h_r", "h_theta", "h_rr", "h_rtheta", "h_thetatheta"],
        complete_mean_implicitly_included_in_positive_matrix=True,
        new_reference_is_carrier_on_part0_original_R48_elsewhere=True,
        reference_joins_by_same_nonmean_two_jets_and_one_integrated_mean=True,
        complete_frequency_error_and_true_same_metric_Darboux_solution_are_unpaid_hypotheses=True,
        reference_vector_is_not_asserted_candidate_normal=True,
        actual_reach_held_or_full_time_family_not_claimed=True,
        rows=rows, gates=dict(actual_formal_carrier_exit0=True, all_original_inputs_and_sources_same=True,
            complete_111_leaf_and_41_J_mode_cover=True, full_actual_mean_and_Hrr_retained=True,
            identical_real_background_K8_paid=True, complete_true_mean_continuation_box=True,
            same_leaf_actual_wJ_over_L_defect=True, no_original_R48_baseline_borrowed=True,
            seven_other_parts_reuse_only_their_original_paid_bounds=True),
        new_Arb_Node_ODE_or_integrals=0, elapsed_seconds=time.monotonic()-started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    args.out.write_text(json.dumps(result, separators=(",", ":"))+"\n")
    print(json.dumps(dict(event="complete_actual_carrier_conditional_curvature", output=str(args.out),
        all_111_conditional_targets=result["every_carrier_leaf_target_passed"],
        formal_curvature_diagnostic=float(max_formal), conditional_curvature_diagnostic=float(max_curvature),
        actual_defect_diagnostic=float(max_defect), whole_seg7_diagnostic=float(max(max_curvature, others)),
        peak_RSS_KiB=result["peak_RSS_KiB"])), flush=True)


if __name__ == "__main__":
    main()
