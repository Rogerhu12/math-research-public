#!/usr/bin/env python3
"""Remove nine confirmed computational outputs; exact historical bytes remain recoverable.

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
# Only these reviewed, exact original output versions may be removed.
# The earlier 11834-file deletion and its complete metadata remain untouched.
CONFIRMED_OUTPUTS = json.loads(r'''[
  {
    "bytes": 2136984,
    "git_blob": "03e122dfc261f9e1341fbc2fcb491db1e5e3c06d",
    "path": "topics/visible-flex-exact-nearby/notes/2026-11-14-R133-complete-correlated-first-phase-parameter-native.json.gz",
    "sha256": "67d3dcbfa415173db552286cabac03f4c9daba521fff3b68d4af9d28eed478da",
    "producer_path": "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_phase_correlated_first_parameter.py",
    "run_reference": "Original report states the run; no Actions run ID is invented.",
    "classification_evidence": {
      "path": "topics/visible-flex-exact-nearby/results/R133-supplement-complete-correlated-phase-twist-and-true-defect-corrections.md",
      "git_blob": "c208ea0210bcbcea1de3ac89f821f2556870c3f1",
      "bytes": 10594,
      "sha256": "cd9530e2d7ecc020ead866d1089419a8daf52e3c3a25e74ce03652d08df96f11"
    },
    "reason": "Complete computed 3095-row correlated first-parameter certificate. The preserved report records its producer, command, six gates and actual local runtime; it is not an input-parameter definition.",
    "parameters_reference": "The retained producer/report and exact historical native retain the original mathematical parameters. This storage worker does not alter or infer them."
  },
  {
    "bytes": 1403016,
    "git_blob": "a28d2b35bbda95a508e82b3b48efeb4bd6c87e0c",
    "path": "topics/visible-flex-exact-nearby/notes/first_symbol_parameter_transfer_ci/run-43597209022-1/consumers/first-symbol-parameter-transfer.json.gz",
    "sha256": "06070fd3b4bd7a3e4ba17d99821c0f6ad06393863bf538f9a8157b6187e60dbb",
    "producer_path": "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_first_symbol_parameter_transfer.py",
    "run_reference": "43597209022/1",
    "classification_evidence": {
      "path": "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_first_symbol_parameter_transfer.py",
      "git_blob": "4393d55b6ee8152e6d1551d6343e62749969bf79",
      "bytes": 26531,
      "sha256": "de12b8129caeb8c51857f6b44a152c7a91e1facbdc553d2bd4f4ea320a38406a"
    },
    "reason": "Complete finite-part parameter-transfer computed output; the retained producer writes this native with complete computed rows and gates.",
    "parameters_reference": "The retained producer/report and exact historical native retain the original mathematical parameters. This storage worker does not alter or infer them."
  },
  {
    "bytes": 700195,
    "git_blob": "dbb29c3735bef5bb74ec88ecca4b503e4cf18324",
    "path": "topics/visible-flex-exact-nearby/notes/2026-11-13-R106-seven-field-moving-parameter-bidisk.json.gz",
    "sha256": "1b0c96c08ea72e16fddeabf91b74d81f539c4819a50af44ab97ec74f338778f8",
    "producer_path": "topics/visible-flex-exact-nearby/scripts/fourfold_subprincipal_root_parameter_bidisk.py",
    "run_reference": "Original report records 256-bit computation; no Actions run ID is inferred.",
    "classification_evidence": {
      "path": "topics/visible-flex-exact-nearby/results/R106-supplement-moving-root-parameter-fields.md",
      "git_blob": "bdab2e80c530d0ad147ab707193937762b23a019",
      "bytes": 8940,
      "sha256": "ce04478af57c60742d90106f92faead5a1adc8f581c93ab19d49a1e0fdd4515d"
    },
    "reason": "1024-cell computed seven-field bidisk modulus certificate; the report distinguishes the parameter domain from this numerical output.",
    "parameters_reference": "The retained producer/report and exact historical native retain the original mathematical parameters. This storage worker does not alter or infer them."
  },
  {
    "bytes": 678654,
    "git_blob": "df8641305a1f3b08b13d93b4b52400d35c00fa62",
    "path": "topics/visible-flex-exact-nearby/notes/2026-11-13-negative-root-physical-graph-operator.json",
    "sha256": "e4b3faf5ae998607207246367a430d80a1fdac7e404d1b013e66b9c373124cb5",
    "producer_path": "topics/visible-flex-exact-nearby/scripts/fourfold_negative_root_physical_graph_operator.py",
    "run_reference": "Original complete report and immutable history identify the calculation.",
    "classification_evidence": {
      "path": "topics/visible-flex-exact-nearby/results/R43-supplement-actual-physical-graph-strong-connector.md",
      "git_blob": "ba584b3731b2339c5a0e018dab7a4ac2dc1e4f01",
      "bytes": 23689,
      "sha256": "9d6154cf3050ed8c70d2d1feb4fbaad76d4bf5ab5a97c1ae16016a83fe9362ad"
    },
    "reason": "Complete computed physical-graph operator budget; retained proof explicitly gives the producer, output SHA and command.",
    "parameters_reference": "The retained producer/report and exact historical native retain the original mathematical parameters. This storage worker does not alter or infer them."
  },
  {
    "bytes": 673138,
    "git_blob": "b9cd2fb10207d6123d89ccadbb229ade77a314e9",
    "path": "topics/visible-flex-exact-nearby/notes/2026-11-13-R46-windowed-density-strong-budget.json",
    "sha256": "bb8f8b4751f87f8a41ce219a8722fff5976ce233a009c90952682c3f2d24539b",
    "producer_path": "topics/visible-flex-exact-nearby/scripts/fourfold_strict_windowed_density_R46.py",
    "run_reference": "Original report records the actual 3.86-second calculation.",
    "classification_evidence": {
      "path": "topics/visible-flex-exact-nearby/results/R46-supplement-requested-window-density-strong-budget.md",
      "git_blob": "2d289dc442c0afdbfaccb4033443251b9f4a4a23",
      "bytes": 18043,
      "sha256": "4dc12e62515504757d7940ab5a1cfff25e8a58600a536aa2c85630b7507c4a4e"
    },
    "reason": "Computed full strict requested-window density budget; command has scales 4096 16384 65536 1048576, windows 0 4/3 2 8, and 320 bits.",
    "parameters_reference": "The retained producer/report and exact historical native retain the original mathematical parameters. This storage worker does not alter or infer them."
  },
  {
    "bytes": 578238,
    "git_blob": "b9f2f61e0f6ed566131c565f80cc3194f4a004c2",
    "path": "topics/visible-flex-exact-nearby/notes/2026-11-12-actual-direct-canonical-source-budget.json",
    "sha256": "b568783f5270102aac2ed2d9656c6e86cc6acdce734358e53a0ac4a265513d3c",
    "producer_path": null,
    "run_reference": "Original R96-R98 ready manifest; original producer is not replaced by its publisher.",
    "classification_evidence": {
      "path": "topics/visible-flex-exact-nearby/scripts/fourfold_phase_canonical_mixed_publish.py",
      "commit": "9dc01afb868480521a7b8287a9c7d06365890150",
      "exact_evidence": "budget=json.loads(a.budget.read_text()); requires budget[proved] and actual_cells==178; copies a.budget to this exact output path and records original budget[source_sha256].",
      "original_identity_manifest": "topics/visible-flex-exact-nearby/notes/2026-11-12-R96-R98-ready-manifest.json"
    },
    "reason": "Exact published copy of the completed 178-cell R96 source budget, not a domain or parameter definition. Its original producer SHA is retained in its historical bytes and the small publication summary.",
    "parameters_reference": "The retained producer/report and exact historical native retain the original mathematical parameters. This storage worker does not alter or infer them."
  },
  {
    "bytes": 530379,
    "git_blob": "3df14b1adb42b90d21f279104c52e5cca2f345f3",
    "path": "topics/visible-flex-exact-nearby/notes/2026-11-13-negative-root-full-Airy-operator.json",
    "sha256": "4a84d560b61efbd3abc44566fe9ae201a7677682a8de7e1062e2c2fc97a8138d",
    "producer_path": "topics/visible-flex-exact-nearby/scripts/fourfold_negative_root_full_Airy_operator.py",
    "run_reference": "Original report records 320 bits and the actual 0.707-second computation.",
    "classification_evidence": {
      "path": "topics/visible-flex-exact-nearby/results/R43-supplement-full-root-Airy-operator-and-scaled-strong-remainder.md",
      "git_blob": "44d4c0618ba06096458d4df3ece81040b8950693",
      "bytes": 19327,
      "sha256": "3596f7f12eb08e09f86d039b9487c3320793c49bf93e58daab2ae475910e6e14"
    },
    "reason": "Full computed root Airy operator and scaled strong-remainder budget, explicitly reproduced with this output path.",
    "parameters_reference": "The retained producer/report and exact historical native retain the original mathematical parameters. This storage worker does not alter or infer them."
  },
  {
    "bytes": 476832,
    "git_blob": "d2d3a1f47042e6604e7ce42ab97d15487c303ce6",
    "path": "topics/visible-flex-exact-nearby/notes/2026-11-13-Codazzi-r005-signed-frame-embedding-native.json",
    "sha256": "05caf21b39edb95ebae0c8229665277342f5673c9dd710b42cdf48dc0580d836",
    "producer_path": "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_signed_frame_embedding.py",
    "run_reference": "Original R129 report identifies the signed-frame calculation.",
    "classification_evidence": {
      "path": "topics/visible-flex-exact-nearby/results/R129-piecewise-certified-exact-waist-to-005.md",
      "git_blob": "fb2e7de24507a687e1964bb98e24a17cacd9cf43",
      "bytes": 11364,
      "sha256": "ccc4b6fc62c894a3ccfcc89c568be2461af9a77a004bbae120f908eb0e003ba6"
    },
    "reason": "Complete computed 168-box signed-frame embedding native, with full original command and output SHA in the retained proof.",
    "parameters_reference": "The retained producer/report and exact historical native retain the original mathematical parameters. This storage worker does not alter or infer them."
  },
  {
    "bytes": 429768,
    "git_blob": "edee1f71602c28fa103bd1db0cb9670fbe47c8e5",
    "path": "topics/visible-flex-exact-nearby/notes/2026-11-13-actual-high-density-first-phase-two-window.json",
    "sha256": null,
    "producer_path": "topics/visible-flex-exact-nearby/scripts/fourfold_actual_high_density_first_phase.py",
    "run_reference": "Original full calculation is identified in the retained report; no later consumer is called its producer.",
    "classification_evidence": {
      "path": "topics/visible-flex-exact-nearby/results/R46-supplement-actual-high-density-first-phase-and-two-order-remainder.md",
      "git_blob": "ed9de8ff2fe7c9c5170838f5b21c4db3f37782e9",
      "bytes": 15955,
      "sha256": "00ff2302e59abcd12335e1f0ec1910a55833d6fea8042752bef90b569db5a141"
    },
    "reason": "Complete calculated high-density first-phase coefficient and two-window operator budget; section 7 identifies the exact producer and output command.",
    "parameters_reference": "The retained producer/report and exact historical native retain the original mathematical parameters. This storage worker does not alter or infer them."
  }
]''')
CONFIRMED_BY_PATH = {row["path"]: row for row in CONFIRMED_OUTPUTS}
PRIOR_RUN = "43679889657"
PRIOR_DELETION_COMMIT = "315bf6e06a2e21fae980f538286dcec6b739bc59"
PRIOR_RECEIPTS = json.loads(r'''[
  {
    "git_blob": "35272be389900b3e7e2be540359f71f59a09f844",
    "bytes": 1652,
    "sha256": "517e1cac985b27ec7d97c273e57ab42b788c5e02f4558c148be6eaae98756f9f"
  },
  {
    "git_blob": "1f6af7c04aabee98aba07fb5a65e0e9364a64786",
    "bytes": 6608,
    "sha256": "171441b39420be0c18e3f349718d54eca32603984fea8945b7f79b5fb5a720eb"
  },
  {
    "git_blob": "b750911e73e0fab8bef458193328ac85c63704eb",
    "bytes": 9466,
    "sha256": "eefd8712891355dbc03636a8741ca747d14b5ec21fa658c31f61569763281bc7"
  }
]''')


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
    reviewed = CONFIRMED_BY_PATH.get(path)
    if reviewed is None:
        return "retain_outside_exact_allowlist", "not one of the nine reviewed original computational outputs"
    if item["mode"] not in ("100644", "100755"):
        return "retain_changed_reviewed_path", "nonregular object retained"
    if (item["git_blob"], item["bytes"]) != (reviewed["git_blob"], reviewed["bytes"]):
        return "retain_changed_reviewed_path", "a different version at a reviewed path is not authorized by this exact allowlist"
    return "delete_reproducible", reviewed["reason"]


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


def verify_prior_receipts(repo):
    receipts = []
    for item in PRIOR_RECEIPTS:
        raw = blob_bytes(repo, item["git_blob"], item["bytes"])
        if sha256(raw) != item["sha256"]:
            raise ValueError("the original storage-only cleanup receipt changed")
        receipts.append(dict(item))
    return receipts


class Provenance:
    def __init__(self, repo, tree, decisions):
        self.groups = {}

    def for_path(self, path):
        reviewed = dict(CONFIRMED_BY_PATH[path])
        record = {
            "reviewed_original_output": reviewed,
            "original_directory": str(PurePosixPath(path).parent),
            "producer_resolution": "Only the already read producer/report evidence listed here is used; no producer is invented.",
            "old_11834_deletion_original_bytes_rehashed": 0,
            "unlisted_recomputable_data_payloads_read": 0,
        }
        identity = sha256(canonical(record))
        self.groups[identity] = record
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
    dest_rel = TOPIC + "/notes/data_cleanup_confirmed_outputs/" + suffix
    destination = repo / dest_rel
    source = Path(__file__).resolve()
    state = {
        "kind": "ordinary_public_topic_nine_confirmed_output_deletion",
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
    prior_receipts = verify_prior_receipts(repo)
    state.update(
        original_storage_run=PRIOR_RUN,
        original_storage_deletion_commit=PRIOR_DELETION_COMMIT,
        original_small_receipts=prior_receipts,
        exact_reviewed_output_paths=len(CONFIRMED_OUTPUTS),
        original_11834_data_bytes_rehashed=0,
        unlisted_recomputable_data_payloads_read=0,
        automatic_broad_data_classification_used=False,
    )
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
        actual_sha = hash_original_blob(repo, item["git_blob"], item["bytes"])
        expected_sha = CONFIRMED_BY_PATH[path].get("sha256")
        if expected_sha is not None and actual_sha != expected_sha:
            raise ValueError("a reviewed computational output changed its exact SHA-256")
        requests.append({
            "path": path, "bytes": item["bytes"],
            "sha256": actual_sha,
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
        "parameters": {"reviewed_rules_path": args.reviewed_rules, "reviewed_rules_sha256": RULES_SHA256, "maximum_topic_bytes": MAX_TOPIC_BYTES,
            "selection": "only nine exact path/Git-blob/byte-count triples reviewed as computed outputs"},
        "complete_reviewed_output_allowlist": CONFIRMED_OUTPUTS,
        "original_cleanup_receipts": prior_receipts,
        "original_cleanup_run": PRIOR_RUN,
        "old_11834_original_data_bytes_rehashed": 0,
        "unlisted_recomputable_data_payloads_read": 0,
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
        "# Ordinary deletion of nine confirmed computational outputs\n\n"
        "Storage administration only: no mathematical target or certificate is evaluated, and no data are uploaded to a Release or Actions artifact.\n\n"
        f"- Public repository: {REPOSITORY}.\n"
        f"- Immutable original commit: {original}.\n"
        f"- Actual run: {run_id}, attempt {attempt}.\n"
        f"- Selected original files: {len(requests)}; original bytes: {state['selected_original_versions_bytes']}.\n"
        f"- Staged ordinary deletions: {len(removable)}; bytes: {state['staged_deleted_original_bytes']}.\n"
        f"- Manifest: {name}; SHA-256 {receipt['sha256']}.\n"
        f"- Worker: {state['source_path']}; SHA-256 {state['source_sha256']}.\n\n"
        "The exact nine-path allowlist comes from the first cleanup's retained-file inventory and individually read producer/report evidence. No generic filename classification is reused. The previous 11834 deleted files are not rehashed; only the nine reviewed output versions are eligible. The manifest retains every exact path, Git blob, byte count, SHA-256, predeletion commit and original producer/parameter/run reference. All scripts, conclusions, parameter/identity records and unlisted paths remain. Concurrent newer versions are preserved.\n\n"
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
    git(repo, ["commit", "-m", "Remove nine reviewed visible-exact computed outputs with exact history restore metadata"])
    publication = sync.push_until_success()
    after = metadata_inventory(repo, publication, api)
    after_bytes = sum(item["bytes"] for item in after.values())
    final = {
        "kind": "actual_nine_confirmed_output_deletion_publication",
        "run_id": run_id, "run_attempt": attempt,
        "ordinary_deletion_commit": publication, "predeletion_commit": original,
        "topic_bytes_at_published_commit": after_bytes,
        "topic_within_200000000_bytes": after_bytes <= MAX_TOPIC_BYTES,
        "current_main_size_metadata_is_exact": True,
        "exact_reviewed_output_paths": len(CONFIRMED_OUTPUTS),
        "original_cleanup_run": PRIOR_RUN,
        "original_cleanup_deletion_commit": PRIOR_DELETION_COMMIT,
        "old_11834_original_data_bytes_rehashed": 0,
        "unlisted_recomputable_data_payloads_read": 0,
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
    if not args.audit_only and exact_final_bytes > MAX_TOPIC_BYTES:
        raise ValueError("ordinary deletion and exact receipt were published, but the actual receipt tree remains above 200000000 bytes; no unreviewed file was deleted")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(json.dumps({"complete": False, "new_mathematics": 0, "error_type": type(error).__name__, "error": redact(error)}, sort_keys=True), flush=True)
        traceback.print_exc()
        sys.exit(1)
