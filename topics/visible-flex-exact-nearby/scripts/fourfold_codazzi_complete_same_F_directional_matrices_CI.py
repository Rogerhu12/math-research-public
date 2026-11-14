#!/usr/bin/env python3
"""Public disjoint same-F matrix completion with exact successful reuse."""
from __future__ import annotations
import argparse,json,shutil,signal,sys
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_finite193_L2_Green_kernel_CI import KernelWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC

REL='topics/visible-flex-exact-nearby/'
PRODUCER=REL+'scripts/fourfold_codazzi_complete_same_F_directional_matrices.py'
FOLDER='notes/complete_same_F_directional_matrices_ci'
KIND='actual_complete_same_F_directional_matrix_data_from_cached5970_v1'
PLAN_KIND='actual_exact5970_same_F_directional_matrix_disjoint_plan_v1'
PLAN='complete-exact5970-same-F-disjoint-plan.json.gz'
FULL='complete5970-same-F-directional-matrix-data.json.gz'
PROFILE_NAME='complete-5970-local-projectors.json.gz'
PROFILE='3460a4b5636bf6a3d9c160f6141ab5153fc5fc705ca79000c5f10370a978cb69'
PROFILE_PROCESS='16608b57571d17a427857bcfe0127186589b3f79e93d89a7e423ac48a2740af9'
PILOT_NAME='complete-four-same-F-triangular-source-Grams.json.gz'
PILOT='9a46d9fc76499a17a90a0a153a0c4907415eadcedfd9f50f70fd82d08f9dbc7c'
PILOT_SOURCE='2173281e0558cbbabf3a21d506ae3cf9b0253a9406aa2d9d15b8681e8faeaf44'
PILOT_WORKER='98ca04e2a5e0691f9e9f319d16700f8884da6eea27f3eb61eb832d3107b19f38'
PILOT_MANIFEST='a24a9a7fec2f39e349e9f547ea4d5c33f72db10d41e3a77ed7030409161e7ad9'
INDICES=[0,76,3300,5969]
LABELS=dict(plan='exact_full5970_matrix_plan_and_four_original_same_F_receipts',
    range='new_missing_canonical_same_F_matrices_and_complete_directional_Grams',
    finish='exact_all5970_same_F_matrix_cover_without_original_cell_recomputation')


def small(path,document):
    raw=(json.dumps(document,ensure_ascii=False,indent=2)+'\n').encode()
    if len(raw)>60000:raise ValueError('one complete-matrix plaintext evidence exceeds60000 bytes')
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(raw)


def name_for(phase,group):
    return PLAN if phase=='plan' else FULL if phase=='finish' else f'complete-same-F-range-{group:02d}.json.gz'


def receipts(row):
    result=[row['array_receipt']]
    for key in ('left_frame_array_receipt','right_frame_array_receipt'):
        if key in row:result.append(row[key])
    return result


class MatrixWorker(ReviewedBodyWorker):
    exact_native=KernelWorker.exact_native

    def __init__(self,a):
        super().__init__(a)
        suffix='plan' if a.phase=='plan' else 'finish' if a.phase=='finish' else f'range-{a.group:02d}'
        self.name=f'run-{self.run_label}-complete-same-F-{suffix}'
        self.dest=TOPIC/FOLDER/self.name;self.reused_complete=False
        self.native_name=name_for(a.phase,a.group)
        self.state.update(kind='actual_public_complete_same_F_directional_matrix_process_v1',
            worker_source_sha256=digest(__file__),phase=a.phase,
            group=a.group if a.phase=='range' else None,
            original_projector_run=43594139132,original_same_F_pilot_run=43648579604,
            original_successful_F_or_Gram_cells_recomputed=0,original_target_or_validator_calls=0,
            all_original_Q_and_R_endpoint_bytes_required=True,
            full_two_boundary_directional_Green_proved=False,
            complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='complete5970_same_F_directional_matrix_data_public_inputs_v1':
            raise ValueError('the exact full5970 directional matrix input manifest is required')

    def successful_math(self,p,d,phase):
        if (not d.get('complete') or d.get('failure') or not d.get('gates')
            or not all(g.get('passed') for g in d['gates'])):return False
        child=any(c.get('label')==LABELS[phase] and c.get('actual_returncode')==0
                  for c in p.get('children',[]))
        reused=(p.get('original_complete_success_reused_without_child')
                and p.get('original_success_process_sha256'))
        return bool(child or reused)

    def profile_inputs(self,root,prepared=False):
        pp=root/('evidence/original-complete-projector-process.json' if prepared else 'process.json')
        p=read(pp)
        if (digest(pp)!=PROFILE_PROCESS or p.get('repository')!='Rogerhu12/math-research-public'
            or str(p.get('run_id'))!='43594139132' or p.get('complete_native_sha256')!=PROFILE):
            raise ValueError('the exact original successful complete projector artifact process changed')
        if prepared:
            path=root/'native'/PROFILE_NAME
            if digest(path)!=PROFILE:raise ValueError('the prepared original full5970 profile changed')
        else:path=self.exact_native(root,'native/'+PROFILE_NAME,p,PROFILE)
        d=read(path)
        if not d.get('complete') or d.get('failure') or len(d.get('rows',[]))!=5970:
            raise ValueError('the exact original complete5970 profile is not complete')
        return path,pp

    def pilot_inputs(self,root):
        pp=root/'process.json';p=read(pp)
        if (p.get('repository')!='Rogerhu12/math-research-public'
            or str(p.get('run_id'))!='43648579604' or str(p.get('run_attempt'))!='1'
            or p.get('worker_source_sha256')!=PILOT_WORKER
            or p.get('input_manifest_sha256')!=PILOT_MANIFEST
            or p.get('complete_native_sha256')!=PILOT
            or not any(c.get('label')=='same_forward_F_triangular_endpoints_and_three_complete128_source_Grams'
                and c.get('actual_returncode')==0 for c in p.get('children',[]))):
            raise ValueError('the four actual same-F scientific successes are required')
        path=self.exact_native(root,'native/'+PILOT_NAME,p,PILOT);d=read(path)
        if (not d.get('complete') or d.get('failure') or d.get('identity',{}).get('source_sha256')!=PILOT_SOURCE
            or [r.get('index') for r in d.get('rows',[])]!=INDICES
            or len(d.get('gates',[]))!=15 or not all(g['passed'] for g in d['gates'])):
            raise ValueError('the complete original same-F native or15 gates changed')
        availability=[]
        for row in d['rows']:
            r=row['array_receipt'];file=root/'matrices'/r['file']
            if (Path(r['file']).name!=r['file'] or not file.exists()
                or file.stat().st_size!=r['bytes'] or digest(file)!=r['sha256']
                or r['sha256']!=self.manifest['original_same_F_array_sha256'][str(row['index'])]):
                raise ValueError('an actual old successful same-F scientific array is absent or changed')
            availability.append(dict(index=row['index'],file=r['file'],bytes=r['bytes'],sha256=r['sha256'],
                original_public_array_origin=r['original_public_array_origin']))
        small(self.evidence/'four-actual-original-same-F-array-availability.json',dict(
            original_native_sha256=PILOT,arrays=availability,zero_original_matrix_recomputation=True))
        shutil.copyfile(pp,self.evidence/'original-same-F-artifact-process.json')
        return path,pp

    def previous(self,phase,group,plan_sha):
        candidates=[];root=TOPIC/FOLDER
        if not root.exists():return None
        for pp in sorted(root.glob('*/process.json')):
            p=read(pp)
            if (p.get('repository')!='Rogerhu12/math-research-public'
                or p.get('worker_source_sha256')!=digest(__file__)
                or p.get('input_manifest_sha256')!=self.args.manifest_sha
                or p.get('phase')!=phase or p.get('group')!=(group if phase=='range' else None)):
                continue
            if phase!='plan' and p.get('exact_plan_native_sha256')!=plan_sha:continue
            records=[r for r in p.get('native_files',[]) if r.get('logical_file')=='native/'+self.native_name]
            if len(records)!=1:continue
            path=self.exact_native(pp.parent,'native/'+self.native_name,p,records[0]['sha256'])
            d=read(path)
            source=d.get('source_sha256') if phase in ('plan','finish') else d.get('identity',{}).get('source_sha256')
            if source!=self.manifest['files'][PRODUCER]:continue
            if phase=='plan':
                if d.get('kind')!=PLAN_KIND or d.get('original_profile_sha256')!=PROFILE:continue
                count=0
            elif phase=='range':
                ident=d.get('identity',{})
                if (d.get('kind')!=KIND or d.get('phase')!='range'
                    or ident.get('exact_plan_native_sha256')!=plan_sha
                    or ident.get('group',{}).get('group')!=group):continue
                rows=d.get('rows',[]);requested=ident['group']['exact_new_indices']
                if [r.get('index') for r in rows]!=requested[:len(rows)] or any(not r.get('complete') for r in rows):
                    raise ValueError('a same-identity completed matrix prefix is not consecutive')
                count=len(rows)
            else:
                if d.get('kind')!=KIND or d.get('phase')!='finish' or d.get('exact_plan_native_sha256')!=plan_sha:continue
                count=len(d.get('rows',[]))
            complete=self.successful_math(p,d,phase)
            if phase!='range' and not complete:continue
            candidates.append(((1 if complete else 0,count),pp,path,complete))
        return max(candidates,key=lambda x:x[0]) if candidates else None

    def copy_previous(self,previous,native,command,phase):
        if not previous:return command
        _,pp,path,complete=previous
        shutil.copyfile(pp,self.evidence/'original-same-identity-process.json')
        small(self.evidence/'original-matrix-success-or-prefix-reuse.json',dict(
            original_process_sha256=digest(pp),original_native_sha256=digest(path),
            original_process_complete=read(pp).get('complete'),actual_science_complete=complete,
            original_failure_preserved=read(pp).get('failure'),
            successful_math_does_not_require_successful_publication=True,
            all_array_bytes_keep_their_original_run_attempt_artifact_origins=True))
        if complete:
            shutil.copyfile(path,native);self.reused_complete=True
            self.state['original_success_process_sha256']=digest(pp)
        elif phase=='range':
            prefix=self.work/'original-completed-matrix-prefix.json.gz'
            shutil.copyfile(path,prefix);command+=['--resume',str(prefix)]
        else:raise ValueError('only a range can consume a noncomplete scientific prefix')
        return command

    def brief(self,d):
        rows=d.get('rows',[])
        return dict(complete=d.get('complete'),failure=d.get('failure'),phase=self.args.phase,
            group=self.args.group if self.args.phase=='range' else None,
            gates=d.get('gates',[]),completed_matrix_cells=len(rows),
            completed_indices=[r['index'] for r in rows] if self.args.phase=='range' else None,
            actual_new_matrix_cells=d.get('actual_new_matrix_cells',d.get('new_matrix_cells_this_child')),
            reused_completed_matrix_cells=d.get('reused_completed_matrix_cells'),
            complete_local_matrix_cells=d.get('complete_local_matrix_cells'),
            actual_complete_local_matrix_cells=d.get('actual_complete_local_matrix_cells'),
            full_two_boundary_directional_Green_proved=False,
            complete_infinite_BVP_inverse_proved=False,
            original_target_or_validator_calls=0,original_successful_F_Gram_cells_recomputed=0)

    def execute(self,label,command):
        try:return super().execute(label,command)
        finally:
            path=self.cache/self.native_name
            if path.exists():
                d=read(path);summary=self.brief(d);summary['native_sha256']=digest(path)
                small(self.evidence/'actual-latest-matrix-outcome.json',summary)
                print(json.dumps(dict(phase=self.args.phase,group=self.args.group,
                    complete=d.get('complete'),failure=d.get('failure'),
                    completed_cells=len(d.get('rows',[])),native_sha256=digest(path))),flush=True)
                if d.get('failure') and self.log.exists():print(self.log.read_text()[-16000:],flush=True)

    def origin_inventory(self,rows):
        inventory={}
        for row in rows:
            for r in receipts(row):
                origin=r['original_public_array_origin']
                current=(str(origin['run_id'])==str(self.state['run_id'])
                    and str(origin['run_attempt'])==str(self.state['run_attempt']))
                if current:
                    path=self.artifact/'matrices'/r['file']
                    if (not path.exists() or path.stat().st_size!=r['bytes'] or digest(path)!=r['sha256']):
                        raise ValueError('a newly completed original scientific matrix file is missing or changed')
                key=(origin['run_id'],origin['run_attempt'],origin['artifact'],r['file'],r['sha256'])
                inventory[key]=dict(file=r['file'],bytes=r['bytes'],sha256=r['sha256'],
                    original_public_array_origin=origin,available_in_this_artifact=current)
        values=list(inventory.values())
        for j,first in enumerate(range(0,len(values),64)):
            small(self.evidence/f'scientific-array-origin-inventory-{j:03d}.json',dict(
                first=first,end=min(first+64,len(values)),complete_unique_files=len(values),
                exact_original_array_receipts=values[first:first+64],
                unavailable_here_means_original_artifact_reuse_not_recomputation=True))
        return len(values)

    def plan_inputs(self):
        root=self.args.prepared_artifact.resolve();pp=root/'process.json';p=read(pp)
        if (p.get('repository')!='Rogerhu12/math-research-public'
            or p.get('worker_source_sha256')!=digest(__file__)
            or p.get('input_manifest_sha256')!=self.args.manifest_sha or p.get('phase')!='plan'):
            raise ValueError('the exact completed public matrix preparation is required')
        entries=[r for r in p.get('native_files',[]) if r.get('logical_file')=='native/'+PLAN]
        if len(entries)!=1:raise ValueError('the plan needs its explicit logical native SHA receipt')
        path=self.exact_native(root,'native/'+PLAN,p,entries[0]['sha256']);d=read(path)
        if (d.get('kind')!=PLAN_KIND or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or not self.successful_math(p,d,'plan')):
            raise ValueError('the completed plan mathematics lacks true child0 or an exact reuse receipt')
        self.state['exact_plan_native_sha256']=digest(path)
        profile,profile_pp=self.profile_inputs(root,prepared=True)
        return path,profile,profile_pp

    def prepare(self):
        phase=self.args.phase;native=self.cache/self.native_name
        command=[sys.executable,'-u',str(self.science/PRODUCER),'--phase',phase,'--bits','256','--out',str(native)]
        plan_sha=None
        if phase=='plan':
            profile,profile_pp=self.profile_inputs(self.args.projector_artifact.resolve())
            pilot,pilot_pp=self.pilot_inputs(self.args.pilot_artifact.resolve())
            reviewed=self.science/self.manifest['original_same_F_reviewed_process']
            command+=['--pilot',str(pilot),'--pilot-process',str(pilot_pp),
                '--reviewed-pilot-process',str(reviewed)]
            shutil.copyfile(profile,self.cache/PROFILE_NAME)
            shutil.copyfile(profile_pp,self.evidence/'original-complete-projector-process.json')
        else:
            plan,profile,profile_pp=self.plan_inputs();plan_sha=digest(plan)
            command+=['--plan',str(plan)]
            if phase=='range':
                group=read(plan)['groups'][self.args.group]
                self.state['exact_requested_group']=group
                command+=['--group',str(self.args.group),'--reference-artifact',str(self.args.reference_artifact.resolve()),
                    '--frame-slice',str(self.args.frame_slice.resolve()),'--arrays',str(self.artifact/'matrices')]
            else:
                pilot,pilot_pp=self.pilot_inputs(self.args.pilot_artifact.resolve())
                reviewed=self.science/self.manifest['original_same_F_reviewed_process']
                command+=['--pilot',str(pilot),'--pilot-process',str(pilot_pp),
                    '--reviewed-pilot-process',str(reviewed)]
                found={}
                for pp in self.args.completed_artifacts.resolve().glob('*/process.json'):
                    p=read(pp);g=p.get('group')
                    if p.get('phase')!='range':continue
                    if (str(p.get('run_id'))!=str(self.state['run_id'])
                        or str(p.get('run_attempt'))!=str(self.state['run_attempt'])):continue
                    if (p.get('repository')!='Rogerhu12/math-research-public'
                        or p.get('worker_source_sha256')!=digest(__file__)
                        or p.get('input_manifest_sha256')!=self.args.manifest_sha
                        or p.get('exact_plan_native_sha256')!=plan_sha
                        or not isinstance(g,int) or not 0<=g<32 or g in found):
                        raise ValueError('a completed range artifact process has a different identity or duplicate group')
                    logical='native/'+name_for('range',g)
                    entries=[r for r in p.get('native_files',[]) if r.get('logical_file')==logical]
                    if len(entries)!=1:raise ValueError('a completed range needs one explicit logical native receipt')
                    path=self.exact_native(pp.parent,logical,p,entries[0]['sha256']);d=read(path)
                    if not self.successful_math(p,d,'range'):
                        raise ValueError('one actual full matrix range lacks scientific success')
                    found[g]=(path,pp)
                if set(found)!=set(range(32)):raise ValueError('all32 actual matrix range processes are required')
                self.state['range_process_input_kind']='actual_public_repository_snapshots_for_this_run_and_attempt'
                self.state['large_matrix_arrays_not_downloaded_for_cover_only_finish']=True
                for g in range(32):
                    path,pp=found[g];command+=['--range-native',str(path)]
                    shutil.copyfile(pp,self.evidence/f'original-complete-range-{g:02d}-process.json')
        command+=['--profile',str(profile),'--profile-process',str(profile_pp)]
        previous=self.previous(phase,self.args.group,plan_sha)
        command=self.copy_previous(previous,native,command,phase)
        self.publish()
        if not self.reused_complete:self.execute(LABELS[phase],command)
        d=read(native)
        if not d.get('complete') or d.get('failure') or not d.get('gates') or not all(g['passed'] for g in d['gates']):
            raise ValueError('the actual complete matrix phase did not finish scientifically')
        source=d.get('source_sha256') if phase in ('plan','finish') else d.get('identity',{}).get('source_sha256')
        if source!=self.manifest['files'][PRODUCER]:raise ValueError('the actual complete matrix source identity changed')
        summary=self.brief(d);summary.update(native_sha256=digest(native),seconds=d.get('seconds'),
            original_complete_success_reused_without_child=self.reused_complete,
            actual_new_matrix_cells_this_child=0 if self.reused_complete else d.get('actual_new_matrix_cells',0),
            full_native_and_all_matrix_origin_receipts_retained=True)
        if phase=='plan':
            self.state['exact_plan_native_sha256']=digest(native)
            summary.update(new_local_cells=d['new_local_cells'],reused_complete_pilot_cells=d['reused_complete_pilot_cells'],
                complete_groups=len(d['groups']),all_shared_original_Q_and_R_endpoints_verified=True)
        elif phase=='range':
            count=self.origin_inventory(d['rows']);summary['complete_scientific_array_origin_files']=count
            hist={}
            for row in d['rows']:
                degree=str(row['canonical_forward_inverse_recurrence_certificate']['degree'])
                hist[degree]=hist.get(degree,0)+1
            summary['actual_canonical_degree_histogram']=hist
            selected=[d['rows'][0],d['rows'][-1]] if len(d['rows'])>1 else d['rows']
            small(self.evidence/'selected-actual-matrix-row-budgets.json',dict(
                exact_native_sha256=digest(native),rows=[dict(index=r['index'],interval=r['interval'],
                    patch=r['patch']['complete_exact_endpoint_patch_upper'],
                    true_generator_error=r['patch']['true_complete_generator_difference_upper'],
                    inverse_fee=r['inverse_polynomial_certificate']['complete_true_patched_F_inverse_minus_C'],
                    source_Gram_traces={k:v['complete_trace_upper'] for k,v in r['source_Grams'].items()},
                    output_Gram_traces={k:v.get('complete_trace_upper',{'exact_zero':True}) for k,v in r['output_Grams'].items()},
                    array_sha256=r['array_receipt']['sha256']) for r in selected]))
        else:
            summary.update(reused_successful_pilot_cells=4,complete_new_canonical_matrix_cells=5966,
                actual_complete_local_matrix_cells=5970,
                interface_coordinate_maps_V_rounding_and_true_boundary_defects_still_required=True)
        small(self.evidence/'complete-'+phase+'-matrix-summary.json',summary)
        self.state.update(complete=True,complete_native_sha256=digest(native),
            actual_scientific_gates=len(d['gates']),actual_complete_local_matrix_cells=summary.get('actual_complete_local_matrix_cells'),
            actual_new_matrix_cells_this_child=summary.get('actual_new_matrix_cells_this_child',0),
            complete_local_matrix_cells=d.get('complete_local_matrix_cells'),
            original_complete_success_reused_without_child=self.reused_complete,
            all_matrix_array_bytes_remain_only_in_public_Actions_artifacts=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','work','artifact-dir'):p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    for name in ('projector-artifact','pilot-artifact','prepared-artifact','reference-artifact','frame-slice','completed-artifacts'):
        p.add_argument('--'+name,type=Path)
    p.add_argument('--phase',choices=('plan','range','finish'),required=True)
    p.add_argument('--group',type=int,default=-1)
    p.add_argument('--compute-minutes',type=int,default=210)
    p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    required={'plan':('projector_artifact','pilot_artifact'),
        'range':('prepared_artifact','reference_artifact','frame_slice'),
        'finish':('prepared_artifact','pilot_artifact','completed_artifacts')}[a.phase]
    if any(getattr(a,k) is None for k in required) or (a.phase=='range' and not 0<=a.group<32):
        raise ValueError('one exact explicit phase and all its actual inputs are required')
    a.kind='complete-same-F-directional-matrices';a.mode='prepare'
    a.first=a.group*192 if a.phase=='range' else 0
    a.end=min(a.first+192,5970) if a.phase=='range' else 0
    a.recovery_manifest=None;a.recovery_sha=None
    worker=MatrixWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):
        signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
