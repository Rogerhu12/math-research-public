#!/usr/bin/env python3
"""Source-bound standard-library public runner for the original p41 single Z.

This module never imports a mathematical core or the ball arithmetic helper.
Its local inspection functions check original bytes, schemas and source links.
"""
import argparse
import datetime as dt
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import signal
import subprocess
import sys
import tarfile
import traceback

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/'topics/serre-uniformity'
REQUEST = TOPIC/'notes/R858-original-p41-single-Z-public-request.json'
REPOSITORY = 'Rogerhu12/math-research-public'
RESULT = 'R858-original-p41-single-Z-and-elliptic-rows'
FINAL = 'p41-original-p41-single-Z-and-elliptic-rows-certificate.json'
PREFIX = 'R858-single-Z-'
MANIFEST = 'full-outputs-manifest.json'
REFERENCE = 'full-outputs-manifest-reference.json'
INVENTORY = PREFIX+'original-source-inventory.json'
BUNDLE = PREFIX+'retained-original-inputs.tar.gz'
INPUT_RECEIPT = PREFIX+'retained-inputs-receipt.json'
CORE = 'R858_original_p41_single_Z_consumer.py'
BALL_HELPER = 'R858_original_p41_ball_arithmetic.py'
BALL_HELPER_SHA = '767b01cba9bfa966d1a545b72abe51fe0b9edc407638db5947ec5dba28637fa3'
PARENT = 'R852_public_original_one_Z_coefficients.py'
PARENT_SHA = '873097d8462f1f20d8cb05adb2e5b3261bbea44a1a58de12a05e9286970dee3c'
TRANSPORT = 'R850_public_original_rigidified_fibres.py'
TRANSPORT_SHA = 'ff318ca06e5bf2a385c866df2abb0ea102d6606eb2af2a818a0493f075b123cf'
RANGE = 'R824_public_original_global_polar_generators.py'
RANGE_SHA = 'c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c'
R854_CORE_SHA = '1feb579a88879739a250f889ab1818019acb8f1156a0e3f34d57b8524024125f'
BASE_KEYS = ('result', 'run_id', 'source_commit', 'core_sha256',
             'manifest_sha256', 'configuration_sha256')
INPUT_KEYS = ('R852_certificate', 'coefficient_program', 'exact_C_coordinates',
              'response_certificate', 'four_response_balls', 'implicit_CM', 'galois', 'tangents')
H64 = re.compile(r'[0-9a-f]{64}')
INTEGER = re.compile(r'-?(?:0|[1-9][0-9]*)')
PARENT_IO = None
IO = None

# This literal is the frozen core's mathematical identity, not a new algorithm.
STRATEGY = {'original_p': 41,
 'original_map_index': 4,
 'original_map_degree': 1206,
 'original_point': 'f4(c1), roots beta_C_x and beta_C_y; not f_R(c1)',
 'original_parameter': 'z=a-1',
 'original_differential': 'dx/(2*y)',
 'coefficient_field': 'Q41[B,s]/(original_F_B,s^2+3); B=lambda*b',
 'coefficient_order': 'B^0..B^6,s*B^0..s*B^6',
 'absolute_precision_unit': 'v_B=7*v41',
 'ramification_index': 7,
 'residue_degree': 2,
 'DAG_operation': 'prune original 839-node program at four original responses',
 'unit_chart_solve_recomputed': False,
 'exact_C_coordinates_recomputed': False,
 'whole_expression_Galois_action': True,
 'multiplication_chain': [1, 2, 4, 5, 10, 20, 21, 42],
 'addition_Z_law': 'Z(P+Q)=Z(P)+Z(Q)+original_secant(P,Q)',
 'beta_recurrence': 'beta_(a+b)=beta_a+beta_b+original_slope(aP,bP)',
 'base_Z': '(Z(42P)-beta42)/42',
 'psi42_or_psi42_derivative_computed': False,
 'formal_branch': 't=-x/y,u=t^2*x,A=b*t^6; v_B(A)>0,v_B(u-1)>0',
 'series_H': 'H_n=[A^(n-1)](9*u+4)/(u^2*(3*u-2)); u=1-delta',
 'delta_coefficients': 'delta_n=binom(3*n-2,n-1)/n in Z',
 'tail_rule': 'N>=2; (N+1)*vB(A)-vB(t)-7*ceil_log41(6*(N+1)-1)',
 'trace14': '(1+c_Bfixed)*sum_(k=0..6) sigma^k; c_Bfixed(s)=-s',
 'elliptic_row': 'c_chi*(Trace14(C_j*Z+D_j)/2)',
 'c_chi_preserved_symbolically': True,
 'Y_Picard_or_global_Hecke_correction_computed': False,
 'actual_height_computed': False,
 'auxiliary_518_balls_used_as_p41': False,
 'budget_target_precision_and_term_limit_excluded_from_mathematical_identity': True}


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def sha(path):
    answer = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(4*1024*1024), b''):
            answer.update(block)
    return answer.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == '.gz' else open)(path, 'rt', encoding='utf-8') as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+'.tmp')
    temporary.write_text(json.dumps(value, sort_keys=True, separators=(',', ':'))+'\n')
    temporary.replace(path)


def plain(value):
    result = {key: value[key] for key in ('file', 'bytes', 'sha256')}
    name = PurePosixPath(result['file'])
    assert len(name.parts) == 1 and name.name not in ('', '.', '..')
    assert '\\' not in result['file'] and not name.is_absolute()
    assert isinstance(result['bytes'], int) and result['bytes'] >= 0
    assert H64.fullmatch(result['sha256'])
    return result


def spec(path):
    path = Path(path)
    return {'file': path.name, 'bytes': path.stat().st_size, 'sha256': sha(path)}


def bound(folder, row):
    row = plain(row)
    path = Path(folder)/row['file']
    assert path.is_file() and path.stat().st_size == row['bytes'], str(path)
    assert sha(path) == row['sha256'], str(path)
    return path


def copy_bound(source, target, row):
    source, target = Path(source), Path(target)
    path = bound(source, row)
    target.mkdir(parents=True, exist_ok=True)
    destination = target/path.name
    if destination.exists():
        bound(target, row)
    else:
        temporary = destination.with_name(destination.name+'.tmp')
        shutil.copyfile(path, temporary)
        assert temporary.stat().st_size == row['bytes'] and sha(temporary) == row['sha256']
        temporary.replace(destination)
    return destination


def source_identity(source):
    return {**{key: source[key] for key in BASE_KEYS},
            'selected_files_sha256': fingerprint({name: plain(row)
                for name, row in sorted(source['files'].items())}),
            'certificate': plain(source['certificate'])}


def same_origin(a, b):
    for key in BASE_KEYS:
        assert str(a[key]) == str(b[key]), ('Original source identity', key)


def load_transport(directory=None):
    """Only the three SHA-bound, standard-library transport modules are loaded."""
    global PARENT_IO, IO
    folder = S if directory is None else Path(directory)
    for name, digest in ((PARENT, PARENT_SHA), (TRANSPORT, TRANSPORT_SHA), (RANGE, RANGE_SHA)):
        assert sha(folder/name) == digest
    entry = importlib.util.spec_from_file_location('R858_frozen_R852_source_IO', folder/PARENT)
    PARENT_IO = importlib.util.module_from_spec(entry)
    entry.loader.exec_module(PARENT_IO)
    PARENT_IO.load_parent({'source_transport_helper': TRANSPORT,
                          'source_transport_helper_sha256': TRANSPORT_SHA,
                          'io_helper_sha256': RANGE_SHA})
    IO = PARENT_IO.P.IO


def stage(folder, source, row, complete=True):
    row = plain(row)
    assert plain(source['files'][row['file']]) == row
    value = read(bound(folder, row))
    assert fingerprint(value['configuration']) == source['configuration_sha256']
    assert value['configuration']['source_sha256'] == source['core_sha256']
    if 'result' in value:
        assert value['result'] == source['result']
    if complete:
        assert value['complete'] is True
    return value


def manifest_entries(source, folder):
    files = {name: plain(row) for name, row in source['files'].items()}
    assert all(name == row['file'] for name, row in files.items())
    assert files[MANIFEST]['sha256'] == source['manifest_sha256']
    assert files[MANIFEST]['bytes'] == source['manifest_bytes']
    data = read(bound(folder, files[MANIFEST]))
    assert data['result'] == source['result']
    entries = {row['file']: plain(row) for row in data['files']}
    assert len(entries) == len(data['files']) == source['manifest_file_count']
    entries[MANIFEST] = files[MANIFEST]
    if REFERENCE in files:
        ref = read(bound(folder, files[REFERENCE]))
        assert ref['manifest_sha256'] == source['manifest_sha256']
        assert ref['manifest_bytes'] == source['manifest_bytes']
        assert ref['file_count'] == source['manifest_file_count']
        entries[REFERENCE] = files[REFERENCE]
    for name, row in files.items():
        assert entries[name] == row
    assert len(files) == source['selected_file_count']
    assert fingerprint(files) == source['selected_files_sha256']
    return entries


def review_source(label, source, folder):
    folder = Path(folder)
    manifest_entries(source, folder)
    for row in source['files'].values():
        bound(folder, row)
    cert = stage(folder, source, source['certificate'], complete=(label != 'R854'))
    run = read(folder/'run-receipt.json')
    core = read(folder/'core-receipt.json')
    public = read(folder/'public-actions-input.json')
    assert run['result'] == core['result'] == public['result'] == cert['result'] == source['result']
    assert str(run['workflow_run_id']) == str(source['run_id'])
    assert run['source_commit'] == public['source_commit'] == source['source_commit']
    assert public['source_repository'] == REPOSITORY
    assert public['job']['core_sha256'] == source['core_sha256']
    if label != 'R791':
        assert public['core_sha256'] == source['core_sha256']
    core_key = 'core_sha256' if label == 'R854' else 'source_sha256'
    assert core[core_key] == source['core_sha256']
    public_driver = 'driver_sha256' if label in ('R791', 'R854') else 'wrapper_sha256'
    assert public[public_driver] == source['wrapper_sha256']
    if label != 'R791':
        assert public['job']['wrapper_sha256'] == source['wrapper_sha256']
    assert public['root_readme_sha256'] == source['original_readme_sha256']['root']
    assert public['topic_readme_sha256'] == source['original_readme_sha256']['topic']
    assert run['process_exit_code'] in source['accepted_process_exit_codes']
    if label == 'R854':
        assert source['core_sha256'] == R854_CORE_SHA
        assert run['process_exit_code'] in (0, 125)
        assert core['exit_code'] == run['process_exit_code']
        assert core['complete'] is cert['complete']
        assert core['final_sha256'] == source['certificate']['sha256']
        assert cert['actual_original_p41_four_response_balls_certified'] is True
        assert cert['four_response_balls'] is not None
        assert cert['unit_minor_and_left_inverse_bound'] is not None
        if cert['complete']:
            assert run['complete'] is True and run['process_exit_code'] == 0
            assert core['error'] is None and run['error'] is None
        else:
            assert run['complete'] is False and run['process_exit_code'] == 125
    else:
        assert run['process_exit_code'] == 0 and run['complete'] is True and core['complete'] is True
        assert run.get('error') is None and core.get('error') is None
        assert core['certificate_sha256'] == source['certificate']['sha256']
    if 'core_receipt_sha256' in run:
        assert run['core_receipt_sha256'] == source['files']['core-receipt.json']['sha256']
    if 'configuration' in core:
        assert core['configuration'] == cert['configuration']
    if 'configuration_sha256' in core:
        assert core['configuration_sha256'] == source['configuration_sha256']
    for name in source['files']:
        if name.endswith('.json.gz'):
            stage(folder, source, source['files'][name])
    return cert


def r854_required_names(source, folder):
    """The response proof closure; no tall operator or large residue inverse."""
    folder = Path(folder)
    cert = stage(folder, source, source['certificate'], complete=False)
    response = stage(folder, source, cert['four_response_balls'])
    unit = stage(folder, source, cert['unit_minor_and_left_inverse_bound'])
    residual = stage(folder, source, response['full_original_residual_certificate'])
    names = {MANIFEST, 'run-receipt.json', 'core-receipt.json', 'public-actions-input.json',
             source['certificate']['file']}
    if REFERENCE in source['files']:
        names.add(REFERENCE)
    for row in (cert['source_audit'], cert['stage_manifest'], cert['four_response_balls'],
                cert['unit_minor_and_left_inverse_bound'], response['full_original_residual_certificate'],
                residual['residual_numerator'], residual['last_digit']):
        assert plain(source['files'][row['file']]) == plain(row)
        names.add(row['file'])
    assert unit['shape'] == [2420, 2420] and unit['original_tall_shape'] == [2560, 2420]
    assert unit['full_selected_residue_inverse_product_verified'] is True
    assert len(unit['selected_rows']) == len(set(unit['selected_rows'])) == 2420
    assert all(isinstance(x, int) and 0 <= x < 2560 for x in unit['selected_rows'])
    assert len(unit['row_transform_lower_bounds']) == 2560
    assert residual['unit_certificate'] == cert['unit_minor_and_left_inverse_bound']
    assert residual['original_rows_verified'] == 2560
    assert residual['original_L_coordinates_per_row'] == 14
    assert len(residual['residual_numerator_row_B_valuation_lower_bounds']) == 2560
    assert len(residual['full_original_residual_row_B_valuation_lower_bounds']) == 2560
    assert len(residual['original_row_block_p41_scale_exponents']) == 128
    for flag in ('exact_original_row_scales_removed_and_weightedly_restored',
                 'original_m0_twenty_by_fourteen_coordinates_exactly_zero',
                 'full_129_by_20_by_14_original_cleared_identity_used',
                 'inverse_norm_bound_used_not_residual_alone',
                 'candidate_is_a_chosen_exact_finite_polynomial_not_an_A1_acceptance'):
        assert residual[flag] is True
    assert residual['minimum_left_inverse_entry_valuation_lower_bound'] == unit['minimum_left_inverse_entry_valuation_lower_bound']
    vector = stage(folder, source, residual['residual_numerator'])
    assert vector['unit_certificate'] == residual['unit_certificate']
    assert vector['last_digit'] == residual['last_digit']
    assert vector['candidate_solution_denominator_B_power'] == residual['candidate_solution_denominator_B_power']
    assert vector['matrix']['shape'] == [2560, 1] and vector['matrix']['p'] == 41
    assert len(vector['matrix']['coefficients']) == 14
    assert all(len(block) == 2560 and all(len(row) == 1 for row in block)
               for block in vector['matrix']['coefficients'])
    assert response['labels'] == ['A0', 'A1', 'B0', 'B1']
    assert response['numerators']['shape'] == [4, 1] and response['numerators']['p'] == 41
    assert len(response['numerators']['coefficients']) == 14
    assert all(len(block) == 4 and all(len(row) == 1 for row in block)
               for block in response['numerators']['coefficients'])
    assert response['absolute_B_precision'] == cert['actual_response_absolute_B_precision']
    assert response['actual_original_p41_four_response_balls_certified'] is True
    assert response['original_CM_scale_applied_again'] is False
    assert response['B_response_free1186_constant_preserved'] is True
    for flag in ('expanded_exact_L_coordinates_accepted', 'A1_exact_zero_proved',
                 'actual_Z_computed', 'actual_height_computed', 'auxiliary_prime_ball_used_as_p41'):
        assert cert[flag] is False
    return names


def fetch_source(label, source, retained):
    folder = Path(retained)/label
    folder.mkdir(parents=True, exist_ok=True)
    missing = []
    for name, row in source['files'].items():
        if (folder/name).exists():
            bound(folder, row)
        else:
            missing.append(name)
    if not missing:
        review_source(label, source, folder)
        return {'already_present_original_bytes_verified': True, 'network_downloaded': False}
    archive = IO.Archive(source, Path(retained).parent/('download-R858-'+label), whole=False)
    try:
        archive.extract_bound(MANIFEST, source['manifest_sha256'], folder/MANIFEST, source['manifest_bytes'])
        if REFERENCE in source['files']:
            row = source['files'][REFERENCE]
            archive.extract_bound(REFERENCE, row['sha256'], folder/REFERENCE, row['bytes'])
        entries = manifest_entries(source, folder)
        assert set(archive.by_name) == set(entries) | {REFERENCE}
        for name, row in entries.items():
            assert len(archive.by_name[name]) == 1 and archive.by_name[name][0].file_size == row['bytes']
        archive.extract_many([(name, source['files'][name]['sha256'], folder/name,
                               source['files'][name]['bytes']) for name in missing])
        review_source(label, source, folder)
        return archive.receipt()
    finally:
        archive.close()


def review_known_sources(item, retained):
    """Pure IO; also callable before the future R854 producer is available."""
    retained = Path(retained)
    source = item['sources']['R852']
    cert = review_source('R852', source, retained/'R852')
    oldjob = read(retained/'R852'/'public-actions-input.json')['job']
    # All three are already selected and bound.  The frozen function cannot
    # take its fresh-download branch and request the old R847 artifact.
    for name in (PARENT_IO.INVENTORY, PARENT_IO.BUNDLE, PARENT_IO.INPUT_RECEIPT):
        bound(retained/'R852', source['files'][name])
    nested, groups, old_receipt = PARENT_IO.sources(oldjob, retained/'R852')
    assert sum(group['selected_file_count'] for group in groups.values()) == 270
    for label in ('CM', 'R791'):
        same_origin(item['sources'][label], groups[label])
        same_origin(item['sources'][label], cert['configuration']['source_identities'][label])
        for name, row in item['sources'][label]['files'].items():
            assert plain(groups[label]['files'][name]) == plain(row)
            copy_bound(Path(nested)/label, retained/label, row)
        review_source(label, item['sources'][label], retained/label)
    program = stage(retained/'R852', source, cert['coefficient_program'])
    coordinates = stage(retained/'R852', source, cert['five_exact_C_coordinates'])
    assert program['node_count'] == len(program['nodes']) == 839
    assert program['imported_original_node_count'] == 733
    assert program['original_sigma_applies_to_entire_unit_chart'] is True
    assert program['original_T7_phase_preserved'] is True
    assert coordinates['coefficient_program'] == cert['coefficient_program']
    assert coordinates['five_C_coefficients_nonzero'] is True
    assert coordinates['five_C_coefficients_Q_linearly_independent'] is True
    assert len(coordinates['five_coefficients']) == 5
    return {'R852_source_identity': source_identity(source),
            'original_direct_carrier_members': 9, 'original_nested_source_members': 270,
            'original_R852_carrier': plain(old_receipt['source_bundle']),
            'all_old_source_bytes_and_parent_child_identities_verified': True,
            'old_numeric_arithmetic_executed': False,
            'no_old_R847_artifact_downloaded': True}


def review_all_sources(item, retained):
    report = review_known_sources(item, retained)
    source = item['sources']['R854']
    cert = review_source('R854', source, Path(retained)/'R854')
    assert set(source['files']) == r854_required_names(source, Path(retained)/'R854')
    same_origin(cert['configuration']['source_identities']['CM'], item['sources']['CM'])
    for key, row in item['inputs'].items():
        assert key in INPUT_KEYS
        group = row['source_group']
        assert plain(item['sources'][group]['files'][row['file']]) == plain(row)
        stage(Path(retained)/group, item['sources'][group], row, complete=(key != 'response_certificate'))
    assert plain(item['inputs']['response_certificate']) == plain(source['certificate'])
    assert plain(item['inputs']['four_response_balls']) == cert['four_response_balls']
    implicit = stage(Path(retained)/'CM', item['sources']['CM'], item['inputs']['implicit_CM'])
    response = stage(Path(retained)/'R854', source, cert['four_response_balls'])
    assert response['exact_functionals'] == implicit['linear_responses']
    assert cert['configuration']['field'] == implicit['original_field']
    report['actual_original_p41_response_B_precision'] = response['absolute_B_precision']
    report['R854_source_identity'] = source_identity(source)
    report['R854_declared_complete'] = cert['complete']
    report['R854_actual_ball_certificate_not_requested_threshold_used'] = True
    report['large_original_operator_or_residue_inverse_downloaded'] = False
    return report


def expected_tag(item, retained):
    implicit = stage(Path(retained)/'CM', item['sources']['CM'], item['inputs']['implicit_CM'])
    return {'result': RESULT, 'source_sha256': item['core_sha256'], 'p': 41,
            'ball_helper_sha256': item['ball_helper_sha256'], 'proofs': item['proofs'],
            'source_identities': {label: source_identity(value)
                                  for label, value in sorted(item['sources'].items())},
            'inputs': {key: {'source_group': row['source_group'], **plain(row)}
                       for key, row in sorted(item['inputs'].items())},
            'field': implicit['original_field'],
            'exact_leaf_B_precision': int(item.get('exact_leaf_B_precision', 256)),
            'series_block_size': int(item.get('series_block_size', 16)), 'strategy': STRATEGY}


def pack_inputs(retained, sources, target):
    retained, target = Path(retained), Path(target)
    temporary = target.with_name(target.name+'.tmp')
    with temporary.open('wb') as raw:
        with gzip.GzipFile(fileobj=raw, mode='wb', mtime=0, filename='', compresslevel=0) as zipped:
            with tarfile.open(fileobj=zipped, mode='w|') as tar:
                for label, source in sorted(sources.items()):
                    for name, row in sorted(source['files'].items()):
                        path = bound(retained/label, row)
                        info = tar.gettarinfo(str(path), arcname=label+'/'+name)
                        info.uid = info.gid = info.mtime = 0
                        info.uname = info.gname = ''
                        with path.open('rb') as stream:
                            tar.addfile(info, stream)
    temporary.replace(target)


def unpack_inputs(bundle, retained, sources):
    wanted = {(label, name): plain(row) for label, source in sources.items()
              for name, row in source['files'].items()}
    seen = set()
    with tarfile.open(bundle, 'r|gz') as tar:
        for member in tar:
            if member.isdir():
                continue
            name = PurePosixPath(member.name)
            assert member.isfile() and not name.is_absolute() and len(name.parts) == 2
            assert '..' not in name.parts and '\\' not in member.name
            key = tuple(name.parts)
            assert key in wanted and key not in seen
            row = wanted[key]
            assert member.size == row['bytes']
            target = Path(retained)/key[0]/key[1]
            target.parent.mkdir(parents=True, exist_ok=True)
            temporary = target.with_name(target.name+'.tmp')
            digest, count = hashlib.sha256(), 0
            with tar.extractfile(member) as inp:
                if target.exists():
                    bound(target.parent, row)
                    for block in iter(lambda: inp.read(4*1024*1024), b''):
                        digest.update(block); count += len(block)
                else:
                    with temporary.open('wb') as out:
                        for block in iter(lambda: inp.read(4*1024*1024), b''):
                            digest.update(block); count += len(block); out.write(block)
            assert count == row['bytes'] and digest.hexdigest() == row['sha256']
            if temporary.exists():
                temporary.replace(target)
            seen.add(key)
    assert seen == set(wanted)
    return len(seen)


def sources(item, out):
    out = Path(out)
    retained = out.parent/'R858-retained'
    retained.mkdir(parents=True, exist_ok=True)
    present = [(out/name).exists() for name in (INVENTORY, BUNDLE, INPUT_RECEIPT)]
    transport = {}
    if all(present):
        inventory, receipt = read(out/INVENTORY), read(out/INPUT_RECEIPT)
        assert inventory['result'] == receipt['result'] == RESULT
        assert inventory['complete'] is True and receipt['complete'] is True
        assert inventory['sources'] == item['sources']
        assert receipt['source_requests'] == item['sources']
        assert receipt['original_source_inventory'] == spec(out/INVENTORY)
        bound(out, receipt['source_bundle'])
        count = unpack_inputs(out/BUNDLE, retained, item['sources'])
        assert count == receipt['carrier_member_count']
    else:
        # A hard stop during packaging may leave a complete inventory or bundle.
        # Reuse their bytes where possible; never alter a completed producer file.
        if (out/INVENTORY).exists():
            assert read(out/INVENTORY)['sources'] == item['sources']
        if (out/BUNDLE).exists():
            unpack_inputs(out/BUNDLE, retained, item['sources'])
        transport['R852'] = fetch_source('R852', item['sources']['R852'], retained)
        review_known_sources(item, retained)
        transport['R854'] = fetch_source('R854', item['sources']['R854'], retained)
        reviewed = review_all_sources(item, retained)
        inventory = {'result': RESULT, 'complete': True, 'sources': item['sources'],
                     'all_members_are_unchanged_original_producer_bytes': True}
        save(out/INVENTORY, inventory)
        if not (out/BUNDLE).exists():
            pack_inputs(retained, item['sources'], out/BUNDLE)
        count = unpack_inputs(out/BUNDLE, retained, item['sources'])
        receipt = {'result': RESULT, 'complete': True, 'source_requests': item['sources'],
                   'original_source_inventory': spec(out/INVENTORY), 'source_bundle': spec(out/BUNDLE),
                   'carrier_member_count': count, 'source_review': reviewed, 'range_transport': transport,
                   'original_R852_9_member_and_nested_270_member_carriers_preserved': True,
                   'original_R854_large_operator_not_selected': True,
                   'new_mathematics_run_by_source_IO': False,
                   'archive_digest_semantics': 'original API digest plus complete selected member SHA; Range ZIP not rehashed'}
        save(out/INPUT_RECEIPT, receipt)
    reviewed = review_all_sources(item, retained)
    assert receipt['source_review'] == reviewed
    print('R858_INPUT_REVIEW='+json.dumps({'carrier_member_count': count,
        'source_bundle': receipt['source_bundle'], 'source_review': reviewed}, sort_keys=True), flush=True)
    return retained, receipt


def stable_job(item):
    excluded = {'resume', 'budget_minutes', 'readme_sha256', 'rules_last_read_commit', 'session',
                'target_Z_B_precision', 'target_elliptic_row_B_precision', 'maximum_series_terms'}
    return {key: value for key, value in item.items() if key not in excluded}


def topic_path(name):
    path = (TOPIC/name).resolve()
    assert path.is_relative_to(TOPIC.resolve())
    return path


def guard(item, request):
    assert os.environ.get('GITHUB_ACTIONS') == 'true'
    assert os.environ.get('GITHUB_REPOSITORY') == REPOSITORY
    assert re.fullmatch(r'[0-9a-f]{40}', os.environ.get('GITHUB_SHA', ''))
    assert request.resolve() == REQUEST.resolve()
    assert item['result'] == RESULT and item['p'] == 41 and item['producer_inputs_pending'] is False
    assert item['core'] == CORE and item['core_sha256'] == sha(S/CORE)
    assert item['wrapper'] == 'R858_public_original_p41_single_Z.py'
    assert item['wrapper_sha256'] == sha(__file__)
    assert item['ball_helper'] == BALL_HELPER and item['ball_helper_sha256'] == BALL_HELPER_SHA == sha(S/BALL_HELPER)
    assert item['source_IO_parent'] == PARENT and item['source_IO_parent_sha256'] == PARENT_SHA
    assert item['source_transport_helper'] == TRANSPORT and item['source_transport_helper_sha256'] == TRANSPORT_SHA
    assert item['io_helper'] == RANGE and item['io_helper_sha256'] == RANGE_SHA
    assert 0 < item['budget_minutes'] <= 300
    assert int(item.get('exact_leaf_B_precision', 256)) > 0
    assert 1 <= int(item.get('series_block_size', 16)) <= 256
    assert int(item.get('target_Z_B_precision', 7)) > 0
    assert int(item.get('target_elliptic_row_B_precision', 7)) > 0
    assert int(item.get('maximum_series_terms', 10000)) >= 2
    assert set(item['proofs']) == {'SP', 'ZA', '41S', 'method', 'consumer'}
    for row in item['proofs'].values():
        assert sha(topic_path(row['path'])) == row['sha256']
    assert sha(REPO/'README.md') == item['readme_sha256']['root']
    assert sha(TOPIC/'README.md') == item['readme_sha256']['topic']
    assert set(item['sources']) == {'R852', 'R854', 'CM', 'R791'}
    assert set(item['inputs']) == set(INPUT_KEYS)
    assert all(row is not None for row in item['sources'].values())
    assert all(row is not None for row in item['inputs'].values())
    for label, source in item['sources'].items():
        assert source['files'][MANIFEST]['sha256'] == source['manifest_sha256']
        assert source['files'][source['certificate']['file']] == plain(source['certificate'])
        assert fingerprint({name: plain(row) for name, row in sorted(source['files'].items())}) == source['selected_files_sha256']
        if label != 'R854':
            assert source['expected_conclusion'] == 'success' and source['accepted_process_exit_codes'] == [0]
        else:
            assert source['core_sha256'] == R854_CORE_SHA
            assert source['accepted_process_exit_codes'] in ([0], [125])
            assert source['expected_conclusion'] == ('success' if source['accepted_process_exit_codes'] == [0] else 'failure')
    load_transport()


def write_manifest(out):
    out = Path(out)
    rows = [dict(spec(path), included_in_git=False) for path in sorted(out.iterdir())
            if path.is_file() and path.name not in (MANIFEST, REFERENCE)
            and not path.name.endswith(('.tmp', '.download', '.partial'))]
    save(out/MANIFEST, {'result': RESULT, 'files': rows, 'temporary_active_checkpoint_retention_days': 1,
                        'reproducible_data_in_git_or_release': False})
    save(out/REFERENCE, {'result': RESULT, 'manifest_file': MANIFEST, 'manifest_sha256': sha(out/MANIFEST),
                         'manifest_bytes': (out/MANIFEST).stat().st_size, 'file_count': len(rows)})


def restore(item, out):
    resume = item.get('resume')
    if resume is None:
        return
    out = Path(out)
    assert resume['result'] == RESULT and resume['core_sha256'] == item['core_sha256']
    meta = out.parent/'R858-resume-original-metadata'
    meta.mkdir(parents=True, exist_ok=True)
    archive = IO.Archive(resume, out.parent/'R858-resume-download', whole=False)
    try:
        archive.extract_bound(MANIFEST, resume['manifest_sha256'], meta/MANIFEST, resume['manifest_bytes'])
        data = read(meta/MANIFEST)
        assert data['result'] == RESULT
        entries = {row['file']: plain(row) for row in data['files']}
        assert len(entries) == len(data['files']) == resume['manifest_file_count']
        assert set(archive.by_name) == set(entries) | {MANIFEST, REFERENCE}
        for name in ('run-receipt.json', 'public-actions-input.json'):
            row = entries[name]
            archive.extract_bound(name, row['sha256'], meta/name, row['bytes'])
        run, initial = read(meta/'run-receipt.json'), read(meta/'public-actions-input.json')
        assert str(run['workflow_run_id']) == str(resume['run_id'])
        assert run['source_commit'] == initial['source_commit'] == resume['source_commit']
        assert initial['source_repository'] == REPOSITORY
        assert initial['core_sha256'] == item['core_sha256']
        assert initial['driver_sha256'] == item['wrapper_sha256']
        assert stable_job(initial['job']) == stable_job(item)
        assert run['process_exit_code'] in resume['accepted_process_exit_codes']
        if 'core-receipt.json' in entries:
            row = entries['core-receipt.json']
            archive.extract_bound(row['file'], row['sha256'], meta/row['file'], row['bytes'])
            oldcore = read(meta/row['file'])
            assert run['core_receipt_sha256'] == row['sha256']
            assert oldcore['core_sha256'] == item['core_sha256'] and oldcore['result'] == RESULT
        else:
            oldcore = None
            assert run.get('core_receipt_sha256') is None and run['complete'] is False
        names = [name for name in (INVENTORY, BUNDLE, INPUT_RECEIPT) if name in entries]
        names += [name for name in entries if name.startswith(PREFIX) and name.endswith('.json.gz')]
        archive.extract_many([(name, entries[name]['sha256'], out/name, entries[name]['bytes']) for name in names])
        final_spec = None
        if FINAL in entries:
            row = entries[FINAL]
            archive.extract_bound(FINAL, row['sha256'], meta/FINAL, row['bytes'])
            oldfinal = read(meta/FINAL)
            final_spec = row
            if oldfinal['complete']:
                assert run['complete'] and run['process_exit_code'] == 0 and oldcore and oldcore['complete']
                assert oldcore['final_sha256'] == row['sha256']
                for key in ('stage_manifest', 'resume_state'):
                    bound(out, oldfinal[key])
                # Preserve a completed endpoint as historical bytes, not as
                # this run's new FINAL or an assertion about a higher target.
                shutil.copyfile(meta/FINAL, out/'previous-success-certificate.json')
            # A false FINAL is historical.  A later immutable stage/current
            # committed before interruption must not be constrained by it.
        save(out/'resume-source-receipt.json', {'result': RESULT, 'source_request': resume,
             'old_final_spec': final_spec, 'stable_job_identical': True,
             'same_core_and_mathematical_sources': True,
             'all_completed_stages_and_current_preserved_unchanged': True,
             'old_false_final_not_used_as_current_snapshot': True,
             'source_core_receipt_present': oldcore is not None, 'transport': archive.receipt()})
    finally:
        archive.close()


def check_ball(data, field_digest):
    assert data['representation'] == 'original-p41-normalized-uniformizer-ball-v1'
    assert data['field_sha256'] == field_digest and data['p'] == 41
    assert data['ramification_index'] == 7 and data['residue_degree'] == 2
    assert data['basis'] == 'B^0..B^6,s*B^0..s*B^6; s^2=-3; B=lambda*b'
    assert data['uniformizer'] == 'original B=lambda*b'
    assert isinstance(data['zero_ball'], bool)
    assert isinstance(data['absolute_precision_B'], int) and isinstance(data['relative_precision_B'], int)
    assert len(data['unit_coefficients']) == 14
    assert all(isinstance(x, str) and INTEGER.fullmatch(x) for x in data['unit_coefficients'])
    assert data['zero_ball_is_not_an_exact_zero_assertion'] is True
    assert data['precision_is_absolute_in_original_uniformizer_units'] is True
    if data['zero_ball']:
        assert data['valuation_B'] is None and data['relative_precision_B'] == 0
        assert data['unit_coefficients'] == ['0']*14
    else:
        assert isinstance(data['valuation_B'], int) and data['relative_precision_B'] > 0
        assert data['valuation_B']+data['relative_precision_B'] == data['absolute_precision_B']


def check_embedded(value, out, tag, field_digest):
    if isinstance(value, dict):
        if value.get('representation') == 'original-p41-normalized-uniformizer-ball-v1':
            check_ball(value, field_digest)
        if set(('file', 'bytes', 'sha256')) <= set(value) and isinstance(value['file'], str):
            if value['file'].startswith(PREFIX) and value['file'].endswith('.json.gz'):
                bound(out, value)
        if 'ball' in value and isinstance(value['ball'], dict) and 'representation' in value['ball']:
            assert value['absolute_B_precision'] == value['ball']['absolute_precision_B']
        for key, child in value.items():
            if key != 'configuration':
                check_embedded(child, out, tag, field_digest)
    elif isinstance(value, list):
        for child in value:
            check_embedded(child, out, tag, field_digest)


def math_stage(out, row, tag):
    path = bound(out, row)
    value = read(path)
    assert value['result'] == RESULT and value['configuration'] == tag
    assert value['complete'] is True
    return value


def review_math(item, out, tag):
    out = Path(out)
    description = tag['field']
    assert isinstance(description['lambda'], str) and re.fullmatch(r'[1-9][0-9]*', description['lambda'])
    field_digest = fingerprint({'p': 41, 'ramification_index': 7, 'residue_degree': 2,
        'basis': 'B^0..B^6,s*B^0..s*B^6; s^2=-3; B=lambda*b',
        'integral_B_minimal_polynomial': [str(x) for x in description['integral_B_minimal_polynomial']],
        'lambda': [description['lambda'], '1']})
    current_name = PREFIX+'current.json.gz'
    stages = {}
    manifests = []
    for path in sorted(out.glob(PREFIX+'*.json.gz')):
        value = read(path)
        assert value['result'] == RESULT and value['configuration'] == tag
        if path.name == current_name:
            assert value['complete'] is False
        else:
            assert value['complete'] is True
            if path.name.startswith(PREFIX+'stage-manifest-'):
                manifests.append((path, value))
            else:
                stages[path.name] = spec(path)
        check_embedded(value, out, tag, field_digest)
    for path, value in manifests:
        rows = {row['file']: plain(row) for row in value['files']}
        assert len(rows) == len(value['files'])
        for name, row in rows.items():
            assert stages[name] == row
        assert path.name == PREFIX+'stage-manifest-'+fingerprint(value['files'])[:24]+'.json.gz'
    if not (out/FINAL).exists():
        return None, {'complete_stage_count': len(stages), 'actual_Z_absolute_B_precision': None,
                      'actual_elliptic_row_absolute_B_precisions': [], 'final_present': False}
    final = read(out/FINAL)
    assert final['result'] == RESULT and final['configuration'] == tag
    assert final['p'] == 41 and final['original_map_index'] == 4 and final['original_map_degree'] == 1206
    assert final['requested_Z_absolute_B_precision'] == item['target_Z_B_precision']
    assert final['requested_elliptic_row_absolute_B_precision'] == item['target_elliptic_row_B_precision']
    assert final['original_c_chi_preserved_symbolically'] is True
    for flag in ('unit_chart_solve_recomputed', 'old_exact_C_coordinates_or_rank_recomputed',
                 'auxiliary_518_balls_used_as_p41', 'exact_expanded_rational_point_coordinates_certified',
                 'original_CM_candidate_A1_accepted', 'actual_Y_Picard_period_computed',
                 'actual_global_Hecke_correction_computed', 'actual_height_computed',
                 'height_nonzero_proved', 'all_p_uniformity_proved'):
        assert final[flag] is False
    inventory = math_stage(out, final['stage_manifest'], tag)
    assert {row['file']: plain(row) for row in inventory['files']} == stages
    current = read(bound(out, final['resume_state']))
    assert current['configuration'] == tag and current['complete'] is False
    assert current['completed_stage_manifest'] == final['stage_manifest']
    assert current['stop'] == final['stop']
    for key in ('source_audit', 'field_model', 'four_response_import', 'base_point',
                'formal_point_42', 'H_coefficients', 'finite_series_sum', 'full_tail_certificate',
                'base_Z', 'original_seven_conjugates', 'stop_record'):
        if final[key] is not None:
            math_stage(out, final[key], tag)
    if final['source_audit'] is not None:
        audit = math_stage(out, final['source_audit'], tag)
        assert audit['source_identities'] == tag['source_identities'] and audit['inputs'] == tag['inputs']
        assert audit['original_839_nodes_hash_and_topological_order_verified'] is True
        assert audit['original_17_field_elements_matched_to_R791'] is True
        assert audit['unit_chart_solve_cut_at_the_four_original_responses'] is True
        assert audit['new_unit_chart_solves'] == 0 and audit['old_C_rank_recomputed'] is False
    if final['four_response_import'] is not None:
        imported = math_stage(out, final['four_response_import'], tag)
        assert imported['source_four_response_balls'] == tag['inputs']['four_response_balls']
        assert imported['labels'] == ['A0', 'A1', 'B0', 'B1']
        assert imported['original_CM_scale_applied_again'] is False
        assert imported['original_free1186_constant_preserved'] is True
        assert imported['source_absolute_B_precision'] == final['original_response_absolute_B_precision']
    z_precision = None
    if final['base_Z'] is not None:
        z = math_stage(out, final['base_Z'], tag)
        z_precision = z['original_Z']['absolute_B_precision']
        assert z['actual_original_41_base_Z_ball_computed'] is True
        assert z['actual_height_computed'] is False
        assert z['psi42_derivative_recomputed'] is False
        for key in ('H_coefficients', 'finite_series_sum', 'full_tail_certificate'):
            assert z[key] == final[key]
    assert final['actual_Z_absolute_B_precision'] == z_precision
    assert final['actual_original_41_base_Z_computed'] is (z_precision is not None)
    assert final['actual_original_41_base_Z_certified_to_positive_absolute_B_precision'] is (z_precision is not None and z_precision >= 1)
    assert final['exact_original_point_expression_source_verified'] is (final['source_audit'] is not None)
    assert final['actual_original_p41_response_balls_consumed'] is (final['four_response_import'] is not None)
    for row in final['multiplication_chain']:
        math_stage(out, row, tag)
    row_precisions = []
    for j, row in enumerate(final['elliptic_rows'], 1):
        value = math_stage(out, row, tag)
        assert value['j'] == j and value['source_original_Z'] == final['base_Z']
        assert value['actual_elliptic_first_derivative_row_ball_computed'] is True
        assert value['actual_Y_Picard_period_computed'] is False and value['actual_height_computed'] is False
        assert value['degree84_extension_trace_substituted'] is False
        assert value['normalized_trace_degree'] == 14 and value['original_outer_factor'] == 7
        assert value['final_rational_scale'] == ['1', '2']
        assert value['original_c_chi'] == 'symbolic unchanged multiplier; not evaluated or set equal to 1'
        row_precisions.append(value['elliptic_row_divided_by_c_chi']['absolute_B_precision'])
    assert final['actual_elliptic_row_absolute_B_precisions'] == row_precisions
    assert final['actual_elliptic_first_derivative_rows_computed'] is (len(row_precisions) == 5)
    assert final['original_seven_conjugates_transport_verified'] is (final['original_seven_conjugates'] is not None)
    if final['original_seven_conjugates'] is not None:
        orbit = math_stage(out, final['original_seven_conjugates'], tag)
        assert orbit['source_original_Z'] == final['base_Z']
        assert [x['sigma_power'] for x in orbit['conjugate_balls']] == list(range(7))
        assert all(x['absolute_B_precision'] == z_precision for x in orbit['conjugate_balls'])
        assert orbit['new_seven_sigma_integrals_computed'] is False
    complete = (final['stop'] is None and z_precision is not None and z_precision >= item['target_Z_B_precision']
                and len(row_precisions) == 5 and min(row_precisions) >= item['target_elliptic_row_B_precision'])
    assert final['complete'] is complete
    if complete:
        assert len(final['multiplication_chain']) == 7
        assert final['original_seven_conjugates_transport_verified'] is True
    if final['stop'] is not None:
        assert final['stop_record'] is not None
        stop = math_stage(out, final['stop_record'], tag)
        assert stop['stop_record'] == final['stop']
    check_embedded(final, out, tag, field_digest)
    return final, {'complete_stage_count': len(stages), 'actual_Z_absolute_B_precision': z_precision,
                   'actual_elliptic_row_absolute_B_precisions': row_precisions, 'final_present': True,
                   'stop_kind': None if final['stop'] is None else final['stop']['kind']}


def compute(item, out):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    source = os.environ['GITHUB_SHA']
    started = dt.datetime.now(dt.timezone.utc).isoformat()
    code, error, final, outer_timeout, prepared = 1, None, None, False, False
    try:
        restore(item, out)
        retained, receipt = sources(item, out)
        tag = expected_tag(item, retained)
        save(out/'public-actions-input.json', {'result': RESULT, 'source_repository': REPOSITORY,
            'source_commit': source, 'core_sha256': item['core_sha256'], 'driver_sha256': sha(__file__),
            'job': item, 'source_inventory': receipt['original_source_inventory'],
            'input_receipt': spec(out/INPUT_RECEIPT), 'expected_configuration_sha256': fingerprint(tag),
            'workflow_sha256': sha(REPO/item['workflow']),
            'root_readme_sha256': item['readme_sha256']['root'],
            'topic_readme_sha256': item['readme_sha256']['topic']})
        config = dict(item)
        config['sources'] = {label: {**row, 'directory': str(retained/label)} for label, row in item['sources'].items()}
        config['topic_directory'], config['script_directory'] = str(TOPIC), str(S)
        config_path = out.parent/'R858-expanded-config.json'
        save(config_path, config)
        prepared = True
        command = [sys.executable, str(S/CORE), '--config', str(config_path), '--retained', str(retained),
                   '--output', str(out), '--budget-minutes', str(item['budget_minutes'])]
        with (out/'core.log').open('wb') as log:
            process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
            try:
                code = process.wait(timeout=item['budget_minutes']*60+900)
            except subprocess.TimeoutExpired:
                outer_timeout = True
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=20)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL); process.wait()
                code = 124
                error = 'Outer timeout; all atomically completed stages preserved without a fabricated core receipt.'
        final, summary = review_math(item, out, tag)
        if code == 0:
            assert final is not None and final['complete'] is True
        if (out/'core-receipt.json').exists():
            core = read(out/'core-receipt.json')
            assert core['result'] == RESULT and core['core_sha256'] == item['core_sha256']
            if core['configuration'] is not None:
                assert core['configuration'] == tag and core['configuration_sha256'] == fingerprint(tag)
            if not outer_timeout:
                assert core['process_exit_code'] == code
            if final is not None:
                assert core['final_sha256'] == sha(out/FINAL)
                assert core['complete'] is final['complete']
        elif not outer_timeout:
            assert code != 0
        print('R858_CORE_ENDPOINT='+json.dumps(summary, sort_keys=True), flush=True)
    except Exception:
        error, code = traceback.format_exc(), 1
        print(error, flush=True)
    finally:
        if (out/'core.log').exists() and code != 0:
            with (out/'core.log').open('rb') as log:
                log.seek(max(0, (out/'core.log').stat().st_size-6000))
                print('R858_CORE_LOG_TAIL\n'+log.read().decode('utf-8', errors='replace'), flush=True)
        run = {'result': RESULT, 'source_commit': source, 'workflow_run_id': os.environ['GITHUB_RUN_ID'],
               'workflow_run_attempt': os.environ.get('GITHUB_RUN_ATTEMPT', '1'), 'started_UTC': started,
               'finished_UTC': dt.datetime.now(dt.timezone.utc).isoformat(), 'process_exit_code': code,
               'complete': bool(code == 0 and final and final['complete']), 'error': error,
               'outer_timeout': outer_timeout, 'source_preparation_complete': prepared,
               'core_receipt_sha256': sha(out/'core-receipt.json') if (out/'core-receipt.json').exists() else None,
               'certificate_sha256': sha(out/FINAL) if (out/FINAL).exists() else None,
               'old_unit_chart_and_source_arithmetic_repeated': False,
               'actual_height_computed': False}
        save(out/'run-receipt.json', run)
        write_manifest(out)
        print('R858_RUN_RECEIPT='+json.dumps(run, sort_keys=True), flush=True)
    return code


def verify(item, out):
    out = Path(out)
    data, reference = read(out/MANIFEST), read(out/REFERENCE)
    assert data['result'] == reference['result'] == RESULT
    assert reference['manifest_sha256'] == sha(out/MANIFEST)
    assert reference['manifest_bytes'] == (out/MANIFEST).stat().st_size
    entries = {row['file']: plain(row) for row in data['files']}
    assert len(entries) == len(data['files']) == reference['file_count']
    actual = {path.name for path in out.iterdir() if path.is_file()
              and not path.name.endswith(('.tmp', '.download', '.partial'))}
    assert actual == set(entries) | {MANIFEST, REFERENCE}
    for row in entries.values():
        bound(out, row)
    run = read(out/'run-receipt.json')
    assert run['result'] == RESULT and run['source_commit'] == os.environ['GITHUB_SHA']
    assert str(run['workflow_run_id']) == os.environ['GITHUB_RUN_ID']
    if not run['source_preparation_complete']:
        assert run['complete'] is False and run['process_exit_code'] != 0
        print('R858_COMPLETE_IO_REVIEW='+json.dumps({'full_output_manifest_verified': True,
              'file_count': len(entries), 'source_preparation_complete': False,
              'complete': False, 'mathematical_success_claimed': False}, sort_keys=True), flush=True)
        return 0
    initial = read(out/'public-actions-input.json')
    assert initial['result'] == RESULT and initial['source_repository'] == REPOSITORY
    assert initial['source_commit'] == run['source_commit']
    assert initial['job'] == item
    assert initial['driver_sha256'] == sha(__file__) == item['wrapper_sha256']
    assert initial['core_sha256'] == item['core_sha256']
    assert initial['workflow_sha256'] == sha(REPO/item['workflow'])
    assert initial['root_readme_sha256'] == item['readme_sha256']['root']
    assert initial['topic_readme_sha256'] == item['readme_sha256']['topic']
    retained, receipt = sources(item, out)
    assert initial['source_inventory'] == spec(out/INVENTORY)
    assert initial['input_receipt'] == spec(out/INPUT_RECEIPT)
    tag = expected_tag(item, retained)
    assert initial['expected_configuration_sha256'] == fingerprint(tag)
    final, summary = review_math(item, out, tag)
    core = None
    if 'core-receipt.json' in entries:
        assert run['core_receipt_sha256'] == entries['core-receipt.json']['sha256']
        core = read(out/'core-receipt.json')
        assert core['result'] == RESULT and core['core_sha256'] == item['core_sha256']
        if core['configuration'] is not None:
            assert core['configuration'] == tag and core['configuration_sha256'] == fingerprint(tag)
        if final is not None:
            assert core['final_sha256'] == entries[FINAL]['sha256']
            assert core['complete'] is final['complete']
            assert core['actual_Z_absolute_B_precision'] == final['actual_Z_absolute_B_precision']
            assert core['actual_original_41_base_Z_computed'] is final['actual_original_41_base_Z_computed']
    else:
        assert run['core_receipt_sha256'] is None and run['complete'] is False
    if run['complete']:
        assert run['process_exit_code'] == 0 and core and core['process_exit_code'] == 0
        assert core['error'] is None and core['complete'] is True
        assert final is not None and final['complete'] is True
    summary.update({'full_output_manifest_verified': True, 'file_count': len(entries),
                    'carrier_member_count': receipt['carrier_member_count'],
                    'core_receipt_present': core is not None, 'complete': run['complete'],
                    'full_manifest': spec(out/MANIFEST), 'source_bundle': spec(out/BUNDLE),
                    'actual_height_computed': False, 'all_checks_are_source_IO_and_schema': True})
    print('R858_COMPLETE_IO_REVIEW='+json.dumps(summary, sort_keys=True), flush=True)
    return 0


def main():
    if hasattr(sys, 'set_int_max_str_digits'):
        sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=('compute', 'verify'))
    parser.add_argument('--request', type=Path, default=REQUEST)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    item = read(args.request)
    guard(item, args.request)
    return compute(item, args.out) if args.mode == 'compute' else verify(item, args.out)


if __name__ == '__main__':
    raise SystemExit(main())
