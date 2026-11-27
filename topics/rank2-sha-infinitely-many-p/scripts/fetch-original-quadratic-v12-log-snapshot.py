#!/usr/bin/env python3
"""Read-only, fixed-binding log snapshot of the single original quadratic v12 job.

No mathematics is recomputed, no workflow is started or retried, and no
files are written. Exact terminal JSON records are hashed and projected
without deriving a mathematical verdict. All API calls are GET. Anonymous public access is tried
first; only an explicitly supplied built-in Actions token can be used as
fallback. Signed download URLs and credentials are never printed.
"""
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.request

if os.environ.get("GITHUB_ACTIONS") != "true" or \
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
    raise SystemExit("This read-only snapshot must run in the named public Actions repository.")

REPO = "Rogerhu12/math-research-public"
RUN = 46033409751
JOB = 140622660136
SOURCE = "048e20343a5f7ec65db9089d824d0635d6815b2b"
API = "https://api.github.com/repos/" + REPO
used_auth = False


class SnapshotError(Exception):
    pass


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def api_get(path, want_redirect=False):
    global used_auth
    token = os.environ.get("RANK2_ACTIONS_READ_TOKEN", "")
    opener = urllib.request.build_opener(NoRedirect())
    for authenticated in (False, True):
        if authenticated and not token:
            break
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "original-quadratic-v12-read-only-log-snapshot",
            "Accept-Encoding": "identity",
        }
        if authenticated:
            headers["Authorization"] = "Bearer " + token
            used_auth = True
        request = urllib.request.Request(API + path, headers=headers, method="GET")
        try:
            response = opener.open(request, timeout=30)
        except urllib.error.HTTPError as exc:
            code = exc.code
            location = exc.headers.get("Location")
            exc.close()
            if code == 302 and want_redirect and location:
                if not location.startswith("https://"):
                    raise SnapshotError("API supplied a non-HTTPS log location")
                return location
            if code in (401, 403) and not authenticated and token:
                continue
            raise SnapshotError("GitHub API HTTP " + str(code))
        if want_redirect:
            response.close()
            raise SnapshotError("Log endpoint did not return its documented 302")
        with response:
            return json.load(response)
    raise SnapshotError("Anonymous API access required authentication; no built-in token was supplied")



# Only exact terminal records from the pinned producer are retained.
# Full JSON bodies are hashed before projecting their scalar fields; the
# collector never substitutes completion of an outer wrapper for nonzero AJ.
RESULT_TAGS = {
    "RANK2_ARTINIAN_CONSUMER_GEOMETRY",
    "RANK2_ARTINIAN_CONSUMER_INTERSECTIONS",
    "RANK2_ARTINIAN_CONSUMER_SHADOW",
    "RANK2_ARTINIAN_CONSUMER",
    "RANK2_TRIANGULAR_ARTINIAN_CONSUMER",
    "RANK2_LINEAR_FIBER_COMPLETE",
    "RANK2_COMPLETE_PROJECTOR_COMPLETE",
    "RANK2_COMPLETE_NATIVE_COMPLETE",
    "RANK2_COMPLETE_QUADRATIC_COMPLETE",
    "RANK2_COMPLETE_PROJECTOR_PRIMARY",
    "RANK2_COMPLETE_NATIVE_ROW",
}
FAILURE_TAGS = {
    "RANK2_LINEAR_FIBER_FAILED",
    "RANK2_COMPLETE_PROJECTOR_FAILED",
    "RANK2_COMPLETE_NATIVE_FAILED",
    "RANK2_COMPLETE_QUADRATIC_FAILED",
    "RANK2_TRIANGULAR_ARTINIAN_FAILED",
}
HOST_STAGES = {
    "offline complete original source solver exited",
    "both original authentication and requested original integral consumer gates succeeded",
    "pipeline incomplete; no mathematical PASS is asserted",
}
SCALAR_KEYS = {
    "kind", "status", "source", "run_id", "run_attempt", "prime", "ell",
    "label", "complete_length", "complete_row_calls", "complete_native_row_calls",
    "complete_original_fallback_row_calls",
    "completed_phase", "requested_trace_method", "completed_trace_method",
    "trace_method", "linear_algebra", "stage", "returncode", "elapsed_seconds",
    "q_precision", "batch_size", "kernel_method", "level",
    "failed_original_stage", "failed_stage", "exception_type", "message",
    "source_genus", "relative_six_genus", "normalization_module_rank_over_ys",
    "original_source_level", "relative_six_level", "RR_base_level", "factor_six",
}
NESTED_KEYS = {
    "complete_phase_receipt_sha256", "readme_blobs",
    "complete_pair_length_accounts", "two_exact_point_detector",
    "all_complete_components",
}
LINE_PATTERN = re.compile(
    rb"^(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?Z) "
    rb"(RANK2_[A-Z0-9_]+) (.*)$")


class TerminalRecords:
    def __init__(self):
        self.pending = b""
        self.records = {}
        self.counts = {}
        self.hashes = {}
        self.host = {}
        self.errors = []
        self.unstructured = []

    def feed(self, chunk):
        lines = (self.pending + chunk).split(b"\n")
        self.pending = lines.pop()
        for line in lines:
            self.line(line.rstrip(b"\r"))

    def line(self, line):
        match = LINE_PATTERN.match(line)
        if match is None:
            if any(token in line for token in (
                    b"TimeoutExpired", b"Process completed with exit code",
                    b"##[error]", b"Traceback (most recent call last)")):
                self.unstructured = (self.unstructured + [
                    line.decode("utf-8", errors="replace")[:600]])[-8:]
            return
        timestamp, raw_tag, payload = match.groups()
        tag = raw_tag.decode("ascii")
        if tag.endswith("_SHA256") and tag[:-7] in RESULT_TAGS:
            self.hashes[tag[:-7]] = payload.decode("ascii", errors="replace")
            return
        base = tag[:-7] if tag.endswith("_RESULT") else tag
        is_result = tag.endswith("_RESULT") and base in RESULT_TAGS
        is_failure = tag in FAILURE_TAGS
        is_host = tag == "RANK2_TRIANGULAR_ARTINIAN_HOST"
        if not (is_result or is_failure or is_host):
            return
        try:
            record = json.loads(payload)
            if not isinstance(record, dict):
                raise ValueError("not a JSON object")
        except Exception as exc:
            self.errors = (self.errors + [{
                "tag": tag, "error": type(exc).__name__,
                "payload_bytes": len(payload),
                "payload_sha256": hashlib.sha256(payload).hexdigest(),
            }])[-8:]
            return
        if is_host and record.get("stage") not in HOST_STAGES:
            return
        fields = {}
        nested = {}
        for key, value in record.items():
            if isinstance(value, bool) or value is None or key in SCALAR_KEYS or key.endswith("_sha256"):
                if isinstance(value, (str, int, float, bool)) or value is None:
                    fields[key] = value if not isinstance(value, str) else value[:2048]
            if key in NESTED_KEYS:
                raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
                if len(raw) <= 6000:
                    nested[key] = value
                else:
                    nested[key] = {"projection_omitted_bytes": len(raw),
                                   "projection_omitted_sha256": hashlib.sha256(raw).hexdigest()}
        summary = {
            "timestamp": timestamp.decode("ascii"),
            "payload_json_bytes": len(payload),
            "payload_json_sha256": hashlib.sha256(payload).hexdigest(),
            "fields": fields, "selected_nested_fields": nested,
            "other_nested_keys": sorted(k for k, v in record.items()
                                        if isinstance(v, (dict, list)) and k not in nested),
        }
        if is_host:
            self.host[record["stage"]] = summary
        else:
            self.counts[base] = self.counts.get(base, 0) + 1
            self.records[base] = summary

    def summary(self):
        out = {}
        for tag, record in self.records.items():
            item = dict(record)
            item["observed_count"] = self.counts[tag]
            item["emitted_payload_sha256"] = self.hashes.get(tag)
            item["emitted_hash_matches"] = (
                self.hashes[tag] == item["payload_json_sha256"]
                if tag in self.hashes else None)
            out[tag] = item
        return {
            "records": out, "host_terminal_stages": self.host,
            "parse_errors": self.errors, "unstructured_terminal_lines": self.unstructured,
            "unfinished_last_line_bytes": len(self.pending),
            "original_mathematical_conclusion_inferred_by_collector": False,
        }


def main():
    run = api_get("/actions/runs/" + str(RUN))
    job = api_get("/actions/jobs/" + str(JOB))
    if run.get("id") != RUN or run.get("head_sha") != SOURCE or \
            job.get("id") != JOB or job.get("run_id") != RUN or \
            job.get("head_sha") != SOURCE:
        raise SnapshotError("Run/job/source binding mismatch")
    location = api_get("/actions/jobs/" + str(JOB) + "/logs", want_redirect=True)

    # Fresh request: no API Authorization header can cross the redirect.
    request = urllib.request.Request(
        location,
        headers={"User-Agent": "original-quadratic-v12-read-only-log-snapshot",
                 "Accept-Encoding": "identity"},
        method="GET")
    digest = hashlib.sha256()
    size = 0
    tail = b""
    terminal = TerminalRecords()
    with urllib.request.urlopen(request, timeout=30) as response:
        encoding = response.headers.get("Content-Encoding", "identity")
        while True:
            chunk = response.read(65536)
            if not chunk:
                break
            digest.update(chunk)
            terminal.feed(chunk)
            size += len(chunk)
            tail = (tail + chunk)[-12000:]
    decoded = tail.decode("utf-8", errors="replace")
    timestamps = re.findall(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?Z", decoded)
    result = {
        "collector_status": "COMPLETE_BYTE_SNAPSHOT",
        "mathematics_recomputed": False,
        "repository": REPO, "original_run": RUN, "original_job": JOB,
        "original_source": SOURCE,
        "run_status": run.get("status"), "run_conclusion": run.get("conclusion"),
        "job_status": job.get("status"), "job_conclusion": job.get("conclusion"),
        "job_started_at": job.get("started_at"), "job_completed_at": job.get("completed_at"),
        "steps": [{"number": s.get("number"), "name": s.get("name"),
                   "status": s.get("status"), "conclusion": s.get("conclusion")}
                  for s in job.get("steps", [])],
        "original_log_bytes": size,
        "original_log_sha256": digest.hexdigest(),
        "response_content_encoding": encoding,
        "tail_last_timestamp": timestamps[-1] if timestamps else None,
        "tail_utf8": decoded,
        "terminal_record_projection": terminal.summary(),
        "built_in_token_fallback_used": used_auth,
    }
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        # A collector/API failure is never a conclusion about the original math.
        message = str(exc) if isinstance(exc, SnapshotError) else type(exc).__name__
        print(json.dumps({
            "collector_status": "API_READ_ERROR",
            "original_mathematics_status": "NOT_ASSESSED",
            "original_run": RUN, "original_job": JOB, "original_source": SOURCE,
            "error": message,
            "built_in_token_fallback_used": used_auth,
        }, sort_keys=True, separators=(",", ":")), file=sys.stderr)
        sys.exit(2)
