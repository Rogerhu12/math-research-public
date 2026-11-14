#!/usr/bin/env python3
"""Run only selected new fixed-eta physical coefficient domains in public Actions."""
from __future__ import annotations
import argparse,json,shutil,signal,sys
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_known_cut_direction_cap_CI_v3 import KnownCutDirectionWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC
from fourfold_native_lossless_parts import restore

REL='topics/visible-flex-exact-nearby/'
PRODUCER=REL+'scripts/fourfold_codazzi_fixed_eta_physical_cap_pilot.py'
FOLDER='notes/fixed_eta_physical_cap_pilot_ci'
NATIVE='fixed-eta0-refined-physical-cap-coefficient-pilot.json.gz'
LABEL='actual_fixed_eta0_refined_physical_cap_coefficient_domains'
KIND='actual_fixed_eta0_refined_physical_cap_coefficient_source_pilot_v1'
PILOT='f36831b1f5cc354548686c7d3e5f3fdfb10a456899d25f57d1be1b4cefccbe5c'
PILOT_PROCESS='c6d87b7e9d5ca64c480c34853a5b17e3ca61f0e18417817591f11afa21879cb4'
COMPLETE='8bc061ec200deb37548005297a1530d341eaa55065e70104cc5d82714aed21c5'
RANGES=((0,512),(512,1024),(1024,1536),(1536,1977))


def small(path,doc):
    data=(json.dumps(doc,ensure_ascii=False,indent=2)+'\n').encode()
    if len(data)>60000:raise ValueError('new plaintext exceeded60000 bytes; the complete native remains intact')
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(data)


def actual(p,run):
    return (p.get('repository')=='Rogerhu12/math-research-public' and str(p.get('run_id'))==str(run)
        and p.get('complete') and not p.get('failure') and p.get('children')
        and all(c.get('actual_returncode')==0 for c in p['children']))


class FixedEtaPhysicalPilotWorker(ReviewedBodyWorker):
    def __init__(self,a):
        super().__init__(a)
        self.name=f'run-{self.run_label}-fixed-eta0-physical-cap-pilot'
        self.dest=TOPIC/FOLDER/self.name;self.reused_complete=False;self.original_rows={}
        self.state.update(kind='actual_public_fixed_eta0_refined_physical_cap_pilot_process_v1',
            worker_source_sha256=digest(__file__),original_complete_direction_run=43615251195,
            original_successful_one_column_cells_repeated=0,
            original_large_array_reconstructions_executed=0,
            new_parameter_domain='exact affine offset zero at physical eta0',
            complete_finite193_response_error_proved=False,complete_infinite_BVP_inverse_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='fixed_eta0_refined_physical_cap_pilot_public_inputs_v1':
            raise ValueError('the exact new domain input manifest is required')

    def exact_native(self,root,logical,p,expected=None):
        records=[x for x in p.get('native_files',[]) if x.get('logical_file')==logical]
        if len(records)!=1:raise ValueError('a unique complete logical native receipt is required')
        entry=records[0]
        if expected is not None and entry['sha256']!=expected:raise ValueError('the pinned native differs')
        target=root/logical
        if not target.exists():
            if 'lossless_manifest' not in entry:raise ValueError('the original complete bytes are missing')
            target=self.work/('restored-'+entry['sha256']+'.json.gz')
            if not target.exists():restore(root/entry['lossless_manifest'],target)
        if digest(target)!=entry['sha256'] or target.stat().st_size!=entry['bytes']:
            raise ValueError('the original native identity or size changed')
        return target

    def original_inputs(self):
        candidate,proposal=KnownCutDirectionWorker.restore_exact_prepared_arrays(self)
        root=self.args.pilot_artifact.resolve();pp=root/'process.json';p=read(pp)
        if not actual(p,43610982446) or digest(pp)!=PILOT_PROCESS:
            raise ValueError('the actual successful v3 artifact process is required')
        pilot=self.exact_native(root,'native/known-cut-direction-complete-cap-mixed-source-pilot.json.gz',p,PILOT)
        root=self.args.complete_artifact.resolve();cp=root/'process.json';c=read(cp)
        if (not actual(c,43615251195) or c.get('phase')!='finish'
            or c.get('worker_source_sha256')!='dd13bf009bbee7b3074d9b200a80c91bbcb798b57d00ed3278e34f5533630b38'
            or c.get('input_manifest_sha256')!='6a38fdc16b65fd052fcf85fc91d239941d82d695fd29a71f7ecad8398c8daad2'):
            raise ValueError('the actual complete1977 source process is required')
        complete=self.exact_native(root,'native/complete1977-cut-direction-and-same-Z-sources.json.gz',c,COMPLETE)
        full=read(complete);receipt={tuple(x['range']):x for x in full['range_receipts']}
        self.range_natives=[];self.range_processes=[]
        self.original_rows={r['index']:r for r in read(pilot)['new_one_column_rows']}
        for first,end in RANGES:
            root=self.args.range_artifacts/f'visible-exact-complete-cut-Z-range-{first}-{end}-43615251195-1'
            rp=root/'process.json';r=read(rp);expected=receipt[(first,end)]
            if (not actual(r,43615251195) or r.get('phase')!='range'
                or digest(rp)!=expected['actual_original_process_sha256']):
                raise ValueError('the original successful direct range artifact snapshot differs')
            native=self.exact_native(root,f'native/new-cut-direction-Z-cells-{first:04d}-{end:04d}.json.gz',
                r,expected['native_sha256'])
            self.range_natives.append(native);self.range_processes.append(rp)
            for row in read(native)['new_one_column_rows']:
                if row['index'] in self.original_rows:raise ValueError('a successful original direct cell is duplicated')
                self.original_rows[row['index']]=row
            shutil.copyfile(rp,self.evidence/f'original-range-{first:04d}-{end:04d}-process.json')
        shutil.copyfile(pp,self.evidence/'original-v3-pilot-process.json')
        shutil.copyfile(cp,self.evidence/'original-complete1977-process.json')
        return {'candidate':candidate,'proposal':proposal,
            'object':self.science/self.manifest['intrinsic_object'],
            'repair-report':self.science/self.manifest['continuous_repair'],
            'pilot':pilot,'pilot-process':pp,'complete':complete,'complete-process':cp}

    def prefix(self,input_sha):
        root=TOPIC/FOLDER
        if not root.exists():return None
        candidates=[]
        for pp in sorted(root.glob('*/process.json')):
            p=read(pp)
            if p.get('repository')!='Rogerhu12/math-research-public':continue
            records=[x for x in p.get('native_files',[]) if x.get('logical_file')=='native/'+NATIVE]
            if len(records)!=1:continue
            native=self.exact_native(pp.parent,'native/'+NATIVE,p,records[0]['sha256']);d=read(native)
            if (d.get('kind')!=KIND or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
                or d.get('input_sha256')!=input_sha or not d.get('new_domain_results')):continue
            complete=bool(d.get('complete') and not d.get('failure') and d.get('gates')
                and all(g['passed'] for g in d['gates']))
            if complete and not any(x.get('label')==LABEL and x.get('actual_returncode')==0 for x in p.get('children',[])):
                continue
            candidates.append((complete,len(d['new_domain_results']),pp,native))
        return max(candidates,key=lambda x:(x[0],x[1])) if candidates else None

    def execute(self,label,command):
        try:return super().execute(label,command)
        finally:
            path=self.cache/NATIVE
            if path.exists():
                d=read(path)
                out=dict(complete=d.get('complete'),failure=d.get('failure'),gates=d.get('gates',[]),
                    native_sha256=digest(path),completed_new_fixed_eta_domains=len(d.get('new_domain_results',[])),
                    original_complete_native_reused=self.reused_complete)
                small(self.evidence/'actual-latest-child-outcome.json',out);print(json.dumps(out),flush=True)
                if d.get('failure') and self.log.exists():print(self.log.read_text()[-16000:],flush=True)

    def diagnostics(self,d):
        def upper(value):return value['upper']
        for parent in d['selected_original_cells']:
            old=self.original_rows[parent]
            choices=d['complete_parent_representation_decisions'][parent]
            record=dict(parent=parent,interval=old['interval'],original_direct_row_sha256=choices['original_direct_row_sha256'],
                original_all_eight_accumulator_terms={k:upper(v) for k,v in old['accumulator_terms'].items()},
                original_physical_coefficient_error_terms={name:{
                    'complete_joint_A0_error':upper(model['complete_joint_A0_error']),
                    'terms':{k:upper(v) for k,v in model['complete_error_terms'].items()}}
                    for name,model in old['physical_coefficient_models'].items()},
                original_scalar_remainder={k:upper(v) for k,v in old['scalar_remainder'].items()},
                selected_coupled_representation=choices['selected_representation'],
                coupled_refinement_options=[dict(subdivision=x['subdivision'],
                    coupled_cell_fee_for_selection=upper(x['coupled_cell_fee_for_selection']),
                    all_eight_accumulator_terms={k:upper(v) for k,v in x['all_eight_terms'].items()})
                    for x in choices['refined_options']],
                all_new_domains=[])
            for r in d['new_domain_results']:
                if r['request'][0]!=parent:continue
                record['all_new_domains'].append(dict(request=r['request'],interval=r['interval'],
                    complete_joint_A0_errors={k:upper(v['complete_joint_A0_error'])
                        for k,v in r['physical_coefficient_models'].items()},
                    scalar_remainder={k:upper(v) for k,v in r['scalar_remainder'].items()}))
            small(self.evidence/f'selected-parent-{parent:04d}-diagnostic.json',record)

    def prepare(self):
        inputs=self.original_inputs();identity={k:digest(v) for k,v in inputs.items()}
        identity.update({'range-native-'+str(i):digest(v) for i,v in enumerate(self.range_natives)})
        identity.update({'range-process-'+str(i):digest(v) for i,v in enumerate(self.range_processes)})
        self.state['actual_input_sha256']=identity;native=self.cache/NATIVE
        command=[sys.executable,'-u',str(self.science/PRODUCER),'--out',str(native)]
        for key,value in inputs.items():command+=['--'+key,str(value)]
        command+=['--range-natives',*map(str,self.range_natives),'--range-processes',*map(str,self.range_processes)]
        old=self.prefix(identity)
        if old:
            complete,count,pp,path=old;self.reused_complete=complete;command+=['--resume',str(path)]
            shutil.copyfile(pp,self.evidence/'original-completed-domain-prefix-process.json')
            small(self.evidence/'original-domain-prefix-reuse.json',dict(
                original_process_sha256=digest(pp),original_native_sha256=digest(path),
                original_process_complete=read(pp).get('complete'),native_complete=complete,
                complete_new_domains_reused=count,source_and_all_actual_inputs_exactly_matched=True))
        self.publish();self.execute(LABEL,command)
        d=read(native)
        if (not d.get('complete') or d.get('failure') or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or d.get('input_sha256')!=identity or d.get('complete_new_fixed_eta_domains')!=336
            or d.get('complete_original_parent_cells')!=1977 or not d.get('gates')
            or not all(x['passed'] for x in d['gates'])
            or d.get('complete_finite193_response_error_proved') or d.get('complete_infinite_BVP_inverse_proved')):
            raise ValueError('the complete new-domain pilot failed or changed its scientific scope')
        summary={k:v for k,v in d.items() if k not in ('new_domain_results','complete_parent_representation_decisions')}
        summary.update(native_sha256=digest(native),complete_original_native_retained=True,
            actual_new_domains_in_this_child=0 if self.reused_complete else d['new_fixed_eta_coefficient_domains_executed_in_this_child'])
        small(self.evidence/'fixed-eta0-physical-cap-pilot-summary.json',summary)
        self.diagnostics(d)
        self.state.update(complete=True,complete_native_sha256=digest(native),actual_scientific_gates=len(d['gates']),
            actual_complete_new_domains=336,actual_complete_parent_cells=1977,
            actual_new_domains_in_this_child=summary['actual_new_domains_in_this_child'],
            selected_complete_physical_cap_error=d['selected_complete_physical_cap_error'],
            original_direct_coupled_baseline_physical_cap_error=d['original_direct_coupled_baseline_physical_cap_error'])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','work','artifact-dir','prepared','pilot-artifact','complete-artifact','range-artifacts'):
        p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--compute-minutes',type=int,default=60);p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='fixed-eta0-physical-cap-pilot';a.mode='prepare';a.first=0;a.end=0
    a.recovery_manifest=None;a.recovery_sha=None
    worker=FixedEtaPhysicalPilotWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()

if __name__=='__main__':main()
