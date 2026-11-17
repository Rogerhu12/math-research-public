#!/usr/bin/env python3
"""Continue only from a verified finite prefix/actual-tail checkpoint pair.

Each amplitude is a design computation. Only the same physical tail is reused.
On failure the last successful pair is retained, never an unconverged trial.
"""
import argparse,json,subprocess,sys,time
from pathlib import Path

p=argparse.ArgumentParser(description=__doc__)
for key in ('source-topic','prefix-driver','coupler-source','worker','profile','chart','port','tail-config','restart','tail-state','out'):
    p.add_argument('--'+key,type=Path,required=True)
p.add_argument('--amplitudes',nargs='+',type=float,required=True);p.add_argument('--modes',type=int,default=8)
p.add_argument('--nodes',type=int,default=501);p.add_argument('--max-nodes',type=int,default=2400)
p.add_argument('--tol',type=float,default=3e-7);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=False)
restart=a.restart.resolve();tail_state=a.tail_state.resolve();rows=[];begin=time.monotonic()
driver=Path(__file__).with_name('couple_smallcut.py')
for q in a.amplitudes:
    name='q'+format(q,'.8f').rstrip('0').replace('.','p')+'-m'+str(a.modes)
    target=(a.out/name).resolve();config=json.loads(a.tail_config.read_text());config['initialCheckpoint']=str(tail_state)
    config['modes']=a.modes;config_path=a.out/(name+'-tail-config.json');config_path.write_text(json.dumps(config,indent=2)+'\n')
    cmd=[sys.executable,'-u',str(driver.resolve())]
    for key in ('source_topic','prefix_driver','coupler_source','worker','profile','chart','port'):
        cmd.extend(['--'+key.replace('_','-'),str(getattr(a,key).resolve())])
    cmd.extend(['--tail-config',str(config_path.resolve()),'--restart',str(restart),'--out',str(target),'--amplitude',str(q),'--modes',str(a.modes),'--angular',str(max(256,32*a.modes)),'--audit-angular',str(max(512,64*a.modes)),'--nodes',str(a.nodes),'--max-nodes',str(a.max_nodes),'--tol',str(a.tol),'--warmup-scales','1'])
    print(json.dumps(dict(event='stage_start',amplitude=q,restart=str(restart),tail_state=str(tail_state),out=str(target))),flush=True)
    started=time.monotonic()
    with (a.out/(name+'.log')).open('w')as log:
        process=subprocess.run(cmd,stdout=log,stderr=subprocess.STDOUT)
    summary_path=target/'summary.json';summary=json.loads(summary_path.read_text())if summary_path.exists()else{}
    row=dict(amplitude=q,success=bool(summary.get('solver_success')),error=summary.get('error'),exit_code=process.returncode,seconds=time.monotonic()-started,command=cmd,summary=str(summary_path))
    if summary.get('summary'):
        row.update({k:summary['summary'].get(k)for k in ('metric_l1','kappa_sample','height_max','terminal_height_coeff_max')})
    if summary.get('tail_seam'):
        seam=summary['tail_seam'];row.update({k:seam.get(k)for k in ('tail_shooting_residual','mean_first_mismatch','mean_second_mismatch','nonmean_first_mismatch','nonmean_second_mismatch')})
    rows.append(row)
    if row['success']:
        restart=target/'prefix.json.gz';tail_state=target/summary['tail_seam']['tail_record']
        if not restart.exists()or not tail_state.exists():raise RuntimeError('Successful stage omitted a complete checkpoint pair')
    report=dict(scope=__doc__,rows=rows,last_successful_prefix=str(restart),last_successful_tail=str(tail_state),seconds=time.monotonic()-begin)
    (a.out/'continuation.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in row.items()if k!='command'}),flush=True)
    if not row['success']:break
