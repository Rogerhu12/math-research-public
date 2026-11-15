#!/usr/bin/env python3
"""Read one completed public Actions job; never import or execute research code.

Only the original log is downloaded (in memory, at most 80 MiB). This observer
prints a bounded semantic readback, not a reconstructible replacement payload.
Its request and its own source are verified at the observer's GITHUB_SHA.
"""
import argparse
import base64
import datetime as dt
import difflib
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

MODE = "read-only-original-actions-log-v1"
REPORT_SCHEMA = "same159-complete-grid-affine-ef-after-nine-restorations-v1"
STAGE = "metric_height159_complete_affine_stage"
TOPIC = "topics/visible-flex-new-mechanism"
LOG_CAP = 80 * 1024 * 1024
STDOUT_CAP = 90000
TEXT_CAP = 6000
API = "https://api.github.com"
TIME_PREFIX = re.compile(r"^(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?Z)\s+(.*)$")
ANSI = re.compile(r"\x1b\[[0-?]*[ -/]*[@-~]")
SHA40 = re.compile(r"^[0-9a-f]{40}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
ENCODER = json.JSONEncoder(ensure_ascii=False, sort_keys=True,
                          separators=(",", ":"), allow_nan=False)


class ObservationError(RuntimeError):
    pass


def digest(data):
    return hashlib.sha256(data).hexdigest()


def encoded(value):
    # Escape legacy and current Actions command markers inside JSON strings.
    # This changes only JSON spelling, not decoded original text or its hashes.
    return (ENCODER.encode(value).encode("utf-8")
            .replace(b"##[", b"\\u0023\\u0023[")
            .replace(b"::", b"\\u003a\\u003a"))


def fingerprint(value):
    h = hashlib.sha256()
    size = 0
    for piece in ENCODER.iterencode(value):
        data = piece.encode("utf-8")
        size += len(data)
        h.update(data)
    return {"canonical_json_bytes": size, "canonical_json_sha256": h.hexdigest()}


def no_duplicates(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ObservationError("duplicate JSON object key")
        result[key] = value
    return result


def decode_json(data):
    if isinstance(data, bytes):
        data = data.decode("utf-8")
    return json.loads(data, object_pairs_hook=no_duplicates,
                      parse_constant=lambda x: (_ for _ in ()).throw(
                          ObservationError("non-finite JSON constant")))


def require(condition, message):
    if not condition:
        raise ObservationError(message)


def repo_path(value):
    require(isinstance(value, str) and value, "missing repository-relative path")
    p = PurePosixPath(value)
    require(not p.is_absolute() and ".." not in p.parts and str(p) == value,
            "invalid repository-relative path")
    return value


def utc_now():
    return dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class GitHubReader:
    def __init__(self, repository):
        self.repository = repository
        self.token = os.environ.get("GITHUB_TOKEN", "")
        require(bool(self.token), "GITHUB_TOKEN is required for authenticated Actions metadata")
        self.opener = urllib.request.build_opener(NoRedirect())

    def get(self, url, cap, *, api_auth):
        parsed = urllib.parse.urlsplit(url)
        require(parsed.scheme == "https" and parsed.hostname and not parsed.username
                and not parsed.password, "only credential-free HTTPS URLs are accepted")
        headers = {"User-Agent": "original-actions-log-readback",
                   "Accept-Encoding": "identity"}
        if api_auth:
            require(parsed.hostname == "api.github.com", "API credential host mismatch")
            headers.update({"Authorization": "Bearer " + self.token,
                            "Accept": "application/vnd.github+json",
                            "X-GitHub-Api-Version": "2022-11-28"})
        req = urllib.request.Request(url, headers=headers, method="GET")
        try:
            response = self.opener.open(req, timeout=60)
        except urllib.error.HTTPError as error:
            if error.code in (301, 302, 303, 307, 308):
                location = error.headers.get("Location")
                error.close()
                require(bool(location), "redirect without Location")
                return None, urllib.parse.urljoin(url, location)
            code = error.code
            error.close()
            raise ObservationError("HTTP GET failed with status " + str(code)) from None
        except (urllib.error.URLError, TimeoutError):
            raise ObservationError("HTTPS read failed; no signed URL or credential printed") from None
        with response:
            length = response.headers.get("Content-Length")
            if length and length.isdigit():
                require(int(length) <= cap, "HTTP body exceeds configured byte limit")
            data = response.read(cap + 1)
            require(len(data) <= cap, "HTTP body exceeds configured byte limit")
            return data, None

    def api_bytes(self, suffix, cap=2 * 1024 * 1024):
        data, redirect = self.get(API + "/repos/" + self.repository + suffix,
                                  cap, api_auth=True)
        require(redirect is None, "unexpected metadata redirect")
        return data

    def api_json(self, suffix):
        return decode_json(self.api_bytes(suffix))

    def content(self, path, commit, cap):
        suffix = "/contents/" + urllib.parse.quote(repo_path(path), safe="/")
        suffix += "?ref=" + urllib.parse.quote(commit, safe="")
        obj = decode_json(self.api_bytes(suffix, cap * 2 + 8192))
        require(obj.get("type") == "file" and obj.get("encoding") == "base64",
                "expected a small base64 GitHub file")
        data = base64.b64decode(obj["content"], validate=False)
        require(len(data) <= cap, "source or metadata file exceeds its limit")
        return data

    def job_log(self, job_id):
        url = API + "/repos/" + self.repository + "/actions/jobs/" + str(job_id) + "/logs"
        data, location = self.get(url, LOG_CAP, api_auth=True)
        redirects = 0
        while location is not None:
            redirects += 1
            require(redirects <= 4, "too many log redirects")
            # No Authorization header is ever sent after the API response.
            data, location = self.get(location, LOG_CAP, api_auth=False)
        require(data is not None, "empty log response")
        return data, redirects


def git(root, arguments, timeout=120):
    env = dict(os.environ)
    for key in list(env):
        if key in ("GITHUB_TOKEN", "GH_TOKEN", "GIT_ASKPASS", "SSH_ASKPASS") or key.startswith("GIT_CONFIG_"):
            env.pop(key, None)
    env["GIT_TERMINAL_PROMPT"] = "0"
    command = ["git", "-c", "credential.helper=", "-c", "http.extraHeader=",
               "-c", "http.https://github.com/.extraHeader="] + list(arguments)
    result = subprocess.run(command, cwd=root, env=env, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, timeout=timeout, check=False)
    return result.returncode, result.stdout


def git_ok(root, arguments):
    code, out = git(root, arguments)
    require(code == 0, "required Git read failed: " + arguments[0])
    return out


def blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def actual_pull(root, request, source):
    paths = ("README.md", TOPIC + "/README.md")
    expected = request["expected_readme_blobs"]
    require(isinstance(expected, dict) and set(expected) == set(paths),
            "expected_readme_blobs must map exactly the two README repository paths")
    require(all(isinstance(v, str) and SHA40.fullmatch(v) for v in expected.values()),
            "invalid expected README blob")
    before = git_ok(root, ["rev-parse", "HEAD"]).decode().strip()
    original = {p: git_ok(root, ["show", source + ":" + p]) for p in paths}
    started = utc_now()
    code, output = git(root, ["pull", "--rebase",
                              "https://github.com/" + request["repository"] + ".git", "main"])
    finished = utc_now()
    after = git_ok(root, ["rev-parse", "HEAD"]).decode().strip()
    current = {p: git_ok(root, ["show", after + ":" + p]) for p in paths}
    rows = {}
    for path in paths:
        a, b = original[path], current[path]
        difference = "".join(difflib.unified_diff(
            a.decode("utf-8").splitlines(True), b.decode("utf-8").splitlines(True),
            fromfile=source + ":" + path, tofile=after + ":" + path))
        rows[path] = {"expected_blob": expected[path], "source_blob": blob_sha(a),
                      "after_pull_blob": blob_sha(b),
                      "source_sha256": digest(a), "after_pull_sha256": digest(b),
                      "unchanged": a == b, "diff": difference if len(difference) <= TEXT_CAP
                      else {"omitted_text_chars": len(difference),
                            "sha256": digest(difference.encode("utf-8"))}}
    record = {"actual_git_pull": True, "read_only_public_pull": True,
              "command": "git pull --rebase https://github.com/" + request["repository"] + ".git main",
              "started_at": started, "completed_at": finished, "returncode": code,
              "before": before, "after": after, "readmes": rows,
              "git_output_bytes": len(output), "git_output_sha256": digest(output),
              "git_output_last_characters": output.decode("utf-8", errors="replace")[-2500:]}
    record["readmes_match_expected"] = all(
        x["source_blob"] == x["expected_blob"] == x["after_pull_blob"]
        for x in rows.values())
    record["passed"] = code == 0 and record["readmes_match_expected"]
    return record


def scalar(value):
    return value is None or isinstance(value, (str, int, float, bool))


def shape(value, depth=2):
    if isinstance(value, dict):
        return {"type": "dict", "length": len(value),
                "fields": {k: shape(v, depth - 1) if depth > 0 else type(v).__name__
                           for k, v in value.items()}}
    if isinstance(value, list):
        result = {"type": "list", "length": len(value),
                  "element_types": sorted({type(x).__name__ for x in value})}
        dictionaries = [x for x in value if isinstance(x, dict)]
        if dictionaries:
            result["item_fields"] = sorted({k for x in dictionaries for k in x})
        if value and depth > 0 and len(value) <= 16:
            result["items"] = [shape(x, depth - 1) for x in value]
        return result
    if isinstance(value, str):
        return {"type": "str", "length": len(value)}
    return {"type": type(value).__name__}


class Preview:
    def __init__(self):
        self.omissions = []

    def omit(self, value, path, reason, directory=False):
        info = {"path": path, "reason": reason,
                "length": len(value) if hasattr(value, "__len__") else None,
                **fingerprint(value)}
        self.omissions.append(info)
        marker = {"_explicit_omission": True, **{k: v for k, v in info.items() if k != "path"}}
        if directory:
            marker["field_directory_and_shape"] = shape(value, 0)
        return marker

    def compact(self, value, path="$"):
        if isinstance(value, dict):
            return {k: self.compact(v, path + "." + k) for k, v in value.items()}
        if isinstance(value, list):
            if len(value) > 64 or (len(value) > 16 and all(scalar(x) for x in value)):
                return self.omit(value, path, "large array")
            return [self.compact(v, path + "[" + str(i) + "]") for i, v in enumerate(value)]
        if isinstance(value, str) and len(value) > TEXT_CAP:
            return self.omit(value, path, "long text")
        return value

    def field(self, result, key, value, limit, path="$", required=False):
        start = len(self.omissions)
        candidate = self.compact(value, path + "." + key)
        trial = dict(result)
        trial[key] = candidate
        if len(encoded(trial)) <= limit:
            result[key] = candidate
        elif required:
            raise ObservationError("required semantic fields exceed their output budget")
        else:
            del self.omissions[start:]
            result[key] = self.omit(value, path + "." + key,
                                   "focused first readback budget", directory=True)


def source_bindings(report, receipt):
    original = report.get("source_files_sha256")
    require(isinstance(original, dict) and original, "original report has no source hash mapping")
    receipt_files = receipt.get("source_files", {})
    for name, value in original.items():
        require(isinstance(value, str) and SHA256.fullmatch(value), "invalid original source SHA")
        matches = [v for p, v in receipt_files.items() if p == name or p.endswith("/" + name)]
        require(len(matches) == 1 and matches[0].get("sha256") == value,
                "original report source binding disagrees with pinned receipt: " + name)
    return original


def walk_records(value, names, path="$"):
    found = []
    if isinstance(value, dict):
        for key, child in value.items():
            if key in names:
                found.append({"path": path + "." + key, "value": child})
            found.extend(walk_records(child, names, path + "." + key))
    elif isinstance(value, list):
        for i, child in enumerate(value):
            if isinstance(child, (dict, list)):
                found.extend(walk_records(child, names, path + "[" + str(i) + "]"))
    return found


def development_view(report, preview):
    result = {k: v for k, v in report.items()
              if scalar(v) and k != "source_files_sha256"}
    records = walk_records(report, {"checks", "all_passed", "passed", "check_count",
                                   "elapsed_seconds", "maximum_RSS_MiB", "error"})
    records = {item["path"]: item["value"] for item in records}
    preview.field(result, "original_check_records", records, 16000, required=True)
    excluded = {k: v for k, v in report.items() if isinstance(v, (dict, list))
                and k not in ("development", "source_files_sha256")}
    result["unexpanded_development_details"] = preview.omit(
        excluded, "$.unexpanded_development_details",
        "only original checks, counts, times and errors are expanded; source mapping is printed once with actual",
        directory=True)
    result["source_hash_mapping_printed_with_actual"] = fingerprint(report["source_files_sha256"])
    return preview.compact(result)


def actual_view(report, preview):
    result = {k: v for k, v in report.items() if scalar(v)}
    preview.field(result, "source_files_sha256", report["source_files_sha256"], 30000, required=True)
    for key in ("final_selection_validation", "value_evaluation_counts", "error", "pipeline_failure"):
        if key in report:
            preview.field(result, key, report[key], 30000, required=True)
    stage = report.get(STAGE)
    if isinstance(stage, dict):
        selected = {k: v for k, v in stage.items() if scalar(v)}
        for key in ("checkpoint", "solver", "last_pre_LP_decision",
                    "complete_original_row_floor_and_nonlinear_defect_records"):
            if key in stage:
                preview.field(selected, key, stage[key], 12000, path="$." + STAGE)
        remaining = {k: v for k, v in stage.items() if k not in selected}
        selected["unexpanded_stage_fields"] = preview.omit(
            remaining, "$." + STAGE + ".unexpanded_stage_fields",
            "original model human lines and focused directories follow; final grids were already read in observer 43732214112",
            directory=True)
        preview.field(result, STAGE, selected, 30000, required=True)
    skipped = {k: v for k, v in report.items() if k not in result}
    result["unexpanded_top_level_fields"] = preview.omit(
        skipped, "$.unexpanded_top_level_fields",
        "focused model/checkpoint/pull observation; original final gates already consumed from run 43732214112",
        directory=True)
    return result


def model_view(value, preview, path):
    result = {k: v for k, v in value.items() if scalar(v)}
    result["complete_top_level_field_directory"] = shape(value, 1)
    lp = value.get("linear_program")
    if isinstance(lp, dict):
        view = {k: v for k, v in lp.items() if scalar(v)}
        view["field_directory"] = shape(lp, 1)
        for key in ("complete_original_grid_model",
                    "physical_values_or_Jacobians_inside_inner_solver",
                    "primary_step_cost_diagnostic", "error"):
            if key in lp:
                preview.field(view, key, lp[key], 4500, path=path + ".linear_program")
        result["linear_program_focused"] = view
    for key in ("primary_step_cost_diagnostic", "scale_feedback_update", "error"):
        if key in value:
            preview.field(result, key, value[key], 6500, path=path)
    for key in ("trials", "corrections", "affine_spectral_observable_model"):
        if key in value:
            result[key] = preview.omit(value[key], path + "." + key,
                                      "native tables retained; detailed dictionaries not expanded",
                                      directory=True)
    return result


def log_time(text):
    return dt.datetime.fromisoformat(text.replace("Z", "+00:00"))


def parse_log(data, job):
    reports, native_actual, model_records, pull_records = [], [], [], []
    human_lines, publisher_lines = [], []
    human_on = False
    publisher_windows = []
    for step in job.get("steps", []):
        if "publish" in str(step.get("name", "")).lower() and step.get("started_at"):
            publisher_windows.append((log_time(step["started_at"]),
                                      log_time(step["completed_at"]) if step.get("completed_at") else None))
    for number, raw in enumerate(io.BytesIO(data), 1):
        line = raw.decode("utf-8").rstrip("\r\n")
        clean = ANSI.sub("", line)
        match = TIME_PREFIX.match(clean)
        timestamp, body = (match.group(1), match.group(2)) if match else (None, clean)
        identity = {"original_line": number, "timestamp": timestamp}
        if body.startswith("COMPLETE_REPORT "):
            payload = body[len("COMPLETE_REPORT "):]
            obj = decode_json(payload)
            if isinstance(obj, dict) and str(obj.get("schema", "")).startswith(REPORT_SCHEMA):
                require(timestamp is not None, "target COMPLETE_REPORT lacks an original timestamp")
                reports.append({**identity, "payload_sha256": digest(payload.encode("utf-8")),
                                "payload_bytes": len(payload.encode("utf-8")),
                                "payload_hash_basis": "original JSON substring, no log timestamp or line ending",
                                "report": obj})
            continue
        if body.startswith("COMPLETE AFFINE OUTER MODEL "):
            human_on = False
            payload = body[len("COMPLETE AFFINE OUTER MODEL "):]
            obj = decode_json(payload)
            require(isinstance(obj, dict), "native model printer did not emit an object")
            model_records.append({**identity, "payload_sha256": digest(payload.encode("utf-8")),
                                  "model": obj})
            continue
        if body.startswith("COMPLETE AFFINE ACTUAL "):
            human_on = False
            payload = body[len("COMPLETE AFFINE ACTUAL "):]
            native_actual.append({**identity, "payload_sha256": digest(payload.encode("utf-8")),
                                  "report": decode_json(payload)})
            continue
        if "COMPLETE TWO-GRID AFFINE E/F SEPARATION: SAME159/SAME163" in body:
            human_on = True
        if human_on:
            human_lines.append({**identity, "text": body})
        if timestamp and publisher_windows:
            instant = log_time(timestamp)
            if any(start <= instant and (end is None or instant <= end)
                   for start, end in publisher_windows):
                publisher_lines.append({**identity, "text": body})
        if ('"actual_pull"' in body or '"actual_git_pull"' in body) and "{" in body:
            try:
                obj, end = json.JSONDecoder(object_pairs_hook=no_duplicates).raw_decode(
                    body[body.index("{"):])
            except (ValueError, ObservationError):
                continue
            pull_records.append({**identity, "record": obj})
    require(len(reports) == 2, "expected exactly two matching COMPLETE_REPORT records")
    development = [x for x in reports if x["report"]["schema"].startswith(REPORT_SCHEMA + "-development")]
    actual = [x for x in reports if x["report"]["schema"] == REPORT_SCHEMA]
    require(len(development) == len(actual) == 1, "expected one development and one actual report")
    require(development[0]["original_line"] < actual[0]["original_line"],
            "development/actual report order is unexpected")
    return development[0], actual[0], native_actual, model_records, human_lines, publisher_lines, pull_records


def compact_records(records, limit, preview, path, transform=None):
    result = []
    consumed = 0
    for i, record in enumerate(records):
        item = transform(record, i) if transform else preview.compact(record, path + "[" + str(i) + "]")
        size = len(encoded(item)) + 1
        if consumed + size > limit:
            result.append(preview.omit(records[i:], path + "[" + str(i) + ":]",
                                       "focused readback byte budget; remaining original records not expanded",
                                       directory=True))
            break
        result.append(item)
        consumed += size
    return result


def concise_api_record(obj, keys):
    return {k: obj.get(k) for k in keys}


def run(args, context):
    require(os.environ.get("GITHUB_ACTIONS") == "true", "observer is restricted to public GitHub Actions")
    repository = os.environ.get("GITHUB_REPOSITORY", "")
    source = os.environ.get("GITHUB_SHA", "")
    require(re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository) is not None,
            "invalid GITHUB_REPOSITORY")
    require(SHA40.fullmatch(source) is not None, "invalid observer GITHUB_SHA")
    source_path, request_path = repo_path(args.source_path), repo_path(args.request)
    root = Path(git_ok(Path.cwd(), ["rev-parse", "--show-toplevel"]).decode().strip())
    require(Path(__file__).resolve() == (root / source_path).resolve(), "source path is not this observer")
    api = GitHubReader(repository)
    source_bytes = api.content(source_path, source, 100000)
    request_bytes = api.content(request_path, source, 64000)
    require((root / source_path).read_bytes() == source_bytes, "running observer differs from its source commit")
    require((root / request_path).read_bytes() == request_bytes, "request differs from its source commit")
    request = decode_json(request_bytes)
    require(request.get("mode") == MODE, "request mode is not read-only log observation")
    require(request.get("repository") == repository, "request repository mismatch")
    require(request.get("source_sha256") == digest(source_bytes), "observer source SHA256 mismatch")
    original_source = request.get("original_source_commit", "")
    require(isinstance(original_source, str) and SHA40.fullmatch(original_source),
            "invalid original source commit")
    for key in ("original_run_id", "original_job_id"):
        require(str(request.get(key, "")).isdigit() and not isinstance(request.get(key), bool),
                "invalid original run/job ID")
    original_run, original_job = str(request["original_run_id"]), str(request["original_job_id"])
    require(SHA256.fullmatch(request.get("original_receipt_sha256", "")) is not None,
            "invalid original receipt SHA256")
    context["observer_binding"] = {"repository": repository, "source_commit": source,
        "source_path": source_path, "source_sha256": digest(source_bytes),
        "request_path": request_path, "request_sha256": digest(request_bytes),
        "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "github_run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT")}
    pull = actual_pull(root, request, source)
    context["observer_actual_git_pull"] = pull
    require(pull["passed"], "public pull or README identity failed; read-only diff retained in observation error")

    # Receipt and request are both read at the pinned observer commit, not floating main.
    receipt_path = repo_path(request["original_receipt_path"])
    receipt_bytes = api.content(receipt_path, source, 100000)
    require(digest(receipt_bytes) == request["original_receipt_sha256"], "original receipt hash mismatch")
    if "original_receipt_bytes" in request:
        require(len(receipt_bytes) == request["original_receipt_bytes"], "original receipt size mismatch")
    receipt = decode_json(receipt_bytes)
    require(receipt.get("repository") == repository and str(receipt.get("run_id")) == original_run
            and receipt.get("source_commit") == original_source, "original receipt identity mismatch")
    require(receipt.get("lane") == "metric_height159_complete_affine", "unexpected original receipt lane")
    require(receipt.get("publication_policy") == "root-README15-reproducible-outputs-metadata-only",
            "unexpected original receipt publication policy")

    original_run_obj = api.api_json("/actions/runs/" + original_run)
    original_job_obj = api.api_json("/actions/jobs/" + original_job)
    require(str(original_run_obj.get("id")) == original_run and
            original_run_obj.get("head_sha") == original_source, "original run binding mismatch")
    require(str(original_job_obj.get("id")) == original_job and
            str(original_job_obj.get("run_id")) == original_run, "original job binding mismatch")
    if original_job_obj.get("head_sha"):
        require(original_job_obj["head_sha"] == original_source, "original job source mismatch")
    require(original_run_obj.get("status") == original_job_obj.get("status") == "completed",
            "original run/job is not complete")
    require(original_run_obj.get("conclusion") == original_job_obj.get("conclusion") == "success",
            "request binds an original successful run/job; its current metadata disagrees")
    require("metric_height159_complete_affine" in original_job_obj.get("name", ""),
            "original job name does not bind the requested lane")
    context["original_identity"] = {"repository": repository, "run_id": original_run,
                                   "job_id": original_job, "source_commit": original_source}
    context["original_run"] = concise_api_record(original_run_obj,
        ("id", "run_attempt", "name", "event", "head_sha", "status", "conclusion",
         "created_at", "run_started_at", "updated_at", "html_url"))
    context["original_job"] = concise_api_record(original_job_obj,
        ("id", "run_id", "run_attempt", "name", "head_sha", "status", "conclusion",
         "started_at", "completed_at", "html_url"))
    context["original_job_steps"] = [concise_api_record(step,
        ("number", "name", "status", "conclusion", "started_at", "completed_at"))
        for step in original_job_obj.get("steps", [])]
    context["original_receipt"] = {"path": receipt_path, "read_at_commit": source,
        "bytes": len(receipt_bytes), "sha256": digest(receipt_bytes),
        "outputs": receipt.get("outputs"), "original_pulls": receipt.get("pulls"),
        "readmes_read_commit": receipt.get("readmes_read_commit")}
    log, redirects = api.job_log(original_job)
    context["original_log"] = {"bytes": len(log), "sha256": digest(log),
        "downloaded_at": utc_now(), "redirects_without_authorization": redirects,
        "byte_limit": LOG_CAP, "only_in_memory": True, "written_or_uploaded": False}
    dev, actual, native, models, human, publisher, pulls = parse_log(log, original_job_obj)
    real = actual["report"]
    require(real.get("github_sha") == original_source and
            str(real.get("github_run_id")) == original_run and
            real.get("github_repository") == repository, "actual report identity mismatch")
    actual_sources = source_bindings(real, receipt)
    dev_sources = source_bindings(dev["report"], receipt)
    require(actual_sources == dev_sources, "development and actual source mappings differ")
    context["source_binding_check"] = {"all_original_report_sources_match_receipt": True,
                                      "source_count": len(actual_sources),
                                      "development_mapping_equals_actual": True}
    preview_dev, preview_actual, preview_extra = Preview(), Preview(), Preview()
    dev_view = development_view(dev["report"], preview_dev)
    actual_semantic = actual_view(real, preview_actual)
    context["complete_report_count_for_schema"] = 2
    context["original_actual_pull_records"] = compact_records(
        pulls + [{"from_report": which, **item} for which, obj in
                 (("development", dev["report"]), ("actual", real))
                 for item in walk_records(obj, {"actual_pull", "actual_git_pull"})],
        2500, preview_extra, "$.original_actual_pull_records")
    context["native_actual_printer"] = compact_records(native, 3500, preview_extra,
        "$.native_actual_printer")
    context["native_human_printer_lines"] = compact_records(human, 10000, preview_extra,
        "$.native_human_printer_lines")
    context["native_model_record_count"] = len(models)
    context["native_model_directories_and_focused_fields"] = compact_records(
        models, 8000, preview_extra, "$.models",
        transform=lambda row, i: {k: v for k, v in row.items() if k != "model"} |
            {"focused_model": model_view(row["model"], preview_extra, "$.models[" + str(i) + "]")})
    context["publisher_short_log"] = compact_records(
        publisher[-24:], 3000, preview_extra, "$.publisher_short_log")
    context["publisher_log_scope"] = {
        "matched_original_publisher_step_timestamps": True,
        "matched_line_count": len(publisher), "last_lines_requested": 24,
        "earlier_publisher_lines_not_expanded": max(0, len(publisher) - 24)}
    context["extra_omissions"] = preview_extra.omissions
    context["observation_scope"] = {
        "no_science_or_development_executed": True,
        "no_payload_file_artifact_release_or_commit_created": True,
        "original_payloads_only_in_memory": True,
        "models_and_trials_not_fully_expanded": True,
        "source_hashes_only_printed_in_actual_report": True,
        "omission_hashes_describe_unexpanded_original_values_not_validation": True,
        "numerical_claims_not_recomputed_or_certified": True}
    rows = []
    for role, row, semantic, preview in (
            ("development", dev, dev_view, preview_dev),
            ("actual", actual, actual_semantic, preview_actual)):
        rows.append(("ORIGINAL_REPORT_READBACK", {
            "role": role, **{k: v for k, v in row.items() if k != "report"},
            "omissions": preview.omissions, "semanticReport": semantic}))
    rows.append(("ORIGINAL_LOG_OBSERVATION", context))
    rows.append(("ORIGINAL_HUMAN_OBSERVATIONS", {
        "development_passed": dev["report"].get("passed"),
        "actual_status": real.get("status"), "actual_phase": real.get("phase"),
        "original_old_optimizer_calls": real.get("old_optimizer_calls_this_run"),
        "original_new_scientific_solver_calls": real.get("new_scientific_solver_calls"),
        "original_process_total_elapsed_seconds": real.get("process_total_elapsed_seconds"),
        "original_peak_rss_kib_linux": real.get("peak_rss_kib_linux"),
        "readback_only": "Values above are copied from the pinned original reports.",
        "unexpanded_detail": "Original model/trial traces remain unexpanded; directories, hashes and original human printer are supplied."}))
    return rows


def main():
    started = time.monotonic()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", required=True, help="repository-relative pinned request path")
    parser.add_argument("--source-path", default=TOPIC + "/scripts/read_original_actions_log.py")
    args = parser.parse_args()
    context = {"schema": "original-actions-log-semantic-observation-v1",
               "started_at": utc_now(), "stdout_byte_limit": STDOUT_CAP}
    try:
        rows = run(args, context)
        context["observer_elapsed_seconds"] = time.monotonic() - started
        context["completed_at"] = utc_now()
        output = b"".join(label.encode("ascii") + b" " + encoded(value) + b"\n"
                          for label, value in rows)
        if len(output) > STDOUT_CAP:
            minimal = {k: v for k, v in context.items() if k in (
                "schema", "observer_binding", "observer_actual_git_pull", "original_identity",
                "original_log", "source_binding_check", "complete_report_count_for_schema",
                "original_job_steps")}
            minimal.update(status="semantic-output-limit-exceeded",
                           proposed_stdout_bytes=len(output), stdout_byte_limit=STDOUT_CAP,
                           mathematical_execution_performed=False,
                           detail="No report payload was printed, saved, split or uploaded. A narrower semantic selection is required.")
            output = b"ORIGINAL_LOG_STRUCTURE_LIMIT " + encoded(minimal) + b"\n"
            require(len(output) <= STDOUT_CAP, "even failure provenance exceeds output cap")
            sys.stdout.buffer.write(output)
            return 2
        sys.stdout.buffer.write(output)
        return 0
    except Exception as error:
        failure = {"schema": "original-actions-log-observation-error-v1",
                   "error_type": type(error).__name__,
                   "error": str(error)[:1500],
                   "observer_elapsed_seconds": time.monotonic() - started,
                   "context": context,
                   "no_science_or_development_executed": True,
                   "no_original_payload_saved_or_uploaded": True}
        output = b"ORIGINAL_LOG_OBSERVATION_ERROR " + encoded(failure) + b"\n"
        if len(output) > STDOUT_CAP:
            failure["context"] = {k: context[k] for k in
                ("observer_binding", "original_identity", "original_log") if k in context}
            failure["context_explicitly_omitted_due_to_output_cap"] = True
            output = b"ORIGINAL_LOG_OBSERVATION_ERROR " + encoded(failure) + b"\n"
        sys.stdout.buffer.write(output)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
