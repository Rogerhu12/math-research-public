#!/usr/bin/env python3
"""Request151: complete public-u enclosures of the actual R300/v3 nine target.

The accurate target is rebuilt from this job's actual core, recipe and C/cut.
The comparison function is the exact-real, piecewise interpretation of the
actual numeric compilation's finite words, not the rounded IEEE evaluator.
All new arithmetic is restricted to this public repository's Actions.  No
field, native solver, tail J, nonlinear residual or acceptance is fabricated.
"""
from __future__ import annotations
import argparse
from collections import deque
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import struct
import sys
import time
import traceback

REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "request151-common-u-complete-nine-target-enclosures-v1"
REQUEST_SCHEMA = "public-continuous-nine-target-enclosures-request-v1"
ORIGINAL_REQUEST_NAME = "public-continuous-nine-v3-construction-request.json"
ORIGINAL_REQUEST_BYTES = 17398
ORIGINAL_REQUEST_SHA = "4b6f78bb25e0d87354e2ad786637fc9e4db5c7c34774d3cad4716638552ba707"
FACTORY_NAME = "geometry_20261115_continuous_nine_scalar_factory_v3.py"
FACTORY_SHA = "0d89370df95c6063cb336182d87137705d5e4ddb87625a3fb1b58b35695a621e"
CONSTRUCTION_NAME = "geometry_20261115_continuous_nine_v3_actual_construction.py"
CONSTRUCTION_SHA = "738dd352cf62fbd47eb80e867ac441b7d0c179074cbee93fb8dd6528ba0d4cb0"
NUMERIC_NAME = "geometry_20261115_continuous_nine_scalar_numeric_v3.py"
NUMERIC_SHA = "7cfab12ebb8bf4a948336e7c605ea096a9597be43a4582f166f9067850ea4b60"
NUMERIC_SCHEMA = "R300-numerical-nine-profile-with-v3-cut-and-accurate-public-u-target-v1"
PARAMETERS = ["p1", "p2", "p3", "theta1", "theta2", "theta3", "eta1", "eta2", "eta3"]
ADDITION_ORDER = [0, 1, 2, 4, 3, 5, 6, 7, 8]
BITS = 320
SCALE = 1 << BITS
ACTUAL_E_BUDGET_SECONDS = 3600
POLICY = dict(grid_bits=320, original_tree_sqrt_bits=256, budget_seconds=900,
              maximum_evaluated_nodes=65536, maximum_depth=32,
              comparison_work_goal="1/10000000", expected_numeric_piece_count=419)


def actions_only():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("New interval arithmetic is public-repository Actions only")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=True, allow_nan=False) + "\n").encode("ascii")


def receipt(path):
    path = Path(path)
    h = hashlib.sha256()
    count = 0
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1048576), b""):
            h.update(block)
            count += len(block)
    return dict(file=path.name, bytes=count, sha256=h.hexdigest())


def read(path, expected=None):
    path = Path(path)
    raw = path.read_bytes()
    actual = dict(file=path.name, bytes=len(raw), sha256=sha(raw))
    if expected is not None:
        for key in ("bytes", "sha256"):
            if actual[key] != expected[key]:
                raise ValueError("Actual original input differs: " + str(path) + ":" + key)
    decoded = gzip.decompress(raw) if raw.startswith(b"\x1f\x8b") else raw
    return json.loads(decoded), dict(actual, decoded_bytes=len(decoded), decoded_sha256=sha(decoded))


def member_path(root, desc):
    name = PurePosixPath(desc["file"])
    if name.is_absolute() or ".." in name.parts or "\\" in desc["file"]:
        raise ValueError("An original descriptor escapes its actual output directory")
    path = Path(root) / str(name)
    if not path.resolve().is_relative_to(Path(root).resolve()):
        raise ValueError("An original descriptor resolves outside its owner")
    return path


def member(root, desc):
    path = member_path(root, desc)
    value, identity = read(path, desc)
    return value, identity, path


def checked_large_member(root, desc):
    # The old nine-domain ledger can be hundreds of MB.  Its identity is
    # streamed, without parsing/repeating its Q arithmetic or loading its tree.
    path = member_path(root, desc)
    identity = receipt(path)
    for key in ("bytes", "sha256"):
        if identity[key] != desc[key]:
            raise ValueError("Complete original large evidence bytes differ: " + str(path))
    return identity


def write(path, value):
    raw = canonical(value)
    Path(path).write_bytes(raw)
    return dict(file=Path(path).name, bytes=len(raw), sha256=sha(raw))


def emit(value):
    raw = canonical(value)
    if len(raw) > 89000:
        return emit_segments(value.get("event", "complete-event"), value)
    print(raw.decode("ascii"), end="", flush=True)
    return dict(bytes=len(raw), sha256=sha(raw), segments=1)


def emit_segments(label, value):
    raw = canonical(value)
    text = raw.decode("ascii")
    width = 12000
    count = (len(text) + width - 1) // width
    identity = dict(label=label, bytes=len(raw), sha256=sha(raw), segments=count,
                    reconstruction="concatenate decoded data strings by index; ASCII bytes include final LF")
    print(canonical(dict(event="request151_complete_metadata_begin", **identity)).decode(), end="", flush=True)
    for index, start in enumerate(range(0, len(text), width)):
        event = dict(event="request151_complete_metadata_segment", label=label,
                     index=index, segments=count, data=text[start:start + width])
        encoded = canonical(event)
        if len(encoded) > 89000:
            raise RuntimeError("A complete metadata segment exceeds its transport bound")
        print(encoded.decode(), end="", flush=True)
    return identity


def import_source(directory, name, digest, label):
    path = Path(directory) / name
    if sha(path.read_bytes()) != digest:
        raise ValueError("Pinned scientific source differs: " + name)
    specification = importlib.util.spec_from_file_location(label, path)
    module = importlib.util.module_from_spec(specification)
    sys.modules[label] = module
    specification.loader.exec_module(module)
    return module


def same(a, b, label):
    # Canonical JSON also distinguishes bool/int and preserves literal floats.
    if canonical(a) != canonical(b):
        raise ValueError("Complete original field differs: " + label)


def same_run(value, label):
    if (str(value.get("run_id")) != os.environ["GITHUB_RUN_ID"]
            or value.get("source_commit") != os.environ["GITHUB_SHA"]):
        raise ValueError("Use this same job's actual output: " + label)


def rational_word(word):
    if not isinstance(word, str) or re.fullmatch(r"[0-9a-f]{16}", word) is None:
        raise ValueError("A finite little-endian binary64 word is required")
    value = struct.unpack("<d", bytes.fromhex(word))[0]
    if not math.isfinite(value):
        raise ValueError("A literal numeric reference word is nonfinite")
    return Q.from_float(value)


class Interval:
    """Closed [lo,hi]/2**320; every nonexact operation rounds outwards."""
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        self.lo = int(lo)
        self.hi = self.lo if hi is None else int(hi)
        if self.lo > self.hi:
            raise ValueError("Reversed fixed-grid interval")

    @staticmethod
    def q(lo, hi=None):
        lo = Q(lo)
        hi = lo if hi is None else Q(hi)
        if lo > hi:
            raise ValueError("Reversed exact rational input enclosure")
        lower = lo.numerator * SCALE // lo.denominator
        upper = -((-hi.numerator * SCALE) // hi.denominator)
        return Interval(lower, upper)

    @staticmethod
    def integer(value):
        return Interval(int(value) * SCALE)

    def __add__(self, other):
        if isinstance(other, int):
            other = Interval.integer(other)
        return Interval(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-other if isinstance(other, Interval) else -int(other))

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        if isinstance(other, int):
            products = (self.lo * other, self.hi * other)
            return Interval(min(products), max(products))
        products = (self.lo * other.lo, self.lo * other.hi,
                    self.hi * other.lo, self.hi * other.hi)
        return Interval(min(products) // SCALE, -((-max(products)) // SCALE))

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Interval.integer(other)
        if other.lo <= 0 <= other.hi:
            raise ArithmeticError("An interval denominator contains zero")
        if other.hi < 0:
            return (-self) / (-other)
        lower = min((x * SCALE) // y for x in (self.lo, self.hi) for y in (other.lo, other.hi))
        upper = max(-((-x * SCALE) // y) for x in (self.lo, self.hi) for y in (other.lo, other.hi))
        return Interval(lower, upper)

    def square(self):
        lower = 0 if self.lo <= 0 <= self.hi else min(self.lo * self.lo, self.hi * self.hi)
        upper = max(self.lo * self.lo, self.hi * self.hi)
        return Interval(lower // SCALE, -((-upper) // SCALE))

    def hull(self, other):
        return Interval(min(self.lo, other.lo), max(self.hi, other.hi))

    def intersection(self, other):
        lo, hi = max(self.lo, other.lo), min(self.hi, other.hi)
        return None if lo > hi else Interval(lo, hi)

    def abs_upper(self):
        return max(abs(self.lo), abs(self.hi))

    def record(self):
        return dict(lower_integer=str(self.lo), upper_integer=str(self.hi), binary_exponent=-BITS)


def poly(coefficients, x):
    result = Interval.integer(0)
    for coefficient in reversed(coefficients):
        result = result * x + coefficient
    return result


def derivative(coefficients):
    return [coefficient * index for index, coefficient in enumerate(coefficients) if index] or [Interval.integer(0)]


def prepared_polynomial(coefficients):
    first = derivative(coefficients)
    return coefficients, first, derivative(first)


def hull_jets(jets):
    if not jets:
        raise ArithmeticError("No possible accurate piece covers this nonempty public interval")
    result = list(jets[0])
    for jet in jets[1:]:
        result = [a.hull(b) for a, b in zip(result, jet)]
    return result


def rebuild_actual(args, request, original):
    """Bind actual 147 outputs and recompute every mathematical definition field."""
    directory = args.construction_directory
    construction, construction_receipt = read(directory / "construction-result.json")
    same_run(construction, "147 construction")
    if (construction.get("schema") != "request147-actual-v3-continuous-nine-construction-v1"
            or construction.get("source", {}).get("sha256") != CONSTRUCTION_SHA
            or construction.get("source", {}).get("bytes") != 20377):
        raise ValueError("Keep the original actual147 subprogram schema and producer")
    same(construction["request"], receipt(args.original_request), "original147 request receipt")
    if not construction.get("exact_model_definition_created") or not construction.get("numerical_profile_compiled"):
        raise ArithmeticError("The current actual147 target definition or numeric reference is unavailable")
    factory = import_source(args.code_directory, FACTORY_NAME, FACTORY_SHA, "_r151_actual_factory")
    builder = import_source(args.code_directory, CONSTRUCTION_NAME, CONSTRUCTION_SHA, "_r151_original_builder")
    kernel, core_source = factory.load_core_kernel(args.code_directory)
    policy = original["construction"]
    accepted_item = original["construction_inputs"]["accepted"]
    accepted_path = args.inputs_directory / accepted_item["runtime_basename"]
    accepted, _ = read(accepted_path, accepted_item)
    config_item = original["inputs"]["config"]
    config_path = args.inputs_directory / config_item["runtime_basename"]
    config, config_receipt = read(config_path, config_item)
    if (accepted.get("success") is not True or accepted.get("M") != 96
            or config["modes"] != 112 or config["quadrature"] != 2048):
        raise ValueError("The original complete accepted core/config identities differ")
    geometry = factory.pointer(accepted, policy["core_geometry_pointer"])
    core_end = Q.from_float(float(accepted["mesh"][-1]))
    cut = Q.from_float(float(config["rCut"]))
    _, core_identity = factory.read_json(accepted_path, accepted_item["sha256"])
    core_identity.update(geometry_pointer=policy["core_geometry_pointer"],
                         selected_geometry_canonical_sha256=factory.sha(factory.canonical(geometry)),
                         original_exact_shared_jet_source=core_source)
    tail_result, tail_receipt = read(args.tail_cover_directory / "result.json")
    same_run(tail_result, "actual continuous C cover")
    cut_readout, cut_receipt = read(args.cut_twojet_readout)
    same_run(cut_readout, "actual complete cut two-jet")
    leaves, tail_identity = factory.cut_jet_from_actual_cover(args.tail_cover_directory,
        tail_receipt["sha256"], args.code_directory, cut, args.cut_twojet_readout, cut_receipt["sha256"])
    if tail_identity["actual_input_binding"]["config"]["sha256"] != config_item["sha256"]:
        raise ValueError("The accurate prefix and continuous tail use different original config")
    actual_E_work = dict(request["actual_continuous_E_reconstruction"]["scientific_parameters"])
    actual_E_work["budget_seconds"] = float(ACTUAL_E_BUDGET_SECONDS)
    same(tail_identity["actual_input_binding"]["work_parameters"], actual_E_work,
         "actual same-job C work parameters, including explicit3600s instead of prior1471800s")
    recipe, recipe_receipt, recipe_path = member(directory, construction["actual_recipe_file"])
    _, recipe_identity = factory.read_json(recipe_path, recipe_receipt["sha256"])
    same(construction["actual_recipe"], recipe, "construction's complete original recipe")
    expected_recipe, expected_calibration = builder.select_recipe(factory, kernel, geometry,
        core_end, cut, leaves, policy["initial_nine_parameters"])
    expected_recipe["parameter_origin"] = policy["parameter_origin"]
    same(expected_recipe, recipe, "R323 recipe rebuilt from actual core and actual complete cut")
    calibration, calibration_receipt, _ = member(directory, construction["actual_width_selection_file"])
    same(expected_calibration, calibration, "all original R323 width-selection fields")
    same(recipe["nine_parameters"], policy["initial_nine_parameters"], "all nine actual R320 parameters")
    same(recipe["parameter_order"], PARAMETERS, "declared nine-parameter order")
    original_result, factory_receipt, _ = member(directory / "factory", construction["original_factory_result_file"])
    same_run(original_result, "actual exact factory")
    same(original_result, construction["original_factory_result"], "whole original factory result")
    if original_result.get("source_sha256") != FACTORY_SHA:
        raise ValueError("The actual factory source differs")
    definition, definition_receipt, definition_path = member(directory / "factory", original_result["model_definition"])
    model = factory.build_expression(kernel, geometry, recipe, leaves, cut)
    values = model["tree"].evaluate(leaves, POLICY["original_tree_sqrt_bits"])
    conditions = factory.construction_conditions(model, values)
    same(conditions, original_result["construction_conditions"], "actual original construction conditions")
    if not conditions["all_strict_conditions_proved"]:
        raise ArithmeticError("The accurate original target construction premises are unpaid")
    # Existing domain ledgers are source-bound evidence fields, not assumed new
    # certificates.  Their entire bytes are checked; their math is not repeated.
    domain_receipts = {}
    for role in ("base_domain", "requested_parameter_domain"):
        record = original_result[role]
        if record is not None:
            domain_receipts[role] = checked_large_member(directory / "factory", record["ledger"])
    proof = original["construction"]["R300_proof"]
    proof_path = args.repository_directory / proof["file"]
    actual_proof = receipt(proof_path)
    same({k: actual_proof[k] for k in ("bytes", "sha256")},
         {k: proof[k] for k in ("bytes", "sha256")}, "actual published R300 proof")
    rebuilt = factory.definition(model, tail_identity, core_identity, recipe_identity)
    rebuilt.update(construction_conditions=conditions,
        published_structural_and_effective_scope_proof=actual_proof,
        given_finite_enclosure_is_not_an_effective_real_name=True,
        automatic_width_search_performed=False,
        actual_enclosure_leaves={key: value.record() for key, value in leaves.items()},
        base_complete_domain=original_result["base_domain"])
    if set(rebuilt) != set(definition):
        raise ValueError("The complete accurate definition has missing or extra fields")
    comparison = []
    for key in sorted(rebuilt):
        same(rebuilt[key], definition[key], "rebuilt definition." + key)
        comparison.append(dict(field=key, exactly_equal=True,
                               canonical_sha256=sha(canonical(definition[key]))))
    if factory.canonical(rebuilt) != definition_path.read_bytes():
        raise ValueError("The complete original factory serialization differs, including its final LF")
    spec, spec_receipt, _ = member(directory, construction["numerical_compilation"]["complete_numeric_specification"])
    if (spec.get("schema") != NUMERIC_SCHEMA or spec.get("source_sha256") != NUMERIC_SHA
            or spec.get("parameter_order") != PARAMETERS
            or spec.get("field_modes") != 112 or spec.get("tail_modes") != 112
            or spec.get("public_material_interval") != ["0", "1"]):
        raise ValueError("Bind the actual full numeric compilation, not another scalar model")
    expected_definition_receipt = dict(file=definition_path.name,
        bytes=definition_receipt["bytes"], sha256=definition_receipt["sha256"])
    same(spec["accurate_definition"], expected_definition_receipt, "numeric reference's accurate definition")
    same(spec["nine_parameters"], policy["initial_nine_parameters"], "numeric actual nine parameters")
    literal_parameters = [Q.from_float(float(x)) for x in policy["initial_nine_parameters"]]
    same(spec["nine_parameter_float64le"], [struct.pack("<d", float(x)).hex()
        for x in policy["initial_nine_parameters"]], "all original parameter words")
    same(spec["nine_parameters_as_exact_dyadics"], [str(x) for x in literal_parameters], "literal parameter dyadics")
    base_keys = ("expression_nodes", "pieces", "three_true_supports", "derived_expression_roots",
                 "continuous_tail", "core_input", "core_end", "cut_radius", "chosen_root_scope")
    expected_base_sha = factory.sha(factory.canonical({key: definition[key] for key in base_keys}))
    if spec["accurate_family_base_identity_sha256"] != expected_base_sha:
        raise ValueError("Numeric reference does not bind the rebuilt complete accurate family")
    compilation = spec["complete_numeric_compilation"]
    if (compilation["schema"] != NUMERIC_SCHEMA + "-finite-compilation"
            or compilation["source_sha256"] != NUMERIC_SHA
            or compilation["factory_sha256"] != FACTORY_SHA
            or spec["numeric_compilation_sha256"] != factory.sha(factory.canonical(compilation))):
        raise ValueError("The complete original numerical compilation identity differs")
    same(compilation["accurate_definition"], expected_definition_receipt, "complete numeric table definition")
    same(compilation["nine_addition_order"], ADDITION_ORDER, "original nine-control addition order")
    word_values = compilation["expression_values_float64le"]
    if len(word_values) != len(model["tree"].nodes):
        raise ValueError("All original DAG literal values are required")
    literal_values = [rational_word(word) for word in word_values]
    if len(compilation["piece_coefficient_float64le"]) != len(model["pieces"]):
        raise ValueError("All original numeric base pieces are required")
    for index, piece in enumerate(model["pieces"]):
        same(compilation["piece_coefficient_float64le"][index],
             [word_values[i] for i in piece["coefficients"]], "complete numeric coefficients " + str(index))
    if len(compilation["supports_float64le"]) != 3:
        raise ValueError("All three actual support tables are required")
    support_table = []
    for index, support in enumerate(model["supports"]):
        row = compilation["supports_float64le"][index]
        if len(row) != 3:
            raise ValueError("Preserve actual left, stored width and rounded-right metadata")
        same(row[:2], [word_values[support["left"]], word_values[support["width"]]],
             "numeric support source words " + str(index))
        left, width, rounded_right = [rational_word(word) for word in row]
        if width <= 0:
            raise ValueError("A literal numeric support has nonpositive width")
        support_table.append(dict(index=index, left_exact=str(left), stored_width_exact=str(width),
            reference_support_right_exact=str(left + width), rounded_right_word=row[2],
            rounded_right_as_exact_dyadic=str(rounded_right),
            rounded_right_not_substituted_for_exact_left_plus_width=True))
    root_index = model["roots"]["total_length"]
    same(compilation["numerical_length_float64le"], word_values[root_index], "literal complete length word")
    if compilation["true_length_expression_root"] != root_index or spec["accurate_length_expression_root"] != root_index:
        raise ValueError("The true and numeric lengths lost their explicitly separate identities")
    ell = rational_word(compilation["numerical_length_float64le"])
    if ell <= 0 or Q.from_float(float(spec["numeric_physical_length"])) != ell:
        raise ValueError("The actual literal numeric length is not positive and consistently recorded")
    partition_words = compilation["common_lookup_partition_float64le"]
    partition = [rational_word(word) for word in partition_words]
    count = len(model["pieces"])
    if (count != POLICY["expected_numeric_piece_count"] or len(partition) != count + 1
            or partition[0] != 0 or partition[-1] != ell
            or any(a >= b for a, b in zip(partition[:-1], partition[1:]))):
        raise ValueError("Retain this actual full 419-piece increasing common lookup partition")
    # The recorded lookup words, not an independently recomputed anchor+width,
    # define each reference piece's complete closed public-u interval.
    grid_rows = []
    grid_values = []
    for index, box in enumerate(values):
        grid = Interval.q(box.lo, box.hi)
        if Q(grid.lo, SCALE) > box.lo or Q(grid.hi, SCALE) < box.hi:
            raise AssertionError("Outward fixed-grid conversion lost an original exact-Q node")
        grid_values.append(grid)
        grid_rows.append(dict(index=index, original_exact_Q_lower=str(box.lo),
            original_exact_Q_upper=str(box.hi), outward_grid=grid.record(), original_Q_contained=True))
    binding = dict(schema=SCHEMA + "-input-binding", run_id=os.environ["GITHUB_RUN_ID"],
        source_commit=os.environ["GITHUB_SHA"], original_subprogram_request=receipt(args.original_request),
        actual_construction_result=construction_receipt, original_factory_result=factory_receipt,
        actual_core_input=core_identity, actual_config=config_receipt,
        actual_recipe=recipe_identity, original_R323_calibration=calibration_receipt,
        actual_tail_result=tail_receipt, actual_cut_twojet=cut_receipt,
        original_tail_binding=tail_identity, actual_definition=definition_receipt,
        all_definition_fields_rebuilt_and_exactly_compared=comparison,
        actual_numeric_specification=spec_receipt,
        actual_numeric_compilation_sha256=spec["numeric_compilation_sha256"],
        original_domain_evidence_files=domain_receipts,
        original_factory_base_domain=original_result["base_domain"],
        original_factory_nine_parameter_domain=original_result["requested_parameter_domain"],
        original_nine_domain_completion_not_required_for_new_enclosures=True,
        original_R320_parameter_origin=policy["parameter_origin"],
        actual_continuous_E_reconstruction=request["actual_continuous_E_reconstruction"],
        complete_nine_parameters_as_exact_dyadics=[str(x) for x in literal_parameters],
        complete_nine_parameter_words=spec["nine_parameter_float64le"],
        actual_lookup_partition_words=partition_words, literal_support_interpretation=support_table,
        reference_is_exact_real_literal_word_expression_not_IEEE_program=True,
        numeric_float_DAG_or_original_BVP_evaluator_not_reexecuted=True,
        grid_precision_bits=BITS, original_tree_sqrt_bits=256,
        fixed_grid_replaces_arithmetic_representation_not_semantic_target=True,
        factory_Q_node_enclosures_all_retained_in_grid=True,
        current_C_tail_J_or_nonzero_field_not_supplied=True)
    return factory, model, grid_values, literal_values, compilation, partition, ell, binding, grid_rows


class CompleteTarget:
    def __init__(self, factory, model, values, literal_values, compilation, partition, ell):
        self.model, self.values = model, values
        self.ell_q = ell
        self.ell = Interval.q(ell)
        self.length = values[model["roots"]["total_length"]]
        if self.length.lo <= 0:
            raise ArithmeticError("The complete accurate length enclosure is not strictly positive")
        self.radial_relative = self.ell.square() / self.length.square() - 1
        self.partition = [x / ell for x in partition]
        self.parameters = [Interval.q(p) for p in model["parameters"]]
        self.true_supports = [(values[s["left"]], values[s["width"]]) for s in model["supports"]]
        self.literal_supports = [(Interval.q(rational_word(row[0])), Interval.q(rational_word(row[1])))
                                 for row in compilation["supports_float64le"]]
        self.bumps = [prepared_polynomial([Interval.q(c) for c in factory.bump_polynomial(k)]) for k in range(3)]
        self.true_pieces, self.numeric_pieces = [], []
        for index, piece in enumerate(model["pieces"]):
            anchor, width = values[piece["anchor"]], values[piece["width"]]
            if width.lo <= 0:
                raise ArithmeticError("A complete accurate piece width is not strictly positive")
            local = Interval.q(Q(piece["local_interval"][0]), Q(piece["local_interval"][1]))
            self.true_pieces.append(dict(index=index, name=piece["name"], anchor=anchor,
                width=width, local=local, physical=anchor + width * local,
                polynomials=prepared_polynomial([values[i] for i in piece["coefficients"]])))
            numeric_width = literal_values[piece["width"]]
            if numeric_width <= 0:
                raise ArithmeticError("A literal numeric piece width is not positive")
            self.numeric_pieces.append(dict(index=index, name=piece["name"],
                anchor=Interval.q(literal_values[piece["anchor"]]), width=Interval.q(numeric_width),
                polynomials=prepared_polynomial([Interval.q(literal_values[i]) for i in piece["coefficients"]])))
        if any(width.lo <= 0 for _, width in self.true_supports + self.literal_supports):
            raise ArithmeticError("Every complete true and literal support must have positive width")

    def controls(self, position, supports):
        result = [Interval.integer(0) for _ in range(3)]
        full_support = Interval.integer(0).hull(Interval.integer(1))
        hit = []
        support_terms = {}
        for support_index, (left, width) in enumerate(supports):
            coordinate = (position - left) / width
            inside = coordinate.intersection(full_support)
            if inside is None:
                continue
            hit.append(support_index)
            outside_possible = coordinate.lo < 0 or coordinate.hi > SCALE
            for order, jets in enumerate(self.bumps):
                index = 3 * order + support_index
                p = self.parameters[index]
                # Original shape amplitude is w**2; its s derivatives have
                # the exact respective factors w and 1.  No support is dropped.
                factors = (width.square(), width, Interval.integer(1))
                terms = [p * factors[j] * poly(jets[j], inside) for j in range(3)]
                if outside_possible:
                    terms = [term.hull(Interval.integer(0)) for term in terms]
                support_terms[index] = terms
        for index in ADDITION_ORDER:
            if index in support_terms:
                result = [a + b for a, b in zip(result, support_terms[index])]
        return result, hit

    def accurate(self, u):
        position = self.length * u
        jets, hits, support_hits = [], [], set()
        for piece in self.true_pieces:
            if position.intersection(piece["physical"]) is None:
                continue
            local = ((position - piece["anchor"]) / piece["width"]).intersection(piece["local"])
            if local is None:
                continue
            current_position = (piece["anchor"] + piece["width"] * local).intersection(position)
            if current_position is None:
                raise ArithmeticError("A possible accurate piece lost its current position enclosure")
            width = piece["width"]
            base = [poly(piece["polynomials"][0], local),
                    poly(piece["polynomials"][1], local) / width,
                    poly(piece["polynomials"][2], local) / width.square()]
            control, support = self.controls(current_position, self.true_supports)
            jets.append([a + b for a, b in zip(base, control)])
            hits.append(piece["index"])
            support_hits.update(support)
        return hull_jets(jets), hits, sorted(support_hits)

    def literal(self, index, u):
        piece = self.numeric_pieces[index]
        position = self.ell * u
        # Deliberately no clipping to the accurate local interval or [0,1].
        # The actual common lookup partition owns this closed formula extension.
        local = (position - piece["anchor"]) / piece["width"]
        width = piece["width"]
        base = [poly(piece["polynomials"][0], local),
                poly(piece["polynomials"][1], local) / width,
                poly(piece["polynomials"][2], local) / width.square()]
        control, supports = self.controls(position, self.literal_supports)
        return [a + b for a, b in zip(base, control)], local, supports

    def evaluate(self, node, deadline):
        index, lo, hi, depth = node
        if time.monotonic() >= deadline:
            raise ResourceStop("wall-clock-before-query")
        u = Interval.q(lo, hi)
        middle = (lo + hi) / 2
        true, pieces, true_supports = self.accurate(u)
        numeric, numeric_local, numeric_supports = self.literal(index, u)
        if time.monotonic() >= deadline:
            raise ResourceStop("wall-clock-before-centred-difference")
        true_mid, mid_pieces, _ = self.accurate(Interval.q(middle))
        numeric_mid, _, _ = self.literal(index, Interval.q(middle))
        d0 = numeric_mid[0] - true_mid[0]
        d1 = self.ell * numeric[1] - self.length * true[1]
        centred = d0 + Interval.q(lo - middle, hi - middle) * d1
        direct = numeric[0] - true[0]
        difference = centred.intersection(direct)
        if difference is None:
            raise ArithmeticError("R330 centred and direct valid enclosures have empty intersection")
        positive = true[0].lo > 0
        subunit = true[1].lo > -SCALE and true[1].hi < SCALE
        radius_refuted = true[0].hi <= 0
        speed_refuted = true[1].lo >= SCALE or true[1].hi <= -SCALE
        rho = angular = None
        radial_upper = self.radial_relative.abs_upper()
        if positive:
            rho = Interval(difference.abs_upper()) / Interval(true[0].lo)
            angular = rho * 2 + rho.square()
        delta = None if angular is None else max(radial_upper, angular.hi)
        goal = Q(POLICY["comparison_work_goal"])
        target_met = delta is not None and delta * goal.denominator <= goal.numerator * SCALE
        reasons = []
        if radius_refuted:
            reasons.append("accurate-radius-upper-nonpositive-rigorous-refutation")
        elif not positive:
            reasons.append("accurate-radius-positivity-unresolved")
        if speed_refuted:
            reasons.append("accurate-speed-entire-enclosure-outside-open-unit-domain-rigorous-refutation")
        elif not subunit:
            reasons.append("accurate-open-unit-speed-domain-unresolved")
        if not target_met:
            reasons.append("relative-target-work-width-unresolved")
        record = dict(numeric_piece=index, numeric_piece_name=self.numeric_pieces[index]["name"],
            closed_public_u=[str(lo), str(hi)], depth=depth, midpoint_exact=str(middle),
            both_closed_formula_endpoints_retained=True,
            accurate_possible_piece_indices=pieces, accurate_midpoint_possible_piece_indices=mid_pieces,
            accurate_possible_control_support_indices=true_supports,
            literal_possible_control_support_indices=numeric_supports,
            literal_unclipped_local_interval=numeric_local.record(),
            accurate_a_as_ass=[x.record() for x in true],
            accurate_a_u_a_uu=[true[0].record(), (self.length * true[1]).record(),
                              (self.length.square() * true[2]).record()],
            literal_a_as_ass=[x.record() for x in numeric],
            literal_a_u_a_uu=[numeric[0].record(), (self.ell * numeric[1]).record(),
                             (self.ell.square() * numeric[2]).record()],
            accurate_radial_target_L_squared=self.length.square().record(),
            accurate_angular_target_a_squared=true[0].square().record(),
            literal_radial_target_ell_squared=self.ell.square().record(),
            literal_angular_target_a_squared=numeric[0].square().record(),
            centred_midpoint_difference=d0.record(), whole_derivative_difference=d1.record(),
            centred_difference=centred.record(), independent_direct_difference=direct.record(),
            intersected_difference=difference.record(),
            relative_radius_error_upper=None if rho is None else rho.record(),
            angular_relative_target_error_upper=None if angular is None else angular.record(),
            radial_relative_target_difference=self.radial_relative.record(),
            common_relative_target_delta_upper=None if delta is None else Interval(delta).record(),
            accurate_radius_strictly_positive=positive, accurate_abs_as_strictly_below_one=subunit,
            accurate_domain_proved=positive and subunit,
            literal_reference_radius_strictly_positive=numeric[0].lo > 0,
            accurate_radius_domain_rigorously_refuted=radius_refuted,
            accurate_speed_domain_rigorously_refuted=speed_refuted,
            accurate_domain_rigorously_refuted=radius_refuted or speed_refuted,
            relative_target_work_goal_met=target_met, work_goal_is_not_native_acceptance=True,
            reasons=reasons)
        return record


class ResourceStop(Exception):
    pass


def interval_of_node(node):
    index, lo, hi, depth = node
    return dict(numeric_piece=index, closed_public_u=[str(lo), str(hi)], depth=depth)


def cover_target(target, directory, deadline, started):
    """First all original pieces; split by atomic replacement with both children.

    Until both child computations return, the certified parent remains in the
    current cover.  Every stop retains that cover plus every pending interval.
    """
    nodes = [(i, a, b, 0) for i, (a, b) in enumerate(zip(target.partition[:-1], target.partition[1:]))]
    cover = {}
    completed_records = 0
    frontier = deque()
    unvisited = []
    interrupted = None
    stop = None
    error = None
    processed = 0
    current_node = None
    maximum = POLICY["maximum_evaluated_nodes"]
    maximum_depth = POLICY["maximum_depth"]
    path = directory / "all-evaluated-nodes.jsonl"
    stream = path.open("xb")
    plan_path = directory / "complete-public-query-plan.json"
    write(plan_path, dict(schema=SCHEMA + "-complete-public-query-plan",
        run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
        closed_public_domain=["0", "1"], both_numeric_seam_sides_retained=True,
        original_closed_numeric_pieces=[interval_of_node(node) for node in nodes]))
    journal_path = directory / "cover-transactions.jsonl"
    journal = journal_path.open("xb")

    def commit(record):
        journal.write(canonical(record))
        journal.flush()

    def compute(node):
        nonlocal processed, completed_records, current_node
        current_node = node
        if processed >= maximum:
            raise ResourceStop("maximum-evaluated-node-budget")
        if time.monotonic() >= deadline:
            raise ResourceStop("wall-clock-budget")
        index = processed
        processed += 1
        record = target.evaluate(node, deadline)
        record["node_id"] = index
        record["phase_when_evaluated"] = "coarse" if node[3] == 0 else "adaptive"
        raw = canonical(record)
        stream.write(raw)
        stream.flush()
        completed_records += 1
        emit(dict(event="request151_actual_node_enclosure", record=record))
        return index, node, record

    def terminal(record):
        return (record["accurate_domain_rigorously_refuted"]
                or (record["accurate_domain_proved"] and record["relative_target_work_goal_met"]))

    try:
        for index, node in enumerate(nodes):
            try:
                node_id, computed_node, record = compute(node)
                cover[node_id] = (computed_node, record)
                commit(dict(kind="coarse-commit", node_id=node_id,
                            interval=interval_of_node(computed_node)))
                if not terminal(record):
                    frontier.append(node_id)
            except ResourceStop as exc:
                stop = str(exc)
                unvisited = [dict(interval_of_node(x), reason="initial-coarse-enclosure-not-completed") for x in nodes[index:]]
                interrupted = dict(interval_of_node(node), phase="initial-coarse", reason=stop)
                break
        initial_complete = not unvisited and len(cover) == len(nodes)
        if initial_complete:
            emit(dict(event="request151_all_original_closed_numeric_pieces_coarsely_enclosed",
                      piece_count=len(nodes), all_public_u_covered=True,
                      every_future_split_keeps_parent_until_both_children_complete=True))
        while initial_complete and frontier and stop is None:
            if time.monotonic() >= deadline:
                stop = "wall-clock-budget"
                break
            if processed + 2 > maximum:
                stop = "maximum-evaluated-node-budget-before-two-child-transaction"
                break
            parent_id = frontier.popleft()
            node, parent_record = cover[parent_id]
            index, lo, hi, depth = node
            if depth >= maximum_depth:
                parent_record["terminal_reason"] = "maximum-depth-with-honest-unresolved-enclosure"
                continue
            middle = (lo + hi) / 2
            children = [(index, lo, middle, depth + 1), (index, middle, hi, depth + 1)]
            completed_children = []
            commit(dict(kind="split-begin", parent_node_id=parent_id,
                        parent_interval=interval_of_node(node),
                        child_intervals=[interval_of_node(child) for child in children]))
            try:
                for child in children:
                    completed_children.append(compute(child))
            except ResourceStop as exc:
                stop = str(exc)
                interrupted = dict(parent_node_id=parent_id, **interval_of_node(node),
                    phase="two-child-transaction", reason=stop,
                    completed_child_node_ids_not_replacing_parent=[row[0] for row in completed_children],
                    complete_parent_enclosure_remains_in_cover=True,
                    child_not_completed=interval_of_node(children[len(completed_children)]))
                frontier.appendleft(parent_id)
                break
            del cover[parent_id]
            for child_id, child_node, child_record in completed_children:
                cover[child_id] = (child_node, child_record)
                if not terminal(child_record):
                    frontier.append(child_id)
            commit(dict(kind="split-commit", parent_node_id=parent_id,
                        child_node_ids=[row[0] for row in completed_children]))
            emit(dict(event="request151_complete_cover_atomic_split", parent_node_id=parent_id,
                      child_node_ids=[row[0] for row in completed_children], exact_children_union_is_parent=True))
    except Exception as exc:
        error = dict(type=type(exc).__name__, message=str(exc), traceback=traceback.format_exc())
        stop = "consumer-error-not-a-domain-or-native-rejection"
        if current_node is not None:
            interrupted = dict(interval_of_node(current_node), phase="actual-query-error",
                               reason=stop, actual_error=error)
    finally:
        stream.flush()
        stream.close()
        journal.flush()
        journal.close()
    # Group by each fixed numeric piece; overlap is allowed only at shared
    # endpoints.  This uses exact public rational coordinates, not float gaps.
    by_piece = [[] for _ in nodes]
    for node, _ in cover.values():
        by_piece[node[0]].append((node[1], node[2]))
    # Also cover engineering/arithmetic exceptions during the coarse pass:
    # every whole numeric piece lacking its first enclosure stays explicit.
    known_unvisited = {row["numeric_piece"] for row in unvisited}
    for index, intervals in enumerate(by_piece):
        if not intervals and index not in known_unvisited:
            unvisited.append(dict(interval_of_node(nodes[index]),
                reason="initial-coarse-enclosure-unavailable-after-" + (stop or "controlled-stop")))
    piece_cover = []
    for index, intervals in enumerate(by_piece):
        intervals.sort()
        expected_lo, expected_hi = nodes[index][1:3]
        exact_complete = bool(intervals) and intervals[0][0] == expected_lo and intervals[-1][1] == expected_hi
        exact_complete = exact_complete and all(a[1] == b[0] for a, b in zip(intervals[:-1], intervals[1:]))
        piece_cover.append(dict(numeric_piece=index, original_closed_public_u=[str(expected_lo), str(expected_hi)],
            current_leaf_count=len(intervals), exactly_complete_closed_cover=exact_complete,
            both_original_numeric_seam_sides_retained=True))
    complete = all(row["exactly_complete_closed_cover"] for row in piece_cover)
    cover_path = directory / "complete-current-cover.jsonl"
    frontier_path = directory / "complete-unresolved-frontier.jsonl"
    counts = dict(leaves=len(cover), radius_proved=0, speed_proved=0, domain_proved=0,
                  rigorously_refuted=0, relative_goal_met=0, unresolved=0)
    delta_values = []
    unbounded_delta = 0
    pending_count = 0
    frontier_ids = set(frontier)
    with cover_path.open("xb") as output, frontier_path.open("xb") as unpaid:
        for node_id, (node, record) in sorted(cover.items(), key=lambda item: (item[1][0][0], item[1][0][1])):
            current = dict(record)
            current["currently_queued_for_refinement"] = node_id in frontier_ids
            current["closed_cover_member_retained_at_stop"] = True
            output.write(canonical(current))
            emit(dict(event="request151_final_complete_cover_leaf", record=current))
            counts["radius_proved"] += int(record["accurate_radius_strictly_positive"])
            counts["speed_proved"] += int(record["accurate_abs_as_strictly_below_one"])
            counts["domain_proved"] += int(record["accurate_domain_proved"])
            counts["rigorously_refuted"] += int(record["accurate_domain_rigorously_refuted"])
            counts["relative_goal_met"] += int(record["relative_target_work_goal_met"])
            if record["common_relative_target_delta_upper"] is None:
                unbounded_delta += 1
            else:
                delta_values.append(int(record["common_relative_target_delta_upper"]["upper_integer"]))
            if not (record["accurate_domain_proved"] and record["relative_target_work_goal_met"]):
                counts["unresolved"] += int(not record["accurate_domain_rigorously_refuted"])
                pending = dict(interval_of_node(node), node_id=node_id, reasons=record["reasons"],
                    retained_complete_enclosure=current,
                    classification="rigorous-domain-refutation" if record["accurate_domain_rigorously_refuted"] else "unresolved",
                    terminal_reason=record.get("terminal_reason", stop or "work-or-domain-criterion-unresolved"))
                unpaid.write(canonical(pending))
                emit(dict(event="request151_full_pending_or_refuted_interval", record=pending))
                pending_count += 1
        for pending in unvisited:
            unpaid.write(canonical(pending))
            emit(dict(event="request151_full_unvisited_coarse_interval", record=pending))
            pending_count += 1
        if interrupted is not None:
            unpaid.write(canonical(dict(interrupted_transaction=interrupted)))
            emit(dict(event="request151_full_interrupted_transaction", record=interrupted))
    if stop is None:
        stop = "finite-adaptive-frontier-finished"
    delta = None if not complete or unbounded_delta or not delta_values else max(delta_values)
    return dict(phase="bounded-target-enclosure-finished", resource_stop_reason=stop,
        error=error, evaluated_node_attempts=processed, completed_node_records=completed_records,
        initial_numeric_pieces=len(nodes), full_public_u_closed_cover=complete,
        complete_numeric_piece_cover_records=piece_cover, current_cover_counts=counts,
        complete_unvisited_coarse_count=len(unvisited), complete_pending_or_refuted_rows=pending_count,
        current_refinement_queue_count=len(frontier), interrupted_transaction=interrupted,
        global_delta_upper=None if delta is None else Interval(delta).record(),
        global_radial_relative_target_difference=target.radial_relative.record(),
        full_target_relative_bound_finite=complete and delta is not None,
        full_accurate_radius_positivity_proved=complete and counts["radius_proved"] == len(cover),
        full_accurate_open_unit_speed_domain_proved=complete and counts["speed_proved"] == len(cover),
        full_accurate_nine_parameter_domain_proved=complete and counts["domain_proved"] == len(cover),
        at_least_one_accurate_domain_interval_rigorously_refuted=counts["rigorously_refuted"] > 0,
        comparison_work_goal_complete=complete and counts["relative_goal_met"] == len(cover),
        whole_prefix_relative_delta_below_one=delta is not None and delta < SCALE,
        accurate_total_length=target.length.record(), literal_total_length_exact=str(target.ell_q),
        original_all_nine_parameters_retained=True, accurate_target_never_replaced_by_numeric_length=True,
        literal_reference_has_both_closed_seam_sides=True, original_numeric_local_variable_never_clipped=True,
        all_possible_accurate_pieces_and_controls_kept=True,
        raw_files=dict(evaluated_nodes=receipt(path), current_cover=receipt(cover_path),
                       complete_frontier=receipt(frontier_path), original_query_plan=receipt(plan_path),
                       complete_cover_transactions=receipt(journal_path)),
        elapsed_seconds_including_binding=time.monotonic() - started,
        complete_cover_and_all_pending_records_printed_before_cleanup=True)


def readback_only(argv):
    """Pure metadata recovery after an actual interrupted/failed target step.

    Transaction replay only joins previously recorded interval strings and
    node IDs.  It never reevaluates an interval, polynomial, profile or bound.
    """
    parser = argparse.ArgumentParser(description=readback_only.__doc__)
    parser.add_argument("--readback-only", action="store_true", required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    actions_only()
    root = Path(os.environ["RUNNER_TEMP"]).resolve()
    if not args.out.resolve().is_relative_to(root) or args.out.resolve() == root:
        raise ValueError("Read only this same job's temporary target output")
    summary_path = args.out / "summary.json"
    if summary_path.is_file():
        raw = summary_path.read_bytes()
        summary = json.loads(raw)
        same_run(summary, "actual target summary")
        if summary.get("schema") != SCHEMA or len(raw) > 90000:
            raise ValueError("The actual target summary identity or transport size differs")
        full, _, _ = member(args.out, summary["actual_complete_result"])
        same_run(full, "actual complete target result")
        emit(dict(event="request151_primary_complete_result_readback_identity",
                  actual_summary=receipt(summary_path), original_result=summary["actual_complete_result"],
                  original_scientific_exit=full["scientific_controlled_exit_code"],
                  no_new_scientific_arithmetic=True))
    else:
        identities = {}
        for name in ("input-binding.json", "original-Q-to-fixed-grid.json", "complete-public-query-plan.json", "result.json"):
            path = args.out / name
            if path.is_file():
                value, identity = read(path)
                identities[name] = identity
                emit_segments("interrupted-retained-" + name, value)
        plan_path = args.out / "complete-public-query-plan.json"
        plan = json.loads(plan_path.read_bytes()) if plan_path.is_file() else None
        node_path = args.out / "all-evaluated-nodes.jsonl"
        node_info = {}
        truncated = []
        if node_path.is_file():
            identities[node_path.name] = receipt(node_path)
            with node_path.open("rb") as stream:
                while True:
                    start = stream.tell()
                    line = stream.readline()
                    if not line:
                        break
                    try:
                        row = json.loads(line)
                    except Exception as exc:
                        malformed = dict(file=node_path.name, byte_offset=start, bytes=len(line),
                            sha256=sha(line), actual_parse_error=repr(exc),
                            complete_original_text_json_ascii=json.dumps(line.decode("utf-8", "surrogateescape"), ensure_ascii=True))
                        truncated.append({key: value for key, value in malformed.items() if key != "complete_original_text_json_ascii"})
                        emit_segments("interrupted-raw-node-line", malformed)
                        continue
                    index = row["node_id"]
                    if index in node_info:
                        raise ValueError("The original temporary node stream repeats a node ID")
                    node_info[index] = dict(offset=start, bytes=len(line), numeric_piece=row["numeric_piece"],
                        closed_public_u=row["closed_public_u"], depth=row["depth"],
                        reasons=row["reasons"], domain_proved=row["accurate_domain_proved"],
                        goal_met=row["relative_target_work_goal_met"], refuted=row["accurate_domain_rigorously_refuted"])
                    emit(dict(event="request151_recovered_original_complete_node", record=row))
        cover_ids = set()
        committed_pieces = set()
        transaction_errors = []
        active_splits = {}
        journal_path = args.out / "cover-transactions.jsonl"
        if journal_path.is_file():
            identities[journal_path.name] = receipt(journal_path)
            with journal_path.open("rb") as stream:
                for line in stream:
                    try:
                        row = json.loads(line)
                    except Exception as exc:
                        transaction_errors.append(dict(error=repr(exc), bytes=len(line), sha256=sha(line)))
                        emit_segments("interrupted-raw-transaction-line", dict(bytes=len(line), sha256=sha(line),
                            complete_original_text_json_ascii=json.dumps(line.decode("utf-8", "surrogateescape"), ensure_ascii=True)))
                        continue
                    emit(dict(event="request151_recovered_original_cover_transaction", record=row))
                    if row["kind"] == "coarse-commit":
                        index = row["node_id"]
                        if index not in node_info or plan is None:
                            raise ValueError("A retained coarse transaction has no complete original node or plan")
                        current = node_info[index]
                        origin = plan["original_closed_numeric_pieces"][current["numeric_piece"]]
                        same(row["interval"], origin, "retained coarse interval and original query plan")
                        same(current["closed_public_u"], origin["closed_public_u"], "retained coarse node interval")
                        if current["numeric_piece"] in committed_pieces or current["depth"] != 0:
                            raise ValueError("A retained original coarse piece was committed twice or at wrong depth")
                        cover_ids.add(index)
                        committed_pieces.add(current["numeric_piece"])
                    elif row["kind"] == "split-begin":
                        active_splits[row["parent_node_id"]] = row
                    elif row["kind"] == "split-commit":
                        parent = row["parent_node_id"]
                        ids = row["child_node_ids"]
                        if parent not in cover_ids or len(ids) != 2 or any(i not in node_info for i in ids):
                            raise ValueError("A completed split lacks its retained parent or two complete nodes")
                        p, a, b = node_info[parent], node_info[ids[0]], node_info[ids[1]]
                        if not (a["numeric_piece"] == b["numeric_piece"] == p["numeric_piece"]
                            and a["depth"] == b["depth"] == p["depth"] + 1
                            and a["closed_public_u"][0] == p["closed_public_u"][0]
                            and a["closed_public_u"][1] == b["closed_public_u"][0]
                            and b["closed_public_u"][1] == p["closed_public_u"][1]):
                            raise ValueError("Recorded split endpoints do not form their original closed parent")
                        cover_ids.remove(parent)
                        cover_ids.update(ids)
                        active_splits.pop(parent, None)
                    else:
                        raise ValueError("Unknown original cover transaction kind")
        unvisited = [] if plan is None else [row for row in plan["original_closed_numeric_pieces"]
                                             if row["numeric_piece"] not in committed_pieces]
        if node_path.is_file():
            with node_path.open("rb") as stream:
                for index in sorted(cover_ids):
                    info = node_info[index]
                    stream.seek(info["offset"])
                    actual = json.loads(stream.read(info["bytes"]))
                    emit(dict(event="request151_recovered_complete_current_cover_leaf", record=actual))
                    if not (info["domain_proved"] and info["goal_met"]):
                        emit(dict(event="request151_recovered_full_pending_or_refuted_interval",
                            node_id=index, numeric_piece=info["numeric_piece"],
                            closed_public_u=info["closed_public_u"], depth=info["depth"], reasons=info["reasons"],
                            rigorous_refutation=info["refuted"], complete_original_enclosure=actual,
                            reason_for_unfinished_adaptation="actual-target-step-interrupted-or-no-primary-summary"))
        for row in unvisited:
            emit(dict(event="request151_recovered_full_unvisited_original_piece", record=row,
                      reason="initial-coarse-transaction-not-committed"))
        for row in active_splits.values():
            emit(dict(event="request151_recovered_full_interrupted_split", record=row,
                      original_parent_kept_in_current_cover=True))
        summary = dict(schema=SCHEMA, repository=REPOSITORY, run_id=os.environ["GITHUB_RUN_ID"],
            source_commit=os.environ["GITHUB_SHA"], source=receipt(Path(__file__)),
            phase="actual-interrupted-output-metadata-recovered", procedure_complete=False,
            summary_complete=False, transport_complete=True, primary_summary_missing=True,
            all_retained_original_values_and_pending_intervals_emitted=True,
            no_new_scientific_arithmetic=True, actual_retained_files=identities,
            retained_complete_node_count=len(node_info), current_cover_node_count=len(cover_ids),
            original_query_piece_count=None if plan is None else len(plan["original_closed_numeric_pieces"]),
            complete_unvisited_original_piece_count=len(unvisited), incomplete_transactions=len(active_splits),
            all_original_query_pieces_have_coarse_coverage=plan is not None and not unvisited and not transaction_errors,
            exact_transaction_cover_reconstructed_without_new_bound_arithmetic=True,
            original_truncated_node_lines=truncated, actual_transaction_parse_errors=transaction_errors,
            global_delta_not_recomputed=True, global_delta_upper=None,
            actual_native_or_fullDN_or_accepted_field=False, original_target_step_failure_not_relabelled=True,
            missing_definition_or_plan_not_invented=plan is None)
        raw = canonical(summary)
        if len(raw) > 90000:
            complete = emit_segments("complete-interrupted-target-readback-summary", summary)
            raw = canonical(dict(schema=SCHEMA, run_id=os.environ["GITHUB_RUN_ID"],
                source_commit=os.environ["GITHUB_SHA"], summary_complete=False, transport_complete=False,
                primary_summary_missing=True, complete_interrupted_summary_log=complete))
        if len(raw) > 90000:
            raise RuntimeError("Even the incomplete readback summary exceeds the output bound")
    print("BEGIN_REQUEST151_COMMON_U_TARGET_SUMMARY", flush=True)
    print(raw.decode("ascii"), end="", flush=True)
    print("END_REQUEST151_COMMON_U_TARGET_SUMMARY", flush=True)
    emit(dict(event="request151_target_readback_identity", bytes=len(raw), sha256=sha(raw),
              no_new_scientific_arithmetic=True, original_science_outcome_retained_separately=True))
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as output:
            output.write("target_summary=" + raw.decode("ascii").rstrip("\n") + "\n")
            output.write("target_summary_bytes=" + str(len(raw)) + "\n")
            output.write("target_summary_sha256=" + sha(raw) + "\n")
    return 0 if json.loads(raw).get("transport_complete") else 70


def bind_request(args):
    request, request_receipt = read(args.request)
    original, original_receipt = read(args.original_request,
        dict(bytes=ORIGINAL_REQUEST_BYTES, sha256=ORIGINAL_REQUEST_SHA))
    if (args.original_request.name != ORIGINAL_REQUEST_NAME
            or original["schema"] != "public-continuous-nine-v3-construction-request-v1"
            or original["request_number"] != 147 or original["source_count"] != 19):
        raise ValueError("Invoke the exact original147 request as an independent atomic subprogram")
    if (request["schema"] != REQUEST_SCHEMA or request["request_number"] != 151
            or request["repository"] != REPOSITORY or request["target_policy"] != POLICY):
        raise ValueError("Use the explicit independent request151 and its declared bounded policy")
    same(request["original_atomic_request"], dict(file=ORIGINAL_REQUEST_NAME,
        bytes=ORIGINAL_REQUEST_BYTES, sha256=ORIGINAL_REQUEST_SHA), "actual original atomic request identity")
    if request["source_count"] != 20 or len(request["source_sha256"]) != 20:
        raise ValueError("Retain all19 original sources and the new independent consumer")
    sources = []
    for name, expected in request["source_sha256"].items():
        if PurePosixPath(name).name != name or re.fullmatch(r"[0-9a-f]{64}", expected) is None:
            raise ValueError("Invalid explicit scientific source basename/pin")
        path = args.code_directory / name
        source = receipt(path)
        if source["sha256"] != expected:
            raise ValueError("Actual scientific source differs: " + name)
        if name != Path(__file__).name and original["source_sha256"].get(name) != expected:
            raise ValueError("An original147 source was replaced")
        sources.append(source)
    if request["source_sha256"].get(Path(__file__).name) != sha(Path(__file__).read_bytes()):
        raise ValueError("The actual independent target consumer is not pinned")
    proofs = []
    for proof in request["target_proofs"]:
        path = args.repository_directory / proof["file"]
        identity = receipt(path)
        same({k: identity[k] for k in ("bytes", "sha256")},
             {k: proof[k] for k in ("bytes", "sha256")}, "actual published target proof")
        proofs.append(identity)
    same(request["literal_nine_parameters"], original["construction"]["initial_nine_parameters"],
         "same actual R320 nine literal parameters")
    actual_E_work = dict(original["scientific_parameters"])
    actual_E_work["budget_seconds"] = ACTUAL_E_BUDGET_SECONDS
    same(request["actual_continuous_E_reconstruction"]["scientific_parameters"], actual_E_work,
         "only the explicitly authorised C work budget changes from original147")
    return request, original, dict(actual_request=request_receipt,
        original_atomic_request=original_receipt, complete_scientific_sources=sources,
        actual_published_target_proofs=proofs)


def main(argv=None):
    arguments = sys.argv[1:] if argv is None else list(argv)
    if "--readback-only" in arguments:
        return readback_only(arguments)
    parser = argparse.ArgumentParser(description=__doc__)
    for option in ("request", "original-request", "inputs-directory", "tail-cover-directory",
                   "cut-twojet-readout", "construction-directory", "code-directory", "repository-directory", "out"):
        parser.add_argument("--" + option, type=Path, required=True)
    args = parser.parse_args(arguments)
    actions_only()
    started = time.monotonic()
    deadline = started + POLICY["budget_seconds"]
    out = args.out.resolve()
    runner_root = Path(os.environ["RUNNER_TEMP"]).resolve()
    if out == runner_root or not out.is_relative_to(runner_root) or args.out.exists():
        raise ValueError("Use a fresh owned RUNNER_TEMP target output directory")
    for key, path in vars(args).items():
        if key != "out" and (path.resolve() == out or path.resolve().is_relative_to(out)):
            raise ValueError("Fresh target output cannot own an original input")
    args.out.mkdir(parents=True)
    result = dict(schema=SCHEMA, repository=REPOSITORY, run_id=os.environ["GITHUB_RUN_ID"],
        source_commit=os.environ["GITHUB_SHA"], source=receipt(Path(__file__)),
        phase="bind-actual-same-job-inputs", error=None, procedure_complete=False,
        full_public_u_closed_cover=False, full_accurate_nine_parameter_domain_proved=False,
        full_target_relative_bound_finite=False, comparison_work_goal_complete=False,
        actual_field_created=False, native_success=False, fullDN_success=False,
        true_IEEE_evaluator_error_bound_supplied=False, same_field_metric_certificate_paid=False,
        whole_tail_or_caps_or_closed_geometry_or_strong_C2_or_reach_or_held_paid=False,
        all_raw_recomputable_outputs_temporary_only=True, new_native_acceptance_gate=False,
        target_policy=POLICY)
    code = 0
    try:
        request, original, source_binding = bind_request(args)
        rebuilt = rebuild_actual(args, request, original)
        factory, model, values, literal, compilation, partition, ell, binding, grid_rows = rebuilt
        binding.update(source_binding)
        input_receipt = write(args.out / "input-binding.json", binding)
        grid_receipt = write(args.out / "original-Q-to-fixed-grid.json", grid_rows)
        result.update(input_binding=input_receipt, exact_Q_grid_binding=grid_receipt,
            complete_input_binding_log=emit_segments("complete-input-and-rebuilt-definition-binding", binding),
            complete_grid_conversion_log=emit_segments("complete-original-Q-node-outward-conversions", grid_rows))
        result["phase"] = "complete-coarse-then-adaptive-public-u-cover"
        target = CompleteTarget(factory, model, values, literal, compilation, partition, ell)
        result.update(cover_target(target, args.out, deadline, started))
        result["procedure_complete"] = result["error"] is None
        if result["error"] is not None:
            code = 2
        elif result["at_least_one_accurate_domain_interval_rigorously_refuted"]:
            code = 4
        elif not (result["full_public_u_closed_cover"] and result["comparison_work_goal_complete"]
                  and result["full_accurate_nine_parameter_domain_proved"]):
            code = 3
    except Exception as exc:
        result["error"] = dict(type=type(exc).__name__, message=str(exc), traceback=traceback.format_exc())
        result["current_source_or_enclosure_failure_not_a_native_rejection"] = True
        code = 2
    result["elapsed_seconds_including_binding"] = time.monotonic() - started
    result["scientific_controlled_exit_code"] = code
    full_receipt = write(args.out / "result.json", result)
    # The whole result, every current cover member and every pending interval
    # are available in compute stdout before the workflow removes raw output.
    full_log = emit_segments("complete-target-result", result)
    summary = dict(result)
    summary.pop("complete_numeric_piece_cover_records", None)
    summary.update(actual_complete_result=full_receipt, complete_result_log=full_log,
        summary_complete=True, all_scientific_fields_and_scope_available_in_complete_compute_log=True,
        transport_complete=True, hash_scope="canonical ASCII UTF8 including final LF")
    raw = canonical(summary)
    if len(raw) > 90000:
        # Explicit transport failure never changes scientific completion or
        # suppresses the full original result already printed losslessly above.
        summary = {key: result[key] for key in ("schema", "repository", "run_id", "source_commit", "source",
            "phase", "procedure_complete", "full_public_u_closed_cover", "full_accurate_nine_parameter_domain_proved",
            "full_target_relative_bound_finite", "comparison_work_goal_complete", "scientific_controlled_exit_code")}
        summary.update(summary_complete=False, transport_complete=False,
            actual_complete_result=full_receipt, complete_result_log=full_log,
            full_result_retained_in_complete_compute_log=True,
            oversized_summary_original_bytes=len(raw), oversized_summary_original_sha256=sha(raw))
        raw = canonical(summary)
        code = 70
    if len(raw) > 90000:
        raise RuntimeError("Even the explicit request151 transport-failure summary exceeds 90000 bytes")
    (args.out / "summary.json").write_bytes(raw)
    print("BEGIN_REQUEST151_COMMON_U_TARGET_SUMMARY", flush=True)
    print(raw.decode("ascii"), end="", flush=True)
    print("END_REQUEST151_COMMON_U_TARGET_SUMMARY", flush=True)
    emit(dict(event="request151_target_summary_identity", bytes=len(raw), sha256=sha(raw),
              hash_scope="canonical ASCII UTF8 including final LF", scientific_exit=result["scientific_controlled_exit_code"],
              actual_process_exit=code))
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as output:
            output.write("target_summary=" + raw.decode("ascii").rstrip("\n") + "\n")
            output.write("target_summary_bytes=" + str(len(raw)) + "\n")
            output.write("target_summary_sha256=" + sha(raw) + "\n")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
