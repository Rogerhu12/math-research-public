#!/usr/bin/env python3
"""R498: complete temporary JSONL storage with distinct stored/decoded identities.

This standard-library helper changes representation only. Each call receives
the original producer's canonical bytes and writes one complete gzip member.
There is no plain-text mirror, row filtering, numeric transformation, source
substitution, cleanup, or scientific acceptance predicate here. The original
producer/caller must explicitly register this source and the derived sources.
All scientific payload use remains in the named public Actions repository.

Author: ChatGPT (AI), geometry agent, 2026-11-16.
"""
from __future__ import annotations
import copy
import gzip
import hashlib
import json
import os
from pathlib import Path
import stat
import sys
import zlib

REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "R498-complete-canonical-JSONL-gzip-members-storage-v1"
ENCODING = "concatenated-gzip-members-one-original-JSONL-row-per-member"
HEX = frozenset("0123456789abcdef")


def require(value, message):
    if not value:
        raise ValueError(message)


def actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
        "Original scientific payload representation belongs only to this repository Actions")


def _sha(raw):
    return hashlib.sha256(raw).hexdigest()


def _digest(value, label):
    require(isinstance(value, str) and len(value) == 64 and set(value) <= HEX,
        "Complete SHA256 required: " + label)
    return value


def _integer(value, label):
    require(type(value) is int and value >= 0, "Nonnegative integer required: " + label)
    return value


def _temporary(path, *, exists):
    root = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    original = Path(path).absolute()
    actual = original.resolve(strict=exists)
    require(actual != root and root in actual.parents, "Payload must stay below actual RUNNER_TEMP")
    cursor = original
    while cursor != cursor.parent:
        require(not cursor.is_symlink(), "No payload or parent symlink")
        if cursor == root:
            break
        cursor = cursor.parent
    return actual


def _contained(directory, name):
    root = _temporary(directory, exists=True)
    require(isinstance(name, str) and name and not Path(name).is_absolute(),
        "Contained relative member name required")
    path = root / name
    require(path.resolve(strict=True) != root and root in path.resolve(strict=True).parents,
        "Original stored member escaped its owner")
    cursor = path
    while cursor != root:
        require(not cursor.is_symlink(), "No original member symlinks")
        cursor = cursor.parent
    require(stat.S_ISREG(path.stat().st_mode), "An actual regular stored member is required")
    return path


def _stamp(path):
    value = Path(path).stat()
    return (value.st_dev, value.st_ino, value.st_size, value.st_mtime_ns)


class GzipJSONLJournal:
    """Same add/finish/rows interface, with complete member boundaries.

    canonicalizer is the actual original producer's canonical function.
    bytes/hash retain their original logical-stream meanings internally.
    finish() reports physical stored bytes/SHA at the descriptor top level
    and the complete original logical stream under decoded. No storage
    assumption is substituted for an actual free-space observation.
    """

    def __init__(self, path, root, *, canonicalizer, compression_level=1):
        actions()
        require(callable(canonicalizer), "Use the actual original canonical row function")
        require(type(compression_level) is int and 1 <= compression_level <= 9,
            "Explicit gzip compression level in 1..9 required")
        self.root = _temporary(root, exists=True)
        self.path = _temporary(path, exists=False)
        require(self.path != self.root and self.root in self.path.parents,
            "Journal must be owned by its actual output directory")
        require(self.path.name.endswith(".jsonl.gz"), "An explicit compressed JSONL basename is required")
        require(self.path.parent.is_dir() and not self.path.exists(),
            "Fresh stored journal with an existing owned parent required")
        self.canonicalizer = canonicalizer
        self.compression_level = compression_level
        self.stream = self.path.open("xb", buffering=0)
        self.hash = hashlib.sha256()
        self.stored_hash = hashlib.sha256()
        self.bytes = self.rows = self.stored_bytes = 0
        self._failure = None
        self._finished = None

    def add(self, value):
        require(self._finished is None and not self.stream.closed and self._failure is None,
            "A finished or failed original journal cannot receive another row")
        raw = self.canonicalizer(value)
        require(isinstance(raw, bytes) and raw.endswith(b"\n") and raw.count(b"\n") == 1,
            "The original canonicalizer must return exactly one complete UTF8 JSONL record")
        # One bounded record is already materialized by the original Journal.
        # Compression adds one record-sized buffer; the entire ledger is never
        # accumulated, mirrored as plaintext, or compressed after completion.
        encoded = gzip.compress(raw, compresslevel=self.compression_level, mtime=0)
        offset = 0
        try:
            while offset < len(encoded):
                number = os.write(self.stream.fileno(), memoryview(encoded)[offset:])
                if number <= 0:
                    raise OSError("Stored original gzip member write made no progress")
                fragment = memoryview(encoded)[offset:offset+number]
                self.stored_hash.update(fragment)
                self.stored_bytes += number
                offset += number
            # The complete member, including CRC/trailer, precedes the caller's
            # existing commit write. No delayed compression buffer is involved.
            self.stream.flush()
        except BaseException as error:
            self._failure = dict(
                type=type(error).__name__, message=str(error),
                original_row_index=self.rows,
                original_row_bytes=len(raw), original_row_sha256=_sha(raw),
                encoded_member_bytes=len(encoded), encoded_member_sha256=_sha(encoded),
                stored_member_prefix_bytes=offset,
                all_preceding_members_and_original_rows_retained=True,
                complete_current_member_not_claimed=True)
            raise
        self.hash.update(raw)
        self.bytes += len(raw)
        self.rows += 1

    def finish(self):
        if self._finished is not None:
            return copy.deepcopy(self._finished)
        if not self.stream.closed:
            # As in the original Journal, an fsync/close failure is an actual
            # I/O failure; it must not be turned into a successful descriptor.
            try:
                self.stream.flush()
                os.fsync(self.stream.fileno())
            finally:
                self.stream.close()
        self._finished = dict(
            file=str(self.path.relative_to(self.root)),
            bytes=self.stored_bytes, sha256=self.stored_hash.hexdigest(), rows=self.rows,
            decoded=dict(bytes=self.bytes, sha256=self.hash.hexdigest(), rows=self.rows),
            storage=dict(
                schema=SCHEMA, encoding=ENCODING,
                compression_level=self.compression_level,
                complete_encoded_stream=self._failure is None,
                complete_member_count=self.rows,
                incomplete_member=copy.deepcopy(self._failure),
                original_canonical_bytes_not_reformatted=True,
                original_logical_row_order_and_indices_preserved=True,
                no_plaintext_ledger_mirror_created=True,
                gzip_mtime=0, python_version=sys.version.split()[0],
                zlib_compile_version=zlib.ZLIB_VERSION,
                zlib_runtime_version=zlib.ZLIB_RUNTIME_VERSION))
        return copy.deepcopy(self._finished)


def decoded_expectation(descriptor):
    """Validate an explicit representation and return its logical identity.

    Old uncompressed descriptors remain supported without changing their
    identity. An encoded descriptor is never treated as a plain old stream.
    """
    require(isinstance(descriptor, dict), "An original complete descriptor is required")
    _integer(descriptor.get("bytes"), "stored bytes")
    _integer(descriptor.get("rows"), "logical rows")
    _digest(descriptor.get("sha256"), "stored SHA256")
    storage = descriptor.get("storage")
    if storage is None:
        require("decoded" not in descriptor, "Ambiguous unregistered decoded identity")
        require(not str(descriptor.get("file", "")).endswith(".gz"),
            "A compressed member needs its explicit storage contract")
        return dict(bytes=descriptor["bytes"], rows=descriptor["rows"], sha256=descriptor["sha256"])
    require(isinstance(storage, dict) and storage.get("schema") == SCHEMA
        and storage.get("encoding") == ENCODING,
        "Use the exact complete original gzip representation contract")
    require(storage.get("complete_encoded_stream") is True
        and storage.get("incomplete_member") is None
        and storage.get("complete_member_count") == descriptor["rows"],
        "An incomplete stored stream cannot be used as a complete original ledger")
    level = storage.get("compression_level")
    require(type(level) is int and 1 <= level <= 9, "Actual declared gzip level missing")
    decoded = descriptor.get("decoded")
    require(isinstance(decoded, dict), "Original decoded bytes/SHA/rows are required")
    _integer(decoded.get("bytes"), "decoded bytes")
    _integer(decoded.get("rows"), "decoded rows")
    _digest(decoded.get("sha256"), "decoded SHA256")
    require(decoded["rows"] == descriptor["rows"], "Stored descriptor and original row count differ")
    require(str(descriptor.get("file", "")).endswith(".jsonl.gz"),
        "Stored compressed path must remain explicit")
    return dict(bytes=decoded["bytes"], rows=decoded["rows"], sha256=decoded["sha256"])



def verify_decoded_readback(descriptor, actual):
    """Thin addition for the existing necessary reader's gzip line_stream."""
    expected = decoded_expectation(descriptor)
    require(actual.get("rows") == expected["rows"]
        and actual.get("decoded_stream_bytes") == expected["bytes"]
        and actual.get("decoded_stream_sha256") == expected["sha256"],
        "The actual decoded complete original JSONL stream differs")
    return dict(storage=copy.deepcopy(descriptor.get("storage")),
        stored=dict(bytes=descriptor["bytes"], sha256=descriptor["sha256"]),
        decoded=expected, complete_original_decoded_identity_verified=True)


def bound_stream(directory, descriptor, budget, selected=None, visit=None, progress=None):
    """Read and bind every original byte/row, retaining only caller selections.

    The compressed path first verifies the complete physical stored bytes,
    then streams decoded original rows. Neither pass expands a ledger onto
    disk. Source/clock/owner checks remain in the original caller. Its budget
    is checked during both passes; no independent clock or limit is created.
    """
    actions()
    state = progress if progress is not None else {}
    chosen = []
    try:
        expected = decoded_expectation(descriptor)
        path = _contained(directory, descriptor["file"])
        stamp = _stamp(path)
        compressed = descriptor.get("storage") is not None
        state.update(
            storage_schema=SCHEMA if compressed else None,
            stored_file=descriptor["file"],
            declared_stored_bytes=descriptor["bytes"],
            declared_decoded_bytes=expected["bytes"],
            declared_original_rows=expected["rows"],
            stored_bytes_read=0, bytes_read=0, physical_lines_read=0,
            logical_scope="complete decoded original JSONL rows",
            complete_original_scope_returned=False,
            phase="stored-byte-binding" if compressed else "original-row-binding")
        if compressed:
            stored_hash = hashlib.sha256()
            with path.open("rb") as stream:
                while True:
                    budget.check()
                    block = stream.read(1 << 20)
                    if not block:
                        break
                    stored_hash.update(block)
                    state["stored_bytes_read"] += len(block)
            require((state["stored_bytes_read"], stored_hash.hexdigest()) ==
                (descriptor["bytes"], descriptor["sha256"]),
                "Complete actual stored gzip bytes/SHA differ")
            require(_stamp(path) == stamp, "Stored member changed during byte binding")
            state["actual_stored_sha256"] = stored_hash.hexdigest()
            state["phase"] = "decoded-original-row-binding"
        digest = hashlib.sha256()
        count = size = 0
        opener = gzip.open if compressed else open
        with opener(path, "rb") as stream:
            for raw in stream:
                budget.check()
                digest.update(raw)
                size += len(raw)
                state.update(bytes_read=size, physical_lines_read=count,
                    current_original_row_index=count,
                    current_original_line_bytes=len(raw),
                    current_original_line_sha256=_sha(raw))
                require(raw.endswith(b"\n"),
                    "A completed original ledger has an unfinished decoded JSONL line")
                if selected is None or selected(count):
                    value = json.loads(raw)
                    if visit is not None:
                        visit(count, value)
                    else:
                        chosen.append(value)
                count += 1
                state["physical_lines_read"] = count
        require((size, count, digest.hexdigest()) ==
            (expected["bytes"], expected["rows"], expected["sha256"]),
            "Complete decoded original bytes/rows/SHA differ")
        require(_stamp(path) == stamp, "Stored member changed during original row binding")
        if not compressed:
            state["stored_bytes_read"] = size
            state["actual_stored_sha256"] = digest.hexdigest()
        state.update(phase="complete", complete_original_scope_returned=True,
            actual_decoded_sha256=digest.hexdigest())
        for key in ("current_original_row_index", "current_original_line_bytes", "current_original_line_sha256"):
            state.pop(key, None)
        return chosen, dict(
            directory=str(Path(directory).resolve()), descriptor=copy.deepcopy(descriptor),
            actual_full_bytes_read=size, actual_full_rows_read=count,
            actual_sha256=digest.hexdigest(),
            actual_stored_bytes_read=state["stored_bytes_read"],
            actual_stored_sha256=state["actual_stored_sha256"],
            actual_decoded_identity=dict(bytes=size, rows=count, sha256=digest.hexdigest()),
            original_stream_fully_verified=True,
            complete_plaintext_ledger_materialized=False,
            whole_byte_identity_and_original_row_scope_not_new_numeric_proof=True)
    except BaseException as error:
        state["complete_original_scope_returned"] = False
        state["error"] = dict(type=type(error).__name__, message=str(error))
        # Preserve the original resource/interruption/parse exception class.
        # In particular the caller's RuntimeError budget stop must not become
        # an arithmetic/metadata exception that another layer could swallow.
        raise
