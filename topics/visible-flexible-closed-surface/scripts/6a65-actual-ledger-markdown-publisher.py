#!/usr/bin/env python3
"""Publish one owned Markdown summary from the actual scratch ledger.

The owner supplies git(), save(status), repo/report/out, run_id/attempt,
record, last_rules, total_pull_count and last_sync. save() must render only
its actual small summary and keep complete reports outside Git. It must not
mutate HANDOFF or other tracked files. This helper never reads credentials.

A failed concurrent push is followed immediately by literal pull --rebase.
Only this call's verified sole unpublished summary/H-marker commit may be
withdrawn. The complete current ledger then regenerates the summary on the
new upstream tree. Upstream text outside the marked owned block, separate
errata, other files and non-owned HANDOFF prose are retained exactly.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import re
import time
from datetime import datetime,timezone

TOPIC=Path('topics/visible-flexible-closed-surface')
HANDOFF=TOPIC/'HANDOFF.md'
RULES=(Path('README.md'),TOPIC/'README.md')

class RulesChanged(RuntimeError):pass
class UnsafePublication(RuntimeError):pass

def utc():return datetime.now(timezone.utc).isoformat()
def digest(text):return hashlib.sha256(text.encode()).hexdigest()
def concurrent_ref(text):
    s=text.lower()
    return ('non-fast-forward' in s or '(fetch first)' in s or
        ('cannot lock ref' in s and 'is at' in s and 'expected' in s) or
        ('remote rejected' in s and 'incorrect old value provided' in s) or
        ('remote rejected' in s and 'failed to update ref' in s and 'expected' in s) or
        ('remote rejected' in s and 'reference update conflict' in s))

class ActualLedgerMarkdownPublisher:
    def __init__(self,owner,*,marker,rules_changed_error=RulesChanged):
        self.owner=owner
        self.repo=Path(owner.repo).resolve()
        self.report=Path(owner.report).resolve()
        try:self.relative=self.report.relative_to(self.repo)
        except ValueError:raise UnsafePublication('Summary is outside the publication worktree')
        if self.relative.parent!=TOPIC/'notes' or self.relative.suffix!='.md':
            raise UnsafePublication('Only one topic Markdown conclusion may be published')
        if not re.fullmatch(r'<!-- [A-Za-z0-9_-]+ -->',marker):
            raise UnsafePublication('An explicit independent HANDOFF marker is required')
        if not str(owner.run_id).isdigit() or not str(owner.attempt).isdigit():
            raise UnsafePublication('Actual run and attempt identifiers required')
        self.marker=marker
        self.begin=f'<!-- 6a65-owned-summary {owner.run_id}/{owner.attempt} begin -->'
        self.end=f'<!-- 6a65-owned-summary {owner.run_id}/{owner.attempt} end -->'
        self.changed_error=rules_changed_error
        self.pending=None
        self.pulls=[]
        self.changed=False

    def git(self,*args,capture=True,check=True):
        return self.owner.git(*args,capture=capture,check=check)

    def head(self):return self.git('rev-parse','HEAD').strip()
    def remote(self):return self.git('rev-parse','origin/main').strip()

    def operation_in_progress(self):
        for key in ('rebase-merge','rebase-apply','MERGE_HEAD','CHERRY_PICK_HEAD','REVERT_HEAD'):
            path=Path(self.git('rev-parse','--git-path',key).strip())
            if not path.is_absolute():path=self.repo/path
            if path.exists():return True
        return False

    def changed_paths(self):
        paths=set()
        for args in (('diff','--name-only','--no-renames','-z'),
                     ('diff','--cached','--name-only','--no-renames','-z')):
            paths.update(x for x in self.git(*args).split('\0') if x)
        return paths

    def show(self,revision,path):
        r=self.git('show',f'{revision}:{path.as_posix()}',check=False)
        return r.stdout if r.returncode==0 else None

    def split_owned(self,text):
        if text is None:return '',''
        starts=[m for m in re.finditer(r'(?m)^'+re.escape(self.begin)+r'\n',text)]
        ends=[m for m in re.finditer(r'(?m)^'+re.escape(self.end)+r'(?:\n|$)',text)]
        if len(starts)!=1 or len(ends)!=1 or starts[0].end()>ends[0].start():
            raise UnsafePublication('Existing summary has no unique block owned by this exact run')
        before,after=text[:starts[0].start()],text[ends[0].end():]
        if '<!-- 6a65-owned-summary ' in before+after:
            raise UnsafePublication('Foreign or duplicate summary ownership markers')
        return before,after

    def render_owned(self,upstream):
        prefix,suffix=self.split_owned(upstream)
        self.owner.save(self.owner.record['state'])
        body=self.report.read_text()
        if self.begin in body or self.end in body or not body.strip():
            raise UnsafePublication('Owner.save must produce the fresh unwrapped actual summary')
        if body.lstrip().startswith(('{','[')):
            raise UnsafePublication('Complete JSON output cannot be published as Markdown')
        text=prefix+self.begin+'\n'+body.rstrip('\n')+'\n'+self.end+'\n'+suffix
        if len(text.encode())>=100000:
            raise UnsafePublication('The actual conclusion summary exceeds 100 KB')
        self.report.write_text(text)
        return text

    def clean_generated_summary_before_pull(self):
        # Only the freshly rendered owned report may be dirty at entry.
        if self.operation_in_progress():
            raise UnsafePublication('Refusing to publish inside an existing Git operation')
        if self.changed_paths()-{str(self.relative)}:
            raise UnsafePublication('Unrelated tracked work exists before publication')
        if self.git('rev-list','origin/main..HEAD').strip():
            raise UnsafePublication('Unrelated or previously pending unpublished commit exists')
        current=self.show('HEAD',self.relative)
        if current is not None:
            self.split_owned(current)
            self.git('restore','--source=HEAD','--staged','--worktree','--',str(self.relative))
        else:
            self.git('reset','--',str(self.relative),check=False)
            if self.report.exists():self.report.unlink()
        if self.changed_paths():raise UnsafePublication('Tracked work was not clean after restoring only the owned report')

    def verify_unique_pending(self,commit,parent,subject,*,check_head=True):
        if check_head and self.head()!=commit:
            raise UnsafePublication('HEAD changed outside this publication call')
        parents=self.git('rev-list','--parents','-n','1',commit).split()
        if parents!=[commit,parent] or self.git('log','-1','--format=%s',commit).strip()!=subject:
            raise UnsafePublication('Not this call\'s exact single-parent summary commit')
        paths=set(self.git('diff-tree','--no-commit-id','--name-only','--no-renames','-r',commit).splitlines())
        allowed={str(self.relative),str(HANDOFF)}
        if not paths or not paths<=allowed:
            raise UnsafePublication('Pending commit changes an unrelated path')
        if str(HANDOFF) in paths:
            before=self.show(parent,HANDOFF);after=self.show(commit,HANDOFF)
            if before is None or after is None:raise UnsafePublication('HANDOFF cannot be created or removed')
            strip=lambda s:''.join(x for x in s.splitlines(keepends=True) if not x.startswith(self.marker))
            if strip(before)!=strip(after):
                raise UnsafePublication('Pending HANDOFF changes include another writer\'s prose')
        if str(self.relative) in paths:
            self.split_owned(self.show(commit,self.relative))
        if self.git('rev-list',self.remote()+'..'+commit).split()!=[commit]:
            raise UnsafePublication('Pending commit is not uniquely unpublished against the actual fetched main')
        if self.git('merge-base','--is-ancestor',commit,'origin/main',check=False).returncode==0:
            raise UnsafePublication('Refusing to withdraw any already-upstream commit')

    def withdraw(self,commit,parent,subject,why):
        self.verify_unique_pending(commit,parent,subject)
        if self.changed_paths() or self.operation_in_progress():
            raise UnsafePublication('Unexpected tracked work or Git operation while withdrawing own commit')
        self.git('reset','--hard',parent)
        self.owner.record.setdefault('withdrawnUnpublishedSummaries',[]).append(dict(
            UTC=utc(),commit=commit,parent=parent,actualFetchedMain=self.remote(),reason=why,
            onlyThisRunSummaryAndOwnHMarker=True,remoteHistoryRewritten=False))
        self.pending=None

    def record_pull(self,result,remote):
        difference=self.git('diff',self.owner.last_rules,remote,'--',*(str(p) for p in RULES))
        if difference:
            print('UNREVIEWED_README_DIFF\n'+difference,flush=True)
            self.changed=True
            self.owner.record['state']='unreviewed-readme-difference-numerical-work-stopped'
            self.owner.record['unreviewedReadmeDiffSHA256']=digest(difference)
        receipt=dict(UTC=utc(),fromCommit=self.owner.last_rules,toCommit=remote,
            readmeDiffEmpty=not bool(difference),pullCommandExit=result.returncode)
        self.pulls.append(receipt)
        self.owner.record.setdefault('pulls',[]).append(receipt)
        self.owner.total_pull_count+=1
        self.owner.record['actualTotalPullCount']=self.owner.total_pull_count
        if not difference:self.owner.last_rules=remote
        return receipt

    def pull_to_clean_main(self,subject):
        # The first operation after an identified NFF is this literal pull.
        result=self.git('pull','--rebase','origin','main',check=False)
        remote=self.remote()
        self.record_pull(result,remote)
        if result.returncode:
            conflicts=set(self.git('diff','--name-only','--diff-filter=U').splitlines())
            if not self.pending or not conflicts or not conflicts<={str(self.relative),str(HANDOFF)}:
                raise UnsafePublication('Actual pull failed outside this call\'s owned summary/H conflict')
            commit,parent=self.pending
            if self.git('rev-parse','ORIG_HEAD').strip()!=commit:
                raise UnsafePublication('Rebase origin is not this call\'s pending summary')
            self.verify_unique_pending(commit,parent,subject,check_head=False)
            if self.changed_paths()-{str(self.relative),str(HANDOFF)}:
                raise UnsafePublication('Other tracked work appeared during the rebase conflict')
            self.git('rebase','--abort')
            self.withdraw(commit,parent,subject,'actual concurrent owned-summary or own-H conflict')
            # The next operation is another literal pull, from the old parent;
            # no forced checkout of remote history or skipped README check.
            return False
        if self.pending:
            pending=self.git('rev-list','origin/main..HEAD').split()
            if not pending:
                if self.head()!=remote:raise UnsafePublication('Unexpected HEAD after a successful pull')
                self.pending=None
            elif len(pending)==1:
                commit=pending[0]
                parent=self.git('rev-parse',commit+'^').strip()
                self.withdraw(commit,parent,subject,'rerender complete actual ledger on newly fetched main')
            else:raise UnsafePublication('Pull retained more than one unpublished commit')
        if self.head()!=remote or self.changed_paths():
            raise UnsafePublication('Publication must resume on the clean actual fetched main')
        return True

    def write_handoff(self):
        path=self.repo/HANDOFF
        lines=path.read_text().splitlines(keepends=True)
        positions=[i for i,x in enumerate(lines) if x.startswith(self.marker)]
        if len(positions)>1:
            old=[lines[i] for i in positions]
            if len(set(old))!=1:
                raise UnsafePublication('Different duplicate own HANDOFF receipts require reconciliation')
            for i in reversed(positions[1:]):del lines[i]
            positions=positions[:1]
        last=self.pulls[-1]
        state='双 README 有差异未审，已打印并停数值步骤' if self.changed else '双 README 无差异'
        # Preserve every actual pull SHA from this publication, including the
        # conflict pull whose local commit could not be published separately.
        read_commits=list(dict.fromkeys(p['toCommit'] for p in self.pulls))
        line=(f'{self.marker} run {self.owner.run_id}/{self.owner.attempt}；实际 pull 至 {last["toCommit"]}；'
            f'{last["UTC"]}；{state}；本次各 pull SHA '+','.join(read_commits)+'。\n')
        if positions:lines[positions[0]]=line
        else:lines.insert(1,line)
        text=''.join(lines)
        if len(text.encode())>=10000:raise UnsafePublication('HANDOFF would exceed 10 KB')
        path.write_text(text)

    def publish(self,reason):
        if '\n' in reason or '\r' in reason:raise UnsafePublication('Single-line publication reason required')
        subject=f'visible-flex: actual summary {self.owner.run_id}/{self.owner.attempt} {reason}'
        self.clean_generated_summary_before_pull()
        while True:
            if not self.pull_to_clean_main(subject):continue
            upstream=self.show('HEAD',self.relative)
            self.owner.record['latestUpstreamSummarySHA256']=digest(upstream) if upstream is not None else None
            self.write_handoff()
            if not self.changed:
                self.render_owned(upstream)
                self.git('add','--',str(self.relative),str(HANDOFF))
            else:
                # No new mathematical note is carried across unreviewed rules.
                # Keep the upstream note exactly and publish only its H receipt.
                self.owner.save(self.owner.record['state'])
                if upstream is None:
                    if self.report.exists():self.report.unlink()
                else:self.report.write_text(upstream)
                self.git('add','--',str(HANDOFF))
            allowed={str(HANDOFF)} if self.changed else {str(self.relative),str(HANDOFF)}
            if self.changed_paths()-allowed:
                raise UnsafePublication('Save or publication changed an unrelated tracked path')
            if self.git('diff','--cached','--quiet',check=False).returncode==0:
                self.owner.last_sync=time.monotonic()
                if self.changed:raise self.changed_error('Unreviewed README receipt retained; no new numerical note published')
                return self.head()
            parent=self.head()
            self.git('commit','-m',subject)
            commit=self.head()
            self.pending=(commit,parent)
            self.verify_unique_pending(commit,parent,subject)
            pushed=self.git('push','origin','HEAD:main',check=False)
            if pushed.returncode==0:
                self.pending=None
                self.owner.last_sync=time.monotonic()
                print(json.dumps(dict(event='actual-ledger-markdown-published',commit=commit,
                    run_id=str(self.owner.run_id),run_attempt=str(self.owner.attempt),
                    state=self.owner.record['state'],completeReportsPublished=False)),flush=True)
                if self.changed:raise self.changed_error('Actual pull/H receipt published; root must read the changed rules')
                return commit
            if not concurrent_ref(pushed.stdout):
                raise UnsafePublication('Actual push failed outside identified concurrent-ref cases; pending commit retained')
            print('non-fast-forward-immediate-literal-pull-rebase-retry',flush=True)
