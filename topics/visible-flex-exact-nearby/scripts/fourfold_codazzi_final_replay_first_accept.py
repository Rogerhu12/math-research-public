#!/usr/bin/env python3
"""Run an unchanged producer, retain its first completed nodal checkpoint.

This supervisor only stops execution after the producer has saved all nodes,
state values, radial derivatives and the checkpoint SHA. No numerical gate is
changed. Every exit status below is observed in this new attempt.
"""
from __future__ import annotations
import argparse, datetime, hashlib, json, os, resource, signal, subprocess, sys, time
from pathlib import Path

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--topic',type=Path,required=True)
    ap.add_argument('--attempt',type=Path,required=True)
    ap.add_argument('--stage',type=int,choices=[1,2],required=True)
    ap.add_argument('--guess',type=Path,required=True)
    ap.add_argument('--address-space-mib',type=int,default=4096)
    args=ap.parse_args()
    args.attempt.mkdir(parents=True,exist_ok=False)
    manifest=json.loads((args.topic/'notes/2026-11-13-R133-final-moving-replay-chain.json').read_text())
    stage=manifest['stages'][args.stage-1]
    producer=args.topic/stage['producer']
    digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    if digest(producer)!=stage['producer_sha256']:
        raise ValueError('original producer SHA mismatch')
    argv=list(stage['original_producer_arguments'])
    replacements={'--guess':str(args.guess.resolve()),'--out':str(args.attempt/'floating.json'),
                  '--candidate':str(args.attempt/'producer-candidate.json')}
    for flag,value in replacements.items():argv[argv.index(flag)+1]=value
    for flag,name in [('--qr-scratch','qr'),('--checkpoint-dir','checkpoints')]:
        if flag in argv:argv[argv.index(flag)+1]=str(args.attempt/name)
        else:argv.extend([flag,str(args.attempt/name)])
        (args.attempt/name).mkdir()
    command=[sys.executable,str(producer),*argv]
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1',PYTHONUNBUFFERED='1')
    record={'kind':'actual_replay_unchanged_producer_first_complete_accept',
            'stage':args.stage,'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'complete':False,'status':'started','producer_sha256':digest(producer),
            'guess_sha256':digest(args.guess),'command':command,'cwd':str(args.topic),
            'address_space_limit_mib':args.address_space_mib,
            'original_mathematical_arguments_retained':True,
            'first_complete_accept_observed':False,'intentional_signal_sent':None,
            'environment':{k:env[k] for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','PYTHONDONTWRITEBYTECODE']}}
    process_file=args.attempt/'process.json'
    def save():
        tmp=process_file.with_suffix('.tmp');tmp.write_text(json.dumps(record,indent=2,allow_nan=False)+'\n');tmp.replace(process_file)
    save()
    def limits():
        n=args.address_space_mib*1024**2
        resource.setrlimit(resource.RLIMIT_AS,(n,n))
    start=time.monotonic()
    with (args.attempt/'stdout.log').open('x') as log:
        child=subprocess.Popen(command,cwd=args.topic,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
                               text=True,bufsize=1,start_new_session=True,preexec_fn=limits)
        record['pid']=child.pid;save()
        for line in child.stdout:
            log.write(line);log.flush();print(line,end='',flush=True)
            if 'accepted_complete_checkpoint' in line and not record['first_complete_accept_observed']:
                record['first_complete_accept_observed']=True
                record['complete_accept_log_line']=line.rstrip('\n')
                record['intentional_signal_sent']='SIGINT after complete checkpoint SHA was printed'
                save();os.killpg(child.pid,signal.SIGINT)
        code=child.wait()
    record.update(complete=True,status='first_complete_accept_then_intentional_stop' if record['first_complete_accept_observed'] else 'producer_exited_before_requested_accept',
                  actual_returncode=code,wall_seconds=time.monotonic()-start,
                  maximum_child_rss_kib=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
                  ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
    save();print(json.dumps(record,indent=2),flush=True)

if __name__=='__main__':main()
