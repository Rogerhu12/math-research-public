#!/usr/bin/env python3
"""Consume completed quarter target jets and preserve exact centre-residual prefixes."""
from __future__ import annotations
import argparse,json,shutil,signal,sys
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_residual_split_cap_Hessian_CI import ResidualSplitHessianWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC

REL='topics/visible-flex-exact-nearby/'
PRODUCER=REL+'scripts/fourfold_codazzi_cached_quarter_centre_Hessian.py'
FOLDER='notes/cached_quarter_centre_Hessian_ci'
NATIVE='complete-cached-quarter-centre-residual-Hessian.json.gz'
LABEL='actual_complete_cached_quarter_centre_residual_Hessian'
KIND='actual_cached_quarter_centre_residual_same_w0_Hessian_v1'
QUARTER_SOURCE='54e5ec52033bb109618fde1c840730b4b589280382b2da196d3ea748af4490de'
QUARTER_WORKER='04d4380d840504f3aedf2da2d95f2112677819885f4a1e367480f97298b332db'
QUARTER_MANIFEST='6dc5bf2d8030d506c74dc29ef2cb3c1991cd5f7fb8c2a051b03b0ad89cb2fb69'
RANGES=((0,256),(256,512),(512,768),(768,1024),(1024,1280),(1280,1536),(1536,1792),(1792,1977))


def small(path,doc):
    raw=(json.dumps(doc,ensure_ascii=False,indent=2)+'\n').encode()
    if len(raw)>60000:raise ValueError('new plaintext summary exceeds60000 bytes; retain native')
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(raw)


def proved(d):
    return d.get('complete') and not d.get('failure') and d.get('gates') and all(g['passed'] for g in d['gates'])


def actual(p,run):
    return (p.get('repository')=='Rogerhu12/math-research-public' and str(p.get('run_id'))==str(run)
        and p.get('complete') and not p.get('failure') and p.get('children')
        and all(c.get('actual_returncode')==0 for c in p['children']))


class CachedQuarterHessianWorker(ResidualSplitHessianWorker):
    def __init__(self,a):
        super().__init__(a);self.name=f'run-{self.run_label}-cached-quarter-centre-residual-Hessian'
        self.dest=TOPIC/FOLDER/self.name;self.reused_complete=False
        self.state.update(kind='actual_public_cached_quarter_centre_Hessian_process_v1',
            worker_source_sha256=digest(__file__),actual_original_quarter_run=a.quarter_run,
            original_target_evaluations_executed=0,original_large_array_reconstructions_executed=0,
            original_physical_cap_residual_domains_recomputed=0,
            original_trial_norm_domains_recomputed=0,exact_affine_parameter_offset='0',
            complete_true_cut_source_claimed=False,complete_finite193_response_error_proved=False,
            complete_infinite_BVP_inverse_proved=False)

    def check_inputs(self):
        ReviewedBodyWorker.check_inputs(self)
        if self.manifest.get('kind')!='cached_quarter_centre_Hessian_public_inputs_v1':
            raise ValueError('the exact independent cached-quarter Hessian manifest is required')

    def original_inputs(self):
        result=super().original_inputs()
        result['candidate']=self.science/self.manifest['published_candidate']
        root=self.args.split_artifact.resolve();pp=root/'process.json';p=read(pp)
        expected='85b6bbb899ab04549131fd20a7b16209056e2a51cb012bffbd7a6ae590b047c5'
        if (not actual(p,43621690619)
            or p.get('worker_source_sha256')!='0f5bb7c3c747a5e62ac52b40d17ee7dda398f044c30c6c723dccc4b8e7eb0b9b'
            or p.get('input_manifest_sha256')!='a3b144b5a6e8c9d84c369f97aac1e849e3035bb7067c461ed574b53b1069d842'
            or p.get('complete_native_sha256')!=expected):
            raise ValueError('the actual complete original residual-split process differs')
        native=self.exact_native(root,'complete-same-w0-residual-split-cap-Hessian.json.gz',p,expected)
        d=read(native)
        if (not proved(d) or d.get('source_sha256')!='a8b1a68d1be78b6288aa5e6db314caded7f80158045a4e7acb959c7e84c25317'
            or d.get('complete_local_rows')!=1341 or d.get('complete_actual_trial_intersections')!=1977):
            raise ValueError('the actual complete original residual-split science differs')
        result.update(split=native);result['split-process']=pp
        shutil.copyfile(pp,self.evidence/'original-residual-split-process.json')
        return result

    def quarter_inputs(self):
        records=[]
        for root in sorted(self.args.quarter_artifacts.resolve().iterdir()):
            pp=root/'process.json'
            if not root.is_dir() or not pp.exists():continue
            p=read(pp)
            if (p.get('repository')!='Rogerhu12/math-research-public'
                or str(p.get('run_id'))!=str(self.args.quarter_run)):
                raise ValueError('a received artifact is from a different public quarter run')
            if (p.get('worker_source_sha256')!=QUARTER_WORKER
                or p.get('input_manifest_sha256')!=QUARTER_MANIFEST):
                raise ValueError('a received quarter artifact has another frozen scientific identity')
            if actual(p,self.args.quarter_run):records.append((root,pp,p))
        finish=[x for x in records if x[2].get('phase')=='finish']
        if not finish:raise ValueError('an actual successful complete quarter finish is required')
        root,pp,p=max(finish,key=lambda x:int(x[2].get('run_attempt','1')))
        expected=p.get('complete_native_sha256')
        if not isinstance(expected,str):raise ValueError('the exact finish native receipt is missing')
        native=self.exact_native(root,'complete1977-fixed-eta-quarter-cap-sources.json.gz',p,expected)
        full=read(native)
        if (not proved(full) or full.get('source_sha256')!=QUARTER_SOURCE
            or full.get('complete_original_parent_cells')!=1977
            or full.get('completed_new_quarter_domains')!=7844 or full.get('complete_quarter_domains')!=7908):
            raise ValueError('the exact completed full quarter science is required')
        out={'quarter':native,'quarter-process':pp}
        shutil.copyfile(pp,self.evidence/'original-complete-quarter-finish-process.json')
        plan_sha=full['plan_native_sha256']
        plans=[x for x in records if x[2].get('phase')=='plan' and x[2].get('complete_native_sha256')==plan_sha]
        if not plans:raise ValueError('the exact original common quarter plan is absent')
        root,pp,p=max(plans,key=lambda x:int(x[2].get('run_attempt','1')))
        plan=self.exact_native(root,'complete1977-fixed-eta-quarter-plan.json.gz',p,plan_sha);pd=read(plan)
        if not proved(pd) or pd.get('source_sha256')!=QUARTER_SOURCE:
            raise ValueError('the exact original quarter plan science is required')
        out.update({'quarter-plan':plan,'quarter-plan-process':pp})
        shutil.copyfile(pp,self.evidence/'original-complete-quarter-plan-process.json')
        receipts={tuple(r['range']):r for r in full['range_receipts']}
        self.range_natives=[];self.range_processes=[]
        for first,end in RANGES:
            receipt=receipts[(first,end)]
            matches=[x for x in records if x[2].get('phase')=='range'
                and x[2].get('source_range')==[first,end]
                and digest(x[1])==receipt['actual_original_process_sha256']
                and x[2].get('complete_native_sha256')==receipt['native_sha256']
                and x[2].get('actual_plan_native_sha256')==plan_sha]
            if len(matches)!=1:raise ValueError('the precise successful range receipt selected by finish is required')
            root,pp,p=matches[0]
            path=self.exact_native(root,f'new-fixed-eta-quarter-domains-{first:04d}-{end:04d}.json.gz',
                p,receipt['native_sha256'])
            self.range_natives.append(path);self.range_processes.append(pp)
            shutil.copyfile(pp,self.evidence/f'original-quarter-range-{first:04d}-{end:04d}-process.json')
        self.state['actual_original_quarter_finish_native_sha256']=digest(native)
        self.state['actual_original_quarter_plan_native_sha256']=plan_sha
        return out

    def best_prefix(self,input_sha):
        folder=TOPIC/FOLDER
        if not folder.exists():return None
        found=[]
        for pp in sorted(folder.glob('*/process.json')):
            p=read(pp)
            if (p.get('repository')!='Rogerhu12/math-research-public'
                or p.get('worker_source_sha256')!=digest(__file__)
                or p.get('input_manifest_sha256')!=self.args.manifest_sha):
                continue
            receipts=[r for r in p.get('native_files',[]) if r.get('logical_file')=='native/'+NATIVE]
            if len(receipts)!=1 or not isinstance(receipts[0].get('sha256'),str):continue
            native=self.exact_native(pp.parent,NATIVE,p,receipts[0]['sha256']);d=read(native)
            if (d.get('kind')!=KIND or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
                or d.get('input_sha256')!=input_sha):continue
            complete=bool(proved(d) and d.get('complete_local_rows')==1341)
            if complete and not any(c.get('label')==LABEL and c.get('actual_returncode')==0 for c in p.get('children',[])):
                continue
            count=len(d.get('new_quarter_residual_rows',[]))
            if complete or count:found.append((complete,count,pp,native))
        return max(found,key=lambda x:(x[0],x[1])) if found else None

    def execute(self,label,command):
        try:return ReviewedBodyWorker.execute(self,label,command)
        finally:
            path=self.cache/NATIVE
            if path.exists():
                d=read(path);out=dict(complete=d.get('complete'),failure=d.get('failure'),
                    gates=d.get('gates',[]),native_sha256=digest(path),
                    complete_residual_domains=len(d.get('new_quarter_residual_rows',[])),
                    actual_new_residual_domains=0 if self.reused_complete else d.get('new_residual_domains_executed_in_this_child',0),
                    original_complete_native_reused=self.reused_complete,new_target_evaluations=0)
                small(self.evidence/'actual-latest-child-outcome.json',out);print(json.dumps(out),flush=True)
                if d.get('failure') and self.log.exists():print(self.log.read_text()[-16000:],flush=True)

    def prepare(self):
        values=self.original_inputs();values.update(self.quarter_inputs())
        input_sha={k:digest(v) for k,v in values.items()}
        for label,paths in (('range-native',self.range_natives),('range-process',self.range_processes)):
            input_sha.update({label+'-'+str(i):digest(path) for i,path in enumerate(paths)})
        self.state['actual_input_sha256']=input_sha
        native=self.cache/NATIVE
        command=[sys.executable,'-u',str(self.science/PRODUCER),'--out',str(native),
            '--quarter-run',str(self.args.quarter_run)]
        for key,path in values.items():command+=['--'+key,str(path)]
        command+=['--range-natives',*[str(p) for p in self.range_natives],
            '--range-processes',*[str(p) for p in self.range_processes]]
        previous=self.best_prefix(input_sha)
        if previous:
            complete,count,pp,path=previous;command+=['--resume',str(path)];self.reused_complete=complete
            shutil.copyfile(pp,self.evidence/'original-successful-residual-prefix-process.json')
            small(self.evidence/'original-successful-residual-prefix-reuse.json',dict(
                original_process_sha256=digest(pp),original_native_sha256=digest(path),
                original_process_complete=read(pp).get('complete'),
                original_publication_failure=read(pp).get('failure'),
                original_completed_residual_domains=count,original_native_complete=complete,
                previously_completed_residual_domains_recomputed=0))
        self.publish();self.execute(LABEL,command);d=read(native)
        if (d.get('kind')!=KIND or not proved(d)
            or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or d.get('input_sha256')!=input_sha or len(d.get('rows',[]))!=1341
            or d.get('complete_actual_trial_intersections')!=1977
            or d.get('original_target_evaluations_executed')!=0
            or d.get('original_physical_cap_residual_domains_recomputed')!=0
            or d.get('complete_true_cut_source_claimed') or d.get('complete_finite193_response_error_proved')
            or d.get('complete_infinite_BVP_inverse_proved')):
            raise ValueError('the complete cached-quarter Hessian science failed or exceeded its scope')
        summary={k:v for k,v in d.items() if k not in
            ('rows','new_quarter_residual_rows','full_original_matrix_array_sha256')}
        summary.update(native_sha256=digest(native),complete_original_native_retained=True,
            original_complete_native_reused=self.reused_complete,
            actual_new_residual_domains=0 if self.reused_complete else d['new_residual_domains_executed_in_this_child'])
        small(self.evidence/'complete-cached-quarter-centre-Hessian-summary.json',summary)
        for i in d['diagnostic_local_indices']:
            small(self.evidence/f'local-{i:04d}-cached-centre-Hessian-diagnostic.json',d['rows'][i])
        self.state.update(complete=True,complete_native_sha256=digest(native),actual_scientific_gates=len(d['gates']),
            actual_complete_local_rows=1341,actual_complete_intersections=1977,
            actual_completed_new_residual_domains=d['complete_new_residual_domains'],
            original_local_rows_retained_for_missing_midpoints=d['original_local_rows_retained_for_missing_midpoints'],
            additive_same_w0_actual_moving_cap_error=d['additive_same_w0_actual_moving_cap_error'])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('manifest','rules','work','artifact-dir','particular-artifact','ordinary-artifact','split-artifact','quarter-artifacts'):
        p.add_argument('--'+key,type=Path,required=True)
    for key in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+key,required=True)
    p.add_argument('--quarter-run',type=int,required=True)
    p.add_argument('--compute-minutes',type=int,default=75);p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='cached-quarter-centre-Hessian';a.mode='prepare';a.first=0;a.end=0
    a.recovery_manifest=None;a.recovery_sha=None
    worker=CachedQuarterHessianWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()

if __name__=='__main__':main()
