#!/usr/bin/env python3
"""Publish explicit closed files; never write root LOG, never force push.

The worktree is the disposable CI publisher clone.  Every rejected normal
main push is followed immediately by literal git pull --rebase, then both
README differences are checked before another mutation or push.  Changed
rules or overlapping owned edits are returned to the research owner.
"""
from __future__ import annotations
import argparse
import datetime
import json
import re
import subprocess
import sys
import time
from pathlib import Path

TOPIC='topics/visible-flexible-closed-surface/'
HANDOFF=TOPIC+'HANDOFF.md'
WORKFLOW='.github/workflows/visible-flex-fd2d-publish-checkpoint.yml'
README_PATHS=['README.md',TOPIC+'README.md']


def run(argv,input=None,check=True):
    result=subprocess.run(argv,input=input,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    if check and result.returncode:
        raise RuntimeError(result.stdout)
    return result


def rules_update(text,base,now):
    a,b=text.index('## 2.'),text.index('## 3.')
    part=re.sub(r'`[0-9a-f]{40}`（[0-9-]{10} [0-9:]+ UTC）',
        f'`{base}`（{now:%Y-%m-%d %H:%M} UTC）',text[a:b],count=1)
    part=re.sub(r'下次(?:pull)?不晚于[0-9:]+ UTC',
        f'下次pull不晚于{now+datetime.timedelta(hours=1):%H:%M} UTC',part,count=1)
    result=text[:a]+part+text[b:]
    if len(result.encode())>=10000:
        raise ValueError('HANDOFF exceeds repository limit')
    return result


def versions(ref,paths):
    out={}
    for row in run(['git','ls-tree','-r','-z',ref,'--',*paths]).stdout.split('\0'):
        if row:
            bits,path=row.split('\t',1);out[path]=bits.split()[2]
    return out


def blob(text):
    return run(['git','hash-object','-w','--stdin'],input=text).stdout.strip()


# Canonical tree overlay is copied unchanged from the previously used
# identity-checked codec.  It never reads or rewrites unrelated blobs.
def overlay(tree,patch):
 entries={}
 if tree:
  for row in run(['git','ls-tree','-z',tree]).stdout.split('\0'):
   if not row:continue
   bits,name=row.split('\t',1);mode,kind,sha=bits.split();entries[name]=(mode,kind,sha)
 groups={}
 for path,(mode,sha) in patch.items():
  first,sep,rest=path.partition('/')
  if sep:groups.setdefault(first,{})[rest]=(mode,sha)
  else:entries[first]=(mode,'blob',sha)
 for name,sub in groups.items():
  previous=entries.get(name)
  if previous and previous[1]!='tree':raise RuntimeError('Parent path is not a directory')
  entries[name]=('040000','tree',overlay(previous[2] if previous else None,sub))
 # Canonical tree encoding avoids mktree's per-entry object lookup in this
 # large partial clone. Entries still come only from fresh main or explicit
 # owned hashes. This exact encoding reproduced an existing 5,040-entry tree.
 encoded=[]
 for name,(mode,kind,sha) in entries.items():
  raw_name=name.encode('utf-8')
  if b'\0' in raw_name or b'/' in raw_name:raise ValueError('Invalid tree basename')
  key=raw_name+(b'/' if kind=='tree' else b'')
  value=format(int(mode,8),'o').encode()+b' '+raw_name+b'\0'+bytes.fromhex(sha)
  encoded.append((key,value))
 body=b''.join(value for _,value in sorted(encoded))
 process=subprocess.run(['git','hash-object','-w','-t','tree','--stdin'],input=body,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 if process.returncode:raise RuntimeError(process.stderr.decode())
 return process.stdout.decode().strip()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--snapshot',type=Path,required=True)
    parser.add_argument('--receipt',type=Path,required=True)
    parser.add_argument('--attempt-log',type=Path)
    args=parser.parse_args()
    def record(value):
        print(json.dumps(value),flush=True)
        if args.attempt_log:
            with args.attempt_log.open('a') as f:f.write(json.dumps(value)+'\n')
    snapshot=json.loads(args.snapshot.read_text())
    paths=[x[2] for x in snapshot['entries']]
    desired={path:sha for mode,sha,path in snapshot['entries']}
    if len(paths)!=len(set(paths)) or HANDOFF not in paths:
        raise ValueError('Explicit unique owned paths including HANDOFF required')
    if any(not (p.startswith(TOPIC) or p==WORKFLOW) for p in paths):
        raise ValueError('Only this topic and its publication workflow may be patched')
    if any('..' in Path(p).parts for p in paths):
        raise ValueError('Invalid owned path')
    branch=run(['git','symbolic-ref','--short','HEAD']).stdout.strip()
    if branch!='fd2d-ci-publisher':
        raise ValueError('Use the disposable fd2d-ci-publisher worktree')
    if run(['git','status','--porcelain','--untracked-files=no']).stdout.strip():
        raise ValueError('Disposable publication worktree must be clean')
    old=re.search(r'`([0-9a-f]{40})`',snapshot['handoff'].split('## 2.',1)[1].split('## 3.',1)[0]).group(1)
    attempt=1
    def pull_and_read(previous):
        # This is also the first operation after every rejected main push.
        pulled=run(['git','pull','--rebase','--no-stat','origin','main'],check=False)
        base=run(['git','rev-parse','origin/main']).stdout.strip()
        diff=run(['git','diff',previous,base,'--',*README_PATHS]).stdout
        record(dict(attempt=attempt,pull_command='git pull --rebase --no-stat origin main',
            pull_exit=pulled.returncode,readme_previous=previous,readme_current=base,
            readme_diff_empty=not bool(diff)))
        if diff:
            print(diff,flush=True)
            return base,78
        if pulled.returncode:
            print(pulled.stdout,flush=True)
            conflicts=run(['git','diff','--name-only','--diff-filter=U'],check=False).stdout.splitlines()
            record(dict(attempt=attempt,status='rebase_requires_actual_reconciliation',paths=conflicts))
            return base,79 if conflicts else pulled.returncode
        return base,0
    base,code=pull_and_read(old)
    if code:return code
    previous,current=versions(snapshot['base_commit'],paths),versions(base,paths)
    conflicts=[p for p in paths if previous.get(p)!=current.get(p) and current.get(p)!=desired.get(p)]
    if conflicts:
        record(dict(attempt=attempt,status='overlapping_remote_changes_require_reading',paths=conflicts))
        return 79
    h=rules_update(snapshot['handoff'],base,datetime.datetime.now(datetime.timezone.utc))
    patch={p:(mode,sha) for mode,sha,p in snapshot['entries'] if p!=HANDOFF}
    patch[HANDOFF]=('100644',blob(h))
    tree=overlay(run(['git','rev-parse',base+'^{tree}']).stdout.strip(),patch)
    commit=run(['git','commit-tree',tree,'-p',base],input=snapshot['message']+'\n').stdout.strip()
    # This is our own fresh, unpublished commit in an isolated CI clone.
    run(['git','reset','--hard',commit])
    old=base
    while True:
        started=time.monotonic()
        commit=run(['git','rev-parse','HEAD']).stdout.strip()
        changed=run(['git','diff','--name-only',base,commit]).stdout.splitlines()
        if not set(changed).issubset(paths):
            raise RuntimeError('Rebased commit would alter an unowned path')
        actual=versions(commit,paths)
        mismatch=[p for p in paths if p!=HANDOFF and actual.get(p)!=desired[p]]
        if mismatch:
            record(dict(attempt=attempt,status='closed_payload_changed_during_rebase',paths=mismatch))
            return 79
        pushed=run(['git','push','origin','HEAD:refs/heads/main'],check=False)
        record(dict(attempt=attempt,push_exit=pushed.returncode,commit=commit,
            seconds=time.monotonic()-started,message=pushed.stdout))
        if pushed.returncode==0:
            receipt=dict(commit=commit,rules_read_sha=base,attempt=attempt,
                utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                method='ordinary terminal Git; literal pull --rebase after each rejected main push; root LOG untouched')
            args.receipt.write_text(json.dumps(receipt,indent=2)+'\n')
            return 0
        race=('fetch first' in pushed.stdout or 'non-fast-forward' in pushed.stdout or
              ("cannot lock ref 'refs/heads/main': is at" in pushed.stdout and 'but expected' in pushed.stdout))
        if not race:return pushed.returncode
        attempt+=1
        base,code=pull_and_read(old)
        if code:return code
        old=base
        mismatch=[p for p,sha in versions('HEAD',paths).items() if p!=HANDOFF and sha!=desired[p]]
        if mismatch:
            record(dict(attempt=attempt,status='closed_payload_changed_during_rebase',paths=mismatch))
            return 79
        hp=Path(HANDOFF)
        hp.write_text(rules_update(hp.read_text(),base,datetime.datetime.now(datetime.timezone.utc)))
        run(['git','add','--',HANDOFF])
        if run(['git','diff','--cached','--quiet'],check=False).returncode:
            if run(['git','rev-parse','HEAD']).stdout.strip()==base:
                run(['git','commit','-m',snapshot['message']+' (rule checkpoint)'])
            else:
                # Only the own unpublished commit is amended; main history
                # and every already pushed commit remain untouched.
                run(['git','commit','--amend','--no-edit'])


if __name__=='__main__':
    sys.exit(main())
