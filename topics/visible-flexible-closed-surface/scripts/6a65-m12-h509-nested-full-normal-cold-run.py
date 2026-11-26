#!/usr/bin/env python3
"""Regenerate actual h487, then consume its certified nested h509/M48 field.

The original fixed g, entire true-cuff half, source and every ancestor
observer remain. The third measured hotspot is h487 element 240 (original
base 181). Its exact original source nodes enlarge the simple radial mesh.
The actual old field is inserted exactly before one receipted binary save.
New radial source queries are actually recovered, not borrowed from an old
cache. No returned or unreturned field from another Actions job is needed.
"""
from __future__ import annotations
import argparse,hashlib,json,math,os,re,subprocess,sys,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
BASE_WINDOWS=[['.432','.436'],['.5122','.5141']]
WINDOWS=BASE_WINDOWS+[['.4881','.4948']]
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):return json.loads(Path(path).read_text())

def verify_ancestor_source(base,grid,tail,cache):
    """Compare actual source queries, endpoints and old windows in this job."""
    oldgrid=read(base/'entire-half-grid.json');newgrid=read(grid)
    oldrecipe=Path(str(base/'entire-half-grid.json')+'.queries.json')
    newrecipe=Path(str(grid)+'.queries.json')
    if sha(oldrecipe)!=oldgrid['query_file_sha256'] or sha(newrecipe)!=newgrid['query_file_sha256']:
        raise ValueError('An actual query recipe changed')
    oq,nq=read(oldrecipe),read(newrecipe)
    oldr={Q(v) for v in oq['radii']};newr={Q(v) for v in nq['radii']}
    if not oldr<=newr:raise ValueError('Old exact query radii were lost')
    if not set(oldgrid['unit_mesh'])<=set(newgrid['unit_mesh']):
        raise ValueError('Old material grid nodes were lost')
    oldreport=read(base/'entire-half-exact-tail-queries.json');newreport=read(tail)
    for j in range(2):
        a=oldreport['diagnostic_groups'][j];b=newreport['diagnostic_groups'][j]
        if a['points']!=b['points'] or a['exact_point_source_sha256']!=b['exact_point_source_sha256']:
            raise ValueError('An old exact diagnostic-window point set changed')
    if len(newreport['diagnostic_groups'])!=3:
        raise ValueError('All three separate diagnostic windows are required')
    with np.load(base/'entire-half-exact-tail-queries.json.npz',allow_pickle=False) as a, np.load(cache,allow_pickle=False) as b:
        oldkeys=list(map(str,a['query_fraction']));newkeys=list(map(str,b['query_fraction']))
        lookup={v:j for j,v in enumerate(newkeys)}
        if len(lookup)!=len(newkeys) or any(v not in lookup for v in oldkeys):
            raise ValueError('An actual old cache query disappeared')
        before=a['coefficients'];after=b['coefficients']
        for start in range(0,len(oldkeys),64):
            stop=min(len(oldkeys),start+64)
            ids=[lookup[v] for v in oldkeys[start:stop]]
            if not np.array_equal(before[start:stop],after[ids]):
                raise ValueError('Common exact-source cached six-jet coefficients changed')
        for key in ('endpoint_numerator','endpoint_denominator','first','second','planar_modes','height_modes'):
            if not np.array_equal(a[key],b[key]):raise ValueError('Original source endpoint or mode changed: '+key)
        olddiag=list(map(str,a['diagnostic_fraction']));newdiag=list(map(str,b['diagnostic_fraction']))
        dl={v:j for j,v in enumerate(newdiag)}
        if any(v not in dl for v in olddiag):raise ValueError('An old original-span diagnostic radius disappeared')
        if not np.array_equal(a['diagnostic_coefficients'],b['diagnostic_coefficients'][[dl[v] for v in olddiag]]):
            raise ValueError('Old microspan source coefficients changed')
    return {'old_exact_queries':len(oldr),'new_exact_queries':len(newr),
        'old_elements':len(oldgrid['unit_mesh'])-1,'new_elements':len(newgrid['unit_mesh'])-1,
        'old_knots_and_all_exact_queries_retained':True,
        'actual_cached_common_source_two_jets_equal':True,
        'old_two_exact_window_point_sets_and_source_values_retained':True,
        'old_query_recipe_sha256':sha(oldrecipe),'new_query_recipe_sha256':sha(newrecipe),
        'same_original_source_endpoint_and_modes':True}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--scripts',type=Path,default=HERE)
    for key in ('data','directory'):ap.add_argument('--'+key,type=Path,required=True)
    for key,value in [('prefix-elements',80),('tail-elements',64),('tail-depth',12),('order',32),
                      ('angular',384),('gauss',6),('iterations',800),('newton',1),('block',24),
                      ('local-element',190),('second-local-element',176),('third-local-element',240),
                      ('warm-order',48),('warm-angular',768),('warm-iterations',800),('warm-newton',1)]:
        ap.add_argument('--'+key,type=int,default=value)
    ap.add_argument('--preconditioner-eta',type=float,default=1e-6)
    ap.add_argument('--normal-assembly-block',type=int,default=8)
    ap.add_argument('--source-knot-window',nargs=2,default=['.432','.5141'])
    ap.add_argument('--diagnostic-window',nargs=2,action='append')
    ap.add_argument('--expected-base-field-sha256')
    ap.add_argument('--source-transport',choices=('git-blob-api','raw-known-commit'),default='git-blob-api')
    ap.add_argument('--plan-only',action='store_true')
    args=ap.parse_args();began=time.monotonic();args.directory.mkdir(parents=True,exist_ok=True)
    fixed=(args.prefix_elements,args.tail_elements,args.tail_depth,args.order,args.angular,args.gauss,
           args.iterations,args.newton,args.block,args.local_element,args.second_local_element,args.third_local_element)
    if fixed!=(80,64,12,32,384,6,800,1,24,190,176,240):
        raise ValueError('The declared same-job h487 baseline and third source-knot element must remain fixed')
    if args.source_knot_window!=['.432','.5141']:raise ValueError('Original local source-knot recovery window changed')
    if args.diagnostic_window is None:args.diagnostic_window=WINDOWS
    if args.diagnostic_window!=WINDOWS:raise ValueError('The two old windows and new third hotspot window are required')
    if (args.warm_order,args.warm_angular)!=(48,768):
        raise ValueError('This explicit nested layer uses M48/N768')
    if not math.isfinite(args.preconditioner_eta) or args.preconditioner_eta<=0 or args.normal_assembly_block<1:
        raise ValueError('Positive finite right-preconditioner eta and assembly block required')
    if args.warm_iterations<1 or args.warm_newton<1:raise ValueError('Positive actual warm solve budget required')
    if args.expected_base_field_sha256 and not re.fullmatch('[0-9a-f]{64}',args.expected_base_field_sha256):
        raise ValueError('Historical h487 comparison identity must be a SHA256')
    receipt=args.directory/'entire-half-cold-execution.json'
    if receipt.exists():raise FileExistsError('Fresh actual nested-refinement directory required')
    base=args.directory/'h487-base';base.mkdir(exist_ok=True)
    base_grid=base/'entire-half-grid.json';base_result=base/'entire-half-result.json'
    base_field=Path(str(base_result)+'.field.npz')
    hgrid=args.directory/'entire-half-radial-grid.json';grid=args.directory/'entire-half-grid.json'
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
    common=['--scripts',str(args.scripts),'--data',str(args.data)]
    base_windows=[x for pair in BASE_WINDOWS for x in ['--diagnostic-window',*pair]]
    windows=[x for pair in WINDOWS for x in ['--diagnostic-window',*pair]]
    names=('6a65-m12-exact-radial-angular-warm-transfer.py',
        '6a65-m12-radial-angular-transfer-finite-check.py',
        '6a65-m12-entire-half-nested-warm-refinement.py',
        '6a65-m12-full-normal-nested-warm-refinement.py',
        '6a65-m12-complete-gram-normal-preconditioner.py','6a65-cartesian-complete-radial-normal.py',
        '6a65-m12-frequency-only-grid-prepare.py','6a65-m12-transitive-source-knot-refinement.py')
    sources=[args.scripts/name for name in names]
    base_common=[*common,'--grid',str(base_grid),'--field',str(base_field),'--result',str(base_result)]
    field_common=[*common,'--grid',str(grid),'--query-report',str(tail),'--query-cache',str(cache)]
    commands=[
      ('compile-nested-execution-sources',[sys.executable,'-m','py_compile',*map(str,sources),str(Path(__file__))]),
      ('finite-nonzero-nested-transfer-storage-six-jets',[sys.executable,str(sources[1]),
          '--scripts',str(args.scripts),'--out',str(args.directory/'nested-interface-finite-check.json')]),
      ('regenerate-h487-whole-half',[sys.executable,str(args.scripts/'6a65-m12-entire-half-two-hotspot-cold-run.py'),
          *common,'--directory',str(base),'--prefix-elements','80','--tail-elements','64','--tail-depth','12',
          '--order','32','--angular','384','--gauss','6','--iterations','800','--newton','1','--block',str(args.block),
          '--local-element','190','--second-local-element','176','--source-knot-window',*args.source_knot_window,
          *base_windows,'--source-transport',args.source_transport]),
      ('regenerated-base-R236-localized-metric',[sys.executable,str(args.scripts/'6a65-m12-local-bernstein-angular-metric-budget.py'),
          *base_common,'--correction-bounds',str(base/'entire-half-continuous-change-bounds.json'),
          '--out',str(base/'entire-half-localized-metric-budget.json')]),
      ('regenerated-base-three-phase-STL',[sys.executable,str(args.scripts/'6a65-m12-entire-half-closed-stl.py'),
          *base_common,'--query-report',str(base/'entire-half-exact-tail-queries.json'),
          '--query-cache',str(base/'entire-half-exact-tail-queries.json.npz'),
          '--geometry-report',str(base/'entire-half-actual-field-geometry.json'),
          '--angular','216','--prefix-intervals','64','--tail-intervals','32',
          '--out',str(base/'entire-half-closed-stl.json')]),
      ('third-hotspot-transitive-source-knot-refinement',[sys.executable,str(sources[7]),
          *common,'--base-grid',str(base_grid),'--suffix-knots',str(base/'entire-half-original-local-knots.json'),
          '--out',str(hgrid),'--element','240','--minimum-new-knot-separation','1e-12']),
      ('retain-h509-radial-queries-and-expand-M48',[sys.executable,str(sources[6]),
          '--old-grid',str(hgrid),'--out',str(grid),'--order','48','--angular','768']),
      ('exact-nested-transfer-with-actual-binary-storage-budget',[sys.executable,str(sources[0]),
          '--scripts',str(args.scripts),'--old-grid',str(base_grid),'--old-result',str(base_result),
          '--old-field',str(base_field),'--old-correction-bounds',str(base/'entire-half-continuous-change-bounds.json'),
          '--new-grid',str(grid),'--out',str(warm)]),
      ('recover-new-exact-tail-queries-and-all-three-source-windows',[sys.executable,
          str(args.scripts/'6a65-m12-stream-tail-multiple-diagnostic-windows.py'),
          '--manifest',str(args.scripts.parent/'notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json'),
          '--endpoint-producer',str(args.scripts/'6a65-m12-stream-tail-exact-endpoint.py'),
          '--queries',str(Path(str(grid)+'.queries.json')),'--out',str(tail),
          '--source-transport',args.source_transport,*windows,'--diagnostic-subdivisions','4']),
      ('continuous-original-source-bound-with-new-query-identity',[sys.executable,
          str(args.scripts/'6a65-m12-original-common-cut-prefix-source-bounds.py'),
          *common,'--tail-report',str(tail),'--tail-cache',str(cache),'--out',str(source)]),
      ('actual-complete-normal-h509-M48-nested-warm-solve',[sys.executable,str(sources[3]),'solve',*common,
          '--preconditioner-eta',str(args.preconditioner_eta),'--normal-assembly-block',str(args.normal_assembly_block),
          '--grid',str(grid),'--query-report',str(tail),'--query-cache',str(cache),'--out',str(result),
          '--warm-field',str(warm_field),'--warm-receipt',str(warm),
          '--iterations',str(args.warm_iterations),'--newton',str(args.warm_newton),'--block',str(args.block)]),
      ('new-actual-field-R226-continuous-six-jets',[sys.executable,str(args.scripts/'6a65-m12-entire-half-continuous-correction-bounds.py'),
          *common,'--field',str(field),'--grid',str(grid),'--result',str(result),'--out',str(change)]),
      ('new-actual-field-all-phase-geometry',[sys.executable,str(args.scripts/'6a65-m12-entire-half-actual-field-geometry-transfer.py'),
          '--source-bounds',str(source),'--correction-bounds',str(change),'--field',str(field),
          '--grid',str(grid),'--result',str(result),'--out',str(geometry)]),
      ('same-warm-input-three-window-microspan-observer',[sys.executable,str(args.scripts/'6a65-m12-entire-half-multiple-window-observer.py'),
          *field_common,'--field',str(warm_field),'--result',str(initial_result),'--out',str(warm_micro),
          '--block',str(min(args.block,12))]),
      ('same-warm-input-all-ancestor-observer-union',[sys.executable,str(args.scripts/'6a65-m12-entire-half-transitive-observer-union.py'),
          *field_common,'--field',str(warm_field),'--result',str(initial_result),'--out',str(warm_union)]),
      ('new-actual-field-three-window-microspan-observer',[sys.executable,str(args.scripts/'6a65-m12-entire-half-multiple-window-observer.py'),
          *field_common,'--field',str(field),'--result',str(result),'--out',str(observer),
          '--block',str(min(args.block,12))]),
      ('new-actual-field-all-ancestor-observer-union',[sys.executable,str(args.scripts/'6a65-m12-entire-half-transitive-observer-union.py'),
          *field_common,'--field',str(field),'--result',str(result),'--out',str(old_union)])]
    paths=set(sources+[Path(__file__)])
    paths.update(Path(c[1]) for name,c in commands if c[1]!='-m')
    record={'schema':'6a65-M12-h487-to-h509-M48-nested-full-normal-execution-v1',
        'script_sha256':sha(__file__),'scope':'Original fixed g and complete true-cuff half; same-job h487 plus measured third hotspot knots, actual certified stored warm input, full-H M48 solve.',
        'source_data_sha256':sha(args.data),'commands':[c for name,c in commands],
        'source_hashes':{p.name:sha(p) for p in sorted(paths)},'stages':[],'finished':False,
        'original_metric_unchanged':True,'base_reproduction_is_not_new_mathematical_improvement':True,
        'warm_linear_regularization':0.,'required_LSMR_damp':0.,
        'actual_preconditioner_eta':args.preconditioner_eta,'normal_assembly_block':args.normal_assembly_block,
        'linear_preconditioner':'complete coupled-planar physical H plus eta original H1, right coordinates only',
        'fullH_h487_reference_run':45851669566,'fullH_h487_reference_source':'0ce2394f1b0b049be99e4e622d504ff5660a5843',
        'another_jobs_field_not_borrowed':True,'prior_actual_h487_run':45833090043,
        'expected_prior_actual_h487_field_sha256':args.expected_base_field_sha256,
        'final_R236_and_STL_required_from_outer_supervisor':True}
    if args.plan_only:
        record['plan_only']=True;record['stage_names']=[name for name,c in commands]
        print(json.dumps(record,indent=2),flush=True);return
    def save():record['seconds']=time.monotonic()-began;receipt.write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
    save()
    for name,command in commands:
        if name=='third-hotspot-transitive-source-knot-refinement':
            actual=sha(base_field);record['actual_regenerated_base_field_sha256']=actual
            record['base_field_matches_prior_actual_bytes']=(actual==args.expected_base_field_sha256 if args.expected_base_field_sha256 else None)
            record['base_comparison_uses_this_jobs_actual_field_only']=True
        if name=='actual-complete-normal-h509-M48-nested-warm-solve':
            record['actual_old_source_retention_check']=verify_ancestor_source(base,grid,tail,cache)
            ng=read(grid);history=ng['h_refinement_history']
            if len(ng['unit_mesh'])-1!=509 or history[-1]['inserted_source_node_indices']!=list(range(17350,17372)):
                raise ValueError('Actual third source-knot mesh differs from declared h509')
            save()
        start=time.monotonic();print(json.dumps({'stage':name,'status':'starting'}),flush=True)
        env={k:v for k,v in os.environ.items() if k not in ('GITHUB_TOKEN','GH_TOKEN')}
        if name not in ('regenerate-h487-whole-half','recover-new-exact-tail-queries-and-all-three-source-windows'):
            env.pop('M12_RECOVERY_TOKEN',None)
        child=subprocess.run(command,env=env)
        record['stages'].append({'stage':name,'exit_code':child.returncode,'seconds':time.monotonic()-start});save()
        if child.returncode:raise SystemExit(child.returncode)
    for key,path in [('result',result),('field',field),('grid',grid),('tail_query_report',tail),('tail_query_cache',cache),
        ('continuous_original_source',source),('continuous_actual_change',change),('actual_field_geometry',geometry),
        ('original_microspan_observer',observer),('old_observer_union',old_union),('warm_transfer',warm),
        ('warm_field',warm_field),('warm_observed_result',initial_result),('warm_microspan_observer',warm_micro),
        ('warm_observer_union',warm_union),('base_result',base_result),('base_field',base_field),('base_grid',base_grid)]:
        record[key+'_sha256']=sha(path)
    new_grid=read(grid);old_grid=read(base_grid)
    record['actual_elements']=[len(old_grid['unit_mesh'])-1,len(new_grid['unit_mesh'])-1]
    record['actual_angular_orders']=[old_grid['order'],new_grid['order']]
    record['actual_training_angles']=[old_grid['angular'],new_grid['angular']]
    record['actual_independent_angles']=[2*old_grid['angular'],2*new_grid['angular']]
    record['actual_training_Gauss_orders']=[old_grid['gauss'],new_grid['gauss']]
    record['source_recovery_token_removed_from_all_numerical_children']=True
    record['complete_reports_and_raw_temporary_only']=True
    record['finished']=True;save();print(json.dumps(record,indent=2,allow_nan=False),flush=True)
if __name__=='__main__':main()
