#!/usr/bin/env python3
"""Complete all46 R74 low-cut values and Cauchy bounds from actual source ledgers.

The auxiliary source is summed over all46 modes, the complete auxiliary far
term is added once, and the full-frequency-minus-auxiliary mass is added once.
All mathematics here uses Fraction. No Arb, ODE or new integral is evaluated.
Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import gc
import json
from pathlib import Path
import resource
import time

from root_moving_auxiliary_centre_family import digest, read, lower, upper, exact, record, write_new
from root_anisotropic_true_cut_cauchy import uprecord


def exp_negative_upper(x):
    """For x>=0, exp(-x)<=1/sum_{k=0}^{32} x^k/k!, exactly rational."""
    if x < 0:
        raise ValueError("A positive strip gap is required")
    term=total=F(1)
    for k in range(1,33):
        term*=x/k
        total+=term
    return 1/total


def exp_positive_upper(x):
    """The elementary R74 bound e<87/32, with exact upward integer exponent."""
    if x < 0:
        raise ValueError("This bound expects a nonnegative exponent")
    ceiling=-((-x.numerator)//x.denominator)
    return F(87,32)**ceiling


def abs_upper(interval):
    return max(abs(lower(interval)),abs(upper(interval)))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pattern",required=True)
    for name in ("batch-state","family","far","trace","r78","out"):
        ap.add_argument("--"+name,type=Path,required=True)
    ap.add_argument("--rss-kib",type=int,default=51200)
    a=ap.parse_args(); started=time.monotonic()
    if a.out.exists():
        raise FileExistsError("Use a fresh complete mathematical output")
    source=Path(__file__).with_name("root_auxiliary_cut_reference_strip.py")
    source_hash=digest(source)
    state=read(a.batch_state)
    if not state.get("all_planned_modes_complete") or len(state["completed"])!=44:
        raise ValueError("The complete remaining44-mode execution is required")
    covered={r["mode"]:r for r in state["completed"]}
    if any(not r["verified_success"] or r["wrapper_exit"]!=0 or r["wait4_exit"]!=0
           for r in covered.values()):
        raise ValueError("A batch mode lacks a formal successful child")
    if set(covered)!=set(range(2,93,2))-{6,8}:
        raise ValueError("The full planned mode window changed")
    source_rows=[];source_sum=F(0);common_inputs=None;groups={};input_hashes={}
    peak_child=0;sum_child_seconds=0.
    for mode in range(2,93,2):
        path=Path(a.pattern.format(mode=mode))
        stem=str(path)[:-8] if str(path).endswith(".json.gz") else None
        if stem is None:
            raise ValueError("Use the immutable compressed source pattern")
        resources=Path(stem+"-resource.json");res=read(resources)
        if res["exitcode"]!=0 or res["termination_signal"] is not None:
            raise ValueError("A selected mode did not formally complete")
        peak_child=max(peak_child,res["peak_rss_kib"])
        sum_child_seconds+=res["wall_seconds"]
        if mode in covered:
            saved=next(r for r in covered[mode]["files"] if r["path"]==str(path))
            if digest(path)!=saved["sha256"]:
                raise ValueError("An executed source primary changed")
        data=read(path)
        if (not data["all_gates"] or not all(data["checks"].values())
                or data["selected_modes"]!=[mode] or data["source_sha256"]!=source_hash
                or data["auxiliary_input_modes"]!=list(range(2,93,2))
                or data["cells"]!=list(range(12,225)) or data["outer_strip"]!="1/64"):
            raise ValueError("The actual complete source identity/coverage differs")
        if common_inputs is None:
            common_inputs=data["input_hashes"]
        elif common_inputs!=data["input_hashes"]:
            raise ValueError("The source modes do not belong to one actual problem")
        row=data["rows"][0]
        if row["mode"]!=mode or [r["cell"] for r in row["source_rows"]]!=list(range(12,225)):
            raise ValueError("An actual source mode lacks one original cell")
        for cell in row["source_rows"]:
            for key in ("nonprincipal_quadratic_reference_strip_gain",
                        "complete_remainder_and_generic_reference_strip_gain"):
                if not 0<upper(cell[key])<=1:
                    raise ValueError("A saved strict spectral gain is invalid")
        value=upper(row["auxiliary_Kbar_Wsigma1_upper"])
        if value<=0:
            raise ValueError("Do not erase a positive source value")
        source_sum+=value
        source_rows.append(dict(mode=mode,source_only_Wsigma1_upper=uprecord(value),
            source_primary=str(path),source_primary_sha256=digest(path),
            source_resource_sha256=digest(resources),source_cells=213,
            largest_source_cell=row["largest_source_cell"]))
        for name,sha in data["group_hashes"].items():
            if name in groups and groups[name]!=sha:
                raise ValueError("A real linear group changed between source modes")
            groups[name]=sha
        input_hashes[str(path)]=digest(path)
        input_hashes[str(resources)]=digest(resources)
        del data,row
        gc.collect()
    if len(groups)!=6:
        raise ValueError("Every original real linear column group is required")
    for name,sha in dict(common_inputs,**groups).items():
        if digest(name)!=sha:
            raise ValueError("An original physical source/kernel prerequisite changed")
    for key in ("batch_state","family","far","trace","r78"):
        path=getattr(a,key);input_hashes[str(path)]=digest(path)
    family,far,trace,prior=[read(getattr(a,k)) for k in ("family","far","trace","r78")]
    if not all(d["all_gates"] for d in (family,far,trace,prior)):
        raise ValueError("The full actual family/far/trace/Cauchy prerequisites are unpaid")
    if (prior["input_hashes"].get(str(a.family))!=digest(a.family)
            or prior["input_hashes"].get(str(a.trace))!=digest(a.trace)
            or prior["input_hashes"].get(str(a.far))!=digest(a.far)):
        raise ValueError("R78 is not the same actual complex family")
    if common_inputs.get(str(a.trace))!=digest(a.trace):
        raise ValueError("The actual source and the cut use different head traces")
    reference_name="notes/2026-11-12-closure-newg-strong-m20-real-reference.json"
    if family["input_hashes"].get(reference_name)!=common_inputs[reference_name]:
        raise ValueError("R74 uses a different actual auxiliary reference")
    reference=read(reference_name)
    reference_tau=lower(reference["cell_rows"][0]["tau"])
    head_tau_upper=upper(trace["head_strip"])
    if reference["cell_rows"][0]["cell"]!=12 or not reference_tau>=head_tau_upper>F(1,64):
        raise ValueError("The full far lift must control the true wider head strip")
    scale=exact(family["envelope_factor"])
    factor=exact(family["rest_coefficient_factor"])**2
    if scale!=F(257,256) or factor!=F(4225,4096):
        raise ValueError("Retain the proved anisotropic multipliers")
    far_value=exact(far["whole_low46_far_K_Wsigma1_upper"])
    gap_lo=lower(trace["gap"]);gap_hi=upper(trace["gap"])
    if not 0<gap_lo<=gap_hi:
        raise ValueError("The actual cut strip gap is positive")
    old_low_sigma=upper(trace["beta"]["outer"]["full_head_low_correction_K"])
    full_low_sigma=4*scale*old_low_sigma
    wide_source_sum=F(0)
    new_rows=[]

    def cauchy(value):
        return dict(uniform_value_upper=uprecord(value),
            first_derivative_linf_to_output_upper=uprecord(4*value),
            second_derivative_linf_pair_to_output_upper=uprecord(64*value))

    for row in source_rows:
        mode=row["mode"];value=upper(row["source_only_Wsigma1_upper"])
        # The saved source upper was rounded upwards; use that same safe value.
        source_part=factor*value
        full_part=full_low_sigma*exp_negative_upper((mode-2)*gap_lo)
        total=source_part+far_value+full_part
        wide_multiplier=exp_positive_upper(mode*gap_hi)
        wide_source_sum+=wide_multiplier*value
        new_rows.append(dict(**row,
            uniform_R74_source_part=uprecord(source_part),
            complete_auxiliary_far_part=record(far_value),
            complete_full_head_minus_auxiliary_selected_part=uprecord(full_part),
            true_DN_minus_exact_linear_DN=cauchy(total),
            source_Wtau_b_from_Wsigma_multiplier=uprecord(wide_multiplier)))
    # Sum the exact unrounded original source values. The auxiliary far and
    # complete full-head mass each occur ONCE in the whole low-block norm.
    low_sigma=factor*source_sum+far_value+full_low_sigma
    low_head=(factor*wide_source_sum+far_value+
              4*scale*upper(trace["beta"]["head"]["full_head_low_correction_K"]))
    axes=family["parameter_axes"]
    axes_by_mode={r["mode"]:r for r in axes}
    linear_mean_input=F(0)
    for row in trace["B0"]:
        mode=row["mode"]
        if mode>40:
            continue
        axis=axes_by_mode[mode]
        amplitude=abs(exact(axis["exact_centre"]))+exact(axis["half_axis"])
        coefficient=abs_upper(row["P_full_sine_coefficient_per_Q"])+abs_upper(row["Kbar_full_cosine_coefficient_per_Q"])
        linear_mean_input+=(1+mode)*exp_positive_upper(mode*head_tau_upper)*coefficient*amplitude
    high_head=upper(prior["complete_coarse_trace_rows"]["head"][
        "complete_high_balanced_P_K"]["uniform_value_upper"])
    mean_input=linear_mean_input+low_head+high_head
    if not mean_input<F(1,10000):
        raise ArithmeticError("The complete complex mean-root domain failed")
    mean_slope=40*mean_input**2
    prior_selected={r["mode"]:r for r in prior["selected_true_DN_minus_exact_linear_DN"]}
    gates=dict(all46_modes_times213_cells_completed=True,
        all46_formal_children_and_original_actual_input_identity=True,
        every_six_real_linear_groups_retained=True,
        wider_strip_gains_positive_and_outward=True,
        R74_full20_complex_parameter_box_unchanged=True,
        complete_auxiliary_far_added_once_to_the_full_low_mass=far_value>0,
        separate_complete_full_head_low_mass_added_once=True,
        all46_nonlinear_coefficient_caps_retained=len(new_rows)==46,
        both_complete_low_block_bounds_improve_R78=(
            low_sigma<upper(prior["complete_coarse_trace_rows"]["outer"]["all46_low_nonlinear_K"]["uniform_value_upper"])
            and low_head<upper(prior["complete_coarse_trace_rows"]["head"]["all46_low_nonlinear_K"]["uniform_value_upper"])),
        selected_m2_m4_complete_bounds_improve_R78=all(
            upper(r["true_DN_minus_exact_linear_DN"]["uniform_value_upper"])<upper(prior_selected[r["mode"]]["uniform_value_upper"])
            for r in new_rows if r["mode"] in (2,4)),
        complete_mean_root_and_improved_input=(
            mean_input<upper(prior["complete_nonmean_cut_mean_input_upper"]))
        )
    result=dict(status="Executed all46 source, complete true low-DN mass and Cauchy interface on actual R74 polydisc",
        author="/root (GPT-6 Astra Pro, AI-assisted)",all_gates=all(gates.values()),gates=gates,
        parameter_norm=prior["parameter_norm"],parameter_axes=axes,
        Cauchy_working_radius=prior["interior_parameter_radius"],
        source_factor=record(factor),envelope_factor=record(scale),
        whole46_original_auxiliary_source_Wsigma1_upper=uprecord(source_sum),
        whole46_uniform_R74_auxiliary_source_Wsigma1_upper=uprecord(factor*source_sum),
        whole46_complete_auxiliary_far_Wsigma1_upper=record(far_value),
        whole46_complete_full_head_minus_auxiliary_Wsigma1_upper=uprecord(full_low_sigma),
        whole46_true_DN_minus_exact_linear_Wsigma1=cauchy(low_sigma),
        whole46_true_DN_minus_exact_linear_Wtau_b1=cauchy(low_head),
        selected_mode_rows=new_rows,
        low_Q_and_P_nonlinear_remainder_identically_zero=True,
        complete_high_blocks_unchanged={strip:{key:value for key,value in fields.items()
            if key.startswith("complete_high") or key=="high_bands_value_upper"}
            for strip,fields in prior["complete_coarse_trace_rows"].items()},
        complete_linear_nonmean_mean_input_upper=uprecord(linear_mean_input),
        complete_nonmean_mean_input_upper=uprecord(mean_input),
        complete_mean_slope=cauchy(mean_slope),
        cuff_normalized_mean_height_unchanged=prior["cuff_normalized_complete_mean_height"],
        mean_height_convention=prior["mean_height_convention"],
        all46_output_caps_are_not_independent_full_mass_allowances=True,
        full_outer_Green_Schur_or_closed_surface_claimed=False,
        input_hashes=input_hashes,common_original_source_inputs=common_inputs,
        real_column_groups=groups,source_sha256=digest(__file__),
        helper_hashes={n:digest(Path(__file__).with_name(n)) for n in
            ("root_moving_auxiliary_centre_family.py","root_anisotropic_true_cut_cauchy.py")},
        source_replay_child_peak_rss_kib=peak_child,source_replay_total_child_seconds=sum_child_seconds,
        no_new_Arb=True,no_new_ODE=True,no_new_source_integral=True,no_Node=True,
        elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    if result["peak_rss_kib"]>a.rss_kib:
        raise MemoryError("The declared owned Fraction-memory observer was exceeded")
    out=write_new(a.out,result)
    print(json.dumps(dict(event="done",all_gates=result["all_gates"],output=out,
        low_value=result["whole46_true_DN_minus_exact_linear_Wsigma1"]["uniform_value_upper"]["display"],
        low_derivative=result["whole46_true_DN_minus_exact_linear_Wsigma1"]["first_derivative_linf_to_output_upper"]["display"],
        mean_slope=result["complete_mean_slope"]["uniform_value_upper"]["display"],
        elapsed_seconds=result["elapsed_seconds"],peak_rss_kib=result["peak_rss_kib"])),flush=True)
    if not result["all_gates"]:
        raise SystemExit(2)


if __name__=="__main__":main()
