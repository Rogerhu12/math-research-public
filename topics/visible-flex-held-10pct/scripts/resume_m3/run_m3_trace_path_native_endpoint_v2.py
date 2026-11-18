#!/usr/bin/env python3
"""One literal M8 lambda=1 continuation with native marker bindings (v2).

The previous completed physical state must name the bound M8 native arithmetic
provider. Keep that actual provider for every new tail request; do not replace
its responses with legacy V8 responses. Prefix/model/initializer equations and
the original whole-source metric observer remain unchanged.

Retain the frozen 4e8 continuation's physical map transfer, every complete
parameter/control, original eight-outer method, five-point domain guard,
actual DN/Jacobian/audit and immediate raw/physical saves. Only scope this
entry to lambda=1 and bind the independently frozen metric observer.

Install the observer in the generated original main immediately before its
already-required metric audit. Pending-inner recovery copies that same main,
so it preserves this observation without repeating an accepted inner or an
old audit. The existing single FFT supplies component/location/bin metadata;
no second FFT, model call, metric formula, sampling or threshold is added.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import copy
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import traceback
import numpy as np

HERE = Path(__file__).resolve().parent
CLOSED = HERE.parent/'resume_closed'
WORK = HERE.parents[4]
sys.path.insert(0, str(CLOSED))
from m3_trace_path_prefix import bind_checkpoint, checked_file
from m3_literal_tail_provider_v2 import bind_provider, runtime_environment, install_client


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


PARENT = HERE/'run_q060_circle_trace_coupled.py'
PARENT_SHA = '1204d93ce144efec9d61d34de7af189e4c597d3c1bf85090a1f7bcbae7c020f3'
GUARD = HERE/'m3_lobatto_domain_guard.py'
GUARD_SHA = '8a15397acf3f0007ef5341373266e25bd8e383fb0a0cb32dc15a9f53adf68c31'
TEMPLATE = WORK/'m3_work/q060-circle-trace-path-coupled-lam002-v1/launch-plan.json'
TEMPLATE_SHA = '99b888b421ecaea72dbbafffca9811121ed8d663c62049c3ce03e54edc6b52be'
parent = module('trace_continuation_original_runner', PARENT)
parent.check_sources({str(PARENT): PARENT_SHA, str(GUARD): GUARD_SHA,
                      str(TEMPLATE): TEMPLATE_SHA})
guard = module('trace_continuation_original_fivepoint_guard', GUARD)
KIND = 'exact_m3_finite_circle_trace_path_partial_lift'
CONTROL_PATH = 'finite-cosine-trace-synchronous-lift-v1'
ORIGINAL_CONTINUATION = HERE/'run_m3_trace_path_continuation.py'
ORIGINAL_CONTINUATION_SHA = '4e8e4548536a0f0091910180247c1240ab49d045acbdf08a892f2809993eac57'
METRIC_OBSERVER = HERE/'metric_audit_observer_v2.py'
METRIC_OBSERVER_SHA = '47993e3856ebc7727b2a8e3bebfd0e9ee50f76a7261fbd3f687247c295bc8520'
ORIGINAL_OBSERVED_ENDPOINT = HERE/'run_m3_trace_path_endpoint_observed_v2.py'
ORIGINAL_OBSERVED_ENDPOINT_SHA = 'f9bf9a43560dba58d6356728156f9dce7e084d7962a7b0091c56568d8bf76933'
parent.check_sources({str(ORIGINAL_CONTINUATION): ORIGINAL_CONTINUATION_SHA,
                      str(METRIC_OBSERVER): METRIC_OBSERVER_SHA,
                      str(ORIGINAL_OBSERVED_ENDPOINT): ORIGINAL_OBSERVED_ENDPOINT_SHA})


def real_response(path, native_sources):
    record = parent.load(path)
    response = record['response']
    J = np.asarray(response['heightJetJacobian'], float)
    if (record['source_sha256'] != native_sources or
            record['request']['jacobian'] is not True or record['request']['audit'] is not True or
            response.get('converged') is not True or not math.isfinite(response['residual']) or
            not response['residual'] < record['config']['solveTolerance'] == 2e-9 or
            response.get('audit') is None or J.size != 208 or not np.all(np.isfinite(J)) or
            parent.binary_sha(record['request']['height']) != parent.binary_sha(response['checkpoint']['cutHeight'])):
        raise ValueError('Every reusable H needs its own genuine original full response')
    return record


def prepare(checkpoint, lam, directory):
    binding = bind_checkpoint(checkpoint)
    cp = binding.record
    lam = float(lam)
    if not cp['path_lambda'] < lam == 1.:
        raise ValueError('This independent entry is only the next literal lambda=1 endpoint')
    template = parent.load(TEMPLATE)
    stored_provider = cp['active_tail_arithmetic_provider']
    provider = bind_provider(checked_file(stored_provider['manifest']), stored_provider['manifest']['sha256'],
        stored_provider['historical_native_source_sha256'], cp['tail_config'])
    if provider != stored_provider:
        raise ValueError('The previous actual native arithmetic provider changed')
    if (cp['path_base_profile'] != template['design']['physical_profile'] or
            cp['gauge_amplitude'] != .06 or cp['warp_reference_q'] != .06 or
            cp['central_correction_scales'] != template['initial_parameter_scales']):
        raise ValueError('This path does not rebase delta, gauge, scales or warp')
    raw_ref = cp.get('accepted_raw_inner')
    side_ref = cp.get('accepted_raw_sidecar')
    if raw_ref is None:
        raw_ref = cp['saved_inner_resume']['raw_inner']
        side_ref = cp['saved_inner_resume']['raw_sidecar']
    raw = parent.load(checked_file(raw_ref))
    checked_file(side_ref)
    if (raw['solver_success'] is not True or
            parent.binary_sha(raw['p']) != parent.binary_sha(cp['parameters']) or
            len(raw['x']) != cp['nodes'] or np.asarray(raw['y']).shape != (25, cp['nodes']) or
            raw['path_lambda'] != cp['path_lambda']):
        raise ValueError('The genuine returned raw mesh/parameters must match the physical terminal')
    entry = module('trace_continuation_registered_scalar', HERE/'prepare_q060_trace_path_entry.py')
    old_entry = parent.load(template['initial_plan']['path'])
    qspec = entry.matched_amplitude(lam, old_entry['registered_P1_enclosure'], .06)
    records = {}
    for item in cp.get('recorded_actual_tail_lookup', {}).get('records', {}).values():
        r = item['original']
        checked_file(r)
        records[r['sha256']] = r
    records[binding.tail_record_sha256] = parent.ref(binding.tail_record)
    for r in records.values():
        real_response(r['path'], provider['native_tail_source_sha256'])
    sources = {**template['source_sha256'], **cp['core_round_sources'], **provider['source_sha256']}
    sources.update(cp.get('physical_postprocessing_source_sha256', {}))
    for file in (Path(__file__).resolve(), CLOSED/'m3_trace_path_prefix.py', PARENT, GUARD,
                 HERE/'prepare_q060_trace_path_entry.py', ORIGINAL_CONTINUATION, METRIC_OBSERVER,
                 ORIGINAL_OBSERVED_ENDPOINT, HERE/'m3_literal_tail_provider_v2.py'):
        sources[str(file)] = parent.sha(file)
    parent.check_sources(sources)
    directory = Path(directory).resolve()
    directory.mkdir(parents=True, exist_ok=False)
    derived = {}
    for name in ('outer-excerpt.py', 'recording-newton-excerpt.py'):
        old = checked_file(template['derived_source_files'][name])
        target = directory/name
        with target.open('x') as stream:
            stream.write(old.read_text())
        derived[name] = parent.ref(target)
    main = checked_file(template['derived_source_files']['main-excerpt.py']).read_text()
    # The original audit has already returned at this exact point. Save its
    # full result before the independent seam call can raise.
    marker = "        out['tail_seam']=o.seam_audit(physical);out['seconds']=time.time()-begin;out['tail_calls']=tail.calls;save_checkpoint(cp,out)"
    main = parent.replace_once(main, marker,
        "        OWNED.save_completed_prefix_audit(cp,out)\n"
        "        out['tail_seam']=o.seam_audit(physical);out['seconds']=time.time()-begin;out['tail_calls']=tail.calls;OWNED.decorate_tail_record_identity(out);save_checkpoint(cp,out)")
    audit_marker = "        cp=a.out_prefix.with_suffix('.json.gz');save_checkpoint(cp,out);out['summary']=adaptive.audit(o,physical,a.audit_angular)"
    audit_observed = "        cp=a.out_prefix.with_suffix('.json.gz');save_checkpoint(cp,out)\n" \
        "        from metric_audit_observer_v2 import install as install_original_metric_observer\n" \
        "        metric_observer_provenance=install_original_metric_observer(adaptive)\n" \
        "        OWNED.event('original_metric_observer_installed',**metric_observer_provenance)\n" \
        "        out['summary']=adaptive.audit(o,physical,a.audit_angular)"
    main = parent.replace_once(main,audit_marker,audit_observed)
    target = directory/'main-excerpt.py'
    compile(main, str(target), 'exec')
    with target.open('x') as stream:
        stream.write(main)
    derived[target.name] = parent.ref(target)
    lobatto = copy.deepcopy(template['lobatto_guard'])
    lobatto['recording_newton_source'] = derived['recording-newton-excerpt.py']
    profile = directory/'profile.json'
    parent.write_json(profile, cp['path_base_profile'])
    design = copy.deepcopy(template['design'])
    design.update(new_core_settings={**cp['core_round_settings'], 'homotopy': lam},
                  new_q=qspec, lambda_value=lam, physical_profile=cp['path_base_profile'],
                  physical_profile_payload_sha256=parent.payload_sha(cp['path_base_profile']))
    plan = dict(scope=__doc__, runner=parent.ref(__file__), source_sha256=sources,
        previous_physical_checkpoint=parent.ref(binding.checkpoint),
        previous_physical_coefficients=[parent.ref(binding.checkpoint.parent/r['file']) for r in cp['pp_coefficient_chunks']],
        previous_path_plan=parent.ref(binding.plan_path), previous_raw_inner=raw_ref,
        previous_raw_sidecar=side_ref, previous_lambda=cp['path_lambda'],
        previous_complete_metric=cp['summary']['metric_l1'],
        intermediate_anchor_scope='Original inner/actual BC/tail and complete finite audit required. A metric value above 1e-6 is retained explicitly; this is not a final completed solution.',
        template_plan=parent.ref(TEMPLATE), design=design, original_coupler=template['original_coupler'],
        derived_source_files=derived, lobatto_guard=lobatto, profile=parent.ref(profile),
        active_tail_provider=provider, native_tail_source_sha256=provider['native_tail_source_sha256'],
        original_main_arguments=template['original_main_arguments'],
        environment={**template['environment'], **runtime_environment(provider,directory)},
        full_initial_parameters=cp['parameters'], initial_parameter_scales=cp['central_correction_scales'],
        initial_physical_controls=cp['physical_controls'], available_actual_responses=list(records.values()),
        preferred_actual_response=parent.ref(binding.tail_record),
        original_raw_cut_H=raw['candidate_cut_height'],
        initializer_policy='Same normalized raw x and complete p; Y_old is the physical quintic at chart(x,p0), not raw.y. Add only the projected reference difference on the same basis, then the original shared C2 inlet repair. Do not re-encode or force H.',
        projection_angular=4096, repair_window=[.5,.9],
        mean_policy='No old mean is copied. The original actual new Flow.height_integral runs in full postprocessing.',
        original_gates=dict(max_nodes=6000,tol=1e-6,bc_tol=1e-7,physical_bc_tol=2e-9,
            rho_floor=1e-5,rho_grid_ceiling=32768,tail_tolerance=2e-9,outer_budget=list(range(8))),
        metric_observer=dict(source=parent.ref(METRIC_OBSERVER),
            original_continuation=parent.ref(ORIGINAL_CONTINUATION),
            installation_point='Generated original main, immediately before the original adaptive.audit; pending recovery retains the same excerpt.',
            preserved_single_original_FFT=True, additional_model_calls=0, additional_FFT_calls=0,
            original_samples_formulas_gates_unchanged=True,
            observation_scope='Finite existing audit E/F/G component peaks, radial samples and dominant signed FFT bins; not continuous bounds or causal attribution.'),
        original_newton_recording_preserved=True, metadata_only=True,
        input_initializer_recomputed=False, old_inner_recomputed=False,
        output_prefix=str(directory/'seed'))
    plan['identity_sha256'] = parent.payload_sha(plan)
    path = directory/'continuation-plan.json'
    parent.write_json(path, plan)
    command = [sys.executable, str(Path(__file__).resolve()), '--run-plan', str(path)]
    observer = [sys.executable, str(parent.OBSERVER), '--out', str(directory/'resource.json'),
                '--log', str(directory/'stdout.log'), '--', *command]
    parent.write_json(directory/'launch-command.json', dict(plan=parent.ref(path), command=command,
                                                           observer_command=observer))
    print(json.dumps(dict(plan=parent.ref(path), lambda_value=lam, q_support=qspec['q_binary64'],
                          source_files=len(sources), metadata_only=True)), flush=True)


def form_initializer(plan, plan_path):
    binding = bind_checkpoint(checked_file(plan['previous_physical_checkpoint']))
    old = binding.native_prefix()
    env = old.environment
    obj = env.make(plan['design']['lambda_value'], plan['design']['new_q']['q_binary64'])
    p = np.asarray(plan['full_initial_parameters'], float).copy()
    obj.initial(p)
    flow = obj.flow(float(p[0]))
    raw = parent.load(checked_file(plan['previous_raw_inner']))
    x = np.asarray(raw['x'], float)
    s, _ = obj.chart(x, float(p[0]))
    if (parent.binary_sha(s) != parent.binary_sha(old.polynomial.x) or
            parent.binary_sha(p) != parent.binary_sha(raw['p']) or
            obj.cfg != old.obj.cfg or obj.q != old.obj.q or obj.q != .06 or
            parent.binary_sha(obj.pscale) != parent.binary_sha(old.obj.pscale) or
            parent.binary_sha(p[1:]*obj.pscale) != parent.binary_sha(plan['initial_physical_controls']) or
            float(flow.end).hex() != float(old.flow.end).hex() or flow.warp_e != old.flow.warp_e):
        raise ValueError('The old normalized mesh, base+p0, all controls and actual chart must carry unchanged')
    oldY = old.polynomial(s)
    y = oldY.copy()
    N = plan['projection_angular']
    B = flow.basis(N)[0]
    reference_correction_max = 0.
    zero_reference_nodes = []
    for first in range(0, len(x), 24):
        sl = slice(first, first+24)
        og, ng = old.flow.geo(s[sl],N), flow.geo(s[sl],N)
        if parent.binary_sha(og['theta']) != parent.binary_sha(ng['theta']):
            raise ValueError('This continuation keeps the entire angular chart')
        delta = og['pos']-ng['pos']
        zero = np.all(delta == 0., axis=(1,2))
        correction = flow.project(delta, B)/obj.q
        reference_correction_max = max(reference_correction_max,float(np.max(np.abs(correction))))
        # At exactly zero reference difference retain the literal old values;
        # the old finite Fourier field itself is not projected a second time.
        y[:,sl] = oldY[:,sl]+correction
        indices = first+np.flatnonzero(zero)
        y[:,indices] = oldY[:,indices]
        zero_reference_nodes.extend(indices.tolist())
    inlet = obj.initial(p)-y[:,0]
    u = np.clip((s-.5*flow.prefix_end)/(.4*flow.prefix_end),0.,1.)
    weight = flow.profile(s)[0]*(1-u**3*(10-15*u+6*u*u))
    active = weight != 0.
    y[:,active] += inlet[:,None]*weight[None,active]
    H = obj.bridge.sigma*obj.q*y[obj.iz:,-1]
    old_physical_H = old.obj.bridge.sigma*old.obj.q*oldY[old.obj.iz:,-1]
    actual = {}
    for item in plan['available_actual_responses']:
        record = real_response(checked_file(item),plan['native_tail_source_sha256'])
        actual[np.asarray(record['request']['height'],dtype='<f8').tobytes()] = (item,record)
    selected = actual.get(np.asarray(H,dtype='<f8').tobytes())
    directory = Path(plan['output_prefix']).parent
    arrays = directory/'initializer-arrays.npz'
    with arrays.open('xb') as stream:
        np.savez_compressed(stream,initial_t=x,initial_s=s,initial_y=y,initial_p=p,initial_H=H,
                            inlet_correction=inlet)
    hashes = dict(state_binary64_sha256=parent.binary_sha(y),parameter_binary64_sha256=parent.binary_sha(p),
                  full_H_binary64_sha256=parent.binary_sha(H))
    record = dict(scope='Necessary new-lambda initial representation only. No original RMS, BVP, actual-tail or mean-height evaluation here.',
        preparation_plan=parent.ref(plan_path),previous_physical_checkpoint=plan['previous_physical_checkpoint'],
        previous_raw_inner=plan['previous_raw_inner'],lambda_value=plan['design']['lambda_value'],
        path_definition=obj.path_definition,arrays=parent.ref(arrays),initial_hashes=hashes,
        nodes=len(x),full_parameters=p.tolist(),physical_controls=(p[1:]*obj.pscale).tolist(),
        complete_physical_quintic_used=True,raw_node_values_used_for_state=False,
        original_raw_H=plan['original_raw_cut_H'],old_physical_H=old_physical_H.tolist(),new_H=H.tolist(),
        new_H_minus_old_physical_H=(H-old_physical_H).tolist(),
        new_H_byte_equal_old_physical=parent.binary_sha(H)==parent.binary_sha(old_physical_H),
        exact_actual_start_response=selected[0] if selected else None,
        unknown_H_policy='No substitution. The original worker must solve any H without a genuine byte-identical complete response.',
        maximum_projected_reference_correction=reference_correction_max,
        zero_reference_nodes=len(zero_reference_nodes),inlet_residual=float(np.max(np.abs(y[:,0]-obj.initial(p)))),
        numerical_core_guard=dict(rho_lower=float(obj._core.rho_lower),rho_sample=float(obj._core.rho_min_sample)),
        core_definition_primary_q=obj.support_amplitude,numerical_gauge=obj.q,
        no_amplitude_power_restart=True,old_mean_not_copied=True,initial_RMS_repeated=False,
        initializer_arrays_complete=True,solver_success_not_claimed=True)
    result = directory/'initializer.json'
    parent.write_json(result,record)
    return dict(obj=obj,x=x,y=y,p=p,env=env,old=old),actual,record,result


def runtime_plan(prepared, prepared_path, initial, initial_path):
    directory = Path(prepared['output_prefix']).parent
    anchor = initial['exact_actual_start_response'] or prepared['preferred_actual_response']
    actual = real_response(checked_file(anchor),prepared['native_tail_source_sha256'])
    config = copy.deepcopy(actual['config'])
    config['initialCheckpoint'] = anchor['path']
    config['traceFile'] = str(directory/'tail-worker.jsonl')
    cfgpath = directory/'tail-config.json'
    parent.write_json(cfgpath,config)
    args = list(prepared['original_main_arguments'])
    for flag,value in {'--profile':prepared['profile']['path'],'--tail-config':str(cfgpath),
        '--out-prefix':prepared['output_prefix'],'--restart':prepared['previous_physical_checkpoint']['path'],
        '--nodes':str(initial['nodes'])}.items():
        args[args.index(flag)+1] = value
    plan = dict(scope=__doc__,runner=parent.ref(__file__),initial_plan=parent.ref(prepared_path),
        completed_initializer=parent.ref(initial_path),completed_initializer_terminal=parent.ref(initial_path),
        initializer_terminal_scope='Completion of the necessary array-construction function only; no separate diagnostic or solver success is implied.',
        initial_arrays=initial['arrays'],design=prepared['design'],source_sha256=prepared['source_sha256'],
        original_coupler=prepared['original_coupler'],derived_source_files=prepared['derived_source_files'],
        lobatto_guard=prepared['lobatto_guard'],profile=prepared['profile'],tail_config=parent.ref(cfgpath),
        active_tail_provider=prepared['active_tail_provider'],
        native_tail_source_sha256=prepared['native_tail_source_sha256'],initial_hashes=initial['initial_hashes'],
        initial_parameter_scales=prepared['initial_parameter_scales'],initial_physical_controls=prepared['initial_physical_controls'],
        original_main_arguments=args,output_prefix=prepared['output_prefix'],environment=prepared['environment'],
        starting_actual_anchor=anchor,available_actual_responses=prepared['available_actual_responses'],
        initial_exact_cache_match=initial['exact_actual_start_response'] is not None,
        previous_physical_checkpoint=prepared['previous_physical_checkpoint'],
        previous_raw_inner=prepared['previous_raw_inner'],outer_budget=list(range(8)),fixed_metric=False,
        new_initial_p0=prepared['full_initial_parameters'][0],warmup_scales=[],
        audit_scope='Original new mean, metric and seam; immediately save every completed prefix audit.',
        metric_observer=prepared['metric_observer'],
        metadata_only=False,initializer_arrays_constructed_once=True,BVP_solver_invoked=False,actual_tail_solver_invoked=False)
    plan['identity_sha256'] = parent.payload_sha(plan)
    path = directory/'launch-plan.json'
    parent.write_json(path,plan)
    return path


class Context(parent.RunContext):
    def __init__(self,plan_path,rebuilt,actual):
        super().__init__(plan_path)
        self.rebuilt,self.actual_records = rebuilt,actual
        self.coupler = rebuilt['env'].coupler
        self.current_actual_record = None

    def reconstruct(self):
        r = self.rebuilt
        H = r['obj'].bridge.sigma*r['obj'].q*r['y'][r['obj'].iz:,-1]
        got = dict(state_binary64_sha256=parent.binary_sha(r['y']),parameter_binary64_sha256=parent.binary_sha(r['p']),
                   full_H_binary64_sha256=parent.binary_sha(H))
        if got != self.plan['initial_hashes']:
            raise ValueError('The once-constructed initializer changed before the original solve')
        self.event('new_lambda_initializer_available',**got,nodes=len(r['x']),
                   lambda_value=self.plan['design']['lambda_value'],no_initializer_rebuild=True,no_initial_RMS_probe=True)
        install_client(self,module)

    def start_values(self,a,cfg,chart,port,tcfg):
        d,r = self.plan['design'],self.rebuilt
        if (parent.payload_sha(cfg)!=d['physical_profile_payload_sha256'] or
                parent.payload_sha(chart)!=d['chart_payload_sha256'] or a.fixed or a.modes!=8 or
                a.amplitude!=.06 or a.warp_reference!=.06 or not a.lagged_tail or a.warmup_scales):
            raise ValueError('The declared same-gauge finite path changed')
        return r['obj'],r['x'],r['y'],r['p'],dict(method='saved_physical_quintic_plus_partial_reference_difference',
            previous_checkpoint=self.plan['previous_physical_checkpoint'],initializer=self.plan['completed_initializer'])

    def prime_original_cache(self,tail,H):
        if tail.sources!=self.plan['native_tail_source_sha256']:
            raise ValueError('Original tail source changed')
        self.tail=tail
        native=tail.solve
        def solve(height,jacobian=True,audit=False):
            h=np.asarray(height,dtype='<f8')
            key=h.tobytes()
            if h.shape!=(8,) or not np.all(np.isfinite(h)):
                raise ValueError('Invalid complete H')
            if key in self.actual_records:
                item,record=self.actual_records[key]
                self.current_actual_record=item
                tail.cache_key=h.copy();tail.cache_value=record['response']
                self.event('genuine_full_H_response_reused',record=item,H_binary64_sha256=parent.binary_sha(h),native_calls=tail.calls)
                return record['response']
            response=native(h,jacobian=True,audit=True)
            path=tail.record_prefix.with_name(tail.record_prefix.name+f'_{tail.calls:04d}.json.gz')
            record=real_response(path,self.plan['native_tail_source_sha256'])
            if parent.binary_sha(record['request']['height'])!=parent.binary_sha(h):
                raise ValueError('Original native response belongs to another H')
            item=parent.ref(path);self.actual_records[key]=(item,record);self.current_actual_record=item
            return response
        tail.solve=solve
        match=self.actual_records.get(np.asarray(H,dtype='<f8').tobytes())
        if match:
            item,record=match
            tail.cache_key=np.asarray(H,float).copy();tail.cache_value=record['response']
            self.current_actual_record=item
        self.event('original_actual_cache_installed',exact_initial_H_match=match is not None,
                   available_genuine_responses=len(self.actual_records),native_calls=0)

    def inner_anchor(self,o):
        affine=o.tail
        if not isinstance(affine,self.coupler.AffineTailForInnerBVP):
            raise ValueError('The original affine inner interface is required')
        item,record=self.actual_records[np.asarray(affine.height,dtype='<f8').tobytes()]
        if parent.payload_sha(record['response'])!=parent.payload_sha(affine.response):
            raise ValueError('Affine data differ from the genuine full response')
        return dict(actual_tail_record=item,height=affine.height.tolist(),
            height_binary64_sha256=parent.binary_sha(affine.height),
            response_payload_sha256=parent.payload_sha(affine.response),tail_native_calls=self.tail.calls)

    def install_trace(self):
        super().install_trace()
        self.lobatto_hook=guard.install(self)

    def save_raw(self,tag,data,anchor):
        obj=self.rebuilt['obj'];d=self.plan['design'];data=dict(data)
        data.update(core_kind=KIND,core_control_path=CONTROL_PATH,path_definition=copy.deepcopy(obj.path_definition),
            path_lambda=d['lambda_value'],q_gauge=obj.q,seed_support_amplitude=obj.seed_support_amplitude,
            partial_lift_strength=d['lambda_value'],lift_window=[.5,.9],path_base_profile=copy.deepcopy(obj.cfg))
        data['active_tail_arithmetic_provider']=self.plan['active_tail_provider']
        return super().save_raw(tag,data,anchor)

    def decorate_checkpoint(self,out,o,sol):
        d=self.plan['design'];lam=d['lambda_value'];q=d['new_q']['q_binary64']
        if o.q!=.06 or o.support_amplitude!=q:
            raise ValueError('Final gauge/support semantics changed')
        out['config']['core_kind']=KIND
        out.update(core_kind=KIND,core_control_path=CONTROL_PATH,core_round_settings=copy.deepcopy(d['new_core_settings']),
            core_projection_order_J=o.M,core_round_sources=self.plan['source_sha256'],
            physical_controls=(sol.p[1:]*o.pscale).tolist(),q_gauge=o.q,seed_support_amplitude=q,
            defining_primary_factor=d['new_q'],path_definition=copy.deepcopy(o.path_definition),path_lambda=lam,
            partial_lift_strength=lam,lift_window=[.5,.9],path_base_profile=copy.deepcopy(o.cfg),
            original_cosine_reference=d['original_reference_checkpoint'],original_cosine_reference_binding=d['original_reference_binding'],
            core_definition_provenance=dict(scope='Definition only; final controls are physical_controls.',kind=KIND,control_path=CONTROL_PATH,lambda_value=lam),
            parameter_semantics='Fixed .06 gauge/scales/warp; support q=.06/P(lambda). All seven c=pscale*p[1:]; full p0 changes delta from the original base exactly once.',
            path_coupled_entry_plan=parent.ref(self.plan_path),initial_array_hashes=self.plan['initial_hashes'],
            original_actual_start_anchor=self.plan['starting_actual_anchor'],raw_inner_records_saved=self.inner_count,
            previous_path_checkpoint=self.plan['previous_physical_checkpoint'],
            returned_raw_inner=parent.ref(self.out.with_name(f'inner-{self.inner_count-1:02d}-returned.json.gz')),
            returned_raw_sidecar=parent.ref(self.out.with_name(f'inner-{self.inner_count-1:02d}-returned-dn-anchor.json')),
            loader_scope='Use the finite trace-path physical reader; no generic amplitude-power restart.')
        out['active_tail_arithmetic_provider']=self.plan['active_tail_provider']
        out['tail_arithmetic_scope']='All actual tail responses in this run use the explicit native provider; original finite gates and prefix equations remain. No V8 bitwise or continuous error equivalence is asserted.'
        if sol.success:
            out['accepted_raw_inner']=out['returned_raw_inner']
            out['accepted_raw_sidecar']=out['returned_raw_sidecar']

    def decorate_tail_record_identity(self,out):
        if self.current_actual_record is None:
            return
        original=checked_file(self.current_actual_record)
        record=real_response(original,self.plan['native_tail_source_sha256'])
        if original.parent==self.out.parent:
            alias=original
        else:
            alias=self.out.with_name('reused-actual-tail-'+self.current_actual_record['sha256'][:16]+'.json.gz')
            if not alias.exists():
                with alias.open('xb') as stream:stream.write(original.read_bytes())
            if parent.sha(alias)!=parent.sha(original):
                raise ValueError('A reused original response alias changed bytes')
        out['tail_config']=copy.deepcopy(record['config'])
        out['active_worker_tail_config']=parent.load(self.plan['tail_config']['path'])
        out['actual_tail_record_provenance']=dict(record=parent.ref(alias),original_actual_record=self.current_actual_record,
            record_is_reused_alias=original!=alias,current_native_calls=self.tail.calls)
        if 'tail_seam' in out:
            if (out['tail_seam']['tail_jets']!=record['response']['jets'] or
                    out['tail_seam']['tail_shooting_residual']!=record['response']['residual']):
                raise ValueError('The physical seam does not match its genuine active response')
            out['tail_seam']['tail_record']=alias.name

    def save_completed_prefix_audit(self,cp,out):
        from curve_stable_prefix_bvp import save_checkpoint
        self.decorate_tail_record_identity(out)
        save_checkpoint(cp,out)
        self.event('complete_prefix_audit_saved_before_seam',checkpoint=parent.ref(cp),
                   metric=out['summary']['metric_l1'],darboux=out['summary']['darboux_l1'])


def run(plan_path):
    plan_path=Path(plan_path).resolve();plan=parent.load(plan_path)
    unsigned={k:v for k,v in plan.items() if k!='identity_sha256'}
    if parent.payload_sha(unsigned)!=plan['identity_sha256']:
        raise ValueError('Declared continuation plan changed')
    parent.check_sources(plan['source_sha256'])
    directory=Path(plan['output_prefix']).parent
    marker=directory/'continuation-started.json'
    parent.write_json(marker,dict(plan=parent.ref(plan_path),time_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
                                  command=[sys.executable,*sys.argv]))
    began=time.monotonic();ctx=None;terminal=dict(original_main_returned=False)
    old_argv=sys.argv[:]
    try:
        rebuilt,actual,initial,initial_path=form_initializer(plan,plan_path)
        path=runtime_plan(plan,plan_path,initial,initial_path)
        ctx=Context(path,rebuilt,actual);ctx.reconstruct()
        c=ctx.coupler;c.OWNED=ctx
        ctx.original_solve_bvp=c.solve_bvp;c.solve_bvp=ctx.observed_solve_bvp
        for name in ('outer-excerpt.py','main-excerpt.py'):
            file=ctx.plan['derived_source_files'][name]['path']
            exec(compile(Path(file).read_text(),file,'exec'),c.__dict__)
        sys.argv=[str(Path(__file__).resolve()),*ctx.plan['original_main_arguments']]
        c.main();terminal['original_main_returned']=True
    except BaseException as error:
        terminal.update(error=repr(error),traceback=traceback.format_exc())
        raise
    finally:
        sys.argv=old_argv;parent.check_sources(plan['source_sha256'])
        summary=directory/'seed-summary.json'
        if summary.is_file():
            value=parent.load(summary)
            terminal.update(original_summary=parent.ref(summary),original_solver_success=value.get('solver_success'),
                            original_error=value.get('error'))
        terminal.update(seconds=time.monotonic()-began,raw_inner_calls=ctx.inner_count if ctx else 0,
            actual_tail_calls=ctx.tail.calls if ctx and ctx.tail else 0,
            observed_worker_returncode=ctx.tail.proc.poll() if ctx and ctx.tail else None)
        parent.write_json(directory/'runner-terminal.json',terminal)
        print(json.dumps(dict(event='continuation_runner_terminal',**terminal)),flush=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    choice=parser.add_mutually_exclusive_group(required=True)
    choice.add_argument('--prepare',type=Path);choice.add_argument('--run-plan',type=Path)
    parser.add_argument('--checkpoint',type=Path);parser.add_argument('--lambda',dest='lam',type=float)
    args=parser.parse_args()
    if args.prepare is not None:
        if args.checkpoint is None or args.lam is None:
            raise ValueError('Preparation requires one complete checkpoint and one explicit lambda')
        prepare(args.checkpoint,args.lam,args.prepare)
    else:
        run(args.run_plan)


if __name__=='__main__':
    main()
