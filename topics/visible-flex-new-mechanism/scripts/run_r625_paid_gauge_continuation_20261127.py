#!/usr/bin/env python3
"""Original Actions rules/runtime plus one read-only paid-log memory preload.

The source log is fetched before credentials are removed, then delivered to
the scientific child through stdin. Neither credentials nor raw files are
given to that child; the original published launcher remains unchanged.
"""
from __future__ import annotations

import argparse
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request

import run_inverse_rotational_metric_20261126 as original


class NoCrossHostAuthorization(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, message, headers, newurl):
        target = super().redirect_request(request, fp, code, message, headers, newurl)
        if (target is not None and urllib.parse.urlparse(request.full_url).netloc
                != urllib.parse.urlparse(newurl).netloc):
            target.remove_header("Authorization")
        return target


def preload_paid_log(request):
    started = time.monotonic()
    source = request["paid_source"]
    token = os.environ.get("MR_TOKEN")
    original.require(bool(token), "MR_TOKEN is required for the paid public job-log preload")
    url = ("https://api.github.com/repos/"+original.REPOSITORY+"/actions/jobs/"
           +str(source["job_id"])+"/logs")
    query = urllib.request.Request(url, headers={
        "Authorization":"Bearer "+token, "Accept":"application/vnd.github+json",
        "X-GitHub-Api-Version":"2022-11-28"})
    opener = urllib.request.build_opener(NoCrossHostAuthorization())
    with opener.open(query, timeout=45) as response:
        raw = response.read()
    digest = original.sha256(raw)
    original.require(len(raw)==source["log_bytes"] and digest==source["log_sha256"],
                     "The paid source log bytes or hash differ")
    receipt = {"run_id":source["run_id"], "job_id":source["job_id"],
               "bytes":len(raw), "sha256":digest, "seconds":time.monotonic()-started,
               "scientific_computations":0, "old_job_log_downloads":1,
               "raw_file_or_artifact_saved":False, "scientific_child_receives_credentials":False}
    original.emit("PAID_SOURCE_PRELOAD", receipt)
    return raw, receipt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", required=True)
    parser.add_argument("--lane", required=True)
    args = parser.parse_args()
    root = Path.cwd()
    source = os.environ["GITHUB_SHA"]
    original.require(re.fullmatch(r"[0-9a-f]{40}", source) is not None,
                     "invalid Actions source commit")
    raw_request = Path(args.request).read_bytes()
    request = json.loads(raw_request)
    original.require(request["repository"]==original.REPOSITORY, "repository identity differs")
    original.require(args.lane in request["lanes"], "unknown continuation lane")
    original.require(platform.python_version()==request["runtime"]["python"], "Python version differs")
    try:
        public_after = original.public_pull(root, request, source)
        private_after = original.private_pull(request)
        paid_log, preload_receipt = preload_paid_log(request)
    finally:
        for name in ("MR_TOKEN", "GITHUB_TOKEN", "GH_TOKEN"):
            os.environ.pop(name, None)
    original.git(root, "checkout", "--detach", source)
    original.require(Path(args.request).read_bytes()==raw_request, "request differs at pinned source")
    bindings = {}
    for path, expected in request["source_sha256"].items():
        actual = original.sha256(Path(path).read_bytes())
        original.require(actual==expected, "source hash differs: "+path)
        bindings[path] = actual
    parameters = dict(request["common_parameters"])
    parameters.update(request["lanes"][args.lane])
    command = [sys.executable, request["entry_point"]]
    for name, value in parameters.items():
        option = "--"+name.replace("_", "-")
        if isinstance(value, bool):
            if value:
                command.append(option)
        else:
            command.extend((option, str(value)))
    original.emit("SOURCE", {"source_commit":source, "run_id":os.environ["GITHUB_RUN_ID"],
        "run_attempt":os.environ["GITHUB_RUN_ATTEMPT"], "lane":args.lane,
        "public_rules_read_commit":public_after, "private_rules_read_commit":private_after,
        "request_path":args.request, "request_bytes":len(raw_request),
        "request_sha256":original.sha256(raw_request), "source_sha256":bindings,
        "parameters":parameters, "command":command, "runtime":request["runtime"],
        "old_scope_replayed":False, "paid_source_preparation":preload_receipt})
    packages = request["runtime"]["packages"]
    subprocess.run([sys.executable, "-m", "pip", "install", "--disable-pip-version-check",
        "--no-cache-dir", *[name+"=="+version for name, version in packages.items()]], check=True)
    actual_versions = {name:importlib.metadata.version(name) for name in packages}
    original.require(actual_versions==packages, "installed numerical versions differ")
    original.emit("RUNTIME", {"python":platform.python_version(), "packages":actual_versions,
                             "credentials_removed_before_science":True})
    science_input = (json.dumps({"source_preparation":preload_receipt}, sort_keys=True,
                               allow_nan=False).encode()+b"\n"+paid_log)
    started = original.utc()
    result = subprocess.run(command, input=science_input, check=False)
    original.emit("FINISHED", {"lane":args.lane, "started_at":started,
        "completed_at":original.utc(), "returncode":result.returncode, "stdout_only":True,
        "paid_source_raw_delivered_only_in_memory":True,
        "frozen_metric_convergence_claim":False, "README_completion_claim":False})
    return result.returncode


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        original.emit("ERROR", {"type":type(error).__name__, "message":str(error)})
        raise SystemExit(2) from None
