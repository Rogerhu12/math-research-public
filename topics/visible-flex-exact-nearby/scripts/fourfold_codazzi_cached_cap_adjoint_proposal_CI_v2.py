#!/usr/bin/env python3
"""Run a new complete97 cap-adjoint proposal from exact public cached scalar jets.

No old target or forward cap trial is rerun. Scientific proposal arrays stay
in this repository's Actions artifacts; only bounded receipts and native
outcomes are published. Real pulls and both README diff checks use the
separately reviewed driver every10minutes, including artifact restoration.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,shutil,signal,sys,time
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_complete_directional_matrix_Green_CI import MatrixGreenWorker
from fourfold_codazzi_cap128_CI_worker import read,digest
from fourfold_codazzi_phase_high7_CI_worker import TOPIC,REPO

REL='topics/visible-flex-exact-nearby/'
PUBLIC='Rogerhu12/math-research-public'
PRODUCER=REL+'scripts/fourfold_codazzi_cached_cap_adjoint_proposal_v2.py'
FOLDER='notes/cached_cap_adjoint_proposal_v2_ci'
KIND='actual_cached_scalar_complete97_physical_adjoint_Hermite_proposal_v2'
NATIVE='complete97-cached-physical-adjoint-proposal-v2.json.gz'
LABEL='new_complete257_state97_input_physical_adjoint_QR_from_original7908_cached_scalar_jets'
ORIGINAL_MANIFEST=REL+'notes/2026-11-15-R133-complete-directional-matrix-Green-CI-inputs.json'
ORIGINAL_MANIFEST_SHA='3350a96fbea47ee33bb09cb6602cb1e978e8ba00a034c7f735dfb60bade99910'
CANDIDATE=REL+'data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json'
REPAIR=REL+'notes/2026-11-14-R133-final-exact-continuous-value-repair-native.json.gz'
QVECTOR=REL+'notes/2026-11-13-R133-regular-r25over8-q256-floating.json'
QUARTER='770106a925812df4fc380785ca3e715b2a30a649a355fb888e0dcbe0e6a65298'
PLAN='406e3e5331720a3f87f2b5f53c2e7d2988bea25b7537d650157ed97278e3073a'
POINT='41156aa8ac5b124b2ccca96e2f52b210edf1a3f5c170fdf839e66bf0602725b8'


def small(path,d):
    raw=(json.dumps(d,ensure_ascii=False,indent=2)+'\n').encode()
    if len(raw)>60000:raise ValueError('one adjoint evidence text exceeds60000 UTF8 bytes')
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(raw)


def artifact_name(run,attempt):return f'visible-exact-cached-cap-adjoint-proposal-v2-{run}-{attempt}'


class AdjointProposalWorker(MatrixGreenWorker):
    def __init__(self,a):
        super().__init__(a)
        self.name=f'run-{self.run_label}-cached-cap-adjoint-proposal-v2'
        self.dest=TOPIC/FOLDER/self.name;self.native_name=NATIVE
        self.proposal_state=self.artifact/'proposal-state';self.proposal_state.mkdir(parents=True,exist_ok=True)
        self.inventory_saved=False
        self.state.update(kind='actual_public_cached_complete97_cap_adjoint_proposal_process_v2',
            worker_source_sha256=digest(__file__),phase='new-adjoint-proposal',
            exact_repaired_centre_definition='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47',
            physical_state_dimension=257,independent_input_columns=97,
            original_scalar_whole_domains_recomputed=0,original_native_point_domains_recomputed=0,
            original_forward_cap_columns_recomputed_or_transposed_as_certificate=False,
            complete_continuous_adjoint_bound_proved=False,
            complete_full_cap_high_to_low_bound_proved=False,complete_infinite_BVP_inverse_proved=False,
            full_actual_scientific_state_saved_on_success_or_failure=True,
            publication_failure_does_not_invalidate_prior_mathematical_success=True)

    def check_inputs(self):
        # Called before science_copy: only the already verified repository
        # copy may be inspected at this lifecycle stage.
        ReviewedBodyWorker.check_inputs(self)
        if self.manifest.get('kind')!='cached_scalar_complete97_cap_adjoint_proposal_public_inputs_v2':
            raise ValueError('the separate adjoint proposal manifest is required')
        old=read(REPO/ORIGINAL_MANIFEST)
        if (digest(REPO/ORIGINAL_MANIFEST)!=ORIGINAL_MANIFEST_SHA
            or any(self.manifest['files'].get(k)!=v for k,v in old['files'].items())):
            raise ValueError('one original234 input pin changed')
        previous=read(REPO/self.manifest['original_adjoint_proposal_manifest'])
        if (digest(REPO/self.manifest['original_adjoint_proposal_manifest'])!=self.manifest['original_adjoint_proposal_manifest_sha256']
            or any(self.manifest['files'].get(k)!=v for k,v in previous['files'].items())):
            raise ValueError('one original247 adjoint proposal input pin changed')

    def one_original(self,run,name,logical,expected):
        root=self.download(run,name);pp=root/'process.json';p=read(pp)
        native=self.exact_native(root,logical,p,expected)
        self.record_process(pp,f'original-processes/{name}.json')
        return native,pp

    def inputs(self):
        inputs={'candidate':self.science/CANDIDATE,'repair':self.science/REPAIR,
            'q-vector':self.science/QVECTOR}
        plan,pp=self.one_original(43623547711,'visible-exact-complete-quarter-cap-plan-43623547711-1',
            'native/complete1977-fixed-eta-quarter-plan.json.gz',PLAN)
        complete,cp=self.one_original(43626024582,'visible-exact-quarter-inlet-recovery-finish-43626024582-1',
            'native/complete1977-fixed-eta-quarter-cap-sources.json.gz',QUARTER)
        point,mp=self.one_original(43635264409,'visible-exact-missing-native-point-Hessian-43635264409-1',
            'native/complete-missing-native-point-Hessian.json.gz',POINT)
        inputs.update({'quarter-plan':plan,'quarter-plan-process':pp,'quarter':complete,
            'quarter-process':cp,'native-points':point,'native-points-process':mp})
        finish=read(complete);receipts=finish.get('range_receipts',[])
        expected={(0,256),(256,512),(512,768),(768,1024),(1024,1280),
            (1280,1536),(1536,1792),(1792,1977)}
        if {tuple(x['range']) for x in receipts}!=expected or len(receipts)!=8:
            raise ValueError('the complete original7908 cover needs its exact eight range receipts')
        for receipt in receipts:
            first,end=receipt['range'];run=receipt['actual_workflow_run'];attempt=receipt['actual_workflow_attempt']
            if (first,end) in {(0,256),(1792,1977)}:
                name=f'visible-exact-quarter-inlet-recovery-range-{first}-{end}-{run}-{attempt}'
            else:name=f'visible-exact-complete-quarter-cap-range-{first}-{end}-{run}-{attempt}'
            native,process=self.one_original(run,name,
                f'native/new-fixed-eta-quarter-domains-{first:04d}-{end:04d}.json.gz',receipt['native_sha256'])
            if digest(process)!=receipt['actual_original_process_sha256']:
                raise ValueError('one exact original range artifact process changed')
            inputs[f'range-{first}-{end}']=native;inputs[f'range-{first}-{end}-process']=process
        if len(inputs)!=25:raise ValueError('the exact complete original scientific input list changed')
        return inputs

    def restore_original_selected_scalars(self,input_sha):
        # The first run already completed both7908 input gates and the
        # scalar selection before the piece-selector failure. Preserve those
        # original selected bytes; no BLAS reselection or QR block is needed.
        root=self.download(43662395328,'visible-exact-cached-cap-adjoint-proposal-43662395328-1')
        pp=root/'process.json';p=read(pp)
        expected='f6cdd51f5776ea66435212188cd5db2518f225c24c240823ee7f726e389757d0'
        native=self.exact_native(root,'native/complete97-cached-physical-adjoint-proposal.json.gz',p,expected)
        d=read(native)
        if (p.get('worker_source_sha256')!='f83b29bcf559820a685f3cc66686126a08ac7ed0b1e2e0fc4a45f7cf6d70d19b'
            or p.get('input_manifest_sha256')!='a5260c946c731d3b50c3bdb2a76fa7aec7b653ad3bec6c9eb844b8bb37be982d'
            or d.get('source_sha256')!='5cdff6d9f51db3e99a3a89738001856182b155ae46819c6c796acdceb8480a89'
            or d.get('input_sha256')!=input_sha or d.get('complete')
            or d.get('failure')!={'type':'ValueError','message':'a new collocation interval crosses an actual original candidate cubic join'}
            or d.get('counted_new_blocks_in_this_child')!=0 or d.get('case') is not None
            or len(d.get('gates',[]))!=2 or not all(g.get('passed') for g in d['gates'])
            or not any(c.get('label')==LABEL and c.get('actual_returncode')==1 for c in p.get('children',[]))):
            raise ValueError('the exact original zero-QR piece-selector failure is required')
        original=root/'proposal-state';receipt_path=original/'selected-intrinsic-proposal.json'
        receipt=read(receipt_path);array=original/'selected-intrinsic-proposal.npz'
        if (not receipt.get('exact_binary64_selection_only') or not receipt.get('no_new_target_evaluation')
            or digest(array)!=receipt.get('sha256') or not receipt.get('original7908_jet_identity')):
            raise ValueError('the original already completed scalar selection is missing or changed')
        for source in (receipt_path,array):
            target=self.proposal_state/source.name
            if target.exists() and digest(target)!=digest(source):
                raise ValueError('an original selected scalar cache would be replaced')
            if not target.exists():shutil.copyfile(source,target)
        self.record_process(pp,'original-zero-QR-adjoint-failure-artifact-process.json')
        self.record_process(receipt_path,'original-selected-intrinsic-proposal.json')
        small(self.evidence/'original-zero-QR-failure-and-exact-selection-reuse.json',dict(
            original_workflow_run=43662395328,original_actual_process_sha256=digest(pp),
            original_failure_native_sha256=expected,original_scientific_gates_passed=2,
            original_completed_QR_blocks=0,original_failure=d['failure'],
            selected_intrinsic_receipt_sha256=digest(receipt_path),selected_intrinsic_array_sha256=digest(array),
            original7908_jet_identity=receipt['original7908_jet_identity'],
            already_selected_array_recomputed=False,original_inputs_and_parameter_scope_unchanged=True))
        self.state.update(original_piece_selector_failure_native_sha256=expected,
            original_already_selected_intrinsic_array_sha256=digest(array),
            original_completed_QR_blocks_recomputed=0,
            one_sided_piece_is_now_chosen_from_exact_left_node=True,
            original_complete_two_endpoint_containment_gate_unchanged=True)

    def math_success(self,p,d):
        child=any(c.get('label')==LABEL and c.get('actual_returncode')==0 for c in p.get('children',[]))
        reused=bool(p.get('original_complete_success_reused_without_child') and p.get('original_success_process_sha256'))
        return bool((child or reused) and d.get('complete') and not d.get('failure')
            and d.get('kind')==KIND and d.get('source_sha256')==self.manifest['files'][PRODUCER]
            and d.get('gates') and all(g.get('passed') for g in d['gates'])
            and d.get('actual_finite_backward_check',{}).get('passed')
            and not d.get('mathematical_certificate')
            and not d.get('complete_continuous_adjoint_bound_proved')
            and not d.get('complete_full_cap_high_to_low_bound_proved'))

    def previous(self,input_sha):
        root=TOPIC/FOLDER;candidates=[]
        if not root.exists():return None
        for pp in sorted(root.glob('*/process.json')):
            p=read(pp)
            if (p.get('repository')!=PUBLIC or p.get('worker_source_sha256')!=digest(__file__)
                or p.get('input_manifest_sha256')!=self.args.manifest_sha
                or p.get('actual_input_sha256')!=input_sha
                or str(p.get('run_id'))==str(self.state['run_id'])):continue
            records=[x for x in p.get('native_files',[]) if x.get('logical_file')=='native/'+NATIVE]
            if len(records)!=1 or not p.get('proposal_state_receipt_sha256'):continue
            native=self.exact_native(pp.parent,'native/'+NATIVE,p,records[0]['sha256']);d=read(native)
            if (d.get('kind')!=KIND or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
                or d.get('input_sha256')!=input_sha or not d.get('case')):continue
            progress=d.get('actual_checkpoint_progress',{})
            stage=(3 if progress.get('matrix-RHS/independent-check.json',{}).get('complete')
                else 2 if progress.get('matrix-RHS/progress.json',{}).get('stage')=='complete'
                else 1 if progress.get('factor.json',{}).get('complete') else 0)
            rank=(int(self.math_success(p,d)),stage,int(d.get('counted_new_blocks_in_this_child',0)))
            candidates.append((rank,pp,native,d))
        return max(candidates,key=lambda x:x[0]) if candidates else None

    def restore_previous(self,previous,input_sha):
        _,reviewed_process,reviewed_native,reviewed_doc=previous
        rp=read(reviewed_process);run=rp['run_id'];attempt=rp.get('run_attempt','1')
        root=self.download(run,artifact_name(run,attempt));pp=root/'process.json';p=read(pp)
        if (p.get('worker_source_sha256')!=digest(__file__)
            or p.get('input_manifest_sha256')!=self.args.manifest_sha
            or p.get('actual_input_sha256')!=input_sha
            or p.get('proposal_state_receipt_sha256')!=rp['proposal_state_receipt_sha256']):
            raise ValueError('the original proposal artifact has another scientific or state receipt identity')
        index=root/'evidence/proposal-state-inventory-index.json'
        if digest(index)!=p['proposal_state_receipt_sha256']:
            raise ValueError('the original complete QR state inventory changed')
        receipt=read(index)
        if (receipt.get('repository')!=PUBLIC or receipt.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or receipt.get('input_sha256')!=input_sha or receipt.get('case')!=reviewed_doc['case']):
            raise ValueError('the exact proposal state belongs to another mathematical object')
        native_records=[x for x in p.get('native_files',[]) if x.get('logical_file')=='native/'+NATIVE]
        if len(native_records)!=1:raise ValueError('the original proposal artifact has no exact native receipt')
        native=self.exact_native(root,'native/'+NATIVE,p,native_records[0]['sha256']);d=read(native)
        if (d.get('kind')!=KIND or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or d.get('input_sha256')!=input_sha or d.get('case')!=receipt['case']):
            raise ValueError('the actual original proposal native has changed identity')
        seen=set();count=0
        for item in receipt['parts']:
            part=root/'evidence'/item['file']
            if Path(item['file']).name!=item['file'] or digest(part)!=item['sha256']:
                raise ValueError('one original state inventory part changed')
            block=read(part)
            if block['first']!=count:raise ValueError('the exact state inventory has a gap')
            for entry in block['files']:
                relative=Path(entry['file'])
                if relative.is_absolute() or '..' in relative.parts or str(relative) in seen:
                    raise ValueError('one original QR state path is unsafe or repeated')
                source=root/'proposal-state'/relative
                if source.stat().st_size!=entry['bytes'] or digest(source)!=entry['sha256']:
                    raise ValueError('one actual original factor, RHS or Hermite array changed')
                destination=self.proposal_state/relative;destination.parent.mkdir(parents=True,exist_ok=True)
                if destination.exists() and digest(destination)!=entry['sha256']:
                    raise ValueError('an original proposal state would be replaced by different bytes')
                if not destination.exists():shutil.copyfile(source,destination)
                seen.add(str(relative));count+=1;self.pull_during_download()
        if count!=receipt['files']:raise ValueError('the exact complete state inventory count changed')
        self.record_process(pp,'original-proposal-artifact-process.json')
        self.record_process(reviewed_process,'original-proposal-reviewed-process.json')
        prefix=self.work/'original-adjoint-native.json.gz';shutil.copyfile(native,prefix)
        complete=self.math_success(p,d)
        small(self.evidence/'original-adjoint-proposal-reuse.json',
            dict(original_actual_artifact_process_sha256=digest(pp),
                original_reviewed_repository_process_sha256=digest(reviewed_process),
                original_native_sha256=digest(native),original_inventory_sha256=digest(index),
                exact_state_files_restored=count,original_process_complete=p.get('complete'),
                original_mathematics_complete=complete,original_failure_preserved=d.get('failure'),
                original_atomic_checkpoint_progress=d.get('actual_checkpoint_progress'),
                complete_mathematics_not_repeated_after_publication_failure=True))
        self.state['original_proposal_state_files_restored']=count
        self.state['original_proposal_state_receipt_sha256']=digest(index)
        if complete:
            shutil.copyfile(native,self.cache/NATIVE);self.reused_complete=True
            self.state['original_success_process_sha256']=digest(pp)
        elif d.get('failure'):
            raise RuntimeError('the original exact mathematical failure is retained; do not repeat it unchanged: '+str(d['failure']))
        return prefix

    def state_inventory(self):
        native=self.cache/NATIVE
        if self.inventory_saved or not native.exists():return
        d=read(native)
        if not d.get('case'):return
        entries=[]
        for path in sorted(self.proposal_state.rglob('*')):
            if not path.is_file() or path.name.endswith('.partial'):continue
            relative=path.relative_to(self.proposal_state)
            entries.append(dict(file=str(relative),bytes=path.stat().st_size,sha256=digest(path)))
        if not entries:return
        parts=[]
        for first in range(0,len(entries),80):
            name=f'proposal-state-inventory-{first//80:04d}.json';path=self.evidence/name
            small(path,dict(first=first,total=len(entries),files=entries[first:first+80],
                exact_original_checkpoint_bytes=True))
            parts.append(dict(file=name,sha256=digest(path),bytes=path.stat().st_size))
        index=self.evidence/'proposal-state-inventory-index.json'
        small(index,dict(repository=PUBLIC,kind='exact_complete_or_partial_adjoint_proposal_state_v1',
            source_sha256=self.manifest['files'][PRODUCER],
            input_sha256=d['input_sha256'],case=d['case'],files=len(entries),parts=parts,
            original_native_sha256=digest(native),math_complete=d.get('complete'),
            original_failure_preserved=d.get('failure'),large_arrays_only_in_public_Actions_artifact=True))
        self.state['proposal_state_receipt_sha256']=digest(index)
        self.state['actual_proposal_state_file_count']=len(entries)
        self.inventory_saved=True

    def outcome(self,d):
        keys=('kind','complete','failure','gates','stage','seconds','radial_nodes','collocation_intervals',
            'case','original_scalar_domain_count','original_native_midpoints_count',
            'counted_new_blocks_in_this_child','atomic_batches_completed','actual_checkpoint_progress',
            'actual_finite_backward_check','end_model_condition_2','new_target_evaluations',
            'all_original7908_scalar_domains_recomputed','all_original64_native_points_recomputed',
            'original_forward_cap_columns_recomputed_or_transposed_as_certificate',
            'complete_continuous_adjoint_bound_proved','complete_full_cap_high_to_low_bound_proved',
            'mathematical_certificate','maximum_floating_inverse_angle_residual','minimum_floating_inverse_angle_jacobian')
        return {k:d.get(k) for k in keys}

    def snapshot(self):
        native=self.cache/NATIVE
        if native.exists():
            raw=native.read_bytes();d=json.loads(gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw)
            brief=self.outcome(d);brief['native_sha256']=hashlib.sha256(raw).hexdigest()
            brief['latest_actual_readme_check']=self.state.get('readme_checks',[])[-1:]
            small(self.evidence/'actual-latest-adjoint-proposal-outcome.json',brief)
            self.state['latest_scientific_native_sha256']=brief['native_sha256']
            self.state['actual_checkpoint_progress']=d.get('actual_checkpoint_progress')
            if self.child is None or self.child.poll() is not None:self.state_inventory()
        ReviewedBodyWorker.snapshot(self)

    def execute(self,label,command):
        self.inventory_saved=False
        try:return ReviewedBodyWorker.execute(self,label,command)
        finally:
            if self.child is None or self.child.poll() is not None:self.state_inventory()
            native=self.cache/NATIVE
            if native.exists():
                d=read(native);brief=self.outcome(d);brief['native_sha256']=digest(native)
                small(self.evidence/'actual-latest-adjoint-proposal-outcome.json',brief)
                print(json.dumps(brief),flush=True)
                if d.get('failure') and self.log.exists():print(self.log.read_text()[-16000:],flush=True)

    def prepare(self):
        inputs=self.inputs();input_sha={k:digest(v) for k,v in inputs.items()}
        self.state['actual_input_sha256']=input_sha
        self.restore_original_selected_scalars(input_sha)
        bundle=self.work/'actual-original-adjoint-inputs.json'
        small(bundle,dict(repository=PUBLIC,kind='cached_adjoint_trial_original_inputs_v1',
            files={k:dict(path=str(v),sha256=input_sha[k]) for k,v in inputs.items()}))
        prefix=None;old=self.previous(input_sha)
        if old:prefix=self.restore_previous(old,input_sha)
        command=[sys.executable,'-u',str(self.science/PRODUCER),
            '--input-index',str(bundle),'--state-dir',str(self.proposal_state),
            '--out',str(self.cache/NATIVE),'--span','8','--batch-blocks','256']
        if prefix and not self.reused_complete:command+=['--resume',str(prefix)]
        self.publish()
        if not self.reused_complete:self.execute(LABEL,command)
        d=read(self.cache/NATIVE)
        if (d.get('source_sha256')!=self.manifest['files'][PRODUCER] or d.get('input_sha256')!=input_sha
            or not d.get('complete') or d.get('failure') or d.get('kind')!=KIND
            or not d.get('gates') or not all(g.get('passed') for g in d['gates'])
            or not d.get('actual_finite_backward_check',{}).get('passed')
            or d.get('mathematical_certificate') or d.get('complete_continuous_adjoint_bound_proved')
            or d.get('complete_full_cap_high_to_low_bound_proved')):
            raise ValueError('the new complete97 finite adjoint trial did not pass its declared scope')
        self.state_inventory();brief=self.outcome(d)
        brief.update(native_sha256=digest(self.cache/NATIVE),exact_input_sha256=input_sha,
            proposal_state_inventory_sha256=self.state.get('proposal_state_receipt_sha256'),
            original_complete_success_reused_without_child=self.reused_complete,
            original_target_evaluations=0,all_original_7908_whole_and64_point_cells_reused=True)
        small(self.evidence/'complete97-cached-adjoint-proposal-summary.json',brief)
        self.state.update(complete=True,complete_native_sha256=digest(self.cache/NATIVE),
            actual_scientific_gates=len(d['gates']),complete_new_finite_adjoint_proposal=True,
            original_complete_success_reused_without_child=self.reused_complete,
            complete_continuous_adjoint_bound_proved=False,
            complete_full_cap_high_to_low_bound_proved=False,complete_infinite_BVP_inverse_proved=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','work','artifact-dir'):
        p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--compute-minutes',type=int,default=320)
    p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='cached-cap-adjoint-proposal';a.mode='prepare';a.phase='proposal'
    a.first=0;a.end=7908;a.matrix_run=None;a.matrix_attempt=None
    a.recovery_manifest=None;a.recovery_sha=None
    worker=AdjointProposalWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):
        signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
