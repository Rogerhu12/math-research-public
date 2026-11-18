#!/usr/bin/env python3
"""Compile the reviewed production-floor variant; never load or run the result."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time


def ref(path):
    path=Path(path).resolve()
    return dict(path=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--plan',type=Path,required=True)
    a=p.parse_args();plan=json.loads(a.plan.read_text())
    if plan['schema']!='n4-native-production-floor-v1':
        raise ValueError('Unsupported reviewed build plan')
    for item in plan['files'].values():
        if ref(item['path'])!=item:
            raise ValueError('Frozen source/input changed: '+item['path'])
    if plan['files']['compiler_driver']!=ref(__file__):
        raise ValueError('This compiler driver is not the frozen plan source')
    old=Path(plan['files']['old_cpp']['path']).read_text()
    new=Path(plan['files']['production_cpp']['path']).read_text()
    before,after=plan['single_source_replacement']['before'],plan['single_source_replacement']['after']
    if old.count(before)!=1 or old.replace(before,after,1)!=new:
        raise ValueError('The owned C++ source differs beyond the one declared validation expression')
    output=Path(plan['build_record'])
    if output.exists():
        raise ValueError('Do not overwrite a recorded build')
    output.parent.mkdir(parents=True,exist_ok=True)
    records={}
    for name,command in plan['compile_commands'].items():
        binary=Path(plan['compiled_outputs'][name])
        stdout=output.parent/(name+'-compiler.stdout')
        stderr=output.parent/(name+'-compiler.stderr')
        if any(x.exists() for x in (binary,stdout,stderr)):
            raise ValueError('Do not overwrite an existing compilation artifact')
        began=time.monotonic()
        result=subprocess.run(command,capture_output=True,check=False)
        stdout.write_bytes(result.stdout);stderr.write_bytes(result.stderr)
        records[name]=dict(command=command,returncode=result.returncode,
            seconds=time.monotonic()-began,stdout=ref(stdout),stderr=ref(stderr),
            binary=ref(binary) if binary.exists() else None)
        if result.returncode:
            break
    successful=(len(records)==2 and all(r['returncode']==0 for r in records.values()))
    data=dict(scope=__doc__,plan=ref(a.plan),source=ref(__file__),command=sys.argv,
        files=plan['files'],single_source_replacement=plan['single_source_replacement'],
        compile_results=records,success=successful,
        library=records.get('library',{}).get('binary'),
        batch_executable=records.get('batch',{}).get('binary'),
        compiled_executable_invoked=False,shared_library_loaded=False,
        new_flow_or_Jacobian=False,original_source_or_library_changed=False)
    with output.open('x') as f:
        json.dump(data,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
    print(json.dumps(dict(build=ref(output),success=successful)),flush=True)
    if not successful:
        raise SystemExit(1)


if __name__=='__main__':
    main()
