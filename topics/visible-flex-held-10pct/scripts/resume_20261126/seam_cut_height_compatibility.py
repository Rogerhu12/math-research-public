#!/usr/bin/env python3
"""Continuous cut audit from an original accepted packet.response.jets.

No tail solve, reparametrization, mean replacement, or full-H inference.
All saved numbers are exact binary64 constants. The target cut is the
already specified R=binary(.3), w=binary(.08), w_R=-7*w/R.
"""

import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
import math
from pathlib import Path
import sys
import time

from mpmath.ctx_iv import MPIntervalContext


BACKGROUND_KEYS = (
    "rCut", "wCut", "width", "curvatureBound", "orientation",
    "prefixR", "prefixEnd", "prefixReturnStart", "protectCell",
    "slopeCap", "capTransition", "calibrationSteps", "warpSteps",
    "cuspAwareQuadrature", "quadratureTolerance", "capMode",
    "valleyControls", "pulseCaps", "valleyCaps", "warpWeightLevels",
)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def fq(value):
    value = float(value)
    if not math.isfinite(value):
        raise ValueError("Nonfinite saved coefficient")
    return F.from_float(value)


def outward(value, direction):
    value = F(value)
    result = float(value)
    if not math.isfinite(result):
        raise ArithmeticError("The reported bound is not finite")
    if (direction < 0 and fq(result) > value) or (
        direction > 0 and fq(result) < value
    ):
        result = math.nextafter(result, -math.inf if direction < 0 else math.inf)
    return result


def dyadic(raw):
    sign, mantissa, exponent, bitcount = raw
    if bitcount < 0:
        raise ArithmeticError("Nonfinite interval endpoint")
    value = F((-1 if sign else 1) * mantissa)
    return value * (2 ** exponent) if exponent >= 0 else value / (2 ** (-exponent))


def ends(value):
    return tuple(dyadic(raw) for raw in value._mpi_)


def report_interval(lo, hi):
    lo, hi = F(lo), F(hi)
    return {
        "lower": outward(lo, -1),
        "upper": outward(hi, 1),
        "lower_exact": str(lo),
        "upper_exact": str(hi),
    }


def upper_report(value):
    value = F(value)
    return {"upper": outward(value, 1), "upper_exact": str(value)}


def lower_report(value):
    value = F(value)
    return {"lower": outward(value, -1), "lower_exact": str(value)}


def ivq(iv, value):
    value = F(value)
    return iv.mpf(value.numerator) / iv.mpf(value.denominator)


def padd(*polys):
    out = {}
    for poly in polys:
        for k, value in poly.items():
            out[k] = out.get(k, F(0)) + value
    return {k: value for k, value in out.items() if value}


def pscale(poly, scale):
    return {k: scale * value for k, value in poly.items() if scale * value}


def pmul(left, right):
    out = {}
    for j, value in left.items():
        for k, other in right.items():
            out[j + k] = out.get(j + k, F(0)) + value * other
    return {k: value for k, value in out.items() if value}


def cosine(coefficients, modes, constant=F(0)):
    out = {0: constant} if constant else {}
    for m, value in zip(modes, coefficients):
        if value:
            out[m] = out[-m] = value / 2
    return out


def darboux_laurent(height, slope, second, c, cr, modes, R, E, Ep):
    """Exact Laurent numerator; theta differentiation equals i*m."""
    z = cosine(height, modes)
    p = cosine(slope, modes, c)
    rr = cosine(second, modes, cr)
    v = {m: m * a for m, a in z.items()}
    ztt = {m: -m * m * a for m, a in z.items()}
    ptheta_no_i = {m: m * a for m, a in p.items() if m}
    AH = padd(rr, pscale(p, -Ep / (2 * E)))
    BH_no_i = padd(ptheta_no_i, pscale(v, -1 / R))
    CH = padd(ztt, pscale(p, R / E))
    det_h = padd(
        {0: E * R * R},
        pscale(pmul(v, v), E),
        pscale(pmul(p, p), -R * R),
    )
    Kg = Ep / (2 * R * E * E)
    numerator = padd(
        pmul(AH, CH),
        pmul(BH_no_i, BH_no_i),
        pscale(det_h, -Kg),
    )
    normalized = pscale(numerator, 1 / (E * R * R))
    return normalized, sum(map(abs, normalized.values()), F(0))


def load_packet(path, source_port, background_record):
    opener = gzip.open if str(path).endswith(".gz") else open
    with opener(path, "rt", encoding="utf-8") as stream:
        packet = json.load(stream)
    response = packet.get("response")
    if not isinstance(response, dict) or response.get("converged") is not True:
        raise ValueError("Require an original packet with response.converged == true")
    if response.get("failed"):
        raise ValueError("Original response carries a failure")
    jets = response.get("jets")
    if not isinstance(jets, dict):
        raise ValueError("Accepted response has no original response.jets")
    config = packet.get("config", {})
    if not isinstance(config, dict) or "solveTolerance" not in config:
        raise ValueError("Require original config.solveTolerance")
    residual, tolerance = fq(response["residual"]), fq(config["solveTolerance"])
    reference = json.loads(background_record.read_text())["config"]
    if not 0 <= residual <= tolerance <= fq(reference["solveTolerance"]):
        raise ValueError("Original residual/solveTolerance gate failed or was weakened")
    if tolerance <= 0:
        raise ValueError("Invalid solveTolerance")
    port = json.loads(source_port.read_text())
    for name in BACKGROUND_KEYS:
        if name not in config or name not in port["parameters"] or name not in reference:
            raise ValueError("Missing original background parameter: " + name)
        if config[name] != port["parameters"][name] or config[name] != reference[name]:
            raise ValueError("Changed specified true background parameter: " + name)
    if config.get("depth") != reference["depth"]:
        raise ValueError("Changed physical tail depth")
    if fq(config["rCut"]) != fq(.3) or fq(config["wCut"]) != fq(.08):
        raise ValueError("Configuration is not the specified true cut")
    cp = response.get("checkpoint", {}).get("parameters", {})
    spacing = config.get("spacing", cp.get("spacing"))
    count = config.get("modes", cp.get("modes"))
    if spacing is None or count is None:
        raise ValueError("Require source-defined config/checkpoint spacing and modes")
    if int(spacing) != spacing or int(count) != count:
        raise ValueError("Nonintegral Fourier dimensions")
    spacing, count = int(spacing), int(count)
    if spacing <= 0 or count <= 0:
        raise ValueError("Invalid Fourier dimensions")
    if cp.get("spacing", spacing) != spacing or cp.get("modes", count) != count:
        raise ValueError("Config/checkpoint Fourier dimensions disagree")
    arrays = []
    for name in ("height", "slope", "second"):
        row = jets.get(name)
        if not isinstance(row, list) or len(row) != count:
            raise ValueError("Require complete physical cosine coefficients: " + name)
        arrays.append(list(map(fq, row)))
    for name in ("meanSlope", "meanSecond", "radius", "backgroundSlope",
                 "backgroundSecond", "E", "Ep"):
        if name not in jets:
            raise ValueError("Incomplete accepted jets: " + name)
    for name in ("radius", "backgroundSlope", "backgroundSecond", "E", "Ep"):
        if fq(jets[name]) != fq(port["cut"][name]):
            raise ValueError("Accepted cut differs from the original source port: " + name)
    if fq(jets["radius"]) != fq(.3):
        raise ValueError("This audit is bound to the specified true cut binary(.3)")
    if port["modes"] != [spacing * j for j in range(1, count + 1)]:
        raise ValueError("Accepted Fourier dimensions differ from the original source port")
    return packet, response, jets, spacing, count, arrays


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--tail-response", type=Path, required=True)
    ap.add_argument("--source-port", type=Path, required=True)
    ap.add_argument("--background-record", type=Path, default=(
        Path(__file__).resolve().parents[2] / "notes/2026-11-20-m3-m24-warm050-execution.json"
    ))
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--quadrature", type=int, default=512)
    ap.add_argument("--digits", type=int, default=70)
    ap.add_argument("--strips", default="1/128,1/64,1/32,1/16,1/8,1/4")
    ap.add_argument("--branch-cells", type=int, default=128)
    ap.add_argument("--max-branch-cells", type=int, default=4096)
    a = ap.parse_args()
    if a.quadrature < 64 or a.digits < 40 or a.branch_cells < 16:
        raise ValueError("Insufficient requested audit precision")
    started = time.monotonic()
    packet, response, jets, spacing, count, arrays = load_packet(
        a.tail_response, a.source_port, a.background_record
    )
    height, slope, second = arrays
    modes = [spacing * (j + 1) for j in range(count)]
    c, cr = fq(jets["meanSlope"]), fq(jets["meanSecond"])
    R, w = fq(.3), fq(.08)
    wR = -7 * w / R
    E, Ep = 1 + w * w, 2 * w * wR
    vmax = sum((m * abs(h) for m, h in zip(modes, height)), F(0))
    pvar = sum(map(abs, slope), F(0))
    pmax = abs(c) + pvar
    Amodes = [(p - E * m * m * h / R) / w
              for m, h, p in zip(modes, height, slope)]
    Sl1 = 1 - (vmax / R) ** 2
    Dl1 = E * Sl1 - pmax * pmax
    Al1 = c / w - sum(map(abs, Amodes), F(0))
    branch_lower = [Sl1, Dl1, Al1]
    iv = MPIntervalContext()
    iv.dps = a.digits
    rI, eI, wI, cI = (ivq(iv, z) for z in (R, E, w, c))
    hI = [ivq(iv, z) for z in height]
    pI = [ivq(iv, z) for z in slope]
    branch_method = "exact coefficient l1"
    branch_cells = 0

    def fields(theta):
        p, v, vtheta = cI, iv.mpf(0), iv.mpf(0)
        for m, h, sp in zip(modes, hI, pI):
            co, sn = iv.cos(m * theta), iv.sin(m * theta)
            p += sp * co
            v -= m * h * sn
            vtheta -= m * m * h * co
        S = 1 - (v / rI) ** 2
        D = eI * S - p * p
        A = (p + eI * vtheta / rI) / wI
        return p, vtheta, S, D, A

    # Tighten only if the global l1 bound did not already certify the branches.
    if min(branch_lower) <= 0:
        cells = a.branch_cells
        while cells <= a.max_branch_cells:
            lows = [None, None, None]
            for j in range(cells):
                theta = 2 * iv.pi * iv.mpf([j, j + 1]) / cells
                values = fields(theta)[2:]
                for k, value in enumerate(values):
                    low = ends(value)[0]
                    lows[k] = low if lows[k] is None else min(lows[k], low)
            branch_lower = [max(x, y) for x, y in zip(branch_lower, lows)]
            branch_method = "exact l1 plus all-angle interval cells"
            branch_cells = cells
            if min(branch_lower) > 0:
                break
            cells *= 2
    branches = min(branch_lower) > 0
    polynomial, dar_l1 = darboux_laurent(
        height, slope, second, c, cr, modes, R, E, Ep
    )
    report = {
        "status": "accepted_cut_height_continuous_audit",
        "scope": "Only the saved accepted height two-jet at the true cut; no new tail solve or bridge identity.",
        "input_sha256": sha(a.tail_response),
        "source_port_sha256": sha(a.source_port),
        "background_record_sha256": sha(a.background_record),
        "audit_source_sha256": sha(__file__),
        "saved_source_sha256": packet.get("source_sha256"),
        "original_response_converged": True,
        "original_response_residual": response.get("residual"),
        "original_solveTolerance": packet["config"]["solveTolerance"],
        "original_residual_gate_passed": True,
        "specified_background_config_verified": True,
        "source_port_cut_identical": True,
        "spacing": spacing,
        "modes": count,
        "coefficient_convention": "Physical cos(spacing*j*theta), j=1..M; arrays omit mean; no sqrt2 factor.",
        "target_cut_exact": {"R": str(R), "w": str(w), "wR": str(wR),
                             "E": str(E), "Ep": str(Ep)},
        "saved_background": {k: jets.get(k) for k in
                             ("backgroundSlope", "backgroundSecond", "E", "Ep")},
        "saved_minus_true_cut_exact": {
            k: str(fq(jets[k]) - exact)
            for k, exact in (
                ("radius", R), ("backgroundSlope", w),
                ("backgroundSecond", wR), ("E", E), ("Ep", Ep)
            )
        },
        "saved_mean_exact": {"slope": str(c), "second": str(cr)},
        "branches": {
            "certified": branches,
            "method": branch_method,
            "cells": branch_cells,
            "S": lower_report(branch_lower[0]),
            "D": lower_report(branch_lower[1]),
            "A": lower_report(branch_lower[2]),
        },
        "normalized_Darboux": {
            "definition": "(det(Hess_g u)-K_g*det(g-du^2))/(E*R^2)",
            "method": "Exact rational Laurent multiplication; l1 coefficient norm.",
            "nonzero_coefficients": len(polynomial),
            "sup_abs": upper_report(dar_l1),
            "RR_error_to_same_one_jet_exact_Darboux_conditional": (
                upper_report(E * E * R * dar_l1 / (w * branch_lower[2]))
                if branch_lower[2] > 0 else None
            ),
        },
        "continuous_turning": None,
        "unique_turning_mean_bracket": None,
        "full_H_certified_here": False,
        "bridge_one_jet_equal_certified_here": False,
        "Cartesian_C2_seam_certified_here": False,
        "target_metric_modified": False,
        "saved_mean_modified": False,
    }
    if branches:
        strip_reports = []
        candidates = []
        for raw in a.strips.split(","):
            sigma = F(raw)
            if sigma <= 0:
                raise ValueError("Strip widths must be positive")
            pv, vv, vt = iv.mpf(0), iv.mpf(0), iv.mpf(0)
            for m, h, sp in zip(modes, height, slope):
                x = ivq(iv, sigma * m)
                ch = (iv.exp(x) + iv.exp(-x)) / 2
                pv += ivq(iv, abs(sp)) * ch
                vv += ivq(iv, m * abs(h)) * ch
                vt += ivq(iv, m * m * abs(h)) * ch
            pvb, vvb, vtb = (ends(z)[1] for z in (pv, vv, vt))
            Ss = 1 - (vvb / R) ** 2
            Ds = E - c * c - 2 * abs(c) * pvb - pvb * pvb - E * (vvb / R) ** 2
            row = {"sigma_exact": str(sigma), "S_lower": outward(Ss, -1),
                   "D_real_part_lower": outward(Ds, -1)}
            if Ss > 0 and Ds > 0:
                Momega = (
                    1 + ivq(iv, (abs(c) + pvb) * vtb / (R * Ss))
                ) / iv.sqrt(ivq(iv, Ds))
                Mbound = ends(Momega)[1]
                error = 2 * ivq(iv, Mbound) / (
                    iv.exp(ivq(iv, a.quadrature * sigma)) - 1
                )
                error_bound = ends(error)[1]
                row.update({"admissible": True,
                            "omega_abs_upper": outward(Mbound, 1),
                            "trapezoid_error_upper": outward(error_bound, 1)})
                candidates.append((error_bound, sigma))
            else:
                row["admissible"] = False
            strip_reports.append(row)
        if candidates:
            error, sigma = min(candidates)
            total = iv.mpf(0)
            for j in range(a.quadrature):
                theta = 2 * iv.pi * j / a.quadrature
                p, vtheta, S, D, _ = fields(theta)
                total += (1 + p * vtheta / (rI * S)) / iv.sqrt(D)
            lo, hi = ends(total / a.quadrature)
            lo, hi = lo - error, hi + error
            turning = {
                "method": "Interval equal-angle trapezoid plus analytic strip tail",
                "nodes": a.quadrature,
                "selected_strip_exact": str(sigma),
                "strip_tests": strip_reports,
                "normalized_I": report_interval(lo, hi),
            }
        else:
            # Honest fallback when coefficient disks are too conservative.
            # Interval integration covers the entire period, not sampled points.
            total = iv.mpf(0)
            cells = max(a.quadrature, branch_cells)
            for j in range(cells):
                theta = 2 * iv.pi * iv.mpf([j, j + 1]) / cells
                p, vtheta, S, D, _ = fields(theta)
                if ends(S)[0] <= 0 or ends(D)[0] <= 0:
                    raise ArithmeticError("Increase branch cells for interval turning integration")
                total += (1 + p * vtheta / (rI * S)) / iv.sqrt(D)
            lo, hi = ends(total / cells)
            turning = {
                "method": "All-cell interval integral; no analytic strip certified",
                "cells": cells,
                "strip_tests": strip_reports,
                "normalized_I": report_interval(lo, hi),
            }
        nu = max(abs(lo - 1), abs(hi - 1))
        turning["normalized_residual"] = upper_report(nu)
        report["continuous_turning"] = turning
        sqrtE_hi = ends(iv.sqrt(eI))[1]
        delta = 2 * E * sqrtE_hi * nu / (w * branch_lower[2])
        Ab = branch_lower[2] - delta / w
        Db = branch_lower[1] - 2 * pmax * delta - delta * delta
        bracket_ok = Ab >= branch_lower[2] / 2 and Db > 0
        report["unique_turning_mean_bracket"] = {
            "certified": bracket_ok,
            "center_meanSlope_exact": str(c),
            "radius": upper_report(delta),
            "meanSlope": report_interval(c - delta, c + delta),
            "bracket_A_lower": lower_report(Ab),
            "bracket_D_lower": lower_report(Db),
            "meaning": "Unique scalar continuous turning-one mean with unchanged height and nonzero slope coefficients; not a full tail solution.",
        }
    report["seconds"] = time.monotonic() - started
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": report["status"],
        "branches_certified": branches,
        "Darboux_upper": outward(dar_l1, 1),
        "continuous_turning": report["continuous_turning"],
        "scalar_mean_bracket_certified": (
            report["unique_turning_mean_bracket"]["certified"]
            if report["unique_turning_mean_bracket"] else False
        ),
        "seconds": report["seconds"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
