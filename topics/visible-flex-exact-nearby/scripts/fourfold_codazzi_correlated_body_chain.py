#!/usr/bin/env python3
"""Run disjoint, bounded complete radial-polynomial parts of the true body.

Already completed actual cells are consumed by identity, not recomputed.
Every child has its own complete process record and checkpoint native.
No worker result is promoted to a complete body or inverse certificate.
"""
from __future__ import annotations
import argparse,datetime,gzip,hashlib,json,os,resource,subprocess,sys,time
from pathlib import Path


def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest()


def read(p):
    b=Path(p).read_bytes();return json.loads(gzip.decompress(b) if b[:2]==b'\x1f\x8b' else b)


def save(p,d):
    q=Path(str(p)+'.tmp');q.write_text(json.dumps(d,indent=2,allow_nan=False)+'\n');q.replace(p)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for n in ('candidate','mean','response','adjoint'):ap.add_argument('--'+n,type=Path,required=True)
    ap.add_argument('--first',type=int,required=True);ap.add_argument('--end',type=int,required=True)
    ap.add_argument('--batch',type=int,default=256)
    ap.add_argument('--already',type=Path,nargs='*',default=[])
    ap.add_argument('--work',type=Path,required=True)
    ap.add_argument('--address-space-mib',type=int,default=1792)
    args=ap.parse_args()
    if not 0<=args.first<args.end<=7721 or args.batch<1 or args.address_space_mib<768:
        raise ValueError('valid genuine full-body ranges and resource cap required')
    args.work.mkdir(parents=True,exist_ok=True);plan=args.work/'chain.json'
    if plan.exists():raise FileExistsError('use a new explicit continuation directory')
    producer=Path(__file__).with_name('fourfold_codazzi_correlated_head_residual_rows.py').resolve()
    producer_hash=sha(producer);occupied=[];known=[];reference=None
    for p in args.already:
        d=read(p)
        if (d.get('kind')!='actual_full_regular_joint_radial_polynomial_residual_rows_v1'
            or not d.get('selected_cells_complete') or d.get('failure') is not None
            or d['source_sha256']!=producer_hash):
            raise ValueError('only complete actual same-producer polynomial cells may be skipped')
        if reference is None:reference=d['identity']
        if d['identity']!=reference:raise ValueError('the supplied completed cells have different actual inputs')
        for name in ('candidate','mean','response','adjoint'):
            path=getattr(args,name)
            if d['identity']['original_inputs'].get(str(path))!=sha(path):
                raise ValueError('a supplied completed cell belongs to a different full input')
        for name,h in d['identity']['dependencies'].items():
            if sha(producer.with_name(name))!=h:raise ValueError('a completed-cell dependency changed')
        lo,hi=d['selected_indices']
        if len(d['rows'])!=hi-lo or [r['common_row'] for r in d['rows']]!=list(range(lo,hi)):
            raise ValueError('the completed native is not its full declared cell range')
        known.append(dict(path=str(p),sha256=sha(p),indices=[lo,hi]))
        if args.first<=lo<hi<=args.end:occupied.append((lo,hi))
        elif lo<args.end and hi>args.first:raise ValueError('a completed native cannot be partially skipped')
    occupied.sort();cuts=[];at=args.first
    for lo,hi in occupied+[(args.end,args.end)]:
        if lo<at:raise ValueError('completed actual row ranges overlap')
        while at<lo:
            end=min(lo,at+args.batch);cuts.append((at,end));at=end
        at=hi
    doc=dict(kind='bounded_disjoint_correlated_body_process_chain',complete=False,
        scientific_body_certificate=False,first=args.first,end=args.end,
        producer=str(producer),producer_sha256=producer_hash,
        source_sha256=sha(__file__),already_complete=known,planned_ranges=[list(x) for x in cuts],
        actual_processes=[],address_space_MiB=args.address_space_mib)
    save(plan,doc)
    env=os.environ.copy();env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
    for lo,hi in cuts:
        if sha(producer)!=producer_hash:raise ValueError('the actual producer changed during this chain')
        name=f'rows-{lo:05d}-{hi:05d}';native=args.work/(name+'-native.json.gz')
        process=args.work/(name+'-process.json');log=args.work/(name+'.log')
        if native.exists() or process.exists():raise FileExistsError('preserve every actual earlier piece')
        cmd=[sys.executable,'-u',str(producer)]
        for n in ('candidate','mean','response','adjoint'):cmd+=['--'+n,str(getattr(args,n))]
        cmd+=['--first',str(lo),'--count',str(hi-lo),'--out',str(native)]
        tick=time.monotonic();p=dict(command=cmd,cwd=os.getcwd(),source_sha256=producer_hash,
            started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),state='started',
            address_space_MiB=args.address_space_mib,indices=[lo,hi])
        save(process,p)
        def limit():
            amount=args.address_space_mib*1024**2;resource.setrlimit(resource.RLIMIT_AS,(amount,amount))
        with log.open('w') as stream:
            child=subprocess.Popen(cmd,stdout=stream,stderr=subprocess.STDOUT,env=env,preexec_fn=limit)
            code=child.wait()
        p.update(state='finished',actual_returncode=code,wall_seconds=time.monotonic()-tick,
            maximum_child_RSS_KiB=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
            finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
        if native.exists():p['saved_native_sha256']=sha(native)
        save(process,p);doc['actual_processes'].append(dict(path=str(process),sha256=sha(process)))
        save(plan,doc);print(dict(indices=[lo,hi],actual_returncode=code,seconds=p['wall_seconds']),flush=True)
        if code:raise SystemExit(1)
        d=read(native)
        if not d['selected_cells_complete'] or d['failure'] is not None:
            raise ValueError('a normal process exit did not complete its actual selected cells')
    doc['complete']=True;doc['complete_scope']='the explicitly selected process ranges only; global cover is checked by the separate mean-error consumer';save(plan,doc)


if __name__=='__main__':main()
