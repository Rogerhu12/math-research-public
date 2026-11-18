#!/usr/bin/env python3
"""Prepare an owned adapter using the unchanged native CLI through four workers.

The original complete input wire, output decoder, port-row conversion and
lexical DN solver are preserved. Only process execution and its independently
bound metadata change. This installer does not construct a physical model,
invoke a native flow, or execute a DN. Its only subprocess is node --check.
"""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys


PRIOR_MANIFEST_SHA = '3e618b4a44c2292a1d12612ceb3a6f82693e703a32b152fa5a42097cb6d877d2'
ADAPTER_SHA = '9931feea9bc905cdc700c4f5078a6ad2af0a215fa5bc2fd1c84212662cbd2718'
WRAPPER_SHA = '9177a8499517695deebf00907c64bdc08adc5e5fd2229c8987a2a7ac8ef6bb42'
EQUIVALENCE_PLAN_SHA = '0bcf040ae92c8dec850ed5786bde31648b0e7f6282af519c2e4468b1d8b027fe'
EQUIVALENCE_RECORD_SHA = 'f97357791f8540835d62c2d1b59b9110965b8a2f504cc001db8aa4dded0decc4'


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def verify(item):
    if ref(item['path'])['sha256'] != item['sha256']:
        raise ValueError('Bound source changed: ' + item['path'])


def save(path, data):
    with Path(path).open('x') as stream:
        json.dump(data, stream, indent=2, ensure_ascii=False, allow_nan=False)
        stream.write('\n')
    return ref(path)


def once(text, before, after):
    if text.count(before) != 1:
        raise ValueError('Expected exactly one declared adapter block')
    return text.replace(before, after, 1)


CHECK_EXECUTION = """function checkParallelExecution(manifest){
  const execution=manifest.execution_provider;
  assert(execution?.kind==='unchanged-native-cli-parallel-wire-v1'&&execution.workers===4,'Expected the four-worker unchanged-CLI provider');
  for(const key of ['wrapper','python','plan','equivalence_record'])exactFile(execution[key]);
  const plan=JSON.parse(fs.readFileSync(execution.plan.path,'utf8'));
  assert(plan.workers===execution.workers&&plan.retain_shards===true,'Parallel execution settings changed');
  assert(plan.source.path===execution.wrapper.path&&plan.source.sha256===execution.wrapper.sha256,'Parallel wrapper/plan binding differs');
  assert(plan.native_cli.path===manifest.native_files.executable.path&&plan.native_cli.sha256===manifest.native_files.executable.sha256,'Parallel child is not the bound original native CLI');
  return execution;
}

export function readNativeManifest(){"""


VERIFY_WRAPPER_TERMINAL = """      assert(outcome.parallel_record!==null,'Missing parallel process terminal metadata');
      const parallel=JSON.parse(fs.readFileSync(outcome.parallel_record.path,'utf8'));
      assert(parallel.source.path===execution.wrapper.path&&parallel.source.sha256===execution.wrapper.sha256,'Actual parallel wrapper differs');
      assert(parallel.plan.path===execution.plan.path&&parallel.plan.sha256===execution.plan.sha256,'Actual parallel execution plan differs');
      assert(parallel.native_cli.path===manifest.native_files.executable.path&&parallel.native_cli.sha256===manifest.native_files.executable.sha256,'Actual original child CLI differs');
      assert(parallel.original_input.path===outcome.input.path&&parallel.original_input.sha256===outcome.input.sha256,'Parallel input identity differs');
      assert(parallel.workers===4&&parallel.parent_returncode===child.status,'Parallel worker count/return code differs');
      assert(parallel.success===(child.status===0),'Parallel success/status differs');
      assert(parallel.records.length===4,'Incomplete parallel child terminal records');
      for(const record of parallel.records){
        assert(record.returncode===0||record.returncode===3,'Parallel child had an engineering failure');
        for(const key of ['input','output','stdout','stderr'])exactFile(record[key]);
      }
      assert(!child.error&&child.signal===null,'Native process engineering interruption');"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', type=Path, required=True)
    parser.add_argument('--out-dir', type=Path, required=True)
    parser.add_argument('--owned-source', type=Path, required=True)
    args = parser.parse_args()
    workspace, out, destination = (p.resolve() for p in
                                   (args.workspace, args.out_dir, args.owned_source))
    topic = workspace / 'math-research-public/topics/visible-flex-held-10pct'
    prior_path = workspace / 'n4_work/native-node-adapter-v1/manifest.json'
    if ref(prior_path)['sha256'] != PRIOR_MANIFEST_SHA:
        raise ValueError('Prior serial owned adapter identity differs')
    prior = json.loads(prior_path.read_text())
    for item in [*prior['original_sources'], *prior['owned_sources'],
                 *prior['native_files'].values(), *prior['runtime_libraries']]:
        verify(item)
    source = Path(prior['source_topic'])
    adapter_path = source / 'scripts/native_batch_adapter.mjs'
    if ref(adapter_path)['sha256'] != ADAPTER_SHA:
        raise ValueError('Prior complete adapter source changed')
    wrapper = topic / 'scripts/resume_n4_tail/native_extended/parallel_native_batch.py'
    equivalence_plan = workspace / 'n4_work/native-parallel-equivalence-v1/plan.json'
    equivalence_record = topic / 'scripts/resume_n4_tail/native_parallel_equivalence.json'
    for path, expected in [(wrapper, WRAPPER_SHA), (equivalence_plan, EQUIVALENCE_PLAN_SHA),
                           (equivalence_record, EQUIVALENCE_RECORD_SHA)]:
        if ref(path)['sha256'] != expected:
            raise ValueError('Parallel equivalence/source reference changed: ' + str(path))
    eq_plan = json.loads(equivalence_plan.read_text())
    if eq_plan['workers'] != 4 or eq_plan['native_cli'] != prior['native_files']['executable']:
        raise ValueError('Tested parallel configuration differs from the unchanged CLI')
    if out.exists() or destination.exists():
        raise FileExistsError('A fresh preparation and owned source are required')
    original = adapter_path.read_text()
    text = original
    patches = []

    def replace(before, after):
        nonlocal text
        text = once(text, before, after)
        patches.append(dict(before=before, after=after))

    replace('export function readNativeManifest(){', CHECK_EXECUTION)
    replace('  for(const item of manifest.runtime_libraries)exactFile(item);\n  return {manifest,binding};',
            '  for(const item of manifest.runtime_libraries)exactFile(item);\n  checkParallelExecution(manifest);\n  return {manifest,binding};')
    replace('    exactFile(manifest.native_files.executable);\n    for(const item of manifest.runtime_libraries)exactFile(item);',
            '    exactFile(manifest.native_files.executable);\n    for(const item of manifest.runtime_libraries)exactFile(item);\n    const execution=checkParallelExecution(manifest);')
    replace("    const child=spawnSync(manifest.native_files.executable.path,[inputPath,outputPath],\n      {encoding:null,maxBuffer:16*1024*1024});",
            "    const command=[execution.python.path,execution.wrapper.path,inputPath,outputPath,'--plan',execution.plan.path];\n    const child=spawnSync(command[0],command.slice(1),\n      {encoding:null,maxBuffer:16*1024*1024});")
    replace('    const outcome={call:calls,withJac:prepared.withJac,command:[manifest.native_files.executable.path,inputPath,outputPath],',
            "    const parallelPath=outputPath+'.parallel.json';\n    const outcome={call:calls,withJac:prepared.withJac,command,\n      execution_provider:execution,original_native_executable:manifest.native_files.executable,\n      parallel_record:fs.existsSync(parallelPath)?ref(parallelPath):null,")
    replace("      assert(!child.error&&child.signal===null,'Native process engineering interruption');", VERIFY_WRAPPER_TERMINAL)
    restored = text
    for patch in reversed(patches):
        restored = once(restored, patch['after'], patch['before'])
    if restored != original:
        raise AssertionError('Changes extend beyond the declared process/metadata blocks')
    shutil.copytree(source, destination, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    new_adapter = destination / 'scripts/native_batch_adapter.mjs'
    new_adapter.write_text(text)
    for item in prior['owned_sources']:
        old = Path(item['path'])
        copied = destination / old.relative_to(source)
        if old != adapter_path and copied.read_bytes() != old.read_bytes():
            raise AssertionError('Another owned mathematical/solver source changed')
    out.mkdir(parents=True)
    execution_plan = save(out / 'execution-plan.json', dict(
        scope='Future complete original-DN input wires, four unchanged original CLI processes per evaluate. No arithmetic/kernel/gate change; the separate equivalent2304-stage run is provenance, not a new physical acceptance.',
        source=ref(wrapper), native_cli=prior['native_files']['executable'],
        workers=4, retain_shards=True, equivalent_complete_batch_plan=ref(equivalence_plan),
        equivalent_complete_batch_record=ref(equivalence_record),
        fixed_adapter_scope=prior['fixed_scope']))
    execution = dict(kind='unchanged-native-cli-parallel-wire-v1', workers=4,
        wrapper=ref(wrapper), python=ref(sys.executable), plan=execution_plan,
        equivalence_record=ref(equivalence_record),
        scope='The wrapper is not the C++ binary. native_files.executable remains the original C++ CLI; wrapper/plan/Python are bound separately.')
    manifest = dict(prior, source_topic=str(destination), installer=ref(__file__),
        previous_owned_manifest=ref(prior_path), previous_owned_source_topic=str(source),
        owned_sources=[ref(p) for p in sorted(destination.rglob('*.mjs'))],
        execution_provider=execution, parallel_adapter_patches=patches,
        previous_adapter_restored_exactly=True,
        no_new_numeric_source_or_protocol=True, new_physical_constructor=False, new_flow=False,
        engine_scope=prior['engine_scope'] + ' Complete stage wires are independently partitioned only after packing, and merged before the unchanged decoder.')
    manifest_ref = save(out / 'manifest.json', manifest)
    syntax = []
    node = Path(shutil.which('node')).resolve()
    for name in ['native_batch_adapter.mjs', 'native_batch_factory.mjs',
                 '950f-tail-stage-core.mjs', '950f-tail-stage-port-v3.mjs']:
        path = destination / 'scripts' / name
        command = [str(node), '--check', str(path)]
        done = subprocess.run(command, capture_output=True, text=True, check=False)
        syntax.append(dict(command=command, source=ref(path), returncode=done.returncode,
                           stdout=done.stdout, stderr=done.stderr))
        if done.returncode:
            raise RuntimeError('Derived source syntax rejected: ' + name)
    summary = save(out / 'preparation.json', dict(scope=__doc__, source=ref(__file__), command=sys.argv,
        prepared_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        prior_manifest=ref(prior_path), manifest=manifest_ref, execution_plan=execution_plan,
        owned_source_topic=str(destination), original_adapter=ref(adapter_path),
        derived_adapter=ref(new_adapter), exact_reverse_patch=True,
        all_other_owned_source_bytes_unchanged=True,
        wrapper=ref(wrapper), python=ref(sys.executable), node=ref(node),
        equivalence_plan=ref(equivalence_plan), equivalence_record=ref(equivalence_record),
        original_native_executable=prior['native_files']['executable'],
        syntax_checks=syntax, constructors=0, flow_calls=0, DN_calls=0,
        next='Use this manifest/source in a separately declared actual original-DN/coupled run. Existing35038 retains its original serial manifest.'))
    print(json.dumps(dict(summary=summary, manifest=manifest_ref, source_topic=str(destination),
                          derived_adapter=ref(new_adapter), native_calls=0)), flush=True)


if __name__ == '__main__':
    main()
