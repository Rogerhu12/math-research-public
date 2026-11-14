#!/usr/bin/env python3
"""New Fourier-linear source diagnostics and selected fixed-eta subcells."""
from __future__ import annotations
import argparse,shutil,signal,sys
from pathlib import Path
from types import SimpleNamespace
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_body_mean_CI_finish import CompleteMeanWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC,save
from fourfold_native_lossless_parts import restore

REL='topics/visible-flex-exact-nearby/'
OLD_MANIFEST='c214f800a5094c905c554e9053c52567d5ae5d76be41ac2e3fe9d673b396d784'
BODY='a4f31dccc4b54661b43fc06bac59b6afbb4fa2d6d19614f68f71e044be6e5870'
BODY_PROCESS='0a5dc06520bad5a1230b65cba6e895e998e1f3ce6a32a65d9ffa8800b8ea1a9e'
REPAIR='05e0493dbe55490adec8fb6603e0ec431d1bc03f051aec86be8a78741f60f0a4'
REPAIR_PROCESS='16de872ce106e05b6add99d8406598de3cc87b94f4533a9fc3bb46294c66366a'
NATIVE='low193-Fourier-mean-and-fixed-eta-pilot.json.gz'
PRODUCER=REL+'scripts/fourfold_codazzi_low193_Fourier_mean_and_fixed_eta_pilot.py'
LABEL='actual_new_Fourier_mean_source_diagnostics_and_fixed_eta_subcell_jets'


class FourierMeanDiagnosticWorker(ReviewedBodyWorker):
    def __init__(self,args):
        super().__init__(args)
        self.name=f'run-{self.run_label}-low193-Fourier-mean-and-fixed-eta-pilot'
        self.dest=TOPIC/'notes/low193_Fourier_mean_fixed_eta_ci'/self.name
        self.state.update(kind='actual_public_low193_Fourier_mean_and_fixed_eta_diagnostic_process_v1',
            worker_source_sha256=digest(__file__),original_complete_body_run=43583838026,
            original_complete_body_mean_run=43586413510,actual_complete_repair_source_run=43597921732,
            original_full_eta_target_certificates_recomputed=0,new_fixed_eta_target_subcells_requested=True,
            original_mean_flows_recomputed=0,
            original_trial_reconstructions_recomputed=0,complete_body_projection_cover=False,
            exact_affine_parameter_offset='0',physical_parameter='fixed original physical eta0 and nu',
            whole_original_parameter_half_width=None,
            actual_finite193_response_error_bound_proved=False,complete_infinite_inverse_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='low193_Fourier_mean_and_fixed_eta_source_diagnostic_public_inputs_v1':
            raise ValueError('the separate actual cached scalar projection-pilot manifest is required')

    def best_original_prefix(self,expected_inputs):
        root=TOPIC/'notes/low193_Fourier_mean_fixed_eta_ci'
        candidates=[]
        if not root.exists():return None
        for process_path in sorted(root.glob('*/process.json')):
            process=read(process_path)
            if (process.get('repository')!='Rogerhu12/math-research-public'
                or process.get('worker_source_sha256')!=digest(__file__)
                or process.get('input_manifest_sha256')!=self.args.manifest_sha
                or process.get('actual_scientific_input_sha256')!=expected_inputs):continue
            records=[x for x in process.get('native_files',[]) if x.get('logical_file')=='native/'+NATIVE]
            if len(records)!=1:continue
            item=records[0];native=process_path.parent/'native'/NATIVE
            if not native.exists():
                if 'lossless_manifest' not in item:continue
                native=self.work/('original-pilot-prefix-'+item['sha256']+'.json.gz')
                if not native.exists():restore(process_path.parent/item['lossless_manifest'],native)
            if digest(native)!=item['sha256']:raise ValueError('an original actual projected-source prefix changed')
            old=read(native)
            if (old.get('source_sha256')!=self.manifest['files'][PRODUCER]
                or old.get('input_sha256')!=expected_inputs):continue
            complete_rows=old.get('rows',[])
            if not complete_rows or not all(x.get('actual_projection_complete') for x in complete_rows):continue
            if old.get('complete') and not any(c.get('label')==LABEL and c.get('actual_returncode')==0
                for c in process.get('children',[])):continue
            candidates.append((len(complete_rows),process_path,native,old))
        if not candidates:return None
        return max(candidates,key=lambda x:x[0])

    def prepare(self):
        original_path=self.science/self.manifest['original_body_manifest']
        if digest(original_path)!=OLD_MANIFEST:raise ValueError('the original complete body manifest changed')
        original=read(original_path)
        audit_dir=self.evidence/'original-input-audit';audit_dir.mkdir(exist_ok=True)
        audit=SimpleNamespace(
            args=SimpleNamespace(prepared=self.args.prepared,manifest_sha=OLD_MANIFEST,
                original_run=43583838026,original_attempt=1,previous_artifacts=self.args.previous_artifacts),
            manifest=original,science=self.science,science_topic=self.science_topic,evidence=audit_dir,state={})
        # These two existing methods only restore byte-identical original
        # inputs and audit the old complete cover. No scientific row runs.
        CompleteMeanWorker.restore_original_bundle(audit)
        parts=CompleteMeanWorker.original_complete_parts(audit)
        actuals={
            'body':(self.args.body_artifact,'native/complete-correlated-body-and-mean-errors.json.gz',
                BODY,BODY_PROCESS,43586413510),
            'repair-source':(self.args.repair_artifact,'native/complete-known-response-centre-repair-source.json.gz',
                REPAIR,REPAIR_PROCESS,43597921732)}
        resolved={}
        for label,(root,relative,native_sha,process_sha,run_id) in actuals.items():
            root=root.resolve();process=read(root/'process.json');native=root/relative
            if (digest(native)!=native_sha or digest(root/'process.json')!=process_sha
                or str(process.get('run_id'))!=str(run_id) or not process.get('complete')
                or process.get('failure') or process.get('repository')!='Rogerhu12/math-research-public'
                or not process.get('children') or any(c.get('actual_returncode')!=0 for c in process['children'])):
                raise ValueError('the exact actually successful original '+label+' input is required')
            process_name='body-process' if label=='body' else 'repair-process'
            resolved[label]=(native,root/'process.json',process_name)
            shutil.copyfile(root/'process.json',self.evidence/('original-'+process_name+'.json'))
        candidate=self.science/original['published_candidate']
        response=Path(original['row_identity']['full_trials']['response']['path'])
        object_path=self.science/(REL+'data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json')
        expected_inputs={'original-manifest':digest(original_path),'candidate':digest(candidate),
            'response':digest(response),'object':digest(object_path)}
        for label,(path,process,process_name) in resolved.items():
            expected_inputs[label]=digest(path);expected_inputs[process_name]=digest(process)
        self.state['actual_scientific_input_sha256']=expected_inputs
        self.state['all_original_40_parts_and_7721_scalar_rows_verified']=True
        self.publish()
        native=self.cache/NATIVE
        previous=self.best_original_prefix(expected_inputs)
        command=[sys.executable,'-u',str(self.science/PRODUCER),'--original-manifest',str(original_path),
            '--candidate',str(candidate),'--response',str(response),'--object',str(object_path),'--parts',*[str(x) for x in parts],
            '--out',str(native)]
        for label,(path,process,process_name) in resolved.items():
            command.extend(['--'+label,str(path),'--'+process_name,str(process)])
        if previous:
            count,original_process,old,prior=previous
            shutil.copyfile(original_process,self.evidence/'original-projected-source-prefix-process.json')
            self.state.update(original_completed_pilot_rows_reused=count,
                original_pilot_prefix_sha256=digest(old),original_pilot_failure_retained=prior.get('failure'))
            if prior.get('complete') and not prior.get('failure'):
                shutil.copyfile(old,native)
                self.state['actual_new_projection_child_executed']=False
            else:
                command.extend(['--resume',str(old)])
                self.execute(LABEL,command);self.state['actual_new_projection_child_executed']=True
        else:
            self.execute(LABEL,command);self.state['actual_new_projection_child_executed']=True
        result=read(native)
        if (not result.get('complete') or result.get('failure') or not result.get('selected_cells_complete')
            or result.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or result.get('input_sha256')!=expected_inputs
            or result.get('complete_body_projection_cover')
            or result.get('actual_finite193_response_error_bound_proved')
            or result.get('complete_infinite_inverse_proved')
            or not all(x['passed'] for x in result['gates'])):
            raise ValueError('the actual selected projection-pilot result failed or exceeded its scope')
        summary={key:value for key,value in result.items() if key!='rows'}
        def upper(record):return record['upper']
        def compact(cell):
            return dict(interval=cell['interval'],
                repaired_low193_sup=upper(cell['repaired_low193_complete_residual_L2_sup']),
                repaired_low193_radial=upper(cell['repaired_low193_complete_residual_L2_radial']),
                direct_low193_sup=upper(cell['direct_Fourier_low193_polynomial_with_own_remainders']['L2_sup']),
                triangle_low193_sup=upper(cell['independent_separate_low193_triangle_bound']['L2_sup']),
                high97_to160_sup=upper(cell['high97_through160_from_complete_D_alone']['L2_sup']),
                uncorrected_low193_sup=upper(cell['low193_uncorrected_trial_residual']['L2_sup']),
                mean_column_low193_sup=upper(cell['low193_complete_mean_coupling_column']['L2_sup']),
                low_polynomial_own_errors=[upper(x) for x in cell['low_component_uniform_A0_remainders']],
                complete_mean_error=cell['same_original_completed_mean_error'],
                mean_decomposition=cell['mean_decomposition'],
                scalar_models={k:dict(norm=upper(v['polynomial_A0_upper']),error=upper(v['complete_uniform_A0_error']))
                    for k,v in cell['scalar_model_budgets'].items()},
                components={key:[dict(norm=upper(v['polynomial_A0_upper']),error=upper(v['complete_uniform_A0_error']),
                    degree=v['complete_finite_support'],error_degree=v['complete_remainder_support']) for v in cell[key]]
                    for key in ('D_component_budgets','Fnu_component_budgets','Rnon_component_budgets','Ae2_component_budgets')})
        summary['rows']=[]
        for row in result['rows']:
            cached=compact(row['direct_Fourier_cached_complete_eta'])
            fresh=[dict(subdivisions=x['subdivisions'],
                repaired_low193_sup=upper(x['repaired_low193_complete_residual_L2_sup']),
                repaired_low193_radial=upper(x['repaired_low193_complete_residual_L2_radial']),
                children=[compact(c) for c in x['children']]) for x in row['new_fixed_eta_selected_refinements']]
            detail=dict(common_row=row['common_row'],interval=row['interval'],
                old_complete_full160=row['original_complete_nonmean_residual_bound'],
                direct_Fourier_cached_complete_eta=cached,new_fixed_eta_refinements=fresh,
                actual_target_calls=row['actual_target_calls_for_new_fixed_eta_refinements'],
                seconds=row['seconds'])
            save(self.evidence/f'row-{row["common_row"]:04d}-source-diagnostic-summary.json',detail)
            summary['rows'].append(dict(common_row=row['common_row'],interval=row['interval'],
                old_full160_sup=upper(row['original_complete_nonmean_residual_bound']['L2_sup']),
                cached_direct_Fourier_low193_sup=cached['direct_low193_sup'],
                cached_triangle_low193_sup=cached['triangle_low193_sup'],
                cached_repaired_low193_sup=cached['repaired_low193_sup'],
                cached_repaired_low193_radial=cached['repaired_low193_radial'],
                cached_true_high97_to160_sup=cached['high97_to160_sup'],
                fresh_fixed_eta=[{k:v for k,v in x.items() if k!='children'} for x in fresh],
                seconds=row['seconds']))
        summary['native_sha256']=digest(native)
        save(self.evidence/'low193-Fourier-mean-and-fixed-eta-pilot-summary.json',summary)
        self.state.update(complete=True,complete_native_sha256=digest(native),
            actual_selected_original_rows=result['selected_original_rows'],
            actual_selected_projection_gates=len(result['gates']),
            complete_body_projection_cover=False,unknown_high_inputs_not_removed=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','prepared','previous-artifacts','body-artifact','repair-artifact','work','artifact-dir'):
        p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--compute-minutes',type=int,default=30);p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='low193-Fourier-mean-fixed-eta-diagnostic';a.mode='prepare';a.first=0;a.end=0
    a.recovery_manifest=None;a.recovery_sha=None
    worker=FourierMeanDiagnosticWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
