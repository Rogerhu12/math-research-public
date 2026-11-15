#!/usr/bin/env python3
"""Root rule 15: hash historical outputs; create immutable provenance blobs only."""
import hashlib, json, os, pathlib, re, subprocess, urllib.request
ROOT = pathlib.Path(__file__).resolve().parents[3]
TOPIC = pathlib.Path(__file__).resolve().parents[1]
PREFIX = TOPIC.relative_to(ROOT).as_posix()
REPO = "Rogerhu12/math-research-public"
def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)
SOURCE = os.environ.get("GITHUB_SHA") or git("rev-parse", "HEAD").decode().strip()
RUN = os.environ.get("GITHUB_RUN_ID")
LANGS = {".py", ".js", ".sage", ".magma", ".m", ".wl", ".sh", ".ts"}
OUTPUTS = {".json", ".csv", ".tsv", ".txt", ".out", ".log", ".gz", ".bin", ".dat"}
EXEMPT = re.compile(r"(?:^|[-_.])(manifest|request|receipt|inventory|config|parameters|params|hashes|lock)(?:[-_.]|$)", re.I)
files = [ROOT / p for p in git("ls-files", "-z", "--", PREFIX).decode().split("\0") if p]
by_stem, by_round = {}, {}
for p in files:
    if p.suffix.lower() not in LANGS:
        continue
    by_stem.setdefault(p.stem.lower(), []).append(p)
    match = re.search(r"(?:^|[-_])r(\d+)(?:[-_.]|$)", p.name.lower())
    if match:
        by_round.setdefault(int(match.group(1)), []).append(p)
records, uncertain = [], []
for p in files:
    rel = p.relative_to(TOPIC).as_posix()
    if p.suffix.lower() not in OUTPUTS or rel.startswith("ci/") or EXEMPT.search(p.name):
        continue
    stem = p.name
    while pathlib.Path(stem).suffix.lower() in OUTPUTS:
        stem = pathlib.Path(stem).stem
    exact = by_stem.get(stem.lower(), [])
    match = re.search(r"(?:^|[-_])r(\d+)(?:[-_.]|$)", p.name.lower())
    number = int(match.group(1)) if match else None
    candidates = exact or by_round.get(number, [])
    record = {
        "path": p.relative_to(ROOT).as_posix(), "bytes": p.stat().st_size,
        "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
        "git_blob": git("rev-parse", SOURCE + ":" + p.relative_to(ROOT).as_posix()).decode().strip(),
        "producer_candidates": [x.relative_to(ROOT).as_posix() for x in candidates],
        "producer_match": "same_stem" if exact else "same_result_number" if candidates else "unresolved",
        "result_number": number,
    }
    (records if exact else uncertain).append(record)
references = []
for p in files:
    if p.suffix.lower() != ".md":
        continue
    data = p.read_text(encoding="utf-8")
    count = sum(1 for x in records if pathlib.PurePosixPath(x["path"]).name in data)
    if count:
        references.append({"path": p.relative_to(ROOT).as_posix(), "matched_output_names": count})
def create_manifest(name, entries):
    value = {
        "schema": "rank2-recomputable-output-provenance-v1",
        "source_commit": SOURCE, "audit_run": int(RUN) if RUN else None,
        "computation_rerun": False,
        "note": "This audit hashes historical outputs; it does not rerun or certify computations. Original parameters and execution provenance remain in the result, script, workflow and log. No output bytes are copied here.",
        "entries": entries,
    }
    content = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"
    raw = content.encode()
    if len(raw) >= 90000:
        raise RuntimeError("Manifest exceeds text limit: " + name)
    req = urllib.request.Request(
        "https://api.github.com/repos/" + REPO + "/git/blobs",
        data=json.dumps({"content": content, "encoding": "utf-8"}).encode(),
        headers={"Authorization": "Bearer " + os.environ["GH_TOKEN"],
                 "Accept": "application/vnd.github+json", "User-Agent": "rank2-rule15-audit",
                 "Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=60) as response:
        result = json.load(response)
    return {"name": name, "sha": result["sha"], "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest(), "entry_count": len(entries)}
outputs = []
for label, source in [("outputs", records), ("review", uncertain)]:
    for group in sorted({(x["result_number"] or 0) // 50 for x in source}):
        entries = [x for x in source if (x["result_number"] or 0) // 50 == group]
        outputs.append(create_manifest(label + "-r%03d-r%03d.json" % (50 * group, 50 * group + 49), entries))
if references:
    outputs.append(create_manifest("documentation-references.json", references))
summary = {"source_commit": SOURCE, "audit_run": int(RUN) if RUN else None,
           "exact_producer_outputs": len(records), "exact_output_bytes": sum(x["bytes"] for x in records),
           "needs_classification": len(uncertain), "classified_output_bytes": sum(x["bytes"] for x in uncertain),
           "manifests": outputs, "ref_mutations": False, "output_bytes_published": False}
print("RANK2_RECOMPUTABLE_OUTPUT_AUDIT " + json.dumps(summary, ensure_ascii=False))
