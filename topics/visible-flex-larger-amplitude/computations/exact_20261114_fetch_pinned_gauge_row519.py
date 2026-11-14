#!/usr/bin/env python3
"""Fetch the pinned actual43 direction and original new519 residual inputs.

This transport-only entry runs in this public repository's Actions. It
verifies the complete pinned artifact metadata and ZIP bytes, but extracts
only result.json.gz, its direction/checkpoint, and original residual/scales. No
G/J/LU arrays are extracted and no scientific source is imported or run.
HTTPS, authorization stripping on origin changes, private staging,
exclusive publication and read-only sealing follow frozen fetch512247.
Only --out is accepted; GITHUB_TOKEN belongs only in this step's environment.
"""
from __future__ import annotations

import argparse
import datetime
import gzip
import hashlib
import json
import ntpath
import os
import re
from pathlib import Path
import shutil
import ssl
import stat
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
import zipfile
import zlib


REPOSITORY = "Rogerhu12/math-research-public"
API_ORIGIN = "https://api.github.com"
PIN = {
    "run_id": 43626121246,
    "source_commit": "5c6f45fcac65d96f6b64c8d97f842efcd280f342",
    "artifact_id": 14126695571,
    "artifact_name": "visible-mainline-rawcell0gauge-43626121246-1",
    "expected_size": 430132210,
    "expected_sha256": "2fd2f07095dce463e7f57c473332a3cfc77cdd0cdaa2ad6e02d3b48f0c86b2f5",
}
PARENT_TRANSPORT_SOURCE_SHA256 = "51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859"
RESULT_MEMBER = "rawcell0-gauge-correction/result.json.gz"
RESULT_SHA256 = "cf6e00345697ed8bd4a114c2d79f8625e49626d2263e83f42e7dc60e3020013e"
RESULT_SCHEMA = "native-gauge-original1372-equilibrated-band-correction-v1"
RESULT_SOURCE_SHA256 = "16fca40ec0ff21a119ce1563241692248005ec6587af000efb968c5158ad9a00"
ORIGINAL_STEP_RESULT_SHA256 = "6e9485dcc8bc512481d714d794f87e76f785b577fd6f714ae12fd9d8e9468adf"
ORIGINAL_MATRIX_SHA256 = "e929e642a9738c98d97dc06129c396b8fdff09aac32430892a412701d5dd4521"
MAX_RESULT_JSON_BYTES = 64 * 1024 * 1024
SHA256_PATTERN = re.compile(r"[0-9a-f]{64}\Z")

SCHEMA = "pinned-actual43-original-direction-and-row519-inputs-fetch-v1"
RECEIPT_NAME = "_pinned_gauge_row519_receipt.json"
CHUNK = 1024*1024
MAX_METADATA = 1024*1024
MAX_REDIRECTS = 8
REQUEST_TIMEOUT_SECONDS = 60


class FetchError(RuntimeError):
    def __init__(self, code, message):
        super().__init__(message)
        self.code, self.safe_message = code, message


def fail(code, message):
    raise FetchError(code, message)


def public_event(event, **values):
    print(json.dumps(dict(event=event, **values),
        sort_keys=True, ensure_ascii=True), flush=True)


def validate_https_url(value):
    """Validate without ever including the URL in a raised error."""
    if not isinstance(value, str) or not value:
        fail("UNSAFE_REDIRECT", "A required HTTPS URL was absent.")
    if any(ord(character) < 32 or ord(character) == 127 for character in value):
        fail("UNSAFE_REDIRECT", "A URL contains a forbidden control character.")
    try:
        parsed = urllib.parse.urlsplit(value)
        hostname, port = parsed.hostname, parsed.port
    except (ValueError, UnicodeError):
        fail("UNSAFE_REDIRECT", "A URL could not be safely parsed.")
    if (parsed.scheme.lower() != "https" or not hostname
            or parsed.username is not None or parsed.password is not None
            or parsed.fragment or port not in (None, 443)):
        fail("UNSAFE_REDIRECT", "Only HTTPS on port443 without userinfo or fragment is allowed.")
    return parsed, (hostname.lower(), port or 443)


class NoAutomaticRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def make_opener():
    # Default certificate and hostname verification remain enabled.
    return urllib.request.build_opener(
        urllib.request.HTTPSHandler(context=ssl.create_default_context()),
        NoAutomaticRedirect())


def request_once(opener, url, token, authorization_allowed):
    parsed, origin = validate_https_url(url)
    headers = {
        "User-Agent": "math-research-public-pinned-artifact-fetch",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "Accept-Encoding": "identity",
    }
    if authorization_allowed:
        if origin != ("api.github.com", 443):
            fail("AUTHORIZATION_ORIGIN", "Authorization is limited to the canonical GitHub API origin.")
        headers["Authorization"] = "Bearer "+token
    request = urllib.request.Request(url, headers=headers, method="GET")
    try:
        return opener.open(request, timeout=REQUEST_TIMEOUT_SECONDS)
    except urllib.error.HTTPError as error:
        # Return the response for status/Location handling, without reading
        # or logging a body, header set, Request repr or signed URL.
        return error
    except (urllib.error.URLError, TimeoutError, OSError, ssl.SSLError):
        fail("NETWORK_FAILURE", "An HTTPS request failed; no URL or credentials are logged.")


def read_metadata(opener, token):
    endpoint = f"{API_ORIGIN}/repos/{REPOSITORY}/actions/artifacts/{PIN['artifact_id']}"
    response = request_once(opener, endpoint, token, True)
    try:
        status = int(response.code)
        if status != 200:
            fail("METADATA_HTTP_STATUS", f"The canonical artifact metadata returned HTTP {status}.")
        raw = response.read(MAX_METADATA+1)
        if len(raw) > MAX_METADATA:
            fail("METADATA_TOO_LARGE", "Artifact metadata exceeded the fixed response-size bound.")
    except FetchError:
        raise
    except (OSError, TimeoutError):
        fail("METADATA_READ_FAILURE", "The artifact metadata transfer did not finish.")
    finally:
        response.close()
    try:
        metadata = json.loads(raw)
    except (UnicodeError, json.JSONDecodeError):
        fail("METADATA_JSON", "Artifact metadata was not valid JSON.")
    if not isinstance(metadata, dict):
        fail("METADATA_SCHEMA", "Artifact metadata must be a JSON object.")
    run = metadata.get("workflow_run")
    expected_digest = "sha256:"+PIN["expected_sha256"]
    if (metadata.get("id") != PIN["artifact_id"]
            or metadata.get("name") != PIN["artifact_name"]
            or metadata.get("size_in_bytes") != PIN["expected_size"]
            or metadata.get("digest") != expected_digest
            or metadata.get("expired") is not False
            or not isinstance(run, dict) or run.get("id") != PIN["run_id"]
            or run.get("head_sha") != PIN["source_commit"]):
        fail("METADATA_PIN_MISMATCH",
            "Artifact metadata did not match the pinned run/source/id/name/size/digest/nonexpired tuple.")
    archive_url = metadata.get("archive_download_url")
    canonical = f"{API_ORIGIN}/repos/{REPOSITORY}/actions/artifacts/{PIN['artifact_id']}/zip"
    # Never use an arbitrary metadata URL as an authorized endpoint.
    if archive_url != canonical:
        fail("METADATA_ARCHIVE_ENDPOINT", "The archive API endpoint is not the canonical pinned public endpoint.")
    return metadata, canonical


def download_archive(opener, token, canonical, destination, state):
    url = canonical
    authorization_allowed = True
    redirect_origins = []
    response = None
    authorization_removed = False
    for hop in range(MAX_REDIRECTS+1):
        _, origin = validate_https_url(url)
        response = request_once(opener, url, token, authorization_allowed)
        status = int(response.code)
        if status in (301, 302, 303, 307, 308):
            location = response.headers.get("Location")
            response.close()
            response = None
            if hop == MAX_REDIRECTS or not location:
                fail("REDIRECT_LIMIT", "Archive redirection was missing or exceeded its fixed bound.")
            try:
                next_url = urllib.parse.urljoin(url, location)
            except (ValueError, UnicodeError):
                fail("UNSAFE_REDIRECT", "An archive redirect could not be safely resolved.")
            _, next_origin = validate_https_url(next_url)
            if next_origin != origin:
                authorization_allowed = False
                authorization_removed = True
            # Authorization is never restored later in a redirect chain.
            redirect_origins.append(dict(
                source_host=origin[0], destination_host=next_origin[0],
                origin_changed=bool(next_origin != origin),
                next_request_authorization=bool(authorization_allowed)))
            url = next_url
            continue
        if status != 200:
            response.close()
            response = None
            fail("ARCHIVE_HTTP_STATUS", f"The artifact download returned HTTP {status}.")
        break
    if response is None:
        fail("ARCHIVE_NO_RESPONSE", "No final archive response was obtained.")
    received, digest = 0, hashlib.sha256()
    declared_length = response.headers.get("Content-Length")
    content_encoding = response.headers.get("Content-Encoding", "identity").lower()
    try:
        if content_encoding != "identity":
            fail("ARCHIVE_CONTENT_ENCODING", "The pinned archive response must retain identity bytes.")
        if declared_length is not None:
            try:
                length = int(declared_length)
            except ValueError:
                fail("ARCHIVE_CONTENT_LENGTH", "The archive Content-Length was not an integer.")
            if length != PIN["expected_size"]:
                fail("ARCHIVE_CONTENT_LENGTH", "The archive Content-Length differs from the pinned size.")
        with open(destination, "xb") as output:
            while True:
                chunk = response.read(CHUNK)
                if not chunk:
                    break
                received += len(chunk)
                state["archive_received_bytes"] = received
                if received > PIN["expected_size"]:
                    fail("ARCHIVE_OVERSIZE", "The archive exceeded its pinned size.")
                digest.update(chunk)
                output.write(chunk)
            output.flush()
            os.fsync(output.fileno())
    except FetchError:
        raise
    except (OSError, TimeoutError):
        fail("ARCHIVE_READ_FAILURE", "The pinned archive transfer or local write did not finish.")
    finally:
        response.close()
    actual_sha = digest.hexdigest()
    if received != PIN["expected_size"] or actual_sha != PIN["expected_sha256"]:
        fail("ARCHIVE_BYTE_MISMATCH", "The complete archive bytes failed pinned size/SHA-256 verification.")
    return dict(actual_size=received, actual_sha256=actual_sha,
        http_status=200, content_length=declared_length,
        redirect_count=len(redirect_origins), redirect_origins=redirect_origins,
        authorization_removed_on_every_origin_change=True,
        any_origin_change_removed_authorization=authorization_removed,
        authorization_never_restored_after_origin_change=True,
        HTTPS_only=True, signed_redirect_urls_recorded=False,
        request_timeout_seconds=REQUEST_TIMEOUT_SECONDS)


def safe_member_name(info):
    raw = info.orig_filename
    if (not isinstance(raw, str) or raw != info.filename or not raw
            or "\x00" in raw or "\\" in raw or ":" in raw
            or raw.startswith("/") or ntpath.splitdrive(raw)[0]
            or any(ord(character) < 32 or ord(character) == 127 for character in raw)):
        fail("UNSAFE_ZIP_PATH", "A ZIP member has an unsafe or ambiguous path.")
    is_directory = raw.endswith("/")
    name = raw[:-1] if is_directory else raw
    parts = name.split("/")
    if not name or any(part in ("", ".", "..") for part in parts):
        fail("UNSAFE_ZIP_PATH", "A ZIP member contains traversal or ambiguous components.")
    if name == RECEIPT_NAME or parts[0] == RECEIPT_NAME:
        fail("ZIP_RECEIPT_COLLISION", "A ZIP member collides with the reserved receipt path.")
    mode = info.external_attr >> 16
    kind = stat.S_IFMT(mode)
    if stat.S_ISLNK(mode):
        fail("ZIP_SYMLINK", "Symbolic links are not accepted in the pinned payload.")
    if kind not in (0, stat.S_IFREG, stat.S_IFDIR):
        fail("ZIP_SPECIAL_FILE", "Special files are not accepted in the pinned payload.")
    if (kind == stat.S_IFDIR and not is_directory
            or kind == stat.S_IFREG and is_directory):
        fail("ZIP_TYPE_MISMATCH", "A ZIP path and its declared file type disagree.")
    if info.flag_bits & 1:
        fail("ZIP_ENCRYPTED", "Encrypted ZIP members are not accepted.")
    if is_directory and info.file_size != 0:
        fail("ZIP_DIRECTORY_DATA", "A ZIP directory entry contains data.")
    return name, parts, is_directory


def selected_descriptor_name(descriptor):
    if not isinstance(descriptor, dict):
        fail("RESULT_DESCRIPTOR", "A selected complete file descriptor is missing.")
    relative = descriptor.get("file")
    if (not isinstance(relative, str) or not relative or "\\" in relative
            or ":" in relative or relative.startswith("/")
            or any(ord(c) < 32 or ord(c) == 127 for c in relative)):
        fail("RESULT_DESCRIPTOR_PATH", "A selected descriptor has an unsafe relative path.")
    parts = relative.split("/")
    if any(p in ("", ".", "..") for p in parts):
        fail("RESULT_DESCRIPTOR_PATH", "A selected descriptor has an ambiguous relative path.")
    if (type(descriptor.get("bytes")) is not int or descriptor["bytes"] < 0
            or SHA256_PATTERN.fullmatch(descriptor.get("sha256", "")) is None):
        fail("RESULT_DESCRIPTOR_IDENTITY", "A selected descriptor lacks an exact byte count and SHA256.")
    return "rawcell0-gauge-correction/" + relative


def extract_one_selected(archive, member, name, payload, expected_sha, expected_size=None):
    if member.is_dir():
        fail("SELECTED_ZIP_DIRECTORY", "A selected packet is not a regular file.")
    if expected_size is not None and member.file_size != expected_size:
        fail("SELECTED_ZIP_SIZE", "A selected packet differs from its bound descriptor size.")
    parts = name.split("/")
    destination = payload.joinpath(*parts)
    destination.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0)
    file_sha, crc, written = hashlib.sha256(), 0, 0
    descriptor = None
    try:
        descriptor = os.open(destination, flags, 0o600)
        with os.fdopen(descriptor, "wb") as output:
            descriptor = None
            with archive.open(member, "r") as source:
                while True:
                    block = source.read(CHUNK)
                    if not block:
                        break
                    written += len(block)
                    if written > member.file_size:
                        fail("ZIP_MEMBER_OVERSIZE", "A selected ZIP member exceeded its declared size.")
                    file_sha.update(block)
                    crc = zlib.crc32(block, crc)
                    output.write(block)
            output.flush()
            os.fsync(output.fileno())
    except FetchError:
        raise
    except (OSError, RuntimeError, NotImplementedError, zipfile.BadZipFile):
        fail("ZIP_MEMBER_READ_FAILURE", "A selected packet failed safe extraction or CRC verification.")
    finally:
        if descriptor is not None:
            os.close(descriptor)
    if (written != member.file_size or (crc & 0xffffffff) != member.CRC
            or file_sha.hexdigest() != expected_sha):
        fail("SELECTED_ZIP_BYTE_MISMATCH", "A selected packet failed its exact size/CRC/SHA256 binding.")
    return dict(path=name, bytes=written, sha256=file_sha.hexdigest(),
                crc32=f"{crc & 0xffffffff:08x}", final_mode="0444", symlink=False)


def read_gzip_metadata(path):
    try:
        with gzip.open(path, "rb") as stream:
            raw = stream.read(MAX_RESULT_JSON_BYTES + 1)
        if len(raw) > MAX_RESULT_JSON_BYTES:
            fail("PACKET_METADATA_SIZE", "A pinned packet exceeds the metadata parsing bound.")
        value = json.loads(raw)
    except FetchError:
        raise
    except (OSError, EOFError, UnicodeError, json.JSONDecodeError):
        fail("PACKET_METADATA_FORMAT", "A selected packet is not a complete gzip JSON document.")
    if not isinstance(value, dict):
        fail("PACKET_METADATA_TYPE", "A selected metadata document must be an object.")
    return value


def read_selected_result(path):
    # This only parses the pinned metadata document. It does not decode raw
    # direction numbers or instantiate any scientific producer/consumer.
    try:
        with gzip.open(path, "rb") as stream:
            raw = stream.read(MAX_RESULT_JSON_BYTES + 1)
        if len(raw) > MAX_RESULT_JSON_BYTES:
            fail("RESULT_METADATA_SIZE", "The pinned result exceeds the metadata parsing bound.")
        result = json.loads(raw)
    except FetchError:
        raise
    except (OSError, EOFError, UnicodeError, json.JSONDecodeError):
        fail("RESULT_METADATA_FORMAT", "The selected result is not a complete gzip JSON document.")
    if (not isinstance(result, dict) or result.get("schema") != RESULT_SCHEMA
            or result.get("source_sha256") != RESULT_SOURCE_SHA256
            or result.get("actual_step_result_sha256") != ORIGINAL_STEP_RESULT_SHA256
            or result.get("original1372_matrix_identity_sha256") != ORIGINAL_MATRIX_SHA256
            or result.get("diagnostic_completed") is not True
            or result.get("linear_direction_computed") is not True):
        fail("RESULT_IDENTITY", "The pinned actual43 result identity or complete direction is inconsistent.")
    return result


def extract_verified_archive(archive_path, payload):
    """Validate all ZIP paths, then extract exactly five bound packets."""
    try:
        archive = zipfile.ZipFile(archive_path, "r")
    except (OSError, zipfile.BadZipFile):
        fail("INVALID_ZIP", "The verified archive could not be opened as a ZIP.")
    with archive:
        infos = archive.infolist()
        names, by_name = {}, {}
        for info in infos:
            name, parts, is_directory = safe_member_name(info)
            if name in names:
                fail("ZIP_DUPLICATE_PATH", "The ZIP contains a duplicate normalized member path.")
            names[name] = is_directory
            by_name[name] = (info, parts, is_directory)
        # Check every member, including every unselected large matrix path.
        # No unselected payload is decompressed or written.
        for name, unused_entry in by_name.items():
            unused_info, parts, unused_directory = unused_entry
            for depth in range(1, len(parts)):
                ancestor = "/".join(parts[:depth])
                if ancestor in names and names[ancestor] is not True:
                    fail("ZIP_PARENT_IS_FILE", "A ZIP member uses a regular file as its parent.")
        if RESULT_MEMBER not in by_name or by_name[RESULT_MEMBER][2]:
            fail("RESULT_ZIP_MEMBER", "The fixed actual43 result is absent from the pinned ZIP.")
        files = [extract_one_selected(
            archive, by_name[RESULT_MEMBER][0], RESULT_MEMBER, payload, RESULT_SHA256)]
        result = read_selected_result(payload/RESULT_MEMBER)
        delta = result.get("step_delta")
        checkpoint = result.get("step_direction_checkpoint")
        delta_name = selected_descriptor_name(delta)
        checkpoint_name = selected_descriptor_name(checkpoint)

        if (delta.get("dtype") != "<f8" or delta.get("order") != "C"
                or delta.get("shape") != [1373, 224]
                or delta.get("bytes") != 1373 * 224 * 8):
            fail("DELTA_DESCRIPTOR", "The result must select the complete original1373-by224 binary64 direction.")
        original_arrays = result.get("original_bound_system_arrays")
        if not isinstance(original_arrays, dict):
            fail("ORIGINAL_INPUT_DESCRIPTORS", "The actual43 original input descriptors are missing.")
        residuals = original_arrays.get("stage-residuals")
        scales = original_arrays.get("original-scales")
        residual_name = selected_descriptor_name(residuals)
        scale_name = selected_descriptor_name(scales)
        for descriptor, shape, count in (
                (residuals, [1372, 224], 2458624), (scales, [1, 1373], 10984)):
            if (descriptor.get("dtype") != "<f8" or descriptor.get("order") != "C"
                    or descriptor.get("shape") != shape or descriptor.get("bytes") != count):
                fail("ORIGINAL_INPUT_SHAPE", "The original residual/scales must retain their complete bound dimensions.")
        selection = [("step_delta", delta_name, delta),
                     ("step_direction_checkpoint", checkpoint_name, checkpoint),
                     ("original_bound_system_arrays.stage-residuals", residual_name, residuals),
                     ("original_bound_system_arrays.original-scales", scale_name, scales)]
        if len({RESULT_MEMBER} | {item[1] for item in selection}) != 5:
            fail("SELECTED_PACKET_ALIAS", "The five selected packets must be distinct files.")
        for role, name, descriptor in selection:
            if name not in by_name or by_name[name][2]:
                fail("SELECTED_ZIP_MEMBER", "A bound direction packet is absent from the pinned ZIP.")
            row = extract_one_selected(archive, by_name[name][0], name, payload,
                                       descriptor["sha256"], descriptor["bytes"])
            row["descriptor_role"] = role
            files.append(row)
        complete_checkpoint = read_gzip_metadata(payload / checkpoint_name)
        binding = complete_checkpoint.get("original_input_binding")
        if (complete_checkpoint.get("schema") != "complete-original1372-direction-from-saved-node-gauge-v1"
                or complete_checkpoint.get("source_sha256") != RESULT_SOURCE_SHA256
                or complete_checkpoint.get("actual_coordinates_are_original_Q_Pi") is not True
                or complete_checkpoint.get("restricted_to_original_nodes") is not False
                or complete_checkpoint.get("original1372_matrix_identity_sha256") != ORIGINAL_MATRIX_SHA256
                or complete_checkpoint.get("delta_float64le_sha256") != delta["sha256"]
                or not isinstance(binding, dict)
                or binding.get("new_matrix_identity_sha256") != ORIGINAL_MATRIX_SHA256
                or binding.get("actual_step_result_sha256") != ORIGINAL_STEP_RESULT_SHA256):
            fail("CHECKPOINT_BINDING", "The selected complete checkpoint does not bind this original direction/system.")
        bound_hashes = binding.get("raw_array_sha256")
        if (not isinstance(bound_hashes, dict)
                or bound_hashes.get("stage-residuals") != residuals["sha256"]
                or bound_hashes.get("original-scales") != scales["sha256"]):
            fail("ORIGINAL_INPUT_BINDING", "The complete residual/scales bytes do not match the checkpoint's original matrix binding.")
        directories = set()
        for record in files:
            parts = record["path"].split("/")
            for depth in range(1, len(parts)):
                directories.add("/".join(parts[:depth]))
        total = sum(record["bytes"] for record in files)
        selected_result = dict(
            path=RESULT_MEMBER, sha256=RESULT_SHA256, schema=RESULT_SCHEMA,
            scientific_producer_source_sha256=result["source_sha256"],
            actual41_result_sha256=result["actual_step_result_sha256"],
            original1372_matrix_identity_sha256=result["original1372_matrix_identity_sha256"],
            best_iteration=result.get("best_iteration"),
            step_delta=dict(file=delta["file"], bytes=delta["bytes"], sha256=delta["sha256"],
                            dtype=delta["dtype"], order=delta["order"], shape=delta["shape"]),
            step_direction_checkpoint=dict(file=checkpoint["file"], bytes=checkpoint["bytes"],
                                           sha256=checkpoint["sha256"]),
            original_stage_residuals=dict(file=residuals["file"], bytes=residuals["bytes"], sha256=residuals["sha256"], shape=residuals["shape"]),
            original_scales=dict(file=scales["file"], bytes=scales["bytes"], sha256=scales["sha256"], shape=scales["shape"]),
            original_input_hashes_crosschecked_against_complete_checkpoint=True)
        return dict(
            zip_member_count=len(infos), selected_file_count=5, file_count=len(files),
            directory_count=len(directories), total_extracted_bytes=total,
            files=files, directories=sorted(directories), selected_result=selected_result,
            all_central_directory_paths_checked_before_any_extraction=True,
            traversal_symlinks_special_files_duplicates_and_encryption_rejected=True,
            selected_file_size_CRC_and_SHA256_verified=True,
            unselected_file_payloads_decompressed=False,
            unselected_file_payloads_written=False,
            unselected_file_CRC_independently_checked=False,
            complete_pinned_ZIP_SHA256_binds_all_archive_bytes=True,
            G_coefficients_J_matrices_LU_and_exact_ledgers_not_extracted=True,
            raw_direction_not_decoded_or_evaluated=True)


def validate_output(argument):
    if os.environ.get("GITHUB_ACTIONS") != "true":
        fail("ENVIRONMENT", "This downloader only runs inside GitHub Actions.")
    if os.environ.get("GITHUB_REPOSITORY") != REPOSITORY:
        fail("REPOSITORY", "This downloader only runs in the exact pinned public repository.")
    if os.name != "posix" or not sys.platform.startswith("linux"):
        fail("PLATFORM", "This entry uses a Linux private temporary directory.")
    runner_value = os.environ.get("RUNNER_TEMP")
    if not runner_value:
        fail("RUNNER_TEMP", "RUNNER_TEMP must identify the independent temporary root.")
    runner = Path(runner_value).resolve(strict=True)
    target = Path(argument)
    if (not target.is_absolute() or ".." in target.parts
            or target.name in ("", ".", "..")):
        fail("OUTPUT_PATH", "Use a new absolute directory under RUNNER_TEMP.")
    # Check original path components before normalization so a symlink
    # cannot be hidden by resolve(). Parent directories must already exist.
    absolute = Path(os.path.abspath(target))
    try:
        relative = absolute.relative_to(runner)
    except ValueError:
        fail("OUTPUT_PATH", "The output directory must be below RUNNER_TEMP.")
    if not relative.parts:
        fail("OUTPUT_PATH", "The RUNNER_TEMP root itself cannot be the output.")
    cursor = runner
    for component in relative.parts[:-1]:
        cursor = cursor/component
        try:
            mode = cursor.lstat().st_mode
        except OSError:
            fail("OUTPUT_PARENT", "The independent output parent must already exist.")
        if stat.S_ISLNK(mode) or not stat.S_ISDIR(mode):
            fail("OUTPUT_PARENT", "The output parent chain must contain real directories only.")
    if os.path.lexists(absolute):
        fail("OUTPUT_EXISTS", "The independent output directory must not already exist.")
    return runner, absolute


def exclusive_publish_function():
    # actual31 verified the whole archive but renameat2 publication failed.
    # Reserve a new private target with mkdir's ordinary no-replace behavior.
    # All scientific consumers run only after this command returns success.
    # Move only already-verified entries, with the receipt last. This is
    # deliberately NOT described as an atomic whole-directory rename.
    def publish(source, target):
        reserved = False
        phase = "exclusive-target-mkdir"
        try:
            target.mkdir(mode=0o700)
            reserved = True
            os.chmod(source, 0o700, follow_symlinks=False)
            phase = "moving-validated-payload"
            for entry in sorted(source.iterdir(), key=lambda value:value.name):
                if entry.name != RECEIPT_NAME:
                    os.rename(entry, target/entry.name)
            phase = "moving-completion-receipt"
            os.rename(source/RECEIPT_NAME, target/RECEIPT_NAME)
            os.chmod(target, 0o555, follow_symlinks=False)
            source.rmdir()
        except OSError as error:
            # errno and a fixed phase are safe: never format exception text,
            # which could include external URLs in another code path.
            code = error.errno
            cleanup_complete = not reserved
            if reserved:
                try:
                    cleanup_staging(target)
                    cleanup_complete = True
                except OSError:
                    cleanup_complete = False
            public_event("exclusive_payload_publication_failed",
                phase=phase, errno=code,
                exclusively_owned_partial_target_removed=cleanup_complete)
            fail("EXCLUSIVE_PUBLISH_FAILED",
                "The verified payload could not be published in its exclusively reserved directory.")
    return publish


def make_read_only(payload, extraction):
    for record in extraction["files"]:
        os.chmod(payload/record["path"], 0o444, follow_symlinks=False)
    os.chmod(payload/RECEIPT_NAME, 0o444, follow_symlinks=False)
    for name in sorted(extraction["directories"],
            key=lambda value:(value.count("/"), value), reverse=True):
        os.chmod(payload/name, 0o555, follow_symlinks=False)
    os.chmod(payload, 0o555, follow_symlinks=False)


def cleanup_staging(path):
    if path is None or not os.path.lexists(path):
        return
    # A failed publication can leave a validated read-only
    # payload in staging. Restore directory write bits top-down so its
    # children can actually be removed; file write bits are unnecessary.
    for directory, unused_subdirs, unused_files in os.walk(path, followlinks=False):
        os.chmod(directory, 0o700, follow_symlinks=False)
    shutil.rmtree(path)


def public_metadata(metadata):
    run = metadata["workflow_run"]
    return dict(id=metadata["id"], name=metadata["name"],
        size_in_bytes=metadata["size_in_bytes"], digest=metadata["digest"],
        expired=metadata["expired"],
        created_at=metadata.get("created_at"),
        updated_at=metadata.get("updated_at"),
        expires_at=metadata.get("expires_at"),
        workflow_run={key:run.get(key) for key in (
            "id", "repository_id", "head_repository_id", "head_branch", "head_sha")})


def parse_arguments():
    class SafeParser(argparse.ArgumentParser):
        def error(self, unused_message):
            fail("CLI_ARGUMENTS",
                 "Only --out is accepted; the actual43 tuple is fixed and credentials belong only in the environment.")
    parser = SafeParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    return parser.parse_args()


def main():
    staging = None
    state = dict(phase="validating-local-environment", archive_received_bytes=0)
    try:
        args = parse_arguments()
        runner, target = validate_output(args.out)
        publish = exclusive_publish_function()
        token = os.environ.get("GITHUB_TOKEN")
        if (not token or any(character.isspace() or ord(character) < 32
                or ord(character) == 127 for character in token)):
            fail("TOKEN_ENVIRONMENT", "A valid GITHUB_TOKEN must be supplied only through this step's environment.")
        opener = make_opener()
        state["phase"] = "checking-pinned-public-artifact-metadata"
        metadata, canonical = read_metadata(opener, token)
        public_event("pinned_gauge_row519_metadata_verified",
            repository=REPOSITORY, run_id=PIN["run_id"],
            artifact_id=PIN["artifact_id"], artifact_name=PIN["artifact_name"],
            source_commit=PIN["source_commit"],
            expected_size=PIN["expected_size"], expected_sha256=PIN["expected_sha256"])
        staging = Path(tempfile.mkdtemp(prefix=f".pinned-artifact-{PIN['artifact_id']}-",
            dir=target.parent))
        payload = staging/"payload"
        payload.mkdir(mode=0o700)
        archive = staging/"verified-download.zip"
        state["phase"] = "downloading-and-verifying-pinned-archive-bytes"
        download = download_archive(opener, token, canonical, archive, state)
        # Delete the only local token reference after network use. No
        # token or authorization header is serialized at any point.
        token = None
        state["phase"] = "validating-pinned-zip-and-extracting-only-five-packets"
        extraction = extract_verified_archive(archive, payload)
        archive.unlink()
        receipt = dict(schema=SCHEMA, success=True,
            repository=REPOSITORY, pinned_input=PIN,
            copied_transport_parent_source_sha256=PARENT_TRANSPORT_SOURCE_SHA256,
            independent_three_packet_selector_source_sha256="bb2c08e1f617d9a8d834d4bb334fbd25885c13d6267fec6e1e94fe1fa1df4aee",
            fixed_result_member=RESULT_MEMBER, fixed_result_sha256=RESULT_SHA256,
            source_file=Path(__file__).name,
            source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            current_actions_run_id=os.environ.get("GITHUB_RUN_ID"),
            current_actions_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
            public_artifact_metadata=public_metadata(metadata),
            download=download, extraction=extraction,
            zip_verified_before_extraction=True, temporary_zip_removed=True,
            publication="Exclusive mkdir; verified child renames; receipt moved last; read-only sealing after moves; not atomic as a whole directory",
            whole_directory_publication_atomic=False, existing_output_directory_replaced=False,
            files_read_only_mode="0444", directories_read_only_mode="0555",
            output_directory=str(target), runner_temp=str(runner),
            token_source="GITHUB_TOKEN environment only",
            token_or_authorization_or_signed_URL_serialized=False,
            scientific_computation_performed=False)
        receipt_path = payload/RECEIPT_NAME
        with open(receipt_path, "x", encoding="utf-8") as output:
            json.dump(receipt, output, sort_keys=True, indent=2,
                ensure_ascii=True, allow_nan=False)
            output.write("\n")
            output.flush()
            os.fsync(output.fileno())
        receipt_sha = hashlib.sha256(receipt_path.read_bytes()).hexdigest()
        state["phase"] = "publishing-validated-payload"
        # Directories remain writable while rename updates parent entries.
        # Actual33 failed with EACCES after premature read-only sealing.
        # Seal only after all validated entries and the receipt have moved;
        # consumers are never started before this command returns success.
        publish(payload, target)
        state["phase"] = "sealing-published-payload-read-only"
        make_read_only(target, extraction)
        state["phase"] = "complete"
        public_event("pinned_gauge_row519_ready",
            success=True, repository=REPOSITORY, run_id=PIN["run_id"],
            artifact_id=PIN["artifact_id"], archive_sha256=download["actual_sha256"],
            archive_bytes=download["actual_size"], extracted_files=extraction["file_count"],
            extracted_bytes=extraction["total_extracted_bytes"],
            output_directory=str(target), receipt_file=RECEIPT_NAME,
            receipt_sha256=receipt_sha, scientific_computation_performed=False)
        return 0
    except FetchError as error:
        public_event("pinned_gauge_row519_failed", success=False,
            phase=state["phase"], error_code=error.code,
            message=error.safe_message,
            archive_received_bytes=state["archive_received_bytes"],
            fully_published_output=bool(state["phase"] == "complete"))
        return 2
    except (KeyboardInterrupt, SystemExit):
        raise
    except Exception:
        # urllib/ZIP/path exception repr can include a signed URL. Keep
        # the failure code and phase, never stringify an unknown exception.
        public_event("pinned_gauge_row519_failed", success=False,
            phase=state["phase"], error_code="UNEXPECTED_LOCAL_OR_TRANSFER_FAILURE",
            message="The fetch failed; exception details are withheld to protect URL credentials.",
            archive_received_bytes=state["archive_received_bytes"],
            fully_published_output=bool(state["phase"] == "complete"))
        return 2
    finally:
        try:
            cleanup_staging(staging)
        except Exception:
            # Cleanup diagnostics must not expose an exception URL or
            # invalidate a published and verified read-only payload.
            public_event("pinned_gauge_row519_staging_cleanup_incomplete",
                credentials_or_redirect_URLs_logged=False)


if __name__ == "__main__":
    raise SystemExit(main())

