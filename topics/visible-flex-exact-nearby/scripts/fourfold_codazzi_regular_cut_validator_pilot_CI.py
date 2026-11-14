#!/usr/bin/env python3
"""Run the public full-state algebra gates and four disjoint actual cells."""
from __future__ import annotations
import argparse,shutil,signal,sys
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC,save


class PilotWorker(ReviewedBodyWorker):
    def __init__(self,args):
        super().__init__(args);self.name=f'run-{self.run_label}-complete-projector-four-cell-pilot'
        self.dest=TOPIC/'notes/regular_cut_validator_ci'/self.name
        self.state.update(kind='actual_public_complete_cut_projector_four_cell_pilot_process',
            worker_source_sha256=digest(__file__),requested_disjoint_original_indices=[0,76,3300,5969],
            original_complete_frame_run=43588509643,original_frame_cells_recomputed=0,
            selected_actual_cells_completed=[],complete_original_5970_cells_claimed=False,
            continuous_global_inverse_proved=False,true_parameter_Schur_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='complete_cut_projector_four_cell_public_pilot_inputs_v1':
            raise ValueError('the explicitly reviewed full-state public pilot manifest is required')

    def prepare(self):
        prior=self.args.prior_artifact.resolve();process=read(prior/'process.json')
        proposal=prior/'native/complete-cut-proposal.json.gz'
        if (str(process.get('run_id'))!='43588509643' or not process.get('complete') or process.get('failure')
            or process.get('repository')!='Rogerhu12/math-research-public'
            or process.get('complete_native_sha256')!=self.manifest['original_proposal_native_sha256']
            or process.get('input_manifest_sha256')!='f8c27873466b88ce7b1d0497d1baeaaa6682ae6ebfa2840fb3c80d9baf3e0e2f'
            or not process.get('children') or any(c.get('actual_returncode')!=0 for c in process['children'])
            or digest(proposal)!=self.manifest['original_proposal_native_sha256']):
            raise ValueError('the actual complete original 5970-frame proposal changed or failed')
        original=read(proposal)
        if (not original.get('complete') or len(original['rows'])!=5970
            or original.get('exact_covered_interval')!=['0','9/10']):
            raise ValueError('every original frame from the true cut to the waist is required')
        shutil.copyfile(prior/'process.json',self.evidence/'original-complete-frame-process.json')
        gates=self.cache/'complete-public-algebra-gates.json.gz'
        self.execute('public_full193_algebra_Gram_signed_rate_mean_and_true_angle_gates',
            [sys.executable,'-u',str(self.science_topic/'scripts/fourfold_codazzi_regular_cut_public_algebra_gates.py'),
             '--out',str(gates)])
        result=read(gates)
        if not result.get('complete') or result.get('failure') or not all(g['passed'] for g in result['gates']):
            raise ValueError('an actual public full-state algebra gate failed')
        for index in self.manifest['pilot_indices']:
            native=self.cache/f'validated-cell-{index:05d}-{index+1:05d}.json.gz'
            command=[sys.executable,'-u',str(self.science_topic/'scripts/fourfold_codazzi_regular_cut_projector_validator.py')]
            for key in ('candidate','object','repair-report'):
                command+=['--'+key,str(self.science/self.manifest['proposal_inputs'][key])]
            command+=['--proposal',str(proposal),'--frames',str(prior/'frames'),
                '--first',str(index),'--end',str(index+1),'--degree','24','--bits','256',
                '--max-new-cells','1','--out',str(native)]
            self.execute(f'actual_complete_193_by_96_continuous_projector_cell_{index}',command)
            result=read(native)
            if (not result.get('selected_cells_complete') or result.get('failure')
                or result['identity']['selected_indices']!=[index,index+1]
                or len(result['rows'])!=1 or result['rows'][0]['index']!=index
                or not result['rows'][0]['complete_continuous_local_projector_estimates']):
                raise ValueError('an actual full-state continuous pilot cell failed')
            self.state['selected_actual_cells_completed'].append(index)
            save(self.evidence/f'validated-cell-{index:05d}-summary.json',dict(
                selected_indices=[index,index+1],complete=True,native_sha256=digest(native),
                whole_original_domain_not_claimed=True,actual_local_estimates=result['rows'][0]))
            self.publish()
        self.state.update(complete=True,actual_public_synthetic_gates=7,
            actual_complete_continuous_cells=4,complete_original_5970_cells_claimed=False,
            continuous_global_inverse_proved=False,true_parameter_Schur_proved=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','prior-artifact','work','artifact-dir'):p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--compute-minutes',type=int,default=45);p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='cut-projector-pilot';a.mode='prepare';a.first=0;a.end=0;a.recovery_manifest=None;a.recovery_sha=None
    worker=PilotWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
