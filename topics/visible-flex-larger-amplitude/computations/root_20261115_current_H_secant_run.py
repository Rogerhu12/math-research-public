#!/usr/bin/env python3
"""Run the independent H(s) complete112 adapter once, with one total wall budget.

This standard-library process wrapper does not import scientific modules or
change a numerical parameter. The source recipe, original tail configuration,
all native iterations and full-DN gates belong to the frozen adapter. A budget
or external interruption is reported as partial, never as a numerical result.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import threading
import time
import traceback


ENTRY = 'geometry_20261115_six_control_current_H_secant_full112.py'
ENTRY_SHA = '7a6b9d0784e358b2f38bfbcdaddeabf32701f36b66b34769f7d51543bff0b5f1'
CLIENT = 'geometry_20261115_current_H_secant_tail_client.py'
CLIENT_SHA = 'd76785f533de468b4b7eebbad160120fdc85be2138b4281388fc1f81269d2ad8'


def digest(path):
    value = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            value.update(block)
    return value.hexdigest()


def write(path, value):
    raw = (json.dumps(value, ensure_ascii=True, allow_nan=False,
                      separators=(',', ':'))+'\n').encode()
    temporary = path.with_suffix(path.suffix+'.partial')
    temporary.write_bytes(raw)
    temporary.replace(path)


def proc_record(pid):
    try:
        raw=(Path("/proc")/str(pid)/"stat").read_text()
        right=raw.rfind(")")
        values=raw[right+2:].split()
        return dict(pid=int(raw[:raw.find(" ")]),state=values[0],
            ppid=int(values[1]),pgid=int(values[2]),sid=int(values[3]),
            start_ticks=int(values[19]))
    except (FileNotFoundError,ProcessLookupError):
        return None


def group_scope(pgid):
    members=[];errors=[]
    for path in Path("/proc").iterdir():
        if not path.name.isdigit():continue
        try:
            value=proc_record(int(path.name))
            if value is not None and value["pgid"]==pgid:
                members.append(value)
        except Exception as error:
            errors.append(dict(pid=path.name,error=repr(error)))
    live=[value for value in members if value["state"]!="Z"]
    return dict(exclusive_group=pgid,members=sorted(members,key=lambda x:x["pid"]),
        live_members=sorted(live,key=lambda x:x["pid"]),read_errors=errors,
        quiescent=not live and not errors,
        shared_parent_group_not_treated_as_science=True)


def stop_group(child):
    """Own only the new session actually created by this wrapper's Popen."""
    pgid=child.pid
    scope=group_scope(pgid)
    if any(value["sid"]!=pgid for value in scope["members"]):
        return dict(**scope,stop_refused_due_to_unexpected_session=True)
    if scope["live_members"]:
        try:os.killpg(pgid,signal.SIGTERM)
        except ProcessLookupError:pass
        until=time.monotonic()+8
        while time.monotonic()<until:
            scope=group_scope(pgid)
            if not scope["live_members"]:break
            try:child.wait(timeout=.2)
            except subprocess.TimeoutExpired:pass
            time.sleep(.05)
    scope=group_scope(pgid)
    if scope["live_members"]:
        if any(value["sid"]!=pgid for value in scope["members"]):
            return dict(**scope,stop_refused_due_to_unexpected_session=True)
        try:os.killpg(pgid,signal.SIGKILL)
        except ProcessLookupError:pass
        until=time.monotonic()+8
        while time.monotonic()<until:
            scope=group_scope(pgid)
            if not scope["live_members"]:break
            try:child.wait(timeout=.2)
            except subprocess.TimeoutExpired:pass
            time.sleep(.05)
    try:child.wait(timeout=1)
    except subprocess.TimeoutExpired:pass
    return group_scope(pgid)

def main():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific child execution belongs only to the public repository Actions')
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('request', 'recipe', 'inputs-directory', 'source-topic', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    args = parser.parse_args()
    request = json.loads(args.request.read_bytes())
    comp = Path(__file__).resolve().parent
    if request.get('schema') != 'public-six-control-current-H-secant-request-v1':
        raise ValueError('Use the explicit complete112 request schema')
    if digest(comp/ENTRY) != ENTRY_SHA or digest(comp/CLIENT) != CLIENT_SHA:
        raise ValueError('The frozen full-DN adapter or original true native client differs')
    if digest(args.recipe) != request['parameter_recipe']['sha256']:
        raise ValueError('Use the actual explicit parameter/positive-lambda recipe bytes')
    root = Path(os.environ['RUNNER_TEMP']).resolve()
    output = args.out.resolve()
    if not output.is_relative_to(root) or output == root or output.is_symlink():
        raise ValueError('Only this request-owned RUNNER_TEMP output may be used')
    output.mkdir(parents=True, exist_ok=False)
    settings = request['execution']
    argv = [sys.executable, '-u', str(comp/ENTRY),
        '--recipe', str(args.recipe.resolve()),
        '--expected-recipe-sha256', request['parameter_recipe']['sha256']]
    for name in ('accepted', 'prepared', 'tail_anchor', 'tail_config'):
        item = request['inputs'][name]
        if Path(item['runtime_basename']).name != item['runtime_basename']:
            raise ValueError('A mathematical input must use one explicit temporary basename')
        file = args.inputs_directory/item['runtime_basename']
        if file.stat().st_size != item['bytes'] or digest(file) != item['sha256']:
            raise ValueError('Restored complete mathematical input differs: '+name)
        argv += ['--'+name.replace('_', '-'), str(file.resolve())]
    argv += ['--tail-client', str(comp/CLIENT), '--expected-tail-client-sha256', CLIENT_SHA,
        '--tail-source-root', str(args.source_topic.resolve()/'repro/source-root'),
        '--out', str(output/'science'), '--work', str(output/'factors')]
    for name in ('jac_workers', 'max_nodes', 'material_angles', 'physical_angles',
                 'node_heap', 'outer_iterations'):
        argv += ['--'+name.replace('_', '-'), str(settings[name])]
    budget = settings['scientific_wall_clock_seconds']
    if not isinstance(budget, int) or budget <= 0:
        raise ValueError('An explicit positive wall-clock budget is required')
    for key in ('VISIBLE_FLEX_FROZEN_LEDGER_READY', 'VISIBLE_FLEX_FROZEN_STORED_READY'):
        if not os.environ.get(key) or not Path(os.environ[key]).is_file():
            raise ValueError('Restore the original existing native geometry slot: '+key)
    record = dict(schema='six-control-current-H-secant-full112-process-wrapper-v1', phase='starting',
        source_commit=os.environ.get('GITHUB_SHA'), run_id=os.environ.get('GITHUB_RUN_ID'),
        wrapper_sha256=digest(__file__), request_sha256=digest(args.request),
        parameter_recipe_sha256=digest(args.recipe), adapter_sha256=ENTRY_SHA,
        native_client_sha256=CLIENT_SHA, command=argv, scientific_wall_clock_seconds=budget,
        original_scientific_iterations_and_thresholds_unchanged=True,
        prepare_only_requested=False, scientific_completion_claimed=False,
        success_claimed_by_wrapper=False, budget_exhausted=False, external_signal=None,
        additional_R360_noJ_calls_are_new_science=True,
        original_mathematical_acceptance_and_iteration_counts_unchanged=True,
        diagnostic_io_or_arithmetic_failure_is_not_original_native_rejection=True,
        owned_group_quiescent_after_return=False,
        diagnostic_policy=request["secant_diagnostic"])
    status = output/'process-status.json'
    write(status, record)
    print(json.dumps(dict(event='request172_height_path_full112_launch', **record),
                     ensure_ascii=True, allow_nan=False), flush=True)
    child = None
    started = time.monotonic()
    child_env = dict(os.environ)
    child_env['VISIBLE_HEIGHT_PATH_DEADLINE_MONOTONIC'] = repr(started+budget)
    child_env['VISIBLE_R273_HEIGHT_PATH_ETA'] = request['r273']['eta_cli_text']
    child_env['VISIBLE_R273_HEIGHT_PATH_EXACT_WORKERS'] = str(request['r273']['exact_workers'])
    child_env['VISIBLE_R273_HEIGHT_PATH_FACTOR_BYTES'] = str(request['r273']['maximum_factor_bytes'])
    diagnostic=request["secant_diagnostic"]
    if (diagnostic.get("schema")!="explicit-current-H-R360-diagnostic-policy-v1"
            or diagnostic.get("extra_alpha_exponents")!=[10,11,12]
            or diagnostic.get("extra_calls_eligible_for_original_acceptance") is not False):
        raise ValueError("Use the explicit independent diagnostic scope")
    seconds=diagnostic.get("per_loop_exact_budget_seconds")
    if type(seconds) not in (int,float) or not 0<seconds<=budget:
        raise ValueError("Explicit diagnostic per-loop resource budget required")
    child_env["VISIBLE_CURRENT_H_SECANT_EXACT_SECONDS"]=str(seconds)
    received = []
    old_handlers = {}
    stream_errors = []
    thread = None

    def interrupted(number, unused_frame):
        received.append(number)

    def copy_output(pipe, logfile):
        try:
            while True:
                block = pipe.read(65536)
                if not block:
                    return
                logfile.write(block)
                logfile.flush()
                sys.stdout.buffer.write(block)
                sys.stdout.buffer.flush()
        except Exception as error:
            stream_errors.append(repr(error))

    code = 70
    try:
        for number in (signal.SIGTERM, signal.SIGINT):
            old_handlers[number] = signal.signal(number, interrupted)
        # A separate group makes the native Node descendants part of this
        # explicit stop responsibility. The wrapper forwards rule-runner TERM.
        with (output/'science-stdout-stderr.log').open('xb') as logfile:
            child = subprocess.Popen(argv, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                     start_new_session=True, bufsize=0, env=child_env)
            thread = threading.Thread(target=copy_output, args=(child.stdout, logfile), daemon=True)
            thread.start()
            record.update(phase='running', child_pid=child.pid,
                child_start=proc_record(child.pid),
                owned_child_pgid=child.pid,exclusive_group_created_by_start_new_session=True,
                parent_process=proc_record(os.getpid()))
            write(status, record)
            while child.poll() is None:
                if received:
                    record.update(external_signal=received[-1], phase='external-interruption-partial')
                    stop_group(child)
                    break
                if time.monotonic()-started >= budget:
                    record.update(budget_exhausted=True, phase='wall-clock-budget-partial')
                    stop_group(child)
                    break
                try:
                    child.wait(timeout=1)
                except subprocess.TimeoutExpired:
                    pass
            # The original driver has returned or was stopped. Quiesce any
            # remaining owned descendants before reading final streams.
            record["owned_group_after_child_return"]=stop_group(child)
            record["owned_group_quiescent_after_return"]=record["owned_group_after_child_return"]["quiescent"]
            thread.join(timeout=5)
            if thread.is_alive():
                stream_errors.append('Scientific stdout reader did not finish after child exit')
            code = child.returncode
            record['scientific_child_returncode'] = code
            if received:
                code = 128+received[-1]
            elif record['budget_exhausted']:
                code = 124
            else:
                record['phase'] = 'original-adapter-returned'
            if code is not None and code < 0:
                code = 128-code
            if code is None:
                code = 70
    except Exception as error:
        record.update(phase='process-wrapper-exception', exception=repr(error),
                      traceback=traceback.format_exc())
        if child is not None:
            stop_group(child)
        raise
    finally:
        if child is not None:
            record["owned_group_after_finally"]=stop_group(child)
            record["owned_group_quiescent_after_return"]=record["owned_group_after_finally"]["quiescent"]
        for number, handler in old_handlers.items():
            signal.signal(number, handler)
        if not record["owned_group_quiescent_after_return"] or stream_errors:
            record["engineering_readback_incomplete"]=True
            if code==0:code=70
        record.update(elapsed_seconds=time.monotonic()-started, wrapper_returncode=code,
                      stdout_copy_errors=stream_errors, scientific_output_only_in_RUNNER_TEMP=True)
        log = output/'science-stdout-stderr.log'
        if log.is_file():
            record['scientific_log'] = dict(bytes=log.stat().st_size, sha256=digest(log))
        write(status, record)
        print(json.dumps(dict(event='request172_height_path_full112_process_returned',
            phase=record['phase'], returncode=code, budget_exhausted=record['budget_exhausted'],
            external_signal=record['external_signal'], process_status_sha256=digest(status),
            scientific_acceptance_not_inferred_from_process_status=True), allow_nan=False), flush=True)
    return code


if __name__ == '__main__':
    raise SystemExit(main())
