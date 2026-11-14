#!/usr/bin/env python3
"""Pay a moving actual auxiliary-centre family using all original 213/641 rows.

The source, real linear columns, continuous strip and infinite R18 graph stay
fixed. Every nonzero saved M20 shallow height may vary in its stated relative
interval. Its linear lift belongs to the new auxiliary centre, not to the tiny
full-frequency correction box. All arithmetic below is exact Fraction.

No source quadrature, ODE, new kernel, floating inverse or Node worker is used.
Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
from __future__ import annotations

import argparse
from decimal import Decimal, localcontext
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time


def pow2(n):
    return F(1 << n) if n >= 0 else F(1, 1 << -n)


def endpoint(value):
    return int(value["mantissa"]) * pow2(int(value["binary_exponent"]))


def lower(value):
    return endpoint(value["lower"])


def upper(value):
    return endpoint(value["upper"])


def exact(value):
    lo, hi = lower(value), upper(value)
    if lo != hi:
        raise ValueError("A defined exact dyadic was expected")
    return lo


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 18), b""):
            h.update(chunk)
    return h.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open(path, "rt") if path.suffix == ".gz" else path.open()) as f:
        return json.load(f)


def record(value):
    value = F(value)
    denominator = value.denominator
    if denominator & (denominator - 1):
        raise ArithmeticError("A serialized bound was not an exact dyadic")
    mantissa = value.numerator
    exponent = 1 - denominator.bit_length()
    if mantissa:
        while mantissa % 2 == 0:
            mantissa //= 2
            exponent += 1
    else:
        exponent = 0
    e = dict(mantissa=str(mantissa), binary_exponent=exponent)
    with localcontext() as ctx:
        ctx.prec = 22
        display = str(Decimal(value.numerator) / Decimal(value.denominator))
    return dict(lower=e, upper=dict(e), display=display)


def write_new(path, value):
    path = Path(path)
    if path.exists():
        raise FileExistsError("Use a fresh immutable output: " + str(path))
    raw = (json.dumps(value, separators=(",", ":"), ensure_ascii=False) + "\n").encode()
    data = gzip.compress(raw, mtime=0) if path.suffix == ".gz" else raw
    if len(data) >= 5_000_000 or (len(data) > 1_000_000 and path.suffix != ".gz"):
        raise ValueError("The repository size/compression rule failed")
    path.write_bytes(data)
    return dict(path=str(path), bytes=len(data), sha256=hashlib.sha256(data).hexdigest())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("reference", "aux-box", "aux-far", "density", "joint", "out-prefix"):
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--epsilon-log2", type=int, default=-10)
    parser.add_argument("--correction-radius-multiple", type=int, default=4)
    parser.add_argument("--rss-kib", type=int, default=40960)
    args = parser.parse_args()
    started = time.monotonic()
    output = args.out_prefix.with_name(args.out_prefix.name + ".json.gz")
    summary_path = args.out_prefix.with_name(args.out_prefix.name + "-summary.json")
    if output.exists() or summary_path.exists():
        raise FileExistsError("Use fresh execution outputs")
    docs, hashes = {}, {}
    for name in ("reference", "aux_box", "aux_far", "density", "joint"):
        path = getattr(args, name)
        hashes[str(path)] = digest(path)
        docs[name] = read(path)
    ref, box, far, density, joint = [docs[n] for n in
        ("reference", "aux_box", "aux_far", "density", "joint")]
    verified = {}
    for name, doc in docs.items():
        for filename, sha in doc.get("input_hashes", {}).items():
            if filename not in verified:
                if digest(filename) != sha:
                    raise ValueError("A paid direct input changed: " + filename)
                verified[filename] = sha
    frozen_verifier = Path(__file__).with_name("closure_two_material_joint_verify.py")
    if digest(frozen_verifier) != joint["source_sha256"]:
        raise ValueError("The complete original-row verifier source changed")
    for filename, sha in joint["helper_hashes"].items():
        if digest(Path(__file__).with_name(filename)) != sha:
            raise ValueError("A frozen original-row helper changed")
    if not all(ref["checks"].values()) or any(not all(d["gates"].values())
            for d in (box, far, density, joint)):
        raise ValueError("Every original input must have paid its own complete gates")
    if (not joint["whole_head_closed"] or joint["dimension"] != 641
            or len(joint["rows"]) != 641
            or joint["input_hashes"].get(str(args.density)) != hashes[str(args.density)]):
        raise ValueError("The original complete actual strong641 certificate is required")
    for doc in (box, far):
        if doc["input_hashes"].get(str(args.reference)) != hashes[str(args.reference)]:
            raise ValueError("The auxiliary centre uses another actual reference")
    if far["input_hashes"].get(str(args.aux_box)) != hashes[str(args.aux_box)]:
        raise ValueError("The true far graph is attached to another auxiliary box")
    cells = list(range(12, 225))
    for doc, key in ((ref, "cell_rows"), (box, "rows"), (far, "rows"), (density, "rows")):
        if [row["cell"] for row in doc[key]] != cells:
            raise ValueError("Every real physical cell must remain present and ordered")
    if ref["modes"] != list(range(2, 93, 2)) or box["modes"] != ref["modes"]:
        raise ValueError("All 46 auxiliary modes are required")
    eps = pow2(args.epsilon_log2)
    alpha, kappa, scale = 1 + eps, 1 + 16 * eps, 1 + 4 * eps
    theta = kappa * scale
    enlargement = F(args.correction_radius_multiple)
    if not (0 < eps < 1 and 1 < alpha <= kappa and scale**2 < kappa and enlargement > 1):
        raise ValueError("The chosen exact scaling inequalities are invalid")
    zaux = exact(joint["auxiliary_far_z"])
    if far["far_z_dyadic_bound"] != "2^-2224" or zaux != pow2(-2224):
        raise ValueError("Retain the original actual auxiliary R18 ball")
    far_lip = upper(far["added_Lipschitz_bound"])
    aux_rows = []
    for rr, br, fr, dr in zip(ref["cell_rows"], box["rows"], far["rows"], density["rows"]):
        u = exact(br["total_radius_multiple"])
        v = exact(br["correction_radius_multiple"])
        if u != 1 + v or v <= 0:
            raise ValueError("The original nonlinear radius must be U-1 > 0")
        total = alpha + kappa * v
        old_map = upper(br["normalized_map_bound"])
        old_far_map = upper(fr["additional_map_bound_relative_to_reference"])
        new_map = scale**2 * old_map + old_far_map
        new_radius = kappa * v
        new_lip = scale * upper(br["Lipschitz_row_bound"]) + far_lip
        new_domain = scale * upper(br["relative_to_R23_ball"])
        old_x = upper(rr["reference_X"])
        old_envelope = exact(dr["canonical_total_envelope"])
        gates = dict(old_complete_auxiliary_map=old_map + old_far_map < v,
            enlarged_linear_and_nonlinear_centre=total <= scale * u,
            old_wide_envelope_covers_old_auxiliary=u * old_x <= old_envelope,
            enlarged_auxiliary_map=new_map < new_radius,
            enlarged_auxiliary_contraction=new_lip < 1,
            complete_R23_mean_and_source_domain=new_domain < 1)
        aux_rows.append(dict(cell=br["cell"], original_total=record(u),
            original_nonlinear_radius=record(v), new_total=record(total),
            new_nonlinear_radius=record(new_radius), new_full_map=record(new_map),
            new_map_slack=record(new_radius - new_map), new_Lipschitz=record(new_lip),
            new_R23_ratio=record(new_domain), new_canonical_envelope=record(scale * old_envelope),
            gates=gates))
    new_aux_far = kappa * upper(box["complete_far_z_bound"])
    factors = dict(low_main=alpha, low_corr=kappa, low_base=scale,
        low_remainder=scale**2, far_main=alpha*scale, far_corr=kappa*scale,
        far_base=scale**2, far_remainder=scale**3,
        source12_refined_corr=kappa, near_refined_mixed=scale,
        near_rest_infinite_gamma=scale, pure_near=scale,
        pure_rest_and_infinite=scale**2, low_high_boundary=1/scale,
        independent_far_boundary=F(1))
    if not all(value <= theta for value in factors.values()):
        raise ArithmeticError("The stated common factor does not cover every source/boundary family")
    # Low/high boundary factors may be left at 1 rather than serializing 1/S.
    # This makes every displayed sufficient coefficient an exact dyadic.
    factors["low_high_boundary"] = F(1)
    r, weights, images, lips = [], [], [], []
    for i, row in enumerate(joint["rows"]):
        expected = (("low", cells[i]) if i < 213 else ("near", cells[i-213])
            if i < 426 else ("rest", cells[i-426]) if i < 639 else
            ("infinite", None) if i == 639 else ("far_z", None))
        if row["index"] != i or (row["block"], row["cell"]) != expected:
            raise ValueError("An original full641 coordinate was omitted or reordered")
        r.append(exact(row["radius"])); weights.append(exact(row["metric_weight"]))
        images.append(upper(row["image"])); lips.append(upper(row["weighted_derivative_row"]))
    if not all(r[i] > images[i] >= 0 and weights[i] > 0 for i in range(641)):
        raise ValueError("The original strict positive box was not paid")
    common_radius = r[0] / weights[0]
    if not all(r[i] == common_radius * weights[i] for i in range(641)):
        raise ValueError("The original radii are not one exact multiple of the distance weights")
    rho, zstar = exact(joint["physical_domain"]), exact(joint["independent_far_z"])
    if rho != pow2(-30) or zstar != pow2(-2200):
        raise ValueError("Keep the original physical working domain and independent far ball")
    joint_rows = []
    for i in range(641):
        new_radius = enlargement * r[i]
        # The original J is an upper on the entire rho domain, not only at r.
        new_image = theta * (images[i] + (enlargement-1) * lips[i] * r[i])
        new_lip = theta * lips[i]
        joint_rows.append(dict(index=i, block=joint["rows"][i]["block"], cell=joint["rows"][i]["cell"],
            old_radius=record(r[i]), old_image=record(images[i]), old_Lipschitz=record(lips[i]),
            metric_weight=record(weights[i]), new_radius=record(new_radius),
            new_image=record(new_image), new_map_slack=record(new_radius-new_image),
            new_uniform_Lipschitz=record(new_lip),
            map_inclusion=new_image < new_radius, contraction=new_lip < 1))
    domains = []
    for n, dr in enumerate(density["rows"]):
        total = enlargement * (r[n] + r[213+n] + r[426+n] + r[639])
        mean = scale * upper(dr["V_over_w_upper"]) * (1 + total)
        domains.append(dict(cell=cells[n], total_correction=record(total),
            complete_mean_ratio=record(mean), physical_domain=total < rho,
            mean_domain=mean < F(1,64)))
    axis_rows = []
    for row in ref["endpoint_rows"]:
        q = exact(row["reference_Q"])
        if row["mode"] <= 40:
            axis_rows.append(dict(mode=row["mode"], exact_centre=record(q),
                relative_parameter_axis=record(eps * abs(q)),
                lower_shallow_Q=record(q-eps*abs(q)), upper_shallow_Q=record(q+eps*abs(q))))
    gates = dict(all213_original_auxiliary_rows=all(all(row["gates"].values()) for row in aux_rows),
        true_R18_auxiliary_parameter_domain=new_aux_far < zaux,
        all_declared_positive_coefficient_factors_dominated=all(v <= theta for v in factors.values()),
        old_complete_positive_rows_and_metric_retained=True,
        all641_enlarged_map_rows=all(row["map_inclusion"] for row in joint_rows),
        all641_uniform_derivative_rows=all(row["contraction"] for row in joint_rows),
        all213_physical_domains=all(row["physical_domain"] for row in domains),
        all213_complete_mean_domains=all(row["mean_domain"] for row in domains),
        full_joint_true_R18_domain=zaux + zstar * enlargement * r[640] < zstar,
        same_continuous_strip_and_norm_jumps=True,
        all46_auxiliary_directions_and_full_infinite_joint_space_retained=True)
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss > args.rss_kib:
        raise MemoryError("The declared self-observed RSS guard failed")
    result = dict(status=("Complete moving auxiliary-centre and full-frequency family certified"
        if all(gates.values()) else "Completed exact row checks; explicit gates failed"),
        author="/root (GPT-6 Astra Pro, AI-assisted)", all_gates=all(gates.values()), gates=gates,
        parameter_domain="For each saved actual M20 mode 2..40, |delta Q_m| <= epsilon*|q_m^*| independently; all 26 remaining shallow low heights stay zero. All46 correction/far coordinates remain present.",
        reference_identity="R39 actual q085 M20 node12 heights on the fixed R26 true rational metric; the saved full20 values, not a rounded display.",
        scope="Uniform complete-frequency real inner head12..224 and R18 infinite C2 tail. Outer0..11 Schur matching, full closed geometry and larger-amplitude completion remain separate.",
        epsilon=record(eps), linear_factor=record(alpha), auxiliary_nonlinear_radius_factor=record(kappa),
        physical_envelope_factor=record(scale), coefficient_domination_factor=record(theta),
        full_joint_radius_factor=record(enlargement), uniform_k_rescaling=record(scale),
        continuous_tau_unchanged=True, exact_chi_unchanged=True,
        auxiliary_far_upper=record(new_aux_far), retained_auxiliary_far_ball=record(zaux),
        original_physical_domain=record(rho), independent_far_ball=record(zstar),
        original_radius_multiple_of_metric_weight=record(common_radius),
        maximum_auxiliary_Lipschitz=record(max(upper(row["new_Lipschitz"]) for row in aux_rows)),
        maximum_full_joint_Lipschitz=record(max(upper(row["new_uniform_Lipschitz"]) for row in joint_rows)),
        maximum_total_correction=record(max(upper(row["total_correction"]) for row in domains)),
        far_normalized_correction=record(enlargement*r[640]),
        factor_table={k:record(v) for k,v in factors.items()},
        displayed_endpoint_axes=axis_rows, auxiliary_rows=aux_rows, joint_rows=joint_rows, domain_rows=domains,
        comparison_proof="R72: moving low auxiliary centre with kappa>S^2; every new complete positive coefficient <=Theta times its original R58 coefficient. Phi_new(c r)<=Theta[Phi_old(r)+(c-1)J_old r], and original r is an exact multiple of W. Every recorded 213/641 row is checked exactly.",
        input_hashes=hashes, verified_original_direct_inputs=verified,
        original_verifier_source_sha256=digest(frozen_verifier), source_sha256=digest(Path(__file__)),
        new_ODE_integrations=0, new_source_integrations=0, new_Green_integrations=0,
        new_floating_matrix_solves=0, new_Node_workers=0,
        exact_arithmetic="fractions.Fraction for every bound and gate; only display strings use Decimal",
        elapsed_seconds=time.monotonic()-started, peak_rss_kib=rss)
    primary = write_new(output,result)
    summary = {k:v for k,v in result.items() if k not in
        ("auxiliary_rows", "joint_rows", "domain_rows", "verified_original_direct_inputs")}
    summary["complete_original_row_ledger"] = primary
    write_new(summary_path,summary)
    print(json.dumps(dict(all_gates=result["all_gates"], gates=gates, output=primary,
        maximum_joint_Lipschitz=result["maximum_full_joint_Lipschitz"]["display"],
        maximum_auxiliary_Lipschitz=result["maximum_auxiliary_Lipschitz"]["display"],
        elapsed_seconds=result["elapsed_seconds"], peak_rss_kib=rss)),flush=True)
    if not result["all_gates"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
