# R165 finite objective entry; never consumes a v25 old-goal packet.
#!/usr/bin/env python3
"""Run missing normal tiles in small context-reusing monitored batches."""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time


def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()


def write_json(path,value):
    temp=path.with_name(path.name+'.tmp')
    temp.write_text(json.dumps(value,indent=2,allow_nan=False)+'\n');temp.replace(path)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--request',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--batch-size',type=int,default=4)
    args=ap.parse_args()
    if not 1<=args.batch_size<=4:raise ValueError('Use at most four independently saved tiles per process')
    request=json.loads(args.request.read_text());root=Path(request['cache_dir'])
    plan_path=root/'normal-partition-plan.json';plan=json.loads(plan_path.read_text())
    stop=Path(request['settings']['owner_stop_file']);started=time.monotonic()
    report_path=args.out_prefix.with_name(args.out_prefix.name+'-report.json')
    if report_path.exists():raise FileExistsError(report_path)
    report=dict(schema='fd2d-owned-normal-small-batch-controller-v1',started_utc=utc(),
        source=dict(path=__file__,sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()),
        request=dict(path=str(args.request),sha256=hashlib.sha256(args.request.read_bytes()).hexdigest()),
        plan=dict(path=str(plan_path),sha256=hashlib.sha256(plan_path.read_bytes()).hexdigest()),
        context_reuse_only=True,finite_target_or_tile_partition_changed=False,
        batch_size=args.batch_size,actual_child_records=[],complete=False,accepted_states_created=0)
    def save():report['seconds']=time.monotonic()-started;write_json(report_path,report)
    save()
    while True:
        missing=[d for d in plan['tiles'] if not (root/'normal-tiles'/d['id']/'manifest.json').exists()]
        report['closed_manifest_count']=len(plan['tiles'])-len(missing);save()
        if not missing:
            report.update(complete=True,ended_utc=utc(),controller_returncode=0,
                whole_normal_sum_not_yet_verified=True);save();return 0
        if stop.exists():
            report.update(owner_stop_observed=True,ended_utc=utc(),controller_returncode=130);save();return 130
        selected=missing[:args.batch_size];first,last=selected[0]['ordinal'],selected[-1]['ordinal']
        attempt=1
        while True:
            prefix=Path(request['run_prefix']+f'-tiles-{first:04d}-{last:04d}-a{attempt:02d}')
            receipt=prefix.with_name(prefix.name+'-process-receipt.json')
            if not receipt.exists() and not prefix.with_name(prefix.name+'-report.json').exists():break
            attempt+=1
        argv=[sys.executable,'-u','scripts/fd2d-run-monitored-command-v2.py','--receipt',str(receipt),
            '--',sys.executable,'-u','scripts/fd2d-gc-grouped-stage-normal-tile-batch.py',
            '--request',str(args.request),'--out-prefix',str(prefix)]
        for d in selected:argv+=['--tile-id',d['id']]
        record=dict(tile_ids=[d['id'] for d in selected],started_utc=utc(),attempt=attempt,
            argv=argv,receipt=str(receipt),complete=False)
        report['actual_child_records'].append(record);save()
        print(json.dumps(dict(event='launch_missing_tile_batch',tile_ids=record['tile_ids'])),flush=True)
        run=subprocess.run(argv)
        record.update(actual_monitor_returncode=run.returncode,ended_utc=utc(),
            closed_tile_ids=[d['id'] for d in selected if (root/'normal-tiles'/d['id']/'manifest.json').exists()])
        if receipt.exists():
            observed=json.loads(receipt.read_text())
            record.update(actual_child_returncode=observed['actual_child_returncode'],
                actual_child_seconds=observed['seconds'],peak_rss_kib=observed['kernel_child_maximum_resident_KiB'])
        record['complete']=run.returncode==0 and len(record['closed_tile_ids'])==len(selected);save()
        print(json.dumps(dict(event='actual_tile_batch_exit',**record)),flush=True)
        if not record['complete']:
            code=run.returncode if run.returncode>0 else 128-run.returncode if run.returncode<0 else 1
            report.update(ended_utc=utc(),controller_returncode=code);save();return code


if __name__=='__main__':raise SystemExit(main())
