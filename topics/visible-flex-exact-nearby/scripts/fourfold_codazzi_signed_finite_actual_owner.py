"""Actual SC/JF columns and complete signed96 inverse gates after full P224.

Whole actual low/58/224/32, all TC targets, original RW, actual JC and the
original negative/left receivers are admitted before numerical imports.
No original scalar, residual, norm or JC target is rerun.  Necessary private
TC value/matrix restoration is separately counted and checks original hashes.
"""
from __future__ import annotations
import argparse, ast, copy, hashlib, importlib.util, json, os, platform, sys, time, traceback
from pathlib import Path
from types import SimpleNamespace

REPO = 'Rogerhu12/math-research-public'
TOPIC = 'topics/visible-flex-exact-nearby'
KIND = 'R149_actual_complete_signed_finite_columns_and_gates_v1'
MANIFEST_KIND = 'R149_actual_complete_signed_finite_inputs_v1'
STAGE = 'actual_signed_finite_columns'
SOURCE_PATH = TOPIC+'/scripts/fourfold_codazzi_signed_finite_actual_owner.py'
WORKER_PATH = TOPIC+'/scripts/fourfold_codazzi_signed_finite_actual_public_worker.py'
GENERATOR_PATH = TOPIC+'/scripts/make_signed_finite_actual_manifest.py'
TARGETS = ['complete_true_PDE_waist_column_errors96',
           'complete_true_physical_primitive96_matrix_gate',
           'complete_true_declared_incoming_cosine96_matrix_gate']
FILES = {'state': 'actual-signed-finite-state.json',
         'columns': 'complete-true-waist-column-errors96.json',
         'physical_primitive96': 'complete-true-physical96-gate.json',
         'declared_incoming_cosine96': 'complete-true-incoming96-gate.json'}
ROOT_FIELDS = ('low_odd96_and_moving_mean_root_error_upper',
               'high_root_mixed_error_upper',
               'complete_physical_root_error_upper')
MAXIMUM_COLUMNS_BYTES = 85000
PARAMETERS = {
    'arithmetic_bits': 320, 'public_digits': 60, 'private_digits': 80,
    'complete_columns': 96, 'complete_rows': 96, 'independent_density_means': 2,
    'required_positive_record_counts': [58, 224, 32],
    'required_TC_complete_targets': 3, 'required_RW_complete_rows': 96,
    'required_JC_complete_records': 7,
    'source_normalizer': 'identity on normalized physical root-even96 inputs',
    'target_normalizer': 'identity on the declared true normalized g1..g96 coordinates',
    'source_and_target_weight_lists_are_separate': True,
    'original_waist_normalizer_J': 268435456,
    'proposal_inverse': 'midpoints of Arb inverse of the entire signed trial midpoint matrix',
    'original_nodal_QR_calls': 0, 'old_completed_targets_recomputed': 0,
    'old_TC_derivative_arrays_recomputed': 0,
    'necessary_TC_trial_value_QR_rematerializations': 1,
    'new_arrays_published': 0,
    'maximum_scientific_seconds': 18000,
}
RUNTIME = {'python': '3.12.14', 'packages': {'numpy': '2.3.5', 'python-flint': '0.9.0'}}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(',', ':'),
                       ensure_ascii=False, allow_nan=False)+'\n').encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def parse(raw):
    return json.loads(raw, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def atomic(path, raw):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+'.candidate')
    with temporary.open('wb') as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    require(temporary.read_bytes() == raw, 'whole candidate bytes read back')
    temporary.replace(path)
    require(path.read_bytes() == raw, 'whole formal bytes read back')


def load(path, label):
    spec = importlib.util.spec_from_file_location(label, path)
    require(spec is not None and spec.loader is not None, 'whole pinned source')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def metadata(input_root, manifest_raw, manifest_sha):
    """All completed small actual inputs, before even necessary rematerialization."""
    root = Path(input_root)
    require(0 < len(manifest_raw) < 100000 and sha(manifest_raw) == manifest_sha,
            'one entire concrete SC actual-input manifest')
    manifest = parse(manifest_raw)
    require(manifest['kind'] == MANIFEST_KIND and manifest['scientific_kind'] == KIND
            and manifest['repository'] == REPO and manifest['stage'] == STAGE
            and manifest['parameters'] == PARAMETERS and manifest['runtime'] == RUNTIME
            and manifest['target_order'] == TARGETS,
            'one complete original-space SC scientific definition')
    specs = {item['role']: item for item in manifest['files']}
    require(len(specs) == len(manifest['files'])
            and specs['science']['path'] == SOURCE_PATH
            and specs['worker']['path'] == WORKER_PATH
            and specs['generator']['path'] == GENERATOR_PATH,
            'unique exact actual owner/worker/generator roles')
    contents = {}
    for role, item in specs.items():
        require(item['path'].startswith(TOPIC+'/')
                and all(part not in ('', '.', '..') for part in item['path'].split('/')),
                'one complete safe topic input path')
        path = root/item['path']
        raw = path.read_bytes()
        require(0 < len(raw) < 100000 and len(raw) == item['bytes']
                and sha(raw) == item['sha256']
                and hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
                    == item['git_blob_sha'], 'the entire current small input: '+role)
        raw.decode('utf-8')
        if item['path'].endswith('.py'):
            ast.parse(raw, filename=item['path'])
        contents[role] = raw
    require(sha(Path(__file__).read_bytes()) == specs['science']['sha256'],
            'the actual source is the exact pinned complete source')
    admission = load(root/specs['input_admission']['path'], '_SC_complete_actual_admission')
    tc_manifest = parse(contents['TC_manifest'])
    tc_specs = {item['path']: item for item in tc_manifest['files']+tc_manifest['historical_inputs']}
    tc_owner_path = tc_manifest['roles']['owner']
    require(sha((root/tc_owner_path).read_bytes()) == tc_specs[tc_owner_path]['sha256'],
            'the exact original TC owner used only for its metadata validators')
    tc_owner = load(root/tc_owner_path, '_SC_original_TC_owner_metadata')
    tc = admission.admit_complete_TC(contents, specs, tc_owner)
    reference = load(root/specs['positive_metadata_reference']['path'], '_SC_original_positive_reference')
    family = tc['state']['input_identity']['same_selected_family']
    require(family['continuous_centre_definition_sha256'] == reference.CENTRE
            and family['continuous_response_definition_sha256'] == reference.DIRECTION
            and family['fixed_current_eta'] == 'eta_0'
            and tc_manifest['parameters']['root_interval'] == reference.ROOT_INTERVAL,
            'the same original positive/negative repaired family and exact true root')
    port_math = load(root/specs['positive_port_math']['path'], '_SC_original_positive_port_units')
    positive = admission.admit_positive_chain(contents, specs, reference.FIXED_REFERENCE_IDENTITY, port_math)
    jc_owner = load(root/specs['JC_definition_source']['path'], '_SC_original_JC_metadata_only')
    require(sha(contents['JC_definition_source']) == next(
        item['sha256'] for item in parse(contents['JC_manifest'])['files'] if item['role'] == 'science'),
        'the complete actual JC numerical definition, never executed again')
    rw_sha = tc_specs[tc_manifest['roles']['RW_manifest']]['sha256']
    jc = admission.admit_JC(contents, specs, jc_owner,
                            family, rw_sha)
    bh = admission.admit_WX(contents['WX_execution'], specs['WX_execution'],
                            tc_manifest['parameters']['root_interval'])
    require(not any(name in sys.modules for name in ('numpy', 'flint', 'scipy')),
            'all actual predecessor admission precedes numerical imports')
    return {'manifest': manifest, 'specs': specs, 'contents': contents,
            'TC': tc, 'TC_owner': tc_owner, 'TC_specs': tc_specs,
            'positive': positive, 'JC': jc, 'BH_record': bh}


def preflight(args):
    root = Path(args.input_root)
    data = metadata(root, Path(args.manifest).read_bytes(), args.manifest_sha)
    spec = data['specs']['TC_manifest']
    tc_args = SimpleNamespace(repo=str(root), manifest=str(root/spec['path']),
                              manifest_sha=spec['sha256'], input_root=str(root),
                              rows_index=args.rows_index)
    admitted = data['TC_owner'].preflight(tc_args)
    require(admitted[-1] == data['TC']['state']['input_identity'],
            'the entire original TC input preflight is unchanged')
    prior = admitted[4]
    jc = data['JC']['actual']
    original_w = prior['RW']['W']
    records = {'EH': original_w['selected']['physical_true_conjugacy_minus_G_norm'],
               'G0': original_w['exact_G_periodic_norm'],
               'G1': original_w['exact_G_derivative_norm'],
               'H1': original_w['selected']['physical_true_conjugacy_derivative_Astrip_upper']}
    require(jc['copied_prior_scalar_records'] == records
            and jc['whole_completed_inputs']['W_native']['sha256']
                == admitted[1]['W_native']['sha256'],
            'the JC bound uses the exact same entire original W, not inferred row errors')
    data['admitted_TC'] = admitted
    data['receiver_records'] = {
        'CR': prior['NW']['gains']['root_or_affine_jump_to_waist_density_gain'],
        'CO': prior['NW']['gains']['ordinary_root_window_source_to_waist_density_gain'],
        'C2': prior['NW']['gains']['strict_L2_Hminus1_source_to_waist_density_gain'],
        'KW': prior['RW']['fixed']['same_inverse_two_window_bounds']['L2'],
        'BH': data['BH_record'],
    }
    data['preflight_receipt'] = {
        'whole_completed_positive_records': [58, 224, 32],
        'whole_TC_targets': list(data['TC_owner'].TARGETS),
        'whole_original_RW_rows': 96, 'whole_actual_JC_records': 7,
        'same_original_TC_input_identity': admitted[-1],
        'old_completed_targets_recomputed': 0,
        'full_physical_mean_phase_nu_Schur_claimed': False,
    }
    return data


def validate_result(document, name, manifest_sha, input_identity):
    require(document['kind'] == KIND and document['complete'] is True
            and document['manifest_sha256'] == manifest_sha
            and document['whole_input_identity'] == input_identity
            and document['old_completed_targets_recomputed'] == 0
            and document['full_mean_phase_nu_Schur_proved'] is False
            and document['topic_completion_proved'] is False,
            'one complete original-space new SC natural object')
    if name == 'columns':
        require(document['target'] == TARGETS[0]
                and document['true_full_waist_column_errors_proved'] is True
                and set(document['complete_column_error_records'])
                    == {'column_%03d'%j for j in range(1, 97)}
                and document['independent_density_means'] == 2,
                'all96 true PDE waist-column error bounds')
        require(set(document['complete_root_error_records'])
                    == {'column_%03d'%j for j in range(1, 97)}
                and all(set(row) == set(ROOT_FIELDS)
                        and all(isinstance(row[key], dict)
                                and set(row[key]) == {'ball'}
                                and isinstance(row[key]['ball'], str) for key in ROOT_FIELDS)
                        for row in document['complete_root_error_records'].values()),
                'all96 complete original low/mean, high/mixed and physical root bounds')
        receipt = document['passive_root_record_identity']
        require(receipt['kind'] == 'SC_same_single_computed_root96_records_v1'
                and receipt['complete_columns'] == 96
                and receipt['whole_original_P224_actual_sha256'] == input_identity['P224_actual_sha256']
                and receipt['whole_original_TC_positive_sha256'] == input_identity['TC_positive_sha256']
                and receipt['whole_original_TC_negative_sha256'] == input_identity['TC_negative_sha256']
                and len(receipt['whole_original_joint_math_sha256']) == 64
                and receipt['original_received_gains'] == document['original_received_gains']
                and receipt['same_single_complete_TC_column_errors_call'] is True
                and receipt['root_formula'] == 'sqrt(d_j^2+z_j^2)'
                and receipt['complete_nonzero_P224_source_indices'] == [1, 2, 7]
                and receipt['additional_scientific_calls'] == 0
                and receipt['new_natural_targets'] == 0,
                'passive full root records preserve the same complete receiver and producer identity')
    else:
        require(name in ('physical_primitive96', 'declared_incoming_cosine96')
                and document['receiver'] == name
                and document['target'] == TARGETS[1 if name == 'physical_primitive96' else 2]
                and document['complete_rows'] == document['complete_columns'] == 96
                and document['true_signed_entry_enclosures_proved'] is True
                and document['full_signed_entry_count'] == 9216,
                'the entire declared true signed96 matrix, never a principal subblock')
        require(document['finite_inverse_proved'] in (True, False),
                'an explicit actual true/false finite inverse outcome')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('input-root', 'manifest', 'manifest-sha', 'rows-index', 'out', 'private', 'checkout'):
        parser.add_argument('--'+name, required=True)
    parser.add_argument('--preflight-only', action='store_true')
    args = parser.parse_args()
    require(os.environ.get('GITHUB_ACTIONS') == 'true'
            and os.environ.get('GITHUB_REPOSITORY') == REPO
            and os.environ.get('GITHUB_RUN_ATTEMPT') == '1',
            'actual SC arithmetic only in the authorized public first-attempt job')
    data = preflight(args)
    if args.preflight_only:
        print(canonical(data['preflight_receipt']).decode(), end='')
        return 0
    root, out, private = Path(args.input_root), Path(args.out), Path(args.private)
    out.mkdir(parents=True, exist_ok=True)
    private.mkdir(parents=True, exist_ok=True)
    require(not any((out/name).exists() for name in FILES.values()),
            'never overwrite a previously completed or failed SC outcome')
    manifest, specs = data['manifest'], data['specs']
    began = time.monotonic()
    input_identity = {
        'TC_state_sha256': specs['TC_state']['sha256'],
        'TC_execution_sha256': specs['TC_execution']['sha256'],
        'TC_matrix_sha256': specs['TC_matrix']['sha256'],
        'TC_negative_sha256': specs['TC_negative']['sha256'],
        'TC_positive_sha256': specs['TC_positive']['sha256'],
        'P224_actual_sha256': specs['ports_actual']['sha256'],
        'whole_gate58_actual_sha256': specs['gate_actual']['sha256'],
        'whole_WPN32_actual_sha256': specs['wpn_actual']['sha256'],
        'whole_JC_actual_sha256': specs['JC_actual']['sha256'],
        'whole_RW_actual_sha256': data['admitted_TC'][3].PRIOR_SHA['RW_actual'],
        'same_selected_family': data['TC']['state']['input_identity']['same_selected_family'],
    }
    state = {'kind': KIND, 'complete': False, 'actual_returncode': None, 'failure': None,
             'run_id': os.environ['GITHUB_RUN_ID'], 'run_attempt': '1',
             'manifest_sha256': args.manifest_sha, 'actual_checkout_commit': args.checkout,
             'parameters': PARAMETERS, 'whole_input_identity': input_identity,
             'preflight': data['preflight_receipt'], 'completed_targets': [],
             'stage': 'whole_actual_predecessors_admitted', 'progress': {},
             'natural_object_receipts': {}, 'necessary_carrier_restoration': None,
             'old_completed_targets_recomputed': 0, 'new_arrays_published': 0,
             'full_mean_phase_nu_Schur_proved': False, 'topic_completion_proved': False,
             'runtime': None, 'wall_seconds': 0.0}

    def save_state():
        state['wall_seconds'] = time.monotonic()-began
        require(state['wall_seconds'] <= PARAMETERS['maximum_scientific_seconds'],
                'actual SC budget reached; whole completed natural objects retained')
        raw = canonical(state)
        require(len(raw) < 45000, 'whole small SC state')
        atomic(out/FILES['state'], raw)

    def progress(name, record):
        state['stage'], state['progress'][name] = name, record
        save_state()
        print(canonical({'stage': name, **record}).decode(), end='', flush=True)

    def common(target):
        return {'kind': KIND, 'complete': True, 'target': target,
                'manifest_sha256': args.manifest_sha, 'whole_input_identity': input_identity,
                'old_completed_targets_recomputed': 0,
                'full_mean_phase_nu_Schur_proved': False, 'topic_completion_proved': False}

    save_state()
    try:
        import numpy as np
        import flint
        from importlib.metadata import version
        runtime = {'python': platform.python_version(),
                   'packages': {name: version(name) for name in RUNTIME['packages']}}
        require(runtime == RUNTIME and sys.byteorder == 'little' and platform.machine() == 'x86_64',
                'the entire original TC and new directed runtime')
        flint.ctx.prec = PARAMETERS['arithmetic_bits']
        arb, arb_mat, fmpq = flint.arb, flint.arb_mat, flint.fmpq
        state['runtime'] = runtime
        joint_math = load(root/specs['joint_math']['path'], '_SC_JF_pure_math')

        class API:
            zero, one = arb(0), arb(1)
            @staticmethod
            def rational(n, d=1): return arb(fmpq(n, d))
            @staticmethod
            def lower(value): return value.lower()
            @staticmethod
            def sqrt(value): return value.sqrt()
            @staticmethod
            def magnitude(value): return abs(value).upper()

        api = API()

        def old_upper(record):
            require(isinstance(record, dict) and isinstance(record.get('ball'), str),
                    'whole original saved scalar ball')
            value = (arb(record['lower']).lower().union(arb(record['upper']).upper())
                     if 'lower' in record and 'upper' in record else arb(record['ball']))
            require(value.is_finite() and value.lower() >= 0, 'complete nonnegative original bound')
            return value.upper()

        def new_record(value):
            point = value.upper()
            require(point.is_finite() and point >= 0, 'finite new directed upper')
            record = {'ball': point.str(PARAMETERS['public_digits'])}
            require(arb(record['ball']).contains(point), 'whole displayed upper encloses its value')
            return record, point

        def save_result(name, document, originals):
            validate_result(document, name, args.manifest_sha, input_identity)
            raw = canonical(document)
            require(0 < len(raw) < 95000, 'one complete small SC natural conclusion')
            if name == 'columns':
                require(len(raw) <= MAXIMUM_COLUMNS_BYTES
                        == manifest['operation']['maximum_columns_bytes'],
                        'one whole waist/root96 conclusion within the actual report budget')
            atomic(out/FILES[name], raw)
            saved = parse((out/FILES[name]).read_bytes())
            require(saved == document, 'whole SC natural result readback')
            for path, point in originals:
                record = saved
                for key in path:
                    record = record[key]
                require(arb(record['ball']).contains(point), 'every saved new bound includes its directed upper')
            receipt = {'file': FILES[name], 'bytes': len(raw), 'sha256': sha(raw)}
            state['natural_object_receipts'][name] = receipt
            state['completed_targets'].append(document['target'])
            state['stage'] = 'complete_new_natural_object_saved'
            save_state()
            return saved

        gains = {name: old_upper(record) for name, record in data['receiver_records'].items()}
        p224 = data['positive']['ports']['actual']['new_records']
        full_table = {(k, code): old_upper(p224['port_%02d_%s_upper'%(k, code)])
                      for k in range(14) for code in joint_math.OUTPUT_CODES}
        residual_columns = []
        for j in range(1, 97):
            key = 'column_%03d'%j
            records = {**data['TC']['positive']['complete_source_records'][key],
                       **data['TC']['negative']['complete_source_records'][key]}
            residual_columns.append({name: old_upper(record) for name, record in records.items()})
        computed = joint_math.complete_TC_column_errors(
            api, full_table, residual_columns, gains['CR'], gains['CO'], gains['C2'])
        column_doc = common(TARGETS[0])
        column_doc.update(true_full_waist_column_errors_proved=True, independent_density_means=2,
                          complete_column_error_records={}, complete_root_error_records={},
                          exact_positive_nonzero_ports=[1, 2, 7],
                          full224_admitted=True, original_received_gains=data['receiver_records'])
        column_doc['passive_root_record_identity'] = {
            'kind': 'SC_same_single_computed_root96_records_v1', 'complete_columns': 96,
            'whole_original_P224_actual_sha256': input_identity['P224_actual_sha256'],
            'whole_original_TC_positive_sha256': input_identity['TC_positive_sha256'],
            'whole_original_TC_negative_sha256': input_identity['TC_negative_sha256'],
            'whole_original_joint_math_sha256': specs['joint_math']['sha256'],
            'original_received_gains': copy.deepcopy(data['receiver_records']),
            'same_single_complete_TC_column_errors_call': True,
            'root_formula': 'sqrt(d_j^2+z_j^2)',
            'complete_nonzero_P224_source_indices': [1, 2, 7],
            'additional_scientific_calls': 0, 'new_natural_targets': 0,
        }
        originals = []
        for row in computed:
            name = 'column_%03d'%row['column']
            record, point = new_record(row['complete_waist_column_error_upper'])
            column_doc['complete_column_error_records'][name] = record
            originals.append((('complete_column_error_records', name), point))
            # These are already returned by the SAME pure call above.
            # Save every original root component without another evaluation.
            column_doc['complete_root_error_records'][name] = {}
            for key in ROOT_FIELDS:
                record, point = new_record(row[key])
                column_doc['complete_root_error_records'][name][key] = record
                originals.append((('complete_root_error_records', name, key), point))
        saved_columns = save_result('columns', column_doc, originals)
        errors = [old_upper(saved_columns['complete_column_error_records']['column_%03d'%j])
                  for j in range(1, 97)]
        waist_norms = [old_upper(data['TC']['matrix']['complete_waist_trial_norms']['column_%03d'%j])
                       for j in range(1, 97)]
        original_rw = data['admitted_TC'][4]['RW_actual']
        row_errors = [old_upper(original_rw['new_records']['row_%03d'%j]['compound_error'])
                      for j in range(1, 97)]
        jc_error = old_upper(data['JC']['joint_row_error_record'])
        source_weights = [arb(1) for _ in range(96)]
        target_weights = [arb(1) for _ in range(96)]
        carrier = load(root/specs['carrier_restore']['path'], '_SC_necessary_original_carriers')
        matrices, restored = carrier.restore(np, flint, root, private, data['admitted_TC'],
                                              data['TC']['state'], data['TC']['matrix'], progress)
        state['necessary_carrier_restoration'] = restored
        save_state()
        for index, name in enumerate(('physical_primitive96', 'declared_incoming_cosine96'), 1):
            progress('new_complete_true_matrix_gate', {'receiver': name, 'complete_rows': 96, 'complete_columns': 96})
            trial = matrices[name]
            old_joint = joint_math.joint_TC_matrix_error(
                api, errors, waist_norms, row_errors, source_weights,
                gains['BH'], gains['KW'], name)
            kappa = arb(1) if name == 'declared_incoming_cosine96' else (arb(1)/2).sqrt().upper()
            new_joint = (old_joint['joint_column_error_contribution_upper']
                         +kappa*jc_error*old_joint['source_weighted_trial_column_operator_upper']).upper()
            candidates = {'complete_RW_Hilbert_Schmidt_candidate': old_joint['complete_source_weighted_matrix_error_upper'],
                          'complete_actual_JC_joint_composition_candidate': new_joint}
            saved_candidates = {key: new_record(value)[0] for key, value in candidates.items()}
            atomic(private/(name+'-complete-joint-candidates.json'), canonical(saved_candidates))
            read_candidates = parse((private/(name+'-complete-joint-candidates.json')).read_bytes())
            require(read_candidates == saved_candidates, 'all whole operator candidates saved and read back')
            selected = min(candidates, key=lambda key: old_upper(read_candidates[key]))
            xi = old_upper(read_candidates[selected])
            # The entire entrywise enclosure remains available as a private
            # certified matrix; the joint gate uses its sharper operator proof.
            gamma = old_joint['complete_true_receiver_upper']
            true_entries = []
            for i in range(96):
                er = row_errors[i] if row_errors[i] <= jc_error else jc_error
                row = []
                for j in range(96):
                    radius = (gamma*errors[j]+kappa*er*waist_norms[j]).upper()
                    row.append(trial[i][j]+(-radius).union(radius))
                true_entries.append(row)
            actual_doc = {'kind': 'SC_complete_true_signed_entry_enclosure96_v1',
                          'receiver': name, 'whole_input_identity': input_identity,
                          'rows': 96, 'columns': 96,
                          'all_signed_entry_balls': [[value.str(PARAMETERS['private_digits'])
                                                      for value in row] for row in true_entries]}
            actual_raw = canonical(actual_doc)
            actual_path = private/(name+'-true-entries.json')
            atomic(actual_path, actual_raw)
            read_entries = parse(actual_path.read_bytes())['all_signed_entry_balls']
            require(all(arb(value).contains(original) for row, oldrow in zip(read_entries, true_entries)
                        for value, original in zip(row, oldrow)), 'all9216 certified true entries read back')
            document = common(TARGETS[index])
            document.update(receiver=name, complete_rows=96, complete_columns=96,
                            full_signed_entry_count=9216, true_signed_entry_enclosures_proved=True,
                            finite_inverse_proved=False, source_weights=['1']*96, target_weights=['1']*96,
                            same_original_signed_trial_carrier=restored['whole_original_matrix_receipts'][name],
                            complete_true_entry_carrier={'bytes': len(actual_raw), 'sha256': sha(actual_raw)},
                            complete_joint_candidates=read_candidates, selected_complete_joint_candidate=selected,
                            true_matrix_error_formula='JF.11 with whole RW or actual JC candidate',
                            new_bounds={}, trial_inverse_carrier=None, inverse_proposal_failure=None)
            originals = []
            try:
                midpoint_inverse = arb_mat([[value.mid() for value in row] for row in trial]).inv()
                inverse = [[midpoint_inverse[i, j].mid() for j in range(96)] for i in range(96)]
                require(all(value.is_finite() and value.lower() == value.upper()
                            for row in inverse for value in row), 'one entire exact dyadic inverse proposal')
            except (ValueError, ZeroDivisionError, ArithmeticError) as error:
                document['inverse_proposal_failure'] = {'type': type(error).__name__, 'message': str(error)[:1000]}
                document['gate_status'] = 'complete_true_matrix_enclosed_inverse_proposal_unavailable'
                save_result(name, document, originals)
                continue
            inverse_doc = {'kind': 'SC_complete_exact_dyadic_trial_inverse96_v1',
                           'receiver': name, 'rows': 96, 'columns': 96,
                           'all_mantissa_exponent_pairs': [[list(map(int, value.man_exp())) for value in row]
                                                           for row in inverse]}
            inverse_raw = canonical(inverse_doc)
            inverse_path = private/(name+'-exact-inverse.json')
            atomic(inverse_path, inverse_raw)
            pairs = parse(inverse_path.read_bytes())['all_mantissa_exponent_pairs']
            inverse_read = [[arb(mantissa)*(arb(2)**exponent) for mantissa, exponent in row] for row in pairs]
            require(all(value == old for row, oldrow in zip(inverse_read, inverse)
                        for value, old in zip(row, oldrow)), 'every exact dyadic inverse entry read back')
            document['trial_inverse_carrier'] = {'bytes': len(inverse_raw), 'sha256': sha(inverse_raw)}
            gate = joint_math.complete_joint_weighted_inverse_gate(
                api, trial, inverse_read, source_weights, target_weights, xi)
            residual = gate.pop('complete_signed_trial_residual_matrix')
            residual_doc = {'kind': 'SC_complete_signed_trial_preconditioned_residual96_v1',
                            'receiver': name, 'rows': 96, 'columns': 96,
                            'all_signed_entry_balls': [[value.str(PARAMETERS['private_digits']) for value in row]
                                                      for row in residual]}
            residual_raw = canonical(residual_doc)
            atomic(private/(name+'-signed-residual.json'), residual_raw)
            document['complete_signed_preconditioned_residual_carrier'] = {
                'bytes': len(residual_raw), 'sha256': sha(residual_raw)}
            primitive_names = ('trial_residual_infinity_upper', 'trial_residual_one_upper',
                'trial_residual_two_upper', 'preconditioned_target_infinity_upper',
                'preconditioned_target_one_upper', 'preconditioned_target_two_upper',
                'trial_inverse_infinity_upper', 'trial_inverse_one_upper', 'trial_inverse_two_upper')
            # Persist the WHOLE norm list before forming dependent perturbation,
            # residual and inverse bounds.  The pure helper's unpersisted strict
            # result is not used as a certificate or a downstream input.
            saved_bound_path = private/(name+'-complete-gate-bounds.json')
            def save_bounds():
                raw = canonical(document['new_bounds'])
                atomic(saved_bound_path, raw)
                saved = parse(saved_bound_path.read_bytes())
                require(saved == document['new_bounds'], 'every complete dependent gate bound read back')
                return saved
            for key in primitive_names:
                record, point = new_record(gate[key])
                document['new_bounds'][key] = record
                originals.append((('new_bounds', key), point))
            saved_bounds = save_bounds()
            perturbation = (old_upper(saved_bounds['preconditioned_target_two_upper'])*xi).upper()
            record, point = new_record(perturbation)
            document['new_bounds']['preconditioned_joint_error_upper'] = record
            originals.append((('new_bounds', 'preconditioned_joint_error_upper'), point))
            saved_bounds = save_bounds()
            residual_bound = (old_upper(saved_bounds['trial_residual_two_upper'])
                              +old_upper(saved_bounds['preconditioned_joint_error_upper'])).upper()
            record, point = new_record(residual_bound)
            document['new_bounds']['complete_actual_residual_two_upper'] = record
            originals.append((('new_bounds', 'complete_actual_residual_two_upper'), point))
            saved_bounds = save_bounds()
            # The strict claim uses the saved output upper, never its midpoint.
            rho = old_upper(saved_bounds['complete_actual_residual_two_upper'])
            passed = bool(rho < 1)
            document['finite_inverse_proved'] = passed
            document['gate_status'] = 'strict_complete_matrix_inverse_proved' if passed else 'complete_sufficient_matrix_gate_failed'
            if passed:
                gap = (arb(1)-rho).lower()
                require(gap > 0, 'strict gap from the saved whole residual upper')
                bound = (old_upper(saved_bounds['trial_inverse_two_upper'])/gap).upper()
                record, point = new_record(bound)
                document['new_bounds']['weighted_actual_inverse_two_upper'] = record
                originals.append((('new_bounds', 'weighted_actual_inverse_two_upper'), point))
                save_bounds()
            document['all_dependent_gate_bounds_use_formal_readback_uppers'] = True
            save_result(name, document, originals)
        require(state['completed_targets'] == TARGETS, 'all three whole new SC natural targets')
        state['complete'], state['actual_returncode'] = True, 0
        state['stage'] = 'complete_actual_columns_and_all_declared_matrix_gate_outcomes'
        save_state()
        return 0
    except BaseException as error:
        state['complete'], state['actual_returncode'] = False, 1
        state['failure'] = {'type': type(error).__name__, 'message': str(error)[:2000],
                            'traceback': traceback.format_exc()[-7000:]}
        state['stage'] = 'failed_with_all_completed_natural_objects_retained'
        state['wall_seconds'] = time.monotonic()-began
        atomic(out/FILES['state'], canonical(state))
        print(traceback.format_exc(), flush=True)
        return 1


if __name__ == '__main__':
    sys.exit(main())
