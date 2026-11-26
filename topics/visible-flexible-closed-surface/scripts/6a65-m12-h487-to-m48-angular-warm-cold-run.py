#!/usr/bin/env python3
"""Regenerate h487, then execute one true fixed-g angular warm refinement.

The first field is regenerated in this SAME temporary job from the original
public inputs. Every old radial node and exact tail query is retained.
The next field starts from exact Fourier zero-embedding, not from zero.
All source, whole-domain, observer and continuous-geometry consumers remain.
This is a new source identity; actual execution is separately receipted.
"""
from __future__ import annotations
import argparse,hashlib,json,os,re,shutil,subprocess,sys,time
from pathlib import Path

HERE=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--scripts',type=Path,default=HERE)
    for key in ('data','directory'):ap.add_argument('--'+key,type=Path,required=True)
    for key,value in [('prefix-elements',80),('tail-elements',64),('tail-depth',12),('order',32),
                      ('angular',384),('gauss',6),('iterations',800),('newton',1),('block',24),
                      ('local-element',190),('second-local-element',176),
                      ('warm-order',48),('warm-angular',768),('warm-iterations',800),('warm-newton',1)]:
        ap.add_argument('--'+key,type=int,default=value)
    ap.add_argument('--source-knot-window',nargs=2,default=['.432','.5141'])
    ap.add_argument('--diagnostic-window',nargs=2,action='append')
    ap.add_argument('--expected-base-field-sha256')
    ap.add_argument('--source-transport',choices=('git-blob-api','raw-known-commit'),default='git-blob-api')
    ap.add_argument('--plan-only',action='store_true')
    args=ap.parse_args();began=time.monotonic();args.directory.mkdir(parents=True,exist_ok=True)
    fixed=(args.prefix_elements,args.tail_elements,args.tail_depth,args.order,args.angular,args.gauss,
           args.iterations,args.newton,args.block,args.local_element,args.second_local_element)
    if fixed!=(80,64,12,32,384,6,800,1,24,190,176):
        raise ValueError('This experiment first regenerates the complete declared h487 baseline unchanged')
    if args.source_knot_window!=['.432','.5141']:raise ValueError('Declared h487 source-knot window changed')
    if args.diagnostic_window is None:args.diagnostic_window=[['.432','.436'],['.5122','.5141']]
    if args.diagnostic_window!=[['.432','.436'],['.5122','.5141']]:
        raise ValueError('Both exact original h487 observation windows must remain')
    if args.warm_order!=48 or args.warm_angular!=768 or args.warm_angular%args.angular:
        raise ValueError('This explicit angular refinement is M32 to M48 and N384 to N768')
    if args.warm_iterations<1 or args.warm_newton<1:raise ValueError('Positive actual warm solve budget required')
    if args.expected_base_field_sha256 and not re.fullmatch('[0-9a-f]{64}',args.expected_base_field_sha256):
        raise ValueError('Expected actual h487 field identity must be a SHA256')
    receipt=args.directory/'entire-half-cold-execution.json'
    if receipt.exists():raise FileExistsError('Fresh actual angular-refinement directory required')
    base=args.directory/'h487-base';base.mkdir(exist_ok=True)
    grid=args.directory/'entire-half-grid.json';base_grid=base/'entire-half-grid.json'
    tail=args.directory/'entire-half-exact-tail-queries.json';cache=Path(str(tail)+'.npz')
    source=args.directory/'entire-half-original-source-bounds.json'
    result=args.directory/'entire-half-result.json';field=Path(str(result)+'.field.npz')
    initial_result=Path(str(result)+'.warm-observed.json')
    change=args.directory/'entire-half-continuous-change-bounds.json'
    geometry=args.directory/'entire-half-actual-field-geometry.json'
    observer=args.directory/'entire-half-original-span-observer.json'
    old_union=args.directory/'entire-half-old-observer-union.json'
    warm_micro=args.directory/'entire-half-warm-original-span-observer.json'
    warm_union=args.directory/'entire-half-warm-old-observer-union.json'
    warm=args.directory/'entire-half-warm-transfer.json';warm_field=Path(str(warm)+'.field.npz')
    base_result=base/'entire-half-result.json';base_field=Path(str(base_result)+'.field.npz')
    common=['--scripts',str(args.scripts),'--data',str(args.data)]
    window_flags=[x for pair in args.diagnostic_window for x in ['--diagnostic-window',*pair]]
    new_files=[args.scripts/name for name in (
        '6a65-m12-frequency-only-grid-prepare.py','6a65-m12-frequency-only-warm-transfer.py',
        '6a65-m12-entire-half-cartesian-warm-refinement.py','6a65-m12-frequency-warm-finite-fixture.py')]
    base_common=[*common,'--grid',str(base_grid),'--field',str(base_field),'--result',str(base_result)]
    field_common=[*common,'--grid',str(grid),'--query-report',str(tail),'--query-cache',str(cache)]
    commands=[
      ('compile-new-unexecuted-sources',[sys.executable,'-m','py_compile',*map(str,new_files),str(Path(__file__))]),
      ('finite-nonzero-exact-warm-interface-fixture',[sys.executable,str(new_files[3]),
          '--scripts',str(args.scripts),'--out',str(args.directory/'frequency-interface-finite-check.json')]),
      ('regenerate-h487-whole-half',[sys.executable,str(args.scripts/'6a65-m12-entire-half-two-hotspot-cold-run.py'),
          *common,'--directory',str(base),'--prefix-elements','80','--tail-elements','64','--tail-depth','12',
          '--order','32','--angular','384','--gauss','6','--iterations','800','--newton','1','--block',str(args.block),
          '--local-element','190','--second-local-element','176','--source-knot-window',*args.source_knot_window,
          *window_flags,'--source-transport',args.source_transport]),
      ('regenerated-base-R236-localized-metric',[sys.executable,str(args.scripts/'6a65-m12-local-bernstein-angular-metric-budget.py'),
          *base_common,'--correction-bounds',str(base/'entire-half-continuous-change-bounds.json'),
          '--out',str(base/'entire-half-localized-metric-budget.json')]),
      ('regenerated-base-three-phase-STL',[sys.executable,str(args.scripts/'6a65-m12-entire-half-closed-stl.py'),
          *base_common,'--query-report',str(base/'entire-half-exact-tail-queries.json'),
          '--query-cache',str(base/'entire-half-exact-tail-queries.json.npz'),
          '--geometry-report',str(base/'entire-half-actual-field-geometry.json'),
          '--angular','216','--prefix-intervals','64','--tail-intervals','32',
          '--out',str(base/'entire-half-closed-stl.json')]),
      ('strict-frequency-only-grid',[sys.executable,str(new_files[0]),'--old-grid',str(base_grid),'--out',str(grid),
          '--order',str(args.warm_order),'--angular',str(args.warm_angular)]),
      ('exact-old-field-zero-Fourier-embedding',[sys.executable,str(new_files[1]),
          '--old-grid',str(base_grid),'--old-result',str(base_result),'--old-field',str(base_field),
          '--new-grid',str(grid),'--out',str(warm)]),
      ('actual-complete-angular-warm-solve',[sys.executable,str(new_files[2]),'solve',*common,
          '--grid',str(grid),'--query-report',str(tail),'--query-cache',str(cache),'--out',str(result),
          '--warm-field',str(warm_field),'--warm-receipt',str(warm),
          '--iterations',str(args.warm_iterations),'--newton',str(args.warm_newton),'--block',str(args.block)]),
      ('new-actual-field-R226-continuous-six-jets',[sys.executable,str(args.scripts/'6a65-m12-entire-half-continuous-correction-bounds.py'),
          *common,'--field',str(field),'--grid',str(grid),'--result',str(result),'--out',str(change)]),
      ('new-actual-field-all-phase-geometry',[sys.executable,str(args.scripts/'6a65-m12-entire-half-actual-field-geometry-transfer.py'),
          '--source-bounds',str(source),'--correction-bounds',str(change),'--field',str(field),
          '--grid',str(grid),'--result',str(result),'--out',str(geometry)]),
      ('same-warm-input-two-window-microspan-observer',[sys.executable,str(args.scripts/'6a65-m12-entire-half-multiple-window-observer.py'),
          *field_common,'--field',str(warm_field),'--result',str(initial_result),'--out',str(warm_micro),
          '--block',str(min(args.block,12))]),
      ('same-warm-input-all-ancestor-observer-union',[sys.executable,str(args.scripts/'6a65-m12-entire-half-transitive-observer-union.py'),
          *field_common,'--field',str(warm_field),'--result',str(initial_result),'--out',str(warm_union)]),
      ('new-actual-field-two-window-microspan-observer',[sys.executable,str(args.scripts/'6a65-m12-entire-half-multiple-window-observer.py'),
          *field_common,'--field',str(field),'--result',str(result),'--out',str(observer),
          '--block',str(min(args.block,12))]),
      ('new-actual-field-all-ancestor-observer-union',[sys.executable,str(args.scripts/'6a65-m12-entire-half-transitive-observer-union.py'),
          *field_common,'--field',str(field),'--result',str(result),'--out',str(old_union)])]
    source_paths=set(new_files+[Path(__file__)])
    source_paths.update(Path(command[1]) for name,command in commands if command[1]!='-m')
    record={'schema':'6a65-M12-h487-to-M48-same-job-angular-warm-execution-v1',
        'script_sha256':sha(__file__),'scope':'Same fixed original g and complete true-cuff half; regenerated h487 then exact zero-embedded M48/N768 warm solve on unchanged G6/radial nodes.',
        'source_data_sha256':sha(args.data),'commands':[command for name,command in commands],
        'source_hashes':{p.name:sha(p) for p in sorted(source_paths)},
        'stages':[],'finished':False,'original_metric_unchanged':True,
        'whole_radial_mesh_and_exact_queries_unchanged_between_layers':True,
        'base_reproduction_is_not_new_mathematical_improvement':True,
        'warm_linear_regularization':0.,'prior_actual_h487_run':45833090043,
        'expected_prior_actual_h487_field_sha256':args.expected_base_field_sha256,
        'final_R236_and_STL_required_from_outer_supervisor':True}
    if args.plan_only:
        record['plan_only']=True;record['stage_names']=[name for name,command in commands]
        print(json.dumps(record,indent=2),flush=True);return
    def save():record['seconds']=time.monotonic()-began;receipt.write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
    save()
    for name,command in commands:
        if name=='strict-frequency-only-grid':
            # Only the fixed source/cache is copied. All field-dependent
            # reports are recomputed later for the actual new field.
            copies=[('entire-half-exact-tail-queries.json',tail),
                    ('entire-half-exact-tail-queries.json.npz',cache),
                    ('entire-half-original-source-bounds.json',source)]
            record['unchanged_source_copies']=[]
            for filename,dest in copies:
                original=base/filename
                if dest.exists():raise FileExistsError('Fresh copied fixed-source path required')
                shutil.copyfile(original,dest)
                if sha(original)!=sha(dest):raise ArithmeticError('Fixed source changed during byte copy')
                record['unchanged_source_copies'].append({'source_name':filename,'sha256':sha(dest),
                    'field_dependent':False})
            actual_base_sha=sha(base_field)
            record['actual_regenerated_base_field_sha256']=actual_base_sha
            record['base_field_matches_prior_actual_bytes']=(actual_base_sha==args.expected_base_field_sha256
                if args.expected_base_field_sha256 else None)
            record['base_comparison_uses_this_jobs_actual_field_only']=True
        started=time.monotonic();print(json.dumps({'stage':name,'status':'starting'}),flush=True)
        env={k:v for k,v in os.environ.items() if k not in ('GITHUB_TOKEN','GH_TOKEN')}
        if name!='regenerate-h487-whole-half':env.pop('M12_RECOVERY_TOKEN',None)
        child=subprocess.run(command,env=env)
        record['stages'].append({'stage':name,'exit_code':child.returncode,'seconds':time.monotonic()-started})
        save()
        if child.returncode:raise SystemExit(child.returncode)
    for key,path in [('result',result),('field',field),('grid',grid),('tail_query_report',tail),('tail_query_cache',cache),
        ('continuous_original_source',source),('continuous_actual_change',change),('actual_field_geometry',geometry),
        ('original_microspan_observer',observer),('old_observer_union',old_union),('warm_transfer',warm),
        ('warm_field',warm_field),('warm_observed_result',initial_result),('warm_microspan_observer',warm_micro),
        ('warm_observer_union',warm_union),('base_result',base_result),('base_field',base_field),('base_grid',base_grid)]:
        record[key+'_sha256']=sha(path)
    new_grid=json.loads(grid.read_text());old_grid=json.loads(base_grid.read_text())
    if new_grid['unit_mesh']!=old_grid['unit_mesh'] or new_grid['query_file_sha256']!=old_grid['query_file_sha256']:
        raise ArithmeticError('The actual angular refinement changed radial mesh or exact queries')
    record['actual_elements']=len(new_grid['unit_mesh'])-1
    record['actual_angular_orders']=[old_grid['order'],new_grid['order']]
    record['actual_training_angles']=[old_grid['angular'],new_grid['angular']]
    record['actual_independent_angles']=[2*old_grid['angular'],2*new_grid['angular']]
    record['actual_training_Gauss_orders']=[old_grid['gauss'],new_grid['gauss']]
    record['source_recovery_token_removed_from_all_numerical_children']=True
    record['scalar_report_files']=[p.name for p in (source,result,change,geometry,observer,old_union,warm,initial_result,warm_micro,warm_union)]
    record['base_scalar_report_directory']=base.name
    record['base_scalar_report_files']=['entire-half-cold-execution.json','entire-half-result.json',
        'entire-half-continuous-change-bounds.json','entire-half-actual-field-geometry.json',
        'entire-half-original-span-observer.json','entire-half-old-observer-union.json',
        'entire-half-closed-stl.json','entire-half-localized-metric-budget.json']
    record['finished']=True;save();print(json.dumps(record,indent=2,allow_nan=False),flush=True)
if __name__=='__main__':main()
