"""P96: first complete same-selected phase row on the original96 TC trials."""
from __future__ import annotations
import argparse, ast, gzip, hashlib, importlib.util, json, os, platform, sys
import tempfile, time, traceback
from fractions import Fraction as F
from pathlib import Path

REPO = 'Rogerhu12/math-research-public'
TOPIC = 'topics/visible-flex-exact-nearby'
SOURCE = TOPIC+'/scripts/fourfold_codazzi_finite_trial_phase_owner.py'
MATH = TOPIC+'/scripts/fourfold_codazzi_finite_trial_phase_math.py'
CARRIERS = TOPIC+'/scripts/fourfold_codazzi_finite_trial_phase_carriers.py'
RESTORE = TOPIC+'/scripts/fourfold_codazzi_finite_trial_phase_restore.py'
WORKER = TOPIC+'/scripts/fourfold_codazzi_finite_trial_phase_public_worker.py'
GENERATOR = TOPIC+'/scripts/make_finite_trial_phase_manifest.py'
PROOF = TOPIC+'/results/R149-supplement-complete-phase-row-on-original-finite-trials.md'
OLD_PHASE_CARRIERS = TOPIC+'/scripts/fourfold_codazzi_strict_nu_phase_carriers.py'
OLD_PHASE_MATH = TOPIC+'/scripts/fourfold_codazzi_strict_nu_phase_math.py'
OLD_PHASE_WORKER = TOPIC+'/scripts/fourfold_codazzi_strict_nu_phase_public_worker.py'
NP_MANIFEST = TOPIC+'/notes/2026-11-27-strict-nu-particular-inputs.json'
TC_MANIFEST = TOPIC+'/notes/2026-11-27-true-root-trial-separated-grid-inputs.json'
TC_BASE = TOPIC+'/notes/true_root_trial_residual_ci/run-45889161044-1'
KIND = 'R149_complete_original_finite_trial_phase_row_v1'
MANIFEST_KIND = 'R149_complete_original_finite_trial_phase_row_inputs_v1'
STAGE = 'complete_original_finite_trial_phase_row'
STOP = '1249886203106135147/5242880000000000000'
RUNTIME = {'python':'3.12.14','packages':{'numpy':'2.3.5','python-flint':'0.9.0'}}
PARAMETERS = {
    'arithmetic_bits':320,'original_phase_recipe_bits':256,'decimal_record_digits':40,
    'maximum_scientific_wall_seconds':18000,'complete_trial_columns':96,
    'complete_trial_nodes':7671,'complete_trial_real_dimension':193,'complete_trial_arrays':4,
    'whole_original_body_rows':7721,'complete_original_certificate_cells':7724,
    'necessary_original_phase_germs':169,'necessary_original_phase_steps':3095,
    'original_phase_extent':64,'original_phase_radial_degree':12,
    'complete_angular_grid':1024,'maximum_complete_adjoint_row_degree':160,
    'original_trial_degree':96,'exact_radial_trial_degree':7,'exact_radial_row_moments':8,
    'exact_phase_carrier_interval':['0',STOP],
    'exact_true_root_interval':['1191984371497/5000000000000','2383968743003/10000000000000'],
    'physical_frequency_factor':4,'normalized_angular_measure':True,
    'selected_member_run':'43588332723/1','selected_member_loss':'1/250',
    'fixed_intrinsic_parameter':'eta_0','selected_absolute_delta_upper':'1/10000000000',
    'full_label_derivative_upper':'11/10','complete_squared_label_error_upper':'3521/100000000',
    'complete_selected_field_difference_upper':'307/200000000','complete_root_sliver_receiver':'54',
    'same_original_trial_factory_OPENBLAS_CORETYPE':'Haswell',
    'true_root_not_replaced_by_proposal_dyadic':True,
    'true_phase_constant_is_not_reset':True,'both_independent_means_retained':True,
    'unused_direction_array_restoration_required':False,
    'old_completed_scientific_targets_recomputed':False,'new_complete_targets':6,
}
TARGETS = [
    'complete_original_TC_phase_trial_row96',
    'complete_original_TC_negative_trial_L1_L2_upper96',
    'complete_original_TC_negative_phase_field_L1_upper96',
    'complete_true_root_phase_sliver_upper96',
    'complete_same_selected_TC_phase_row96',
    'complete_same_selected_TC_phase_joint_radius_upper',
]
SCI_FIELDS = sorted([
    'identity','parameters','runtime','complete','proved','actual_returncode','failure','stage',
    'completed_targets','current_target','candidate_record','new_records','saved_record_count',
    'whole_completed_inputs','reference_identity','selected_member_identity','copied_prior_scalar_records',
    'necessary_original_trial_receipts','necessary_original_phase_receipts','necessary_original_carrier_calls',
    'phase_integral_prefix','result','old_scientific_target_calls','new_arrays_published',
    'new_artifacts','new_Releases','wall_seconds',
])


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(',',':'),
                       ensure_ascii=False,allow_nan=False)+'\n').encode()


def parse(raw):
    return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw,
                      parse_constant=lambda x:(_ for _ in ()).throw(ValueError(x)))


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def atomic(path, raw):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    candidate = path.with_name(path.name+'.candidate')
    with candidate.open('wb') as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(candidate, path)


def gather(root, tree_metadata, complete_cover):
    root = Path(root)
    current, roles = {}, {}
    def add(role, path, expected=None, remember=True):
        require(path.startswith(TOPIC+'/') and '..' not in Path(path).parts, 'complete topic input')
        raw = (root/path).read_bytes()
        raw.decode()
        require(0 < len(raw) < 100000, 'one complete small current input: '+path)
        if path.endswith('.py'):
            ast.parse(raw.decode(), filename=path)
        spec = {'role':role,'path':path,'bytes':len(raw),'sha256':sha(raw),
                'git_blob_sha':hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()}
        if expected is not None:
            require(all(spec[k] == expected[k] for k in ('path','bytes','sha256','git_blob_sha')),
                    'the entire unchanged inherited input: '+role)
        current.setdefault(path, spec)
        if remember:
            roles[role] = path
        return parse(raw) if path.endswith('.json') else raw
    npm = add('NP_manifest', NP_MANIFEST)
    review = next(x for x in npm['files'] if x['role'] == 'reviewed_rules')
    add('reviewed_rules', review['path'], review)
    for item in npm['files']:
        add('NP_'+item['role'], item['path'], item, False)
    for role, path in [
        ('TC_manifest',TC_MANIFEST),('TC_state',TC_BASE+'/actual-trial-state.json'),
        ('TC_execution',TC_BASE+'/execution.json'),('TC_prefix',TC_BASE+'/complete-radial-integration-prefix.json'),
        ('TC_matrix',TC_BASE+'/complete-signed-trial-matrices.json'),
        ('science',SOURCE),('phase_math',MATH),('phase_carriers',CARRIERS),('trial_restore',RESTORE),
        ('worker',WORKER),('generator',GENERATOR),('proof',PROOF),
        ('original_phase_carriers',OLD_PHASE_CARRIERS),('original_phase_math',OLD_PHASE_MATH),
        ('original_phase_worker',OLD_PHASE_WORKER),
        ('proof_PH',TOPIC+'/results/R147-supplement-exact-nonlocal-phase-and-height-parameter-ports.md'),
        ('proof_RP',TOPIC+'/results/R144-supplement-full-off-constraint-principal-return-Hessian.md'),
    ]:
        add(role, path)
    history = [dict(x, role='NP_'+x['role']) for x in npm['historical_inputs']]
    require(len(history) == 51, 'the complete original base, rows and selected-family input closure')
    carrier = load(root/CARRIERS, '_P96_input_plan')
    old, unused = carrier.original(root/OLD_PHASE_CARRIERS)
    phase = carrier.plan(root, tree_metadata, complete_cover)
    extra = carrier.expand(phase, old)
    specs = list(current.values())+history+extra
    require(len({x['path'] for x in specs}) == len(specs)
            and len({x['role'] for x in specs}) == len(specs),
            'every current and original whole object occurs once')
    return {'files':sorted(current.values(),key=lambda x:x['role']),
            'historical_inputs':history,'roles':roles,'phase_input_plan':phase}


def admit(manifest, raws, paths):
    roles = manifest['roles']
    npm = parse(raws[roles['NP_manifest']])
    old_np = load(paths[npm['roles']['science']], '_P96_original_selected_metadata')
    prior = old_np.admit_current(npm, raws, paths)
    tcm, state, execution, prefix, matrix = (
        parse(raws[roles[x]]) for x in ('TC_manifest','TC_state','TC_execution','TC_prefix','TC_matrix'))
    require(sha(raws[roles['TC_manifest']]) == 'c5fd0a7a8cd7c6a1a2207e7b640a213ea8dd2ed8bb967107cff969501ed5d447'
            and state['kind'] == 'R149_complete_true_root_finite_trial_residuals_v1'
            and state['run_id'] == execution['run_id'] == prefix['run_id'] == '45889161044'
            and state['run_attempt'] == execution['run_attempt'] == prefix['run_attempt'] == '1'
            and state['input_identity']['manifest_sha256'] == execution['manifest_sha256']
                == matrix['input_manifest_sha256'] == sha(raws[roles['TC_manifest']])
            and state['parameters'] == tcm['parameters'] and tcm['runtime'] == RUNTIME,
            'the actual whole original TC trial and its unchanged defining manifest')
    require(state['complete'] is state['proved'] is execution['complete'] is False
            and state['actual_returncode'] == execution['actual_child_returncode'] == 1
            and state['completed_targets'] == ['complete_signed_finite_trial_matrices_and_waist96']
            and matrix['complete'] is matrix['proved'] is True
            and matrix['complete_rows'] == matrix['complete_columns'] == 96
            and matrix['true_PDE_columns_or_inverse_proved'] is False
            and prefix['next_cell'] == prefix['complete_cell_count'] == 992
            and prefix['total_cells'] == 7724 and prefix['whole_mathematical_target_complete'] is False
            and state['failure']['message'] == 'finite-trial wall budget reached; complete saved radial prefix retained',
            'the old failure and unfinished negative/positive PDE targets remain facts')
    require(state['proposal'] == prefix['proposal_identity'] == matrix['proposal_identity']
            and state['proposal']['definition_sha256'] == matrix['trial_definition_sha256']
            and state['input_identity']['same_selected_family'] == matrix['same_selected_family']
                == prior['R147']['reference_identity']
            and state['input_identity']['original_row_payload_sha256']
                == prior['D']['original_rows_canonical_payload_sha256'],
            'the entire same trial, selected family, true root and7721-row payload')
    expected_files = [{'path':roles[x],'bytes':len(raws[roles[x]]),'sha256':sha(raws[roles[x]])}
                      for x in ('TC_state','TC_prefix','TC_matrix')]
    require(execution['kind'] == 'R149_complete_true_root_finite_trial_execution_v1'
            and execution['scientific_files'] == expected_files
            and execution['scientific_children'] == 1 and execution['child_timeout'] is False
            and execution['old_completed_targets_recomputed'] == state['old_scientific_target_calls'] == 0,
            'the whole original terminal execution binds all three original natural objects')
    current_specs = {x['path']:x for x in manifest['files']}
    old_specs = {x['path']:x for x in tcm['files']}
    for role in ('proposal_math','inputs_math','trial_math','box_math','fft_math','candidate_reader','repair_source'):
        path = npm['roles'][role]
        require(path == tcm['roles'][role]
                and current_specs[path]['sha256'] == old_specs[path]['sha256']
                    == state['input_identity']['scientific_sources'][role],
                'same whole source needed for exact TC rematerialization: '+role)
    p = state['proposal']
    require(p['complete_trial_nodes'] == 7671 and p['complete_certificate_cells'] == 7724
            and p['root_index'] == 3021 and p['root_node'] == 'true_root'
            and len(p['complete_endpoint_arrays']) == 4
            and all(x['shape'] == [7671,193,96] and x['bytes'] == 1137026304
                    for x in p['complete_endpoint_arrays']),
            'all four entire original TC carriers and the exact root convention')
    require(not any(x in sys.modules for x in ('numpy','flint','scipy')),
            'complete metadata admission precedes any numerical call')
    return {'NP_manifest':npm,'prior':prior,'TC_manifest':tcm,'TC_state':state,
            'TC_matrix':matrix,'original_TC_partial_cells':992}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('manifest','input-map','output'):
        parser.add_argument('--'+key, type=Path, required=True)
    parser.add_argument('--manifest-sha', required=True)
    parser.add_argument('--checkout', required=True)
    args = parser.parse_args()
    require(os.environ.get('GITHUB_ACTIONS') == 'true'
            and os.environ.get('GITHUB_REPOSITORY') == REPO
            and os.environ.get('GITHUB_RUN_ATTEMPT') == '1',
            'one authorized first public P96 target')
    raw_manifest = args.manifest.read_bytes()
    manifest = parse(raw_manifest)
    require(sha(raw_manifest) == args.manifest_sha and manifest['kind'] == MANIFEST_KIND
            and manifest['scientific_kind'] == KIND and manifest['stage'] == STAGE
            and manifest['parameters'] == PARAMETERS and manifest['runtime'] == RUNTIME
            and manifest['target_order'] == TARGETS and manifest['allowed_scientific_fields'] == SCI_FIELDS,
            'the whole concrete P96 mathematical contract')
    input_map = parse(args.input_map.read_bytes())
    current = {x['role']:x for x in manifest['files']}
    for role in ('phase_carriers','original_phase_carriers'):
        require(sha(Path(input_map[role]).read_bytes()) == current[role]['sha256'],
                'complete phase metadata/recipe helper')
    carrier = load(input_map['phase_carriers'], '_P96_full_phase_carrier')
    old_carrier, old_raw = carrier.original(input_map['original_phase_carriers'])
    specs = manifest['files']+manifest['historical_inputs']+carrier.expand(manifest['phase_input_plan'],old_carrier)
    require(set(input_map) == {x['role'] for x in specs}, 'all complete current and original input objects')
    raws, paths = {}, {}
    for item in specs:
        path = Path(input_map[item['role']])
        raw = path.read_bytes()
        require(len(raw) == item['bytes'] and sha(raw) == item['sha256'],
                'whole frozen input: '+item['role'])
        raws[item['path']], paths[item['path']] = raw, path
    require(sha(Path(__file__).read_bytes()) == current['science']['sha256'],
            'the entire actual running owner')
    sys.dont_write_bytecode = True
    admitted = admit(manifest, raws, paths)
    phase_admit, phase_consume, adapter_receipt = carrier.full_functions(old_carrier, old_raw)
    phases = phase_admit(manifest['phase_input_plan'], raws)
    npm, prior = admitted['NP_manifest'], admitted['prior']
    nr = npm['roles']
    helper = load(paths[nr['inputs_math']], '_P96_original_TC_inputs')
    rows, part_receipts = helper.admit_all_rows(
        [paths[x['path']] for x in npm['historical_inputs'] if x['role'].startswith('original_rows_')],
        {'old_body_manifest':parse(raws[nr['old_body_manifest']]),'NW':{'difference':prior['D']}})
    require(not args.output.exists(), 'every actual output and accepted prefix is preserved')
    state = {
        'identity':{'kind':KIND,'scalar_stage':STAGE,'manifest_sha256':args.manifest_sha,
            'source_sha256':sha(Path(__file__).read_bytes()),'run_id':os.environ['GITHUB_RUN_ID'],
            'run_attempt':'1','event_commit':os.environ['GITHUB_SHA'],
            'actual_checkout_commit':args.checkout,'arithmetic_bits':320},
        'parameters':PARAMETERS,'runtime':{},'complete':False,'proved':False,
        'actual_returncode':None,'failure':None,'stage':'complete_original_inputs_admitted',
        'completed_targets':[],'current_target':None,'candidate_record':None,'new_records':{},
        'saved_record_count':0,'whole_completed_inputs':{
            'complete_input_inventory_sha256':sha(canonical(specs)),
            'current_files':len(manifest['files']),'historical_files':len(specs)-len(manifest['files']),
            'whole_original_body_rows':len(rows),'all40_original_parts_admitted':True,
            'phase_input_receipt':phases['receipt'],'phase_adapter_receipt':adapter_receipt,
            'original_TC_partial_cells':992,'original_TC_full_negative_result_complete':False},
        'reference_identity':prior['R147']['reference_identity'],
        'selected_member_identity':prior['R147']['selected_member_identity'],
        'copied_prior_scalar_records':{},'necessary_original_trial_receipts':None,
        'necessary_original_phase_receipts':None,
        'necessary_original_carrier_calls':{'TC_floating_factory':0,'original_nodal_QR':0},
        'phase_integral_prefix':None,'result':None,'old_scientific_target_calls':0,
        'new_arrays_published':0,'new_artifacts':0,'new_Releases':0,'wall_seconds':0.,
    }
    require(sorted(state) == SCI_FIELDS, 'the entire scientific result envelope')
    started = time.perf_counter()
    def save(enforce=True):
        state['wall_seconds'] = time.perf_counter()-started
        if enforce:
            require(state['wall_seconds'] <= PARAMETERS['maximum_scientific_wall_seconds'],
                    'P96 mathematical wall budget; accepted complete germs retained')
        raw = canonical(state)
        require(len(raw) <= manifest['operation']['maximum_scientific_bytes'],
                'whole complete public scientific receipt budget')
        atomic(args.output, raw)
    def progress(stage, detail):
        state['stage'] = stage
        if stage == 'necessary_same_four_TC_trial_arrays':
            state['necessary_original_carrier_calls']['TC_floating_factory'] = 1
        save()
        print(json.dumps({'stage':stage,**detail}), flush=True)
    save()
    try:
        import numpy as np
        import flint
        from importlib.metadata import version
        runtime = {'python':platform.python_version(),
                   'packages':{name:version(name) for name in RUNTIME['packages']}}
        require(runtime == RUNTIME and sys.byteorder == 'little' and platform.machine() == 'x86_64',
                'same complete original directed and floating runtime')
        state['runtime'] = {**runtime,'OPENBLAS_CORETYPE':os.environ.get('OPENBLAS_CORETYPE')}
        flint.ctx.prec = 320
        arb = flint.arb
        def ball(record):
            value = arb(record['ball'])
            if 'lower' in record and 'upper' in record:
                value = value.union(arb(record['lower'])).union(arb(record['upper']))
            require(value.is_finite(), 'whole finite original or new ball')
            return value
        def record(value, direction):
            value = value if direction == 'signed_enclosure' else value.upper()
            require(value.is_finite() and (direction == 'signed_enclosure' or value >= 0),
                    'whole finite directed record')
            result = {'ball':value.str(PARAMETERS['decimal_record_digits']),'bound':direction}
            require(arb(result['ball']).contains(value), 'the complete directed scalar is serialized')
            return result
        def publish(name, value, direction):
            index = state['saved_record_count']
            require(name == TARGETS[index], 'next complete declared target')
            if direction == 'upper':
                saved = record(value, 'upper')
            else:
                require(len(value) == 96, 'all96 entries in one complete target')
                bound = 'upper' if direction == 'upper96' else 'signed_enclosure'
                saved = {'complete_count':96,'bound':bound,
                         'balls':[record(x,bound)['ball'] for x in value]}
                if direction == 'signed96_with_centres':
                    saved['exact_dyadic_centres'] = [str(F.from_float(float(arb(x).mid()))) for x in saved['balls']]
            state['current_target'] = name
            state['candidate_record'] = {'name':name,'record':saved}
            save()
            require(parse(args.output.read_bytes())['candidate_record'] == state['candidate_record'],
                    'the entire new candidate is saved before its target marker')
            state['new_records'][name] = saved
            state['completed_targets'].append(name)
            state['saved_record_count'] += 1
            state['current_target'] = state['candidate_record'] = None
            if index == 2:
                prefix = state['phase_integral_prefix']
                original_prefix_sha = sha(canonical(prefix))
                for key in ('signed_original_trial_row96','complete_trial_L1_L2_upper96','complete_field_L1_upper96'):
                    del prefix[key]
                prefix['complete_accumulators_in_new_records'] = TARGETS[:3]
                prefix['whole_completed_integral_prefix_sha256'] = original_prefix_sha
            save()
            restored = parse(args.output.read_bytes())['new_records'][name]
            if direction == 'upper':
                return arb(restored['ball']).upper()
            values = [arb(x) for x in restored['balls']]
            return [x.upper() for x in values] if direction == 'upper96' else values
        rw = prior['RW']
        R31, K48, H = (parse(raws[nr[x]]) for x in ('RW_R31_native','RW_K_native','RW_H_native'))
        chosen = rw['chosen']
        require(ball(chosen['physical_true_conjugacy_minus_G_norm']).upper() < arb('2.211e-7')
                and ball(chosen['physical_true_conjugacy_derivative_Astrip_upper']).upper() < arb(33)/32
                and ball(R31['complete_real_parameter_one_leg_Lipschitz']).upper() < arb(1)/16
                and ball(R31['complete_return_first_parameter']).upper() < arb('.541')
                and ball(K48['postcomposition_real_derivative_minus_one_norm']).upper() < arb('1.422e-8')
                and 1+ball(H['H_prime_minus_one_strip_norm']).upper() < arb(33)/32
                and ball(phases['label']['full_true_endpoint_derivative_error']).upper() < arb('2e-12'),
                'all whole original bounds used in the full selected-label proof')
        state['copied_prior_scalar_records'] = {
            'true_H_minus_G':chosen['physical_true_conjugacy_minus_G_norm'],
            'true_H_prime':chosen['physical_true_conjugacy_derivative_Astrip_upper'],
            'partial_leg_Lipschitz':R31['complete_real_parameter_one_leg_Lipschitz'],
            'full_parameter_flow':R31['complete_return_first_parameter'],
            'K48_derivative_change':K48['postcomposition_real_derivative_minus_one_norm'],
            'H24_derivative_change':H['H_prime_minus_one_strip_norm'],
            'full_transport_derivative_error':phases['label']['full_true_endpoint_derivative_error']}
        core = load(paths[nr['trial_math']], '_P96_original_directed_core')
        base_math = load(paths[nr['nu_math']], '_P96_original_base_polynomials')
        phase_math = load(paths[manifest['roles']['original_phase_math']], '_P96_original_phase_polynomials')
        math_module = load(paths[manifest['roles']['phase_math']], '_P96_new_full_functional')
        restore = load(paths[manifest['roles']['trial_restore']], '_P96_same_TC_array_restorer')
        require(list(math_module.OUTPUT_ORDER) == TARGETS, 'all six declared whole new targets')
        backend, unused_receipts = helper.directed_backend(
            np, flint, raws[nr['box_math']], raws[nr['fft_math']])
        c = core.DirectedContext(np, arb, backend['Box'], backend['CBox'], backend['zeros'],
                                backend['arb_box'], backend['reduce_box'], backend['DirectedFFT']())
        reader, unused = helper.candidate_reader(np, raws[nr['candidate_reader']])
        iterator, unused = helper.repair_iterator(raws[nr['repair_source']])
        base = reader(paths[nr['base_index']])
        repair = parse(raws[nr['old_centre_repair']])
        with tempfile.TemporaryDirectory(prefix='private-P96-original-carriers-') as private:
            jets, definition, plan, offsets, exact_offsets, receipts = restore.restore(
                np, flint, c, helper, base, iterator, repair, rows,
                admitted['TC_manifest'], admitted['TC_state'], paths[nr['proposal_math']], private, progress)
            state['necessary_original_trial_receipts'] = receipts
            save()
            integrator = math_module.Integrator(c, core, helper, phase_math, base_math,
                        base, offsets, definition, plan, jets, ball)
            namespace = old_carrier.recurrence_namespace(raws[nr['RW_H_transport_source']], flint)
            original_nodes = [F.from_float(float(x)) for x in base['radial_nodes']]
            def completed_germ(index, edge, steps, chain):
                prefix = integrator.prefix(record)
                prefix.update(last_complete_original_germ=index, complete_original_steps=steps,
                    whole_original_polynomial_receipt_chain_sha256=chain)
                state['phase_integral_prefix'] = prefix
                state['stage'] = 'complete_new_phase_integral_germ_prefix'
                save()
                require(parse(args.output.read_bytes())['phase_integral_prefix'] == prefix,
                        'one entire accepted96-column new radial prefix')
                print(json.dumps({'stage':state['stage'],'complete_original_germs':index+1,
                    'new_complete_intersections':integrator.cells,'exact_endpoint':str(edge)}),flush=True)
            state['necessary_original_phase_receipts'] = phase_consume(
                phases, namespace, flint, base, helper.ALPHA, original_nodes, exact_offsets, H,
                integrator.consume, completed_germ)
            save()
            math_module.finish(c, integrator, publish)
            state['result'] = {
                'kind':KIND,'complete_new_target_count':6,'complete_new_target_order':TARGETS,
                'complete_signed_phase_columns':96,'same_original_selected_Q_delta':True,
                'same_four_whole_original_TC_arrays':True,'all169_original_phase_germs':True,
                'all3095_original_two_leg_polynomial_hashes':True,
                'complete_true_root_sliver_included':True,'complete_true_root_sliver_cells':integrator.sliver_cells,
                'full_adjoint_row_formed_before_finite_pairing':True,
                'all_eight_exact_radial_moments_retained':True,
                'complete_selected_label_and_background_errors_paid':True,
                'both_means_and_original_phase_constant_retained':True,
                'same_original_orthonormal_trial_input_coordinates':True,
                'complete_final_balls_and_exact_dyadic_centres_saved':True,
                'joint_radius_includes_all_final_ball_radii':True,
                'every_dependent_target_uses_whole_saved_readback':True,
                'old_scientific_targets_recomputed':False,'new_trial_selected':False,
                'true_PDE_corrected_columns_proved':False,'original_TC_negative_result_complete':False,
                'full_regular_or_Theta_inverse_proved':False,
                'full_phase_Schur_or_topic_completion_proved':False,
            }
        state.update(complete=True,proved=True,actual_returncode=0,
                     stage='complete_'+STAGE+'_scalar_branch')
        save()
        return 0
    except BaseException as error:
        state.update(complete=False,proved=False,actual_returncode=1,
            failure={'type':type(error).__name__,'message':str(error)[:2500],
                     'traceback':traceback.format_exc()[-5000:]})
        save(False)
        print(json.dumps({'actual_failure':state['failure'],'saved_record_count':state['saved_record_count']}),flush=True)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
