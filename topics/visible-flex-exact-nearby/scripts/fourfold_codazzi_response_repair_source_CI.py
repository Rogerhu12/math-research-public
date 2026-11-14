#!/usr/bin/env python3
"""Pay only the new centre-repair fee in the original complete known response.

The successful original trial bundle, all forty complete residual parts,
and the completed scalar means are reused exactly. The old finalizer's
input-only audit is reused without executing its mean consumer.
"""
from __future__ import annotations
import argparse,shutil,signal,sys
from pathlib import Path
from types import SimpleNamespace
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_body_mean_CI_finish import CompleteMeanWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC,save

REL='topics/visible-flex-exact-nearby/'
ORIGINAL_MANIFEST='c214f800a5094c905c554e9053c52567d5ae5d76be41ac2e3fe9d673b396d784'
BODY='a4f31dccc4b54661b43fc06bac59b6afbb4fa2d6d19614f68f71e044be6e5870'
BODY_PROCESS='0a5dc06520bad5a1230b65cba6e895e998e1f3ce6a32a65d9ffa8800b8ea1a9e'


class RepairSourceWorker(ReviewedBodyWorker):
    def __init__(self,args):
        super().__init__(args)
        self.name=f'run-{self.run_label}-complete-known-response-centre-repair'
        self.dest=TOPIC/'notes/response_repair_source_ci'/self.name
        self.state.update(kind='actual_public_complete_known_response_centre_repair_source_process_v1',
            worker_source_sha256=digest(__file__),original_complete_body_run=43583838026,
            original_complete_body_mean_run=43586413510,
            original_residual_rows_recomputed=0,original_mean_flows_recomputed=0,
            original_trial_reconstructions_recomputed=0,original_target_primitives_rerun=0,
            exact_affine_parameter_offset='0',physical_parameter='fixed original physical eta0 and nu',
            complete_continuous_inverse_proved=False,actual_full_PDE_response_error_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='complete_known_response_centre_repair_source_public_inputs_v1':
            raise ValueError('the separately pinned complete response-repair manifest is required')

    def prepare(self):
        old_path=self.science/self.manifest['original_body_manifest']
        if digest(old_path)!=ORIGINAL_MANIFEST:
            raise ValueError('the original successful body scientific manifest changed')
        old=read(old_path)
        # Reuse only the old exact input/cover audit. Its numerical
        # complete-mean consumer is never called or relabelled.
        audit_dir=self.evidence/'original-input-audit';audit_dir.mkdir(exist_ok=True)
        audit=SimpleNamespace(
            args=SimpleNamespace(prepared=self.args.prepared,manifest_sha=ORIGINAL_MANIFEST,
                original_run=43583838026,original_attempt=1,previous_artifacts=self.args.previous_artifacts),
            manifest=old,science=self.science,science_topic=self.science_topic,evidence=audit_dir,state={})
        CompleteMeanWorker.restore_original_bundle(audit)
        parts=CompleteMeanWorker.original_complete_parts(audit)
        actual=self.args.body_artifact.resolve();process=read(actual/'process.json')
        body=actual/'native/complete-correlated-body-and-mean-errors.json.gz'
        if (digest(actual/'process.json')!=BODY_PROCESS or digest(body)!=BODY
            or str(process.get('run_id'))!='43586413510'
            or process.get('repository')!='Rogerhu12/math-research-public'
            or not process.get('complete') or process.get('failure')
            or not process.get('children') or any(x.get('actual_returncode')!=0 for x in process['children'])):
            raise ValueError('the same actually successful complete mean/body outcome is required')
        shutil.copyfile(actual/'process.json',self.evidence/'original-complete-body-mean-process.json')
        self.state.update(original_complete_40_parts_and_7721_rows_verified=True,
            original_prepared_bundle_sha256=digest(self.args.prepared/'prepared-manifest.json'),
            original_complete_body_mean_process_sha256=BODY_PROCESS)
        self.publish()
        native=self.cache/'complete-known-response-centre-repair-source.json.gz'
        producer=REL+'scripts/fourfold_codazzi_complete_response_repair_source.py'
        command=[sys.executable,'-u',str(self.science/producer),
            '--original-manifest',str(old_path),
            '--candidate',str(self.science/old['published_candidate']),
            '--response',old['row_identity']['full_trials']['response']['path'],
            '--body',str(body),'--body-process',str(actual/'process.json'),
            '--repair',str(self.science/self.manifest['exact_continuous_centre_repair_native']),
            '--parts',*[str(path) for path in parts],'--out',str(native)]
        self.execute('actual_complete_7721_known_response_centre_repair_source_fees',command)
        result=read(native)
        if (not result.get('complete') or result.get('failure')
            or result.get('source_sha256')!=self.manifest['files'][producer]
            or result.get('complete_common_rows')!=7721 or len(result.get('rows',[]))!=7721
            or result.get('exact_interval')!=['0','25/8']
            or not result.get('true_complete_mean_correction_retained')
            or not result.get('entire_repaired_parameter_source_paid')
            or result.get('original_residual_rows_recomputed')!=0
            or result.get('original_mean_flows_recomputed')!=0
            or result.get('actual_full_PDE_response_error_proved')
            or result.get('complete_continuous_inverse_proved')):
            raise ValueError('the actual complete repair-source consumer failed or exceeded its scope')
        summary={key:value for key,value in result.items() if key!='rows'}
        summary['native_sha256']=digest(native)
        save(self.evidence/'complete-known-response-centre-repair-source-summary.json',summary)
        self.state.update(complete=True,complete_native_sha256=digest(native),
            actual_original_common_rows_consumed=7721,
            complete_repair_source_L2_radial=result['complete_repair_source_L2_radial'],
            complete_repaired_response_residual_L2_radial=result['complete_repaired_response_residual_L2_radial'],
            full_high_input_feedback_and_true_regular_boundary_fees_still_required=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','prepared','previous-artifacts','body-artifact','work','artifact-dir'):
        p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--compute-minutes',type=int,default=40);p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='complete-response-repair-source';a.mode='prepare';a.first=0;a.end=0
    a.recovery_manifest=None;a.recovery_sha=None
    worker=RepairSourceWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
