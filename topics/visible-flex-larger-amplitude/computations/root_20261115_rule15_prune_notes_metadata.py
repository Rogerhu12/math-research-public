#!/usr/bin/env python3
"""Request104: Git-tree-only cleanup, read-only unless --apply is explicit.

All generated inventory files are temporary operational files. Do not commit or
upload them. Commit this script, its small recipe, the run id and output hashes.
The authorized Actions --apply path makes an ordinary deletion commit, never a force push.
Only its own compact bookkeeping note is written; H/open/log are not edited.
"""
from __future__ import annotations
import argparse
import base64
import concurrent.futures
import collections
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request

SCHEMA = "rule15-notes-tree-metadata-prune-inventory-v1"
TOPIC = "topics/visible-flex-larger-amplitude"
NOTES = TOPIC + "/notes"
BASE_COMMIT = "52704ecdfc84f1d67c8a3cf6233d910f46582844"
REPOSITORY = "Rogerhu12/math-research-public"
READMES = {
    "README.md": "74c08a36f6c997d0bc1e64a7956b42276f5fa5d7",
    TOPIC + "/README.md": "bff8aea253a9e6a7a4fac28d810ac454c5499fec",
}
NOTES_TREE = "3832eb52ca0b5414ab761a47fd6774497695b431"
HISTORY_REF = "8bd267107cc8710d371f3b62c02986655ac965b0"
EXPECTED = {
    "files": 14551, "bytes": 2789284775,
    "delete_files": 8184, "delete_bytes": 2641928364,
    "keep_files": 6367, "keep_bytes": 147356411,
    "metadata_tsv_sha256":
        "53e551c2075176798781a879bd0f5c45d0196f9aa166d9bf13ec831c96e9b488",
    "deletion_tsv_sha256":
        "7b725628c3fb394d2d22f0fe7cbac28b7238bfac0d13a06227b1481804f450f0",
    "deletion_paths_nul_sha256":
        "289ac88afec320e42045f1928b4112a625e7dca70ff35bbf1c5fd7ede0371625",
}
INPUT_RECOVERY = [
    {
        "role": "original_accepted96",
        "path": NOTES + "/public-actions-43580643038-1-free3/stage-00/actual.json.gz",
        "bytes": 2614352,
        "sha256": "b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff",
        "disposition": "remove_from_main_if_OID_matches; historical_bootstrap_only",
    },
    {
        "role": "original_prepared112",
        "path": NOTES + "/public-actions-43588155190-1-prepare112/preparation112/prepared.json.gz",
        "bytes": 4220043,
        "sha256": "0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714",
        "disposition": "remove_from_main_if_OID_matches; historical_bootstrap_only",
    },
    {
        "role": "original_zero_T112_anchor",
        "path": NOTES + "/public-actions-43592195185-1-coupling112banded/full-DN112/outer-00-anchor-tail.json.gz",
        "bytes": 6815,
        "sha256": "e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51",
        "disposition": "remove_from_main_if_OID_matches; historical_bootstrap_only",
    },
    {
        "role": "original_T112_parameters",
        "path": NOTES + "/public-actions-43588155190-1-prepare112/T112-config.json",
        "bytes": 2161,
        "sha256": "01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5",
        "disposition": "keep_in_main_as_parameters",
    },
    {
        "role": "request101_actual99_parent_status",
        "path": NOTES + "/public-actions-43677789194-1-smallcoreresonance/small-core-inexact-p3-restoration/inexact-p3-restoration-status.json",
        "bytes": 971400,
        "sha256": "9b4cf9f1c7488ef310f38fcecccdeee7a8883c276d9cba351bf8f0bc2185fe82",
        "disposition": "remove_from_main_if_OID_matches; historical_bootstrap_only",
    },
]
def need(value, message):
    if not value:
        raise RuntimeError(message)

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def classify(path, mode):
    # Only actual ordinary blob paths can become deletion candidates.
    if mode not in ("100644", "100755"):
        return "keep-unknown"
    name = path.rsplit("/", 1)[-1].lower()
    if name == ".gitkeep" or re.search(
            r"\.(md|rst|tex|py|js|mjs|cjs|sh|yaml|yml|toml|diff)$", name):
        return "keep-code-conclusion"
    if re.search(
            r"(?:^|[-_.])(manifest|receipt|provenance|identity|identities|dependencies|request|recipe)(?:[-_.]|$)",
            name) and re.search(r"\.json(?:l)?(?:\.gz)?$", name):
        return "keep-identity-manifest"
    if (re.search(
            r"(?:^|[-_])(config|configuration|params|parameters|spec|plan|intent|profile|commands|command)\.json(?:\.gz)?$",
            name)
        or re.search(r"^(package|package-lock)\.json$", name)
        or re.search(
            r"^(input-binding|source-origin|source-dependencies|input-and-source-identity|public-artifacts)\.json(?:\.gz)?$",
            name)):
        return "keep-parameters"
    if re.search(r"\.(gz|zip|tar|npz|npy|bin|f64|f64le|i32)$", name):
        return "delete-generated-raw"
    if re.search(r"\.(jsonl|log|txt)$", name) and not re.search(
            r"readme|license|requirements|citation", name):
        return "delete-generated-log"
    if path.startswith("public-actions-") and name.endswith(".json"):
        return "delete-actions-json-output"
    if name.endswith(".json") and re.search(
            r"(?:^|[-_.])(summary|status|result|report|readout|diagnostic|certificate|check|audit|trial|step|iteration|coeff|spectrum|cache|operator|direction|field|hessian|jacobian|residual|checkpoint|boundary|equations?)(?:[-_.]|$)",
            name):
        return "delete-named-computation-json"
    return "keep-unknown"

_TREE_CACHE = {}

def api_tree(tree_sha, recursive=False):
    need(re.fullmatch(r"[0-9a-f]{40}", tree_sha), "Invalid tree SHA")
    cache_key = (tree_sha, recursive)
    if cache_key in _TREE_CACHE:
        return _TREE_CACHE[cache_key]
    url = "https://api.github.com/repos/" + REPOSITORY + "/git/trees/" + tree_sha
    if recursive:
        url += "?recursive=1"
    headers = {"Accept": "application/vnd.github+json",
               "X-GitHub-Api-Version": "2022-11-28",
               "User-Agent": "rule15-request104-metadata-only"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = "Bearer " + token
    for attempt in range(6):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers),
                                        timeout=60) as response:
                data = json.load(response)
            need(data.get("sha") == tree_sha and isinstance(data.get("tree"), list),
                 "GitHub tree identity mismatch")
            _TREE_CACHE[cache_key] = data
            return data
        except urllib.error.HTTPError as exc:
            if exc.code not in (403, 404, 429, 500, 502, 503, 504) or attempt == 5:
                raise RuntimeError("Metadata API HTTP " + str(exc.code)) from None
        except (TimeoutError, urllib.error.URLError):
            if attempt == 5:
                raise RuntimeError("Metadata API transport did not complete") from None
        time.sleep(min(16, 2 ** attempt))
    raise RuntimeError("Unreachable tree fetch failure")

def safe_path(path):
    need(isinstance(path, str) and path and not path.startswith("/") and
         ".." not in path.split("/") and not any(c in path for c in "\0\t\r\n"),
         "Unsafe metadata path")

def api_rows(tree_sha):
    data = api_tree(tree_sha, recursive=True)
    if data.get("truncated"):
        data = api_tree(tree_sha, recursive=False)
        need(not data.get("truncated"), "Even a direct tree is truncated")
        rows = []
        children = [row for row in data["tree"] if row["type"] == "tree"]
        for row in data["tree"]:
            if row["type"] == "blob":
                rows.append(dict(row))
            else:
                need(row["type"] == "tree", "Unexpected submodule in cleanup scope")
        def child_rows(child):
            return [dict(row, path=child["path"] + "/" + row["path"])
                    for row in api_rows(child["sha"])]
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
            for result in pool.map(child_rows, children):
                rows.extend(result)
        # Recursive child results below are already normalized; normalize once.
        normalized = []
        for row in rows:
            if "git_blob_sha1" in row:
                normalized.append(row)
            else:
                normalized.append(normalize_api_blob(row))
        return sorted(normalized, key=lambda row: row["path"].encode("utf-8"))
    rows = [normalize_api_blob(row) for row in data["tree"] if row["type"] == "blob"]
    need(all(row["type"] in ("blob", "tree") for row in data["tree"]),
         "Unexpected submodule in cleanup scope")
    rows.sort(key=lambda row: row["path"].encode("utf-8"))
    need(len({row["path"] for row in rows}) == len(rows), "Duplicate API tree path")
    return rows

def normalize_api_blob(row):
    safe_path(row["path"])
    need(isinstance(row.get("size"), int) and row["size"] >= 0 and
         re.fullmatch(r"[0-9a-f]{40}", row["sha"]), "Missing blob metadata")
    return dict(path=row["path"], mode=row["mode"], git_blob_sha1=row["sha"],
                bytes=row["size"])

def git_process(repo, args, input_bytes=None, check=True):
    env = dict(os.environ)
    env["GIT_OPTIONAL_LOCKS"] = "0"
    env["GIT_NO_LAZY_FETCH"] = "1"
    token = env.get("GITHUB_TOKEN")
    # Disable inexact rename discovery for every Git subprocess, including
    # pull/rebase, so a mass deletion cannot request promisor data for similarity.
    config = [("merge.renames", "false"), ("diff.renames", "false")]
    if token:
        # Authentication exists only in process environment; never in a file.
        config.append(("http.https://github.com/.extraheader",
            "AUTHORIZATION: basic " + base64.b64encode(
                ("x-access-token:" + token).encode()).decode()))
    inherited_count = int(env.get("GIT_CONFIG_COUNT", "0"))
    need(inherited_count >= 0, "Invalid inherited Git process configuration")
    for index, (key, value) in enumerate(config, inherited_count):
        env["GIT_CONFIG_KEY_" + str(index)] = key
        env["GIT_CONFIG_VALUE_" + str(index)] = value
    env["GIT_CONFIG_COUNT"] = str(inherited_count + len(config))
    process = subprocess.run(["git", "-C", str(repo), *args], check=False,
                             input=input_bytes, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, env=env)
    if check and process.returncode:
        # Git's stderr has no supplied token/credential argument.
        message = process.stderr.decode("utf-8", "replace")
        if token:
            message = message.replace(token, "[REDACTED]")
        raise RuntimeError("Git command failed (" + args[0] + "): " + message)
    return process

def git(repo, args, input_bytes=None):
    return git_process(repo, args, input_bytes).stdout

def git_rows(repo, treeish, pathspec):
    # DO NOT add -l: in a partial clone that can hydrate promisor blobs for sizes.
    raw = git(repo, ["ls-tree", "-r", "-z", treeish, "--", pathspec])
    result = []
    for record in raw.split(b"\0"):
        if not record:
            continue
        head, raw_path = record.split(b"\t", 1)
        mode, kind, oid = head.decode("ascii").split()
        need(kind == "blob" and re.fullmatch(r"[0-9a-f]{40}", oid),
             "Unexpected object in current Git tree")
        path = raw_path.decode("utf-8")
        safe_path(path)
        result.append(dict(path=path, mode=mode, git_blob_sha1=oid))
    result.sort(key=lambda row: row["path"].encode("utf-8"))
    need(len({row["path"] for row in result}) == len(result), "Duplicate Git tree path")
    return result

def check_readmes(repo, previous_head=None):
    actual = {path: git(repo, ["rev-parse", "HEAD:" + path]).decode().strip()
              for path in READMES}
    if actual != READMES:
        if previous_head:
            # Only these two already-small instruction files may be read.
            diff = git_process(repo, ["diff", previous_head, "HEAD", "--", *READMES],
                               check=False)
            print(diff.stdout.decode("utf-8", "replace"), flush=True)
        raise RuntimeError("README changed; preserve current files and read updated rules")
    return actual

def pull_rebase(repo):
    before = git(repo, ["rev-parse", "HEAD"]).decode().strip()
    process = git_process(repo, ["pull", "--rebase", "origin", "main"], check=False)
    if process.returncode:
        conflicts = git_process(repo, ["diff", "--name-only", "--diff-filter=U"],
                                check=False).stdout.decode("utf-8", "replace")
        git_process(repo, ["rebase", "--abort"], check=False)
        if not conflicts.strip():
            raise RuntimeError("Ordinary pull/rebase failed; no deletion/push attempted")
        return False
    check_readmes(repo, before)
    return True

def current_metadata(repo):
    head = git(repo, ["rev-parse", "HEAD"]).decode().strip()
    topic_tree = git(repo, ["rev-parse", head + ":" + TOPIC]).decode().strip()
    api = [dict(row, path=TOPIC + "/" + row["path"]) for row in api_rows(topic_tree)]
    local = git_rows(repo, head, TOPIC)
    need([(x["path"], x["mode"], x["git_blob_sha1"]) for x in api] ==
         [(x["path"], x["mode"], x["git_blob_sha1"]) for x in local],
         "Git tree and GitHub metadata disagree")
    return head, api

def select_applicable(deletion, current):
    by_path = {row["path"]: row for row in current}
    applicable, absent, changed = [], [], []
    for row in deletion:
        now = by_path.get(row["path"])
        if now is None:
            absent.append(row["path"])
        elif all(now[key] == row[key] for key in ("mode", "git_blob_sha1")):
            need(now["bytes"] == row["bytes"], "Same blob OID with different API size")
            applicable.append(row)
        else:
            changed.append(dict(path=row["path"], pinned={
                key: row[key] for key in ("mode", "git_blob_sha1", "bytes")},
                current=now))
    return applicable, absent, changed

def meta_line(row):
    return (row["mode"] + "\t" + row["git_blob_sha1"] + "\t" +
            str(row["bytes"]) + "\t" + row["path"] + "\n").encode("utf-8")

def delete_line(row):
    return (row["mode"] + "\t" + row["git_blob_sha1"] + "\t" +
            str(row["bytes"]) + "\t" + row["category"] + "\t" +
            row["path"] + "\n").encode("utf-8")

def receipt(path, raw):
    path.write_bytes(raw)
    return dict(file=path.name, bytes=len(raw), sha256=digest(raw),
                temporary_operational_file_only=True)

def compact_note(report, recipe_sha, source_sha, run_id, attempt):
    lines = [
        "# Request104: ordinary removal of regenerable notes payloads",
        "",
        "Status: repository bookkeeping; no scientific computation or acceptance decision.",
        "",
        "- Actions run: " + run_id + ", attempt " + attempt + ".",
        "- Script SHA-256: " + source_sha + ".",
        "- Exact selector source SHA-256: " + report["selector_source_sha256"] + ".",
        "- Request/recipe SHA-256: " + recipe_sha + ".",
        "- Pinned historical commit: " + BASE_COMMIT + ".",
        "- Pinned notes tree: " + NOTES_TREE + ".",
        "- Planning HEAD: " + report["planning_head"] + ".",
        "- Root README blob: " + READMES["README.md"] + ".",
        "- Topic README blob: " + READMES[TOPIC + "/README.md"] + ".",
        "",
        "## Exact deletion scope",
        "",
        "The selector preserves Markdown, code, named parameters, manifests/identity records",
        "and every unclassified JSON. Only the pinned tree's exact path + mode + blob OID",
        "matches are removed from the current index. A changed or newly introduced file",
        "is not inferred to be deletable from its name.",
        "",
        "| Scope at the planning HEAD | Files | Bytes |",
        "|---|---:|---:|",
        "| Complete topic before this deletion | " + str(report["current_topic_files"]) +
            " | " + str(report["current_topic_bytes"]) + " |",
        "| Exact current matches selected for deletion | " +
            str(report["currently_matching_delete_files"]) + " | " +
            str(report["currently_matching_delete_bytes"]) + " |",
        "| Projected topic before adding this small note | " +
            str(report["projected_topic_files_before_note"]) + " | " +
            str(report["projected_topic_bytes_before_note"]) + " |",
        "",
        "- Already absent candidates: " + str(report["already_absent_candidate_count"]) + ".",
        "- Changed candidates retained: " + str(report["changed_candidate_count"]) + ".",
        "- Pinned deletion ledger SHA-256: " + EXPECTED["deletion_tsv_sha256"] + ".",
        "- Current matching ledger SHA-256: " +
            report["temporary_inventory_files"]["applicable_deletion_ledger"]["sha256"] + ".",
        "- Current matching NUL path list SHA-256: " +
            report["temporary_inventory_files"]["applicable_paths_nul"]["sha256"] + ".",
        "",
        "The large metadata ledger and path list are generated only in runner temporary",
        "storage. Neither is committed or uploaded. The committed selector, parameters,",
        "historical tree and hashes regenerate the exact list. Sizes come from GitHub",
        "Git Tree metadata; Git matching uses ls-tree -r -z, without -l or data reads.",
        "",
        "## Input continuity and remaining scope",
        "",
        "The already declared original-input bootstrap commit remains " + HISTORY_REF + ".",
        "Request101 and subsequent literal-recipe continuations can restore their original",
        "accepted/prepared/zero-anchor bytes from that history and verify their old SHA-256.",
        "T112-config.json and all computations/source-dependencies.json/public78 code remain.",
        "No historical commit is rewritten and no Release is created.",
        "",
        "This conservative pass retains unknown JSON and does not claim to have classified",
        "every historical small file under Rule15. It does not create a scientific gate.",
        "Any later source/parameter change is independent of this metadata-only deletion.",
        "",
        "The planning counts above are tied to the stated HEAD; the run's final compact",
        "stdout records the actual post-push topic size after any concurrent rebase.",
        "",
    ]
    return "\n".join(lines).encode("utf-8")

def make_plan(repo, deletion, out, generation):
    head, current = current_metadata(repo)
    applicable, absent, changed = select_applicable(deletion, current)
    current_bytes = sum(row["bytes"] for row in current)
    deleted_bytes = sum(row["bytes"] for row in applicable)
    ledger = b"".join(delete_line(row) for row in applicable)
    paths = b"".join(row["path"].encode("utf-8") + b"\0" for row in applicable)
    prefix = "generation-" + str(generation).zfill(3)
    report = dict(
        planning_head=head, current_topic_files=len(current), current_topic_bytes=current_bytes,
        currently_matching_delete_files=len(applicable),
        currently_matching_delete_bytes=deleted_bytes,
        projected_topic_files_before_note=len(current)-len(applicable),
        projected_topic_bytes_before_note=current_bytes-deleted_bytes,
        already_absent_candidate_count=len(absent), changed_candidate_count=len(changed),
        changed_candidates_receipt=receipt(out / (prefix + "-changed-candidates.json"),
            (json.dumps(changed, sort_keys=True, separators=(",", ":")) + "\n").encode()),
        temporary_inventory_files={
            "applicable_deletion_ledger": receipt(out / (prefix + "-delete-manifest.tsv"), ledger),
            "applicable_paths_nul": receipt(out / (prefix + "-delete-paths.nul"), paths),
        })
    return report, applicable, paths

def verify_recipe(recipe, source_sha, selector_sha):
    need(recipe.get("schema") == "rule15-topic104-metadata-cleanup-request-v1" and
         recipe.get("request_number") == 104 and
         recipe.get("repository") == REPOSITORY, "Wrong cleanup recipe")
    need(recipe.get("base_commit") == BASE_COMMIT and
         recipe.get("notes_tree") == NOTES_TREE and
         recipe.get("expected_pinned_totals") == EXPECTED, "Pinned recipe changed")
    need(recipe.get("readme_git_blobs") == READMES and
         recipe.get("original_input_history_commit") == HISTORY_REF,
         "Rule/input history identities differ")
    need(recipe.get("script_sha256") == source_sha and
         recipe.get("selector_source_sha256") == selector_sha and
         recipe.get("keep_unknown_JSON") is True and
         recipe.get("no_artifact_or_Release_upload") is True and
         recipe.get("ordinary_nonforce_commit_only") is True,
         "Source or ordinary-cleanup policy differs")

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--recipe", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    repo = Path(args.repository).resolve()
    out = Path(args.out).resolve()
    need(not out.exists(), "Output must be a new temporary directory")
    need(out != repo and repo not in out.parents,
         "Keep regenerable operational inventories outside the Git checkout")
    recipe_raw = Path(args.recipe).read_bytes()
    source_raw = Path(__file__).read_bytes()
    source_sha = digest(source_raw)
    source_text = source_raw.decode("utf-8")
    selector_start = source_text.index("def classify(")
    selector_stop = source_text.index("\n_TREE_CACHE = {}", selector_start)
    selector_sha = digest(source_text[selector_start:selector_stop].encode("utf-8"))
    verify_recipe(json.loads(recipe_raw), source_sha, selector_sha)
    recipe_sha = digest(recipe_raw)
    run_id = os.environ.get("GITHUB_RUN_ID", "read-only")
    attempt = os.environ.get("GITHUB_RUN_ATTEMPT", "0")
    if args.apply:
        need(os.environ.get("GITHUB_ACTIONS") == "true" and
             run_id.isdigit() and attempt.isdigit() and os.environ.get("GITHUB_TOKEN"),
             "Explicit --apply requires its authorized Actions environment")
        need(not git(repo, ["status", "--porcelain", "--untracked-files=normal"]).strip(),
             "Refuse to alter a checkout with pre-existing changes")
        git(repo, ["switch", "-c", "rule15-cleanup-" + run_id + "-" + attempt + "-0"])
        need(pull_rebase(repo), "Initial metadata checkout could not rebase")
    check_readmes(repo)
    git_version = git(repo, ["--version"]).decode("utf-8", "replace").strip()
    out.mkdir(parents=True)

    # Read only tree metadata. These APIs never request any blob contents.
    pinned = api_rows(NOTES_TREE)
    need(len(pinned) == EXPECTED["files"] and
         sum(row["bytes"] for row in pinned) == EXPECTED["bytes"],
         "Pinned notes totals differ from the complete API metadata inventory")
    original_metadata = b"".join(meta_line(row) for row in pinned)
    need(digest(original_metadata) == EXPECTED["metadata_tsv_sha256"],
         "Pinned metadata ledger differs")
    classified = []
    counts, groups = {}, {}
    for row in pinned:
        category = classify(row["path"], row["mode"])
        item = dict(row, category=category)
        classified.append(item)
        total = counts.setdefault(category, dict(files=0, bytes=0))
        total["files"] += 1
        total["bytes"] += row["bytes"]
        group = row["path"].split("/", 1)[0] if "/" in row["path"] else "(notes-root)"
        total = groups.setdefault(group, dict(files=0, bytes=0, delete_files=0, delete_bytes=0))
        total["files"] += 1
        total["bytes"] += row["bytes"]
        if category.startswith("delete-"):
            total["delete_files"] += 1
            total["delete_bytes"] += row["bytes"]
    deletion = [dict(row, path=NOTES + "/" + row["path"])
                for row in classified if row["category"].startswith("delete-")]
    need(len(deletion) == EXPECTED["delete_files"] and
         sum(row["bytes"] for row in deletion) == EXPECTED["delete_bytes"],
         "Selector no longer reproduces the pinned whitelist")
    deletion_tsv = b"".join(delete_line(row) for row in deletion)
    deletion_nul = b"".join(row["path"].encode("utf-8") + b"\0" for row in deletion)
    need(digest(deletion_tsv) == EXPECTED["deletion_tsv_sha256"] and
         digest(deletion_nul) == EXPECTED["deletion_paths_nul_sha256"],
         "Exact pinned deletion whitelist differs")
    pinned_manifest_receipt = receipt(out / "pinned-delete-manifest.tsv", deletion_tsv)
    recovery = []
    pinned_paths = {NOTES + "/" + row["path"]: row for row in classified}
    for spec in INPUT_RECOVERY:
        row = pinned_paths.get(spec["path"])
        need(row is not None and row["bytes"] == spec["bytes"],
             "Known historical input metadata differs")
        recovery.append(dict(spec, history_ref=HISTORY_REF,
            git_blob_sha1=row["git_blob_sha1"], classification=row["category"],
            payload_SHA256_previously_verified_not_recomputed_here=True))

    generation = 0
    push_rejections = 0
    report, applicable, paths = make_plan(repo, deletion, out, generation)
    report["selector_source_sha256"] = selector_sha
    published_commit = None
    note_receipt = None
    while args.apply:
        # A rebase conflict never licenses removal of a changed remote file.
        # Start a fresh local branch from the fetched main and rematch by OID.
        note_rel = (NOTES + "/2026-11-15-rule15-request104-run" + run_id +
                    "-attempt" + attempt + "-metadata-cleanup.md")
        note_path = repo / note_rel
        need(not note_path.exists(), "This run's compact note already exists")
        note_raw = compact_note(report, recipe_sha, source_sha, run_id, attempt)
        note_path.parent.mkdir(parents=True, exist_ok=True)
        note_path.write_bytes(note_raw)
        need(git(repo, ["rev-parse", "HEAD"]).decode().strip() == report["planning_head"],
             "HEAD changed while building the metadata-only plan")
        check_readmes(repo)
        git(repo, ["update-index", "--force-remove", "-z", "--stdin"], paths)
        git(repo, ["add", "--sparse", "--", note_rel])
        deleted = git(repo, ["diff", "--cached", "--no-renames", "--diff-filter=D",
                             "--name-only", "-z"]).split(b"\0")
        added = git(repo, ["diff", "--cached", "--no-renames", "--diff-filter=A",
                           "--name-only", "-z"]).split(b"\0")
        all_changed = git(repo, ["diff", "--cached", "--no-renames",
                                "--name-only", "-z"]).split(b"\0")
        expected_deleted = {row["path"].encode() for row in applicable}
        need(set(filter(None, deleted)) == expected_deleted and
             set(filter(None, added)) == {note_rel.encode()} and
             set(filter(None, all_changed)) == expected_deleted | {note_rel.encode()},
             "Staged changes exceed the exact whitelist and one own compact note")
        git(repo, ["-c", "user.name=github-actions[bot]", "-c",
                   "user.email=41898282+github-actions[bot]@users.noreply.github.com",
                   "commit", "--no-gpg-sign", "-m",
                   "visible-larger: remove regenerable notes payloads under rule15"])
        note_receipt = dict(file=note_rel, bytes=len(note_raw), sha256=digest(note_raw))
        restart = False
        while True:
            if not pull_rebase(repo):
                generation += 1
                git(repo, ["switch", "-c",
                    "rule15-cleanup-" + run_id + "-" + attempt + "-" + str(generation),
                    "origin/main"])
                check_readmes(repo)
                report, applicable, paths = make_plan(repo, deletion, out, generation)
                report["selector_source_sha256"] = selector_sha
                restart = True
                break
            # Only ordinary, non-force Git push. No GitHub API mutation is used.
            push = git_process(repo, ["push", "origin", "HEAD:refs/heads/main"], check=False)
            if push.returncode == 0:
                published_commit = git(repo, ["rev-parse", "HEAD"]).decode().strip()
                break
            message = push.stderr.decode("utf-8", "replace").lower()
            if not any(word in message for word in ("non-fast-forward", "fetch first", "[rejected]")):
                raise RuntimeError("Ordinary push failed for a reason other than concurrent main")
            push_rejections += 1
            print(json.dumps(dict(event="rule15-non-fast-forward-rebase-and-retry",
                                  rejected_push_count=push_rejections)), flush=True)
        if restart:
            continue
        break

    final_head, final_rows = current_metadata(repo)
    final_bytes = sum(row["bytes"] for row in final_rows)
    result = dict(
        schema=SCHEMA, run_id=run_id, run_attempt=attempt, source_sha256=source_sha,
        recipe_sha256=recipe_sha, selector_source_sha256=selector_sha,
        base_commit=BASE_COMMIT, notes_tree=NOTES_TREE,
        readme_git_blobs=READMES, expected_pinned_totals=EXPECTED,
        category_totals=counts, notes_top_level_directory_totals=groups,
        plan=report, pinned_deletion_manifest=pinned_manifest_receipt,
        known_original_input_history_recovery=recovery,
        applied=args.apply, published_commit=published_commit, final_head=final_head,
        compact_note=note_receipt, final_topic_files=len(final_rows),
        final_topic_bytes=final_bytes, final_topic_under_decimal_200MB=final_bytes <= 200000000,
        non_fast_forward_pushes=push_rejections, metadata_rematch_generations=generation,
        scientific_data_blob_contents_requested=False,
        Git_tree_sizes_source="GitHub Git Tree API metadata",
        Git_ls_tree_l_option_used=False, git_version=git_version,
        process_merge_renames=False, process_diff_renames=False,
        GIT_NO_LAZY_FETCH_environment_set=True, scientific_calculations=0,
        Release_uploads=0, artifact_uploads=0, history_rewritten=False,
        H_open_log_modified=False, unknown_JSON_retained=True,
        rule15_complete_classification_claimed=False,
        full_inventory_retained_in_commit_or_artifact=False)
    raw = (json.dumps(result, ensure_ascii=True, sort_keys=True,
                      separators=(",", ":"), allow_nan=False) + "\n").encode("utf-8")
    need(len(raw) <= 90000, "Compact cleanup report exceeds text scope")
    receipt(out / "inventory-summary.json", raw)
    print("BEGIN_VISIBLE104_METADATA_SUMMARY", flush=True)
    print(raw.decode(), end="", flush=True)
    print("END_VISIBLE104_METADATA_SUMMARY", flush=True)
    print(json.dumps(dict(event="visible104-summary-sha256", bytes=len(raw),
                          sha256=digest(raw), source_sha256=source_sha)), flush=True)

if __name__ == "__main__":
    main()
