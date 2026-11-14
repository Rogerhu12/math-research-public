#!/usr/bin/env python3
"""Full continuous R64 scan of a nine-piece compatible outer-cell height.

The ten physical endpoint jets are shared exactly by definition. Existing
true source panels are reweighted by the five positive local-x Hermite
bases. The actual candidate K_x comes from those polynomials. Full mean
and full Darboux source use R64, without assuming the R33 small ball.
No Node, new source quadrature, radial ODE, or BVP is started.
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
from closure_split_joint_io import read, digest, iter_array
from tail_r33_middle_ordered_physical import SourceValues
from tail_outer_positive_moment_panels import (
    MOMENT_KEYS, BASIS_CAPS, Subdivide, positive_hull, add_moments, zero_moments)
from tail_outer_weighted_compatible import (
    intersection, positive_basis, normalized_endpoint_jet,
    make_weighted_candidate, weighted_panel_fields)
from tail_outer_general_mean_bounds import general_mean_and_defect


def primitive(u):
    return {"00":u-u**3+u**4/2,
            "10":u*u/2-2*u**3/3+u**4/4,
            "01":u**3-u**4/2,
            "11":u**3/3-u**4/4,
            "b":u**3/3-u**4/2+u**5/5}


def local_moments(row):
    """Same true measure w dr, now with the local original-segment bases."""
    a, b = F(row["x_left"]), F(row["x_right"])
    if not 0 <= a < b <= 1:
        raise ValueError("A complete positive local source interval is required")
    rx, w, width = (ball(row[key]) for key in ("radius_x", "w", "width"))
    if not all(v > 0 for v in (rx, w, width)):
        raise ArithmeticError("The real source measure lost positivity")
    left, right = primitive(a), primitive(b)
    u = exact_q(a).union(exact_q(b))
    basis = positive_basis(u)
    out = {}
    for key in MOMENT_KEYS:
        integral = exact_q(right[key]-left[key])
        if not integral > 0:
            raise ArithmeticError("An exact positive polynomial integral was lost")
        # Integrating the polynomial basis exactly gives a strict lower
        # bound even for a constant-source panel covering the whole [0,1].
        lower = (rx.lower()*w.lower()*integral.lower()).lower()
        upper = (rx.upper()*w.upper()*integral.upper()).upper()
        blo = max(arb(0), basis[key].lower())
        bup = min(exact_q(BASIS_CAPS[key]).upper(), basis[key].upper())
        # Independently retain the original actual physical-width bound.
        lower = max(lower, (width.lower()*w.lower()*blo).lower())
        upper = min(upper, (width.upper()*w.upper()*bup).upper())
        out[key] = positive_hull(lower, upper, strict=True)
    return out


def endpoint(cell, segment_index, side, node):
    x = F(side)
    s = cell.segments[segment_index]
    kind = cell.classify(s, x, x)
    if kind is None:
        raise ArithmeticError("A local original endpoint branch is unresolved")
    logw, ell = cell.profile(s, exact_q(x), kind[0])
    w = logw.exp()
    rx = cell.integrand(s, exact_q(x), kind[0], kind[1])
    intersection(w, ball(node["w"]))
    intersection(w*ell/rx, ball(node["wr"]))
    jets = {key:{int(m):ball(value) for m,value in node["shared_physical_jets"][key].items()}
            for key in ("H", "Hr", "Hrr")}
    return normalized_endpoint_jet(jets["H"], jets["Hr"], jets["Hrr"],
                                   w=w, radius_u=rx, log_w_u=ell)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ("cell-manifest", "nodes", "ready", "out"):
        p.add_argument("--"+name, type=Path, required=True)
    p.add_argument("--rss-limit-mib", type=int, default=40)
    args = p.parse_args()
    if args.out.exists():
        raise FileExistsError("Use a fresh piecewise candidate output")
    ctx.prec = 192
    started = time.monotonic()
    def memory_gate(stage):
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 1024*args.rss_limit_mib:
            raise MemoryError("The owned piecewise R64 scan exceeded its RSS cap at "+stage)
    paths = (args.cell_manifest, args.nodes, args.ready)
    hashes = {str(path):digest(path) for path in paths}
    material, nodes, ready = map(read, paths)
    if (not all(material["checks"].values())
            or not nodes["complete_original_segment_node_cover"]
            or not nodes["saved_cut_height_exactly_preserved"]):
        raise ValueError("Complete true panels and shared ten-node data are required")
    for path in (args.cell_manifest, args.ready):
        if nodes["input_hashes"].get(str(path)) != hashes[str(path)]:
            raise ValueError("The shared nodes belong to another actual source or material")
    n, tau, modes = material["cell"], F(nodes["tau"]), nodes["modes"]
    if nodes["cell"] != n or [row["point"] for row in nodes["rows"]] != list(range(10)):
        raise ValueError("The shared point ordering changed")
    if sorted(g["source_segment"] for g in material["groups"]) != list(range(9)):
        raise ValueError("All nine true original segments are required")
    head = SourceValues(ready)
    head.params = ready["rationalDeepModel"]["physicalParameters"]
    cell = OuterCell(head, n)
    weights = {m:((1+m)*(exact_q(tau)*m).exp()).upper() for m in modes}
    segments, worst, minima, failed_panels = [], {}, {}, []
    count, failures, abort = 0, 0, None
    def update_max(name, value, witness):
        if name not in worst or value > worst[name]["value"]:
            worst[name] = dict(value=value.upper(), witness=witness)
    def update_min(name, value, witness):
        if name not in minima or value < minima[name]["value"]:
            minima[name] = dict(value=value.lower(), witness=witness)
    try:
        for group in sorted(material["groups"], key=lambda row:row["source_segment"]):
            j, path = group["source_segment"], Path(group["path"])
            if digest(path) != group["sha256"]:
                raise ValueError("A true original source group changed")
            hashes[str(path)] = group["sha256"]
            moments, total = [], zero_moments()
            for row in iter_array(path, "panels"):
                mm = local_moments(row)
                moments.append(mm)
                total = add_moments(total, mm)
                if len(moments) % 128 == 0:
                    memory_gate("local-positive-integrals")
            if len(moments) != group["panels"]:
                raise ValueError("The complete source group was not reweighted")
            suffix = [zero_moments() for unused in range(len(moments)+1)]
            for i in range(len(moments)-1, -1, -1):
                suffix[i] = add_moments(moments[i], suffix[i+1])
            candidate = make_weighted_candidate(endpoint(cell,j,0,nodes["rows"][j]),
                endpoint(cell,j,1,nodes["rows"][j+1]), total)
            prefix, local_count, good, maxR, local_min = zero_moments(), 0, 0, arb(0), None
            for i, g in enumerate(iter_array(path, "panels")):
                after = add_moments(prefix, moments[i])
                before_boxes = {key:positive_hull(prefix[key].lower(), after[key].upper())
                                for key in MOMENT_KEYS}
                after_boxes = {key:positive_hull(suffix[i+1][key].lower(), suffix[i][key].upper())
                               for key in MOMENT_KEYS}
                # Positive true partial integrals may have a slightly
                # negative symmetric radius; use the already proved domain.
                from tail_outer_candidate_domain import nonnegative_integral
                before_boxes = {key:nonnegative_integral(ball_record(value)) for key,value in before_boxes.items()}
                after_boxes = {key:nonnegative_integral(ball_record(value)) for key,value in after_boxes.items()}
                u = exact_q(F(g["x_left"])).union(exact_q(F(g["x_right"])))
                H, K, Kx = weighted_panel_fields(candidate, u=u, u_x=arb(1),
                    prefix_moments=before_boxes, suffix_moments=after_boxes)
                answer = general_mean_and_defect(H,K,Kx,modes=modes,weights=weights,
                    radius=ball(g["radius"]),radius_x=ball(g["radius_x"]),
                    w=ball(g["w"]),log_w_x=ball(g["log_w_x"]))
                witness = dict(segment=j,panel=i,original_parent=g["original_parent"],
                    x_left=g["x_left"],x_right=g["x_right"],radius=g["radius"],w=g["w"])
                R = (answer["norms"][1]["P"]+answer["norms"][1]["K"]).upper()
                maxR = max(maxR,R)
                update_max("R_tau",R,witness)
                for name in ("P","K","T","L","linear"):
                    update_max(name+"_tau",answer["norms"][1][name],witness)
                if answer["gate"]:
                    good += 1
                    for key,value in answer["bounds"].items():
                        update_max(key,value,witness)
                    for key in ("mean_sign_margin","mean_derivative_lower","real_y_lower",
                                "real_N_lower","real_D_lower","real_S_lower","real_L_lower","Wiener_L_lower"):
                        update_min(key,answer[key],witness)
                    if local_min is None or answer["Wiener_L_lower"] < local_min:
                        local_min = answer["Wiener_L_lower"]
                else:
                    failures += 1
                    if len(failed_panels)<32:
                        failed_panels.append(dict(witness=witness,reason=answer["failure"],
                            quadratic_mean=ball_record(answer["quadratic_mean"]),
                            mean_tail=ball_record(answer["mean_tail"]) if "mean_tail" in answer else None,
                            mean_epsilon=ball_record(answer["mean_epsilon"]) if "mean_epsilon" in answer else None,
                            norms=[{key:ball_record(v) for key,v in rr.items()} for rr in answer["norms"]]))
                count, local_count = count+1, local_count+1
                prefix = after
                moments[i], suffix[i] = None, None
                if count%128==0:
                    memory_gate("full-R64-panel")
            if local_count != group["panels"]:
                raise ValueError("A piecewise true source panel was omitted")
            record = dict(segment=j,panels=local_count,general_mean_passed_panels=good,
                all_general_mean_gates=good==local_count,R_tau=ball_record(maxR),
                local_Wiener_L_lower=ball_record(local_min) if local_min is not None else None,
                total_local_positive_moments={key:ball_record(v) for key,v in total.items()},
                bubble_coefficients={str(m):ball_record(v) for m,v in candidate["bubble_coefficient"].items()},
                shared_endpoint_points=[j,j+1])
            segments.append(record)
            print(json.dumps(dict(event="piecewise_R64_segment",cell=n,segment=j,panels=local_count,
                passed=good,R_tau=str(maxR),seconds=time.monotonic()-started,
                peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
            del moments,suffix,candidate
    except (ArithmeticError,ValueError,MemoryError,Subdivide) as error:
        abort = dict(type=type(error).__name__,message=str(error),completed_segments=len(segments),scanned_panels=count)
    complete = abort is None and count==material["panels"] and len(segments)==9
    all_mean = complete and failures==0
    result = dict(status="Complete true-panel R64 scan of the shared-jet nine-piece candidate" if complete else
        "Incomplete piecewise scan; actual failed gate retained",author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",
        cell=n,modes=modes,tau=str(tau),panels=count,segments=segments,abort=abort,
        failed_mean_panels=failures,first_failed_mean_panels=failed_panels,
        gates=dict(complete_same_background_cover=complete,all_general_mean_branches=all_mean,
            all_continuous_full_mean_derivatives=all_mean,all_continuous_Darboux_defects=all_mean),
        worst={key:dict(value=ball_record(row["value"]),witness=row["witness"]) for key,row in worst.items()},
        minima_over_passed_panels={key:dict(value=ball_record(row["value"]),witness=row["witness"]) for key,row in minima.items()},
        first_height_compatibility_exact_by_R48=True,
        shared_nonmean_physical_two_jets=True,saved_true_outer_cut_height_preserved=True,
        mean_scope="R64 complete M(c) and true actual candidate derivative; no R33 small-ball hypothesis",
        local_moment_semantics="Same true w dr measure, original-segment x coordinate; intersect exact polynomial primitive times the real density range with original physical-width times basis range",
        partial_defect_scope="Worst defect fields cover only panels whose full general mean gate passed unless all four gates are true",
        exact_radial_solution_claimed=False,new_source_quadrature=0,new_Node_or_BVP=False,
        input_hashes=hashes,source_hashes={name:digest(Path(__file__).with_name(name)) for name in (
            Path(__file__).name,"tail_outer_general_mean_bounds.py","tail_outer_weighted_compatible.py",
            "tail_outer_positive_moment_panels.py","tail_outer_candidate_domain.py",
            "closure_real_outer_radius.py","tail_r33_middle_ordered_physical.py")},
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    payload=(json.dumps(result,indent=2)+"\n").encode()
    if len(payload)>=1_000_000:
        raise ValueError("Use a separately compressed whole report if this diagnostic exceeds1MB")
    args.out.write_bytes(payload)
    print(json.dumps(dict(event="complete" if complete else "failed",output=str(args.out),
        gates=result["gates"],failed_mean_panels=failures,abort=abort)),flush=True)
    if abort is not None:
        raise SystemExit(1)


if __name__=="__main__":
    main()
