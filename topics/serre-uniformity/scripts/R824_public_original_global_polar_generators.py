#!/usr/bin/env python3
"""R824 public IO runner; source-preserving subset transfers and exact-stage continuation.

This file imports only the standard library.  The mathematical core is launched
only as a separate public Actions subprocess.  HTTP Range subset transfers are
never described as a fresh whole-ZIP digest verification.
"""
import argparse
import datetime as dt
import gzip
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import signal
import subprocess
import sys
import tarfile
import time
import urllib.error
import urllib.request
import zipfile

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/"topics/serre-uniformity"
REQUEST = TOPIC/"notes/R824-public-original-global-polar-generators-request.json"
RESULT = "R824-original-global-polar-generators"
FINAL = "p41-original-global-polar-generators-certificate.json"
BUNDLE = "R824-retained-producer-inputs.tar.gz"
REFERENCE = "full-outputs-manifest-reference.json"
META = ("full-outputs-manifest.json", "run-receipt.json",
        "core-receipt.json", "public-actions-input.json")
LABELS = {"R781", "R787", "R786", "R795", "R799", "R801", "R798", "R805"}
BASE_KEYS = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
H64 = re.compile(r"[0-9a-f]{64}")
INT = re.compile(r"-?(0|[1-9][0-9]*)")
R787_PREFIX = "R787-prime-1000000753-"
PINNED_OLD = {
    R787_PREFIX+"chart.json.gz": "47ac1ce2a95781417a4e3b51f2128d2dd4836e5d1793cf2a50793911dcedce96",
    R787_PREFIX+"selection.json.gz": "a420d94a9a2f56fa449946bac6379f437e7e53120a651d7df95b5f9ef9b07adb",
    R787_PREFIX+"branch-00.json.gz": "c5b75f48b5c5d1cf2d98390e814a245306fa63f10ae43dae194dbfd560d895d7",
    R787_PREFIX+"rational-blocks.json.gz": "fb8a82957474e657fc476aa2baa0d8ce9f4c8b6cc86c2b55a79e75913d610b3b",
}


def sha(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for part in iter(lambda: stream.read(4*1024*1024), b""):
            value.update(part)
    return value.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".tmp")
    data = (json.dumps(value, sort_keys=True, separators=(",", ":"))+"\n").encode()
    if path.suffix == ".gz":
        with temporary.open("wb") as stream:
            with gzip.GzipFile(fileobj=stream, mode="wb", mtime=0, compresslevel=2) as compressed:
                compressed.write(data)
    else:
        temporary.write_bytes(data)
    temporary.replace(path)


def file_spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def plain(row):
    return {key: row[key] for key in ("file", "bytes", "sha256")}


def check_spec(row):
    assert isinstance(row["file"], str) and Path(row["file"]).name == row["file"]
    assert row["file"] not in (".", "..") and "\\" not in row["file"]
    assert isinstance(row["bytes"], int) and row["bytes"] >= 0
    assert H64.fullmatch(row["sha256"])


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def identity(item):
    answer = {key: item[key] for key in BASE_KEYS}
    name = item.get("certificate_name")
    if name is not None:
        answer["certificate"] = {"file": name, "sha256": item["files"][name]}
    return answer


def same_identity(left, right):
    for key in BASE_KEYS:
        assert str(left[key]) == str(right[key]), ("Changed original producer", key)
    name = left.get("certificate_name")
    if name is not None and right.get("certificate_name") is not None:
        assert name == right["certificate_name"]
        assert left["files"][name] == right["files"][name]


def topic_path(relative):
    value = (TOPIC/relative).resolve()
    assert value.is_relative_to(TOPIC.resolve())
    return value


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("R824 execution belongs to this public repository's Actions.")


def github(path):
    return json.loads(subprocess.check_output(
        ["gh", "api", "repos/Rogerhu12/math-research-public/"+path], text=True))


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, message, headers, newurl):
        return None


def signed_artifact_url(artifact_id):
    """Keep the temporary signed URL only in memory; do not forward auth headers."""
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    assert token
    url = "https://api.github.com/repos/Rogerhu12/math-research-public/actions/artifacts/"+str(artifact_id)+"/zip"
    request = urllib.request.Request(url, headers={
        "Authorization": "Bearer "+token, "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"})
    opener = urllib.request.build_opener(NoRedirect)
    try:
        response = opener.open(request, timeout=60)
    except urllib.error.HTTPError as error:
        assert error.code in (301, 302, 303, 307, 308)
        location = error.headers["Location"]
        assert location.startswith("https://")
        return location
    else:
        response.close()
        raise AssertionError("Expected a signed artifact redirect.")


class RangeReader(io.RawIOBase):
    """Seekable HTTP Range input, including ZIP64 central-directory reads."""
    def __init__(self, artifact_id, size):
        self.artifact_id, self.size, self.position = artifact_id, int(size), 0
        self.url = signed_artifact_url(artifact_id)
        self.cached_start, self.cached = 0, b""
        self.transferred, self.requests = 0, 0

    def readable(self):
        return True

    def seekable(self):
        return True

    def tell(self):
        return self.position

    def seek(self, offset, whence=io.SEEK_SET):
        value = offset if whence == io.SEEK_SET else \
            self.position+offset if whence == io.SEEK_CUR else self.size+offset
        assert 0 <= value <= self.size
        self.position = value
        return value

    def interval(self, first, stop):
        assert 0 <= first <= stop <= self.size and stop-first <= 64*1024*1024
        if first == stop:
            return b""
        for attempt in range(3):
            request = urllib.request.Request(self.url, headers={
                "Range": "bytes="+str(first)+"-"+str(stop-1),
                "Accept-Encoding": "identity"})
            try:
                with urllib.request.urlopen(request, timeout=60) as response:
                    assert response.status == 206
                    assert response.headers["Content-Range"] == \
                        "bytes "+str(first)+"-"+str(stop-1)+"/"+str(self.size)
                    data = response.read(stop-first+1)
                    assert len(data) == stop-first
                self.transferred += len(data)
                self.requests += 1
                return data
            except urllib.error.HTTPError as error:
                if attempt == 2 or error.code not in (401, 403, 408, 429, 500, 502, 503, 504):
                    raise
                self.url = signed_artifact_url(self.artifact_id)
                time.sleep(attempt+1)
        raise AssertionError("Unreachable Range retry exhaustion.")

    def preload(self, first, stop):
        self.cached_start, self.cached = first, self.interval(first, stop)

    def read(self, size=-1):
        stop = self.size if size < 0 else min(self.size, self.position+size)
        assert stop-self.position <= 64*1024*1024
        if self.cached_start <= self.position <= stop <= self.cached_start+len(self.cached):
            first = self.position-self.cached_start
            data = self.cached[first:first+stop-self.position]
        else:
            data = self.interval(self.position, stop)
        self.position = stop
        return data

    def clear_cache(self):
        self.cached = b""


class Archive:
    def __init__(self, item, directory, whole=False):
        self.item, self.directory = item, Path(directory)
        self.directory.mkdir(parents=True, exist_ok=True)
        artifact = github("actions/artifacts/"+str(item["artifact_id"]))
        run = github("actions/runs/"+str(item["run_id"]))
        assert str(run["id"]) == str(item["run_id"]) and run["head_sha"] == item["source_commit"]
        assert run["status"] == "completed"
        assert run["conclusion"] == item.get("expected_conclusion", "success")
        assert str(artifact["id"]) == str(item["artifact_id"])
        assert artifact["name"] == item["artifact_name"] and artifact["expired"] is False
        assert str(artifact["workflow_run"]["id"]) == str(item["run_id"])
        assert artifact["workflow_run"]["head_sha"] == item["source_commit"]
        assert artifact.get("digest") == "sha256:"+item["archive_sha256"]
        size = int(artifact["size_in_bytes"])
        if "archive_bytes" in item:
            assert size == item["archive_bytes"]
        self.reader = None
        self.whole = whole
        if whole:
            path = self.directory/"artifact.zip"
            if not path.exists():
                temporary = path.with_name("artifact.zip.partial")
                digest, count = hashlib.sha256(), 0
                process = subprocess.Popen(
                    ["gh", "api", "repos/Rogerhu12/math-research-public/actions/artifacts/"+
                     str(item["artifact_id"])+"/zip"], stdout=subprocess.PIPE)
                try:
                    with temporary.open("wb") as destination:
                        for block in iter(lambda: process.stdout.read(4*1024*1024), b""):
                            destination.write(block)
                            digest.update(block)
                            count += len(block)
                    assert process.wait() == 0
                    assert count == size and digest.hexdigest() == item["archive_sha256"]
                    temporary.replace(path)
                except BaseException:
                    process.kill()
                    process.wait()
                    raise
            assert path.stat().st_size == size and sha(path) == item["archive_sha256"]
            self.zip = zipfile.ZipFile(path)
        else:
            self.reader = RangeReader(item["artifact_id"], size)
            self.zip = zipfile.ZipFile(self.reader)
        self.by_name = {}
        infos = []
        for member in self.zip.infolist():
            name = PurePosixPath(member.filename)
            assert not name.is_absolute() and ".." not in name.parts and "\\" not in member.filename
            if member.is_dir():
                continue
            assert not (member.flag_bits & 1), "Encrypted producer members are not accepted."
            self.by_name.setdefault(name.name, []).append(member)
            infos.append(member)
        ordered = sorted(infos, key=lambda member: member.header_offset)
        self.next_offset = {member.header_offset:
                            (ordered[i+1].header_offset if i+1 < len(ordered) else self.zip.start_dir)
                            for i, member in enumerate(ordered)}
        self.record = {"artifact_id": item["artifact_id"], "artifact_name": item["artifact_name"],
            "run_id": item["run_id"], "source_commit": item["source_commit"],
            "advertised_archive_bytes": size,
            "advertised_archive_sha256": item["archive_sha256"],
            "github_artifact_digest_matches_pinned_prior_identity": True,
            "all_archive_bytes_rehashed_in_this_transfer": whole,
            "selected_members_verified_against_original_manifest": True}

    def receipt(self):
        value = dict(self.record)
        if self.reader is not None:
            value["actual_http_range_bytes_transferred"] = self.reader.transferred
            value["actual_http_range_request_count"] = self.reader.requests
        return value

    def extract_bound(self, name, digest, target, expected_bytes=None):
        assert Path(name).name == name and H64.fullmatch(digest)
        target = Path(target)
        if target.exists():
            assert sha(target) == digest
            if expected_bytes is not None:
                assert target.stat().st_size == expected_bytes
            return target
        target.parent.mkdir(parents=True, exist_ok=True)
        for member in self.by_name.get(name, []):
            if expected_bytes is not None and member.file_size != expected_bytes:
                continue
            temporary = target.with_name(target.name+".download")
            actual, count = hashlib.sha256(), 0
            with self.zip.open(member) as source, temporary.open("wb") as destination:
                for block in iter(lambda: source.read(4*1024*1024), b""):
                    actual.update(block)
                    count += len(block)
                    destination.write(block)
            assert count == member.file_size
            if actual.hexdigest() != digest:
                temporary.unlink()
                continue
            temporary.replace(target)
            return target
        raise FileNotFoundError("Bound original member absent: "+name+" "+digest)

    def extract_many(self, requests):
        pending = []
        for name, digest, target, count in requests:
            if Path(target).exists():
                self.extract_bound(name, digest, target, count)
                continue
            members = [value for value in self.by_name.get(name, [])
                       if count is None or value.file_size == count]
            if self.reader is None or len(members) != 1:
                self.extract_bound(name, digest, target, count)
            else:
                member = members[0]
                pending.append((member.header_offset, self.next_offset[member.header_offset],
                                (name, digest, target, count)))
        pending.sort(key=lambda row: row[0])
        groups = []
        for first, stop, request in pending:
            if groups and first-groups[-1][1] <= 1024*1024 and stop-groups[-1][0] <= 32*1024*1024:
                groups[-1][1] = max(stop, groups[-1][1])
                groups[-1][2].append(request)
            else:
                groups.append([first, stop, [request]])
        for first, stop, group in groups:
            if stop-first <= 32*1024*1024:
                self.reader.preload(first, stop)
            for request in group:
                self.extract_bound(*request)
            self.reader.clear_cache()

    def verify_all(self, manifest):
        entries = {row["file"]: row for row in manifest["files"]}
        assert len(entries) == len(manifest["files"])
        assert set(self.by_name) == set(entries) | {"full-outputs-manifest.json", REFERENCE}
        for name, row in entries.items():
            check_spec(row)
            members = self.by_name[name]
            assert len(members) == 1 and members[0].file_size == row["bytes"]
            actual, count = hashlib.sha256(), 0
            with self.zip.open(members[0]) as stream:
                for block in iter(lambda: stream.read(4*1024*1024), b""):
                    actual.update(block)
                    count += len(block)
            assert count == row["bytes"] and actual.hexdigest() == row["sha256"]
        return entries

    def close(self):
        self.zip.close()
        if self.reader is not None:
            self.reader.close()


class Producer:
    """Manifest-verified exact source bytes; only R787 may be a completed checkpoint."""
    def __init__(self, label, item, directory, archive=None):
        self.label, self.item, self.directory, self.archive = label, item, Path(directory), archive
        self.directory.mkdir(parents=True, exist_ok=True)
        self.selected = {}
        manifest_path = self.materialize("full-outputs-manifest.json", item["manifest_sha256"])
        self.manifest = read(manifest_path)
        assert self.manifest["result"] == item["result"]
        self.files = {row["file"]: row for row in self.manifest["files"]}
        assert len(self.files) == len(self.manifest["files"])
        for row in self.files.values():
            check_spec(row)
        run, core, initial = (self.raw(name) for name in META[1:])
        assert run["result"] == core["result"] == initial["result"] == item["result"]
        assert str(run["workflow_run_id"]) == str(item["run_id"])
        assert run["source_commit"] == initial["source_commit"] == item["source_commit"]
        assert initial["source_repository"] == "Rogerhu12/math-research-public"
        assert initial["core_sha256"] == initial["job"]["core_sha256"] == item["core_sha256"]
        assert core["source_sha256"] == item["core_sha256"]
        assert run["core_receipt_sha256"] == self.files["core-receipt.json"]["sha256"]
        certname = item.get("certificate_name")
        if certname is None:
            assert label == "R787" and item["expected_conclusion"] == "failure"
            assert run["complete"] is False and run["process_exit_code"] != 0
            assert core["complete"] is False
            self.certificate = None
            self.tag = self.raw(R787_PREFIX+"chart.json.gz")["configuration"]
        else:
            assert run["complete"] is True and run["process_exit_code"] == 0
            assert core["complete"] is True
            assert core["certificate_sha256"] == item["files"][certname] == self.files[certname]["sha256"]
            self.certificate = self.raw(certname)
            assert self.certificate["result"] == item["result"] and self.certificate["complete"] is True
            self.tag = self.certificate["configuration"]
        assert self.tag["source_sha256"] == item["core_sha256"] and self.tag["python_flint"] == "0.9.0"
        self.initial = initial

    def materialize(self, name, digest, count=None):
        assert Path(name).name == name and H64.fullmatch(digest)
        path = self.directory/name
        if not path.exists():
            try:
                if self.archive is None:
                    raise FileNotFoundError(name)
                self.archive.extract_bound(name, digest, path, count)
            except FileNotFoundError:
                fallback = self.item.get("metadata_repository_paths", {}).get(name)
                assert fallback is not None and name in META
                original = topic_path(fallback)
                assert original.is_file() and sha(original) == digest
                if count is not None:
                    assert original.stat().st_size == count
                shutil.copyfile(original, path)
        assert path.is_file() and sha(path) == digest
        if count is not None:
            assert path.stat().st_size == count
        self.selected[name] = path
        return path

    def raw(self, name):
        entry = self.files[name]
        if name in self.item.get("files", {}):
            assert entry["sha256"] == self.item["files"][name]
        return read(self.materialize(name, entry["sha256"], entry["bytes"]))

    def prefetch(self, names):
        names = sorted(set(names))
        if self.archive is not None:
            self.archive.extract_many([
                (name, self.files[name]["sha256"], self.directory/name, self.files[name]["bytes"])
                for name in names])
        for name in names:
            row = self.files[name]
            self.materialize(name, row["sha256"], row["bytes"])

    def stage(self, entry):
        if isinstance(entry, str):
            entry = self.files[entry]
        assert plain(entry) == plain(self.files[entry["file"]])
        data = self.raw(entry["file"])
        assert data["complete"] is True and data["configuration"] == self.tag
        return data

    def closure_receipt(self):
        return {"producer": self.label, "identity": identity(self.item),
                "files": [file_spec(self.selected[name]) for name in sorted(self.selected)]}


def extract_carrier(bundle, directory, requested, manifests=None):
    """Only exact source-labelled regular files; selected members are then SHA checked."""
    directory = Path(directory)
    wanted = {label: set(names) for label, names in requested.items()}
    seen = set()
    with tarfile.open(bundle, "r|gz") as archive:
        for member in archive:
            if member.isdir():
                continue
            name = PurePosixPath(member.name)
            assert not name.is_absolute() and ".." not in name.parts and "\\" not in member.name
            assert member.isfile() and len(name.parts) == 2
            label, filename = name.parts
            if label not in wanted or filename not in wanted[label]:
                continue
            key = (label, filename)
            assert key not in seen
            seen.add(key)
            target = directory/label/filename
            target.parent.mkdir(parents=True, exist_ok=True)
            expected = None if manifests is None else manifests[label][filename]
            if expected is not None:
                assert member.size == expected["bytes"]
            actual, count = hashlib.sha256(), 0
            temporary = target.with_name(target.name+".download")
            with archive.extractfile(member) as source, temporary.open("wb") as out:
                for block in iter(lambda: source.read(4*1024*1024), b""):
                    out.write(block)
                    actual.update(block)
                    count += len(block)
            assert count == member.size
            if expected is not None:
                assert count == expected["bytes"] and actual.hexdigest() == expected["sha256"]
            if target.exists():
                assert target.stat().st_size == count and sha(target) == actual.hexdigest()
                temporary.unlink()
            else:
                temporary.replace(target)
    return seen


def check_source_links(producers):
    p = producers
    for child in ("R781", "R786"):
        same_identity(p["R787"].tag["retained_artifacts"][child], p[child].item)
    for child in ("R786", "R795", "R799"):
        same_identity(p["R801"].tag["retained_artifacts"][child], p[child].item)
    for child in ("R786", "R795"):
        same_identity(p["R799"].tag["retained_artifacts"][child], p[child].item)
        same_identity(p["R798"].tag["retained_artifacts"][child], p[child].item)
    same_identity(p["R795"].tag["retained_artifacts"]["R786"], p["R786"].item)
    for child in ("R786", "R799"):
        same_identity(p["R805"].tag["retained_artifacts"][child], p[child].item)
    if "R787_complete" in p:
        assert p["R787_complete"].tag == p["R787"].tag


def source_selection_plan(producers):
    p = producers
    needed = {label: set() for label in p}
    r781 = p["R781"]
    c781 = r781.certificate
    assert c781["original_map_index"] == 4 and c781["original_map_degree"] == "1206"
    assert c781["actual_cusp_order"] == 1 and c781["normalized_Laurent_R_bound"] == 142
    assert c781["all_original_real_tangent_phases_verified"] is True
    assert c781["all_recurrence_coefficients_verified_exactly"] is True
    needed["R781"].add("R781-original-real-field-input.json.gz")
    needed["R781"].update("R781-inverse-free-Laurent-"+str(n).zfill(3)+".json.gz" for n in range(143))
    r787 = p["R787"]
    for name, digest in PINNED_OLD.items():
        assert r787.files[name]["sha256"] == digest
    needed["R787"].update("R787-real-power5-row-"+str(i).zfill(4)+".json.gz" for i in range(1234))
    needed["R787"].update(R787_PREFIX+suffix+".json.gz" for suffix in ("selection", "chart", "rational-blocks"))
    needed["R787"].update(R787_PREFIX+"branch-"+str(i).zfill(2)+".json.gz" for i in range(14))
    r786 = p["R786"]
    c786 = r786.certificate
    assert c786["exact_power5_basis_dimension"] == 1234
    assert c786["exact_K_basis_prefix_bound_qY"] == 128
    assert c786["basis_integer_scale"] == str(82**10)
    assert c786["basis_in_original_R775_saved_order"] is True
    index5 = r786.stage(c786["basis_index"])
    assert index5["dimension"] == 1234 and index5["bound_qY"] == 128
    assert [row["index"] for row in index5["basis_rows"]] == list(range(1234))
    needed["R786"].add(c786["basis_index"]["file"])
    needed["R786"].update("R786-exact-power-1-row-"+str(i).zfill(4)+".json.gz" for i in (0, 1, 73))
    needed["R786"].add("R786-exact-power-2-row-0000.json.gz")
    c795, c799, c801 = (p[label].certificate for label in ("R795", "R799", "R801"))
    assert c795["exact_power6_basis_dimension"] == 1506 and c795["exact_K_basis_prefix_bound_qY"] == 81
    assert c799["power6_new_interval"] == [82, 109]
    assert c799["actual_anchor_indices"] == [0, 1, 73]
    assert c799["new_exact_basis_dimensions"] == {"7": 1778, "8": 2050}
    assert c799["three_original_anchor_basepoint_free_input_verified"] is True
    old6 = p["R795"].stage(c795["basis_index"])
    mid6 = p["R799"].stage(c799["power6_tail_index"])
    short7 = p["R799"].stage(c799["basis_indices"]["7"])
    frontier6 = p["R801"].stage(c801["basis_tail_indices"]["6"])
    assert frontier6["coverage_stop"] == 142 and frontier6["dimension"] == 1506
    assert frontier6["integer_scale"] == str(82**12)
    assert short7["dimension"] == 1778 and short7["bound_qY"] == 95
    assert short7["integer_scale"] == str(82**14)
    assert short7["actual_nonzero_minor"] == c799["actual_new_nonzero_minors"]["7"]
    assert short7["characteristic_zero_basis_certified"] is True
    needed["R795"].add(c795["basis_index"]["file"])
    needed["R799"].update((c799["power6_tail_index"]["file"], c799["basis_indices"]["7"]["file"]))
    needed["R801"].add(c801["basis_tail_indices"]["6"]["file"])
    assert [row["index"] for row in old6["basis_rows"]] == list(range(1506))
    assert [row["index"] for row in mid6["basis_rows"]] == list(range(1506))
    assert [row["index"] for row in frontier6["basis_rows"]] == list(range(1506))
    assert [row["index"] for row in short7["basis_rows"]] == list(range(1778))
    for index, row in enumerate(frontier6["basis_rows"]):
        segments = row["original_prefix_segments"]+row["new_tail_segments"]
        cursor = 0
        assert len(row["original_prefix_segments"]) == 2
        assert plain(segments[0]) == plain(old6["basis_rows"][index])
        assert plain(segments[1]) == plain(mid6["basis_rows"][index])
        assert [(value["producer"], value["first"], value["stop"]) for value in segments[:2]] == \
            [("R795", 0, 82), ("R799", 82, 109)]
        for entry in segments:
            label = entry["producer"]
            assert label in ("R795", "R799", "R801")
            assert entry["first"] == cursor < entry["stop"] <= 142
            assert plain(entry) == plain(p[label].files[entry["file"]])
            needed[label].add(entry["file"])
            cursor = entry["stop"]
        assert cursor == 142
    for row in short7["basis_rows"]:
        assert plain(row) == plain(p["R799"].files[row["file"]])
        recipe = row["recipe"]
        assert recipe["kind"] == "product" and recipe["left_power"] == 1 and recipe["right_power"] == 6
        assert recipe["left_index"] in (0, 1, 73) and 0 <= recipe["right_index"] < 1506
        needed["R799"].add(row["file"])
    needed["R798"].add("R798-selected-short-rows.json.gz")
    c805 = p["R805"].certificate
    assert c805["actual_pencil_n"] == 1 and c805["actual_pencil_rank"] == 690
    assert c805["affine_free_module_rank"] == 272
    assert c805["graded_free_basis_degrees"] == [1, 144, 127]
    needed["R805"].add(c805["pencil_stage"]["file"])
    if "R787_complete" in p:
        cert = p["R787_complete"].certificate
        assert cert["exact_nonzero_A_B_relation_verified"] is True
        assert cert["exact_verified_orders"] == 129 and cert["exact_verified_Q_coordinates_per_order"] == 280
        needed["R787_complete"].add(cert["relation_spec"]["file"])
    return needed, {"index5": index5, "frontier6": frontier6, "short7": short7}


def check_selected_source_schemas(producers, needed, indexes):
    p = producers
    field = p["R781"].stage("R781-original-real-field-input.json.gz")["field"]
    prior = "R781-original-real-field-input.json.gz"
    for n in range(143):
        name = "R781-inverse-free-Laurent-"+str(n).zfill(3)+".json.gz"
        row = p["R781"].stage(name)
        assert row["order"] == n and row["exact_differential_identity_at_this_order"] is True
        key = "input_stage_sha256" if n == 0 else "previous_stage_sha256"
        assert row[key] == p["R781"].files[prior]["sha256"]
        assert "R" in row["coefficients"] and "kappa_power" in row["coefficients"]
        prior = name
    assert p["R787"].tag["field"] == field
    assert p["R787"].tag["original_map_index"] == 4 and p["R787"].tag["original_map_degree"] == "1206"
    assert p["R787"].tag["basis_dimension"] == 1234 and p["R787"].tag["basis_integer_scale"] == str(82**10)
    selection = p["R787"].stage(R787_PREFIX+"selection.json.gz")
    chart = p["R787"].stage(R787_PREFIX+"chart.json.gz")
    block = p["R787"].stage(R787_PREFIX+"rational-blocks.json.gz")
    assert chart["actual_modular_rank"] == 1186 and chart["chosen_free_column"] == 1186
    assert len(chart["pivot_rows"]) == len(chart["pivot_columns"]) == 1186
    assert selection["all_14_L_branches_distinct"] is True
    assert selection["all_rational_denominators_units"] is True
    assert selection["all_kappa_reductions_invertible"] is True
    assert len(selection["roots_B_s"]) == 14
    assert block["A_minor_det_mod_prime"] == 336446771
    assert block["B_constant_minor_det_mod_prime"] == 322380492
    assert len(block["A_pivot_rows"]) == 1234
    for branch in range(14):
        data = p["R787"].stage(R787_PREFIX+"branch-"+str(branch).zfill(2)+".json.gz")
        assert data["branch"] == branch and data["actual_Schur_rank"] == 1186
        assert data["roots_B_s"] == selection["roots_B_s"][branch]
        assert data["chart_sha256"] == PINNED_OLD[R787_PREFIX+"chart.json.gz"]
        assert data["all_2560_original_uncleared_rows_verified"] is True
        assert len(data["Schur_minor_inverse_mod_prime"]) == 1186
        assert all(len(row) == 1186 for row in data["Schur_minor_inverse_mod_prime"])
        assert len(data["C_J_pivot_columns"]) == 1234
        assert all(len(row) == 1186 for row in data["C_J_pivot_columns"])
        if branch == 0:
            assert data["selected_minor_det_mod_prime"] == 296007862
            assert data["roots_B_s"] == [3197390, 99932770]
    for i, original in enumerate(indexes["index5"]["basis_rows"]):
        data = p["R787"].stage("R787-real-power5-row-"+str(i).zfill(4)+".json.gz")
        assert data["index"] == i and data["R786_row_sha256"] == original["sha256"]
        assert data["all_original_phase_involutions_verified"] is True
        assert len(data["integer_t_coefficients"]) == 129
        assert all(len(row) == 20 for row in data["integer_t_coefficients"])
    for row in indexes["frontier6"]["basis_rows"]:
        for entry in row["original_prefix_segments"]+row["new_tail_segments"]:
            data = p[entry["producer"]].stage(entry)
            assert data["weight"] == 12 and data["integer_scale"] == str(82**12)
            assert data["all_original_phase_involutions_verified"] is True
            values = data["integer_v_t_coefficients"]
            assert len(values) == entry["stop"]-entry["first"] and all(len(v) == 20 for v in values)
            if entry["producer"] == "R801":
                assert data["node_key"] == row["node_key"] and data["node_fingerprint"] == row["node_fingerprint"]
                assert data["first_exponent"] == entry["first"]
                assert data["last_exponent_exclusive"] == entry["stop"]
            else:
                assert data["index"] == row["index"] and data["recipe"] == row["original_recipe"]
    for row in indexes["short7"]["basis_rows"]:
        data = p["R799"].stage(row)
        assert data["recipe"] == row["recipe"] and data["ordinary_power"] == 7
        assert data["bound_qY"] == 95 and data["integer_scale"] == str(82**14)
        assert len(data["integer_v_t_coefficients"]) == 96
        assert all(len(v) == 20 for v in data["integer_v_t_coefficients"])
    for power, index in ((1, 0), (1, 1), (1, 73), (2, 0)):
        data = p["R786"].stage("R786-exact-power-"+str(power)+"-row-"+str(index).zfill(4)+".json.gz")
        assert data["weight"] == 2*power and data["integer_scale"] == str(82**(2*power))
        assert len(data["integer_qY_xi_coefficients"]) == 129
        assert all(len(row) == 40 for row in data["integer_qY_xi_coefficients"])
    selected = p["R798"].stage("R798-selected-short-rows.json.gz")
    assert len(selected["selected_row_indices"]) == len(set(selected["selected_row_indices"])) == 1506
    assert all(0 <= row < 1640 for row in selected["selected_row_indices"])
    pencil = p["R805"].stage(p["R805"].certificate["pencil_stage"])
    assert pencil["n"] == 1
    if "R787_complete" in p:
        cert = p["R787_complete"].certificate
        row = p["R787_complete"].stage(cert["relation_spec"])
        assert row["exact_original_A_equals_yB"] is True and row["full_129_original_relations_verified"] is True
        assert row["B_nonzero"] is True and row["field"] == field
        assert row["basis_integer_scale"] == str(82**10)
        assert row["R786_basis_index"] == p["R786"].certificate["basis_index"]
        for key in ("A_integer_L_coordinates", "B_integer_L_coordinates"):
            assert len(row[key]) == 1234 and all(len(value) == 14 for value in row[key])
    return {"original_field": field, "original_weight5_rows": 1234,
            "original_weight6_rows": 1506, "original_weight6_intervals": [[0, 82], [82, 109], [109, 142]],
            "original_weight7_short_rows": 1778, "original_R781_last_order": 142,
            "actual_old_Schur_rank": 1186, "actual_old_reserved_free_column": 1186,
            "all14_actual_old_branches_verified_by_source_receipts": True,
            "all_selected_original_files_verified": True,
            "new_arithmetic_executed_by_IO": False}


def expected_configuration(item, producers, indexes, field):
    sources = {}
    for label, source in producers.items():
        if label == "R787_complete":
            continue
        entry = {key: source.item[key] for key in BASE_KEYS}
        name = source.item.get("certificate_name")
        if name is not None:
            entry["certificate"] = plain(source.files[name])
        sources[label] = entry
    return {
        "result": RESULT, "source_sha256": item["core_sha256"], "python_flint": "0.9.0",
        "R824_proof_sha256": item["R824_proof_sha256"], "R824_method_sha256": item["R824_method_sha256"],
        "R781_field_core_sha256": item["field_core_sha256"],
        "source_identities": sources,
        "original_map_index": 4, "original_map_degree": 1206,
        "field": field, "original_basis_dimensions": {"5": 1234, "6": 1506},
        "orders": {"5": 129, "6": 142},
        "original_integer_scales": {"5": str(82**10), "6": str(82**12)},
        "generator_profile_weights_5_6_7": [28, 244, 0],
        "source_degree_sum": 1604, "ambient_epsilon_degree_sum": 398,
        "expected_global_colength": 1206, "reserved_R787_free_column": 1186,
        "R801_power6_frontier": plain(producers["R801"].certificate["basis_tail_indices"]["6"]),
        "R799_power7_short_index": plain(producers["R799"].certificate["basis_indices"]["7"]),
        "R798_selected_rows": plain(producers["R798"].files["R798-selected-short-rows.json.gz"]),
        "operator": "D_N*(246^3*kappa^N*v*A+sum(R_n*kappa^(N-1-n)*v^n)*B) mod v^N",
        "packed_q_stride": 1521, "fixed_field_basis_degree": 280,
        "reconstruction": "strict 2*A*B<ell^digits; whole original relation checked",
        "new_weight7_or_Laurent_tail": False,
        "original_R787_reserved_target_recomputed": False,
    }


def check_files(item):
    assert item["result"] == RESULT and item["p"] == 41
    assert item["producer_inputs_pending"] is False
    assert set(item["retained_sources"]) in (LABELS, LABELS | {"R787_complete"})
    assert item["core_sha256"] == sha(S/item["core"])
    assert item["wrapper_sha256"] == sha(__file__)
    assert item["R824_proof_sha256"] == sha(topic_path(item["proof"]))
    assert item["R824_method_sha256"] == sha(topic_path(item["method"]))
    assert item["field_core_sha256"] == sha(S/item["field_core"])
    assert item["R824_proof_sha256"] == "3a32e69f5ff3fb74ad7b262357e6b9d00da5e1f4348f65b1cdc0705d6fef7be1"
    assert item["field_core_sha256"] == "d024a7a6f5febd4658e8b5b5e5e3659f3c5fcc0daa39d70569ac408ef83a8751"
    if "readme_sha256" in item:
        assert sha(REPO/"README.md") == item["readme_sha256"]["root"]
        assert sha(TOPIC/"README.md") == item["readme_sha256"]["topic"]
    assert item["retained_sources"]["R787"]["certificate_name"] is None
    assert item["retained_sources"]["R787"]["expected_conclusion"] == "failure"
    assert item["retained_sources"]["R787"]["core_sha256"] == \
        "93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04"
    return True


def restore(item, out, retained):
    previous = item.get("resume")
    if previous is None:
        return None
    assert previous["result"] == RESULT and previous["core_sha256"] == item["core_sha256"]
    archive = Archive(previous, out.parent/"resume-download", whole=True)
    try:
        staging = out.parent/"resume-original-metadata"
        staging.mkdir(parents=True, exist_ok=True)
        mp = archive.extract_bound("full-outputs-manifest.json", previous["manifest_sha256"],
                                   staging/"full-outputs-manifest.json")
        manifest = read(mp)
        assert manifest["result"] == RESULT
        entries = archive.verify_all(manifest)
        def old_file(name):
            row = entries[name]
            return archive.extract_bound(name, row["sha256"], staging/name, row["bytes"])
        old_input = read(old_file("public-actions-input.json"))
        old_job = old_input["job"]
        assert old_input["source_commit"] == previous["source_commit"]
        assert old_input["core_sha256"] == item["core_sha256"]
        for key in ("core_sha256", "field_core_sha256", "R824_proof_sha256", "R824_method_sha256"):
            assert old_job[key] == item[key]
        for label in LABELS:
            assert identity(old_job["retained_sources"][label]) == identity(item["retained_sources"][label])
        if "R787_complete" in old_job["retained_sources"]:
            assert identity(old_job["retained_sources"]["R787_complete"]) == \
                identity(item["retained_sources"]["R787_complete"])
        old_run = read(old_file("run-receipt.json"))
        old_core = read(old_file("core-receipt.json"))
        assert old_run["source_commit"] == previous["source_commit"]
        assert str(old_run["workflow_run_id"]) == str(previous["run_id"])
        assert old_run["core_receipt_sha256"] == entries["core-receipt.json"]["sha256"]
        assert old_core["source_sha256"] == item["core_sha256"]
        input_receipt = read(old_file("retained-inputs-receipt.json"))
        bundle = old_file(BUNDLE)
        assert plain(input_receipt["bundle"]) == plain(entries[BUNDLE])
        requested, manifests = {}, {}
        for label, source in input_receipt["producers"].items():
            assert source["identity"] == identity(old_job["retained_sources"][label])
            manifests[label] = {row["file"]: row for row in source["files"]}
            assert len(manifests[label]) == len(source["files"])
            requested[label] = set(manifests[label])
        seen = extract_carrier(bundle, retained, requested, manifests)
        assert seen == {(label, name) for label, names in requested.items() for name in names}
        copied = []
        for name, row in entries.items():
            if name.startswith("R824-") and name.endswith(".json.gz"):
                target = archive.extract_bound(name, row["sha256"], out/name, row["bytes"])
                data = read(target)
                assert data["complete"] is True and data["configuration"] == input_receipt["configuration"]
                copied.append(plain(row))
        receipt = {"result": RESULT, "resumed": True, "previous": previous,
            "archive": archive.receipt(), "all_previous_manifest_files_verified": len(entries),
            "all_previous_selected_bundle_members_verified": len(seen),
            "restored_complete_stage_count": len(copied),
            "restored_complete_stage_files": copied,
            "previous_configuration": input_receipt["configuration"],
            "large_historical_vectors_recomputed": False}
        save(out/"resume-receipt.json", receipt)
        return receipt
    finally:
        archive.close()


def seed_metadata_names(item, label):
    names = set(META)
    if item.get("certificate_name") is not None:
        names.add(item["certificate_name"])
    if label == "R786":
        names.add("R786-exact-power5-basis-index.json.gz")
    elif label == "R795":
        names.add("R795-exact-power6-basis-index.json.gz")
    elif label == "R799":
        names.update(("R799-original-power6-tail-index.json.gz", "R799-original-power7-basis-index.json.gz"))
    return names


def build_input_bundle(out, producers):
    rows = {label: source.closure_receipt() for label, source in sorted(producers.items())}
    temporary = out/(BUNDLE+".tmp")
    with temporary.open("wb") as raw:
        with gzip.GzipFile(fileobj=raw, mode="wb", compresslevel=2, mtime=0) as compressed:
            with tarfile.open(fileobj=compressed, mode="w|") as archive:
                for label, source in sorted(producers.items()):
                    for name, path in sorted(source.selected.items()):
                        info = archive.gettarinfo(str(path), arcname=label+"/"+name)
                        assert info.isfile()
                        info.uid = info.gid = 0
                        info.uname = info.gname = ""
                        info.mtime = 0
                        with path.open("rb") as stream:
                            archive.addfile(info, stream)
    temporary.replace(out/BUNDLE)
    expected = {(label, row["file"]): row for label, source in rows.items() for row in source["files"]}
    seen = set()
    with tarfile.open(out/BUNDLE, "r|gz") as archive:
        for member in archive:
            assert member.isfile()
            name = PurePosixPath(member.name)
            assert len(name.parts) == 2
            key = tuple(name.parts)
            assert key in expected and key not in seen
            seen.add(key)
            row = expected[key]
            actual, count = hashlib.sha256(), 0
            with archive.extractfile(member) as stream:
                for block in iter(lambda: stream.read(4*1024*1024), b""):
                    count += len(block)
                    actual.update(block)
            assert count == member.size == row["bytes"] and actual.hexdigest() == row["sha256"]
    assert seen == set(expected)
    return rows, file_spec(out/BUNDLE)


def prepare(item, out):
    check_files(item)
    out.mkdir(parents=True, exist_ok=True)
    retained = out.parent/"retained"
    retained.mkdir(parents=True, exist_ok=True)
    resumed = restore(item, out, retained)
    producers, archives = {}, {}
    carrier_path = None
    try:
        if resumed is not None:
            for label in LABELS:
                producers[label] = Producer(label, item["retained_sources"][label], retained/label)
            if "R787_complete" in item["retained_sources"] and (retained/"R787_complete"/META[0]).exists():
                producers["R787_complete"] = Producer(
                    "R787_complete", item["retained_sources"]["R787_complete"], retained/"R787_complete")
        else:
            # The live R801 carrier preserves its exact R786/R795/R799 mathematical sources.
            source_item = item["retained_sources"]["R801"]
            archives["R801"] = Archive(source_item, out.parent/"download-R801")
            parent = Producer("R801", source_item, retained/"R801", archives["R801"])
            producers["R801"] = parent
            for label in ("R786", "R795", "R799"):
                same_identity(parent.tag["retained_artifacts"][label], item["retained_sources"][label])
            carrier_name = "R801-retained-producer-inputs.tar.gz"
            carrier_row = parent.files[carrier_name]
            carrier_path = parent.materialize(carrier_name, carrier_row["sha256"], carrier_row["bytes"])
            metadata = {label: seed_metadata_names(item["retained_sources"][label], label)
                        for label in ("R786", "R795", "R799")}
            extract_carrier(carrier_path, retained, metadata)
            for label in ("R786", "R795", "R799"):
                producers[label] = Producer(label, item["retained_sources"][label], retained/label)
            for label in ("R781", "R787", "R798", "R805"):
                source_item = item["retained_sources"][label]
                archives[label] = Archive(source_item, out.parent/("download-"+label))
                producers[label] = Producer(label, source_item, retained/label, archives[label])
        if "R787_complete" in item["retained_sources"] and "R787_complete" not in producers:
            source_item = item["retained_sources"]["R787_complete"]
            archives["R787_complete"] = Archive(source_item, out.parent/"download-R787-complete")
            producers["R787_complete"] = Producer(
                "R787_complete", source_item, retained/"R787_complete", archives["R787_complete"])
        check_source_links(producers)
        needed, indexes = source_selection_plan(producers)
        if carrier_path is not None:
            child_labels = ("R786", "R795", "R799")
            wanted = {label: needed[label] for label in child_labels}
            manifests = {label: producers[label].files for label in child_labels}
            seen = extract_carrier(carrier_path, retained, wanted, manifests)
            # A specifically missing old row is fetched from its same immutable
            # original producer; no completed prefix is regenerated.
            for label, names in wanted.items():
                missing = names-{name for group, name in seen if group == label}
                if missing:
                    archives[label] = Archive(item["retained_sources"][label],
                                              out.parent/("download-missing-"+label))
                    producers[label].archive = archives[label]
                    producers[label].prefetch(missing)
            # Do not nest the old 523 MB carrier in this new minimal bundle.
            producers["R801"].selected.pop("R801-retained-producer-inputs.tar.gz")
        for label, names in needed.items():
            producers[label].prefetch(names)
        schema = check_selected_source_schemas(producers, needed, indexes)
        configuration = expected_configuration(item, producers, indexes, schema["original_field"])
        if resumed is not None:
            assert configuration == resumed["previous_configuration"]
        rows, bundle_spec = build_input_bundle(out, producers)
        receipt = {"result": RESULT, "complete": True, "configuration": configuration,
            "producers": rows, "bundle": bundle_spec,
            "file_count": sum(len(value["files"]) for value in rows.values()),
            "selected_total_bytes": sum(row["bytes"] for value in rows.values() for row in value["files"]),
            "source_schema": schema,
            "archive_subset_transfer_receipts": {label: archive.receipt() for label, archive in archives.items()},
            "all_selected_source_members_and_new_bundle_members_SHA_verified": True,
            "whole_source_archives_rehashed_during_subset_transfer": False,
            "new_mathematics_executed": False}
        save(out/"retained-inputs-receipt.json", receipt)
        if carrier_path is not None:
            carrier_path.unlink()
        if resumed is None:
            save(out/"resume-receipt.json", {"result": RESULT, "resumed": False})
        print("R824_INPUT_REVIEW="+json.dumps({
            "producer_labels": sorted(producers), "file_count": receipt["file_count"],
            "selected_total_bytes": receipt["selected_total_bytes"],
            "bundle": bundle_spec, "original_R781_last_order": 142,
            "actual_old_Schur_rank": 1186, "original_reserved_column": 1186,
            "source_schema_verified": True, "new_mathematics_executed": False}), flush=True)
        return retained, configuration
    finally:
        for archive in archives.values():
            archive.close()


def output_manifest(out):
    for path in out.iterdir():
        if path.is_file() and path.name.endswith((".tmp", ".download", ".partial")):
            path.unlink()
    artifact = "serre-global-"+RESULT+"-"+os.environ["GITHUB_RUN_ID"]+"-"+os.environ["GITHUB_RUN_ATTEMPT"]
    entries = [dict(file_spec(path), artifact=artifact, included_in_git=False)
               for path in sorted(out.iterdir()) if path.is_file()
               and path.name not in ("full-outputs-manifest.json", REFERENCE)]
    save(out/"full-outputs-manifest.json", {"result": RESULT, "files": entries,
        "temporary_active_checkpoint_artifact": artifact,
        "temporary_active_checkpoint_retention_days": 1,
        "reproducible_data_in_git_or_release": False})
    path = out/"full-outputs-manifest.json"
    save(out/REFERENCE, {"result": RESULT, "manifest_file": path.name,
        "manifest_bytes": path.stat().st_size, "manifest_sha256": sha(path),
        "file_count": len(entries), "full_outputs_artifact": artifact,
        "automatic_git_or_release_publication": False})


def integer_matrix(values, rows, columns):
    assert len(values) == rows and all(len(row) == columns for row in values)
    for row in values:
        for value in row:
            assert isinstance(value, str) and INT.fullmatch(value) and value != "-0"


def verify(out):
    """Complete bytes/schema review only; no import of the mathematical core."""
    out = Path(out)
    manifest = read(out/"full-outputs-manifest.json")
    assert manifest["result"] == RESULT
    entries = {row["file"]: row for row in manifest["files"]}
    assert len(entries) == len(manifest["files"])
    assert {path.name for path in out.iterdir() if path.is_file()} == \
        set(entries) | {"full-outputs-manifest.json", REFERENCE}
    for name, row in entries.items():
        check_spec(row)
        assert file_spec(out/name) == plain(row)
    reference = read(out/REFERENCE)
    assert reference["manifest_sha256"] == sha(out/"full-outputs-manifest.json")
    assert reference["manifest_bytes"] == (out/"full-outputs-manifest.json").stat().st_size
    assert reference["file_count"] == len(entries)
    initial, run, core = (read(out/name) for name in ("public-actions-input.json",
                                                   "run-receipt.json", "core-receipt.json"))
    item = initial["job"]
    assert initial["result"] == run["result"] == core["result"] == RESULT
    assert initial["source_repository"] == "Rogerhu12/math-research-public"
    assert initial["source_commit"] == run["source_commit"]
    assert initial["core_sha256"] == item["core_sha256"] == core["source_sha256"]
    assert initial["driver_sha256"] == item["wrapper_sha256"]
    assert run["core_receipt_sha256"] == entries["core-receipt.json"]["sha256"]
    assert run["complete"] is True and run["process_exit_code"] == 0 and core["complete"] is True
    assert core["certificate_sha256"] == entries[FINAL]["sha256"]
    receipt = read(out/"retained-inputs-receipt.json")
    assert receipt["result"] == RESULT and receipt["complete"] is True
    assert plain(receipt["bundle"]) == plain(entries[BUNDLE])
    assert receipt["all_selected_source_members_and_new_bundle_members_SHA_verified"] is True
    retained = out.parent/"retained"
    requested, originals = {}, {}
    for label, source in receipt["producers"].items():
        assert source["identity"] == identity(item["retained_sources"][label])
        originals[label] = {row["file"]: row for row in source["files"]}
        assert len(originals[label]) == len(source["files"])
        requested[label] = set(originals[label])
    seen = extract_carrier(out/BUNDLE, retained, requested, originals)
    assert seen == {(label, name) for label, names in requested.items() for name in names}
    producers = {label: Producer(label, item["retained_sources"][label], retained/label)
                 for label in requested}
    check_source_links(producers)
    needed, indexes = source_selection_plan(producers)
    for label, names in needed.items():
        producers[label].prefetch(names)
    schema = check_selected_source_schemas(producers, needed, indexes)
    configuration = expected_configuration(item, producers, indexes, schema["original_field"])
    assert configuration == receipt["configuration"]
    assert receipt["file_count"] == len(seen)
    assert receipt["selected_total_bytes"] == sum(row["bytes"] for group in originals.values() for row in group.values())
    assert all(set(source.selected) == requested[label] for label, source in producers.items())
    def local(entry):
        assert plain(entry) == plain(entries[entry["file"]])
        value = read(out/entry["file"])
        assert value["complete"] is True and value["configuration"] == configuration
        return value
    cert = read(out/FINAL)
    assert cert["result"] == RESULT and cert["complete"] is True and cert["configuration"] == configuration
    assert cert["completed_requested_scopes"] == item["requested_scopes"]
    stages = local(cert["stage_manifest"])
    actual_stages = {name for name in entries if name.startswith("R824-") and name.endswith(".json.gz")}
    actual_stages.remove(cert["stage_manifest"]["file"])
    assert {row["file"] for row in stages["files"]} == actual_stages
    assert len(stages["files"]) == len(actual_stages)
    for row in stages["files"]:
        assert plain(row) == plain(entries[row["file"]])
        data = read(out/row["file"])
        assert data["complete"] is True and data["configuration"] == configuration
    index = local(cert["generator_index"])
    counts = {5: 0, 6: 0}
    seen_targets = set()
    for target in index["exact_generators"]:
        power, column = target["ordinary_power"], target["free_column"]
        assert power in counts and (power, column) not in seen_targets
        seen_targets.add((power, column))
        counts[power] += 1
        source = target["source"]
        if "producer" in source:
            assert source["producer"] == "R787_complete" and (power, column) == (5, 1186)
            producer = producers["R787_complete"]
            assert plain(source) == plain(producer.certificate["relation_spec"])
            data = producer.stage(source)
            assert data["full_129_original_relations_verified"] is True
        else:
            assert (power, column) != (5, 1186)
            data = local(source)
            assert data["ordinary_power"] == power
            assert data["target_configuration"]["free_column"] == column
            assert data["full_original_relation_orders"] == {5: 129, 6: 142}[power]
            assert data["full_original_t_coordinates"] == 20
            assert data["full_original_Q_coordinates_per_order"] == 280
            assert data["actual_Dixon_digits"] > 0
            expected_order, count = 0, {5: 129, 6: 142}[power]
            for check in data["full_relation_verification_stages"]:
                verified = local(check)
                assert verified["first_order"] == expected_order
                assert expected_order < verified["stop_order"] <= min(expected_order+8, count)
                assert verified["all_original_280_Q_coordinates_zero_at_each_order"] is True
                assert verified["candidate_sha256"] == data["candidate_stage"]["sha256"]
                assert verified["unreduced_product_sha256"] == data["unreduced_product_digest_only"]["sha256"]
                expected_order = verified["stop_order"]
            assert expected_order == count
            operator = local(data["common_clear_operator"])
            assert operator["orders"] == count and operator["ordinary_power"] == power
            integer_matrix(operator["U_integer_coordinates"], count, 280)
            integer_matrix([operator["Q_integer_coordinates"]], 1, 280)
            assert int(operator["common_positive_denominator"]) > 0
            assert operator["all_N_original_relations_equivalent_by_nonzero_row_scalings"] is True
            candidate = local(data["candidate_stage"])
            assert candidate["target_configuration"] == data["target_configuration"]
            assert candidate["A_integer_L_coordinates"] == data["A_integer_L_coordinates"]
            assert candidate["B_integer_L_coordinates"] == data["B_integer_L_coordinates"]
            assert data["original_basis_index"] == plain(
                producers["R786"].certificate["basis_index"] if power == 5 else
                producers["R801"].certificate["basis_tail_indices"]["6"])
        assert data["exact_original_A_equals_yB"] is True and data["B_nonzero"] is True
        assert data["field"] == schema["original_field"]
        assert data["basis_integer_scale"] == str(82**(2*power))
        for key in ("A_integer_L_coordinates", "B_integer_L_coordinates"):
            integer_matrix(data[key], {5: 1234, 6: 1506}[power], 14)
        assert any(value != "0" for row in data["B_integer_L_coordinates"] for value in row)
        assert int(data["common_rational_denominator_cleared"]) > 0
        assert int(data["common_integer_content_removed"]) > 0
    assert counts[5] == cert["exact_weight5_generators"] == index["exact_weight5_generators"]
    assert counts[6] == cert["exact_weight6_generators"] == index["exact_weight6_generators"]
    assert cert["exact_weight7_generators"] == index["exact_weight7_generators"] == 0
    assert cert["global_generator_count"] == sum(counts.values()) == len(seen_targets)
    full = counts == {5: 28, 6: 244}
    assert cert["all_272_generators_exact"] == index["all_272_generators_exact"] == full
    assert index["original_R787_reserved_generator_present"] == ((5, 1186) in seen_targets)
    for row in cert["completed_requested_generators"]:
        assert (row["ordinary_power"], row["free_column"]) in seen_targets
    assert cert["actual_complete_polar_module_certified"] == index["complete_polar_module_certified"]
    if cert["actual_complete_polar_module_certified"]:
        assert full and cert["fiber_certificate"] == index["fiber_certificate"]
        fiber = local(cert["fiber_certificate"])
        assert fiber["actual_nonzero_determinant_mod_prime"] != 0
        assert fiber["actual_square_matrix_size"] == 1778
        assert fiber["generator_weight_counts"] == {"5": 28, "6": 244, "7": 0}
        assert fiber["source_degree_sum"] == cert["weighted_source_degree"] == 1604
        assert fiber["ambient_epsilon_degree_sum"] == cert["ambient_epsilon_degree"] == 398
        assert fiber["actual_global_colength_from_homogeneous_certificate"] == cert["actual_polar_module_colength"] == 1206
        assert fiber["exact_generator_sources"] == index["exact_generators"]
        assert fiber["complete_polar_module_certified_by_R824_and_R822"] is True
        trial = local(fiber["actual_fiber_minor_stage"])
        assert trial["exact_generator_sources"] == index["exact_generators"]
        assert trial["actual_determinant_mod_prime"] == fiber["actual_nonzero_determinant_mod_prime"]
        assert trial["actual_fiber_rank_1778"] is True
        assert trial["rows"] == trial["columns"] == 1778
        for row in trial["source_product_blocks"]:
            local(row)
    else:
        assert cert["actual_polar_module_colength"] is None and cert["fiber_certificate"] is None
    assert cert["original_R787_reserved_target_recomputed"] is False
    assert cert["new_weight7_or_Laurent_tail_computed"] is False
    assert cert["normal_polynomial_ideal_matrices_computed"] is False
    assert cert["radical_or_Jacobian_eta_or_height_computed"] is False
    summary = {"result": RESULT, "full_manifest_files_verified": len(entries),
        "all_retained_bundle_files_verified": len(seen),
        "exact_weight5_generators": counts[5], "exact_weight6_generators": counts[6],
        "actual_complete_polar_module_certified": cert["actual_complete_polar_module_certified"],
        "actual_polar_module_colength": cert["actual_polar_module_colength"],
        "completed_requested_scopes": cert["completed_requested_scopes"],
        "core_seconds": cert["seconds"], "certificate": file_spec(out/FINAL),
        "stage_manifest": cert["stage_manifest"], "generator_index": cert["generator_index"],
        "source_commit": initial["source_commit"], "workflow_run_id": run["workflow_run_id"],
        "new_mathematics_executed_by_verifier": False}
    print("R824_COMPLETE_IO_REVIEW="+json.dumps(summary), flush=True)
    return summary


def compute(item, out):
    guard()
    check_files(item)
    out.mkdir(parents=True, exist_ok=True)
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    for name in (FINAL, "core-receipt.json", "run-receipt.json", "full-outputs-manifest.json", REFERENCE):
        if (out/name).exists():
            (out/name).unlink()
    save(out/"public-actions-input.json", {
        "result": RESULT, "p": 41, "source_repository": "Rogerhu12/math-research-public",
        "source_commit": source, "job": item,
        "core_sha256": sha(S/item["core"]), "field_core_sha256": sha(S/item["field_core"]),
        "proof_sha256": sha(topic_path(item["proof"])), "method_sha256": sha(topic_path(item["method"])),
        "driver_sha256": sha(__file__), "request_sha256": sha(REQUEST),
        "root_readme_sha256": sha(REPO/"README.md"), "topic_readme_sha256": sha(TOPIC/"README.md"),
        "workflow_sha256": sha(REPO/item["workflow"]),
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "original_R787_reserved_target_recomputed": False})
    code, error, process = 1, None, None
    try:
        retained, configuration = prepare(item, out)
        config_path = out.parent/"R824-math-config.json"
        save(config_path, item)
        command = [sys.executable, str(S/item["core"]), "--config", str(config_path),
            "--proof", str(topic_path(item["proof"])), "--method", str(topic_path(item["method"])),
            "--field-core", str(S/item["field_core"]), "--retained", str(retained),
            "--output", str(out), "--budget-minutes", str(item["budget_minutes"])]
        with (out/"core.log").open("wb") as log:
            process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
            try:
                code = process.wait(timeout=60*(float(item["budget_minutes"])+15))
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=45)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                code, error = 124, "Outer budget boundary; completed atomic stages remain reusable."
        if code == 0:
            cert = read(out/FINAL)
            assert cert["complete"] is True and cert["configuration"] == configuration
    except BaseException as failure:
        error = type(failure).__name__+": "+str(failure)
        if process is not None and process.poll() is None:
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.wait(timeout=45)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait()
        code = 1
    finally:
        if not (out/"core-receipt.json").exists():
            save(out/"core-receipt.json", {"result": RESULT, "complete": False,
                "source_sha256": item["core_sha256"], "error": error,
                "mathematical_core_may_not_have_started": process is None,
                "actual_complete_polar_module_certified": False})
        save(out/"run-receipt.json", {"result": RESULT, "p": 41,
            "source_commit": source, "workflow_run_id": os.environ["GITHUB_RUN_ID"],
            "workflow_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
            "process_exit_code": code, "complete": code == 0, "error": error,
            "core_receipt_sha256": sha(out/"core-receipt.json"),
            "execution_environment": "public-repository-github-actions",
            "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
        output_manifest(out)
    print("R824_RUN_RECEIPT="+json.dumps(read(out/"run-receipt.json")), flush=True)
    if (out/"core.log").exists():
        with (out/"core.log").open("rb") as log:
            log.seek(max(0, (out/"core.log").stat().st_size-50000))
            print(log.read().decode("utf-8", errors="replace"), flush=True)
    return code


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--prepare-only", action="store_true")
    args = parser.parse_args()
    sys.set_int_max_str_digits(0)
    if args.verify:
        verify(args.output)
        return 0
    item = read(REQUEST)["job"]
    if args.prepare_only:
        guard()
        prepare(item, args.output)
        return 0
    return compute(item, args.output)


if __name__ == "__main__":
    raise SystemExit(main())
