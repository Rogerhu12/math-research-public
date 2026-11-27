"""Complete actual-public09 M160 to M320 history, fixed-point and checkpoint contracts.

Source template only. Its functions are inserted into the complete, strictly pinned
history bridge by the source-only package reproducer; no scientific code runs here.
"""

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
    return dict(schema='actual-public09-M320-input-point-and-fixed-reference-v1',
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
    return _module(Path(__file__).with_name('complete_material_envelope_memory_public_reference.py'),
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
    binding=_module(Path(__file__).with_name('frequency_refined_public_reference_source_binding.py'),ANALYTIC_BINDING_SOURCE_SHA256)
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
        path=Path(q.base.__class__.__init__.__code__.co_filename).parent/'so3_frequency_refinement_layout.py'
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
    layout_module=_module(Path(__file__).with_name('so3_frequency_refinement_layout.py'),LAYOUT_SOURCE_SHA256)
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
