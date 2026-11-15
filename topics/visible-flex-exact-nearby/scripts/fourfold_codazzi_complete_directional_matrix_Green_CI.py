#!/usr/bin/env python3
"""Actual complete directional matrix Green, with immutable array origins.

Only this public repository is used. All old scientific arrays stay in
Actions artifacts. Every matrix row is independently checkpointed; a
publication failure does not invalidate a preceding mathematical success.
"""
from __future__ import annotations
import argparse,fcntl,hashlib,json,os,shutil,signal,stat,sys,time,urllib.error,urllib.request,zipfile
from collections import defaultdict
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_finite193_L2_Green_kernel_CI import KernelWorker
from fourfold_codazzi_finite193_cached_interface_impulse_gains_CI import ImpulseWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC,REPO

REL='topics/visible-flex-exact-nearby/'
PRODUCER=REL+'scripts/fourfold_codazzi_complete_directional_matrix_Green.py'
FOLDER='notes/complete_directional_matrix_Green_ci'
KIND='actual_complete_direction_preserving_finite193_matrix_Green_v1'
LOCAL_SOURCE='e2cedf8860bbf807a3db66718fd9d195b5c312776f1902d492aa8180e1525d59'
LOCAL_WORKER='71b203d54afc982de4ac762a7486cd99bde7acbd9ca50d7ca9c486a283c1326b'
LOCAL_MANIFEST='8d334ee75c0cf78a13b31483ceb495194c73e7cbcf57c1eeec3f447da17cab19'
LOCAL_KIND='actual_complete_same_F_directional_matrix_data_from_cached5970_v2'
LOCAL_NAME='complete5970-same-F-directional-matrix-data.json.gz'
PLAN='d893f609bc12e58720444b99a565dc5fdb79df1842cdab4ba6da3ac695a46fd4'
PROFILE='3460a4b5636bf6a3d9c160f6141ab5153fc5fc705ca79000c5f10370a978cb69'
PROFILE_PROCESS='16608b57571d17a427857bcfe0127186589b3f79e93d89a7e423ac48a2740af9'
IMPULSE='fbba350708fb89366272641433e9c2899c4ec04027616650b4317969105bcd37'
IMPULSE_PROCESS='b55c2df02439b910c1e6e46fb78c2391ca135138421e2f05ee05a14dcb5de468'
IMPULSE_REVIEW=REL+'notes/finite193_cached_interface_impulse_ci/run-43649423561-1-all5970-cached-interface-impulse-gains/process.json'
BOUNDARY='56db8a3498494bf48de14b50418010053bb6058c722c41993c894c463786dc25'
CUT=REL+'notes/2026-11-14-R133-complete-moving-cap-cut-boundary-v2-native.json.gz'
REPOSITORY='Rogerhu12/math-research-public'
LABELS=dict(backward='all5970_complete97_future_directional_covariance_rows',
    forward='all5970_complete96_past_covariances_true_boundaries_and_posterior_directional_Green')


def small(path,d):
    raw=(json.dumps(d,ensure_ascii=False,indent=2)+'\n').encode()
    if len(raw)>60000:raise ValueError('one matrix Green evidence file exceeds60000 UTF8 bytes')
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(raw)


def native_name(phase):return 'complete-directional-matrix-Green-'+phase+'.json.gz'


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,request,fp,code,msg,headers,newurl):return None


class MatrixGreenWorker(ReviewedBodyWorker):
    exact_native=KernelWorker.exact_native

    def __init__(self,a):
        super().__init__(a)
        self.name=f'run-{self.run_label}-directional-matrix-Green-{a.phase}'
        self.dest=TOPIC/FOLDER/self.name
        self.native_name=native_name(a.phase)
        self.input_root=self.work/'original-public-inputs'
        self.array_root=self.work/'original-public-array-artifacts'
        self.new_arrays=self.artifact/'matrices'
        for p in (self.input_root,self.array_root,self.new_arrays):p.mkdir(parents=True,exist_ok=True)
        self.artifact_cache={};self.last_download_pull=time.monotonic()
        self.reused_complete=False
        self.state.update(kind='actual_public_complete_directional_matrix_Green_process_v1',
            worker_source_sha256=digest(__file__),phase=a.phase,
            complete_matrix_run=str(a.matrix_run),complete_matrix_attempt=str(a.matrix_attempt),
            original_targets_F_C_source_Grams_output_Grams_and_scalar_ports_recomputed=0,
            complete_finite193_directional_two_boundary_bound_proved=False,
            complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False,
            new_array_storage='original public Actions artifacts only',
            complete_rows_reused_despite_later_publication_failure=True)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='complete_direction_preserving_finite193_matrix_Green_public_inputs_v1':
            raise ValueError('the separate complete matrix Green input manifest is required')
        # This hook runs BEFORE science_copy. Every path here is the
        # exact repository copy already verified by ReviewedRules.
        old=read(REPO/self.manifest['original_complete_matrix_manifest'])
        if (digest(REPO/self.manifest['original_complete_matrix_manifest'])!=LOCAL_MANIFEST
            or any(self.manifest['files'].get(k)!=v for k,v in old['files'].items())):
            raise ValueError('an original complete matrix pin changed')
        if digest(REPO/IMPULSE_REVIEW)!=IMPULSE_PROCESS:
            raise ValueError('the separately reviewed original impulse process changed')

    def api(self,path):
        if not path.startswith('/repos/'+REPOSITORY+'/'):
            raise ValueError('only the authorized public repository API may be accessed')
        token=os.environ.get('GITHUB_TOKEN')
        if not token:raise RuntimeError('the public runner token is unavailable')
        request=urllib.request.Request('https://api.github.com'+path,
            headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json',
                     'X-GitHub-Api-Version':'2022-11-28'})
        with urllib.request.urlopen(request,timeout=90) as response:return json.load(response)

    def pull_during_download(self):
        if time.monotonic()-self.last_download_pull>self.args.checkpoint_minutes*60:
            self.publish()
            self.last_download_pull=time.monotonic()

    def artifact_metadata(self,run,name):
        if Path(name).name!=name or not str(run).isdigit():
            raise ValueError('one original artifact has an unsafe name or run')
        key=(str(run),name)
        if key in self.artifact_cache:return self.artifact_cache[key]
        matches=[]
        for page in range(1,101):
            d=self.api(f'/repos/{REPOSITORY}/actions/runs/{run}/artifacts?per_page=100&page={page}')
            entries=d.get('artifacts',[])
            matches.extend(x for x in entries if x.get('name')==name)
            if len(entries)<100:break
        if len(matches)!=1 or matches[0].get('expired'):
            raise ValueError('one exact original public artifact is absent, duplicated or expired')
        a=matches[0]
        if str(a.get('workflow_run',{}).get('id'))!=str(run):
            raise ValueError('the original artifact belongs to another run')
        self.artifact_cache[key]=a;return a

    def zip_download(self,metadata,path):
        token=os.environ['GITHUB_TOKEN']
        url=f"https://api.github.com/repos/{REPOSITORY}/actions/artifacts/{metadata['id']}/zip"
        request=urllib.request.Request(url,headers={'Authorization':'Bearer '+token,
            'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'})
        opener=urllib.request.build_opener(NoRedirect)
        try:
            response=opener.open(request,timeout=90)
        except urllib.error.HTTPError as e:
            if e.code not in (301,302,303,307,308):raise
            location=e.headers.get('Location','')
            if not location.startswith('https://'):raise ValueError('artifact download redirect is not HTTPS')
            # No repository credential is forwarded to the signed archive URL.
            response=urllib.request.urlopen(location,timeout=90)
        path.parent.mkdir(parents=True,exist_ok=True)
        h=hashlib.sha256();count=0
        with response,path.open('wb') as output:
            while True:
                data=response.read(8*1024*1024)
                if not data:break
                output.write(data);h.update(data);count+=len(data)
                self.pull_during_download()
        if not count:raise ValueError('the original artifact archive is empty')
        return dict(bytes=count,sha256=h.hexdigest())

    def download(self,run,name,arrays_only=False):
        target=(self.array_root if arrays_only else self.input_root)/name
        marker=target/'actual-original-artifact-download.json'
        metadata=self.artifact_metadata(run,name)
        if marker.exists():
            d=read(marker)
            if (d.get('repository')!=REPOSITORY or str(d.get('run_id'))!=str(run)
                or d.get('artifact_id')!=metadata['id'] or d.get('arrays_only')!=arrays_only):
                raise ValueError('one staged original artifact has a different exact identity')
            return target
        archive=self.work/f"download-original-artifact-{metadata['id']}.zip"
        actual=self.zip_download(metadata,archive);target.mkdir(parents=True,exist_ok=True)
        extracted=0
        with zipfile.ZipFile(archive) as z:
            for info in z.infolist():
                name0=info.filename;relative=Path(name0)
                if (relative.is_absolute() or '..' in relative.parts
                    or stat.S_ISLNK(info.external_attr>>16)):
                    raise ValueError('an original artifact contains a nonordinary path')
                if info.is_dir():continue
                if arrays_only and name0!='process.json' and not name0.startswith('matrices/'):continue
                out=target/relative;out.parent.mkdir(parents=True,exist_ok=True)
                with z.open(info) as source,out.open('wb') as destination:
                    shutil.copyfileobj(source,destination,8*1024*1024)
                extracted+=1;self.pull_during_download()
        if not extracted or not (target/'process.json').exists():
            raise ValueError('one original artifact has no actual process or requested scientific files')
        process=read(target/'process.json')
        if (process.get('repository')!=REPOSITORY or str(process.get('run_id'))!=str(run)):
            raise ValueError('the downloaded actual process belongs to another repository or run')
        receipt=dict(repository=REPOSITORY,run_id=str(run),run_attempt=str(process.get('run_attempt')),
            artifact_name=name,artifact_id=metadata['id'],api_size_in_bytes=metadata['size_in_bytes'],
            exact_downloaded_archive=actual,arrays_only=arrays_only,extracted_files=extracted,
            actual_process_sha256=digest(target/'process.json'))
        small(marker,receipt)
        small(self.evidence/'original-artifact-downloads'/f"{metadata['id']}.json",receipt)
        archive.unlink()
        self.pull_during_download();return target

    def record_process(self,path,name):
        destination=self.evidence/name;destination.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(path,destination)

    def matrix_inputs(self):
        run=self.args.matrix_run;attempt=self.args.matrix_attempt
        root=self.download(run,f'visible-exact-complete-same-F-5970-finish-{run}-{attempt}')
        pp=root/'process.json';p=read(pp)
        if (str(p.get('run_attempt'))!=str(attempt)
            or p.get('phase')!='finish' or p.get('worker_source_sha256')!=LOCAL_WORKER
            or p.get('input_manifest_sha256')!=LOCAL_MANIFEST):
            raise ValueError('the actual complete matrix finish has another frozen identity')
        records=[x for x in p.get('native_files',[]) if x.get('logical_file')=='native/'+LOCAL_NAME]
        if len(records)!=1:raise ValueError('one complete5970 native receipt is required')
        native=self.exact_native(root,'native/'+LOCAL_NAME,p,records[0]['sha256']);d=read(native)
        child=any(c.get('label')=='exact_all5970_same_F_matrix_cover_without_original_cell_recomputation'
            and c.get('actual_returncode')==0 for c in p.get('children',[]))
        reused=(p.get('original_complete_success_reused_without_child') and p.get('original_success_process_sha256'))
        if (not (child or reused) or not d.get('complete') or d.get('failure')
            or d.get('kind')!=LOCAL_KIND or d.get('source_sha256')!=LOCAL_SOURCE
            or d.get('exact_plan_native_sha256')!=PLAN or len(d.get('rows',[]))!=5970
            or d.get('reused_successful_pilot_cells')!=4 or d.get('complete_new_canonical_matrix_cells')!=5966
            or d.get('original_successful_matrix_cells_recomputed')!=0
            or not d.get('gates') or not all(g['passed'] for g in d['gates'])):
            raise ValueError('the actual complete5970 same-F mathematical cover is not proved')
        self.record_process(pp,'original-complete5970-matrix-process.json')
        return {'matrix-data':native,'matrix-process':pp},d

    def inputs(self):
        inputs,data=self.matrix_inputs()
        root=self.download(43594139132,'visible-exact-complete-5970-projectors-43594139132-1')
        pp=root/'process.json';p=read(pp)
        if digest(pp)!=PROFILE_PROCESS:raise ValueError('the exact original complete projector process changed')
        profile=self.exact_native(root,'native/complete-5970-local-projectors.json.gz',p,PROFILE)
        inputs.update(profile=profile,**{'profile-process':pp})
        self.record_process(pp,'original-complete5970-projector-process.json')
        self.args.green_artifact=self.download(43601964129,'visible-exact-complete-cut-Green-complete-43601964129-1')
        self.args.kernel_artifact=self.download(43633074696,'visible-exact-finite193-L2-Green-kernel-43633074696-1')
        inputs.update(ImpulseWorker.inputs(self))
        root=self.download(43649423561,'visible-exact-cached-interface-impulse-43649423561-1')
        pp=root/'process.json';p=read(pp)
        impulse=self.exact_native(root,'native/complete-all5970-cached-interface-impulse-gains.json.gz',p,IMPULSE)
        inputs.update(impulse=impulse,**{'impulse-process':pp,
            'reviewed-impulse-process':self.science/IMPULSE_REVIEW})
        self.record_process(pp,'original-all5970-impulse-artifact-process.json')
        root=self.download(43594139132,'visible-exact-cut-projector-prepared-43594139132-1')
        pp=root/'process.json';p=read(pp)
        if p.get('weighted_boundary_native_sha256')!=BOUNDARY or not p.get('complete_weighted_boundaries_verified'):
            raise ValueError('the actual original complete97 boundary preparation changed')
        boundary=self.exact_native(root,'native/complete-true-weighted-boundaries.json.gz',p,BOUNDARY)
        inputs.update(boundary=boundary,**{'nominal-cut':self.science/CUT})
        self.record_process(pp,'original-complete97-weighted-boundary-process.json')
        return inputs,data

    def math_success(self,p,d,phase):
        child=any(c.get('label')==LABELS[phase] and c.get('actual_returncode')==0
            for c in p.get('children',[]))
        reused=(p.get('original_complete_success_reused_without_child')
                and p.get('original_success_process_sha256'))
        return bool((child or reused) and d.get('complete') and not d.get('failure')
            and d.get('completed_rows')==5970 and d.get('gates')
            and all(g.get('passed') for g in d['gates'])
            and (phase=='backward' or d.get('complete_finite193_directional_two_boundary_bound_proved')))

    def staged_sweep(self,root,p,header,target):
        """Restore header and every exact referenced chunk into one directory."""
        d=read(header);target.mkdir(parents=True,exist_ok=True)
        name=native_name(d['phase']);out=target/name
        if out.resolve()!=header.resolve():shutil.copyfile(header,out)
        count=0
        for entry in d.get('row_chunks',[]):
            file=entry['file']
            if Path(file).name!=file or entry['first_row']!=count or not 0<entry['rows']<=32:
                raise ValueError('an original sweep chunk is not a consecutive ordinary basename')
            source=self.exact_native(root,'native/'+file,p,entry['sha256'])
            if source.stat().st_size!=entry['bytes']:
                raise ValueError('one original sweep chunk has changed size')
            content=read(source)
            if (content.get('kind')!=KIND or content.get('phase')!=d['phase']
                or content.get('source_sha256')!=self.manifest['files'][PRODUCER]
                or content.get('first_row')!=count or len(content.get('rows',[]))!=entry['rows']
                or any(not row.get('complete') for row in content['rows'])):
                raise ValueError('one sweep chunk lost its complete scientific rows')
            expected=[i if d['phase']=='backward' else 5969-i for i in range(count,count+entry['rows'])]
            if [r.get('index') for r in content['rows']]!=expected:
                raise ValueError('one original sweep prefix has a gap or reorder')
            destination=target/file
            if destination.resolve()!=source.resolve():shutil.copyfile(source,destination)
            count+=entry['rows']
        if count!=d.get('completed_rows') or count>5970:
            raise ValueError('one sweep header has the wrong exact complete prefix count')
        return out

    def previous(self,input_sha,backward_sha):
        root=TOPIC/FOLDER;candidates=[]
        if not root.exists():return None
        for pp in sorted(root.glob('*/process.json')):
            p=read(pp)
            if (p.get('repository')!=REPOSITORY or p.get('phase')!=self.args.phase
                or p.get('worker_source_sha256')!=digest(__file__)
                or p.get('input_manifest_sha256')!=self.args.manifest_sha
                or p.get('actual_input_sha256')!=input_sha
                or p.get('backward_native_sha256')!=backward_sha):continue
            records=[x for x in p.get('native_files',[]) if x.get('logical_file')=='native/'+self.native_name]
            if len(records)!=1:continue
            native=self.exact_native(pp.parent,'native/'+self.native_name,p,records[0]['sha256'])
            d=read(native)
            if (d.get('kind')!=KIND or d.get('phase')!=self.args.phase
                or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
                or d.get('input_sha256')!=input_sha or d.get('backward_native_sha256')!=backward_sha):
                continue
            if not 0<=d.get('completed_rows',-1)<=5970:
                raise ValueError('one matching scientific prefix has an impossible count')
            complete=self.math_success(p,d,self.args.phase)
            candidates.append(((int(complete),d['completed_rows']),pp,native,complete))
        return max(candidates,key=lambda x:x[0]) if candidates else None

    def backward_input(self,input_sha):
        if self.args.phase!='forward':return None
        run=self.args.backward_run;attempt=self.args.backward_attempt
        if not run or not attempt:raise ValueError('the actual complete backward run and attempt are required')
        root=self.download(run,f'visible-exact-directional-matrix-Green-backward-{run}-{attempt}')
        pp=root/'process.json';p=read(pp)
        if (p.get('phase')!='backward' or str(p.get('run_attempt'))!=str(attempt)
            or p.get('worker_source_sha256')!=digest(__file__)
            or p.get('input_manifest_sha256')!=self.args.manifest_sha
            or p.get('actual_input_sha256')!=input_sha):
            raise ValueError('the actual complete backward sweep has another exact identity')
        name=native_name('backward')
        records=[x for x in p.get('native_files',[]) if x.get('logical_file')=='native/'+name]
        if len(records)!=1:raise ValueError('one actual backward native receipt is required')
        native=self.exact_native(root,'native/'+name,p,records[0]['sha256']);d=read(native)
        if (d.get('kind')!=KIND or d.get('phase')!='backward'
            or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or d.get('input_sha256')!=input_sha or not self.math_success(p,d,'backward')):
            raise ValueError('the complete successful backward mathematical sweep is required')
        self.record_process(pp,'original-complete-backward-matrix-process.json')
        return self.staged_sweep(root,p,native,self.work/'complete-backward-native')

    def all_sweep_rows(self,path):
        d=read(path);rows=[]
        for entry in d.get('row_chunks',[]):
            p=path.parent/entry['file']
            if digest(p)!=entry['sha256']:raise ValueError('a staged exact sweep chunk changed')
            rows.extend(read(p)['rows'])
        if len(rows)!=d.get('completed_rows'):raise ValueError('staged complete row count changed')
        return d,rows

    def matrix_arrays(self,data,backward,prefix,complete):
        if complete:return
        receipts=[]
        for row in data['rows']:
            receipts.append(row['array_receipt'])
            for name in ('left_frame_array_receipt','right_frame_array_receipt'):
                if name in row:receipts.append(row[name])
        if backward:
            _,rows=self.all_sweep_rows(backward)
            receipts.extend(row['array_receipt'] for row in rows)
        if prefix:
            header,rows=self.all_sweep_rows(prefix)
            if rows:receipts.append(rows[-1]['array_receipt'])
            if header.get('initial_waist_state'):
                receipts.append(header['initial_waist_state']['array_receipt'])
        grouped=defaultdict(dict)
        for r in receipts:
            origin=r['original_public_array_origin']
            if origin.get('repository')!=REPOSITORY or origin.get('folder','matrices')!='matrices':
                raise ValueError('a matrix or covariance array has an unauthorized origin')
            run,name=str(origin['run_id']),origin['artifact']
            if Path(name).name!=name or Path(r['file']).name!=r['file']:
                raise ValueError('a scientific array has an unsafe original basename')
            key=(run,name)
            old=grouped[key].get(r['file'])
            if old and old!=r:raise ValueError('one original array basename has conflicting exact receipts')
            grouped[key][r['file']]=r
        self.state['required_original_array_artifacts']=len(grouped)
        self.state['required_original_array_files']=sum(map(len,grouped.values()))
        checked=0
        for (run,name),entries in sorted(grouped.items()):
            root=self.download(run,name,arrays_only=True)
            p=read(root/'process.json')
            for file,r in entries.items():
                origin=r['original_public_array_origin']
                if str(p.get('run_attempt'))!=str(origin['run_attempt']):
                    raise ValueError('one original matrix array belongs to another actual attempt')
                path=root/'matrices'/file
                if (not path.exists() or path.stat().st_size!=r['bytes'] or digest(path)!=r['sha256']):
                    raise ValueError('one original full matrix/covariance file changed or is absent')
                checked+=1;self.pull_during_download()
            small(self.evidence/'original-array-availability'/f"{self.artifact_metadata(run,name)['id']}.json",
                dict(repository=REPOSITORY,run_id=run,artifact=name,
                     actual_process_sha256=digest(root/'process.json'),
                     complete_verified_files=len(entries),
                     exact_original_array_receipts_in_native=True,
                     selected_file_sha256=[dict(file=k,sha256=v['sha256'],bytes=v['bytes'])
                         for k,v in list(sorted(entries.items()))[:8]],
                     all_files_verified_not_only_evidence_selection=True))
        self.state['all_original_array_files_verified']=checked
        self.state['original_array_data_recomputed']=0

    def outcome(self,d):
        result={k:d.get(k) for k in ('kind','phase','complete','failure','gates','seconds',
            'completed_rows','actual_progress','reused_complete_rows','new_covariance_rows',
            'new_forward_covariance_rows','complete_true_finite193_body_high_to_low_bounds',
            'complete_finite193_directional_two_boundary_bound_proved',
            'full_cap_infinite_high_trace_input_still_independent',
            'negative_high_BVP_inverse_and_full_low_high_Schur_still_required',
            'complete_infinite_BVP_inverse_proved','true_parameter_Schur_proved')}
        result['complete_saved_native_chunks']=len(d.get('row_chunks',[]))
        result['all_old_F_C_Grams_targets_and_ports_recomputed']=0
        return result

    def snapshot(self):
        # The same lock is held while the mathematical child commits a
        # complete row's chunk and header. Snapshot never interrupts or
        # changes mathematical data and cannot read mixed generations.
        with (self.cache/'checkpoint.lock').open('a') as checkpoint:
            fcntl.flock(checkpoint.fileno(),fcntl.LOCK_SH)
            native=self.cache/self.native_name
            if native.exists():
                d=read(native);brief=self.outcome(d)
                brief['native_sha256']=digest(native)
                brief['actual_process_context']=dict(repository=REPOSITORY,run_id=self.state.get('run_id'),
                    run_attempt=self.state.get('run_attempt'),worker_source_sha256=digest(__file__),
                    input_manifest_sha256=self.args.manifest_sha,
                    actual_readme_check_count=len(self.state.get('readme_checks',[])),
                    latest_actual_readme_check=self.state.get('readme_checks',[])[-1:] or None,
                    actual_child_returns=[dict(label=c['label'],actual_returncode=c.get('actual_returncode'))
                        for c in self.state.get('children',[])])
                small(self.evidence/'actual-latest-matrix-Green-outcome.json',brief)
                self.state['actual_completed_directional_rows']=d.get('completed_rows',0)
                self.state['latest_scientific_native_sha256']=brief['native_sha256']
            super().snapshot()

    def execute(self,label,command):
        try:return super().execute(label,command)
        finally:
            native=self.cache/self.native_name
            if native.exists():
                d=read(native);brief=self.outcome(d);brief['native_sha256']=digest(native)
                small(self.evidence/'actual-latest-matrix-Green-outcome.json',brief)
                print(json.dumps(brief),flush=True)
                if d.get('failure') and self.log.exists():print(self.log.read_text()[-16000:],flush=True)

    def prepare(self):
        inputs,data=self.inputs()
        input_sha={k:digest(v) for k,v in inputs.items()}
        self.state['actual_input_sha256']=input_sha
        backward=self.backward_input(input_sha)
        backward_sha=digest(backward) if backward else None
        self.state['backward_native_sha256']=backward_sha
        previous=self.previous(input_sha,backward_sha)
        prefix=None;native=self.cache/self.native_name
        if previous:
            _,pp,path,complete=previous;p=read(pp)
            prefix=self.staged_sweep(pp.parent,p,path,self.work/'original-exact-sweep-prefix')
            self.record_process(pp,'original-same-identity-matrix-Green-process.json')
            old=read(prefix)
            small(self.evidence/'original-matrix-Green-prefix-reuse.json',
                dict(original_process_sha256=digest(pp),original_native_sha256=digest(path),
                    original_process_complete=p.get('complete'),original_math_complete=complete,
                    original_actual_complete_rows=old.get('completed_rows'),
                    original_failure_preserved=old.get('failure'),
                    successful_mathematics_not_recomputed_after_publication_failure=True))
            if complete:
                self.staged_sweep(pp.parent,p,path,self.cache)
                self.reused_complete=True
                self.state['original_success_process_sha256']=digest(pp)
        self.matrix_arrays(data,backward,prefix,self.reused_complete)
        command=[sys.executable,'-u',str(self.science/PRODUCER),
            '--phase',self.args.phase,'--matrix-run',str(self.args.matrix_run),
            '--array-root',str(self.array_root),'--arrays',str(self.new_arrays),'--out',str(native)]
        for key,path in inputs.items():command+=['--'+key,str(path)]
        if backward:command+=['--backward',str(backward)]
        if prefix and not self.reused_complete:command+=['--resume',str(prefix)]
        self.publish()
        if not self.reused_complete:self.execute(LABELS[self.args.phase],command)
        d=read(native)
        if (d.get('kind')!=KIND or d.get('phase')!=self.args.phase
            or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or d.get('input_sha256')!=input_sha or d.get('backward_native_sha256')!=backward_sha
            or d.get('completed_rows')!=5970 or not d.get('complete') or d.get('failure')
            or not d.get('gates') or not all(g['passed'] for g in d['gates'])
            or d.get('complete_infinite_BVP_inverse_proved') or d.get('true_parameter_Schur_proved')):
            raise ValueError('the complete directional matrix sweep did not pass its exact scope')
        if self.args.phase=='forward' and not d.get('complete_finite193_directional_two_boundary_bound_proved'):
            raise ValueError('the actual forward sweep did not prove its complete finite193 directional bound')
        brief=self.outcome(d)
        brief.update(native_sha256=digest(native),exact_input_sha256=input_sha,
            original_complete_success_reused_without_child=self.reused_complete,
            actual_new_directional_rows_this_child=0 if self.reused_complete else
                d.get('new_covariance_rows',d.get('new_forward_covariance_rows')),
            original_full_scientific_native_chunks_retained=True,
            all_matrix_array_origins_remain_original_public_Actions_artifacts=True)
        small(self.evidence/f'complete-directional-matrix-Green-{self.args.phase}-summary.json',brief)
        if self.args.phase=='forward':
            for channel,content in d['complete_directional_posterior_components'].items():
                small(self.evidence/f'complete-posterior-channel-{channel}.json',
                    dict(complete_native_sha256=digest(native),channel=channel,**content))
            small(self.evidence/'complete-true-posterior-Green-and-cut-trace-constants.json',
                dict(complete_native_sha256=digest(native),
                    actual_constants=d['posterior_complete_true_Green_constants'],
                    separate_cut_trace_proof=d['new_cut_jump_trace_proof'],
                    original_complete97_boundary_has_independent_mean=True,
                    full_infinite_high_cut_input_remains_separate=True))
        self.state.update(complete=True,complete_native_sha256=digest(native),
            actual_scientific_gates=len(d['gates']),actual_completed_directional_rows=5970,
            original_complete_success_reused_without_child=self.reused_complete,
            actual_new_directional_rows_this_child=brief['actual_new_directional_rows_this_child'],
            complete_finite193_directional_two_boundary_bound_proved=(
                self.args.phase=='forward' and d.get('complete_finite193_directional_two_boundary_bound_proved')),
            complete_true_finite193_body_high_to_low_bounds=d.get('complete_true_finite193_body_high_to_low_bounds'),
            complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--phase',choices=('backward','forward'),required=True)
    for name in ('manifest','rules','work','artifact-dir'):
        p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha','matrix-run','matrix-attempt'):
        p.add_argument('--'+name,required=True)
    p.add_argument('--backward-run');p.add_argument('--backward-attempt')
    p.add_argument('--compute-minutes',type=int,default=320)
    p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args()
    a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='complete-directional-matrix-Green';a.mode='prepare';a.first=0;a.end=5970
    a.recovery_manifest=None;a.recovery_sha=None
    worker=MatrixGreenWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):
        signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
