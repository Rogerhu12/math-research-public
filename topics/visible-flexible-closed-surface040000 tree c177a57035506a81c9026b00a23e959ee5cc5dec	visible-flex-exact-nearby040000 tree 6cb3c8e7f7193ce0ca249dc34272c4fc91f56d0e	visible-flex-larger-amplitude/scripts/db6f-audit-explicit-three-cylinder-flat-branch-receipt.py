#!/usr/bin/env python3
"""Record a closed, immutable-source execution receipt for the flat disk proof."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time


TOPIC = Path(__file__).resolve().parent.parent
STEM = "2026-11-09-db6f-audit-explicit-three-cylinder-flat-branch"
SCRIPT = TOPIC / "scripts/db6f-audit-explicit-three-cylinder-flat-branch.py"
PROOF = TOPIC / "notes" / (STEM + ".md")
FROZEN = TOPIC / "notes" / (STEM + ".json")
ERRATUM = TOPIC / "notes" / (STEM + "-erratum.md")
REPLAY = TOPIC / "notes" / (STEM + "-receipt-replay.json")
SOURCES = TOPIC / "notes" / (STEM + "-sources.json")
OBSERVED = TOPIC / "notes" / (STEM + "-observed.json")
PUBLICATION = TOPIC / "notes" / (STEM + "-publication.json")


def utc():
    return datetime.now(timezone.utc).isoformat()


def entry(path):
    data = path.read_bytes()
    return {"path": str(path.relative_to(TOPIC)), "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def write(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def main():
    for output in (REPLAY, SOURCES, OBSERVED, PUBLICATION):
        if output.exists():
            raise FileExistsError(f"Refusing to overwrite execution evidence: {output}")
    source_paths = [SCRIPT, PROOF, FROZEN, ERRATUM, Path(__file__).resolve(),
                    TOPIC / "results/R38-ck-local-exact-isometric-collar.md",
                    TOPIC / "results/R41-flat-annulus-conditional-local-geometry.md",
                    TOPIC / "results/R42-degenerate-flat-endpoint-and-finite-mode-uniqueness.md"]
    before = [entry(path) for path in source_paths]
    write(SOURCES, {"schema": "immutable-source-list-v1", "files": before,
                    "source_count": len(before)})
    command = [sys.executable, str(SCRIPT), "--output", str(REPLAY)]
    started = utc()
    clock = time.monotonic()
    process = subprocess.Popen(command, cwd=TOPIC.parents[1],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    elapsed = time.monotonic() - clock
    finished = utc()
    after = [entry(path) for path in source_paths]
    unchanged = before == after
    same_bytes = REPLAY.exists() and REPLAY.read_bytes() == FROZEN.read_bytes()
    observed = {
        "schema": "observed-subprocess-execution-v1",
        "command_argv": command,
        "working_directory": str(TOPIC.parents[1]),
        "pid": process.pid,
        "started_utc": started,
        "finished_utc": finished,
        "wall_seconds": elapsed,
        "returncode": process.returncode,
        "stdout": stdout,
        "stderr": stderr,
        "frozen_sources_unchanged": unchanged,
        "replay_report_byte_equal_to_frozen": same_bytes,
        "source_manifest": entry(SOURCES),
        "replay_report": entry(REPLAY) if REPLAY.exists() else None,
        "main_candidate_data_read": False,
        "mesh_count": 0,
    }
    write(OBSERVED, observed)
    assert process.returncode == 0, observed
    assert unchanged and same_bytes, observed
    files = [SCRIPT, PROOF, FROZEN, ERRATUM, Path(__file__).resolve(),
             REPLAY, SOURCES, OBSERVED]
    write(PUBLICATION, {
        "status": "AUTHOR_FROZEN_READY_FOR_ROOT_FULL_REVIEW",
        "files": [entry(path) for path in files],
        "source_binding_count": len(before),
        "actual_child_exit_zero": True,
        "immutable_source_replay_byte_equal": True,
        "exact_embedded_disk_with_boundary_constructed": True,
        "full_closed_surface_constructed": False,
        "whole_common_metric_connection_to_activity_core_constructed": False,
        "G5_of_main_candidate_completed": False,
        "typesetting_erratum": "one backslash before sin in equation (8)",
    })
    print(json.dumps({"publication": entry(PUBLICATION),
                      "observed": entry(OBSERVED), "actual_child_exit": process.returncode,
                      "source_count": len(before)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
