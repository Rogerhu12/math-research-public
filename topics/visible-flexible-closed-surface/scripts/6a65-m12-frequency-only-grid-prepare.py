#!/usr/bin/env python3
"""Prepare a strictly nested M12 angular layer with no radial query changes.

The old actual physical mesh, quintic multiplicities, target g, common
chart, Gauss rules and exact query recipe remain. This preparation does not
solve a new field. The complete old correction embeds by zero high modes.
"""
from __future__ import annotations
import argparse,hashlib,json,time
from pathlib import Path
import numpy as np
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for key in ('old-grid','out'):ap.add_argument('--'+key,type=Path,required=True)
    ap.add_argument('--order',type=int,default=48);ap.add_argument('--angular',type=int,default=768)
    args=ap.parse_args();start=time.monotonic()
    query=Path(str(args.out)+'.queries.json')
    if args.out.exists() or query.exists():raise FileExistsError('Fresh angular-layer grid required')
    old=json.loads(args.old_grid.read_text());oq=Path(str(args.old_grid)+'.queries.json')
    if sha(oq)!=old['query_file_sha256']:raise ValueError('Old exact-query recipe identity mismatch')
    if args.order<=old['order'] or args.angular<=old['angular'] or args.angular%old['angular']:
        raise ValueError('Both frequency and angular sample counts must increase; old angular nodes must be retained')
    if args.angular<=2*(3*args.order+1):raise ValueError('Aliased correction basis')
    for count in (old['angular'],2*old['angular']):
        old_angles=np.arange(count)*2*np.pi/count
        new_count=count*args.angular//old['angular']
        new_angles=np.arange(new_count)*2*np.pi/new_count
        if not np.array_equal(old_angles,new_angles[::new_count//count]):
            raise ArithmeticError('Uniform angular points were not retained bitwise by this runtime')
    out=dict(old);out['schema']='6a65-original-M12-same-radial-grid-frequency-refinement-v1'
    out['script_sha256']=sha(__file__);out['parent_grid_sha256']=sha(args.old_grid)
    out['order']=args.order;out['angular']=args.angular
    if 'comparison_observer' in old:
        comp=dict(old['comparison_observer'])
        ancestors=list(comp.get('ancestor_angular_nodes',[]))+[comp['angular_nodes'],2*old['angular']]
        if any(2*args.angular%n for n in ancestors):raise ValueError('An ancestor angle set would be lost')
        comp['ancestor_angular_nodes']=sorted(set(ancestors));comp['angular_nodes']=2*args.angular
        comp['ancestor_grid_sha256s']=sorted(set(comp.get('ancestor_grid_sha256s',[])+[sha(args.old_grid)]))
        comp['all_ancestor_observers_contained_in_union']=True
        comp['same_radial_union_and_all_ancestor_angles_retained']=True
        out['comparison_observer']=comp
    out['frequency_refinement']={'old_order':old['order'],'new_order':args.order,
        'old_angular_nodes':old['angular'],'new_angular_nodes':args.angular,
        'old_independent_angular_nodes':2*old['angular'],'new_independent_angular_nodes':2*args.angular,
        'same_exact_physical_mesh_and_knots':True,'same_training_and_observer_Gauss_orders':True,
        'same_original_g_and_position_source':True,'exact_tail_query_recipe_unchanged':True,
        'old_field_embeds_exactly_by_zero_high_modes':True,
        'complete_source_angular_representation_or_exact_isometry_claimed':False}
    query.write_bytes(oq.read_bytes());args.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    radial=(len(out['unit_knots'])-12) if 'unit_knots' in out else len(out['unit_mesh'])-2
    report={'schema':out['schema'],'script_sha256':sha(__file__),'old_grid_sha256':sha(args.old_grid),
        'new_grid_sha256':sha(args.out),'same_exact_query_file_sha256':sha(query),
        'physical_elements':len(out['unit_mesh'])-1,'radial_columns':radial,
        'old_angular_columns':3*old['order']+2,'new_angular_columns':3*args.order+2,
        'old_unknowns':radial*(3*old['order']+2),'new_unknowns':radial*(3*args.order+2),
        'new_tail_queries_required':0,'same_original_g':True,
        'new_numerical_field_solved':False,'seconds':time.monotonic()-start}
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
