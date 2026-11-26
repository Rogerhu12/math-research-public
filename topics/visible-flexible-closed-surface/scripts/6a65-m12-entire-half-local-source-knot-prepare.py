#!/usr/bin/env python3
"""Insert original-tail microspan knots into one existing whole-half element.

The old unit mesh is retained exactly. Only simple interior quintic knots
inside the selected old element are added; angular order, quadrature order,
original g, all position sources, and complete physical range are unchanged.
Training and independent-observer requests are regenerated from the final
mesh and locked by the same exact-radius query-file hash as the old solver.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

LD=np.longdouble
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(name,p):
    spec=importlib.util.spec_from_file_location(name,p)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('scripts','data','base-grid','suffix-knots','out'):ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--element',type=int,default=190)
    ap.add_argument('--minimum-new-knot-separation',type=float,default=1e-12)
    args=ap.parse_args()
    if args.out.exists() or Path(str(args.out)+'.queries.json').exists():raise FileExistsError('Fresh refined grid required')
    if not 0<args.minimum_new_knot_separation<=1e-9:raise ValueError('Unexpected local refinement separation rule')
    began=time.monotonic();base=json.loads(args.base_grid.read_text());recipe=json.loads(args.suffix_knots.read_text())
    whole=load('local_h_original_whole',args.scripts/'6a65-m12-entire-half-cartesian-bvp.py')
    joint=load('local_h_original_joint',args.scripts/'6a65-m12-global-common-cut-position-recovered.py')
    background=load('local_h_original_background',args.scripts/'6a65-m12-original-tail-background.py')
    args.background_tolerance=base['background_tolerance']
    notes,meta_path,bridge_path,meta,native,chart=whole.definition(args,joint,background)
    for key,path in [('data_sha256',args.data),('common_meta_sha256',meta_path),('bridge_sha256',bridge_path),
                     ('joint_source_sha256',Path(joint.__file__)),('background_source_sha256',Path(background.__file__))]:
        if base[key]!=sha(path):raise ValueError('Changed original base-grid identity '+key)
    manifest=notes/'2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json'
    if recipe['manifest_sha256']!=sha(manifest) or not recipe['exact_cut_backward_increment_arithmetic']:
        raise ValueError('Different original source knot recipe')
    mesh=np.asarray(base['unit_mesh'],float)
    if not 0<=args.element<len(mesh)-1:raise ValueError('No such original whole-grid element')
    left,right=mesh[args.element:args.element+2]
    if LD(left)*chart.total<=chart.S:raise ValueError('The selected element is not in the original tail')
    additions=[];selected=[];nearby=0;maximum_roundtrip=LD(0)
    for node_index,value in zip(recipe['source_node_indices'],recipe['radius_fraction']):
        r=whole.ld(Q(value));z=float(chart.inverse_radius(r))
        if not left<z<right:continue
        maximum_roundtrip=max(maximum_roundtrip,abs(chart.radius(z)[0]-r))
        if min(abs(mesh-z))<args.minimum_new_knot_separation or (additions and min(abs(np.asarray(additions)-z))<args.minimum_new_knot_separation):
            nearby+=1;continue
        additions.append(z);selected.append(int(node_index))
    if not additions:raise ArithmeticError('No original source knots were inserted')
    refined=np.unique(np.r_[mesh,additions])
    if not set(mesh).issubset(set(refined)) or refined[0]!=0 or refined[-1]!=1:
        raise ArithmeticError('Old physical range or old knots changed')
    if maximum_roundtrip>LD('1e-14'):raise ArithmeticError('Source-knot/common-chart inverse did not settle')
    rlo,rhi=sorted([chart.radius(left)[0],chart.radius(right)[0]])
    window=[whole.ld(Q(v)) for v in recipe['window_exact']]
    if not window[0]<rlo<rhi<window[1]:raise ArithmeticError('Source window does not cover the complete selected element')
    m=json.loads(manifest.read_text());inner=whole.ld(Q(m['radialGeometry']['innerAnchor']))
    radii={whole.exact_key(chart.c),whole.exact_key(chart.cuff),whole.exact_key(inner)}
    node_counts=[]
    for gauss in (base['gauss'],base['gauss']+2):
        z,weights=whole.quadrature(refined,gauss,chart);node_counts.append(len(z))
        for point in z:
            if LD(point)*chart.total>chart.S:radii.add(whole.exact_key(chart.radius(point)[0]))
    new_observer=set(map(float,z))
    old_observer,unused=whole.quadrature(mesh,base['gauss']+2,chart)
    missing_indices=[i for i,x in enumerate(old_observer) if float(x) not in new_observer]
    missing=[float(old_observer[i]) for i in missing_indices]
    if any(not left<x<right for x in missing):
        raise ArithmeticError('An observation outside the selected element changed')
    for point in missing:
        if LD(point)*chart.total>chart.S:radii.add(whole.exact_key(chart.radius(point)[0]))
    query=Path(str(args.out)+'.queries.json')
    query.write_text(json.dumps({'schema':'6a65-original-M12-whole-half-radial-queries-v1',
                                'radii':sorted(radii,key=Q)},indent=2)+'\n')
    record=dict(base)
    record.update({'schema':'6a65-original-M12-whole-half-local-source-knot-grid-v1',
                   'script_sha256':sha(__file__),'base_prepare_source_sha256':base['script_sha256'],
                   'base_grid_sha256':sha(args.base_grid),'source_knot_recipe_sha256':sha(args.suffix_knots),
                   'unit_mesh':refined.tolist(),'query_file_sha256':sha(query),
                   'comparison_observer':{'old_gauss':base['gauss']+2,'angular_nodes':2*base['angular'],
                     'old_radial_nodes':len(old_observer),'new_radial_nodes':len(z),
                     'missing_old_unit_nodes':missing,'missing_old_radial_indices':missing_indices,
                     'all_old_nodes_contained_in_union':True,'all_unchanged_element_nodes_retained_exactly':True},
                   'h_refinement':{'old_elements':len(mesh)-1,'new_elements':len(refined)-1,
                     'old_element_index':args.element,'old_unit_interval':[left,right],
                     'old_common_q_interval':[float(LD(left)*chart.total),float(LD(right)*chart.total)],
                     'new_knots':len(additions),'inserted_source_node_indices':selected,
                     'omitted_near_existing_knots':nearby,'minimum_new_knot_separation':args.minimum_new_knot_separation,
                     'old_knots_retained_exactly':True,'knot_multiplicity':'one; old and new correction spaces remain C4',
                     'inverse_radius_roundtrip_max_numerical':str(maximum_roundtrip),
                     'same_g_same_source_same_angle_and_quadrature_order':True},
                   'background':chart.background.receipt()})
    args.out.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'refined_grid_sha256':sha(args.out),'query_file_sha256':sha(query),
                      'old_elements':len(mesh)-1,'new_elements':len(refined)-1,
                      'added_knots':len(additions),'unknowns':(len(refined)-2)*(3*base['order']+2),
                      'radial_node_counts':node_counts,'tail_queries':len(radii),
                      'additional_old_observer_queries':len(missing),
                      'selected_old_element':args.element,'seconds':time.monotonic()-began},indent=2))
if __name__=='__main__':main()

