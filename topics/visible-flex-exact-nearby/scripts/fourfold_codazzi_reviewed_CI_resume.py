#!/usr/bin/env python3
"""Resume unchanged scientific jobs after explicitly reading new repository rules.

The original mathematical manifests, producer files and expected array
SHA256s remain unchanged. Reviewed README versions are separate inputs.
Original artifacts are inspected and published before any missing row is
computed. Completed rows are consumed without executing them again.
"""
from __future__ import annotations
import argparse, gzip, hashlib, importlib.metadata, json, os, shutil, signal
import subprocess, sys, time
from fractions import Fraction
from pathlib import Path
from fourfold_codazzi_cap128_CI_worker import CapWorker, digest, read, link_exact
from fourfold_codazzi_body_CI_worker import BodyWorker
from fourfold_codazzi_phase_high7_CI_worker import TOPIC, REPO, save, now
from fourfold_native_lossless_parts import pack

REL=Path('topics/visible-flex-exact-nearby')
RULES=('README.md',str(REL/'README.md'))
REPOSITORY='Rogerhu12/math-research-public'


def checked_json(path,expected):
    if digest(path)!=expected:raise ValueError('a separate reviewed infrastructure input changed: '+str(path))
    return read(path)


def hydrate(args):
    scientific=checked_json(args.manifest,args.manifest_sha)
    checked_json(args.rules,args.rules_sha)
    paths=set(scientific['files'])|set(RULES)|{
        str(args.manifest.relative_to(REPO)),str(args.rules.relative_to(REPO)),
        str(Path(__file__).relative_to(REPO)),str(REL/'scripts/'),
        str(REL/'notes/physical_cap128_ci/'),str(REL/'notes/correlated_body_ci/')}
    if args.recovery_manifest:
        recovery=checked_json(args.recovery_manifest,args.recovery_sha)
        paths.update(recovery['files']);paths.add(str(args.recovery_manifest.relative_to(REPO)))
    subprocess.run(['git','-c','safe.directory='+str(REPO),'sparse-checkout','set','--no-cone','--stdin'],
        cwd=REPO,input='\n'.join('/'+p for p in sorted(paths))+'\n',text=True,check=True)
    print(json.dumps(dict(exact_paths=len(paths),original_scientific_manifest_unchanged=True)))


class ReviewedRules:
    def __init__(self,args):
        super().__init__(args)
        self.reviewed=checked_json(args.rules,args.rules_sha)
        self.recovery=checked_json(args.recovery_manifest,args.recovery_sha) if args.recovery_manifest else None
        self.state.update(infrastructure_resume_source_sha256=digest(__file__),
            reviewed_rules_sha256=args.rules_sha,explicit_readme_review_commit=self.reviewed['read_commit'],
            original_scientific_input_manifest_preserved=True)

    def check_inputs(self):
        if digest(__file__)!=self.args.driver_sha:raise ValueError('the explicit resume driver changed')
        self.manifest=checked_json(self.args.manifest,self.args.manifest_sha)
        self.reviewed=checked_json(self.args.rules,self.args.rules_sha)
        if os.environ.get('GITHUB_REPOSITORY')!=REPOSITORY or self.reviewed['repository']!=REPOSITORY:
            raise ValueError('only this public repository is authorized')
        if self.args.mode=='consume' and [self.args.first,self.args.end] not in self.manifest['consumer_ranges']:
            raise ValueError('an unassigned scientific range was requested')
        for relative,expected in self.manifest['files'].items():
            if digest(REPO/relative)!=expected:raise ValueError('an unchanged scientific source or input differs: '+relative)
        if self.args.recovery_manifest:
            self.recovery=checked_json(self.args.recovery_manifest,self.args.recovery_sha)
            if self.recovery['scientific_manifest_sha256']!=self.args.manifest_sha:
                raise ValueError('the recovery belongs to another scientific manifest')
            for relative,expected in self.recovery['files'].items():
                if digest(REPO/relative)!=expected:raise ValueError('an original recovered input changed: '+relative)
        actual_rules={p:digest(REPO/p) for p in RULES}
        for path,actual in actual_rules.items():
            accepted={self.reviewed['readme_sha256'][path],self.reviewed['previously_read_readme_sha256'][path]}
            if actual not in accepted:
                raise RuntimeError('new unread repository rules need their actual diff read: '+path)
        versions={name:importlib.metadata.version(name) for name in self.manifest['packages']}
        if versions!=self.manifest['packages'] or '.'.join(map(str,sys.version_info[:3]))!=self.manifest['python_version']:
            raise ValueError('the original arithmetic environment changed')
        self.state.update(input_manifest_sha256=self.args.manifest_sha,package_versions=versions,
            all_pinned_inputs_verified=True,actual_reviewed_readme_sha256=actual_rules)

    def sync(self):
        # A previous failure snapshot can have changed this job's own report.
        # Commit those exact owned bytes before pulling; never stash or erase them.
        owned=str(self.dest.relative_to(REPO))
        changed=set(self.git(['diff','--name-only']).stdout.splitlines())
        changed.update(self.git(['diff','--cached','--name-only']).stdout.splitlines())
        if any(p!=owned and not p.startswith(owned+'/') for p in changed):
            raise RuntimeError('unexpected changes outside this job report; preserve them')
        if changed:
            self.git(['add','--sparse','--',owned])
            if self.git(['diff','--cached','--quiet'],check=False).returncode:
                self.git(['commit','-m','visible-exact: preserve actual CI evidence before rebase'])
        before=self.read_commit or self.git(['rev-parse','HEAD']).stdout.strip()
        self.git(['pull','--rebase','origin','main'])
        after=self.git(['rev-parse','HEAD']).stdout.strip()
        difference=self.git(['diff',before,after,'--',*RULES]).stdout
        self.state['readme_checks'].append(dict(time=now(),before=before,after=after,
            changed=bool(difference),actual_diff=difference,
            separately_read_rules_commit=self.reviewed['read_commit']))
        if difference:print('ACTUAL_README_DIFF_CHECKED_AGAINST_EXPLICIT_REVIEW\n'+difference,flush=True)
        self.check_inputs();self.read_commit=after;self.state['last_read_commit']=after

    def science_copy(self):
        super().science_copy()
        if self.recovery:
            for relative,expected in self.recovery['files'].items():
                target=self.science/relative;target.parent.mkdir(parents=True,exist_ok=True)
                if not target.exists():shutil.copyfile(REPO/relative,target)
                if digest(target)!=expected:raise ValueError('the immutable original prefix changed')

    def snapshot(self):
        self.dest.mkdir(parents=True,exist_ok=True);entries=[]
        candidates=list(self.evidence.rglob('*'))+list(self.cache.glob('*.json.gz'))+list(self.artifact.glob('*.json.gz'))
        if (self.artifact/'prepared-manifest.json').exists():candidates.append(self.artifact/'prepared-manifest.json')
        for path in sorted(set(candidates)):
            if not path.is_file():continue
            raw=path.read_bytes();relative=path.relative_to(self.artifact)
            if len(raw)>1_000_000 and path.suffix!='.gz':
                raw=gzip.compress(raw,mtime=0);relative=Path(str(relative)+'.gz')
            if len(raw)>5_000_000:
                exact=self.work/('snapshot-'+hashlib.sha256(raw).hexdigest()+'.json.gz')
                if not exact.exists():exact.write_bytes(raw)
                manifest=self.dest/(str(relative).replace('/','-')+'-'+digest(exact)[:16]+'-parts.json')
                parts=pack(exact,manifest,2_000_000)
                entries.append(dict(logical_file=str(relative),lossless_manifest=manifest.name,
                    bytes=len(raw),sha256=digest(exact),parts=len(parts['parts'])))
            else:
                target=self.dest/relative;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(raw)
                entries.append(dict(logical_file=str(relative),file=str(relative),bytes=len(raw),
                    sha256=hashlib.sha256(raw).hexdigest()))
        if self.log.exists():
            raw=gzip.compress(self.log.read_bytes(),mtime=0)
            if len(raw)<=5_000_000:(self.dest/'producer.stdout.log.gz').write_bytes(raw)
            else:self.state['full_stdout_in_artifact']=digest(self.log)
        self.state.update(snapshot_utc=now(),wall_seconds=time.monotonic()-self.started,native_files=entries)
        save(self.statusfile,self.state);save(self.dest/'process.json',self.state)

    def publish(self,final=False):
        self.sync();self.snapshot();owned=str(self.dest.relative_to(REPO))
        self.git(['add','--sparse','--',owned])
        if self.git(['diff','--cached','--quiet'],check=False).returncode==0:return
        self.git(['commit','-m',f'visible-exact: {"finish" if final else "checkpoint"} actual {self.args.kind} {self.args.mode} {self.args.first}-{self.args.end}'])
        while True:
            result=self.git(['push','--no-thin','origin','HEAD:refs/heads/main'],check=False)
            print(result.stdout,flush=True)
            if result.returncode==0:
                self.state['published_checkpoints'].append(dict(time=now(),final=final,
                    commit=self.git(['rev-parse','HEAD']).stdout.strip()))
                save(self.statusfile,self.state);return
            if not any(s in result.stdout for s in ('fetch first','non-fast-forward','failed to update ref','remote rejected','rejected')):
                raise RuntimeError('actual push failed for another reason')
            self.sync();save(self.dest/'process.json',self.state)
            self.git(['add','--sparse','--',str((self.dest/'process.json').relative_to(REPO))])
            self.git(['commit','--amend','--no-edit'])

    def run_cap(self):
        try:
            self.check_inputs()
            if not os.environ.get('GITHUB_TOKEN'):raise RuntimeError('terminal publication credential unavailable')
            self.git(['config','user.name','github-actions[bot]'])
            self.git(['config','user.email','41898282+github-actions[bot]@users.noreply.github.com'])
            self.sync();self.science_copy()
            self.prepare() if self.args.mode=='prepare' else self.consume()
        except BaseException as error:
            self.terminate_child('actual resume wrapper exception; preserve the original prefix')
            self.state.update(failure=dict(type=type(error).__name__,message=str(error)),finished_utc=now())
            self.snapshot()
            try:self.publish(final=True)
            except Exception as publication_error:
                self.state['publication_failure']=str(publication_error);save(self.statusfile,self.state)
            raise
        self.state['finished_utc']=now();self.publish(final=True)


class ReviewedBodyWorker(ReviewedRules,BodyWorker):
    pass


class ReviewedCapWorker(ReviewedRules,CapWorker):
    def __init__(self,args):
        super().__init__(args)
        if args.mode=='finish-cap':
            self.name=f'run-{self.run_label}-recovered-complete-cap'
            self.dest=TOPIC/'notes/physical_cap128_ci'/self.name
            self.state.update(mode='recover_artifacts_then_complete_original_cap',
                requested_cells=[0,1977],original_failed_run=self.recovery['prior_run_id'])

    def cap_matches(self,document,identity):
        sources={
            'complete_repaired_physical128_cap_moving96_inlet_residual_v3':'9f80d0cb4a54db0e90921e35a8e79e610d2a7ba04f7f2fe46c91093fe436ecf7',
            'complete_repaired_physical128_cap_moving96_inlet_residual_v4':'28cbc02bfe60d91e608728437f2c5dd2906c56aa3a892f5a2fffbaafe72c6046',
            'complete_repaired_physical128_cap_moving96_inlet_residual_packed_v5':'953227cd8871a71ee0c5b9e7ed8a53c3099b1890eadfde3936d9de06067e455a'}
        old=document.get('identity',{})
        return (document.get('kind') in sources and old.get('source_sha256')==sources[document['kind']]
            and {**old,'source_sha256':identity['source_sha256']}==identity)

    def consume(self):
        if self.args.mode!='finish-cap':return super().consume()
        prepared=self.args.prepared.resolve();bundle=read(prepared/'prepared-manifest.json')
        if (bundle.get('kind')!='exact_same_cap128_moving97_CI_bundle' or not bundle.get('complete')
            or bundle['input_manifest_sha256']!=self.args.manifest_sha
            or not bundle.get('every_regenerated_array_matches_historical_bytes')):
            raise ValueError('the original successful complete prepared cap artifact is required')
        for relative,entry in bundle['files'].items():
            path=prepared/relative
            if path.stat().st_size!=entry['bytes'] or digest(path)!=entry['sha256']:
                raise ValueError('an original prepared cap array changed')
        proposal=self.science/self.manifest['precomposed_descriptor'];old=read(proposal)
        if digest(proposal)!=bundle['precomposed_descriptor_sha256'] or old['work_directory']!=bundle['canonical_directory']:
            raise ValueError('the complete historical cap descriptor changed')
        link_exact(old['work_directory'],prepared/bundle['array_directory'])
        for path,expected in old['full_matrix_inputs'].items():
            if digest(path)!=expected:raise ValueError('the original canonical cap array differs')
        cover=read(self.science/self.recovery['original_complete_prefix_cover'])
        identity=cover['common_identity_after_proved_producer_equivalence']
        prefix_parts=[self.science/x['native'] for x in cover['parts']]
        candidates={};recovered=[]
        for folder in sorted(self.args.previous_artifacts.iterdir()):
            if not folder.is_dir():continue
            process=folder/'process.json';native=folder/'native.json.gz'
            if process.exists():
                actual=read(process)
                if (str(actual.get('run_id'))!=str(self.recovery['prior_run_id'])
                    or actual.get('repository')!=REPOSITORY):
                    raise ValueError('an artifact belongs to another original process')
                target=self.evidence/'original-artifacts'/folder.name;target.mkdir(parents=True,exist_ok=True)
                shutil.copyfile(process,target/'process.json')
                if (folder/'producer.stdout.log').exists():
                    (target/'producer.stdout.log.gz').write_bytes(gzip.compress((folder/'producer.stdout.log').read_bytes(),mtime=0))
            if not native.exists():continue
            document=read(native)
            if not self.cap_matches(document,identity) or document.get('failure') is not None:
                raise ValueError('an actual artifact has a different scientific identity or mathematical failure')
            pair=(document['first'],document['end'])
            if list(pair) not in self.recovery['consumer_ranges']:
                raise ValueError('the original cap artifact has an unexpected domain')
            rows=document['rows']
            if [r['index'] for r in rows]!=list(range(pair[0],pair[0]+len(rows))):
                raise ValueError('an original cap artifact lost its consecutive prefix')
            for a,b in zip(rows,rows[1:]):
                if Fraction(a['interval'][1])!=Fraction(b['interval'][0]):
                    raise ValueError('an original cap artifact has a radial gap')
            candidates[pair]=(native,document)
            recovered.append(dict(artifact=folder.name,original_native_sha256=digest(native),
                indices=list(pair),actual_rows=len(rows),selected_cells_complete=document.get('selected_cells_complete',False),
                actual_child_returncodes=[x.get('actual_returncode') for x in read(process).get('children',[])] if process.exists() else None))
        self.state['original_artifact_outcomes']=recovered
        selected=[]
        for first,end in self.recovery['consumer_ranges']:
            result=self.cache/f'cells-{first:04d}-{end:04d}.json.gz'
            chosen=candidates.get((first,end))
            if chosen and chosen[1].get('selected_cells_complete'):
                if len(chosen[1]['rows'])!=end-first:raise ValueError('a complete artifact lacks its entire range')
                shutil.copyfile(chosen[0],result)
                self.state.setdefault('completed_ranges_reused_without_execution',[]).append([first,end])
                self.publish()
            else:
                # Place the verified original prefix in this job's own ordinary
                # checkpoint directory so the unchanged CapWorker selects it.
                if chosen:
                    seed=self.dest/'native.json.gz';seed.parent.mkdir(parents=True,exist_ok=True)
                    shutil.copyfile(chosen[0],seed);self.publish()
                self.args.first,self.args.end=first,end
                super().consume()
                shutil.move(str(self.artifact/'native.json.gz'),str(result))
                self.state['complete']=False
            document=read(result)
            if (not document.get('selected_cells_complete') or document.get('failure')
                or not self.cap_matches(document,identity) or len(document['rows'])!=end-first):
                raise ValueError('a requested original cap range did not complete')
            selected.append(result)
        self.args.first,self.args.end=0,1977
        assembled=self.cache/'complete-cap-native.json.gz'
        prepared=self.args.prepared.resolve();bundle=read(prepared/'prepared-manifest.json')
        command=[sys.executable,'-u',str(self.science_topic/'scripts/fourfold_codazzi_physical_cap_matrix_residual_packed_v5.py'),
            '--candidate',str(prepared/bundle['candidate']),
            '--proposal',str(self.science/self.manifest['precomposed_descriptor']),
            '--first','0','--count','1977','--parts',*[str(x) for x in prefix_parts+selected],'--out',str(assembled)]
        self.execute('assemble_all_original_1977_cap_cells_and_true_boundary',command)
        full=read(assembled)
        if not full.get('complete') or full.get('failure') or len(full['rows'])!=1977:
            raise ValueError('the actual whole cap and all boundary fees did not complete')
        save(self.evidence/'complete-cap-summary.json',{k:v for k,v in full.items() if k!='rows'})
        self.state.update(complete=True,whole_original_cap_complete=True,completed_cells=1977,
            complete_native_sha256=digest(assembled),complete_actual_cap_graph_error=full['complete_actual_cap_graph_error'],
            whole_body_inverse_claimed=False)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--kind',choices=('cap','body'),required=True)
    ap.add_argument('--mode',choices=('hydrate','prepare','consume','finish-cap'),required=True)
    ap.add_argument('--manifest',type=Path,required=True);ap.add_argument('--manifest-sha',required=True)
    ap.add_argument('--rules',type=Path,required=True);ap.add_argument('--rules-sha',required=True)
    ap.add_argument('--driver-sha',required=True)
    ap.add_argument('--recovery-manifest',type=Path);ap.add_argument('--recovery-sha')
    ap.add_argument('--previous-artifacts',type=Path)
    ap.add_argument('--first',type=int,default=0);ap.add_argument('--end',type=int)
    ap.add_argument('--work',type=Path);ap.add_argument('--artifact-dir',type=Path);ap.add_argument('--prepared',type=Path)
    ap.add_argument('--compute-minutes',type=int,default=310);ap.add_argument('--checkpoint-minutes',type=int,default=10)
    args=ap.parse_args();args.manifest=args.manifest.resolve();args.rules=args.rules.resolve()
    if args.end is None:args.end=1977 if args.kind=='cap' else 7721
    if args.recovery_manifest:args.recovery_manifest=args.recovery_manifest.resolve()
    if digest(__file__)!=args.driver_sha:raise ValueError('the requested reviewed driver differs')
    if args.mode=='hydrate':hydrate(args);return
    if args.work is None or args.artifact_dir is None:ap.error('work and artifact-dir are required')
    if args.mode in ('consume','finish-cap') and args.prepared is None:ap.error('the original prepared artifact is required')
    if args.mode=='finish-cap' and (args.kind!='cap' or args.recovery_manifest is None or args.previous_artifacts is None):
        ap.error('complete cap recovery requires its explicit original run and artifact manifest')
    worker=(ReviewedCapWorker if args.kind=='cap' else ReviewedBodyWorker)(args)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
