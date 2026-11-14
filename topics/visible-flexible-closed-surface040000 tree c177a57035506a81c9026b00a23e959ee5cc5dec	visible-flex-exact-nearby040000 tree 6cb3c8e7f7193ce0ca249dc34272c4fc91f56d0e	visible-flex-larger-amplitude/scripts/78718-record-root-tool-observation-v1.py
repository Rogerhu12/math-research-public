#!/usr/bin/env python3
"""Record metadata supplied by an actual root terminal-tool return.

This script never starts or inspects a solver.  It cannot infer an exit from
guard files.  The root orchestration cell must supply the genuine tool result.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path


def identity(path):
    raw = path.read_bytes()
    return {"path": str(path.resolve()), "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest()}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out-prefix", type=Path, required=True)
    ap.add_argument("--phase", choices=("start", "complete", "unavailable"), required=True)
    ap.add_argument("--session-id", type=int)
    ap.add_argument("--tool-result-json", required=True)
    args = ap.parse_args()
    out = args.out_prefix.resolve()
    result = json.loads(args.tool_result_json)
    if not isinstance(result, dict):
        raise ValueError("Expected a genuine tool-result object")
    if args.phase == "complete":
        if type(result.get("exit_code")) is not int or not result.get("chunk_id"):
            raise ValueError("Natural tool exit code and receipt are required")
        if result.get("session_id") is not None:
            raise ValueError("A running tool session is not a natural completion")
        status = "observed-process-completed"
        suffix = "-root-observed-exit.json"
    elif args.phase == "start":
        if type(result.get("session_id")) is not int or result.get("exit_code") is not None:
            raise ValueError("Start observation requires an actual running tool session")
        if result["session_id"] != args.session_id or not result.get("chunk_id"):
            raise ValueError("Start session/receipt mismatch")
        status = "observed-process-started-not-completed"
        suffix = "-root-observed-start.json"
    else:
        if not isinstance(result.get("tool_error"), str) or "exit_code" in result:
            raise ValueError("Unavailable sessions must not invent an exit code")
        status = "tool-session-unavailable-no-completion-observed"
        suffix = "-root-unavailable-session.json"
    path = Path(str(out) + suffix)
    if path.exists():
        raise ValueError("Refusing to overwrite an observation")
    record = {
        "status": status, "observer": "/root", "stem": out.name,
        "session_id": args.session_id, "tool_receipt": result.get("chunk_id"),
        "actual_exit_code": result.get("exit_code"),
        "observed_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "observation_scope": "Actual root orchestration tool return; timestamp is the recording time, not exact process wall-end. Guard metadata is not used to infer an exit.",
        "tool_return_metadata": {k: v for k, v in result.items() if k != "output"},
        "recorder_source": identity(Path(__file__).resolve()),
        "files": [],
    }
    if args.phase == "complete":
        record["files"] = [identity(p) for p in sorted(out.parent.glob(out.name + "*"))
                           if p.is_file()]
    else:
        for tail in ("-launch.json", "-preparation.json", "-guard-launch.json", "-tail-config.json"):
            record["files"].append(identity(Path(str(out) + tail)))
    raw = (json.dumps(record, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode()
    if len(raw) >= 1_000_000:
        raise ValueError("Unexpectedly large observation metadata")
    with path.open("xb") as stream:
        stream.write(raw)
    print(json.dumps({"status": status, "observation": identity(path)}))


if __name__ == "__main__":
    main()
