#!/usr/bin/env python3
"""Run only the new L2 kernel integration on exact successful finite193 ports."""
from __future__ import annotations
import argparse,json,shutil,signal,sys
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC
from fourfold_native_lossless_parts import restore

REL='topics/visible-flex-exact-nearby/'
PRODUCER=REL+'scripts/fourfold_codazzi_finite193_L2_Green_kernel.py'
FOLDER='notes/finite193_L2_Green_kernel_ci'
NATIVE='complete-finite193-ordinary-L2-Green-kernel.json.gz'
LABEL='actual_complete6391_ordinary_L2_Green_kernel_integrals'
KIND='actual_finite193_ordinary_L2_source_kernel_from_complete_ports_v1'
OLD_RUN=43601964129
OLD_NATIVE='fd6c1f4baa4ec86aab08d4925a0ec9565c3791cbe470b77c2e41549d8f071de6'
OLD_PROCESS='297cb4c9b8f58bbaacbcf1d0be594f43ea385420f8ea58fbb14e83bf84a63a1c'
OLD_WORKER='6d3446499f8cad204aedd71142e9ba1b86d1f57af2394050af1681d040169770'
OLD_MANIFEST='da3e142168cb2a92d08548efe71ed4505e2e82d82cda965b128582e1acb22764'


def small(path,doc):
    raw=(json.dumps(doc,ensure_ascii=False,indent=2)+'\n').encode()
    if len(raw)>60000:raise ValueError('small L2 kernel evidence exceeds60000 bytes; keep full native')
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(raw)


class KernelWorker(ReviewedBodyWorker):
    def __init__(self,a):
        super().__init__(a)
        self.name=f'run-{self.run_label}-finite193-ordinary-L2-Green-kernel'
        self.dest=TOPIC/FOLDER/self.name
        self.reused_complete=False
        self.state.update(kind='actual_public_finite193_ordinary_L2_kernel_process_v1',
            worker_source_sha256=digest(__file__),original_complete_finite193_Green_run=OLD_RUN,
            original_6391_signed_ports_recomputed=0,original_target_or_large_array_calls=0,
            original_complete_Riccati_projector_body_mean_or_cap_cells_recomputed=0,
            complete_finite193_ordinary_L2_source_inverse_bound_proved=False,
            complete_infinite_BVP_inverse_proved=False,
            actual_full_PDE_response_error_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='finite193_ordinary_L2_source_kernel_public_inputs_v1':
            raise ValueError('the separate complete L2 kernel manifest is required')

    def exact_native(self,root,logical,p,expected=None):
        records=[x for x in p.get('native_files',[]) if x.get('logical_file')==logical]
        if len(records)!=1:raise ValueError('one exact native byte receipt is required')
        entry=records[0]
        if expected is not None and entry['sha256']!=expected:
            raise ValueError('the expected original complete native changed')
        target=root/logical
        if not target.exists():
            if 'lossless_manifest' not in entry:raise ValueError('the exact native bytes are absent')
            target=self.work/('restored-'+entry['sha256']+'.json.gz')
            if not target.exists():restore(root/entry['lossless_manifest'],target)
        if digest(target)!=entry['sha256'] or target.stat().st_size!=entry['bytes']:
            raise ValueError('an original native hash or complete byte size changed')
        return target

    def original_inputs(self):
        root=self.args.green_artifact.resolve();pp=root/'process.json';p=read(pp)
        if (digest(pp)!=OLD_PROCESS or p.get('repository')!='Rogerhu12/math-research-public'
            or str(p.get('run_id'))!=str(OLD_RUN) or not p.get('complete') or p.get('failure')
            or p.get('phase')!='complete' or p.get('worker_source_sha256')!=OLD_WORKER
            or p.get('input_manifest_sha256')!=OLD_MANIFEST
            or p.get('complete_native_sha256')!=OLD_NATIVE
            or not p.get('complete_finite193_inverse_proved')
            or not p.get('children') or any(c.get('actual_returncode')!=0 for c in p['children'])):
            raise ValueError('the exact successful original Green artifact process is required')
        native=self.exact_native(root,'native/complete-finite-head-Green-and-distributed-known-sources.json.gz',
                                 p,OLD_NATIVE)
        shutil.copyfile(pp,self.evidence/'original-complete-finite193-Green-process.json')
        return {'green':native,'green-process':pp}

    def previous(self,input_sha):
        candidates=[];root=TOPIC/FOLDER
        if not root.exists():return None
        for pp in sorted(root.glob('*/process.json')):
            p=read(pp)
            if (p.get('repository')!='Rogerhu12/math-research-public'
                or p.get('worker_source_sha256')!=digest(__file__)
                or p.get('input_manifest_sha256')!=self.args.manifest_sha
                or p.get('actual_input_sha256')!=input_sha
                or not any(c.get('label')==LABEL for c in p.get('children',[]))):continue
            records=[x for x in p.get('native_files',[]) if x.get('logical_file')=='native/'+NATIVE]
            if len(records)!=1:continue
            path=self.exact_native(pp.parent,'native/'+NATIVE,p,records[0]['sha256'])
            d=read(path)
            if (d.get('kind')!=KIND or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
                or d.get('input_sha256')!=input_sha):continue
            if any(x.get('complete') is not True for name in ('backward_kernel_rows','forward_kernel_event_rows')
                   for x in d.get(name,[])):
                raise ValueError('a same-identity saved kernel prefix contains incomplete rows')
            mathematical_success=(d.get('complete') and not d.get('failure')
                and d.get('gates') and all(x['passed'] for x in d['gates'])
                and d.get('complete_finite193_ordinary_L2_source_inverse_bound_proved')
                and len(d.get('backward_kernel_rows',[]))==12361
                and len(d.get('forward_kernel_event_rows',[]))==12361
                and any(c.get('label')==LABEL and c.get('actual_returncode')==0 for c in p['children']))
            score=(1 if mathematical_success else 0,
                   len(d.get('backward_kernel_rows',[]))+len(d.get('forward_kernel_event_rows',[])))
            candidates.append((score,pp,path,mathematical_success))
        return max(candidates,key=lambda x:x[0]) if candidates else None

    def execute(self,label,command):
        try:return super().execute(label,command)
        finally:
            native=self.cache/NATIVE
            if native.exists():
                d=read(native)
                outcome=dict(complete=d.get('complete'),failure=d.get('failure'),gates=d.get('gates',[]),
                    native_sha256=digest(native),actual_progress=d.get('actual_progress'),
                    backward_events=len(d.get('backward_kernel_rows',[])),
                    forward_events=len(d.get('forward_kernel_event_rows',[])),
                    actual_new_four_by_four_integrals=d.get('new_four_by_four_kernel_integrals_executed'))
                small(self.evidence/'actual-latest-child-outcome.json',outcome)
                print(json.dumps(outcome),flush=True)
                if d.get('failure') and self.log.exists():print(self.log.read_text()[-16000:],flush=True)

    def prepare(self):
        inputs=self.original_inputs();input_sha={key:digest(path) for key,path in inputs.items()}
        self.state['actual_input_sha256']=input_sha;native=self.cache/NATIVE
        prior=self.previous(input_sha)
        command=[sys.executable,'-u',str(self.science/PRODUCER),'--out',str(native)]
        for key,path in inputs.items():command+=['--'+key,str(path)]
        if prior:
            _,pp,path,complete=prior
            shutil.copyfile(pp,self.evidence/'original-same-identity-kernel-prefix-process.json')
            small(self.evidence/'original-kernel-prefix-reuse.json',dict(
                original_process_sha256=digest(pp),original_native_sha256=digest(path),
                original_process_complete=read(pp).get('complete'),original_native_complete=complete,
                original_failure_preserved=read(pp).get('failure'),
                complete_success_may_precede_a_failed_publication=True))
            if complete:
                shutil.copyfile(path,native);self.reused_complete=True
            else:
                prefix=self.work/'original-exact-kernel-prefix.json.gz'
                shutil.copyfile(path,prefix);command+=['--resume',str(prefix)]
        self.publish()
        if not self.reused_complete:self.execute(LABEL,command)
        d=read(native)
        if (not d.get('complete') or d.get('failure') or d.get('kind')!=KIND
            or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or d.get('input_sha256')!=input_sha or not d.get('gates')
            or not all(x['passed'] for x in d['gates'])
            or d.get('complete_continuous_cells')!=6391
            or d.get('complete_projector_interfaces')!=5970
            or not d.get('complete_finite193_ordinary_L2_source_inverse_bound_proved')
            or d.get('complete_infinite_BVP_inverse_proved')
            or d.get('exact_full_PDE_parameter_response_error_proved')):
            raise ValueError('the actual complete ordinary L2 kernel did not pass or changed scope')
        summary={key:value for key,value in d.items()
                 if key not in ('backward_kernel_rows','forward_kernel_event_rows')}
        summary.update(native_sha256=digest(native),full_original_kernel_native_retained=True,
            original_complete_new_kernel_native_reused_without_any_child=self.reused_complete,
            new_four_by_four_integrals_this_child=0 if self.reused_complete
                else d['new_four_by_four_kernel_integrals_executed'],
            new_whole_cell_integrals_this_child=0 if self.reused_complete
                else d['new_whole_cell_L2_integral_bounds_executed'])
        small(self.evidence/'complete-finite193-ordinary-L2-Green-kernel-summary.json',summary)
        self.state.update(complete=True,complete_native_sha256=digest(native),
            actual_scientific_gates=len(d['gates']),
            complete_finite193_ordinary_L2_source_inverse_bound_proved=True,
            complete_ordinary_L2_source_to_L2_bounds=d['complete_ordinary_L2_source_to_L2_bounds'],
            complete_ordinary_L2_source_to_C0_bounds=d['complete_ordinary_L2_source_to_C0_bounds'],
            new_four_by_four_integrals_this_child=summary['new_four_by_four_integrals_this_child'],
            new_whole_cell_integrals_this_child=summary['new_whole_cell_integrals_this_child'],
            original_complete_new_kernel_native_reused_without_any_child=self.reused_complete)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','green-artifact','work','artifact-dir'):
        p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--compute-minutes',type=int,default=75)
    p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='finite193-ordinary-L2-kernel';a.mode='prepare';a.first=0;a.end=0
    a.recovery_manifest=None;a.recovery_sha=None
    worker=KernelWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):
        signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
