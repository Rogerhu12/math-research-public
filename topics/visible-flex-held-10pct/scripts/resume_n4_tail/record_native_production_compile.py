#!/usr/bin/env python3
"""Read the completed production-floor compilation; do not load/run binaries."""
import argparse
import hashlib
import json
from pathlib import Path
import sys


def ref(path):
    p=Path(path).resolve()
    return dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest())


def load(path):
    return json.loads(Path(path).read_text())


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('plan','build','resource','log','out'):
        p.add_argument('--'+name,type=Path,required=True)
    a=p.parse_args();plan,build,resource=map(load,(a.plan,a.build,a.resource))
    if ref(a.plan)['sha256']!='6d3aa2a9deaea97a73e2a6d4a227c6f7ae0e775edbbd94c4982c748721d41a4e':
        raise ValueError('A different production-floor plan')
    if ref(a.build)['sha256']!='069165b977b12576586a94ffd60a17f24f9c292b30827bf6e874c7b0c9daa2d3':
        raise ValueError('A different real build result')
    for item in plan['files'].values():
        if ref(item['path'])!=item:
            raise ValueError('Frozen source/compiler/input changed')
    if (build['plan']!=ref(a.plan) or build['files']!=plan['files'] or not build['success'] or
            resource['status']!='observed_terminal' or resource['child_returncode']!=0 or
            resource['command']!=plan['compile_driver_command'] or
            resource['script_sha256']!=plan['files']['observer']['sha256']):
        raise ValueError('No matching real successful compile terminal')
    r=plan['single_source_replacement']
    old=Path(plan['files']['old_cpp']['path']).read_text()
    new=Path(plan['files']['production_cpp']['path']).read_text()
    if old.count(r['before'])!=1 or old.replace(r['before'],r['after'],1)!=new:
        raise ValueError('More than the declared single validation expression changed')
    results={}
    if set(build['compile_results'])!={'library','batch'}:
        raise ValueError('Both planned compiler invocations are required')
    for key,row in build['compile_results'].items():
        if row['returncode']!=0 or row['command']!=plan['compile_commands'][key]:
            raise ValueError('A compiler did not complete with the exact declared command')
        for field in ('stdout','stderr','binary'):
            if ref(row[field]['path'])!=row[field]:
                raise ValueError('A real compiler artifact changed')
        results[key]={**row,'stdout_bytes':Path(row['stdout']['path']).stat().st_size,
                      'stderr_bytes':Path(row['stderr']['path']).stat().st_size}
    events=[json.loads(line) for line in a.log.read_text().splitlines() if line.strip()]
    if events!=[dict(build=ref(a.build),success=True)]:
        raise ValueError('The original compiler-driver log differs from its build record')
    output=dict(scope=__doc__,source=ref(__file__),command=sys.argv,plan=ref(a.plan),
        build=ref(a.build),resource=ref(a.resource),log=ref(a.log),files=plan['files'],
        single_source_replacement=r,compile_results=results,
        execution=dict(observer_session=83860,child_returncode=resource['child_returncode'],
            observed_utc=resource['observed_utc'],observer_seconds=resource['seconds']),
        production_floor=.05,retained_capsule_floor=.1,
        original_source_and_binaries_unchanged=True,
        compiled_executable_invoked=False,shared_library_loaded=False,
        new_flow_root_or_Jacobian=False,new_whole_tail_or_DN_acceptance=False,
        pending='The separately frozen two-floor/three-stage batch identity execution has not run. Production Node hook and original DN/audit are separate later steps.')
    with a.out.open('x') as stream:
        json.dump(output,stream,ensure_ascii=False,indent=2,allow_nan=False);stream.write('\n')
    print(json.dumps(dict(record=ref(a.out),compiler_returncodes={k:v['returncode'] for k,v in results.items()})),flush=True)


if __name__=='__main__':
    main()
