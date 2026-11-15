#!/usr/bin/env python3
"""One ephemeral public run: exact old inputs, three streams, complete contraction.

Only script/parameter/run/output-hash receipts and true small conclusions
are committed. No new numerical array, native output, stdout archive or
Actions artifact is uploaded. Missing immutable old pins are restored
from one explicitly fixed pre-deletion public commit into scratch only.
"""
from __future__ import annotations
import argparse,hashlib,importlib.metadata,json,os,re,shutil,signal,subprocess,sys,time
from pathlib import Path
import fourfold_codazzi_complete_directional_matrix_Green_CI as original
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC,REPO,save,now

REL='topics/visible-flex-exact-nearby/'
PRODUCER=REL+'scripts/fourfold_codazzi_ephemeral_parallel_matrix_Green_Poisson.py'
FOLDER='notes/ephemeral_parallel_matrix_Green_Poisson_ci'
KIND='actual_ephemeral_parallel_finite193_Green_true97_Poisson_same97_cap_v1'
WORKER_KIND='actual_public_ephemeral_parallel_matrix_Green_Poisson_process_v1'
MANIFEST_KIND='ephemeral_parallel_matrix_Green_Poisson_public_inputs_v1'
OLD_MANIFEST=REL+'notes/2026-11-15-R133-complete-same97-cap-posterior-Poisson-CI-inputs.json'
OLD_MANIFEST_SHA='7473f7866cc7676124f0f95ce047b6316ec5a4156bed8452f3cbd1bfb257ae95'
PREDELETE='7c130fb94528de8f003a43e7049fb42768a64eec'
RULES=('README.md',REL+'README.md')
RULES_SHA='f2661bd5cf5cb006c1f78c64126b3ac065e6bc26a50790545ac443efb5e372bd'
REPOSITORY='Rogerhu12/math-research-public'
BACK_RUN='43672023585'
BACK_NAME='visible-exact-directional-matrix-Green-backward-43672023585-1'
BACK_ID=14146873569
BACK_ZIP='de4e8dbdde0e34f6cfbd00b643ed70544ddc55d5852e1654a400ec8d3eaf3773'
CAP_RUN='43671537267'
CAP_NAME='visible-exact-same97-cap-posterior-cap-43671537267-1'
CAP_ID=14144516627
CAP_ZIP='b8809594d2efeba92b510c1c78ba4b8155b62514f60475c806e2bf10ceae7957'
CAP_NATIVE='56efa27c6410caed656eb7e691de49283dfbd34d60e5b2c23c516b932c72dd99'
CAP_ARRAY='c500a1a96ae6eca76de7447effe225e0a11621b06090e2fbf2dce7ef325c3ec0'
LABEL='actual_ephemeral_missing_future_past_true97_Poisson_and_same97_contraction'
SOURCE_KEYS=('matrix-data','matrix-process','profile','profile-process','green','green-process',
    'kernel','kernel-process','impulse','impulse-process','reviewed-impulse-process',
    'boundary','nominal-cut')
WINDOWS=('whole_inner_body','fixed_complete_negative_phase_window','true_cut_trace')


def small(path,document):
    raw=(json.dumps(document,ensure_ascii=False,indent=2,allow_nan=False)+'\n').encode()
    if len(raw)>60000:raise ValueError('a genuine small conclusion exceeds60000 bytes; do not split its full data')
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_suffix(path.suffix+'.tmp');temporary.write_bytes(raw);os.replace(temporary,path)


def safe_relative(name):
    p=Path(name)
    if p.is_absolute() or '..' in p.parts or not name.startswith(REL):
        raise ValueError('only an exact topic-relative immutable input is authorized')
    return p


class EphemeralWorker(original.MatrixGreenWorker):
    def __init__(self,a):
        super().__init__(a)
        self.name=f'run-{self.run_label}-ephemeral-parallel-matrix-Green-Poisson'
        self.dest=TOPIC/FOLDER/self.name
        self.temp=self.work/'ephemeral-mathematics'
        self.final_native=self.work/'ephemeral-complete-Green-Poisson-cap.json.gz'
        self.hydrated=False;self.history_ready=False;self.summary=None
        self.source_receipts=[]
        self.state.update(kind=WORKER_KIND,worker_source_sha256=digest(__file__),
            phase='one_ephemeral_complete_consumer',
            historical_restore_commit=PREDELETE,
            new_recomputable_repository_data=False,new_Release_uploads=False,new_Actions_artifacts=False,
            actual_original_backwards_run=BACK_RUN,actual_original_cap_run=CAP_RUN,
            original_complete_scientific_rows_recomputed=0,new_arithmetic_bits=a.bits,
            maximum_compute_processes=4,actual_available_cpu_count=os.cpu_count(),conclusion_scope='finite193 and true97 Poisson; full high inverse remains separate')
        self.state.pop('new_array_storage',None)

    def ensure_history(self):
        if self.history_ready:return
        check=self.git(['cat-file','-e',PREDELETE+'^{commit}'],check=False)
        if check.returncode:self.git(['fetch','--filter=blob:none','--no-tags','--depth=1','origin',PREDELETE])
        if self.git(['cat-file','-e',PREDELETE+'^{commit}'],check=False).returncode:
            raise ValueError('the fixed public pre-deletion commit is unavailable')
        self.history_ready=True

    def restore_pins(self):
        self.science.mkdir(parents=True,exist_ok=True)
        receipts=[]
        for name,expected in sorted(self.manifest['files'].items()):
            relative=safe_relative(name);target=self.science/relative;current=REPO/relative
            target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists():
                if digest(target)!=expected:raise ValueError('an immutable temporary pin changed: '+name)
                source='existing_exact_temporary'
            elif current.is_file() and digest(current)==expected:
                shutil.copyfile(current,target);source='exact_current_public_checkout'
            else:
                # New scripts and current rule receipts cannot be substituted
                # by history. Only the exact original closure is eligible.
                if name in self.manifest['new_nonhistorical_files']:
                    raise ValueError('a new exact source or rule receipt is absent or changed: '+name)
                self.ensure_history()
                temporary=target.with_suffix(target.suffix+'.historical-tmp')
                with temporary.open('wb') as output:
                    result=subprocess.run(self.gitbase+['show',PREDELETE+':'+name],
                        cwd=REPO,env=self.env,stdout=output,stderr=subprocess.PIPE,timeout=180)
                if result.returncode:
                    temporary.unlink(missing_ok=True)
                    raise ValueError('one fixed historical public input is absent: '+name)
                if digest(temporary)!=expected:
                    temporary.unlink(missing_ok=True)
                    raise ValueError('one fixed historical public input has another SHA: '+name)
                os.replace(temporary,target);source='fixed_public_history'
            if digest(target)!=expected:raise ValueError('one temporary restored scientific pin changed')
            receipts.append(dict(path=name,sha256=expected,bytes=target.stat().st_size,source=source))
        self.source_receipts=receipts
        save(self.work/'exact-historical-hydration.json',dict(
            commit=PREDELETE,entries=receipts,restored_into_checkout=False,old_mathematics_executed=False))
        self.state['historical_hydration']=dict(
            fixed_public_commit=PREDELETE,exact_files=len(receipts),
            historical_files=sum(r['source']=='fixed_public_history' for r in receipts),
            full_temporary_receipt_sha256=digest(self.work/'exact-historical-hydration.json'),
            restored_into_checkout=False,old_mathematics_executed=False)
        self.hydrated=True

    def check_inputs(self):
        if digest(__file__)!=self.args.worker_sha:raise ValueError('the exact new worker changed')
        if digest(self.args.manifest)!=self.args.manifest_sha:raise ValueError('the new input manifest changed')
        if digest(self.args.rules)!=RULES_SHA or self.args.rules_sha!=RULES_SHA:
            raise ValueError('the currently read no-persistence rules receipt changed')
        self.manifest=read(self.args.manifest);self.reviewed=read(self.args.rules)
        if (self.manifest.get('kind')!=MANIFEST_KIND
            or self.manifest.get('repository')!=REPOSITORY
            or os.environ.get('GITHUB_REPOSITORY')!=REPOSITORY
            or self.manifest.get('historical_restore_commit')!=PREDELETE
            or self.manifest.get('new_recomputable_outputs_persisted') is not False):
            raise ValueError('the exact current public one-run policy is required')
        if digest(Path(original.__file__))!=self.manifest['files'][REL+'scripts/'+Path(original.__file__).name]:
            raise ValueError('the actually imported original CI worker changed')
        if self.args.driver_sha!=self.manifest['files'][REL+'scripts/fourfold_codazzi_reviewed_CI_resume.py']:
            raise ValueError('the original reviewed driver identity changed')
        for module in list(sys.modules.values()):
            filename=getattr(module,'__file__',None)
            if not filename:continue
            path=Path(filename).resolve()
            try:relative=str(path.relative_to(REPO))
            except ValueError:continue
            if relative in self.manifest['files'] and digest(path)!=self.manifest['files'][relative]:
                raise ValueError('one actually imported frozen infrastructure source changed: '+relative)
        actual_rules={p:digest(REPO/p) for p in RULES}
        if actual_rules!=self.reviewed['readme_sha256']:
            raise RuntimeError('new unread repository rules require their actual diff to be read and applied')
        versions={name:importlib.metadata.version(name) for name in self.manifest['packages']}
        if (versions!=self.manifest['packages']
            or '.'.join(map(str,sys.version_info[:3]))!=self.manifest['python_version']):
            raise ValueError('the pinned arithmetic runtime changed')
        if not self.hydrated:self.restore_pins()
        for name,expected in self.manifest['files'].items():
            if digest(self.science/safe_relative(name))!=expected:
                raise ValueError('the immutable scientific copy changed: '+name)
        old=read(self.science/OLD_MANIFEST)
        if (digest(self.science/OLD_MANIFEST)!=OLD_MANIFEST_SHA
            or len(old['files'])!=353
            or any(self.manifest['files'].get(k)!=v for k,v in old['files'].items())
            or set(self.manifest['files'])!=(set(old['files'])|{OLD_MANIFEST}|set(self.manifest['new_nonhistorical_files']))):
            raise ValueError('one original same97/Poisson/5970 closure pin changed')
        self.state.update(input_manifest_sha256=self.args.manifest_sha,
            package_versions=versions,python_version=sys.version,all_pinned_inputs_verified=True,
            immutable_scientific_copy=str(self.science),
            actual_reviewed_readme_sha256=actual_rules,
            explicit_readme_review_commit=self.reviewed['read_commit'])

    def science_copy(self):
        if not self.hydrated:raise ValueError('exact historical hydrate must precede science execution')
        self.check_inputs()

    def zip_download(self,metadata,path):
        actual=super().zip_download(metadata,path)
        expected=metadata.get('digest','')
        if (metadata.get('size_in_bytes')!=actual['bytes']
            or not expected.startswith('sha256:') or expected[7:]!=actual['sha256']):
            raise ValueError('an actual original artifact ZIP differs from GitHub metadata')
        fixed={BACK_ID:(286134725,BACK_ZIP),CAP_ID:(759122,CAP_ZIP)}
        if metadata['id'] in fixed and (actual['bytes'],actual['sha256'])!=fixed[metadata['id']]:
            raise ValueError('one explicitly fixed original complete ZIP changed')
        return actual

    def download(self,run,name,arrays_only=False):
        # Full extraction can also supply the original matrices. Reuse the
        # one actual ZIP instead of downloading the old failure a second time.
        if arrays_only:
            full=self.input_root/name
            marker=full/'actual-original-artifact-download.json'
            if marker.exists() and (full/'matrices').is_dir():
                recorded=read(marker);metadata=self.artifact_metadata(run,name)
                if (recorded.get('artifact_id')!=metadata['id'] or
                    str(recorded.get('run_id'))!=str(run) or recorded.get('arrays_only')):
                    raise ValueError('a complete original artifact alias changed identity')
                alias=self.array_root/name
                if alias.is_symlink():
                    if alias.resolve()!=full.resolve():raise ValueError('an existing exact array alias changed')
                elif alias.exists():raise ValueError('refuse to replace any original array directory')
                else:alias.symlink_to(full,target_is_directory=True)
                return alias
        return super().download(run,name,arrays_only=arrays_only)

    def original_prefix(self):
        root=self.download(BACK_RUN,BACK_NAME);meta=self.artifact_metadata(BACK_RUN,BACK_NAME)
        if meta['id']!=BACK_ID:raise ValueError('the unique actual rule-failure artifact changed')
        pp=root/'process.json';actual=read(pp)
        if (str(actual.get('run_id'))!=BACK_RUN or str(actual.get('run_attempt'))!='1'
            or actual.get('worker_source_sha256')!='3709858655e70ebe7bd334b4c1b0c070cdb8855ad31878a240229c4768b3e096'
            or actual.get('input_manifest_sha256')!='3350a96fbea47ee33bb09cb6602cb1e978e8ba00a034c7f735dfb60bade99910'
            or actual.get('failure',{}).get('type')!='RuntimeError'
            or actual.get('failure',{}).get('message')!='new unread repository rules need their actual diff read: README.md'):
            raise ValueError('the actual original stopping reason or scientific worker identity differs')
        logical='native/complete-directional-matrix-Green-backward.json.gz'
        matches=[x for x in actual.get('native_files',[]) if x.get('logical_file')==logical]
        if len(matches)!=1:raise ValueError('one exact native receipt of the stopped original sweep is required')
        header=self.exact_native(root,logical,actual,matches[0]['sha256'])
        staged=self.staged_sweep(root,actual,header,self.work/'exact-old-future-prefix')
        doc,rows=self.all_sweep_rows(staged)
        if (doc.get('complete') or doc.get('failure') or not 1658<=len(rows)<5970
            or not doc.get('gates') or not all(g['passed'] for g in doc['gates'])):
            raise ValueError('the old successful future prefix has another complete scope')
        self.state['exact_old_future_prefix']=dict(
            run_id=BACK_RUN,run_attempt='1',artifact_id=BACK_ID,original_zip_sha256=BACK_ZIP,
            native_sha256=digest(staged),process_sha256=digest(pp),
            actual_complete_rows=len(rows),old_successful_rows_recomputed=0,
            actual_original_failure=actual['failure'],actual_original_gates=doc['gates'],
            latest_original_readme_check=actual.get('readme_checks',[])[-1:] or None)
        self.record_process(pp,'original-rule-failure-process.json')
        self.publish()
        return staged,pp

    def original_cap(self):
        root=self.download(CAP_RUN,CAP_NAME);meta=self.artifact_metadata(CAP_RUN,CAP_NAME)
        if meta['id']!=CAP_ID:raise ValueError('the exact completed same97 cap artifact changed')
        pp=root/'process.json';actual=read(pp)
        native=self.exact_native(root,'native/complete-same97-cap-posterior.json.gz',actual,CAP_NATIVE)
        arrays=root/'matrices'/'complete-same97-full-cap-posterior-Grams.npz'
        if not arrays.is_file() or arrays.stat().st_size!=723262 or digest(arrays)!=CAP_ARRAY:
            raise ValueError('the original complete signed97 cap matrices changed')
        self.record_process(pp,'original-complete-same97-cap-process.json')
        self.state['exact_original_cap']=dict(run_id=CAP_RUN,artifact_id=CAP_ID,
            native_sha256=CAP_NATIVE,original_array_sha256=CAP_ARRAY,
            actual_process_sha256=digest(pp),original_rows_recomputed=0)
        return native,pp,root/'matrices'

    def small_progress(self):
        progress={}
        directory=self.temp/'progress'
        if directory.exists():
            for path in sorted(directory.glob('*.json')):
                d=read(path)
                progress[path.stem]={k:d.get(k) for k in
                    ('stage','actual_utc','completed_rows','reused_rows','new_rows','completed_groups',
                     'last_group','streams','complete_groups','queued_groups','consumer_processes',
                     'done','seconds','failure') if k in d}
                progress[path.stem]['original_temporary_receipt_sha256']=digest(path)
        return progress

    def summarize(self,d):
        result={k:d.get(k) for k in (
            'kind','source_sha256','complete','failure','gates','seconds','arithmetic_bits',
            'input_sha256','original_formula_sources','exact_original_future_prefix','actual_phase_output_hashes',
            'complete_true_finite193_body_high_to_low_bounds','complete_directional_posterior_components',
            'complete_true_right_Poisson_operator_upper','actual_true97_normalization',
            'exact_inner_interval','exact_negative_output_interval','exact_boundary_input_units',
            'old_future_rows_recomputed','old_target_F_C_Gram_or_validator_calls',
            'complete_finite193_directional_two_boundary_bound_proved',
            'complete97_input_Poisson_Gram_bound_proved',
            'complete_true_right_Poisson_contraction_proved',
            'independent_full_high_body_and_high_cut_inputs_retained',
            'complete_infinite_BVP_inverse_proved','true_parameter_Schur_proved',
            'new_recomputable_arrays_persisted')}
        result['output_sha256']=digest(self.final_native)
        result['output_bytes']=self.final_native.stat().st_size
        result['complete_same_input_directional_contractions']={
            w:dict(complete_operator_upper=r['complete_operator_upper'],
                selected_complete_contraction=r['selected_complete_contraction'],
                all_complete_contraction_choices={k:dict(operator_upper=v['operator_upper'],origin=v['origin'])
                    for k,v in r['all_complete_contraction_choices'].items()},
                signed_trace_before_final_upper=r['signed_trace_before_final_upper'])
            for w,r in d.get('complete_same_input_directional_contractions',{}).items()}
        result['actual_parallel_completion']={k:v for k,v in d.get('actual_parallel_completion',{}).items()
            if k!='streams'}
        result['actual_final_stream_counts']=self.small_progress()
        result['temporary_final_output_receipts']=[]
        for name in ('complete-true97-Poisson.json','complete-same97-contraction.json'):
            path=self.temp/name
            if path.exists():
                meta=read(path)
                result['temporary_final_output_receipts'].append(dict(
                    logical_file=name,sha256=digest(path),bytes=path.stat().st_size,
                    array_receipt=meta.get('arrays'),retained_after_job=False))
        return result

    def snapshot(self):
        self.dest.mkdir(parents=True,exist_ok=True)
        self.state.update(snapshot_utc=now(),wall_seconds=time.monotonic()-self.started,
            actual_temporary_progress=self.small_progress(),
            new_recomputable_repository_data=False,new_Release_uploads=False,new_Actions_artifacts=False)
        if self.final_native.exists():
            d=read(self.final_native);self.summary=self.summarize(d)
            self.state['actual_output_sha256']=digest(self.final_native)
            self.state['actual_scientific_complete']=bool(d.get('complete'))
            self.state['actual_scientific_failure']=d.get('failure')
            small(self.dest/'actual-conclusion-summary.json',self.summary)
        actual=dict(self.state)
        # Full original inputs/processes and temporary native outputs are
        # only in scratch. The concise publication contains no such bytes.
        actual['original_process_receipts']=[dict(file=p.name,bytes=p.stat().st_size,sha256=digest(p))
            for p in sorted(self.evidence.glob('*process.json')) if p.is_file()]
        actual['actual_original_artifact_archives']=[read(p)
            for p in sorted((self.evidence/'original-artifact-downloads').glob('*.json'))]
        actual['new_output_policy']='only scripts, parameters, run IDs, output SHA and true small conclusions; no new data artifact'
        small(self.dest/'process.json',actual)
        save(self.statusfile,self.state)

    def execute(self,label,command):
        item=dict(label=label,command=command,started_utc=now(),actual_returncode=None)
        self.state['children'].append(item);save(self.statusfile,self.state)
        began=time.monotonic()
        with self.log.open('ab') as stream:
            self.child=subprocess.Popen(command,cwd=self.science_topic,env=self.env,
                stdout=stream,stderr=subprocess.STDOUT,start_new_session=True)
            previous=time.monotonic()
            while self.child.poll() is None:
                if self.interrupted:
                    self.terminate_child('actual runner signal; new temporary outputs are not persisted');break
                if time.monotonic()-self.started>self.args.compute_minutes*60:
                    self.terminate_child('actual single public slot reached its limit; no false completion');break
                if time.monotonic()-previous>self.args.checkpoint_minutes*60:
                    self.publish();previous=time.monotonic()
                time.sleep(5)
        item.update(actual_returncode=self.child.returncode,wall_seconds=time.monotonic()-began,finished_utc=now())
        save(self.statusfile,self.state)
        if self.child.returncode:
            if self.log.exists():print(self.log.read_text(errors='replace')[-20000:],flush=True)
            raise RuntimeError(label+' actually returned '+str(self.child.returncode))
        self.publish()

    def prepare(self):
        inputs,data=self.inputs()
        backward,process=self.original_prefix()
        if read(process).get('actual_input_sha256')!={k:digest(inputs[k]) for k in SOURCE_KEYS}:
            raise ValueError('the old successful future prefix uses another exact input process snapshot')
        self.matrix_arrays(data,backward,None,False)
        native,cap_process,cap_arrays=self.original_cap()
        self.state['actual_input_sha256']={k:digest(v) for k,v in inputs.items()}
        self.state['actual_source_sha256']=self.manifest['files'][PRODUCER]
        self.publish()
        command=[sys.executable,'-u',str(self.science/PRODUCER),
            '--matrix-run',self.args.matrix_run,'--array-root',str(self.array_root),
            '--old-backward',str(backward),'--old-backward-process',str(process),
            '--cap',str(native),'--cap-process',str(cap_process),'--cap-arrays',str(cap_arrays),
            '--temp',str(self.temp),'--out',str(self.final_native),'--bits',str(self.args.bits)]
        for key in SOURCE_KEYS:command+=['--'+key,str(inputs[key])]
        self.execute(LABEL,command)
        d=read(self.final_native)
        if (d.get('kind')!=KIND or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or not d.get('complete') or d.get('failure')
            or not d.get('gates') or not all(g['passed'] for g in d['gates'])
            or not d.get('complete_finite193_directional_two_boundary_bound_proved')
            or not d.get('complete97_input_Poisson_Gram_bound_proved')
            or not d.get('complete_true_right_Poisson_contraction_proved')
            or d.get('complete_infinite_BVP_inverse_proved') or d.get('true_parameter_Schur_proved')
            or d.get('old_future_rows_recomputed')!=0
            or d.get('old_target_F_C_Gram_or_validator_calls')!=0):
            raise ValueError('the new full temporary calculation did not pass its declared exact scope')
        self.state.update(complete=True,actual_output_sha256=digest(self.final_native),
            actual_scientific_gates=len(d['gates']),actual_complete5970=True,
            actual_full_source_Poisson_and_cap_contraction=True,
            old_future_rows_recomputed=0,
            complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False)
        self.snapshot()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','work','artifact-dir'):
        parser.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha','worker-sha'):
        parser.add_argument('--'+name,required=True)
    parser.add_argument('--matrix-run',default='43654510038')
    parser.add_argument('--matrix-attempt',default='1')
    parser.add_argument('--bits',type=int,default=192)
    parser.add_argument('--compute-minutes',type=int,default=340)
    parser.add_argument('--checkpoint-minutes',type=int,default=10)
    a=parser.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    if a.matrix_run!='43654510038' or a.matrix_attempt!='1' or a.bits<192:
        raise ValueError('the exact old whole5970 matrix identity and directed precision floor are fixed')
    if not 1<=a.checkpoint_minutes<=10 or not 1<=a.compute_minutes<=345:
        raise ValueError('real pull checkpoints and one bounded public runner are required')
    a.phase='ephemeral';a.kind='ephemeral-parallel-matrix-Green-Poisson'
    a.mode='prepare';a.first=0;a.end=5970;a.recovery_manifest=None;a.recovery_sha=None
    worker=EphemeralWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
