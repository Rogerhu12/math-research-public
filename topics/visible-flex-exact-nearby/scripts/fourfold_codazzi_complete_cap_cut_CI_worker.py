#!/usr/bin/env python3
"""Publish the actual small complete-cap/cut consumer using original artifacts."""
from __future__ import annotations
import argparse,shutil,signal,sys
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC,save


class CompleteCutWorker(ReviewedBodyWorker):
    def __init__(self,args):
        super().__init__(args)
        self.name=f'run-{self.run_label}-complete-cap-and-true-cut'
        self.dest=TOPIC/'notes/complete_cap_cut_ci'/self.name
        self.state.update(kind='actual_public_complete_cap_and_true_cut_consumer_process',
            worker_source_sha256=digest(__file__),original_completed_cap_run=43583838015,
            original_complete_cap_rows_recomputed=0,
            physical_parameter_half_width='1/1000000000',actual_moving_parameter_offset='0',
            continuous_BVP_inverse_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='complete_actual_cap_and_true_cut_consumer_pinned_inputs_v1':
            raise ValueError('the explicitly reviewed complete cap consumer manifest is required')

    def prepare(self):
        prior=self.args.prior_artifact.resolve();process=prior/'process.json'
        shutil.copyfile(process,self.evidence/'original-complete-cap-process.json')
        native=self.cache/'complete-cap-and-true-moving-cut-native.json.gz'
        command=[sys.executable,'-u',str(self.science_topic/'scripts/fourfold_codazzi_complete_cap_cut_consumer.py'),
            '--cap',str(prior/'native/complete-cap-native.json.gz'),'--actual-process',str(process),
            '--hessian',str(self.science/self.manifest['hessian_input']),
            '--cut',str(self.science/self.manifest['cut_input']),'--out',str(native)]
        self.execute('actual_complete_cap_Hessian_low_high_mean_and_full_Gram_consumer',command)
        result=read(native)
        if not result.get('complete') or result.get('failure') or not all(x['passed'] for x in result['gates']):
            raise ValueError('an actual complete-cap/cut gate failed')
        save(self.evidence/'complete-cap-and-cut-summary.json',result)
        self.state.update(complete=True,complete_native_sha256=digest(native),
            true_complete_cap_and_cut_boundary_budget_paid=True,actual_gates=len(result['gates']),
            continuous_BVP_inverse_proved=False,true_parameter_Schur_nonzero_proved=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--manifest',type=Path,required=True);p.add_argument('--manifest-sha',required=True)
    p.add_argument('--rules',type=Path,required=True);p.add_argument('--rules-sha',required=True)
    p.add_argument('--driver-sha',required=True);p.add_argument('--prior-artifact',type=Path,required=True)
    p.add_argument('--work',type=Path,required=True);p.add_argument('--artifact-dir',type=Path,required=True)
    p.add_argument('--compute-minutes',type=int,default=40);p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='cap-cut';a.mode='prepare';a.first=0;a.end=1977;a.recovery_manifest=None;a.recovery_sha=None
    worker=CompleteCutWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
