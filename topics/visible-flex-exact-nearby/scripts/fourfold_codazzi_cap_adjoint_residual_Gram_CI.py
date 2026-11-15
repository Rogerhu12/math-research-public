#!/usr/bin/env python3
"""Public Actions wrapper for four complete97 ordinary adjoint residual Grams."""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,shutil,signal,stat,sys,zipfile
from pathlib import Path
from fourfold_codazzi_cached_cap_adjoint_proposal_CI_v2 import AdjointProposalWorker
from fourfold_codazzi_complete_directional_matrix_Green_CI import MatrixGreenWorker
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_cap128_CI_worker import read,digest
from fourfold_codazzi_phase_high7_CI_worker import TOPIC,REPO

REL='topics/visible-flex-exact-nearby/'
PUBLIC='Rogerhu12/math-research-public'
PRODUCER=REL+'scripts/fourfold_codazzi_cap_adjoint_residual_Gram_pilot.py'
CORE=REL+'scripts/fourfold_codazzi_cap_adjoint_residual_Gram_core.py'
NATIVE='complete97-ordinary-cap-adjoint-residual-Gram-pilot.json.gz'
KIND='actual_complete97_ordinary_physical_adjoint_residual_Gram_four_quarter_pilot_v1'
FOLDER='notes/cap_adjoint_residual_Gram_pilot_ci'
LABEL='four_actual_closed_quarters_complete97_ordinary_adjoint_and_Hessian_Grams'
PROPOSAL_RUN=43662865692
PROPOSAL_NAME='visible-exact-cached-cap-adjoint-proposal-v2-43662865692-1'
PROPOSAL_NATIVE='acb2151b60f24ad88b30e6f7d1d966851abc53c15e45df19df2bfca27c2393c7'
PROPOSAL_LOGICAL='native/complete97-cached-physical-adjoint-proposal-v2.json.gz'
PROPOSAL_SOURCE='0bc067d92254b78e00b022beb455a30595b9713fba686639be78480c69685721'
PROPOSAL_WORKER='de387aaf02696fb1794cb0843028d898b0f3cde21bb3816e4e67199c0ca32368'
PROPOSAL_MANIFEST='af838e4127505e8744e140833f30037f8c4103dad08f2a11dc229932666045f3'
BACKGROUND=REL+'notes/2026-11-14-R133-continuous-repair-physical-cap-background-v2-native.json.gz'
LOCAL=REL+'notes/2026-11-14-R133-complete-local-cap-Hessian-source-native.json.gz'


def small(path,value):
    raw=(json.dumps(value,ensure_ascii=False,indent=2)+'\n').encode()
    if len(raw)>60000:raise ValueError('one actual adjoint Gram evidence file exceeds60000 UTF8 bytes')
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(raw)


def artifact_name(run,attempt):return f'visible-exact-cap-adjoint-Gram-pilot-{run}-{attempt}'


class AdjointGramWorker(AdjointProposalWorker):
    def __init__(self,a):
        MatrixGreenWorker.__init__(self,a)
        self.name=f'run-{self.run_label}-cap-adjoint-residual-Gram-pilot'
        self.dest=TOPIC/FOLDER/self.name;self.native_name=NATIVE
        self.state.update(kind='actual_public_complete97_ordinary_adjoint_residual_Gram_pilot_process_v1',
            worker_source_sha256=digest(__file__),phase='four-quarter-adjoint-Grams',
            original_adjoint_proposal_run=PROPOSAL_RUN,original_target_evaluations=0,
            original_complete_adjoint_trial_recomputed=False,
            complete7908_adjoint_cover_proved=False,complete_full_cap_high_to_low_bound_proved=False,
            complete_infinite_BVP_inverse_proved=False,
            successful_scientific_quarters_preserved_on_publication_failure=True)

    def check_inputs(self):
        ReviewedBodyWorker.check_inputs(self)
        if self.manifest.get('kind')!='complete97_ordinary_adjoint_Gram_pilot_public_inputs_v1':
            raise ValueError('the independent complete97 Gram pilot manifest is required')
        for path,expected,count in (
            (REL+'notes/2026-11-15-R133-cached-cap-adjoint-proposal-CI-inputs-v2.json',
             PROPOSAL_MANIFEST,253),
            (REL+'notes/2026-11-14-R133-residual-split-cap-Hessian-CI-inputs.json',
             'a3b144b5a6e8c9d84c369f97aac1e849e3035bb7067c461ed574b53b1069d842',164)):
            source=REPO/path;old=read(source)
            if (digest(source)!=expected or len(old['files'])!=count
                or any(self.manifest['files'].get(k)!=v for k,v in old['files'].items())):
                raise ValueError('an original proposal or complete Hessian input pin changed')

    def proposal_artifact(self):
        # Download once in Actions, but retain only the exact seven required
        # arrays plus actual native/process. No QR factor is rerun or copied
        # into the new artifact; no binary passes through a connector.
        metadata=self.artifact_metadata(PROPOSAL_RUN,PROPOSAL_NAME)
        root=self.input_root/PROPOSAL_NAME;marker=root/'selected-complete-proposal-download.json'
        if marker.exists():
            old=read(marker)
            if old.get('artifact_id')!=metadata['id'] or old.get('native_sha256')!=PROPOSAL_NATIVE:
                raise ValueError('the staged exact original adjoint artifact changed')
        else:
            archive=self.work/f"download-complete-adjoint-{metadata['id']}.zip"
            actual=self.zip_download(metadata,archive);root.mkdir(parents=True,exist_ok=True)
            with zipfile.ZipFile(archive) as z:
                infos={info.filename:info for info in z.infolist()}
                for info in z.infolist():
                    path=Path(info.filename)
                    if path.is_absolute() or '..' in path.parts or stat.S_ISLNK(info.external_attr>>16):
                        raise ValueError('one original adjoint artifact path is unsafe')
                def extract(name):
                    if name not in infos or infos[name].is_dir():
                        raise ValueError('one exact original adjoint artifact file is absent')
                    target=root/name;target.parent.mkdir(parents=True,exist_ok=True)
                    with z.open(infos[name]) as source,target.open('wb') as out:
                        shutil.copyfileobj(source,out,8*1024*1024)
                    self.pull_during_download();return target
                pp=extract('process.json');native=extract(PROPOSAL_LOGICAL)
                if digest(native)!=PROPOSAL_NATIVE:
                    raise ValueError('the original completed adjoint native changed')
                d=read(native)
                if len(d.get('proposal_array_receipts',[]))!=7:
                    raise ValueError('all seven original complete adjoint array receipts are required')
                count=0
                for item in d['proposal_array_receipts']:
                    relative=Path(item['file'])
                    if relative.is_absolute() or '..' in relative.parts:
                        raise ValueError('one original exact array receipt path is unsafe')
                    path=extract('proposal-state/'+str(relative))
                    if path.stat().st_size!=item['bytes'] or digest(path)!=item['sha256']:
                        raise ValueError('one actual original exact Hermite array failed its SHA receipt')
                    count+=1
            small(marker,dict(repository=PUBLIC,original_run=PROPOSAL_RUN,artifact_id=metadata['id'],
                artifact_name=PROPOSAL_NAME,api_size_in_bytes=metadata['size_in_bytes'],
                exact_downloaded_archive=actual,native_sha256=PROPOSAL_NATIVE,
                actual_process_sha256=digest(pp),retained_exact_proposal_arrays=count,
                old_QR_factors_extracted_or_recomputed=False))
            archive.unlink()
        pp=root/'process.json';p=read(pp);native=root/PROPOSAL_LOGICAL;d=read(native)
        if (p.get('repository')!=PUBLIC or str(p.get('run_id'))!=str(PROPOSAL_RUN)
            or p.get('worker_source_sha256')!=PROPOSAL_WORKER
            or p.get('input_manifest_sha256')!=PROPOSAL_MANIFEST
            or d.get('source_sha256')!=PROPOSAL_SOURCE or digest(native)!=PROPOSAL_NATIVE
            or not d.get('complete') or d.get('failure')
            or not any(c.get('label')=='new_complete257_state97_input_physical_adjoint_QR_from_original7908_cached_scalar_jets'
                and c.get('actual_returncode')==0 for c in p.get('children',[]))):
            raise ValueError('the actual completed adjoint proposal identity or child receipt changed')
        self.record_process(pp,'original-complete97-adjoint-artifact-process.json')
        self.record_process(marker,'original-complete97-adjoint-selected-download.json')
        return native,pp,root/'proposal-state'

    def inputs(self):
        original=AdjointProposalWorker.inputs(self)
        native,process,arrays=self.proposal_artifact()
        inputs=dict(original,background=self.science/BACKGROUND,local=self.science/LOCAL,
            proposal=native,**{'proposal-process':process})
        return original,inputs,arrays

    def success(self,p,d,input_sha):
        child=any(c.get('label')==LABEL and c.get('actual_returncode')==0 for c in p.get('children',[]))
        reused=bool(p.get('original_complete_success_reused_without_child') and p.get('original_success_process_sha256'))
        return bool((child or reused) and d.get('complete') and not d.get('failure')
            and d.get('source_sha256')==self.manifest['files'][PRODUCER]
            and d.get('core_source_sha256')==self.manifest['files'][CORE]
            and d.get('kind')==KIND and len(d.get('rows',[]))==4
            and d.get('gates') and all(g.get('passed') for g in d['gates'])
            and p.get('actual_input_sha256')==input_sha
            and d.get('mathematical_certificate_for_listed_four_quarters_only')
            and not d.get('complete7908_adjoint_cover_proved')
            and not d.get('complete_full_cap_high_to_low_bound_proved'))

    def previous(self,input_sha):
        root=TOPIC/FOLDER;candidates=[]
        if not root.exists():return None
        for pp in sorted(root.glob('*/process.json')):
            p=read(pp)
            if (p.get('repository')!=PUBLIC or p.get('worker_source_sha256')!=digest(__file__)
                or p.get('input_manifest_sha256')!=self.args.manifest_sha
                or p.get('actual_input_sha256')!=input_sha
                or str(p.get('run_id'))==str(self.state['run_id'])):continue
            records=[x for x in p.get('native_files',[]) if x.get('logical_file')=='native/'+NATIVE]
            if len(records)!=1:continue
            native=self.exact_native(pp.parent,'native/'+NATIVE,p,records[0]['sha256']);d=read(native)
            if (d.get('kind')!=KIND or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
                or d.get('core_source_sha256')!=self.manifest['files'][CORE]):continue
            candidates.append(((int(self.success(p,d,input_sha)),len(d.get('rows',[]))),pp,native))
        return max(candidates,key=lambda x:x[0]) if candidates else None

    def restore_previous(self,previous,input_sha):
        _,rp,rn=previous;p0=read(rp);run=p0['run_id'];attempt=p0.get('run_attempt','1')
        root=self.download(run,artifact_name(run,attempt));pp=root/'process.json';p=read(pp)
        if (p.get('worker_source_sha256')!=digest(__file__)
            or p.get('input_manifest_sha256')!=self.args.manifest_sha
            or p.get('actual_input_sha256')!=input_sha):
            raise ValueError('one exact previous mathematical pilot belongs to another input set')
        entries=[x for x in p.get('native_files',[]) if x.get('logical_file')=='native/'+NATIVE]
        if len(entries)!=1:raise ValueError('the actual pilot prefix has no exact native receipt')
        native=self.exact_native(root,'native/'+NATIVE,p,entries[0]['sha256']);d=read(native)
        if (d.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or d.get('core_source_sha256')!=self.manifest['files'][CORE]
            or d.get('exact_identity')!=read(rn).get('exact_identity')):
            raise ValueError('the original native prefix scientific identity changed')
        for row in d.get('rows',[]):
            item=row['new_array_receipt'];relative=Path(item['file'])
            if relative.is_absolute() or '..' in relative.parts:raise ValueError('an old exact matrix path is unsafe')
            source=root/'matrices'/relative
            if source.stat().st_size!=item['bytes'] or digest(source)!=item['sha256']:
                raise ValueError('one complete old signed Gram/model array is missing or changed')
            target=self.new_arrays/relative
            if target.exists() and digest(target)!=item['sha256']:
                raise ValueError('one old successful Gram would be overwritten')
            if not target.exists():shutil.copyfile(source,target)
        self.record_process(pp,'original-adjoint-Gram-artifact-process.json')
        self.record_process(rp,'original-adjoint-Gram-reviewed-process.json')
        prefix=self.work/'original-adjoint-Gram-prefix.json.gz';shutil.copyfile(native,prefix)
        complete=self.success(p,d,input_sha)
        small(self.evidence/'original-adjoint-Gram-prefix-reuse.json',dict(
            actual_original_process_sha256=digest(pp),reviewed_process_sha256=digest(rp),
            actual_original_native_sha256=digest(native),original_process_complete=p.get('complete'),
            mathematical_complete=complete,successful_quarters=len(d.get('rows',[])),
            failure_preserved=d.get('failure'),publication_success_not_required_for_math_reuse=True))
        if complete:
            shutil.copyfile(native,self.cache/NATIVE);self.reused_complete=True
            self.state['original_success_process_sha256']=digest(pp)
        elif d.get('failure'):
            raise RuntimeError('preserve this real mathematical failure and completed prefix; do not repeat unchanged: '+str(d['failure']))
        return prefix

    def outcome(self,d):
        value={k:d.get(k) for k in ('kind','complete','failure','gates','seconds',
            'completed_quarters','reused_completed_quarters','new_completed_quarters_this_child',
            'exact_identity_sha256','original_proposal_case','old_target_calls',
            'mathematical_certificate_for_listed_four_quarters_only','complete7908_adjoint_cover_proved',
            'complete_full_cap_high_to_low_bound_proved','complete_infinite_BVP_inverse_proved')}
        value['actual_selected_quarters']=[dict(index=r['original_quarter_index'],request=r['request'],
            interval=r['interval'],Gram_trace_uppers=r['complete_Gram_trace_uppers'],
            array_receipt=r['new_array_receipt'],seconds=r['seconds']) for r in d.get('rows',[])]
        return value

    def snapshot(self):
        native=self.cache/NATIVE
        if native.exists():
            raw=native.read_bytes();d=json.loads(gzip.decompress(raw));brief=self.outcome(d)
            brief['native_sha256']=hashlib.sha256(raw).hexdigest()
            brief['latest_actual_readme_check']=self.state.get('readme_checks',[])[-1:]
            small(self.evidence/'actual-latest-adjoint-Gram-pilot-outcome.json',brief)
            self.state['actual_completed_quarters']=len(d.get('rows',[]))
            self.state['latest_scientific_native_sha256']=brief['native_sha256']
        ReviewedBodyWorker.snapshot(self)

    def execute(self,label,command):
        try:return ReviewedBodyWorker.execute(self,label,command)
        finally:
            native=self.cache/NATIVE
            if native.exists():
                d=read(native);brief=self.outcome(d);brief['native_sha256']=digest(native)
                small(self.evidence/'actual-latest-adjoint-Gram-pilot-outcome.json',brief)
                print(json.dumps(brief),flush=True)
                if d.get('failure') and self.log.exists():print(self.log.read_text()[-16000:],flush=True)

    def prepare(self):
        original,inputs,arrays=self.inputs();input_sha={k:digest(v) for k,v in inputs.items()}
        self.state['actual_input_sha256']=input_sha
        bundle=self.work/'exact-original-adjoint-Gram-inputs.json'
        small(bundle,dict(repository=PUBLIC,kind='cached_adjoint_trial_original_inputs_v1',
            files={k:dict(path=str(v),sha256=input_sha[k]) for k,v in original.items()}))
        prefix=None;previous=self.previous(input_sha)
        if previous:prefix=self.restore_previous(previous,input_sha)
        command=[sys.executable,'-u',str(self.science/PRODUCER),'--input-index',str(bundle),
            '--proposal-arrays',str(arrays),'--arrays',str(self.new_arrays),'--out',str(self.cache/NATIVE)]
        for key in ('proposal','proposal-process','background','local'):command+=['--'+key,str(inputs[key])]
        if prefix and not self.reused_complete:command+=['--resume',str(prefix)]
        self.publish()
        if not self.reused_complete:self.execute(LABEL,command)
        d=read(self.cache/NATIVE)
        if (d.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or d.get('core_source_sha256')!=self.manifest['files'][CORE]
            or d.get('kind')!=KIND or not d.get('complete') or d.get('failure')
            or len(d.get('rows',[]))!=4 or not d.get('gates') or not all(x['passed'] for x in d['gates'])
            or not d.get('mathematical_certificate_for_listed_four_quarters_only')
            or d.get('complete7908_adjoint_cover_proved') or d.get('complete_full_cap_high_to_low_bound_proved')):
            raise ValueError('the four actual complete97 Gram domains did not pass their exact scope')
        brief=self.outcome(d);brief.update(native_sha256=digest(self.cache/NATIVE),
            actual_input_sha256=input_sha,original_complete_success_reused_without_child=self.reused_complete)
        small(self.evidence/'complete97-adjoint-residual-Gram-pilot-summary.json',brief)
        for row in d['rows']:
            small(self.evidence/f"actual-adjoint-quarter-{row['original_quarter_index']:04d}-summary.json",
                {k:v for k,v in row.items() if k not in ('complete_radial_intersections','physical_coefficient_model')})
        self.state.update(complete=True,complete_native_sha256=digest(self.cache/NATIVE),
            actual_scientific_gates=len(d['gates']),actual_completed_quarters=4,
            original_complete_success_reused_without_child=self.reused_complete,
            complete_four_closed_quarter_adjoint_Gram_bounds_proved=True,
            complete7908_adjoint_cover_proved=False,complete_full_cap_high_to_low_bound_proved=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','work','artifact-dir'):p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--compute-minutes',type=int,default=170)
    p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='cap-adjoint-residual-Gram-pilot';a.mode='prepare';a.phase='pilot';a.first=0;a.end=4
    a.matrix_run=None;a.matrix_attempt=None;a.recovery_manifest=None;a.recovery_sha=None
    worker=AdjointGramWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):
        signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
