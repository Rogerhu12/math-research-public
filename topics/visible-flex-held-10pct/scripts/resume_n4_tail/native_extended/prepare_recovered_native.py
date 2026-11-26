#!/usr/bin/env python3
"""Prepare the existing native solver in a new environment without lost plans.

Input must be an owned sparse/shared/periodic source tree. The mathematical
kernel, boundary equations, normalizations, Newton/line-search rules and all
acceptance gates are unchanged. The declared M/spacing/quadrature and the
fresh source/binary hashes replace references to unavailable old scratch.
The unchanged native wire splitter may use one to four CPUs. No solver or
old result is replayed as a preparation requirement.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def once(text, before, after):
    if text.count(before) != 1:
        raise ValueError('Expected one source anchor: ' + before)
    return text.replace(before, after, 1)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('source-topic', 'dest', 'native-cli'):
        p.add_argument('--' + key, type=Path, required=True)
    p.add_argument('--modes', type=int, required=True)
    p.add_argument('--spacing', type=int, required=True)
    p.add_argument('--quadrature', type=int, required=True)
    p.add_argument('--steps', type=int, default=16)
    p.add_argument('--workers', type=int, default=2)
    a = p.parse_args()
    if a.dest.exists():
        raise FileExistsError('Use a fresh owned destination')
    if not 1 <= a.workers <= 4:
        raise ValueError('Use one to four native workers')
    if a.quadrature <= 4*a.modes*a.spacing:
        raise ValueError('Retain the original strict quadrature bound')
    own = Path(__file__).resolve().parent
    source = a.source_topic.resolve()
    src_core = source / 'scripts/950f-tail-stage-core.mjs'
    text = src_core.read_text()
    if 'function sparseGlobalSolve(payload)' not in text or 'const engineCache=new Map();' not in text:
        raise ValueError('Prepare sparse/shared source before the native hook')
    if not (source/'scripts/periodic-quadrature').is_dir():
        raise ValueError('Prepare periodic source before the native hook')
    patches = []
    def replace(before, after):
        nonlocal text
        text = once(text, before, after)
        patches.append(dict(before=before, after=after))
    replace(' function evaluate(states,target,withJac,scales){', ''' let nativeBatch=null;
 function getNativeBatch(){
  if(!options.nativeBatchFactory)throw Error('No native batch factory installed');
  if(!nativeBatch)nativeBatch=options.nativeBatchFactory({cells,M,spacing,quadrature,steps,projectionFloor,orientation,cuspAwareFlow,physicalParameters:physical.parameters});
  return nativeBatch;
 }
 function evaluate(states,target,withJac,scales){''')
    replace('  const flows=[],residuals=[];let norm=0,minA=Infinity,minD=Infinity;\n  for(let n=0;n<depth;n++){\n   const f=cellFlow(n,states[n+1],withJac),r=',
            '  const flows=[],residuals=[];let norm=0,minA=Infinity,minD=Infinity;\n  const nativeFlows=options.nativeBatchFactory?getNativeBatch().evaluate(states,withJac):null;\n  for(let n=0;n<depth;n++){\n   const f=nativeFlows?nativeFlows[n]:cellFlow(n,states[n+1],withJac),r=')
    replace(' return {solve,initial,evaluate,cells,graphs,gains,physical,rawNode:stages.rawNode,parameters:',
            ' return {...(options.nativeBatchFactory?{nativeBatch:getNativeBatch}:{}),solve,initial,evaluate,cells,graphs,gains,physical,rawNode:stages.rawNode,parameters:')
    worker = source/'scripts/950f-tail-stage-port-v3.mjs'
    worker_text = once(worker.read_text(),
        "import {createSplitFluxCompactTailDN as createCompactTailDN} from './950f-tail-stage-split.mjs';",
        "import {createNativeCompactTailDN as createCompactTailDN} from './native_batch_factory.mjs';")
    shutil.copytree(source, a.dest, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    (a.dest/'scripts/950f-tail-stage-core.mjs').write_text(text)
    (a.dest/'scripts/950f-tail-stage-port-v3.mjs').write_text(worker_text)
    for name in ('native_batch_adapter.mjs', 'native_batch_factory.mjs'):
        shutil.copy2(own/name, a.dest/'scripts'/name)
    # Parallelism changes only process execution; the original binary,
    # per-stage numerical bytes and returned global order are preserved.
    parallel_plan = a.dest/'native-parallel-plan.json'
    parallel_plan.write_text(json.dumps(dict(native_cli=ref(a.native_cli), workers=a.workers,
                                            retain_shards=False), indent=2)+'\n')
    adapter = a.dest/'scripts/native_batch_adapter.mjs'
    text = adapter.read_text()
    replacement = f'''    const command=[{json.dumps(sys.executable)},{json.dumps(str(own/'parallel_native_batch.py'))},inputPath,outputPath,'--plan',{json.dumps(str(parallel_plan.resolve()))}];
    const child=spawnSync(command[0],command.slice(1),
      {{encoding:null,maxBuffer:16*1024*1024}});'''
    text = once(text, '    const child=spawnSync(manifest.native_files.executable.path,[inputPath,outputPath],\n      {encoding:null,maxBuffer:16*1024*1024});', replacement)
    text = once(text, 'command:[manifest.native_files.executable.path,inputPath,outputPath],', 'command,')
    adapter.write_text(text)
    for path in (a.dest/'scripts/950f-tail-stage-core.mjs', a.dest/'scripts/950f-tail-stage-port-v3.mjs', adapter):
        subprocess.run(['node', '--check', str(path)], check=True)
    manifest = dict(schema='n4-native-batch-adapter-v1', source_topic=str(a.dest.resolve()),
        original_source_topic=str(source), installer=ref(__file__),
        owned_sources=[ref(x) for x in sorted(a.dest.rglob('*.mjs'))],
        native_files=dict(executable=ref(a.native_cli), cpp=ref(own/'frozen_flow_production.cpp'),
                          header=ref(own/'frozen_flow.h'), parallel_wrapper=ref(own/'parallel_native_batch.py'),
                          parallel_plan=ref(parallel_plan)),
        runtime_libraries=[],
        fixed_scope=dict(M=a.modes, spacing=a.spacing, quadrature=a.quadrature, steps=a.steps,
                         projectionFloor=.05, orientation=1, cuspAwareFlow=True),
        source_patches=patches,
        gate_scope='Original equations, root and projection guards, residual normalization, Newton, line search, stopping tolerance, cut/audit unchanged.',
        provenance_scope='Fresh source/CLI binding; no assertion that the unavailable old field, binary, manifest, or execution environment has been recovered.',
        execution_provider=dict(workers=a.workers, wrapper=ref(own/'parallel_native_batch.py'), plan=ref(parallel_plan)),
        preparation_only=True)
    path = a.dest/'native-manifest.json'
    path.write_text(json.dumps(manifest, indent=2)+'\n')
    print(json.dumps(dict(source_topic=str(a.dest.resolve()), manifest=ref(path),
                         modes=a.modes, spacing=a.spacing, workers=a.workers)), flush=True)


if __name__ == '__main__':
    main()
