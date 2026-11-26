#!/usr/bin/env python3
"""One additional original-source h refinement, preserving ancestor observers.

The existing h preparation computes the new physical mesh. This wrapper
retains all earlier exact query radii and inherited missing observer points;
the first eight old-G8 points cannot be lost by a later refinement.
"""
from __future__ import annotations
import argparse,hashlib,json,os,subprocess,sys,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def origin_record(grid,index):return {'origin_grid_sha256':grid,'origin_radial_index':int(index)}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for key in ('scripts','data','base-grid','suffix-knots','out'):ap.add_argument('--'+key,type=Path,required=True)
    ap.add_argument('--element',type=int,default=176)
    ap.add_argument('--minimum-new-knot-separation',default='1e-12');args=ap.parse_args();began=time.monotonic()
    if args.out.exists() or Path(str(args.out)+'.queries.json').exists():raise FileExistsError('Fresh transitive grid output required')
    base=json.loads(args.base_grid.read_text());bquery=Path(str(args.base_grid)+'.queries.json')
    if sha(bquery)!=base['query_file_sha256']:raise ValueError('Ancestor exact-query recipe identity mismatch')
    previous=base.get('comparison_observer')
    if not previous or not previous['all_old_nodes_contained_in_union']:raise ValueError('Expected an already verified first h refinement')
    middle=Path(str(args.out)+'.unmerged.json');producer=args.scripts/'6a65-m12-entire-half-local-source-knot-prepare.py'
    command=[sys.executable,str(producer),'--scripts',str(args.scripts),'--data',str(args.data),
        '--base-grid',str(args.base_grid),'--suffix-knots',str(args.suffix_knots),'--out',str(middle),
        '--element',str(args.element),'--minimum-new-knot-separation',args.minimum_new_knot_separation]
    env={k:v for k,v in os.environ.items() if k not in ('M12_RECOVERY_TOKEN','GITHUB_TOKEN','GH_TOKEN')}
    child=subprocess.run(command,env=env)
    if child.returncode:raise SystemExit(child.returncode)
    new=json.loads(middle.read_text());nquery=Path(str(middle)+'.queries.json')
    if sha(nquery)!=new['query_file_sha256']:raise ValueError('New physical query recipe identity mismatch')
    old_queries=set(json.loads(bquery.read_text())['radii']);new_queries=set(json.loads(nquery.read_text())['radii'])
    radii=sorted(old_queries|new_queries,key=Q)
    comp=new['comparison_observer'];mesh=np.asarray(new['unit_mesh'])
    gx,_=np.polynomial.legendre.leggauss(comp['old_gauss'])
    observed=set(map(float,((mesh[:-1]+mesh[1:])[:,None]/2+(mesh[1:]-mesh[:-1])[:,None]*gx/2).ravel()))
    inherited_origins=previous.get('missing_old_observer_origins')
    if inherited_origins is None:
        inherited_origins=[[origin_record(base['base_grid_sha256'],i)] for i in previous['missing_old_radial_indices']]
    missing={}
    for value,origins in zip(previous['missing_old_unit_nodes'],inherited_origins):
        if float(value) not in observed:missing.setdefault(float(value),[]).extend(origins)
    for value,index in zip(comp['missing_old_unit_nodes'],comp['missing_old_radial_indices']):
        if float(value) not in observed:missing.setdefault(float(value),[]).append(origin_record(sha(args.base_grid),index))
    points=sorted(missing)
    # Keep the old reader's labels for compatibility, but preserve their
    # exact origin-grid provenance and identify this as a transitive union.
    comp['missing_old_unit_nodes']=points
    comp['missing_old_radial_indices']=[missing[x][0]['origin_radial_index'] for x in points]
    comp['missing_old_observer_origins']=[missing[x] for x in points]
    comp['all_ancestor_observers_contained_in_union']=True
    comp['ancestor_grid_sha256s']=sorted(set(previous.get('ancestor_grid_sha256s',[])+[base['base_grid_sha256'],sha(args.base_grid)]))
    comp['inherited_missing_points_kept']=sum(float(x) in missing or float(x) in observed for x in previous['missing_old_unit_nodes'])
    if comp['inherited_missing_points_kept']!=len(previous['missing_old_unit_nodes']):raise ArithmeticError('An inherited old observer point was lost')
    query=Path(str(args.out)+'.queries.json');query.write_text(json.dumps({'schema':'6a65-original-M12-whole-half-radial-queries-v1','radii':radii},indent=2)+'\n')
    new['schema']='6a65-original-M12-transitive-source-aligned-h-grid-v1';new['script_sha256']=sha(__file__)
    new['single_h_prepare_source_sha256']=sha(producer);new['query_file_sha256']=sha(query)
    history=base.get('h_refinement_history',[base['h_refinement']])
    new['h_refinement_history']=history+[new['h_refinement']]
    new['ancestor_query_recipe_sha256s']=base.get('ancestor_query_recipe_sha256s',[])+[base['query_file_sha256']]
    new['all_ancestor_exact_query_radii_retained']=True
    new['ancestor_query_count']=len(old_queries);new['new_physical_query_count']=len(new_queries);new['transitive_query_count']=len(radii)
    args.out.write_text(json.dumps(new,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'schema':new['schema'],'grid_sha256':sha(args.out),'query_file_sha256':sha(query),
        'old_elements':len(base['unit_mesh'])-1,'new_elements':len(new['unit_mesh'])-1,
        'new_knots':new['h_refinement']['new_knots'],'unknowns':(len(new['unit_mesh'])-2)*(3*new['order']+2),
        'missing_ancestor_observer_points':len(points),'inherited_points_retained':comp['inherited_missing_points_kept'],
        'all_ancestor_query_radii_retained':True,'exact_query_count':len(radii),'same_original_g':True,
        'numerical_solve_executed':False,'seconds':time.monotonic()-began},indent=2))
if __name__=='__main__':main()
