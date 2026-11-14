#!/usr/bin/env python3
"""Public orchestration for the complete mixed continuous-Z source cover.

The source plan and four actual ranges preserve all original bytes. Every
range resumes its own exact prefix; a successful prefix is consumed by a
zero-new-cell child. Every user-facing summary is checked below60000 bytes.
"""
from __future__ import annotations
import argparse,json,os,shutil,signal,sys
from pathlib import Path
from types import SimpleNamespace
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_body_mean_CI_finish import CompleteMeanWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC,save
from fourfold_native_lossless_parts import restore

REL='topics/visible-flex-exact-nearby/'
PRODUCER=REL+'scripts/fourfold_codazzi_complete_mixed_Z_source_cover.py'
OLD_MANIFEST='c214f800a5094c905c554e9053c52567d5ae5d76be41ac2e3fe9d673b396d784'
BODY='a4f31dccc4b54661b43fc06bac59b6afbb4fa2d6d19614f68f71e044be6e5870'
BODY_PROCESS='0a5dc06520bad5a1230b65cba6e895e998e1f3ce6a32a65d9ffa8800b8ea1a9e'
REPAIR='05e0493dbe55490adec8fb6603e0ec431d1bc03f051aec86be8a78741f60f0a4'
REPAIR_PROCESS='16de872ce106e05b6add99d8406598de3cc87b94f4533a9fc3bb46294c66366a'
PILOT='c37a5796a3829dfab1846928041f6a91472dc47f20e02f8a2a4080198b574b1c'
PILOT_WORKER='1abd553afff8444552ce20e8948f9141da53a0ae3fb2a2632bd86c9008e6840f'
PILOT_MANIFEST='563fc148bf219581259eea090271c37f4760115cc6d09e40c0437a14ee93b7bd'
RANGES=((597,886),(886,1175),(1175,1464),(1464,1753))


def small(path,doc):
    raw=(json.dumps(doc,ensure_ascii=False,indent=2)+'\n').encode()
    if len(raw)>60000:
        raise ValueError('a new plaintext summary exceeds the explicit60000-byte limit; preserve the full native')
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_bytes(raw)


def actual(process,run):
    return (process.get('repository')=='Rogerhu12/math-research-public'
        and str(process.get('run_id'))==str(run) and process.get('complete')
        and not process.get('failure') and process.get('children')
        and all(c.get('actual_returncode')==0 for c in process['children']))


class MixedZWorker(ReviewedBodyWorker):
    def __init__(self,a):
        super().__init__(a)
        suffix=a.phase if a.phase!='range' else f'range-{a.first:04d}-{a.end:04d}'
        self.name=f'run-{self.run_label}-complete-Z-sources-{suffix}'
        self.dest=TOPIC/'notes/complete_Z_source_v2_ci'/self.name
        self.native_name=('complete-Z-source-plan.json.gz' if a.phase=='plan' else
            f'new-exact-bump-Z-source-{a.first:04d}-{a.end:04d}.json.gz' if a.phase=='range'
            else 'complete7721-mixed-Z-sources.json.gz')
        self.state.update(kind='actual_public_complete_mixed_Z_source_process_v2',
            worker_source_sha256=digest(__file__),phase=a.phase,
            source_range=[a.first,a.end] if a.phase=='range' else None,
            new_target_provider_calls=0,old_original_target_mean_or_trial_reconstructions_executed=0,
            original_exact_bump_pilot_run=43610523058,
            original_exact_bump_pilot_native_sha256=PILOT,
            full_mean_and_known_high_sources_retained=True,
            complete_infinite_inverse_proved=False,actual_full_PDE_response_error_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='complete_mixed_Z_source_public_inputs_v2':
            raise ValueError('the separate full mixed-Z manifest is required')
        if self.args.phase=='range' and (self.args.first,self.args.end) not in RANGES:
            raise ValueError('an unassigned or overlapping new compact source range was requested')

    def execute(self,label,command):
        try:return super().execute(label,command)
        finally:
            path=self.cache/self.native_name
            if path.exists():
                native=read(path);rows=native.get('rows',[])
                outcome=dict(native_sha256=digest(path),complete=native.get('complete'),
                    failure=native.get('failure'),gates=native.get('gates',[]),
                    actual_completed_rows=len(rows),
                    completed_original_indices=[x['common_row'] for x in rows] if len(rows)<=100 else None,
                    first_completed_original_index=rows[0]['common_row'] if rows else None,
                    last_completed_original_index=rows[-1]['common_row'] if rows else None)
                small(self.evidence/'actual-latest-child-outcome.json',outcome)
                print(json.dumps(outcome),flush=True)
                if native.get('failure') and self.log.exists():
                    print(self.log.read_text()[-16000:],flush=True)

    def exact_native(self,root,name,process,expected=None):
        path=root/'native'/name
        if not path.exists():
            matches=[x for x in process.get('native_files',[]) if x.get('logical_file')=='native/'+name]
            if len(matches)!=1 or 'lossless_manifest' not in matches[0]:
                raise ValueError('the full actual source native is absent')
            target=self.work/('restored-'+matches[0]['sha256']+'.json.gz')
            if not target.exists():restore(root/matches[0]['lossless_manifest'],target)
            path=target
        expected=expected or process.get('complete_native_sha256')
        if digest(path)!=expected:raise ValueError('the actual complete native bytes changed')
        return path

    def original_inputs(self):
        original_path=self.science/self.manifest['original_body_manifest']
        if digest(original_path)!=OLD_MANIFEST:raise ValueError('the original body manifest changed')
        original=read(original_path)
        audit_dir=self.evidence/'original-input-audit';audit_dir.mkdir(exist_ok=True)
        audit=SimpleNamespace(
            args=SimpleNamespace(prepared=self.args.prepared,manifest_sha=OLD_MANIFEST,
                original_run=43583838026,original_attempt=1,previous_artifacts=self.args.previous_artifacts),
            manifest=original,science=self.science,science_topic=self.science_topic,evidence=audit_dir,state={})
        CompleteMeanWorker.restore_original_bundle(audit)
        parts=CompleteMeanWorker.original_complete_parts(audit)
        resolved={}
        specs={
            'body':(self.args.body_artifact,'complete-correlated-body-and-mean-errors.json.gz',BODY,BODY_PROCESS,43586413510,'body-process'),
            'repair-source':(self.args.repair_artifact,'complete-known-response-centre-repair-source.json.gz',REPAIR,REPAIR_PROCESS,43597921732,'repair-process'),
            'pilot':(self.args.pilot_artifact,'exact-bump-and-continuous-Z-source-pilot.json.gz',PILOT,None,43610523058,'pilot-process')}
        for label,(root,name,expected,process_sha,run,process_label) in specs.items():
            root=root.resolve();pp=root/'process.json';process=read(pp)
            if not actual(process,run):raise ValueError('the original successful '+label+' process is required')
            if process_sha and digest(pp)!=process_sha:raise ValueError('the exact original process bytes changed')
            if label=='pilot' and (process.get('worker_source_sha256')!=PILOT_WORKER
                or process.get('input_manifest_sha256')!=PILOT_MANIFEST):
                raise ValueError('the exact original completed bump pilot process differs')
            native=self.exact_native(root,name,process,expected)
            if process.get('complete_native_sha256')!=expected:
                raise ValueError('the original actual native and its completed process disagree')
            resolved[label]=native;resolved[process_label]=pp
            shutil.copyfile(pp,self.evidence/('original-'+process_label+'.json'))
        resolved['original-manifest']=original_path
        resolved['candidate']=self.science/original['published_candidate']
        resolved['response']=Path(original['row_identity']['full_trials']['response']['path'])
        resolved['object']=self.science/(REL+'data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json')
        resolved['direction']=self.science/self.manifest['complete_continuous_direction_native']
        return resolved,parts

    def completed_plan(self,inputs):
        if self.args.original_plan_artifact is not None:
            root=self.args.original_plan_artifact.resolve();pp=root/'process.json';p=read(pp)
            old_sha='26a488b4347e0e30106e67dcd18b54e211dba6adecd7d2c029a4dc6ba097d95a'
            failure=p.get('failure',{})
            if (p.get('repository')!='Rogerhu12/math-research-public'
                or str(p.get('run_id'))!='43612904296'
                or p.get('worker_source_sha256')!='84e0666e30f5d77fff393e7db40529f1c579ffa6bac13fbadd367252883cbb15'
                or p.get('input_manifest_sha256')!='854261f57cc390f17659ec5ff9cdc83d98d8ef8b32b6b7b241c54fb3359075be'
                or p.get('phase')!='plan' or p.get('complete') is not False
                or failure.get('type')!='TypeError'
                or failure.get('message')!="unsupported operand type(s) for +: 'PosixPath' and 'str'"
                or not p.get('children')
                or not all(c.get('actual_returncode')==0 for c in p['children'])
                or p.get('actual_common_input_sha256')!=inputs):
                raise ValueError('the precise original successful-child/failed-summary plan receipt is required')
            matches=[x for x in p.get('native_files',[]) if x.get('logical_file')=='native/complete-Z-source-plan.json.gz']
            if len(matches)!=1 or matches[0].get('sha256')!=old_sha:
                raise ValueError('the complete actual seven-gate original plan native is absent')
            native=self.exact_native(root,'complete-Z-source-plan.json.gz',p,old_sha);old=read(native)
            if (not old.get('complete') or old.get('failure')
                or old.get('source_sha256')!=self.manifest['files'][PRODUCER]
                or old.get('common_input_sha256')!=inputs
                or not old.get('complete_valid_source_cover') or len(old.get('rows',[]))!=7721
                or len(old.get('gates',[]))!=7 or not all(x['passed'] for x in old['gates'])):
                raise ValueError('the original mathematical plan did not actually complete')
            receipt=dict(original_run=43612904296,original_actual_process_sha256=digest(pp),
                original_native_sha256=old_sha,original_wrapper_failure=failure,
                original_children=[dict(label=c.get('label'),actual_returncode=c.get('actual_returncode'),
                    wall_seconds=c.get('wall_seconds')) for c in p['children']],
                original_successful_native_gates=old['gates'],
                original_complete_rows=7721,original_native_bytes_reused=True,
                original_scientific_source_unchanged=True,new_original_plan_rows_computed=0)
            small(self.evidence/'original-successful-plan-and-failed-summary-receipt.json',receipt)
            self.state['original_successful_plan_publication_failure_receipt']=receipt
            return pp,native
        root=TOPIC/'notes/complete_Z_source_v2_ci'
        if not root.exists():return None
        for pp in sorted(root.glob('*/process.json')):
            process=read(pp)
            if (not actual(process,process.get('run_id'))
                or process.get('worker_source_sha256')!=digest(__file__)
                or process.get('input_manifest_sha256')!=self.args.manifest_sha
                or process.get('phase')!='plan'
                or process.get('actual_common_input_sha256')!=inputs):
                continue
            native=self.exact_native(pp.parent,'complete-Z-source-plan.json.gz',process)
            old=read(native)
            if (old.get('source_sha256')==self.manifest['files'][PRODUCER]
                and old.get('common_input_sha256')==inputs and old.get('complete')
                and not old.get('failure') and old.get('complete_valid_source_cover')
                and len(old.get('rows',[]))==7721
                and old.get('gates') and all(x['passed'] for x in old['gates'])):
                return pp,native
        return None

    def best_prefix(self,inputs,plan_sha):
        root=TOPIC/'notes/complete_Z_source_v2_ci';candidates=[]
        if not root.exists():return None
        for pp in sorted(root.glob('*/process.json')):
            process=read(pp)
            if (process.get('repository')!='Rogerhu12/math-research-public'
                or process.get('worker_source_sha256')!=digest(__file__)
                or process.get('input_manifest_sha256')!=self.args.manifest_sha
                or process.get('phase')!='range'
                or process.get('source_range')!=[self.args.first,self.args.end]
                or process.get('actual_common_input_sha256')!=inputs
                or process.get('actual_plan_native_sha256')!=plan_sha):
                continue
            matches=[x for x in process.get('native_files',[]) if x.get('logical_file')=='native/'+self.native_name]
            if len(matches)!=1:continue
            native=self.exact_native(pp.parent,self.native_name,process,matches[0]['sha256'])
            old=read(native);rows=old.get('rows',[])
            if (old.get('source_sha256')!=self.manifest['files'][PRODUCER]
                or old.get('common_input_sha256')!=inputs or old.get('plan_native_sha256')!=plan_sha
                or not rows or not all(x.get('actual_new_source_cell_complete') for x in rows)):
                continue
            candidates.append((len(rows),pp,native,old))
        return max(candidates,key=lambda x:x[0]) if candidates else None

    def finish_inputs(self):
        root=self.args.plan_artifact.resolve();pp=root/'process.json';process=read(pp)
        if (not actual(process,self.args.workflow_run) or process.get('phase')!='plan'
            or process.get('worker_source_sha256')!=digest(__file__)
            or process.get('input_manifest_sha256')!=self.args.manifest_sha):
            raise ValueError('the actual completed same-run full source plan is required')
        plan=self.exact_native(root,'complete-Z-source-plan.json.gz',process)
        shutil.copyfile(pp,self.evidence/'actual-completed-plan-process.json')
        natives=[];processes=[];found={}
        for directory in sorted(self.args.range_artifacts.iterdir()):
            if not directory.is_dir() or not (directory/'process.json').exists():continue
            rp=directory/'process.json';r=read(rp);pair=tuple(r.get('source_range',[]))
            if pair not in RANGES:raise ValueError('an unassigned range artifact was supplied')
            if (pair in found or not actual(r,self.args.workflow_run) or r.get('phase')!='range'
                or r.get('worker_source_sha256')!=digest(__file__)
                or r.get('input_manifest_sha256')!=self.args.manifest_sha
                or r.get('actual_plan_native_sha256')!=digest(plan)):
                raise ValueError('an original actual source range failed or changed identity')
            found[pair]=(self.exact_native(directory,f'new-exact-bump-Z-source-{pair[0]:04d}-{pair[1]:04d}.json.gz',r),rp)
        if set(found)!=set(RANGES):raise ValueError('all four actual completed range artifacts are required')
        for pair in RANGES:
            native,rp=found[pair];natives.append(native);processes.append(rp)
            shutil.copyfile(rp,self.evidence/f'actual-range-{pair[0]:04d}-{pair[1]:04d}-process.json')
        return plan,natives,processes

    def prepare(self):
        native=self.cache/self.native_name
        command=[sys.executable,'-u',str(self.science/PRODUCER),'--phase',self.args.phase,'--out',str(native)]
        if self.args.phase=='finish':
            plan,natives,processes=self.finish_inputs()
            command+=['--plan',str(plan),'--workflow-run',str(self.args.workflow_run),
                '--range-natives',*[str(x) for x in natives],'--range-processes',*[str(x) for x in processes]]
            self.state.update(actual_plan_native_sha256=digest(plan),
                actual_range_native_sha256=[digest(x) for x in natives])
        else:
            inputs,parts=self.original_inputs()
            expected={k:digest(v) for k,v in inputs.items()}
            self.state['actual_common_input_sha256']=expected
            for k,v in inputs.items():command+=['--'+k,str(v)]
            command+=['--parts',*[str(x) for x in parts]]
            if self.args.phase=='plan':
                previous=self.completed_plan(expected)
                if previous:
                    pp,old=previous;command+=['--resume',str(old)]
                    shutil.copyfile(pp,self.evidence/'original-completed-plan-process.json')
                    self.state.update(original_completed_plan_native_sha256=digest(old),
                        original_completed_plan_consumed_without_recomputing_any_baseline_row=True)
            if self.args.phase=='range':
                root=self.args.plan_artifact.resolve();pp=root/'process.json';process=read(pp)
                if (not actual(process,self.args.workflow_run) or process.get('phase')!='plan'
                    or process.get('worker_source_sha256')!=digest(__file__)
                    or process.get('input_manifest_sha256')!=self.args.manifest_sha):
                    raise ValueError('the exact actual successful source plan is required')
                plan=self.exact_native(root,'complete-Z-source-plan.json.gz',process)
                oldplan=read(plan)
                if oldplan.get('common_input_sha256')!=expected:
                    raise ValueError('the new range and completed source plan use different original input bytes')
                self.state['actual_plan_native_sha256']=digest(plan)
                shutil.copyfile(pp,self.evidence/'actual-completed-plan-process.json')
                command+=['--plan',str(plan),'--first',str(self.args.first),'--end',str(self.args.end)]
                prefix=self.best_prefix(expected,digest(plan))
                if prefix:
                    count,pp,old,prior=prefix
                    command+=['--resume',str(old)]
                    shutil.copyfile(pp,self.evidence/'original-new-source-prefix-process.json')
                    self.state.update(original_completed_source_cells_reused=count,
                        original_source_prefix_sha256=digest(old),original_source_prefix_failure=prior.get('failure'))
        self.publish()
        self.execute('actual_complete_Z_source_'+self.args.phase,command)
        result=read(native)
        if (not result.get('complete') or result.get('failure')
            or result.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or not result.get('gates') or not all(x['passed'] for x in result['gates'])
            or result.get('new_target_provider_calls')!=0
            or result.get('actual_full_PDE_response_error_proved')
            or result.get('complete_infinite_inverse_proved')):
            raise ValueError('the actual complete mixed source outcome failed or exceeded its scope')
        summary={k:v for k,v in result.items() if k not in ('rows','original_parts')}
        rows=result.get('rows',[])
        summary.update(native_sha256=digest(native),complete_rows=len(rows),
            full_rows_retained_in_original_native=True,
            first_original_index=rows[0]['common_row'] if rows else None,
            last_original_index=rows[-1]['common_row'] if rows else None)
        # Existing upper bounds choose display rows only. This is not a new
        # floating mathematical maximum or a substitute for the full native.
        summaries=[]
        for row in rows[:8]:
            summaries.append(dict(common_row=row['common_row'],interval=row['interval'],
                complete_Z_source={k:{n:v['upper'] for n,v in b.items()} for k,b in row['complete_Z_source'].items()}))
        summary['first_eight_row_examples_only']=summaries
        small(self.evidence/('complete-Z-source-'+self.args.phase+'-summary.json'),summary)
        self.state.update(complete=True,complete_native_sha256=digest(native),
            actual_scientific_gates=len(result['gates']),actual_completed_source_rows=len(rows),
            complete_valid_source_cover=bool(result.get('complete_valid_source_cover')),
            new_compact_rows_computed=result.get('new_compact_rows_computed'),
            actual_new_source_rows_executed_in_this_child=result.get('new_source_rows_executed_in_this_child'),
            all_summary_files_strictly_below60000_bytes=True)
        if 'complete_source_bounds' in result:
            self.state['complete_source_bounds']=result['complete_source_bounds']


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','work','artifact-dir'):
        p.add_argument('--'+name,type=Path,required=True)
    for name in ('prepared','previous-artifacts','body-artifact','repair-artifact','pilot-artifact','plan-artifact','range-artifacts','original-plan-artifact'):
        p.add_argument('--'+name,type=Path)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--phase',choices=('plan','range','finish'),required=True)
    p.add_argument('--first',type=int,default=0);p.add_argument('--end',type=int,default=0)
    p.add_argument('--workflow-run',type=int,required=True)
    p.add_argument('--compute-minutes',type=int,default=80);p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='complete-mixed-Z-source-v2';a.mode='prepare';a.recovery_manifest=None;a.recovery_sha=None
    worker=MixedZWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
