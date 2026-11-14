#!/usr/bin/env python3
"""Execute one complete unchanged original replay stage with new paths only."""
from __future__ import annotations
import argparse,datetime,hashlib,json,os,resource,subprocess,sys,time
from pathlib import Path

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--topic',type=Path,required=True)
    ap.add_argument('--attempt',type=Path,required=True)
    ap.add_argument('--stage',type=int,choices=[3,4,5,6],required=True)
    ap.add_argument('--guess',type=Path,required=True)
    ap.add_argument('--address-space-mib',type=int,default=4096)
    a=ap.parse_args();a.attempt.mkdir(parents=True,exist_ok=False)
    stages=json.loads((a.topic/'notes/2026-11-13-R133-final-moving-replay-chain.json').read_text())['stages']
    s=stages[a.stage-1];producer=a.topic/s['producer'];sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    if sha(producer)!=s['producer_sha256']:raise ValueError('original producer SHA mismatch')
    argv=list(s['original_producer_arguments'])
    out_name=Path(argv[argv.index('--out')+1]).name
    candidate_name=Path(argv[argv.index('--candidate')+1]).name
    out=a.attempt/out_name;candidate=a.attempt/candidate_name
    substitutions={'--guess':str(a.guess.resolve()),'--out':str(out),'--candidate':str(candidate),
                   '--qr-scratch':str(a.attempt/'qr'),'--checkpoint-dir':str(a.attempt/'checkpoints')}
    for flag,value in substitutions.items():argv[argv.index(flag)+1]=value
    for d in ('qr','checkpoints'):(a.attempt/d).mkdir()
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1',PYTHONUNBUFFERED='1')
    command=[sys.executable,str(producer),*argv]
    record=dict(kind='actual_complete_original_final_moving_replay_stage',stage=a.stage,
        complete=False,status='started',producer_sha256=sha(producer),guess_sha256=sha(a.guess),
        candidate_path=str(candidate),out_path=str(out),cwd=str(a.topic),command=command,
        original_mathematical_arguments_retained=True,address_space_limit_mib=a.address_space_mib,
        started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
    process=a.attempt/'process.json'
    def save():
        tmp=process.with_suffix('.tmp');tmp.write_text(json.dumps(record,indent=2,allow_nan=False)+'\n');tmp.replace(process)
    def limits():
        bound=a.address_space_mib*1024**2;resource.setrlimit(resource.RLIMIT_AS,(bound,bound))
    save();start=time.monotonic()
    with (a.attempt/'stdout.log').open('x') as log:
        child=subprocess.Popen(command,cwd=a.topic,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
                               text=True,bufsize=1,start_new_session=True,preexec_fn=limits)
        record['pid']=child.pid;save()
        for line in child.stdout:
            log.write(line);log.flush();print(line,end='',flush=True)
        code=child.wait()
    record.update(complete=True,status='producer_returned_normally' if code==0 else 'actual_nonzero_exit',
        actual_returncode=code,wall_seconds=time.monotonic()-start,
        maximum_child_rss_kib=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
        ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
    if out.exists():
        native=json.loads(out.read_text());record.update(out_sha256=sha(out),
            finite_BVP_success=native.get('finite_BVP_success'),exact_nu=native.get('exact_float_nu'),
            actual_nodes=native.get('radial_nodes'),original_rms_gate_value=native.get('maximum_estimated_relative_radial_residual'))
    if candidate.exists():
        saved=json.loads(candidate.read_text());record.update(candidate_sha256=sha(candidate),
            historical_candidate_sha256=s['historical_complete_candidate_sha256'],
            exact_historical_candidate_container=sha(candidate)==s['historical_complete_candidate_sha256'],
            complete_saved_parts=saved['parts'])
    save();print(json.dumps(record,indent=2),flush=True)

if __name__=='__main__':main()
