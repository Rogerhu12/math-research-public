#!/usr/bin/env python3
"""Actual complete97 right-boundary Poisson Gram consumer and prefix recovery."""
from __future__ import annotations
import argparse,fcntl,json,shutil,signal,sys
from pathlib import Path
from fourfold_codazzi_complete_directional_matrix_Green_CI import MatrixGreenWorker
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC,REPO

REL='topics/visible-flex-exact-nearby/'
PRODUCER=REL+'scripts/fourfold_codazzi_complete97_right_Poisson_Grams.py'
FOLDER='notes/complete97_right_Poisson_Grams_ci'
NATIVE='complete97-true-right-boundary-Poisson-Grams.json.gz'
KIND='actual_complete97_right_boundary_Poisson_Grams_from_same_F_v1'
LABEL='all5970_complete97_true_right_Poisson_input_Grams_and_all_posterior_defects'
GLOBAL_SOURCE='9dca5868ed04b051aa10799978412a4b74644ae75dea748bcdc4159b3d47659d'
GLOBAL_WORKER='3709858655e70ebe7bd334b4c1b0c070cdb8855ad31878a240229c4768b3e096'
GLOBAL_MANIFEST='3350a96fbea47ee33bb09cb6602cb1e978e8ba00a034c7f735dfb60bade99910'
GLOBAL_KIND='actual_complete_direction_preserving_finite193_matrix_Green_v1'
GLOBAL_NATIVE='complete-directional-matrix-Green-forward.json.gz'


def small(path,d):
    raw=(json.dumps(d,ensure_ascii=False,indent=2)+'\n').encode()
    if len(raw)>60000:raise ValueError('one complete97 Poisson evidence file exceeds60000 UTF8 bytes')
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(raw)


class PoissonWorker(MatrixGreenWorker):
    def __init__(self,a):
        super().__init__(a)
        self.name=f'run-{self.run_label}-complete97-right-Poisson-Grams'
        self.dest=TOPIC/FOLDER/self.name;self.native_name=NATIVE
        self.state.update(kind='actual_public_complete97_right_Poisson_Gram_process_v1',
            worker_source_sha256=digest(__file__),phase='right-Poisson',
            original_directional_run=str(a.directional_run),
            original_directional_attempt=str(a.directional_attempt),
            complete_matrix_run=None,complete_matrix_attempt=None,
            original_matrix_run_will_be_read_from_actual_directional_process=True,
            complete97_input_Poisson_Gram_bound_proved=False,
            complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False)

    def check_inputs(self):
        ReviewedBodyWorker.check_inputs(self)
        if self.manifest.get('kind')!='complete97_right_Poisson_Gram_public_inputs_v1':
            raise ValueError('the separate complete97 right Poisson manifest is required')
        path=REPO/self.manifest['original_directional_manifest']
        old=read(path)
        if (digest(path)!=GLOBAL_MANIFEST
            or any(self.manifest['files'].get(k)!=v for k,v in old['files'].items())):
            raise ValueError('an original complete directional pin changed')

    def inputs(self):
        run=self.args.directional_run;attempt=self.args.directional_attempt
        root=self.download(run,f'visible-exact-directional-matrix-Green-forward-{run}-{attempt}')
        pp=root/'process.json';p=read(pp)
        if (p.get('repository')!='Rogerhu12/math-research-public'
            or str(p.get('run_attempt'))!=str(attempt)
            or p.get('phase')!='forward' or p.get('worker_source_sha256')!=GLOBAL_WORKER
            or p.get('input_manifest_sha256')!=GLOBAL_MANIFEST):
            raise ValueError('the complete directional process has another original identity')
        records=[x for x in p.get('native_files',[]) if x.get('logical_file')=='native/'+GLOBAL_NATIVE]
        if len(records)!=1:raise ValueError('one original complete directional native receipt is required')
        path=self.exact_native(root,'native/'+GLOBAL_NATIVE,p,records[0]['sha256']);d=read(path)
        if (d.get('kind')!=GLOBAL_KIND or d.get('phase')!='forward'
            or d.get('source_sha256')!=GLOBAL_SOURCE
            or not MatrixGreenWorker.math_success(self,p,d,'forward')
            or not d.get('complete_finite193_directional_two_boundary_bound_proved')):
            raise ValueError('the full actual successful direction-preserving finite193 result is required')
        matrix_run=str(p.get('complete_matrix_run'))
        matrix_attempt=str(p.get('complete_matrix_attempt'))
        if not matrix_run.isdigit() or not matrix_attempt.isdigit():
            raise ValueError('the actual directional process has no explicit original matrix run and attempt')
        self.args.matrix_run=matrix_run;self.args.matrix_attempt=matrix_attempt
        self.state.update(complete_matrix_run=matrix_run,complete_matrix_attempt=matrix_attempt,
            original_complete_directional_native_sha256=digest(path),
            original_complete_directional_process_sha256=digest(pp))
        inputs,data=MatrixGreenWorker.inputs(self)
        expected={k:digest(v) for k,v in inputs.items()}
        if d.get('input_sha256')!=expected:
            raise ValueError('the actual complete directional matrix result has another original input bundle')
        header=MatrixGreenWorker.staged_sweep(self,root,p,path,self.work/'original-complete-directional-native')
        self.record_process(pp,'original-complete-directional-forward-process.json')
        inputs.update(directional=header,**{'directional-process':pp})
        return inputs,data,header

    def mathematical_success(self,p,d):
        child=any(c.get('label')==LABEL and c.get('actual_returncode')==0 for c in p.get('children',[]))
        reused=(p.get('original_complete_success_reused_without_child')
                and p.get('original_success_process_sha256'))
        return bool((child or reused) and d.get('complete') and not d.get('failure')
            and d.get('completed_rows')==5970 and d.get('gates') and all(g['passed'] for g in d['gates'])
            and d.get('complete97_input_Poisson_Gram_bound_proved'))

    def previous(self,input_sha):
        root=TOPIC/FOLDER;candidates=[]
        if not root.exists():return None
        for pp in sorted(root.glob('*/process.json')):
            p=read(pp)
            if (p.get('repository')!='Rogerhu12/math-research-public'
                or p.get('worker_source_sha256')!=digest(__file__)
                or p.get('input_manifest_sha256')!=self.args.manifest_sha
                or p.get('actual_input_sha256')!=input_sha):continue
            records=[x for x in p.get('native_files',[]) if x.get('logical_file')=='native/'+NATIVE]
            if len(records)!=1:continue
            path=self.exact_native(pp.parent,'native/'+NATIVE,p,records[0]['sha256']);d=read(path)
            if (d.get('kind')!=KIND or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
                or d.get('input_sha256')!=input_sha):continue
            if not 0<=d.get('completed_rows',-1)<=5970:
                raise ValueError('a matching complete97 prefix has an impossible exact count')
            complete=self.mathematical_success(p,d)
            candidates.append(((int(complete),d['completed_rows']),pp,path,complete))
        return max(candidates,key=lambda x:x[0]) if candidates else None

    def stage_prefix(self,root,p,header,target):
        d=read(header);target.mkdir(parents=True,exist_ok=True)
        out=target/NATIVE
        if out.resolve()!=header.resolve():shutil.copyfile(header,out)
        count=0
        for entry in d.get('row_chunks',[]):
            name=entry['file']
            if Path(name).name!=name or entry['first_row']!=count or not 0<entry['rows']<=32:
                raise ValueError('one complete97 prefix chunk is not consecutive')
            path=self.exact_native(root,'native/'+name,p,entry['sha256']);chunk=read(path)
            rows=chunk.get('rows',[])
            if (path.stat().st_size!=entry['bytes'] or chunk.get('kind')!=KIND
                or chunk.get('source_sha256')!=self.manifest['files'][PRODUCER]
                or chunk.get('first_row')!=count or len(rows)!=entry['rows']
                or [r.get('index') for r in rows]!=list(range(count,count+len(rows)))
                or any(not r.get('complete') for r in rows)):
                raise ValueError('one original complete97 chunk lost its exact completed rows')
            destination=target/name
            if destination.resolve()!=path.resolve():shutil.copyfile(path,destination)
            count+=len(rows)
        if count!=d.get('completed_rows') or count>5970:
            raise ValueError('the exact complete97 prefix and header counts differ')
        return out

    def extra_prefix_arrays(self,prefix):
        if not prefix:return
        d=read(prefix);receipts=[]
        if d.get('initial_boundary_family'):receipts.append(d['initial_boundary_family']['array_receipt'])
        if d.get('latest_state'):receipts.append(d['latest_state']['array_receipt'])
        for receipt in receipts:
            source=receipt['original_public_array_origin']
            if source.get('repository')!='Rogerhu12/math-research-public' or source.get('folder','matrices')!='matrices':
                raise ValueError('a complete97 state has an unauthorized original array source')
            root=self.download(source['run_id'],source['artifact'],arrays_only=True)
            p=read(root/'process.json')
            if str(p.get('run_attempt'))!=str(source['run_attempt']):
                raise ValueError('the original complete97 state array belongs to another attempt')
            file=receipt['file']
            if Path(file).name!=file:raise ValueError('a complete97 array basename is unsafe')
            path=root/'matrices'/file
            if path.stat().st_size!=receipt['bytes'] or digest(path)!=receipt['sha256']:
                raise ValueError('one original complete97 state array changed')
        self.state['original_complete97_prefix_state_array_files_verified']=len(receipts)

    def outcome(self,d):
        out={k:d.get(k) for k in ('kind','complete','failure','gates','seconds','completed_rows','actual_progress',
            'reused_complete_rows','new_product_rows','complete_true_right_Poisson_operator_upper',
            'complete97_input_Poisson_Gram_bound_proved','true_complete_finite193_BVP_only',
            'complete_infinite_BVP_inverse_proved','exact_full_PDE_parameter_response_error_proved',
            'true_parameter_Schur_proved')}
        out.update(complete_native_chunks=len(d.get('row_chunks',[])),
            exact_immutable_chunk_end_states=len(d.get('immutable_chunk_end_states',[])),
            old_F_C_H_J_target_validator_and_positive_port_recomputations=0)
        return out

    def snapshot(self):
        with (self.cache/'checkpoint.lock').open('a') as handle:
            fcntl.flock(handle.fileno(),fcntl.LOCK_SH)
            native=self.cache/NATIVE
            if native.exists():
                d=read(native);brief=self.outcome(d);brief['native_sha256']=digest(native)
                brief['actual_process_context']=dict(repository='Rogerhu12/math-research-public',
                    run_id=self.state.get('run_id'),run_attempt=self.state.get('run_attempt'),
                    worker_source_sha256=digest(__file__),input_manifest_sha256=self.args.manifest_sha,
                    latest_actual_readme_check=self.state.get('readme_checks',[])[-1:] or None,
                    actual_child_returns=[dict(label=c['label'],actual_returncode=c.get('actual_returncode'))
                        for c in self.state.get('children',[])])
                small(self.evidence/'actual-latest-complete97-right-Poisson-outcome.json',brief)
                self.state['actual_complete97_rows']=d.get('completed_rows',0)
            ReviewedBodyWorker.snapshot(self)

    def execute(self,label,command):
        try:return ReviewedBodyWorker.execute(self,label,command)
        finally:
            native=self.cache/NATIVE
            if native.exists():
                d=read(native);brief=self.outcome(d);brief['native_sha256']=digest(native)
                small(self.evidence/'actual-latest-complete97-right-Poisson-outcome.json',brief)
                print(json.dumps(brief),flush=True)
                if d.get('failure') and self.log.exists():print(self.log.read_text()[-16000:],flush=True)


    def prepare(self):
        inputs,data,graph=self.inputs()
        input_sha={k:digest(v) for k,v in inputs.items()}
        self.state['actual_input_sha256']=input_sha
        previous=self.previous(input_sha)
        prefix=None;native=self.cache/NATIVE
        if previous:
            _,pp,path,complete=previous;p=read(pp)
            prefix=self.stage_prefix(pp.parent,p,path,self.work/'original-exact-right-Poisson-prefix')
            self.record_process(pp,'original-same-identity-right-Poisson-process.json')
            old=read(prefix)
            small(self.evidence/'original-right-Poisson-prefix-reuse.json',
                dict(original_process_sha256=digest(pp),original_native_sha256=digest(path),
                    original_process_complete=p.get('complete'),original_math_complete=complete,
                    original_actual_complete_rows=old.get('completed_rows'),
                    original_failure_preserved=old.get('failure'),
                    successful_mathematics_not_recomputed_after_publication_failure=True))
            if complete:
                self.stage_prefix(pp.parent,p,path,self.cache)
                self.reused_complete=True
                self.state['original_success_process_sha256']=digest(pp)
        if not self.reused_complete:
            # The global forward header is deliberately passed in both
            # positions: retain all complete V rows and its initial waist
            # family as well as every original local matrix/frame. The
            # Poisson prefix has a different schema and is restored below.
            MatrixGreenWorker.matrix_arrays(self,data,graph,graph,False)
            self.extra_prefix_arrays(prefix)
        command=[sys.executable,'-u',str(self.science/PRODUCER),
            '--matrix-run',str(self.args.matrix_run),'--directional-run',str(self.args.directional_run),
            '--array-root',str(self.array_root),'--arrays',str(self.new_arrays),'--out',str(native)]
        for key,path in inputs.items():command+=['--'+key,str(path)]
        if prefix and not self.reused_complete:command+=['--resume',str(prefix)]
        self.publish()
        if not self.reused_complete:self.execute(LABEL,command)
        d=read(native)
        if (d.get('kind')!=KIND or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or d.get('input_sha256')!=input_sha or d.get('completed_rows')!=5970
            or not d.get('complete') or d.get('failure')
            or not d.get('gates') or not all(g['passed'] for g in d['gates'])
            or not d.get('complete97_input_Poisson_Gram_bound_proved')
            or not d.get('true_complete_finite193_BVP_only')
            or d.get('complete_infinite_BVP_inverse_proved')
            or d.get('exact_full_PDE_parameter_response_error_proved')
            or d.get('true_parameter_Schur_proved')):
            raise ValueError('the full complete97 right Poisson mathematical result did not pass its exact scope')
        brief=self.outcome(d)
        brief.update(native_sha256=digest(native),exact_input_sha256=input_sha,
            original_complete_success_reused_without_child=self.reused_complete,
            actual_new_product_rows_this_child=0 if self.reused_complete else d.get('new_product_rows'),
            all_full_scientific_native_chunks_retained=True,
            all_output_matrix_receipts_retain_their_actual_original_public_artifact_origins=True)
        small(self.evidence/'complete97-true-right-Poisson-Gram-summary.json',brief)
        for window,content in d['complete_true_right_Poisson_Gram_certificates'].items():
            small(self.evidence/f'complete97-right-Poisson-{window}-certificate.json',
                dict(complete_native_sha256=digest(native),window=window,**content))
        small(self.evidence/'complete97-right-Poisson-final-matrix-receipt.json',
            dict(complete_native_sha256=digest(native),
                actual_complete_matrix_array=d['complete_true97_Gram_array_receipt'],
                actual_initial_boundary_family=d['initial_boundary_family'],
                all97_input_directions_and_independent_mean=True,
                all_correlated_defects_paid_by_positive_weighted_Cauchy=True,
                unknown_full_cap_high_input_map_requires_separate_proof=True))
        self.state.update(complete=True,complete_native_sha256=digest(native),
            actual_scientific_gates=len(d['gates']),actual_complete97_rows=5970,
            original_complete_success_reused_without_child=self.reused_complete,
            actual_new_product_rows_this_child=brief['actual_new_product_rows_this_child'],
            complete97_input_Poisson_Gram_bound_proved=True,
            complete_true_right_Poisson_operator_upper=d['complete_true_right_Poisson_operator_upper'],
            all_original_F_C_H_J_targets_validators_and_scalar_ports_recomputed=0,
            complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','work','artifact-dir'):
        p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha','directional-run','directional-attempt'):
        p.add_argument('--'+name,required=True)
    p.add_argument('--compute-minutes',type=int,default=320)
    p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args()
    a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.phase='right-Poisson';a.matrix_run=None;a.matrix_attempt=None
    a.kind='complete97-right-Poisson-Grams';a.mode='prepare';a.first=0;a.end=5970
    a.recovery_manifest=None;a.recovery_sha=None
    worker=PoissonWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):
        signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
