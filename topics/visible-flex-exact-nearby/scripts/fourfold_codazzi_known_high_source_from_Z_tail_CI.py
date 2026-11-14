#!/usr/bin/env python3
"""Public exact-input orchestration for the known M32-centre Z-tail source.

Only the new directed coefficient norm consumer runs. Original complete
target, mean and source rows are restored and audited without recomputation.
Every successful prefix is reusable even if its later publication failed.
"""
from __future__ import annotations
import argparse,json,shutil,signal,sys
from pathlib import Path
from types import SimpleNamespace
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_body_mean_CI_finish import CompleteMeanWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC
from fourfold_native_lossless_parts import restore

REL='topics/visible-flex-exact-nearby/'
PRODUCER=REL+'scripts/fourfold_codazzi_known_high_source_from_Z_tail.py'
OLD_MANIFEST='c214f800a5094c905c554e9053c52567d5ae5d76be41ac2e3fe9d673b396d784'
REPAIR='05e0493dbe55490adec8fb6603e0ec431d1bc03f051aec86be8a78741f60f0a4'
REPAIR_PROCESS='16de872ce106e05b6add99d8406598de3cc87b94f4533a9fc3bb46294c66366a'
MIXED='365f0763d8f4c87182507c4372a3be055624607a77d818a084471b368b33d32e'
MIXED_PROCESS='56c84147351d56b262a17ae0cbf96e18c6525083d72bd51e2f590620dc6e5168'
NATIVE='complete-repaired-M32-known-high-tail-source.json.gz'
KIND='actual_complete_repaired_M32_known_high_source_from_Z_tail_v1'


def small(path,data):
    raw=(json.dumps(data,ensure_ascii=False,indent=2)+'\n').encode()
    if len(raw)>60000:raise ValueError('small source evidence exceeds60000 bytes; preserve full native instead')
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(raw)


def actual(p,run):
    return (p.get('repository')=='Rogerhu12/math-research-public'
        and str(p.get('run_id'))==str(run) and p.get('complete')
        and not p.get('failure') and p.get('children')
        and all(c.get('actual_returncode')==0 for c in p['children']))


class KnownHighWorker(ReviewedBodyWorker):
    def __init__(self,a):
        super().__init__(a)
        self.name=f'run-{self.run_label}-complete-known-high-Z-tail-source'
        self.dest=TOPIC/'notes/known_high_Z_tail_source_ci'/self.name
        self.state.update(kind='actual_public_complete_known_high_Z_tail_source_process_v1',
            worker_source_sha256=digest(__file__),new_target_provider_calls=0,
            original_complete_body_run=43583838026,original_complete_repair_source_run=43597921732,
            original_complete_mixed_Z_source_run=43613560173,
            new_original_residual_evaluations=0,new_mean_flow_evaluations=0,
            complete_infinite_inverse_proved=False,actual_full_PDE_response_error_proved=False,
            coefficient_family_delta='0',fixed_repaired_M32_centre_only=True)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='complete_known_high_Z_tail_source_public_inputs_v1':
            raise ValueError('the separately frozen known high source manifest is required')

    def execute(self,label,command):
        try:return super().execute(label,command)
        finally:
            p=self.cache/NATIVE
            if p.exists():
                d=read(p);rows=d.get('rows',[])
                outcome=dict(native_sha256=digest(p),complete=d.get('complete'),failure=d.get('failure'),
                    gates=d.get('gates',[]),actual_complete_rows=len(rows),
                    actual_new_tail_source_rows=d.get('actual_new_tail_source_rows'),
                    actual_reused_tail_source_rows=d.get('actual_reused_tail_source_rows'))
                small(self.evidence/'actual-latest-child-outcome.json',outcome)
                print(json.dumps(outcome),flush=True)
                if d.get('failure') and self.log.exists():print(self.log.read_text()[-16000:],flush=True)

    def exact_native(self,root,name,process,expected):
        matches=[x for x in process.get('native_files',[]) if x.get('logical_file')=='native/'+name]
        p=root/'native'/name
        if not p.exists():
            if len(matches)!=1 or matches[0].get('sha256')!=expected or not matches[0].get('lossless_manifest'):
                raise ValueError('the exact original native byte receipt is absent')
            p=self.work/('restored-'+expected+'.json.gz')
            if not p.exists():restore(root/matches[0]['lossless_manifest'],p)
        if digest(p)!=expected:raise ValueError('an exact actual native SHA changed')
        return p

    def original_inputs(self):
        old_path=self.science/self.manifest['original_body_manifest']
        if digest(old_path)!=OLD_MANIFEST:raise ValueError('the exact original body manifest changed')
        old=read(old_path);audit_dir=self.evidence/'original-input-audit';audit_dir.mkdir(exist_ok=True)
        audit=SimpleNamespace(args=SimpleNamespace(
            prepared=self.args.prepared,manifest_sha=OLD_MANIFEST,
            original_run=43583838026,original_attempt=1,previous_artifacts=self.args.previous_artifacts),
            manifest=old,science=self.science,science_topic=self.science_topic,evidence=audit_dir,state={})
        CompleteMeanWorker.restore_original_bundle(audit)
        parts=CompleteMeanWorker.original_complete_parts(audit)
        values={}
        for label,root,name,expected,expected_process,run in (
            ('repair-source',self.args.repair_artifact,'complete-known-response-centre-repair-source.json.gz',
                REPAIR,REPAIR_PROCESS,43597921732),
            ('mixed',self.args.mixed_artifact,'complete7721-mixed-Z-sources.json.gz',
                MIXED,MIXED_PROCESS,43613560173)):
            root=root.resolve();pp=root/'process.json';p=read(pp)
            if (digest(pp)!=expected_process or not actual(p,run)
                or p.get('complete_native_sha256')!=expected):
                raise ValueError('the exact successful original '+label+' artifact receipt is required')
            native=self.exact_native(root,name,p,expected)
            process_label='repair-process' if label=='repair-source' else 'mixed-process'
            values[label]=native;values[process_label]=pp
            shutil.copyfile(pp,self.evidence/('original-'+process_label+'.json'))
        values.update({
            'original-manifest':old_path,
            'candidate':self.science/old['published_candidate'],
            'response':Path(old['row_identity']['full_trials']['response']['path']),
            'direction':self.science/self.manifest['complete_continuous_direction_native']})
        return values,parts

    def prefix(self,identity):
        root=TOPIC/'notes/known_high_Z_tail_source_ci';choices=[]
        if not root.exists():return None
        for pp in sorted(root.glob('*/process.json')):
            p=read(pp)
            if (p.get('repository')!='Rogerhu12/math-research-public'
                or p.get('worker_source_sha256')!=digest(__file__)
                or p.get('input_manifest_sha256')!=self.args.manifest_sha
                or p.get('actual_common_input_sha256')!=identity):
                continue
            matches=[x for x in p.get('native_files',[]) if x.get('logical_file')=='native/'+NATIVE]
            if len(matches)!=1:continue
            path=self.exact_native(pp.parent,NATIVE,p,matches[0]['sha256'])
            d=read(path);rows=d.get('rows',[])
            if (d.get('kind')!=KIND or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
                or d.get('common_input_sha256')!=identity
                or [r['common_row'] for r in rows]!=list(range(len(rows))) or len(rows)>7721):
                continue
            if d.get('complete') and (d.get('failure') or not d.get('gates')
                or not all(g['passed'] for g in d['gates'])
                or not p.get('children') or any(c.get('actual_returncode')!=0 for c in p['children'])):
                continue
            choices.append((len(rows),path,pp,digest(path)))
        if not choices:return None
        _,path,pp,expected=max(choices,key=lambda x:x[0])
        target=self.work/'preserved-original-known-high-prefix.json.gz';shutil.copyfile(path,target)
        small(self.evidence/'actual-prefix-reuse-receipt.json',dict(
            original_actual_process_sha256=digest(pp),original_native_sha256=expected,
            original_completed_rows=read(target).get('rows') and len(read(target)['rows']) or 0,
            original_native_bytes_reused=True,completed_mathematical_rows_recomputed=0,
            original_publication_complete_not_required=True))
        return target

    def prepare(self):
        values,parts=self.original_inputs()
        identity={name:digest(path) for name,path in values.items()}
        self.state['actual_common_input_sha256']=identity;self.publish()
        prefix=self.prefix(identity);native=self.cache/NATIVE
        command=[sys.executable,'-u',str(self.science/PRODUCER)]
        for name,path in values.items():command+=['--'+name,str(path)]
        command+=['--parts',*[str(p) for p in parts],'--out',str(native)]
        if prefix:command+=['--resume',str(prefix)]
        self.execute('actual_complete7721_known_high_from_exact_Z_tail',command)
        d=read(native)
        if (d.get('kind')!=KIND or not d.get('complete') or d.get('failure')
            or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or d.get('common_input_sha256')!=identity
            or d.get('complete_original_common_rows')!=7721 or len(d.get('rows',[]))!=7721
            or not d.get('gates') or not all(g['passed'] for g in d['gates'])
            or not d.get('complete_known_high_source_bound_proved')
            or not d.get('all_original_low_and_independent_mean_bounds_retained_without_recomputation')
            or d.get('new_target_provider_calls')!=0
            or d.get('actual_full_PDE_response_error_proved') or d.get('complete_infinite_inverse_proved')):
            raise ValueError('the complete actual known-high source consumer failed or exceeded its scope')
        summary={k:v for k,v in d.items() if k not in ('rows','original_parts')}
        summary['native_sha256']=digest(native)
        small(self.evidence/'complete-known-high-Z-tail-source-summary.json',summary)
        # Read-only diagnostics of the completed rows; do not transfer giant summaries.
        from fourfold_codazzi_known_high_source_from_Z_tail import up
        worst=sorted(d['rows'],key=lambda r:up(r['selected_known_high']['L2_sup']),reverse=True)[:20]
        small(self.evidence/'largest-known-high-source-rows.json',dict(native_sha256=digest(native),
            rows=[{k:r[k] for k in ('common_row','interval','continuous_Z_tail33_through96_A0',
                'continuous_Z_tail33_through96_angular_A0','tail_high_L2_sup',
                'original_known_high','selected_known_high')} for r in worst]))
        self.state.update(complete=True,complete_native_sha256=digest(native),
            actual_original_common_rows_consumed=7721,
            actual_new_tail_source_rows=d['actual_new_tail_source_rows'],
            actual_reused_tail_source_rows=d['actual_reused_tail_source_rows'],
            complete_known_high_bounds=d['complete_known_high_bounds'],
            unknown_high_input_feedback_still_required=True,
            delta_nonzero_background_transfer_still_required=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','prepared','previous-artifacts','repair-artifact','mixed-artifact','work','artifact-dir'):
        p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--compute-minutes',type=int,default=35);p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='complete-known-high-Z-tail-source';a.mode='prepare';a.first=0;a.end=7721
    a.recovery_manifest=None;a.recovery_sha=None
    worker=KnownHighWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
