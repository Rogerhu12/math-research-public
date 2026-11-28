#!/usr/bin/env python3
"""Run one explicit fixed-g v7 command and clean only its joined child's store.

There is no continuation, retry, parameter change or inferred acceptance.
Only an observed subprocess return permits the already reviewed owned-store
cleanup. Original fields, checkpoints, hashes and verification arrays remain.
Preparing this launcher does not start a BVP; its explicit invocation does.
"""
import argparse
import hashlib
import json
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"design"))
from mapped_factor_cleanup import cleanup_joined_child


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, value):
    temporary = path.with_name(path.name+".tmp")
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False)+"\n")
    temporary.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prepared-command", type=Path, required=True)
    parser.add_argument("--process-record", type=Path, required=True)
    parser.add_argument("--console", type=Path, required=True)
    args = parser.parse_args()
    prepared = json.loads(args.prepared_command.read_text())
    command = prepared["prepared_command_not_executed"]
    source = HERE/"fixed_support_literal_driver_v7.py"
    if (len(command) < 4 or Path(command[1]).resolve() != source.resolve()
            or prepared["source"]["sha256"] != sha(source)
            or prepared.get("nonlinear_solver_invoked") is not False
            or "--outdir" not in command or "--source-run" not in command):
        raise ValueError("An explicit unchanged independent fixed-support v7 command is required")
    for path, digest in prepared["bound_source_hashes"].items():
        if sha(path) != digest:
            raise ValueError("A bound mapped fixed-support source changed: "+path)
    recovery = prepared["updated_actual_nodal_recovery"]
    for path, digest in ((recovery["path"], recovery["sha256"]),
                         (recovery["initial_file"], recovery["initial_sha256"])):
        if sha(path) != digest:
            raise ValueError("The updated real complete nodal input changed")
    out = Path(command[command.index("--outdir")+1]).resolve()
    if out.exists() or args.process_record.exists() or args.console.exists():
        raise FileExistsError("Use a fresh output, process record and console")
    started = time.monotonic()
    record = dict(status="starting_one_original_fixed_support_mapped_process",
        command=command, prepared_command=str(args.prepared_command.resolve()),
        prepared_command_sha256=sha(args.prepared_command),
        source_sha256=sha(source), launcher_source_sha256=sha(__file__),
        source_run=command[command.index("--source-run")+1],
        updated_complete_nodal_initializer_sha256=recovery["initial_sha256"],
        map_scope="factor-only", accepted=False,
        actual_child_terminal_observed=False,
        output=str(out), console=str(args.console.resolve()))
    save(args.process_record, record)
    with args.console.open("x") as console:
        child = subprocess.Popen(command, stdout=console, stderr=subprocess.STDOUT)
        record.update(status="one_original_fixed_support_mapped_process_running", pid=child.pid)
        save(args.process_record, record)
        try:
            code = child.wait()
        except KeyboardInterrupt:
            # A manual interrupt is forwarded; cleanup still waits for a true return.
            child.send_signal(signal.SIGINT)
            code = child.wait()
    record.update(status="one_original_fixed_support_mapped_process_returned",
        actual_child_terminal_observed=True, returncode=code,
        seconds=time.monotonic()-started,
        maximum_child_rss_kib=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
        mathematical_acceptance_inferred_from_process_return=False)
    save(args.process_record, record)
    try:
        record["joined_child_mapped_storage_cleanup"] = cleanup_joined_child(
            out, code, child_return_observed=True, entry_sha256=sha(source))
    except Exception as error:
        record["joined_child_mapped_storage_cleanup_error"] = repr(error)
        record["cleanup_failure_does_not_relabel_original_child_return"] = True
    save(args.process_record, record)
    print(json.dumps(record, allow_nan=False), flush=True)
    raise SystemExit(code)


if __name__ == "__main__":
    main()
