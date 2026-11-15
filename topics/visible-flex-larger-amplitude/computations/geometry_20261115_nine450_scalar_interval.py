#!/usr/bin/env python3
"""Exact-real scalar adapter for an actual all-nine-frozen450 v2 field.

Reuse the published nine-family interpreter, including the genuine nested
three-control finite-Gauss expression.  Point, batch and exact-real targets
keep separate identities.  Reading a checkpoint does not establish a live
constructor-table match, global C2 interfaces, or a new native acceptance.
Scientific imports and evaluation are public repository Actions only.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import struct
import sys

HERE = Path(__file__).resolve().parent
REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "frozen-nine450-exact-real-scalar-interval-adapter-v1"
DESCRIPTOR_SCHEMA = "frozen-nine450-complete-scalar-real-expression-v1"
PROFILE_SCHEMA = "frozen-nine-control-complete-same-metric-scalar-v2"
PARAMETER_ORDER = ["p1", "p2", "p3", "theta1", "theta2", "theta3", "eta1", "eta2", "eta3"]
SOURCE_PINS = {
    "geometry_20261115_small_core_nine_control_family.py": "086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629",
    "geometry_20261115_nine_control_same_metric_profile_v2.py": "5e95afdb82f83a276003e6a4846e20893b7eb7f2b44b309d56950f11dbfaa0d3",
    "geometry_20261115_nine_control_same_metric_full112_v2.py": "92cfb0701824df770dfcd009a623e84695e72fe9c489d70537d8983415adc7e8",
    "geometry_20261115_nine_control_same_metric_saved_prefix.py": "e8deb4136dbaf021d2648e02a2cdb774db4ebe1836b239b609472c596fc70404",
    "geometry_20261114_full_prefix_operator.py": "a9a25d96eeb286d9f2214f997c992e50e42f6e6ec2bc59c136a183febe2a0703",
    "geometry_20261114_direct_operator_cell.py": "1774f8da00ccd8ced6199e85d1fda6f455a224eed7d20d1a92ac04df3801e2ce",
}


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("Scientific evaluation is restricted to this public repository's Actions")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
        ensure_ascii=False, allow_nan=False)+"\n").encode()


def receipt(path):
    path = Path(path)
    raw = path.read_bytes()
    return dict(file=path.name, bytes=len(raw), sha256=sha(raw))


def checked_runtime(directory=HERE):
    require_actions()
    directory = Path(directory).resolve()
    sources = {name:receipt(directory/name) for name in SOURCE_PINS}
    for name, expected in SOURCE_PINS.items():
        if sources[name]["sha256"] != expected:
            raise ValueError("A frozen scalar/450 source differs: "+name)
    sys.path.insert(0, str(directory))
    loaded = {}
    for name in SOURCE_PINS:
        module_name = name[:-3]
        previous = sys.modules.get(module_name)
        if previous is not None:
            if receipt(previous.__file__)["sha256"] != SOURCE_PINS[name]:
                raise ValueError("A different scalar module is already loaded: "+name)
            module = previous
        else:
            spec = importlib.util.spec_from_file_location(module_name, directory/name)
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)
        loaded[name] = module
    family = loaded["geometry_20261115_small_core_nine_control_family.py"]
    profile = loaded["geometry_20261115_nine_control_same_metric_profile_v2.py"]
    prefix = loaded["geometry_20261114_full_prefix_operator.py"]
    cell = loaded["geometry_20261114_direct_operator_cell.py"]
    for name, digest in {**prefix.checked_original_sources(), **family.checked_sources(),
                         **profile.checked_sources()}.items():
        if name in sources and sources[name]["sha256"] != digest:
            raise ValueError("Conflicting actual source closure: "+name)
        sources[name] = receipt(directory/name)
        if sources[name]["sha256"] != digest:
            raise ValueError("Imported scalar dependency differs: "+name)
    return dict(family=family, profile=profile, prefix=prefix, cell=cell,
        saved=loaded["geometry_20261115_nine_control_same_metric_saved_prefix.py"],
        source_closure=sources)


def valid_sha(value):
    return isinstance(value, str) and len(value) == 64 and all(c in "0123456789abcdef" for c in value)


def export_scalar_descriptor(runtime, frozen_profile, frozen_specification, *,
        checkpoint_sha256, origin="reconstructed-from-checkpoint"):
    require_actions()
    profile, family = runtime["profile"], runtime["family"]
    if (not valid_sha(checkpoint_sha256)
            or origin not in ("reconstructed-from-checkpoint", "actual-live-profile")):
        raise ValueError("Name this actual completed checkpoint and the real table provenance")
    if (frozen_specification.get("schema") != PROFILE_SCHEMA
            or frozen_specification.get("parameter_order") != PARAMETER_ORDER
            or frozen_specification.get("active_parameter_indices") != []
            or frozen_specification.get("frozen_parameter_indices") != list(range(9))
            or profile.canonical_bytes(frozen_profile.specification) !=
               profile.canonical_bytes(frozen_specification)
            or profile.words(frozen_profile.frozen_parameters.tolist()) !=
               frozen_specification["frozen_nine_float64le"]):
        raise ValueError("Consume the complete actual v2 nine-frozen profile, not its empty active vector")
    design = frozen_specification["frozen_design_scalar_profile"]
    designed = frozen_profile.designed_nine
    if (len(designed.bumps) != 9 or int(designed.parameter_count) != 9
            or profile.words(design["frozen_design_parameters"]) !=
               frozen_specification["frozen_nine_float64le"]):
        raise ValueError("A frozen control/support was omitted")
    supports = [dict(index=i, parameter=PARAMETER_ORDER[i],
        left_float64le=struct.pack("<d", float(b.left)).hex(),
        right_float64le=struct.pack("<d", float(b.right)).hex(),
        stored_width_float64le=struct.pack("<d", float(b.width)).hex())
        for i,b in enumerate(designed.bumps)]
    if supports != frozen_specification["scalar_support_float64le"]:
        raise ValueError("A stored width or one of the nine support words differs")
    identity = profile.scalar_identity_payload(design, supports)
    if (profile.canonical_sha(identity) != frozen_specification["canonical_scalar_identity_sha256"]
            or frozen_specification["finite_assembly"] != profile.finite_assembly_contract()):
        raise ValueError("The v2 point/batch finite-assembly identity differs")
    # This is a genuinely nested v3 definition inside the original nine
    # family.  The accepted450 schema is never presented to the old reader.
    nine = family.export_scalar_descriptor(designed, design)
    expression = dict(
        exact_target="The complete nine-control exact-real expression on copied binary constants",
        frozen_v2_scalar_identity_sha256=frozen_specification["canonical_scalar_identity_sha256"],
        complete_frozen_specification_sha256=profile.canonical_sha(frozen_specification),
        complete_nine_design_specification_sha256=family.canonical_sha(design),
        parameter_order=PARAMETER_ORDER,
        frozen_nine_float64le=frozen_specification["frozen_nine_float64le"],
        all_nine_support_words=supports,
        original_nine_family_mathematical_identity_sha256=nine["mathematical_identity_sha256"],
        original_nine_family_expression=nine["mathematical_expression"],
        frozen_v2_finite_assembly=copy.deepcopy(frozen_specification["finite_assembly"]),
        real_addition_commutes_but_point_batch_binary_sums_are_not_identified=True,
        returned_ap_app_not_used_as_derivatives_of_the_finite_Gauss_radius=True)
    return dict(schema=DESCRIPTOR_SCHEMA, source_sha256=sha(Path(__file__).read_bytes()),
        mathematical_expression=expression, mathematical_identity_sha256=sha(canonical(expression)),
        complete_frozen_specification_sha256=profile.canonical_sha(frozen_specification),
        frozen_v2_scalar_identity_sha256=frozen_specification["canonical_scalar_identity_sha256"],
        original_nine_descriptor=nine,
        producer=dict(origin=origin, checkpoint_sha256=checkpoint_sha256,
            profile_class=type(frozen_profile).__module__+"."+type(frozen_profile).__name__,
            exporter_source_sha256=sha(Path(__file__).read_bytes()),
            origin_is_caller_declaration=True,
            actual_live_execution_attested_by_this_exporter=False),
        source_closure=runtime["source_closure"],
        all_nine_parameters_and_supports_retained=True,
        original_base_48_turn_and_64_bridge_Gauss_tables_copied=True,
        literal_floating_point_or_batch_evaluator_error_certified=False,
        original_returned_ap_app_equals_true_radius_derivatives_proved=False,
        original_global_scalar_C2_interfaces_proved=False,
        added_six_polynomial_controls_alone_have_zero_012_boundary_jets=True,
        empty_active_vector_relabelled_as_zero_scalar_parameters=False)


def descriptor_binding(reconstructed, supplied=None, supplied_receipt=None):
    result = dict(external_descriptor_supplied=supplied is not None,
        actual_live_runtime_constants_verified=False,
        complete_frozen_scalar_identity_sha256=reconstructed["frozen_v2_scalar_identity_sha256"],
        mathematical_identity_sha256=reconstructed["mathematical_identity_sha256"],
        declared_expression_bound_to_current_reconstruction=True,
        point_batch_and_real_arithmetic_identified=False,
        scalar_C2_or_literal_floating_error_proved=False)
    if supplied is None:
        result["unpaid"] = "No actual-live v2 descriptor sidecar; bind this reconstruction's exact-real expression only"
        return result
    if (supplied.get("schema") != DESCRIPTOR_SCHEMA
            or supplied.get("source_sha256") != sha(Path(__file__).read_bytes())
            or supplied.get("mathematical_identity_sha256") != sha(canonical(supplied["mathematical_expression"]))
            or supplied["mathematical_expression"] != reconstructed["mathematical_expression"]
            or supplied.get("complete_frozen_specification_sha256") != reconstructed["complete_frozen_specification_sha256"]):
        raise ValueError("The supplied v2 scalar sidecar has other complete coefficients or construction tables")
    producer = supplied.get("producer", {})
    declared_live = (producer.get("origin") == "actual-live-profile"
        and producer.get("checkpoint_sha256") == reconstructed["producer"]["checkpoint_sha256"]
        and producer.get("exporter_source_sha256") == sha(Path(__file__).read_bytes()))
    result.update(external_descriptor=supplied_receipt,
        external_descriptor_producer=producer,
        exact_mathematical_descriptor_match=True,
        supplied_descriptor_declares_matching_live_provenance=declared_live,
        actual_live_runtime_constants_verified=False,
        completed450_producer_record_binding_live_exporter_not_supplied=True,
        JSON_origin_or_exporter_hash_used_as_historical_execution_proof=False)
    result["unpaid"] = (
        "The matching JSON declares live provenance, but the frozen450 producer has no bound live-export event; this declaration is not verified execution"
        if declared_live else
        "Matching expression; actual-live construction provenance for this checkpoint is absent")
    return result


class ScalarExpression:
    """The original nine interpreter with explicit v2 identity and real derivatives."""
    def __init__(self, runtime, frozen_specification, descriptor):
        require_actions()
        profile, family, cell = runtime["profile"], runtime["family"], runtime["cell"]
        if (descriptor.get("schema") != DESCRIPTOR_SCHEMA
                or descriptor["complete_frozen_specification_sha256"] != profile.canonical_sha(frozen_specification)
                or descriptor["mathematical_identity_sha256"] != sha(canonical(descriptor["mathematical_expression"]))):
            raise ValueError("The scalar interpreter requires its complete current450 descriptor")
        self.original = family.ScalarExpression(frozen_specification["frozen_design_scalar_profile"],
            descriptor["original_nine_descriptor"], cell)
        self.base = self.original.base
        self.cell, self.arb, self.arb_series = cell, self.base.arb, self.base.arb_series
        self.b, self.boundaries = self.original.b, self.base.boundaries
        self.breakpoints = sorted(set(self.original.breakpoints))
        self.d = descriptor["mathematical_expression"]
        self._prefix = runtime["prefix"]
        # Every odd/quadratic support uses the same exact left+stored_width
        # as its original even control.  Do not replace that by recorded right.
        for control in self.original.odd_controls+self.original.quadratic_controls:
            for end in (control["left"], control["left"]+control["stored_width"]):
                if self.breakpoints[0] < end < self.breakpoints[-1] and end not in self.breakpoints:
                    raise ValueError("A genuine stored-width support boundary is missing")

    def branch(self, middle):
        return self.original.branch(middle)

    def value(self, s, branch, middle):
        return self.original.value(s, branch, middle)

    def exact_degree(self, branch, middle):
        degree = self.base.exact_degree(branch, middle)
        if degree is None:
            return None
        for coefficients, controls, added_degree in (
                (self.original.odd_coefficients, self.original.odd_controls, 7),
                (self.original.quadratic_coefficients, self.original.quadratic_controls, 8)):
            if any(p and c["left"] < middle < c["left"]+c["stored_width"]
                   for p,c in zip(coefficients,controls)):
                degree = max(degree, added_degree)
        return degree

    def envelope(self, left, right, nonpolynomial_degree=4):
        # The old Taylor/Bernstein machinery dispatches through this value
        # and exact_degree, so all nine terms participate in every derivative.
        return self._prefix.ScalarExpression.envelope(self, left, right, nonpolynomial_degree)

    def branch_derivative_enclosure(self, left, right):
        """Value/true first/true second derivative of one analytic branch.

        This does not assert differentiability across its closed endpoints.
        The metric consumer separately unions actual selected endpoint values.
        """
        if left > right or any(left < c < right for c in self.breakpoints):
            raise ValueError("Split every original scalar branch and support first")
        middle = (left+right)/2
        branch = self.branch(middle)
        old_cap = self.cell.ctx.cap
        try:
            self.cell.ctx.cap = max(int(old_cap), 3)
            interval = self.b(left).union(self.b(right))
            series = self.value(self.arb_series([interval, self.arb(1)], prec=3), branch, middle)
            if series.prec < 3:
                raise ArithmeticError("The exact-real scalar derivative series was truncated")
            return (series[0], series[1], 2*series[2]), dict(
                branch=list(branch), interval=[str(left),str(right)],
                derivatives_are_of_this_finite_Gauss_real_expression=True,
                old_returned_ap_app_substituted=False, global_C2_claimed=False)
        finally:
            self.cell.ctx.cap = old_cap


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--checkpoint", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--code-directory", type=Path, default=HERE)
    args = p.parse_args()
    require_actions()
    if args.out.exists():
        raise FileExistsError("Use a fresh temporary descriptor path")
    runtime = checked_runtime(args.code_directory)
    saved = runtime["saved"].NineControlSameMetricSavedPrefix(args.checkpoint)
    descriptor = export_scalar_descriptor(runtime, saved.profile_model,
        saved.rec["fixed_scalar_profile"]["geometry"],
        checkpoint_sha256=receipt(args.checkpoint)["sha256"])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_bytes(canonical(descriptor))
    print(json.dumps(dict(event="frozen-nine450-scalar-real-expression", output=receipt(args.out),
        actual_live_tables_certified=False, actual_field_acceptance_created=False), separators=(",", ":")), flush=True)


if __name__ == "__main__":
    main()
