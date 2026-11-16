#!/usr/bin/env python3
"""Standard-library transport/verification for the original R856 ideal bases."""

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
REQUEST = TOPIC/'notes/R856-fixed-branch-ideal-bases-public-request.json'
RESULT = 'R856-original-fixed-branch-ideal-bases'
FINAL = 'p41-original-fixed-branch-ideal-bases-certificate.json'
PREFIX = 'R856-'
STAGES = 'R856-stage-manifest.json.gz'
SCOPE = 'complete_two_chart_point_and_fixed_branch_ideal_bases'
MANIFEST = 'full-outputs-manifest.json'
REFERENCE = 'full-outputs-manifest-reference.json'
BUNDLE = 'R856-retained-original-inputs.tar.gz'
INVENTORY = 'R856-original-source-inventory.json'
INPUT_RECEIPT = 'R856-retained-inputs-receipt.json'
TRANSPORT_SHA = 'eec99c9e849c051a8314f00ff594037e962d9bc23e2d2bfaa6334307a3bb5eae'
RANGE_SHA = 'c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c'
BASE = ('result', 'run_id', 'source_commit', 'core_sha256', 'manifest_sha256')
PROOFS = ('proof', 'method', 'finite_RR_proof', 'cusp_proof', 'P0_proof')
META = ('run-receipt.json', 'core-receipt.json', 'public-actions-input.json')
H64 = re.compile(r'[0-9a-f]{64}')
DECIMAL = re.compile(r'-?(0|[1-9][0-9]*)')
EPS = [0]+[1]*144+[2]*127
N, BATCH = 272, 16
FREE = {'file': 'R805-graded-free-basis.json.gz', 'bytes': 11649,
        'sha256': '74311a7a143fafc43a36d1a43f6146e6aa3cb28809a020e3fa1337fdc4e475c9'}
P0_VALUES = 'R837-original-P0-evaluation.json.gz'
V2_VALUES = 'R837-original-V2-P0-evaluation.json.gz'
SOURCE_DEFINITIONS = {
    'R805': {'result': 'R805-original-affine-pencil-free-basis',
             'core_sha256': '730a7d8f51d76d1153386c63f2e082285ada4573a2baf8d87d1825d3ce75b420',
             'certificate': 'p41-original-affine-pencil-free-basis-certificate.json',
             'selected_count': 7},
    'R820': {'result': 'R820-original-cusp-finite-algebra-and-ideals',
             'core_sha256': '25f5582ed0c6dae2cf29d5eb288469067c09d917bfe1f565fb042978ea9b173c',
             'certificate': 'p41-original-cusp-finite-algebra-ideals-certificate.json',
             'selected_count': 554},
    'R837': {'result': 'R837-original-fixed-branch-pencil',
             'core_sha256': '5702b42ee014ab7552e61383e24b738fe5ed48955dfc207ad3d85cae08e8b924',
             'certificate': 'p41-original-fixed-branch-pencil-certificate.json',
             'selected_count': 8},
}


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
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name+'.tmp')
    temp.write_text(json.dumps(value, sort_keys=True, separators=(',', ':'))+'\n', encoding='utf-8')
    temp.replace(path)


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def safe_name(name):
    assert isinstance(name, str) and Path(name).name == name and name not in ('.', '..') and '\\' not in name
    return name


def plain(value):
    row = {k: value[k] for k in ('file', 'bytes', 'sha256')}
    safe_name(row['file'])
    assert isinstance(row['bytes'], int) and row['bytes'] >= 0 and H64.fullmatch(row['sha256'])
    return row


def file_spec(path):
    path = Path(path)
    return {'file': path.name, 'bytes': path.stat().st_size, 'sha256': sha(path)}


def bound(directory, reference):
    reference = plain(reference)
    path = Path(directory)/reference['file']
    assert file_spec(path) == reference, ('changed bytes', reference['file'])
    return path


def topic_path(value):
    value = PurePosixPath(value)
    assert not value.is_absolute() and '..' not in value.parts
    result = (TOPIC/str(value)).resolve()
    assert result.is_relative_to(TOPIC.resolve())
    return result


def identity(source):
    return {k: source[k] for k in BASE}


def source_math_identity(source):
    return {**identity(source), 'configuration_sha256': source['configuration_sha256'],
            'selected_files_sha256': source['selected_files_sha256'],
            'certificate': plain(source['certificate'])}


def load_transport(item):
    path = S/safe_name(item['transport_helper'])
    assert path.name == 'R837_original_branch_pencil_public.py'
    assert sha(path) == item['transport_helper_sha256'] == TRANSPORT_SHA
    assert item['io_helper'] == 'R824_public_original_global_polar_generators.py'
    assert item['io_helper_sha256'] == RANGE_SHA
    module_spec = importlib.util.spec_from_file_location('R856_frozen_R837_transport', path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    module.load_io(item)
    return module


def guard(item, request):
    if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public':
        raise SystemExit('R856 execution belongs to the public repository Actions.')
    assert request.resolve() == REQUEST.resolve()
    assert item['result'] == RESULT and item['p'] == 41 and item['producer_inputs_pending'] is False
    assert item['requested_stage'] == SCOPE
    assert item['core'] == 'R856_original_fixed_branch_ideal_bases.py'
    assert item['wrapper'] == 'R856_original_fixed_branch_ideal_bases_public.py'
    assert sha(S/item['core']) == item['core_sha256'] and sha(__file__) == item['wrapper_sha256']
    assert 1 < item['budget_minutes'] <= 300
    for key in PROOFS:
        assert sha(topic_path(item[key])) == item[key+'_sha256']
    assert sha(REPO/'README.md') == item['readme_sha256']['root']
    assert sha(TOPIC/'README.md') == item['readme_sha256']['topic']
    assert set(item['sources']) == set(SOURCE_DEFINITIONS)
    for label, source in item['sources'].items():
        d = SOURCE_DEFINITIONS[label]
        assert source['result'] == d['result'] and source['core_sha256'] == d['core_sha256']
        assert source['expected_conclusion'] == 'success'
        assert source['selected_file_count'] == d['selected_count']
        assert H64.fullmatch(source['selected_files_sha256']) and H64.fullmatch(source['configuration_sha256'])
        assert source['manifest_bytes'] > 0 and source['manifest_file_count'] > 0
        assert plain(source['certificate'])['file'] == d['certificate']
    assert item['sources']['R805']['transport_source'] == identity(item['sources']['R820'])
    return load_transport(item)


def basic_names(label, source):
    names = {MANIFEST, *META, SOURCE_DEFINITIONS[label]['certificate']}
    if label == 'R805':
        names.update((FREE['file'], 'R805-accepted-pencil.json.gz'))
    elif label == 'R837':
        names.update((source['stage_manifest']['file'], P0_VALUES, V2_VALUES))
    else:
        assert label == 'R820'
        names.update((source['stage_manifest']['file'], 'retained-inputs-receipt.json',
                      source['finite_algebra_interface']['file']))
        names.update(s['file'] for s in source['cusp_indexes'].values())
    return names


def selected_names(label, source, directory):
    names = basic_names(label, source)
    if label == 'R820':
        for chart in ('tau', 'sigma'):
            index = read(Path(directory)/source['cusp_indexes'][chart]['file'])
            assert len(index['Hermite_columns_in_original_basis_order']) == N
            names.update(s['file'] for s in index['Hermite_columns_in_original_basis_order'])
    assert len(names) == SOURCE_DEFINITIONS[label]['selected_count']
    return sorted(names)


def source_review(label, item, directory):
    directory = Path(directory)
    source = item['sources'][label]
    manifest_path = directory/MANIFEST
    assert file_spec(manifest_path) == {'file': MANIFEST, 'bytes': source['manifest_bytes'], 'sha256': source['manifest_sha256']}
    manifest = read(manifest_path)
    assert manifest['result'] == source['result']
    entries = {s['file']: plain(s) for s in manifest['files']}
    assert len(entries) == len(manifest['files']) == source['manifest_file_count']
    entries[MANIFEST] = file_spec(manifest_path)
    names = selected_names(label, source, directory)
    selected = {name: entries[name] for name in names}
    for s in selected.values():
        bound(directory, s)
    assert fingerprint({n: selected[n] for n in sorted(selected)}) == source['selected_files_sha256']
    initial, run, core = (read(directory/n) for n in ('public-actions-input.json', 'run-receipt.json', 'core-receipt.json'))
    assert run['result'] == initial['result'] == core['result'] == source['result']
    assert run['source_commit'] == initial['source_commit'] == source['source_commit']
    assert str(run['workflow_run_id']) == str(source['run_id'])
    assert run['complete'] is True and run['process_exit_code'] == 0 and run.get('error') is None
    assert core['complete'] is True
    assert initial['source_repository'] == 'Rogerhu12/math-research-public'
    assert initial['core_sha256'] == initial['job']['core_sha256'] == core['source_sha256'] == source['core_sha256']
    assert run['core_receipt_sha256'] == selected['core-receipt.json']['sha256']
    assert core['certificate_sha256'] == source['certificate']['sha256']
    cert = read(bound(directory, source['certificate']))
    assert cert['result'] == source['result'] and cert['complete'] is True
    tag = cert['configuration']
    assert tag['result'] == source['result'] and tag['source_sha256'] == source['core_sha256']
    assert fingerprint(tag) == source['configuration_sha256']

    def old_stage(reference):
        s = plain(reference)
        assert selected[s['file']] == s
        d = read(bound(directory, s))
        assert d['complete'] is True and d['configuration'] == tag
        assert d.get('result', tag['result']) == source['result']
        return d

    if label == 'R805':
        assert plain(cert['graded_free_basis_stage']) == FREE == source['free_basis']
        assert plain(cert['pencil_stage']) == source['pencil']
        free = old_stage(FREE); pencil = old_stage(cert['pencil_stage'])
        assert free['degree1_original_indices'] == list(range(2, 146))
        assert len(free['degree2_original_indices']) == len(set(free['degree2_original_indices'])) == 127
        assert free['characteristic_zero_complement_certified'] is True
        assert free['degree_distribution'] == [1, 144, 127] and free['affine_free_module_rank'] == N
        assert cert['actual_pencil_n'] == pencil['n'] == 1
    else:
        assert plain(cert['stage_manifest']) == source['stage_manifest']
        inventory = old_stage(cert['stage_manifest'])
        stages = {s['file']: plain(s) for s in inventory['files']}
        assert len(stages) == len(inventory['files'])
        for n, s in stages.items():
            assert entries[n] == s
        if label == 'R837':
            assert plain(cert['original_P0_evaluation']) == source['P0_values'] == selected[P0_VALUES]
            p0, v2 = old_stage(source['P0_values']), old_stage(source['V2_values'])
            assert p0['value_count'] == 146 and v2['value_count'] == 418
            assert p0['coefficient_basis'] == ['1', 'zeta=(-1+sqrt(-3))/2']
            assert p0['integer_scale_already_in_source'] == '6724'
            assert p0['additional_scale_inserted'] is False
            assert v2['original_integer_scale_already_in_products'] == '45212176'
            assert plain(v2['original_P0_evaluation']) == source['P0_values']
            assert v2['all_418_original_product_recipes_used_without_rescaling'] is True
            for name in (P0_VALUES, V2_VALUES):
                assert selected[name] == stages[name]
        else:
            assert label == 'R820'
            assert cert['normal_basis_rank'] == N and cert['normal_basis_degrees'] == EPS
            assert cert['actual_cusp_colengths'] == {'tau': 20, 'sigma': 20}
            for key in ('original_two_chart_cusp_ideals_computed', 'complete_polynomial_kernels_certified',
                        'same_original_cusp_field_and_two_chart_transitions_verified'):
                assert cert[key] is True
            assert plain(cert['original_finite_algebra_interface']) == source['finite_algebra_interface']
            old_stage(cert['original_finite_algebra_interface'])
            for chart in ('tau', 'sigma'):
                assert plain(cert['two_chart_cusp_ideal_indexes'][chart]) == source['cusp_indexes'][chart]
                index = old_stage(source['cusp_indexes'][chart])
                assert index['chart'] == chart and index['normal_basis_rank'] == N
                assert index['actual_diagonal_degrees'] == [0]*271+[20]
                assert index['actual_total_diagonal_degree'] == index['actual_quotient_dimension_over_Q'] == 20
                for flag in ('all_272_original_relations_verified_in_full_finite_algebra',
                             'canonical_lower_triangular_monic_and_reduced_conditions_verified',
                             'complete_polynomial_kernel_certified_by_inclusion_and_equal_colength'):
                    assert index[flag] is True
                for a, s in enumerate(index['Hermite_columns_in_original_basis_order']):
                    assert plain(s) == stages[s['file']]
                    col = old_stage(s)
                    assert col['kind'] == 'first_dependence' and col['chart'] == chart
                    assert col['normal_basis_index'] == col['exact_original_normal_basis_column'] == a
                    assert col['monic_diagonal_degree'] == (20 if a == 271 else 0)
                    assert col['complete_relation_evaluation_zero_in_all_20_original_coordinates'] is True
            receipt = read(directory/'retained-inputs-receipt.json')
            assert plain(receipt['input_bundle']) == item['sources']['R805']['transport_input_bundle']
            assert receipt['actual_selected_file_count'] == 289
            assert identity(receipt['producer_identities']['R805']) == identity(item['sources']['R805'])
    result = {**identity(source), 'configuration_sha256': source['configuration_sha256'],
              'selected_files_sha256': source['selected_files_sha256'], 'files': selected,
              'certificate': plain(source['certificate']),
              'stage_manifest': plain(source['stage_manifest']) if source.get('stage_manifest') else None}
    return result


def expected_tag(item, sources):
    return {
        'result': RESULT, 'source_sha256': item['core_sha256'], 'p': 41,
        'requested_stage': SCOPE, **{k+'_sha256': item[k+'_sha256'] for k in PROOFS},
        'source_identities': {label: source_math_identity(sources[label]) for label in SOURCE_DEFINITIONS},
        'coefficient_field': 'K=Q(zeta), zeta^2+zeta+1=0; original ordered basis (1,zeta)',
        'exact_arithmetic': 'fractions.Fraction; canonical rational pairs',
        'normal_basis_rank': N, 'normal_basis_degrees': EPS, 'charts': ['tau', 'sigma'],
        'original_R805_free_basis': FREE,
        'fixed_divisor': 'original reduced twenty cusps plus original P0=phi(c0)',
        'new_basis_rule': 'first nonzero original C-column P0 evaluation; exact one-row kernel',
        'output_column_order': 'original 0,...,271 in each chart', 'column_block_size': BATCH,
        'no_old_Fourier_rank_cusp_kernel_or_primitive_computation_repeated': True,
        'only_directories_transport_and_budget_excluded_from_mathematical_identity': True,
    }


def extract_R805(item, retained, r820_directory, r820_archive, entries):
    source = item['sources']['R805']
    receipt = read(r820_directory/'retained-inputs-receipt.json')
    bundle = plain(receipt['input_bundle'])
    assert bundle == source['transport_input_bundle'] == entries[bundle['file']]
    assert source['transport_retained_receipt'] == entries['retained-inputs-receipt.json']
    bundle_path = r820_directory.parent/'R820-original-input-carrier.tar.gz'
    r820_archive.extract_bound(bundle['file'], bundle['sha256'], bundle_path, bundle['bytes'])
    expected = {label+'/'+s['file']: plain(s) for label, refs in receipt['selected_files'].items() for s in refs}
    assert len(expected) == receipt['actual_selected_file_count'] == 289
    wanted = basic_names('R805', source)
    assert len(wanted) == 7
    destination = retained/'R805'; destination.mkdir(parents=True, exist_ok=True)
    actual, extracted = {}, set()
    with tarfile.open(bundle_path, 'r:gz') as stream:
        for member in stream:
            name = PurePosixPath(member.name)
            assert member.isfile() and not member.issym() and not member.islnk()
            assert not name.is_absolute() and '..' not in name.parts and len(name.parts) == 2
            assert member.name in expected and member.name not in actual
            s = expected[member.name]
            assert member.size == s['bytes']
            keep = name.parts[0] == 'R805' and name.name in wanted
            target = destination/name.name if keep else None
            temp = target.with_name(target.name+'.tmp') if keep else None
            output = temp.open('wb') if keep else None
            h, length = hashlib.sha256(), 0
            try:
                with stream.extractfile(member) as source_stream:
                    for block in iter(lambda: source_stream.read(4*1024*1024), b''):
                        length += len(block); h.update(block)
                        if output is not None:
                            output.write(block)
            finally:
                if output is not None:
                    output.close()
            assert length == s['bytes'] and h.hexdigest() == s['sha256']
            actual[member.name] = s
            if keep:
                temp.replace(target); extracted.add(name.name)
    assert actual == expected and extracted == wanted
    assert file_spec(destination/MANIFEST)['sha256'] == source['manifest_sha256']
    return {'original_R820_input_bundle': bundle, 'all_original_carrier_members_hashed': 289,
            'selected_original_R805_members': 7, 'mathematical_producer_not_relabelled': True}


def download_direct(label, item, retained, out, transport):
    assert label in ('R820', 'R837')
    source = item['sources'][label]
    folder = retained/label; folder.mkdir(parents=True, exist_ok=True)
    archive = transport.IO.Archive(source, out.parent/('download-R856-'+label), whole=False)
    try:
        print('R856_SOURCE_START='+label, flush=True)
        archive.extract_bound(MANIFEST, source['manifest_sha256'], folder/MANIFEST, source['manifest_bytes'])
        m = read(folder/MANIFEST)
        assert m['result'] == source['result']
        entries = {s['file']: plain(s) for s in m['files']}
        assert len(entries) == len(m['files']) == source['manifest_file_count']
        assert set(archive.by_name) == set(entries) | {MANIFEST, REFERENCE}
        for n, s in entries.items():
            assert len(archive.by_name[n]) == 1 and archive.by_name[n][0].file_size == s['bytes']
        basic = basic_names(label, source)-{MANIFEST}
        archive.extract_many([(n, entries[n]['sha256'], folder/n, entries[n]['bytes']) for n in sorted(basic)])
        additional = set(selected_names(label, source, folder))-basic-{MANIFEST}
        archive.extract_many([(n, entries[n]['sha256'], folder/n, entries[n]['bytes']) for n in sorted(additional)])
        carrier = extract_R805(item, retained, folder, archive, entries) if label == 'R820' else None
        reviewed = source_review(label, item, folder)
        print('R856_SOURCE_COMPLETE='+json.dumps({'label': label, 'count': len(reviewed['files']),
              'selected_files_sha256': reviewed['selected_files_sha256']}, sort_keys=True), flush=True)
        return reviewed, {'range_transport': archive.receipt(), 'R805_carrier': carrier}
    finally:
        archive.close()


def prepare_sources(item, out, transport, allow_download=True):
    out = Path(out)
    retained = out.parent/'retained-original-R856'; retained.mkdir(parents=True, exist_ok=True)
    if (out/INPUT_RECEIPT).exists() and (out/INVENTORY).exists() and (out/BUNDLE).exists():
        receipt, inventory = read(out/INPUT_RECEIPT), read(out/INVENTORY)
        assert receipt['result'] == inventory['result'] == RESULT
        assert receipt['complete'] is True and inventory['complete'] is True
        assert receipt['sources'] == item['sources']
        bound(out, receipt['source_inventory']); bound(out, receipt['source_bundle'])
        count = transport.unpack_sources(out/BUNDLE, retained, inventory)
        sources = {label: source_review(label, item, retained/label) for label in SOURCE_DEFINITIONS}
        assert sources == inventory['sources'] and count == receipt['minimal_bundle_member_count'] == 569
        return retained, receipt, sources
    assert allow_download, 'The same original input carrier is required for output verification.'
    sources, transfers = {}, {}
    sources['R820'], transfers['R820'] = download_direct('R820', item, retained, out, transport)
    sources['R805'] = source_review('R805', item, retained/'R805')
    sources['R837'], transfers['R837'] = download_direct('R837', item, retained, out, transport)
    inventory = {'result': RESULT, 'complete': True, 'sources': sources,
                 'all_entries_are_unchanged_completed_original_source_bytes': True}
    save(out/INVENTORY, inventory)
    transport.pack_sources(retained, inventory, out/BUNDLE)
    count = sum(len(s['files']) for s in sources.values()); assert count == 569
    receipt = {'result': RESULT, 'complete': True, 'sources': item['sources'],
               'source_inventory': file_spec(out/INVENTORY), 'source_bundle': file_spec(out/BUNDLE),
               'minimal_bundle_member_count': count, 'original_transport': transfers,
               'old_cusp_or_P0_or_Fourier_arithmetic_recomputed': False}
    save(out/INPUT_RECEIPT, receipt)
    print('R856_INPUT_REVIEW='+json.dumps({'selected_original_files': count,
          'source_inventory': receipt['source_inventory'], 'source_bundle': receipt['source_bundle'],
          'new_mathematics_executed_in_source_preparation': False}, sort_keys=True), flush=True)
    return retained, receipt, sources


def stable_job(item):
    return {k: v for k, v in item.items() if k not in
            ('resume', 'budget_minutes', 'readme_sha256', 'rules_last_read_commit', 'wrapper_sha256', 'workflow')}


def restore(item, out, transport):
    source = item.get('resume')
    if source is None:
        return
    assert source['result'] == RESULT and source['core_sha256'] == item['core_sha256']
    folder = out.parent/'resume-R856-metadata'; folder.mkdir(parents=True, exist_ok=True)
    archive = transport.IO.Archive(source, out.parent/'download-R856-resume', whole=False)
    try:
        archive.extract_bound(MANIFEST, source['manifest_sha256'], folder/MANIFEST, source['manifest_bytes'])
        manifest = read(folder/MANIFEST)
        assert manifest['result'] == RESULT
        entries = {s['file']: plain(s) for s in manifest['files']}
        assert len(entries) == len(manifest['files']) == source['manifest_file_count']
        assert set(archive.by_name) == set(entries) | {MANIFEST, REFERENCE}
        for name in ('run-receipt.json', 'core-receipt.json', 'public-actions-input.json', INPUT_RECEIPT, INVENTORY, BUNDLE):
            if name == 'core-receipt.json' and name not in entries:
                continue
            s = entries[name]
            target = out/name if name in (INPUT_RECEIPT, INVENTORY, BUNDLE) else folder/name
            archive.extract_bound(name, s['sha256'], target, s['bytes'])
        run, initial = read(folder/'run-receipt.json'), read(folder/'public-actions-input.json')
        assert run['result'] == initial['result'] == RESULT
        assert run['source_commit'] == initial['source_commit'] == source['source_commit']
        assert str(run['workflow_run_id']) == str(source['run_id'])
        assert initial['core_sha256'] == item['core_sha256']
        assert stable_job(initial['job']) == stable_job(item)
        assert run['process_exit_code'] in source['accepted_process_exit_codes']
        core = None
        if 'core-receipt.json' in entries:
            core = read(folder/'core-receipt.json')
            assert core['result'] == RESULT and core['source_sha256'] == item['core_sha256']
            assert run['core_receipt_sha256'] == entries['core-receipt.json']['sha256']
        else:
            assert run['complete'] is False and run['core_receipt_sha256'] is None
        unused, receipt, reviewed = prepare_sources(item, out, transport, allow_download=False)
        tag = expected_tag(item, reviewed)
        names = sorted(n for n in entries if n.startswith(PREFIX) and n.endswith('.json.gz'))
        archive.extract_many([(n, entries[n]['sha256'], out/n, entries[n]['bytes']) for n in names])
        for n in names:
            value = read(out/n)
            assert value['configuration'] == tag and value['complete'] is True
        success = False
        if FINAL in entries:
            s = entries[FINAL]
            archive.extract_bound(FINAL, s['sha256'], folder/FINAL, s['bytes'])
            final = read(folder/FINAL)
            assert final['result'] == RESULT and final['configuration'] == tag
            # An incomplete FINAL is only a historical receipt; later atomic stages prevail.
            if final['complete'] is True:
                assert run['complete'] is True and run['process_exit_code'] == 0
                assert core is not None and core['complete'] is True and core['certificate_sha256'] == s['sha256']
                assert final['complete_two_chart_fixed_branch_ideals_certified'] is True
                refs = [final[k] for k in ('source_audit', 'original_normal_P0_values', 'stage_manifest')]
                refs += list(final['two_chart_fixed_branch_ideal_indexes'].values())
                refs += list(final['two_chart_point_ideal_bases'].values())
                for ref in refs:
                    assert entries[ref['file']] == plain(ref); bound(out, ref)
                shutil.copyfile(folder/FINAL, out/FINAL); success = True
        save(out/'resume-inheritance-receipt.json', {'result': RESULT, 'complete': True,
            'source_resume': source, 'original_manifest': file_spec(folder/MANIFEST),
            'all_restored_complete_stages': [entries[n] for n in names], 'restored_successful_final': success,
            'range_transport': archive.receipt(), 'completed_original_ideal_blocks_not_recomputed': True})
    finally:
        archive.close()


def output_manifest(out):
    entries = [dict(file_spec(path), included_in_git=False) for path in sorted(out.iterdir())
               if path.is_file() and path.name not in (MANIFEST, REFERENCE)
               and not path.name.endswith(('.tmp', '.download'))]
    save(out/MANIFEST, {'result': RESULT, 'files': entries,
                       'temporary_active_checkpoint_retention_days': 1, 'reproducible_data_in_git_or_release': False})
    save(out/REFERENCE, {'result': RESULT, 'manifest_file': MANIFEST, 'manifest_sha256': sha(out/MANIFEST),
                        'manifest_bytes': (out/MANIFEST).stat().st_size, 'file_count': len(entries)})


def compute(item, out, request, transport):
    out.mkdir(parents=True, exist_ok=True)
    process, exitcode, error, outer_timeout = None, 1, None, False
    try:
        restore(item, out, transport)
        retained, receipt, sources = prepare_sources(item, out, transport)
        expanded = dict(item)
        expanded['sources'] = {label: {**value, 'directory': str((retained/label).resolve())}
                               for label, value in sources.items()}
        for key in PROOFS:
            expanded[key] = str(topic_path(item[key]))
        save(out/'public-actions-expanded-job.json', expanded)
        initial = {'result': RESULT, 'p': 41, 'source_repository': 'Rogerhu12/math-research-public',
            'source_commit': os.environ['GITHUB_SHA'], 'job': item, 'request_sha256': sha(request),
            'driver_sha256': sha(__file__), 'core_sha256': item['core_sha256'],
            **{k+'_sha256': item[k+'_sha256'] for k in PROOFS},
            'transport_helper_sha256': TRANSPORT_SHA, 'io_helper_sha256': RANGE_SHA,
            'workflow_sha256': sha(REPO/item['workflow']),
            'root_readme_sha256': sha(REPO/'README.md'), 'topic_readme_sha256': sha(TOPIC/'README.md'),
            'source_inventory': receipt['source_inventory'],
            'prepared_at_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
            'all_new_mathematics_runs_only_in_separate_public_Actions_core': True}
        save(out/'public-actions-input.json', initial)
        command = [sys.executable, str(S/item['core']), '--config', str(out/'public-actions-expanded-job.json'),
                   '--out', str(out), '--budget-minutes', str(item['budget_minutes'])]
        with (out/'public-actions-run.log').open('w', encoding='utf-8') as log:
            process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
            try:
                exitcode = process.wait(timeout=60*item['budget_minutes']+900)
            except subprocess.TimeoutExpired:
                outer_timeout = True
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=20)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL); process.wait()
                exitcode = 124
    except BaseException as exc:
        error = type(exc).__name__+': '+str(exc)
        traceback.print_exc()
        if process is not None and process.poll() is None:
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.wait(timeout=20)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL); process.wait()
        exitcode = 1
    finally:
        core_path = out/'core-receipt.json'
        core = read(core_path) if core_path.exists() else None
        final = read(out/FINAL) if (out/FINAL).exists() else None
        complete = exitcode == 0 and core is not None and core.get('complete') is True \
            and final is not None and final.get('complete') is True \
            and final.get('complete_two_chart_point_ideals_certified') is True \
            and final.get('complete_two_chart_fixed_branch_ideals_certified') is True
        run = {'result': RESULT, 'p': 41, 'complete': complete, 'process_exit_code': exitcode, 'error': error,
               'core_receipt_sha256': sha(core_path) if core_path.exists() else None,
               'source_commit': os.environ.get('GITHUB_SHA'), 'workflow_run_id': os.environ.get('GITHUB_RUN_ID'),
               'workflow_attempt': os.environ.get('GITHUB_RUN_ATTEMPT'),
               'execution_environment': 'public-repository-github-actions', 'outer_timeout': outer_timeout,
               'finished_at_utc': dt.datetime.now(dt.timezone.utc).isoformat()}
        save(out/'run-receipt.json', run); output_manifest(out)
        print('R856_RUN_RECEIPT='+json.dumps(run, sort_keys=True), flush=True)
    return exitcode


def rational_shape(value):
    assert isinstance(value, list) and len(value) == 2
    assert all(isinstance(x, str) and DECIMAL.fullmatch(x) for x in value)
    assert int(value[1]) > 0


def field_shape(value):
    assert isinstance(value, list) and len(value) == 2
    for q in value:
        rational_shape(q)


def column_shape(terms):
    positions = set()
    for term in terms:
        row, power = term['normal_basis_row'], term['power']
        assert isinstance(row, int) and 0 <= row < N
        assert isinstance(power, int) and 0 <= power <= 21
        assert (row, power) not in positions
        positions.add((row, power)); field_shape(term['coefficient_K_1_zeta'])


def verify(item, out, request, transport):
    manifest = read(out/MANIFEST)
    assert manifest['result'] == RESULT
    entries = {s['file']: plain(s) for s in manifest['files']}
    assert len(entries) == len(manifest['files'])
    for s in entries.values():
        bound(out, s)
    ref = read(out/REFERENCE)
    assert ref['result'] == RESULT and ref['manifest_sha256'] == sha(out/MANIFEST)
    assert ref['manifest_bytes'] == (out/MANIFEST).stat().st_size and ref['file_count'] == len(entries)
    run = read(out/'run-receipt.json')
    if run['complete'] is not True:
        print('R856_INCOMPLETE_IO_REVIEW='+json.dumps({'run': run, 'manifest_files': len(entries),
              'partial_stages_not_claimed_as_complete_two_chart_ideals': True}, sort_keys=True), flush=True)
        return 2
    retained, receipt, sources = prepare_sources(item, out, transport, allow_download=False)
    initial, core, final = (read(out/n) for n in ('public-actions-input.json', 'core-receipt.json', FINAL))
    assert initial['job'] == item and initial['request_sha256'] == sha(request)
    assert initial['driver_sha256'] == sha(__file__) and initial['core_sha256'] == item['core_sha256']
    assert initial['source_commit'] == run['source_commit']
    assert core['result'] == final['result'] == RESULT and core['complete'] is True and final['complete'] is True
    assert core['source_sha256'] == item['core_sha256'] and run['process_exit_code'] == 0
    assert run['core_receipt_sha256'] == entries['core-receipt.json']['sha256']
    assert core['certificate_sha256'] == entries[FINAL]['sha256']
    tag = expected_tag(item, sources)
    assert final['configuration'] == tag and core['configuration_sha256'] == fingerprint(tag)
    assert final['completed_scope'] == SCOPE
    assert final['normal_basis_rank'] == N and final['normal_basis_degrees'] == EPS
    assert final['actual_fixed_branch_colengths'] == core['actual_fixed_branch_colengths'] == {'tau': 21, 'sigma': 21}
    assert final['actual_point_colengths'] == {'tau': 1, 'sigma': 1}
    for flag in ('complete_two_chart_point_ideals_certified', 'complete_two_chart_fixed_branch_ideals_certified'):
        assert final[flag] is True and core[flag] is True
    for flag in ('original_P0_normal_values_certified', 'same_original_global_fixed_branch_ideal_on_both_charts',
                 'all_original_scales_and_normal_basis_orders_preserved'):
        assert final[flag] is True
    for flag in ('old_cusp_kernel_or_Fourier_or_primitive_arithmetic_recomputed', 'new_B_or_D_normal_coordinates_computed',
                 'new_Gamma_or_multiplication_table_computed', 'actual_eta_or_height_computed'):
        assert final[flag] is False
    inventory = read(bound(out, final['stage_manifest']))
    assert plain(final['stage_manifest']) == entries[STAGES]
    assert inventory['configuration'] == tag and inventory['complete'] is True
    stages = {s['file']: plain(s) for s in inventory['files']}
    assert len(stages) == len(inventory['files']) == 42
    actual_names = {n for n in entries if n.startswith(PREFIX) and n.endswith('.json.gz') and n != STAGES}
    assert actual_names == set(stages)
    for n, s in stages.items():
        assert entries[n] == s
        d = read(bound(out, s))
        assert d['configuration'] == tag and d['result'] == RESULT and d['complete'] is True

    def stage(reference):
        s = plain(reference)
        assert stages[s['file']] == s
        return read(bound(out, s))

    audit = stage(final['source_audit'])
    assert audit['source_identities'] == tag['source_identities']
    assert audit['source_file_counts'] == {'R805': 7, 'R820': 554, 'R837': 8}
    assert audit['original_free_basis'] == FREE
    assert audit['original_P0_values'] == sources['R837']['files'][P0_VALUES]
    assert audit['original_V2_P0_values'] == sources['R837']['files'][V2_VALUES]
    for flag in ('all_selected_original_bytes_and_tags_verified',
                 'all_127_degree2_sources_matched_to_original_V2_values',
                 'old_complete_cusp_kernels_reused_without_arithmetic'):
        assert audit[flag] is True
    normal = stage(final['original_normal_P0_values'])
    assert normal['source_P0_values'] == audit['original_P0_values']
    assert normal['source_V2_P0_values'] == audit['original_V2_P0_values']
    assert normal['source_free_basis'] == FREE and normal['normal_basis_degrees'] == EPS
    assert len(normal['degree2_original_indices']) == len(set(normal['degree2_original_indices'])) == 127
    assert normal['original_82_scales_already_in_source'] == {'V1': '6724', 'V2': '45212176'}
    assert normal['additional_scale_inserted'] is False
    for flag in ('original_P0_in_both_charts_verified', 'all_original_ratio_multiply_backs_verified',
                 'all_272_two_chart_value_transitions_verified'):
        assert normal[flag] is True
    for chart in ('tau', 'sigma'):
        field_shape(normal['chart_base_values_K_1_zeta'][chart])
        assert len(normal['normal_basis_values_K_1_zeta'][chart]) == N
        for value in normal['normal_basis_values_K_1_zeta'][chart]:
            field_shape(value)
        point_spec = final['two_chart_point_ideal_bases'][chart]
        point = stage(point_spec)
        assert point['chart'] == chart and point['source_normal_values'] == final['original_normal_P0_values']
        assert point['actual_colength_over_K'] == 1
        assert point['all_272_original_point_evaluations_zero'] is True
        assert point['complete_original_P0_evaluation_kernel_certified'] is True
        assert len(point['columns']) == N and len(point['actual_polynomial_determinant_K_1_zeta']) == 2
        for a, col in enumerate(point['columns']):
            assert col['column_index'] == a; column_shape(col['column_terms'])
        index = stage(final['two_chart_fixed_branch_ideal_indexes'][chart])
        assert index['chart'] == chart and index['normal_basis_rank'] == N and index['normal_basis_degrees'] == EPS
        assert index['column_count'] == N and index['actual_colength_over_K'] == 21
        assert index['complete_point_ideal_basis'] == point_spec
        assert index['source_normal_values'] == final['original_normal_P0_values']
        assert index['original_C_index'] == item['sources']['R820']['cusp_indexes'][chart]
        for flag in ('complete_fixed_branch_ideal_certified', 'ideal_equals_original_C_intersect_P0',
                     'ideal_equals_original_C_times_P0', 'all_272_source_column_multiply_backs_verified',
                     'all_272_original_P0_evaluations_zero',
                     'determinant_certified_by_original_triangular_C_and_explicit_column_transform'):
            assert index[flag] is True
        assert index['new_272_by_272_determinant_or_Hermite_computed'] is False
        assert len(index['source_C_determinant_K_1_zeta']) == 21
        assert len(index['exact_change_of_basis_determinant_K_1_zeta']) == 2
        assert len(index['actual_polynomial_determinant_K_1_zeta']) == 22
        for key in ('source_C_determinant_K_1_zeta', 'exact_change_of_basis_determinant_K_1_zeta',
                    'actual_polynomial_determinant_K_1_zeta'):
            for value in index[key]:
                field_shape(value)
        evaluation = stage(index['source_cusp_evaluation'])
        assert evaluation['chart'] == chart and evaluation['evaluation_row_rank'] == 1
        assert evaluation['original_C_index'] == index['original_C_index']
        assert evaluation['original_normal_values'] == final['original_normal_P0_values']
        pivot = evaluation['first_nonzero_column']
        assert isinstance(pivot, int) and 0 <= pivot < N and index['actual_pivot_column'] == pivot
        for flag in ('exact_nonzero_pivot_and_inverse_multiply_back_verified', 'all_ratio_multiply_backs_verified',
                     'original_P0_disjoint_from_original_cusp_support_certified'):
            assert evaluation[flag] is True
        assert len(evaluation['C_column_P0_values_K_1_zeta']) == len(evaluation['ratios_to_pivot_K_1_zeta']) == N
        for value in evaluation['C_column_P0_values_K_1_zeta']+evaluation['ratios_to_pivot_K_1_zeta']:
            field_shape(value)
        old_index = read(retained/'R820'/index['original_C_index']['file'])
        old_columns = old_index['Hermite_columns_in_original_basis_order']
        assert len(index['column_groups']) == 17
        for first, group_spec in zip(range(0, N, BATCH), index['column_groups']):
            group = stage(group_spec); stop = min(N, first+BATCH)
            assert group['chart'] == chart and group['first'] == first and group['stop'] == stop
            assert group['pivot_column'] == pivot
            assert group['original_C_index'] == index['original_C_index']
            assert group['source_normal_values'] == final['original_normal_P0_values']
            assert group['source_cusp_evaluation'] == index['source_cusp_evaluation']
            for flag in ('all_source_column_multiply_backs_verified', 'all_new_original_P0_evaluations_zero',
                         'complete_block_in_original_order'):
                assert group[flag] is True
            assert len(group['columns']) == stop-first
            for a, col in zip(range(first, stop), group['columns']):
                assert col['column_index'] == a
                assert col['source_C_column'] == plain(old_columns[a])
                assert col['source_C_pivot_column'] == plain(old_columns[pivot])
                assert 1 <= len(col['source_change_of_basis_terms']) <= 2
                for term in col['source_change_of_basis_terms']:
                    assert term['source_C_column'] in (a, pivot) and term['power'] in (0, 1)
                    field_shape(term['coefficient_K_1_zeta'])
                column_shape(col['column_terms'])
    print('R856_COMPLETE_IO_REVIEW='+json.dumps({'result': RESULT, 'certificate': entries[FINAL],
        'complete_math_stages': len(stages), 'manifest_files': len(entries), 'stage_manifest': final['stage_manifest'],
        'source_inventory': receipt['source_inventory'], 'source_bundle': receipt['source_bundle'],
        'selected_original_files': 569, 'actual_fixed_branch_colengths': final['actual_fixed_branch_colengths'],
        'actual_pivots': {c: stage(final['two_chart_fixed_branch_ideal_indexes'][c])['actual_pivot_column'] for c in ('tau', 'sigma')},
        'complete_two_chart_fixed_branch_ideals_certified': True, 'seconds': final['seconds'],
        'all_output_and_selected_source_bytes_verified': True, 'mathematics_reexecuted_by_wrapper': False}, sort_keys=True), flush=True)
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True); parser.add_argument('--verify', action='store_true')
    args = parser.parse_args()
    item = read(REQUEST); transport = guard(item, REQUEST)
    return verify(item, args.output, REQUEST, transport) if args.verify else compute(item, args.output, REQUEST, transport)


if __name__ == '__main__':
    sys.set_int_max_str_digits(0)
    raise SystemExit(main())
