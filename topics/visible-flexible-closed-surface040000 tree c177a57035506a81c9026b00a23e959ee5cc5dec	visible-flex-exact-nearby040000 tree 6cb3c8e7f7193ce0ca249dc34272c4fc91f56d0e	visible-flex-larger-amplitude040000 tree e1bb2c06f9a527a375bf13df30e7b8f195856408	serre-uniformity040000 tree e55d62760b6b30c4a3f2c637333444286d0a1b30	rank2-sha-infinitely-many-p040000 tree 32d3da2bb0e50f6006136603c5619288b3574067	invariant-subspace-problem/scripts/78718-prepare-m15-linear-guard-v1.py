#!/usr/bin/env python3
"""Resource metadata only for the frozen M15 linear-DN launch; never starts it."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--launch', type=Path, required=True)
    args = ap.parse_args()
    spec = importlib.util.spec_from_file_location('restart8000_guard_metadata_driver',
                                                HERE/'78718-prefix-spectral-m15-linear-v1.py')
    c = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(c)
    launch = c.read(args.launch)
    context = c.validate_inputs(launch)
    c.require(args.launch.resolve() == Path(launch['launch_path']), 'Wrong frozen launch file')
    out = context['out']
    path = Path(str(out)+'-guard-launch.json')
    wrapper = HERE/'78718-run-m14-csc-resource-6g.py'
    guard = HERE/'db6f-root-run-space-guarded.py'
    c.require(c.identity(wrapper)['sha256'] == '8260d9e9ac76f4816b5c40aafd3c07ec841388ea9b88316556e56f60c85a0ccc',
              'Resource wrapper must retain its reviewed byte identity')
    c.require(c.identity(guard)['sha256'] == 'cf1e2364300015c841b2070be51e948dc7ba37ef5b98eef0441819bca1e6aabd',
              'Original disk guard changed')
    rows = {row['path']: row for row in launch['bindings']}
    for source in (args.launch, Path(str(out)+'-preparation.json'), wrapper, guard, Path(__file__)):
        row = c.identity(source)
        rows[row['path']] = row
    command = [sys.executable, str(wrapper), '--launch', str(path),
               '--observation', str(out)+'-guard-completion.json',
               '--backup-observation', str(out)+'-guard-live.json']
    value = {'schema':'78718-m15-linear-resource-bound-command-v1',
             'status':'PREPARED_NOT_STARTED', 'cwd':launch['cwd'], 'out_prefix':str(out),
             'command':launch['command'], 'bound_files':sorted(rows.values(),key=lambda row:row['path']),
             'resource_policy':{'RLIMIT_DATA_bytes_per_process':6*1024**3,
                 'Node_heap_MiB':1536,'disk_minimum_free_bytes':512*1024**2,
                 'disk_resume_free_bytes':768*1024**2},
             'root_start_command':command, 'solver_started':False,
             'scope':'Resource/storage supervision only. Same frozen mathematical argv, no convergence or aggregate-memory guarantee.'}
    c.write_json(path,value,exclusive=True)
    print(json.dumps({'status':value['status'],'guard_launch':c.identity(path),
                      'bound_files':len(rows),'solver_calls':0,'root_start_command':command},indent=2))


if __name__=='__main__':
    main()
