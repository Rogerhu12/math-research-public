"""Run one owned child and retain observed exit, CPU and resident-memory data."""
import argparse,datetime,hashlib,json,os,resource,subprocess,sys,time
from pathlib import Path


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--receipt',type=Path,required=True)
    ap.add_argument('--sample-period',type=float,default=.5)
    ap.add_argument('argv',nargs=argparse.REMAINDER)
    args=ap.parse_args();argv=args.argv
    if argv and argv[0]=='--':argv=argv[1:]
    if not argv or not .1<=args.sample_period<=5:raise ValueError('Missing command or invalid sample period')
    args.receipt.parent.mkdir(parents=True,exist_ok=True)
    if args.receipt.exists():raise FileExistsError(args.receipt)
    observations=args.receipt.parent/'process-observations'
    observations.mkdir(parents=True,exist_ok=True)
    telemetry=observations/(args.receipt.stem+'-samples.jsonl')
    console=observations/(args.receipt.stem+'-console.txt')
    start=time.monotonic();started=utc();tick=os.sysconf('SC_CLK_TCK')
    peaks={};last=None;limits=None;cgroup=None;samples=0
    with console.open('w') as output,telemetry.open('w') as log:
        proc=subprocess.Popen(argv,stdout=output,stderr=subprocess.STDOUT)
        while True:
            observed=proc.poll()
            if observed is not None:break
            try:
                root=Path('/proc')/str(proc.pid)
                raw={k:v.strip() for k,v in (line.split(':',1) for line in (root/'status').read_text().splitlines() if ':' in line)}
                stats=(root/'stat').read_text().rsplit(')',1)[1].split()
                row={'utc':utc(),'seconds':time.monotonic()-start,'pid':proc.pid,
                     'utime_seconds':int(stats[11])/tick,'stime_seconds':int(stats[12])/tick}
                for key in ('VmRSS','VmHWM','VmSize','VmPeak','RssAnon','RssFile'):
                    if key in raw:
                        row[key+'_KiB']=int(raw[key].split()[0])
                        peaks[key+'_KiB']=max(peaks.get(key+'_KiB',0),row[key+'_KiB'])
                mem={k:v.strip() for k,v in (line.split(':',1) for line in Path('/proc/meminfo').read_text().splitlines() if ':' in line)}
                row['host_MemAvailable_KiB']=int(mem['MemAvailable'].split()[0])
                if limits is None:limits=(root/'limits').read_text();cgroup=(root/'cgroup').read_text()
                log.write(json.dumps(row)+'\n');log.flush();last=row;samples+=1
            except (FileNotFoundError,ProcessLookupError,IndexError,ValueError):
                # /proc can disappear before wait observes the actual exit.
                pass
            time.sleep(args.sample_period)
        code=proc.wait()
    usage=resource.getrusage(resource.RUSAGE_CHILDREN)
    report=dict(schema='fd2d-owned-child-exit-and-resource-observation-v1',
        observer_source=dict(path=str(Path(__file__).resolve()),sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()),
        argv=argv,cwd=str(Path.cwd()),started_utc=started,ended_utc=utc(),
        seconds=time.monotonic()-start,actual_child_returncode=code,
        wrapper_returncode=(code if code>=0 else 128-code),
        child_cpu_seconds=dict(user=usage.ru_utime,system=usage.ru_stime),
        kernel_child_maximum_resident_KiB=usage.ru_maxrss,
        sampled_process_peaks=peaks,last_sample=last,samples=samples,
        observed_child_limits=limits,observed_child_cgroup=cgroup,
        telemetry_path=str(telemetry),console_path=str(console),
        termination_cause='Actual wait return code only; no inferred OOM or time-limit cause')
    args.receipt.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(event='actual_owned_child_exit',receipt=str(args.receipt),
        returncode=code,seconds=report['seconds'],kernel_maxrss_kib=usage.ru_maxrss,
        cpu_seconds=usage.ru_utime+usage.ru_stime)),flush=True)
    return report['wrapper_returncode']


if __name__=='__main__':raise SystemExit(main())
