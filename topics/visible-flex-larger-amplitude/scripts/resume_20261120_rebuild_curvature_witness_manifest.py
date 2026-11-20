#!/usr/bin/env python3
"""Rebuild the immutable physical-witness manifest from retained run recipes.

All inputs are locally regenerated raw reports. No numeric field arrays are
embedded here. The point ordering matches the actual 2026-11-20 handoff.
"""
import argparse
import hashlib
import json
from pathlib import Path


def unique(points):
    return [list(p) for p in dict.fromkeys(tuple(p) for p in points)]


def coarse_points(report):
    last=report['iterations'][-1]
    local=report['final_memory']['arbitrary']
    grid=report['final_memory']['grid']
    curves=local['protected_curvature_points']+local['curvature_points']+last['pinned_curvature_points']
    curves += [p['point'] for p in report['final_arbitrary_geometry']['curvature_witnesses']]
    curves += [report['final_arbitrary_geometry']['best_arbitrary_curvature']['point']]
    radii=local['radius_points']+last['pinned_radius_points']+[report['final_arbitrary_geometry']['best_arbitrary_diameter']['point']]
    grid_c=grid['curvature_locations'][:]
    grid_r=grid['radius_locations'][:]
    for row in last['active_constraints']:
        c,r=row['curvature_point'],row['diameter_point']
        if c['kind']=='grid':
            grid_c.append([c['stage'],c['angle']])
        if r['kind']=='grid':
            grid_r.append([r['stage'],r['angle']])
    c=report['final_gauss_geometry']['worst']
    r=report['final_gauss_geometry']['farthest']
    grid_c.append([c['stage'],c['angle']])
    grid_r.append([r['stage'],r['angle']])
    return dict(curvature_points=unique(curves),radius_points=unique(radii),
                grid_curvature_locations=unique(grid_c),grid_radius_locations=unique(grid_r))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('coarse-report','expanded-report','dense-report','bundle','out'):
        p.add_argument('--'+key,type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():
        raise FileExistsError('Use a fresh manifest path')
    c=json.loads(a.coarse_report.read_text())
    r=json.loads(a.expanded_report.read_text())
    d=json.loads(a.dense_report.read_text())
    if r['output_bundle_sha256']!=d['input_sha256'] or d['input_sha256']!=d['output_bundle_sha256']:
        raise ValueError('Dense diagnostic must leave the actual expanded field unchanged')
    if hashlib.sha256(a.bundle.read_bytes()).hexdigest()!=r['output_bundle_sha256']:
        raise ValueError('Actual bundle hash mismatch')
    prior=coarse_points(c)
    local=r['final_memory']['arbitrary']
    curves=prior['curvature_points']+local['protected_curvature_points']+local['curvature_points']
    curves += [v['point'] for v in d['final_arbitrary_geometry']['curvature_witnesses']]
    radii=prior['radius_points']+local['radius_points']+[d['final_arbitrary_geometry']['best_arbitrary_diameter']['point']]
    value=dict(schema='dense-angle-known-point-handoff-v1',
        bundle_path=str(a.bundle),bundle_sha256=r['output_bundle_sha256'],
        carrier_sha256=r['dependency_sha256']['carrier'],
        optimization_full_angles=2048,diagnostic_full_angles=8192,
        curvature_points=unique(curves),radius_points=unique(radii),
        grid_curvature_locations=unique(prior['grid_curvature_locations']+r['final_memory']['grid']['curvature_locations']),
        grid_radius_locations=unique(prior['grid_radius_locations']+r['final_memory']['grid']['radius_locations']),
        new_dense_witnesses=d['final_arbitrary_geometry']['curvature_witnesses'],
        dense_grid_maximum=d['final_gauss_geometry'],optimization_statistics=r['final'],
        necessary_product=d['final_arbitrary_geometry']['necessary_reach_product'],
        scope='Locations are permanent actual witnesses to reread at every descendant. Only the diagnostic has N8192; original optimization objective/rows remain N2048. No continuous upper bound or reach proof.')
    a.out.write_text(json.dumps(value,indent=2)+'\n')
    print(json.dumps(dict(out=str(a.out),sha256=hashlib.sha256(a.out.read_bytes()).hexdigest(),
        curvature_points=len(value['curvature_points']),radius_points=len(value['radius_points']))))


if __name__=='__main__':
    main()

