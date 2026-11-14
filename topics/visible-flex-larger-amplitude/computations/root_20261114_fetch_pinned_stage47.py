#!/usr/bin/env python3
"""Fetch the actual47 byte-pinned saved stage43 local-J and exact-action artifact.

This independent entry reuses the unchanged, byte-locked actual28 transport
kernel. Its in-memory PIN, receipt schema and public receipt metadata
decorator are replaced; an additional metadata wrapper checks the exact
triggering source commit without another API request. The decorator explicitly labels adapter provenance
as local, not as a GitHub metadata field. The kernel's own source_file and
source_sha256 remain truthful; the same final receipt also binds this entry.

The original CLI/environment guards, metadata checks, HTTPS redirect and
Authorization handling, stream limits, ZIP validation, exclusive publication,
receipt-last sequence and read-only sealing all execute in the frozen kernel.
No original file is edited. All original payload files are retained, including the complete saved four
local matrices and exact-action evidence. No scientific package is imported
or computation performed. GITHUB_TOKEN is read only by the frozen kernel from the environment.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys


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
    "run_id": 43630351235,
    "artifact_id": 14127582983,
    "artifact_name": "visible-mainline-stage43probe-43630351235-1",
    "expected_size": 3530956,
    "expected_sha256": "02973eefffbd82f57dcee02776f2ed7a28c41fe750f73ec7930ff07d2f9fa400",
}
SCHEMA = "pinned-public-actions-stage47-local-j-artifact-fetch-v1"
SOURCE_COMMIT = "c9c466f468d49e3f4699d0e0247109e83047bdb5"
ADAPTER_METADATA_KEY = "local_pin_adapter_identity_not_GitHub_metadata"


def event(name, **values):
    print(json.dumps(dict(event=name, **values), sort_keys=True,
        ensure_ascii=True, allow_nan=False), flush=True)


def failure(code, message):
    event("pinned_saved_stage47_artifact_adapter_failed", success=False,
        error_code=code, message=message,
        credentials_or_signed_URLs_serialized=False,
        scientific_computation_performed=False)
    return 2


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
        name = "_visible_public_actual47_frozen_transport_kernel"
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
            schema="actual47-fixed-pin-adapter-provenance-v1",
            source_file=entry_path.name, source_sha256=entry_sha,
            kernel_source_file=KERNEL_NAME, kernel_source_sha256=KERNEL_SHA256,
            original_kernel_receipt_schema=KERNEL_SCHEMA,
            actual_receipt_schema=SCHEMA,
            actual_fixed_pin=dict(PIN),
            actual_source_commit=SOURCE_COMMIT,
            original_kernel_pin=dict(ORIGINAL_KERNEL_PIN),
            replaced_in_memory_names=["PIN", "SCHEMA", "public_metadata", "read_metadata"],
            provenance_is_local_not_returned_by_GitHub=True,
            kernel_source_file_not_modified=True,
            kernel_main_network_extraction_and_publication_functions_unchanged=True,
            adapter_does_not_read_GITHUB_TOKEN=True,
            scientific_computation_performed=False)
        original_read_metadata = kernel.read_metadata

        def read_metadata_with_source_pin(opener, token):
            metadata, canonical = original_read_metadata(opener, token)
            if metadata.get("workflow_run", {}).get("head_sha") != SOURCE_COMMIT:
                kernel.fail("SOURCE_COMMIT_PIN_MISMATCH", "The original artifact source commit changed.")
            return metadata, canonical

        original_public_metadata = kernel.public_metadata

        def public_metadata_with_adapter(metadata):
            # Preserve every original whitelisted provider field. This one
            # conspicuously named field is local provenance, never represented
            # as provider-supplied metadata. It is written before the kernel
            # hashes/moves/seals its single completion receipt.
            value = original_public_metadata(metadata)
            if ADAPTER_METADATA_KEY in value:
                raise RuntimeError("Reserved adapter metadata key collision")
            value[ADAPTER_METADATA_KEY] = adapter_identity
            return value

        kernel.PIN = dict(PIN)
        kernel.SCHEMA = SCHEMA
        kernel.public_metadata = public_metadata_with_adapter
        kernel.read_metadata = read_metadata_with_source_pin
        event("pinned_saved_stage47_artifact_adapter_bound",
            repository=REPOSITORY, adapter_identity=adapter_identity)
        # The original parser still requires the full explicit tuple and
        # compares it with the actual47 constant above. The old kernel file
        # and its own source_file/source_sha256 receipt fields remain intact.
        return kernel.main()
    except (KeyboardInterrupt, SystemExit):
        raise
    except Exception:
        # Never stringify an exception or arbitrary external data: the kernel
        # has the same rule for possible signed URLs and credentials.
        return failure("ADAPTER_LOCAL_FAILURE",
            "The fixed-PIN adapter failed before reporting a successful transfer; exception details are withheld.")


if __name__ == "__main__":
    raise SystemExit(main())
