#!/usr/bin/env python3
"""Read-only public producer transport and finite-precision witness IO.

This module uses only the Python standard library.  It never imports either
mathematical core, evaluates a DAG, or repeats any p-adic arithmetic.
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
import signal
import subprocess
import sys
import tarfile

S = Path(__file__).resolve().parent
TOPIC = S.parent
REPO = TOPIC.parents[1]
REQUEST = TOPIC/'notes/R792-log-jet-padic-witness-public-request.json'
RESULT = 'R792-original-comparison-log-jet-padic-witness'
FINAL = 'p41-original-comparison-log-jet-padic-witness-certificate.json'
PREFIX = 'R792-log-jet-padic-'
BUNDLE = 'R792-log-jet-padic-retained-inputs.tar.gz'
MANIFEST = 'full-outputs-manifest.json'
REFERENCE = 'full-outputs-manifest-reference.json'
INPUT_RECEIPT = 'retained-inputs-receipt.json'
META = (MANIFEST, 'run-receipt.json', 'core-receipt.json', 'public-actions-input.json')
PARENT_FINAL = 'p41-original-Hom-comparison-log-jets-certificate.json'
PARENT_BUNDLE = 'R792-Hom-log-jets-retained-inputs.tar.gz'
PARENT_CORE = '417f2df7365fcb3ea2e9ce5403404b9c0d0859fc43359b52bb775468452328c2'
PARENT_WRAPPER = 'f79f4aa340a7e8050d19c746c4a02bb495081710f54566454bc8332ad2a3778b'
PARENT_PROGRAM = '555e3c6c877ef2b3fb64f0dfe17f463f49fd6ca83bb1a1faedc2db562724547b'
DAG_CORE_SHA = 'afb49c1ac4245674d29364789e817b566517e1f5bf6d506cee684ed03fa34b8b'
BALL_CORE_SHA = 'dd3f06a2ed34d31d4d9cc7000eeb5ca763b3fa26b238b418de3e2a47e8dca9c0'
METHOD_SHA = 'd55f377e2bb3532bfe6d5b18ecfdc26f74f1c6451507fefea5f3ea0b6a09fbf2'
IO_SHA = 'c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c'
BASE = ('result', 'run_id', 'source_commit', 'core_sha256', 'manifest_sha256',
        'configuration_sha256', 'selected_files_sha256')
H64 = re.compile(r'[0-9a-f]{64}')
IO = None
STRATEGY = {
    'original_program': 'R846 complete 733-node DAG, unchanged, with its original five logarithmic-jet roots',
    'source_precision': 518,
    'local_prime': 1000000753,
    'embedding': 'R843 completed branch 0; original simple-root lift and original f4 point balls reused',
    'Galois': 'eval(node,k)=iota_0(sigma^k(value(node))); each sigma node shifts the complete context modulo 7',
    'unit_chart': 'four completed modular linear responses only; no 2420-vector is solved or reconstructed',
    'arithmetic': 'frozen R843 absolute-precision Qell Ball arithmetic with exact rational constants',
    'inverse': 'only a ball with known finite valuation; an uncertain denominator makes this dependency inconclusive',
    'witness': 'a final ball not containing zero proves the original logarithmic jet nonzero',
    'ordinary_derivative': 'nonzero logarithmic jet and R844 original nonzero comparison value imply nonzero first derivative',
    'new_point_additions_or_Hensel_Dixon_CM_traces': False,
    'rational_reconstruction_candidates_consumed': False,
    'height_or_A1_acceptance': False,
    'budget_excluded_from_mathematical_identity': True,
}


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''):
            digest.update(block)
    return digest.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == '.gz' else open)(path, 'rt', encoding='utf-8') as stream:
        return json.load(stream)


def save(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+'.tmp')
    raw = (json.dumps(data, sort_keys=True, separators=(',', ':'))+'\n').encode()
    if path.suffix == '.gz':
        with temporary.open('wb') as destination:
            with gzip.GzipFile(fileobj=destination, mode='wb', mtime=0, compresslevel=2) as stream:
                stream.write(raw)
    else:
        temporary.write_bytes(raw)
    temporary.replace(path)


def fingerprint(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def safe(name):
    assert isinstance(name, str) and Path(name).name == name and name not in ('.', '..') and '\\' not in name
    return name


def plain(row):
    answer = {key: row[key] for key in ('file', 'bytes', 'sha256')}
    safe(answer['file'])
    assert isinstance(answer['bytes'], int) and answer['bytes'] >= 0 and H64.fullmatch(answer['sha256'])
    return answer


def file_spec(path):
    path = Path(path)
    return {'file': path.name, 'bytes': path.stat().st_size, 'sha256': sha(path)}


def bound(root, row):
    row = plain(row)
    path = Path(root)/row['file']
    assert path.stat().st_size == row['bytes'] and sha(path) == row['sha256']
    return path


def topic_path(relative):
    path = (TOPIC/relative).resolve()
    assert path.is_relative_to(TOPIC.resolve())
    return path


def identity(item):
    return {**{key: item[key] for key in BASE}, 'certificate': plain(item['certificate'])}


def load_io(item):
    global IO
    path = S/safe(item['io_helper'])
    assert path.name == 'R824_public_original_global_polar_generators.py'
    assert sha(path) == item['io_helper_sha256'] == IO_SHA
    definition = importlib.util.spec_from_file_location('frozen_R824_transport_only_for_log_jet_balls', path)
    IO = importlib.util.module_from_spec(definition)
    definition.loader.exec_module(IO)


def guard(item, request):
    if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public':
        raise SystemExit('This consumer executes only in public repository Actions.')
    assert request.resolve() == REQUEST.resolve()
    assert item['result'] == RESULT and item['p'] == 41 and item['producer_inputs_pending'] is False
    assert item['core'] == 'R792_original_comparison_log_jet_padic_witness.py'
    assert item['wrapper'] == 'R792_public_original_comparison_log_jet_padic_witness.py'
    for key, pin in (('core', item['core_sha256']), ('wrapper', item['wrapper_sha256']),
                     ('dag_core', DAG_CORE_SHA), ('ball_core', BALL_CORE_SHA)):
        assert sha(S/safe(item[key])) == item[key+'_sha256'] == pin
    assert sha(topic_path(item['method'])) == item['method_sha256'] == METHOD_SHA
    assert sha(REPO/'README.md') == item['readme_sha256']['root']
    assert sha(TOPIC/'README.md') == item['readme_sha256']['topic']
    assert 0 < item['budget_minutes'] <= 300
    parent = item['parent_source']
    assert parent['result'] == 'R792-original-Hom-comparison-log-jets'
    assert parent['core_sha256'] == PARENT_CORE and parent['wrapper_sha256'] == PARENT_WRAPPER
    assert parent['expected_conclusion'] == 'success'
    load_io(item)


def source_review(label, item, retained):
    root = Path(retained)/label
    assert (root/MANIFEST).stat().st_size == item['manifest_bytes'] and sha(root/MANIFEST) == item['manifest_sha256']
    manifest = read(root/MANIFEST)
    assert manifest['result'] == item['result']
    inventory = {row['file']: plain(row) for row in manifest['files']}
    assert len(inventory) == len(manifest['files']) == item['manifest_file_count']
    inventory[MANIFEST] = file_spec(root/MANIFEST)
    files = {name: plain(row) for name, row in item['files'].items()}
    assert fingerprint([files[name] for name in sorted(files)]) == item['selected_files_sha256']
    for name, row in files.items():
        assert safe(name) == row['file'] and inventory[name] == row
        bound(root, row)
    cert = read(bound(root, item['certificate']))
    assert files[item['certificate']['file']] == plain(item['certificate'])
    tag = cert['configuration']
    assert cert['result'] == item['result'] and cert['complete'] is True
    assert tag['source_sha256'] == item['core_sha256'] and fingerprint(tag) == item['configuration_sha256']
    run, core, public = (read(bound(root, files[name])) for name in META[1:])
    assert run['result'] == core['result'] == public['result'] == item['result']
    assert str(run['workflow_run_id']) == str(item['run_id'])
    assert run['source_commit'] == public['source_commit'] == item['source_commit']
    assert run['complete'] is True and run['process_exit_code'] == 0 and run.get('error') is None
    assert core['complete'] is True and core['source_sha256'] == item['core_sha256']
    assert core['certificate_sha256'] == item['certificate']['sha256']
    if 'core_receipt_sha256' in run:
        assert run['core_receipt_sha256'] == files['core-receipt.json']['sha256']
    actual_core = public['core_sha256'] if 'core_sha256' in public else public['job']['core_sha256']
    assert actual_core == item['core_sha256']
    if 'wrapper_sha256' in item:
        if 'wrapper_sha256' in public:
            actual_wrapper = public['wrapper_sha256']
        elif 'wrapper_sha256' in public.get('job', {}):
            actual_wrapper = public['job']['wrapper_sha256']
        else:
            assert label == 'R791'
            actual_wrapper = public['driver_sha256']
        assert actual_wrapper == item['wrapper_sha256']
    if 'original_readme_sha256' in item:
        assert public['root_readme_sha256'] == item['original_readme_sha256']['root']
        assert public['topic_readme_sha256'] == item['original_readme_sha256']['topic']
    return cert, tag, files


def parent_names(directory):
    directory = Path(directory)
    cert = read(directory/PARENT_FINAL)
    inventory = read(bound(directory, cert['stage_manifest']))
    assert inventory['complete'] is True and inventory['configuration'] == cert['configuration']
    return sorted(set(META) | {PARENT_FINAL, INPUT_RECEIPT, cert['stage_manifest']['file']} |
                  {row['file'] for row in inventory['files']})


def review_parent(item, retained):
    parent, root = item['parent_source'], Path(retained)/'JETS'
    assert (root/MANIFEST).stat().st_size == parent['manifest_bytes'] and sha(root/MANIFEST) == parent['manifest_sha256']
    manifest = read(root/MANIFEST)
    inventory = {row['file']: plain(row) for row in manifest['files']}
    inventory[MANIFEST] = file_spec(root/MANIFEST)
    names = parent_names(root)
    assert len(names) == parent['selected_file_count'] == 9
    files = {name: inventory[name] for name in names}
    selected = dict(parent, files=files)
    cert, tag, _ = source_review('JETS', selected, retained)
    assert tag['source_sha256'] == PARENT_CORE
    public = read(root/'public-actions-input.json')
    receipt = read(root/INPUT_RECEIPT)
    children = receipt['expanded_sources']
    assert set(children) == {'CM', 'R791', 'DAG', 'NONTORSION', 'POINTS'}
    assert children == public['expanded_sources']
    assert receipt['parent_source'] == public['job']['parent_source']
    assert receipt['selected_source_file_count'] == sum(len(value['files']) for value in children.values()) == 261
    assert receipt['all_source_bytes_and_original_parent_child_bindings_verified'] is True
    assert receipt['old_CM_Hom_point_or_nontorsion_arithmetic_recomputed'] is False
    assert plain(receipt['input_bundle']) == plain(parent['input_bundle']) == inventory[PARENT_BUNDLE]
    child_tags = {}
    for key, value in children.items():
        _, child_tags[key], _ = source_review(key, value, retained)
    assert tag['source_identities'] == {key: identity(value) for key, value in children.items()}
    for key, child_tag in child_tags.items():
        for inner, expected in child_tag.get('source_identities', {}).items():
            if inner in children:
                assert expected == identity(children[inner])
    for flag in ('actual_nontorsion_source_verified', 'all_new_inverse_nodes_have_original_nonzero_Hom_proofs',
                 'original_comparison_first_jets_as_exact_expressions',
                 'original_comparison_logarithmic_first_jets_as_exact_expressions',
                 'original_comparison_constants_preserved'):
        assert cert[flag] is True
    assert cert['point_program_node_count'] == 733 and cert['imported_R844_node_count'] == 529
    assert cert['new_point_addition_count'] == 0 and cert['actual_eta_or_height_computed'] is False
    assert cert['jet_program']['sha256'] == PARENT_PROGRAM
    for name in names:
        if name.endswith('.json.gz'):
            data = read(root/name)
            assert data['complete'] is True and data['configuration'] == tag
    for row in read(bound(root, cert['stage_manifest']))['files']:
        assert files[row['file']] == plain(row)
    program = read(bound(root, cert['jet_program']))
    assert program['node_count'] == len(program['nodes']) == 733
    assert program['imported_R844_nodes_unchanged'] is True
    known = {}
    for node in program['nodes']:
        assert fingerprint({key: value for key, value in node.items() if key != 'id'}) == node['id']
        assert node['id'] not in known and all(key in known for key in node['inputs'])
        known[node['id']] = node
    assert all(value in known for value in program['roots'].values())
    oldcert = read(bound(Path(retained)/'POINTS', children['POINTS']['certificate']))
    old = read(bound(Path(retained)/'POINTS', oldcert['point_program']))
    assert program['nodes'][:529] == old['nodes']
    assert program['original_parameter'] == 'z=a-1' and program['original_differential'] == 'dx/(2y)'
    comparisons = program['original_comparison_first_jets']
    assert [row['j'] for row in comparisons] == [1, 2, 3, 4, 5]
    for row in comparisons:
        assert row['logarithmic_derivative_z'] == program['roots']['R791_comparison_'+str(row['j'])+'_logarithmic_derivative_z']
        assert row['actual_seven_sigma_trace_used'] and row['original_value_and_all_norm_constants_unchanged']
    expanded = dict(children, JETS=selected)
    assert sum(len(value['files']) for value in expanded.values()) == 270
    return expanded


def unpack_sources(bundle, retained, expanded):
    retained = Path(retained)
    expected = {label+'/'+safe(name): plain(row) for label, item in expanded.items() for name, row in item['files'].items()}
    seen = set()
    with tarfile.open(bundle, 'r:gz') as archive:
        for member in archive:
            assert member.isfile() and not member.issym() and not member.islnk()
            name = PurePosixPath(member.name)
            assert not name.is_absolute() and '..' not in name.parts and '\\' not in member.name
            assert member.name in expected and member.name not in seen
            row = expected[member.name]
            assert member.size == row['bytes']
            destination = retained/Path(*name.parts)
            destination.parent.mkdir(parents=True, exist_ok=True)
            stream = archive.extractfile(member)
            assert stream is not None
            digest, count = hashlib.sha256(), 0
            temporary = destination.with_name(destination.name+'.extract')
            with temporary.open('wb') as output:
                for block in iter(lambda: stream.read(1024*1024), b''):
                    digest.update(block)
                    count += len(block)
                    output.write(block)
            assert count == row['bytes'] and digest.hexdigest() == row['sha256']
            if destination.exists():
                assert file_spec(destination) == row
                temporary.unlink()
            else:
                temporary.replace(destination)
            seen.add(member.name)
    assert seen == set(expected)


def pack_sources(retained, expanded, path):
    path = Path(path)
    temporary = path.with_name(path.name+'.tmp')
    with temporary.open('wb') as raw:
        with gzip.GzipFile(fileobj=raw, mode='wb', mtime=0, compresslevel=2) as zipped:
            with tarfile.open(fileobj=zipped, mode='w') as archive:
                for label, item in sorted(expanded.items()):
                    safe(label)
                    for name, row in sorted(item['files'].items()):
                        original = bound(Path(retained)/label, row)
                        info = tarfile.TarInfo(label+'/'+name)
                        info.size, info.mode, info.mtime = row['bytes'], 0o644, 0
                        with original.open('rb') as stream:
                            archive.addfile(info, stream)
    temporary.replace(path)


def prepare(item, out, allow_download=True):
    retained = out.parent/(out.name+'-retained')
    if (out/INPUT_RECEIPT).exists() and (out/BUNDLE).exists():
        receipt = read(out/INPUT_RECEIPT)
        assert receipt['parent_source'] == item['parent_source']
        assert file_spec(out/BUNDLE) == plain(receipt['input_bundle'])
        unpack_sources(out/BUNDLE, retained, receipt['expanded_sources'])
        expanded = review_parent(item, retained)
        assert expanded == receipt['expanded_sources']
        return retained, expanded
    assert allow_download
    parent, root = item['parent_source'], retained/'JETS'
    root.mkdir(parents=True, exist_ok=True)
    transfer = out.parent/(out.name+'-parent-transfer')
    archive = IO.Archive(parent, transfer, whole=True)
    try:
        archive.extract_bound(MANIFEST, parent['manifest_sha256'], root/MANIFEST, parent['manifest_bytes'])
        manifest = read(root/MANIFEST)
        files = archive.verify_all(manifest)
        def take(names):
            archive.extract_many([(name, files[name]['sha256'], root/name, files[name]['bytes'])
                                  for name in names if name != MANIFEST])
        take([PARENT_FINAL])
        take([read(root/PARENT_FINAL)['stage_manifest']['file']])
        take(parent_names(root))
        bundle = plain(parent['input_bundle'])
        assert files[PARENT_BUNDLE] == bundle
        archive.extract_bound(PARENT_BUNDLE, bundle['sha256'], transfer/PARENT_BUNDLE, bundle['bytes'])
        receipt = read(root/INPUT_RECEIPT)
        assert plain(receipt['input_bundle']) == bundle == file_spec(transfer/PARENT_BUNDLE)
        unpack_sources(transfer/PARENT_BUNDLE, retained, receipt['expanded_sources'])
        expanded = review_parent(item, retained)
        pack_sources(retained, expanded, out/BUNDLE)
        source_receipt = {'result': RESULT, 'parent_source': parent, 'expanded_sources': expanded,
            'input_bundle': file_spec(out/BUNDLE), 'source_transport': archive.receipt(),
            'selected_source_file_count': 270,
            'all_source_bytes_and_original_parent_child_bindings_verified': True,
            'old_CM_Hom_point_or_nontorsion_arithmetic_recomputed': False}
        save(out/INPUT_RECEIPT, source_receipt)
        print('INPUT_REVIEW='+json.dumps({key: source_receipt[key] for key in
            ('selected_source_file_count', 'input_bundle', 'all_source_bytes_and_original_parent_child_bindings_verified',
             'old_CM_Hom_point_or_nontorsion_arithmetic_recomputed')}), flush=True)
        return retained, expanded
    finally:
        archive.close()


def expected_tag(item, expanded):
    return {'result': RESULT, 'source_sha256': item['core_sha256'], 'p': 41,
        'method_sha256': METHOD_SHA, 'dag_core_sha256': DAG_CORE_SHA, 'ball_core_sha256': BALL_CORE_SHA,
        'source_identities': {key: identity(value) for key, value in expanded.items()},
        'strategy': STRATEGY, 'budget_excluded_from_mathematical_identity': True}


def stable_job(item):
    return {key: value for key, value in item.items() if key not in ('resume', 'budget_minutes')}


def output_manifest(out):
    rows = [file_spec(path) for path in sorted(out.iterdir()) if path.is_file() and
            path.name not in (MANIFEST, REFERENCE) and not path.name.endswith('.tmp')]
    save(out/MANIFEST, {'result': RESULT, 'files': rows,
        'temporary_active_checkpoint_retention_days': 1, 'reproducible_tables_in_git_or_release': False})
    save(out/REFERENCE, {'result': RESULT, 'manifest': file_spec(out/MANIFEST)})


def restore(item, out):
    source = item.get('resume')
    if source is None:
        return
    assert source['result'] == RESULT and source['core_sha256'] == item['core_sha256']
    assert source['wrapper_sha256'] == item['wrapper_sha256']
    root = out.parent/(out.name+'-resume')
    archive = IO.Archive(source, root, whole=False)
    try:
        archive.extract_bound(MANIFEST, source['manifest_sha256'], root/MANIFEST, source['manifest_bytes'])
        manifest = read(root/MANIFEST)
        assert manifest['result'] == RESULT
        files = {row['file']: plain(row) for row in manifest['files']}
        assert len(files) == len(manifest['files'])
        for name in ('public-actions-input.json', 'run-receipt.json', INPUT_RECEIPT):
            row = files[name]
            archive.extract_bound(name, row['sha256'], root/name, row['bytes'])
        public, run, receipt = (read(root/name) for name in ('public-actions-input.json', 'run-receipt.json', INPUT_RECEIPT))
        assert stable_job(public['job']) == stable_job(item)
        assert public['source_commit'] == run['source_commit'] == source['source_commit']
        assert str(run['workflow_run_id']) == str(source['run_id'])
        assert public['core_sha256'] == item['core_sha256'] and public['wrapper_sha256'] == item['wrapper_sha256']
        assert receipt['parent_source'] == item['parent_source']
        assert public['expanded_sources'] == receipt['expanded_sources']
        wanted = [name for name in files if name.startswith(PREFIX) and name.endswith('.json.gz')]+[BUNDLE, INPUT_RECEIPT]
        final = None
        if FINAL in files:
            row = files[FINAL]
            archive.extract_bound(FINAL, row['sha256'], root/FINAL, row['bytes'])
            final = read(root/FINAL)
            if final['complete']:
                wanted.append(FINAL)
        archive.extract_many([(name, files[name]['sha256'], out/name, files[name]['bytes']) for name in wanted])
        tag = expected_tag(item, receipt['expanded_sources'])
        for name in wanted:
            if name.endswith('.json.gz'):
                data = read(out/name)
                assert data['complete'] is True and data['configuration'] == tag
        if final is not None:
            assert final['configuration'] == tag
            if final['complete']:
                for row in read(bound(out, final['stage_manifest']))['files']:
                    bound(out, row)
        save(out/'resume-source-receipt.json', {'result': RESULT, 'source': source, 'transport': archive.receipt(),
            'old_complete_stage_arithmetic_recomputed': False, 'historical_incomplete_FINAL_restored': False})
    finally:
        archive.close()


def compute(item, out, request):
    out.mkdir(parents=True, exist_ok=True)
    restore(item, out)
    retained, expanded = prepare(item, out)
    config = dict(item, retained_sources=expanded)
    config_path = out.parent/(out.name+'-config.json')
    save(config_path, config)
    save(out/'public-actions-input.json', {'result': RESULT, 'job': item,
        'source_commit': os.environ['GITHUB_SHA'], 'source_repository': os.environ['GITHUB_REPOSITORY'],
        'core_sha256': item['core_sha256'], 'wrapper_sha256': item['wrapper_sha256'], 'request_sha256': sha(request),
        'expanded_sources': expanded, 'expanded_job_sha256': fingerprint(config),
        'root_readme_sha256': sha(REPO/'README.md'), 'topic_readme_sha256': sha(TOPIC/'README.md'),
        'prepared_at_utc': dt.datetime.now(dt.timezone.utc).isoformat()})
    command = [sys.executable, str(S/item['core']), '--config', str(config_path),
        '--method', str(topic_path(item['method'])), '--dag-core', str(S/item['dag_core']),
        '--ball-core', str(S/item['ball_core']), '--retained', str(retained), '--output', str(out),
        '--budget-minutes', str(item['budget_minutes'])]
    error, code = None, 1
    with (out/'core.log').open('ab') as stream:
        process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT, start_new_session=True)
        try:
            code = process.wait(timeout=item['budget_minutes']*60+900)
        except subprocess.TimeoutExpired:
            error, code = 'outer_timeout', 124
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.wait(timeout=15)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait()
    path = out/'core-receipt.json'
    receipt = read(path) if path.exists() else None
    complete = code == 0 and receipt is not None and receipt.get('complete') is True and (out/FINAL).exists()
    run = {'result': RESULT, 'source_commit': os.environ['GITHUB_SHA'], 'workflow_run_id': os.environ['GITHUB_RUN_ID'],
        'workflow_attempt': os.environ.get('GITHUB_RUN_ATTEMPT', '1'), 'complete': complete, 'process_exit_code': code,
        'error': error, 'core_receipt_sha256': sha(path) if receipt is not None else None,
        'actual_eta_or_height_computed': False, 'finished_at_utc': dt.datetime.now(dt.timezone.utc).isoformat()}
    save(out/'run-receipt.json', run)
    for path in out.glob('*.tmp'):
        path.unlink()
    output_manifest(out)
    print('RUN_RECEIPT='+json.dumps(run), flush=True)
    if not complete:
        raise SystemExit(code or 1)


def check_ball(row):
    assert isinstance(row, dict) and set(row) == {'unit', 'valuation_or_lower_bound', 'absolute_precision', 'known_nonzero'}
    assert isinstance(row['unit'], str) and row['unit'].isdigit()
    assert isinstance(row['valuation_or_lower_bound'], int) and isinstance(row['absolute_precision'], int)
    assert row['known_nonzero'] is (row['unit'] != '0')
    if row['known_nonzero']:
        assert row['valuation_or_lower_bound'] < row['absolute_precision']
    else:
        assert row['valuation_or_lower_bound'] == row['absolute_precision']


def verify(item, out, request):
    manifest = read(out/MANIFEST)
    assert manifest['result'] == RESULT and plain(read(out/REFERENCE)['manifest']) == file_spec(out/MANIFEST)
    files = {row['file']: plain(row) for row in manifest['files']}
    assert len(files) == len(manifest['files'])
    assert set(files) == {path.name for path in out.iterdir() if path.is_file() and path.name not in (MANIFEST, REFERENCE)}
    for row in files.values():
        bound(out, row)
    retained, expanded = prepare(item, out, allow_download=False)
    tag = expected_tag(item, expanded)
    public, run = read(out/'public-actions-input.json'), read(out/'run-receipt.json')
    assert public['job'] == item and public['request_sha256'] == sha(request)
    assert public['expanded_sources'] == expanded
    assert public['expanded_job_sha256'] == fingerprint(dict(item, retained_sources=expanded))
    assert public['core_sha256'] == item['core_sha256'] and public['wrapper_sha256'] == item['wrapper_sha256']
    assert public['source_commit'] == run['source_commit']
    core = read(out/'core-receipt.json') if 'core-receipt.json' in files else None
    if core is not None:
        assert core['result'] == RESULT and core['source_sha256'] == item['core_sha256']
        assert run['core_receipt_sha256'] == files['core-receipt.json']['sha256']
        assert core['configuration'] is None or core['configuration'] == tag
        assert core['new_Hensel_or_Dixon_digits'] == 0 and core['new_point_addition_count'] == 0
        assert core['actual_eta_or_height_computed'] is False
    else:
        assert run['core_receipt_sha256'] is None and run['complete'] is False
    stages = {}
    for name, row in files.items():
        if name.startswith(PREFIX) and name.endswith('.json.gz'):
            data = read(out/name)
            assert data['complete'] is True and data['configuration'] == tag
            stages[name] = row
    if FINAL not in files:
        print('PARTIAL_IO_REVIEW='+json.dumps({'complete': False, 'complete_stage_count': len(stages),
            'source_and_output_bytes_verified': True}), flush=True)
        raise SystemExit(1)
    final = read(out/FINAL)
    assert final['result'] == RESULT and final['configuration'] == tag
    assert core is not None and core['certificate_sha256'] == files[FINAL]['sha256']
    assert final['source_Dixon_digits'] == 518 and final['local_prime'] == 1000000753 and final['original_branch'] == 0
    assert final['original_node_count'] == 733
    for flag in ('zero_containing_ball_means_exact_zero', 'old_CM_Hom_point_or_nontorsion_arithmetic_recomputed',
                 'old_original_DAG_nodes_modified', 'candidate_arrays_used', 'original_value_rowspace_zero_A1_proved',
                 'expanded_original_coordinates_exactly_certified', 'original_rigidification_computed',
                 'actual_eta_or_height_computed', 'all_p_nonzero_conclusion_claimed'):
        assert final[flag] is False
    assert final['new_point_addition_count'] == final['new_Hensel_or_Dixon_digits'] == 0
    inventory = read(bound(out, final['stage_manifest']))
    assert inventory['complete'] is True and inventory['configuration'] == tag
    expected = {name: row for name, row in stages.items() if not name.startswith(PREFIX+'stage-manifest-')}
    if final['complete']:
        assert {row['file']: plain(row) for row in inventory['files']} == expected
    else:
        for row in inventory['files']:
            assert expected[row['file']] == plain(row)
    for key in ('source_audit', 'seven_embedding_balls'):
        assert expected[final[key]['file']] == plain(final[key])
    audit = read(bound(out, final['source_audit']))
    assert audit['source_identities'] == tag['source_identities']
    assert audit['original_node_count'] == 733 and audit['imported_R844_nodes_unchanged'] is True
    assert audit['new_Hensel_or_Dixon_digits'] == audit['new_point_additions'] == 0
    assert audit['source_candidate_arrays_consumed'] is False
    jets = expanded['JETS']
    cert = read(bound(retained/'JETS', jets['certificate']))
    program = read(bound(retained/'JETS', cert['jet_program']))
    assert final['original_program'] == {'source_group': 'JETS', **plain(cert['jet_program'])}
    nodes = {row['id']: row for row in program['nodes']}
    def reference(row):
        if 'source_group' in row:
            label = row['source_group']
            assert expanded[label]['files'][row['file']] == plain(row)
            return read(bound(retained/label, row))
        assert row['file'] in expected and expected[row['file']] == plain(row)
        return read(bound(out, row))
    for name in expected:
        data = read(out/name)
        if name.startswith(PREFIX+'node-'):
            node = nodes[data['original_node_id']]
            assert name == PREFIX+'node-'+node['id']+'-sigma-'+str(data['sigma_power'])+'.json.gz'
            assert 0 <= data['sigma_power'] < 7 and data['operation'] == node['operation']
            assert data['original_program'] == final['original_program']
            assert data['exact_zero_claimed'] is False and data['original_DAG_node_modified'] is False
            for ref in data['dependencies']:
                reference(ref)
            if data['evaluation_available']:
                check_ball(data['ball'])
                assert data['inconclusive_reason'] is None
            else:
                assert data['ball'] is None and data['inconclusive_reason'] is not None
    embeddings = read(bound(out, final['seven_embedding_balls']))
    assert len(embeddings['b_values']) == 7 and len(set(embeddings['seven_distinct_residue_embeddings'])) == 7
    for row in embeddings['b_values']+[embeddings['s'], embeddings['zeta'], embeddings['sigma7_consistency_residual']]:
        check_ball(row)
    assert embeddings['sigma7_consistency_residual']['known_nonzero'] is False
    assert embeddings['old_root_lift_recomputed'] is False
    summaries, witnessed = [], 0
    for ref in final['comparison_decisions']:
        decision = reference(ref)
        j = decision['j']
        assert 1 <= j <= 5 and ref['file'] == PREFIX+'comparison-'+str(j)+'.json.gz'
        old = program['original_comparison_first_jets'][j-1]
        assert decision['source_logarithmic_jet_root'] == old['logarithmic_derivative_z']
        assert decision['source_original_comparison_value_root'] == old['original_comparison_value_root']
        assert decision['source_original_derivative_root'] == old['derivative_z']
        evaluated = reference(decision['evaluated_root'])
        assert evaluated['original_node_id'] == old['logarithmic_derivative_z'] and evaluated['sigma_power'] == 0
        assert decision['evaluation_available'] == evaluated['evaluation_available']
        if decision['evaluation_available']:
            check_ball(decision['ball'])
            assert decision['ball'] == evaluated['ball'] and decision['inconclusive_reason'] is None
            nonzero = decision['ball']['known_nonzero']
        else:
            assert decision['ball'] is None and decision['inconclusive_reason'] is not None
            nonzero = False
        assert decision['original_logarithmic_jet_proved_nonzero'] is nonzero
        assert decision['original_comparison_derivative_proved_nonzero'] is nonzero
        assert decision['exact_jet_zero_claimed'] is False and decision['height_jet_nonzero_claimed'] is False
        witnessed += nonzero
        summaries.append({'j': j, 'proved_nonzero': nonzero,
            'valuation_or_lower_bound': None if decision['ball'] is None else decision['ball']['valuation_or_lower_bound'],
            'absolute_precision': None if decision['ball'] is None else decision['ball']['absolute_precision'], 'stage': ref})
    assert len({row['j'] for row in summaries}) == len(summaries) == final['processed_comparison_count']
    assert witnessed == final['strict_nonzero_witness_count'] == core['strict_nonzero_witness_count']
    assert final['all_five_logarithmic_jets_proved_nonzero'] is (witnessed == 5)
    assert final['all_five_comparison_derivatives_proved_nonzero'] is (witnessed == 5)
    if not final['complete']:
        assert core['complete'] is False and run['complete'] is False
        print('PARTIAL_IO_REVIEW='+json.dumps({'complete': False, 'processed': len(summaries),
            'witnesses': witnessed, 'source_and_output_bytes_verified': True}), flush=True)
        raise SystemExit(1)
    assert len(summaries) == 5 and core['complete'] is True and run['complete'] is True and run['process_exit_code'] == 0
    print('COMPLETE_PADIC_LOG_JET_IO_REVIEW='+json.dumps({'complete': True, 'source_files': 270,
        'strict_nonzero_witness_count': witnessed, 'original_DAG_nodes_unchanged': 733,
        'comparison_decisions': summaries, 'all_five_proved_nonzero': witnessed == 5,
        'actual_eta_or_height_computed': False, 'certificate': files[FINAL], 'stage_manifest': final['stage_manifest']}), flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('operation', choices=('compute', 'verify'))
    parser.add_argument('--request', type=Path, default=REQUEST)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    item = read(args.request)['job']
    guard(item, args.request)
    (compute if args.operation == 'compute' else verify)(item, args.output, args.request)


if __name__ == '__main__':
    main()
