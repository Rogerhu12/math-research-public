#!/usr/bin/env python3
"""Prepare an independent n3/M8 whole-evaluate native provider.

Only source copying, reversible provider hooks, syntax checks and hashes are
performed. The original n3 norm, scales, Robin condition, sparse correction,
line search, stopping test, cut jets and audits remain byte-identical.
The production domain floor is the original stage-core default .05, bound
also by the actual failed checkpoint. The separate three-fixture .1 root
baseline is retained with that restricted scope, not relabelled as .05.
"""
import argparse
import ast
import copy
import datetime
import gzip
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys


def ref(path):
    p=Path(path).resolve()
    return dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest())


def load(path):
    p=Path(path)
    return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())


def check(item):
    if ref(item['path'])!=item:raise ValueError('Bound source/input changed: '+item['path'])


def save(path,data):
    with Path(path).open('x') as f:json.dump(data,f,indent=2,ensure_ascii=False,allow_nan=False);f.write('\n')
    return ref(path)


def once(text,before,after):
    if text.count(before)!=1:raise ValueError('A unique original source block is required: '+before)
    return text.replace(before,after,1)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--workspace',type=Path,required=True)
    p.add_argument('--out-dir',type=Path,required=True)
    p.add_argument('--owned-source',type=Path,required=True)
    a=p.parse_args();w=a.workspace.resolve();out=a.out_dir.resolve();dest=a.owned_source.resolve()
    if out.exists() or dest.exists():raise FileExistsError('Use fresh independent output/source directories')
    topic=w/'math-research-public/topics/visible-flex-held-10pct'
    own=Path(__file__).resolve().parent
    source=w/'m3_work/recovered-valley-design/bundle/topics/visible-flexible-closed-surface'
    parent_path=w/'n4_work/native-parallel-adapter-v1/manifest.json'
    if ref(parent_path)['sha256']!='1661d97aba9dc5ac332ca859ad968b93164e8255df9d52a814d61338ada599c6':raise ValueError('The unchanged generic parallel adapter provenance changed')
    parent=load(parent_path)
    for item in [*parent['owned_sources'],*parent['native_files'].values(),*parent['runtime_libraries']]:check(item)
    for key in ('wrapper','python','plan','equivalence_record'):check(parent['execution_provider'][key])
    plan_path=w/'m3_work/trace-path-lam064-coupled-v1/launch-plan.json'
    if ref(plan_path)['sha256']!='498fcf2197aef47df981f0936e99c6d2d903e1976c85df4503133317b566d3a5':raise ValueError('Original n3 execution plan changed')
    plan=load(plan_path)
    for file,digest in plan['source_sha256'].items():check(dict(path=file,sha256=digest))
    failure_path=w/'m3_work/trace-path-lam064-coupled-v1/seed_tail_0001.json.gz'
    if ref(failure_path)['sha256']!='753aa9ec4584f0bafa216acbfaffe98fab44a0369e914ca06c7c739d81b365c4':raise ValueError('Use the original near-converged failed state')
    failed=load(failure_path);cfg=failed['config'];cp=failed['response']['checkpoint']
    if (cfg['modes'],cfg['spacing'],cfg['quadrature'],cfg['steps'],cfg['shootingParts'],cfg['solveTolerance'])!=(8,3,128,16,16,2e-9):raise ValueError('Original finite n3 problem differs')
    if cp['parameters']['projectionFloor']!=.05 or cfg.get('projectionFloor',.05)!=.05:raise ValueError('Keep the actual original stage-core domain floor .05')
    if len(cp['states'])!=1153 or any(len(row)!=16 for row in cp['states']):raise ValueError('Original full finite state is required')
    baseline_path=w/'m3_work/native-literal-baseline-v1/native-check/summary.json'
    baseline=load(baseline_path)
    if baseline['original_input']!=ref(failure_path) or not baseline['all_named_output_and_root_events_bitwise_equal'] or baseline['verified_output_count']!=54 or baseline['verified_event_count']!=130176:
        raise ValueError('The actual n3/M8 .1 fixture arithmetic baseline is required')
    for name in ('source','capsule_summary','coefficients','reference','native_library','native_executable','generic_CPP','header','ABI_helper','original_V8_helper','original_V8_bridge','raw'):check(baseline[name])
    core_path=source/'scripts/950f-tail-stage-core.mjs';worker_path=source/'scripts/950f-tail-stage-port-v3.mjs'
    if ref(core_path)['sha256']!='fdf5943ea9655f98cacd2c749d0155cfad08111c88915ce31b2c832bea68d68e':raise ValueError('Original n3 core changed')
    core_original=core_path.read_text();core=core_original;patches=[]
    before=' function evaluate(states,target,withJac,scales){'
    after=""" let nativeBatch=null;
 function getNativeBatch(){
  if(!options.nativeBatchFactory)throw Error('No native batch factory installed');
  if(!nativeBatch)nativeBatch=options.nativeBatchFactory({cells,M,spacing,quadrature,steps,projectionFloor,orientation,cuspAwareFlow,physicalParameters:physical.parameters});
  return nativeBatch;
 }
 function evaluate(states,target,withJac,scales){"""
    patches.append(dict(file=core_path.name,before=before,after=after));core=once(core,before,after)
    before='  const flows=[],residuals=[];let norm=0,minA=Infinity,minD=Infinity;\n  for(let n=0;n<depth;n++){\n   const f=cellFlow(n,states[n+1],withJac),r='
    after='  const flows=[],residuals=[];let norm=0,minA=Infinity,minD=Infinity;\n  const nativeFlows=options.nativeBatchFactory?getNativeBatch().evaluate(states,withJac):null;\n  for(let n=0;n<depth;n++){\n   const f=nativeFlows?nativeFlows[n]:cellFlow(n,states[n+1],withJac),r='
    patches.append(dict(file=core_path.name,before=before,after=after));core=once(core,before,after)
    before=' return {solve,initial,evaluate,cells,graphs,gains,physical,rawNode:stages.rawNode,parameters:'
    after=' return {...(options.nativeBatchFactory?{nativeBatch:getNativeBatch}:{}),solve,initial,evaluate,cells,graphs,gains,physical,rawNode:stages.rawNode,parameters:'
    patches.append(dict(file=core_path.name,before=before,after=after));core=once(core,before,after)
    restored=core
    for item in reversed(patches):restored=once(restored,item['after'],item['before'])
    if restored!=core_original:raise ValueError('An original mathematical core block changed')
    before="import {createSplitFluxCompactTailDN as createCompactTailDN} from './950f-tail-stage-split.mjs';"
    after="import {createNativeCompactTailDN as createCompactTailDN} from './native_batch_factory.mjs';"
    worker=once(worker_path.read_text(),before,after);patches.append(dict(file=worker_path.name,before=before,after=after))
    parent_source=Path(parent['source_topic'])
    adapter_path=parent_source/'scripts/native_batch_adapter.mjs';factory_path=parent_source/'scripts/native_batch_factory.mjs'
    if ref(adapter_path)['sha256']!='0eab1ee41a2c1851dbf9c17f2c608d68547ca779558c350ad954ed8ecfb5f530' or ref(factory_path)['sha256']!='4bf754298349103c1e5a4fe3c6330cb183bf61b9a306bbef2148eb531ef15c53':raise ValueError('Generic native transport source changed')
    adapter=adapter_path.read_text();adapter_patches=[]
    for before,after in [("manifest.schema==='n4-native-batch-adapter-v1'","manifest.schema==='m3-native-batch-adapter-v1'"),
        ("cell.engine.orientation===orientation&&cell.engine.quadratureIndependentNodes===nq,'Original periodic engine metadata differ'",
         "cell.engine.orientation===orientation&&(cell.engine.quadratureIndependentNodes??N)===nq,'Original actual engine quadrature metadata differ'")]:
        adapter=once(adapter,before,after);adapter_patches.append(dict(before=before,after=after))
    restored=adapter
    for item in reversed(adapter_patches):restored=once(restored,item['after'],item['before'])
    if restored!=adapter_path.read_text():raise ValueError('Unexpected generic transport arithmetic change')
    # The original n3 engines have no periodic metadata. Here gcd(128,3)=1,
    # so their literal all-N summations are exactly the native nq=N formula.
    if math_gcd(cfg['quadrature'],cfg['spacing'])!=1:raise ValueError('Original nonperiodic source requires gcd(N,spacing)=1')
    original_sources=[]
    files=[*sorted(source.rglob('*.mjs')),source/'scripts/950f-tail-client-v3.py']
    for file in files:
        original_sources.append(ref(file));target=dest/file.relative_to(source)
        target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(file,target)
    (dest/'scripts/950f-tail-stage-core.mjs').write_text(core)
    (dest/'scripts/950f-tail-stage-port-v3.mjs').write_text(worker)
    (dest/'scripts/native_batch_adapter.mjs').write_text(adapter)
    shutil.copyfile(factory_path,dest/'scripts/native_batch_factory.mjs')
    out.mkdir(parents=True,exist_ok=False)
    syntax=[];node=Path(shutil.which('node')).resolve()
    for name in ['950f-tail-stage-core.mjs','950f-tail-stage-port-v3.mjs','native_batch_adapter.mjs','native_batch_factory.mjs']:
        file=dest/'scripts'/name;cmd=[str(node),'--check',str(file)];r=subprocess.run(cmd,capture_output=True,text=True)
        syntax.append(dict(command=cmd,returncode=r.returncode,stdout=r.stdout,stderr=r.stderr))
        if r.returncode:raise RuntimeError('Owned syntax rejected: '+name)
    ast.parse(Path(__file__).read_text());ast.parse((dest/'scripts/950f-tail-client-v3.py').read_text())
    scope=dict(M=8,spacing=3,quadrature=128,steps=16,projectionFloor=.05,orientation=1,cuspAwareFlow=True,stageCount=1152)
    ex=copy.deepcopy(parent['execution_provider'])
    parallel_plan=dict(scope='Actual n3/M8 wires through four unchanged generic CLI children; no numeric decoding/rewriting. The old n4 transport case is historical provenance only.',source=ex['wrapper'],native_cli=parent['native_files']['executable'],workers=4,retain_shards=True,fixed_adapter_scope=scope,historical_transport_record=ex['equivalence_record'])
    ex['plan']=save(out/'execution-plan.json',parallel_plan)
    manifest=save(out/'manifest.json',dict(schema='m3-native-batch-adapter-v1',source_topic=str(dest),original_source_topic=str(source),
        installer=ref(__file__),original_execution_plan=ref(plan_path),original_sources=original_sources,
        owned_sources=[ref(file) for file in sorted(dest.rglob('*')) if file.is_file()],source_patches=patches,original_core_restored_exactly=True,
        native_files=copy.deepcopy(parent['native_files']),runtime_libraries=copy.deepcopy(parent['runtime_libraries']),
        execution_provider=ex,fixed_scope=scope,physical_source_input=ref(failure_path),parent_transport_manifest=ref(parent_path),
        adapter_patches=adapter_patches,parent_adapter_restored_exactly=True,
        independent_m3_fixture_baseline=ref(baseline_path),
        fixture_scope='The saved three-stage standalone point-root trace baseline uses .1; actual DN production floor remains .05. It is not a whole-state .05 acceptance.',
        quadrature_scope='Original nonperiodic n3 engines, gcd(128,3)=1: nq=N=128. No periodic source replacement or node reduction.',
        source_scope='Only original lexical whole-evaluate hook and worker factory import; original .05 cut/audit, target/norm/scales/Robin/Newton/line search/2e-9 gate remain.',
        preparation_only=True,model_constructed=False,flow_evaluated=False,DN_invoked=False))
    prep=save(out/'preparation.json',dict(scope=__doc__,source=ref(__file__),command=sys.argv,utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        manifest=manifest,source_topic=str(dest),syntax_checks=syntax,original_sources=len(original_sources),
        original_client_bytes_unchanged=ref(dest/'scripts/950f-tail-client-v3.py')['sha256']==ref(source/'scripts/950f-tail-client-v3.py')['sha256'],
        source_only=True,new_model=False,new_flow=False,new_DN=False))
    for item in original_sources:check(item)
    print(json.dumps(dict(manifest=manifest,preparation=prep,source_topic=str(dest),source_only=True)),flush=True)


def math_gcd(a,b):
    while b:a,b=b,a%b
    return a


if __name__=='__main__':main()
