#!/usr/bin/env python3
"""Exact unit-tangent formulas and controlled Fourier primitives (R33).

The finite beta/gamma vectors define analytic, generally infinite-Fourier
functions. tangent_jets evaluates those functions, not a position
truncation. FourierPrimitive approximates their zero-mean primitives.
Its analytic tail/alias estimates are formulas for exact-arithmetic FFT
samples, evaluated here with ordinary floats: rounding is NOT certified.

All vectors returned by this module use the fixed Cartesian basis. Radial
derivatives mean derivatives of the supplied beta/gamma coefficient jets;
they do not differentiate an FFT interpolant in the radial variable.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
import math
from pathlib import Path
from typing import Mapping

import numpy as np


COEFFICIENT_KEYS = (
    "beta", "gamma", "beta_x", "gamma_x", "beta_xx", "gamma_xx"
)


def coefficient_jets(beta, gamma=(), beta_x=(), gamma_x=(),
                     beta_xx=(), gamma_xx=()):
    """Pad six finite real vectors to one common angular cutoff."""
    raw = dict(zip(COEFFICIENT_KEYS,
                   (beta, gamma, beta_x, gamma_x, beta_xx, gamma_xx)))
    size = max((np.asarray(v).size for v in raw.values()), default=0)
    result = {}
    for key, value in raw.items():
        vector = np.asarray(value, dtype=float).reshape(-1)
        if not np.all(np.isfinite(vector)):
            raise ValueError(f"{key} must contain finite real numbers")
        result[key] = np.pad(vector, (0, size - vector.size))
    return result


def tangent_jets(theta, beta, gamma=(), beta_x=(), gamma_x=(),
                 beta_xx=(), gamma_xx=()):
    """Return T, T_x, T_xx, T_theta, with the exact R33 angular formula.

    The output shape is theta.shape + (3,). Other entries contain the
    angle fields B and psi and their jets, useful when inspecting a chart.
    """
    coefficients = coefficient_jets(
        beta, gamma, beta_x, gamma_x, beta_xx, gamma_xx)
    theta = np.asarray(theta, dtype=float)
    frequency = 4 * np.arange(1, len(coefficients["beta"]) + 1)
    sine = np.sin(theta[..., None] * frequency)
    cosine = np.cos(theta[..., None] * frequency)
    fields = {key: sine @ value for key, value in coefficients.items()}
    B, psi = fields["beta"], fields["gamma"]
    bx, px = fields["beta_x"], fields["gamma_x"]
    bxx, pxx = fields["beta_xx"], fields["gamma_xx"]
    bt = cosine @ (frequency * coefficients["beta"])
    pt = cosine @ (frequency * coefficients["gamma"])
    phi = theta + np.pi / 2 + B
    cp, sp, cf, sf = np.cos(psi), np.sin(psi), np.cos(phi), np.sin(phi)
    tangent = np.stack((cp * cf, cp * sf, sp), axis=-1)
    ephi = np.stack((-sf, cf, np.zeros_like(phi)), axis=-1)
    epsi = np.stack((-sp * cf, -sp * sf, cp), axis=-1)
    tangent_x = (cp * bx)[..., None] * ephi + px[..., None] * epsi
    tangent_xx = (
        (cp * bxx - 2 * sp * bx * px)[..., None] * ephi
        + (pxx + sp * cp * bx**2)[..., None] * epsi
        - (cp**2 * bx**2 + px**2)[..., None] * tangent
    )
    tangent_theta = (
        (cp * (1 + bt))[..., None] * ephi + pt[..., None] * epsi
    )
    return {
        "T": tangent, "T_x": tangent_x, "T_xx": tangent_xx,
        "T_theta": tangent_theta,
        "B": B, "psi": psi, "B_x": bx, "psi_x": px,
        "B_xx": bxx, "psi_xx": pxx,
        "B_theta": bt, "psi_theta": pt,
    }


def strip_bounds(sigma, **coefficient_data):
    """Upper bounds for complex vector norms on |Im theta|<=sigma.

    We bound the sum of component absolute values, dominating the Euclidean
    norm. The bound applies to the full infinite Fourier fields.
    """
    if not math.isfinite(sigma) or sigma <= 0:
        raise ValueError("sigma must be finite and positive")
    coefficients = coefficient_jets(**coefficient_data)
    frequency = 4 * np.arange(1, len(coefficients["beta"]) + 1)
    weights = np.cosh(frequency * sigma)
    size = {key: float(np.abs(value) @ weights)
            for key, value in coefficients.items()}
    b, p = size["beta"], size["gamma"]
    bx, px = size["beta_x"], size["gamma_x"]
    bxx, pxx = size["beta_xx"], size["gamma_xx"]
    ep = math.exp(p)
    horizontal = 2 * math.exp(sigma + b)
    tangent = ep * (horizontal + 1)
    tangent_x = ep * horizontal * bx + tangent * px
    tangent_xx = (
        ep * horizontal * (bxx + 2 * bx * px)
        + tangent * (pxx + 2 * ep**2 * bx**2 + px**2)
    )
    bt = float((frequency * np.abs(coefficients["beta"])) @ weights)
    pt = float((frequency * np.abs(coefficients["gamma"])) @ weights)
    tangent_theta = ep * horizontal * (1 + bt) + tangent * pt
    answer = {"T": tangent, "T_x": tangent_x, "T_xx": tangent_xx,
              "T_theta": tangent_theta}
    if not all(math.isfinite(v) for v in answer.values()):
        raise ValueError("strip bound overflow; choose a narrower strip")
    return {"sigma": sigma, "bounds": answer, "angle_bounds": size}


def primitive_error_bounds(bound, sigma, nodes, keep):
    """Tail + alias bounds for angular derivative orders 0, 1, 2 of P T.

    Bound is one vector-valued analytic strip bound. The Fourier mean is
    set to its true value zero. Bounds omit all floating point rounding.
    """
    if not (0 <= keep < nodes / 2):
        raise ValueError("require 0 <= keep < nodes/2")
    q = math.exp(-sigma)
    denominator = -math.expm1(-sigma)
    qnext = math.exp(-sigma * (keep + 1))
    tails = np.array((
        2 * bound * qnext / ((keep + 1) * denominator),
        2 * bound * qnext / denominator,
        2 * bound * qnext * (
            (keep + 1) / denominator + q / denominator**2),
    ))
    n = np.arange(1, keep + 1, dtype=float)
    alias_coefficient = (
        4 * bound * np.exp(-sigma * (nodes - n))
        / (-math.expm1(-sigma * nodes))
    )
    aliases = np.array([
        float(np.sum(alias_coefficient * n**(order - 1)))
        for order in range(3)
    ])
    return {
        "tail": tails.tolist(), "alias": aliases.tolist(),
        "total": (tails + aliases).tolist(),
        "derivative_orders": [0, 1, 2],
        "roundoff_included": False,
    }


@dataclass
class FourierPrimitive:
    """Finite primitive approximant plus explicit infinite-function budgets."""

    coefficient_data: Mapping[str, np.ndarray]
    nodes: int
    keep: int
    sigma: float
    frequencies: np.ndarray
    coefficients: Mapping[str, np.ndarray]
    budgets: Mapping[str, dict]
    strip: Mapping[str, object]
    discarded_sample_means: Mapping[str, list]

    def evaluate(self, theta, angular_derivative=0):
        """Approximate P T, P T_x, P T_xx or their angular derivatives.

        The derivatives here belong to the finite primitive approximant.
        For the exact infinite-function angular jets use exact_jets.
        """
        if angular_derivative not in (0, 1, 2):
            raise ValueError("implemented angular derivative orders are 0,1,2")
        theta = np.asarray(theta, dtype=float)
        wave = np.exp(1j * theta[..., None] * self.frequencies)
        multiplier = (1j * self.frequencies)**angular_derivative
        return {
            key: np.real(wave @ (value * multiplier[:, None]))
            for key, value in self.coefficients.items()
        }

    def exact_jets(self, theta):
        return tangent_jets(theta, **self.coefficient_data)

    def summary(self):
        return {
            "nodes": self.nodes, "keep": self.keep, "sigma": self.sigma,
            "strip": self.strip, "primitive_error_bounds": self.budgets,
            "discarded_sample_means": self.discarded_sample_means,
            "limitations": [
                "finite FFT primitives approximate infinite analytic fields",
                "budgets exclude sample and floating point rounding errors",
                "no radial metric equations or cap conditions are solved",
            ],
        }


def fourier_primitive(beta, gamma=(), beta_x=(), gamma_x=(),
                      beta_xx=(), gamma_xx=(), *,
                      nodes=512, keep=192, sigma=0.25):
    """Build controlled FFT approximants for three radial primitive jets."""
    if nodes < 8 or nodes % 4 or not 0 <= keep < nodes / 2:
        raise ValueError("nodes must be a multiple of 4 and 0<=keep<nodes/2")
    data = coefficient_jets(beta, gamma, beta_x, gamma_x, beta_xx, gamma_xx)
    theta = 2 * np.pi * np.arange(nodes) / nodes
    samples = tangent_jets(theta, **data)
    frequencies = np.r_[np.arange(-keep, 0), np.arange(1, keep + 1)]
    strip = strip_bounds(sigma, **data)
    coefficients, budgets, means = {}, {}, {}
    for key in ("T", "T_x", "T_xx"):
        fft = np.fft.fft(samples[key], axis=0) / nodes
        coefficients[key] = (
            fft[frequencies % nodes] / (1j * frequencies[:, None])
        )
        means[key] = np.real(fft[0]).tolist()
        budgets[key] = primitive_error_bounds(
            strip["bounds"][key], sigma, nodes, keep)
    return FourierPrimitive(data, nodes, keep, sigma, frequencies,
                            coefficients, budgets, strip, means)


def cylindrical_primitive(radial_sine, angular_cosine, vertical_sine,
                           frequencies):
    """Exact algebra for a finite cylindrical Fourier field.

    Input: A_m sin(m theta) e_r + B_m cos(m theta) e_theta
           + C_m sin(m theta) e_z.
    Output: U_m cos(m theta) e_r + V_m sin(m theta) e_theta
            + W_m cos(m theta) e_z.
    All m must be 0 or >=2. In the fourfold class m=4j.
    """
    A, B, C, m = np.broadcast_arrays(
        np.asarray(radial_sine, dtype=float),
        np.asarray(angular_cosine, dtype=float),
        np.asarray(vertical_sine, dtype=float),
        np.asarray(frequencies, dtype=int),
    )
    if np.any(m < 0) or np.any(m == 1):
        raise ValueError("cylindrical formula requires m=0 or m>=2")
    U = np.zeros_like(A)
    V = np.zeros_like(A)
    W = np.zeros_like(A)
    nonzero = m != 0
    U[nonzero] = -(m[nonzero] * A[nonzero] + B[nonzero]) / (
        m[nonzero]**2 - 1)
    V[nonzero] = (A[nonzero] + m[nonzero] * B[nonzero]) / (
        m[nonzero]**2 - 1)
    W[nonzero] = -C[nonzero] / m[nonzero]
    U[~nonzero] = B[~nonzero]
    return U, V, W


def refinement_diagnostic(primitive, sample_count=257):
    """Float check; does not replace the analytic budgets."""
    fine = fourier_primitive(
        **primitive.coefficient_data, nodes=2 * primitive.nodes,
        keep=min(2 * primitive.keep + 1, primitive.nodes - 1),
        sigma=primitive.sigma)
    theta = 2 * np.pi * (
        np.arange(sample_count) + 0.3141592653589793) / sample_count
    result = {}
    for order in range(3):
        coarse_values = primitive.evaluate(theta, order)
        fine_values = fine.evaluate(theta, order)
        result[str(order)] = {
            key: float(np.max(np.linalg.norm(
                coarse_values[key] - fine_values[key], axis=-1)))
            for key in coarse_values
        }
    exact = primitive.exact_jets(theta)
    first = primitive.evaluate(theta, 1)
    second = primitive.evaluate(theta, 2)
    result["exact_first_derivative_mismatch"] = {
        key: float(np.max(np.linalg.norm(first[key] - exact[key], axis=-1)))
        for key in ("T", "T_x", "T_xx")
    }
    result["exact_second_derivative_mismatch_T"] = float(
        np.max(np.linalg.norm(second["T"] - exact["T_theta"], axis=-1)))
    return result


def self_check():
    """Meaningful formula checks with independent finite differences."""
    data = coefficient_jets(
        [.19, .007], [.02, -.003], [.04, .001], [-.02, .002],
        [.015, -.001], [.03, -.004])
    theta = np.linspace(.0123, 2 * np.pi + .0123, 193, endpoint=False)
    jets = tangent_jets(theta, **data)
    step = 2e-4
    shifted = []
    for sign in (-1, 1):
        delta = sign * step
        shifted.append(tangent_jets(
            theta,
            data["beta"] + delta * data["beta_x"]
            + delta**2 / 2 * data["beta_xx"],
            data["gamma"] + delta * data["gamma_x"]
            + delta**2 / 2 * data["gamma_xx"])["T"])
    first = (shifted[1] - shifted[0]) / (2 * step)
    second = (shifted[1] - 2 * jets["T"] + shifted[0]) / step**2
    angular_step = 1e-6
    angular = (
        tangent_jets(theta + angular_step, **data)["T"]
        - tangent_jets(theta - angular_step, **data)["T"]
    ) / (2 * angular_step)
    formula_errors = {
        "unit_length": float(np.max(np.abs(np.linalg.norm(jets["T"], axis=-1)-1))),
        "radial_first": float(np.max(np.linalg.norm(first-jets["T_x"], axis=-1))),
        "radial_second": float(np.max(np.linalg.norm(second-jets["T_xx"], axis=-1))),
        "angular_first": float(np.max(np.linalg.norm(angular-jets["T_theta"], axis=-1))),
    }
    if formula_errors["unit_length"] > 1e-14:
        raise AssertionError(formula_errors)
    if formula_errors["radial_first"] > 1e-7:
        raise AssertionError(formula_errors)
    if formula_errors["radial_second"] > 5e-7:
        raise AssertionError(formula_errors)
    if formula_errors["angular_first"] > 1e-7:
        raise AssertionError(formula_errors)
    primitive = fourier_primitive(**data, nodes=256, keep=96, sigma=.25)
    return {"formula_errors": formula_errors,
            "primitive": primitive.summary(),
            "refinement": refinement_diagnostic(primitive)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-check", action="store_true")
    parser.add_argument("--beta", nargs="*", type=float, default=[.227])
    parser.add_argument("--gamma", nargs="*", type=float, default=[])
    parser.add_argument("--nodes", type=int, default=512)
    parser.add_argument("--keep", type=int, default=192)
    parser.add_argument("--sigma", type=float, default=.25)
    parser.add_argument("--out")
    args = parser.parse_args()
    if args.self_check:
        result = self_check()
    else:
        primitive = fourier_primitive(
            args.beta, args.gamma, nodes=args.nodes,
            keep=args.keep, sigma=args.sigma)
        result = {"primitive": primitive.summary(),
                  "refinement": refinement_diagnostic(primitive)}
    payload = json.dumps(result, indent=2)
    if args.out:
        Path(args.out).write_text(payload + "\n")
    print(payload)


if __name__ == "__main__":
    main()
