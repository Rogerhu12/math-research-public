#!/usr/bin/env python3
"""Retain full-input M28 variational stages without changing the tail equations.

This explicit Python adapter selects the already frozen exact-stage worker.
The original accepted/pending prefix, source, full-H, physical-profile, RMS and
tail guards remain. A separate diagnostic compares every complete evaluate
output byte and is never a nonlinear response. Normal mode still executes the
original full nonlinear solve, Jacobian, positivity gates and complete audit.
Only exact complete cache entries are reusable; M24 entries are never M28 data.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
for key in tuple(os.environ):
    if key in ('GH_TOKEN','GITHUB_TOKEN','GITHUB_PAT') or key.startswith('GIT_CONFIG_'):
        os.environ.pop(key,None)
import argparse
import ast
import hashlib
import json
from pathlib import Path
import sys
import time
import numpy as np
import strong_sameg_m28_staged_audit as original

HERE=Path(__file__).resolve().parent
SELF_SHA=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
STAGED_SHA='2bfd570f1497022767b0736d099ab42d248cd492a8914f3c69707fed3ef6bf8f'
STAGE_SHA='b6f587ac428a477f32e04c13a2686ecb196cbefd342deadc669e13cc988e6753'
YOUNG_GUARD_SHA="867244ef03a99ea50f7629d437873c073e9a07ee8a88b48568c79817be7b7eba"
ANCHOR='        response = tail.solve(height, jacobian=True, audit=True)'
DIAGNOSTIC=r"""        if STRONG_CACHE_DIAGNOSTIC:
            request=dict(height=height.tolist(),jacobian=True,audit=True,exactStageDiagnostic=True)
            tail.proc.stdin.write(json.dumps(request)+'\n');tail.proc.stdin.flush()
            line=tail.proc.stdout.readline()
            if not line:
                raise RuntimeError('M28 complete-evaluate diagnostic worker stopped')
            answer=json.loads(line);check=answer.get('exactStageDiagnostic',{})
            if (not check.get('passed') or check.get('nonlinearSolution') or
                    check.get('nonlinearSolves')!=0 or check.get('finalAudits')!=0 or
                    not check.get('literalEveryOutputFloat64ByteCompared') or
                    check.get('modes')!=modes or
                    check.get('stagesCompared')!=tail.ready['parameters']['depth']):
                raise ValueError('Original complete M28 evaluate byte comparison failed')
            diagnostic_path=prefix.with_name(prefix.name+'-diagnostic.json')
            diagnostic_path.write_text(json.dumps(answer,indent=2)+'\n')
            result.update(status='diagnostic-complete',tail_converged=False,
                diagnostic=str(diagnostic_path),diagnostic_sha256=sha(diagnostic_path),
                original_complete_evaluate_bitwise_equal=True,
                no_nonlinear_solve_or_final_audit_performed=True,
                complete_height_exactly_matched=True)
            return
        response = tail.solve(height, jacobian=True, audit=True)"""


def main():
    parser=argparse.ArgumentParser(add_help=False)
    parser.add_argument('--cache-directory',type=Path,required=True)
    parser.add_argument('--seed-prefix',type=Path,required=True)
    parser.add_argument('--initial-seed',type=Path)
    parser.add_argument('--diagnostic-complete-evaluate',action='store_true')
    args,remaining=parser.parse_known_args()
    def argument(name):
        if remaining.count(name)!=1:
            raise ValueError('Exactly one '+name+' is required')
        return Path(remaining[remaining.index(name)+1])
    out=argument('--out-prefix');topic=argument('--source-topic').resolve()
    if original.stage.sha(original.__file__)!=STAGED_SHA:
        raise ValueError('Original M28 whole-field and complete-H guard source changed')
    root_source=Path(original.stage.__file__).read_text()
    if hashlib.sha256(root_source.encode()).hexdigest()!=STAGE_SHA:
        raise ValueError('Original staged full-audit source changed')
    if root_source.count(ANCHOR)!=1:
        raise ValueError('Original full-audit call anchor changed')
    # The persistent engine intentionally rejects all symlinks in each source
    # tree. Use byte-identical real files, not a symlink runtime snapshot.
    for root in (HERE,topic,topic/'repro/source-root'):
        if not root.is_dir():
            raise FileNotFoundError(root)
        for item in root.rglob('*'):
            if item.is_symlink():
                raise ValueError('Stage identity requires a real-file source snapshot: '+str(item))
    # All Python sources are an additional effective cache-key coordinate.
    # The frozen MJS engine's native identity remains untouched and continues
    # to bind every actual stage dependency. This outer namespace can only
    # turn a putative hit into a conservative miss.
    python_roots={'adapter':HERE,'physical_topic':topic,
                  'physical_root':topic/'repro/source-root'}
    python_trees={role:{str(file.relative_to(root)):original.stage.sha(file)
                       for file in sorted(root.rglob('*.py'))}
                  for role,root in python_roots.items()}
    python_identity=dict(schema='M28-complete-Python-source-namespace-v1',
        trees=python_trees,source_root_paths={role:str(root) for role,root in python_roots.items()},
        adapter_entry_sha256=SELF_SHA)
    python_identity_bytes=(json.dumps(python_identity,sort_keys=True,
        separators=(',',':'),allow_nan=False)+'\n').encode()
    python_identity_sha=hashlib.sha256(python_identity_bytes).hexdigest()
    cache_base=args.cache_directory.resolve()
    cache_directory=cache_base/('python-'+python_identity_sha)
    cache_directory.mkdir(parents=True,exist_ok=True)
    python_identity_file=cache_directory/'Python-source-identity.json'
    original.spectral.atomic_new_or_same(python_identity_file,python_identity)
    source=root_source.replace(ANCHOR,DIAGNOSTIC,1)
    ast.parse(source,filename='<M28-original-stage-with-explicit-diagnostic>')
    names=('strong_exact_stage_tail_client.py','strong_exact_stage_tail_worker.mjs',
        'strong_exact_stage_engine.mjs','strong_exact_stage_flow_store.mjs',
        'strong_exact_stage_seed.mjs','strong_exact_stage_evaluation_check.mjs',
        'strong_exact_raw_tail_client.py','strong_exact_raw_tail_worker.mjs',
        'strong_exact_raw_tail_warm.mjs','strong_tail_young_space_guard.py',
        'strong_tail_constructor_guard.py')
    hashes={name:original.stage.sha(HERE/name) for name in names}
    if hashes['strong_tail_young_space_guard.py']!=YOUNG_GUARD_SHA:
        raise ValueError('The explicit exact-stage resource adapter changed')
    seed_record=None
    if args.initial_seed:
        seed_record=original.stage.read_json(args.initial_seed)
        cp=seed_record.get('checkpoint',seed_record)
        if seed_record.get('status')!='initial-warm-only' or not cp.get('exactInitialSeed'):
            raise ValueError('Only a recorded exact initial seed is permitted here')
        if not isinstance(cp.get('cutHeight'),list) or len(cp['cutHeight'])!=28:
            raise ValueError('Exact seed lacks the full M28 physical H')
    record=dict(scope=__doc__,entry_sha256=SELF_SHA,
        original_M28_guard_sha256=STAGED_SHA,original_full_stage_sha256=STAGE_SHA,
        source_sha256=hashes,transformed_stage_sha256=hashlib.sha256(source.encode()).hexdigest(),
        source_transforms=[dict(before=ANCHOR,after=DIAGNOSTIC,count=1)],
        cache_directory=str(cache_directory),cache_base_directory=str(cache_base),
        effective_cache_key=['complete Python snapshot SHA','original native stage identity','complete native input key'],
        complete_python_source_namespace=dict(sha256=python_identity_sha,
            manifest=str(python_identity_file),file_sha256=original.stage.sha(python_identity_file),
            files=sum(len(tree) for tree in python_trees.values()),
            adding_or_changing_any_Python_source_selects_a_new_namespace=True,
            original_native_MJS_cache_identity_unchanged=True),
        seed_prefix=str(args.seed_prefix.resolve()),
        initial_seed=None if args.initial_seed is None else
            dict(file=str(args.initial_seed),sha256=original.stage.sha(args.initial_seed)),
        diagnostic_only=bool(args.diagnostic_complete_evaluate),
        normal_mode_requires_original_full_solve_Jacobian_and_audit=True,
        source_trees_have_no_symlinks=True,MJS_sources_modified=False,
        persistent_identity_includes_Node_V8_platform_arch_and_complete_source=True,
        resource_factory_binding=dict(
            original_module='strong_sameg_spectral_refinement',
            original_module_sha256=original.stage.sha(original.spectral.__file__),
            replacement_module='strong_tail_young_space_guard',
            replacement_module_sha256=YOUNG_GUARD_SHA,
            replacement_function='resource_port_class',
            original_recognized_worker='tail_frozen_worker.mjs',
            actual_recognized_worker='strong_exact_stage_tail_worker.mjs',
            same_explicit_old_and_young_heap_arguments=True,
            original_one_owned_spawn_and_cleanup_guards_retained=True,
            purely_Python_launch_binding=True),
        prefix_Newton_calls=0,changed_physical_metric_or_tail_parameters=[],
        command_arguments=[v for v in remaining if v!='--prepare-only'],
        status='prepared; no new numerical acceptance')
    manifest=out.with_name(out.name+'-stage-cache-adapter.json')
    original.spectral.atomic_new_or_same(manifest,record)
    namespace=dict(__file__=str(Path(original.stage.__file__)),__name__='strong_m28_cached_original_stage',
                   STRONG_CACHE_DIAGNOSTIC=bool(args.diagnostic_complete_evaluate))
    exec(compile(source,'<M28-original-stage-with-explicit-diagnostic>','exec'),namespace)
    staged_main=namespace['main']
    # Import the exact-stage class before replacing the frozen class. Its
    # original protocol constructor therefore retains the real frozen template.
    import strong_exact_stage_tail_client
    import strong_tail_young_space_guard as young_guard
    import tail_frozen_client
    if (original.stage.sha(young_guard.__file__)!=YOUNG_GUARD_SHA or
            young_guard.WORKER_SHA!=hashes['strong_exact_stage_tail_worker.mjs']):
        raise ValueError('The resource factory is not bound to the actual frozen stage worker')
    old_class=tail_frozen_client.WeightedTailPort
    old_main=original.stage.main
    old_resource_factory=original.spectral.resource_class
    oldargv=sys.argv
    env_keys=('VISIBLE_FLEX_EXACT_STAGE_CACHE','VISIBLE_FLEX_EXACT_STAGE_SEED_PREFIX',
              'VISIBLE_FLEX_SOURCE_TOPIC','VISIBLE_FLEX_SOURCE_ROOT')
    old_env={key:os.environ.get(key) for key in env_keys}
    os.environ['VISIBLE_FLEX_EXACT_STAGE_CACHE']=str(cache_directory)
    os.environ['VISIBLE_FLEX_EXACT_STAGE_SEED_PREFIX']=str(args.seed_prefix.resolve())
    os.environ['VISIBLE_FLEX_SOURCE_TOPIC']=str(topic)
    os.environ['VISIBLE_FLEX_SOURCE_ROOT']=str(topic/'repro/source-root')
    tail_frozen_client.WeightedTailPort=strong_exact_stage_tail_client.WeightedTailPort
    def execute_after_original_guards():
        # original.main has already checked the accepted raw against the old
        # full-J response and every original physical/source datum. A seed may
        # replace only the I/O warm filename used by the true worker.
        guard=original.stage.read_json(out.with_name(out.name+'-recovery-guards.json'))
        prior_argv=sys.argv
        argv=list(prior_argv)
        if args.initial_seed:
            cp=seed_record.get('checkpoint',seed_record)
            if (np.asarray(cp['cutHeight'],dtype=np.float64).tobytes()!=
                    np.asarray(guard['physical_height'],dtype=np.float64).tobytes()):
                raise ValueError('The exact seed is for another complete physical H')
            argv[argv.index('--warm')+1]=str(args.initial_seed)
        try:
            sys.argv=argv
            return staged_main()
        finally:
            sys.argv=prior_argv
    original.stage.main=execute_after_original_guards
    # The original frozen-only launch wrapper cannot recognize a stage worker.
    # Use the previously validated stage-specific wrapper with identical heap
    # arguments; this changes no MJS, source/cache identity or mathematical path.
    original.spectral.resource_class=young_guard.resource_port_class
    started=time.monotonic();failure=None
    try:
        sys.argv=[oldargv[0],*remaining]
        original.main()
    except BaseException as exc:
        failure=repr(exc)
        raise
    finally:
        original.stage.main=old_main
        original.spectral.resource_class=old_resource_factory
        tail_frozen_client.WeightedTailPort=old_class
        sys.argv=oldargv
        for key,value in old_env.items():
            if value is None:os.environ.pop(key,None)
            else:os.environ[key]=value
        result=dict(entry_sha256=SELF_SHA,seconds=time.monotonic()-started,error=failure,
            diagnostic_only=bool(args.diagnostic_complete_evaluate),
            prepare_only='--prepare-only' in remaining,
            original_stage_summary=str(out.with_name(out.name+'-summary.json')),
            prefix_accepted=False,mathematical_gates_not_replaced_by_cache=True)
        summary=out.with_name(out.name+'-summary.json')
        if summary.exists():
            end=original.stage.read_json(summary)
            result.update(observed_stage_status=end.get('status'),
                observed_tail_converged=end.get('tail_converged'),
                response=end.get('response'),response_sha256=end.get('response_sha256'),
                worker_returncode_before_close=end.get('worker_returncode_before_close'),
                worker_returncode_after_close=end.get('worker_returncode_after_close'))
        suffix='-stage-cache-prepare-terminal.json' if '--prepare-only' in remaining else '-stage-cache-terminal.json'
        original.spectral.atomic_new_or_same(out.with_name(out.name+suffix),result)

if __name__=='__main__':main()
