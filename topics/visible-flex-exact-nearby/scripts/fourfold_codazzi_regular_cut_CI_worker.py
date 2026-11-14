#!/usr/bin/env python3
"""Execute and checkpoint the complete cut-to-waist frame proposal publicly.

All 193-by-96 arrays stay in Actions artifacts. The committed native is
an explicitly diagnostic proposal with all ordinary/mean/true-cap/jump
and infinite-high verification still required. Original science and all
historical cap computations remain unchanged.
"""
from __future__ import annotations
import argparse, gzip, os, shutil, signal, sys
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC,save


class CutWorker(ReviewedBodyWorker):
    def __init__(self,args):
        super().__init__(args)
        self.name=f'run-{self.run_label}-cut-to-waist-frame-proposal'
        self.dest=TOPIC/'notes/regular_cut_subspace_ci'/self.name
        self.state.update(kind='actual_public_complete_cut_to_waist_frame_proposal_process',
            worker_source_sha256=digest(__file__),requested_exact_interval=['0','9/10'],
            mathematical_continuous_inverse_claimed=False,
            proposal_only=True,whole_original_parameter_half_width='0',
            full_mean_and_complete_193_by_96_frames_retained=True)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='complete_repaired_cut_to_waist_proposal_pinned_inputs_v1':
            raise ValueError('the explicitly reviewed complete cut proposal manifest is required')

    def prepare(self):
        frames=self.artifact/'frames'
        if self.args.prior_artifact:
            prior=self.args.prior_artifact.resolve();actual=read(prior/'process.json')
            if (actual.get('repository')!='Rogerhu12/math-research-public'
                or actual.get('input_manifest_sha256')!=self.args.manifest_sha
                or actual.get('kind')!='actual_public_complete_cut_to_waist_frame_proposal_process'):
                raise ValueError('the prior complete frame prefix belongs to another scientific proposal')
            source=prior/'frames'
            if not (source/'checkpoint.json').exists():
                raise ValueError('the prior actual artifact has no complete resumable frame checkpoint')
            if frames.exists():raise FileExistsError('preserve existing complete proposal arrays')
            shutil.copytree(source,frames)
            previous=self.evidence/'original-prefix';previous.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(prior/'process.json',previous/'process.json')
            self.state['consumed_original_frame_checkpoint_sha256']=digest(frames/'checkpoint.json')
            checkpoint=read(frames/'checkpoint.json')
            self.state['original_completed_frame_cells_reused']=len(checkpoint['rows'])
            if checkpoint.get('complete'):
                for chunk in checkpoint['complete_frame_chunks']:
                    if digest(frames/chunk['file'])!=chunk['sha256']:
                        raise ValueError('a prior complete full frame chunk changed')
                save(self.cache/'complete-cut-proposal.json.gz',checkpoint)
                self.state.update(complete=True,reused_complete_proposal_without_execution=True,
                    mathematical_continuous_inverse_claimed=False)
                return
        native=self.cache/'complete-cut-proposal.json.gz'
        command=[sys.executable,'-u',str(self.science_topic/'scripts/fourfold_codazzi_regular_cut_polynomial_proposal.py')]
        for key,path in self.manifest['proposal_inputs'].items():
            command+=['--'+key,str(self.science/path)]
        for key,value in self.manifest['proposal_parameters'].items():command+=['--'+key,str(value)]
        command+=['--work',str(frames),'--out',str(native),'--max-new-cells','10000000']
        self.execute('complete_193_by_96_repaired_cut_to_waist_weighted_frame_proposal',command)
        result=read(native)
        if (not result.get('complete') or result.get('failure')
            or not result.get('all_original_common_cells_covered')
            or result.get('exact_covered_interval')!=['0','9/10']
            or not result.get('all_frames_have_193_rows_and_96_columns')):
            raise ValueError('the actual complete cut-to-waist frame proposal did not complete')
        files=[]
        for chunk in result['complete_frame_chunks']:
            path=frames/chunk['file']
            if digest(path)!=chunk['sha256']:raise ValueError('a complete saved frame chunk changed')
            files.append(dict(chunk))
        save(self.evidence/'complete-frame-artifact-map.json',dict(complete=True,
            exact_interval=['0','9/10'],frame_chunks=files,
            exact_weight_mesh_sha256=digest(frames/'exact-weight-and-base-mesh.json'),
            complete_native_sha256=digest(native),large_arrays_only_in_this_original_Actions_artifact=True,
            no_continuous_inverse_certificate_claimed=True))
        summary={k:v for k,v in result.items() if k not in ('rows','complete_frame_chunks')}
        summary['complete_saved_cells']=len(result['rows'])
        summary['complete_native_sha256']=digest(native)
        save(self.evidence/'complete-cut-proposal-summary.json',summary)
        self.state.update(complete=True,complete_proposal_cell_count=len(result['rows']),
            complete_native_sha256=digest(native),continuous_BVP_inverse_proved=False,
            true_parameter_Schur_proved=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--manifest',type=Path,required=True);p.add_argument('--manifest-sha',required=True)
    p.add_argument('--rules',type=Path,required=True);p.add_argument('--rules-sha',required=True)
    p.add_argument('--driver-sha',required=True)
    p.add_argument('--work',type=Path,required=True);p.add_argument('--artifact-dir',type=Path,required=True)
    p.add_argument('--prior-artifact',type=Path)
    p.add_argument('--compute-minutes',type=int,default=310);p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='cut-head';a.mode='prepare';a.first=0;a.end=0;a.recovery_manifest=None;a.recovery_sha=None
    worker=CutWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
