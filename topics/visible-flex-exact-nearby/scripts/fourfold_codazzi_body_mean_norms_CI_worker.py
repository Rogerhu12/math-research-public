#!/usr/bin/env python3
"""Publish the full mean-correction norm without rerunning any body row."""
from __future__ import annotations
import argparse,shutil,signal,sys
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC,save


class MeanNormWorker(ReviewedBodyWorker):
    def __init__(self,args):
        super().__init__(args)
        self.name=f'run-{self.run_label}-complete-mean-norm-and-phase-direction'
        self.dest=TOPIC/'notes/body_mean_norm_ci'/self.name
        self.state.update(kind='actual_public_complete_mean_norm_and_phase_direction_consumer_process',
            worker_source_sha256=digest(__file__),original_completed_body_run=43586413510,
            original_complete_body_rows_recomputed=0,phase_application_parameter_offset='0',
            continuous_BVP_inverse_proved=False,true_parameter_Schur_nonzero_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='complete_actual_body_mean_norm_and_phase_direction_pinned_inputs_v1':
            raise ValueError('the explicit same-object complete mean-norm manifest is required')

    def prepare(self):
        prior=self.args.prior_artifact.resolve();process=prior/'process.json'
        shutil.copyfile(process,self.evidence/'original-complete-body-process.json')
        native=self.cache/'complete-body-mean-norm-and-phase-direction-native.json.gz'
        command=[sys.executable,'-u',str(self.science_topic/'scripts/fourfold_codazzi_complete_body_mean_norms.py'),
            '--body',str(prior/'native/complete-correlated-body-and-mean-errors.json.gz'),
            '--actual-process',str(process),'--direction',str(self.science/self.manifest['direction_input']),
            '--out',str(native)]
        self.execute('actual_complete_mean_norm_and_raw_trial_to_phase_direction_consumer',command)
        result=read(native)
        if not result.get('complete') or result.get('failure') or not all(x['passed'] for x in result['gates']):
            raise ValueError('an actual full mean-norm bridge gate failed')
        save(self.evidence/'complete-mean-norm-summary.json',result)
        self.state.update(complete=True,complete_native_sha256=digest(native),
            exact_mean_completion_to_explicit_phase_direction_bound_paid=True,
            actual_gates=len(result['gates']),continuous_BVP_inverse_proved=False,
            true_parameter_Schur_nonzero_proved=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--manifest',type=Path,required=True);p.add_argument('--manifest-sha',required=True)
    p.add_argument('--rules',type=Path,required=True);p.add_argument('--rules-sha',required=True)
    p.add_argument('--driver-sha',required=True);p.add_argument('--prior-artifact',type=Path,required=True)
    p.add_argument('--work',type=Path,required=True);p.add_argument('--artifact-dir',type=Path,required=True)
    p.add_argument('--compute-minutes',type=int,default=25);p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='body-mean-norm';a.mode='prepare';a.first=0;a.end=7721;a.recovery_manifest=None;a.recovery_sha=None
    worker=MeanNormWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
