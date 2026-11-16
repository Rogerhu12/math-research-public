#!/usr/bin/env python3
"""R493 identity-bound live-worker process-group ownership, without science."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import signal
import time

SCHEMA = "R493-owned-live128-worker-session-v1"
QUIET_SCHEMA = "R493-owned-live128-worker-quiescence-v1"
RUN_KEYS = ("GITHUB_REPOSITORY", "GITHUB_RUN_ID", "GITHUB_RUN_ATTEMPT", "GITHUB_SHA")
ENV_NAMESPACE = "R493_OWNED_NAMESPACE"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=True,
                      separators=(",", ":"), allow_nan=False).encode("ascii")+b"\n"


def identity(path):
    path = Path(path).resolve(strict=True)
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1 << 20), b""):
            h.update(chunk)
    return dict(file=str(path), bytes=path.stat().st_size, sha256=h.hexdigest())


def require_actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY", "").lower() == "rogerhu12/math-research-public",
            "Process ownership applies only to this public repository Actions")


def proc_info(pid, namespace=None):
    path = Path("/proc", str(int(pid)))
    try:
        raw = (path/"stat").read_text()
        fields = raw[raw.rfind(")")+2:].split()
        info = dict(pid=int(pid), ppid=int(fields[1]), pgid=int(fields[2]), sid=int(fields[3]),
                    state=fields[0], start_ticks=int(fields[19]), uid=path.stat().st_uid)
        if namespace is not None:
            env = (path/"environ").read_bytes().split(b"\0")
            needle = (ENV_NAMESPACE+"="+str(namespace)).encode()
            info["namespace_environment_matches"] = needle in env
        return info
    except FileNotFoundError:
        return None


def register(proc, namespace, path, command, deadline):
    require_actions()
    runner = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    namespace = Path(namespace).resolve(strict=True)
    path = Path(path).resolve()
    require(namespace != runner and namespace.is_relative_to(runner) and path.is_relative_to(namespace),
            "One contained real worker session directory")
    info = proc_info(proc.pid, namespace)
    require(info is not None and info["uid"] == os.getuid()
            and info["pgid"] == info["sid"] == info["pid"]
            and info["namespace_environment_matches"] is True,
            "Actual fresh worker pid/start-time/uid/session/group/environment")
    record = dict(schema=SCHEMA, source=identity(__file__),
        run={key:os.environ.get(key) for key in RUN_KEYS}, namespace=str(namespace),
        worker=info, command=list(command), deadline=deadline,
        separate_actual_worker_session=True, original_children_inherit_this_session=True,
        numerical_work_not_accepted_by_this_record=True)
    with path.open("xb") as f:
        f.write(canonical(record))
    return record


def group_members(record):
    wanted = record["worker"]
    found, unknown = [], []
    namespace = Path(record["namespace"]).resolve(strict=True)
    for path in Path("/proc").iterdir():
        if not path.name.isdecimal():
            continue
        try:
            info = proc_info(int(path.name))
            if info is None or info["pgid"] != wanted["pgid"]:
                continue
            if info["state"] == "Z":
                # A zombie cannot execute or write. Its identity remains visible.
                info["zombie_nonwriting"] = True
                found.append(info)
                continue
            full = proc_info(info["pid"], namespace)
            if full is None:
                continue
            if full["start_ticks"] != info["start_ticks"]:
                unknown.append(dict(pid=info["pid"], reason="pid-reused-during-observation"))
                continue
            same_leader = full["pid"] == wanted["pid"] and full["start_ticks"] == wanted["start_ticks"]
            linked = (full["sid"] == wanted["sid"] and full["uid"] == wanted["uid"]
                      and full["start_ticks"] >= wanted["start_ticks"]
                      and full["namespace_environment_matches"] is True)
            if not linked or (full["pid"] == wanted["pid"] and not same_leader):
                unknown.append(dict(actual=full, reason="not-bound-to-original-owned-session"))
            else:
                found.append(full)
        except (OSError, ValueError) as error:
            # Never infer quiet from an unreadable possible same-uid member.
            # A process that genuinely vanished cannot subsequently write.
            try:
                actual_uid = path.stat().st_uid
            except FileNotFoundError:
                continue
            except OSError:
                actual_uid = None
            if actual_uid is None or actual_uid == wanted["uid"]:
                unknown.append(dict(pid=int(path.name),
                    reason="possible-owned-process-unreadable: "+type(error).__name__+": "+str(error)))
    return found, unknown


def quiet(registry, *, terminate=True):
    require_actions()
    registry = Path(registry).resolve(strict=True)
    record = json.loads(registry.read_bytes())
    require(record["schema"] == SCHEMA, "Explicit real worker-session registry")
    for key in RUN_KEYS:
        require(record["run"][key] == os.environ.get(key), "Same actual worker run identity: "+key)
    namespace = Path(record["namespace"]).resolve(strict=True)
    runner = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    require(namespace != runner and namespace.is_relative_to(runner)
            and registry.is_relative_to(namespace), "Actual owned session paths")
    result = dict(schema=QUIET_SCHEMA, source=identity(__file__), registry=identity(registry),
        run=record["run"], namespace=str(namespace), original_worker=record["worker"],
        signals=[], quiescent=False, unknown=[], observed_before=None, observed_after=None,
        native_or_fullDN_acceptance_not_inferred=True)
    before, unknown = group_members(record)
    result["observed_before"], result["unknown"] = before, unknown
    active = [row for row in before if not row.get("zombie_nonwriting")]
    if unknown:
        result["reason"] = "actual-session-ownership-could-not-be-proved-no-signal-no-cleanup"
    elif active and not terminate:
        result["reason"] = "actual-owned-worker-session-still-active"
    else:
        for sig, grace in ((signal.SIGTERM,15.0),(signal.SIGKILL,15.0)):
            current, uncertain = group_members(record)
            if uncertain:
                result["unknown"] = uncertain
                result["reason"] = "actual-ownership-changed-no-further-signal"
                break
            live = [row for row in current if not row.get("zombie_nonwriting")]
            if not live:
                break
            # Every current non-zombie member has the original unique session
            # and explicit inherited namespace. Never signal an unbound group.
            try:
                os.killpg(record["worker"]["pgid"], sig)
                result["signals"].append(dict(signal=int(sig), members=live))
            except ProcessLookupError:
                pass
            until = time.monotonic()+grace
            while time.monotonic() < until:
                rows, uncertain = group_members(record)
                if uncertain or not any(not row.get("zombie_nonwriting") for row in rows):
                    break
                time.sleep(0.1)
        after, unknown = group_members(record)
        result["observed_after"] = after
        result["unknown"] = unknown
        result["quiescent"] = not unknown and not any(not row.get("zombie_nonwriting") for row in after)
        result["reason"] = ("actual-owned-session-has-no-executing-members" if result["quiescent"]
                            else "actual-session-not-proved-quiescent")
    quiet_file = registry.with_name(registry.stem+"-quiet.json")
    # Repeated close/readback observation may replace only this metadata record.
    quiet_file.write_bytes(canonical(result))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path, required=True)
    parser.add_argument("--observe-only", action="store_true")
    args = parser.parse_args()
    result = quiet(args.registry, terminate=not args.observe_only)
    raw = canonical(result)
    if len(raw) > 90000:
        print(json.dumps(dict(schema=QUIET_SCHEMA, quiescent=result["quiescent"],
            transport_complete=False, actual_complete_bytes=len(raw),
            actual_complete_sha256=hashlib.sha256(raw).hexdigest(),
            no_raw_cleanup_authorized=True), ensure_ascii=True))
        return 70
    print(raw.decode("ascii"), end="", flush=True)
    return 0 if result["quiescent"] else 3


if __name__ == "__main__":
    raise SystemExit(main())
