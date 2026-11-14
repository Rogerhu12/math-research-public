#!/usr/bin/env python3
"""Public new full193 local matrix pilot; reuse all completed exact new rows."""
from __future__ import annotations
import argparse,json,shutil,signal,sys
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_finite193_L2_Green_kernel_CI import KernelWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC

REL='topics/visible-flex-exact-nearby/'
PRODUCER=REL+'scripts/fourfold_codazzi_cached_full193_matrix_pilot.py'
FOLDER='notes/cached_full193_matrix_pilot_ci'
NATIVE='complete-four-cached-full193-matrix-polynomials.json.gz'
KIND='actual_full193_local_matrix_polynomials_from_cached_exact_reference_v1'
LABEL='new_complete193_by193_local_polynomials_from_four_exact_cached_rows'
INDICES=[0,76,3300,5969]


def small(path,doc):
    raw=(json.dumps(doc,ensure_ascii=False,indent=2)+'\n').encode()
    if len(raw)>60000:raise ValueError('new full193 pilot plaintext evidence exceeds60000 bytes')
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(raw)


class MatrixWorker(ReviewedBodyWorker):
    exact_native=KernelWorker.exact_native

    def __init__(self,a):
        super().__init__(a)
        self.name=f'run-{self.run_label}-cached-full193-local-matrix-pilot'
        self.dest=TOPIC/FOLDER/self.name;self.reused_complete=False
        self.state.update(kind='actual_public_cached_full193_matrix_pilot_process_v1',
            worker_source_sha256=digest(__file__),original_projector_pilot_run=43591378059,
            original_all_projector_run=43594139132,
            original_successful_projector_or_target_cells_recomputed=0,
            original_Q_anchors_not_used_as_full_matrix_propagators=True,
            requested_original_indices=INDICES,
            full5970_matrix_cover_claimed=False,
            directional_full_BVP_inverse_bound_proved=False,
            complete_infinite_BVP_inverse_proved=False,
            true_parameter_Schur_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='cached_full193_local_matrix_public_pilot_inputs_v1':
            raise ValueError('the exact new full193 cached-matrix pilot manifest is required')

    def inputs(self):
        folder=self.science/self.manifest['pilot_summary_directory'];inputs={}
        for index in INDICES:
            path=folder/f'validated-cell-{index:05d}-summary.json'
            expected=self.manifest['original_pilot_summary_sha256'][str(index)]
            if digest(path)!=expected:raise ValueError('one original full-row summary differs')
            d=read(path)
            if (not d.get('complete') or d.get('selected_indices')!=[index,index+1]
                or d.get('native_sha256')!=self.manifest['original_pilot_native_sha256'][str(index)]):
                raise ValueError('the original complete local-matrix input is not a successful old row')
            inputs[str(index)]=digest(path)
        return folder,inputs

    def previous(self,inputs):
        root=TOPIC/FOLDER;candidates=[]
        if not root.exists():return None
        for pp in sorted(root.glob('*/process.json')):
            p=read(pp)
            if (p.get('repository')!='Rogerhu12/math-research-public'
                or p.get('worker_source_sha256')!=digest(__file__)
                or p.get('input_manifest_sha256')!=self.args.manifest_sha
                or p.get('actual_original_summary_sha256')!=inputs):continue
            records=[x for x in p.get('native_files',[]) if x.get('logical_file')=='native/'+NATIVE]
            if len(records)!=1:continue
            path=self.exact_native(pp.parent,'native/'+NATIVE,p,records[0]['sha256'])
            d=read(path);identity=d.get('identity',{})
            if (d.get('kind')!=KIND or identity.get('source_sha256')!=self.manifest['files'][PRODUCER]
                or identity.get('original_summary_sha256')!=inputs
                or identity.get('exact_pilot_indices')!=INDICES
                or identity.get('new_polynomial_degree')!=24
                or identity.get('arithmetic_bits')!=256):continue
            rows=d.get('rows',[])
            if ([r.get('index') for r in rows]!=INDICES[:len(rows)]
                or any(not r.get('complete') or not r.get('array_receipt',{}).get('sha256') for r in rows)):
                raise ValueError('a same-identity new matrix checkpoint has incomplete successful rows')
            successful_child=any(c.get('label')==LABEL and c.get('actual_returncode')==0
                                 for c in p.get('children',[]))
            successful_reuse=(p.get('complete') and p.get('original_complete_success_reused_without_child')
                              and p.get('original_success_process_sha256'))
            complete=(d.get('complete') and not d.get('failure') and len(rows)==4
                and d.get('gates') and all(g['passed'] for g in d['gates'])
                and d.get('true_full193_local_matrix_polynomials_certified')
                and (successful_child or successful_reuse))
            candidates.append(((1 if complete else 0,len(rows)),pp,path,complete))
        return max(candidates,key=lambda x:x[0]) if candidates else None

    def outcome(self,d):
        return dict(complete=d.get('complete'),failure=d.get('failure'),gates=d.get('gates',[]),
            completed_indices=[r['index'] for r in d.get('rows',[])],
            new_matrix_cells_this_child=d.get('new_matrix_cells_this_child'),
            reused_completed_new_matrix_cells=d.get('reused_completed_new_matrix_cells'),
            original_target_calls=d.get('original_target_calls'),
            actual_local_rows=[dict(index=r['index'],interval=r['interval'],
                seconds=r.get('seconds'),
                new_true_generator_error=r['definition']['new_full_true_generator_error'],
                forward_true_local_rational_error=r['forward']['full_true_local_rational_operator_error'],
                backward_true_local_rational_error=r['backward']['full_true_local_rational_operator_error'],
                forward_whole_inverse=r['forward']['whole_polynomial_inverse_operator_upper'],
                backward_whole_inverse=r['backward']['whole_polynomial_inverse_operator_upper'],
                array_receipt=r['array_receipt']) for r in d.get('rows',[])],
            directional_full_BVP_inverse_bound_proved=False,
            full5970_matrix_cover_claimed=False)

    def execute(self,label,command):
        try:return super().execute(label,command)
        finally:
            native=self.cache/NATIVE
            if native.exists():
                d=read(native);outcome=self.outcome(d)
                outcome['native_sha256']=digest(native)
                small(self.evidence/'actual-latest-full193-matrix-outcome.json',outcome)
                print(json.dumps(dict(complete=d.get('complete'),failure=d.get('failure'),
                    rows=len(d.get('rows',[])),native_sha256=digest(native))),flush=True)
                if d.get('failure') and self.log.exists():print(self.log.read_text()[-16000:],flush=True)

    def prepare(self):
        folder,inputs=self.inputs();self.state['actual_original_summary_sha256']=inputs
        native=self.cache/NATIVE;arrays=self.artifact/'matrices';arrays.mkdir(parents=True,exist_ok=True)
        previous=self.previous(inputs)
        command=[sys.executable,'-u',str(self.science/PRODUCER),
            '--summary-dir',str(folder),'--arrays',str(arrays),'--out',str(native),
            '--degree','24','--bits','256']
        if previous:
            _,pp,path,complete=previous
            shutil.copyfile(pp,self.evidence/'original-same-identity-matrix-process.json')
            small(self.evidence/'original-matrix-prefix-reuse.json',dict(
                original_process_sha256=digest(pp),original_native_sha256=digest(path),
                original_process_complete=read(pp).get('complete'),original_mathematics_complete=complete,
                original_failure_preserved=read(pp).get('failure'),
                complete_success_reused_independently_of_later_publication=True,
                older_array_files_keep_their_original_public_artifact_origins=True))
            if complete:
                shutil.copyfile(path,native);self.reused_complete=True
                self.state['original_success_process_sha256']=digest(pp)
            else:
                prefix=self.work/'original-cached-full193-matrix-prefix.json.gz'
                shutil.copyfile(path,prefix);command+=['--resume',str(prefix)]
        self.publish()
        if not self.reused_complete:self.execute(LABEL,command)
        d=read(native)
        if (d.get('kind')!=KIND or not d.get('complete') or d.get('failure')
            or d['identity']['source_sha256']!=self.manifest['files'][PRODUCER]
            or d['identity']['original_summary_sha256']!=inputs
            or not d.get('gates') or not all(g['passed'] for g in d['gates'])
            or [r['index'] for r in d.get('rows',[])]!=INDICES
            or not d.get('true_full193_local_matrix_polynomials_certified')
            or d.get('full5970_matrix_cover_claimed') or d.get('directional_full_BVP_inverse_bound_proved')
            or d.get('original_target_calls')!=0):
            raise ValueError('the actual new full193 pilot did not complete in its declared scope')
        origin_inventory=[]
        for row in d['rows']:
            receipt=row['array_receipt'];origin=receipt['original_public_array_origin']
            current=(str(origin['run_id'])==str(self.state['run_id'])
                     and str(origin['run_attempt'])==str(self.state['run_attempt']))
            if current:
                path=arrays/receipt['file']
                if (not path.exists() or path.stat().st_size!=receipt['bytes']
                    or digest(path)!=receipt['sha256']):
                    raise ValueError('a newly completed full matrix array is absent or changed')
            origin_inventory.append(dict(index=row['index'],available_in_this_artifact=current,receipt=receipt))
        summary=self.outcome(d)
        summary.update(native_sha256=digest(native),seconds=d['seconds'],
            original_identity=d['identity'],complete_native_retained=True,
            actual_new_matrix_cells_this_child=0 if self.reused_complete else d['actual_new_full193_matrix_cells'],
            original_complete_success_reused_without_child=self.reused_complete)
        small(self.evidence/'complete-cached-full193-matrix-pilot-summary.json',summary)
        small(self.evidence/'complete-matrix-array-origin-inventory.json',dict(
            arrays=origin_inventory,old_array_bytes_not_recomputed_or_relabelled=True))
        self.state.update(complete=True,complete_native_sha256=digest(native),
            actual_scientific_gates=len(d['gates']),actual_complete_local_matrix_cells=4,
            true_full193_local_matrix_polynomials_certified=True,
            actual_new_matrix_cells_this_child=summary['actual_new_matrix_cells_this_child'],
            original_complete_success_reused_without_child=self.reused_complete,
            all_full_matrix_arrays_have_preserved_exact_origin_receipts=True,
            large_matrix_arrays_only_in_public_Actions_artifacts=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','work','artifact-dir'):p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--compute-minutes',type=int,default=75)
    p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='cached-full193-matrix-pilot';a.mode='prepare';a.first=0;a.end=0
    a.recovery_manifest=None;a.recovery_sha=None
    worker=MatrixWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):
        signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
