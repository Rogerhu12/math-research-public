#!/usr/bin/env python3
"""Fetch the pinned actual28 public Actions artifact without scientific work.

Only the exact Rogerhu12/math-research-public Actions environment may run
this entry. GITHUB_TOKEN is read from the environment only. Metadata and
the complete archive bytes must match the explicit pinned CLI tuple.
Redirects are handled manually, remain HTTPS, and lose Authorization on
an origin change. Tokens, response bodies and signed redirect URLs are
never printed or placed in the receipt.

Extraction rejects traversal, duplicate paths, symlinks and other special
files. A fresh private staging directory is validated completely before
an atomic no-replace rename publishes a read-only payload in RUNNER_TEMP.
The temporary ZIP is removed after validation/extraction. This entry
only downloads and preserves bytes; it imports no numerical packages.
"""
from __future__ import annotations

import argparse
import ctypes
import datetime
import hashlib
import json
import ntpath
import os
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
    "run_id": 43611175099,
    "artifact_id": 14120548264,
    "artifact_name": "visible-mainline-nativecorrection-43611175099-1",
    "expected_size": 235561097,
    "expected_sha256": "0ff8e6f597af60f19243b5457c28e8638096c775551b6f3d044dc2d2f1fabeee",
}
SCHEMA = "pinned-public-actions-artifact-fetch-v1"
RECEIPT_NAME = "_pinned_public_artifact_receipt.json"
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
            or not isinstance(run, dict) or run.get("id") != PIN["run_id"]):
        fail("METADATA_PIN_MISMATCH",
            "Artifact metadata did not match the pinned run/id/name/size/digest/nonexpired tuple.")
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


def extract_verified_archive(archive_path, payload):
    files, directories = [], set()
    total = 0
    try:
        archive = zipfile.ZipFile(archive_path, "r")
    except (OSError, zipfile.BadZipFile):
        fail("INVALID_ZIP", "The verified archive could not be opened as a ZIP.")
    with archive:
        infos = archive.infolist()
        names, members = {}, []
        for info in infos:
            name, parts, is_directory = safe_member_name(info)
            if name in names:
                fail("ZIP_DUPLICATE_PATH", "The ZIP contains a duplicate normalized member path.")
            names[name] = is_directory
            members.append((info, name, parts, is_directory))
        for info, name, parts, is_directory in members:
            for depth in range(1, len(parts)):
                ancestor = "/".join(parts[:depth])
                if ancestor in names and names[ancestor] is not True:
                    fail("ZIP_PARENT_IS_FILE", "A ZIP member uses another file as its parent.")
                directories.add(ancestor)
            if is_directory:
                directories.add(name)
        for directory in sorted(directories, key=lambda value:(value.count("/"), value)):
            (payload/directory).mkdir(mode=0o700, parents=False, exist_ok=True)
        for info, name, parts, is_directory in members:
            if is_directory:
                continue
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
                            block = input_file.read(CHUNK)
                            if not block:
                                break
                            written += len(block)
                            if written > info.file_size:
                                fail("ZIP_MEMBER_OVERSIZE", "A ZIP member exceeded its declared uncompressed size.")
                            file_sha.update(block)
                            crc = zlib.crc32(block, crc)
                            output.write(block)
                    output.flush()
                    os.fsync(output.fileno())
            except FetchError:
                raise
            except (OSError, RuntimeError, NotImplementedError, zipfile.BadZipFile):
                fail("ZIP_MEMBER_READ_FAILURE", "A ZIP member failed safe extraction or CRC verification.")
            finally:
                if descriptor is not None:
                    os.close(descriptor)
            if written != info.file_size or (crc & 0xffffffff) != info.CRC:
                fail("ZIP_MEMBER_BYTE_MISMATCH", "A ZIP member failed its declared size/CRC verification.")
            total += written
            files.append(dict(path=name, bytes=written,
                sha256=file_sha.hexdigest(), crc32=f"{crc & 0xffffffff:08x}",
                final_mode="0444", symlink=False))
    return dict(zip_member_count=len(infos), file_count=len(files),
        directory_count=len(directories), total_extracted_bytes=total,
        files=files, directories=sorted(directories),
        zip_paths_checked_before_any_extraction=True,
        traversal_symlinks_special_files_duplicates_and_encryption_rejected=True,
        per_file_size_CRC_and_SHA256_verified=True)


def validate_output(argument):
    if os.environ.get("GITHUB_ACTIONS") != "true":
        fail("ENVIRONMENT", "This downloader only runs inside GitHub Actions.")
    if os.environ.get("GITHUB_REPOSITORY") != REPOSITORY:
        fail("REPOSITORY", "This downloader only runs in the exact pinned public repository.")
    if os.name != "posix" or not sys.platform.startswith("linux"):
        fail("PLATFORM", "This entry uses Linux atomic no-replace directory publication.")
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


def atomic_publish_function():
    # ctypes is standard library. Linux renameat2(RENAME_NOREPLACE)
    # publishes the validated directory atomically without replacing even
    # an empty directory created by another process during this fetch.
    libc = ctypes.CDLL(None, use_errno=True)
    try:
        renameat2 = libc.renameat2
    except AttributeError:
        fail("ATOMIC_RENAME_UNAVAILABLE", "Atomic no-replace directory rename is unavailable.")
    renameat2.argtypes = (ctypes.c_int, ctypes.c_char_p,
        ctypes.c_int, ctypes.c_char_p, ctypes.c_uint)
    renameat2.restype = ctypes.c_int

    def publish(source, target):
        result = renameat2(-100, os.fsencode(source), -100, os.fsencode(target), 1)
        if result != 0:
            fail("ATOMIC_PUBLISH_FAILED",
                "The validated directory could not be atomically published without replacement.")
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
    # A failed no-replace publication can leave a validated read-only
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
            # argparse's default text echoes unexpected arguments; do
            # not risk exposing a mistakenly supplied token or signed URL.
            fail("CLI_ARGUMENTS", "Supply all required pinned public-artifact arguments; credentials belong only in the environment.")

    parser = SafeParser(description=__doc__)
    parser.add_argument("--run-id", type=int, required=True)
    parser.add_argument("--artifact-id", type=int, required=True)
    parser.add_argument("--artifact-name", required=True)
    parser.add_argument("--expected-size", type=int, required=True)
    parser.add_argument("--expected-sha256", required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    supplied = {key:getattr(args, key) for key in PIN}
    if supplied != PIN:
        fail("CLI_PIN_MISMATCH", "The explicit CLI tuple must equal this source's actual28 pinned artifact.")
    return args


def main():
    staging = None
    state = dict(phase="validating-local-environment", archive_received_bytes=0)
    try:
        args = parse_arguments()
        runner, target = validate_output(args.out)
        publish = atomic_publish_function()
        token = os.environ.get("GITHUB_TOKEN")
        if (not token or any(character.isspace() or ord(character) < 32
                or ord(character) == 127 for character in token)):
            fail("TOKEN_ENVIRONMENT", "A valid GITHUB_TOKEN must be supplied only through this step's environment.")
        opener = make_opener()
        state["phase"] = "checking-pinned-public-artifact-metadata"
        metadata, canonical = read_metadata(opener, token)
        public_event("pinned_public_artifact_metadata_verified",
            repository=REPOSITORY, run_id=PIN["run_id"],
            artifact_id=PIN["artifact_id"], artifact_name=PIN["artifact_name"],
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
        state["phase"] = "validating-and-extracting-pinned-zip"
        extraction = extract_verified_archive(archive, payload)
        archive.unlink()
        receipt = dict(schema=SCHEMA, success=True,
            repository=REPOSITORY, pinned_input=PIN,
            source_file=Path(__file__).name,
            source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            current_actions_run_id=os.environ.get("GITHUB_RUN_ID"),
            current_actions_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
            public_artifact_metadata=public_metadata(metadata),
            download=download, extraction=extraction,
            zip_verified_before_extraction=True, temporary_zip_removed=True,
            publication="Linux renameat2 RENAME_NOREPLACE; fully validated private directory",
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
        state["phase"] = "publishing-validated-read-only-payload"
        make_read_only(payload, extraction)
        publish(payload, target)
        state["phase"] = "complete"
        public_event("pinned_public_artifact_ready",
            success=True, repository=REPOSITORY, run_id=PIN["run_id"],
            artifact_id=PIN["artifact_id"], archive_sha256=download["actual_sha256"],
            archive_bytes=download["actual_size"], extracted_files=extraction["file_count"],
            extracted_bytes=extraction["total_extracted_bytes"],
            output_directory=str(target), receipt_file=RECEIPT_NAME,
            receipt_sha256=receipt_sha, scientific_computation_performed=False)
        return 0
    except FetchError as error:
        public_event("pinned_public_artifact_failed", success=False,
            phase=state["phase"], error_code=error.code,
            message=error.safe_message,
            archive_received_bytes=state["archive_received_bytes"],
            no_partial_output_directory_published=bool(state["phase"] != "complete"))
        return 2
    except (KeyboardInterrupt, SystemExit):
        raise
    except Exception:
        # urllib/ZIP/path exception repr can include a signed URL. Keep
        # the failure code and phase, never stringify an unknown exception.
        public_event("pinned_public_artifact_failed", success=False,
            phase=state["phase"], error_code="UNEXPECTED_LOCAL_OR_TRANSFER_FAILURE",
            message="The fetch failed; exception details are withheld to protect URL credentials.",
            archive_received_bytes=state["archive_received_bytes"],
            no_partial_output_directory_published=bool(state["phase"] != "complete"))
        return 2
    finally:
        try:
            cleanup_staging(staging)
        except Exception:
            # Cleanup diagnostics must not expose an exception URL or
            # invalidate a published and verified read-only payload.
            public_event("pinned_public_artifact_staging_cleanup_incomplete",
                credentials_or_redirect_URLs_logged=False)


if __name__ == "__main__":
    raise SystemExit(main())

