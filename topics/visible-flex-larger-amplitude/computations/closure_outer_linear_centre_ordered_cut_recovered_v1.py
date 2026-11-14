#!/usr/bin/env python3
"""Fresh exact ordered audit of the R88 true linear-centre source.

This is a NEW recovery consumer, not a claimed copy of any lost file.
Only standard-library rational arithmetic is used.  The source is the
executed L_R + C_rest* centre, not the old R79 candidate.  Its parameter
variation is paid separately by the certified complete source derivative.
No ODE, source integral, mean-root evaluation or Arb job is launched.
"""
from __future__ import annotations
import argparse
from decimal import Decimal, localcontext
from fractions import Fraction as F
import gzip
import json
from pathlib import Path
import resource
import sys
import tempfile
import time

from closure_split_joint_io_v2 import read, iter_array, digest

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

MODES = (2, 4)
ORIGINAL = list(range(2, 41, 2))
ZERO = (F(0), F(0))
FIELDS_SHA = "0828f8597f2847c2a321d8e2804a9ff21e0084ec1abb1c80421ba303ab659b20"
FROZEN = {
    "profiles": "b67e06912449b95cb99f84bb6969f34d10f11bf70e8bb798634bc3252ee476d6",
    "green": "7c2425f35a5d1a972a6a112e34ab7cf8bc2a0edf28e17a20bf6a86a48d805d00",
    "ball": "027311615c86e468be9a1f4b53f594a2d88192dd7760537b190f818b6a0d0a67",
    "inner_head": "9e891098dd625f7418c48d91ee92db900bd7b0d1c44b2b69c1cdebbd8d03c930",
    "family": "17b1d776cdce044722db61c2981d64838d18fd66c6ef3fdd4c48fa183a9a3776",
    "linear": "80e3d069ee7484702db7a06601db66db25f446c4efae9d53a24a3fc5864e0a95",
}
GEOMETRY_SOURCE = "c48606c4e127fb0d3f27479eeed11bff3c5cb69139148633ea4f74a9e1f63829"
BUDGET_SOURCE = "e2113502398ebb1d4649a82a813ef0d6f2f90802ef9da52cbac8e37d36a39d83"
IO_SHA = "6cbcb8cf69a39d8df5d10be35a29b941b47fd66456364eb90fab7bbb22b386f0"


def p2(n):
    return F(1 << n) if n >= 0 else F(1, 1 << (-n))


def point(v):
    if isinstance(v, int):
        return F(v)
    if isinstance(v, str):
        return F(v)
    if isinstance(v, F):
        return v
    if isinstance(v, list) and len(v) == 2 and all(isinstance(x, int) for x in v):
        return F(v[0]) * p2(v[1])
    if isinstance(v, dict):
        if "numerator" in v:
            return F(int(v["numerator"]), int(v["denominator"]))
        if "mantissa" in v:
            return F(int(v["mantissa"])) * p2(int(v["binary_exponent"]))
        if "lower" in v and "upper" in v:
            a, b = point(v["lower"]), point(v["upper"])
            if a != b:
                raise ValueError("An exact scalar was required")
            return a
    raise ValueError("Unknown exact scalar representation")


def pair(v):
    if isinstance(v, dict) and "lower" in v and "upper" in v:
        out = point(v["lower"]), point(v["upper"])
    elif isinstance(v, list) and len(v) == 2 and not all(isinstance(x, int) for x in v):
        out = point(v[0]), point(v[1])
    else:
        z = point(v)
        out = z, z
    if out[0] > out[1]:
        raise ValueError("Reversed exact interval")
    return out


def up(v):
    return pair(v)[1]


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def sub(a, b):
    return a[0] - b[1], a[1] - b[0]


def mul(a, b):
    z = [x*y for x in a for y in b]
    return min(z), max(z)


def div(a, b):
    if b[0] <= 0 <= b[1]:
        raise ArithmeticError("True global denominator contains zero")
    return mul(a, (1/b[1], 1/b[0]))


def norm(a):
    return max(abs(a[0]), abs(a[1]))


def minimum_abs(a):
    if a[0] <= 0 <= a[1]:
        raise ArithmeticError("True global denominator contains zero")
    return min(abs(a[0]), abs(a[1]))


def intersection(a, b):
    z = max(a[0], b[0]), min(a[1], b[1])
    if z[0] > z[1]:
        raise ArithmeticError("Proven representations of one true datum are disjoint")
    return z


def remove_summand(total, part):
    # Both endpoints are sums of the same independent contribution intervals.
    # This removes a stored summand; it is not independent interval subtraction.
    z = total[0] - part[0], total[1] - part[1]
    if z[0] > z[1]:
        raise ArithmeticError("Exact source-suffix subtraction lost a summand")
    return z


def rec(x):
    x = F(x)
    with localcontext() as c:
        c.prec = 28
        text = str(Decimal(x.numerator)/Decimal(x.denominator))
    return {"numerator": str(x.numerator), "denominator": str(x.denominator),
            "display_only": text}


def interval(a):
    return {"lower": rec(a[0]), "upper": rec(a[1])}


def exp_bounds(x, order=64):
    if not 0 <= x <= 2:
        raise ValueError("Declared rational exponential range exceeded")
    term = F(1)
    total = term
    for k in range(1, order+1):
        term *= x/k
        total += term
    nxt = term*x/(order+1)
    return total, total+nxt/(1-x/(order+2))


def integral(kernel, N):
    signed = pair(kernel["signed"])
    mass = point(kernel["absolute"])
    if mass < 0:
        raise ArithmeticError("A positive source-kernel mass is negative")
    mid, rad = (N[0]+N[1])/2, (N[1]-N[0])/2
    return add(mul((mid, mid), signed), (-rad*mass, rad*mass)), mass*norm(N)


def save(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    encoded = (json.dumps(data, separators=(",", ":"), ensure_ascii=False)+"\n").encode()
    if len(encoded) > 1000000:
        path = Path(str(path)+".gz")
        packed = gzip.compress(encoded, mtime=0)
    else:
        packed = encoded
    if len(packed) >= 5*1024*1024:
        raise ValueError("A complete primary exceeds the repository size gate")
    if path.exists():
        raise FileExistsError("Never overwrite a completed or failed audit")
    tmp = Path(str(path)+".partial")
    tmp.write_bytes(packed)
    tmp.replace(path)
    return path


def forward_rows(group, spool_dir):
    with tempfile.TemporaryFile(mode="w+b", dir=spool_dir) as out:
        offsets = []
        for row in iter_array(Path(group["path"]), "panels"):
            offsets.append(out.tell())
            out.write(json.dumps(row, separators=(",", ":")).encode()+b"\n")
        if len(offsets) != group["subpanels"]:
            raise ValueError("Missing whole source-profile group")
        for at in reversed(offsets):
            out.seek(at)
            yield json.loads(out.readline())


def source_table(group, hashes):
    tab = {}
    right = F(0)
    for chunk in group["chunks"]:
        path = Path(chunk["path"])
        if digest(path) != chunk["sha256"]:
            raise ValueError("Actual linear-centre source chunk changed")
        hashes[str(path)] = chunk["sha256"]
        count = 0
        for row in iter_array(path, "panels"):
            i = row["panel"]
            lo, hi = F(row["x_left"]), F(row["x_right"])
            if (i != len(tab) or row["cell"] != group["cell"]
                    or row["segment"] != group["segment"] or lo != right or not lo < hi):
                raise ValueError("Actual centre-source positions are incomplete")
            V = pair(row["source_envelope"])
            if V[0] != V[1] or V[0] <= 0:
                raise ArithmeticError("The exact original positive V is required")
            values = {r["mode"]: pair(r["complete_source_cosine"])
                      for r in row["selected_cosine_sources"]}
            if sorted(values) != list(MODES):
                raise ValueError("Both selected complete signed source modes are required")
            tab[i] = (lo, hi, V[0], values)
            right = hi
            count += 1
        if count != chunk["panels"]:
            raise ValueError("Source chunk count differs")
    if len(tab) != group["panels"] or right != 1:
        raise ValueError("Complete actual source segment [0,1] was not preserved")
    return tab


def local_source(tab, row):
    lo, hi, V, values = tab[row["panel"]]
    x, y = F(row["x_left"]), F(row["x_right"])
    if not lo <= x < y <= hi or pair(row["source_envelope"]) != (V, V):
        raise ValueError("The true profile/source position or exact V differs")
    return V, values


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for key in ("source-summary", "profiles", "green", "ball", "inner-head",
                "family", "linear", "out-prefix"):
        ap.add_argument("--"+key, type=Path, required=True)
    ap.add_argument("--physical-budget", type=Path)
    ap.add_argument("--physical-geometry", type=Path)
    ap.add_argument("--fields-source-sha256", default=FIELDS_SHA)
    ap.add_argument("--parameter-radius", default="3/4")
    ap.add_argument("--rss-kib", type=int, default=98304)
    ap.add_argument("--prepare-only", action="store_true")
    a = ap.parse_args()
    started = time.monotonic()
    a.out_prefix.parent.mkdir(parents=True, exist_ok=True)
    if any(Path(str(a.out_prefix)+s).exists() for s in
           (".json", ".json.gz", "-summary.json", "-failure.json", "-failure.json.gz")):
        raise FileExistsError("Use a fresh complete R88 source/cut audit prefix")
    if digest(Path(__file__).with_name("closure_split_joint_io_v2.py")) != IO_SHA:
        raise ValueError("The frozen streaming reader changed")
    if bool(a.physical_budget) != bool(a.physical_geometry):
        raise ValueError("Supply the new physical budget and its complete geometry together")
    radius = F(a.parameter_radius)
    if radius != F(3, 4):
        raise ValueError("Retain the actual R78 Cauchy interior parameter radius")
    hashes = {}
    docs = {}
    for key, wanted in FROZEN.items():
        path = getattr(a, key)
        hashes[str(path)] = digest(path)
        if hashes[str(path)] != wanted:
            raise ValueError("Frozen actual input identity changed: "+key)
        docs[key] = read(path)
        if not docs[key]["all_gates"]:
            raise ValueError("An actual input certificate is incomplete: "+key)
    hashes[str(a.source_summary)] = digest(a.source_summary)
    fields = read(a.source_summary)
    if (not fields["all_gates"] or fields["source_sha256"] != a.fields_source_sha256
            or fields["original_panels"] != 10793 or fields["actual_subpanels"] != 10933
            or fields["tau"] != "1/64"):
        raise ValueError("The complete true new-centre source is required")
    profiles, green, oldball, head, family, linear = [
        docs[k] for k in ("profiles", "green", "ball", "inner_head", "family", "linear")]
    for key in ("profiles", "green", "linear"):
        path = getattr(a, key)
        if fields["input_hashes"].get(str(path)) != hashes[str(path)]:
            raise ValueError("The new source uses another true input: "+key)
    for key in ("profiles", "green", "family"):
        path = getattr(a, key)
        if oldball["input_hashes"].get(str(path)) != hashes[str(path)]:
            raise ValueError("R86 uses another actual profile/Green/family")
    if green["input_hashes"].get(str(a.inner_head)) != hashes[str(a.inner_head)]:
        raise ValueError("The complete true-head field lift changed")
    if green["input_hashes"].get(str(a.linear)) != hashes[str(a.linear)]:
        raise ValueError("The affine target and actual linear data changed")
    if head["parameter_axes"] != family["parameter_axes"] or oldball["parameter_axes"] != family["parameter_axes"]:
        raise ValueError("Retain the entire actual R74 twenty-axis family")
    config = profiles["config"]
    if (config["modes"] != list(MODES) or profiles["counts"]["original_material"] != 10793
            or config["input_cutoff"] != 92 or config["field_radius"] != "1/16"
            or point(oldball["radius"]) != 16 or oldball["unknown_outputs"] != list(MODES)):
        raise ValueError("The exact R84/R86 projected field problem changed")
    axes = {r["mode"]: r for r in family["parameter_axes"]}
    if sorted(axes) != ORIGINAL:
        raise ValueError("All twenty original R74 axes must be retained")
    lrows = {r["mode"]: r for r in linear["rows"] if r["endpoint_physical_node"] == 10}
    if sorted(lrows) != list(MODES):
        raise ValueError("Both true physical-node10 affine data are required")
    for m in MODES:
        if pair(lrows[m]["same_exact_saved_cut_Q"]) != pair(axes[m]["exact_centre"]):
            raise ValueError("The frozen head centre differs from the actual candidate cut")
    W = {m: pair(config["true_Wronskians"][str(m)]) for m in MODES}
    Wabs = {m: minimum_abs(W[m]) for m in MODES}
    angular = {m: tuple((1+m)*x for x in exp_bounds(F(m,64))) for m in MODES}
    sourcegroups = {(g["cell"],g["segment"]):g for g in fields["groups"]}
    wanted_order = [(n,j) for n in (11,10) for j in range(9)]
    if [(g["cell"],g["segment"]) for g in profiles["profile_groups"]] != wanted_order:
        raise ValueError("The true outward profile order differs")
    if sorted(sourcegroups) != sorted(wanted_order):
        raise ValueError("All18 true new-source groups are required")
    for g in profiles["profile_groups"]:
        k = g["cell"],g["segment"]
        sg = sourcegroups[k]
        if (sg["profile_sha256"] != g["sha256"] or sg["panels"] != g["original_panels"]
                or sg["subpanels"] != g["subpanels"] or digest(Path(g["path"])) != g["sha256"]):
            raise ValueError("The new source and true whole-field partitions differ")
        hashes[g["path"]] = g["sha256"]
    physical = geometry = None
    if a.physical_budget:
        for path in (a.physical_budget,a.physical_geometry):
            hashes[str(path)] = digest(path)
        physical,geometry = read(a.physical_budget),read(a.physical_geometry)
        pc = geometry["config"]
        if (not physical["all_gates"] or not geometry["all_gates"]
                or physical["entrypoint_sha256"] != BUDGET_SOURCE
                or pc["entrypoint_sha256"] != GEOMETRY_SOURCE
                or physical["geometry_sha256"] != hashes[str(a.physical_geometry)]
                or pc["parameter_sigma"] != "17/16" or pc["source_tau"] != "1/64"
                or pc["modes"] != list(range(2,93,2))):
            raise ValueError("The full same-norm weak physical budget is required")
        for marker in ("closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json",
                       "closure-outer-source-cell11-r1-summary.json",
                       "closure-outer-source-cell10-refined-moments-r1-summary.json"):
            matches = [(p,h) for p,h in profiles["input_hashes"].items() if p.endswith(marker)]
            if len(matches) != 1 or pc["input_hashes"].get(matches[0][0]) != matches[0][1]:
                raise ValueError("The physical weak kernel has a different true source")
        if pc["input_hashes"].get(str(a.family)) != hashes[str(a.family)]:
            raise ValueError("The physical weak axes changed")
        intersection(pair(pc["actual_true_cut_radius"]), pair(config["cut_radius"]))
        intersection(pair(pc["global_mu11"]), pair(config["global_mu_star"]))
        for m in MODES:
            if pair(pc["actual_outer_Q"][str(m)]) != pair(lrows[m]["exact_saved_outer_candidate_Q"]):
                raise ValueError("The two physical/canonical affine targets differ")
    def guard():
        peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if peak > a.rss_kib:
            raise MemoryError("Observed ordered R88 RSS exceeds declared threshold: "+str(peak))
    plan = {"status":"Prepared exact new-centre ordered audit, no execution claim",
            "input_hashes":dict(hashes),"source_sha256":digest(__file__),
            "fields_source_sha256":a.fields_source_sha256,"selected_modes":list(MODES),
            "parameter_radius":str(radius),"same_real_metric_and_original_V":True,
            "no_Arb_no_ODE_no_new_source_integral":True,"rss_kib":a.rss_kib}
    save(str(a.out_prefix)+"-plan.json",plan)
    if a.prepare_only:
        print(json.dumps({"prepared":True,"out_prefix":str(a.out_prefix)}),flush=True)
        return
    total = {m:{z:{"signed":ZERO,"absolute":F(0),"old_derivative":F(0)}
                for z in ("phi","chi")} for m in MODES}
    groups = []
    processed = 0
    try:
        # New N is joined by its exact original leaf. Old candidate N is never used.
        for g in profiles["profile_groups"]:
            sg = sourcegroups[g["cell"],g["segment"]]
            tab = source_table(sg,hashes)
            recent = {m:{z:{"signed":ZERO,"absolute":F(0),"old_derivative":F(0)}
                         for z in ("phi","chi")} for m in MODES}
            right = F(1)
            count = 0
            for row in iter_array(Path(g["path"]),"panels"):
                if F(row["x_right"]) != right:
                    raise ValueError("Actual reverse profile cover has a gap")
                right = F(row["x_left"])
                V,N = local_source(tab,row)
                d = point(row["whole_low46_source_derivative_density"])
                if d < 0:
                    raise ArithmeticError("Old derivative source density is negative")
                if [x["mode"] for x in row["modes"]] != list(MODES):
                    raise ValueError("A complete selected physical profile is missing")
                for p in row["modes"]:
                    m = p["mode"]
                    for z in ("phi","chi"):
                        value,absolute = integral(p["integrals"][z],N[m])
                        derivative = point(p["integrals"][z]["absolute"])*d
                        for acc in (total[m][z],recent[m][z]):
                            acc["signed"] = add(acc["signed"],value)
                            acc["absolute"] += absolute
                            acc["old_derivative"] += derivative
                count += 1
                processed += 1
                if processed % 128 == 0:
                    guard()
            if count != g["subpanels"] or right != 0:
                raise ValueError("Incomplete actual ordered first pass")
            groups.append({"cell":g["cell"],"segment":g["segment"],"subpanels":count,
                           "integrals":{str(m):{z:{"signed":interval(v["signed"]),
                               "absolute":rec(v["absolute"]),"old_derivative":rec(v["old_derivative"])}
                               for z,v in r.items()} for m,r in recent.items()}})
            del tab
        if processed != 10933:
            raise ValueError("The full original actual profile count is required")
        print(json.dumps({"event":"r88_actual_source_totals_complete","subpanels":processed,
                           "seconds":time.monotonic()-started}),flush=True)
        prefix = {m:ZERO for m in MODES}
        suffix = {m:total[m]["chi"]["signed"] for m in MODES}
        maximum = {m:{z:F(0) for z in ("P","K")} for m in MODES}
        where = {m:{z:None for z in ("P","K")} for m in MODES}
        visited = 0
        for g in profiles["profile_groups"]:
            tab = source_table(sourcegroups[g["cell"],g["segment"]],hashes)
            right = F(0)
            count = 0
            for row in forward_rows(g,a.out_prefix.parent):
                if F(row["x_left"]) != right:
                    raise ValueError("Actual forward profile cover has a gap")
                right = F(row["x_right"])
                V,N = local_source(tab,row)
                for p in row["modes"]:
                    m = p["mode"]
                    pv,pa = integral(p["integrals"]["phi"],N[m])
                    cv,ca = integral(p["integrals"]["chi"],N[m])
                    after = remove_summand(suffix[m],cv)
                    leftpart = add(prefix[m],(-pa,pa))
                    rightpart = add(after,(-ca,ca))
                    for k,z in enumerate(("P","K")):
                        fp,cp = pair(p["phi_physical_PK"][k]),pair(p["chi_physical_PK"][k])
                        response = div(add(mul(cp,leftpart),mul(fp,rightpart)),W[m])
                        bound = angular[m][1]*norm(response)/V
                        if bound > maximum[m][z]:
                            maximum[m][z] = bound
                            where[m][z] = {"cell":g["cell"],"segment":g["segment"],
                                "panel":row["panel"],"subpanel":row["subpanel"],
                                "x_left":row["x_left"],"x_right":row["x_right"]}
                    prefix[m] = add(prefix[m],pv)
                    suffix[m] = after
                count += 1
                visited += 1
                if visited % 128 == 0:
                    guard()
            if count != g["subpanels"] or right != 1:
                raise ValueError("Incomplete actual ordered second pass")
            del tab
        if visited != processed or any(suffix[m] != ZERO or
                prefix[m] != total[m]["phi"]["signed"] for m in MODES):
            raise ArithmeticError("The complete signed prefix/suffix identities failed")
        g0 = sum(sum(v.values()) for v in maximum.values())
        oldgamma = up(oldball["enlarged_complete_source_derivative_Green_upper"])
        gamma = oldgamma
        gamma_candidates = {"R86_complete_strong_rho16":rec(oldgamma)}
        newrows = {}
        if physical:
            d = next(r for r in physical["densities"] if r["density"]=="weak_local_rho_16")
            if not d["all_input_frequencies_allowed"]:
                raise ValueError("Weak derivative must retain all input frequencies")
            newgamma = point(d["selected_m2_m4_sum"])
            gamma_candidates["actual_physical_weak_rho16"] = rec(newgamma)
            gamma = min(gamma,newgamma)
            newrows = {r["mode"]:next(v for v in r["densities"]
                        if v["density"]=="weak_local_rho_16") for r in physical["mode_rows"] if r["mode"] in MODES}
            if sorted(newrows) != list(MODES):
                raise ValueError("Both weak physical cut rows are required")
        if not 0 <= gamma < 1:
            raise ArithmeticError("No valid strict projected field contraction")
        mass = fields["original_mode_component_mass"]
        if sorted(map(int,mass)) != ORIGINAL:
            raise ValueError("All original mode masses must be retained")
        delta = sum(radius*up(axes[m]["relative_radius"])*
                    (up(mass[str(m)]["P"])+up(mass[str(m)]["K"]))
                    for m in ORIGINAL if m not in MODES)
        headfield = up(green["sums"]["true_head_value_lift"])
        headD = up(green["sums"]["true_head_parameter_derivative_lift"])
        zeta = (g0+gamma*delta+headfield)/(1-gamma)
        image86 = up(oldball["projected_map_full_ball_upper"])
        triangle86 = up(oldball["linear_lift_minus_candidate_triangle_upper"])
        line_domain = triangle86 < 16 and image86+delta < 16
        direct = {r["mode"]:r["normalized_inner_nonlinear_feedback"]
                  for r in head["actual_selected_boundary_feedback_rows"]
                  if r["endpoint_physical_node"] == 10}
        if sorted(direct) != list(MODES):
            raise ValueError("Complete actual-node10 head beta feedback required")
        K16 = up(oldball["derivative_density_multiplier"])
        cutrows = []
        for m in MODES:
            axis = point(axes[m]["half_axis"])
            if axis <= 0:
                raise ValueError("The actual R74 canonical axis is positive")
            I0 = div(total[m]["chi"]["signed"],W[m])
            qlinear = div(pair(lrows[m]["exact_saved_outer_candidate_Q"]),
                          pair(lrows[m]["same_true_S0_Q"]))
            centre = sub(add(qlinear,I0),pair(axes[m]["exact_centre"]))
            Dold = K16*total[m]["chi"]["old_derivative"]/(Wabs[m]*angular[m][0]*axis)
            Dcut = Dold
            dcandidates = {"R86_complete_strong_rho16":rec(Dold)}
            if physical:
                Dnew = point(newrows[m]["canonical_cut_original_axis_ratio"])
                dcandidates["actual_physical_weak_rho16"] = rec(Dnew)
                Dcut = min(Dcut,Dnew)
            hvalue = up(direct[m]["uniform_value_upper"])
            hderiv = up(direct[m]["first_derivative_linf_to_output_upper"])
            central = norm(centre)/axis
            nonlinear_error = Dcut*(zeta+delta)
            image = central+nonlinear_error+hvalue
            # Other18 parameters are held fixed. Selected centre eta does
            # not occur in the absolute field representation L_R+G N+B beta.
            lip = Dcut*headD/(1-gamma)+hderiv
            cutrows.append({"mode":m,"canonical_axis":rec(axis),
                "exact_saved_cut_centre":axes[m]["exact_centre"],
                "complete_signed_source_I0":interval(I0),
                "exact_linear_cut_from_fixed_outer_target":interval(qlinear),
                "signed_centre_residual_canonical_Q":interval(centre),
                "centre_residual_axis_upper":rec(central),
                "complete_cut_derivative_candidates":dcandidates,
                "chosen_complete_cut_derivative_upper":rec(Dcut),
                "unknown_field_and_rest_cut_error_upper":rec(nonlinear_error),
                "complete_direct_head_value_axis_upper":rec(hvalue),
                "complete_direct_head_selected_derivative_upper":rec(hderiv),
                "cut_parameter_map_image_upper":rec(image),
                "selected_parameter_row_lipschitz_upper":rec(lip),
                "self_map_on_radius_three_quarters":image <= radius,
                "strict_selected_parameter_lipschitz":lip < 1})
        selfmap = all(r["self_map_on_radius_three_quarters"] for r in cutrows)
        contraction = all(r["strict_selected_parameter_lipschitz"] for r in cutrows)
        structural = dict(all10793_original_positions_and10933_true_subpanels=True,
            same_fixed_metric_original20_modes_and_actual_R74_axes=True,
            complete_new_centre_mean_and_Wiener_inverse_source=True,
            exact_signed_prefix_suffix_and_partial_same_panel_bounds=True,
            both_physical_component_suprema_precede_sum=True,
            source_is_LR_plus_original_rest_not_old_R79=True,
            source_parameter_variation_paid_separately_by_actual_mode_masses=True,
            selected_parameter_candidate_dependence_cancels_in_absolute_field=True,
            complete_true_head_value_and_derivative_and_direct_cut_lift=True,
            no_Arb_no_ODE_no_new_source_integral=True)
        mathematical = dict(common_complete_rho16_line_domain=line_domain,
            conditional_field_contraction=gamma < 1,
            both_selected_cut_self_maps=selfmap,
            strict_selected_cut_contraction=contraction)
        result = {"status":"Completed actual two-mode centre/source/cut audit; mathematical gates explicit",
            "author":"exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12",
            "calculation_complete":True,"structural_gates":structural,
            "mathematical_gates":mathematical,
            "all_gates":all(structural.values()) and all(mathematical.values()),
            "conditional_selected_cut_existence_paid":line_domain and selfmap and contraction,
            "parameter_radius":str(radius),"other18_parameters_fixed_but_uniform_in_same_radius":True,
            "physical_norm":oldball["physical_norm"],
            "complete_new_centre_response_upper":rec(g0),
            "complete_new_centre_component_responses":{str(m):{z:{"bound":rec(v),
                "maximizer":where[m][z]} for z,v in row.items()} for m,row in maximum.items()},
            "rest_parameter_field_difference_upper":rec(delta),
            "complete_projected_derivative_candidates":gamma_candidates,
            "chosen_complete_projected_derivative":rec(gamma),
            "complete_head_field_value_upper":rec(headfield),
            "complete_head_field_selected_derivative_upper":rec(headD),
            "absolute_field_departure_from_LR_upper":rec(zeta),
            "domain_accounting":{"reference_LR_to_selected_candidate_triangle_upper":rec(triangle86),
                "actual_R86_image_plus_rest_delta_upper":rec(image86+delta),
                "radius":16,"connected_domain_gate":line_domain},
            "cut_rows":cutrows,"group_source_integrals":groups,
            "source_profile_subpanels":processed,"source_original_panels":10793,
            "all46_cut_consistency_paid":False,"high_frequency_outer_PDE_paid":False,
            "full_outer_or_closed_surface_claimed":False,
            "input_hashes":hashes,"source_sha256":digest(__file__),
            "fields_source_sha256":fields["source_sha256"],
            "elapsed_seconds":time.monotonic()-started,
            "peak_RSS_KiB":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
        guard()
        out = save(str(a.out_prefix)+".json",result)
        summary = {k:v for k,v in result.items() if k not in
                   ("group_source_integrals","input_hashes","complete_new_centre_component_responses")}
        summary["primary"] = {"path":str(out),"sha256":digest(out)}
        summary_out = save(str(a.out_prefix)+"-summary.json",summary)
        print(json.dumps({"event":"r88_complete_ordered_centre_cut_audit",
            "primary":str(out),"summary":str(summary_out),"all_gates":result["all_gates"],
            "mathematical_gates":mathematical,"source_bound":float(g0),
            "field_departure":float(zeta),"rest_delta":float(delta),
            "gamma":float(gamma),"seconds":result["elapsed_seconds"],
            "peak_RSS_KiB":result["peak_RSS_KiB"]}),flush=True)
    except BaseException as err:
        save(str(a.out_prefix)+"-failure.json",{
            "status":"Incomplete new-centre audit; not a mathematical impossibility claim",
            "error":type(err).__name__+": "+str(err),"processed_first_pass_subpanels":processed,
            "input_hashes":hashes,"source_sha256":digest(__file__),
            "elapsed_seconds":time.monotonic()-started,
            "peak_RSS_KiB":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss})
        raise


if __name__ == "__main__":
    main()
