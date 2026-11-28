"""The concrete hard-stopped TC terminal, its three original cursors and the reviewed policy overlay."""
import hashlib
import json
import os
from pathlib import Path
import urllib.request

TOPIC = "topics/visible-flex-exact-nearby"
NOTES = TOPIC + "/notes/"
RUN = "46117170011"
JOB = 140893469951
EVENT = "fa24312d2388f164c2e9cb5dd4014d2a83d09ce5"
CHECKOUT = "94ba02707d2d9de81316cc1e4e4bdfe650ec20ce"
DIR = NOTES + "true_root_trial_residual_ci/run-" + RUN + "-1"
REPO = "Rogerhu12/math-research-public"
RUN_API = NOTES + "2026-11-28-TCF-terminal-46117170011-run-API.json"
JOBS_API = NOTES + "2026-11-28-TCF-terminal-46117170011-jobs-API.json"
MARKER = NOTES + "true_root_trial_residual_ci/consumed-complete2677.json"
RULES = NOTES + "2026-11-28-read-public-model-ultra-rules.json"
OLD_RULES = NOTES + "2026-11-20-reviewed-public-CI-rules.json"
INPUTS = {
    "TC_terminal_run_API": (RUN_API, 13310, "e86f4e95b51c81a701472a572c27f1e4990cf57f5f2f098dbaf99f9b50167212"),
    "TC_terminal_jobs_API": (JOBS_API, 2746, "ff13ebdb36e4c1d061f026177bb50b49dca2a43003e2c0e8b4ed498cbae59a8e"),
    "TC_original_consumed": (MARKER, 688, "f44f8e6333d3df433c671671d4953c9ded679c00bb3bdc16962a6f380b178254"),
    "TC_current_reviewed_rules": (RULES, 2649, "32fa03fbdb357d7d5a98b7115a24acc10f218705a1ecdef2e756ff73284098ce"),
    "TC_original_reviewed_rules": (OLD_RULES, 2112, "26da0165d2a7ec5f968959332c9fd04aae7259059de2b56f41e76b49b61fc051"),
}
TERMINAL = {
    "state": (44834, "dbfd8d879eab2352dd02c32eac6f63b4cf24ee2d70f7f078a622b39ad666996e"),
    "prefix": (9552, "dcf1bc35d5ed91cf71ee91174f78c81cde6a5b8902643e87014d08b9b3f43634"),
    "matrix": (13137, "f2cc92916a9d39e9f8f418861029de00b7b973aef09384a00c339edfad1cd247"),
    "execution": (30853, "976dfe7a95d0073bc67825cb7d207bbc119a8950b27c73fabeed21f43edbaba3"),
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def read(root, spec):
    path, size, digest = spec
    raw = (Path(root) / path).read_bytes()
    require(len(raw) == size and sha(raw) == digest, "complete terminal ancestor " + path)
    return raw


def job_record(jobs):
    require(jobs["total_count"] == len(jobs["jobs"]) == 1, "all jobs in the original attempt")
    j = jobs["jobs"][0]
    expected = {"id": JOB, "run_id": int(RUN), "run_attempt": 1, "name": "complete-new-finite-trial-objects",
                "head_sha": EVENT, "status": "completed", "conclusion": "failure",
                "started_at": "2026-11-28T06:33:38Z", "completed_at": "2026-11-28T11:16:03Z"}
    require(all(j[key] == val for key, val in expected.items()), "the final real original public runner job")
    return expected


def hard_stopped(root, record, raw):
    # This path accepts only these four complete original terminal objects and the one historical runner.
    for key, (size, digest) in TERMINAL.items():
        require(len(raw[key]) == size and sha(raw[key]) == digest, "actual final TC " + key)
    docs = {role: json.loads(read(root, spec)) for role, spec in INPUTS.items()}
    run = docs["TC_terminal_run_API"]
    require(run["id"] == int(RUN) and run["run_attempt"] == 1 and run["head_sha"] == EVENT
            and run["status"] == "completed" and run["conclusion"] == "failure"
            and run["updated_at"] == "2026-11-28T11:16:04Z" and run["repository"]["full_name"] == REPO,
            "actual complete original run and event")
    job_record(docs["TC_terminal_jobs_API"])
    e, s, m = (json.loads(raw[key]) for key in ("execution", "state", "manifest"))
    marker = docs["TC_original_consumed"]
    require(marker["run_id"] == e["run_id"] == s["run_id"] == RUN
            and marker["run_attempt"] == e["run_attempt"] == s["run_attempt"] == "1"
            and marker["manifest_sha256"] == e["manifest_sha256"] == sha(raw["manifest"])
            and marker["problem_id"] == e["problem_id"] == m["problem_id"]
            and marker["output_directory"] == DIR and marker["automatic_scientific_retry"] is False
            and e["event_commit"] == s["workflow_event_commit"] == EVENT
            and s["actual_checkout_commit"] == e["actual_scientific_checkout"]
                == e["consumed_marker_publication"]["commit"] == CHECKOUT
            and e["actual_child_returncode"] == -9 and e["child_timeout"] is False
            and s["actual_returncode"] is s["failure"] is None
            and e["failure"]["type"] == "ValueError" and e["failure"]["message"] ==
                "README changed: preserve prefix and apply the printed change before further science"
            and e["scientific_finished_utc"] == "2026-11-28T11:15:55.948406+00:00"
            and e["finished_utc"] == "2026-11-28T11:15:55.963524+00:00",
            "actual killed scientific parent, its exclusive marker and the final whole publication failure")
    require(record["child_outcomes"] == [] and record["seed_prefix"]["next_cell"] == 992
            and [(x["first_cell"], x["next_cell"], x["stop_cell"]) for x in record["slices"]] ==
                [(992,1952,3236), (3236,4080,5480), (5480,6296,7724)]
            and record["accepted_union_complete_cells"] == e["parallel_accepted_complete_cells"] == 3612
            and record["contiguous_next_cell"] == e["qualified_complete_cells"] == 1952,
            "genuine complete seed+three accepted slices; no invented per-process exit status")
    return True


def current_policy(root, original_spec, original_raw):
    old = json.loads(read(root, INPUTS["TC_original_reviewed_rules"]))
    raw = read(root, INPUTS["TC_current_reviewed_rules"])
    new = json.loads(raw)
    require(original_raw == (Path(root)/OLD_RULES).read_bytes()
            and all(new["supersedes_review"][k] == original_spec[k] for k in ("path","git_blob_sha","sha256","bytes"))
            and new["previously_read_readme_sha256"] == old["readme_sha256"]
            and new["large_data_policy"] == old["large_data_policy"]
            and new["model"] == "gpt-6.2-astra" and new["reasoning_effort"] == "ultra"
            and new["new_unread_rules_must_still_be_reported_and_applied"] is True,
            "the original whole review and its exact independently read rule-16 successor")
    return {"path": RULES, "bytes": len(raw), "sha256": sha(raw),
            "git_blob_sha": hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()}


def live_job():
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = "Bearer " + token
    url = "https://api.github.com/repos/"+REPO+"/actions/runs/"+RUN+"/attempts/1/jobs?per_page=100"
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60) as response:
        raw = response.read()
    return {"bytes": len(raw), "sha256": sha(raw), "terminal_job": job_record(json.loads(raw))}
