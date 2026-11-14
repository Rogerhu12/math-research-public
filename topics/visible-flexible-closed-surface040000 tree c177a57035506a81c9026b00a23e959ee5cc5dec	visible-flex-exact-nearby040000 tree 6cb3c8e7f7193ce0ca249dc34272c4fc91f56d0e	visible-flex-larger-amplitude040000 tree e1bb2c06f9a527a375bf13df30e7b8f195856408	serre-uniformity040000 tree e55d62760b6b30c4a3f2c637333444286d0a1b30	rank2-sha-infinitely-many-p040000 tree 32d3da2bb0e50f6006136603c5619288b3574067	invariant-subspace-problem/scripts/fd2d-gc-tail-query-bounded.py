#!/usr/bin/env python3
"""Record one real nonlinear finite-tail request, its full answer and exit.

This wrapper changes no tail equation or Newton acceptance rule.  It retains
the actual source/configuration/request identities, protocol and heartbeat.
"""
from __future__ import annotations
import argparse,datetime,hashlib,json,os,subprocess,threading,time
from pathlib import Path


def identity(path):
    path=Path(path).resolve();data=path.read_bytes()
    return dict(path=str(path),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())


def write(path,value):
    temporary=path.with_name(path.name+'.tmp')
    temporary.write_text(json.dumps(value,indent=2,allow_nan=False)+'\n');temporary.replace(path)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--node-heap-mib',type=int,default=128)
    parser.add_argument('--node-semi-space-mib',type=int,default=8)
    for name in ('worker','config','request','out-prefix'):
        parser.add_argument('--'+name,type=Path,required=True)
    args=parser.parse_args();stem=args.out_prefix.resolve();stem.parent.mkdir(parents=True,exist_ok=True)
    if list(stem.parent.glob(stem.name+'*')):raise FileExistsError('Use a fresh query stem')
    started=time.monotonic();request=json.loads(args.request.read_text());stop=threading.Event()
    runtime=dict(phase='starting',body_finished=False,maximum_observed_worker_rss_kb=0)
    record=dict(schema='fd2d-real-nonlinear-tail-query-v1',source=identity(__file__),worker=identity(args.worker),
        config=identity(args.config),request=identity(args.request),request_value=request,
        scope='Actual finite Fourier/depth nonlinear worker response; no infinite-tail or full-surface assertion.')
    def heartbeat():
        while not stop.is_set():
            item=dict(runtime,seconds=time.monotonic()-started,utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
            pid=runtime.get('worker_pid')
            if pid:
                try:
                    status=Path(f'/proc/{pid}/status').read_text().splitlines()
                    item['worker_memory']={line.split(':',1)[0]:line.split(':',1)[1].strip() for line in status if line.startswith(('VmRSS:','VmHWM:','Threads:'))}
                    rss=int(item['worker_memory'].get('VmRSS','0 kB').split()[0])
                    runtime['maximum_observed_worker_rss_kb']=max(runtime['maximum_observed_worker_rss_kb'],rss)
                    item['maximum_observed_worker_rss_kb']=runtime['maximum_observed_worker_rss_kb']
                    stat=Path(f'/proc/{pid}/stat').read_text().split();item['worker_cpu_seconds']=(int(stat[13])+int(stat[14]))/os.sysconf(os.sysconf_names['SC_CLK_TCK'])
                except OSError:pass
            write(stem.with_name(stem.name+'-runtime.json'),item)
            with stem.with_name(stem.name+'-heartbeat.jsonl').open('a') as log:log.write(json.dumps(item)+'\n')
            stop.wait(5.)
    thread=threading.Thread(target=heartbeat,daemon=True);thread.start()
    try:
        with stem.with_name(stem.name+'-stderr.txt').open('w') as stderr:
            env=os.environ.copy();env.pop('NODE_OPTIONS',None)
            command=['node',f'--max-heap-size={args.node_heap_mib}',f'--max-semi-space-size={args.node_semi_space_mib}',str(args.worker.resolve()),str(args.config.resolve())]
            record['actual_worker_command']=command
            process=subprocess.Popen(command,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=stderr,text=True,bufsize=1,env=env)
            runtime.update(worker_pid=process.pid,phase='waiting_ready')
            line=process.stdout.readline()
            if not line:raise RuntimeError(f'Worker EOF before ready; actual return code {process.poll()}')
            ready=json.loads(line);write(stem.with_name(stem.name+'-ready.json'),ready)
            if ready.get('event')!='ready':raise RuntimeError('Worker first record was not ready')
            runtime['phase']='actual_nonlinear_solve'
            process.stdin.write(json.dumps(request)+'\n');process.stdin.flush()
            line=process.stdout.readline()
            if not line:raise RuntimeError(f'Worker EOF before actual response; actual return code {process.poll()}')
            response=json.loads(line);response_path=stem.with_name(stem.name+'-response.json');write(response_path,response)
            record.update(response=identity(response_path),converged=response.get('converged'),residual=response.get('residual'),
                history_count=len(response.get('history',[])),has_actual_height_jet_jacobian=response.get('heightJetJacobian') is not None,
                has_actual_audit=response.get('audit') is not None)
            runtime.update(phase='response_saved',converged=response.get('converged'),residual=response.get('residual'))
            process.stdin.write('{"stop":true}\n');process.stdin.flush();process.stdin.close()
            process.stdout.close();record['worker_returncode']=process.wait()
    except BaseException as exc:
        record['exception']=dict(type=type(exc).__name__,message=str(exc))
        if 'process' in locals():record['worker_returncode_observed']=process.poll()
    finally:
        if 'process' in locals() and process.poll() is None and 'exception' in record:
            record['cleanup_owner_terminated_live_child']=True;process.terminate()
            record['worker_returncode_after_cleanup']=process.wait()
        record['maximum_observed_worker_rss_kb']=runtime['maximum_observed_worker_rss_kb']
        record['seconds']=time.monotonic()-started;write(stem.with_name(stem.name+'-report.json'),record)
        runtime.update(phase='body_completed',body_finished=True);stop.set();thread.join(timeout=1.)
        write(stem.with_name(stem.name+'-runtime.json'),dict(runtime,seconds=time.monotonic()-started,utc=datetime.datetime.now(datetime.timezone.utc).isoformat()))
    print(json.dumps({k:record.get(k) for k in ('converged','residual','history_count','worker_returncode','worker_returncode_observed','exception','seconds')}),flush=True)


if __name__=='__main__':main()
