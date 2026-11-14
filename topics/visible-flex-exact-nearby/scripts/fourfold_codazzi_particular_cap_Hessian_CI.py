#!/usr/bin/env python3
"""Run only the particular cap Hessian; preserve exact successful output and prefixes."""
from __future__ import annotations
import argparse,json,shutil,signal,sys
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_known_cut_direction_cap_CI_v3 import KnownCutDirectionWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC
from fourfold_native_lossless_parts import restore

REL='topics/visible-flex-exact-nearby/'
PRODUCER=REL+'scripts/fourfold_codazzi_particular_cap_Hessian.py'
FOLDER='notes/particular_cap_Hessian_ci'
NATIVE='complete-same-w0-particular-cap-Hessian.json.gz'
LABEL='actual_complete_same_w0_particular_cap_Hessian'
PILOT='f36831b1f5cc354548686c7d3e5f3fdfb10a456899d25f57d1be1b4cefccbe5c'
PILOT_PROCESS='c6d87b7e9d5ca64c480c34853a5b17e3ca61f0e18417817591f11afa21879cb4'


def small(path,doc):
    data=(json.dumps(doc,ensure_ascii=False,indent=2)+'\n').encode()
    if len(data)>60000:raise ValueError('new plaintext exceeds60000 bytes; the full native remains preserved')
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(data)


class ParticularHessianWorker(ReviewedBodyWorker):
    def __init__(self,a):
        super().__init__(a)
        self.name=f'run-{self.run_label}-same-w0-particular-cap-Hessian'
        self.dest=TOPIC/FOLDER/self.name
        self.reused_complete=False
        self.state.update(kind='actual_public_same_w0_particular_cap_Hessian_process_v1',
            worker_source_sha256=digest(__file__),original_large_matrix_reconstructions_executed=0,
            original_complete_physical_residual_cells_recomputed=0,
            original_target_primitive_endpoint_or_mean_computations_repeated=0,
            complete_true_cut_source_claimed=False,complete_finite193_response_error_proved=False,
            complete_infinite_BVP_inverse_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='particular_same_w0_cap_Hessian_public_inputs_v1':
            raise ValueError('the exact independent particular Hessian manifest is required')

    def exact_native(self,root,name,process,expected):
        entries=[x for x in process.get('native_files',[]) if x.get('logical_file')=='native/'+name]
        if len(entries)!=1 or entries[0].get('sha256')!=expected:
            raise ValueError('the exact unique native receipt is required')
        entry=entries[0];path=root/'native'/name
        if not path.exists():
            if 'lossless_manifest' not in entry:raise ValueError('the original complete native bytes are absent')
            path=self.work/('restored-'+expected+'.json.gz')
            if not path.exists():restore(root/entry['lossless_manifest'],path)
        if digest(path)!=expected or path.stat().st_size!=entry['bytes']:
            raise ValueError('native identity or complete size differs')
        return path

    def original_inputs(self):
        candidate,proposal=KnownCutDirectionWorker.restore_exact_prepared_arrays(self)
        root=self.args.pilot_artifact.resolve();pp=root/'process.json';p=read(pp)
        if (digest(pp)!=PILOT_PROCESS or p.get('repository')!='Rogerhu12/math-research-public'
            or str(p.get('run_id'))!='43610982446' or not p.get('complete') or p.get('failure')
            or not p.get('children') or any(c.get('actual_returncode')!=0 for c in p['children'])):
            raise ValueError('the actual original successful one-column process is required')
        pilot=self.exact_native(root,'known-cut-direction-complete-cap-mixed-source-pilot.json.gz',p,PILOT)
        shutil.copyfile(pp,self.evidence/'original-successful-v3-pilot-process.json')
        return {'proposal':proposal,'pilot':pilot,'pilot-process':pp,
            'local':self.science/self.manifest['local_complete_Hessian_input'],
            'old-hessian':self.science/self.manifest['hessian_input']}

    def prefix(self,input_sha):
        root=TOPIC/FOLDER
        if not root.exists():return None
        candidates=[]
        for pp in sorted(root.glob('*/process.json')):
            p=read(pp)
            if p.get('repository')!='Rogerhu12/math-research-public':continue
            records=[x for x in p.get('native_files',[]) if x.get('logical_file')=='native/'+NATIVE]
            if len(records)!=1 or not isinstance(records[0].get('sha256'),str):continue
            path=self.exact_native(pp.parent,NATIVE,p,records[0]['sha256']);doc=read(path)
            if (doc.get('kind')!='actual_complete_same_w0_particular_cap_Hessian_source_v1'
                or doc.get('source_sha256')!=self.manifest['files'][PRODUCER]
                or doc.get('input_sha256')!=input_sha or not doc.get('rows')):continue
            complete=bool(doc.get('complete') and not doc.get('failure')
                and doc.get('gates') and all(g['passed'] for g in doc['gates']))
            if complete and not any(c.get('label')==LABEL and c.get('actual_returncode')==0 for c in p.get('children',[])):
                continue
            candidates.append((complete,len(doc['rows']),pp,path,doc))
        return max(candidates,key=lambda row:(row[0],row[1])) if candidates else None

    def execute(self,label,command):
        try:return super().execute(label,command)
        finally:
            path=self.cache/NATIVE
            if path.exists():
                d=read(path)
                outcome=dict(complete=d.get('complete'),failure=d.get('failure'),gates=d.get('gates',[]),
                    native_sha256=digest(path),actual_complete_local_rows=len(d.get('rows',[])),
                    original_complete_output_reused_without_new_mathematics=self.reused_complete,
                    actual_new_local_rows_in_this_child=0 if self.reused_complete else d.get('new_local_rows_executed_in_this_child',0),
                    actual_new_intersections_in_this_child=0 if self.reused_complete else d.get('new_Hermite_intersections_executed_in_this_child',0))
                small(self.evidence/'actual-latest-child-outcome.json',outcome)
                print(json.dumps(outcome),flush=True)
                if d.get('failure') and self.log.exists():print(self.log.read_text()[-16000:],flush=True)

    def prepare(self):
        inputs=self.original_inputs();input_sha={k:digest(v) for k,v in inputs.items()}
        self.state['actual_original_input_sha256']=input_sha
        native=self.cache/NATIVE
        command=[sys.executable,'-u',str(self.science/PRODUCER),'--out',str(native)]
        for key,path in inputs.items():command+=['--'+key,str(path)]
        previous=self.prefix(input_sha)
        if previous:
            complete,count,pp,path,doc=previous
            self.reused_complete=complete
            command+=['--resume',str(path)]
            shutil.copyfile(pp,self.evidence/'actual-original-prefix-process.json')
            small(self.evidence/'exact-source-prefix-reuse.json',dict(
                original_process_sha256=digest(pp),original_native_sha256=digest(path),
                original_process_complete=read(pp).get('complete'),original_publication_failure=read(pp).get('failure'),
                native_complete=complete,completed_local_rows=count,
                exact_scientific_source_and_all_input_bytes_verified=True,completed_rows_not_repeated=True))
        self.publish();self.execute(LABEL,command)
        d=read(native)
        if (not d.get('complete') or d.get('failure')
            or d.get('source_sha256')!=self.manifest['files'][PRODUCER] or d.get('input_sha256')!=input_sha
            or d.get('complete_local_rows')!=1341 or d.get('complete_actual_trial_intersections')!=1977
            or not d.get('gates') or not all(g['passed'] for g in d['gates'])
            or d.get('complete_true_cut_source_claimed') or d.get('complete_finite193_response_error_proved')
            or d.get('complete_infinite_BVP_inverse_proved')):
            raise ValueError('the complete particular Hessian result failed or exceeded its scope')
        summary={key:value for key,value in d.items() if key not in ('rows','direction')}
        summary.update(native_sha256=digest(native),full_original_native_retained=True,
            original_complete_output_reused_without_new_mathematics=self.reused_complete,
            actual_new_local_rows_in_this_child=0 if self.reused_complete else d['new_local_rows_executed_in_this_child'],
            actual_new_intersections_in_this_child=0 if self.reused_complete else d['new_Hermite_intersections_executed_in_this_child'])
        small(self.evidence/'complete-same-w0-particular-cap-Hessian-summary.json',summary)
        self.state.update(complete=True,complete_native_sha256=digest(native),actual_scientific_gates=len(d['gates']),
            actual_complete_local_rows=1341,actual_complete_intersections=1977,
            actual_new_local_rows_in_this_child=summary['actual_new_local_rows_in_this_child'],
            actual_new_intersections_in_this_child=summary['actual_new_intersections_in_this_child'],
            additive_same_w0_actual_moving_cap_error=d['additive_same_w0_actual_moving_cap_error'],
            original97_HS_additive_times_same_w0_norm=d['original97_HS_additive_times_same_w0_norm'])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','work','artifact-dir','prepared','pilot-artifact'):
        p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--compute-minutes',type=int,default=45)
    p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='particular-cap-Hessian';a.mode='prepare';a.first=0;a.end=0
    a.recovery_manifest=None;a.recovery_sha=None
    worker=ParticularHessianWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()

if __name__=='__main__':main()
