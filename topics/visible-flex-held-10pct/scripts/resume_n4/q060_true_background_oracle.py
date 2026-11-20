#!/usr/bin/env python3
"""True-integral interval oracle for the frozen first-valley-4.625 background.

This module uses the exact mathematical definition of R58, with the saved
binary calibration roots and the unique true-integral cut normalization.
It is not a certificate for the JS quadrature function, a new tail solve,
or a certificate for a nonrotating finite shooting state.  Source x is kept
as a locator; the surface's C2 radial coordinate is physical radius R.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
import math
from pathlib import Path
from types import ModuleType, SimpleNamespace
import time


KERNEL_SHA256 = "b7a8dc501dc3dbbe4ccb14d6b4ea2b4b85849d14b9551a94f5c23798d7985806"
DEFINITION_SHA256 = "e764e2cc370f0b7a8a55324f2744702017c16690195f45db92ca66b9781bae56"


def file_sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical_sha256(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                     allow_nan=False).encode()).hexdigest()


def rational(value):
    """A float means its exact binary value; a string means an exact rational."""
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError("finite endpoint required")
        return Q.from_float(value)
    return Q(value)


def mpf_fraction(value):
    sign, man, exponent, _ = value._mpf_
    return (-1 if sign else 1) * Q(man) * Q(2) ** exponent


class Q060TrueBackgroundOracle:
    """Return outward ranges of true primitives and physical-radius jets.

    All intervals returned by public methods belong to this object's private
    mpmath interval context.  ``bounds`` converts one to JSON-safe bounds.
    The normalization certificate is a previously executed R58 integral
    proof, not a freely selected interval parameter.  A narrower certificate
    of the same definition may be supplied without changing the target g.
    """

    def __init__(self, constants, normalization_certificate, *, kernel=None,
                 coefficient_tolerance="1e-14", variation_tolerance="1e-21",
                 digits=60, max_depth=64):
        self.constants_path = Path(constants)
        self.normalization_path = Path(normalization_certificate)
        self.kernel_path = Path(kernel) if kernel else Path(__file__).with_name(
            "certify_q060_background_integrals_tight.py")
        data = json.loads(self.constants_path.read_text())
        norm = json.loads(self.normalization_path.read_text())
        self.definition = {key: data[key] for key in
                           ("parameters", "cells", "checkpoint_sha256", "factory_sha256")}
        if canonical_sha256(self.definition) != DEFINITION_SHA256:
            raise ValueError("This oracle is bound to the recorded 4.625 definition.")
        if file_sha256(self.kernel_path) != KERNEL_SHA256:
            raise ValueError("The proved integral kernel has changed.")
        if norm["source_sha256"] != KERNEL_SHA256 or norm["input_sha256"] != file_sha256(self.constants_path):
            raise ValueError("Normalization proof and true-integrand constants differ.")
        if not 60 <= digits <= 200:
            raise ValueError("Use 60 through 200 interval digits.")
        if not 20 <= max_depth <= 128:
            raise ValueError("Unsupported adaptive depth.")
        self.tolerance = rational(coefficient_tolerance)
        self.variation_tolerance = rational(variation_tolerance)
        if min(self.tolerance, self.variation_tolerance) <= 0:
            raise ValueError("Positive integration tolerances required.")
        self.max_depth = max_depth

        # Reuse the already proved formulas, without its CLI or complete-tail
        # execution.  Independent contexts avoid changing another audit's
        # precision.  The original source bytes are checked before adaptation.
        source = self.kernel_path.read_text().split("\nstarted=time.monotonic()\n")[0]
        a = source.index("p=argparse.ArgumentParser()")
        b = source.index("args=p.parse_args()") + len("args=p.parse_args()")
        source = source[:a] + "args=_oracle_arguments" + source[b:]
        source = source.replace("mp.mp.dps=90\niv=mp.iv\niv.dps=60",
                                "mp=mp.mp.clone()\nmp.dps=_oracle_digits+30\n"
                                "from mpmath.ctx_iv import MPIntervalContext\n"
                                "iv=MPIntervalContext()\niv.dps=_oracle_digits")
        module = ModuleType("_q060_true_background_kernel")
        module.__dict__.update(__file__=str(self.kernel_path), _oracle_digits=digits,
                               _oracle_arguments=SimpleNamespace(
                                   input=self.constants_path, cells=32,
                                   out=Path("/dev/null"), max_depth=max_depth))
        exec(compile(source, str(self.kernel_path), "exec"), module.__dict__)
        self.k = module
        self.iv, self.mp = module.iv, module.mp
        self.lo, self.hi = module.lo, module.hi
        self.zero, self.one = module.Z, module.ONE
        self.constants, self.normalization = data, norm
        self.alpha = self._stored_bound(norm["exact_normalization"])
        if self.lo(self.alpha) <= 0:
            raise ValueError("Positive true normalization was not proved.")
        self.integrals_complete = {name: self._stored_bound(value)
                                   for name, value in norm["complete_integrals"].items()}
        self.radius_deep = module.source_radius(160)
        self._pieces = {}
        self._integrals = {}
        self._outward_sums = [tuple([self.zero] * 4)]
        self.evaluations = 0
        self.provenance = {
            "definition_sha256": DEFINITION_SHA256,
            "constants_sha256": file_sha256(self.constants_path),
            "normalization_certificate_sha256": file_sha256(self.normalization_path),
            "kernel_sha256": KERNEL_SHA256,
            "oracle_sha256": file_sha256(__file__),
            "interval_digits": digits,
            "coefficient_tolerance": str(self.tolerance),
            "variation_tolerance": str(self.variation_tolerance),
            "normalization_definition": "(rCut - true_r160 - integral_A) / integral_B",
            "calibration_roots": "The 160 recorded binary calibrationAlpha values, unchanged.",
            "coordinate": "Original cell/segment/x locator; C2 surface jets use physical R=r(x).",
            "mean_contract": "Only the rotational background height relative to its cut; no nonrotating mean is supplied or reset.",
            "finite_oracle_transfer_certified": False,
        }

    def qi(self, value):
        value = rational(value)
        return self.iv.mpf(value.numerator) / value.denominator

    def interval(self, left, right):
        left, right = rational(left), rational(right)
        if left > right:
            raise ValueError("Reversed interval")
        return self.k.I(self.lo(self.qi(left)), self.hi(self.qi(right)))

    def _stored_bound(self, row):
        return self.interval(Q(row["lower_exact"]), Q(row["upper_exact"]))

    def bounds(self, value):
        left, right = mpf_fraction(self.lo(value)), mpf_fraction(self.hi(value))
        low, high = float(left), float(right)
        if Q.from_float(low) > left:
            low = math.nextafter(low, -math.inf)
        if Q.from_float(high) < right:
            high = math.nextafter(high, math.inf)
        return {"lower": low, "upper": high,
                "lower_exact": str(left), "upper_exact": str(right)}

    def json_value(self, value):
        if hasattr(value, "_mpi_"):
            return self.bounds(value)
        if isinstance(value, dict):
            return {k: self.json_value(v) for k, v in value.items()}
        if isinstance(value, (tuple, list)):
            return [self.json_value(v) for v in value]
        if isinstance(value, Q):
            return str(value)
        return value

    def _intersection(self, a, b):
        return self.k.I(max(self.lo(a), self.lo(b)), min(self.hi(a), self.hi(b)))

    def piece(self, cell, segment):
        cell, segment = int(cell), int(segment)
        if not (0 <= cell < 160 and 0 <= segment < 9):
            raise ValueError("Only the 160 explicitly modified cells are exposed.")
        if (cell, segment) not in self._pieces:
            offset = self.zero
            for j in range(9):
                piece = self.k.Piece(cell, j, offset)
                self._pieces[cell, j] = piece
                offset += piece.length
        return self._pieces[cell, segment]

    def _fields_for_simpson(self, piece, x):
        if (piece.n, piece.j) != (159, 0):
            return piece.fields(x)
        # The tight full-tail proof encloses this cell by a remainder.  A
        # local query must instead include its actual protected-end blend.
        z, S = piece.zjet(x)
        raw = x * piece.zx + piece.z0
        if self.hi(raw.c[0] - piece.cap0) >= -self.hi(self.k.q(self.k.cfg["capTransition"])):
            raise ArithmeticError("The protected inner piece is not uncapped.")
        w = z.exp()
        E = 1 + w * w
        old_rx = (x * piece.rd).exp() * (piece.r0 * piece.rd)
        A = (1 - S) * old_rx + S * (-piece.zx / 8) * w * E.power(self.k.q(-1.5))
        B = S * old_rx * E.power(-1)
        return [A, B, w * A, w * B]

    def _simpson(self, piece, left, right, tolerance, depth=0):
        J = self.k.J
        middle = (left + right) / 2
        full = self._fields_for_simpson(piece, J.var(self.interval(left, right)))
        endpoints = [self._fields_for_simpson(piece, J.var(self.qi(t)))
                     for t in (left, middle, right)]
        self.evaluations += 4
        h = self.qi(right - left)
        results = []
        for i, f in enumerate(full):
            base = (endpoints[0][i].c[0] + 4 * endpoints[1][i].c[0] + endpoints[2][i].c[0]) * h / 6
            error = abs(f.c[4]) * h ** 5 / 120
            padded = base + self.k.I(-self.hi(error), self.hi(error))
            ranged = f.c[0] * h
            results.append(self.k.I(max(self.mp.mpf(0), self.lo(padded), self.lo(ranged)),
                                    min(self.hi(padded), self.hi(ranged))))
        if max(self.hi(v) - self.lo(v) for v in results) <= self.lo(self.qi(tolerance)):
            return results
        if depth >= self.max_depth:
            raise ArithmeticError("Local Simpson enclosure exhausted the requested depth.")
        a = self._simpson(piece, left, middle, tolerance / 2, depth + 1)
        b = self._simpson(piece, middle, right, tolerance / 2, depth + 1)
        return [x + y for x, y in zip(a, b)]

    def _variation_primitives(self, piece, x):
        z = piece.zjet(self.k.J.var(self.qi(x)))[0].c[0]
        w = self.iv.exp(z)
        root = self.iv.sqrt(1 + w * w)
        return w / root / 8, -1 / root / 8

    def _variation(self, piece, left, right, tolerance, depth=0):
        z = piece.zjet(self.k.J.var(self.interval(left, right)))[0]
        self.evaluations += 1
        derivative = z.c[1]
        if self.lo(derivative) >= 0 or self.hi(derivative) <= 0:
            a, b = self._variation_primitives(piece, left), self._variation_primitives(piece, right)
            results = [y - x for x, y in zip(a, b)] if self.lo(derivative) >= 0 else [x - y for x, y in zip(a, b)]
            return [self.k.I(max(self.mp.mpf(0), self.lo(v)), self.hi(v)) for v in results]
        w = self.iv.exp(z.c[0])
        E = 1 + w * w
        A = abs(w * derivative) / (8 * E * self.iv.sqrt(E))
        upper = A * self.qi(right - left)
        results = [self.k.I(0, self.hi(upper)), self.k.I(0, self.hi(w * upper))]
        if max(self.hi(v) for v in results) <= self.lo(self.qi(tolerance)):
            return results
        if depth >= self.max_depth:
            raise ArithmeticError("Local total-variation enclosure exhausted the requested depth.")
        middle = (left + right) / 2
        # This is a local stopping bound for each unresolved critical box,
        # not a claimed global error budget. The actual returned interval
        # sums every such contribution, so no root-count assumption enters.
        a = self._variation(piece, left, middle, tolerance, depth + 1)
        b = self._variation(piece, middle, right, tolerance, depth + 1)
        return [x + y for x, y in zip(a, b)]

    def integrate(self, cell, segment, left=0, right=1):
        """True integrals (A, B, wA, wB) on an exact source-x interval."""
        left, right = rational(left), rational(right)
        if not 0 <= left <= right <= 1:
            raise ValueError("Source x must lie in [0,1].")
        if left == right:
            return tuple([self.zero] * 4)
        key = (int(cell), int(segment), left, right)
        if key not in self._integrals:
            piece = self.piece(cell, segment)
            tolerance = self.tolerance * Q(2) ** (-int(cell)) / 9
            if piece.outer or (piece.n, piece.j) == (159, 0):
                values = self._simpson(piece, left, right, tolerance)
            else:
                va = self._variation(piece, left, right, self.variation_tolerance / 9)
                vb = self._simpson(piece, left, right, tolerance)
                values = [va[0], vb[0], va[1], vb[1]]
            self._integrals[key] = tuple(values)
        return self._integrals[key]

    def _outside_integrals(self, cell, segment):
        # Outward -> inward sequence: (0,8),...,(0,0),(1,8),... .
        index = 9 * int(cell) + 8 - int(segment)
        while len(self._outward_sums) <= index:
            k = len(self._outward_sums) - 1
            n, j = k // 9, 8 - k % 9
            values = self.integrate(n, j)
            self._outward_sums.append(tuple(a + b for a, b in zip(self._outward_sums[-1], values)))
        return self._outward_sums[index]

    def primitives(self, cell, segment, left, right=None):
        """Ranges of r and cut-relative height for every x in [left,right]."""
        left = rational(left)
        right = left if right is None else rational(right)
        self.piece(cell, segment)
        if not 0 <= left <= right <= 1:
            raise ValueError("Source x must lie in [0,1].")
        if (cell, segment, left, right) == (0, 8, Q(1), Q(1)):
            values = tuple([self.zero] * 4)
            radius = self.k.cut
        elif (cell, segment, left, right) == (159, 0, Q(0), Q(0)):
            values = tuple(self.integrals_complete[k] for k in ("A", "B", "AH", "BH"))
            radius = self.radius_deep
        else:
            outside = self._outside_integrals(cell, segment)
            a = self.integrate(cell, segment, right, 1)
            b = a if left == right else self.integrate(cell, segment, left, 1)
            values = tuple(o + self.k.I(self.lo(x), self.hi(y)) for o, x, y in zip(outside, a, b))
            radius = self.k.cut - values[0] - self.alpha * values[1]
            radius = self._intersection(radius, self.k.I(self.lo(self.radius_deep), self.hi(self.k.cut)))
        drop = values[2] + self.alpha * values[3]
        return {"r": radius, "height_drop_to_cut": drop,
                "z_relative_to_cut": -drop, "outward_integrals": values}

    def local_jets(self, cell, segment, left, right=None):
        """Algebraic local jets, with r_xx explicitly a one-sided hull."""
        left = rational(left)
        right = left if right is None else rational(right)
        if not 0 <= left <= right <= 1:
            raise ValueError("Source x must lie in [0,1].")
        piece = self.piece(cell, segment)
        z, S = piece.zjet(self.k.J.var(self.interval(left, right)))
        w = self.iv.exp(z.c[0])
        wx = w * z.c[1]
        wxx = w * (2 * z.c[2] + z.c[1] ** 2)
        E = 1 + w * w
        root = self.iv.sqrt(E)
        old_rx = piece.r0 * piece.rd * self.iv.exp(piece.rd * self.interval(left, right))
        weight = piece.weight0 * self.iv.exp(piece.weights * S.c[0])
        chi, chix, j0, j0x = self.one, self.zero, self.one, self.zero
        if piece.outer:
            chi, chix = 1 - S.c[0], -S.c[1]
            j0 = 1 + (self.k.cut / self.k.oldcut - 1) * S.c[0]
            j0x = (self.k.cut / self.k.oldcut - 1) * S.c[1]
        elif (cell, segment) == (159, 0):
            chi, chix = S.c[0], S.c[1]
        P = old_rx * j0
        Px = old_rx * (piece.rd * j0 + j0x)
        B0 = old_rx * weight / E
        A0 = abs(wx) / (8 * E * root)
        Q0 = A0 + self.alpha * B0
        rx = (1 - chi) * P + chi * Q0
        # Both summands describe a convex blend. This positive lower bound
        # does not lose the exact relation chi+(1-chi)=1.
        rx = self._intersection(rx, self.k.I(min(self.lo(P), self.lo(Q0)), max(self.hi(P), self.hi(Q0))))
        if self.lo(rx) <= 0:
            raise ArithmeticError("Positive radius derivative was not enclosed.")
        if self.lo(wx) > 0:
            dabs = wxx
        elif self.hi(wx) < 0:
            dabs = -wxx
        else:
            dabs = self.k.I(-1, 1) * wxx
        A0x = (dabs - 3 * abs(wx) * w * wx / E) / (8 * E * root)
        B0x = B0 * (piece.rd + piece.weights * S.c[1] - 2 * w * wx / E)
        Qx = A0x + self.alpha * B0x
        rxx = (1 - chi) * Px + chi * Qx + chix * (Q0 - P)
        wR = wx / rx
        # h_RR uses only r_x and is continuous, including absolute-value
        # cusps. No classical r_xx is needed for the surface's two-jet.
        result = {"w": w, "w_x": wx, "w_xx": wxx, "r_x": rx,
                  "r_xx_one_sided_hull": rxx, "h_R": w, "h_RR": wR,
                  "E": E, "E_R": 2 * w * wR,
                  "z_x": w * rx, "z_xx_one_sided_hull": wx * rx + w * rxx,
                  "meridian_curvature": wR / (E * root),
                  "x_second_derivative_scope": "Piecewise classical derivatives and their one-sided hulls; not a global C2 x-chart."}
        if (cell, segment, left, right) == (0, 8, Q(1), Q(1)):
            # These are exact identities of the chosen true definition.
            wc, rc = self.k.wcut, self.k.cut
            result.update(w=wc, w_x=-7 * piece.rd * wc,
                          w_xx=49 * piece.rd ** 2 * wc,
                          r_x=piece.rd * rc, r_xx_one_sided_hull=piece.rd ** 2 * rc,
                          h_R=wc, h_RR=-7 * wc / rc,
                          E=1 + wc * wc, E_R=-14 * wc * wc / rc,
                          z_x=wc * piece.rd * rc,
                          z_xx_one_sided_hull=-6 * wc * piece.rd ** 2 * rc,
                          meridian_curvature=(-7 * wc / rc) / ((1 + wc * wc) * self.iv.sqrt(1 + wc * wc)))
        return result

    def at_source(self, cell, segment, left, right=None):
        """Complete background ranges on an original x interval."""
        right = left if right is None else right
        result = {"cell": int(cell), "segment": int(segment),
                  "source_x": [rational(left), rational(right)],
                  **self.primitives(cell, segment, left, right),
                  **self.local_jets(cell, segment, left, right)}
        result["angular_curvature"] = result["w"] / (result["r"] * self.iv.sqrt(result["E"]))
        result["g_RR"] = result["E"]
        result["g_theta_theta"] = result["r"] ** 2
        result["g_xx"] = result["E"] * result["r_x"] ** 2
        return result

    def at_stage(self, stage, left=0, right=1):
        """Use the original native stage's exact affine source-x chart."""
        a, b = rational(stage["rawLeft"]), rational(stage["rawRight"])
        left, right = rational(left), rational(right)
        if not 0 <= left <= right <= 1 or not 0 <= a < b <= 1:
            raise ValueError("Invalid stage chart")
        scale = b - a
        result = self.at_source(stage["rawCell"], stage["rawSegment"],
                                a + scale * left, a + scale * right)
        result.update(stage=stage.get("stage"), stage_xi=[left, right],
                      source_affine=[a, scale], r_xi=result["r_x"] * self.qi(scale),
                      r_xixi_one_sided_hull=result["r_xx_one_sided_hull"] * self.qi(scale ** 2),
                      w_xi=result["w_x"] * self.qi(scale),
                      w_xixi=result["w_xx"] * self.qi(scale ** 2))
        return result

    def at_radius(self, cell, segment, radius_left, radius_right=None, *,
                  x_tolerance="1e-10", max_iterations=32):
        """Certified monotone inverse inside a specified original piece.

        Endpoint inequalities must be certified. An unattained x tolerance
        is reported, never replaced by a midpoint alpha or an unchecked root.
        The returned x enclosure is valid even if normalization uncertainty
        prevents further contraction.
        """
        rl = rational(radius_left)
        rr = rl if radius_right is None else rational(radius_right)
        if rl > rr:
            raise ValueError("Reversed physical radius interval")
        target = self.interval(rl, rr)
        at0 = self.primitives(cell, segment, 0)["r"]
        at1 = self.primitives(cell, segment, 1)["r"]
        if self.hi(at0) > self.lo(target) or self.lo(at1) < self.hi(target):
            raise ValueError("This radius interval is not proved strictly inside this piece; use source coordinates or a neighboring-piece union.")
        left, right = Q(0), Q(1)
        tolerance = rational(x_tolerance)
        iterations = 0
        for iterations in range(1, max_iterations + 1):
            if right - left <= tolerance:
                break
            middle = (left + right) / 2
            rm = self.primitives(cell, segment, middle)["r"]
            derivative = self.local_jets(cell, segment, left, right)["r_x"]
            newton = self.qi(middle) + (target - rm) / derivative
            nl = max(left, mpf_fraction(self.lo(newton)))
            nr = min(right, mpf_fraction(self.hi(newton)))
            if nl > nr:
                raise ArithmeticError("Inconsistent inverse enclosures")
            if nr - nl >= (right - left) * Q(999, 1000):
                # Certified bisection may still help while interval Newton
                # is broad. If the point interval overlaps the target, its
                # uncertainty is retained rather than deciding by midpoint.
                if self.hi(rm) < self.lo(target):
                    nl = middle
                elif self.lo(rm) > self.hi(target):
                    nr = middle
                else:
                    left, right = nl, nr
                    break
            left, right = nl, nr
        result = self.at_source(cell, segment, left, right)
        result["r"] = self._intersection(result["r"], target)
        result["g_theta_theta"] = result["r"] ** 2
        result["angular_curvature"] = result["w"] / (result["r"] * self.iv.sqrt(result["E"]))
        result.update(inverse_iterations=iterations,
                      requested_x_tolerance=str(tolerance),
                      x_tolerance_met=right - left <= tolerance,
                      inverse_status="certified_enclosure", radius_target=[rl, rr])
        return result

    def bind_native_metadata(self, metadata):
        """Check physical inputs and stage coordinates, not field accuracy."""
        p = metadata["physicalParameters"]
        expected = self.constants["parameters"]
        # Derived floating aliases may not be serialized in the metadata.
        derived = {"rCuff", "oldCut", "epsilonScale", "prefixRByCell", "constructor"}
        keys = sorted(set(expected) - derived)
        mismatch = [key for key in keys if key not in p or p[key] != expected[key]]
        if mismatch:
            raise ValueError("Native physical inputs differ: " + ", ".join(mismatch))
        depth = int(p.get("physicalDepth", p["depth"]))
        stages = metadata["stages"]
        if len(stages) % (9 * depth):
            raise ValueError("Unexpected stage count")
        parts = len(stages) // (9 * depth)
        for index, stage in enumerate(stages):
            cell = index // (9 * parts)
            segment = 8 - (index // parts) % 9
            part = parts - 1 - index % parts
            if (stage["stage"] != index or stage["rawCell"] != cell or stage["rawSegment"] != segment
                    or rational(stage["rawLeft"]) != Q(part, parts)
                    or rational(stage["rawRight"]) != Q(part + 1, parts)):
                raise ValueError("Unexpected native source-x chart at stage " + str(index))
        return {"status": "physical_inputs_and_stage_coordinates_bound",
                "definition_sha256": DEFINITION_SHA256,
                "checked_parameter_keys": keys, "depth": depth, "parts": parts,
                "stages": len(stages), "finite_scope": metadata["scope"],
                "field_transfer_certified": False,
                "state_contract": "states[k+1] is the inner endpoint of stage k; u=H/r_JS^4. A true-R shared-C2 map must explicitly specify physical H and physical-R jets, and its original nonrotating mean primitive."}


def read_json(path):
    path = Path(path)
    return json.loads(gzip.decompress(path.read_bytes()) if path.suffix == ".gz" else path.read_text())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--constants", type=Path, required=True)
    parser.add_argument("--normalization-certificate", type=Path, required=True)
    parser.add_argument("--kernel", type=Path)
    parser.add_argument("--queries", type=Path, required=True)
    parser.add_argument("--metadata", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--coefficient-tolerance", default="1e-14")
    args = parser.parse_args()
    started = time.monotonic()
    oracle = Q060TrueBackgroundOracle(args.constants, args.normalization_certificate,
                                     kernel=args.kernel, coefficient_tolerance=args.coefficient_tolerance)
    metadata = read_json(args.metadata) if args.metadata else None
    binding = oracle.bind_native_metadata(metadata) if metadata else None
    rows = []
    for request in read_json(args.queries):
        kind = request.get("kind", "source")
        if kind == "source":
            value = oracle.at_source(request["cell"], request["segment"], request["left"], request.get("right"))
        elif kind == "stage" and metadata:
            value = oracle.at_stage(metadata["stages"][request["stage"]], request.get("left", 0), request.get("right", 1))
        elif kind == "radius":
            value = oracle.at_radius(request["cell"], request["segment"], request["left"], request.get("right"),
                                     x_tolerance=request.get("x_tolerance", "1e-10"))
        else:
            raise ValueError("Unknown query kind or missing stage metadata")
        rows.append({"request": request, "result": oracle.json_value(value)})
        print(json.dumps({"query": request, "seconds": time.monotonic() - started,
                          "r": oracle.bounds(value["r"]), "h_RR": oracle.bounds(value["h_RR"])}), flush=True)
    result = {"scope": __doc__, "status": "true_background_queries_enclosed",
              "provenance": oracle.provenance, "alpha": oracle.bounds(oracle.alpha),
              "binding": binding, "queries_sha256": file_sha256(args.queries),
              "metadata_sha256": file_sha256(args.metadata) if args.metadata else None,
              "queries": rows, "interval_evaluations": oracle.evaluations,
              "seconds": time.monotonic() - started}
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "queries": len(rows),
                      "seconds": result["seconds"], "out_sha256": file_sha256(args.out)}), flush=True)


if __name__ == "__main__":
    main()
