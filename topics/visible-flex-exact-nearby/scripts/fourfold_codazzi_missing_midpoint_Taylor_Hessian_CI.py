#!/usr/bin/env python3
"""Consume exact completed quarter/Hessian artifacts and only missing point data."""
from __future__ import annotations
import argparse,json,shutil,signal,sys
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_cached_quarter_centre_Hessian_CI_v2 import CachedQuarterHessianWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC

REL='topics/visible-flex-exact-nearby/'
PRODUCER=REL+'scripts/fourfold_codazzi_missing_midpoint_Taylor_Hessian.py'
FOLDER='notes/missing_midpoint_Taylor_Hessian_ci'
NATIVE='complete-missing-midpoint-Taylor-Hessian.json.gz'
LABEL='actual_missing_point_Taylor_and_same_w0_Hessian'
KIND='actual_missing_cached_midpoint_Taylor_same_w0_Hessian_v1'
OLD_NATIVE='8d652d2515359e3ad1bf91c8ad03fbf66a646ddf0b6bdef1f0aa20d2adcbf12c'
OLD_PROCESS='cd7fdccd2e87f0099b9bde6a82774cc2ddc827ea52b8b06f9664b1514721d5e8'


def small(path,data):
    raw=(json.dumps(data,ensure_ascii=False,indent=2)+'\n').encode()
    if len(raw)>60000:raise ValueError('small Taylor evidence exceeds60000 bytes; preserve complete native')
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(raw)


class TaylorWorker(CachedQuarterHessianWorker):
    def __init__(self,a):
        super().__init__(a)
        self.name=f'run-{self.run_label}-missing-midpoint-Taylor-Hessian'
        self.dest=TOPIC/FOLDER/self.name;self.reused_complete=False
        self.state.update(kind='actual_public_missing_midpoint_Taylor_Hessian_process_v1',
            worker_source_sha256=digest(__file__),original_cached_Hessian_run=43628443697,
            original7844_successful_residuals_recomputed=0,
            original_target_evaluations_executed=0,original_trial_norm_domains_recomputed=0,
            conditional_new_residual_domains_at_most=64,
            actual_full_PDE_response_error_proved=False,complete_infinite_BVP_inverse_proved=False)

    def check_inputs(self):
        ReviewedBodyWorker.check_inputs(self)
        if self.manifest.get('kind')!='missing_midpoint_Taylor_Hessian_public_inputs_v1':
            raise ValueError('the separate exact Taylor/Hessian manifest is required')

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
            score=(1 if complete else 0,len(d.get('derived_midpoint_cells',[])),
                len(d.get('new_missing_residual_rows',[])),len(d.get('updated_local_rows',[])))
            found.append((score,pp,native,bool(complete)))
        return max(found,key=lambda r:r[0]) if found else None

    def execute(self,label,command):
        try:return ReviewedBodyWorker.execute(self,label,command)
        finally:
            native=self.cache/NATIVE
            if native.exists():
                d=read(native)
                out=dict(complete=d.get('complete'),failure=d.get('failure'),gates=d.get('gates',[]),
                    native_sha256=digest(native),
                    actual_fallback_budget_diagnostic=d.get('actual_fallback_budget_diagnostic'),
                    complete_derived_midpoints=len(d.get('derived_midpoint_cells',[])),
                    complete_new_missing_residuals=len(d.get('new_missing_residual_rows',[])),
                    complete_local_updates=len(d.get('updated_local_rows',[])),
                    original7844_residuals_recomputed=0,new_target_evaluations=0)
                small(self.evidence/'actual-latest-child-outcome.json',out);print(json.dumps(out),flush=True)
                if d.get('failure') and self.log.exists():print(self.log.read_text()[-16000:],flush=True)

    def prepare(self):
        values=self.original_inputs();values.update(self.quarter_inputs());values.update(self.previous_hessian())
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
            shutil.copyfile(pp,self.evidence/'original-exact-Taylor-prefix-process.json')
            small(self.evidence/'original-exact-Taylor-prefix-reuse.json',dict(
                original_process_sha256=digest(pp),original_native_sha256=digest(path),
                original_process_complete=read(pp).get('complete'),original_native_complete=complete,
                actual_publication_failure=read(pp).get('failure'),
                successful_native_reused_even_if_publication_failed=True))
            if complete:
                shutil.copyfile(path,native);self.reused_complete=True
            else:
                prefix=self.work/'original-exact-Taylor-prefix.json.gz'
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
            or d.get('complete_new_missing_point_residual_domains',1000)>64
            or d.get('new_target_evaluations')!=0
            or d.get('original7844_completed_residuals_recomputed')!=0
            or d.get('complete_true_cut_source_claimed') or d.get('complete_finite193_response_error_proved')
            or d.get('complete_infinite_BVP_inverse_proved')):
            raise ValueError('the actual missing-point Taylor science failed or changed scope')
        excluded=('rows','new_missing_residual_rows','derived_midpoint_cells','midpoint_derivation_receipts',
                  'updated_local_rows','original_reused_local_row_receipts')
        summary={key:value for key,value in d.items() if key not in excluded}
        summary.update(native_sha256=digest(native),complete_native_retained=True,
            original_complete_Taylor_native_reused_without_any_child=self.reused_complete,
            actual_new_missing_residuals_this_child=0 if self.reused_complete else d['new_residual_domains_executed_in_this_child'],
            actual_new_Taylor_points_this_child=0 if self.reused_complete else d['new_Taylor_midpoint_derivations_executed'])
        small(self.evidence/'complete-missing-midpoint-Taylor-Hessian-summary.json',summary)
        small(self.evidence/'actual-original-fallback-group-budget.json',d['actual_fallback_budget_diagnostic'])
        small(self.evidence/'complete-midpoint-receipt-inventory.json',dict(
            original_complete_cached_Hessian_native_sha256=OLD_NATIVE,
            original7844_residuals_recomputed=0,new_target_evaluations=0,
            receipts=[dict(request=c['request'],original_quarter_row_sha256=c['original_quarter_row_sha256'],
                derived_midpoint_jets_sha256=c['derived_midpoint_jets_sha256'],
                original_anchor_count=len(c['original_anchor_receipts']))
                for c in d['midpoint_derivation_receipts']],
            unavailable=d['unavailable_midpoints'],changed_local_indices=d['changed_local_indices']))
        self.state.update(complete=True,complete_native_sha256=digest(native),actual_scientific_gates=len(d['gates']),
            actual_fallback_budget_diagnostic=d['actual_fallback_budget_diagnostic'],
            actual_new_missing_residuals_this_child=summary['actual_new_missing_residuals_this_child'],
            actual_new_Taylor_points_this_child=summary['actual_new_Taylor_points_this_child'],
            original_complete_Taylor_native_reused_without_any_child=self.reused_complete,
            original_local_rows_retained_for_missing_midpoints=d['original_local_rows_retained_for_missing_midpoints'],
            additive_same_w0_actual_moving_cap_error=d['additive_same_w0_actual_moving_cap_error'])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('manifest','rules','work','artifact-dir','particular-artifact','ordinary-artifact',
                'split-artifact','quarter-artifacts','previous-hessian-artifact'):
        p.add_argument('--'+key,type=Path,required=True)
    for key in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+key,required=True)
    p.add_argument('--quarter-run',type=int,required=True)
    p.add_argument('--compute-minutes',type=int,default=50);p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='missing-midpoint-Taylor-Hessian';a.mode='prepare';a.first=0;a.end=0
    a.recovery_manifest=None;a.recovery_sha=None
    worker=TaylorWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
