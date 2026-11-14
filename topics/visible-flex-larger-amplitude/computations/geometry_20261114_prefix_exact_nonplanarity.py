#!/usr/bin/env python3
"""R254: exact rational nonplanarity witnesses for a complete physical prefix.

This recovered source is a new content identity.  It implements the proved
shared-binary-node Hermite normal form, not bitwise identities of rounded
PPoly coefficients.  It keeps every physical state and the full z0.  The
certificate is prefix-only; it never creates BVP acceptance, a tail
certificate, global embedding, or positive rigid-motion Hausdorff distance.
Run numerical consumption only in this public repository's GitHub Actions.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as Q
import gzip
import hashlib
import json
import os
from pathlib import Path
import sys
import time

for _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_name] = "1"

import numpy as np


HERE = Path(__file__).resolve().parent
SCHEMA = "exact-full-physical-prefix-cell-nonplanarity-v1"
RADIAL = (Q(1, 2), Q(1, 4), Q(3, 4), Q(1, 8), Q(3, 8), Q(5, 8))
CARDINAL = ((Q(1), Q(0)), (Q(0), Q(1)),
            (Q(-1), Q(0)), (Q(0), Q(-1)))


def actions_only():
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Run this finite-field consumer in the public repository's Actions")


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)


def canonical_sha(value):
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"),
                     ensure_ascii=False, allow_nan=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def array_sha(value):
    # Exactly the R249 shared-node identity convention, including shape.
    array = np.asarray(value, dtype="<f8", order="C")
    return hashlib.sha256(str(array.shape).encode("ascii") +
                          b"\0" + array.tobytes()).hexdigest()


def exact(value):
    return Q.from_float(float(value))


def rational_record(value):
    value = Q(value)
    numerator, denominator = value.numerator, value.denominator
    result = dict(numerator_hex=hex(numerator),
                  denominator_hex=hex(denominator),
                  numerator_bits=abs(numerator).bit_length(),
                  denominator_bits=denominator.bit_length())
    if max(abs(numerator).bit_length(), denominator.bit_length()) <= 512:
        result["readable_fraction"] = str(value)
    return result


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), Q(0))


def angle_sequence(M, cosine, sine):
    cosine, sine = Q(cosine), Q(sine)
    if cosine*cosine+sine*sine != 1:
        raise ValueError("Supply an exact rational point of the unit circle")
    c2, s2 = cosine*cosine-sine*sine, 2*cosine*sine
    C, S = [Q(1)], [Q(0)]
    for _ in range(M):
        C.append(c2*C[-1]-s2*S[-1])
        S.append(s2*C[-2]+c2*S[-1])
    return tuple(C), tuple(S)


def hermite_position(left, right, width, unit):
    """Interpolate exact world XYZ endpoint 0/1/2 s jets, not rounded c."""
    width, unit = Q(width), Q(unit)
    if width <= 0 or not 0 < unit < 1:
        raise ValueError("Witnesses must lie in a nonempty open radial cell")
    result = []
    for coordinate in range(3):
        y0, v0, w0 = (left[order][coordinate] for order in range(3))
        y1, v1, w1 = (right[order][coordinate] for order in range(3))
        c0, c1, c2 = y0, width*v0, width*width*w0/2
        A = y1-c0-c1-c2
        B = width*v1-c1-2*c2
        C = width*width*w1-2*c2
        coefficients = (c0, c1, c2, 10*A-4*B+C/2,
                        -15*A+7*B-C, 6*A-3*B+C/2)
        value = Q(0)
        for coefficient in reversed(coefficients):
            value = value*unit+coefficient
        result.append(value)
    return tuple(result)


class NodeAngles:
    """Complete-state synthesis at rational physical circle points."""

    def __init__(self, M, nodal):
        self.M = M
        self.nodal = nodal
        self.angles = {}
        self.values = {}

    def at(self, node, angle):
        angle = tuple(Q(v) for v in angle)
        key = (node, angle)
        if key in self.values:
            return self.values[key]
        if angle not in self.angles:
            self.angles[angle] = angle_sequence(self.M, *angle)
        C, S = self.angles[angle]
        cosine, sine = angle
        M = self.M
        result = []
        for jets in self.nodal:
            row = jets[node]
            R = sum((exact(row[m])*C[m] for m in range(M+1) if C[m]), Q(0))
            T = sum((exact(row[M+m])*S[m] for m in range(1, M+1) if S[m]), Q(0))
            Z = sum((exact(row[2*M+1+m])*C[m] for m in range(M+1) if C[m]), Q(0))
            result.append((cosine*R-sine*T, sine*R+cosine*T, Z))
        self.values[key] = tuple(result)
        return self.values[key]

    def discard_before(self, node):
        self.values = {key: value for key, value in self.values.items()
                       if key[0] >= node}


class AffineWitness:
    """Maintain an exact affine basis of every point encountered."""

    def __init__(self):
        self.points = []
        self.parameters = []
        self.normal = None
        self.determinant = None
        self.samples = 0

    def add(self, point, parameter):
        self.samples += 1
        keep = False
        if not self.points:
            keep = True
        else:
            difference = sub(point, self.points[0])
            if len(self.points) == 1:
                keep = any(difference)
            elif len(self.points) == 2:
                candidate = cross(sub(self.points[1], self.points[0]), difference)
                if any(candidate):
                    self.normal = candidate
                    keep = True
            elif len(self.points) == 3:
                determinant = dot(self.normal, difference)
                if determinant:
                    self.determinant = determinant
                    keep = True
            else:
                raise RuntimeError("Stop a witness search after four independent points")
        if keep:
            self.points.append(point)
            self.parameters.append(copy.deepcopy(parameter))
        return self.determinant is not None

    def record(self):
        result = dict(tested_positions=self.samples,
                      affine_span_dimension=len(self.points)-1,
                      parameters=copy.deepcopy(self.parameters),
                      exact_positions=[[rational_record(v) for v in point]
                                       for point in self.points])
        if self.determinant is not None:
            result["determinant"] = rational_record(self.determinant)
            result["determinant_sign"] = 1 if self.determinant > 0 else -1
        elif self.normal is not None:
            result["containing_plane_normal"] = [rational_record(v) for v in self.normal]
            result["containing_plane_offset"] = rational_record(dot(self.normal, self.points[0]))
        return result


def certify_prefix(saved, *, assembly=None, plan=None, complete_fallback=True):
    """Return summary and exact witnesses for this particular saved instance.

    Reusing an already constructed SavedPrefix avoids regenerating its
    original finite-ODE second nodal jets.  Existing R249 nodal hashes are
    checked when present.  Without those hashes the report explicitly
    limits older-assembly identity to the recorded new nodal instance.
    """
    actions_only()
    started = time.monotonic()
    M, n = int(saved.M), int(saved.n)
    x = np.asarray(saved.quintic.x, dtype=float)
    nodal = tuple(np.asarray(v, dtype=float) for v in saved.quintic.nodal)
    if (M < 1 or n != 3*M+2 or x.ndim != 1 or len(x) < 2 or
            not np.all(np.isfinite(x)) or not np.all(np.diff(x) > 0)):
        raise ValueError("Use every node of a finite complete 3M+2 prefix")
    if not np.array_equal(x, np.asarray(saved.sol.x, dtype=float)):
        raise ValueError("The reader's physical knots and the polynomial knots differ")
    if (len(nodal) != 3 or any(v.shape != (len(x), n) for v in nodal) or
            not all(np.all(np.isfinite(v)) for v in nodal)):
        raise ValueError("All full-state shared value/first/second nodal jets are required")
    record = saved.rec
    if (record.get("success") is not True or record.get("status") != 0 or
            not record.get("actual_tail") or int(record["M"]) != M):
        raise ValueError("This workflow consumes a genuinely accepted complete checkpoint")
    definition = copy.deepcopy(saved.definition)
    normalization = copy.deepcopy(definition.get("inlet_normalization", {"enabled": False}))
    if not isinstance(normalization, dict) or type(normalization.get("enabled")) is not bool:
        raise ValueError("The inlet normalization choice must be an explicit boolean")
    nodal_hashes = [array_sha(v) for v in nodal]
    preexisting_binding = False
    if normalization["enabled"]:
        if normalization.get("normal_form_nodal_jet_sha256") != nodal_hashes:
            raise ValueError("The actual nodal instance does not match the R249 normal form")
        preexisting_binding = True
    for name, bundle in (("assembly", assembly), ("plan", plan)):
        if bundle is not None and bundle.get("large_core_prefix") != definition:
            raise ValueError("The {} must contain this same complete prefix definition".format(name))
    if definition.get("input_sha256") != sha(saved.path):
        raise ValueError("The complete prefix input identity differs from the actual checkpoint")
    reader_module = sys.modules[type(saved).__module__]
    reader_identity = dict(class_name=type(saved).__name__,
                           source_file=Path(reader_module.__file__).name,
                           source_sha256=sha(reader_module.__file__))
    synthesis = NodeAngles(M, nodal)
    witnesses, planar, unresolved, short_cells = [], [], [], []
    for cell in range(len(x)-1):
        left_s, right_s = exact(x[cell]), exact(x[cell+1])
        width = right_s-left_s
        search = AffineWitness()
        tested = set()

        def scan(angles):
            for angle in angles:
                angle = tuple(Q(v) for v in angle)
                left = synthesis.at(cell, angle)
                right = synthesis.at(cell+1, angle)
                for unit in RADIAL:
                    key = (unit, angle)
                    if key in tested:
                        continue
                    tested.add(key)
                    point = hermite_position(left, right, width, unit)
                    parameter = dict(radial_fraction=str(unit),
                                     exact_s=rational_record(left_s+width*unit),
                                     cos_phi=str(angle[0]), sin_phi=str(angle[1]))
                    if search.add(point, parameter):
                        return True
            return False

        success = scan(CARDINAL)
        method = "cardinal-fast-search"
        if not success and complete_fallback:
            L = 2*M+1
            angles = ((Q(1-q*q, 1+q*q), Q(2*q, 1+q*q))
                      for q in range(-L, L+1))
            success = scan(angles)
            method = "complete-six-radial-times-rational-circle-grid"
        item = dict(cell=cell, exact_left=rational_record(left_s),
                    exact_right=rational_record(right_s), search_method=method,
                    witnesses_found=bool(success), **search.record())
        if success:
            witnesses.append(item)
            status = "exact-nonplanar-cell"
        elif complete_fallback:
            planar.append(item)
            status = "exact-planar-cell-by-complete-grid"
        else:
            unresolved.append(item)
            status = "unresolved-cardinal-only-search"
        short_cells.append(dict(cell=cell, status=status,
                                tested_positions=search.samples,
                                affine_span_dimension=len(search.points)-1,
                                search_method=method))
        synthesis.discard_before(cell+1)
        if (cell+1) % 64 == 0 or cell+1 == len(x)-1:
            print(json.dumps(dict(event="R254-progress", completed_cells=cell+1,
                                  total_cells=len(x)-1, nonplanar_cells=len(witnesses),
                                  exact_planar_cells=len(planar), unresolved_cells=len(unresolved),
                                  seconds=time.monotonic()-started)), flush=True)
    complete = len(witnesses) == len(x)-1
    scalar = record["fixed_scalar_profile"]["geometry"]
    report = dict(
        schema=SCHEMA,
        theorem="R254",
        scope="The exact shared-binary-node complete physical Hermite prefix; no claim about a nonlinear limit or a complete closed surface",
        source_sha256=sha(__file__),
        recovery_identity="Reconstructed small-text source after execution-environment loss; this source SHA is its new identity",
        actual_checkpoint_sha256=sha(saved.path),
        complete_prefix_definition=definition,
        reader_identity=reader_identity,
        actual_field_modes=M,
        physical_state_dimension=n,
        physical_nodes=len(x),
        physical_cells=len(x)-1,
        physical_knots_array_sha256=array_sha(x),
        complete_shared_nodal_jet_sha256=nodal_hashes,
        inlet_normalization=normalization,
        preexisting_R249_nodal_byte_binding_verified=preexisting_binding,
        exact_object="Unique real quintic through all exact binary-rational shared state jets, synthesized in the full rotating physical-phi layout including z0",
        full_scalar_specification_sha256=canonical_sha(scalar),
        finite_boundary_scheme=copy.deepcopy(record.get("finite_boundary_scheme",
                                                       "not separately labeled in source checkpoint")),
        original_checkpoint_unchanged=True,
        field_modified_by_this_consumer=False,
        old_mean_added=False,
        all_physical_modes_and_full_z0_retained=True,
        rounded_polynomial_coefficients_used=False,
        material_angle_inverse_used=False,
        floating_trigonometric_evaluations_used=False,
        witnesses_in_pre_registration_coordinates=True,
        recorded_global_registration=copy.deepcopy(assembly.get("single_global_planar_registration")) if assembly is not None else None,
        original_assembly_prefix_definition_matched=assembly is not None,
        same_assembly_nodal_byte_binding_verified=assembly is not None and preexisting_binding,
        without_preexisting_node_hashes_scope="This report binds the specific newly recorded nodal instance; old DDY or rounded-renderer byte identity is not inferred from a shared checkpoint",
        search=dict(radial_fractions=[str(v) for v in RADIAL],
                    cardinal_angles=[list(map(str, angle)) for angle in CARDINAL],
                    complete_fallback_enabled=bool(complete_fallback),
                    maximum_world_trigonometric_degree=2*M+1,
                    complete_grid_circle_points=4*M+3,
                    complete_grid_positions=6*(4*M+3),
                    complete_circle_formula="q=-L..L, L=2M+1; cos=(1-q^2)/(1+q^2), sin=2q/(1+q^2)",
                    nonzero_test="Exact Fraction determinant, with no floating threshold"),
        all_cells_have_exact_nonzero_four_point_witness=complete,
        prefix_no_planar_parameter_open_piece_proved=complete,
        whole_prefix_including_finite_radial_seams_covered=complete,
        conditional_phase_transfer="R248 phase rotation/material shift, a fixed invertible affine registration or reflection, and an independently certified material-circle diffeomorphism preserve this property",
        cells=short_cells,
        exact_planar_cell_indices=[v["cell"] for v in planar],
        unresolved_cell_indices=[v["cell"] for v in unresolved],
        elapsed_seconds=time.monotonic()-started,
        original_rounded_renderer_identity_certified=False,
        tail_collar_outer_correction_nonplanarity_certified=False,
        closed_activity_annulus_topology_certified=False,
        global_embedding_or_reach_certified=False,
        exact_nonlinear_limit_nonplanarity_certified=False,
        actual_delta_E_certified=False,
        task_completed=False,
    )
    details = dict(schema=SCHEMA+"-exact-witnesses",
                   source_sha256=sha(__file__),
                   actual_checkpoint_sha256=sha(saved.path),
                   physical_knots_array_sha256=array_sha(x),
                   complete_shared_nodal_jet_sha256=nodal_hashes,
                   rational_encoding="Signed hexadecimal integer numerator / positive hexadecimal integer denominator; recover with int(text,16)",
                   nonplanar_witnesses=witnesses,
                   exact_planar_cells=planar,
                   unresolved_cells=unresolved)
    return report, details


def write_outputs(path, report, details):
    """Retain all exact positions/determinants, with bounded legitimate artifacts."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    groups = ("nonplanar_witnesses", "exact_planar_cells", "unresolved_cells")
    rows = []
    for key in groups:
        rows.extend(dict(kind=key, **row) for row in details[key])
    rows.sort(key=lambda row: row["cell"])
    header = {key: value for key, value in details.items() if key not in groups}
    pending, chunks = [rows], []
    while pending:
        part = pending.pop(0)
        payload = dict(header, cells=part)
        raw = json.dumps(payload, sort_keys=True, separators=(",", ":"),
                         ensure_ascii=False, allow_nan=False).encode("utf-8")
        packed = gzip.compress(raw, mtime=0)
        if len(packed) >= 4_000_000 and len(part) > 1:
            middle = len(part)//2
            pending[0:0] = [part[:middle], part[middle:]]
            continue
        if len(packed) >= 5_000_000:
            raise ValueError("A single exact witness exceeds the repository per-file budget")
        target = path.with_name(path.stem+"-witnesses-{:03d}.json.gz".format(len(chunks)))
        target.write_bytes(packed)
        chunks.append(dict(file=target.name, sha256=sha(target), bytes=len(packed),
                           uncompressed_sha256=hashlib.sha256(raw).hexdigest(),
                           first_cell=part[0]["cell"] if part else None,
                           last_cell=part[-1]["cell"] if part else None,
                           cell_count=len(part)))
    report["exact_witness_artifacts"] = chunks
    raw_report = (json.dumps(report, indent=2, ensure_ascii=False, allow_nan=False)+"\n").encode("utf-8")
    if len(raw_report) >= 5_000_000:
        raise ValueError("The summary exceeds the repository per-file budget")
    path.write_bytes(raw_report)
    return report


def main():
    actions_only()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    choice = parser.add_mutually_exclusive_group(required=True)
    choice.add_argument("--assembly", type=Path)
    choice.add_argument("--inlet-normalization", choices=("original", "r249"))
    parser.add_argument("--plan", type=Path)
    parser.add_argument("--cardinal-only", action="store_true",
                        help="An unsuccessful fast search is unresolved, never a planar-cell proof")
    args = parser.parse_args()
    if args.plan is not None and args.assembly is None:
        parser.error("--plan requires the corresponding --assembly")
    assembly = read(args.assembly) if args.assembly is not None else None
    plan = read(args.plan) if args.plan is not None else None
    if assembly is not None:
        normalization = assembly["large_core_prefix"].get("inlet_normalization", {"enabled": False})
        if type(normalization.get("enabled")) is not bool:
            raise ValueError("The assembly must explicitly identify its inlet normal form")
        normalize = normalization["enabled"]
    else:
        normalize = args.inlet_normalization == "r249"
    if plan is not None:
        if assembly["inputs"]["plan"]["sha256"] != sha(args.plan):
            raise ValueError("The assembly's exact plan input differs")
        if plan["inputs"]["checkpoint"]["sha256"] != sha(args.checkpoint):
            raise ValueError("The plan's complete checkpoint differs")
    from geometry_20261114_inlet_parity_normal_form import read_saved
    saved = read_saved(args.checkpoint, normalize=normalize)
    report, details = certify_prefix(saved, assembly=assembly, plan=plan,
                                     complete_fallback=not args.cardinal_only)
    report["input_files"] = {
        "checkpoint": dict(file=str(args.checkpoint), sha256=sha(args.checkpoint))}
    for name, path in (("assembly", args.assembly), ("plan", args.plan)):
        if path is not None:
            report["input_files"][name] = dict(file=str(path), sha256=sha(path))
    write_outputs(args.out, report, details)
    passed = report["all_cells_have_exact_nonzero_four_point_witness"]
    print(json.dumps(dict(event="R254-complete", all_cells_nonplanar=passed,
                          physical_cells=report["physical_cells"],
                          exact_planar_cells=report["exact_planar_cell_indices"],
                          unresolved_cells=report["unresolved_cell_indices"],
                          elapsed_seconds=report["elapsed_seconds"],
                          output=str(args.out))), flush=True)
    return 0 if passed else 2


if __name__ == "__main__":
    raise SystemExit(main())
