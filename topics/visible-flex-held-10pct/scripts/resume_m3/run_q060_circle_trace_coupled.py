#!/usr/bin/env python3
"""One reviewed q060-to-circle M8 actual coupled design; no parameter search.

--prepare writes a new immutable entry plan and source excerpts only. --run-plan
is the separate real solve. The frozen initial-state function is reused up to
the first collocation diagnostic, where it returns its existing arrays instead.
Their original y/p/H hashes must match before the original BVP can run.

The original actual-tail outer loop and postprocessing are retained. Its new-H
requests additionally request the existing complete audit. Only the first,
bitwise-identical H reuses the bound original actual response in the original
client cache. Raw inner entry/return states and their actual DN anchors are
saved before any later native tail, physical export or audit can fail.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse
import ast
import copy
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import traceback
import numpy as np

HERE=Path(__file__).resolve().parent
WORK=HERE.parents[4]
INITIALIZER=HERE/'q060_circle_trace_design.py'
INITIALIZER_SHA='2d9054efe56f8c0374b4cf12708a162de87e8857f90489d9c6674085f859b92e'
INITIAL_PLAN=WORK/'m3_work/q060-circle-trace-design-plan.json'
INITIAL_PLAN_SHA='ce2533b9bb0342fdcb6a7c81560281e8ef47ace3798e0e9e79fc1b44a176d1fc'
INITIAL_OUTPUT=WORK/'m3_work/q060-circle-trace-initializer-v1/initializer.json'
INITIAL_OUTPUT_SHA='974ee6c90a142e983e91acfa8cd86bdda6aaa8ff9f7b7a33823480aad2a78538'
INITIAL_TERMINAL=HERE/'q060_circle_trace_initializer_terminal.json'
INITIAL_TERMINAL_SHA='8c478f12c2472a3df75017613e606adf801282a7d5f413aec48e14705bc5aa75'
COUPLER_SHA='37defb33c031fd967ab0e06e086da56f2d67e30dd88bbbcb8e5e13201476511a'
TRACE=HERE.parent/'resume_n4/trace_domain_newton.py'
OBSERVER=HERE.parent/'resume_n4/observe_command_live.py'
SPARSE=WORK/'publication/topics/visible-flex-held-10pct/scripts/nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py'
SPARSE_SHA='a52567b2bfaded2fa9271a08f3cd969dc0291261f22cf2847c83234d93462fa5'
KIND='exact_m3_circle_trace_replacement_integral'
CONTROL_PATH='circle-trace-replace-last-two-v1'


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def ref(path):return dict(path=str(Path(path).resolve()),sha256=sha(path))
def load(path):
    path=Path(path);raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw)
def payload_sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()
def binary_sha(value):return hashlib.sha256(np.asarray(value,dtype='float64').tobytes()).hexdigest()
def write_json(path,value):
    with Path(path).open('x') as stream:json.dump(value,stream,indent=2,allow_nan=False);stream.write('\n')
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path);obj=importlib.util.module_from_spec(spec)
    sys.modules[name]=obj;spec.loader.exec_module(obj);return obj
def check_sources(sources):
    for path,expected in sources.items():
        if sha(path)!=expected:raise ValueError('Changed bound source/input: '+path)
def function_text(path,name):
    text=Path(path).read_text();node=next(n for n in ast.parse(text).body if isinstance(n,ast.FunctionDef) and n.name==name)
    return ''.join(text.splitlines(keepends=True)[node.lineno-1:node.end_lineno])+'\n'
def replace_once(text,old,new):
    if text.count(old)!=1:raise ValueError('The single reviewed source anchor changed: '+old[:100])
    return text.replace(old,new,1)


def derived_functions(coupler):
    initial=function_text(INITIALIZER,'evaluate_initializer')
    marker='        h=np.diff(t);col,middle,rhs,rhs_middle=_bvp.collocation_fun(obj.fun,y,par,t,h)'
    initial=replace_once(initial,marker,
        "        bound.check_sources()\n"
        "        return dict(obj=obj,x=t,y=y,p=par,env=env,core=core,flow=f,native=native,\n"
        "                    H=H,H0=H0,result=result,settings=settings)\n"+marker)
    outer=function_text(coupler,'solve_with_actual_tail')
    outer=replace_once(outer,'actual=tail.solve(candidate,jacobian=True,audit=False)',
                            'actual=tail.solve(candidate,jacobian=True,audit=True)')
    main=function_text(coupler,'main')
    start=main.index('    _,Base=adaptive.build_classes(chart)')
    end=main.index('    tail=None;begin=time.time();',start)
    old=main[start:end]
    main=replace_once(main,old,'    o,x,y,par,restart_info=OWNED.start_values(a,cfg,chart,port,tcfg)\n')
    tail_line="        tail=active_client.WeightedTailPort(a.tail_config,a.source_root,a.out_prefix.with_name(a.out_prefix.name+'_tail'),node_heap=a.node_heap);o.tail=tail"
    main=replace_once(main,tail_line,tail_line+'\n        OWNED.prime_original_cache(tail,H=o.bridge.sigma*o.q*y[o.iz:,-1])')
    main=replace_once(main,"        install();print(json.dumps(dict(event='start_coupled'",
        "        install();OWNED.install_trace();print(json.dumps(dict(event='start_coupled'")
    marker="        out['dn_solver']='outer_actual_inner_affine'if a.lagged_tail else'actual_dn_at_every_query';out['actual_outer_checks']=outer_checks"
    main=replace_once(main,marker,"        OWNED.decorate_checkpoint(out,o,sol)\n"+marker)
    old="    except Exception as exc:summary.update(error=repr(exc),tail_calls=tail.calls if tail else 0);print(json.dumps(dict(event='failure',error=repr(exc))),flush=True)"
    main=replace_once(main,old,"    except Exception as exc:OWNED.failure(exc);summary.update(error=repr(exc),tail_calls=tail.calls if tail else 0);print(json.dumps(dict(event='failure',error=repr(exc))),flush=True)")
    main=replace_once(main,'        if tail:tail.close()',
        '        if tail:tail.close()\n        OWNED.observe_worker_return(tail)')
    texts={'initializer-excerpt.py':initial,'outer-excerpt.py':outer,'main-excerpt.py':main}
    for name,text in texts.items():compile(text,name,'exec')
    return texts


def prepare(directory):
    fixed={str(INITIALIZER):INITIALIZER_SHA,str(INITIAL_PLAN):INITIAL_PLAN_SHA,
           str(INITIAL_OUTPUT):INITIAL_OUTPUT_SHA,str(INITIAL_TERMINAL):INITIAL_TERMINAL_SHA,
           str(SPARSE):SPARSE_SHA}
    check_sources(fixed)
    oldplan=load(INITIAL_PLAN);terminal=load(INITIAL_TERMINAL);probe=load(INITIAL_OUTPUT)
    if probe['plan']['identity_sha256']!=oldplan['identity_sha256']:raise ValueError('Initializer plan mismatch')
    design=oldplan['design'];binding=load(design['old_reference_binding']['path'])
    source=Path(binding['source_topic']);coupler=source/'scripts/db6f-prefix-coupled.py'
    if sha(coupler)!=COUPLER_SHA:raise ValueError('Original coupler changed')
    anchor=load(design['actual_affine_tail_anchor']['path']);config=copy.deepcopy(anchor['config'])
    if (design['new_q']['binary64'].hex()!='0x1.aad97acac1567p-5' or design['new_modes']!=8 or
        not terminal['finite_initializer']['full_H_binary64_equal']):raise ValueError('Only the one reviewed M8 design is allowed')
    expected_native=anchor['source_sha256']
    sources={**fixed,**probe['evaluation']['source_sha256']}
    for name,digest in expected_native.items():
        path=source/'scripts'/name
        if sha(path)!=digest:raise ValueError('Original native tail source mismatch: '+name)
        sources[str(path)]=digest
    # These transitive files are the existing source-root dependency snapshot.
    dependency_dir=source/'repro/source-root/topics/large-amplitude-twist-flex/scripts'
    dependencies=list(dependency_dir.glob('*.mjs'))+list(dependency_dir.glob('*.cjs'))
    dependencies += [source/'scripts/closing_tail_sources.mjs',source/'notes/closing_tail_dependency_blobs.json',
                     dependency_dir/'f6curve_domain_newton.py',dependency_dir/'curve_stable_prefix_bvp.py',
                     Path(__file__).resolve(),TRACE,OBSERVER]
    sources.update({str(path.resolve()):sha(path) for path in dependencies})
    check_sources(sources)
    directory=Path(directory).resolve();directory.mkdir(parents=True,exist_ok=False)
    source_files={}
    for name,text in derived_functions(coupler).items():
        path=directory/name
        with path.open('x') as stream:stream.write(text)
        source_files[name]=ref(path)
    profile=directory/'profile.json';tcfg=directory/'tail-config.json';out=directory/'seed'
    write_json(profile,design['physical_profile'])
    config['initialCheckpoint']=design['actual_affine_tail_anchor']['path']
    config['traceFile']=str(directory/'tail-worker.jsonl')
    changed=sorted(k for k in set(config)|set(anchor['config']) if config.get(k)!=anchor['config'].get(k))
    if changed!=['initialCheckpoint','traceFile']:raise ValueError('Unexpected tail configuration change')
    write_json(tcfg,config)
    args=['--source-root',str(source/'repro/source-root'),'--profile',str(profile),
          '--chart',design['original_chart']['path'],'--linear-port',design['physical_port']['path'],
          '--tail-config',str(tcfg),'--out-prefix',str(out),'--restart',design['old_checkpoint']['path'],
          '--amplitude',repr(design['new_q']['binary64']),'--warp-reference','0.06',
          '--modes','8','--angular','256','--audit-angular','512','--nodes','257',
          '--max-nodes','6000','--tol','1e-6','--bc-tol','1e-7','--physical-bc-tol','2e-9',
          '--node-heap','3072','--warmup-scales','--lagged-tail']
    plan=dict(scope=__doc__,runner=ref(__file__),initial_plan=ref(INITIAL_PLAN),
        completed_initializer=ref(INITIAL_OUTPUT),completed_initializer_terminal=ref(INITIAL_TERMINAL),
        design_identity_sha256=oldplan['identity_sha256'],design=design,source_sha256=sources,
        original_coupler=ref(coupler),derived_source_files=source_files,profile=ref(profile),tail_config=ref(tcfg),
        changed_tail_configuration_keys=changed,native_tail_source_sha256=expected_native,
        initial_hashes={k:terminal['finite_initializer'][k] for k in
            ('state_binary64_sha256','parameter_binary64_sha256','full_H_binary64_sha256')},
        initial_parameter_scales=terminal['actual_core']['parameter_scales'],
        initial_physical_controls=terminal['actual_core']['physical_controls'],
        original_main_arguments=args,output_prefix=str(out),
        environment=dict(VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(SPARSE),VISIBLE_FLEX_SPARSE_PYTHON=sys.executable),
        outer_budget=list(range(8)),fixed_metric=False,new_initial_p0=0.,warmup_scales=[],
        starting_actual_anchor=design['actual_affine_tail_anchor'],
        first_same_H_policy='Prime original cache with the verified original actual full-Jac/audit response; no new solve or fabricated response is recorded.',
        subsequent_H_policy='Original solve_with_actual_tail with candidate audit=True; original native solve/Jac/audit and original BC check, then next affine inner if needed.',
        initializer_rebuild_scope='Necessary creation of unstored arrays via the frozen function, stopping before the diagnostic collocation/RMS; y,p,H hashes and physical controls must match.',
        raw_recovery_scope='Before every inner call save its inputs and actual DN anchor; immediately after every return save raw x,y,p,cubic x/c/axis/extrapolate, full RMS/message/status, before any later actual tail or audit.',
        parameter_scope='Fixed q; physical c=pscale*p[1:], last two d/dt=T and d/du=U via the existing analytic integral-core chain. fixed=False p0 only changes delta/chart, initially zero on the final original frozen profile.',
        metadata_only=True,BVP_solver_invoked=False,actual_tail_solver_invoked=False)
    plan['identity_sha256']=payload_sha(plan)
    path=directory/'launch-plan.json';write_json(path,plan)
    command=[sys.executable,str(Path(__file__).resolve()),'--run-plan',str(path)]
    observer=[sys.executable,str(OBSERVER),'--out',str(directory/'resource.json'),
              '--log',str(directory/'stdout.log'),'--',*command]
    write_json(directory/'launch-command.json',dict(plan=ref(path),command=command,observer_command=observer))
    print(json.dumps(dict(plan=ref(path),plan_identity_sha256=plan['identity_sha256'],metadata_only=True,
                         source_files=len(sources),observer_command=observer)),flush=True)


class RunContext:
    def __init__(self,plan_path):
        self.plan_path=Path(plan_path).resolve();self.plan=load(plan_path);self.out=Path(self.plan['output_prefix'])
        self.events=self.out.with_name('entry-events.jsonl');self.tail=None;self.inner_count=0
        if self.events.exists():raise FileExistsError('The planned real execution already began')
        check=copy.deepcopy(self.plan);identity=check.pop('identity_sha256')
        if payload_sha(check)!=identity:raise ValueError('Launch plan identity changed')
        self.check_sources()
        for key in ('profile','tail_config','initial_plan','completed_initializer','completed_initializer_terminal'):
            item=self.plan[key]
            if sha(item['path'])!=item['sha256']:raise ValueError('Changed launch input: '+key)
        for item in self.plan['derived_source_files'].values():
            if sha(item['path'])!=item['sha256']:raise ValueError('Changed derived source')
        os.environ.update(self.plan['environment'])
        self.event('entry_started',plan=ref(plan_path),command=[sys.executable,*sys.argv],
                   no_restart=True,no_warmup=True)

    def check_sources(self):check_sources(self.plan['source_sha256'])
    def event(self,event,**fields):
        row=dict(event=event,time_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),**fields)
        with self.events.open('a') as stream:stream.write(json.dumps(row,separators=(',',':'),allow_nan=False)+'\n')
        print(json.dumps(row,separators=(',',':'),allow_nan=False),flush=True)

    def reconstruct(self):
        init=module('q060_circle_bound_initializer',INITIALIZER)
        bound,anchor,design=init.bind_design(self.plan['design']['old_reference_binding']['path'])
        if design['identity_sha256']!=self.plan['design_identity_sha256']:raise ValueError('Frozen initializer identity changed')
        path=self.plan['derived_source_files']['initializer-excerpt.py']['path']
        exec(compile(Path(path).read_text(),path,'exec'),init.__dict__)
        rebuilt=init.evaluate_initializer(bound,anchor,design)
        if 'obj' not in rebuilt:raise RuntimeError('Original initializer reconstruction failed: '+repr(rebuilt))
        got=dict(state_binary64_sha256=binary_sha(rebuilt['y']),parameter_binary64_sha256=binary_sha(rebuilt['p']),
                 full_H_binary64_sha256=binary_sha(rebuilt['H']))
        if got!=self.plan['initial_hashes']:raise ValueError('Necessary initializer rebuild changed y/p/H')
        o=rebuilt['obj'];physical=rebuilt['p'][1:]*o.pscale
        if (binary_sha(o.pscale)!=binary_sha(self.plan['initial_parameter_scales']) or
            binary_sha(physical)!=binary_sha(self.plan['initial_physical_controls'])):
            raise ValueError('The original seven physical controls/scales changed')
        self.rebuilt=rebuilt;self.anchor=anchor;self.coupler=rebuilt['env'].coupler
        self.event('initializer_rebuilt',**got,native_reference_constructed=True,nodes=len(rebuilt['x']),
            q=float(o.q),p0=float(rebuilt['p'][0]),physical_controls=physical.tolist(),parameter_scales=o.pscale.tolist(),
            original_diagnostic_RMS_repeated=False,mean_height_reconstructed=False)

    def start_values(self,a,cfg,chart,port,tcfg):
        d=self.plan['design'];r=self.rebuilt;o=r['obj']
        if (payload_sha(cfg)!=d['physical_profile_payload_sha256'] or
            payload_sha(chart)!=d['chart_payload_sha256'] or a.fixed or a.modes!=8 or
            a.amplitude.hex()!=d['new_q']['binary64_hex'] or a.warp_reference!=.06 or
            not a.lagged_tail or a.warmup_scales):raise ValueError('Changed explicit coupled design')
        return o,r['x'],r['y'],r['p'],dict(method='frozen_q060_circle_trace_initializer_exact_hash_rebuild',
            completed_initializer=self.plan['completed_initializer'],initial_hashes=self.plan['initial_hashes'])

    def prime_original_cache(self,tail,H):
        if tail.sources!=self.plan['native_tail_source_sha256']:raise ValueError('Original native tail changed')
        if binary_sha(H)!=self.plan['initial_hashes']['full_H_binary64_sha256']:raise ValueError('Initial H changed')
        if binary_sha(H)!=binary_sha(self.anchor['request']['height']):raise ValueError('No exact same-H anchor')
        self.tail=tail;tail.cache_key=np.asarray(H,float).copy();tail.cache_value=copy.deepcopy(self.anchor['response'])
        self.event('original_actual_cache_primed',actual_anchor=self.plan['starting_actual_anchor'],
                   native_calls=tail.calls,no_native_request_claim=True,ready=tail.ready)

    def install_trace(self):module('q060_circle_trace_newton_observer',TRACE).install(self.out.with_name('domain-newton.jsonl'))
    def failure(self,error):self.event('original_main_exception',error=repr(error),traceback=traceback.format_exc())
    def observe_worker_return(self,tail):
        self.event('worker_close_observed',native_calls=tail.calls if tail else 0,
            worker_returncode=tail.proc.poll() if tail else None,
            scope='Observed process status only; a missing returncode is not a mathematical or memory diagnosis.')

    def inner_anchor(self,o):
        affine=o.tail
        if not isinstance(affine,self.coupler.AffineTailForInnerBVP):raise ValueError('Inner must use the original affine class')
        source=(Path(self.plan['starting_actual_anchor']['path']) if self.tail.calls==0 else
                self.tail.record_prefix.with_name(self.tail.record_prefix.name+f'_{self.tail.calls:04d}.json.gz'))
        actual=load(source)
        if (binary_sha(actual['request']['height'])!=binary_sha(affine.height) or
            payload_sha(actual['response'])!=payload_sha(affine.response) or
            actual['request']['jacobian'] is not True or actual['request']['audit'] is not True):
            raise ValueError('The current affine anchor is not the bound original full-Jac/audit response')
        return dict(actual_tail_record=ref(source),height=affine.height.tolist(),
            height_binary64_sha256=binary_sha(affine.height),response_payload_sha256=payload_sha(affine.response),
            tail_native_calls=self.tail.calls)

    def save_raw(self,tag,data,anchor):
        path=self.out.with_name(tag+'.json.gz')
        encoded=(json.dumps(data,separators=(',',':'),allow_nan=False)+'\n').encode()
        with path.open('xb') as stream:stream.write(gzip.compress(encoded,mtime=0))
        side=self.out.with_name(tag+'-dn-anchor.json')
        write_json(side,dict(plan=ref(self.plan_path),raw=ref(path),**anchor))
        self.event('raw_inner_saved',raw=ref(path),dn_anchor=ref(side),stage=data['stage'],inner=data['inner'])

    def observed_solve_bvp(self,fun,bc,x,y,p,**options):
        o=self.rebuilt['obj'];index=self.inner_count;self.inner_count+=1
        anchor=self.inner_anchor(o)
        provenance=dict(plan=ref(self.plan_path),inner=index,coordinate='Original normalized adaptive collocation chart',
            core_kind=KIND,core_control_path=CONTROL_PATH,core_round_settings=self.plan['design']['new_core_settings'],
            q_gauge=float(o.q),fixed_metric=False,base_frozen_profile=self.plan['design']['physical_profile'],
            chart=self.plan['design']['original_chart'],parameter_scales=o.pscale.tolist(),
            note='Raw initial/returned state, not an accepted physical C2 checkpoint; no mean-height trajectory is silently added.')
        self.save_raw(f'inner-{index:02d}-entry',dict(**provenance,stage='before_original_solve_bvp',
            x=np.asarray(x).tolist(),y=np.asarray(y).tolist(),p=np.asarray(p).tolist(),cubic_available=False),anchor)
        try:sol=self.original_solve_bvp(fun,bc,x,y,p,**options)
        except BaseException as exc:
            self.event('inner_raised_before_return',inner=index,error=repr(exc),traceback=traceback.format_exc());raise
        raw=dict(**provenance,stage='immediately_after_original_solve_bvp',x=sol.x.tolist(),y=sol.y.tolist(),p=sol.p.tolist(),
            cubic_available=sol.sol is not None,solver_success=bool(sol.success),status=int(sol.status),
            message=sol.message,niter=int(sol.niter),rms_residuals=sol.rms_residuals.tolist(),
            original_physical_controls=(sol.p[1:]*o.pscale).tolist(),
            candidate_cut_height=(o.bridge.sigma*o.q*sol.y[o.iz:,-1]).tolist())
        if sol.sol is not None:raw['raw_cubic']=dict(x=sol.sol.x.tolist(),c=sol.sol.c.tolist(),axis=int(sol.sol.axis),extrapolate=bool(sol.sol.extrapolate))
        self.save_raw(f'inner-{index:02d}-returned',raw,anchor)
        return sol

    def decorate_checkpoint(self,out,o,sol):
        out['config']['core_kind']=KIND
        out.update(core_kind=KIND,core_control_path=CONTROL_PATH,
            core_round_settings=copy.deepcopy(self.plan['design']['new_core_settings']),core_projection_order_J=o.M,
            core_round_sources=self.plan['source_sha256'],physical_controls=(sol.p[1:]*o.pscale).tolist(),
            core_definition_provenance=self.rebuilt['result']['core_definition_provenance'],
            parameter_semantics='actual_primary_amplitude is the base q, not the true primary support moment q*P; fixed=False p0 changes only delta from the final original frozen profile.',
            circle_trace_entry_plan=ref(self.plan_path),initial_rebuild_hashes=self.plan['initial_hashes'],
            original_actual_start_anchor=self.plan['starting_actual_anchor'],raw_inner_records_saved=self.inner_count)


def run(plan_path):
    ctx=RunContext(plan_path);began=time.monotonic();terminal=dict(original_main_returned=False)
    old_argv=sys.argv[:]
    try:
        ctx.reconstruct();c=ctx.coupler;c.OWNED=ctx
        ctx.original_solve_bvp=c.solve_bvp;c.solve_bvp=ctx.observed_solve_bvp
        for name in ('outer-excerpt.py','main-excerpt.py'):
            path=ctx.plan['derived_source_files'][name]['path']
            exec(compile(Path(path).read_text(),path,'exec'),c.__dict__)
        sys.argv=[str(Path(__file__).resolve()),*ctx.plan['original_main_arguments']]
        c.main();terminal['original_main_returned']=True
    except BaseException as exc:
        terminal.update(error=repr(exc),traceback=traceback.format_exc());raise
    finally:
        sys.argv=old_argv;ctx.check_sources()
        summary=ctx.out.with_name(ctx.out.name+'-summary.json')
        if summary.is_file():
            value=load(summary);terminal.update(original_summary=ref(summary),
                original_solver_success=value.get('solver_success'),original_error=value.get('error'))
        terminal.update(seconds=time.monotonic()-began,raw_inner_calls=ctx.inner_count,
            actual_tail_calls=ctx.tail.calls if ctx.tail else 0,
            observed_worker_returncode=ctx.tail.proc.poll() if ctx.tail else None)
        write_json(ctx.out.with_name('runner-terminal.json'),terminal)
        ctx.event('runner_terminal',**terminal)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    choice=parser.add_mutually_exclusive_group(required=True)
    choice.add_argument('--prepare',type=Path);choice.add_argument('--run-plan',type=Path)
    args=parser.parse_args()
    if args.prepare is not None:prepare(args.prepare)
    else:run(args.run_plan)


if __name__=='__main__':main()
