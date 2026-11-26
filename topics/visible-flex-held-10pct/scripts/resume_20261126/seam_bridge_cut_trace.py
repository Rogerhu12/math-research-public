#!/usr/bin/env python3
"""Enclose a new accepted prefix's true common-R cut trace on its own runner.

Reads the saved quintic only; no core or BVP evaluation. Large coefficient
arrays stay in the output NPZ. Height position is relative to the same exact
Z_cut symbol, never a chosen numerical value. Optional accepted tail input
gives actual height-jet differences, without making a full-H assertion.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parent
MEAN_SHA = "ab08dc1dc7f24f6e92e3d64fcc530767cb66f5ae5a2940f953460a3274b6a1a5"
INTERVAL_SHA = "6234c458d303dfd2e47dcf1e1a6ee54a3d466118a8aea4d76f66013154c034e7"
PSI_SHA = "f4834f978de38046e374b020d2a928d293fc405f794159e40e2271f4ee9bd9cf"
SHORT_SHA = "7e00a3336a302ba94c751c09e6f75749d6973c86605269538c8f0b44c60779b4"
WARM = "warm-supported-material-phase-fixed-metric"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


def fq(value):
    value = float(value)
    if not np.isfinite(value):
        raise ValueError("Nonfinite literal input")
    return F.from_float(value)


def interval_array(b, values):
    rows = [b.I.rational(v) for v in values]
    return b.I(np.asarray([v.x[0] for v in rows]), np.asarray([v.x[1] for v in rows]))


def scalar(value):
    lo, hi = map(float, value.x)
    return {"lower": lo, "upper": hi,
            "lower_exact": str(fq(lo)), "upper_exact": str(fq(hi))}


def tensor(rows):
    return np.stack([np.stack(row.x, axis=0) for row in rows], axis=0)


def l1_upper(b, value):
    return float(b.I(np.maximum(abs(value.x[0]), abs(value.x[1]))).sum().x[1])


def endpoint_jets(primitive, physical, gauge, count):
    with np.load(physical) as z:
        x, c = z["x"], z["c"]
        if x.dtype != np.float64 or c.dtype != np.float64:
            raise ValueError("Require original binary64 physical coefficients")
        if c.shape != (6, len(x) - 1, 3 * count + 1):
            raise ValueError("Require the original physical common-C2 quintic")
        if not np.all(np.isfinite(c)) or not np.all(np.diff(x) > 0):
            raise ValueError("Invalid physical quintic")
        h = fq(x[-1]) - fq(x[-2])
        rows = [[], [], []]
        for j in range(c.shape[2]):
            poly = [fq(c[5 - k, -1, j]) for k in range(6)]
            for order in range(3):
                rows[order].append(gauge * primitive.value(poly, h))
                poly = primitive.derivative(poly)
        return fq(x[-1]), rows


def true_radius(primitive, bridge, span):
    p, eps, L1, L2, L3 = map(
        fq, (bridge.peak, bridge.eps, bridge.L1, bridge.L2, bridge.L3)
    )
    u = (span - L1 - L2) / L3
    phi = p - eps * u * u
    if not (0 < eps < p and 0 < phi < p and F(999, 1000) < u < F(1001, 1000)):
        raise ValueError("Cut is outside the declared terminal analytic phase")
    first = primitive.sin_polynomial([F(0), F(0), 3 * p, -2 * p], 40)
    terminal = primitive.sin_polynomial([p, F(0), -eps], 40)
    plateau = primitive.sin_polynomial([p], 40)[0]
    center = (fq(bridge.astart) - L1 * primitive.integral(first, F(1))
              - L2 * plateau - L3 * primitive.integral(terminal, u))
    error = span * p ** 41 / primitive.factorial(41)
    sl, sh = primitive.trig_scalar(phi, 40, True)
    cl, ch = primitive.trig_scalar(phi, 40, False)
    fac = 2 * eps * u / L3
    return [(center - error, center + error), (-sh, -sl), (fac * cl, fac * ch)], {
        "peak": str(p), "eps": str(eps), "L1": str(L1), "L2": str(L2), "L3": str(L3),
        "terminal_u_exact": str(u), "terminal_phase_exact": str(phi),
        "a_start_exact": str(fq(bridge.astart)),
    }


def original_mean_at_cut(b, Y, a, ap, app, psi, count):
    """Same finite literal mean and s derivative; warp/lift cut jets vanish."""
    frequencies = np.arange(1, count + 1) * 3
    mp.iv.dps = 80
    coslo = np.empty((count, len(psi)))
    coshi, sinlo, sinhi = (np.empty_like(coslo) for _ in range(3))
    for j, m in enumerate(frequencies):
        for k, p in enumerate(psi):
            x = mp.iv.mpf(float(p)) * int(m)
            co, sn = mp.iv.cos(x), mp.iv.sin(x)
            coslo[j, k], coshi[j, k] = b.K.dn(float(co.a)), b.K.up(float(co.b))
            sinlo[j, k], sinhi[j, k] = b.K.dn(float(sn.a)), b.K.up(float(sn.b))
    co, sn = b.I(coslo, coshi), b.I(sinlo, sinhi)
    y = b.D(interval_array(b, Y[0]), interval_array(b, Y[1]))
    aa, aa_s = b.D(a, ap), b.D(ap, app)
    fr = b.I(frequencies[:, None])
    radial = y.item(slice(1, count + 1)).expand()
    tangent = y.item(slice(count + 1, 2 * count + 1)).expand()
    height = y.item(slice(2 * count + 1, None)).expand()
    R = y.item(0) + (radial * co).sum()
    Rp, Rpp = -(radial * (fr * sn)).sum(), -(radial * (fr.sq() * co)).sum()
    T, Tp = (tangent * sn).sum(), (tangent * (fr * co)).sum()
    Tpp = -(tangent * (fr.sq() * sn)).sum()
    Zp, Zpp = -(height * (fr * sn)).sum(), -(height * (fr.sq() * co)).sum()
    U = [(Rp - T) / aa, 1 + (Tp + R) / aa, Zp / aa]
    V = [-1 + (Rpp - 2 * Tp - R) / aa, (Tpp + 2 * Rp - T) / aa, Zpp / aa]
    un = b.norm(U)
    kap_a = b.norm(b.cross(U, V)) / (un * un * un)
    unit_tangent = [x / un for x in U]
    projection = b.dot(unit_tangent, V)
    normal_unscaled = [x - projection * t for x, t in zip(V, unit_tangent)]
    normal_norm = b.norm(normal_unscaled)
    normal = [x / normal_norm for x in normal_unscaled]
    binormal = b.cross(unit_tangent, normal)
    alpha = -aa_s / kap_a
    root = 1 - alpha.sq()
    if np.any(root.v.x[0] <= 0):
        raise ArithmeticError("Original literal-node Frenet mean root not enclosed positive")
    mean = (alpha * normal[2] + root.sqrt() * binormal[2]).sum() / len(psi)
    return mean, float(np.min(root.v.x[0]))


def finite_gate(run, actual=False):
    """The original finite thresholds, under the declared boundary problem."""
    gates = run["gates"]
    bc_names = (("actual_scaled_bc_max", "actual_physical_bc_max") if actual else
                ("original_scaled_bc_max", "linear_dn_physical_bc_max"))
    if not (0 < fq(gates["tol"]) <= fq(1e-6) and
            0 < fq(gates["bc_tol"]) <= fq(1e-7) and
            0 < fq(gates["physical_bc_tol"]) <= fq(2e-9) and
            0 <= fq(run["raw_return"]["rms"]) <= fq(gates["tol"]) and
            0 <= fq(run[bc_names[0]]) <= fq(gates["bc_tol"]) and
            0 <= fq(run[bc_names[1]]) <= fq(gates["physical_bc_tol"])):
        raise ValueError("Warm source changed or failed the original finite gates")
    rows = run.get("metric_diagnostics")
    if not rows or not all(
            row["angular"] >= 16 * (3 * int(run["modes"]) + 1) and
            0 <= fq(row["legacy_max_component_fft_l1"]) <= fq(1e-6) and
            0 <= fq(row["sample_operator_max"]) <= fq(1e-6) for row in rows):
        raise ValueError("Warm source did not pass its actual full metric diagnostics")


def accepted_source_record(source_run, physical):
    """Validate actual provenance without constructing a core or invoking a solver."""
    source_run, physical = Path(source_run).resolve(), Path(physical).resolve()
    run = json.loads(source_run.read_text())
    kind = run.get("model_kind")
    if isinstance(kind, str) and kind.startswith(WARM) and kind not in (
            WARM, WARM + "-v2", WARM + "-actual-dn"):
        raise ValueError("Unknown warm model version requires its own explicit accepted-input adapter")
    actual = kind == WARM + "-actual-dn"
    gate = dict(model_kind=kind or "original-design-prefix",
                original_boundary_problem=run.get("terminal_kind", "original_linear_dn"),
                actual_DN_checked=False, versioned_reexpression_checked=False)
    if kind == WARM + "-v2":
        loader_path = HERE / "warm_fixed_m3_model_v2.py"
        loader = module("_seam_cut_v2_source_gate", loader_path)
        run = loader.accepted_input(source_run, require_lambda_one=False)
        gate.update(validator="warm_fixed_m3_model_v2.accepted_input",
            validator_sha256=sha(loader_path), acceptance_kind=run["acceptance_kind"],
            solver_invoked=run["solver_invoked"], solver_success=run["solver_success"],
            raw_success=run["raw_return"]["success"],
            versioned_reexpression_checked=(run["acceptance_kind"] ==
                                             "same_cartesian_map_verified_reexpression"))
        if gate["versioned_reexpression_checked"]:
            gate["source_solver_provenance"] = run["source_solver_provenance"]
    elif actual:
        loader_path = HERE / "warm_true_dn_solve.py"
        loader = module("_seam_cut_actual_source_gate", loader_path)
        if (run.get("error") or run.get("status") != "audited_finite_actual_dn_candidate"
                or run.get("fixed_metric") is not True
                or run.get("finite_actual_dn_candidate_pass") is not True
                or run.get("solver_success") is not True
                or run.get("raw_return", {}).get("success") is not True
                or run.get("raw_return", {}).get("status") != 0
                or run.get("terminal_kind") != "original_actual_nonlinear_dn"
                or run.get("actual_tail_requested") is not True
                or run.get("original_actual_nonlinear_tail") is not True
                or run.get("parameter_zero_meaning") != "log(q_aux/gauge_q)"
                or run.get("mean_nodes") != 1168 or run.get("bc_normalization") != .02):
            raise ValueError("The actual-DN source lacks its real complete successful return")
        finite_gate(run, actual=True)
        original_path = Path(run["linear_source_run"])
        if sha(original_path) != run["linear_source_run_sha256"]:
            raise ValueError("The accepted lambda-one linear source changed")
        original = loader.validate_warm_source(HERE.parents[3], original_path)
        for key in ("frozen_profile", "warm_definition", "angular_chart", "gauge_q",
                    "warp_reference", "mean_nodes", "bc_normalization", "modes", "angular",
                    "physical_tail_parameters", "physical_tail_cut", "linear_port_path",
                    "linear_port_sha256", "origin_design_run", "origin_design_sha256",
                    "frozen_source_signature", "warm_provider_sha256"):
            if run[key] != original[key]:
                raise ValueError("Frozen actual-DN geometry differs: " + key)
        for key in ("frozen_radial_chart", "warm_geometry_base_sha256"):
            if run.get(key) != original.get(key):
                raise ValueError("Versioned actual-DN geometry differs: " + key)
        if (run["linear_source_model_kind"] != original["model_kind"]
                or run["linear_source_acceptance_kind"] != original.get(
                    "acceptance_kind", "actual_warm_bvp_return")
                or run["linear_source_solver_invoked"] != original.get("solver_invoked", True)):
            raise ValueError("The original warm representation provenance changed")
        for path, digest in run["source_hashes"].items():
            if sha(path) != digest:
                raise ValueError("An actual-DN bound source changed: " + path)
        if sha(loader_path) not in run["source_hashes"].values():
            raise ValueError("The actual-DN gate source is not bound to this return")
        raw_path = source_run.parent / run["raw_return"]["file"]
        if sha(raw_path) != run["raw_return"]["sha256"]:
            raise ValueError("The actual-DN raw field changed")
        with np.load(raw_path, allow_pickle=False) as raw, np.load(physical, allow_pickle=False) as field:
            if (not np.array_equal(raw["p"], field["p"])
                    or not np.all(np.isfinite(raw["rms"])) or np.any(raw["rms"] < 0)
                    or float(np.max(raw["rms"])) != run["raw_return"]["rms"]):
                raise ValueError("The final physical field or original actual RMS identity changed")
        metric_path = source_run.parent / "relative-metric.json"
        if sha(metric_path) != run["relative_metric_sha256"]:
            raise ValueError("The actual complete finite metric artifact changed")
        final = run["result"]
        seam = run["tail_seam"]
        if (final["original_nonlinear_DN_accepted"] is not True
                or final["raw_sha256"] != run["raw_return"]["sha256"]
                or final["physical_sha256"] != run["physical_sha256"]
                or run.get("seam_reuses_same_accepted_full_H_packet") is not True
                or seam["mean_nodes"] != 1168):
            raise ValueError("The final nonlinear-DN field/mean identity changed")
        packet_path, target_path = Path(final["full_height_record"]), Path(final["height_reference"])
        if (packet_path.resolve() != Path(seam["tail_packet"]).resolve()
                or sha(packet_path) != seam["tail_packet_sha256"]):
            raise ValueError("The actual final full-height packet changed")
        stage = next((row for row in reversed(run["stages"])
                      if Path(row["packet"]).resolve() == packet_path.resolve()), None)
        if (stage is None or stage.get("full_height") is not True or stage["factor"] != 1.
                or stage.get("requested_jacobian") is not True
                or stage["packet_sha256"] != seam["tail_packet_sha256"]
                or Path(stage["height_reference"]).resolve() != target_path.resolve()
                or sha(target_path) != stage["height_reference_sha256"]
                or stage["height_reference_key"] != "candidate_H"
                or stage["height_arithmetic"] != "numpy"):
            raise ValueError("The final accepted original full-height request binding changed")
        target = json.loads(target_path.read_text())
        if (target["physical_sha256"] != run["physical_sha256"]
                or target["raw_sha256"] != run["raw_return"]["sha256"]
                or target["gauge_q"] != run["gauge_q"] or target["mean_nodes"] != 1168
                or target["candidate_H"] != run["candidate_H"]
                or target["candidate_H"] != run["raw_return"]["candidate_H"]):
            raise ValueError("The full-height target is not the final actual physical field")
        with gzip.open(packet_path, "rt") as stream:
            packet = json.load(stream)
        if (packet["request"]["height"] != target["candidate_H"]
                or packet["response"]["checkpoint"]["cutHeight"] != target["candidate_H"]
                or packet["request"]["jacobian"] is not True
                or packet["request"]["audit"] is not True):
            raise ValueError("The final original worker packet is not this exact full-height request")
        gate.update(validator="warm_true_dn_solve.validate_warm_source + actual return and full-height bindings",
            validator_sha256=sha(loader_path), acceptance_kind="actual_nonlinear_dn_return",
            actual_DN_checked=True, solver_invoked=True, solver_success=True, raw_success=True,
            linear_source_model_kind=original["model_kind"],
            linear_source_acceptance_kind=run["linear_source_acceptance_kind"],
            linear_source_solver_invoked=run["linear_source_solver_invoked"],
            full_height_packet=str(packet_path.resolve()),
            full_height_packet_sha256=seam["tail_packet_sha256"],
            full_height_target=str(target_path.resolve()), full_height_target_sha256=sha(target_path),
            finite_full_height_request_identity_checked=True,
            exact_infinite_tail_or_Cartesian_attachment_inferred=False)
    else:
        old = module("_seam_original_gate", SCRIPTS / "resume_m3/continue_material_true_tail.py")
        fixed = run.get("fixed_metric") is True
        if kind == WARM:
            if (not fixed or run.get("terminal_kind") != "original_linear_dn"
                    or run.get("status") != "audited_finite_linear_candidate"
                    or run.get("parameter_zero_meaning") != "log(q_aux/gauge_q)"
                    or run.get("raw_return", {}).get("success") is not True):
                raise ValueError("Unsupported or unaccepted warm source-run contract")
            finite_gate(run)
            if sha(HERE / "warm_supported_core_factory.py") != run["warm_provider_sha256"]:
                raise ValueError("The declared warm provider source changed")
            if sha(run["origin_design_run"]) != run["origin_design_sha256"]:
                raise ValueError("The warm branch's actual original anchor changed")
        accepted = (run.get("finite_linear_candidate_pass") is True if fixed else
                    old.prefix_gate(run) and run.get("raw_return", {}).get("success") is True)
        if not accepted or not run.get("solver_success") or run.get("error"):
            raise ValueError("Require an actually accepted original prefix candidate")
        gate.update(validator="original finite linear acceptance gate",
            acceptance_kind="actual_original_bvp_return",
            solver_invoked=True, solver_success=True, raw_success=run["raw_return"].get("success"))
    if sha(physical) != run["physical_sha256"]:
        raise ValueError("Saved physical field changed")
    return run, gate


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ("source-run", "physical", "short-bridge-source", "source-port", "out-npz", "out"):
        ap.add_argument("--" + name, type=Path, required=True)
    ap.add_argument("--tail-packet", type=Path)
    a = ap.parse_args()
    started = time.monotonic()
    primitive = module("_seam_cut_primitive", HERE / "seam_bridge_endpoint_primitive.py")
    profile_module = module("_seam_canonical_profile", SCRIPTS / "resume_m3/multistage_flat_profile.py")
    audit = module("_seam_accepted_tail_input", HERE / "seam_cut_height_compatibility.py")
    short = module("_seam_literal_short_bridge", a.short_bridge_source)
    run, source_gate = accepted_source_record(a.source_run, a.physical)
    warm = run.get("model_kind") in (WARM, WARM + "-v2")
    source_hash = sha(a.short_bridge_source)
    if source_hash != SHORT_SHA:
        raise ValueError("The analyzed literal ShortBridge phase source changed")
    declared = list(run.get("source_hashes", {}).values()) + list(
        run.get("frozen_source_signature", {}).values()
    )
    if source_hash not in declared:
        raise ValueError("ShortBridge source is not bound to this accepted run")
    count = int(run["modes"])
    gauge = fq(run["gauge_q"])
    if gauge != fq(.06):
        raise ValueError("Retain the declared gauge .06; q_actual is not a gauge replacement")
    nodes = int(run.get("mean_nodes", run.get("prefix_audit", {}).get("samples_psi", 0)))
    if nodes != 1168:
        raise ValueError("This map definition requires the preserved mean1168 rule")
    profile = run["frozen_profile"]
    if profile.get("ramp_law") != "held10_multistage_flat_v1":
        raise ValueError("Require the declared canonical multistage profile")
    ref_delta, _, _, _, knots = profile_module._reference(profile)
    sb = fq((float(profile["delta"]) / ref_delta) * knots[-1])
    cut = run["physical_tail_cut"]
    port = json.loads(a.source_port.read_text())
    reference_path = HERE.parents[1] / "notes/2026-11-20-m3-m24-warm050-execution.json"
    reference = json.loads(reference_path.read_text())["config"]
    for key in audit.BACKGROUND_KEYS:
        if run["physical_tail_parameters"].get(key) != reference[key]:
            raise ValueError("Changed true background in prefix run: " + key)
        if port["parameters"].get(key) != reference[key]:
            raise ValueError("Changed true background in original port: " + key)
    if any(fq(cut[key]) != fq(port["cut"][key]) for key in
           ("radius", "backgroundSlope", "backgroundSecond", "E", "Ep")):
        raise ValueError("Prefix background cut differs from original port")
    port_sha = sha(a.source_port)
    declared_ports = list(run.get("inputs", {}).values()) + [run.get("linear_port_sha256")]
    if port_sha not in declared_ports:
        raise ValueError("Original port is not bound to this prefix run")
    if source_gate["actual_DN_checked"]:
        full_packet = Path(source_gate["full_height_packet"])
        packet, response, _, spacing, modes, _ = audit.load_packet(
            full_packet, a.source_port, reference_path)
        if spacing != 3 or modes != count:
            raise ValueError("The actual final tail and prefix dimensions differ")
        if a.tail_packet and sha(a.tail_packet) != source_gate["full_height_packet_sha256"]:
            raise ValueError("An actual-DN trace must use its same accepted final full-height packet")
        source_gate["original_accepted_full_height_residual"] = response["residual"]
        source_gate["original_accepted_full_height_solveTolerance"] = packet["config"]["solveTolerance"]
    bridge_settings = profile["prefix_bridge"]
    if cut.get("_prefix_bridge") != bridge_settings:
        raise ValueError("Actual ShortBridge settings differ from the frozen profile")
    if bridge_settings["kind"] != "turn_plateau_v1":
        raise ValueError("Unsupported terminal phase")
    bridge = short.ShortBridge(
        cut, 1., float(bridge_settings["curvature"]), float(bridge_settings["peak_fraction"])
    )
    sc, Y = endpoint_jets(primitive, a.physical, gauge, count)
    if sc != fq(float(sb) + bridge.L):
        raise ValueError("Physical last node is not the original bridge endpoint")
    a_bounds, phase_parameters = true_radius(primitive, bridge, sc - sb)
    mean_path = SCRIPTS / "resume_m3/certify_r59_fixed_mean_ranges.py"
    kernel_path = SCRIPTS / "finite_closure/m3_m8_closed_map/interval_geometry_kernel.py"
    if sha(mean_path) != MEAN_SHA or sha(kernel_path) != INTERVAL_SHA:
        raise ValueError("Original verified interval kernel changed")
    b = module("_seam_fixed_mean", mean_path)
    b.K = module("_seam_interval_kernel", kernel_path)
    ajets = [b.I(b.I.rational(lo).x[0], b.I.rational(hi).x[1]) for lo, hi in a_bounds]
    psi = 2 * np.pi * np.arange(nodes) / nodes
    psisha = hashlib.sha256(psi.tobytes()).hexdigest()
    if psisha != PSI_SHA:
        raise ValueError("Literal mean1168 nodes changed")
    mean, root_lower = original_mean_at_cut(b, Y, *ajets, psi, count)
    Rc, w = fq(.3), fq(.08)
    wR, E = -7 * w / Rc, 1 + w * w
    if fq(cut["radius"]) != Rc:
        raise ValueError("This common target coordinate is the declared true cut")
    pm = sorted([1] + [1 + sign * 3 * j for j in range(1, count + 1) for sign in (-1, 1)])
    hm = list(range(0, 3 * count + 1, 3))
    planar, height = [], []
    for row in Y:
        coeff = {1: row[0]}
        for j in range(1, count + 1):
            coeff[1 + 3 * j] = (row[j] + row[count + j]) / 2
            coeff[1 - 3 * j] = (row[j] - row[count + j]) / 2
        planar.append(interval_array(b, [coeff[m] for m in pm]))
        height.append(interval_array(b, [F(0)] + row[2 * count + 1:]))
    ip = b.I(np.asarray([int(m == 1) for m in pm]))
    ih = b.I(np.asarray([int(m == 0) for m in hm]))
    planar = [p + ip * av for p, av in zip(planar, ajets)]
    height[1], height[2] = height[1] + ih * mean.v, height[2] + ih * mean.d
    sqrtE = b.I.rational(E).sqrt()
    c2 = -b.I.rational(w * wR) / sqrtE
    pR = [planar[0], -sqrtE * planar[1], b.I.rational(E) * planar[2] + c2 * planar[1]]
    hR = [height[0], -sqrtE * height[1], b.I.rational(E) * height[2] + c2 * height[1]]
    pdef = [pR[0] - b.I.rational(Rc) * ip, pR[1] - ip, pR[2]]
    report = {
        "status": "accepted_prefix_true_cut_R_trace_enclosed",
        "scope": "Current accepted prefix cut only; full Cartesian tail seam is not asserted.",
        "source_sha256": sha(__file__), "source_run_sha256": sha(a.source_run),
        "source_model_kind": run.get("model_kind", "original-design-prefix"),
        "source_terminal_kind": run.get("terminal_kind", "original_linear_dn"),
        "warm_linear_gate_checked": warm,
        "source_acceptance": source_gate,
        "physical_sha256": sha(a.physical), "ShortBridge_sha256": source_hash,
        "source_port_sha256": port_sha,
        "background_record_sha256": sha(reference_path),
        "primitive_helper_sha256": sha(HERE / "seam_bridge_endpoint_primitive.py"),
        "profile_helper_sha256": sha(SCRIPTS / "resume_m3/multistage_flat_profile.py"),
        "mean_kernel_sha256": sha(mean_path), "interval_kernel_sha256": sha(kernel_path),
        "modes": count, "gauge_exact": str(gauge), "mean_nodes": nodes, "psi_sha256": psisha,
        "s_entry_exact": str(sb), "s_cut_exact": str(sc),
        "R_cut_exact": str(Rc), "target_w_exact": str(w), "target_wR_exact": str(wR),
        "literal_phase_parameters": phase_parameters,
        "actual_a_s_jets": [scalar(x) for x in ajets],
        "mean_M": scalar(mean.v), "mean_M_s": scalar(mean.d),
        "literal_node_Frenet_root_lower": root_lower,
        "horizontal_perturbation_R_jet_l1_upper": [l1_upper(b, x) for x in pdef],
        "height_nonzero_R_jet_l1_upper": [l1_upper(b, x.item(slice(1, None))) for x in hR],
        "height_mean_R_first": scalar(hR[1].item(0)),
        "height_mean_R_second": scalar(hR[2].item(0)),
        "height_position_mean": "Same exact Z_cut symbol; NPZ stores position relative to Z_cut.",
        "tail_height_comparison": None,
        "full_H_identity_certified_here": False,
        "Cartesian_C2_seam_certified_here": False,
        "absolute_cut_height_certified_here": False,
        "core_evaluations": 0, "nonlinear_solves": 0,
    }
    extra = {}
    if a.tail_packet:
        packet, response, jets, spacing, tail_count, arrays = audit.load_packet(
            a.tail_packet, a.source_port, reference_path
        )
        if spacing != 3 or tail_count != count:
            raise ValueError("Compare the same complete nonzero cut Fourier dimensions")
        tail_rows = [
            [F(0)] + arrays[0],
            [fq(jets["meanSlope"])] + arrays[1],
            [fq(jets["meanSecond"])] + arrays[2],
        ]
        # Upper tail is reflected lower worker. Zero-mode position cancels
        # symbolically under z_b=Z_cut+mu_cut before any interval subtraction.
        diffs = [h + interval_array(b, t) for h, t in zip(hR, tail_rows)]
        extra["height_bridge_minus_upper_tail_R_jets"] = tensor(diffs)
        for key in ("meanSlopeCorrection", "meanSecondCorrection"):
            if key not in jets:
                raise ValueError("Need the preserved perturbation-mean cut component: " + key)
        true_mean = [
            F(0), w + fq(jets["meanSlopeCorrection"]),
            wR + fq(jets["meanSecondCorrection"]),
        ]
        true_rows = [[zero] + row[1:] for zero, row in zip(true_mean, tail_rows)]
        true_diffs = [h + interval_array(b, t) for h, t in zip(hR, true_rows)]
        extra["height_bridge_minus_true_background_tail_R_jets"] = tensor(true_diffs)
        report["tail_height_comparison"] = {
            "packet_sha256": sha(a.tail_packet), "source_port_sha256": sha(a.source_port),
            "residual": response["residual"], "solveTolerance": packet["config"]["solveTolerance"],
            "complete_difference_R_jet_l1_upper": [l1_upper(b, v) for v in diffs],
            "nonzero_difference_R_jet_l1_upper": [l1_upper(b, v.item(slice(1, None))) for v in diffs],
            "mean_first_difference": scalar(diffs[1].item(0)),
            "mean_second_difference": scalar(diffs[2].item(0)),
            "mean_position_difference_exact": "0 under the preserved Z_cut+mu_cut contract",
            "native_mean_scope": "Saved binary total meanSlope/meanSecond, including the worker background.",
            "true_background_preserved_mean_components": {
                "scope": "Exact true w/wR plus original literal mean corrections. Shared-R stage export must use these same perturbation cut coefficients before treating this as that graph's trace.",
                "true_minus_native_mean_exact": [
                    str(true_mean[j] - tail_rows[j][0]) for j in (1, 2)
                ],
                "complete_difference_R_jet_l1_upper": [
                    l1_upper(b, v) for v in true_diffs
                ],
                "mean_first_difference": scalar(true_diffs[1].item(0)),
                "mean_second_difference": scalar(true_diffs[2].item(0)),
            },
            "full_H_inferred": False,
        }
    bindings = dict(report)
    bindings.pop("tail_height_comparison")
    a.out_npz.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        a.out_npz, planar_modes=np.asarray(pm, int), height_modes=np.asarray(hm, int),
        planar_R_jets=tensor(pR), height_R_jets_relative_Zc=tensor(hR),
        qY_s_jets=tensor([interval_array(b, row) for row in Y]),
        exact_qY_s_jets_json=np.asarray(json.dumps([[str(v) for v in row] for row in Y])),
        bindings_json=np.asarray(json.dumps(bindings)), **extra
    )
    report["npz_sha256"] = sha(a.out_npz)
    report["seconds"] = time.monotonic() - started
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: report[k] for k in (
        "status", "mean_M", "mean_M_s", "height_mean_R_first", "height_mean_R_second",
        "tail_height_comparison", "npz_sha256", "seconds"
    )}))


if __name__ == "__main__":
    main()
