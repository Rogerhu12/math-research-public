#!/usr/bin/env python3
"""Preserve exact completed inputs; run only new positive head weights and cut ports."""
from __future__ import annotations
import argparse,json,shutil,signal,sys
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_finite193_L2_Green_kernel_CI import KernelWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC

REL='topics/visible-flex-exact-nearby/'
PRODUCER=REL+'scripts/fourfold_codazzi_positive_high_weighted_body_cut_ports.py'
FOLDER='notes/positive_high_weighted_body_cut_ci'
NATIVE='complete-positive-high-weighted-body-and-cut-ports.json.gz'
KIND='actual_repaired_positive_high_weighted_inner_body_and_cut_trace_ports_v1'
LABEL='actual_positive_high_weighted_head_and_inner_body_cut_trace_ports'
BODY='eefb94952a409473fed7f9c34afc9214a3346d8c3b19ed7e0a7fc6fd06f48a68'
BODY_WORKER='9b9ae2e6bc08cbfd6dfd531d324342fbed070cf0c9ed21ea1c35a75965ea0480'
BODY_MANIFEST='a61b4053128b75672816fad256139e2cd8c231cf752321f82f276a9d0d992cd0'
CROSS_WORKER='17b01cfc23cef3b8a0119e4dfb004c7ac77c2b33fa43b2c677f84827f710ed7f'
CROSS_MANIFEST='fecb0119d3e4f472cd74d4ae80f8f31de2ee0ba4b3635e974c2bbe65f200b12e'
CROSS_SOURCE='cbcfcaf8712e03f329961b2543b320bda0aeae6d75491f05a78f22ca8ef4188e'
CROSS_NATIVE='a12fd95f9ebaf50cc6fb0db7c97d0416152c985b739ad19fcdc730a12c82ef09'
CROSS_KIND='actual_fixed_M32_body_cross_bands_and_cached_weighted_L2_Green_v1'
STAGES=('source_weight_rows','forward_source_square_rows','backward_source_square_rows')


def small(path,doc):
    data=(json.dumps(doc,ensure_ascii=False,indent=2)+'\n').encode()
    if len(data)>60000:raise ValueError('new positive-port plaintext exceeds60000 bytes; full native retained')
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(data)
def child_ok(process,label):
    return any(x.get('label')==label and x.get('actual_returncode')==0
        for x in process.get('children',[]))


class PortsWorker(KernelWorker):
    def __init__(self,a):
        super().__init__(a)
        self.name=f'run-{self.run_label}-positive-high-weighted-body-cut'
        self.dest=TOPIC/FOLDER/self.name
        self.state.update(kind='actual_public_positive_high_weighted_body_cut_process_v1',
            worker_source_sha256=digest(__file__),original_complete_positive_body_run=43601149891,
            original_positive_given_head_graph_run=43605513540,
            original_M32_body_cross_run=a.cross_run,
            original_4650_target_or_Riccati_rows_recomputed=0,
            original_cap_residual_finite_Green_or_negative_return_recomputed=0,
            complete_positive_given_head_body_and_cut_trace_ports_proved=False,
            complete_infinite_BVP_inverse_proved=False,actual_full_PDE_response_error_proved=False)

    def check_inputs(self):
        ReviewedBodyWorker.check_inputs(self)
        if self.manifest.get('kind')!='positive_high_weighted_inner_body_and_cut_ports_public_inputs_v1':
            raise ValueError('the separate positive two-output manifest is required')

    def original_inputs(self):
        root=self.args.body_artifact.resolve();pp=root/'process.json';p=read(pp)
        if (p.get('repository')!='Rogerhu12/math-research-public'
            or str(p.get('run_id'))!='43601149891' or str(p.get('run_attempt'))!='1'
            or p.get('worker_source_sha256')!=BODY_WORKER
            or p.get('input_manifest_sha256')!=BODY_MANIFEST
            or not child_ok(p,'actual_repaired_4650_complete_positive_rows_and_both_unbounded_high_orders')):
            raise ValueError('the actual original repaired positive body process is required')
        body=self.exact_native(root,'native/repaired-complete-positive-N97-high-inverse.json.gz',p,BODY)
        inputs={'body':body,'body-process':pp}
        shutil.copyfile(pp,self.evidence/'original-positive-body-artifact-process.json')
        root=self.args.cross_artifact.resolve();pp=root/'process.json';p=read(pp)
        logical='native/complete-M32-body-cross-and-weighted-Green.json.gz'
        records=[r for r in p.get('native_files',[]) if r.get('logical_file')==logical]
        if (p.get('repository')!='Rogerhu12/math-research-public'
            or str(p.get('run_id'))!=str(self.args.cross_run)
            or str(p.get('run_attempt'))!=str(self.args.cross_attempt)
            or p.get('worker_source_sha256')!=CROSS_WORKER
            or p.get('input_manifest_sha256')!=CROSS_MANIFEST
            or len(records)!=1 or records[0].get('sha256')!=CROSS_NATIVE
            or not child_ok(p,'actual_M32_body_cross_fees_and_cached_weighted_Green')):
            raise ValueError('the actual complete body-cross mathematical success and exact receipt are required')
        cross=self.exact_native(root,logical,p,CROSS_NATIVE);d=read(cross)
        if (d.get('kind')!=CROSS_KIND or d.get('source_sha256')!=CROSS_SOURCE
            or not d.get('complete') or d.get('failure') or not d.get('gates')
            or not all(g['passed'] for g in d['gates'])
            or d.get('complete_original_common_rows')!=7721
            or not d.get('complete_fixed_M32_body_cross_operator_fees_proved')):
            raise ValueError('the complete body-cross native did not certify the required same-centre fees')
        inputs.update({'cross':cross,'cross-process':pp})
        shutil.copyfile(pp,self.evidence/'original-complete-body-cross-artifact-process.json')
        small(self.evidence/'original-body-cross-math-receipt.json',dict(
            native_sha256=digest(cross),artifact_process_sha256=digest(pp),
            run_id=p['run_id'],run_attempt=p['run_attempt'],original_process_complete=p.get('complete'),
            original_publication_failure_retained=p.get('failure'),mathematical_native_complete=True,
            mathematical_gates=d['gates'],mathematical_success_accepted_independently_of_later_publication=True))
        for name,path in self.manifest['original_graph_small_inputs'].items():
            inputs[name]=self.science/path
            shutil.copyfile(inputs[name],self.evidence/('original-'+name+'.json'))
        return inputs

    def previous(self,input_sha):
        directory=TOPIC/FOLDER;candidates=[]
        if not directory.exists():return None
        for pp in sorted(directory.glob('*/process.json')):
            p=read(pp)
            if (p.get('repository')!='Rogerhu12/math-research-public'
                or p.get('worker_source_sha256')!=digest(__file__)
                or p.get('input_manifest_sha256')!=self.args.manifest_sha
                or p.get('actual_input_sha256')!=input_sha
                or not any(c.get('label')==LABEL for c in p.get('children',[]))):continue
            records=[r for r in p.get('native_files',[]) if r.get('logical_file')=='native/'+NATIVE]
            if len(records)!=1:continue
            native=self.exact_native(pp.parent,'native/'+NATIVE,p,records[0]['sha256']);d=read(native)
            if (d.get('kind')!=KIND or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
                or d.get('input_sha256')!=input_sha):continue
            if any(r.get('complete') is not True for name in STAGES for r in d.get(name,[])):
                raise ValueError('a same-science positive-port prefix contains an incomplete row')
            complete=bool(d.get('complete') and not d.get('failure') and d.get('gates')
                and all(g['passed'] for g in d['gates'])
                and d.get('complete_positive_given_head_body_and_cut_trace_ports_proved')
                and d.get('complete_positive_weighted_head_source_columns_proved')
                and child_ok(p,LABEL))
            score=(int(complete),sum(len(d.get(name,[])) for name in STAGES))
            candidates.append((score,pp,native,complete))
        return max(candidates,key=lambda row:row[0]) if candidates else None

    def execute(self,label,command):
        try:return ReviewedBodyWorker.execute(self,label,command)
        finally:
            path=self.cache/NATIVE
            if path.exists():
                d=read(path);out=dict(kind=d.get('kind'),complete=d.get('complete'),
                    failure=d.get('failure'),gates=d.get('gates',[]),native_sha256=digest(path),
                    actual_progress=d.get('actual_progress'),
                    stage_rows={name:len(d.get(name,[])) for name in STAGES})
                small(self.evidence/'actual-latest-positive-port-outcome.json',out)
                print(json.dumps(out),flush=True)
                if d.get('failure') and self.log.exists():print(self.log.read_text()[-16000:],flush=True)

    def prepare(self):
        inputs=self.original_inputs();input_sha={k:digest(v) for k,v in inputs.items()}
        self.state['actual_input_sha256']=input_sha;native=self.cache/NATIVE
        command=[sys.executable,'-u',str(self.science/PRODUCER),'--out',str(native)]
        for name,path in inputs.items():command+=['--'+name,str(path)]
        prior=self.previous(input_sha)
        if prior:
            _,pp,old,complete=prior
            shutil.copyfile(pp,self.evidence/'original-same-positive-port-prefix-process.json')
            small(self.evidence/'original-positive-port-prefix-reuse.json',dict(
                original_process_sha256=digest(pp),original_native_sha256=digest(old),
                original_process_complete=read(pp).get('complete'),mathematical_native_complete=complete,
                publication_failure_retained=read(pp).get('failure'),
                successful_mathematics_reused_without_requiring_publication_complete=True))
            if complete:shutil.copyfile(old,native);self.reused_complete=True
            else:
                previous=self.work/'original-positive-port-prefix.json.gz'
                shutil.copyfile(old,previous);command+=['--resume',str(previous)]
        self.publish()
        if not self.reused_complete:self.execute(LABEL,command)
        d=read(native)
        if (d.get('kind')!=KIND or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or d.get('input_sha256')!=input_sha or not d.get('complete') or d.get('failure')
            or not d.get('gates') or not all(g['passed'] for g in d['gates'])
            or d.get('complete_original_positive_rows')!=4650
            or d.get('complete_original_body_cross_rows')!=7721
            or not d.get('complete_positive_given_head_body_and_cut_trace_ports_proved')
            or not d.get('complete_positive_weighted_head_source_columns_proved')
            or not d.get('high_trace_not_inferred_from_radial_L2')
            or d.get('complete_infinite_BVP_inverse_proved') or d.get('actual_full_PDE_response_error_proved')):
            raise ValueError('the actual positive body/cut port consumer failed or exceeded its scope')
        excluded=set(STAGES)|{'original_graph_seven_response_rows_retained','original_cross_collar_cover'}
        summary={k:v for k,v in d.items() if k not in excluded}
        summary.update(native_sha256=digest(native),complete_native_retained=True,
            original_complete_success_reused_without_child=self.reused_complete)
        small(self.evidence/'complete-positive-high-weighted-body-cut-summary.json',summary)
        self.state.update(complete=True,complete_native_sha256=digest(native),
            actual_scientific_gates=len(d['gates']),
            complete_positive_given_head_body_and_cut_trace_ports_proved=True,
            complete_positive_weighted_head_source_columns_proved=True,
            true_cut_high_even_reconstruction_upper=d['true_cut_high_even_reconstruction_upper'],
            weighted_head_combined_inner_output_columns=d['weighted_head_combined_inner_output_columns'],
            original_complete_success_reused_without_child=self.reused_complete)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','body-artifact','cross-artifact','work','artifact-dir'):
        p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha','cross-run','cross-attempt'):
        p.add_argument('--'+name,required=True)
    p.add_argument('--compute-minutes',type=int,default=40)
    p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='positive-high-weighted-body-cut';a.mode='prepare';a.first=0;a.end=0
    a.recovery_manifest=None;a.recovery_sha=None
    worker=PortsWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):
        signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
