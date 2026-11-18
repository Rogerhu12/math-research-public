#!/usr/bin/env python3
"""Prepare one independent floor-binding source and plans; never compile/run.

The executed CPP/library remain immutable. The new CPP changes exactly one
validation expression, accepting the existing capsule.1 and production.05.
No numerical arithmetic, root rule, RK, implicit Jacobian or wire layout changes.
"""
import argparse
import ast
import datetime
import hashlib
import json
from pathlib import Path
import sys


OLD_CPP='916d0a948a15100f9bb68b255c2192460efe249c08a3559ea9fb800fbb59ac3f'
BEFORE='c.floor!=.1||'
AFTER='!(c.floor==.1||c.floor==.05)||'


def ref(path):
    p=Path(path).resolve()
    return dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest())


def load(path):
    return json.loads(Path(path).read_text())


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace',type=Path,required=True)
    parser.add_argument('--out-dir',type=Path,required=True)
    a=parser.parse_args();w=a.workspace.resolve();out=a.out_dir.resolve()
    topic=w/'math-research-public/topics/visible-flex-held-10pct'
    own=topic/'scripts/resume_n4_tail/native_extended'
    old_path=own/'frozen_flow.cpp';new_path=own/'frozen_flow_production.cpp'
    if ref(old_path)['sha256']!=OLD_CPP:
        raise ValueError('The executed original CPP changed')
    old=old_path.read_text()
    if old.count(BEFORE)!=1 or new_path.exists() or out.exists():
        raise ValueError('One fresh owned source/directory and one exact old validation occurrence required')
    builder=own/'compile_native_production_floor.py'
    probe=own/'probe_native_batch_floor_binding.py'
    for path in (Path(__file__),builder,probe):
        ast.parse(path.read_text(),filename=str(path))
    original_build_path=w/'n4_work/native-extended-build-v1/build.json'
    original_build=load(original_build_path)
    if original_build['sources']['cpp']!=ref(old_path):
        raise ValueError('Original build/source mismatch')
    for item in [original_build['compiler'],*original_build['sources'].values(),
                 original_build['library'],original_build['batch_executable']]:
        if ref(item['path'])!=item:
            raise ValueError('An original source/compiler/binary changed')
    cs_path=w/'n4_work/parts32-frozen-mp-baseline-v1/capsule-summary.json';cs=load(cs_path)
    ld_path=w/'n4_work/native-longdouble-pair-v1/readout-summary.json';ld=load(ld_path)
    new_path.write_text(old.replace(BEFORE,AFTER,1));out.mkdir(parents=True,exist_ok=False)
    files=dict(preparer=ref(__file__),compiler_driver=ref(builder),batch_probe=ref(probe),
        old_cpp=ref(old_path),production_cpp=ref(new_path),header=original_build['sources']['header'],
        harness=original_build['sources']['harness'],compiler=original_build['compiler'],
        original_build=ref(original_build_path),original_library=original_build['library'],
        original_batch=original_build['batch_executable'],capsule_summary=ref(cs_path),
        capsule_coefficients=cs['coefficients'],capsule_reference=cs['reference'],
        production_CP=cs['input'],LD_summary=ref(ld_path),LD_raw=ld['raw'],
        LD_resource=ref(w/'n4_work/native-longdouble-pair-v1/resource.json'),
        floor_discovery=ref(topic/'scripts/resume_n4_tail/native_production_floor_binding.json'),
        observer=ref(topic/'scripts/resume_n4/observe_command_live.py'))
    for item in files.values():
        if ref(item['path'])!=item:
            raise ValueError('Preparation source/input mismatch')
    binary=dict(library=str(out/'libfrozen_flow_production.so'),batch=str(out/'frozen_flow_production_batch'))
    prefix=[original_build['compiler']['path'],*original_build['flags']]
    commands=dict(library=[*prefix,'-fPIC','-shared',str(new_path),'-o',binary['library'],'-lm'],
                  batch=[*prefix,'-DVF_BUILD_MAIN',str(new_path),'-o',binary['batch'],'-lm'])
    plan_path=out/'plan.json';build_record=out/'build.json'
    compile_command=['python',str(builder),'--plan',str(plan_path)]
    batch_command=['python',str(probe),'--plan',str(plan_path),'--build-record',str(build_record)]
    observer=files['observer']['path']
    plan=dict(schema='n4-native-production-floor-v1',scope=__doc__,
        prepared_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        preparation_command=sys.argv,files=files,
        single_source_replacement=dict(before=BEFORE,after=AFTER,occurrences=1,
            same_source_outside_this_expression=True),
        production_floor=.05,retained_capsule_floor=.1,
        compile_commands=commands,compiled_outputs=binary,build_record=str(build_record),
        compile_driver_command=compile_command,
        compile_observer_command=['python',observer,'--log',str(out/'compile.log'),
            '--out',str(out/'compile-resource.json'),'--',*compile_command],
        batch_cases=[dict(label='capsule-point1',floor=.1),dict(label='production-point05',floor=.05)],
        batch_output_prefix=str(out/'fixture-batch'),batch_probe_command=batch_command,
        batch_observer_command=['python',observer,'--log',str(out/'batch-process.log'),
            '--out',str(out/'batch-resource.json'),'--',*batch_command],
        batch_execution_purpose='Two separate CLI calls, each exactly original stages43,38,175 with fullJac. Verify new binary/wire/floor configuration identity, not an algorithm scan. Match all42 and42x40 boundary64 outputs and available root aggregates to existing unchanged LD fullJac; time is observational only.',
        input_difference_gate='Between the two fixture batch inputs, only8 floor bytes and64 payload-token bytes may differ. The token binds payload bytes only; source/compiler/binary identity is checked separately.',
        first_phase='Only prepare sources/AST/hashes/plan. No compiler, library load, new flow or batch process has been invoked. Compilation and later numerical fixture-interface execution are separate explicitly approved phases.',
        existing_sources_or_binaries_changed=False,new_compilation=False,new_mathematical_execution=False,
        native_source_math_scope='Only validation accepts exactly the two original declared floor constants. The actual Engine domain tests still use supplied c.floor; no point-root equation/B/Newton iteration/halving/stop/fallback/RK/Jacobian/coefficients/transcendentals/boundary conversion/wire field changes.',
        production_hook_implemented=False,whole_tail_or_DN_invoked=False,
        next_Node_boundary='Owned lexical evaluate hook calls one whole-evaluate batch, keeps original residual/scales/left-target/far-Robin/correction/line search and audit. Inputs copy first40 with mean2 zero; only output pi rows divide c.portRatio. Original sparse correction/cut graph consume the first40 rows of full42x40. cutJets/FD/audit retain the original engine and original.05 floor.',
        cache_boundary='Keep original same-mu engine Map/identity. Cache frozen JS geometry, state trig and actual cusp grid once per fixed DN options, lazily after split-engine replacement. No persistent native coefficient cache is claimed by this self-contained batch protocol.',
        wire_cost=dict(header_bytes=42284,stage_bytes_formula='344+256*p+36*s atM20',
            ordinary_no_extra_cusp_steps_per_stage=16,ordinary_unique_points_per_stage=33,
            ordinary_2304_input_bytes=21626156,state_only_2304_output_bytes=940120,
            full_Jacobian_2304_output_bytes=31905880,
            qualifier='Exact fieldwise byte formulas for the stated ordinary-grid counts, not an observation of every actual cusp grid. Actual summed p/s require separate metadata at packing. Each complete evaluate starts one batch process, never one per stage.'))
    with plan_path.open('x') as stream:
        json.dump(plan,stream,indent=2,ensure_ascii=False,allow_nan=False);stream.write('\n')
    print(json.dumps(dict(plan=ref(plan_path),production_cpp=ref(new_path),
        new_compilation=False,new_mathematical_execution=False,source_difference_occurrences=1)),flush=True)


if __name__=='__main__':
    main()
