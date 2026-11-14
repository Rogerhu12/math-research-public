#!/usr/bin/env python3
"""Consume completed native bytes and pay only the new full-real-delta transfer."""
from __future__ import annotations
import argparse,json,os,shutil,signal,subprocess,sys
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC,REPO
from fourfold_native_lossless_parts import restore

REL='topics/visible-flex-exact-nearby/'
SELF=REL+'scripts/fourfold_codazzi_full_delta_positive_CI.py'
OUTER=REL+'scripts/fourfold_codazzi_full_delta_regular_Hs_outer.py'
BODY=REL+'scripts/fourfold_codazzi_full_delta_positive_high_Volterra.py'
FOLDER=REL+'notes/full_delta_positive_ci/'
OLD_BODY='eefb94952a409473fed7f9c34afc9214a3346d8c3b19ed7e0a7fc6fd06f48a68'
OLD_OUTER='75e7c0e1447306a97971ee05dcb68b8d357cb4fffa5c1a37335a6fc29a473424'
OLD_REPAIR='05e0493dbe55490adec8fb6603e0ec431d1bc03f051aec86be8a78741f60f0a4'
REPAIR_PROCESS='16de872ce106e05b6add99d8406598de3cc87b94f4533a9fc3bb46294c66366a'
OLD_POSITIVE_WORKER='9b9ae2e6bc08cbfd6dfd531d324342fbed070cf0c9ed21ea1c35a75965ea0480'
OLD_POSITIVE_MANIFEST='a61b4053128b75672816fad256139e2cd8c231cf752321f82f276a9d0d992cd0'

def small(path,doc):
    data=(json.dumps(doc,ensure_ascii=False,indent=2)+'\n').encode()
    if len(data)>60000:raise ValueError('a new plaintext summary exceeds60000 bytes; full native retained')
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(data)

def successful(process,run):
    return (process.get('repository')=='Rogerhu12/math-research-public'
        and str(process.get('run_id'))==str(run) and process.get('complete')
        and not process.get('failure') and process.get('children')
        and all(c.get('actual_returncode')==0 for c in process['children']))

def hydrate(a):
    if digest(a.manifest)!=a.manifest_sha or digest(a.rules)!=a.rules_sha:
        raise ValueError('the exact manifest or separately reviewed rules changed')
    doc=read(a.manifest)
    if doc['files'].get(SELF)!=digest(__file__):raise ValueError('the new transfer worker changed')
    paths=set(doc['files'])|{'README.md',REL+'README.md',FOLDER,
        str(a.manifest.relative_to(REPO)),str(a.rules.relative_to(REPO))}
    subprocess.run(['git','-c','safe.directory='+str(REPO),'sparse-checkout','set','--no-cone','--stdin'],
        cwd=REPO,input='\n'.join('/'+p for p in sorted(paths))+'\n',text=True,check=True)
    print(json.dumps(dict(exact_paths=len(paths),old_large_coefficient_and_frame_directories_not_hydrated=True)))

class FullDeltaPositiveWorker(ReviewedBodyWorker):
    def __init__(self,a):
        super().__init__(a)
        self.name=f'run-{self.run_label}-full-real-delta-positive'
        self.dest=REPO/FOLDER/self.name
        self.active_native=None
        self.state.update(kind='actual_public_full_real_delta_outer_and_positive_process_v1',
            worker_source_sha256=digest(__file__),exact_real_delta_radius='1/100000000',
            original_positive_rows_recomputed=0,original_response_rows_recomputed=0,
            original_target_endpoint_cap_and_nonlinear_solves_recomputed=0,
            complete_positive_finite_head_inverse_proved=False,
            complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='full_real_delta_cached_outer_and_positive_public_inputs_v1':
            raise ValueError('the independent full delta input manifest is required')

    def exact_native(self,root,name,process,expected):
        logical='native/'+name
        records=[x for x in process.get('native_files',[]) if x.get('logical_file')==logical]
        if len(records)!=1 or records[0].get('sha256')!=expected:
            raise ValueError('the unique native receipt differs: '+logical)
        entry=records[0];path=root/'native'/name
        if not path.exists():
            if 'lossless_manifest' not in entry:raise ValueError('the exact native bytes are absent')
            path=self.work/('restored-'+expected+'.json.gz')
            if not path.exists():restore(root/entry['lossless_manifest'],path)
        if digest(path)!=expected or path.stat().st_size!=entry['bytes']:
            raise ValueError('the unchanged native bytes or complete size differ')
        return path

    def original_inputs(self):
        positive=self.args.positive_artifact.resolve()
        repair=self.args.repair_artifact.resolve()
        pp=positive/'process.json';rp=repair/'process.json'
        p,q=read(pp),read(rp)
        if (not successful(p,43601149891)
            or p.get('worker_source_sha256')!=OLD_POSITIVE_WORKER
            or p.get('input_manifest_sha256')!=OLD_POSITIVE_MANIFEST):
            raise ValueError('the actual completed original positive process is required')
        if not successful(q,43597921732) or digest(rp)!=REPAIR_PROCESS:
            raise ValueError('the exact original complete repair-source process is required')
        inputs=dict(
            body=self.exact_native(positive,'repaired-complete-positive-N97-high-inverse.json.gz',p,OLD_BODY),
            repaired_outer=self.exact_native(positive,'repaired-complete-regular-Hs-outer.json.gz',p,OLD_OUTER),
            repair_source=self.exact_native(repair,'complete-known-response-centre-repair-source.json.gz',q,OLD_REPAIR))
        for key in ('old_outer','endpoint','direction'):
            inputs[key]=self.science/self.manifest['input_paths'][key]
        small(self.evidence/'original-native-restoration-receipt.json',dict(complete=True,
            original_positive_run=43601149891,original_repair_run=43597921732,
            original_process_sha256=dict(positive=digest(pp),repair=digest(rp)),
            inputs={k:dict(sha256=digest(v),bytes=v.stat().st_size) for k,v in inputs.items()},
            all_original_completed_mathematics_recomputed=0))
        self.state['original_native_restoration_verified']=True
        return inputs

    def outcome(self,path):
        if not path.exists():return
        native=read(path)
        out=dict(native_sha256=digest(path),native_bytes=path.stat().st_size,
            complete=native.get('complete'),failure=native.get('failure'),
            gates=native.get('gates',[]),complete_original_rows=native.get('complete_original_rows'),
            actual_orders=[dict(order=o.get('homogeneous_angular_order'),complete=o.get('complete'),
                failure=o.get('failure'),bounds=o.get('bounds',{})) for o in native.get('orders',[])])
        small(self.evidence/(path.name.removesuffix('.json.gz')+'-actual-outcome.json'),out)

    def execute(self,label,command):
        try:return super().execute(label,command)
        finally:
            if self.active_native:self.outcome(self.active_native)
            if self.active_native and self.active_native.exists() and read(self.active_native).get('failure'):
                if self.log.exists():print(self.log.read_text()[-16000:],flush=True)

    def reuse(self,name,producer,input_sha,label):
        root=REPO/FOLDER
        if not root.exists():return None
        for pp in sorted(root.glob('*/process.json')):
            p=read(pp)
            if (p.get('repository')!='Rogerhu12/math-research-public'
                or not any(c.get('label')==label and c.get('actual_returncode')==0 for c in p.get('children',[]))):
                continue
            rows=[x for x in p.get('native_files',[]) if x.get('logical_file')=='native/'+name]
            if len(rows)!=1 or not isinstance(rows[0].get('sha256'),str):continue
            path=self.exact_native(pp.parent,name,p,rows[0]['sha256']);doc=read(path)
            if (not doc.get('complete') or doc.get('failure')
                or doc.get('source_sha256')!=self.manifest['files'][producer]
                or doc.get('input_sha256')!=input_sha
                or not doc.get('gates') or not all(g['passed'] for g in doc['gates'])):continue
            target=self.cache/name;shutil.copyfile(path,target)
            small(self.evidence/(name.removesuffix('.json.gz')+'-exact-reuse.json'),dict(
                original_run_id=p['run_id'],original_process_sha256=digest(pp),
                native_sha256=digest(target),actual_original_child_returncode=0,
                complete_source_and_input_sha256_verified=True,new_mathematical_execution=False))
            self.state.setdefault('reused_complete_native',{})[name]=dict(
                original_run_id=p['run_id'],sha256=digest(target))
            return target
        return None

    def checked_result(self,path,producer,input_sha):
        doc=read(path)
        if (not doc.get('complete') or doc.get('failure')
            or doc.get('source_sha256')!=self.manifest['files'][producer]
            or doc.get('input_sha256')!=input_sha or not doc.get('gates')
            or not all(x['passed'] for x in doc['gates'])):
            raise ValueError('the actual complete new transfer did not pass: '+path.name)
        return doc

    def prepare(self):
        inputs=self.original_inputs();self.publish()
        outer_name='full-delta-complete-regular-Hs-outer.json.gz'
        outer_inputs={key:digest(inputs[key.replace('-','_')]) for key in ('old-outer','repaired-outer','endpoint')}
        outer_label='actual_full_real_delta_physical_outer_graph'
        outer=self.reuse(outer_name,OUTER,outer_inputs,outer_label)
        if outer is None:
            outer=self.cache/outer_name;self.active_native=outer
            self.execute(outer_label,[sys.executable,'-u',str(self.science/OUTER),
                '--old-outer',str(inputs['old_outer']),'--repaired-outer',str(inputs['repaired_outer']),
                '--endpoint',str(inputs['endpoint']),'--out',str(outer)])
        o=self.checked_result(outer,OUTER,outer_inputs)
        if (not o.get('full_real_delta_outer_graph_proved')
            or o.get('exact_real_delta_radius')!='1/100000000'
            or o.get('complete_infinite_BVP_inverse_proved')
            or o.get('physical_H7_over6_nonlinear_exterior_graph_claimed')):
            raise ValueError('the actual outer result changed its scope')
        summary=dict(o);summary['native_sha256']=digest(outer)
        small(self.evidence/'full-delta-complete-regular-Hs-outer-summary.json',summary)
        self.state.update(actual_full_delta_outer_complete=True,actual_full_delta_outer_native_sha256=digest(outer))
        self.publish()
        body_name='full-delta-complete-positive-N97-high-inverse.json.gz'
        body_inputs=dict(body=digest(inputs['body']),**{'repair-source':digest(inputs['repair_source']),
            'direction':digest(inputs['direction']),'outer':digest(outer)})
        body_label='actual_full_real_delta_4650_positive_rows_and_both_high_orders'
        body=self.reuse(body_name,BODY,body_inputs,body_label)
        if body is None:
            body=self.cache/body_name;self.active_native=body
            self.execute(body_label,[sys.executable,'-u',str(self.science/BODY),
                '--body',str(inputs['body']),'--repair-source',str(inputs['repair_source']),
                '--direction',str(inputs['direction']),'--outer',str(outer),
                '--outer-source-sha',self.manifest['files'][OUTER],'--out',str(body)])
        d=self.checked_result(body,BODY,body_inputs)
        if (not d.get('full_delta_positive_high_inverse_proved')
            or d.get('exact_real_delta_radius')!='1/100000000'
            or d.get('complete_original_rows')!=4650 or len(d.get('inflated_rows',[]))!=4650
            or d.get('complete_original_raw_response_envelope_rows')!=7721
            or [x.get('homogeneous_angular_order') for x in d.get('orders',[])]!=[0,1]
            or any(not x.get('complete') or x.get('failure') for x in d['orders'])
            or d.get('original_right_interfaces_preserved')!=3594
            or d.get('complete_low_to_high_source_shell')!=288
            or d.get('original_4650_coefficient_rows_recomputed')!=0
            or d.get('original7721_target_or_response_rows_recomputed')!=0
            or d.get('complete_positive_finite_head_inverse_proved')
            or d.get('complete_infinite_BVP_inverse_proved') or d.get('true_parameter_Schur_proved')):
            raise ValueError('the actual full delta positive result is incomplete or exceeds scope')
        summary={k:v for k,v in d.items() if k not in ('inflated_rows','orders')}
        summary['orders']=[{k:v for k,v in row.items() if k!='complete_rows'} for row in d['orders']]
        summary['native_sha256']=digest(body)
        small(self.evidence/'full-delta-complete-positive-N97-high-inverse-summary.json',summary)
        self.state.update(complete=True,complete_native_sha256=digest(body),
            actual_full_delta_positive_closed_rows=4650,actual_unbounded_high_orders=[0,1],
            all_original_right_interfaces_retained=3594,
            order_feedback={str(x['homogeneous_angular_order']):x['bounds']['total_feedback'] for x in d['orders']},
            complete_unknown_high_not_truncated=True,full_head_mean_and_all_affine_source_ports_retained=True)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--mode',choices=('hydrate','run'),required=True)
    for name in ('manifest','rules'):p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    for name in ('work','artifact-dir','positive-artifact','repair-artifact'):p.add_argument('--'+name,type=Path)
    p.add_argument('--compute-minutes',type=int,default=40)
    p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    if a.mode=='hydrate':hydrate(a);return
    if any(getattr(a,k) is None for k in ('work','artifact_dir','positive_artifact','repair_artifact')):
        p.error('the exact two original artifacts and owned work/output paths are required')
    a.kind='full-real-delta-positive';a.mode='prepare';a.first=0;a.end=0
    a.recovery_manifest=None;a.recovery_sha=None
    worker=FullDeltaPositiveWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()

if __name__=='__main__':main()
