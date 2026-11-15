#!/usr/bin/env python3
"""R286 convention-C continuous E with unit-panel six-integral scaling.

All scientific arithmetic runs only in the named public Actions repository.
This is a declared real-integral model, never a relabelled finite selector.
The 160-cell head keeps every original cap/flat/weight expression; the deep
part uses bounds valid for EVERY original exact calibration root in [1/2,2].
No R26 numerical certificate, binary quadrature, nonlinear state or new J is
used. The independent v2 producer preserves the original real expressions,
the original six full-width work goals, and all closed branch/cusp pieces.
Its Acb tolerances are scaled in the units of the restored integral; true
piecewise callbacks report non-holomorphy instead of omitting a branch.
Temporary detailed ledgers are recomputable; retain scripts/parameters,
run identity and hashes under repository Rule15, not these raw ledgers.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction as Q
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import struct
import sys
import time

REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "R286-original-stored-convention-C-continuous-E-cover-v2"
BASE_SOURCE_NAME = "geometry_20261115_stored_continuous_E_cover.py"
BASE_SOURCE_SHA256 = "9aa0da45027afa37ca329eab73e5e93e788f2bbafb908b9e8c2960f537a427ed"
QUERY_SCHEMA = "R286-original-stored-convention-C-closed-queries-v1"
MODEL_SCHEMA = "R286-original-stored-continuous-model-convention-C-v1"
REVISION = "869436630c99aa5a68afb55bd8877c826034d117"
PROOF_SHA = "81d061a6db372a531a119d54298a68d1b9804a7e08fea0fd33bc5fe75a809efb"
PINS = {
    "runtime:tail_frozen_geometry.mjs": "db6664fcd7be618d2b684c39c01c53d97833d11e14af206b12c71e4b058713e3",
    "runtime:strong_frozen_calibration_factory.mjs": "77e9d2fc0e277ef69c9a4300ceba2d3d6b03056fc6a4868fab049a1a1c290247",
    "runtime:closure_bounded_point_cache.mjs": "35289a4de44ec409bc211f82c7a1bee81a10c6bc1c5fb31e4ca9a8634cc09043",
    "runtime:exact_20261114_closed_background.mjs": "be358bf780c88ebd85cdf07d9e8d2cc3b37ca20a4d8ea3a1ba69e7c40c2c4e1b",
    "scripts:closing_weighted_tail.mjs": "740e672edee58cff7a15f89d75e181577dd439c1c62777c57d0d0ab1af32141e",
    "scripts:closing_recalibrated_tail.mjs": "4a109f26b0e6c9741dfff678c0fe42da4935bfda9c605e55688e97848aef0dd6",
    "original:tailnext_balanced_tail.mjs": "928567418f411b70c4040be9ee08be2a78b65e147b8d0c5728f4cf6766a28888",
    "original:general_root_smooth_tail_cells.cjs": "d074799099e27401456449343c8f490ec60cdec7eb0d02758f024f541d409575",
    "original:f6tail_cusp_grid.mjs": "b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f",
}
DEFAULTS = dict(rCut=1.03, wCut=.05, width=.04, curvatureBound=210,
    delta0=.006, R=64, a=2.75, etaPower=1.5, etaRatioAtN0=.05,
    orientation=-1, prefixR=8, prefixEnd=15, prefixReturnStart=8,
    protectCell=80, calibrationSteps=1024, warpSteps=16,
    quadratureTolerance=2e-11, slopeCap=0, capTransition=2,
    capMode="original", cuspAwareQuadrature=True, valleyControls=[],
    rejoinR20At=None, rejoinIndexOffset=4)
GEOMETRY_KEYS = tuple(DEFAULTS) + ("pulseCaps", "valleyCaps", "warpWeightLevels",
    "flatOuterThroughCell", "flatOuterStartSegment", "flatSlope")
DERIVED_KEYS = ("rCuff", "oldCut", "epsilonScale", "prefixRByCell")
SIX_NAMES = ("A", "B", "sqrtE_A", "sqrtE_B", "w_A", "w_B")
MISSING = object()
arb = acb = ctx = fmpq = None


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("Scientific arithmetic only in the named public Actions repository")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"), allow_nan=False)+"\n").encode()


def receipt(path, root=None):
    path = Path(path)
    digest = hashlib.sha256(); count = 0
    with path.open("rb") as stream:
        for raw in iter(lambda: stream.read(1048576), b""):
            digest.update(raw); count += len(raw)
    return dict(file=str(path.relative_to(root)) if root else path.name,
                bytes=count, sha256=digest.hexdigest())


def unique_object(items):
    out = {}
    for key, value in items:
        if key in out:
            raise ValueError("Duplicate JSON key: "+key)
        out[key] = value
    return out


def finite_json_float(token):
    value = float(token)
    if not math.isfinite(value):
        raise ValueError("Nonfinite original JSON number")
    return value


def read_bound(path, expected):
    raw = Path(path).read_bytes()
    if sha(raw) != expected:
        raise ValueError("Actual input SHA differs: "+str(path))
    decoded = gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw
    value = json.loads(decoded, object_pairs_hook=unique_object,
        parse_int=lambda token: -0.0 if token == "-0" else int(token),
        parse_float=finite_json_float,
        parse_constant=lambda token: (_ for _ in ()).throw(ValueError("Nonfinite JSON token")))
    return value, dict(file=Path(path).name, bytes=len(raw), sha256=expected,
        decoded_bytes=len(decoded), decoded_sha256=sha(decoded),
        encoding="gzip-json" if decoded is not raw else "plain-json")


def write_json(path, value):
    raw = canonical(value)
    with Path(path).open("xb") as stream:
        stream.write(raw); stream.flush(); os.fsync(stream.fileno())
    return dict(file=Path(path).name, bytes=len(raw), sha256=sha(raw))


class Journal:
    def __init__(self, path, root):
        self.path, self.root = Path(path), Path(root)
        self.stream = self.path.open("xb")
        self.hash = hashlib.sha256(); self.bytes = self.rows = 0

    def add(self, value):
        raw = canonical(value)
        self.stream.write(raw); self.stream.flush()
        self.hash.update(raw); self.bytes += len(raw); self.rows += 1

    def finish(self):
        if not self.stream.closed:
            self.stream.flush(); os.fsync(self.stream.fileno()); self.stream.close()
        return dict(file=str(self.path.relative_to(self.root)), bytes=self.bytes,
                    rows=self.rows, sha256=self.hash.hexdigest())


def numeric(value):
    return type(value) in (int, float) and math.isfinite(value)


def same(a, b):
    if a is MISSING or b is MISSING:
        return a is b
    if numeric(a) or numeric(b):
        return numeric(a) and numeric(b) and struct.pack("<d", a) == struct.pack("<d", b)
    if type(a) is not type(b):
        return False
    if isinstance(a, list):
        return len(a) == len(b) and all(same(x, y) for x, y in zip(a, b))
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(same(a[k], b[k]) for k in a)
    return a == b


def normal(value):
    out = dict(DEFAULTS); out.update(value)
    if out.get("warpWeightLevels") is None:
        out["warpWeightLevels"] = []
    return out


def compare_geometry(a, b, label):
    a, b = normal(a), normal(b)
    for key in GEOMETRY_KEYS:
        if not same(a.get(key, MISSING), b.get(key, MISSING)):
            raise ValueError(label+": original geometry differs at "+key)


def ready(value):
    return value.get("ready", value)


def rat(value):
    if type(value) is bool:
        raise ValueError("A Boolean is not a rational endpoint")
    if type(value) is float:
        if not math.isfinite(value):
            raise ValueError("Nonfinite scalar")
        return Q.from_float(value)
    if type(value) is int:
        return Q(value)
    if isinstance(value, str):
        return Q(value)
    raise ValueError("Use an exact rational string or an original finite JSON number")


def bind_inputs(args):
    base_source = receipt(Path(__file__).with_name(BASE_SOURCE_NAME))
    if base_source["sha256"] != BASE_SOURCE_SHA256:
        raise ValueError("The preserved original convention-C producer source differs")
    config, config_receipt = read_bound(args.config, args.config_sha256)
    ledger, ledger_receipt = read_bound(args.ledger_ready, args.ledger_ready_sha256)
    stored, stored_receipt = read_bound(args.stored_ready, args.stored_ready_sha256)
    ledger, stored = ready(ledger), ready(stored)
    model = ledger["rationalDeepModel"]
    table = ledger["shallowSourceParameters"]
    old = stored["storedMetricAdapter"]
    p = model["physicalParameters"]
    if (model["sourceRevision"] != REVISION or model["start"] != 160
            or old["sourceRevision"] != REVISION or old["cellCount"] != 160
            or len(table["cells"]) != 160):
        raise ValueError("The actual original 160-cell ledger/stored source is required")
    compare_geometry(config, p, "Config/ledger")
    compare_geometry(old["physicalParameters"], p, "Stored/ledger")
    for key in DERIVED_KEYS:
        if not same(old["physicalParameters"][key], p[key]):
            raise ValueError("Original derived parameter differs: "+key)
    lam = model["frozenWarpAlpha"]
    if not numeric(lam) or lam <= 0 or not same(lam, old["frozenWarpAlpha"]):
        raise ValueError("The original positive saved global warp coefficient differs")
    if (old["profileFingerprintBefore"] != old["profileFingerprintAfter"]
            or old["fingerprintFields"] != ["r", "drdx", "logw", "dlogwdx"]
            or old["fingerprintFractions"] != [0, .125, .25, .5, .75, .875, 1]):
        raise ValueError("The stored reference did not preserve its own original source")
    for value in (old["profileFingerprintAfter"], model["headFingerprint"]):
        if (not isinstance(value, str) or len(value) != 64
                or any(c not in "0123456789abcdef" for c in value)):
            raise ValueError("Keep both actual historical source fingerprint identities")
    if (p["orientation"] != 1 or p["protectCell"] != 160
            or p.get("rejoinR20At") is not None or p["a"] != 2.75
            or p["etaPower"] != 1.5 or p["R"] != 64
            or not p["protectCell"] > p["prefixEnd"]+2):
        raise ValueError("This R286 interpretation requires the actual outward unrejoined source")
    rows = []
    for n, row in enumerate(table["cells"]):
        if row["n"] != n:
            raise ValueError("The original calibration table is not complete and ordered")
        for key in ("delta", "R", "c", "lengthScale", "alpha"):
            if not numeric(row[key]) or row[key] <= 0:
                raise ValueError("Invalid original calibration scalar")
        if row["lengthScale"] != 1:
            raise ValueError("R286 does not silently change a nonunit source lengthScale")
        rows.append({key:row[key] for key in ("n", "delta", "R", "c", "lengthScale", "alpha")})
    for key in ("rCuff", "oldCut", "epsilonScale", "delta0", "etaRatioAtN0",
                "rCut", "curvatureBound", "capTransition"):
        if not numeric(p[key]) or p[key] <= 0:
            raise ValueError("A required original positive finite parameter is absent: "+key)
    origin = args.source_topic/"source-origin.json"
    origin_raw = origin.read_bytes(); source_origin = json.loads(origin_raw)
    if source_origin["source_revision"] != REVISION:
        raise ValueError("Original source-topic revision differs")
    roots = dict(runtime=args.runtime_computations, scripts=args.source_topic/"scripts",
        original=args.source_topic/"repro/source-root/topics/large-amplitude-twist-flex/scripts")
    sources = {}
    for key, expected in PINS.items():
        kind, name = key.split(":", 1); path = roots[kind]/name
        desc = receipt(path)
        if desc["sha256"] != expected:
            raise ValueError("Original formula source differs: "+name)
        sources[key] = desc
    for name, key in (("weighted", "scripts:closing_weighted_tail.mjs"),
                      ("cells", "original:general_root_smooth_tail_cells.cjs")):
        if model["sourceHashes"][name] != PINS[key]:
            raise ValueError("Ledger formula source differs")
    if old["sourceSHA256"]["weighted"] != PINS["scripts:closing_weighted_tail.mjs"]:
        raise ValueError("Stored weighted source differs")
    proof_receipt = receipt(args.proof)
    if proof_receipt["sha256"] != PROOF_SHA:
        raise ValueError("The R286 proof text differs from this source contract")
    requested = None; query_receipt = None
    if args.queries is not None:
        requested, query_receipt = read_bound(args.queries, args.queries_sha256)
        if requested.get("schema") != QUERY_SCHEMA or not requested.get("queries"):
            raise ValueError("Use the declared convention-C closed-query schema")
        if requested.get("config_sha256") != config_receipt["sha256"]:
            raise ValueError("The closed-query plan must bind the actual configuration")
        for key, expected in (("calibration_ledger_sha256", ledger_receipt["sha256"]),
                              ("stored_reference_sha256", stored_receipt["sha256"]),
                              ("original_profile_fingerprint", old["profileFingerprintAfter"])):
            if key in requested and requested[key] != expected:
                raise ValueError("The optional query source identity differs: "+key)
    root_conditions = dict(
        positive_delta0=rat(p["delta0"]) > 0,
        delta0_at_most_one_tenth=rat(p["delta0"]) <= Q(1, 10),
        positive_c0=rat(p["etaRatioAtN0"]) > 0,
        c0_at_most_one_sixteenth=rat(p["etaRatioAtN0"]) <= Q(1, 16),
        deep_start=160, R=64,
        proof="R286 (286.22)-(286.24): B<2^-63<33 for every n>=160")
    root_proved = all(root_conditions[k] for k in ("positive_delta0",
        "delta0_at_most_one_tenth", "positive_c0", "c0_at_most_one_sixteenth"))
    convention = dict(schema=MODEL_SCHEMA,
        explicit_model_layer_choice=True,
        binary_inputs_are_exact_dyadics=True,
        dependent_delta_c_mu_and_radius_are_real_relations_not_independent_rounded_words=True,
        shallow_alpha_and_R_are_original_saved_dyadics=True,
        global_lambda_reselected=False, natural_outer_radius_reidentified_as_nominal_cut=False,
        deep_definition=args.deep_definition,
        deep_bounds_valid_for_every_original_root_in_half_to_two=True,
        deep_roots_numerically_selected_or_computed=False,
        root_existence_proved=root_proved, root_conditions=root_conditions,
        available_unselected_root_rule_reference="R286 section286.8 fixed dovetailed rational middle-third rule",
        old_finite_selector_certified_as_this_continuous_model=False,
        R26_rational_deep_or_numerical_certificate_used=False)
    binding = dict(schema=SCHEMA+"-input-binding", source_sha256=sha(Path(__file__).read_bytes()),
        preserved_original_producer_source=base_source,
        integral_strategy="unit-panel-normalisation-and-complete-piecewise-Acb-callback-v2",
        original_six_full_width_goal_unchanged=True,
        original_real_profile_and_model_C_unchanged=True,
        config=config_receipt, calibration_ledger=ledger_receipt,
        stored_reference=stored_receipt, original_source_origin=receipt(origin),
        original_sources=sources, proof=proof_receipt,
        original_source_revision=REVISION, physical_parameters=p,
        original_frozen_warp_alpha=lam, original_shallow_rows=rows,
        original_profile_fingerprint=old["profileFingerprintAfter"],
        original_finite_head_fingerprint=model["headFingerprint"],
        historical_fingerprints_recomputed_by_this_producer=False,
        original_calibration_table_interpretation=table.get("interpretation"),
        query_input=query_receipt, convention=convention,
        original_factory_or_selector_imported=False, actual_accepted_field_supplied=False)
    return p, rows, lam, requested, binding


def initialise_math(bits):
    require_actions()
    global arb, acb, ctx, fmpq
    import flint
    from flint import arb, acb, ctx, fmpq
    if flint.__version__ != "0.9.0":
        raise RuntimeError("Use the explicit python-flint==0.9.0 runtime")
    ctx.prec = bits
    return dict(python=sys.version, python_flint=flint.__version__, precision_bits=bits)


def exact(value):
    q = value if isinstance(value, Q) else rat(value)
    return arb(fmpq(q.numerator, q.denominator))


def p2(exponent):
    return arb((1, exponent))


def interval(lo, hi):
    return exact(lo).union(exact(hi))


def hull(values):
    values = list(values)
    if not values:
        raise ArithmeticError("An enclosure has no possible branch")
    out = values[0]
    for value in values[1:]:
        out = out.union(value)
    return out


def dyadic(value):
    m, e = value.man_exp()
    return dict(mantissa=str(m), binary_exponent=int(e))


def record(value):
    if not value.is_finite():
        raise ArithmeticError("A nonfinite ball is not a certified enclosure")
    return dict(lower=dyadic(value.lower()), upper=dyadic(value.upper()), display=str(value))


def is_narrow(value, goal):
    return value.is_finite() and value.upper()-value.lower() <= goal


@dataclass(frozen=True)
class Jet2:
    value: object
    first: object
    second: object

    @staticmethod
    def lift(value):
        return value if isinstance(value, Jet2) else Jet2(value, 0, 0)

    def __add__(self, other):
        other = self.lift(other)
        return Jet2(self.value+other.value, self.first+other.first, self.second+other.second)

    __radd__ = __add__

    def __neg__(self):
        return Jet2(-self.value, -self.first, -self.second)

    def __sub__(self, other):
        return self+-self.lift(other)

    def __rsub__(self, other):
        return self.lift(other)+-self

    def __mul__(self, other):
        other = self.lift(other)
        return Jet2(self.value*other.value,
            self.first*other.value+self.value*other.first,
            self.second*other.value+2*self.first*other.first+self.value*other.second)

    __rmul__ = __mul__

    def __truediv__(self, constant):
        if isinstance(constant, Jet2):
            raise TypeError("Only constant division is used by the complete log-profile")
        return Jet2(self.value/constant, self.first/constant, self.second/constant)

    def __pow__(self, exponent):
        if type(exponent) is not int or exponent < 0:
            raise TypeError("The profile polynomial requires a nonnegative integer power")
        out = Jet2.lift(1)
        for _ in range(exponent):
            out = out*self
        return out

    def exp(self):
        value = self.value.exp()
        return Jet2(value, value*self.first, value*(self.first*self.first+self.second))


def smooth(x):
    return x*x*x*(10+x*(-15+6*x))


def cap_primitive(x):
    return x**5*(7+x*(-14+x*(10-x*exact(Q(5, 2)))))


class ResourceStop(Exception):
    pass


class WorkBudget:
    def __init__(self, args):
        self.started = time.monotonic(); self.seconds = args.budget_seconds
        self.max_panels = args.max_panels; self.max_query_nodes = args.max_query_nodes
        self.panels = self.query_nodes = self.integral_calls = 0

    def check(self):
        if time.monotonic()-self.started >= self.seconds:
            raise ResourceStop("Declared wall-clock resource budget reached")

    def panel(self):
        self.check()
        if self.panels >= self.max_panels:
            raise ResourceStop("Declared complete integral-panel resource budget reached")
        self.panels += 1

    def query(self):
        self.check()
        if self.query_nodes >= self.max_query_nodes:
            raise ResourceStop("Declared inverse-cover node resource budget reached")
        self.query_nodes += 1


def intersect_known(value, lower, upper):
    """Intersect a computed enclosure with a proved scalar range."""
    lower = lower if hasattr(lower, "lower") else exact(lower)
    upper = upper if hasattr(upper, "upper") else exact(upper)
    a = max(value.lower(), lower.lower())
    b = min(value.upper(), upper.upper())
    if a > b:
        raise ArithmeticError("Two enclosures of the same real quantity are disjoint")
    return a.union(b)


def smooth_jet(x, bounds=None):
    value = smooth(x)
    first = 30*x*x*(1-x)*(1-x)
    second = 60*x*(1-x)*(1-2*x)
    if bounds is not None:
        lo, hi = bounds
        # S is monotone on [0,1]; its derivatives have these exact coarse bounds.
        value = intersect_known(value, smooth(exact(lo)), smooth(exact(hi)))
        first = intersect_known(first, 0, Q(15, 8))
        second = intersect_known(second, -15, 15)
    return Jet2(value, first, second)


def item(values, index, default):
    if values is None or index >= len(values) or values[index] is None:
        return default
    return values[index]


def js_truthy(value):
    if value is None or value is False:
        return False
    if type(value) in (int, float):
        return value != 0 and not math.isnan(value)
    if isinstance(value, str):
        return bool(value)
    return True


class Piece:
    def __init__(self, head, n, j, length, log_r0, log_mu, log_p0, jump):
        self.head, self.n, self.j = head, n, j
        self.index = (159-n)*9+j
        self.length, self.log_r0, self.log_mu = length, log_r0, log_mu
        self.log_p0, self.jump = log_p0, jump
        p = head.p
        self.beta = exact(item(p.get("valleyControls", []), n, 0))
        self.cap_on = numeric(p["slopeCap"]) and p["slopeCap"] > 0
        base_cap = p["slopeCap"]
        pulse = item(p.get("pulseCaps", []), n, None)
        valley = item(p.get("valleyCaps", []), n, None)
        levels = [base_cap]*5
        if self.cap_on and (js_truthy(pulse) or js_truthy(valley)):
            levels = [base_cap, item(pulse, 0, base_cap),
                      base_cap if valley is None else valley,
                      item(pulse, 1, base_cap), base_cap]
        if self.cap_on and any(not numeric(v) or v <= 0 for v in levels):
            raise ValueError("The declared continuous log-cap needs the actual positive layer values")
        self.cap_values = levels
        self.caps = [exact(v).log() for v in levels] if self.cap_on else None
        self.weights = item(p.get("warpWeightLevels", []), n, [1]*5)
        if (len(self.weights) != 5 or self.weights[0] != 1 or self.weights[4] != 1
                or any(not numeric(v) or v <= 0 for v in self.weights)):
            raise ValueError("Keep all original positive weights and both unit port weights")
        last, slope = p.get("flatOuterThroughCell"), p.get("flatSlope")
        self.flat_enabled = (numeric(last) and int(last) == last and last >= 0
                             and numeric(slope) and slope > 0)
        self.flat_last = last
        self.flat_start = p.get("flatOuterStartSegment", 2)
        if self.flat_start is None:
            self.flat_start = 2
        self.flat_log = exact(slope).log() if self.flat_enabled else None
        self.flat_full = (self.flat_enabled and
            (n < last or (n == last and j > self.flat_start)))
        self.flat_transition = self.flat_enabled and n == last and j == self.flat_start
        self.cut_preserving = p.get("capMode") == "cut-preserving"

    def descriptor(self):
        return dict(index=self.index, original_cell=self.n, original_segment=self.j,
            x_interval=["0", "1"], original_order="cell159..0, segment0..8",
            real_source_length=record(self.length),
            cap_enabled=self.cap_on, cap_layer_values=self.cap_values if self.cap_on else None,
            positive_weight_levels=self.weights, flat_full=self.flat_full,
            flat_transition=self.flat_transition, cut_preserving=self.cut_preserving)

    def raw_and_cap(self, x, bounds=None):
        S = smooth_jet(x, bounds)
        X = Jet2(x, 1, 0)
        raw = (S*self.jump+(self.log_mu+self.log_p0)
               -(X*self.length/self.head.sqrt12+self.log_r0)*7)
        if self.j == 3:
            raw = raw+S*self.beta
        elif self.j == 4:
            raw = raw+self.beta
        elif self.j == 5:
            raw = raw+(1-S)*self.beta
        cap = None
        if self.cap_on:
            if self.j % 2 == 0:
                cap = Jet2.lift(self.caps[self.j//2])
            else:
                k = (self.j-1)//2
                jump = (exact(0) if self.cap_values[k+1] == self.cap_values[k]
                        else (exact(self.cap_values[k+1])/exact(self.cap_values[k])).log())
                cap = S*jump+self.caps[k]
        return raw, cap, S

    def possible_branches(self, lo, hi):
        if self.cut_preserving and self.n == 0 and self.j == 8:
            return ["raw"]
        if self.flat_full:
            return ["cap-overwritten-by-flat"]
        if not self.cap_on:
            return ["raw"]
        raw, cap, _ = self.raw_and_cap(interval(lo, hi), (lo, hi))
        z = raw.value-cap.value; L = self.head.cap_L
        out = []
        if not z > -L:
            out.append("raw")
        if not z < L:
            out.append("cap")
        if not (z < -L or z > 0):
            out.append("transition-low")
        if not (z < 0 or z > L):
            out.append("transition-high")
        if not out:
            raise ArithmeticError("No possible true cap branch")
        return out

    def log_profile(self, x, branch, bounds=None):
        raw, cap, S = self.raw_and_cap(x, bounds)
        if branch in ("raw", "cap-overwritten-by-flat"):
            g = raw
        elif branch == "cap":
            g = cap
        elif branch == "transition-low":
            t = (raw-cap+self.head.cap_L)/(2*self.head.cap_L)
            g = raw-cap_primitive(t)*(2*self.head.cap_L)
        elif branch == "transition-high":
            u = (cap+self.head.cap_L-raw)/(2*self.head.cap_L)
            g = cap-cap_primitive(u)*(2*self.head.cap_L)
        else:
            raise ValueError("Unknown real cap branch")
        if self.flat_full:
            g = Jet2.lift(self.flat_log)
        elif self.flat_transition:
            g = g+S*(-g+self.flat_log)
        # Preserve the original later overwrites; no flat early-return.
        if self.cut_preserving and self.n == 0 and self.j == 8:
            g = raw
        elif self.cut_preserving and self.n == 0 and self.j == 7:
            g = raw+(1-S)*(g-raw)
        return g, S

    def weight(self, S):
        if self.j % 2 == 0:
            return Jet2.lift(exact(self.weights[self.j//2]))
        k = (self.j-1)//2
        jump = (exact(0) if self.weights[k+1] == self.weights[k]
                else (exact(self.weights[k+1])/exact(self.weights[k])).log())
        return (S*jump+exact(self.weights[k]).log()).exp()

    def expression(self, x, branch, sign=None, bounds=None, analytic=False,
                   derivatives=True):
        g, S = self.log_profile(x, branch, bounds)
        w = g.exp(); E = 1+w.value*w.value
        if isinstance(E, acb):
            root = E.sqrt(analytic=analytic)
        else:
            E = intersect_known(E, 1, E.upper())
            root = E.sqrt()
        ro = (self.log_r0+self.length*x/self.head.sqrt12).exp()
        rx = self.length*ro/self.head.sqrt12
        chi, j0 = Jet2.lift(1), Jet2.lift(1)
        if self.n == 159 and self.j == 0:
            chi = S
        if self.n == 0 and self.j == 8:
            chi = 1-S
            j0 = S*(self.head.cut_ratio-1)+1
            if bounds is not None:
                j0 = Jet2(intersect_known(j0.value,
                    min(exact(1), self.head.cut_ratio.lower()),
                    max(exact(1), self.head.cut_ratio.upper())), j0.first, j0.second)
        weight = self.weight(S)
        q = w.first
        magnitude = abs(q) if sign is None else sign*q
        if bounds is not None:
            magnitude = intersect_known(magnitude, 0, magnitude.upper())
        A = rx*j0.value*(1-chi.value)+chi.value*magnitude/(self.head.K*E*root)
        B = chi.value*rx*weight.value/E
        six = [A, B, root*A, root*B, w.value*A, w.value*B]
        out = dict(six=six, w=w.value, E=E, logw=g.value,
                   q=q, raw_radius=ro, source_log_first=g.first)
        if not derivatives:
            return out
        if bounds is None:
            raise ValueError("Radial derivative ranges require a real closed panel")
        Ep = 2*w.value*q
        U = (1-chi.value)*j0.value+self.head.lam*chi.value*weight.value/E
        b = rx*U
        b_lower = rx.lower()*min(j0.value.lower() if hasattr(j0.value, "lower") else exact(j0.value),
            (self.head.lam*weight.value/E).lower())
        b = intersect_known(b, b_lower, b.upper())
        bp = (self.length/self.head.sqrt12)*b + rx*(
            -chi.first*j0.value+(1-chi.value)*j0.first
            +self.head.lam*((chi.first*weight.value+chi.value*weight.first)/E
                           -chi.value*weight.value*Ep/(E*E)))
        c = chi.value/(self.head.K*E*root)
        c = intersect_known(c, 0, c.upper())
        cp = (chi.first/(self.head.K*E*root)
              -3*chi.value*w.value*q/(self.head.K*E*E*root))
        D = b+c*magnitude
        D = intersect_known(D, b_lower, D.upper())
        if not D > 0:
            raise ArithmeticError("The complete panel lost the proved positive true radial speed")
        wr = q/D
        wrr = (b*w.second-q*bp-q*cp*abs(q))/(D**3)
        out.update(radial_speed=D, w_r=wr, w_rr=wrr,
                   E_r=2*w.value*wr, E_rr=2*(wr*wr+w.value*wrr))
        return out

    def range(self, lo, hi):
        branches = self.possible_branches(lo, hi)
        values = [self.expression(interval(lo, hi), branch, bounds=(lo, hi))
                  for branch in branches]
        keys = ("w", "E", "q", "radial_speed", "w_r", "w_rr", "E_r", "E_rr")
        out = {key:hull(v[key] for v in values) for key in keys}
        out["six"] = [hull(v["six"][k] for v in values) for k in range(6)]
        out["branches"] = branches
        if any(not value.is_finite() for key, value in out.items()
               if key not in ("six", "branches")) or any(not v.is_finite() for v in out["six"]):
            raise ArithmeticError("Nonfinite complete real-expression range")
        return out

    def analytic_kind(self, lo, hi):
        branches = self.possible_branches(lo, hi)
        if len(branches) != 1:
            return None
        branch = branches[0]
        g, _ = self.log_profile(interval(lo, hi), branch, (lo, hi))
        q = g.first
        sign = 1 if q > 0 else -1 if q < 0 else 0 if q == 0 else None
        return (branch, sign) if sign is not None else None


def complex_cap_branches(piece, x):
    """All possible branches of the real-part piecewise extension.

    This is used only when the ORIGINAL REAL panel crosses a possible cap
    boundary. If a whole real panel has one branch, its analytic extension
    can instead be used on a complex ellipse around that panel. Neither
    path assumes that an uncertain branch boundary has disappeared.
    """
    if piece.cut_preserving and piece.n == 0 and piece.j == 8:
        return ["raw"]
    if piece.flat_full:
        return ["cap-overwritten-by-flat"]
    if not piece.cap_on:
        return ["raw"]
    raw, cap, _ = piece.raw_and_cap(x)
    z = (acb(raw.value)-acb(cap.value)).real
    L = piece.head.cap_L
    out = []
    if not z > -L:
        out.append("raw")
    if not z < L:
        out.append("cap")
    if not (z < -L or z > 0):
        out.append("transition-low")
    if not (z < 0 or z > L):
        out.append("transition-high")
    return out


def branch_integrand_component(piece, x, branch, component, analytic, stats):
    """The ORIGINAL six real functions, extended only as needed by Acb.

    The odd components contain no |w_x| and are not blocked by its zero.
    The even components use real_abs(analytic=...), not complex modulus.
    All complete cap, flat, valley, weight and cut overwrites are inherited
    from Piece.log_profile / Piece.weight without changing those methods.
    """
    g, S = piece.log_profile(x, branch)
    w = acb(g.value).exp()
    E = 1+w*w
    ro = (piece.log_r0+piece.length*x/piece.head.sqrt12).exp()
    rx = piece.length*ro/piece.head.sqrt12
    chi, j0 = acb(1), acb(1)
    if piece.n == 159 and piece.j == 0:
        chi = acb(S.value)
    if piece.n == 0 and piece.j == 8:
        chi = 1-S.value
        j0 = S.value*(piece.head.cut_ratio-1)+1
    if component in (1, 3, 5):
        B = chi*rx*piece.weight(S).value/E
        if component == 1:
            return B
        if component == 3:
            return E.sqrt(analytic=analytic)*B
        return w*B
    q = w*acb(g.first)
    magnitude = q.real_abs(analytic=analytic)
    if analytic and not magnitude.is_finite():
        stats["analytic_absolute_value_nonholomorphic_callbacks"] += 1
    root = E.sqrt(analytic=analytic)
    A = rx*j0*(1-chi)+chi*magnitude/(piece.head.K*E*root)
    if component == 0:
        return A
    if component == 2:
        return root*A
    if component == 4:
        return w*A
    raise ValueError("The complete six-component index is outside 0..5")


def complete_integrand_component(piece, x, component, analytic, real_branches,
                                 legacy_kind, stats):
    if legacy_kind is not None:
        # An analytic extension of a branch that agrees on the entire real
        # integration panel is sufficient; it need not retain the global
        # piecewise formula outside that panel on the real axis.
        branch, sign = legacy_kind
        return piece.expression(x, branch, sign=sign, analytic=analytic,
                                derivatives=False)["six"][component]
    branches = real_branches if len(real_branches) == 1 else complex_cap_branches(piece, x)
    if analytic and len(branches) != 1:
        stats["analytic_cap_nonholomorphic_callbacks"] += 1
        return acb("nan")
    if not branches:
        return acb("nan")
    values = [acb(branch_integrand_component(piece, x, branch, component, analytic, stats))
              for branch in branches]
    # With analytic=False this includes every possible original branch at
    # every real point in the entire supplied ball, including boundaries.
    return hull(values)


class ContinuousHead:
    def __init__(self, p, rows, lam, binding):
        require_actions()
        self.p, self.rows, self.binding = normal(p), rows, binding
        self.rc, self.d0, self.c0, self.eps = map(exact,
            (p["rCuff"], p["delta0"], p["etaRatioAtN0"], p["epsilonScale"]))
        self.lam, self.K, self.cap_L = map(exact, (lam, p["curvatureBound"], p["capTransition"]))
        self.sqrt12, self.log2 = arb(12).sqrt(), arb(2).log()
        self.a = exact(Q(11, 4)); self.rho = (self.a*self.log2).exp()
        self.q32 = (-exact(Q(3, 2))*self.log2).exp()
        self.cut_ratio = exact(p["rCut"])/exact(p["oldCut"])
        self.pieces = []
        shape = ((0,0,"c"),(0,1,"c"),(1,1,"one"),(1,2,"c"),(2,2,"one"),
                 (2,3,"c"),(3,3,"one"),(3,4,"c"),(4,4,"c"))
        for n in range(159, -1, -1):
            delta = self.d0*p2(-n)
            c = self.c0*(-exact(Q(n, 2))*self.log2).exp()
            after = 3*delta+6*self.c0*self.d0*self.q32**(n+1)/(1-self.q32)
            log_r = self.rc.log()+after/self.sqrt12
            log_mu = self.eps.log()+self.a*delta.log()
            row = rows[n]
            logs = (exact(0), exact(row["R"]).log()-delta.log(),
                    delta.log()-exact(row["alpha"]).log(), -delta.log(), self.a*self.log2)
            offset = exact(0)
            for j, (lo, hi, length_kind) in enumerate(shape):
                length = delta*(c if length_kind == "c" else 1)
                jump = exact(0) if lo == hi else logs[hi]-logs[lo]
                self.pieces.append(Piece(self, n, j, length,
                    log_r+offset/self.sqrt12, log_mu, logs[lo], jump))
                offset += length
        delta159 = self.d0*p2(-159)
        after159 = 3*delta159+6*self.c0*self.d0*self.q32**160/(1-self.q32)
        self.inner_radius = self.rc*(after159/self.sqrt12).exp()

    def deep_cover(self):
        if not self.binding["convention"]["root_existence_proved"]:
            return None
        n = 160; delta = self.d0*p2(-n)
        eta = self.c0*self.d0*(-exact(Q(3*n, 2))*self.log2).exp()
        W = self.eps*64/self.rc**7*(exact(Q(7, 4))*delta.log()).exp()
        H = (128/(delta*delta)).log()
        L = exact(Q(15, 8))*H/eta+7/self.sqrt12
        M = 15*H/(eta*eta)
        # H_(n+k) <= (k+1) H_n. The positive series below dominate every
        # deep-cell term, not merely the first cell or a finite sample.
        if not H >= 2*self.log2:
            raise ArithmeticError("The analytic all-deep derivative-series premise is unresolved")
        q = (-self.log2/2).exp()
        S1 = 1/(1-q)**2
        S2 = (1+q)/(1-q)**3
        derivative1 = 2*self.sqrt12/self.rc*W*W*L/(1-exact(Q(1, 4)))**2
        derivative2 = W*W/self.rc**2*(48*L*L*S2+24*M*S1
                         +2*self.sqrt12*L/(1-exact(Q(1, 4)))**2)
        width = self.inner_radius-self.rc
        E = exact(1).union(1+W*W)
        six = [width, exact(0), width.union(width*(1+W*W).sqrt()), exact(0),
               exact(0).union(W*width), exact(0)]
        return dict(E=E, E_r=(-derivative1).union(derivative1),
            E_rr=(-derivative2).union(derivative2), w=exact(0).union(W),
            radius_left=self.rc, radius_right=self.inner_radius, six=six,
            root_values_computed=False, all_admissible_root_choices=True,
            source_cells=dict(first=160, stop="infinity"),
            formulas="R286 (286.25)-(286.30), with positive geometric-series derivative bounds")

    def protected_join(self):
        piece = self.pieces[0]
        raw, cap, _ = piece.raw_and_cap(exact(0), (Q(0), Q(0)))
        cap_raw = not piece.cap_on or raw.value-cap.value < -self.cap_L
        flat_preserves = not piece.flat_full
        # If this is the flat transition at x=0, S,S',S'' all vanish;
        # thus the same endpoint two-jet is retained without deleting it.
        proved = bool(cap_raw and flat_preserves)
        actual = [piece.log_profile(exact(0), branch, (Q(0), Q(0)))[0]
                  for branch in piece.possible_branches(Q(0), Q(0))]
        differences = [hull((g.value-raw.value) for g in actual),
                       hull((g.first-raw.first) for g in actual),
                       hull((g.second-raw.second) for g in actual)]
        return dict(proved=proved, cap_is_structurally_raw_at_protect_endpoint=bool(cap_raw),
            full_flat_override_absent=bool(flat_preserves),
            possible_flat_transition_has_zero_first_two_endpoint_jets=piece.flat_transition,
            log_slope_two_jet_difference=[record(v) for v in differences],
            chi_value_and_first_derivative_zero_by_original_quintic=True,
            schema_or_finite_fingerprint_used_as_C2_proof=False,
            unpaid_reason=None if proved else "Actual protected slope two-jet compatibility not proved")


def range_record(box):
    return {key:record(box[key]) for key in
            ("w", "E", "radial_speed", "w_r", "w_rr", "E_r", "E_rr")}


class SixPrimitiveIntegrator:
    def __init__(self, head, args, budget, ledger, unpaid):
        self.head, self.args, self.budget = head, args, budget
        self.ledger, self.unpaid = ledger, unpaid
        self.absolute = p2(-args.integral_absolute_bits)
        self.relative = p2(-args.integral_relative_bits)
        self.all_work_goals_met = True
        self.guard = p2(-args.analytic_guard_bits)
        self.diagnostics = dict(real_range_failures=0, real_range_goal_passes=0,
            analytic_panels_attempted=0, analytic_components_attempted=0,
            analytic_components_finite=0, analytic_components_fallback=0,
            legacy_whole_panel_gate_satisfied=0, legacy_gate_bypassed_for_cap=0,
            legacy_gate_bypassed_for_derivative_sign=0,
            analytic_cap_nonholomorphic_callbacks=0,
            analytic_absolute_value_nonholomorphic_callbacks=0,
            restored_six_goals_passes=0, subdivided_after_restored_goal_failure=0,
            coarse_valid_panels_at_maximum_depth=0,
            complete_accepted_panels=0,
            failed_component_full_width_goals=[0]*6)
        self.last_panel = None
        self.last_component_attempts = []

    def goal_met(self, values, width):
        for value in values:
            size = max(abs(value.lower()), abs(value.upper()))
            if not is_narrow(value, self.absolute*exact(width)+self.relative*size):
                return False
        return True

    def goal_records(self, values, width):
        rows = []
        for k, value in enumerate(values):
            size = max(abs(value.lower()), abs(value.upper()))
            goal = self.absolute*exact(width)+self.relative*size
            full_width = value.upper()-value.lower()
            rows.append(dict(component=SIX_NAMES[k], enclosure=record(value),
                full_width=record(full_width), complete_work_goal=record(goal),
                full_width_goal_met=bool(is_narrow(value, goal))))
        return rows

    def analytic_integrals(self, piece, lo, hi, kind, ranges, real_branches):
        values = []
        length, start = exact(hi-lo), exact(lo)
        if not length > 0:
            raise ArithmeticError("A unit-panel map requires a positive original interval")
        self.last_component_attempts = []
        self.diagnostics["analytic_panels_attempted"] += 1
        if kind is not None:
            self.diagnostics["legacy_whole_panel_gate_satisfied"] += 1
        elif len(real_branches) != 1:
            self.diagnostics["legacy_gate_bypassed_for_cap"] += 1
        else:
            self.diagnostics["legacy_gate_bypassed_for_derivative_sign"] += 1
        for k in range(6):
            self.budget.check()
            bound = ranges[k]
            if bound == 0:
                values.append(exact(0))
                self.last_component_attempts.append(dict(component=SIX_NAMES[k],
                    identically_zero_from_complete_real_range=True))
                continue
            scale = max(abs(bound.lower()), abs(bound.upper()))
            if not scale > 0:
                raise ArithmeticError("No strictly positive analytic normalisation scale")
            # J=integral_0^1 f(lo+length*t)/scale dt, I=length*scale*J.
            # Thus an absolute error epsA/scale in J has ORIGINAL units
            # epsA*length after recovery. Guard bits are work margins, not
            # a theorem that Acb's total error meets the final full-width goal.
            abs_tol = self.absolute*self.guard/scale
            rel_tol = self.relative*self.guard
            attempt = dict(component=SIX_NAMES[k], original_interval_length=record(length),
                normalisation_scale=record(scale), unit_interval=["0", "1"],
                requested_absolute_tolerance=record(abs_tol),
                requested_relative_tolerance=record(rel_tol),
                original_full_width_goal_rechecked_after_recovery=True)
            self.last_component_attempts.append(attempt)

            def callback(t, analytic):
                self.budget.check()
                x = start+length*t
                return complete_integrand_component(piece, x, k, analytic,
                    real_branches, kind, self.diagnostics)/scale

            self.diagnostics["analytic_components_attempted"] += 1
            try:
                value = acb.integral(callback, acb(0), acb(1),
                    rel_tol=rel_tol, abs_tol=abs_tol,
                    deg_limit=64, eval_limit=self.args.integral_evaluation_limit,
                    depth_limit=40)
                self.budget.integral_calls += 1
                if not value.is_finite() or not value.imag.contains(0):
                    raise ArithmeticError("Unit-panel integral did not certify a finite real enclosure")
                recovered = length*scale*value.real
                values.append(recovered)
                attempt.update(finite_real_enclosure=True,
                    recovered_full_width=record(recovered.upper()-recovered.lower()))
                self.diagnostics["analytic_components_finite"] += 1
            except ResourceStop:
                raise
            except (ArithmeticError, ValueError, ZeroDivisionError, OverflowError) as error:
                # Preserve all successful components and the complete valid
                # real-range integral for this one; no primitive is dropped.
                values.append(length*bound)
                attempt.update(finite_real_enclosure=False,
                    complete_real_range_fallback=True, error=str(error))
                self.diagnostics["analytic_components_fallback"] += 1
        return values

    def integrate(self, piece, left=Q(0), right=Q(1), purpose="head"):
        pending = [(left, right, 0)]
        accepted = []; total = [exact(0) for _ in range(6)]
        incomplete = None
        while pending:
            try:
                self.budget.panel()
            except ResourceStop as error:
                incomplete = str(error); break
            lo, hi, depth = pending.pop()
            box = None; error_text = None
            self.last_component_attempts = []
            self.last_panel = dict(purpose=purpose, source_piece=piece.index,
                original_cell=piece.n, original_segment=piece.j,
                closed_parameter_interval=[str(lo), str(hi)], depth=depth,
                interval_classification_is_not_a_unique_physical_failure_cause=True)
            try:
                box = piece.range(lo, hi)
            except (ArithmeticError, ValueError, ZeroDivisionError, OverflowError) as error:
                error_text = str(error)
            if box is None:
                self.diagnostics["real_range_failures"] += 1
                self.last_panel.update(finite_complete_real_range=False, range_error=error_text)
                if depth < self.args.max_depth:
                    mid = (lo+hi)/2
                    pending.extend(((mid, hi, depth+1), (lo, mid, depth+1)))
                    continue
                pending.append((lo, hi, depth))
                incomplete = "No finite real range at maximum panel depth: "+str(error_text)
                break
            integrals = [exact(hi-lo)*value for value in box["six"]]
            method = "complete-real-range-times-exact-length"
            kind = None; analytic_error = None
            met = self.goal_met(integrals, hi-lo)
            self.last_panel.update(finite_complete_real_range=True,
                possible_original_cap_branches=box["branches"],
                original_w_derivative_range=record(box["q"]),
                complete_real_range_goals=self.goal_records(integrals, hi-lo))
            if met:
                self.diagnostics["real_range_goal_passes"] += 1
            if not met:
                kind = piece.analytic_kind(lo, hi)
                try:
                    tighter = self.analytic_integrals(piece, lo, hi, kind,
                        box["six"], box["branches"])
                    # Both methods enclose the same integral. Retain their
                    # intersection, including all six original components.
                    integrals = [intersect_known(a, b.lower(), b.upper())
                                 for a, b in zip(integrals, tighter)]
                    method = "unit-panel-piecewise-six-integrals-intersected-with-full-real-range"
                    met = self.goal_met(integrals, hi-lo)
                    if met:
                        self.diagnostics["restored_six_goals_passes"] += 1
                except ResourceStop as error:
                    self.last_panel.update(resource_stop=str(error),
                        actual_component_attempts=self.last_component_attempts)
                    pending.append((lo, hi, depth))
                    incomplete = str(error); break
                except (ArithmeticError, ValueError, ZeroDivisionError, OverflowError) as error:
                    analytic_error = str(error)
            work_rows = self.goal_records(integrals, hi-lo)
            self.last_panel.update(legacy_unique_branch_and_sign=kind,
                restored_integral_goals=work_rows,
                actual_component_attempts=self.last_component_attempts,
                all_six_work_goals_met=bool(met), analytic_error=analytic_error)
            for k, row in enumerate(work_rows):
                if not row["full_width_goal_met"]:
                    self.diagnostics["failed_component_full_width_goals"][k] += 1
            if not met and depth < self.args.max_depth:
                self.diagnostics["subdivided_after_restored_goal_failure"] += 1
                mid = (lo+hi)/2
                pending.extend(((mid, hi, depth+1), (lo, mid, depth+1)))
                continue
            # A complete range remains valid even when the work-width request
            # was not met. It is not converted into a scientific rejection.
            self.all_work_goals_met &= met
            self.diagnostics["complete_accepted_panels"] += 1
            if not met:
                self.diagnostics["coarse_valid_panels_at_maximum_depth"] += 1
            row_number = self.ledger.rows
            self.ledger.add(dict(purpose=purpose, source_piece=piece.index,
                original_cell=piece.n, original_segment=piece.j,
                closed_parameter_interval=[str(lo), str(hi)], depth=depth,
                all_six_primitive_names=list(SIX_NAMES),
                all_six_integrals=[record(v) for v in integrals],
                all_six_real_ranges=[record(v) for v in box["six"]],
                field_range=range_record(box), possible_cap_branches=box["branches"],
                analytic_branch_sign=kind, analytic_fallback_reason=analytic_error,
                restored_full_width_work_goals=work_rows,
                actual_component_attempts=self.last_component_attempts,
                method=method, work_width_goal_met=met,
                entire_closed_panel_included=True, omitted_cusp_or_branch_strip=False))
            accepted.append(dict(left=lo, right=hi, depth=depth, box=box,
                integrals=integrals, ledger_row=row_number, work_goal_met=met))
            total = [a+b for a, b in zip(total, integrals)]
        if incomplete is not None:
            for lo, hi, depth in reversed(pending):
                self.unpaid.add(dict(kind="integral-panel", purpose=purpose,
                    source_piece=piece.index, original_cell=piece.n, original_segment=piece.j,
                    closed_parameter_interval=[str(lo), str(hi)], depth=depth,
                    reason=incomplete, included_in_complete_primitive=False))
            return dict(complete=False, accepted=accepted, six=total,
                reason=incomplete, pending=[dict(left=str(a), right=str(b), depth=d)
                                           for a,b,d in reversed(pending)])
        if (not accepted or accepted[0]["left"] != left or accepted[-1]["right"] != right
                or any(a["right"] != b["left"] for a,b in zip(accepted, accepted[1:]))):
            raise AssertionError("A primitive partition lost part of the original closed interval")
        return dict(complete=True, accepted=accepted, six=total, reason=None, pending=[])


def radial_image(fragment):
    return fragment["radius_left"].lower().union(fragment["radius_right"].upper())


def fragment_record(fragment):
    box = fragment["box"]
    out = dict(kind=fragment["kind"], real_radial_image_enclosure=record(radial_image(fragment)),
        E=record(box["E"]), E_r=record(box["E_r"]), E_rr=record(box["E_rr"]),
        radius_left=record(fragment["radius_left"]), radius_right=record(fragment["radius_right"]))
    if fragment["kind"] == "head":
        out.update(source_piece=fragment["piece"].index,
            original_cell=fragment["piece"].n, original_segment=fragment["piece"].j,
            closed_parameter_interval=[str(fragment["left"]), str(fragment["right"])],
            primitive_ledger_row=fragment.get("ledger_row"),
            inverse_refinement_depth=fragment.get("depth", 0))
    else:
        out.update(source_cells=dict(first=160, stop="infinity"),
            all_admissible_original_roots_included=True, exact_cuff_E=1,
            exact_cuff_E_r=0, exact_cuff_E_rr=0)
    return out


def build_head(head, integrator, source_ledger, unpaid):
    radius = head.inner_radius
    cumulative = [exact(0) for _ in range(6)]
    fragments = []; complete_pieces = 0; suffix = None; reason = None
    for piece in head.pieces:
        result = integrator.integrate(piece)
        # All accepted panels are saved, but a partial piece is never advanced
        # past its missing intervals to construct an invented outer radius.
        for panel in result["accepted"]:
            increment = panel["integrals"][0]+head.lam*panel["integrals"][1]
            whole_range = exact(panel["right"]-panel["left"])*panel["box"]["radial_speed"]
            increment = intersect_known(increment, whole_range.lower(), whole_range.upper())
            next_radius = radius+increment
            fragment = dict(kind="head", piece=piece, left=panel["left"], right=panel["right"],
                radius_left=radius, radius_right=next_radius, box=panel["box"], depth=0,
                ledger_row=panel["ledger_row"])
            fragments.append(fragment)
            source_ledger.add(fragment_record(fragment))
            radius = next_radius
        cumulative = [a+b for a,b in zip(cumulative, result["six"])]
        if not result["complete"]:
            suffix = dict(first_piece=piece.index+1, stop_piece=len(head.pieces),
                full_piece_index_file="large-arrays/source-piece-index.json")
            reason = result["reason"]
            unpaid.add(dict(kind="unvisited-source-piece-suffix", **suffix,
                reason=reason, whole_original_pieces_retained=True))
            break
        complete_pieces += 1
        if piece.j == 8:
            print(json.dumps(dict(event="R286-continuous-original-source-cell-complete",
                original_cell=piece.n, completed_pieces=complete_pieces,
                elapsed_seconds=time.monotonic()-integrator.budget.started)), flush=True)
    complete = complete_pieces == len(head.pieces)
    if complete:
        alternative = head.inner_radius+cumulative[0]+head.lam*cumulative[1]
        radius = intersect_known(radius, alternative.lower(), alternative.upper())
    return dict(complete=complete, complete_pieces=complete_pieces,
        full_source_piece_count=len(head.pieces), fragments=fragments,
        six=cumulative, outer_radius=radius if complete else None,
        partial_prefix_radius=radius, unvisited_piece_suffix=suffix, reason=reason)


class QueryCover:
    def __init__(self, head, source, deep, args, budget, integrator, ledger, unpaid):
        self.head, self.source, self.deep, self.args = head, source, deep, args
        self.budget, self.integrator, self.ledger, self.unpaid = budget, integrator, ledger, unpaid
        self.goal = p2(-args.value_width_bits)
        self.cache = {}

    def intersects(self, fragment, query):
        if query["kind"] == "whole-natural-domain":
            return True
        a, b = map(exact, (query["left"], query["right"]))
        return not (fragment["radius_right"].upper() < a
                    or fragment["radius_left"].lower() > b)

    def split(self, fragment, query_id):
        piece, lo, hi = fragment["piece"], fragment["left"], fragment["right"]
        mid = (lo+hi)/2; key = (piece.index, lo, mid)
        if key not in self.cache:
            value = self.integrator.integrate(piece, lo, mid, purpose="inverse-query:"+query_id)
            if not value["complete"]:
                raise ResourceStop("Partial inverse-cover primitive: "+str(value["reason"]))
            self.cache[key] = value["six"]
        integrals = self.cache[key]
        left_box, right_box = piece.range(lo, mid), piece.range(mid, hi)
        increment = integrals[0]+self.head.lam*integrals[1]
        known = exact(mid-lo)*left_box["radial_speed"]
        increment = intersect_known(increment, known.lower(), known.upper())
        middle_radius = fragment["radius_left"]+increment
        # Monotonicity is a theorem about the real primitive, not point.r.
        middle_radius = intersect_known(middle_radius,
            fragment["radius_left"].lower(), fragment["radius_right"].upper())
        left = dict(kind="head", piece=piece, left=lo, right=mid,
            radius_left=fragment["radius_left"], radius_right=middle_radius,
            box=left_box, depth=fragment["depth"]+1, ledger_row=None)
        right = dict(kind="head", piece=piece, left=mid, right=hi,
            radius_left=middle_radius, radius_right=fragment["radius_right"],
            box=right_box, depth=fragment["depth"]+1, ledger_row=None)
        return left, right

    def run(self, query):
        complete_source = self.source["complete"] and self.deep is not None
        domain_proved = False; domain_reason = None
        if complete_source:
            if query["kind"] == "whole-natural-domain":
                domain_proved = True
            else:
                a, b = query["left"], query["right"]
                if a < rat(self.head.p["rCuff"]):
                    domain_reason = "Query extends below the declared true cuff"
                elif exact(b) <= self.source["outer_radius"].lower():
                    domain_proved = True
                elif exact(b) > self.source["outer_radius"].upper():
                    domain_reason = "Query extends above the true natural outer radius"
                else:
                    domain_reason = "Actual natural cut containment is unresolved; no renormalisation"
        else:
            domain_reason = "The complete source or original-root existence premise is unpaid"
        if not domain_proved:
            self.unpaid.add(dict(kind="whole-query", query_id=query["id"],
                requested_query=encode_query(query), reason=domain_reason,
                whole_closed_query_retained=True))
            return dict(query=encode_query(query), complete_closed_domain_bound=False,
                domain_containment_proved=False, reason=domain_reason, E=None,
                work_resolution_complete=False, unresolved_whole_query=True)
        deep = dict(kind="deep", radius_left=self.deep["radius_left"],
            radius_right=self.deep["radius_right"], box=self.deep, depth=0)
        roots = [deep, *self.source["fragments"]]
        pending = [fragment for fragment in reversed(roots) if self.intersects(fragment, query)]
        values = []; first = self.ledger.rows; refined = unpaid_count = 0
        resolution_complete = True; stop_reason = None

        def retain(fragment, resolution_met, reason=None):
            nonlocal unpaid_count, resolution_complete
            values.append(fragment["box"]["E"])
            row = fragment_record(fragment)
            row.update(query_id=query["id"], work_resolution_met=resolution_met,
                       entire_possible_inverse_fragment_included=True)
            self.ledger.add(row)
            if not resolution_met:
                resolution_complete = False; unpaid_count += 1
                self.unpaid.add(dict(kind="query-resolution", query_id=query["id"],
                    inherited_valid_coarse_enclosure=True, complete_fragment=row, reason=reason))

        while pending:
            fragment = pending.pop()
            try:
                self.budget.query()
            except ResourceStop as error:
                pending.append(fragment); stop_reason = str(error); break
            if not self.intersects(fragment, query):
                continue
            met = is_narrow(fragment["box"]["E"], self.goal)
            if met:
                retain(fragment, True); continue
            if fragment["kind"] == "deep":
                retain(fragment, False,
                    "Uniform infinite original-root-family bound retained; no uncomputed root was selected")
                continue
            if fragment["depth"] >= self.args.query_depth:
                retain(fragment, False, "Declared inverse-cover refinement depth reached")
                continue
            try:
                left, right = self.split(fragment, query["id"])
                refined += 1
                if self.intersects(right, query):
                    pending.append(right)
                if self.intersects(left, query):
                    pending.append(left)
            except (ResourceStop, ArithmeticError, ValueError, ZeroDivisionError, OverflowError) as error:
                retain(fragment, False, "Parent enclosure retained after refinement failure: "+str(error))
                if isinstance(error, ResourceStop):
                    stop_reason = str(error); break
        if stop_reason is not None:
            # Existing parent bounds already contain each whole remaining
            # inverse fragment. Keep every one; no undecided branch is dropped.
            for fragment in reversed(pending):
                if self.intersects(fragment, query):
                    retain(fragment, False, stop_reason)
        if not values:
            raise AssertionError("A proved nonempty query has no retained inverse cover")
        value = hull(values)
        return dict(query=encode_query(query), complete_closed_domain_bound=True,
            domain_containment_proved=True, E=record(value),
            work_resolution_complete=resolution_complete,
            refined_nodes=refined, unresolved_resolution_fragments=unpaid_count,
            leaf_ledger_rows=dict(first=first, stop=self.ledger.rows),
            budget_or_refinement_stop=stop_reason,
            root_choice_scope="uniform-for-every-admissible-original-exact-root-sequence",
            actual_finite_selector_error_certified=False)


def encode_query(query):
    out = dict(index=query["index"], id=query["id"], kind=query["kind"])
    if query["kind"] == "closed-rational-radius-interval":
        out.update(left=str(query["left"]), right=str(query["right"]),
                   left_closed=True, right_closed=True)
    else:
        out.update(left="original-exact-dyadic-rCuff", right="natural-real-integral-R_out",
                   left_closed=True, right_closed=True)
    return out


def parse_queries(requested):
    if requested is None:
        return [dict(index=0, id="whole-declared-natural-domain", kind="whole-natural-domain")]
    out = []; ids = set()
    for index, row in enumerate(requested["queries"]):
        name = row.get("id", str(index))
        if not isinstance(name, str) or name in ids:
            raise ValueError("Query ids must be unique strings")
        ids.add(name)
        kind = row.get("kind", "closed-rational-radius-interval")
        if kind == "whole-natural-domain":
            out.append(dict(index=index, id=name, kind=kind)); continue
        if kind != "closed-rational-radius-interval":
            raise ValueError("Unsupported query kind")
        a, b = rat(row["left"]), rat(row["right"])
        if a > b:
            raise ValueError("Reversed original closed radial query")
        if row.get("left_closed", True) is not True or row.get("right_closed", True) is not True:
            raise ValueError("This producer retains both endpoints of every query")
        out.append(dict(index=index, id=name, kind=kind, left=a, right=b))
    return out


def finite_join_conditions(head):
    p = head.p
    last, start = p.get("flatOuterThroughCell"), p.get("flatOuterStartSegment", 2)
    if start is None:
        start = 2
    enabled = (numeric(last) and int(last) == last and last >= 0
               and numeric(p.get("flatSlope")) and p["flatSlope"] > 0)
    flat_indices = not enabled or (numeric(start) and int(start) == start and 0 <= start <= 8)
    return dict(proved=bool(flat_indices),
        actual_flat_start_segment=start, active_flat_transition_index_is_an_original_segment=bool(flat_indices),
        raw_port_relations_are_convention_C_real_relations=True,
        original_quintic_has_zero_first_two_endpoint_derivatives=True,
        identical_base_cap_port_values_and_unit_weight_ports_checked=True,
        finite_source_schema_used_as_seam_proof=False,
        unpaid_reason=None if flat_indices else "An unsupported flat index can omit the original smooth transition")


def argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("config", "ledger-ready", "stored-ready"):
        parser.add_argument("--"+name, type=Path, required=True)
        parser.add_argument("--"+name+"-sha256", required=True)
    parser.add_argument("--runtime-computations", type=Path, required=True)
    parser.add_argument("--source-topic", type=Path, required=True)
    parser.add_argument("--proof", type=Path, required=True)
    parser.add_argument("--queries", type=Path)
    parser.add_argument("--queries-sha256")
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--deep-definition", choices=["original-exact-root-family"],
                        default="original-exact-root-family")
    parser.add_argument("--precision-bits", type=int, default=256)
    parser.add_argument("--integral-absolute-bits", type=int, default=96)
    parser.add_argument("--integral-relative-bits", type=int, default=80)
    parser.add_argument("--analytic-guard-bits", type=int, default=8)
    parser.add_argument("--integral-evaluation-limit", type=int, default=100000)
    parser.add_argument("--value-width-bits", type=int, default=24)
    parser.add_argument("--max-depth", type=int, default=48)
    parser.add_argument("--query-depth", type=int, default=12)
    parser.add_argument("--max-panels", type=int, default=200000)
    parser.add_argument("--max-query-nodes", type=int, default=200000)
    parser.add_argument("--budget-seconds", type=float, default=1800)
    return parser


def main(argv=None):
    args = argument_parser().parse_args(argv)
    require_actions()
    if (args.queries is None) != (args.queries_sha256 is None):
        raise ValueError("Pair the actual query file with its exact SHA")
    if (not 128 <= args.precision_bits <= 8192
            or not 1 <= args.integral_absolute_bits <= args.precision_bits
            or not 1 <= args.integral_relative_bits <= args.precision_bits
            or not 0 <= args.analytic_guard_bits <= 64
            or not 1 <= args.value_width_bits <= args.precision_bits
            or not 0 <= args.max_depth <= 80 or not 0 <= args.query_depth <= 60
            or args.max_panels <= 0 or args.max_query_nodes <= 0
            or args.integral_evaluation_limit <= 0
            or not math.isfinite(args.budget_seconds) or args.budget_seconds <= 0):
        raise ValueError("Invalid explicit work precision or resource parameters")
    if args.out.exists():
        raise ValueError("Use a fresh request-owned output directory")
    for path in (args.config, args.ledger_ready, args.stored_ready, args.proof):
        if path.resolve().is_relative_to(args.out.resolve()):
            raise ValueError("The fresh output cannot own an original input")
    p, rows, lam, requested, binding = bind_inputs(args)
    queries = parse_queries(requested)
    args.out.mkdir(parents=True)
    large = args.out/"large-arrays"; large.mkdir()
    budget = WorkBudget(args)
    runtime = initialise_math(args.precision_bits)
    binding["runtime"] = runtime
    binding["work_parameters"] = {name:getattr(args, name) for name in
        ("precision_bits", "integral_absolute_bits", "integral_relative_bits", "analytic_guard_bits",
         "integral_evaluation_limit", "value_width_bits", "max_depth", "query_depth",
         "max_panels", "max_query_nodes", "budget_seconds", "deep_definition")}
    binding_receipt = write_json(args.out/"input-binding.json", binding)
    query_receipt = write_json(args.out/"query-plan.json", dict(schema=QUERY_SCHEMA,
        input_binding_sha256=binding_receipt["sha256"], queries=[encode_query(q) for q in queries]))
    primitive_ledger = Journal(large/"six-primitive-panels.jsonl", args.out)
    source_ledger = Journal(large/"complete-source-radial-panels.jsonl", args.out)
    query_ledger = Journal(large/"query-closed-inverse-cover.jsonl", args.out)
    unpaid = Journal(large/"unpaid-complete-scope.jsonl", args.out)
    source = head = deep = integrator = None
    protected = joins = None
    piece_index_receipt = None; query_results = []
    query_suffix = None; error_record = None
    try:
        head = ContinuousHead(p, rows, lam, binding)
        piece_index_receipt = write_json(large/"source-piece-index.json", dict(
            schema=SCHEMA+"-source-pieces", original_source_order="n159..0/j0..8",
            complete_piece_count=1440, pieces=[piece.descriptor() for piece in head.pieces]))
        piece_index_receipt["file"] = "large-arrays/"+piece_index_receipt["file"]
        joins, protected = finite_join_conditions(head), head.protected_join()
        deep = head.deep_cover()
        if deep is None:
            unpaid.add(dict(kind="whole-infinite-deep-source", first_cell=160,
                last_cell="infinity", reason="R286 original exact-root existence box is not proved",
                conditions=binding["convention"]["root_conditions"], no_root_assumed_from_zero_unresolved=True))
        integrator = SixPrimitiveIntegrator(head, args, budget, primitive_ledger, unpaid)
        source = build_head(head, integrator, source_ledger, unpaid)
        cover = QueryCover(head, source, deep, args, budget, integrator, query_ledger, unpaid)
        for index, query in enumerate(queries):
            if index and (time.monotonic()-budget.started >= budget.seconds
                          or budget.query_nodes >= budget.max_query_nodes):
                query_suffix = dict(first=index, stop=len(queries), file="query-plan.json")
                unpaid.add(dict(kind="unvisited-query-suffix", **query_suffix,
                    reason="Declared resource budget reached; complete original plan retained"))
                break
            result = cover.run(query)
            result["continuous_model_family_conditions_proved"] = bool(
                binding["convention"]["root_existence_proved"] and joins["proved"] and protected["proved"])
            query_results.append(result)
            print(json.dumps(dict(event="R286-continuous-E-query-result",
                query_index=index, domain_bound_complete=result["complete_closed_domain_bound"],
                work_resolution_complete=result["work_resolution_complete"])), flush=True)
    except Exception as error:
        error_record = dict(type=type(error).__name__, message=str(error))
        unpaid.add(dict(kind="producer-exception", error=error_record,
            complete_original_query_plan_retained=True,
            conservative_unfinished_scope="All source/query regions not proved by the completed records"))
        print(json.dumps(dict(event="R286-continuous-producer-exception", **error_record)), file=sys.stderr, flush=True)
    finally:
        ledgers = dict(six_primitives=primitive_ledger.finish(),
            source_radial_panels=source_ledger.finish(), query_inverse_cover=query_ledger.finish(),
            complete_unpaid_scope=unpaid.finish())
    query_result_receipt = write_json(args.out/"query-results.json", dict(schema=SCHEMA+"-queries",
        results=query_results, unvisited_query_suffix=query_suffix))
    source_complete = source is not None and source["complete"]
    continuous_conditions = bool(binding["convention"]["root_existence_proved"]
        and protected is not None and protected["proved"] and joins is not None and joins["proved"])
    all_queries = (source_complete and deep is not None and len(query_results) == len(queries)
                   and all(q["complete_closed_domain_bound"] for q in query_results))
    full_six = ([a+b for a,b in zip(source["six"], deep["six"])]
                if source_complete and deep is not None else None)
    report = dict(schema=SCHEMA, source_sha256=sha(Path(__file__).read_bytes()),
        preserved_original_producer_source=binding["preserved_original_producer_source"],
        integral_strategy=binding["integral_strategy"],
        original_six_full_width_goal_unchanged=True,
        original_real_profile_and_model_C_unchanged=True,
        run_id=os.environ.get("GITHUB_RUN_ID"), source_commit=os.environ.get("GITHUB_SHA"),
        repository=REPOSITORY, runtime=runtime, input_binding=binding_receipt,
        query_plan=query_receipt, query_results=query_result_receipt,
        source_piece_index=piece_index_receipt, ledgers=ledgers,
        target_model_schema=MODEL_SCHEMA,
        model_choice_is_explicit_and_not_original_finite_output_relabel=True,
        deep_definition=args.deep_definition,
        original_exact_deep_root_existence_proved=binding["convention"]["root_existence_proved"],
        original_exact_deep_root_choice_resolved=False,
        all_admissible_original_root_choices_uniformly_enclosed=deep is not None,
        deep_root_values_computed=0, finite_root_table_recalibrated=False,
        protected_join=protected, finite_joins=joins,
        declared_continuous_model_family_conditions_proved=continuous_conditions,
        full_finite_head_complete=bool(source_complete),
        complete_original_pieces=source["complete_pieces"] if source is not None else 0,
        original_piece_count=1440, original_finite_cell_count=160,
        natural_outer_radius=record(source["outer_radius"]) if source_complete else None,
        natural_outer_radius_minus_nominal_binary_cut=(record(source["outer_radius"]-exact(p["rCut"]))
                                                      if source_complete else None),
        global_warp_alpha_or_original_cut_renormalised=False,
        finite_head_all_six_primitives=[record(v) for v in source["six"]] if source_complete else None,
        full_deep_plus_head_all_six_primitives=[record(v) for v in full_six] if full_six is not None else None,
        primitive_names=list(SIX_NAMES),
        deep_cover=(dict(radial_right=record(deep["radius_right"]), E=record(deep["E"]),
            E_r=record(deep["E_r"]), E_rr=record(deep["E_rr"]),
            includes_all_source_cells_from160_and_exact_cuff=True,
            all_original_root_choices=True, formulas=deep["formulas"]) if deep is not None else None),
        all_requested_closed_query_bounds_complete=bool(all_queries),
        continuous_convention_C_query_enclosures_complete=bool(all_queries and continuous_conditions),
        requested_query_count=len(queries), returned_query_count=len(query_results),
        unvisited_query_suffix=query_suffix,
        unvisited_source_piece_suffix=source["unvisited_piece_suffix"] if source is not None else dict(first_piece=0, stop_piece=1440),
        numerical_work_resolution_complete=bool(all_queries and integrator is not None
            and integrator.all_work_goals_met and all(q["work_resolution_complete"] for q in query_results)),
        resource_or_unpaid_scope_rows=ledgers["complete_unpaid_scope"]["rows"],
        counts=dict(integral_panels=budget.panels, inverse_cover_nodes=budget.query_nodes,
                    rigorous_analytic_component_integrals=budget.integral_calls),
        integration_diagnostics=(dict(counts=integrator.diagnostics,
            last_attempted_panel=integrator.last_panel,
            declared_analytic_guard_bits=args.analytic_guard_bits,
            guard_bits_alone_are_not_an_error_certificate=True,
            original_complete_full_width_postcondition_is_decisive=True,
            finite_coarse_enclosure_is_separate_from_work_resolution=True,
            actual132_unique_numerical_cause_not_claimed=True)
            if integrator is not None else None),
        error=error_record, elapsed_seconds=time.monotonic()-budget.started,
        original_numeric_factory_or_48_selector_executed=False,
        R26_numerical_certificate_or_rational_deep_target_used=False,
        original_finite_output_certified_as_continuous_solution=False,
        original_continuous_g_model_choice_automatically_discharged=False,
        a601_same_field_binding_or_relative_metric_threshold_paid=False,
        actual_accepted_field_created=False, nonlinear_tail_or_ODE_or_shooting_J_run=False,
        arbitrary_source_or_query_suffix_omitted=False,
        raw_outputs_are_request_owned_temporary_recomputable_data=True)
    result_receipt = write_json(args.out/"result.json", report)
    primary = dict(report)
    primary["actual_result_file"] = result_receipt
    raw = canonical(primary)
    if len(raw) > 90000:
        print(json.dumps(dict(event="R286-summary-metadata-too-large", bytes=len(raw),
            sha256=sha(raw), result=result_receipt, complete_result_written=True)), flush=True)
        return 70
    print("BEGIN_R286_CONTINUOUS_ORIGINAL_E_SUMMARY", flush=True)
    print(raw.decode(), end="", flush=True)
    print("END_R286_CONTINUOUS_ORIGINAL_E_SUMMARY", flush=True)
    print(json.dumps(dict(event="R286-continuous-E-summary-identity",
        bytes=len(raw), sha256=sha(raw), actual_result_file=result_receipt)), flush=True)
    return 2 if error_record is not None else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(json.dumps(dict(event="R286-continuous-E-input-or-output-failure",
            type=type(error).__name__, message=str(error))), file=sys.stderr, flush=True)
        raise
