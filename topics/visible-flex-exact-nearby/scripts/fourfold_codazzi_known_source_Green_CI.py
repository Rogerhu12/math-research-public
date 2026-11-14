#!/usr/bin/env python3
"""Consume only the newly paid source channels of an actual complete Green run."""
from __future__ import annotations
import argparse,shutil,signal,sys
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC,save
from fourfold_native_lossless_parts import restore

REL='topics/visible-flex-exact-nearby/'
GREEN_WORKER='6d3446499f8cad204aedd71142e9ba1b86d1f57af2394050af1681d040169770'
GREEN_MANIFEST='da3e142168cb2a92d08548efe71ed4505e2e82d82cda965b128582e1acb22764'
REPAIR_NATIVE='05e0493dbe55490adec8fb6603e0ec431d1bc03f051aec86be8a78741f60f0a4'
REPAIR_PROCESS='4bb16cb2c349977243a5e07ce1f9abdae7a9130f403277b68e5b64ffdafd5386'
BOUNDARY_NATIVE='b1adeea522b31efa2fc83a6436bc3fe52dbd04630c17d5436927b5872b05e263'
BOUNDARY_PROCESS='6ff7f39ab70150f99eebb8a880fb0f52867574b25e122b59d95c1a0105e2609e'
NATIVE='complete-finite193-known-repair-and-true-boundary-error.json.gz'
LABEL='actual_cached_complete_finite193_Green_new_known_repair_and_true_boundary_sources'


class KnownGreenWorker(ReviewedBodyWorker):
    def __init__(self,args):
        super().__init__(args)
        self.name=f'run-{self.run_label}-known-source-Green-from-{args.green_run}'
        self.dest=TOPIC/'notes/known_response_Green_ci'/self.name
        self.state.update(kind='actual_public_cached_complete_finite193_Green_known_source_process_v1',
            worker_source_sha256=digest(__file__),original_complete_Green_run=args.green_run,
            actual_complete_repair_source_run=43597921732,actual_complete_boundary_source_run=43599771405,
            exact_affine_parameter_offset='0',physical_parameter='fixed original physical eta0 and nu',
            whole_original_parameter_half_width=None,
            original_Riccati_ports_recomputed=0,original_projector_cells_recomputed=0,
            original_four_source_columns_recomputed=0,original_mean_flows_recomputed=0,
            original_cap_matrix_or_cap_trial_residual_recomputed=0,
            complete_finite193_compressed_response_error_bound_proved=False,
            actual_full_PDE_response_error_proved=False,complete_infinite_BVP_inverse_proved=False,
            true_parameter_Schur_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='cached_complete_finite193_Green_known_new_sources_public_inputs_v1':
            raise ValueError('the separate cached Green known-source manifest is required')

    def exact_native(self,root,logical,process,expected=None):
        root=root.resolve()
        records=[x for x in process.get('native_files',[]) if x.get('logical_file')==logical]
        if len(records)!=1:raise ValueError('an original exact native record is missing or duplicated')
        item=records[0]
        if expected is not None and item['sha256']!=expected:raise ValueError('the original native identity changed')
        path=root/logical
        if path.exists():
            if digest(path)!=item['sha256']:raise ValueError('the original artifact native bytes changed')
            return path
        # Repository snapshots may use exact container parts. This is a
        # byte restoration only, never a mathematical replay.
        if 'lossless_manifest' not in item:raise FileNotFoundError(str(path))
        restored=self.work/('original-native-'+item['sha256']+'.json.gz')
        if not restored.exists():
            restore(root/item['lossless_manifest'],restored)
        if digest(restored)!=item['sha256']:raise ValueError('the original lossless native did not restore exactly')
        return restored

    def reuse(self,producer,native,expected_inputs):
        root=TOPIC/'notes/known_response_Green_ci'
        if not root.exists():return False
        for process_path in sorted(root.glob('*/process.json')):
            process=read(process_path)
            children=[x for x in process.get('children',[]) if x.get('label')==LABEL and x.get('actual_returncode')==0]
            if (process.get('repository')!='Rogerhu12/math-research-public'
                or process.get('worker_source_sha256')!=digest(__file__)
                or process.get('input_manifest_sha256')!=self.args.manifest_sha
                or process.get('actual_input_sha256')!=expected_inputs or not children):continue
            old=self.exact_native(process_path.parent,'native/'+NATIVE,process)
            result=read(old)
            if (not result.get('complete') or result.get('failure')
                or result.get('source_sha256')!=self.manifest['files'][producer]
                or result.get('input_sha256')!=expected_inputs
                or not result.get('complete_finite193_compressed_response_error_bound_proved')
                or result.get('actual_full_PDE_response_error_proved')
                or not result.get('gates') or not all(x['passed'] for x in result['gates'])):
                raise ValueError('a recorded successful identical known-source child is inconsistent')
            shutil.copyfile(old,native)
            shutil.copyfile(process_path,self.evidence/'original-successful-known-source-Green-process.json')
            self.state.update(actual_new_source_consumer_executed=False,
                original_successful_known_source_run=process['run_id'],
                actual_successful_identical_source_consumer_reused=True)
            return True
        return False

    def prepare(self):
        specifications={
            'green':(self.args.green_artifact,self.args.green_run,
                'native/complete-finite-head-Green-and-distributed-known-sources.json.gz',None,None),
            'repair-source':(self.args.repair_artifact,43597921732,
                'native/complete-known-response-centre-repair-source.json.gz',REPAIR_NATIVE,REPAIR_PROCESS),
            'boundary-source':(self.args.boundary_artifact,43599771405,
                'native/known-waist-and-true-cap-sources.json.gz',BOUNDARY_NATIVE,BOUNDARY_PROCESS)}
        resolved={};expected_inputs={}
        for label,(root,run_id,logical,expected_native,expected_process) in specifications.items():
            root=root.resolve();process=read(root/'process.json')
            if (process.get('repository')!='Rogerhu12/math-research-public'
                or str(process.get('run_id'))!=str(run_id)
                or not process.get('complete') or process.get('failure') or not process.get('children')
                or any(x.get('actual_returncode')!=0 for x in process['children'])):
                raise ValueError('the actual successful original '+label+' process is required')
            if expected_process is not None and digest(root/'process.json')!=expected_process:
                raise ValueError('the original '+label+' process bytes changed')
            if label=='green' and (process.get('phase')!='complete'
                or process.get('worker_source_sha256')!=GREEN_WORKER
                or process.get('input_manifest_sha256')!=GREEN_MANIFEST
                or not process.get('complete_finite193_inverse_proved')):
                raise ValueError('the actual original complete finite193 Green outcome is required')
            native=self.exact_native(root,logical,process,expected_native)
            if digest(native)!=process.get('complete_native_sha256'):
                raise ValueError('the actual complete native and its original process disagree')
            process_label={'green':'green-process','repair-source':'repair-process','boundary-source':'boundary-process'}[label]
            expected_inputs[label]=digest(native);expected_inputs[process_label]=digest(root/'process.json')
            resolved[label]=(native,root/'process.json',process_label)
            shutil.copyfile(root/'process.json',self.evidence/('original-'+process_label+'.json'))
        self.state['actual_input_sha256']=expected_inputs
        self.state['all_original_completed_source_and_Green_outcomes_verified']=True
        self.publish()
        native=self.cache/NATIVE
        producer=REL+'scripts/fourfold_codazzi_cached_Green_known_response_sources.py'
        if not self.reuse(producer,native,expected_inputs):
            command=[sys.executable,'-u',str(self.science/producer),
                '--green-run',str(self.args.green_run),'--out',str(native)]
            for label,(path,process,process_label) in resolved.items():
                command.extend(['--'+label,str(path),'--'+process_label,str(process)])
            self.execute(LABEL,command)
            self.state.update(actual_new_source_consumer_executed=True,
                actual_successful_identical_source_consumer_reused=False,
                original_successful_known_source_run=self.state['run_id'])
        result=read(native)
        if (not result.get('complete') or result.get('failure')
            or result.get('source_sha256')!=self.manifest['files'][producer]
            or result.get('input_sha256')!=expected_inputs
            or not result.get('gates') or not all(x['passed'] for x in result['gates'])
            or not result.get('complete_finite193_compressed_response_error_bound_proved')
            or result.get('actual_full_PDE_response_error_proved')
            or result.get('complete_infinite_BVP_inverse_proved')
            or not result.get('known_full_high_output_kept_separate_from_unknown_high_feedback')
            or not result.get('every_original_body_and_trial_interface_retained')):
            raise ValueError('the actual known-source Green certificate failed or exceeded its scope')
        excluded={'new_repair_backward_profiles','complete_new_known_source_profiles',
                  'complete_new_repair_interface_profiles'}
        summary={key:value for key,value in result.items() if key not in excluded}
        summary['native_sha256']=digest(native)
        save(self.evidence/'complete-known-source-Green-summary.json',summary)
        self.state.update(complete=True,complete_native_sha256=digest(native),
            actual_public_known_source_Green_gates=len(result['gates']),
            complete_finite193_compressed_response_error_bound_proved=True,
            complete_distributed_known_source_L2_bounds=result['complete_distributed_known_source_L2_bounds'],
            separate_known_full_high_cut_output=result['separate_known_full_high_cut_output'],
            full_high_input_feedback_and_high_response_still_required=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','green-artifact','repair-artifact','boundary-artifact','work','artifact-dir'):
        p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--green-run',type=int,required=True)
    p.add_argument('--compute-minutes',type=int,default=40);p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    if a.green_run<=0:raise ValueError('the actual original complete Green run is required')
    a.kind='cached-Green-known-sources';a.mode='prepare';a.first=0;a.end=0
    a.recovery_manifest=None;a.recovery_sha=None
    worker=KnownGreenWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
