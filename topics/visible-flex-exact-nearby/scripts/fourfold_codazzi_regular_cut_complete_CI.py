#!/usr/bin/env python3
"""Public disjoint completion of the original 5970 projector cells.

Preparation verifies and slices unchanged full-frame files, reuses the
four actual successful pilot cells, and verifies both true weighted
boundaries.  Matrix workers never repeat those pilot cells.  The final
consumer requires the exact full cover before declaring local estimates
complete; no global Green or infinite inverse is inferred from coverage.
"""
from __future__ import annotations
import argparse,copy,hashlib,json,shutil,signal,sys
from fractions import Fraction
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC,save

PROPOSAL='6dbc3acfcfbdd051c83344561f13102d30f20699db1e0046357d0ede1ec79639'
MESH='f94fd64f8faff800dfe67ea6689905b87acde06964d10eb667629d5c8cd25a75'
VALIDATOR='998e4112f4ee79706f43b9ac550fcb15023e0899999fa8516c7cec07c3a7ff97'
MODEL='b30eb7299d5803856712134947f3d7899961cc3ab7597ce961b9bf0cf5205183'
PILOT={
 0:'5e8ed96c4be24de926f935c0366c53b17ea05f40a19d5b5332a4e9300fa243a9',
 76:'26a9dae9bfe1bbf0d3aab306612db7d985cebeeecad06e48716fe0d1fcd98a54',
 3300:'ffd2b2755481d0c7c71cfd12aa41f94f85fd57c16ab8fad27cb5f775d6384cbe',
 5969:'d51f3f1aa0bf8ac7af555de349f52c9b0fecb6e5beec67a90fbe81a9a8c7424e'}
ALGEBRA='e0f83a7592374b9ec51af1c852b6d40c12fc1e08443d82b37a7ca9fc8327d6c8'


def plan():
    result=[]
    for i,first in enumerate(range(0,5970,384)):
        end=min(first+384,5970);ranges=[];start=first
        for skip in sorted(x for x in PILOT if first<=x<end):
            if start<skip:ranges.append([start,skip])
            start=skip+1
        if start<end:ranges.append([start,end])
        result.append(dict(slice_id=i,original_group=[first,end],new_ranges=ranges,
            reused_pilot_indices=[x for x in sorted(PILOT) if first<=x<end],
            new_cells=sum(b-a for a,b in ranges)))
    return result


def actual_success(process,run_id,manifest=None):
    return (str(process.get('run_id'))==str(run_id) and process.get('complete')
        and not process.get('failure') and process.get('repository')=='Rogerhu12/math-research-public'
        and (manifest is None or process.get('input_manifest_sha256')==manifest)
        and all(row.get('actual_returncode')==0 for row in process.get('children',[])))


def validated(path,first,end):
    document=read(path);ident=document['identity']
    if (document.get('kind')!='actual_complete_weighted_cut_local_projector_validation_v1'
        or not document.get('selected_cells_complete') or document.get('failure')
        or ident.get('source_sha256')!=VALIDATOR or ident.get('interval_model_source_sha256')!=MODEL
        or ident.get('selected_indices')!=[first,end]
        or ident.get('input_sha256',{}).get('proposal')!=PROPOSAL
        or ident.get('exact_weight_mesh_sha256')!=MESH
        or ident.get('full_state_dimension')!=193 or ident.get('regular_dimension')!=96
        or ident.get('polynomial_degree')!=24 or ident.get('arithmetic_bits')!=256
        or ident.get('parameter_offset')!='0'
        or document.get('global_continuous_Green_criterion_proved')
        or len(document.get('rows',[]))!=end-first
        or [row.get('index') for row in document['rows']]!=list(range(first,end))
        or not all(row.get('complete_continuous_local_projector_estimates')
                   and row.get('every_endpoint_projector_jump_paid')
                   and row.get('all_193_rows_96_columns_mean_and_radial_weight_derivative_retained')
                   for row in document['rows'])):
        raise ValueError('a complete original continuous projector range changed or failed')
    return document


def same_science(document):
    result=copy.deepcopy(document['identity']);result.pop('selected_indices')
    return result


class CompleteWorker(ReviewedBodyWorker):
    def __init__(self,args):
        super().__init__(args)
        suffix=f'prepare' if args.phase=='prepare' else f'slice-{args.slice_id:02d}' if args.phase=='range' else 'complete-5970-consumer'
        self.name=f'run-{self.run_label}-projectors-{suffix}'
        self.dest=TOPIC/'notes/regular_cut_validator_ci'/self.name
        self.state.update(kind='actual_public_complete_cut_projector_disjoint_process_v1',
            worker_source_sha256=digest(__file__),phase=args.phase,
            slice_id=args.slice_id if args.phase=='range' else None,
            original_complete_frame_run=43588509643,original_successful_pilot_run=43591378059,
            original_proposal_cells_recomputed=0,successful_pilot_cells_recomputed=0,
            exact_affine_parameter_offset='0',whole_original_parameter_half_width=None,
            physical_parameter='fixed original physical eta0',
            complete_original_5970_cells_claimed=False,global_continuous_inverse_proved=False,
            complete_infinite_inverse_proved=False,true_parameter_Schur_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='complete_original_5970_cut_projector_disjoint_inputs_v1':
            raise ValueError('the complete original disjoint projector manifest is required')
        if self.manifest.get('disjoint_plan')!=plan():raise ValueError('the immutable mutually exclusive plan changed')

    def pilot(self,root):
        root=Path(root);process=read(root/'process.json')
        if (not actual_success(process,43591378059,
                'f4d98d4e9316b005621b539c538b6e6b49f19e56d450c789c5fc7f99965a2bd3')
            or len(process.get('children',[]))!=5
            or process.get('selected_actual_cells_completed')!=sorted(PILOT)):
            raise ValueError('the real successful original four-cell pilot is required')
        algebra=root/'native/complete-public-algebra-gates.json.gz'
        if digest(algebra)!=ALGEBRA:raise ValueError('the actual original public algebra native changed')
        gates=read(algebra)
        if not gates.get('complete') or len(gates.get('gates',[]))!=7 or not all(x['passed'] for x in gates['gates']):
            raise ValueError('the actual complete seven public algebra gates are required')
        files=[];science=None
        for i,expected in PILOT.items():
            path=root/f'native/validated-cell-{i:05d}-{i+1:05d}.json.gz'
            if digest(path)!=expected:raise ValueError('an original successful pilot cell changed')
            document=validated(path,i,i+1);current=same_science(document)
            if science is None:science=current
            if current!=science:raise ValueError('the successful original pilot identities differ')
            files.append(path)
        return files,science

    def prepare_frames(self):
        prior=self.args.prior_artifact.resolve();process=read(prior/'process.json')
        proposal=prior/'native/complete-cut-proposal.json.gz'
        if (not actual_success(process,43588509643,
             'f8c27873466b88ce7b1d0497d1baeaaa6682ae6ebfa2840fb3c80d9baf3e0e2f')
            or not process.get('children') or digest(proposal)!=PROPOSAL
            or process.get('complete_native_sha256')!=PROPOSAL):
            raise ValueError('the actual full original frame proposal is required')
        original=read(proposal);rows=original['rows'];chunks=original['complete_frame_chunks']
        if not original.get('complete') or len(rows)!=5970 or original.get('exact_covered_interval')!=['0','9/10']:
            raise ValueError('the full original frame radial domain changed')
        mesh=prior/'frames/exact-weight-and-base-mesh.json'
        if digest(mesh)!=MESH:raise ValueError('the original exact continuous weight changed')
        for row in chunks:
            file=Path(row['file'])
            if file.name!=str(file) or digest(prior/'frames'/file)!=row['sha256']:
                raise ValueError('a complete original frame chunk changed before slicing')
        pilot_files,science=self.pilot(self.args.pilot_artifact)
        for path in pilot_files:shutil.copyfile(path,self.cache/path.name)
        shutil.copyfile(self.args.pilot_artifact/'process.json',self.evidence/'original-successful-pilot-process.json')
        shutil.copyfile(self.args.pilot_artifact/'native/complete-public-algebra-gates.json.gz',
                        self.cache/'complete-public-algebra-gates.json.gz')
        shutil.copyfile(prior/'process.json',self.evidence/'original-complete-frame-process.json')
        shutil.copyfile(proposal,self.cache/'complete-original-cut-proposal.json.gz')
        boundary=self.cache/'complete-true-weighted-boundaries.json.gz'
        command=[sys.executable,'-u',str(self.science_topic/'scripts/fourfold_codazzi_regular_cut_true_weighted_boundaries.py'),
            '--proposal',str(proposal),'--frames',str(prior/'frames'),
            '--cut',str(self.science/self.manifest['proposal_inputs']['cut-native']),
            '--cap-cut',str(self.args.cap_cut_artifact/'native/complete-cap-and-true-moving-cut-native.json.gz'),
            '--cap-cut-process',str(self.args.cap_cut_artifact/'process.json'),'--out',str(boundary)]
        self.execute('actual_all97_weighted_cut_and_all96_waist_boundaries',command)
        bounds=read(boundary)
        if not bounds.get('complete') or bounds.get('failure') or not all(x['passed'] for x in bounds['gates']):
            raise ValueError('the actual complete true weighted boundary consumer failed')
        packages=[];root=self.args.slices.resolve();root.mkdir(parents=True,exist_ok=True)
        for item in plan():
            path=root/f'slice-{item["slice_id"]:02d}';(path/'native').mkdir(parents=True,exist_ok=False)
            (path/'frames').mkdir()
            shutil.copyfile(proposal,path/'native/complete-cut-proposal.json.gz')
            shutil.copyfile(mesh,path/'frames/exact-weight-and-base-mesh.json')
            shutil.copyfile(prior/'process.json',path/'original-complete-frame-process.json')
            selected=[row for row in chunks if any(row['first_cell']<end and first<row['end_cell']
                                                   for first,end in item['new_ranges'])]
            for row in selected:shutil.copyfile(prior/'frames'/row['file'],path/'frames'/row['file'])
            files={str(file.relative_to(path)):dict(sha256=digest(file),bytes=file.stat().st_size)
                   for file in sorted(path.rglob('*')) if file.is_file()}
            package=dict(kind='unchanged_complete_frame_slice_for_disjoint_projector_validation_v1',
                current_public_workflow_run=str(self.state['run_id']),plan=item,
                original_complete_proposal_sha256=PROPOSAL,original_complete_weight_mesh_sha256=MESH,
                original_complete_frame_chunks=selected,files=files,
                source_input_manifest_sha256=self.args.manifest_sha,
                no_original_frame_value_or_order_changed=True)
            save(path/'slice-manifest.json',package)
            packages.append(dict(plan=item,slice_manifest_sha256=digest(path/'slice-manifest.json'),
                                 original_frame_files=len(selected),bytes=sum(x['bytes'] for x in files.values())))
        save(self.evidence/'exact-disjoint-frame-slices.json',dict(complete=True,packages=packages,
             original_cells=5970,reused_successful_pilot_indices=sorted(PILOT),new_cells=5966,
             original_frame_arrays_recomputed=0,successful_pilot_cells_recomputed=0))
        save(self.evidence/'complete-true-weighted-boundaries-summary.json',dict(
             complete=True,native_sha256=digest(boundary),actual_bounds=bounds))
        self.state.update(complete=True,prepared_frame_slices=len(packages),reused_actual_pilot_cells=4,
            new_requested_cells=5966,complete_weighted_boundaries_verified=True,
            weighted_boundary_native_sha256=digest(boundary),full_validator_scientific_identity=science)

    def run_range(self):
        item=plan()[self.args.slice_id];root=self.args.frame_slice.resolve()
        package=read(root/'slice-manifest.json')
        if (package.get('kind')!='unchanged_complete_frame_slice_for_disjoint_projector_validation_v1'
            or package.get('current_public_workflow_run')!=str(self.state['run_id'])
            or package.get('plan')!=item or package.get('source_input_manifest_sha256')!=self.args.manifest_sha
            or package.get('original_complete_proposal_sha256')!=PROPOSAL
            or package.get('original_complete_weight_mesh_sha256')!=MESH
            or not package.get('no_original_frame_value_or_order_changed')):
            raise ValueError('the immutable same-workflow original frame slice changed')
        for name,record in package['files'].items():
            path=Path(name)
            if path.is_absolute() or '..' in path.parts or digest(root/path)!=record['sha256']:
                raise ValueError('a sliced original complete input changed')
        if digest(root/'native/complete-cut-proposal.json.gz')!=PROPOSAL:
            raise ValueError('the complete original frame proposal changed')
        self.state.update(disjoint_plan=item,successful_new_ranges=[],
            assigned_new_cells=item['new_cells'],original_slice_manifest_sha256=digest(root/'slice-manifest.json'))
        for first,end in item['new_ranges']:
            if any(first<=x<end for x in PILOT):raise ValueError('a successful original pilot cell would be repeated')
            native=self.cache/f'validated-cells-{first:05d}-{end:05d}.json.gz'
            command=[sys.executable,'-u',str(self.science_topic/'scripts/fourfold_codazzi_regular_cut_projector_validator.py')]
            for key in ('candidate','object','repair-report'):
                command+=['--'+key,str(self.science/self.manifest['proposal_inputs'][key])]
            command+=['--proposal',str(root/'native/complete-cut-proposal.json.gz'),
                '--frames',str(root/'frames'),'--first',str(first),'--end',str(end),
                '--degree','24','--bits','256','--max-new-cells',str(end-first),'--out',str(native)]
            self.execute(f'actual_complete_continuous_projector_cells_{first}_{end}',command)
            document=validated(native,first,end)
            record=dict(first=first,end=end,native_sha256=digest(native),actual_cells=len(document['rows']))
            self.state['successful_new_ranges'].append(record)
            save(self.evidence/f'complete-range-{first:05d}-{end:05d}.json',record)
            self.publish()
        self.state.update(complete=True,assigned_original_ranges_complete=True,
            actual_new_continuous_cells=item['new_cells'])

    def finish(self):
        prepared=self.args.prepared_artifact.resolve();process=read(prepared/'process.json')
        if (not actual_success(process,self.state['run_id'],self.args.manifest_sha)
            or process.get('phase')!='prepare' or process.get('prepared_frame_slices')!=16
            or not process.get('complete_weighted_boundaries_verified')):
            raise ValueError('the actual same-workflow complete preparation failed')
        boundary=prepared/'native/complete-true-weighted-boundaries.json.gz'
        bounds=read(boundary)
        if digest(boundary)!=process['weighted_boundary_native_sha256'] or not bounds.get('complete') or bounds.get('failure'):
            raise ValueError('the original actual true weighted boundary outcome changed')
        proposal=prepared/'native/complete-original-cut-proposal.json.gz'
        if digest(proposal)!=PROPOSAL:raise ValueError('the complete original proposal changed')
        original=read(proposal);rows={};inputs=[];science=None
        def add(path,first,end,expected=None):
            nonlocal science
            if expected is not None and digest(path)!=expected:raise ValueError('an original successful pilot native changed')
            document=validated(path,first,end);current=same_science(document)
            if science is None:science=current
            if current!=science:raise ValueError('complete projector pieces use different mathematical objects')
            for row in document['rows']:
                i=row['index'];source=original['rows'][i]
                if i in rows:raise ValueError('a complete projector cell would be counted twice')
                if row['interval']!=source['interval'] or row['original_candidate_piece']!=source['original_candidate_piece']:
                    raise ValueError('an original complete interval or physical piece changed')
                rows[i]=row
            inputs.append(dict(file=path.name,sha256=digest(path),selected_indices=[first,end]))
        for i,expected in PILOT.items():add(prepared/f'native/validated-cell-{i:05d}-{i+1:05d}.json.gz',i,i+1,expected)
        found={}
        for path in self.args.completed_artifacts.resolve().glob('*/process.json'):
            child=read(path)
            if child.get('phase')!='range':continue
            sid=child.get('slice_id')
            if sid in found or not isinstance(sid,int) or not 0<=sid<16:
                raise ValueError('a complete original worker slice is missing or duplicated')
            if (not actual_success(child,self.state['run_id'],self.args.manifest_sha)
                or child.get('disjoint_plan')!=plan()[sid]
                or not child.get('assigned_original_ranges_complete')):
                raise ValueError('an actual original disjoint matrix worker did not finish')
            found[sid]=path
            for first,end in plan()[sid]['new_ranges']:
                add(path.parent/f'native/validated-cells-{first:05d}-{end:05d}.json.gz',first,end)
        if sorted(found)!=list(range(16)) or sorted(rows)!=list(range(5970)):
            raise ValueError('the actual full 5970-cell cover is incomplete')
        ordered=[rows[i] for i in range(5970)];edge=Fraction(9,10)
        previous=None
        for row in ordered:
            left,right=map(Fraction,row['interval'])
            if right!=edge or not left<right:raise ValueError('the complete actual radial cover has a gap or overlap')
            if previous is not None and previous['exact_left_anchor_array_sha256']!=row['exact_right_anchor_array_sha256']:
                raise ValueError('two independently stored original chunks disagree at a complete interface')
            edge=left
            previous=row
        if edge!=0:raise ValueError('the full continuous projector domain did not reach the waist')
        if (ordered[0]['exact_right_anchor_array_sha256']!=bounds['exact_cut_anchor_array_sha256']
            or ordered[-1]['exact_left_anchor_array_sha256']!=bounds['exact_waist_anchor_array_sha256']):
            raise ValueError('the verified true boundaries and the local polynomial anchors differ')
        # Keep every original full reference definition in its already
        # published input native.  The complete scalar profile stores all
        # Green data plus exact hashes to those original complete rows.
        keys=('index','interval','original_candidate_piece','original_frame_chunk',
            'original_frame_chunk_sha256','exact_right_anchor_array_sha256','exact_left_anchor_array_sha256',
            'whole_polynomial_smallest_singular_lower','whole_polynomial_Gram_lower',
            'generator_uniform_true_operator_error','full_normal_projector_defect_e',
            'complete_forward_signed_rate_mu','complete_backward_signed_rate_nu',
            'complete_cross_c','complete_left_interface_projector_jump',
            'all_193_rows_96_columns_mean_and_radial_weight_derivative_retained',
            'every_endpoint_projector_jump_paid','complete_continuous_local_projector_estimates')
        profile=[]
        for row in ordered:
            entry={key:row[key] for key in keys}
            definition=row['exact_new_reference_definition']
            entry['exact_weight']={key:definition['exact_weight'][key]
                for key in ('exact_rho_left','exact_rho_right','exact_rho_derivative')}
            entry['complete_original_row_canonical_json_sha256']=hashlib.sha256(
                (json.dumps(row,sort_keys=True,separators=(',',':'))+'\n').encode()).hexdigest()
            entry['complete_reference_definition_retained_in_its_original_native']=True
            profile.append(entry)
        native=self.cache/'complete-5970-local-projectors.json.gz'
        save(native,dict(kind='actual_complete_5970_local_projector_cover_and_all_interfaces_v1',
            complete=True,failure=None,consumer_source_sha256=digest(__file__),
            actual_public_run_id=str(self.state['run_id']),complete_scientific_identity=science,
            original_complete_proposal_sha256=PROPOSAL,original_successful_pilot_run=43591378059,
            exact_interval=['0','9/10'],complete_original_cells=5970,
            reused_original_successful_pilot_cells=4,new_original_cells=5966,inputs=inputs,rows=profile,
            all_original_exact_reference_coefficients_retained_in_the_input_natives=True,
            all_complete_193_by_96_continuous_Gram_mean_rates_and_defects_consumed=True,
            all_5970_projector_jumps_including_virtual_waist_jump_retained=True,
            complete_true_weighted_boundary_native_sha256=digest(boundary),
            continuous_global_Green_criterion_proved=False,unknown_high_input_feedback_paid=False,
            true_response_error_proved=False,true_parameter_Schur_proved=False))
        shutil.copyfile(boundary,self.cache/boundary.name)
        save(self.evidence/'complete-5970-cover-summary.json',dict(complete=True,complete_original_cells=5970,
            exact_interval=['0','9/10'],native_sha256=digest(native),original_sources=inputs,
            complete_true_weighted_boundary_native_sha256=digest(boundary),
            all_original_cells_and_all_interfaces_consumed_exactly_once=True,
            continuous_global_Green_criterion_still_required=True))
        self.state.update(complete=True,complete_original_5970_cells_claimed=True,
            complete_native_sha256=digest(native),actual_complete_local_cells=5970,
            weighted_boundary_native_sha256=digest(boundary))

    def prepare(self):
        if self.args.phase=='prepare':self.prepare_frames()
        elif self.args.phase=='range':self.run_range()
        else:self.finish()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','work','artifact-dir'):p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    for name in ('prior-artifact','pilot-artifact','cap-cut-artifact','slices','frame-slice','prepared-artifact','completed-artifacts'):
        p.add_argument('--'+name,type=Path)
    p.add_argument('--phase',choices=('prepare','range','finish'),required=True)
    p.add_argument('--slice-id',type=int,default=-1)
    p.add_argument('--compute-minutes',type=int,default=170)
    p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    required={'prepare':('prior_artifact','pilot_artifact','cap_cut_artifact','slices'),
        'range':('frame_slice',),'finish':('prepared_artifact','completed_artifacts')}[a.phase]
    if any(getattr(a,key) is None for key in required) or (a.phase=='range' and not 0<=a.slice_id<16):
        raise ValueError('all explicitly selected phase inputs and a valid disjoint range are required')
    a.kind='cut-projector-complete';a.mode='prepare';a.first=0;a.end=0
    a.recovery_manifest=None;a.recovery_sha=None
    worker=CompleteWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
