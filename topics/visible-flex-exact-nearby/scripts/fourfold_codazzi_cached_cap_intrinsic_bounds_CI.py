#!/usr/bin/env python3
"""Restore the four original native byte parts and publish new cap maxima."""
from __future__ import annotations
import argparse,json,shutil,signal,subprocess,sys
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC,REPO
from fourfold_native_lossless_parts import restore

PUBLIC='Rogerhu12/math-research-public'
REL=Path('topics/visible-flex-exact-nearby')
PRODUCER=REL/'scripts/fourfold_codazzi_cached_cap_intrinsic_bounds.py'
FOLDER='cached_cap_intrinsic_ci'
KIND='actual_cached_complete_cap_intrinsic_beta_gamma_K_maxima_v1'
NATIVE='complete-cap-cached-intrinsic-beta-gamma-K.json.gz'
ORIGINAL_SPLIT=REL/'notes/2026-11-14-R133-current-positive-complete-ac1-binary-parts.json'
ORIGINAL_SOURCE=REL/'scripts/fourfold_codazzi_current_positive_complete_coefficients.py'
OBJECT=REL/'data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'
JOINT_FOLDER=REL/'notes/cap_Z_joint_coefficient_ci/run-43674204314-1-complete-cap-Z-joint-coefficients'
JOINT_SUMMARY=JOINT_FOLDER/'evidence/complete-cap-Z-joint-summary.json'
JOINT_PROCESS=JOINT_FOLDER/'process.json'
SOURCE_SHA='b0e930d6ba184b4f5d13966e3bba723c101102b751876fd070ec19136a5260af'
EXPECTED=dict(
    native='ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d',
    split_manifest='32b430a27a20726f095098902afdb93e656ea746eb81bce09a559e6f65787fd3',
    original_source='1292a1c06695d49a6f5e6bca27ad375b2fd82b44ebe1e6066327b7b7a79d882c',
    object='91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848',
    joint_summary='67fa3c6664ab90a1dbbc91960b10f4f75c8f6372fee272ddca8f780f834efb86',
    joint_process='61896c151fcd7593076195e0d320713f829a087cb9e3b597bbbd61b0c650ae61')

def small(path,value):
    raw=(json.dumps(value,indent=2,allow_nan=False)+'\n').encode()
    if len(raw)>60000:raise ValueError('the genuine intrinsic summary exceeds60000 UTF8 bytes')
    Path(path).parent.mkdir(parents=True,exist_ok=True);Path(path).write_bytes(raw)

def identity():
    return dict(EXPECTED,exact_cap_interval=['9/10','25/8'],
        exact_eta='-7789843107295549/4611686018427387904',
        original_parameter_half_width='1/1000000000',
        original_exact_nu='-2572625729470897/72057594037927936',
        original_candidate='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413',
        original_intrinsic_cap_cache='3a89805ebe1ab22000529a7a8c2fdc262b1c3a2afbc52433cf610d2d6542ff22',
        complete_Z_definition='6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04')

def hydrate(a):
    if digest(a.manifest)!=a.manifest_sha or digest(a.rules)!=a.rules_sha:
        raise ValueError('the exact intrinsic manifest or reviewed rules changed')
    m=read(a.manifest)
    paths=set(m['files'])|set(m['readme_sha256'])|{
        str(a.manifest.relative_to(REPO)),str(a.rules.relative_to(REPO)),
        str(REL/'scripts/'),str(REL/'notes'/FOLDER)}
    subprocess.run(['git','-c','safe.directory='+str(REPO),'sparse-checkout','set','--no-cone','--stdin'],
        cwd=REPO,input='\n'.join('/'+p for p in sorted(paths))+'\n',text=True,check=True)
    print(json.dumps(dict(complete_pinned_paths=len(paths),
        original_four_native_parts_only=True,original_mathematics_not_executed=True)),flush=True)

class CapIntrinsicWorker(ReviewedBodyWorker):
    def __init__(self,args):
        super().__init__(args)
        self.name=f'run-{self.run_label}-complete-cap-cached-intrinsic'
        self.dest=TOPIC/'notes'/FOLDER/self.name
        self.state.update(kind='actual_public_cached_complete_cap_intrinsic_process',
            worker_source_sha256=digest(__file__),
            original_intrinsic_target_ODE_FFT_and_repair_recomputations=0,
            original_Bernstein_joint_rows_recomputed=0,already_complete_joint_cells_reused=660,
            complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False)
        self.state.pop('whole_original_parameter_half_width',None)
        self.state.pop('original_ac1_operator_not_relabelled_as_repaired',None)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest['files'][str(PRODUCER)]!=SOURCE_SHA:
            raise ValueError('the new intrinsic mathematical source changed')
        if self.manifest['exact_scientific_inputs']!=EXPECTED:
            raise ValueError('the original complete native or joint receipt identity differs')

    def original_inputs(self):
        manifest=self.science/ORIGINAL_SPLIT
        if digest(manifest)!=EXPECTED['split_manifest']:
            raise ValueError('the original four-part restoration manifest changed')
        m=read(manifest)
        if (len(m.get('parts',[]))!=4 or m.get('original_sha256')!=EXPECTED['native']
            or m.get('original_bytes')!=6223338 or not m.get('native_complete')
            or m.get('complete_native_rows')!=4650):
            raise ValueError('the original complete intrinsic native has another scope')
        original=self.artifact/'original-native'/'current-positive-complete-ac1-native.json.gz'
        restored=restore(manifest,original)
        if digest(original)!=EXPECTED['native'] or original.stat().st_size!=6223338:
            raise ValueError('the restored exact original complete container changed')
        small(self.evidence/'original-four-part-native-restoration.json',
            dict(original_native_sha256=digest(original),original_bytes=original.stat().st_size,
                original_parts_manifest_sha256=digest(manifest),original_parts=restored['parts'],
                original_numerical_producer_executed=False,
                old_intrinsic_target_or_grid_recomputed=False,new_byte_parts_created=False))
        return original

    def previous(self):
        candidates=[]
        for pp in sorted((TOPIC/'notes'/FOLDER).glob('*/process.json')):
            if pp==self.dest/'process.json':continue
            p=read(pp)
            if (p.get('kind')!=self.state['kind'] or p.get('repository')!=PUBLIC
                or p.get('worker_source_sha256')!=digest(__file__)
                or p.get('input_manifest_sha256')!=self.args.manifest_sha):continue
            entries=[r for r in p.get('native_files',[]) if r.get('logical_file')=='native/'+NATIVE]
            if not entries:continue
            if len(entries)!=1:raise ValueError('one original intrinsic native receipt is ambiguous')
            entry=entries[0]
            if entry.get('file'):path=pp.parent/entry['file']
            else:
                path=self.work/('restored-'+entry['sha256']+'.json.gz')
                restore(pp.parent/entry['lossless_manifest'],path)
            if not path.exists() or digest(path)!=entry['sha256'] or path.stat().st_size!=entry['bytes']:
                raise ValueError('restore the missing original intrinsic prefix without recomputing it')
            d=read(path)
            if (d.get('kind')!=KIND or d.get('source_sha256')!=SOURCE_SHA
                or d.get('input_sha256')!=identity()):continue
            if d.get('failure'):
                raise ValueError('preserve the actual failed mathematics; do not repeat without a correction')
            rows=d.get('completed_cap_rows',-1)
            if rows<0 or rows!=len(d.get('rows',[])):
                raise ValueError('the original completed intrinsic row count differs')
            child0=any(c.get('label')=='complete_cap_intrinsic_maxima_from_original_closed_rows'
                and c.get('actual_returncode')==0 for c in p.get('children',[]))
            reused=p.get('original_complete_success_reused_without_child') and p.get('original_success_process_sha256')
            complete=bool(d.get('complete') and len(d.get('gates',[]))==9
                and all(g['passed'] for g in d['gates']) and (child0 or reused))
            candidates.append(((int(complete),rows),pp,path,complete))
        return max(candidates,key=lambda item:item[0]) if candidates else None

    def summary(self,d):
        return {k:d.get(k) for k in (
            'kind','source_sha256','complete','failure','gates','seconds','input_sha256',
            'exact_interval','original_complete_row_count','selected_cap_row_count','completed_cap_rows',
            'reused_cap_rows','new_cap_rows_this_child','complete_cap_intrinsic_constants',
            'original_full_native_sha256','original_native_bytes','original_four_lossless_parts_only',
            'old_target_ODE_FFT_and_repair_recomputations','completed_new_Bernstein_joint_cells',
            'already_complete_joint_cells_reused','original_joint_summary_sha256',
            'original_joint_native_sha256','same_intrinsic_cap_v2_complete_rows',
            'scoped_to_original_fixed_eta0','whole_original_eta_half_width_also_covers_eta0',
            'no_new_target_or_intrinsic_coefficient_enclosure_created',
            'no_new_nonlinear_solution_or_infinite_inverse_claimed')}

    def snapshot(self):
        path=self.cache/NATIVE
        if path.exists():
            d=read(path);s=self.summary(d);s['native_sha256']=digest(path)
            small(self.evidence/'actual-latest-cap-intrinsic-summary.json',s)
            self.state.update(actual_completed_cap_rows=d.get('completed_cap_rows'),
                latest_scientific_native_sha256=digest(path))
        super().snapshot()

    def prepare(self):
        old=self.previous();native=self.cache/NATIVE;resume=None;complete=False
        if old:
            _,pp,path,complete=old
            original_processes=self.artifact/'original-processes';original_processes.mkdir(exist_ok=True)
            shutil.copyfile(pp,original_processes/'process.json')
            small(self.evidence/'original-cap-intrinsic-prefix-reuse.json',
                dict(original_process_sha256=digest(pp),original_native_sha256=digest(path),
                    original_process_complete=read(pp).get('complete'),original_math_complete=complete,
                    original_completed_cap_rows=read(path)['completed_cap_rows'],
                    original_complete_math_reused_independently_of_publication=True))
            if complete:
                shutil.copyfile(path,native)
                self.state.update(original_complete_success_reused_without_child=True,
                    original_success_process_sha256=digest(pp))
            else:
                resume=self.work/'accepted-original-intrinsic-prefix.json.gz';shutil.copyfile(path,resume)
        if not complete:
            original=self.original_inputs();self.publish()
            command=[sys.executable,'-u',str(self.science/PRODUCER),
                '--native',str(original),'--split-manifest',str(self.science/ORIGINAL_SPLIT),
                '--original-source',str(self.science/ORIGINAL_SOURCE),'--object',str(self.science/OBJECT),
                '--joint-summary',str(self.science/JOINT_SUMMARY),
                '--joint-process',str(self.science/JOINT_PROCESS),'--out',str(native)]
            if resume:command+=['--resume',str(resume)]
            self.execute('complete_cap_intrinsic_maxima_from_original_closed_rows',command)
        d=read(native)
        if (d.get('kind')!=KIND or d.get('source_sha256')!=SOURCE_SHA
            or d.get('input_sha256')!=identity() or not d.get('complete') or d.get('failure')
            or len(d.get('gates',[]))!=9 or not all(g['passed'] for g in d['gates'])
            or d['completed_cap_rows']!=d['selected_cap_row_count']
            or d['old_target_ODE_FFT_and_repair_recomputations']!=0
            or d['completed_new_Bernstein_joint_cells']!=0
            or d['already_complete_joint_cells_reused']!=660
            or not d['no_new_nonlinear_solution_or_infinite_inverse_claimed']):
            raise ValueError('the actual complete intrinsic bounds did not pass their exact scope')
        summary=self.summary(d);summary.update(native_sha256=digest(native),
            original_complete_success_reused_without_child=complete)
        small(self.evidence/'complete-cap-intrinsic-summary.json',summary)
        self.state.update(complete=True,complete_native_sha256=digest(native),
            actual_completed_cap_rows=d['completed_cap_rows'],
            actual_scientific_gates=len(d['gates']),
            actual_new_cap_rows_this_child=0 if complete else d['new_cap_rows_this_child'],
            original_complete_success_reused_without_child=complete,
            complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--mode',choices=('hydrate','prepare'),required=True)
    for name in ('manifest','rules'):p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--work',type=Path);p.add_argument('--artifact-dir',type=Path)
    p.add_argument('--compute-minutes',type=int,default=20)
    p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='cached-cap-intrinsic';a.first=0;a.end=4650;a.recovery_manifest=None;a.recovery_sha=None
    if a.mode=='hydrate':hydrate(a);return
    if a.work is None or a.artifact_dir is None:p.error('actual work and artifact directories are required')
    worker=CapIntrinsicWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):
        signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()

if __name__=='__main__':main()
