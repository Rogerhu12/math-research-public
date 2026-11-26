#!/usr/bin/env python3
"""Sequential cold entry for the original M12 TRUE-cuff Cartesian BVP.

All generated data remain in the requested temporary directory. This script
does not publish Git data, artifacts, or releases. Its caller may retain a
small scalar receipt and output SHA values. Numerical scope is the entire
upper half, including the original finite tail and the true deep collar.
"""
import argparse,hashlib,json,os,subprocess,sys,time
from pathlib import Path

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--scripts',type=Path,default=Path(__file__).resolve().parent)
    ap.add_argument('--data',type=Path,required=True);ap.add_argument('--directory',type=Path,required=True)
    ap.add_argument('--prefix-elements',type=int,default=80);ap.add_argument('--tail-elements',type=int,default=64)
    ap.add_argument('--tail-depth',type=int,default=12);ap.add_argument('--order',type=int,default=32)
    ap.add_argument('--angular',type=int,default=384);ap.add_argument('--gauss',type=int,default=6)
    ap.add_argument('--iterations',type=int,default=800);ap.add_argument('--newton',type=int,default=1)
    ap.add_argument('--block',type=int,default=24);args=ap.parse_args()
    args.directory.mkdir(parents=True,exist_ok=True)
    receipt=args.directory/'entire-half-cold-execution.json'
    if receipt.exists():raise FileExistsError('Fresh whole-half cold directory required')
    grid=args.directory/'entire-half-grid.json';queries=Path(str(grid)+'.queries.json')
    tail=args.directory/'entire-half-exact-tail-queries.json';result=args.directory/'entire-half-result.json'
    numerical=args.scripts/'6a65-m12-entire-half-cartesian-bvp.py'
    commands=[
        [sys.executable,str(numerical),'prepare','--scripts',str(args.scripts),'--data',str(args.data),'--out',str(grid),
         '--prefix-elements',str(args.prefix_elements),'--tail-elements',str(args.tail_elements),'--tail-depth',str(args.tail_depth),
         '--order',str(args.order),'--angular',str(args.angular),'--gauss',str(args.gauss)],
        [sys.executable,str(args.scripts/'6a65-m12-stream-tail-query-cache.py'),
         '--manifest',str(args.scripts.parent/'notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json'),
         '--queries',str(queries),'--out',str(tail)],
        [sys.executable,str(numerical),'solve','--scripts',str(args.scripts),'--data',str(args.data),'--out',str(result),
         '--grid',str(grid),'--query-report',str(tail),'--query-cache',str(tail)+'.npz',
         '--iterations',str(args.iterations),'--newton',str(args.newton),'--block',str(args.block)]
    ]
    record={'schema':'6a65-M12-entire-half-cold-execution-v1','script_sha256':sha(__file__),
            'scope':'Original unchanged g from exact central trace through prefix, bridge, finite tail, deep collar to the true flat cuff.',
            'source_data_sha256':sha(args.data),'commands':commands,'stages':[],'finished':False}
    began=time.monotonic()
    for name,command in zip(('prepare','exact-tail-queries','whole-half-solve'),commands):
        start=time.monotonic();print(json.dumps({'stage':name,'status':'starting'}),flush=True)
        child_env=os.environ.copy()
        if name!='exact-tail-queries':child_env.pop('M12_RECOVERY_TOKEN',None)
        child=subprocess.run(command,env=child_env)
        record['stages'].append({'stage':name,'exit_code':child.returncode,'seconds':time.monotonic()-start})
        record['seconds']=time.monotonic()-began
        receipt.write_text(json.dumps(record,indent=2)+'\n')
        if child.returncode:raise SystemExit(child.returncode)
    record['finished']=True
    record['recovery_token_removed_from_numerical_children']=True
    record['result_sha256']=sha(result)
    record['field_sha256']=sha(str(result)+'.field.npz')
    record['grid_sha256']=sha(grid);record['tail_query_report_sha256']=sha(tail)
    record['tail_query_cache_sha256']=sha(str(tail)+'.npz');record['seconds']=time.monotonic()-began
    receipt.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2),flush=True)

if __name__=='__main__':main()
