#!/usr/bin/env python3
"""Actual public32-range completion of same-proposal complete97 adjoint Grams."""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,shutil,signal,sys
from pathlib import Path
from fourfold_codazzi_cap_adjoint_residual_Gram_CI import (
    AdjointGramWorker,REL,PUBLIC,PROPOSAL_NATIVE,BACKGROUND,LOCAL)
from fourfold_codazzi_complete_directional_matrix_Green_CI import MatrixGreenWorker
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_cap128_CI_worker import read,digest
from fourfold_codazzi_phase_high7_CI_worker import TOPIC,REPO

PRODUCER=REL+'scripts/fourfold_codazzi_complete_cap_adjoint_Grams.py'
FOLDER='notes/complete_cap_adjoint_Grams_ci'
KIND='actual_complete7908_same_proposal_physical_adjoint_residual_Grams_v1'
OLD_MANIFEST=REL+'notes/2026-11-15-R133-complete97-ordinary-adjoint-Gram-pilot-CI-inputs.json'
OLD_SHA='467cd31f6d62b834d3a0cf07a1ef92efe1a2ef218e27d862140122c37a9ce71f'
PILOT_RUN=43664278200
PILOT_NAME='visible-exact-cap-adjoint-Gram-pilot-43664278200-1'
PILOT_NATIVE='eb58b97ae182cedf621c4ff122b421ffb844e3839266a6a7d6df86b9134d8cfb'
PILOT_LOGICAL='native/complete97-ordinary-cap-adjoint-residual-Gram-pilot.json.gz'
PILOT_SOURCE='ae3b90c15e65343a0d5bdeb80cba4d6eb2a6f519155bff9a175b0f48a2f72310'
PILOT_WORKER='3f7c1f5862530cf13bda0a30466fc16998ef2a1f0f60ab97a8e5bc9506d81222'
CANDIDATE=REL+'data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json'
REPAIR=REL+'notes/2026-11-14-R133-final-exact-continuous-value-repair-native.json.gz'
LABELS=dict(plan='prepare_exact_original32_slices_without_target_or_trial_recomputation',
    range='new_missing_complete97_adjoint_quarter_Grams',
    finish='complete7908_same_object_signed97_ordinary_adjoint_Gram_union')
GROUPS=[(248*g,min(7908,248*(g+1))) for g in range(32)]
PILOTS={0,64,4096,7907}


def small(path,value):
    raw=(json.dumps(value,ensure_ascii=False,indent=2)+'\n').encode()
    if len(raw)>60000:raise ValueError('one complete-adjoint evidence text exceeds60000 UTF8 bytes')
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(raw)


def relative(value):
    path=Path(value)
    if path.is_absolute() or '..' in path.parts:raise ValueError('an exact scientific receipt path is unsafe')
    return path


def native_name(phase,group=None):
    suffix=f'range-{group:02d}' if phase=='range' else phase
    return 'complete7908-cap-adjoint-Grams-'+suffix+'.json.gz'


def artifact_name(phase,run,attempt,group=None):
    suffix=f'range-{group:02d}' if phase=='range' else phase
    return f'visible-exact-complete-adjoint-Grams-{suffix}-{run}-{attempt}'


def bundle_name(group,run,attempt):
    return f'visible-exact-complete-adjoint-original-slice-{group:02d}-{run}-{attempt}'


class CompleteAdjointGramWorker(AdjointGramWorker):
    def __init__(self,a):
        MatrixGreenWorker.__init__(self,a)
        suffix=f'range-{a.group:02d}' if a.phase=='range' else a.phase
        self.name=f'run-{self.run_label}-complete-adjoint-Grams-{suffix}'
        self.dest=TOPIC/FOLDER/self.name;self.native_name=native_name(a.phase,a.group)
        self.bundle_root=self.artifact/'bundles';self.bundle_root.mkdir(parents=True,exist_ok=True)
        self.state.update(kind='actual_public_complete7908_cap_adjoint_Gram_process_v1',
            worker_source_sha256=digest(__file__),phase=a.phase,group=a.group,
            original_pilot_run=PILOT_RUN,original_pilot_native_sha256=PILOT_NATIVE,
            original_targets_or_adjoint_trial_recomputed=0,
            exact_original_four_pilot_quarters_recomputed=0,
            original_arrays_and_new_Grams_stay_in_public_Actions=True,
            successful_scientific_rows_preserved_after_publication_failure=True,
            complete7908_adjoint_cover_proved=False,
            complete_full_cap_high_to_low_bound_proved=False,
            complete_infinite_BVP_inverse_proved=False)

    def check_inputs(self):
        ReviewedBodyWorker.check_inputs(self)
        if self.manifest.get('kind')!='complete7908_same_proposal_adjoint_Grams_public_inputs_v1':
            raise ValueError('the separate exact32-range adjoint Gram manifest is required')
        old=read(REPO/OLD_MANIFEST)
        if (digest(REPO/OLD_MANIFEST)!=OLD_SHA or len(old.get('files',{}))!=337
            or any(self.manifest['files'].get(k)!=v for k,v in old['files'].items())):
            raise ValueError('one original337 pilot input pin changed')
        if self.args.phase=='range' and self.args.group not in range(32):
            raise ValueError('only the32 explicitly assigned complete ranges may run')

    def checked_native(self,root,phase,group=None):
        pp=root/'process.json';p=read(pp)
        logical='native/'+native_name(phase,group)
        entries=[x for x in p.get('native_files',[]) if x.get('logical_file')==logical]
        if (p.get('repository')!=PUBLIC or p.get('worker_source_sha256')!=digest(__file__)
            or p.get('input_manifest_sha256')!=self.args.manifest_sha
            or p.get('phase')!=phase or phase=='range' and p.get('group')!=group
            or len(entries)!=1):
            raise ValueError('an actual complete-adjoint native has another original process identity')
        native=self.exact_native(root,logical,p,entries[0]['sha256']);d=read(native)
        if d.get('kind')!=KIND or d.get('phase')!=phase or d.get('source_sha256')!=self.manifest['files'][PRODUCER]:
            raise ValueError('an actual complete-adjoint native has another scientific source')
        return native,pp,d,p

    def mathematical_success(self,p,d,phase,group=None):
        child=any(c.get('label')==LABELS[phase] and c.get('actual_returncode')==0
            for c in p.get('children',[]))
        reused=bool(p.get('original_complete_success_reused_without_child')
            and p.get('original_success_process_sha256'))
        if (not(child or reused) or not d.get('complete') or d.get('failure')
            or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or d.get('kind')!=KIND or d.get('phase')!=phase
            or not d.get('gates') or not all(x.get('passed') for x in d['gates'])):return False
        if phase=='plan':
            return bool(d.get('completed_bundles')==32 and len(d.get('bundles',[]))==32
                and d.get('original_complete_pilot_native_sha256')==PILOT_NATIVE)
        if phase=='range':
            want=[i for i in range(*GROUPS[group]) if i not in PILOTS]
            return bool(d.get('group')==group
                and [r.get('original_quarter_index') for r in d.get('rows',[])]==want)
        return bool(d.get('complete_quarter_count')==7908
            and d.get('original_successful_pilot_quarters_reused')==4
            and d.get('new_quarters_from_actual_ranges')==7904
            and d.get('complete7908_adjoint_cover_proved')
            and not d.get('complete_full_cap_high_to_low_bound_proved'))

    def pilot_inputs(self):
        root=self.download(PILOT_RUN,PILOT_NAME);pp=root/'process.json';p=read(pp)
        native=self.exact_native(root,PILOT_LOGICAL,p,PILOT_NATIVE);d=read(native)
        if (p.get('worker_source_sha256')!=PILOT_WORKER or p.get('input_manifest_sha256')!=OLD_SHA
            or d.get('source_sha256')!=PILOT_SOURCE or not d.get('complete') or d.get('failure')
            or len(d.get('rows',[]))!=4 or len(d.get('gates',[]))!=9
            or not all(x.get('passed') for x in d['gates'])
            or not any(c.get('label')=='four_actual_closed_quarters_complete97_ordinary_adjoint_and_Hessian_Grams'
                and c.get('actual_returncode')==0 for c in p.get('children',[]))):
            raise ValueError('the exact actually successful four-quarter pilot is required')
        for row in d['rows']:
            e=row['new_array_receipt'];path=root/'matrices'/relative(e['file'])
            if path.stat().st_size!=e['bytes'] or digest(path)!=e['sha256']:
                raise ValueError('one actual complete signed97 pilot array changed')
        self.record_process(pp,'original-successful-four-quarter-pilot-process.json')
        return native,pp,root/'matrices'

    def stage_plan(self):
        run=self.args.source_run;attempt=self.args.source_attempt
        if run is None or attempt is None:raise ValueError('the actual successful plan run and attempt are required')
        root=self.download(run,artifact_name('plan',run,attempt))
        native,pp,d,p=self.checked_native(root,'plan')
        if (str(p.get('run_attempt'))!=str(attempt) or not self.mathematical_success(p,d,'plan')):
            raise ValueError('the actual completed exact32 slice plan is required')
        self.state['plan_native_sha256']=digest(native)
        self.record_process(pp,'actual-complete32-slice-plan-process.json')
        return native,pp,d,p

    def stage_bundle(self,run,attempt,group,plan):
        root=self.download(run,bundle_name(group,run,attempt))
        pp=root/'process.json';p=read(pp);item=plan['bundles'][group]
        if (p.get('phase')!='plan' or str(p.get('run_attempt'))!=str(attempt)
            or p.get('worker_source_sha256')!=digest(__file__)
            or p.get('input_manifest_sha256')!=self.args.manifest_sha):
            raise ValueError('one prepared original binary64 slice belongs to another plan process')
        path=root/'bundle-index.json'
        if digest(path)!=item['bundle_index']['sha256']:
            raise ValueError('one exact original prepared slice index changed')
        d=read(path)
        if (d.get('group')!=group or d.get('object_identity_sha256')!=plan['object_identity_sha256']
            or not d.get('all_node_values_and_derivatives_are_literal_original_binary64_slices')):
            raise ValueError('one literal original Hermite slice changed mathematical objects')
        for entry in d['exact_source_files']:
            path=root/relative(entry['file'])
            if path.stat().st_size!=entry['bytes'] or digest(path)!=entry['sha256']:
                raise ValueError('one exact prepared original proposal byte slice changed')
        return root

    def scope(self,plan=None):
        value=dict(phase=self.args.phase,group=self.args.group,
            source_sha256=self.manifest['files'][PRODUCER],manifest_sha256=self.args.manifest_sha,
            original_pilot_native_sha256=PILOT_NATIVE,original_proposal_native_sha256=PROPOSAL_NATIVE)
        if plan is not None:value['plan_native_sha256']=digest(plan)
        return value

    def previous(self,scope):
        root=TOPIC/FOLDER;choices=[]
        if not root.exists():return None
        for pp in sorted(root.glob('*/process.json')):
            p=read(pp)
            if (p.get('repository')!=PUBLIC or p.get('worker_source_sha256')!=digest(__file__)
                or p.get('input_manifest_sha256')!=self.args.manifest_sha
                or p.get('exact_recovery_scope')!=scope
                or str(p.get('run_id'))==str(self.state['run_id'])
                    and str(p.get('run_attempt'))==str(self.state['run_attempt'])):continue
            try:native,_,d,_=self.checked_native(pp.parent,self.args.phase,self.args.group)
            except (ValueError,FileNotFoundError):continue
            count=d.get('completed_bundles',0) if self.args.phase=='plan' else d.get('completed_quarters',0)
            complete=self.mathematical_success(p,d,self.args.phase,self.args.group)
            choices.append(((int(complete),count),pp,native))
        return max(choices,key=lambda x:x[0]) if choices else None

    def copy_array(self,source,target,receipt):
        if source.stat().st_size!=receipt['bytes'] or digest(source)!=receipt['sha256']:
            raise ValueError('one actually successful original Gram/model array changed')
        target.parent.mkdir(parents=True,exist_ok=True)
        if target.exists() and digest(target)!=receipt['sha256']:
            raise ValueError('an old successful scientific array would be overwritten')
        if not target.exists():shutil.copyfile(source,target)

    def restore_previous(self,previous,scope):
        _,reviewed,n0=previous;p0=read(reviewed);run=p0['run_id'];attempt=p0['run_attempt']
        phase=self.args.phase;group=self.args.group
        root=self.download(run,artifact_name(phase,run,attempt,group))
        native,pp,d,p=self.checked_native(root,phase,group)
        if (p.get('exact_recovery_scope')!=scope
            or d.get('source_sha256')!=read(n0).get('source_sha256')):
            raise ValueError('the exact previous successful scientific prefix changed')
        if phase=='plan':
            for item in d.get('bundles',[]):
                g=item['group'];bundle=self.stage_bundle(run,attempt,g,d)
                target=self.bundle_root/f'range-{g:02d}';target.mkdir(parents=True,exist_ok=True)
                paths=[item['bundle_index'],*item['source_files']]
                for entry in paths:
                    name=Path(entry['file']).name
                    self.copy_array(bundle/name,target/name,entry)
        elif phase=='range':
            for row in d.get('rows',[]):
                item=row['new_array_receipt'];r=relative(item['file'])
                self.copy_array(root/'matrices'/r,self.new_arrays/r,item)
        elif d.get('complete_new_array_receipt'):
            item=d['complete_new_array_receipt'];r=relative(item['file'])
            self.copy_array(root/'matrices'/r,self.new_arrays/r,item)
        self.record_process(pp,'original-complete-adjoint-artifact-process.json')
        self.record_process(reviewed,'original-complete-adjoint-reviewed-process.json')
        prefix=self.work/'original-complete-adjoint-successful-prefix.json.gz';shutil.copyfile(native,prefix)
        complete=self.mathematical_success(p,d,phase,group)
        small(self.evidence/'original-complete-adjoint-prefix-reuse.json',dict(
            original_run=str(run),original_attempt=str(attempt),phase=phase,group=group,
            actual_original_process_sha256=digest(pp),reviewed_process_sha256=digest(reviewed),
            original_native_sha256=digest(native),original_process_complete=p.get('complete'),
            mathematical_complete=complete,actual_completed_bundles=d.get('completed_bundles'),
            actual_completed_quarters=d.get('completed_quarters'),failure_preserved=d.get('failure'),
            publication_success_not_required_for_scientific_reuse=True))
        if complete:
            shutil.copyfile(native,self.cache/self.native_name);self.reused_complete=True
            self.state.update(original_success_process_sha256=digest(pp),
                actual_input_sha256=p.get('actual_input_sha256',{}))
        elif d.get('failure'):
            raise RuntimeError('preserve the actual mathematical failure and prefix without unchanged repetition: '+str(d['failure']))
        return prefix

    def set_scope_and_previous(self,plan=None):
        scope=self.scope(plan);self.state['exact_recovery_scope']=scope
        previous=self.previous(scope)
        return self.restore_previous(previous,scope) if previous else None

    def prepare_plan(self):
        prefix=self.set_scope_and_previous()
        if not self.reused_complete:
            old,inputs,arrays=AdjointGramWorker.inputs(self)
            pilot,pp,pilot_arrays=self.pilot_inputs()
            inputs.update(pilot=pilot,**{'pilot-process':pp})
            self.state['actual_input_sha256']={k:digest(v) for k,v in inputs.items()}
            index=self.work/'exact-original-complete-adjoint-inputs.json'
            small(index,dict(repository=PUBLIC,kind='cached_adjoint_trial_original_inputs_v1',
                files={k:dict(path=str(v),sha256=digest(v)) for k,v in old.items()}))
            command=[sys.executable,'-u',str(self.science/PRODUCER),'--phase','plan',
                '--input-index',str(index),'--proposal-arrays',str(arrays),
                '--pilot-arrays',str(pilot_arrays),'--bundles',str(self.bundle_root),
                '--out',str(self.cache/self.native_name)]
            for k in ('proposal','proposal-process','background','local','pilot','pilot-process'):
                command+=['--'+k,str(inputs[k])]
            if prefix:command+=['--resume',str(prefix)]
            self.publish();self.execute(LABELS['plan'],command)
        self.complete_phase()

    def prepare_range(self):
        plan,pp,d,p=self.stage_plan()
        prefix=self.set_scope_and_previous(plan)
        if not self.reused_complete:
            root=self.stage_bundle(self.args.source_run,self.args.source_attempt,self.args.group,d)
            candidate=self.science/CANDIDATE;repair=self.science/REPAIR
            self.state['actual_input_sha256']=dict(plan=digest(plan),**{
                'plan-process':digest(pp),'bundle-index':digest(root/'bundle-index.json'),
                'candidate':digest(candidate),'repair':digest(repair)})
            command=[sys.executable,'-u',str(self.science/PRODUCER),'--phase','range',
                '--group',str(self.args.group),'--plan',str(plan),'--bundle',str(root),
                '--candidate',str(candidate),'--repair',str(repair),
                '--arrays',str(self.new_arrays),'--out',str(self.cache/self.native_name)]
            if prefix:command+=['--resume',str(prefix)]
            self.publish();self.execute(LABELS['range'],command)
        self.complete_phase()

    def completed_range(self,run,group,plan_sha):
        prefix=f'visible-exact-complete-adjoint-Grams-range-{group:02d}-{run}-'
        candidates=[]
        if not hasattr(self,'available_range_artifacts'):
            entries=[]
            for page in range(1,101):
                value=self.api(f'/repos/{PUBLIC}/actions/runs/{run}/artifacts?per_page=100&page={page}')
                entries.extend(value.get('artifacts',[]))
                if len(value.get('artifacts',[]))<100:break
            self.available_range_artifacts=entries
        for item in self.available_range_artifacts:
            name=item.get('name','')
            if name.startswith(prefix) and name[len(prefix):].isdigit() and not item.get('expired'):
                candidates.append((int(name[len(prefix):]),item))
        for attempt,item in sorted(candidates,key=lambda x:x[0],reverse=True):
            self.artifact_cache[(str(run),item['name'])]=item
            root=self.download(run,item['name'])
            native,pp,d,p=self.checked_native(root,'range',group)
            if (str(p.get('run_attempt'))!=str(attempt)
                or d.get('exact_range_identity',{}).get('plan_native_sha256')!=plan_sha):
                raise ValueError('one actual range artifact has another exact plan or attempt')
            if self.mathematical_success(p,d,'range',group):
                return root,native,pp,d,p
        raise ValueError('no mathematically complete original range artifact exists for this exact plan')

    def prepare_finish(self):
        plan,pp,pd,p=self.stage_plan()
        prefix=self.set_scope_and_previous(plan)
        if not self.reused_complete:
            pilot,pilot_process,pilot_arrays=self.pilot_inputs()
            ranges=[];run=self.args.source_run;attempt=self.args.source_attempt
            for group in range(32):
                root,native,process,d,p=self.completed_range(run,group,digest(plan))
                if not self.mathematical_success(p,d,'range',group):
                    raise ValueError('one of the32 actual adjoint ranges is mathematically incomplete')
                ranges.append(dict(group=group,native=str(native),native_sha256=digest(native),
                    process=str(process),actual_process_sha256=digest(process),arrays=str(root/'matrices')))
                self.record_process(process,f'actual-range-processes/range-{group:02d}.json')
            index=self.work/'actual32-complete-adjoint-range-index.json'
            data=dict(repository=PUBLIC,plan_native_sha256=digest(plan),worker_source_sha256=digest(__file__),
                manifest_sha256=self.args.manifest_sha,original_pilot_actual_process_sha256=digest(pilot_process),
                original_pilot_native_sha256=digest(pilot),ranges=ranges)
            small(index,data)
            self.state['actual_input_sha256']=dict(plan=digest(plan),**{'plan-process':digest(pp),
                'original-pilot':digest(pilot),'original-pilot-process':digest(pilot_process),
                'actual32-range-index':digest(index)})
            command=[sys.executable,'-u',str(self.science/PRODUCER),'--phase','finish',
                '--plan',str(plan),'--range-index',str(index),'--pilot-arrays',str(pilot_arrays),
                '--arrays',str(self.new_arrays),'--out',str(self.cache/self.native_name)]
            self.publish();self.execute(LABELS['finish'],command)
        self.complete_phase()

    def outcome(self,d):
        value={k:d.get(k) for k in ('kind','phase','complete','failure','gates','seconds','group','range',
            'completed_bundles','completed_quarters','reused_completed_quarters',
            'new_completed_quarters_this_child','complete_quarter_count','object_identity_sha256',
            'plan_native_sha256','new_intrinsic_target_calls','original_successful_pilot_quarters_reused',
            'new_quarters_from_actual_ranges','complete_Gram_trace_uppers','complete_Gram_HS_uppers',
            'mathematical_certificate_for_listed_range_only',
            'mathematical_certificate_for_complete_ordinary_adjoint_body_Grams',
            'complete7908_adjoint_cover_proved','complete_full_cap_high_to_low_bound_proved',
            'complete_infinite_BVP_inverse_proved')}
        rows=d.get('rows',[])
        value['latest_actual_quarters']=[dict(index=r['original_quarter_index'],request=r['request'],
            interval=r['interval'],true_adjoint_Gram_trace_upper=r['complete_Gram_trace_uppers']['complete_true_adjoint_ordinary'],
            exact_array=r['new_array_receipt']) for r in rows[-2:]]
        if d.get('complete_new_array_receipt'):value['complete_new_array_receipt']=d['complete_new_array_receipt']
        return value

    def snapshot(self):
        native=self.cache/self.native_name
        if native.exists():
            raw=native.read_bytes();d=json.loads(gzip.decompress(raw))
            brief=self.outcome(d);brief['native_sha256']=hashlib.sha256(raw).hexdigest()
            brief['latest_actual_readme_check']=self.state.get('readme_checks',[])[-1:]
            small(self.evidence/'actual-latest-complete-adjoint-Grams-outcome.json',brief)
            self.state.update(actual_completed_bundles=d.get('completed_bundles',0),
                actual_completed_quarters=d.get('completed_quarters',0),
                latest_scientific_native_sha256=brief['native_sha256'])
        ReviewedBodyWorker.snapshot(self)

    def execute(self,label,command):
        try:return ReviewedBodyWorker.execute(self,label,command)
        finally:
            native=self.cache/self.native_name
            if native.exists():
                d=read(native);brief=self.outcome(d);brief['native_sha256']=digest(native)
                small(self.evidence/'actual-latest-complete-adjoint-Grams-outcome.json',brief)
                print(json.dumps(brief),flush=True)
                if d.get('failure') and self.log.exists():print(self.log.read_text()[-16000:],flush=True)

    def complete_phase(self):
        native=self.cache/self.native_name;d=read(native)
        # The live process has its actual completed child at this point; a
        # publication failure after this check never makes those rows disappear.
        if self.reused_complete:
            self.state['original_complete_success_reused_without_child']=True
        if not self.mathematical_success(self.state,d,self.args.phase,self.args.group):
            raise ValueError('the actual complete-adjoint scientific phase did not complete its exact gates')
        brief=self.outcome(d);brief.update(native_sha256=digest(native),
            actual_input_sha256=self.state.get('actual_input_sha256',{}),
            original_complete_success_reused_without_child=self.reused_complete)
        small(self.evidence/('complete-adjoint-Grams-'+self.args.phase+'-summary.json'),brief)
        self.state.update(complete=True,complete_native_sha256=digest(native),
            actual_scientific_gates=len(d['gates']),
            original_complete_success_reused_without_child=self.reused_complete,
            complete7908_adjoint_cover_proved=bool(d.get('complete7908_adjoint_cover_proved')),
            complete_full_cap_high_to_low_bound_proved=False,
            complete_infinite_BVP_inverse_proved=False)

    def prepare(self):
        if self.args.phase=='plan':self.prepare_plan()
        elif self.args.phase=='range':self.prepare_range()
        else:self.prepare_finish()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','work','artifact-dir'):p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--phase',choices=('plan','range','finish'),required=True)
    p.add_argument('--group',type=int)
    p.add_argument('--source-run',type=int);p.add_argument('--source-attempt',type=int)
    p.add_argument('--compute-minutes',type=int,default=170)
    p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='complete-adjoint-Grams-'+a.phase+(f'-{a.group:02d}' if a.phase=='range' else '')
    a.mode='prepare';a.first,a.end=GROUPS[a.group] if a.phase=='range' else (0,7908)
    a.matrix_run=None;a.matrix_attempt=None;a.recovery_manifest=None;a.recovery_sha=None
    worker=CompleteAdjointGramWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):
        signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
