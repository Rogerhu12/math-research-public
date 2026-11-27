#!/usr/bin/env python3
"""Complete same-Fejer M160 to M320 words, addresses and typed-history transfer.

Only an actually returned complete 477499/274d Fejer parent can supply its
thirteen-member final and complete typed/protected discoveries. Independent
reference-zero inclusion and same-source restart are distinct explicit modes.
The older pre-Fejer targets remain source-bound unresolved provenance only.
No old field values, selected roots, norm, acceptance or certificate transfer.
All original history/role inputs are reread; no ancestry or typed row is capped.
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


SCHEMA = "complete-fixed-fejer-M160-to-M320-history-transfer-v1"
ANALYTIC_BINDING_SOURCE_SHA256 = "caf16fbc87ef618ddae5ba42616d9bbe136beac6d32487224073ac6958c4d3c0"
MEMORY_SOURCE_SHA256 = 'c79c7f7ec1febf0ab6dca30d28a91b1566745972342c7336a3a9a106f56b3152'
CURRENT_MEMORY_SOURCE_SHA256 = "9f268e066274eff19ee2635124a8addf9c92eabf6d7177249f4ac4782c88a39a"
HISTORICAL_INDEPENDENT_MEMORY_SOURCE_SHA256 = '4d92ca2387523a76bbea0a3444e0665c306369dd0351c3354c998a09884e043b'
LAYOUT_SOURCE_SHA256 = "67c5503e8df036aa1468a3df2f395f5a33c91c4309520fbb8862b39c2495a251"
HISTORY_SOURCE_SHA256 = '4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60'
ORIGINAL_DRIVER_SHA256 = 'cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5'
ORIGINAL_READER_SHA256 = '104e014062f29969c0c94884bf810b6f9b23999ad8cc902238f981a9b0ad35f7'
ORIGINAL_OPERATOR_SHA256 = 'a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd'
ORIGINAL_CALIBRATION_SHA256 = '3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991'
ORIGINAL_REPORT_SCHEMA = 'complete-R711-reference-centred-C1-material-envelope-fixed-normal-plane-SO3-QP-v1'
ORIGINAL_OPERATOR_SCHEMA = 'complete-R711-reference-centred-C1-reuse-SO3-fixed-normal-plane-six-control-layer-v1'
ORIGINAL_READER_RELATIVE = 'scripts/resume_20261126/read_reference_centred_c1_material_envelope_so3_report.py'
ADDRESS_ROLES = ('curvature_points','radius_points','protected_curvature_points')
TYPE_KEYS = ('family','location','partner','branch','sign')
PARENT_FAMILIES = {
    'c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1': dict(
        report_schema='complete-run10-detached-closure-value-material-envelope-SO3-QP-v1',
        reader_sha256='2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e',
        reader_relative='scripts/resume_20261126/read_run10_detached_closure_so3_report.py',
        operator_sha256='6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4',
        operator_schema='complete-R711-reference-centred-detached-closure-values-analytic-frame-J3-normal-layer-v1',
        memory_sha256='f1c6629fc52e17ad8cc74d1fd2431e3e7ee132e9da2b46ed4cf63a14e99d38ba'),
    'ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5': dict(
        report_schema='complete-run09-public-reference-analytic-frame-material-envelope-SO3-QP-v1',
        reader_sha256='aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32',
        reader_relative='scripts/resume_20261126/read_run09_public_reference_analytic_frame_so3_report_v2.py',
        operator_sha256='3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc',
        operator_schema='complete-R711-reference-centred-analytic-frame-and-J3-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1',
        memory_sha256='2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb'),
    '0dfb96e53fa92e741e2d94819636486b45c49e341006370d1c6864ce70c36b51': dict(
        report_schema='complete-R711-reference-centred-analytic-J3-independent-chart-material-envelope-fixed-normal-plane-SO3-QP-v1',
        reader_sha256='c2a6039633dbb397bdb6f56358153a362ed4e34c8e035a6a739eb23d5a1b785e',
        reader_relative='scripts/resume_20261126/read_reference_centred_analytic_j3_material_envelope_so3_report.py',
        operator_sha256='04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e',operator_schema='complete-R711-reference-centred-analytic-J3-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1',
        memory_sha256=HISTORICAL_INDEPENDENT_MEMORY_SOURCE_SHA256),
    ORIGINAL_DRIVER_SHA256: dict(report_schema=ORIGINAL_REPORT_SCHEMA,
        reader_sha256=ORIGINAL_READER_SHA256,reader_relative=ORIGINAL_READER_RELATIVE,
        operator_sha256=ORIGINAL_OPERATOR_SHA256,operator_schema=ORIGINAL_OPERATOR_SCHEMA,
        memory_sha256=MEMORY_SOURCE_SHA256),
    '95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9': dict(
        report_schema='complete-R711-reference-centred-independent-chart-material-envelope-fixed-normal-plane-SO3-QP-v1',
        reader_sha256='f382bedb07fdf43e3fd94ac411c4a072519494dd2a16ec19ab627492d9606470',
        reader_relative='scripts/resume_20261126/read_reference_centred_independent_chart_material_envelope_so3_report.py',
        operator_sha256='d5da5e3db88a03cc0afdc00e3a6bc74e425aa3f1b730ea7f66ac278f93d8e6eb',
        operator_schema='complete-R711-reference-centred-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1',
        memory_sha256=HISTORICAL_INDEPENDENT_MEMORY_SOURCE_SHA256)}


PARENT_FAMILIES['477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd'] = dict(
    report_schema='complete-fixed-fejer-immutable-point-material-envelope-SO3-QP-v1',
    reader_sha256='274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b',
    reader_relative='scripts/resume_20261126/read_fixed_fejer_immutable_point_so3_report.py',
    operator_sha256='1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778',
    operator_schema='complete-fixed-fejer-reference-centred-immutable-point-closure-values-analytic-frame-J3-normal-layer-v1',
    memory_sha256=CURRENT_MEMORY_SOURCE_SHA256)

def _parent_family(source, payload=None):
    if source not in PARENT_FAMILIES:
        raise ValueError('Use one complete explicitly supported original parent source')
    family=PARENT_FAMILIES[source]
    if payload is not None and (payload.get('source_sha256')!=source
            or payload.get('schema')!=family['report_schema']
            or payload.get('representation',{}).get('source_sha256')!=family['operator_sha256']
            or payload.get('representation',{}).get('schema')!=family['operator_schema']
            or payload.get('material_envelope',{}).get('source_sha256')!=family['memory_sha256']):
        raise ValueError('The parent report must bind its own complete source, field and memory')
    return family


def requested_parent_memory(args):
    """Select a complete loader only; load_memory still performs every full read."""
    selected=None
    for filename in getattr(args,'material_envelope_parent_report',[]):
        record,raw=_record_bytes(filename)
        value=json.loads(raw)
        memory=_parent_family(value.get('source_sha256'),value)['memory_sha256']
        if selected is not None and selected!=memory:
            raise ValueError('Do not mix different full material-envelope policies in one transfer')
        selected=memory
        _same_bytes(record)
    return selected



def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Actual complete history transfer requires public repository Actions')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
        allow_nan=False).encode()).hexdigest()


def definition():
    return dict(schema=SCHEMA,source_sha256=sha(__file__),
        unchanged_complete_memory_source_sha256=MEMORY_SOURCE_SHA256,
        complete_original_history_walker_sha256=HISTORY_SOURCE_SHA256,
        supported_prior_driver_sha256=ORIGINAL_DRIVER_SHA256,
        supported_prior_complete_reader_sha256=ORIGINAL_READER_SHA256,
        supported_prior_operator_sha256=ORIGINAL_OPERATOR_SHA256,
        supported_prior_calibration_sha256=ORIGINAL_CALIBRATION_SHA256,
        complete_explicit_parent_families=copy.deepcopy(PARENT_FAMILIES),
        pre_fejer_parent_families_are_provenance_not_current_target_parents=True,
        complete_actual_fejer_M160_parent_and_all_thirteen_final_members_supported=True,
        frequency_layout_source_sha256=LAYOUT_SOURCE_SHA256,reference_M=160,current_M=320,J=923,full_N=2048,
        complete_fixed_fejer_target_reference_seed_mesh_observer_Q_gamma_partition_retained=True,
        three_unequal_rotation_blocks_copied_with_explicit_new_zero_modes=True,
        full_actual_fixed_input_target_and_mathematical_recipe_validation_retained=True,
        previous_target_complete_finals_or_field_values_supported_as_new_target=False,
        predeclared_fixed_fejer_RN_even_binary64_chart=True,
        fixed_mathematical_recipe_distinct_from_mesh_and_execution=True,
        old_known_literal_addresses_reinterpreted_on_new_target=True,
        same_old_physical_s_or_point_claimed=False,
        actual_run10_c3dc_complete_terminal_report_and_full13_final_transfer_supported=False,
        same_run10_fixed_target_claimed=False,
        immutable_point_storage_does_not_change_any_equation_or_outer_budget=True,
        historical_parent_families_retained_for_source_bound_unknown_peer_obligations=True,
        prior_pending_parallel_obligations_preserved_as_complete_source_bound_origins=True,
        each_current_pending_run_has_an_explicit_whole_parent_driver_source=True,
        fresh_entry_requires_actual_terminal_prior_envelope_report=False,
        default_strict_entry_requires_actual_terminal_prior_envelope_report=True,
        explicit_independent_memory_source_sha256=CURRENT_MEMORY_SOURCE_SHA256,
        strict_terminal_transfer_memory_source_sha256=CURRENT_MEMORY_SOURCE_SHA256,
        new_current_restorer_source_sha256='e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb',
        actual_fixed_input_binding_source_sha256='3da43e82722dfb4548ff4e8b454d47ec2626ece76084c7801c0be5b8c989670f',
        actual_origin_run_id=None,actual_origin_run_attempt=None,
        whole_actual_input_binding_sha256=None,
        independent_chart_is_a_predeclared_complete_target=True,
        strict_terminal_model_relationship_is_not_relaxed_for_new_chart=True,
        original_complete_scan_and_typed_separation_mathematics_retained=True,
        explicit_independent_branch_uses_complete_reinterpreted_P0_and_initial_current_grid=True,
        independent_branch_uses_frozen_original_reference_free_point=True,
        pending_peer_values_or_typed_priority_inherited=False,
        previous_target_unreturned_history_reconstructed=False,
        previous_target_completion_claimed=False,
        actual_later_peer_material_queries_require_explicit_reinterpretation_not_value_migration=True,
        current_source_same_model_complete_restart_also_supported=True,
        all_current_reference_base_chart_carrier_and_envelope_policy_must_match=True,
        changed_model_fields='only current M160-to-M320 layout, explicit frozen-point coordinate identities and whole bound source policies; same complete fixed Fejer target and unchanged radial/angular observer',
        complete_analytic_source_and_report_binding_sha256=ANALYTIC_BINDING_SOURCE_SHA256,
        original_same_model_restore_guard_unchanged=True,
        prior_complete_reports_consumed_by_original_walker=True,
        complete_known_explicit_roles_and_protected_addresses_serialized=True,
        all_actual_same_target_typed_rows_retained_without_eviction_or_count_cap=True,
        typed_first_discovery_point_retains_own_source_provenance=True,
        old_unknown_protected_labels_or_order_reconstructed=False,
        old_field_values_root_states_jacobians_or_acceptance_inherited=False,
        cross_new_model_equivalence_of_computed_float_fields_claimed=False,
        all_addresses_and_types_require_actual_new_field_reread=True,
        explicit_old_pre_fejer_complete_final_free_variable_words_supported=False,
        explicit_same_target_fejer_M160_complete_final_free_variable_words_supported=True,
        complete_same_source_restart_retains_all_thirteen_checkpoint_members=True,
        fixed_reference_seed_is_not_reselected_from_old_final=True)

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


def _old_reader(topic, family):
    path=topic/family['reader_relative']
    expected=family['reader_sha256']
    if sha(path)!=expected:
        raise ValueError('Use the complete actual original parent reader')
    name='_complete_original_envelope_transfer_reader_'+expected
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    if sha(module.read_report.__code__.co_filename)!=expected:
        raise ValueError('The complete original report reader body changed')
    return module


def _compatible_models(old,new,current_pins,*,frozen_point_relation):
    path=Path(__file__).with_name('fixed_fejer_frequency_source_binding.py')
    if (sha(path)!=ANALYTIC_BINDING_SOURCE_SHA256
            or current_pins.get('analytic_J3_binding',(None,None))[1]!=ANALYTIC_BINDING_SOURCE_SHA256):
        raise ValueError('Bind the complete explicit new local-matrix model relation')
    name='_complete_analytic_J3_model_relation_'+ANALYTIC_BINDING_SOURCE_SHA256
    if name not in sys.modules:
        spec=importlib.util.spec_from_file_location(name,path)
        module=importlib.util.module_from_spec(spec)
        sys.modules[name]=module
        spec.loader.exec_module(module)
    module=sys.modules[name]
    if sha(module.compatible_legacy_model.__code__.co_filename)!=ANALYTIC_BINDING_SOURCE_SHA256:
        raise ValueError('The complete model-relation function changed')
    return module.compatible_legacy_model(old,new,current_pins,source_directory=path.parent,
        frozen_point_relation=frozen_point_relation)


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


def load_memory(args, preparation, q, history, *, memory, current_driver_source,
                restart=None, source_report_path=None):
    require_actions()
    actual_memory_sha=sha(memory.__file__)
    if (q.M!=320 or q.n!=962 or q.J!=923 or q.full_N!=2048 or q.N!=513
            or q.base.reference_M!=160):
        raise ValueError('Use the exact M320 current layout with the frozen M160/N2048 reference')
    if (actual_memory_sha != CURRENT_MEMORY_SOURCE_SHA256
            or sha(history.Locations.walk.__code__.co_filename) != HISTORY_SOURCE_SHA256):
        raise ValueError('Keep both complete original history consumers unchanged')
    for function in (memory.load_memory,memory.validate_report_metadata,
            memory.MaterialEnvelope._separate,memory.MaterialEnvelope.restore,memory.MaterialEnvelope.metadata):
        if sha(function.__code__.co_filename) != actual_memory_sha:
            raise ValueError('The actual full memory method differs from its bound source')
    topic = Path(args.repo).resolve()/'topics/visible-flex-larger-amplitude'
    caller_record,caller_bytes = _record_bytes(current_driver_source)
    caller = _literal_assignments(caller_bytes)
    pins = caller['SOURCE_PINS']
    if (pins.get('envelope_transfer',(None,None))[1] != sha(__file__)
            or pins.get('envelope_memory',(None,None))[1] != MEMORY_SOURCE_SHA256
            or pins.get('independent_envelope_memory',(None,None))[1] != CURRENT_MEMORY_SOURCE_SHA256
            or pins.get('history',(None,None))[1] != HISTORY_SOURCE_SHA256
            or pins.get('endpoint',(None,None))[1] != q.model.get('source_sha256')
            or pins.get('reference_calibration',(None,None))[1]
                != q.model.get('reference_centering_definition',{}).get('source_sha256')
            or canonical(q.model) != q.identity):
        raise ValueError('Bind the complete actual caller, model, original memory and this independent transfer')
    for relative,expected in pins.values():
        if sha(topic/relative) != expected:
            raise ValueError('The full actual current runtime source closure changed')
    frozen_relation=_frozen_initial_points(q,pins)
    current_carrier_sha = sha(args.carrier)
    expected_policy = memory.definition(args.envelope_near_active_rows)
    paths = [Path(path).resolve() for path in getattr(args,'material_envelope_parent_report',[])]
    if len(paths) != len(set(paths)):
        raise ValueError('State each actual parent report once in its explicit ordered input list')
    independent=getattr(args,'independent_envelope_branch',False)
    pending=list(getattr(args,'pending_parallel_envelope_run',[]))
    pending_sources={}
    for item in getattr(args,'pending_parallel_envelope_source',[]):
        fields=item.split('=')
        if (len(fields)!=2 or fields[0] in pending_sources
                or fields[1] not in PARENT_FAMILIES):
            raise ValueError('Each pending run must explicitly name one supported complete parent driver')
        pending_sources[fields[0]]=fields[1]
    if set(pending_sources)!=set(pending):
        raise ValueError('Bind every declared unknown peer run one-to-one to its actual source family')
    if (type(independent) is not bool or len(pending)!=len(set(pending))
            or any(not isinstance(v,str) or len(v.split('/'))!=2
                or any(not w.isdigit() or int(w)<1 or str(int(w))!=w for w in v.split('/')) for v in pending)):
        raise ValueError('Use explicit canonical run/attempt identities for unread parallel obligations')
    if independent and (paths or restart is not None or source_report_path is not None
            or any(getattr(args,key,None) is not None for key in ('restart_checkpoint',
                'restart_report','seed_so3_checkpoint','seed_so3_report',
                'material_envelope_seed_checkpoint','material_envelope_seed_report'))):
        raise ValueError('An independent fresh branch uses the original reference, without an unknown prior final')
    if pending and not independent:
        raise ValueError('Pending peer declarations belong only to the explicit independent fresh branch')
    if not paths and restart is None and not independent:
        raise ValueError('The default strict continuation still requires its actual prior terminal report')
    parent_memory=requested_parent_memory(args)
    expected_memory=(CURRENT_MEMORY_SOURCE_SHA256 if independent else
        restart.get('material_envelope',{}).get('source_sha256') if restart is not None else parent_memory)
    if (expected_memory!=actual_memory_sha
            or (parent_memory is not None and parent_memory!=actual_memory_sha)):
        raise ValueError('Select the exact complete memory of the explicitly bound parent family')

    parents = []
    for path in paths:
        record,raw = _record_bytes(path)
        payload = json.loads(raw)
        family=_parent_family(payload.get('source_sha256'),payload)
        if family['memory_sha256']!=actual_memory_sha:
            raise ValueError('The captured complete parent changed the selected memory family')
        pure = _old_reader(topic,family).read_report(args.repo,path,verify_final_bundle=False)
        if pure.get('report_sha256') != record['sha256']:
            raise ValueError('The original reader and captured whole parent bytes are different snapshots')
        _same_bytes(record)
        if (payload.get('observation_carrier_sha256') != current_carrier_sha
                or payload.get('N') != q.full_N or payload.get('J') != q.J
                or payload.get('M')!=160
                or payload.get('original_variables') != q.base.frequency_layout_definition['original_free_size']
                or float(payload.get('material_envelope_active_band',math.nan)).hex() != float(args.active_band).hex()
                or payload.get('bundle_sha256') != sha(args.reference_bundle)
                or payload.get('fixed_scalar_metric',{}).get('identity_sha256') != q.context.scalar_identity):
            raise ValueError('Use the complete actual same-reference/carrier/chart/free-variable predecessor')
        terminal = _terminal(payload)
        _input_identity(payload,args,q)
        model_binding = _compatible_models(payload['representation'],q.model,pins,frozen_point_relation=frozen_relation)
        actual = payload.get('material_envelope')
        memory.validate_report_metadata(actual,model_identity=payload['model_identity_sha256'],
            carrier_sha256=current_carrier_sha)
        _policy_inclusion(actual.get('definition'),expected_policy)
        inbound=_complete_input_reports(payload,current_carrier_sha256=current_carrier_sha)
        for item in inbound:
            if item['kind']=='complete_preparation' and item['payload'].get('reference_definition')!=preparation['reference_definition']:
                raise ValueError('Every complete inherited preparation must retain the same actual frozen target')
        parents.append(dict(record=record,payload=payload,terminal=terminal,
            model_binding=model_binding,family=family,inbound=inbound,
            original_complete_reader_sha256=family['reader_sha256']))
    restart_record = None
    prior_transfer = None
    if restart is not None:
        if source_report_path is None:
            raise ValueError('The complete actual same-source restart report path is required')
        restart_record,restart_raw = _record_bytes(source_report_path)
        if json.loads(restart_raw) != restart:
            raise ValueError('Keep the already source-validated restart snapshot')
        if (restart.get('schema') != caller['SCHEMA']
                or restart.get('source_sha256') != caller_record['sha256']
                or restart.get('complete') is not True
                or restart.get('model_identity_sha256') != q.identity
                or restart.get('representation') != q.model
                or restart.get('observation_carrier_sha256') != current_carrier_sha):
            raise ValueError('Only the actual complete same-source/model restart is restored directly')
        prior_transfer = restart.get('material_envelope_transfer')
        validate_metadata(prior_transfer,model=q.model,envelope=restart['material_envelope'],
            caller_source_sha256=caller_record['sha256'],carrier_sha256=current_carrier_sha)
    manifest = [Path(path).resolve() for path in args.manifest]
    for parent in parents:
        for item in parent['inbound']:
            path=Path(item['record']['path']).resolve()
            if item['kind']!='complete_preparation' and path not in manifest:manifest.append(path)
    for path in paths:
        if path not in manifest:
            manifest.append(path)
    original_args = SimpleNamespace(**vars(args))
    original_args.manifest = manifest
    witnesses,radii,history_record,envelope = memory.load_memory(original_args,preparation,q,history,
        restart=restart,source_report_path=source_report_path)
    if envelope.definition != expected_policy:
        raise ValueError('The actually constructed complete envelope uses a different working policy')
    if restart is not None:
        _restore_annotations(envelope,restart['material_envelope']['actual_separation_memory']['rows'])
    arrays = _from_witnesses(witnesses,radii)
    current_sets = {role:{_point(row) for row in arrays[role]} for role in ADDRESS_ROLES}
    parent_records = [] if prior_transfer is None else copy.deepcopy(prior_transfer['actual_parent_reports'])
    imported = []
    for parent in parents:
        payload,record = parent['payload'],parent['record']
        old = payload['material_envelope']
        inclusion=_grid_inclusion(old,envelope.metadata())
        locations = history.Locations(q.J,q.P,q.full_N)
        for item in parent['inbound']:
            if item['kind']!='complete_preparation':
                locations.walk(item['payload'],path=('complete_original_input_history',item['record']['sha256']))
        locations.walk(payload,path=('complete_source_bound_envelope_parent',))
        locations.resolve_grid(args.carrier)
        old_arrays = locations.arrays()
        fingerprints = _address_fingerprints(old_arrays)
        for role in ADDRESS_ROLES:
            if not {_point(row) for row in old_arrays[role]} <= current_sets[role]:
                raise ValueError('The original complete walker lost a prior explicit role/protection address')
        rows = old['actual_separation_memory']['rows']
        source_record = dict(report=copy.deepcopy(record),
            actual_driver_sha256=payload['source_sha256'],
            actual_model_identity_sha256=payload['model_identity_sha256'],
            original_complete_reader_sha256=parent['family']['reader_sha256'],
            inherited_prior_independent_branch_origin=copy.deepcopy(
                payload.get('material_envelope_transfer',{}).get('independent_branch_origin')),
            actual_terminal_report_kind=parent['terminal'],
            model_binding=parent['model_binding'],
            actual_complete_walker_role_fingerprints=fingerprints,
            complete_original_role_arrays=copy.deepcopy(old_arrays),
            complete_original_typed_rows=copy.deepcopy(rows),
            complete_grid_inclusion=inclusion,
            complete_inbound_history_records=[dict(record=v['record'],kind=v['kind']) for v in parent['inbound']],
            inherited_prior_transfer_metadata=copy.deepcopy(payload.get('material_envelope_transfer')),
            actual_typed_memory_count=len(rows),actual_typed_memory_sha256=canonical(rows),
            actual_typed_core_order_sha256=canonical([_type(row) for row in rows]),
            all_typed_rows_transferred_without_eviction_or_count_cap=True,
            previous_numeric_values_or_certificates_inherited=False)
        parent_records.append(source_record)
        for ordinal,row in enumerate(rows):
            typed = _type(row)
            key = canonical(typed)
            origin = dict(source_report_sha256=record['sha256'],source_row_ordinal=ordinal,
                source_model_identity_sha256=payload['model_identity_sha256'],
                source_driver_sha256=payload['source_sha256'],
                first_discovered_source_full_point_sha256=row['first_discovered_current_full_point_sha256'],
                typed_core_sha256=key,actual_new_field_value_inherited=False,
                complete_original_typed_row=copy.deepcopy(row))
            was_new = key not in envelope._separation
            envelope._separate(row['family'],row['location'],partner=row['partner'],
                branch=row['branch'],sign=row['sign'],token=row['first_discovered_current_full_point_sha256'])
            current = envelope._separation[key]
            origins = current.setdefault('source_bound_address_transfer_origins',[])
            if origin not in origins:
                origins.append(origin)
            if was_new:
                current['origin'] = 'source-bound prior typed address transfer; no current field value inherited'
            imported.append(dict(parent_report_sha256=record['sha256'],source_row_ordinal=ordinal,
                typed_core_sha256=key,retained_initial_ordinal=list(envelope._separation).index(key)))
        _same_bytes(record)
    branch_origin=(None if prior_transfer is None else copy.deepcopy(prior_transfer.get('independent_branch_origin')))
    if independent:
        target=envelope.metadata()['historical_address_binding']['actual_path_binding']['fixed_target_definition']
        reference=q.base.model['complete_axisymmetric_reference_model']
        if (target['complete_current_reference_model']!=reference
                or target['complete_current_reference_bundle_sha256']!=sha(args.reference_bundle)
                or target['fixed_chart_core_array_record']['sha256']!=reference['fixed_chart_core_sha256']):
            raise ValueError('Bind this actual new fixed target before creating its independent origin')
        branch_origin=dict(schema='explicit-fixed-fejer-frequency-inclusion-origin-v1',
            independent_fixed_target_definition_identity_sha256=canonical(target),
            actual_origin_reference_model_identity_sha256=canonical(reference),
            actual_origin_reference_bundle_sha256=target['complete_current_reference_bundle_sha256'],
            actual_origin_fixed_chart_core_sha256=reference['fixed_chart_core_sha256'],
            mathematical_target_identity_sha256=target['mathematical_target_identity_sha256'],
            same_declared_fejer_mathematical_target=True,
            current_frequency_refinement_changes_fixed_target=False,
            historical_sameg_false_flags_refer_to_pre_fejer_targets=True,
            old_physical_s_or_field_point_equality_claimed=False,
            literal_history_interpretation='full original cell/u/phi requests on the new target and deterministic mesh',
            same_original_fixed_chart=False,same_original_g_claimed=False,
            same_mathematical_g_claimed=False,old_values_or_certificates_inherited=False,
            actual_origin_model_identity_sha256=q.identity,
            actual_origin_driver_sha256=caller_record['sha256'],
            actual_origin_carrier_sha256=current_carrier_sha,
            frozen_original_reference_point_sha256=q.reference_point_sha256,
            original_complete_memory_source_sha256=actual_memory_sha,
            complete_reinterpreted_P0_and_initial_current_grid_responsibility=True,
            independent_initial_point_is_original_reference=True,
            pending_parallel_runs=pending,pending_parallel_driver_sources=pending_sources,
            pending_parallel_driver_sha256=(next(iter(set(pending_sources.values())))
                if len(set(pending_sources.values()))==1 else None),
            pending_parallel_terminal_reports_read=False,
            pending_parallel_final_or_typed_discovery_words_inherited=False,
            later_actual_addresses_and_typed_memory_require_bound_merge=True,
            unknown_typed_priority_equivalence_claimed=False)
    initial_rows = envelope.separation_rows()
    record = dict(schema=SCHEMA,source_sha256=sha(__file__),definition=definition(),
        actual_current_driver_sha256=caller_record['sha256'],
        actual_current_driver_source=copy.deepcopy(caller_record),
        frozen_original_point_relation=copy.deepcopy(frozen_relation),
        reference_M=160,current_M=320,
        actual_current_model_identity_sha256=q.identity,
        actual_current_base_model_identity_sha256=q.base.identity,
        actual_current_carrier_sha256=current_carrier_sha,
        actual_memory_source_sha256=actual_memory_sha,
        actual_current_fixed_scalar_identity_sha256=q.context.scalar_identity,
        envelope_policy_identity_sha256=canonical(envelope.definition),
        actual_parent_reports=parent_records,
        independent_branch_origin=branch_origin,
        current_invocation_memory_mode=('explicit-independent-branch' if independent else
            'same-source-restart' if restart is not None else
            'strict-current-target-terminal-transfer' if parent_memory==CURRENT_MEMORY_SOURCE_SHA256
            else 'strict-terminal-transfer'),
        current_invocation_parent_report_count=len(parents),
        actual_same_source_restart_report=restart_record,
        prior_transfer_identity_sha256=None if prior_transfer is None else canonical(prior_transfer),
        complete_initial_explicit_address_union=arrays,
        complete_initial_explicit_role_fingerprints=_address_fingerprints(arrays),
        initial_imported_typed_rows=initial_rows,
        initial_imported_typed_count=len(initial_rows),initial_imported_typed_sha256=canonical(initial_rows),
        current_invocation_typed_source_order_mapping=imported,
        all_original_report_addresses_consumed_by_original_walker=True,
        all_transferred_known_protection_retained=True,
        all_transferred_types_require_actual_new_field_read=True,
        previous_feasibility_or_function_values_inherited=False,
        actual_new_field_already_screened_by_transfer=False,
        original_same_model_restore_guard_changed=False,
        continuous_same_field_geometry_or_metric_certificate=False)
    for parent in parents:
        _same_bytes(parent['record'])
    if restart_record is not None:
        _same_bytes(restart_record)
    _same_bytes(caller_record)
    validated = validate_metadata(record,model=q.model,envelope=envelope.metadata(),
        caller_source_sha256=caller_record['sha256'],carrier_sha256=current_carrier_sha)
    history_record['source_bound_prior_envelope_transfer'] = dict(
        source_sha256=sha(__file__),definition_identity_sha256=canonical(definition()),
        actual_parent_report_records=[copy.deepcopy(parent['record']) for parent in parents],
        initial_imported_typed_count=validated['initial_imported_typed_count'],
        complete_initial_explicit_role_fingerprints=validated['complete_initial_explicit_role_fingerprints'],
        old_values_or_certificates_inherited=False)
    return witnesses,radii,history_record,envelope,record


def _digest(value):
    if (not isinstance(value,str) or len(value) != 64
            or any(character not in '0123456789abcdef' for character in value)):
        raise ValueError('Keep an actual complete source/model/point digest')
    return value


def seed_from_complete_prior_final(args,q,*,current_driver_source,transfer_record):
    """Read the actual complete coarse final and include EVERY free word."""
    require_actions()
    checkpoint=getattr(args,'material_envelope_seed_checkpoint',None)
    report_path=getattr(args,'material_envelope_seed_report',None)
    if checkpoint is None and report_path is None:return None,None
    if checkpoint is None or report_path is None or args.restart_checkpoint is not None:
        raise ValueError('A fine first point has one complete coarse report/checkpoint pair')
    caller_record,caller_bytes=_record_bytes(current_driver_source)
    pins=_literal_assignments(caller_bytes)['SOURCE_PINS']
    if (pins.get('envelope_transfer',(None,None))[1]!=sha(__file__)
            or transfer_record.get('actual_current_driver_sha256')!=caller_record['sha256']
            or transfer_record.get('actual_current_model_identity_sha256')!=q.identity
            or canonical(q.model)!=q.identity):
        raise ValueError('Keep the complete actual source, current model and historical transfer')
    source_record,raw=_record_bytes(report_path)
    parents=[item for item in transfer_record['actual_parent_reports'] if item['report']==source_record]
    if len(parents)!=1:
        raise ValueError('The complete coarse final must be the explicitly transferred actual predecessor')
    payload=json.loads(raw);family=_parent_family(payload.get('source_sha256'),payload)
    topic=Path(args.repo).resolve()/'topics/visible-flex-larger-amplitude'
    pure=_old_reader(topic,family).read_report(args.repo,report_path,verify_final_bundle=True)
    _same_bytes(source_record);_input_identity(payload,args,q)
    if (pure.get('report_sha256')!=source_record['sha256'] or payload.get('complete') is not True
            or payload.get('final_statistics') is None
            or payload.get('final_geometry',{}).get('complete') is not True):
        raise ValueError('Only a returned complete original field supplies free-variable words')
    model_binding=_compatible_models(payload['representation'],q.model,pins,
        frozen_point_relation=_frozen_initial_points(q,pins))
    if model_binding!=parents[0]['model_binding']:
        raise ValueError('The seed and history must be the same complete source-bound parent')
    bundle_record,bundle_bytes=_record_bytes(checkpoint)
    if (bundle_record['sha256']!=payload.get('final_bundle_sha256')
            or pure.get('actual_final_bundle_sha256')!=bundle_record['sha256']):
        raise ValueError('Read the exact actual complete reported coarse checkpoint bytes')
    import io
    import numpy as np
    module=_layout(q,pins)
    array_sha=q.base.__class__.__init__.__globals__['array_sha']
    before_model=canonical(q.model);frozen_initial=array_sha(q.base.initial())
    if frozen_initial!=q.reference_point_sha256:
        raise ValueError('The original complete reference remains frozen before any coarse final inclusion')
    names={'schema','omega_jets','core','Hcap','mesh','fixed_parent_core',
        'zero_closure_model_json','zero_closure_model_identity_sha256',
        'base_so3_model_identity_sha256','fixed_scalar_metric_identity_sha256',
        'endpoint_root_policy_json','working_integration_order','working_full_angles'}
    oldmodel=payload['representation']
    with np.load(io.BytesIO(bundle_bytes),allow_pickle=False) as saved:
        if set(saved.files)!=names or len(saved.files)!=len(names):
            raise ValueError('Read all thirteen original checkpoint members without hidden state or aliases')
        if (str(saved['schema'].item())!=family['operator_schema']
                or str(saved['zero_closure_model_identity_sha256'].item())!=payload['model_identity_sha256']
                or json.loads(str(saved['zero_closure_model_json'].item()))!=oldmodel
                or str(saved['base_so3_model_identity_sha256'].item())!=oldmodel['base_model_identity_sha256']
                or str(saved['fixed_scalar_metric_identity_sha256'].item())!=q.context.scalar_identity
                or json.loads(str(saved['endpoint_root_policy_json'].item()))!=q.policy.metadata()
                or saved['working_integration_order'].shape!=()
                or saved['working_full_angles'].shape!=()
                or int(saved['working_integration_order'].item())!=q.integration_order
                or int(saved['working_full_angles'].item())!=q.full_N):
            raise ValueError('Keep the actual old complete model, exact target and unchanged complete working quadrature')
        arrays={name:np.array(saved[name],copy=True) for name in
            ('omega_jets','core','Hcap','mesh','fixed_parent_core')}
    expected_shapes=dict(omega_jets=(923,3,482),core=(160,),Hcap=(),mesh=(923,),fixed_parent_core=(160,))
    for name,value in arrays.items():
        if value.dtype!=np.dtype(float) or value.shape!=expected_shapes[name] or not np.isfinite(value).all():
            raise ValueError('Every actual old saved array must be finite binary64 with its ORIGINAL complete layout: '+name)
    same=lambda a,b:a.dtype==b.dtype and a.shape==b.shape and np.ascontiguousarray(a).tobytes()==np.ascontiguousarray(b).tobytes()
    if (not same(arrays['mesh'],q.mesh) or not same(arrays['fixed_parent_core'],q.parent_core)
            or not same(arrays['core'][:q.K],q.parent_core[:q.K])):
        raise ValueError('The actual complete fixed chart/core slots and radial mesh must agree')
    flat=arrays['omega_jets'].reshape(3*q.J,482)
    zero_slots=[0,3*(q.J-1),3*(q.J-1)+1]
    if np.any(flat[zero_slots]!=0):
        raise ValueError('The original complete checkpoint must retain all structural endpoint zeros')
    old=np.r_[arrays['core'][q.K:],flat[q.radial_free].ravel(),float(arrays['Hcap'])]
    if old.shape!=(q.base.frequency_layout_definition['original_free_size'],):
        raise ValueError('Reassemble every actual coarse free core, radial rotation and height word')
    point=array_sha(old)
    if (payload.get('latest_operator_metadata',{}).get('current_full_point_sha256')!=point
            or payload['final_geometry'].get('current_full_point_sha256')!=point):
        raise ValueError('The returned complete original variable words are not the actual final-read point')
    result,inclusion=module.embed_outer_words(old,q.base.frequency_layout_definition)
    core,omega,height=q.unpack(result)
    if (not same(core[:160],arrays['core']) or np.any(core[160:]!=0)
            or not same(omega[:,:,:161],arrays['omega_jets'][:,:,:161])
            or not same(omega[:,:,321:482],arrays['omega_jets'][:,:,161:322])
            or not same(omega[:,:,642:802],arrays['omega_jets'][:,:,322:482])
            or not same(np.array(height),arrays['Hcap'])):
        raise ValueError('Reconstruct all three correctly offset odd-sine/odd-cosine/even-sine blocks and the complete core/H')
    used=np.zeros(962,dtype=bool);used[:161]=True;used[321:482]=True;used[642:802]=True
    if np.any(omega[:,:,~used]!=0):
        raise ValueError('Every added rotation mode must be explicitly zero, never a copied old block alias')
    if (canonical(q.model)!=before_model or array_sha(q.base.initial())!=frozen_initial
            or q.reference_point_sha256!=frozen_initial):
        raise ValueError('Including an old final must not change the fixed reference, Q or exact model')
    for record in (source_record,bundle_record,caller_record):_same_bytes(record)
    record=dict(schema='actual-complete-M160-final-to-M320-zero-inclusion-v1',
        mode='actual-complete-parent-zero-inclusion',source_sha256=sha(__file__),
        actual_current_driver_sha256=caller_record['sha256'],
        actual_current_model_identity_sha256=q.identity,
        parent_report=source_record,parent_checkpoint=bundle_record,
        parent_driver_source_sha256=payload['source_sha256'],
        parent_model_identity_sha256=payload['model_identity_sha256'],
        parent_norm_identity_sha256=payload['coordinate_norm']['norm_identity_sha256'],
        original_complete_reader_sha256=family['reader_sha256'],
        complete_model_binding=model_binding,coordinate_inclusion=inclusion,
        current_full_point_sha256=array_sha(result),
        frozen_original_reference_point_sha256=frozen_initial,
        reference_M=160,current_M=320,
        complete_saved_array_sha256={name:array_sha(value) for name,value in arrays.items()},
        actual_current_free_layout=dict(J=q.J,n=q.n,K=q.K,core_size=q.core_size,
            rotation_size=q.rotation_size,free_size=q.free_size,radial_free_sha256=array_sha(q.radial_free)),
        source_complete_field_read=True,
        source_final_true_sampled_geometry_feasible=payload['final_true_sampled_geometry_feasible'],
        source_actual_accepted_direction_count=sum(int(item.get('accepted') is True)
            for item in payload.get('metric_directions',[])+payload.get('restoration_directions',[])),
        all_original_variable_words_retained_and_new_modes_zero=True,
        fixed_reference_seed_and_original_core_height_unchanged=True,
        old_norm_identity_damping_roots_physical_values_or_certificates_inherited=False,
        exact_selected_field_inclusion_requires_compatible_implicit_branch=True,
        new_initial_metric_geometry_roots_and_norm_must_be_read=True,
        current_field_already_read_by_variable_copy=False)
    return result,record


def validate_seed_metadata(value,*,report,model,transfer):
    """Pure complete inclusion evidence; this does not evaluate a new field."""
    requested=report.get('explicit_prior_final_variable_seed_requested')
    if type(requested) is not bool:
        raise ValueError('Declare whether a complete actual coarse final supplies the fine first point')
    _digest(report.get('initial_full_variable_point_sha256'))
    if value is None:
        if requested:
            raise ValueError('An explicitly requested prior final must retain its complete inclusion evidence')
        return None
    if (not requested or not isinstance(value,dict)
            or value.get('schema')!='actual-complete-M160-final-to-M320-zero-inclusion-v1'
            or value.get('mode')!='actual-complete-parent-zero-inclusion'
            or value.get('source_sha256')!=sha(__file__)
            or value.get('actual_current_driver_sha256')!=report['source_sha256']
            or value.get('actual_current_model_identity_sha256')!=canonical(model)
            or value.get('current_full_point_sha256')!=report['initial_full_variable_point_sha256']
            or value.get('frozen_original_reference_point_sha256')!=report['actual_reference_initial_full_point_sha256']
            or value.get('reference_M')!=160 or value.get('current_M')!=320
            or report.get('restart') is not None or report.get('direct_base_seed') is not None):
        raise ValueError('The actual coarse final inclusion must belong to this complete independently read M320 point')
    family=PARENT_FAMILIES.get(value.get('parent_driver_source_sha256'))
    if family is None or value.get('original_complete_reader_sha256')!=family['reader_sha256']:
        raise ValueError('Bind the exact original complete source/reader family')
    for key in ('source_complete_field_read','all_original_variable_words_retained_and_new_modes_zero',
            'fixed_reference_seed_and_original_core_height_unchanged',
            'exact_selected_field_inclusion_requires_compatible_implicit_branch',
            'new_initial_metric_geometry_roots_and_norm_must_be_read'):
        if value.get(key) is not True:raise ValueError('A complete inclusion responsibility is missing: '+key)
    for key in ('old_norm_identity_damping_roots_physical_values_or_certificates_inherited',
            'current_field_already_read_by_variable_copy'):
        if value.get(key) is not False:raise ValueError('Do not inherit an old field value or certificate: '+key)
    parents=[item for item in transfer['actual_parent_reports'] if item['report']==value.get('parent_report')]
    if (len(parents)!=1 or parents[0]['actual_terminal_report_kind']!='complete-original-budget-report'
            or parents[0]['actual_driver_sha256']!=value['parent_driver_source_sha256']
            or parents[0]['actual_model_identity_sha256']!=value.get('parent_model_identity_sha256')
            or parents[0]['model_binding']!=value.get('complete_model_binding')):
        raise ValueError('The complete free point and uncapped memory must have the same actual parent')
    _digest(value.get('parent_norm_identity_sha256'))
    checkpoint=value.get('parent_checkpoint',{})
    if not isinstance(checkpoint.get('path'),str) or type(checkpoint.get('bytes')) is not int or checkpoint['bytes']<1:
        raise ValueError('Keep the actual complete old checkpoint file record')
    _digest(checkpoint.get('sha256'))
    inclusion=value.get('coordinate_inclusion',{})
    if (inclusion.get('layout_source_sha256')!=LAYOUT_SOURCE_SHA256
            or inclusion.get('layout_identity_sha256')!=model['base_complete_model']['frequency_layout_identity_sha256']
            or inclusion.get('current_full_point_sha256')!=value['current_full_point_sha256']):
        raise ValueError('Bind the independent full zero-inclusion record to the current layout and first point')
    layout_module=_module(Path(__file__).with_name('fixed_fejer_frequency_layout.py'),LAYOUT_SOURCE_SHA256)
    layout_module.validate_inclusion(inclusion,model['base_complete_model']['frequency_layout_definition'])
    arrays=value.get('complete_saved_array_sha256')
    if not isinstance(arrays,dict) or set(arrays)!={'omega_jets','core','Hcap','mesh','fixed_parent_core'}:
        raise ValueError('Keep every actual complete old saved array identity')
    for digest in arrays.values():_digest(digest)
    layout=value.get('actual_current_free_layout',{})
    if (set(layout)!={'J','n','K','core_size','rotation_size','free_size','radial_free_sha256'}
            or layout['J']!=923 or layout['n']!=962 or layout['K']!=3 or layout['core_size']!=317
            or layout['free_size']!=report['original_variables']
            or layout['core_size']+layout['rotation_size']+1!=layout['free_size']):
        raise ValueError('Keep the complete current M320 layout without treating M160 as its size')
    _digest(layout['radial_free_sha256'])
    count=value.get('source_actual_accepted_direction_count')
    if type(count) is not int or count<0 or type(value.get('source_final_true_sampled_geometry_feasible')) is not bool:
        raise ValueError('A returned final and an accepted direction remain distinct actual facts')
    initial=report.get('initial')
    snapshot=initial.get('endpoint_roots') if isinstance(initial,dict) else report.get('initial_endpoint_roots')
    if isinstance(snapshot,dict) and snapshot.get('current_full_point_sha256') not in (None,value['current_full_point_sha256']):
        raise ValueError('The actual initial root record belongs to another full variable point')
    return copy.deepcopy(value)


def validate_metadata(value, *, model, envelope, caller_source_sha256, carrier_sha256):
    """Pure stdlib reader for complete imported addresses, types and provenance."""
    expected = definition()
    actual_memory_sha=value.get('actual_memory_source_sha256') if isinstance(value,dict) else None
    if (not isinstance(value,dict) or value.get('schema') != SCHEMA
            or value.get('source_sha256') != sha(__file__) or value.get('definition') != expected
            or value.get('actual_current_driver_sha256') != caller_source_sha256
            or value.get('actual_current_model_identity_sha256') != canonical(model)
            or value.get('actual_current_base_model_identity_sha256') != model['base_model_identity_sha256']
            or value.get('actual_current_fixed_scalar_identity_sha256') != model['fixed_scalar_metric_identity_sha256']
            or value.get('actual_current_carrier_sha256') != carrier_sha256
            or value.get('envelope_policy_identity_sha256') != envelope['definition_identity_sha256']
            or envelope.get('actual_model_identity_sha256') != canonical(model)
            or actual_memory_sha != CURRENT_MEMORY_SOURCE_SHA256
            or envelope.get('source_sha256') != actual_memory_sha):
        raise ValueError('Read the complete actual transfer from its own new model, source and policy')
    arrays = value.get('complete_initial_explicit_address_union')
    fingerprints = _address_fingerprints(arrays)
    if fingerprints != value.get('complete_initial_explicit_role_fingerprints'):
        raise ValueError('Keep the complete actual initial known-role/protection union')
    for key in ('all_original_report_addresses_consumed_by_original_walker',
            'all_transferred_known_protection_retained','all_transferred_types_require_actual_new_field_read'):
        if value.get(key) is not True:
            raise ValueError('A declared transferred responsibility was omitted: '+key)
    for key in ('previous_feasibility_or_function_values_inherited','actual_new_field_already_screened_by_transfer',
            'original_same_model_restore_guard_changed','continuous_same_field_geometry_or_metric_certificate'):
        if value.get(key) is not False:
            raise ValueError('An address transfer is not a physical value, root or certificate: '+key)
    parents = value.get('actual_parent_reports')
    if not isinstance(parents,list):
        raise ValueError('Preserve every actual predecessor evidence list')
    branch=value.get('independent_branch_origin')
    mode=value.get('current_invocation_memory_mode')
    if mode not in ('explicit-independent-branch','same-source-restart','strict-terminal-transfer',
            'strict-current-target-terminal-transfer'):
        raise ValueError('State the actual independent, restart or strict-terminal mode')
    if branch is not None:
        target=envelope['historical_address_binding']['actual_path_binding']['fixed_target_definition']
        reference=model['base_complete_model']['complete_axisymmetric_reference_model']
        if (target['complete_current_reference_model']!=reference
                or target['complete_current_reference_bundle_sha256']!=model['base_complete_model']['initial_reference_bundle_sha256']
                or target['fixed_chart_core_array_record']['sha256']!=reference['fixed_chart_core_sha256']):
            raise ValueError('The independent origin must retain the whole current reference and target')
        if (not isinstance(branch,dict)
                or branch.get('schema')!='explicit-fixed-fejer-frequency-inclusion-origin-v1'
                or branch.get('independent_fixed_target_definition_identity_sha256')!=canonical(target)
                or branch.get('actual_origin_reference_model_identity_sha256')!=canonical(reference)
                or branch.get('actual_origin_reference_bundle_sha256')!=target['complete_current_reference_bundle_sha256']
                or branch.get('actual_origin_fixed_chart_core_sha256')!=reference['fixed_chart_core_sha256']
                or branch.get('mathematical_target_identity_sha256')!=target['mathematical_target_identity_sha256']
                or branch.get('same_declared_fejer_mathematical_target') is not True
                or branch.get('current_frequency_refinement_changes_fixed_target') is not False
                or branch.get('historical_sameg_false_flags_refer_to_pre_fejer_targets') is not True
                or branch.get('old_physical_s_or_field_point_equality_claimed') is not False
                or branch.get('same_original_fixed_chart') is not False
                or branch.get('same_original_g_claimed') is not False
                or branch.get('same_mathematical_g_claimed') is not False
                or branch.get('old_values_or_certificates_inherited') is not False
                or branch.get('actual_origin_model_identity_sha256')!=canonical(model)
                or branch.get('actual_origin_driver_sha256')!=caller_source_sha256
                or branch.get('actual_origin_carrier_sha256')!=carrier_sha256
                or branch.get('frozen_original_reference_point_sha256')
                    !=model['reference_centering_definition']['original_reference_point_sha256']
                or branch.get('original_complete_memory_source_sha256')!=actual_memory_sha
                or actual_memory_sha!=CURRENT_MEMORY_SOURCE_SHA256):
            raise ValueError('Bind the complete actual independent branch and frozen original reference')
        for key in ('complete_reinterpreted_P0_and_initial_current_grid_responsibility',
                'independent_initial_point_is_original_reference','later_actual_addresses_and_typed_memory_require_bound_merge'):
            if branch.get(key) is not True:raise ValueError('Independent responsibility is incomplete: '+key)
        for key in ('pending_parallel_terminal_reports_read',
                'pending_parallel_final_or_typed_discovery_words_inherited','unknown_typed_priority_equivalence_claimed'):
            if branch.get(key) is not False:raise ValueError('Unknown parallel state was promoted: '+key)
        pending=branch.get('pending_parallel_runs')
        pending_sources=branch.get('pending_parallel_driver_sources')
        if (not isinstance(pending_sources,dict) or not isinstance(pending,list)
                or set(pending_sources)!=set(pending)
                or any(source not in PARENT_FAMILIES for source in pending_sources.values())
                or branch.get('pending_parallel_driver_sha256')!=(next(iter(set(pending_sources.values())))
                    if len(set(pending_sources.values()))==1 else None)):
            raise ValueError('The complete unknown-peer source map must retain every actual declared run')
        if (not isinstance(pending,list) or len(pending)!=len(set(pending))
                or any(not isinstance(v,str) or len(v.split('/'))!=2
                    or any(not w.isdigit() or int(w)<1 or str(int(w))!=w for w in v.split('/')) for v in pending)):
            raise ValueError('Keep canonical declared unread peer run identities, not fabricated reports')
    elif not parents or mode=='explicit-independent-branch':
        raise ValueError('A strict branch still needs complete actual terminal predecessor evidence')
    if branch is None and actual_memory_sha==CURRENT_MEMORY_SOURCE_SHA256:
        if not parents or any(_parent_family(p.get('actual_driver_sha256'))['memory_sha256']
                !=CURRENT_MEMORY_SOURCE_SHA256 for p in parents):
            raise ValueError('The current-target strict path requires its complete same-target parent lineage')
    _reread_transfer_parents(value,model,envelope,caller_source_sha256,carrier_sha256)
    known_reports = {}
    for parent in parents:
        report = parent.get('report',{})
        digest = _digest(report.get('sha256'))
        family=_parent_family(parent.get('actual_driver_sha256'))
        if (not isinstance(report.get('path'),str) or type(report.get('bytes')) is not int or report['bytes'] < 1
                or parent.get('original_complete_reader_sha256') != family['reader_sha256']
                or family['memory_sha256']!=actual_memory_sha
                or parent.get('actual_terminal_report_kind') not in (
                    'complete-original-budget-report','explicit-original-initial-field-failure-report')
                or parent.get('all_typed_rows_transferred_without_eviction_or_count_cap') is not True
                or parent.get('previous_numeric_values_or_certificates_inherited') is not False):
            raise ValueError('Keep each actual whole parent and its independently checked terminal scope')
        inherited=parent.get('inherited_prior_transfer_metadata')
        if not isinstance(inherited,dict):
            raise ValueError('Keep the complete prior lineage and all unresolved source-bound obligations')
        if parent.get('inherited_prior_independent_branch_origin')!=inherited.get('independent_branch_origin'):
            raise ValueError('Do not rewrite a prior independent origin for a larger current space')
        _digest(parent.get('actual_model_identity_sha256'))
        _digest(parent.get('actual_typed_memory_sha256'))
        _digest(parent.get('actual_typed_core_order_sha256'))
        binding = parent.get('model_binding',{})
        if (binding.get('exact_old_complete_model_identity_sha256') != parent['actual_model_identity_sha256']
                or binding.get('exact_new_complete_model_identity_sha256') != canonical(model)
                or binding.get('full_fixed_reference_chart_profile_seed_mesh_Q_gamma_partition_and_observer_equal') is not True
                or binding.get('only_declared_current_frequency_layout_and_complete_source_policies_changed') is not True
                or binding.get('computed_float_field_equality_claimed') is not False):
            raise ValueError('Do not loosen the explicitly paid old/new complete-model relationship')
        _digest(binding.get('complete_unchanged_definition_sha256'))
        if type(parent.get('actual_typed_memory_count')) is not int or parent['actual_typed_memory_count'] < 0:
            raise ValueError('Keep actual nonnegative parent typed-memory counts')
        known_reports[digest] = parent
    count = value.get('current_invocation_parent_report_count')
    if type(count) is not int or not 0 <= count <= len(parents):
        raise ValueError('Keep actual current-parent and inherited-parent scopes distinct')
    restart = value.get('actual_same_source_restart_report')
    if restart is None:
        if value.get('prior_transfer_identity_sha256') is not None:
            raise ValueError('A fresh branch cannot invent a same-source restart')
        if mode=='explicit-independent-branch':
            if branch is None or count!=0 or parents:
                raise ValueError('An explicit fresh branch does not pretend to have terminal predecessors')
        elif (mode!=('strict-current-target-terminal-transfer' if actual_memory_sha==CURRENT_MEMORY_SOURCE_SHA256
                else 'strict-terminal-transfer') or count==0 or branch is not None):
            raise ValueError('Each strict fresh branch retains its nonempty complete terminal-input requirement')
    else:
        if mode!='same-source-restart':
            raise ValueError('An actual same-source restore must retain its declared mode')
        _digest(restart.get('sha256'))
        _digest(value.get('prior_transfer_identity_sha256'))
        if not isinstance(restart.get('path'),str) or type(restart.get('bytes')) is not int or restart['bytes'] < 1:
            raise ValueError('Keep the complete actual same-source restart file record')
    rows = value.get('initial_imported_typed_rows')
    final_rows = envelope['actual_separation_memory']['rows']
    if (not isinstance(rows,list) or value.get('initial_imported_typed_count') != len(rows)
            or value.get('initial_imported_typed_sha256') != canonical(rows)
            or final_rows[:len(rows)] != rows or len(final_rows) < len(rows)):
        raise ValueError('The entire initial typed memory must remain an unchanged uncapped prefix')
    if mode=='explicit-independent-branch' and rows:
        raise ValueError('A fresh independent origin cannot prefill unknown actual typed discoveries')
    core_keys = [_typed_key(row) for row in rows]
    if len(core_keys) != len(set(core_keys)):
        raise ValueError('The complete typed union must retain one append-only entry per actual typed constraint')
    for row in rows:
        _digest(row.get('first_discovered_current_full_point_sha256'))
        for origin in row.get('source_bound_address_transfer_origins',[]):
            source = known_reports.get(origin.get('source_report_sha256'))
            if (source is None or origin.get('source_driver_sha256') != source['actual_driver_sha256']
                    or origin.get('source_model_identity_sha256') != source['actual_model_identity_sha256']
                    or type(origin.get('source_row_ordinal')) is not int
                    or not 0 <= origin['source_row_ordinal'] < source['actual_typed_memory_count']
                    or origin.get('typed_core_sha256') != _typed_key(row)
                    or origin.get('actual_new_field_value_inherited') is not False):
                raise ValueError('Keep the old discovery provenance distinct from an actual new-model scan')
            old_row=source['complete_original_typed_rows'][origin['source_row_ordinal']]
            if origin.get('complete_original_typed_row')!=old_row or _typed_key(old_row)!=_typed_key(row):
                raise ValueError('Retain the entire original typed row and its complete discovery lineage')
            _digest(origin.get('first_discovered_source_full_point_sha256'))
    mapping = value.get('current_invocation_typed_source_order_mapping')
    if not isinstance(mapping,list):
        raise ValueError('Keep every actual imported source-row ordinal and its retained union position')
    for item in mapping:
        source = known_reports.get(item.get('parent_report_sha256'))
        ordinal = item.get('source_row_ordinal')
        target = item.get('retained_initial_ordinal')
        if (source is None or type(ordinal) is not int or not 0 <= ordinal < source['actual_typed_memory_count']
                or type(target) is not int or not 0 <= target < len(rows)
                or item.get('typed_core_sha256') != core_keys[target]):
            raise ValueError('An imported typed row was lost, reordered or given a false target address')
    if count:
        current_parents = parents[-count:]
        expected_pairs = [(item['report']['sha256'],i) for item in current_parents
            for i in range(item['actual_typed_memory_count'])]
        if [(item['parent_report_sha256'],item['source_row_ordinal']) for item in mapping] != expected_pairs:
            raise ValueError('Transfer every source typed row in its complete actual order')
    elif mapping:
        raise ValueError('A restore-only call cannot invent newly imported parent rows')
    return dict(schema=SCHEMA,source_sha256=sha(__file__),definition=expected,
        actual_current_model_identity_sha256=canonical(model),
        actual_memory_source_sha256=actual_memory_sha,
        actual_parent_report_count=len(parents),current_invocation_parent_report_count=count,
        same_source_restart_used=restart is not None,
        current_invocation_memory_mode=mode,independent_branch_origin=copy.deepcopy(branch),
        pending_parallel_report_values_or_priority_inherited=False,
        complete_initial_explicit_role_fingerprints=fingerprints,
        initial_imported_typed_count=len(rows),initial_imported_typed_sha256=canonical(rows),
        current_envelope_typed_count=len(final_rows),all_imported_types_retained_as_prefix=True,
        original_full_walker_and_same_model_restore_unchanged=True,
        old_values_or_feasibility_inherited=False,new_field_already_screened=False,
        reference_M=160,current_M=320,full_N=2048,J=923,
        fixed_target_observer_and_original_free_variables_retained=True,continuous_certificate=False)


def _policy_inclusion(old,new):
    source=_original_memory()
    cap=new.get('additional_current_near_active_rows')
    if old!=new or new!=source.definition(cap):
        raise ValueError('M-only inclusion preserves the entire actual envelope policy and near-active cap')

def _grid_inclusion(old,new):
    source=_original_memory()
    source._validate_grid(old['implicit_grid']);source._validate_grid(new['implicit_grid'])
    if old['implicit_grid']!=new['implicit_grid']:
        raise ValueError('M-only inclusion must retain every original/current radial and literal angular address')
    for key in ('origin_carrier','current_carrier'):
        before,after=copy.deepcopy(old['historical_address_binding'][key]),copy.deepcopy(new['historical_address_binding'][key])
        before['record'].pop('path');after['record'].pop('path')
        if before!=after:raise ValueError('Retain the complete identical radial carriers')
    old_target=old['historical_address_binding']['actual_path_binding']['fixed_target_definition']
    new_target=new['historical_address_binding']['actual_path_binding']['fixed_target_definition']
    if old_target!=new_target:
        raise ValueError('A frequency inclusion cannot relabel another exact target')
    return dict(full_N=2048,quarter_angles=513,J=923,
        complete_old_current_grid_equal=True,
        complete_independent_target_identity_sha256=canonical(old_target),
        complete_old_grid_identity_sha256=canonical(old['implicit_grid']),
        complete_new_grid_identity_sha256=canonical(new['implicit_grid']))

def frequency_initial_record(args,q,x,*,transfer_record,seed_record):
    require_actions()
    array_sha=q.base.__class__.__init__.__globals__['array_sha']
    current=array_sha(x)
    relation=transfer_record['frozen_original_point_relation']
    if (array_sha(q.base.initial())!=relation['current_full_point_sha256']
            or q.reference_point_sha256!=relation['current_full_point_sha256']):
        raise ValueError('The reference seed cannot move when choosing the current M320 input point')
    mode=transfer_record['current_invocation_memory_mode']
    extra={}
    if seed_record is not None:
        if current!=seed_record['current_full_point_sha256']:
            raise ValueError('The complete included old final is not the actual first fine point')
        selected='actual-complete-parent-zero-inclusion'
        extra=dict(coordinate_inclusion=copy.deepcopy(seed_record['coordinate_inclusion']),
            parent_report=copy.deepcopy(seed_record['parent_report']))
    elif args.restart_checkpoint is not None:
        if mode!='same-source-restart':raise ValueError('Restart input and restored memory must be identical')
        selected='same-source-complete-restart'
        extra=dict(restart_report=copy.deepcopy(transfer_record['actual_same_source_restart_report']))
    else:
        if current!=relation['current_full_point_sha256']:
            raise ValueError('Without a complete final or restart, use the full zero-included original reference point')
        if mode=='explicit-independent-branch':selected='fresh-original-reference-zero-inclusion'
        elif mode=='strict-current-target-terminal-transfer':selected='terminal-history-original-reference-zero-inclusion'
        else:raise ValueError('Declare the actual fresh or terminal-history input mode')
    return dict(schema='actual-fixed-fejer-M320-input-point-and-fixed-reference-v1',
        source_sha256=sha(__file__),mode=selected,current_full_point_sha256=current,
        frequency_layout_identity_sha256=q.base.model['frequency_layout_identity_sha256'],
        frozen_original_point_relation=copy.deepcopy(relation),
        all_original_free_variables_retained=True,all_new_mode_initialization_explicit=True,
        fixed_reference_seed_unchanged=True,
        new_initial_field_roots_geometry_and_norm_require_read=True,
        old_values_roots_norm_or_certificates_inherited=False,**extra)

def _module(path,digest):
    path=Path(path).resolve()
    if sha(path)!=digest:
        raise ValueError('Keep the entire bound source '+path.name)
    name='_complete_M320_transfer_'+digest
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    if sha(path)!=digest:
        raise ValueError('A complete source changed during loading')
    return module

def _original_memory():
    return _module(Path(__file__).with_name('complete_fixed_fejer_material_envelope_memory.py'),
        CURRENT_MEMORY_SOURCE_SHA256)

def _complete_input_reports(payload,*,current_carrier_sha256):
    """Read every actual original inbound history; do not truncate an ancestry."""
    pending=list(payload.get('history',{}).get('sources',[]))
    seen=set();result=[]
    while pending:
        recorded=pending.pop(0)
        if not isinstance(recorded,dict) or set(recorded)!=set(('path','sha256','bytes')):
            raise ValueError('Keep every complete actual inbound history file record')
        key=(recorded['path'],recorded['sha256'])
        if key in seen:continue
        actual,raw=_record_bytes(recorded['path'])
        if actual!=recorded:
            raise ValueError('An original complete inbound history changed')
        value=json.loads(raw);seen.add(key)
        if value.get('schema')=='R690-fixed-fejer-axisymmetric-SO3-preparation-v1':
            result.append(dict(record=actual,kind='complete_preparation',payload=value))
            continue
        if value.get('carrier_sha256',value.get('observation_carrier_sha256'))!=current_carrier_sha256:
            raise ValueError('All original inbound histories retain the actual unchanged radial carrier')
        declared=value.get('N',value.get('full_angles',value.get('full_N')))
        if declared is not None and declared!=2048:
            raise ValueError('Each supported original parent has its own N2048 indexed history')
        result.append(dict(record=actual,kind='complete_original_N_history',payload=value))
        previous=value.get('history',{})
        if isinstance(previous,dict):pending.extend(previous.get('sources',[]))
    return result

def _reread_transfer_parents(value,model,envelope,caller_source_sha256,carrier_sha256):
    """Pure complete-source/file validation of every actual migrated lineage."""
    source=value.get('actual_current_driver_source',{})
    _same_bytes(source)
    if source.get('sha256')!=caller_source_sha256:
        raise ValueError('Bind the actual caller source path before pure cross-M validation')
    source_path=Path(source['path']).resolve()
    topic=source_path.parents[2]
    pins=_literal_assignments(source_path.read_bytes())['SOURCE_PINS']
    if (pins.get('envelope_transfer',(None,None))[1]!=sha(__file__)
            or pins.get('independent_envelope_memory',(None,None))[1]!=CURRENT_MEMORY_SOURCE_SHA256):
        raise ValueError('The complete caller role table does not bind this actual M history bridge')
    binding=_module(Path(__file__).with_name('fixed_fejer_frequency_source_binding.py'),ANALYTIC_BINDING_SOURCE_SHA256)
    binding.validate_frozen_point_relation(value.get('frozen_original_point_relation'),model,source_directory=source_path.parent)
    if value.get('reference_M')!=160 or value.get('current_M')!=320:
        raise ValueError('Retain the explicitly separate frozen and current frequency dimensions')
    arrays=value['complete_initial_explicit_address_union']
    current_sets={role:{_point(row) for row in arrays[role]} for role in ADDRESS_ROLES}
    for item in value['actual_parent_reports']:
        record=item['report'];_same_bytes(record)
        payload=json.loads(Path(record['path']).read_bytes())
        family=_parent_family(payload.get('source_sha256'),payload)
        if family['memory_sha256']!=CURRENT_MEMORY_SOURCE_SHA256:
            raise ValueError('An actual M-parent must belong to the same complete independent fixed target family')
        pure=_old_reader(topic,family).read_report(topic.parent.parent,Path(record['path']),verify_final_bundle=False)
        if (pure.get('report_sha256')!=record['sha256'] or _terminal(payload)!=item['actual_terminal_report_kind']
                or payload.get('N')!=2048 or payload.get('observation_carrier_sha256')!=carrier_sha256
                or canonical(payload['representation'])!=item['actual_model_identity_sha256']
                or _compatible_models(payload['representation'],model,pins,frozen_point_relation=value['frozen_original_point_relation'])!=item['model_binding']
                or payload.get('material_envelope_transfer')!=item.get('inherited_prior_transfer_metadata')
                or payload['material_envelope']['actual_separation_memory']['rows']!=item.get('complete_original_typed_rows')):
            raise ValueError('The complete original report, target, typed rows or unresolved ancestor obligations changed')
        inbound=_complete_input_reports(payload,current_carrier_sha256=carrier_sha256)
        expected=[dict(record=v['record'],kind=v['kind']) for v in inbound]
        if expected!=item.get('complete_inbound_history_records'):
            raise ValueError('Keep the entire actual original input-history closure')
        old_arrays=item.get('complete_original_role_arrays')
        if _address_fingerprints(old_arrays)!=item.get('actual_complete_walker_role_fingerprints'):
            raise ValueError('Keep every complete known original role and protected-address set')
        for role in ADDRESS_ROLES:
            if not {_point(v) for v in old_arrays[role]}<=current_sets[role]:
                raise ValueError('The full old explicit/protected history is not contained in the current initial memory')
        _policy_inclusion(payload['material_envelope']['definition'],envelope['definition'])
        if _grid_inclusion(payload['material_envelope'],envelope)!=item.get('complete_grid_inclusion'):
            raise ValueError('The entire complete unchanged observation identity changed')
        _same_bytes(record)
    _same_bytes(source)

def _layout(q,pins):
    module=getattr(q.base,'frequency_layout_module',None)
    if module is None:
        # The current base stores the source-bound module in its constructor globals.
        path=Path(q.base.__class__.__init__.__code__.co_filename).parent/'fixed_fejer_frequency_layout.py'
        if sha(path)!=LAYOUT_SOURCE_SHA256:
            raise ValueError('Bind the complete independent frequency-layout module')
        name='_actual_frequency_layout_'+LAYOUT_SOURCE_SHA256
        spec=importlib.util.spec_from_file_location(name,path)
        module=importlib.util.module_from_spec(spec);sys.modules[name]=module;spec.loader.exec_module(module)
    for function in (module.definition,module.validate_base_model,module.embed_outer_words,module.validate_inclusion):
        if sha(function.__code__.co_filename)!=LAYOUT_SOURCE_SHA256:
            raise ValueError('Keep each complete current layout and byte inclusion body')
    if pins.get('frequency_layout',(None,None))[1]!=LAYOUT_SOURCE_SHA256:
        raise ValueError('The actual full caller must pin the independent layout source')
    module.validate_base_model(q.base.model,expected_base_source_sha256=pins['meridian'][1])
    return module

def _frozen_initial_points(q,pins):
    import numpy as np
    module=_layout(q,pins)
    array_sha=q.base.__class__.__init__.__globals__['array_sha']
    if sha(array_sha.__code__.co_filename)!=pins['meridian'][1]:
        raise ValueError('Bind the current complete point identity source')
    old=np.r_[q.parent_core[q.K:],np.zeros(len(q.radial_free)*482),float.fromhex(q.parent_jet.model['initial_height_hex'])]
    current=q.base.initial()
    included,record=module.embed_outer_words(old,q.base.frequency_layout_definition)
    if (included.dtype!=current.dtype or included.shape!=current.shape
            or included.tobytes()!=current.tobytes()
            or array_sha(current)!=q.reference_point_sha256):
        raise ValueError('The new frozen reference point must be the exact zero inclusion of the old core/H/zero-omega point')
    return dict(original_full_point_sha256=array_sha(old),
        current_full_point_sha256=array_sha(current),coordinate_inclusion=record)

def _input_identity(payload,args,q):
    records=dict(bundle_sha256=args.reference_bundle,observation_carrier_sha256=args.carrier,
        exact_tail_node_report_sha256=args.node_report,exact_tail_scalar_input_sha256=args.scalar_input)
    if any(payload.get(key)!=sha(path) for key,path in records.items()):
        raise ValueError('The original reference, carrier, symbolic nodes and scalar input must be the same whole files')
    if payload.get('independent_preparation_report',{}).get('sha256')!=sha(args.preparation_report):
        raise ValueError('Keep the complete actual original preparation report')
    if (payload.get('N')!=q.full_N or payload.get('J')!=q.J
            or payload.get('fixed_scalar_metric',{}).get('identity_sha256')!=q.context.scalar_identity
            or float(payload.get('material_envelope_active_band',math.nan)).hex()!=float(args.active_band).hex()
            or payload.get('radial_weights',{}).get('legacy_fraction')!=args.legacy_fraction
            or any(payload.get('spectral_parameters',{}).get(key)!=value for key,value in
                dict(p=args.spectral_p,epsilon=args.spectral_epsilon,scale=args.spectral_scale).items())
            or float(payload.get('numerical_reach_safety_factor',math.nan)).hex()!=float(args.reach_safety_factor).hex()):
        raise ValueError('Keep the same full observation measure, spectral loss and strict geometric safety policy')
    budgets=payload.get('amplitude_design_constraints',{}).get('budgets',{})
    for key,wanted in dict(marked_diameter_budget=args.marked_diameter_budget,
            witness_lower_budget=args.witness_lower_budget,height_floor=args.amplitude_height_floor,
            cap_radius=float(q.R)).items():
        if budgets.get(key)!=wanted:
            raise ValueError('Retain the same complete physical amplitude budget: '+key)
    geometric=payload.get('final_geometry')
    if isinstance(geometric,dict) and geometric.get('source_binding',{}).get('reach_ratio')!=args.reach_ratio:
        raise ValueError('Retain the same actual reach ratio')
    norm=payload.get('coordinate_norm',{})
    if (norm.get('norm_kind')!=args.norm_kind or norm.get('radial_length')!=args.radial_norm_length
            or norm.get('angular_transition')!=args.angular_transition
            or canonical({key:value for key,value in norm.items() if key!='norm_identity_sha256'})
            !=norm.get('norm_identity_sha256')):
        raise ValueError('Bind the actual full previous norm, without inheriting it as the new norm')
    return {key:sha(path) for key,path in records.items()}
