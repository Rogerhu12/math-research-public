#!/usr/bin/env python3
"""Continue the original q recovery from a genuine accepted checkpoint.

No earlier q is recomputed.  The old recovery body is retained except for
binding its already-generated ports and entering its original q loop after
the supplied accepted q.  Subsequent original lift/positive-lambda/bootstrap
stages remain intact; the complete-lift secant and isolated v3 resource
wrappers execute with separate actual-command/source provenance.
"""
import argparse
import hashlib
import importlib.util
import inspect
import json
from pathlib import Path
import subprocess
import sys
import time


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'work', 'source-run', 'outdir'):
        parser.add_argument('--' + name, type=Path, required=True)
    parser.add_argument('--wait-for-source', action='store_true')
    args = parser.parse_args()
    repo, work, source, out = (p.resolve() for p in
                              (args.repo, args.work, args.source_run, args.outdir))
    if repo == work or repo in work.parents or work not in out.parents or work not in source.parents:
        raise ValueError('Actual and generated fields must stay under work outside Git')
    scripts = repo / 'topics/visible-flex-held-10pct/scripts'
    sys.path[:0] = [str(scripts / 'resume_m3'), str(scripts / 'resume_20261126')]
    from material_design_continue import original_finite_checks, complete_initializer
    from continue_material_true_tail import prefix_gate
    while True:
        try:
            record = json.loads(source.read_text())
        except (FileNotFoundError, json.JSONDecodeError):
            record = {}
        if 'seconds' in record:
            break
        if not args.wait_for_source:
            raise ValueError('The requested source has not actually returned')
        time.sleep(5)
    if (not prefix_gate(record) or
            not original_finite_checks(record)['solver_and_boundary_pass'] or
            not complete_initializer(source, record)):
        raise ValueError('The actual source did not pass every original prefix gate')
    if record.get('core_settings') is not None or record.get('actual_tail_requested'):
        raise ValueError('Only the recorded original support-family q recovery is resumed')
    checkpoint = source.parent / 'checkpoint.json.gz'
    if not checkpoint.is_file() or sha(checkpoint) != record.get('checkpoint_sha256'):
        raise ValueError('The actual complete q checkpoint is missing or has changed')
    for group in ('source_hashes', 'inputs'):
        for name, expected in record[group].items():
            if sha(name) != expected:
                raise ValueError('An actual source/input changed: ' + name)
    q = record['gauge_q']
    chain = [('006', '.006'), ('012', '.012'), ('020', '.02'), ('030', '.03'),
             ('040', '.04'), ('050', '.05'), ('060', '.06')]
    if q not in [float(value) for _, value in chain] or record['modes'] != 8:
        raise ValueError('The source is not an original M8 q-chain stage')
    remaining = [(label, value) for label, value in chain if float(value) > q]
    # A real accepted source may live in a later continuation directory.
    # Bind the existing exporter outputs through its actual --port argument,
    # not through an assumed position of its output directory.
    source_command = record['command']
    if source_command.count('--port') != 1:
        raise ValueError('The actual source must bind exactly one original port')
    old_out = Path(source_command[source_command.index('--port') + 1]).resolve().parent
    ports = {24: work / 'm24-linear-port.json'}
    port24 = json.loads(ports[24].read_text())
    for modes in (8, 16):
        port = old_out / ('m' + str(modes) + '-linear-port.json')
        settings = old_out / ('m' + str(modes) + '-tail-settings.json')
        value = json.loads(port.read_text())
        if (value['parameters'] != port24['parameters'] or value['cut'] != port24['cut'] or
                value['modes'] != [3*(j+1) for j in range(modes)] or
                value['source']['config_sha256'] != sha(settings)):
            raise ValueError('The existing mode port changed its complete physical binding')
        ports[modes] = port

    original_path = scripts / 'resume_20261126/lowq_prefix_recovery_secant_design.py'
    original = load('_resumed_original_q_body_20261128', original_path)
    before = inspect.getsource(original.main)
    begin = before.index('        ports = {24:')
    end = before.index("        common = ['--source-topic'", begin)
    after = before[:begin] + '        ports = dict(_actual_existing_ports)\n\n' + before[end:]
    marker = "        previous = None\n        for label, q in (('006', '.006'), ('012', '.012'), ('020', '.02'),\n                         ('030', '.03'), ('040', '.04'), ('050', '.05'), ('060', '.06')):"
    if after.count(marker) != 1:
        raise ValueError('The original q-chain entry changed')
    after = after.replace(marker,
        "        previous = _actual_resume_run\n"
        "        raw = _actual_resume_raw\n"
        "        state['resumed_actual_source'] = _actual_resume_identity\n"
        "        save()\n"
        "        for label, q in _actual_remaining_q:")
    raw = source.parent / record['raw_return']['file']
    identity = dict(source_run=str(source), source_run_sha256=sha(source),
                    checkpoint_sha256=sha(checkpoint), raw_sha256=sha(raw),
                    accepted_q=q, earlier_q_recomputed=False,
                    old_stage_parameters_preserved=True)
    original.__dict__.update(_actual_existing_ports=ports,
        _actual_resume_run=source, _actual_resume_raw=raw,
        _actual_resume_identity=identity, _actual_remaining_q=remaining)
    exec(compile(after, str(Path(__file__).resolve()) + '::resumed_original_body', 'exec'),
         original.__dict__)
    here = Path(__file__).resolve().parent
    resource = here / 'prefix_resource_driver_v3.py'
    controller = here / 'run_lifted_secant_v2.py'
    bootstrap_wrapper = here / 'run_bootstrap_design_v2.py'
    portable = scripts / 'resume_m3/portable_prefix_continue.py'
    secant = scripts / 'resume_20261126/material_design_secant_continue.py'
    bootstrap = scripts / 'resume_20261126/material_design_continue.py'
    metadata = out.with_name(out.name + '-execution.jsonl')
    files = (Path(__file__).resolve(), original_path, resource, controller,
             bootstrap_wrapper, here/'prefix_resource_driver_v2.py',
             here/'prefix_resource_driver.py', here/'cached_fourier_tables.py')
    with metadata.open('x') as stream:
        stream.write(json.dumps(dict(event='resumed_execution_begin',
            original_main_sha256=hashlib.sha256(before.encode()).hexdigest(),
            executed_main_sha256=hashlib.sha256(after.encode()).hexdigest(),
            source_hashes={str(p): sha(p) for p in files}, source=identity,
            remaining_q=remaining, existing_port_sha256={str(m):sha(p) for m,p in ports.items()},
            original_equations_changed=False, original_acceptance_gates_changed=False)) + '\n')
    old_popen = subprocess.Popen

    def execute(command, *positional, **keywords):
        actual = list(map(str, command))
        requested = list(actual)
        if '--driver' in actual and actual[actual.index('--driver') + 1] == str(portable):
            actual[actual.index('--driver') + 1] = str(resource)
        if len(actual) > 1 and actual[1] == str(secant):
            actual[1] = str(controller)
        if len(actual) > 1 and actual[1] == str(bootstrap):
            actual[1] = str(bootstrap_wrapper)
        executed_sources = {str(Path(path).resolve()): sha(path) for path in actual
                            if path.endswith('.py') and Path(path).is_file()}
        with metadata.open('a') as stream:
            stream.write(json.dumps(dict(event='subprocess', requested=requested,
                executed=actual, executed_source_sha256=executed_sources)) + '\n')
        return old_popen(actual, *positional, **keywords)

    subprocess.Popen = execute
    sys.argv = [str(original_path), '--repo', str(repo), '--work', str(work), '--outdir', str(out)]
    return original.main()


if __name__ == '__main__':
    sys.exit(main())
