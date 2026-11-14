#!/usr/bin/env python3
"""Export exact original successful artifact receipts without new mathematics."""
from __future__ import annotations
import argparse,shutil,signal
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC,save

RECORDS={
    'repair':dict(run=43597921732,
        native='native/complete-known-response-centre-repair-source.json.gz',
        native_sha='05e0493dbe55490adec8fb6603e0ec431d1bc03f051aec86be8a78741f60f0a4',
        source='6e4e8f1a3f69fdc06c15a0471cedb62abce0740b4825ddf5a0d04de4b984d7ad',
        worker='56dbc2905e4c8e41b58fe0dec051c302a648645fe1b272216697919af7fe5bc1',
        manifest='f069ca3ca7c4249f6998f80caba2dffb51abe21b7fc157de438161290ad046e6',
        gates=47),
    'boundary':dict(run=43599771405,
        native='native/known-waist-and-true-cap-sources.json.gz',
        native_sha='b1adeea522b31efa2fc83a6436bc3fe52dbd04630c17d5436927b5872b05e263',
        source='79796ab53f20088da1ef11261be81e2ce548c16772c991eb9d5e8148b2b23204',
        worker='b20f2d6f585ff2cd0627b47feadbce335e1d54b3efa3759a73e57fe60f4bf54a',
        manifest='baebd3764b9a1f013f1b6cf89df5864e2fbe850ceb99510a8efe0460b0aa6f85',
        gates=10)}


class ReceiptWorker(ReviewedBodyWorker):
    def __init__(self,args):
        super().__init__(args)
        self.name=f'run-{self.run_label}-original-known-source-artifact-receipts'
        self.dest=TOPIC/'notes/known_source_receipts_ci'/self.name
        self.state.update(kind='actual_public_original_known_source_artifact_receipts_process_v1',
            worker_source_sha256=digest(__file__),new_mathematical_children_executed=0,
            original_artifact_native_bytes_changed=False,complete_inverse_claimed=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='cached_complete_finite193_Green_known_new_sources_public_inputs_v1':
            raise ValueError('the unchanged existing known-source input closure is required')
        if digest(__file__)!=self.args.receipt_worker_sha:
            raise ValueError('the separately pinned receipt-only infrastructure source changed')
        self.state['separately_pinned_receipt_worker_sha256']=self.args.receipt_worker_sha

    def prepare(self):
        entries=[]
        for label,expected in RECORDS.items():
            root=getattr(self.args,label+'_artifact').resolve()
            process_path=root/'process.json';process=read(process_path);native_path=root/expected['native']
            if (str(process.get('run_id'))!=str(expected['run'])
                or process.get('repository')!='Rogerhu12/math-research-public'
                or not process.get('complete') or process.get('failure')
                or process.get('worker_source_sha256')!=expected['worker']
                or process.get('input_manifest_sha256')!=expected['manifest']
                or process.get('complete_native_sha256')!=expected['native_sha']
                or not process.get('children') or any(c.get('actual_returncode')!=0 for c in process['children'])
                or digest(native_path)!=expected['native_sha']):
                raise ValueError('the original actually successful '+label+' artifact is not exact')
            native=read(native_path)
            if (not native.get('complete') or native.get('failure')
                or native.get('source_sha256')!=expected['source']
                or len(native.get('gates',[]))!=expected['gates']
                or not all(g['passed'] for g in native['gates'])):
                raise ValueError('the original successful '+label+' native record is inconsistent')
            destination=self.evidence/(label+'-original-artifact-process.json')
            shutil.copyfile(process_path,destination)
            entries.append(dict(label=label,original_run=expected['run'],
                exact_artifact_process_sha256=digest(process_path),
                exact_process_evidence_file=str(destination.relative_to(self.artifact)),
                exact_original_native_sha256=digest(native_path),
                original_mathematical_source_sha256=expected['source'],
                original_worker_sha256=expected['worker'],original_manifest_sha256=expected['manifest'],
                original_complete_gates=expected['gates'],
                original_process_bytes_unchanged=True,original_native_bytes_unchanged=True,
                original_actual_children=process['children']))
        receipt=self.evidence/'original-known-source-artifact-receipts.json'
        save(receipt,dict(kind='actual_original_completed_known_source_artifact_receipts_v1',
            complete=True,source_sha256=digest(__file__),entries=entries,
            no_new_mathematical_evaluation=True,
            repository_snapshot_and_final_artifact_receipt_not_identified=True))
        self.state.update(complete=True,receipt_sha256=digest(receipt),
            original_artifact_process_sha256={x['label']:x['exact_artifact_process_sha256'] for x in entries},
            all_original_completed_mathematical_outcomes_reused=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','repair-artifact','boundary-artifact','work','artifact-dir'):
        p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha','receipt-worker-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--compute-minutes',type=int,default=10);p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='original-known-source-receipts';a.mode='prepare';a.first=0;a.end=0
    a.recovery_manifest=None;a.recovery_sha=None
    worker=ReceiptWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
