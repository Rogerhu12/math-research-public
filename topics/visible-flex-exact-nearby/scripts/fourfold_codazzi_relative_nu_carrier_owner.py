"""RHI first complete relative frame/position strict parameter column."""
from __future__ import annotations
import argparse,ast,gzip,hashlib,importlib.util,json,os,platform,sys,tempfile,time,traceback
from pathlib import Path

REPO='Rogerhu12/math-research-public'
TOPIC='topics/visible-flex-exact-nearby'
SOURCE=TOPIC+'/scripts/fourfold_codazzi_relative_nu_carrier_owner.py'
MATH=TOPIC+'/scripts/fourfold_codazzi_relative_nu_carrier_math.py'
WORKER=TOPIC+'/scripts/fourfold_codazzi_relative_nu_carrier_public_worker.py'
GENERATOR=TOPIC+'/scripts/make_relative_nu_carrier_manifest.py'
PROOF=TOPIC+'/results/R147-supplement-certified-relative-parameter-frame-and-position-carriers.md'
RESTORE=TOPIC+'/scripts/fourfold_codazzi_strict_nu_trial_carrier_restore.py'
ADMISSION=TOPIC+'/scripts/fourfold_codazzi_strict_nu_phase_owner.py'
PARENT_WORKER=TOPIC+'/scripts/fourfold_codazzi_strict_nu_phase_public_worker.py'
NP_MANIFEST=TOPIC+'/notes/2026-11-27-strict-nu-particular-inputs.json'
NP_BASE=TOPIC+'/notes/strict_nu_particular_ci/run-45893562391-1'
SB_MANIFEST=TOPIC+'/notes/2026-11-27-short-strict-nu-error-inputs.json'
SB_BASE=TOPIC+'/notes/short_strict_nu_error_ci/run-45908403884-1'
KIND='R147_complete_relative_strict_nu_carriers_v1'
MANIFEST_KIND='R147_complete_relative_strict_nu_carriers_inputs_v1'
STAGE='complete_relative_strict_nu_carriers'
RUNTIME={'python':'3.12.14','packages':{'numpy':'2.3.5','python-flint':'0.9.0'}}
PARAMETERS={
    'arithmetic_bits':320,'decimal_record_digits':60,'maximum_scientific_wall_seconds':18000,
    'complete_frozen_trial_nodes':740,'complete_frozen_trial_real_dimension':193,'complete_frozen_arrays':4,
    'whole_original_body_rows':7721,'complete_original_certificate_cells':2472,
    'maximum_new_certificate_cells':3947,'maximum_certificate_step':'1/8192',
    'source_angular_grid':1024,'complete_carrier_angular_grid':2048,'source_radial_polynomial_degree':3,
    'chosen_carrier_radial_degree':6,'complete_relative_components':18,'maximum_complete_source_degree':288,
    'angular_strips':['1/256','1/128','1/64'],'exact_interval':['0','9/50'],
    'compact_metric_interval':['1/20','9/50'],'physical_frequency_factor':4,
    'physical_period':'pi/2','normalized_angular_measure':True,
    'exact_alpha':'6890507429876859/9007199254740992','fixed_intrinsic_parameter':'eta_0',
    'selected_absolute_delta_upper':'1/10000000000','selected_state_difference_upper':'1/500000000',
    'continuous_centre_definition_sha256':'440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47',
    'continuous_direction_definition_sha256':'6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04',
    'true_state_error_to_axial_relative_frame':'17/16','true_state_error_to_relative_position':'36/25',
    'component_order':['A_rowmajor9','x3','axial_parameter3','position_parameter3'],
    'actual_metric_variation':1,'both_moving_means_retained':True,
    'world_anchor_frame_position_and_physical_coordinate_ports_independent':True,
    'every_numerical_endpoint_impulse_paid':True,
    'private_whole_carrier_encoding':'little-endian IEEE754 binary64 row-major',
    'proved_reflection_zero_mean_indices':[0,2,4],
    'automatic_scientific_retry':False,'new_complete_targets':4,
}
TARGETS=['complete_same_selected_trial_relative_mean6','complete_same_selected_relative_profile_error4',
    'complete_true_strict_nu_relative_mean6','complete_true_strict_nu_relative_profile_error2']
COUNTS=[6,4,6,2]
SIGNED_INDICES=(0,2)
SCI_FIELDS=sorted(['identity','parameters','runtime','complete','proved','actual_returncode','failure','stage',
    'completed_targets','current_target','candidate_record','new_records','saved_record_count','whole_completed_inputs',
    'reference_identity','selected_member_identity','copied_prior_scalar_records','necessary_original_trial_receipts',
    'relative_carrier_prefix','whole_private_carrier_receipt','result','old_scientific_target_calls',
    'new_arrays_published','new_artifacts','new_Releases','wall_seconds'])


def require(ok,message):
    if not ok:raise ValueError(message)


def sha(raw):return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False)+'\n').encode()


def parse(raw):
    return json.loads(gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw,
        parse_constant=lambda x:(_ for _ in ()).throw(ValueError(x)))


def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


def atomic(path,raw):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True);candidate=path.with_name(path.name+'.candidate')
    with candidate.open('wb') as stream:stream.write(raw);stream.flush();os.fsync(stream.fileno())
    os.replace(candidate,path)


def gather(root):
    root=Path(root);current,roles={},{}
    def add(role,path,expected=None,remember=True):
        require(path.startswith(TOPIC+'/') and '..' not in Path(path).parts,'complete current topic source')
        raw=(root/path).read_bytes();raw.decode();require(0<len(raw)<100000,'small whole current input')
        if path.endswith('.py'):ast.parse(raw.decode(),filename=path)
        spec={'role':role,'path':path,'bytes':len(raw),'sha256':sha(raw),
            'git_blob_sha':hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()}
        if expected is not None:require(all(spec[k]==expected[k] for k in ('path','bytes','sha256','git_blob_sha')),
            'same complete original input: '+role)
        current.setdefault(path,spec)
        if remember:roles[role]=path
        return parse(raw) if path.endswith('.json') else raw
    npm=add('NP_manifest',NP_MANIFEST)
    review=next(x for x in npm['files'] if x['role']=='reviewed_rules');add('reviewed_rules',review['path'],review)
    for item in npm['files']:add('NP_'+item['role'],item['path'],item,False)
    for role,path in [('NP_actual',NP_BASE+'/actual-strict-nu-particular.json'),('NP_execution',NP_BASE+'/execution.json'),
        ('SB_manifest',SB_MANIFEST),('SB_actual',SB_BASE+'/actual-short-strict-nu-error.json'),
        ('SB_execution',SB_BASE+'/execution.json'),('science',SOURCE),('relative_math',MATH),
        ('trial_restore',RESTORE),('metadata_admission',ADMISSION),('parent_worker',PARENT_WORKER),
        ('worker',WORKER),('generator',GENERATOR),('proof',PROOF),
        ('proof_RH',TOPIC+'/results/R147-supplement-relative-height-carriers-and-short-full-frequency-errors.md'),
        ('proof_PH',TOPIC+'/results/R147-supplement-exact-nonlocal-phase-and-height-parameter-ports.md')]:add(role,path)
    history=[dict(x,role='NP_'+x['role']) for x in npm['historical_inputs']]
    require(len(history)==51,'all original necessary NP inputs')
    specs=list(current.values())+history
    require(len({x['path'] for x in specs})==len(specs) and len({x['role'] for x in specs})==len(specs),
            'distinct complete current and original input objects')
    return {'files':sorted(current.values(),key=lambda x:x['role']),'historical_inputs':history,'roles':roles}


def admit(manifest,raws,paths):
    old=load(paths[manifest['roles']['metadata_admission']],'_RHI_unchanged_complete_NP_SB_admission')
    return old.admit(manifest,raws,paths)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','input-map','output'):parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--manifest-sha',required=True);parser.add_argument('--checkout',required=True)
    args=parser.parse_args()
    require(os.environ.get('GITHUB_ACTIONS')=='true' and os.environ.get('GITHUB_REPOSITORY')==REPO
        and os.environ.get('GITHUB_RUN_ATTEMPT')=='1','one public first relative-parameter target')
    raw_manifest=args.manifest.read_bytes();manifest=parse(raw_manifest)
    require(sha(raw_manifest)==args.manifest_sha and manifest['kind']==MANIFEST_KIND
        and manifest['scientific_kind']==KIND and manifest['stage']==STAGE and manifest['parameters']==PARAMETERS
        and manifest['runtime']==RUNTIME and manifest['target_order']==TARGETS
        and manifest['allowed_scientific_fields']==SCI_FIELDS,'entire immutable relative carrier contract')
    input_map=parse(args.input_map.read_bytes());specs=manifest['files']+manifest['historical_inputs']
    require(set(input_map)=={x['role'] for x in specs},'every whole original and current object')
    raws,paths={},{}
    for item in specs:
        path=Path(input_map[item['role']]);raw=path.read_bytes()
        require(len(raw)==item['bytes'] and sha(raw)==item['sha256'],'whole input: '+item['role'])
        raws[item['path']],paths[item['path']]=raw,path
    require(sha(Path(__file__).read_bytes())==next(x['sha256'] for x in specs if x['role']=='science'),
            'whole actual running owner source')
    sys.dont_write_bytecode=True;admitted=admit(manifest,raws,paths)
    npm,prior=admitted['NP_manifest'],admitted['prior'];nr=npm['roles']
    helper=load(paths[nr['inputs_math']],'_RHI_original_full_row_admission')
    rows,part_receipts=helper.admit_all_rows([paths[x['path']] for x in npm['historical_inputs']
        if x['role'].startswith('original_rows_')],
        {'old_body_manifest':parse(raws[nr['old_body_manifest']]),'NW':{'difference':prior['D']}})
    require(not args.output.exists(),'preserve every genuine relative-target execution')
    state={'identity':{'kind':KIND,'scalar_stage':STAGE,'manifest_sha256':args.manifest_sha,
        'source_sha256':sha(Path(__file__).read_bytes()),'run_id':os.environ['GITHUB_RUN_ID'],'run_attempt':'1',
        'event_commit':os.environ['GITHUB_SHA'],'actual_checkout_commit':args.checkout,'arithmetic_bits':320},
        'parameters':PARAMETERS,'runtime':{},'complete':False,'proved':False,'actual_returncode':None,'failure':None,
        'stage':'complete_original_inputs_admitted','completed_targets':[],'current_target':None,'candidate_record':None,
        'new_records':{},'saved_record_count':0,'whole_completed_inputs':{'complete_input_inventory_sha256':sha(canonical(specs)),
            'current_files':len(manifest['files']),'historical_files':51,'whole_original_body_rows':len(rows),
            'all40_original_parts_admitted':True},'reference_identity':admitted['NP']['reference_identity'],
        'selected_member_identity':admitted['NP']['selected_member_identity'],'copied_prior_scalar_records':admitted['saved'],
        'necessary_original_trial_receipts':None,'relative_carrier_prefix':None,'whole_private_carrier_receipt':None,
        'result':None,'old_scientific_target_calls':0,'new_arrays_published':0,'new_artifacts':0,'new_Releases':0,'wall_seconds':0.}
    require(sorted(state)==SCI_FIELDS,'entire scientific result envelope')
    started=time.perf_counter()
    def save(enforce=True):
        state['wall_seconds']=time.perf_counter()-started
        if enforce:require(state['wall_seconds']<=PARAMETERS['maximum_scientific_wall_seconds'],'relative certificate time budget')
        raw=canonical(state);require(len(raw)<=manifest['operation']['maximum_scientific_bytes'],'whole small public result')
        atomic(args.output,raw)
    def progress(stage,detail):
        state['stage']=stage;save();print(json.dumps({'stage':stage,**detail}),flush=True)
    save()
    try:
        import numpy as np
        import flint
        from importlib.metadata import version
        runtime={'python':platform.python_version(),'packages':{x:version(x) for x in RUNTIME['packages']}}
        require(runtime==RUNTIME,'same original NP and directed runtime')
        state['runtime']=runtime;flint.ctx.prec=320;arb=flint.arb
        def ball(record):
            value=arb(record['ball'])
            if 'lower' in record and 'upper' in record:value=value.union(arb(record['lower'])).union(arb(record['upper']))
            require(value.is_finite(),'whole finite original or new scalar');return value
        def record(value,direction):
            value=value if direction=='signed_enclosure' else value.upper()
            require(value.is_finite() and (direction=='signed_enclosure' or value>=0),'finite whole directed ball')
            result={'ball':value.str(PARAMETERS['decimal_record_digits']),'bound':direction}
            require(arb(result['ball']).contains(value),'whole directed scalar serialization')
            return result
        def publish(name,values,direction,centres=None):
            i=state['saved_record_count']
            require(name==TARGETS[i] and len(values)==COUNTS[i]
                and direction==('signed_enclosure' if i in SIGNED_INDICES else 'upper'),'next whole vector target')
            saved={'complete_count':len(values),'bound':direction,'balls':[record(x,direction)['ball'] for x in values]}
            if centres is not None:
                require(i in SIGNED_INDICES and len(centres)==6,'all chosen dyadic grid means distinct')
                saved['exact_dyadic_grid_means']=centres
            state['current_target']=name;state['candidate_record']={'name':name,'record':saved};save()
            require(parse(args.output.read_bytes())['candidate_record']==state['candidate_record'],'whole candidate readback')
            state['new_records'][name]=saved;state['completed_targets'].append(name);state['saved_record_count']+=1
            state['current_target']=state['candidate_record']=None;save()
            restored=parse(args.output.read_bytes())['new_records'][name]
            return [arb(x) if direction=='signed_enclosure' else arb(x).upper() for x in restored['balls']]
        core=load(paths[nr['trial_math']],'_RHI_original_directed_algebra')
        nu=load(paths[nr['nu_math']],'_RHI_original_trial_definition')
        math=load(paths[manifest['roles']['relative_math']],'_RHI_new_complete_relative_algebra')
        restore=load(paths[manifest['roles']['trial_restore']],'_RHI_unchanged_original_NP_restore')
        require(list(math.TARGETS)==TARGETS and math.GRID==2048 and math.ORDER==6,'four complete new targets')
        with tempfile.TemporaryDirectory(prefix='private-RHI-relative-carrier-') as private:
            unused_waist,unused_intrinsic,receipts=restore.restore(np,flint,npm,admitted['NP'],raws,paths,
                helper,rows,part_receipts,private,progress,atomic)
            state['necessary_original_trial_receipts']=receipts;save()
            jets=[np.memmap(Path(private)/('original_NP_endpoint_derivative_%d.f64'%k),dtype='<f8',mode='r',shape=(740,193))
                  for k in range(4)]
            backend,_=helper.directed_backend(np,flint,raws[nr['box_math']],raws[nr['fft_math']])
            c=core.DirectedContext(np,arb,backend['Box'],backend['CBox'],backend['zeros'],
                backend['arb_box'],backend['reduce_box'],backend['DirectedFFT']())
            reader,_=helper.candidate_reader(np,raws[nr['candidate_reader']])
            iterator,_=helper.repair_iterator(raws[nr['repair_source']])
            base=reader(paths[nr['base_index']]);nodes,original_plan=nu.complete_plan(rows,base['radial_nodes'])
            offsets={key:np.zeros((6144,65)) for key in ('lower','upper')}
            last=max(x['background_piece'] for x in original_plan)
            for piece,values,_ in iterator(base,nu.ALPHA):
                if piece>last:break
                for k,value in enumerate(values):
                    x=c.box(value);offsets['lower'][piece,k],offsets['upper'][piece,k]=float(x.lo),float(x.hi)
            integrator=math.Integrator(c,core,nu,base,offsets,rows,nodes,original_plan,jets,ball)
            plan_sha=sha(canonical(integrator.plan));chain=sha(b'RHI complete ordered relative carrier v1\n')
            carrier_path=Path(private)/'complete-relative-endpoint.f64'
            progress('new_complete_relative_carrier_integrating',{'complete_new_cells':len(integrator.plan),
                'grid':2048,'components':18,'all_original_arrays_read_back':True})
            while integrator.cells<len(integrator.plan):
                integrator.step()
                payload=np.asarray(integrator.state,dtype='<f8').tobytes(order='C');atomic(carrier_path,payload)
                receipt={'shape':[2048,18],'bytes':len(payload),'sha256':sha(payload),
                    'encoding':PARAMETERS['private_whole_carrier_encoding']}
                chain=sha(canonical({'previous':chain,'complete_cells':integrator.cells,
                                    'exact_endpoint':str(integrator.edge),'whole_carrier':receipt}))
                state['relative_carrier_prefix']=integrator.prefix(record,receipt,plan_sha,chain)
                state['stage']='complete_new_relative_cell_prefix';save()
                if integrator.cells%32==0 or integrator.cells==len(integrator.plan):
                    print(json.dumps({'stage':state['stage'],'complete_cells':integrator.cells,
                        'total_cells':len(integrator.plan),'exact_endpoint':str(integrator.edge)}),flush=True)
            require(carrier_path.read_bytes()==payload,'entire final18-component private carrier readback')
            state['whole_private_carrier_receipt']=dict(receipt,exact_endpoint='0',complete_readback=True,
                complete_plan_sha256=plan_sha,whole_ordered_receipt_chain_sha256=chain,
                source_sha256=state['identity']['source_sha256'],manifest_sha256=args.manifest_sha,
                actual_runtime=runtime,all18_components_retained=True)
            save()
            details=integrator.finish(ball(admitted['saved']['true_error_L2rL2']).upper(),publish)
        state['result']={'kind':KIND,'complete_new_record_count':4,'complete_new_record_order':TARGETS,
            'same_original_selected_Q_delta':True,'whole_four_original_NP_arrays_restored':True,
            'all_original2472_cells_and_every_true_join_retained':True,'complete_relative18_component_carrier':True,
            'all2048_grid_labels_and_complete_angular_interpolation_errors':True,
            'real_orthogonal_residual_propagation_and_all_rounding_impulses':True,
            'complete_selected_background_direct_metric_and_both_means':True,
            'full_infinite_PDE_response_error_paid':True,'complete_signed_vectors_and_exact_dyadic_means_distinct':True,
            'world_anchors_rigid_ports_and_physical_coordinate_term_independent':True,
            'every_dependent_target_uses_whole_saved_readback':True,'strict_particular_only':True,
            'old_NP_or_phase_scientific_targets_recomputed':False,'original_Z14_materialized':False,
            'new_NP_trial_selected':False,'full_regular_response_proved':False,
            'actual_world_anchor_carrier_computed':False,'full_world_height_signed_value_proved':False,
            'true_phase_height_Schur_or_topic_completion_proved':False,'actual_complete_profile_details':details}
        state.update(complete=True,proved=True,actual_returncode=0,stage='complete_'+STAGE+'_scalar_branch')
        save();return 0
    except BaseException as error:
        state.update(complete=False,proved=False,actual_returncode=1,
            failure={'type':type(error).__name__,'message':str(error)[:2500],'traceback':traceback.format_exc()[-5000:]})
        save(False);print(json.dumps({'actual_failure':state['failure'],'saved_record_count':state['saved_record_count']}),flush=True)
        return 1


if __name__=='__main__':raise SystemExit(main())
