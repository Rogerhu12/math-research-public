#!/usr/bin/env python3
"""Push only an explicit payload to a new owned branch, then let CI publish.

The checkpoint has its own root commit. It does not copy the complete main
tree or make unrelated partial-clone blobs reachable from its push. Main is
untouched here; the CI publisher independently pulls main, reads rule diffs,
checks owned-file overlaps, preserves its full tree, and pushes normally.
"""
import argparse
import datetime
import json
import re
import subprocess
import sys
from pathlib import Path


def run(argv, data=None, check=True):
    result = subprocess.run(argv, input=data, text=True, capture_output=True)
    if check and result.returncode:
        raise RuntimeError(result.stdout+result.stderr)
    return result


def update_rules(text, base, now):
    a, b = text.index('## 2.'), text.index('## 3.')
    section = re.sub(r'\x60[0-9a-f]{40}\x60（[0-9-]{10} [0-9:]+ UTC）',
        f'\x60{base}\x60（{now:%Y-%m-%d %H:%M} UTC）', text[a:b], count=1)
    section = re.sub(r'下次(?:pull)?不晚于[0-9:]+ UTC',
        f'下次pull不晚于{now+datetime.timedelta(hours=1):%H:%M} UTC', section, count=1)
    result = text[:a]+section+text[b:]
    assert len(result.encode()) < 10000
    return result


def tree(entries):
    direct, groups = {}, {}
    for path, (mode, sha) in entries.items():
        first, sep, rest = path.partition('/')
        if sep:
            groups.setdefault(first, {})[rest] = (mode, sha)
        else:
            direct[first] = (mode, sha, False)
    for name, sub in groups.items():
        direct[name] = ('40000', tree(sub), True)
    encoded = []
    for name, (mode, sha, is_tree) in direct.items():
        raw = name.encode()
        if b'\0' in raw or b'/' in raw:
            raise ValueError('Invalid tree name')
        key = raw+(b'/' if is_tree else b'')
        value = format(int(mode, 8), 'o').encode()+b' '+raw+b'\0'+bytes.fromhex(sha)
        encoded.append((key, value))
    result = subprocess.run(['git','hash-object','-w','-t','tree','--stdin'],
        input=b''.join(v for _,v in sorted(encoded)), capture_output=True)
    if result.returncode:
        raise RuntimeError(result.stderr.decode())
    return result.stdout.decode().strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--snapshot', type=Path, required=True)
    parser.add_argument('--receipt', type=Path, required=True)
    parser.add_argument('--live-handoff', type=Path, required=True)
    parser.add_argument('--checkpoint-ref', required=True)
    args = parser.parse_args()
    if not args.checkpoint_ref.startswith('refs/heads/visible-flex-fd2d-ci-publish-'):
        raise ValueError('An explicit new owned CI branch is required')
    run(['git','check-ref-format',args.checkpoint_ref])
    snapshot = json.loads(args.snapshot.read_text())
    hp = 'topics/visible-flexible-closed-surface/HANDOFF.md'
    live = args.live_handoff.read_text()
    old = re.search(r'\x60([0-9a-f]{40})\x60',
        live.split('## 2.',1)[1].split('## 3.',1)[0]).group(1)
    pull = run(['git','pull','--ff-only','--no-stat','origin','main'], check=False)
    base = run(['git','rev-parse','origin/main']).stdout.strip()
    diff = run(['git','diff',old,base,'--','README.md',
                'topics/visible-flexible-closed-surface/README.md']).stdout
    print(json.dumps(dict(pull_exit=pull.returncode, previous=old,
        current=base, readme_diff_empty=not bool(diff))), flush=True)
    if diff:
        print(diff, flush=True)
        return 78
    if pull.returncode:
        print(pull.stdout+pull.stderr, flush=True)
        return pull.returncode
    now = datetime.datetime.now(datetime.timezone.utc)
    args.live_handoff.write_text(update_rules(args.live_handoff.read_text(), base, now))
    payload_handoff = update_rules(snapshot['handoff'], base, now)
    entries = {path:(mode,sha) for mode,sha,path in snapshot['entries'] if path != hp}
    for path in entries:
        if not (path.startswith('topics/visible-flexible-closed-surface/') or
                path == '.github/workflows/visible-flex-fd2d-publish-checkpoint.yml'):
            raise ValueError('Payload contains an unowned path')
    entries[hp] = ('100644', run(['git','hash-object','-w','--stdin'], payload_handoff).stdout.strip())
    # Context files are copied by identity. They are not in the CI owned-path
    # write list, so the runner only reads the fresh main versions.
    for path in ('README.md','topics/visible-flexible-closed-surface/README.md'):
        row = run(['git','ls-tree',base,'--',path]).stdout.strip()
        mode, unused_kind, sha = row.split('\t',1)[0].split()
        entries[path] = (mode, sha)
    commit = run(['git','commit-tree',tree(entries)],
        snapshot['message']+'\n\nExplicit closed payload; main publication is performed by the CI Git publisher.\n').stdout.strip()
    print(json.dumps(dict(payload_commit=commit, files=len(entries),
        parentless_payload=True, main_untouched=True)), flush=True)
    pushed = run(['git','push','origin',commit+':'+args.checkpoint_ref], check=False)
    print(json.dumps(dict(push_exit=pushed.returncode, message=pushed.stdout+pushed.stderr)), flush=True)
    if pushed.returncode:
        return pushed.returncode
    receipt = dict(commit=commit, ref=args.checkpoint_ref, rules_read_sha=base,
        readme_diff_empty=True, pull_exit=0, push_exit=0,
        utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        method='Ordinary terminal Git push of a self-contained explicit payload root; main integration delegated only to the existing Git publisher',
        main_publication_completed=False)
    args.receipt.write_text(json.dumps(receipt,indent=2)+'\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
