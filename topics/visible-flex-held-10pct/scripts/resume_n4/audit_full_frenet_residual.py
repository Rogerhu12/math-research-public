#!/usr/bin/env python3
"""Read-only complete Frenet residual and angular-shell diagnostic.

Load the SAME physical quintic and model as audit_full_relative_metric.py.
The fixed mean rule is independent of every angular evaluation grid.  No
BVP/tail solve, parameter update, interpolation rebuild, or gate change is
performed.  Complete R always uses the actual quintic derivative, full geo
and lift, and moving-chart convection.  A separate native-RHS split never
replaces that derivative.

All FFTs, theta quadratures, sampled rho minima and radial trapezoids below
are numerical diagnostics, not continuous residual/metric certificates.
Only compact maxima, shells and a few leading coefficients are serialized.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import traceback
import numpy as np


def _module(name, path):
    spec = importlib.util.spec_from_file_location(name, Path(path))
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def _sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _rows(value, count):
    result = np.asarray(value, float).reshape(-1)
    if result.shape != (count,) or not np.all(np.isfinite(result)):
        raise ValueError("Mean provider must return one finite value per s")
    return result


def _vector_norm(value):
    return np.sqrt(np.sum(np.abs(value)**2, axis=-1))


def _shells(cutoff, edges):
    ends = sorted(set([0, int(cutoff)]+
                      [min(int(cutoff), int(k)) for k in edges if int(k) >= 0]))
    result = []
    low = 0
    for high in ends:
        if high >= low:
            result.append(dict(low=low, high=high,
                               R_l1_max=0., R_l1_peak_s=None,
                               derivative_l1_max=0., derivative_l1_peak_s=None))
        low = high+1
    return result


def _update_shells(rows, coeff, frequencies, s):
    magnitude = _vector_norm(coeff)
    absolute_k = np.abs(frequencies)
    for row in rows:
        mask = (absolute_k >= row["low"]) & (absolute_k <= row["high"])
        a = np.sum(magnitude[:, mask], axis=1)
        b = np.sum(magnitude[:, mask]*absolute_k[None, mask], axis=1)
        i, j = int(np.argmax(a)), int(np.argmax(b))
        if float(a[i]) > row["R_l1_max"]:
            row["R_l1_max"], row["R_l1_peak_s"] = float(a[i]), float(s[i])
        if float(b[j]) > row["derivative_l1_max"]:
            row["derivative_l1_max"] = float(b[j])
            row["derivative_l1_peak_s"] = float(s[j])


def _top(coeff, frequencies, *, derivative=False, count=10):
    magnitude = _vector_norm(coeff)
    score = magnitude*np.abs(frequencies) if derivative else magnitude
    indices = np.argsort(-score, kind="stable")[:min(count, len(score))]
    return [dict(
        frequency=int(frequencies[j]), vector_coefficient_norm=float(magnitude[j]),
        derivative_weighted_norm=float(abs(frequencies[j])*magnitude[j]),
        real=np.asarray(coeff[j].real, float).tolist(),
        imag=np.asarray(coeff[j].imag, float).tolist()) for j in indices]


def _theta_coefficients(R, theta, rho, modes):
    """Finite dtheta=rho*dpsi quadrature; every Cartesian integer mode."""
    result = np.empty((len(R), len(modes), 3), complex)
    # Bound temporary phase storage independently of the requested cutoff.
    for first in range(0, len(modes), 16):
        kk = modes[first:first+16]
        phase = np.exp(-1j*theta[:, :, None]*kk[None, None, :])
        result[:, first:first+len(kk)] = np.einsum(
            "rnk,rnc,rn->rkc", phase, R, rho, optimize=True)/R.shape[1]
    return result


def _initial_row(N, cutoff, edges):
    return dict(
        angular=int(N), R_sample_max=0., R_sample_peak=None,
        R_cartesian_component_sample_max=np.zeros(3),
        R_psi_interpolant_l1_max=0.,
        Rpsi_psi_interpolant_weighted_l1_max=0.,
        Rtheta_grid_derivative_sample_max=0.,
        tangent_Rtheta_c2_sample_max=0.,
        tangent_Rtheta_dft_sample_max=0.,
        tangent_Rtheta_c2_minus_dft_sample_max=0.,
        normalized_angular_length_material_s_derivative_sample_max=0.,
        tangent_Rtheta_c2_peak=None, tangent_Rtheta_difference_peak=None,
        Rtheta_psi_interpolant_over_sample_rho_proxy_max=0.,
        R_material_truncated_l1_max=0.,
        Rtheta_material_truncated_weighted_l1_max=0.,
        native_radial_projection_defect_sample_max=0.,
        complement_after_native_projection_sample_max=0.,
        mean_zero_mode_Rz_sample_max=0.,
        fixed_mean_minus_evaluation_mean_max=0.,
        Rz_zero_mode_minus_mean_discrepancy_max=0.,
        convection_sample_max=0.,
        rho_sample_min=float("inf"),
        root_margin_sample_min=float("inf"),
        inlet_relative_angular_length_error_sample_max=None,
        common_node_R_difference_max=0.,
        material_common_coefficient_difference_l1_max=0.,
        material_common_derivative_coefficient_difference_l1_max=0.,
        psi_shells=_shells(N//2, edges),
        material_theta_shells=_shells(cutoff, edges),
        psi_R_peak_spectrum=None, psi_Rpsi_peak_spectrum=None,
        material_R_peak_spectrum=None, material_Rtheta_peak_spectrum=None)


def diagnose_loaded_model(obj, physical, *, angular=(512, 1024),
                          mean_nodes=None, mean_provider=None, radial=None,
                          physical_cutoff=96, shell_edges=None, batch=8,
                          native_projection_split=True):
    """Evaluate only: physical.sol is the actual saved physical-s quintic.

    mean_provider(s,Y,Ys,flow) may return {"value": ..., "scope": ...};
    alternatively mean_nodes fixes the identical original finite mean rule
    at every angular evaluation grid.  Neither choice is silently certified.
    """
    angular = tuple(sorted(set(int(n) for n in angular)))
    if not angular or min(angular) < 16 or int(batch) < 1:
        raise ValueError("Declare angular grids >=16 and a positive batch")
    if (mean_nodes is None) == (mean_provider is None):
        raise ValueError("Supply exactly one fixed mean rule")
    if mean_nodes is not None and int(mean_nodes) < 16:
        raise ValueError("mean_nodes must be at least 16")
    cutoff = int(physical_cutoff)
    if cutoff < 1 or 2*cutoff >= min(angular):
        raise ValueError("Require 1 <= physical_cutoff < min(angular)/2")
    p0 = np.asarray(physical.p, float).copy()
    obj.initial(p0)
    flow = obj.flow(float(p0[0]))
    if radial is None:
        ss = np.unique(np.r_[np.linspace(physical.x[0], physical.x[-1], 151),
                             physical.x, (physical.x[:-1]+physical.x[1:])/2.])
    else:
        ss = np.unique(np.asarray(radial, float).reshape(-1))
    if (len(ss) == 0 or not np.all(np.isfinite(ss)) or
            ss[0] < physical.x[0] or ss[-1] > physical.x[-1]):
        raise ValueError("Use finite radial points inside the physical quintic")
    base_mode = int(getattr(obj, "base_mode", 3))
    field_edge = base_mode*int(obj.M)+1
    edges = ([0, base_mode, field_edge, 2*field_edge, 4*field_edge, 8*field_edge]
             if shell_edges is None else list(shell_edges))
    stats = {N: _initial_row(N, cutoff, edges) for N in angular}
    profiles = {N: dict(
        psi_c1=np.zeros(len(ss)), theta_c1=np.zeros(len(ss)),
        radius=np.zeros(len(ss))) for N in angular}
    means_seen = set()
    physical_modes = np.arange(-cutoff, cutoff+1, dtype=int)
    base_N = angular[0]
    for first in range(0, len(ss), int(batch)):
        s = ss[first:first+int(batch)]
        Y, Ys = physical.sol(s), physical.sol(s, 1)
        if not np.all(np.isfinite(Y)) or not np.all(np.isfinite(Ys)):
            raise FloatingPointError("Actual physical quintic is nonfinite")
        radius = np.asarray(flow.profile(s)[0], float)
        if not np.all(np.isfinite(radius)) or np.any(radius <= 0):
            raise FloatingPointError("Original physical profile radius is not positive")
        if mean_provider is None:
            _, B1m, B2m = flow.basis(int(mean_nodes))
            frm = flow.frame(s, obj.q*Y, B1m, B2m)
            mean = _rows(np.mean(frm["V"][:, :, 2], axis=1), len(s))
            means_seen.add("fixed original finite periodic W_z mean at N="+
                           str(int(mean_nodes))+"; no continuous-mean remainder")
        else:
            mr = mean_provider(s, Y, Ys, flow)
            if isinstance(mr, dict):
                mean = _rows(mr["value"], len(s))
                means_seen.add(str(mr.get("scope", "caller-provided mean")))
            else:
                mean = _rows(mr, len(s))
                means_seen.add("caller-provided mean; no error contract")
        # Optional decomposition only.  R below ALWAYS uses actual Ys.
        projected = (np.asarray(flow.fun(s, Y, p0), float)
                     if native_projection_split else None)
        base_R, base_theta_coeff = None, None
        for N in angular:
            item = stats[N]
            B, B1, B2 = flow.basis(N)
            fr = flow.frame(s, obj.q*Y, B1, B2)
            g = fr["geo"]  # Full background, original chart and reference lift.
            Ps = np.asarray(g["s1"]+obj.q*flow.values(Ys, B), float).copy()
            Ps[:, :, 2] += mean[:, None]
            R = Ps-fr["V"]  # Original V is Vnormal + v * P_psi.
            rho = np.asarray(g["rho"], float)
            if (not np.all(np.isfinite(R)) or not np.all(np.isfinite(rho)) or
                    np.any(rho <= 0)):
                raise FloatingPointError("Original full residual/chart is not regular")
            norms = _vector_norm(R)
            ir, ia = np.unravel_index(int(np.argmax(norms)), norms.shape)
            if float(norms[ir, ia]) > item["R_sample_max"]:
                item["R_sample_max"] = float(norms[ir, ia])
                item["R_sample_peak"] = dict(
                    s=float(s[ir]), radial_index=int(first+ir),
                    psi=float(2*np.pi*ia/N), theta=float(g["theta"][ir, ia]),
                    R=np.asarray(R[ir, ia], float).tolist(),
                    norm=float(norms[ir, ia]))
            item["R_cartesian_component_sample_max"] = np.maximum(
                item["R_cartesian_component_sample_max"],
                np.max(np.abs(R), axis=(0, 1)))
            item["rho_sample_min"] = min(item["rho_sample_min"], float(np.min(rho)))
            item["root_margin_sample_min"] = min(
                item["root_margin_sample_min"], float(np.min(fr["margin"])))
            item["convection_sample_max"] = max(
                item["convection_sample_max"],
                float(np.max(_vector_norm(g["v"][:, :, None]*fr["d"]))))
            rz_zero = np.mean(R[:, :, 2], axis=1)
            mean_discrepancy = mean-np.mean(fr["V"][:, :, 2], axis=1)
            item["mean_zero_mode_Rz_sample_max"] = max(
                item["mean_zero_mode_Rz_sample_max"],
                float(np.max(np.abs(rz_zero))))
            item["fixed_mean_minus_evaluation_mean_max"] = max(
                item["fixed_mean_minus_evaluation_mean_max"],
                float(np.max(np.abs(mean_discrepancy))))
            item["Rz_zero_mode_minus_mean_discrepancy_max"] = max(
                item["Rz_zero_mode_minus_mean_discrepancy_max"],
                float(np.max(np.abs(rz_zero-mean_discrepancy))))
            if first == 0 and ss[0] == physical.x[0]:
                u0 = fr["lam"][0]/rho[0]/radius[0]
                item["inlet_relative_angular_length_error_sample_max"] = float(
                    np.max(np.abs(u0-1.)))
            if native_projection_split:
                radial_defect = obj.q*flow.values(Ys-projected, B)
                complement = R-radial_defect
                item["native_radial_projection_defect_sample_max"] = max(
                    item["native_radial_projection_defect_sample_max"],
                    float(np.max(_vector_norm(radial_defect))))
                item["complement_after_native_projection_sample_max"] = max(
                    item["complement_after_native_projection_sample_max"],
                    float(np.max(_vector_norm(complement))))
            transformed = np.fft.fft(R, axis=1)/N
            frequencies = np.rint(np.fft.fftfreq(N)*N).astype(int)
            magnitudes = _vector_norm(transformed)
            sums = np.sum(magnitudes, axis=1)
            weighted = np.sum(magnitudes*np.abs(frequencies)[None, :], axis=1)
            rho_min = np.min(rho, axis=1)
            psi_proxy = weighted/rho_min
            item["R_psi_interpolant_l1_max"] = max(
                item["R_psi_interpolant_l1_max"], float(np.max(sums)))
            item["Rpsi_psi_interpolant_weighted_l1_max"] = max(
                item["Rpsi_psi_interpolant_weighted_l1_max"], float(np.max(weighted)))
            item["Rtheta_psi_interpolant_over_sample_rho_proxy_max"] = max(
                item["Rtheta_psi_interpolant_over_sample_rho_proxy_max"],
                float(np.max(psi_proxy)))
            _update_shells(item["psi_shells"], transformed, frequencies, s)
            for key, score, derivative in (
                    ("psi_R_peak_spectrum", sums, False),
                    ("psi_Rpsi_peak_spectrum", weighted, True)):
                r = int(np.argmax(score))
                if item[key] is None or float(score[r]) > item[key]["score"]:
                    item[key] = dict(s=float(s[r]), score=float(score[r]),
                                     leading=_top(transformed[r], frequencies,
                                                  derivative=derivative))
            # Canonical real trigonometric interpolant derivative at the nodes.
            # The even-N Nyquist cosine derivative is zero AT those nodes.
            half = np.fft.rfft(R, axis=1)
            khalf = np.arange(half.shape[1], dtype=float)
            derivative_half = 1j*khalf[None, :, None]*half
            if N % 2 == 0:
                derivative_half[:, -1, :] = 0.
            Rpsi_grid = np.fft.irfft(derivative_half, n=N, axis=1)
            Rtheta_grid = Rpsi_grid/rho[:, :, None]
            item["Rtheta_grid_derivative_sample_max"] = max(
                item["Rtheta_grid_derivative_sample_max"],
                float(np.max(_vector_norm(Rtheta_grid))))
            # Independent C2 scalar identity, without differentiating V:
            # T.R_theta = T.F_s,theta - (a_s/a)|F_theta|.
            # Both moving-chart derivative terms remain explicit.
            Fspsi = (g["sp"]+obj.q*flow.values(Ys, B1) -
                     g["vp"][:, :, None]*fr["d"] -
                     g["v"][:, :, None]*fr["dd"])
            elltheta = fr["lam"]/rho
            tangent_c2 = (
                np.sum(fr["T"]*(Fspsi/rho[:, :, None]), axis=2) -
                (np.asarray(fr["ap"])/radius)[:, None]*elltheta)
            tangent_dft = np.sum(fr["T"]*Rtheta_grid, axis=2)
            tangent_difference = tangent_c2-tangent_dft
            length_drift = tangent_c2/radius[:, None]
            item["tangent_Rtheta_c2_sample_max"] = max(
                item["tangent_Rtheta_c2_sample_max"],
                float(np.max(np.abs(tangent_c2))))
            item["tangent_Rtheta_dft_sample_max"] = max(
                item["tangent_Rtheta_dft_sample_max"],
                float(np.max(np.abs(tangent_dft))))
            item["tangent_Rtheta_c2_minus_dft_sample_max"] = max(
                item["tangent_Rtheta_c2_minus_dft_sample_max"],
                float(np.max(np.abs(tangent_difference))))
            item["normalized_angular_length_material_s_derivative_sample_max"] = max(
                item["normalized_angular_length_material_s_derivative_sample_max"],
                float(np.max(np.abs(length_drift))))
            for key, field in (
                    ("tangent_Rtheta_c2_peak", tangent_c2),
                    ("tangent_Rtheta_difference_peak", tangent_difference)):
                r, j = np.unravel_index(int(np.argmax(np.abs(field))), field.shape)
                score = float(abs(field[r, j]))
                if item[key] is None or score > item[key]["absolute"]:
                    item[key] = dict(
                        absolute=score, s=float(s[r]), radial_index=int(first+r),
                        psi=float(2*np.pi*j/N), theta=float(g["theta"][r, j]),
                        tangent_Rtheta_c2=float(tangent_c2[r, j]),
                        tangent_Rtheta_dft=float(tangent_dft[r, j]),
                        difference=float(tangent_difference[r, j]),
                        normalized_length_material_s_derivative=float(length_drift[r, j]))

            # Physical theta coefficients use ALL integer Cartesian modes,
            # including horizontal +/-1+n*j; no scalar n*j restriction.
            material = _theta_coefficients(
                R, np.asarray(g["theta"]), rho, physical_modes)
            material_mag = _vector_norm(material)
            material_sum = np.sum(material_mag, axis=1)
            material_weighted = np.sum(
                material_mag*np.abs(physical_modes)[None, :], axis=1)
            item["R_material_truncated_l1_max"] = max(
                item["R_material_truncated_l1_max"], float(np.max(material_sum)))
            item["Rtheta_material_truncated_weighted_l1_max"] = max(
                item["Rtheta_material_truncated_weighted_l1_max"],
                float(np.max(material_weighted)))
            _update_shells(
                item["material_theta_shells"], material, physical_modes, s)
            for key, score, derivative in (
                    ("material_R_peak_spectrum", material_sum, False),
                    ("material_Rtheta_peak_spectrum", material_weighted, True)):
                r = int(np.argmax(score))
                if item[key] is None or float(score[r]) > item[key]["score"]:
                    item[key] = dict(s=float(s[r]), score=float(score[r]),
                                     leading=_top(material[r], physical_modes,
                                                  derivative=derivative))
            if N == base_N:
                base_R, base_theta_coeff = R.copy(), material.copy()
            else:
                if N % base_N == 0:
                    difference = R[:, ::N//base_N, :]-base_R
                    item["common_node_R_difference_max"] = max(
                        item["common_node_R_difference_max"],
                        float(np.max(_vector_norm(difference))))
                c_difference = _vector_norm(material-base_theta_coeff)
                item["material_common_coefficient_difference_l1_max"] = max(
                    item["material_common_coefficient_difference_l1_max"],
                    float(np.max(np.sum(c_difference, axis=1))))
                item["material_common_derivative_coefficient_difference_l1_max"] = max(
                    item["material_common_derivative_coefficient_difference_l1_max"],
                    float(np.max(np.sum(
                        c_difference*np.abs(physical_modes)[None, :], axis=1))))
            sl = slice(first, first+len(s))
            profiles[N]["psi_c1"][sl] = psi_proxy
            profiles[N]["theta_c1"][sl] = material_weighted
            profiles[N]["radius"][sl] = radius
    rows = []
    for N in angular:
        item, prof = stats[N], profiles[N]
        item["R_cartesian_component_sample_max"] = (
            item["R_cartesian_component_sample_max"].tolist())
        integrals = {}
        for name in ("psi_c1", "theta_c1"):
            q = prof[name]/prof["radius"]
            integrals[name] = float(np.sum(
                .5*(q[:-1]+q[1:])*np.diff(ss))) if len(ss) > 1 else 0.
        item["radial_trapezoid_diagnostic"] = dict(
            start=float(ss[0]), end=float(ss[-1]),
            integral_Rtheta_proxy_over_a_from_psi=integrals["psi_c1"],
            integral_truncated_Rtheta_spectrum_over_a=integrals["theta_c1"],
            angular_or_radial_tail_certified=False)
        scalar_scale = item["tangent_Rtheta_c2_sample_max"]
        item["tangent_derivative_difference_over_c2_scale"] = (
            item["tangent_Rtheta_c2_minus_dft_sample_max"]/scalar_scale
            if scalar_scale > 0 else None)
        item["scope"] = (
            "finite actual-field evaluations; FFT/quadrature/trapezoid proxies only")
        rows.append(item)
    if not np.array_equal(np.asarray(physical.p), p0):
        raise ValueError("Diagnostic changed physical parameter input")
    return dict(
        scope=__doc__, status="evaluated", modes=int(obj.M), base_mode=base_mode,
        q_gauge=float(obj.q), actual_parameters=p0.tolist(),
        physical_source_path=getattr(physical, "source_path", None),
        physical_source_sha256=getattr(physical, "source_sha256", None),
        radial_samples=len(ss), radial_range=[float(ss[0]), float(ss[-1])],
        radial_rule="151 uniform + every actual quintic knot + every midpoint"
                    if radial is None else "explicit supplied finite radial points",
        mean_nodes=mean_nodes, mean_rule=sorted(means_seen),
        mean_integration_error_paid=False,
        native_projection_split=bool(native_projection_split),
        native_projection_nodes=int(flow.B.shape[1]),
        projection_split_scope=(
            "R_radial=q_g B(Ys-Flow.fun); complement=complete R-R_radial. "
            "Complement includes finite native projection and mean-rule effects; "
            "it is not asserted to be only an exact omitted Fourier tail."),
        psi_spectrum_scope=(
            "DFT of complete Cartesian R on uniform psi; |k|-weighted shell is "
            "the trigonometric interpolant derivative. Dividing by sampled rho "
            "does not certify the continuous material derivative."),
        material_theta_spectrum_scope=(
            "finite rho-weighted quadrature of all integer modes -K..K; "
            "|k| multiplies the estimated R coefficient for a derivative proxy. "
            "No unsampled physical-mode tail or quadrature error is bounded."),
        physical_cutoff=cutoff, input_shell_edges=[int(k) for k in edges],
        common_reference_angular=base_N,
        profile_scope="native fixed profile evaluation; no true-integral error bound",
        mean_zero_mode_scope=(
            "At each N, R_z mean equals fixed mean minus evaluated W_z mean "
            "up to the actual finite P_s vertical mean. Changing N never "
            "changes the defining mean_nodes rule."),
        tangent_c2_scope=(
            "T.Rtheta=T.(Fspsi/rho)-(a_s/a)|Ftheta| from actual C2 jets; "
            "Fspsi retains -v_psi P_psi-v P_psipsi. No assumption G=a^2, "
            "no third angular jet, and no continuous bound is used. "
            "Reported comparison is at the same finite nodes only."),
        fixed_g_convergence_claim=False, continuous_angle_certified=False,
        continuous_radial_certified=False, full_metric_gate_evaluated=False,
        solver_and_acceptance_gates_changed=False,
        bvp_or_tail_solver_invoked=False, rows=rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model-adapter", type=Path, required=True)
    parser.add_argument("--model-config", type=Path, required=True)
    parser.add_argument("--physical", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--metric-loader", type=Path, default=(
        Path(__file__).resolve().parents[1]/"resume_m3"/"audit_full_relative_metric.py"))
    parser.add_argument("--angular", type=int, nargs="+", default=[512, 1024])
    parser.add_argument("--mean-nodes", type=int, required=True)
    parser.add_argument("--physical-cutoff", type=int, default=96)
    parser.add_argument("--shell-edges", type=int, nargs="+")
    parser.add_argument("--radial", type=float, nargs="*")
    parser.add_argument("--batch", type=int, default=8)
    parser.add_argument("--no-native-projection-split", action="store_true")
    args = parser.parse_args()
    try:
        loader = _module("_held10_residual_physical_loader", args.metric_loader)
        adapter = _module("_held10_residual_model_adapter", args.model_adapter)
        obj = adapter.load_model(json.loads(args.model_config.read_text()))
        physical = loader.load_physical(args.physical)
        result = diagnose_loaded_model(
            obj, physical, angular=args.angular, mean_nodes=args.mean_nodes,
            physical_cutoff=args.physical_cutoff, shell_edges=args.shell_edges,
            radial=args.radial, batch=args.batch,
            native_projection_split=not args.no_native_projection_split)
        result["command"] = sys.argv
        result["source_sha256"] = dict(
            diagnostic=_sha(__file__), metric_loader=_sha(args.metric_loader),
            model_adapter=_sha(args.model_adapter), model_config=_sha(args.model_config))
        result["diagnostics"] = {k: result[k] for k in (
            "radial_samples", "mean_nodes", "mean_rule", "physical_cutoff",
            "continuous_angle_certified", "full_metric_gate_evaluated", "rows")}
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n")
        print(json.dumps(dict(
            status="evaluated", out=str(args.out),
            residual=[row["R_sample_max"] for row in result["rows"]],
            material_derivative_proxy=[
                row["Rtheta_material_truncated_weighted_l1_max"]
                for row in result["rows"]],
            continuous_certificate=False)), flush=True)
    except Exception as error:
        trace = traceback.format_exc()[-8000:]
        result = dict(
            status="error", error=type(error).__name__+": "+str(error),
            traceback=trace, bvp_or_tail_solver_invoked=False,
            solver_and_acceptance_gates_changed=False,
            diagnostics=dict(error=type(error).__name__+": "+str(error),
                             traceback=trace, continuous_certificate=False))
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n")
        print(json.dumps(dict(status="error", out=str(args.out),
                              error=result["error"])), flush=True)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
