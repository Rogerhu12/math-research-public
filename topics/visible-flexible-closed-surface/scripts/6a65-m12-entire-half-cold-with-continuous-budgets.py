#!/usr/bin/env python3
"""Original-g whole-half cold run with continuous source and field budgets.

This successor keeps the original whole-half numerical solver. Before the
solve it certifies the original source two-jets; after the solve the same
saved field is consumed by R226, the all-phase geometry transfer, and an
original-Hermite-microspan observer. All raw arrays stay in the caller's
temporary directory. The caller publishes only small scalar reports.
"""
from __future__ import annotations
import argparse,hashlib,json,os,subprocess,sys,time
from pathlib import Path

HERE=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--scripts',type=Path,default=HERE)
    ap.add_argument('--data',type=Path,required=True);ap.add_argument('--directory',type=Path,required=True)
    ap.add_argument('--prefix-elements',type=int,default=80);ap.add_argument('--tail-elements',type=int,default=64)
    ap.add_argument('--tail-depth',type=int,default=12);ap.add_argument('--order',type=int,default=32)
    ap.add_argument('--angular',type=int,default=384);ap.add_argument('--gauss',type=int,default=6)
    ap.add_argument('--iterations',type=int,default=800);ap.add_argument('--newton',type=int,default=1)
    ap.add_argument('--block',type=int,default=24)
    ap.add_argument('--source-transport',choices=('git-blob-api','raw-known-commit'),default='git-blob-api')
    ap.add_argument('--diagnostic-window',nargs=2,default=['.432','.436'])
    ap.add_argument('--diagnostic-subdivisions',type=int,default=4)
    args=ap.parse_args();args.directory.mkdir(parents=True,exist_ok=True)
    receipt=args.directory/'entire-half-cold-execution.json'
    if receipt.exists():raise FileExistsError('Fresh budgeted whole-half directory required')
    grid=args.directory/'entire-half-grid.json';queries=Path(str(grid)+'.queries.json')
    tail=args.directory/'entire-half-exact-tail-queries.json';cache=Path(str(tail)+'.npz')
    source=args.directory/'entire-half-original-source-bounds.json'
    result=args.directory/'entire-half-result.json';field=Path(str(result)+'.field.npz')
    change=args.directory/'entire-half-continuous-change-bounds.json'
    geometry=args.directory/'entire-half-actual-field-geometry.json'
    observer=args.directory/'entire-half-original-span-observer.json'
    numerical=args.scripts/'6a65-m12-entire-half-cartesian-bvp.py'
    common=['--scripts',str(args.scripts),'--data',str(args.data)]
    commands=[
        ('prepare',[sys.executable,str(numerical),'prepare',*common,'--out',str(grid),
          '--prefix-elements',str(args.prefix_elements),'--tail-elements',str(args.tail_elements),
          '--tail-depth',str(args.tail_depth),'--order',str(args.order),'--angular',str(args.angular),
          '--gauss',str(args.gauss)]),
        ('exact-tail-queries-and-continuous-source',[sys.executable,str(HERE/'6a65-m12-stream-tail-query-and-source-bounds-recovered.py'),
          '--manifest',str(args.scripts.parent/'notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json'),
          '--endpoint-producer',str(args.scripts/'6a65-m12-stream-tail-exact-endpoint.py'),
          '--queries',str(queries),'--out',str(tail),'--source-transport',args.source_transport,
          '--diagnostic-window',*args.diagnostic_window,'--diagnostic-subdivisions',str(args.diagnostic_subdivisions)]),
        ('continuous-prefix-and-entire-source',[sys.executable,str(HERE/'6a65-m12-original-common-cut-prefix-source-bounds.py'),
          *common,'--tail-report',str(tail),'--tail-cache',str(cache),'--out',str(source)]),
        ('whole-half-solve',[sys.executable,str(numerical),'solve',*common,'--out',str(result),
          '--grid',str(grid),'--query-report',str(tail),'--query-cache',str(cache),
          '--iterations',str(args.iterations),'--newton',str(args.newton),'--block',str(args.block)]),
        ('R226-actual-field-continuous-six-jets',[sys.executable,str(args.scripts/'6a65-m12-entire-half-continuous-correction-bounds.py'),
          *common,'--field',str(field),'--grid',str(grid),'--result',str(result),'--out',str(change)]),
        ('actual-field-all-phase-geometry-transfer',[sys.executable,str(HERE/'6a65-m12-entire-half-actual-field-geometry-transfer.py'),
          '--source-bounds',str(source),'--correction-bounds',str(change),'--field',str(field),'--grid',str(grid),
          '--result',str(result),'--out',str(geometry)]),
        ('actual-field-original-microspan-observer',[sys.executable,str(HERE/'6a65-m12-entire-half-original-span-observer.py'),
          *common,'--grid',str(grid),'--query-report',str(tail),'--query-cache',str(cache),
          '--field',str(field),'--result',str(result),'--out',str(observer),'--block',str(min(args.block,12))])
    ]
    record={'schema':'6a65-M12-entire-half-cold-continuous-budget-execution-v2','script_sha256':sha(__file__),
            'scope':'The same original fixed g, complete half through the true cuff; source C_X, actual field six jets, all-phase transfer and microspan observer.',
            'source_data_sha256':sha(args.data),'commands':[command for name,command in commands],
            'source_hashes':{Path(command[1]).name:sha(command[1]) for name,command in commands},
            'stages':[],'finished':False}
    record['source_hashes']['6a65-m12-tail-polynomial-continuous-bounds-recovered.py']=sha(HERE/'6a65-m12-tail-polynomial-continuous-bounds-recovered.py')
    began=time.monotonic()
    for name,command in commands:
        started=time.monotonic();print(json.dumps({'stage':name,'status':'starting'}),flush=True)
        child_env=os.environ.copy()
        if name!='exact-tail-queries-and-continuous-source':child_env.pop('M12_RECOVERY_TOKEN',None)
        child=subprocess.run(command,env=child_env)
        record['stages'].append({'stage':name,'exit_code':child.returncode,'seconds':time.monotonic()-started})
        record['seconds']=time.monotonic()-began
        receipt.write_text(json.dumps(record,indent=2)+'\n')
        if child.returncode:raise SystemExit(child.returncode)
    record['finished']=True;record['recovery_token_removed_from_numerical_children']=True
    for key,path in [('result',result),('field',field),('grid',grid),('tail_query_report',tail),('tail_query_cache',cache),
                     ('continuous_original_source',source),('continuous_actual_change',change),
                     ('actual_field_geometry',geometry),('original_microspan_observer',observer)]:
        record[key+'_sha256']=sha(path)
    record['scalar_report_files']=[p.name for p in (source,result,change,geometry,observer)]
    record['seconds']=time.monotonic()-began
    receipt.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2),flush=True)
if __name__=='__main__':main()

