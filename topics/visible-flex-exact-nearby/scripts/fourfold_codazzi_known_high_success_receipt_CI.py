#!/usr/bin/env python3
"""Publish the original complete known-high result after a diagnostic size failure.

This receipt worker runs no mathematical child and no source row. It consumes
the exact successful7721-row native from run43628921664, whose original child
returned zero before an optional large diagnostic violated the60000-byte gate.
The failed process and original native remain unchanged.
"""
from __future__ import annotations
import argparse,json,shutil,signal
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC
from fourfold_native_lossless_parts import restore

PUBLIC='Rogerhu12/math-research-public'
OLD_RUN=43628921664
OLD_MANIFEST='de4bd52b27daceb5b3ea85a79c2ba37dd01196143384ffc72d0946dc6826a759'
OLD_WORKER='b11f7e85a555b3942d531ce120700c605d081a989abf320ff5758f70e8ee41cd'
OLD_SOURCE='f9104cce14a3f04ebe3271ed19085d9bf4bdc7f9f7c215ed79dd99244e7034bf'
NATIVE_SHA='5ad8aaada967f4626a33e978b1c81adf640ee1abaf0876f54ffd22d6dbd107fd'
SUMMARY_SHA='74e7b40d0eb4c79bf511a501467e73d80116d46990d1ab8e5b43f66f4fcd1b35'
NATIVE_NAME='complete-repaired-M32-known-high-tail-source.json.gz'
SUMMARY_NAME='complete-known-high-Z-tail-source-summary.json'
FAILURE={'type':'ValueError','message':'small source evidence exceeds60000 bytes; preserve full native instead'}


def small(path,data):
    raw=(json.dumps(data,ensure_ascii=False,indent=2)+'\n').encode()
    if len(raw)>60000:raise ValueError('receipt-only plaintext exceeds60000 bytes')
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(raw)


class ReceiptWorker(ReviewedBodyWorker):
    def __init__(self,a):
        super().__init__(a)
        self.name=f'run-{self.run_label}-known-high-math-success-receipt'
        self.dest=TOPIC/'notes/known_high_Z_tail_receipt_ci'/self.name
        self.state.update(kind='actual_public_known_high_success_receipt_without_new_mathematics_v1',
            worker_source_sha256=digest(__file__),original_successful_mathematical_run=OLD_RUN,
            original_mathematical_child_reexecuted=False,new_source_rows_executed=0,
            new_target_provider_calls=0,original_successful_native_bytes_unchanged=True)

    def check_inputs(self):
        super().check_inputs()
        if (self.args.manifest_sha!=OLD_MANIFEST
            or self.manifest.get('kind')!='complete_known_high_Z_tail_source_public_inputs_v1'
            or digest(__file__)!=self.args.receipt_worker_sha):
            raise ValueError('the unchanged147 scientific pins and exact separate receipt worker are required')

    def prepare(self):
        root=self.args.original_artifact.resolve();pp=root/'process.json';p=read(pp)
        gates=[]
        def gate(name,ok):
            gates.append(dict(name=name,passed=bool(ok)))
            if not ok:raise ValueError('original known-high receipt: '+name)
        gate('exact_original_failed_publication_and_successful_mathematical_child',
            p.get('repository')==PUBLIC and str(p.get('run_id'))==str(OLD_RUN)
            and str(p.get('run_attempt'))=='1' and p.get('complete') is False
            and p.get('failure')==FAILURE and p.get('worker_source_sha256')==OLD_WORKER
            and p.get('input_manifest_sha256')==OLD_MANIFEST
            and len(p.get('children',[]))==1
            and p['children'][0].get('label')=='actual_complete7721_known_high_from_exact_Z_tail'
            and p['children'][0].get('actual_returncode')==0)
        records=[x for x in p.get('native_files',[]) if x.get('logical_file')=='native/'+NATIVE_NAME]
        gate('original_complete_native_logical_byte_receipt_retained',
            len(records)==1 and records[0].get('sha256')==NATIVE_SHA and records[0].get('bytes')==7508940)
        native=root/'native'/NATIVE_NAME
        if not native.exists():
            if not records[0].get('lossless_manifest'):raise ValueError('the original complete native is absent')
            native=self.work/'restored-original-complete-known-high.json.gz'
            restore(root/records[0]['lossless_manifest'],native)
        gate('original_successful_native_exact_bytes',digest(native)==NATIVE_SHA)
        d=read(native)
        gate('all_original7721_rows_and_eight_actual_mathematical_gates_complete',
            d.get('kind')=='actual_complete_repaired_M32_known_high_source_from_Z_tail_v1'
            and d.get('source_sha256')==OLD_SOURCE and d.get('complete') and not d.get('failure')
            and d.get('complete_original_common_rows')==7721 and len(d.get('rows',[]))==7721
            and [r['common_row'] for r in d['rows']]==list(range(7721))
            and all(r.get('actual_tail_source_row_complete') for r in d['rows'])
            and len(d.get('gates',[]))==8 and all(g['passed'] for g in d['gates'])
            and d.get('complete_known_high_source_bound_proved')
            and not d.get('actual_full_PDE_response_error_proved')
            and not d.get('complete_infinite_inverse_proved'))
        summary=root/'evidence'/SUMMARY_NAME
        gate('already_successful_small_main_summary_is_exactly_preserved',
            digest(summary)==SUMMARY_SHA and summary.stat().st_size==14387)
        s=read(summary)
        gate('original_summary_refers_to_the_same_complete_native_and_bounds',
            s.get('native_sha256')==NATIVE_SHA and s.get('gates')==d['gates']
            and s.get('complete_known_high_bounds')==d['complete_known_high_bounds']
            and s.get('seconds')==d.get('seconds') and s.get('complete')
            and s.get('source_sha256')==OLD_SOURCE)
        # No old source subprocess, no target and no optional large diagnostic.
        # These are the original complete bytes, not a regenerated certificate.
        shutil.copyfile(native,self.cache/NATIVE_NAME)
        shutil.copyfile(pp,self.evidence/'original-math-success-publication-failure-process.json')
        shutil.copyfile(summary,self.evidence/SUMMARY_NAME)
        receipt=dict(kind='exact_known_high_mathematical_success_then_diagnostic_size_failure_receipt_v1',
            complete=True,gates=gates,original_run=OLD_RUN,original_run_attempt=1,
            original_actual_artifact_process_sha256=digest(pp),original_publication_failure=p['failure'],
            original_mathematical_source_sha256=OLD_SOURCE,original_worker_sha256=OLD_WORKER,
            original_manifest_sha256=OLD_MANIFEST,original_native_sha256=NATIVE_SHA,
            original_small_summary_sha256=SUMMARY_SHA,
            original_child_returncode=0,original_mathematical_gates=d['gates'],
            original_complete_source_rows=7721,original_mathematical_seconds=d['seconds'],
            original_complete_known_high_bounds=d['complete_known_high_bounds'],
            new_mathematical_children=0,new_source_rows=0,new_target_evaluations=0,
            original_native_exact_bytes_republished=True,optional_large_diagnostic_not_recreated=True,
            original_publication_failure_retained=True,
            all_original_low_and_independent_mean_sources_unchanged=True,
            unknown_high_input_feedback_still_required=True,delta_nonzero_background_transfer_still_required=True,
            actual_full_PDE_response_error_proved=False,complete_infinite_inverse_proved=False)
        small(self.evidence/'known-high-original-success-receipt.json',receipt)
        self.state.update(complete=True,complete_native_sha256=NATIVE_SHA,
            original_actual_artifact_process_sha256=digest(pp),original_complete_source_rows=7721,
            original_actual_mathematical_child_returncode=0,original_actual_mathematical_gates=8,
            receipt_checks=len(gates),new_mathematical_children=0,
            complete_known_high_bounds=d['complete_known_high_bounds'])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','original-artifact','work','artifact-dir'):
        p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha','receipt-worker-sha'):
        p.add_argument('--'+name,required=True)
    p.add_argument('--compute-minutes',type=int,default=15);p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='known-high-success-receipt';a.mode='prepare';a.first=0;a.end=0
    a.recovery_manifest=None;a.recovery_sha=None
    worker=ReceiptWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
