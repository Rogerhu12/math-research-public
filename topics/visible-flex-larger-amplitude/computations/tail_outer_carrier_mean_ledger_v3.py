#!/usr/bin/env python3
"""Consume complete carrier/physical audits and the selected old mean trace.

Only saved true positive moments and exact directed dyadics are used.
The original 8594-leaf composition remains selected; this program reports
what mean-height shift a replacement would require, without selecting it.
Every new mean root, derivative and complete-domain gate remains intact.
Version 3 applies the complete true-line rational root-difference theorem
and the complete radial root-derivative difference theorem only to the two
new candidates whose full same-location physical two-jets are saved.
No Arb, source evaluation, integration, ODE, BVP or Node is started.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

COMPARISON_SHA = "8e30c100e9428f2c7aeae0efe7e4bd02cf6adf80ab5f43a78179ff9c442b0fb9"
SELECTED_SHA = "dd5e3e74f5707be007d7ed539e1001b33e91205066c7a0c6c1bc95f9c891f179"
SELECTED_RESOURCE_SHA = "9e8d0fe2142ee2aed33b34d7a2e9471818eb635112801c8728843af22e42fcb5"
OLD_SUMMARY_SHA = "806fdb96b9aa6eafd921c07518a5b52218180d2182f7b8d18abb8e3d695638e4"
OLD_RESOURCE_SHA = "912ad6200027fdb445cd3e8636c1f6cd404a3480d2c013b6c4722e6888016820"
OLD_CANDIDATE_SHA = "7da554bdb467fe2b997a01971dd4917003fd5deeb36978e200e1457ea3c8fddf"
PAIR_PROOF_SHA = "f617b8c1063b13ce1da3f0821b5bb4441660d2eaa94b7de5078b7ceab430bb2e"
RADIAL_PROOF_SHA = "d3225e6fd8a4dfef43acee82bdf3b846e3c279dbfd8c242bb1aaaf170f72dc24"


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            h.update(block)
    return h.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open(path, "rt", encoding="utf-8") if path.suffix == ".gz"
          else path.open(encoding="utf-8")) as stream:
        return json.load(stream)


def dyadic(value):
    if isinstance(value, dict):
        m, e = int(value["mantissa"]), int(value["binary_exponent"])
    else:
        m, e = int(value[0]), int(value[1])
    return Q(m)*(Q(2)**e)


def interval(value):
    if isinstance(value, dict):
        pair = dyadic(value["lower"]), dyadic(value["upper"])
    else:
        pair = dyadic(value[0]), dyadic(value[1])
    if pair[0] > pair[1]:
        raise ValueError("A directed interval is reversed")
    return pair


def abs_upper(value):
    lo, hi = interval(value)
    return max(abs(lo), abs(hi))


def difference_upper(a, b):
    al, ah = interval(a)
    bl, bh = interval(b)
    return max(abs(bl-ah), abs(bh-al))


def qr(value):
    return dict(numerator=str(value.numerator), denominator=str(value.denominator),
                decimal_diagnostic=format(float(value), ".17g"))


def upper(record, key):
    value = dyadic(record["bounds_upper"][key])
    if value < 0:
        raise ValueError("A norm upper bound is negative")
    return value


def option(command, key):
    return Path(command[command.index(key)+1])


def formal(resource_path, target, key):
    value = read(resource_path)
    if value["exitcode"] != 0 or value["termination_signal"] is not None:
        raise ValueError("A prerequisite has no formal successful exit")
    actual = option(value["command"], key)
    if key == "--out-prefix":
        actual = Path(str(actual)+"-summary.json")
    if actual != target:
        raise ValueError("A formal resource record belongs to a different result")
    return value["command"]


def require_gates(value):
    if not value.get("gates") or not all(x is True for x in value["gates"].values()):
        raise ValueError("A complete original gate is absent")


def save(path, value):
    if path.exists():
        raise FileExistsError("Use a fresh exact mean ledger")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".tmp")
    with temporary.open("w", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write("\n")
    temporary.replace(path)


def validate_old_primary(part, summary, inputs, rss_check):
    path = Path(part["output"])
    if digest(path) != part["output_sha256"]:
        raise ValueError("The original complete mean primary changed")
    inputs[str(path)] = part["output_sha256"]
    at, stop = Q(part["left"]), Q(part["right"])
    count = 0
    header = trailer = False
    rows = []
    with gzip.open(path, "rt", encoding="utf-8") as stream:
        for line in stream:
            row = json.loads(line)
            if row["kind"] == "header":
                if (header or count or row["part"] != part["part"]
                        or row["input_hashes"] != summary["input_hashes"]
                        or row["source_hashes"] != summary["source_hashes"]):
                    raise ValueError("Original mean primary identity mismatch")
                header = True
                continue
            if row["kind"] == "complete_substage_trailer":
                if (trailer or not row["complete_source_cover"]
                        or row["accepted_panels"] != count
                        or row["part"] != part["part"]):
                    raise ValueError("Original complete mean trailer mismatch")
                trailer = True
                continue
            if (not header or trailer or row["kind"] != "accepted_complete_R64_and_J_panel"
                    or not row["same_candidate_complete_mean"]
                    or any(dyadic(v) <= 0 for v in row["gates_lower"].values())):
                raise ValueError("Original continuous mean/domain proof is incomplete")
            left, right = Q(row["source_left"]), Q(row["source_right"])
            if left != at or not left < right <= stop:
                raise ValueError("The original source partition has a gap or overlap")
            rxlo = interval(row["source"]["radius_x"])[0]
            if rxlo <= 0:
                raise ValueError("Original source-to-physical derivative conversion is absent")
            rows.append(dict(left=left, right=right, panel=count,
                mean=upper(row, "complete_mean_abs"),
                mean_r=upper(row, "complete_mean_source_derivative_abs")/rxlo))
            count += 1
            at = right
            rss_check()
    if not (header and trailer and at == stop and count == part["panels"]):
        raise ValueError("Original complete mean primary did not finish")
    return rows


def primary_rows(part, record, *, moments, inputs, rss_check):
    path = Path(part["path"])
    if digest(path) != part["sha256"]:
        raise ValueError("A new true-moment or audit primary changed")
    inputs[str(path)] = part["sha256"]
    at, stop = Q(part["source_left"]), Q(part["source_right"])
    count = 0
    header = trailer = False
    with gzip.open(path, "rt", encoding="utf-8") as stream:
        for line in stream:
            row = json.loads(line)
            if row["kind"] == "header":
                if (header or count or row["input_hashes"] != record["input_hashes"]
                        or row["source_hashes"] != record["source_hashes"]):
                    raise ValueError("New complete primary identity mismatch")
                if not moments and row["mode"] != record["mode"]:
                    raise ValueError("The candidate mode in its primary changed")
                header = True
                continue
            if row["kind"] == "trailer":
                if trailer or not row["complete"] or row["panels"] != count:
                    raise ValueError("A new complete primary trailer differs")
                trailer = True
                continue
            kind = ("complete_physical_substage_moment_leaf" if moments
                    else "complete_new_physical_substage_R64_J_R77_leaf")
            if (not header or trailer or row["kind"] != kind
                    or row["part"] != part["part"] or row["panel"] != count):
                raise ValueError("An actual primary leaf has a different identity")
            left = Q(row["x_left"] if moments else row["source_left"])
            right = Q(row["x_right"] if moments else row["source_right"])
            if left != at or not left < right <= stop:
                raise ValueError("A new exact continuous cover has a gap or overlap")
            if not moments and (not row["complete_mean"]
                    or row["mode"] != record["mode"]
                    or any(dyadic(v) <= 0 for v in row["gates_lower"].values())):
                raise ValueError("A complete mean or inverse-domain gate is absent")
            count += 1
            at = right
            rss_check()
            yield left, right, row
    if not (header and trailer and at == stop and count == part["panels"]):
        raise ValueError("A new true-moment or audit primary did not finish")


def paired_mean_bound(p, c, moment, modes):
    """M.14 on the true full-state line between two exact complete roots.

    The intermediate states need not be roots. Concavity of A and D and
    affinity of L preserve their real positive lower bounds on this line.
    No complex strip or intermediate Wiener inverse is asserted here.
    """
    ph = p["actual_nonmean_jet_cosine_intervals"]
    ch = c["actual_nonmean_jet_cosine_intervals"]
    if any(len(field[key]) != len(modes) for field in (ph,ch)
           for key in ("H","Kbar","Kbar_r")):
        raise ValueError("Full actual finite jets are required for the paired mean")
    rlo = interval(moment["radius"])[0]
    wlo, whi = interval(moment["w"])
    if rlo <= 0 or wlo <= 0:
        raise ValueError("The paired mean lost its real physical normalization")
    z = whi*whi
    E = 1+z
    normalization = rlo*wlo
    cp, cc = upper(p,"complete_mean_abs"),upper(c,"complete_mean_abs")
    pnorm = max(sum((Q(m)*abs_upper(h) for m,h in zip(modes,field["H"])),Q(0))
                /normalization for field in (ph,ch))
    tnorm = max(sum((Q(m*m)*abs_upper(h) for m,h in zip(modes,field["H"])),Q(0))
                /normalization for field in (ph,ch))
    knorm = max(sum((abs_upper(k) for k in ph["Kbar"]),Q(0))+cp,
                sum((abs_upper(k) for k in ch["Kbar"]),Q(0))+cc)
    eK = sum((difference_upper(a,b) for a,b in zip(ph["Kbar"],ch["Kbar"])),Q(0))
    eP = sum((Q(m)*difference_upper(a,b)
              for m,a,b in zip(modes,ph["H"],ch["H"])),Q(0))/normalization
    eT = sum((Q(m*m)*difference_upper(a,b)
              for m,a,b in zip(modes,ph["H"],ch["H"])),Q(0))/normalization
    a0 = min(dyadic(p["gates_lower"]["real_S_lower"]),
             dyadic(c["gates_lower"]["real_S_lower"]))
    d0 = min(Q(1),dyadic(p["gates_lower"]["real_D_lower"]),
             dyadic(c["gates_lower"]["real_D_lower"]))
    l0 = min(dyadic(p["gates_lower"]["real_L_lower"]),
             dyadic(c["gates_lower"]["real_L_lower"]))
    if min(a0,d0,l0) <= 0:
        raise ValueError("The true-line A/D/L mean denominator is not positive")
    u = z*(2*knorm+knorm*knorm+E*pnorm*pnorm)
    CK = (knorm+E*tnorm)/(d0*d0)+Q(3,2)*u/(d0*d0*d0)
    CT = (knorm+z*pnorm*pnorm)/(a0*d0)+u/(2*d0*d0)
    CP = (E*pnorm*(1+z*(1+knorm)*tnorm/a0)/(d0*d0)
          +2*z*pnorm*(1+knorm)*tnorm/(a0*a0*d0))
    inverse_mean_derivative = E*E/l0
    direct = cp+cc
    comparison = inverse_mean_derivative*(CK*eK+CP*eP+CT*eT)
    best = min(direct,comparison)
    diagnostics = dict(
        complete_mean_abs_sum=qr(direct),
        complete_true_line_rational_difference=qr(comparison),
        same_root_difference_upper=qr(best),
        strictly_improves_sum=comparison<direct,
        true_line_real_A_D_L_lower={k:qr(v) for k,v in dict(A=a0,D=d0,L=l0).items()},
        input_full_norms={k:qr(v) for k,v in dict(P=pnorm,K=knorm,T=tnorm).items()},
        actual_differences={k:qr(v) for k,v in dict(Kbar=eK,P=eP,T=eT).items()},
        rational_coefficients={k:qr(v) for k,v in dict(
            C_K=CK,C_P=CP,C_T=CT,inverse_mean_derivative=inverse_mean_derivative).items()},
        no_intermediate_root_or_complex_inverse_assumed=True,
        zero_means_of_Kbar_and_T_used_exactly=True)
    return best,diagnostics


def product_difference(*factors):
    """A signed product difference bounded by positive telescoping data."""
    total = Q(0)
    for index, (_, change) in enumerate(factors):
        value = change
        for other, (bound, _) in enumerate(factors):
            if other != index:
                value *= bound
        total += value
    return total


def paired_mean_radial_bound(p, c, moment, modes, c_difference):
    """MR.15; both actual full roots and their physical derivatives are retained."""
    ph = p["actual_nonmean_jet_cosine_intervals"]
    ch = c["actual_nonmean_jet_cosine_intervals"]
    fields = (ph,ch)

    def norm(key, order=0):
        return max(sum((Q(m)**order*abs_upper(value)
                        for m,value in zip(modes,field[key])),Q(0))
                   for field in fields)

    def changed(key, order=0):
        return sum((Q(m)**order*difference_upper(a,b)
                    for m,a,b in zip(modes,ph[key],ch[key])),Q(0))

    rlo = interval(moment["radius"])[0]
    wlo,whi = interval(moment["w"])
    wr = abs_upper(moment["wr"])
    if min(rlo,wlo) <= 0:
        raise ValueError("The radial mean difference lost its true normalization")
    z,E = whi*whi,1+whi*whi
    normalization = rlo*wlo
    cp,cc = upper(p,"complete_mean_abs"),upper(c,"complete_mean_abs")
    crp,crc = (upper(p,"complete_mean_source_derivative_abs"),
               upper(c,"complete_mean_source_derivative_abs"))
    pnorm,tnorm = norm("H",1)/normalization,norm("H",2)/normalization
    knorm = max(sum((abs_upper(v) for v in ph["Kbar"]),Q(0))+cp,
                sum((abs_upper(v) for v in ch["Kbar"]),Q(0))+cc)
    eK = changed("Kbar")+c_difference
    eP,eT = changed("H",1)/normalization,changed("H",2)/normalization
    a = min(dyadic(p["gates_lower"]["real_S_lower"]),
            dyadic(c["gates_lower"]["real_S_lower"]))
    d = min(Q(1),dyadic(p["gates_lower"]["real_D_lower"]),
            dyadic(c["gates_lower"]["real_D_lower"]))
    l = min(dyadic(p["gates_lower"]["real_L_lower"]),
            dyadic(c["gates_lower"]["real_L_lower"]))
    if min(a,d,l) <= 0:
        raise ValueError("The radial paired mean real A/D/L gate failed")

    Y = 1+knorm
    U,dU = Y*tnorm,tnorm*eK+Y*eT
    p2,dp2 = pnorm*pnorm,2*pnorm*eP
    dmag,dd = 2*knorm+knorm*knorm+E*p2,2*Y*eK+E*dp2
    emag,de = dmag+z*p2,dd+z*dp2
    dA,dD = z*dp2,z*dd
    L,dL = Y+E*tnorm,eK+E*eT
    A1,A2 = (1/a,dA/(a*a)),(1/(a*a),2*dA/(a*a*a))
    F1,F3 = (1/d,dD/(2*d*d)),(1/(d*d),Q(3,2)*dD/(d*d*d))
    j = 1/(1+d)
    dJ = j*j*dD/(2*d)
    J,B = (j,dJ),(2*j-j*j,2*dJ)
    N = (1+z*U/a,z*(dU/a+U*dA/(a*a)))
    dBK = product_difference((L,dL),F3)
    dBT = product_difference((Y,eK),A1,F1)
    dBP = (E*product_difference((pnorm,eP),N,F3)
            +2*z*product_difference((pnorm,eP),(U,dU),A2,F1))
    dGz = (product_difference((U,dU),(p2,dp2),A2,F1)
           +product_difference((U,dU),(emag,de),A1,F3)/2
           +product_difference((p2,dp2),F1,J)
           +product_difference((dmag,dd),(emag,de),F3,B)/2)

    u = z*dmag
    CK = (knorm+E*tnorm)/(d*d)+Q(3,2)*u/(d*d*d)
    CT = (knorm+z*p2)/(a*d)+u/(2*d*d)
    CP = (E*pnorm*(1+z*Y*tnorm/a)/(d*d)
          +2*z*pnorm*Y*tnorm/(a*a*d))
    alpha = 1/rlo+wr/wlo
    RK,eKr = norm("Kbar_r"),changed("Kbar_r")
    RP = norm("Kbar",1)/rlo+alpha*pnorm
    RT = norm("Kbar",2)/rlo+alpha*tnorm
    ePr = changed("Kbar",1)/rlo+alpha*eP
    eTr = changed("Kbar",2)/rlo+alpha*eT
    zr = 2*whi*wr
    F_difference = (dBK*RK+CK*eKr+dBP*RP+CP*ePr
                    +dBT*RT+CT*eTr+zr*dGz)
    direct = crp+crc
    comparison = E*E/l*(F_difference+dBK*min(crp,crc))
    best = min(direct,comparison)
    record = dict(
        complete_mean_radial_derivative_abs_sum=qr(direct),
        complete_true_root_radial_difference=qr(comparison),
        same_root_radial_difference_upper=qr(best),
        strictly_improves_sum=comparison<direct,
        true_line_real_A_D_L_lower={key:qr(v) for key,v in dict(A=a,D=d,L=l).items()},
        full_root_and_field_differences={key:qr(v) for key,v in
            dict(c=c_difference,K=eK,P=eP,T=eT,Kbar_r=eKr,P_r=ePr,T_r=eTr).items()},
        radial_field_norms={key:qr(v) for key,v in
            dict(Kbar_r=RK,P_r=RP,T_r=RT,z_r=zr,alpha=alpha).items()},
        complete_coefficient_differences={key:qr(v) for key,v in
            dict(B_K=dBK,B_P=dBP,B_T=dBT,G_z=dGz).items()},
        numerator_difference_upper=qr(F_difference),
        all_four_complete_G_z_terms_retained=True,
        mean_zero_subtractions_exact=True,
        shared_background_difference_not_charged_twice=True,
        candidate_actual_second_derivatives_used=True,
        no_third_radial_derivative_or_PDE_jet_substitution=True)
    return best,record


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ("selected-composition", "selected-resource", "original-summary",
                 "original-resource", "physical-summary", "physical-resource",
                 "carrier-summary", "carrier-resource", "comparison",
                 "comparison-resource", "out-prefix"):
        ap.add_argument("--"+name, type=Path, required=True)
    ap.add_argument("--rss-limit-mib", type=int, default=96)
    args = ap.parse_args()
    summary_path = Path(str(args.out_prefix)+"-summary.json")
    if summary_path.exists():
        raise FileExistsError("Use a fresh complete mean ledger prefix")
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    began = time.monotonic()

    def memory():
        rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if rss > 1024*args.rss_limit_mib:
            raise MemoryError("Mean ledger exceeded its explicit observation limit")
        return rss

    expected = ((args.selected_composition, SELECTED_SHA),
                (args.selected_resource, SELECTED_RESOURCE_SHA),
                (args.original_summary, OLD_SUMMARY_SHA),
                (args.original_resource, OLD_RESOURCE_SHA))
    for path, checksum in expected:
        if digest(path) != checksum:
            raise ValueError("The published selected candidate or old audit identity differs: "+str(path))
    pair_proof = Path(__file__).resolve().parent.parent/"notes/2026-11-12-tail-two-complete-mean-roots-rational-difference.md"
    if digest(pair_proof) != PAIR_PROOF_SHA:
        raise ValueError("The complete paired-mean rational proof changed")
    radial_proof = Path(__file__).resolve().parent.parent/"notes/2026-11-12-tail-two-complete-mean-radial-difference.md"
    if digest(radial_proof) != RADIAL_PROOF_SHA:
        raise ValueError("The complete paired-mean radial proof changed")
    helper = Path(__file__).with_name("tail_outer_carrier_candidate_comparison.py")
    if digest(helper) != COMPARISON_SHA:
        raise ValueError("The formally executed exact comparison source changed")
    original, selected = read(args.original_summary), read(args.selected_composition)
    physical, carrier, comparison = map(read,
        (args.physical_summary, args.carrier_summary, args.comparison))
    for value in (original, selected, physical, carrier, comparison):
        require_gates(value)
    formal(args.selected_resource, args.selected_composition, "--out")
    formal(args.original_resource, args.original_summary, "--out")
    cp = formal(args.physical_resource, args.physical_summary, "--out-prefix")
    cc = formal(args.carrier_resource, args.carrier_summary, "--out-prefix")
    formal(args.comparison_resource, args.comparison, "--out")
    comparison_source_rows = [checksum for name, checksum in comparison["input_hashes"].items()
                              if Path(name).name == helper.name]
    if (comparison["schema"] != "formal-physical-carrier-comparison-v1"
            or comparison_source_rows != [COMPARISON_SHA]):
        raise ValueError("The complete exact comparison is not this executed source")
    for path in (args.physical_summary, args.physical_resource,
                 args.carrier_summary, args.carrier_resource):
        if comparison["input_hashes"].get(str(path)) != digest(path):
            raise ValueError("The complete comparison did not use this actual audit")
    if (selected["cell"] != 0 or selected["total_continuous_panels"] != 8594
            or [r["segment"] for r in selected["components"]] != list(range(9))
            or original["segment"] != 7 or original["cell"] != 0):
        raise ValueError("This application is bound to the published 8594-leaf cell")
    chosen = selected["components"][7]
    candidate = Path(chosen["candidate_path"])
    if (chosen["candidate_sha256"] != OLD_CANDIDATE_SHA or digest(candidate) != OLD_CANDIDATE_SHA
            or chosen["audit"] != str(args.original_summary)
            or chosen["audit_sha256"] != OLD_SUMMARY_SHA
            or original["input_hashes"].get(str(candidate)) != OLD_CANDIDATE_SHA):
        raise ValueError("The selected old segment and its audited complete mean differ")
    for key in ("cell", "segment", "modes", "tau", "original_candidate_input_hashes"):
        if physical[key] != carrier[key] or physical[key] != original[key]:
            raise ValueError("A real source or mode identity changed: "+key)
    if physical["nodes"] != carrier["nodes"]:
        raise ValueError("The two new candidates do not share physical endpoint jets")
    for value in (physical, carrier):
        if (not value["mean_height_uses_one_global_constant"]
                or not value["endpoint_nonmean_two_jets_exact_by_construction"]
                or not value["two_fixed_mean_endpoint_heights_not_implicitly_claimed"]):
            raise ValueError("The actual candidate lacks its full mean compatibility convention")
    pm_path, cm_path = option(cp, "--moment-summary"), option(cc, "--moment-summary")
    pm, cm = read(pm_path), read(cm_path)
    require_gates(pm)
    require_gates(cm)
    if (physical["input_hashes"].get(str(pm_path)) != digest(pm_path)
            or carrier["input_hashes"].get(str(cm_path)) != digest(cm_path)
            or cm["original_physical_moment_summary"] != str(pm_path)
            or cm["original_physical_moment_summary_sha256"] != digest(pm_path)
            or cm["physical_candidate_audit_sha256"] != digest(args.physical_summary)
            or pm["input_hashes"].get(str(candidate)) != OLD_CANDIDATE_SHA
            or pm["nodes"] != physical["nodes"] or cm["nodes"] != physical["nodes"]):
        raise ValueError("The same true moments and shared endpoint origin are not preserved")
    pparts = {r["part"]:r for r in physical["parts"]}
    cparts = {r["part"]:r for r in carrier["parts"]}
    groups = {r["part"]:r for r in pm["groups"]}
    oldparts = {r["part"]:r for r in original["parts"]}
    indices = sorted(groups)
    if (indices != sorted(pparts) or indices != sorted(cparts)
            or not indices or indices != list(range(indices[0], indices[-1]+1))):
        raise ValueError("One common contiguous collection of complete parts is required")
    paths = [args.selected_composition, args.selected_resource, args.original_summary,
        args.original_resource, args.physical_summary, args.physical_resource,
        args.carrier_summary, args.carrier_resource, args.comparison,
        args.comparison_resource, pm_path, cm_path, candidate, helper, pair_proof, radial_proof, Path(__file__)]
    inputs = {str(path):digest(path) for path in paths}
    # Bind all requested streams before writing any output header, including
    # later parts. These are byte checks only, never new source evaluations.
    for index in indices:
        for row in (groups[index], pparts[index], cparts[index]):
            path = Path(row["path"])
            if digest(path) != row["sha256"]:
                raise ValueError("A requested complete primary changed before consumption")
            inputs[str(path)] = row["sha256"]
        row = oldparts[index]
        path = Path(row["output"])
        if digest(path) != row["output_sha256"]:
            raise ValueError("An original complete mean primary changed before consumption")
        inputs[str(path)] = row["output_sha256"]
    cumulative = {key:Q(0) for key in ("old_to_carrier", "old_to_physical", "physical_to_carrier")}
    out_parts = []
    total_count = 0
    paired_mean_improved_leaves = 0
    paired_mean_radial_improved_leaves = 0
    paired_mean_unimproved_prefix_upper = Q(0)
    jet_max = {key:Q(0) for key in ("h", "h_r", "h_rr", "h_theta", "h_rtheta", "h_thetatheta")}
    modes = list(physical["modes"])
    for index in indices:
        group, pa, ca, oldpart = groups[index], pparts[index], cparts[index], oldparts[index]
        bounds = [(Q(x["source_left"]),Q(x["source_right"]),x["panels"])
                  for x in (group,pa,ca)]
        if len(set(bounds)) != 1 or bounds[0][:2] != (Q(oldpart["left"]),Q(oldpart["right"])):
            raise ValueError("Actual old and new substage domains do not agree")
        oldrows = validate_old_primary(oldpart, original, inputs, memory)
        streams = [primary_rows(group,pm,moments=True,inputs=inputs,rss_check=memory),
                   primary_rows(pa,physical,moments=False,inputs=inputs,rss_check=memory),
                   primary_rows(ca,carrier,moments=False,inputs=inputs,rss_check=memory)]
        output = Path(str(args.out_prefix)+f"-part{index:02d}-mean.jsonl.gz")
        if output.exists():
            raise FileExistsError("Use a fresh mean primary")
        before = dict(cumulative)
        point = 0
        count = 0
        local_mass = Q(0)
        with gzip.open(output,"xt",encoding="utf-8",compresslevel=6) as out:
            out.write(json.dumps(dict(kind="header",part=index,
                metric_and_candidate_origin_hashes=inputs,
                scope="Bounds for fixed actual candidates, not a new PDE solution",
                formulas="omega=I00+I01; mean_delta=integral w*(c_new-c_old) dr"),
                separators=(",",":"))+"\n")
            while True:
                entries = [next(stream,None) for stream in streams]
                if all(row is None for row in entries):
                    break
                if any(row is None for row in entries):
                    raise ValueError("A true-moment or audited stream ended early")
                (left,right,m),(lp,rp,p),(lc,rc,c) = entries
                if (left,right) != (lp,rp) or (left,right) != (lc,rc):
                    raise ValueError("The true moments and two new candidates use different leaves")
                if p["source"] != c["source"] or p["physical_u"] != c["physical_u"]:
                    raise ValueError("A same-leaf actual background identity changed")
                while oldrows[point]["right"] <= left:
                    point += 1
                overlapping = []
                probe = point
                covered = left
                while probe < len(oldrows) and oldrows[probe]["left"] < right:
                    row = oldrows[probe]
                    lo, hi = max(left,row["left"]),min(right,row["right"])
                    if lo != covered or lo >= hi:
                        raise ValueError("Original mean enclosures do not cover the new source leaf")
                    overlapping.append(row)
                    covered = hi
                    probe += 1
                if covered != right or not overlapping:
                    raise ValueError("A new source leaf has no complete old mean cover")
                cold = max(x["mean"] for x in overlapping)
                crold = max(x["mean_r"] for x in overlapping)
                cpa, cca = upper(p,"complete_mean_abs"),upper(c,"complete_mean_abs")
                crpa, crca = (upper(p,"complete_mean_source_derivative_abs"),
                             upper(c,"complete_mean_source_derivative_abs"))
                wlo, whi = interval(m["w"])
                drlo, drhi = interval(m["source_width"])
                wr = abs_upper(m["wr"])
                z0,z1 = interval(m["moments"]["00"]),interval(m["moments"]["01"])
                omega_lo = max(z0[0]+z1[0],drlo*wlo)
                omega = min(z0[1]+z1[1],drhi*whi)
                if not (wlo>0 and drlo>0 and 0<omega_lo<=omega):
                    raise ValueError("The same positive integral omega lost its domain")
                local_mass += omega
                c_difference, paired_record = paired_mean_bound(p,c,m,modes)
                cr_difference, paired_radial_record = paired_mean_radial_bound(
                    p,c,m,modes,c_difference)
                paired_mean_radial_improved_leaves += int(paired_radial_record["strictly_improves_sum"])
                paired_mean_improved_leaves += int(paired_record["strictly_improves_sum"])
                paired_mean_unimproved_prefix_upper += omega*(cpa+cca)
                increment = dict(old_to_carrier=omega*(cold+cca),
                    old_to_physical=omega*(cold+cpa),physical_to_carrier=omega*c_difference)
                prefix_before = dict(cumulative)
                for key in cumulative:
                    cumulative[key] += increment[key]
                jets = {}
                for key in ("H","Kbar","Kbar_r"):
                    av=p["actual_nonmean_jet_cosine_intervals"][key]
                    bv=c["actual_nonmean_jet_cosine_intervals"][key]
                    if len(av)!=len(modes) or len(bv)!=len(modes):
                        raise ValueError("An actual nonmean jet has incomplete Fourier modes")
                    jets[key]=[difference_upper(a,b) for a,b in zip(av,bv)]
                h0=sum(jets["H"],Q(0))
                k0=sum(jets["Kbar"],Q(0))
                kr0=sum(jets["Kbar_r"],Q(0))
                actual = dict(
                    h=cumulative["physical_to_carrier"]+h0,
                    h_theta=sum((m0*v for m0,v in zip(modes,jets["H"])),Q(0)),
                    h_thetatheta=sum((m0*m0*v for m0,v in zip(modes,jets["H"])),Q(0)),
                    h_r=whi*(c_difference+k0),
                    h_rtheta=whi*sum((m0*v for m0,v in zip(modes,jets["Kbar"])),Q(0)),
                    h_rr=wr*(c_difference+k0)+whi*(cr_difference+kr0))
                for key in jet_max:
                    jet_max[key]=max(jet_max[key],actual[key])
                record=dict(kind="complete_exact_mean_difference_leaf",part=index,panel=count,
                    source_left=str(left),source_right=str(right),
                    old_mean_panels=[x["panel"] for x in overlapping],
                    omega_lower=qr(omega_lo),omega_upper=qr(omega),
                    physical_to_carrier_paired_mean=paired_record,
                    physical_to_carrier_paired_mean_radial=paired_radial_record,
                    actual_physical_mass_from_two_positive_moments=True,
                    physical_mass_intersection_only_same_integral=True,
                    complete_mean_upper={k:qr(v) for k,v in
                        dict(old=cold,physical=cpa,carrier=cca).items()},
                    mean_difference_increment_upper={k:qr(v) for k,v in increment.items()},
                    mean_prefix_before_upper={k:qr(v) for k,v in prefix_before.items()},
                    mean_prefix_through_whole_leaf_upper={k:qr(v) for k,v in cumulative.items()},
                    old_to_carrier_mean_radial_derivative_upper=qr(whi*(cold+cca)),
                    old_to_carrier_mean_second_radial_derivative_upper=
                        qr(wr*(cold+cca)+whi*(crold+crca)),
                    physical_to_carrier_complete_height_jet_upper=
                        {k:qr(v) for k,v in actual.items()})
                out.write(json.dumps(record,separators=(",",":"),allow_nan=False)+"\n")
                count+=1
                total_count+=1
                memory()
            if count != group["panels"]:
                raise ValueError("The complete shared partition was not consumed")
            out.write(json.dumps(dict(kind="trailer",part=index,complete=True,panels=count),
                separators=(",",":"))+"\n")
        if output.stat().st_size>=5_000_000:
            raise ValueError("The exact mean primary exceeds the single-file limit")
        out_parts.append(dict(part=index,panels=count,source_left=group["source_left"],
            source_right=group["source_right"],path=str(output),sha256=digest(output),
            bytes=output.stat().st_size,
            positive_w_dr_mass_upper=qr(local_mass),
            mean_shift_before_upper={k:qr(v) for k,v in before.items()},
            mean_shift_after_upper={k:qr(v) for k,v in cumulative.items()}))
        print(json.dumps(dict(event="complete_saved_mean_difference_part",part=index,
            panels=count,old_to_carrier_shift_upper=qr(cumulative["old_to_carrier"]),
            peak_RSS_KiB=memory())),flush=True)
    if total_count!=physical["panels"] or total_count!=carrier["panels"]:
        raise ValueError("The audited requested panel count changed")
    result=dict(author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",scope=__doc__,
        schema="exact-original-physical-carrier-mean-ledger-v3",
        status="Complete exact consumption of the requested formally audited candidate parts",
        input_hashes=inputs,cell=0,segment=7,modes=modes,tau=physical["tau"],
        selected_original_continuous_panels=8594,
        requested_complete_parts=indices,continuous_panels=total_count,parts=out_parts,
        complete_mean_height_difference_upper={k:qr(v) for k,v in cumulative.items()},
        physical_to_carrier_complete_height_jet_upper={k:qr(v) for k,v in jet_max.items()},
        physical_to_carrier_true_line_mean_refinement=dict(
            evaluated_leaves=total_count,strictly_improved_leaves=paired_mean_improved_leaves,
            original_root_abs_sum_integral_upper=qr(paired_mean_unimproved_prefix_upper),
            same_pair_refined_integral_upper=qr(cumulative["physical_to_carrier"]),
            radial_derivative_evaluated_leaves=total_count,
            strictly_improved_radial_derivative_leaves=paired_mean_radial_improved_leaves,
            complete_mean_radial_difference_uses_full_implicit_equation=True,
            original_complete_mean_radial_bounds_kept_as_valid_fallback=True,
            old_candidate_difference_still_uses_certified_old_mean_abs=True),
        mean_after_replacement="With the left mean value fixed once, the same signed "
            "integral shift continues as a constant through all unchanged later pieces. "
            "This ledger bounds its absolute value and never resets it at a node.",
        retained_selected_candidate_unchanged=True,
        candidate_replacement_automatically_selected=False,
        original_lost_R77_output_not_used_or_reconstructed=True,
        signed_mean_cancellation_claimed=False,
        exact_outer_solution_or_spatial_geometry_error_claimed=False,
        new_Arb_source_integration_ODE_BVP_Node=False,
        gates=dict(published_selected_8594_origin_checked=True,
            old_and_new_formal_audits_and_comparison_exit0=True,
            every_consumed_primary_SHA_and_complete_cover_checked=True,
            complete_original_mean_root_and_inverse_margins_retained=True,
            exact_positive_w_dr_from_existing_moments=True,
            paired_mean_true_line_real_A_D_L_positive=True,
            paired_mean_zero_modes_and_full_root_derivatives_preserved=True,
            paired_radial_full_mean_and_four_G_z_terms_preserved=True,
            no_actual_second_derivative_replaced_by_PDE=True,
            common_mean_constant_not_reset=True,
            all_new_full_physical_height_derivatives_retained=True,
            no_minimum_between_different_candidate_residuals=True),
        elapsed_seconds=time.monotonic()-began,peak_RSS_KiB=memory())
    save(summary_path,result)
    print(json.dumps(dict(event="complete_exact_carrier_mean_ledger",
        summary=str(summary_path),panels=total_count,
        mean_difference_upper=result["complete_mean_height_difference_upper"],
        gates=result["gates"],peak_RSS_KiB=memory())),flush=True)


if __name__=="__main__":
    main()
