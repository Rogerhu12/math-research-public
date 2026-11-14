#!/usr/bin/env python3
"""Actual same-g nonlinear DN continuation in a declared cut-height ray.

Every response is retained. Only a real converged response advances the
accepted ray factor. Failed requests are not fabricated into checkpoints.
The worker's equations, residual tolerance and geometric root checks remain
unchanged. This is a finite tail calculation, not a complete surface proof.
"""
from __future__ import annotations
import argparse,datetime,gzip,hashlib,json,os,subprocess,threading,time
from pathlib import Path


def identity(path):
    path=Path(path).resolve();data=path.read_bytes()
    return dict(path=str(path),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())


def save(path,value):
    data=(json.dumps(value,indent=2,allow_nan=False)+'\n').encode()
    if len(data)>1_000_000:path=path.with_name(path.name+'.gz');data=gzip.compress(data,compresslevel=6)
    if len(data)>=5_000_000:raise ValueError('Split an actual response before exceeding 5 MB')
    temporary=path.with_name(path.name+'.tmp');temporary.write_bytes(data);temporary.replace(path)
    return identity(path)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('worker','config','request','out-prefix'):parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--initial-scale',type=float,required=True)
    parser.add_argument('--growth',type=float,default=1.8)
    args=parser.parse_args();stem=args.out_prefix.resolve();stem.parent.mkdir(parents=True,exist_ok=True)
    if list(stem.parent.glob(stem.name+'*')):raise FileExistsError('Use a fresh continuation stem')
    if not 0<args.initial_scale<=1 or not 1<args.growth<4:raise ValueError('Positive initial scale and growth between 1 and 4 required')
    target=json.loads(args.request.read_text());height=target['height'];started=time.monotonic();stop=threading.Event()
    runtime=dict(phase='starting',body_finished=False,accepted_factor=0.,request_count=0)
    report=dict(schema='fd2d-actual-nonlinear-tail-ray-continuation-v1',source=identity(__file__),
        worker=identity(args.worker),config=identity(args.config),request=identity(args.request),
        target=target,initial_factor=args.initial_scale,growth=args.growth,responses=[],
        scope=__doc__,full_target_accepted=False)
    def heartbeat():
        while not stop.is_set():
            item=dict(runtime,seconds=time.monotonic()-started,utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
            pid=runtime.get('worker_pid')
            if pid:
                try:item['worker_memory']={a.split(':',1)[0]:a.split(':',1)[1].strip() for a in Path(f'/proc/{pid}/status').read_text().splitlines() if a.startswith(('VmRSS:','VmHWM:','Threads:'))}
                except OSError:pass
            save(stem.with_name(stem.name+'-runtime.json'),item);stop.wait(5.)
    thread=threading.Thread(target=heartbeat,daemon=True);thread.start()
    try:
        with stem.with_name(stem.name+'-stderr.txt').open('w') as stderr:
            process=subprocess.Popen(['node',str(args.worker.resolve()),str(args.config.resolve())],stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,stderr=stderr,text=True,bufsize=1,env=os.environ.copy())
            runtime.update(worker_pid=process.pid,phase='waiting_ready')
            line=process.stdout.readline()
            if not line:raise RuntimeError(f'EOF before ready, observed code {process.poll()}')
            ready=json.loads(line);report['ready']=save(stem.with_name(stem.name+'-ready.json'),ready)
            if ready.get('event')!='ready':raise RuntimeError('First record was not ready')
            accepted=0.;factor=args.initial_scale;count=0;failed_upper=None
            while True:
                count+=1;req=dict(height=[factor*h for h in height],jacobian=True,audit=factor==1.)
                req_path=stem.with_name(stem.name+f'-request-{count:04d}.json');req_id=save(req_path,req)
                runtime.update(phase='actual_nonlinear_solve',request_count=count,requested_factor=factor)
                process.stdin.write(json.dumps(req)+'\n');process.stdin.flush();request_start=time.monotonic()
                line=process.stdout.readline()
                if not line:raise RuntimeError(f'EOF on request {count}, observed code {process.poll()}')
                response=json.loads(line);response_id=save(stem.with_name(stem.name+f'-response-{count:04d}.json'),response)
                row=dict(call=count,factor=factor,converged=response.get('converged',False),residual=response.get('residual'),
                    failure=response.get('failed'),request=req_id,response=response_id,seconds=time.monotonic()-request_start,
                    has_actual_audit=response.get('audit') is not None)
                report['responses'].append(row)
                if response.get('converged') is True:
                    accepted=factor;runtime['accepted_factor']=accepted;runtime['accepted_response']=response_id
                    report['last_accepted']=row
                    if accepted==1.:
                        report['full_target_accepted']=True;save(stem.with_name(stem.name+'-progress.json'),report)
                        print(json.dumps({k:row[k] for k in ('call','factor','converged','residual','failure','seconds')}),flush=True);break
                    if failed_upper is not None and accepted>=failed_upper:failed_upper=None
                    factor=min(1.,accepted*args.growth)
                    # A previously failed target can become solvable from a
                    # nearer true nonlinear state. Retry that exact target.
                    if failed_upper is not None:factor=min(factor,failed_upper)
                else:
                    failed_upper=factor if failed_upper is None else min(failed_upper,factor)
                    factor=(accepted+factor)/2 if accepted else factor/4
                save(stem.with_name(stem.name+'-progress.json'),report)
                print(json.dumps({k:row[k] for k in ('call','factor','converged','residual','failure','seconds')}),flush=True)
                if factor<=accepted or factor<=0:raise ArithmeticError('Continuation increment exhausted floating representation; retain last actual accepted state')
                if failed_upper is not None and accepted and failed_upper-accepted<=1e-12*max(accepted,args.initial_scale):
                    raise ArithmeticError('Actual failed/successful factors bracket a resolved local continuation obstruction; inspect saved failures and states')
            runtime['phase']='closing_worker';process.stdin.write('{"stop":true}\n');process.stdin.flush();process.stdin.close()
            process.stdout.close();report['worker_returncode']=process.wait()
    except BaseException as exc:
        report['exception']=dict(type=type(exc).__name__,message=str(exc))
        if 'process' in locals():
            report['worker_returncode_observed']=process.poll()
            if process.poll() is None:
                # This owner finishes its own protocol after a handled local
                # continuation obstruction; no other process is touched.
                try:process.stdin.write('{"stop":true}\n');process.stdin.flush();process.stdin.close();process.stdout.close();report['worker_returncode']=process.wait()
                except (BrokenPipeError,OSError):report['worker_returncode_observed']=process.poll()
    finally:
        report['seconds']=time.monotonic()-started;save(stem.with_name(stem.name+'-report.json'),report)
        runtime.update(phase='body_completed',body_finished=True);stop.set();thread.join(timeout=1.)
        save(stem.with_name(stem.name+'-runtime.json'),dict(runtime,seconds=time.monotonic()-started,utc=datetime.datetime.now(datetime.timezone.utc).isoformat()))
    print(json.dumps({k:report.get(k) for k in ('full_target_accepted','worker_returncode','worker_returncode_observed','exception','seconds')}),flush=True)


if __name__=='__main__':main()
