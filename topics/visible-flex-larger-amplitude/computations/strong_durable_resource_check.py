#!/usr/bin/env python3
"""Small owned-process fixtures for durable wait4/exit/signal bookkeeping."""
import argparse
import hashlib
import json
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time

HERE = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError(args.out)
    helper = HERE/'strong_durable_resource_run.py'
    sources = {str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in (helper,Path(__file__))}
    rows = []
    with tempfile.TemporaryDirectory(prefix='strong-owned-resource-fixture-') as temporary:
        root = Path(temporary)
        for name,body,expected in (
                ('normal','import sys;sys.exit(0)',0),
                ('nonzero','import sys;sys.exit(7)',7),
                ('signal','import time;time.sleep(30)',-signal.SIGTERM)):
            out,heartbeat,ownership = (root/(name+s) for s in ('.json','-heartbeat.json','-owner.json'))
            command = [sys.executable,str(helper),'--out',str(out),'--heartbeat',str(heartbeat),
                '--ownership',str(ownership),'--task-prefix','fixture-'+name,
                '--heartbeat-seconds','1','--',sys.executable,'-c',body]
            started = time.monotonic()
            proc = subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
            if name=='signal':
                deadline = started+10
                while not heartbeat.exists():
                    if proc.poll() is not None or time.monotonic()>deadline:
                        raise RuntimeError('Fixture supervisor did not publish live ownership')
                    time.sleep(.02)
                proc.send_signal(signal.SIGTERM)
            stdout,stderr = proc.communicate(timeout=15)
            data = json.loads(out.read_text())
            beat = json.loads(heartbeat.read_text())
            owned = json.loads(ownership.read_text())
            passed = (data['exitcode']==expected and data['wait4_observed']
                and data['owned_child_pid']==owned['owned_child_pid']
                and beat['status']=='completed-by-owned-wait4'
                and data['automatic_restarts']==0
                and data['resource_wrapper_sha256']==sources[str(helper)]
                and proc.returncode==(expected if expected>=0 else 128-expected))
            if name=='signal':
                passed = passed and data['received_supervisor_signals'][0]['forwarded']
            rows.append(dict(name=name,passed=bool(passed),resource=data,ownership=owned,
                final_heartbeat=beat,supervisor_returncode=proc.returncode,stdout=stdout,stderr=stderr,
                fixture_wall_seconds=time.monotonic()-started))
            if not passed:
                raise RuntimeError('Owned process resource fixture failed: '+name)
    report = dict(scope=__doc__,passed=all(row['passed'] for row in rows),source_sha256=sources,
        cases=rows,physical_Flow_or_RHS_loaded=False,Node_processes_started=0,
        BVPs_solved=0,prior_unknown_job_exit_not_inferred=True)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(passed=report['passed'],cases=len(rows),out=str(args.out))),flush=True)


if __name__ == '__main__':
    main()
