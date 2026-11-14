#!/usr/bin/env python3
"""Public reviewed wrapper consuming only actual same-Z source outcomes."""
from __future__ import annotations
import argparse,json,shutil,signal,sys
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC
from fourfold_native_lossless_parts import restore

REL='topics/visible-flex-exact-nearby/'
PRODUCER=REL+'scripts/fourfold_codazzi_same_Z_cached_Green.py'
NATIVE='complete-finite193-same-Z-known-source-Green.json.gz'
GREEN='fd6c1f4baa4ec86aab08d4925a0ec9565c3791cbe470b77c2e41549d8f071de6'
GREEN_PROCESS='297cb4c9b8f58bbaacbcf1d0be594f43ea385420f8ea58fbb14e83bf84a63a1c'
BODY_WORKER='c0654466f3451b38f469c00f7286a0f450db0bd52cc62973f72838ac1528e411'
BODY_MANIFEST='05178f530e1fbc9be1016faa52cb9f5773e199915ab7bfcae1ad187609e7e0ac'
CUT_WORKER='dd13bf009bbee7b3074d9b200a80c91bbcb798b57d00ed3278e34f5533630b38'
CUT_MANIFEST='6a38fdc16b65fd052fcf85fc91d239941d82d695fd29a71f7ecad8398c8daad2'


def small(path,doc):
    data=(json.dumps(doc,ensure_ascii=False,indent=2)+'\n').encode()
    if len(data)>60000:raise ValueError('a new same-Z Green plaintext summary exceeded60000 bytes')
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(data)


def actual(process,run):
    return (process.get('repository')=='Rogerhu12/math-research-public'
        and str(process.get('run_id'))==str(run) and process.get('complete')
        and not process.get('failure') and process.get('children')
        and all(c.get('actual_returncode')==0 for c in process['children']))


class SameZGreenWorker(ReviewedBodyWorker):
    def __init__(self,a):
        super().__init__(a)
        self.name=f'run-{self.run_label}-same-Z-Green-body-{a.body_run}-cut-{a.cut_run}'
        self.dest=TOPIC/'notes/same_Z_Green_ci'/self.name
        self.state.update(kind='actual_public_complete_finite193_same_Z_Green_process_v1',
            worker_source_sha256=digest(__file__),original_complete_Green_run=43601964129,
            complete_body_source_run=a.body_run,complete_cut_source_run=a.cut_run,
            original_Riccati_ports_recomputed=0,original_projector_cells_recomputed=0,
            original_body_or_cap_source_cells_recomputed=0,
            complete_finite193_compressed_response_error_bound_proved=False,
            actual_full_PDE_response_error_proved=False,complete_infinite_BVP_inverse_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='complete_same_Z_cached_finite_Green_public_inputs_v1':
            raise ValueError('the exact independent same-Z Green manifest is required')

    def exact_native(self,root,logical,process,expected=None):
        records=[x for x in process.get('native_files',[]) if x.get('logical_file')==logical]
        if len(records)!=1:raise ValueError('an actual complete input native record is absent or duplicated')
        item=records[0]
        if expected is not None and item['sha256']!=expected:raise ValueError('the exact original native differs')
        path=root/logical
        if not path.exists():
            if 'lossless_manifest' not in item:raise ValueError('the complete native bytes are missing')
            path=self.work/('restored-'+item['sha256']+'.json.gz')
            if not path.exists():restore(root/item['lossless_manifest'],path)
        if digest(path)!=item['sha256']:raise ValueError('the original lossless native did not restore byte-for-byte')
        return path

    def original_inputs(self):
        specs={
            'green':(self.args.green_artifact,43601964129,'native/complete-finite-head-Green-and-distributed-known-sources.json.gz',GREEN),
            'body-source':(self.args.body_artifact,self.args.body_run,'native/complete7721-mixed-Z-sources.json.gz',None),
            'cut-source':(self.args.cut_artifact,self.args.cut_run,'native/complete1977-cut-direction-and-same-Z-sources.json.gz',None)}
        inputs={}
        for label,(root,run,logical,expected) in specs.items():
            root=root.resolve();pp=root/'process.json';p=read(pp)
            if not actual(p,run):raise ValueError('the actual complete '+label+' process did not succeed')
            if label=='green' and digest(pp)!=GREEN_PROCESS:
                raise ValueError('the exact original successful Green artifact process changed')
            if label=='body-source' and (p.get('phase')!='finish'
                or p.get('worker_source_sha256')!=BODY_WORKER or p.get('input_manifest_sha256')!=BODY_MANIFEST):
                raise ValueError('the body-source outcome is not the exact full7721 completed consumer')
            if label=='cut-source' and (p.get('phase')!='finish'
                or p.get('worker_source_sha256')!=CUT_WORKER or p.get('input_manifest_sha256')!=CUT_MANIFEST):
                raise ValueError('the cut-source outcome is not the exact complete1977 same-Z consumer')
            native=self.exact_native(root,logical,p,expected)
            if p.get('complete_native_sha256')!=digest(native):raise ValueError('a successful process names different native bytes')
            process_label='green-process' if label=='green' else 'body-process' if label=='body-source' else 'cut-process'
            inputs[label]=native;inputs[process_label]=pp
            shutil.copyfile(pp,self.evidence/('original-'+process_label+'.json'))
        return inputs

    def completed(self,inputs):
        root=TOPIC/'notes/same_Z_Green_ci'
        if not root.exists():return None
        for pp in sorted(root.glob('*/process.json')):
            p=read(pp)
            if (p.get('repository')!='Rogerhu12/math-research-public'
                or p.get('worker_source_sha256')!=digest(__file__)
                or p.get('input_manifest_sha256')!=self.args.manifest_sha
                or p.get('actual_input_sha256')!=inputs
                or not any(c.get('actual_returncode')==0 for c in p.get('children',[]))):continue
            records=[x for x in p.get('native_files',[]) if x.get('logical_file')=='native/'+NATIVE]
            if len(records)!=1:continue
            old=self.exact_native(pp.parent,'native/'+NATIVE,p);result=read(old)
            if (result.get('complete') and not result.get('failure')
                and result.get('source_sha256')==self.manifest['files'][PRODUCER]
                and result.get('input_sha256')==inputs and result.get('gates')
                and all(g['passed'] for g in result['gates'])
                and result.get('complete_finite193_compressed_response_error_bound_proved')):
                return pp,old
        return None

    def execute(self,label,command):
        try:return super().execute(label,command)
        finally:
            native=self.cache/NATIVE
            if native.exists():
                result=read(native)
                outcome=dict(native_sha256=digest(native),complete=result.get('complete'),
                    failure=result.get('failure'),gates=result.get('gates',[]),
                    actual_progress=result.get('actual_progress'),
                    complete_finite193_error_proved=result.get('complete_finite193_compressed_response_error_bound_proved',False),
                    actual_full_PDE_response_error_proved=result.get('actual_full_PDE_response_error_proved',False))
                small(self.evidence/'actual-latest-child-outcome.json',outcome);print(json.dumps(outcome),flush=True)
                if result.get('failure') and self.log.exists():print(self.log.read_text()[-16000:],flush=True)

    def prepare(self):
        native=self.cache/NATIVE;inputs=self.original_inputs();expected={k:digest(v) for k,v in inputs.items()}
        self.state['actual_input_sha256']=expected
        command=[sys.executable,'-u',str(self.science/PRODUCER),'--out',str(native),
            '--body-run',str(self.args.body_run),'--cut-run',str(self.args.cut_run)]
        for k,v in inputs.items():command+=['--'+k,str(v)]
        prior=self.completed(expected)
        if prior:
            pp,old=prior;command+=['--resume',str(old)]
            shutil.copyfile(pp,self.evidence/'original-completed-same-Z-Green-process.json')
            self.state.update(original_successful_same_Z_Green_native_sha256=digest(old),
                original_successful_source_propagation_reused=True)
        self.publish();self.execute('actual_same_Z_complete_known_source_Green',command)
        result=read(native)
        if (not result.get('complete') or result.get('failure')
            or result.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or result.get('input_sha256')!=expected or not result.get('gates')
            or not all(x['passed'] for x in result['gates'])
            or not result.get('complete_finite193_compressed_response_error_bound_proved')
            or result.get('actual_full_PDE_response_error_proved') or result.get('complete_infinite_BVP_inverse_proved')):
            raise ValueError('the actual same-Z known-source result failed or exceeded its scope')
        summary=dict(native_sha256=digest(native),complete=True,gates=result['gates'],seconds=result['seconds'],
            input_sha256=expected,exact_inner_BVP_interval=result['exact_inner_BVP_interval'],
            fixed_phase_error_norm_interval=result['fixed_phase_error_norm_interval'],
            exact_continuous_direction_definition_sha256=result['exact_continuous_direction_definition_sha256'],
            complete_finite193_compressed_response_error_bound_proved=True,
            actual_full_PDE_response_error_proved=False,complete_infinite_BVP_inverse_proved=False,
            true_parameter_Schur_proved=False,full_unknown_high_feedback_and_high_response_still_required=True,
            original_Riccati_ports_recomputed=0,original_projector_cells_recomputed=0,
            original_body_or_cap_source_cells_recomputed=0,
            complete_original_profiles_and_vectors_retained_in_native=True)
        for key in ('complete_finite193_same_Z_error_L2_bounds','complete_finite193_same_Z_error_sup_bounds',
            'component_L2_triangle_bounds','known_boundary_loads'):
            summary[key]={k:v['upper'] for k,v in result[key].items()}
        summary['complete_component_L2_bounds']={w:{k:v['upper'] for k,v in row.items()}
            for w,row in result['complete_component_L2_bounds'].items()}
        summary['separate_known_high_body_source_bounds']={w:{k:v['upper'] for k,v in row.items()}
            for w,row in result['separate_known_high_body_source_bounds'].items()}
        summary['separate_known_full_high_cut_output']=result['separate_known_full_high_cut_output']['upper']
        summary['complete_finite193_negative_error_upper_below_one_over200']=result['complete_finite193_negative_error_upper_below_one_over200']
        small(self.evidence/'complete-same-Z-Green-summary.json',summary)
        self.state.update(complete=True,complete_native_sha256=digest(native),actual_gates=len(result['gates']),
            complete_finite193_compressed_response_error_bound_proved=True,
            complete_finite193_same_Z_error_L2_bounds=result['complete_finite193_same_Z_error_L2_bounds'],
            actual_new_summary_bytes=(self.evidence/'complete-same-Z-Green-summary.json').stat().st_size)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','work','artifact-dir','green-artifact','body-artifact','cut-artifact'):
        p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--body-run',type=int,required=True);p.add_argument('--cut-run',type=int,required=True)
    p.add_argument('--compute-minutes',type=int,default=80);p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='same-Z-complete-known-source-Green';a.mode='prepare';a.first=0;a.end=0
    a.recovery_manifest=None;a.recovery_sha=None
    worker=SameZGreenWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
