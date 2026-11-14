#!/usr/bin/env python3
"""Local Git integration checks: a real push race and changed README rules."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import shlex
import subprocess
import sys
import tempfile
import time
from pathlib import Path

TOPIC='topics/visible-flexible-closed-surface/'
HP=TOPIC+'HANDOFF.md'

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--publisher',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();source=args.publisher.resolve();started=time.monotonic()
    env=dict(os.environ,GIT_EDITOR='true',GIT_SEQUENCE_EDITOR='true')
    def git(cwd,*argv,input=None):
        p=subprocess.run(['git',*argv],cwd=cwd,input=input,text=True,capture_output=True,env=env)
        if p.returncode:raise RuntimeError(p.stdout+p.stderr)
        return p.stdout.strip()
    results=[]
    with tempfile.TemporaryDirectory(prefix='fd2d-rebase-publication-') as temp:
        root=Path(temp)
        for change_readme in (False,True):
            case=root/('rules_changed' if change_readme else 'foreign_race');case.mkdir()
            remote=case/'remote.git';seed=case/'seed';pub=case/'publisher';peer=case/'peer'
            git(case,'init','--bare',str(remote));git(case,'init','-b','main',str(seed))
            for key,value in [('user.name','Publication Fixture'),('user.email','fixture@example.invalid'),('commit.gpgsign','false')]:git(seed,'config',key,value)
            h='# Fixture\n\n## 2. Rules\n\n`'+'0'*40+'`（2026-11-12 16:37 UTC）\n下次pull不晚于17:37 UTC\n\n## 3. Scope\n\nFixture only.\n'
            files={'README.md':'Original rules\n','LOG.md':'Historical root log; must remain byte-identical.\n',TOPIC+'README.md':'Topic rules\n',HP:h,'foreign/data.txt':'Original foreign data\n'}
            for name,body in files.items():
                path=seed/name;path.parent.mkdir(parents=True,exist_ok=True);path.write_text(body)
            git(seed,'add','.');git(seed,'commit','-m','Fixture base');base=git(seed,'rev-parse','HEAD')
            git(seed,'remote','add','origin',str(remote));git(seed,'push','-u','origin','main');git(remote,'symbolic-ref','HEAD','refs/heads/main')
            git(case,'clone',str(remote),str(pub));git(case,'clone',str(remote),str(peer))
            for repo in (pub,peer):
                for key,value in [('user.name','Publication Fixture'),('user.email','fixture@example.invalid'),('commit.gpgsign','false')]:git(repo,'config',key,value)
            git(pub,'switch','-c','fd2d-ci-publisher','--track','origin/main')
            (peer/'foreign/data.txt').write_text('New concurrent foreign work\n')
            if change_readme:(peer/'README.md').write_text('Changed repository rules\n')
            git(peer,'add','.');git(peer,'commit','-m','Concurrent foreign work');foreign=git(peer,'rev-parse','HEAD')
            flag=case/'hook-used';hook=pub/'.git/hooks/pre-push'
            hook.write_text('#!/bin/sh\nset -eu\nif ! test -e '+shlex.quote(str(flag))+'; then\n  touch '+shlex.quote(str(flag))+'\n  env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE -u GIT_COMMON_DIR -u GIT_OBJECT_DIRECTORY -u GIT_ALTERNATE_OBJECT_DIRECTORIES git -C '+shlex.quote(str(peer))+' push origin main\nfi\n')
            hook.chmod(0o755)
            payload={HP:h.replace('0'*40,base),TOPIC+'notes/payload.txt':'Closed owned payload\n'}
            entries=[['100644',git(pub,'hash-object','-w','--stdin',input=body),name] for name,body in payload.items()]
            snapshot=case/'snapshot.json';receipt=case/'receipt.json';events=case/'events.jsonl'
            snapshot.write_text(json.dumps(dict(message='Publish fixture payload',entries=entries,handoff=payload[HP],base_commit=base)))
            p=subprocess.run([sys.executable,str(source),'--snapshot',str(snapshot),'--receipt',str(receipt),'--attempt-log',str(events)],cwd=pub,capture_output=True,text=True,env=env)
            history=[json.loads(x) for x in events.read_text().splitlines()]
            head=git(remote,'rev-parse','refs/heads/main')
            actual_log=git(remote,'show',head+':LOG.md')+'\n'
            assert git(remote,'rev-parse',base+':LOG.md')==git(remote,'rev-parse',head+':LOG.md')
            assert actual_log==files['LOG.md']
            assert git(remote,'show',head+':foreign/data.txt')=='New concurrent foreign work'
            pulls=[e for e in history if 'pull_exit' in e];pushes=[e for e in history if 'push_exit' in e]
            args.output.write_text(json.dumps(dict(status='case_observed_before_assertions',case=case.name,exit_code=p.returncode,history=history,stdout=p.stdout,stderr=p.stderr),indent=2)+'\n')
            print(json.dumps(dict(case=case.name,exit_code=p.returncode,pulls=len(pulls),pushes=[e['push_exit'] for e in pushes])),flush=True)
            assert len(pulls)==2 and pulls[1]['pull_command']=='git pull --rebase --no-stat origin main'
            assert pushes[0]['push_exit']!=0
            if change_readme:
                assert p.returncode==78,(p.returncode,p.stdout,p.stderr)
                assert head==foreign and not receipt.exists()
                assert pulls[-1]['readme_diff_empty'] is False
                assert git(remote,'ls-tree',head,'--',TOPIC+'notes/payload.txt')==''
            else:
                assert p.returncode==0,(p.returncode,p.stdout,p.stderr)
                paid=json.loads(receipt.read_text());assert paid['attempt']==2 and paid['rules_read_sha']==foreign
                assert git(remote,'show',head+':'+TOPIC+'notes/payload.txt')=='Closed owned payload'
                assert foreign in git(remote,'show',head+':'+HP)
                assert pushes[-1]['push_exit']==0
            results.append(dict(case=case.name,exit_code=p.returncode,root_log_unchanged=True,foreign_work_preserved=True,
                actual_pull_commands=[e['pull_command'] for e in pulls],push_exit_codes=[e['push_exit'] for e in pushes],
                changed_rules_stop_before_remote_payload=change_readme,
                receipt=json.loads(receipt.read_text()) if receipt.exists() else None,
                history=history,stdout=p.stdout,stderr=p.stderr))
    report=dict(schema='fd2d-local-git-rebase-publication-check-v1',completed=True,
        source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        no_external_remote_used=True,no_credentials_used=True,seconds=time.monotonic()-started,cases=results)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(completed=True,seconds=report['seconds'],cases=[dict(case=x['case'],exit_code=x['exit_code'],push_exit_codes=x['push_exit_codes']) for x in results])))

if __name__=='__main__':main()
