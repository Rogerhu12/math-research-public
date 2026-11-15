#!/usr/bin/env python3
"""One declared fine-initialization allowance per stage; no geometry or solver.

The unchanged eleven-group initializer adds at most the integer bound recorded
here. This is an algorithm-resource configuration change, not a physical model
change or a relaxation of any sampled gate. Development runs only on Actions.
"""
from __future__ import annotations
import copy
import hashlib
import json
from pathlib import Path
import numpy as np

POLICY='height159-fine-initialization-one-structural-reserve-v1'
HISTORY_KEY='fine_initialization_capacity_reservations'
CAP_KEY='max_fine_physical_pool_rows'
STAGE_KEYS=('capacity-height159-input-production','capacity-SOC-hold')
INITIALIZER_REASON='retain-old-seven-groups-and-add-complete-fine-curvature-minima'


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
        ensure_ascii=False,allow_nan=False).encode()).hexdigest()


def implementation_hashes():
    p=Path(__file__)
    return {p.name:hashlib.sha256(p.read_bytes()).hexdigest()}


def _integer(value,label,*,positive=False):
    if type(value) not in (int,np.int64,np.int32):
        raise ValueError(label+' must be an integer, not a rounded value or bool')
    value=int(value)
    if value<(1 if positive else 0):raise ValueError(label+' is outside its declared range')
    return value


def _original_ids(indices,total):
    ids=[_integer(i,'original fine row ID') for i in indices]
    if not ids or ids!=sorted(set(ids)) or ids[-1]>=total:
        raise ValueError('nonempty sorted unique original eleven-group fine IDs required')
    return ids


def reserve_initialization(cfg,indices,Nr,Nt,known_metric_locations,stage_key):
    """Copy cfg and add one structural allowance without evaluating any field.

    No call site in a model/learning loop uses this function. The sequence guard
    rejects repeat reservations and limits this driver to the two named stages.
    """
    Nr=_integer(Nr,'radial count',positive=True);Nt=_integer(Nt,'fine angle count',positive=True)
    if stage_key not in STAGE_KEYS:raise ValueError('unknown capacity-production stage')
    C=_integer(cfg[CAP_KEY],'inherited fine capacity',positive=True)
    km=_integer(cfg['fine_initial_metric_rows_per_radial_branch'],'metric rows per radius')
    kc=_integer(cfg['fine_initial_curvature_rows_per_radial_group'],'curvature rows per radius')
    ids=_original_ids(indices,11*Nr*Nt)
    if len(ids)>C:raise ValueError('inherited pool already exceeds its declared capacity')
    locations=copy.deepcopy(list(known_metric_locations))
    for loc in locations:
        if not isinstance(loc,dict) or not all(k in loc for k in ('t','theta')):
            raise ValueError('recorded metric locations require their original t/theta fields')
        if not all(np.isfinite(float(loc[k])) for k in ('t','theta')):
            raise ValueError('recorded metric locations must be finite')
    history=copy.deepcopy(cfg.get(HISTORY_KEY,[]))
    if not isinstance(history,list) or any(not isinstance(r,dict) for r in history):
        raise ValueError('capacity reservation history must be a list of records')
    if [r.get('stage_key') for r in history]!=list(STAGE_KEYS[:STAGE_KEYS.index(stage_key)]):
        raise ValueError('exactly one ordered capacity reservation per declared stage')
    if history and history[-1].get('new_fine_capacity')!=C:
        raise ValueError('the second stage must inherit the first stage capacity unchanged')
    metric_bound=2*Nr*min(Nt,km);curvature_bound=4*Nr*min(Nt,kc)
    peak_bound=2*len(locations);B=metric_bound+curvature_bound+peak_bound
    record={'schema':POLICY,'stage_key':stage_key,'ordinal':len(history)+1,
        'inherited_configuration_sha256':digest(cfg),'inherited_fine_capacity':C,
        'inherited_fine_row_count':len(ids),'inherited_fine_row_indices_sha256':digest(ids),
        'inherited_learning_slots':C-len(ids),'radial_count':Nr,'fine_angular_count':Nt,
        'full_group_count':11,'full_original_grid_row_count':11*Nr*Nt,
        'metric_rows_per_radial_branch':km,'curvature_rows_per_radial_group':kc,
        'known_metric_location_count':len(locations),'known_metric_locations_sha256':digest(locations),
        'metric_seed_upper_bound':metric_bound,'curvature_seed_upper_bound':curvature_bound,
        'known_peak_seed_upper_bound':peak_bound,'total_initialization_upper_bound':B,
        'formula':'Nr*(2*min(Nt,k_metric)+4*min(Nt,k_curvature))+2*len(known_metric_locations)',
        'new_fine_capacity':C+B,'minimum_learning_slots_after_initializer':C-len(ids),
        'one_selected_159_column_binary64_J_additional_upper_bound_bytes':B*159*8,
        'memory_formula_is_not_a_peak_RSS_bound':True,
        'all_original_integer_row_IDs_preserved':True,
        'fixed_stage_capacity_no_automatic_learning_loop_expansion':True,
        'geometry_gates_physical_definition_trust_and_optimization_budgets_unchanged':True,
        'algorithm_resource_configuration_changes_and_can_change_numerical_trajectory':True}
    new=copy.deepcopy(cfg);new[CAP_KEY]=C+B;new[HISTORY_KEY]=history+[record]
    changed={k for k in set(cfg)|set(new) if cfg.get(k)!=new.get(k)}
    if changed-{CAP_KEY,HISTORY_KEY}:raise AssertionError('capacity adapter changed another configuration key')
    receipt=copy.deepcopy(record);receipt['executed_configuration_sha256']=digest(new)
    return new,receipt


def initialization_diagnostic(stage,cfg,reservation):
    """Read the already recorded initialization; never rerun selection or values.

    If the original stage stopped before recording the union, leave it unknown.
    A recorded inconsistency is reported explicitly, not repaired or reclassified.
    """
    stage=stage if isinstance(stage,dict) else {}
    checkpoint=stage.get('checkpoint',{})
    checkpoint=checkpoint if isinstance(checkpoint,dict) else {}
    histories=checkpoint.get('fine_physical_row_pool_history',[])
    histories=histories if isinstance(histories,list) else []
    selected=[r for r in histories if isinstance(r,dict) and
        isinstance(r.get('reason'),dict) and r['reason'].get('kind')==INITIALIZER_REASON]
    result={'schema':POLICY+'-existing-initialization-diagnostic',
        'stage_key':reservation['stage_key'],'reservation':copy.deepcopy(reservation),
        'executed_configuration_sha256':digest(cfg),'stage_status':stage.get('status'),
        'stage_error':copy.deepcopy(stage.get('error')),'stage_budget_message':stage.get('budget_message'),
        'recorded_fine_pool_history_count':len(histories),'initializer_record_count':len(selected),
        'initializer_union_available':bool(selected),'no_new_values_geometry_or_row_selection':True}
    if not selected:
        result.update(contract_pass=None,
            unavailable_reason='the original initializer did not record a returned union; no attempted count is inferred')
        return result
    errors=[]
    if len(selected)!=1:errors.append('initializer was recorded more than once')
    record=selected[0];ids=record.get('row_indices');before=histories[0] if histories else {}
    original=before.get('row_indices') if isinstance(before,dict) else None
    try:
        Nr=reservation['radial_count'];Nt=reservation['fine_angular_count'];total=11*Nr*Nt
        ids=_original_ids(ids,total);original=_original_ids(original,total)
    except (TypeError,ValueError) as error:
        result.update(contract_pass=False,contract_errors=errors+[str(error)])
        return result
    if digest(cfg)!=reservation['executed_configuration_sha256']:errors.append('executed configuration hash differs')
    if cfg.get(CAP_KEY)!=reservation['new_fine_capacity']:errors.append('stage capacity differs')
    if digest(original)!=reservation['inherited_fine_row_indices_sha256']:errors.append('first recorded original pool differs')
    if len(original)!=reservation['inherited_fine_row_count']:errors.append('inherited pool size differs')
    if not set(original).issubset(ids):errors.append('original IDs missing')
    if record.get('row_count')!=len(ids) or record.get('row_indices_sha256')!=digest(ids):
        errors.append('recorded union row count/hash differs')
    added=sorted(set(ids)-set(original));remaining=cfg[CAP_KEY]-len(ids)
    if len(added)>reservation['total_initialization_upper_bound']:errors.append('initializer exceeded its structural bound')
    if remaining<reservation['inherited_learning_slots']:errors.append('inherited learning headroom was lost')
    size=Nr*Nt
    result.update(actual_union_row_count=len(ids),actual_union_row_indices_sha256=digest(ids),
        actual_added_unique_rows=len(added),actual_added_rows_by_original_group=[sum(i//size==g for i in added) for g in range(11)],
        all_inherited_IDs_retained=bool(set(original).issubset(ids)),
        remaining_learning_slots_after_initialization=remaining,
        inherited_learning_slots_preserved=bool(remaining>=reservation['inherited_learning_slots']),
        contract_pass=not errors,contract_errors=errors)
    return result


def developer_check():
    """Only new capacity fixtures, using the real old array initializer/setter.

    No objective constructor, surface, geometry, Jacobian or LP is called.
    This entry is first executed by the public Actions lane, never locally.
    """
    from frame_metric_budget_recovery import MetricRecoveryObjective as Original
    class ArrayFixture:
        set_fine_pool=Original.set_fine_pool
        initialize_fine_pool=Original.initialize_fine_pool
        learn_fine_violations=Original.learn_fine_violations
        def __init__(self,cfg,Nr=3,Nt=8):
            self.cfg=copy.deepcopy(cfg);self.radial=np.arange(Nr,dtype=float)
            self.fine_theta=np.arange(Nt)*2*np.pi/Nt;self.fine_pool=np.array([],np.int64)
            self.fine_pool_version=0;self.fine_pool_history=[];self.fine_derivative_cache=None
            self.rows=np.zeros((11,Nr,Nt));self.fine_cache={'data':{'eta':np.zeros((Nr,Nt))}}
        def fine_rows(self,state):return self.rows
        def row_tolerances(self):return np.zeros(11)
    cfg={CAP_KEY:6,'fine_initial_metric_rows_per_radial_branch':2,
        'fine_initial_curvature_rows_per_radial_group':1,'fixed_metric_budget_exact':'13/50',
        'fixed_hard_curvature_cap_exact':'58','minimum_trust_box_fraction_exact':'1/128000',
        'max_LP_invocations':12,'unchanged_guard_fixture':{'radius':0.00003125,'streak':1}}
    old_ids=[0,24,96,240];locations=[{'t':2.,'theta':float(7*2*np.pi/8)}]
    frozen=copy.deepcopy(cfg);saved_ids=old_ids.copy();saved_locations=copy.deepcopy(locations)
    old=ArrayFixture(cfg);old.set_fine_pool(old_ids,{'kind':'inherited-fixture'})
    old_failure=False
    try:old.initialize_fine_pool(None,known_metric_locations=locations)
    except ValueError as error:
        old_failure='within unchanged capacity' in str(error)
    new_cfg,first=reserve_initialization(cfg,old_ids,3,8,locations,STAGE_KEYS[0])
    new=ArrayFixture(new_cfg);new.set_fine_pool(old_ids,{'kind':'inherited-fixture'})
    union=new.initialize_fine_pool(None,known_metric_locations=locations)
    diagnostic=initialization_diagnostic({'status':'artificial-initialized','checkpoint':{
        'fine_physical_row_pool_history':new.fine_pool_history}},new_cfg,first)
    union_ok=bool(diagnostic['contract_pass'] and union['row_count']>cfg[CAP_KEY]
        and diagnostic['remaining_learning_slots_after_initialization']>=cfg[CAP_KEY]-len(old_ids))
    rejected={}
    for name,bad in [('negative',[-1]+old_ids),('outside',old_ids+[11*3*8]),('removed-old',old_ids[1:])]:
        fixture=ArrayFixture(new_cfg);fixture.set_fine_pool(old_ids,{'kind':'inherited-fixture'})
        try:fixture.set_fine_pool(bad,{'kind':'bad-fixture'});rejected[name]=False
        except ValueError:rejected[name]=True
    bad_peak=False
    try:new.initialize_fine_pool(None,known_metric_locations=[{'t':0.125,'theta':0.}])
    except ValueError as error:bad_peak='exact original full-grid location' in str(error)
    before_cap=new.cfg[CAP_KEY];before_pool=new.fine_pool.copy();before_history=len(new.fine_pool_history)
    new.rows[:]=-1.;new.fine_cache['data']['eta'][:]=1.
    learned,detail=new.learn_fine_violations(None,'artificial-exceed-stage-capacity')
    no_auto=bool(learned is None and detail.get('pool_capacity_would_be_exceeded')
        and new.cfg[CAP_KEY]==before_cap and np.array_equal(new.fine_pool,before_pool)
        and len(new.fine_pool_history)==before_history)
    second_cfg,second=reserve_initialization(new_cfg,union['row_indices'],3,8,locations,STAGE_KEYS[1])
    twice=False;reverse=False
    try:reserve_initialization(second_cfg,union['row_indices'],3,8,locations,STAGE_KEYS[1])
    except ValueError:twice=True
    try:reserve_initialization(cfg,old_ids,3,8,locations,STAGE_KEYS[1])
    except ValueError:reverse=True
    clamp_cfg=dict(cfg,**{'fine_initial_metric_rows_per_radial_branch':9,
        'fine_initial_curvature_rows_per_radial_group':10})
    duplicate=[{'t':0.,'theta':float(2*np.pi/4)},{'t':0.,'theta':float(2*np.pi/4)}]
    clamped,clamp=reserve_initialization(clamp_cfg,[0],2,4,duplicate,STAGE_KEYS[0])
    cl=ArrayFixture(clamped,2,4);cl.set_fine_pool([0],{'kind':'clamped-inherited'})
    cl.initialize_fine_pool(None,known_metric_locations=duplicate)
    clamp_ok=bool(clamp['total_initialization_upper_bound']==52 and len(cl.fine_pool)<=1+52)
    unavailable=initialization_diagnostic({'status':'artificial-error','error':{
        'type':'ValueError','message':'original failure'},'checkpoint':{
        'fine_physical_row_pool_history':[new.fine_pool_history[0]]}},new_cfg,first)
    checks={
        'real_original_initializer_reproduces_old_capacity_rejection':old_failure,
        'one_declared_reserve_keeps_the_same_union_and_old_learning_headroom':union_ok,
        'all_original_ID_validation_and_no_drop_guards_still_reject':all(rejected.values()),
        'original_known_peak_coordinate_guard_still_rejects':bad_peak,
        'post_initialization_learning_exits_at_fixed_capacity_without_growth':no_auto,
        'two_named_stages_each_reserve_once_and_repeat_or_reverse_is_rejected':bool(twice and reverse
            and second['inherited_fine_capacity']==first['new_fine_capacity']),
        'k_clamping_and_duplicate_known_peaks_respect_structural_bound':clamp_ok,
        'source_configuration_rows_locations_and_unrelated_parameters_unchanged':bool(
            cfg==frozen and old_ids==saved_ids and locations==saved_locations
            and all(new_cfg[k]==cfg[k] for k in cfg if k!=CAP_KEY)),
        'failed_initializer_preserves_original_error_without_inventing_union':bool(
            unavailable['contract_pass'] is None and not unavailable['initializer_union_available']
            and unavailable['stage_error']['message']=='original failure')}
    return {'schema':POLICY+'-development','artificial_inputs_only':True,
        'passed':bool(all(checks.values())),'checks':checks,'first_reservation':first,
        'first_recorded_initialization':diagnostic,'second_reservation':second,
        'old_geometry_solver_and_development_suites_not_executed':True}
