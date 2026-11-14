#!/usr/bin/env python3
"""Read-only identity checks for the frozen per-request DN continuation plan.

This imports no numerical engine and reads only the frozen source/closed-record
allowlist below.  It does not inspect the active continuation03 process/files.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path


TOPIC = Path(__file__).resolve().parents[1]
NOTES = TOPIC / "notes"
P = "2026-11-09-db6f-"
PREFIX = P + "prefix-matched-cut-linear-dn-continuation"
PINNED = {
    PREFIX + "-plan.md": "62e59c6b5c4ed63b492db830320497c4e36e0369f5b414c637b117adfbddf7d1",
    PREFIX + "-plan-v2.md": "a65890daff2c55ff8e0593445c0f7689e06d445024e87988444160762da04fe6",
    PREFIX + "-sources.json": "f0be47e98594c8e46ff6597257dd034fffe88c23becfcb6432fcdbbc2d02c922",
    PREFIX + "-v2-sources.json": "b0af556d2cc5aae09bbe4a0eb43be7d20ae75bbc987de759f43741eb77a5f983",
    PREFIX + "-publication.json": "d8f1e74d8245f74ac6d86d1d82c899c26d6a6c3d2331585213fb9a9ac654391b",
    PREFIX + "-v2-publication.json": "1452e309eb3560087b25c1856f8478c7f011deffb831270692a4b5d2e3a4c661",
    PREFIX + "-diagnosis.json": "c15fe8ad4b26adea9638acca728bcf170d7cae744b10e1b66b2e923cbacdd702",
    PREFIX + "-observed-execution.json": "867b1bba535fe69f1e488e76e2a87b1c9b04f7b43d9b1f4e555a7cfc527d6c3e",
}
INPUT_NAME = P + "prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-matched-cut-s63of64-01-input-bindings.json"
INPUT_SHA = "5b184918f4c5a86f10189c5433cd447af4a822856a2fe569df4439e03efdeb21"
ENGINE_NAMES = (
    "general_root_tail_momentum.mjs",
    "f6tail_fast_momentum.mjs",
    "f6tail_fast_split_flux_engine.mjs",
    "f6tail_cusp_grid.mjs",
    "f6tail_momentum_split_flux.mjs",
)


def digest(b):
    return hashlib.sha256(b).hexdigest()


def checked_path(path):
    p = Path(path)
    if not p.is_absolute():
        p = TOPIC / p
    p = p.resolve(strict=True)
    if not p.is_relative_to(TOPIC):
        raise ValueError("Read outside this topic is not allowed")
    return p


def read_pinned(path, sha, size=None):
    p = checked_path(path)
    b = p.read_bytes()
    if digest(b) != sha or (size is not None and len(b) != size):
        raise ValueError("Frozen identity mismatch: " + str(p))
    return b, {"path": str(p.relative_to(TOPIC)), "bytes": len(b), "sha256": sha}


def record(rec):
    return read_pinned(rec["path"], rec["sha256"], rec["bytes"])[1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(NOTES / (P + "tail-review-linear-dn-plan-check.json")))
    a = ap.parse_args()
    out = Path(a.out).resolve()
    if not out.is_relative_to(NOTES) or out.exists():
        raise ValueError("Use a new output under this topic's notes")
    loaded, identities = {}, []
    for name, sha in PINNED.items():
        b, r = read_pinned(NOTES / name, sha)
        identities.append(r)
        loaded[name] = b
    led = json.loads(loaded[PREFIX + "-sources.json"])
    direct = [record(r) for r in led["direct_and_closed_sources"]]
    if len(direct) != 32:
        raise ValueError("Unexpected direct/closed source count")
    v2led = json.loads(loaded[PREFIX + "-v2-sources.json"])
    for key in ("v1", "v1_sources", "v1_publication", "v2"):
        record(v2led[key])
    transformed = loaded[PREFIX + "-plan.md"].decode("utf-8")
    reps = v2led["replacements"]
    if len(reps) != 4:
        raise ValueError("Expected exactly the four frozen replacements")
    for rep in reps:
        if transformed.count(rep["before"]) != 1:
            raise ValueError("Replacement source is not unique")
        transformed = transformed.replace(rep["before"], rep["after"])
    if transformed.encode("utf-8") != loaded[PREFIX + "-plan-v2.md"]:
        raise ValueError("V2 has an unrecorded textual change")
    publication_counts = []
    for suffix, count in (("-publication.json", 5), ("-v2-publication.json", 2)):
        pub = json.loads(loaded[PREFIX + suffix])
        rows = [record(r) for r in pub["files"]]
        if len(rows) != count or sum(r["bytes"] for r in rows) != pub["total_bytes"]:
            raise ValueError("Publication ledger count/size mismatch")
        publication_counts.append(count)
    ib, input_identity = read_pinned(NOTES / INPUT_NAME, INPUT_SHA)
    inputs = json.loads(ib)
    command = inputs["command"]
    source_root = checked_path(command[command.index("--source-root") + 1])
    if source_root != TOPIC / "repro" / "source-root":
        raise ValueError("Unexpected actual source-root")
    input_map = {str(Path(r["path"]).resolve()): r for r in inputs["bound_files"]}
    if len(input_map) != 121:
        raise ValueError("Unexpected original binding-document size")
    engines = []
    for name in ENGINE_NAMES:
        p = source_root / "topics" / "large-amplitude-twist-flex" / "scripts" / name
        engines.append(record(input_map[str(p)]))
    replay = NOTES / (P + "tail-review-linear-dn-closed-diagnosis-replay.json")
    rb, replay_identity = read_pinned(replay, PINNED[PREFIX + "-diagnosis.json"])
    if rb != loaded[PREFIX + "-diagnosis.json"]:
        raise ValueError("Closed metadata replay differs")
    parsed = []
    for name in ("db6f-prefix-tail-trial-client.py", "db6f-prefix-coupled.py",
                 "db6f-prefix-flat-trial-coupled.py"):
        p = TOPIC / "scripts" / name
        source = p.read_bytes()
        ast.parse(source, filename=str(p))
        parsed.append({"file": str(p.relative_to(TOPIC)), "sha256": digest(source)})
    gates = led["original_gate_unchanged"]
    expected = {"solveTolerance": 2e-9, "maxIterations": 36, "projectionFloor": .05,
                "modes": 15, "quadrature": 256, "shootingParts": 8,
                "steps": 32, "physicalDepth": 12}
    canonical = lambda o: json.dumps(o, sort_keys=True, separators=(",", ":"), allow_nan=False)
    if canonical(gates) != canonical(expected):
        raise ValueError("Original gate declaration changed")
    report = {
        "status": "PASS_STATIC_BINDINGS_AND_CLOSED_METADATA_REPLAY",
        "scope": "Identity checks, exact four-change reconstruction, syntax parsing only; the mathematical/control-flow review is a separate note. No imported numerical modules or subprocesses.",
        "script": {"file": str(Path(__file__).resolve().relative_to(TOPIC)),
                   "sha256": digest(Path(__file__).read_bytes())},
        "frozen_documents": identities,
        "direct_and_closed_source_count_rehashed": len(direct),
        "direct_and_closed_sources": direct,
        "original_input_binding": input_identity,
        "original_binding_record_count": 121,
        "whole_121_file_rehash_claimed": False,
        "selected_actual_source_root_files_rehashed": engines,
        "exact_replacements": len(reps),
        "v1_to_v2_reconstruction_byte_equal": True,
        "publication_counts": publication_counts,
        "metadata_replay": replay_identity,
        "metadata_replay_byte_equal_to_author": True,
        "syntax_only": parsed,
        "original_gate_unchanged": gates,
        "new_solver_calls": 0,
        "active_continuation03_files_read": 0,
        "git_commands_or_mutations": 0,
    }
    data = (json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode()
    with out.open("xb") as f:
        f.write(data)
    print(json.dumps({"status": report["status"], "file": str(out),
                      "bytes": len(data), "sha256": digest(data),
                      "direct_sources": len(direct), "selected_engine_sources": len(engines)},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()
