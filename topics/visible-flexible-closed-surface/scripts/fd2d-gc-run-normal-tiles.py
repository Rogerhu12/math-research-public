#!/usr/bin/env python3
"""Execute only missing declared normal tiles, recording every child exit.

The individual tile entry writes its transport manifest last.  A complete
manifest is reused here, then fully verified by the independent merger.
An interrupted controller can therefore resume without recomputing any
closed tile.  There is no process timeout or mathematical retry rule.
"""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time


def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()


def atomic_json(path,value):
    tmp=path.with_name(path.name+'.tmp')
    tmp.write_text(json.dumps(value,indent=2,allow_nan=False)+'\n')
    tmp.replace(path)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--request',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--maximum-new-tiles',type=int)
    args=ap.parse_args()
    request=json.loads(args.request.read_text());root=Path(request['cache_dir'])
    plan_path=root/'normal-partition-plan.json';plan=json.loads(plan_path.read_text())
    stop=Path(request['settings']['owner_stop_file'])
    report_path=args.out_prefix.with_name(args.out_prefix.name+'-report.json')
    if report_path.exists():raise FileExistsError('A controller report is immutable; choose a fresh prefix')
    began=time.monotonic()
    report=dict(schema='fd2d-owned-normal-tile-controller-v1',source=dict(path=__file__,
        sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()),started_utc=utc(),
        request=dict(path=str(args.request),sha256=hashlib.sha256(args.request.read_bytes()).hexdigest()),
        plan=dict(path=str(plan_path),sha256=hashlib.sha256(plan_path.read_bytes()).hexdigest()),
        actual_child_records=[],already_closed_tiles=[],complete=False,
        accepted_states_created=0,finite_objective_changed=False,no_timeout_installed=True)
    def save():
        report['seconds']=time.monotonic()-began;atomic_json(report_path,report)
    save();new=0
    for descriptor in plan['tiles']:
        tile_id=descriptor['id'];manifest=root/'normal-tiles'/tile_id/'manifest.json'
        if manifest.exists():
            report['already_closed_tiles'].append(tile_id);save();continue
        if stop.exists():
            report.update(owner_stop_observed=True,ended_utc=utc(),controller_returncode=130);save();return 130
        if args.maximum_new_tiles is not None and new>=args.maximum_new_tiles:
            report.update(natural_batch_boundary=True,ended_utc=utc(),controller_returncode=0);save();return 0
        attempt=1
        while True:
            prefix=Path(request['run_prefix']+'-tile-'+tile_id+f'-a{attempt:02d}')
            receipt=prefix.with_name(prefix.name+'-process-receipt.json')
            if not receipt.exists() and not prefix.with_name(prefix.name+'-report.json').exists():break
            attempt+=1
        argv=[sys.executable,'-u','scripts/fd2d-run-monitored-command-v2.py',
            '--receipt',str(receipt),'--',sys.executable,'-u','scripts/fd2d-gc-stage-normal-tile.py',
            '--request',str(args.request),'--out-prefix',str(prefix),'--tile-id',tile_id]
        record=dict(tile_id=tile_id,ordinal=descriptor['ordinal'],kind=descriptor['kind'],
            attempt=attempt,started_utc=utc(),argv=argv,receipt=str(receipt),complete=False)
        report['actual_child_records'].append(record);save()
        print(json.dumps(dict(event='launch_missing_normal_tile',tile_id=tile_id,attempt=attempt)),flush=True)
        run=subprocess.run(argv)
        record.update(actual_monitor_returncode=run.returncode,ended_utc=utc(),
            transport_manifest_exists=manifest.exists())
        if receipt.exists():
            observed=json.loads(receipt.read_text())
            record.update(actual_child_returncode=observed['actual_child_returncode'],
                actual_child_seconds=observed['seconds'],
                peak_rss_kib=observed['kernel_child_maximum_resident_KiB'])
        record['complete']=bool(run.returncode==0 and manifest.exists());new+=1;save()
        print(json.dumps(dict(event='actual_normal_tile_exit',**record)),flush=True)
        if not record['complete']:
            code=run.returncode if run.returncode>0 else 128-run.returncode if run.returncode<0 else 1
            report.update(ended_utc=utc(),controller_returncode=code,stopped_at_missing_tile=tile_id);save();return code
    report.update(complete=True,ended_utc=utc(),controller_returncode=0,
        all_tile_manifests_present=True,whole_normal_sum_not_yet_verified=True)
    save();print(json.dumps(dict(event='all_normal_tiles_durably_present',tiles=len(plan['tiles']))),flush=True)
    return 0


if __name__=='__main__':raise SystemExit(main())
