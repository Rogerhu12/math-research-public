"""Public SC execution with full actual predecessors and exact old carriers.

No scientific retry is automatic.  Whole new natural conclusions are pushed
as soon as saved.  Every rejected push immediately rebases and retries.
Capacity uses a published origin tree plus exact local Git delta, including
an already committed but not yet pushed outcome; local trees are never sent
to the GitHub tree API as if they were published objects.
"""
from __future__ import annotations
import argparse, ast, base64, codecs, gc, hashlib, importlib.util, json, os
from pathlib import Path
import selectors, subprocess, sys, tempfile, time, traceback, urllib.request
from datetime import datetime, timezone
from types import SimpleNamespace

REPO = 'Rogerhu12/math-research-public'
TOPIC = 'topics/visible-flex-exact-nearby'
LIMIT, RESERVE = 200000000, 120000


def require(ok, message):
    if not ok:
        raise ValueError(message)


def utc():
    return datetime.now(timezone.utc).isoformat()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()


def encode(value):
    return (json.dumps(value, sort_keys=True, separators=(',', ':'),
                       ensure_ascii=False, allow_nan=False)+'\n').encode()


def parse(raw):
    return json.loads(raw, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def atomic(path, raw):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+'.candidate')
    with temporary.open('wb') as stream:
        stream.write(raw); stream.flush(); os.fsync(stream.fileno())
    require(temporary.read_bytes() == raw, 'whole candidate byte readback')
    temporary.replace(path)
    require(path.read_bytes() == raw, 'whole formal byte readback')


def topic_path(path):
    require(isinstance(path, str) and path.startswith(TOPIC+'/')
            and all(part not in ('', '.', '..') for part in path.split('/')),
            'one exact safe topic path')
    return path


def load(path, label):
    spec = importlib.util.spec_from_file_location(label, path)
    require(spec is not None and spec.loader is not None, 'one complete pinned source')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def emit(path, raw):
    print('BEGIN COMPLETE PUBLIC FILE '+path+' bytes='+str(len(raw))+' sha256='+sha(raw), flush=True)
    sys.stdout.write(raw.decode()); sys.stdout.flush()
    print('END COMPLETE PUBLIC FILE '+path, flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', required=True)
    parser.add_argument('--manifest', required=True)
    parser.add_argument('--manifest-sha', required=True)
    args = parser.parse_args()
    require(os.environ.get('GITHUB_ACTIONS') == 'true'
            and os.environ.get('GITHUB_REPOSITORY') == REPO
            and os.environ.get('GITHUB_RUN_ATTEMPT') == '1',
            'the authorized public first-attempt execution only')
    root = Path(args.repo).resolve()
    os.chdir(root)
    sys.dont_write_bytecode = True

    def git(*arguments, check_return=True, binary=False):
        result = subprocess.run(['git', '-c', 'user.name=github-actions[bot]', '-c',
            'user.email=41898282+github-actions[bot]@users.noreply.github.com', *arguments],
            cwd=root, capture_output=True, text=not binary)
        if check_return and result.returncode:
            message = result.stderr.decode('utf-8', 'replace') if binary else result.stderr
            raise RuntimeError('git '+' '.join(arguments)+' failed: '+message)
        return result

    token = os.environ['GITHUB_TOKEN']
    authorization = base64.b64encode(('x-access-token:'+token).encode()).decode()
    os.environ.update(GIT_CONFIG_COUNT='1', GIT_CONFIG_KEY_0='http.https://github.com/.extraheader',
                      GIT_CONFIG_VALUE_0='AUTHORIZATION: basic '+authorization)
    run, attempt = os.environ['GITHUB_RUN_ID'], os.environ['GITHUB_RUN_ATTEMPT']
    manifest_path = Path(args.manifest)
    if not manifest_path.is_absolute():
        manifest_path = root/manifest_path
    raw_manifest = manifest_path.read_bytes()
    require(0 < len(raw_manifest) < 100000 and sha(raw_manifest) == args.manifest_sha,
            'one complete pinned actual-input manifest')
    manifest = parse(raw_manifest)
    require(manifest['repository'] == REPO
            and manifest['kind'] == 'R149_actual_complete_signed_finite_inputs_v1'
            and manifest['stage'] == 'actual_signed_finite_columns'
            and manifest['whole_actual_prerequisite_counts'] == {
                'positive': [58, 224, 32], 'TC': 3, 'RW': 96, 'JC': 7}
            and manifest['original_TC_manifest_transitively_restored_whole'] is True
            and manifest['same_original_TC_trial_and_matrix_carrier_hashes_required'] is True,
            'the entire actual signed96 target, never a six-port-only substitute')
    operation = manifest['operation']
    require(operation['topic_maximum_bytes'] == LIMIT and operation['reserve_bytes'] == RESERVE
            and operation['readme_pull_interval_seconds'] == 1800
            and operation['automatic_scientific_retry'] is False,
            'original capacity, README checks and no automatic science retry')
    specs = manifest['files']
    by_role = {item['role']: item for item in specs}
    require(len(by_role) == len(specs) == manifest['expected_current_input_count']
            and len({item['path'] for item in specs}) == len(specs),
            'every whole actual input has one unique role and path')
    marker_path = topic_path(operation['consumed_marker'])
    output_dir = topic_path(operation['output_base']+'/run-'+run+'-'+attempt)
    temporary = Path(tempfile.mkdtemp(prefix='actual-signed-finite-', dir=os.environ.get('RUNNER_TEMP')))
    inputs = temporary/'complete-input-tree'
    outputs, private = temporary/'new-natural-conclusions', temporary/'private-carriers'
    inputs.mkdir(); outputs.mkdir(); private.mkdir()
    immutable_manifest, rows_index = temporary/'manifest.json', inputs/'original-row-parts-index.json'
    atomic(immutable_manifest, raw_manifest)
    staged, published_targets, owner, actual_state = {}, set(), None, None
    state = {
        'kind': 'R149_complete_actual_signed_finite_execution_v1', 'repository': REPO,
        'problem_id': manifest['problem_id'], 'manifest_sha256': args.manifest_sha,
        'run_id': run, 'run_attempt': attempt, 'event_commit': os.environ['GITHUB_SHA'],
        'started_utc': utc(), 'readme_checks': [], 'readme_check_count': 0,
        'readme_receipt_chain_sha256': None, 'current_input_receipts': [],
        'original_TC_current_closure': None, 'historical_restoration': None,
        'original_row_restoration': None, 'necessary_input_reconstruction': None,
        'necessary_input_reconstruction_children': 0, 'old_numerical_producers_called': 0,
        'scientific_children': 0, 'actual_child_returncode': None,
        'old_completed_targets_recomputed': 0, 'new_arrays_published': 0,
        'new_artifacts': 0, 'new_Releases': 0, 'complete': False, 'failure': None,
        'completed_natural_targets': [], 'scientific_files': [], 'publication_attempts': 0,
        'full_mean_phase_nu_high_Schur_proved': False, 'topic_completion_proved': False,
    }

    def fetch_commit(commit):
        require(isinstance(commit, str) and len(commit) == 40
                and all(value in '0123456789abcdef' for value in commit), 'one immutable original commit')
        if git('cat-file', '-e', commit+'^{commit}', check_return=False).returncode:
            git('fetch', '--filter=blob:none', '--no-tags', '--depth=1', 'origin', commit)

    def checked_bytes(spec, head, small=True):
        path = topic_path(spec['path'])
        observed = git('rev-parse', head+':'+path).stdout.strip()
        require(observed == spec['git_blob_sha'], 'the original whole Git blob: '+path)
        raw = git('show', head+':'+path, binary=True).stdout
        require(len(raw) == spec['bytes'] and sha(raw) == spec['sha256'] and blob(raw) == observed,
                'the original entire file bytes: '+path)
        if small:
            require(0 < len(raw) < 100000, 'one whole small UTF8 input')
            raw.decode()
            if path.endswith('.py'):
                ast.parse(raw, filename=path)
        return raw, observed

    entry_head = git('rev-parse', 'HEAD').stdout.strip()
    state['entry_checkout'] = entry_head
    review_spec = by_role['reviewed_rules']
    review = parse(checked_bytes(review_spec, entry_head)[0])
    require(review['repository'] == REPO and review['new_unread_rules_must_still_be_reported_and_applied'] is True
            and review['large_data_policy']['maximum_topic_bytes'] == LIMIT
            and review['large_data_policy']['original_completed_mathematics_must_not_be_recomputed'] is True
            and review['large_data_policy']['keep_only_scripts_parameters_runs_output_hashes_and_conclusions'] is True,
            'the complete actual README review and original large-data rules')
    read_commit = review['read_commit']
    fetch_commit(read_commit)
    for path, expected in review['readme_sha256'].items():
        require(sha(git('show', read_commit+':'+path, binary=True).stdout) == expected,
                'the explicitly reviewed whole README bytes')

    def pull():
        before, began = git('rev-parse', 'HEAD').stdout.strip(), utc()
        git('pull', '--rebase', 'origin', 'main')
        after = git('rev-parse', 'HEAD').stdout.strip()
        paths = list(review['readme_sha256'])
        difference = git('diff', before, after, '--', *paths).stdout
        from_review = git('diff', read_commit, after, '--', *paths).stdout
        observed = {path: sha(git('show', after+':'+path, binary=True).stdout) for path in paths}
        receipt = {'started_utc': began, 'finished_utc': utc(), 'before': before, 'after': after,
                   'actual_diff': difference, 'diff_from_read_commit': from_review,
                   'read_commit': read_commit, 'reviewed_rules_sha256': review_spec['sha256'],
                   'readme_sha256': observed}
        state['readme_check_count'] += 1
        state['readme_receipt_chain_sha256'] = sha(encode({
            'previous': state['readme_receipt_chain_sha256'], 'receipt': receipt}))
        state['readme_checks'].append(receipt)
        if len(state['readme_checks']) > 4:
            state['readme_checks'] = [state['readme_checks'][0], *state['readme_checks'][-3:]]
            state['readme_retention'] = 'First and latest three full receipts; every receipt printed and hash chained.'
        print('COMPLETE PULL AND README RECEIPT '+encode(receipt).decode(), end='', flush=True)
        require(observed == review['readme_sha256'] and not from_review,
                'README changed: retain the entire conclusion prefix and apply the printed new rules')
        return after

    capacity_cache = {}
    def capacity(head):
        # The corrected negative-nu worker rule: REST only for the published
        # origin tree; account for an unpushed rebased local commit by Git delta.
        tree_sha = git('rev-parse', head+':'+TOPIC).stdout.strip()
        base_head = git('rev-parse', 'origin/main').stdout.strip()
        base_tree = git('rev-parse', base_head+':'+TOPIC).stdout.strip()
        if base_tree not in capacity_cache:
            request = urllib.request.Request('https://api.github.com/repos/'+REPO+'/git/trees/'+base_tree+'?recursive=1',
                headers={'Authorization': 'Bearer '+token, 'Accept': 'application/vnd.github+json'})
            with urllib.request.urlopen(request, timeout=60) as response:
                raw = response.read()
            data = parse(raw)
            require(data.get('truncated') is False and data['sha'] == base_tree,
                    'complete published-base capacity metadata')
            sizes, blobs = {}, {}
            for row in data['tree']:
                if row['type'] != 'blob':
                    continue
                require(type(row['size']) is int and row['size'] >= 0, 'whole Git blob size')
                path = topic_path(TOPIC+'/'+row['path'])
                require(path not in sizes, 'unique complete published topic path')
                sizes[path], blobs[path] = row['size'], row['sha']
            capacity_cache.clear()
            capacity_cache[base_tree] = (len(raw), sha(raw), sizes, blobs)
        metadata_bytes, metadata_sha, base_sizes, base_blobs = capacity_cache[base_tree]
        sizes, blobs = dict(base_sizes), dict(base_blobs)
        delta = git('diff', '--raw', '--no-abbrev', '--no-renames', '-z', base_head, head, '--', TOPIC, binary=True).stdout
        pieces = delta.split(b'\0')
        require(pieces[-1] == b'' and (len(pieces)-1) % 2 == 0, 'entire NUL-delimited local delta')
        changes, null = [], '0'*40
        for index in range(0, len(pieces)-1, 2):
            fields = pieces[index].decode('ascii').split()
            path = topic_path(pieces[index+1].decode())
            require(len(fields) == 5 and fields[0].startswith(':') and fields[4] in ('A', 'D', 'M', 'T'),
                    'one complete ordinary local file delta')
            old, new = fields[2], fields[3]
            require(old == blobs.get(path, null), 'the exact published-base delta source')
            before = sizes.get(path, 0)
            if new == null:
                require(path in sizes, 'the complete deleted original blob')
                after = 0; del sizes[path]; del blobs[path]
            else:
                require(git('cat-file', '-t', new).stdout.strip() == 'blob', 'a complete local changed blob')
                after = int(git('cat-file', '-s', new).stdout.strip())
                require(after >= 0, 'exact complete local changed size')
                sizes[path], blobs[path] = after, new
            changes.append({'path': path, 'status': fields[4], 'old_git_blob_sha': old,
                            'new_git_blob_sha': new, 'old_bytes': before, 'new_bytes': after})
        return {'head': head, 'topic_tree': tree_sha, 'topic_blob_bytes': sum(sizes.values()),
                'blob_count': len(sizes), 'metadata_bytes': metadata_bytes, 'metadata_sha256': metadata_sha,
                'published_metadata_base_head': base_head, 'published_metadata_base_topic_tree': base_tree,
                'complete_local_delta_bytes': len(delta), 'complete_local_delta_sha256': sha(delta),
                'complete_changed_local_blobs': changes}, sizes

    def materialize_current(head):
        for spec in specs:
            raw, unused = checked_bytes(spec, head)
            destination = inputs/spec['path']
            if destination.exists():
                require(destination.read_bytes() == raw, 'never change an admitted whole predecessor')
            else:
                atomic(destination, raw)
        require(sha(Path(__file__).read_bytes()) == by_role['worker']['sha256'],
                'the actually running worker is the whole pinned source')
        require(sha(git('show', head+':'+str(manifest_path.relative_to(root)), binary=True).stdout) == args.manifest_sha,
                'the same complete manifest after every actual pull')
        state['current_input_receipts'] = specs

    def materialize_original_TC():
        tc_manifest = parse((inputs/by_role['TC_manifest']['path']).read_bytes())
        tc_specs = {item['path']: item for item in tc_manifest['files']+tc_manifest['historical_inputs']}
        tc_roles = {role: tc_specs[path] for role, path in tc_manifest['roles'].items()}
        checkout = manifest['original_TC_checkout']
        fetch_commit(checkout)
        receipts = []
        for spec in tc_manifest['files']:
            raw, observed = checked_bytes(spec, checkout)
            destination = inputs/spec['path']
            if destination.exists():
                require(destination.read_bytes() == raw, 'whole shared input has identical original bytes')
            else:
                atomic(destination, raw)
            receipts.append({'path': spec['path'], 'bytes': len(raw), 'sha256': sha(raw), 'git_blob_sha': observed})
        state['original_TC_current_closure'] = {
            'original_checkout': checkout, 'complete_input_count': len(receipts),
            'complete_input_receipts_sha256': sha(encode(receipts)),
            'original_manifest_sha256': by_role['TC_manifest']['sha256'],
            'all_current_original_files_retained': True}
        return tc_manifest, tc_roles

    def restore_original_native(tc_manifest, tc_roles):
        receipts = []
        for spec in tc_manifest['historical_inputs']:
            if spec.get('reconstruct_only') is True:
                require(spec in tc_manifest['input_restoration']['generated_direction_inputs'],
                        'only the original explicit14 direction shards may be rematerialized')
                continue
            require(spec['restore_only'] is True, 'restore whole original historical bytes only')
            fetch_commit(spec['commit'])
            raw, observed = checked_bytes(spec, spec['commit'], small=False)
            destination = inputs/spec['path']
            if destination.exists():
                require(destination.read_bytes() == raw, 'one same original native identity')
            else:
                atomic(destination, raw)
            receipts.append({'path': spec['path'], 'commit': spec['commit'], 'bytes': len(raw),
                             'sha256': sha(raw), 'git_blob_sha': observed})
        state['historical_restoration'] = {'whole_original_file_count': len(receipts),
            'complete_receipts': receipts, 'scientific_target_calls': 0, 'original_bytes_changed': 0}
        helper = load(inputs/tc_roles['restoration_helper']['path'], '_SC_original_nodal_and_rows_restore')
        parts, table = helper.restore_rows(tc_manifest['input_restoration'], inputs,
                                          checked_bytes, fetch_commit, atomic)
        index = {'kind': 'TC_restored_complete_original_40_parts_v1',
                 'original_manifest_sha256': tc_roles['old_body_manifest']['sha256'],
                 'parts': parts, 'part_receipts': table}
        atomic(rows_index, encode(index))
        state['original_row_restoration'] = {'complete_original_part_count': len(parts),
            'complete_original_part_receipts_sha256': sha(encode(table)),
            'complete_private_restoration_index_sha256': sha(encode(index)),
            'original_arrays_recomputed': 0, 'original_arrays_published': 0}
        helper.reconstruct_direction(tc_manifest['input_restoration'], inputs, temporary, tc_roles, state)

    def publish(factory, message, before_science=False):
        while True:
            state['publication_attempts'] += 1
            head = pull()
            cap, sizes = capacity(head)
            state['latest_publication_capacity'] = cap
            files = factory()
            if before_science and git('cat-file', '-e', head+':'+marker_path, check_return=False).returncode == 0:
                prior = parse(git('show', head+':'+marker_path, binary=True).stdout)
                require(prior.get('run_id') == run and prior.get('run_attempt') == attempt,
                        'another actual attempt already consumed this complete target')
            require(sum(len(raw) for raw in files.values()) <= operation['maximum_total_publication_bytes'],
                    'whole complete small-publication budget')
            projected = cap['topic_blob_bytes']
            for path, raw in files.items():
                topic_path(path)
                require(0 < len(raw) < 100000, 'one whole small UTF8 public file')
                raw.decode()
                projected += len(raw)-sizes.get(path, 0)
            allowance = operation['maximum_total_publication_bytes']+RESERVE if before_science else 0
            require(projected+allowance <= LIMIT, 'the whole actual rebased topic remains within200MB')
            for path, raw in files.items():
                atomic(root/path, raw)
            git('add', '--sparse', '--', *files)
            if git('diff', '--cached', '--quiet', check_return=False).returncode:
                git('commit', '-m', message)
            # The index may be unchanged after a successful rebase while HEAD
            # still contains our rejected output commit.  Always push HEAD.
            result = git('push', 'origin', 'HEAD:main', check_return=False)
            if result.returncode == 0:
                for path, raw in files.items():
                    emit(path, raw)
                return {'commit': git('rev-parse', 'HEAD').stdout.strip(), 'projected_topic_bytes': projected}
            print('Push rejected; immediately pull --rebase, check READMEs, and push again.', flush=True)
            pull()

    def collect():
        nonlocal actual_state
        if owner is None:
            return []
        state_path = outputs/owner.FILES['state']
        if not state_path.exists():
            return []
        raw = state_path.read_bytes()
        require(0 < len(raw) <= operation['maximum_state_bytes'], 'whole actual SC state budget')
        actual_state = parse(raw)
        require(actual_state['kind'] == owner.KIND and actual_state['manifest_sha256'] == args.manifest_sha
                and actual_state['run_id'] == run and actual_state['run_attempt'] == attempt
                and actual_state['parameters'] == owner.PARAMETERS
                and actual_state['completed_targets'] == owner.TARGETS[:len(actual_state['completed_targets'])]
                and actual_state['old_completed_targets_recomputed'] == actual_state['new_arrays_published'] == 0,
                'the complete actual owner identity and honest natural-object prefix')
        staged[output_dir+'/'+owner.FILES['state']] = raw
        available = []
        for name in ('columns', 'physical_primitive96', 'declared_incoming_cosine96'):
            path = outputs/owner.FILES[name]
            if not path.exists():
                continue
            raw = path.read_bytes()
            limit = operation['maximum_columns_bytes' if name == 'columns' else 'maximum_matrix_bytes']
            require(0 < len(raw) <= limit, 'whole SC natural conclusion budget')
            document = parse(raw)
            owner.validate_result(document, name, args.manifest_sha, actual_state['whole_input_identity'])
            public_path = output_dir+'/'+owner.FILES[name]
            require(public_path not in staged or staged[public_path] == raw,
                    'a complete natural conclusion can never be overwritten')
            staged[public_path] = raw
            available.append(document['target'])
        require(available == owner.TARGETS[:len(available)], 'every complete object retained in declared order')
        state['completed_natural_targets'] = available
        state['scientific_files'] = [{'path': path, 'bytes': len(raw), 'sha256': sha(raw)}
                                     for path, raw in sorted(staged.items())]
        return available

    def outcome_files():
        state['original_scientific_complete'] = None if actual_state is None else actual_state['complete']
        state['original_scientific_failure'] = None if actual_state is None else actual_state['failure']
        state['necessary_trial_carrier_restoration'] = (None if actual_state is None
                                                       else actual_state['necessary_carrier_restoration'])
        body = encode(state)
        require(len(body) <= operation['maximum_execution_bytes'], 'whole execution evidence budget')
        report = ('# Actual complete signed96 PDE-column conclusions\n\nRun '+run+'/'+attempt
            +'; complete mathematical target: '+str(state['complete'])+'.\n\n'
            'Every original positive58/224/32 stage, all three TC objects, all96 original RW rows '
            'and all seven actual JC records precede this arithmetic.  Original carriers are '
            'necessarily rematerialized with their complete original hashes; no old residual, '
            'norm, KAM, or JC target runs again.  The new objects contain96 true full waist-column '
            'error bounds, every original low/mean, high/mixed and combined root96 bound passively '
            'saved from the same single column-error call, and both entire signed96 matrices '
            'with honest sufficient inverse-gate '
            'outcomes.  Both physical density means are retained in the receiver.  The full mean, '
            'phase, nu and high-eliminated Schur problem and nonlinear closed-family completion '
            'remain separate obligations.  Complete private arrays are not published.\n').encode()
        return {**staged, output_dir+'/execution.json': body, output_dir+'/report.md': report}

    try:
        head = pull()
        if git('cat-file', '-e', head+':'+marker_path, check_return=False).returncode == 0:
            prior = parse(git('show', head+':'+marker_path, binary=True).stdout)
            require(prior.get('problem_id') == manifest['problem_id'], 'one same already consumed full target')
            print('Consumed whole target retained; no scientific child or automatic retry.', flush=True)
            print(encode(prior).decode(), end='', flush=True)
            return
        materialize_current(head)
        tc_manifest, tc_roles = materialize_original_TC()
        owner = load(inputs/by_role['science']['path'], '_SC_actual_owner_metadata_only')
        metadata = owner.metadata(inputs, raw_manifest, args.manifest_sha)
        state['whole_actual_predecessor_admission_before_native_restore'] = {
            'positive_records': [58, 224, 32], 'TC_targets': len(metadata['TC_owner'].TARGETS),
            'RW_rows': 96, 'actual_JC_records': 7, 'old_targets_called': 0}
        del metadata
        cap, unused = capacity(head)
        require(cap['topic_blob_bytes']+operation['maximum_total_publication_bytes']+RESERVE <= LIMIT,
                'complete topic publication room before necessary carrier restoration')
        state['pre_execution_capacity'] = cap
        restore_original_native(tc_manifest, tc_roles)
        admitted = owner.preflight(SimpleNamespace(input_root=str(inputs), manifest=str(immutable_manifest),
                    manifest_sha=args.manifest_sha, rows_index=str(rows_index)))
        state['whole_original_input_admission_before_science'] = admitted['preflight_receipt']
        del admitted
        gc.collect()
        require(not any(name in sys.modules for name in ('numpy', 'flint', 'scipy')),
                'the worker and all predecessor admission remain metadata only')
        marker = {'kind': 'consumed_R149_actual_complete_signed96_target_v1',
                  'problem_id': manifest['problem_id'], 'manifest_sha256': args.manifest_sha,
                  'run_id': run, 'run_attempt': attempt, 'prepared_utc': utc(),
                  'output_directory': output_dir, 'automatic_scientific_retry': False,
                  'status': 'all_whole_actual_predecessors_and_original_inputs_admitted',
                  'old_completed_targets_may_be_recomputed': False}
        state['consumed_marker_publication'] = publish(lambda: {marker_path: encode(marker)},
            'visible-exact: reserve complete actual signed96 target', before_science=True)
        head = pull()
        materialize_current(head)
        state['actual_scientific_checkout'] = head
        command = [sys.executable, '-u', str(inputs/by_role['science']['path']),
            '--input-root', str(inputs), '--manifest', str(immutable_manifest), '--manifest-sha', args.manifest_sha,
            '--rows-index', str(rows_index), '--out', str(outputs), '--private', str(private), '--checkout', head]
        environment = dict(os.environ)
        for key in ('GITHUB_TOKEN', 'GIT_CONFIG_COUNT', 'GIT_CONFIG_KEY_0', 'GIT_CONFIG_VALUE_0'):
            environment.pop(key, None)
        environment.update(PYTHONDONTWRITEBYTECODE='1', OPENBLAS_CORETYPE='Haswell', OPENBLAS_NUM_THREADS='1',
            OMP_NUM_THREADS='1', MKL_NUM_THREADS='1', BLIS_NUM_THREADS='1', VECLIB_MAXIMUM_THREADS='1', NUMEXPR_NUM_THREADS='1')
        state['scientific_children'], state['scientific_started_utc'] = 1, utc()
        began, next_pull, next_scan = time.monotonic(), time.monotonic()+1800, time.monotonic()+5
        child = subprocess.Popen(command, cwd=temporary, env=environment, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        selector = selectors.DefaultSelector()
        selector.register(child.stdout, selectors.EVENT_READ)
        decoder = codecs.getincrementaldecoder('utf-8')()
        timed_out, periodic_failure = False, None
        log_path = temporary/'scientific-child.log'
        with log_path.open('wb') as log:
            while selector.get_map():
                now = time.monotonic()
                if child.poll() is None and periodic_failure is None and now >= next_scan:
                    try:
                        available = collect()
                        if set(available)-published_targets:
                            state['intermediate_publication'] = True
                            publish(outcome_files, 'visible-exact: save complete signed96 natural conclusion')
                            published_targets.update(available)
                    except BaseException as error:
                        periodic_failure = error; child.kill()
                    next_scan = time.monotonic()+5
                if child.poll() is None and periodic_failure is None and now >= next_pull:
                    try:
                        pull(); collect()
                        if staged:
                            state['intermediate_publication'] = True
                            publish(outcome_files, 'visible-exact: preserve complete actual signed96 progress')
                    except BaseException as error:
                        periodic_failure = error; child.kill()
                    next_pull = time.monotonic()+1800
                if child.poll() is None and now-began > operation['child_timeout_seconds']:
                    child.kill(); timed_out = True
                for key, unused in selector.select(timeout=1):
                    chunk = os.read(key.fd, 65536)
                    if not chunk:
                        selector.unregister(key.fileobj); continue
                    log.write(chunk); log.flush()
                    sys.stdout.write(decoder.decode(chunk)); sys.stdout.flush()
            sys.stdout.write(decoder.decode(b'', final=True)); sys.stdout.flush()
        selector.close()
        state['actual_child_returncode'] = child.wait()
        state['scientific_finished_utc'], state['child_wall_seconds'] = utc(), time.monotonic()-began
        state['child_timeout'] = timed_out
        raw_log = log_path.read_bytes()
        state['complete_child_stdout'] = {'bytes': len(raw_log), 'sha256': sha(raw_log),
                                         'body_not_published_or_split': True}
        collect()
        if periodic_failure is not None:
            raise periodic_failure
        require(not timed_out and state['actual_child_returncode'] == 0
                and actual_state is not None and actual_state['complete'] is True
                and actual_state['actual_returncode'] == 0 and actual_state['failure'] is None
                and state['completed_natural_targets'] == owner.TARGETS,
                'all three complete actual SC natural mathematical objects')
        materialize_current(pull())
        state['complete'] = True
    except BaseException as error:
        full_trace = traceback.format_exc()
        print(full_trace, flush=True)
        state['failure'] = {'type': type(error).__name__, 'message': str(error)[:2000],
                            'traceback': full_trace[-8000:], 'full_trace_in_job_log': True}
        try:
            collect()
        except BaseException as collect_error:
            state['output_collection_failure'] = {'type': type(collect_error).__name__, 'message': str(collect_error)[:2000]}
    state['finished_utc'], state['intermediate_publication'] = utc(), False
    try:
        publication = publish(outcome_files, 'visible-exact: preserve whole actual signed96 outcome')
        print('Published whole actual signed96 outcome '+publication['commit'], flush=True)
    except BaseException:
        traceback.print_exc()
        for path, raw in outcome_files().items():
            emit(path, raw)
        raise
    if not state['complete']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
