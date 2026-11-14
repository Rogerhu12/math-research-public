#!/usr/bin/env python3
"""Reconstruct the original cap trial once, then consume disjoint real cells.

The large arrays travel only as a GitHub Actions artifact. A historical
proposal descriptor is consumed only after the new arrays have exactly
its scientific SHA256s; the new process outcomes are recorded separately.
No equation, source identity, Fourier tail, mean, or arithmetic gate changes.
"""
from __future__ import annotations
import argparse, gzip, hashlib, importlib.metadata, json, os, shutil, signal
import subprocess, sys, time
from pathlib import Path
from fourfold_codazzi_phase_high7_CI_worker import Worker as PublishingWorker
from fourfold_codazzi_phase_high7_CI_worker import TOPIC, REPO, save, now

REL=Path('topics/visible-flex-exact-nearby')
REPOSITORY='Rogerhu12/math-research-public'


def digest(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(1024*1024),b''):h.update(block)
    return h.hexdigest()


def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw)


def link_exact(link,target):
    """Only a fresh runner's owned canonical alias; never replace a file."""
    link,target=Path(link),Path(target).resolve()
    if link.is_symlink():
        if link.resolve()!=target:raise ValueError('a canonical path already has a different target')
        return
    if link.exists():
        if link.resolve()!=target:raise FileExistsError('refusing to replace an existing canonical directory')
        return
    link.parent.mkdir(parents=True,exist_ok=True);link.symlink_to(target,target_is_directory=True)


def hydrate(args):
    if digest(args.manifest)!=args.manifest_sha:raise ValueError('the input manifest changed')
    doc=read(args.manifest)
    paths=set(doc['files'])|set(doc['readme_sha256'])|{
        str(args.manifest.relative_to(REPO)),str(Path(__file__).relative_to(REPO)),
        str(REL/'scripts/'),str(REL/'notes/physical_cap128_ci/')}
    patterns='\n'.join('/'+p for p in sorted(paths))+'\n'
    subprocess.run(['git','-c','safe.directory='+str(REPO),'sparse-checkout','set',
        '--no-cone','--stdin'],cwd=REPO,input=patterns,text=True,check=True)
    print(json.dumps({'requested_exact_paths':len(paths),'large_intermediate_data_excluded':True}))


class CapWorker(PublishingWorker):
    def __init__(self,args):
        args.germ_start=args.first;args.germ_stop=args.end
        super().__init__(args)
        suffix='prepare' if args.mode=='prepare' else f'cells{args.first:04d}-{args.end:04d}'
        self.name=f'run-{self.run_label}-{suffix}'
        self.dest=TOPIC/'notes'/'physical_cap128_ci'/self.name
        self.evidence=self.artifact/'evidence';self.evidence.mkdir(exist_ok=True)
        self.work=args.work.resolve();self.work.mkdir(parents=True,exist_ok=True)
        self.science=self.work/'science';self.science_topic=self.science/REL
        self.state=dict(kind='actual_public_physical128_cap_CI_process',complete=False,
            repository=REPOSITORY,run_id=os.environ.get('GITHUB_RUN_ID'),
            run_attempt=os.environ.get('GITHUB_RUN_ATTEMPT'),mode=args.mode,
            requested_cells=None if args.mode=='prepare' else [args.first,args.end],
            workflow_commit=os.environ.get('GITHUB_SHA'),worker_source_sha256=digest(__file__),
            started_utc=now(),children=[],readme_checks=[],published_checkpoints=[],
            original_scientific_sources_unchanged=True,whole_body_inverse_claimed=False)

    def check_inputs(self):
        if digest(self.args.manifest)!=self.args.manifest_sha:
            raise ValueError('the reviewed manifest changed')
        self.manifest=read(self.args.manifest)
        if os.environ.get('GITHUB_REPOSITORY')!=REPOSITORY:
            raise ValueError('this execution belongs only to the migrated public repository')
        if self.args.mode=='consume' and [self.args.first,self.args.end] not in self.manifest['consumer_ranges']:
            raise ValueError('an unassigned or overlapping cap range was requested')
        for rel,expected in self.manifest['files'].items():
            if digest(REPO/rel)!=expected:raise ValueError('scientific source/input changed: '+rel)
        for rel,expected in self.manifest['readme_sha256'].items():
            if digest(REPO/rel)!=expected:raise ValueError('the reviewed README changed: '+rel)
        packages={name:importlib.metadata.version(name) for name in self.manifest['packages']}
        if packages!=self.manifest['packages']:raise ValueError('the pinned arithmetic environment changed')
        if '.'.join(map(str,sys.version_info[:3]))!=self.manifest['python_version']:
            raise ValueError('the exact reconstruction Python version changed')
        self.state.update(input_manifest_sha256=self.args.manifest_sha,
            package_versions=packages,all_pinned_inputs_verified=True)

    def science_copy(self):
        # git pulls never mutate the source tree of an active mathematical child.
        for rel,expected in self.manifest['files'].items():
            source,target=REPO/rel,self.science/rel
            target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists():
                if digest(target)!=expected:raise ValueError('immutable scientific copy changed')
            else:shutil.copyfile(source,target)
        self.state['immutable_scientific_copy']=str(self.science)

    def snapshot(self):
        self.dest.mkdir(parents=True,exist_ok=True);entries=[]
        candidates=list(self.evidence.rglob('*'))
        if (self.artifact/'native.json.gz').exists():candidates.append(self.artifact/'native.json.gz')
        if (self.artifact/'prepared-manifest.json').exists():candidates.append(self.artifact/'prepared-manifest.json')
        for path in sorted(candidates):
            if not path.is_file():continue
            raw=path.read_bytes();relative=path.relative_to(self.artifact)
            # Scientific arrays are never among the evidence candidates.
            if len(raw)>1_000_000 and path.suffix!='.gz':
                raw=gzip.compress(raw,mtime=0);relative=Path(str(relative)+'.gz')
            if len(raw)>5_000_000:
                self.state.setdefault('artifact_only_evidence',{})[str(relative)]=digest(path);continue
            target=self.dest/relative;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(raw)
            entries.append(dict(path=str(relative),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest()))
        if self.log.exists():
            data=gzip.compress(self.log.read_bytes(),mtime=0)
            if len(data)<=5_000_000:(self.dest/'producer.stdout.log.gz').write_bytes(data)
        self.state.update(snapshot_utc=now(),wall_seconds=time.monotonic()-self.started,native_files=entries)
        save(self.statusfile,self.state);save(self.dest/'process.json',self.state)

    def publish(self,final=False):
        self.sync();self.snapshot()
        self.git(['add','--sparse','--',str(self.dest.relative_to(REPO))])
        if self.git(['diff','--cached','--quiet'],check=False).returncode==0:return
        label='finish' if final else 'checkpoint'
        self.git(['commit','-m',f'visible-exact: {label} actual cap128 {self.args.mode} {self.args.first}-{self.args.end}'])
        while True:
            result=self.git(['push','--no-thin','origin','HEAD:refs/heads/main'],check=False)
            print(result.stdout,flush=True)
            if result.returncode==0:
                self.state['published_checkpoints'].append(dict(time=now(),commit=self.git(['rev-parse','HEAD']).stdout.strip(),final=final))
                save(self.statusfile,self.state);return
            if not any(s in result.stdout for s in ('fetch first','non-fast-forward','failed to update ref','remote rejected','rejected')):
                raise RuntimeError('actual push failed for a reason other than concurrent main updates')
            self.sync();save(self.dest/'process.json',self.state)
            self.git(['add','--sparse','--',str((self.dest/'process.json').relative_to(REPO))])
            self.git(['commit','--amend','--no-edit'])

    def execute(self,label,command):
        item=dict(label=label,command=command,started_utc=now(),actual_returncode=None)
        self.state['children'].append(item);save(self.statusfile,self.state)
        start=time.monotonic()
        with self.log.open('ab') as stream:
            self.child=subprocess.Popen(command,cwd=self.science_topic,env=self.env,
                stdout=stream,stderr=subprocess.STDOUT,start_new_session=True)
            previous=time.monotonic()
            while self.child.poll() is None:
                if self.interrupted:
                    self.terminate_child('runner signal observed');break
                if time.monotonic()-self.started>self.args.compute_minutes*60:
                    self.terminate_child('bounded CI slot ended; actual prefix retained');break
                if time.monotonic()-previous>self.args.checkpoint_minutes*60:
                    self.publish();previous=time.monotonic()
                time.sleep(5)
        item.update(actual_returncode=self.child.returncode,wall_seconds=time.monotonic()-start,finished_utc=now())
        save(self.statusfile,self.state)
        if self.child.returncode:raise RuntimeError(label+' returned '+str(self.child.returncode))
        self.publish()

    def historical(self,key):return self.science/self.manifest[key]

    def prepare(self):
        candidate=self.science/self.manifest['published_candidate']
        if digest(candidate)!=self.manifest['candidate_sha256']:
            raise ValueError('the published complete original centre changed')
        candidate_files={candidate.name:digest(candidate)}
        for item in read(candidate)['parts']:
            part=candidate.parent/item['file']
            if part.stat().st_size!=item['bytes'] or digest(part)!=item['sha256']:
                raise ValueError('a complete original candidate shard changed')
            candidate_files[part.name]=digest(part)
        self.state['consumed_published_original_candidate']=candidate_files
        save(self.evidence/'published-candidate-input.json',dict(
            complete=True,all_original_parts_verified=True,files=candidate_files,
            reused_original_candidate_not_replayed=True,scientific_centre_unchanged=True))
        actual_parent=self.evidence/'physical128-proposal-actual.json'
        self.execute('all128_physical_columns',[sys.executable,'-u',str(self.science_topic/'scripts/fourfold_codazzi_physical_cap_DN_padded_proposal.py'),
            '--candidate',str(candidate),'--physical-modes','128','--left','9/10','--max-new-blocks','10000000',
            '--work',str(self.work/'cap-build'),'--out',str(actual_parent)])
        historical_parent=read(self.historical('parent_descriptor'))
        historical_child=read(self.historical('precomposed_descriptor'))
        generated=read(actual_parent)
        if not generated.get('complete') or generated.get('failure') or not generated['actual_finite_backward_check']['passed']:
            raise ValueError('the new finite graph actually failed')
        if generated['identity']!=historical_parent['identity'] or generated['case']!=historical_parent['case']:
            raise ValueError('the regenerated physical graph has a different scientific definition')
        canonical_parent=Path(historical_parent['work_directory']);actual_directory=Path(generated['work_directory'])
        checked={}
        for old_path,expected in historical_child['identity']['full_parent_array_sha256'].items():
            source=actual_directory/Path(old_path).relative_to(canonical_parent)
            actual=digest(source)
            if actual!=expected:raise ValueError('regenerated physical128 array differs: '+Path(old_path).name)
            checked[old_path]=actual
        link_exact(canonical_parent,actual_directory)
        base=Path(historical_child['work_directory']).parent
        destination=self.artifact/'cap';destination.mkdir(exist_ok=True);link_exact(base,destination)
        actual_child=self.evidence/'moving97-precomposition-actual.json'
        self.execute('all97_true_moving_inputs',[sys.executable,'-u',str(self.science_topic/'scripts/fourfold_codazzi_physical_cap_precompose_moving_head.py'),
            '--proposal',str(self.historical('parent_descriptor')),'--work',str(base),'--out',str(actual_child)])
        result=read(actual_child)
        if not result.get('complete') or result.get('failure') or result['identity']!=historical_child['identity']:
            raise ValueError('the regenerated complete moving trial differs')
        files={}
        for old_path,expected in historical_child['full_matrix_inputs'].items():
            source=Path(old_path)
            if digest(source)!=expected:raise ValueError('regenerated moving97 array differs: '+source.name)
            relative=source.resolve().relative_to(self.artifact)
            files[str(relative)]=dict(sha256=expected,bytes=source.stat().st_size)
        endpoint=Path(historical_child['physical_endpoint_graph']['path'])
        if digest(endpoint)!=historical_child['physical_endpoint_graph']['sha256']:
            raise ValueError('the regenerated original endpoint container differs')
        files[str(endpoint.resolve().relative_to(self.artifact))]=dict(sha256=digest(endpoint),bytes=endpoint.stat().st_size)
        candidate_dir=self.artifact/'candidate';candidate_dir.mkdir(exist_ok=True)
        for name in [candidate.name]+[p['file'] for p in read(candidate)['parts']]:
            source,target=candidate.parent/name,candidate_dir/name
            if target.exists():raise FileExistsError('preserve the original copied candidate')
            shutil.copyfile(source,target)
            files[str(target.relative_to(self.artifact))]=dict(sha256=digest(target),bytes=target.stat().st_size)
        bundle=dict(kind='exact_same_cap128_moving97_CI_bundle',complete=True,
            input_manifest_sha256=self.args.manifest_sha,candidate=str((candidate_dir/candidate.name).relative_to(self.artifact)),
            candidate_sha256=digest(candidate),canonical_directory=historical_child['work_directory'],
            array_directory=str(Path(historical_child['work_directory']).resolve().relative_to(self.artifact)),files=files,
            parent_descriptor_sha256=digest(self.historical('parent_descriptor')),
            precomposed_descriptor_sha256=digest(self.historical('precomposed_descriptor')),
            every_regenerated_array_matches_historical_bytes=True,
            actual_new_process_reports_are_separate=True,large_arrays_not_committed=True)
        save(self.artifact/'prepared-manifest.json',bundle)
        self.state.update(reconstructed_all_original_array_sha256=checked,prepared_bundle_sha256=digest(self.artifact/'prepared-manifest.json'),complete=True)

    def consume(self):
        prepared=self.args.prepared.resolve();bundle=read(prepared/'prepared-manifest.json')
        if (bundle.get('kind')!='exact_same_cap128_moving97_CI_bundle' or not bundle.get('complete')
            or bundle['input_manifest_sha256']!=self.args.manifest_sha
            or not bundle.get('every_regenerated_array_matches_historical_bytes')):
            raise ValueError('a complete same-scientific-trial preparation is required')
        for rel,entry in bundle['files'].items():
            path=prepared/rel
            if path.stat().st_size!=entry['bytes'] or digest(path)!=entry['sha256']:
                raise ValueError('a complete prepared array or candidate shard changed: '+rel)
        proposal=self.historical('precomposed_descriptor');old=read(proposal)
        if digest(proposal)!=bundle['precomposed_descriptor_sha256'] or old['work_directory']!=bundle['canonical_directory']:
            raise ValueError('the exact historical descriptor changed')
        link_exact(old['work_directory'],prepared/bundle['array_directory'])
        for path,expected in old['full_matrix_inputs'].items():
            if digest(path)!=expected:raise ValueError('canonical array mapping changed')
        candidate=prepared/bundle['candidate']
        if digest(candidate)!=self.manifest['candidate_sha256']:raise ValueError('the complete candidate changed')
        native=self.artifact/'native.json.gz';prefix=None;best=-1
        if self.args.first==768:
            prefix=self.science/self.manifest['original_prefix'];best=len(read(prefix)['rows'])
        # A rerun takes the most advanced actual same-range checkpoint.
        for path in (TOPIC/'notes/physical_cap128_ci').glob('*/native.json.gz'):
            d=read(path)
            if (d.get('first')!=self.args.first or d.get('end')!=self.args.end or d.get('failure')
                or d.get('kind')!=self.manifest['residual_kind']
                or d.get('identity',{}).get('source_sha256')!=self.manifest['residual_sha256']):continue
            if len(d.get('rows',[]))>best:prefix=path;best=len(d['rows'])
        command=[sys.executable,'-u',str(self.science_topic/'scripts/fourfold_codazzi_physical_cap_matrix_residual_packed_v5.py'),
            '--candidate',str(candidate),'--proposal',str(proposal),
            '--first',str(self.args.first),'--count',str(self.args.end-self.args.first),'--out',str(native)]
        if prefix is not None:
            immutable=self.work/'original-prefix.json.gz';shutil.copyfile(prefix,immutable)
            command+=['--resume',str(immutable)]
            self.state['consumed_original_prefix']=dict(path=str(prefix),sha256=digest(prefix),rows=best)
        self.execute('complete_original_continuous_cells',command)
        result=read(native)
        if (result.get('failure') or not result.get('selected_cells_complete')
            or result['first']!=self.args.first or result['end']!=self.args.end
            or len(result['rows'])!=self.args.end-self.args.first):
            raise ValueError('the requested exact closed-cell range is incomplete')
        self.state.update(complete=True,completed_cells=len(result['rows']),native_sha256=digest(native),
            whole_cap_complete=False,independent_mean_and_infinite_tails_retained=True)

    def run_cap(self):
        self.check_inputs()
        if not os.environ.get('GITHUB_TOKEN'):raise RuntimeError('terminal publication credential unavailable')
        self.git(['config','user.name','github-actions[bot]'])
        self.git(['config','user.email','41898282+github-actions[bot]@users.noreply.github.com'])
        self.sync();self.science_copy()
        try:
            self.prepare() if self.args.mode=='prepare' else self.consume()
        except BaseException as error:
            self.terminate_child('actual wrapper exception; preserve the real prefix')
            self.state['failure']=dict(type=type(error).__name__,message=str(error))
            self.snapshot()
            try:self.publish(final=True)
            except Exception as publication_error:
                self.state['publication_failure']=str(publication_error);save(self.statusfile,self.state)
            raise
        self.state['finished_utc']=now();self.publish(final=True)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--mode',choices=('hydrate','prepare','consume'),required=True)
    ap.add_argument('--manifest',type=Path,required=True);ap.add_argument('--manifest-sha',required=True)
    ap.add_argument('--first',type=int,default=0);ap.add_argument('--end',type=int,default=1977)
    ap.add_argument('--work',type=Path);ap.add_argument('--artifact-dir',type=Path);ap.add_argument('--prepared',type=Path)
    ap.add_argument('--compute-minutes',type=int,default=310);ap.add_argument('--checkpoint-minutes',type=int,default=10)
    args=ap.parse_args();args.manifest=args.manifest.resolve()
    if args.mode=='hydrate':hydrate(args);return
    if args.work is None or args.artifact_dir is None:ap.error('work and artifact-dir are required')
    if args.mode=='consume' and args.prepared is None:ap.error('consume requires the prepared bundle')
    worker=CapWorker(args)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
