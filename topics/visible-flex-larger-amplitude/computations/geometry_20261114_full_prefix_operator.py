#!/usr/bin/env python3
"""R251 whole-prefix consumer, with same-source scalar-square envelopes.

The actual accepted v3/v4 checkpoint and optional R249 inlet normal form
define the complete physical shared-node quintic. The scalar is the same
declared exact prefix polynomial plus the original binary-constant finite
Gauss expressions, with every frozen design control retained.

This proves pointwise relative operator inequalities for that declared
real expression. It does not identify a literal floating program with
its real expression, prove the scalar interfaces C2, certify the tail or
caps, manufacture a nonlinear acceptance, or add a machine nine-jet gate.

The descriptor exporter is deliberately importable without flint/numpy.
Call it on the LIVE original profile in the successful producer if exact
runtime Gauss-table provenance is required. Reconstructing it later is
labelled as reconstruction and is not silently promoted to live provenance.
All mathematical execution is restricted to the public repository Actions.
"""
from __future__ import annotations

import argparse
import bisect
from fractions import Fraction
import gzip
import hashlib
import json
from math import comb, isfinite
import os
from pathlib import Path
import sys
import time

SCHEMA = "R251-complete-prefix-Arb-operator-v1"
DESCRIPTOR_SCHEMA = "same-source-complete-scalar-real-expression-v1"
V3 = "complete-prefix-controls-independent-field-modes-v3"
V4 = "frozen-complete-scalar-same-metric-refinement-v4"
HERE = Path(__file__).resolve().parent
SOURCE_SHA256 = {
    "geometry_20261114_r225_fixed_profile.py": "478d0bf603ea05a9f20228ff2fd591e2f767e6ab0686a6129b1114aa831b0c6c",
    "geometry_20261114_full_scalar_profile.py": "8ff23e31a58d0f8b087929d69ac8d6f9b6f2777615e50eef5ebe40ed7b6bed6b",
    "geometry_20261114_prefix_controls_profile.py": "f019e6b33c8e1776d5cca87c22efadd0f999766b894be855efb53ad10b4d6a24",
    "geometry_20261114_lifted_modes_profile.py": "13cd479d91590a6ce7a82e6461d6cd2c1561d7303264680621e9cbe438b7cee5",
    "geometry_20261114_same_metric_profile.py": "651fd91fcf8d34be6cf2054f79728b417149ae4a07e0830915821f32ccf9cd89",
    "strong_20261114_scaled_core_tail_connector.py": "661d5d84dc0dd3da46f4936c2c3ad28f80df3475f421c56d770a2afa6402ac08",
    "alternative-neck-provider.py": "84ed048425c8b0f4deeec8af37828e318150cde5d59995da77f64d923591b9c2",
    "alternative-neck-flatturn.py": "c0578ed401a2433c72ec99702c9c32a8412c66264a7fb81a8b8c74ba054fbbdd",
    "alternative-neck-excursion.py": "f70571b8356e33cb89eabae2dba4e173e6612dac4d65d5df74f5ec14c34ad53c",
    "strong_angle_boost.py": "ce2117cffe2e55d310eb0be219e7d22e750d97cd22704e75c3dd74a085c020be",
}


def actions_only():
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Run scientific evaluation in this public repository's Actions")


def Q(value):
    if isinstance(value, Fraction):
        return value
    if isinstance(value, float):
        if not isfinite(value):
            raise ValueError("Nonfinite scalar source constant")
        return Fraction.from_float(value)
    return Fraction(value)


def canonical_sha(value):
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"),
                     ensure_ascii=False, allow_nan=False).encode()
    return hashlib.sha256(raw).hexdigest()


def file_sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False)+"\n").encode()
    path.write_bytes(gzip.compress(raw, mtime=0) if path.suffix == ".gz" else raw)


def encoded(value):
    """Exact real constants; floats become their exact binary rational values."""
    if isinstance(value, dict):
        return {str(key): encoded(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [encoded(item) for item in value]
    if isinstance(value, (str, bool)) or value is None:
        return value
    if hasattr(value, "tolist"):
        return encoded(value.tolist())
    if isinstance(value, (int, float, Fraction)):
        return str(Q(value))
    raise TypeError("Unsupported original scalar descriptor value: "+type(value).__name__)


def design_specification(specification):
    if specification.get("schema") == V3:
        design = specification
    elif specification.get("schema") == V4:
        design = specification["frozen_design_scalar_profile"]
        if (specification.get("canonical_scalar_identity_sha256") != canonical_sha(design)
                or specification.get("active_scalar_parameters") != 0
                or specification.get("frozen_design_parameters") != design.get("frozen_design_parameters")):
            raise ValueError("The original three frozen scalar controls changed in v4")
    else:
        raise ValueError("Use the actual complete v3/v4 scalar specification")
    if (design.get("schema") != V3 or len(design.get("frozen_design_parameters", [])) != 3
            or int(design["field_modes"]) != int(design["tail_modes"])):
        raise ValueError("Retain the entire v3 scalar design")
    return design


def checked_original_sources():
    actual = {name: file_sha(HERE/name) for name in SOURCE_SHA256}
    differences = [name for name in SOURCE_SHA256 if actual[name] != SOURCE_SHA256[name]]
    if differences:
        raise ValueError("Review the scalar formula before using changed source: "+", ".join(differences))
    return actual


def export_scalar_descriptor(profile, specification, parameters=None, *,
        producer_checkpoint_sha256=None, origin="unspecified-runtime-object"):
    """Copy actual live construction constants; do not construct a new Gauss rule.

    For live provenance use origin='actual-live-profile' and the SHA256 of
    the completed accepted checkpoint. This is a sidecar, avoiding a cyclic
    checkpoint/descriptor hash. A v4 producer must additionally compare the
    mathematical identity with its actual parent to certify same-g across runs.
    """
    actions_only()
    design = design_specification(specification)
    sources = checked_original_sources()
    designed = getattr(profile, "designed", profile)
    if hasattr(profile, "frozen_parameters"):
        live_parameters = list(map(float, profile.frozen_parameters))
        if parameters is not None and encoded(parameters) != encoded(live_parameters):
            raise ValueError("Do not replace any of the actual frozen controls")
    else:
        live_parameters = design["frozen_design_parameters"] if parameters is None else parameters
    if (encoded(live_parameters) != encoded(design["frozen_design_parameters"])
            or int(designed.parameter_count) != 3
            or canonical_sha(designed.fixed_geometry) != canonical_sha(design["base_prefix_geometry"])
            or Q(float(designed.prefix_end)) != Q(float(design["base_prefix_end"]))
            or encoded([[b.left, b.right] for b in designed.bumps]) !=
               encoded(design["control_supports_binary64"])):
        raise ValueError("The supplied actual profile differs from its complete scalar specification")
    if origin not in ("actual-live-profile", "reconstructed-from-checkpoint", "unspecified-runtime-object"):
        raise ValueError("Use an explicit supported descriptor origin")
    if producer_checkpoint_sha256 is not None and (
            len(producer_checkpoint_sha256) != 64 or
            any(c not in "0123456789abcdef" for c in producer_checkpoint_sha256)):
        raise ValueError("The producer checkpoint identity must be a SHA256")
    if origin == "actual-live-profile" and producer_checkpoint_sha256 is None:
        raise ValueError("A live descriptor must bind its completed accepted checkpoint")
    turn = designed.turn
    turn_values = {key: getattr(turn, key) for key in (
        "a0", "ap0", "app0", "phi0", "phi1", "k0", "K", "ei", "eo",
        "integrated_K", "length", "end_radius")}
    turn_values.update(gx=turn.gx.tolist(), gw=turn.gw.tolist())
    base = designed.provider.fl.base
    segments = [dict(segment) for segment in designed.bridge.segments]
    if (len(turn_values["gx"]) != 48 or len(turn_values["gw"]) != 48
            or len(base.gu) != 64 or len(base.gw) != 64
            or not segments or any(s["kind"] not in ("turn", "coast", "brake") for s in segments)
            or any("strong_angle_boost" in s for s in segments)):
        raise ValueError("This verified scalar formula covers the actual 48/64 original turn/coast/brake source")
    expression = dict(
        exact_target="Original exact shared-knot scalar prefix plus original binary-constant finite-Gauss real expressions; all three p* retained",
        original_sources_sha256=sources,
        prefix_geometry_sha256=canonical_sha(designed.fixed_geometry),
        prefix_exact_coefficient_sha256=designed.prefix.exact_coefficient_sha256,
        prefix_rounded_evaluator_coefficients_sha256=canonical_sha(encoded(designed.prefix.coefficients.tolist())),
        frozen_parameters=encoded(live_parameters),
        boundaries=encoded({key: getattr(designed, key) for key in
            ("prefix_end", "turn_end", "coast_length", "bridge_start", "end")}),
        auxiliary_knots=encoded(list(map(float, designed.knots))),
        controls=encoded([dict(left=b.left, right=b.right, stored_width=b.width) for b in designed.bumps]),
        outside_coast_speed=encoded(.985),
        turn=encoded(turn_values),
        bridge=dict(segments=encoded(segments), gu=encoded(base.gu.tolist()), gw=encoded(base.gw.tolist()),
            actual_end=encoded(designed.bridge.end),
            mask_left_tolerance=encoded(1e-13), mask_last_right_tolerance=encoded(1e-12),
            selection="Last matching segment, source masks and clip to [0,1], interpreted as exact real operations on the recorded binary constants"),
        returned_ap_app_used_as_derivatives_of_finite_Gauss_radius=False,
        actual_constructor_tables_copied_without_regeneration=True)
    result = dict(schema=DESCRIPTOR_SCHEMA,
        canonical_v3_specification_sha256=canonical_sha(design),
        current_full_specification_sha256=canonical_sha(specification),
        mathematical_expression=expression, mathematical_identity_sha256=canonical_sha(expression),
        producer=dict(origin=origin, checkpoint_sha256=producer_checkpoint_sha256,
            profile_class=type(profile).__module__+"."+type(profile).__name__,
            exporter_source_sha256=file_sha(__file__),
            numpy_version=getattr(sys.modules.get("numpy"), "__version__", None)),
        literal_floating_evaluator_error_verified=False,
        scalar_C2_interfaces_verified_here=False, new_metric_fitted=False)
    return result


def original_jet(law, s):
    length, velocity, k0 = (Q(float(law[key])) for key in ("length", "velocity", "k0"))
    if s >= length:
        end = 1+length*velocity/2+k0*length*length/12
        return end+velocity*(s-length), velocity, Fraction(0)
    u = s/length
    b, c, d = k0*length, 3*velocity-2*k0*length, k0*length-2*velocity
    return (1+length*(b*u*u/2+c*u**3/3+d*u**4/4),
            b*u+c*u*u+d*u**3, (b+2*c*u+3*d*u*u)/length)


def prefix_coefficients(geometry):
    x = [Q(float(row["s"])) for row in geometry["knots"]]
    if len(x) < 2 or any(b <= a for a, b in zip(x[:-1], x[1:])):
        raise ValueError("The exact original scalar knots must be strictly ordered")
    jets = [[Q(float(row[key])) for key in ("a", "ap", "app")] for row in geometry["knots"]]
    jets[0] = list(original_jet(geometry["initial_law"], x[0]))
    answer = []
    for j in range(len(x)-1):
        h = x[j+1]-x[j]
        c0, c1, c2 = jets[j][0], h*jets[j][1], h*h*jets[j][2]/2
        A, B, C = jets[j+1][0]-c0-c1-c2, h*jets[j+1][1]-c1-2*c2, h*h*jets[j+1][2]-2*c2
        answer.append([c0, c1, c2, 10*A-4*B+C/2, -15*A+7*B-C, 6*A-3*B+C/2])
    return x, answer


class ScalarExpression:
    """Evaluate the fixed real expression and its local Arb-series enclosure."""
    def __init__(self, specification, descriptor, primitive):
        self.cell = primitive
        self.arb, self.arb_series = primitive.arb, __import__("flint").arb_series
        self.b = primitive.ball
        self.design = design_specification(specification)
        if (descriptor.get("schema") != DESCRIPTOR_SCHEMA
                or descriptor.get("canonical_v3_specification_sha256") != canonical_sha(self.design)
                or descriptor.get("mathematical_identity_sha256") !=
                   canonical_sha(descriptor["mathematical_expression"])):
            raise ValueError("The scalar expression descriptor is not bound to the whole original design")
        self.d = descriptor["mathematical_expression"]
        self.geometry = self.design["base_prefix_geometry"]
        self.x, self.coefficients = prefix_coefficients(self.geometry)
        if (self.d["prefix_geometry_sha256"] != canonical_sha(self.geometry)
                or self.d["prefix_exact_coefficient_sha256"] !=
                   canonical_sha([[str(c) for c in row] for row in self.coefficients])
                or self.d["original_sources_sha256"] != checked_original_sources()):
            raise ValueError("The same exact prefix or source expression was not retained")
        self.boundaries = {key: Q(value) for key, value in self.d["boundaries"].items()}
        self.turn = {key: ([Q(x) for x in value] if isinstance(value, list) else Q(value))
                     for key, value in self.d["turn"].items()}
        self.controls = [{key: Q(value) for key, value in row.items()} for row in self.d["controls"]]
        self.parameters = [Q(value) for value in self.d["frozen_parameters"]]
        self.speed = Q(self.d["outside_coast_speed"])
        bridge = self.d["bridge"]
        self.segments = [{key: value if isinstance(value, str) and key == "kind" else
                          (Q(value) if isinstance(value, str) else value)
                          for key, value in row.items()} for row in bridge["segments"]]
        self.gu, self.gw = [Q(v) for v in bridge["gu"]], [Q(v) for v in bridge["gw"]]
        self.left_tol, self.right_tol = Q(bridge["mask_left_tolerance"]), Q(bridge["mask_last_right_tolerance"])
        if (len(self.controls) != 3 or len(self.parameters) != 3 or
                any(b["stored_width"] <= 0 for b in self.controls) or
                any(not 0 < x < 1 for x in self.turn["gx"]+self.gu) or
                any(w <= 0 for w in self.turn["gw"]+self.gw)):
            raise ValueError("Retain finite positive original Gauss data and every scalar control")
        self.constant_panels = {}
        self.breakpoints = self._breakpoints()

    def _breakpoints(self):
        B, t = self.boundaries, self.turn
        values = [Fraction(0), *self.x, *[B[key] for key in
            ("prefix_end", "turn_end", "bridge_start", "end")],
            *map(Q, self.d["auxiliary_knots"])]
        values.append(Q(float(self.geometry["initial_law"]["length"])))
        for control in self.controls:
            values.extend((control["left"], control["right"],
                           control["left"]+control["stored_width"]))
        S, L = B["prefix_end"], t["length"]
        values.extend(S+L*u for u in (Fraction(0), t["ei"], 1-t["eo"], Fraction(1)))
        start = B["bridge_start"]
        for i, seg in enumerate(self.segments):
            s0, s1, length = seg["s0"], seg["s1"], seg["length"]
            if length <= 0:
                raise ValueError("The stored original segment list contains a nonpositive length")
            values.extend((start+s0-self.left_tol, start+s0, start+s1,
                           start+s0+length))
            if i == len(self.segments)-1:
                values.append(start+s1+self.right_tol)
            if "turn_ramp" in seg:
                eps = seg["turn_ramp"]
                if not 0 < eps < Fraction(1, 2):
                    raise ValueError("The two original phase ramps must be disjoint")
                values.extend((start+s0+length*eps, start+s0+length*(1-eps)))
        return sorted(set(x for x in values if 0 <= x <= B["end"]))

    def branch(self, s):
        B = self.boundaries
        if not 0 <= s <= B["end"]:
            raise ValueError("The exact scalar request is outside its stored complete domain")
        if s <= B["prefix_end"]:
            if s <= self.x[0]:
                return ("initial", 0)
            return ("prefix", min(len(self.x)-2, bisect.bisect_right(self.x, s)-1))
        if s <= B["turn_end"]:
            return ("turn", 0)
        if s <= B["bridge_start"]:
            return ("coast", 0)
        local, chosen = s-B["bridge_start"], None
        for i, seg in enumerate(self.segments):
            right = local < seg["s1"] if i+1 < len(self.segments) else local <= seg["s1"]+self.right_tol
            if local >= seg["s0"]-self.left_tol and right:
                chosen = i
        if chosen is None:
            raise ValueError("The source's exact mask convention leaves this radius unassigned")
        return ("bridge", chosen)

    def angle_phase(self, u, panel):
        t, b = self.turn, self.b
        k0, K, ei, eo = (b(t[key]) for key in ("k0", "K", "ei", "eo"))
        if panel == 0:
            v = u/ei
            integral = k0*u+(K-k0)*ei*(v**3-v**4/2)
        elif panel == 1:
            integral = ei*(k0+K)/2+K*(u-ei)
        else:
            v = (u-(1-eo))/eo
            integral = ei*(k0+K)/2+K*(1-eo-ei)+K*eo*(v-v**3+v**4/2)
        return b(t["phi0"])-b(t["length"])*integral

    def bridge_phase(self, seg, u, panel):
        b = self.b
        p0, dp = b(seg["p0"]), b(seg["p1"]-seg["p0"])
        if "turn_ramp" in seg:
            eps = b(seg["turn_ramp"])
            if panel == 0:
                v = u/eps
                integral = eps*(v**3-v**4/2)
            elif panel == 1:
                integral = u-eps/2
            else:
                v = (1-u)/eps
                integral = 1-eps-eps*(v**3-v**4/2)
            return p0+dp*integral/(1-eps)
        if seg["kind"] == "turn":
            return p0+dp*(3*u*u-2*u**3)
        if seg["kind"] == "brake":
            return p0+dp*u*u
        return u*0+p0

    def finite_integral(self, u, middle_u, *, bridge_index=None):
        b = self.b
        if bridge_index is None:
            t = self.turn
            cuts, nodes, weights = [Fraction(0), t["ei"], 1-t["eo"], Fraction(1)], t["gx"], t["gw"]
            phase = lambda v, j: self.angle_phase(v, j)
            key = ("turn",)
        else:
            seg = self.segments[bridge_index]
            cuts = ([Fraction(0), seg["turn_ramp"], 1-seg["turn_ramp"], Fraction(1)]
                    if "turn_ramp" in seg else [Fraction(0), Fraction(1)])
            nodes, weights = self.gu, [w/2 for w in self.gw]
            phase = lambda v, j: self.bridge_phase(seg, v, j)
            key = ("bridge", bridge_index)
        result = u*0
        for j, (left, right) in enumerate(zip(cuts[:-1], cuts[1:])):
            if middle_u <= left:
                continue
            if middle_u >= right:
                ck = (*key, j, int(self.cell.ctx.prec))
                if ck not in self.constant_panels:
                    width = right-left
                    total = sum((b(w)*phase(b(left+x*width), j).sin()
                                 for x, w in zip(nodes, weights)), self.arb(0))
                    self.constant_panels[ck] = b(width)*total
                result = result+self.constant_panels[ck]
            else:
                width = u-b(left)
                total = sum((b(w)*phase(b(left)+b(x)*width, j).sin()
                             for x, w in zip(nodes, weights)), u*0)
                result = result+width*total
        return result

    def value(self, s, branch, middle):
        b, B = self.b, self.boundaries
        kind, index = branch
        if kind == "initial":
            law = self.geometry["initial_law"]
            length, v, k0 = (Q(float(law[key])) for key in ("length", "velocity", "k0"))
            if middle >= length:
                base = s*0+b(1+length*v/2+k0*length*length/12)+b(v)*(s-b(length))
            else:
                u = s/b(length)
                q0, q1, q2 = k0*length, 3*v-2*k0*length, k0*length-2*v
                base = 1+b(length)*(b(q0)*u*u/2+b(q1)*u**3/3+b(q2)*u**4/4)
        elif kind == "prefix":
            u = (s-b(self.x[index]))/b(self.x[index+1]-self.x[index])
            base = u*0
            for coefficient in reversed(self.coefficients[index]):
                base = base*u+b(coefficient)
        elif kind == "turn":
            u = (s-b(B["prefix_end"]))/b(self.turn["length"])
            mid_u = (middle-B["prefix_end"])/self.turn["length"]
            base = b(self.turn["a0"])+b(self.turn["length"])*self.finite_integral(u, mid_u)
        elif kind == "coast":
            base = s*0+b(self.turn["end_radius"])-b(self.speed)*(s-b(B["turn_end"]))
        elif kind == "bridge":
            seg = self.segments[index]
            mid_u = (middle-B["bridge_start"]-seg["s0"])/seg["length"]
            if mid_u <= 0:
                u, mid_u = s*0, Fraction(0)
            elif mid_u >= 1:
                u, mid_u = s*0+1, Fraction(1)
            else:
                u = (s-b(B["bridge_start"]+seg["s0"]))/b(seg["length"])
            base = b(seg["a0"])+b(seg["length"])*self.finite_integral(u, mid_u, bridge_index=index)
        else:
            raise AssertionError("Unknown scalar source branch")
        for control, parameter in zip(self.controls, self.parameters):
            if parameter and control["left"] < middle < control["left"]+control["stored_width"]:
                width = b(control["stored_width"])
                x = (s-b(control["left"]))/width
                base = base+b(parameter)*width*width*64*x**3*(1-x)**3
        return base

    def exact_degree(self, branch, middle):
        kind, index = branch
        if kind == "prefix":
            degree = 5
        elif kind == "initial":
            degree = 1 if middle >= Q(float(self.geometry["initial_law"]["length"])) else 4
        elif kind == "coast" or (kind == "bridge" and self.segments[index]["kind"] == "coast"):
            degree = 1
        else:
            return None
        if any(parameter and control["left"] < middle < control["left"]+control["stored_width"]
               for control, parameter in zip(self.controls, self.parameters)):
            degree = max(degree, 6)
        return degree

    def envelope(self, left, right, nonpolynomial_degree=4):
        if left >= right or any(left < cut < right for cut in self.breakpoints):
            raise ValueError("Split at every exact source polynomial/phase/clip/mask boundary first")
        middle, h = (left+right)/2, right-left
        branch = self.branch(middle)
        polynomial_degree = self.exact_degree(branch, middle)
        degree = int(nonpolynomial_degree if polynomial_degree is None else polynomial_degree)
        if degree < 1 or degree > 12:
            raise ValueError("Use a local scalar Taylor degree from one to twelve")
        series = self.arb_series
        self.cell.ctx.cap = max(int(self.cell.ctx.cap), degree+2)
        center = self.value(series([self.b(middle), self.arb(1)], prec=degree+2), branch, middle)
        interval = self.arb(str(middle), str(h/2))
        entire = self.value(series([interval, self.arb(1)], prec=degree+2), branch, middle)
        if center.prec < degree+2 or entire.prec < degree+2:
            raise ArithmeticError("The scalar derivative series was truncated below the required remainder order")
        remainder = (entire[degree+1].abs_upper()*self.b((h/2)**(degree+1))).upper()
        power = []
        for j in range(degree+1):
            value = sum((center[i]*self.b(comb(i, j)*h**i*Fraction(-1, 2)**(i-j))
                         for i in range(j, degree+1)), self.arb(0))
            power.append(value)
        qbern = self.cell.scalar_power_to_bernstein(power)
        A = max((v.abs_upper().upper() for v in qbern))
        delta = (2*A*remainder+remainder*remainder).upper()
        square = self.cell.BernsteinLaurent.scalar(qbern)
        square = square*square
        lower, upper = [p[0]-delta for p in square.controls], [p[0]+delta for p in square.controls]
        a_lower = self.cell.minimum_lower(qbern)-remainder
        report = dict(method="Exact source expression with Arb series derivatives and Taylor remainder; Bernstein square envelopes",
            branch=list(branch), interval=list(map(str, (left, right))),
            scalar_polynomial_degree=polynomial_degree, local_Taylor_degree=degree,
            finite_Gauss_radius_differentiated_directly=True,
            separate_returned_ap_app_used=False,
            Taylor_remainder_upper=self.cell.ball_record(remainder),
            square_envelope_half_width_upper=self.cell.ball_record(delta),
            scalar_positive_lower=self.cell.ball_record(a_lower),
            scalar_positive=bool(a_lower > 0), exact_polynomial_remainder_zero=bool(remainder == 0),
            same_mathematical_expression_sha256=canonical_sha(self.d),
            full_frozen_controls_retained=True, original_quadrature_nodes_weights_retained=True)
        return lower, upper, report, branch, middle


def descriptor_binding(saved, actual_descriptor, external_path):
    result = dict(external_descriptor_supplied=external_path is not None,
        actual_live_runtime_constants_verified=False, same_complete_scalar_specification=True,
        reconstructed_descriptor=actual_descriptor)
    if external_path is None:
        result["unpaid"] = "No actual-live producer sidecar; this result binds the current reconstruction's declared real expression only"
        return result
    supplied = read(external_path)
    if (supplied.get("schema") != DESCRIPTOR_SCHEMA
            or supplied.get("mathematical_identity_sha256") != canonical_sha(supplied["mathematical_expression"])
            or supplied.get("canonical_v3_specification_sha256") != actual_descriptor["canonical_v3_specification_sha256"]
            or supplied["mathematical_expression"] != actual_descriptor["mathematical_expression"]):
        raise ValueError("The supplied source scalar constants/tables or entire p* differ")
    producer = supplied.get("producer", {})
    live = (producer.get("origin") == "actual-live-profile" and
            producer.get("checkpoint_sha256") == file_sha(saved.path))
    result.update(external_descriptor_sha256=file_sha(external_path),
        external_descriptor_producer=producer, exact_mathematical_descriptor_match=True,
        actual_live_runtime_constants_verified=live)
    if not live:
        result["unpaid"] = "The matching sidecar does not bind this accepted checkpoint as an actual-live producer"
    return result


def array_identity(array):
    # Same canonical bytes as the R249 normalizer, without depending on its hash helper.
    import numpy as np
    value = np.ascontiguousarray(array, dtype="<f8")
    raw = str(value.shape).encode("ascii")+b"\0"+value.tobytes()
    return hashlib.sha256(raw).hexdigest()


def main():
    actions_only()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--scalar-descriptor", type=Path)
    parser.add_argument("--scalar-descriptor-out", type=Path)
    parser.add_argument("--eta", default="1/1000000")
    parser.add_argument("--precision", type=int, default=160)
    parser.add_argument("--angular-points", type=int, default=2048)
    parser.add_argument("--max-angular-points", type=int, default=32768)
    parser.add_argument("--scalar-degree", type=int, default=4)
    parser.add_argument("--max-radial-depth", type=int, default=8)
    parser.add_argument("--cell-start", type=int, default=0)
    parser.add_argument("--cell-stop", type=int)
    parser.add_argument("--no-normalize-inlet", action="store_true")
    parser.add_argument("--continue-after-counterexample", action="store_true")
    parser.add_argument("--first-cell-packet", type=Path)
    args = parser.parse_args()
    if args.precision < 80 or args.max_radial_depth < 0:
        raise ValueError("Use at least 80-bit Arb precision and a nonnegative subdivision budget")
    import flint
    import geometry_20261114_direct_operator_cell as cell
    from geometry_20261114_inlet_parity_normal_form import read_saved
    cell.ctx.prec = args.precision
    begin = time.monotonic()
    saved = read_saved(args.checkpoint, normalize=not args.no_normalize_inlet)
    specification = saved.rec["fixed_scalar_profile"]["geometry"]
    reconstructed = export_scalar_descriptor(saved.profile_model, specification,
        producer_checkpoint_sha256=file_sha(args.checkpoint), origin="reconstructed-from-checkpoint")
    binding = descriptor_binding(saved, reconstructed, args.scalar_descriptor)
    descriptor_path = args.scalar_descriptor_out or args.out.with_name(args.out.stem+".scalar-expression.json")
    write(descriptor_path, reconstructed)
    scalar = ScalarExpression(specification, reconstructed, cell)
    x = [Q(float(v)) for v in saved.sol.x]
    if x[0] != 0 or x[-1] != scalar.boundaries["end"]:
        raise ValueError("The saved field and same scalar must have exactly the same parameter domain")
    cuts = sorted(set(x+scalar.breakpoints))
    intervals = list(zip(cuts[:-1], cuts[1:]))
    stop = len(intervals) if args.cell_stop is None else args.cell_stop
    if not 0 <= args.cell_start < stop <= len(intervals):
        raise ValueError("The requested exact common-cell range is empty or outside the full prefix")
    eta, core = Q(args.eta), [float(v) for v in saved.core]
    if not 0 < eta < 1:
        raise ValueError("The exact requested operator bound must lie in (0,1)")
    angular = cell.AngularCertificate(args.angular_points, args.max_angular_points)
    core_sha = cell.canonical_sha([str(Q(v)) for v in core])
    # The accepted reader independently establishes R237 by exact Fraction arithmetic.
    rho_lower = Q(saved.rho_lower_exact)
    if rho_lower <= 0:
        raise ValueError("The complete material density was not proved positive")
    density = dict(certified=True, complete_core_sha256=core_sha,
        lower=cell.ball_record(cell.ball(rho_lower)),
        proof="Accepted full saved reader's exact R237 triangle bound for every original core coefficient",
        reader_definition=saved.definition.get("material_circle_diffeomorphism_proof"),
        exact_fraction_bound=str(rho_lower), angular_sampling_used=False)
    identity = dict(checkpoint_sha256=file_sha(args.checkpoint), M=int(saved.M), N=int(saved.N),
        physical_state_dimension=int(saved.n), complete_core_sha256=core_sha,
        physical_node_sha256=array_identity(saved.sol.x),
        physical_nodal_jet_sha256=[array_identity(v) for v in saved.quintic.nodal],
        full_scalar_specification_sha256=canonical_sha(specification),
        canonical_v3_scalar_specification_sha256=reconstructed["canonical_v3_specification_sha256"],
        scalar_mathematical_identity_sha256=reconstructed["mathematical_identity_sha256"],
        inlet_normalization=saved.definition.get("inlet_normalization", dict(enabled=False)),
        complete_saved_field_definition=saved.definition,
        interval_partition_sha256=canonical_sha([[str(a), str(b)] for a, b in intervals]))
    ledger = args.out.with_name(args.out.stem+".cells.jsonl.gz")
    if ledger.exists():
        raise FileExistsError("Do not overwrite an existing completed-cell ledger; choose a new output")
    ledger.parent.mkdir(parents=True, exist_ok=True)
    record_count = 0
    compact = []
    first_packet_written = False
    full_cache = {}
    stopped_for_witness = False

    def append_record(value):
        nonlocal record_count
        payload = (json.dumps(value, separators=(",", ":"), ensure_ascii=False, allow_nan=False)+"\n").encode()
        # Independent complete gzip members retain every flushed earlier record.
        with ledger.open("ab") as stream:
            stream.write(gzip.compress(payload, mtime=0))
        record_count += 1

    append_record(dict(type="identity", schema=SCHEMA, identity=identity,
        source_sha256=file_sha(__file__), primitive_source_sha256=file_sha(cell.__file__),
        requested_eta=str(eta), source_scalar_descriptor=reconstructed))

    def inspect(a, b, base_index, depth):
        nonlocal first_packet_written, stopped_for_witness
        j = min(len(x)-2, bisect.bisect_right(x, (a+b)/2)-1)
        if not x[j] <= a < b <= x[j+1]:
            raise AssertionError("A certificate subcell crossed an original physical node")
        if j not in full_cache:
            nodal = [[[float(v) for v in saved.quintic.nodal[order][row]]
                       for row in (j, j+1)] for order in range(3)]
            full_cache.clear()  # Stream one physical cell; retain all its coefficients.
            full_cache[j] = nodal, cell.exact_hermite_controls(x[j], x[j+1], nodal)
        nodal, full_controls = full_cache[j]
        controls = cell.restrict_controls(full_controls, (a-x[j])/(x[j+1]-x[j]), (b-x[j])/(x[j+1]-x[j]))
        lower, upper, scalar_report, branch, middle = scalar.envelope(a, b, args.scalar_degree)
        if args.first_cell_packet is not None and not first_packet_written:
            packet = dict(schema=cell.PACKET_SCHEMA, field_modes=int(saved.M),
                complete_core_coefficients=core, physical_cell=list(map(str, (x[j], x[j+1]))),
                physical_nodal_jets=nodal, check_interval=list(map(str, (a, b))), eta=str(eta),
                scalar_square_envelopes=dict(
                    lower_Bernstein=[cell.exact_endpoint(v.lower()) for v in lower],
                    upper_Bernstein=[cell.exact_endpoint(v.upper()) for v in upper],
                    identity=dict(mathematical_expression_sha256=reconstructed["mathematical_identity_sha256"],
                                  full_scalar_envelope_report=scalar_report)),
                source_identity=identity,
                external_cell_primitive_still_reports_envelope_proof_as_external=True)
            write(args.first_cell_packet, packet)
            first_packet_written = True
        report = cell.certify_cell(controls, b-a, core, lower, upper, eta, int(saved.M),
                                   angular=angular, known_density=density)
        passed = report["certified_under_scalar_envelopes"] and scalar_report["scalar_positive"]
        witness = None
        if not passed:
            value = scalar.value(cell.ball(middle), branch, middle)
            if value > 0:
                witness = cell.point_failure_witness(controls, b-a, core, value, eta,
                                                     int(saved.M), angular)
        if not passed and witness is None and depth < args.max_radial_depth:
            inspect(a, middle, base_index, depth+1)
            if not stopped_for_witness:
                inspect(middle, b, base_index, depth+1)
            return
        row = dict(type="leaf", original_common_cell=base_index, original_physical_cell=j,
            interval=list(map(str, (a, b))), subdivision_depth=depth,
            certified=bool(passed), scalar_envelopes_proved_here=True,
            scalar_envelope=scalar_report, operator=report, actual_point_failure=witness)
        append_record(row)
        compact.append(dict(interval=row["interval"], common_cell=base_index, physical_cell=j,
            depth=depth, certified=bool(passed), point_failure=witness is not None))
        if witness is not None and not args.continue_after_counterexample:
            stopped_for_witness = True

    error = None
    completed_common_cells, attempted_common_cells = [], []
    try:
        for index in range(args.cell_start, stop):
            attempted_common_cells.append(index)
            first_leaf = len(compact)
            inspect(*intervals[index], index, 0)
            leaves_here = compact[first_leaf:]
            if (leaves_here and Q(leaves_here[0]["interval"][0]) == intervals[index][0]
                    and Q(leaves_here[-1]["interval"][1]) == intervals[index][1]):
                completed_common_cells.append(index)
            if (index-args.cell_start) % 10 == 0 or stopped_for_witness:
                print(json.dumps(dict(event="R251_prefix_progress", common_cell=index,
                    total_common_cells=len(intervals), completed_leaf_cells=len(compact),
                    certified_leaf_cells=sum(row["certified"] for row in compact),
                    actual_point_failures=sum(row["point_failure"] for row in compact),
                    seconds=time.monotonic()-begin)), flush=True)
            if stopped_for_witness:
                break
    except Exception as exc:
        error = dict(type=type(exc).__name__, message=str(exc))
        append_record(dict(type="execution_error", error=error))
    leaf_intervals = [(Q(row["interval"][0]), Q(row["interval"][1])) for row in compact]
    covered = bool(leaf_intervals and leaf_intervals[0][0] == cuts[args.cell_start]
        and leaf_intervals[-1][1] == cuts[stop]
        and all(left[1] == right[0] for left, right in zip(leaf_intervals[:-1], leaf_intervals[1:])))
    selected_certified = bool(covered and error is None and all(row["certified"] for row in compact))
    whole_selected = args.cell_start == 0 and stop == len(intervals)
    whole_certified = selected_certified and whole_selected
    result = dict(schema=SCHEMA, theorem="R251", source_sha256=file_sha(__file__),
        primitive_source_sha256=file_sha(cell.__file__), flint_version=flint.__version__,
        working_precision_bits=int(cell.ctx.prec), requested_eta_exact=str(eta),
        input_identity=identity, complete_density_certificate=density,
        scalar_binding=binding, scalar_descriptor_path=str(descriptor_path),
        scalar_descriptor_sha256=file_sha(descriptor_path),
        scalar_envelope_method="Direct same-expression Arb automatic Taylor derivatives; exact polynomial prefix where applicable",
        source_returned_ap_app_substituted_for_finite_Gauss_derivatives=False,
        total_common_cells=len(intervals), requested_common_cell_range=[args.cell_start, stop],
        requested_interval=list(map(str, (cuts[args.cell_start], cuts[stop]))),
        attempted_common_cells=attempted_common_cells,
        completed_common_cells=completed_common_cells, leaf_cells=compact,
        selected_closed_intervals_covered_without_holes=covered,
        selected_prefix_pointwise_operator_certified=selected_certified,
        whole_prefix_pointwise_operator_certified_for_declared_real_expression=whole_certified,
        whole_prefix_pointwise_operator_certified_with_actual_live_constants=
            bool(whole_certified and binding["actual_live_runtime_constants_verified"]),
        actual_failure_witness_present=any(row["point_failure"] for row in compact),
        stopped_after_proved_point_failure=stopped_for_witness, execution_error=error,
        certificate_ledger_path=str(ledger), certificate_ledger_sha256=file_sha(ledger),
        certificate_ledger_records=record_count, full_physical_z0_and_all_modes_retained=True,
        new_metric_fitted=False, literal_floating_evaluator_error_verified=False,
        scalar_C2_interfaces_verified_here=False, angular_or_radial_samples_mislabelled_as_bounds=False,
        original_nonlinear_acceptance_modified=False, nine_jet_machine_gate_added=False,
        tail_caps_and_collar_covered=False, closed_surface_standard4_certified=False,
        task_completed=False, seconds=time.monotonic()-begin)
    write(args.out, result)
    print(json.dumps(dict(event="R251_prefix_complete", output=str(args.out),
        selected_prefix_certified=selected_certified, whole_prefix_certified=whole_certified,
        actual_point_failure=result["actual_failure_witness_present"], error=error,
        seconds=result["seconds"])), flush=True)
    raise SystemExit(0 if selected_certified else 2)


if __name__ == "__main__":
    main()
