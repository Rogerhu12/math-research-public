#!/usr/bin/env python3
"""Solve the R643 complete free-mean system under the unchanged actual397 E.

All1472 prior angular columns and94 actual mean columns, all original
position rows plus the real F/rG rows. Full-row QR/SVD, no mean elimination,
same true accepted seed and all inherited costs. Work automatically advances
to the original full fine grid. Public-only science, hourly actual rules pull.
"""
import argparse
from collections import defaultdict
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time
from types import SimpleNamespace

import numpy as np

HERE = Path(__file__).resolve().parent
SCHEMA = 'r643-actual397-complete-coupled-mean-same-E-solve-v1'
BINDINGS = {
    'legacy':('r618_actual397_fourier_centered_20261128.py',
              'a024487d792f39d2f4620835900a07c3a4ccd5eb9a8dfc149a51c45d82814994'),
    'model':('r643_complete_mean_height_model_20261128.py','91944d7298d81952a28c09b416db1242d5d913fc43b8d19ea97fbab5c38b8185'),
    'tail':('r643_complete_mean_tail_bounds_20261128.py','4cc0d0430efb6815806a6a1ba04a58067c5c5dc7e3efcb124aae9547c184c47a'),
    'consumers':('r643_complete_mean_consumers_20261128.py','d00141559ee66da018ef1aaec263517de3fc396311f2325d9d0720e9ee2177ca')}
COUNTS,REJECTIONS = defaultdict(int),defaultdict(int)


def emit(tag,value):
    print('R643_COUPLED_'+tag+' '+json.dumps(value,sort_keys=True,separators=(',',':'),
                                            allow_nan=False),flush=True)


def sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
                                     allow_nan=False).encode()).hexdigest()


def load(label):
    filename,digest = BINDINGS[label]
    path = HERE/filename
    if hashlib.sha256(path.read_bytes()).hexdigest()!=digest:
        raise ValueError('actual coupled source changed: '+filename)
    name = 'r643_actual_'+label
    spec = importlib.util.spec_from_file_location(name,path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class RuleChange(Exception):
    pass


class SolverReserve(Exception):
    pass


class Rules:
    def __init__(self,request_path):
        self.request = json.loads(Path(request_path).read_text())
        path = HERE/'run_inverse_state_stdin_20261126.py'
        relative = str(path.relative_to(Path.cwd()))
        if hashlib.sha256(path.read_bytes()).hexdigest()!=self.request['source_sha256'][relative]:
            raise ValueError('the actual public pull implementation differs')
        spec = importlib.util.spec_from_file_location('r643_actual_hourly_rule_pull',path)
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)
        self.source = os.environ['GITHUB_SHA']
        self.last = time.monotonic()
        self.receipts = []
        self.failed = False

    def check(self):
        if self.failed:
            raise RuleChange('new science remains stopped after changed rules or failed pull')
        now = time.monotonic()
        if now-self.last<3300:
            return
        row = {'actual_public_pull_and_both_README_exact_differences':True,
               'seconds_since_last_check':now-self.last,
               'private_hourly_pull_owned_by_active_parent':self.request['queue_session']}
        self.receipts.append(row)
        try:
            row['after_pull_commit'] = self.module.public_pull(Path.cwd(),self.request,self.source)
            row['status'] = 'unchanged_rules_continue_same_actual_source'
        except Exception as exc:
            self.failed = True
            row['status'] = 'changed_rules_or_pull_failure_stop_old_scope'
            row['failure_type'] = type(exc).__name__
        finally:
            # Even when a rule changed, restore the pinned files solely so
            # the old scope can serialize its real state/costs. No further
            # science is allowed on that branch.
            try:
                self.module.git(Path.cwd(),'checkout','--detach',self.source)
                row['pinned_source_restored_for_complete_actual_state_receipt'] = True
            except Exception as exc:
                self.failed = True
                row['source_restore_failure_type'] = type(exc).__name__
            self.last = time.monotonic()
            emit('HOURLY_RULES',row)
        if self.failed:
            raise RuleChange('apply the printed README differences before any new scientific scope')


def function_limit(model,response,direction,data,state,maximum_change):
    combined = model.combined_direction(response,direction,data,state)
    changes = {'relative_b':0.,'relative_u':0.,'relative_N':0.,
               'relative_turning_normalization':0.,'actual_height':0.,
               'actual_p_over_one_plus_sqrt_E':0.}
    worst = {'quantity':None,'ratio':0.}
    for i,r in enumerate(data['r']):
        model.check()
        dmean = combined['mean_jets'][i]
        dm = model.chain.direction(state['mean_states'][i],
              {key:value[i,:,None] for key,value in combined['canonical_jets'].items()},
              np.asarray([dmean[1]]),np.asarray([dmean[2]]),canonical_mean=True)
        ds = model.chain.direction(state['output_states'][i],
              {key:value[i,:,None] for key,value in combined['output_jets'].items()},
              np.asarray([dmean[1]]),np.asarray([dmean[2]]))
        current = state['output_states'][i]
        for name,key in (('relative_b','b'),('relative_u','u'),('relative_N','N')):
            ratios = abs(ds[key][:,0])/current[key]
            at = int(np.argmax(ratios));value = float(ratios[at])
            changes[name] = max(changes[name],value)
            if value>worst['ratio']:
                worst = {'quantity':name,'ratio':value,'r':float(r),
                         'theta':float(data['theta'][at]),
                         'actual_direction':float(ds[key][at,0]),
                         'actual_positive_denominator':float(current[key][at])}
        value = float(abs(dm['F'][0])/state['mean_states'][i]['A'])
        changes['relative_turning_normalization'] = max(changes['relative_turning_normalization'],value)
        if value>worst['ratio']:
            worst = {'quantity':'relative_turning_normalization','ratio':value,
                     'r':float(r),'actual_direction':float(dm['F'][0]),
                     'actual_positive_denominator':float(state['mean_states'][i]['A'])}
        height_change = abs(combined['output_jets']['f'][i]+dmean[0])
        hv = float(np.max(height_change))
        changes['actual_height'] = max(changes['actual_height'],hv)
        if hv>worst['ratio']:
            at = int(np.argmax(height_change))
            worst = {'quantity':'actual_height','ratio':hv,'r':float(r),
                     'theta':float(data['theta'][at]),'physical_height_unit':1.}
        pv = float(np.max(abs(ds['p'][:,0]))/(1+np.sqrt(current['E'])))
        changes['actual_p_over_one_plus_sqrt_E'] = max(changes['actual_p_over_one_plus_sqrt_E'],pv)
        if pv>worst['ratio']:
            at = int(np.argmax(abs(ds['p'][:,0])))
            worst = {'quantity':'actual_p_over_one_plus_sqrt_E','ratio':pv,'r':float(r),
                     'theta':float(data['theta'][at]),'actual_direction':float(ds['p'][at,0]),
                     'actual_positive_denominator':float(1+np.sqrt(current['E']))}
    largest = max(changes.values())
    if not np.isfinite(largest):
        raise ArithmeticError('complete actual coupled physical direction is not finite')
    factor = min(1.,maximum_change/largest) if largest>0 else 1.
    COUNTS['actual_complete_physical_direction_limits'] += 1
    return factor,{'factor':factor,'actual_physical_changes':changes,'actual_attainer':worst,
                   'lambda_or_inverse_c0_constraint_used':False,
                   'nonlinear_or_continuous_domain_certificate':False}


class CoupledRun:
    def __init__(self,incoming,args,modules,started):
        self.incoming,self.args,self.modules = incoming,args,modules
        self.started = started
        self.deadline = started+args.maximum_seconds
        self.solver_deadline = self.deadline-args.final_reserve_seconds
        self.rules = Rules(args.request_path)
        self.attempts,self.history,self.failure_history = [],[],[]
        self.model,self.owned,self.current,self.response,self.tail = None,None,None,None,None
        self.record,self.pending,self.last_trial,self.readout,self.partial_readout = None,None,None,None,None
        self.accepted = 0
        self.damping = float(incoming['solver']['initial_damping'])
        self.last_spectrum = None
        legacy = modules['legacy']
        self.previous = legacy.bound_import('previous')
        self.driver,self.identity_module = [self.previous.bound_import(k) for k in ('original','identity')]
        oldtext = incoming['preceding_centered_scope_stdin_JSON']
        oldargs = SimpleNamespace(source_state_json=oldtext,
                         source_state_sha256=incoming['preceding_centered_scope_stdin_sha256'])
        self.old_input,self.source,self.identity,_,self.older_final = legacy.read_input(
            oldargs,self.previous,self.identity_module,modules['model'].centered)
        terminal = incoming['preceding_centered_natural_terminal']
        if (hashlib.sha256(terminal['literal_FINAL_JSON'].encode()).hexdigest()
                !=modules['model'].SEED_FINAL_SHA):
            raise ValueError('same naturally completed centered run required')
        self.seed_final = json.loads(terminal['literal_FINAL_JSON'])

    def check(self,solver=False):
        self.driver.check(self.deadline)
        self.rules.check()
        if solver and time.monotonic()>=self.solver_deadline:
            raise SolverReserve('declared reserve for same-state full fine/direct/mean-height readout')

    def checkpoint(self,label):
        data,state = self.current
        report = self.modules['consumers'].complete_observation(self.model,self.response,data,state)
        self.record = {
            'label':label,'actual_response':self.response.tolist(),
            'response_identity':self.previous.response_identity(self.response),
            'joint_model_sha256':self.model.model_sha256,
            'same_frozen_target_sha256':self.identity.target_sha256,
            'actual_new_accepted_steps':self.accepted,'actual_next_damping':self.damping,
            'last_complete_field_observation':report,'hard_tau':1.}
        emit('CHECKPOINT',self.record)
        return report

    def goal(self,state,target):
        return (state['conditional_eta_identity_observation']<=target
                and float(np.max(abs(state['F'])))<=target
                and float(np.max(abs(self.current[0]['r']*state['G'])))<=target)

    def solve_current_grid(self,target,label):
        params = self.incoming['solver']
        for iteration in range(int(params['maximum_iterations_per_grid'])):
            self.check(solver=True)
            data,state = self.current
            if self.goal(state,target):
                self.checkpoint(label+'_finite_target_observed')
                return 'finite_target_observed'
            rows,columns = len(state['residual']),self.model.nq
            if rows*columns>int(params['maximum_materialized_J_entries']):
                raise MemoryError('declared full same-E J exceeds its explicit materialized range')
            COUNTS['complete1566_J_attempts'] += 1
            J = self.model.jacobian(self.response,data,state)
            COUNTS['complete1566_J_completed'] += 1
            self.check()
            factor = self.driver.factorization.CompleteRowFactor(
                J,state['residual'],batch_rows=4096,deadline_check=self.check)
            del J
            self.last_spectrum = factor.spectrum()
            emit('FULL_SPECTRUM',{'grid':label,'iteration':iteration,'spectrum':self.last_spectrum})
            base_merit = float(state['residual']@state['residual']/2)
            accepted = False
            for dtrial in range(int(params['damping_trials'])):
                self.check(solver=True)
                damping = self.damping*10.**dtrial
                direction = factor.direction(damping)
                limit,measures = function_limit(self.model,self.response,direction,data,state,
                                                float(params['maximum_relative_function_step']))
                emit('DIRECTION',{'grid':label,'iteration':iteration,'damping_trial':dtrial,
                                  'damping':damping,'function_measures':measures})
                for cut in range(int(params['line_search_cuts'])):
                    self.check(solver=True)
                    fraction = limit*2.**(-cut)
                    proposed = self.response+fraction*direction
                    predicted = factor.predicted_decrease(direction,fraction)
                    self.pending = {'grid':label,'iteration':iteration,'damping_trial':dtrial,
                                    'cut':cut,'fraction':fraction,'predicted_decrease':predicted,
                                    'actual_proposed_response':proposed.tolist(),
                                    'actual_proposed_response_identity':self.previous.response_identity(proposed)}
                    COUNTS['actual_coupled_nonlinear_trials_attempted'] += 1
                    reason = 'no_resolvable_full_coupled_decrease'
                    try:
                        candidate_tail = self.tail.evaluate(proposed)
                        candidate = self.model.evaluate(proposed,data)
                        merit = float(candidate['residual']@candidate['residual']/2)
                        actual = base_merit-merit
                        ratio = actual/predicted if predicted>0 else -1.
                        resolvable = max(64*np.finfo(float).eps*max(base_merit,1e-30),1e-36)
                        okay = bool(predicted>0 and actual>resolvable and ratio>1e-4)
                        self.last_trial = {key:value for key,value in self.pending.items()
                                           if key!='actual_proposed_response'}
                        self.last_trial.update(accepted=okay,actual_decrease=actual,
                                               actual_merit=merit,actual_over_predicted=ratio)
                    except (ArithmeticError,FloatingPointError,self.driver.base.DomainError) as exc:
                        okay = False;reason = type(exc).__name__+':'+str(exc)
                        self.last_trial = {key:value for key,value in self.pending.items()
                                           if key!='actual_proposed_response'}
                        self.last_trial.update(accepted=False,failure=reason)
                    self.pending = None
                    if okay:
                        self.response,self.current = proposed,(data,candidate)
                        self.damping = max(1e-14,damping/3)
                        self.accepted += 1
                        COUNTS['actual_full_coupled_steps_accepted'] += 1
                        self.history.append({'grid':label,'iteration':iteration,
                            'actual_new_accepted_step':self.accepted,'actual_response_sha256':sha(proposed.tolist()),
                            'actual_merit':merit,'actual_decrease':actual,'actual_over_predicted':ratio,
                            'next_damping':self.damping})
                        emit('ACCEPTANCE',{**self.history[-1],'function_measures':measures,
                                           'actual_true_tail_bound':candidate_tail})
                        self.checkpoint('accepted_complete_'+label+'_coupled_decrease')
                        accepted = True
                        break
                    COUNTS['actual_coupled_nonlinear_trials_rejected'] += 1
                    REJECTIONS[reason] += 1
                if accepted:
                    break
            if not accepted:
                self.checkpoint(label+'_finite_space_no_resolvable_step')
                return 'no_resolvable_full_coupled_step_on_this_grid'
        return 'declared_full_grid_iteration_range_used'

    def execute(self):
        model_module = self.modules['model']
        self.owned = model_module.centered.FourierCenteredHeight.restore_from_frozen_reference(
            self.driver,self.source['actual_1130q_JSON'],self.source['amplitude'],
            self.identity,self.old_input['maximum_independent_mode'],
            self.old_input['numerical_and_response_policy'],deadline=self.deadline,attempts=self.attempts)
        self.model = model_module.CompleteMeanHeight(self.owned,
            np.asarray(self.seed_final['actual_response']),self.incoming['preceding_centered_natural_terminal'],
            self.incoming['coupled_model_policy'],safe_point=self.rules.check)
        self.response = self.model.initial_response()
        data = self.model.prepare(self.model.original_work_radii,256)
        contract = self.previous.conditional_source_contract(
            self.owned,SimpleNamespace(producer=self.modules['tail'].paid))
        self.tail = self.modules['tail'].CompleteMeanTail(
            self.model,data,self.incoming['preceding_centered_natural_terminal'],contract[0],contract[1])
        emit('TRUE_TAIL_SOURCE_CONTRACT',{'literal_JSON':contract[0],'sha256':contract[1],
                                        'same_unresolved_original_source_errors_retained':True})
        initial_tail = self.tail.evaluate(self.response)
        state = self.model.evaluate(self.response,data)
        self.current = (data,state)
        self.checkpoint('same_real_accepted_seed_embedded_in_complete1566_system')
        emit('INITIAL_TRUE_TAIL',initial_tail)
        work_status = self.solve_current_grid(float(self.incoming['solver']['work_eta_target']),'work')
        # A work stall does not end the objective; the complete original fine
        # equations are the next declared stage of the SAME fixed metric.
        self.check(solver=True)
        fine = self.model.prepare(self.model.original_fine_radii,512)
        fine_state = self.model.evaluate(self.response,fine)
        self.current = (fine,fine_state)
        self.checkpoint('same_current_response_on_all_original_fine_points')
        fine_status = self.solve_current_grid(float(self.incoming['solver']['fine_eta_target']),'fine')
        return {'work_status':work_status,'fine_status':fine_status}

    def complete_readout(self):
        if self.model is None or self.response is None:
            return None
        self.check()
        data,state = self.current if self.current is not None else (None,None)
        is_paid_fine = (data is not None and state is not None
            and len(data['theta'])==512 and np.array_equal(data['r'],self.model.original_fine_radii)
            and np.array_equal(state['response'],self.response))
        if is_paid_fine:
            COUNTS['already_paid_complete_fine_states_reused'] += 1
        else:
            data = self.model.prepare(self.model.original_fine_radii,512)
            state = self.model.evaluate(self.response,data)
            self.current = (data,state)
        report = self.modules['consumers'].complete_observation(self.model,self.response,data,state)
        self.partial_readout = {'stage':'complete_original_fine_joint_state','fine':report}
        fields = self.model.coefficient_fields(self.response,data,state)
        D = np.stack([s['D'] for s in state['output_states']])
        Dfft = np.fft.rfft(D,axis=1)/len(data['theta'])
        tail_source = self.owned.exact_tail_source_observation(data)
        coefficients = {
            'pre_tanh_threejet_max_by_mode':np.max(abs(fields['pre_tanh_threejet_coefficients']),axis=0).tolist(),
            'all_post_modes':fields['all_post_modes'].tolist(),
            'all_post_threejet_max_by_mode':np.max(abs(fields['all_post_tanh_threejet_coefficients']),axis=0).tolist(),
            'actual_explicit_mean_change_threejet_max':np.max(abs(fields['actual_explicit_mean_change_threejets']),axis=0).tolist(),
            'all_D_harmonics_through_output_Nyquist_max':np.max(abs(Dfft),axis=0).tolist(),
            'all_true_tail_L_j_max_by_mode_and_degree':np.max(abs(tail_source['L_j_columns']),axis=0).tolist(),
            'original_source_errors_not_assigned_zero':fields['unresolved_errors'],
            'mean_root_and_derivative_error_category_applies_to_fixed_seed_only':True,
            'new_F_G_position_and_radial_errors_unresolved':True,
            'whole_continuous_or_README_certificate':False}
        self.partial_readout.update(coefficient_observations=coefficients)
        height_report = self.modules['consumers'].complete_actual_mean_height(
            self.model,self.response,data,state,self.tail.seed_anchor)
        self.partial_readout.update(stage='complete_fine_coefficients_and_real_mean_height',
                                    actual_mean_height=height_report)
        direct_report = self.modules['consumers'].two_actual_position_stencils(
            self.model,self.response,data,state,query_block_radii=128)
        passed = (self.goal(state,float(self.incoming['solver']['fine_eta_target']))
            and all(direct_report[key]['direct_reconstructed_metric_eta']<=float(self.incoming['solver']['fine_eta_target'])
                    for key in ('direct_step','direct_half_step')))
        self.readout = {'fine':report,'coefficient_observations':coefficients,
            'actual_mean_height':height_report,'actual_position_double_readout':direct_report,
            'actual_true_tail':self.tail.evaluate(self.response),
            'complete_finite_same_E_observations_passed':bool(passed),
            'source_continuous_uniform_inverse_macro_and_README_certified':False}
        self.partial_readout = {'stage':'all_declared_actual_readouts_complete','complete':self.readout}
        emit('COMPLETE_READOUT',self.readout)
        return self.readout


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-state-json',required=True)
    parser.add_argument('--source-state-sha256',required=True)
    parser.add_argument('--request-path',required=True)
    parser.add_argument('--maximum-seconds',type=float,default=18000.)
    parser.add_argument('--final-reserve-seconds',type=float,default=6000.)
    args = parser.parse_args()
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise RuntimeError('new coupled scientific computation belongs to this public Actions scope')
    raw = sys.stdin.buffer.read() if args.source_state_json=='@stdin' else args.source_state_json.encode()
    if hashlib.sha256(raw).hexdigest()!=args.source_state_sha256:
        raise ValueError('complete actual coupled input bytes differ')
    incoming = json.loads(raw)
    if (incoming['schema']!=SCHEMA
            or not 0<args.final_reserve_seconds<args.maximum_seconds<=19800):
        raise ValueError('declared same-E coupled scientific range differs')
    started = time.monotonic()
    modules = {key:load(key) for key in BINDINGS}
    run = CoupledRun(incoming,args,modules,started)
    emit('DEFINITION',{'schema':SCHEMA,'complete_actual_input':incoming,
        'source_state_sha256':args.source_state_sha256,'source_bound_components':BINDINGS,
        'all_free_columns':1566,'work_position_plus_F_G_rows':123500,
        'same_original_work950_N256_fine1728_N512':True,
        'same_frozen_E_H_amplitude_and_hard_tau1':True,
        'actual_mean_unknown_not_new_trial_scalar_roots':True,
        'hourly_actual_public_pull_and_double_README_differences':True,
        'old_independent_gates_replayed':False,'continuous_or_README_claim':False,
        'arguments':{key:value for key,value in vars(args).items() if key!='source_state_json'}})
    failure,status = None,'genuine_joint_seed_not_yet_reconstructed'
    try:
        status = run.execute()
    except SolverReserve as exc:
        status = 'declared_solver_reserve_actual_coupled_checkpoint'
        failure = {'type':type(exc).__name__,'message':str(exc)}
    except Exception as exc:
        status = 'actual_coupled_rule_clock_or_numerical_failure_retained'
        failure = {'type':type(exc).__name__,'message':str(exc)}
        emit('FAILURE',failure)
    if run.current is not None and not run.rules.failed:
        try:
            run.complete_readout()
        except Exception as exc:
            run.failure_history.append({'attempt':'complete_actual_fine_mean_height_and_double_position_readout',
                'failure_type':type(exc).__name__,'message':str(exc),'all_partial_work_retained':True})
    costs = None
    if run.model is not None:
        try:
            costs = run.model.cumulative_cost_receipt()
        except Exception as exc:
            run.failure_history.append({'attempt':'complete_model_cost_serialization','failure_type':type(exc).__name__})
            costs = {'new_mean_model_counts':dict(run.model.counts),
                     'new_explicit_chain_counts':dict(run.model.chain.counts),
                     'serialization_guard_failure_does_not_erase_partial_work':True}
    final = {
        'schema':SCHEMA,'status':status,'failure':failure,'elapsed_seconds':time.monotonic()-started,
        'same_frozen_target_sha256':run.identity.target_sha256,
        'actual_response':None if run.response is None else run.response.tolist(),
        'actual_response_identity':None if run.response is None else run.previous.response_identity(run.response),
        'actual_current_checkpoint':run.record,'actual_next_damping':run.damping,
        'actual_new_accepted_steps':run.accepted,
        'pending_trial_not_accepted':run.pending,'last_actual_trial':run.last_trial,
        'accepted_history':run.history,'last_complete_full_spectrum':run.last_spectrum,
        'complete_final_readout':run.readout,'partial_readout':run.partial_readout,
        'failed_attempts_and_partial_readouts':run.failure_history,
        'new_actual_model_costs':costs,
        'original_reconstruction_attempts':run.driver.full.attempt_receipts(run.attempts),
        'original_costs_including_incomplete_reconstruction':run.previous.original_costs(run.driver),
        'new_scope_counts':dict(COUNTS),'full_row_QR_SVD_counts':dict(run.driver.factorization.COUNTS),
        'new_mean_tail_counts':dict(modules['tail'].COUNTS),
        'new_mean_consumer_counts':dict(modules['consumers'].COUNTS),
        'actual_stencil_helper_counts':dict(modules['consumers'].direct.COUNTS),
        'new_owned_reference_and_fixed_seed_root_receipts':modules['model'].centered.root_attempt_receipts(),
        'hourly_actual_public_rules_pull_receipts':run.rules.receipts,'rejections':dict(REJECTIONS),
        'preceding_centered_natural_terminal_identity':{key:value for key,value in
            incoming['preceding_centered_natural_terminal'].items() if key!='literal_FINAL_JSON'},
        'preceding_centered_complete_actual_receipt_not_counted_as_new':run.seed_final,
        'older_reference_cost_ledger_not_counted_as_new':run.source['source_cost_ledger'],
        'older_prior_cost_ledgers_not_counted_as_new':run.source['prior_cost_ledgers'],
        'overlapping_cost_counters_and_inherited_ledgers_not_disjoint':True,
        'same_fixed_E_near_cap_all_rows_and_all1566_columns_retained':True,
        'no_trial_W_or_c0_division_or_mean_root':True,
        'true_seed_branch_existence_and_source_errors_not_promoted_to_certificates':True,
        'current_small_core_not_claimed_to_meet_macro_completion':True,
        'uniform_infinite_band_C2_embedding_reach_and_README_certified':False,
        'raw_scientific_arrays_artifacts_releases_or_git_writes':False}
    literal = json.dumps(final,sort_keys=True,separators=(',',':'),allow_nan=False)
    print('R643_COUPLED_FINAL '+literal,flush=True)
    emit('FINAL_IDENTITY',{'JSON_bytes':len(literal.encode()),
                           'sha256':hashlib.sha256(literal.encode()).hexdigest()})


if __name__=='__main__':
    main()
