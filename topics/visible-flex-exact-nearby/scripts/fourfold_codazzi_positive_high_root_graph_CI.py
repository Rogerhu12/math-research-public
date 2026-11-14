#!/usr/bin/env python3
"""Run only the small same-reference positive high interface consumer."""
from __future__ import annotations
import argparse,shutil,signal,sys
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC,save

REL='topics/visible-flex-exact-nearby/'
PRODUCER=REL+'scripts/fourfold_codazzi_repaired_positive_high_root_graph.py'
NATIVE='repaired-positive-high-root-to-regular-graph.json.gz'
LABEL='actual_same_reference_positive_high_root_to_regular_interface_arithmetic'
KIND='actual_same_reference_repaired_root_to_regular_given_head_high_graph_v1'


class PositiveHighGlueWorker(ReviewedBodyWorker):
    def __init__(self,args):
        super().__init__(args)
        self.name=f'run-{self.run_label}-positive-high-root-to-regular'
        self.dest=TOPIC/'notes/positive_high_root_graph_ci'/self.name
        self.state.update(kind='actual_public_repaired_positive_high_root_graph_process_v1',
            worker_source_sha256=digest(__file__),original_root_collar_run=43600926806,
            original_complete_positive_body_run=43601149891,
            original_collar_mathematics_recomputed=0,original_4650_body_rows_recomputed=0,
            original_target_or_outer_graph_recomputed=0,exact_affine_parameter_offset='0',
            physical_parameter='fixed physical eta0 and original nu',
            given_complete_head_positive_high_graph_proved=False,
            full_low_high_Schur_inverse_proved=False,complete_infinite_BVP_inverse_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='same_reference_repaired_positive_high_root_graph_public_inputs_v1':
            raise ValueError('the separate full positive high interface manifest is required')

    def reuse(self,native,inputs):
        directory=TOPIC/'notes/positive_high_root_graph_ci'
        if not directory.exists():return False
        for path in sorted(directory.glob('*/process.json')):
            process=read(path)
            if (process.get('repository')!='Rogerhu12/math-research-public'
                or process.get('worker_source_sha256')!=digest(__file__)
                or process.get('input_manifest_sha256')!=self.args.manifest_sha
                or process.get('actual_scientific_input_sha256')!=inputs
                or not process.get('complete') or process.get('failure')
                or not any(c.get('label')==LABEL and c.get('actual_returncode')==0
                    for c in process.get('children',[]))):continue
            old=path.parent/'native'/NATIVE
            if not old.exists() or digest(old)!=process.get('complete_native_sha256'):
                raise ValueError('an identical successful high interface native is missing or changed')
            result=read(old)
            if (result.get('kind')!=KIND or not result.get('complete') or result.get('failure')
                or result.get('source_sha256')!=self.manifest['files'][PRODUCER]
                or result.get('input_sha256')!=inputs
                or not result.get('given_complete_head_positive_high_inverse_and_root_graph_proved')
                or result.get('full_low_high_Schur_inverse_proved')
                or not all(g['passed'] for g in result['gates'])):
                raise ValueError('an identical prior complete high interface outcome is inconsistent')
            shutil.copyfile(old,native);shutil.copyfile(path,self.evidence/'original-identical-successful-process.json')
            self.state.update(actual_new_interface_child_executed=False,
                identical_successful_interface_reused=True,original_successful_interface_run=process['run_id'])
            return True
        return False

    def prepare(self):
        resolved={label:self.science/path for label,path in self.manifest['actual_small_inputs'].items()}
        inputs={label:digest(path) for label,path in resolved.items()}
        self.state['actual_scientific_input_sha256']=inputs
        for label,path in resolved.items():shutil.copyfile(path,self.evidence/('original-'+label+'.json'))
        self.publish()
        native=self.cache/NATIVE
        if not self.reuse(native,inputs):
            command=[sys.executable,'-u',str(self.science/PRODUCER),'--out',str(native)]
            for label,path in resolved.items():command.extend(['--'+label,str(path)])
            self.execute(LABEL,command)
            self.state.update(actual_new_interface_child_executed=True,
                identical_successful_interface_reused=False)
        result=read(native)
        if (result.get('kind')!=KIND or not result.get('complete') or result.get('failure')
            or result.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or result.get('input_sha256')!=inputs
            or not result.get('given_complete_head_positive_high_inverse_and_root_graph_proved')
            or result.get('full_low_high_Schur_inverse_proved')
            or result.get('complete_infinite_BVP_inverse_proved')
            or result.get('actual_full_PDE_response_error_proved')
            or not result.get('gates') or not all(g['passed'] for g in result['gates'])):
            raise ValueError('the new actual complete positive high interface failed or exceeded its scope')
        summary=dict(result,native_sha256=digest(native))
        save(self.evidence/'repaired-positive-high-root-graph-summary.json',summary)
        self.state.update(complete=True,complete_native_sha256=digest(native),
            actual_interface_gates=len(result['gates']),
            actual_interface_constants=result['constants'],
            given_complete_head_positive_high_graph_proved=True,
            all_seven_source_and_jump_response_rows_retained=True,
            full_low_high_Schur_and_negative_return_still_required=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','work','artifact-dir'):p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--compute-minutes',type=int,default=15);p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='repaired-positive-high-root-graph';a.mode='prepare';a.first=0;a.end=0
    a.recovery_manifest=None;a.recovery_sha=None
    worker=PositiveHighGlueWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
