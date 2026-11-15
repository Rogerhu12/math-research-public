#!/usr/bin/env python3
"""Actual public true-boundary and complete high-output97 adjoint Grams."""
from __future__ import annotations
import argparse,gzip,hashlib,json,shutil,signal,sys
from pathlib import Path
from fourfold_codazzi_cap_adjoint_residual_Gram_CI import AdjointGramWorker
from fourfold_codazzi_complete_directional_matrix_Green_CI import MatrixGreenWorker
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_cap128_CI_worker import read,digest
from fourfold_codazzi_phase_high7_CI_worker import TOPIC,REPO

REL='topics/visible-flex-exact-nearby/'
PUBLIC='Rogerhu12/math-research-public'
PRODUCER=REL+'scripts/fourfold_codazzi_cap_adjoint_boundary_high_Grams.py'
CORE=REL+'scripts/fourfold_codazzi_cap_adjoint_residual_Gram_core.py'
NATIVE='complete97-true-cap-adjoint-boundary-and-high-Grams.json.gz'
KIND='actual_same97_adjoint_true_endpoints_and_complete_high_output_Grams_v1'
FOLDER='notes/cap_adjoint_boundary_high_Grams_ci'
LABEL='true_endpoints_complete97_Grams_and_all_infinite_high_trial_outputs'
OLD_MANIFEST=REL+'notes/2026-11-15-R133-complete97-ordinary-adjoint-Gram-pilot-CI-inputs.json'
OLD_SHA='467cd31f6d62b834d3a0cf07a1ef92efe1a2ef218e27d862140122c37a9ce71f'
PILOT_RUN=43664278200
PILOT_NAME='visible-exact-cap-adjoint-Gram-pilot-43664278200-1'
PILOT_NATIVE='eb58b97ae182cedf621c4ff122b421ffb844e3839266a6a7d6df86b9134d8cfb'
PILOT_WORKER='3f7c1f5862530cf13bda0a30466fc16998ef2a1f0f60ab97a8e5bc9506d81222'
REFERENCE=REL+'notes/2026-11-14-R133-final-physical-cap-linear-module-r09-v2-native.json.gz'
Q_NATIVE=REL+'notes/2026-11-13-R133-regular-r25over8-q256-long-ports-native.json.gz'


def small(path,value):
    raw=(json.dumps(value,ensure_ascii=False,indent=2)+'\n').encode()
    if len(raw)>60000:raise ValueError('one actual boundary/high evidence file exceeds60000 UTF8 bytes')
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(raw)


def artifact_name(run,attempt):
    return f'visible-exact-cap-adjoint-boundary-high-Grams-{run}-{attempt}'


class BoundaryHighWorker(AdjointGramWorker):
    def __init__(self,a):
        MatrixGreenWorker.__init__(self,a)
        self.name=f'run-{self.run_label}-cap-adjoint-boundary-high-Grams'
        self.dest=TOPIC/FOLDER/self.name;self.native_name=NATIVE
        self.state.update(kind='actual_public_true_cap_adjoint_boundary_and_high_Grams_process_v1',
            worker_source_sha256=digest(__file__),phase='true-boundary-and-high-Grams',
            original_adjoint_proposal_run=43662865692,original_successful_body_pilot_run=PILOT_RUN,
            original_target_evaluations=0,old_adjoint_proposal_recomputed=False,
            original_four_residual_Gram_quarters_recomputed=False,
            complete_full_cap_high_to_low_bound_proved=False,
            complete_infinite_BVP_inverse_proved=False,
            successful_scientific_stages_preserved_on_publication_failure=True)

    def check_inputs(self):
        ReviewedBodyWorker.check_inputs(self)
        if self.manifest.get('kind')!='same97_true_cap_adjoint_boundary_high_Grams_public_inputs_v1':
            raise ValueError('the separate true-endpoint/high Gram manifest is required')
        old=read(REPO/OLD_MANIFEST)
        if (digest(REPO/OLD_MANIFEST)!=OLD_SHA or len(old.get('files',{}))!=337
            or any(self.manifest['files'].get(k)!=v for k,v in old['files'].items())):
            raise ValueError('an original337 complete-input adjoint pin changed')

    def boundary_inputs(self):
        old,inputs,arrays=AdjointGramWorker.inputs(self)
        root=self.download(PILOT_RUN,PILOT_NAME);pp=root/'process.json';p=read(pp)
        native=self.exact_native(root,'native/complete97-ordinary-cap-adjoint-residual-Gram-pilot.json.gz',p,PILOT_NATIVE)
        d=read(native)
        if (p.get('worker_source_sha256')!=PILOT_WORKER or p.get('input_manifest_sha256')!=OLD_SHA
            or not d.get('complete') or d.get('failure') or len(d.get('gates',[]))!=9
            or not all(x.get('passed') for x in d['gates'])
            or not any(c.get('label')=='four_actual_closed_quarters_complete97_ordinary_adjoint_and_Hessian_Grams'
                and c.get('actual_returncode')==0 for c in p.get('children',[]))):
            raise ValueError('the original actually successful complete-input residual pilot is required')
        self.record_process(pp,'original-successful-four-quarter-pilot-process.json')
        inputs.update(pilot=native,**{'pilot-process':pp,'reference':self.science/REFERENCE,
            'q-native':self.science/Q_NATIVE})
        return old,inputs,arrays

    def success(self,p,d,input_sha):
        child=any(c.get('label')==LABEL and c.get('actual_returncode')==0 for c in p.get('children',[]))
        reused=bool(p.get('original_complete_success_reused_without_child') and p.get('original_success_process_sha256'))
        return bool((child or reused) and d.get('complete') and not d.get('failure')
            and d.get('kind')==KIND and d.get('source_sha256')==self.manifest['files'][PRODUCER]
            and d.get('core_source_sha256')==self.manifest['files'][CORE]
            and p.get('actual_input_sha256')==input_sha
            and [s.get('stage') for s in d.get('stages',[])]==['left','outer','high']
            and all(s.get('complete') for s in d['stages'])
            and d.get('gates') and all(g.get('passed') for g in d['gates'])
            and d.get('mathematical_certificate_for_true_endpoints_and_trial_high_output')
            and not d.get('complete_full_cap_high_to_low_bound_proved')
            and not d.get('complete_infinite_BVP_inverse_proved'))

    def previous(self,input_sha):
        root=TOPIC/FOLDER;candidates=[]
        if not root.exists():return None
        for pp in sorted(root.glob('*/process.json')):
            p=read(pp)
            if (p.get('repository')!=PUBLIC or p.get('worker_source_sha256')!=digest(__file__)
                or p.get('input_manifest_sha256')!=self.args.manifest_sha
                or p.get('actual_input_sha256')!=input_sha
                or str(p.get('run_id'))==str(self.state['run_id'])
                    and str(p.get('run_attempt'))==str(self.state['run_attempt'])):continue
            entries=[x for x in p.get('native_files',[]) if x.get('logical_file')=='native/'+NATIVE]
            if len(entries)!=1:continue
            native=self.exact_native(pp.parent,'native/'+NATIVE,p,entries[0]['sha256']);d=read(native)
            if d.get('kind')!=KIND or d.get('source_sha256')!=self.manifest['files'][PRODUCER]:continue
            candidates.append(((int(self.success(p,d,input_sha)),len(d.get('stages',[]))),pp,native))
        return max(candidates,key=lambda x:x[0]) if candidates else None

    def restore_previous(self,previous,input_sha):
        _,rp,rn=previous;p0=read(rp);run=p0['run_id'];attempt=p0['run_attempt']
        root=self.download(run,artifact_name(run,attempt));pp=root/'process.json';p=read(pp)
        if (p.get('worker_source_sha256')!=digest(__file__)
            or p.get('input_manifest_sha256')!=self.args.manifest_sha
            or p.get('actual_input_sha256')!=input_sha):
            raise ValueError('one exact previous endpoint/high calculation has another identity')
        entries=[x for x in p.get('native_files',[]) if x.get('logical_file')=='native/'+NATIVE]
        if len(entries)!=1:raise ValueError('the actual endpoint/high native has no exact receipt')
        native=self.exact_native(root,'native/'+NATIVE,p,entries[0]['sha256']);d=read(native)
        if (d.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or d.get('exact_identity')!=read(rn).get('exact_identity')):
            raise ValueError('the original successful endpoint/high mathematical identity changed')
        for stage in d.get('stages',[]):
            item=stage['array_receipt'];relative=Path(item['file'])
            if relative.is_absolute() or '..' in relative.parts:raise ValueError('an original exact Gram path is unsafe')
            source=root/'matrices'/relative;target=self.new_arrays/relative
            if source.stat().st_size!=item['bytes'] or digest(source)!=item['sha256']:
                raise ValueError('one original successful signed boundary/high Gram array changed')
            if target.exists() and digest(target)!=item['sha256']:
                raise ValueError('one original successful Gram array would be overwritten')
            if not target.exists():shutil.copyfile(source,target)
        self.record_process(pp,'original-boundary-high-artifact-process.json')
        self.record_process(rp,'original-boundary-high-reviewed-process.json')
        prefix=self.work/'original-boundary-high-successful-prefix.json.gz';shutil.copyfile(native,prefix)
        complete=self.success(p,d,input_sha)
        small(self.evidence/'original-boundary-high-prefix-reuse.json',dict(
            actual_original_process_sha256=digest(pp),reviewed_process_sha256=digest(rp),
            actual_original_native_sha256=digest(native),original_process_complete=p.get('complete'),
            mathematical_complete=complete,successful_stages=len(d.get('stages',[])),
            failure_preserved=d.get('failure'),publication_success_not_required_for_mathematical_reuse=True))
        if complete:
            shutil.copyfile(native,self.cache/NATIVE);self.reused_complete=True
            self.state['original_success_process_sha256']=digest(pp)
        elif d.get('failure'):
            raise RuntimeError('preserve this genuine failure and successful stages without unchanged repetition: '+str(d['failure']))
        return prefix

    def outcome(self,d):
        value={k:d.get(k) for k in ('kind','complete','failure','gates','seconds',
            'completed_stages','reused_completed_stages','exact_identity_sha256',
            'exact_true_endpoints','point_background_receipt','complete_constants',
            'original_trial_node_count','all_internal_exact_physical_value_jumps_zero',
            'original_one_sided_derivatives_remain_independent','original_intrinsic_target_calls',
            'mathematical_certificate_for_true_endpoints_and_trial_high_output',
            'body_ordinary_source_Gram_still_requires_all7908_actual_quarters',
            'unknown_high_operator_not_replaced_by_a_finite_output_cutoff',
            'complete_full_cap_high_to_low_bound_proved','complete_infinite_BVP_inverse_proved')}
        value['actual_complete_stages']=[dict(stage=s['stage'],complete=s['complete'],
            Gram_trace_uppers=s['complete_Gram_trace_uppers'],
            array_receipt=s['array_receipt'],seconds=s['seconds']) for s in d.get('stages',[])]
        return value

    def snapshot(self):
        native=self.cache/NATIVE
        if native.exists():
            raw=native.read_bytes();d=json.loads(gzip.decompress(raw));brief=self.outcome(d)
            brief['native_sha256']=hashlib.sha256(raw).hexdigest()
            brief['latest_actual_readme_check']=self.state.get('readme_checks',[])[-1:]
            small(self.evidence/'actual-latest-boundary-high-Grams-outcome.json',brief)
            self.state.update(actual_completed_stages=len(d.get('stages',[])),
                latest_scientific_native_sha256=brief['native_sha256'])
        ReviewedBodyWorker.snapshot(self)

    def execute(self,label,command):
        try:return ReviewedBodyWorker.execute(self,label,command)
        finally:
            native=self.cache/NATIVE
            if native.exists():
                d=read(native);brief=self.outcome(d);brief['native_sha256']=digest(native)
                small(self.evidence/'actual-latest-boundary-high-Grams-outcome.json',brief)
                print(json.dumps(brief),flush=True)
                if d.get('failure') and self.log.exists():print(self.log.read_text()[-16000:],flush=True)

    def prepare(self):
        old,inputs,arrays=self.boundary_inputs();input_sha={k:digest(v) for k,v in inputs.items()}
        self.state['actual_input_sha256']=input_sha
        index=self.work/'exact-original-boundary-high-inputs.json'
        small(index,dict(repository=PUBLIC,kind='cached_adjoint_trial_original_inputs_v1',
            files={k:dict(path=str(v),sha256=digest(v)) for k,v in old.items()}))
        prefix=None;previous=self.previous(input_sha)
        if previous:prefix=self.restore_previous(previous,input_sha)
        command=[sys.executable,'-u',str(self.science/PRODUCER),'--input-index',str(index),
            '--proposal-arrays',str(arrays),'--arrays',str(self.new_arrays),'--out',str(self.cache/NATIVE)]
        for key in ('proposal','proposal-process','pilot','pilot-process','local','background','reference','q-native'):
            command+=['--'+key,str(inputs[key])]
        if prefix and not self.reused_complete:command+=['--resume',str(prefix)]
        self.publish()
        if not self.reused_complete:self.execute(LABEL,command)
        d=read(self.cache/NATIVE)
        if self.reused_complete:self.state['original_complete_success_reused_without_child']=True
        if not self.success(self.state,d,input_sha):
            raise ValueError('the actual true-boundary/high mathematical gates did not all pass')
        brief=self.outcome(d);brief.update(native_sha256=digest(self.cache/NATIVE),
            actual_input_sha256=input_sha,original_complete_success_reused_without_child=self.reused_complete)
        small(self.evidence/'complete97-boundary-high-Grams-summary.json',brief)
        for stage in d['stages']:
            value=dict(stage=stage['stage'],complete=stage['complete'],
                Gram_trace_uppers=stage['complete_Gram_trace_uppers'],
                array_receipt=stage['array_receipt'],seconds=stage['seconds'])
            value['metadata']={k:v for k,v in stage['metadata'].items() if k!='full_alias_and_tail'}
            small(self.evidence/('complete-'+stage['stage']+'-Gram-summary.json'),value)
        self.state.update(complete=True,complete_native_sha256=digest(self.cache/NATIVE),
            actual_scientific_gates=len(d['gates']),actual_completed_stages=3,
            original_complete_success_reused_without_child=self.reused_complete,
            complete_true_boundary_and_infinite_trial_high_output_Grams_proved=True,
            complete_full_cap_high_to_low_bound_proved=False,
            complete_infinite_BVP_inverse_proved=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','work','artifact-dir'):p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--compute-minutes',type=int,default=170)
    p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='cap-adjoint-boundary-high-Grams';a.mode='prepare';a.phase='boundary-high'
    a.first=0;a.end=3;a.matrix_run=None;a.matrix_attempt=None;a.recovery_manifest=None;a.recovery_sha=None
    worker=BoundaryHighWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):
        signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
