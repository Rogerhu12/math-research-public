#!/usr/bin/env python3
"""Lossless formatting of unreferenced legacy JSON metadata; no science."""
from pathlib import Path
from collections import Counter, defaultdict
import argparse
import hashlib
import json
import re
import subprocess

TOPIC = "topics/visible-flex-exact-nearby"
AREA = TOPIC + "/data/phase_ring_continuation/step5_ci_forward_blocks/"
RECEIPT = TOPIC + "/notes/2026-11-28-legacy-native-metadata-whitespace-twelfth.json"
EXT = {".py", ".json", ".yaml", ".yml", ".sh", ".js", ".mjs", ".ts", ".md"}
HEX = re.compile(r"[0-9a-fA-F]{40,64}")

def git(*args):
    return subprocess.check_output(["git", *args], text=True)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def compact(data):
    text = data.decode("utf-8")
    parts = []
    quoted = False
    escaped = False
    for c in text:
        if quoted:
            parts.append(c)
            if escaped:
                escaped = False
            elif c == "\\":
                escaped = True
            elif c == '"':
                quoted = False
        else:
            if c == '"':
                quoted = True
            if c not in " \t\r\n":
                parts.append(c)
    if quoted or escaped:
        raise ValueError("unfinished JSON string")
    out = ("".join(parts) + "\n").encode("utf-8")
    opts = dict(parse_int=str, parse_float=str)
    if json.loads(data, **opts) != json.loads(out, **opts):
        raise ValueError("JSON value changed")
    return out

def tracked_text_paths():
    paths = sorted(set(git("ls-files", "--cached", "--others", "--exclude-standard", "--", TOPIC, ".github", "README.md", "AGENTS.md").splitlines()))
    return paths, [p for p in paths if Path(p).suffix in EXT]

def blocked_references(rows):
    all_paths, text_paths = tracked_text_paths()
    leaf_counts = Counter(Path(p).name for p in all_paths)
    hash_to_ids = defaultdict(set)
    needles = {}
    for i, row in enumerate(rows):
        p = row["path"]
        short = p[len(TOPIC)+1:] if p.startswith(TOPIC+"/") else p
        values = {p, short, str(Path(p).parent), str(Path(short).parent)}
        if leaf_counts[Path(p).name] == 1:
            values.add(Path(p).name)
        needles[i] = tuple(sorted(values, key=len, reverse=True))
        hash_to_ids[row["original_sha256"].lower()].add(i)
        hash_to_ids[row["original_git_blob_sha"].lower()].add(i)
    blocked = {}
    examined = 0
    for ref in text_paths:
        if ref == RECEIPT:
            continue
        raw = Path(ref).read_bytes()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            continue
        examined += 1
        for token in HEX.findall(text):
            for i in hash_to_ids.get(token.lower(), ()):
                if ref != rows[i]["path"]:
                    blocked.setdefault(i, ref)
        if "step5_ci_forward_blocks" in text:
            for i, vals in needles.items():
                if ref != rows[i]["path"] and any(v in text for v in vals):
                    blocked.setdefault(i, ref)
        # A unique leaf could be mentioned without its parent path.
        for i, row in enumerate(rows):
            leaf = Path(row["path"]).name
            if leaf_counts[leaf] == 1 and ref != row["path"] and leaf in text:
                blocked.setdefault(i, ref)
    return blocked, examined

def prepare():
    if Path(RECEIPT).exists():
        print(json.dumps({"already_has_complete_receipt": RECEIPT}))
        return
    baseline = git("rev-parse", "HEAD").strip()
    lines = git("ls-tree", "-r", "-l", "HEAD", "--", AREA).splitlines()
    candidates = []
    payload = {}
    for line in lines:
        meta, name = line.split("\t", 1)
        mode, kind, oid, size = meta.split()
        size = int(size)
        if kind != "blob" or not name.endswith("/manifest.json"):
            continue
        if not 20000 <= size < 40000:
            continue
        data = Path(name).read_bytes()
        if len(data) != size or blob_sha(data) != oid:
            raise ValueError("current whole Git identity differs: " + name)
        new = compact(data)
        if len(data) - len(new) < 6000:
            continue
        row = dict(path=name, bytes=len(data), compact_bytes=len(new),
                   saving=len(data)-len(new), original_sha256=sha(data),
                   original_git_blob_sha=oid, compact_sha256=sha(new))
        candidates.append(row)
        payload[name] = new
        if len(candidates) >= 512:
            break
    if len(candidates) < 200:
        raise ValueError("insufficient fresh eligible metadata")
    blocked, examined = blocked_references(candidates)
    selected = [row for i, row in enumerate(candidates) if i not in blocked][:200]
    if len(selected) != 200:
        raise ValueError("insufficient unreferenced complete metadata")
    receipt = {
        "schema": "lossless-json-whitespace-compaction/v1",
        "original_complete_commit": baseline,
        "batch": "twelfth-200-new-current-metadata-manifests",
        "method": (
            "Delete only ASCII JSON whitespace outside strings, retain final LF. "
            "All strings, escapes, literal numbers, keys, values and array order "
            "are unchanged. Complete originals remain at original_complete_commit. "
            "This formats metadata and executes no scientific target."
        ),
        "reference_filter": (
            "Exclude whole root/topic path, complete parent path, unique leaf, "
            "whole original SHA256 or Git blob references in every other current "
            "tracked or untracked Python/JSON/YAML/shell/JavaScript/TypeScript/Markdown "
            "file under this topic and .github, plus root README/AGENTS, including "
            "all published and new actual manifests/workflows. "
            "Repeat this check after every pull before push."
        ),
        "tracked_source_and_manifest_files_examined": examined,
        "candidate_count": len(candidates),
        "excluded_candidate_count": len(blocked),
        "files": selected,
    }
    encoded = (json.dumps(receipt, ensure_ascii=False, separators=(",", ":")) + "\n").encode()
    if len(encoded) >= 100000:
        raise ValueError("complete receipt exceeds text limit")
    # All identity, lexical, semantic and reference checks precede every mutation.
    for row in selected:
        data = Path(row["path"]).read_bytes()
        if len(data) != row["bytes"] or sha(data) != row["original_sha256"]:
            raise ValueError("whole original changed before write")
    for row in selected:
        Path(row["path"]).write_bytes(payload[row["path"]])
    Path(RECEIPT).write_bytes(encoded)
    subprocess.check_call(["git", "add", "--",
                           *[row["path"] for row in selected], RECEIPT])
    print(json.dumps({
        "complete_files": len(selected),
        "gross_bytes_released": sum(r["saving"] for r in selected),
        "whole_receipt_bytes": len(encoded),
        "net_bytes_released": sum(r["saving"] for r in selected)-len(encoded),
        "old_scientific_targets_executed": 0,
        "receipt": RECEIPT,
        "receipt_sha256": sha(encoded),
        "original_complete_commit": baseline,
    }, sort_keys=True))

def recheck():
    r = json.loads(Path(RECEIPT).read_bytes())
    rows = r["files"]
    if len(rows) != 200:
        raise ValueError("partial receipt")
    for row in rows:
        data = Path(row["path"]).read_bytes()
        if len(data) != row["compact_bytes"] or sha(data) != row["compact_sha256"]:
            raise ValueError("complete compact identity changed")
    blocked, examined = blocked_references(rows)
    if blocked:
        print(json.dumps({"new_current_references": [
            {"candidate": rows[i]["path"], "source": ref}
            for i, ref in sorted(blocked.items())]}, sort_keys=True))
        raise ValueError("new current input reference; do not publish")
    print(json.dumps({"complete_files_rechecked": 200,
                      "current_source_manifest_files": examined,
                      "reference_conflicts": 0,
                      "old_scientific_targets_executed": 0}))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--recheck", action="store_true")
    args = parser.parse_args()
    if args.recheck:
        recheck()
    else:
        prepare()
