"""Complete actual-public09 M160 to M320 source/model/report contracts."""

def _bound_module(path, expected):
    path=Path(path).resolve()
    if sha(path)!=expected:raise ValueError('Keep the entire bound source '+path.name)
    name='_public09_frequency_binding_'+expected
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module
    spec.loader.exec_module(module)
    if sha(path)!=expected:raise ValueError('The bound source changed during reading')
    return module


def _layout(source_directory):
    return _bound_module(Path(source_directory)/'so3_frequency_refinement_layout.py',
        'ce188ae4bdf1ccecfbf9549897284e8dc44f4722e04e974c7a0cd045c78a3a27')


def _validate_original_parent_model(old,directory):
    if (old.get('source_sha256')!='3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc'
            or old.get('schema')!='complete-R711-reference-centred-analytic-frame-and-J3-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1'):
        raise ValueError('Use the complete actual public09 M160 analytic-frame model')
    original=_bound_module(Path(directory)/'run09_public_reference_analytic_frame_binding.py',
        '15f6393acb1f069e3c5dee62708f9350b3e329b877b19fc8a69868365a45a592')
    roles={role:record[1] for role,record in original.SOURCE_BINDINGS.items()}
    original.validate_current_model(old,roles=roles,source_directory=directory)
    return tuple(original.POLICY_KEYS.values())


def validate_frozen_point_relation(value,model,*,source_directory):
    layout_module=_layout(source_directory)
    layout=layout_module.validate_base_model(model['base_complete_model'],
        expected_base_source_sha256=BASE_SOURCE_SHA256)
    if not isinstance(value,dict) or set(value)!={'original_full_point_sha256',
            'current_full_point_sha256','coordinate_inclusion'}:
        raise ValueError('Retain the actual full frozen-reference coordinate inclusion')
    included=layout_module.validate_inclusion(value['coordinate_inclusion'],layout)
    if (included['original_full_point_sha256']!=value['original_full_point_sha256']
            or included['current_full_point_sha256']!=value['current_full_point_sha256']
            or model['frozen_moment_Q_definition']['initial_full_point_sha256']!=value['current_full_point_sha256']
            or model['reference_centering_definition']['original_reference_point_sha256']!=value['current_full_point_sha256']):
        raise ValueError('The new Q and calibration must bind the actual included frozen point')
    return copy.deepcopy(value)


def compatible_legacy_model(old,new,current_pins,*,source_directory,frozen_point_relation):
    roles={role:value[1] for role,value in current_pins.items()}
    validate_current_model(new,roles=roles,source_directory=source_directory)
    old_policy_keys=_validate_original_parent_model(old,source_directory)
    relation=validate_frozen_point_relation(frozen_point_relation,new,source_directory=source_directory)
    oldpoint,newpoint=relation['original_full_point_sha256'],relation['current_full_point_sha256']
    before,after=copy.deepcopy(old),copy.deepcopy(new)
    oldbase,newbase=old['base_complete_model'],new['base_complete_model']
    normalized=copy.deepcopy(newbase)
    for key in ('reference_M','current_M','frequency_layout_definition',
            'frequency_layout_identity_sha256','frequency_layout_source_sha256',
            'all_original_outer_free_variables_retained_and_new_modes_added',
            'frozen_reference_layout_unchanged','current_norm_layout_changed'):
        normalized.pop(key)
    normalized.update(schema=oldbase['schema'],source_sha256=oldbase['source_sha256'],M=160,
        all_original_outer_free_variables_and_norm_layout_unchanged=True)
    if normalized!=oldbase:
        raise ValueError('Keep the entire fixed scalar/reference/chart/seed/radial mesh and physical working definition')
    oldq,newq=old['frozen_moment_Q_definition'],new['frozen_moment_Q_definition']
    if (oldq.get('schema')!='supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1'
            or newq.get('schema')!='frequency-refined-supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1'
            or oldq.get('initial_full_point_sha256')!=oldpoint
            or newq.get('initial_full_point_sha256')!=newpoint
            or canonical(oldq)!=old['frozen_moment_Q_definition_identity_sha256']
            or canonical(newq)!=new['frozen_moment_Q_definition_identity_sha256']):
        raise ValueError('Bind both complete literal-Q definitions to their own exact full frozen points')
    qcopy=copy.deepcopy(newq)
    qcopy.update(schema=oldq['schema'],base_model_identity_sha256=canonical(oldbase),
        initial_full_point_sha256=oldpoint)
    if qcopy!=oldq:
        raise ValueError('Every original Q word, support and entire seed/target definition must be retained')
    oldcal,newcal=old['reference_centering_definition'],new['reference_centering_definition']
    if (oldcal.get('original_reference_point_sha256')!=oldpoint
            or newcal.get('original_reference_point_sha256')!=newpoint
            or newcal.get('frozen_reference_M')!=160 or newcal.get('current_M')!=320
            or newcal.get('current_layout_reference_point_is_old_layout_byte_identical') is not False
            or newcal.get('frozen_seed_and_original_reference_core_H_unchanged') is not True):
        raise ValueError('Distinguish exact fixed seed identity from distinct current coordinate bytes')
    calcopy=copy.deepcopy(newcal)
    for key in ('reference_point_coordinate_layout','frozen_reference_M','current_M',
            'current_layout_reference_point_is_old_layout_byte_identical',
            'frozen_seed_and_original_reference_core_H_unchanged'):
        calcopy.pop(key)
    calcopy.update(source_sha256=oldcal['source_sha256'],
        endpoint_source_sha256=oldcal['endpoint_source_sha256'],
        original_reference_point_sha256=oldpoint,base_model_identity_sha256=canonical(oldbase))
    if calcopy!=oldcal:
        raise ValueError('The complete frozen quadrature/centering definition changed beyond declared coordinates and sources')
    for key in old_policy_keys:before.pop(key)
    for key in POLICY_KEYS.values():after.pop(key)
    after.update(base_complete_model=copy.deepcopy(oldbase),
        base_model_identity_sha256=canonical(oldbase),base_source_sha256=old['base_source_sha256'],
        base_schema=old['base_schema'],M=160,frozen_moment_Q_definition=copy.deepcopy(oldq),
        frozen_moment_Q_definition_identity_sha256=canonical(oldq),
        literal_Q_input_schema=old['literal_Q_input_schema'],
        new_reference_input_binding_source_sha256=old['new_reference_input_binding_source_sha256'],
        reference_centering_definition=copy.deepcopy(oldcal),
        schema=old['schema'],source_sha256=old['source_sha256'])
    if before!=after:
        raise ValueError('An undeclared fixed target, original variable, gamma, partition, observation or implicit-selection parameter changed')
    return dict(complete_unchanged_definition_sha256=canonical(before),
        exact_old_complete_model_identity_sha256=canonical(old),
        exact_new_complete_model_identity_sha256=canonical(new),
        original_base_model_identity_sha256=canonical(oldbase),
        current_base_model_identity_sha256=canonical(newbase),
        reference_M=160,current_M=320,full_N=2048,J=923,
        frequency_layout_identity_sha256=newbase['frequency_layout_identity_sha256'],
        frozen_original_point_relation=relation,
        full_fixed_reference_chart_profile_seed_mesh_Q_gamma_partition_and_observer_equal=True,
        only_declared_current_frequency_layout_and_complete_source_policies_changed=True,
        computed_float_field_equality_claimed=False,
        exact_selected_field_inclusion_requires_compatible_implicit_branch=True,
        original_geometry_or_metric_certificate_inherited=False)


def frequency_refinement_binding(report,*,roles,source_directory):
    module=_layout(source_directory)
    model=report['representation'];base=model['base_complete_model']
    layout=module.validate_base_model(base,expected_base_source_sha256=BASE_SOURCE_SHA256)
    if (roles.get('frequency_layout')!=sha(module.__file__)
            or report.get('frequency_layout_definition')!=layout
            or report.get('frequency_layout_identity_sha256')!=canonical(layout)
            or report.get('frequency_layout_source',{}).get('sha256')!=sha(module.__file__)
            or report.get('reference_M')!=160 or report.get('current_M')!=320
            or report.get('M')!=320 or report.get('N')!=2048 or report.get('J')!=923
            or report.get('original_variables')!=layout['current_free_size']
            or report.get('radial_observation_refinement_performed') is not False
            or report.get('angular_observation_refinement_performed') is not False
            or report.get('saved_parent_Phi_used_as_current_baseline') is not False):
        raise ValueError('Declare the entire M-only inclusion and unchanged N/radial observation rules')
    norm=report['coordinate_norm']
    if canonical({k:v for k,v in norm.items() if k!='norm_identity_sha256'})!=norm.get('norm_identity_sha256'):
        raise ValueError('The complete current norm identity must be independently read')
    transfer=report['material_envelope_transfer']
    relation=validate_frozen_point_relation(transfer['frozen_original_point_relation'],
        model,source_directory=source_directory)
    record=report.get('frequency_refinement')
    if (not isinstance(record,dict)
            or record.get('frequency_layout_identity_sha256')!=canonical(layout)
            or record.get('current_full_point_sha256')!=report.get('initial_full_variable_point_sha256')
            or record.get('frozen_original_point_relation')!=relation
            or record.get('source_sha256')!=report.get('material_envelope_transfer_source',{}).get('sha256')):
        raise ValueError('The actual fine first point and fixed seed inclusion must remain separate')
    mode=record.get('mode')
    if mode in ('fresh-original-reference-zero-inclusion','terminal-history-original-reference-zero-inclusion'):
        if (record['current_full_point_sha256']!=relation['current_full_point_sha256']
                or report.get('restart') is not None
                or report.get('explicit_prior_final_variable_seed_requested') is not False
                or report.get('prior_envelope_final_variable_seed') is not None):
            raise ValueError('A fresh/reference point must not impersonate a returned parent final')
        expected=('explicit-independent-branch' if mode=='fresh-original-reference-zero-inclusion'
            else 'strict-current-target-terminal-transfer')
        if transfer.get('current_invocation_memory_mode')!=expected:
            raise ValueError('Keep explicit fresh and actual terminal-history modes distinct')
    elif mode=='actual-complete-parent-zero-inclusion':
        seed=report.get('prior_envelope_final_variable_seed')
        if (not isinstance(seed,dict) or record.get('coordinate_inclusion')!=seed.get('coordinate_inclusion')
                or record.get('parent_report')!=seed.get('parent_report')
                or report.get('explicit_prior_final_variable_seed_requested') is not True):
            raise ValueError('Bind the real complete prior final and all its uncapped history')
        included=module.validate_inclusion(record['coordinate_inclusion'],layout)
        if included['current_full_point_sha256']!=record['current_full_point_sha256']:
            raise ValueError('The full zero inclusion must equal the actual first M320 point')
    elif mode=='same-source-complete-restart':
        if (report.get('restart') is None or record.get('restart_report')!=transfer.get('actual_same_source_restart_report')
                or report.get('explicit_prior_final_variable_seed_requested') is not False):
            raise ValueError('A same-source restart requires its actual complete source-bound report')
    else:raise ValueError('Use one explicitly declared M320 input mode')
    for key in ('all_original_free_variables_retained','all_new_mode_initialization_explicit',
            'fixed_reference_seed_unchanged','new_initial_field_roots_geometry_and_norm_require_read'):
        if record.get(key) is not True:raise ValueError('Keep every complete inclusion responsibility: '+key)
    if record.get('old_values_roots_norm_or_certificates_inherited') is not False:
        raise ValueError('No old computed field or certificate may be inherited')
    return dict(schema='actual-public09-M320-complete-refinement-binding-v1',
        source_sha256=sha(__file__),layout=layout,layout_identity_sha256=canonical(layout),
        reference_M=160,current_M=320,full_N=2048,J=923,mode=mode,
        actual_initial_full_point_sha256=record['current_full_point_sha256'],
        frozen_original_point_relation=relation,
        all_original_free_variables_retained=True,
        exact_selected_field_inclusion_requires_compatible_implicit_branch=True,
        old_field_values_or_certificates_inherited=False)
