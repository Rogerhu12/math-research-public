#!/usr/bin/env python3
"""Restore the old coefficient bytes and run only the new M32 transfer."""
from __future__ import annotations
import argparse,gzip,hashlib,shutil,signal,sys
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC,save

REL='topics/visible-flex-exact-nearby/'
COEFFICIENTS='ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d'


class RepairedPositiveWorker(ReviewedBodyWorker):
    def __init__(self,args):
        super().__init__(args)
        self.name=f'run-{self.run_label}-exact-M32-repaired-positive'
        self.dest=TOPIC/'notes/repaired_positive_ci'/self.name
        self.state.update(kind='actual_public_exact_M32_repaired_outer_and_positive_high_process_v1',
            worker_source_sha256=digest(__file__),
            original_positive_coefficients_sha256=COEFFICIENTS,
            original_4650_coefficient_rows_recomputed=0,original_target_primitives_rerun=0,
            original_endpoint_or_cap_matrix_recomputed=0,
            exact_affine_parameter_offset='0',physical_parameter='fixed original physical eta0 and nu',
            root_collar_transfer_separate=True,complete_infinite_BVP_inverse_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='exact_M32_repair_cached_positive_and_outer_public_inputs_v1':
            raise ValueError('the separate exact repaired-positive input manifest is required')

    def restore_coefficients(self):
        index_path=self.science/self.manifest['original_positive_binary_parts_index']
        container=read(index_path)
        if (container.get('kind')!='complete_native_lossless_container_binary_parts_v2'
            or container.get('original_sha256')!=COEFFICIENTS
            or container.get('complete_native_rows')!=4650
            or not container.get('native_complete') or container.get('native_failure') is not None
            or not container.get('no_numerical_record_changed')
            or not container.get('original_container_restored_exactly')):
            raise ValueError('the unchanged complete positive binary-container index is required')
        folder=self.args.work.resolve()/'original-verified-inputs';folder.mkdir(parents=True,exist_ok=True)
        output=folder/'original-complete-positive-coefficients.json.gz'
        if output.exists():raise FileExistsError('preserve every restoration provenance')
        hashed=hashlib.sha256();offset=0;records=[]
        with output.open('wb') as stream:
            for i,item in enumerate(container['parts']):
                if item['index']!=i or item['offset']!=offset or Path(item['file']).name!=item['file']:
                    raise ValueError('an original binary container part is missing or reordered')
                part=index_path.parent/item['file'];data=part.read_bytes()
                if len(data)!=item['compressed_bytes'] or digest(part)!=item['compressed_sha256']:
                    raise ValueError('an original compressed positive part changed')
                raw=gzip.decompress(data)
                if len(raw)!=item['bytes'] or hashlib.sha256(raw).hexdigest()!=item['sha256']:
                    raise ValueError('an original positive byte range changed')
                stream.write(raw);hashed.update(raw);offset+=len(raw)
                records.append(dict(index=i,file=item['file'],original_offset=item['offset'],
                    original_bytes=item['bytes'],sha256=item['sha256'],
                    compressed_sha256=item['compressed_sha256']))
        if offset!=container['original_bytes'] or hashed.hexdigest()!=COEFFICIENTS or digest(output)!=COEFFICIENTS:
            raise ValueError('the full original native was not restored byte-for-byte')
        save(self.evidence/'original-positive-byte-restoration.json',dict(
            complete=True,container_sha256=digest(index_path),original_sha256=COEFFICIENTS,
            original_bytes=offset,complete_native_rows=4650,all_original_parts=records,
            no_mathematical_coefficient_recomputation=True))
        self.state['original_complete_positive_byte_restoration_verified']=True
        return output

    def reuse_outer(self,producer,native,expected_inputs):
        root=TOPIC/'notes/repaired_positive_ci'
        if not root.exists():return False
        for process_path in sorted(root.glob('*/process.json')):
            process=read(process_path)
            label='actual_repaired_complete_regular_Hs_and_true_outer_reference'
            children=[c for c in process.get('children',[]) if c.get('label')==label and c.get('actual_returncode')==0]
            original=process_path.parent/'native/repaired-complete-regular-Hs-outer.json.gz'
            records=[item for item in process.get('native_files',[]) if item.get('logical_file')=='native/repaired-complete-regular-Hs-outer.json.gz']
            if (process.get('repository')!='Rogerhu12/math-research-public' or not children
                or not original.exists() or len(records)!=1 or digest(original)!=records[0]['sha256']):
                continue
            outcome=read(original)
            if (not outcome.get('complete') or outcome.get('failure')
                or outcome.get('source_sha256')!=self.manifest['files'][producer]
                or outcome.get('input_sha256')!=expected_inputs
                or len(outcome.get('gates',[]))!=25 or not all(x['passed'] for x in outcome['gates'])):
                continue
            shutil.copyfile(original,native)
            shutil.copyfile(process_path,self.evidence/'original-successful-repaired-outer-process.json')
            self.state.update(repaired_outer_reused_without_execution=True,
                actual_original_repaired_outer_run=process['run_id'])
            return True
        return False

    def prepare(self):
        coefficients=self.restore_coefficients()
        repair=self.science/self.manifest['exact_M32_repair_native']
        cap=self.science/self.manifest['complete_repaired_physical_cap_background']
        old_outer=self.science/self.manifest['original_complete_Hs_outer_native']
        outer=self.cache/'repaired-complete-regular-Hs-outer.json.gz'
        outer_producer=REL+'scripts/fourfold_codazzi_repaired_regular_Hs_outer.py'
        expected_inputs={'repair':digest(repair),'cap-background':digest(cap),'old-outer':digest(old_outer)}
        self.publish()
        if not self.reuse_outer(outer_producer,outer,expected_inputs):
            self.execute('actual_repaired_complete_regular_Hs_and_true_outer_reference',
                [sys.executable,'-u',str(self.science/outer_producer),
                 '--repair',str(repair),'--cap-background',str(cap),'--old-outer',str(old_outer),'--out',str(outer)])
            self.state.update(repaired_outer_reused_without_execution=False,
                actual_original_repaired_outer_run=self.state['run_id'])
        o=read(outer)
        if (not o.get('complete') or o.get('failure')
            or o.get('source_sha256')!=self.manifest['files'][outer_producer]
            or o.get('input_sha256')!=expected_inputs
            or len(o.get('gates',[]))!=25 or not all(x['passed'] for x in o['gates'])):
            raise ValueError('the actual repaired complete Hs outer graph did not pass')
        outer_summary=dict(o);outer_summary['native_sha256']=digest(outer)
        save(self.evidence/'repaired-complete-regular-Hs-outer-summary.json',outer_summary)
        self.state.update(actual_repaired_outer_complete=True,actual_repaired_outer_native_sha256=digest(outer))
        self.publish()
        native=self.cache/'repaired-complete-positive-N97-high-inverse.json.gz'
        producer=REL+'scripts/fourfold_codazzi_repaired_positive_high_Volterra.py'
        self.execute('actual_repaired_4650_complete_positive_rows_and_both_unbounded_high_orders',
            [sys.executable,'-u',str(self.science/producer),
             '--coefficients',str(coefficients),'--repair',str(repair),'--outer',str(outer),
             '--outer-source-sha',self.manifest['files'][outer_producer],'--out',str(native)])
        result=read(native)
        if (not result.get('complete') or result.get('failure')
            or result.get('source_sha256')!=self.manifest['files'][producer]
            or result.get('complete_original_rows')!=4650
            or len(result.get('inflated_rows',[]))!=4650
            or [row.get('homogeneous_angular_order') for row in result.get('orders',[])]!=[0,1]
            or any(not row.get('complete') or row.get('failure') for row in result['orders'])
            or result.get('original_4650_coefficient_rows_recomputed')!=0
            or result.get('original_target_primitives_rerun')!=0
            or result.get('complete_infinite_BVP_inverse_proved')):
            raise ValueError('the complete repaired positive high transfer failed or exceeded its scope')
        summary={key:value for key,value in result.items() if key not in ('inflated_rows','orders')}
        summary['orders']=[{key:value for key,value in row.items() if key!='complete_rows'} for row in result['orders']]
        summary['native_sha256']=digest(native)
        save(self.evidence/'repaired-complete-positive-N97-high-inverse-summary.json',summary)
        self.state.update(complete=True,complete_native_sha256=digest(native),
            actual_repaired_positive_closed_rows=4650,actual_unbounded_high_orders=[0,1],
            order_feedback={str(row['homogeneous_angular_order']):row['bounds']['total_feedback'] for row in result['orders']},
            all_finite_head_mean_and_affine_source_columns_retained=True,
            complete_negative_return_and_global_Schur_still_required=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','work','artifact-dir'):p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--compute-minutes',type=int,default=40);p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='repaired-positive-high';a.mode='prepare';a.first=0;a.end=0
    a.recovery_manifest=None;a.recovery_sha=None
    worker=RepairedPositiveWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
