#!/usr/bin/env python3
"""Strict complete N-only history and original-free-word transfer.

Fixed scalar/chart/seed/radial/integration/control definitions are compared in
full. The current finite observer is independently N4096. Old tagged indices
are decoded with their original N2048 before union; no physical value or root
is imported. Original final-array reads require public Actions.
"""
import ast
import copy
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import struct
import sys
from types import SimpleNamespace

SCHEMA='complete-dyadic-angular-history-and-free-word-transfer-v1'
CURRENT_OPERATOR_SCHEMA='complete-angular-refined-reference-centred-C1-fixed-normal-plane-SO3-v1'
ORIGINAL_BASE_SHA256='6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865'
ORIGINAL_FRAME_SHA256='ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9'
HISTORY_SOURCE_SHA256 = '4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60'
ORIGINAL_DRIVER_SHA256 = 'cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5'
ORIGINAL_READER_SHA256 = '104e014062f29969c0c94884bf810b6f9b23999ad8cc902238f981a9b0ad35f7'
ORIGINAL_OPERATOR_SHA256 = 'a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd'
ORIGINAL_CALIBRATION_SHA256 = '3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991'
ORIGINAL_REPORT_SCHEMA = 'complete-R711-reference-centred-C1-material-envelope-fixed-normal-plane-SO3-QP-v1'
ORIGINAL_OPERATOR_SCHEMA = 'complete-R711-reference-centred-C1-reuse-SO3-fixed-normal-plane-six-control-layer-v1'
ORIGINAL_READER_RELATIVE = 'scripts/resume_20261126/read_reference_centred_c1_material_envelope_so3_report.py'
ADDRESS_ROLES = ('curvature_points', 'radius_points', 'protected_curvature_points')
TYPE_KEYS = ('family', 'location', 'partner', 'branch', 'sign')

def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Actual complete history transfer requires public repository Actions')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
        allow_nan=False).encode()).hexdigest()


def _record_bytes(path):
    path = Path(path).resolve()
    raw = path.read_bytes()
    record = dict(path=str(path),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
    return record,raw


def _same_bytes(record):
    path = Path(record['path'])
    if path.stat().st_size != record['bytes'] or sha(path) != record['sha256']:
        raise ValueError('An actual history input changed during its complete consumption')


def _literal_assignments(raw):
    result = {}
    for node in ast.parse(raw).body:
        if isinstance(node,ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0],ast.Name):
            if node.targets[0].id in ('SCHEMA','SOURCE_PINS'):
                result[node.targets[0].id] = ast.literal_eval(node.value)
    if set(result) != {'SCHEMA','SOURCE_PINS'}:
        raise ValueError('Bind the complete actual caller source and role table')
    return result


def _point(value):
    if (not isinstance(value,(tuple,list)) or len(value) != 3
            or isinstance(value[0],bool) or int(value[0]) != value[0]
            or not 0 <= int(value[0]) < 922
            or any(isinstance(v,bool) or not isinstance(v,(float,int))
                or not math.isfinite(v) for v in value[1:])
            or not 0 <= float(value[1]) <= 1
            or not 0 <= float(value[2]) <= math.pi/2):
        raise ValueError('Keep the complete literal same-mesh material point')
    return int(value[0]),float(value[1]).hex(),float(value[2]).hex()


def _address_fingerprints(arrays):
    if not isinstance(arrays,dict) or set(arrays) != set(ADDRESS_ROLES):
        raise ValueError('Serialize all three complete explicit role arrays')
    result,sets = {},{}
    for role in ADDRESS_ROLES:
        if not isinstance(arrays[role],list):
            raise ValueError('The whole explicit address array must remain a list')
        words = [_point(row) for row in arrays[role]]
        if len(words) != len(set(words)):
            raise ValueError('The complete explicit union must not carry duplicate words')
        sets[role] = set(words)
        result[role] = dict(count=len(words),exact_binary_word_set_sha256=canonical(sorted(words)))
    if not sets['protected_curvature_points'] <= sets['curvature_points']:
        raise ValueError('Every protected known address must remain in complete curvature memory')
    return result


def _from_witnesses(witnesses,radii):
    arrays = dict(curvature_points=[[int(v['cell']),float(v['u']),float(v['phi'])] for v in witnesses],
        radius_points=[[int(v['cell']),float(v['u']),float(v['phi'])] for v in radii],
        protected_curvature_points=[[int(v['cell']),float(v['u']),float(v['phi'])]
            for v in witnesses if v.get('protected',False)])
    for role in ADDRESS_ROLES:
        arrays[role].sort(key=_point)
    _address_fingerprints(arrays)
    return arrays


def _type(row):
    if not isinstance(row,dict) or not all(key in row for key in TYPE_KEYS):
        raise ValueError('Keep every original family/location/partner/branch/sign component')
    return {key:copy.deepcopy(row[key]) for key in TYPE_KEYS}


def _typed_key(row):
    return canonical(_type(row))


def _terminal(value):
    if value.get('complete') is True:
        return 'complete-original-budget-report'
    if (value.get('complete') is False
            and value.get('stop_reason') == 'actual_initial_zero_closure_field_read_failed'
            and isinstance(value.get('actual_initial_read_error'),str)
            and value.get('initial_failed_candidate_is_not_an_accepted_field') is True
            and not value.get('metric_directions') and not value.get('restoration_directions')):
        return 'explicit-original-initial-field-failure-report'
    raise ValueError('Do not consume a future, still-running or unclosed partial envelope report as terminal history')


def _old_reader(topic):
    path = topic/ORIGINAL_READER_RELATIVE
    if sha(path) != ORIGINAL_READER_SHA256:
        raise ValueError('Use the complete original corrected 104e reader')
    name = '_complete_original_envelope_transfer_reader_'+ORIGINAL_READER_SHA256
    spec = importlib.util.spec_from_file_location(name,path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    if sha(module.read_report.__code__.co_filename) != ORIGINAL_READER_SHA256:
        raise ValueError('The complete original report reader body changed')
    return module


def _restore_annotations(envelope,rows):
    for old in rows:
        key = _typed_key(old)
        current = envelope._separation.get(key)
        if current is None or _type(current) != _type(old):
            raise ValueError('The unchanged same-model restore lost a complete typed address')
        if current['first_discovered_current_full_point_sha256'] != old['first_discovered_current_full_point_sha256']:
            raise ValueError('Retain the actual original first-discovery point')
        # This restores only the same-source record's provenance fields.  It
        # does not substitute a different-model envelope into old restore().
        envelope._separation[key] = copy.deepcopy(old)


def _digest(value):
    if (not isinstance(value,str) or len(value) != 64
            or any(character not in '0123456789abcdef' for character in value)):
        raise ValueError('Keep an actual complete source/model/point digest')
    return value


def definition():
    return dict(schema=SCHEMA,source_sha256=sha(__file__),
        original_complete_driver_sha256=ORIGINAL_DRIVER_SHA256,
        original_complete_reader_sha256=ORIGINAL_READER_SHA256,
        original_complete_operator_sha256=ORIGINAL_OPERATOR_SHA256,
        reference_full_N=2048,current_full_N=4096,
        original_material_chart_reference_seed_mesh_and_free_layout_frozen=True,
        old_literal_angles_at_all_even_current_columns=True,
        all_history_indices_resolved_with_own_original_N_before_union=True,
        all_original_typed_rows_and_discovery_provenance_retained=True,
        complete_13_member_parent_checkpoint_supported=True,
        original_free_point_words_copied_without_interpolation=True,
        explicit_independent_reference_start_supported=True,
        unknown_parallel_typed_metadata_inherited=False,
        subsequently_available_peer_history_remains_binding_obligation=True,
        old_numerical_field_values_roots_Phi_or_certificates_inherited=False,
        radial_mesh_refinement_performed=False)


def _compatible_models(old,new,current_pins):
    """Normalize ONLY declared observation/source identities, compare everything else."""
    if (old.get('schema')!=ORIGINAL_OPERATOR_SCHEMA
            or old.get('source_sha256')!=ORIGINAL_OPERATOR_SHA256
            or new.get('schema')!=CURRENT_OPERATOR_SCHEMA
            or new.get('source_sha256')!=current_pins['endpoint'][1]
            or new.get('base_source_sha256')!=current_pins['meridian'][1]
            or new.get('new_reference_input_binding_source_sha256')!=current_pins['new_moment_input'][1]):
        raise ValueError('Only the complete declared original and N-refined sources may be compared')
    before,after=copy.deepcopy(old),copy.deepcopy(new)
    ob,nb=before['base_complete_model'],after['base_complete_model']
    if (ob.get('source_sha256')!=ORIGINAL_BASE_SHA256 or nb.get('source_sha256')!=current_pins['meridian'][1]
            or canonical(ob)!=before['base_model_identity_sha256']
            or canonical(nb)!=after['base_model_identity_sha256']):
        raise ValueError('Full base identities must match before observation normalization')
    observer=_module(Path(current_pins['_topic'])/current_pins['angular_observation'][0],current_pins['angular_observation'][1])
    observer.validate_base_model(nb)
    for key in ('angular_observation_refinement','reference_full_N','current_full_N'):
        nb.pop(key)
    for value in (ob,nb):
        value.pop('schema');value.pop('source_sha256')
    if ob!=nb:
        raise ValueError('The full fixed scalar/reference/chart/seed/radial mesh or original free layout changed')
    base_semantics=canonical(ob)
    for value in (before,after):
        value['base_model_identity_sha256']=base_semantics
        value['base_complete_model']=copy.deepcopy(ob)
        for key in ('schema','source_sha256','base_source_sha256','base_schema',
                    'literal_Q_input_schema','new_reference_input_binding_source_sha256'):
            value.pop(key)
        calibration=value['reference_centering_definition']
        if calibration['base_model_identity_sha256'] not in (old['base_model_identity_sha256'],new['base_model_identity_sha256']):
            raise ValueError('Reference calibration must bind its own actual complete base')
        calibration['base_model_identity_sha256']=base_semantics
        calibration.pop('source_sha256');calibration.pop('endpoint_source_sha256')
        value['normal_frame_C1_reuse'].pop('source_sha256')
        Q=value['frozen_moment_Q_definition']
        if Q['base_model_identity_sha256'] not in (old['base_model_identity_sha256'],new['base_model_identity_sha256']):
            raise ValueError('Literal Q definition must bind its own actual base')
        Q['base_model_identity_sha256']=base_semantics
        Q.pop('schema')
        value['frozen_moment_Q_definition_identity_sha256']=canonical(Q)
    # These are strict source checks; they are not inferred merely because
    # deleting a source field leaves equal mathematical descriptions.
    for value,calibration,frame in ((old,ORIGINAL_CALIBRATION_SHA256,ORIGINAL_FRAME_SHA256),
            (new,current_pins['reference_calibration'][1],current_pins['frame_C1'][1])):
        if (value['reference_centering_definition']['source_sha256']!=calibration
                or value['reference_centering_definition']['endpoint_source_sha256']!=value['source_sha256']
                or value['normal_frame_C1_reuse']['source_sha256']!=frame):
            raise ValueError('Full calibration and C1 source identities changed outside this declared family')
    if before!=after:
        raise ValueError('Only source/schema and the explicit finite observer may change, not any field/root/target parameter')
    return dict(complete_fixed_field_definition_sha256=canonical(before),
        old_complete_model_identity_sha256=canonical(old),new_complete_model_identity_sha256=canonical(new),
        all_fixed_reference_target_chart_seed_mesh_Q_gamma_tau_and_free_layout_equal=True,
        only_declared_observation_source_and_dependent_identity_fields_changed=True,
        computed_floating_fields_equal_claimed=False,old_Phi_inherited=False)


def _module(path,digest):
    if sha(path)!=digest:
        raise ValueError('Changed complete source '+str(path))
    name='_angular_transfer_'+digest
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module
    spec.loader.exec_module(module)
    return module


def _pins(args,current_driver_source):
    record,raw=_record_bytes(current_driver_source)
    pins=_literal_assignments(raw)['SOURCE_PINS']
    if pins.get('envelope_transfer',(None,None))[1]!=sha(__file__):
        raise ValueError('The complete caller must bind this actual N-transfer source')
    topic=Path(args.repo).resolve()/'topics/visible-flex-larger-amplitude'
    for role,(relative,digest) in pins.items():
        if sha(topic/relative)!=digest:
            raise ValueError('A complete actual caller source changed: '+role)
    pins['_topic']=str(topic)
    return record,pins


def _complete_input_reports(payload,*,current_carrier_sha256):
    """Read every actually recorded inbound history JSON, without truncating a chain."""
    pending=list(payload.get('history',{}).get('sources',[]))
    seen={};result=[]
    while pending:
        recorded=pending.pop(0)
        if not isinstance(recorded,dict) or not all(k in recorded for k in ('path','sha256','bytes')):
            raise ValueError('A complete parent history input needs its actual entire file record')
        key=(recorded['path'],recorded['sha256'])
        if key in seen:
            continue
        actual,raw=_record_bytes(recorded['path'])
        if actual!=recorded:
            raise ValueError('An actual inbound original history JSON changed')
        value=json.loads(raw)
        seen[key]=True
        if value.get('schema')=='R690-independent-axisymmetric-SO3-preparation-v1':
            # The full preparation is already bound by the same reference
            # model. Its explicit locations are a separate recorded source.
            result.append(dict(record=actual,kind='complete_preparation',payload=value))
            continue
        carrier=value.get('carrier_sha256',value.get('observation_carrier_sha256'))
        if carrier!=current_carrier_sha256:
            raise ValueError('Every inherited explicit history source must bind the same unchanged radial carrier')
        declared=value.get('N',value.get('full_angles',value.get('full_N')))
        if declared is not None and declared!=2048:
            raise ValueError('The original cc0a history has its own fixed N2048 interpretation')
        result.append(dict(record=actual,kind='complete_original_N_history',payload=value))
        history=value.get('history',{})
        if isinstance(history,dict):
            pending.extend(history.get('sources',[]))
    return result


def load_memory(args,preparation,q,history,*,memory,current_driver_source,restart=None):
    require_actions()
    caller,pins=_pins(args,current_driver_source)
    if (sha(memory.__file__)!=pins['envelope_memory'][1]
            or sha(history.Locations.walk.__code__.co_filename)!=HISTORY_SOURCE_SHA256
            or canonical(q.model)!=q.identity):
        raise ValueError('Use the complete current model, memory and original history walker')
    parent_path=getattr(args,'material_envelope_seed_report',None)
    checkpoint=getattr(args,'material_envelope_seed_checkpoint',None)
    independent=bool(getattr(args,'independent_reference_start',False))
    if restart is not None:
        if parent_path is not None or checkpoint is not None or independent:
            raise ValueError('A complete same-source restart is distinct from a new branch or old final seed')
    elif independent:
        if parent_path is not None or checkpoint is not None:
            raise ValueError('The explicit frozen-reference branch cannot also copy an old final')
    elif parent_path is None or checkpoint is None:
        raise ValueError('Choose an actual complete parent pair or explicit independent reference start')
    parents=[]
    manifests=list(args.manifest)
    parent_paths=[Path(v).resolve() for v in getattr(args,'material_envelope_parent_report',[])]
    if parent_path is not None and parent_path not in parent_paths:
        parent_paths.append(parent_path)
    if len(parent_paths)!=len(set(parent_paths)):
        raise ValueError('Do not duplicate a complete original history parent')
    for path in parent_paths:
        record,raw=_record_bytes(path)
        parent_payload=json.loads(raw)
        pure=_old_reader(Path(pins['_topic'])).read_report(args.repo,path,verify_final_bundle=True)
        _same_bytes(record)
        terminal=_terminal(parent_payload)
        if (pure.get('report_sha256')!=record['sha256']
                or parent_payload.get('source_sha256')!=ORIGINAL_DRIVER_SHA256
                or parent_payload.get('N')!=2048
                or parent_payload.get('observation_carrier_sha256')!=sha(args.carrier)
                or parent_payload.get('bundle_sha256')!=sha(args.reference_bundle)):
            raise ValueError('The actual fully read original parent must bind this same complete reference/carrier')
        relation=_compatible_models(parent_payload['representation'],q.model,pins)
        origin=history.Locations(q.J,q.P,2048)
        inbound=_complete_input_reports(parent_payload,current_carrier_sha256=sha(args.carrier))
        for item in inbound:
            if item['kind']=='complete_preparation':
                if item['payload'].get('reference_definition')!=preparation['reference_definition']:
                    raise ValueError('An inbound preparation belongs to another complete fixed reference')
                continue
            memory._walk_at_declared_N(origin,item['payload'],history,args.carrier,
                label='complete_original_inbound_history',default_N=2048)
            if item['record']['path'] not in {str(v) for v in manifests}:
                manifests.append(Path(item['record']['path']))
        origin.walk(parent_payload,path=('whole_complete_original_parent',))
        origin.resolve_grid(args.carrier)
        parent_arrays=origin.arrays()
        _address_fingerprints(parent_arrays)
        parents.append(dict(report=record,actual_terminal_report_kind=terminal,
            actual_model_identity_sha256=parent_payload['model_identity_sha256'],model_binding=relation,
            complete_inbound_history_records=[dict(record=v['record'],kind=v['kind']) for v in inbound],
            complete_original_role_arrays=parent_arrays,original_role_fingerprints=_address_fingerprints(parent_arrays),
            original_typed_rows=copy.deepcopy(parent_payload['material_envelope']['actual_separation_memory']['rows'])))
        if str(path) not in {str(v) for v in manifests}:
            manifests.append(path)
    proxy=SimpleNamespace(**vars(args));proxy.manifest=manifests
    witnesses,radii,history_record,envelope=memory.load_memory(proxy,preparation,q,history,
        restart=restart,source_report_path=args.restart_report if restart is not None else None)
    previous_parents=[]
    if restart is not None:
        previous=restart.get('angular_history_transfer')
        validate_metadata(previous,model=q.model,envelope=restart['material_envelope'],
            caller_source_sha256=caller['sha256'],carrier_sha256=sha(args.carrier),pins=pins)
        _restore_annotations(envelope,restart['material_envelope']['actual_separation_memory']['rows'])
        previous_parents=copy.deepcopy(previous['actual_parent_reports'])
        independent=previous['independent_original_reference_branch']
    for parent in parents:
        current=_from_witnesses(witnesses,radii)
        for role in ADDRESS_ROLES:
            if not {_point(v) for v in parent['complete_original_role_arrays'][role]} <= {_point(v) for v in current[role]}:
                raise ValueError('A full original explicit or protected address was omitted by N transfer')
        for ordinal,row in enumerate(parent['original_typed_rows']):
            envelope._separate(row['family'],row['location'],partner=row['partner'],branch=row['branch'],
                sign=row['sign'],token=row['first_discovered_current_full_point_sha256'])
            key=_typed_key(row)
            actual=envelope._separation[key]
            if _type(actual)!=_type(row):
                raise ValueError('A complete old typed family/branch/sign/partner was omitted')
            origin=dict(source_report=parent['report'],
                source_model_identity_sha256=parent['actual_model_identity_sha256'],
                original_ordinal=ordinal,original_full_row=copy.deepcopy(row),
                old_physical_values_or_feasibility_inherited=False)
            origins=actual.setdefault('angular_refinement_origins',[])
            if origin not in origins:
                origins.append(origin)
    combined={v['report']['sha256']:v for v in previous_parents}
    for parent in parents:
        key=parent['report']['sha256']
        if key in combined and combined[key]!=parent:
            raise ValueError('An already retained original parent cannot change under the same whole SHA')
        combined[key]=parent
    parents=list(combined.values())
    arrays=_from_witnesses(witnesses,radii)
    record=dict(schema=SCHEMA,source_sha256=sha(__file__),definition=definition(),
        actual_current_driver_sha256=caller['sha256'],actual_current_model_identity_sha256=q.identity,
        current_carrier_sha256=sha(args.carrier),actual_parent_reports=parents,
        complete_explicit_role_arrays=arrays,complete_explicit_role_fingerprints=_address_fingerprints(arrays),
        independent_original_reference_branch=independent,
        original_reference_full_N=2048,current_full_N=4096,
        original_complete_P0_and_old_and_new_grids_retained=True,
        exact_original_angle_words_at_even_columns=True,
        old_tagged_indices_reinterpreted=False,unknown_peer_typed_metadata_inherited=False,
        future_actual_peer_memory_merge_obligation_retained=True,
        old_field_values_roots_Phi_acceptance_or_certificates_inherited=False)
    history_record['angular_history_transfer']=copy.deepcopy(record)
    return witnesses,radii,history_record,envelope,record


def validate_metadata(value,*,model,envelope,caller_source_sha256,carrier_sha256,pins):
    if (not isinstance(value,dict) or value.get('schema')!=SCHEMA
            or value.get('source_sha256')!=sha(__file__) or value.get('definition')!=definition()
            or value.get('actual_current_driver_sha256')!=caller_source_sha256
            or value.get('actual_current_model_identity_sha256')!=canonical(model)
            or value.get('current_carrier_sha256')!=carrier_sha256
            or value.get('original_reference_full_N')!=2048 or value.get('current_full_N')!=4096):
        raise ValueError('Bind the entire actual angular history transfer')
    for key in ('original_complete_P0_and_old_and_new_grids_retained','exact_original_angle_words_at_even_columns',
                'future_actual_peer_memory_merge_obligation_retained'):
        if value.get(key) is not True:
            raise ValueError('Incomplete original/refined observation responsibility')
    for key in ('old_tagged_indices_reinterpreted','unknown_peer_typed_metadata_inherited',
                'old_field_values_roots_Phi_acceptance_or_certificates_inherited'):
        if value.get(key) is not False:
            raise ValueError('Do not reinterpret or inherit an unpaid old field value')
    arrays=value.get('complete_explicit_role_arrays')
    if _address_fingerprints(arrays)!=value.get('complete_explicit_role_fingerprints'):
        raise ValueError('Complete explicit role arrays changed')
    if type(value.get('independent_original_reference_branch')) is not bool:
        raise ValueError('Declare the actual independent-versus-parent origin')
    parents=value.get('actual_parent_reports')
    if (not isinstance(parents,list) or (not value['independent_original_reference_branch'] and not parents)
            or len({v['report']['sha256'] for v in parents})!=len(parents)):
        raise ValueError('The actual branch origin cannot be invented or lost')
    actual_rows=envelope['actual_separation_memory']['rows']
    by_type={_typed_key(v):v for v in actual_rows}
    for parent in parents:
        _same_bytes(parent['report'])
        payload=json.loads(Path(parent['report']['path']).read_bytes())
        inbound=_complete_input_reports(payload,current_carrier_sha256=carrier_sha256)
        if [dict(record=v['record'],kind=v['kind']) for v in inbound]!=parent.get('complete_inbound_history_records'):
            raise ValueError('Keep the entire original input-history closure, not only returned extrema')
        if (payload.get('source_sha256')!=ORIGINAL_DRIVER_SHA256 or _terminal(payload)!=parent['actual_terminal_report_kind']
                or payload.get('N')!=2048 or payload.get('observation_carrier_sha256')!=carrier_sha256
                or canonical(payload['representation'])!=parent['actual_model_identity_sha256']
                or _compatible_models(payload['representation'],model,pins)!=parent['model_binding']
                or parent['original_typed_rows']!=payload['material_envelope']['actual_separation_memory']['rows']):
            raise ValueError('The complete original returned parent and same-fixed-target relation changed')
        if _address_fingerprints(parent['complete_original_role_arrays'])!=parent['original_role_fingerprints']:
            raise ValueError('Complete original known-role identity changed')
        for role in ADDRESS_ROLES:
            if not {_point(v) for v in parent['complete_original_role_arrays'][role]} <= {_point(v) for v in arrays[role]}:
                raise ValueError('The full parent known protected or ordinary memory was truncated')
        for ordinal,row in enumerate(parent['original_typed_rows']):
            kept=by_type.get(_typed_key(row),{})
            matches=[v for v in kept.get('angular_refinement_origins',[])
                if v.get('source_report')==parent['report'] and v.get('original_ordinal')==ordinal]
            if (len(matches)!=1 or matches[0].get('original_full_row')!=row
                    or matches[0].get('source_model_identity_sha256')!=parent['actual_model_identity_sha256']
                    or matches[0].get('old_physical_values_or_feasibility_inherited') is not False):
                raise ValueError('Every actual old typed row and first-discovery provenance is permanent')
        _same_bytes(parent['report'])
    return dict(schema=SCHEMA,source_sha256=sha(__file__),
        actual_current_model_identity_sha256=canonical(model),
        independent_original_reference_branch=value['independent_original_reference_branch'],
        actual_complete_parent_count=len(parents),
        complete_explicit_role_fingerprints=copy.deepcopy(value['complete_explicit_role_fingerprints']),
        original_reference_full_N=2048,current_full_N=4096,
        all_old_even_and_new_full_observation_responsibility_retained=True,
        same_fixed_g_proved_by_complete_definition_equality=bool(parents),
        old_values_or_certificates_inherited=False)


def seed_from_complete_prior_final(args, q, *, current_driver_source, transfer_record):
    """Optional complete old free-variable copy; no old field or root is loaded."""
    require_actions()
    checkpoint = getattr(args,'material_envelope_seed_checkpoint',None)
    report_path = getattr(args,'material_envelope_seed_report',None)
    if checkpoint is None and report_path is None:
        return None,None
    if checkpoint is None or report_path is None or args.restart_checkpoint is not None:
        raise ValueError('An explicit old final seed needs its two files and cannot also be a same-source restart')
    caller_record,caller_bytes = _record_bytes(current_driver_source)
    pins = _literal_assignments(caller_bytes)['SOURCE_PINS']
    if (pins.get('envelope_transfer',(None,None))[1] != sha(__file__)
            or transfer_record.get('actual_current_driver_sha256') != caller_record['sha256']
            or transfer_record.get('actual_current_model_identity_sha256') != q.identity
            or canonical(q.model) != q.identity):
        raise ValueError('Bind the explicit final seed to the same complete caller/model/history transfer')
    source_record,raw = _record_bytes(report_path)
    parents = [item for item in transfer_record['actual_parent_reports']
        if item['report'] == source_record]
    if len(parents) != 1:
        raise ValueError('The final seed report must be an explicitly and completely transferred prior envelope')
    payload = json.loads(raw)
    topic = Path(args.repo).resolve()/'topics/visible-flex-larger-amplitude'
    pure = _old_reader(topic).read_report(args.repo,report_path,verify_final_bundle=True)
    _same_bytes(source_record)
    if (pure.get('report_sha256') != source_record['sha256']
            or payload.get('complete') is not True
            or payload.get('schema') != ORIGINAL_REPORT_SCHEMA
            or payload.get('source_sha256') != ORIGINAL_DRIVER_SHA256
            or payload.get('final_statistics') is None
            or payload.get('final_geometry',{}).get('complete') is not True):
        raise ValueError('Only an actual complete final field, fully read by the original reader, supplies variable words')
    pins['_topic']=str(topic)
    model_binding = _compatible_models(payload['representation'],q.model,pins)
    bundle_record,bundle_bytes = _record_bytes(checkpoint)
    if (bundle_record['sha256'] != payload.get('final_bundle_sha256')
            or pure.get('actual_final_bundle_sha256') != bundle_record['sha256']):
        raise ValueError('The complete old final bundle must be exactly the reported returned bytes')
    # This numerical array read is runner-only.  The old operator is never
    # constructed or executed, and its root/cache data is never imported.
    import io
    import numpy as np
    base_globals = q.base.__class__.__init__.__globals__
    array_sha = base_globals['array_sha']
    if (sha(q.base.__class__.__init__.__code__.co_filename) != pins['meridian'][1]
            or sha(array_sha.__code__.co_filename) != pins['meridian'][1]):
        raise ValueError('Use the actual complete unchanged free-layout source and array identity function')
    before_model = canonical(q.model)
    frozen_initial = array_sha(q.base.initial())
    if frozen_initial != q.reference_point_sha256:
        raise ValueError('Keep the original complete supported-reference point fixed before copying any final variables')
    names = {'schema','omega_jets','core','Hcap','mesh','fixed_parent_core',
        'zero_closure_model_json','zero_closure_model_identity_sha256',
        'base_so3_model_identity_sha256','fixed_scalar_metric_identity_sha256',
        'endpoint_root_policy_json','working_integration_order','working_full_angles'}
    with np.load(io.BytesIO(bundle_bytes),allow_pickle=False) as saved:
        if set(saved.files) != names or len(saved.files) != len(names):
            raise ValueError('Read every declared old checkpoint member without aliases or extra hidden state')
        if (str(saved['schema'].item()) != ORIGINAL_OPERATOR_SCHEMA
                or str(saved['zero_closure_model_identity_sha256'].item()) != payload['model_identity_sha256']
                or json.loads(str(saved['zero_closure_model_json'].item())) != payload['representation']
                or str(saved['base_so3_model_identity_sha256'].item()) != payload['representation']['base_model_identity_sha256']
                or str(saved['fixed_scalar_metric_identity_sha256'].item()) != q.context.scalar_identity
                or json.loads(str(saved['endpoint_root_policy_json'].item())) != q.policy.metadata()
                or saved['working_integration_order'].shape != ()
                or saved['working_full_angles'].shape != ()
                or int(saved['working_integration_order'].item()) != q.integration_order
                or int(saved['working_full_angles'].item()) != 2048):
            raise ValueError('Keep the actual old checkpoint complete model, exact target and working integration contract')
        arrays = {name:np.array(saved[name],copy=True) for name in
            ('omega_jets','core','Hcap','mesh','fixed_parent_core')}
    expected_shapes = dict(omega_jets=(q.J,3,q.n),core=q.parent_core.shape,
        Hcap=(),mesh=q.mesh.shape,fixed_parent_core=q.parent_core.shape)
    for name,value in arrays.items():
        if value.dtype != np.dtype(float) or value.shape != expected_shapes[name] or not np.isfinite(value).all():
            raise ValueError('Every complete original array must have its actual finite binary64 layout: '+name)
    same_words = lambda a,b: (a.dtype == b.dtype and a.shape == b.shape
        and np.ascontiguousarray(a).tobytes() == np.ascontiguousarray(b).tobytes())
    if (not same_words(arrays['mesh'],q.mesh)
            or not same_words(arrays['fixed_parent_core'],q.parent_core)
            or not same_words(arrays['core'][:q.K],q.parent_core[:q.K])):
        raise ValueError('The complete actual fixed chart, exact fixed core slots or mesh carrier changed')
    flat = arrays['omega_jets'].reshape(3*q.J,q.n)
    result = np.r_[arrays['core'][q.K:],flat[q.radial_free].ravel(),float(arrays['Hcap'])]
    core,omega,height = q.unpack(result)
    if (result.shape != (q.free_size,) or not same_words(core,arrays['core'])
            or not same_words(omega,arrays['omega_jets'])
            or not same_words(np.array(height),arrays['Hcap'])):
        raise ValueError('Copy every original free word and verify the entire reconstructed core/rotation/height arrays')
    point = array_sha(result)
    old_metadata = payload.get('latest_operator_metadata',{})
    if (old_metadata.get('current_full_point_sha256') != point
            or payload['final_geometry'].get('current_full_point_sha256') != point):
        raise ValueError('The returned full-variable words must be the same point as the original complete final reads')
    if (canonical(q.model) != before_model or array_sha(q.base.initial()) != frozen_initial
            or q.reference_point_sha256 != frozen_initial):
        raise ValueError('Copying a final seed must not change the model or the original frozen reference')
    _same_bytes(source_record)
    _same_bytes(bundle_record)
    _same_bytes(caller_record)
    directions = payload.get('metric_directions',[])+payload.get('restoration_directions',[])
    accepted = sum(int(item.get('accepted') is True) for item in directions)
    record = dict(schema='actual-prior-envelope-final-original-variable-seed-v1',
        source_sha256=sha(__file__),actual_current_driver_sha256=caller_record['sha256'],
        actual_current_model_identity_sha256=q.identity,source_report=source_record,
        source_checkpoint=bundle_record,original_complete_reader_sha256=ORIGINAL_READER_SHA256,
        source_driver_sha256=ORIGINAL_DRIVER_SHA256,
        source_complete_model_identity_sha256=payload['model_identity_sha256'],
        complete_model_binding=model_binding,source_complete_field_read=True,
        source_final_true_sampled_geometry_feasible=payload['final_true_sampled_geometry_feasible'],
        source_actual_accepted_direction_count=accepted,
        actual_full_free_point_sha256=point,frozen_original_reference_point_sha256=frozen_initial,
        actual_full_free_variable_count=q.free_size,
        complete_saved_array_sha256={name:array_sha(value) for name,value in arrays.items()},
        actual_free_layout=dict(J=q.J,n=q.n,K=q.K,core_size=q.core_size,
            rotation_size=q.rotation_size,free_size=q.free_size,
            radial_free_sha256=array_sha(q.radial_free)),
        all_original_variable_words_copied_and_reconstructed=True,
        fixed_reference_model_and_original_initial_words_unchanged=True,
        old_roots_caches_physical_values_Phi_or_certificates_inherited=False,
        new_initial_metric_geometry_roots_and_norm_must_be_read=True,
        current_field_already_read_by_variable_copy=False)
    return result,record


def validate_seed_metadata(value, *, report, model, transfer):
    """Pure byte/provenance checks; no old value is a new initial statistic."""
    requested = report.get('explicit_prior_final_variable_seed_requested')
    if type(requested) is not bool:
        raise ValueError('State whether an actual old final was explicitly requested as the variable seed')
    _digest(report.get('initial_full_variable_point_sha256'))
    if value is None:
        if requested:
            raise ValueError('An explicitly requested old final seed must retain its complete actual record')
        return None
    if (not requested or not isinstance(value,dict)
            or value.get('schema') != 'actual-prior-envelope-final-original-variable-seed-v1'
            or value.get('source_sha256') != sha(__file__)
            or value.get('actual_current_driver_sha256') != report['source_sha256']
            or value.get('actual_current_model_identity_sha256') != canonical(model)
            or value.get('source_driver_sha256') != ORIGINAL_DRIVER_SHA256
            or value.get('original_complete_reader_sha256') != ORIGINAL_READER_SHA256
            or value.get('actual_full_free_point_sha256') != report['initial_full_variable_point_sha256']
            or value.get('frozen_original_reference_point_sha256') != report['actual_reference_initial_full_point_sha256']
            or value.get('actual_full_free_variable_count') != report['original_variables']
            or report.get('restart') is not None or report.get('direct_base_seed') is not None):
        raise ValueError('An explicit old final must be a complete original-variable seed for this independently read model')
    for key in ('all_original_variable_words_copied_and_reconstructed',
            'fixed_reference_model_and_original_initial_words_unchanged',
            'source_complete_field_read','new_initial_metric_geometry_roots_and_norm_must_be_read'):
        if value.get(key) is not True:
            raise ValueError('Keep the complete source-bound full-variable copy and new-read responsibility')
    for key in ('old_roots_caches_physical_values_Phi_or_certificates_inherited',
            'current_field_already_read_by_variable_copy'):
        if value.get(key) is not False:
            raise ValueError('An old final variable copy is not a new field certificate or reused physical value')
    parent_record = value.get('source_report')
    parents = [item for item in transfer['actual_parent_reports'] if item['report'] == parent_record]
    if (len(parents) != 1 or parents[0]['actual_terminal_report_kind'] != 'complete-original-budget-report'
            or value.get('source_complete_model_identity_sha256') != parents[0]['actual_model_identity_sha256']
            or value.get('complete_model_binding') != parents[0]['model_binding']):
        raise ValueError('The explicit final must belong to the same fully imported terminal history')
    checkpoint = value.get('source_checkpoint',{})
    _digest(checkpoint.get('sha256'))
    if (not isinstance(checkpoint.get('path'),str) or type(checkpoint.get('bytes')) is not int
            or checkpoint['bytes'] < 1):
        raise ValueError('Keep the actual complete checkpoint file record')
    arrays = value.get('complete_saved_array_sha256')
    if not isinstance(arrays,dict) or set(arrays) != {'omega_jets','core','Hcap','mesh','fixed_parent_core'}:
        raise ValueError('Keep every complete saved physical array identity')
    for digest in arrays.values():
        _digest(digest)
    layout = value.get('actual_free_layout',{})
    if (set(layout) != {'J','n','K','core_size','rotation_size','free_size','radial_free_sha256'}
            or any(type(layout[key]) is not int or layout[key] < 1
                for key in ('J','n','K','core_size','rotation_size','free_size'))
            or layout['J'] != report['J'] or layout['free_size'] != report['original_variables']
            or layout['core_size']+layout['rotation_size']+1 != layout['free_size']):
        raise ValueError('Keep the actual complete free-layout record')
    _digest(layout['radial_free_sha256'])
    count = value.get('source_actual_accepted_direction_count')
    if (type(count) is not int or count < 0
            or type(value.get('source_final_true_sampled_geometry_feasible')) is not bool):
        raise ValueError('Report prior actual acceptance and geometry separately, without upgrading a final to an accepted step')
    initial = report.get('initial')
    snapshot = initial.get('endpoint_roots') if isinstance(initial,dict) else report.get('initial_endpoint_roots')
    if isinstance(snapshot,dict):
        point = snapshot.get('current_full_point_sha256')
        if point is not None and point != value['actual_full_free_point_sha256']:
            raise ValueError('The initial current-source root snapshot belongs to a different free point')
    return copy.deepcopy(value)

