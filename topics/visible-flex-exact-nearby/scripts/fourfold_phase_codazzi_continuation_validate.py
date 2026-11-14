#!/usr/bin/env python3
"""Directed continuous R126 validation of an exact finite BC candidate.

The candidate is not assumed to solve a projected or true PDE.  Complete
closed radial boxes, closed angular cells, the full affine parameter box,
and the true infinite target primitive are enclosed.  Success requires the
explicit nonlinear C0/C1 characteristic barriers, not numerical convergence.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import io
import json
from pathlib import Path
import time
import numpy as np
from flint import arb, acb, ctx

from fourfold_phase_codazzi_coefficients import CodazziCoefficientTarget
from fourfold_phase_newton_source_centered import CenteredPolynomial
from fourfold_phase_two_jet_newton_source import (
    Box, CBox, zeros, arb_box, square_box, real_interval,
    save, record, sha, box_abs_upper, range_record,
)
from fourfold_phase_beta_bulk_interval import exact_arb


def complex_box(values):
    return CBox(Box(np.asarray(values).real), Box(np.asarray(values).imag))


def positive_to_full(pos, grid):
    result = zeros((grid, 2))
    result[:len(pos.real.lo)] = pos
    indices = np.arange(1, len(pos.real.lo))
    result[(-indices) % grid] = CBox(pos.real[indices], -pos.imag[indices])
    return result


class ExactCandidate:
    def __init__(self, path, target):
        self.path = Path(path)
        with np.load(io.BytesIO(gzip.decompress(self.path.read_bytes())),
                     allow_pickle=False) as saved:
            self.times = [Fraction.from_float(float(x)) for x in saved["time_nodes"]]
            self.ends = saved["positive_endpoint_coefficients"].copy()
            self.corrections = saved["positive_dense_corrections"].copy()
            self.metadata = json.loads(str(saved["metadata"]))
        self.target = target
        self.degree = self.ends.shape[1]-1
        self.grid = target.product_grid
        if self.grid <= 2*self.degree:
            raise ValueError("candidate Fourier support reaches convolution boundary")
        if self.times[0] != 0 or any(b <= a for a, b in zip(self.times, self.times[1:])):
            raise ValueError("nonpositive candidate time partition")
        if list(map(str, self.times)) != self.metadata["time_nodes_exact_fractions"]:
            raise ValueError("candidate exact dyadic time metadata mismatch")
        for values in (self.ends, self.corrections):
            if not np.all(np.isfinite(values)) or np.any(values[..., 0, :].imag != 0):
                raise ValueError("nonfinite coefficients or nonreal mean")
        if not np.all(self.ends[0, :, 0] == 0):
            raise ValueError("initial candidate B must be exactly zero")
        self.frequencies = 4*np.asarray([
            j if j < self.grid//2 else j-self.grid for j in range(self.grid)
        ])
        self.pieces = len(self.times)-1

    def polynomials(self, piece, left, right):
        lo, hi = self.times[piece:piece+2]
        if not lo <= left <= right <= hi:
            raise ValueError("candidate box crosses a time-polynomial join")
        x = arb_box((real_interval(left, right)-exact_arb(lo))/exact_arb(hi-lo))
        L, R = complex_box(self.ends[piece]), complex_box(self.ends[piece+1])
        cc = [complex_box(v) for v in self.corrections[piece]]
        value, derivative = cc[5], zeros(cc[5].real.lo.shape)
        for j in range(4, -1, -1):
            factor, sign = (x, 1) if j % 2 == 0 else (1-x, -1)
            derivative = sign*value+derivative*factor
            value = cc[j]+value*factor
        # Keep the shared endpoint correlation.  Evaluating (1-x)L+xR
        # with two independent copies of a wide x box would lose even
        # the sign of an almost constant C field.
        field = L+(R-L)*x+value*x*(1-x)
        radial = (R-L+value*(1-2*x)+derivative*x*(1-x))/arb_box(exact_arb(hi-lo))
        full, rfull = positive_to_full(field, self.grid), positive_to_full(radial, self.grid)

        def angular_polynomial(array, component, order):
            coeff = array[:, component]
            for _ in range(order):
                coeff = coeff*CBox(0., Box(self.frequencies))
            return CenteredPolynomial(coeff, arb(0), self.degree,
                                      self.target.polynomial_fft)

        return {name: angular_polynomial(array, component, order)
                for array, derivative_name, orders in ((full, "", range(3)),
                                                       (rfull, "r", range(2)))
                for component, field_name in enumerate(("B", "C"))
                for order in orders
                for name in (field_name+derivative_name+"t"*order,)}


def maxabs(*values):
    return max((box_abs_upper(value) for value in values)).upper()

def angular_cells_taylor(polynomial, angles):
    """Closed real angular cells with local first/second Taylor terms.

    The finite midpoint polynomial is exact.  Its complete original field
    error is added only once; the cubic remainder uses its full physical
    Fourier norm and thus covers every mode of that polynomial.
    """
    if angles < polynomial.grid or angles & (angles-1):
        raise ValueError("angular grid must be a power of two above Fourier support")
    modes = np.asarray([j if j < polynomial.grid//2 else j-polynomial.grid
                        for j in range(polynomial.grid)])
    physical = 4*modes
    block = zeros((angles, 3))
    coefficient = polynomial.c
    for order in range(3):
        block[modes % angles, order] = coefficient
        coefficient = coefficient*CBox(0., Box(physical))
    samples = polynomial.fft.fft(block, inverse=True)*angles
    if not np.all((samples.imag.lo <= 0) & (samples.imag.hi >= 0)):
        raise ValueError("real Taylor angular samples lost their imaginary zero")
    width = arb.pi()/(4*angles)
    w = arb_box(width)
    d1 = Box(samples.real[:, 1].abs_upper())
    d2 = Box(samples.real[:, 2].abs_upper())
    error = (polynomial.error+width**3*polynomial.norm(3)/6).upper()
    fee = (d1*w+d2*w*w/2+arb_box(error)).hi
    return samples.real[:, 0]+Box(-fee, fee)


def piece_budget(candidate, target, piece, left, right, angles):
    coeff = target.coefficients(left, right)
    if not coeff["K"] < 0:
        raise ValueError("strict negative target gate unresolved")
    polynomials = candidate.polynomials(piece, left, right)
    values = {key: angular_cells_taylor(value, angles)
              for key, value in polynomials.items()}
    B, C, Bt, Ct, Btt, Ctt, Br, Cr, Brt, Crt = (
        values[name] for name in ("B", "C", "Bt", "Ct", "Btt", "Ctt",
                                 "Br", "Cr", "Brt", "Crt"))
    if not np.all(C.hi < 0):
        raise ValueError("candidate C negative denominator gate unresolved")
    K, k, gamma, beta = (arb_box(coeff[key]) for key in ("K", "k", "gamma", "beta"))
    C2 = square_box(C)
    V = K+square_box(B)
    A = V/C
    At = 2*B*Bt/C-V*Ct/C2
    Att = (2*(square_box(Bt)+B*Btt)/C-4*B*Bt*Ct/C2
           -V*Ctt/C2+2*V*square_box(Ct)/(C2*C))
    RB = Br-gamma*At+2*beta*B
    RC = Cr-gamma*Bt-beta*(A-C)
    RBt = Brt-gamma*Att+2*beta*Bt
    RCt = Crt-gamma*Btt-beta*(At-Ct)
    P, Q = (B+k)/C, (B-k)/C
    Pt, Qt = Bt/C-(B+k)*Ct/C2, Bt/C-(B-k)*Ct/C2
    Ptt = Btt/C-2*Bt*Ct/C2-(B+k)*Ctt/C2+2*(B+k)*square_box(Ct)/(C2*C)
    Qtt = Btt/C-2*Bt*Ct/C2-(B-k)*Ctt/C2+2*(B-k)*square_box(Ct)/(C2*C)
    RP, RQ = (RB-P*RC)/C, (RB-Q*RC)/C
    RPt = (RBt-Pt*RC-P*RCt)/C-(RB-P*RC)*Ct/C2
    RQt = (RBt-Qt*RC-Q*RCt)/C-(RB-Q*RC)*Ct/C2
    bounds = dict(
        Mhat=maxabs(P, Q), D1=maxabs(Pt, Qt), D2=maxabs(Ptt, Qtt),
        rho0=maxabs(RP, RQ), rho1=maxabs(RPt, RQt),
        BCrho0=maxabs(RB, RC), BCrho1=maxabs(RBt, RCt),
        gamma=coeff["gamma"].upper(), beta=abs(coeff["beta"]).upper(),
        kappa=abs(coeff["kappa"]).upper(),
        k_lower=coeff["k"].lower(),
        C_abs_lower=arb(float(np.min(-C.hi))),
        C_abs_upper=maxabs(C),
        candidate_gap=(2*coeff["k"].lower()/maxabs(C)).lower(),
    )
    return bounds, coeff, list(map(str, target.cell))


def initial_error(candidate, target, angles):
    coeff = target.coefficients(Fraction(0), Fraction(0))
    if not coeff["K"] < 0:
        raise ValueError("initial target is not rigorously negative")
    real = target.exact_initial_C_polynomials(1)
    reference = candidate.polynomials(0, Fraction(0), Fraction(0))
    c, ct = (angular_cells_taylor(p, angles) for p in real)
    chat, chatt = (angular_cells_taylor(reference[name], angles) for name in ("C", "Ct"))
    delta = angular_cells_taylor(reference["C"]-real[0], angles)
    deltat = angular_cells_taylor(reference["Ct"]-real[1], angles)
    if not np.all(c.hi < 0) or not np.all(chat.hi < 0):
        raise ValueError("initial C chart not enclosed")
    k = arb_box(coeff["k"])
    e0 = k*delta/(c*chat)
    e1 = k*(deltat/(c*chat)-delta*(ct*chat+c*chatt)/(square_box(c)*square_box(chat)))
    return dict(epsilon0=maxabs(e0), epsilon1=maxabs(e1),
                C_difference=maxabs(delta), C_theta_difference=maxabs(deltat),
                k=coeff["k"])


def complete_barrier(rows, initial, right):
    maxima = {key: max(row["raw"][key] for row in rows).upper()
              for key in ("Mhat", "D1", "D2", "rho0", "rho1", "gamma", "beta", "kappa")}
    gap = min(row["raw"]["candidate_gap"] for row in rows).lower()
    klower = min(row["raw"]["k_lower"] for row in rows).lower()
    tube = arb(1)/16
    M = (maxima["Mhat"]+tube).upper()
    J = (maxima["beta"]*(1+3*M*M)+2*maxima["kappa"]).upper()
    A0 = (maxima["gamma"]*maxima["D1"]+J).upper()
    A1 = (2*maxima["gamma"]*maxima["D1"]+J).upper()
    A10 = (maxima["gamma"]*maxima["D2"]+6*maxima["beta"]*M*maxima["D1"]).upper()
    T = exact_arb(right)
    eps0 = (2*initial["epsilon0"]+arb("1e-30")).upper()
    eps1 = (2*initial["epsilon1"]+arb("1e-30")).upper()
    result = dict(maxima={key: record(value) for key, value in maxima.items()},
                  coefficient_bounds={key: record(value) for key, value in
                                      dict(M=M, J0=J, A0=A0, A1=A1, A10=A10).items()},
                  tube=record(tube), candidate_gap_lower=record(gap),
                  target_k_lower=record(klower),
                  initial_barrier=[record(eps0), record(eps1)])
    gates = {"positive_k": bool(klower > 0),
             "C0_linear_barrier_denominator": bool(1-T*A0 > 0)}
    if not all(gates.values()):
        result.update(gates=gates, passed=False)
        return result
    Y0 = (2*(eps0+T*maxima["rho0"])/(1-T*A0)).upper()
    b = (1-T*A1).lower()
    aa = (T*maxima["gamma"]).upper()
    cc = (eps1+T*(A10*Y0+maxima["rho1"])).upper()
    gates.update(C0_stays_in_prescribed_tube=bool(Y0 < tube),
                 Riemann_denominator_stays_nonzero=bool(gap > 2*Y0),
                 C1_linear_margin=bool(b > 0),
                 C1_Riccati_discriminant=bool(b*b-4*aa*cc > 0))
    result.update(C0_final_barrier=record(Y0),
                  C1_quadratic={key: record(value) for key, value in
                                dict(a=aa, b=b, c=cc, discriminant=b*b-4*aa*cc).items()})
    if not all(gates.values()):
        result.update(gates=gates, passed=False)
        return result
    Y1 = (2*cc/b).upper()
    margin0 = Y0-eps0-T*(A0*Y0+maxima["rho0"])
    margin1 = Y1-eps1-T*(A1*Y1+maxima["gamma"]*Y1*Y1
                        +A10*Y0+maxima["rho1"])
    gates.update(strict_C0_differential_barrier=bool(margin0 > 0),
                 strict_C1_differential_barrier=bool(margin1 > 0))
    result.update(C1_final_barrier=record(Y1),
                  strict_barrier_margins=[record(margin0), record(margin1)],
                  gates=gates, passed=all(gates.values()))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate", type=Path, default=Path(
        "notes/2026-11-13-codazzi-dense-r0005-n1024-candidate.npz.gz"))
    parser.add_argument("--object", type=Path, default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"))
    parser.add_argument("--half-width", type=Fraction, default=Fraction(1, 10**9))
    parser.add_argument("--right", type=Fraction, default=Fraction(1, 200))
    parser.add_argument("--subdivide", type=int, default=1)
    parser.add_argument("--nodes", type=int, default=512)
    parser.add_argument("--angles", type=int, default=16384)
    parser.add_argument("--bits", type=int, default=192)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.subdivide < 1:
        raise ValueError("positive subdivision required")
    ctx.prec, ctx.cap = args.bits, 4
    started = time.monotonic()
    target = CodazziCoefficientTarget(args.object, args.half_width, args.nodes, args.angles)
    candidate = ExactCandidate(args.candidate, target)
    if candidate.metadata["object_sha256"] != sha(args.object):
        raise ValueError("candidate and true target object mismatch")
    if not 0 < args.right <= candidate.times[-1]:
        raise ValueError("requested interval outside complete candidate")
    initial = initial_error(candidate, target, args.angles)
    print({"progress": "actual complete initial error", "epsilon0": str(initial["epsilon0"]),
           "epsilon1": str(initial["epsilon1"]), "elapsed": time.monotonic()-started}, flush=True)
    report = dict(
        kind="actual_R126_continuous_Codazzi_Cauchy_validation",
        complete=False, continuation_certified=False, closed_surface_complete=False,
        exact_requested_interval=["0", str(args.right)],
        whole_affine_parameter_interval=True,
        parameter_half_width=str(args.half_width),
        exact_center_parameter=candidate.metadata["exact_center_parameter"],
        whole_real_angular_circle=True,
        source_sha256=sha(__file__), candidate_sha256=sha(args.candidate),
        candidate_metadata=candidate.metadata, object_sha256=sha(args.object),
        coefficient_provider_sha256=sha(Path(__file__).with_name("fourfold_phase_codazzi_coefficients.py")),
        bits=args.bits, primitive_nodes=args.nodes, angular_closed_cells=args.angles,
        initial_error={key: record(value) for key, value in initial.items()},
        rows=[], failure=None,
    )
    rows = []
    end = Fraction(0)
    try:
        for piece, (a, b) in enumerate(zip(candidate.times, candidate.times[1:])):
            if a >= args.right:
                break
            b = min(b, args.right)
            for part in range(args.subdivide):
                left = a+(b-a)*part/args.subdivide
                right = a+(b-a)*(part+1)/args.subdivide
                if left != end:
                    raise ValueError("gap or overlap in actual radial cover")
                bounds, coeff, germ = piece_budget(
                    candidate, target, piece, left, right, args.angles)
                row = dict(piece=piece, part=part, interval=[str(left), str(right)],
                           actual_scalar_germ=germ,
                           bounds={key: record(value) for key, value in bounds.items()},
                           true_target_coefficients={key: record(value) for key, value in coeff.items()})
                report["rows"].append(row)
                rows.append(dict(raw=bounds))
                end = right
                report["covered_interval"] = ["0", str(end)]
                report["wall_seconds"] = time.monotonic()-started
                save(args.out, report)
                print({"piece": piece, "part": part, "right": str(right),
                       "rho0": bounds["rho0"].str(8), "rho1": bounds["rho1"].str(8),
                       "D1": bounds["D1"].str(8), "D2": bounds["D2"].str(8),
                       "elapsed": report["wall_seconds"]}, flush=True)
        if end != args.right:
            raise ValueError("incomplete requested radial cover")
        report["barrier"] = complete_barrier(rows, initial, args.right)
        report["complete"] = True
        report["continuation_certified"] = report["barrier"]["passed"]
    except Exception as exc:
        report["failure"] = repr(exc)
    report["wall_seconds"] = time.monotonic()-started
    save(args.out, report)
    print({"complete": report["complete"],
           "continuation_certified": report["continuation_certified"],
           "failure": report["failure"], "out": str(args.out),
           "wall_seconds": report["wall_seconds"]}, flush=True)


if __name__ == "__main__":
    main()
