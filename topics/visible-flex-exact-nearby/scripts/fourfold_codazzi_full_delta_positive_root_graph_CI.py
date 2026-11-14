#!/usr/bin/env python3
"""Consume three actual small receipts and verify the full-delta positive root graph."""
from __future__ import annotations
import argparse,json,shutil,signal,subprocess,sys
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import REPO
from fourfold_native_lossless_parts import restore

REL='topics/visible-flex-exact-nearby/'
SELF=REL+'scripts/fourfold_codazzi_full_delta_positive_root_graph_CI.py'
SOURCE=REL+'scripts/fourfold_codazzi_full_delta_positive_high_root_graph.py'
FOLDER=REL+'notes/full_delta_positive_root_graph_ci/'
LABEL='actual_full_real_delta_seven_column_positive_root_graph'
NAME='full-real-delta-positive-root-high-graph.json.gz'

def small(path,doc):
    raw=(json.dumps(doc,ensure_ascii=False,indent=2)+'\n').encode()
    if len(raw)>60000:raise ValueError('the new plaintext summary exceeds60000 bytes; native evidence retained')
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(raw)

def hydrate(a):
    if digest(a.manifest)!=a.manifest_sha or digest(a.rules)!=a.rules_sha:
        raise ValueError('the exact manifest or separately reviewed rules changed')
    d=read(a.manifest)
    if d['files'].get(SELF)!=digest(__file__):raise ValueError('the separately pinned new worker changed')
    paths=set(d['files'])|{'README.md',REL+'README.md',FOLDER,
        str(a.manifest.relative_to(REPO)),str(a.rules.relative_to(REPO))}
    subprocess.run(['git','-c','safe.directory='+str(REPO),'sparse-checkout','set','--no-cone','--stdin'],
        cwd=REPO,input='\n'.join('/'+p for p in sorted(paths))+'\n',text=True,check=True)
    print(json.dumps(dict(exact_paths=len(paths),large_original_arrays_not_hydrated=True)))

class FullDeltaRootGraphWorker(ReviewedBodyWorker):
    def __init__(self,a):
        super().__init__(a)
        self.name=f'run-{self.run_label}-full-real-delta-positive-root-graph'
        self.dest=REPO/FOLDER/self.name
        self.active_native=None
        self.state.update(kind='actual_public_full_real_delta_positive_root_graph_process_v1',
            worker_source_sha256=digest(__file__),exact_real_delta_radius='1/100000000',
            whole_original_parameter_half_width='1/100000000',
            original_collar_body_outer_target_or_response_mathematics_recomputed=0,
            all_seven_complete_source_and_jump_columns_retained=True,
            complete_low_high_Schur_inverse_proved=False,
            complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='full_real_delta_positive_root_graph_actual_receipts_inputs_v1':
            raise ValueError('the exact new three-receipt input manifest is required')

    def outcome(self,path):
        if not path.exists():return
        d=read(path)
        small(self.evidence/'actual-latest-interface-outcome.json',dict(
            complete=d.get('complete'),failure=d.get('failure'),gates=d.get('gates',[]),
            native_sha256=digest(path),native_bytes=path.stat().st_size))

    def execute(self,label,command):
        try:return super().execute(label,command)
        finally:
            if self.active_native:self.outcome(self.active_native)
            if self.active_native and self.active_native.exists() and read(self.active_native).get('failure'):
                if self.log.exists():print(self.log.read_text()[-16000:],flush=True)

    def checked_result(self,path,inputs):
        d=read(path)
        if (d.get('kind')!='actual_full_real_delta_root_to_regular_given_head_high_graph_v1'
            or not d.get('complete') or d.get('failure')
            or d.get('source_sha256')!=self.manifest['files'][SOURCE]
            or d.get('input_sha256')!=inputs or not d.get('gates')
            or not all(x['passed'] for x in d['gates'])
            or not d.get('given_complete_head_positive_high_inverse_and_root_graph_proved')
            or not d.get('nonzero_delta_M96_family_proved')
            or d.get('exact_real_delta_radius')!='1/100000000'
            or len(d.get('input_order',[]))!=7
            or any(len(row)!=7 for row in d.get('response_rows',{}).values())
            or len(d.get('response_rows',{}))!=7
            or d.get('full_low_high_Schur_inverse_proved')
            or d.get('complete_infinite_BVP_inverse_proved')
            or d.get('true_parameter_Schur_proved') or d.get('order1_exterior_upgrade_proved')):
            raise ValueError('the actual complete seven-column graph failed or changed scope')
        return d

    def reuse(self,inputs):
        root=REPO/FOLDER
        if not root.exists():return None
        for pp in sorted(root.glob('*/process.json')):
            p=read(pp)
            if (p.get('repository')!='Rogerhu12/math-research-public'
                or not any(c.get('label')==LABEL and c.get('actual_returncode')==0
                    for c in p.get('children',[]))):continue
            entries=[r for r in p.get('native_files',[]) if r.get('logical_file')=='native/'+NAME]
            if len(entries)!=1:continue
            e=entries[0];path=pp.parent/'native'/NAME
            if not path.exists():
                if 'lossless_manifest' not in e:continue
                path=self.work/('restored-'+e['sha256']+'.json.gz')
                if not path.exists():restore(pp.parent/e['lossless_manifest'],path)
            if digest(path)!=e['sha256'] or path.stat().st_size!=e['bytes']:
                raise ValueError('an actual prior native changed')
            d=read(path)
            if d.get('source_sha256')!=self.manifest['files'][SOURCE] or d.get('input_sha256')!=inputs:continue
            self.checked_result(path,inputs)
            target=self.cache/NAME;shutil.copyfile(path,target)
            small(self.evidence/'exact-complete-interface-reuse.json',dict(
                original_run_id=p['run_id'],original_process_sha256=digest(pp),
                actual_original_child_returncode=0,native_sha256=digest(target),
                original_complete_new_interface_mathematics_recomputed=False))
            self.state['reused_original_complete_interface_run_id']=p['run_id']
            return target
        return None

    def prepare(self):
        paths={name:self.science/relative for name,relative in self.manifest['input_paths'].items()}
        inputs={name:digest(path) for name,path in paths.items()}
        self.state['actual_original_small_input_sha256']=inputs
        self.publish()
        path=self.reuse(inputs)
        if path is None:
            path=self.cache/NAME;self.active_native=path
            command=[sys.executable,'-u',str(self.science/SOURCE)]
            for name,p in paths.items():command+=['--'+name,str(p)]
            self.execute(LABEL,command+['--out',str(path)])
        d=self.checked_result(path,inputs)
        summary=dict(d);summary.update(native_sha256=digest(path),native_bytes=path.stat().st_size)
        small(self.evidence/'full-real-delta-positive-root-high-graph-summary.json',summary)
        self.state.update(complete=True,complete_native_sha256=digest(path),
            actual_scientific_gates=len(d['gates']),actual_complete_source_columns=7,
            interface_loop_upper=d['constants']['interface_loop_upper'],
            root_reflection_upper=d['constants']['root_reflection_upper'],
            given_complete_head_positive_high_inverse_and_root_graph_proved=True,
            nonzero_delta_M96_family_proved=True)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--mode',choices=('hydrate','run'),required=True)
    for name in ('manifest','rules'):p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    for name in ('work','artifact-dir'):p.add_argument('--'+name,type=Path)
    p.add_argument('--compute-minutes',type=int,default=30)
    p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    if a.mode=='hydrate':hydrate(a);return
    if a.work is None or a.artifact_dir is None:p.error('owned work and output paths are required')
    a.kind='full-real-delta-positive-root-graph';a.mode='prepare';a.first=0;a.end=0
    a.recovery_manifest=None;a.recovery_sha=None
    worker=FullDeltaRootGraphWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()

if __name__=='__main__':main()
