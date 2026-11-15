#!/usr/bin/env python3
"""Lower one fixed metric target while preserving a fixed actual-curvature cap.

All actual geometry remains in the unchanged physical family. Coarse/fine
values are complete; selected fine curvature derivatives use complete two
jets on uniform angular circles, not isolated angular queries.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import hashlib
from pathlib import Path
import time
import numpy as np
import scipy
from scipy.optimize import linprog

from frame_collar_residual_audit import digest
from frame_height_affine_gate import EvaluationBudgetReached, require_public_research_environment
from frame_metric_epigraph import geometry_values, metric_rows
from frame_curvature_epigraph_exchange import (GROUPS, POSITION_JETS, candidate_decision,
    curvature_forms)
from frame_curvature_soc_steps import SOCObjective
from frame_curvature_soc_arc_steps import parabolic_candidate, curvature_arc_slack_bound
from frame_curvature_soc_metric_reserve import implementation_hashes as previous_hashes
import frame_metric_budget_restoration_rows as rows_api

POLICY = 'fixed-hard-curvature-two-grid-metric-budget-recovery-v1'


def implementation_hashes():
    result = previous_hashes(); result.update(rows_api.implementation_hashes())
    p = Path(__file__); result[p.name] = hashlib.sha256(p.read_bytes()).hexdigest()
    return result


def configuration(base, *, target='13/50', curvature_cap='58', artificial_io=False):
    origin=Q(base['fixed_metric_budget_exact'])
    if artificial_io and origin>=1:
        # The published artificial report-chain fixture has deliberately loose
        # metric=100000. Preserve that declared artificial IO family only.
        # The actual 19-input path never enables this branch.
        target=str(origin*Q(9,10))
        cfg=copy.deepcopy(base)
        cfg.update(metric_restoration_schema=rows_api.SCHEMA,
            previous_qualified_metric_budget_exact=str(origin),fixed_metric_budget_exact=target,
            fixed_hard_curvature_cap_exact=str(Q(curvature_cap)),
            metric_recovery_group_indices=[0,1],hard_group_indices=list(range(2,11)),
            metric_recovery_row_roles=list(rows_api.ROLES),
            hard_curvature_uses_complete_actual_position_two_jets=True,
            fine_hard_curvature_requires_new_groups_7_to_10=True,
            only_constraint_definition_not_physical_g_or_state_changes=True,
            artificial_large_metric_budget_for_IO_only=True)
    else:
        cfg = rows_api.configuration(base, origin_budget_exact=base['fixed_metric_budget_exact'],
            target_budget_exact=target, curvature_cap_exact=curvature_cap)
    cfg.update(metric_recovery_policy=POLICY, fixed_curvature_target_exact=str(Q(curvature_cap)),
        curvature_target_schedule_exact=[str(Q(curvature_cap))],
        no_curvature_target_ladder_in_this_stage=True,
        optimizer_objective='metric-target row slack then small normalized step; curvature is hard',
        final_selection='last two-grid hard-cap eligible point with strictly decreasing true maximum eta',
        minimum_accepted_eta_decrease_exact='1/10000000',
        fine_initial_curvature_rows_per_radial_group=1,
        fine_initial_metric_rows_per_radial_branch=2,
        soft_goal_separation='target row below selected worst target slack, plus true eta peak pair',
        hard_fine_groups_use_original_tolerances_and_all_observed_violations=True,
        fine_group_order=list(GROUPS), fine_row_roles=list(rows_api.ROLES),
        SOC_metric_row_reserve_applied=False,
        prior_SOC_metric_floor_is_not_applied_to_new_soft_metric_rows=True,
        old_curvature_target55_is_history_not_this_fixed_hard_cap=True,
        unchanged_physical_g_b0_space_and_complete_value_grids=True)
    return cfg


def recovery_decision(problem, gate, state, data, lower, upper, cfg, *, forms=None):
    """Full physical decision; old-qualified and new-target metrics are separate."""
    cap = float(Q(cfg['fixed_hard_curvature_cap_exact']))
    scale = float(Q(cfg['curvature_scale_exact']))
    d = candidate_decision(problem, gate, state, cap/scale, data, lower, upper, cfg, forms=forms)
    values = geometry_values(data); origin = float(Q(cfg['previous_qualified_metric_budget_exact']))
    om, op = metric_rows(values['e'], values['f'], origin)
    old_pass = bool(min(float(np.min(om)), float(np.min(op))) >= -cfg['metric_row_tolerance']
        and d['direct_max_eta'] <= origin+cfg['direct_eta_tolerance'])
    hard = bool(d['physical_gate_pass_excluding_fixed_metric']
        and d['curvature_scaled_PSD_row_pass'] and d['independent_direct_curvature_pass']
        and d.get('regularity_screen_pass', False))
    d.update(previous_qualified_metric_budget_exact=cfg['previous_qualified_metric_budget_exact'],
        previous_metric_budget_pass=old_pass,
        previous_metric_row_minima=[float(np.min(om)), float(np.min(op))],
        metric_recovery_target_exact=cfg['fixed_metric_budget_exact'],
        new_metric_target_pass=bool(d['fixed_metric_budget_pass']),
        fixed_hard_curvature_cap_exact=cfg['fixed_hard_curvature_cap_exact'],
        single_grid_hard_gate_pass=hard,
        single_grid_admissible_recovery_point=bool(hard and old_pass),
        single_grid_new_target_qualified=bool(hard and d['fixed_metric_budget_pass']),
        curvature_auxiliary_is_fixed_not_a_state_or_solver_variable=True,
        two_grid_true_eta_decrease_is_an_additional_acceptance_condition=True)
    return d


def compact(d):
    names = ['single_grid_hard_gate_pass', 'previous_metric_budget_pass',
        'single_grid_admissible_recovery_point', 'single_grid_new_target_qualified',
        'new_metric_target_pass', 'direct_max_eta', 'direct_max_eta_location',
        'direct_maximum_absolute_principal_curvature', 'direct_max_curvature_location',
        'fixed_hard_curvature_cap_exact', 'metric_recovery_target_exact',
        'previous_qualified_metric_budget_exact', 'minimum_signed_height',
        'ball_radius_squared_normalized_max', 'maximum_absolute_y', 'inner_strip_absolute_margin',
        'direct_mirror_radius_min_finite', 'regularity_screen_pass', 'cap_and_box']
    return {k:copy.deepcopy(d[k]) for k in names if k in d}


def separation(rows, pool, tolerances, eta):
    """Hard violations versus a soft minimax envelope: not every negative goal row."""
    count = rows.shape[1]*rows.shape[2]
    ids = np.asarray(pool, np.int64); groups = ids//count
    selected_soft = rows.reshape(-1)[ids[groups < 2]]
    slack = max(0., float(np.max(-selected_soft))) if len(selected_soft) else 0.
    violating = rows < -np.asarray(tolerances)[:, None, None]
    violating[:2] = rows[:2] < -slack-float(np.max(np.asarray(tolerances)[:2]))
    peak = int(np.argmax(eta))
    goal_peak = np.zeros(rows.shape, bool)
    # A true eta maximum is also retained even when a different Schur row
    # defines the selected soft slack. It is not called a hard violation.
    goal_peak.reshape(11, -1)[:2, peak] = True
    missing = violating | goal_peak
    missing.reshape(-1)[ids] = False
    hard_missing = missing.copy(); hard_missing[:2] = False
    return missing, {'omitted_violating_count':int(np.count_nonzero(missing)),
        'omitted_hard_violating_count':int(np.count_nonzero(hard_missing)),
        'selected_soft_metric_slack':slack, 'true_eta_peak_point_index':peak,
        'soft_goal_rows_are_not_initial_hard_feasibility_requirements':True,
        'group_counts':{name:{'whole_grid':int(np.count_nonzero(violating[g])),
            'omitted':int(np.count_nonzero(missing[g]))} for g,name in enumerate(GROUPS)},
        'original_actual_tolerances':np.asarray(tolerances).tolist()}


class MetricRecoveryObjective(SOCObjective):
    """Reuse unchanged batched coarse jets and accepted-state cache ownership."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.recovery_events = []
        self.evaluation_definition.update(schema=POLICY+'-evaluation',
            metric_recovery_policy=POLICY, objective=self.cfg['optimizer_objective'],
            solver_parameter_count=self.n, fixed_hard_curvature_cap_exact=self.cfg['fixed_hard_curvature_cap_exact'],
            previous_qualified_metric_budget_exact=self.cfg['previous_qualified_metric_budget_exact'],
            new_metric_target_exact=self.cfg['fixed_metric_budget_exact'],
            constant_internal_zeta_is_never_optimized_or_in_physical_identity=True,
            group_roles=list(rows_api.ROLES),
            fine_selected_Jacobian_definition={
                'full_uniform_angular_nodes':len(self.fine_theta), 'group_order':list(GROUPS),
                'fine_flat_index_rule':'group*(Nr*Nfine)+radial_index*Nfine+fine_theta_index',
                'owned_radial_rows_per_batch':self.cfg['fine_Jacobian_owned_radial_rows'],
                'each_query_includes_original_radial_indices_0_and_last':True,
                'curvature_groups_request_complete_two_jet_parameter_Jacobian':True,
                'physical_only_batches_may_use_first_jet_request':True,
                'height_mean_and_height_primitive_evaluation_unchanged':True},
            implementation_source_sha256=implementation_hashes())
        for k in ['auxiliary_curvature_zeta_index', 'target_ladder_policy', 'mixed_grid_policy']:
            self.evaluation_definition.pop(k, None)
        family=self.gate.family
        context={'complete_metric_sha256':digest(family.get('complete_fixed_metric',family)),
            'fixed_b0_definition_sha256':digest(family.get('immutable_height_reference',family)),
            'physical_space_definition_sha256':digest(self.space),
            'height_gate_physical_sha256':self.gate.physical_sha256,
            'height_gate_numerical_sha256':self.gate.numerical_sha256,
            'geometry_evaluation_definition_sha256':digest(self.problem.evaluation_definition())}
        self.constraint_definitions={
            'coarse':rows_api.constraint_definition(self.cfg,context,self.radial,self.theta),
            'fine':rows_api.constraint_definition(self.cfg,context,self.radial,self.fine_theta)}
        self.evaluation_definition['constraint_definition_sha256']={
            k:v['definition_sha256'] for k,v in self.constraint_definitions.items()}
        self.evaluation_sha256 = digest(self.evaluation_definition)

    @property
    def fixed_zeta(self):
        return float(Q(self.cfg['fixed_hard_curvature_cap_exact']))/float(Q(self.cfg['curvature_scale_exact']))

    def vector(self, state):
        return np.r_[np.asarray(state, float), self.fixed_zeta]

    def _capture_coarse(self):
        cached = self.epigraph_cache
        if cached is None: return
        record = cached['record']; number = record['physical_geometry_evaluation']
        if number in self.saved_coarse_trials: return
        state = cached['vector'][:-1]
        self.saved_coarse_trials[number] = {
            'coarse_physical_evaluation':number, 'physical_state_sha256':digest(self.problem.identity(state)),
            'exact_binary64_physical_coefficients':[str(Q.from_float(float(x))) for x in state],
            'physical_parameter_coefficients_binary64':state.tolist(),
            'fixed_hard_curvature_cap_exact':self.cfg['fixed_hard_curvature_cap_exact'],
            'new_metric_target_exact':self.cfg['fixed_metric_budget_exact'],
            'decision':copy.deepcopy(record['decision'])}

    def evaluate(self, vector):
        vector = np.asarray(vector, float)
        if vector.shape != (self.n+1,) or not np.all(np.isfinite(vector)) or vector[-1] != self.fixed_zeta:
            raise ValueError('physical state followed only by the declared fixed internal curvature scale')
        self.assert_context(vector[:-1]); self._wall()
        if (self.epigraph_cache is not None and np.array_equal(vector, self.epigraph_cache['vector'])
                and self.geometry_cache is not None and np.array_equal(vector[:-1], self.geometry_cache['state'])):
            return self.epigraph_cache['record']
        data = self.physical_geometry(vector[:-1])
        decision = recovery_decision(self.problem,self.gate,vector[:-1],data,self.lower,self.upper,
            self.cfg,forms=data['curvature'])
        rows = self.rows_from_geometry(data,self.fixed_zeta)
        _,detail = separation(rows,self.pool,self.row_tolerances(),data['eta'])
        self.epigraph_evaluations += 1; now = time.monotonic()
        record = {'row_evaluation':self.epigraph_evaluations,
            'physical_geometry_evaluation':data['geometry_evaluation'], 'elapsed_seconds':now-self.total_started,
            'optimization_elapsed_seconds':None if self.optimization_started is None else now-self.optimization_started,
            'pool_version':self.pool_version,'pool_rows':len(self.pool),
            'whole_grid_and_pool_separation_at_this_same_trial':detail,'decision':decision}
        rows.setflags(write=False); self.history.append(record)
        self.epigraph_cache = {'vector':vector.copy(),'record':record,'rows':rows}
        self._capture_coarse()
        if self.checkpoint is not None and (
                self.geometry_evaluations-self.last_checkpoint_geometry >= self.cfg['checkpoint_physical_evaluations']
                or now-self.last_checkpoint >= self.cfg['checkpoint_seconds']):
            self.checkpoint(self.snapshot()); self.last_checkpoint=now
            self.last_checkpoint_geometry=self.geometry_evaluations
        self._wall(); return record

    def fine_decision(self, state):
        state = np.asarray(state,float); self.assert_context(state); self._wall()
        saved = self.accepted_cache
        if (saved is not None and np.array_equal(state,saved['state'])
                and (self.fine_cache is None or not np.array_equal(state,self.fine_cache['state']))):
            self.fine_cache = saved['fine']; d = saved.get('fine_derivatives')
            self.fine_derivative_cache = d if d is not None and d['pool_version']==self.fine_pool_version else None
            self.accepted_fine_cache_restores += 1
        if self.fine_cache is not None and np.array_equal(state,self.fine_cache['state']):
            return self.fine_cache['decision']
        if self.full_value_evaluations >= self.cfg['max_physical_evaluations']:
            raise EvaluationBudgetReached('shared coarse/fine value cap; last two-grid metric iterate retained')
        before=time.monotonic(); self.fine_evaluations += 1
        record={'fine_value_evaluation':self.fine_evaluations,
            'combined_value_evaluation':self.full_value_evaluations,
            'physical_state_sha256':digest(self.problem.identity(state)),
            'exact_binary64_physical_coefficients':[str(Q.from_float(float(x))) for x in state],
            'status':'doubled-angle-value-call-started'}
        self.saved_fine_trials.append(record)
        try:
            data=self.problem.geometry(state,self.radial,self.fine_theta,self.order,jacobian=False)
            for key in POSITION_JETS:
                if np.asarray(data[key]).shape != (len(self.radial),len(self.fine_theta),3) or not np.all(np.isfinite(data[key])):
                    raise FloatingPointError('finite complete fine two jets required: '+key)
            data['curvature']=curvature_forms(data,self.cfg)
            d=recovery_decision(self.problem,self.gate,state,data,self.lower,self.upper,self.cfg,forms=data['curvature'])
            val=geometry_values(data)
            data.update(e=val['e'],f=val['f'],eta=val['eta'])
            from frame_metric_epigraph_dense import mirror_values
            data['mirror_polynomial']=mirror_values(data,float(Q(self.cfg['mirror_target_exact'])))['polynomial']
            rows=self.rows_from_geometry(data,self.fixed_zeta); rows.setflags(write=False)
            self.fine_cache={'state':state.copy(),'data':data,'decision':d,'rows':rows}
            record.update(status='complete-doubled-angle-value-call',decision=copy.deepcopy(d))
        except Exception as error:
            record.update(status='failed-doubled-angle-value-call',
                error={'type':type(error).__name__,'message':str(error)})
            raise
        finally:
            record['elapsed_seconds']=time.monotonic()-before
            self.fine_value_seconds+=record['elapsed_seconds']
        self._wall(); return d

    def fine_rows(self,state):
        self.fine_decision(state); return self.fine_cache['rows']

    def set_fine_pool(self,indices,reason):
        raw=list(indices)
        if any(type(x) not in [int,np.int64,np.int32] for x in raw):
            raise ValueError('integer fine original-grid rows required')
        ids=np.asarray(sorted(set(int(i) for i in raw)),np.int64)
        total=11*len(self.radial)*len(self.fine_theta)
        if (not len(ids) or np.any(ids<0) or np.any(ids>=total)
                or len(ids)>self.cfg['max_fine_physical_pool_rows'] or not set(self.fine_pool).issubset(ids)):
            raise ValueError('full eleven-group fine pool must retain every old row within unchanged capacity')
        added=np.setdiff1d(ids,self.fine_pool); self.fine_pool=ids; self.fine_pool_version+=1
        self.fine_derivative_cache=None
        record={'version':self.fine_pool_version,'row_count':len(ids),'row_indices':ids.tolist(),
            'row_indices_sha256':digest(ids.tolist()),'added_row_indices':added.tolist(),
            'added_original_grid_coordinates':rows_api.fine_coordinates(added,self.radial,self.fine_theta),
            'group_order':list(GROUPS),'roles':list(rows_api.ROLES),'total_full_grid_rows':total,
            'flat_index_rule':'group*(Nr*Nfine)+radial_index*Nfine+fine_theta_index','reason':copy.deepcopy(reason)}
        self.fine_pool_history.append(record); return record

    def initialize_fine_pool(self,state,*,known_metric_locations=()):
        rows=self.fine_rows(state); Nr,Nt=rows.shape[1:]
        chosen=set(int(i) for i in self.fine_pool)
        for g in [0,1,7,8,9,10]:
            k=min(Nt,int(self.cfg['fine_initial_metric_rows_per_radial_branch'] if g<2
                else self.cfg['fine_initial_curvature_rows_per_radial_group']))
            worst=np.argsort(rows[g],axis=1,kind='stable')[:,:k]
            chosen.update((g*Nr*Nt+np.arange(Nr)[:,None]*Nt+worst).ravel().tolist())
        for loc in known_metric_locations:
            r=int(np.argmin(abs(self.radial-float(loc['t']))))
            t=int(np.argmin(abs(self.fine_theta-float(loc['theta']))))
            tol=128*np.finfo(float).eps*max(1.,abs(float(loc['t'])),abs(float(loc['theta'])))
            if abs(self.radial[r]-float(loc['t']))>tol or abs(self.fine_theta[t]-float(loc['theta']))>tol:
                raise ValueError('known peak must remain an exact original full-grid location')
            chosen.update(g*Nr*Nt+r*Nt+t for g in [0,1])
        return self.set_fine_pool(chosen,{'kind':'retain-old-seven-groups-and-add-complete-fine-curvature-minima',
            'metric_target_exact':self.cfg['fixed_metric_budget_exact'],
            'fixed_curvature_cap_exact':self.cfg['fixed_hard_curvature_cap_exact'],
            'legacy_row_ids_unchanged':True})

    def missing_rows(self,vector,*,callback_trigger=False):
        if callback_trigger: raise ValueError('no relaxed callback tolerance in metric restoration')
        rows=self.all_rows(vector)
        missing,detail=separation(rows,self.pool,self.row_tolerances(),self.geometry_cache['eta'])
        return rows,missing,detail

    def expand_pool(self,vector,reason):
        rows,missing,detail=self.missing_rows(vector)
        ids=np.flatnonzero(missing)
        if not len(ids):return None,detail
        if len(self.pool)+len(ids)>self.cfg['max_pool_rows']:
            detail.update(pool_capacity_would_be_exceeded=True,proposed_pool_rows=len(self.pool)+len(ids))
            return None,detail
        record=self.set_pool(np.r_[self.pool,ids],{'kind':reason,'whole_coarse_separation':detail,
            'all_observed_hard_violations_and_soft_envelope_witnesses_added':True})
        return record,detail

    def learn_fine_violations(self,state,reason):
        rows=self.fine_rows(state)
        missing,detail=separation(rows,self.fine_pool,self.row_tolerances(),self.fine_cache['data']['eta'])
        ids=np.flatnonzero(missing)
        if not len(ids):return None,detail
        if len(self.fine_pool)+len(ids)>self.cfg['max_fine_physical_pool_rows']:
            detail.update(pool_capacity_would_be_exceeded=True,proposed_pool_rows=len(self.fine_pool)+len(ids))
            return None,detail
        record=self.set_fine_pool(np.r_[self.fine_pool,ids],{'kind':reason,'whole_fine_separation':detail,
            'all_observed_hard_violations_and_soft_envelope_witnesses_added':True})
        return record,detail

    def fine_derivatives(self,state):
        self.fine_decision(state)
        if not len(self.fine_pool):raise ValueError('initialize full fine pool before derivatives')
        d=self.fine_derivative_cache
        if d is not None and d['pool_version']==self.fine_pool_version and np.array_equal(state,d['state']):
            return d['J']
        before=time.monotonic(); Nr,Nt=len(self.radial),len(self.fine_theta)
        groups=self.fine_pool//(Nr*Nt); points=self.fine_pool%(Nr*Nt)
        radial_ids=np.unique(points//Nt); J=np.empty((len(points),self.n)); covered=np.zeros(len(points),bool)
        width=int(self.cfg['fine_Jacobian_owned_radial_rows']); self.fine_Jacobian_refreshes+=1
        for start in range(0,len(radial_ids),width):
            self._wall(); owned=radial_ids[start:start+width]
            selected=np.flatnonzero(np.isin(points//Nt,owned)); query=np.unique(np.r_[0,owned,Nr-1])
            second=bool(np.any(groups[selected]>=7))
            data=self.problem.geometry(state,self.radial[query],self.fine_theta,self.order,
                jacobian=True,full_two_jet_jacobian=second)
            self.fine_Jacobian_batches+=1
            self.fine_Jacobian_maximum_query_radial_rows=max(self.fine_Jacobian_maximum_query_radial_rows,len(query))
            maximum=0.; scale=1.
            for key in POSITION_JETS+('center',):
                current=np.asarray(data[key]); target=np.asarray(self.fine_cache['data'][key])[query]
                if current.shape!=target.shape or not np.all(np.isfinite(current)):
                    raise FloatingPointError('fine batch ordinary replay: '+key)
                error=float(np.max(abs(current-target))); maximum=max(maximum,error)
                scale=max(scale,float(np.max(abs(target))))
                self.fine_batch_replay_maxima[key]=max(self.fine_batch_replay_maxima[key],error)
            for group in ['metric','height']:
                for key,target0 in self.fine_cache['data'].get(group,{}).items():
                    current=np.asarray(data[group][key]); target=np.asarray(target0)[query]
                    if current.shape!=target.shape or not np.all(np.isfinite(current)):
                        raise FloatingPointError('fine batch common primitive replay: '+group+'/'+key)
                    error=float(np.max(abs(current-target))); maximum=max(maximum,error)
                    scale=max(scale,float(np.max(abs(target))))
                    self.fine_batch_replay_maxima[group]=max(self.fine_batch_replay_maxima[group],error)
            if maximum>self.cfg['value_Jacobian_replay_relative_tolerance']*scale:
                raise ArithmeticError('batch changed same-state full ordinary two jets beyond floating replay tolerance')
            requested=POSITION_JETS if second else ('X','Xs','Xt','T')
            total=0
            for key in requested:
                jac=np.asarray(data['jac_'+key])
                if jac.shape!=(len(query),Nt,3,self.n) or not np.all(np.isfinite(jac)):
                    raise FloatingPointError('required complete fine parameter jet missing: '+key)
                total+=jac.nbytes
            self.fine_Jacobian_maximum_returned_bytes=max(self.fine_Jacobian_maximum_returned_bytes,total)
            ri=np.searchsorted(query,points[selected]//Nt); ti=points[selected]%Nt
            small={k:np.asarray(data[k])[ri,ti] for k in POSITION_JETS}
            small.update({'jac_'+k:np.asarray(data['jac_'+k])[ri,ti] for k in requested})
            J[selected]=rows_api.selected_parameter_jacobian(small,np.asarray(data['metric']['a'])[ri],
                groups[selected],self.gate.side,self.cfg)
            covered[selected]=True
            del data,small,jac
        if not np.all(covered) or not np.all(np.isfinite(J)):raise ArithmeticError('fine eleven-group Jacobian incomplete')
        J.setflags(write=False)
        self.fine_derivative_cache={'state':np.asarray(state).copy(),'pool_version':self.fine_pool_version,'J':J}
        self.fine_Jacobian_maximum_retained_bytes=max(self.fine_Jacobian_maximum_retained_bytes,J.nbytes)
        self.fine_Jacobian_seconds+=time.monotonic()-before; self._wall(); return J

    def accepted_point(self,state,coarse,fine,reason):
        if not(coarse['single_grid_admissible_recovery_point'] and fine['single_grid_admissible_recovery_point']):
            raise ValueError('both hard-curvature/physical and previously-qualified metric gates required')
        if (self.geometry_cache is None or not np.array_equal(state,self.geometry_cache['state'])
                or self.fine_cache is None or not np.array_equal(state,self.fine_cache['state'])):
            raise ArithmeticError('accepted point must own both actual full value caches')
        maximum=max(coarse['direct_max_eta'],fine['direct_max_eta'])
        if self.accepted_iterates and maximum>=self.accepted_iterates[-1]['maximum_eta_on_both_grids']:
            raise ValueError('recovery accepted sequence must strictly reduce actual two-grid eta')
        point={'accepted_index':len(self.accepted_iterates),'physical_state_sha256':digest(self.problem.identity(state)),
            'exact_binary64_physical_coefficients':[str(Q.from_float(float(x))) for x in state],
            'physical_parameter_coefficients_binary64':np.asarray(state).tolist(),
            'coarse':compact(coarse),'fine':compact(fine),'maximum_eta_on_both_grids':maximum,
            'maximum_curvature_on_both_grids':max(coarse['direct_maximum_absolute_principal_curvature'],
                fine['direct_maximum_absolute_principal_curvature']),
            'new_metric_target_qualified_on_both_grids':bool(coarse['single_grid_new_target_qualified']
                and fine['single_grid_new_target_qualified']),'reason':copy.deepcopy(reason)}
        self.accepted_iterates.append(point); dc=self.derivative_cache; df=self.fine_derivative_cache
        self.accepted_cache={'state':np.asarray(state).copy(),'coarse':self.geometry_cache,'fine':self.fine_cache,
            'coarse_derivatives':dc if dc is not None and np.array_equal(state,dc['state']) else None,
            'fine_derivatives':df if df is not None and np.array_equal(state,df['state']) else None}
        self._cache_size(); return point

    def snapshot(self):
        snap=super().snapshot()
        for key in ['best_physical_curvature_point','best_auxiliary_feasible_lambda_point',
                'best_auxiliary_feasible_curvature_point','lowest_lambda_trial_may_be_ineligible',
                'target_ladder_policy','curvature_target_schedule_exact','active_stage_index',
                'active_stage_target_exact','stage_events','cached_fine_target_rescorings_without_geometry']:
            snap.pop(key,None)
        snap.update(schema=POLICY+'-checkpoint',metric_recovery_policy=POLICY,
            fixed_hard_curvature_cap_exact=self.cfg['fixed_hard_curvature_cap_exact'],
            previous_qualified_metric_budget_exact=self.cfg['previous_qualified_metric_budget_exact'],
            new_metric_target_exact=self.cfg['fixed_metric_budget_exact'],
            group_order=list(GROUPS),group_roles=list(rows_api.ROLES),
            fine_all_eleven_groups_and_required_second_jet_Jacobians=True,
            constraint_definitions=copy.deepcopy(self.constraint_definitions),
            selected_point_rule='last actual two-grid hard-qualified state strictly decreasing true maximum eta',
            recovery_events=copy.deepcopy(self.recovery_events))
        return snap


def primary_proposal(values,J,groups,tolerances,state,lower,upper,cap_row,cap_margin,trust,cfg):
    values,J,groups,tolerances=np.asarray(values,float),np.asarray(J,float),np.asarray(groups,int),np.asarray(tolerances,float)
    state,lower,upper,cap_row=[np.asarray(x,float) for x in (state,lower,upper,cap_row)]
    n=len(state); m=len(values); soft=groups<2; hard=~soft
    if (J.shape!=(m,n) or groups.shape!=values.shape or tolerances.shape!=values.shape
            or np.any(groups<0) or np.any(groups>10) or not np.any(soft)
            or any(x.shape!=state.shape for x in [lower,upper,cap_row])
            or not all(np.all(np.isfinite(x)) for x in [values,J,tolerances,state,lower,upper,cap_row])
            or np.any(lower>=upper) or trust<=0 or not np.isfinite(cap_margin)):
        raise ValueError('finite complete fixed-cap metric-restoration linear model required')
    if np.any(values[hard]<-tolerances[hard]):
        raise ValueError('hard rows must be feasible at the accepted linearization point')
    scale=trust*(upper-lower); gamma=float(Q(cfg['linear_fraction_to_boundary_exact']))
    A=np.zeros((m+1+2*n,n+2)); b=np.empty(m+1+2*n)
    A[:m,:n]=-J*scale; b[:m]=values
    b[:m][hard]=gamma*(values[hard]+tolerances[hard]); A[:m,n][soft]=-1.
    A[m,:n]=-cap_row*scale; b[m]=cap_margin
    for j in range(n):
        A[m+1+j,j]=1.; A[m+1+j,n+1]=-1.
        A[m+1+n+j,j]=-1.; A[m+1+n+j,n+1]=-1.
    b[m+1:]=0.; lo=np.maximum(-1.,(lower-state)/scale); hi=np.minimum(1.,(upper-state)/scale)
    if np.any(lo>hi):raise ValueError('accepted point outside original box')
    c=np.zeros(n+2); c[n]=1.; c[n+1]=float(Q(cfg['linear_step_norm_weight_exact']))
    before=time.monotonic()
    r=linprog(c,A_ub=A,b_ub=b,bounds=list(zip(lo,hi))+[(0.,None),(0.,1.)],method='highs',
        options={'primal_feasibility_tolerance':cfg['linear_program_primal_tolerance'],
            'dual_feasibility_tolerance':cfg['linear_program_dual_tolerance'],'time_limit':cfg['linear_program_seconds']})
    rho0=max(0.,float(np.max(-values[soft])))
    report={'method':'HiGHS linear metric-target recovery; actual curvature rows hard',
        'success':bool(r.success),'status':int(r.status),'message':str(r.message),'nit':int(r.nit),
        'elapsed_seconds':time.monotonic()-before,'rows':len(b),'variables':n+2,'matrix_bytes':A.nbytes,
        'trust_fraction':trust,'initial_metric_slack':rho0,
        'hard_rows_count':int(hard.sum()),'soft_metric_rows_count':int(soft.sum()),
        'curvature_cap_and_physical_rows_and_cap_not_elastic':True}
    if r.x is None or not np.all(np.isfinite(r.x)):return None,report
    x=np.asarray(r.x); p=scale*x[:n]; violation=max(0.,float(np.max(A@x-b)))
    bv=max(0.,float(np.max(lo-x[:n])),float(np.max(x[:n]-hi)),-float(x[n]),-float(x[n+1]),float(x[n+1]-1))
    report.update(predicted_metric_slack=float(x[n]),predicted_slack_improvement=rho0-float(x[n]),
        normalized_step_norm=float(x[n+1]),maximum_linear_row_violation=violation,maximum_linear_bound_violation=bv,
        maximum_absolute_physical_step=float(np.max(abs(p))),physical_step_l2=float(np.linalg.norm(p)))
    if not r.success or max(violation,bv)>cfg['linear_model_residual_limit']:
        report['proposal_rejected_before_geometry']='LP status or independent linear residual'; return None,report
    return p,report


def correction_proposal(base,trial,J,groups,state,p,lower,upper,cap_row,cap_y,cfg):
    base,trial,J,groups=np.asarray(base,float),np.asarray(trial,float),np.asarray(J,float),np.asarray(groups,int)
    state,p,lower,upper,cap_row=[np.asarray(x,float) for x in (state,p,lower,upper,cap_row)]
    n=len(state); m=len(base); soft=groups<2; hard=~soft
    if (trial.shape!=base.shape or groups.shape!=base.shape or J.shape!=(m,n)
            or any(x.shape!=state.shape for x in [p,lower,upper,cap_row]) or not np.any(soft)
            or np.any(groups<0) or np.any(groups>10) or np.any(lower>=upper)
            or not all(np.all(np.isfinite(x)) for x in [base,trial,J,state,p,lower,upper,cap_row])
            or not np.isfinite(cap_y)):
        raise ValueError('same actual two-grid trial residuals and fixed accepted-state Jacobian required')
    width=upper-lower; norm=float(np.max(abs(p)/width)); linear=base+J@p
    rho0=max(0.,float(np.max(-base[soft]))); rho1=max(0.,float(np.max(-linear[soft])))
    gain=rho0-rho1; report={'initial_metric_slack':rho0,'primary_predicted_metric_slack':rho1,
        'primary_predicted_slack_improvement':gain,'primary_box_normalized_step_infinity_norm':norm,
        'residual_source':'actual same y on both full grids','Jacobian_source':'last accepted x',
        'hard_curvature_is_not_given_slack':True,'cap_and_box_use_y_plus_w':True}
    if norm==0 or gain<=cfg['linear_model_improvement_floor']:
        report['proposal_rejected_before_LP']='no primary predicted metric restoration'; return None,report
    gamma=float(Q(cfg['SOC_physical_margin_retention_exact']))
    retained=float(Q(cfg['SOC_predicted_descent_retention_exact']))
    radius=float(Q(cfg['SOC_maximum_correction_relative_to_proposed_step_exact']))*norm
    budget=rho0-retained*gain; target=gamma*np.maximum(base,0.)
    A=np.zeros((m+1+2*n,2*n)); b=np.empty(m+1+2*n); A[:m,:n]=-J*width
    # The retained budget comes from the primary prediction, but BOTH actual
    # residual blocks are now taken at the same y. This corrects nonlinear
    # metric curvature as well as the hard constraints.
    b[:m][hard]=trial[hard]-target[hard]; b[:m][soft]=trial[soft]+budget
    A[m,:n]=-cap_row*width; b[m]=cap_y
    for j in range(n):
        A[m+1+j,j]=1.; A[m+1+j,n+j]=-1.
        A[m+1+n+j,j]=-1.; A[m+1+n+j,n+j]=-1.
    b[m+1:]=0.; y=state+p
    lo=np.maximum(-radius,(lower-y)/width); hi=np.minimum(radius,(upper-y)/width)
    report.update(metric_slack_budget=budget,maximum_box_normalized_correction_infinity_norm=radius,
        hard_margin_retention=gamma,rows=len(b),variables=2*n,matrix_bytes=A.nbytes,
        metric_budget_applied_to_actual_trial_rows_plus_old_Jacobian_correction=True,
        selected_metric_actual_minus_primary_linear_minimum=float(np.min(trial[soft]-linear[soft])))
    if np.any(lo>hi):
        report['proposal_rejected_before_LP']='no correction in original box and relative radius';return None,report
    before=time.monotonic()
    r=linprog(np.r_[np.zeros(n),np.ones(n)],A_ub=A,b_ub=b,
        bounds=list(zip(lo,hi))+[(0.,radius)]*n,method='highs',
        options={'primal_feasibility_tolerance':cfg['linear_program_primal_tolerance'],
            'dual_feasibility_tolerance':cfg['linear_program_dual_tolerance'],'time_limit':cfg['linear_program_seconds']})
    report.update(LP_invoked=True,success=bool(r.success),status=int(r.status),message=str(r.message),
        nit=int(r.nit),elapsed_seconds=time.monotonic()-before)
    if r.x is None or not np.all(np.isfinite(r.x)):return None,report
    x=np.asarray(r.x); w=width*x[:n]
    violation=max(0.,float(np.max(A@x-b)))
    bv=max(0.,float(np.max(lo-x[:n])),float(np.max(x[:n]-hi)),float(np.max(-x[n:])),float(np.max(x[n:]-radius)))
    report.update(maximum_linear_row_violation=violation,maximum_linear_bound_violation=bv,
        maximum_absolute_correction=float(np.max(abs(w))),correction_l2=float(np.linalg.norm(w)),
        correction_box_normalized_infinity_norm=float(np.max(abs(w)/width)),
        correction_box_normalized_l1_norm=float(np.sum(abs(w)/width)),
        corrected_predicted_metric_slack=max(0.,float(np.max(-(linear+J@w)[soft]))),
        corrected_actual_trial_linear_metric_slack=max(0.,float(np.max(-(trial+J@w)[soft]))),
        basepoint_prediction_slack_is_only_for_parabolic_linear_bookkeeping=True,
        minimum_corrected_linear_hard_margin=float(np.min(trial[hard]+J[hard]@w)) if np.any(hard) else None,
        corrected_affine_cap_margin=float(cap_y+cap_row@w))
    if not r.success or max(violation,bv)>cfg['linear_model_residual_limit']:
        report['proposal_rejected_before_geometry']='SOC LP status or linear residual';return None,report
    return w,report


def run_recovery(objective,initial,*,known_metric_locations=(),artificial_inputs_only=False,evaluate_only=False):
    if objective.cfg.get('artificial_large_metric_budget_for_IO_only') and not (artificial_inputs_only and evaluate_only):
        raise ValueError('the loose predecessor fixture budget is only for artificial IO without LPs')
    if not artificial_inputs_only:require_public_research_environment()
    elif objective.gate.kind!='artificial-array' and not evaluate_only:
        raise ValueError('local nonlinear steps require the explicit artificial array family')
    cfg=objective.cfg
    meta={'method':POLICY,'new_metric_target_exact':cfg['fixed_metric_budget_exact'],
        'previous_qualified_metric_budget_exact':cfg['previous_qualified_metric_budget_exact'],
        'fixed_hard_curvature_cap_exact':cfg['fixed_hard_curvature_cap_exact'],
        'nonlinear_minimize_invocation_count':0,'linear_program_invocation_count':0,
        'primary_LP_invocation_count':0,'correction_LP_invocation_count':0,
        'shared_max_LPs':cfg['max_linear_models'],'shared_max_values':cfg['max_physical_evaluations'],
        'shared_active_seconds':cfg['max_seconds'],'models':[],
        'artificial_inputs_only':bool(artificial_inputs_only),'evaluate_only':bool(evaluate_only),
        'numpy_version':np.__version__,'scipy_version':scipy.__version__}
    def finish(status,error=None,budget=None):
        snap=objective.snapshot(); point=snap.get('selected_two_grid_physical_point')
        if objective.checkpoint:objective.checkpoint(snap)
        return {'status':status,'error':error,'budget_message':budget,'solver':meta,'checkpoint':snap,
            'new_metric_target_reached_on_both_grids':bool(point and point['new_metric_target_qualified_on_both_grids']),
            'no_free_curvature_or_metric_auxiliary_is_a_physical_coefficient':True}
    try:
        current=np.asarray(initial,float).copy(); vector=objective.vector(current)
        cd=objective.evaluate(vector)['decision']; fd=objective.fine_decision(current)
        if not(cd['single_grid_admissible_recovery_point'] and fd['single_grid_admissible_recovery_point']):
            return finish('initial-hard-curvature-or-prior-metric-physical-gate-failed')
        accepted=objective.accepted_point(current,cd,fd,{'kind':'saved-reserve-two-grid-success-metric-recovery-start'})
        if not len(objective.pool):objective.initialize_pool(vector)
        objective.expand_pool(vector,'initial-soft-metric-envelope-and-hard-coarse-separation')
        objective.initialize_fine_pool(current,known_metric_locations=known_metric_locations)
        if evaluate_only:return finish('evaluation-only-recovery-initialization')
        if accepted['new_metric_target_qualified_on_both_grids']:return finish('new-metric-target-already-qualified')
        objective.linear_rows(vector); objective.begin_optimization()
        trust=float(Q(cfg['initial_trust_box_fraction_exact']))
        minimum_trust=float(Q(cfg['minimum_trust_box_fraction_exact']))
        drop=float(Q(cfg['minimum_accepted_eta_decrease_exact']))
        while meta['linear_program_invocation_count']<cfg['max_linear_models']:
            objective._wall(); vector=objective.vector(current)
            base,J,groups,tols=objective.linear_rows(vector)
            versions=(objective.pool_version,objective.fine_pool_version)
            remaining=cfg['max_seconds']-(time.monotonic()-objective.optimization_started)
            local=dict(cfg,linear_program_seconds=min(cfg['linear_program_seconds'],max(.001,remaining)))
            p,lp=primary_proposal(base,J,groups,tols,current,objective.lower,objective.upper,objective.gate.row,
                objective.gate.intercept+float(objective.gate.row@current)-objective.gate.target,trust,local)
            meta['linear_program_invocation_count']+=1; meta['primary_LP_invocation_count']+=1
            model={'number':len(meta['models'])+1,'linearized_at_accepted_index':accepted['accepted_index'],
                'linearized_at_physical_sha256':accepted['physical_state_sha256'],
                'coarse_pool_rows':len(objective.pool),'fine_pool_rows':len(objective.fine_pool),
                'linear_program':lp,'trials':[],'corrections':[]}; meta['models'].append(model);objective._wall()
            if p is None:
                trust*=.5;model['result']='primary-LP-failed-trust-shrunk'
                if trust<minimum_trust:return finish('minimum-trust-after-primary-failure')
                continue
            if lp['predicted_slack_improvement']<=cfg['linear_model_improvement_floor'] or np.max(abs(p))==0:
                model['result']='no-primary-metric-restoration';return finish('metric-restoration-linear-model-stalled')
            model['exact_binary64_proposed_step']=[str(Q.from_float(float(x))) for x in p]
            old_eta=accepted['maximum_eta_on_both_grids']; succeeded=False; relearned=False; soc_used=False; arc=None
            def assess(candidate,kind,alpha,need_fine=False,curve=None):
                nonlocal current,accepted,succeeded,relearned
                record={'kind':kind,'alpha_exact':alpha,'accepted_as_next_iterate':False,
                    'exact_binary64_physical_coefficients':[str(Q.from_float(float(x))) for x in candidate],
                    'attempt_status':'coarse-value-call-started'}
                if curve is not None:record['parabolic_curve']=copy.deepcopy(curve)
                model['trials'].append(record)
                rv=objective.evaluate(objective.vector(candidate)); c=rv['decision']
                record.update(attempt_status='coarse-value-call-complete',
                    coarse_physical_evaluation=rv['physical_geometry_evaluation'],coarse_decision=compact(c))
                possible=c['direct_max_eta']<old_eta and (
                    old_eta-c['direct_max_eta']>=drop or c['single_grid_new_target_qualified'])
                f=None
                if c.get('regularity_screen_pass',False) and (need_fine or (possible and c['single_grid_admissible_recovery_point'])):
                    f=objective.fine_decision(candidate)
                    record.update(fine_value_evaluation=objective.fine_evaluations,fine_decision=compact(f),
                        actual_fine_evaluated_even_if_coarse_ineligible=not c['single_grid_admissible_recovery_point'])
                    maximum=max(c['direct_max_eta'],f['direct_max_eta'])
                    qualified=c['single_grid_new_target_qualified'] and f['single_grid_new_target_qualified']
                    if (c['single_grid_admissible_recovery_point'] and f['single_grid_admissible_recovery_point']
                            and maximum<old_eta and (old_eta-maximum>=drop or qualified)):
                        accepted=objective.accepted_point(candidate,c,f,{'kind':kind,'model':model['number'],
                            'alpha_exact':alpha,'previous_two_grid_maximum_eta':old_eta})
                        current=candidate.copy();succeeded=True
                        record.update(accepted_as_next_iterate=True,accepted_index=accepted['accepted_index'])
                added,detail=objective.expand_pool(objective.vector(candidate),'recovery-coarse-actual-hard-and-soft-envelope')
                record.update(coarse_omitted_rows=detail['omitted_violating_count'],
                    coarse_omitted_hard_rows=detail['omitted_hard_violating_count'],
                    new_coarse_rows=len(added['added_row_indices']) if added else 0)
                if detail.get('pool_capacity_would_be_exceeded'):
                    raise EvaluationBudgetReached('coarse row capacity; last accepted metric point retained')
                relearned=relearned or bool(added)
                if f is not None:
                    addf,detailf=objective.learn_fine_violations(candidate,'recovery-fine-hard-and-soft-envelope')
                    record.update(fine_omitted_rows=detailf['omitted_violating_count'],
                        fine_omitted_hard_rows=detailf['omitted_hard_violating_count'],
                        fine_violation_groups=detailf['group_counts'],
                        new_fine_rows=len(addf['added_row_indices']) if addf else 0)
                    if detailf.get('pool_capacity_would_be_exceeded'):
                        raise EvaluationBudgetReached('fine row capacity; last accepted metric point retained')
                    relearned=relearned or bool(addf)
                return c,f,record
            for bi in range(int(cfg['maximum_backtracks_per_model'])):
                alpha=str(Q(1,2**bi)); step=float(Q(alpha))*p
                may_soc=arc is None and not soc_used and meta['linear_program_invocation_count']<cfg['max_linear_models']
                if arc is None:y=current+step;kind='primary-metric-short-step';curve=None
                else:
                    y,curve=parabolic_candidate(current,p,arc['w'],alpha,arc['reference_alpha_exact'])
                    curve.update(correction_index=arc['correction_index'],
                        linear_metric_slack_upper_bound=curvature_arc_slack_bound(
                            arc['initial'],arc['primary'],arc['corrected'],float(Q(curve['curve_fraction_exact']))))
                    kind='metric-SOC-parabolic-backtrack'
                c,f,trial=assess(y,kind,alpha,may_soc,curve)
                if succeeded:model['result']='accepted-two-grid-true-metric-descent';break
                if relearned:model['result']='new-rows-return-to-last-accepted-before-SOC';break
                if may_soc and f is not None and c.get('regularity_screen_pass',False) and f.get('regularity_screen_pass',False):
                    soc_used=True
                    if versions!=(objective.pool_version,objective.fine_pool_version):
                        raise ArithmeticError('SOC old Jacobian cannot survive pool layout change')
                    trial_rows=np.r_[objective.constraint_fun(objective.vector(y)),
                        objective.fine_rows(y).reshape(-1)[objective.fine_pool]]
                    remaining=cfg['max_seconds']-(time.monotonic()-objective.optimization_started)
                    local=dict(cfg,linear_program_seconds=min(cfg['linear_program_seconds'],max(.001,remaining)))
                    w,soc=correction_proposal(base,trial_rows,J,groups,current,step,objective.lower,objective.upper,
                        objective.gate.row,objective.gate.intercept+float(objective.gate.row@y)-objective.gate.target,local)
                    if soc.get('LP_invoked'):
                        meta['linear_program_invocation_count']+=1;meta['correction_LP_invocation_count']+=1
                    correction={'primary_trial_index':len(model['trials'])-1,
                        'primary_trial_physical_sha256':digest(objective.problem.identity(y)),
                        'coarse_residual_evaluation':trial['coarse_physical_evaluation'],
                        'fine_residual_evaluation':trial['fine_value_evaluation'],
                        'coarse_pool_version':versions[0],'fine_pool_version':versions[1],'linear_program':soc}
                    model['corrections'].append(correction);objective._wall()
                    if w is not None:
                        correction['exact_binary64_correction']=[str(Q.from_float(float(x))) for x in w]
                        arc={'w':w.copy(),'reference_alpha_exact':alpha,'correction_index':len(model['corrections'])-1,
                            'initial':soc['initial_metric_slack'],'primary':soc['primary_predicted_metric_slack'],
                            'corrected':soc['corrected_predicted_metric_slack']}
                        assess(y+w,'metric-SOC-corrected-short-step',alpha)
                        if succeeded:model['result']='accepted-full-SOC-two-grid-metric-descent';break
                        if relearned:model['result']='corrected-new-rows-return-to-last-accepted';break
            if succeeded and accepted['new_metric_target_qualified_on_both_grids']:
                return finish('fixed-new-metric-target-qualified-on-both-grids')
            if not succeeded and not relearned:
                trust*=.5;model['result']='all-proposals-rejected-last-accepted-retained'
                if trust<minimum_trust:return finish('minimum-trust-after-SOC-and-backtracking')
            if objective.checkpoint:objective.checkpoint(objective.snapshot())
        return finish('shared-primary-plus-SOC-LP-budget-exit')
    except EvaluationBudgetReached as error:
        return finish('shared-value-time-or-pool-budget-exit',budget=str(error))
    except Exception as error:
        return finish('metric-recovery-error',error={'type':type(error).__name__,'message':str(error)})


def developer_check():
    """New roles, full fine curvature chain, cache/whole-grid acceptance only."""
    from frame_curvature_epigraph_exchange import _CurvatureArrayProblem
    from frame_height_affine_gate import HeightAffineGate
    from frame_curvature_soc_steps import configuration as old_cfg
    initial=np.array([.3,.6,.6]); radial=np.array([0.,.2,.4,.7,1.]); theta=np.arange(12)*2*np.pi/12
    lower=np.array([-.8,-1.,-1.]); upper=np.array([2.,1.,1.])
    def make(changes=None):
        p=_CurvatureArrayProblem()
        cfg=configuration(old_cfg(),target='1/100',curvature_cap='3')
        cfg.update(radial_Jacobian_batch_owned_rows=2,fine_Jacobian_owned_radial_rows=2,
            max_seconds=20.,initial_trust_box_fraction_exact='1/1000')
        if changes:cfg.update(changes)
        return MetricRecoveryObjective(p,HeightAffineGate.from_artificial_array_problem(p),
            radial,theta,3,lower,upper,cfg=cfg)
    obj=make(); vector=obj.vector(initial)
    cd=obj.evaluate(vector)['decision']; fd=obj.fine_decision(initial)
    oldcount=len(radial)*len(obj.fine_theta); oldids=np.array([0,oldcount+3,2*oldcount+5,6*oldcount+8])
    obj.set_fine_pool(oldids,{'kind':'artificial-legacy-seven-group-pool'})
    obj.initialize_pool(vector); obj.initialize_fine_pool(initial)
    ids=obj.fine_pool.copy(); rows,J,groups,tols=obj.linear_rows(vector)
    retained=set(oldids).issubset(ids)
    direction=np.array([.2,-.3,.4]); eps=1e-6
    def values_at(x):
        return np.r_[obj.constraint_fun(obj.vector(x)),obj.fine_rows(x).reshape(-1)[obj.fine_pool]]
    numerical=(values_at(initial+eps*direction)-values_at(initial-eps*direction))/(2*eps)
    error=float(np.max(abs(numerical-J@direction)))
    obj.evaluate(vector);obj.fine_decision(initial);obj.linear_rows(vector)
    calls=obj.problem.calls; obj.linear_rows(vector)
    reuse=obj.problem.calls==calls
    obj.accepted_point(initial,obj.evaluate(vector)['decision'],obj.fine_decision(initial),{'kind':'artificial'})
    saved_calls=obj.full_value_evaluations
    trial=initial.copy();trial[0]+=.001
    obj.evaluate(obj.vector(trial));obj.fine_decision(trial)
    after_trial=obj.full_value_evaluations
    obj.evaluate(vector);obj.fine_decision(initial)
    rollback=obj.full_value_evaluations==after_trial and after_trial==saved_calls+2
    metadata_same=obj.problem.identity(initial)==make().problem.identity(initial)
    two_jet_group_present=bool(np.any(ids//oldcount>=7) and obj.fine_Jacobian_maximum_query_radial_rows<=4)
    # Initial target failure is admissible only because previous budget and all
    # hard gates pass; it is not silently called a new-target success.
    separated=bool(cd['single_grid_admissible_recovery_point'] and fd['single_grid_admissible_recovery_point']
        and not cd['single_grid_new_target_qualified'] and not fd['single_grid_new_target_qualified'])
    bad_data=copy.deepcopy(obj.fine_cache['data']);bad_data['Xss']*=10
    bad=recovery_decision(obj.problem,obj.gate,initial,bad_data,lower,upper,obj.cfg)
    hard_curvature=bool(not bad['single_grid_hard_gate_pass'] and not bad['single_grid_admissible_recovery_point'])
    synthetic=np.ones((11,1,4));synthetic[:2]=-.01
    synthetic[9,0,3]=-2e-9
    missing,detail=separation(synthetic,np.array([0,4]),np.full(11,1e-9),np.array([[.04,.03,.02,.01]]))
    soft_not_all=bool(not missing[:2].any() and missing[9,0,3] and detail['omitted_hard_violating_count']==1)
    cfg=make().cfg
    base=np.array([-.1,.001]); jac=np.eye(2); labels=np.array([0,7]); state=np.array([0.,.001])
    lo=np.full(2,-2.); hi=-lo; p=np.array([.1,-.0005])
    y=state+p
    trialrows=np.array([base[0]+p[0]-6*p[0]**2,y[1]*(1-y[0])-y[0]**2])
    w,cr=correction_proposal(base,trialrows,jac,labels,state,p,lo,hi,np.array([0.,1.]),y[1],cfg)
    soc_role=bool(w is not None and cr['hard_curvature_is_not_given_slack']
        and trialrows[1]+w[1]>=float(Q(cfg['SOC_physical_margin_retention_exact']))*.001-1e-12
        and trialrows[0]+w[0]+cr['metric_slack_budget']>=-1e-12
        and w[0]>.0099
        and cr['corrected_actual_trial_linear_metric_slack']<=cr['metric_slack_budget']+1e-12)
    arc,_=parabolic_candidate(state,p,w,'1/2','1')
    arc_hard=float(arc[1]*(1-arc[0])-arc[0]**2)
    arc_pass=bool(arc_hard>=0 and cr['maximum_linear_row_violation']<1e-8)
    run_obj=make({'max_linear_models':2}); run=run_recovery(run_obj,initial,artificial_inputs_only=True)
    points=run['checkpoint']['accepted_iterates']
    monotone=all(b['maximum_eta_on_both_grids']<a['maximum_eta_on_both_grids'] for a,b in zip(points,points[1:]))
    all_hard=all(p['coarse']['single_grid_admissible_recovery_point'] and p['fine']['single_grid_admissible_recovery_point'] for p in points)
    # A fine value failure after a coarse proposal must keep the saved initial
    # state, and its consumed value call must remain in the shared count.
    fail=make({'max_linear_models':2}); original=fail.fine_decision
    def injected(x):
        if fail.accepted_iterates and not np.array_equal(x,initial):
            fail.fine_evaluations+=1
            raise FloatingPointError('artificial recovery fine-value failure')
        return original(x)
    fail.fine_decision=injected
    failed=run_recovery(fail,initial,artificial_inputs_only=True)
    kept=bool(failed['status']=='metric-recovery-error' and len(failed['checkpoint']['accepted_iterates'])==1
        and failed['checkpoint']['selected_two_grid_physical_point']['physical_parameter_coefficients_binary64']==initial.tolist())
    passed=bool(error<1e-7 and retained and reuse and rollback and metadata_same and two_jet_group_present
        and separated and hard_curvature and soft_not_all and soc_role and arc_pass
        and monotone and all_hard and len(points)>1 and kept
        and run['solver']['linear_program_invocation_count']<=2
        and run['checkpoint']['total_full_value_physical_evaluations']<=cfg['max_physical_evaluations'])
    return {'schema':POLICY+'-artificial-check','artificial_inputs_only':True,
        'research_candidate_geometry_evaluated_or_optimized':False,
        'full_mixed_selected_parameter_Jacobian_max_error':error,
        'legacy_fine_indices_preserved':retained,'full_fine_curvature_rows_and_batches':two_jet_group_present,
        'same_derivative_cache_reused':reuse,'same_accepted_value_cache_rollback_does_not_recompute':rollback,
        'physical_identity_unchanged_by_constraint_definition':metadata_same,
        'initial_goal_failure_not_confused_with_hard_failure':separated,
        'better_metric_cannot_bypass_hard_curvature':hard_curvature,
        'soft_envelope_not_all_negative_goals_and_hard_fine_violation_added':soft_not_all,
        'role_reversed_SOC_linear_inequalities_pass':soc_role,'SOC_curve_toy_hard_boundary_pass':arc_pass,
        'SOC_toy_report':cr,'actual_toy_accepted_eta_strictly_decreases':monotone,
        'actual_toy_accepted_points_pass_both_hard_grids':all_hard,
        'failed_fine_trial_keeps_last_accepted':kept,
        'toy_status':run['status'],'toy_error':run['error'],
        'toy_counts':{k:v for k,v in run['solver'].items() if k.endswith('invocation_count')},
        'toy_accepted_eta':[p['maximum_eta_on_both_grids'] for p in points],'passed':passed}
