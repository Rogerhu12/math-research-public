#!/usr/bin/env python3
"""Supervise the fixed-g M12 angular warm refinement with live 45 min rules checks.

Only this controller touches the publication worktree. Numerical programs
read a separate frozen copy. A changed README stops the numerical process
group and writes an explicit exit-42 state; publication cannot ignore it.
No raw arrays are copied into Git, and credentials stay in process env.
"""
from __future__ import annotations
import argparse,hashlib,json,os,re,signal,subprocess,sys,time
from pathlib import Path

TOPIC=Path('topics/visible-flexible-closed-surface')
READMES=['README.md',str(TOPIC/'README.md')]
HANDOFF=str(TOPIC/'HANDOFF.md')
MARKER='<!-- 6a65-m12-angular-warm-ci-rules -->'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def concurrent_ref(message):
    return bool(re.search(r"non-fast-forward|fetch first|\[rejected\]|"
        r"cannot lock ref ['\"]refs/heads/main['\"][^\n]*(?:is at [0-9a-f]+ but expected [0-9a-f]+|incorrect old value provided)|"
        r"\[remote rejected\][^\n]*->\s*main\b[^\n]*(?:is at [0-9a-f]+ but expected [0-9a-f]+|incorrect old value provided)",message,re.I))
class RulesChanged(RuntimeError):pass

class RulesMonitor:
    def __init__(self,repository,source_head,run_id,attempt,state_path):
        self.repository=Path(repository);self.last_read=source_head
        self.source_head=source_head;self.run_id=str(run_id);self.attempt=str(attempt)
        self.state_path=Path(state_path);self.events=[];self.changed=False
        self.on_rules_changed=None
        self.env=os.environ.copy()
        self.env.update({'GIT_TERMINAL_PROMPT':'0','GIT_EDITOR':'true',
                         'GIT_CONFIG_COUNT':'2','GIT_CONFIG_KEY_0':'credential.helper',
                         'GIT_CONFIG_VALUE_0':'','GIT_CONFIG_KEY_1':'credential.helper',
                         'GIT_CONFIG_VALUE_1':'!f() { printf "username=x-access-token\\npassword=%s\\n" "$M12_RECOVERY_TOKEN"; }; f'})
        self.subject='Check M12 angular warm frozen-source rules run '+self.run_id+' attempt '+self.attempt
        # Rebase --continue needs persistent identity, not just commit -c.
        self.git('config','user.name','Astra-visible-flex-6a65')
        self.git('config','user.email','41898282+github-actions[bot]@users.noreply.github.com')
    def git(self,*args,check=True):
        result=subprocess.run(['git',*args],cwd=self.repository,env=self.env,
                              text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        if check and result.returncode:
            raise RuntimeError('Git '+args[0]+' failed: '+result.stderr.strip())
        return result
    def save(self):
        self.state_path.write_text(json.dumps({'schema':'6a65-M12-live-rules-checks-v1',
            'frozen_source_head':self.source_head,'last_rules_read_sha':self.last_read,
            'rules_changed':self.changed,'events':self.events},indent=2)+'\n')
    def marker(self):
        path=self.repository/HANDOFF;lines=path.read_text().splitlines(keepends=True)
        matches=[i for i,line in enumerate(lines) if line.startswith(MARKER)]
        if len(matches)>1:raise ValueError('Ambiguous own HANDOFF rules marker')
        state='README changed; root application pending' if self.changed else 'README unchanged'
        line=(MARKER+' '+state+' at '+self.last_read+'; run '+self.run_id+
              ' attempt '+self.attempt+'.\n')
        if matches:lines[matches[0]]=line
        else:
            if lines and not lines[-1].endswith('\n'):lines[-1]+='\n'
            lines.append(line)
        raw=''.join(lines).encode('utf-8')
        if len(raw)>10000:raise ValueError('HANDOFF would exceed 10000 bytes; root must compact its prose')
        path.write_bytes(raw)
    def check_and_publish(self):
        while True:
            # The only literal pull in this controller. Inspect both README
            # diffs immediately after its return, including rebase failures.
            pull=self.git('pull','--rebase','origin','main',check=False)
            current=self.git('rev-parse','origin/main').stdout.strip()
            diff=self.git('diff',self.last_read,current,'--',*READMES).stdout
            event={'previous_read_sha':self.last_read,'fetched_sha':current,
                   'literal_pull_exit':pull.returncode,'readme_changed':bool(diff),
                   'utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())}
            self.events.append(event)
            if diff:
                self.changed=True;event['actual_readme_diff']=diff
                if self.on_rules_changed is not None:self.on_rules_changed()
                print(diff,flush=True)
            self.last_read=current;self.save()
            if pull.returncode:
                conflicts=self.git('diff','--name-only','--diff-filter=U').stdout.splitlines()
                if conflicts!=[HANDOFF]:
                    raise RuntimeError('Pull failed outside this job own HANDOFF marker: '+pull.stderr.strip())
                # During rebase stage 2 is the upstream version. Keep all
                # upstream prose/other markers; this job line is re-added.
                upstream=self.git('show',':2:'+HANDOFF).stdout
                (self.repository/HANDOFF).write_text(upstream);self.git('add','--',HANDOFF)
                staged=self.git('diff','--cached','--quiet',check=False)
                self.git('rebase','--skip' if staged.returncode==0 else '--continue')
            self.marker();self.git('add','--',HANDOFF)
            if self.git('diff','--cached','--quiet',check=False).returncode:
                self.git('-c','user.name=Astra-visible-flex-6a65',
                         '-c','user.email=41898282+github-actions[bot]@users.noreply.github.com',
                         'commit','-m',self.subject)
            push=self.git('push','origin','HEAD:main',check=False)
            event['push_exit']=push.returncode;self.save()
            if push.returncode==0:
                print(json.dumps({'rules_read_and_marker_published':current,'frozen_source':self.source_head}),flush=True)
                if self.changed:
                    raise RulesChanged('README change recorded in HANDOFF; root must apply the actual diff')
                return
            # Ordinary NFF retry; no reset, force-push, or amendment.
            if not concurrent_ref(push.stderr):
                raise RuntimeError('Ordinary rules marker push failed: '+push.stderr.strip())

def terminate(child):
    if child.poll() is not None:return
    os.killpg(child.pid,signal.SIGTERM)
    try:child.wait(timeout=10)
    except subprocess.TimeoutExpired:
        os.killpg(child.pid,signal.SIGKILL);child.wait()

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for key in ('repository','frozen-root','directory'):ap.add_argument('--'+key,type=Path,required=True)
    for key in ('source-head','run-id','attempt'):ap.add_argument('--'+key,required=True)
    for key,value in [('prefix-elements',80),('tail-elements',64),('tail-depth',12),('order',32),
                      ('angular',384),('gauss',6),('iterations',800),('newton',1),('block',24),
                      ('warm-order',48),('warm-angular',768),('warm-iterations',800),('warm-newton',1)]:
        ap.add_argument('--'+key,type=int,default=value)
    ap.add_argument('--interval-seconds',type=int,default=2700)
    ap.add_argument('--expected-base-field-sha256')
    args=ap.parse_args()
    if not 60<=args.interval_seconds<=2700:raise ValueError('Rule checks must be at most 45 minutes apart')
    if args.frozen_root.resolve()==args.repository.resolve():raise ValueError('Numerical source must be frozen outside publication worktree')
    scripts=args.frozen_root/TOPIC/'scripts';data=args.directory/'m12-prefix-data.npz.gz'
    task=args.directory/'entire-half';task.mkdir(parents=True,exist_ok=True)
    freeze=json.loads((args.directory/'frozen-source.json').read_text())
    if freeze['source_head']!=args.source_head:raise ValueError('Frozen source head mismatch')
    for name in READMES:
        if freeze['readme_sha256'][name]!=sha(args.frozen_root/name):raise ValueError('Frozen README identity mismatch')
    monitor=RulesMonitor(args.repository,args.source_head,args.run_id,args.attempt,args.directory/'live-rules-checks.json')
    base=[sys.executable,str(scripts/'6a65-m12-h487-to-m48-angular-warm-cold-run.py'),
          '--data',str(data),'--directory',str(task),'--local-element','190','--second-local-element','176',
          '--source-knot-window','.432','.5141','--diagnostic-window','.432','.436',
          '--diagnostic-window','.5122','.5141']
    for key in ('prefix_elements','tail_elements','tail_depth','order','angular','gauss','iterations','newton','block',
                'warm_order','warm_angular','warm_iterations','warm_newton'):
        base+=['--'+key.replace('_','-'),str(getattr(args,key))]
    if args.expected_base_field_sha256:base+=['--expected-base-field-sha256',args.expected_base_field_sha256]
    common=['--scripts',str(scripts),'--data',str(data),'--grid',str(task/'entire-half-grid.json'),
            '--field',str(task/'entire-half-result.json.field.npz'),'--result',str(task/'entire-half-result.json')]
    commands=[
        ('fixed-g-h487-to-M48-warm-numerical-run',base),
        ('same-field-three-phase-STL',[sys.executable,str(scripts/'6a65-m12-entire-half-closed-stl.py'),*common,
          '--query-report',str(task/'entire-half-exact-tail-queries.json'),
          '--query-cache',str(task/'entire-half-exact-tail-queries.json.npz'),
          '--geometry-report',str(task/'entire-half-actual-field-geometry.json'),
          '--angular','216','--prefix-intervals','64','--tail-intervals','32','--out',str(task/'entire-half-closed-stl.json')]),
        ('same-field-R236-localized-continuous-metric',[sys.executable,str(scripts/'6a65-m12-local-bernstein-angular-metric-budget.py'),
          *common,'--correction-bounds',str(task/'entire-half-continuous-change-bounds.json'),
          '--out',str(task/'entire-half-localized-metric-budget.json')])]
    record={'schema':'6a65-M12-angular-warm-frozen-source-supervised-execution-v1','script_sha256':sha(__file__),
            'frozen_source_head':args.source_head,'frozen_source_receipt_sha256':sha(args.directory/'frozen-source.json'),
            'source_hashes':{Path(c[1]).name:sha(c[1]) for name,c in commands},
            'rule_check_interval_seconds':args.interval_seconds,'stages':[],
            'finished':False,'rules_changed':False}
    receipt=args.directory/'supervised-execution.json'
    def save():receipt.write_text(json.dumps(record,indent=2)+'\n')
    start=time.monotonic();child=None;save()
    monitor.on_rules_changed=lambda:terminate(child) if child is not None else None
    try:
        monitor.check_and_publish();next_check=time.monotonic()+args.interval_seconds
        for name,command in commands:
            began=time.monotonic();print(json.dumps({'supervised_stage':name,'starting':True}),flush=True)
            env={k:v for k,v in os.environ.items() if k not in ('GITHUB_TOKEN','GH_TOKEN')}
            if name!='fixed-g-h487-to-M48-warm-numerical-run':env.pop('M12_RECOVERY_TOKEN',None)
            child=subprocess.Popen(command,env=env,start_new_session=True)
            while child.poll() is None:
                if time.monotonic()>=next_check:
                    monitor.check_and_publish();next_check=time.monotonic()+args.interval_seconds
                time.sleep(1)
            record['stages'].append({'stage':name,'exit_code':child.returncode,'seconds':time.monotonic()-began})
            record['seconds']=time.monotonic()-start;save()
            if child.returncode:raise SystemExit(child.returncode)
        record['finished']=True;record['seconds']=time.monotonic()-start;save()
    except RulesChanged as error:
        if child is not None:terminate(child)
        record['rules_changed']=True;record['failure']=str(error);record['exit_code']=42
        record['seconds']=time.monotonic()-start;save();raise SystemExit(42)
    finally:
        if child is not None and child.poll() is None:terminate(child)
    print(json.dumps(record,indent=2),flush=True)
if __name__=='__main__':main()
