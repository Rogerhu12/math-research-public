#!/usr/bin/env python3
"""Continuous C2 bounds for two actual complete v2 shared-R tail maps.

Both inputs are real accepted lambda-one nonlinear-DN fields of the same
frozen problem. Compare their declared finite Cartesian maps on the same
physical radius disk. No source Fourier truncation error is set to zero,
no translation or rigid alignment is performed, and one finite pair is
not a Cauchy proof. Exact cut Hermite seam corrections are outside this
baseline-map comparison.
"""
import argparse
from dataclasses import dataclass
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import io
import json
import math
from pathlib import Path
import sys
import time

from seam_export_tail_geometry_v2 import (
    read, sha, ref, checked, canonical_sha, write, fresh_dir, state_match,
)
from seam_certify_tail_geometry_v2 import validate_inputs, fq, sqrt_upper, upper_row, H
from seam_tail_spectrum_v2 import GEOMETRY_SCHEMA, validate_spectrum_container
from seam_restore_true_background import DEFINITION_SHA


HERE = Path(__file__).resolve().parent
TOPIC = HERE.parents[1]
REPO = TOPIC.parents[1]
MULTI_INDICES = ((0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2))
BASE_ACTUAL_KIND = "warm-supported-material-phase-fixed-metric-actual-dn"
ACTUAL_KINDS = {BASE_ACTUAL_KIND, BASE_ACTUAL_KIND + "-refinement-v1"}
ZERO = [Q(0)]


def verify_ref(reference):
    """Hash large bound runner data with constant memory."""
    digest = hashlib.sha256()
    with Path(reference["path"]).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    if digest.hexdigest() != reference["sha256"]:
        raise ValueError("A bound input changed: " + reference["path"])


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


def add(a, b):
    out = [Q(0)] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    return out


def derivative(poly, width):
    return [(j + 1) * poly[j + 1] / width for j in range(len(poly) - 1)] or ZERO


def evaluate(poly, t):
    value = Q(0)
    for coefficient in reversed(poly):
        value = value * t + coefficient
    return value


def hermite(left, right, width):
    """Exact quintic of the declared two endpoint physical-R two-jets."""
    y0, d0, dd0 = left
    y1, d1, dd1 = right
    delta, u0, u1 = y1 - y0, width * d0, width * d1
    v0, v1 = width * width * dd0, width * width * dd1
    return [y0, u0, v0 / 2,
            10 * delta - 6 * u0 - 4 * u1 - Q(3, 2) * v0 + v1 / 2,
            -15 * delta + 8 * u0 + 7 * u1 + Q(3, 2) * v0 - v1,
            6 * delta - 3 * u0 - 3 * u1 - v0 / 2 + v1 / 2]


def restrict(poly, start, length):
    """Power coefficients of p(start + length*u), all exact rationals."""
    if not 0 <= start < start + length <= 1:
        raise ValueError("A common span leaves its original polynomial domain")
    return [length ** k * sum(
        (poly[j] * math.comb(j, k) * start ** (j - k)
         for j in range(k, len(poly))), Q(0)) for k in range(len(poly))]


def bernstein_abs(poly):
    n = len(poly) - 1
    return max(abs(sum(
        (poly[j] * Q(math.comb(k, j), math.comb(n, j))
         for j in range(k + 1)), Q(0))) for k in range(n + 1))


@dataclass
class Span:
    left: Q
    right: Q
    polys: dict
    provenance: dict


def common_spans(left_iterator, right_iterator, outer):
    """Stream the exact union partition without loading all stage arrays."""
    left, right = next(left_iterator), next(right_iterator)
    cursor, ordinal = Q(0), 0
    if left.left != cursor or right.left != cursor:
        raise ValueError("Both complete disks must begin at their actual center")
    while True:
        endpoint = min(left.right, right.right)
        if not (left.left <= cursor < endpoint <= left.right and
                right.left <= cursor < endpoint <= right.right):
            raise ValueError("The complete common-R coverage has a gap")
        yield ordinal, cursor, endpoint, left, right
        ordinal += 1
        cursor = endpoint
        if cursor == outer:
            if left.right != outer or right.right != outer:
                raise ValueError("A represented disk has a different outer cut")
            for iterator in (left_iterator, right_iterator):
                if next(iterator, None) is not None:
                    raise ValueError("The represented disk extends beyond the actual cut")
            return
        if cursor > outer:
            raise ValueError("The common radius partition passed the actual cut")
        if cursor == left.right:
            left = next(left_iterator, None)
            if left is None or left.left != cursor:
                raise ValueError("The left complete disk ended or has a gap")
        if cursor == right.right:
            right = next(right_iterator, None)
            if right is None or right.left != cursor:
                raise ValueError("The right complete disk ended or has a gap")


def compare_span(left, right, low, high, modes, delta_mu_cut):
    """Right minus left, relative to the actual (unremoved) Delta Z_cut."""
    width = high - low
    bounds = {key: Q(0) for key in MULTI_INDICES}
    for key in modes:
        lp = restrict(left.polys.get(key, ZERO),
                      (low - left.left) / (left.right - left.left),
                      width / (left.right - left.left))
        rp = restrict(right.polys.get(key, ZERO),
                      (low - right.left) / (right.right - right.left),
                      width / (right.right - right.left))
        difference = add(rp, [-v for v in lp])
        if key == ("height", 0):
            # z = Z_cut + mu_cut - (h(R)-h(R_cut)) - mu(R,theta).
            # The whole nonrotating mean is preserved, including mu_cut.
            difference[0] += delta_mu_cut
        current = difference
        for radial in range(3):
            coefficient_bound = bernstein_abs(current)
            for angular in range(3 - radial):
                bounds[radial, angular] += abs(key[1]) ** angular * coefficient_bound
            current = derivative(current, width)
    if low == 0:
        if any(bounds[key] != 0 for key in MULTI_INDICES if key != (0, 0)):
            raise ValueError("A nonconstant angular map reaches the polar center")
        first_squared = second_squared = Q(0)
    else:
        # Euclidean disk polar frame, for the Cartesian vector-valued difference.
        first_squared = bounds[1, 0] ** 2 + (bounds[0, 1] / low) ** 2
        mixed = bounds[1, 1] / low + bounds[0, 1] / low ** 2
        angular_second = bounds[0, 2] / low ** 2 + bounds[1, 0] / low
        second_squared = bounds[2, 0] ** 2 + 2 * mixed ** 2 + angular_second ** 2
    return bounds, first_squared, second_squared


def validate_actual_source(path, api):
    provisional = read(path)
    if provisional.get("model_kind") not in ACTUAL_KINDS:
        raise ValueError("Only an actual original nonlinear-DN field or its explicit refinement is allowed")
    record = api.accepted_input(path, repo=REPO)
    if (record.get("model_kind") not in ACTUAL_KINDS
            or record["warm_definition"]["homotopy"] != 1
            or record["mean_nodes"] != 1168):
        raise ValueError("A real lambda-one original finite-mean field is required")
    return record


class CompleteTail:
    """One source-bound full finite chain plus its own exact deep collar."""
    def __init__(self, source_path, source, summary_path):
        self.source_path, self.source = Path(source_path), source
        self.summary_path = Path(summary_path)
        summary = self.summary = read(summary_path)
        if summary.get("status") not in (
                "new_whole_tail_disk_metric_curvature_certified",
                "new_selected_tail_geometry_bounds_recorded"):
            raise ValueError("The full actual tail certificate execution did not finish")
        if summary["source"] != ref(HERE / "seam_certify_tail_geometry_v2.py"):
            raise ValueError("The full tail certificate used another mathematical entry")
        verify_ref(summary["source"])
        for item in summary["mathematical_sources"].values():
            verify_ref(item)
        for key in ("geometry_bundle", "constants", "normalization"):
            verify_ref(summary[key])
        bundle, chain, manifest, index, constants = validate_inputs(
            Path(summary["geometry_bundle"]["path"]),
            Path(summary["constants"]["path"]), Path(summary["normalization"]["path"]))
        self.bundle, self.chain, self.manifest = bundle, chain, manifest
        self.index, self.constants = index, constants
        for summary_key, bundle_key in (
                ("accepted_packet", "accepted_packet"),
                ("shared_R_manifest", "shared_R_manifest"),
                ("original_mean_chain", "mean_chain"),
                ("height_identity", "height_identity"),
                ("spectrum", "spectrum"),
                ("spectrum_contract", "spectrum_contract"),
                ("representation_sources", "representation_sources")):
            if summary[summary_key] != bundle[bundle_key]:
                raise ValueError("The certificate chain changed a finite map identity")
        if summary.get("geometry_schema") != GEOMETRY_SCHEMA:
            raise ValueError("The complete map is not the explicit v2 Fourier definition")
        self.S = S = index["finite_stage_count"]
        if (type(S) is not int or S < 1 or len(chain["mean_chain"]) != S + 1
                or summary.get("all_finite_stages_audited") is not True
                or summary.get("finite_tail_to_its_own_deep_disk_C2") is not True
                or index.get("all_stages_exported") is not True
                or index.get("all_finite_stage_adjacencies_verified") is not True):
            raise ValueError("A selected-stage result is not a complete tail disk")
        self.files = {row["stage"]: row for row in manifest["files"]}
        self.proofs = {row["stage"]: row for row in summary["stages"]}
        self.nodes = {row["node"]: row for row in index["unique_boundary_nodes"]}
        if (len(self.files) != len(manifest["files"]) or set(self.files) != set(range(S))
                or len(self.proofs) != len(summary["stages"]) or set(self.proofs) != set(range(S))
                or len(self.nodes) != len(index["unique_boundary_nodes"])
                or set(self.nodes) != set(range(S + 1))
                or index["cut_node"] != self.nodes[0] or index["deep_node"] != self.nodes[S]):
            raise ValueError("The complete canonical stage/node/proof chain is missing or duplicated")
        packet_ref = bundle["accepted_packet"]
        final = source["result"]
        if (packet_ref != ref(final["full_height_record"])
                or packet_ref["sha256"] != source["tail_seam"]["tail_packet_sha256"]
                or bundle["source_port"]["sha256"] != source["linear_port_sha256"]
                or bundle["finite_scope"]["M"] != source["modes"]):
            raise ValueError("The complete tail does not belong to the final actual prefix")
        identity = bundle["height_identity"]
        if (identity["factor"] != 1 or identity["original_arithmetic"] != "numpy"
                or identity["reference_key"] != "candidate_H"
                or identity["reference"] != ref(final["height_reference"])):
            raise ValueError("A scaled warm tail is not the actual complete-H tail")
        target = checked(identity["reference"])
        if (target["physical_sha256"] != source["physical_sha256"]
                or target["raw_sha256"] != source["raw_return"]["sha256"]
                or target["candidate_H"] != source["candidate_H"]):
            raise ValueError("The full-height target belongs to another actual field")
        packet = checked(packet_ref)
        native = checked(bundle["native_record"])
        if not state_match(bundle["native_record"]["path"], packet):
            raise ValueError("The native representation does not use these complete accepted states")
        protocol = bundle["native_protocol_identity"]
        if protocol["status"] != "actual_native_scope_metric_abi_and_payload_cross_checked":
            raise ValueError("The source-bound original native protocol was not checked")
        for key in ("metadata", "manifest", "input", "output"):
            native_key = "static_metadata" if key == "metadata" else key
            if protocol[key] != native[native_key]:
                raise ValueError("The saved native protocol identity changed")
            verify_ref(native[native_key])
        self.outer = fq(constants["parameters"]["rCut"])
        if self.outer != Q(self.nodes[0]["R_exact_binary"]):
            raise ValueError("The full disk does not end at its actual physical cut")
        self.mu_cut = Q(self.nodes[0]["mean_perturbation_exact_binary"])
        if self.mu_cut != fq(chain["mean_chain"][0][0]):
            raise ValueError("The full nonrotating cut mean changed")
        self.spectrum = bundle["spectrum"]
        self.keys = tuple([("planar", m) for m in self.spectrum["planar_modes"]] +
                          [("height", m) for m in self.spectrum["height_modes"]])
        deep_small = summary.get("deep_collar")
        if not deep_small:
            raise ValueError("The actual deepest-node collar certificate is missing")
        deep = self.deep = checked(deep_small["certificate"])
        if {k: v for k, v in deep_small.items() if k != "certificate"} != deep:
            raise ValueError("The deep certificate projection changed")
        if (deep["source"] != summary["source"] or deep["stage_data"] != self.files[S - 1]
                or deep["source_stage"] != S - 1 or deep["canonical_deep_node"] != S
                or deep["canonical_deep_value_sha256"] != self.nodes[S]["value_sha256"]
                or deep["true_background_definition_sha256"] != DEFINITION_SHA
                or deep["geometry_schema"] != GEOMETRY_SCHEMA
                or deep["spectrum_contract"] != bundle["spectrum_contract"]
                or deep["C2_outer_match_exact"] is not True
                or deep["C2_inner_zero_two_jet_exact"] is not True
                or deep["upper_height_sign"] != -1
                or deep["right_Hermite_basis_exact"] != [[str(v) for v in row] for row in H]):
            raise ValueError("The actual complete collar definition changed")
        self.R0 = Q(deep["outer_R_exact"])
        self.cuff = fq(constants["parameters"]["rCuff"])
        self.Ri, self.L = (self.R0 + self.cuff) / 2, (self.R0 - self.cuff) / 2
        if (self.R0 != Q(self.nodes[S]["R_exact_binary"])
                or Q(deep["inner_R_exact"]) != self.Ri
                or Q(deep["collar_width_exact"]) != self.L
                or Q(deep["cuff_R_exact"]) != self.cuff
                or not 0 < self.cuff < self.Ri < self.R0 < self.outer):
            raise ValueError("The actual collar radius partition changed")
        self.completed_stages = 0
        self.completed_native_spans = 0

    def stage(self, index):
        entry, small = self.files[index], self.proofs[index]
        data, proof = checked(entry), checked(small["certificate"])
        validate_spectrum_container(data, self.spectrum, stage=True)
        projection = {k: v for k, v in proof.items()
                      if k not in ("rows", "background_cover", "mean_definition")}
        if projection != {k: v for k, v in small.items() if k != "certificate"}:
            raise ValueError("A stage certificate projection changed")
        if (data["stage"] != index or data["spectrumContract"] != self.bundle["spectrum_contract"]
                or data["sharing"]["mapHash"] != entry["mapHash"]
                or data["boundInput"] != self.bundle["mean_chain"]
                or data["status"] != "literal_R_stage_with_exact_common_boundary_two_jets"
                or proof["data"] != entry or proof["stage"] != index
                or proof["map_hash"] != entry["mapHash"]
                or proof["spans"] != len(data["nodes"]) - 1
                or len(proof["rows"]) != len(data["nodes"]) - 1):
            raise ValueError("A complete stage map/continuous-proof identity changed")
        if not all(data["physicalParameters"].get(k) == v
                   for k, v in self.constants["parameters"].items()):
            raise ValueError("A stage uses a different actual background")
        for j, row in enumerate(proof["rows"]):
            radii = [str(fq(data["nodes"][i]["radiusJS"])) for i in (j, j + 1)]
            if row["span"] != j or row["R_exact"] != radii:
                raise ValueError("A continuous stage proof omitted or changed a radial interval")
        P = len(self.spectrum["planar_modes"])
        for canonical, local in ((index + 1, 0), (index, len(data["nodes"]) - 1)):
            node, binding = data["nodes"][local], self.nodes[canonical]
            value = {"radius": node["radiusJS"], "coefficients": node["coefficients"]}
            if (node["canonicalNode"] != canonical
                    or canonical_sha(value) != binding["value_sha256"]
                    or fq(node["radiusJS"]) != Q(binding["R_exact_binary"])
                    or node["coefficients"][0][P] != node["meanPerturbation"]
                    or [node["meanPerturbation"], node["meanBackground"]] != self.chain["mean_chain"][canonical]):
                raise ValueError("A canonical common two-jet or original mean changed")
        return data

    def spans(self):
        data = self.stage(self.S - 1)
        node = data["nodes"][0]
        if (data["rawCell"] != 7 or data["rawSegment"] != 0 or data["rawLeft"] != 0
                or node["meanPerturbation"] != 0 or node["meanBackground"] != 0):
            raise ValueError("The own deep collar does not use its original zero mean anchor")
        yield Span(Q(0), self.Ri, {}, {"kind": "inner_rotational_disk"})
        collar = {}
        for index, key in enumerate(self.keys):
            sign = 1 if key[0] == "planar" else -1
            jet = [sign * fq(row[index]) for row in node["coefficients"]]
            collar[key] = [sum((self.L ** j * jet[j] * H[j][k]
                               for j in range(3)), Q(0)) for k in range(6)]
        yield Span(self.Ri, self.R0, collar, {"kind": "own_deep_C2_collar"})
        del collar
        previous_endpoint = self.R0
        for stage_index in reversed(range(self.S)):
            if stage_index != self.S - 1:
                data = self.stage(stage_index)
            if fq(data["nodes"][0]["radiusJS"]) != previous_endpoint:
                raise ValueError("The complete canonical stage sequence has a radial gap")
            for index, (left, right) in enumerate(zip(data["nodes"], data["nodes"][1:])):
                r0, r1 = fq(left["radiusJS"]), fq(right["radiusJS"])
                polys = {}
                for j, key in enumerate(self.keys):
                    sign = 1 if key[0] == "planar" else -1
                    lv = [sign * fq(row[j]) for row in left["coefficients"]]
                    rv = [sign * fq(row[j]) for row in right["coefficients"]]
                    polys[key] = hermite(lv, rv, r1 - r0)
                yield Span(r0, r1, polys, {"kind": "finite_shared_R_stage",
                                          "stage": stage_index, "span": index,
                                          "map_hash": self.files[stage_index]["mapHash"]})
                self.completed_native_spans += 1
            previous_endpoint = fq(data["nodes"][-1]["radiusJS"])
            self.completed_stages += 1
        if previous_endpoint != self.outer:
            raise ValueError("The complete finite stage chain does not reach its actual cut")

    def identity(self):
        return dict(source_run=ref(self.source_path), model_kind=self.source["model_kind"],
            physical_sha256=self.source["physical_sha256"],
            tail_certificate_summary=ref(self.summary_path),
            geometry_bundle=self.summary["geometry_bundle"], accepted_packet=self.bundle["accepted_packet"],
            shared_R_manifest=self.bundle["shared_R_manifest"],
            original_mean_chain=self.bundle["mean_chain"],
            canonical_node_index=self.bundle["canonical_node_index"],
            spectrum_contract=self.bundle["spectrum_contract"], spectrum=self.spectrum,
            finite_stage_count=self.S, own_collar_R_exact=[str(self.Ri), str(self.R0)],
            original_mu_cut_exact=str(self.mu_cut),
            complete_tail_metric_gate_passed=self.summary["complete_tail_disk_metric_gate_passed"],
            complete_tail_curvature_allocation_passed=self.summary["complete_tail_disk_curvature_allocation_passed"])


def cut_height(path, tail):
    record = read(path)
    if (record.get("status") != "actual_true_cut_height_enclosed"
            or record.get("complete") is not True or record.get("mean_nodes") != 1168
            or record.get("model_kind") != tail.source["model_kind"]
            or record.get("homotopy") != 1 or record.get("true_height_anchor_exact") != "0"
            or record["source_run"] != ref(tail.source_path)
            or record["physical"] != ref(tail.source_path.parent / "physical.npz")
            or record["physical"]["sha256"] != tail.source["physical_sha256"]
            or record["gauge_exact"] != str(fq(tail.source["gauge_q"]))
            or record["source"] != ref(HERE / "seam_certify_true_cut_height.py")
            or record.get("partial_integrals_are_not_Z_cut") is not False
            or record.get("same_common_Z_cut_symbol_as_bridge_trace") is not True):
        raise ValueError("Require a complete true height certificate for this same actual source map")
    for key in ("source", "source_run", "physical", "actual_leaf_record",
                "source_model_loader", "core_mean_certificate", "core_mean_intervals"):
        verify_ref(record[key])
    for source, digest in record["helper_sources"].items():
        verify_ref(dict(path=source, sha256=digest))
    core = checked(record["core_mean_certificate"])
    if (core["source_run_sha256"] != sha(tail.source_path)
            or core["physical_sha256"] != tail.source["physical_sha256"]
            or core["arrays"] != record["core_mean_intervals"]):
        raise ValueError("The complete true height source/core interval binding changed")
    interval = record["Z_cut_interval"]
    bounds = [Q(interval["lower_exact"]), Q(interval["upper_exact"])]
    if bounds[0] > bounds[1]:
        raise ValueError("The true cut height interval is reversed")
    return record, bounds


def compare(args):
    started = time.monotonic()
    out = fresh_dir(args.outdir)
    summary_path, spans_path = out / "summary.json", out / "common-spans.jsonl.gz"
    report = dict(status="validating_two_actual_complete_tail_maps", complete=False,
        source=ref(__file__), whole_closed_surface=False, Cauchy_sequence_proved=False,
        source_continuous_Fourier_projection_error_assumed_zero=False,
        new_BVP_or_tail_solver_invoked=False, old_other_field_bounds_reused=False,
        rigid_or_height_alignment_performed=False, exact_cut_seam_corrections_included=False,
        comparison="right minus left in the same physical-R Cartesian disk coordinates")
    write(summary_path, report)
    try:
        api_path = HERE / "warm_actual_dn_refine_model.py"
        api = module("_seam_tail_pair_actual_gate", api_path)
        left_source = validate_actual_source(args.left_source_run, api)
        right_source = validate_actual_source(args.right_source_run, api)
        frozen = api.require_same_problem(REPO, left_source, right_source)
        left = CompleteTail(args.left_source_run, left_source, args.left_tail_certificate)
        right = CompleteTail(args.right_source_run, right_source, args.right_tail_certificate)
        if left.outer != right.outer:
            raise ValueError("The two fixed disks have different outer cuts")
        background_keys = ("parameters", "cells", "checkpoint_sha256", "factory_sha256")
        if any(left.constants[key] != right.constants[key] for key in background_keys):
            raise ValueError("The backgrounds are different; symbolic cancellation is not available")
        height_difference = None
        heights = None
        if bool(args.left_cut_height) != bool(args.right_cut_height):
            raise ValueError("Supply both actual true cut height certificates or neither")
        if args.left_cut_height:
            lh, lb = cut_height(args.left_cut_height, left)
            rh, rb = cut_height(args.right_cut_height, right)
            if lh["explicit_map_definition"] != rh["explicit_map_definition"]:
                raise ValueError("The true heights use different continuous map interpretations")
            height_difference = [rb[0] - lb[1], rb[1] - lb[0]]
            heights = dict(left=ref(args.left_cut_height), right=ref(args.right_cut_height),
                Delta_Z_cut_interval_exact=list(map(str, height_difference)),
                method="Subtract complete true intervals with their original zero anchors; no midpoint or alignment.")
        modes = tuple(sorted(set(left.keys) | set(right.keys)))
        delta_mu_cut = right.mu_cut - left.mu_cut
        report.update(status="bounding_exact_common_radius_spans",
            actual_source_acceptance_api=ref(api_path),
            frozen_complete_problem_sha256=canonical_sha(frozen),
            inputs={"left": left.identity(), "right": right.identity()},
            same_true_background_definition_sha256=DEFINITION_SHA,
            identical_background_canceled_symbolically=True,
            domain_R_exact=["0", str(left.outer)],
            exact_mode_union={"planar": [m for kind, m in modes if kind == "planar"],
                              "height": [m for kind, m in modes if kind == "height"]},
            Delta_original_mu_cut_exact=str(delta_mu_cut),
            true_cut_heights=heights,
            exact_height_difference="Delta Z_cut + Delta mu_cut - Delta mu(R,theta); the common true h(R)-h(R_cut) cancels.",
            stage_mean_reset_performed=False,
            finite_projection_scope="Each own saved N/degree declares a finite map; changed N/degree and all added modes are compared here. No estimate to the unprojected continuous source follows.")
        write(summary_path, report)
        maxima = {key: Q(0) for key in MULTI_INDICES}
        first_squared = second_squared = Q(0)
        count, last_update = 0, time.monotonic()
        with gzip.GzipFile(filename=str(spans_path), mode="wb", mtime=0) as zipped:
            with io.TextIOWrapper(zipped, encoding="utf-8") as stream:
                for ordinal, low, high, ls, rs in common_spans(
                        iter(left.spans()), iter(right.spans()), left.outer):
                    bounds, first, second = compare_span(ls, rs, low, high, modes, delta_mu_cut)
                    for key in maxima:
                        maxima[key] = max(maxima[key], bounds[key])
                    first_squared, second_squared = max(first_squared, first), max(second_squared, second)
                    row = dict(common_span=ordinal, R_exact=[str(low), str(high)],
                        left_piece=ls.provenance, right_piece=rs.provenance,
                        derivative_bounds_exact={str(a)+","+str(b): str(value)
                                                 for (a, b), value in bounds.items()},
                        disk_first_Frobenius_squared_upper_exact=str(first),
                        disk_second_Frobenius_squared_upper_exact=str(second))
                    stream.write(json.dumps(row, separators=(",", ":"), allow_nan=False) + "\n")
                    count += 1
                    if time.monotonic() - last_update >= 30:
                        stream.flush()
                        progress = dict(common_spans=count, last_R_exact=str(high),
                            left_complete_stages=left.completed_stages,
                            right_complete_stages=right.completed_stages,
                            seconds=time.monotonic() - started)
                        report.update(progress=progress)
                        write(summary_path, report)
                        print(json.dumps(progress), flush=True)
                        last_update = time.monotonic()
        if left.completed_stages != left.S or right.completed_stages != right.S:
            raise ValueError("The full common partition did not consume both complete tails")
        first, second = sqrt_upper(first_squared), sqrt_upper(second_squared)
        relative_position = maxima[0, 0]
        absolute_position = None if height_difference is None else (
            relative_position + max(map(abs, height_difference)))
        absolute_complete = height_difference is not None
        report.update(status=("two_actual_complete_tail_finite_C2_difference_enclosed" if absolute_complete
                              else "two_actual_tail_derivative_bounds_enclosed_height_constant_unpaid"),
            complete=absolute_complete,
            exact_radial_spectral_comparison_complete=True,
            comparison_complete_for_declared_two_finite_maps=absolute_complete,
            common_spans=count, common_span_certificate=ref(spans_path),
            exact_common_R_partition_consumed_both_complete_maps=True,
            consumed_native_spans={"left": left.completed_native_spans,
                                   "right": right.completed_native_spans},
            derivative_bounds_exact={str(a)+","+str(b): str(value)
                                     for (a, b), value in maxima.items()},
            position_difference_relative_to_Delta_Z_cut=upper_row(relative_position),
            disk_first_derivative_operator_upper=upper_row(first),
            disk_second_derivative_bilinear_upper=upper_row(second),
            Euclidean_disk_C1_C2_norm_convention="Vector Euclidean norm; operator and bilinear second derivative bounded by their full Cartesian Frobenius norms.",
            absolute_Delta_Z_cut_bounded=height_difference is not None,
            absolute_position_difference_upper=(None if absolute_position is None
                                                else upper_row(absolute_position)),
            absolute_C2_norm_upper=(None if absolute_position is None else
                                    upper_row(max(absolute_position, first, second))),
            outstanding_height_term=(None if height_difference is not None else
                "The actual Delta Z_cut remains an unpaid constant vector in the position difference; no absolute position or full C2 norm is claimed."),
            finite_pair_not_Cauchy_proof=True,
            seconds=time.monotonic() - started)
        write(summary_path, report)
        return report
    except Exception as exc:
        report.update(status="failed", complete=False, error=repr(exc),
                      seconds=time.monotonic() - started)
        if spans_path.exists():
            report["partial_span_certificate"] = ref(spans_path)
        write(summary_path, report)
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("left-source-run", "right-source-run", "left-tail-certificate",
                 "right-tail-certificate", "outdir"):
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--left-cut-height", type=Path)
    parser.add_argument("--right-cut-height", type=Path)
    args = parser.parse_args()
    result = compare(args)
    print(json.dumps({key: result[key] for key in (
        "status", "complete", "common_spans", "absolute_Delta_Z_cut_bounded",
        "position_difference_relative_to_Delta_Z_cut", "absolute_position_difference_upper",
        "disk_first_derivative_operator_upper", "disk_second_derivative_bilinear_upper",
        "Cauchy_sequence_proved", "seconds")}), flush=True)


if __name__ == "__main__":
    main()

