#!/usr/bin/env python3
"""Source-bound standard-library runner for the original c0 first-jet core."""
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
REQUEST = TOPIC/'notes/R803-c0-Hodge-jets-public-request.json'
RESULT = 'R803-original-c0-Hodge-jets-and-comparison-leading-coefficients'
FINAL = 'p41-original-c0-Hodge-jets-and-comparison-leading-coefficients-certificate.json'
PREFIX = 'R803-c0-'
MANIFEST = 'full-outputs-manifest.json'
REFERENCE = 'full-outputs-manifest-reference.json'
INVENTORY = PREFIX+'original-source-inventory.json'
BUNDLE = PREFIX+'retained-original-inputs.tar.gz'
RECEIPT = PREFIX+'retained-inputs-receipt.json'
HELPER = 'R824_public_original_global_polar_generators.py'
HELPER_SHA = 'c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c'
FIELD_BASIS = 'b^0..b^6,s*b^0..s*b^6; s=1+2*zeta; original b'
K_BASIS = ['1', 's=1+2*zeta; s^2=-3']
LABELS = ['R803', 'R837', 'R791']
BASE = ['result', 'run_id', 'source_commit', 'core_sha256', 'manifest_sha256',
        'configuration_sha256', 'certificate_name', 'selected_files_sha256']
SCOPE = {
    'p': 41, 'original_point_on_X': 'c0', 'original_point_on_Y': 'P0=phi(c0)',
    'original_coarse_parameter': 't=a^3', 'first_jet_order': 1,
    'original_target': 'C:y^2=x^3+b; omega_C=dx/(2*y)',
    'M6_dimension': 694, 'original_M6_integer_scale': '304006671424',
    'original_regular_Phi_integer_scale': '6724',
    'original_M6_rows_used': [690, 691, 692, 693],
    'original_Phi_indices_used': [0, 73],
    'original_U_indices': [0, 1, 2, 3, 4, 5],
    'coefficient_field_basis': FIELD_BASIS,
    'relative_norm_degree': 7, 'relative_norm_target_basis': K_BASIS,
    'comparison_indices': [1, 2, 3, 4, 5],
    'leading_constants_representation': 'exact integer-power DAG of actual original norms',
    'no_cubic_root_chosen': True,
    'no_global_A_B_or_Fourier_or_period_or_CM_torsion_recomputed': True,
}
TRUE_FLAGS = [
    'all_six_original_U_over_E6_values_and_first_jets_computed',
    'all_six_original_lambda_cubes_and_logarithmic_derivatives_computed',
    'all_six_true_relative_norms_and_traces_computed',
    'all_five_original_comparison_leading_constants_DAG_and_unit_jets_computed',
    'all_original_nonzero_values_and_division_denominators_checked',
    'original_1722_82_and_108_normalizations_preserved',
    'original_pq_eta_directions_and_true_norm_constants_preserved',
]
FALSE_FLAGS = [
    'large_integer_powers_of_leading_constants_expanded',
    'cubic_root_or_new_CM_period_normalization_chosen',
    'original_global_A_B_Fourier_Hom_periods_or_torsion_recomputed',
    'global_Picard_rigidification_or_height_computed',
    'actual_eta_zero_or_uniformity_proved',
]
H64 = re.compile(r'[0-9a-f]{64}')
IO = None


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


def plain(row):
    value = {key: row[key] for key in ('file', 'bytes', 'sha256')}
    safe_name(value['file'])
    assert isinstance(value['bytes'], int) and value['bytes'] >= 0 and H64.fullmatch(value['sha256'])
    return value


def file_spec(path):
    path = Path(path)
    return {'file': path.name, 'bytes': path.stat().st_size, 'sha256': sha(path)}


def bound(folder, row):
    row = plain(row)
    path = Path(folder)/row['file']
    assert file_spec(path) == row
    return path


def source_identity(source):
    value = {key: source[key] for key in BASE}
    value['files'] = {name: plain(row) for name, row in sorted(source['files'].items())}
    return value


def topic_path(name):
    path = PurePosixPath(name)
    assert not path.is_absolute() and '..' not in path.parts
    result = (TOPIC/str(path)).resolve()
    assert result.is_relative_to(TOPIC.resolve())
    return result


def load_helper(item, helper_dir=None):
    global IO
    path = (S if helper_dir is None else Path(helper_dir))/HELPER
    assert item['io_helper_sha256'] == HELPER_SHA and sha(path) == HELPER_SHA
    spec = importlib.util.spec_from_file_location('original_c0_stdlib_Range_IO', path)
    IO = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(IO)


def guard(item, path):
    assert os.environ.get('GITHUB_ACTIONS') == 'true'
    assert os.environ.get('GITHUB_REPOSITORY') == 'Rogerhu12/math-research-public'
    assert path.resolve() == REQUEST.resolve()
    assert item['result'] == RESULT and item['p'] == 41 and item['producer_inputs_pending'] is False
    assert item['core'] == 'R803_original_c0_Hodge_jets.py'
    assert item['wrapper'] == 'R803_original_c0_Hodge_jets_public.py'
    assert sha(S/item['core']) == item['core_sha256'] and sha(__file__) == item['wrapper_sha256']
    assert 0 < item['budget_minutes'] <= 300
    for key in ('proof', 'method'):
        assert sha(topic_path(item[key])) == item[key+'_sha256']
    assert sha(REPO/'README.md') == item['readme_sha256']['root']
    assert sha(TOPIC/'README.md') == item['readme_sha256']['topic']
    assert set(item['sources']) == set(LABELS)
    assert item['selected_original_file_count'] == 35
    for label, source in item['sources'].items():
        for key in ('core_sha256', 'manifest_sha256', 'configuration_sha256', 'selected_files_sha256'):
            assert H64.fullmatch(source[key])
        assert source['artifact_id'] > 0 and source['archive_bytes'] > 0
        assert H64.fullmatch(source['archive_sha256'])
        assert source['expected_conclusion'] == 'success'
        assert source['accepted_process_exit_codes'] == [0]
        assert source['selected_file_count'] == {'R803': 19, 'R837': 9, 'R791': 7}[label]
    load_helper(item)


def review_source(label, source, folder):
    folder = Path(folder)
    files = {name: plain(value) for name, value in source['files'].items()}
    assert len(files) == source['selected_file_count']
    assert fingerprint([files[name] for name in sorted(files)]) == source['selected_files_sha256']
    for name, value in files.items():
        assert name == value['file']
        bound(folder, value)
    assert files[MANIFEST] == {'file': MANIFEST, 'bytes': source['manifest_bytes'], 'sha256': source['manifest_sha256']}
    manifest = read(folder/MANIFEST)
    assert manifest['result'] == source['result']
    entries = {row['file']: plain(row) for row in manifest['files']}
    assert len(entries) == len(manifest['files']) == source['manifest_file_count']
    for name, value in files.items():
        if name != MANIFEST:
            assert entries[name] == value
    run, core, public = (read(folder/name) for name in ('run-receipt.json', 'core-receipt.json', 'public-actions-input.json'))
    assert run['result'] == core['result'] == public['result'] == source['result']
    assert run['source_commit'] == public['source_commit'] == source['source_commit']
    assert str(run['workflow_run_id']) == str(source['run_id'])
    assert run['process_exit_code'] == 0 and run['complete'] is True and run['error'] is None
    assert core['complete'] is True and core['source_sha256'] == source['core_sha256']
    assert public['source_repository'] == 'Rogerhu12/math-research-public'
    assert public['driver_sha256'] == source['wrapper_sha256']
    assert public['job']['core_sha256'] == source['core_sha256']
    if label == 'R791':
        assert 'core_receipt_sha256' not in run and 'core_sha256' not in public
    else:
        assert public['core_sha256'] == source['core_sha256']
        assert run['core_receipt_sha256'] == files['core-receipt.json']['sha256']
    cert = read(folder/source['certificate_name'])
    assert cert['result'] == source['result'] and cert['complete'] is True
    assert files[source['certificate_name']]['sha256'] == core['certificate_sha256']
    tag = cert['configuration']
    assert tag['result'] == source['result'] and tag['source_sha256'] == source['core_sha256']
    assert fingerprint(tag) == source['configuration_sha256']
    for name in files:
        if name.endswith('.json.gz'):
            value = read(folder/name)
            assert value['complete'] is True and value['configuration'] == tag
            if 'result' in value:
                assert value['result'] == source['result']
    if label == 'R803':
        assert cert['M6_dimension'] == 694 and cert['basis_integer_scale'] == '304006671424'
        assert cert['all84_rational_RHS_columns_verified_in_all1680_original_rows'] is True
        for j in range(6):
            assert plain(cert['coordinate_stages'][str(j)]) == files[cert['coordinate_stages'][str(j)]['file']]
    elif label == 'R837':
        assert cert['original_P0_evaluation_certified'] is True
        value = read(bound(folder, cert['original_P0_evaluation']))
        assert value['original_target_point'] == 'P0=phi(c0)'
        assert value['integer_scale_already_in_source'] == '6724'
        assert value['all_146_reflected_outputs_verified'] is True
    else:
        value = read(folder/'R791-original-real-descent-and-eta-basis-inputs.json.gz')
        assert value['all_original_F0_directions_covered'] is True
        assert [row['j'] for row in value['degree_zero_basis']] == [1, 2, 3, 4, 5]
    return source_identity(source)


def review_all(item, retained):
    result = {label: review_source(label, item['sources'][label], Path(retained)/label) for label in LABELS}
    assert fingerprint(result) == item['expanded_sources_sha256']
    assert sum(len(value['files']) for value in result.values()) == item['selected_original_file_count']
    return result


def fetch_source(label, source, retained):
    folder = Path(retained)/label
    folder.mkdir(parents=True, exist_ok=True)
    print('C0_SOURCE_IO_START='+json.dumps({'label': label, 'run_id': source['run_id']}, sort_keys=True), flush=True)
    archive = IO.Archive(source, Path(retained).parent/('download-c0-'+label), whole=False)
    try:
        archive.extract_bound(MANIFEST, source['manifest_sha256'], folder/MANIFEST, source['manifest_bytes'])
        manifest = read(folder/MANIFEST)
        assert manifest['result'] == source['result']
        entries = {row['file']: plain(row) for row in manifest['files']}
        assert len(entries) == len(manifest['files']) == source['manifest_file_count']
        expected = set(entries)|{MANIFEST, REFERENCE}
        if label == 'R791':
            assert source['run_id'] == '43686308194'
            assert source['source_commit'] == 'f945ef5d5aee4d8222dc791e39a0709b661cebbc'
            assert source['manifest_sha256'] == '4eeb9ba12e203f41d2525325bf1ae207b46baa2b88ad88b31de2c3ac58a317fc'
            assert len(entries) == 9
            expected = set(entries)|{MANIFEST}
        assert set(archive.by_name) == expected
        for name, row in entries.items():
            assert len(archive.by_name[name]) == 1 and archive.by_name[name][0].file_size == row['bytes']
        requests = []
        for name, spec in source['files'].items():
            spec = plain(spec)
            if name == MANIFEST:
                assert file_spec(folder/name) == spec
            else:
                assert entries[name] == spec
                requests.append((name, spec['sha256'], folder/name, spec['bytes']))
        archive.extract_many(requests)
        review_source(label, source, folder)
        return archive.receipt()
    finally:
        archive.close()


def pack(retained, sources, target):
    target = Path(target)
    temporary = target.with_name(target.name+'.tmp')
    with temporary.open('wb') as raw:
        with gzip.GzipFile(fileobj=raw, mode='wb', mtime=0, filename='') as compressed:
            with tarfile.open(fileobj=compressed, mode='w|') as archive:
                for label in LABELS:
                    for name, spec in sorted(sources[label]['files'].items()):
                        path = bound(Path(retained)/label, spec)
                        info = archive.gettarinfo(str(path), arcname=label+'/'+name)
                        info.uid = info.gid = info.mtime = 0
                        info.uname = info.gname = ''
                        with path.open('rb') as stream:
                            archive.addfile(info, stream)
    temporary.replace(target)


def unpack(bundle, retained, sources):
    wanted = {(label, name): plain(spec) for label in LABELS for name, spec in sources[label]['files'].items()}
    seen = set()
    with tarfile.open(bundle, 'r|gz') as archive:
        for member in archive:
            if member.isdir():
                continue
            path = PurePosixPath(member.name)
            assert member.isfile() and not path.is_absolute() and '..' not in path.parts and len(path.parts) == 2
            key = tuple(path.parts)
            assert key in wanted and key not in seen
            seen.add(key)
            spec = wanted[key]
            assert member.size == spec['bytes']
            target = Path(retained)/key[0]/key[1]
            target.parent.mkdir(parents=True, exist_ok=True)
            temporary = target.with_name(target.name+'.download')
            h, count = hashlib.sha256(), 0
            with archive.extractfile(member) as stream, temporary.open('wb') as sink:
                for block in iter(lambda: stream.read(4*1024*1024), b''):
                    sink.write(block)
                    h.update(block)
                    count += len(block)
            assert count == spec['bytes'] and h.hexdigest() == spec['sha256']
            if target.exists():
                bound(target.parent, spec)
                temporary.unlink()
            else:
                temporary.replace(target)
    assert seen == set(wanted)
    return len(seen)


def prepare(item, out, allow_download=True):
    out = Path(out)
    retained = out.parent/'retained-original-c0-Hodge'
    retained.mkdir(parents=True, exist_ok=True)
    if all((out/name).exists() for name in (INVENTORY, RECEIPT, BUNDLE)):
        inventory, receipt = read(out/INVENTORY), read(out/RECEIPT)
        assert inventory['result'] == receipt['result'] == RESULT
        assert inventory['complete'] is True and receipt['complete'] is True
        assert receipt['source_requests'] == item['sources']
        assert receipt['expanded_sources_sha256'] == item['expanded_sources_sha256']
        bound(out, receipt['source_inventory'])
        bound(out, receipt['source_bundle'])
        count = unpack(out/BUNDLE, retained, inventory['sources'])
        reviewed = review_all(item, retained)
        assert reviewed == inventory['sources'] and count == item['selected_original_file_count']
        return retained, receipt, reviewed
    assert allow_download, 'Continuation lost its original c0 source carrier.'
    transport = {label: fetch_source(label, item['sources'][label], retained) for label in LABELS}
    reviewed = review_all(item, retained)
    save(out/INVENTORY, {'result': RESULT, 'complete': True, 'sources': reviewed,
        'all_members_are_unchanged_original_producer_bytes': True})
    pack(retained, reviewed, out/BUNDLE)
    receipt = {'result': RESULT, 'complete': True, 'source_requests': item['sources'],
        'source_inventory': file_spec(out/INVENTORY), 'source_bundle': file_spec(out/BUNDLE),
        'expanded_sources_sha256': item['expanded_sources_sha256'],
        'minimal_bundle_member_count': item['selected_original_file_count'],
        'range_transport': transport, 'old_mathematical_arithmetic_recomputed': False}
    save(out/RECEIPT, receipt)
    print('C0_SOURCE_IO_COMPLETE='+json.dumps({'source_inventory': receipt['source_inventory'],
        'source_bundle': receipt['source_bundle'], 'source_file_count': item['selected_original_file_count'],
        'new_mathematics_executed': False}, sort_keys=True), flush=True)
    return retained, receipt, reviewed


def expected_tag(item):
    return {'result': RESULT, 'source_sha256': item['core_sha256'],
        'arithmetic': 'Python exact Fraction, original Q(b,s) quotient and K determinant',
        'proof_sha256': item['proof_sha256'], 'method_sha256': item['method_sha256'],
        'sources': {label: source_identity(item['sources'][label]) for label in LABELS}, **SCOPE}


def stable_job(item):
    return {key: value for key, value in item.items() if key not in
            ('resume', 'budget_minutes', 'readme_sha256', 'rules_last_read_commit')}


def restore(item, out):
    previous = item.get('resume')
    if previous is None:
        return
    assert previous['result'] == RESULT and previous['core_sha256'] == item['core_sha256']
    out = Path(out)
    meta = out.parent/'resume-c0-metadata'
    meta.mkdir(parents=True, exist_ok=True)
    archive = IO.Archive(previous, out.parent/'download-c0-resume', whole=False)
    try:
        archive.extract_bound(MANIFEST, previous['manifest_sha256'], meta/MANIFEST, previous['manifest_bytes'])
        manifest = read(meta/MANIFEST)
        assert manifest['result'] == RESULT
        entries = {row['file']: plain(row) for row in manifest['files']}
        assert len(entries) == len(manifest['files']) == previous['manifest_file_count']
        names = ['public-actions-input.json', 'run-receipt.json', INVENTORY, RECEIPT, BUNDLE]
        if 'core-receipt.json' in entries:
            names.append('core-receipt.json')
        if FINAL in entries:
            names.append(FINAL)
        for name in names:
            spec = entries[name]
            target = out/name if name in (INVENTORY, RECEIPT, BUNDLE) else meta/name
            archive.extract_bound(name, spec['sha256'], target, spec['bytes'])
        initial, run = read(meta/'public-actions-input.json'), read(meta/'run-receipt.json')
        assert initial['result'] == run['result'] == RESULT
        assert initial['source_commit'] == run['source_commit'] == previous['source_commit']
        assert str(run['workflow_run_id']) == str(previous['run_id'])
        assert stable_job(initial['job']) == stable_job(item)
        assert initial['core_sha256'] == item['core_sha256']
        assert run['process_exit_code'] in previous['accepted_process_exit_codes']
        if 'core-receipt.json' in entries:
            core = read(meta/'core-receipt.json')
            assert core['source_sha256'] == item['core_sha256']
            assert run['core_receipt_sha256'] == entries['core-receipt.json']['sha256']
        else:
            assert run['core_receipt_sha256'] is None and run['complete'] is False
        prepare(item, out, allow_download=False)
        tag = expected_tag(item)
        requests = []
        for name, spec in entries.items():
            if name.startswith(PREFIX) and name.endswith('.json.gz'):
                requests.append((name, spec['sha256'], out/name, spec['bytes']))
        archive.extract_many(requests)
        for name, _, _, _ in requests:
            value = read(out/name)
            assert value['result'] == RESULT and value['configuration'] == tag and value['complete'] is True
        if FINAL in entries:
            final = read(meta/FINAL)
            assert final['result'] == RESULT and final['configuration'] == tag
            if final['complete'] is True:
                assert run['complete'] is True and run['process_exit_code'] == 0
                for spec in read(bound(out, final['stage_manifest']))['files']:
                    bound(out, spec)
                shutil.copyfile(meta/FINAL, out/FINAL)
        save(out/'resume-receipt.json', {'result': RESULT, 'producer': previous,
            'same_core_and_all_source_bound_completed_stages_preserved': True,
            'restored_complete_stage_count': len(requests),
            'incomplete_final_not_used_to_override_newer_atomic_stages': True,
            'transport': archive.receipt(), 'old_arithmetic_recomputed': False})
    finally:
        archive.close()


def output_manifest(out):
    out = Path(out)
    files = [dict(file_spec(path), included_in_git=False) for path in sorted(out.iterdir())
             if path.is_file() and path.name not in (MANIFEST, REFERENCE)
             and not path.name.endswith(('.tmp', '.download', '.partial'))]
    save(out/MANIFEST, {'result': RESULT, 'files': files,
        'temporary_active_checkpoint_artifact': True, 'temporary_active_checkpoint_retention_days': 1,
        'reproducible_outputs_saved_in_repository_or_release': False})
    save(out/REFERENCE, {'result': RESULT, 'manifest_file': MANIFEST,
        'manifest_sha256': sha(out/MANIFEST), 'manifest_bytes': (out/MANIFEST).stat().st_size,
        'file_count': len(files), 'automatic_git_or_release_publication': False})


def compute(item, out, request_path):
    out.mkdir(parents=True, exist_ok=True)
    code, error, outer_timeout = 1, None, False
    try:
        restore(item, out)
        retained, receipt, reviewed = prepare(item, out)
        expanded = dict(item)
        expanded['sources'] = {label: {**item['sources'][label], 'directory': str((retained/label).resolve())}
                               for label in LABELS}
        for key in ('proof', 'method'):
            expanded[key+'_absolute_path'] = str(topic_path(item[key]))
        save(out/'public-actions-expanded-job.json', expanded)
        save(out/'public-actions-input.json', {'result': RESULT, 'p': 41,
            'source_repository': 'Rogerhu12/math-research-public', 'source_commit': os.environ['GITHUB_SHA'],
            'job': item, 'request_sha256': sha(request_path), 'driver_sha256': sha(__file__),
            'core_sha256': item['core_sha256'], 'proof_sha256': item['proof_sha256'],
            'method_sha256': item['method_sha256'], 'io_helper_sha256': HELPER_SHA,
            'workflow_sha256': sha(REPO/item['workflow']),
            'root_readme_sha256': sha(REPO/'README.md'), 'topic_readme_sha256': sha(TOPIC/'README.md'),
            'source_inventory': receipt['source_inventory'],
            'prepared_at_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
            'all_new_mathematical_arithmetic_runs_only_in_public_Actions_core': True})
        command = [sys.executable, '-u', str(S/item['core']), '--config', str(out/'public-actions-expanded-job.json'),
                   '--out', str(out), '--budget-minutes', str(item['budget_minutes'])]
        with (out/'public-actions-run.log').open('w', encoding='utf-8') as log:
            process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
            try:
                code = process.wait(timeout=item['budget_minutes']*60+120)
            except subprocess.TimeoutExpired:
                outer_timeout = True
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=20)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                code = 124
    except BaseException as exception:
        error = {'type': type(exception).__name__, 'message': str(exception)}
        traceback.print_exc()
        print(json.dumps({'wrapper_error': error}, sort_keys=True), flush=True)
    finally:
        core = read(out/'core-receipt.json') if (out/'core-receipt.json').exists() else None
        final = read(out/FINAL) if (out/FINAL).exists() else None
        complete = bool(code == 0 and error is None and core and core['complete'] and final and final['complete'])
        save(out/'run-receipt.json', {'result': RESULT, 'p': 41,
            'source_commit': os.environ.get('GITHUB_SHA'), 'workflow_run_id': os.environ.get('GITHUB_RUN_ID'),
            'workflow_attempt': os.environ.get('GITHUB_RUN_ATTEMPT'), 'process_exit_code': code,
            'complete': complete, 'error': error, 'outer_timeout': outer_timeout,
            'core_receipt_sha256': sha(out/'core-receipt.json') if core else None,
            'finished_at_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
            'original_global_A_B_Fourier_Hom_periods_or_torsion_recomputed': False,
            'global_Picard_rigidification_or_height_computed': False})
        output_manifest(out)
    return 0 if complete else code or 1


def rational_shape(value):
    assert isinstance(value, list) and len(value) == 2
    assert all(isinstance(x, str) for x in value) and value[1] not in ('0', '-0')


def coordinate_shape(value, length):
    assert isinstance(value, list) and len(value) == length
    for entry in value:
        rational_shape(entry)


def verify(out):
    out = Path(out)
    initial, run, core = (read(out/name) for name in ('public-actions-input.json', 'run-receipt.json', 'core-receipt.json'))
    item = initial['job']
    assert initial['core_sha256'] == item['core_sha256'] == core['source_sha256']
    assert initial['driver_sha256'] == item['wrapper_sha256']
    assert initial['source_commit'] == run['source_commit']
    assert run['core_receipt_sha256'] == file_spec(out/'core-receipt.json')['sha256']
    assert run['complete'] is True and run['process_exit_code'] == 0 and run['error'] is None
    assert core['complete'] is True and core['process_exit_code'] == 0 and core['error'] is None
    _, _, reviewed = prepare(item, out, allow_download=False)
    tag = expected_tag(item)
    assert core['configuration_sha256'] == fingerprint(tag)
    final = read(out/FINAL)
    assert final['result'] == RESULT and final['p'] == 41 and final['complete'] is True
    assert final['configuration'] == tag and core['certificate_sha256'] == sha(out/FINAL)
    for key in TRUE_FLAGS:
        assert final[key] is True
    for key in FALSE_FLAGS:
        assert final[key] is False
    inventory = read(bound(out, final['stage_manifest']))
    assert inventory['result'] == RESULT and inventory['configuration'] == tag and inventory['complete'] is True
    files = {row['file']: plain(row) for row in inventory['files']}
    assert len(files) == len(inventory['files']) == inventory['completed_stage_count'] == 24
    assert inventory['only_complete_current_source_stages_listed'] is True
    actual = {path.name for path in out.glob(PREFIX+'*.json.gz') if path.name != final['stage_manifest']['file']}
    assert actual == set(files)
    for spec in files.values():
        value = read(bound(out, spec))
        assert value['result'] == RESULT and value['configuration'] == tag and value['complete'] is True

    def own(spec):
        assert files[spec['file']] == plain(spec)
        return read(bound(out, spec))

    audit = own(final['source_audit'])
    assert audit['source_identities'] == tag['sources']
    for key in ('all_selected_original_source_bytes_SHA_and_configuration_verified',
                'original_1722_and_82_power_scales_preserved',
                'unscaled_original_M6_coordinates_used_without_rescaling'):
        assert audit[key] is True
    assert audit['new_field_or_target_or_Hom_normalization_introduced'] is False
    for group in ('V_jets', 'W_jets', 'norm_and_trace'):
        assert set(final[group]) == {str(j) for j in range(6)}
    assert set(final['comparison_leading_jets']) == {str(j) for j in range(1, 6)}
    for j in range(6):
        v = own(final['V_jets'][str(j)])
        assert v['j'] == j and v['actual_value_nonzero'] is True
        coordinate_shape(v['value_L'], 14)
        coordinate_shape(v['derivative_t_L'], 14)
        assert v['ordinary_690_basis_rows_have_factor_R_squared'] is True
        assert v['no_Phi_derivative_needed_at_this_order'] is True
        assert v['no_extra_82_power_or_1722_power_inserted'] is True
        w = own(final['W_jets'][str(j)])
        assert w['j'] == j and w['original_lambda_cube_constant'] == 108
        for key in ('W_value_L', 'W_derivative_t_L', 'W_logarithmic_derivative_t_L',
                    'lambda_cube_value_L', 'lambda_cube_derivative_t_L',
                    'lambda_over_lambda_f_value_L', 'lambda_over_lambda_f_derivative_t_L'):
            coordinate_shape(w[key], 14)
        assert w['actual_W_and_lambda_cube_nonzero'] is True
        assert w['all_field_inverses_and_displayed_quotients_multiplied_back'] is True
        assert w['cubic_root_selected_or_extra_target_phase_inserted'] is False
        norm = own(final['norm_and_trace'][str(j)])
        assert norm['j'] == j and norm['source_W_jet'] == final['W_jets'][str(j)]
        coordinate_shape(norm['norm_K_1_s'], 2)
        coordinate_shape(norm['trace_K_1_s'], 2)
        for key in ('original_norm_multiplication_matrix_K', 'original_trace_multiplication_matrix_K'):
            assert len(norm[key]) == 7 and all(len(row) == 7 for row in norm[key])
            for row in norm[key]:
                for value in row:
                    coordinate_shape(value, 2)
        assert len(norm['norm_pivot_transcript']) == 7
        for step in norm['norm_pivot_transcript']:
            assert step['pivot_inverse_verified'] is True
        for key in ('actual_norm_nonzero', 'all_pivot_inverses_multiplied_back',
                    'actual_norm_and_trace_in_original_K_basis_computed',
                    'Norm_is_actual_field_norm_not_same_target_T_product',
                    'no_original_Galois_or_target_scaling_constant_discarded'):
            assert norm[key] is True
    expected_pq = [(165, 67), (93, 67), (100, 67), (168, 67), (371, 134)]
    for j in range(1, 6):
        data = own(final['comparison_leading_jets'][str(j)])
        assert data['j'] == j and (data['p'], data['q']) == expected_pq[j-1]
        coordinate_shape(data['unit_first_logarithmic_derivative_K_1_s'], 2)
        dag = data['leading_constant_DAG']
        assert dag['output'] == 'kappa' and dag['coefficient_field_basis'] == K_BASIS
        assert len(dag['nodes']) == 5 and fingerprint(dag['nodes']) == data['leading_constant_DAG_sha256']
        assert dag['nodes'][0]['source'] == final['norm_and_trace']['0']
        assert dag['nodes'][1]['source'] == final['norm_and_trace'][str(j)]
        assert dag['nodes'][2]['operation'] == dag['nodes'][3]['operation'] == 'integer_power'
        assert dag['nodes'][4]['operation'] == 'divide'
        for key in ('actual_all_DAG_denominators_nonzero', 'actual_leading_constant_defined_and_nonzero',
                    'actual_unit_first_logarithmic_derivative_computed',
                    'both_original_K_coordinates_retained_without_projection'):
            assert data[key] is True
        assert data['leading_constant_large_integer_powers_expanded'] is False
        assert data['global_Picard_rigidification_or_height_computed'] is False
    print('ORIGINAL_C0_FIRST_JETS_VERIFIED='+json.dumps({'complete': True,
        'V_jets': 6, 'W_jets': 6, 'relative_norms_and_traces': 6, 'comparison_leading_jets': 5,
        'stage_count': len(files), 'new_mathematics_reexecuted_in_verifier': False}, sort_keys=True), flush=True)


def main():
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--request', type=Path, default=REQUEST)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--mode', choices=('compute', 'verify'), required=True)
    args = parser.parse_args()
    if args.mode == 'compute':
        item = read(args.request)
        guard(item, args.request)
        raise SystemExit(compute(item, args.output, args.request))
    item = read(args.output/'public-actions-input.json')['job']
    load_helper(item)
    verify(args.output)


if __name__ == '__main__':
    main()
