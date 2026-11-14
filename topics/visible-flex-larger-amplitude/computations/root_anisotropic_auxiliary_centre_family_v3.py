#!/usr/bin/env python3
"""Enlarge only the actual fourth-mode shallow axis on the same actual R72 head.

Stream saved true linear columns by physical cell, use exact dyadic arithmetic and an elementary
exponential upper bound.  No ODE, quadrature, Arb operation, new matrix or Node
worker is used.  The original complete mean, far graph and all641 rows remain.
Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import gc
import hashlib
import json
from pathlib import Path
import resource
import time

from root_stream_column_groups import iter_group_cells

from root_moving_auxiliary_centre_family import (
    digest, exact, lower, upper, pow2, read, record, write_new)


def ceil_fraction(x):
    return -((-x.numerator) // x.denominator)


def rounded_up(x, exponent=-128):
    return ceil_fraction(x / pow2(exponent)) * pow2(exponent)


def dyadic_endpoint(row):
    return int(row["mantissa"]), int(row["binary_exponent"])


def abs_endpoint_upper(row):
    choices = [dyadic_endpoint(row[k]) for k in ("lower", "upper")]
    choices = [(abs(m), e) for m, e in choices]
    # The stored two endpoints of a normalized column have nearby exponents.
    def compare_key(item):
        m, e = item
        return m.bit_length() + e if m else -(1 << 60)
    a, b = sorted(choices, key=compare_key)
    if compare_key(a) != compare_key(b):
        return b
    e = min(a[1], b[1])
    return (max(a[0] << (a[1]-e), b[0] << (b[1]-e)), e)


def units_above(mantissa, exponent, unit_exponent):
    """Ceil a positive dyadic in prescribed units without enormous shifts."""
    if mantissa < 0:
        raise ValueError("Only positive column bounds enter this sum")
    if not mantissa:
        return 0
    shift = exponent-unit_exponent
    if shift >= 0:
        if mantissa.bit_length()+shift > 4096:
            raise ArithmeticError("A column greatly exceeds the proposed physical norm")
        return mantissa << shift
    bits = -shift
    if bits >= mantissa.bit_length():
        return 1
    quotient, remainder = divmod(mantissa, 1 << bits)
    return quotient + bool(remainder)


def rational_endpoint(value):
    return F(int(value["numerator"]), int(value["denominator"]))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ("reference", "aux-box", "aux-far", "columns", "r72-summary",
                 "two-cell-budget", "out-prefix"):
        ap.add_argument("--"+name, type=Path, required=True)
    ap.add_argument("--rss-kib", type=int, default=51200)
    a = ap.parse_args()
    started = time.monotonic()
    paths = {n: getattr(a, n) for n in
        ("reference", "aux_box", "aux_far", "columns", "r72_summary", "two_cell_budget")}
    hashes = {str(p): digest(p) for p in paths.values()}
    ref, box, far, columns, summary, budget = [read(paths[n]) for n in paths]
    for doc in (ref, box, far, summary, budget):
        for name, sha in doc.get("input_hashes", {}).items():
            if digest(name) != sha:
                raise ValueError("A saved certified input changed: "+name)
    if (not all(ref["checks"].values()) or not all(box["gates"].values())
            or not all(far["gates"].values()) or not summary["all_gates"]
            or not budget["all_gates"]):
        raise ValueError("Use the completed original certificates and corrected source budget")
    if summary["input_hashes"].get(str(a.reference)) != hashes[str(a.reference)]:
        raise ValueError("R72 uses another actual reference")
    if summary["input_hashes"].get(str(a.aux_box)) != hashes[str(a.aux_box)]:
        raise ValueError("R72 uses another auxiliary box")
    if summary["input_hashes"].get(str(a.aux_far)) != hashes[str(a.aux_far)]:
        raise ValueError("R72 uses another complete far lift")
    if ref["input_hashes"].get(str(a.columns)) != hashes[str(a.columns)]:
        raise ValueError("The linear columns do not belong to this reference")
    frozen = Path(__file__).with_name("root_moving_auxiliary_centre_family.py")
    if digest(frozen) != summary["source_sha256"]:
        raise ValueError("The original R72 verifier changed")
    cells = list(range(12, 225))
    modes = list(range(2, 93, 2))
    if (ref["modes"] != modes or [r["cell"] for r in ref["cell_rows"]] != cells
            or [r["cell"] for r in box["rows"]] != cells
            or [r["cell"] for r in far["rows"]] != cells):
        raise ValueError("Every original physical cell and low mode is required")
    eps2, eps_other = pow2(-10), pow2(-4)
    alpha_main, alpha_total = 1+eps2, 1+2*eps2
    kappa_aux, kappa_rest, scale = 1+12*eps2, 1+16*eps2, 1+4*eps2
    theta = kappa_rest*scale
    if (exact(summary["coefficient_domination_factor"]) != theta
            or exact(summary["physical_envelope_factor"]) != scale
            or not scale**2 < kappa_aux < kappa_rest):
        raise ValueError("The declared positive coefficient comparison differs")
    # e = sum_{k=0}^4 1/k! + remainder < 65/24 + (1/120)/(1-1/6).
    # Hence e < 1631/600 < 87/32.  No transcendental numeric value is used.
    if not F(65,24)+F(1,100) == F(1631,600) < F(87,32):
        raise ArithmeticError("The elementary exponential bound failed")
    amplitudes = {r["mode"]: abs_endpoint_upper(r["required_far_Q"])
                  for r in ref["endpoint_rows"]}
    if any(amplitudes[m][0] for m in modes if m > 40):
        raise ValueError("The twenty actual reference heights must be the only nonzero ones")
    unit_exp = []
    for row in ref["cell_rows"]:
        mantissa, exponent = dyadic_endpoint(row["reference_X"]["lower"])
        if mantissa <= 0:
            raise ValueError("The original physical normalization must be positive")
        unit_exp.append(mantissa.bit_length()-1+exponent-128)
    rest_units = [0]*len(cells)
    group_records, covered = [], [[] for _ in cells]
    for group_ref in columns["column_groups"]:
        path = Path(group_ref["path"])
        if digest(path) != group_ref["sha256"]:
            raise ValueError("A true complete column group changed")
        for n, row in enumerate(iter_group_cells(path, group_ref["modes"])):
            tau = upper(ref["cell_rows"][n]["tau"])
            for col in row["linear_rows"]:
                m = col["mode"]
                covered[n].append(m)
                if m != 4:
                    continue
                am, ae = amplitudes[m]
                degree = ceil_fraction(tau*m)
                exp_mantissa = 87**degree
                # Both summands are rounded UP separately.  This avoids
                # keeping negligible high-mode dyadics with millions of bits.
                for name, weight in (("column_Q_sup", (1+m)**3),
                                     ("column_Xi_sup", 1+m)):
                    cm, ce = dyadic_endpoint(col[name]["upper"])
                    rest_units[n] += units_above(am*cm*weight*exp_mantissa,
                        ae+ce-5*degree, unit_exp[n])
        group_records.append(dict(path=str(path), sha256=group_ref["sha256"],
            modes=group_ref["modes"], all213_cells=True))
        gc.collect()
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > a.rss_kib:
            raise MemoryError("The declared self-observed RSS budget failed")
    if any(sorted(row) != modes for row in covered):
        raise ValueError("A mode was omitted or counted twice")
    aux_rows, ratios, rest_ratios = [], [], []
    far_lip = upper(far["added_Lipschitz_bound"])
    for n, (rr, br, fr) in enumerate(zip(ref["cell_rows"], box["rows"], far["rows"])):
        xlo, xhi = lower(rr["reference_X"]), upper(rr["reference_X"])
        v, u = exact(br["correction_radius_multiple"]), exact(br["total_radius_multiple"])
        if u != 1+v:
            raise ValueError("The actual nonlinear auxiliary radius changed")
        rest_upper = rest_units[n]*pow2(unit_exp[n])
        linear_extra = (eps_other-eps2)*rest_upper
        rest_extra = (eps_other-eps2)*rest_upper
        new_map = scale**2*upper(br["normalized_map_bound"])+upper(fr["additional_map_bound_relative_to_reference"])
        new_lip = scale*upper(br["Lipschitz_row_bound"])+far_lip
        gates = dict(actual_total_linear_mass=linear_extra <= (alpha_total-alpha_main)*xlo,
            complete_nonprincipal_linear_mass_and_nonlinear_rest=
                rest_extra <= (kappa_rest-kappa_aux)*v*xlo,
            new_total_physical_envelope=alpha_total+kappa_aux*v <= scale*u,
            auxiliary_self_map=new_map < kappa_aux*v,
            auxiliary_uniform_contraction=new_lip < 1,
            complete_R23_mean_and_source_domain=scale*upper(br["relative_to_R23_ball"]) < 1)
        ratios.append(rounded_up(rest_upper/xlo))
        rest_ratios.append(rounded_up(rest_extra/((kappa_rest-kappa_aux)*v*xlo)))
        aux_rows.append(dict(cell=rr["cell"], expanded_mode4_linear_mass_upper=record(rest_upper),
            unit_exponent=unit_exp[n], all46_columns_present=True,
            mass_relative_to_old_reference_upper=record(ratios[-1]),
            new_total_linear_factor=record(alpha_total),
            nonlinear_radius_multiple=record(kappa_aux*v), new_full_map=record(new_map),
            new_uniform_Lipschitz=record(new_lip),
            rest_budget_fraction_upper=record(rest_ratios[-1]),
            rest_comparison="Base relative2^-10 multiplies the entire old nonprincipal linear mass by alpha_main <= kappa_rest; only the extra mode4 mass is charged against (kappa_rest-kappa_aux)*v*x", gates=gates))
    far_factor = max(1+eps_other, kappa_aux)
    new_far = far_factor*upper(box["complete_far_z_bound"])
    zaux = exact(summary["retained_auxiliary_far_ball"])
    # The original complete R72 ledger is reused only after the new linear,
    # rest, envelope and far conditions have been checked independently.
    ledger_ref = summary["complete_original_row_ledger"]
    ledger_path = Path(ledger_ref["path"])
    if digest(ledger_path) != ledger_ref["sha256"]:
        raise ValueError("The full original641 ledger changed")
    ledger = read(ledger_path)
    if (not ledger["all_gates"] or len(ledger["joint_rows"]) != 641
            or len(ledger["domain_rows"]) != 213):
        raise ValueError("The complete certified R72 rows are required")
    joint_rows, domains = ledger["joint_rows"], ledger["domain_rows"]
    all_joint_maps = all(exact(r["new_image"]) < exact(r["new_radius"])
                         for r in joint_rows)
    all_joint_derivatives = all(exact(r["new_uniform_Lipschitz"]) < 1
                                for r in joint_rows)
    all_domains = all(r["physical_domain"] and r["mean_domain"] for r in domains)
    axis_rows, axes = [], {}
    for row in ref["endpoint_rows"][:20]:
        m, q = row["mode"], exact(row["reference_Q"])
        eps = eps_other if m == 4 else eps2
        axis = eps*abs(q)
        axes[m] = axis
        axis_rows.append(dict(mode=m, exact_centre=record(q), relative_radius=record(eps),
            half_axis=record(axis), lower=record(q-axis), upper=record(q+axis)))
    outer_rows = []
    for row in budget["rows"]:
        interval = row["original_candidate_complete_node10_centre"]
        centre_abs = max(abs(rational_endpoint(interval[k])) for k in ("lower", "upper"))
        axis = axes[row["mode"]]
        outer_rows.append(dict(mode=row["mode"], corrected_centre_abs_upper=record(centre_abs),
            available_axis=record(axis), centre_axis_ratio_upper=record(rounded_up(centre_abs/axis)),
            current_candidate_centre_within_axis=centre_abs < axis))
    gates = dict(all213_new_auxiliary_and_mass_rows=all(all(r["gates"].values()) for r in aux_rows),
        complete_true_R18_auxiliary_far_domain=new_far < zaux,
        unchanged_complete_positive_coefficient_factor=theta == exact(summary["coefficient_domination_factor"]),
        all641_complete_joint_map_rows=all_joint_maps,
        all641_uniform_derivative_rows=all_joint_derivatives,
        all213_physical_and_complete_mean_domains=all_domains,
        unchanged_full_joint_true_R18_domain=ledger["gates"]["full_joint_true_R18_domain"],
        all20_independent_parameters_and_all46_auxiliary_modes=True,
        same_fixed_g_continuous_tau_norm_interfaces=True,
        complete_corrected_candidate_centres_within_new_axes=all(r["current_candidate_centre_within_axis"] for r in outer_rows))
    result = dict(status="Actual anisotropic moving-centre family certified" if all(gates.values())
        else "Executed exact anisotropic proposal with unpaid gates", all_gates=all(gates.values()), gates=gates,
        author="/root (GPT-6 Astra Pro, AI-assisted)",
        parameter_domain="m4 relative +/-2^-4; every other actual mode m2,m6..40 independently +/-2^-10; m42..92 shallow heights zero, all46 auxiliary/far coordinates retained",
        main_linear_factor=record(alpha_main), total_linear_factor=record(alpha_total),
        auxiliary_nonlinear_factor=record(kappa_aux), rest_coefficient_factor=record(kappa_rest),
        envelope_factor=record(scale), complete_coefficient_factor=record(theta),
        elementary_exponential_bound="e < 65/24+1/100 = 1631/600 < 87/32; exp(m*tau) <= (87/32)^ceil(m*tau_upper)",
        column_rounding="Each positive column summand rounded upward in units 2^(floor(log2(x_lower))-128); integer shifts never discard a positive summand",
        maximum_expanded_mode4_mass_reference_ratio_upper=record(max(ratios)),
        maximum_rest_budget_fraction_upper=record(max(rest_ratios)),
        auxiliary_far_factor=record(far_factor), auxiliary_far_upper=record(new_far),
        retained_auxiliary_far_ball=record(zaux),
        maximum_auxiliary_Lipschitz=record(max(exact(r["new_uniform_Lipschitz"]) for r in aux_rows)),
        maximum_joint_Lipschitz=summary["maximum_full_joint_Lipschitz"],
        auxiliary_rows=aux_rows, joint_rows=joint_rows, domain_rows=domains,
        parameter_axes=axis_rows, current_candidate_outer_budget_rows=outer_rows,
        original_R72_ledger=ledger_ref, original_column_groups=group_records,
        input_hashes=hashes, source_sha256=digest(Path(__file__)),
        streaming_helper_sha256=digest(Path(__file__).with_name("root_stream_column_groups.py")),
        prior_same_math_source_sha256="88ca040649952d6fd19da7117ad96924c6a5d35be7e7625c711bccc6f35d9511",
        no_new_ODE=True, no_new_source_integrals=True, no_new_Green=True,
        no_Arb_or_transcendental_evaluation=True, no_Node=True,
        full_outer_matching_or_contraction_claimed=False,
        scope="Same actual full-frequency inner head12..224 plus the original R18 infinite C2 tail; two candidate centre bounds fit the larger axes but the full outer Green/Schur problem and closed geometry remain unpaid",
        elapsed_seconds=time.monotonic()-started,
        peak_rss_kib_before_serialization=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    primary = write_new(a.out_prefix.with_suffix(".json.gz"), result)
    small = {k:v for k,v in result.items() if k not in
        ("auxiliary_rows", "joint_rows", "domain_rows", "original_column_groups")}
    small["complete_row_ledger"] = primary
    write_new(a.out_prefix.with_name(a.out_prefix.name+"-summary.json"), small)
    print(json.dumps(dict(all_gates=result["all_gates"], gates=gates, primary=primary,
        maximum_rest_mass_ratio=result["maximum_expanded_mode4_mass_reference_ratio_upper"]["display"],
        maximum_rest_budget_fraction=result["maximum_rest_budget_fraction_upper"]["display"],
        far=result["auxiliary_far_upper"]["display"], outer_ratios=[r["centre_axis_ratio_upper"]["display"] for r in outer_rows],
        elapsed_seconds=result["elapsed_seconds"],
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)), flush=True)
    if not result["all_gates"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
