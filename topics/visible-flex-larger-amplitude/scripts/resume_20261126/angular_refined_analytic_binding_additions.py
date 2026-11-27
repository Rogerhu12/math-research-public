"""Complete pure binding additions, embedded by the source-only deriver."""

def _bound_module(path, expected):
    path=Path(path).resolve()
    if sha(path)!=expected:
        raise ValueError('Keep the entire actual pure source '+path.name)
    name='_angular_analytic_binding_'+expected
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    if sha(path)!=expected:
        raise ValueError('The pure source changed while loading')
    return module


def _observer(source_directory):
    return _bound_module(Path(source_directory)/'angular_observation_refinement.py',
        '8506eb861bb8650ddfd0c5db5c268e8bb0a71b38e48ebb551767b45d2d339ab3')


def _validate_original_parent_model(model, source_directory):
    """Validate an entire original N2048 family before normalizing identities."""
    original_source='f34fcafc06b50594b7a651a90e38553ea8ae3da5b6ac8b6ca4ea691d2ab9f14f'
    original=_bound_module(Path(source_directory)/'analytic_j3_source_and_report_binding.py',original_source)
    analytic='04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e'
    adjacent='d5da5e3db88a03cc0afdc00e3a6bc74e425aa3f1b730ea7f66ac278f93d8e6eb'
    if model.get('source_sha256')==analytic:
        roles={name:value[1] for name,value in original.SOURCE_BINDINGS.items()}
        original.validate_current_model(model,roles=roles,source_directory=source_directory)
        keys=tuple(original.POLICY_KEYS.values())
    elif model.get('source_sha256')==adjacent:
        if (model.get('schema')!='complete-R711-reference-centred-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1'
                or model.get('reference_centering_definition',{}).get('source_sha256')
                    !='ccb3340e500a032943aaed084376136fd67ad81b222e1afbcc5e79d468f21ef8'
                or model['reference_centering_definition'].get('endpoint_source_sha256')!=adjacent):
            raise ValueError('Keep the entire actual N2048 adjacent parent calibration')
        policies={
            'normal_frame_C1_reuse':('normal_frame_c1_reuse.py',
                'ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9',
                {'SCHEMA','ORIGINAL_CENTERED_SOURCE','METHOD_AST'}),
            'detached_stage_matrix_reuse':('detached_normal_stage_matrix_reuse.py',
                '375059dc973633a1639ceddd3105fc34fe8b37eec4c9e61a55ce3959a0b9fc59',
                {'SCHEMA','FRAME_C1_SOURCE_SHA256','ORIGINAL_C1_OPERATOR_SOURCE_SHA256','BASE_SOURCE_SHA256','PHASES'}),
            'adjacent_normal_frame_matrices':('adjacent_normal_frame_matrices.py',
                '955dafdc865e34695489f4e8832ecb8a6d48e056f801ba119fd92e9097ad69b3',
                {'SCHEMA','FRAME_C1_SOURCE_SHA256','STAGE_MATRIX_SOURCE_SHA256','PARENT_OPERATOR_SOURCE_SHA256','BASE_SOURCE_SHA256'})}
        for key,(name,digest,constants) in policies.items():
            namespace=original._pure(Path(source_directory)/name,digest,constants,{'sha','definition'})
            if model.get(key)!=namespace['definition']():
                raise ValueError('The entire actual N2048 parent policy changed: '+key)
        keys=tuple(policies)
    else:
        raise ValueError('This N-only relation requires its complete N2048 analytic or adjacent parent')
    base=model.get('base_complete_model',{})
    if (model.get('base_source_sha256')!='6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865'
            or base.get('source_sha256')!=model['base_source_sha256']
            or base.get('schema')!='complete-supported-smooth-triangle-reference-so3-meridian-with-core-lift-v1'
            or canonical(base)!=model.get('base_model_identity_sha256')
            or model.get('base_schema')!=base['schema']
            or model.get('new_reference_input_binding_source_sha256')
                !='307ebae301db059f30ff1cc5fda024b09e9c2730c9f6bffbd82f0821d2a727a7'
            or model.get('literal_Q_input_schema')!='supported-smooth-triangle-reference-literal-zero-endpoint-Q-input-v1'):
        raise ValueError('Keep the actual complete original supported base and Q input')
    return keys


def compatible_legacy_model(old,new,current_pins,*,source_directory):
    """Normalize only the declared observer/source identities; compare all else."""
    roles={role:value[1] for role,value in current_pins.items()}
    validate_current_model(new,roles=roles,source_directory=source_directory)
    old_policy_keys=_validate_original_parent_model(old,source_directory)
    observer=_observer(source_directory)
    observation=observer.validate_base_model(new['base_complete_model'])
    if (roles.get('angular_observation')!=sha(observer.__file__)
            or new.get('new_reference_input_binding_source_sha256')
                !='a4a53ff3ff92bb4fdbf8db2da048c717437d945423932e2b3d69cfc1cc06035d'
            or new.get('literal_Q_input_schema')!='angular-refined-supported-smooth-triangle-literal-Q-input-v1'):
        raise ValueError('Bind the exact complete current observer and dependent Q identity source')
    before,after=copy.deepcopy(old),copy.deepcopy(new)
    old_base,new_base=before['base_complete_model'],after['base_complete_model']
    for key in ('angular_observation_refinement','reference_full_N','current_full_N'):
        new_base.pop(key)
    for base in (old_base,new_base):
        base.pop('schema');base.pop('source_sha256')
    if old_base!=new_base:
        raise ValueError('The fixed full scalar/reference/chart/seed/radial mesh or free layout changed')
    base_identity=canonical(old_base)
    for key in old_policy_keys:
        before.pop(key)
    for key in POLICY_KEYS.values():
        after.pop(key)
    for original,value in ((old,before),(new,after)):
        own_base=original['base_model_identity_sha256']
        value['base_model_identity_sha256']=base_identity
        value['base_complete_model']=copy.deepcopy(old_base)
        for key in ('schema','source_sha256','base_source_sha256','base_schema',
                'literal_Q_input_schema','new_reference_input_binding_source_sha256'):
            value.pop(key)
        calibration=value['reference_centering_definition']
        if calibration.get('base_model_identity_sha256')!=own_base:
            raise ValueError('Each complete calibration must bind its own full base')
        calibration['base_model_identity_sha256']=base_identity
        calibration.pop('source_sha256');calibration.pop('endpoint_source_sha256')
        Q=value['frozen_moment_Q_definition']
        expected_schema=('supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1'
            if original is old else 'angular-refined-supported-smooth-triangle-literal-two-bubble-Q-v1')
        if (Q.get('base_model_identity_sha256')!=own_base or Q.get('schema')!=expected_schema
                or canonical(Q)!=original['frozen_moment_Q_definition_identity_sha256']):
            raise ValueError('Each actual complete Q definition must bind its own base/source schema')
        Q['base_model_identity_sha256']=base_identity
        Q.pop('schema')
        value['frozen_moment_Q_definition_identity_sha256']=canonical(Q)
    if before!=after:
        raise ValueError('Only observer/source/dependent identities may change; keep every target/seed/Q/gamma/tau/free parameter')
    return dict(complete_unchanged_definition_sha256=canonical(before),
        exact_old_complete_model_identity_sha256=canonical(old),
        exact_new_complete_model_identity_sha256=canonical(new),
        full_fixed_reference_chart_profile_seed_mesh_Q_gamma_partition_and_free_layout_equal=True,
        only_explicit_observation_source_schema_and_matrix_working_policy_fields_changed=True,
        reference_full_N=2048,old_current_full_N=2048,new_current_full_N=4096,
        original_angle_words_at_all_even_indices=True,
        angular_observation_definition_identity_sha256=observation['definition_identity_sha256'],
        computed_float_field_equality_claimed=False,old_finite_objective_inherited=False)


def angular_observation_binding(report,*,roles,source_directory):
    observer=_observer(source_directory)
    model=report['representation']
    if roles.get('angular_observation')!=sha(observer.__file__):
        raise ValueError('Bind the actual entire observer source')
    checked=observer.validate_report(report.get('angular_observation_refinement'),model)
    if (report.get('N')!=4096 or report.get('reference_full_N')!=2048
            or report.get('current_full_N')!=4096 or report.get('reference_quarter_angle_count')!=513
            or report.get('current_quarter_angle_count')!=1025
            or report.get('radial_observation_refinement_performed') is not False
            or report.get('full_fixed_reference_target_unchanged') is not True
            or report.get('saved_parent_Phi_used_as_current_baseline') is not False):
        raise ValueError('State the actual N-only scope and new finite-objective responsibility')
    attribution=[]
    def visit(value):
        if isinstance(value,dict):
            if value.get('schema')=='same-current-buffer-dyadic-observation-attribution-v1':
                attribution.append(observer.validate_attribution(value))
            for child in value.values():visit(child)
        elif isinstance(value,list):
            for child in value:visit(child)
    visit(report.get('initial'))
    visit(report.get('final_statistics'))
    visit(report.get('metric_directions',[]))
    visit(report.get('restoration_directions',[]))
    return dict(**checked,actual_same_buffer_attribution_count=len(attribution),
        actual_same_buffer_attributions=attribution,
        old_field_values_or_certificates_inherited=False)
