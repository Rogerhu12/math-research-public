#!/usr/bin/env python3
"""Independent relative-operator metric audit of a loaded full prefix map.

No solver, boundary condition, core parameter, lift, chart or gate is changed.
The physical map is reconstructed from the supplied model and its physical
quintic PPoly, including the complete exact reference lift and s-dependent
angular chart. The vertical mean-velocity rule MUST be explicit and is fixed
while angular sampling changes.

Finite samples/FFTs are diagnostics, never continuous certificates. Optional
certified derivative/evaluation/mean/reference bounds supply the exact conditional
continuous-angle enclosure formula at each sampled radial section; its displayed
floating evaluation is not an outward-rounded certificate; radial continuity
remains unpaid. This source has not yet been executed when saved.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.interpolate import PPoly

COMPONENTS = ("ss_minus_1", "s_theta", "theta_theta_minus_1")


def load_physical(path):
    """The actual portable driver's physical.npz, not a raw chart checkpoint."""
    with np.load(path, allow_pickle=False) as data:
        x, c, p = data["x"].copy(), data["c"].copy(), data["p"].copy()
    if c.ndim != 3 or c.shape[0] != 6 or c.shape[1] != len(x)-1:
        raise ValueError("Expected the saved physical quintic PPoly coefficients")
    pp = PPoly.construct_fast(c, x, extrapolate=False, axis=1)
    return SimpleNamespace(x=x, p=p, sol=pp, source_path=str(Path(path).resolve()),
                           source_sha256=hashlib.sha256(Path(path).read_bytes()).hexdigest())


def _rows(value, count, name):
    array = np.asarray(value, dtype=float)
    if array.ndim == 0:
        array = np.full(count, float(array))
    array = array.reshape(-1)
    if len(array) != count or not np.all(np.isfinite(array)):
        raise ValueError("Invalid radial values for "+name)
    return array


def _errors(U, V):
    return np.stack((np.sum(U*U, axis=-1)-1.,
                     np.sum(U*V, axis=-1),
                     np.sum(V*V, axis=-1)-1.), axis=-1)


def _op(errors):
    aa, bb, cc = (errors[..., j] for j in range(3))
    return np.abs((aa+cc)/2.)+np.hypot((aa-cc)/2., bb)


def _top(coefficients, frequencies, number=10):
    magnitude = np.abs(coefficients)
    indices = np.argsort(-magnitude, kind="stable")[:number]
    return [dict(frequency=int(frequencies[j]), absolute=float(magnitude[j]),
                 real=float(coefficients[j].real), imag=float(coefficients[j].imag))
            for j in indices]


def _frame_fields(obj, flow, s, Y, Yp, N, mean, sigma, radius):
    B, B1, B2 = flow.basis(N)
    g = flow.geo(s, N)  # Includes the full installed exact_core_lift.
    d = g["p1"]+obj.q*flow.values(Y, B1)
    dd = g["p2"]+obj.q*flow.values(Y, B2)
    Fsc = g["s1"]+obj.q*flow.values(Yp, B)
    Fsc = np.asarray(Fsc, float).copy()
    Fsc[:, :, 2] += mean[:, None]
    rho, v = g["rho"], g["v"]
    Fs = Fsc-v[:, :, None]*d
    Ftheta = d/rho[:, :, None]
    U, V = Fs/sigma[:, None, None], Ftheta/radius[:, None, None]
    # Exact psi first jets of the same normalized frame. Mean has no psi dependence.
    Fsc_psi = g["sp"]+obj.q*flow.values(Yp, B1)
    Fs_psi = Fsc_psi-g["vp"][:, :, None]*d-v[:, :, None]*dd
    Ftheta_psi = (dd/rho[:, :, None] -
                  d*g["rhop"][:, :, None]/rho[:, :, None]**2)
    Upsi = Fs_psi/sigma[:, None, None]
    Vpsi = Ftheta_psi/radius[:, None, None]
    derivative = np.stack((2.*np.sum(U*Upsi, axis=-1),
                           np.sum(Upsi*V+U*Vpsi, axis=-1),
                           2.*np.sum(V*Vpsi, axis=-1)), axis=-1)
    return _errors(U, V), derivative, Fs, Ftheta, g


def audit_loaded_model(obj, physical, *, angular=(512, 1024), radial=None,
                       mean_nodes=None, mean_provider=None,
                       metric_provider=None, angular_bounds_provider=None,
                       physical_harmonics=24, batch=8, target=1.e-6):
    """Audit an actual loaded model and physical PPoly, without running a BVP.

    mean_provider(s, Y, Yp, flow) -> dict:
      value: actual vertical mean velocity defining this map;
      absolute_error_bound: optional certified error to that actual mean;
      certified: bool; scope: text.
    Alternatively, explicit mean_nodes fixes the original finite periodic
    mean(fr['V']_z) rule at that N for EVERY angular audit. This is a declared
    numerical proxy unless the caller's map is defined by that finite rule.
    Its integration/evaluation error is not silently set to zero.

    metric_provider(s, flow) -> dict:
      sigma: meridian scale in g=sigma(s)^2 ds^2+radius(s)^2 dtheta^2;
      radius; optional sigma_interval/radius_interval, each shape (len(s),2);
      certified: bool; scope: text.
    Without it, sigma=1 and flow.profile(s)[0] are an explicitly numerical
    reference proxy. They are not automatically the R31 true-integral metric.

    angular_bounds_provider(s) -> dict:
      second_derivative_bound: uniform operator bound for d_psi^2 E_proxy;
      evaluation_error_bound: error of ALL sampled proxy matrices;
      certified: bool; scope: text.
    Bounds must hold on the complete angular circle at each supplied s.
    The conditional remainder is (2*pi/N)^2*bound/8. No radial certificate
    is inferred. Empty/missing bounds leave continuous_angle_inputs_declared_certified=False.
    """
    angular = tuple(sorted(set(int(N) for N in angular)))
    if not angular or angular[0] < 16:
        raise ValueError("Require declared angular grids of at least 16 points")
    if (mean_nodes is None) == (mean_provider is None):
        raise ValueError("Declare exactly one fixed mean rule: mean_nodes or mean_provider")
    if mean_nodes is not None and int(mean_nodes) < 16:
        raise ValueError("mean_nodes must be at least 16")
    obj.initial(physical.p)
    flow = obj.flow(physical.p[0])
    if radial is None:
        ss = np.unique(np.r_[np.linspace(physical.x[0], physical.x[-1], 151),
                             physical.x, (physical.x[:-1]+physical.x[1:])/2.])
    else:
        ss = np.unique(np.asarray(radial, float).reshape(-1))
    if len(ss) == 0 or ss[0] < physical.x[0] or ss[-1] > physical.x[-1]:
        raise ValueError("Radial audit lies outside the supplied physical PPoly")
    modes = int(getattr(obj, "base_mode", 3))*np.arange(int(physical_harmonics)+1)
    stats = {N: dict(angular=N, sample_operator_max=-1., peak=None,
                    component_fft_l1=np.zeros(3), legacy_component_fft_l1=np.zeros(3),
                    interpolant_operator_row_sum_bound=0.,
                    components=[None]*3, physical_components=[None]*3,
                    first_angular_derivative_sample_max=0.,
                    common_node_component_difference=np.zeros(3),
                    conditional_angle_upper_max=None,
                    conditional_angle_peak=None,
                    continuous_angle_inputs_declared_certified=True, conditions_seen=0)
             for N in angular}
    mean_scope, metric_scope, bounds_scope = set(), set(), set()
    base_N = angular[0]
    for first in range(0, len(ss), int(batch)):
        s = ss[first:first+int(batch)]
        Y, Yp = physical.sol(s), physical.sol(s, 1)
        count = len(s)
        native_radius = np.asarray(flow.profile(s)[0], float)
        if mean_provider is None:
            _, B1m, B2m = flow.basis(int(mean_nodes))
            fr = flow.frame(s, obj.q*Y, B1m, B2m)
            mean_record = dict(value=np.mean(fr["V"][:, :, 2], axis=1),
                               certified=False,
                               scope="fixed finite periodic mean at N="+str(int(mean_nodes))+
                                     "; no true-mean/evaluation remainder supplied")
        else:
            mean_record = mean_provider(s, Y, Yp, flow)
            if not isinstance(mean_record, dict):
                mean_record = dict(value=mean_record, certified=False,
                                   scope="caller-provided mean; no error contract")
        mean = _rows(mean_record["value"], count, "mean")
        mean_scope.add(str(mean_record.get("scope", "unspecified")))
        mean_error = (None if "absolute_error_bound" not in mean_record else
                      _rows(mean_record["absolute_error_bound"], count, "mean error"))
        if mean_error is not None and float(mean_error.min()) < 0.:
            raise ValueError("Mean error bounds must be nonnegative")
        if metric_provider is None:
            metric_record = dict(sigma=np.ones(count), radius=native_radius,
                                 certified=False,
                                 scope="native numerical flow.profile; true-integral g gap unpaid")
        else:
            metric_record = metric_provider(s, flow)
        sigma = _rows(metric_record["sigma"], count, "metric sigma")
        radius = _rows(metric_record["radius"], count, "metric radius")
        if min(float(sigma.min()), float(radius.min())) <= 0.:
            raise ValueError("Reference metric is not positive")
        metric_scope.add(str(metric_record.get("scope", "unspecified")))
        transfer = None
        if "sigma_interval" in metric_record and "radius_interval" in metric_record:
            si = np.asarray(metric_record["sigma_interval"], float)
            ri = np.asarray(metric_record["radius_interval"], float)
            if si.shape != (count, 2) or ri.shape != (count, 2):
                raise ValueError("Metric intervals must have shape (radial_count,2)")
            if (np.min(si[:, 0]) <= 0. or np.min(ri[:, 0]) <= 0. or
                    np.any(si[:, 1] < si[:, 0]) or np.any(ri[:, 1] < ri[:, 0])):
                raise ValueError("Invalid positive metric intervals")
            low = np.column_stack((sigma/si[:, 1], radius/ri[:, 1]))**2
            high = np.column_stack((sigma/si[:, 0], radius/ri[:, 0]))**2
            transfer = (np.max(high, axis=1),
                        np.max(np.maximum(np.abs(low-1.), np.abs(high-1.)), axis=1))
        bound_record = (None if angular_bounds_provider is None else
                        angular_bounds_provider(s))
        if bound_record is not None:
            second = _rows(bound_record["second_derivative_bound"], count, "angular second bound")
            evaluation = _rows(bound_record["evaluation_error_bound"], count, "evaluation bound")
            if min(float(second.min()), float(evaluation.min())) < 0.:
                raise ValueError("Error bounds must be nonnegative")
            bounds_scope.add(str(bound_record.get("scope", "unspecified")))
        base_errors = None
        for N in angular:
            item = stats[N]
            errors, derivative, Fs, Ft, g = _frame_fields(
                obj, flow, s, Y, Yp, N, mean, sigma, radius)
            if not np.all(np.isfinite(errors)):
                raise FloatingPointError("Nonfinite full-map metric matrix")
            point_op = _op(errors)
            row_peak = np.max(point_op, axis=1)
            ir, ia = np.unravel_index(int(np.argmax(point_op)), point_op.shape)
            if float(point_op[ir, ia]) > item["sample_operator_max"]:
                item["sample_operator_max"] = float(point_op[ir, ia])
                item["peak"] = dict(s=float(s[ir]), radial_index=int(first+ir),
                                    psi=float(2.*np.pi*ia/N),
                                    theta=float(g["theta"][ir, ia]),
                                    components=[float(v) for v in errors[ir, ia]],
                                    operator_norm=float(point_op[ir, ia]))
            item["first_angular_derivative_sample_max"] = max(
                item["first_angular_derivative_sample_max"], float(np.max(_op(derivative))))
            transformed = np.fft.fft(errors, axis=1)/N
            sums = np.sum(np.abs(transformed), axis=1)
            item["component_fft_l1"] = np.maximum(item["component_fft_l1"], sums.max(axis=0))
            item["interpolant_operator_row_sum_bound"] = max(
                item["interpolant_operator_row_sum_bound"],
                float(np.max(np.maximum(sums[:, 0]+sums[:, 1], sums[:, 2]+sums[:, 1]))))
            signed = np.rint(np.fft.fftfreq(N)*N).astype(int)
            for component in range(3):
                r = int(np.argmax(sums[:, component]))
                old = item["components"][component]
                if old is None or float(sums[r, component]) > old["fft_l1"]:
                    item["components"][component] = dict(
                        component=COMPONENTS[component], s=float(s[r]),
                        fft_l1=float(sums[r, component]),
                        pointwise_max_abs=float(np.max(np.abs(errors[r, :, component]))),
                        dominant_psi_bins=_top(transformed[r, :, component], signed))
            if metric_provider is None:
                native_sums = sums
            else:
                native_errors = _errors(Fs, Ft/native_radius[:, None, None])
                native_sums = np.sum(np.abs(np.fft.fft(native_errors, axis=1)/N), axis=1)
            item["legacy_component_fft_l1"] = np.maximum(
                item["legacy_component_fft_l1"], native_sums.max(axis=0))
            # Physical theta Fourier coefficients use the true dtheta=rho dpsi
            # of the declared chart. This remains finite quadrature, not a tail proof.
            phase = np.exp(-1j*g["theta"][:, :, None]*modes[None, None, :])
            coefficients = np.einsum("rnk,rnc,rn->rkc", phase, errors, g["rho"])/N
            for component in range(3):
                r, k = np.unravel_index(int(np.argmax(np.abs(coefficients[:, :, component]))),
                                        coefficients[:, :, component].shape)
                old = item["physical_components"][component]
                amplitude = float(abs(coefficients[r, k, component]))
                if old is None or amplitude > old["maximum_coefficient_abs"]:
                    item["physical_components"][component] = dict(
                        component=COMPONENTS[component], s=float(s[r]),
                        maximum_coefficient_abs=amplitude,
                        dominant_theta_modes=_top(coefficients[r, :, component], modes))
            if N == base_N:
                base_errors = errors.copy()
            elif N % base_N == 0:
                difference = np.max(np.abs(errors[:, ::N//base_N, :]-base_errors), axis=(0, 1))
                item["common_node_component_difference"] = np.maximum(
                    item["common_node_component_difference"], difference)
            usable = (bound_record is not None and mean_error is not None and transfer is not None)
            declared_certified = (usable and bool(bound_record.get("certified", False)) and
                                  bool(mean_record.get("certified", False)) and
                                  bool(metric_record.get("certified", False)))
            item["continuous_angle_inputs_declared_certified"] = item["continuous_angle_inputs_declared_certified"] and declared_certified
            if usable:
                bound = row_peak+evaluation+second*(2.*np.pi/N)**2/8.
                dU = mean_error/sigma
                bound += 2.*np.sqrt(1.+bound)*dU+dU*dU
                bound = transfer[0]*bound+transfer[1]
                r = int(np.argmax(bound))
                if (item["conditional_angle_upper_max"] is None or
                        float(bound[r]) > item["conditional_angle_upper_max"]):
                    item["conditional_angle_upper_max"] = float(bound[r])
                    item["conditional_angle_peak"] = dict(s=float(s[r]), upper=float(bound[r]))
                item["conditions_seen"] += len(s)
    output_rows = []
    for N in angular:
        item = stats[N]
        for key in ("component_fft_l1", "legacy_component_fft_l1",
                    "common_node_component_difference"):
            item[key] = item[key].tolist()
        item["legacy_max_component_fft_l1"] = max(item["legacy_component_fft_l1"])
        item["observed_operator_within_target"] = item["sample_operator_max"] <= target
        item["continuous_angle_inputs_declared_certified"] = bool(
            item["continuous_angle_inputs_declared_certified"] and item["conditions_seen"] == len(ss))
        item["conditional_angle_float_bound_within_target"] = bool(
            item["continuous_angle_inputs_declared_certified"] and item["conditional_angle_upper_max"] <= target)
        output_rows.append(item)
    return dict(
        scope=__doc__, target=float(target), modes=int(obj.M), gauge_q=float(obj.q),
        actual_physical_parameters=np.asarray(physical.p, float).tolist(),
        physical_source_path=getattr(physical, "source_path", None),
        physical_source_sha256=getattr(physical, "source_sha256", None),
        radial_samples=len(ss), radial_range=[float(ss[0]), float(ss[-1])],
        radial_scope="finite physical s sections only; no radial interpolation certificate",
        mean_rule=sorted(mean_scope), mean_nodes=mean_nodes,
        reference_metric=sorted(metric_scope), angular_bound_sources=sorted(bounds_scope),
        physical_fourier_modes=modes.tolist(),
        physical_fourier_scope="weighted finite quadrature in physical theta; no unsampled tail bound",
        continuous_angle_certified_by_this_script=False,
        conditional_bound_arithmetic="displayed floating evaluation of the exact formula; final outward rounding remains external",
        full_prefix_certified=False,
        core_projection_is_not_a_metric_lower_bound=True,
        solver_and_acceptance_gates_changed=False,
        rows=output_rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model-adapter", type=Path, required=True)
    parser.add_argument("--model-config", type=Path, required=True)
    parser.add_argument("--physical", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--angular", type=int, nargs="+", default=[512, 1024])
    parser.add_argument("--mean-nodes", type=int, required=True)
    parser.add_argument("--radial", type=float, nargs="*")
    parser.add_argument("--physical-harmonics", type=int, default=24)
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location("_held10_actual_model_adapter", args.model_adapter)
    adapter = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(adapter)
    obj = adapter.load_model(json.loads(args.model_config.read_text()))
    result = audit_loaded_model(
        obj, load_physical(args.physical), angular=args.angular, radial=args.radial,
        mean_nodes=args.mean_nodes, physical_harmonics=args.physical_harmonics)
    result["audit_source_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result["diagnostics"] = {key: result[key] for key in (
        "radial_samples", "mean_rule", "mean_nodes", "full_prefix_certified", "rows")}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n")
    print(json.dumps(dict(out=str(args.out), radial_samples=result["radial_samples"],
                         observed_operator=[row["sample_operator_max"] for row in result["rows"]],
                         full_prefix_certified=False)), flush=True)


if __name__ == "__main__":
    main()
