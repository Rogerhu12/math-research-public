#!/usr/bin/env python3
"""Reviewed public DAG for complete fixed-eta quarter-cell cap sources."""
from __future__ import annotations
import argparse,json,shutil,signal,sys
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_known_cut_direction_cap_CI_v3 import KnownCutDirectionWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC
from fourfold_native_lossless_parts import restore

REL='topics/visible-flex-exact-nearby/'
PRODUCER=REL+'scripts/fourfold_codazzi_complete_quarter_cap_sources.py'
FOLDER='notes/complete_quarter_cap_ci'
RANGES=((0,256),(256,512),(512,768),(768,1024),(1024,1280),(1280,1536),(1536,1792),(1792,1977))
ORIGINAL_RANGES=((0,512),(512,1024),(1024,1536),(1536,1977))
KINDS={k:'actual_complete_fixed_eta_quarter_cap_'+k+'_v1' for k in ('plan','range','finish')}


def small(path,doc):
    raw=(json.dumps(doc,ensure_ascii=False,indent=2)+'\n').encode()
    if len(raw)>60000:raise ValueError('a new plaintext summary exceeds60000 bytes; preserve full native')
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(raw)


def actual(p,run):
    return (p.get('repository')=='Rogerhu12/math-research-public' and str(p.get('run_id'))==str(run)
        and p.get('complete') and not p.get('failure') and p.get('children')
        and all(c.get('actual_returncode')==0 for c in p['children']))


class FullQuarterCapWorker(ReviewedBodyWorker):
    def __init__(self,a):
        super().__init__(a)
        suffix=a.phase if a.phase!='range' else f'range-{a.first:04d}-{a.end:04d}'
        self.name=f'run-{self.run_label}-complete-quarter-cap-{suffix}'
        self.dest=TOPIC/FOLDER/self.name;self.reused_complete=False
        self.native_name=('complete1977-fixed-eta-quarter-plan.json.gz' if a.phase=='plan' else
            f'new-fixed-eta-quarter-domains-{a.first:04d}-{a.end:04d}.json.gz' if a.phase=='range' else
            'complete1977-fixed-eta-quarter-cap-sources.json.gz')
        self.state.update(kind='actual_public_complete_fixed_eta_quarter_cap_process_v1',
            worker_source_sha256=digest(__file__),phase=a.phase,
            source_range=[a.first,a.end] if a.phase=='range' else None,
            original_fixed_eta_pilot_run=43619535345,original_fixed_eta_pilot_quarters_reused=64,
            original_large_array_reconstructions_executed=0,
            original_completed_domains_recomputed=0,complete_true_cut_source_claimed=False,
            complete_finite193_response_error_proved=False,complete_infinite_BVP_inverse_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='complete_fixed_eta_quarter_cap_public_inputs_v1':
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

    def plan_inputs(self):
        result={'candidate':self.science/self.manifest['published_candidate'],
            'proposal':self.science/self.manifest['precomposed_descriptor'],
            'object':self.science/self.manifest['intrinsic_object'],
            'repair-report':self.science/self.manifest['continuous_repair']}
        specs=[
            ('pilot',self.args.pilot_artifact,43610982446,
             'known-cut-direction-complete-cap-mixed-source-pilot.json.gz',
             'f36831b1f5cc354548686c7d3e5f3fdfb10a456899d25f57d1be1b4cefccbe5c',
             'ccf1b8d76eb68ce2731538b87e6f90f627d2633d1dc469272176743ba422d4d0',
             'fb0971a3d5e471c7c8d13d009c7dd23b109e3c88e6875f3236373cd79e329f5a'),
            ('complete',self.args.complete_artifact,43615251195,
             'complete1977-cut-direction-and-same-Z-sources.json.gz',
             '8bc061ec200deb37548005297a1530d341eaa55065e70104cc5d82714aed21c5',
             'dd13bf009bbee7b3074d9b200a80c91bbcb798b57d00ed3278e34f5533630b38',
             '6a38fdc16b65fd052fcf85fc91d239941d82d695fd29a71f7ecad8398c8daad2'),
            ('fixed-pilot',self.args.fixed_artifact,43619535345,
             'fixed-eta0-refined-physical-cap-coefficient-pilot.json.gz',
             'b5a157d4005eb4aad1c536512c4ea5dcb431e90d09c4b05f324db5cf09203138',
             '953940428d8c2ac6a1bf9a1874d9e806d8920f2787f00ba9042ce449db208267',
             '0e0c95425c53d9fa0d3287f656b9ac478483ff03b159a5412048b39e04f5ffad')]
        for role,rawroot,run,name,expected,worker,manifest in specs:
            root=rawroot.resolve();pp=root/'process.json';p=read(pp)
            if (not actual(p,run) or p.get('worker_source_sha256')!=worker
                or p.get('input_manifest_sha256')!=manifest or p.get('complete_native_sha256')!=expected):
                raise ValueError('an actual original completed cap artifact differs')
            if role=='pilot' and digest(pp)!='c6d87b7e9d5ca64c480c34853a5b17e3ca61f0e18417817591f11afa21879cb4':
                raise ValueError('the exact actual v3 pilot artifact snapshot differs')
            result[role]=self.exact_native(root,'native/'+name,p,expected)
            result[('fixed-process' if role=='fixed-pilot' else role+'-process')]=pp
            shutil.copyfile(pp,self.evidence/('original-'+role+'-process.json'))
        full=read(result['complete']);receipts={tuple(r['range']):r for r in full['range_receipts']}
        self.original_natives=[];self.original_processes=[]
        for first,end in ORIGINAL_RANGES:
            root=self.args.original_ranges/f'visible-exact-complete-cut-Z-range-{first}-{end}-43615251195-1'
            pp=root/'process.json';p=read(pp);r=receipts[(first,end)]
            if (not actual(p,43615251195) or p.get('phase')!='range'
                or digest(pp)!=r['actual_original_process_sha256']):
                raise ValueError('an original complete direct range artifact snapshot differs')
            path=self.exact_native(root,f'native/new-cut-direction-Z-cells-{first:04d}-{end:04d}.json.gz',
                p,r['native_sha256'])
            self.original_natives.append(path);self.original_processes.append(pp)
            shutil.copyfile(pp,self.evidence/f'original-direct-range-{first:04d}-{end:04d}-process.json')
        return result

    def actual_plan(self):
        root=self.args.plan_artifact.resolve();pp=root/'process.json';p=read(pp)
        if (not actual(p,self.args.workflow_run) or p.get('phase')!='plan'
            or p.get('worker_source_sha256')!=digest(__file__)
            or p.get('input_manifest_sha256')!=self.args.manifest_sha):
            raise ValueError('the exact current successful complete-quarter plan process is required')
        path=self.exact_native(root,'native/complete1977-fixed-eta-quarter-plan.json.gz',p)
        d=read(path)
        if (d.get('kind')!=KINDS['plan'] or not d.get('complete') or d.get('failure')
            or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or not d.get('gates') or not all(g['passed'] for g in d['gates'])):
            raise ValueError('the complete actual source plan is required')
        shutil.copyfile(pp,self.evidence/'actual-plan-process.json')
        self.state['actual_plan_native_sha256']=digest(path)
        return path

    def new_range_inputs(self,plan_sha):
        found={}
        for root in sorted(self.args.range_artifacts.iterdir()):
            if not root.is_dir() or not (root/'process.json').exists():continue
            pp=root/'process.json';p=read(pp);pair=tuple(p.get('source_range') or [])
            # A rerun of only failed jobs may leave earlier-attempt artifacts.
            # Retain them in Actions, but choose one exact successful receipt per
            # range.  Never add overlapping attempts as extra mathematical rows.
            if (pair not in RANGES or p.get('phase')!='range'
                or p.get('worker_source_sha256')!=digest(__file__)
                or p.get('input_manifest_sha256')!=self.args.manifest_sha
                or p.get('actual_plan_native_sha256')!=plan_sha):
                raise ValueError('a quarter range artifact has a different frozen scientific identity')
            if not actual(p,self.args.workflow_run):continue
            path=self.exact_native(root,f'native/new-fixed-eta-quarter-domains-{pair[0]:04d}-{pair[1]:04d}.json.gz',p)
            choice=(int(p.get('run_attempt','1')),path,pp)
            if pair not in found or choice[0]>found[pair][0]:found[pair]=choice
        if set(found)!=set(RANGES):raise ValueError('all eight actual completed quarter ranges are required')
        paths=[];processes=[]
        for pair in RANGES:
            attempt,path,pp=found[pair];paths.append(path);processes.append(pp)
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
        if self.args.phase=='plan':
            inputs=self.plan_inputs();rn,rp=self.original_natives,self.original_processes
        elif self.args.phase=='range':
            plan=self.actual_plan()
            candidate,proposal=KnownCutDirectionWorker.restore_exact_prepared_arrays(self)
            inputs={'candidate':candidate,'proposal':proposal,
                'object':self.science/self.manifest['intrinsic_object'],
                'repair-report':self.science/self.manifest['continuous_repair'],'plan':plan}
            rn,rp=[],[];command+=['--first',str(self.args.first),'--end',str(self.args.end)]
        else:
            plan=self.actual_plan();inputs={'plan':plan};rn,rp=self.new_range_inputs(digest(plan))
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
    for name in ('prepared','pilot-artifact','complete-artifact','fixed-artifact','original-ranges','plan-artifact','range-artifacts'):
        p.add_argument('--'+name,type=Path)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--phase',choices=('plan','range','finish'),required=True)
    p.add_argument('--first',type=int,default=0);p.add_argument('--end',type=int,default=0)
    p.add_argument('--workflow-run',type=int,required=True)
    p.add_argument('--compute-minutes',type=int,default=75);p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='complete-fixed-eta-quarter-cap';a.mode='prepare';a.recovery_manifest=None;a.recovery_sha=None
    worker=FullQuarterCapWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()

if __name__=='__main__':main()
