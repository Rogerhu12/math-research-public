#!/usr/bin/env python3
"""Bounded scalar observations of operations already completed by the full solver.

The writer never imports numerical libraries, evaluates a field, requests a root,
or calls a scientific operator. Point digests are supplied by the complete caller
after the original operation. Different points and trial/iterate states stay
separate. A mutable progress file is not a final report or certificate.
"""
import copy
import datetime
import hashlib
import json
import math
import os
from pathlib import Path

SCHEMA = 'actual-complete-fejer-geometry-trial-scalar-progress-v1'
BINDING_SCHEMA = 'actual-complete-fejer-own-point-scalar-observation-v1'
MAX_FILE_BYTES = 16384
COUNT_KEYS = ('events','statistics_returns','geometry_returns','trial_starts',
    'trial_decisions','accepted_checkpoint_returns','report_saves',
    'point_digest_reads','writes','write_failures','observation_failures',
    'completed_trial_scalar_files_written','completed_trial_scalar_file_failures')
SLOTS = ('initial_statistics','initial_geometry','current_statistics',
    'current_geometry','latest_trial_statistics','latest_trial_geometry')
GEOMETRY_FAMILIES = ('reach','body_diameter','distance_plus','distance_minus',
    'cap_diameter','height_floor')
COMPLETED_TRIAL_SCHEMA = 'actual-complete-fejer-returned-trial-scalar-observation-v1'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
        allow_nan=False).encode()).hexdigest()


def definition():
    return dict(schema=SCHEMA,source_sha256=sha(__file__),
        observation_scope='existing complete statistics, finite geometry, actual decisions and saved reports only',
        actual_field_J_or_root_calls=0,new_numerical_evaluation_performed=False,
        point_binding='complete caller array SHA after the original returned operation; never latest-root point substitution',
        statistics_scope='all original finite metric observation rows, not a continuous surface norm',
        geometry_scope='original complete finite permanent and grid screen, not a continuous reach certificate',
        current_iterate_and_latest_trial_kept_separate=True,
        incomplete_or_nonfinite_values_represented_by_null=True,
        accepted_decision_and_checkpoint_return_distinct_from_final_report=True,
        mutable_progress_is_not_an_immutable_field_input=True,
        original_numerical_sequence_and_budgets_unchanged=True,
        maximum_progress_file_bytes=MAX_FILE_BYTES,
        geometry_components='all six original dimensionless returned physical_g values; no new field evaluation',
        ties='all exactly equal finite maximizers in original family order',
        latest_completed_trial_survives_next_trial_start=True,
        completed_trial_scalar_files='one immutable scalar-only runner file after each actually returned decision',
        complete_trial_arrays_or_direction_execution_checkpoint_claimed=False,
        completed_scalar_file_unavailability_changes_science=False)


def _utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def _digest(value):
    return (isinstance(value,str) and len(value)==64
        and all(c in '0123456789abcdef' for c in value))


def _number(value):
    if isinstance(value,bool) or not isinstance(value,(int,float)):
        return None
    return value if math.isfinite(value) else None


def _same(value):
    return json.loads(json.dumps(value,allow_nan=False))


def _statistics(value,point,objective,*,source,model,driver,state):
    if not isinstance(value,dict) or not _digest(point):
        raise ValueError('Keep the actual complete returned statistics and its caller point')
    spectral=value.get('spectral')
    if not isinstance(spectral,dict):
        raise ValueError('Keep the complete returned scalar-objective object')
    result=dict(schema=BINDING_SCHEMA,source_sha256=source,
        model_identity_sha256=model,driver_source_sha256=driver,
        point_sha256=point,state=state,recorded_at_utc=_utc(),
        kind='complete-finite-metric-statistics',objective_key=objective,
        Phi=_number(spectral.get(objective)),
        max_relative_gram=_number(value.get('max_relative_gram')),
        legacy_max_relative_gram=_number(value.get('legacy_max_relative_gram')),
        min_relative_E=_number(value.get('min_relative_E')),
        min_relative_determinant=_number(value.get('min_relative_determinant')),
        full_original_finite_metric_rows_returned=True,
        continuous_metric_bound_claimed=False,accepted_or_final_inferred=False)
    return result



def _geometry_components(value):
    amplitude=value.get('amplitude')
    amplitude=amplitude if isinstance(amplitude,dict) else {}
    return dict(reach=_number(value.get('reach_physical_g')),
        **{name:_number(amplitude.get(name)) for name in GEOMETRY_FAMILIES[1:]})


def _maximum_families(components,maximum,complete):
    if not complete or maximum is None or any(components.get(k) is None for k in GEOMETRY_FAMILIES):
        return None
    if max(components.values())!=maximum:
        raise ValueError('The six returned physical inequalities do not match their original maximum')
    return '|'.join(k for k in GEOMETRY_FAMILIES if components[k]==maximum)


def _validate_geometry_components(item,raw=None):
    components=item.get('physical_g_by_family')
    if (not isinstance(components,dict) or set(components)!=set(GEOMETRY_FAMILIES)
            or any(v is not None and _number(v) is None for v in components.values())):
        raise ValueError('Keep each original finite geometry family or explicit null')
    complete=item.get('complete') is True
    available=complete and all(components[k] is not None for k in GEOMETRY_FAMILIES)
    if (item.get('all_six_physical_g_returned')!=available
            or item.get('maximum_physical_families')!=_maximum_families(
                components,item.get('maximum_physical_g'),complete)):
        raise ValueError('Do not guess the worst physical family or discard an exact tie')
    if raw is not None and components!=_geometry_components(raw):
        raise ValueError('The six physical inequalities differ from their actual returned source')


def _geometry(value,point,*,source,model,driver,state):
    if not isinstance(value,dict) or not _digest(point):
        raise ValueError('Keep the actual returned geometry object and its caller point')
    recorded=value.get('current_full_point_sha256')
    complete=value.get('complete') is True
    if recorded is not None and recorded!=point:
        raise ValueError('Do not substitute another field point for this geometry return')
    if complete and recorded!=point:
        raise ValueError('A complete screen retains its own actual point')
    maximum=_number(value.get('maximum_physical_g'))
    positive=max(0,maximum) if complete and maximum is not None else None
    components=_geometry_components(value)
    families=_maximum_families(components,maximum,complete)
    return dict(schema=BINDING_SCHEMA,source_sha256=source,
        model_identity_sha256=model,driver_source_sha256=driver,
        point_sha256=point,recorded_geometry_point_sha256=recorded,
        state=state,recorded_at_utc=_utc(),kind='original-finite-geometry-screen',
        complete=complete,passed=value.get('passed') if isinstance(value.get('passed'),bool) else None,
        maximum_physical_g=maximum,positive_physical_g=positive,
        physical_g_by_family=components,maximum_physical_families=families,
        all_six_physical_g_returned=complete and all(v is not None for v in components.values()),
        necessary_reach_product=_number(value.get('necessary_reach_product')),
        maximum_absolute_principal_curvature=_number(value.get('maximum_absolute_principal_curvature')),
        diameter_point_lower=_number(value.get('diameter_point_lower')),
        current_height=_number(value.get('current_height')),
        continuous_geometry_bound_claimed=False,accepted_or_final_inferred=False)


def capture_original_progress(report):
    """Capture the complete small original 48-selector source, without scientific calls."""
    try:
        path=Path(report['actual_evaluation_progress_path']).resolve()
        size=path.stat().st_size
        if size>=MAX_FILE_BYTES:
            raise ValueError('The original progress file exceeds the complete small capture bound')
        with path.open('rb') as handle:
            raw=handle.read(MAX_FILE_BYTES)
        with path.open('rb') as handle:
            second=handle.read(MAX_FILE_BYTES)
        if len(raw)!=size or raw!=second or path.stat().st_size!=size:
            raise ValueError('The original progress file changed across two bounded complete reads')
        value=json.loads(raw)
        _validate_original_progress_value(value,report)
        return dict(available=True,record=dict(path=str(path),bytes=size,
            sha256=hashlib.sha256(raw).hexdigest()),complete_value=value,
            complete_value_identity_sha256=canonical(value),
            two_complete_bounded_reads_agreed=True,
            original_normal_point_not_relabelled_as_current_iterate=True,
            mutable_origin_is_not_an_immutable_final_or_parent=True)
    except Exception as error:
        return dict(available=False,error_type=type(error).__name__,reason=str(error)[:700],
            scientific_success_or_failure_inferred=False)


def _validate_original_progress_value(value,report):
    roles=report['source_sha256_by_role']
    if (not isinstance(value,dict) or value.get('schema')!='actual-complete-normal-evaluation-progress-v1'
            or value.get('source_sha256')!=roles['closure_values']
            or value.get('operator_source_sha256')!=roles['endpoint']
            or value.get('actual_model_identity_sha256')!=report['model_identity_sha256']
            or value.get('current_full_point_sha256') is not None and not _digest(value['current_full_point_sha256'])
            or value.get('actual_scientific_evaluations_by_observer')!=0
            or value.get('scientific_complete_inferred') is not False
            or value.get('first_field_or_geometry_return_inferred') is not False
            or value.get('mutable_latest_status') is not True):
        raise ValueError('Keep the original whole progress source, model, own point and non-completion scope')


class Recorder:
    def __init__(self,path,report):
        self.path=Path(path)
        self.definition=definition()
        self.source=self.definition['source_sha256']
        self.model=report['model_identity_sha256']
        self.driver=report['source_sha256']
        self.target=report['predeclared_mathematical_target_identity_sha256']
        self.objective=report['selected_scalar_objective_key']
        if (any(not _digest(v) for v in (self.source,self.model,self.driver,self.target))
                or report.get('source_sha256_by_role',{}).get('scalar_progress')!=self.source):
            raise ValueError('Bind the actual complete caller and all scalar-progress source identities')
        self.counts={key:0 for key in COUNT_KEYS}
        self.values={key:None for key in SLOTS}
        self.current_state='prepared; no field read or acceptance inferred'
        self.trial=None
        self.last_completed_trial=None
        self.last_completed_trial_record=None
        self.completed_trial_record_chain=None
        self.accepted_keys=set()
        self.accepted_metric=0
        self.accepted_restoration=0
        self.report_complete=False
        self.stop=None
        self.last_failure=None
        self.last_report_saved_at=None
        self.last_event='prepared'
        self.point_digest_seconds=0.
        self._write()

    def failure(self,phase,error):
        self.counts['observation_failures']+=1
        self.last_failure=dict(phase=str(phase)[:160],type=type(error).__name__,
            reason=str(error)[:700],recorded_at_utc=_utc(),
            scientific_success_or_failure_inferred=False)
        self.last_event='observation-unavailable'
        if phase in ('initial-statistics-returned','final-statistics-returned',
                     'accepted-checkpoint-returned','report-snapshot','report-saved'):
            self.values['current_statistics']=None
            self.values['current_geometry']=None
            self.current_state='current scalar observation unavailable; no replacement point inferred'
        elif phase in ('current-geometry-returned','final-geometry-returned'):
            self.values['current_geometry']=None
        if str(phase).startswith('trial-'):
            self.values['latest_trial_statistics']=None
            self.values['latest_trial_geometry']=None
        self._write()


    def _preserve_completed_trial(self,value):
        # These are already returned original scalars, not another scientific read.
        statistics=self.values['latest_trial_statistics']
        geometry=self.values['latest_trial_geometry']
        point=self.trial['point_sha256']
        for item in (statistics,geometry):
            if item is not None and item.get('point_sha256')!=point:
                raise ValueError('Do not move a previous trial scalar onto a new trial point')
        booleans={}
        for key in ('metric_descent_required','full_true_geometry_read','domain_feasible',
                    'actual_Phi_descent','physically_feasible'):
            original=value.get(key)
            booleans[key]=original if isinstance(original,bool) else None
        completed=dict(schema=COMPLETED_TRIAL_SCHEMA,source_sha256=self.source,
            driver_source_sha256=self.driver,model_identity_sha256=self.model,
            mathematical_target_identity_sha256=self.target,point_sha256=point,
            recorded_at_utc=_utc(),decision_sequence=self.counts['trial_decisions'],
            phase=self.trial.get('phase'),serial=self.trial.get('serial'),
            index=self.trial.get('index'),alpha=self.trial.get('alpha'),
            accepted=value['accepted'],decision_returned=True,
            actual_positive_physical_g=_number(value.get('actual_positive_physical_g')),
            actual_seconds=_number(value.get('actual_seconds')),
            actual_read_error=self.trial.get('actual_read_error'),
            statistics=_same(statistics),geometry=_same(geometry),**booleans,
            accepted_checkpoint_or_final_inferred=False,
            raw_scientific_arrays_or_resume_execution_state=False)
        self.last_completed_trial=completed
        self.last_completed_trial_record=None
        try:
            raw=(json.dumps(completed,sort_keys=True,separators=(',',':'),
                allow_nan=False)+'\n').encode()
            if len(raw)>=MAX_FILE_BYTES:
                raise ValueError('Returned trial scalar record exceeds the original small-file bound')
            directory=self.path.parent/'completed-mathematical-trial-scalars'
            directory.mkdir(parents=True,exist_ok=True)
            path=directory/('trial-%06d.json'%self.counts['trial_decisions'])
            if path.exists():
                if path.read_bytes()!=raw:
                    raise ValueError('Do not replace a different immutable returned trial scalar record')
            else:
                pending=path.with_name(path.name+'.pending')
                pending.write_bytes(raw)
                os.replace(pending,path)
            record=dict(path=str(path.resolve()),bytes=len(raw),
                sha256=hashlib.sha256(raw).hexdigest(),point_sha256=point,
                source_sha256=self.source,decision_sequence=self.counts['trial_decisions'])
            self.completed_trial_record_chain=canonical(dict(
                previous=self.completed_trial_record_chain,record=record))
            self.last_completed_trial_record=record
            self.counts['completed_trial_scalar_files_written']+=1
        except Exception as error:
            self.counts['completed_trial_scalar_file_failures']+=1
            self.last_failure=dict(phase='immutable returned trial scalar write',
                type=type(error).__name__,reason=str(error)[:700],recorded_at_utc=_utc(),
                scientific_success_or_failure_inferred=False)

    def observe(self,event,value,*,point_sha256,phase=None,serial=None,
                point_digest_seconds=0.):
        self.counts['events']+=1
        self.counts['point_digest_reads']+=1
        seconds=_number(point_digest_seconds)
        if seconds is None or seconds<0 or not _digest(point_sha256):
            raise ValueError('Keep the actual point digest read and its elapsed time')
        self.point_digest_seconds+=seconds
        self.last_event=event
        if event=='trial-start':
            self.counts['trial_starts']+=1
            self.values['latest_trial_statistics']=None
            self.values['latest_trial_geometry']=None
            self.trial=dict(point_sha256=point_sha256,phase=phase,serial=serial,
                index=value.get('index'),alpha=_number(value.get('alpha')),
                decision_returned=False,accepted=None,actual_read_error=None)
        elif event in ('initial-statistics-returned','trial-statistics-returned','final-statistics-returned'):
            r=_statistics(value,point_sha256,self.objective,source=self.source,
                model=self.model,driver=self.driver,state=event)
            value['actual_scalar_progress_binding']=_same(r)
            self.counts['statistics_returns']+=1
            if event=='initial-statistics-returned':
                self.values['initial_statistics']=r
                self.values['current_statistics']=_same(r)
                self.current_state='initial statistics returned; no accepted direction'
            elif event=='final-statistics-returned':
                self.values['current_statistics']=r
                self.current_state='final statistics returned; final report not yet saved'
            else:
                if self.trial is None or self.trial['point_sha256']!=point_sha256:
                    raise ValueError('Keep each trial start and its own statistics point')
                self.values['latest_trial_statistics']=r
        elif event in ('initial-geometry-returned','current-geometry-returned',
                       'trial-geometry-returned','final-geometry-returned'):
            r=_geometry(value,point_sha256,source=self.source,model=self.model,
                driver=self.driver,state=event)
            value['actual_scalar_progress_binding']=_same(r)
            self.counts['geometry_returns']+=1
            if event=='initial-geometry-returned':
                self.values['initial_geometry']=r
                self.values['current_geometry']=_same(r)
            elif event=='trial-geometry-returned':
                if self.trial is None or self.trial['point_sha256']!=point_sha256:
                    raise ValueError('Keep each trial geometry at its own actual point')
                self.values['latest_trial_geometry']=r
            else:
                self.values['current_geometry']=r
        elif event=='trial-decision-returned':
            if self.trial is None or self.trial['point_sha256']!=point_sha256:
                raise ValueError('Do not attach a trial decision to another point')
            if not isinstance(value.get('accepted'),bool):
                raise ValueError('Keep the actual boolean decision, not a descent inference')
            self.counts['trial_decisions']+=1
            self.trial.update(decision_returned=True,accepted=value['accepted'],
                actual_read_error=(None if value.get('actual_read_error') is None
                    else str(value['actual_read_error'])[:700]))
            self._preserve_completed_trial(value)
        elif event=='accepted-checkpoint-returned':
            if (value.get('accepted') is not True or not isinstance(value.get('accepted_bundle'),dict)
                    or phase not in ('metric','restoration') or type(serial) is not int):
                raise ValueError('Keep the actual accepted decision and returned checkpoint record')
            a=value['accepted_statistics'].get('actual_scalar_progress_binding')
            g=value['accepted_geometry'].get('actual_scalar_progress_binding')
            if (not isinstance(a,dict) or not isinstance(g,dict)
                    or a.get('point_sha256')!=point_sha256 or g.get('point_sha256')!=point_sha256):
                raise ValueError('Keep the accepted statistics and geometry at the same actual point')
            key=(phase,serial)
            if key in self.accepted_keys:
                raise ValueError('Do not count the same accepted direction twice')
            self.accepted_keys.add(key)
            self.counts['accepted_checkpoint_returns']+=1
            if phase=='metric':
                self.accepted_metric+=1
            else:
                self.accepted_restoration+=1
            self.values['current_statistics']=_same(a)
            self.values['current_geometry']=_same(g)
            self.current_state='accepted '+phase+' checkpoint returned; final report not inferred'
        else:
            raise ValueError('Use only the declared original completed-operation observation events')
        self._write()

    def _sync_report(self,report):
        if (report.get('model_identity_sha256')!=self.model
                or report.get('source_sha256')!=self.driver
                or report.get('selected_scalar_objective_key')!=self.objective):
            raise ValueError('Keep the same complete actual report and objective')
        current=report.get('current')
        if isinstance(current,dict):
            bound=current.get('actual_scalar_progress_binding')
            self.values['current_statistics']=_same(bound) if isinstance(bound,dict) else None
        if isinstance(report.get('final_geometry'),dict):
            bound=report['final_geometry'].get('actual_scalar_progress_binding')
            self.values['current_geometry']=_same(bound) if isinstance(bound,dict) else None
        self.accepted_metric=sum(v.get('accepted') is True for v in report['metric_directions'])
        self.accepted_restoration=sum(v.get('accepted') is True for v in report['restoration_directions'])
        self.report_complete=report.get('complete') is True
        self.stop=report.get('stop_reason')
        if self.report_complete:
            self.current_state='all original calculations returned; original report complete flag is true'
        elif report.get('initial_failed_candidate_is_not_an_accepted_field') is True:
            self.current_state='initial field read failed; any returned statistics remain a failed-candidate observation'

    def report_snapshot(self,report):
        self._sync_report(report)
        result=self.snapshot()
        result['snapshot_scope']='complete scalar snapshot prepared immediately before original report serialization'
        result['mutable_file_reread_or_final_completion_inferred']=False
        result['original_normal_progress_snapshot']=capture_original_progress(report)
        return result

    def report_saved(self,report):
        self._sync_report(report)
        self.counts['report_saves']+=1
        self.last_report_saved_at=_utc()
        self.last_event='original-full-report-saved'
        self._write()

    def snapshot(self):
        current_a=self.values['current_statistics']
        current_g=self.values['current_geometry']
        return dict(schema=SCHEMA,source_sha256=self.source,
            driver_source_sha256=self.driver,model_identity_sha256=self.model,
            mathematical_target_identity_sha256=self.target,
            objective_key=self.objective,recorded_at_utc=_utc(),event=self.last_event,
            current_state=self.current_state,report_complete=self.report_complete,
            stop_reason=self.stop,accepted_metric_count=self.accepted_metric,
            accepted_restoration_count=self.accepted_restoration,
            accepted_direction_count=self.accepted_metric+self.accepted_restoration,
            current_statistics_and_geometry_same_point=(None if current_a is None or current_g is None
                else current_a['point_sha256']==current_g['point_sha256']),
            **_same(self.values),latest_trial=_same(self.trial),
            last_completed_trial=_same(self.last_completed_trial),
            last_completed_trial_record=_same(self.last_completed_trial_record),
            completed_trial_scalar_record_chain_sha256=self.completed_trial_record_chain,
            actual_counts=dict(self.counts),point_digest_seconds=self.point_digest_seconds,
            last_failure=_same(self.last_failure),last_report_saved_at_utc=self.last_report_saved_at,
            scientific_field_calls_by_observer=0,scientific_J_calls_by_observer=0,
            scientific_root_calls_by_observer=0,continuous_bound_claimed=False,
            mutable_progress_is_an_immutable_final_or_parent=False)

    def _write(self):
        try:
            self.counts['writes']+=1
            raw=(json.dumps(self.snapshot(),sort_keys=True,separators=(',',':'),
                allow_nan=False)+'\n').encode()
            if len(raw)>=MAX_FILE_BYTES:
                raise ValueError('Scalar progress exceeds its explicit small-file bound')
            self.path.parent.mkdir(parents=True,exist_ok=True)
            pending=self.path.with_name(self.path.name+'.pending')
            pending.write_bytes(raw)
            os.replace(pending,self.path)
        except Exception as error:
            self.counts['write_failures']+=1
            self.last_failure=dict(phase='atomic scalar progress write',type=type(error).__name__,
                reason=str(error)[:700],recorded_at_utc=_utc(),
                scientific_success_or_failure_inferred=False)



def _validate_completed_trial(snapshot,report,source,driver):
    item=snapshot.get('last_completed_trial')
    record=snapshot.get('last_completed_trial_record')
    chain=snapshot.get('completed_trial_scalar_record_chain_sha256')
    if chain is not None and not _digest(chain):
        raise ValueError('Keep the actual returned-scalar record chain digest or null')
    if item is None:
        if record is not None:
            raise ValueError('A scalar file cannot stand for an unobserved trial')
        return None
    if (not isinstance(item,dict) or item.get('schema')!=COMPLETED_TRIAL_SCHEMA
            or item.get('source_sha256')!=source or item.get('driver_source_sha256')!=driver
            or item.get('model_identity_sha256')!=report.get('model_identity_sha256')
            or item.get('mathematical_target_identity_sha256')!=report.get('predeclared_mathematical_target_identity_sha256')
            or not _digest(item.get('point_sha256')) or item.get('decision_returned') is not True
            or not isinstance(item.get('accepted'),bool)
            or type(item.get('decision_sequence')) is not int or item['decision_sequence']<1
            or item.get('accepted_checkpoint_or_final_inferred') is not False
            or item.get('raw_scientific_arrays_or_resume_execution_state') is not False):
        raise ValueError('Keep a genuinely returned decision at its own actual source and point')
    for slot in ('statistics','geometry'):
        bound=item.get(slot)
        if bound is None:
            continue
        if (not isinstance(bound,dict) or bound.get('schema')!=BINDING_SCHEMA
                or bound.get('source_sha256')!=source or bound.get('driver_source_sha256')!=driver
                or bound.get('model_identity_sha256')!=report['model_identity_sha256']
                or bound.get('point_sha256')!=item['point_sha256']):
            raise ValueError('Retained trial scalars must belong to that same actual trial')
        if slot=='geometry':
            maximum=bound.get('maximum_physical_g')
            expected=max(0,maximum) if bound.get('complete') is True and maximum is not None else None
            if (maximum is not None and _number(maximum) is None
                    or bound.get('positive_physical_g')!=expected
                    or bound.get('recorded_geometry_point_sha256') not in (None,item['point_sha256'])
                    or bound.get('complete') is True and bound.get('recorded_geometry_point_sha256')!=item['point_sha256']):
                raise ValueError('A retained partial trial screen is not a complete same-point violation')
            _validate_geometry_components(bound)
        elif (bound.get('objective_key')!=report['selected_scalar_objective_key']
                or any(bound.get(k) is not None and _number(bound[k]) is None
                    for k in ('Phi','max_relative_gram','legacy_max_relative_gram',
                              'min_relative_E','min_relative_determinant'))):
            raise ValueError('Keep the original returned trial objective and statistics')
    if record is not None:
        if (not isinstance(record,dict) or not isinstance(record.get('path'),str)
                or type(record.get('bytes')) is not int or not 0<record['bytes']<MAX_FILE_BYTES
                or not _digest(record.get('sha256')) or record.get('source_sha256')!=source
                or record.get('point_sha256')!=item['point_sha256']
                or record.get('decision_sequence')!=item['decision_sequence'] or chain is None):
            raise ValueError('Keep the actual optional immutable scalar file identity')
        exact=(json.dumps(item,sort_keys=True,separators=(',',':'),allow_nan=False)+'\n').encode()
        if len(exact)!=record['bytes'] or hashlib.sha256(exact).hexdigest()!=record['sha256']:
            raise ValueError('The retained scalar file record does not name these complete captured scalar bytes')
    # The pure reader does not consume the mutable progress file or make an
    # optional scalar side file a new requirement for the scientific report.
    phase=item.get('phase')
    if phase not in ('metric','restoration'):
        raise ValueError('Keep the actual scientific direction phase')
    for direction in report[phase+'_directions']:
        if direction.get('serial')!=item.get('serial'):
            continue
        for trial in direction.get('trials',[]):
            if trial.get('index')!=item.get('index'):
                continue
            if (trial.get('accepted')!=item['accepted']
                    or _number(trial.get('alpha'))!=item.get('alpha')
                    or _number(trial.get('actual_seconds'))!=item.get('actual_seconds')
                    or _number(trial.get('actual_positive_physical_g'))!=item.get('actual_positive_physical_g')):
                raise ValueError('Retained decision differs from the original surviving trial')
            for key in ('metric_descent_required','full_true_geometry_read','domain_feasible',
                        'actual_Phi_descent','physically_feasible'):
                original=trial.get(key)
                expected=original if isinstance(original,bool) else None
                if item.get(key)!=expected:
                    raise ValueError('Retained decision hypothesis differs from its original returned boolean')
            original_error=trial.get('actual_read_error')
            expected_error=None if original_error is None else str(original_error)[:700]
            if item.get('actual_read_error')!=expected_error:
                raise ValueError('Keep the original bounded actual read-error text')
            for slot,key in (('statistics','statistics'),('geometry','full_geometry')):
                raw=trial.get(key)
                bound=None if raw is None else raw.get('actual_scalar_progress_binding')
                if bound!=item.get(slot):
                    raise ValueError('Retained trial scalar differs from its surviving original object')
            return True
    return None


def validate_report_progress(report,*,source_sha256,driver_sha256):
    """Pure validation of the immutable copy in the actual full report.

    The mutable monitoring file is deliberately not read. Values from a point
    that has no surviving full statistics/geometry object stay source-bound
    scalar observations; they are not promoted to a continuous certificate.
    """
    if sha(__file__)!=source_sha256 or report.get('source_sha256')!=driver_sha256:
        raise ValueError('Keep the actual complete observer and driver source')
    if report.get('mathematical_progress_definition')!=definition():
        raise ValueError('Keep the whole scalar observation policy')
    value=report.get('actual_mathematical_observation')
    if value is None:
        return dict(available=False,source_sha256=source_sha256,
            reason='No complete scalar report snapshot was serialized',
            numerical_failure_or_success_inferred=False)
    if (not isinstance(value,dict) or value.get('schema')!=SCHEMA
            or value.get('source_sha256')!=source_sha256
            or value.get('driver_source_sha256')!=driver_sha256
            or value.get('model_identity_sha256')!=report.get('model_identity_sha256')
            or value.get('mathematical_target_identity_sha256')!=report.get('predeclared_mathematical_target_identity_sha256')
            or value.get('objective_key')!=report.get('selected_scalar_objective_key')
            or value.get('snapshot_scope')!='complete scalar snapshot prepared immediately before original report serialization'
            or value.get('mutable_file_reread_or_final_completion_inferred') is not False):
        raise ValueError('Keep the actual report, target, source, point and snapshot boundary')
    counts=value.get('actual_counts')
    if not isinstance(counts,dict) or set(counts)!=set(COUNT_KEYS) or any(type(n) is not int or n<0 for n in counts.values()):
        raise ValueError('Keep every actual observation counter')
    if (counts['write_failures']>counts['writes']
            or _number(value.get('point_digest_seconds')) is None or value['point_digest_seconds']<0):
        raise ValueError('Keep the actual bounded observer costs')
    for key in SLOTS:
        item=value.get(key)
        if item is None:
            continue
        if (not isinstance(item,dict) or item.get('schema')!=BINDING_SCHEMA
                or item.get('source_sha256')!=source_sha256
                or item.get('driver_source_sha256')!=driver_sha256
                or item.get('model_identity_sha256')!=report['model_identity_sha256']
                or not _digest(item.get('point_sha256'))):
            raise ValueError('Every returned scalar record retains its own actual complete point')
        if key.endswith('statistics'):
            if item.get('objective_key')!=report['selected_scalar_objective_key']:
                raise ValueError('Do not change the original scalar objective')
            for field in ('Phi','max_relative_gram','legacy_max_relative_gram','min_relative_E','min_relative_determinant'):
                if item.get(field) is not None and _number(item[field]) is None:
                    raise ValueError('Keep finite existing scalar values or explicit null')
        else:
            maximum=item.get('maximum_physical_g')
            expected=max(0,maximum) if item.get('complete') is True and maximum is not None else None
            if (maximum is not None and _number(maximum) is None
                    or item.get('positive_physical_g')!=expected
                    or item.get('recorded_geometry_point_sha256') not in (None,item['point_sha256'])
                    or item.get('complete') is True and item.get('recorded_geometry_point_sha256')!=item['point_sha256']):
                raise ValueError('Do not turn a partial or different-point screen into a complete violation')
            _validate_geometry_components(item)
    completed_match=_validate_completed_trial(value,report,source_sha256,driver_sha256)
    raw_pairs=(('initial_statistics',report.get('initial')),('current_statistics',report.get('current')),
        ('initial_geometry',report.get('initial_geometry')),('current_geometry',report.get('final_geometry')))
    matches={}
    for key,raw in raw_pairs:
        if raw is None:
            matches[key]=None
            continue
        bound=raw.get('actual_scalar_progress_binding')
        if bound is None:
            matches[key]=None
            continue
        if bound!=value.get(key):
            raise ValueError('Scalar snapshot differs from its surviving actual report object')
        if key.endswith('statistics'):
            for field in ('max_relative_gram','legacy_max_relative_gram','min_relative_E','min_relative_determinant'):
                if bound[field]!=_number(raw.get(field)):
                    raise ValueError('A scalar observation changed its original statistics')
            if bound['Phi']!=_number(raw['spectral'].get(report['selected_scalar_objective_key'])):
                raise ValueError('The actual scalar objective differs')
        else:
            if (bound['complete']!=(raw.get('complete') is True)
                    or bound['maximum_physical_g']!=_number(raw.get('maximum_physical_g'))):
                raise ValueError('The actual finite geometry observation differs')
            _validate_geometry_components(bound,raw)
        matches[key]=True
    accepted=[sum(r.get('accepted') is True for r in report[key]) for key in ('metric_directions','restoration_directions')]
    if (value.get('accepted_metric_count')!=accepted[0] or value.get('accepted_restoration_count')!=accepted[1]
            or value.get('accepted_direction_count')!=sum(accepted)
            or value.get('report_complete')!=(report.get('complete') is True)
            or value.get('stop_reason')!=report.get('stop_reason')
            or any(value.get(k)!=0 for k in ('scientific_field_calls_by_observer','scientific_J_calls_by_observer','scientific_root_calls_by_observer'))
            or value.get('continuous_bound_claimed') is not False
            or value.get('mutable_progress_is_an_immutable_final_or_parent') is not False):
        raise ValueError('Acceptance and completion come only from the actual full report')
    normal=value.get('original_normal_progress_snapshot')
    if not isinstance(normal,dict) or not isinstance(normal.get('available'),bool):
        raise ValueError('Keep the original complete normal progress capture or honest unavailability')
    if normal['available']:
        record=normal.get('record',{})
        if (type(record.get('bytes')) is not int or not 0<=record['bytes']<MAX_FILE_BYTES
                or not _digest(record.get('sha256'))
                or normal.get('two_complete_bounded_reads_agreed') is not True
                or normal.get('original_normal_point_not_relabelled_as_current_iterate') is not True
                or normal.get('mutable_origin_is_not_an_immutable_final_or_parent') is not True
                or canonical(normal.get('complete_value'))!=normal.get('complete_value_identity_sha256')):
            raise ValueError('Keep the actual complete captured normal metadata identity')
        _validate_original_progress_value(normal['complete_value'],report)
    result=_same(value)
    result.update(available=True,actual_surviving_report_objects_compared=matches,
        last_completed_trial_surviving_report_comparison=completed_match,
        mutable_progress_file_consumed=False,pure_validation_did_not_evaluate_F_J_or_roots=True)
    return result
