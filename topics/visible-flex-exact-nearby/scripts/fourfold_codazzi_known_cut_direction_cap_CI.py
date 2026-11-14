#!/usr/bin/env python3
"""Compute new known-cut cap directions from byte-identical saved matrices."""
from __future__ import annotations
import argparse,shutil,signal,sys
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_cap128_CI_worker import digest,read,link_exact
from fourfold_codazzi_phase_high7_CI_worker import TOPIC,save
from fourfold_native_lossless_parts import restore

REL='topics/visible-flex-exact-nearby/'
PREPARED='0d417ea1da798b8d268fe17eccfb25884e98cf6de71aaaa0b261dfae0faafa70'
OLD_MANIFEST='867699a5e7f968f97d9a3f50267e310181023fdbe0b815a7f9c22c6b21585e32'
CAP='69f55939742b26988690e54b7f5636eb591a351063b93187feeb38c1f6611ebe'
CAP_CUT='36f498e3b0addbb46290c12fae6b63af7673db20ba230e22dd83809d18427104'
BOUNDARY='b1adeea522b31efa2fc83a6436bc3fe52dbd04630c17d5436927b5872b05e263'
BOUNDARY_PROCESS='d81f87fb08dde8d1a8501cf4ac2dc71b71f08c542fc39870c0ac8cb0f13f57c7'
PRODUCER=REL+'scripts/fourfold_codazzi_known_cut_direction_cap_pilot.py'
NATIVE='known-cut-direction-complete-cap-mixed-source-pilot.json.gz'
LABEL='actual_new_one_column_cap_sources_for_the_full_known_even_cut_direction'


class KnownCutDirectionWorker(ReviewedBodyWorker):
    def __init__(self,args):
        super().__init__(args)
        self.name=f'run-{self.run_label}-known-cut-direction-cap-pilot'
        self.dest=TOPIC/'notes/known_cut_direction_ci'/self.name
        self.state.update(kind='actual_public_known_cut_direction_cap_mixed_source_pilot_process_v1',
            worker_source_sha256=digest(__file__),original_prepared_cap_run=43580498603,
            original_complete_cap_run=43583838015,original_complete_cap_cut_run=43587619797,
            original_complete_known_boundary_source_run=43599771405,
            original_large_matrix_reconstructions_executed=0,
            old_complete_matrix_residual_cells_recomputed=0,
            original_1977_operator_certificate_unchanged=True,
            only_actual_known_source_direction_improved_if_new_enclosures_allow=True,
            full_boundary_operator_improvement_claimed=False,
            complete_finite193_response_error_proved=False,complete_infinite_inverse_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='actual_known_cut_direction_cap_mixed_source_pilot_public_inputs_v1':
            raise ValueError('the separate exact known-cut direction manifest is required')

    def best_prefix(self,expected_inputs):
        root=TOPIC/'notes/known_cut_direction_ci';candidates=[]
        if not root.exists():return None
        for path in sorted(root.glob('*/process.json')):
            process=read(path)
            if (process.get('repository')!='Rogerhu12/math-research-public'
                or process.get('worker_source_sha256')!=digest(__file__)
                or process.get('input_manifest_sha256')!=self.args.manifest_sha
                or process.get('actual_scientific_input_sha256')!=expected_inputs):continue
            records=[x for x in process.get('native_files',[]) if x.get('logical_file')=='native/'+NATIVE]
            if len(records)!=1:continue
            item=records[0];native=path.parent/'native'/NATIVE
            if not native.exists():
                if 'lossless_manifest' not in item:continue
                native=self.work/('known-cut-prefix-'+item['sha256']+'.json.gz')
                if not native.exists():restore(path.parent/item['lossless_manifest'],native)
            if digest(native)!=item['sha256']:raise ValueError('a true original one-column prefix changed')
            doc=read(native);rows=doc.get('new_one_column_rows',[])
            if (doc.get('source_sha256')!=self.manifest['files'][PRODUCER]
                or doc.get('input_sha256')!=expected_inputs or not rows
                or not all(x.get('actual_complete_one_column_cell') for x in rows)):continue
            if doc.get('complete') and not any(c.get('label')==LABEL and c.get('actual_returncode')==0
                for c in process.get('children',[])):continue
            candidates.append((len(rows),path,native,doc))
        return max(candidates,key=lambda x:x[0]) if candidates else None

    def restore_exact_prepared_arrays(self):
        prepared=self.args.prepared.resolve();bundle_path=prepared/'prepared-manifest.json'
        bundle=read(bundle_path)
        if (digest(bundle_path)!=PREPARED
            or bundle.get('kind')!='exact_same_cap128_moving97_CI_bundle' or not bundle.get('complete')
            or bundle.get('input_manifest_sha256')!=OLD_MANIFEST
            or not bundle.get('every_regenerated_array_matches_historical_bytes')):
            raise ValueError('the original actually successful exact prepared cap bundle is required')
        for relative,item in bundle['files'].items():
            path=prepared/relative
            if path.stat().st_size!=item['bytes'] or digest(path)!=item['sha256']:
                raise ValueError('a complete original cap array or candidate shard changed')
        proposal=self.science/self.manifest['precomposed_descriptor'];old=read(proposal)
        if (digest(proposal)!=bundle['precomposed_descriptor_sha256']
            or old['work_directory']!=bundle['canonical_directory']):
            raise ValueError('the original same-array cap descriptor changed')
        link_exact(old['work_directory'],prepared/bundle['array_directory'])
        for path,expected in old['full_matrix_inputs'].items():
            if digest(path)!=expected:raise ValueError('a canonical scientific array link changed bytes')
        candidate=prepared/bundle['candidate']
        if digest(candidate)!=self.manifest['candidate_sha256']:
            raise ValueError('the complete original prepared candidate changed')
        shutil.copyfile(bundle_path,self.evidence/'original-prepared-manifest.json')
        self.state.update(original_prepared_bundle_sha256=PREPARED,
            all_original_large_array_bytes_verified=True,large_matrix_reconstructions_executed=0)
        return candidate,proposal

    def prepare(self):
        candidate,proposal=self.restore_exact_prepared_arrays()
        inputs=dict(candidate=candidate,proposal=proposal)
        for label,key in (('object','object_input'),('repair-report','repair_input'),
            ('inlet','inlet_input'),('q-vector','q_vector_input'),('q-native','q_native_input'),
            ('hessian','hessian_input'),('cut','cut_input')):
            inputs[label]=self.science/self.manifest[key]
        originals={
            'cap':(self.args.cap_artifact,'native/complete-cap-native.json.gz',CAP,43583838015),
            'cap-cut':(self.args.cap_cut_artifact,'native/complete-cap-and-true-moving-cut-native.json.gz',
                CAP_CUT,43587619797),
            'boundary':(self.args.boundary_artifact,'native/known-waist-and-true-cap-sources.json.gz',
                BOUNDARY,43599771405)}
        for label,(root,relative,expected,run) in originals.items():
            root=root.resolve();process_path=root/'process.json';process=read(process_path);native=root/relative
            if (digest(native)!=expected or str(process.get('run_id'))!=str(run)
                or process.get('repository')!='Rogerhu12/math-research-public' or not process.get('complete')
                or process.get('failure') or process.get('complete_native_sha256')!=expected
                or not process.get('children') or any(c.get('actual_returncode')!=0 for c in process['children'])):
                raise ValueError('the actual successful original '+label+' artifact is required')
            if label=='boundary' and digest(process_path)!=BOUNDARY_PROCESS:
                raise ValueError('the original boundary artifact process receipt changed')
            inputs[label]=native;inputs[label+'-process']=process_path
            shutil.copyfile(process_path,self.evidence/('original-'+label+'-artifact-process.json'))
        expected_inputs={key:digest(value) for key,value in inputs.items()}
        self.state['actual_scientific_input_sha256']=expected_inputs
        self.state['requested_new_one_column_cells']=self.manifest['selected_new_one_column_cells']
        self.publish()
        native=self.cache/NATIVE;prior=self.best_prefix(expected_inputs)
        command=[sys.executable,'-u',str(self.science/PRODUCER),
            '--count',str(self.manifest['selected_new_one_column_cells']),'--out',str(native)]
        for key,value in inputs.items():command.extend(['--'+key,str(value)])
        if prior:
            count,process,old,doc=prior
            shutil.copyfile(process,self.evidence/'original-known-cut-direction-prefix-process.json')
            self.state.update(original_completed_one_column_cells_reused=count,
                original_same_direction_prefix_native_sha256=digest(old),
                actual_prior_failure_preserved=doc.get('failure'))
            if doc.get('complete') and not doc.get('failure'):
                shutil.copyfile(old,native);self.state['actual_new_direction_child_executed']=False
            else:
                command.extend(['--resume',str(old)])
                self.execute(LABEL,command);self.state['actual_new_direction_child_executed']=True
        else:
            self.execute(LABEL,command);self.state['actual_new_direction_child_executed']=True
        result=read(native)
        if (not result.get('complete') or result.get('failure') or not result.get('selected_cells_complete')
            or result.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or result.get('input_sha256')!=expected_inputs
            or not result.get('complete_actual_known_cut_load_bound_proved')
            or result.get('full_boundary_operator_or_weighted_kernel_improvement_claimed')
            or result.get('complete_finite193_response_error_proved')
            or result.get('complete_infinite_inverse_proved')
            or not all(x['passed'] for x in result['gates'])):
            raise ValueError('the actual directional cap source outcome failed or exceeded its scope')
        summary={k:v for k,v in result.items() if k not in ('new_one_column_rows','complete_mixed_cell_bounds','direction')}
        summary['direction']={k:v for k,v in result['direction'].items()
            if k not in ('exact_binary64_w0_hex','original_even_trace_intervals')}
        summary['new_one_column_rows']=[{k:v for k,v in row.items()
            if k in ('index','interval','matrix_piece','accumulator_terms','actual_seconds',
                'original_complete_cap_row_sha256','full_resolved_support','scalar_remainder')}
            for row in result['new_one_column_rows']]
        summary['native_sha256']=digest(native)
        save(self.evidence/'known-cut-direction-complete-cap-pilot-summary.json',summary)
        self.state.update(complete=True,complete_native_sha256=digest(native),
            actual_new_selected_one_column_cells=len(result['new_one_column_rows']),
            complete_mixed_cover_cells=len(result['complete_mixed_cell_bounds']),
            complete_known_true_cut_source_bounds=result['complete_true_known_cut_source_bounds'],
            complete_known_moving_direction_cap_error=result['complete_actual_even_direction_moving_cap_error'],
            actual_directional_gates=len(result['gates']))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','prepared','cap-artifact','cap-cut-artifact','boundary-artifact','work','artifact-dir'):
        p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--compute-minutes',type=int,default=40);p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='known-cut-direction';a.mode='prepare';a.first=0;a.end=1977
    a.recovery_manifest=None;a.recovery_sha=None
    worker=KnownCutDirectionWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
