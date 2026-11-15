#!/usr/bin/env python3
"""Public exact97 cap posterior and optional true right-Poisson contraction."""
from __future__ import annotations
import argparse,hashlib,io,json,os,re,shutil,signal,stat,sys,urllib.error,urllib.request,zipfile
from collections import OrderedDict
from pathlib import Path
from fourfold_codazzi_complete_directional_matrix_Green_CI import MatrixGreenWorker,NoRedirect
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_cap128_CI_worker import read,digest
from fourfold_codazzi_phase_high7_CI_worker import TOPIC,REPO

REL='topics/visible-flex-exact-nearby/'
PUBLIC='Rogerhu12/math-research-public'
PRODUCER=REL+'scripts/fourfold_codazzi_complete_same97_cap_posterior.py'
FOLDER='notes/same97_cap_posterior_ci'
KIND='actual_complete_same97_cap_posterior_and_right_Poisson_contraction_v1'
LABELS=dict(cap='complete_same97_full_cap_posterior_matrices',
    compose='complete_same97_cap_times_true_right_Poisson_signed_Gram_contractions')
NATIVES=dict(cap='complete-same97-cap-posterior.json.gz',
    compose='complete-same97-cap-times-right-Poisson.json.gz')
ORIGINALS=dict(
    body=dict(prefix='visible-exact-complete-adjoint-Grams-finish',
        logical='native/complete7908-cap-adjoint-Grams-finish.json.gz'),
    boundary=dict(prefix='visible-exact-cap-adjoint-boundary-high-Grams',
        logical='native/complete97-true-cap-adjoint-boundary-and-high-Grams.json.gz'),
    poisson=dict(prefix='visible-exact-complete97-right-Poisson-Grams',
        logical='native/complete97-true-right-boundary-Poisson-Grams.json.gz'),
    cap=dict(prefix='visible-exact-same97-cap-posterior-cap',
        logical='native/'+NATIVES['cap']),
    compose=dict(prefix='visible-exact-same97-cap-posterior-compose',
        logical='native/'+NATIVES['compose']))
OLD_MANIFESTS=(
    (REL+'notes/2026-11-15-R133-complete7908-cap-adjoint-Gram-CI-inputs.json',
        'baf3a42869c52ac0158ec6aac709aebced64a06efda8a8ea6d52939da71f1df5',341),
    (REL+'notes/2026-11-15-R133-cap-adjoint-true-boundary-high-Gram-CI-inputs.json',
        'b753b78658c11326aadb0b70fab2be440c690b1f3ac78fabcac42ca799612465',341),
    (REL+'notes/2026-11-15-R133-complete97-right-Poisson-Gram-CI-inputs.json',
        '94e46b2262ce542eccf04e948eae29eee49d4e4bb62b80231afac48821a79181',238))


def small(path,value):
    raw=(json.dumps(value,ensure_ascii=False,indent=2)+'\n').encode()
    if len(raw)>60000:raise ValueError('one actual posterior evidence text exceeds60000 UTF8 bytes')
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(raw)


def relative(value):
    path=Path(value)
    if path.is_absolute() or '..' in path.parts:raise ValueError('one exact artifact member path is unsafe')
    return path


def artifact_name(role,run,attempt):
    return ORIGINALS[role]['prefix']+f'-{run}-{attempt}'


def array_receipts(role,d):
    if role=='body':return [d['complete_new_array_receipt']]
    if role=='boundary':return [s['array_receipt'] for s in d['stages']]
    if role=='poisson':return [d['complete_true97_Gram_array_receipt']]
    if role=='cap':return [d['complete_posterior_array_receipt']]
    if role=='compose':return [d['complete_contraction_array_receipt']]
    raise ValueError('an exact posterior input role is unknown')


class ActualRangeArchive(io.RawIOBase):
    """Read only original ZIP members, without copying old5970 row arrays.

    Every HTTP request verifies its exact Content-Range and body length.
    The token is used only to obtain the repository artifact redirect,
    and is never forwarded to the signed storage URL.
    """
    def __init__(self,worker,metadata):
        super().__init__();self.worker=worker;self.metadata=metadata
        self.position=0;self.size=None;self.cache=OrderedDict();self.downloaded=0
        self.url=self.signed_url();self.get_range(0,0)
        if self.size is None or self.size<=0:raise ValueError('the original archive has no positive exact length')

    def signed_url(self):
        token=os.environ['GITHUB_TOKEN']
        url=f"https://api.github.com/repos/{PUBLIC}/actions/artifacts/{self.metadata['id']}/zip"
        request=urllib.request.Request(url,headers={'Authorization':'Bearer '+token,
            'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'})
        opener=urllib.request.build_opener(NoRedirect)
        try:
            response=opener.open(request,timeout=90)
        except urllib.error.HTTPError as error:
            if error.code not in (301,302,303,307,308):raise
            target=error.headers.get('Location','')
            if not target.startswith('https://'):
                raise ValueError('the exact original artifact redirect is not HTTPS')
            return target
        else:
            response.close()
            raise ValueError('the original public artifact did not return the expected signed redirect')

    def get_range(self,start,end):
        for attempt in range(2):
            request=urllib.request.Request(self.url,headers={
                'Range':f'bytes={start}-{end}','Accept-Encoding':'identity'})
            try:
                with urllib.request.urlopen(request,timeout=90) as response:
                    if response.status!=206:
                        raise ValueError('the original archive server did not honor the exact byte range')
                    matched=re.fullmatch(r'bytes (\d+)-(\d+)/(\d+)',response.headers.get('Content-Range',''))
                    if not matched or tuple(map(int,matched.groups()[:2]))!=(start,end):
                        raise ValueError('the original archive returned a different exact range')
                    size=int(matched.group(3))
                    if self.size is not None and size!=self.size:
                        raise ValueError('the original archive length changed during selected extraction')
                    self.size=size;data=response.read(end-start+2)
                if len(data)!=end-start+1:raise ValueError('an original exact compressed range was truncated')
                self.downloaded+=len(data);self.worker.pull_during_download();return data
            except urllib.error.HTTPError as error:
                if attempt or error.code not in (401,403):raise
                self.url=self.signed_url()
        raise RuntimeError('the original archive range was not returned')

    def readable(self):return True
    def seekable(self):return True
    def tell(self):return self.position
    def seek(self,offset,whence=io.SEEK_SET):
        value=offset if whence==io.SEEK_SET else self.position+offset if whence==io.SEEK_CUR else self.size+offset
        if value<0:raise ValueError('a selected original archive seek is negative')
        self.position=int(value);return self.position

    def read(self,n=-1):
        if n is None or n<0:n=max(0,self.size-self.position)
        end=min(self.size,self.position+n);parts=[];block=1024*1024
        while self.position<end:
            first=self.position//block*block
            if first not in self.cache:
                self.cache[first]=self.get_range(first,min(self.size-1,first+block-1))
                if len(self.cache)>16:self.cache.popitem(last=False)
            self.cache.move_to_end(first);data=self.cache[first]
            stop=min(end,first+len(data));parts.append(data[self.position-first:stop-first]);self.position=stop
        return b''.join(parts)


class PosteriorWorker(MatrixGreenWorker):
    def __init__(self,a):
        super().__init__(a)
        self.name=f'run-{self.run_label}-same97-cap-posterior-{a.phase}'
        self.dest=TOPIC/FOLDER/self.name;self.native_name=NATIVES.get(a.phase,'actual-selection-no-mathematics.json.gz')
        self.state.update(kind='actual_public_same97_cap_posterior_and_Poisson_process_v1',
            worker_source_sha256=digest(__file__),phase=a.phase,
            original_targets_trials7908cells5970propagators_and_Grams_recomputed=0,
            complete_full_cap_high_to_low_bound_proved=False,
            complete_true_right_Poisson_contraction_proved=False,
            complete_infinite_BVP_inverse_proved=False,
            original_successful_math_reused_despite_publication_failure=True,
            original_inputs_are_selected_exact_artifact_members_not_new_mathematics=True)

    def check_inputs(self):
        ReviewedBodyWorker.check_inputs(self)
        if self.manifest.get('kind')!='complete_same97_cap_posterior_Poisson_public_inputs_v1':
            raise ValueError('the separate complete same-input97 posterior manifest is required')
        for path,expected,count in OLD_MANIFESTS:
            old=read(REPO/path)
            if (digest(REPO/path)!=expected or len(old.get('files',{}))!=count
                or any(self.manifest['files'].get(k)!=v for k,v in old['files'].items())):
                raise ValueError('one original complete body boundary or Poisson input pin changed')

    def evidence_process(self,path,name):
        raw=Path(path).read_bytes()
        if len(raw)<=60000:
            self.record_process(path,name);return
        # Keep the complete original native process as ONE unchanged member
        # of this Actions artifact. Do not divide or reencode it to bypass
        # the bounded plaintext publication rule.
        destination=self.artifact/'original-processes'/Path(name).name
        destination.parent.mkdir(parents=True,exist_ok=True)
        if destination.exists() and destination.read_bytes()!=raw:
            raise ValueError('one complete original process would be overwritten by different bytes')
        if not destination.exists():shutil.copyfile(path,destination)
        d=read(path)
        children=[{k:c.get(k) for k in ('label','actual_returncode','started_utc',
            'finished_utc','wall_seconds')} for c in d.get('children',[])]
        final_names={item['logical'] for item in ORIGINALS.values()}
        native=[item for item in d.get('native_files',[]) if item.get('logical_file') in final_names]
        checks=[]
        for item in d.get('readme_checks',[])[-2:]:
            diff=str(item.get('actual_diff',''))
            checks.append(dict(time=item.get('time'),before=item.get('before'),after=item.get('after'),
                changed=item.get('changed'),actual_diff_empty=diff=='',
                actual_diff_sha256=hashlib.sha256(diff.encode()).hexdigest(),
                separately_read_rules_commit=item.get('separately_read_rules_commit')))
        brief=dict(kind='bounded_summary_of_one_complete_unchanged_actual_artifact_process_v1',
            complete_original_process_sha256=hashlib.sha256(raw).hexdigest(),
            complete_original_process_bytes=len(raw),
            complete_original_file_in_this_Actions_artifact=str(destination.relative_to(self.artifact)),
            original_repository=d.get('repository'),original_run_id=d.get('run_id'),
            original_run_attempt=d.get('run_attempt'),original_workflow_commit=d.get('workflow_commit'),
            original_worker_source_sha256=d.get('worker_source_sha256'),
            original_input_manifest_sha256=d.get('input_manifest_sha256'),
            original_process_complete=d.get('complete'),original_phase=d.get('phase'),
            original_complete_native_sha256=d.get('complete_native_sha256'),
            actual_children=children,complete_final_native_receipts=native,
            original_native_receipt_count=len(d.get('native_files',[])),
            latest_actual_readme_checks=checks,last_read_commit=d.get('last_read_commit'),
            actual_scientific_gates=d.get('actual_scientific_gates'),
            original_failure_summary=str(d.get('failure'))[:4000],
            original_publication_failure_summary=str(d.get('publication_failure'))[:4000],
            full_process_not_split_recompressed_or_reencoded=True,
            original_artifact_and_this_artifact_retain_complete_original_bytes=True)
        small(self.evidence/(Path(name).stem+'-summary.json'),brief)

    def selected_input(self,role,run,attempt):
        name=artifact_name(role,run,attempt);metadata=self.artifact_metadata(run,name)
        root=self.input_root/name;root.mkdir(parents=True,exist_ok=True)
        marker=root/'actual-selected-input-receipt.json'
        logical=ORIGINALS[role]['logical']
        if not marker.exists():
            with ActualRangeArchive(self,metadata) as remote,zipfile.ZipFile(remote) as archive:
                infos={x.filename:x for x in archive.infolist()}
                if len(infos)!=len(archive.infolist()):raise ValueError('an original archive has duplicate member names')
                for item in archive.infolist():
                    relative(item.filename)
                    if stat.S_ISLNK(item.external_attr>>16):raise ValueError('an original artifact has a symbolic link')
                extracted=[]
                def extract(filename):
                    item=infos.get(filename)
                    if item is None or item.is_dir():raise ValueError('one exact original scientific member is absent')
                    if item.file_size>128*1024*1024:
                        raise ValueError('an expected small complete97 native or matrix member is unexpectedly large')
                    path=root/relative(filename);path.parent.mkdir(parents=True,exist_ok=True)
                    temporary=path.with_suffix(path.suffix+'.partial')
                    with archive.open(item) as source,temporary.open('wb') as out:
                        shutil.copyfileobj(source,out,8*1024*1024)
                    temporary.replace(path)
                    extracted.append(dict(file=filename,bytes=path.stat().st_size,sha256=digest(path)))
                    self.pull_during_download();return path
                pp=extract('process.json');p=read(pp)
                if (p.get('repository')!=PUBLIC or str(p.get('run_id'))!=str(run)
                    or str(p.get('run_attempt'))!=str(attempt)):
                    raise ValueError('one selected original process belongs to another public run')
                entries=[x for x in p.get('native_files',[]) if x.get('logical_file')==logical]
                if len(entries)!=1:raise ValueError('the actual original complete native has no unique SHA receipt')
                # These are full exact native bytes and any original lossless
                # parts; no old per-cell matrix arrays are fetched.
                for filename,item in infos.items():
                    if filename.startswith('native/') and not item.is_dir():extract(filename)
                native=self.exact_native(root,logical,p,entries[0]['sha256']);d=read(native)
                for receipt in array_receipts(role,d):
                    name0='matrices/'+str(relative(receipt['file']))
                    path=extract(name0)
                    if path.stat().st_size!=receipt['bytes'] or digest(path)!=receipt['sha256']:
                        raise ValueError('one actual complete final Gram archive differs from its exact receipt')
                value=dict(repository=PUBLIC,run_id=str(run),run_attempt=str(attempt),role=role,
                    artifact_name=name,artifact_id=metadata['id'],api_archive_bytes=metadata['size_in_bytes'],
                    actual_archive_length=remote.size,actual_HTTP_range_bytes=remote.downloaded,
                    complete_archive_downloaded_or_claimed_hashed=False,
                    actual_process_sha256=digest(pp),actual_native_sha256=digest(native),
                    exact_selected_files=extracted,old_per_cell_arrays_fetched=False)
            small(marker,value)
        audit=read(marker)
        if (audit.get('artifact_id')!=metadata['id'] or audit.get('role')!=role
            or audit.get('run_id')!=str(run) or audit.get('run_attempt')!=str(attempt)):
            raise ValueError('one staged original selected archive has changed identity')
        for item in audit['exact_selected_files']:
            path=root/relative(item['file'])
            if path.stat().st_size!=item['bytes'] or digest(path)!=item['sha256']:
                raise ValueError('one staged exact selected member changed after extraction')
        pp=root/'process.json';p=read(pp)
        native=self.exact_native(root,logical,p,audit['actual_native_sha256'])
        self.evidence_process(pp,'original-'+role+'-actual-artifact-process.json')
        small(self.evidence/('original-'+role+'-selected-input-receipt.json'),audit)
        return native,pp,root/'matrices'

    def select_inputs(self):
        # This mode verifies original artifact receipts only. It does not
        # launch a mathematical child or recalculate a single old Gram.
        scripts=self.science/REL/'scripts'
        sys.path.insert(0,str(scripts))
        import fourfold_codazzi_complete_same97_cap_posterior as science
        if digest(science.__file__)!=self.manifest['files'][PRODUCER]:
            raise ValueError('the exact receipt verifier is not the frozen posterior source')
        event=read(Path(os.environ['GITHUB_EVENT_PATH']));given=event.get('inputs') or {}
        roles=dict(
            body=('visible-exact complete7908 cap adjoint Grams',43665656138),
            boundary=('visible-exact true cap adjoint boundary and high Grams',43666716585),
            poisson=('visible-exact complete97 right Poisson Grams',None))
        recent=[]
        for page in range(1,5):
            data=self.api(f'/repos/{PUBLIC}/actions/runs?per_page=100&page={page}')
            entries=data.get('workflow_runs',[]);recent.extend(entries)
            if len(entries)<100:break
        selected={};rejected=[]
        for role,(workflow,fallback) in roles.items():
            requested=str(given.get(role+'_run') or '').strip()
            if requested and not requested.isdigit():raise ValueError('an explicit original run must be numeric')
            pool=[]
            if requested:pool.append(self.api(f'/repos/{PUBLIC}/actions/runs/{requested}'))
            else:
                parent=event.get('workflow_run') or {}
                if parent.get('name')==workflow:pool.append(parent)
                pool.extend(r for r in recent if r.get('name')==workflow and r.get('status')=='completed')
                if fallback:pool.append(self.api(f'/repos/{PUBLIC}/actions/runs/{fallback}'))
            seen=set()
            for original in pool:
                run=original.get('id');attempt=original.get('run_attempt',1)
                if run in seen:continue
                seen.add(run)
                if original.get('name')!=workflow or original.get('status')!='completed':continue
                # No workflow-conclusion gate: a complete child followed by
                # publication failure is a valid scientific input.
                checked=dict(gates=[])
                try:
                    native,process,folder=self.selected_input(role,run,attempt)
                    d,p=science.actual_native(role,native,process,run,attempt,checked)
                    if role=='body':
                        complete=(d.get('complete7908_adjoint_cover_proved')
                            and d.get('complete_quarter_count')==7908
                            and d.get('original_successful_pilot_quarters_reused')==4
                            and d.get('new_quarters_from_actual_ranges')==7904)
                    elif role=='boundary':
                        complete=(d.get('mathematical_certificate_for_true_endpoints_and_trial_high_output')
                            and d.get('completed_stages')==3
                            and [r.get('stage') for r in d.get('stages',[])]==['left','outer','high'])
                    else:
                        complete=(d.get('complete97_input_Poisson_Gram_bound_proved')
                            and d.get('true_complete_finite193_BVP_only') and d.get('completed_rows')==5970)
                    if not complete:raise ValueError('the required actual full mathematical scope is incomplete')
                    selected[role]=dict(run=run,attempt=attempt,
                        artifact=artifact_name(role,run,attempt),actual_native_sha256=digest(native),
                        actual_artifact_process_sha256=digest(process),
                        original_workflow_conclusion=original.get('conclusion'),
                        original_process_complete=p.get('complete'),
                        original_mathematical_gates=len(d['gates']),receipt_gates=checked['gates'],
                        exact_mathematical_complete=True,
                        original_worker_source_sha256=p['worker_source_sha256'],
                        original_input_manifest_sha256=p['input_manifest_sha256'])
                    break
                except Exception as error:
                    item=dict(role=role,run=run,attempt=attempt,
                        original_workflow_conclusion=original.get('conclusion'),
                        actual_receipt_gates=checked['gates'],selected=False,
                        reason_type=type(error).__name__,reason_summary=str(error)[:2000],
                        no_mathematical_child_started=True,no_failed_science_repeated=True)
                    small(self.evidence/f'not-selected-{role}-{run}-{attempt}.json',item)
                    rejected.append(dict(role=role,run=run,attempt=attempt,
                        receipt=f'not-selected-{role}-{run}-{attempt}.json'))
            if requested and role not in selected:
                raise ValueError('the explicitly requested artifact has no verified complete mathematics')
        ready='body' in selected and 'boundary' in selected
        values=dict(cap_ready=str(ready).lower(),poisson_ready=str('poisson' in selected).lower())
        for role in roles:
            values[role+'_run']=str(selected.get(role,{}).get('run',''))
            values[role+'_attempt']=str(selected.get(role,{}).get('attempt',''))
        with open(os.environ['GITHUB_OUTPUT'],'a') as out:
            for key,value in values.items():out.write(key+'='+value+'\n')
        result=dict(selected_actual_complete_mathematics=selected,
            rejected_original_artifact_receipts=rejected,cap_ready=ready,
            Poisson_ready='poisson' in selected,workflow_conclusion_not_a_mathematical_gate=True,
            exact_original_child_or_success_reuse_native_and_all_gates_required=True,
            only_original_receipts_consumed_no_mathematical_recalculation=True)
        small(self.evidence/'verified-actual-original-selection.json',result)
        self.state.update(complete=True,verified_actual_original_selection=result,
            no_mathematical_child_or_new_scientific_result=True,
            complete_full_cap_high_to_low_bound_proved=False,
            complete_true_right_Poisson_contraction_proved=False)
        print(json.dumps(result,indent=2),flush=True)

    def inputs(self):
        roles=('body','boundary') if self.args.phase=='cap' else ('cap','poisson')
        inputs={};arrays={}
        for role in roles:
            run=getattr(self.args,role+'_run');attempt=getattr(self.args,role+'_attempt')
            if not run or not attempt:raise ValueError('every selected exact input run and attempt is required')
            native,process,folder=self.selected_input(role,run,attempt)
            inputs[role]=native;inputs[role+'-process']=process;arrays[role+'-arrays']=folder
        return inputs,arrays

    def success(self,p,d,input_sha):
        child=any(c.get('label')==LABELS[self.args.phase] and c.get('actual_returncode')==0
            for c in p.get('children',[]))
        reused=p.get('original_complete_success_reused_without_child') and p.get('original_success_process_sha256')
        return bool((child or reused) and d.get('kind')==KIND
            and d.get('phase')==self.args.phase and d.get('source_sha256')==self.manifest['files'][PRODUCER]
            and d.get('complete') and not d.get('failure') and d.get('input_sha256')==input_sha
            and p.get('actual_input_sha256')==input_sha
            and d.get('gates') and all(g.get('passed') for g in d['gates'])
            and d.get('complete_full_cap_high_to_low_bound_proved')
            and (self.args.phase=='cap' or d.get('complete_true_right_Poisson_contraction_proved'))
            and not d.get('complete_infinite_BVP_inverse_proved') and not d.get('true_parameter_Schur_proved'))

    def previous(self,input_sha):
        root=TOPIC/FOLDER;candidates=[]
        if not root.exists():return None
        for pp in sorted(root.glob('*/process.json')):
            p=read(pp)
            if (p.get('repository')!=PUBLIC or p.get('worker_source_sha256')!=digest(__file__)
                or p.get('input_manifest_sha256')!=self.args.manifest_sha
                or p.get('phase')!=self.args.phase or p.get('actual_input_sha256')!=input_sha
                or str(p.get('run_id'))==str(self.state['run_id'])
                    and str(p.get('run_attempt'))==str(self.state['run_attempt'])):continue
            entries=[x for x in p.get('native_files',[]) if
                x.get('logical_file')=='native/'+self.native_name]
            if len(entries)!=1:continue
            native=self.exact_native(pp.parent,'native/'+self.native_name,p,entries[0]['sha256']);d=read(native)
            if d.get('kind')!=KIND or d.get('source_sha256')!=self.manifest['files'][PRODUCER]:continue
            candidates.append((int(self.success(p,d,input_sha)),pp,native))
        return max(candidates,key=lambda x:x[0]) if candidates else None

    def reuse(self,previous,input_sha):
        _,rp,rn=previous;p0=read(rp);d0=read(rn)
        if d0.get('failure'):
            self.evidence_process(rp,'original-unchanged-failed-posterior-process.json')
            raise RuntimeError('preserve the genuine original posterior failure; no unchanged retry: '+str(d0['failure']))
        native,pp,arrays=self.selected_input(self.args.phase,p0['run_id'],p0['run_attempt']);p=read(pp);d=read(native)
        if (p.get('worker_source_sha256')!=digest(__file__)
            or p.get('input_manifest_sha256')!=self.args.manifest_sha
            or d.get('input_sha256')!=input_sha or not self.success(p,d,input_sha)):
            raise ValueError('the actual original posterior result is not the same complete mathematics')
        for receipt in array_receipts(self.args.phase,d):
            source=arrays/relative(receipt['file']);target=self.new_arrays/relative(receipt['file'])
            if target.exists() and digest(target)!=receipt['sha256']:
                raise ValueError('one exact completed posterior matrix would be overwritten')
            if not target.exists():shutil.copyfile(source,target)
        shutil.copyfile(native,self.cache/self.native_name);self.reused_complete=True
        self.state.update(original_success_process_sha256=digest(pp),
            original_complete_success_reused_without_child=True)
        small(self.evidence/'same-mathematics-reuse.json',dict(
            actual_original_process_sha256=digest(pp),reviewed_original_process_sha256=digest(rp),
            original_native_sha256=digest(native),original_process_complete=p.get('complete'),
            original_mathematical_complete=True,
            successful_scientific_matrices_reused_without_recalculation=True))

    def outcome(self,d):
        value={k:d.get(k) for k in ('kind','phase','complete','failure','gates','seconds',
            'complete_same_repaired_centre_definition_sha256',
            'selected_complete_cap_candidate','complete_full_cap_high_to97_operator_upper',
            'complete_constants','all_internal_value_jumps_exactly_zero',
            'all_full_body_and_boundary_error_channels_retained',
            'complete_full_cap_high_to_low_bound_proved',
            'complete_true_right_Poisson_contraction_proved',
            'complete_infinite_BVP_inverse_proved','true_parameter_Schur_proved')}
        value['complete_cap_candidate_bounds']={name:{
            k:entry[k] for k in ('full_cap_operator_upper','signed_objective_trace_upper',
                'complete_body_choice','complete_Young_choice')}
            for name,entry in d.get('complete_cap_candidates',{}).items()}
        value['complete_directional_contractions']={name:dict(
            selected_complete_contraction=entry['selected_complete_contraction'],
            complete_operator_upper=entry['complete_operator_upper'])
            for name,entry in d.get('complete_same_input_directional_contractions',{}).items()}
        value['new_complete_array_receipt']=d.get('complete_posterior_array_receipt',
            d.get('complete_contraction_array_receipt'))
        return value

    def snapshot(self):
        native=self.cache/self.native_name
        if native.exists():
            d=read(native);value=self.outcome(d);value['native_sha256']=digest(native)
            value['latest_actual_readme_check']=self.state.get('readme_checks',[])[-1:]
            small(self.evidence/'actual-latest-same97-posterior-outcome.json',value)
        ReviewedBodyWorker.snapshot(self)

    def execute(self,label,command):
        try:return ReviewedBodyWorker.execute(self,label,command)
        finally:
            native=self.cache/self.native_name
            if native.exists():
                d=read(native);value=self.outcome(d);value['native_sha256']=digest(native)
                small(self.evidence/'actual-latest-same97-posterior-outcome.json',value)
                print(json.dumps(value),flush=True)
                if d.get('failure') and self.log.exists():print(self.log.read_text()[-16000:],flush=True)

    def prepare(self):
        if self.args.phase=='select':return self.select_inputs()
        inputs,arrays=self.inputs();input_sha={k:digest(v) for k,v in inputs.items()}
        self.state['actual_input_sha256']=input_sha
        previous=self.previous(input_sha)
        if previous:self.reuse(previous,input_sha)
        command=[sys.executable,'-u',str(self.science/PRODUCER),'--phase',self.args.phase,
            '--arrays',str(self.new_arrays),'--out',str(self.cache/self.native_name),
            '--consumer-worker-sha',digest(__file__),'--consumer-manifest-sha',self.args.manifest_sha]
        for key,path in dict(inputs,**arrays).items():command+=['--'+key,str(path)]
        roles=('body','boundary') if self.args.phase=='cap' else ('cap','poisson')
        for role in roles:
            command+=['--'+role+'-run',str(getattr(self.args,role+'_run')),
                '--'+role+'-attempt',str(getattr(self.args,role+'_attempt'))]
        self.publish()
        if not self.reused_complete:self.execute(LABELS[self.args.phase],command)
        d=read(self.cache/self.native_name)
        if self.reused_complete:self.state['original_complete_success_reused_without_child']=True
        if not self.success(self.state,d,input_sha):
            raise ValueError('the actual complete same-input97 posterior mathematical gates did not pass')
        value=self.outcome(d);value.update(native_sha256=digest(self.cache/self.native_name),
            actual_input_sha256=input_sha,original_complete_success_reused_without_child=self.reused_complete)
        small(self.evidence/('complete-same97-'+self.args.phase+'-summary.json'),value)
        for key,entry in d.get('complete_cap_candidates',{}).items():
            small(self.evidence/('complete-cap-'+key+'-certificate.json'),
                dict(native_sha256=digest(self.cache/self.native_name),candidate=key,**entry))
        for key,entry in d.get('complete_same_input_directional_contractions',{}).items():
            small(self.evidence/('complete-'+key+'-contraction-summary.json'),dict(
                native_sha256=digest(self.cache/self.native_name),window=key,
                selected_complete_contraction=entry['selected_complete_contraction'],
                complete_operator_upper=entry['complete_operator_upper'],
                actual_true97_Poisson_Gram=entry['actual_true97_Poisson_Gram'],
                all_complete_contraction_choices=entry['all_complete_contraction_choices']))
            for name,item in entry['complete_new_cap_candidates'].items():
                small(self.evidence/('complete-'+key+'-'+name+'-weights.json'),
                    dict(native_sha256=digest(self.cache/self.native_name),window=key,candidate=name,**item))
        self.state.update(complete=True,complete_native_sha256=digest(self.cache/self.native_name),
            actual_scientific_gates=len(d['gates']),original_complete_success_reused_without_child=self.reused_complete,
            complete_full_cap_high_to_low_bound_proved=True,
            complete_true_right_Poisson_contraction_proved=self.args.phase=='compose',
            complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','work','artifact-dir'):ap.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):ap.add_argument('--'+name,required=True)
    ap.add_argument('--phase',choices=('select','cap','compose'),required=True)
    for role in ('body','boundary','cap','poisson'):
        ap.add_argument('--'+role+'-run');ap.add_argument('--'+role+'-attempt',default='1')
    ap.add_argument('--compute-minutes',type=int,default=60)
    ap.add_argument('--checkpoint-minutes',type=int,default=10)
    a=ap.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='same97-cap-posterior-'+a.phase;a.mode='prepare';a.first=0;a.end=97
    a.matrix_run=None;a.matrix_attempt=None;a.recovery_manifest=None;a.recovery_sha=None
    worker=PosteriorWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):
        signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
