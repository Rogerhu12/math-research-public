#!/usr/bin/env python3
"""R103 curvature gates for complete, fixed-scale position two-jets.

This module evaluates arrays only. Its CLI uses artificial local jets and never
loads a research candidate. Research geometry must be evaluated in public Actions.
The caller supplies a>0 broadcastable to the point shape (radial[:, None] for
a radial-by-angle grid). The scale a and radius target tau are fixed parameters.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

JET_NAMES = ("Xs", "Xt", "Xss", "Xst", "Xtt")
ROW_NAMES = ("plus_trace", "plus_determinant", "minus_trace", "minus_determinant")


def _dot(left, right):
    return np.einsum("...c,...c->...", left, right)


def _dot_jac(left, right):
    return np.einsum("...c,...cn->...n", left, right)


def curvature_values(data, a, tau, *, area_floor=1e-10):
    """Four exact smooth PSD rows plus the actual first/second forms.

    Degenerate or nonfinite jets are rejected before any row can be accepted.
    Neither a target unit metric nor a unit-T shortcut is used.
    """
    tau, area_floor = float(tau), float(area_floor)
    if not np.isfinite(tau) or tau <= 0:
        raise ValueError("finite positive curvature radius target required")
    if not np.isfinite(area_floor) or area_floor < 0:
        raise ValueError("finite nonnegative independent area floor required")
    fields = {name: np.asarray(data[name], dtype=float) for name in JET_NAMES}
    shape = fields["Xs"].shape
    if not shape or shape[-1] != 3:
        raise ValueError("position jets must end in a three-vector axis")
    if any(x.shape != shape or not np.all(np.isfinite(x)) for x in fields.values()):
        raise ValueError("matching finite complete position two-jets required")
    scale = np.broadcast_to(np.asarray(a, dtype=float), shape[:-1])
    if not np.all(np.isfinite(scale)) or np.any(scale <= 0):
        raise ValueError("fixed scale a must be finite and positive")
    A = fields["Xs"]
    T = fields["Xt"] / scale[..., None]
    U = fields["Xss"]
    V = fields["Xst"] / scale[..., None]
    W = fields["Xtt"] / scale[..., None] ** 2
    w = np.cross(A, T)
    q2 = _dot(w, w)
    q = np.sqrt(q2)
    if np.any(q <= area_floor) or not np.all(np.isfinite(q)):
        raise ValueError("independent regular-normal-area gate failed")
    E, F, G = _dot(A, A), _dot(A, T), _dot(T, T)
    e, f, k = _dot(w, U), _dot(w, V), _dot(w, W)
    h11 = np.stack((q * E + tau * e, q * E - tau * e), axis=-1)
    h12 = np.stack((q * F + tau * f, q * F - tau * f), axis=-1)
    h22 = np.stack((q * G + tau * k, q * G - tau * k), axis=-1)
    trace = h11 + h22
    determinant = h11 * h22 - h12 * h12
    rows = np.stack((trace[..., 0], determinant[..., 0],
                     trace[..., 1], determinant[..., 1]), axis=-1)
    if not np.all(np.isfinite(rows)):
        raise FloatingPointError("nonfinite actual-metric curvature PSD rows")
    actual_I = np.stack((E, F, F, G), axis=-1).reshape(shape[:-1] + (2, 2))
    numerator_K = np.stack((e, f, f, k), axis=-1).reshape(shape[:-1] + (2, 2))
    return dict(A=A, T=T, U=U, V=V, W=W, w=w, q=q, q2=q2,
                E=E, F=F, G=G, e=e, f=f, k=k,
                h11=h11, h12=h12, h22=h22, rows=rows,
                actual_I=actual_I, numerator_K=numerator_K,
                actual_II=numerator_K / q[..., None, None],
                scale=scale, tau=tau, area_floor=area_floor)


def curvature_parameter_jacobian(data, a, tau, *, area_floor=1e-10, values=None):
    """Analytic complete physical Jacobian, shape points+(4, parameters).

    Reusing values requires the caller to pass the same immutable physical state,
    a and tau. No auxiliary epigraph variable is appended here.
    """
    v = curvature_values(data, a, tau, area_floor=area_floor) if values is None else values
    if float(tau) != v["tau"] or float(area_floor) != v["area_floor"]:
        raise ValueError("curvature values and derivative configuration differ")
    scale = np.broadcast_to(np.asarray(a, dtype=float), v["q"].shape)
    if not np.array_equal(scale, v["scale"]):
        raise ValueError("curvature values and derivative scale differ")
    jac = {name: np.asarray(data["jac_" + name], dtype=float) for name in JET_NAMES}
    shape = v["A"].shape
    sample = jac["Xs"]
    if sample.ndim != len(shape) + 1 or sample.shape[:-1] != shape:
        raise ValueError("complete two-jet Jacobians need a final parameter axis")
    if any(x.shape != sample.shape or not np.all(np.isfinite(x)) for x in jac.values()):
        raise ValueError("matching finite complete two-jet parameter Jacobians required")
    dA = jac["Xs"]
    dT = jac["Xt"] / scale[..., None, None]
    dU = jac["Xss"]
    dV = jac["Xst"] / scale[..., None, None]
    dW = jac["Xtt"] / scale[..., None, None] ** 2
    dw = np.moveaxis(
        np.cross(np.moveaxis(dA, -1, -2), v["T"][..., None, :])
        + np.cross(v["A"][..., None, :], np.moveaxis(dT, -1, -2)), -2, -1)
    dq = _dot_jac(v["w"], dw) / v["q"][..., None]
    dE = 2 * _dot_jac(v["A"], dA)
    dF = _dot_jac(v["T"], dA) + _dot_jac(v["A"], dT)
    dG = 2 * _dot_jac(v["T"], dT)
    de = _dot_jac(v["U"], dw) + _dot_jac(v["w"], dU)
    df = _dot_jac(v["V"], dw) + _dot_jac(v["w"], dV)
    dk = _dot_jac(v["W"], dw) + _dot_jac(v["w"], dW)

    def pair(metric, dmetric, dsecond):
        base = dq * metric[..., None] + v["q"][..., None] * dmetric
        return np.stack((base + v["tau"] * dsecond,
                         base - v["tau"] * dsecond), axis=-2)

    dh11 = pair(v["E"], dE, de)
    dh12 = pair(v["F"], dF, df)
    dh22 = pair(v["G"], dG, dk)
    dtrace = dh11 + dh22
    ddet = (v["h22"][..., :, None] * dh11
            + v["h11"][..., :, None] * dh22
            - 2 * v["h12"][..., :, None] * dh12)
    result = np.stack((dtrace[..., 0, :], ddet[..., 0, :],
                       dtrace[..., 1, :], ddet[..., 1, :]), axis=-2)
    if not np.all(np.isfinite(result)):
        raise FloatingPointError("nonfinite complete curvature parameter Jacobian")
    return result


def polynomial_gate_matrix(values):
    """The optional division-free R103 matrix q^4 I-tau^2 K adj(I) K."""
    I, K = values["actual_I"], values["numerator_K"]
    adj = np.stack((values["G"], -values["F"], -values["F"], values["E"]),
                   axis=-1).reshape(I.shape)
    return (values["q2"][..., None, None] ** 2 * I
            - values["tau"] ** 2 * (K @ adj @ K))


def independent_principal_curvatures(values):
    """Independent diagnostic using the actual metric Cholesky congruence."""
    L = np.linalg.cholesky(values["actual_I"])
    inverse_L = np.linalg.inv(L)
    S = inverse_L @ values["actual_II"] @ np.swapaxes(inverse_L, -1, -2)
    return np.linalg.eigvalsh(S)


def _graph_jet(kx, ky, *, scale=1., skew=False):
    # Local graph z=(kx*x^2+ky*y^2)/2 at its origin, with an optional
    # nonorthogonal material-coordinate change and independent fixed a.
    u = np.array([2., 0.]) if skew else np.array([1., 0.])
    v = np.array([.3, .75]) if skew else np.array([0., 1.])
    quadratic = np.diag([float(kx), float(ky)])
    return dict(Xs=np.r_[u, 0.], Xt=scale * np.r_[v, 0.],
                Xss=np.array([0., 0., u @ quadratic @ u]),
                Xst=scale * np.array([0., 0., u @ quadratic @ v]),
                Xtt=scale ** 2 * np.array([0., 0., v @ quadratic @ v]))


def artificial_check():
    cases = []
    for name, kx, ky in [("plane", 0., 0.), ("sphere_local_jet", .5, .5),
                        ("cylinder_local_jet", 0., .5), ("saddle_local_jet", -.5, .5)]:
        for skew in [False, True]:
            for tau in [1.7, 2.2]:
                scale = 2.3
                v = curvature_values(_graph_jet(kx, ky, scale=scale, skew=skew), scale, tau)
                principal = independent_principal_curvatures(v)
                expected = max(abs(kx), abs(ky)) <= 1 / tau
                row_pass = bool(np.all(v["rows"] >= -1e-12))
                polynomial_pass = bool(np.all(np.linalg.eigvalsh(polynomial_gate_matrix(v)) >= -1e-12))
                cases.append(dict(name=name, nonorthogonal_chart=skew, tau=tau,
                                  analytic_curvatures=[kx, ky],
                                  observed_curvatures=principal.tolist(),
                                  expected_pass=expected, row_pass=row_pass,
                                  polynomial_pass=polynomial_pass,
                                  eigenvalue_error=float(np.max(abs(principal - np.sort([kx, ky]))))))

    # R103's explicit counterexample to replacing the actual metric with g.
    counterexample = dict(Xs=np.array([.5, 0., 0.]), Xt=np.array([0., 1., 0.]),
                          Xss=np.array([0., 0., .5]), Xst=np.zeros(3), Xtt=np.zeros(3))
    cv = curvature_values(counterexample, 1., 1.)
    frozen_metric_would_pass = bool(np.max(abs(np.linalg.eigvalsh(cv["actual_II"]))) < 1.)
    actual_metric_rejects = bool(np.any(cv["rows"] < 0))

    rng = np.random.default_rng(603)
    data = {}
    base = _graph_jet(.37, -.23, scale=1.4, skew=True)
    for name in JET_NAMES:
        data[name] = np.broadcast_to(base[name], (2, 3, 3)).copy()
        data["jac_" + name] = rng.normal(size=(2, 3, 3, 5)) * .03
    scale = np.full((2, 1), 1.4)
    values = curvature_values(data, scale, 1.3)
    jac = curvature_parameter_jacobian(data, scale, 1.3, values=values)
    direction = rng.normal(size=5)
    eps = 1e-6
    plus, minus = {}, {}
    for name in JET_NAMES:
        delta = np.einsum("...cn,n->...c", data["jac_" + name], direction)
        plus[name], minus[name] = data[name] + eps * delta, data[name] - eps * delta
    finite_difference = (curvature_values(plus, scale, 1.3)["rows"]
                         - curvature_values(minus, scale, 1.3)["rows"]) / (2 * eps)
    analytic = np.einsum("...rn,n->...r", jac, direction)
    derivative_error = float(np.max(abs(finite_difference - analytic))
                             / (1 + np.max(abs(analytic))))

    reversed_data = {}
    # An ambient reflection reverses normal orientation and swaps H+ with H-.
    reflection = np.array([-1., 1., 1.])
    for name in JET_NAMES:
        reversed_data[name] = data[name] * reflection
    reverse_rows = curvature_values(reversed_data, scale, 1.3)["rows"]
    orientation_error = float(np.max(abs(reverse_rows - values["rows"][..., [2, 3, 0, 1]])))

    degenerate = dict(counterexample)
    degenerate["Xt"] = degenerate["Xs"].copy()
    degenerate_rejected = False
    try:
        curvature_values(degenerate, 1., 1.)
    except ValueError as exc:
        degenerate_rejected = "regular-normal-area" in str(exc)
    passed = (all(x["expected_pass"] == x["row_pass"] == x["polynomial_pass"]
                  and x["eigenvalue_error"] < 1e-12 for x in cases)
              and frozen_metric_would_pass and actual_metric_rejects
              and derivative_error < 2e-7 and orientation_error < 1e-12
              and degenerate_rejected)
    return dict(schema="actual-metric-curvature-PSD-artificial-array-check-v1",
                artificial_inputs_only=True, research_geometry_evaluated=False,
                research_optimizer_called=False, row_order=list(ROW_NAMES),
                graph_jet_cases=cases, target_metric_false_acceptance_demonstrated=frozen_metric_would_pass,
                actual_metric_counterexample_rejected=actual_metric_rejects,
                complete_two_jet_directional_jacobian_error=derivative_error,
                ambient_reflection_swaps_two_PSD_gates_error=orientation_error,
                zero_area_rejected_before_row_acceptance=degenerate_rejected,
                helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), passed=passed)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    report = artificial_check()
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k != "graph_jet_cases"}, ensure_ascii=False))
    if not report["passed"]:
        raise SystemExit("artificial curvature interface check failed")


if __name__ == "__main__":
    main()
