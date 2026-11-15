#!/usr/bin/env python3
"""Ordinary deletion of reproducible data; exact historical bytes remain recoverable.

Storage administration only: no target, interval, Fourier, or mathematical stage
is evaluated.  No Release or Actions artifact is uploaded.  No history rewrite.
"""
from __future__ import annotations
import argparse
import datetime as dt
import gzip
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import tempfile
import time
import traceback
import urllib.error
import urllib.request

REPOSITORY = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
MAX_TOPIC_BYTES = 200_000_000
MAX_GIT_FILE_BYTES = 5_000_000
MAX_METADATA_READ_BYTES = 100_000
MAX_READABLE_BYTES = 60_000
RULES_PATH = TOPIC + "/notes/2026-11-15-R133-reviewed-public-CI-rules-reproducible-data.json"
RULES_SHA256 = "f2661bd5cf5cb006c1f78c64126b3ac065e6bc26a50790545ac443efb5e372bd"
READMES = ("README.md", TOPIC + "/README.md")
SOURCE_EXTENSIONS = {
    ".py", ".pyi", ".sh", ".bash", ".js", ".ts", ".tsx", ".jsx",
    ".c", ".cc", ".cpp", ".h", ".hpp", ".f", ".f90", ".jl", ".m",
    ".r", ".sage", ".tex", ".bib", ".yml", ".yaml", ".toml",
    ".ini", ".cfg", ".lock", ".ipynb", ".lean", ".v", ".agda",
}
DATA_EXTENSIONS = {
    ".gz", ".npz", ".npy", ".bin", ".zip", ".tar", ".tgz", ".xz",
    ".bz2", ".zst", ".h5", ".hdf5", ".pkl", ".pickle", ".parquet",
    ".feather", ".arrow", ".csv", ".tsv", ".dat",
}
OUTPUT_SEGMENTS = {
    "native", "natives", "consumers", "matrices", "stages", "cases",
    "rows", "checkpoints", "outputs", "prepared", "cache", "arrays",
    "candidates", "trials", "reconstructed", "certificates",
}
METADATA_WORDS = re.compile(
    r"(?:^|[-_.])(?:manifest|index|inputs?|parameters?|params?|process|"
    r"summary|receipt|inventory|provenance|identity|audit|status|selection|"
    r"publication|runtime|rules|metadata|configuration|config)(?:[-_.]|$)", re.I
)
PARAMETER_WORDS = re.compile(
    r"(?:^|[-_.])(?:parameters?|params?|inputs?|configuration|config)(?:[-_.]|$)", re.I
)
PART_WORDS = re.compile(r"(?:[._-](?:part|chunk)[._-]?\d+)(?:[._-]|$)", re.I)
RUN_WORDS = re.compile(r"(?:^|/)run-(\d+)(?:-(\d+))?(?:-|/|$)")
SOURCE_PATH = re.compile(r"(?:topics/[A-Za-z0-9_.-]+/)?scripts/[A-Za-z0-9_./-]+\.py")


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def canonical(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def safe_relative(value):
    if not isinstance(value, str) or any(x in value for x in ("\x00", "\n", "\r")):
        raise ValueError("unsafe relative path")
    p = PurePosixPath(value)
    if p.is_absolute() or not p.parts or any(q in ("..", ".git") for q in p.parts):
        raise ValueError("unsafe relative path")
    return str(p)


def redact(value):
    answer = str(value)
    for key in ("GITHUB_TOKEN", "GH_TOKEN"):
        secret = os.environ.get(key, "")
        if secret:
            answer = answer.replace(secret, "[REDACTED]")
    return answer


def git(repo, argv, *, check=True, data=None):
    result = subprocess.run(
        ["git", "-C", str(repo), *argv], input=data,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    if check and result.returncode:
        raise RuntimeError("git operation failed: " + redact(result.stderr.decode("utf-8", "replace")[-6000:]))
    return result


def git_text(repo, argv):
    return git(repo, argv).stdout.decode("utf-8").strip()


def assert_public_repository(repo):
    origin = git_text(repo, ["remote", "get-url", "origin"]).removesuffix(".git")
    if origin not in (
        "https://github.com/" + REPOSITORY,
        "git@github.com:" + REPOSITORY,
        "ssh://git@github.com/" + REPOSITORY,
    ):
        raise ValueError("only the authorized public origin is accepted")
    if os.environ.get("GITHUB_REPOSITORY", REPOSITORY) != REPOSITORY:
        raise ValueError("unexpected GitHub repository")
    if git_text(repo, ["symbolic-ref", "--short", "HEAD"]) != "main":
        raise ValueError("checkout must be on the ordinary main branch")
    if git(repo, ["status", "--porcelain"]).stdout:
        raise ValueError("cleanup requires a clean checkout at entry")


class GitHub:
    def __init__(self):
        self.token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
        if not self.token:
            raise ValueError("an Actions token is required for repository metadata")

    def get(self, suffix):
        if not suffix.startswith("/") or ".." in suffix:
            raise ValueError("unexpected API path")
        url = "https://api.github.com/repos/" + REPOSITORY + suffix
        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": "Bearer " + self.token,
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "visible-exact-reproducible-data-cleanup",
        }
        for attempt in range(5):
            try:
                request = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(request, timeout=90) as response:
                    return json.load(response)
            except urllib.error.HTTPError as exc:
                if exc.code not in (429, 500, 502, 503, 504) or attempt == 4:
                    raise RuntimeError("GitHub metadata request failed with status " + str(exc.code)) from exc
                time.sleep(min(2 ** attempt, 16))
            except (TimeoutError, OSError):
                if attempt == 4:
                    raise
                time.sleep(min(2 ** attempt, 16))
        raise AssertionError("unreachable")

    def subtree(self, tree_sha):
        first = self.get("/git/trees/" + tree_sha + "?recursive=1")
        if not first.get("truncated"):
            return first["tree"]
        result = []
        pending = [("", tree_sha)]
        while pending:
            prefix, oid = pending.pop()
            current = self.get("/git/trees/" + oid)
            if current.get("truncated"):
                raise ValueError("nonrecursive Git tree was truncated")
            for node in current["tree"]:
                item = dict(node)
                item["path"] = prefix + node["path"]
                if node["type"] == "tree":
                    pending.append((item["path"] + "/", node["sha"]))
                else:
                    result.append(item)
        return result


def git_tree(repo, commit):
    # No -l size query: keep a partial clone from downloading the whole topic.
    raw = git(repo, ["ls-tree", "-r", "-z", commit, "--", TOPIC]).stdout
    records = {}
    for row in raw.split(b"\x00"):
        if not row:
            continue
        header, path = row.split(b"\t", 1)
        mode, kind, oid = header.decode("ascii").split()
        name = safe_relative(path.decode("utf-8"))
        if not name.startswith(TOPIC + "/"):
            raise ValueError("tree path escaped the authorized topic")
        records[name] = {"mode": mode, "type": kind, "git_blob": oid}
    return records


def metadata_inventory(repo, commit, api):
    local = git_tree(repo, commit)
    subtree = git_text(repo, ["rev-parse", commit + ":" + TOPIC])
    remote = {}
    for item in api.subtree(subtree):
        if item["type"] != "tree":
            remote[TOPIC + "/" + safe_relative(item["path"])] = item
    if set(local) != set(remote):
        raise ValueError("local and server-side complete topic trees differ")
    for path, item in local.items():
        other = remote[path]
        if (item["git_blob"], item["mode"], item["type"]) != (other["sha"], other["mode"], other["type"]):
            raise ValueError("server-side metadata is not the exact Git tree")
        if item["type"] != "blob":
            raise ValueError("unexpected submodule or non-blob topic object")
        size = other.get("size")
        if not isinstance(size, int) or size < 0:
            raise ValueError("server-side blob size metadata is missing")
        item["bytes"] = size
    return local


def classification(path, item):
    rel = path[len(TOPIC) + 1:]
    p = PurePosixPath(rel)
    name, low, ext = p.name, p.name.lower(), p.suffix.lower()
    if item["mode"] not in ("100644", "100755"):
        return "retain_ambiguous", "nonregular object retained"
    if rel.startswith(("scripts/", "results/", "papers/", "notes/data_cleanup/")):
        return "retain_source_or_metadata", "source, proof, paper, or deletion metadata"
    if ext == ".md" or ext in SOURCE_EXTENSIONS or low in ("license", ".gitkeep", ".gitignore", "makefile", "requirements.txt"):
        return "retain_source_or_metadata", "source, documentation, or runtime parameter file"
    if low in ("readme", "handoff", "open", "log"):
        return "retain_source_or_metadata", "topic instructions or human record"
    if PARAMETER_WORDS.search(name) and item["bytes"] <= MAX_GIT_FILE_BYTES:
        return "retain_parameter", "explicit original parameter/input file"
    if ext == ".json" and METADATA_WORDS.search(name) and item["bytes"] <= MAX_GIT_FILE_BYTES:
        return "retain_source_or_metadata", "original manifest, process, summary, or identity metadata"
    if PART_WORDS.search(name):
        return "delete_reproducible", "original numbered certificate/data part; exact bytes remain in Git history"
    if ext in DATA_EXTENSIONS:
        return "delete_reproducible", "reproducible numerical data or compressed computation output"
    if rel.startswith("data/"):
        if ext in (".json", ".txt") and item["bytes"] <= MAX_METADATA_READ_BYTES:
            return "retain_source_or_metadata", "small original data index or parameter text"
        if ext in (".json", ".txt") or item["bytes"] > 1_000_000:
            return "delete_reproducible", "large or structured numerical data under data/"
        return "retain_ambiguous", "unclassified original data input"
    if any(segment in OUTPUT_SEGMENTS for segment in p.parts[:-1]):
        if ext == ".json":
            return "delete_reproducible", "saved native, stage, case, or array JSON output"
        if ext in (".txt", ".log") and item["bytes"] > MAX_METADATA_READ_BYTES:
            return "delete_reproducible", "large reproducible computation trace"
    if ext == ".json" and item["bytes"] > 1_000_000:
        return "delete_reproducible", "large numerical JSON outside a source/parameter namespace"
    if ext in (".txt", ".log") and item["bytes"] > 1_000_000:
        return "delete_reproducible", "large reproducible textual computation output"
    return "retain_ambiguous", "small text or unknown file retained"


def blob_bytes(repo, oid, expected_size):
    if expected_size > MAX_METADATA_READ_BYTES:
        raise ValueError("metadata reader refused a large file")
    raw = git(repo, ["cat-file", "blob", oid]).stdout
    if len(raw) != expected_size:
        raise ValueError("metadata blob size mismatch")
    if hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\x00" + raw).hexdigest() != oid:
        raise ValueError("metadata Git blob identity mismatch")
    return raw


def hash_original_blob(repo, oid, expected_size):
    # Streaming hash only; never deserialize or recompute the mathematics.
    h = hashlib.sha256()
    g = hashlib.sha1(b"blob " + str(expected_size).encode("ascii") + b"\x00")
    count = 0
    with tempfile.TemporaryFile() as error:
        proc = subprocess.Popen(
            ["git", "-C", str(repo), "cat-file", "blob", oid],
            stdout=subprocess.PIPE, stderr=error,
        )
        assert proc.stdout is not None
        while True:
            block = proc.stdout.read(1024 * 1024)
            if not block:
                break
            count += len(block)
            h.update(block)
            g.update(block)
        status = proc.wait()
        if status:
            error.seek(0)
            raise RuntimeError("original blob read failed: " + redact(error.read(6000).decode("utf-8", "replace")))
    if count != expected_size or g.hexdigest() != oid:
        raise ValueError("original Git identity or byte count failed")
    return h.hexdigest()


def extract_command_parameters(value):
    scripts, commands, named = set(), [], {}
    def visit(node, key="", depth=0):
        if depth > 9:
            return
        if isinstance(node, str):
            for match in SOURCE_PATH.findall(node):
                scripts.add(match if match.startswith("topics/") else TOPIC + "/" + match)
            if key.lower() in ("command", "cmd", "argv", "arguments", "args", "producer", "script", "source", "scientific_source", "input_manifest"):
                if len(node.encode("utf-8")) <= 4000:
                    named.setdefault(key, node)
        elif isinstance(node, list):
            if key.lower() in ("command", "cmd", "argv", "arguments", "args") and all(isinstance(x, (str, int, float, bool)) or x is None for x in node):
                if len(canonical(node)) <= 6000:
                    commands.append(node)
            else:
                for item in node[:100]:
                    visit(item, key, depth + 1)
        elif isinstance(node, dict):
            for child_key, child in node.items():
                visit(child, str(child_key), depth + 1)
    visit(value)
    return {
        "script_paths_recorded_in_original_metadata": sorted(scripts),
        "command_vectors_recorded_in_original_metadata": commands[:4],
        "original_named_source_or_parameter_fields": named,
        "no_producer_inferred_from_a_later_consumer": True,
    }


class Provenance:
    def __init__(self, repo, tree, decisions):
        self.repo, self.tree = repo, tree
        self.cache, self.groups = {}, {}
        self.candidates = [
            p for p, item in tree.items()
            if decisions[p][0] != "delete_reproducible"
            and item["bytes"] <= MAX_METADATA_READ_BYTES
            and PurePosixPath(p).suffix.lower() == ".json"
            and METADATA_WORDS.search(PurePosixPath(p).name)
        ]

    def for_path(self, path):
        match = RUN_WORDS.search(path)
        pieces = path.split("/")
        if match:
            at = next(i for i, x in enumerate(pieces) if re.match(r"run-\d+", x))
            prefix = "/".join(pieces[:at + 1])
            run_id, attempt = match.group(1), match.group(2)
        else:
            prefix = "/".join(pieces[:4]) if len(pieces) >= 4 else str(PurePosixPath(path).parent)
            run_id, attempt = None, None
        if prefix in self.cache:
            return self.cache[prefix]
        related = [p for p in self.candidates if p.startswith(prefix + "/")]
        def priority(p):
            score = 0 if PurePosixPath(p).name.lower() in ("process.json", "worker-process.json", "publication.json") else 1
            return (score, p.count("/"), len(p), p)
        evidence = []
        for p in sorted(related, key=priority)[:6]:
            raw = blob_bytes(self.repo, self.tree[p]["git_blob"], self.tree[p]["bytes"])
            try:
                value = json.loads(raw)
            except (UnicodeDecodeError, json.JSONDecodeError):
                continue
            evidence.append({
                "path": p, "git_blob": self.tree[p]["git_blob"],
                "bytes": len(raw), "sha256": sha256(raw),
                **extract_command_parameters(value),
            })
        record = {
            "original_directory": prefix,
            "workflow_run_id_from_original_path": run_id,
            "workflow_run_attempt_from_original_path": attempt,
            "retained_original_source_parameter_and_run_metadata": evidence,
            "producer_resolution": (
                "read_original_metadata_above; no regenerated values" if evidence else
                "not_identified_by_this_storage_worker; original scripts and immutable history retained"
            ),
        }
        identity = sha256(canonical(record))
        self.groups[identity], self.cache[prefix] = record, identity
        return identity


class Synchronizer:
    def __init__(self, repo, rules, state):
        self.repo, self.rules, self.state = repo, rules, state
        self.last_checked_commit, self.last_sync = rules["read_commit"], 0.0

    def check(self, label, before=None):
        commit = git_text(self.repo, ["rev-parse", "HEAD"])
        current = {p: sha256(git(self.repo, ["show", commit + ":" + p]).stdout) for p in READMES}
        prior = before or self.last_checked_commit
        diff = git(self.repo, ["diff", prior, commit, "--", *READMES]).stdout.decode("utf-8")
        entry = {
            "label": label, "utc": now(), "commit": commit,
            "compared_with_commit": prior, "readme_sha256": current,
            "readme_diff": diff if len(diff.encode("utf-8")) <= 40_000 else "See the two immutable commits; diff exceeds the readable metadata bound.",
            "reviewed_rule15_metadata_sha256": RULES_SHA256,
        }
        self.state["pulls_and_readme_checks"].append(entry)
        if current != self.rules["readme_sha256"]:
            self.state["unread_rule_change"] = entry
            print(json.dumps({"unread_rule_change": entry}, sort_keys=True), flush=True)
            raise ValueError("instructions changed; exact diff recorded before further deletion")
        self.last_checked_commit, self.last_sync = commit, time.monotonic()
        return commit

    def pull(self, label):
        before = git_text(self.repo, ["rev-parse", "HEAD"])
        git(self.repo, ["pull", "--rebase", "origin", "main"])
        return self.check(label, before)

    def periodic(self):
        if time.monotonic() - self.last_sync >= 3000:
            self.pull("hourly_true_pull_during_byte_inventory")

    def push_until_success(self):
        while True:
            pushed = git(self.repo, ["push", "origin", "HEAD:main"], check=False)
            if pushed.returncode == 0:
                return git_text(self.repo, ["rev-parse", "HEAD"])
            before = git_text(self.repo, ["rev-parse", "HEAD"])
            pulled = git(self.repo, ["pull", "--rebase", "origin", "main"], check=False)
            if pulled.returncode:
                raw = git(self.repo, ["diff", "--name-only", "--diff-filter=U", "-z"]).stdout
                paths = [p.decode("utf-8") for p in raw.split(b"\x00") if p]
                if not paths:
                    raise RuntimeError("non-fast-forward recovery failed: " + redact(pulled.stderr.decode("utf-8", "replace")[-6000:]))
                # Preserve any concurrent newer data version.  Unique metadata
                # conflicts are never resolved by overwriting another author.
                for p in paths:
                    if p not in self.state["deletion_request_by_path"]:
                        raise RuntimeError("non-data conflict preserved for continuation; no forced resolution")
                    kept = git(self.repo, ["checkout", "--ours", "--", p], check=False)
                    if kept.returncode == 0:
                        git(self.repo, ["add", "--", p])
                    else:
                        git(self.repo, ["rm", "-f", "--ignore-unmatch", "--", p])
                    self.state["upstream_changed_paths_retained_during_rebase"].append(p)
                environment = dict(os.environ)
                environment["GIT_EDITOR"] = "true"
                result = subprocess.run(
                    ["git", "-C", str(self.repo), "rebase", "--continue"],
                    env=environment, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                )
                if result.returncode:
                    raise RuntimeError("ordinary rebase could not finish; no force push attempted")
            self.check("non_fast_forward_true_pull_rebase", before)


def atomic_bytes(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_bytes(value)
    temporary.replace(path)


def readable_json(path, value):
    raw = (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    if len(raw) > MAX_READABLE_BYTES:
        raise ValueError("readable cleanup metadata exceeded 60000 bytes")
    atomic_bytes(path, raw)
    return {"bytes": len(raw), "sha256": sha256(raw)}


def manifest_file(directory, document):
    raw = canonical(document)
    value = gzip.compress(raw, compresslevel=9, mtime=0) if len(raw) > 1_000_000 else raw
    name = "deletion-manifest.json.gz" if len(raw) > 1_000_000 else "deletion-manifest.json"
    if len(value) > MAX_GIT_FILE_BYTES:
        raise ValueError("single natural metadata manifest exceeds 5 MB; no data deletion staged")
    atomic_bytes(directory / name, value)
    return name, {
        "bytes": len(value), "sha256": sha256(value),
        "uncompressed_canonical_bytes": len(raw),
        "uncompressed_canonical_sha256": sha256(raw),
        "contains_only_paths_hashes_parameters_and_run_identity": True,
        "contains_no_certificate_or_numerical_output_payload": True,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", required=True)
    parser.add_argument("--reviewed-rules", default=RULES_PATH)
    parser.add_argument("--reviewed-rules-sha256", default=RULES_SHA256)
    parser.add_argument("--publish", action="store_true")
    parser.add_argument("--audit-only", action="store_true")
    args = parser.parse_args()
    repo = Path(args.repo_root).resolve()
    if args.reviewed_rules_sha256 != RULES_SHA256:
        raise ValueError("worker is bound to the explicitly read current reproducible-data policy")
    rules_raw = (repo / safe_relative(args.reviewed_rules)).read_bytes()
    if sha256(rules_raw) != RULES_SHA256:
        raise ValueError("reviewed rules identity mismatch")
    rules = json.loads(rules_raw)
    if rules.get("repository") != REPOSITORY:
        raise ValueError("rules concern a different repository")
    policy = rules["large_data_policy"]
    if policy.get("reproducible_data_persisted_in_repository") is not False or policy.get("reproducible_data_persisted_in_Releases") is not False:
        raise ValueError("current policy forbids persistent reproducible data in both locations")
    assert_public_repository(repo)
    reviewed_commit = rules["read_commit"]
    if not re.fullmatch(r"[0-9a-f]{40}", reviewed_commit):
        raise ValueError("reviewed instruction commit is not immutable")
    if git(repo, ["cat-file", "-e", reviewed_commit + "^{commit}"], check=False).returncode:
        git(repo, ["fetch", "--no-tags", "--depth=1", "--filter=blob:none", "origin", reviewed_commit])
    run_id, attempt = os.environ.get("GITHUB_RUN_ID", "manual"), os.environ.get("GITHUB_RUN_ATTEMPT", "1")
    suffix = "run-" + re.sub(r"[^0-9A-Za-z_-]", "", run_id) + "-" + re.sub(r"[^0-9A-Za-z_-]", "", attempt)
    dest_rel = TOPIC + "/notes/data_cleanup/" + suffix
    destination = repo / dest_rel
    source = Path(__file__).resolve()
    state = {
        "kind": "ordinary_public_topic_reproducible_data_deletion",
        "complete": False, "started_utc": now(), "repository": REPOSITORY,
        "topic": TOPIC, "source_path": TOPIC + "/scripts/" + source.name,
        "source_sha256": sha256(source.read_bytes()),
        "reviewed_rules_path": args.reviewed_rules, "reviewed_rules_sha256": RULES_SHA256,
        "workflow_event_commit": os.environ.get("GITHUB_SHA"),
        "run_id": run_id, "run_attempt": attempt,
        "new_mathematical_evaluations": 0, "old_mathematical_recomputations": 0,
        "Release_uploads": 0, "Actions_artifact_uploads": 0,
        "history_rewrites": 0, "force_pushes": 0,
        "pulls_and_readme_checks": [], "upstream_changed_paths_retained_during_rebase": [],
        "deletion_request_by_path": {},
    }
    sync = Synchronizer(repo, rules, state)
    sync.check("initial_checked_out_rules")
    original = sync.pull("initial_true_pull")
    state["actual_scientific_checkout_commit"] = state["predeletion_commit"] = original
    api = GitHub()
    tree = metadata_inventory(repo, original, api)
    decisions = {p: classification(p, item) for p, item in tree.items()}
    before_bytes = sum(item["bytes"] for item in tree.values())
    counts = {}
    for path, (kind, reason) in decisions.items():
        bucket = counts.setdefault(kind, {"files": 0, "bytes": 0})
        bucket["files"] += 1
        bucket["bytes"] += tree[path]["bytes"]
    selected = sorted(p for p in tree if decisions[p][0] == "delete_reproducible")
    state.update(initial_topic_bytes=before_bytes, classification_totals=counts, initial_selected_files=len(selected))
    print(json.dumps({"storage_only": True, "predeletion_commit": original, "initial_topic_bytes": before_bytes, "classification_totals": counts, "new_mathematics": 0}, sort_keys=True), flush=True)
    provenance, requests = Provenance(repo, tree, decisions), []
    for number, path in enumerate(selected):
        sync.periodic()
        item = tree[path]
        requests.append({
            "path": path, "bytes": item["bytes"],
            "sha256": hash_original_blob(repo, item["git_blob"], item["bytes"]),
            "git_blob": item["git_blob"], "git_mode": item["mode"],
            "classification_reason": decisions[path][1],
            "producer_parameters_run_reference": provenance.for_path(path),
            "predeletion_commit": original,
        })
        if (number + 1) % 250 == 0:
            print(json.dumps({"hashed_original_files": number + 1, "total_selected_files": len(selected), "new_mathematics": 0}), flush=True)
    current = sync.pull("true_pull_before_deletion_staging")
    current_tree = git_tree(repo, current)
    removable, changed, absent = [], [], []
    for entry in requests:
        present = current_tree.get(entry["path"])
        if present is None:
            absent.append(entry)
        elif (present["git_blob"], present["mode"]) == (entry["git_blob"], entry["git_mode"]):
            removable.append(entry)
        else:
            changed.append(entry)
    state["deletion_request_by_path"] = {e["path"]: e["git_blob"] for e in removable}
    state.update(
        already_absent_original_versions=len(absent),
        changed_original_paths_retained=len(changed), pre_staging_main_commit=current,
        selected_original_versions_bytes=sum(e["bytes"] for e in requests),
        requested_deletion_files=len(removable),
        requested_deletion_bytes=sum(e["bytes"] for e in removable),
    )
    protected = [
        {"path": p, "bytes": tree[p]["bytes"], "git_blob": tree[p]["git_blob"], "reason": decisions[p][1]}
        for p in sorted(tree)
        if decisions[p][0] in ("retain_parameter", "retain_ambiguous") and tree[p]["bytes"] > 1_000_000
    ]
    document = {
        "schema": 1, "kind": "immutable_original_paths_hashes_and_reproduction_metadata",
        "repository": REPOSITORY, "topic": TOPIC, "created_utc": now(),
        "run_id": run_id, "run_attempt": attempt,
        "workflow_event_commit": os.environ.get("GITHUB_SHA"),
        "predeletion_commit": original, "pre_staging_main_commit": current,
        "producer": state["source_path"], "producer_sha256": state["source_sha256"],
        "parameters": {"reviewed_rules_path": args.reviewed_rules, "reviewed_rules_sha256": RULES_SHA256, "maximum_topic_bytes": MAX_TOPIC_BYTES},
        "requests_to_remove_exact_original_versions": removable,
        "already_absent_original_versions": absent,
        "newer_versions_at_original_paths_retained": changed,
        "original_source_parameter_and_run_metadata": provenance.groups,
        "large_parameter_or_ambiguous_inputs_retained": protected,
        "restoration_contract": {
            "command": "git show <predeletion_commit>:<path> > <temporary_scientific_file>",
            "public_repository_only": True,
            "required_checks": ["exact_original_bytes", "sha256", "git_blob"],
            "restore_destination": "temporary immutable scientific work only; do not recommit data",
            "scientific_source_and_parameter_manifests_are_unchanged": True,
            "mathematics_recomputed": False,
            "old_failure_and_success_identities_remain_in_git_history": True,
            "no_artificial_concatenation_or_reassembly_is_needed_for_history_restore": True,
        },
        "ordinary_deletion_only": True, "no_Release_or_Actions_artifact_upload": True,
        "deletion_version_semantics": "Entries identify original versions requested for removal. A concurrent newer version is preserved; the manifest does not license deleting a different blob.",
    }
    if args.audit_only:
        document["audit_only"] = True
        removable = []
    name, receipt = manifest_file(destination, document)
    state["deletion_manifest"] = {"path": dest_rel + "/" + name, **receipt}
    state["audit_only"] = bool(args.audit_only)
    if removable:
        with tempfile.NamedTemporaryFile(prefix="visible-exact-delete-paths-", delete=False) as listing:
            listing.write(b"".join(e["path"].encode("utf-8") + b"\x00" for e in removable))
            listing_name = listing.name
        try:
            git(repo, ["rm", "-f", "--sparse", "--ignore-unmatch", "--pathspec-from-file=" + listing_name, "--pathspec-file-nul"])
        finally:
            Path(listing_name).unlink(missing_ok=True)
    state.update(
        staged_data_deletions=len(removable),
        staged_deleted_original_bytes=sum(e["bytes"] for e in removable),
        complete=True, finished_local_utc=now(),
    )
    small = {k: v for k, v in state.items() if k != "deletion_request_by_path"}
    small["protected_large_files"] = protected[:20]
    small["protected_large_files_complete_in_manifest"] = True
    small["projected_original_tree_retained_bytes_before_small_metadata"] = before_bytes - sum(e["bytes"] for e in requests)
    small["topic_budget_claim"] = "Exact post-push tree size is checked separately; unknown parameters are not deleted to reach the limit."
    readable_json(destination / "process.json", small)
    note = (
        "# Ordinary deletion of reproducible data\n\n"
        "Storage administration only: no mathematical target or certificate is evaluated, and no data are uploaded to a Release or Actions artifact.\n\n"
        f"- Public repository: {REPOSITORY}.\n"
        f"- Immutable original commit: {original}.\n"
        f"- Actual run: {run_id}, attempt {attempt}.\n"
        f"- Selected original files: {len(requests)}; original bytes: {state['selected_original_versions_bytes']}.\n"
        f"- Staged ordinary deletions: {len(removable)}; bytes: {state['staged_deleted_original_bytes']}.\n"
        f"- Manifest: {name}; SHA-256 {receipt['sha256']}.\n"
        f"- Worker: {state['source_path']}; SHA-256 {state['source_sha256']}.\n\n"
        "The manifest retains each path, Git blob, byte count, SHA-256, predeletion commit, and available original producer/parameter/run metadata. Scripts, conclusions, small parameter/identity records, and explicitly named parameter inputs are retained. Concurrent newer versions are preserved.\n\n"
        "## Restore an original input for a continuing calculation\n\n"
        "Use the exact manifest entry in the public repository:\n\n"
        "~~~sh\n"
        "git show <predeletion_commit>:<original_path> > <temporary_scientific_file>\n"
        "~~~\n\n"
        "Verify the original byte count and SHA-256 before using the file with its unchanged scientific manifest. Restore only required files to an independent temporary science tree. This copies original bytes; it neither recomputes an accepted stage nor grants a new result. Do not recommit the data or upload it to a Release. Both old successes and failures remain identified by their original public commits and runs.\n"
    ).encode("utf-8")
    if len(note) > MAX_READABLE_BYTES:
        raise ValueError("restoration note exceeded the readable bound")
    atomic_bytes(destination / "README.md", note)
    git(repo, ["add", "--sparse", "--", dest_rel])
    if not args.publish:
        print(json.dumps({"complete": True, "published": False, "staged_metadata": dest_rel, "new_mathematics": 0}, sort_keys=True), flush=True)
        return
    git(repo, ["config", "user.name", "visible-exact-actions"])
    git(repo, ["config", "user.email", "visible-exact-actions@users.noreply.github.com"])
    git(repo, ["commit", "-m", "Remove reproducible visible-exact data with exact history restore metadata"])
    publication = sync.push_until_success()
    after = metadata_inventory(repo, publication, api)
    after_bytes = sum(item["bytes"] for item in after.values())
    final = {
        "kind": "actual_ordinary_data_deletion_publication",
        "run_id": run_id, "run_attempt": attempt,
        "ordinary_deletion_commit": publication, "predeletion_commit": original,
        "topic_bytes_at_published_commit": after_bytes,
        "topic_within_200000000_bytes": after_bytes <= MAX_TOPIC_BYTES,
        "current_main_size_metadata_is_exact": True,
        "new_mathematical_evaluations": 0, "old_mathematical_recomputations": 0,
        "Release_uploads": 0, "Actions_artifact_uploads": 0,
        "history_rewrites": 0, "force_pushes": 0,
        "upstream_changed_paths_retained_during_rebase": state["upstream_changed_paths_retained_during_rebase"],
        "pulls_and_readme_checks": state["pulls_and_readme_checks"],
        "large_retained_items": [
            {"path": p, "bytes": item["bytes"], "git_blob": item["git_blob"]}
            for p, item in sorted(after.items(), key=lambda pair: (-pair[1]["bytes"], pair[0]))[:20]
        ],
        "size_limit_if_unmet": "Known sources/parameters and unknown inputs remain listed for classification, not recomputation.",
    }
    readable_json(destination / "publication.json", final)
    git(repo, ["add", "--sparse", "--", dest_rel + "/publication.json"])
    git(repo, ["commit", "-m", "Record actual visible-exact cleanup size and publication identity"])
    receipt_commit = sync.push_until_success()
    exact_final_tree = metadata_inventory(repo, receipt_commit, api)
    exact_final_bytes = sum(item["bytes"] for item in exact_final_tree.values())
    print(json.dumps({
        "complete": True, "deletion_commit": publication,
        "receipt_commit": receipt_commit,
        "topic_bytes_before_publication_receipt": after_bytes,
        "topic_bytes_at_receipt_commit": exact_final_bytes,
        "topic_within_200000000_bytes_at_receipt_commit": exact_final_bytes <= MAX_TOPIC_BYTES,
        "new_mathematics": 0, "data_uploads": 0,
    }, sort_keys=True), flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(json.dumps({"complete": False, "new_mathematics": 0, "error_type": type(error).__name__, "error": redact(error)}, sort_keys=True), flush=True)
        traceback.print_exc()
        sys.exit(1)
