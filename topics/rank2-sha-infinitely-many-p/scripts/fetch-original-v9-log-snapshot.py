#!/usr/bin/env python3
"""Read-only, fixed-binding log snapshot of the single original v9 job.

No mathematics is recomputed, no workflow is started or retried, and no
files are written. All API calls are GET. Anonymous public access is tried
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
RUN = 45920983633
JOB = 140251398928
SOURCE = "1eeab95eb057de2b6ea6753ff9e36a18bd20bbd2"
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
            "User-Agent": "original-v9-read-only-log-snapshot",
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
        headers={"User-Agent": "original-v9-read-only-log-snapshot",
                 "Accept-Encoding": "identity"},
        method="GET")
    digest = hashlib.sha256()
    size = 0
    tail = b""
    with urllib.request.urlopen(request, timeout=30) as response:
        encoding = response.headers.get("Content-Encoding", "identity")
        while True:
            chunk = response.read(65536)
            if not chunk:
                break
            digest.update(chunk)
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
