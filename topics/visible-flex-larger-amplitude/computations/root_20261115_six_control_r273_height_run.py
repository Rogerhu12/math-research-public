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


ENTRY = 'geometry_20261115_six_control_r273_height_full112.py'
ENTRY_SHA = 'd1f21025a91234252c856cb15bf26ce48e2628e8fa92352a9d98ffd53b14a69d'
CLIENT = 'geometry_20261115_original_r273_tail_client.py'
CLIENT_SHA = '2fe2c25233061de0fd89b7af72cba5ddd2e2d144889492ec42156f781c4828a9'


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


def stop_group(child):
    if child.poll() is not None:
        return
    try:
        os.killpg(child.pid, signal.SIGTERM)
    except ProcessLookupError:
        pass
    try:
        child.wait(timeout=8)
    except subprocess.TimeoutExpired:
        try:
            os.killpg(child.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        child.wait()


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
    if request.get('schema') != 'public-six-control-r273-height-request-v1':
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
    record = dict(schema='six-control-r273-height-full112-process-wrapper-v1', phase='starting',
        source_commit=os.environ.get('GITHUB_SHA'), run_id=os.environ.get('GITHUB_RUN_ID'),
        wrapper_sha256=digest(__file__), request_sha256=digest(args.request),
        parameter_recipe_sha256=digest(args.recipe), adapter_sha256=ENTRY_SHA,
        native_client_sha256=CLIENT_SHA, command=argv, scientific_wall_clock_seconds=budget,
        original_scientific_iterations_and_thresholds_unchanged=True,
        prepare_only_requested=False, scientific_completion_claimed=False,
        success_claimed_by_wrapper=False, budget_exhausted=False, external_signal=None)
    status = output/'process-status.json'
    write(status, record)
    print(json.dumps(dict(event='request145_height_path_full112_launch', **record),
                     ensure_ascii=True, allow_nan=False), flush=True)
    child = None
    started = time.monotonic()
    child_env = dict(os.environ)
    child_env['VISIBLE_HEIGHT_PATH_DEADLINE_MONOTONIC'] = repr(started+budget)
    child_env['VISIBLE_R273_HEIGHT_PATH_ETA'] = request['r273']['eta_cli_text']
    child_env['VISIBLE_R273_HEIGHT_PATH_EXACT_WORKERS'] = str(request['r273']['exact_workers'])
    child_env['VISIBLE_R273_HEIGHT_PATH_FACTOR_BYTES'] = str(request['r273']['maximum_factor_bytes'])
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
            record.update(phase='running', child_pid=child.pid)
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
            thread.join(timeout=2)
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
        if child is not None and child.poll() is None:
            stop_group(child)
        for number, handler in old_handlers.items():
            signal.signal(number, handler)
        record.update(elapsed_seconds=time.monotonic()-started, wrapper_returncode=code,
                      stdout_copy_errors=stream_errors, scientific_output_only_in_RUNNER_TEMP=True)
        log = output/'science-stdout-stderr.log'
        if log.is_file():
            record['scientific_log'] = dict(bytes=log.stat().st_size, sha256=digest(log))
        write(status, record)
        print(json.dumps(dict(event='request145_height_path_full112_process_returned',
            phase=record['phase'], returncode=code, budget_exhausted=record['budget_exhausted'],
            external_signal=record['external_signal'], process_status_sha256=digest(status),
            scientific_acceptance_not_inferred_from_process_status=True), allow_nan=False), flush=True)
    return code


if __name__ == '__main__':
    raise SystemExit(main())
