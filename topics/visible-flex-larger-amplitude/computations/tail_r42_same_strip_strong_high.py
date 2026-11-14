#!/usr/bin/env python3
"""Rescale the paid q high kernel to actual strong M20 on the identical q strip.

R42 sections4/5 give every scaling used here.  The continuous function is
defined to remain tau_q(r); its endpoints alone are not used to identify
two independently normalized strips.  The new k only proves derivative
domination.  Consumers that reconstruct tau must use the original q
material/density package, not renormalize a new strong integral.

The complete high box is recomputed, with all213 cells, the full causal
triangle, all modes >=8192, the full mean/inverse and an independent R18
parameter ball.  No new ODE, source integration, low solve or Node task.

Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

from flint import arb, ctx
from closure_real_head_source_enclosure import exact_q, ball_record, power2
from closure_real_head_green_enclosure import load_json, ball
from tail_r33_quadratic_high_box import majorant, derivative


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def exact_dyadic(record):
    """A fixed outward envelope is a defined exact dyadic, not a radius ball."""
    if record["lower"] != record["upper"]:
        raise ValueError("An exact stored envelope coefficient was required")
    entry = record["lower"]
    value = Fraction(int(entry["mantissa"]))
    exponent = int(entry["binary_exponent"])
    return value*2**exponent if exponent >= 0 else value/Fraction(2**(-exponent))


def same_ball(left, right):
    return all(left[k] == right[k] for k in ("lower", "upper"))


def dump(path, document):
    raw = (json.dumps(document, indent=2)+"\n").encode()
    if len(raw) >= 1_000_000 and path.suffix != ".gz":
        raise ValueError("Expanded ledgers must use gzip")
    if path.suffix == ".gz":
        raw = gzip.compress(raw, mtime=0)
    if len(raw) >= 5_000_000:
        raise ValueError("The repository single-file limit was exceeded")
    path.write_bytes(raw)
    return dict(path=str(path), bytes=len(raw), sha256=sha(raw))


def fixed_high(cells, gamma, A, ghi, pure, far, deep, pure_inf, h):
    """The original quadratic high-box proof, on the newly defined norms."""
    radii, images, slack, weights, liprows, slopes = {}, {}, {}, {}, {}, {}
    failure = None
    inf_image = inf_lip = z_column = None
    tiny = power2(-10000)
    for n in reversed(cells):
        constant = (pure[n]+far[n]+sum(
            (gamma[n, j]*majorant(radii[j]+h, A[j]) for j in range(n+1, 225)),
            arb(0))).upper()
        value = arb(0)
        for unused in range(256):
            updated = (constant+gamma[n, n]*majorant(value+h, A[n])).upper()
            if updated == value or updated > 1:
                break
            value = updated
        radius = (arb(101)/100*updated+tiny).upper()
        image = (constant+gamma[n, n]*majorant(radius+h, A[n])).upper()
        if not image < radius or not A[n]*(1+radius+h) < arb(1)/64:
            failure = dict(cell=n, reason="Strong fixed-low inclusion or complete mean domain failed",
                           radius=ball_record(radius), image=ball_record(image))
            break
        radii[n], images[n], slack[n] = radius, image, (radius-image).lower()
    if failure is None:
        inf_image = (deep+pure_inf+ghi*sum(
            (majorant(radii[n]+h, A[n]) for n in cells), arb(0))).upper()
        slopes = {n: derivative(radii[n]+h, A[n]) for n in cells}
        target = arb(3)/4
        for n in reversed(cells):
            diagonal = gamma[n, n]*slopes[n]
            if not diagonal < target:
                failure = dict(cell=n, reason="A strong local derivative exceeds3/4")
                break
            infinite_input = sum(
                (gamma[n, j]*slopes[j] for j in range(n, 225)), arb(0))
            future = sum(
                (gamma[n, j]*slopes[j]*weights[j] for j in range(n+1, 225)), arb(0))
            weights[n] = max((radii[n]/h).upper(),
                (arb(101)/100*(infinite_input+future)/(target-diagonal)).upper(), tiny)
        if failure is None:
            liprows = {
                n: (sum((gamma[n, j]*slopes[j]*(weights[j]+1)
                         for j in range(n, 225)), arb(0))/weights[n]).upper()
                for n in cells}
            inf_lip = (ghi*sum(
                (slopes[n]*(weights[n]+1) for n in cells), arb(0))).upper()
            z_column = max([4*deep]+[(4*far[n]/weights[n]).upper() for n in cells])
    gates = dict(
        middle_invariance=failure is None,
        infinite_invariance=inf_image is not None and inf_image < h,
        complete_mean_domain=failure is None,
        middle_metric=bool(liprows) and max(liprows.values()) < arb(3)/4,
        infinite_metric=inf_lip is not None and inf_lip < arb(3)/4)
    rows = []
    for n in cells:
        row = dict(cell=n, pure_low_residual=ball_record(pure[n]),
                   far_boundary=ball_record(far[n]), Astar=ball_record(A[n]))
        if n in radii:
            row.update(radius=ball_record(radii[n]), image=ball_record(images[n]),
                       map_slack=ball_record(slack[n]))
        if n in weights:
            row.update(metric_weight=ball_record(weights[n]),
                       local_full_source_derivative=ball_record(slopes[n]))
        if n in liprows:
            row["weighted_derivative_row"] = ball_record(liprows[n])
        rows.append(row)
    return dict(rows=rows, gates=gates, failure=failure,
        infinite_radius=ball_record(h),
        infinite_image=ball_record(inf_image) if inf_image is not None else None,
        infinite_weighted_derivative_row=ball_record(inf_lip) if inf_lip is not None else None,
        independent_far_map_column=ball_record(z_column) if z_column is not None else None)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("q-density", "strong-density", "q-high", "q-middle", "out-prefix"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--z-log2", type=int, default=-2200)
    parser.add_argument("--infinite-radius-log2", type=int, default=-120)
    args = parser.parse_args()
    ctx.prec = 192
    started = time.monotonic()
    names = ("density.json.gz", "middle.json.gz", "high.json.gz", "summary.json")
    paths = {name.split(".")[0]: args.out_prefix.with_name(args.out_prefix.name+"-"+name)
             for name in names}
    if any(path.exists() for path in paths.values()):
        raise FileExistsError("Use a fresh complete output prefix")
    docs, hashes = {}, {}
    for name in ("q_density", "strong_density", "q_high", "q_middle"):
        path = getattr(args, name)
        docs[name], raw = load_json(path)
        hashes[str(path)] = sha(raw)
    qd, sd, qh, qm = (docs[k] for k in
        ("q_density", "strong_density", "q_high", "q_middle"))
    if any(not all(doc["gates"].values()) for doc in (qd, sd, qh, qm)):
        raise ValueError("Every original input must have paid all its own stated gates")
    qhash = hashes[str(args.q_density)]
    if any(qhash not in doc["input_hashes"].values() for doc in (qh, qm)):
        raise ValueError("The original high response/kernel use another q envelope")
    if hashes[str(args.q_middle)] not in qh["input_hashes"].values():
        raise ValueError("The original high response names another causal kernel")
    if Path(qh["gamma_source"]) != args.q_middle:
        raise ValueError("The original high kernel path differs")
    if not qh["independent_far_parameter"] or not qh["complete_mean_and_pointwise_inverse"]:
        raise ValueError("The original complete source or independent far ball is absent")
    if args.z_log2 != -2200 or qh["z_log2"] != args.z_log2:
        raise ValueError("This adapter keeps the original independent Z=2^-2200 exactly")
    if qd["cutoff"] != 8192 or sd["cutoff"] != 8192:
        raise ValueError("The proved middle/infinite split must remain8192")
    common_sources = (
        "notes/2026-11-12-closure-real-linear-q003-low46-recovered-columns-01-08.json.gz",
        "notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json",
        "notes/2026-11-12-closure-wide-strip-head-ledger-paid-source.json")
    for name in common_sources:
        if name not in qd["input_hashes"] or qd["input_hashes"][name] != sd["input_hashes"].get(name):
            raise ValueError("The strong reference does not share the exact real source/columns: "+name)
    cells = list(range(12, 225))
    qr, sr, hr = ({r["cell"]: r for r in doc["rows"]} for doc in (qd, sd, qh))
    if sorted(qr) != cells or sorted(sr) != cells or sorted(hr) != cells:
        raise ValueError("Every one of the213 actual cells is required")
    unchanged = ("B", "Q_coefficient", "mu_lower", "mu_upper",
        "normalized_width_upper", "TV_log_w_upper", "w_lower",
        "beta_integral_upper", "eta_integral_upper",
        "certified_reference_tau", "reference_tau", "minimum_strip_buffer")
    for n in cells:
        for field in unchanged:
            if not same_ball(qr[n][field], sr[n][field]):
                raise ValueError(f"The strong physical/strip reference differs at cell{n}/{field}")
    Xq = {n: exact_dyadic(qr[n]["canonical_total_envelope"]) for n in cells}
    Xs = {n: exact_dyadic(sr[n]["canonical_total_envelope"]) for n in cells}
    if any(Xq[n] <= 0 or Xs[n] <= 0 for n in cells):
        raise ValueError("Positive exact canonical envelopes are required")
    sigma_exact = {n: Xs[n]/Xq[n] for n in cells}
    sigma = {n: exact_q(sigma_exact[n]) for n in cells}
    sminus, splus = exact_q(min(sigma_exact.values())), exact_q(max(sigma_exact.values()))
    infinite_scale = (splus*splus/sminus).upper()
    k_required = max(sigma_exact.values())*exact_dyadic(qd["k"])
    ks = exact_q(k_required).upper()
    if exact_dyadic(ball_record(ks)) < k_required:
        raise ArithmeticError("The new defined dyadic k failed upward rounding")
    A = {n: (sigma[n]*ball(qr[n]["V_over_w_upper"])).upper() for n in cells}
    ghi = (infinite_scale*ball(qd["gamma_high"])).upper()
    density_rows, jumps = [], []
    for n in cells:
        row = dict(qr[n])
        row["canonical_total_envelope"] = sr[n]["canonical_total_envelope"]
        row["scale_from_original_q"] = ball_record(sigma[n])
        row["original_q_canonical_total_envelope"] = qr[n]["canonical_total_envelope"]
        row["V_over_w_upper"] = ball_record(A[n])
        row["density_integral_upper"] = ball_record(
            (sigma[n]*ball(qr[n]["density_integral_upper"])).upper())
        # tau is the OLD q function, not a new normalized integral.  The
        # exact inequality sigma_n*k_q<=k_s proves its derivative gate.
        if sigma_exact[n]*exact_dyadic(qd["k"]) > exact_dyadic(ball_record(ks)):
            raise ArithmeticError("A source-density derivative domination failed")
        # The old sufficient cost is still a valid upper bound for the
        # new b_tau integral by that pointwise domination.
        if not ball(row["available_strip_drop"]) >= ball(row["sufficient_strip_cost"]):
            raise ValueError("An original continuous-strip cost is not paid")
        density_rows.append(row)
    for n in cells[:-1]:
        jumps.append(dict(
            outer_cell=n, inner_cell=n+1,
            B_contracts_outward=exact_dyadic(qr[n]["B"]) <= exact_dyadic(qr[n+1]["B"]),
            V_Q_part_increases_outward=Xs[n]*exact_dyadic(qr[n]["Q_coefficient"]) >=
                Xs[n+1]*exact_dyadic(qr[n+1]["Q_coefficient"]),
            V_Xi_part_increases_outward=Xs[n]*exact_dyadic(qr[n]["mu_upper"]) >=
                Xs[n+1]*exact_dyadic(qr[n+1]["mu_upper"])))
    jump_gate = all(all(v for key, v in row.items() if key.endswith("outward")) for row in jumps)
    Amax = max(A.values())
    density_gates = dict(
        identical_real_source_and_envelope_geometry=True,
        identical_certified_wide_reference_strips=True,
        explicitly_identical_original_q_continuous_strip=True,
        pointwise_strong_density_dominated_by_original_strip_budget=True,
        all_original_cell_strip_costs_paid=True,
        all_contractive_norm_jumps=jump_gate,
        positive_shallow_strip=bool(ball(qd["tau_shallow"]) > 0),
        complete_mean_working_domain=bool(Amax*(ball(sd["low_state_bound"])+1) < arb(1)/64),
        complete_strong_auxiliary_far_domain=bool(sd["gates"]["nonlinear_deep_graph_domain"]),
        independent_R18_parameter_ball_preserved=True)
    if not all(density_gates.values()):
        raise ValueError("A new strong same-strip physical domain gate failed")
    source_hashes = {name: sha(Path(__file__).with_name(name).read_bytes()) for name in
        (Path(__file__).name, "tail_r33_quadratic_high_box.py",
         "closure_real_head_source_enclosure.py", "closure_real_head_green_enclosure.py")}
    density = dict(
        status="Strong M20 physical envelope on the explicitly identical original q continuous strip",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)", theorem="R42 sections4/5",
        cutoff=8192, cell_range=[12, 224], precision_bits=ctx.prec,
        physical_envelope=qd["physical_envelope"],
        physical_envelope_coefficients=qd["physical_envelope_coefficients"],
        canonical_box=sd["canonical_box"], low_state_bound=sd["low_state_bound"],
        norm_order=qd["norm_order"],
        continuous_strip_definition="tau_s(r) is DEFINED to equal the original q tau_q(r), point by point",
        continuous_strip_origin=dict(
            path=str(args.q_density), sha256=qhash,
            definition="The identical original q continuous function tau_q(r), not a new integral sharing its endpoints",
            original_definition=qd["continuous_strip_definition"],
            original_k=qd["k"],
            do_not_renormalize_using_new_strong_density=True),
        buffer=qd["buffer"], endpoint_rounding_margin=qd["endpoint_rounding_margin"],
        tau_deep=qd["tau_deep"], tau_shallow=qd["tau_shallow"],
        k=ball_record(ks), Astar_upper=ball_record(Amax), gamma_high=ball_record(ghi),
        density_integral_upper=ball_record(sum(
            (ball(row["density_integral_upper"]) for row in density_rows), arb(0)).upper()),
        beta_integral_upper=qd["beta_integral_upper"], eta_integral_upper=qd["eta_integral_upper"],
        sigma_lower=ball_record(sminus), sigma_upper=ball_record(splus),
        infinite_kernel_scale=ball_record(infinite_scale),
        far_evaluation_bound=ball_record((sigma[224]*ball(qd["far_evaluation_bound"])).upper()),
        far_high_lift_bound=ball_record((ball(qd["far_high_lift_bound"])/sminus).upper()),
        rows=density_rows, norm_jump_checks=jumps, gates=density_gates,
        input_hashes=dict(hashes), source_hashes=source_hashes,
        original_strong_strip_not_reused=True,
        all46_low_parameters_retained=True, complete_mean_and_pointwise_inverse=True,
        radial_integrations=0, new_low_solve=False, new_Node=False,
        complete_full_frequency_head_paid=False, outer_cells_0_to_11_included=False)
    density_record = dump(paths["density"], density)
    new_hashes = dict(hashes)
    new_hashes[str(paths["density"])] = density_record["sha256"]
    gamma, gamma_rows = {}, []
    if [row["output_cell"] for row in qm["gamma_rows"]] != cells:
        raise ValueError("The original causal target order is incomplete")
    for row in qm["gamma_rows"]:
        k = row["output_cell"]
        if [s["source_cell"] for s in row["sources"]] != list(range(k, 225)):
            raise ValueError("The original causal source order is incomplete")
        new_sources = []
        for source in row["sources"]:
            n = source["source_cell"]
            value = (sigma[n]**2/sigma[k]*ball(source["gamma"])).upper()
            gamma[k, n] = value
            new_sources.append(dict(source_cell=n, gamma=ball_record(value)))
        gamma_rows.append(dict(output_cell=k, sources=new_sources))
    pure = {n: (splus*splus/sigma[n]*ball(hr[n]["pure_low_residual"])).upper() for n in cells}
    far = {n: (ball(hr[n]["far_boundary"])/sigma[n]).upper() for n in cells}
    deep = (ball(qh["deep_high_boundary"])/sminus).upper()
    pure_inf = (infinite_scale*ball(qh["pure_low_infinite_residual"])).upper()
    solved = fixed_high(cells, gamma, A, ghi, pure, far, deep, pure_inf,
                        power2(args.infinite_radius_log2))
    middle = dict(
        status="Complete real causal middle kernel rescaled to strong M20 on exactly the original q strip",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)", theorem="R42 section5",
        gamma_rows=gamma_rows, cells=[
            dict(cell=n, far_boundary=ball_record(far[n])) for n in cells],
        z_log2=args.z_log2, causal_triangle_size=len(gamma),
        scaling="Gamma_s[k,n]=(sigma_n^2/sigma_k)*Gamma_q[k,n], rounded upward",
        original_kernel=str(args.q_middle), original_kernel_sha256=hashes[str(args.q_middle)],
        input_hashes=dict(new_hashes), source_hashes=source_hashes,
        gates=dict(full_causal_triangle=len(gamma)==len(cells)*(len(cells)+1)//2,
                   same_real_source=True, exactly_same_continuous_strip=True,
                   complete_strong_mean_domain=density_gates["complete_mean_working_domain"]),
        no_new_radial_integrations=True, fixed_low_box_paid=all(solved["gates"].values()))
    middle_record = dump(paths["middle"], middle)
    new_hashes[str(paths["middle"])] = middle_record["sha256"]
    high = dict(
        status="Complete strong fixed-low high response on the original q strip" if all(solved["gates"].values())
            else "Strong same-strip high response attempt; stated gates remain unpaid",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",
        independent_far_parameter=True, z_log2=args.z_log2,
        far_metric="|delta z|_38 / 2^-2200; low field and far input are independent",
        complete_mean_and_pointwise_inverse=True,
        source_majorant=qh["source_majorant"], source_derivative=qh["source_derivative"],
        gamma_source=str(paths["middle"]), gamma_unchanged=False,
        gamma_rescaled_from=str(args.q_middle), low46_held_fixed=True,
        whole_head_closed=False, deep_high_boundary=ball_record(deep),
        pure_low_infinite_residual=ball_record(pure_inf),
        input_hashes=new_hashes, source_hashes=source_hashes,
        pure_scaling="sigma_plus^2/sigma_target; infinity sigma_plus^2/sigma_minus; whole canonical envelope bound, no q-specific mode truncation",
        far_scaling="The same complete independent R18 ball, divided only by the target physical normalization",
        elapsed_seconds=time.monotonic()-started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        **solved)
    high_record = dump(paths["high"], high)
    summary = dict(
        status=high["status"], author=high["author"], files=[density_record, middle_record, high_record],
        gates=solved["gates"], failure=solved["failure"],
        sigma_lower=ball_record(sminus), sigma_upper=ball_record(splus),
        k=ball_record(ks), gamma_high=ball_record(ghi),
        tau_identity="Exactly the original q function; native strong tau is not used",
        input_hashes=hashes, source_hashes=source_hashes,
        radial_integrations=0, nonlinear_numerical_solves=0, new_Node=False,
        elapsed_seconds=time.monotonic()-started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    summary_record = dump(paths["summary"], summary)
    print(json.dumps(dict(output=str(paths["summary"]), sha256=summary_record["sha256"],
        gates=solved["gates"], failure=solved["failure"],
        seconds=summary["elapsed_seconds"], RSS_KiB=summary["peak_RSS_KiB"])), flush=True)


if __name__ == "__main__":
    main()
