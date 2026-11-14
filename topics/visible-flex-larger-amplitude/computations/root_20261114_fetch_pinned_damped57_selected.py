#!/usr/bin/env python3
"""Fetch exactly five saved actual57 files after verifying the complete ZIP.

This is a transport-only adapter for the exact public repository's Actions.
The SHA-locked standard-library kernel retains its original explicit CLI,
network/Authorization handling, full ZIP size/SHA verification, safe output
reservation, receipt-last publication, cleanup and read-only sealing.

The kernel's full extraction function is deliberately replaced. Every ZIP
member name/type and the complete central directory's path relationships
are validated, but only the pinned result and its four pinned descriptor
payloads are inflated. Only those five payloads receive CRC/size/SHA checks.
No unselected member payload, factor, full1373 direction or54 J is claimed
to have an independent extracted-byte audit. The array manifest is copied
as an original file; its other declarations are not verification of arrays
that this adapter did not extract. No numerical module is imported.
"""
from __future__ import annotations

import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import zipfile
import zlib


REPOSITORY = "Rogerhu12/math-research-public"
KERNEL_NAME = "exact_20261114_fetch_pinned_public_artifact.py"
KERNEL_SHA256 = "51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859"
KERNEL_SCHEMA = "pinned-public-actions-artifact-fetch-v3"
ORIGINAL_KERNEL_PIN = {
    "run_id": 43611175099,
    "artifact_id": 14120548264,
    "artifact_name": "visible-mainline-nativecorrection-43611175099-1",
    "expected_size": 235561097,
    "expected_sha256": "0ff8e6f597af60f19243b5457c28e8638096c775551b6f3d044dc2d2f1fabeee",
}
PIN = {
    "run_id": 43637356027,
    "artifact_id": 14130547938,
    "artifact_name": "visible-mainline-dampedchain-43637356027-1",
    "expected_size": 845612536,
    "expected_sha256": "226227489fb0e4111061ac03c8bfe204a8a53cda16e6bb731d2656569288aec8",
}
SOURCE_COMMIT = "adbdf144b14ae7adc71df09948a5c05f8a30e8b8"
SCHEMA = "pinned-public-actions-damped57-selected-five-artifact-fetch-v1"
ADAPTER_METADATA_KEY = "local_pin_adapter_identity_not_GitHub_metadata"
PAYLOAD_PREFIX = "native-damped-chain-qr"
RESULT_SCHEMA = "complete-native-direct-LD-J1372-damped-square-root-direction-v1"
MAX_RESULT_JSON_BYTES = 1024*1024
SELECTED = (
    {
        "descriptor_key": None,
        "file": "result.json.gz",
        "bytes": 4712,
        "sha256": "c6feb54847e96778b076076ba17b4ccd666c2548c72f8c36414b2897d176cdc1",
    },
    {
        "descriptor_key": "input_binding",
        "file": "input-binding.json.gz",
        "bytes": 335715,
        "sha256": "32cb5a0b92ab4ce642b65c0b75ba010ff26dcab5cbf77b1b847b5b469ea5279f",
    },
    {
        "descriptor_key": "array_manifest",
        "file": "output-array-manifest.json.gz",
        "bytes": 133187,
        "sha256": "8a77b6b6365562ae3d41b3ff4832576f0bd880f41f2b5ed0a8fdefa86a650401",
    },
    {
        "descriptor_key": "restricted_old_node_delta",
        "file": "large-arrays/complete-old-node-restricted-delta.f64le",
        "bytes": 1033984,
        "sha256": "5b6e7bb4205ce79c6d0f20b63e491def9747e95a3272e8add1712595ea1c4a85",
    },
    {
        "descriptor_key": "restricted_direction_checkpoint",
        "file": "restricted-original-node-direction.json.gz",
        "bytes": 1590751,
        "sha256": "691d2b98bbd767c7c524bc9e7d6dd287067a0e9283939401d8b80bf028d72d84",
    },
)


def event(name, **values):
    print(json.dumps(dict(event=name, **values), sort_keys=True,
        ensure_ascii=True, allow_nan=False), flush=True)


def failure(code, message):
    event("pinned_damped57_selected_adapter_failed", success=False,
        error_code=code, message=message,
        credentials_or_signed_URLs_serialized=False,
        scientific_computation_performed=False)
    return 2


def selected_paths():
    return [dict(item, archive_path=PAYLOAD_PREFIX+"/"+item["file"])
            for item in SELECTED]


def selection_scope():
    return dict(
        extraction_kind="exactly-five-pinned-original-payload-files",
        complete_original_ZIP_size_and_SHA256_required=True,
        all_original_ZIP_member_paths_and_types_required=True,
        selected_payload_count=5,
        selected_payloads=selected_paths(),
        selected_payload_size_CRC_and_SHA256_required=True,
        selected_result_four_descriptor_links_required=True,
        unselected_payloads_extracted=False,
        unselected_payload_CRC_checked=False,
        all_artifact_payloads_independently_audited=False,
        full_factor_payloads_extracted=False,
        full1373_direction_payload_extracted=False,
        actual54_J_payloads_extracted=False,
        array_manifest_other_array_declarations_verified=False,
        scientific_computation_performed=False)


def verify_result_links(kernel, payload):
    """Read only the already byte-pinned small result, never a numerical array."""
    result_path = payload/PAYLOAD_PREFIX/SELECTED[0]["file"]
    try:
        with gzip.open(result_path, "rb") as stream:
            raw = stream.read(MAX_RESULT_JSON_BYTES+1)
        if len(raw) > MAX_RESULT_JSON_BYTES:
            kernel.fail("SELECTED_RESULT_JSON_TOO_LARGE",
                "The pinned result exceeded its fixed decoded metadata bound.")
        result = json.loads(raw)
    except kernel.FetchError:
        raise
    except (OSError, EOFError, zlib.error, UnicodeError, json.JSONDecodeError):
        kernel.fail("SELECTED_RESULT_JSON_INVALID",
            "The byte-pinned result is not readable bounded gzip JSON.")
    if not isinstance(result, dict) or result.get("schema") != RESULT_SCHEMA:
        kernel.fail("SELECTED_RESULT_SCHEMA",
            "The pinned result schema differs from the recorded actual57 producer.")
    linked = []
    for expected in SELECTED[1:]:
        key = expected["descriptor_key"]
        descriptor = result.get(key)
        if (not isinstance(descriptor, dict)
                or any(descriptor.get(name) != expected[name]
                       for name in ("file", "bytes", "sha256"))):
            kernel.fail("SELECTED_DESCRIPTOR_PIN_MISMATCH",
                "A required original result descriptor differs from the pinned five-file selection.")
        if key == "restricted_old_node_delta" and (
                descriptor.get("dtype") != "<f8"
                or descriptor.get("order") != "C"
                or descriptor.get("shape") != [577, 224]):
            kernel.fail("SELECTED_RESTRICTION_DESCRIPTOR",
                "The selected original-node restriction descriptor changed.")
        linked.append(dict(descriptor_key=key,
            file=descriptor["file"], bytes=descriptor["bytes"],
            sha256=descriptor["sha256"]))
    return dict(result_archive_path=PAYLOAD_PREFIX+"/"+SELECTED[0]["file"],
        original_result_sha256=SELECTED[0]["sha256"],
        original_result_schema=result["schema"],
        decoded_result_bytes=len(raw), original_descriptors=linked, descriptor_links_verified=True,
        result_and_descriptors_rewritten=False,
        unselected_manifest_array_payloads_checked=False)


def extract_selected_archive(kernel, archive_path, payload):
    """Replace only extraction; the kernel has already verified the full ZIP."""
    selected = selected_paths()
    wanted = {record["archive_path"]: record for record in selected}
    if len(wanted) != 5:
        kernel.fail("SELECTED_SOURCE_INTERFACE", "The fixed selection must contain five distinct paths.")
    try:
        archive = zipfile.ZipFile(archive_path, "r")
    except (OSError, zipfile.BadZipFile):
        kernel.fail("INVALID_ZIP", "The verified archive could not be opened as a ZIP.")
    files, directories, total, original_files = [], set(), 0, 0
    with archive:
        infos = archive.infolist()
        names, members = {}, {}
        # Check every original central-directory entry before creating any
        # selected subdirectory or file, including entries never inflated.
        for info in infos:
            name, parts, is_directory = kernel.safe_member_name(info)
            if name in names:
                kernel.fail("ZIP_DUPLICATE_PATH",
                    "The ZIP contains a duplicate normalized member path.")
            names[name] = is_directory
            members[name] = (info, parts, is_directory)
            original_files += int(not is_directory)
        for name, (info, parts, is_directory) in members.items():
            for depth in range(1, len(parts)):
                ancestor = "/".join(parts[:depth])
                if ancestor in names and names[ancestor] is not True:
                    kernel.fail("ZIP_PARENT_IS_FILE",
                        "A ZIP member uses another file as its parent.")
        for expected in selected:
            name = expected["archive_path"]
            if name not in members or members[name][2]:
                kernel.fail("SELECTED_MEMBER_MISSING",
                    "An exact required selected original payload file is absent.")
            info, parts, unused_directory = members[name]
            if info.file_size != expected["bytes"]:
                kernel.fail("SELECTED_MEMBER_DECLARED_SIZE",
                    "A selected member's declared size differs from its pinned original bytes.")
            for depth in range(1, len(parts)):
                directories.add("/".join(parts[:depth]))
        # Only the selected files' ancestors are created. All modes and
        # exclusive/no-follow writes follow the original frozen extractor.
        for name in sorted(directories, key=lambda value:(value.count("/"), value)):
            (payload/name).mkdir(mode=0o700, parents=False, exist_ok=True)
        for expected in selected:
            name = expected["archive_path"]
            info, parts, unused_directory = members[name]
            destination = payload.joinpath(*parts)
            flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0)
            file_sha, crc, written = hashlib.sha256(), 0, 0
            descriptor = None
            try:
                descriptor = os.open(destination, flags, 0o600)
                with os.fdopen(descriptor, "wb") as output:
                    descriptor = None
                    with archive.open(info, "r") as input_file:
                        while True:
                            block = input_file.read(kernel.CHUNK)
                            if not block:
                                break
                            written += len(block)
                            if written > expected["bytes"]:
                                kernel.fail("SELECTED_MEMBER_OVERSIZE",
                                    "A selected ZIP member exceeded its fixed original size.")
                            file_sha.update(block)
                            crc = zlib.crc32(block, crc)
                            output.write(block)
                    output.flush()
                    os.fsync(output.fileno())
            except kernel.FetchError:
                raise
            except (OSError, RuntimeError, NotImplementedError, zipfile.BadZipFile, zlib.error):
                kernel.fail("SELECTED_MEMBER_READ_FAILURE",
                    "A selected ZIP member failed safe extraction or CRC verification.")
            finally:
                if descriptor is not None:
                    os.close(descriptor)
            digest = file_sha.hexdigest()
            if (written != expected["bytes"] or written != info.file_size
                    or (crc & 0xffffffff) != info.CRC
                    or digest != expected["sha256"]):
                kernel.fail("SELECTED_MEMBER_BYTE_MISMATCH",
                    "A selected member failed its pinned size/SHA256 or original ZIP CRC.")
            total += written
            files.append(dict(path=name, bytes=written, sha256=digest,
                crc32=f"{crc & 0xffffffff:08x}", final_mode="0444", symlink=False,
                original_result_descriptor_key=expected["descriptor_key"]))
        links = verify_result_links(kernel, payload)
    return dict(zip_member_count=len(infos),
        original_archive_file_count=original_files,
        file_count=len(files), directory_count=len(directories),
        total_extracted_bytes=total, files=files, directories=sorted(directories),
        zip_paths_checked_before_any_extraction=True,
        traversal_symlinks_special_files_duplicates_and_encryption_rejected=True,
        per_file_size_CRC_and_SHA256_verified=True,
        per_file_verification_scope="only the five files in extraction.files",
        all_original_payloads_extracted=False,
        unselected_original_file_count=original_files-len(files),
        unselected_original_payloads_inflated_or_CRC_checked=False,
        selection_scope=selection_scope(), result_descriptor_binding=links)


def main():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        return failure("PUBLIC_ACTIONS_ONLY",
            "Run this entry only in the exact public repository's GitHub Actions.")
    try:
        here = Path(__file__).resolve().parent
        kernel_path = here/KERNEL_NAME
        kernel_bytes = kernel_path.read_bytes()
        if hashlib.sha256(kernel_bytes).hexdigest() != KERNEL_SHA256:
            return failure("FROZEN_TRANSPORT_SOURCE_MISMATCH",
                "The unchanged public-artifact transport kernel does not match its full SHA256.")
        entry_path = Path(__file__).resolve()
        entry_sha = hashlib.sha256(entry_path.read_bytes()).hexdigest()
        name = "_visible_public_actual57_selected_frozen_transport_kernel"
        spec = importlib.util.spec_from_file_location(name, kernel_path)
        if spec is None or spec.loader is None:
            return failure("TRANSPORT_IMPORT_SPEC",
                "The frozen standard-library transport kernel could not be loaded.")
        kernel = importlib.util.module_from_spec(spec)
        sys.modules[name] = kernel
        spec.loader.exec_module(kernel)
        if (kernel.REPOSITORY != REPOSITORY or kernel.SCHEMA != KERNEL_SCHEMA
                or kernel.PIN != ORIGINAL_KERNEL_PIN):
            return failure("TRANSPORT_INTERFACE_IDENTITY",
                "The frozen kernel's repository, original PIN or receipt schema differs.")
        adapter_identity = dict(
            schema="actual57-fixed-pin-selected-five-adapter-provenance-v1",
            source_file=entry_path.name, source_sha256=entry_sha,
            kernel_source_file=KERNEL_NAME, kernel_source_sha256=KERNEL_SHA256,
            original_kernel_receipt_schema=KERNEL_SCHEMA,
            actual_receipt_schema=SCHEMA, actual_fixed_pin=dict(PIN),
            actual_source_commit=SOURCE_COMMIT,
            original_kernel_pin=dict(ORIGINAL_KERNEL_PIN),
            replaced_in_memory_names=["PIN", "SCHEMA", "public_metadata",
                "read_metadata", "extract_verified_archive"],
            provenance_is_local_not_returned_by_GitHub=True,
            kernel_source_file_not_modified=True,
            kernel_main_network_output_guards_publication_and_sealing_unchanged=True,
            original_full_payload_extractor_replaced_by_selected_five_extractor=True,
            adapter_does_not_read_GITHUB_TOKEN=True,
            selection_scope=selection_scope(), scientific_computation_performed=False)
        original_read_metadata = kernel.read_metadata

        def read_metadata_with_source_pin(opener, token):
            metadata, canonical = original_read_metadata(opener, token)
            if metadata.get("workflow_run", {}).get("head_sha") != SOURCE_COMMIT:
                kernel.fail("SOURCE_COMMIT_PIN_MISMATCH",
                    "The original artifact source commit changed.")
            return metadata, canonical

        original_public_metadata = kernel.public_metadata

        def public_metadata_with_adapter(metadata):
            value = original_public_metadata(metadata)
            if ADAPTER_METADATA_KEY in value:
                raise RuntimeError("Reserved adapter metadata key collision")
            value[ADAPTER_METADATA_KEY] = adapter_identity
            return value

        kernel.PIN = dict(PIN)
        kernel.SCHEMA = SCHEMA
        kernel.public_metadata = public_metadata_with_adapter
        kernel.read_metadata = read_metadata_with_source_pin
        kernel.extract_verified_archive = lambda archive, payload: extract_selected_archive(
            kernel, archive, payload)
        event("pinned_damped57_selected_adapter_bound", repository=REPOSITORY,
            adapter_identity=adapter_identity)
        # The unchanged parser requires all five explicit PIN fields plus
        # --out. The kernel's own source_file/source_sha256 stay truthful.
        return kernel.main()
    except (KeyboardInterrupt, SystemExit):
        raise
    except Exception:
        return failure("ADAPTER_LOCAL_FAILURE",
            "The fixed-pin selected adapter failed; exception details are withheld to protect credentials and signed URLs.")


if __name__ == "__main__":
    raise SystemExit(main())
