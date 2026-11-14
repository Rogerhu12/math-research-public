#!/usr/bin/env python3
"""Rebuilt actual physical-r substage candidate, optionally with a carrier.

The physical mode defines a NEW R48 candidate from the same saved endpoint
jets and the newly certified physical-r moments. It is not the old source-x
polynomial. The carrier mode adds F=HL+a(r-rL)+b*integral(dr/w) and applies
R48 to the exact residual jets. Both modes use actual physical derivatives,
the complete R64 mean, every finite J coefficient, and R77 on every leaf.
No unperformed old result or lost source SHA is reconstructed.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import gzip
import json
from pathlib import Path
import resource
import time

from flint import arb, acb, ctx
from closure_split_joint_io import read, digest
from closure_real_head_source_enclosure import exact_q, ball_record
from closure_real_head_green_enclosure import ball
from tail_outer_weighted_compatible import normalized_endpoint_jet, make_weighted_candidate, MOMENT_KEYS
from tail_outer_centered_quartic_fields_v2 import (
    weighted_panel_fields, finite, intersection, rational_identity_checks)
from tail_outer_candidate_domain import nonnegative_integral
from tail_outer_general_mean_bounds import general_mean_and_defect
from tail_outer_substage_span_refinement import (
    finite_complete_J, MINIMUM_FIELDS, compact_ball, rounded_dyadic,
    cosine_coefficients, cosine_norm)
from tail_outer_original_piece_finite_j import r77
from tail_r41_connection_polynomial import add, scale, product, derivative
from tail_outer_physical_substage_moments_rebuilt import check_sources, check_record, write_json

EXPECTED_AUDIT = {
    "tail_outer_weighted_compatible.py": "03c88b010447c78e4fb6bb26f0d3704fafd23510d16cc00084f315daa07f3d1b",
    "tail_outer_candidate_domain.py": "17d6b7d85be80f8f40b3eec411ae49a73c51c6b624d030df57b94202a7d08690",
    "tail_outer_general_mean_bounds.py": "4b16b860eb89d7b8f19d7f8ff05642ea0122b0a2016d4be623d5483430023a5c",
    "tail_outer_substage_span_refinement.py": "85bf30e818e7ab92107a5f5a537225afb9273877327bf6e0092b303b01a1b5d8",
    "tail_outer_original_piece_finite_j.py": "b5196622ed649c6e3a3d6ad3227f30b0c54651d402c5866cfa2102d5e6def2d4",
}

def jets(node):
    return {key:{int(m):ball(v) for m,v in node["shared_physical_jets"][key].items()}
        for key in ("H","Hr","Hrr")}

def normalized(fields, node, width):
    w,wr = ball(node["w"]),ball(node["wr"])
    return normalized_endpoint_jet(fields["H"],fields["Hr"],fields["Hrr"],
        w=w,radius_u=width,log_w_u=width*wr/w)

def make_candidate(left,right,width,total,carrier,A_total=None):
    jl,jr = jets(left),jets(right)
    info = dict(carrier=carrier,original_left=jl,original_right=jr)
    if not carrier:
        candidate = make_weighted_candidate(normalized(jl,left,width),normalized(jr,right,width),total)
        return candidate,info
    if A_total is None or not A_total > 0:
        raise ArithmeticError("The complete positive carrier integral is required")
    rL,wL,wrL = ball(left["radius"]),ball(left["w"]),ball(left["wr"])
    wR,wrR = ball(right["w"]),ball(right["wr"])
    aa = {m:m*m*jl["H"][m]/rL for m in jl["H"]}
    bb = {m:wL*(jl["Hr"][m]-aa[m]) for m in aa}
    gl = dict(H={m:arb(0) for m in aa},Hr={m:arb(0) for m in aa},
        Hrr={m:jl["Hrr"][m]+bb[m]*wrL/(wL*wL) for m in aa})
    gr = dict(H={m:jr["H"][m]-jl["H"][m]-aa[m]*width-bb[m]*A_total for m in aa},
        Hr={m:jr["Hr"][m]-aa[m]-bb[m]/wR for m in aa},
        Hrr={m:jr["Hrr"][m]+bb[m]*wrR/(wR*wR) for m in aa})
    candidate = make_weighted_candidate(normalized(gl,left,width),normalized(gr,right,width),total)
    info.update(a=aa,b=bb,A_total=A_total,residual_left=gl,residual_right=gr)
    return candidate,info

def fields_on_leaf(candidate,info,row,width):
    u = intersection(ball(row["u"]),arb(0).union(arb(1)))
    before = {key:nonnegative_integral(row["prefix_moments"][key]) for key in MOMENT_KEYS}
    after = {key:nonnegative_integral(row["suffix_moments"][key]) for key in MOMENT_KEYS}
    G,kappa,kappa_r = weighted_panel_fields(candidate,u=u,u_x=1/width,
        prefix_moments=before,suffix_moments=after)
    if not info["carrier"]:
        return G,kappa,kappa_r,None
    w,wr,radius = ball(row["w"]),ball(row["wr"]),ball(row["radius"])
    offset = nonnegative_integral(row["physical_offset"])
    Apre = nonnegative_integral(row["carrier_prefix"])
    Aafter = nonnegative_integral(row["carrier_suffix"])
    intersection(Apre+Aafter,info["A_total"])
    H,K,Kr,stable = {},{},{},{}
    for m in info["a"]:
        aa,bb = info["a"][m],info["b"][m]
        g,kap,kapr = 2*G[m].real,2*kappa[m].real,2*kappa_r[m].real
        hl = info["original_left"]["H"][m]+aa*offset+bb*Apre+g
        hr = (info["original_right"]["H"][m]-aa*(width-offset)-bb*Aafter
            -(info["residual_right"]["H"][m]-g))
        height = intersection(hl,hr)
        kval = aa/w+bb/(w*w)+kap
        krval = -aa*wr/(w*w)-2*bb*wr/(w*w*w)+kapr
        numerator = aa*(1-m*m)*offset-m*m*bb*Apre-m*m*g
        linear = kapr+(wr/w)*(2*kap+numerator/(radius*w))
        for dest,value in ((H,height),(K,kval),(Kr,krval),(stable,linear)):
            dest[m] = dest[-m] = acb(finite(value)/2)
    details = dict(G=G,kappa=kappa,kappa_r=kappa_r,linear=stable)
    return H,K,Kr,details

def complete_carrier_J(H,K,Kr,details,*,radius,g,r64,cutoff,weights):
    full = finite_complete_J(H,K,Kr,radius=radius,g=g,r64=r64,cutoff=cutoff,weights=weights)
    if details is None:
        return full
    w,ell = g["w"],g["log_w_x"]
    z,E = w*w,1+w*w
    P = scale(derivative(H),1/(radius*w))
    T = derivative(P)
    U = add(derivative(K),scale(P,-1))
    lnm = add(K,scale(T,E))
    direct_linear = add(Kr,scale(add(scale(K,2),T),ell))
    linear = {}
    for m,value in details["linear"].items():
        if not direct_linear[m].imag.contains(0):
            raise ArithmeticError("Real carrier linear Fourier symmetry failed")
        linear[m] = acb(intersection(value.real,direct_linear[m].real))
    quadratic = add(product(lnm,Kr),scale(product(U,U),-E/radius),
        scale(add(product(K,K),scale(product(P,P),z),product(K,T)),ell))
    c,cx = full["c"],full["cx"]
    J = add(linear,quadratic,scale(linear,c),scale(lnm,cx),
        {0:acb(cx*(1+c)+ell*(2*c+c*c))})
    new = cosine_coefficients(J,2*cutoff)
    coeff = {m:intersection(full["coefficients"][m],value) for m,value in new.items()}
    factor = full["physical_conversion_factor"]
    bounds = dict(full["bounds"])
    bounds["complete_J_l1"] = min(bounds["complete_J_l1"],cosine_norm(coeff))
    bounds["complete_J_W1_tau"] = min(bounds["complete_J_W1_tau"],cosine_norm(coeff,weights))
    bounds["finite_J_l1_Darboux_upper"] = min(bounds["finite_J_l1_Darboux_upper"],
        (factor*cosine_norm(coeff)).upper())
    for name,subset in (
            ("mean",{0:coeff[0]}),
            ("retained_nonmean",{m:v for m,v in coeff.items() if 0<m<=cutoff}),
            ("outside_saved_height",{m:v for m,v in coeff.items() if m>cutoff})):
        key = "finite_J_"+name+"_l1_Darboux_upper"
        bounds[key] = min(bounds[key],(factor*cosine_norm(subset)).upper())
    full.update(coefficients=coeff,bounds=bounds,carrier_linear_identity_used=True)
    return full

def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ("candidate","moment-summary","moment-resource","out-prefix"):
        p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--mode",choices=("physical","carrier"),default="physical")
    p.add_argument("--rss-limit-mib",type=int,default=40)
    a = p.parse_args()
    summary = Path(str(a.out_prefix)+"-summary.json")
    recovery = Path(str(a.out_prefix)+"-recovery.json")
    if summary.exists() or recovery.exists():
        raise FileExistsError("Use a fresh complete candidate audit prefix")
    ctx.prec,ctx.threads = 192,1
    started = time.monotonic()
    paths = (a.candidate,a.moment_summary,a.moment_resource)
    inputs = {str(path):digest(path) for path in paths}
    old,meta,usage = map(read,paths)
    if (usage["exitcode"] != 0 or usage["termination_signal"] is not None
            or not all(old["gates"].values()) or not all(meta["gates"].values())
            or old["cell"] != meta["cell"] or old["segment"] != meta["segment"]
            or old["modes"] != meta["modes"] or old["tau"] != meta["tau"]
            or old["nodes"] != meta["nodes"]
            or meta["input_hashes"].get(str(a.candidate)) != inputs[str(a.candidate)]):
        raise ValueError("The complete real moment run and exact same endpoint data are required")
    cmd = usage["command"]
    prefix = cmd[cmd.index("--out-prefix")+1]
    if Path(prefix+"-summary.json") != a.moment_summary:
        raise ValueError("The supplied formal exit belongs to another moment summary")
    if a.mode == "carrier" and not meta.get("carrier_integrals_complete"):
        raise ValueError("Carrier mode requires the formal complete additional integral")
    sources = check_sources((Path(__file__).name,))
    here = Path(__file__).parent
    got = {name:digest(here/name) for name in EXPECTED_AUDIT}
    if got != EXPECTED_AUDIT:
        raise ValueError("A complete mean, finite-J or endpoint mathematical helper changed")
    sources.update(got)
    check_record(old,sources)
    check_record(meta,sources)
    # Bind every requested primary before constructing the new candidate.
    for group in meta["groups"]:
        path = Path(group["path"])
        if digest(path) != group["sha256"]:
            raise ValueError("A complete true moment primary changed")
        inputs[str(path)] = group["sha256"]
    modes,tau = old["modes"],F(old["tau"])
    cutoff = max(modes)
    weights = {m:((1+m)*(exact_q(tau)*m).exp()).upper()
        for m in range(0,2*cutoff+1,2)}
    checks = rational_identity_checks()
    parts,global_maxima,global_minima = [],{},{}
    counts = 0
    def memory():
        peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if peak > a.rss_limit_mib*1024:
            raise MemoryError("Owned complete candidate audit exceeded observed RSS gate")
        return peak
    def checkpoint(stage,error=None):
        write_json(recovery,dict(status="Recovery-only completed leaves, not a final candidate certificate",
            stage=stage,mode=a.mode,completed=counts,parts=parts,error=error,
            input_hashes=inputs,source_hashes=sources,elapsed_seconds=time.monotonic()-started))
    def update(table,key,value,witness,minimum=False):
        value = finite(value).lower() if minimum else finite(value).upper()
        if key not in table or (value<table[key]["value"] if minimum else value>table[key]["value"]):
            table[key] = dict(value=value,witness=witness)
    def records(table):
        return {key:dict(value=ball_record(v["value"]),witness=v["witness"]) for key,v in table.items()}
    total_mean_correction,total_mean_change = arb(0),arb(0)
    try:
        for group in meta["groups"]:
            k = group["part"]
            source = Path(group["path"])
            output = Path(str(a.out_prefix)+f"-part{k:02d}-fields.jsonl.gz")
            if output.exists():
                raise FileExistsError("Use a fresh actual candidate primary")
            width = ball(group["true_width"])
            if not width > 0:
                raise ArithmeticError("Actual physical width is not positive")
            total = {key:ball(group["total_true_positive_moments"][key]) for key in MOMENT_KEYS}
            A_total = ball(group["carrier_integral_total"]) if a.mode == "carrier" else None
            candidate,info = make_candidate(old["nodes"][k],old["nodes"][k+1],width,total,
                a.mode=="carrier",A_total)
            old_part = next(row for row in old["parts"] if row["part"]==k)
            old_cmax = ball(old_part["bounds"]["complete_mean_abs"]["value"]).upper()
            if not old_cmax >= 0:
                raise ArithmeticError("The original complete mean bound is invalid")
            local_maxima,local_minima = {},{}
            part_mean_correction,part_mean_change = arb(0),arb(0)
            covered,count = F(group["source_left"]),0
            header=trailer=False
            with gzip.open(source,"rt") as inp,gzip.open(output,"xt",compresslevel=6) as out:
                out.write(json.dumps(dict(kind="header",cell=old["cell"],segment=old["segment"],part=k,
                    mode=a.mode,new_candidate_definition=True,
                    derivative_coordinate="physical r, r_r=1; source x only for complete coverage",
                    complete_J_cosine_modes=list(range(0,2*cutoff+1,2)),
                    input_hashes=inputs,source_hashes=sources),separators=(",",":"))+"\n")
                for line in inp:
                    row=json.loads(line)
                    if row["kind"]=="header":
                        if (header or count or row["input_hashes"] != meta["input_hashes"]
                                or row["source_hashes"] != meta["source_hashes"]):
                            raise ValueError("The complete moment header does not match its summary")
                        header=True
                        continue
                    if row["kind"]=="trailer":
                        if trailer or not row["complete"] or row["panels"]!=count:
                            raise ValueError("The complete moment trailer does not match")
                        trailer=True
                        continue
                    if (not header or trailer or row["kind"]!="complete_physical_substage_moment_leaf"
                            or row["part"]!=k or row["panel"]!=count):
                        raise ValueError("Unexpected physical moment row")
                    left,right=F(row["x_left"]),F(row["x_right"])
                    if left!=covered or not left<right<=F(group["source_right"]):
                        raise ValueError("Actual source partition is not exactly complete")
                    rxsource=ball(row["source_radius_x"])
                    if not rxsource>0:
                        raise ArithmeticError("Actual source-to-radius monotonicity is missing")
                    radius,w,ell=ball(row["radius"]),ball(row["w"]),ball(row["log_w_r"])
                    H,K,Kr,details=fields_on_leaf(candidate,info,row,width)
                    answer=general_mean_and_defect(H,K,Kr,modes=modes,weights=weights,
                        radius=radius,radius_x=arb(1),w=w,log_w_x=ell)
                    if not answer["gate"]:
                        raise ArithmeticError("The actual candidate complete mean gate failed: "+
                            str((k,count,answer.get("failure"))))
                    full=complete_carrier_J(H,K,Kr,details,radius=radius,
                        g=dict(w=w,radius_x=arb(1),log_w_x=ell),r64=answer,
                        cutoff=cutoff,weights=weights)
                    values=dict(answer["bounds"],**full["bounds"],**r77(full,answer,w))
                    witness=dict(segment=old["segment"],part=k,panel=count,
                        source_left=str(left),source_right=str(right),
                        physical_u=row["u"],derivative_coordinate="physical r")
                    for key,value in values.items():
                        update(local_maxima,key,value,witness)
                        update(global_maxima,key,value,witness)
                    for key in MINIMUM_FIELDS:
                        if not finite(answer[key]).lower()>0:
                            raise ArithmeticError("A real or analytic complete mean margin failed")
                        update(local_minima,key,answer[key],witness,True)
                        update(global_minima,key,answer[key],witness,True)
                    leaf_width=ball(row["source_width"])
                    if not leaf_width>0:
                        raise ArithmeticError("True positive physical leaf measure is missing")
                    cm=answer["bounds"]["complete_mean_abs"].upper()
                    part_mean_correction += (leaf_width*w.upper()*cm).upper()
                    part_mean_change += (leaf_width*w.upper()*(cm+old_cmax)).upper()
                    record=dict(kind="complete_new_physical_substage_R64_J_R77_leaf",**witness,
                        complete_mean=True,mode=a.mode,
                        source={key:compact_ball(value) for key,value in (
                            ("radius",radius),("radius_x",arb(1)),("w",w),("log_w_x",ell),
                            ("source_radius_x",rxsource),
                            ("physical_conversion_factor",full["physical_conversion_factor"]))},
                        bounds_upper={key:rounded_dyadic(value,upper=True) for key,value in values.items()},
                        gates_lower={key:rounded_dyadic(answer[key],upper=False) for key in MINIMUM_FIELDS},
                        full_J_cosine_intervals=[compact_ball(full["coefficients"][m])
                            for m in range(0,2*cutoff+1,2)],
                        actual_nonmean_jet_cosine_intervals={key:[compact_ball(2*v[m].real) for m in modes]
                            for key,v in (("H",H),("Kbar",K),("Kbar_r",Kr))})
                    out.write(json.dumps(record,separators=(",",":"),allow_nan=False)+"\n")
                    counts+=1;count+=1;covered=right
                    if count%32==0:
                        checkpoint("complete candidate leaves")
                        print(json.dumps(dict(event="new_candidate_actual_J_progress",mode=a.mode,
                            part=k,panels=count,total=group["panels"],peak_RSS_KiB=memory())),flush=True)
                if not (header and trailer and covered==F(group["source_right"]) and count==group["panels"]):
                    raise ValueError("A complete requested physical substage was not validated")
                out.write(json.dumps(dict(kind="trailer",complete=True,part=k,panels=count),
                    separators=(",",":"))+"\n")
            if output.stat().st_size>=5_000_000:
                raise ArithmeticError("A primary exceeds the single-file limit")
            carrier_record=None
            if info["carrier"]:
                carrier_record=dict(a={str(m):ball_record(v) for m,v in info["a"].items()},
                    b={str(m):ball_record(v) for m,v in info["b"].items()},
                    A_total=ball_record(info["A_total"]),
                    residual_left={key:{str(m):ball_record(v) for m,v in vals.items()}
                        for key,vals in info["residual_left"].items()},
                    residual_right={key:{str(m):ball_record(v) for m,v in vals.items()}
                        for key,vals in info["residual_right"].items()})
            parts.append(dict(part=k,panels=count,source_left=group["source_left"],
                source_right=group["source_right"],true_width=group["true_width"],
                bounds=records(local_maxima),minima=records(local_minima),
                bubble_coefficients={str(m):ball_record(v) for m,v in candidate["bubble_coefficient"].items()},
                carrier=carrier_record,mean_correction_height_abs=ball_record(part_mean_correction.upper()),
                mean_height_change_from_original_abs=ball_record(part_mean_change.upper()),
                path=str(output),sha256=digest(output),bytes=output.stat().st_size))
            total_mean_correction+=part_mean_correction
            total_mean_change+=part_mean_change
            checkpoint("complete physical substage candidate")
    except BaseException as error:
        checkpoint("failed",dict(type=type(error).__name__,message=str(error)))
        raise
    gates=dict(formal_true_moment_exit0_and_primary_identity=True,
        same_true_metric_and_original_shared_physical_two_jets=True,
        complete_exact_requested_source_and_physical_radius_cover=True,
        complete_R64_mean_and_all_inverse_domains=True,
        actual_physical_derivatives_not_ODE_substitutes=True,
        full_finite_J_through_twice_height_cutoff=True,
        full_R77_zero_mode_every_leaf=True,
        one_mean_constant_with_explicit_height_change_bound=True)
    result=dict(author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",scope=__doc__,
        schema="rebuilt-physical-substage-candidate-v2",mode=a.mode,
        status="Complete NEW candidate on the explicitly requested substages",
        cell=old["cell"],segment=old["segment"],modes=modes,tau=str(tau),
        parts=parts,panels=counts,nodes=old["nodes"],
        bounds=records(global_maxima),minima=records(global_minima),gates=gates,
        new_candidate_definition=True,old_candidate_not_intersected_or_selected=True,
        endpoint_nonmean_two_jets_exact_by_construction=True,
        complete_mean_jet_match_conditional_on_same_R64_root=True,
        mean_height_uses_one_global_constant=True,
        total_mean_correction_height_abs=ball_record(total_mean_correction.upper()),
        total_mean_height_change_from_original_abs=ball_record(total_mean_change.upper()),
        two_fixed_mean_endpoint_heights_not_implicitly_claimed=True,
        input_hashes=inputs,source_hashes=sources,finite_horner_checks=checks,
        original_candidate_input_hashes=old["input_hashes"],
        whole_original_segment_covered=meta["whole_original_segment_covered"],
        source_evaluation_or_new_integration=False,new_radial_ODE_or_Node=False,
        exact_outer_solution_claimed=False,
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=memory())
    write_json(summary,result,fresh=True)
    print(json.dumps(dict(event="complete_rebuilt_candidate_audit",mode=a.mode,
        summary=str(summary),panels=counts,gates=gates,
        Darboux=result["bounds"]["R77_full_physical_Darboux_upper"],
        seconds=result["elapsed_seconds"],peak_RSS_KiB=result["peak_RSS_KiB"])),flush=True)

if __name__=="__main__":
    main()
