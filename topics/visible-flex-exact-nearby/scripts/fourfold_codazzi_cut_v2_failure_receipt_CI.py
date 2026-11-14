#!/usr/bin/env python3
"""Publish the actual failed cut-v2 native and child log as small text receipts.

No mathematical producer is imported or invoked. Original compressed bytes,
native SHA, process SHA and child outcome are retained without reclassification.
"""
from __future__ import annotations
import argparse,gzip,json,shutil,signal
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC,save

RUN=43609037484
NATIVE='9f8ed802456a6098e2b7ba03cb1f31f7dbcec62be426bd3d7c3d4ee0f14d42a4'
PRODUCER='8df26cef87a2eef12638d9bb374a973497512056ed656a7d0ef5bb4601474c34'
WORKER='7ac3d9f34a3735b5ed8a0d88487ad115124dc30957a50cb74679d8e2d1129a5e'
MANIFEST='24d6e0b1f3e9fc2604a6e83f557dd2da142f734cb8e3db58f055727aad56f175'


class ReceiptWorker(ReviewedBodyWorker):
    def __init__(self,a):
        super().__init__(a)
        self.name=f'run-{self.run_label}-original-cut-v2-failure-receipt'
        self.dest=TOPIC/'notes/known_cut_failure_receipts_ci'/self.name
        self.state.update(kind='original_cut_v2_actual_failure_text_receipt_process_v1',
            worker_source_sha256=digest(__file__),mathematical_children_executed=0,
            original_run=RUN,original_scientific_sources_unchanged=True)

    def check_inputs(self):
        super().check_inputs()
        if digest(__file__)!=self.args.receipt_source_sha:
            raise ValueError('the separately frozen receipt source changed')
        if self.args.manifest_sha!=MANIFEST:
            raise ValueError('the original cut-v2 manifest is required')

    def prepare(self):
        root=self.args.original_artifact.resolve()
        pp=root/'process.json'
        np=root/'native/known-cut-direction-complete-cap-mixed-source-pilot.json.gz'
        process=read(pp);native=read(np)
        if (digest(np)!=NATIVE or native.get('source_sha256')!=PRODUCER
            or str(process.get('run_id'))!=str(RUN)
            or process.get('repository')!='Rogerhu12/math-research-public'
            or process.get('worker_source_sha256')!=WORKER
            or process.get('input_manifest_sha256')!=MANIFEST
            or not process.get('failure') or not native.get('failure')
            or process.get('complete') or native.get('complete')
            or len(process.get('children',[]))!=1
            or process['children'][0].get('actual_returncode')!=1):
            raise ValueError('the original actual failed-v2 artifact differs')
        shutil.copyfile(pp,self.evidence/'original-v2-artifact-process.json')
        save(self.evidence/'original-v2-failed-native-decoded.json',native)
        lp=root/'producer.stdout.log'
        if not lp.exists():lp=root/'producer.stdout.log.gz'
        if not lp.exists():raise FileNotFoundError('the actual original child stdout is required')
        raw=lp.read_bytes()
        decoded=gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw
        log=decoded.decode('utf-8',errors='strict')
        (self.evidence/'original-v2-child-log-tail.txt').write_text(log[-60000:],encoding='utf-8')
        receipt=dict(original_public_run=RUN,original_native_sha256=digest(np),
            original_actual_artifact_process_sha256=digest(pp),
            original_source_sha256=PRODUCER,original_worker_sha256=WORKER,
            original_native_failure=native['failure'],original_native_gates=native.get('gates',[]),
            original_completed_new_one_column_cells=len(native.get('new_one_column_rows',[])),
            original_log_sha256=digest(lp),original_log_was_compressed=raw[:2]==b'\x1f\x8b',
            published_log_is_last60000_text_characters=True,
            mathematical_children_executed=0,original_failure_not_relabelled=True)
        save(self.evidence/'original-v2-failure-receipt.json',receipt)
        self.state.update(complete=True,receipt=receipt)
        print(json.dumps(receipt),flush=True)
        print('ORIGINAL_ACTUAL_CHILD_LOG_TAIL\n'+log[-60000:],flush=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','original-artifact','work','artifact-dir'):
        p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha','receipt-source-sha'):
        p.add_argument('--'+name,required=True)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='cut-v2-failure-receipt';a.mode='prepare';a.first=0;a.end=0
    a.recovery_manifest=None;a.recovery_sha=None;a.prepared=None;a.previous_artifacts=None
    a.compute_minutes=5;a.checkpoint_minutes=1
    w=ReceiptWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(w,'interrupted',True))
    w.run_cap()


if __name__=='__main__':main()
