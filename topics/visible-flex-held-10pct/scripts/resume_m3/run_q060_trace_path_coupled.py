#!/usr/bin/env python3
"""One actual lambda=.02 finite-path solve from the stored complete initializer.

Use the unchanged original main/outer excerpts and the already reviewed five-
point domain guard. Read existing t/y/p directly; do not repeat projection or
initial RMS. Original complete raw Newton/inner snapshots, true changed-H tail,
eight-outer budget, physical export, mean integration and audits remain active.
Only model construction, starting-array loading and truthful path metadata are
new. This is a new physical path design, not fixed-g refinement.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse
import copy
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np

HERE=Path(__file__).resolve().parent
WORK=HERE.parents[4]
PARENT=HERE/'run_q060_circle_trace_coupled.py'
PARENT_SHA='1204d93ce144efec9d61d34de7af189e4c597d3c1bf85090a1f7bcbae7c020f3'
GUARD=HERE/'m3_lobatto_domain_guard.py'
GUARD_SHA='8a15397acf3f0007ef5341373266e25bd8e383fb0a0cb32dc15a9f53adf68c31'
ENTRY=WORK/'m3_work/q060-circle-trace-path-entry-v1'
ENTRY_PLAN_SHA='945259b830d5d4a129cbe86068a6f72a2940f5cba2265224584cc8ac192a785f'
ENTRY_OUTPUT_SHA='7e39adda827887d715188f0ef263136316e8dcaa7d286abe13c44c5ee1fa0444'
ENTRY_ARRAY_SHA='1f882f0004ad58817b60245a363a9e773322b8bc8620179d36f9b6ce16a5e142'
ENTRY_TERMINAL=HERE/'q060_trace_path_entry_terminal.json'
ENTRY_TERMINAL_SHA='58cbed40e796100e9fc49efec1e8f69eeff13ca63cd7d4317f2de0651dc23b20'
OLD_LAUNCH=WORK/'m3_work/q060-circle-trace-lobatto-guard-v1/lobatto-launch-plan.json'
OLD_LAUNCH_SHA='da2c3d945ac45fcb04dc456c7e00283fb1c8b9bdbe4d2fe5fb5d3c8687c2374b'
KIND='exact_m3_finite_circle_trace_path_partial_lift'
CONTROL_PATH='finite-cosine-trace-synchronous-lift-v1'
LAMBDA=.02
QSEED=.059818741459951905


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path);obj=importlib.util.module_from_spec(spec)
    sys.modules[name]=obj;spec.loader.exec_module(obj);return obj


parent=module('q060_path_original_coupled_runner',PARENT)
if parent.sha(PARENT)!=PARENT_SHA or parent.sha(GUARD)!=GUARD_SHA:
    raise ValueError('The reviewed original runner or five-point guard changed')
guard=module('q060_path_original_lobatto_guard',GUARD)


def prepare(directory):
    fixed={str(ENTRY/'launch-plan.json'):ENTRY_PLAN_SHA,str(ENTRY/'entry.json'):ENTRY_OUTPUT_SHA,
        str(ENTRY/'entry-arrays.npz'):ENTRY_ARRAY_SHA,str(ENTRY_TERMINAL):ENTRY_TERMINAL_SHA,
        str(OLD_LAUNCH):OLD_LAUNCH_SHA,str(PARENT):PARENT_SHA,str(GUARD):GUARD_SHA,
        str(parent.SPARSE):parent.SPARSE_SHA}
    parent.check_sources(fixed)
    ep=parent.load(ENTRY/'launch-plan.json');result=parent.load(ENTRY/'entry.json')
    terminal=parent.load(ENTRY_TERMINAL);old=parent.load(OLD_LAUNCH)
    first=result['formed_first_entry'];definition=first['path_definition']
    if (not result['complete'] or not terminal['entry_complete'] or
        result['counters']!={'BVP_attempts':0,'native_tail_attempts':0} or
        first['lambda_value']!=LAMBDA or definition['defining_support_amplitude']!=QSEED or
        definition['numerical_gauge']!=.06 or not first['full_H_binary64_equal']):
        raise ValueError('Only the one completed lambda=.02 entry may be used')
    source=Path(ep['original_source_topic']);coupler=source/'scripts/db6f-prefix-coupled.py'
    if parent.sha(coupler)!=parent.COUPLER_SHA:raise ValueError('Original coupler changed')
    anchor=parent.load(ep['original_actual_anchor']['path'])
    if (anchor['request']['jacobian'] is not True or anchor['request']['audit'] is not True or
        not anchor['response']['converged'] or not np.isfinite(anchor['response']['residual']) or
        not anchor['response']['residual']<2e-9 or
        parent.binary_sha(anchor['request']['height'])!=first['full_H_binary64_sha256']):
        raise ValueError('The same full-H actual original Jacobian/audit anchor is required')
    sources={**ep['source_sha256'],**fixed,**old['source_sha256']}
    sources[str(Path(__file__).resolve())]=parent.sha(__file__)
    native_sources=anchor['source_sha256']
    for name,digest in native_sources.items():sources[str(source/'scripts'/name)]=digest
    parent.check_sources(sources)
    directory=Path(directory).resolve();directory.mkdir(parents=True,exist_ok=False)
    excerpts={}
    # The two numerical/control-flow excerpts are byte-for-byte those already
    # used by the original actual-tail + five-point-guard run.
    for name in ('outer-excerpt.py','main-excerpt.py'):
        oldref=old['derived_source_files'][name]
        if parent.sha(oldref['path'])!=oldref['sha256']:raise ValueError('Old main/outer excerpt changed')
        path=directory/name
        with path.open('x') as f:f.write(Path(oldref['path']).read_text())
        excerpts[name]=parent.ref(path)
    domain=Path(old['lobatto_guard']['original_domain_newton']['path'])
    recorded=guard.recording_newton_source(domain)
    oldrecord=old['lobatto_guard']['recording_newton_source']
    if recorded!=Path(oldrecord['path']).read_text() or parent.sha(oldrecord['path'])!=oldrecord['sha256']:
        raise ValueError('The observation-only original Newton excerpt changed')
    recording=directory/'recording-newton-excerpt.py'
    with recording.open('x') as f:f.write(recorded)
    excerpts[recording.name]=parent.ref(recording)
    binding=copy.deepcopy(old['lobatto_guard']);binding['recording_newton_source']=parent.ref(recording)
    profile=directory/'profile.json';tcfg=directory/'tail-config.json';out=directory/'seed'
    parent.write_json(profile,ep['physical_profile'])
    config=copy.deepcopy(anchor['config'])
    config['initialCheckpoint']=ep['original_actual_anchor']['path']
    config['traceFile']=str(directory/'tail-worker.jsonl')
    changed=sorted(k for k in set(config)|set(anchor['config']) if config.get(k)!=anchor['config'].get(k))
    if changed!=['initialCheckpoint','traceFile']:raise ValueError('Tail options changed beyond source/output paths')
    parent.write_json(tcfg,config)
    args=list(old['original_main_arguments'])
    replacements={'--profile':str(profile),'--tail-config':str(tcfg),'--out-prefix':str(out),
        '--amplitude':'0.06','--restart':ep['inputs']['physical_checkpoint']['path']}
    for flag,value in replacements.items():args[args.index(flag)+1]=value
    if args[args.index('--warp-reference')+1]!='0.06':raise ValueError('Original warp reference changed')
    active_settings={**ep['core_settings'],'homotopy':LAMBDA}
    design=dict(new_core_settings=active_settings,physical_profile=ep['physical_profile'],
        physical_profile_payload_sha256=ep['physical_profile_payload_sha256'],
        original_chart=ep['inputs']['original_chart'],chart_payload_sha256=ep['original_chart_payload_sha256'],
        original_reference_checkpoint=ep['inputs']['physical_checkpoint'],
        original_reference_binding=ep['inputs']['original_binding'],
        new_q=ep['support_amplitudes'][str(LAMBDA)],gauge_amplitude=.06,
        control_path=CONTROL_PATH,lambda_value=LAMBDA,lift_window=[.5,.9])
    plan=dict(scope=__doc__,runner=parent.ref(__file__),initial_plan=parent.ref(ENTRY/'launch-plan.json'),
        completed_initializer=parent.ref(ENTRY/'entry.json'),completed_initializer_terminal=parent.ref(ENTRY_TERMINAL),
        initial_arrays=parent.ref(ENTRY/'entry-arrays.npz'),previous_guard_plan=parent.ref(OLD_LAUNCH),
        design=design,source_sha256=sources,original_coupler=parent.ref(coupler),
        derived_source_files=excerpts,lobatto_guard=binding,profile=parent.ref(profile),tail_config=parent.ref(tcfg),
        changed_tail_configuration_keys=changed,native_tail_source_sha256=native_sources,
        initial_hashes={k:first[k] for k in ('state_binary64_sha256','parameter_binary64_sha256','full_H_binary64_sha256')},
        initial_parameter_scales=ep['original_parameter_scales'],
        initial_physical_controls=first['complete_physical_controls'],
        original_main_arguments=args,output_prefix=str(out),environment=old['environment'],
        outer_budget=list(range(8)),fixed_metric=False,new_initial_p0=0.,warmup_scales=[],
        starting_actual_anchor=ep['original_actual_anchor'],
        first_same_H_policy=old['first_same_H_policy'],subsequent_H_policy=old['subsequent_H_policy'],
        initializer_scope='Directly load the completed stored 25x271 state, t and all eight parameters. Build the same fixed-lambda model once; do not project or recompute initial RMS.',
        raw_recovery_scope=old['raw_recovery_scope'],
        snapshot_metadata_override='The inherited guard/inner observer contains legacy endpoint kind strings. This runner replaces only their saved kind/path and adds the true partial-path definition; all numerical arrays and algorithms are untouched.',
        parameter_scope='q_gauge=.06 and original pscales/warp stay fixed. q_support=.059818741459951905; full seven physical c=pscale*p[1:] enter C_j(lambda=.02). fixed=False p0 changes only delta from the recorded base profile. All lift-control derivatives carry lambda, inlet projection derivatives do not.',
        audit_scope='Unchanged original adaptive.audit and seam_audit use this actual partial-lift flow, its height_integral and complete mean velocity. No old mean trajectory is supplied.',
        subsequent_restart_scope='Do not apply the old ratio**j restart to this path. Exact reload uses path_base_profile plus all original p; rebasing to frozen_profile requires a declared material-coordinate transfer.',
        metadata_only=True,BVP_solver_invoked=False,actual_tail_solver_invoked=False)
    plan['identity_sha256']=parent.payload_sha(plan)
    path=directory/'launch-plan.json';parent.write_json(path,plan)
    command=[sys.executable,str(Path(__file__).resolve()),'--run-plan',str(path)]
    observer=[sys.executable,str(parent.OBSERVER),'--out',str(directory/'resource.json'),
              '--log',str(directory/'stdout.log'),'--',*command]
    parent.write_json(directory/'launch-command.json',dict(plan=parent.ref(path),command=command,observer_command=observer))
    print(json.dumps(dict(plan=parent.ref(path),identity_sha256=plan['identity_sha256'],
        metadata_only=True,source_files=len(sources),no_equation_evaluations=True)),flush=True)


class Context(parent.RunContext):
    def reconstruct(self):
        item=self.plan['initial_arrays']
        if parent.sha(item['path'])!=item['sha256']:raise ValueError('The completed initializer arrays changed')
        entry=module('q060_path_completed_entry_source',HERE/'prepare_q060_trace_path_entry.py')
        bound,_=entry.bind_old();native=bound.native_reference()
        from m3_circle_trace_path_model import CircleTracePathEnvironment
        env=CircleTracePathEnvironment(bound,native,entry.SETTINGS)
        obj=env.make(LAMBDA,QSEED)
        with np.load(item['path'],allow_pickle=False) as a:
            x,y,p,H=(a[k].copy() for k in ('initial_t','initial_y','initial_p','initial_H'))
        obj.initial(p)
        if p[0]!=0. or y.shape!=(25,271) or x.shape!=(271,):raise ValueError('Stored initial state changed')
        if (obj.q!=.06 or obj.support_amplitude!=QSEED or
            parent.binary_sha(obj.pscale)!=parent.binary_sha(self.plan['initial_parameter_scales']) or
            parent.binary_sha(p[1:]*obj.pscale)!=parent.binary_sha(self.plan['initial_physical_controls'])):
            raise ValueError('Original gauge, support seed or full physical controls changed')
        actualH=obj.bridge.sigma*obj.q*y[obj.iz:,-1]
        hashes=dict(state_binary64_sha256=parent.binary_sha(y),parameter_binary64_sha256=parent.binary_sha(p),
                    full_H_binary64_sha256=parent.binary_sha(actualH))
        if hashes!=self.plan['initial_hashes'] or parent.binary_sha(H)!=parent.binary_sha(actualH):
            raise ValueError('Stored initializer y/p/full-H identity changed')
        self.rebuilt=dict(obj=obj,x=x,y=y,p=p,env=env,native=native)
        self.anchor=parent.load(self.plan['starting_actual_anchor']['path']);self.coupler=env.coupler
        self.event('stored_initializer_loaded',**hashes,nodes=len(x),native_reference_constructed=True,
            q_gauge=obj.q,q_support=obj.support_amplitude,lambda_value=LAMBDA,
            physical_controls=(p[1:]*obj.pscale).tolist(),parameter_scales=obj.pscale.tolist(),
            no_projection_repeated=True,no_initial_RMS_repeated=True,no_mean_height_reconstructed=True)

    def start_values(self,a,cfg,chart,port,tcfg):
        d=self.plan['design'];r=self.rebuilt
        if (parent.payload_sha(cfg)!=d['physical_profile_payload_sha256'] or
            parent.payload_sha(chart)!=d['chart_payload_sha256'] or a.fixed or a.modes!=8 or
            a.amplitude!=.06 or a.warp_reference!=.06 or not a.lagged_tail or a.warmup_scales):
            raise ValueError('Changed explicit lambda=.02 coupled model')
        return r['obj'],r['x'],r['y'],r['p'],dict(method='completed_lambda002_entry_stored_arrays',
            completed_initializer=self.plan['completed_initializer'],initial_arrays=self.plan['initial_arrays'],
            initial_hashes=self.plan['initial_hashes'])

    def install_trace(self):
        super().install_trace()
        self.lobatto_hook=guard.install(self)

    def save_raw(self,tag,data,anchor):
        # Correct inherited endpoint-only provenance without touching any
        # state, RHS, cubic, guard, merit or control-flow quantity.
        obj=self.rebuilt['obj'];data=dict(data)
        data.update(core_kind=KIND,core_control_path=CONTROL_PATH,
            path_definition=copy.deepcopy(obj.path_definition),path_lambda=LAMBDA,
            q_gauge=float(obj.q),seed_support_amplitude=QSEED,partial_lift_strength=LAMBDA,
            lift_window=[.5,.9],path_base_profile=copy.deepcopy(obj.cfg))
        return super().save_raw(tag,data,anchor)

    def decorate_checkpoint(self,out,o,sol):
        if o.support_amplitude!=QSEED or o.q!=.06:raise ValueError('Final amplitude semantics changed')
        out['config']['core_kind']=KIND
        out.update(core_kind=KIND,core_control_path=CONTROL_PATH,
            core_round_settings=copy.deepcopy(self.plan['design']['new_core_settings']),
            core_projection_order_J=o.M,core_round_sources=self.plan['source_sha256'],
            physical_controls=(sol.p[1:]*o.pscale).tolist(),q_gauge=float(o.q),
            seed_support_amplitude=QSEED,defining_primary_factor=self.plan['design']['new_q'],
            path_definition=copy.deepcopy(o.path_definition),path_lambda=LAMBDA,
            partial_lift_strength=LAMBDA,lift_window=[.5,.9],path_base_profile=copy.deepcopy(o.cfg),
            original_cosine_reference=self.plan['design']['original_reference_checkpoint'],
            original_cosine_reference_binding=self.plan['design']['original_reference_binding'],
            core_definition_provenance=dict(scope='Definition and numerical representation only; final controls are the separate complete physical_controls field.',
                kind=KIND,control_path=CONTROL_PATH,lambda_value=LAMBDA,window=[.5,.9]),
            parameter_semantics='actual_primary_amplitude is q_support (the defining base seed), not q_gauge or the true primary moment q_support*P(lambda). Full seven c=pscale*p[1:]; p0 changes delta only from path_base_profile. Original frozen_profile already includes final p0.',
            path_coupled_entry_plan=parent.ref(self.plan_path),initial_array_hashes=self.plan['initial_hashes'],
            original_actual_start_anchor=self.plan['starting_actual_anchor'],raw_inner_records_saved=self.inner_count,
            loader_scope='Requires the finite-cosine-trace-synchronous-lift path loader. Neither legacy raw/full-lift loaders nor the old ratio**j restart apply.')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    choice=parser.add_mutually_exclusive_group(required=True)
    choice.add_argument('--prepare',type=Path);choice.add_argument('--run-plan',type=Path)
    args=parser.parse_args()
    if args.prepare is not None:prepare(args.prepare)
    else:
        parent.RunContext=Context
        parent.run(args.run_plan)


if __name__=='__main__':main()
