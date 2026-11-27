"""Complete additional source for the independent-chart N-only history bridge."""

def _module(path,digest):
    path=Path(path).resolve()
    if sha(path)!=digest:
        raise ValueError('Keep the entire bound source '+path.name)
    name='_complete_N4096_transfer_'+digest
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    if sha(path)!=digest:
        raise ValueError('A complete source changed during loading')
    return module


def _original_memory():
    return _module(Path(__file__).with_name('complete_material_envelope_memory_independent_chart.py'),
        ORIGINAL_CURRENT_MEMORY_SOURCE_SHA256)


def _observer():
    return _module(Path(__file__).with_name('angular_observation_refinement.py'),
        '8506eb861bb8650ddfd0c5db5c268e8bb0a71b38e48ebb551767b45d2d339ab3')


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
        if value.get('schema')=='R690-independent-axisymmetric-SO3-preparation-v1':
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


def _policy_inclusion(old,new):
    source=_original_memory()
    cap=new.get('additional_current_near_active_rows')
    if old!=source.definition(cap):
        raise ValueError('Preserve the full original policy and its actual near-active cap')
    if (new.get('reference_full_N')!=2048 or new.get('current_full_N')!=4096
            or new.get('original_tagged_angles_resolved_before_union') is not True
            or new.get('complete_original_grid_is_even_subset_of_new_grid') is not True
            or new.get('discovered_typed_separation_rows_have_no_eviction_or_count_cap') is not True
            or new.get('finite_angular_objective_changed') is not True):
        raise ValueError('Only the declared complete N observation policy may replace the original policy')


def _grid_inclusion(old,new):
    source=_original_memory()
    old_grid=source._validate_grid(old['implicit_grid'])
    # _validate_grid validates in place and may return None; use the actual
    # object after that complete source-bound validation.
    old_grid=old['implicit_grid']
    new_grid=new['implicit_grid']
    observation=_observer().validate_carrier(new_grid.get('angular_observation'))
    radial=('current_radial_entry_count','current_unique_radial_count','origin_unique_radial_count',
        'extra_historical_radial_count','union_unique_radial_count','union_radial_words_sha256',
        'extra_radial_words_sha256')
    if (any(old_grid.get(key)!=new_grid.get(key) for key in radial)
            or old_grid.get('angular_count')!=513 or old_grid.get('full_angular_count')!=2048
            or new_grid.get('angular_count')!=1025 or new_grid.get('full_angular_count')!=4096
            or old_grid.get('actual_phi_sha256')!=observation['reference_phi_sha256']
            or new_grid.get('actual_phi_sha256')!=observation['current_phi_sha256']
            or old_grid.get('unique_implicit_material_locations')!=old_grid['union_unique_radial_count']*513
            or new_grid.get('unique_implicit_material_locations')!=new_grid['union_unique_radial_count']*1025):
        raise ValueError('Preserve the entire old radial grid times every literal old/even angle')
    old_binding=old['historical_address_binding']
    new_binding=new['historical_address_binding']
    for key in ('origin_carrier','current_carrier'):
        before,after=copy.deepcopy(old_binding[key]),copy.deepcopy(new_binding[key])
        before['record'].pop('path');after['record'].pop('path')
        if before!=after:
            raise ValueError('Keep every complete radial carrier member and full-byte identity')
    old_target=old_binding['actual_path_binding']['fixed_target_definition']
    new_target=new_binding['actual_path_binding']['fixed_target_definition']
    if old_target!=new_target or canonical(old_target)!=new_binding['actual_path_binding']['fixed_target_definition_identity_sha256']:
        raise ValueError('N refinement must retain the entire independent fixed target, not relabel another chart')
    return dict(reference_full_N=2048,current_full_N=4096,
        full_old_radial_union_unchanged=True,all_old_literal_angles_at_even_indices=True,
        complete_independent_target_identity_sha256=canonical(old_target),
        complete_old_grid_identity_sha256=canonical(old_grid),
        complete_new_grid_identity_sha256=canonical(new_grid))


def _reread_transfer_parents(value,model,envelope,caller_source_sha256,carrier_sha256):
    """Pure complete-source/file validation of every actual migrated lineage."""
    source=value.get('actual_current_driver_source',{})
    _same_bytes(source)
    if source.get('sha256')!=caller_source_sha256:
        raise ValueError('Bind the actual caller source path before pure cross-N validation')
    source_path=Path(source['path']).resolve()
    topic=source_path.parents[2]
    pins=_literal_assignments(source_path.read_bytes())['SOURCE_PINS']
    if (pins.get('envelope_transfer',(None,None))[1]!=sha(__file__)
            or pins.get('independent_envelope_memory',(None,None))[1]!=CURRENT_MEMORY_SOURCE_SHA256):
        raise ValueError('The complete caller role table does not bind this actual N history bridge')
    arrays=value['complete_initial_explicit_address_union']
    current_sets={role:{_point(row) for row in arrays[role]} for role in ADDRESS_ROLES}
    for item in value['actual_parent_reports']:
        record=item['report'];_same_bytes(record)
        payload=json.loads(Path(record['path']).read_bytes())
        family=_parent_family(payload.get('source_sha256'),payload)
        if family['memory_sha256']!=ORIGINAL_CURRENT_MEMORY_SOURCE_SHA256:
            raise ValueError('An actual N-parent must belong to the same complete independent fixed target family')
        pure=_old_reader(topic,family).read_report(topic.parent.parent,Path(record['path']),verify_final_bundle=False)
        if (pure.get('report_sha256')!=record['sha256'] or _terminal(payload)!=item['actual_terminal_report_kind']
                or payload.get('N')!=2048 or payload.get('observation_carrier_sha256')!=carrier_sha256
                or canonical(payload['representation'])!=item['actual_model_identity_sha256']
                or _compatible_models(payload['representation'],model,pins)!=item['model_binding']
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
            raise ValueError('The entire actual old/even observation inclusion changed')
        _same_bytes(record)
    _same_bytes(source)
