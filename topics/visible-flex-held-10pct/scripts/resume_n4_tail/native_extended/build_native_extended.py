#!/usr/bin/env python3
"""Compile the one native kernel twice; never execute or import a flow probe."""
import argparse
import ast
from concurrent.futures import ThreadPoolExecutor
import datetime
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import time


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ident(path):
    return dict(path=str(Path(path).resolve()),sha256=sha(path))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--build-dir',type=Path,required=True)
    p.add_argument('--compiler',default='g++')
    a=p.parse_args()
    root=Path(__file__).resolve().parent
    source_paths=dict(cpp=root/'frozen_flow.cpp',header=root/'frozen_flow.h',
        harness=root/'probe_native_frozen_flow.py',builder=Path(__file__).resolve())
    sources={name:ident(path)for name,path in source_paths.items()}
    for name in ('harness','builder'):
        ast.parse(source_paths[name].read_text())
    if a.build_dir.exists():
        raise ValueError('An owned compile directory must be new; preserve prior build evidence')
    a.build_dir.mkdir(parents=True)
    compiler=Path(shutil.which(a.compiler)or a.compiler).resolve()
    version=subprocess.run([str(compiler),'--version'],text=True,capture_output=True,check=True)
    flags=['-std=c++17','-O2','-fno-fast-math','-ffp-contract=off','-fexcess-precision=standard','-frounding-math']
    library=a.build_dir.resolve()/'libfrozen_flow.so'
    executable=a.build_dir.resolve()/'frozen_flow_batch'
    commands={
        'library':[str(compiler),*flags,'-fPIC','-shared',str(source_paths['cpp']),'-o',str(library),'-lm'],
        'batch':[str(compiler),*flags,'-DVF_BUILD_MAIN',str(source_paths['cpp']),'-o',str(executable),'-lm']}
    def compile_one(item):
        name,command=item;start=time.monotonic()
        process=subprocess.run(command,text=True,capture_output=True,check=False)
        stdout=a.build_dir/(name+'-compiler.stdout');stderr=a.build_dir/(name+'-compiler.stderr')
        stdout.write_text(process.stdout);stderr.write_text(process.stderr)
        return name,dict(command=command,returncode=process.returncode,seconds=time.monotonic()-start,
            stdout=ident(stdout),stderr=ident(stderr))
    with ThreadPoolExecutor(max_workers=2)as pool:
        runs=dict(pool.map(compile_one,commands.items()))
    if any(sha(path)!=sources[name]['sha256']for name,path in source_paths.items()):
        raise ValueError('A source changed during compilation')
    output=dict(scope=__doc__,created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        command=sys.argv,sources=sources,compiler=ident(compiler),compiler_version=version.stdout,
        flags=flags,compile_results=runs,harness_AST_syntax_only=True,
        mathematical_executable_invoked=False,shared_library_loaded=False,
        no_new_flow_or_Jacobian=True,original_sources_modified=False)
    if all(run['returncode']==0for run in runs.values()):
        output.update(library=ident(library),batch_executable=ident(executable),status='compile_success_no_execution')
    else:
        output['status']='compile_failure_no_execution'
    out=a.build_dir/'build.json';out.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(record=ident(out),status=output['status'],sources=sources),ensure_ascii=False),flush=True)
    if output['status']!='compile_success_no_execution':
        for name,result in runs.items():
            if result['returncode']:print(Path(result['stderr']['path']).read_text(),file=sys.stderr)
        raise SystemExit(1)


if __name__=='__main__':main()
