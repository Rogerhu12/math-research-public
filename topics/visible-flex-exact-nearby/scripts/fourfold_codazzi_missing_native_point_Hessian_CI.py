#!/usr/bin/env python3
"""Run only missing native scalar points and preserve every earlier success."""
from __future__ import annotations
import argparse,json,shutil,signal,sys
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_cached_quarter_centre_Hessian_CI_v2 import CachedQuarterHessianWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC

REL='topics/visible-flex-exact-nearby/'
PRODUCER=REL+'scripts/fourfold_codazzi_missing_native_point_Hessian.py'
FOLDER='notes/missing_native_point_Hessian_ci'
NATIVE='complete-missing-native-point-Hessian.json.gz'
LABEL='actual_missing_native_points_and_same_w0_Hessian'
KIND='actual_missing_native_point_same_w0_Hessian_v1'
OLD_NATIVE='8d652d2515359e3ad1bf91c8ad03fbf66a646ddf0b6bdef1f0aa20d2adcbf12c'
OLD_PROCESS='cd7fdccd2e87f0099b9bde6a82774cc2ddc827ea52b8b06f9664b1514721d5e8'
TAYLOR_NATIVE='f85bddc8c1ac7e30a6790818fb52596c88e193fff9312cd4f2bfe20b07549759'


def small(path,data):
    raw=(json.dumps(data,ensure_ascii=False,indent=2)+'\n').encode()
    if len(raw)>60000:raise ValueError('small native-point evidence exceeds60000 bytes; preserve the full native')
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(raw)


class NativePointWorker(CachedQuarterHessianWorker):
    def __init__(self,a):
        super().__init__(a)
        self.name=f'run-{self.run_label}-missing-native-point-Hessian'
        self.dest=TOPIC/FOLDER/self.name;self.reused_complete=False
        self.state.update(kind='actual_public_missing_native_point_Hessian_process_v1',
            worker_source_sha256=digest(__file__),original_cached_Hessian_run=43628443697,
            original_complete_Taylor_Hessian_run=43633412397,
            original7908_whole_target_domains_recomputed=0,
            original7844_successful_residuals_recomputed=0,original_Taylor64_residual_rows_preserved=True,
            original_trial_norm_domains_recomputed=0,
            new_native_point_domain_limit=64,new_point_residual_domain_limit=64,
            actual_full_PDE_response_error_proved=False,complete_infinite_BVP_inverse_proved=False)

    def check_inputs(self):
        ReviewedBodyWorker.check_inputs(self)
        if self.manifest.get('kind')!='missing_native_point_Hessian_public_inputs_v1':
            raise ValueError('the separate exact native-point/Hessian manifest is required')

    def previous_hessian(self):
        root=self.args.previous_hessian_artifact.resolve();pp=root/'process.json';p=read(pp)
        if (digest(pp)!=OLD_PROCESS or p.get('repository')!='Rogerhu12/math-research-public'
            or str(p.get('run_id'))!='43628443697' or not p.get('complete') or p.get('failure')
            or p.get('worker_source_sha256')!='b5029d5d69085114cef9219007488f1780e53e9d5ad73f44c3a0d88500ed9d64'
            or p.get('input_manifest_sha256')!='47ff50fc768a24269ea7dab3de284581fdf8be1abd04fb867d4a55be78b1368d'
            or p.get('complete_native_sha256')!=OLD_NATIVE or not p.get('children')
            or any(c.get('actual_returncode')!=0 for c in p['children'])):
            raise ValueError('the exact actual completed cached-Hessian process is required')
        native=self.exact_native(root,'complete-cached-quarter-centre-residual-Hessian.json.gz',p,OLD_NATIVE)
        shutil.copyfile(pp,self.evidence/'original-complete-cached-Hessian-process.json')
        return {'previous-hessian':native,'previous-process':pp}

    def actual_taylor(self):
        root=self.args.taylor_artifact.resolve();pp=root/'process.json';p=read(pp)
        if (p.get('repository')!='Rogerhu12/math-research-public'
            or str(p.get('run_id'))!='43633412397' or not p.get('complete') or p.get('failure')
            or p.get('worker_source_sha256')!='5ea4af7652c92b89b7570fde1a9a187ff24be1a37a6fdd357ddc45efccac9963'
            or p.get('input_manifest_sha256')!='890c5f9d9c5251ddf7d545b4c373fd96d35dfca5782b9137651374be367a14fd'
            or p.get('complete_native_sha256')!=TAYLOR_NATIVE or not p.get('children')
            or any(c.get('actual_returncode')!=0 for c in p['children'])):
            raise ValueError('the actual successful zero-target Taylor artifact process is required')
        native=self.exact_native(root,'complete-missing-midpoint-Taylor-Hessian.json.gz',p,TAYLOR_NATIVE)
        d=read(native)
        if (d.get('source_sha256')!='ebaa3caaca274b36e816dc4c1797cf7367a3ce06d5eb1d8778879e24c0349c3e'
            or not d.get('complete') or d.get('failure') or not d.get('gates')
            or not all(g['passed'] for g in d['gates']) or d.get('new_target_evaluations')!=0):
            raise ValueError('the original completed Taylor mathematics differs')
        shutil.copyfile(pp,self.evidence/'original-complete-Taylor-process.json')
        self.state['actual_Taylor_artifact_process_sha256']=digest(pp)
        return {'actual-taylor':native,'actual-taylor-process':pp,
                'object':self.science/self.manifest['exact_target_object']}

    def new_prefix(self,input_sha):
        root=TOPIC/FOLDER;found=[]
        if not root.exists():return None
        for pp in sorted(root.glob('*/process.json')):
            p=read(pp)
            if (p.get('repository')!='Rogerhu12/math-research-public'
                or p.get('worker_source_sha256')!=digest(__file__)
                or p.get('input_manifest_sha256')!=self.args.manifest_sha
                or p.get('actual_input_sha256')!=input_sha
                or not any(c.get('label')==LABEL for c in p.get('children',[]))):continue
            records=[x for x in p.get('native_files',[]) if x.get('logical_file')=='native/'+NATIVE]
            if len(records)!=1:continue
            native=self.exact_native(pp.parent,NATIVE,p,records[0]['sha256']);d=read(native)
            if (d.get('kind')!=KIND or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
                or d.get('input_sha256')!=input_sha):continue
            complete=(d.get('complete') and not d.get('failure') and d.get('gates')
                and all(g['passed'] for g in d['gates']) and len(d.get('rows',[]))==1341
                and any(c.get('label')==LABEL and c.get('actual_returncode')==0 for c in p['children']))
            score=(1 if complete else 0,len(d.get('new_native_point_cells',[])),
                len(d.get('new_point_residual_rows',[])),len(d.get('updated_local_rows',[])))
            found.append((score,pp,native,bool(complete)))
        return max(found,key=lambda r:r[0]) if found else None

    def execute(self,label,command):
        try:return ReviewedBodyWorker.execute(self,label,command)
        finally:
            native=self.cache/NATIVE
            if native.exists():
                d=read(native)
                out=dict(complete=d.get('complete'),failure=d.get('failure'),gates=d.get('gates',[]),
                    native_sha256=digest(native),complete_native_points=len(d.get('new_native_point_cells',[])),
                    complete_new_point_residuals=len(d.get('new_point_residual_rows',[])),
                    complete_local_updates=len(d.get('updated_local_rows',[])),
                    actual_new_point_target_calls=d.get('new_native_point_evaluations_in_this_child',0),
                    new_whole_target_domains_evaluated=0,original7844_residuals_recomputed=0)
                small(self.evidence/'actual-latest-child-outcome.json',out);print(json.dumps(out),flush=True)
                if d.get('failure') and self.log.exists():print(self.log.read_text()[-16000:],flush=True)

    def prepare(self):
        values=self.original_inputs();values.update(self.quarter_inputs())
        values.update(self.previous_hessian());values.update(self.actual_taylor())
        input_sha={key:digest(path) for key,path in values.items()}
        for label,paths in (('range-native',self.range_natives),('range-process',self.range_processes)):
            input_sha.update({label+'-'+str(i):digest(path) for i,path in enumerate(paths)})
        self.state['actual_input_sha256']=input_sha;native=self.cache/NATIVE
        command=[sys.executable,'-u',str(self.science/PRODUCER),'--out',str(native),
                 '--quarter-run',str(self.args.quarter_run)]
        for key,path in values.items():command+=['--'+key,str(path)]
        command+=['--range-natives',*[str(path) for path in self.range_natives],
                  '--range-processes',*[str(path) for path in self.range_processes]]
        prior=self.new_prefix(input_sha)
        if prior:
            _,pp,path,complete=prior
            shutil.copyfile(pp,self.evidence/'original-exact-native-point-prefix-process.json')
            small(self.evidence/'original-exact-native-point-prefix-reuse.json',dict(
                original_process_sha256=digest(pp),original_native_sha256=digest(path),
                original_process_complete=read(pp).get('complete'),original_native_complete=complete,
                actual_publication_failure=read(pp).get('failure'),
                successful_native_reused_even_if_publication_failed=True))
            if complete:
                shutil.copyfile(path,native);self.reused_complete=True
            else:
                prefix=self.work/'original-exact-native-point-prefix.json.gz'
                shutil.copyfile(path,prefix);command+=['--resume',str(prefix)]
        self.publish()
        if not self.reused_complete:self.execute(LABEL,command)
        d=read(native)
        if (not d.get('complete') or d.get('failure') or d.get('kind')!=KIND
            or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or d.get('input_sha256')!=input_sha or not d.get('gates')
            or not all(g['passed'] for g in d['gates'])
            or len(d.get('rows',[]))!=1341 or d.get('complete_actual_trial_intersections')!=1977
            or d.get('original_completed_residual_domains_reused')!=7844
            or d.get('complete_new_native_point_domains')!=64
            or d.get('complete_new_native_point_residual_domains')!=64
            or d.get('new_whole_target_domains_evaluated')!=0
            or d.get('original7844_completed_residuals_recomputed')!=0
            or d.get('original_Taylor64_residual_rows_preserved_without_recomputation') is not True
            or d.get('complete_true_cut_source_claimed') or d.get('complete_finite193_response_error_proved')
            or d.get('complete_infinite_BVP_inverse_proved')):
            raise ValueError('the actual native-point science failed or changed scope')
        excluded=('rows','new_point_residual_rows','new_native_point_cells','native_point_receipts',
                  'updated_local_rows','original_reused_local_row_receipts')
        summary={key:value for key,value in d.items() if key not in excluded}
        summary.update(native_sha256=digest(native),complete_native_retained=True,
            original_complete_native_point_result_reused_without_any_child=self.reused_complete,
            actual_new_point_residuals_this_child=0 if self.reused_complete else d['new_residual_domains_executed_in_this_child'],
            actual_new_native_points_this_child=0 if self.reused_complete else d['new_native_point_evaluations_in_this_child'])
        small(self.evidence/'complete-missing-native-point-Hessian-summary.json',summary)
        small(self.evidence/'complete-native-point-receipt-inventory.json',dict(
            original_complete_Taylor_native_sha256=TAYLOR_NATIVE,
            original_whole_target_domains_recomputed=0,
            receipts=[dict(request=c['request'],exact_midpoint=c['exact_midpoint'],
                actual_scalar_germ=c['actual_scalar_germ'],
                original_quarter_row_sha256=c['original_quarter_row_sha256'],
                successful_Taylor_derived_cell_sha256=c['successful_Taylor_derived_cell_sha256'],
                refined_midpoint_jets_sha256=c['refined_midpoint_jets_sha256'])
                for c in d['native_point_receipts']],changed_local_indices=d['changed_local_indices']))
        for row in d['updated_local_rows']:
            small(self.evidence/('local-'+str(row['local_source_row']).zfill(4)+'-native-point-Hessian.json'),row)
        self.state.update(complete=True,complete_native_sha256=digest(native),actual_scientific_gates=len(d['gates']),
            actual_new_point_residuals_this_child=summary['actual_new_point_residuals_this_child'],
            actual_new_native_points_this_child=summary['actual_new_native_points_this_child'],
            original_complete_native_point_result_reused_without_any_child=self.reused_complete,
            additive_same_w0_actual_moving_cap_error=d['additive_same_w0_actual_moving_cap_error'])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('manifest','rules','work','artifact-dir','particular-artifact','ordinary-artifact',
                'split-artifact','quarter-artifacts','previous-hessian-artifact','taylor-artifact'):
        p.add_argument('--'+key,type=Path,required=True)
    for key in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+key,required=True)
    p.add_argument('--quarter-run',type=int,required=True)
    p.add_argument('--compute-minutes',type=int,default=50);p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='missing-native-point-Hessian';a.mode='prepare';a.first=0;a.end=0
    a.recovery_manifest=None;a.recovery_sha=None
    worker=NativePointWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
