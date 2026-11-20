#!/usr/bin/env python3
"""Build the q=.06 field by actual low-height/high-DN amplitude continuation.

Each intermediate amplitude is a new initializer design. Its H3 target is
the historical q=.06 height times q/.06, and the other seven conditions are
the original linear DN. The original equations, domain and metric tests are
not relaxed. A failed larger step is retried from the previous accepted full
field with a smaller amplitude step, never by labelling failure as success.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--workdir',type=Path,required=True)
    p.add_argument('--amplitudes',type=float,nargs='+',default=[.006,.012,.02,.03,.04,.05,.06])
    p.add_argument('--minimum-step',type=float,default=.0005)
    a=p.parse_args()
    repo,work=a.repo.resolve(),a.workdir.resolve()
    topic=repo/'topics/visible-flex-held-10pct'
    scripts=topic/'scripts/resume_m3'
    bootstrap=json.loads((work/'bootstrap.json').read_text())
    inputs=work/'inputs'
    pending=list(a.amplitudes)
    if pending[0]<=0 or pending[-1]!=.06 or any(x>=y for x,y in zip(pending,pending[1:])):
        raise ValueError('Use increasing positive amplitudes ending at .06')
    record=dict(scope=__doc__,stages=[],original_nonlinear_DN_accepted=False)
    summary=work/'height-amplitude-path.json'
    previous=None
    accepted_q=None
    serial=0
    while pending:
        q=pending.pop(0)
        output=work/('height-q060' if q==.06 and not (work/'height-q060').exists()
                    else f'height-path-{serial:02d}-q{q:.7f}')
        command=[sys.executable,'-u',scripts/'height_anchor_prefix_lowmode.py',
            '--height-record',topic/'scripts/resume_transfer/q060_exact_saved_inner_resume_terminal.json',
            '--height-count','1','--amplitude',str(q),'--warp-reference',str(q),
            '--source-topic',bootstrap['source_topic'],'--short-bridge',bootstrap['short_bridge'],
            '--profile',inputs/'q060-profile.json','--chart',inputs/'reference/chart.json',
            '--port',inputs/'q060-port.json','--nodes','401','--max-nodes','6000',
            '--outdir',output]
        if previous is not None:
            command+=['--restart-checkpoint',previous/'checkpoint.json.gz']
        # The first small-amplitude seed has zero high controls. It does not
        # inject the historical q=.06 physical controls at q=.006.
        print(json.dumps(dict(event='height_path_start',q=q,previous_q=accepted_q)),flush=True)
        result=subprocess.run(list(map(str,command)),cwd=repo,check=False)
        run_path=output/'run.json'
        row=json.loads(run_path.read_text()) if run_path.exists() else {}
        metric=row.get('prefix_audit',{}).get('metric_l1')
        success=bool(result.returncode==0 and row.get('solver_success') and not row.get('error')
                     and metric is not None and metric<=1.e-6)
        brief=dict(q=q,previous_q=accepted_q,returncode=result.returncode,accepted=success,
                   metric_l1=metric,error=row.get('error'),raw=row.get('raw_return'),
                   original_linear_DN_physical_residual=row.get('original_linear_DN_physical_residual'),
                   run_sha256=hashlib.sha256(run_path.read_bytes()).hexdigest() if run_path.exists() else None)
        record['stages'].append(brief)
        summary.write_text(json.dumps(record,indent=2)+'\n')
        print(json.dumps(dict(event='height_path_terminal',**brief)),flush=True)
        serial+=1
        if success:
            previous,accepted_q=output,q
            continue
        if accepted_q is None or (q-accepted_q)/2<a.minimum_step:
            return 2
        pending[:0]=[(q+accepted_q)/2,q]
    # After a smaller retry at .06, the accepted directory may have a serial
    # name; this compact record is the authoritative handoff to the next stage.
    record.update(accepted_q=accepted_q,accepted_directory=str(previous),
                  accepted_raw=str(previous/row['raw_return']['file']),
                  status='q060_initializer_ready')
    summary.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(dict(event='q060_height_initializer_ready',
                         directory=str(previous),raw=record['accepted_raw'])),flush=True)
    return 0


if __name__=='__main__':
    sys.exit(main())
