#!/usr/bin/env python3
"""Install a minimal whole-evaluate hook into an independent source copy.

This preparation only copies/patches source, checks syntax and binds metadata.
It never imports a model, calls a compiler, starts the native CLI or runs a flow.
The original lexical norm/correction/line-search/cut/audit code is unchanged.
"""
import argparse
import ast
import datetime
import gzip
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys


CORE_SHA='84f944c560dcb65dc3f6fda2e97f3ebc549f1dbcdcc1fe2525324561d754c3be'
SPLIT_SHA='e93b9e946e8b9b5916bfefc8bc64b44094eb5c62a6eff1eab73f2381d6c2d55a'
CPP_SHA='e5a7d3b0a1021aae54fabcd3c5baae0558cab4246b4a10cfdeb31b6d275a8ddf'


def ref(p):
    p=Path(p).resolve()
    return dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest())


def save(p,data):
    with Path(p).open('x') as f:
        json.dump(data,f,indent=2,ensure_ascii=False,allow_nan=False);f.write('\n')
    return ref(p)


def load(p):
    p=Path(p)
    return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())


def once(text,before,after):
    if text.count(before)!=1:
        raise ValueError('Expected exactly one original source block: '+before)
    return text.replace(before,after,1)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace',type=Path,required=True)
    parser.add_argument('--out-dir',type=Path,required=True)
    parser.add_argument('--owned-source',type=Path,required=True)
    args=parser.parse_args();w=args.workspace.resolve();out=args.out_dir.resolve()
    destination=args.owned_source.resolve()
    topic=w/'math-research-public/topics/visible-flex-held-10pct'
    own=topic/'scripts/resume_n4_tail/native_extended'
    source=w/'n4_work/shared-periodic-source'
    if out.exists() or destination.exists():
        raise ValueError('Fresh preparation directory and independent owned source required')
    build_path=w/'n4_work/native-production-floor-v1/build.json';build=load(build_path)
    if not build['success'] or build['files']['production_cpp']['sha256']!=CPP_SHA:
        raise ValueError('The reviewed production-floor build is required')
    for item in [*build['files'].values(),build['library'],build['batch_executable']]:
        if ref(item['path'])!=item:raise ValueError('Changed build/source reference')
    core_path=source/'scripts/950f-tail-stage-core.mjs'
    split_path=source/'scripts/950f-tail-stage-split.mjs'
    worker_path=source/'scripts/950f-tail-stage-port-v3.mjs'
    if ref(core_path)['sha256']!=CORE_SHA or ref(split_path)['sha256']!=SPLIT_SHA:
        raise ValueError('The current shared/periodic sparse source is required')
    original_core=core_path.read_text();core=original_core
    patches=[]
    before=' function evaluate(states,target,withJac,scales){'
    after=""" let nativeBatch=null;
 function getNativeBatch(){
  if(!options.nativeBatchFactory)throw Error('No native batch factory installed');
  if(!nativeBatch)nativeBatch=options.nativeBatchFactory({cells,M,spacing,quadrature,steps,projectionFloor,orientation,cuspAwareFlow,physicalParameters:physical.parameters});
  return nativeBatch;
 }
 function evaluate(states,target,withJac,scales){"""
    patches.append(dict(file=core_path.name,before=before,after=after))
    core=once(core,before,after)
    before='  const flows=[],residuals=[];let norm=0,minA=Infinity,minD=Infinity;\n  for(let n=0;n<depth;n++){\n   const f=cellFlow(n,states[n+1],withJac),r='
    after='  const flows=[],residuals=[];let norm=0,minA=Infinity,minD=Infinity;\n  const nativeFlows=options.nativeBatchFactory?getNativeBatch().evaluate(states,withJac):null;\n  for(let n=0;n<depth;n++){\n   const f=nativeFlows?nativeFlows[n]:cellFlow(n,states[n+1],withJac),r='
    patches.append(dict(file=core_path.name,before=before,after=after))
    core=once(core,before,after)
    before=' return {solve,initial,evaluate,cells,graphs,gains,physical,rawNode:stages.rawNode,parameters:'
    after=' return {...(options.nativeBatchFactory?{nativeBatch:getNativeBatch}:{}),solve,initial,evaluate,cells,graphs,gains,physical,rawNode:stages.rawNode,parameters:'
    patches.append(dict(file=core_path.name,before=before,after=after))
    core=once(core,before,after)
    restored=core
    for patch in reversed(patches):
        restored=once(restored,patch['after'],patch['before'])
    if restored!=original_core:
        raise AssertionError('Unexpected edit outside the exact lexical flow-source/interface hook')
    original_worker=worker_path.read_text()
    before="import {createSplitFluxCompactTailDN as createCompactTailDN} from './950f-tail-stage-split.mjs';"
    after="import {createNativeCompactTailDN as createCompactTailDN} from './native_batch_factory.mjs';"
    worker=once(original_worker,before,after)
    patches.append(dict(file=worker_path.name,before=before,after=after))
    original_sources=[ref(p) for p in sorted(source.rglob('*.mjs'))]
    for p in [Path(__file__)]:
        ast.parse(p.read_text(),filename=str(p))
    for name in ['native_batch_adapter.mjs','native_batch_factory.mjs','probe_native_adapter_entry.mjs']:
        if not (own/name).is_file():raise ValueError('Complete adapter/probe source required')
    shutil.copytree(source,destination,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
    (destination/'scripts/950f-tail-stage-core.mjs').write_text(core)
    (destination/'scripts/950f-tail-stage-port-v3.mjs').write_text(worker)
    for name in ['native_batch_adapter.mjs','native_batch_factory.mjs']:
        shutil.copyfile(own/name,destination/'scripts'/name)
    out.mkdir(parents=True,exist_ok=False)
    syntax=[]
    node=Path(shutil.which('node')).resolve()
    for p in [destination/'scripts/950f-tail-stage-core.mjs',destination/'scripts/950f-tail-stage-port-v3.mjs',
              destination/'scripts/native_batch_adapter.mjs',destination/'scripts/native_batch_factory.mjs',
              own/'probe_native_adapter_entry.mjs']:
        command=[str(node),'--check',str(p)]
        result=subprocess.run(command,capture_output=True,text=True,check=False)
        syntax.append(dict(command=command,returncode=result.returncode,
            stdout=result.stdout,stderr=result.stderr,source=ref(p)))
        if result.returncode!=0:raise RuntimeError('Source syntax rejected: '+str(p))
    for item in original_sources:
        if ref(item['path'])!=item:raise AssertionError('Original source tree changed')
    ld=load(w/'n4_work/native-longdouble-pair-v1/readout-summary.json')
    runtime_names={'ld-linux-x86-64.so.2','libc.so.6','libgcc_s.so.1','libm.so.6','libstdc++.so.6.0.33'}
    libraries=[item for item in ld['loaded_runtime']['mapped_binaries'] if Path(item['path']).name in runtime_names]
    if len(libraries)!=5:raise ValueError('Incomplete prior runtime-library identity')
    for item in libraries:
        if ref(item['path'])!=item:raise ValueError('Runtime library changed')
    cp=build['files']['production_CP'];capsule=build['files']['capsule_coefficients']
    manifest=save(out/'manifest.json',dict(schema='n4-native-batch-adapter-v1',
        source_topic=str(destination),original_source_topic=str(source),
        installer=ref(__file__),original_sources=original_sources,
        owned_sources=[ref(p) for p in sorted(destination.rglob('*.mjs'))],
        source_patches=patches,original_core_restored_exactly=True,
        native_files=dict(build=ref(build_path),cpp=build['files']['production_cpp'],
            header=build['files']['header'],executable=build['batch_executable']),
        runtime_libraries=libraries,
        fixed_scope=dict(M=20,spacing=4,quadrature=512,steps=16,projectionFloor=.05,
            orientation=1,cuspAwareFlow=True,stageCount=2304),
        physical_source_input=cp,original_capsule=capsule,
        gate_scope='No norm/target/scales/far Robin/correction/line-search/stop/cut/audit edits. The only numerical provider change is whole-evaluate native state and literal implicit Jacobian; original code consumes first40 rows and only output pi is port-normalized.',
        engine_scope='Same-mu Map and split Object.assign identity untouched. Native coefficients are cached lazily per fixed DN, after actual split/cusp replacement.',
        error_scope='CLI/protocol/native-stage errors retain stdout/stderr/partial binary output and an explicit classification. Original trial catch remains byte-identical; a recorded engineering interruption is not a mathematical obstruction.',
        token_scope='Payload SHA only; all source, executable and library fingerprints are separate bindings.',
        preparation_only=True,new_physical_constructor=False,new_flow=False))
    observer=ref(topic/'scripts/resume_n4/observe_command_live.py')
    probe=ref(own/'probe_native_adapter_entry.mjs')
    plan_path=out/'plan.json'
    command=[str(node),'--max-old-space-size=1536',probe['path'],'--plan',str(plan_path)]
    files=dict(installer=ref(__file__),adapter=ref(own/'native_batch_adapter.mjs'),
        factory=ref(own/'native_batch_factory.mjs'),probe=probe,manifest=manifest,
        production_CP=cp,capsule_coefficients=capsule,build=ref(build_path),node=ref(node),observer=observer,
        finite_interface_terminal=ref(topic/'scripts/resume_n4_tail/native_production_floor_batch_terminal.json'))
    plan=save(plan_path,dict(schema='n4-native-adapter-entry-v1',scope=__doc__,
        prepared_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        preparation_command=sys.argv,files=files,syntax_checks=syntax,
        source_topic=str(destination),run_directory=str(out/'actual-entry'),
        outputs=dict(summary=str(out/'entry-summary.json'),raw=str(out/'entry-raw.json.gz')),
        command=command,observer_command=['python',observer['path'],'--log',str(out/'entry-process.log'),
            '--out',str(out/'entry-resource.json'),'--',*command],
        prescribed_operations=[
            'Construct exactly the original physical/linear-graph DN from the complete saved failed CP config, using owned provider hook.',
            'Build actual cusp grids independently along original scalar and variational paths; require literal x/h equality, then freeze original Number coefficients/trig.',
            'Before any native call, require original43/38/175 all coefficient points, trig, input42, scales, portRatio and literal grids byte-identical to the saved capsule; .05 is the production gate.',
            'Invoke exactly one complete original lexical evaluate(states,target,true,scales), one CLI process for all2304 actual stages.',
            'Retain complete raw binary42/42x40 outputs and original residual/J-consumption results; no Newton correction, DN solve, cutJets or audit in this one entry probe.'],
        native_evaluate_count=1,native_stage_process_count=1,withJac=True,
        same_state_cp_is_accepted=False,
        source_preparation_invoked_models_or_flows=False,
        budgets_scope='Actual cusp p/s and wire sizes will be measured once static packing executes. Existing ordinary33point/16step estimates are not an observation of every actual stage.',
        subsequent_scope='If transport and original full residual complete, use the same owned worker in an actual original DN solve with original2e-9/line search/Jac/audit. No automatic retry or changed physical target is included here.'))
    print(json.dumps(dict(plan=plan,manifest=manifest,source_topic=str(destination),
        syntax_checks=len(syntax),model_constructed=False,native_calls=0)),flush=True)


if __name__=='__main__':
    main()
