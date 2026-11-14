#!/usr/bin/env python3
"""Independent new-H tail audit with explicit completed-stage persistence.

The original endpoint, physical source and complete target-H guards are kept.
An optional diagnostic request runs and compares the entire original evaluate
twice, retaining every completed original stage and exact initial seed; it is
not a nonlinear response. Normal requests retain all original solve/audit gates.
"""
from __future__ import annotations
import ast
import hashlib
from pathlib import Path

HERE=Path(__file__).resolve().parent
TEMPLATE=HERE/'strong_warm_target_tail_audit.py'
EXPECTED='a670790d9521ee0425a8f5d00a0f90b6f3e66ae9ddf326ae046a4d7c7224e553'


def build_source():
    original=TEMPLATE.read_text()
    if hashlib.sha256(original.encode()).hexdigest()!=EXPECTED:
        raise ValueError('Original new-H audit runner changed')
    edits=[
        ("    parser.add_argument('--prepare-only', action='store_true')",
         "    parser.add_argument('--prepare-only', action='store_true')\n"
         "    parser.add_argument('--cache-directory', type=Path, required=True)\n"
         "    parser.add_argument('--seed-prefix', type=Path, required=True)\n"
         "    parser.add_argument('--initial-seed', type=Path)\n"
         "    parser.add_argument('--diagnostic-complete-evaluate', action='store_true')"),
        ("    cfg['initialCheckpoint'] = str(args.accepted_tail.resolve())",
         "    cfg['initialCheckpoint'] = str((args.initial_seed or args.accepted_tail).resolve())\n"
         "    seed_input=None\n"
         "    if args.initial_seed:\n"
         "        seed_input=read(args.initial_seed)\n"
         "        checkpoint=seed_input.get('checkpoint',seed_input)\n"
         "        if not checkpoint.get('exactInitialSeed'):\n"
         "            raise ValueError('The explicit initial seed has no exact binary marker')\n"
         "        if checkpoint['cutHeight'] != binding['complete_warm_H']:\n"
         "            raise ValueError('The explicit seed belongs to another complete H')\n"
         "        if seed_input.get('status') != 'initial-warm-only':\n"
         "            raise ValueError('An initial seed cannot be relabelled as an accepted trial')"),
        ("        'tail_resumable_engine.mjs', 'numerical-tail-slope-jacobian.mjs')",
         "        'tail_resumable_engine.mjs', 'numerical-tail-slope-jacobian.mjs',\n"
         "        'strong_cached_target_tail_audit.py','strong_exact_stage_tail_client.py',\n"
         "        'strong_exact_stage_tail_worker.mjs','strong_exact_stage_engine.mjs',\n"
         "        'strong_exact_stage_flow_store.mjs','strong_exact_stage_seed.mjs',\n"
         "        'strong_exact_stage_evaluation_check.mjs')"),
        ('    plan = dict(scope=__doc__,source_sha256=hashes,endpoint_binding=binding,',
         '    if args.initial_seed: hashes[str(args.initial_seed)]=sha(args.initial_seed)\n'
         '    plan = dict(scope=__doc__,stage_persistence_adapter=STAGE_SOURCE_TRANSFORM,\n'
         '        diagnostic_complete_evaluate=bool(args.diagnostic_complete_evaluate),\n'
         '        cache_directory=str(args.cache_directory.resolve()),seed_prefix=str(args.seed_prefix.resolve()),\n'
         '        initial_seed=None if args.initial_seed is None else str(args.initial_seed),\n'
         '        source_sha256=hashes,endpoint_binding=binding,'),
        ('        exact_same_H_raw_shortcut_will_not_apply=True,',
         '        exact_same_H_raw_shortcut_will_not_apply=(args.initial_seed is None),'),
        ('    from strong_exact_raw_tail_client import WeightedTailPort',
         "    os.environ['VISIBLE_FLEX_EXACT_STAGE_CACHE']=str(args.cache_directory.resolve())\n"
         "    os.environ['VISIBLE_FLEX_EXACT_STAGE_SEED_PREFIX']=str(args.seed_prefix.resolve())\n"
         '    from strong_exact_stage_tail_client import WeightedTailPort'),
        ("        response=tail.solve(binding['complete_warm_H'],jacobian=True,audit=True)",
         "        if args.diagnostic_complete_evaluate:\n"
         "            request=dict(height=binding['complete_warm_H'],jacobian=True,audit=True,exactStageDiagnostic=True)\n"
         "            tail.proc.stdin.write(json.dumps(request)+'\\n');tail.proc.stdin.flush()\n"
         "            line=tail.proc.stdout.readline()\n"
         "            if not line: raise RuntimeError('Exact-stage diagnostic worker stopped')\n"
         "            result=json.loads(line)\n"
         "            check=result.get('exactStageDiagnostic',{})\n"
         "            if not check.get('passed') or check.get('nonlinearSolution') or check.get('stagesCompared')!=tail.ready['parameters']['depth']:\n"
         "                raise ValueError('The complete actual stage-equivalence check failed: '+repr(result))\n"
         "            file('-diagnostic.json').write_text(json.dumps(result,indent=2)+'\\n')\n"
         "            report.update(status='diagnostic-complete',tail_converged=False,\n"
         "                original_complete_evaluate_bitwise_equal=True,diagnostic=result,\n"
         "                no_nonlinear_solve_or_final_audit_performed=True)\n"
         "            event(dict(event='complete_actual_stage_equivalence_passed',\n"
         "                stages=check['stagesCompared'],cache_identity=check['cacheIdentitySHA'],\n"
         "                initial_seed=result['exactInitialSeed'],prefix_accepted=False,tail_converged=False))\n"
         "            return\n"
         "        response=tail.solve(binding['complete_warm_H'],jacobian=True,audit=True)")]
    source=original
    for before,after in edits:
        if source.count(before)!=1:
            raise ValueError('Target-H stage-adapter anchor is not unique: '+repr(before))
        source=source.replace(before,after,1)
    ast.parse(source,filename='<explicit-cached-target-tail-audit>')
    record=dict(scope=__doc__,original_runner_sha256=EXPECTED,
        entry_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        transformed_source_sha256=hashlib.sha256(source.encode()).hexdigest(),
        replacements=[dict(before=a,after=b,count=1) for a,b in edits],
        complete_target_H_and_physical_source_guards_preserved=True,
        original_solve_full_Jacobian_and_audit_path_unchanged_for_normal_requests=True,
        diagnostic_request_never_an_accepted_nonlinear_response=True)
    return source,record


def main():
    source,record=build_source()
    namespace=dict(__file__=str(TEMPLATE),__name__='strong_cached_target_tail_source',
        STAGE_SOURCE_TRANSFORM=record)
    exec(compile(source,'<explicit-cached-target-tail-audit>','exec'),namespace)
    namespace['main']()


if __name__=='__main__':main()
