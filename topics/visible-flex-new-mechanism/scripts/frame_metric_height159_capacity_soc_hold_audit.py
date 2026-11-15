#!/usr/bin/env python3
"""Five frozen input prefixes, one new-capacity159 production, then SOC hold.

The two stages reserve their mandatory fine-initialization rows once each.
The frozen scientific drivers, all geometry/gates/controller/budget equations,
and all old row IDs are reused. Reports explicitly distinguish the new capacity
input production from restoration under the old complete parameter set.
Only the new capacity development branch is executed before public research.
"""
from __future__ import annotations
import argparse
import copy
from contextlib import redirect_stdout
import hashlib
import io
import json
import os
from pathlib import Path
import tempfile
import time
import traceback
import numpy as np

from frame_collar_bvp import atomic_save
from frame_entry_paired_repair_audit import require_public_actions
import frame_height159_fine_capacity as capacity
import frame_metric_height159_soc_hold_audit as frozen

height159=frozen.height159
growth=frozen.growth;strip=frozen.strip;soc=frozen.soc
body103=frozen.body103;tail154=frozen.tail154
INPUTS=frozen.INPUTS;SHA_NAMES=frozen.SHA_NAMES
_temporary_binding=frozen._temporary_binding
_scalar=frozen._scalar
prefix_handoff_diagnostic=frozen.prefix_handoff_diagnostic
handoff_restored_height159=frozen.handoff_restored_height159
SCHEMA='same159-two-declared-fine-capacity-stages-and-SOC-hold-audit-v1'
STAGE='metric_height159_capacity_soc_hold_stage'
CAPACITY_INPUT_STAGE=capacity.STAGE_KEYS[0]
CAPACITY_HOLD_STAGE=capacity.STAGE_KEYS[1]
FROZEN_ADAPTER_DEPENDENCIES={
    'frame_metric_height159_soc_hold_audit.py':'172567136e6cfd9373cdd41556555a3cb92938dc2ee8c6e238f42dcb13ab927e',
    'frame_metric_height159_soc_hold.py':'c6fb9d46840c64f9b6a43146ebbece8928e78f9efe609a624cf8ee4cc1da47de',
    'frame_metric_budget_recovery.py':'ba3e2becec3ad750ef8818711d8034003f3077877d39115925c308d123dec9ff'}


def implementation_hashes():
    result=frozen.implementation_hashes();result.update(capacity.implementation_hashes())
    p=Path(__file__);result[p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
    return result


def require_frozen_prefix_sources():
    frozen.require_frozen_prefix_sources()
    actual=frozen.implementation_hashes()
    for name,expected in FROZEN_ADAPTER_DEPENDENCIES.items():
        if actual.get(name)!=expected:raise ValueError('frozen capacity-adapter dependency differs: '+name)


def reserve_prepared_stage(prepared,stage_key):
    """Keep every runtime object/state; copy only cfg and descriptive replay."""
    restored,bindings,tenth,replay,coarse,fine=prepared
    problem,state,gate,lower,upper,source_cfg,cfg=restored
    radial,theta,grid=frozen.curvature_grid(tenth)
    new_cfg,receipt=capacity.reserve_initialization(cfg,fine,len(radial),2*len(theta),
        replay['known_fine_metric_locations'],stage_key)
    copied=copy.deepcopy(replay)
    copied['current_fine_initialization_capacity_reservation']=copy.deepcopy(receipt)
    copied['capacity_configuration_scope']={
        'schema':'same-runtime159-one-explicit-stage-resource-variant-v1',
        'stage_key':stage_key,'physical_state_sha256':replay['canonical_physical_state_sha256'],
        'original_complete_value_grid_definition_sha256':grid['definition_sha256'],
        'independent_coordinate_definition_sha256':replay['exact_coordinate_definition_sha256'],
        'runtime_field_reference_H_and_parameter_bytes_are_not_rebuilt_or_modified':True,
        'source_controller_radius_and_success_streak_are_unchanged':True,
        'capacity_is_not_part_of_physical_g_b0_or_coefficient_identity':True,
        'configuration_change_can_change_LP_rows_cost_and_numerical_trajectory':True}
    return ((problem,state,gate,lower,upper,source_cfg,new_cfg),bindings,tenth,copied,coarse,fine),receipt


def annotate_validated_input_handoff(continued,reservation,diagnostic):
    """Only after the unmodified strict handoff, state the new capacity scope."""
    restored,bindings,tenth,replay,coarse,fine=continued
    copied=copy.deepcopy(replay);previous=copied['temporary_input_restoration']
    original_schema=previous['schema']
    previous.update(schema='same-job-new-capacity159-input-production-v1',
        purpose='explicit new initialization-capacity input production using the frozen159 implementation',
        original_strict_handoff_receipt_schema=original_schema,
        original_source_config_state_pools_and_two_grid_handoff_passed=True,
        not_restoration_of_the_original_full159_parameter_configuration=True,
        capacity_reservation=copy.deepcopy(reservation),initialization_diagnostic=copy.deepcopy(diagnostic),
        old_observed_b429_comparison_is_historical_metadata_not_a_replay_requirement=True)
    copied['temporary_input_restorations'][-1]=copy.deepcopy(previous)
    copied['schema']='same-runtime-capacity159-production-to-frozen-SOC-hold-handoff-v1'
    copied['controller_continuation']['origin']=(
        'same-job new-capacity159 input production; actual inherited154 initialization '
        'followed only by completed frozen159 controller updates')
    previous['controller_continuation']=copy.deepcopy(copied['controller_continuation'])
    copied['temporary_input_restorations'][-1]=copy.deepcopy(previous)
    copied['capacity_input_production_scope']={
        'five_prior_prefixes_keep_all_original_parameters':True,
        'sixth_stage_implementation_frozen_but_capacity_configuration_new':True,
        'old_observed_canonical_not_forced':True,
        'hold_progress_starts_from_this_actual_qualified_production_result':True}
    return restored,bindings,tenth,copied,coarse,fine


def print_capacity(label,record):
    print('FINE CAPACITY '+label+': '+json.dumps(record,ensure_ascii=False,sort_keys=True,allow_nan=False),flush=True)


def input_production_outcome_text(report,receipt):
    label='new-capacity-entry-tail-height159-input-production'
    text=soc.prefix_outcome_text(report,receipt,label)
    return text.replace('TEMPORARY INPUT RESTORATION '+label+' -- not new scientific progress',
        'NEW CAPACITY159 INPUT PRODUCTION -- frozen implementation, new declared capacity; scientific cost and improvement are separate',1)


def adapt_report(report,reservations,diagnostics):
    """Relabel metadata only. Scientific records and numerical results are kept."""
    result=dict(report)
    result['invoked_frozen_driver_schema']=report.get('schema')
    result['invoked_frozen_driver_status']=report.get('status')
    result['invoked_frozen_driver_source_files_sha256']=copy.deepcopy(report.get('source_files_sha256'))
    result['schema']=SCHEMA;result['source_files_sha256']=implementation_hashes()
    if result.get('status')=='complete-two-grid-height159-SOC-hold-audit':
        result['status']='complete-two-grid-height159-capacity-SOC-hold-audit'
    if frozen.STAGE in result:result[STAGE]=result.pop(frozen.STAGE)
    result['fine_initialization_capacity_policy']=capacity.POLICY
    result['fine_initialization_capacity_reservations']=copy.deepcopy(reservations)
    result['fine_initialization_capacity_diagnostics']=copy.deepcopy(diagnostics)
    result['inherited_driver_counter_labels']={key:report.get(key) for key in
        ['old_optimizer_calls_this_run','necessary_height159_prefix_restoration_calls','new_scientific_solver_calls']}
    result['old_optimizer_calls_this_run']=5
    result['necessary_height159_prefix_restoration_calls']=0
    result['capacity_height159_input_production_calls']=1
    result['capacity_SOC_hold_calls']=1
    result['capacity_SOC_hold_solver_calls']=report.get('new_scientific_solver_calls',0)
    result['new_scientific_solver_calls']=2
    result['new_stage_call_counter_semantics']='capacity159 producer plus capacity-SOC-hold driver invocations, not LP counts'
    result['algorithm_stage_scope']={
        'five_frozen_prefixes_each_once':True,
        'sixth_is_new_capacity_configuration_input_production_not_old_parameter_replay':True,
        'hold_has_its_own_once_declared_capacity_reservation':True,
        'scientific_loop_and_gate_code_reused_without_monkeypatch':True,
        'only_two_configuration_keys_changed_by_each_capacity_adapter':[capacity.CAP_KEY,capacity.HISTORY_KEY],
        'no_old_failed_run_reclassified_and_no_historical_hash_forced':True,
        'costs_and_accepted_improvement_must_be_read_separately_for_the_two_new_configuration_stages':True}
    limits=copy.deepcopy(result.get('limitations',{}))
    limits.pop('six_prefixes_each_once_not_new_scientific_progress',None)
    limits.update(five_original_prefixes_are_necessary_input_restoration=True,
        capacity159_production_is_a_new_algorithm_configuration=True,
        enlarged_row_capacity_is_not_an_increased_LP_value_or_active_time_budget=True)
    result['limitations']=limits
    result['process_clock_scope']='five frozen prefixes, capacity159 input production, then separately budgeted capacity-SOC-hold'
    return result


def _frozen_format_view(report):
    view=dict(report)
    if STAGE in view:view[frozen.STAGE]=view.pop(STAGE)
    return view


def small_summary(report,out):
    summary=frozen.small_summary(_frozen_format_view(report),out)
    if frozen.STAGE in summary:summary[STAGE]=summary.pop(frozen.STAGE)
    for key in ['schema','source_files_sha256','invoked_frozen_driver_schema','invoked_frozen_driver_status',
            'invoked_frozen_driver_source_files_sha256','fine_initialization_capacity_policy',
            'fine_initialization_capacity_reservations','fine_initialization_capacity_diagnostics',
            'algorithm_stage_scope','capacity_height159_input_production_calls','capacity_SOC_hold_calls','capacity_SOC_hold_solver_calls',
            'new_stage_call_counter_semantics',
            'necessary_height159_prefix_restoration_calls','last_temporary_prefix_diagnostic']:
        if key in report:summary[key]=copy.deepcopy(report[key])
    return summary


def save_report(out,report):
    atomic_save(out,report)
    path=frozen.summary_path(out);tmp=path.with_name(path.name+'.tmp')
    tmp.write_text(json.dumps(small_summary(report,out),ensure_ascii=False,separators=(',',':'),allow_nan=False)+'\n')
    os.replace(tmp,path)


def _output_scope(text):
    # These are exact labels of frozen printers, not scientific data transforms.
    replacements={
        'All six necessary prefixes are input restoration, not new scientific progress or forced historical hashes.':
        'Five original prefixes are restoration. The sixth has a NEW declared fine capacity; its input-production progress and cost are separate.',
        'All five necessary prefixes are input restoration, not new scientific progress or forced historical hashes.':
        'The five prior prefixes are restoration. This159 input-production stage has a NEW declared fine capacity.',
        'ACTUAL SIXTH-PREFIX CONTROLLER:':'ACTUAL NEW-CAPACITY159 INPUT-PRODUCTION CONTROLLER:',
        'FROZEN159 PRE-HANDOFF DIAGNOSTIC:':'CAPACITY159 PRE-HANDOFF DIAGNOSTIC:'}
    for old,new in replacements.items():text=text.replace(old,new)
    return text


def run_audit(prepared,out,*,artificial=False,evaluate_only=False,process_started=None,prepare_seconds=0.,
        capacity_reservations=(),capacity_diagnostics=()):
    """Invoke the unchanged hold driver once; adapt only its metadata/output."""
    output=io.StringIO();report=None
    try:
        with redirect_stdout(output):
            report=frozen.run_audit(prepared,out,artificial=artificial,evaluate_only=evaluate_only,
                process_started=process_started,prepare_seconds=prepare_seconds)
    finally:
        # Do not lose original emitted failure information if the frozen call raises.
        if report is None and output.getvalue():print(_output_scope(output.getvalue()),end='',flush=True)
    diagnostic=capacity.initialization_diagnostic(report.get(frozen.STAGE),prepared[0][-1],capacity_reservations[-1])
    diagnostics=list(capacity_diagnostics)+[diagnostic]
    converted=adapt_report(report,list(capacity_reservations),diagnostics)
    save_report(out,converted)
    print(_output_scope(output.getvalue()),end='',flush=True)
    print_capacity('HOLD INITIALIZER ACTUAL',diagnostic)
    print('CAPACITY STAGE COUNTS: five frozen restorations; one new-capacity159 input production; one capacity-SOC-hold invocation. No retry.',flush=True)
    if diagnostic.get('contract_pass') is False:
        converted['capacity_diagnostic_error']='recorded initialization violates the declared structural reservation'
        converted['status']='capacity-initialization-contract-error-original-records-preserved'
        save_report(out,converted)
    return converted


def run_pipeline(args,*,artificial=False,evaluate_only=False,process_started=None):
    started=time.monotonic() if process_started is None else process_started
    phase='public-environment-and-original24-input-contract';restorations=[];raw_bindings=[]
    last_prefix_diagnostic=None;reservations=[];capacity_diagnostics=[]
    invoked={'growth':0,'strip':0,'SOC':0,'body103':0,'tail154':0,'height159':0,'hold':0}
    try:
        require_frozen_prefix_sources()
        if not artificial:
            require_public_actions(os.environ.get('GITHUB_ACTIONS'),os.environ.get('GITHUB_REPOSITORY'),
                [getattr(args,k) for k in INPUTS])
        parent='/dev/shm' if artificial and Path('/dev/shm').is_dir() else os.environ.get('RUNNER_TEMP')
        with tempfile.TemporaryDirectory(prefix='visible-capacity159-five-inputs-',dir=parent) as folder:
            growth_out=Path(folder)/'restored-growth.json';strip_out=Path(folder)/'restored-strip.json'
            soc_out=Path(folder)/'restored-scaled-SOC.json';body_out=Path(folder)/'restored-body103.json'
            tail_out=Path(folder)/'restored-tail154.json';height_out=Path(folder)/'restored-height159.json'
            prefix_args=copy.copy(args);prefix_args.out=growth_out
            phase='strict-original24-input-preparation';before=time.monotonic()
            prepared=growth.prepare_run(prefix_args,artificial=artificial,process_started=started)
            prepare_seconds=time.monotonic()-before
            phase='one-necessary-frozen-growth-restoration';invoked['growth']=1
            previous=growth.run_audit(prepared,growth_out,artificial=artificial,evaluate_only=evaluate_only,
                process_started=started,prepare_seconds=prepare_seconds)
            binding=_temporary_binding(growth_out);raw_bindings.append(binding)
            phase='growth-qualified-state-and-all-pools-handoff'
            continued=strip.handoff_restored_growth(prepared,previous,binding,artificial=artificial)
            restorations.append(continued[3]['temporary_input_restoration'])
            print(soc.prefix_outcome_text(previous,restorations[-1],'growth'),end='',flush=True)
            del previous,prepared
            phase='one-necessary-frozen-strip-restoration';invoked['strip']=1
            previous=strip.run_audit(continued,strip_out,artificial=artificial,evaluate_only=evaluate_only,
                process_started=started,prepare_seconds=time.monotonic()-started)
            binding=_temporary_binding(strip_out);raw_bindings.append(binding)
            phase='strip-qualified-state-and-all-pools-controller-handoff'
            prepared_soc=soc.handoff_restored_strip(continued,previous,binding,artificial=artificial)
            restorations=list(prepared_soc[3]['temporary_input_restorations'])
            print(soc.prefix_outcome_text(previous,restorations[-1],'strip-reserve'),end='',flush=True)
            del previous,continued
            phase='one-necessary-frozen-scaled-SOC-restoration';invoked['SOC']=1
            previous=soc.run_audit(prepared_soc,soc_out,artificial=artificial,evaluate_only=evaluate_only,
                process_started=started,prepare_seconds=time.monotonic()-started)
            binding=_temporary_binding(soc_out);raw_bindings.append(binding)
            phase='SOC-qualified-state-complete-pools-and-explicit-new-subspace-handoff'
            prepared_body=body103.handoff_restored_soc(prepared_soc,previous,binding,artificial=artificial)
            restorations=list(prepared_body[3]['temporary_input_restorations'])
            print(soc.prefix_outcome_text(previous,restorations[-1],'scaled-SOC'),end='',flush=True)
            print('Regenerated scaled-SOC equals observed ec76: '+_scalar(
                restorations[-1]['regenerated_final_equals_observed_SOC_ec76'])+'; never a forced replay condition.',flush=True)
            del previous,prepared_soc
            phase='one-necessary-frozen-body103-restoration';invoked['body103']=1
            previous=body103.run_audit(prepared_body,body_out,artificial=artificial,evaluate_only=evaluate_only,
                process_started=started,prepare_seconds=time.monotonic()-started)
            binding=_temporary_binding(body_out);raw_bindings.append(binding)
            phase='body103-qualified-full-state-complete-pools-handoff'
            prepared_tail=tail154.handoff_restored_body103(prepared_body,previous,binding,artificial=artificial)
            restorations=list(prepared_tail[3]['temporary_input_restorations'])
            print(soc.prefix_outcome_text(previous,restorations[-1],'entry-body103'),end='',flush=True)
            print('Regenerated body103 equals observed bfbd: '+_scalar(
                restorations[-1]['regenerated_final_equals_observed_body103_bfbd'])+'; never a forced replay condition.',flush=True)
            del previous,prepared_body
            phase='one-necessary-frozen-entry-tail154-restoration';invoked['tail154']=1
            previous=tail154.run_audit(prepared_tail,tail_out,artificial=artificial,evaluate_only=evaluate_only,
                process_started=started,prepare_seconds=time.monotonic()-started)
            binding=_temporary_binding(tail_out);raw_bindings.append(binding)
            phase='tail154-qualified-state-pools-controller-and-exact-height-map-handoff'
            prepared_height=height159.handoff_restored_tail154(prepared_tail,previous,binding,artificial=artificial)
            restorations=list(prepared_height[3]['temporary_input_restorations'])
            print(soc.prefix_outcome_text(previous,restorations[-1],'entry-tail154'),end='',flush=True)
            print('Regenerated tail154 equals observed2ee6: '+_scalar(
                restorations[-1]['regenerated_final_equals_observed_tail154_2ee6'])+
                '; no retry or forced canonical. This is the sixth-prefix initial state.',flush=True)
            del previous,prepared_tail
            phase='declare-once-capacity159-input-production-reserve'
            prepared_height,reservation=reserve_prepared_stage(prepared_height,CAPACITY_INPUT_STAGE)
            reservations.append(reservation);print_capacity('INPUT PRODUCTION DECLARED',reservation)
            phase='one-new-capacity-five-null-height159-input-production';invoked['height159']=1
            captured=io.StringIO()
            try:
                with redirect_stdout(captured):
                    previous=height159.run_audit(prepared_height,height_out,artificial=artificial,evaluate_only=evaluate_only,
                        process_started=started,prepare_seconds=time.monotonic()-started)
            finally:
                if captured.getvalue():print(_output_scope(captured.getvalue()),end='',flush=True)
            binding=_temporary_binding(height_out);raw_bindings.append(binding)
            phase='height159-qualified-state-full-pools-reference-and-controller-handoff'
            last_prefix_diagnostic=prefix_handoff_diagnostic(previous,binding)
            print('CAPACITY159 PRE-HANDOFF DIAGNOSTIC: '+json.dumps(last_prefix_diagnostic,
                ensure_ascii=False,sort_keys=True,allow_nan=False),flush=True)
            capacity_result=capacity.initialization_diagnostic(previous.get(height159.STAGE),
                prepared_height[0][-1],reservation)
            capacity_diagnostics.append(capacity_result);print_capacity('INPUT PRODUCTION INITIALIZER ACTUAL',capacity_result)
            new_prepared=handoff_restored_height159(prepared_height,previous,binding,artificial=artificial)
            if capacity_result.get('contract_pass') is False:
                raise ValueError('recorded capacity159 initialization violates its declared structural allowance')
            new_prepared=annotate_validated_input_handoff(new_prepared,reservation,capacity_result)
            restorations=list(new_prepared[3]['temporary_input_restorations'])
            print(input_production_outcome_text(previous,restorations[-1]),end='',flush=True)
            print('Regenerated height159 equals observed b429: '+_scalar(
                restorations[-1]['regenerated_final_equals_observed_height159_b429'])+
                '; historical comparison only: this is NEW capacity input production. No retry or forced canonical; hold progress starts here.',flush=True)
            del previous,prepared_height
            phase='declare-once-hold-initialization-reserve'
            new_prepared,reservation=reserve_prepared_stage(new_prepared,CAPACITY_HOLD_STAGE)
            reservations.append(reservation);print_capacity('HOLD DECLARED',reservation)
            phase='one-capacity-conditional-successful-SOC-radius-stage';invoked['hold']=1
            return run_audit(new_prepared,args.out,artificial=artificial,evaluate_only=evaluate_only,
                process_started=started,prepare_seconds=time.monotonic()-started,
                capacity_reservations=reservations,capacity_diagnostics=capacity_diagnostics)
    except Exception as error:
        failure={'schema':SCHEMA,'status':'height159-SOC-hold-pipeline-failed-last-written-checkpoint-preserved',
            'phase':phase,'source_files_sha256':implementation_hashes(),
            'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
            'github_repository':os.environ.get('GITHUB_REPOSITORY'),'artificial_inputs_only':bool(artificial),
            'necessary_growth_prefix_restoration_calls':invoked['growth'],
            'necessary_strip_prefix_restoration_calls':invoked['strip'],
            'necessary_SOC_prefix_restoration_calls':invoked['SOC'],
            'necessary_body103_prefix_restoration_calls':invoked['body103'],
            'necessary_tail154_prefix_restoration_calls':invoked['tail154'],
            'necessary_height159_prefix_restoration_calls':0,
            'capacity_height159_input_production_calls':invoked['height159'],
            'capacity_SOC_hold_calls':invoked['hold'],
            'fine_initialization_capacity_policy':capacity.POLICY,
            'fine_initialization_capacity_reservations':copy.deepcopy(reservations),
            'fine_initialization_capacity_diagnostics':copy.deepcopy(capacity_diagnostics),
            'new_scientific_solver_calls':invoked['height159']+invoked['hold'],
            'inherited_driver_counter_labels':{'new_scientific_solver_calls':invoked['hold']},
            'new_stage_call_counter_semantics':'capacity159 producer plus capacity-SOC-hold driver invocations, not LP counts',
            'temporary_prefix_raw_bindings':raw_bindings,'temporary_input_restorations':restorations,
            'last_temporary_prefix_diagnostic':copy.deepcopy(last_prefix_diagnostic),
            'process_total_elapsed_seconds':time.monotonic()-started,
            'error':{'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}}
        if invoked['hold'] and Path(args.out).exists():
            try:
                existing=json.loads(Path(args.out).read_text())
                if existing.get('schema')!=SCHEMA:existing=adapt_report(existing,reservations,capacity_diagnostics)
                existing['scientific_status_before_pipeline_failure']=existing.get('status')
                existing['status']='height159-SOC-hold-pipeline-error-last-checkpoint-preserved';existing['pipeline_failure']=failure
                save_report(args.out,existing);return existing
            except (OSError,ValueError,TypeError,KeyError):pass
        save_report(args.out,failure)
        print_capacity('PIPELINE FAILURE',failure['error'])
        if last_prefix_diagnostic is not None:
            print('CAPACITY159 PRE-HANDOFF FAILURE RETAINED: '+json.dumps(last_prefix_diagnostic,sort_keys=True,allow_nan=False),flush=True)
        return failure


def developer_check():
    """New capacity arrays plus orchestration stubs; no old suite or science."""
    from contextlib import ExitStack
    from types import SimpleNamespace
    from unittest.mock import patch
    import sys
    arrays=capacity.developer_check()
    module=sys.modules[__name__]
    cfg={capacity.CAP_KEY:6,'fine_initial_metric_rows_per_radial_branch':2,
        'fine_initial_curvature_rows_per_radial_group':1,'max_linear_models':12,
        'max_physical_evaluations':40,'max_seconds':120,
        'unchanged_minimum_radius':'1/128000'}
    state=np.array([0.,-0.,.125]);coarse=np.array([0,1],np.int64)
    fine=np.array([0,24,96,240],np.int64);problem=object();gate=object()
    lower=np.array([-1.,-1.,-1.]);upper=-lower;source_cfg={'primitive_order':8}
    controller={'trust_evaluated':.00003125,'trust_binary64_exact':'1/32000','success_streak':1}
    restoration={'schema':'artificial-original-prefix','controller_continuation':copy.deepcopy(controller),
        **{k:False for k in ['regenerated_final_equals_observed_SOC_ec76',
            'regenerated_final_equals_observed_body103_bfbd','regenerated_final_equals_observed_tail154_2ee6',
            'regenerated_final_equals_observed_height159_b429']}}
    replay={'canonical_physical_state_sha256':'artificial-state',
        'exact_coordinate_definition_sha256':'artificial-exact-H',
        'known_fine_metric_locations':[{'t':2.,'theta':7.}],
        'controller_continuation':copy.deepcopy(controller),
        'temporary_input_restoration':copy.deepcopy(restoration),
        'temporary_input_restorations':[copy.deepcopy(restoration) for _ in range(5)]}
    prepared=((problem,state,gate,lower,upper,source_cfg,cfg),{},
        {'artificial_grid':True},replay,coarse,fine)
    radial=np.arange(3,dtype=float);theta=np.arange(4,dtype=float)
    grid={'definition_sha256':'artificial-grid-3-by-4','radial_nodes_exact':['0','1','2']}
    frozen_cfg=copy.deepcopy(cfg);state_bytes=state.tobytes();original_replay=copy.deepcopy(replay)
    calls={k:0 for k in ['growth','strip','SOC','body103','tail154','height159','hold']}
    seen=[];fail_height=[False]

    def recorded_stage(prepared_here):
        current_cfg=prepared_here[0][-1];initial_ids=prepared_here[5].tolist()
        chosen=set(initial_ids)
        for g in [0,1,7,8,9,10]:
            k=2 if g<2 else 1
            for r in range(3):chosen.update(g*24+r*8+j for j in range(k))
        chosen.update([23,47])
        union=sorted(chosen)
        def record(ids,reason):
            return {'row_indices':ids,'row_count':len(ids),'row_indices_sha256':capacity.digest(ids),
                'reason':{'kind':reason}}
        history=[record(initial_ids,'artificial-inherited')]
        if not fail_height[0]:history.append(record(union,capacity.INITIALIZER_REASON))
        return {'status':'artificial-init-error' if fail_height[0] else 'artificial-complete',
            'error':{'type':'ValueError','message':'new capacity IO injected original stage failure'} if fail_height[0] else None,
            'solver':{'models':[],'linear_program_invocation_count':0},
            'checkpoint':{'fine_physical_row_pool_history':history}},union

    def old_run(label):
        def call(prepared_here,out,**kwargs):
            calls[label]+=1
            result={'schema':'artificial-old-prefix','configuration':prepared_here[0][-1]}
            if label=='height159':
                seen.append(copy.deepcopy(prepared_here[0][-1]));stage,ids=recorded_stage(prepared_here)
                result.update(schema=height159.SCHEMA,status='artificial-capacity159-result',
                    **{height159.STAGE:stage,'artificial_final_fine_IDs':ids})
            atomic_save(out,result);return result
        return call

    def plain_handoff(prepared_here,previous,binding,**kwargs):return prepared_here

    def height_handoff(prepared_here,previous,binding,**kwargs):
        if previous[height159.STAGE]['error']:
            raise ValueError('sixth-prefix implementation failure is not a usable restoration')
        # Only the old handoff's new controller/configuration installation is mocked.
        items=list(prepared_here);restored=list(items[0]);new_cfg=copy.deepcopy(restored[-1])
        new_cfg['successful_SOC_radius_retention_policy']='artificial-hold-policy'
        restored[-1]=new_cfg;items[0]=tuple(restored)
        rp=copy.deepcopy(items[3]);r=copy.deepcopy(restoration)
        r['schema']='artificial-validated-capacity159';r['prefix_configuration']=copy.deepcopy(prepared_here[0][-1])
        rp['temporary_input_restoration']=r;rp['temporary_input_restorations'].append(copy.deepcopy(r))
        items[3]=rp;items[5]=np.asarray(previous['artificial_final_fine_IDs'],np.int64)
        return tuple(items)

    def held_run(prepared_here,out,**kwargs):
        calls['hold']+=1;seen.append(copy.deepcopy(prepared_here[0][-1]))
        stage,_=recorded_stage(prepared_here)
        result={'schema':frozen.SCHEMA,'source_files_sha256':{'artificial':'frozen-hold'},
            'configuration':prepared_here[0][-1],'status':'complete-two-grid-height159-SOC-hold-audit',
            'new_scientific_solver_calls':1,'old_optimizer_calls_this_run':6,
            'necessary_height159_prefix_restoration_calls':1,'temporary_input_restorations':prepared_here[3]['temporary_input_restorations'],
            frozen.STAGE:stage}
        atomic_save(out,result)
        print('All six necessary prefixes are input restoration, not new scientific progress or forced historical hashes.')
        print('ARTIFICIAL HOLD ORIGINAL RECORDS PRESERVED')
        return result

    def semantic_stub(report,out):
        # The unchanged legacy summary was already covered publicly. Here only
        # this new adapter's namespace/capacity metadata and JSON path are tested.
        result={k:copy.deepcopy(v) for k,v in report.items() if k not in ['temporary_input_restorations']}
        result['full_report']={'filename':Path(out).name,'sha256':hashlib.sha256(Path(out).read_bytes()).hexdigest()}
        return result

    def patches(stack):
        stack.enter_context(patch.object(module,'require_frozen_prefix_sources',return_value=None))
        stack.enter_context(patch.object(frozen,'curvature_grid',return_value=(radial,theta,grid)))
        stack.enter_context(patch.object(growth,'prepare_run',return_value=prepared))
        for mod,label in [(growth,'growth'),(strip,'strip'),(soc,'SOC'),(body103,'body103'),
                (tail154,'tail154'),(height159,'height159')]:
            stack.enter_context(patch.object(mod,'run_audit',side_effect=old_run(label)))
        for mod,name in [(strip,'handoff_restored_growth'),(soc,'handoff_restored_strip'),
                (body103,'handoff_restored_soc'),(tail154,'handoff_restored_body103'),
                (height159,'handoff_restored_tail154')]:
            stack.enter_context(patch.object(mod,name,side_effect=plain_handoff))
        stack.enter_context(patch.object(module,'handoff_restored_height159',side_effect=height_handoff))
        stack.enter_context(patch.object(frozen,'run_audit',side_effect=held_run))
        stack.enter_context(patch.object(frozen,'small_summary',side_effect=semantic_stub))
        stack.enter_context(patch.object(soc,'prefix_outcome_text',side_effect=lambda report,receipt,label:
            'TEMPORARY INPUT RESTORATION '+label+' -- not new scientific progress\nARTIFICIAL PREFIX METADATA ONLY\n'))
    directory='/dev/shm' if Path('/dev/shm').is_dir() else os.environ.get('RUNNER_TEMP')
    with tempfile.TemporaryDirectory(prefix='capacity159-new-IO-only-',dir=directory) as folder:
        out=Path(folder)/'capacity-audit.json';args=SimpleNamespace(out=out)
        for k in INPUTS:setattr(args,k,Path(folder)/('artificial-'+k+'.json'))
        for k in SHA_NAMES:setattr(args,'expected_'+k+'_sha256','artificial-no-input-opened')
        capture=io.StringIO()
        with ExitStack() as stack,redirect_stdout(capture):
            patches(stack);report=run_pipeline(args,artificial=True,evaluate_only=True)
        saved=json.loads(out.read_text());summary=json.loads(frozen.summary_path(out).read_text())
        once=bool(all(n==1 for n in calls.values()) and saved[STAGE]['status']=='artificial-complete')
        boundaries=bool(len(seen)==2 and len(seen[0][capacity.HISTORY_KEY])==1
            and len(seen[1][capacity.HISTORY_KEY])==2
            and seen[1][capacity.HISTORY_KEY][1]['inherited_fine_capacity']==seen[0][capacity.CAP_KEY])
        scope=bool(saved['capacity_height159_input_production_calls']==1
            and saved['necessary_height159_prefix_restoration_calls']==0
            and saved['new_scientific_solver_calls']==2
            and saved['inherited_driver_counter_labels']['new_scientific_solver_calls']==1
            and saved['old_optimizer_calls_this_run']==5 and frozen.STAGE not in saved
            and len([k for k in saved if k.endswith('_stage')])==1
            and 'sixth_is_new_capacity_configuration_input_production_not_old_parameter_replay' in saved['algorithm_stage_scope'])
        printed=bool('FINE CAPACITY INPUT PRODUCTION DECLARED' in capture.getvalue()
            and 'FINE CAPACITY INPUT PRODUCTION INITIALIZER ACTUAL' in capture.getvalue()
            and 'FINE CAPACITY HOLD DECLARED' in capture.getvalue()
            and 'FINE CAPACITY HOLD INITIALIZER ACTUAL' in capture.getvalue()
            and 'ARTIFICIAL HOLD ORIGINAL RECORDS PRESERVED' in capture.getvalue()
            and 'NEW CAPACITY159 INPUT PRODUCTION -- frozen implementation, new declared capacity' in capture.getvalue()
            and 'TEMPORARY INPUT RESTORATION new-capacity-entry-tail-height159-input-production' not in capture.getvalue()
            and 'All six necessary prefixes are input restoration' not in capture.getvalue())
        summary_ok=bool(summary['fine_initialization_capacity_diagnostics']==saved['fine_initialization_capacity_diagnostics']
            and summary['full_report']['sha256']==hashlib.sha256(out.read_bytes()).hexdigest())
        before=calls.copy();fail_height[0]=True;args.out=Path(folder)/'failure-audit.json';capture=io.StringIO()
        with ExitStack() as stack,redirect_stdout(capture):
            patches(stack);failed=run_pipeline(args,artificial=True,evaluate_only=True)
        failure_ok=bool(calls['hold']==before['hold'] and failed['capacity_height159_input_production_calls']==1
            and failed['new_scientific_solver_calls']==1 and failed['capacity_SOC_hold_calls']==0
            and failed['last_temporary_prefix_diagnostic']['stage_error']['message']=='new capacity IO injected original stage failure'
            and failed['fine_initialization_capacity_diagnostics'][0]['contract_pass'] is None
            and 'PRE-HANDOFF FAILURE RETAINED' in capture.getvalue())
        args.out=Path(folder)/'guard-audit.json';before=calls.copy()
        with ExitStack() as stack,redirect_stdout(io.StringIO()):
            patches(stack)
            stack.enter_context(patch.dict(os.environ,{'GITHUB_ACTIONS':'false','GITHUB_REPOSITORY':'artificial/nonpublic'}))
            rejected=run_pipeline(args,artificial=False,evaluate_only=False)
        guard_ok=bool(calls==before and rejected['capacity_height159_input_production_calls']==0
            and rejected['new_scientific_solver_calls']==0 and not rejected['fine_initialization_capacity_reservations'])
        marker={'schema':'artificial-capacity-dispatch-only','passed':True,'artificial_inputs_only':True}
        devout=Path(folder)/'new-development.json'
        with patch.object(module,'developer_check',return_value=marker), \
                patch.object(module,'run_pipeline',side_effect=AssertionError('development must not call research')), \
                patch.object(frozen,'developer_check',side_effect=AssertionError('old fifteen checks must not rerun')), \
                patch.object(frozen,'prefix_diagnostic_developer_check',side_effect=AssertionError('old diagnostic checks must not rerun')), \
                patch.object(sys,'argv',[__file__,'--check-capacity-only','--out',str(devout)]),redirect_stdout(io.StringIO()):
            main()
        dispatched=json.loads(devout.read_text())['schema']==marker['schema']
    immutability=bool(cfg==frozen_cfg and state.tobytes()==state_bytes and replay==original_replay)
    checks={'old_five_plus_new_capacity159_and_hold_called_once_by_new_orchestration':once,
        'two_explicit_stage_boundaries_preserve_inherited_capacity_and_headroom':boundaries,
        'one_native_stage_and_honest_new_input_production_counter_labels':scope,
        'all_capacity_metadata_and_original_scientific_output_preserved_with_correct_scope':printed,
        'new_summary_and_full_report_have_identical_capacity_metadata_and_byte_binding':summary_ok,
        'original159_failure_still_stops_handoff_and_keeps_error_no_hold_call':failure_ok,
        'nonpublic_guard_stops_before_any_prefix_or_capacity_change':guard_ok,
        'new_development_CLI_calls_only_the_new_capacity_branch':dispatched,
        'runtime_state_controller_source_configuration_and_replay_not_mutated':immutability}
    return {'schema':SCHEMA+'-capacity-development-only','artificial_inputs_only':True,
        'passed':bool(arrays['passed'] and all(checks.values())),'checks':checks,
        'capacity_array_development':arrays,'pipeline_stubs_call_counts':calls,
        'scientific_prefix_geometry_Jacobian_and_LP_not_executed':True,
        'old_fifteen_and_old_diagnostic_development_suites_not_executed':True}


def main():
    started=time.monotonic();parser=argparse.ArgumentParser(description=__doc__)
    for name in INPUTS:parser.add_argument('--'+name.replace('_','-'),type=Path)
    for name in SHA_NAMES:parser.add_argument('--expected-'+name+'-sha256')
    parser.add_argument('--check-only',action='store_true',help='alias for the NEW capacity-only development branch')
    parser.add_argument('--check-capacity-only',action='store_true')
    parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    if args.check_only and args.check_capacity_only:parser.error('choose one spelling of the new development branch')
    if args.check_only or args.check_capacity_only:
        try:result=developer_check()
        except Exception as error:
            atomic_save(args.out,{'schema':SCHEMA+'-development-error','passed':False,'artificial_inputs_only':True,
                'source_files_sha256':implementation_hashes(),'process_total_elapsed_seconds':time.monotonic()-started,
                'error':{'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}})
            raise
        result.update(source_files_sha256=implementation_hashes(),process_total_elapsed_seconds=time.monotonic()-started)
        atomic_save(args.out,result);print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
        if not result['passed']:raise SystemExit(1)
        return
    report=run_pipeline(args,process_started=started)
    print(json.dumps({'out':str(args.out),'status':report.get('status')}),flush=True)
    if report.get('status')!='complete-two-grid-height159-capacity-SOC-hold-audit':raise SystemExit(1)


if __name__=='__main__':main()


