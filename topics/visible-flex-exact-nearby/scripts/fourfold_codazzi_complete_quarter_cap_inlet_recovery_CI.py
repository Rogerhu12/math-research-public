#!/usr/bin/env python3
"""Recover two exact failed endpoint prefixes and consume six frozen successful ranges."""
from __future__ import annotations
import argparse,json,os,shutil,signal,sys,time,urllib.request,urllib.parse,zipfile
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_known_cut_direction_cap_CI_v3 import KnownCutDirectionWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC
from fourfold_native_lossless_parts import restore

REL='topics/visible-flex-exact-nearby/'
PRODUCER=REL+'scripts/fourfold_codazzi_complete_quarter_cap_inlet_recovery.py'
FOLDER='notes/complete_quarter_cap_inlet_recovery_ci'
RANGES=((0,256),(256,512),(512,768),(768,1024),(1024,1280),(1280,1536),(1536,1792),(1792,1977))
ORIGINAL_RANGES=((0,512),(512,1024),(1024,1536),(1536,1977))
KINDS={'range':'actual_complete_fixed_eta_quarter_cap_range_inlet_recovery_v2',
    'finish':'actual_complete_fixed_eta_quarter_cap_finish_inlet_recovery_v2'}
ORIGINAL_RUN=43623547711
ORIGINAL_SOURCE='54e5ec52033bb109618fde1c840730b4b589280382b2da196d3ea748af4490de'
ORIGINAL_WORKER='04d4380d840504f3aedf2da2d95f2112677819885f4a1e367480f97298b332db'
ORIGINAL_MANIFEST='6dc5bf2d8030d506c74dc29ef2cb3c1991cd5f7fb8c2a051b03b0ad89cb2fb69'
ORIGINAL_PLAN='406e3e5331720a3f87f2b5f53c2e7d2988bea25b7537d650157ed97278e3073a'
ORIGINAL_PREFIXES={(0,256):'dff609fe852fb538f126865296e76e991c553f2b586471eb58627461dd320f63',
    (1792,1977):'1d940cb67a807560c016c2fdb07503ca4c0be1ffd0866bf83a988c27477c3028'}
RECOVERY_RANGES=tuple(ORIGINAL_PREFIXES)
API='https://api.github.com/repos/Rogerhu12/math-research-public/'


def small(path,doc):
    raw=(json.dumps(doc,ensure_ascii=False,indent=2)+'\n').encode()
    if len(raw)>60000:raise ValueError('a new plaintext summary exceeds60000 bytes; preserve full native')
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(raw)


def actual(p,run):
    return (p.get('repository')=='Rogerhu12/math-research-public' and str(p.get('run_id'))==str(run)
        and p.get('complete') and not p.get('failure') and p.get('children')
        and all(c.get('actual_returncode')==0 for c in p['children']))


class InletQuarterRecoveryWorker(ReviewedBodyWorker):
    def __init__(self,a):
        super().__init__(a)
        suffix=a.phase if a.phase!='range' else f'range-{a.first:04d}-{a.end:04d}'
        self.name=f'run-{self.run_label}-complete-quarter-cap-inlet-recovery-{suffix}'
        self.dest=TOPIC/FOLDER/self.name;self.reused_complete=False
        self.native_name=('complete1977-fixed-eta-quarter-plan.json.gz' if a.phase=='plan' else
            f'new-fixed-eta-quarter-domains-{a.first:04d}-{a.end:04d}.json.gz' if a.phase=='range' else
            'complete1977-fixed-eta-quarter-cap-sources.json.gz')
        self.state.update(kind='actual_public_complete_fixed_eta_quarter_cap_inlet_recovery_process_v2',
            worker_source_sha256=digest(__file__),phase=a.phase,
            source_range=[a.first,a.end] if a.phase=='range' else None,
            original_fixed_eta_pilot_run=43619535345,original_fixed_eta_pilot_quarters_reused=64,
            exact_original_quarter_run=ORIGINAL_RUN,recovered_range_workflow_run=a.workflow_run,
            original_large_array_reconstructions_executed=0,
            original_completed_domains_recomputed=0,complete_true_cut_source_claimed=False,
            complete_finite193_response_error_proved=False,complete_infinite_BVP_inverse_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='complete_fixed_eta_quarter_cap_inlet_recovery_public_inputs_v2':
            raise ValueError('the exact independent complete-quarter manifest is required')

    def exact_native(self,root,logical,p,expected=None):
        entries=[x for x in p.get('native_files',[]) if x.get('logical_file')==logical]
        if len(entries)!=1:raise ValueError('one exact logical native receipt is required')
        e=entries[0];want=expected or e.get('sha256')
        if not isinstance(want,str) or e.get('sha256')!=want:raise ValueError('native receipt SHA differs')
        path=root/logical
        if not path.exists():
            if 'lossless_manifest' not in e:raise ValueError('the complete original native bytes are absent')
            path=self.work/('restored-'+want+'.json.gz')
            if not path.exists():restore(root/e['lossless_manifest'],path)
        if digest(path)!=want or path.stat().st_size!=e['bytes']:
            raise ValueError('complete native size or SHA differs')
        return path

    def actual_plan(self):
        root=self.args.plan_artifact.resolve();pp=root/'process.json';p=read(pp)
        if (not actual(p,ORIGINAL_RUN) or p.get('phase')!='plan'
            or p.get('worker_source_sha256')!=ORIGINAL_WORKER
            or p.get('input_manifest_sha256')!=ORIGINAL_MANIFEST
            or digest(pp)!='82a44b78e3e3af3e0b1285a828a7aba2026dcc5b04001996bd228243baccca43'):
            raise ValueError('the exact original successful complete-quarter plan process is required')
        path=self.exact_native(root,'native/complete1977-fixed-eta-quarter-plan.json.gz',p,ORIGINAL_PLAN)
        d=read(path)
        if (d.get('kind')!='actual_complete_fixed_eta_quarter_cap_plan_v1'
            or not d.get('complete') or d.get('failure') or d.get('source_sha256')!=ORIGINAL_SOURCE
            or not d.get('gates') or not all(g['passed'] for g in d['gates'])):
            raise ValueError('the original successful plan native differs')
        shutil.copyfile(pp,self.evidence/'actual-original-plan-process.json')
        self.state['actual_plan_native_sha256']=digest(path)
        return path

    def original_prefix(self):
        pair=(self.args.first,self.args.end);expected=ORIGINAL_PREFIXES[pair]
        root=self.args.prefix_artifact.resolve();pp=root/'process.json';p=read(pp)
        if (p.get('repository')!='Rogerhu12/math-research-public'
            or str(p.get('run_id'))!=str(ORIGINAL_RUN) or p.get('source_range')!=list(pair)
            or p.get('phase')!='range' or p.get('worker_source_sha256')!=ORIGINAL_WORKER
            or p.get('input_manifest_sha256')!=ORIGINAL_MANIFEST):
            raise ValueError('the original successful-prefix failure process differs')
        path=self.exact_native(root,f'native/new-fixed-eta-quarter-domains-{pair[0]:04d}-{pair[1]:04d}.json.gz',p,expected)
        shutil.copyfile(pp,self.evidence/'actual-original-successful-prefix-failure-process.json')
        self.state['original_successful_quarter_prefix_native_sha256']=digest(path)
        self.state['original_successful_quarter_prefix_process_sha256']=digest(pp)
        return path,pp

    def api(self,suffix):
        token=os.environ.get('GITHUB_TOKEN')
        if not token:raise RuntimeError('the public Actions artifact read credential is missing')
        request=urllib.request.Request(API+suffix,headers={
            'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json',
            'X-GitHub-Api-Version':'2022-11-28','User-Agent':'visible-exact-original-quarter-recovery'})
        with urllib.request.urlopen(request,timeout=60) as response:
            return json.load(response)

    def download_original_artifact(self,artifact):
        name=artifact['name'];root=self.work/'original-completed-range-artifacts'/name
        receipt=root/'process.json'
        if receipt.exists():return root
        root.mkdir(parents=True,exist_ok=True)
        token=os.environ['GITHUB_TOKEN']
        class ExactRedirect(urllib.request.HTTPRedirectHandler):
            def redirect_request(self,request,fp,code,msg,headers,newurl):
                result=super().redirect_request(request,fp,code,msg,headers,newurl)
                if result is not None and urllib.parse.urlparse(newurl).netloc!='api.github.com':
                    result.remove_header('Authorization')
                return result
        opener=urllib.request.build_opener(ExactRedirect())
        request=urllib.request.Request(API+'actions/artifacts/'+str(artifact['id'])+'/zip',
            headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json',
                'X-GitHub-Api-Version':'2022-11-28','User-Agent':'visible-exact-original-quarter-recovery'})
        archive=self.work/('original-range-artifact-'+str(artifact['id'])+'.zip')
        with opener.open(request,timeout=60) as response,archive.open('wb') as target:
            shutil.copyfileobj(response,target)
        with zipfile.ZipFile(archive) as bundle:
            for member in bundle.infolist():
                target=(root/member.filename).resolve()
                if not target.is_relative_to(root.resolve()) or (member.external_attr>>16)&0o170000==0o120000:
                    raise ValueError('an original artifact contains an invalid member path')
            bundle.extractall(root)
        self.state.setdefault('original_range_artifact_downloads',[]).append(dict(
            artifact_id=artifact['id'],artifact_name=name,archive_sha256=digest(archive),
            archive_bytes=archive.stat().st_size,original_workflow_run=ORIGINAL_RUN))
        if not receipt.exists():raise ValueError('the exact original process is absent from its artifact')
        return root

    def original_completed_ranges(self):
        wanted={f'visible-exact-complete-quarter-cap-range-{first}-{end}-{ORIGINAL_RUN}-1':(first,end)
            for first,end in RANGES if (first,end) not in RECOVERY_RANGES}
        start=time.monotonic();last_publish=start;last_status=None
        while True:
            jobs=self.api('actions/runs/'+str(ORIGINAL_RUN)+'/jobs?per_page=100')['jobs']
            expected={f'ranges ({first}, {end})' for first,end in RANGES if (first,end) not in RECOVERY_RANGES}
            chosen=[j for j in jobs if j['name'] in expected]
            status=[dict(id=j['id'],name=j['name'],status=j['status'],conclusion=j.get('conclusion')) for j in chosen]
            self.state['actual_original_outer_range_jobs']=status
            if status!=last_status:print(json.dumps(dict(original_outer_jobs=status)),flush=True);last_status=status
            failures=[j for j in chosen if j['status']=='completed' and j.get('conclusion')!='success']
            if failures:raise RuntimeError('an original outer range has an actual failure; preserve every existing domain')
            artifacts=self.api('actions/runs/'+str(ORIGINAL_RUN)+'/artifacts?per_page=100')['artifacts']
            found={a['name']:a for a in artifacts if a['name'] in wanted and not a.get('expired')}
            if len(chosen)==6 and all(j['status']=='completed' and j.get('conclusion')=='success' for j in chosen) and set(found)==set(wanted):
                return {wanted[name]:self.download_original_artifact(found[name]) for name in sorted(wanted)}
            if self.interrupted:raise RuntimeError('finish wait interrupted; no completed range was recomputed')
            if time.monotonic()-start>75*60:raise TimeoutError('original ranges are still running; preserve the successful recovery')
            if time.monotonic()-last_publish>=300:
                self.publish();last_publish=time.monotonic()
            time.sleep(20)

    def new_range_inputs(self,plan_sha):
        roots=self.original_completed_ranges()
        candidates={}
        for root in sorted(self.args.recovered_artifacts.resolve().iterdir()):
            pp=root/'process.json'
            if not root.is_dir() or not pp.exists():continue
            p=read(pp);pair=tuple(p.get('source_range') or [])
            if (pair not in RECOVERY_RANGES or p.get('repository')!='Rogerhu12/math-research-public'
                or str(p.get('run_id'))!=str(self.args.workflow_run)
                or p.get('worker_source_sha256')!=digest(__file__)
                or p.get('input_manifest_sha256')!=self.args.manifest_sha):
                raise ValueError('a recovery artifact has a different exact run or science identity')
            if not any(c.get('label')=='actual_complete_quarter_cap_range' and c.get('actual_returncode')==0
                for c in p.get('children',[])):continue
            choice=(int(p.get('run_attempt','1')),root)
            if pair not in candidates or choice[0]>candidates[pair][0]:candidates[pair]=choice
        if set(candidates)!=set(RECOVERY_RANGES):raise ValueError('both successful endpoint recovery ranges are required')
        roots.update({pair:choice[1] for pair,choice in candidates.items()})
        paths=[];processes=[]
        for pair in RANGES:
            root=roots[pair];pp=root/'process.json';p=read(pp)
            recovery=pair in RECOVERY_RANGES;run=self.args.workflow_run if recovery else ORIGINAL_RUN
            worker=digest(__file__) if recovery else ORIGINAL_WORKER
            manifest=self.args.manifest_sha if recovery else ORIGINAL_MANIFEST
            if (p.get('repository')!='Rogerhu12/math-research-public' or str(p.get('run_id'))!=str(run)
                or p.get('phase')!='range' or p.get('source_range')!=list(pair)
                or p.get('worker_source_sha256')!=worker or p.get('input_manifest_sha256')!=manifest
                or p.get('actual_plan_native_sha256')!=plan_sha
                or not any(c.get('label')=='actual_complete_quarter_cap_range' and c.get('actual_returncode')==0
                    for c in p.get('children',[]))):
                raise ValueError('an exact successful original or recovery range process differs')
            path=self.exact_native(root,f'native/new-fixed-eta-quarter-domains-{pair[0]:04d}-{pair[1]:04d}.json.gz',p)
            d=read(path);source=self.manifest['files'][PRODUCER] if recovery else ORIGINAL_SOURCE
            kind=KINDS['range'] if recovery else 'actual_complete_fixed_eta_quarter_cap_range_v1'
            if (not d.get('complete') or d.get('failure') or not d.get('selected_domains_complete')
                or d.get('source_sha256')!=source or d.get('kind')!=kind
                or d.get('plan_native_sha256')!=plan_sha or not d.get('gates')
                or not all(g['passed'] for g in d['gates'])):
                raise ValueError('an exact original or recovery range native is incomplete')
            paths.append(path);processes.append(pp)
            shutil.copyfile(pp,self.evidence/f'actual-quarter-range-{pair[0]:04d}-{pair[1]:04d}-process.json')
        return paths,processes

    def best_prefix(self,input_sha):
        root=TOPIC/FOLDER
        if not root.exists():return None
        found=[]
        for pp in sorted(root.glob('*/process.json')):
            p=read(pp)
            if (p.get('repository')!='Rogerhu12/math-research-public'
                or p.get('phase')!=self.args.phase
                or p.get('worker_source_sha256')!=digest(__file__)
                or p.get('input_manifest_sha256')!=self.args.manifest_sha
                or self.args.phase=='range' and p.get('source_range')!=[self.args.first,self.args.end]):
                continue
            receipts=[r for r in p.get('native_files',[]) if r.get('logical_file')=='native/'+self.native_name]
            if len(receipts)!=1 or not isinstance(receipts[0].get('sha256'),str):continue
            path=self.exact_native(pp.parent,'native/'+self.native_name,p,receipts[0]['sha256']);d=read(path)
            if (d.get('kind')!=KINDS[self.args.phase]
                or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
                or d.get('input_sha256')!=input_sha):continue
            complete=bool(d.get('complete') and not d.get('failure')
                and d.get('gates') and all(g['passed'] for g in d['gates']))
            if complete and not any(c.get('label')=='actual_complete_quarter_cap_'+self.args.phase
                and c.get('actual_returncode')==0 for c in p.get('children',[])):continue
            count=len(d.get('rows',[]))
            if complete or self.args.phase=='range' and count:found.append((complete,count,pp,path,d))
        return max(found,key=lambda x:(x[0],x[1])) if found else None

    def execute(self,label,command):
        try:return super().execute(label,command)
        finally:
            path=self.cache/self.native_name
            if path.exists():
                d=read(path);o=dict(phase=self.args.phase,complete=d.get('complete'),
                    failure=d.get('failure'),gates=d.get('gates',[]),native_sha256=digest(path),
                    complete_new_domains=len(d.get('rows',[])),
                    new_domains_in_this_child=0 if self.reused_complete else d.get('new_quarter_domains_executed_in_this_child',0),
                    original_complete_native_reused=self.reused_complete)
                small(self.evidence/'actual-latest-child-outcome.json',o);print(json.dumps(o),flush=True)
                if d.get('failure') and self.log.exists():print(self.log.read_text()[-16000:],flush=True)

    def prepare(self):
        native=self.cache/self.native_name
        command=[sys.executable,'-u',str(self.science/PRODUCER),'--phase',self.args.phase,
            '--workflow-run',str(self.args.workflow_run),'--out',str(native)]
        if self.args.phase=='range':
            plan=self.actual_plan()
            candidate,proposal=KnownCutDirectionWorker.restore_exact_prepared_arrays(self)
            inputs={'candidate':candidate,'proposal':proposal,
                'object':self.science/self.manifest['intrinsic_object'],
                'repair-report':self.science/self.manifest['continuous_repair'],'plan':plan}
            prefix,prefix_process=self.original_prefix()
            rn,rp=[],[];command+=['--first',str(self.args.first),'--end',str(self.args.end),
                '--original-prefix',str(prefix),'--original-prefix-process',str(prefix_process)]
        else:
            plan=self.actual_plan();inputs={'plan':plan}
            self.publish()
            rn,rp=self.new_range_inputs(digest(plan))
        for k,path in inputs.items():command+=['--'+k,str(path)]
        if rn:command+=['--range-natives',*[str(p) for p in rn],'--range-processes',*[str(p) for p in rp]]
        input_sha={k:digest(v) for k,v in inputs.items()}
        for label,paths in (('range-native',rn),('range-process',rp)):
            input_sha.update({label+'-'+str(i):digest(path) for i,path in enumerate(paths)})
        self.state['actual_input_sha256']=input_sha
        previous=self.best_prefix(input_sha)
        if previous:
            complete,count,pp,path,d=previous;command+=['--resume',str(path)];self.reused_complete=complete
            shutil.copyfile(pp,self.evidence/'original-successful-domain-prefix-process.json')
            small(self.evidence/'original-successful-domain-prefix-reuse.json',dict(
                original_process_sha256=digest(pp),original_native_sha256=digest(path),
                original_process_complete=read(pp).get('complete'),
                original_publication_failure=read(pp).get('failure'),
                original_scientific_failure=d.get('failure'),native_complete=complete,
                completed_new_domains=count,original_completed_domains_recomputed=0))
        self.publish();self.execute('actual_complete_quarter_cap_'+self.args.phase,command)
        d=read(native)
        if (d.get('kind')!=KINDS[self.args.phase] or not d.get('complete') or d.get('failure')
            or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or d.get('input_sha256')!=input_sha or not d.get('gates')
            or not all(g['passed'] for g in d['gates'])
            or d.get('complete_true_cut_source_claimed') or d.get('complete_finite193_response_error_proved')
            or d.get('complete_infinite_BVP_inverse_proved')):
            raise ValueError('the complete new source phase failed or exceeded its scope')
        summary=dict(phase=self.args.phase,kind=d['kind'],complete=True,gates=d['gates'],
            source_sha256=d['source_sha256'],native_sha256=digest(native),input_sha256=input_sha,
            seconds=d.get('seconds'),complete_original_native_retained=True,
            original_completed_domains_recomputed=0,original_complete_native_reused=self.reused_complete,
            actual_new_domains_in_this_child=0 if self.reused_complete else d.get('new_quarter_domains_executed_in_this_child',0),
            complete_finite193_response_error_proved=False,complete_infinite_BVP_inverse_proved=False)
        for key in ('range','complete_original_parent_cells','reused_original_quarter_domains',
            'requested_new_quarter_domains','total_complete_quarter_domains','completed_new_domains',
            'completed_new_quarter_domains','complete_quarter_domains','selected_whole_representation',
            'plan_native_sha256','exact_continuous_direction_definition_sha256','direction_sha256'):
            if key in d:summary[key]=d[key]
        if 'assignments' in d:
            summary['assignments']=[dict(first=r['first'],end=r['end'],
                new_parents=len(r['actual_new_parent_indices']),new_domains=len(r['actual_new_requests']),
                reused_parents=len(r['reused_original_parent_indices'])) for r in d['assignments']]
        for key in ('selected_complete_physical_cap_error','new_coupled_complete_physical_cap_error',
            'all_complete_quarters_physical_cap_error','original_pilot_complete_physical_cap_error',
            'original_direct_coupled_baseline_physical_cap_error'):
            if key in d:summary[key]=d[key]
        for key in ('selected_complete_fourteen_physical_fees','all_complete_quarters_fourteen_physical_fees'):
            if key in d:summary[key]={k:v['upper'] for k,v in d[key].items()}
        small(self.evidence/('complete-quarter-cap-'+self.args.phase+'-summary.json'),summary)
        self.state.update(complete=True,complete_native_sha256=digest(native),actual_scientific_gates=len(d['gates']),
            actual_new_domains_in_this_child=summary['actual_new_domains_in_this_child'],
            actual_completed_new_domains=d.get('completed_new_domains',0))
        if 'selected_complete_physical_cap_error' in d:
            self.state['selected_complete_physical_cap_error']=d['selected_complete_physical_cap_error']


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','work','artifact-dir'):p.add_argument('--'+name,type=Path,required=True)
    for name in ('prepared','plan-artifact','prefix-artifact','recovered-artifacts'):
        p.add_argument('--'+name,type=Path)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--phase',choices=('range','finish'),required=True)
    p.add_argument('--first',type=int,default=0);p.add_argument('--end',type=int,default=256)
    p.add_argument('--workflow-run',type=int,required=True)
    p.add_argument('--compute-minutes',type=int,default=75);p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='complete-fixed-eta-quarter-cap-inlet-recovery';a.mode='prepare';a.recovery_manifest=None;a.recovery_sha=None
    if a.phase=='range' and (a.first,a.end) not in RECOVERY_RANGES:
        raise ValueError('only the two incomplete endpoint ranges may execute')
    if a.plan_artifact is None:raise ValueError('the exact original plan artifact is mandatory')
    if a.phase=='range' and (a.prepared is None or a.prefix_artifact is None):
        raise ValueError('the original exact arrays and successful quarter prefix are mandatory')
    if a.phase=='finish' and a.recovered_artifacts is None:
        raise ValueError('the two actual recovery range artifacts are mandatory')
    worker=InletQuarterRecoveryWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()

if __name__=='__main__':main()
