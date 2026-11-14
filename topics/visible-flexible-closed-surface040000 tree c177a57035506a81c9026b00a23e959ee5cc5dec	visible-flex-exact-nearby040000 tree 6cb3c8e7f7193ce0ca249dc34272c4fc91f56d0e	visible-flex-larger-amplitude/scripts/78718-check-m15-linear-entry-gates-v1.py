#!/usr/bin/env python3
"""Small immutable-input and live-control-code check; no numerical port."""
import argparse
import copy
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--launch', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    i = module('m15_small_metadata_gate', HERE/'78718-prefix-m15-linear-inputs-v1.py')
    i.require(not a.out.exists(), 'Fresh output required')
    launch = json.loads(a.launch.read_text())
    context = i.validate(launch)
    i.require(a.launch.resolve() == Path(launch['launch_path']), 'Wrong declared launch path')
    actual = module('db6f_shared_client', i.CONTROL)
    record = i.check_actual_control_module(actual, launch)
    changes_rejected = []
    for name in sorted(record):
        changed = copy.deepcopy(record)
        changed[name]['typed']['canonical_code_sha256'] = '0'*64
        try:
            i.check_control_runtime_record(changed, launch)
        except ValueError:
            changes_rejected.append(name)
        else:
            raise AssertionError('Live control code alteration was accepted: '+name)
    for row in launch['bindings']:
        i.verify(row)
    report = {'schema':'78718-m15-linear-input-live-code-check-v1',
              'status':'PASS_INPUTS_AND_COMPLETE_LIVE_CONTROL_CODE_ONLY',
              'scope':__doc__, 'checker':i.identity(__file__), 'input_gate':i.identity(i.__file__),
              'launch':i.identity(a.launch), 'bindings':len(launch['bindings']),
              'live_control_functions':len(record), 'alterations_rejected':changes_rejected,
              'actual_control_code':record, 'original_canonical_kernel_functions':10,
              'candidate_initializations':0, 'port_constructors':0, 'BVP_Newton_DN_calls':0,
              'new_math_success':False}
    raw = (json.dumps(report,indent=2,allow_nan=False)+'\n').encode()
    i.require(len(raw)<1_000_000, 'Small-code report exceeds 1 MB')
    a.out.open('xb').write(raw)
    print(json.dumps({'status':report['status'], 'bindings':report['bindings'],
        'live_control_functions':len(record), 'changes_rejected':len(changes_rejected),
        'report':i.identity(a.out), 'solver_calls':0}))


if __name__ == '__main__':
    main()
