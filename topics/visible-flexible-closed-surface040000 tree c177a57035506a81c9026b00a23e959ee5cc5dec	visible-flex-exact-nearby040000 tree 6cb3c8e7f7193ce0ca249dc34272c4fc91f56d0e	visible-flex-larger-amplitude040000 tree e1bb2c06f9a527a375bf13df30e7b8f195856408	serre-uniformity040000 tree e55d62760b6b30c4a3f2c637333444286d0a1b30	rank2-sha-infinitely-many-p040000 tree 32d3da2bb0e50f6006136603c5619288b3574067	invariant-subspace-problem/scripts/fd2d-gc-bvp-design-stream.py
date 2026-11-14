#!/usr/bin/env python3
"""Run the unchanged warm finite GC design equations with streaming CSC storage."""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import hashlib,importlib.util,json,resource,sys,threading,time
from pathlib import Path
import scipy
import fd2d_gc_stream_csc as streaming

HERE=Path(__file__).resolve().parent


def main():
    source=HERE/'fd2d-gc-bvp-design-warm.py'
    spec=importlib.util.spec_from_file_location('fd2d_warm_stream_target',source)
    warm=importlib.util.module_from_spec(spec);spec.loader.exec_module(warm)
    args=sys.argv[1:]
    if '--out-prefix' not in args:raise ValueError('The warm runner requires --out-prefix')
    stem=Path(args[args.index('--out-prefix')+1])
    record=stem.parent/'stream-resources'/(stem.name+'.jsonl')
    if record.exists():raise FileExistsError(record)
    record.parent.mkdir(parents=True,exist_ok=True)
    started=time.monotonic();stop=threading.Event()
    sources=[]
    for path in (Path(__file__),source,Path(streaming.__file__)):
        data=path.read_bytes();sources.append(dict(path=str(path.resolve()),sha256=hashlib.sha256(data).hexdigest(),bytes=len(data)))
    def snapshot(event):
        rss={}
        try:
            for line in Path('/proc/self/status').read_text().splitlines():
                key,_,value=line.partition(':')
                if key in ('VmRSS','VmHWM','VmSize','Threads'):rss[key]=value.strip()
        except OSError:pass
        return dict(event=event,utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
            seconds=time.monotonic()-started,pid=os.getpid(),resources=rss,
            maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            streaming=dict(streaming.STATUS),newton=dict(warm.newton.STATS))
    def append(item):
        with record.open('a') as out:out.write(json.dumps(item,allow_nan=False)+'\n')
    def heartbeat():
        while not stop.wait(5.):append(snapshot('heartbeat'))
    thread=threading.Thread(target=heartbeat,daemon=True)
    first=snapshot('start');first.update(scipy_version=scipy.__version__,sources=sources,
        same_collocation_equations=True,all_zero_parameter_columns_asserted=True,
        reduced_mode_count=False,new_math_acceptance_gate=False)
    append(first);streaming.install();thread.start()
    try:warm.main()
    finally:
        stop.set();thread.join(timeout=1.);append(snapshot('wrapper_exit'))
        print(json.dumps(snapshot('stream_wrapper_done')),flush=True)


if __name__=='__main__':main()
