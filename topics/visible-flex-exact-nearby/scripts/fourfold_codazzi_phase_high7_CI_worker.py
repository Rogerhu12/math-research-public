#!/usr/bin/env python3
"""Run one actual scalar-cache range and publish normal/failed checkpoints.

Only this public repository is used. No candidate replay or private data
is required. Numerical files stay outside the checkout while git pulls.
Every publication performs real pull--rebase and checks both READMEs;
non-fast-forward pushes immediately rebase and retry, without force.
"""
from __future__ import annotations
import argparse,datetime,gzip,hashlib,importlib.metadata,json,os,signal,subprocess,sys,time
from pathlib import Path
from fourfold_native_lossless_parts import pack,restore

TOPIC=Path(__file__).resolve().parents[1]
REPO=TOPIC.parents[1]
RULES=('README.md','topics/visible-flex-exact-nearby/README.md')


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()


def save(path,doc):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(doc,indent=2,allow_nan=False)+'\n').encode()
    if path.suffix=='.gz':raw=gzip.compress(raw,mtime=0)
    temporary=path.with_suffix(path.suffix+'.tmp');temporary.write_bytes(raw);temporary.replace(path)


class Worker:
    def __init__(self,args):
        self.args=args;self.started=time.monotonic();self.child=None;self.interrupted=False
        self.artifact=args.artifact_dir.resolve();self.artifact.mkdir(parents=True,exist_ok=True)
        self.cache=self.artifact/'native';self.cache.mkdir(exist_ok=True)
        self.log=self.artifact/'producer.stdout.log';self.statusfile=self.artifact/'process.json'
        self.run_label=os.environ.get('GITHUB_RUN_ID','local')+'-'+os.environ.get('GITHUB_RUN_ATTEMPT','1')
        self.name=f'run-{self.run_label}-germs{args.germ_start:04d}-{args.germ_stop:04d}'
        self.dest=TOPIC/'notes'/'phase_scalar_high7_ci'/self.name
        self.state=dict(kind='actual_high7_scalar_cache_CI_process',complete=False,
            repository='Rogerhu12/math-research-public',run_id=os.environ.get('GITHUB_RUN_ID'),
            run_attempt=os.environ.get('GITHUB_RUN_ATTEMPT'),workflow_commit=os.environ.get('GITHUB_SHA'),
            worker_source_sha256=sha(__file__),requested_germs=[args.germ_start,args.germ_stop],
            child_exit_code=None,started_utc=now(),readme_checks=[],published_checkpoints=[],
            first_germ_reused_not_recomputed=True,invalid_cap6_outputs_used=False)
        self.env=dict(os.environ,GIT_TERMINAL_PROMPT='0')
        helper='!f() { printf "%s\\n" "username=x-access-token" "password=$GITHUB_TOKEN"; }; f'
        self.gitbase=['git','-c','safe.directory='+str(REPO),'-c','gc.auto=0',
            '-c','maintenance.auto=false','-c','credential.helper=','-c','credential.helper='+helper]
        self.read_commit=None

    def git(self,args,check=True):
        p=subprocess.run(self.gitbase+args,cwd=REPO,env=self.env,text=True,
            stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=180)
        if check and p.returncode:
            print(p.stdout,flush=True);raise RuntimeError('actual git '+args[0]+' failed')
        return p

    def check_inputs(self):
        if sha(self.args.manifest)!=self.args.manifest_sha:
            raise ValueError('the pinned source/input manifest changed')
        self.manifest=json.loads(self.args.manifest.read_text())
        if os.environ.get('GITHUB_REPOSITORY')!=self.manifest['repository']:
            raise ValueError('this computation is authorized only in the migrated public repository')
        if [self.args.germ_start,self.args.germ_stop] not in self.manifest['worker_ranges']:
            raise ValueError('this worker is not one of the four disjoint nonzero-germ ranges')
        for path,expected in self.manifest['files'].items():
            if sha(REPO/path)!=expected:raise ValueError('pinned scientific source/input changed: '+path)
        for path,expected in self.manifest['readme_sha256'].items():
            if sha(REPO/path)!=expected:raise ValueError('current README differs from the reviewed input rules: '+path)
        actual={name:importlib.metadata.version(name) for name in self.manifest['packages']}
        if actual!=self.manifest['packages']:raise ValueError('the pinned numerical package versions changed')
        if '.'.join(map(str,sys.version_info[:3]))!=self.manifest['python_version']:
            raise ValueError('the pinned Python version changed')
        first=json.loads(gzip.decompress((REPO/self.manifest['first_germ_path']).read_bytes()))
        if not first['complete'] or first['germ_index']!=0 or first['configuration']['jet_order']!=7:
            raise ValueError('the corrected complete first germ is not present')
        self.state.update(input_manifest_sha256=self.args.manifest_sha,package_versions=actual,
            python_version=sys.version,first_germ_sha256=sha(REPO/self.manifest['first_germ_path']),
            scientific_input_count=len(self.manifest['files']),all_pinned_inputs_verified=True)
        self.expected_configuration=first['configuration']

    def seed_published_prefix(self):
        root=TOPIC/'notes'/'phase_scalar_high7_ci';selected=[]
        if not root.exists():return
        packed={}
        for status in root.glob('*/process.json'):
            document=json.loads(status.read_text())
            for item in document.get('native_files',[]):
                logical=item.get('logical_file');manifest_name=item.get('lossless_manifest')
                if not logical or not manifest_name:continue
                if Path(logical).name!=logical or Path(manifest_name).name!=manifest_name:
                    raise ValueError('a published lossless checkpoint uses a nonlocal filename')
                packed.setdefault(logical,[]).append((status.parent/manifest_name,item['sha256']))
        for index in range(self.args.germ_start,self.args.germ_stop):
            choices=[]
            for logical in (f'germ{index:04d}.json.gz',f'germ{index:04d}.partial.json.gz'):
                paths=[(p,str(p.relative_to(REPO))) for p in root.glob('*/'+logical)]
                for manifest,digest in packed.get(logical,[]):
                    recovered=self.artifact/'restored-prefix'/(digest+'-'+logical)
                    recovered.parent.mkdir(parents=True,exist_ok=True)
                    restore(manifest,recovered)
                    if sha(recovered)!=digest:raise ValueError('restored published checkpoint identity changed')
                    paths.append((recovered,str(manifest.relative_to(REPO))))
                for path,origin in paths:
                    doc=json.loads(gzip.decompress(path.read_bytes()))
                    if doc.get('configuration')!=self.expected_configuration or doc.get('germ_index')!=index:continue
                    complete=bool(doc.get('complete'))
                    if complete and (len(doc.get('gates',[]))!=6 or not all(g.get('passed') for g in doc['gates'])):continue
                    choices.append((complete,len(doc.get('rows',[])),path,logical,origin))
            if not choices:continue
            complete,count,path,logical,origin=max(choices,key=lambda z:(z[0],z[1],z[4]))
            target=self.cache/logical
            if target.exists():continue
            target.write_bytes(path.read_bytes())
            selected.append(dict(germ_index=index,source=origin,sha256=sha(path),
                complete=complete,accepted_rows=count))
        self.state['reused_exact_published_checkpoints']=selected

    def sync(self):
        if self.read_commit is None:self.read_commit=self.git(['rev-parse','HEAD']).stdout.strip()
        self.git(['pull','--rebase','--no-tags','origin','main'])
        current=self.git(['rev-parse','origin/main']).stdout.strip()
        difference=self.git(['diff',self.read_commit,current,'--',*RULES]).stdout
        self.state['readme_checks'].append(dict(time=now(),before=self.read_commit,after=current,changed=bool(difference)))
        if difference:
            (self.artifact/'README-difference.txt').write_text(difference)
            self.state['readme_difference_requires_researcher_consumption']=True
            print('ACTUAL_README_CHANGE\n'+difference,flush=True)
            raise RuntimeError('new repository rules detected; preserve native prefix for the active researcher')
        self.read_commit=current;self.state['last_read_commit']=current
        self.check_inputs()

    def snapshot(self):
        self.dest.mkdir(parents=True,exist_ok=True);entries=[]
        for path in sorted(self.cache.glob('*.gz')):
            try:raw=path.read_bytes()
            except FileNotFoundError:
                # The producer atomically publishes the completed germ and
                # then removes its partial. A vanished partial is normal.
                continue
            digest=hashlib.sha256(raw).hexdigest()
            if len(raw)<=5_000_000:
                target=self.dest/path.name;target.write_bytes(raw)
                entries.append(dict(logical_file=path.name,file=path.name,bytes=len(raw),sha256=digest))
            else:
                # Preserve the original complete gzip container byte for byte.
                # Parts are binary gzip, never base64 or JSON-encoded binary.
                exact=self.artifact/(digest+'-'+path.name);exact.write_bytes(raw)
                manifest=self.dest/(path.stem+'-'+digest[:16]+'-parts.json')
                doc=pack(exact,manifest,2_000_000)
                entries.append(dict(logical_file=path.name,lossless_manifest=manifest.name,
                    bytes=len(raw),sha256=digest,parts=len(doc['parts'])))
        if self.log.exists():
            compressed=gzip.compress(self.log.read_bytes(),mtime=0)
            if len(compressed)>5_000_000:
                # The full raw log remains in the always-uploaded artifact.
                self.state['stdout_commit_omitted_due_file_limit']=dict(bytes=len(compressed),
                    raw_sha256=sha(self.log),full_log_in_artifact=True)
            else:(self.dest/'producer.stdout.log.gz').write_bytes(compressed)
        self.state.update(snapshot_utc=now(),wall_seconds=time.monotonic()-self.started,
            native_files=entries,observed_complete_germs=sum(e['logical_file'].startswith('germ') and '.partial.' not in e['logical_file'] for e in entries))
        save(self.statusfile,self.state);save(self.dest/'process.json',self.state)
        save(self.dest/'pinned-inputs.json',self.manifest)
        for p in self.dest.iterdir():
            if not p.is_file():continue
            if p.stat().st_size>5_000_000:raise ValueError('a publication file exceeds 5MB')
            if p.stat().st_size>1_000_000 and p.suffix!='.gz':raise ValueError('a publication file above1MB is not compressed')

    def publish(self,final=False):
        self.sync();self.snapshot()
        relative=str(self.dest.relative_to(REPO))
        self.git(['add','--sparse','--',relative])
        if self.git(['diff','--cached','--quiet'],check=False).returncode==0:return
        label='finished' if final else 'checkpoint'
        self.git(['commit','-m',f'visible-exact: {label} actual high7 scalar germs {self.args.germ_start}-{self.args.germ_stop}'])
        while True:
            p=self.git(['push','--no-thin','origin','HEAD:refs/heads/main'],check=False)
            print(p.stdout,flush=True)
            if p.returncode==0:
                commit=self.git(['rev-parse','HEAD']).stdout.strip()
                self.state['published_checkpoints'].append(dict(time=now(),commit=commit,final=final))
                save(self.statusfile,self.state);print('ACTUAL_CHECKPOINT_PUBLISHED '+commit,flush=True);return
            if not any(s in p.stdout for s in ('fetch first','non-fast-forward','failed to update ref','remote rejected','rejected')):
                raise RuntimeError('actual push failed for a reason other than concurrent main updates')
            self.sync()
            # Record the newly read rules in the same owned process report.
            save(self.dest/'process.json',self.state)
            self.git(['add','--sparse','--',str((self.dest/'process.json').relative_to(REPO))])
            self.git(['commit','--amend','--no-edit'])

    def terminate_child(self,reason):
        if self.child is None or self.child.poll() is not None:return
        self.state['termination_reason']=reason
        os.killpg(self.child.pid,signal.SIGTERM)
        try:self.child.wait(timeout=20)
        except subprocess.TimeoutExpired:
            os.killpg(self.child.pid,signal.SIGKILL);self.child.wait(timeout=20)

    def run(self):
        self.check_inputs()
        if not os.environ.get('GITHUB_TOKEN'):raise RuntimeError('terminal Git publication token unavailable')
        self.git(['config','user.name','github-actions[bot]'])
        self.git(['config','user.email','41898282+github-actions[bot]@users.noreply.github.com'])
        self.sync()
        self.seed_published_prefix()
        command=[sys.executable,'-u',str(TOPIC/'scripts/fourfold_codazzi_phase_Arb_high_Taylor_cache.py'),
            '--germ-start',str(self.args.germ_start),'--germ-stop',str(self.args.germ_stop),
            '--resume','--out-dir',str(self.cache)]
        self.state['command']=command;save(self.statusfile,self.state)
        with self.log.open('ab') as stream:
            self.child=subprocess.Popen(command,cwd=TOPIC,env=self.env,stdout=stream,stderr=subprocess.STDOUT,start_new_session=True)
            previous=time.monotonic()
            while self.child.poll() is None:
                if self.interrupted:
                    self.terminate_child('runner signal observed');break
                if time.monotonic()-self.started>self.args.compute_minutes*60:
                    self.terminate_child('explicit bounded compute time reached; valid prefix preserved');break
                if time.monotonic()-previous>self.args.checkpoint_minutes*60:
                    self.publish();previous=time.monotonic()
                time.sleep(5)
        self.state['child_exit_code']=self.child.returncode
        path=self.cache/f'manifest-{self.args.germ_start:04d}-{self.args.germ_stop:04d}.json.gz'
        manifest=json.loads(gzip.decompress(path.read_bytes())) if path.exists() else {}
        complete=bool(self.child.returncode==0 and manifest.get('complete_requested_germs')
            and len(manifest.get('reports',[]))==self.args.germ_stop-self.args.germ_start)
        self.state.update(complete=complete,producer_manifest_complete=manifest.get('complete_requested_germs',False),
            completed_utc=now(),all_native_failures_retained=True)
        self.publish(final=True)
        if not complete:raise RuntimeError('the actual worker did not complete its full declared germ range')


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--manifest',type=Path,required=True);ap.add_argument('--manifest-sha',required=True)
    ap.add_argument('--germ-start',type=int,required=True);ap.add_argument('--germ-stop',type=int,required=True)
    ap.add_argument('--artifact-dir',type=Path,required=True)
    ap.add_argument('--compute-minutes',type=int,default=310)
    ap.add_argument('--checkpoint-minutes',type=int,default=10)
    args=ap.parse_args();worker=Worker(args)
    def signal_seen(signum,frame):
        worker.interrupted=True;worker.state['runner_signal']=int(signum)
    signal.signal(signal.SIGTERM,signal_seen);signal.signal(signal.SIGINT,signal_seen)
    try:worker.run()
    except BaseException as exc:
        worker.terminate_child('worker exception: '+type(exc).__name__)
        worker.state.update(complete=False,worker_exception=type(exc).__name__+': '+str(exc),
            child_exit_code=None if worker.child is None else worker.child.poll(),wall_seconds=time.monotonic()-worker.started)
        save(worker.statusfile,worker.state)
        if worker.log.exists():(worker.artifact/'producer.stdout.log.gz').write_bytes(gzip.compress(worker.log.read_bytes(),mtime=0))
        print(json.dumps(worker.state,indent=2),flush=True)
        raise


if __name__=='__main__':main()
