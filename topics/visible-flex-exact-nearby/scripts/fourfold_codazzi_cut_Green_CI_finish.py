#!/usr/bin/env python3
"""Automatically consume the actual completed public finite projector cover.

No original matrix cell, mean flow or cap residual is recomputed.  This
separate actual process runs the new public signed-port algebra gates,
then the full directed Green/source consumer and preserves any failure.
"""
from __future__ import annotations
import argparse,shutil,signal,sys
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC,save

REL='topics/visible-flex-exact-nearby/'
BODY='a4f31dccc4b54661b43fc06bac59b6afbb4fa2d6d19614f68f71e044be6e5870'
BODY_PROCESS='0a5dc06520bad5a1230b65cba6e895e998e1f3ce6a32a65d9ffa8800b8ea1a9e'
BOUNDARY='56db8a3498494bf48de14b50418010053bb6058c722c41993c894c463786dc25'


class GreenWorker(ReviewedBodyWorker):
    def __init__(self,args):
        super().__init__(args)
        self.name=(f'run-{self.run_label}-public-signed-Green-algebra' if args.phase=='algebra'
            else f'run-{self.run_label}-finite-head-distributed-Green-from-{args.projector_run}')
        self.dest=TOPIC/'notes/regular_cut_green_ci'/self.name
        self.state.update(kind='actual_public_complete_finite_head_Green_and_source_component_process_v1',
            worker_source_sha256=digest(__file__),original_complete_projector_run=args.projector_run,
            phase=args.phase,
            original_complete_body_mean_run=43586413510,
            original_matrix_cells_recomputed=0,original_body_or_mean_cells_recomputed=0,
            exact_affine_parameter_offset='0',whole_original_parameter_half_width=None,
            physical_parameter='fixed original physical eta0 and original nu',
            complete_finite193_inverse_proved=False,complete_infinite_inverse_proved=False,
            actual_full_PDE_parameter_response_error_proved=False,true_parameter_Schur_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='complete_finite_head_distributed_Green_public_inputs_v1':
            raise ValueError('the separately reviewed signed Green manifest is required')

    def algebra(self):
        gates=self.cache/'public-signed-Green-algebra-gates.json.gz'
        producer=REL+'scripts/fourfold_codazzi_signed_Green_public_algebra_gates.py'
        core=REL+'scripts/fourfold_codazzi_signed_positive_Green_ports.py'
        candidates=[];root=TOPIC/'notes/regular_cut_green_ci'
        if root.exists():
            for process_path in sorted(root.glob('*/process.json')):
                process=read(process_path)
                # A later global Green failure does not erase a genuinely
                # successful independent algebra child. Preserve that full
                # original process, including its failure, when reusing it.
                successful=[child for child in process.get('children',[]) if
                    child.get('label')=='actual_public_signed_positive_Green_and_interface_source_algebra_gates'
                    and child.get('actual_returncode')==0]
                if (process.get('phase') not in ('algebra','complete')
                    or process.get('repository')!='Rogerhu12/math-research-public'
                    or process.get('input_manifest_sha256')!=self.args.manifest_sha
                    or process.get('worker_source_sha256')!=digest(__file__)
                    or len(successful)!=1):continue
                native=process_path.parent/'native/public-signed-Green-algebra-gates.json.gz'
                records=[entry for entry in process.get('native_files',[]) if
                    entry.get('logical_file')=='native/public-signed-Green-algebra-gates.json.gz']
                if not native.exists() or len(records)!=1 or digest(native)!=records[0]['sha256']:continue
                outcome=read(native)
                if (outcome.get('complete') and not outcome.get('failure')
                    and outcome.get('source_sha256')==self.manifest['files'][producer]
                    and outcome.get('core_source_sha256')==self.manifest['files'][core]
                    and len(outcome.get('gates',[]))==7 and all(x['passed'] for x in outcome['gates'])):
                    candidates.append((process_path,native,process))
        if candidates:
            original,native,process=candidates[0]
            shutil.copyfile(native,gates)
            shutil.copyfile(original,self.evidence/'original-successful-public-signed-Green-algebra-process.json')
            self.state.update(algebra_gates_executed_in_this_run=False,
                original_successful_algebra_run=process['run_id'],algebra_gates_reused_without_execution=True)
        else:
            self.execute('actual_public_signed_positive_Green_and_interface_source_algebra_gates',
                [sys.executable,'-u',str(self.science/producer),'--out',str(gates)])
            self.state.update(algebra_gates_executed_in_this_run=True,
                original_successful_algebra_run=self.state['run_id'],algebra_gates_reused_without_execution=False)
        result=read(gates)
        if (not result.get('complete') or result.get('failure')
            or result.get('source_sha256')!=self.manifest['files'][producer]
            or result.get('core_source_sha256')!=self.manifest['files'][core]
            or len(result.get('gates',[]))!=7 or not all(x['passed'] for x in result['gates'])):
            raise ValueError('an actual public directed signed-port algebra gate failed')
        self.state['algebra_native_sha256']=digest(gates)
        return gates

    def prepare(self):
        if self.args.phase=='algebra':
            gates=self.algebra()
            self.state.update(complete=True,complete_native_sha256=digest(gates),actual_public_signed_port_algebra_gates=7)
            return
        source=self.args.projector_artifact.resolve();body=self.args.body_artifact.resolve()
        original=read(source/'process.json');body_process=read(body/'process.json')
        full_source=REL+'scripts/fourfold_codazzi_regular_cut_complete_CI.py'
        if (str(original.get('run_id'))!=str(self.args.projector_run)
            or original.get('repository')!='Rogerhu12/math-research-public'
            or not original.get('complete') or original.get('failure')
            or original.get('phase')!='finish'
            or not original.get('complete_original_5970_cells_claimed')
            or original.get('worker_source_sha256')!=self.manifest['files'][full_source]
            or original.get('input_manifest_sha256')!=self.manifest['complete_projector_input_manifest_sha256']):
            raise ValueError('the actual successful whole original projector run is required')
        projectors=source/'native/complete-5970-local-projectors.json.gz'
        boundary=source/'native/complete-true-weighted-boundaries.json.gz'
        original_body=body/'native/complete-correlated-body-and-mean-errors.json.gz'
        if (digest(projectors)!=original.get('complete_native_sha256')
            or digest(boundary)!=original.get('weighted_boundary_native_sha256')
            or digest(boundary)!=BOUNDARY
            or digest(original_body)!=BODY or digest(body/'process.json')!=BODY_PROCESS
            or str(body_process.get('run_id'))!='43586413510' or not body_process.get('complete')
            or body_process.get('failure') or not body_process.get('children')
            or any(x.get('actual_returncode')!=0 for x in body_process['children'])):
            raise ValueError('an original real complete projector, boundary or mean-flow outcome changed')
        shutil.copyfile(source/'process.json',self.evidence/'original-complete-projector-process.json')
        shutil.copyfile(body/'process.json',self.evidence/'original-complete-body-mean-process.json')
        self.algebra()
        native=self.cache/'complete-finite-head-Green-and-distributed-known-sources.json.gz'
        command=[sys.executable,'-u',str(self.science_topic/'scripts/fourfold_codazzi_regular_cut_distributed_Green_consumer.py'),
            '--projectors',str(projectors),'--projector-process',str(source/'process.json'),
            '--projector-run',str(self.args.projector_run),
            '--projector-consumer-sha',self.manifest['files'][full_source],
            '--projector-manifest-sha',self.manifest['complete_projector_input_manifest_sha256'],
            '--boundary',str(boundary),'--body',str(original_body),'--body-process',str(body/'process.json'),
            '--root-germ',str(self.science/self.manifest['fixed_original_root_germ']),
            '--out',str(native)]
        self.execute('actual_complete_5970_finite_head_Green_with_distributed_original_sources',command)
        result=read(native)
        if (not result.get('complete') or result.get('failure')
            or not result.get('complete_finite193_compressed_body_and_true_low97_cut_inverse_proved')
            or result.get('complete_infinite_inverse_proved')
            or result.get('exact_full_PDE_parameter_response_error_proved')
            or not result.get('both_complete_independent_boundary_source_columns_retained')):
            raise ValueError('the complete finite Green contract failed or exceeded its actual scope')
        summary={k:v for k,v in result.items() if k not in
            ('all_continuous_ports_and_all_interface_sources','complete_forward_source_component_profiles',
             'actual_backward_ports_before_failure')}
        summary['native_sha256']=digest(native)
        save(self.evidence/'complete-finite-head-Green-and-source-summary.json',summary)
        self.state.update(complete=True,actual_public_signed_port_algebra_gates=7,
            complete_native_sha256=digest(native),complete_finite193_inverse_proved=True,
            exact_fixed_phase_norm_interval=result['fixed_phase_error_norm_interval'],
            known_original_residual_and_jump_component_negative_window_L2_upper=
                result['known_original_residual_and_jump_component_negative_window_L2_upper'],
            all_unknown_high_cap_source_and_background_fees_retained=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','work','artifact-dir'):
        p.add_argument('--'+name,type=Path,required=True)
    for name in ('projector-artifact','body-artifact'):p.add_argument('--'+name,type=Path)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--phase',choices=('algebra','complete'),required=True)
    p.add_argument('--projector-run',type=int,default=0)
    p.add_argument('--compute-minutes',type=int,default=50);p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    if a.phase=='complete' and (a.projector_run<=0 or a.projector_artifact is None or a.body_artifact is None):
        raise ValueError('an actual completed original public projector run and both artifacts are required')
    a.kind='complete-cut-Green';a.mode='prepare';a.first=0;a.end=0;a.recovery_manifest=None;a.recovery_sha=None
    worker=GreenWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
