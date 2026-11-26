"""PHI first signed nonlocal phase functional of the original strict nu column."""
from __future__ import annotations
import argparse, ast, gzip, hashlib, importlib.util, json, os, platform, sys, tempfile, time, traceback
from fractions import Fraction
from pathlib import Path

REPO = 'Rogerhu12/math-research-public'
TOPIC = 'topics/visible-flex-exact-nearby'
SOURCE = TOPIC+'/scripts/fourfold_codazzi_strict_nu_phase_owner.py'
MATH = TOPIC+'/scripts/fourfold_codazzi_strict_nu_phase_math.py'
CARRIERS = TOPIC+'/scripts/fourfold_codazzi_strict_nu_phase_carriers.py'
RESTORE = TOPIC+'/scripts/fourfold_codazzi_strict_nu_trial_carrier_restore.py'
WORKER = TOPIC+'/scripts/fourfold_codazzi_strict_nu_phase_public_worker.py'
GENERATOR = TOPIC+'/scripts/make_strict_nu_phase_manifest.py'
PROOF = TOPIC+'/results/R147-supplement-first-signed-nonlocal-phase-pairing-of-the-strict-parameter-column.md'
PH = TOPIC+'/results/R147-supplement-exact-nonlocal-phase-and-height-parameter-ports.md'
NP_MANIFEST = TOPIC+'/notes/2026-11-27-strict-nu-particular-inputs.json'
NP_BASE = TOPIC+'/notes/strict_nu_particular_ci/run-45893562391-1'
SB_MANIFEST = TOPIC+'/notes/2026-11-27-short-strict-nu-error-inputs.json'
SB_BASE = TOPIC+'/notes/short_strict_nu_error_ci/run-45908403884-1'
KIND = 'R147_complete_strict_nu_nonlocal_phase_v1'
MANIFEST_KIND = 'R147_complete_strict_nu_nonlocal_phase_inputs_v1'
STAGE = 'complete_strict_nu_nonlocal_phase'
RUNTIME = {'python':'3.12.14','packages':{'numpy':'2.3.5','python-flint':'0.9.0'}}
PARAMETERS = {
    'arithmetic_bits':320,'original_phase_recipe_bits':256,'decimal_record_digits':60,
    'maximum_scientific_wall_seconds':6000,'complete_frozen_trial_nodes':740,
    'complete_frozen_trial_real_dimension':193,'complete_frozen_arrays':4,'whole_original_body_rows':7721,
    'necessary_original_phase_germs':131,'necessary_original_phase_steps':1572,
    'original_phase_extent':64,'original_phase_radial_degree':12,
    'complete_angular_grid':1024,'maximum_complete_trial_integrand_degree':256,
    'exact_interval':['0','9/50'],'compact_metric_interval':['1/20','9/50'],
    'physical_frequency_factor':4,'physical_period':'pi/2','normalized_angular_measure':True,
    'continuous_centre_definition_sha256':'440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47',
    'continuous_direction_definition_sha256':'6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04',
    'exact_alpha':'6890507429876859/9007199254740992','fixed_intrinsic_parameter':'eta_0',
    'original_selected_run':'43588332723/1','original_selected_loss':'1/250',
    'selected_absolute_delta_upper':'1/10000000000','selected_state_difference_upper':'1/500000000',
    'full_phase_ordinary_L2_dual_upper':'3/2','full_true_phase_derivative_upper':'11/10',
    'complete_label_derivative_error_upper':'1/62500','complete_squared_label_error_upper':'3521/100000000',
    'true_phase_constant_is_not_reset':True,'both_means_and_all_true_response_modes_retained':True,
    'only_necessary_original_carriers_restored':True,'old_scientific_targets_recomputed':False,
    'new_complete_scalar_records':6,
}
TARGETS = ['complete_original_trial_phase_pairing','complete_original_trial_phase_field_L1_upper',
    'complete_selected_trial_phase_field_difference_L1_upper','complete_label_and_selected_background_phase_fee_upper',
    'complete_true_particular_phase_error_upper','complete_true_strict_parameter_phase_enclosure']
SIGNED_INDICES = (0,5)
SCI_FIELDS = sorted(['identity','parameters','runtime','complete','proved','actual_returncode','failure','stage',
    'completed_targets','current_target','candidate_record','new_records','saved_record_count','whole_completed_inputs',
    'reference_identity','selected_member_identity','copied_prior_scalar_records','necessary_original_trial_receipts',
    'necessary_original_phase_receipts','phase_integral_prefix','result','old_scientific_target_calls',
    'new_arrays_published','new_artifacts','new_Releases','wall_seconds'])


def require(ok,message):
    if not ok:raise ValueError(message)


def sha(raw):return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False)+'\n').encode()


def parse(raw):
    return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw,
        parse_constant=lambda x:(_ for _ in ()).throw(ValueError(x)))


def load(path,name):
    spec = importlib.util.spec_from_file_location(name,path)
    module = importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


def atomic(path,raw):
    path = Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    candidate = path.with_name(path.name+'.candidate')
    with candidate.open('wb') as stream:stream.write(raw);stream.flush();os.fsync(stream.fileno())
    os.replace(candidate,path)


def gather(root,tree_metadata=None):
    root = Path(root);current,roles = {},{}
    def add(role,path,expected=None,remember=True):
        require(path.startswith(TOPIC+'/') and '..' not in Path(path).parts,'whole current topic input')
        raw = (root/path).read_bytes();raw.decode();require(0 < len(raw) < 100000,'small whole current input')
        if path.endswith('.py'):ast.parse(raw.decode(),filename=path)
        spec = {'role':role,'path':path,'bytes':len(raw),'sha256':sha(raw),
            'git_blob_sha':hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()}
        if expected is not None:require(all(spec[k] == expected[k] for k in ('path','bytes','sha256','git_blob_sha')),
            'unchanged complete original input: '+role)
        current.setdefault(path,spec)
        if remember:roles[role] = path
        return parse(raw) if path.endswith('.json') else raw
    npm = add('NP_manifest',NP_MANIFEST)
    review = next(x for x in npm['files'] if x['role'] == 'reviewed_rules')
    add('reviewed_rules',review['path'],review)
    for item in npm['files']:add('NP_'+item['role'],item['path'],item,False)
    for role,path in [('NP_actual',NP_BASE+'/actual-strict-nu-particular.json'),('NP_execution',NP_BASE+'/execution.json'),
        ('SB_manifest',SB_MANIFEST),('SB_actual',SB_BASE+'/actual-short-strict-nu-error.json'),
        ('SB_execution',SB_BASE+'/execution.json'),('science',SOURCE),('phase_math',MATH),('phase_carriers',CARRIERS),
        ('trial_restore',RESTORE),('worker',WORKER),('generator',GENERATOR),('proof',PROOF),('proof_PH',PH),
        ('old_phase_inventory',TOPIC+'/notes/2026-11-14-R133-phase-transport-resume127-inputs.json'),
        ('proof_P',TOPIC+'/results/R133-supplement-full-regular-phase-counterterm-and-actual-error-functional.md'),
        ('proof_L',TOPIC+'/results/R133-supplement-full-label-L2-energy-and-sharp-phase-row.md'),
        ('proof_STC',TOPIC+'/results/R144-supplement-actual-full-frequency-strict-propagation-for-compact-centres.md')]:
        add(role,path)
    history = [dict(x,role='NP_'+x['role']) for x in npm['historical_inputs']]
    require(len(history) == 51,'the complete original NP input closure')
    carrier = load(root/CARRIERS,'_PHI_metadata_phase_plan')
    phase = carrier.plan(root,tree_metadata);extra = carrier.expand(phase)
    all_specs = list(current.values())+history+extra
    require(len({x['path'] for x in all_specs}) == len(all_specs)
        and len({x['role'] for x in all_specs}) == len(all_specs),'distinct whole current and original native objects')
    return {'files':sorted(current.values(),key=lambda x:x['role']),'historical_inputs':history,
        'roles':roles,'phase_input_plan':phase}


def admit(manifest,raws,paths):
    roles = manifest['roles'];npm = parse(raws[roles['NP_manifest']])
    old = load(paths[npm['roles']['science']],'_PHI_original_complete_NP_metadata')
    prior = old.admit_current(npm,raws,paths)
    actual,execution = parse(raws[roles['NP_actual']]),parse(raws[roles['NP_execution']])
    npm_specs = {x['role']:x for x in npm['files']}
    require(actual['complete'] is actual['proved'] is execution['complete'] is True
        and actual['actual_returncode'] == execution['actual_child_returncode'] == 0
        and actual['failure'] is execution['failure'] is None
        and actual['identity']['kind'] == old.KIND and actual['parameters'] == npm['parameters'] == old.PARAMETERS
        and actual['identity']['manifest_sha256'] == sha(raws[roles['NP_manifest']])
        and actual['identity']['source_sha256'] == npm_specs['science']['sha256']
        and actual['identity']['run_id'] == execution['run_id'] == '45893562391'
        and actual['identity']['run_attempt'] == execution['run_attempt'] == '1'
        and actual['completed_targets'] == old.TARGETS and actual['saved_record_count'] == 2
        and set(actual['new_records']) == set(old.TARGETS) and sorted(actual) == npm['allowed_scientific_fields']
        and actual['reference_identity'] == prior['R147']['reference_identity']
        and actual['selected_member_identity'] == prior['R147']['selected_member_identity']
        and execution['scientific_files'] == [{'path':roles['NP_actual'],'bytes':len(raws[roles['NP_actual']]),
                                              'sha256':sha(raws[roles['NP_actual']])}],
        'the whole genuine completed NP result and its implicit selected member')
    for key in ('complete_selected_strict_nu_particular_certified','unknown_true_solution_remains_full_Fourier',
                'both_physical_density_means_retained','all_trial_jumps_proved_zero_from_shared_exact_endpoint_data',
                'direct_positive_and_root_state_exactly_zero'):
        require(actual['result'][key] is True,'original complete qualification: '+key)
    require(len(actual['trial_receipts']['complete_arrays']) == 4
        and all(x['shape'] == [740,193] and x['bytes'] == 1142560 for x in actual['trial_receipts']['complete_arrays'])
        and actual['new_records'][old.TARGETS[1]]['complete_signed_output_count'] == 194
        and actual['new_records'][old.TARGETS[1]]['complete_signed_trial_pairing_count'] == 192,
        'the whole original trial and all completed signed outputs remain distinct')
    sbm,sb,sbe = (parse(raws[roles[x]]) for x in ('SB_manifest','SB_actual','SB_execution'))
    sb_source = next(x for x in sbm['files'] if x['role'] == 'science')
    require(sb['complete'] is sb['proved'] is sbe['complete'] is True
        and sb['actual_returncode'] == sbe['actual_child_returncode'] == 0
        and sb['failure'] is sbe['failure'] is None and sb['parameters'] == sbm['parameters']
        and sb['completed_targets'] == sbm['target_order'] and sb['saved_record_count'] == len(sbm['target_order']) == 11
        and set(sb['new_records']) == set(sbm['target_order']) and sorted(sb) == sbm['allowed_scientific_fields']
        and sb['identity']['kind'] == sbm['scientific_kind']
        and sb['identity']['source_sha256'] == sb_source['sha256']
        and sb['identity']['manifest_sha256'] == sha(raws[roles['SB_manifest']])
        and sb['identity']['run_id'] == sbe['run_id'] == '45908403884'
        and sb['identity']['run_attempt'] == sbe['run_attempt'] == '1'
        and sb['reference_identity'] == actual['reference_identity']
        and sb['selected_member_identity'] == actual['selected_member_identity']
        and sbe['scientific_files'] == [{'path':roles['SB_actual'],'bytes':len(raws[roles['SB_actual']]),
                                       'sha256':sha(raws[roles['SB_actual']])}],
        'all eleven true completed short-receiver outputs on the same particular')
    require(not any(x in sys.modules for x in ('flint','numpy','scipy')),'metadata admission precedes all numerical calls')
    saved = {'trial_L1_L2':actual['new_records'][old.TARGETS[0]]['whole_trial_integrals']['trial_L1_L2'],
        'true_error_L2rL2':sb['new_records'][sbm['target_order'][10]]}
    return {'NP':actual,'NP_manifest':npm,'prior':prior,'SB':sb,'saved':saved}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('manifest','input-map','output'):parser.add_argument('--'+key,type=Path,required=True)
    parser.add_argument('--manifest-sha',required=True);parser.add_argument('--checkout',required=True)
    args = parser.parse_args()
    require(os.environ.get('GITHUB_ACTIONS') == 'true' and os.environ.get('GITHUB_REPOSITORY') == REPO
        and os.environ.get('GITHUB_RUN_ATTEMPT') == '1','one authorized public new phase target')
    raw_manifest = args.manifest.read_bytes();manifest = parse(raw_manifest)
    require(sha(raw_manifest) == args.manifest_sha and manifest['kind'] == MANIFEST_KIND
        and manifest['scientific_kind'] == KIND and manifest['stage'] == STAGE
        and manifest['parameters'] == PARAMETERS and manifest['runtime'] == RUNTIME
        and manifest['target_order'] == TARGETS and manifest['allowed_scientific_fields'] == SCI_FIELDS,
        'the entire first signed phase input contract')
    input_map = parse(args.input_map.read_bytes());base_specs = manifest['files']+manifest['historical_inputs']
    carrier_spec = next(x for x in manifest['files'] if x['role'] == 'phase_carriers')
    carrier_path = Path(input_map['phase_carriers']);require(sha(carrier_path.read_bytes()) == carrier_spec['sha256'],
        'whole exact carrier metadata/recipe helper')
    carrier = load(carrier_path,'_PHI_original_phase_carrier_definitions')
    specs = base_specs+carrier.expand(manifest['phase_input_plan'])
    require(set(input_map) == {x['role'] for x in specs},'every complete current and historical input')
    raws,paths = {},{}
    for item in specs:
        path = Path(input_map[item['role']]);raw = path.read_bytes()
        require(len(raw) == item['bytes'] and sha(raw) == item['sha256'],'whole frozen original input: '+item['role'])
        raws[item['path']],paths[item['path']] = raw,path
    require(sha(Path(__file__).read_bytes()) == next(x['sha256'] for x in specs if x['role'] == 'science'),
            'the full actual running source')
    sys.dont_write_bytecode = True;admitted = admit(manifest,raws,paths)
    phases = carrier.admit(manifest['phase_input_plan'],raws)
    npm,prior = admitted['NP_manifest'],admitted['prior'];nr = npm['roles']
    helper = load(paths[nr['inputs_math']],'_PHI_complete_original_row_admission')
    rows,part_receipts = helper.admit_all_rows([paths[x['path']] for x in npm['historical_inputs']
        if x['role'].startswith('original_rows_')],
        {'old_body_manifest':parse(raws[nr['old_body_manifest']]),'NW':{'difference':prior['D']}})
    require(not args.output.exists(),'preserve every true actual new integral prefix')
    state = {'identity':{'kind':KIND,'scalar_stage':STAGE,'manifest_sha256':args.manifest_sha,
        'source_sha256':sha(Path(__file__).read_bytes()),'run_id':os.environ['GITHUB_RUN_ID'],'run_attempt':'1',
        'event_commit':os.environ['GITHUB_SHA'],'actual_checkout_commit':args.checkout,'arithmetic_bits':320},
        'parameters':PARAMETERS,'runtime':{},'complete':False,'proved':False,'actual_returncode':None,'failure':None,
        'stage':'complete_original_inputs_admitted','completed_targets':[],'current_target':None,'candidate_record':None,
        'new_records':{},'saved_record_count':0,'whole_completed_inputs':{'complete_input_inventory_sha256':sha(canonical(specs)),
            'current_files':len(manifest['files']),'historical_files':len(specs)-len(manifest['files']),
            'whole_original_body_rows':len(rows),'all40_original_parts_admitted':True,
            'phase_input_receipt':phases['receipt']},'reference_identity':admitted['NP']['reference_identity'],
        'selected_member_identity':admitted['NP']['selected_member_identity'],'copied_prior_scalar_records':admitted['saved'],
        'necessary_original_trial_receipts':None,'necessary_original_phase_receipts':None,'phase_integral_prefix':None,
        'result':None,'old_scientific_target_calls':0,'new_arrays_published':0,'new_artifacts':0,'new_Releases':0,'wall_seconds':0.}
    require(sorted(state) == SCI_FIELDS,'the entire new scientific envelope')
    started = time.perf_counter()
    def save(enforce=True):
        state['wall_seconds'] = time.perf_counter()-started
        if enforce:require(state['wall_seconds'] <= PARAMETERS['maximum_scientific_wall_seconds'],'new phase scientific time budget')
        raw = canonical(state);require(len(raw) <= manifest['operation']['maximum_scientific_bytes'],'whole small public new result')
        atomic(args.output,raw)
    def progress(stage,detail):
        state['stage'] = stage;save();print(json.dumps({'stage':stage,**detail}),flush=True)
    save()
    try:
        import numpy as np
        import flint
        from importlib.metadata import version
        runtime = {'python':platform.python_version(),'packages':{x:version(x) for x in RUNTIME['packages']}}
        require(runtime == RUNTIME,'same original directed and floating carrier runtime')
        state['runtime'] = runtime;flint.ctx.prec = 320;arb = flint.arb
        def ball(record):
            value = arb(record['ball'])
            if 'lower' in record and 'upper' in record:value = value.union(arb(record['lower'])).union(arb(record['upper']))
            require(value.is_finite(),'whole finite original or new ball');return value
        def record(value,direction):
            value = value if direction == 'signed_enclosure' else value.upper()
            require(value.is_finite() and (direction == 'signed_enclosure' or value >= 0),'whole finite signed or upper record')
            result = {'ball':value.str(PARAMETERS['decimal_record_digits']),'bound':direction}
            require(arb(result['ball']).contains(value),'all digits and error of the whole directed scalar')
            return result
        def publish(name,value,direction):
            i = state['saved_record_count']
            require(name == TARGETS[i] and direction == ('signed_enclosure' if i in SIGNED_INDICES else 'upper'),
                'next complete scalar in the declared order')
            saved = record(value,direction);state['current_target'] = name
            state['candidate_record'] = {'name':name,'record':saved};save()
            require(parse(args.output.read_bytes())['candidate_record'] == state['candidate_record'],'whole new candidate readback')
            state['new_records'][name] = saved;state['completed_targets'].append(name);state['saved_record_count'] += 1
            state['current_target'] = state['candidate_record'] = None;save()
            restored = ball(parse(args.output.read_bytes())['new_records'][name])
            return restored if direction == 'signed_enclosure' else restored.upper()
        rw = prior['RW'];R31 = parse(raws[nr['RW_R31_native']]);K48 = parse(raws[nr['RW_K_native']])
        H = parse(raws[nr['RW_H_native']]);chosen = rw['chosen']
        require(ball(chosen['physical_true_conjugacy_minus_G_norm']).upper() < arb('2.211e-7')
            and ball(chosen['physical_true_conjugacy_derivative_Astrip_upper']).upper() < arb(33)/32
            and ball(R31['complete_real_parameter_one_leg_Lipschitz']).upper() < arb(1)/16
            and ball(R31['complete_return_first_parameter']).upper() < arb('.541')
            and ball(K48['postcomposition_real_derivative_minus_one_norm']).upper() < arb('1.422e-8')
            and 1+ball(H['H_prime_minus_one_strip_norm']).upper() < arb(33)/32
            and ball(phases['label']['full_true_endpoint_derivative_error']).upper() < arb('2e-12'),
            'all complete original saved bounds used by PH, without recomputing their targets')
        state['copied_prior_scalar_records'].update(
            true_H_minus_G=chosen['physical_true_conjugacy_minus_G_norm'],
            true_H_prime_Astrip=chosen['physical_true_conjugacy_derivative_Astrip_upper'],
            original_real_family_partial_leg_Lipschitz=R31['complete_real_parameter_one_leg_Lipschitz'],
            original_real_family_first_parameter=R31['complete_return_first_parameter'],
            original_K48_derivative_change=K48['postcomposition_real_derivative_minus_one_norm'],
            original_finite_H_derivative_change=H['H_prime_minus_one_strip_norm'],
            original_complete_label_error=phases['label']['full_true_endpoint_derivative_error'])
        core = load(paths[nr['trial_math']],'_PHI_original_directed_algebra')
        nu = load(paths[nr['nu_math']],'_PHI_original_trial_definition')
        math = load(paths[manifest['roles']['phase_math']],'_PHI_new_signed_functional')
        restore = load(paths[manifest['roles']['trial_restore']],'_PHI_unchanged_original_NP_restore')
        require(list(math.OUTPUT_ORDER) == TARGETS and math.SIGNED_INDICES == SIGNED_INDICES,'all six whole new scalar targets')
        with tempfile.TemporaryDirectory(prefix='private-PHI-original-carriers-') as private:
            unused_waist,unused_intrinsic,receipts = restore.restore(np,flint,npm,admitted['NP'],raws,paths,
                helper,rows,part_receipts,private,progress,atomic)
            state['necessary_original_trial_receipts'] = receipts
            jets = [np.memmap(Path(private)/('original_NP_endpoint_derivative_%d.f64'%k),
                     dtype='<f8',mode='r',shape=(740,193)) for k in range(4)]
            backend,_ = helper.directed_backend(np,flint,raws[nr['box_math']],raws[nr['fft_math']])
            c = core.DirectedContext(np,arb,backend['Box'],backend['CBox'],backend['zeros'],
                backend['arb_box'],backend['reduce_box'],backend['DirectedFFT']())
            reader,_ = helper.candidate_reader(np,raws[nr['candidate_reader']])
            iterator,_ = helper.repair_iterator(raws[nr['repair_source']])
            base = reader(paths[nr['base_index']]);nodes,plan = nu.complete_plan(rows,base['radial_nodes'])
            original_nodes = [Fraction.from_float(float(x)) for x in base['radial_nodes']]
            offsets = {key:np.zeros((6144,65)) for key in ('lower','upper')};exact_offsets = {}
            last = max(x['background_piece'] for x in plan)
            for piece,values,_ in iterator(base,nu.ALPHA):
                if piece > last:break
                exact_offsets[piece] = values
                for k,value in enumerate(values):
                    x = c.box(value);offsets['lower'][piece,k],offsets['upper'][piece,k] = float(x.lo),float(x.hi)
            integrator = math.Integrator(c,core,nu,base,offsets,rows,nodes,plan,jets,ball)
            ns = carrier.recurrence_namespace(raws[nr['RW_H_transport_source']],flint)
            def completed_germ(index,edge,steps,chain):
                prefix = integrator.prefix(record)
                prefix.update(last_complete_original_germ=index,complete_original_steps=steps,
                    whole_original_polynomial_receipt_chain_sha256=chain)
                state['phase_integral_prefix'] = prefix
                state['stage'] = 'complete_new_phase_integral_germ_prefix';save()
                require(parse(args.output.read_bytes())['phase_integral_prefix'] == prefix,'whole accepted new integral prefix')
                print(json.dumps({'stage':state['stage'],'completed_original_germs':index+1,
                    'new_complete_intersections':integrator.cells,'exact_endpoint':str(edge)}),flush=True)
            phase_receipts = carrier.consume(phases,ns,flint,base,nu.ALPHA,original_nodes,exact_offsets,H,
                integrator.consume,completed_germ)
            state['necessary_original_phase_receipts'] = phase_receipts;save()
            old_H0 = ball(admitted['saved']['trial_L1_L2']).upper()
            old_error = ball(admitted['saved']['true_error_L2rL2']).upper()
            math.finish(c,integrator,old_H0,old_error,publish)
        final = ball(parse(args.output.read_bytes())['new_records'][TARGETS[5]])
        state['result'] = {'kind':KIND,'complete_new_record_count':6,'complete_new_record_order':TARGETS,
            'same_original_selected_Q_delta':True,'whole_original_NP_arrays_restored':True,
            'whole_original_two_leg_phase_polynomials_restored':True,'original_phase_constant_preserved':True,
            'true_squared_label_weight_used':True,'full_direct_metric_and_state_mean_retained':True,
            'complete_selected_background_change_paid':True,'complete_infinite_PDE_response_error_paid':True,
            'all_accepted_new_integral_prefixes_preserved':True,'every_dependent_scalar_uses_whole_readback':True,
            'strict_particular_only':True,'strict_phase_enclosure_excludes_zero':not final.contains(0),
            'old_phase_residual_or_norm_targets_recomputed':False,'old_NP_scientific_targets_recomputed':False,
            'new_trial_selected':False,'full_regular_response_phase_column_proved':False,
            'physical_height_or_rigid_ports_proved':False,'true_nu_or_phase_Schur_proved':False,'topic_completion_proved':False}
        state.update(complete=True,proved=True,actual_returncode=0,stage='complete_'+STAGE+'_scalar_branch')
        save();return 0
    except BaseException as error:
        state.update(complete=False,proved=False,actual_returncode=1,
            failure={'type':type(error).__name__,'message':str(error)[:2500],
                     'traceback':traceback.format_exc()[-5000:]})
        save(False);print(json.dumps({'actual_failure':state['failure'],'saved_record_count':state['saved_record_count']}),flush=True)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
