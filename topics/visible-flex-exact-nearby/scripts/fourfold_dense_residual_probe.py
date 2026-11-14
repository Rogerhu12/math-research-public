#!/usr/bin/env python3
"""Floating e0/e1 diagnostics for saved exact-affine dense references.

Analytic differentiation of the saved polynomial is compared with freshly
evaluated principal fields. These are samples and quadrature estimates, not
continuous interval residuals, ODE error bounds, or a true-flow certificate.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import time

import numpy as np
from numpy.polynomial.legendre import leggauss

from fourfold_phase_exact_affine_nodes import load_npz, ExactAffineMap
from fourfold_phase_symmetric_geometry import load_exact_object


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_reference(path):
    if not str(path).endswith(".trace.json"):
        return load_npz(path)
    manifest = json.loads(Path(path).read_text())
    pieces = []
    for reference in manifest["traces"]:
        source = Path(reference["path"])
        if digest(source) != reference["sha256"]:
            raise ValueError("trace chunk SHA mismatch")
        pieces.append(load_npz(source))
    if len(pieces) == 1:
        return pieces[0]
    result = dict(pieces[0])
    for key in ("dense_t_old", "dense_h", "dense_y_old", "dense_F"):
        result[key] = np.concatenate([piece[key] for piece in pieces])
    for left, right in zip(pieces[:-1], pieces[1:]):
        if (left["accepted_tau"][-1] != right["accepted_tau"][0]
            or not np.array_equal(left["accepted_state"][-1],right["accepted_state"][0])):
            raise ValueError("trace chunks do not share exactly one endpoint state")
    for key in ("accepted_tau", "accepted_state"):
        result[key] = np.concatenate([piece[key] if index==0 else piece[key][1:]
                                     for index,piece in enumerate(pieces)])
    result["initial_angles"] = np.asarray(manifest["initial_angles"])
    return result


def dense_value_and_derivative(yold, F, z, h):
    value, derivative = np.zeros_like(yold), np.zeros_like(yold)
    for index, coefficient in enumerate(F[::-1]):
        added = value+coefficient
        factor, slope = (z, 1.) if index % 2 == 0 else (1-z, -1.)
        derivative = derivative*factor+added*slope
        value = added*factor
    return value+yold, derivative/h


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--object", type=Path, required=True)
    parser.add_argument("--root-certificate", type=Path, required=True)
    parser.add_argument("--trace", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--quadrature-order", type=int, default=8)
    parser.add_argument("--with-parameter", action="store_true")
    parser.add_argument("--maximum-segments", type=int)
    args = parser.parse_args()
    if args.quadrature_order < 2:
        raise ValueError("quadrature order must be at least 2")
    started = time.monotonic()
    arrays = load_reference(args.trace)
    metadata = json.loads(str(arrays["metadata"]))
    identity = metadata["identity"]
    if identity["source_sha256"] != digest(args.object) or identity["root_certificate_sha256"] != digest(args.root_certificate):
        raise ValueError("trace belongs to another object or root reference")
    geometry, _ = load_exact_object(args.object, identity["quarter_nodes"])
    if identity["geometry_source_sha256"] != digest(Path(__file__).with_name("fourfold_phase_symmetric_geometry.py")):
        raise ValueError("geometry evaluator changed from the one that generated this trace")
    root_data = json.loads(args.root_certificate.read_text())
    mapper = ExactAffineMap(geometry, root_data["root_center"], identity)
    sign = float(identity["sign"])
    gauss, weights = leggauss(args.quadrature_order)
    nodes = np.r_[0., (gauss+1)/2, 1.]
    weights = np.r_[0., weights/2, 0.]
    count = len(arrays["dense_h"])
    if args.maximum_segments is not None:
        count = min(count, args.maximum_segments)
    rays = len(arrays["initial_angles"])
    integrals = np.zeros((3 if args.with_parameter else 2, rays))
    global_max = np.zeros_like(integrals)
    rows = []
    for segment in range(count):
        left, right = arrays["accepted_tau"][segment:segment+2]
        h = arrays["dense_h"][segment]
        told = arrays["dense_t_old"][segment]
        per_max = np.zeros_like(integrals)
        per_integral = np.zeros_like(integrals)
        weighted_max = 0.
        worst = None
        for node, weight in zip(nodes, weights):
            tau = float(left+(right-left)*node)
            z = (tau-told)/h
            state, derivative = dense_value_and_derivative(
                arrays["dense_y_old"][segment], arrays["dense_F"][segment], z, h)
            theta = state[0]
            radial = mapper.root*np.sin(tau)
            sqk, cosine = mapper.ksquare(tau, radial)
            raw = geometry.principal_quantities(np.full(rays, radial), theta, args.with_parameter)
            m, n, G = (raw[key] for key in ("m", "n", "G"))
            mt, nt, Gt = (raw[key] for key in ("m_theta", "n_theta", "G_theta"))
            b, w = -m/n, G/n
            bt, wt = -mt/n+m*nt/n**2, Gt/n-G*nt/n**2
            factor = mapper.root*cosine
            field = factor*(b+sign*w*sqk)
            field_theta = factor*(bt+sign*wt*sqk)
            e0 = derivative[0]-field
            e1 = derivative[1]-field_theta
            residuals = [e0, e1]
            q = np.exp(state[1])
            weighted = abs(e0)/q
            index = int(np.argmax(weighted))
            if weighted[index] > weighted_max:
                weighted_max = float(weighted[index])
                worst = dict(tau=tau, radial_x=float(radial), local_ray=index,
                             theta=float(theta[index]), residual_theta=float(e0[index]),
                             residual_logJ=float(e1[index]), reference_q=float(q[index]))
            if args.with_parameter:
                qroot = sqk/cosine if cosine else np.sqrt(mapper.endpoint_qbar)
                mp, np_, Gp = (raw[key] for key in ("m_parameter", "n_parameter", "G_parameter"))
                bp, wp = -mp/n+m*np_/n**2, Gp/n-G*np_/n**2
                target = geometry.radial_target_metric([radial], with_variations=True)
                kp = float(target["minus_K_columns"][0, 0])
                forcing = (factor*bp+sign*mapper.root*cosine*cosine*qroot*wp
                           +sign*mapper.root*w*kp/(2*qroot))
                residuals.append(derivative[2]-field_theta*state[2]-forcing)
            absolute = abs(np.stack(residuals))
            per_max = np.maximum(per_max, absolute)
            integrand = absolute.copy()
            integrand[0] /= q
            if args.with_parameter:
                integrand[2] /= q
            per_integral += abs(right-left)*weight*integrand
        integrals += per_integral
        global_max = np.maximum(global_max, per_max)
        rows.append(dict(segment=segment, tau_interval=[float(left), float(right)],
                         sampled_component_max=per_max.max(axis=1).tolist(),
                         sampled_weighted_e0_max=weighted_max,
                         absolute_integral_quadrature_estimate_max=per_integral.max(axis=1).tolist(),
                         worst_weighted_e0_sample=worst))
        if segment and segment % 40 == 0:
            print(json.dumps(dict(progress="floating dense residual probe", completed_segments=segment,
                                  elapsed_seconds=time.monotonic()-started)), flush=True)
    report = dict(kind="floating_dense_reference_residual_samples_not_a_certificate",
                  source_sha256=digest(Path(__file__)), trace_sha256=digest(args.trace),
                  object_sha256=digest(args.object), root_certificate_sha256=digest(args.root_certificate),
                  geometry_source_sha256=identity["geometry_source_sha256"],
                  trace_identity=identity, evaluated_segments=count, total_saved_segments=len(arrays["dense_h"]),
                  rays=rays, quadrature_order=args.quadrature_order,
                  parameter_residual_included=args.with_parameter,
                  residual_definitions=["theta_tau-f", "L_tau-f_theta"]+
                    (["z_tau-f_theta*z-fixed_x_parameter_forcing"] if args.with_parameter else []),
                  integral_weights=["1/exp(L)", "1"]+(["1/exp(L)"] if args.with_parameter else []),
                  sampled_component_max=global_max.max(axis=1).tolist(),
                  sampled_weighted_e0_max=max(row["sampled_weighted_e0_max"] for row in rows),
                  absolute_integral_quadrature_estimate_max=integrals.max(axis=1).tolist(),
                  absolute_integral_quadrature_estimates_per_ray=integrals.tolist(),
                  worst_segments_by_sampled_weighted_e0=sorted(rows,key=lambda row:row["sampled_weighted_e0_max"],reverse=True)[:12],
                  segments=rows,
                  limitations=["ordinary floating samples and finite Gauss quadrature, not upper bounds",
                    "field evaluation has unpaid infinite primitive, trig/FFT and radial quotient errors",
                    "no continuous time/angle/parameter or complex-tube enclosure",
                    "dense endpoint jumps and exact initial H errors must be added separately",
                    "reference q is not the true Jacobian; no ODE or KAM conclusion"])
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+"\n")
    print(json.dumps({key:report[key] for key in ("evaluated_segments", "sampled_component_max",
        "sampled_weighted_e0_max", "absolute_integral_quadrature_estimate_max")}), flush=True)


if __name__ == "__main__":
    main()
