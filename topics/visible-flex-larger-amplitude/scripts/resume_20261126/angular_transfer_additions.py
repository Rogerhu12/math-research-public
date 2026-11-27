"""Source sections used by the complete N-only transfer deriver. No science here."""


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
