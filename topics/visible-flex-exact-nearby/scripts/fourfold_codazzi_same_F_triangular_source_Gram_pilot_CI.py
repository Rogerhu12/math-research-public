#!/usr/bin/env python3
"""Public same-F triangular/source-Gram pilot with exact successful reuse."""
from __future__ import annotations
import argparse,json,shutil,signal,sys
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_finite193_L2_Green_kernel_CI import KernelWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC

REL='topics/visible-flex-exact-nearby/'
PRODUCER=REL+'scripts/fourfold_codazzi_same_F_triangular_source_Gram_pilot.py'
FOLDER='notes/same_F_triangular_source_Gram_pilot_ci'
NATIVE='complete-four-same-F-triangular-source-Grams.json.gz'
KIND='actual_same_F_triangular_endpoints_and_full128_source_Grams_four_cell_pilot_v1'
LABEL='same_forward_F_triangular_endpoints_and_three_complete128_source_Grams'
INDICES=[0,76,3300,5969]
OLD_NATIVE='4328b19228049235aded13355585a6d9093a3621daa8d2018f84bc169437d317'
OLD_SOURCE='c8fb7a4ea178fd7415848e36336995149fdfa8959f7cc0700a3efe48d8512b06'
OLD_WORKER='dcdf2ae60435d942cc3139920214d9b071b7b54c60b79a97b6616df250dcfed9'
OLD_MANIFEST='e15a4e56df96b96bdd8f2bd8628f6985518b140978912fa3d45aad7e6c265936'
OLD_PROCESS='7198cd349d5403757728ba641cbc9bf501c6bc2dc2aebafd17c81a62fd95fbdd'
OLD_LABEL='new_complete193_by193_local_polynomials_from_four_exact_cached_rows'


def small(path,doc):
    raw=(json.dumps(doc,ensure_ascii=False,indent=2)+'\n').encode()
    if len(raw)>60000:raise ValueError('same-F pilot plaintext evidence exceeds60000 bytes')
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(raw)


class SameFWorker(ReviewedBodyWorker):
    exact_native=KernelWorker.exact_native

    def __init__(self,a):
        super().__init__(a)
        self.name=f'run-{self.run_label}-same-F-triangular-source-Gram-pilot'
        self.dest=TOPIC/FOLDER/self.name;self.reused_complete=False
        self.state.update(kind='actual_public_same_F_triangular_matrix_Gram_pilot_process_v1',
            worker_source_sha256=digest(__file__),original_full_matrix_run=43645186441,
            original_frame_slice_run=43594139132,
            requested_original_indices=INDICES,original_successful_F_cells_recomputed=0,
            original_target_or_validator_calls=0,original_existing_Green_calls=0,
            original_Q_anchors_not_used_as_full_propagators=True,
            full5970_matrix_cover_claimed=False,full_two_boundary_Green_bound_claimed=False,
            complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='same_F_triangular_complete128_source_Gram_public_pilot_inputs_v1':
            raise ValueError('the exact new same-F source Gram manifest is required')

    def inputs(self):
        root=self.args.matrix_artifact.resolve();pp=root/'process.json';p=read(pp)
        reviewed=self.science/self.manifest['original_reviewed_process'];r=read(reviewed)
        if (digest(reviewed)!=OLD_PROCESS or p.get('repository')!='Rogerhu12/math-research-public'
            or str(p.get('run_id'))!='43645186441' or str(p.get('run_attempt'))!='1'
            or p.get('worker_source_sha256')!=OLD_WORKER
            or p.get('input_manifest_sha256')!=OLD_MANIFEST
            or p.get('complete_native_sha256')!=OLD_NATIVE
            or not any(c.get('label')==OLD_LABEL and c.get('actual_returncode')==0 for c in p.get('children',[]))):
            raise ValueError('the four original successful full193 matrix process identities changed')
        pc=p.get('published_checkpoints',[]);rc=r.get('published_checkpoints',[])
        if ({k:v for k,v in p.items() if k!='published_checkpoints'}
                !={k:v for k,v in r.items() if k!='published_checkpoints'}
            or pc[:min(len(pc),len(rc))]!=rc[:min(len(pc),len(rc))]):
            raise ValueError('the original artifact process differs beyond appended publication receipts')
        native=self.exact_native(root,'native/complete-four-cached-full193-matrix-polynomials.json.gz',p,OLD_NATIVE)
        d=read(native)
        if (not d.get('complete') or d.get('failure')
            or d.get('identity',{}).get('source_sha256')!=OLD_SOURCE
            or [x.get('index') for x in d.get('rows',[])]!=INDICES
            or not d.get('gates') or not all(g['passed'] for g in d['gates'])
            or not d.get('true_full193_local_matrix_polynomials_certified')):
            raise ValueError('the original full193 native mathematics was not fully successful')
        for row in d['rows']:
            receipt=row['array_receipt'];path=root/'matrices'/receipt['file']
            if (not path.exists() or path.stat().st_size!=receipt['bytes']
                or digest(path)!=receipt['sha256']
                or receipt['sha256']!=self.manifest['original_full193_matrix_file_sha256'][str(row['index'])]):
                raise ValueError('one old successful full193 matrix file is absent or changed')
        folder=self.science/self.manifest['pilot_summary_directory'];summaries={}
        for index in INDICES:
            path=folder/f'validated-cell-{index:05d}-summary.json'
            if digest(path)!=self.manifest['original_pilot_summary_sha256'][str(index)]:
                raise ValueError('an original complete coefficient row changed')
            summaries[str(index)]=digest(path)
        slices=[]
        for root0 in self.args.frame_slice:
            root0=root0.resolve();m=root0/'slice-manifest.json';package=read(m)
            if (package.get('kind')!='unchanged_complete_frame_slice_for_disjoint_projector_validation_v1'
                or str(package.get('current_public_workflow_run'))!='43594139132'
                or package.get('original_complete_proposal_sha256')!=self.manifest['original_complete_proposal_sha256']
                or package.get('original_complete_weight_mesh_sha256')!=self.manifest['original_complete_weight_mesh_sha256']
                or not package.get('no_original_frame_value_or_order_changed')):
                raise ValueError('an exact original public frame slice changed')
            sid=package['plan']['slice_id']
            if sid not in (0,8,15):raise ValueError('only the three explicitly requested original frame slices are needed')
            slices.append(dict(slice_id=sid,slice_manifest_sha256=digest(m),
                actual_original_proposal_sha256=digest(root0/'native/complete-cut-proposal.json.gz'),
                actual_original_weight_mesh_sha256=digest(root0/'frames/exact-weight-and-base-mesh.json')))
        if sorted(x['slice_id'] for x in slices)!=[0,8,15] or any(
            x['actual_original_proposal_sha256']!=self.manifest['original_complete_proposal_sha256']
            or x['actual_original_weight_mesh_sha256']!=self.manifest['original_complete_weight_mesh_sha256'] for x in slices):
            raise ValueError('the exact three original complete frame input bundles changed')
        receipt=dict(original_complete_native_sha256=digest(native),
            actual_artifact_process_sha256=digest(pp),
            separately_reviewed_repository_process_sha256=digest(reviewed),
            only_appended_publication_checkpoint_difference_accepted=True,
            artifact_published_checkpoints=pc,reviewed_published_checkpoints=rc)
        self.state['actual_original_input_receipt']=receipt
        self.state['actual_original_summary_sha256']=summaries
        self.state['actual_original_frame_slices']=slices
        shutil.copyfile(pp,self.evidence/'original-full193-artifact-process.json')
        shutil.copyfile(reviewed,self.evidence/'original-full193-reviewed-repository-process.json')
        small(self.evidence/'exact-original-input-receipts.json',dict(
            original_matrix_process_receipt=receipt,original_frame_slices=slices,
            four_original_matrix_file_sha256=self.manifest['original_full193_matrix_file_sha256'],
            original_input_arrays_unchanged=True))
        return native,pp,reviewed,folder,summaries,receipt

    def previous(self,summaries,receipt):
        root=TOPIC/FOLDER;candidates=[]
        if not root.exists():return None
        for pp in sorted(root.glob('*/process.json')):
            p=read(pp)
            if (p.get('repository')!='Rogerhu12/math-research-public'
                or p.get('worker_source_sha256')!=digest(__file__)
                or p.get('input_manifest_sha256')!=self.args.manifest_sha
                or p.get('actual_original_summary_sha256')!=summaries
                or p.get('actual_original_input_receipt')!=receipt):continue
            records=[x for x in p.get('native_files',[]) if x.get('logical_file')=='native/'+NATIVE]
            if len(records)!=1:continue
            path=self.exact_native(pp.parent,'native/'+NATIVE,p,records[0]['sha256'])
            d=read(path);identity=d.get('identity',{})
            if (d.get('kind')!=KIND or identity.get('source_sha256')!=self.manifest['files'][PRODUCER]
                or identity.get('original_full193_native_sha256')!=OLD_NATIVE
                or identity.get('original_summary_sha256')!=summaries
                or identity.get('actual_original_process_receipt')!=receipt
                or identity.get('original_indices')!=INDICES
                or identity.get('new_inverse_polynomial_degree')!=24
                or identity.get('arithmetic_bits')!=256):continue
            rows=d.get('rows',[])
            if ([r.get('index') for r in rows]!=INDICES[:len(rows)]
                or any(not r.get('complete') or not r.get('array_receipt',{}).get('sha256') for r in rows)):
                raise ValueError('a same-identity same-F matrix prefix is incomplete or out of order')
            child_ok=any(c.get('label')==LABEL and c.get('actual_returncode')==0 for c in p.get('children',[]))
            reused_ok=(p.get('complete') and p.get('original_complete_success_reused_without_child')
                       and p.get('original_success_process_sha256'))
            complete=(d.get('complete') and not d.get('failure') and len(rows)==4
                and d.get('gates') and all(g['passed'] for g in d['gates'])
                and d.get('same_F_local_directional_matrix_Grams_certified') and (child_ok or reused_ok))
            candidates.append(((1 if complete else 0,len(rows)),pp,path,complete))
        return max(candidates,key=lambda x:x[0]) if candidates else None

    def row_brief(self,row):
        return dict(index=row['index'],interval=row['interval'],complete=row.get('complete'),
            seconds=row.get('seconds'),
            complete_endpoint_patch=row['patch']['complete_exact_endpoint_patch_upper'],
            complete_true_generator_difference=row['patch']['true_complete_generator_difference_upper'],
            patched_F_whole_singular_lower=row['patch']['whole_patched_polynomial_singular_lower'],
            inverse_polynomial_difference=row['inverse_polynomial_certificate']['complete_true_patched_F_inverse_minus_C'],
            cross_uniform_error=row['source_definition']['full_true_weighted_cross_source_uniform_error'],
            source_Gram_traces={k:v['complete_trace_upper'] for k,v in row['source_Grams'].items()},
            source_Gram_slacks={k:v['exact_diagonal_slack'] for k,v in row['source_Grams'].items()},
            output_Gram_traces={k:v.get('complete_trace_upper',{'exact_zero':True}) for k,v in row['output_Grams'].items()},
            scientific_array_file=row['array_receipt']['file'],
            scientific_array_sha256=row['array_receipt']['sha256'],
            scientific_array_original_origin=row['array_receipt']['original_public_array_origin'])

    def outcome(self,d):
        return dict(complete=d.get('complete'),failure=d.get('failure'),gates=d.get('gates',[]),
            completed_indices=[r['index'] for r in d.get('rows',[])],
            new_same_F_cells_this_child=d.get('new_same_F_cells_this_child'),
            reused_completed_same_F_cells=d.get('reused_completed_same_F_cells'),
            actual_local_rows=[self.row_brief(r) for r in d.get('rows',[])],
            original_successful_F_cells_recomputed=d.get('original_successful_F_cells_recomputed'),
            original_target_calls=d.get('original_target_calls'),
            full5970_matrix_cover_claimed=False,full_two_boundary_Green_bound_claimed=False,
            unknown_high_or_true_parameter_Schur_claimed=False)

    def execute(self,label,command):
        try:return super().execute(label,command)
        finally:
            native=self.cache/NATIVE
            if native.exists():
                d=read(native);outcome=self.outcome(d);outcome['native_sha256']=digest(native)
                small(self.evidence/'actual-latest-same-F-matrix-Gram-outcome.json',outcome)
                print(json.dumps(dict(complete=d.get('complete'),failure=d.get('failure'),
                    completed_indices=outcome['completed_indices'],native_sha256=digest(native))),flush=True)
                if d.get('failure') and self.log.exists():print(self.log.read_text()[-16000:],flush=True)

    def prepare(self):
        original,pp,reviewed,folder,summaries,receipt=self.inputs()
        native=self.cache/NATIVE;arrays=self.artifact/'matrices';arrays.mkdir(parents=True,exist_ok=True)
        command=[sys.executable,'-u',str(self.science/PRODUCER),
            '--original-native',str(original),'--original-process',str(pp),
            '--reviewed-process',str(reviewed),'--original-arrays',str(self.args.matrix_artifact.resolve()/'matrices'),
            '--summary-dir',str(folder),'--arrays',str(arrays),'--out',str(native),'--degree','24','--bits','256']
        for root in self.args.frame_slice:command+=['--frame-slice',str(root.resolve())]
        previous=self.previous(summaries,receipt)
        if previous:
            _,prior_pp,path,complete=previous
            shutil.copyfile(prior_pp,self.evidence/'original-same-identity-same-F-process.json')
            small(self.evidence/'original-same-F-prefix-reuse.json',dict(
                original_process_sha256=digest(prior_pp),original_native_sha256=digest(path),
                original_process_complete=read(prior_pp).get('complete'),original_mathematics_complete=complete,
                original_failure_preserved=read(prior_pp).get('failure'),
                successful_mathematics_reused_independently_of_publication_completion=True,
                old_new_array_bytes_keep_original_run_attempt_artifact_origins=True))
            if complete:
                shutil.copyfile(path,native);self.reused_complete=True
                self.state['original_success_process_sha256']=digest(prior_pp)
            else:
                prefix=self.work/'original-exact-same-F-matrix-prefix.json.gz'
                shutil.copyfile(path,prefix);command+=['--resume',str(prefix)]
        self.publish()
        if not self.reused_complete:self.execute(LABEL,command)
        d=read(native)
        if (d.get('kind')!=KIND or not d.get('complete') or d.get('failure')
            or d.get('identity',{}).get('source_sha256')!=self.manifest['files'][PRODUCER]
            or d['identity'].get('original_full193_native_sha256')!=OLD_NATIVE
            or d['identity'].get('original_summary_sha256')!=summaries
            or d['identity'].get('actual_original_process_receipt')!=receipt
            or [r['index'] for r in d.get('rows',[])]!=INDICES
            or not d.get('gates') or not all(g['passed'] for g in d['gates'])
            or not d.get('same_F_local_directional_matrix_Grams_certified')
            or d.get('original_successful_F_cells_recomputed')!=0 or d.get('original_target_calls')!=0
            or d.get('full5970_matrix_cover_claimed') or d.get('full_two_boundary_Green_bound_claimed')):
            raise ValueError('the actual same-F local source-Gram pilot did not finish within its declared scope')
        origins=[]
        for row in d['rows']:
            entry=row['array_receipt'];origin=entry['original_public_array_origin']
            current=(str(origin['run_id'])==str(self.state['run_id'])
                     and str(origin['run_attempt'])==str(self.state['run_attempt']))
            if current:
                path=arrays/entry['file']
                if not path.exists() or path.stat().st_size!=entry['bytes'] or digest(path)!=entry['sha256']:
                    raise ValueError('a newly successful matrix Gram array is absent or changed')
            origins.append(dict(index=row['index'],available_in_this_artifact=current,receipt=entry))
            small(self.evidence/f'complete-same-F-cell-{row["index"]:05d}-summary.json',
                dict(actual_row=self.row_brief(row),source_Grams=row['source_Grams'],
                    output_Grams=row['output_Grams'],patch=row['patch'],
                    source_definition=row['source_definition'],inverse=row['inverse_polynomial_certificate'],
                    complete_native_sha256=digest(native)))
        summary=self.outcome(d);summary.update(native_sha256=digest(native),seconds=d['seconds'],
            original_process_receipt=receipt,complete_native_retained=True,
            actual_new_same_F_cells_this_child=0 if self.reused_complete else d['actual_new_same_F_cells'],
            original_complete_success_reused_without_child=self.reused_complete)
        small(self.evidence/'complete-same-F-matrix-Gram-pilot-summary.json',summary)
        small(self.evidence/'complete-same-F-array-origin-inventory.json',dict(
            arrays=origins,old_array_bytes_not_recomputed_or_relabelled=True))
        self.state.update(complete=True,complete_native_sha256=digest(native),
            actual_scientific_gates=len(d['gates']),actual_complete_same_F_cells=4,
            complete_source_channels_per_cell=3,same_F_local_directional_matrix_Grams_certified=True,
            actual_new_same_F_cells_this_child=summary['actual_new_same_F_cells_this_child'],
            original_complete_success_reused_without_child=self.reused_complete,
            all_new_arrays_have_exact_origin_receipts=True,
            matrix_arrays_retained_only_in_public_Actions_artifacts=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','work','artifact-dir','matrix-artifact'):
        p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--frame-slice',type=Path,action='append',required=True)
    p.add_argument('--compute-minutes',type=int,default=100)
    p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='same-F-triangular-source-Gram-pilot';a.mode='prepare';a.first=0;a.end=0
    a.recovery_manifest=None;a.recovery_sha=None
    worker=SameFWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):
        signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
