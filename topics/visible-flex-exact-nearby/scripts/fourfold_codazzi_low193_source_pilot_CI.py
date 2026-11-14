#!/usr/bin/env python3
"""Reuse saved scalar jets and compute only new selected low193 projections."""
from __future__ import annotations
import argparse,shutil,signal,sys
from pathlib import Path
from types import SimpleNamespace
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_body_mean_CI_finish import CompleteMeanWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC,save
from fourfold_native_lossless_parts import restore

REL='topics/visible-flex-exact-nearby/'
OLD_MANIFEST='c214f800a5094c905c554e9053c52567d5ae5d76be41ac2e3fe9d673b396d784'
BODY='a4f31dccc4b54661b43fc06bac59b6afbb4fa2d6d19614f68f71e044be6e5870'
BODY_PROCESS='0a5dc06520bad5a1230b65cba6e895e998e1f3ce6a32a65d9ffa8800b8ea1a9e'
REPAIR='05e0493dbe55490adec8fb6603e0ec431d1bc03f051aec86be8a78741f60f0a4'
REPAIR_PROCESS='16de872ce106e05b6add99d8406598de3cc87b94f4533a9fc3bb46294c66366a'
NATIVE='cached-scalar-low193-source-projection-pilot.json.gz'
PRODUCER=REL+'scripts/fourfold_codazzi_cached_scalar_low193_source_pilot.py'
LABEL='actual_new_selected_low193_and_high97_to160_source_projections_from_saved_scalar_jets'


class LowSourcePilotWorker(ReviewedBodyWorker):
    def __init__(self,args):
        super().__init__(args)
        self.name=f'run-{self.run_label}-cached-scalar-low193-source-pilot'
        self.dest=TOPIC/'notes/low193_source_pilot_ci'/self.name
        self.state.update(kind='actual_public_cached_scalar_low193_source_projection_pilot_process_v1',
            worker_source_sha256=digest(__file__),original_complete_body_run=43583838026,
            original_complete_body_mean_run=43586413510,actual_complete_repair_source_run=43597921732,
            original_target_primitives_rerun=0,original_mean_flows_recomputed=0,
            original_trial_reconstructions_recomputed=0,complete_body_projection_cover=False,
            exact_affine_parameter_offset='0',physical_parameter='fixed original physical eta0 and nu',
            whole_original_parameter_half_width=None,
            actual_finite193_response_error_bound_proved=False,complete_infinite_inverse_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='cached_scalar_low193_known_source_projection_pilot_public_inputs_v1':
            raise ValueError('the separate actual cached scalar projection-pilot manifest is required')

    def best_original_prefix(self,expected_inputs):
        root=TOPIC/'notes/low193_source_pilot_ci'
        candidates=[]
        if not root.exists():return None
        for process_path in sorted(root.glob('*/process.json')):
            process=read(process_path)
            if (process.get('repository')!='Rogerhu12/math-research-public'
                or process.get('worker_source_sha256')!=digest(__file__)
                or process.get('input_manifest_sha256')!=self.args.manifest_sha
                or process.get('actual_scientific_input_sha256')!=expected_inputs):continue
            records=[x for x in process.get('native_files',[]) if x.get('logical_file')=='native/'+NATIVE]
            if len(records)!=1:continue
            item=records[0];native=process_path.parent/'native'/NATIVE
            if not native.exists():
                if 'lossless_manifest' not in item:continue
                native=self.work/('original-pilot-prefix-'+item['sha256']+'.json.gz')
                if not native.exists():restore(process_path.parent/item['lossless_manifest'],native)
            if digest(native)!=item['sha256']:raise ValueError('an original actual projected-source prefix changed')
            old=read(native)
            if (old.get('source_sha256')!=self.manifest['files'][PRODUCER]
                or old.get('input_sha256')!=expected_inputs):continue
            complete_rows=old.get('rows',[])
            if not complete_rows or not all(x.get('actual_projection_complete') for x in complete_rows):continue
            if old.get('complete') and not any(c.get('label')==LABEL and c.get('actual_returncode')==0
                for c in process.get('children',[])):continue
            candidates.append((len(complete_rows),process_path,native,old))
        if not candidates:return None
        return max(candidates,key=lambda x:x[0])

    def prepare(self):
        original_path=self.science/self.manifest['original_body_manifest']
        if digest(original_path)!=OLD_MANIFEST:raise ValueError('the original complete body manifest changed')
        original=read(original_path)
        audit_dir=self.evidence/'original-input-audit';audit_dir.mkdir(exist_ok=True)
        audit=SimpleNamespace(
            args=SimpleNamespace(prepared=self.args.prepared,manifest_sha=OLD_MANIFEST,
                original_run=43583838026,original_attempt=1,previous_artifacts=self.args.previous_artifacts),
            manifest=original,science=self.science,science_topic=self.science_topic,evidence=audit_dir,state={})
        # These two existing methods only restore byte-identical original
        # inputs and audit the old complete cover. No scientific row runs.
        CompleteMeanWorker.restore_original_bundle(audit)
        parts=CompleteMeanWorker.original_complete_parts(audit)
        actuals={
            'body':(self.args.body_artifact,'native/complete-correlated-body-and-mean-errors.json.gz',
                BODY,BODY_PROCESS,43586413510),
            'repair-source':(self.args.repair_artifact,'native/complete-known-response-centre-repair-source.json.gz',
                REPAIR,REPAIR_PROCESS,43597921732)}
        resolved={}
        for label,(root,relative,native_sha,process_sha,run_id) in actuals.items():
            root=root.resolve();process=read(root/'process.json');native=root/relative
            if (digest(native)!=native_sha or digest(root/'process.json')!=process_sha
                or str(process.get('run_id'))!=str(run_id) or not process.get('complete')
                or process.get('failure') or process.get('repository')!='Rogerhu12/math-research-public'
                or not process.get('children') or any(c.get('actual_returncode')!=0 for c in process['children'])):
                raise ValueError('the exact actually successful original '+label+' input is required')
            process_name='body-process' if label=='body' else 'repair-process'
            resolved[label]=(native,root/'process.json',process_name)
            shutil.copyfile(root/'process.json',self.evidence/('original-'+process_name+'.json'))
        candidate=self.science/original['published_candidate']
        response=Path(original['row_identity']['full_trials']['response']['path'])
        expected_inputs={'original-manifest':digest(original_path),'candidate':digest(candidate),
            'response':digest(response)}
        for label,(path,process,process_name) in resolved.items():
            expected_inputs[label]=digest(path);expected_inputs[process_name]=digest(process)
        self.state['actual_scientific_input_sha256']=expected_inputs
        self.state['all_original_40_parts_and_7721_scalar_rows_verified']=True
        self.publish()
        native=self.cache/NATIVE
        previous=self.best_original_prefix(expected_inputs)
        command=[sys.executable,'-u',str(self.science/PRODUCER),'--original-manifest',str(original_path),
            '--candidate',str(candidate),'--response',str(response),'--parts',*[str(x) for x in parts],
            '--out',str(native)]
        for label,(path,process,process_name) in resolved.items():
            command.extend(['--'+label,str(path),'--'+process_name,str(process)])
        if previous:
            count,original_process,old,prior=previous
            shutil.copyfile(original_process,self.evidence/'original-projected-source-prefix-process.json')
            self.state.update(original_completed_pilot_rows_reused=count,
                original_pilot_prefix_sha256=digest(old),original_pilot_failure_retained=prior.get('failure'))
            if prior.get('complete') and not prior.get('failure'):
                shutil.copyfile(old,native)
                self.state['actual_new_projection_child_executed']=False
            else:
                command.extend(['--resume',str(old)])
                self.execute(LABEL,command);self.state['actual_new_projection_child_executed']=True
        else:
            self.execute(LABEL,command);self.state['actual_new_projection_child_executed']=True
        result=read(native)
        if (not result.get('complete') or result.get('failure') or not result.get('selected_cells_complete')
            or result.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or result.get('input_sha256')!=expected_inputs
            or result.get('complete_body_projection_cover')
            or result.get('actual_finite193_response_error_bound_proved')
            or result.get('complete_infinite_inverse_proved')
            or not all(x['passed'] for x in result['gates'])):
            raise ValueError('the actual selected projection-pilot result failed or exceeded its scope')
        summary={key:value for key,value in result.items() if key!='rows'}
        summary['rows']=[dict(common_row=row['common_row'],interval=row['interval'],
            original_full160_L2_sup=row['original_complete_nonmean_residual_bound']['L2_sup'],
            original_full160_L2_radial=row['original_complete_nonmean_residual_bound']['L2_L2_radial'],
            new_low193_L2_sup=row['repaired_low193_complete_residual_L2_sup'],
            new_low193_L2_radial=row['repaired_low193_complete_residual_L2_radial'],
            high97_to160_L2_sup=row['fresh_high97_through160_original_background_nonmean_residual']['L2_sup'],
            uncorrected_low193_L2_sup=row['fresh_low193_uncorrected_trial_residual']['L2_sup'],
            complete_mean_error=row['same_original_completed_mean_error'],
            low_uniform_remainders=row['low_component_uniform_A0_remainders'],
            new_repair_fee=row['complete_new_repair_source_pair_A0_sup'],
            seconds=row['seconds']) for row in result['rows']]
        summary['native_sha256']=digest(native)
        save(self.evidence/'cached-scalar-low193-source-projection-pilot-summary.json',summary)
        self.state.update(complete=True,complete_native_sha256=digest(native),
            actual_selected_original_rows=result['selected_original_rows'],
            actual_selected_projection_gates=len(result['gates']),
            complete_body_projection_cover=False,unknown_high_inputs_not_removed=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','prepared','previous-artifacts','body-artifact','repair-artifact','work','artifact-dir'):
        p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--compute-minutes',type=int,default=30);p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='cached-low193-source-pilot';a.mode='prepare';a.first=0;a.end=0
    a.recovery_manifest=None;a.recovery_sha=None
    worker=LowSourcePilotWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
