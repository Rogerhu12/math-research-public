#!/usr/bin/env python3
"""Reuse the actual full trial and mean to pay only the known boundary sources."""
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
PREPARED='fd7594990ecc126e63a79198e00bbaf5912537ff1db480ade8ac82ff8917c893'
BODY='a4f31dccc4b54661b43fc06bac59b6afbb4fa2d6d19614f68f71e044be6e5870'
BODY_PROCESS='0a5dc06520bad5a1230b65cba6e895e998e1f3ce6a32a65d9ffa8800b8ea1a9e'
CAP_CUT='36f498e3b0addbb46290c12fae6b63af7673db20ba230e22dd83809d18427104'
WEIGHTED='56db8a3498494bf48de14b50418010053bb6058c722c41993c894c463786dc25'


class KnownBoundaryWorker(ReviewedBodyWorker):
    def __init__(self,args):
        super().__init__(args)
        self.name=f'run-{self.run_label}-known-waist-and-true-cap-sources'
        self.dest=TOPIC/'notes/known_response_boundary_ci'/self.name
        self.state.update(kind='actual_public_complete_known_response_boundary_source_process_v1',
            worker_source_sha256=digest(__file__),
            original_complete_body_run=43583838026,original_complete_body_mean_run=43586413510,
            original_complete_cap_cut_run=43587619797,original_weighted_boundary_run=43594139132,
            old_trial_reconstructions_recomputed=0,old_mean_flows_recomputed=0,old_cap_matrix_cells_recomputed=0,
            exact_affine_parameter_offset='0',physical_parameter='fixed original physical eta0 and nu',
            complete_continuous_inverse_proved=False,actual_full_PDE_response_error_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='complete_known_response_waist_and_true_cap_source_public_inputs_v1':
            raise ValueError('the separately pinned complete boundary-source manifest is required')

    def prepare(self):
        old_path=self.science/self.manifest['original_body_manifest']
        if digest(old_path)!=ORIGINAL_MANIFEST or digest(self.args.prepared/'prepared-manifest.json')!=PREPARED:
            raise ValueError('the original complete prepared trial input or manifest changed')
        old=read(old_path)
        audit_dir=self.evidence/'original-input-audit';audit_dir.mkdir(exist_ok=True)
        audit=SimpleNamespace(
            args=SimpleNamespace(prepared=self.args.prepared,manifest_sha=ORIGINAL_MANIFEST,
                original_run=43583838026,original_attempt=1),
            manifest=old,science=self.science,science_topic=self.science_topic,evidence=audit_dir,state={})
        # This old method only verifies every original file and restores its
        # exact canonical alias. No residual, scalar flow or reconstruction is called.
        CompleteMeanWorker.restore_original_bundle(audit)
        inputs={
            'body':(self.args.body_artifact,'native/complete-correlated-body-and-mean-errors.json.gz',BODY,43586413510),
            'cap-cut':(self.args.cap_cut_artifact,'native/complete-cap-and-true-moving-cut-native.json.gz',CAP_CUT,43587619797),
            'weighted':(self.args.weighted_artifact,'native/complete-true-weighted-boundaries.json.gz',WEIGHTED,43594139132)}
        resolved={}
        for label,(root,relative,expected,run_id) in inputs.items():
            root=root.resolve();process=read(root/'process.json');native=root/relative
            if (digest(native)!=expected
                or str(process.get('run_id'))!=str(run_id)
                or process.get('repository')!='Rogerhu12/math-research-public'
                or not process.get('complete') or process.get('failure')
                or not process.get('children')
                or any(child.get('actual_returncode')!=0 for child in process['children'])):
                raise ValueError('the same actually successful original '+label+' outcome is required')
            if label=='body' and digest(root/'process.json')!=BODY_PROCESS:
                raise ValueError('the original complete mean-flow process bytes changed')
            if label=='weighted' and process.get('phase')!='prepare':
                raise ValueError('the original actual weighted-boundary prepare process is required')
            shutil.copyfile(root/'process.json',self.evidence/('original-'+label+'-process.json'))
            resolved[label]=(native,root/'process.json')
        self.state.update(original_prepared_manifest_sha256=PREPARED,
            original_complete_trial_bytes_verified=True,
            original_actual_process_SHA256={label:digest(value[1]) for label,value in resolved.items()})
        self.publish()
        native=self.cache/'known-waist-and-true-cap-sources.json.gz'
        producer=REL+'scripts/fourfold_codazzi_known_response_true_boundary_sources.py'
        command=[sys.executable,'-u',str(self.science/producer),
            '--response',old['row_identity']['full_trials']['response']['path'],
            '--cut',str(self.science/self.manifest['complete_nominal_cut']),
            '--out',str(native)]
        for label,(original,process) in resolved.items():
            command.extend(['--'+label,str(original),'--'+label+'-process',str(process)])
        self.execute('actual_complete_known193_response_waist_and_true97_plus_high_cap_sources',command)
        result=read(native)
        if (not result.get('complete') or result.get('failure')
            or result.get('source_sha256')!=self.manifest['files'][producer]
            or len(result.get('gates',[]))!=10 or not all(x['passed'] for x in result['gates'])
            or result.get('exact_interior_interval')!=['0','9/10']
            or not result.get('radial_weight_cancels_in_the_actual_boundary_source')
            or not result.get('known_high_output_is_a_source_and_not_a_high_feedback_bound')
            or not result.get('every_original_interior_trial_jump_still_required')
            or result.get('actual_full_PDE_response_error_proved')
            or result.get('complete_continuous_inverse_proved')):
            raise ValueError('the actual complete known boundary-source gate failed or exceeded its scope')
        excluded={'waist_trace','cut_trace','complete_waist_source_96_rows','complete_nominal_cut_source_97_rows'}
        summary={key:value for key,value in result.items() if key not in excluded}
        summary['trace_selection']={name:{key:value for key,value in result[name].items()
            if not key.startswith('complete_193')} for name in ('waist_trace','cut_trace')}
        summary['native_sha256']=digest(native)
        save(self.evidence/'known-waist-and-true-cap-sources-summary.json',summary)
        self.state.update(complete=True,complete_native_sha256=digest(native),
            actual_public_complete_boundary_source_gates=10,
            known_boundary_source_bounds=result['source_bounds'],
            full_true_cap_and_unknown_high_feedback_still_required=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','prepared','body-artifact','cap-cut-artifact','weighted-artifact','work','artifact-dir'):
        p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--compute-minutes',type=int,default=20);p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='complete-known-boundary-source';a.mode='prepare';a.first=0;a.end=0
    a.recovery_manifest=None;a.recovery_sha=None
    worker=KnownBoundaryWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
