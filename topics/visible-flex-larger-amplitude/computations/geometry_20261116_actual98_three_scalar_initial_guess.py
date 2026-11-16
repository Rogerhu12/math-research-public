#!/usr/bin/env python3
"""R578: actual98 prefix input and three returned scalar words as a fresh guess.

No actual228 field, derivative, H, J or response is loaded or reconstructed.
The actual98 archive is verified by the original byte transport. Only its
two complete original warm/status members are selected. During science the
original augmented RHS is evaluated on a new copy of that field with the
three explicitly supplied control rows; no old producer is relabelled.
"""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
import traceback
import zipfile

HERE = Path(__file__).resolve().parent
REPOSITORY = "Rogerhu12/math-research-public"
PREFIX_SCHEMA = "R578-original98-complete-prefix-input-v1"
SEED_SCHEMA = "R578-returned-three-scalar-words-new-initial-guess-v1"
INITIAL_SCHEMA = "R578-original98-field-with-explicit-three-control-initial-guess-v1"
STATUS_SCHEMA = "R578-actual-scalar-initialization-and-fresh-RHS-v1"
READER = "root_20261115_read_existing98_scalar_summary.py"
READER_SHA = "e2e8ec32c30bbc9ff0e77709524ff09f100f0ff5f4decd23c43b6445562b7484"
TRANSPORT = "exact_20261114_fetch_pinned_public_artifact.py"
TRANSPORT_SHA = "51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859"
SOURCE_COMMIT = "918fdb11dbb7a424b6149b405e2c7fab3cc0c737"
PARENT_SCHEMA = "exact-constraint-thirty-one-query-condensed-complete-H-warm-v1"
ARTIFACT = dict(run_id=43677587785, artifact_id=14147700690,
    artifact_name="visible-followup-condensedqp-43677587785-1",
    expected_size=809042943,
    expected_sha256="9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a")
MEMBERS = {
    "warm-001.json.gz": dict(member_suffix="thirty-one-condensed-warm/warm-001.json.gz",
        bytes=4927052, sha256="b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67"),
    "driver-status.json": dict(member_suffix="thirty-one-condensed-warm/driver-status.json",
        bytes=3379453, sha256="b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff"),
}
RUN_KEYS = ("GITHUB_REPOSITORY", "GITHUB_RUN_ID", "GITHUB_RUN_ATTEMPT", "GITHUB_SHA")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            value.update(block)
    return value.hexdigest()


def receipt(path):
    path = Path(path).resolve(strict=True)
    return dict(file=str(path), bytes=path.stat().st_size, sha256=sha(path))


def run_identity():
    return {key: os.environ.get(key) for key in RUN_KEYS}


def require_actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
        "Actual input restoration and initial-RHS evaluation belong to public Actions")


def checked_source(name, expected):
    require(Path(name).name == name, "An explicit source basename")
    path = HERE / name
    require(path.is_file() and not path.is_symlink() and sha(path) == expected,
        "Actual frozen source bytes: " + name)
    return path


def restore_prefix(declaration, output, read, write, current_source_pins):
    """Original whole-archive transport; original member bytes, not summaries.

    The supplied metadata writer must support replacement of this helper's
    own progress record. It never overwrites either original input member.
    """
    require_actions()
    require(isinstance(declaration, dict) and declaration.get("schema") == PREFIX_SCHEMA,
        "The explicit current actual98 prefix input contract")
    require(declaration.get("artifact") == ARTIFACT
        and declaration.get("source_commit") == SOURCE_COMMIT
        and declaration.get("members") == MEMBERS,
        "Exactly the original complete98 artifact and two original members")
    token = os.environ.get("GITHUB_TOKEN")
    require(bool(token), "The original Actions artifact transport requires its read token")
    output = Path(output)
    require(not output.exists(), "One fresh actual98 input directory")
    output.mkdir(mode=0o700)
    record_path = output / "input-receipt.json"
    archive_path = output / "original98.zip"
    state = dict(schema=PREFIX_SCHEMA, run=run_identity(), source=receipt(__file__),
        declaration=copy.deepcopy(declaration), complete=False,
        phase="binding-original-byte-transport", error=None,
        artifact_metadata=None, archive=None, selected_members=[],
        actual_producer_sources={}, original_producer_source_map_identity=None,
        pending_original_producer_sources=None, scientific_evaluation_performed=False,
        original_member_bytes_not_reserialized=True,
        prior_actual228_payload_not_consumed=True,
        original63_input_ancestry_not_relabelled_as_actual98=True,
        current_prefix_acceptance_not_inherited=True,
        archive_removed=False)
    write(record_path, state)
    try:
        path = checked_source(READER, READER_SHA)
        checked_source(TRANSPORT, TRANSPORT_SHA)
        spec = importlib.util.spec_from_file_location("_R578_original98_byte_reader", path)
        reader = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = reader
        spec.loader.exec_module(reader)
        transport = reader.load_transport(HERE / TRANSPORT)
        require(transport.PIN == ARTIFACT, "Original98 transport pin, not an old result substitute")
        state["phase"] = "reading-official-artifact-metadata"
        write(record_path, state)
        opener = transport.make_opener()
        metadata, canonical = transport.read_metadata(opener, token)
        require(metadata["workflow_run"].get("head_sha") == SOURCE_COMMIT,
            "Official original98 artifact source identity")
        state["artifact_metadata"] = metadata
        state["phase"] = "reading-complete-original-archive"
        write(record_path, state)
        downloaded = transport.download_archive(opener, token, canonical, archive_path, {})
        state["archive"] = downloaded
        state["phase"] = "selecting-two-exact-original-members"
        write(record_path, state)
        with zipfile.ZipFile(archive_path, "r") as archive:
            index, count = reader.zip_index(archive, transport)
            state["original_archive_entry_count"] = count
            for name, expected in MEMBERS.items():
                matches = [entry for member, entry in index.items()
                    if member == expected["member_suffix"]
                    or member.endswith("/" + expected["member_suffix"])]
                require(len(matches) == 1, "One exact original input member: " + name)
                member = matches[0]
                require(member.file_size == expected["bytes"], "Original member size: " + name)
                raw = archive.read(member)
                require(len(raw) == expected["bytes"]
                    and hashlib.sha256(raw).hexdigest() == expected["sha256"],
                    "Complete original input member bytes/SHA: " + name)
                target = output / name
                with target.open("xb") as stream:
                    stream.write(raw)
                state["selected_members"].append(dict(actual=receipt(target),
                    original_member=member.filename, original_CRC_checked=True))
                write(record_path, state)
        warm_path, status_path = output / "warm-001.json.gz", output / "driver-status.json"
        warm, status = read(warm_path), read(status_path)
        require(status.get("schema") == PARENT_SCHEMA
            and status.get("accepted_warm_steps") == 1
            and status.get("optimization_progress") is True
            and status.get("success") is False
            and status.get("new_coupled_finite_acceptance") is False
            and status.get("latest_warm_file") == "warm-001.json.gz"
            and status.get("latest_warm_sha256") == MEMBERS["warm-001.json.gz"]["sha256"],
            "The real original98 completed but explicitly unaccepted warm/status pair")
        producer = warm.get("optimization_warm", {}).get("source_sha256")
        require(isinstance(producer, dict) and producer,
            "The complete actual98 producer ledger is present")
        producer_raw = (json.dumps(producer, ensure_ascii=True, sort_keys=True,
            separators=(",", ":"), allow_nan=False) + "\n").encode("ascii")
        state["original_producer_source_map_identity"] = dict(
            canonical_ASCII_sorted_compact_with_LF_bytes=len(producer_raw),
            canonical_ASCII_sorted_compact_with_LF_sha256=hashlib.sha256(producer_raw).hexdigest(),
            actual_member=receipt(warm_path), JSON_pointer="/optimization_warm/source_sha256",
            actual_source_count=len(producer))
        state["pending_original_producer_sources"] = list(producer)
        write(record_path, state)
        for name, digest in producer.items():
            require(current_source_pins.get(name) == digest,
                "Every actual98 producer belongs to the explicit current closure: " + name)
            checked_source(name, digest)
            state["actual_producer_sources"][name] = digest
            state["pending_original_producer_sources"].remove(name)
        port_path = output / "actual98-original-port-object.json"
        write(port_path, warm["complete_scalar_profile"]["complete_original_port"])
        state["port_transport"] = dict(actual=receipt(port_path), source=receipt(warm_path),
            source_JSON_pointer="/complete_scalar_profile/complete_original_port",
            original_complete_object_preserved=True, original_port_file_SHA_claimed=False)
        state["exact_current_prefix_inputs"] = dict(warm=receipt(warm_path),
            warm_status=receipt(status_path), port=receipt(port_path))
        # The unused whole archive is retired only after its original hash and
        # both complete original members returned. The live input pair remains.
        archive_path.unlink()
        state["archive_removed"] = True
        state.update(complete=True, phase="complete-original98-input-pair",
            genuine_prefix_source="actual98 complete31 unaccepted warm",
            complete_current_field_or_native_acceptance=False)
        return state
    except BaseException as error:
        state["error"] = dict(type=type(error).__name__, message=str(error),
            traceback=traceback.format_exc())
        raise
    finally:
        write(record_path, state)


def rebuild_initial_guess(args, context, output, read, write,
                          array_identity, scalar_spec, true_height):
    """Form one new 453-row initial field and reevaluate the original RHS.

    The 338 physical and112 core columns are copied from the validated original
    input. Only all three constant-control columns receive the explicit seed.
    No residual or derivative from the original warm is claimed current.
    """
    require_actions()
    import numpy as np

    def complete_array_identity(value):
        # Complete bytes are bound. A large state/RHS vector is not re-encoded
        # in a diagnostic list of signed-zero addresses.
        actual = np.asarray(value, dtype="<f8", order="C")
        flat = actual.reshape(-1)
        return dict(shape=list(actual.shape), dtype="<f8", order="C",
            raw_sha256=hashlib.sha256(actual.tobytes(order="C")).hexdigest(),
            negative_zero_count=int(np.count_nonzero((flat == 0) & np.signbit(flat))),
            complete_large_array_values_not_returned=True)

    output = Path(output)
    require(not output.exists(), "Fresh scalar-seed initialization output")
    output.mkdir(mode=0o700)
    status_path = output / "initialization.json"
    record = dict(schema=STATUS_SCHEMA, run=run_identity(), source=receipt(__file__),
        phase="reading-explicit-parameter-seed", complete=False, error=None,
        original_prefix_input=dict(warm=receipt(args.warm),
            warm_status=receipt(args.warm_status), port=receipt(args.port)),
        original_prefix_source="actual98 complete31",
        prior_actual228_field_or_rhs_or_H_or_J_consumed=False,
        old_prefix_producer_rewritten=False, original_input_bytes_rewritten=False,
        new_initial_guess_is_not_a_solver_result=True,
        original_RHS_started=False, original_RHS_returned=False,
        original_height_started=False, original_height_returned=False,
        source_current_native_acceptance_inherited=False,
        actual_current_H_native_not_yet_called=True)
    write(status_path, record)
    try:
        require(sha(args.warm) == MEMBERS["warm-001.json.gz"]["sha256"]
            and Path(args.warm).stat().st_size == MEMBERS["warm-001.json.gz"]["bytes"]
            and sha(args.warm_status) == MEMBERS["driver-status.json"]["sha256"]
            and Path(args.warm_status).stat().st_size == MEMBERS["driver-status.json"]["bytes"],
            "The original98 pair, distinct from the current seeded initial field")
        require(context["status"].get("schema") == PARENT_SCHEMA
            and context["warm"].get("optimization_warm", {}).get("schema") == PARENT_SCHEMA,
            "Both actual original98 producer identities remain unchanged")
        seed_path = Path(args.initial_scalar_seed).resolve(strict=True)
        require(seed_path.is_file() and not seed_path.is_symlink()
            and sha(seed_path) == args.initial_scalar_seed_sha256,
            "The explicit three-word seed has its actual complete file identity")
        seed = read(seed_path)
        require(seed.get("schema") == SEED_SCHEMA, "Explicit initial-only scalar seed schema")
        values = seed.get("values")
        require(isinstance(values, list) and len(values) == 3
            and all(type(value) in (int, float) and math.isfinite(value) for value in values),
            "All three finite real scalar initial coordinates")
        parameters = np.asarray(values, dtype=float)
        flow, profile = context["flow"], context["profile"]
        require(context["M"] == 112 and context["N"] == 2048
            and flow.n == 338 and flow.k == 3 and flow.dimension == 453
            and flow.core_slice == slice(338, 450)
            and flow.parameter_slice == slice(450, 453),
            "Original338 physical,112 core andthree parameter layout")
        mesh = np.array(context["mesh"], dtype=float, copy=True)
        states = np.array(context["states"], dtype=float, copy=True)
        require(states.shape == (len(mesh), 453),
            "The complete actual prefix initial field retains every node and row")
        record.update(seed=receipt(seed_path), complete_seed_record=copy.deepcopy(seed),
            scalar_parameters_binary64=parameters.tolist(),
            scalar_parameter_words_float64le=[np.asarray([p], dtype="<f8").tobytes().hex()
                for p in parameters],
            original_parameter_rows=complete_array_identity(states[:, flow.parameter_slice]),
            original_mesh=complete_array_identity(mesh),
            original_physical_and_core_rows=complete_array_identity(states[:, :450]),
            physical_rows_copied_without_alteration=338,
            core_rows_copied_without_alteration=112,
            initial_parameters_remain_solver_unknowns=True,
            fixed_parameter_solve_or_new_acceptance_gate=False)
        states[:, flow.parameter_slice] = parameters[None, :]
        record.update(phase="original-augmented-RHS-at-new-initial-parameters",
            original_RHS_started=True, complete_node_count=len(mesh))
        write(status_path, record)
        rhs = np.asarray(flow(mesh, states.T)).T
        require(rhs.shape == states.shape and np.all(np.isfinite(rhs)),
            "The original RHS must return all finite current augmented rows")
        record.update(original_RHS_returned=True,
            new_initial_state=complete_array_identity(states), new_initial_rhs=complete_array_identity(rhs),
            old_saved_rhs_reused=False,
            phase="current-unquantized-height-from-new-initial-field",
            original_height_started=True)
        write(status_path, record)
        height = np.asarray(true_height(context["boundary"], states[-1]), dtype=float)
        require(height.shape == (112,) and np.all(np.isfinite(height)),
            "Original true_height must return the complete finite current112 H")
        specification = scalar_spec(profile, context["port"], parameters,
            context["specification"]["accepted_prefix_sha256"])
        new_warm = dict(schema=INITIAL_SCHEMA, scope=__doc__,
            M=112, N=2048, mesh=mesh.tolist(), states=states.tolist(), rhs=rhs.tolist(),
            state_layout="338 physical rows,112 constant core rows,3 constant scalar-control rows",
            field_representation=copy.deepcopy(context["warm"]["field_representation"]),
            complete_scalar_profile=specification,
            finite_boundary_scheme=context["warm"]["finite_boundary_scheme"],
            source_sha256=sha(__file__), success=False,
            new_coupled_finite_acceptance=False, nonlinear_native_solved=False,
            parameter_initialization=dict(schema=STATUS_SCHEMA, source=receipt(__file__),
                original_input=copy.deepcopy(record["original_prefix_input"]),
                seed=receipt(seed_path), current_three_values=parameters.tolist(),
                physical_and_core_guess_source="actual98 complete31 original saved words",
                previous_actual228_scientific_payload_consumed=False,
                fresh_original_augmented_rhs=True, scalar_controls_fixed_for_solver=False))
        warm_path = output / "initial-parameter-guess.json.gz"
        write(warm_path, new_warm)
        specification_raw = (json.dumps(specification, ensure_ascii=True,
            sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode("ascii")
        record.update(complete=True, phase="new-initial-field-and-H-returned",
            original_height_returned=True, actual_initial_guess=receipt(warm_path),
            actual_height=array_identity(height), actual_height_entries=112,
            current_scalar_specification=dict(actual_file=receipt(warm_path),
                JSON_pointer="/complete_scalar_profile",
                canonical_ASCII_sorted_compact_with_LF_bytes=len(specification_raw),
                canonical_ASCII_sorted_compact_with_LF_sha256=hashlib.sha256(specification_raw).hexdigest(),
                schema=specification["schema"],
                original_complete_formula_preserved_in_current_initial_guess=True,
                original_complete_scalar_object_is_not_returned_as_necessary_raw=True),
            full_prefix_solution_not_claimed=True,
            H_may_equal_an_older_initial_H_no_substitution_or_improvement_claim=True,
            native_J_FD_fullDN_and_final_audit_all_still_required=True)
        context.update(warm=new_warm, mesh=mesh, states=states, height=height,
            specification=specification, actual_solver_warm_path=warm_path,
            scalar_initialization=record)
        context["warm_provenance"] = dict(**context["warm_provenance"],
            current_original_prefix_kind="actual98 complete31",
            current_seeded_initial_guess_is_distinct_from_original_prefix=True,
            current_seeded_initial_guess=receipt(warm_path), scalar_seed=receipt(seed_path),
            only_returned_actual228_three_parameters_used=True,
            prior_actual228_state_rhs_H_J_or_cache_imported=False)
        return context
    except BaseException as error:
        record["error"] = dict(type=type(error).__name__, message=str(error),
            traceback=traceback.format_exc())
        raise
    finally:
        write(status_path, record)
