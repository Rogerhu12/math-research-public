#!/usr/bin/env python3
"""True finite-mean height of one new accepted complete m3 warm field.

The map is the explicit common-right-two-jet Y/e interpretation, the frozen
amplitude prefix normalized once to its literal physical endpoint, and the
true integral of the same literal ShortBridge phase.  It uses the complete
new true-core lift at the original literal mean1168 nodes.  The source float
GL6 primitive is not substituted for this integral.  All complete radial
leaves and core interval arrays remain on the runner, outside git.
"""
import os
for _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_name] = "1"
import argparse
from bisect import bisect_right
from fractions import Fraction as Q
import gc
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time

import numpy as np

HERE = Path(__file__).resolve().parent
SUPPORT = HERE.parent / "resume_m3"
REPO = HERE.parents[3]
sys.path.insert(0, str(SUPPORT))
sys.path.insert(0, str(HERE))
import certify_bridge_metric_fourier_taylor as jets
import certify_prefix_metric_interval_taylor as prefix_mean
from seam_m3_prefix_pieces import M3PrefixPieces
import certify_r59_shared_jet_transfer as shared

MEAN_SHA = "ab08dc1dc7f24f6e92e3d64fcc530767cb66f5ae5a2940f953460a3274b6a1a5"
INTERVAL_SHA = "6234c458d303dfd2e47dcf1e1a6ee54a3d466118a8aea4d76f66013154c034e7"
PSI_SHA = "f4834f978de38046e374b020d2a928d293fc405f794159e40e2271f4ee9bd9cf"
SHORT_SHA = "7e00a3336a302ba94c751c09e6f75749d6973c86605269538c8f0b44c60779b4"
WARM = "warm-supported-material-phase-fixed-metric"
ACTUAL = WARM + "-actual-dn"
WARM_LINEAR_MODELS = {
    WARM + "-v2": "warm_fixed_m3_model_v2.py",
    WARM + "-v3": "warm_fixed_m3_model_v3.py",
}
I = jets.I


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def fq(value):
    value = float(value)
    if not math.isfinite(value):
        raise ValueError("Nonfinite literal input")
    return Q.from_float(value)


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


def read(path):
    path = Path(path)
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt") as stream:
        return json.load(stream)


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path))


def checked(reference):
    path = Path(reference["path"])
    if sha(path) != reference["sha256"]:
        raise ValueError("Bound artifact changed: " + str(path))
    return read(path)


def write(path, data):
    path = Path(path)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(data, indent=2, allow_nan=False) + "\n")
    temporary.replace(path)


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                    allow_nan=False).encode()).hexdigest()


def source_model(path, allow_intermediate):
    """Use explicit family gates, preserving honest reexpression provenance."""
    run = read(path)
    kind = run.get("model_kind")
    if kind in WARM_LINEAR_MODELS:
        adapter_path = HERE / WARM_LINEAR_MODELS[kind]
        adapter = module("_seam_height_versioned_warm", adapter_path)
        run = adapter.accepted_input(path, require_lambda_one=not allow_intermediate)
        gate = dict(validator=adapter_path.stem + ".accepted_input",
                    source=ref(adapter_path), acceptance_kind=run["acceptance_kind"],
                    solver_invoked=run["solver_invoked"], solver_success=run["solver_success"],
                    raw_success=run["raw_return"]["success"])
        if run["acceptance_kind"] == "same_cartesian_map_verified_reexpression":
            gate["source_solver_provenance"] = run["source_solver_provenance"]
    elif kind == ACTUAL:
        gate_path = HERE / "warm_actual_dn_acceptance.py"
        validator = module("_seam_height_actual_gate", gate_path)
        run = validator.accepted_actual_input(path, repo=REPO)
        adapter = module("_seam_height_actual_model", HERE / "warm_true_dn_solve.py")
        gate = dict(validator="warm_actual_dn_acceptance.accepted_actual_input",
                    source=ref(gate_path), acceptance_kind="actual_nonlinear_dn_return",
                    solver_invoked=True, solver_success=True, raw_success=True,
                    linear_source_model_kind=run["linear_source_model_kind"],
                    linear_source_acceptance_kind=run["linear_source_acceptance_kind"],
                    linear_source_solver_invoked=run["linear_source_solver_invoked"],
                    finite_full_height_request_identity_checked=True,
                    exact_infinite_tail_or_Cartesian_attachment_inferred=False)
    else:
        raise ValueError("Use an explicit warm-v2, warm-v3 or warm actual-DN source contract")
    if (run.get("mean_nodes") != 1168 or not isinstance(run["modes"], int) or run["modes"] < 1
            or fq(run["gauge_q"]) != fq(.06)
            or run.get("parameter_zero_meaning") != "log(q_aux/gauge_q)"):
        raise ValueError("Retain the actual positive mode count, gauge .06 and literal mean1168 contract")
    if not allow_intermediate and run["warm_definition"]["homotopy"] != 1.:
        raise ValueError("Default geometry entry requires the actual lambda-one field")
    # Read-only reconstruction selects the declared source family; no BVP or
    # nonlinear tail is evaluated by load_model.
    model = adapter.load_model(dict(source_run=str(path), repo=str(REPO)))
    return run, model, Path(adapter.__file__).resolve(), gate


def core_intervals(certificate_path, arrays_path, run_path, physical_path, run):
    certificate = read(certificate_path)
    if (certificate.get("complete") is not True or certificate.get("mean_nodes") != 1168
            or certificate.get("kind") != "warm_true_core_literal_mean_intervals"
            or certificate.get("format_version") != 1
            or certificate.get("model_kind") != run["model_kind"]
            or certificate.get("modes") != run["modes"]
            or certificate.get("source_run_sha256") != sha(run_path)
            or certificate.get("physical_sha256") != sha(physical_path)
            or certificate.get("literal_psi_sha256") != PSI_SHA):
        raise ValueError("Require the complete new true-core literal-mean1168 certificate")
    if certificate.get("warm_definition_sha256") != canonical_sha(run["warm_definition"]):
        raise ValueError("The true-core definition is not this frozen warm definition")
    source_family = run.get("linear_source_model_kind", run["model_kind"])
    if source_family == WARM + "-v3":
        if (certificate.get("linear_source_model_kind") != source_family
                or certificate.get("warm_definition") != run["warm_definition"]
                or certificate.get("phase_basis") != run["warm_definition"]["phase_basis"]
                or any(certificate.get(key) != run[key] for key in
                       ("basis_anchor_v2_run", "basis_anchor_v2_sha256"))):
            raise ValueError("The v3 true-core proof belongs to a different complete phase family or zero-control anchor")
    binding = certificate["arrays"]
    if Path(binding["path"]).resolve() != arrays_path.resolve() or sha(arrays_path) != binding["sha256"]:
        raise ValueError("True core interval arrays changed")
    sources = certificate.get("source_hashes")
    if not isinstance(sources, dict) or not sources:
        raise ValueError("The true-core proof entry must bind its actual source files")
    for name, digest in sources.items():
        if sha(name) != digest:
            raise ValueError("True core oracle source changed: " + name)
    psi = 2 * np.pi * np.arange(1168) / 1168
    if hashlib.sha256(psi.tobytes()).hexdigest() != PSI_SHA:
        raise ValueError("The original literal angular-node construction changed")
    result = {}
    with np.load(arrays_path, allow_pickle=False) as data:
        for name in ("psi_lo", "psi_hi"):
            if name not in data or not np.array_equal(data[name], psi):
                raise ValueError("Core mean intervals use a different angular rule")
        for name in ("H1", "H2"):
            values = data[name]
            if (values.dtype != np.float64 or values.shape != (2, 1168, 3)
                    or not np.all(np.isfinite(values)) or np.any(values[0] > values[1])):
                raise ValueError("Invalid complete Cartesian lift interval array: " + name)
            result[name] = values.copy()
        initial = data["exact_lift_initial"]
        if (initial.dtype != np.float64 or initial.shape != (3 * run["modes"] + 1,)
                or not np.all(np.isfinite(initial))
                or hashlib.sha256(initial.tobytes()).hexdigest() != certificate["exact_lift_initial_sha256"]):
            raise ValueError("The frozen complete lift projection identity changed")
        result["exact_lift_initial"] = initial.copy()
    return certificate, psi, result


def ipoly(coefficients, x):
    value = I(0)
    for coefficient in coefficients[::-1]:
        value = value * x + coefficient
    return value


def interval_array(values):
    pairs = [I.rational(v).x for v in values]
    return I(np.asarray([float(v[0]) for v in pairs]), np.asarray([float(v[1]) for v in pairs]))


def packed_interval(low, high):
    lo = float(I.rational(low).x[0])
    hi = float(I.rational(high).x[1])
    return dict(lower=lo, upper=hi, lower_exact=str(low), upper_exact=str(high))


class MeanMap:
    """Only actual new coefficients, with the original explicit C2 convention."""
    def __init__(self, model, physical, psi, lift_arrays):
        self.p = p = M3PrefixPieces(model, physical)
        self.f = f = p.f
        self.M, self.n, self.N = p.M, p.n, 1168
        if not np.array_equal(np.asarray(f.exact_lift_initial, float), lift_arrays["exact_lift_initial"]):
            raise ValueError("The new true-core lift did not subtract this same complete literal projection")
        self.entry, self.end, self.xx, self.spx = p.entry, p.end, p.xx, p.spx
        if (self.xx[0] != 0 or self.xx[-1] != self.end or
                f.cfg["prefix_bridge"] != dict(kind="turn_plateau_v1", curvature=4, peak_fraction=.2)):
            raise ValueError("The saved physical domain or the original short bridge changed")
        self.endpoint_algebra = p.exact_endpoint_report()
        # Endpoint identities have been checked exactly. The defining source
        # and the outward interval coefficients remain; these large Fraction
        # dictionaries are proof temporaries, unused by profile/lift or mean.
        p.field_coefficients_exact.clear()
        p.field_right_targets_exact.clear()
        gc.collect()
        self.q = I.rational(fq(model.q))
        self.pc = dict(p.pc)
        # The same right-hand node two-jets are used across the prefix/bridge.
        for i in range(len(self.xx) - 1):
            if i in self.pc:
                continue
            h = self.xx[i + 1] - self.xx[i]
            rows = []
            for j in range(self.n):
                original = [fq(physical.sol.c[5 - k, i, j]) for k in range(6)]
                if i + 1 < len(self.xx) - 1:
                    target = [fq(physical.sol.c[5, i + 1, j]),
                              fq(physical.sol.c[4, i + 1, j]),
                              2 * fq(physical.sol.c[3, i + 1, j])]
                else:
                    target = [shared.value(shared.derivative(original, k), h) for k in range(3)]
                correction, _ = shared.right_correction(original, h, target)
                poly = [v + c for v, c in zip(original, correction)]
                if [shared.value(shared.derivative(poly, k), h) for k in range(3)] != target:
                    raise ArithmeticError("The common exact bridge Y two-jet identity failed")
                rows.append(poly)
            self.pc[i] = [interval_array([row[k] for row in rows]) for k in range(6)]
        self.cutoff = Q(3, 4) * self.end
        self.ec = {}
        for i in range(len(self.spx) - 1):
            original = [fq(f.spline.c[3 - k, i]) / self.end ** k for k in range(4)]
            h = self.spx[i + 1] - self.spx[i]
            if i + 1 < len(self.spx) - 1:
                target = [fq(f.spline.c[3, i + 1]), fq(f.spline.c[2, i + 1]) / self.end,
                          2 * fq(f.spline.c[1, i + 1]) / self.end ** 2]
            else:
                target = [shared.value(shared.derivative(original, k), h) for k in range(3)]
            correction, _ = shared.right_correction(original, h, target)
            common = [(original[k] if k < 4 else Q(0)) + correction[k] for k in range(6)]
            for late in (False, True):
                poly = common
                if late:
                    u = [(self.spx[i] - self.cutoff) / (self.end / 4), 4 / self.end]
                    cutoff = [Q(1)] + [Q(0)] * 5
                    for factor, degree in ((-10, 3), (15, 4), (-6, 5)):
                        for j, value in enumerate(shared.power(u, degree)):
                            cutoff[j] += factor * value
                    poly = shared.mul(poly, cutoff)
                poly = [fq(f.warp_e) * v for v in poly]
                self.ec[i, late] = ([I.rational(v) for v in poly],
                                    [I.rational(v) for v in shared.derivative(poly)])
        table = prefix_mean.AngleTable(psi, psi, f.even)
        self.cp, self.sp = table.cp, table.sp
        self.co3, self.sn3, self.co, self.sn = table.co3, table.sn3, table.co, table.sn
        self.fr = I(np.asarray(f.even, int)[:, None])
        self.lift = []
        for name in ("H1", "H2"):
            values = lift_arrays[name]
            x, y, z = [I(values[0, :, k], values[1, :, k]) for k in range(3)]
            self.lift.append([x * self.cp + y * self.sp, -x * self.sp + y * self.cp, z])
        primitive = module("_seam_height_true_bridge", HERE / "seam_bridge_endpoint_primitive.py")
        self.bridge_phase = primitive
        bridge = f.bridge
        self.peak, self.eps, self.L1, self.L2, self.L3 = map(
            fq, (bridge.peak, bridge.eps, bridge.L1, bridge.L2, bridge.L3))
        if not (bridge.astart == 1. and 0 < self.eps < self.peak < 2
                and min(self.L1, self.L2, self.L3) > 0):
            raise ValueError("The actual short-bridge analytic phase is outside scope")
        self.first = primitive.sin_polynomial([Q(0), Q(0), 3 * self.peak, -2 * self.peak], 40)
        self.last = primitive.sin_polynomial([self.peak, Q(0), -self.eps], 40)
        self.first_integral = [I(0)] + [I.rational(v / (j + 1)) for j, v in enumerate(self.first)]
        self.last_integral = [I(0)] + [I.rational(v / (j + 1)) for j, v in enumerate(self.last)]
        self.drop1 = I.rational(self.L1) * ipoly(self.first_integral, I(1))
        self.plateau = I.rational(primitive.sin_polynomial([self.peak], 40)[0])
        self.bridge_remainder = self.peak ** 41 / math.factorial(41)
        self.grid = sorted(set(p.grid + [self.end, self.cutoff]
            + [v for v in self.xx + self.spx if self.entry < v < self.end]
            + [self.entry + self.L1, self.entry + self.L1 + self.L2]))
        if self.grid[0] != 0 or self.grid[-1] != self.end:
            raise ValueError("The continuous mean partition does not cover exactly the full physical domain")

    def chart(self, s, left, right):
        middle = (left + right) / 2
        index = min(len(self.spx) - 2, bisect_right(self.spx, middle) - 1)
        if not (self.spx[index] <= left <= right <= self.spx[index + 1]):
            raise ValueError("An angular polynomial breakpoint was omitted")
        c, d = self.ec[index, middle > self.cutoff]
        x = s - I.rational(self.spx[index])
        return ipoly(c, x), ipoly(d, x)

    def field(self, s, left, right):
        index = min(len(self.xx) - 2, bisect_right(self.xx, (left + right) / 2) - 1)
        if not (self.xx[index] <= left <= right <= self.xx[index + 1]):
            raise ValueError("A physical quintic breakpoint was omitted")
        return ipoly(self.pc[index], s - I.rational(self.xx[index])) * self.q

    def bridge(self, left, right):
        middle = (left + right) / 2 - self.entry
        first, last = left - self.entry, right - self.entry
        if last <= self.L1:
            u = I.rational(middle / self.L1)
            radius = 1 - I.rational(self.L1) * ipoly(self.first_integral, u)
            def phi(x):
                z = x / self.L1
                return self.peak * (3 * z * z - 2 * z * z * z)
            low, high = phi(first), phi(last)
        elif first >= self.L1 and last <= self.L1 + self.L2:
            radius = 1 - self.drop1 - I.rational(middle - self.L1) * self.plateau
            low = high = self.peak
        elif first >= self.L1 + self.L2:
            u = (middle - self.L1 - self.L2) / self.L3
            end_u = (last - self.L1 - self.L2) / self.L3
            if not 0 <= u <= end_u < Q(1001, 1000):
                raise ValueError("The terminal bridge extension is outside its stated interval")
            radius = (1 - self.drop1 - I.rational(self.L2) * self.plateau
                      - I.rational(self.L3) * ipoly(self.last_integral, I.rational(u)))
            low = self.peak - self.eps * end_u ** 2
            high = self.peak - self.eps * ((first - self.L1 - self.L2) / self.L3) ** 2
        else:
            raise ValueError("A true bridge phase join was omitted")
        if not 0 <= low <= high <= self.peak:
            raise ValueError("The declared bridge phase range failed")
        phase = I(float(I.rational(low).x[0]), float(I.rational(high).x[1]))
        sine, _ = jets.m.sincos_i(phase)
        # The center integral has its explicit Taylor remainder.  Since the
        # derivative is -sin(phi), the radius changes by at most |s-center|.
        error = I.rational(middle * self.bridge_remainder + (right - left) / 2)
        pad = I(-float(error.x[1]), float(error.x[1]))
        return radius + pad, -sine

    def evaluate(self, left, right):
        s = I(float(I.rational(left).x[0]), float(I.rational(right).x[1]))
        y = self.field(s, left, right)
        e, ep = self.chart(s, left, right)
        if right <= self.entry:
            aa, ap = self.p.profile(s, left, right)
            aa, ap = aa.v, ap.v
            chi = self.p.lift(s, left, right)[0].v
            chi = I(np.maximum(0., chi.x[0]), np.minimum(1., chi.x[1]))
        elif left >= self.entry:
            aa, ap = self.bridge(left, right)
            chi = I(0)
        else:
            raise ValueError("The prefix/bridge breakpoint was omitted")
        rho, rp = 1 - e * self.co3, 3 * e * self.sn3
        if float(np.min(aa.x[0])) <= 0 or float(np.min(rho.x[0])) <= 0:
            raise ValueError("Positive radius or angular chart is unresolved")
        rr = y.item(slice(1, self.M + 1)).expand()
        tt = y.item(slice(self.M + 1, 2 * self.M + 1)).expand()
        zz = y.item(slice(2 * self.M + 1, None)).expand()
        R = y.item(0) + (rr * self.co).sum()
        Rp, Rpp = -(rr * self.fr * self.sn).sum(), -(rr * self.fr.sq() * self.co).sum()
        T, Tp = (tt * self.sn).sum(), (tt * self.fr * self.co).sum()
        Tpp = -(tt * self.fr.sq() * self.sn).sum()
        Zp, Zpp = -(zz * self.fr * self.sn).sum(), -(zz * self.fr.sq() * self.co).sum()
        d1 = [Rp - T, Tp + R, Zp]
        d2 = [Rpp - 2 * Tp - R, Tpp + 2 * Rp - T, Zpp]
        d1 = [v + aa * chi * h for v, h in zip(d1, self.lift[0])]
        d2 = [v + aa * chi * h for v, h in zip(d2, self.lift[1])]
        sd, cd = jets.m.sincos_i(e * self.sn3 / 3)
        R1, T1 = d1[0] * cd - d1[1] * sd, d1[0] * sd + d1[1] * cd
        R2, T2 = d2[0] * cd - d2[1] * sd, d2[0] * sd + d2[1] * cd
        U = [R1 / (aa * rho), 1 + T1 / (aa * rho), d1[2] / (aa * rho)]
        V = [-1 + R2 / (aa * rho.sq()) - R1 * rp / (aa * rho ** 3),
             T2 / (aa * rho.sq()) - T1 * rp / (aa * rho ** 3),
             d2[2] / (aa * rho.sq()) - d1[2] * rp / (aa * rho ** 3)]
        def dot(x, z):
            return sum((a * b for a, b in zip(x, z)), I(0))
        def norm(x):
            return sum((v.sq() for v in x), I(0)).sqrt()
        def cross(x, z):
            return [x[1] * z[2] - x[2] * z[1], x[2] * z[0] - x[0] * z[2],
                    x[0] * z[1] - x[1] * z[0]]
        un = norm(U)
        ka = norm(cross(U, V)) / (un ** 3)
        tangent = [v / un for v in U]
        projection = dot(tangent, V)
        normal0 = [v - projection * t for v, t in zip(V, tangent)]
        nn = norm(normal0)
        normal = [v / nn for v in normal0]
        binormal = cross(tangent, normal)
        alpha = -ap / ka
        root = 1 - alpha.sq()
        if np.any(root.x[0] <= 0):
            raise ValueError("The continuous fixed-node Frenet root is unresolved")
        vertical = alpha * normal[2] + root.sqrt() * binormal[2]
        # Exact orthonormality gives this bound, independently of interval width.
        vertical = I(np.maximum(-1., vertical.x[0]), np.minimum(1., vertical.x[1]))
        convection = -ep * self.sn3 / (3 * rho) * d1[2]
        mean = (vertical + convection).sum() / self.N
        if not mean.finite():
            raise ArithmeticError("Nonfinite mean enclosure")
        return mean, float(np.min(root.x[0]))


def placement(bundle_path, source_run, height):
    bundle = read(bundle_path)
    if (bundle.get("status") != "accepted_new_tail_shared_R_representation_exported"
            or bundle.get("actual_cut_stage_exported") is not True):
        raise ValueError("Require the actual new canonical stage-zero tail export")
    if bundle["finite_scope"]["M"] != source_run["modes"] or bundle["finite_scope"]["spacing"] != 3:
        raise ValueError("A tail bundle at another finite mode count cannot supply this placement")
    if bundle["source_port"]["sha256"] != source_run["linear_port_sha256"]:
        raise ValueError("Prefix and tail use different physical ports")
    reference = checked(bundle["height_identity"]["reference"])
    if reference.get("physical_sha256") != source_run["physical_sha256"]:
        raise ValueError("Tail height reference belongs to a different physical prefix field")
    chain = checked(bundle["mean_chain"])
    manifest = checked(bundle["shared_R_manifest"])
    if (chain.get("status") != "all_saved_initial_states_matched_single_mean_chain"
            or chain["all_stage_input_maximum_difference"] != 0
            or manifest["input"] != bundle["mean_chain"]
            or manifest["existingCheckpoint"] != bundle["accepted_packet"]
            or chain["checkpoint"] != bundle["accepted_packet"]):
        raise ValueError("The original full perturbation mean chain binding changed")
    checked(bundle["accepted_packet"])
    row = next(v for v in manifest["files"] if v["stage"] == 0)
    stage = checked(row)
    if (stage["sharing"]["mapHash"] != row["mapHash"]
            or stage["boundInput"] != bundle["mean_chain"] or stage["stage"] != 0):
        raise ValueError("The stage-zero exact common map identity changed")
    cut = stage["nodes"][-1]
    mu = fq(chain["mean_chain"][0][0])
    hm, pm = stage["heightModes"], stage["planarModes"]
    if (cut["canonicalNode"] != 0 or fq(cut["radiusJS"]) != fq(.3)
            or fq(cut["meanPerturbation"]) != mu
            or fq(cut["coefficients"][0][len(pm) + hm.index(0)]) != mu):
        raise ValueError("The original tail cut perturbation mean was replaced")
    low, high = height[0] + mu, height[1] + mu
    return dict(geometry_bundle=ref(bundle_path), original_mean_chain=bundle["mean_chain"],
        stage_zero_map_hash=row["mapHash"], original_mu_cut_exact=str(mu),
        rule="z_b = Z_cut + original_mu_cut; one common exact height translation",
        z_b_interval=packed_interval(low, high), R58_placement_window=[.1, 1.28],
        R58_placement_condition_proved=(low >= Q(1, 10) and high <= Q(32, 25)),
        height_identity=bundle["height_identity"], full_height_coupling_proved=False,
        common_Cartesian_two_jet_attachment_proved=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("source-run", "physical", "core-mean-certificate", "core-mean-intervals",
                 "interval-kernel", "outdir"):
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--tail-geometry-bundle", type=Path)
    parser.add_argument("--allow-intermediate-lambda", action="store_true",
                        help="Audit this actual intermediate field without claiming lambda-one geometry")
    parser.add_argument("--cell-mean-width", type=float, default=.02)
    parser.add_argument("--max-cells", type=int, default=60000)
    parser.add_argument("--max-depth", type=int, default=24)
    args = parser.parse_args()
    out = args.outdir.resolve()
    if out == REPO or REPO in out.parents:
        raise ValueError("Full radial certificate leaves and arrays must remain outside git")
    if (not math.isfinite(args.cell_mean_width) or args.cell_mean_width <= 0
            or args.max_cells < 1 or args.max_depth < 1):
        raise ValueError("Positive enclosure controls required")
    out.mkdir(parents=True, exist_ok=False)
    summary_path = out / "true-cut-height.json"
    begin = time.monotonic()
    report = dict(status="validating_actual_inputs", complete=False, source=ref(__file__),
        source_run=ref(args.source_run), physical=ref(args.physical), mean_nodes=1168,
        source_GL6_replaced_by_true_primitive=True, new_BVP_or_tail_solver_invoked=False,
        old_field_height_bounds_reused=False, closed_surface_proved=False)
    write(summary_path, report)
    try:
        if sha(SUPPORT / "certify_r59_fixed_mean_ranges.py") != MEAN_SHA:
            raise ValueError("The reviewed finite-mean interval arithmetic source changed")
        if sha(args.interval_kernel) != INTERVAL_SHA:
            raise ValueError("The reviewed outward interval kernel changed")
        jets.m.K = module("_seam_height_intervals", args.interval_kernel)
        run_path = args.source_run.resolve()
        run, model, loader_path, source_gate = source_model(run_path, args.allow_intermediate_lambda)
        if sha(args.physical) != run["physical_sha256"]:
            raise ValueError("The saved actual physical field changed")
        sources = list(run.get("frozen_source_signature", {}).values())
        if SHORT_SHA not in sources:
            raise ValueError("This field does not bind the reviewed original ShortBridge source")
        core_record, psi, lift = core_intervals(
            args.core_mean_certificate, args.core_mean_intervals, run_path, args.physical, run)
        loader = module("_seam_height_physical", SUPPORT / "audit_full_relative_metric.py")
        physical = loader.load_physical(args.physical)
        if (physical.x.dtype != np.float64 or physical.sol.c.dtype != np.float64
                or physical.sol.c.shape != (6, len(physical.x) - 1, 3 * run["modes"] + 1)
                or physical.p.shape != (run["modes"],)
                or not all(np.all(np.isfinite(v)) for v in (physical.x, physical.sol.c, physical.p))
                or not np.all(np.diff(physical.x) > 0)):
            raise ValueError("Invalid original complete m3 physical quintic")
        obj = MeanMap(model, physical, psi, lift)
        report.update(status="integrating_actual_continuous_mean",
            model_kind=run["model_kind"], homotopy=run["warm_definition"]["homotopy"],
            source_acceptance=source_gate,
            source_acceptance_kind=source_gate["acceptance_kind"],
            source_solver_invoked=source_gate["solver_invoked"],
            source_model_loader=ref(loader_path), core_mean_certificate=ref(args.core_mean_certificate),
            core_mean_intervals=ref(args.core_mean_intervals),
            literal_psi_sha256=PSI_SHA, gauge_exact=str(fq(run["gauge_q"])),
            modes=obj.M, physical_field_dimension=obj.n,
            actual_frequencies=obj.p.frequencies.tolist(),
            exact_lift_initial_sha256=core_record["exact_lift_initial_sha256"],
            true_height_anchor_exact="0", prefix_end_exact=str(obj.entry),
            cut_s_exact=str(obj.end), exact_prefix_endpoint_algebra=obj.endpoint_algebra,
            proof_temporary_lifetime=dict(
                exact_field_and_right_target_dictionaries_released_after_endpoint_check=True,
                interval_pc_and_profile_and_lift_retained=True,
                physical_input_or_mathematical_map_changed=False),
            literal_bridge_phase_exact={name: str(getattr(obj, name)) for name in
                                        ("peak", "eps", "L1", "L2", "L3")},
            original_frozen_source_signature=run["frozen_source_signature"],
            helper_sources={str(path): sha(path) for path in (
                HERE / "seam_m3_prefix_pieces.py",
                SUPPORT / "certify_prefix_metric_interval_taylor.py",
                SUPPORT / "certify_r59_shared_jet_transfer.py",
                SUPPORT / "certify_bridge_metric_fourier_taylor.py",
                SUPPORT / "certify_r59_fixed_mean_ranges.py",
                HERE / "seam_bridge_endpoint_primitive.py", args.interval_kernel)},
            explicit_map_definition=dict(
                field="Exact quintic Hermite of right-side literal physical node two-jets; final node from last left polynomial",
                angular_chart="Same exact shared-right-two-jet spline times the original late quintic cutoff",
                prefix_profile="Frozen amplitude delta; exact original rational velocity table; duration normalized once to literal prefix_end",
                bridge_profile="True integral of minus sine of the original literal phase; analytic terminal extension to physical.x[-1]",
                core="Complete newly certified true R53 plus supported material-phase lift; source frozen projection constants retained",
                mean="Equal positive weights at the original literal NumPy binary64 mean1168 nodes; true radial primitive from zero"),
            source_float_map_identified_with_explicit_C2_map=False,
            metric_or_geometry_transfer_to_original_target_certified=False)
        write(summary_path, report)
        todo = [(l, r, 0) for l, r in zip(obj.grid[:-1], obj.grid[1:])][::-1]
        sums = {"prefix": [Q(0), Q(0)], "bridge": [Q(0), Q(0)]}
        attempts = accepted = splits = domain_splits = 0
        root_min, mean_low, mean_high = math.inf, math.inf, -math.inf
        max_depth = 0
        last_event = time.monotonic()
        failure = None
        leaves = out / "continuous-mean-leaves.jsonl.gz"
        with gzip.open(leaves, "wt") as stream:
            while todo:
                if attempts >= args.max_cells:
                    left, right, depth = todo[-1]
                    failure = dict(left_exact=str(left), right_exact=str(right), depth=depth,
                                   reason="declared absolute radial-box attempt budget reached",
                                   mean_range=None)
                    break
                left, right, depth = todo.pop()
                attempts += 1
                try:
                    mean, root = obj.evaluate(left, right)
                    lo, hi = map(float, mean.x)
                    valid = fq(hi) - fq(lo) <= fq(args.cell_mean_width)
                    reason = "continuous mean interval wider than requested"
                except (ValueError, ArithmeticError, FloatingPointError) as exc:
                    valid, reason = False, str(exc)
                    lo = hi = root = None
                    domain_splits += 1
                if not valid:
                    if attempts >= args.max_cells or depth >= args.max_depth:
                        failure = dict(left_exact=str(left), right_exact=str(right), depth=depth,
                                       reason=reason, mean_range=[lo, hi])
                        break
                    middle = (left + right) / 2
                    todo.extend(((middle, right, depth + 1), (left, middle, depth + 1)))
                    splits += 1
                else:
                    part = "prefix" if right <= obj.entry else "bridge"
                    if part == "bridge" and left < obj.entry:
                        raise ArithmeticError("An accepted cell crossed the exact prefix endpoint")
                    length = right - left
                    sums[part][0] += length * fq(lo)
                    sums[part][1] += length * fq(hi)
                    stream.write(json.dumps(dict(part=part, left_exact=str(left), right_exact=str(right),
                        mean_lower_exact=str(fq(lo)), mean_upper_exact=str(fq(hi)),
                        frenet_root_lower=root, depth=depth), separators=(",", ":")) + "\n")
                    accepted += 1
                    max_depth = max(max_depth, depth)
                    root_min = min(root_min, root)
                    mean_low, mean_high = min(mean_low, lo), max(mean_high, hi)
                if time.monotonic() - last_event >= 20:
                    event = dict(stage="true_mean_integral", accepted_cells=accepted,
                        attempted_cells=attempts, pending_cells=len(todo), seconds=time.monotonic() - begin)
                    print(json.dumps(event), flush=True)
                    report.update(progress=event)
                    write(summary_path, report)
                    last_event = time.monotonic()
        complete = failure is None and not todo
        height = [sums["prefix"][j] + sums["bridge"][j] for j in range(2)]
        report.update(status=("actual_true_cut_height_enclosed" if complete else
                              "actual_true_cut_height_unresolved"), complete=complete,
            actual_leaf_record=ref(leaves), accepted_cells=accepted, attempted_cells=attempts,
            split_cells=splits, interval_domain_bisections=domain_splits, maximum_depth=max_depth,
            absolute_radial_box_attempt_budget=args.max_cells,
            failed_cell=failure, remaining_cells=len(todo),
            prefix_integral=packed_interval(*sums["prefix"]),
            bridge_integral=packed_interval(*sums["bridge"]),
            Z_cut_interval=(packed_interval(*height) if complete else None),
            partial_integrals_are_not_Z_cut=(not complete),
            frenet_root_lower=(root_min if accepted else None),
            continuous_mean_range=([mean_low, mean_high] if accepted else None),
            integration="Exact rational outward Darboux sums; every physical, profile, chart, lift and bridge phase break is included",
            same_common_Z_cut_symbol_as_bridge_trace=True)
        if complete and args.tail_geometry_bundle:
            report["tail_absolute_placement"] = placement(args.tail_geometry_bundle, run, height)
        report["seconds"] = time.monotonic() - begin
        write(summary_path, report)
        print(json.dumps({key: report.get(key) for key in (
            "status", "complete", "accepted_cells", "attempted_cells", "Z_cut_interval",
            "frenet_root_lower", "tail_absolute_placement", "failed_cell", "seconds")}), flush=True)
        return 0 if complete else 1
    except Exception as exc:
        report.update(status="failed", complete=False, error=repr(exc), seconds=time.monotonic() - begin)
        write(summary_path, report)
        raise


if __name__ == "__main__":
    raise SystemExit(main())
