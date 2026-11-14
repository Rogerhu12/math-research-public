#!/usr/bin/env python3
"""Public all5970 jump-gain consumer; read existing kernels, no new exp."""
from __future__ import annotations
import argparse,json,shutil,signal,sys
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_finite193_L2_Green_kernel_CI import KernelWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC

REL='topics/visible-flex-exact-nearby/'
PRODUCER=REL+'scripts/fourfold_codazzi_finite193_cached_interface_impulse_gains.py'
FOLDER='notes/finite193_cached_interface_impulse_ci'
NATIVE='complete-all5970-cached-interface-impulse-gains.json.gz'
KIND='actual_all5970_weighted_state_impulse_L2_gains_from_cached_Green_v1'
LABEL='all5970_true_weighted_state_jump_L2_gains_from_cached_signed_kernels'
KERNEL='ac4441cb98afabbbc646697434caebf464a22f702e2d0fa7d8e5910efd7ef448'
KERNEL_PROCESS='641c0ca655a9f0ac7c49a30c4b5fd44a4b79552d7c8f8f4533f086d6d2f88800'
KERNEL_SOURCE='5b8f83906d36363266977441427add053a6ed05625525cfd000e05e03360b3db'
KERNEL_WORKER='368b9b0eb613fa7c508adcae6fb3fbd92193413ac879b1a7ab21d7721492f314'
KERNEL_MANIFEST='fb2336796edcd9ccc57a082015cdb6c51ee7c47a921ce03a3cbf3bbab6181ff6'


def small(path,doc):
    raw=(json.dumps(doc,ensure_ascii=False,indent=2)+'\n').encode()
    if len(raw)>60000:raise ValueError('cached interface plaintext evidence exceeds60000 bytes')
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(raw)


class ImpulseWorker(ReviewedBodyWorker):
    exact_native=KernelWorker.exact_native

    def __init__(self,a):
        super().__init__(a)
        self.name=f'run-{self.run_label}-all5970-cached-interface-impulse-gains'
        self.dest=TOPIC/FOLDER/self.name;self.reused_complete=False
        self.state.update(kind='actual_public_all5970_cached_interface_impulse_process_v1',
            worker_source_sha256=digest(__file__),original_complete_Green_run=43601964129,
            original_complete_L2_kernel_run=43633074696,original_target_or_frame_calls=0,
            new_matrix_or_scalar_exponentials=0,new_Lyapunov_Gram_integrals=0,
            full_matrix_directional_Green_kernel_proved=False,complete_infinite_BVP_inverse_proved=False,
            actual_full_PDE_response_error_proved=False,true_parameter_Schur_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='all5970_cached_interface_impulse_public_inputs_v1':
            raise ValueError('the new exact all-interface impulse manifest is required')

    def inputs(self):
        inputs=KernelWorker.original_inputs(self)
        root=self.args.kernel_artifact.resolve();pp=root/'process.json';p=read(pp)
        if (digest(pp)!=KERNEL_PROCESS or p.get('repository')!='Rogerhu12/math-research-public'
            or str(p.get('run_id'))!='43633074696' or str(p.get('run_attempt'))!='1'
            or p.get('worker_source_sha256')!=KERNEL_WORKER
            or p.get('input_manifest_sha256')!=KERNEL_MANIFEST
            or p.get('complete_native_sha256')!=KERNEL
            or not any(c.get('label')=='actual_complete6391_ordinary_L2_Green_kernel_integrals'
                and c.get('actual_returncode')==0 for c in p.get('children',[]))):
            raise ValueError('the original successful ordinary-L2 kernel process changed')
        native=self.exact_native(root,'native/complete-finite193-ordinary-L2-Green-kernel.json.gz',p,KERNEL)
        d=read(native)
        if (d.get('kind')!='actual_finite193_ordinary_L2_source_kernel_from_complete_ports_v1'
            or d.get('source_sha256')!=KERNEL_SOURCE or not d.get('complete') or d.get('failure')
            or not d.get('gates') or not all(x['passed'] for x in d['gates'])
            or not d.get('complete_finite193_ordinary_L2_source_inverse_bound_proved')
            or len(d.get('backward_kernel_rows',[]))!=12361
            or len(d.get('forward_kernel_event_rows',[]))!=12361):
            raise ValueError('the original complete signed ordinary-L2 kernel proof is required')
        shutil.copyfile(pp,self.evidence/'original-complete-L2-kernel-process.json')
        inputs.update(kernel=native,**{'kernel-process':pp})
        return inputs

    def previous(self,input_sha):
        root=TOPIC/FOLDER;candidates=[]
        if not root.exists():return None
        for pp in sorted(root.glob('*/process.json')):
            p=read(pp)
            if (p.get('repository')!='Rogerhu12/math-research-public'
                or p.get('worker_source_sha256')!=digest(__file__)
                or p.get('input_manifest_sha256')!=self.args.manifest_sha
                or p.get('actual_input_sha256')!=input_sha):continue
            entries=[r for r in p.get('native_files',[]) if r.get('logical_file')=='native/'+NATIVE]
            if len(entries)!=1:continue
            native=self.exact_native(pp.parent,'native/'+NATIVE,p,entries[0]['sha256']);d=read(native)
            if (d.get('kind')!=KIND or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
                or d.get('input_sha256')!=input_sha):continue
            lists=[d.get(k,[]) for k in ('left_response_rows','right_response_rows','interface_impulse_rows')]
            if any(not r.get('complete') for rows in lists for r in rows):
                raise ValueError('a matching impulse checkpoint contains an incomplete row')
            child=any(c.get('label')==LABEL and c.get('actual_returncode')==0 for c in p.get('children',[]))
            reuse=(p.get('complete') and p.get('original_complete_success_reused_without_child')
                   and p.get('original_success_process_sha256'))
            complete=(d.get('complete') and not d.get('failure') and d.get('gates')
                and all(x['passed'] for x in d['gates']) and d.get('all_actual_interface_impulse_gains_proved')
                and list(map(len,lists))==[12361,12361,5970] and (child or reuse))
            candidates.append(((int(bool(complete)),sum(map(len,lists))),pp,native,bool(complete)))
        return max(candidates,key=lambda x:x[0]) if candidates else None

    def outcome(self,d):
        return dict(complete=d.get('complete'),failure=d.get('failure'),gates=d.get('gates',[]),
            actual_progress=d.get('actual_progress'),
            complete_left_events=len(d.get('left_response_rows',[])),
            complete_right_events=len(d.get('right_response_rows',[])),
            complete_individual_interfaces=len(d.get('interface_impulse_rows',[])),
            maximum_individual_jump_L2_gain=d.get('maximum_individual_jump_L2_gain'),
            maximum_individual_jump_gain_at_exact_radius=d.get('maximum_individual_jump_gain_at_exact_radius'),
            new_local_homogeneous_scalar_bounds=d.get('new_local_homogeneous_scalar_bounds'),
            new_matrix_or_scalar_exponentials=d.get('new_matrix_or_scalar_exponentials'),
            new_Lyapunov_Gram_integrals=d.get('new_Lyapunov_Gram_integrals'),
            full_matrix_directional_Green_kernel_proved=False,
            complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False)

    def execute(self,label,command):
        try:return super().execute(label,command)
        finally:
            native=self.cache/NATIVE
            if native.exists():
                d=read(native);outcome=self.outcome(d);outcome['native_sha256']=digest(native)
                small(self.evidence/'actual-latest-interface-impulse-outcome.json',outcome)
                print(json.dumps(outcome),flush=True)
                if d.get('failure') and self.log.exists():print(self.log.read_text()[-16000:],flush=True)

    def prepare(self):
        inputs=self.inputs();input_sha={k:digest(v) for k,v in inputs.items()}
        self.state['actual_input_sha256']=input_sha
        native=self.cache/NATIVE;previous=self.previous(input_sha)
        command=[sys.executable,'-u',str(self.science/PRODUCER)]
        for k,v in inputs.items():command+=['--'+k,str(v)]
        command+=['--out',str(native)]
        if previous:
            _,pp,path,complete=previous
            shutil.copyfile(pp,self.evidence/'original-same-identity-impulse-process.json')
            small(self.evidence/'original-impulse-prefix-reuse.json',dict(
                original_process_sha256=digest(pp),original_native_sha256=digest(path),
                original_process_complete=read(pp).get('complete'),
                original_mathematics_complete=complete,original_failure_preserved=read(pp).get('failure'),
                successful_mathematics_reused_independently_of_later_publication=True))
            if complete:
                shutil.copyfile(path,native);self.reused_complete=True
                self.state['original_success_process_sha256']=digest(pp)
            else:
                prefix=self.work/'original-exact-interface-impulse-prefix.json.gz'
                shutil.copyfile(path,prefix);command+=['--resume',str(prefix)]
        self.publish()
        if not self.reused_complete:self.execute(LABEL,command)
        d=read(native)
        if (d.get('kind')!=KIND or not d.get('complete') or d.get('failure')
            or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or d.get('input_sha256')!=input_sha or not d.get('gates')
            or not all(x['passed'] for x in d['gates'])
            or not d.get('all_actual_interface_impulse_gains_proved')
            or len(d.get('left_response_rows',[]))!=12361
            or len(d.get('right_response_rows',[]))!=12361
            or len(d.get('interface_impulse_rows',[]))!=5970
            or d.get('new_matrix_or_scalar_exponentials')!=0
            or d.get('new_Lyapunov_Gram_integrals')!=0
            or d.get('complete_infinite_BVP_inverse_proved')):
            raise ValueError('the complete cached interface impulse consumer did not finish in its scope')
        summary=self.outcome(d);summary.update(native_sha256=digest(native),seconds=d['seconds'],
            exact_input_sha256=input_sha,complete_native_retained=True,
            actual_new_homogeneous_cells_this_child=0 if self.reused_complete else d['new_local_homogeneous_scalar_bounds'],
            original_complete_success_reused_without_child=self.reused_complete,
            exact_inner_BVP_interval=d['exact_inner_BVP_interval'],
            fixed_phase_error_norm_interval=d['fixed_phase_error_norm_interval'],
            weighted_state_jump_has_no_second_input_weight=True,
            multiple_jump_responses_are_not_declared_orthogonal=True)
        small(self.evidence/'complete-all5970-interface-impulse-summary.json',summary)
        indices=sorted(set([0,1,76,1000,2000,3000,4000,5000,5968,5969]+[
            next(i for i,r in enumerate(d['interface_impulse_rows']) if r['radius']==radius)
            for radius in d['maximum_individual_jump_gain_at_exact_radius'].values()]))
        small(self.evidence/'selected-actual-interface-impulse-rows.json',dict(
            complete_native_sha256=digest(native),
            selected_actual_rows=[dict(original_event_index=d['interface_impulse_rows'][i]['original_event_index'],
                radius=d['interface_impulse_rows'][i]['radius'],
                original_event_sha256=d['interface_impulse_rows'][i]['original_event_sha256'],
                unit_weighted_jump_z_before_upper=d['interface_impulse_rows'][i]['unit_weighted_jump_z_before']['upper'],
                unit_weighted_jump_p_after_upper=d['interface_impulse_rows'][i]['unit_weighted_jump_p_after']['upper'],
                ordinary_L2_output_upper={w:v['upper'] for w,v in
                    d['interface_impulse_rows'][i]['ordinary_L2_output_bound'].items()})
                for i in indices],
            selection_is_evidence_only_complete5970_rows_retained_in_native=True))
        self.state.update(complete=True,complete_native_sha256=digest(native),
            actual_scientific_gates=len(d['gates']),actual_individual_interfaces=5970,
            complete_left_events=12361,complete_right_events=12361,
            all_actual_interface_impulse_gains_proved=True,
            original_complete_success_reused_without_child=self.reused_complete,
            actual_new_homogeneous_cells_this_child=summary['actual_new_homogeneous_cells_this_child'],
            maximum_individual_jump_L2_gain=d['maximum_individual_jump_L2_gain'])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','work','artifact-dir','green-artifact','kernel-artifact'):
        p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--compute-minutes',type=int,default=40)
    p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='all5970-cached-interface-impulse';a.mode='prepare';a.first=0;a.end=0
    a.recovery_manifest=None;a.recovery_sha=None
    worker=ImpulseWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):
        signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
