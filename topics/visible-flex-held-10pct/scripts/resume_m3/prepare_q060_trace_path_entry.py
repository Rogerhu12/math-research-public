#!/usr/bin/env python3
"""One source/metadata plan for lambda0 identity and the first lambda=.02 entry.

--prepare binds the original physical cosine checkpoint and new source only.
It reuses the already registered P(1) enclosure, with exact Fraction scalar
arithmetic for q(lambda)=.06/P(lambda). It does not construct a core or flow.
--evaluate-entry-plan is a separate future finite model check, never a BVP or
actual-tail solve. It uses the one declared lambda=.02, no alternate widths,
amplitudes, trace matching, failed-lambda1 coefficients, or parameter search.

The numerical gauge/pscale/warp remain the original .06. The support seed is
q(lambda). All seven original physical cosine coefficients enter the new
seven-column path; no column is discarded or converted to a twojet guess.
At lambda0 the original complete physical polynomial and unlifted Flow are
the reference identity. At positive lambda the mean-height primitive must be
recomputed by the original definition; it is not computed by this entry probe.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse
import copy
from fractions import Fraction as F
import gzip
import hashlib
import importlib.metadata
import importlib.util
import inspect
import json
import math
from pathlib import Path
import sys
import time
import traceback
import numpy as np

HERE=Path(__file__).resolve().parent
WORK=HERE.parents[4]
READER=HERE.parent/'resume_closed/q060_cosine_reference.py'
READER_SHA='776bd257f9a299cce73d215597dcf2d02d161bf493deb2a66f9ece0972a327d4'
BINDING=HERE.parent/'resume_closed/q060_cosine_reference_binding.json'
BINDING_SHA='01bfeedc8a160daf8ccae91a66b2f65d99c934166d26592b6a0e2b25049b0897'
PRIOR_SCALAR_PLAN=WORK/'m3_work/q060-circle-trace-design-plan.json'
PRIOR_SCALAR_PLAN_SHA='ce2533b9bb0342fdcb6a7c81560281e8ef47ace3798e0e9e79fc1b44a176d1fc'
OBSERVER=HERE.parent/'resume_n4/observe_command_live.py'
FIRST_LAMBDA=.02
ZERO_PHYSICAL_NODE_INDICES=(0,1,17,67,129,257,513,1025,1537,1933)
SETTINGS=dict(halfwidth=.21,transition=.32,control_transition=.4,homotopy=1.,
    center=math.pi/3,bimodal_eta=0.,lock_fundamental=True,
    coefficient_precision=80,positivity_grid_max=32768)
NEW_SOURCES=('circle_trace_homotopy_basis.py','circle_trace_homotopy_core.py',
             'synchronous_core_lift.py','m3_circle_trace_path_model.py',
             'prepare_q060_trace_path_entry.py')


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def ref(path):return dict(path=str(Path(path).resolve()),sha256=sha(path))
def binary_sha(value):return hashlib.sha256(np.asarray(value,dtype='float64').tobytes()).hexdigest()
def payload_sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()
def load(path):
    path=Path(path);raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw)
def write_json(path,value):
    with Path(path).open('x') as stream:json.dump(value,stream,indent=2,allow_nan=False);stream.write('\n')
def check_sources(sources):
    for path,expected in sources.items():
        if sha(path)!=expected:raise ValueError('Changed source/input: '+path)
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path);value=importlib.util.module_from_spec(spec)
    sys.modules[name]=value;spec.loader.exec_module(value);return value


def outward(interval,digits=50):
    denominator=10**digits
    values=[interval[0]*denominator,interval[1]*denominator]
    integers=[values[0].numerator//values[0].denominator,
              -((-values[1].numerator)//values[1].denominator)]
    def text(v):
        sign='-' if v<0 else '';integer,frac=divmod(abs(v),denominator)
        return sign+str(integer)+'.'+str(frac).zfill(digits)
    return list(map(text,integers))


def matched_amplitude(homotopy,registered_P1,old_q):
    """Reuse a registered scalar enclosure; no new moment integral evaluation."""
    lam=F.from_float(float(homotopy));one=F(1)
    p1=tuple(map(F,registered_P1))
    P=tuple(one+lam*(value-one) for value in p1)
    if not 0<=lam<=1 or P[0]<=0:raise ValueError('Positive declared scalar factor required')
    qold=F.from_float(float(old_q));interval=(qold/P[1],qold/P[0])
    nearest=float((interval[0]+interval[1])/2)
    left=(F.from_float(math.nextafter(nearest,-math.inf))+F.from_float(nearest))/2
    right=(F.from_float(nearest)+F.from_float(math.nextafter(nearest,math.inf)))/2
    if not left<interval[0]<=interval[1]<right:
        raise ArithmeticError('The registered P1 enclosure does not identify a unique nearest q')
    residual=tuple(F.from_float(nearest)*p-qold for p in P)
    return dict(lambda_value=float(homotopy),lambda_binary64_hex=float(homotopy).hex(),
        P_enclosure=outward(P),q_enclosure=outward(interval),q_binary64=nearest,
        q_binary64_hex=nearest.hex(),uniquely_nearest_binary64=True,
        defining_primary_residual_enclosure=outward(residual,60),
        rule='P(lambda)=1+lambda*(registered P1-1); q(lambda)=old_actual_q/P(lambda). Widths retain the registered defining-integral convention; lambda and old q are exact binary64 reals.',
        scope='Only the defining scalar moment. Rounded production core evaluation and the partially lifted finite inlet are separate.')


def bind_old():
    check_sources({str(READER):READER_SHA,str(BINDING):BINDING_SHA,
                   str(PRIOR_SCALAR_PLAN):PRIOR_SCALAR_PLAN_SHA})
    reader=module('q060_finite_path_original_reader',READER)
    record=load(BINDING)
    bound=reader.bind_reference(record['checkpoint']['path'],record['terminal_record']['path'],
                               record['source_topic'],record['short_bridge']['path'])
    return bound,record


def prepare(directory):
    bound,binding=bind_old();cp=bound.record
    prior=load(PRIOR_SCALAR_PLAN)
    P1=prior['design']['new_q']['Pnew_enclosure']
    if prior['design']['new_core_settings']!=SETTINGS:
        raise ValueError('The registered P1 belongs to a different endpoint')
    qspec={str(lam):matched_amplitude(lam,P1,cp['actual_primary_amplitude'])
           for lam in (0.,FIRST_LAMBDA,1.)}
    if qspec['0.0']['q_binary64']!=.06:
        raise ValueError('The literal cosine endpoint amplitude changed')
    tail_path=bound.checkpoint.with_name('seed_tail_0003.json.gz')
    tail=load(tail_path);response=tail['response'];request=tail['request']
    if (sha(tail_path)!=prior['design']['actual_affine_tail_anchor']['sha256'] or
        response.get('converged') is not True or not np.isfinite(response['residual']) or
        not response['residual']<2e-9 or tail['config']['solveTolerance']!=2e-9 or
        request['jacobian'] is not True or request['audit'] is not True):
        raise ValueError('The existing original full-H actual response is required')
    if np.asarray(response['heightJetJacobian']).size!=208 or not np.all(np.isfinite(response['heightJetJacobian'])):
        raise ValueError('The original complete finite M8 Jacobian must be available')
    inputs=dict(original_binding=ref(BINDING),physical_checkpoint=ref(bound.checkpoint),
        original_terminal=ref(bound.terminal_record),registered_scalar_plan=ref(PRIOR_SCALAR_PLAN),
        original_actual_tail=ref(tail_path),original_chart=binding['original_inputs']['chart'],
        original_linear_port=binding['original_inputs']['linear_port'],
        original_saved_inner=bound.terminal['saved_outer1']['raw_inner'])
    for i,item in enumerate(binding['coefficient_chunks']):inputs['physical_coefficient_chunk_'+str(i)]=item
    for item in inputs.values():
        if sha(item['path'])!=item['sha256']:raise ValueError('Changed entry input')
    sources={**bound.all_source_sha256,**prior['source_sha256'],
             str(READER):READER_SHA,str(BINDING):BINDING_SHA,str(PRIOR_SCALAR_PLAN):PRIOR_SCALAR_PLAN_SHA,
             str(OBSERVER):sha(OBSERVER)}
    sources.update({str((HERE/name).resolve()):sha(HERE/name) for name in NEW_SOURCES})
    scipy_source=Path(importlib.util.find_spec('scipy').origin).parent/'integrate/_bvp.py'
    sources[str(scipy_source.resolve())]=sha(scipy_source)
    check_sources(sources)
    from synchronous_core_lift import derived_sources,source_provenance
    derived=derived_sources()
    for name,text in derived.items():compile(text,'declared-'+name,'exec')
    directory=Path(directory).resolve()
    if directory.exists():raise FileExistsError('Use a new source/metadata directory')
    directory.mkdir(parents=True)
    derived_refs={}
    for name,text in derived.items():
        path=directory/(name+'-excerpt.py')
        with path.open('x') as stream:stream.write(text)
        derived_refs[name]=ref(path)
    p=np.asarray(cp['parameters'],float).copy();p[0]=0.
    controls=p[1:]*np.asarray(cp['central_correction_scales'])
    if binary_sha(controls)!=binary_sha(bound.actual_controls):
        raise ValueError('All seven original physical controls must enter the path')
    plan=dict(scope=__doc__,source_sha256=sources,inputs=inputs,
        original_source_topic=str(bound.source_topic),short_bridge=ref(bound.short_bridge),
        core_settings=SETTINGS,gauge_amplitude=.06,warp_reference_q=.06,modes=8,angular=cp['config']['angular'],
        original_parameter_scales=cp['central_correction_scales'],
        initial_parameters=p.tolist(),initial_parameters_binary64_sha256=binary_sha(p),
        complete_original_controls=controls.tolist(),
        physical_profile=cp['frozen_profile'],physical_profile_payload_sha256=payload_sha(cp['frozen_profile']),
        original_meridian_length=cp['meridian_length'],original_chart_payload_sha256=payload_sha(cp['chart']),
        original_historical_p0=cp['parameters'][0],new_p0=0.,
        delta_semantics='The final original frozen profile is the new base. The old p0 is not applied again; new p0 only varies delta.',
        support_amplitudes=qspec,registered_P1_enclosure=P1,
        scalar_scope='Read the existing P1 enclosure, then exact Fraction arithmetic only; no repeated moment integral, core evaluation, or amplitude scan.',
        evaluated_lambdas=[0.,FIRST_LAMBDA],endpoint_lambda_one_evaluated=False,
        lambda0_identity=dict(original_physical_polynomial_shape=[6,1933,25],extrapolate=False,
            full_polynomial_coefficients_reused=True,
            physical_node_indices=list(ZERO_PHYSICAL_NODE_INDICES),angular_samples=256,
            jets=['pos','p1','p2','s1','s2','sp','spp'],
            complete_H='Compare old and new full eight-component H read from the same original physical polynomial. Separately record its difference from the original accepted-tail H; never silently identify a rounded polynomial endpoint with the recorded raw endpoint.',
            mean_scope='Read the same original height_integral method/source and reuse the unchanged physical polynomial; no mean integration is performed, and no new sampled trajectory is claimed.',
            no_lift_factory='The actual original cosine class; original unlifted geo with no exact-lift property. The same rho>1e-5 path floor is additionally required after the unchanged original cosine constructor.'),
        first_entry=dict(lambda_value=FIRST_LAMBDA,nodes_argument=257,projection_angular=4096,
            initial_controls='All seven original physical coefficients via original parameter/scales, including old cos21 and cos24. No new trace twojet matching and no failed-lambda1 coefficients.',
            initialization='Original represented field Geo_old+.06*all25-state physical quintic; subtract new partial-lift reference, finite-project at4096 angles, then the same shared C2 inlet repair. Record omitted mean height separately.',
            repair_window=[.5,.9],repair_weight='a(s)*(1-smoothstep5((s-.5*prefix_end)/(.4*prefix_end)))',
            full_H='Explicitly encode the original complete actual H with unchanged sigma*.06; record all eight actual multiply-back differences and hashes after forming Y.',
            affine_scope='The original full-Jac actual response is used only by the original AffineTailForInnerBVP for initial BC. No native/actual tail is invoked or accepted.',
            diagnostics=['Original core guard','Original collocation nodes and midpoint domain',
                'Original RMS Lobatto points','Original initial BC with the declared affine anchor',
                'Finite represented pos/p1/p2 projection differences','Full H encoding'],
            no_mean_height_reconstruction=True,no_complete_metric=True,
            no_BVP=True,no_native_tail=True,no_step_or_parameter_search=True),
        lift_provenance=source_provenance(),derived_source_files=derived_refs,
        scipy=dict(version=importlib.metadata.version('scipy'),source=ref(scipy_source)),
        derivative_scope='For fixed lambda all h*dHpsi, h*dHpsipsi, convection, and -hp*dH terms carry lambda; inlet projection/Jacobian remains unscaled. p0 is the original finite difference of the actual partially lifted fun. No Jacobian result from the old failed lambda1 gauge is borrowed.',
        intermediate_inlet='(1-lambda)*(background+.06*finite inlet projection)+lambda*Gamma_lambda. Definition-core rho and primary moments are not actual finite-inlet geometry certificates.',
        original_gates=dict(rho_floor=1e-5,rho_grid_ceiling=32768,Frenet_margin='original >0',
            original_initial_RMS_only=True,BVP_tol=cp['config']['tol'],BC_tol=cp['config']['bc_tol'],
            physical_BC_tol=cp['config']['physical_bc_tol'],tail_tolerance=2e-9),
        original_actual_anchor=dict(**ref(tail_path),full_H=request['height'],
            full_H_binary64_sha256=binary_sha(request['height']),residual=response['residual']),
        output=str(directory/'entry.json'),arrays_output=str(directory/'entry-arrays.npz'),
        events_output=str(directory/'entry-events.jsonl'),
        metadata_only=True,native_reference_constructed=False,new_core_constructed=False,
        initializer_constructed=False,BVP_solver_invoked=False,actual_tail_solver_invoked=False,
        mean_height_reconstructed=False)
    plan['identity_sha256']=payload_sha(plan)
    path=directory/'launch-plan.json';write_json(path,plan)
    command=[sys.executable,str(Path(__file__).resolve()),'--evaluate-entry-plan',str(path)]
    observer=[sys.executable,str(OBSERVER),'--out',str(directory/'resource.json'),
              '--log',str(directory/'stdout.log'),'--',*command]
    write_json(directory/'launch-command.json',dict(plan=ref(path),command=command,observer_command=observer))
    print(json.dumps(dict(metadata_only=True,plan=ref(path),identity_sha256=plan['identity_sha256'],
        source_inputs=len(sources),references=len(inputs),first_lambda=FIRST_LAMBDA,
        first_primary_q=qspec[str(FIRST_LAMBDA)]['q_binary64'],no_model_evaluation=True)),flush=True)


def finite_difference_row(a,b):
    return dict(binary64_equal=binary_sha(a)==binary_sha(b),
                maximum_absolute_difference=float(np.max(np.abs(a-b))),shape=list(np.asarray(a).shape))


def evaluate(plan_path):
    plan_path=Path(plan_path).resolve();plan=load(plan_path)
    check=copy.deepcopy(plan);identity=check.pop('identity_sha256')
    if payload_sha(check)!=identity:raise ValueError('Frozen plan payload changed')
    check_sources(plan['source_sha256'])
    for item in [*plan['inputs'].values(),*plan['derived_source_files'].values()]:
        if sha(item['path'])!=item['sha256']:raise ValueError('Changed frozen reference or derived source')
    if (plan['evaluated_lambdas']!=[0.,FIRST_LAMBDA] or
        plan['lambda0_identity']['physical_node_indices']!=list(ZERO_PHYSICAL_NODE_INDICES)):
        raise ValueError('The declared unique entry scope changed')
    for key in ('output','arrays_output','events_output'):
        if Path(plan[key]).exists():raise FileExistsError('This unique entry already began')
    began=time.monotonic();stage='bind_original_reference';arrays={}
    counters=dict(BVP_attempts=0,native_tail_attempts=0)
    result=dict(scope=__doc__,plan=ref(plan_path),plan_identity_sha256=identity,
        complete=False,source_sha256=plan['source_sha256'],counters=counters,
        BVP_solver_invoked=False,actual_tail_solver_invoked=False,mean_height_reconstructed=False,
        full_metric_computed=False,endpoint_lambda_one_evaluated=False)
    def event(name,**fields):
        value=dict(event=name,utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),**fields)
        with Path(plan['events_output']).open('a') as stream:
            stream.write(json.dumps(value,separators=(',',':'),allow_nan=False)+'\n')
        print(json.dumps(value,separators=(',',':'),allow_nan=False),flush=True)
    event('entry_started',plan=ref(plan_path))
    try:
        import scipy.integrate
        from scipy.integrate import _bvp
        def forbidden_BVP(*args,**kwargs):
            counters['BVP_attempts']+=1
            raise RuntimeError('The model-entry check does not invoke a BVP')
        scipy.integrate.solve_bvp=forbidden_BVP;_bvp.solve_bvp=forbidden_BVP
        bound,_=bind_old();native=bound.native_reference()
        result['native_reference_constructed']=True
        # The reader descriptor itself says construction=False because its
        # original CLI was metadata-only. This actual call is recorded above.
        from m3_circle_trace_path_model import CircleTracePathEnvironment
        env=CircleTracePathEnvironment(bound,native,plan['core_settings'])
        def forbidden_native(*args,**kwargs):
            counters['native_tail_attempts']+=1
            raise RuntimeError('The model-entry check does not invoke an actual tail')
        env.coupler.client.WeightedTailPort=forbidden_native
        p=np.asarray(plan['initial_parameters'],float)
        if binary_sha(p)!=plan['initial_parameters_binary64_sha256']:
            raise ValueError('All eight initial parameters must be retained')
        stage='lambda_zero_original_model_identity'
        zero=env.make(0.,plan['support_amplitudes']['0.0']['q_binary64'])
        zero.initial(p);f0=zero.flow(0.);oldf=native.flow;pp=native.polynomial
        if type(zero._core) is not type(native.core):raise ValueError('Lambda zero lost the literal original core class')
        if (hasattr(f0,'exact_lift_core') or hasattr(oldf,'exact_lift_core') or
            inspect.getsource(type(f0).geo)!=inspect.getsource(type(oldf).geo)):
            raise ValueError('Lambda zero must retain the original unlifted geo path')
        if (binary_sha(zero._core.coefficients)!=binary_sha(native.core.coefficients) or
            binary_sha(zero.pscale)!=binary_sha(native.original_scales) or
            float(f0.end).hex()!=float(oldf.end).hex() or f0.q!=oldf.q or f0.warp_e!=oldf.warp_e):
            raise ValueError('Original full cosine core/scales/domain/gauge/chart changed')
        si=pp.x[np.asarray(ZERO_PHYSICAL_NODE_INDICES,int)]
        oldB=oldf.basis(256);zeroB=f0.basis(256)
        oldgeo,zerogeo=oldf.geo(si,256),f0.geo(si,256)
        Y=[pp(si,k) for k in range(3)]
        identity_rows={}
        for key,dr,da in [('pos',0,0),('p1',0,1),('p2',0,2),('s1',1,0),
                          ('s2',2,0),('sp',1,1),('spp',1,2)]:
            oldvalue=oldgeo[key]+oldf.q*oldf.values(Y[dr],oldB[da])
            zerovalue=zerogeo[key]+f0.q*f0.values(Y[dr],zeroB[da])
            identity_rows[key]=finite_difference_row(oldvalue,zerovalue)
            arrays['lambda0_original_'+key]=oldvalue;arrays['lambda0_new_'+key]=zerovalue
        ycut=pp(np.array([pp.x[-1]]))[:,0]
        oldH=oldf.bridge.sigma*oldf.q*ycut[17:]
        zeroH=zero.bridge.sigma*zero.q*ycut[17:]
        Hanchor=np.asarray(plan['original_actual_anchor']['full_H'],float)
        mean_method_equal=inspect.getsource(type(oldf).height_integral)==inspect.getsource(type(f0).height_integral)
        if not all(row['binary64_equal'] for row in identity_rows.values()) or binary_sha(oldH)!=binary_sha(zeroH):
            raise ValueError('The declared finite lambda0 represented identity did not hold')
        if not mean_method_equal:raise ValueError('Lambda zero changed the mean-height definition')
        result['lambda_zero_identity']=dict(core_class_literal_original=True,
            original_polynomial_shape=list(pp.c.shape),original_polynomial_coefficients_binary64_sha256=binary_sha(pp.c),
            original_physical_mesh_binary64_sha256=binary_sha(pp.x),original_polynomial_reused=True,
            full_25_states=True,physical_node_indices=list(ZERO_PHYSICAL_NODE_INDICES),
            physical_nodes=si.tolist(),angular_samples=256,represented_jet_checks=identity_rows,
            complete_H_identity=finite_difference_row(oldH,zeroH),
            physical_polynomial_H=oldH.tolist(),accepted_actual_anchor_H=Hanchor.tolist(),
            physical_polynomial_vs_actual_anchor_difference=(oldH-Hanchor).tolist(),
            physical_polynomial_vs_actual_anchor_binary64_equal=binary_sha(oldH)==binary_sha(Hanchor),
            mean_height_method_source_equal=True,mean_height_reconstructed=False,
            mean_scope='Same original method and unchanged physical polynomial; the actual integral trajectory has not been recomputed.',
            source_scope='The lambda0 model uses the literal original cosine core and unlifted geo; the finite jet equality above is sampled, not an interval bound on transcendental evaluation.',
            p0=0.,full_physical_controls=(p[1:]*zero.pscale).tolist(),
            gauge=zero.q,support_amplitude=zero.support_amplitude,
            old_historical_p0_not_reapplied=True)
        event('lambda_zero_identity_completed',represented_jets=7,full_H_equal=True)
        stage='first_nonzero_core_and_original_domain'
        obj=env.make(FIRST_LAMBDA,plan['support_amplitudes'][str(FIRST_LAMBDA)]['q_binary64'])
        obj.initial(p);f=obj.flow(0.)
        if (obj.q!=.06 or obj.support_amplitude!=obj.seed_support_amplitude or
            binary_sha(p[1:]*obj.pscale)!=binary_sha(plan['complete_original_controls']) or
            float(f.end).hex()!=float(oldf.end).hex()):
            raise ValueError('The first positive-lambda model changed a frozen identity')
        from fixed_metric_mode3_bvp import merge_profile_mesh
        t=merge_profile_mesh(np.linspace(0,1,257),obj.chart_breaks);s,_=obj.chart(t,0.)
        oldY=pp(s);B,B1,B2=f.basis(4096);oldbasis=oldf.basis(4096)
        y=np.empty((25,len(t)));projection_errors=np.zeros(3)
        stage='first_nonzero_complete_represented_field_projection'
        for first in range(0,len(t),24):
            sl=slice(first,first+24);ogeo=oldf.geo(s[sl],4096);ngeo=f.geo(s[sl],4096)
            if not np.array_equal(ogeo['theta'],ngeo['theta']):
                raise ValueError('This declared entry does not change the angular chart')
            previous=ogeo['pos']+oldf.q*oldf.values(oldY[:,sl],oldbasis[0])
            y[:,sl]=f.project(previous-ngeo['pos'],B)/obj.q
            for k,(key,bb,ob) in enumerate(zip(('pos','p1','p2'),(B,B1,B2),oldbasis)):
                difference=ngeo[key]+obj.q*f.values(y[:,sl],bb)-ogeo[key]-oldf.q*oldf.values(oldY[:,sl],ob)
                projection_errors[k]=max(projection_errors[k],float(np.max(abs(difference))))
        prior_cut=y[17:,-1].copy()
        y[17:,-1]=Hanchor/(obj.bridge.sigma*obj.q)
        inlet_correction=obj.initial(p)-y[:,0]
        u=np.clip((s-.5*f.prefix_end)/(.4*f.prefix_end),0.,1.)
        weight=f.profile(s)[0]*(1-u**3*(10-15*u+6*u*u))
        y+=inlet_correction[:,None]*weight[None,:]
        H=obj.bridge.sigma*obj.q*y[17:,-1]
        arrays.update(initial_t=t,initial_y=y,initial_p=p,initial_s=s,initial_H=H,
                      original_H_anchor=Hanchor,initial_inlet_correction=inlet_correction)
        result['formed_first_entry']=dict(lambda_value=FIRST_LAMBDA,path_definition=obj.path_definition,
            nodes=len(t),state_binary64_sha256=binary_sha(y),parameter_binary64_sha256=binary_sha(p),
            complete_physical_controls=(p[1:]*obj.pscale).tolist(),
            represented_pos_angular1_angular2_projection_errors=projection_errors.tolist(),
            representation_scope='Geo plus all25 finite Fourier states only; the original velocity mean primitive is omitted from these projection differences, not assumed zero.',
            full_H=H.tolist(),old_actual_H=Hanchor.tolist(),full_H_binary64_sha256=binary_sha(H),
            full_H_binary64_equal=binary_sha(H)==binary_sha(Hanchor),full_H_difference=(H-Hanchor).tolist(),
            cut_coefficient_reencoding_difference=(y[17:,-1]-prior_cut).tolist(),
            inlet_residual=float(np.max(abs(y[:,0]-obj.initial(p)))),
            actual_inlet_metrics_metadata=copy.deepcopy(obj._inlet_metrics),
            numerical_core_guard=dict(rho_lower=float(obj._core.rho_lower),
                rho_min_sample=float(obj._core.rho_min_sample),grid=int(obj._core.positivity_grid_per_sector)),
            full_metric_computed=False,mean_height_reconstructed=False)
        event('first_nonzero_entry_formed',nodes=len(t),H_equal=binary_sha(H)==binary_sha(Hanchor))
        tail=load(plan['original_actual_anchor']['path'])
        obj.tail=env.coupler.AffineTailForInnerBVP(Hanchor,tail['response'],8)
        stage='first_nonzero_original_collocation_domain'
        h=np.diff(t);col,middle,rhs,rhs_middle=_bvp.collocation_fun(obj.fun,y,p,t,h)
        spline=_bvp.create_spline(y,rhs,t,h)
        arrays.update(initial_node_rhs=rhs,initial_cubic=spline.c,collocation_residual=col,
                      collocation_midpoint=middle)
        stage='first_nonzero_original_RMS_domain'
        rms=_bvp.estimate_rms_residuals(obj.fun,spline,t,h,p,1.5*col/h,rhs_middle)
        arrays['initial_rms']=rms
        stage='first_nonzero_original_initial_BC_affine_only'
        boundary=obj.bc(y[:,0],y[:,-1],p)
        arrays['initial_BC_affine_only']=boundary
        if not all(np.all(np.isfinite(a)) for a in (col,rms,boundary)):
            raise FloatingPointError('A planned original entry diagnostic was nonfinite')
        # No additional scan: these are the same nodes and midpoint states
        # whose original collocation call just passed its own frame checks.
        minimum=1.
        for coords,field in ((t,y),((t[:-1]+t[1:])/2,middle)):
            physical,_=obj.chart(coords,0.)
            for first in range(0,len(coords),32):
                sl=slice(first,first+32)
                minimum=min(minimum,float(np.min(f.frame(physical[sl],obj.q*field[:,sl])['margin'].real)))
        result['original_entry_diagnostics']=dict(original_domains_passed=True,
            maximum_original_collocation_RMS=float(np.max(rms)),
            maximum_collocation_residual=float(np.max(abs(col))),
            maximum_original_BC_affine_only=float(np.max(abs(boundary))),
            sampled_nodes_midpoints_minimum_Frenet_margin=minimum,
            scope='Initial finite diagnostics with the old actual response used only as an affine slope anchor. No solver acceptance or complete metric is asserted.')
        if counters['BVP_attempts'] or counters['native_tail_attempts']:
            raise RuntimeError('A forbidden solver was attempted')
        result['complete']=True
        event('entry_diagnostic_completed',maximum_RMS=float(np.max(rms)))
    except Exception as error:
        result['failure']=dict(stage=stage,type=type(error).__name__,message=str(error),
                               traceback=traceback.format_exc(),automatic_retry=False)
        event('entry_diagnostic_failed',stage=stage,error=repr(error))
    check_sources(plan['source_sha256'])
    if arrays:
        with Path(plan['arrays_output']).open('xb') as stream:np.savez_compressed(stream,**arrays)
        result['arrays']=ref(plan['arrays_output'])
    result['seconds']=time.monotonic()-began
    result['exit_status_requested']=0 if result['complete'] else 2
    write_json(plan['output'],result)
    event('entry_record_saved',output=ref(plan['output']),complete=result['complete'])
    return result['exit_status_requested']


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--prepare',type=Path)
    group.add_argument('--evaluate-entry-plan',type=Path)
    args=parser.parse_args()
    if args.prepare:
        prepare(args.prepare);return 0
    return evaluate(args.evaluate_entry_plan)


if __name__=='__main__':raise SystemExit(main())
