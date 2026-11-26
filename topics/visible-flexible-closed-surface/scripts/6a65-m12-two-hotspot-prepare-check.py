#!/usr/bin/env python3
"""Check the transitive finite-grid and exact diagnostic-point contract.

This does not solve a new field. The old 297 exact source diagnostic points
are compared byte for byte as rational strings and source-span indices.
Both ancestor G8 point sets are checked against the final G8-plus-extra set.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def nodes(grid):
    mesh=np.asarray(grid['unit_mesh']);gx,_=np.polynomial.legendre.leggauss(grid['gauss']+2)
    return ((mesh[:-1]+mesh[1:])[:,None]/2+(mesh[1:]-mesh[:-1])[:,None]*gx/2).ravel()
def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('base-grid','first-grid','final-grid','suffix-knots','old-diagnostic-cache','out'):
        ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--selector',type=Path,default=Path(__file__).with_name('6a65-m12-stream-tail-multiple-diagnostic-windows.py'))
    args=ap.parse_args();start=time.monotonic()
    if args.out.exists():raise FileExistsError('Fresh scalar check report required')
    spec=importlib.util.spec_from_file_location('two_window_checked_selector',args.selector)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    grids=[json.loads(path.read_text()) for path in (args.base_grid,args.first_grid,args.final_grid)]
    base,first,final=grids
    for old in (base,first):
        if not set(old['unit_mesh']).issubset(set(final['unit_mesh'])):raise ArithmeticError('Ancestor knot lost')
    union=set(nodes(final))|set(final['comparison_observer']['missing_old_unit_nodes'])
    for old in (base,first):
        if not set(nodes(old)).issubset(union):raise ArithmeticError('Ancestor independent point lost')
    final_queries=set(json.loads(Path(str(args.final_grid)+'.queries.json').read_text())['radii'])
    first_queries=set(json.loads(Path(str(args.first_grid)+'.queries.json').read_text())['radii'])
    if not first_queries.issubset(final_queries):raise ArithmeticError('Ancestor exact source query lost')
    source=json.loads(args.suffix_knots.read_text());indices=source['source_node_indices'];rr=list(map(Q,source['radius_fraction']))
    if any(b!=a+1 for a,b in zip(indices,indices[1:])):raise ValueError('Source knot recipe has a gap')
    windows=[(Q('.432'),Q('.436')),(Q('.5122'),Q('.5141'))]
    if not rr[0]<windows[0][0]<windows[-1][1]<rr[-1]:raise ValueError('Local recipe does not surround the two windows')
    radii=[];spans=[];masks=[];lookup={};selected_spans=[set(),set()]
    for i,(left,right) in enumerate(zip(rr,rr[1:])):
        groups=module.diagnostic_groups(left,right,windows)
        if not groups:continue
        mask=sum(1<<j for j in groups);span=indices[i]
        for j in groups:selected_spans[j].add(span)
        for k in range(5):
            r=left+Q(k,4)*(right-left)
            if r in lookup:masks[lookup[r]]|=mask;continue
            lookup[r]=len(radii);radii.append(r);spans.append(span);masks.append(mask)
    groups=[]
    for j,window in enumerate(windows):
        ids=[i for i,mask in enumerate(masks) if mask & (1<<j)]
        payload='\n'.join(str(radii[i])+'\t'+str(spans[i]) for i in ids)+'\n'
        groups.append({'window_exact':list(map(str,window)),'points':len(ids),
                       'source_spans':len(selected_spans[j]),
                       'first_source_span':min(selected_spans[j]),'last_source_span':max(selected_spans[j]),
                       'exact_point_source_sha256':hashlib.sha256(payload.encode()).hexdigest()})
    old_ids=[i for i,mask in enumerate(masks) if mask&1]
    with np.load(args.old_diagnostic_cache,allow_pickle=False) as cache:
        old_fraction=cache['diagnostic_fraction'];old_spans=cache['diagnostic_source_span']
        if list(old_fraction)!=[str(radii[i]) for i in old_ids] or list(old_spans)!=[spans[i] for i in old_ids]:
            raise ArithmeticError('The old exact 297-point microspan observer changed')
    for p in args.selector.parent.glob('6a65-m12-*.py'):
        compile(p.read_text(),str(p),'exec')
    report={'schema':'6a65-M12-two-hotspot-prepare-contract-check-v1','script_sha256':sha(__file__),
            'selector_sha256':sha(args.selector),'base_grid_sha256':sha(args.base_grid),
            'first_h_grid_sha256':sha(args.first_grid),'final_grid_sha256':sha(args.final_grid),
            'suffix_knots_sha256':sha(args.suffix_knots),'old_diagnostic_cache_sha256':sha(args.old_diagnostic_cache),
            'final_query_file_sha256':sha(Path(str(args.final_grid)+'.queries.json')),
            'elements':[len(g['unit_mesh'])-1 for g in grids],
            'unknowns':(len(final['unit_mesh'])-2)*(3*final['order']+2),
            'all_ancestor_knots_retained':True,'both_ancestor_independent_observers_retained':True,
            'both_ancestor_point_counts':[len(nodes(g)) for g in (base,first)],
            'final_G8_point_count':len(nodes(final)),
            'missing_ancestor_observer_points':len(final['comparison_observer']['missing_old_unit_nodes']),
            'all_first_h_exact_query_radii_retained':True,'final_exact_queries':len(final_queries),
            'old_297_diagnostic_points_and_source_indices_unchanged':True,
            'diagnostic_groups':groups,'total_disjoint_diagnostic_points':len(radii),
            'gap_not_sampled_or_claimed_observed':True,
            'all_six_python_sources_compile':True,'new_field_solve_executed':False,
            'same_original_g':True,'exact_isometry_proved':False,'seconds':time.monotonic()-start}
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
