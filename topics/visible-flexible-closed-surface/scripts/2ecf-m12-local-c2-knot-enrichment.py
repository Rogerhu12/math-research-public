#!/usr/bin/env python3
"""Enlarge an existing M12 correction space at existing selected nodes.

The physical mesh, every source query, fixed g, angular basis, and all
quadrature points stay unchanged. Selected existing simple knots acquire
multiplicity three, allowing C2 corrections there. This is a space recipe,
not a solved field or a claim that binary64 knots exactly equal source-r
breakpoints. Existing exact Boehm transfer supplies the warm field.
"""
from __future__ import annotations
import argparse,collections,hashlib,json,shutil
from fractions import Fraction as Q
from pathlib import Path

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--old-grid',type=Path,required=True)
    ap.add_argument('--coarse-grid',type=Path,required=True,
                    help='Only old-grid knots absent from this known ancestor are enriched')
    ap.add_argument('--old-queries',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();qp=Path(str(args.out)+'.queries.json')
    if args.out.exists() or qp.exists():raise FileExistsError('Fresh enriched recipe required')
    old=json.loads(args.old_grid.read_text());coarse=json.loads(args.coarse_grid.read_text())
    if sha(args.old_queries)!=old['query_file_sha256']:raise ValueError('Actual original query recipe differs')
    for key in ('data_sha256','common_meta_sha256','bridge_sha256','joint_source_sha256',
                'background_source_sha256','background_tolerance','physical_prefix_length_numerical',
                'material_chart_length_numerical','true_cuff_exact','order','angular','gauss'):
        if old[key]!=coarse[key]:raise ValueError('Changed original identity or quadrature: '+key)
    mesh=old['unit_mesh'];coarse_mesh=coarse['unit_mesh']
    if not set(coarse_mesh)<=set(mesh):raise ValueError('Declared coarse mesh is not an ancestor')
    if any(b<=a for a,b in zip(mesh,mesh[1:])):raise ValueError('Physical mesh must be strictly increasing')
    selected=set(mesh)-set(coarse_mesh)
    if not selected or not all(0<x<1 for x in selected):raise ValueError('No valid interior enrichment knots')
    knots=old.get('unit_knots',[0.]*6+mesh[1:-1]+[1.]*6)
    counts=collections.Counter(knots)
    if counts[0.]!=6 or counts[1.]!=6 or any(n>3 for k,n in counts.items() if 0<k<1):
        raise ValueError('Original space was not clamped quintic C2')
    added=0
    for x in selected:
        added+=3-counts[x];counts[x]=3
    nt=sorted(x for x,n in counts.items() for unused in range(n))
    if added<=0:raise ValueError('All selected nodes are already C2')
    new=dict(old);new['unit_knots']=nt
    new['c2_knot_enrichment']={'script_sha256':sha(__file__),'old_grid_sha256':sha(args.old_grid),
      'coarse_grid_sha256':sha(args.coarse_grid),'query_recipe_sha256':sha(args.old_queries),
      'selected_existing_knots':sorted(selected),'added_knot_copies':added,
      'old_radial_free_columns':len(knots)-12,'new_radial_free_columns':len(nt)-12,
      'same_unique_physical_mesh':True,'same_all_source_query_radii':True,
      'same_training_and_observation_quadrature':True,'same_original_g':True,
      'selected_knots_continuity':'C2','other_interior_knots_continuity':'inherited',
      'exact_source_radial_knot_coincidence_claimed':False,
      'note':'Each knot is its original binary64 exact real. Original source-r inverse roundtrip errors are inherited, not declared zero.',
      'requires_actual_Boehm_warm_transfer':True,'new_nonlinear_solve_executed':False}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(args.old_queries,qp)
    if sha(qp)!=old['query_file_sha256']:raise ArithmeticError('Query copy changed')
    args.out.write_text(json.dumps(new,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'new_grid':str(args.out),'new_grid_sha256':sha(args.out),
      'selected_nodes':len(selected),'added_knot_copies':added,
      'new_unknowns':(len(nt)-12)*(3*old['order']+2),
      'physical_elements':len(mesh)-1,'query_recipe_unchanged':True},indent=2))

if __name__=='__main__':main()
