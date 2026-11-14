#!/usr/bin/env python3
"""R258 nonplanarity and R238 inputs from one actual complete closed bundle.

The complete prefix is the R254 shared-node real Hermite field, including
the assembly's explicit R249 choice.  The tail uses THIS actual readout's
full FFT nodal coefficients, then exact shared-node Hermite/collar and the
full-angular outer correction.  It is not the old raw-cardinal R243 field
or an assertion that independently rounded renderer coefficients are C2.

Every current input, original tail source, mean/gauge and recorded SE2 is
bound by the existing complete-field loader.  Only the declared angle's
exact cos/sin in the mixed outer correction needs Arb; unpatched pieces
are rational.  A nonzero determinant proves a whole open radial piece,
not merely four sampled positions.  Global embedding, common background
C2, representation-error envelopes and continuous image change remain
separate inputs.  No new BVP, nonlinear tail or radial ODE is solved.
"""
from __future__ import annotations

import os
for _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_name] = "1"

import argparse
from fractions import Fraction as Q
from functools import lru_cache
import gzip
import hashlib
import json
from pathlib import Path
import time

import numpy as np
from flint import arb, ctx, fmpq

from geometry_20261114_full_state_continuous_cover import load_full_bundle
from geometry_20261114_prefix_exact_nonplanarity import (
    actions_only, array_sha, canonical_sha, certify_prefix, read, sha,
    NodeAngles, CARDINAL, rational_record, write_outputs)
from geometry_20261114_planar_germ_coefficients import markers
from geometry_20261114_cardinal_tail_exact_check import (
    hermite, evaluate, det, matrix_add, matrix_sub, zeros)


HERE = Path(__file__).resolve().parent
SCHEMA = "R258-actual-full-state-planar-germ-inputs-v1"
FROZEN_SOURCES = {
    "geometry_20261114_full_state_continuous_cover.py":
        "c39012655f36f652bacdbc39087c6934f03e6fde721830785fb0636930ceabe6",
    "geometry_20261114_large_core_closed_assembly.py":
        "e70d27a92bf153e49e50016706db854b339d96d3414d7f4c00a5993e1f7609c0",
    "exact_20261114_refined_tail_adapter.py":
        "6b06db6c7c96078b9fabe403a0b3ade14f8b30b07a78b565ed299c77f840d937",
}
B = ((Q(-1), Q(1), Q(0)), (Q(-2), Q(0), Q(0)),
     (Q(-1), Q(-1), Q(0)))
FRACTIONS = (Q(0), Q(1), Q(1, 2), *(Q(j, 15) for j in range(1, 15)))


def exact(value):
    if isinstance(value, Q):
        return value
    if isinstance(value, (int, np.integer)):
        return Q(int(value))
    n, d = value.as_integer_ratio()
    return Q(int(n), int(d))


def ball(value):
    value = exact(value)
    return arb(fmpq(value.numerator, value.denominator))


def enclosure(value):
    if not value.is_finite():
        return dict(finite=False, enclosure=str(value))
    return dict(finite=True, lower=str(value.lower().fmpq()),
                upper=str(value.upper().fmpq()), enclosure=value.str(40))


def encode_matrix(value):
    return [[rational_record(x) for x in row] for row in value]


def scale_matrix(value, factor):
    return [[factor*x for x in row] for row in value]


def write(path, record):
    raw = (json.dumps(record, sort_keys=True, ensure_ascii=False,
        indent=2, allow_nan=False)+"\n").encode()
    if len(raw) >= 1_000_000 and not str(path).endswith(".gz"):
        raise ValueError("Write a large summary with an explicit .gz name")
    if str(path).endswith(".gz"):
        raw = gzip.compress(raw, mtime=0)
    with Path(path).open("xb") as stream:
        stream.write(raw)


def write_rows(output, stem, rows, header):
    """Actual reconstructible evidence, gzip chunks below the Git file limit."""
    pending, artifacts = [rows], []
    while pending:
        part = pending.pop(0)
        raw = (json.dumps(dict(**header, rows=part), sort_keys=True,
            ensure_ascii=False, separators=(",", ":"), allow_nan=False)+"\n").encode()
        encoded = gzip.compress(raw, mtime=0)
        if len(encoded) >= 4_000_000 and len(part) > 1:
            middle = len(part)//2
            pending[0:0] = [part[:middle], part[middle:]]
            continue
        if len(encoded) >= 5_000_000:
            raise ValueError("One complete proof row exceeds the per-file repository budget")
        path = output / (stem+f"-{len(artifacts):03d}.json.gz")
        with path.open("xb") as stream:
            stream.write(encoded)
        artifacts.append(dict(file=path.name, sha256=sha(path), bytes=len(encoded),
            raw_sha256=hashlib.sha256(raw).hexdigest(), rows=len(part)))
    return artifacts


def cardinal_differences(coefficients):
    """Exact j*pi/2 minus angle-zero values of every actual FFT mode.

    For each Cartesian component only five sums over residue classes mod 4
    are needed.  This is algebraic grouping, not a low-frequency projection.
    Zero-frequency translations and k divisible by 4 cancel in these four
    particular angle differences; all coefficients remain hash-bound.
    """
    c = np.asarray(coefficients)
    if c.ndim != 2 or c.shape[1] != 3:
        raise ValueError("Keep the full Cartesian complex Fourier coefficient array")
    result = zeros()
    for component in range(3):
        odd = sum((exact(v.real) for v in c[1::2, component]), Q(0))
        even_two = sum((exact(v.real) for v in c[2::4, component]), Q(0))
        imaginary = (sum((exact(v.imag) for v in c[1::4, component]), Q(0))
            - sum((exact(v.imag) for v in c[3::4, component]), Q(0)))
        result[0][component] = -odd-2*even_two-imaginary
        result[1][component] = -2*odd
        result[2][component] = -odd-2*even_two+imaginary
    return result


class ActualFFTNodes:
    """The complete actual node coefficients, with bounded numeric caching."""
    def __init__(self, assembly):
        self.tail = assembly.tail
        self.radii = tuple(exact(r) for r in self.tail.r)
        self.sigma = exact(assembly.sigma)
        self.records = {}
        if self.sigma != -1 or any(a >= b for a, b in zip(self.radii, self.radii[1:])):
            raise ValueError("Use this actual reflected positive-r finite tail")

    @lru_cache(maxsize=12)
    def jets(self, index):
        generated = np.asarray(self.tail.node_coefficients(index))
        expected = (3, self.tail.N//2+1, 3)
        if generated.shape != expected or not np.all(np.isfinite(generated)):
            raise ValueError("The actual readout lost a node, derivative or Fourier mode")
        # fourier() produces binary64 complex amplitudes and only widens
        # them.  Check this identity instead of losing longdouble bits.
        binary = np.asarray(generated, dtype="<c16", order="C")
        if not np.array_equal(np.asarray(binary, dtype=np.clongdouble), generated):
            raise ValueError("The source acquired non-binary64 Fourier data; update the exact encoding explicitly")
        descriptor = str(binary.shape).encode("ascii")+b"\0"
        coefficient_sha = hashlib.sha256(descriptor+binary.tobytes()).hexdigest()
        if index in self.records and self.records[index]["complete_FFT_node_coefficients_sha256"] != coefficient_sha:
            raise ValueError("Re-evaluation changed the same actual Fourier node")
        out = []
        # Consume the original generated values, not the encoding cast.
        # exact() calls each actual scalar's as_integer_ratio directly.
        for derivative, coefficients in enumerate(generated):
            value = cardinal_differences(coefficients)
            factor = self.radii[index] if derivative == 0 else Q(1) if derivative == 1 else Q(0)
            for j in range(3):
                value[j][2] *= self.sigma
                for coordinate in range(3):
                    value[j][coordinate] += factor*B[j][coordinate]
            out.append(value)
        row = self.tail.rows[index]
        self.records[index] = dict(index=index, exact_radius=rational_record(self.radii[index]),
            original_readout_node_file=row["file"], original_compressed_node_sha256=row["sha256"],
            original_raw_node_sha256=row["rawSha256"],
            complete_FFT_node_coefficients_sha256=coefficient_sha,
            complete_FFT_node_coefficients_shape=list(expected),
            actual_FFT_node_dtype=str(generated.dtype),
            complex128_portable_encoding_exact_round_trip_verified=True,
            exact_scalar_extraction="Original scalar.as_integer_ratio(); no Python float conversion",
            complete_FFT_hash_encoding="str(shape).encode('ascii') + NUL + little-endian complex128 C-order bytes",
            full_radial_cardinal_difference_jets=[encode_matrix(value) for value in out])
        return tuple(out)


def prefix_cut_terms(saved, assembly):
    """Exact complete cut jets, with the producer's declared real rotation.

    The return is three rational matrices of jets: constant, cos(beta),
    sin(beta).  Only angle differences are used, so no physical mean or
    translation is approximated or removed from the represented surface.
    """
    M = int(saved.M)
    if exact(saved.quintic.x[-1]) != exact(assembly.L):
        raise ValueError("The actual complete cut must be its shared terminal node")
    if exact(saved.rho_lower_exact) <= 0:
        raise ValueError("The complete material map needs its existing global positive certificate")
    nodal = tuple(np.asarray(value) for value in saved.quintic.nodal)
    if any(value.dtype.kind != "f" or value.dtype.itemsize != 8 for value in nodal):
        raise ValueError("R254 NodeAngles is the actual binary64 physical-node API; do not silently cast a new dtype")
    synthesis = NodeAngles(M, nodal)
    values = [synthesis.at(len(saved.quintic.x)-1, angle) for angle in CARDINAL]
    differences = [[[values[j+1][derivative][k]-values[0][derivative][k]
        for k in range(3)] for j in range(3)] for derivative in range(3)]
    v, second = exact(assembly.ap), exact(assembly.app)
    if v >= 0:
        raise ValueError("Retain the actual negative cut radial orientation")
    radial = [differences[0], scale_matrix(differences[1], 1/v),
        matrix_sub(scale_matrix(differences[2], 1/(v*v)),
                   scale_matrix(differences[1], second/(v*v*v)))]
    terms = [[zeros() for _ in range(3)] for _ in range(3)]
    for derivative in range(3):
        for j in range(3):
            x, y, z = radial[derivative][j]
            terms[0][derivative][j][2] = z
            terms[1][derivative][j][0] = x
            terms[1][derivative][j][1] = y
            terms[2][derivative][j][0] = y
            terms[2][derivative][j][1] = -x
    registration = saved.registration
    beta = exact(registration["rotation_angle"])
    return terms, beta, dict(
        complete_shared_nodal_jet_sha256=[array_sha(v) for v in nodal],
        exact_terminal_s=rational_record(exact(assembly.L)),
        exact_cut_r_s=rational_record(v), exact_cut_r_ss=rational_record(second),
        exact_registration_angle=rational_record(beta),
        rotation_definition="Exact cos/sin of the producer's recorded angle; printed matrix not reinterpreted as exact SO2",
        complete_material_density_lower=str(saved.rho_lower_exact),
        material_inverse_at_four_cardinal_angles="Exactly identity by R258 and global positive rho; no numerical inversion is used in these witnesses",
        all_physical_modes_and_all_three_nodal_jets_retained=True,
        common_z0_and_translation_cancel_only_from_differences=True,
        unregistered_radial_difference_jets=[encode_matrix(value) for value in radial],
        target_constant_cos_sin_jets=[[encode_matrix(value) for value in term] for term in terms])


def prove_tail(assembly, *, precision=160, maximum_precision=2560):
    nodes = ActualFFTNodes(assembly)
    radii = nodes.radii
    cuff, inner, cut, width = (exact(getattr(assembly, key))
                               for key in ("cuff", "inner", "cut", "W"))
    if (not 0 < cuff < inner < cut or not 0 < width < cut-inner
            or radii[0] != inner or radii[-1] != cut):
        raise ValueError("The actual whole collar/tail/patch anchors differ")
    patch_start = cut-width
    target_terms, beta, target_record = prefix_cut_terms(assembly.saved, assembly)
    outer = nodes.jets(len(radii)-1)
    delta_terms = [[matrix_sub(target_terms[0][j], outer[j]) for j in range(3)],
                   target_terms[1], target_terms[2]]
    patches = [hermite(zeros(), values[0], zeros(), values[1], zeros(), values[2], width)
               for values in delta_terms]
    inner_jets = nodes.jets(0)
    collar = hermite(scale_matrix(B, cuff), inner_jets[0], B, inner_jets[1],
                    zeros(), inner_jets[2], inner-cuff)
    witnesses, unresolved, summaries = [], [], []
    started = time.monotonic()
    precisions = [precision]
    while precisions[-1] < maximum_precision:
        precisions.append(min(maximum_precision, 2*precisions[-1]))
    trig = {}

    def sign_at(radius, origin, span_width, coefficients, patched):
        base = evaluate(coefficients, (radius-origin)/span_width)
        if not patched:
            value = det(base)
            return (dict(kind="exact-rational", determinant=rational_record(value),
                         determinant_sign=1 if value > 0 else -1 if value < 0 else 0)
                    if value else None)
        t = (radius-patch_start)/width
        if not 0 <= t <= 1:
            raise ValueError("A split patch witness left its exact Hermite interval")
        constant = matrix_add(base, evaluate(patches[0], t))
        cosine, sine = evaluate(patches[1], t), evaluate(patches[2], t)
        for bits in precisions:
            ctx.prec = bits
            if bits not in trig:
                angle = ball(beta)
                trig[bits] = angle.cos(), angle.sin()
            co, si = trig[bits]
            matrix = [[ball(constant[j][k])+co*ball(cosine[j][k])+si*ball(sine[j][k])
                for k in range(3)] for j in range(3)]
            value = det(matrix)
            if value.is_finite() and (value.lower() > 0 or value.upper() < 0):
                return dict(kind="rigorous-Arb-real-rotation", precision_bits=bits,
                    determinant_sign=1 if value.lower() > 0 else -1,
                    determinant_enclosure=enclosure(value),
                    exact_matrix_constant=encode_matrix(constant),
                    exact_matrix_cosine=encode_matrix(cosine),
                    exact_matrix_sine=encode_matrix(sine),
                    cosine_enclosure=enclosure(co), sine_enclosure=enclosure(si))
        return None

    def piece(label, lo, hi, origin, span_width, coefficients):
        if not lo < hi:
            raise ValueError("A nonempty radial proof piece is required")
        # Pieces have already been split at the exact start.  At the start
        # itself all patch terms vanish, so either branch agrees exactly.
        patched = lo >= patch_start
        proof = None
        for fraction in FRACTIONS:
            radius = lo+(hi-lo)*fraction
            proof = sign_at(radius, origin, span_width, coefficients, patched)
            if proof is not None:
                break
        item = dict(piece=label, exact_left=rational_record(lo), exact_right=rational_record(hi),
            outer_patch_active=patched, determinant_polynomial_degree_at_most=15)
        if proof is not None:
            item.update(exact_witness_radius=rational_record(radius),
                witness_relative_position=str(fraction), **proof)
            witnesses.append(item)
        else:
            item.update(reason=("All exact rational four-cardinal determinant values vanished; this does not prove the whole surface planar."
                if not patched else
                "No attempted exact point/Arb precision excluded zero; zero polynomial or planarity is not inferred."),
                attempted_relative_positions=list(map(str, FRACTIONS)),
                attempted_Arb_precisions=precisions if patched else [])
            unresolved.append(item)
        summaries.append(dict(piece=label, proved_nonplanar=proof is not None,
            outer_patch_active=patched, exact_interval=[str(lo), str(hi)]))

    piece("inner-collar", cuff, inner, cuff, inner-cuff, collar)
    for i in range(len(radii)-1):
        lo, hi = radii[i:i+2]
        left, right = nodes.jets(i), nodes.jets(i+1)
        coefficients = hermite(left[0], right[0], left[1], right[1], left[2], right[2], hi-lo)
        edges = [lo]+([patch_start] if lo < patch_start < hi else [])+[hi]
        for part, (a, b) in enumerate(zip(edges, edges[1:])):
            piece(f"tail-{i}-part-{part}", a, b, lo, hi-lo, coefficients)
        if (i+1) % 256 == 0 or i+1 == len(radii)-1:
            print(json.dumps(dict(event="R258-own-tail", completed_spans=i+1,
                total_spans=len(radii)-1, unresolved=len(unresolved),
                seconds=time.monotonic()-started)), flush=True)
    if len(nodes.records) != len(radii) or len(nodes.tail.verified_nodes) != len(radii):
        raise AssertionError("The entire current tail node set must be read and hash checked")
    producer_start = exact(assembly.cut-assembly.W)
    report = dict(schema="R258-actual-FFT-shared-node-tail-nonplanarity-v1", theorem="R258-A",
        complete_readout_sha256=sha(nodes.tail.path), actual_tail_angular=nodes.tail.N,
        actual_tail_nodes=len(radii), original_nodes_hash_verified=len(nodes.tail.verified_nodes),
        radial_polynomial_pieces=len(summaries), proved_pieces=len(witnesses),
        all_tail_collar_outer_patch_pieces_no_planar_open_set=not unresolved,
        exact_inner_collar_interval=[str(cuff), str(inner)], exact_patch_interval=[str(patch_start), str(cut)],
        source_rounded_patch_start=str(producer_start),
        rounded_minus_exact_patch_start=str(producer_start-patch_start),
        cut_target=target_record, pieces=summaries, unresolved_pieces=unresolved,
        exact_object="Full actual binary64 FFT nodal coefficients with exact shared-node real Hermite; exact-width zero-jet collar and full-angle outer correction to the same complete prefix normal form",
        actual_full_FFT_coefficients_including_Nyquist_consumed=True,
        tail_radial_node_dtype=str(nodes.tail.r.dtype),
        exact_radial_nodes_extracted_from_actual_dtype_without_float_conversion=True,
        complete_node_coefficients_actual_dtype_and_exact_round_trip_checked=True,
        old_raw_cardinal_packet_or_A_tail_consumed=False,
        no_projection_of_complete_material_cut_correction=True,
        only_same_radius_common_translations_cancelled=True,
        exact_rational_unpatched_pieces=True,
        real_rotation_in_outer_patch_enclosed_without_printed_matrix_substitution=True,
        C2_nonround_tail_and_collar_from_shared_nodes=True,
        original_rounded_renderer_identity_certified=False,
        normal_form_versus_renderer_error_envelope_certified=False,
        common_background_C2_or_absolute_mean_seams_certified=False,
        all_phase_nonplanarity_transfer="R248/R258 angular shift and fixed spatial rotation/reflection; no whole-surface rigid-motion assertion",
        exact_nonlinear_limit_nonplanarity_certified=False,
        actual_delta_E_certified=False, elapsed_seconds=time.monotonic()-started)
    details = dict(witnesses=witnesses,
        node_coefficients=[nodes.records[i] for i in range(len(radii))])
    return report, details


def use_prefix_report(path, saved, plan, assembly):
    report = read(path)
    if (report.get("schema") != "exact-full-physical-prefix-cell-nonplanarity-v1"
            or report.get("source_sha256") != sha(HERE/"geometry_20261114_prefix_exact_nonplanarity.py")
            or report.get("actual_checkpoint_sha256") != sha(saved.path)
            or report.get("complete_prefix_definition") != saved.definition
            or report.get("physical_knots_array_sha256") != array_sha(saved.quintic.x)
            or report.get("complete_shared_nodal_jet_sha256") !=
               [array_sha(value) for value in saved.quintic.nodal]
            or plan["large_core_prefix"] != saved.definition
            or assembly["large_core_prefix"] != saved.definition):
        raise ValueError("The existing R254 report does not prove this same complete nodal prefix")
    for item in report["exact_witness_artifacts"]:
        filename = item["file"]
        if Path(filename).name != filename:
            raise ValueError("Use the original local complete witness artifacts")
        witness = Path(path).parent / filename
        if sha(witness) != item["sha256"]:
            raise ValueError("A bound original R254 witness artifact differs")
    return report


def optional_held(path, bindings):
    if path is None:
        return dict(provided=False, actual_continuous_image_change_certified=False)
    report = read(path)
    if report.get("schema") != "actual-complete-full-state-held-Hausdorff-cover-witness-v1":
        raise ValueError("Use the own-full-field held consumer, not an old-A or point-cloud result")
    source_binding = report["full_state_input_binding"]["complete_field_binding"]
    if source_binding != bindings:
        raise ValueError("The held report and current complete closed bundle differ")
    return dict(provided=True, report_sha256=sha(path),
        bound_conditional_image_change=report["genuine_image_change_conditionally_established"],
        reported_delta_hold_lower=report["delta_hold_lower"],
        actual_continuous_image_change_certified=False,
        unpaid="Its continuous envelopes and this precise shared-node normal-form identity/representation error must still be proved; a conditional numerical report is not promoted here.")


def main():
    actions_only()
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("directory", "checkpoint", "port", "config", "tail-response", "complete", "source-topic", "out"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--basename", default="surface")
    parser.add_argument("--prefix-report", type=Path)
    parser.add_argument("--held-report", type=Path)
    parser.add_argument("--precision", type=int, default=160)
    parser.add_argument("--max-precision", type=int, default=2560)
    args = parser.parse_args()
    if args.precision < 80 or args.max_precision < args.precision:
        raise ValueError("Use a declared positive Arb precision budget")
    for name, digest in FROZEN_SOURCES.items():
        if sha(HERE/name) != digest:
            raise ValueError("The actual finite construction source changed: "+name)
    output = args.out.resolve()
    output.mkdir(parents=True, exist_ok=True)
    if any(output.iterdir()):
        raise ValueError("Use a fresh complete nonplanarity output directory")
    started = time.monotonic()
    old_precision = ctx.prec
    paths, plan, assembly, background, saved, A, bindings = load_full_bundle(args)
    # R254 hashes and exact NodeAngles deliberately describe its producer's
    # binary64 shared physical nodes.  Reject a future dtype change before
    # that existing API can create an unlabelled binary64 shadow.
    original_prefix_arrays = (np.asarray(saved.quintic.x),
                             *(np.asarray(value) for value in saved.quintic.nodal))
    if any(value.dtype.kind != "f" or value.dtype.itemsize != 8
           for value in original_prefix_arrays):
        raise ValueError("The actual physical shared-node dtype changed; an explicit exact API update is required")
    source_names = [Path(__file__).name, *FROZEN_SOURCES,
        "geometry_20261114_prefix_exact_nonplanarity.py", "geometry_20261114_planar_germ_coefficients.py",
        "geometry_20261114_cardinal_tail_exact_check.py", "geometry_20261114_inlet_parity_normal_form.py",
        "geometry_20261114_large_core_saved_prefix.py", "geometry_20261114_lifted_modes_saved_prefix.py",
        "geometry_20261114_same_metric_saved_prefix.py"]
    intent = dict(schema=SCHEMA+"-intent", source_sha256=sha(__file__),
        consumed_source_sha256={name:sha(HERE/name) for name in source_names},
        complete_field_binding=bindings, input_arguments={key:str(value) if isinstance(value,Path) else value
            for key,value in vars(args).items()}, numpy_version=np.__version__,
        scientific_execution_repository=os.environ.get("GITHUB_REPOSITORY"),
        scientific_execution_commit=os.environ.get("GITHUB_SHA"),
        new_BVP_or_native_tail_solve_requested=False, success_not_predeclared=True)
    write(output/"intent.json", intent)
    try:
        if args.prefix_report:
            prefix = use_prefix_report(args.prefix_report, saved, plan, assembly)
            prefix_evidence = dict(reused_original_report_sha256=sha(args.prefix_report),
                identical_actual_shared_nodes_checked=True, repeated_exact_prefix_search=False)
        else:
            prefix, details = certify_prefix(saved, assembly=assembly, plan=plan)
            prefix = write_outputs(output/"prefix.json", prefix, details)
            prefix_evidence = dict(file="prefix.json", sha256=sha(output/"prefix.json"),
                identical_actual_shared_nodes_checked=True, repeated_exact_prefix_search=False)
        tail, details = prove_tail(A, precision=args.precision, maximum_precision=args.max_precision)
        header = dict(schema=SCHEMA+"-proof-evidence", source_sha256=sha(__file__),
            complete_field_binding=bindings,
            mathematical_object=tail["exact_object"], exact_rotation=tail["cut_target"]["exact_registration_angle"])
        tail["exact_witness_artifacts"] = write_rows(output, "tail-witnesses", details["witnesses"], header)
        tail["actual_FFT_cardinal_node_artifacts"] = write_rows(output, "actual-FFT-nodes", details["node_coefficients"], header)
        tail_path = output/"tail.json.gz"
        write(tail_path, tail)
        marker = markers(paths["plan"], paths["assembly"])
        write(output/"markers.json", marker)
        held = optional_held(args.held_report, bindings)
        prefix_passed = prefix.get("prefix_no_planar_parameter_open_piece_proved") is True
        tail_passed = tail["all_tail_collar_outer_patch_pieces_no_planar_open_set"]
        marker_passed = marker["finite_marker_algebra_passed"]
        normalized = bindings["inlet_normalization"]["enabled"]
        exact_rho = str(saved.rho_lower_exact)
        obligations = dict(
            actual_full_field_and_own_tail_sources_bound=True,
            complete_material_circle_diffeomorphism=dict(proved=True, exact_global_rho_lower=exact_rho),
            complete_prefix_normal_form_no_planar_open_piece=prefix_passed,
            complete_tail_collar_outer_correction_normal_form_no_planar_open_piece=tail_passed,
            all_active_normal_form_parameter_open_pieces_nonplanar=bool(prefix_passed and tail_passed),
            marker_support_radius_center_and_separation_algebra=marker_passed,
            underlying_active_parameter_domain_is_annulus_by_R258=True,
            actual_image_is_embedded_annulus=False,
            shared_nonround_radial_normal_form_C2_proved=True,
            R249_inlet_normal_form_identified=normalized,
            same_exact_common_background_mean_and_all_seams_C2_certified=False,
            previous_rounded_geometry_envelopes_transferred=False,
            global_all_phase_embedding_certified=False,
            actual_continuous_image_change_certified=False,
            all_R238_hypotheses_paid=False)
        summary = dict(schema=SCHEMA, finished=True, scope=__doc__, theorem="R258-A/B and R254/R238",
            source_sha256=sha(__file__), complete_field_binding=bindings,
            prefix_evidence=prefix_evidence,
            tail_evidence=dict(file=tail_path.name,sha256=sha(tail_path),
                radial_pieces=tail["radial_polynomial_pieces"],proved_pieces=tail["proved_pieces"],
                unresolved=len(tail["unresolved_pieces"])),
            marker_evidence=dict(file="markers.json",sha256=sha(output/"markers.json")),
            R238_inputs=obligations, supplied_held_report=held,
            nonplanarity_and_marker_algebra_completed=bool(prefix_passed and tail_passed and marker_passed),
            conditional_conclusion="For this precisely bound normal form, if the remaining common-background/C2/embedding/representation and continuous image-change hypotheses are supplied, R258-B/R238 force strictly positive Euclidean-quotient Hausdorff distance.",
            all_phase_nonplanarity_follows_from_phase_rule_under_R248=True,
            no_quantitative_Euclidean_quotient_lower_bound_created=True,
            no_new_six_jet_machine_accuracy_gate=True,
            actual_delta_E_certified=False, exact_nonlinear_limit_nonplanarity_certified=False,
            task_completed=False, elapsed_seconds=time.monotonic()-started)
        write(output/"summary.json", summary)
        print(json.dumps(dict(event="R258-completed", prefix=prefix_passed,
            own_tail_and_collar=tail_passed, markers=marker_passed,
            actual_delta_E_certified=False, output=str(output))), flush=True)
        return 0 if summary["nonplanarity_and_marker_algebra_completed"] else 2
    finally:
        ctx.prec = old_precision


if __name__ == "__main__":
    raise SystemExit(main())
