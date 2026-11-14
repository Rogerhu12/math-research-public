#!/usr/bin/env python3
"""Complete current moving coefficients on the positive body, in bounded batches.

The candidate index and every polynomial shard are verified by their real
SHA identities. Only the unchanged intrinsic cap v2 boxes are reused.
The short interval before 239/1000 is recomputed on its true scalar germs.
Every finite Fourier coefficient, every allowed mean and every PPoly
one-sided interface is retained. This producer does not claim an inverse.
"""
from __future__ import annotations
import argparse
import ast
from bisect import bisect_right
from fractions import Fraction
import gzip
import json
from pathlib import Path
import time
from flint import arb, ctx

from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_rotational_cap_jacobi import RotationalPositiveCap, box_from_record
from fourfold_phase_beta_affine import load_definition
from fourfold_phase_beta_bulk_interval import exact_arb, real_interval
from fourfold_phase_metric_defect import record, save, sha

CURRENT_SHA = "ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
OBJECT_SHA = "91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848"
CAP_CACHE_SHA = "3a89805ebe1ab22000529a7a8c2fdc262b1c3a2afbc52433cf610d2d6542ff22"
LEFT = Fraction("0.2384058742994")
RIGHT = Fraction(25, 8)
CACHE_LEFT = Fraction(239, 1000)
KIND = "complete_current_moving_positive_body_coefficients_v1"


def read_doc(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if Path(path).suffix == ".gz" else raw)


def dyadic(x):
    return Fraction.from_float(float(x))


def upper(x):
    return abs(arb(x)).upper()


def literal_coordinates():
    path = Path(__file__).with_name("fourfold_codazzi_moving_polynomial_system.py")
    tree = ast.parse(path.read_text())
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(isinstance(t, ast.Name) and t.id == "COORDINATES" for t in node.targets):
                value = ast.literal_eval(node.value)
                if isinstance(value, str):
                    return value
    raise ValueError("the actual moving coordinate identity was not found")


def convolution(a, b):
    out = [arb(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def angular_norm(a, lower, order=0, omit_mean=False):
    total = arb(0)
    for k, z in zip(range(lower, lower + len(a)), a):
        if omit_mean and k == 0:
            continue
        total += abs(z) * (4 * abs(k)) ** order
    return total.upper()


def polynomial_values(saved, nodes, piece, left, right):
    if not nodes[piece] <= left < right <= nodes[piece + 1]:
        raise ValueError("a closed row crosses the actual PPoly piece")
    x = real_interval(left - nodes[piece], right - nodes[piece])
    coeff = saved["piece_coefficients"]
    values = []
    for component in range(coeff.shape[2]):
        z = arb(0)
        for degree in range(4):
            z = z * x + exact_arb(dyadic(coeff[degree, piece, component]))
        values.append(z)
    return values


def exact_polynomial_endpoint(saved, nodes, piece, radial):
    x = radial - nodes[piece]
    coeff = saved["piece_coefficients"]
    values = []
    for component in range(coeff.shape[2]):
        z = Fraction(0)
        for degree in range(4):
            z = z * x + dyadic(coeff[degree, piece, component])
        values.append(z)
    return values


def interface_record(saved, nodes, piece, alpha, modes, radial):
    if piece + 1 >= len(nodes) - 1 or radial != nodes[piece + 1]:
        return None
    left = exact_polynomial_endpoint(saved, nodes, piece, radial)
    right = exact_polynomial_endpoint(saved, nodes, piece + 1, radial)
    jump = [alpha * (b - a) for a, b in zip(left, right)]
    weights = [4 * j for j in range(1, modes + 1)] + [0] + [
        4 * j for j in range(1, modes + 1)
    ]
    a0 = sum(map(abs, jump), Fraction(0))
    a1 = sum((abs(z) * (1 + k) for z, k in zip(jump, weights)), Fraction(0))
    a2 = sum((abs(z) * (1 + k) ** 2 for z, k in zip(jump, weights)), Fraction(0))
    return dict(
        radial=str(radial), left_piece=piece, right_piece=piece + 1,
        convention="right minus left in the same moving angle",
        intrinsic_s_jump="0 by the actual target's proved continuous chart",
        u_v_pair_A0_exact=str(a0), u_v_pair_A1_upper_exact=str(a1),
        u_v_pair_A2_upper_exact=str(a2),
        even_mean_v_jump_exact=str(jump[modes]), odd_mean_jump_exact="0",
        independent_affine_interface_source_retained=True,
        homogeneous_linear_interface="identity in the same moving unknown",
    )


def full_fields(values, modes, alpha, scalar_s):
    """u=i*ui and v=vr, in the full complex Fourier convention."""
    ui = [arb(0) for _ in range(2 * modes + 1)]
    vr = [arb(0) for _ in range(2 * modes + 1)]
    vr[modes] = scalar_s + alpha * values[modes]
    for j in range(1, modes + 1):
        sine = alpha * values[j - 1] / 2
        cosine = alpha * values[modes + j] / 2
        ui[modes + j], ui[modes - j] = -sine, sine
        vr[modes + j] = vr[modes - j] = cosine
    return ui, vr


def coefficient_row(saved, nodes, piece, left, right, alpha, modes, intrinsic):
    gamma, beta, K, Cr = (intrinsic[name] for name in ("gamma", "beta", "K", "Cref"))
    if not gamma > 0 or not K > 0 or not Cr < 0:
        raise ValueError("strict intrinsic positivity/negative Cref failed")
    values = polynomial_values(saved, nodes, piece, left, right)
    ui, vr = full_fields(values, modes, alpha, 1 / Cr)
    mean = vr[modes]
    speed = -gamma * mean
    if not mean < 0 or not speed > 0:
        raise ValueError("the actual moving radial speed is unresolved")
    if not all(z.is_finite() for z in ui + vr):
        raise ValueError("nonfinite complete candidate enclosure")
    u2 = [-z for z in convolution(ui, ui)]
    v2 = convolution(vr, vr)
    uv_imag = convolution(ui, vr)
    S = [a + K * b for a, b in zip(u2, v2)]
    zero = 2 * modes
    la = [-beta * (3 * a + K * b + (1 if k == zero else 0))
          for k, (a, b) in enumerate(zip(u2, v2))]
    le = [beta * ((1 if k == zero else 0) - a - 3 * K * b)
          for k, (a, b) in enumerate(zip(u2, v2))]
    lb = [-2 * beta * z for z in uv_imag]
    U = angular_norm(ui, -modes)
    V = angular_norm(vr, -modes)
    U1 = angular_norm(ui, -modes, 1)
    V1 = angular_norm(vr, -modes, 1)
    Vne = angular_norm(vr, -modes, omit_mean=True)
    ab = upper(beta)
    dphi = (ab * angular_norm(S, -2 * modes, omit_mean=True)).upper()
    drift = (ab * sum(
        (abs(z) / (4 * abs(k))
         for k, z in zip(range(-2 * modes, 2 * modes + 1), S) if k),
        arb(0))).upper()
    aA, eA, bA = (angular_norm(p, -2 * modes) for p in (la, le, lb))
    aSup = min(aA, (ab * (1 + 3 * U * U + K * V * V)).upper()).upper()
    eSup = min(eA, (ab * max(arb(1), (U * U + 3 * K * V * V - 1).upper())).upper()).upper()
    bSup = min(bA, (2 * ab * U * V).upper()).upper()
    primitive_raw = (ab * (U1 + V1) * (U + K * V) / 2).upper()
    mean_rank_raw = (gamma * (U1 + K * V1)).upper()
    mean_own = beta * (1 - S[zero] - 2 * K * mean * mean)
    mean_feedback = (2 * ab * abs(mean) * (U + K * Vne)).upper()
    physical_gap = -mean - Vne
    bounds = dict(
        mean_v=mean, radial_speed=speed, U_A0=U, V_A0=V,
        U_phi_A0=U1, V_phi_A0=V1, V_nonmean_A0=Vne,
        drift_A0=drift, drift_phi_A0=dphi, full_S_mean=S[zero],
        local_a_A0=aA, local_e_A0=eA, local_b_A0=bA,
        local_a_sup=aSup, local_e_sup=eSup, local_b_sup=bSup,
        primitive_raw_L2=primitive_raw, mean_rank_raw_L2=mean_rank_raw,
        mean_own_rate=mean_own, mean_nonmean_feedback_L2=mean_feedback,
        real_physical_inverse_gap=physical_gap,
    )
    if not all(z.is_finite() for z in bounds.values()):
        raise ValueError("nonfinite complete moving coefficient bound")
    return dict(
        bounds={k: record(v) for k, v in bounds.items()},
        physical_inverse_gap_certified=bool(physical_gap > 0),
        complete_finite_modes=modes, exact_local_band=2 * modes,
        complete_primitive_intermediate_retained=True,
        complete_mean_column_retained=True,
        fields_are_moving_phi_not_physical_theta=True,
    )



def intersect_intrinsic_K(values):
    """Use the independently proved whole-positive intrinsic floor, not sampling."""
    values=dict(values)
    raw=values["K"]
    lo=max(raw.lower(),exact_arb(Fraction(1,2000)).lower()).lower()
    hi=min(raw.upper(),arb(4)).upper()
    if not lo<=hi:
        raise ValueError("native K and the independent true global K theorem are disjoint")
    values["K"]=lo.union(hi)
    if not all(values[k]>0 for k in ("a","Ebar","R","K")):
        raise ValueError("strict complete intrinsic primitive positivity is unresolved")
    if "gamma" not in values:values["gamma"]=values["Ebar"].sqrt()
    if "Cref" not in values:values["Cref"]=-(values["R"]/values["Ebar"]).sqrt()
    return values,record(raw)


def checked_cap(path, object_path, half_width):
    if sha(path) != CAP_CACHE_SHA:
        raise ValueError("the exact published 1334-box intrinsic cache changed")
    cap = read_doc(path)
    if (cap.get("kind") != "actual_fixed_target_rotational_cap_complete_Codazzi_Jacobi_v2"
        or not cap.get("complete") or not cap.get("cap_linear_reference_certified")
        or cap.get("object_sha256") != sha(object_path)
        or Fraction(cap["parameter_half_width"]) != half_width
        or list(map(Fraction, cap["exact_requested_interval"])) != [CACHE_LEFT, RIGHT]
        or list(map(Fraction, cap["covered_interval"])) != [CACHE_LEFT, RIGHT]):
        raise ValueError("the complete strict-positive intrinsic cap cache differs")
    for key, filename in (
        ("source_sha256", "fourfold_codazzi_rotational_cap_jacobi_v2.py"),
        ("original_source_sha256", "fourfold_codazzi_rotational_cap_jacobi.py"),
    ):
        if cap[key] != sha(Path(__file__).with_name(filename)):
            raise ValueError("the certified cap producer changed: " + filename)
    for filename, digest in cap["dependency_sha256"].items():
        if sha(Path(__file__).with_name(filename)) != digest:
            raise ValueError("an intrinsic cap dependency changed: " + filename)
    endpoint = CACHE_LEFT
    for row in cap["rows"]:
        left, right = map(Fraction, row["interval"])
        if left != endpoint or right <= left:
            raise ValueError("the cached complete intrinsic cover has a gap")
        vals = {name: box_from_record(row["coefficients"][name])
                for name in ("a", "beta", "Ebar", "R", "K", "gamma", "Cref")}
        if not all(vals[k] > 0 for k in ("a", "Ebar", "R", "K", "gamma")) or not vals["Cref"] < 0:
            raise ValueError("cached primitive positivity must precede all ratios")
        endpoint = right
    if endpoint != RIGHT:
        raise ValueError("the cached intrinsic cap does not reach the true endpoint")
    return cap


def verify_cover(doc, left, right):
    endpoint = left
    for row in doc["rows"]:
        a, b = map(Fraction, row["interval"])
        if a != endpoint or not a < b:
            raise ValueError("the completed actual coefficient prefix has a gap")
        endpoint = b
    for a, b, depth in reversed(doc["pending"]):
        a, b = Fraction(a), Fraction(b)
        if a != endpoint or not a < b or int(depth) < 0:
            raise ValueError("the true pending partition has a gap")
        endpoint = b
    if endpoint != right:
        raise ValueError("the saved prefix plus pending cells is not the complete domain")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--candidate", type=Path, required=True)
    ap.add_argument("--candidate-sha256", default=CURRENT_SHA)
    ap.add_argument("--object", type=Path, default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"))
    ap.add_argument("--cap-cache", type=Path, default=Path(
        "notes/2026-11-13-Codazzi-rotational-positive-cap-v2-native.json.gz"))
    ap.add_argument("--left", type=Fraction, default=LEFT)
    ap.add_argument("--half-width", type=Fraction, default=Fraction(1, 10**9))
    ap.add_argument("--bits", type=int, default=320)
    ap.add_argument("--nodes", type=int, default=512)
    ap.add_argument("--max-depth", type=int, default=16)
    ap.add_argument("--max-rows", type=int, default=64)
    ap.add_argument("--save-every", type=int, default=8)
    ap.add_argument("--resume", action="store_true")
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    if (not LEFT <= args.left < CACHE_LEFT or args.half_width != Fraction(1, 10**9)
        or args.bits < 256 or args.nodes < 512 or args.max_rows <= 0 or args.save_every <= 0):
        raise ValueError("invalid actual domain, parameter, precision or batch")
    ctx.prec = args.bits
    ctx.cap = 6
    start = time.monotonic()
    if sha(args.candidate) != args.candidate_sha256 or sha(args.object) != OBJECT_SHA:
        raise ValueError("the exact complete candidate or intrinsic object changed")
    saved = load_candidate(args.candidate)
    meta = json.loads(str(saved["metadata"]))
    if meta["object_sha256"] != OBJECT_SHA or meta["coordinates"] != literal_coordinates():
        raise ValueError("moving and physical finite coordinates must not be identified")
    modes = int(meta["modes"])
    alpha_q = dyadic(meta["amplitude"])
    alpha = exact_arb(alpha_q)
    if alpha_q <= 0 or saved["piece_coefficients"].shape[2] != 2 * modes + 1:
        raise ValueError("incomplete moving finite candidate")
    nu = Fraction(meta["exact_float_nu"])
    if not Fraction(-1, 25) <= nu <= Fraction(-1, 40):
        raise ValueError("the compact nu interval differs from the proved target")
    cap = checked_cap(args.cap_cache, args.object, args.half_width)
    definition, _, _, eta_center = load_definition(args.object)
    if str(eta_center) != cap["exact_center_parameter"]:
        raise ValueError("the actual affine eta centre differs")
    nodes = list(map(dyadic, saved["radial_nodes"]))
    if not nodes[0] <= args.left < RIGHT <= nodes[-1]:
        raise ValueError("the actual candidate does not cover the full positive body")
    target = RotationalPositiveCap(args.object, args.half_width, args.nodes)
    cap_starts = [Fraction(r["interval"][0]) for r in cap["rows"]]
    cap_edges = [Fraction(r["interval"][1]) for r in cap["rows"]]
    identity = dict(
        source_sha256=sha(__file__), candidate_sha256=sha(args.candidate),
        object_sha256=sha(args.object), cap_cache_sha256=sha(args.cap_cache),
        exact_eta_center=str(eta_center), parameter_half_width=str(args.half_width),
        actual_nu=str(nu), actual_alpha=str(alpha_q), modes=modes, bits=args.bits,
        primitive_nodes=args.nodes, left=str(args.left), right=str(RIGHT),
        max_depth=args.max_depth,
        theorem_sha256={name:sha(Path("results")/name) for name in (
            "R133-supplement-whole-positive-reference-floor-and-cached-producer.md",
            "R133-supplement-global-positive-reference-and-current-collar.md",
            "R133-supplement-full-compact-metric-curvature-type.md",
            "R133-actual-rotational-positive-cap-and-Codazzi-Jacobi-graph.md")},
        dependency_sha256={name: sha(Path(__file__).with_name(name)) for name in (
            "fourfold_codazzi_candidate_shards.py",
            "fourfold_codazzi_rotational_cap_jacobi.py",
            "fourfold_codazzi_rotational_cap_jacobi_v2.py",
            "fourfold_codazzi_moving_polynomial_system.py",
            "fourfold_phase_beta_bulk_interval.py",
            "fourfold_phase_metric_defect.py")},
    )
    if args.out.exists():
        if not args.resume:
            raise FileExistsError("use --resume only for an unfinished nonfailed checkpoint")
        doc = read_doc(args.out)
        if doc.get("kind") != KIND or doc["identity"] != identity:
            raise ValueError("the unchanged checkpoint identities differ")
        if doc.get("failure") is not None:
            raise ValueError("preserve the failed attempt; do not overwrite it")
        verify_cover(doc, args.left, RIGHT)
        if doc.get("complete"):
            print(json.dumps(dict(complete=True,already_complete=True,rows=len(doc["rows"]))), flush=True)
            return
    else:
        if args.resume:
            raise FileNotFoundError("the requested checkpoint does not exist")
        cuts = {args.left, CACHE_LEFT, RIGHT}
        cuts.update(x for x in nodes if args.left < x < RIGHT)
        cuts.update(x for x in cap_edges if args.left < x < RIGHT)
        cuts.update(x for x in target.cuts if args.left < x < CACHE_LEFT)
        cuts = sorted(cuts)
        pending = [[str(a),str(b),0] for a,b in reversed(list(zip(cuts[:-1],cuts[1:])))]
        doc = dict(
            kind=KIND, complete=False, coefficient_cover_complete=False,
            identity=identity, whole_original_eta=True, actual_candidate_metadata=meta,
            fixed_left_cut_is_inside_every_paid_root_piece=(args.left == LEFT),
            reuses_only_intrinsic_cap_coefficients=True,
            centre_angular_band_only=True, arbitrary_neighbourhood_not_certified=True,
            actual_high_inverse_certified=False, whole_BVP_inverse_certified=False,
            full_original_primitive_tail=True, original_cap_failure_not_modified=True,
            rows=[], pending=pending, subdivisions=[], failure=None, runs=[],
        )
        save(args.out, doc)
    verify_cover(doc, args.left, RIGHT)
    added = 0
    last_saved_added = 0
    run = dict(start_prefix_rows=len(doc["rows"]), maximum_new_rows=args.max_rows)
    doc["runs"].append(run)
    while doc["pending"] and added < args.max_rows:
        left_s,right_s,depth = doc["pending"].pop()
        left,right = Fraction(left_s),Fraction(right_s)
        try:
            piece = bisect_right(nodes,left)-1
            if left >= CACHE_LEFT:
                ci = bisect_right(cap_starts,left)-1
                cached = cap["rows"][ci]
                cl,cr = map(Fraction,cached["interval"])
                if not cl <= left < right <= cr:
                    raise ValueError("a reused row crossed its actual certified intrinsic box")
                germ = list(map(Fraction,cached["actual_scalar_germ"]))
                intrinsic = {k:box_from_record(cached["coefficients"][k])
                             for k in ("a","beta","Ebar","R","K","gamma","Cref")}
                provenance = dict(kind="same_intrinsic_cap_v2",row=ci,part=cached["part"])
            else:
                if right > CACHE_LEFT:
                    raise ValueError("a fresh intrinsic row crossed the cache entrance")
                intrinsic,germ,part = target.body_values(left,right)
                provenance = dict(kind="new_true_intrinsic_closed_box",part=part)
            intrinsic,original_K = intersect_intrinsic_K(intrinsic)
            row = coefficient_row(saved,nodes,piece,left,right,alpha,modes,intrinsic)
            row.update(
                interval=[str(left),str(right)],depth=depth,candidate_piece=piece,
                actual_candidate_germ=[str(nodes[piece]),str(nodes[piece+1])],
                actual_scalar_germ=list(map(str,germ)),intrinsic_provenance=provenance,
                original_K_enclosure_before_independent_intersection=original_K,
                independent_intrinsic_K_floor="1/2000 on the entire stated actual interval",
                intrinsic={k:record(intrinsic[k]) for k in ("a","beta","Ebar","R","K","gamma","Cref")},
                right_interface=interface_record(saved,nodes,piece,alpha_q,modes,right),
            )
            doc["rows"].append(row)
            added += 1
        except (ValueError,ZeroDivisionError) as exc:
            rejection=dict(interval=[str(left),str(right)],depth=depth,reason=str(exc))
            doc["subdivisions"].append(rejection)
            if depth >= args.max_depth:
                doc["pending"].append([str(left),str(right),depth])
                doc["failure"]=rejection
                break
            mid=(left+right)/2
            doc["pending"].extend([[str(mid),str(right),depth+1],[str(left),str(mid),depth+1]])
        if added - last_saved_added >= args.save_every:
            run["new_rows"]=added
            run["wall_seconds"]=time.monotonic()-start
            verify_cover(doc,args.left,RIGHT)
            save(args.out,doc)
            last_saved_added = added
            print(json.dumps(dict(rows=len(doc["rows"]),new_rows=added,
                pending=len(doc["pending"]),last_right=doc["rows"][-1]["interval"][1])),flush=True)
    verify_cover(doc,args.left,RIGHT)
    doc["complete"]=doc["failure"] is None and not doc["pending"]
    doc["coefficient_cover_complete"]=doc["complete"]
    doc["covered_interval"]=[str(args.left),doc["rows"][-1]["interval"][1] if doc["rows"] else str(args.left)]
    doc["all_closed_box_speeds_positive"]=all(
        box_from_record(r["bounds"]["radial_speed"])>0 for r in doc["rows"])
    doc["physical_angle_chart_certified_on_covered_interval"]=all(
        r["physical_inverse_gap_certified"] for r in doc["rows"])
    run["new_rows"]=added
    run["wall_seconds"]=time.monotonic()-start
    save(args.out,doc)
    print(json.dumps(dict(complete=doc["complete"],rows=len(doc["rows"]),new_rows=added,
        pending=len(doc["pending"]),failure=doc["failure"],out=str(args.out))),flush=True)
    if doc["failure"] is not None:
        raise RuntimeError("the actual coefficient gate failed; the failed report is preserved")


if __name__ == "__main__":
    main()
