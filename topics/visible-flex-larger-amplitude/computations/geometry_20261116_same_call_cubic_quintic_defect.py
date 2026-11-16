#!/usr/bin/env python3
"""R569 same-call literal solver cubic versus the actual accurate quintic.

This library does not run a solve, create an accepted checkpoint, change a
solver/metric gate or infer an error bound from a scalar RMS.  A future
explicit caller may install the transparent return recorder around its real
original solve_bvp call.  The original object is returned unchanged.  Only
that same accepted call's complete PPoly words can bind the comparison.
Numerical evaluation is restricted to the named public Actions.
Author: geometry agent (AI), 2026-11-16.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import inspect
import json
import math
import os
from pathlib import Path
import struct
import sys
import traceback

REPOSITORY = "Rogerhu12/math-research-public"
HERE = Path(__file__).resolve().parent
SCHEMA = "R569-same-call-literal-cubic-and-accurate-quintic-v1"
TUBE_NAME = "geometry_20261116_actual_prefix_coefficient_tube_majorants.py"
TUBE_SHA = "81d33e7135eeba50b7d0b372d82cbcd656f0da34cf3f2691792f865e2dada96b"
CORE_NAME = "geometry_20261114_full_dn_solve.py"
CORE_SHA = "c6a1f4d8025508ee49fe9324b3401440a2de88329d0b78ef0d0814860c2d3162"
ACTIVE_NAME = "geometry_20261115_shared_active_interval_balls.py"
ACTIVE_SHA = "675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b"
ORDINARY_ERRORS = (ArithmeticError, ValueError, TypeError, KeyError,
                   IndexError, AttributeError, OSError)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
            "Only the named public Actions may evaluate the captured field")


def run_identity():
    return {key: os.environ.get(key) for key in
            ("GITHUB_REPOSITORY", "GITHUB_RUN_ID", "GITHUB_RUN_ATTEMPT", "GITHUB_SHA")}


def encode(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {key: encode(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [encode(item) for item in value]
    return value


def canonical(value):
    return (json.dumps(encode(value), sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False)+"\n").encode("utf-8")


def identity(path):
    path = Path(path).resolve()
    raw = path.read_bytes()
    return dict(file=str(path), bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def same_payload(left, right):
    return (isinstance(left, dict) and isinstance(right, dict)
            and left.get("bytes") == right.get("bytes")
            and left.get("sha256") == right.get("sha256"))


def bound_file(path, descriptor):
    actual = identity(path)
    require(same_payload(actual, descriptor), "The complete actual file identity differs")
    return actual


def load_tube():
    path = HERE/TUBE_NAME
    record = identity(path)
    require(record["sha256"] == TUBE_SHA, "The original actual-tube helper differs")
    tag = "_r569_bound_r553_"+TUBE_SHA
    module = sys.modules.get(tag)
    if module is None:
        spec = importlib.util.spec_from_file_location(tag, path)
        require(spec is not None and spec.loader is not None, "The R553 loader is unavailable")
        module = importlib.util.module_from_spec(spec)
        sys.modules[tag] = module
        try:
            spec.loader.exec_module(module)
        except BaseException:
            sys.modules.pop(tag, None)
            raise
    require(Path(module.__file__).resolve() == path.resolve()
            and module.SCHEMA == "R553-actual-complete-prefix-coefficient-tube-majorants-v1",
            "The actual R553 module owner differs")
    return module, record


def array_record(np, value):
    """The actual finite binary64 words, not a re-evaluation of a spline."""
    a = np.asarray(value)
    require(a.dtype.kind == "f" and a.dtype.itemsize == 8
            and np.all(np.isfinite(a)), "Retain the complete finite original binary64 array")
    a = np.asarray(a, dtype="<f8", order="C")
    raw = a.tobytes(order="C")
    return raw, dict(dtype="<f8", shape=list(a.shape), bytes=len(raw),
                     sha256=hashlib.sha256(raw).hexdigest())


def read_json(path):
    path = Path(path)
    receipt = identity(path)
    raw = path.read_bytes()
    value = json.loads(gzip.decompress(raw) if path.suffix == ".gz" else raw)
    return value, receipt


def write_new(path, raw):
    path = Path(path)
    with path.open("xb") as stream:
        stream.write(raw)
        stream.flush()
    return identity(path)


def member(root, row):
    name = row["file"]
    require(isinstance(name, str) and Path(name).name == name,
            "Every retained member is a direct file of this owned capsule")
    path = Path(root)/name
    require(path.is_file() and not path.is_symlink(), "The complete retained member is absent")
    raw = path.read_bytes()
    require(len(raw) == row["bytes"] and hashlib.sha256(raw).hexdigest() == row["sha256"],
            "The complete retained member payload differs")
    return raw


class SameCallCubicCapture:
    """Transparent explicit instrumentation of the actual original solve call.

    The caller must retain its real source/owner/deadline registrations.  This
    class is not automatically installed by any published current driver.
    Binding failures here are diagnostic unavailable records, never new
    BVP success or acceptance.  Original resource exceptions still propagate.
    """
    def __init__(self, core, *, actual_driver_source, field_modes,
                 physical_size, augmented_size, budget_check,
                 actual_clock_receipt):
        actions()
        require(type(field_modes) is int and field_modes > 0
                and physical_size == 3*field_modes+2
                and type(augmented_size) is int and augmented_size >= physical_size,
                "Use the real complete flow dimensions")
        self.core = core
        self.core_source = identity(core.__file__)
        require(Path(core.__file__).name == CORE_NAME
                and self.core_source["sha256"] == CORE_SHA,
                "The actual unchanged complete full-DN module must own this solve")
        self.driver = identity(actual_driver_source)
        self.np = core.np
        self.M, self.n, self.dimension = field_modes, physical_size, augmented_size
        self.budget_check = budget_check
        require(callable(budget_check), "Use the already owned caller's original budget callback")
        require(isinstance(actual_clock_receipt, dict)
                and all(key in actual_clock_receipt for key in ("file", "bytes", "sha256")),
                "Keep the actual caller's retained clock document identity")
        self.clock = bound_file(actual_clock_receipt["file"], actual_clock_receipt)
        self.original = core.solve_bvp
        self.installed = False
        self.call_count = 0
        self.last = None
        self.last_error = None
        self.source = identity(__file__)
        function_file = inspect.getsourcefile(self.original)
        require(function_file is not None, "The actual original solver has no source file")
        self.original_solver = dict(module=getattr(self.original, "__module__", None),
            name=getattr(self.original, "__name__", None), source=identity(function_file))
        self.scope = dict(original_core_source=self.core_source, actual_driver_source=self.driver,
            actual_solver_callable=self.original_solver, actual_clock=self.clock,
            transparent_return_recorder_source=self.source,
            original_solver_object_returned_without_mutation=True,
            no_new_solve_or_RHS_evaluation=True,
            full_current_owner_registration_not_supplied_by_this_library=True)

        def wrapped(*args, **kwargs):
            self.budget_check()
            self.call_count += 1
            self.last = None
            self.last_error = None
            # Never catch or relabel an exception from the actual original solve.
            answer = self.original(*args, **kwargs)
            self.budget_check()
            try:
                self.last = self.snapshot(answer)
            except ORDINARY_ERRORS as error:
                self.last_error = dict(type=type(error).__name__, message=str(error),
                    traceback=traceback.format_exc(), call_index=self.call_count-1,
                    original_solve_returned=True, source_capture_unavailable=True)
            return answer
        self.wrapper = wrapped

    def __enter__(self):
        require(not self.installed and self.core.solve_bvp is self.original,
                "Do not overlap another actual solve wrapper")
        self.core.solve_bvp = self.wrapper
        self.installed = True
        return self

    def __exit__(self, kind, value, trace):
        if self.installed and self.core.solve_bvp is self.wrapper:
            self.core.solve_bvp = self.original
        self.installed = False
        return False

    def snapshot(self, answer):
        """Copy all words while the same returned solver object is still live."""
        self.budget_check()
        np = self.np
        x = np.asarray(answer.x)
        y = np.asarray(answer.y)
        yp = np.asarray(answer.yp)
        spline = answer.sol
        sx = np.asarray(spline.x)
        c = np.asarray(spline.c)
        require(x.ndim == 1 and len(x) >= 2 and np.all(np.diff(x) > 0),
                "Retain every actual increasing final solver mesh node")
        require(y.shape == yp.shape == (self.dimension, len(x))
                and c.shape == (4, len(x)-1, self.dimension)
                and np.asarray(answer.rms_residuals).shape == (len(x)-1,),
                "The original PPoly lost a power, interval, physical, core or control row")
        rawx, idx = array_record(np, x)
        raws, ids = array_record(np, sx)
        require(rawx == raws and idx == ids and int(spline.axis) == 1,
                "The literal PPoly and actual solve have different complete node words")
        rows = {"mesh": (rawx, idx)}
        for name, value in (("augmented_states", y.T),
                            ("original_spline_rhs", yp.T),
                            ("ppoly_coefficients", c),
                            ("original_rms_residuals", np.asarray(answer.rms_residuals))):
            rows[name] = array_record(np, value)
            self.budget_check()
        p = np.asarray([] if answer.p is None else answer.p, dtype=np.float64)
        rows["solver_parameters"] = array_record(np, p)
        return dict(call_index=self.call_count-1, members=rows,
            status=int(answer.status), success=bool(answer.success),
            message=str(answer.message), niter=int(answer.niter),
            field_modes=self.M, physical_size=self.n, augmented_size=self.dimension,
            node_count=len(x), interval_count=len(x)-1,
            coefficient_layout="PPoly.c[descending_power,interval,all_augmented_columns]",
            exact_literal_polynomial="sum(c[3-j,i,k]*(s-x[i])**j,j=0..3)",
            both_mean_columns_and_all_actual_augmented_rows_retained=True,
            dtype_and_signed_zero_word_identity_retained=True)

    def write_for_accepted_result(self, *, original_result, out):
        """Freeze only this same returned accepted result, or a truthful unpaid receipt.

        No original checkpoint, result file, solver object or source is changed.
        The future registered caller owns retention/readback/cleanup of out.
        """
        actions()
        self.budget_check()
        out = Path(out).resolve()
        root = Path(os.environ["RUNNER_TEMP"]).resolve()
        require(not out.exists() and out.is_relative_to(root),
                "Use a fresh owned temporary capture directory")
        require(not Path(original_result).resolve().is_relative_to(out),
                "The new capture cannot own the original full-DN result input")
        out.mkdir(parents=True)
        result = dict(schema=SCHEMA+"-capture", repository=REPOSITORY, run=run_identity(),
            source=self.source, source_scope=copy.deepcopy(self.scope),
            call_count=self.call_count, complete=False, error=None,
            capture_error=copy.deepcopy(self.last_error), members={},
            original_fullDN=None, original_checkpoint_not_rewritten=True,
            original_BVP_acceptance_not_changed=True,
            numerical_operator_or_continuous_metric_certified=False)
        try:
            raw, receipt = read_json(original_result)
            result["original_fullDN"] = receipt
            require(raw.get("source_sha256") == CORE_SHA
                    and raw.get("success") is True and raw.get("status") == 0,
                    "A true original accepted full-DN result is required for this diagnostic input")
            require(self.last is not None and self.last["success"]
                    and self.last["status"] == 0, "The same last actual cubic was not captured")
            np = self.np
            accepted_x = array_record(np, np.asarray(raw["mesh"], dtype=np.float64))
            accepted_y = array_record(np, np.asarray(raw["augmented_states"], dtype=np.float64))
            require(accepted_x == self.last["members"]["mesh"]
                    and accepted_y == self.last["members"]["augmented_states"],
                    "This accepted result is not the complete captured same-call mesh and iterate")
            require(raw["M"] == self.M
                    and np.asarray(raw["states"]).shape == (self.last["node_count"], self.n),
                    "The complete physical field dimension differs")
            physical_raw, physical_id = array_record(np, np.asarray(raw["states"], dtype=np.float64))
            physical_rhs_raw, physical_rhs_id = array_record(np, np.asarray(raw["rhs"], dtype=np.float64))
            require(np.asarray(raw["augmented_rhs"]).shape == (self.last["node_count"], self.dimension),
                    "The recomputed complete augmented RHS is missing")
            augmented_rhs = array_record(np, np.asarray(raw["augmented_rhs"], dtype=np.float64))
            require(np.asarray(raw["rhs"]).shape == (self.last["node_count"], self.n),
                    "The entire actual frozen-physical RHS is missing")
            records = dict(self.last["members"])
            records["physical_states"] = (physical_raw, physical_id)
            records["frozen_physical_rhs"] = (physical_rhs_raw, physical_rhs_id)
            records["recomputed_augmented_rhs"] = augmented_rhs
            for name, (payload, descriptor) in records.items():
                self.budget_check()
                basename = name+".f64le"
                actual = write_new(out/basename, payload)
                require(same_payload(actual, descriptor), "The actual full capture write differs")
                result["members"][name] = dict(descriptor, file=basename)
            result["literal_cubic"] = {key: copy.deepcopy(value)
                for key, value in self.last.items() if key != "members"}
            result.update(complete=True, original_actual_acceptance_preserved=True,
                actual_original_fullDN_arrays_match=True,
                physical_RHS_is_not_assumed_original_spline_RHS=True,
                original_spline_RHS_is_not_assumed_fresh_augmented_RHS=True,
                actual_spline_RHS_words_equal_fresh_augmented_RHS=(
                    self.last["members"]["original_spline_rhs"] == augmented_rhs),
                original_RMS_array_retained_but_not_a_uniform_error_bound=True,
                original_complete_scalar_profile_identity=dict(
                    bytes=len(canonical(raw["complete_scalar_profile"])),
                    sha256=hashlib.sha256(canonical(raw["complete_scalar_profile"])).hexdigest()),
                current_exact_quintic_must_be_independently_bound_by_its_real_loader=True)
        except ORDINARY_ERRORS as error:
            result["error"] = dict(type=type(error).__name__, message=str(error),
                                   traceback=traceback.format_exc())
            result["unpaid"] = "The same-call literal cubic capsule was not completely bound"
        self.budget_check()
        result_path = out/"result.json"
        write_new(result_path, canonical(result))
        return result, identity(result_path)


def exact_f64(raw):
    require(len(raw) == 8, "Retain one complete binary64 word")
    value = struct.unpack("<d", raw)[0]
    require(math.isfinite(value), "A nonfinite coefficient has no exact finite dyadic lift")
    return Q.from_float(value)


def raw_at(raw, index):
    return raw[8*index:8*(index+1)]


def record_array_equal(np, value, row, payload):
    raw, actual = array_record(np, value)
    return same_payload(actual, row) and actual.get("shape") == row.get("shape") and raw == payload


def hermite_cubic(left, right, width):
    """Canonical exact cubic from current Q's own dyadic values and first jets."""
    y0, d0 = left
    y1, d1 = right
    h = width
    a = y1-y0-h*d0
    b = h*(d1-d0)
    return y0, h*d0, 3*a-b, b-2*a


def pad(values, length):
    require(len(values) <= length, "No power may be truncated")
    return tuple(values)+(Q(0),)*(length-len(values))


def difference(a, b):
    size = max(len(a), len(b))
    return tuple(x-y for x, y in zip(pad(a, size), pad(b, size)))


def hull(a, b):
    return min(a[0], b[0]), max(a[1], b[1])


def endpoint(coefficients, order, h, right):
    values = tuple(coefficients)
    for _ in range(order):
        values = tuple(j*values[j]/h for j in range(1, len(values))) or (Q(0),)
    return sum(values, Q(0)) if right else values[0]


class BoundCubicQuintic:
    """Same actual CP/675 expression, captured original cubic and complete powers."""
    def __init__(self, current, *, capture_result, capture_sha256,
                 angular_count, sqrt_bits, budget_check):
        actions()
        self.current, self.field, self.Active = current, current.field, current.Active
        self.budget_check = budget_check
        self.T, self.tube_source = load_tube()
        self.api, self.majorant_source = self.T.load_majorants()
        self.coefficient_source = self.T.actual_module(
            self.field.prefix_coefficients, ACTIVE_NAME, ACTIVE_SHA)
        require(type(angular_count) is int and type(sqrt_bits) is int
                and angular_count > 0 and sqrt_bits > 0,
                "Use actual angular resolution and explicit existing square-root work bits")
        self.N, self.sqrt_bits, self.M = angular_count, sqrt_bits, int(self.field.M)
        require(self.N == int(self.field.saved.N),
                "Use the actual current prefix angular quadrature, not a new reference grid")
        self.n = 3*self.M+2
        self.rho_lower = self.T.exact(self.field.rho_lower)
        require(self.rho_lower > 0,
                "Retain the existing actual675 complete material-density certificate")
        self.cp = self.field.saved.checkpoint
        path = Path(capture_result).resolve()
        receipt = identity(path)
        require(receipt["sha256"] == capture_sha256, "The actual capture result differs")
        data = json.loads(path.read_bytes())
        require(data["schema"] == SCHEMA+"-capture" and data["complete"] is True
                and data["error"] is None and data["run"] == run_identity(),
                "Use a complete same-job same-source actual cubic capsule")
        require(same_payload(data["source"], identity(__file__)),
                "The actual capture source differs from this explicit library")
        require(same_payload(data["original_fullDN"], self.cp.manifest["members"]["fullDN"])
                and same_payload(data["source_scope"]["actual_driver_source"],
                                 self.cp.manifest["actual_driver_source"]),
                "The captured cubic belongs to another actual accepted checkpoint or driver")
        scalar = data["literal_cubic"]
        require((scalar["field_modes"], scalar["physical_size"]) == (self.M, self.n),
                "All current physical frequencies and both means are required")
        self.members = data["members"]
        self.payloads = {}
        for name, row in self.members.items():
            self.budget_check()
            self.payloads[name] = member(path.parent, row)
        np = self.field.saved._kernel.np
        arrays = self.cp.arrays
        for name, value in (
                ("mesh", arrays["mesh"]),
                ("augmented_states", arrays["augmented"]),
                ("physical_states", arrays["physical"]),
                ("frozen_physical_rhs", arrays["physical_rhs"])):
            require(record_array_equal(np, value, self.members[name], self.payloads[name]),
                    "A complete current checkpoint array differs from the same captured call: "+name)
        require(record_array_equal(np, self.field.nodal[0],
                    self.members["physical_states"], self.payloads["physical_states"])
                and record_array_equal(np, self.field.nodal[1],
                    self.members["frozen_physical_rhs"], self.payloads["frozen_physical_rhs"]),
                "The current accurate Hermite has different original Y/DY words")
        self.nodes = int(scalar["node_count"])
        self.intervals = self.nodes-1
        self.dimension = int(scalar["augmented_size"])
        require(self.members["ppoly_coefficients"]["shape"]
                == [4, self.intervals, self.dimension]
                and len(self.payloads["ppoly_coefficients"])
                == 8*4*self.intervals*self.dimension,
                "Keep every literal original cubic coefficient")
        require(len(self.field.x) == self.nodes,
                "The current accurate field and captured solver have different whole meshes")
        self.binding = dict(schema=SCHEMA+"-binding", source=identity(__file__),
            capture=receipt, original_fullDN=copy.deepcopy(data["original_fullDN"]),
            actual_checkpoint=copy.deepcopy(self.cp.receipt),
            actual_current_driver=copy.deepcopy(self.cp.manifest["actual_driver_source"]),
            current_target_identity=copy.deepcopy(self.cp.target_identity),
            actual_coefficient_owner=self.coefficient_source,
            original_R553_helper=self.tube_source, original_R521_helper=self.majorant_source,
            actual_full_675_expression=self.field.expression_identity(),
            full_capture_array_identities=copy.deepcopy(self.members),
            field_modes=self.M, physical_size=self.n, augmented_size=self.dimension,
            angular_count=self.N,
            actual_complete_material_density_lower=str(self.rho_lower),
            physical_angle_target="diag(mu^2, A^2*rho(phi)^2), rho=actual Phi prime",
            source_capture_clock=copy.deepcopy(data["source_scope"]["actual_clock"]),
            current_budget_callback_supplied_by_actual_caller=True,
            raw_capture_owned_launcher_and_necessary_registration_not_implemented_here=True,
            operator_and_root_branch_or_FFT_rounding_equivalence_not_inferred=True)

    def cubic_coefficients(self, index):
        require(type(index) is int and 0 <= index < self.intervals,
                "Use an actual complete original solver interval")
        h = self.field.x[index+1]-self.field.x[index]
        raw = self.payloads["ppoly_coefficients"]
        rows = []
        for column in range(self.n):
            self.budget_check()
            local = tuple(exact_f64(raw_at(raw,
                ((3-power)*self.intervals+index)*self.dimension+column))
                for power in range(4))
            rows.append(tuple(local[power]*h**power for power in range(4)))
        return tuple(rows)

    def describe(self):
        return copy.deepcopy(self.binding)

    def cell(self, original_cell, actual_scalar_context):
        """Read complete actual polynomials on one original closed prefix cell.

        This method neither divides the original cell nor decides its metric
        retirement.  There is no global-complete flag: the unchanged caller
        must retain its entire original DFS/phase/frontier responsibilities.
        """
        self.budget_check()
        T = self.T
        record = dict(schema=SCHEMA+"-cell", original_cell=copy.deepcopy(original_cell),
            binding_identity=T.value_identity(self.binding),
            polynomial_comparison_available=False, geometric_gap_available=False,
            whole_pair_tube_available=False, error=None, unpaid=[],
            all_prefix_columns_required=True, original_metric_decision_changed=False,
            source_capture_does_not_certify_FFT_or_nonlinear_projection_error=True,
            original_solver_cubic_and_accurate_quintic_not_identified=True,
            no_solver_tolerance_to_metric_floor_claim=True)
        try:
            piece = self.field.pieces[original_cell["piece_index"]]
            require(piece["kind"] == "prefix", "This comparison pays prefix cells only")
            index = piece["prefix_span"]
            lo, hi = T.pair(original_cell["radial"])
            left, right = self.field.x[index], self.field.x[index+1]
            require(left <= lo <= hi <= right, "Use the whole original closed cell inside one actual span")
            h = right-left
            require(h > 0, "The actual full prefix span is empty")
            unit = ((lo-left)/h, (hi-left)/h)
            self.budget_check()
            quintic = tuple(tuple(T.exact(v) for v in row)
                            for row in self.field.prefix_coefficients(index))
            cubic = self.cubic_coefficients(index)
            require(len(quintic) == len(cubic) == self.n
                    and all(len(row) == 6 for row in quintic),
                    "Retain all actual powers and all physical rows")
            pair_boxes, delta0, delta1, delta2 = [], [], [], []
            canonical_rows, exact_gap_rows, second_gaps = [], [], []
            c_prime, c_second, q_prime, q_second = Q(0), Q(0), Q(0), Q(0)
            canonical_e0 = canonical_e1 = actual_correction_e0 = actual_correction_e1 = Q(0)
            literal_endpoint_value_gap = literal_endpoint_first_gap = Q(0)
            for column, (qrow, crow) in enumerate(zip(quintic, cubic)):
                self.budget_check()
                y0 = Q.from_float(float(self.field.nodal[0][index, column]))
                y1 = Q.from_float(float(self.field.nodal[0][index+1, column]))
                d0 = Q.from_float(float(self.field.nodal[1][index, column]))
                d1 = Q.from_float(float(self.field.nodal[1][index+1, column]))
                canonical_c = hermite_cubic((y0, d0), (y1, d1), h)
                canonical_rows.append(canonical_c)
                delta = difference(qrow, crow)
                exact_gap_rows.append(delta)
                qbox = T.polynomial_range(qrow, *unit)[0]
                cbox = T.polynomial_range(crow, *unit)[0]
                pair_boxes.append(hull(qbox, cbox))
                q1, c1 = T.derivative(qrow, h), T.derivative(crow, h)
                q2, c2 = T.derivative(q1, h), T.derivative(c1, h)
                dfirst = T.derivative(delta, h)
                dsecond = T.derivative(dfirst, h)
                delta0.append(T.absolute(T.polynomial_range(delta, *unit)[0]))
                delta1.append(T.absolute(T.polynomial_range(dfirst, *unit)[0]))
                delta2.append(T.absolute(T.polynomial_range(dsecond, *unit)[0]))
                c_prime = max(c_prime, T.absolute(T.polynomial_range(c1, *unit)[0]))
                c_second = max(c_second, T.absolute(T.polynomial_range(c2, *unit)[0]))
                q_prime = max(q_prime, T.absolute(T.polynomial_range(q1, *unit)[0]))
                q_second = max(q_second, T.absolute(T.polynomial_range(q2, *unit)[0]))
                star_gap = difference(qrow, canonical_c)
                actual_correction = difference(canonical_c, crow)
                canonical_e0 = max(canonical_e0,
                    T.absolute(T.polynomial_range(star_gap, *unit)[0]))
                canonical_e1 = max(canonical_e1,
                    T.absolute(T.polynomial_range(T.derivative(star_gap, h), *unit)[0]))
                actual_correction_e0 = max(actual_correction_e0,
                    T.absolute(T.polynomial_range(actual_correction, *unit)[0]))
                actual_correction_e1 = max(actual_correction_e1,
                    T.absolute(T.polynomial_range(T.derivative(actual_correction, h), *unit)[0]))
                dd0 = Q.from_float(float(self.field.nodal[2][index, column]))
                dd1 = Q.from_float(float(self.field.nodal[2][index+1, column]))
                second_gaps.append((dd0-endpoint(canonical_c, 2, h, False),
                                    dd1-endpoint(canonical_c, 2, h, True)))
                for at_right, y, d in ((False, y0, d0), (True, y1, d1)):
                    literal_endpoint_value_gap = max(literal_endpoint_value_gap,
                        abs(endpoint(crow, 0, h, at_right)-y))
                    literal_endpoint_first_gap = max(literal_endpoint_first_gap,
                        abs(endpoint(crow, 1, h, at_right)-d))
            maximum_second_gap = max(abs(x) for row in second_gaps for x in row)
            record["polynomial_comparison"] = dict(
                prefix_span=index, full_span=(left, right), radial=(lo, hi),
                normalized_closed_subinterval=unit,
                physical_size=self.n, field_modes=self.M,
                actual_cubic_power_identity=T.value_identity(cubic),
                actual_quintic_power_identity=T.value_identity(quintic),
                actual_difference_all_power_identity=T.value_identity(exact_gap_rows),
                canonical_same_Y_DY_cubic_identity=T.value_identity(canonical_rows),
                canonical_second_gap_identity=T.value_identity(second_gaps),
                complete_curve_segment_coefficient_box=tuple(pair_boxes),
                complete_per_column_E0_upper=tuple(delta0),
                complete_per_column_E1_upper=tuple(delta1),
                complete_per_column_E2_upper=tuple(delta2),
                E0_upper=max(delta0), E1_upper=max(delta1), E2_upper=max(delta2),
                original_literal_C_prime_upper=c_prime,
                original_literal_C_second_upper=c_second,
                accurate_Q_prime_upper=q_prime, accurate_Q_second_upper=q_second,
                Q_minus_Cstar_E0_upper=canonical_e0,
                Q_minus_Cstar_E1_upper=canonical_e1,
                Cstar_minus_actual_C_E0_upper=actual_correction_e0,
                Cstar_minus_actual_C_E1_upper=actual_correction_e1,
                canonical_full_span_simple_E0_upper=h*h*maximum_second_gap/20,
                canonical_full_span_simple_E1_upper=h*maximum_second_gap/2,
                literal_cubic_endpoint_value_gap_from_current_Y=literal_endpoint_value_gap,
                literal_cubic_endpoint_first_gap_from_current_DY=literal_endpoint_first_gap,
                exact_literal_PPoly_C1_join_not_assumed=True,
                canonical_Cstar_is_not_the_original_solver_PPoly=True,
                both_mean_columns_retained=True,
                all_curve_segment_points_in_recorded_box=True)
            record["polynomial_comparison_available"] = True
            require(isinstance(actual_scalar_context, dict)
                    and actual_scalar_context.get("schema") == T.SCHEMA+"-same-target-return",
                    "The same already evaluated accurate target context is absent")
            a = T.pair(actual_scalar_context["radius"])
            ap = T.pair(actual_scalar_context["accurate_arc_derivative"])
            g11 = T.pair(actual_scalar_context["numeric_s_radial_metric"])
            record["same_target"] = copy.deepcopy(actual_scalar_context)
            if a[0] <= 0 or g11[0] <= 0:
                record["unpaid"].append("same_target_A_or_mu_positive_lower_unpaid")
                return encode(record)
            mu = (self.api.sqrt_bounds(g11[0], self.sqrt_bits)[0],
                  self.api.sqrt_bounds(g11[1], self.sqrt_bits)[1])
            nu = T.mul(ap, mu)
            record["scalar_box"] = dict(A=a, mu=mu, nu=nu,
                nu_rule="accurate_arc_derivative_times_Ltrue_over_Lnumeric",
                same_accurate_C_family_and_original_numeric_s_chart=True)
            # These are complete physical-angle Fourier synthesis bounds.
            # Registration and either whole lower reflection are orthogonal.
            m = self.M
            radial_components = (
                sum(delta1[:m+1], Q(0)),
                sum(delta1[m+1:2*m+1], Q(0)),
                sum(delta1[2*m+1:], Q(0)))
            angular_components = [
                sum((2*j*delta0[j]+delta0[m+j] for j in range(1, m+1)), Q(0)),
                delta0[0]+sum((2*j*delta0[m+j]+delta0[j] for j in range(1, m+1)), Q(0)),
                sum((2*j*delta0[2*m+1+j] for j in range(1, m+1)), Q(0))]
            radial_square = sum((v*v for v in radial_components), Q(0))
            angular_square = sum((v*v for v in angular_components), Q(0))
            angular_metric_lower = a[0]*self.rho_lower
            delta_square = radial_square/(mu[0]*mu[0])+angular_square/(angular_metric_lower*angular_metric_lower)
            delta_upper = self.api.sqrt_bounds(delta_square, self.sqrt_bits)[1]
            record["geometric_derivative_gap"] = dict(
                full_physical_angle_circle=True,
                same_common_SE2_and_material_pullback_required=True,
                both_reflections_preserve_this_bound=True,
                radial_component_upper=radial_components,
                angular_component_upper=tuple(angular_components),
                radial_norm_square_upper=radial_square,
                angular_norm_square_upper=angular_square,
                relative_derivative_Frobenius_square_upper=delta_square,
                relative_derivative_operator_upper=delta_upper,
                exact_target_mu_lower=mu[0], exact_target_A_lower=a[0],
                actual_complete_Phi_prime_lower=self.rho_lower,
                exact_target_A_times_Phi_prime_lower=angular_metric_lower,
                physical_angle_target="diag(mu^2, A^2*rho(phi)^2)",
                normalized_q_two_pi_derivative_and_metric_factors_cancel=True,
                does_not_require_Frenet_P_positive=True,
                original_cubic_metric_error_still_needed_for_metric_transfer=True,
                caps_tail_collar_cut_patch_not_certified_by_this_prefix_record=True)
            record["geometric_gap_available"] = True
            self.budget_check()
            angular = T.complete_angular_box(self.Active, tuple(pair_boxes),
                original_cell["angular"], self.M, self.budget_check)
            q = T.norm_squared(angular["d"])
            w = T.norm_squared(T.cross(angular["d"], angular["e"]))
            p = T.sub(T.mul(T.mul(T.square(a), T.square(mu)), w),
                      T.mul(T.square(nu), T.mul(T.square(q), q)))
            record["whole_pair_joint_box"] = dict(
                angular_box=angular, d_squared=q, W=w, P=p,
                entire_closed_cell_both_curves_and_all_affine_combinations=True,
                actual_angular_subcell=copy.deepcopy(original_cell["angular"]),
                full_angular_circle_positivity_not_inferred_from_this_one_cell=True,
                an_old_quintic_only_P_lower_was_not_reused=True)
            if p[0] <= 0:
                record["unpaid"].append("whole_actual_cubic_quintic_segment_P_positive_unpaid")
                return encode(record)
            self.api.validate_modes(self.M, self.N)
            synthesis = self.api.fourier_synthesis_majorants(
                tuple(T.absolute(v) for v in pair_boxes), self.M, self.N, self.sqrt_bits)
            domain = dict(A_lower=a[0], A_upper=a[1], mu_lower=mu[0],
                mu_upper=mu[1], nu_abs_upper=T.absolute(nu), P_lower=p[0], W_lower=w[0])
            self.budget_check()
            majorants = self.api.finite_rhs_majorants(domain, synthesis, self.sqrt_bits)
            record["actual_R521_whole_pair_majorants"] = majorants
            record["whole_pair_tube_available"] = True
            record["fixed_reference_branch_scope"] = dict(
                either_fixed_sigma_supported_by_same_unsigned_majorants=True,
                original_worker_root_or_branch_not_inferred_from_a_source_label=True,
                exact_reference_DFT_not_actual_FFT_formation=True,
                finite_projection_defect_PiNV_minus_V_still_unpaid=True,
                majorants_are_local_angular_ingredients_not_a_complete_DFT_bound=True,
                all_original_angular_cells_and_complete_N_sample_cover_still_required=True,
                no_arbitrary_formation_or_scalar_gap_zero_filled=True,
                original_cubic_eta_C_not_supplied_by_this_library=True)
            return encode(record)
        except ORDINARY_ERRORS as error:
            record["error"] = dict(type=type(error).__name__, message=str(error),
                                  traceback=traceback.format_exc())
            record["unpaid"].append("actual_same_call_polynomial_comparison_or_target_tube_unpaid")
            return encode(record)


def bind_loaded_cubic_quintic(current, *, capture_result, capture_sha256,
                             angular_count, sqrt_bits, budget_check):
    """Bind only the already loaded current field and actual same-call capsule.

    A missing/unavailable capsule is a diagnostic-unpaid reason for a future
    caller, never a reason to alter the original BVP or metric decisions.
    """
    return BoundCubicQuintic(current, capture_result=capture_result,
        capture_sha256=capture_sha256, angular_count=angular_count,
        sqrt_bits=sqrt_bits, budget_check=budget_check)


def conditional_metric_transfer(cubic_error_upper, relative_derivative_gap_upper,
                                sqrt_bits):
    """Elementary conditional Gram transport, never inference from RMS.

    Both arguments must already be actual rigorous upper bounds on the same
    closed cell with the same accurate target and common parameterization.
    This pure bound does not manufacture their provenance.
    """
    actions()
    T, _ = load_tube()
    api, _ = T.load_majorants()
    epsilon, delta = T.exact(cubic_error_upper), T.exact(relative_derivative_gap_upper)
    require(epsilon >= 0 and delta >= 0, "Require actual nonnegative rigorous input bounds")
    scale = api.sqrt_bounds(1+epsilon, sqrt_bits)[1]
    return dict(schema=SCHEMA+"-conditional-metric-transfer",
        original_cubic_relative_metric_upper=str(epsilon),
        same_cell_relative_derivative_gap_upper=str(delta),
        accurate_quintic_relative_metric_upper=str(epsilon+2*scale*delta+delta*delta),
        input_bounds_and_same_target_provenance_remain_caller_responsibility=True,
        original_solver_RMS_is_not_a_substitute_for_cubic_error=True,
        no_complete_closed_cover_or_acceptance_inferred=True)
