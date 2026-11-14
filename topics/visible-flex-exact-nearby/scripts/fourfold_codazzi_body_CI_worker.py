#!/usr/bin/env python3
"""Restore fixed regular trials once and consume disjoint original body rows.

Only the complete fixed nodal states are stored as new scientific input.
All full/nonmean Hermite arrays remain Actions artifacts. Existing rows
are reused with their original identity; the mathematical producer is
unchanged. Every new process outcome, failed prefix, and publication is
recorded separately from the historical finite solves.
"""
from __future__ import annotations
import argparse, gzip, hashlib, json, os, shutil, signal, subprocess, sys, time
from pathlib import Path
from fourfold_codazzi_cap128_CI_worker import CapWorker, digest, read, link_exact
from fourfold_codazzi_phase_high7_CI_worker import TOPIC, REPO, save, now
from fourfold_native_lossless_parts import restore, pack

REL=Path('topics/visible-flex-exact-nearby')


def hydrate(args):
    if digest(args.manifest)!=args.manifest_sha:raise ValueError('the complete body input manifest changed')
    manifest=read(args.manifest)
    paths=set(manifest['files'])|set(manifest['readme_sha256'])|{
        str(args.manifest.relative_to(REPO)),str(Path(__file__).relative_to(REPO)),
        str(REL/'scripts/'),str(REL/'notes/correlated_body_ci/')}
    subprocess.run(['git','-c','safe.directory='+str(REPO),'sparse-checkout','set','--no-cone','--stdin'],
        cwd=REPO,input='\n'.join('/'+p for p in sorted(paths))+'\n',text=True,check=True)
    print(json.dumps(dict(exact_requested_paths=len(paths),large_QR_and_Hermite_arrays_excluded=True)))


class BodyWorker(CapWorker):
    def __init__(self,args):
        super().__init__(args)
        suffix='prepare' if args.mode=='prepare' else f'rows{args.first:04d}-{args.end:04d}'
        self.name=f'run-{self.run_label}-{suffix}'
        self.dest=TOPIC/'notes/correlated_body_ci'/self.name
        self.state.update(kind='actual_public_correlated_regular_body_CI_process',
            requested_rows=None if args.mode=='prepare' else [args.first,args.end],
            worker_source_sha256=digest(__file__),original_ac1_operator_not_relabelled_as_repaired=True,
            complete_scalar_mean_error_flow_claimed=False,complete_BVP_inverse_claimed=False,
            whole_original_parameter_half_width='1/1000000000')
        self.state.pop('requested_cells',None)

    def snapshot(self):
        self.dest.mkdir(parents=True,exist_ok=True);entries=[]
        candidates=list(self.evidence.rglob('*'))+list(self.cache.glob('*.json.gz'))
        if (self.artifact/'prepared-manifest.json').exists():candidates.append(self.artifact/'prepared-manifest.json')
        for path in sorted(candidates):
            if not path.is_file():continue
            raw=path.read_bytes();relative=path.relative_to(self.artifact)
            if len(raw)>1_000_000 and path.suffix!='.gz':
                raw=gzip.compress(raw,mtime=0);relative=Path(str(relative)+'.gz')
            if len(raw)>5_000_000:
                exact=self.work/('snapshot-'+hashlib.sha256(raw).hexdigest()+'.json.gz')
                if not exact.exists():exact.write_bytes(raw)
                manifest=self.dest/(str(relative).replace('/','-')+'-'+digest(exact)[:16]+'-parts.json')
                packed=pack(exact,manifest,2_000_000)
                entries.append(dict(logical_file=str(relative),lossless_manifest=manifest.name,
                    bytes=len(raw),sha256=digest(exact),parts=len(packed['parts'])))
                continue
            target=self.dest/relative;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(raw)
            entries.append(dict(logical_file=str(relative),file=str(relative),bytes=len(raw),
                sha256=hashlib.sha256(raw).hexdigest()))
        if self.log.exists():
            raw=gzip.compress(self.log.read_bytes(),mtime=0)
            if len(raw)<=5_000_000:(self.dest/'producer.stdout.log.gz').write_bytes(raw)
            else:self.state['full_stdout_preserved_in_artifact']=digest(self.log)
        self.state.update(snapshot_utc=now(),wall_seconds=time.monotonic()-self.started,native_files=entries)
        save(self.statusfile,self.state);save(self.dest/'process.json',self.state)

    def publish(self,final=False):
        self.sync();self.snapshot()
        self.git(['add','--sparse','--',str(self.dest.relative_to(REPO))])
        if self.git(['diff','--cached','--quiet'],check=False).returncode==0:return
        self.git(['commit','-m',f'visible-exact: {"finish" if final else "checkpoint"} actual body {self.args.mode} {self.args.first}-{self.args.end}'])
        while True:
            result=self.git(['push','--no-thin','origin','HEAD:refs/heads/main'],check=False)
            print(result.stdout,flush=True)
            if result.returncode==0:
                self.state['published_checkpoints'].append(dict(time=now(),
                    commit=self.git(['rev-parse','HEAD']).stdout.strip(),final=final))
                save(self.statusfile,self.state);return
            if not any(s in result.stdout for s in ('fetch first','non-fast-forward','failed to update ref','remote rejected','rejected')):
                raise RuntimeError('actual publication failed for a reason other than concurrent main updates')
            self.sync();save(self.dest/'process.json',self.state)
            self.git(['add','--sparse','--',str((self.dest/'process.json').relative_to(REPO))])
            self.git(['commit','--amend','--no-edit'])

    def prepare(self):
        candidate=self.science/self.manifest['published_candidate']
        nodal=self.science/self.manifest['nodal_manifest']
        candidate_dir=self.artifact/'candidate';candidate_dir.mkdir(exist_ok=True)
        for name in [candidate.name]+[x['file'] for x in read(candidate)['parts']]:
            shutil.copyfile(candidate.parent/name,candidate_dir/name)
        if digest(candidate_dir/candidate.name)!=self.manifest['candidate_sha256']:
            raise ValueError('the entire original background candidate changed')
        mean_dir=self.artifact/'mean';mean_dir.mkdir(exist_ok=True)
        restore(self.science/self.manifest['mean_parts_manifest'],mean_dir/'native.json.gz')
        if digest(mean_dir/'native.json.gz')!=self.manifest['mean_sha256']:
            raise ValueError('the complete original mean native changed')
        aliases={self.manifest['canonical_candidate_directory']:'candidate',
                 self.manifest['canonical_mean_directory']:'mean'}
        for role in ('response','adjoint'):
            directory=self.artifact/'trials'/role
            self.execute('restore_original_'+role+'_Hermite_trial',[
                sys.executable,'-u',str(self.science_topic/'scripts/fourfold_codazzi_regular_trial_from_fixed_nodes.py'),
                '--nodal-manifest',str(nodal),'--role',role,'--candidate',str(candidate),
                '--work',str(self.work/('rebuild-'+role)),'--trial-directory',str(directory),
                '--out',str(self.evidence/(role+'-actual-reconstruction.json'))])
            actual=read(self.evidence/(role+'-actual-reconstruction.json'))
            if not actual.get('complete') or actual.get('failure') or not actual.get('all_original_shards_match'):
                raise ValueError('the actual original full trial did not reconstruct')
            aliases[self.manifest['canonical_trial_directories'][role]]=str(directory.relative_to(self.artifact))
        files={}
        for folder in ('candidate','mean','trials'):
            for path in sorted((self.artifact/folder).rglob('*')):
                if path.is_file():files[str(path.relative_to(self.artifact))]=dict(sha256=digest(path),bytes=path.stat().st_size)
        bundle=dict(kind='exact_same_all_regular_body_CI_bundle_v1',complete=True,
            input_manifest_sha256=self.args.manifest_sha,files=files,canonical_aliases=aliases,
            all_original_cubic_and_trial_shard_SHA256_verified=True,
            historical_finite_solve_not_relabelled_as_new_execution=True,
            complete_body_residual_proved=False,complete_BVP_inverse_proved=False)
        save(self.artifact/'prepared-manifest.json',bundle)
        self.state.update(complete=True,prepared_bundle_sha256=digest(self.artifact/'prepared-manifest.json'),
            all_original_scientific_bytes_reconstructed=True)

    def known_prefixes(self):
        paths=[self.science/x for x in self.manifest['original_partial_prefixes']]
        root=TOPIC/'notes/correlated_body_ci'
        paths.extend(root.glob('*/native/*.json.gz'))
        for status in root.glob('*/process.json'):
            for entry in read(status).get('native_files',[]):
                if not entry.get('logical_file','').startswith('native/') or 'lossless_manifest' not in entry:continue
                source=status.parent/entry['lossless_manifest'];target=self.work/('restored-prefix-'+entry['sha256']+'.json.gz')
                restore(source,target)
                if digest(target)!=entry['sha256']:raise ValueError('the published row prefix changed')
                paths.append(target)
        candidates={}
        for path in paths:
            doc=read(path)
            if (doc.get('kind')!=self.manifest['residual_kind'] or doc.get('failure') is not None
                or doc.get('identity')!=self.manifest['row_identity']):continue
            first,end=doc['selected_indices'];rows=doc['rows']
            if not rows or [r['common_row'] for r in rows]!=list(range(first,first+len(rows))):
                raise ValueError('a published prefix is not its original consecutive rows')
            key=(first,end)
            if key not in candidates or len(rows)>candidates[key][1]:candidates[key]=(path,len(rows),doc)
        return candidates

    def consume(self):
        prepared=self.args.prepared.resolve();bundle=read(prepared/'prepared-manifest.json')
        if (bundle.get('kind')!='exact_same_all_regular_body_CI_bundle_v1' or not bundle.get('complete')
            or bundle['input_manifest_sha256']!=self.args.manifest_sha
            or not bundle.get('all_original_cubic_and_trial_shard_SHA256_verified')):
            raise ValueError('a complete same-scientific-trial body preparation is required')
        for relative,entry in bundle['files'].items():
            path=prepared/relative
            if path.stat().st_size!=entry['bytes'] or digest(path)!=entry['sha256']:
                raise ValueError('an original prepared complete body input changed')
        for canonical,relative in bundle['canonical_aliases'].items():link_exact(canonical,prepared/relative)
        for original,expected in self.manifest['row_identity']['original_inputs'].items():
            path=Path(original) if Path(original).is_absolute() else self.science_topic/original
            if digest(path)!=expected:raise ValueError('the original canonical scientific input differs')
        assigned=self.manifest['atomic_ranges'][f'{self.args.first}-{self.args.end}']
        prefixes=self.known_prefixes();self.state['actual_atomic_ranges']=assigned;completed=[]
        for first,end in assigned:
            native=self.cache/f'rows-{first:05d}-{end:05d}.json.gz'
            prefix=prefixes.get((first,end))
            if prefix is not None and prefix[2].get('selected_cells_complete'):
                if prefix[1]!=end-first:raise ValueError('a completed published part has an incomplete cover')
                shutil.copyfile(prefix[0],native)
                self.state.setdefault('consumed_completed_parts',[]).append(dict(
                    path=str(prefix[0]),sha256=digest(prefix[0]),indices=[first,end]))
            else:
                command=[sys.executable,'-u',str(self.science_topic/'scripts/fourfold_codazzi_correlated_head_residual_rows.py')]
                for name,path in self.manifest['original_cli_inputs'].items():command+=['--'+name,path]
                command+=['--first',str(first),'--count',str(end-first),'--out',str(native)]
                if prefix is not None:
                    fixed=self.work/f'original-prefix-{first}-{end}.json.gz';shutil.copyfile(prefix[0],fixed)
                    command+=['--resume',str(fixed)]
                    self.state.setdefault('consumed_original_prefixes',[]).append(dict(
                        path=str(prefix[0]),sha256=digest(prefix[0]),actual_rows=prefix[1],indices=[first,end]))
                self.execute(f'actual_body_rows_{first}_{end}',command)
            doc=read(native)
            if (doc.get('failure') is not None or not doc.get('selected_cells_complete')
                or doc['selected_indices']!=[first,end] or len(doc['rows'])!=end-first
                or doc['identity']!=self.manifest['row_identity']):
                raise ValueError('the requested complete original body row range failed')
            completed.append(dict(indices=[first,end],sha256=digest(native),rows=end-first))
            self.state['completed_atomic_parts']=completed;self.publish()
        self.state.update(complete=True,completed_rows=sum(x['rows'] for x in completed),
            complete_full_body_cover_claimed=False,complete_scalar_mean_error_flow_claimed=False,
            complete_BVP_inverse_claimed=False)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--mode',choices=('hydrate','prepare','consume'),required=True)
    ap.add_argument('--manifest',type=Path,required=True);ap.add_argument('--manifest-sha',required=True)
    ap.add_argument('--first',type=int,default=0);ap.add_argument('--end',type=int,default=7721)
    ap.add_argument('--work',type=Path);ap.add_argument('--artifact-dir',type=Path);ap.add_argument('--prepared',type=Path)
    ap.add_argument('--compute-minutes',type=int,default=310);ap.add_argument('--checkpoint-minutes',type=int,default=10)
    args=ap.parse_args();args.manifest=args.manifest.resolve()
    if args.mode=='hydrate':hydrate(args);return
    if args.work is None or args.artifact_dir is None:ap.error('work and artifact-dir are required')
    if args.mode=='consume' and args.prepared is None:ap.error('consume requires the original complete trial bundle')
    worker=BodyWorker(args)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
