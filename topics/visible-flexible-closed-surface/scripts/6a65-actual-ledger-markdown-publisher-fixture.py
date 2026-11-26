#!/usr/bin/env python3
"""One actual bare-Git replay of the observed concurrent summary conflict.

All files and runs are synthetic interface inputs. No scientific value,
accepted step, external credential, public ref or remote repository is used.
The complete transcript and receipt are scratch-only reproducible outputs.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import time


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def load(path):
    spec=importlib.util.spec_from_file_location('actual_ledger_git_fixture_module',path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=module
    spec.loader.exec_module(module)
    return module


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--publisher',type=Path,required=True)
    parser.add_argument('--prefix',type=Path,required=True)
    args=parser.parse_args()
    started=time.monotonic()
    prefix=args.prefix.resolve()
    work=Path(str(prefix)+'-work')
    if work.exists():raise FileExistsError('A fresh scratch fixture directory is required')
    work.mkdir(parents=True)
    env={k:v for k,v in os.environ.items() if k not in (
        'GH_TOKEN','GITHUB_TOKEN','MR_TOKEN','VISIBLE_FLEX_TOKEN','M12_RECOVERY_TOKEN',
        'CART_COLD_TOKEN','CART_CONTINUATION_TOKEN') and not k.startswith('GIT_CONFIG_')}
    env.update(GIT_CONFIG_NOSYSTEM='1',GIT_CONFIG_GLOBAL='/dev/null',GIT_TERMINAL_PROMPT='0')
    transcript=[]

    def run(cwd,*command,check=True):
        result=subprocess.run(command,cwd=cwd,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        transcript.append(dict(cwd=str(cwd),command=list(command),OSExitCode=result.returncode,stdout=result.stdout))
        if check and result.returncode:raise RuntimeError(result.stdout)
        return result

    remote=work/'remote.git';seed=work/'seed';runner=work/'runner';upstream=work/'upstream'
    run(work,'git','init','--bare','--initial-branch=main',str(remote))
    run(work,'git','clone',str(remote),str(seed))
    for key,value in [('user.name','Synthetic Fixture'),('user.email','synthetic@example.invalid')]:
        run(seed,'git','config','--local',key,value)
    topic=Path('topics/visible-flexible-closed-surface');notes=topic/'notes';handoff=topic/'HANDOFF.md'
    (seed/notes).mkdir(parents=True)
    (seed/'README.md').write_text('# Synthetic root rules\nOnly a local Git interface fixture.\n')
    (seed/topic/'README.md').write_text('# Synthetic topic rules\nNo mathematical acceptance is tested.\n')
    foreign_h='Foreign writer prose: retain exactly.\n<!-- foreign-ci-marker --> unrelated task receipt.\n'
    (seed/handoff).write_text('# HANDOFF\n\n'+foreign_h)
    run(seed,'git','add','README.md',str(topic))
    run(seed,'git','commit','-m','synthetic initial repository')
    run(seed,'git','push','origin','HEAD:main')
    for path in (runner,upstream):
        run(work,'git','clone',str(remote),str(path))
        for key,value in [('user.name','Synthetic Fixture'),('user.email','synthetic@example.invalid')]:
            run(path,'git','config','--local',key,value)

    module=load(args.publisher.resolve())
    marker='<!-- 6a65-polar-publisher-fixture -->'
    report_rel=notes/'synthetic-owned-summary-12345-1.md'
    owner_commands=[]

    class Owner:
        def __init__(self):
            self.repo=runner;self.out=work/'scratch';self.out.mkdir()
            self.report=runner/report_rel;self.run_id='12345';self.attempt='1'
            self.record=dict(state='synthetic-initial',stage='own-zero',actualAcceptedSteps=0,
                             fixtureOnly=True,pulls=[])
            self.last_rules=run(runner,'git','rev-parse','HEAD').stdout.strip()
            self.total_pull_count=0;self.last_sync=time.monotonic();self.push_hook=None
        def git(self,*command,capture=False,check=True):
            if command[0]=='push' and self.push_hook:
                hook=self.push_hook;self.push_hook=None;hook()
            result=run(self.repo,'git',*command,check=False)
            owner_commands.append(dict(command=list(command),OSExitCode=result.returncode,stdout=result.stdout))
            if result.stdout and not capture:print(result.stdout,end='',flush=True)
            if check and result.returncode:raise RuntimeError(result.stdout)
            if capture and check:return result.stdout
            return result
        def save(self,status):
            self.record['state']=status
            (self.out/'actual-ledger.json').write_text(json.dumps(self.record,indent=2)+'\n')
            self.report.parent.mkdir(parents=True,exist_ok=True)
            self.report.write_text('# Synthetic owned conclusion\n\nStage: '+self.record['stage']+
                '\nAccepted scientific steps: 0 (interface fixture only).\n'+
                'Latest actual synthetic receipt: '+self.record.get('actualReceipt','none')+'\n')

    owner=Owner();owner.save('synthetic-initial')
    initial_commit=module.ActualLedgerMarkdownPublisher(owner,marker=marker).publish('initial local interface fixture')
    human_outside='Human note outside the owned block: this exact prose must survive.\n'
    erratum=notes/'synthetic-independent-erratum.md'
    erratum_text='# Independent synthetic erratum\nKeep upstream evidence verbatim.\n'
    foreign_new=foreign_h+'Foreign writer second paragraph: preserved concurrently.\n'
    concurrent_commit=None

    def concurrent_edit():
        nonlocal concurrent_commit
        run(upstream,'git','pull','--ff-only','origin','main')
        path=upstream/report_rel
        before=path.read_text()
        if before.count('Stage: own-zero\n')!=1:raise AssertionError('Synthetic conflict base changed')
        path.write_text(before.replace('Stage: own-zero\n',
            'Stage: own-zero (upstream scope correction of the original model)\n')+'\n'+human_outside)
        (upstream/erratum).write_text(erratum_text)
        h=upstream/handoff
        if foreign_h not in h.read_text():raise AssertionError('Foreign HANDOFF base absent')
        h.write_text(h.read_text().replace(foreign_h,foreign_new))
        run(upstream,'git','add',str(report_rel),str(erratum),str(handoff))
        run(upstream,'git','commit','-m','upstream edits active generated summary plus independent prose')
        concurrent_commit=run(upstream,'git','rev-parse','HEAD').stdout.strip()
        run(upstream,'git','push','origin','HEAD:main')

    owner.record.update(stage='prepare',state='synthetic-prepare-complete',actualReceipt='cache completed; acceptance zero')
    owner.save(owner.record['state']);owner.push_hook=concurrent_edit
    publisher=module.ActualLedgerMarkdownPublisher(owner,marker=marker)
    final_commit=publisher.publish('regenerate current ledger after real conflicting push')
    final_text=owner.report.read_text();final_h=(runner/handoff).read_text()
    assert 'Stage: prepare\n' in final_text
    assert 'Latest actual synthetic receipt: cache completed; acceptance zero\n' in final_text
    assert final_text.endswith('\n'+human_outside)
    assert (runner/erratum).read_text()==erratum_text
    assert foreign_new in final_h
    assert len([line for line in final_h.splitlines() if line.startswith(marker)])==1
    for receipt in publisher.pulls:assert receipt['toCommit'] in final_h
    assert not publisher.operation_in_progress()
    assert not publisher.changed_paths()
    assert run(runner,'git','rev-parse','origin/main').stdout.strip()==final_commit
    assert run(runner,'git','merge-base','--is-ancestor',concurrent_commit,final_commit,check=False).returncode==0
    assert len(owner.record.get('withdrawnUnpublishedSummaries',[]))==1
    failed_pushes=[i for i,r in enumerate(owner_commands) if r['command'][0]=='push' and r['OSExitCode']]
    assert len(failed_pushes)==1
    assert owner_commands[failed_pushes[0]+1]['command']==['pull','--rebase','origin','main']
    conflicts=[r for r in owner_commands if r['command']==['pull','--rebase','origin','main'] and r['OSExitCode']]
    assert len(conflicts)==1 and 'CONFLICT (content)' in conflicts[0]['stdout']
    assert all('--force' not in r['command'] and '-f' not in r['command'] for r in owner_commands)
    assert not any(publisher.operation_in_progress() for unused in range(1))

    # The one unsafe case is directly relevant to withdrawing a pending commit:
    # an unrelated unpublished commit must never be reset by this helper.
    protected=runner/'unrelated-local-work.txt';protected.write_text('Do not discard this local user work.\n')
    run(runner,'git','add',protected.name)
    run(runner,'git','commit','-m','unrelated unpublished user work')
    protected_head=run(runner,'git','rev-parse','HEAD').stdout.strip();protected_sha=sha(protected)
    owner.save('synthetic-second-publication-with-unrelated-commit')
    rejected=None
    try:module.ActualLedgerMarkdownPublisher(owner,marker=marker).publish('must reject unrelated pending commit')
    except module.UnsafePublication as error:rejected=str(error)
    assert rejected and 'unpublished commit' in rejected
    assert run(runner,'git','rev-parse','HEAD').stdout.strip()==protected_head
    assert sha(protected)==protected_sha

    log_path=Path(str(prefix)+'-transcript.json')
    log_path.write_text(json.dumps(transcript,indent=2)+'\n')
    receipt=dict(schema='6a65-actual-ledger-conflicting-Markdown-local-bare-Git-fixture-v1',
        scriptSHA256=sha(__file__),publisherSHA256=sha(args.publisher),
        syntheticInterfaceOnly=True,mathematicalEvaluationExecuted=False,acceptedScientificSteps=0,
        publicRepositoryTouched=False,externalCredentialsRead=False,
        actualGitVersion=run(work,'git','--version').stdout.strip(),
        actualInitialPublishedCommit=initial_commit,actualConcurrentUpstreamCommit=concurrent_commit,
        actualFinalPublishedCommit=final_commit,actualFailedPushCount=len(failed_pushes),
        actualRebaseContentConflictCount=len(conflicts),
        immediateLiteralPullAfterRejectedPush=True,
        ownSoleUnpublishedSummaryWithdrawn=True,completeCurrentLedgerRegenerated=True,
        upstreamOutsideOwnedBlockPreservedExactly=True,independentErratumPreservedExactly=True,
        foreignHandoffProsePreservedExactly=True,everyActualConflictPullSHARecordedInHandoff=True,
        noExistingRebaseLeft=True,noForcedPushOrRemoteHistoryRewrite=True,
        unrelatedUnpublishedWorkRejectedWithoutHeadOrFileChange=True,
        unsafePendingGuardMessage=rejected,
        actualTotalPullCount=owner.total_pull_count,conflictPublicationPulls=publisher.pulls,
        withdrawnUnpublishedSummaries=owner.record['withdrawnUnpublishedSummaries'],
        finalPublishedSummarySHA256=hashlib.sha256(final_text.encode()).hexdigest(),
        finalPublishedHandoffSHA256=hashlib.sha256(final_h.encode()).hexdigest(),
        transcriptSHA256=sha(log_path),seconds=time.monotonic()-started)
    receipt_path=Path(str(prefix)+'-receipt.json')
    receipt_path.write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(dict(actualFixtureComplete=True,receipt=str(receipt_path),
        receiptSHA256=sha(receipt_path),transcriptSHA256=sha(log_path),seconds=receipt['seconds'])),flush=True)


if __name__=='__main__':main()
