#!/usr/bin/env python3
"""Cache a topic's new objects in small normal pushes before publishing main.

This version uses Git tree objects only and never constructs a repository-wide
index. Only the uniquely named owned cache branch is advanced. Every intermediate
tree preserves the base outside this topic. Source and main are untouched.
The caller supplies ephemeral CLI authentication; no credentials are saved.
"""
from __future__ import annotations

import argparse
import datetime
import json
import os
from pathlib import Path
import subprocess
import tempfile
import time

from publish_topic_checkpoint import update_read_marker


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--active', type=Path, required=True)
    ap.add_argument('--publish', type=Path, required=True)
    ap.add_argument('--source', required=True)
    ap.add_argument('--base', required=True)
    ap.add_argument('--read', required=True)
    ap.add_argument('--state', type=Path, required=True)
    ap.add_argument('--topic', default='topics/visible-flex-larger-amplitude')
    ap.add_argument('--batch-bytes', type=int, default=8_000_000)
    args = ap.parse_args()
    active, pub = args.active.resolve(), args.publish.resolve()
    if active == pub or args.batch_bytes < 5_000_000:
        raise ValueError('Require a separate publisher and at least one legal file per batch')
    if len(Path(args.topic).parts) != 2 or not args.topic.startswith('topics/'):
        raise ValueError('Expected one topic')

    def git(*command, input=None, env=None, check=True):
        result = subprocess.run(['git', '-c', 'gc.auto=0', *command], cwd=pub,
            input=input, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if check and result.returncode:
            raise RuntimeError('git ' + command[0] + ': ' + result.stderr.decode()[-3000:])
        return result

    def value(*command):
        return git(*command).stdout.decode().strip()

    source, base = value('rev-parse', args.source+'^{commit}'), value('rev-parse', args.base+'^{commit}')
    branch = 'agent-visible-larger-cache-' + source[:20]
    if args.state.exists():
        state = json.loads(args.state.read_text())
        if (state['source'], state['base'], state['branch'], state['topic']) != (source, base, branch, args.topic):
            raise ValueError('The saved object-cache identity differs')
    else:
        state = dict(source=source, base=base, branch=branch, topic=args.topic,
                     read=args.read, batches=[], completed_pushes=[], complete_cache=False,
                     main_changed=False)

    def save():
        state['updated_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        tmp = args.state.with_suffix(args.state.suffix+'.tmp')
        tmp.write_text(json.dumps(state, indent=2)+'\n')
        tmp.replace(args.state)

    def review_pull():
        git('pull', '--quiet', '--ff-only', 'origin', 'main')
        head = value('rev-parse', 'HEAD')
        difference = git('diff', state['read'], head, '--', 'README.md', args.topic+'/README.md').stdout
        if difference:
            state.update(blocked='Read changed README diff before continuing', pulled=head)
            save()
            print(difference.decode(), flush=True)
            raise SystemExit(50)
        state['read'] = head
        handoff = active/args.topic/'HANDOFF.md'
        handoff.write_text(update_read_marker(handoff.read_text(), head))
        state['last_pull_reviewed_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        save()
        print(json.dumps(dict(pulled=head, readme_changed=False)), flush=True)

    review_pull()
    last_pull = time.monotonic()
    if not state['batches']:
        paths = git('diff', '--no-renames', '--name-only', '-z', base, source, '--', args.topic).stdout.split(b'\0')
        changed_paths = [p.decode() for p in paths if p]
        source_entries = {}
        for entry in git('ls-tree', '-r', '-z', source, '--', args.topic).stdout.split(b'\0'):
            if entry:
                metadata, raw_path = entry.split(b'\t', 1)
                source_entries[raw_path.decode()] = metadata.decode().split()
        oids = [source_entries[path][2] for path in changed_paths if path in source_entries]
        sizes = {}
        if oids:
            checked = git('cat-file', '--batch-check=%(objectname) %(objecttype) %(objectsize)',
                          input=('\n'.join(oids)+'\n').encode()).stdout.decode().splitlines()
            for item in checked:
                oid, kind, size = item.split()
                if kind != 'blob':
                    raise ValueError('Expected existing source blobs')
                sizes[oid] = int(size)
        changes = []
        for path in changed_paths:
            if not path.startswith(args.topic+'/'):
                raise ValueError('A change escaped the topic')
            if path in source_entries:
                mode, kind, oid = source_entries[path]
                size = sizes[oid]
                if kind != 'blob' or size >= 5_000_000:
                    raise ValueError('Invalid source blob or repository file size')
            else:
                mode, oid, size = '0', '0'*40, 0
            changes.append(dict(path=path, mode=mode, oid=oid, bytes=size))
        groups, current, count = [], [], 0
        for change in changes:
            if current and count+change['bytes'] > args.batch_bytes:
                groups.append(current)
                current, count = [], 0
            current.append(change)
            count += change['bytes']
        if current:
            groups.append(current)
        def update_tree(tree, records):
            entries = {}
            if tree:
                for entry in git('ls-tree', '-z', tree).stdout.split(b'\0'):
                    if entry:
                        metadata, name = entry.split(b'\t', 1)
                        entries[name.decode()] = metadata.decode().split()
            children = {}
            for parts, record in records:
                children.setdefault(parts[0], []).append((parts[1:], record))
            for name, remaining in children.items():
                leaves = [(parts, r) for parts, r in remaining if not parts]
                if leaves:
                    if len(remaining) != 1:
                        raise ValueError('A source path is both a file and a directory')
                    record = leaves[0][1]
                    if record['mode'] == '0':
                        entries.pop(name, None)
                    else:
                        entries[name] = [record['mode'], 'blob', record['oid']]
                else:
                    prior = entries.get(name)
                    if prior and prior[1] != 'tree':
                        raise ValueError('Directory path collides with a blob')
                    child, empty = update_tree(prior[2] if prior else None, remaining)
                    if empty:
                        entries.pop(name, None)
                    else:
                        entries[name] = ['040000', 'tree', child]
            data = b''.join((' '.join(metadata)+'\t'+name).encode()+b'\0'
                            for name, metadata in entries.items())
            oid = git('mktree', '-z', '--missing', input=data).stdout.decode().strip()
            return oid, not bool(entries)
        parent = base
        for i, group in enumerate(groups):
            tree = value('rev-parse', parent+'^{tree}')
            tree, _ = update_tree(tree, [(Path(r['path']).parts, r) for r in group])
            message = ('Cache topic objects '+str(i+1)+'/'+str(len(groups))+' for '+source+'\n\nTemporary owned upload branch; main is unchanged.\n').encode()
            commit = git('commit-tree', tree, '-p', parent, input=message).stdout.decode().strip()
            state['batches'].append(dict(index=i, commit=commit, parent=parent,
                bytes=sum(r['bytes'] for r in group), files=group))
            parent = commit
            print(json.dumps(dict(prepared_batch=i, files=len(group), bytes=state['batches'][-1]['bytes'])), flush=True)
        save()
        final_topic = value('rev-parse', parent+':'+args.topic)
        if final_topic != value('rev-parse', source+':'+args.topic):
            raise ValueError('The complete cached topic differs from the immutable source')
        state['complete_source_topic_identity_checked'] = True
        save()
    if not state['batches']:
        raise ValueError('No new topic objects to cache')
    if value('rev-parse', state['batches'][-1]['commit']+':'+args.topic) != value('rev-parse', source+':'+args.topic):
        raise ValueError('The saved cache plan does not reproduce the complete source topic')
    state['complete_source_topic_identity_checked'] = True
    save()
    remote = value('ls-remote', '--heads', 'origin', branch)
    if remote:
        remote_head = remote.split()[0]
        known = [r['commit'] for r in state['batches']]
        if remote_head not in known:
            raise ValueError('Refusing to modify an unrecognized remote branch')
        start = known.index(remote_head)+1
    else:
        if state['completed_pushes']:
            raise ValueError('A previously acknowledged owned branch disappeared')
        start = 0
    for item in state['batches'][start:]:
        if time.monotonic()-last_pull >= 3000:
            review_pull()
            last_pull = time.monotonic()
        state['active_push'] = {k:item[k] for k in ('index', 'commit', 'bytes')}
        save()
        print(json.dumps(dict(uploading_batch=item['index'], bytes=item['bytes'])), flush=True)
        result = git('push', '--porcelain', 'origin', item['commit']+':refs/heads/'+branch, check=False)
        if result.returncode:
            remote = value('ls-remote', '--heads', 'origin', branch)
            if not remote or remote.split()[0] != item['commit']:
                state['failed_push'] = dict(index=item['index'], exitcode=result.returncode,
                    diagnostic=result.stderr.decode()[-3000:])
                save()
                print(result.stderr.decode()[-3000:], flush=True)
                raise SystemExit(result.returncode)
        state['completed_pushes'].append(dict(index=item['index'], commit=item['commit'],
            bytes=item['bytes'], push_exitcode=result.returncode,
            remote_commit_verified_after_disconnect=bool(result.returncode)))
        state['active_push'] = None
        save()
        print(json.dumps(dict(cached_batch=item['index'], commit=item['commit'])), flush=True)
    state['complete_cache'] = True
    save()
    print(json.dumps(dict(complete_cache=True, branch=branch, source=source,
                         batches=len(state['batches']), read=state['read'])), flush=True)


if __name__ == '__main__':
    main()
