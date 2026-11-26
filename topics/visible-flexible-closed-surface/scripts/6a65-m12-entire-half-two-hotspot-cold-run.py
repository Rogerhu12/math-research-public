#!/usr/bin/env python3
"""Original fixed-g cold run refining both measured tail hotspots.

The original element190 source-aligned refinement is retained. Its actual
whole-field successor moved the global peak to original element176, so this
entry inserts that element's original source knots too. All ancestor G8
observers and all ancestor exact query radii survive. Two disjoint exact
source-span windows are observed separately; the gap is not relabeled as
observed. Complete geometry checks and the underlying solver are unchanged.

Raw arrays remain only in the caller's temporary directory. This entry
executes finite numerical work and does not assert an exact isometry.
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
    ap.add_argument('--local-element',type=int,default=190)
    ap.add_argument('--second-local-element',type=int,default=176)
    ap.add_argument('--minimum-new-knot-separation',type=float,default=1e-12)
    ap.add_argument('--plan-only',action='store_true',help='Print the source-pinned command graph without executing stages')
    ap.add_argument('--source-transport',choices=('git-blob-api','raw-known-commit'),default='git-blob-api')
    ap.add_argument('--diagnostic-window',nargs=2,action='append')
    ap.add_argument('--source-knot-window',nargs=2,default=['.432','.5141'])
    ap.add_argument('--diagnostic-subdivisions',type=int,default=4)
    args=ap.parse_args();args.directory.mkdir(parents=True,exist_ok=True)
    if args.diagnostic_window is None:args.diagnostic_window=[['.432','.436'],['.5122','.5141']]
    if args.local_element!=190 or args.second_local_element!=176:
        raise ValueError('This measured comparison uses the declared 190 then 176 element sequence')
    window_flags=[x for pair in args.diagnostic_window for x in ['--diagnostic-window',*pair]]
    receipt=args.directory/'entire-half-cold-execution.json'
    if receipt.exists():raise FileExistsError('Fresh budgeted whole-half directory required')
    grid=args.directory/'entire-half-grid.json';queries=Path(str(grid)+'.queries.json')
    base_grid=args.directory/'entire-half-base-grid.json';local_knots=args.directory/'entire-half-original-local-knots.json'
    first_grid=args.directory/'entire-half-first-h-grid.json'
    tail=args.directory/'entire-half-exact-tail-queries.json';cache=Path(str(tail)+'.npz')
    source=args.directory/'entire-half-original-source-bounds.json'
    result=args.directory/'entire-half-result.json';field=Path(str(result)+'.field.npz')
    change=args.directory/'entire-half-continuous-change-bounds.json'
    geometry=args.directory/'entire-half-actual-field-geometry.json'
    observer=args.directory/'entire-half-original-span-observer.json'
    old_union=args.directory/'entire-half-old-observer-union.json'
    numerical=args.scripts/'6a65-m12-entire-half-cartesian-bvp.py'
    common=['--scripts',str(args.scripts),'--data',str(args.data)]
    commands=[
        ('prepare-base-grid',[sys.executable,str(numerical),'prepare',*common,'--out',str(base_grid),
          '--prefix-elements',str(args.prefix_elements),'--tail-elements',str(args.tail_elements),
          '--tail-depth',str(args.tail_depth),'--order',str(args.order),'--angular',str(args.angular),
          '--gauss',str(args.gauss)]),
        ('recover-original-local-knots',[sys.executable,str(args.scripts/'6a65-m12-original-tail-local-knot-suffix.py'),
          '--scripts',str(args.scripts),
          '--manifest',str(args.scripts.parent/'notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json'),
          '--out',str(local_knots),'--window',*args.source_knot_window,'--source-transport',args.source_transport]),
        ('retain-first-hotspot-source-knot-h-refinement',[sys.executable,str(args.scripts/'6a65-m12-entire-half-local-source-knot-prepare.py'),
          *common,'--base-grid',str(base_grid),'--suffix-knots',str(local_knots),'--out',str(first_grid),
          '--element',str(args.local_element),'--minimum-new-knot-separation',str(args.minimum_new_knot_separation)]),
        ('second-hotspot-transitive-h-refinement',[sys.executable,str(HERE/'6a65-m12-transitive-source-knot-refinement.py'),
          *common,'--base-grid',str(first_grid),'--suffix-knots',str(local_knots),'--out',str(grid),
          '--element',str(args.second_local_element),'--minimum-new-knot-separation',str(args.minimum_new_knot_separation)]),
        ('exact-tail-queries-and-continuous-source',[sys.executable,str(HERE/'6a65-m12-stream-tail-multiple-diagnostic-windows.py'),
          '--manifest',str(args.scripts.parent/'notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json'),
          '--endpoint-producer',str(args.scripts/'6a65-m12-stream-tail-exact-endpoint.py'),
          '--queries',str(queries),'--out',str(tail),'--source-transport',args.source_transport,
          *window_flags,'--diagnostic-subdivisions',str(args.diagnostic_subdivisions)]),
        ('continuous-prefix-and-entire-source',[sys.executable,str(args.scripts/'6a65-m12-original-common-cut-prefix-source-bounds.py'),
          *common,'--tail-report',str(tail),'--tail-cache',str(cache),'--out',str(source)]),
        ('whole-half-solve',[sys.executable,str(numerical),'solve',*common,'--out',str(result),
          '--grid',str(grid),'--query-report',str(tail),'--query-cache',str(cache),
          '--iterations',str(args.iterations),'--newton',str(args.newton),'--block',str(args.block)]),
        ('R226-actual-field-continuous-six-jets',[sys.executable,str(args.scripts/'6a65-m12-entire-half-continuous-correction-bounds.py'),
          *common,'--field',str(field),'--grid',str(grid),'--result',str(result),'--out',str(change)]),
        ('actual-field-all-phase-geometry-transfer',[sys.executable,str(args.scripts/'6a65-m12-entire-half-actual-field-geometry-transfer.py'),
          '--source-bounds',str(source),'--correction-bounds',str(change),'--field',str(field),'--grid',str(grid),
          '--result',str(result),'--out',str(geometry)]),
        ('actual-field-two-window-original-microspan-observer',[sys.executable,str(HERE/'6a65-m12-entire-half-multiple-window-observer.py'),
          *common,'--grid',str(grid),'--query-report',str(tail),'--query-cache',str(cache),
          '--field',str(field),'--result',str(result),'--out',str(observer),'--block',str(min(args.block,12))]),
        ('all-ancestor-independent-observer-preserving-union',[sys.executable,str(HERE/'6a65-m12-entire-half-transitive-observer-union.py'),
          *common,'--grid',str(grid),'--query-report',str(tail),'--query-cache',str(cache),
          '--field',str(field),'--result',str(result),'--out',str(old_union)])
    ]
    record={'schema':'6a65-M12-entire-half-two-hotspot-transitive-h-cold-execution-v2','script_sha256':sha(__file__),
            'scope':'Source-aligned h insertion in original element190 and successor element176; fixed original g, whole true-cuff domain, all ancestor knots, exact query radii and independent observers retained.',
            'source_data_sha256':sha(args.data),'commands':[command for name,command in commands],
            'source_hashes':{Path(command[1]).name:sha(command[1]) for name,command in commands},
            'stages':[],'finished':False}
    record['source_hashes']['6a65-m12-tail-polynomial-continuous-bounds-recovered.py']=sha(args.scripts/'6a65-m12-tail-polynomial-continuous-bounds-recovered.py')
    if args.plan_only:
        record['plan_only']=True
        record['stage_names']=[name for name,command in commands]
        print(json.dumps(record,indent=2),flush=True)
        return
    began=time.monotonic()
    for name,command in commands:
        started=time.monotonic();print(json.dumps({'stage':name,'status':'starting'}),flush=True)
        child_env={k:v for k,v in os.environ.items() if k not in ('GITHUB_TOKEN','GH_TOKEN')}
        if name not in ('exact-tail-queries-and-continuous-source','recover-original-local-knots'):child_env.pop('M12_RECOVERY_TOKEN',None)
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
    record['base_grid_sha256']=sha(base_grid);record['first_h_grid_sha256']=sha(first_grid)
    record['original_local_knots_sha256']=sha(local_knots)
    record['old_observer_union_sha256']=sha(old_union)
    record['scalar_report_files']=[p.name for p in (source,result,change,geometry,observer,old_union)]
    record['seconds']=time.monotonic()-began
    receipt.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2),flush=True)
if __name__=='__main__':main()

