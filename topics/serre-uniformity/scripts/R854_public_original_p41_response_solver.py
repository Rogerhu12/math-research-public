#!/usr/bin/env python3
"""Standard-library source, continuation and IO runner for the original p41 solve.

This module imports only the frozen standard-library carrier code.  It never
imports either mathematical core or the p41 arithmetic helper.
"""
from __future__ import annotations

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
REQUEST = TOPIC/'notes/R854-original-p41-response-solver-public-request.json'
RESULT = 'R854-original-p41-four-response-balls'
FINAL = 'p41-original-p41-four-response-balls-certificate.json'
PREFIX = 'R854-p41-'
MANIFEST = 'full-outputs-manifest.json'
REFERENCE = 'full-outputs-manifest-reference.json'
INVENTORY = PREFIX+'retained-source-inventory.json'
INPUT_RECEIPT = PREFIX+'retained-inputs-receipt.json'
BUNDLE = PREFIX+'retained-original-inputs.tar.gz'
PARENT_HELPER = 'R850_public_original_rigidified_fibres.py'
PARENT_HELPER_SHA = 'ff318ca06e5bf2a385c866df2abb0ea102d6606eb2af2a818a0493f075b123cf'
RANGE_HELPER = 'R824_public_original_global_polar_generators.py'
RANGE_HELPER_SHA = 'c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c'
ORIGINAL_CORE = 'R787_original_power5_relation_solver.py'
ORIGINAL_CORE_SHA = '93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04'
DIRECT_LABELS = ('GLOBAL', 'POINTS')
MATH_LABELS = ('R781', 'R787', 'CM')
POINT_LABELS = ('CM', 'DAG', 'JETS', 'NONTORSION', 'POINTS', 'R791')
BASE_KEYS = ('result', 'run_id', 'source_commit', 'core_sha256', 'manifest_sha256', 'configuration_sha256')
FIELD_NAME = 'R781-original-real-field-input.json.gz'
IMPLICIT_NAME = 'R787-implicit-CM-exact-source-bound-implicit-expression.json.gz'
H64 = re.compile(r'[0-9a-f]{64}')
RF = IO = None
# Filled from the literal, frozen mathematical scope, without importing it.
SCOPE = {'original_p': 41, 'original_map_index': 4, 'original_map_degree': '1206', 'unknown_dimension': 2420, 'full_cleared_equation_rows': 2560, 't_coordinates': 20, 'full_L_coordinate_dimension': 14, 'original_free_column': 1186, 'other_original_free_columns': 'zero', 'field_basis': 'B^0..B^6,s*B^0..s*B^6; s^2=-3; B=lambda*b', 'uniformizer': 'original B=lambda*b', 'ramification_index': 7, 'residue_degree': 2, 'cleared_A_sign': 1, 'cleared_C_sign': 1, 'free_rhs_sign': -1, 'initial_scale_rule': 'geometric-original-row-scaling; Rtilde_n=41^(a*n+c)R_n, Ktilde_n=41^(a*n)K_n, c=max(0,a-3)', 'inverse_bound_applies_to': 'geometrically_scaled_original_tall_matrix', 'residue_lift_rule': 'a+s*b with a,b in 0..40', 'row_saturation_rule': 'independent rows unchanged; dependent differences divided by B', 'residue_matrix_backend': 'paired restriction of scalars to nmod_mat(41)', 'composite_modulus_matrix_inverse_used': False, 'original_kappa_algebraic_inverse_recomputed': False, 'completed_auxiliary_prime_arithmetic_recomputed': False, 'auxiliary_518_balls_are_p41_inputs': False, 'unaccepted_A1_candidate_consumed': False, 'precision_and_budget_excluded_from_mathematical_identity': True, 'working_matrix_retention': 'latest complete saturation state; immutable row operations and SHA retirement receipts'}


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(4*1024*1024), b''):
            h.update(block)
    return h.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == '.gz' else open)(path, 'rt', encoding='utf-8') as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+'.tmp')
    temporary.write_text(json.dumps(value, sort_keys=True, separators=(',', ':'))+'\n', encoding='utf-8')
    temporary.replace(path)


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def safe_name(name):
    assert isinstance(name, str) and Path(name).name == name and name not in ('.', '..') and '\\' not in name
    return name


def plain(value):
    result = {key: value[key] for key in ('file', 'bytes', 'sha256')}
    safe_name(result['file'])
    assert isinstance(result['bytes'], int) and result['bytes'] >= 0 and H64.fullmatch(result['sha256'])
    return result


def file_spec(path):
    path = Path(path)
    return {'file': path.name, 'bytes': path.stat().st_size, 'sha256': sha(path)}


def bound(folder, value):
    value = plain(value)
    path = Path(folder)/value['file']
    assert file_spec(path) == value, ('Original bytes changed', value['file'])
    return path


def identity(source):
    return {key: source[key] for key in BASE_KEYS}


def topic_path(name):
    part = PurePosixPath(name)
    assert not part.is_absolute() and '..' not in part.parts
    result = (TOPIC/str(part)).resolve()
    assert result.is_relative_to(TOPIC.resolve())
    return result


def load_io(item, helper_dir=None):
    global RF, IO
    folder = S if helper_dir is None else Path(helper_dir)
    assert item['source_io_helper_sha256'] == PARENT_HELPER_SHA
    assert item['io_helper_sha256'] == RANGE_HELPER_SHA
    path = folder/PARENT_HELPER
    assert sha(path) == PARENT_HELPER_SHA
    module = importlib.util.spec_from_file_location('R854_frozen_stdlib_parent_IO', path)
    RF = importlib.util.module_from_spec(module)
    module.loader.exec_module(RF)
    RF.load_helper({'io_helper_sha256': RANGE_HELPER_SHA}, folder)
    IO = RF.IO


def compressed_property(path, key):
    """Read a small own-stage property without retaining large coefficient arrays."""
    token, buffer = json.dumps(key)+':', ''
    decoder = json.JSONDecoder()
    with gzip.open(path, 'rt', encoding='utf-8') as stream:
        while True:
            chunk = stream.read(65536)
            if not chunk:
                raise AssertionError('Missing own-stage property '+key+': '+str(path))
            buffer += chunk
            position = buffer.find(token)
            if position < 0:
                buffer = buffer[-len(token):]
                continue
            tail = buffer[position+len(token):]
            try:
                return decoder.raw_decode(tail.lstrip())[0]
            except json.JSONDecodeError:
                buffer = buffer[position:]


def check_stage(path, tag):
    assert compressed_property(path, 'configuration') == tag
    assert compressed_property(path, 'complete') is True


def expected_tag(item, groups, retained):
    retained = Path(retained)
    field = read(bound(retained/'R781', groups['R781']['files'][FIELD_NAME]))['field']
    implicit = read(bound(retained/'CM', groups['CM']['files'][IMPLICIT_NAME]))
    chart = read(bound(retained/'R787', implicit['unit_chart_solve']['original_chart']))
    assert field == implicit['original_field']
    return {'result': RESULT, 'source_sha256': item['core_sha256'], 'python_flint': '0.9.0',
        'method_sha256': item['method_sha256'], 'single_Z_contract_sha256': item['single_Z_contract_sha256'],
        'scaling_method_sha256': item['scaling_method_sha256'], 'ZA_proof_sha256': item['ZA_proof_sha256'],
        'linear_algebra_sha256': item['linear_algebra_sha256'],
        'original_R787_core_sha256': ORIGINAL_CORE_SHA,
        'source_identities': {label: {**identity(groups[label]),
            'selected_files_sha256': fingerprint(groups[label]['files'])} for label in MATH_LABELS},
        'field': field, 'original_pivot_columns': chart['pivot_columns'],
        'operator_column_block_size': item['operator_column_block_size'],
        'matrix_checkpoint_rows': item['matrix_checkpoint_rows'], **SCOPE}


def guard(item, path):
    assert os.environ.get('GITHUB_ACTIONS') == 'true'
    assert os.environ.get('GITHUB_REPOSITORY') == 'Rogerhu12/math-research-public'
    assert path.resolve() == REQUEST.resolve()
    assert item['result'] == RESULT and item['p'] == 41 and item['producer_inputs_pending'] is False
    assert item['core'] == 'R854_original_p41_response_solver.py'
    assert item['wrapper'] == Path(__file__).name == 'R854_public_original_p41_response_solver.py'
    assert sha(S/item['core']) == item['core_sha256'] and sha(__file__) == item['wrapper_sha256']
    assert item['linear_algebra'] == 'R854_p41_DVR_linear_algebra.py'
    assert sha(S/item['linear_algebra']) == item['linear_algebra_sha256']
    assert item['original_R787_core'] == ORIGINAL_CORE and item['original_R787_core_sha256'] == ORIGINAL_CORE_SHA
    assert sha(S/ORIGINAL_CORE) == ORIGINAL_CORE_SHA
    for key in ('method', 'scaling_method', 'single_Z_contract', 'ZA_proof'):
        assert sha(topic_path(item[key])) == item[key+'_sha256']
    assert 0 < item['budget_minutes'] <= 300
    assert isinstance(item['operator_B_precision'], int) and item['operator_B_precision'] >= 2
    assert isinstance(item['requested_response_B_precision'], int) and item['requested_response_B_precision'] > 0
    assert 1 <= item['operator_column_block_size'] <= 32 and 1 <= item['matrix_checkpoint_rows'] <= 128
    assert sha(REPO/'README.md') == item['readme_sha256']['root']
    assert sha(TOPIC/'README.md') == item['readme_sha256']['topic']
    assert set(item['sources']) == set(DIRECT_LABELS)
    for source in item['sources'].values():
        assert source['expected_conclusion'] == 'success' and source['accepted_process_exit_codes'] == [0]
        for key in ('manifest_sha256', 'configuration_sha256', 'core_sha256', 'wrapper_sha256',
                    'archive_sha256', 'selected_files_sha256'):
            assert H64.fullmatch(source[key])
        assert source['artifact_id'] > 0 and source['archive_bytes'] > 0
        plain(source['reference'])
    load_io(item)


def source_layout(item, parents):
    """Select actual old groups, preserving every source identity and byte spec."""
    parents = Path(parents)
    global_inventory = read(parents/'GLOBAL'/RF.GLOBAL_INVENTORY)
    point_receipt = read(parents/'POINTS'/RF.POINT_RECEIPT)
    nested = point_receipt['expanded_sources']
    assert set(nested) == set(POINT_LABELS)
    groups = {label: global_inventory['sources'][label] for label in ('R781', 'R787')}
    groups.update(nested)
    assert len(groups['R781']['files']) == 134 and len(groups['R787']['files']) == 1241
    assert sum(len(nested[k]['files']) for k in POINT_LABELS) == 270
    RF.same_origin(global_inventory['sources']['R840'], groups['CM'])
    RF.same_origin(global_inventory['sources']['R791'], groups['R791'])
    assert fingerprint(groups) == item['retained_sources_sha256']
    assert sum(len(g['files']) for g in groups.values()) == item['retained_source_file_count']
    metadata = {}
    for label in DIRECT_LABELS:
        selected = RF.selected_rows(label, item['sources'][label], parents/label)
        if label == 'GLOBAL':
            selected = {name: row for name, row in selected.items() if name != RF.GLOBAL_BUNDLE}
        metadata[label] = selected
    assert fingerprint(metadata) == item['parent_metadata_sha256']
    return groups, metadata


def extract_global_subset(bundle, inventory, retained):
    """Hash all 2709 old members once; save only the 1375 required R781/R787 files."""
    all_members = {(label, name): plain(row) for label, source in inventory['sources'].items()
                   for name, row in source['files'].items()}
    selected = {key for key in all_members if key[0] in ('R781', 'R787')}
    assert len(all_members) == 2709 and len(selected) == 1375
    seen = set()
    retained = Path(retained)
    with tarfile.open(bundle, 'r|gz') as archive:
        for member in archive:
            if member.isdir():
                continue
            part = PurePosixPath(member.name)
            assert member.isfile() and not part.is_absolute() and len(part.parts) == 2 and '..' not in part.parts
            key = tuple(part.parts)
            assert key in all_members and key not in seen
            seen.add(key)
            row = all_members[key]
            assert member.size == row['bytes']
            destination = retained/key[0]/key[1]
            temporary = destination.with_name(destination.name+'.download')
            sink = None
            if key in selected and not destination.exists():
                destination.parent.mkdir(parents=True, exist_ok=True)
                sink = temporary.open('wb')
            h, count = hashlib.sha256(), 0
            try:
                with archive.extractfile(member) as stream:
                    for block in iter(lambda: stream.read(4*1024*1024), b''):
                        h.update(block); count += len(block)
                        if sink is not None:
                            sink.write(block)
            finally:
                if sink is not None:
                    sink.close()
            assert count == row['bytes'] and h.hexdigest() == row['sha256']
            if key in selected:
                if destination.exists():
                    bound(destination.parent, row)
                else:
                    temporary.replace(destination)
    assert seen == set(all_members)
    return {'original_carrier_members_hashed': len(seen), 'selected_original_members': len(selected)}


def review_group(label, source, retained):
    folder = Path(retained)/label
    files = {name: plain(row) for name, row in source['files'].items()}
    assert len(files) == source['selected_file_count']
    assert fingerprint([files[n] for n in sorted(files)]) == source['selected_files_sha256']
    for name, row in files.items():
        assert name == row['file']
        bound(folder, row)
    manifest = read(folder/MANIFEST)
    assert files[MANIFEST]['sha256'] == source['manifest_sha256'] and manifest['result'] == source['result']
    entries = {row['file']: plain(row) for row in manifest['files']}
    assert len(entries) == len(manifest['files'])
    for name, row in files.items():
        if name not in (MANIFEST, REFERENCE):
            assert entries[name] == row
    if label in ('R781', 'R787'):
        if source.get('certificate_name'):
            cert = read(folder/source['certificate_name'])
            assert cert['complete'] is True and cert['result'] == source['result']
            tag = cert['configuration']
        else:
            tag = read(folder/source['configuration_stage'])['configuration']
        assert fingerprint(tag) == source['configuration_sha256']
        assert tag['source_sha256'] == source['core_sha256']
        run = read(folder/'run-receipt.json')
        assert str(run['workflow_run_id']) == str(source['run_id']) and run['source_commit'] == source['source_commit']
        # The R787 parent is a real BudgetStop.  Its complete row stages remain
        # valid sources; no successful original function certificate is invented.
        if label == 'R787':
            public = read(folder/'public-actions-input.json')
            core = read(folder/'core-receipt.json')
            assert public['source_commit'] == source['source_commit']
            assert public['job']['core_sha256'] == source['core_sha256']
            assert core['source_sha256'] == source['core_sha256']
            assert run['process_exit_code'] == 1 and core['complete'] is False
        else:
            assert run['process_exit_code'] == 0
        for name in files:
            if name.endswith('.json.gz'):
                value = read(folder/name)
                assert value['complete'] is True and value['configuration'] == tag
    return files


def review_source_closure(item, parents, retained, historical_global_carrier=False):
    parents, retained = Path(parents), Path(retained)
    direct = {label: RF.review_source(label, item['sources'][label], parents/label,
        allow_missing_opaque=(historical_global_carrier and label == 'GLOBAL')) for label in DIRECT_LABELS}
    groups, metadata = source_layout(item, parents)
    # The POINTS carrier is small and remains in our carrier.  Its 270 original
    # members and actual parent-child configurations are checked on every resume.
    nested = RF.review_nested_points(parents/'POINTS', retained)
    for label in POINT_LABELS:
        assert nested[label] == groups[label]
    for label in ('R781', 'R787'):
        review_group(label, groups[label], retained)
    field = read(retained/'R781'/FIELD_NAME)['field']
    implicit = read(retained/'CM'/IMPLICIT_NAME)
    assert implicit['original_field'] == field and implicit['expanded_coordinates_exactly_certified'] is False
    assert implicit['unit_chart_solve']['shape'] == [2420, 2420]
    assert implicit['unit_chart_solve']['free_column'] == 1186
    recipe = implicit['operator_recipe']
    assert len(recipe['original_F_rows']) == 1234
    for row in recipe['original_F_rows']:
        assert plain(row) == groups['R787']['files'][row['file']]
    for name in recipe['R781_source_files']:
        assert name in groups['R781']['files']
    for key in ('original_Z_and_A_row_selection', 'original_chart'):
        row = plain(implicit['unit_chart_solve'][key])
        assert row == groups['R787']['files'][row['file']]
    for key in ('e0_e1', 'e0Z_e1Z'):
        row = plain(implicit['linear_responses'][key])
        assert row == groups['CM']['files'][row['file']]
        index = read(retained/'CM'/row['file'])
        children = index['completed_blocks'] if key == 'e0_e1' else index['blocks']
        for child in children:
            assert plain(child) == groups['CM']['files'][child['file']]
    return groups, metadata, direct


def carrier_members(groups, metadata):
    result = {label: source['files'] for label, source in groups.items()}
    result.update({'_PARENT_'+label: files for label, files in metadata.items()})
    return result


def pack_carrier(retained, parents, groups, metadata, target):
    retained, parents, target = Path(retained), Path(parents), Path(target)
    temporary = target.with_name(target.name+'.tmp')
    with temporary.open('wb') as raw, gzip.GzipFile(fileobj=raw, mode='wb', mtime=0,
            filename='', compresslevel=0) as compressed, tarfile.open(fileobj=compressed, mode='w|') as archive:
        for label, files in sorted(carrier_members(groups, metadata).items()):
            folder = parents/label[len('_PARENT_'):] if label.startswith('_PARENT_') else retained/label
            for name, row in sorted(files.items()):
                path = bound(folder, row)
                info = archive.gettarinfo(str(path), arcname=label+'/'+name)
                info.uid = info.gid = info.mtime = 0
                info.uname = info.gname = ''
                with path.open('rb') as stream:
                    archive.addfile(info, stream)
    temporary.replace(target)


def unpack_carrier(bundle, retained, parents, groups, metadata):
    retained, parents = Path(retained), Path(parents)
    wanted = {(label, name): plain(row) for label, files in carrier_members(groups, metadata).items()
              for name, row in files.items()}
    seen = set()
    with tarfile.open(bundle, 'r|gz') as archive:
        for member in archive:
            if member.isdir():
                continue
            path = PurePosixPath(member.name)
            assert member.isfile() and not path.is_absolute() and len(path.parts) == 2 and '..' not in path.parts
            label, name = path.parts
            key = (label, name)
            assert key in wanted and key not in seen
            seen.add(key); row = wanted[key]
            assert member.size == row['bytes']
            folder = parents/label[len('_PARENT_'):] if label.startswith('_PARENT_') else retained/label
            folder.mkdir(parents=True, exist_ok=True)
            destination = folder/name
            temporary = destination.with_name(name+'.download')
            h, count = hashlib.sha256(), 0
            with archive.extractfile(member) as source, temporary.open('wb') as sink:
                for block in iter(lambda: source.read(4*1024*1024), b''):
                    h.update(block); count += len(block); sink.write(block)
            assert count == row['bytes'] and h.hexdigest() == row['sha256']
            if destination.exists():
                bound(folder, row); temporary.unlink()
            else:
                temporary.replace(destination)
    assert seen == set(wanted)
    return len(seen)


def prepare_sources(item, out, allow_download=True):
    out = Path(out)
    parents = out.parent/'R854-source-parents'
    retained = out.parent/'R854-retained'
    parents.mkdir(parents=True, exist_ok=True); retained.mkdir(parents=True, exist_ok=True)
    present = [(out/name).exists() for name in (INPUT_RECEIPT, INVENTORY, BUNDLE)]
    if all(present):
        receipt, inventory = read(out/INPUT_RECEIPT), read(out/INVENTORY)
        assert receipt['result'] == inventory['result'] == RESULT
        assert receipt['complete'] is True and inventory['complete'] is True
        assert receipt['direct_source_requests'] == item['sources']
        assert receipt['retained_sources_sha256'] == item['retained_sources_sha256']
        bound(out, receipt['source_inventory']); bound(out, receipt['source_bundle'])
        count = unpack_carrier(out/BUNDLE, retained, parents, inventory['retained_sources'], inventory['parent_metadata'])
        groups, metadata, direct = review_source_closure(item, parents, retained, historical_global_carrier=True)
        assert groups == inventory['retained_sources'] and metadata == inventory['parent_metadata']
        assert count == receipt['carrier_member_count'] == item['carrier_member_count']
        assert receipt['first_source_transfer']['GLOBAL']['original_carrier_members_hashed'] == 2709
        return retained, groups, receipt
    assert allow_download, 'Resume must preserve the completed original source carrier.'
    transfer = {label: RF.fetch_direct(label, item['sources'][label], parents) for label in DIRECT_LABELS}
    global_inventory = read(parents/'GLOBAL'/RF.GLOBAL_INVENTORY)
    global_receipt = read(parents/'GLOBAL'/RF.GLOBAL_RECEIPT)
    global_bundle = bound(parents/'GLOBAL', global_receipt['source_bundle'])
    subset = extract_global_subset(global_bundle, global_inventory, retained)
    groups, metadata, direct = review_source_closure(item, parents, retained)
    inventory = {'result': RESULT, 'complete': True, 'retained_sources': groups,
        'parent_metadata': metadata, 'direct_source_identities': {k: identity(item['sources'][k]) for k in DIRECT_LABELS},
        'all_members_are_unchanged_original_producer_bytes': True,
        'core_source_labels': list(MATH_LABELS), 'future_point_source_labels': list(POINT_LABELS)}
    save(out/INVENTORY, inventory)
    pack_carrier(retained, parents, groups, metadata, out/BUNDLE)
    receipt = {'result': RESULT, 'complete': True, 'direct_source_requests': item['sources'],
        'retained_sources_sha256': item['retained_sources_sha256'],
        'source_inventory': file_spec(out/INVENTORY), 'source_bundle': file_spec(out/BUNDLE),
        'carrier_member_count': item['carrier_member_count'],
        'retained_original_source_file_count': item['retained_source_file_count'],
        'first_source_transfer': {'GLOBAL': {**subset, 'source_bundle': plain(global_receipt['source_bundle']),
            'source_bundle_actual_bytes_hashed_before_extraction': True},
            'POINTS': {'original_members_verified': 270, 'opaque_input_bundle_kept': True}},
        'range_transport': transfer, 'original_395MB_carrier_replaced_only_by_manifest_bound_required_members': True,
        'old_mathematical_arithmetic_recomputed': False, 'auxiliary_current_is_not_a_p41_input': True}
    save(out/INPUT_RECEIPT, receipt)
    print('R854_SOURCE_IO='+json.dumps({'carrier': receipt['source_bundle'],
        'retained_sources': item['retained_source_file_count'], 'carrier_members': item['carrier_member_count'],
        'source_GLOBAL_members_hashed': 2709, 'source_POINT_members_hashed': 270,
        'new_mathematical_arithmetic_executed': False}, sort_keys=True), flush=True)
    return retained, groups, receipt


def output_manifest(out):
    out = Path(out)
    rows = [dict(file_spec(path), included_in_git=False) for path in sorted(out.iterdir()) if path.is_file()
            and path.name not in (MANIFEST, REFERENCE) and not path.name.endswith(('.tmp', '.download', '.partial'))]
    save(out/MANIFEST, {'result': RESULT, 'files': rows, 'temporary_active_checkpoint_retention_days': 1,
                        'reproducible_data_in_git_or_release': False})
    save(out/REFERENCE, {'result': RESULT, 'manifest_file': MANIFEST, 'manifest_sha256': sha(out/MANIFEST),
        'manifest_bytes': (out/MANIFEST).stat().st_size, 'file_count': len(rows)})


def check_manifest(out):
    out = Path(out)
    manifest = read(out/MANIFEST)
    assert manifest['result'] == RESULT
    entries = {row['file']: plain(row) for row in manifest['files']}
    assert len(entries) == len(manifest['files'])
    for row in entries.values():
        bound(out, row)
    reference = read(out/REFERENCE)
    assert reference['result'] == RESULT and reference['manifest_file'] == MANIFEST
    assert reference['manifest_sha256'] == sha(out/MANIFEST)
    assert reference['manifest_bytes'] == (out/MANIFEST).stat().st_size and reference['file_count'] == len(entries)
    return entries


def stable_job(item):
    excluded = ('resume', 'budget_minutes', 'readme_sha256', 'rules_last_read_commit',
                'operator_B_precision', 'requested_response_B_precision')
    return {key: value for key, value in item.items() if key not in excluded}


def restore(item, out):
    resume = item.get('resume')
    if resume is None:
        return
    assert resume['result'] == RESULT and resume['core_sha256'] == item['core_sha256']
    out = Path(out)
    meta = out.parent/'R854-resume-metadata'
    meta.mkdir(parents=True, exist_ok=True)
    archive = IO.Archive(resume, out.parent/'R854-resume-download', whole=False)
    try:
        archive.extract_bound(MANIFEST, resume['manifest_sha256'], meta/MANIFEST, resume['manifest_bytes'])
        manifest = read(meta/MANIFEST)
        assert manifest['result'] == RESULT
        entries = {row['file']: plain(row) for row in manifest['files']}
        assert len(entries) == len(manifest['files']) == resume['manifest_file_count']
        assert set(archive.by_name) == set(entries)|{MANIFEST, REFERENCE}
        names = ['run-receipt.json', 'public-actions-input.json', INPUT_RECEIPT, INVENTORY, BUNDLE]
        if 'core-receipt.json' in entries:
            names.append('core-receipt.json')
        for name in names:
            row = entries[name]
            destination = out/name if name in (INPUT_RECEIPT, INVENTORY, BUNDLE) else meta/name
            archive.extract_bound(name, row['sha256'], destination, row['bytes'])
        run, initial = read(meta/'run-receipt.json'), read(meta/'public-actions-input.json')
        assert run['result'] == initial['result'] == RESULT
        assert run['source_commit'] == initial['source_commit'] == resume['source_commit']
        assert str(run['workflow_run_id']) == str(resume['run_id'])
        assert initial['core_sha256'] == item['core_sha256'] and initial['driver_sha256'] == item['wrapper_sha256']
        assert stable_job(initial['job']) == stable_job(item)
        assert item['operator_B_precision'] >= initial['job']['operator_B_precision']
        assert run['process_exit_code'] in resume['accepted_process_exit_codes']
        if 'core-receipt.json' in entries:
            core = read(meta/'core-receipt.json')
            assert core['result'] == RESULT and core['core_sha256'] == item['core_sha256']
            assert run['core_receipt_sha256'] == entries['core-receipt.json']['sha256']
        else:
            core = None
            assert run.get('core_receipt_sha256') is None and run['complete'] is False
        retained, groups, receipt = prepare_sources(item, out, allow_download=False)
        tag = expected_tag(item, groups, retained)
        names = sorted(name for name in entries if name.startswith(PREFIX) and name.endswith('.json.gz'))
        archive.extract_many([(name, entries[name]['sha256'], out/name, entries[name]['bytes']) for name in names])
        for name in names:
            check_stage(out/name, tag)
        restored_final = False
        if FINAL in entries:
            row = entries[FINAL]
            archive.extract_bound(FINAL, row['sha256'], meta/FINAL, row['bytes'])
            final = read(meta/FINAL)
            assert final['result'] == RESULT and final['configuration'] == tag
            if final['complete']:
                assert run['complete'] and run['process_exit_code'] == 0 and core and core['complete']
                assert core['final_sha256'] == row['sha256']
                for key in ('source_audit', 'stage_manifest', 'four_response_balls', 'unit_minor_and_left_inverse_bound'):
                    bound(out, final[key])
                shutil.copyfile(meta/FINAL, out/FINAL)
                restored_final = True
        save(out/'resume-inheritance-receipt.json', {'result': RESULT, 'complete': True,
            'source_resume': resume, 'original_manifest': file_spec(meta/MANIFEST),
            'range_transport': archive.receipt(), 'restored_complete_stages': [entries[name] for name in names],
            'restored_successful_final': restored_final,
            'old_false_final_does_not_override_current_manifest': True,
            'unchanged_stage_bytes_and_row_operation_retirement_receipts_preserved': True,
            'no_old_p41_digit_or_source_arithmetic_executed_by_wrapper': True})
    finally:
        archive.close()


def compute(item, out, request_path):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    process, exitcode, error, outer_timeout = None, 1, None, False
    try:
        restore(item, out)
        retained, groups, receipt = prepare_sources(item, out)
        expanded = dict(item)
        expanded['retained_sources'] = {label: groups[label] for label in MATH_LABELS}
        save(out/'public-actions-expanded-job.json', expanded)
        tag = expected_tag(item, groups, retained)
        initial = {'result': RESULT, 'source_repository': 'Rogerhu12/math-research-public',
            'source_commit': os.environ['GITHUB_SHA'], 'job': item, 'request_sha256': sha(request_path),
            'core_sha256': item['core_sha256'], 'driver_sha256': sha(__file__),
            'expanded_job_sha256': sha(out/'public-actions-expanded-job.json'),
            'source_inventory': receipt['source_inventory'], 'expected_configuration_sha256': fingerprint(tag),
            'root_readme_sha256': sha(REPO/'README.md'), 'topic_readme_sha256': sha(TOPIC/'README.md'),
            'workflow_sha256': sha(REPO/item['workflow']),
            'prepared_at_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
            'all_new_original_p41_arithmetic_is_in_public_Actions_core': True}
        save(out/'public-actions-input.json', initial)
        command = [sys.executable, str(S/item['core']), '--config', str(out/'public-actions-expanded-job.json'),
            '--method', str(topic_path(item['method'])), '--scaling-method', str(topic_path(item['scaling_method'])),
            '--linear-algebra', str(S/item['linear_algebra']), '--original-core', str(S/ORIGINAL_CORE),
            '--retained', str(retained), '--output', str(out), '--budget-minutes', str(item['budget_minutes'])]
        with (out/'core.log').open('w', encoding='utf-8') as log:
            process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
            try:
                exitcode = process.wait(timeout=item['budget_minutes']*60+900)
            except subprocess.TimeoutExpired:
                outer_timeout = True
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=20)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL); process.wait()
                exitcode = 124
    except BaseException as exc:
        error = {'type': type(exc).__name__, 'message': str(exc)}
        traceback.print_exc()
        print('R854_WRAPPER_ERROR='+json.dumps(error, sort_keys=True), flush=True)
    finally:
        core = read(out/'core-receipt.json') if (out/'core-receipt.json').exists() else None
        final = read(out/FINAL) if (out/FINAL).exists() else None
        complete = bool(exitcode == 0 and error is None and core and core['complete'] and final and final['complete'])
        run = {'result': RESULT, 'p': 41, 'source_commit': os.environ.get('GITHUB_SHA'),
            'workflow_run_id': os.environ.get('GITHUB_RUN_ID'), 'workflow_attempt': os.environ.get('GITHUB_RUN_ATTEMPT'),
            'process_exit_code': exitcode, 'complete': complete, 'error': error, 'outer_timeout': outer_timeout,
            'core_receipt_sha256': sha(out/'core-receipt.json') if core else None,
            'finished_at_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
            'A1_exact_zero_proved': False, 'actual_height_computed': False}
        save(out/'run-receipt.json', run)
        output_manifest(out)
        print('R854_RUN_RECEIPT='+json.dumps(run, sort_keys=True), flush=True)
    return 0 if complete else exitcode or 1


def verify_retirement(out, entries, tag):
    """Only obsolete work matrices may be absent, with immutable SHA receipts."""
    retired = {}
    count = 0
    for name in sorted(entries):
        if not name.startswith(PREFIX+'retired-work-') or not name.endswith('.json.gz'):
            continue
        record = read(out/name)
        assert record['configuration'] == tag and record['complete'] is True
        assert record['all_row_operations_and_bounds_remain_retained'] is True
        assert record['old_work_is_not_a_new_mathematical_input'] is True
        for key in ('old_completed_state', 'superseding_completed_state'):
            bound(out, record[key])
        old = read(out/record['old_completed_state']['file'])
        new = read(out/record['superseding_completed_state']['file'])
        assert new['previous_state'] == record['old_completed_state'] and new['step'] == old['step']+1
        assert len(old['row_transform_lower_bounds']) == len(new['row_transform_lower_bounds']) == 2560
        names = {row['file']: plain(row) for row in record['retired_files']}
        for key in ('matrix', 'right_numerator'):
            assert names[old[key]['file']] == plain(old[key])
        for filename, row in names.items():
            assert filename.startswith(PREFIX+'N') and ('-matrix.' in filename or '-right-numerator.' in filename or '-rows-' in filename)
            if filename in entries:
                assert entries[filename] == row
            if filename in retired:
                assert retired[filename] == row
            retired[filename] = row
        count += 1
    return count, retired


def verify(out):
    out = Path(out)
    entries = check_manifest(out)
    initial, run = read(out/'public-actions-input.json'), read(out/'run-receipt.json')
    item = initial['job']
    assert initial['result'] == run['result'] == RESULT
    assert initial['source_commit'] == run['source_commit']
    assert initial['driver_sha256'] == item['wrapper_sha256'] == sha(__file__)
    assert initial['core_sha256'] == item['core_sha256']
    load_io(item)
    retained, groups, receipt = prepare_sources(item, out, allow_download=False)
    tag = expected_tag(item, groups, retained)
    assert fingerprint(tag) == initial['expected_configuration_sha256']
    assert sha(out/'public-actions-expanded-job.json') == initial['expanded_job_sha256']
    expanded = read(out/'public-actions-expanded-job.json')
    assert expanded['retained_sources'] == {label: groups[label] for label in MATH_LABELS}
    for key, value in item.items():
        assert expanded[key] == value
    core = read(out/'core-receipt.json') if 'core-receipt.json' in entries else None
    if core is None:
        assert run.get('core_receipt_sha256') is None and run['complete'] is False
    else:
        assert run['core_receipt_sha256'] == entries['core-receipt.json']['sha256']
        assert core['result'] == RESULT and core['core_sha256'] == item['core_sha256']
        if core['configuration'] is not None:
            assert core['configuration'] == tag and core['configuration_sha256'] == fingerprint(tag)
        assert core['A1_exact_zero_proved'] is False and core['actual_height_computed'] is False
    math_names = sorted(name for name in entries if name.startswith(PREFIX) and name.endswith('.json.gz'))
    for name in math_names:
        check_stage(out/name, tag)
    retired_count, retired = verify_retirement(out, entries, tag)
    stage_inventory_name = PREFIX+'stage-manifest.json.gz'
    if stage_inventory_name in entries:
        inventory = read(out/stage_inventory_name)
        selected = {row['file']: plain(row) for row in inventory['files']}
        assert len(selected) == len(inventory['files'])
        # On a hard stop an old snapshot may survive while a new stage or work
        # retirement is already complete.  The full output manifest is current.
        for name, row in selected.items():
            mutable_current = bool(re.fullmatch(re.escape(PREFIX)+r'N\d{6}-Dixon-current\.json\.gz', name))
            assert ((name in entries and (entries[name] == row or mutable_current))
                    or retired.get(name) == row)
    final = read(out/FINAL) if FINAL in entries else None
    if final is not None:
        assert final['result'] == RESULT and final['configuration'] == tag
        for flag in ('expanded_exact_L_coordinates_accepted', 'A1_exact_zero_proved', 'actual_Z_computed',
                     'actual_height_computed', 'auxiliary_prime_ball_used_as_p41'):
            assert final[flag] is False
        if final['complete']:
            assert run['complete'] is True and run['process_exit_code'] == 0
            assert core and core['complete'] is True and core['exit_code'] == 0
            assert core['final_sha256'] == entries[FINAL]['sha256']
            assert final['actual_original_p41_four_response_balls_certified'] is True
            assert final['actual_response_absolute_B_precision'] >= final['requested_response_absolute_B_precision'] > 0
            assert final['actual_response_absolute_B_precision'] >= item['requested_response_B_precision']
            for key in ('source_audit', 'stage_manifest', 'four_response_balls', 'unit_minor_and_left_inverse_bound'):
                bound(out, final[key])
            actual_inventory = read(out/final['stage_manifest']['file'])
            actual = {row['file']: plain(row) for row in actual_inventory['files']}
            assert set(actual) == set(math_names)-{stage_inventory_name}
            for name, row in actual.items():
                assert row == entries[name]
            response = read(out/final['four_response_balls']['file'])
            unit = read(out/final['unit_minor_and_left_inverse_bound']['file'])
            assert response['labels'] == ['A0', 'A1', 'B0', 'B1']
            assert response['absolute_B_precision'] == final['actual_response_absolute_B_precision']
            assert response['actual_original_p41_four_response_balls_certified'] is True
            assert response['B_response_free1186_constant_preserved'] is True
            assert response['original_CM_scale_applied_again'] is False
            assert response['numerators']['shape'] == [4, 1]
            assert unit['shape'] == [2420, 2420] and unit['original_tall_shape'] == [2560, 2420]
            assert unit['full_selected_residue_inverse_product_verified'] is True
            assert len(unit['selected_rows']) == len(set(unit['selected_rows'])) == 2420
            assert len(unit['row_transform_lower_bounds']) == 2560
            residual = read(bound(out, response['full_original_residual_certificate']))
            assert residual['unit_certificate'] == final['unit_minor_and_left_inverse_bound']
            assert residual['original_rows_verified'] == 2560 and residual['original_L_coordinates_per_row'] == 14
            assert residual['full_129_by_20_by_14_original_cleared_identity_used'] is True
            assert residual['inverse_norm_bound_used_not_residual_alone'] is True
            assert residual['exact_original_row_scales_removed_and_weightedly_restored'] is True
            assert residual['inverse_bound_applies_to'] == SCOPE['inverse_bound_applies_to']
            assert len(residual['full_original_residual_row_B_valuation_lower_bounds']) == 2560
            bound(out, residual['residual_numerator'])
            bound(out, residual['last_digit'])
        else:
            assert run['complete'] is False
    summary = {'result': RESULT, 'all_output_bytes_and_original_source_identities_verified': True,
        'full_output_file_count': len(entries), 'complete_mathematical_stage_count': len(math_names),
        'retired_work_receipt_count': retired_count, 'retired_old_work_files': len(retired),
        'carrier_member_count': receipt['carrier_member_count'], 'core_receipt_present': core is not None,
        'actual_original_p41_four_response_balls_certified': bool(final and final['actual_original_p41_four_response_balls_certified']),
        'actual_response_absolute_B_precision': None if final is None else final['actual_response_absolute_B_precision'],
        'complete': bool(final and final['complete']), 'A1_exact_zero_proved': False,
        'actual_Z_computed': False, 'actual_height_computed': False,
        'new_arithmetic_executed_by_verifier': False}
    print('R854_COMPLETE_IO_REVIEW='+json.dumps(summary, sort_keys=True), flush=True)
    return 0 if summary['complete'] else 2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['compute', 'verify'])
    parser.add_argument('--request', type=Path, default=REQUEST)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if hasattr(sys, 'set_int_max_str_digits'):
        sys.set_int_max_str_digits(0)
    if args.mode == 'verify':
        raise SystemExit(verify(args.out))
    item = read(args.request)
    guard(item, args.request)
    raise SystemExit(compute(item, args.out, args.request))


if __name__ == '__main__':
    main()
