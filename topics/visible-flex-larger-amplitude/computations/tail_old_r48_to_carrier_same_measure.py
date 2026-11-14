#!/usr/bin/env python3
"""Local-only original R48 -> carrier bridge on the same111 physical leaves.

Prepared exact Fraction consumer. Reuses the complete old candidate, true
measure omega=integral w dr, audited CF fields and full mean records. No PM,
PA, source, root, ODE, Arb, Node or BVP is rerun. The output concerns two
defined candidate references, not a proved exact outer solution.

Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import resource
import sys
import time

SOURCE_HASHES = {
    "core": "734af51836d7a57cd9d80a7804eccdc286ae4a4c38263cb519e93d473a460eaf",
    "io_helper": "71b8e666c07e5e2a203dbde028ff8e0bb64a883551b0cd47d609773e88c848fe",
    "mean_helper": "857d698dde2a6ca548c2ad55f6297d03fb0bc61870427bcf78d000225de16fd5",
}
EXPECTED = {
    "original_candidate": "7da554bdb467fe2b997a01971dd4917003fd5deeb36978e200e1457ea3c8fddf",
    "original_summary": "806fdb96b9aa6eafd921c07518a5b52218180d2182f7b8d18abb8e3d695638e4",
    "original_resource": "912ad6200027fdb445cd3e8636c1f6cd404a3480d2c013b6c4722e6888016820",
    "carrier_summary": "0ac4b1e14ec34a86035add63e6250660924537c54acc834e497c6ebdd396ae12",
    "carrier_resource": "dee1cef1a748f4459e00a5428dd4b6b1602c3eb442498091b29bd88e0ea1c865",
    "carrier_primary": "d07456782cfd2cd292cbb77fbbf437617a82ab6039f774fc5637c74a2e486dbe",
    "mean_summary": "a178bc76d676eaa3aa6e0e1f57592dceea27bc996017503097a1fd01f8bde1f2",
    "mean_resource": "263ea6873d694bc3ffaa8540c08bea21bfc6f38defd4a7c52e5dd63a4e0e82ff",
    "mean_primary": "6b6748eab26c02b1960b367acc22f3a80760d6d40c20aa998ddaa3c4193d0e71",
}
MODES = list(range(2, 41, 2))


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def load_module(path, name, expected):
    if digest(path) != expected:
        raise ValueError("A complete mathematical helper changed: "+name)
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in EXPECTED:
        ap.add_argument("--"+name.replace("_", "-"), type=Path, required=True)
    ap.add_argument("--original-primary", type=Path, required=True)
    ap.add_argument("--core", type=Path,
        default=Path(__file__).with_name("tail_r48_same_measure_core.py"))
    ap.add_argument("--io-helper", type=Path,
        default=Path(__file__).with_name("tail_r103_local_carrier_centre_drift.py"))
    ap.add_argument("--mean-helper", type=Path,
        default=Path(__file__).with_name("tail_outer_carrier_mean_ledger_v3.py"))
    ap.add_argument("--out-prefix", type=Path, required=True)
    ap.add_argument("--rss-limit-mib", type=int, default=96)
    args = ap.parse_args()
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    began = time.monotonic()
    summary_path = Path(str(args.out_prefix)+"-summary.json")
    primary_path = Path(str(args.out_prefix)+"-leaves.jsonl.gz")
    if summary_path.exists() or primary_path.exists():
        raise FileExistsError("Use a fresh complete bridge prefix")
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    core = load_module(args.core, "same_measure_core", SOURCE_HASHES["core"])
    io = load_module(args.io_helper, "local_drift_io", SOURCE_HASHES["io_helper"])
    mean = load_module(args.mean_helper, "complete_mean_math", SOURCE_HASHES["mean_helper"])
    algebra_checks = core.exact_basis_checks()
    I, keys = core.I, core.KEYS

    def memory():
        rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if rss > args.rss_limit_mib*1024:
            raise MemoryError("Owned same-measure consumer exceeded observed RSS")
        return rss

    def iv(value):
        return I(*io.interval(value))

    def read(path):
        with (gzip.open(path, "rt") if Path(path).suffix == ".gz"
              else Path(path).open()) as stream:
            return json.load(stream)

    def dy(value):
        return io.dyadic(value)

    def csum(values):
        out = Q(0)
        for value in values:
            out = io.positive_upper(out+value)
        return out

    files = {}
    for name, expected in EXPECTED.items():
        p = getattr(args, name)
        if digest(p) != expected:
            raise ValueError("A frozen actual input changed: "+name)
        files[name] = dict(path=str(p), sha256=expected, bytes=p.stat().st_size)
    original, old, carrier, measured = map(read, (
        args.original_candidate, args.original_summary,
        args.carrier_summary, args.mean_summary))
    old_usage, cf_usage, mean_usage = map(read, (
        args.original_resource, args.carrier_resource, args.mean_resource))
    for value in (original, old, carrier, measured):
        io.assert_gates(value)
    if old_usage["exitcode"] != 0 or old_usage["termination_signal"] is not None:
        raise ValueError("Original continuous audit has no formal successful exit")
    original_out = Path(old_usage["command"][old_usage["command"].index("--out")+1])
    if original_out.name != args.original_summary.name:
        raise ValueError("Original resource identifies another old audit")
    io.check_formal(cf_usage, args.carrier_summary)
    io.check_formal(mean_usage, args.mean_summary)
    if (original["cell"] != 0 or original["segment"] != 7
            or original["modes"] != MODES or original["shooting_parts"] != 8
            or len(original["nodes"]) != 9
            or carrier["nodes"] != original["nodes"]
            or carrier["original_candidate_input_hashes"] != original["input_hashes"]
            or not carrier["gates"]["same_true_metric_and_original_shared_physical_two_jets"]
            or not carrier["endpoint_nonmean_two_jets_exact_by_construction"]
            or carrier["mode"] != "carrier" or carrier["modes"] != MODES
            or carrier["panels"] != 111 or [p["part"] for p in carrier["parts"]] != [0]):
        raise ValueError("The fixed endpoints or mathematical carrier origin changed")
    if (measured["continuous_panels"] != 111 or measured["modes"] != MODES
            or measured["requested_complete_parts"] != [0]
            or [p["part"] for p in measured["parts"]] != [0]):
        raise ValueError("The complete common111 mean partition changed")
    if EXPECTED["original_candidate"] not in old["input_hashes"].values():
        raise ValueError("Old audit is not attached to this exact candidate")
    old_part = next(p for p in old["parts"] if p["part"] == 0)
    defined_part = next(p for p in original["parts"] if p["part"] == 0)
    if (old_part["panels"] != 37 or Q(old_part["left"]) != 0
            or Q(old_part["right"]) != Q(1, 8)
            or Q(defined_part["left"]) != 0 or Q(defined_part["right"]) != Q(1, 8)):
        raise ValueError("The original part0 identity differs")
    if digest(args.original_primary) != old_part["output_sha256"]:
        raise ValueError("The original37-leaf primary changed")
    files["original_primary"] = dict(path=str(args.original_primary),
        sha256=old_part["output_sha256"], bytes=args.original_primary.stat().st_size)
    for data, name in ((carrier, "carrier_primary"), (measured, "mean_primary")):
        if data["parts"][0]["sha256"] != EXPECTED[name] or data["parts"][0]["panels"] != 111:
            raise ValueError("The explicit primary is not bound to its frozen summary")

    def complete_J(row):
        b = {key:dy(value) for key,value in row["bounds_upper"].items()}
        values = [max(map(abs, io.interval(x))) for x in row["full_J_cosine_intervals"]]
        if len(values) != 41 or any(x < 0 for x in b.values()):
            raise ValueError("Full scalar and finite outside frequencies are required")
        d = min(Q(1), dy(row["gates_lower"]["real_D_lower"]))
        w = io.interval(row["source"]["w"])[1]
        if d <= 0:
            raise ValueError("No positive real D")
        perp = sum(values[1:], Q(0))
        zero = min(values[0], Q(3,2)*(1+w*w)**2*b["full_D_nonconstant_W1"]*perp/d**3)
        return min(sum(values, Q(0)), b["complete_J_l1"], zero+perp)

    old_rows = []
    at, header, trailer = Q(0), False, False
    with gzip.open(args.original_primary, "rt") as stream:
        for line in stream:
            row = json.loads(line)
            if row["kind"] == "header":
                if (header or old_rows or row["part"] != 0
                        or row["input_hashes"] != old["input_hashes"]
                        or row["source_hashes"] != old["source_hashes"]):
                    raise ValueError("Old complete primary header changed")
                header = True
                continue
            if row["kind"] == "complete_substage_trailer":
                if (trailer or not row["complete_source_cover"]
                        or row["accepted_panels"] != len(old_rows) or row["part"] != 0):
                    raise ValueError("Old complete primary trailer changed")
                trailer = True
                continue
            left, right = Q(row["source_left"]), Q(row["source_right"])
            if (not header or trailer or row["kind"] != "accepted_complete_R64_and_J_panel"
                    or not row["same_candidate_complete_mean"] or left != at
                    or not left < right <= Q(1, 8)
                    or any(dy(x) <= 0 for x in row["gates_lower"].values())):
                raise ValueError("Incomplete actual old root/domain/continuous cover")
            old_rows.append(dict(left=left, right=right, source=row["source"],
                b={k:dy(v) for k,v in row["bounds_upper"].items()},
                gates={k:dy(v) for k,v in row["gates_lower"].items()},
                J=complete_J(row)))
            at = right
    if not (header and trailer and at == Q(1, 8) and len(old_rows) == 37):
        raise ValueError("Not all original37 leaves were read")

    def overlap(left, right):
        rows = [r for r in old_rows if r["left"] < right and r["right"] > left]
        at = left
        for r in rows:
            a, b = max(left, r["left"]), min(right, r["right"])
            if a != at or not a < b:
                raise ValueError("Old boxes do not cover the complete new leaf")
            at = b
        if not rows or at != right:
            raise ValueError("Missing old continuous coverage")
        return rows

    def chead(h):
        if (h["mode"] != "carrier" or h["input_hashes"] != carrier["input_hashes"]
                or h["source_hashes"] != carrier["source_hashes"]
                or h["complete_J_cosine_modes"] != list(range(0, 81, 2))):
            raise ValueError("CF complete header identity changed")

    def mhead(h):
        if h["part"] != 0 or h["metric_and_candidate_origin_hashes"] != measured["input_hashes"]:
            raise ValueError("Complete mean origin changed")

    cs = io.primary_rows(args.carrier_primary,
        "complete_new_physical_substage_R64_J_R77_leaf", chead)
    ms = io.primary_rows(args.mean_primary, "complete_exact_mean_difference_leaf", mhead)
    leaves = []
    while True:
        c, m = next(cs, None), next(ms, None)
        if c is None and m is None:
            break
        if c is None or m is None:
            raise ValueError("The paired primary ended early")
        left, right = Q(c["source_left"]), Q(c["source_right"])
        if (c["panel"] != m["panel"] or c["part"] != m["part"]
                or left != Q(m["source_left"]) or right != Q(m["source_right"])
                or not c["complete_mean"]
                or not m["actual_physical_mass_from_two_positive_moments"]
                or not m["physical_mass_intersection_only_same_integral"]
                or any(dy(v) <= 0 for v in c["gates_lower"].values())
                or io.interval(c["source"]["radius_x"]) != (Q(1), Q(1))):
            raise ValueError("Same actual leaf/mean/physical coordinate is required")
        omega = I(io.ratio(m["omega_lower"]), io.ratio(m["omega_upper"]))
        if omega.lo <= 0:
            raise ValueError("The true positive measure has no lower bound")
        covers = overlap(left, right)
        rx_old = I(min(io.interval(r["source"]["radius_x"])[0] for r in covers),
                   max(io.interval(r["source"]["radius_x"])[1] for r in covers))
        source_rx = iv(c["source"]["source_radius_x"]).meet(rx_old)
        if source_rx.lo <= 0:
            raise ValueError("Actual source rx is not positive")
        fields = {key:[iv(x) for x in c["actual_nonmean_jet_cosine_intervals"][key]]
                  for key in ("H", "Kbar", "Kbar_r")}
        if any(len(x) != 20 for x in fields.values()):
            raise ValueError("The complete20-mode candidate must be retained")
        leaves.append(dict(left=left, right=right, source=c["source"],
            source_rx=source_rx, omega=omega, cf=fields, raw_cf=c,
            old=covers, Jcf=complete_J(c),
            old_mean_prefix=io.ratio(m["mean_prefix_through_whole_leaf_upper"]["old_to_carrier"])))
        # Only the necessary fields of the large full-mean row are retained.
        memory()
    if len(leaves) != 111:
        raise ValueError("The actual111 leaves are incomplete")
    print(json.dumps(dict(event="same_measure_original_inputs_checked",
        old_leaves=37, new_leaves=111, peak_RSS_KiB=memory())), flush=True)

    bins = [b for b in original["bins"] if b["part"] == 0]
    if len(bins) != 8:
        raise ValueError("All original8 positive bins must remain")
    at = Q(0)
    for j,b in enumerate(bins):
        if b["bin"] != j or Q(b["left"]) != at or not at < Q(b["right"]) <= Q(1,8):
            raise ValueError("The exact original bin cover differs")
        at = Q(b["right"])
    if at != Q(1,8):
        raise ValueError("Original bin cover stopped early")
    old_total = {k:iv(defined_part["total_true_positive_moments"][k]).nonnegative()
                 for k in keys}
    old_bins = [{k:iv(b["values"][k]).nonnegative() for k in keys} for b in bins]
    piece = []
    for leaf in leaves:
        piece.append({k:core.positive_basis_range(k, 8*leaf["left"], 8*leaf["right"])
                         *leaf["omega"] for k in keys})
    zero = {k:I(0) for k in keys}
    prefix = [zero]
    for row in piece:
        prefix.append({k:prefix[-1][k]+row[k] for k in keys})
    suffix = [None]*(len(piece)+1)
    suffix[-1] = zero
    for j in range(len(piece)-1, -1, -1):
        suffix[j] = {k:suffix[j+1][k]+piece[j][k] for k in keys}
    total = {k:prefix[-1][k].meet(old_total[k]).meet(core.sum_i(b[k] for b in old_bins))
             for k in keys}
    if min(total[k].lo for k in keys) <= 0:
        raise ValueError("A same true total moment lost its strict positive lower end")

    def old_prefix_at(x, key):
        low = core.sum_i(old_bins[j][key] for j,b in enumerate(bins) if Q(b["right"]) <= x).lo
        high = core.sum_i(old_bins[j][key] for j,b in enumerate(bins) if Q(b["left"]) < x).hi
        return I(low, high)

    def old_suffix_at(x, key):
        low = core.sum_i(old_bins[j][key] for j,b in enumerate(bins) if Q(b["left"]) >= x).lo
        high = core.sum_i(old_bins[j][key] for j,b in enumerate(bins) if Q(b["right"]) > x).hi
        return I(low, high)

    points = [leaves[0]["left"]]+[r["right"] for r in leaves]
    pre_at, post_at = [], []
    for i,x in enumerate(points):
        pre_at.append({k:prefix[i][k].meet(total[k]-suffix[i][k])
                            .meet(old_prefix_at(x,k)).nonnegative() for k in keys})
        post_at.append({k:suffix[i][k].meet(total[k]-prefix[i][k])
                             .meet(old_suffix_at(x,k)).nonnegative() for k in keys})

    def endpoint(node, leaf):
        w = iv(node["w"]).meet(iv(leaf["source"]["w"]))
        wr = iv(node["wr"]).meet(iv(leaf["source"]["w"])*iv(leaf["source"]["log_w_x"]))
        rx = leaf["source_rx"]
        if "radius_x" in node:
            rx = rx.meet(iv(node["radius_x"]))
        jets = node["shared_physical_jets"]
        if any(sorted(map(int, jets[k])) != MODES for k in ("H","Hr","Hrr")):
            raise ValueError("The original complete endpoint modes changed")
        return {m:core.endpoint(iv(jets["H"][str(m)]), iv(jets["Hr"][str(m)]),
            iv(jets["Hrr"][str(m)]), w, wr, rx) for m in MODES}

    if Q(original["nodes"][0]["source_x"]) != 0 or Q(original["nodes"][1]["source_x"]) != Q(1,8):
        raise ValueError("The old endpoint source coordinates differ")
    left_end = endpoint(original["nodes"][0], leaves[0])
    right_end = endpoint(original["nodes"][1], leaves[-1])
    candidates = {m:core.old_candidate(left_end[m], right_end[m], total,
                    iv(defined_part["bubble_coefficients"][str(m)])) for m in MODES}
    for i,leaf in enumerate(leaves):
        pre = {k:I(pre_at[i][k].lo, pre_at[i+1][k].hi) for k in keys}
        post = {k:I(post_at[i+1][k].lo, post_at[i][k].hi) for k in keys}
        field = {k:[] for k in ("H","Kbar","Kbar_r")}
        for m in MODES:
            f = core.evaluate_old(candidates[m], 8*leaf["left"], 8*leaf["right"],
                                  pre, post, leaf["source_rx"])
            for k in field:
                field[k].append(f[k])
        leaf["old_field"] = field
        leaf["dK"] = [(a-b).absmax() for a,b in zip(field["Kbar"],leaf["cf"]["Kbar"])]
        leaf["dKr"] = [(a-b).absmax() for a,b in zip(field["Kbar_r"],leaf["cf"]["Kbar_r"])]
        leaf["direct_dH"] = [(a-b).absmax() for a,b in zip(field["H"],leaf["cf"]["H"])]
        memory()
    # Both candidates are built from the exact same two endpoint heights.
    prefix_dH = [[Q(0)]*20]
    for leaf in leaves:
        prefix_dH.append([io.positive_upper(a+leaf["omega"].hi*b)
                          for a,b in zip(prefix_dH[-1],leaf["dK"])])
    suffix_dH = [[Q(0)]*20 for _ in range(112)]
    for i in range(110,-1,-1):
        suffix_dH[i] = [io.positive_upper(a+leaves[i]["omega"].hi*b)
                        for a,b in zip(suffix_dH[i+1],leaves[i]["dK"])]
    for i,leaf in enumerate(leaves):
        leaf["dH"] = [min(a,b,c) for a,b,c in
            zip(leaf["direct_dH"], prefix_dH[i+1], suffix_dH[i])]
        for j,h in enumerate(leaf["dH"]):
            a,b = leaf["old_field"]["H"][j],leaf["cf"]["H"][j]
            leaf["old_field"]["H"][j] = a.meet(b+I(-h,h))
            leaf["cf"]["H"][j] = b.meet(a+I(-h,h))

    def norm(field, key, power=0):
        return sum((Q(m)**power*z.absmax() for m,z in zip(MODES,field[key])),Q(0))

    def moment_record(leaf):
        w,ell = iv(leaf["source"]["w"]),iv(leaf["source"]["log_w_x"])
        return dict(radius=leaf["source"]["radius"],w=leaf["source"]["w"],
                    wr=(w*ell).record())

    for leaf in leaves:
        c = leaf["raw_cf"]
        bcf = {k:dy(v) for k,v in c["bounds_upper"].items()}
        oldcover = leaf["old"]
        cold = max(r["b"]["complete_mean_abs"] for r in oldcover)
        crold = min(max(r["b"]["complete_mean_source_derivative_abs"]/
                        io.interval(r["source"]["radius_x"])[0] for r in oldcover),
                    max(r["b"]["complete_mean_source_derivative_abs"] for r in oldcover)/leaf["source_rx"].lo)
        cc,crc = bcf["complete_mean_abs"],bcf["complete_mean_source_derivative_abs"]
        gates_old = {k:min(r["gates"][k] for r in oldcover)
                     for k in ("real_S_lower","real_D_lower","real_L_lower")}
        A = min(Q(1),gates_old["real_S_lower"],dy(c["gates_lower"]["real_S_lower"]))
        D = min(Q(1),gates_old["real_D_lower"],dy(c["gates_lower"]["real_D_lower"]))
        L = min(gates_old["real_L_lower"],dy(c["gates_lower"]["real_L_lower"]))
        if min(A,D,L) <= 0:
            raise ValueError("Complete actual roots have no positive common real line")
        r,w = iv(leaf["source"]["radius"]),iv(leaf["source"]["w"])
        if not Q(1,20) < r.lo <= r.hi < Q(1,3) or not 0 < w.lo <= w.hi <= Q(3,25):
            raise ValueError("The same paid real source range changed")
        z,E,scale = w.hi*w.hi,1+w.hi*w.hi,r.lo*w.lo
        of,cf = leaf["old_field"],leaf["cf"]
        old_R = max(q["b"]["R_tau"] for q in oldcover)
        old_T = max(q["b"]["P_theta_W1"] for q in oldcover)/3
        p = max(min(norm(of,"H",1)/scale, old_R/3), norm(cf,"H",1)/scale)
        t = max(min(norm(of,"H",2)/scale, old_T),
                min(norm(cf,"H",2)/scale,bcf["P_theta_W1"]/3))
        k = max(min(norm(of,"Kbar"),old_R/3)+cold,norm(cf,"Kbar")+cc)
        eK = sum(leaf["dK"],Q(0))
        eP = sum((m*h for m,h in zip(MODES,leaf["dH"])),Q(0))/scale
        eT = sum((m*m*h for m,h in zip(MODES,leaf["dH"])),Q(0))/scale
        vd = z*(2*k+k*k+E*p*p)
        CK = (k+E*t)/D**2+Q(3,2)*vd/D**3
        CT = (k+z*p*p)/(A*D)+vd/(2*D**2)
        CP = E*p*(1+z*(1+k)*t/A)/D**2+2*z*p*(1+k)*t/(A*A*D)
        dc = min(cold+cc,E*E/L*(CK*eK+CP*eP+CT*eT))
        old_math = dict(
            kind="derived_same_original_R48_enclosures_not_an_original_stream_row",
            actual_nonmean_jet_cosine_intervals={key:[x.record() for x in of[key]] for key in of},
            bounds_upper=dict(complete_mean_abs=core.upper_record(cold),
                              complete_mean_source_derivative_abs=core.upper_record(crold)),
            gates_lower={key:core.lower_record(v) for key,v in gates_old.items()})
        cf_math = dict(
            kind="derived_same_CF_enclosures_not_an_original_stream_row",
            actual_nonmean_jet_cosine_intervals={key:[x.record() for x in cf[key]] for key in cf},
            bounds_upper=c["bounds_upper"],gates_lower=c["gates_lower"])
        dcr, radial = mean.paired_mean_radial_bound(old_math,cf_math,moment_record(leaf),MODES,dc)
        if dcr < 0 or dcr > crold+crc:
            raise ArithmeticError("Complete radial mean difference lost its direct bound")
        wr = (w*iv(leaf["source"]["log_w_x"])).absmax()
        jets = dict(
            h_nonmean=sum(leaf["dH"],Q(0)),
            h_theta=sum((m*h for m,h in zip(MODES,leaf["dH"])),Q(0)),
            h_thetatheta=sum((m*m*h for m,h in zip(MODES,leaf["dH"])),Q(0)),
            h_r=w.hi*(dc+eK),
            h_rtheta=w.hi*sum((m*v for m,v in zip(MODES,leaf["dK"])),Q(0)),
            h_rr=wr*(dc+eK)+w.hi*(dcr+sum(leaf["dKr"],Q(0))))
        geometry = core.centred_geometry(r.hi,w.hi,E,A,D,p,k,t,eP,eK,eT,dc)
        oldD = min(Q(1),gates_old["real_D_lower"])
        cfD = min(Q(1),dy(c["gates_lower"]["real_D_lower"]))
        Jold = max(x["J"] for x in oldcover)
        common = Q(22,7)**2/16*r.hi*w.hi*leaf["omega"].hi
        drift_old = common*Jold/(leaf["source_rx"].lo*oldD**2)
        drift_cf = common*leaf["Jcf"]/cfD**2
        leaf.update(mean_difference=dc,mean_radial_difference=dcr,jets=jets,geometry=geometry,
                    mean_increment=leaf["omega"].hi*dc,
                    drift_old_increment=drift_old,drift_cf_increment=drift_cf,
                    original_physical_mean_r=crold,original_mean=cold,
                    radial_full_Gz_retained=radial["all_four_complete_G_z_terms_retained"])
        memory()

    def positive_prefix(key):
        result=[Q(0)]
        for leaf in leaves:
            result.append(io.positive_upper(result[-1]+leaf[key]))
        return result

    def positive_suffix(key):
        result=[Q(0)]*112
        for i in range(110,-1,-1):
            result[i]=io.positive_upper(result[i+1]+leaves[i][key])
        return result

    mean_pre,mean_post=positive_prefix("mean_increment"),positive_suffix("mean_increment")
    co_pre,co_post=positive_prefix("drift_old_increment"),positive_suffix("drift_old_increment")
    cn_pre,cn_post=positive_prefix("drift_cf_increment"),positive_suffix("drift_cf_increment")
    mean_total_old=leaves[-1]["old_mean_prefix"]
    maxima={k:Q(0) for k in ("h_left","h_right","h_r","h_rr","h_theta",
        "h_rtheta","h_thetatheta","reference_vector","centred_xy",
        "radial_reference_position_left_gauge","radial_reference_position_right_gauge")}
    tmp=primary_path.with_name(primary_path.name+".tmp-"+str(os.getpid()))
    sources={k:dict(path=str(getattr(args,k)),sha256=v) for k,v in SOURCE_HASHES.items()}
    with gzip.open(tmp,"xt",encoding="utf-8",compresslevel=6) as stream:
        stream.write(json.dumps(dict(kind="header",schema="old-R48-to-CF-same-measure-v1",
            sources=sources,input_hashes={k:v["sha256"] for k,v in files.items()},
            modes=MODES,physical_radial_derivatives=True),separators=(",",":"))+"\n")
        for i,leaf in enumerate(leaves):
            ml=min(mean_pre[i+1],leaf["old_mean_prefix"])
            mr=min(mean_post[i],mean_total_old)
            j,g=leaf["jets"],leaf["geometry"]
            hl,hr=ml+j["h_nonmean"],mr+j["h_nonmean"]
            pl=g["centred_xy"]+co_pre[i+1]+cn_pre[i+1]+hl
            pr=g["centred_xy"]+co_post[i]+cn_post[i]+hr
            values=dict(h_left=hl,h_right=hr,reference_vector=g["reference_vector"],
                centred_xy=g["centred_xy"],radial_reference_position_left_gauge=pl,
                radial_reference_position_right_gauge=pr,
                **{k:j[k] for k in ("h_r","h_rr","h_theta","h_rtheta","h_thetatheta")})
            for k,value in values.items():
                maxima[k]=max(maxima[k],value)
            outrow=dict(kind="complete_actual_same_measure_candidate_bridge_leaf",
                part=0,panel=i,source_left=str(leaf["left"]),source_right=str(leaf["right"]),
                old_actual_nonmean_jet_cosine_intervals={k:[v.record() for v in leaf["old_field"][k]]
                                                       for k in leaf["old_field"]},
                actual_difference_cosine_bounds={k:[core.upper_record(v) for v in leaf[k]]
                                                for k in ("dH","dK","dKr")},
                full_mean_difference_upper=core.upper_record(leaf["mean_difference"]),
                full_physical_mean_radial_difference_upper=core.upper_record(leaf["mean_radial_difference"]),
                original_cx_converted_to_physical_cr=True,
                mean_height_left_gauge_upper=core.upper_record(ml),
                mean_height_right_gauge_upper=core.upper_record(mr),
                old_centre_drift_left_upper=core.upper_record(co_pre[i+1]),
                old_centre_drift_right_upper=core.upper_record(co_post[i]),
                carrier_centre_drift_left_upper=core.upper_record(cn_pre[i+1]),
                carrier_centre_drift_right_upper=core.upper_record(cn_post[i]),
                complete_six_jets_and_reference_geometry={k:core.upper_record(v) for k,v in values.items()},
                full_Gz_radial_mean_terms_retained=leaf["radial_full_Gz_retained"])
            stream.write(json.dumps(outrow,separators=(",",":"),allow_nan=False)+"\n")
        stream.write(json.dumps(dict(kind="trailer",continuous_leaves=111,complete=True))+"\n")
    if tmp.stat().st_size>=5_000_000:
        raise ValueError("The complete owned bridge stream exceeds5 MB")
    if primary_path.exists():
        raise FileExistsError("A result appeared while writing")
    os.replace(tmp,primary_path)
    result=dict(schema="complete-actual-old-R48-to-CF-same-measure-bridge-v1",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",date_utc="2026-11-13",
        status="Actual continuous bridge between two fixed candidate references, not exact-surface error",
        source_sha256=digest(__file__),mathematical_sources=sources,files=files,
        core_finite_algebra_checks=algebra_checks,old_leaves=37,new_common_leaves=111,
        old_coordinate="u=8x",new_coordinate="physical r; never equated to old u",
        true_measure="omega=I00^(r)+I01^(r)=integral w dr",
        improved_old_five_total_intervals={k:total[k].record() for k in keys},
        same_old_lambda_intervals={str(m):candidates[m]["lam"].record() for m in MODES},
        complete_difference_maxima={k:core.upper_record(v) for k,v in maxima.items()},
        complete_mean_height_end_shift_upper=core.upper_record(min(mean_pre[-1],mean_total_old)),
        old_radial_reference_centre_drift_upper=core.upper_record(co_pre[-1]),
        carrier_radial_reference_centre_drift_upper=core.upper_record(cn_pre[-1]),
        two_global_gauges="Left or right alignment is selected once for the whole reference; no pointwise min of gauges.",
        unchanged_right_seven_parts="In the right global gauge all reference geometry there agrees exactly; in the left gauge only one fixed end translation persists.",
        original_PM_PA_A_CF_or_integrals_recomputed=False,
        complete_scalar_mean_and_radial_derivative=True,
        candidate_actual_second_derivatives_only=True,
        candidate_vectors_are_only_reference_vectors=True,
        true_outer_solution_or_error_or_reach_claimed=False,
        primary=dict(path=str(primary_path),sha256=digest(primary_path),bytes=primary_path.stat().st_size),
        gates=dict(
            all_frozen_consumed_inputs_and_helpers_SHA=True,
            all_three_original_formal_resources_exit0=True,
            all37_old_and111_new_complete_leaves=True,
            exact_shared_original_endpoints_not_interval_overlap=True,
            same_positive_measure_and_five_old_basis=True,
            same_lambda_only_no_midpoint_redefinition=True,
            actual_old_u_derivative_and_source_rx=True,
            two_sided_zero_endpoint_height_difference=True,
            complete_mean_and_all_Gz_radial_terms=True,
            full_even20_nonmean_modes_retained=True,
            complete41_J_modes_in_both_centre_drifts=True,
            one_global_gauge_no_per_leaf_or_per_part_reset=True),
        new_Arb_Node_ODE_source_integrals=0,
        elapsed_seconds=time.monotonic()-began,peak_RSS_KiB=memory())
    io.atomic_json(summary_path,result)
    print(json.dumps(dict(event="complete_actual_R48_CF_same_measure_bridge",
        summary=str(summary_path),gates=result["gates"],
        maxima=result["complete_difference_maxima"],peak_RSS_KiB=result["peak_RSS_KiB"])),flush=True)


if __name__ == "__main__":
    main()
