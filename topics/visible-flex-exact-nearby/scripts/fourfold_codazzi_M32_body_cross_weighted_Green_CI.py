#!/usr/bin/env python3
"""Consume frozen scalar coefficients and cached Green kernels for body feedback."""
from __future__ import annotations
import argparse,json,shutil,signal,sys
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_finite193_L2_Green_kernel_CI import KernelWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC

REL='topics/visible-flex-exact-nearby/'
PRODUCER=REL+'scripts/fourfold_codazzi_M32_body_cross_weighted_Green.py'
FOLDER='notes/M32_body_cross_weighted_Green_ci'
NATIVE='complete-M32-body-cross-and-weighted-Green.json.gz'
KIND='actual_fixed_M32_body_cross_bands_and_cached_weighted_L2_Green_v1'
LABEL='actual_M32_body_cross_fees_and_cached_weighted_Green'
KERNEL='ac4441cb98afabbbc646697434caebf464a22f702e2d0fa7d8e5910efd7ef448'
KERNEL_WORKER='368b9b0eb613fa7c508adcae6fb3fbd92193413ac879b1a7ab21d7721492f314'
KERNEL_MANIFEST='fb2336796edcd9ccc57a082015cdb6c51ee7c47a921ce03a3cbf3bbab6181ff6'
HIGH='5ad8aaada967f4626a33e978b1c81adf640ee1abaf0876f54ffd22d6dbd107fd'
HIGH_MANIFEST='de4bd52b27daceb5b3ea85a79c2ba37dd01196143384ffc72d0946dc6826a759'
RECEIPT='cd7aa5f5c21509c629f8508bef21af4254e05716e2868e1804bce60e1ee583fa'
RECEIPT_WORKER='74a00ec426b897222424ca6a9241d7aa1f2d3b9763529fa2fd6be31671caecee'
MATH_PROCESS='085a31c2f760df9076b0aa87672b05becaa1e699838bc14a71438c7592d38496'


def small(path,document):
    data=(json.dumps(document,ensure_ascii=False,indent=2)+'\n').encode()
    if len(data)>60000:raise ValueError('new body-feedback plaintext exceeds60000 bytes; full native retained')
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(data)


class FeedbackWorker(KernelWorker):
    def __init__(self,a):
        super().__init__(a)
        self.name=f'run-{self.run_label}-M32-body-cross-weighted-Green'
        self.dest=TOPIC/FOLDER/self.name
        self.state.update(kind='actual_public_fixed_M32_body_cross_weighted_Green_process_v1',
            worker_source_sha256=digest(__file__),
            original_complete_L2_kernel_run=43633074696,
            original_complete_scalar_receipt_run=43630093667,
            original_complete_scalar_mathematical_run=43628921664,
            original_6391_Gram_or_scalar_exponentials_recomputed=0,
            original_target_residual_mean_cap_or_trial_calculations=0,
            actual_full_PDE_response_error_proved=False,complete_infinite_BVP_inverse_proved=False,
            complete_body_only_weighted_Green_feedback_bound_proved=False,
            high_cut_trace_is_an_independent_input_not_bounded_by_body_L2=True)

    def check_inputs(self):
        ReviewedBodyWorker.check_inputs(self)
        if self.manifest.get('kind')!='fixed_M32_body_cross_and_cached_weighted_Green_public_inputs_v1':
            raise ValueError('the separate fixed-M32 body feedback manifest is required')

    def original_inputs(self):
        inputs=KernelWorker.original_inputs(self)
        root=self.args.kernel_artifact.resolve();pp=root/'process.json';p=read(pp)
        if (p.get('repository')!='Rogerhu12/math-research-public'
            or str(p.get('run_id'))!='43633074696' or str(p.get('run_attempt'))!='1'
            or not p.get('complete') or p.get('failure')
            or p.get('worker_source_sha256')!=KERNEL_WORKER
            or p.get('input_manifest_sha256')!=KERNEL_MANIFEST
            or p.get('complete_native_sha256')!=KERNEL
            or not p.get('complete_finite193_ordinary_L2_source_inverse_bound_proved')
            or not p.get('children') or any(c.get('actual_returncode')!=0 for c in p['children'])):
            raise ValueError('the actual completed original L2 kernel artifact is required')
        inputs['kernel']=self.exact_native(root,
            'native/complete-finite193-ordinary-L2-Green-kernel.json.gz',p,KERNEL)
        inputs['kernel-process']=pp
        shutil.copyfile(pp,self.evidence/'original-complete-L2-kernel-artifact-process.json')

        root=self.args.high_receipt_artifact.resolve();pp=root/'process.json';p=read(pp)
        rp=root/'evidence/known-high-original-success-receipt.json'
        mp=root/'evidence/original-math-success-publication-failure-process.json'
        if (p.get('repository')!='Rogerhu12/math-research-public'
            or str(p.get('run_id'))!='43630093667' or str(p.get('run_attempt'))!='1'
            or not p.get('complete') or p.get('failure')
            or p.get('kind')!='actual_public_known_high_success_receipt_without_new_mathematics_v1'
            or p.get('worker_source_sha256')!=RECEIPT_WORKER
            or p.get('input_manifest_sha256')!=HIGH_MANIFEST
            or p.get('complete_native_sha256')!=HIGH
            or p.get('children')!=[] or p.get('receipt_checks')!=6
            or digest(rp)!=RECEIPT or digest(mp)!=MATH_PROCESS):
            raise ValueError('the exact zero-mathematics receipt and original successful child must be kept')
        inputs['high']=self.exact_native(root,
            'native/complete-repaired-M32-known-high-tail-source.json.gz',p,HIGH)
        inputs.update({'high-receipt':rp,'high-receipt-process':pp,'high-math-process':mp,
            'candidate':self.science/self.manifest['candidate_input']})
        for source,name in ((pp,'original-known-high-receipt-artifact-process.json'),
            (rp,'original-known-high-six-gate-receipt.json'),
            (mp,'original-known-high-math-success-publication-failure-process.json')):
            shutil.copyfile(source,self.evidence/name)
        return inputs

    def previous(self,input_sha):
        root=TOPIC/FOLDER;candidates=[]
        if not root.exists():return None
        for pp in sorted(root.glob('*/process.json')):
            p=read(pp)
            if (p.get('repository')!='Rogerhu12/math-research-public'
                or p.get('worker_source_sha256')!=digest(__file__)
                or p.get('input_manifest_sha256')!=self.args.manifest_sha
                or p.get('actual_input_sha256')!=input_sha
                or not any(c.get('label')==LABEL for c in p.get('children',[]))):continue
            matches=[x for x in p.get('native_files',[]) if x.get('logical_file')=='native/'+NATIVE]
            if len(matches)!=1:continue
            path=self.exact_native(pp.parent,'native/'+NATIVE,p,matches[0]['sha256'])
            d=read(path)
            if (d.get('kind')!=KIND or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
                or d.get('input_sha256')!=input_sha):continue
            names=('body_cross_rows','weighted_backward_rows','weighted_forward_rows')
            if any(r.get('complete') is not True for name in names for r in d.get(name,[])):
                raise ValueError('an exact same-science prefix contains incomplete saved rows')
            complete=(d.get('complete') and not d.get('failure')
                and d.get('gates') and all(g['passed'] for g in d['gates'])
                and len(d.get('body_cross_rows',[]))==7721
                and len(d.get('weighted_backward_rows',[]))==12361
                and len(d.get('weighted_forward_rows',[]))==12361
                and d.get('complete_body_only_weighted_Green_feedback_bound_proved')
                and any(c.get('label')==LABEL and c.get('actual_returncode')==0 for c in p['children']))
            score=(int(bool(complete)),sum(len(d.get(name,[])) for name in names))
            candidates.append((score,pp,path,bool(complete)))
        return max(candidates,key=lambda x:x[0]) if candidates else None

    def execute(self,label,command):
        # Bypass KernelWorker.execute: this child has its own native basename.
        try:return ReviewedBodyWorker.execute(self,label,command)
        finally:
            path=self.cache/NATIVE
            if path.exists():
                d=read(path)
                outcome=dict(kind=d.get('kind'),complete=d.get('complete'),failure=d.get('failure'),
                    gates=d.get('gates',[]),native_sha256=digest(path),actual_progress=d.get('actual_progress'),
                    actual_new_scalar_rows=d.get('new_body_cross_scalar_rows'),
                    scalar_rows=len(d.get('body_cross_rows',[])),
                    backward_events=len(d.get('weighted_backward_rows',[])),
                    forward_events=len(d.get('weighted_forward_rows',[])))
                small(self.evidence/'actual-latest-child-outcome.json',outcome)
                print(json.dumps(outcome),flush=True)
                if d.get('failure') and self.log.exists():print(self.log.read_text()[-16000:],flush=True)

    def prepare(self):
        inputs=self.original_inputs();input_sha={k:digest(v) for k,v in inputs.items()}
        self.state['actual_input_sha256']=input_sha;path=self.cache/NATIVE
        command=[sys.executable,'-u',str(self.science/PRODUCER),'--out',str(path)]
        for k,v in inputs.items():command+=['--'+k,str(v)]
        prior=self.previous(input_sha)
        if prior:
            _,pp,native,complete=prior
            shutil.copyfile(pp,self.evidence/'original-same-science-prefix-process.json')
            small(self.evidence/'original-body-feedback-prefix-reuse.json',dict(
                original_process_sha256=digest(pp),original_native_sha256=digest(native),
                original_process_complete=read(pp).get('complete'),original_native_complete=complete,
                original_publication_failure_retained=read(pp).get('failure'),
                mathematical_success_not_rejected_by_a_later_publication_failure=True))
            if complete:
                shutil.copyfile(native,path);self.reused_complete=True
            else:
                saved=self.work/'original-exact-body-feedback-prefix.json.gz'
                shutil.copyfile(native,saved);command+=['--resume',str(saved)]
        self.publish()
        if not self.reused_complete:self.execute(LABEL,command)
        d=read(path)
        if (not d.get('complete') or d.get('failure') or d.get('kind')!=KIND
            or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or d.get('input_sha256')!=input_sha or not d.get('gates')
            or not all(g['passed'] for g in d['gates'])
            or d.get('complete_original_common_rows')!=7721
            or d.get('complete_continuous_cells')!=6391 or d.get('complete_projector_interfaces')!=5970
            or not d.get('complete_body_only_weighted_Green_feedback_bound_proved')
            or not d.get('complete_fixed_M32_body_cross_operator_fees_proved')
            or not d.get('high_cut_trace_is_an_independent_input_not_bounded_by_body_L2')
            or d.get('actual_full_PDE_response_error_proved')
            or d.get('complete_infinite_BVP_inverse_proved')):
            raise ValueError('the actual complete body feedback consumer failed or changed its scope')
        summary={k:v for k,v in d.items()
            if k not in ('body_cross_rows','weighted_backward_rows','weighted_forward_rows')}
        summary.update(native_sha256=digest(path),full_complete_native_retained=True,
            original_complete_success_reused_without_any_child=self.reused_complete,
            actual_new_scalar_rows_this_child=0 if self.reused_complete else d['new_body_cross_scalar_rows'],
            actual_new_weighted_backward_events_this_child=0 if self.reused_complete else d['new_weighted_backward_events'],
            actual_new_weighted_forward_events_this_child=0 if self.reused_complete else d['new_weighted_forward_events'])
        small(self.evidence/'complete-M32-body-cross-weighted-Green-summary.json',summary)
        self.state.update(complete=True,complete_native_sha256=digest(path),
            actual_scientific_gates=len(d['gates']),
            complete_body_only_weighted_Green_feedback_bound_proved=True,
            complete_body_cross_multiplier_bounds=d['complete_body_cross_multiplier_bounds'],
            complete_body_only_Green_high_to_low_L2_bounds=d['complete_body_only_Green_high_to_low_L2_bounds'],
            complete_body_only_Green_high_to_low_C0_bounds=d['complete_body_only_Green_high_to_low_C0_bounds'],
            original_complete_success_reused_without_any_child=self.reused_complete)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','green-artifact','kernel-artifact','high-receipt-artifact','work','artifact-dir'):
        p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--compute-minutes',type=int,default=60)
    p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='M32-body-cross-weighted-Green';a.mode='prepare';a.first=0;a.end=0
    a.recovery_manifest=None;a.recovery_sha=None
    worker=FeedbackWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):
        signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
