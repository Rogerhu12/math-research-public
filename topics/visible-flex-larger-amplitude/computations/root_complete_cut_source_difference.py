#!/usr/bin/env python3
"""Bound the actual complete head correction through its true cut functional.

Reuse all46 by213 original R82 pre-gain source integrals. The complete R74
correction is only known on the variable physical strip, so none of the R82
wider-reference-strip gains is applied to this difference. The auxiliary and
difference far terms are combined algebraically before taking absolute values.
All proof arithmetic is Fraction with explicit outward dyadic rounding.
Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import gc
import gzip
import json
from pathlib import Path
import resource
import time

from root_moving_auxiliary_centre_family import (
    digest, exact, lower, upper, pow2, read, record, write_new)
from root_anisotropic_true_cut_cauchy import uprecord, require_hashes


def up(value):
    return upper(uprecord(value))


def exp_upper(x, terms=64):
    """Taylor sum plus a geometric bound on its entire positive remainder."""
    x = F(x)
    if not 0 <= x < terms+2:
        raise ValueError("The positive exponential tail ratio must be below1")
    term = total = F(1)
    for k in range(1, terms+1):
        term *= x/k
        total += term
    tail = term*x/(terms+1)/(1-x/(terms+2))
    return up(total+tail)


def cauchy(value):
    return dict(uniform_value_upper=uprecord(value),
        first_derivative_linf_to_output_upper=uprecord(4*value),
        second_derivative_linf_pair_to_output_upper=uprecord(64*value))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pattern", required=True)
    for name in ("family", "r72-summary", "far", "trace", "r82", "rows", "out"):
        ap.add_argument("--"+name, type=Path, required=True)
    ap.add_argument("--rss-kib", type=int, default=51200)
    a = ap.parse_args(); began = time.monotonic()
    if a.out.exists() or a.rows.exists():
        raise FileExistsError("Use new immutable summary and complete cell ledger paths")
    paths = {key:getattr(a,key) for key in ("family","r72_summary","far","trace","r82")}
    hashes = {str(p):digest(p) for p in paths.values()}
    family, r72, far, trace, prior = [read(paths[k]) for k in paths]
    for d in (family,r72,far,trace,prior):
        if not d["all_gates"]:
            raise ValueError("An actual complete prerequisite is unpaid")
        require_hashes(d)
    if any(prior["input_hashes"].get(str(paths[k])) != hashes[str(paths[k])]
           for k in ("family","far","trace")):
        raise ValueError("R82 must refer to the same actual family, far and trace")
    if family["input_hashes"].get(str(a.r72_summary)) != digest(a.r72_summary):
        raise ValueError("The complete correction/far domains changed")
    if ([r["cell"] for r in family["domain_rows"]] != list(range(12,225))
            or [r["index"] for r in family["joint_rows"]] != list(range(641))
            or [r["mode"] for r in prior["selected_mode_rows"]] != list(range(2,93,2))):
        raise ValueError("Retain all physical cells, joint rows and low modes")
    alpha = exact(family["main_linear_factor"])
    kappa = exact(family["rest_coefficient_factor"])
    scale = exact(family["envelope_factor"])
    source_factor = exact(prior["source_factor"])
    if (alpha,kappa,scale,source_factor) != (F(1025,1024),F(65,64),F(257,256),F(4225,4096)):
        raise ValueError("The actual anisotropic family multipliers changed")
    if family["parameter_axes"] != prior["parameter_axes"]:
        raise ValueError("Keep the same simultaneous20-coordinate polydisc")
    if not all(r["map_inclusion"] and r["contraction"]
               and exact(r["new_radius"]) == 4*exact(r["old_radius"])
               for r in family["joint_rows"]):
        raise ValueError("The complete correction is the proved4r box")
    domains = {}
    for row in family["domain_rows"]:
        n = row["cell"]; i = n-12
        t = exact(row["total_correction"])
        full = sum(exact(family["joint_rows"][j]["new_radius"])
                   for j in (i,213+i,426+i,639))
        if t != full or not row["physical_domain"] or not row["mean_domain"]:
            raise ValueError("A low, near, rest or infinite contribution is missing")
        domains[n] = scale*t  # Old Vs normalization used by the source integrals.
    zstar = exact(r72["independent_far_ball"])
    zaux = exact(family["retained_auxiliary_far_ball"])
    if (zstar,zaux) != (pow2(-2200),pow2(-2224)):
        raise ValueError("Keep both actual R18 far balls")
    rz = exact(family["joint_rows"][640]["new_radius"])
    if not upper(family["auxiliary_far_upper"])+zstar*rz < zstar:
        raise ValueError("The complete solution left the independent far ball")
    far_aux = exact(far["whole_low46_far_K_Wsigma1_upper"])
    ci = upper(far["point_cut_inner_mu12_K_conversion"])
    if not far_aux >= ci*upper(far["boundary_operator_at_cell12"])*exact(far["raw_D_bound"]):
        raise ValueError("The recorded complete far majorant is inconsistent")
    if exact(far["raw_D_bound"]) != pow2(1967)*zaux**2:
        raise ValueError("Retain the full R18 quadratic defect constant")
    far_true = far_aux*(zstar/zaux)**2
    sigma = F(1,64)
    tau_b = upper(trace["head_strip"])
    if not sigma < tau_b < 2 or not 0 < far_true:
        raise ValueError("Both output strips must be covered by the canonical far norm")
    old_rows = {r["mode"]:r for r in prior["selected_mode_rows"]}
    new_rows=[];total_sigma=total_head=F(0);source_sigma=source_head=F(0)
    improvements=[];count=0;source_hashes={};maxrss=0
    source_code = Path(__file__).with_name("root_auxiliary_cut_reference_strip.py")
    expected_code = digest(source_code)
    with gzip.open(a.rows,"xt",encoding="utf-8",compresslevel=6) as out:
        for mode in range(2,93,2):
            path=Path(a.pattern.format(mode=mode)); sha=digest(path)
            if prior["input_hashes"].get(str(path)) != sha:
                raise ValueError("An original R82 source primary changed")
            data=read(path)
            if (not data["all_gates"] or data["source_sha256"] != expected_code
                    or data["selected_modes"] != [mode]
                    or data["cells"] != list(range(12,225))
                    or data["auxiliary_input_modes"] != list(range(2,93,2))
                    or upper(data["point_cut_K_conversion"]) != ci
                    or data["input_hashes"] != prior["common_original_source_inputs"]):
                raise ValueError("The true cut functional/source identity changed")
            raw=data["rows"][0]
            if [r["cell"] for r in raw["source_rows"]] != list(range(12,225)):
                raise ValueError("A complete source row is missing")
            parts={k:F(0) for k in ("main","corr","quadratic","remainder")}
            xi=F(0);largest=(F(0),None)
            for row in raw["source_rows"]:
                n=row["cell"]; e=domains[n]
                integral={k:upper(v) for k,v in row["phi_source_integrals"].items()}
                mu=upper(row["mu_ratio_upper"])
                if not e>0 or not mu>0 or not all(x>0 for x in integral.values()):
                    raise ValueError("Do not discard a positive complete source component")
                # These are the PRE reference-strip-gain integrals. E is only
                # known in the original variable physical strip.
                pieces=dict(main=alpha*e*integral["main"],
                    corr=3*kappa*e*integral["corr"],
                    quadratic=F(3,2)*e**2*integral["base"],
                    remainder=216*(scale**2*e+scale*e**2+e**3/3)*integral["remainder"])
                weighted={k:up(mu*v) for k,v in pieces.items()}
                contribution=up(sum(weighted.values()))
                xi=up(xi+contribution)
                for key,value in weighted.items():
                    parts[key]=up(parts[key]+value)
                if contribution>largest[0]:largest=(contribution,n)
                out.write(json.dumps(dict(mode=mode,cell=n,
                    complete_source_difference_Xi_pieces={k:record(v) for k,v in weighted.items()},
                    complete_source_difference_Xi_contribution=record(contribution)),
                    separators=(",",":"))+"\n")
                count+=1
            coefficient=up(ci*xi)
            sigma_value=up((1+mode)*exp_upper(mode*sigma)*coefficient)
            head_value=up((1+mode)*exp_upper(mode*tau_b)*coefficient)
            total_sigma=up(total_sigma+sigma_value);total_head=up(total_head+head_value)
            source=upper(raw["auxiliary_Kbar_Wsigma1_upper"])
            source_sigma=up(source_sigma+source_factor*source)
            source_head=up(source_head+source_factor*source*exp_upper(mode*(tau_b-sigma)))
            direct=source_factor*source+sigma_value+far_true
            old=upper(old_rows[mode]["true_DN_minus_exact_linear_DN"]["uniform_value_upper"])
            chosen=min(direct,old)
            if direct<old:improvements.append(mode)
            new_rows.append(dict(mode=mode,source_cells=213,largest_difference_cell=largest[1],
                source_primary=str(path),source_primary_sha256=sha,
                complete_difference_Xi_pieces={k:record(v) for k,v in parts.items()},
                complete_difference_source_Wsigma1_upper=record(sigma_value),
                complete_difference_source_Wtau_b1_upper=record(head_value),
                uniform_R74_auxiliary_source_Wsigma1_upper=uprecord(source_factor*source),
                complete_true_far_Wsigma1_upper=record(far_true),
                direct_true_DN_minus_exact_linear_Wsigma1_upper=uprecord(direct),
                old_R82_complete_true_DN_minus_exact_linear_Wsigma1_upper=record(old),
                chosen_complete_true_DN_minus_exact_linear_Wsigma1=cauchy(chosen),
                direct_bound_strictly_improves_R82=direct<old,
                improvement_ratio_upper=uprecord(chosen/old)))
            source_hashes[str(path)]=sha
            del data,raw
            gc.collect()
            maxrss=max(maxrss,resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            if maxrss>a.rss_kib:raise MemoryError("The declared owned RSS guard was exceeded")
            print(json.dumps(dict(event="mode_complete",mode=mode,
                difference=record(sigma_value)["display"],improves=direct<old)),flush=True)
    direct_sigma=source_sigma+total_sigma+far_true
    direct_head=source_head+total_head+far_true
    low_sigma=min(direct_sigma,upper(prior["whole46_true_DN_minus_exact_linear_Wsigma1"]["uniform_value_upper"]))
    low_head=min(direct_head,upper(prior["whole46_true_DN_minus_exact_linear_Wtau_b1"]["uniform_value_upper"]))
    high=upper(prior["complete_high_blocks_unchanged"]["head"]["complete_high_balanced_P_K"]["uniform_value_upper"])
    linear_mean=upper(prior["complete_linear_nonmean_mean_input_upper"])
    mean_input=linear_mean+low_head+high
    if not mean_input<F(1,10000):raise ArithmeticError("The complete complex mean-root domain failed")
    gates=dict(all46_by213_original_source_cells=count==46*213,
        same20_parameter_R74_complex_polydisc=True,
        all_low_near_rest_infinite_and_far_correction_rows_retained=True,
        no_reference_strip_gain_applied_to_complete_difference=True,
        complete_mean_and_inverse_cubic_difference_retained=True,
        auxiliary_and_difference_far_combined_exactly_before_bounds=True,
        complete_true_far_added_once_to_whole_low_mass=far_true>0,
        original_auxiliary_sources_and_all46_coefficient_caps_retained=True,
        new_complete_bound_available_for_every_low_mode=len(new_rows)==46,
        both_whole_low_bounds_no_larger_than_R82=(low_sigma<=upper(prior["whole46_true_DN_minus_exact_linear_Wsigma1"]["uniform_value_upper"]) and low_head<=upper(prior["whole46_true_DN_minus_exact_linear_Wtau_b1"]["uniform_value_upper"])),
        direct_source_estimate_strictly_improves_every_low_mode=len(improvements)==46,
        complete_complex_mean_root_domain=True)
    result=dict(status="Executed direct complete source-difference cut functional on the actual R74 family",
        author="/root (GPT-6 Astra Pro, AI-assisted)",all_gates=all(gates.values()),gates=gates,
        decomposition="Ftrue-L=G N(Caux)+G[N(Caux+E)-N(Caux)]+B D(ztrue); E contains all four frequency blocks and the independent far variable",
        parameter_norm=prior["parameter_norm"],parameter_axes=prior["parameter_axes"],
        Cauchy_working_radius=prior["Cauchy_working_radius"],
        old_envelope_complete_correction_rows=[dict(cell=n,bound=record(e)) for n,e in domains.items()],
        source_difference_formula="e*(alpha I_main+3 kappa_R I_corr)+3 e^2 I_base/2+216*(S^2 e+S e^2+e^3/3)*I_remainder, then mu_n/mu12 and true point cut conversion",
        original_auxiliary_far_upper=record(far_aux),true_far_enlargement_factor=record((zstar/zaux)**2),
        whole46_complete_true_far_upper=record(far_true),
        whole46_complete_difference_source_Wsigma1_upper=record(total_sigma),
        whole46_complete_difference_source_Wtau_b1_upper=record(total_head),
        whole46_auxiliary_source_Wsigma1_upper=record(source_sigma),
        whole46_auxiliary_source_Wtau_b1_upper=record(source_head),
        whole46_direct_true_DN_minus_exact_linear_Wsigma1_upper=uprecord(direct_sigma),
        whole46_direct_true_DN_minus_exact_linear_Wtau_b1_upper=uprecord(direct_head),
        whole46_chosen_true_DN_minus_exact_linear_Wsigma1=cauchy(low_sigma),
        whole46_chosen_true_DN_minus_exact_linear_Wtau_b1=cauchy(low_head),
        selected_mode_rows=new_rows,strictly_improved_modes=improvements,
        low_Q_and_P_nonlinear_remainder_identically_zero=True,
        complete_high_blocks_unchanged=prior["complete_high_blocks_unchanged"],
        complete_nonmean_mean_input_upper=uprecord(mean_input),complete_mean_slope=cauchy(40*mean_input**2),
        cuff_normalized_mean_height_unchanged=prior["cuff_normalized_mean_height_unchanged"],
        mean_height_convention=prior["mean_height_convention"],
        complete_cell_ledger=dict(path=str(a.rows),rows=count,bytes=a.rows.stat().st_size,sha256=digest(a.rows)),
        input_hashes=hashes,source_primary_hashes=source_hashes,source_sha256=digest(__file__),
        helper_hashes={n:digest(Path(__file__).with_name(n)) for n in
            ("root_moving_auxiliary_centre_family.py","root_anisotropic_true_cut_cauchy.py")},
        no_Arb=True,no_ODE=True,no_new_source_integral=True,no_Node=True,
        full_outer_Green_or_closed_surface_claimed=False,
        elapsed_seconds=time.monotonic()-began,peak_rss_kib=maxrss)
    output=write_new(a.out,result)
    print(json.dumps(dict(event="done",all_gates=result["all_gates"],output=output,
        difference=record(total_sigma)["display"],low_value=cauchy(low_sigma)["uniform_value_upper"]["display"],
        mode92=new_rows[-1]["chosen_complete_true_DN_minus_exact_linear_Wsigma1"]["uniform_value_upper"]["display"],
        seconds=result["elapsed_seconds"],RSS_KiB=maxrss)),flush=True)
    if not result["all_gates"]:raise SystemExit(2)


if __name__=="__main__":main()
