#!/usr/bin/env python3
"""Publish an independent scalar consumption of already completed Hessian norms."""
from __future__ import annotations
import argparse,json,shutil,signal,sys
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC
from fourfold_native_lossless_parts import restore

REL='topics/visible-flex-exact-nearby/'
PRODUCER=REL+'scripts/fourfold_codazzi_residual_split_cap_Hessian.py'
FOLDER='notes/residual_split_cap_Hessian_ci'
NATIVE='complete-same-w0-residual-split-cap-Hessian.json.gz'
LABEL='actual_complete_same_w0_residual_derivative_split_Hessian'
KIND='actual_same_w0_residual_derivative_split_Hessian_source_v1'


def small(path,doc):
    data=(json.dumps(doc,ensure_ascii=False,indent=2)+'\n').encode()
    if len(data)>60000:raise ValueError('plaintext summary exceeds60000 bytes; preserve full native')
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(data)


class ResidualSplitHessianWorker(ReviewedBodyWorker):
    def __init__(self,a):
        super().__init__(a);self.name=f'run-{self.run_label}-same-w0-residual-split-cap-Hessian'
        self.dest=TOPIC/FOLDER/self.name;self.reused_complete=False
        self.state.update(kind='actual_public_same_w0_residual_split_Hessian_process_v1',
            worker_source_sha256=digest(__file__),original_large_array_reconstructions_executed=0,
            original_target_primitive_trial_or_endpoint_computations_repeated=0,
            original_complete_physical_cap_residual_cells_recomputed=0,
            complete_true_cut_source_claimed=False,complete_finite193_response_error_proved=False,
            complete_infinite_BVP_inverse_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='residual_split_same_w0_cap_Hessian_public_inputs_v1':
            raise ValueError('the exact independent residual split manifest is required')

    def exact_native(self,root,name,process,expected):
        rows=[x for x in process.get('native_files',[]) if x.get('logical_file')=='native/'+name]
        if len(rows)!=1 or rows[0].get('sha256')!=expected:
            raise ValueError('the unique exact logical native receipt is required')
        receipt=rows[0];path=root/'native'/name
        if not path.exists():
            if 'lossless_manifest' not in receipt:raise ValueError('native bytes are absent')
            path=self.work/('restored-'+expected+'.json.gz')
            if not path.exists():restore(root/receipt['lossless_manifest'],path)
        if digest(path)!=expected or path.stat().st_size!=receipt['bytes']:
            raise ValueError('the native complete size or SHA differs')
        return path

    def original_inputs(self):
        result={'local':self.science/self.manifest['local_complete_Hessian_input'],
            'background':self.science/self.manifest['complete_physical_background_input']}
        specs=[
            ('particular',self.args.particular_artifact,43616252389,
             'complete-same-w0-particular-cap-Hessian.json.gz',
             '9360555293def4b1803da05c5c432a8f737ed4f3d62ea2b84c89e7e236ff7650',
             'f5d1f3ffc96f631076d22768d0e4999ba7357231d9f63d8ec68113a3fc7d1cff',
             '9d4e781665ee61de9f99caea51070f87b5d1c62c7106ae4190f0af6a683b7531',
             '47d24bca452b483a9320d89ff707cc273f4a3bff77a0c2bb4b71d5d89d48168d'),
            ('ordinary',self.args.ordinary_artifact,43618931236,
             'complete-same-w0-ordinary-only-cap-Hessian.json.gz',
             'b1ffc21737ba45d1ef8823af9dccc0baba8b100a1169b60c69f6a7a5d1cfda6c',
             '9ffffba7ade5ea593f1e472ce1d7023f0470779ab9a01ccdd6fbb19e8e88d8ec',
             'd6189c9b6663a99a91746b7f4f00e5b4fddba55ecb9291250693e8a275f3673f',
             '7dc64563295143a0a12445a2bbd074c27589521ad668b79810733ef991808bf7')]
        for role,rawroot,run,name,native_sha,source,worker,manifest in specs:
            root=rawroot.resolve();pp=root/'process.json';p=read(pp)
            if (p.get('repository')!='Rogerhu12/math-research-public'
                or str(p.get('run_id'))!=str(run) or not p.get('complete') or p.get('failure')
                or p.get('worker_source_sha256')!=worker or p.get('input_manifest_sha256')!=manifest
                or p.get('complete_native_sha256')!=native_sha or not p.get('children')
                or any(c.get('actual_returncode')!=0 for c in p['children'])):
                raise ValueError('the actual complete original Hessian process is required')
            native=self.exact_native(root,name,p,native_sha);d=read(native)
            if (not d.get('complete') or d.get('failure') or d.get('source_sha256')!=source
                or not d.get('gates') or not all(g['passed'] for g in d['gates'])):
                raise ValueError('the original complete Hessian mathematics is required')
            result[role]=native;result[role+'-process']=pp
            shutil.copyfile(pp,self.evidence/('original-'+role+'-process.json'))
        return result

    def completed(self,input_sha):
        root=TOPIC/FOLDER
        if not root.exists():return None
        for pp in sorted(root.glob('*/process.json')):
            p=read(pp)
            if (p.get('repository')!='Rogerhu12/math-research-public'
                or p.get('worker_source_sha256')!=digest(__file__)
                or p.get('input_manifest_sha256')!=digest(self.args.manifest)
                or not any(c.get('label')==LABEL and c.get('actual_returncode')==0 for c in p.get('children',[]))):
                continue
            receipts=[r for r in p.get('native_files',[]) if r.get('logical_file')=='native/'+NATIVE]
            if len(receipts)!=1 or not isinstance(receipts[0].get('sha256'),str):continue
            native=self.exact_native(pp.parent,NATIVE,p,receipts[0]['sha256']);d=read(native)
            if (d.get('kind')==KIND and d.get('complete') and not d.get('failure')
                and d.get('source_sha256')==self.manifest['files'][PRODUCER]
                and d.get('input_sha256')==input_sha and d.get('complete_local_rows')==1341
                and d.get('complete_actual_trial_intersections')==1977
                and d.get('gates') and all(g['passed'] for g in d['gates'])):
                return pp,native
        return None

    def execute(self,label,command):
        try:return super().execute(label,command)
        finally:
            path=self.cache/NATIVE
            if path.exists():
                d=read(path);out=dict(complete=d.get('complete'),failure=d.get('failure'),
                    gates=d.get('gates',[]),native_sha256=digest(path),
                    original_complete_native_reused=self.reused_complete,
                    original_norms_targets_or_trials_recomputed=0)
                small(self.evidence/'actual-latest-child-outcome.json',out);print(json.dumps(out),flush=True)
                if d.get('failure') and self.log.exists():print(self.log.read_text()[-16000:],flush=True)

    def prepare(self):
        inputs=self.original_inputs();input_sha={k:digest(v) for k,v in inputs.items()}
        self.state['actual_input_sha256']=input_sha;native=self.cache/NATIVE
        command=[sys.executable,'-u',str(self.science/PRODUCER),'--out',str(native)]
        for key,path in inputs.items():command+=['--'+key,str(path)]
        previous=self.completed(input_sha)
        if previous:
            pp,path=previous;command+=['--resume',str(path)];self.reused_complete=True
            shutil.copyfile(pp,self.evidence/'original-complete-consumption-process.json')
            small(self.evidence/'original-complete-consumption-reuse.json',dict(
                original_process_sha256=digest(pp),original_native_sha256=digest(path),
                original_process_complete=read(pp).get('complete'),
                original_publication_failure=read(pp).get('failure'),
                original_actual_child_returncode=0,complete_scientific_identity_verified=True))
        self.publish();self.execute(LABEL,command);d=read(native)
        if (d.get('kind')!=KIND or not d.get('complete') or d.get('failure')
            or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or d.get('input_sha256')!=input_sha or not d.get('gates')
            or not all(g['passed'] for g in d['gates']) or len(d.get('rows',[]))!=1341
            or d.get('complete_actual_trial_intersections')!=1977
            or d.get('complete_true_cut_source_claimed') or d.get('complete_finite193_response_error_proved')
            or d.get('complete_infinite_BVP_inverse_proved')):
            raise ValueError('the actual full split-source result failed or exceeded its scope')
        summary={k:v for k,v in d.items() if k not in ('rows','full_original_matrix_array_sha256')}
        summary.update(native_sha256=digest(native),complete_original_native_retained=True,
            actual_new_scalar_consumptions=0 if self.reused_complete else 1341)
        small(self.evidence/'complete-residual-split-cap-Hessian-summary.json',summary)
        for i in d['diagnostic_local_indices']:
            small(self.evidence/f'local-{i:04d}-source-diagnostic.json',d['rows'][i])
        self.state.update(complete=True,complete_native_sha256=digest(native),actual_scientific_gates=len(d['gates']),
            actual_complete_local_rows=1341,actual_complete_intersections=1977,
            selected_new_decomposition_cell_count=d['selected_new_decomposition_cell_count'],
            additive_same_w0_actual_moving_cap_error=d['additive_same_w0_actual_moving_cap_error'])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','work','artifact-dir','particular-artifact','ordinary-artifact'):
        p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--compute-minutes',type=int,default=20)
    p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='residual-split-cap-Hessian';a.mode='prepare';a.first=0;a.end=0
    a.recovery_manifest=None;a.recovery_sha=None
    worker=ResidualSplitHessianWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()

if __name__=='__main__':main()
