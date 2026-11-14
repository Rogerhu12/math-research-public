#!/usr/bin/env python3
"""Publish one immutable topic checkpoint with negotiated object reuse.

Credentials must be supplied only through the caller's ephemeral environment.
The active computation checkout is never reset, rebased, or checked out here.
The disposable publication checkout must be dedicated to this program.
Every actual pull and every fresh main fetch compares both README files.
A real pull is performed initially and at least every fifty minutes. Retry
construction uses FETCH_HEAD so a large worktree checkout is outside the
compare-and-push interval. No force push or upstream-topic overwrite is allowed.
A changed
README or upstream topic stops the program for the caller to read/reconcile.
Normal non-fast-forward races retry; no force push is supported.
"""
import argparse
import datetime
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time


def git(repo, *args, data=None, check=True):
    p = subprocess.run(['git', '-C', str(repo), *args], input=data,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if check and p.returncode:
        sys.stderr.buffer.write(p.stderr)
        raise RuntimeError('git operation failed: ' + ' '.join(args[:3]))
    return p


def value(repo, *args):
    return git(repo, *args).stdout.decode().strip()


def replace_child(repo, tree, name, oid, object_type='tree', mode='040000'):
    entries = git(repo, 'ls-tree', '-z', tree).stdout.split(b'\0')
    found = False
    out = []
    for entry in entries:
        if not entry:
            continue
        meta, child = entry.split(b'\t', 1)
        if child.decode() == name:
            old_mode, old_type, _ = meta.decode().split()
            if old_type != object_type or int(old_mode, 8) != int(mode, 8):
                raise ValueError('Unexpected tree entry type: ' + name)
            meta = f'{mode} {object_type} {oid}'.encode()
            found = True
        out.append(meta + b'\t' + child + b'\0')
    if not found:
        raise ValueError('Missing tree entry: ' + name)
    return git(repo, 'mktree', '-z', '--missing', data=b''.join(out)).stdout.decode().strip()


def update_read_marker(text, commit):
    pattern = r'(两README最近确认提交`)\w{40}(`)'
    updated, count = re.subn(pattern, lambda m: m[1] + commit + m[2], text)
    if count != 1:
        raise ValueError('HANDOFF must have exactly one reviewed-README marker')
    if len(updated.encode()) >= 10000:
        raise ValueError('HANDOFF must remain below 10000 bytes')
    return updated


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--active', type=Path, required=True)
    p.add_argument('--publish', type=Path, required=True)
    p.add_argument('--topic', default='topics/visible-flex-larger-amplitude')
    p.add_argument('--commit', required=True)
    p.add_argument('--base', required=True, help='last accepted remote topic state')
    p.add_argument('--read', required=True, help='last README commit read by operator')
    p.add_argument('--status', type=Path, required=True)
    p.add_argument('--message-file', type=Path, required=True)
    p.add_argument('--attempts', type=int, default=24)
    p.add_argument('--preupload', action='store_true')
    p.add_argument('--cache-ref', required=True)
    p.add_argument('--cache-tip', required=True)
    a = p.parse_args()
    active, pub = a.active.resolve(), a.publish.resolve()
    if active == pub or active in pub.parents or pub in active.parents:
        raise ValueError('Publication checkout must be a separate sibling')
    parts = Path(a.topic).parts
    if len(parts) != 2 or parts[0] != 'topics' or '..' in parts:
        raise ValueError('Expected topics/<topic-name>')
    source = value(active, 'rev-parse', a.commit + '^{commit}')
    def metadata_ref(ref):
        # Published graft commits live in the publication object database;
        # the active branch deliberately retains its original ancestry.
        for repository in (pub, active):
            if not (repository / '.git').is_dir():
                continue
            result = git(repository, 'rev-parse', ref + '^{commit}', check=False)
            if result.returncode == 0:
                return repository, result.stdout.decode().strip()
        raise ValueError('Recorded publication/read commit is unavailable: ' + ref)
    base_repository, base = metadata_ref(a.base)
    _, read = metadata_ref(a.read)
    source_topic = value(active, 'rev-parse', source + ':' + a.topic)
    if not a.cache_ref.startswith('agent-visible-larger-cache-') or not re.fullmatch(r'[0-9a-f]{40}', a.cache_tip):
        raise ValueError('Expected an owned immutable object-cache ref and exact tip')
    remote_cache = value(pub, 'ls-remote', '--heads', 'origin', a.cache_ref).split()
    if remote_cache != [a.cache_tip, 'refs/heads/' + a.cache_ref]:
        raise ValueError('Owned cache tip has changed or disappeared')
    if value(pub, 'rev-parse', a.cache_tip + ':' + a.topic) != source_topic:
        raise ValueError('Cache topic is not the complete requested source topic')
    base_topic = value(base_repository, 'rev-parse', base + ':' + a.topic)
    source_handoff = git(active, 'show', source + ':' + a.topic + '/HANDOFF.md').stdout.decode()
    message = a.message_file.read_bytes()
    if not message.strip():
        raise ValueError('Empty commit message')
    state = dict(source=source, base=base, read=read, published=None, attempts=[], cache_ref=a.cache_ref, cache_tip=a.cache_tip, object_reuse='negotiated-push-with-verified-cache-parent')

    def save():
        state['updated_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        a.status.parent.mkdir(parents=True, exist_ok=True)
        temp = a.status.with_suffix(a.status.suffix + '.tmp')
        temp.write_text(json.dumps(state, ensure_ascii=False, indent=2) + '\n')
        temp.replace(a.status)

    if not pub.exists():
        pub.parent.mkdir(parents=True, exist_ok=True)
        clone = subprocess.run(['git', '-c', 'gc.auto=0', 'clone', '--shared',
                                '--no-checkout', str(active), str(pub)],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if clone.returncode:
            sys.stderr.buffer.write(clone.stderr)
            raise RuntimeError('Cannot initialize dedicated publication checkout')
    if not (pub / '.git').is_dir():
        raise ValueError('Publication path is not a normal dedicated checkout')
    for key, val in [('gc.auto', '0'), ('maintenance.auto', 'false'),
                     ('pack.threads', '1'), ('pack.windowMemory', '32m'),
                     ('pack.deltaCacheSize', '32m'), ('user.name', 'Codex'),
                     ('user.email', 'codex@openai.com')]:
        git(pub, 'config', key, val)
    git(pub, 'remote', 'set-url', 'origin', 'https://github.com/Rogerhu12/math-research.git')
    git(pub, 'config', 'remote.origin.fetch', '+refs/heads/main:refs/remotes/origin/main')
    # A shared clone does not inherit the source partial-clone configuration.
    # Keep the publication fetch filtered so a thin pack cannot assume that
    # promised old blobs exist in the alternate object database.
    git(pub, 'config', 'core.repositoryformatversion', '1')
    git(pub, 'config', 'remote.origin.promisor', 'true')
    git(pub, 'config', 'remote.origin.partialclonefilter', 'blob:none')
    git(pub, 'sparse-checkout', 'init', '--cone')
    git(pub, 'sparse-checkout', 'set', a.topic)
    git(pub, 'fetch', '--quiet', 'origin', 'main')
    git(pub, 'reset', '--hard', 'origin/main')
    temporary_branch = None
    if a.preupload:
        temporary_branch = 'agent-visible-larger-source-' + source[:20]
        if value(pub, 'ls-remote', '--heads', 'origin', temporary_branch):
            raise ValueError('Refusing to overwrite an existing temporary branch')
        git(pub, 'push', '--porcelain', 'origin', source + ':refs/heads/' + temporary_branch)
        state['temporary_branch'] = temporary_branch
        save()

    last_actual_pull = None
    state['synchronizations'] = []

    def check_readmes(head, operation):
        nonlocal read
        difference = git(pub, 'diff', read, head, '--', 'README.md', a.topic + '/README.md').stdout
        entry = dict(operation=operation, head=head, readme_changed=bool(difference),
                     utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
        state['synchronizations'].append(entry)
        if difference:
            state['blocked'] = 'README changed: read this diff and resume with its commit'
            save()
            sys.stdout.buffer.write(difference)
            return False
        read = head
        state['read'] = read
        live_handoff = active / a.topic / 'HANDOFF.md'
        updated = update_read_marker(live_handoff.read_text(), read)
        temporary = live_handoff.with_name('HANDOFF.publication.tmp')
        temporary.write_text(updated)
        temporary.replace(live_handoff)
        entry['readme_reviewed'] = read
        save()
        return True

    for attempt in range(1, a.attempts + 1):
        if last_actual_pull is None or time.monotonic()-last_actual_pull >= 3000:
            git(pub, 'pull', '--quiet', '--ff-only', 'origin', 'main')
            pulled_head = value(pub, 'rev-parse', 'HEAD')
            if not check_readmes(pulled_head, 'pull --ff-only'):
                return 50
            last_actual_pull = time.monotonic()
        git(pub, 'fetch', '--quiet', '--filter=blob:none', 'origin', 'main')
        head = value(pub, 'rev-parse', 'FETCH_HEAD')
        refreshed_at = time.monotonic()
        if not check_readmes(head, 'fetch --filter=blob:none'):
            return 50
        record = dict(attempt=attempt, fetched=head, readme_changed=False, readme_reviewed=read)
        state['attempts'].append(record)
        if value(pub, 'rev-parse', head + ':' + a.topic) != base_topic:
            state['blocked'] = 'Upstream topic changed: reconcile before publishing'
            save()
            print(json.dumps(record), flush=True)
            return 51
        saved_handoff = update_read_marker(source_handoff, read).encode()
        blob = git(pub, 'hash-object', '-w', '--stdin', data=saved_handoff).stdout.decode().strip()
        new_topic = replace_child(pub, source_topic, 'HANDOFF.md', blob, 'blob', '100644')
        changed = value(pub, 'diff', '--name-only', source_topic, new_topic)
        if changed not in ('', 'HANDOFF.md'):
            raise AssertionError('Source topic changed outside its README marker')
        topics_tree = value(pub, 'rev-parse', head + ':topics')
        new_topics = replace_child(pub, topics_tree, parts[1], new_topic)
        root_tree = value(pub, 'rev-parse', head + '^{tree}')
        new_root = replace_child(pub, root_tree, 'topics', new_topics)
        names = value(pub, 'diff', '--name-only', root_tree, new_root).splitlines()
        if not names or any(not x.startswith(a.topic + '/') for x in names):
            raise AssertionError('Publication must change only the requested topic')
        commit = git(pub, 'commit-tree', new_root, '-p', head, '-p', a.cache_tip, data=message).stdout.decode().strip()
        record.update(candidate=commit, files=len(names), fetch_to_candidate_seconds=time.monotonic()-refreshed_at)
        save()
        print(json.dumps(record), flush=True)
        pushed = git(pub, '-c', 'push.negotiate=true', 'push', '--porcelain', '--progress', 'origin', commit + ':refs/heads/main', check=False)
        record['pack_progress'] = pushed.stderr.decode(errors='replace')[-6000:]
        record['push_exit'] = pushed.returncode
        record['fetch_to_push_result_seconds'] = time.monotonic()-refreshed_at
        if pushed.returncode == 0:
            state['published'] = commit
            save()
            print(json.dumps(dict(published=commit, source=source, read=read, files=len(names))), flush=True)
            if temporary_branch is not None:
                deletion = git(pub, 'push', '--porcelain', 'origin', '--delete', temporary_branch, check=False)
                state['temporary_branch_deleted'] = deletion.returncode == 0
                save()
            return 0
        diagnostic = (pushed.stdout + pushed.stderr).decode(errors='replace')
        record['push_diagnostic'] = diagnostic[-3000:]
        save()
        advertised_race = ('[rejected]' in diagnostic and
                           ('fetch first' in diagnostic or 'non-fast-forward' in diagnostic))
        locked_race = ('[remote rejected]' in diagnostic and re.search(
            r"cannot lock ref 'refs/heads/main': is at [0-9a-f]{40} but expected [0-9a-f]{40}",
            diagnostic) is not None)
        if not (advertised_race or locked_race):
            sys.stderr.write(diagnostic)
            return pushed.returncode or 1
        print('Normal main race; refreshing main and checking both READMEs again.', flush=True)
    state['blocked'] = 'Normal main races exhausted configured attempts; state preserved'
    save()
    return 52


if __name__ == '__main__':
    raise SystemExit(main())
