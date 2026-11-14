#!/usr/bin/env python3
"""Consume successful source natives; only reweight the existing positive Green profiles."""
from __future__ import annotations
import argparse,json,shutil,signal,sys
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC
from fourfold_native_lossless_parts import restore

REL='topics/visible-flex-exact-nearby/'
PRODUCER=REL+'scripts/fourfold_codazzi_native_point_Hessian_cached_Green.py'
FOLDER='notes/native_point_Hessian_Green_ci'
NATIVE='complete-same-Z-native-point-Hessian-cut-and-Green.json.gz'
LABEL='actual_same_Z_native_point_Hessian_cut_and_positive_profile_reweight'


def small(path,doc):
    data=(json.dumps(doc,ensure_ascii=False,indent=2)+'\n').encode()
    if len(data)>60000:raise ValueError('new plaintext exceeded60000 bytes; complete native is retained')
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(data)


def actual(p,run):
    return (p.get('repository')=='Rogerhu12/math-research-public'
        and str(p.get('run_id'))==str(run) and p.get('complete') and not p.get('failure')
        and p.get('children') and all(c.get('actual_returncode')==0 for c in p['children']))


class QuarterHessianGreenWorker(ReviewedBodyWorker):
    def __init__(self,a):
        super().__init__(a)
        self.name=f'run-{self.run_label}-native-point-Hessian-cut-Green'
        self.dest=TOPIC/FOLDER/self.name
        self.reused_complete=False
        self.state.update(kind='actual_public_same_Z_native_point_Hessian_reweighted_Green_process_v1',
            worker_source_sha256=digest(__file__),original_same_Z_Green_run=a.green_run,
            original_complete_cut_run=a.cut_run,original_particular_Hessian_run=a.hessian_run,
            original_complete_quarter_run=a.quarter_run,
            original_Riccati_projector_or_Green_source_propagations_recomputed=0,
            original_body_cap_endpoint_or_Hessian_source_cells_recomputed=0,
            actual_full_PDE_response_error_proved=False,complete_infinite_BVP_inverse_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='same_Z_native_point_Hessian_cut_and_cached_Green_public_inputs_v1':
            raise ValueError('the independent exact reweighting manifest is required')

    def exact_native(self,root,logical,p,expected=None):
        records=[x for x in p.get('native_files',[]) if x.get('logical_file')==logical]
        if len(records)!=1:raise ValueError('a unique exact original native receipt is required')
        entry=records[0]
        if expected is not None and entry['sha256']!=expected:raise ValueError('the original pinned native differs')
        target=root/logical
        if not target.exists():
            if 'lossless_manifest' not in entry:raise ValueError('the complete original bytes are absent')
            target=self.work/('restored-'+entry['sha256']+'.json.gz')
            if not target.exists():restore(root/entry['lossless_manifest'],target)
        if digest(target)!=entry['sha256'] or target.stat().st_size!=entry['bytes']:
            raise ValueError('the exact native byte identity or size changed')
        return target

    def original_inputs(self):
        inputs={}
        specs=(
            ('same-z-green','green-process',self.args.same_z_artifact,self.args.green_run,
             'native/complete-finite193-same-Z-known-source-Green.json.gz','eb34e2506c1cda9c1f53b4ef44605d02034e0cddf3feef44593edd635506bb18'),
            ('cut-source','cut-process',self.args.cut_artifact,self.args.cut_run,
             'native/complete1977-cut-direction-and-same-Z-sources.json.gz','8bc061ec200deb37548005297a1530d341eaa55065e70104cc5d82714aed21c5'),
            ('particular-hessian','hessian-process',self.args.hessian_artifact,self.args.hessian_run,
             'native/complete-missing-native-point-Hessian.json.gz',None))
        for name,process_name,root,run,logical,expected in specs:
            root=root.resolve();pp=root/'process.json';p=read(pp)
            if not actual(p,run):raise ValueError('the original '+name+' did not actually succeed')
            native=self.exact_native(root,logical,p,expected)
            if p.get('complete_native_sha256')!=digest(native):raise ValueError('the original successful result identity changed')
            pins=self.manifest['actual_input_process_permissions'][name]
            if (p.get('worker_source_sha256')!=pins['worker_sha256']
                or p.get('input_manifest_sha256')!=pins['manifest_sha256']):
                raise ValueError('the successful '+name+' is not the frozen complete source')
            inputs[name]=native;inputs[process_name]=pp
            shutil.copyfile(pp,self.evidence/('original-'+process_name+'.json'))
        hessian=read(inputs['particular-hessian'])
        expected_native=hessian['input_sha256']['quarter']
        expected_process=hessian['input_sha256']['quarter-process']
        found=[]
        for root in sorted(self.args.quarter_artifacts.resolve().iterdir()):
            pp=root/'process.json'
            if not root.is_dir() or not pp.exists():continue
            p=read(pp)
            if digest(pp)!=expected_process:continue
            if (not actual(p,self.args.quarter_run) or p.get('phase')!='finish'
                or p.get('worker_source_sha256')!='cdaebcd03696c86249dc2cb0798a39fb4e4fabef92259af7ec3fcbe63c12a9e2'
                or p.get('input_manifest_sha256')!='b141f6d9be92cb86fc06b49933bfb005eb0de383eef5dd8bd91a6c347d8b1263'
                or p.get('complete_native_sha256')!=expected_native):
                raise ValueError('the exact completed quarter finish process changed')
            native=self.exact_native(root,'native/complete1977-fixed-eta-quarter-cap-sources.json.gz',p,expected_native)
            found.append((native,pp))
        if len(found)!=1:raise ValueError('one precise quarter receipt selected by the cached Hessian is required')
        native,pp=found[0];inputs.update({'quarter':native,'quarter-process':pp})
        shutil.copyfile(pp,self.evidence/'original-quarter-process.json')
        if (hessian.get('actual_original_quarter_run')!=self.args.quarter_run
            or read(inputs['hessian-process']).get('actual_original_quarter_run')!=self.args.quarter_run):
            raise ValueError('the complete cached Hessian and quarter workflow runs differ')
        inputs['cut']=self.science/self.manifest['original_cut_input']
        if read(inputs['green-process']).get('complete_cut_source_run')!=self.args.cut_run:
            raise ValueError('the cut artifact is not the original actual Green input')
        return inputs

    def completed(self,input_sha):
        root=TOPIC/FOLDER
        if not root.exists():return None
        for pp in sorted(root.glob('*/process.json')):
            p=read(pp)
            if (p.get('repository')!='Rogerhu12/math-research-public'
                or not any(c.get('label')==LABEL and c.get('actual_returncode')==0 for c in p.get('children',[]))):continue
            records=[x for x in p.get('native_files',[]) if x.get('logical_file')=='native/'+NATIVE]
            if len(records)!=1:continue
            native=self.exact_native(pp.parent,'native/'+NATIVE,p,records[0]['sha256']);d=read(native)
            if (d.get('complete') and not d.get('failure')
                and d.get('source_sha256')==self.manifest['files'][PRODUCER]
                and d.get('input_sha256')==input_sha and d.get('gates')
                and all(g['passed'] for g in d['gates'])
                and d.get('complete_finite193_compressed_response_error_bound_proved')):
                return pp,native
        return None

    def execute(self,label,command):
        try:return super().execute(label,command)
        finally:
            path=self.cache/NATIVE
            if path.exists():
                d=read(path)
                out=dict(complete=d.get('complete'),failure=d.get('failure'),gates=d.get('gates',[]),
                    native_sha256=digest(path),actual_rescaled_segments=d.get('actual_rescaled_continuous_segments'),
                    original_complete_native_reused=self.reused_complete)
                small(self.evidence/'actual-latest-child-outcome.json',out);print(json.dumps(out),flush=True)
                if d.get('failure') and self.log.exists():print(self.log.read_text()[-16000:],flush=True)

    def prepare(self):
        inputs=self.original_inputs();input_sha={k:digest(v) for k,v in inputs.items()}
        self.state['actual_input_sha256']=input_sha;native=self.cache/NATIVE
        command=[sys.executable,'-u',str(self.science/PRODUCER),'--out',str(native),
            '--green-run',str(self.args.green_run),'--cut-run',str(self.args.cut_run),
            '--hessian-run',str(self.args.hessian_run),'--quarter-run',str(self.args.quarter_run)]
        for key,path in inputs.items():command+=['--'+key,str(path)]
        previous=self.completed(input_sha)
        if previous:
            pp,path=previous;command+=['--resume',str(path)];self.reused_complete=True
            shutil.copyfile(pp,self.evidence/'original-complete-reweight-process.json')
            small(self.evidence/'original-complete-reweight-reuse.json',dict(
                original_process_sha256=digest(pp),original_native_sha256=digest(path),
                original_process_complete=read(pp).get('complete'),
                actual_original_child_returncode=0,all_complete_scientific_and_input_identities_verified=True))
        self.publish();self.execute(LABEL,command)
        d=read(native)
        if (not d.get('complete') or d.get('failure')
            or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or d.get('input_sha256')!=input_sha or not d.get('gates')
            or not all(g['passed'] for g in d['gates'])
            or len(d.get('complete_refined_same_Z_source_profiles',[]))!=6391
            or not d.get('complete_finite193_compressed_response_error_bound_proved')
            or d.get('actual_full_PDE_response_error_proved') or d.get('complete_infinite_BVP_inverse_proved')):
            raise ValueError('the actual complete reweighted finite Green result failed or changed scope')
        summary={key:value for key,value in d.items() if key!='complete_refined_same_Z_source_profiles'}
        summary.update(native_sha256=digest(native),complete_segments=6391,full_original_native_retained=True,
            new_profile_rescalings_in_this_child=0 if self.reused_complete else 6391)
        small(self.evidence/'complete-native-point-Hessian-cut-and-Green-summary.json',summary)
        self.state.update(complete=True,complete_native_sha256=digest(native),actual_scientific_gates=len(d['gates']),
            complete_finite193_compressed_response_error_bound_proved=True,
            complete_finite193_same_Z_error_L2_bounds=d['complete_finite193_same_Z_error_L2_bounds'],
            complete_finite193_negative_error_upper_below_one_over200=d['complete_finite193_negative_error_upper_below_one_over200'],
            new_profile_rescalings_in_this_child=summary['new_profile_rescalings_in_this_child'])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','work','artifact-dir','same-z-artifact','cut-artifact','hessian-artifact','quarter-artifacts'):
        p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    for name in ('green-run','cut-run','hessian-run','quarter-run'):p.add_argument('--'+name,type=int,required=True)
    p.add_argument('--compute-minutes',type=int,default=25)
    p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='same-Z-native-point-Hessian-Green';a.mode='prepare';a.first=0;a.end=0
    a.recovery_manifest=None;a.recovery_sha=None
    worker=QuarterHessianGreenWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()

if __name__=='__main__':main()
