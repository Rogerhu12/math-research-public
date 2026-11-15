#!/usr/bin/env python3
"""Request157: persistent Decimal50 full3 residual quadratic square, with labelled old fallback.

The complete finite699-node radius/three-mode equations and112 slope rows
are reevaluated using exact lifts of the old binary64 coefficient words.
Parameters, forward9/second9/normal2 variations, QR, model trials, R299
selection and the full3 Armijo decision never round the owner state to64.
The old initial/final54 finite-difference column checks and scalar/453-circle
checks are retained at explicitly recorded binary64 projection points.
They are not a certificate for the different persistent Decimal point.
No native nonlinear field, high-mode Schur result or full-DN is claimed.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import signal
import sys
import time
import traceback

HERE=Path(__file__).resolve().parent
ENTRY='geometry_20261115_small_core_nine_control_decimal_residual_quadratic_recipe.py'
SCHEMA='R259-nine-control-persistent-decimal50-residual-quadratic-square-trust-v1'
STATUS_NAME='nine-control-decimal50-residual-quadratic-status.json'
DECIMAL_RECIPE_SCHEMA='R259-explicit-nine-control-decimal50-residual-quadratic-exploration-recipe-v1'
ACTUAL_PARENT='geometry_20261115_small_core_nine_control_decimal_curvature_recipe.py'
ACTUAL_PARENT_SHA='3d59811078d82110449216a8ab5dadf905c435e1e45085b96f6d1c8fa04eb0c4'
ACTUAL_PARENT_SCHEMA='R259-nine-control-persistent-decimal50-ambient-curvature-trust-v1'
OLD_DECIMAL_PRODUCER='geometry_20261115_small_core_nine_control_decimal_recipe.py'
OLD_DECIMAL_PRODUCER_SHA='66906f121c52f6dc57894efa368299990eea45f2f1d4fc5e6ce4af2fc5b9536e'
AMBIENT_HELPERS='geometry_20261115_nine_control_decimal_ambient_trust.py'
AMBIENT_HELPERS_SHA='bb603fc6c32f146552262b38648ddc2e777e5968a1473259ad6d1e6ce2a86115'
ORIGINAL_MODEL='geometry_20261115_nine_control_decimal_literal_model.py'
ORIGINAL_MODEL_SHA='2422be0c2e30d10c38b56ff7b68412c5397d37ed36451676bb16acbdc142ef75'
ORIGINAL_SEARCH='geometry_20261115_nine_control_decimal_curved_search.py'
ORIGINAL_SEARCH_SHA='433d5ddd2587efa581fb28ea151ddf3cec5b6a63eb5017340375d1f19b6d98d0'
EXPLORATION_POLICY={'initial_relative_trust_radius':'0.01','parent_radius_is_provenance_only':True,'primary_path':'complete-nine-residual-quadratic-square-straight-line','fallback':'original149-complete-GN-normal-only-if-primary-fails-or-all20-reject'}
PARENT='geometry_20261115_small_core_nine_control_direct_normal_response_recipe.py'
PARENT_SHA='c717bafb95854bef7b60048a8194b9949a30fbff29bc5e1eee8a0dbb25cf233b'
PARENT_SCHEMA='R259-nine-control-full-three-direct-normal-response-carried-radius-trust-recipe-v1'
MODEL='geometry_20261115_nine_control_decimal_second_variation.py'
MODEL_SHA='ad568abc8bf35003375d80e303c44df6dcb2f1c75fd41163cf5c0f423ba321a1'
SEARCH='geometry_20261115_nine_control_decimal_residual_quadratic_trust.py'
SEARCH_SHA='ef61c5f19370a302b198901a7691fda31ed0a6619d9f9dcafc147f6b1bdc3180'
INPUTS={
 'accepted':'b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff',
 'prepared':'0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714',
 'tail_anchor':'e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51',
 'tail_config':'01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5',
}


class ResourceStopped(RuntimeError):
    pass


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS')!='true'
        or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific execution is public repository Actions only')


def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(1<<20),b''):
            h.update(block)
    return h.hexdigest()


def source_module(name,expected):
    if Path(name).name!=name or sha(HERE/name)!=expected:
        raise ValueError('The explicitly bound source differs: '+name)
    spec=importlib.util.spec_from_file_location(name[:-3],HERE/name)
    module=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=module
    spec.loader.exec_module(module)
    return module


def require_digest(value,length=64):
    if not isinstance(value,str) or len(value)!=length or any(c not in '0123456789abcdef' for c in value):
        raise ValueError('An entire actual digest is required')
    return value


def read_recipe(path,expected,parent,parent_sources,baseline_sources,sources,k):
    raw=Path(path).read_bytes()
    if len(raw)>16384 or hashlib.sha256(raw).hexdigest()!=require_digest(expected):
        raise ValueError('The complete short actual parent recipe must match its stated bytes')
    def reject(value):
        raise ValueError('Nonstandard JSON number: '+value)
    value=json.loads(raw,parse_constant=reject)
    required={'schema','origin','literal_parameters','algorithm_state','input_sha256','family','precision','exploration_policy'}
    if set(value)!=required or value.get('schema')!=DECIMAL_RECIPE_SCHEMA:
        raise ValueError('Require the independent residual-quadratic recipe and explicit exploration policy')
    if value['input_sha256']!=INPUTS or value['family']!=parent.FAMILY_IDENTITY:
        raise ValueError('Keep all original inputs and all nine physical controls')
    if value['precision']!={'decimal_digits':50,'rounding':'ROUND_HALF_EVEN','parameter_encoding':'finite-decimal-strings'}:
        raise ValueError('Do not reproject or relabel the persistent parent arithmetic')
    if value['exploration_policy']!=EXPLORATION_POLICY:
        raise ValueError('This experiment explicitly explores radius .01; no silent radius substitution')
    origin=value['origin']
    fields={'repository','run_id','source_commit','producer_file','producer_sha256','producer_schema',
            'status_bytes','status_sha256','log_summary_bytes','log_summary_sha256','parameter_field','radius_field'}
    if not isinstance(origin,dict) or set(origin)!=fields:
        raise ValueError('Keep the complete actual origin tuple')
    allowed={ACTUAL_PARENT:(ACTUAL_PARENT_SHA,ACTUAL_PARENT_SCHEMA),ENTRY:(sources[ENTRY],SCHEMA)}
    pair=allowed.get(origin['producer_file'])
    if (origin['repository']!='Rogerhu12/math-research-public' or not isinstance(origin['run_id'],str)
        or not origin['run_id'].isdigit() or pair!=(origin['producer_sha256'],origin['producer_schema'])
        or origin['parameter_field']!='final.parameters' or origin['radius_field']!='final_relative_trust_radius'):
        raise ValueError('Use actual154 or this exact own-schema parent, retaining its true producer')
    for name,length in [('source_commit',40),('producer_sha256',64),('status_sha256',64),('log_summary_sha256',64)]:
        require_digest(origin[name],length)
    if any(type(origin[name]) is not int or origin[name]<=0 for name in ('status_bytes','log_summary_bytes')):
        raise ValueError('Record actual origin byte counts')
    if not isinstance(value['literal_parameters'],list) or not all(type(x)is str for x in value['literal_parameters']):
        raise ValueError('Every persistent parameter remains an explicit exact decimal string')
    parameters=k.exact_parameters(value['literal_parameters'])
    algorithm=value['algorithm_state']
    if not isinstance(algorithm,dict) or set(algorithm)!={'relative_trust_radius'} or type(algorithm['relative_trust_radius'])is not str:
        raise ValueError('Preserve the actual parent radius separately as a decimal string')
    parent_radius=k.dec(algorithm['relative_trust_radius'])
    if not parent_radius.is_finite() or not k.ZERO<=parent_radius<=k.ONE:
        raise ValueError('Malformed parent radius metadata')
    radius=k.dec(EXPLORATION_POLICY['initial_relative_trust_radius'])
    receipt=dict(file='parameter-recipe.json',bytes=len(raw),sha256=expected,schema=DECIMAL_RECIPE_SCHEMA,
        origin=origin,literal_parameters=value['literal_parameters'],algorithm_state=algorithm,
        exploration_policy=EXPLORATION_POLICY,actual_parent_radius=parent_radius,
        new_experiment_initial_radius=radius,new_radius_does_not_claim_parent_carry=True,
        precision=value['precision'],family=value['family'],current_parameter_encoding='finite-decimal-strings',
        persistent_high_precision_parent_parameters_reused=True,
        origin_source_closure_from_pinned_producer_definition={n:h for n,h in sources.items()
            if n not in (SEARCH,ENTRY)} if origin['producer_file']==ACTUAL_PARENT else sources,
        origin_source_closure_not_reverified_from_parent_status=True,
        reported_origin_status_and_log_payloads_read=False,reported_origin_status_and_log_hashes_are_provenance_only=True,
        saved_parent_J_merit_Hessian_state_or_FD_reused=False,
        parameter_recipe_is_not_a_completed_field_or_original_status=True)
    return raw,parameters,radius,receipt


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('accepted','prepared','tail-anchor','tail-config','parameter-recipe','out'):
        parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--parameter-recipe-sha256',required=True)
    parser.add_argument('--decimal-digits',type=int,default=50)
    parser.add_argument('--candidate-steps',type=int,default=8)
    parser.add_argument('--backtracks',type=int,default=20)
    parser.add_argument('--normal-iterations',type=int,default=12)
    parser.add_argument('--normal-backtracks',type=int,default=20)
    parser.add_argument('--normal-target-tolerance',default='1e-8')
    parser.add_argument('--candidate-resonance-tolerance',default='1e-8')
    parser.add_argument('--interval-bits',type=int,default=160)
    parser.add_argument('--interval-depth',type=int,default=14)
    args=parser.parse_args()
    require_actions()
    if Path(__file__).name!=ENTRY:
        raise ValueError('Retain this independent producer identity')
    if (args.decimal_digits,args.candidate_steps,args.backtracks,args.normal_iterations,
        args.normal_backtracks,args.normal_target_tolerance,args.candidate_resonance_tolerance,
        args.interval_bits,args.interval_depth)!=(50,8,20,12,20,'1e-8','1e-8',160,14):
        raise ValueError('Retain Decimal50, original8x20/12x20, both original1e-8 flags and final160/14 consumers')
    for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
        os.environ[name]='1'
    parent=source_module(PARENT,PARENT_SHA)
    baseline,baseline_sources,parent_sources=parent.load_baseline()
    if len(parent_sources)!=33 or parent_sources.get(PARENT)!=PARENT_SHA or parent.INPUTS!=INPUTS:
        raise ValueError('Keep actual146 entire thirty-three-source ancestry and inputs')
    for name,expected in ((ORIGINAL_MODEL,ORIGINAL_MODEL_SHA),(ORIGINAL_SEARCH,ORIGINAL_SEARCH_SHA),
                          (OLD_DECIMAL_PRODUCER,OLD_DECIMAL_PRODUCER_SHA),
                          (AMBIENT_HELPERS,AMBIENT_HELPERS_SHA),
                          (ACTUAL_PARENT,ACTUAL_PARENT_SHA),(MODEL,MODEL_SHA),(SEARCH,SEARCH_SHA)):
        if sha(HERE/name)!=expected:
            raise ValueError('The independent high-precision source changed: '+name)
    k=source_module(MODEL,MODEL_SHA)
    solver=source_module(SEARCH,SEARCH_SHA)
    sources={**parent_sources,ORIGINAL_MODEL:ORIGINAL_MODEL_SHA,ORIGINAL_SEARCH:ORIGINAL_SEARCH_SHA,
             OLD_DECIMAL_PRODUCER:OLD_DECIMAL_PRODUCER_SHA,AMBIENT_HELPERS:AMBIENT_HELPERS_SHA,
             ACTUAL_PARENT:ACTUAL_PARENT_SHA,MODEL:MODEL_SHA,SEARCH:SEARCH_SHA,ENTRY:sha(__file__)}
    if len(sources)!=41:
        raise ValueError('Keep actual154 complete39 plus the independent residual-model search and producer')
    for name,expected in INPUTS.items():
        if sha(getattr(args,name))!=expected:
            raise ValueError('Use the complete original mathematical input: '+name)
    raw_recipe,p,radius,receipt=read_recipe(args.parameter_recipe,args.parameter_recipe_sha256,
        parent,parent_sources,baseline_sources,sources,k)
    if not radius.is_finite() or not k.ZERO<=radius<=k.ONE:
        raise ValueError('Do not clamp the true finite original radius')
    family=source_module(parent.FAMILY,parent.FAMILY_SHA)
    if family.EXPECTED!=INPUTS or any(sources.get(n)!=s for n,s in family.checked_sources().items()):
        raise ValueError('The original complete nine-control model/source binding changed')
    np,original=family.np,family.original
    if args.out.exists() and any(args.out.iterdir()):
        raise ValueError('Use a fresh independent experiment output')
    args.out.mkdir(parents=True,exist_ok=True)
    (args.out/'parameter-recipe.json').write_bytes(raw_recipe)
    status=dict(schema=SCHEMA,phase='starting',source_sha256=sources[ENTRY],
        consumed_source_sha256=sources,input_sha256=INPUTS,parameter_recipe=receipt,
        source_roles=dict(current_literal_model=MODEL,current_complete_search=SEARCH,
            original_projection_and_coefficient_model=parent.FAMILY,
            original146_identity_setup_helpers=PARENT,actual154_source_identity=ACTUAL_PARENT,
            inherited149_producer_identity=OLD_DECIMAL_PRODUCER,
            frozen154_spectral_and_shift_helpers=AMBIENT_HELPERS,
            original154_producer_and_search_main_not_executed=True,
            original149_model_and_tagged_fallback_helpers_used=True,
            original149_producer_main_not_executed=True),
        run_id=os.environ.get('GITHUB_RUN_ID'),source_commit=os.environ.get('GITHUB_SHA'),
        decimal_digits=50,rounding='ROUND_HALF_EVEN',parameter_encoding='finite-decimal-strings',
        candidate_iteration_budget=8,original_backtrack_budget=20,
        primary_straight_trial_budget=20,separate_original_normal_fallback_trial_budget=20,
        maximum_outer_trials_per_direction=40,primary_residual_polynomial_not_used_for_normal_path=True,
        complete_polynomial_solver_budget=solver.MODEL_POLICY,
        polynomial_inner_progress_never_adopts_a_physical_state=True,
        complete_second_forward_Hessian_shape=[3,9,9],initial_and_final_second_axis_checks_planned=54,
        initial_and_final_second_axis_checks_completed=False,explicit_new_exploration_policy=EXPLORATION_POLICY,
        normal_correction_iterations=12,normal_correction_backtracks=20,
        normal_target_error_tolerance=k.TOL,candidate_resonance_tolerance=k.TOL,
        original_armijo_coefficient=k.ARM,original_binary64_epsilon_damping_floor_coefficient=k.EPS64,
        actual_initial_parameters=p,initial_relative_trust_radius=radius,
        current_persistent_parameters=p,current_relative_trust_radius=radius,
        original_Armijo_accepted_point_count=0,searches=[],
        original_nine_design_parameters_and_all112_linear_rows_retained=True,
        full_high109_Schur_or_native_nonlinear_solver_called=False,
        native_nonlinear_solver_called=False,full_nonlinear_nonzero_lambda_solution_computed=False,
        nonzero_field_completed=False,success=False,diagnostic_completed=False,resource_partial=False,
        initial_guess_not_an_accepted_nonzero_field=True,
        no_additional_inner_target_or_rank_acceptance_gate=True,
        R299_completed_trace_full3_minimum_rule_retained=True,
        R299_selection_does_not_rescue_incomplete_evaluation=True,
        complex_step_used_for_high_precision_response=False,
        persistent_owner_ever_replaced_by_binary64_projection=False,
        original_initial_and_final_54_FD_column_checks_are_at_declared_binary64_projection=True,
        new_initial_and_final_54_Decimal_FD_column_checks_are_at_actual_persistent_points=True,
        derivative_is_rounded_forward_real_expression_not_discrete_rounding_derivative=True,
        interval_enclosure_or_exact_derivative_certificate_claimed=False,
        input_literal_table_formation_recomputed_in_high_precision=False,
        original_target_and_native_anchor_J_not_recomputed=True,
        final_projection_checks_do_not_certify_the_distinct_high_precision_point=True,
        original_public_Actions_only=True)
    started=time.monotonic()
    trace=None;model=None
    ledger_path=args.out/'decimal-evaluation-events.jsonl'
    ledger=ledger_path.open('wb')
    ledger_hash=hashlib.sha256();ledger_count=0
    status_path=args.out/STATUS_NAME

    def checkpoint():
        raw=k.encoded(status)+b'\n'
        temporary=status_path.with_suffix('.pending')
        temporary.write_bytes(raw)
        os.replace(temporary,status_path)

    def event_sink(event):
        nonlocal ledger_count
        raw=k.encoded(event)+b'\n'
        ledger.write(raw);ledger.flush();ledger_hash.update(raw);ledger_count+=1
        if model is not None:
            status['high_precision_call_counts']=dict(model.counts)

    def outer_event(event):
        print(k.encoded(event).decode('ascii'),flush=True)

    def stopped(signum,frame):
        raise ResourceStopped('Received signal '+str(signum)+'; scientific completion not inferred')
    old_signals={}
    for signum in (signal.SIGTERM,signal.SIGINT):
        old_signals[signum]=signal.signal(signum,stopped)
    checkpoint()
    try:
        prepared,accepted,anchor=[original.read(path) for path in
                                (args.prepared,args.accepted,args.tail_anchor)]
        profile,flow,boundary=family.setup(accepted,prepared,anchor,4096,1)
        true_J=np.asarray(anchor['heightJetJacobian']).reshape(3*flow.M+2,flow.M)[:flow.M]
        target=np.asarray(accepted['core']['coefficients'])[:3]
        trace=baseline.EvaluationTrace(args.out/'original-projection-calls')
        original_model=family.observed_model_class(trace,baseline)(
            profile,prepared['mesh'],true_J,target,boundary.eh,boundary.cut_scale)
        if not original_model.exactly_diagonal or np.any(target==0):
            raise ValueError('The original unit-equation guard retains every actual offdiagonal entry and every nonzero target')
        status.update(original_mesh_nodes=len(original_model.x),field_and_tail_modes=flow.M,
            original_nine_profile=profile.description(),family_identity=parent.FAMILY_IDENTITY,
            original_native_slope_J_exactly_diagonal=bool(original_model.exactly_diagonal),
            original_target_all_nonzero=bool(np.all(target!=0)))

        def projection(parameters,label):
            # This is an explicit one-way diagnostic/export conversion only.
            fp=[float(x) for x in parameters]
            if not all(math.isfinite(x) for x in fp):
                raise k.NumericalFailure('The declared binary64 projection is not finite')
            q=np.asarray(fp,float)
            with trace.context(label+'/original-binary64-primal'):
                projected_state=original_model.evaluate(q)
            with trace.context(label+'/original-all-nine-column-three-step-FD'):
                description=original_model.description(projected_state)
            binding=dict(scope='fresh original64 diagnostics only; never adopted by Decimal owner',
                actual_persistent_parameters=list(parameters),actual_binary64_parameters=q.tolist(),
                actual_binary64_parameter_hex=[x.hex() for x in fp],
                exact_binary64_parameter_lifts=[k.dec(x) for x in fp],
                persistent_minus_binary64_lift=[x-k.dec(y) for x,y in zip(parameters,fp)],
                projection_difference_is_rounded_Decimal50_readback_not_an_interval_bound=True,
                coefficient_model_identity=parent.FAMILY_SHA,
                all27_original_FD_checks_attempted_by_original_description=True,
                parameter_cast_is_an_explicit_projection_not_a_precision_refinement=True,
                projected_checks_are_not_same_point_high_precision_certificates=True)
            return projected_state,dict(projection=binding,original_description=description)

        with k.precision_context():
            model=k.LiteralCircleModel(original_model,event_sink)
            status['literal_model_binding']=model.binding
            projected_initial,projection_initial=projection(p,'initial-projection')
            status['initial_original_binary64_projection']=projection_initial
            with trace.context('initial-projection/old-zero-quadratic-counterfactual-readback'):
                status['original_zero_added_quadratic_counterfactual_at_projection']=family.zero_added_quadratic_reduction_readback(
                    original_model,projected_initial['parameters'],projected_initial,trace=trace,baseline=baseline)
            with model.context('fresh-persistent-high-precision-initial-state'):
                state=model.evaluate(p)
            status['initial']=model.description(state)
            J=status['initial']['complete_three_by_nine_forward_response']
            status['initial_original_three_equation_merit']=k.merit(state)
            status['phase']='initial-full-nine-curvature-and-independent-second-column-checks'
            checkpoint()
            with model.context('initial/complete-nine-second-forward'):
                j2,h2,hr,hs=model.curvature(p,label='initial-all-nine-second-forward')
            status['initial_ambient_curvature']=hr
            status['initial_second_primal_words_equal']=hs['equation']==state['equation']
            status['initial_second_J_minus_first_J']=[[x-y for x,y in zip(a,b)] for a,b in zip(j2,J)]
            status['initial_second_axis_difference_checks']=[]
            model.second_difference_checks(p,h2,'initial/second-axis-FD',
                status['initial_second_axis_difference_checks'],checkpoint)
            status['phase']='decimal50-complete-residual-quadratic-square-search'
            checkpoint()
            state,radius=solver.search(model,state,J,radius,status,checkpoint,outer_event)
            status['phase']='high-precision-and-declared-projection-final-diagnostics'
            checkpoint()
            status['final']=model.description(state)
            p=list(state['parameters'])
            status['phase']='final-full-nine-curvature-and-independent-second-column-checks'
            checkpoint()
            with model.context('final/complete-nine-second-forward'):
                j2,h2,hr,hs=model.curvature(p,label='final-all-nine-second-forward')
            status['final_ambient_curvature']=hr
            status['final_second_primal_words_equal']=hs['equation']==state['equation']
            jf=status['final']['complete_three_by_nine_forward_response']
            status['final_second_J_minus_first_J']=[[x-y for x,y in zip(a,b)] for a,b in zip(j2,jf)]
            status['final_second_axis_difference_checks']=[]
            model.second_difference_checks(p,h2,'final/second-axis-FD',
                status['final_second_axis_difference_checks'],checkpoint)
            status['initial_and_final_second_axis_checks_completed']=True
            status['final_relative_trust_radius']=radius
            status['final_original_three_equation_merit']=k.merit(state)
            status['high_precision_original_unit_stopping_tolerance_met']=k.maxabs(state['equation'])<=k.TOL
            status['high_precision_full112_linear_right_tolerance_met']=k.maxabs(state['full_right'])<=k.TOL
            projected_final,projection_final=projection(p,'final-projection')
            status['final_original_binary64_projection']=projection_final
            q=projected_final['parameters']
            specification=family.scalar_spec(profile,prepared['complete_scalar_profile']['complete_original_port'],
                                            q,INPUTS['accepted'])
            status['binary64_projection_scalar_family_sha256']=family.canonical_sha(specification)
            status['complete_scalar_domain_at_binary64_projection']=family.scalar_domain(
                profile,specification,args.out,args.interval_bits,args.interval_depth)
            status['original_complete_circle_check_at_binary64_projection']=family.complete_reference_check(
                original_model,projected_final,profile,flow,boundary,args.out,prepared,INPUTS['prepared'])
            status['binary64_projection_original_unit_stopping_tolerance_met']=bool(
                np.max(abs(projected_final['equation']))<=1e-8)
            status['binary64_projection_full112_linear_right_tolerance_met']=bool(
                np.max(abs(projected_final['full_right']))<=1e-8)
            status.update(phase='diagnostic-completed',diagnostic_completed=True,
                last_accepted_parameters=p,original_unit_stopping_tolerance_met=
                    status['high_precision_original_unit_stopping_tolerance_met'],
                low_mode_candidate_has_small_full_recorded_right_residual=
                    status['high_precision_full112_linear_right_tolerance_met'],
                original54_FD_checks_and_high_precision54_FD_checks_completed=True,
                final_scalar_and_453_circle_checks_applied_to_binary64_projection_only=True,
                finite_high_precision_circle_collocation_domain_rechecked_at_every_trial=True,
                high_precision_full_continuous_scalar_or_full453_domain_certified=False,
                high_mode_nonresonance_or_interval_transversality_proved=False,
                nonzero_field_completed=False,success=False)
            status['restart_recipe']=dict(schema=DECIMAL_RECIPE_SCHEMA,
                literal_parameters=k.clean(p),algorithm_state=dict(relative_trust_radius=k.clean(radius)),
                exploration_policy=EXPLORATION_POLICY,
                next_exploration_radius_is_explicit_new_strategy_not_silent_carry=True,
                input_sha256=INPUTS,family=parent.FAMILY_IDENTITY,
                precision=dict(decimal_digits=50,rounding='ROUND_HALF_EVEN',
                               parameter_encoding='finite-decimal-strings'),
                origin_must_be_completed_with_actual_run_source_status_and_primary_identity=True,
                this_record_alone_is_not_a_ready_parent_recipe=True)
        return 0
    except ResourceStopped as error:
        status.update(phase='resource-partial',resource_partial=True,
            exception=repr(error),traceback=traceback.format_exc(),
            scientific_completion_not_claimed=True)
        return 75
    except Exception as error:
        status.update(phase='exception',exception=repr(error),traceback=traceback.format_exc(),
            scientific_completion_not_claimed=True)
        raise
    finally:
        if trace is not None:
            trace.close()
            status['original_projection_call_trace']=trace.report()
            status['original_projection_call_trace'].update(
                used_only_for_declared_binary64_projection_consumers=True,
                original_model_method_returns_or_acceptance_rules_modified=False,
                not_the_high_precision_search_primal_or_response=True)
        if model is not None:
            status['high_precision_call_counts']=dict(model.counts)
        ledger.close()
        status['high_precision_call_ledger']=dict(file=ledger_path.name,bytes=ledger_path.stat().st_size,
            sha256=ledger_hash.hexdigest(),events=ledger_count,
            all_events_are_same_primal_model_calls=True,
            raw_call_ledger_not_retained_after_scalar_readout=True)
        status['seconds']=time.monotonic()-started
        status['complete_original_outer_direction_count']=len(status['searches'])
        status['unvisited_outer_direction_indices']=list(range(len(status['searches']),8))
        checkpoint()
        for signum,handler in old_signals.items():
            signal.signal(signum,handler)
        print(k.encoded(dict(event='request157-producer-final-status',schema=SCHEMA,
            phase=status['phase'],diagnostic_completed=status['diagnostic_completed'],
            resource_partial=status['resource_partial'],source_sha256=sources[ENTRY],
            status_file=STATUS_NAME,status_bytes=status_path.stat().st_size,
            status_sha256=sha(status_path),original_Armijo_accepted_point_count=
                status.get('original_Armijo_accepted_point_count'),
            actual_persistent_parameters=status.get('current_persistent_parameters'),
            actual_radius=status.get('current_relative_trust_radius'),
            final_parameters=status.get('final',{}).get('parameters'),
            final_radius=status.get('final_relative_trust_radius'),
            native_nonlinear_solver_called=False,success=False)).decode('ascii'),flush=True)


if __name__=='__main__':
    raise SystemExit(main())
