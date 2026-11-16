#!/usr/bin/env python3
"""R442: complete finite-M same-C Pruefer propagation with positive endpoints.

Scientific arithmetic only in the named public Actions repository.
Start from the original complete R312 deep root family and retain every
closed cut inverse candidate. Use globally existing constant-coefficient
angle barriers with full matrix-Taylor error, a proved positive-dot small
increment, and a real angle lift never reduced modulo pi or two pi.
Positive amplitude and exact power-of-two flux frame changes are retained.
Normalize each physical (u,k) Robin row using its correlated nonzero norm
before taking any candidate hull. DN still requires every height cosine
to exclude zero. No native Q/Pi scale mu is supplied or invented here.
No previous finite J, root midpoint selection or claimed native success.
Author: AI, 2026-11-15. Source delivery does not execute scientific arithmetic.
"""
from __future__ import annotations
import argparse
from collections import OrderedDict
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import sys
import time

REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "R442-original-C-complete-M-Pruefer-positive-endpoint-cut-family-enclosure-v1"
ORIGINAL_PRUEFER_NAME = "geometry_20261115_stored_C_finite_head_pruefer.py"
ORIGINAL_PRUEFER_SHA = "250474d748842d9b5423be2123460308ab16419d4b5dac1d8c9967fc208c0122"
POSITIVE_ENDPOINT_NAME = "geometry_20261115_pruefer_positive_endpoints.py"
POSITIVE_ENDPOINT_SHA = "91dd207bc20a87a36e2d4bc13e1b88a14333b67cf47ec048f85e8d46500822ff"
MODEL_SCHEMA = "R286-original-stored-continuous-model-convention-C-v1"
BINDER_NAME = "geometry_20261115_stored_continuous_E_cover_v3.py"
BINDER_SHA = "f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df"
COVER_SCHEMA = "R286-original-stored-convention-C-continuous-E-cover-v3"
FAR_NAME = "geometry_20261116_stored_continuous_C_M_far_graph.py"
FAR_SHA = "5f16872e6e2e71914a73345b2f9b9142dbb0a7438e68805033a3277d3eb3d528"
FAR_SCHEMA = "R442-original-C-root-family-complete-M-deep-far-enclosure-v1"
FAR_ROW_SCHEMA = "R442-original-C-one-mode-deep-far-enclosure-v1"
TAIL_PROOF_SHA = "036289ed624b59456cfee700217f442d26104cae76bf33d9affd8ec618c9ac73"
BASE_TUBE_PROOF_SHA = "f99acd8b025b38f5f2cdacbc8e129debbb48467587e72f92f74df5065fcad796"
BASE_PROPAGATOR_NAME = "geometry_20261115_stored_C_finite_head_flux.py"
BASE_PROPAGATOR_SHA = "4531b5b35093fa9c0010f9fdbd6700dcf4b099c076b5a3d69d20ccafda8af87d"
PROOF_SHA = "8a51036fd130c80365284c2e4678c3aa765d177471b4d16df0f4c85add016fa9"
PREVIOUS_RICCATI_NAME = "geometry_20261115_stored_C_finite_head_riccati.py"
PREVIOUS_RICCATI_SHA = "34606e3fea2093f78cc3cb88fa6e5f7bcc32112c8f9053484628ad1a16e11124"
PREVIOUS_RICCATI_PROOF_SHA = "c05a22becdc752bb87b7152761ae6b8ef02b30084bd09de62c7b305701609fec"
PREVIOUS_PROJECTIVE_NAME = "geometry_20261115_stored_C_finite_head_projective.py"
PREVIOUS_PROJECTIVE_SHA = "5440e2e0457b360120c180a2531e3db899d8534cf6366183fd68d111ede18216"
PROJECTIVE_PROOF_SHA = "29f79e1fff0fb872f1ae4920ff4ecbe459ca8aeb84f8dea639dd4bbe42f577f0"
QUERY_ID = "original-binary-config-cut-point"
MODE_EXTENSION_PROOF_SHA = "535118e0403bdf10af73f7b47d35e607121c298c12a077b76e20337a3a6c2013"
SUMMARY_LIMIT = 90000
B = P = None


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("Scientific arithmetic only in the named public Actions repository")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True,
        separators=(",", ":"), allow_nan=False)+"\n").encode()


def unique(items):
    out = {}
    for key, value in items:
        if key in out:
            raise ValueError("Duplicate JSON key: "+key)
        out[key] = value
    return out


def decode(raw):
    return json.loads(raw, object_pairs_hook=unique,
        parse_constant=lambda t: (_ for _ in ()).throw(ValueError("Nonfinite JSON token")))


def file_receipt(path, root=None):
    path = Path(path)
    digest = hashlib.sha256()
    count = 0
    with path.open("rb") as stream:
        for raw in iter(lambda: stream.read(1048576), b""):
            digest.update(raw)
            count += len(raw)
    return dict(file=str(path.relative_to(root)) if root else path.name,
        bytes=count, sha256=digest.hexdigest())


def bound_json(path, expected):
    raw = Path(path).read_bytes()
    if sha(raw) != expected:
        raise ValueError("Actual original SHA differs: "+str(path))
    return decode(raw), dict(file=Path(path).name, bytes=len(raw), sha256=expected)


def within(directory, relative):
    rel = PurePosixPath(relative)
    if rel.is_absolute() or ".." in rel.parts:
        raise ValueError("A descriptor escaped its original output directory")
    path = Path(directory)/rel
    if path.is_symlink() or not path.resolve().is_relative_to(Path(directory).resolve()):
        raise ValueError("The source descriptor does not name an owned original file")
    return path


def descriptor(directory, desc):
    path = within(directory, desc["file"])
    actual = file_receipt(path, Path(directory))
    if any(actual[k] != desc[k] for k in ("file", "bytes", "sha256")):
        raise ValueError("Original descriptor differs: "+desc["file"])
    return path


def json_descriptor(directory, desc):
    return decode(descriptor(directory, desc).read_bytes())


def write_json(path, value):
    raw = canonical(value)
    with Path(path).open("xb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    return dict(file=Path(path).name, bytes=len(raw), sha256=sha(raw))


def rational(value):
    if type(value) is int:
        return Q(value)
    if type(value) is float and math.isfinite(value):
        return Q.from_float(value)
    if isinstance(value, str):
        return Q(value)
    raise ValueError("Use an original finite scalar or an exact rational")


def pow2q(exponent):
    return Q(1 << exponent) if exponent >= 0 else Q(1, 1 << (-exponent))


def dyadic_q(value):
    if not isinstance(value, dict) or set(value) != {"mantissa", "binary_exponent"}:
        raise ValueError("Use exact producer endpoints, never their display")
    m, e = value["mantissa"], value["binary_exponent"]
    if (not isinstance(m, str) or re.fullmatch(r"-?(0|[1-9][0-9]*)", m) is None
            or type(e) is not int):
        raise ValueError("Invalid original dyadic endpoint")
    return Q(int(m))*pow2q(e)


def record_bounds(value):
    lo, hi = dyadic_q(value["lower"]), dyadic_q(value["upper"])
    if lo > hi:
        raise ValueError("Reversed interval in an actual original record")
    return lo, hi


def same_interval(a, b):
    return record_bounds(a) == record_bounds(b)


def requested_modes(value):
    if isinstance(value, bool) or not isinstance(value, int) or value < 112:
        raise ValueError("An explicit finite integer M>=112 is required")
    return tuple(range(2, 2*value+1, 2))


def load_runtime(args):
    global B,P
    require_actions()
    pins = {
        BINDER_NAME:BINDER_SHA,
        "geometry_20261115_stored_continuous_E_cover_v2.py":
            "004010b681aa35635e15b229a3e5b78602b3ec480a631a761e42f6c7d563b6ea",
        "geometry_20261115_stored_continuous_E_cover.py":
            "9aa0da45027afa37ca329eab73e5e93e788f2bbafb908b9e8c2960f537a427ed",
        FAR_NAME:FAR_SHA,
        BASE_PROPAGATOR_NAME:BASE_PROPAGATOR_SHA,
        PREVIOUS_PROJECTIVE_NAME:PREVIOUS_PROJECTIVE_SHA,
        PREVIOUS_RICCATI_NAME:PREVIOUS_RICCATI_SHA,
        ORIGINAL_PRUEFER_NAME:ORIGINAL_PRUEFER_SHA,
        POSITIVE_ENDPOINT_NAME:POSITIVE_ENDPOINT_SHA}
    sources = {}
    for name, expected in pins.items():
        rec = file_receipt(args.code_directory/name)
        if rec["sha256"] != expected:
            raise ValueError("Frozen scientific source differs: "+name)
        sources[name] = rec
    proof = file_receipt(args.proof)
    if proof["sha256"] != PROOF_SHA:
        raise ValueError("Use the complete frozen R380 real-angle comparison proof")
    path = args.code_directory/BINDER_NAME
    spec = importlib.util.spec_from_file_location("_R380_frozen_original_C", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    B = module
    runtime = B.initialise_math(args.precision_bits)
    pspec = importlib.util.spec_from_file_location("_R380_positive_endpoints",
        args.code_directory/POSITIVE_ENDPOINT_NAME)
    P = importlib.util.module_from_spec(pspec)
    sys.modules[pspec.name] = P
    pspec.loader.exec_module(P)
    return runtime, sources, proof


def original_core(binding):
    # Far source intentionally used no query. These are the only fields
    # specific to a producer's numerical work/query rather than its C object.
    ignored = {"query_input", "runtime", "work_parameters"}
    return {k:v for k,v in binding.items() if k not in ignored}


def check_source_run(report, schema, producer):
    if (report["schema"] != schema or report["source_sha256"] != producer
            or report["repository"] != REPOSITORY
            or report["run_id"] != os.environ["GITHUB_RUN_ID"]
            or report["source_commit"] != os.environ["GITHUB_SHA"]):
        raise ValueError("Use actual same-job, same-source outputs of the pinned producers")
    if report["target_model_schema"] != MODEL_SCHEMA:
        raise ValueError("A different continuous or finite target was supplied")


def stream_rows(directory, desc):
    path = within(directory, desc["file"])
    digest = hashlib.sha256()
    count = rows = 0
    with path.open("rb") as stream:
        for raw in stream:
            digest.update(raw)
            count += len(raw)
            value = decode(raw)
            yield rows, value
            rows += 1
    if (count != desc["bytes"] or rows != desc["rows"]
            or digest.hexdigest() != desc["sha256"]):
        raise ValueError("The complete original row stream differs: "+desc["file"])


def bind_inputs(args):
    modes = requested_modes(args.field_modes)
    extension_proof = file_receipt(args.mode_extension_proof)
    if extension_proof["sha256"] != MODE_EXTENSION_PROOF_SHA:
        raise ValueError("Use the complete R442 finite-M root-family theorem")
    cover, cover_rec = bound_json(args.cover_directory/"result.json", args.cover_result_sha256)
    far, far_rec = bound_json(args.far_directory/"result.json", args.far_result_sha256)
    check_source_run(cover, COVER_SCHEMA, BINDER_SHA)
    check_source_run(far, FAR_SCHEMA, FAR_SHA)
    cb = json_descriptor(args.cover_directory, cover["input_binding"])
    fb = json_descriptor(args.far_directory, far["input_binding"])
    if (cb["schema"] != COVER_SCHEMA+"-input-binding"
            or cb["source_sha256"] != BINDER_SHA
            or fb["schema"] != "R442-original-C-root-family-complete-M-deep-far-input-binding-v1"
            or fb["source_sha256"] != FAR_SHA
            or original_core(cb) != original_core(fb["original_C_input_binding"])):
        raise ValueError("Deep and finite-head objects do not have identical original C input bindings")
    if (cb["convention"]["schema"] != MODEL_SCHEMA
            or cb["convention"]["deep_definition"] != "original-exact-root-family"
            or cb["convention"]["root_existence_proved"] is not True
            or cover["original_real_profile_and_model_C_unchanged"] is not True
            or far["far_port"] != 159 or far["physical_node"] != 160
            or far["actual_R312_proof"]["sha256"] != TAIL_PROOF_SHA
            or far["actual_R442_proof"]["sha256"] != MODE_EXTENSION_PROOF_SHA
            or fb["actual_R442_proof"]["sha256"] != MODE_EXTENSION_PROOF_SHA
            or far["field_modes"] != args.field_modes or fb["field_modes"] != args.field_modes
            or far["complete_requested_modes"] != list(modes)
            or fb["complete_physical_modes"] != list(modes)):

        raise ValueError("The original root-family/deep-port contract differs")
    point_result = json_descriptor(args.cover_directory, cover["query_results"])
    query_plan = json_descriptor(args.cover_directory, cover["query_plan"])
    if point_result["schema"] != COVER_SCHEMA+"-queries":
        raise ValueError("The actual query-results schema differs")
    cut = rational(cb["physical_parameters"]["rCut"])
    planned = [q for q in query_plan["queries"] if q["id"] == QUERY_ID]
    points = [r for r in point_result["results"] if r["query"]["id"] == QUERY_ID]
    if len(planned) != 1 or len(points) > 1:
        raise ValueError("The original config-cut query is not unique")
    target = planned[0]
    if (target["kind"] != "closed-rational-radius-interval"
            or rational(target["left"]) != cut or rational(target["right"]) != cut
            or target["left_closed"] is not True or target["right_closed"] is not True):
        raise ValueError("The query changed the actual binary config cut")
    point = points[0] if points else None
    if point is not None and point["query"] != target:
        raise ValueError("Actual point-query/plan identity differs")
    facts = dict(
        full_original_1440_head=bool(cover["full_finite_head_complete"]
            and cover["complete_original_pieces"] == 1440),
        continuous_model_conditions=cover["declared_continuous_model_family_conditions_proved"] is True,
        protected_join=cover["protected_join"] is not None and cover["protected_join"].get("proved") is True,
        all_finite_joins=cover["finite_joins"] is not None and cover["finite_joins"].get("proved") is True,
        complete_original_point_domain=bool(point is not None
            and point.get("complete_closed_domain_bound") is True
            and point.get("domain_containment_proved") is True
            and point.get("continuous_model_family_conditions_proved") is True),
        complete_M_deep_rows=far["all_complete_M_deep_far_rows_enclosed"] is True,
        all_original_root_choices=far["all_original_root_choices_uniformly_included"] is True)
    pieces = []
    previous = None
    for row_index, row in stream_rows(args.cover_directory, cover["ledgers"]["source_radial_panels"]):
        if row["kind"] != "head":
            raise ValueError("A finite source stream contains a different kind")
        p = row["source_piece"]
        lo, hi = map(rational, row["closed_parameter_interval"])
        if (type(p) is not int or not 0 <= p < 1440 or not Q(0) <= lo < hi <= 1
                or row["original_cell"] != 159-p//9 or row["original_segment"] != p%9):
            raise ValueError("An original whole source panel is malformed")
        if previous is None:
            if p != 0 or lo != 0:
                raise ValueError("The original source prefix did not begin at the deep port")
        else:
            pp, ph, pr = previous
            if not ((p == pp and lo == ph) or (p == pp+1 and ph == 1 and lo == 0)):
                raise ValueError("A closed source panel or piece was dropped")
            if not same_interval(pr, row["radius_left"]):
                raise ValueError("The original cumulative primitive has a disconnected endpoint receipt")
        record_bounds(row["radius_left"])
        record_bounds(row["radius_right"])
        previous = (p, hi, row["radius_right"])
        pieces.append(dict(row=row_index, source_piece=p, left=lo, right=hi,
            radius_left=row["radius_left"], radius_right=row["radius_right"],
            original=row))
    if facts["full_original_1440_head"] and (
            previous is None or previous[0] != 1439 or previous[1] != 1):
        raise ValueError("A declared complete source omitted its final original endpoint")
    span = point.get("leaf_ledger_rows") if facts["complete_original_point_domain"] else None
    if span is not None and not (type(span["first"]) is int and type(span["stop"]) is int
            and 0 <= span["first"] < span["stop"]):
        raise ValueError("The complete original cut leaf span is absent")
    leaves = []
    deep_leaves = []
    for i, row in stream_rows(args.cover_directory, cover["ledgers"]["query_inverse_cover"]):
        if span is None or not span["first"] <= i < span["stop"]:
            continue
        if (row["query_id"] != QUERY_ID
                or row["entire_possible_inverse_fragment_included"] is not True):
            raise ValueError("A cut leaf's complete source inclusion differs")
        if row["kind"] == "deep":
            deep_leaves.append(dict(leaf_row=i, original=row))
        elif row["kind"] == "head":
            p = row["source_piece"]
            lo, hi = map(rational, row["closed_parameter_interval"])
            if (type(p) is not int or not 0 <= p < 1440 or not 0 <= lo <= hi <= 1
                    or row["original_cell"] != 159-p//9 or row["original_segment"] != p%9):
                raise ValueError("An original possible cut leaf is malformed")
            leaves.append(dict(leaf_row=i, source_piece=p, left=lo, right=hi, original=row))
        else:
            raise ValueError("Unknown original cut leaf kind")
    if span is not None and len(leaves)+len(deep_leaves) != span["stop"]-span["first"]:
        raise ValueError("The actual complete cut leaf span was not read")
    far_rows = []
    for i, row in stream_rows(args.far_directory, far["complete_rows"]):
        if (i >= len(modes) or row["schema"] != FAR_ROW_SCHEMA or row["mode_index"] != i
                or row["physical_frequency"] != modes[i] or row["far_port"] != 159
                or row["physical_node"] != 160
                or row["every_actual_original_root_choice_included"] is not True
                or row["finite_head_propagation_or_cut_DN_claimed"] is not False):
            raise ValueError("The complete original deep row sequence differs")
        far_rows.append(row)
    if facts["complete_M_deep_rows"] and len(far_rows) != len(modes):
        raise ValueError("A complete_M deep result omitted actual rows")
    inner = far["original_R286_deep_geometry"]
    if inner is not None:
        facts["cut_strictly_beyond_original_deep_port"] = cut > record_bounds(inner["radius"])[1]
    else:
        facts["cut_strictly_beyond_original_deep_port"] = False
    facts["no_unpaid_deep_interior_cut_leaf"] = len(deep_leaves) == 0
    facts["nonempty_full_head_cut_cover"] = len(leaves) > 0
    if facts["complete_original_point_domain"] and facts["full_original_1440_head"]:
        outer_lo, _ = record_bounds(cover["natural_outer_radius"])
        facts["natural_cut_inclusion_rechecked"] = cut <= outer_lo
    else:
        facts["natural_cut_inclusion_rechecked"] = False
    binding = dict(schema=SCHEMA+"-input-binding",
        source_sha256=sha(Path(__file__).read_bytes()), target_model_schema=MODEL_SCHEMA,
        actual_cover_result=cover_rec, actual_far_result=far_rec,
        actual_cover_input_binding=cover["input_binding"],
        actual_far_input_binding=far["input_binding"],
        original_C_input_binding=cb,
        actual_complete_source_stream=cover["ledgers"]["source_radial_panels"],
        actual_complete_inverse_stream=cover["ledgers"]["query_inverse_cover"],
        actual_complete_deep_row_stream=far["complete_rows"],
        actual_query_plan=cover["query_plan"], actual_query_results=cover["query_results"],
        actual_point_query=point, original_binary_cut_exact_rational=str(cut),
        same_original_C_binding_cross_checked=True,
        field_modes=args.field_modes, complete_requested_modes=list(modes),
        actual_R442_proof=extension_proof,
        actual_M_theorem_applicability=far["exact_theorem_applicability"],
        actual_scope_conditions=facts,
        same_actual_source_run_required=True,
        initial_column_normalization="original Q_F=1; positive rho_F=r_F^4*sqrt(1+(w_F*slope_F)^2), real phi_F=atan(w_F*slope_F)",
        column_representation="positive-amplitude factor chain plus complete unwrapped real angle and exact binary flux frame",
        native_Q_Pi_scale_mu_not_supplied_or_invented=True,
        original_QF_one_cut_column_materialized=False,
        physical_state=["u","k=dH/dr"], internal_continuous_flux_state=["u","j=w*k"],
        extra_source_length_or_Pi_port_applied=False,
        original_source_full_row_count=len(pieces), selected_cut_leaf_count=len(leaves),
        unpaid_deep_interior_cut_leaf_count=len(deep_leaves),
        original_finite_selector_or_old_zero_J_used=False,
        original_family_root_choice_resolved=False)
    return dict(cover=cover, far=far, core=cb, binding=binding, facts=facts,
        field_modes=args.field_modes, modes=modes,
        panels=pieces, leaves=leaves, far_rows=far_rows, cut=cut,
        ready=all(facts.values()))


class WorkStop(Exception):
    pass


class PanelUnpaid(Exception):
    pass


class Budget:
    """Actual linear-phase resources; binding/runtime setup precede this clock."""
    def __init__(self, args):
        self.started = time.monotonic()
        self.seconds, self.limit = args.budget_seconds, args.max_panels
        self.reserve = args.free_bytes_reserve
        self.output = args.out
        self.attempts = self.checks = self.storage_observations = 0
        self.last_storage_time = None
        self.checks_since_storage = 0
        self.last_storage = None
        self.stop = None

    def halt(self, kind, **facts):
        if self.stop is None:
            self.stop = dict(kind=kind, actual_elapsed_seconds=time.monotonic()-self.started,
                actual_panel_attempts=self.attempts, **facts)
        raise WorkStop(kind)

    def check(self, force_storage=False):
        now = time.monotonic()
        self.checks += 1
        self.checks_since_storage += 1
        if (force_storage or self.last_storage_time is None
                or now-self.last_storage_time >= 1 or self.checks_since_storage >= 256):
            try:
                disk = shutil.disk_usage(self.output)
            except OSError as failure:
                self.halt("actual-output-filesystem-capacity-observation-failed",
                    original_error=dict(type=type(failure).__name__,message=str(failure)))
            self.last_storage = dict(total=disk.total,used=disk.used,free=disk.free,
                required_free_reserve=self.reserve,
                elapsed_seconds=now-self.started)
            self.storage_observations += 1
            self.last_storage_time = now
            self.checks_since_storage = 0
            if disk.free < self.reserve:
                self.halt("declared-output-filesystem-free-reserve-reached",
                    actual_storage=self.last_storage)
        if now-self.started >= self.seconds:
            self.halt("declared-linear-propagation-wall-budget-reached",
                declared_seconds=self.seconds)

    def attempt(self):
        self.check()
        if self.attempts >= self.limit:
            self.halt("declared-complete-mode-panel-attempt-budget-reached",
                declared_panel_attempts=self.limit)
        self.attempts += 1

    def record(self):
        return dict(clock_scope="linear phase after source/input binding and runtime setup",
            elapsed_seconds=time.monotonic()-self.started,
            declared_seconds=self.seconds,declared_max_panels=self.limit,
            actual_panel_attempts=self.attempts,actual_checks=self.checks,
            free_bytes_reserve=self.reserve,
            storage_check_seconds_at_most_between_available_checks=1,
            storage_check_call_count_at_most=256,
            storage_observations=self.storage_observations,
            last_actual_storage=self.last_storage,stop=self.stop,
            all_stops_are_partial_scope_not_mathematical_refutations=True)


def as_ball(record):
    lo, hi = record_bounds(record)
    return B.interval(lo, hi)


def lower_q(ball):
    return dyadic_q(B.dyadic(ball.lower()))


def upper_q(ball):
    return dyadic_q(B.dyadic(ball.upper()))


def abs_upper_q(ball):
    if not ball.is_finite():
        raise ArithmeticError("A nonfinite interval is not a certified bound")
    return max(abs(lower_q(ball)), abs(upper_q(ball)))


def upper_ball(q):
    return B.exact(q).upper()


def finite(values):
    if any(not v.is_finite() for v in values):
        raise ArithmeticError("Nonfinite rigorous propagation enclosure")


def floor_log2(q):
    if q <= 0:
        raise ArithmeticError("A positive exact scale bound is required")
    e = q.numerator.bit_length()-q.denominator.bit_length()
    if q < pow2q(e):
        e -= 1
    return e


def exact_center(ball, bits):
    lo, hi = lower_q(ball), upper_q(ball)
    mid = (lo+hi)/2
    if mid == 0:
        return B.exact(0)
    quantum = pow2q(floor_log2(abs(mid))-bits+1)
    center = (mid//quantum)*quantum
    out = B.exact(center)
    if lower_q(out) != center or upper_q(out) != center:
        raise ArithmeticError("The declared exact dyadic center was rounded")
    return out


def sym(radius):
    if not radius.is_finite() or radius < 0:
        raise ArithmeticError("Invalid rigorous symmetric error radius")
    bound = radius.upper()
    return (-bound).union(bound)


def vector_norm(v):
    return upper_ball(max(abs_upper_q(x) for x in v))


def matrix_norm(M):
    return upper_ball(max(sum(abs_upper_q(x) for x in row) for row in M))


def eye():
    return [[B.exact(1), B.exact(0)], [B.exact(0), B.exact(1)]]


def mm(A, C):
    return [[sum((A[i][k]*C[k][j] for k in range(2)), B.exact(0))
             for j in range(2)] for i in range(2)]


def mv(A, v):
    return [A[i][0]*v[0]+A[i][1]*v[1] for i in range(2)]


def rec_matrix(A):
    return [[B.record(x) for x in row] for row in A]


def square_box(value):
    """Outward interval for the square; exact rational endpoint comparisons."""
    lo,hi = lower_q(value),upper_q(value)
    if lo >= 0:
        return B.interval(lo*lo,hi*hi)
    if hi <= 0:
        return B.interval(hi*hi,lo*lo)
    return B.interval(Q(0),max(lo*lo,hi*hi))


def known_range(value, lo, hi, name):
    if lo > hi:
        raise ArithmeticError("A proved range was reversed: "+name)
    result = B.intersect_known(value,B.exact(lo).lower(),B.exact(hi).upper())
    finite([result])
    return result


def circle_values(angle):
    """Entire real interval, including all turns and all trigonometric extrema."""
    cosine,sine = angle.cos(),angle.sin()
    finite([cosine,sine])
    return cosine,sine


def reframe_endpoint(angle_q,c):
    """F_c(phi)=phi+atan((c-1)sin(phi)cos(phi)/(cos²+c sin²))."""
    angle = B.exact(angle_q)
    cosine,sine = circle_values(angle)
    dot = B.exact(1)+(B.exact(c)-1)*square_box(sine)
    positive_dot = P.intersect(B,dot,min(Q(1),c),max(Q(1),c),
        "positive diagonal-frame dot")
    dot = P.enclosure(B,positive_dot)
    cross = (B.exact(c)-1)*sine*cosine
    ratio,ratio_receipt = P.quotient(B,cross,positive_dot)
    increment = ratio.atan()
    value = angle+increment
    finite([cross,increment,value])
    return value,dict(exact_input_lift=str(angle_q),
        positive_frame_dot=B.record(dot),frame_cross=B.record(cross),
        positive_dot_endpoints=P.record(positive_dot),
        endpoint_reciprocal_operation=ratio_receipt,
        small_continuous_angle_increment=B.record(increment),
        outgoing_unwrapped_angle=B.record(value),
        positive_dot_selects_the_unique_increment_in_open_minus_pi_over_two_to_pi_over_two=True)


def reframe(state, balance_power):
    """Exact positive diagonal change, with its complete real angle lift."""
    delta = state["balance_power"]-balance_power
    angle = state["angle"]
    if delta == 0:
        receipt = dict(changed=False,source_balance=state["balance_power"],
            destination_balance=balance_power,exact_positive_flux_scale="1",
            angle_lift_identity=True,
            whole_log_positive_amplitude_shift=B.record(B.exact(0)))
        return dict(state,frame_role="fixed-panel-Pruefer-frame"),receipt
    c = pow2q(delta)
    low,low_receipt = reframe_endpoint(lower_q(angle),c)
    high,high_receipt = reframe_endpoint(upper_q(angle),c)
    left,right = lower_q(low),upper_q(high)
    if left > right:
        raise ArithmeticError("The increasing continuous frame lift lost endpoint order")
    transformed = B.interval(left,right)
    _,sine = circle_values(angle)
    norm2 = B.exact(1)+(B.exact(c*c)-1)*square_box(sine)
    positive_norm2 = P.intersect(B,norm2,min(Q(1),c*c),max(Q(1),c*c),
        "complete positive frame-norm square")
    norm2 = P.enclosure(B,positive_norm2)
    log_norm2,log_receipt = P.logarithm(B,positive_norm2)
    log_shift = log_norm2/2
    logabs = state["amplitude_logabs"]+log_shift
    finite([transformed,norm2,log_shift,logabs])
    receipt = dict(changed=True,source_balance=state["balance_power"],
        destination_balance=balance_power,
        exact_positive_flux_scale=str(c),flux_scale_power_of_two=delta,
        complete_incoming_unwrapped_angle=B.record(angle),
        complete_outgoing_unwrapped_angle=B.record(transformed),
        lower_endpoint_lift=low_receipt,upper_endpoint_lift=high_receipt,
        endpoint_order_uses_Fc_derivative_c_over_cos2_plus_c2sin2_strictly_positive=True,
        full_frame_norm_squared=B.record(norm2),
        positive_frame_norm_squared_endpoints=P.record(positive_norm2),
        endpoint_log_operation=log_receipt,
        whole_log_positive_amplitude_shift=B.record(log_shift),
        no_principal_angle_or_shortest_arc_replacement=True)
    framed = dict(state,angle=transformed,v=list(circle_values(transformed)),
        balance_power=balance_power,amplitude_logabs=logabs,
        frame_role="fixed-panel-Pruefer-frame")
    return framed,receipt


def state_record(state):
    return dict(unwrapped_real_angle=B.record(state["angle"]),
        unit_circle_component_enclosures=[B.record(v) for v in state["v"]],
        flux_balance_power_of_two=state["balance_power"],
        positive_amplitude_sign=1,
        log_positive_amplitude=B.record(state["amplitude_logabs"]),
        complete_amplitude_factor_count=state["factor_count"],
        complete_amplitude_factor_chain_sha256=state["factor_chain_sha256"],
        frame_role=state.get("frame_role","accepted-Pruefer-endpoint"),
        exact_semantics="(u,j)=rho*diag(1,2^b)*(cos(phi),sin(phi)); rho>0; phi is a real unwrapped lift",
        angle_never_reduced_modulo_pi_or_two_pi=True,
        both_component_boxes_may_contain_zero_without_losing_exact_unit_circle_identity=True,
        original_QF_one_physical_column_not_materialized_by_this_record=True,
        inherited_interval_uncertainty_not_replaced_by_midpoint=True)


def small_lift(initial, column, angle_q, radius):
    """Angle of exp(t H)v0 relative to v0, on a proved positive-dot subarc."""
    cosine,sine = initial
    dot = cosine*column[0]+sine*column[1]
    cross = cosine*column[1]-sine*column[0]
    r = B.exact(radius)
    analytic_lower = (-r).exp()*r.cos()
    analytic_upper = r.exp()
    if not analytic_lower > 0:
        raise ArithmeticError("The complete small-step positive-dot bound was not isolated")
    positive_dot = P.intersect(B,dot,lower_q(analytic_lower),upper_q(analytic_upper),
        "complete auxiliary small-step positive dot")
    dot = P.enclosure(B,positive_dot)
    ratio,ratio_receipt = P.quotient(B,cross,positive_dot)
    increment = ratio.atan()
    increment = known_range(increment,-radius,radius,"global bounded phase displacement")
    lifted = B.exact(angle_q)+increment
    finite([dot,cross,increment,lifted])
    return lifted,dict(dot=B.record(dot),cross=B.record(cross),
        proved_dot_lower=B.record(analytic_lower),
        proved_dot_upper=B.record(analytic_upper),
        positive_dot_endpoints=P.record(positive_dot),
        endpoint_reciprocal_operation=ratio_receipt,
        continuous_small_increment=B.record(increment),
        unwrapped_angle=B.record(lifted),
        same_unit_initial_column_used_in_both_dot_and_cross=True,
        positive_dot_not_a_physical_height_condition=True)


def pruefer_barrier(Aq,Bq,initial,h,args):
    """Global phi'=A cos²(phi)-B sin²(phi), with complete Taylor transport."""
    A,Bc = B.exact(Aq),B.exact(Bq)
    H = [[B.exact(0),Bc],[A,B.exact(0)]]
    gamma_q = max(abs(Aq),abs(Bq))
    radius = h*gamma_q
    gamma = B.exact(gamma_q)
    norm_length = B.exact(radius)
    base = dict(exact_A=str(Aq),exact_B=str(Bq),exact_initial_angle=str(initial),
        exact_closed_time_interval=["0",str(h)],matrix=H,
        norm=gamma,length_norm=norm_length,exact_length_norm=str(radius),
        exact_matrix_two_norm=str(gamma_q),
        globally_existing_bounded_lipschitz_angle_ODE=True)
    if radius > args.panel_norm_limit:
        return dict(base,needs_norm_split=True,lift_complete=False)
    if h == 0:
        angle = B.exact(initial)
        initial_column = list(circle_values(angle))
        identity = dict(dot=B.record(B.exact(1)),cross=B.record(B.exact(0)),
            proved_dot_lower=B.record(B.exact(1)),proved_dot_upper=B.record(B.exact(1)),
            continuous_small_increment=B.record(B.exact(0)),unwrapped_angle=B.record(angle),
            same_unit_initial_column_used_in_both_dot_and_cross=True,
            positive_dot_not_a_physical_height_condition=True)
        return dict(base,needs_norm_split=False,lift_complete=True,
            initial_column=initial_column,endpoint=initial_column,tube=initial_column,
            endpoint_angle=angle,closed_angle=angle,endpoint_lift=identity,tube_lift=identity,
            endpoint_tail=B.exact(0),tube_tail=B.exact(0),
            initial_norm=vector_norm(initial_column),
            endpoint_error=B.exact(0),tube_error=B.exact(0))
    endpoint_matrix,endpoint_tail = taylor_exponential(
        H,h,gamma,args.taylor_terms,False)
    tube_matrix,tube_tail = taylor_exponential(
        H,h,gamma,args.taylor_terms,True)
    initial_column = list(circle_values(B.exact(initial)))
    endpoint,tube = mv(endpoint_matrix,initial_column),mv(tube_matrix,initial_column)
    initial_norm = vector_norm(initial_column)
    endpoint_error = (endpoint_tail*initial_norm).upper()
    tube_error = (tube_tail*initial_norm).upper()
    endpoint_angle,endpoint_lift = small_lift(initial_column,endpoint,initial,radius)
    closed_angle,tube_lift = small_lift(initial_column,tube,initial,radius)
    # Both are independently valid enclosures of the same endpoint.
    endpoint_angle = B.intersect_known(endpoint_angle,closed_angle.lower(),closed_angle.upper())
    finite(endpoint+tube+[endpoint_angle,closed_angle,endpoint_tail,tube_tail,
                         endpoint_error,tube_error])
    return dict(base,needs_norm_split=False,lift_complete=True,
        initial_column=initial_column,endpoint=endpoint,tube=tube,
        endpoint_angle=endpoint_angle,closed_angle=closed_angle,
        endpoint_lift=endpoint_lift,tube_lift=tube_lift,
        endpoint_tail=endpoint_tail,tube_tail=tube_tail,
        initial_norm=initial_norm,endpoint_error=endpoint_error,tube_error=tube_error)


def barrier_record(value):
    result = dict(exact_A=value["exact_A"],exact_B=value["exact_B"],
        exact_initial_unwrapped_angle=value["exact_initial_angle"],
        exact_closed_time_interval=value["exact_closed_time_interval"],
        constant_auxiliary_matrix=rec_matrix(value["matrix"]),
        exact_matrix_two_norm=value["exact_matrix_two_norm"],
        matrix_norm_upper=B.record(value["norm"]),
        complete_length_times_matrix_norm=B.record(value["length_norm"]),
        exact_length_times_matrix_norm=value["exact_length_norm"],
        globally_existing_bounded_lipschitz_angle_ODE=True,
        needs_norm_split=value["needs_norm_split"],
        continuous_angle_lift_complete=value["lift_complete"],
        no_physical_height_or_ratio_denominator_required=True)
    if not value["needs_norm_split"]:
        result.update(
            complete_initial_unit_column=[B.record(x) for x in value["initial_column"]],
            endpoint_auxiliary_column=[B.record(x) for x in value["endpoint"]],
            complete_closed_auxiliary_tube=[B.record(x) for x in value["tube"]],
            endpoint_unwrapped_angle=B.record(value["endpoint_angle"]),
            complete_closed_unwrapped_angle=B.record(value["closed_angle"]),
            endpoint_small_lift=value["endpoint_lift"],
            closed_small_lift=value["tube_lift"],
            endpoint_matrix_Taylor_remainder=B.record(value["endpoint_tail"]),
            whole_tube_matrix_Taylor_remainder=B.record(value["tube_tail"]),
            complete_initial_column_norm=B.record(value["initial_norm"]),
            endpoint_column_Taylor_error_bound=B.record(value["endpoint_error"]),
            whole_tube_column_Taylor_error_bound=B.record(value["tube_error"]),
            Taylor_matrix_remainder_applied_to_entire_initial_column=True,
            angle_is_not_principalised_after_auxiliary_transport=True)
    return result

class GeometryCache:
    def __init__(self, head, panels, args, journal, budget):
        self.head, self.panels, self.args = head, panels, args
        self.journal, self.budget = journal, budget
        self.cache = OrderedDict()
        self.base_speed = {}
        self.range_calls = 0
        self.hits = 0

    def ranges(self, piece, lo, hi):
        self.budget.check()
        self.range_calls += 1
        return piece.range(lo, hi)

    def original_speed(self, panel):
        index = panel["row"]
        if index not in self.base_speed:
            piece = self.head.pieces[panel["source_piece"]]
            try:
                box = self.ranges(piece, panel["left"], panel["right"])
                value = box["radial_speed"]
                self.base_speed[index] = value if value > 0 else None
            except ArithmeticError:
                # The original positive/monotone primitive bounds remain
                # valid; this optional tightening is not needed for them.
                self.base_speed[index] = None
        return self.base_speed[index]

    def radial_range(self, panel, lo, hi):
        left, right = as_ball(panel["radius_left"]), as_ball(panel["radius_right"])
        lower, upper = left.lower(), right.upper()
        speed = self.original_speed(panel)
        if speed is None:
            return lower.union(upper), "original-complete-panel-monotone-bounds"
        a, b = panel["left"], panel["right"]

        def endpoint(x):
            first = left+B.exact(x-a)*speed
            second = right-B.exact(b-x)*speed
            value = B.intersect_known(first, second.lower(), second.upper())
            return B.intersect_known(value, lower, upper)

        at_left, at_right = endpoint(lo), endpoint(hi)
        return at_left.lower().union(at_right.upper()), "both-original-primitive-endpoints-and-complete-D-range"

    def get(self, panel, lo, hi):
        key = (panel["row"], lo, hi)
        if key in self.cache:
            self.hits += 1
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        piece = self.head.pieces[panel["source_piece"]]
        box = self.ranges(piece, lo, hi)
        radius, method = self.radial_range(panel, lo, hi)
        w, q, D = box["w"], box["q"], box["radial_speed"]
        if not (w > 0 and D > 0 and radius > 0):
            raise ArithmeticError("The whole closed coefficient box did not separate R,w,D from zero")
        a, b0 = D/w, q/radius
        finite([w,q,D,radius,a,b0])
        record = dict(schema=SCHEMA+"-coefficient-box",
            coefficient_row=self.journal.rows, original_source_panel_row=panel["row"],
            source_piece=piece.index, original_cell=piece.n, original_segment=piece.j,
            closed_parameter_interval=[str(lo),str(hi)],
            complete_possible_cap_branches=box["branches"],
            same_original_R_primitive_bound_method=method,
            R=B.record(radius), w=B.record(w), q_equals_w_x=B.record(q),
            D_equals_R_x=B.record(D),
            flux_upper_right_D_over_w=B.record(a),
            flux_lower_left_before_m_squared_q_over_R=B.record(b0),
            new_primitives_integrated=0,
            extra_source_length_or_Pi_port_applied=False,
            all_possible_original_branches_retained=True)
        self.journal.add(record)
        value = dict(a=a,b0=b0,w=w,q=q,D=D,R=radius,
            coefficient_row=record["coefficient_row"], branches=box["branches"])
        self.cache[key] = value
        if len(self.cache) > self.args.max_geometry_cache_records:
            self.cache.popitem(last=False)
        return value


def pruefer_coefficients(geometry, m):
    a,b0 = geometry["a"],B.exact(m*m)*geometry["b0"]
    au,bu = abs_upper_q(a),abs_upper_q(b0)
    if au <= 0 or not a > 0:
        raise ArithmeticError("The whole positive flux coefficient must be strictly isolated")
    balance = -floor_log2(au) if bu == 0 else (floor_log2(bu)-floor_log2(au))//2
    alpha,beta = a*B.p2(balance),b0*B.p2(-balance)
    finite([alpha,beta])
    return alpha,beta,balance


def taylor_exponential(M0, h, beta, terms, whole_tube):
    t = B.exact(0).union(B.exact(h)) if whole_tube else B.exact(h)
    X = [[x*t for x in row] for row in M0]
    term, total = eye(), eye()
    for degree in range(1, terms+1):
        product = mm(term, X)
        term = [[x/degree for x in row] for row in product]
        total = [[total[i][j]+term[i][j] for j in range(2)] for i in range(2)]
    rho = (B.exact(h)*beta).upper()
    tail = rho.exp()
    # Written as a complete positive product; no unverified "guard" claim.
    for degree in range(1, terms+2):
        tail = tail*rho/degree
    tail = tail.upper()
    finite([tail]+[x for row in total for x in row])
    error = sym(tail)
    total = [[x+error for x in row] for row in total]
    return total,tail


def advance_candidate(state, geometry, m, lo, hi, args):
    h = hi-lo
    if h < 0:
        raise ValueError("A closed propagation panel cannot have negative original x length")
    alpha,beta,balance = pruefer_coefficients(geometry,m)
    framed,frame_change = reframe(state,balance)
    initial = framed["angle"]
    L0,U0 = lower_q(initial),upper_q(initial)
    al,au,bl,bu = lower_q(alpha),upper_q(alpha),lower_q(beta),upper_q(beta)
    if al <= 0:
        raise ArithmeticError("Balanced positive alpha lost its strict lower bound")
    # Every real phase is admitted, including all zeros of either component.
    lower = pruefer_barrier(bl,au,L0,h,args)
    upper = pruefer_barrier(bu,al,U0,h,args)
    common = dict(alpha=alpha,beta=beta,balance=balance,framed=framed,
        input_column_shift=state["balance_power"]-balance,
        exact_flux_frame_change=frame_change,
        lower_barrier=lower,upper_barrier=upper,zero_width_closed_point_panel=h == 0,
        actual_angle_initial_interval=initial,
        norm_length=upper_ball(max(upper_q(lower["length_norm"]),upper_q(upper["length_norm"]))),
        local_work_goal=B.p2(-args.local_defect_bits))
    if lower["needs_norm_split"] or upper["needs_norm_split"]:
        return dict(common,needs_norm_split=True,needs_barrier_split=False)
    if not (lower["lift_complete"] and upper["lift_complete"]):
        return dict(common,needs_norm_split=False,needs_barrier_split=True,
            next_state=None,amplitude_factor=None,work_goal_met=False)
    Lh,Uh = lower_q(lower["endpoint_angle"]),upper_q(upper["endpoint_angle"])
    if Lh > Uh:
        raise ArithmeticError("Ordered global angle barriers have incompatible endpoint enclosures")
    endpoint_angle = B.interval(Lh,Uh)
    # Each autonomous comparison solution is monotone or constant. The
    # actual variable-coefficient phase is not assumed monotone.
    tube_angle = B.interval(min(L0,Lh),max(U0,Uh))
    endpoint,tube = list(circle_values(endpoint_angle)),list(circle_values(tube_angle))
    sine_double = (2*tube_angle).sin()
    rate = (alpha+beta)*sine_double/2
    increment = B.exact(h)*rate
    logabs = framed["amplitude_logabs"]+increment
    logtube = framed["amplitude_logabs"]+B.interval(
        min(Q(0),lower_q(increment)),max(Q(0),upper_q(increment)))
    finite([endpoint_angle,tube_angle,rate,increment,logabs,logtube]+endpoint+tube)
    goal = common["local_work_goal"]
    met = all(error <= goal for barrier in (lower,upper)
        for error in (barrier["endpoint_error"],barrier["tube_error"]))
    factor = dict(schema=SCHEMA+"-positive-Pruefer-amplitude-factor",
        factor_index=state["factor_count"]+1,
        previous_factor_chain_sha256=state["factor_chain_sha256"],
        exact_flux_frame_change=frame_change,
        incoming_positive_amplitude_sign=1,outgoing_positive_amplitude_sign=1,
        whole_log_amplitude_rate=B.record(rate),
        full_endpoint_log_amplitude_increment=B.record(increment),
        complete_closed_log_positive_amplitude=B.record(logtube),
        outgoing_log_positive_amplitude=B.record(logabs),
        outgoing_flux_balance_power_of_two=balance,
        positive_exponential_from_finite_real_log_integral=True,
        no_midpoint_or_fixed_global_root_selected=True,
        exact_factor_semantics="rho_end=rho_old*kappa_frame(phi_old)*exp(integral_gamma); every factor is positive",
        complete_original_uncertainty_retained=True)
    chain = sha(canonical(factor))
    next_state = dict(angle=endpoint_angle,v=endpoint,balance_power=balance,
        amplitude_logabs=logabs,factor_count=state["factor_count"]+1,
        factor_chain_sha256=chain,frame_role="accepted-Pruefer-endpoint")
    factor["factor_chain_sha256"] = chain
    factor["factor_chain_hash_scope"] = "canonical complete factor record before adding these two hash fields"
    return dict(common,needs_norm_split=False,needs_barrier_split=False,
        work_goal_met=bool(met),endpoint=endpoint,tube=tube,
        actual_angle_endpoint=endpoint_angle,actual_angle_closed_tube=tube_angle,
        amplitude_log_rate=rate,amplitude_logabs_tube=logtube,
        next_state=next_state,amplitude_factor=factor)


def associate_cut_leaves(data):
    by_piece = {}
    for panel in data["panels"]:
        by_piece.setdefault(panel["source_piece"],[]).append(panel)
    by_panel = {}
    for leaf in data["leaves"]:
        candidates = [p for p in by_piece[leaf["source_piece"]]
            if p["left"] <= leaf["left"] and leaf["right"] <= p["right"]]
        if not candidates or (leaf["left"] < leaf["right"] and len(candidates) != 1):
            raise ValueError("An inverse fragment escaped its original complete source panel")
        # A legitimate zero-width shared endpoint belongs to each adjacent
        # original closed source panel. Retain every such responsibility.
        for panel in candidates:
            by_panel.setdefault(panel["row"],[]).append(leaf)
    last_row = max(by_panel)
    last_parameter = max(leaf["right"] for leaf in by_panel[last_row])
    required = []
    for panel in data["panels"][:last_row+1]:
        right = last_parameter if panel["row"] == last_row else panel["right"]
        if right < panel["left"]:
            raise ValueError("Required original closed prefix is reversed")
        required.append(dict(panel=panel,left=panel["left"],right=right))
    after = dict(original_source_panel_row=last_row,
        unneeded_remaining_part_of_last_panel=(
            [str(last_parameter),str(data["panels"][last_row]["right"])]
            if last_parameter < data["panels"][last_row]["right"] else None),
        unneeded_original_panel_suffix=dict(first=last_row+1,stop=len(data["panels"])),
        reason="Beyond every member of the actual complete config-cut inverse cover",
        zero_width_shared_endpoint_fragments_not_discarded=True,
        all_original_source_bytes_still_bound=True)
    return by_panel,required,after


def pending_description(required, index, stack):
    if index >= len(required):
        return None
    panel = required[index]["panel"]
    current = [dict(source_piece=panel["source_piece"],original_source_panel_row=panel["row"],
        closed_parameter_interval=[str(lo),str(hi)],subdivision_depth=depth)
        for lo,hi,depth in reversed(stack)]
    return dict(current_original_source_panel_row=panel["row"],
        complete_current_panel_stack_in_outward_order=current,
        subsequent_required_original_panel_suffix=dict(first=index+1,stop=len(required)),
        required_panel_index_file="required-source-panels.json",
        no_pending_sibling_or_required_mode_silently_discarded=True)


def prepare_cut_tubes(candidate, geometry, panel, lo, hi, leaves, mode,
                      coverage, transaction_index):
    """Every closed cut intersection; per-candidate unit row before any hull."""
    relevant = [(leaf,max(lo,leaf["left"]),min(hi,leaf["right"])) for leaf in leaves]
    relevant = [(leaf,left,right) for leaf,left,right in relevant if left <= right]
    if not relevant:
        return [],[],{},[]
    if not geometry["w"] > 0:
        raise ArithmeticError("The same whole closed w must be positive for a physical Robin row")
    T0,T1 = candidate["tube"]
    framed = candidate["framed"]
    K = B.p2(framed["balance_power"])/geometry["w"]
    flux = B.p2(framed["balance_power"])*T1
    physical_k = K*T1
    finite([T0,T1,K,flux,physical_k])
    klo,khi = lower_q(K),upper_q(K)
    if klo <= 0:
        raise ArithmeticError("The complete positive physical row scale was not isolated")
    # This bound uses the same underlying angle in cos and sin. Independent
    # component boxes may both contain zero without the exact row vanishing.
    norm2 = square_box(T0)+square_box(K)*square_box(T1)
    positive_norm2 = P.intersect(B,norm2,min(Q(1),klo*klo),max(Q(1),khi*khi),
        "correlated physical Robin norm square")
    norm2 = P.enclosure(B,positive_norm2)
    inverse_norm,norm_receipt = P.inverse_square_root(B,positive_norm2)
    unit_row = [-physical_k*inverse_norm,T0*inverse_norm]
    finite([norm2,inverse_norm]+unit_row)
    amplitude = dict(positive_sign=1,
        complete_closed_log_positive_value=B.record(candidate["amplitude_logabs_tube"]),
        incoming_log_positive_value=B.record(framed["amplitude_logabs"]),
        log_rate_enclosure=B.record(candidate["amplitude_log_rate"]),
        prior_factor_count=framed["factor_count"],
        prior_factor_chain_sha256=framed["factor_chain_sha256"],
        exact_semantics="rho(t)=rho_at_left_after_positive_diagonal_frame_change*exp(integral_0^t gamma)",
        amplitude_is_a_positive_function_on_the_whole_panel_not_a_fixed_scalar=True,
        every_factor_strictly_positive_proved=True)
    rows,quotients,updates,unit_rows = [],[],{},[]
    for leaf,left,right in relevant:
        nonzero = bool(T0 > 0 or T0 < 0)
        quotient = None
        quotient_error = None
        if nonzero:
            try:
                quotient = K*T1/T0
                finite([quotient])
            except (ArithmeticError,ZeroDivisionError,OverflowError) as failure:
                quotient = None
                quotient_error = dict(type=type(failure).__name__,message=str(failure))
        old = coverage.get(leaf["leaf_row"])
        if old is None:
            if left != leaf["left"]:
                raise ValueError("A cut leaf began after an unpaid parameter prefix")
            updated = dict(left=left,right=right,candidate_count=0,
                height_unproved_count=0,legal_quotient_count=0,
                quotient_arithmetic_error_count=0)
        else:
            if left > old["right"]:
                raise ValueError("A closed cut leaf lost a parameter interval")
            updated = dict(old,right=max(old["right"],right))
        updated["candidate_count"] += 1
        updated["height_unproved_count"] += int(not nonzero)
        updated["legal_quotient_count"] += int(quotient is not None)
        updated["quotient_arithmetic_error_count"] += int(quotient_error is not None)
        updates[leaf["leaf_row"]] = updated
        rows.append(dict(schema=SCHEMA+"-cut-tube-contribution",
            physical_frequency=mode,transaction_index=transaction_index,
            original_cut_leaf_row=leaf["leaf_row"],
            original_source_panel_row=panel["row"],source_piece=panel["source_piece"],
            step_closed_parameter_interval=[str(lo),str(hi)],
            actual_cut_leaf_intersection=[str(left),str(right)],
            coefficient_row=geometry["coefficient_row"],
            whole_closed_step_tube_used_for_intersection=True,
            complete_unwrapped_angle_tube=B.record(candidate["actual_angle_closed_tube"]),
            complete_unit_circle_tube=[B.record(T0),B.record(T1)],
            fixed_flux_balance_power_of_two=framed["balance_power"],
            positive_panel_amplitude_family=amplitude,
            complete_global_angle_comparison_and_continuous_lift_paid=True,
            normalized_physical_height=B.record(T0),
            normalized_flux_j=B.record(flux),
            normalized_physical_k=B.record(physical_k),
            same_closed_panel_positive_w=B.record(geometry["w"]),
            physical_row_scale_K=B.record(K),
            positive_amplitude_nondividing_physical_Robin_row=dict(order=["u","k"],
                coefficient_u=B.record(-physical_k),coefficient_k=B.record(T0),
                original_QF_one_row_divided_only_by_its_positive_rho=True),
            correlated_Robin_norm_squared=B.record(norm2),
            positive_norm_square_endpoints=P.record(positive_norm2),
            endpoint_inverse_norm_operation=norm_receipt,
            exact_correlated_norm_square_lower_bound=str(min(Q(1),klo*klo)),
            oriented_unit_physical_Robin_row=dict(order=["u","k"],
                coefficient_u=B.record(unit_row[0]),coefficient_k=B.record(unit_row[1]),
                orientation_inherited_from_original_QF_one_and_positive_rho=True,
                entire_nonzero_row_normalized_before_any_candidate_hull=True),
            both_coordinate_boxes_may_contain_zero_without_zero_exact_row=True,
            original_QF_one_column_materialized=False,
            different_candidate_amplitude_scales_not_hulled_as_a_single_column=True,
            whole_candidate_height_excludes_zero=nonzero,
            candidate_cut_slope_enclosure_computed=quotient is not None,
            cut_slope_per_unit_physical_height=B.record(quotient) if quotient is not None else None,
            quotient_error=quotient_error,
            actual_resonance_not_inferred_when_height_cosine_contains_zero=True,
            complete_original_root_family_and_inherited_uncertainty_retained=True,
            Q_Pi_native_scale_mu_not_supplied_or_invented=True,
            no_old_Pi_or_second_source_length_used=True))
        quotients.append(quotient)
        unit_rows.append(unit_row)
    return rows,quotients,updates,unit_rows


def candidate_record(candidate):
    result = dict(needs_norm_split=candidate["needs_norm_split"],
        needs_barrier_split=candidate["needs_barrier_split"],
        full_balanced_alpha=B.record(candidate["alpha"]),
        full_balanced_beta=B.record(candidate["beta"]),
        maximum_barrier_length_times_matrix_norm=B.record(candidate["norm_length"]),
        original_unwrapped_angle_initial_enclosure=B.record(candidate["actual_angle_initial_interval"]),
        lower_global_comparison_barrier=barrier_record(candidate["lower_barrier"]),
        upper_global_comparison_barrier=barrier_record(candidate["upper_barrier"]),
        internal_complete_incoming_frame=state_record(candidate["framed"]),
        exact_flux_frame_change=candidate["exact_flux_frame_change"],
        local_numerical_work_goal=B.record(candidate["local_work_goal"]),
        zero_width_closed_point_panel=candidate["zero_width_closed_point_panel"],
        prior_state_uncertainty_was_not_replaced_by_midpoint=True,
        actual_angle_not_assumed_monotone=True,
        both_comparison_ODEs_globally_exist_without_ratio_poles=True,
        numerical_small_dot_transport_is_not_a_physical_height_gate=True)
    if candidate["needs_norm_split"] or candidate["needs_barrier_split"]:
        result.update(amplitude_factor=None,local_numerical_work_goal_met=False)
        return result
    result.update(
        complete_unwrapped_angle_endpoint=B.record(candidate["actual_angle_endpoint"]),
        complete_closed_unwrapped_angle_tube=B.record(candidate["actual_angle_closed_tube"]),
        complete_unit_circle_endpoint=[B.record(v) for v in candidate["endpoint"]],
        complete_unit_circle_closed_tube=[B.record(v) for v in candidate["tube"]],
        whole_log_amplitude_rate=B.record(candidate["amplitude_log_rate"]),
        whole_closed_log_positive_amplitude=B.record(candidate["amplitude_logabs_tube"]),
        amplitude_factor=candidate["amplitude_factor"],
        local_numerical_work_goal_met=candidate["work_goal_met"],
        valid_coarse_enclosure_retained=not candidate["work_goal_met"],
        work_goal_scope="constant-barrier matrix Taylor remainder times complete initial unit-column norm",
        all_Taylor_trigonometric_division_atan_and_log_rounding_remain_outward_intervals=True,
        comparison_coefficient_variation_included_by_ordered_barriers_not_omitted_as_small_defect=True,
        all_turns_in_real_angle_lift_retained=True,
        amplitude_strictly_positive_inside_this_whole_panel=True,
        internal_complete_outgoing_state=state_record(candidate["next_state"]))
    return result


def initial_column(far,data):
    geometry = data["far"]["original_R286_deep_geometry"]
    radius,w = as_ball(geometry["radius"]),as_ball(geometry["w"])
    if not (radius > 0 and w > 0):
        raise ArithmeticError("The original R312 deep physical geometry is not positive")
    slope = as_ball(far["actual_deep_port_slope_per_unit_physical_height"])
    u = radius**4
    k = slope*u
    j = w*k
    ratio = w*slope
    angle = ratio.atan()
    norm2 = B.exact(1)+square_box(ratio)
    positive_norm2 = P.intersect(B,norm2,Q(1),upper_q(norm2),
        "complete original initial polar norm square")
    norm2 = P.enclosure(B,positive_norm2)
    log_norm2,log_receipt = P.logarithm(B,positive_norm2)
    logabs = B.exact(4)*radius.log()+log_norm2/2
    v = list(circle_values(angle))
    finite([u,k,j,ratio,angle,norm2,logabs]+v)
    anchor = dict(schema=SCHEMA+"-initial-positive-amplitude",
        physical_frequency=far["physical_frequency"],
        actual_deep_row_canonical_sha256=sha(canonical(far)),
        original_radius=B.record(radius),positive_factor_radius_to_fourth=B.record(u),
        complete_initial_flux_ratio=B.record(ratio),
        initial_unwrapped_angle=B.record(angle),
        initial_positive_polar_norm_squared=B.record(norm2),
        positive_initial_norm_squared_endpoints=P.record(positive_norm2),
        endpoint_log_operation=log_receipt,
        log_positive_amplitude=B.record(logabs),positive_amplitude_sign=1,
        original_Q_F_normalization="1",
        exact_initial_factorization="rho=rF^4*sqrt(1+(wF*slopeF)^2); b=0; phi=atan(wF*slopeF) in (-pi/2,pi/2)",
        all_original_root_choices_included=True,
        no_original_slope_midpoint_or_subfamily_selected=True)
    chain = sha(canonical(anchor))
    state = dict(angle=angle,v=v,balance_power=0,
        amplitude_logabs=logabs,factor_count=0,factor_chain_sha256=chain,
        frame_role="original-positive-amplitude-real-angle-initial-frame")
    receipt = dict(original_deep_mode_index=far["mode_index"],
        physical_frequency=far["physical_frequency"],far_port=159,
        original_physical_radius=B.record(radius),original_w=B.record(w),
        R312_slope_per_unit_height=B.record(slope),
        original_u_F=B.record(u),original_k_F=B.record(k),original_j_F=B.record(j),
        original_Q_F_normalization="1",initial_amplitude_factor=anchor,
        initial_amplitude_factor_chain_sha256=chain,
        normalized_state=state_record(state),
        complete_original_root_family_not_midpoint_selected=True)
    return state,receipt


def propagate_mode(far,data,required,by_panel,geometry,args,budget,
                   step_journal,cut_journal,commit_journal,coverage_journal,unpaid_journal):
    m = far["physical_frequency"]
    state,initial = initial_column(far,data)
    coverage = {}
    partial_dn = None
    partial_unit_robin = None
    candidate_count = legal_count = height_unproved_count = quotient_error_count = 0
    accepted = coarse = norm_splits = defect_splits = range_splits = barrier_splits = 0
    index = 0
    stack = []
    last_paid = None
    error = None
    first_step,first_cut = step_journal.rows,cut_journal.rows
    first_commit,first_coverage = commit_journal.rows,coverage_journal.rows
    committed_step_stop,committed_cut_stop = first_step,first_cut
    in_flight = None
    last_unaccepted = None
    transaction_open = None
    try:
        for index,item in enumerate(required):
            panel = item["panel"]
            stack = [(item["left"],item["right"],0)]
            while stack:
                budget.attempt()
                lo,hi,depth = stack.pop()
                in_flight = (lo,hi,depth)
                can_split = depth < args.max_depth and lo < hi
                try:
                    coeff = geometry.get(panel,lo,hi)
                    candidate = advance_candidate(state,coeff,m,lo,hi,args)
                except (ArithmeticError,ZeroDivisionError,OverflowError) as failure:
                    last_unaccepted = dict(original_source_panel_row=panel["row"],
                        closed_parameter_interval=[str(lo),str(hi)],
                        subdivision_depth=depth,original_incoming_state=state_record(state),
                        error=dict(type=type(failure).__name__,message=str(failure)))
                    if can_split:
                        mid = (lo+hi)/2
                        stack.append((mid,hi,depth+1));stack.append((lo,mid,depth+1))
                        range_splits += 1;in_flight = None
                        continue
                    stack.append((lo,hi,depth))
                    raise PanelUnpaid("Complete coefficient/global-angle/small-lift enclosure unresolved: "+str(failure))
                if candidate["needs_norm_split"]:
                    if not can_split:
                        last_unaccepted = dict(original_source_panel_row=panel["row"],
                            closed_parameter_interval=[str(lo),str(hi)],
                            subdivision_depth=depth,
                            original_incoming_state=state_record(state),
                            candidate=candidate_record(candidate))
                        stack.append((lo,hi,depth))
                        raise PanelUnpaid("Declared panel-norm work bound unresolved at maximum depth")
                    mid = (lo+hi)/2
                    stack.append((mid,hi,depth+1));stack.append((lo,mid,depth+1))
                    norm_splits += 1;in_flight = None
                    continue
                if candidate["needs_barrier_split"]:
                    if not can_split:
                        last_unaccepted = dict(original_source_panel_row=panel["row"],
                            closed_parameter_interval=[str(lo),str(hi)],
                            subdivision_depth=depth,
                            original_incoming_state=state_record(state),
                            candidate=candidate_record(candidate))
                        stack.append((lo,hi,depth))
                        raise PanelUnpaid("A numerical enclosure of the proved continuous small-step angle lift remains unresolved")
                    mid = (lo+hi)/2
                    stack.append((mid,hi,depth+1));stack.append((lo,mid,depth+1))
                    barrier_splits += 1;in_flight = None
                    continue
                if not candidate["work_goal_met"] and can_split:
                    mid = (lo+hi)/2
                    stack.append((mid,hi,depth+1));stack.append((lo,mid,depth+1))
                    defect_splits += 1;in_flight = None
                    continue
                # A finite max-depth Taylor-work-coarse enclosure is admissible only
                # after both entire closed small-angle Taylor transports are paid.
                before = state_record(state)
                cut_rows,quotients,updates,unit_rows = prepare_cut_tubes(
                    candidate,coeff,panel,lo,hi,by_panel.get(panel["row"],[]),
                    m,coverage,accepted)
                step = dict(schema=SCHEMA+"-validated-Pruefer-panel",
                    physical_frequency=m,transaction_index=accepted,
                    original_source_panel_row=panel["row"],
                    source_piece=panel["source_piece"],
                    closed_parameter_interval=[str(lo),str(hi)],subdivision_depth=depth,
                    coefficient_row=coeff["coefficient_row"],
                    original_complete_incoming_state=before,
                    input_flux_frame_exponent_change=candidate["input_column_shift"],
                    commit_required_before_this_row_belongs_to_the_paid_prefix=True,
                    Pruefer_comparison_enclosure=candidate_record(candidate))
                budget.check()
                transaction_open = dict(transaction_index=accepted,
                    original_source_panel_row=panel["row"],
                    closed_parameter_interval=[str(lo),str(hi)],
                    prepared_panel_row=step_journal.rows,
                    prepared_cut_rows=dict(first=cut_journal.rows,stop=cut_journal.rows+len(cut_rows)),
                    prior_state=before,
                    candidate_outgoing_state=state_record(candidate["next_state"]))
                # Prepare every interval union and complete scalar record
                # before the journal commit or any change to the live state.
                new_partial_dn = partial_dn
                new_partial_unit_robin = partial_unit_robin
                new_candidate_count = candidate_count
                new_height_unproved_count = height_unproved_count
                new_quotient_error_count = quotient_error_count
                new_legal_count = legal_count
                if not (len(cut_rows) == len(quotients) == len(unit_rows)):
                    raise ValueError("A cut transaction omitted an original candidate unit row")
                for row,quotient,unit_row in zip(cut_rows,quotients,unit_rows):
                    new_partial_unit_robin = (list(unit_row) if new_partial_unit_robin is None
                        else [old.union(new) for old,new in zip(new_partial_unit_robin,unit_row)])
                    new_candidate_count += 1
                    new_height_unproved_count += int(not row["whole_candidate_height_excludes_zero"])
                    new_quotient_error_count += int(row["quotient_error"] is not None)
                    if quotient is not None:
                        new_legal_count += 1
                        new_partial_dn = quotient if new_partial_dn is None else new_partial_dn.union(quotient)
                new_coverage = dict(coverage)
                new_coverage.update(updates)
                new_last_paid = dict(original_source_panel_row=panel["row"],
                    source_piece=panel["source_piece"],parameter=str(hi),
                    complete_state=state_record(candidate["next_state"]),
                    panel_commit_row=commit_journal.rows)
                coarse_increment = int(not candidate["work_goal_met"])
                step_sha = sha(canonical(step))
                step_row = step_journal.rows
                cut_first = cut_journal.rows
                step_journal.add(step)
                for row in cut_rows:
                    row["prepared_panel_row"] = step_row
                    cut_journal.add(row)
                commit_journal.add(dict(schema=SCHEMA+"-committed-panel",
                    physical_frequency=m,transaction_index=accepted,
                    prepared_panel_row=step_row,prepared_panel_canonical_sha256=step_sha,
                    cut_contribution_span=dict(first=cut_first,stop=cut_journal.rows),
                    complete_outgoing_factor_chain_sha256=candidate["next_state"]["factor_chain_sha256"],
                    all_scalar_and_cut_rows_precede_this_commit=True))
                # The last write above is the commit record. No resource
                # check or scientific operation occurs between it and state
                # assignment; prior uncommitted rows cannot pay a prefix.
                state = candidate["next_state"]
                coverage = new_coverage
                partial_dn = new_partial_dn
                partial_unit_robin = new_partial_unit_robin
                candidate_count = new_candidate_count
                height_unproved_count = new_height_unproved_count
                quotient_error_count = new_quotient_error_count
                legal_count = new_legal_count
                accepted += 1
                coarse += coarse_increment
                committed_step_stop = step_journal.rows
                committed_cut_stop = cut_journal.rows
                transaction_open = None;in_flight = None;last_unaccepted = None
                last_paid = new_last_paid
            index += 1
        for leaf in data["leaves"]:
            actual = coverage.get(leaf["leaf_row"])
            if actual is None or (actual["left"],actual["right"]) != (leaf["left"],leaf["right"]):
                raise ValueError("A declared complete Pruefer mode omitted an entire original cut leaf")
        if candidate_count == 0:
            raise ValueError("The complete point cover has no indexed physical cut contribution")
    except Exception as failure:
        if in_flight is not None and in_flight not in stack:
            stack.append(in_flight)
        error = dict(type=type(failure).__name__,message=str(failure))
    pending = pending_description(required,index,stack) if error is not None else None
    complete = error is None
    completed_leaves = 0
    for leaf in data["leaves"]:
        actual = coverage.get(leaf["leaf_row"])
        paid = actual is not None and (
            actual["left"],actual["right"]) == (leaf["left"],leaf["right"])
        completed_leaves += int(paid)
        coverage_journal.add(dict(schema=SCHEMA+"-original-cut-leaf-coverage",
            physical_frequency=m,original_cut_leaf_row=leaf["leaf_row"],
            source_piece=leaf["source_piece"],
            required_closed_parameter_interval=[str(leaf["left"]),str(leaf["right"])],
            committed_covered_closed_interval=(
                [str(actual["left"]),str(actual["right"])] if actual else None),
            complete_original_leaf_spatial_scope_paid=paid,
            committed_candidate_count=actual["candidate_count"] if actual else 0,
            height_condition_unproved_count=actual["height_unproved_count"] if actual else 0,
            legal_quotient_count=actual["legal_quotient_count"] if actual else 0,
            quotient_arithmetic_error_count=actual["quotient_arithmetic_error_count"] if actual else 0,
            same_original_closed_endpoint_not_discarded=True,
            unvisited_original_leaf_not_labelled_geometry_failure=True))
    nonzero = bool(complete and candidate_count > 0 and height_unproved_count == 0)
    all_quotients = bool(nonzero and legal_count == candidate_count and partial_dn is not None)
    if error is not None:
        unpaid_journal.add(dict(kind="incomplete-mode-required-Pruefer-scope",
            physical_frequency=m,error=error,last_paid=last_paid,
            complete_pending_scope=pending,complete_current_state=state_record(state),
            last_unaccepted_candidate=last_unaccepted,
            uncommitted_transaction=transaction_open,
            partial_legal_cut_slope_hull_not_full_cut_claim=True))
    if complete and not all_quotients:
        unpaid_journal.add(dict(kind="complete-spatial-cut-family-with-unpaid-quotient-conditions",
            physical_frequency=m,total_cut_candidates=candidate_count,
            height_condition_unproved_count=height_unproved_count,
            quotient_arithmetic_error_count=quotient_error_count,
            cut_contribution_ledger_span=dict(first=first_cut,stop=committed_cut_stop),
            complete_original_leaf_coverage_span=dict(first=first_coverage,stop=coverage_journal.rows),
            indexed_nondividing_Robin_family_retained=True,
            actual_resonance_or_nonexistence_not_inferred=True))
    return dict(schema=SCHEMA+"-mode-result",physical_frequency=m,mode_index=far["mode_index"],
        original_deep_initial_column=initial,
        complete_required_cut_propagation=complete,
        complete_original_cut_family_enclosed=complete,
        completed_original_cut_leaves=completed_leaves,
        required_original_cut_leaf_count=len(data["leaves"]),
        accepted_closed_panels=accepted,coarse_valid_panels=coarse,
        norm_work_splits=norm_splits,defect_work_splits=defect_splits,
        coefficient_range_splits=range_splits,uncertain_barrier_existence_splits=barrier_splits,
        panel_ledger_span=dict(first=first_step,stop=committed_step_stop),
        panel_commit_ledger_span=dict(first=first_commit,stop=commit_journal.rows),
        cut_contribution_ledger_span=dict(first=first_cut,stop=committed_cut_stop),
        cut_leaf_coverage_ledger_span=dict(first=first_coverage,stop=coverage_journal.rows),
        uncommitted_written_panel_span=dict(first=committed_step_stop,stop=step_journal.rows),
        uncommitted_written_cut_span=dict(first=committed_cut_stop,stop=cut_journal.rows),
        uncommitted_transaction=transaction_open,last_unaccepted_candidate=last_unaccepted,
        last_paid=last_paid,complete_pending_scope=pending,
        complete_current_factorized_state=state_record(state),
        factorized_original_QF_one_column_retained=True,
        materialized_original_QF_one_cut_column=False,
        physical_cut_column=None,original_Robin_row=None,
        angle_indexed_oriented_unit_physical_Robin_family=dict(
            ledger="large-arrays/all-actual-cut-tube-contributions.jsonl",
            committed_rows=dict(first=first_cut,stop=committed_cut_stop),
            candidate_count=candidate_count,complete_spatial_scope=complete,
            each_row_has_its_own_positive_amplitude_family_and_fixed_balance=True,
            different_candidate_scales_not_hulled_as_original_column=True,
            candidate_row_norm_uses_correlated_cos2_plus_K2sin2_lower_bound=True,
            candidate_unit_rows_are_normalized_before_hulling=True),
        complete_physical_unit_Robin_row_hull=(
            [B.record(v) for v in partial_unit_robin] if complete and partial_unit_robin is not None else None),
        partial_physical_unit_Robin_row_hull=(
            [B.record(v) for v in partial_unit_robin] if partial_unit_robin is not None else None),
        full_unit_Robin_hull_requires_complete_spatial_cut_scope=True,
        native_Q_Pi_scale_mu_not_supplied_or_invented=True,
        all_cut_candidate_heights_exclude_zero=nonzero,
        height_condition_unproved_candidate_count=height_unproved_count,
        quotient_arithmetic_error_candidate_count=quotient_error_count,
        cut_candidate_count=candidate_count,legal_cut_quotient_count=legal_count,
        all_cut_candidate_quotients_computed=all_quotients,
        actual_cut_slope_enclosure_computed=all_quotients,
        cut_slope_per_unit_physical_height=B.record(partial_dn) if all_quotients else None,
        partial_legal_cut_slope_hull=B.record(partial_dn) if partial_dn is not None else None,
        partial_hull_is_not_full_cut_DN_unless_all_candidate_conditions_paid=True,
        actual_exact_column_nonzero_by_R312_and_invertibility=True,
        every_binary_frame_change_preserves_the_complete_real_angle_lift=True,
        no_finite_ratio_chart_or_physical_height_condition_used_for_angle_propagation=True,
        auxiliary_small_angle_lifts_use_proved_positive_dots_and_complete_Taylor_errors=True,
        family_uniform_over_every_fixed_original_root_sequence=True,
        unique_original_root_sequence_selected=False,
        nonlinear_DN_or_full_BVP_claimed=False,error=error)


def argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cover-directory",type=Path,required=True)
    parser.add_argument("--cover-result-sha256",required=True)
    parser.add_argument("--far-directory",type=Path,required=True)
    parser.add_argument("--far-result-sha256",required=True)
    parser.add_argument("--code-directory",type=Path,required=True)
    parser.add_argument("--proof",type=Path,required=True)
    parser.add_argument("--mode-extension-proof",type=Path,required=True)
    parser.add_argument("--field-modes",type=int,required=True)
    parser.add_argument("--precision-bits",type=int,default=256)
    parser.add_argument("--budget-seconds",type=float,default=14400)
    parser.add_argument("--max-panels",type=int,default=25000000)
    parser.add_argument("--free-bytes-reserve",type=int,default=2147483648)
    parser.add_argument("--max-depth",type=int,default=32)
    parser.add_argument("--local-defect-bits",type=int,default=12)
    parser.add_argument("--panel-norm-limit",type=Q,default=Q(1,4))
    parser.add_argument("--taylor-terms",type=int,default=24)
    parser.add_argument("--max-geometry-cache-records",type=int,default=65536)
    parser.add_argument("--out",type=Path,required=True)
    return parser


def main(argv=None):
    args = argument_parser().parse_args(argv)
    require_actions()
    modes = requested_modes(args.field_modes)
    if (not 128 <= args.precision_bits <= 8192 or not 0 <= args.max_depth <= 128
            or not 0 <= args.local_defect_bits <= 1024
            or not 1 <= args.taylor_terms <= 256
            or args.max_panels <= 0 or args.max_geometry_cache_records <= 0
            or args.free_bytes_reserve <= 0
            or not math.isfinite(args.budget_seconds) or args.budget_seconds <= 0
            or not 0 < args.panel_norm_limit <= Q(1,4)):
        raise ValueError("Use explicit positive finite work parameters in the implemented range")
    if args.out.exists():
        raise ValueError("Use a fresh request-owned temporary output directory")
    for path in (args.cover_directory,args.far_directory,args.code_directory,args.proof,args.mode_extension_proof):
        if path.resolve().is_relative_to(args.out.resolve()):
            raise ValueError("The output cannot own an original input or scientific source")
    data = bind_inputs(args)
    runtime,sources,proof = load_runtime(args)
    args.out.mkdir(parents=True)
    large = args.out/"large-arrays"
    large.mkdir()
    binding = data["binding"]
    work = {key:getattr(args,key) for key in (
        "precision_bits","budget_seconds","max_panels","max_depth",
        "local_defect_bits","taylor_terms","max_geometry_cache_records","free_bytes_reserve")}
    work["panel_norm_limit"] = str(args.panel_norm_limit)
    binding.update(actual_frozen_sources=sources,actual_R380_proof=proof,
        original_181_Pruefer_source_sha256=ORIGINAL_PRUEFER_SHA,
        positive_endpoint_operations_source_sha256=POSITIVE_ENDPOINT_SHA,
        original_R375_source_preserved=sources[PREVIOUS_RICCATI_NAME],
        original_R375_comparison_proof_sha256=PREVIOUS_RICCATI_PROOF_SHA,
        original_R324_tube_proof_sha256=BASE_TUBE_PROOF_SHA,
        original_R324_source_preserved=sources[BASE_PROPAGATOR_NAME],
        original_R347_source_preserved=sources[PREVIOUS_PROJECTIVE_NAME],
        original_R347_projective_proof_sha256=PROJECTIVE_PROOF_SHA,
        runtime=runtime,numerical_work_parameters=work,
        work_goal_scope="complete Taylor remainder for the global angle barriers; physical height and DN remain independent",
        work_goals_are_not_new_BVP_acceptance_gates=True)
    binding_rec = write_json(args.out/"input-binding.json",binding)
    coefficient_journal = B.Journal(large/"actual-closed-coefficient-boxes.jsonl",args.out)
    step_journal = B.Journal(large/"complete-accepted-panel-tubes.jsonl",args.out)
    cut_journal = B.Journal(large/"all-actual-cut-tube-contributions.jsonl",args.out)
    commit_journal = B.Journal(large/"complete-projective-panel-commits.jsonl",args.out)
    coverage_journal = B.Journal(large/"complete-original-cut-leaf-coverage.jsonl",args.out)
    mode_journal = B.Journal(large/"complete_M-mode-status-and-columns.jsonl",args.out)
    unpaid_journal = B.Journal(large/"complete-unpaid-scope.jsonl",args.out)
    budget = Budget(args)
    rows = []
    head = cache = None
    required_receipt = None
    nonrequired_suffix = None
    required_count = 0
    top_error = None
    started_modes = []
    completed_modes = []
    nonzero_modes = []
    not_started = list(modes)
    active_mode = None
    try:
        if not data["ready"]:
            unpaid_journal.add(dict(kind="whole-required-cut-propagation",
                original_scope_conditions=data["facts"],all_modes=list(modes),
                no_actual_denominator_or_ODE_claim=True,
                original_point_result_retained_in_input_binding=True))
        else:
            budget.check(force_storage=True)
            cb = data["core"]
            head = B.ContinuousHead(cb["physical_parameters"],cb["original_shallow_rows"],
                cb["original_frozen_warp_alpha"],cb)
            # Same real expressions; intervals need only intersect. A source
            # schema or an arbitrary metadata label is not a replacement.
            original_inner = as_ball(data["far"]["original_R286_deep_geometry"]["radius"])
            B.intersect_known(head.inner_radius,original_inner.lower(),original_inner.upper())
            if data["panels"]:
                first_radius = as_ball(data["panels"][0]["radius_left"])
                B.intersect_known(head.inner_radius,first_radius.lower(),first_radius.upper())
            by_panel,required,nonrequired_suffix = associate_cut_leaves(data)
            required_count = len(required)
            required_receipt = write_json(args.out/"required-source-panels.json",
                dict(schema=SCHEMA+"-required-original-source-prefix",
                    complete_original_source_stream=data["cover"]["ledgers"]["source_radial_panels"],
                    original_complete_cut_leaf_stream=data["cover"]["ledgers"]["query_inverse_cover"],
                    all_point_leaves_included=True,
                    required=[dict(original_source_panel_row=x["panel"]["row"],
                        source_piece=x["panel"]["source_piece"],
                        closed_parameter_interval=[str(x["left"]),str(x["right"])])
                        for x in required],
                    original_full_source_after_required_cut_cover=nonrequired_suffix))
            cache = GeometryCache(head,data["panels"],args,coefficient_journal,budget)
            for far in data["far_rows"]:
                try:
                    budget.check()
                except WorkStop as failure:
                    top_error = dict(type=type(failure).__name__,message=str(failure))
                    break
                m = far["physical_frequency"]
                started_modes.append(m)
                not_started.remove(m)
                active_mode = m
                row = propagate_mode(far,data,required,by_panel,cache,args,budget,
                    step_journal,cut_journal,commit_journal,coverage_journal,unpaid_journal)
                rows.append(row)
                mode_journal.add(row)
                active_mode = None
                if row["complete_required_cut_propagation"]:
                    completed_modes.append(m)
                if row["all_cut_candidate_heights_exclude_zero"]:
                    nonzero_modes.append(m)
                print(json.dumps(dict(event="R380-original-C-Pruefer-head-mode-result",
                    physical_frequency=m,
                    complete_required_cut_propagation=row["complete_required_cut_propagation"],
                    all_cut_candidate_heights_exclude_zero=row["all_cut_candidate_heights_exclude_zero"],
                    accepted_closed_panels=row["accepted_closed_panels"],
                    valid_coarse_panels=row["coarse_valid_panels"],
                    error=row["error"],elapsed_seconds=time.monotonic()-budget.started)),flush=True)
                if row["error"] is not None:
                    top_error = row["error"]
                    # Preserve this mode's full stack and every unstarted
                    # mode. Do not fabricate rows or silently restart it.
                    break
    except Exception as failure:
        top_error = dict(type=type(failure).__name__,message=str(failure))
        if active_mode is not None:
            failed = dict(schema=SCHEMA+"-mode-result",
                physical_frequency=active_mode,mode_index=active_mode//2-1,
                started=True,complete_required_cut_propagation=False,
                all_cut_candidate_heights_exclude_zero=False,
                all_cut_candidate_quotients_computed=False,
                actual_cut_slope_enclosure_computed=False,
                accepted_closed_panels=None,coarse_valid_panels=None,
                no_zero_count_inferred_from_unreturned_mode=True,
                materialized_original_QF_one_cut_column=False,
                physical_cut_column=None,original_Robin_row=None,
                cut_slope_per_unit_physical_height=None,
                whole_original_cut_query_unpaid=True,
                complete_pending_scope=dict(
                    whole_required_source_prefix=required_receipt,
                    reason="Failure before a complete mode result was returned"),
                error=top_error)
            rows.append(failed)
            mode_journal.add(failed)
        unpaid_journal.add(dict(kind="producer-exception",error=top_error,
            unstarted_modes=not_started,
            all_unfinished_required_source_scopes_remain_unpaid=True))
    finally:
        if not_started:
            unpaid_journal.add(dict(kind="complete-unstarted-mode-suffix",
                physical_frequencies=not_started,far_port=159,
                required_source_scope_file=required_receipt,
                whole_original_cut_query_id=QUERY_ID,
                complete_required_source_if_unstarted=True))
            for m in not_started:
                mode_journal.add(dict(schema=SCHEMA+"-mode-result",
                    physical_frequency=m,mode_index=m//2-1,started=False,
                    complete_required_cut_propagation=False,
                    all_cut_candidate_heights_exclude_zero=False,
                    all_cut_candidate_quotients_computed=False,
                    actual_cut_slope_enclosure_computed=False,
                    materialized_original_QF_one_cut_column=False,
                    accepted_closed_panels=0,coarse_valid_panels=0,
                    physical_cut_column=None,original_Robin_row=None,
                    cut_slope_per_unit_physical_height=None,
                    whole_original_cut_query_unpaid=True))
        ledgers = dict(coefficients=coefficient_journal.finish(),
            accepted_panels=step_journal.finish(),
            cut_tube_contributions=cut_journal.finish(),
            projective_panel_commits=commit_journal.finish(),
            cut_leaf_coverage=coverage_journal.finish(),
            complete_M_mode_status_and_columns=mode_journal.finish(),
            complete_unpaid_scope=unpaid_journal.finish())
    all_families = len(completed_modes) == len(modes)
    all_heights = all_families and len(nonzero_modes) == len(modes)
    all_dn = all_heights and all(r.get("actual_cut_slope_enclosure_computed") is True for r in rows)
    diagonal_rec = None
    if all_dn:
        diagonal_rec = write_json(large/"complete_M-linear-cut-DN-diagonal.json",
            dict(schema=SCHEMA+"-complete-diagonal",
                source_sha256=sha(Path(__file__).read_bytes()),
                input_binding=binding_rec,target_model_schema=MODEL_SCHEMA,
                physical_frequencies=list(modes),
                slope_units="physical dH/dr per unit physical H",
                diagonal_enclosures=[r["cut_slope_per_unit_physical_height"] for r in rows],
                original_root_choice_resolved=False,
                uniform_over_every_fixed_admissible_original_root_sequence=True,
                actual_nonlinear_DN_existence_or_derivative_not_inferred=True))
        diagonal_rec["file"] = "large-arrays/"+diagonal_rec["file"]
    row_summaries = [dict(physical_frequency=r["physical_frequency"],
        completed_original_cut_leaves=r.get("completed_original_cut_leaves"),
        required_original_cut_leaf_count=r.get("required_original_cut_leaf_count"),
        cut_candidate_count=r.get("cut_candidate_count"),
        height_condition_unproved_candidate_count=r.get("height_condition_unproved_candidate_count"),
        legal_cut_quotient_count=r.get("legal_cut_quotient_count"),
        complete_pending_scope=r.get("complete_pending_scope"),
        last_paid_source_coordinate=(dict(original_source_panel_row=r["last_paid"]["original_source_panel_row"],
            source_piece=r["last_paid"]["source_piece"],parameter=r["last_paid"]["parameter"])
            if r.get("last_paid") else None),
        complete_required_cut_propagation=r["complete_required_cut_propagation"],
        all_cut_candidate_heights_exclude_zero=r["all_cut_candidate_heights_exclude_zero"],
        accepted_closed_panels=r["accepted_closed_panels"],
        coarse_valid_panels=r["coarse_valid_panels"],
        error=r["error"]) for r in rows]
    report = dict(schema=SCHEMA,source_sha256=sha(Path(__file__).read_bytes()),
        repository=REPOSITORY,run_id=os.environ["GITHUB_RUN_ID"],
        source_commit=os.environ["GITHUB_SHA"],target_model_schema=MODEL_SCHEMA,
        actual_R380_proof=proof,
        original_181_Pruefer_source_sha256=ORIGINAL_PRUEFER_SHA,
        positive_endpoint_operations_source_sha256=POSITIVE_ENDPOINT_SHA,
        exact_positive_endpoints_retained_before_Arb_union=True,
        wide_reciprocal_enclosures_used_only_as_multipliers=True,
        original_R375_source_sha256=PREVIOUS_RICCATI_SHA,
        original_R375_comparison_proof_sha256=PREVIOUS_RICCATI_PROOF_SHA,
        original_R324_tube_proof_sha256=BASE_TUBE_PROOF_SHA,
        original_R347_source_sha256=PREVIOUS_PROJECTIVE_SHA,
        original_R347_projective_proof_sha256=PROJECTIVE_PROOF_SHA,
        actual_R312_proof_sha256=TAIL_PROOF_SHA,
        actual_R442_proof=binding["actual_R442_proof"],
        field_modes=args.field_modes,
        actual_M_theorem_applicability=binding["actual_M_theorem_applicability"],
        runtime=runtime,numerical_work_parameters=work,input_binding=binding_rec,
        actual_scope_conditions=data["facts"],
        actual_cover_result=binding["actual_cover_result"],actual_far_result=binding["actual_far_result"],
        actual_cover_complete_source=binding["actual_complete_source_stream"],
        actual_complete_cut_inverse_cover=binding["actual_complete_inverse_stream"],
        actual_complete_deep_rows=binding["actual_complete_deep_row_stream"],
        original_binary_cut_exact_rational=str(data["cut"]),
        natural_outer_radius=data["cover"]["natural_outer_radius"],
        original_point_work_resolution_complete=(
            binding["actual_point_query"].get("work_resolution_complete")
            if binding["actual_point_query"] is not None else None),
        original_whole_cover_work_resolution_complete=data["cover"]["numerical_work_resolution_complete"],
        original_cover_error=data["cover"]["error"],
        original_unvisited_query_suffix=data["cover"]["unvisited_query_suffix"],
        selected_actual_cut_leaf_count=len(data["leaves"]),
        required_original_source_panel_count=required_count,
        required_source_panel_index=required_receipt,
        original_full_source_after_required_cut_cover=nonrequired_suffix,
        complete_requested_modes=list(modes),started_modes=started_modes,
        completed_factorized_cut_family_modes=completed_modes,
        actual_nonzero_height_modes=nonzero_modes,complete_unstarted_mode_suffix=not_started,
        unpaid_cut_height_modes=[m for m in completed_modes if m not in nonzero_modes],
        all_complete_M_factorized_cut_families_enclosed=all_families,
        all_complete_M_physical_cut_columns_materialized=False,
        all_complete_M_oriented_unit_physical_Robin_families_enclosed=all_families,
        all_complete_M_height_denominators_verified=all_heights,
        all_complete_M_cut_slope_enclosures_computed=all_dn,
        complete_M_cut_DN_diagonal=diagonal_rec,
        complete_original_mode_scope=ledgers["complete_M_mode_status_and_columns"],
        detailed_ledgers=ledgers,started_mode_summaries=row_summaries,
        total_panel_attempts=budget.attempts,actual_linear_resource_scope=budget.record(),
        new_complete_expression_range_evaluations=cache.range_calls if cache else 0,
        coefficient_cache_hits=cache.hits if cache else 0,
        original_six_primitive_integrations_repeated=0,
        original_root_calibrations_or_choices_performed=0,
        true_new_interval_linear_ODE_propagation_attempted=budget.attempts > 0,
        physical_state_coordinates=["u","k=dH/dr"],
        internal_continuous_flux_coordinates=["u","j=w*k"],
        exact_power_of_two_frame_and_amplitude_factors_recorded=True,
        all_cut_candidates_retain_their_own_positive_amplitude_and_flux_frame=True,
        all_original_cut_tubes_materialized_in_same_QF_one_normalization=False,
        original_QF_one_normalization_preserved_in_factorized_columns=True,
        different_candidate_scales_not_hulled_as_original_column=True,
        all_prior_interval_uncertainty_propagated=True,
        original_source_length_not_multiplied_twice=True,
        old_Pi_port_factor_not_reapplied=True,
        complete_unwrapped_angle_lifts_preserved_across_every_positive_binary_frame_change=True,
        cut_DN_hull_taken_only_after_individual_legal_candidate_divisions=True,
        original_C_object_or_frozen_warp_changed=False,
        initial_family_recomputed_from_original_deep_rows_not_previous_propagated_boxes=True,
        full_panel_coefficient_variation_retained_by_comparison=True,
        scalar_barrier_Taylor_error_multiplies_complete_initial_column=True,
        global_angle_barriers_do_not_require_nonzero_height_or_any_finite_ratio_chart=True,
        small_auxiliary_steps_use_full_positive_dot_proof_and_Taylor_error=True,
        exact_unit_Robin_norm_lower_bound_preserves_angle_correlation=True,
        candidate_unit_Robin_normalization_precedes_any_cross_candidate_hull=True,
        actual_angle_not_assumed_monotone=True,
        positive_amplitude_and_log_propagated_over_full_closed_panels=True,
        native_Q_Pi_scale_mu_not_supplied_or_invented=True,
        native_Q_Pi_Robin_rows_not_claimed=True,
        actual_unique_deep_root_sequence_selected=False,
        result_is_uniform_root_family_enclosure=True,
        old_finite_zero_J_or_readylineargraph_used=False,
        actual_nonlinear_tail_DN_existence_or_differentiability_proved=False,
        actual_nonlinear_solve=False,full_BVP_or_closed_surface_accepted=False,
        physical_boundary_material_pullback_not_applied_twice=True,
        interval_work_goal_not_new_BVP_acceptance_gate=True,
        error=top_error,elapsed_seconds=time.monotonic()-budget.started,
        raw_outputs_are_request_owned_temporary_recomputable_data=True)
    result_rec = write_json(args.out/"result.json",report)
    summary = dict(report,actual_result_file=result_rec)
    raw = canonical(summary)
    if len(raw) > SUMMARY_LIMIT:
        print(json.dumps(dict(event="R380-summary-over-transport-budget",
            bytes=len(raw),sha256=sha(raw),actual_result_file=result_rec,
            complete_temporary_result_retained=True,
            scientific_success_or_failure_not_inferred_from_transport=True)),flush=True)
        return 70
    print("BEGIN_R380_CONTINUOUS_C_POSITIVE_ENDPOINT_PRUEFER_HEAD_SUMMARY",flush=True)
    print(raw.decode(),end="",flush=True)
    print("END_R380_CONTINUOUS_C_POSITIVE_ENDPOINT_PRUEFER_HEAD_SUMMARY",flush=True)
    print(json.dumps(dict(event="R380-Pruefer-head-summary-identity",bytes=len(raw),
        sha256=sha(raw),actual_result_file=result_rec,
        hash_scope="canonical UTF8 JSON including final LF")),flush=True)
    output = os.environ.get("GITHUB_OUTPUT")
    if output:
        with open(output,"a") as stream:
            stream.write("finite_head_summary="+raw.decode().rstrip("\n")+"\n")
            stream.write("finite_head_summary_bytes="+str(len(raw))+"\n")
            stream.write("finite_head_summary_sha256="+sha(raw)+"\n")
    return 0 if all_families else 2


if __name__ == "__main__":
    raise SystemExit(main())
