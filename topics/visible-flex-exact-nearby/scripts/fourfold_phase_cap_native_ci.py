#!/usr/bin/env python3
"""Portable disjoint FE worker for the frozen true native cap-energy kernel.

This wrapper does not change any mathematical quadrature or acceptance gate.
It verifies the complete frozen local source/data closure, then invokes the
original producer. Complete original FE reports retain its exact identity.
Incomplete pre-existing reports are preserved before an original-kernel rerun.
"""
from __future__ import annotations

import argparse
import ast
from fractions import Fraction
import gzip
import hashlib
import importlib
import importlib.metadata
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    path=Path(path)
    return json.load(gzip.open(path,'rt')) if path.suffix=='.gz' else json.loads(path.read_text())


def save(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_suffix(path.suffix+'.tmp')
    temporary.write_text(json.dumps(value,indent=2)+'\n')
    temporary.replace(path)


def safe_relative(value):
    path=Path(value)
    if path.is_absolute() or '..' in path.parts:
        raise ValueError('worker inputs and outputs must use portable topic-relative paths')
    return path


def local_imports(path):
    result=set()
    for node in ast.walk(ast.parse(path.read_text())):
        names=([node.module] if isinstance(node,ast.ImportFrom) and node.module
               else [alias.name for alias in node.names] if isinstance(node,ast.Import) else [])
        for name in names:
            file=Path('scripts')/(name.split('.')[0]+'.py')
            if file.exists():result.add(str(file))
    return result


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--input-manifest',type=Path,default=Path('notes/2026-11-12-cap-native-ci-inputs.json'))
    ap.add_argument('--manifest-sha256',required=True)
    ap.add_argument('--first-element',type=int,required=True)
    ap.add_argument('--last-element',type=int,required=True,help='exclusive upper FE index')
    ap.add_argument('--out-dir',type=Path,required=True)
    ap.add_argument('--check-only',action='store_true')
    args=ap.parse_args()
    topic=Path(__file__).resolve().parents[1];os.chdir(topic)
    args.out_dir=safe_relative(args.out_dir)
    if sha(args.input_manifest)!=args.manifest_sha256:
        raise ValueError('the exact CI input manifest SHA differs')
    inputs=read(args.input_manifest)
    if inputs.get('kind')!='frozen_true_native_cap_CI_input_closure':
        raise ValueError('unsupported native-cap CI input manifest')
    listed={item['path']:item for item in inputs['files']}
    if len(listed)!=len(inputs['files']):raise ValueError('duplicate frozen input paths')
    for name,item in listed.items():
        path=safe_relative(name)
        if not path.is_file() or path.stat().st_size!=item['bytes'] or sha(path)!=item['sha256']:
            raise ValueError('a frozen source or actual mathematical input differs: '+name)
    source_names=set(inputs['source_closure'])
    if any(name not in listed for name in source_names):
        raise ValueError('the source closure is absent from the verified manifest')
    for name in source_names:
        missing=local_imports(Path(name))-source_names
        if missing:raise ValueError('a local Python dependency is not in the frozen closure: '+str(sorted(missing)))
    worker='scripts/'+Path(__file__).name
    if worker not in listed or sha(__file__)!=listed[worker]['sha256']:
        raise ValueError('the executed worker differs from its frozen input closure')
    lower,upper=inputs['allowed_element_range']
    if not lower<=args.first_element<args.last_element<=upper:
        raise ValueError('requested FE range is outside the exact remaining inner-body allocation')
    native=inputs['native_arguments']
    trial=read(native['trial'])
    if (trial['object_sha256']!=inputs['object_sha256']
        or trial['exact_delta_fraction']!=inputs['exact_delta_fraction']
        or sha(trial['arrays']['path'])!=trial['arrays']['sha256']):
        raise ValueError('native CI trial/object identity differs')
    import numpy as np
    with np.load(trial['arrays']['path'],allow_pickle=False) as array:
        mesh=array['mesh'].copy()
    a,b=map(lambda i:Fraction(float(mesh[i])),(args.first_element,args.last_element))
    if not Fraction(1,4)<=a<b<=3:
        raise ValueError('the requested native FE range is not in the actual body')
    kernel=safe_relative(inputs['kernel'])
    if kernel.name!='fourfold_phase_cap_native_cover_v2.py':
        raise ValueError('this worker invokes only the frozen paid native-v2 producer')
    sys.path.insert(0,str(topic/'scripts'))
    # An import check catches missing pinned runtime libraries before any job
    # is called complete. The mathematical entry remains the original CLI.
    importlib.import_module(kernel.stem)
    runtime={'python':sys.version}
    for package in ('numpy','scipy','python-flint'):
        runtime[package]=importlib.metadata.version(package)
    command=[sys.executable,'-u',str(kernel),
        '--start-element',str(args.first_element),'--stop-element',str(args.last_element),
        '--trial',native['trial'],'--seed',native['seed'],
        '--reuse-partial',native['reuse_partial'],'--out-dir',str(args.out_dir)]
    for key in ('bits','primitive_nodes','angles','normalized_strip',
                'minimum_analytic_radius','max_gauss_order','max_depth','error_per_length'):
        command.extend(('--'+key.replace('_','-'),str(native[key])))
    identity=dict(worker_sha256=sha(__file__),input_manifest=str(args.input_manifest),
        input_manifest_sha256=args.manifest_sha256,kernel=str(kernel),kernel_sha256=sha(kernel),
        source_closure_sha256={name:listed[name]['sha256'] for name in sorted(source_names)},
        complete_input_sha256={name:item['sha256'] for name,item in sorted(listed.items())},
        exact_delta_fraction=inputs['exact_delta_fraction'],object_sha256=inputs['object_sha256'],
        requested_element_range=[args.first_element,args.last_element],
        exact_radial_interval=[str(a),str(b)],native_arguments=native,out_dir=str(args.out_dir))
    if args.check_only:
        print(json.dumps(dict(checked=True,numerical_work_performed=False,
            requested_element_range=identity['requested_element_range'],
            exact_radial_interval=identity['exact_radial_interval'],
            frozen_input_files=len(listed),runtime=runtime,command=command),indent=2),flush=True)
        return
    provenance=args.out_dir/'worker_provenance.json'
    if provenance.exists() and read(provenance)['identity']!=identity:
        raise ValueError('an existing output directory belongs to a different frozen job')
    preserved=[]
    for element in range(args.first_element,args.last_element):
        old=args.out_dir/f'element_{element:03d}.json.gz'
        if old.exists() and not read(old).get('complete'):
            digest=sha(old);destination=args.out_dir/'recovery'/f'element_{element:03d}_{digest}.json.gz'
            destination.parent.mkdir(parents=True,exist_ok=True)
            if not destination.exists():shutil.copyfile(old,destination)
            if sha(destination)!=digest:raise ValueError('an incomplete proof checkpoint was not preserved exactly')
            preserved.append(dict(path=str(destination),sha256=digest))
    result=dict(kind='frozen_native_cap_disjoint_CI_worker',complete=False,identity=identity,
        runtime=runtime,command=command,preserved_incomplete_reports=preserved,
        scope='Only the requested exact FE range. Missing intervals are never replaced by zero; original complete FE reports must pass their own full mathematical fees.')
    save(provenance,result)
    env=os.environ.copy()
    env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
    started=time.monotonic()
    process=subprocess.run(command,env=env,check=False)
    result['observed_child_returncode']=process.returncode
    result['wall_seconds']=time.monotonic()-started
    if process.returncode:
        save(provenance,result)
        raise SystemExit(process.returncode if process.returncode>0 else 128-process.returncode)
    manifest=args.out_dir/'manifest.json';finished=read(manifest)
    if (not finished['complete']
        or finished['requested_element_range']!=[args.first_element,args.last_element]
        or finished['requested_exact_radial_interval']!=[str(a),str(b)]
        or finished['identity']['source_sha256']!=sha(kernel)
        or finished['identity']['object_sha256']!=inputs['object_sha256']):
        raise ValueError('the original native kernel did not complete the precise requested job')
    if [item['element'] for item in finished['elements']]!=list(range(args.first_element,args.last_element)):
        raise ValueError('native worker completion has missing, repeated or extra finite elements')
    for item in finished['elements']:
        if not item['complete'] or sha(item['path'])!=item['sha256']:
            raise ValueError('a completed native FE proof is absent or differs')
        proof=read(item['path'])
        if not proof['complete'] or proof['identity']!=finished['identity']:
            raise ValueError('native FE proof identity differs from its manifest')
    result.update(complete=True,completed_manifest=dict(path=str(manifest),sha256=sha(manifest)),
        completed_elements=finished['elements'])
    save(provenance,result)
    print(json.dumps(dict(complete=True,requested_element_range=identity['requested_element_range'],
        completed_manifest=result['completed_manifest'],wall_seconds=result['wall_seconds']),indent=2),flush=True)


if __name__=='__main__':main()
