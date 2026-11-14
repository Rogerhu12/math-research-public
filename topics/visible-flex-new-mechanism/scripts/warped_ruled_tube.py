#!/usr/bin/env python3
"""Continuous centerline reach and embedded normal-ribbon certificates.

This consumes the frozen warped_ruled_core.certified_centerline API.  Near
parameter pairs are covered by an arc-length/curvature lemma; every other
whole-cell pair is bounded with outward three-dimensional boxes.  It proves
only the accurate core is embedded when successful, not a closed surface's
reach.  Research inputs run in this public repository's GitHub Actions.
"""
from __future__ import annotations

import argparse
from decimal import Decimal as D
import hashlib
import json
import os
from pathlib import Path
import time

import numpy as np

from folded_reference_geometry import I, PI, DOWN, UP
from star_core_geometry import F, down, up, square, unit_enclosures, midpoint_with_error
from warped_ruled_core import certified_centerline, vnorm


def decimal_interval_to_binary(value):
    """Enclose Decimal endpoints even when binary conversion rounds inward."""
    return float(down(float(value.lo))),float(up(float(value.hi)))


def norm3(vector):
    total=vector[0].square()+vector[1].square()+vector[2].square()
    return F(np.maximum(total.lo,0.),total.hi).sqrt()


def tube_audit(certificate,half_width_text,block=128):
    report=certificate['report'];nodes=report['nodes']
    if len(certificate['position_cells'])!=nodes or len(certificate['derivative_cells'])!=nodes:
        raise ValueError('inconsistent continuous cell count')
    if not report.get('exact_center_closure_from_formula',False):
        raise ValueError('the curve must have a proved exact period')
    width=I(half_width_text)
    if width.lo<0:
        raise ValueError('normal ribbon half-width must be nonnegative')
    kappa=report.get('sphere_geodesic_curvature_absolute_upper')
    if kappa is None:
        return {'schema':'warped-ruled-tube-v1','available':False,
                'reason':'continuous central curvature was unresolved',
                'core_embedding_proved':False,'whole_closed_surface_reach_proved':False}
    scale=I(report['exact_decimal_parameters']['scale'])
    curvature=(I(kappa)/scale).hi
    if curvature<=0:
        raise ValueError('a positive curvature bound for a regular closed curve is required')
    curvature_radius=(I(1)/I(curvature)).lo
    near_arc_threshold=(PI/(2*I(curvature))).lo
    threshold_binary=float(down(float(near_arc_threshold)))
    step=2*PI/nodes

    # Each stored scalar is an exact Decimal upper bound for the true arc
    # length of that cell. Directed prefix sums let subtractions remain safe.
    arc_bounds=[(step*I(vnorm(v).hi)).hi for v in certificate['derivative_cells']]
    prefix=[I(0)]
    for value in arc_bounds:
        prefix.append(prefix[-1]+I(value))
    prefix_binary=np.array([decimal_interval_to_binary(x) for x in prefix])
    pfx=F(prefix_binary[:,0],prefix_binary[:,1])
    total=F(prefix_binary[-1,0],prefix_binary[-1,1])

    cells=np.array([[decimal_interval_to_binary(x) for x in row]
                    for row in certificate['position_cells']])
    near_count=0;far_count=0;far_lower=np.inf;far_pair=None
    all_j=np.arange(nodes)[None,:]
    for start in range(0,nodes,block):
        stop=min(nodes,start+block)
        all_i=np.arange(start,stop)[:,None]
        left=np.minimum(all_i,all_j);right=np.maximum(all_i,all_j)
        forward=F(pfx.lo[right+1],pfx.hi[right+1])-F(pfx.lo[left],pfx.hi[left])
        backward=total-F(pfx.lo[right],pfx.hi[right])+F(pfx.lo[left+1],pfx.hi[left+1])
        near=np.minimum(forward.hi,backward.hi)<=threshold_binary
        # Only the upper triangle is needed. Near includes the diagonal;
        # each entry represents all points in the two corresponding cells.
        use=all_j>=all_i
        far=use&(~near)
        near_count+=int(np.sum(use&near));far_count+=int(np.sum(far))
        if not np.any(far):
            continue
        delta=[F(cells[start:stop,k,0,None],cells[start:stop,k,1,None])-
               F(cells[None,:,k,0],cells[None,:,k,1]) for k in range(3)]
        lower=norm3(delta).lo
        masked=np.where(far,lower,np.inf)
        index=np.unravel_index(int(np.argmin(masked)),masked.shape)
        candidate=float(masked[index])
        if candidate<far_lower:
            far_lower=candidate;far_pair=[start+int(index[0]),int(index[1])]
    if far_count:
        far_distance=D.from_float(far_lower)
        reach_lower=min(curvature_radius,DOWN.divide(far_distance,D(2)))
    else:
        far_distance=None;reach_lower=curvature_radius
    # The local lemma gives positive chord length for all near distinct
    # parameters. Positive far-cell separation therefore first establishes
    # injectivity; the normal-chord bound then establishes curve reach.
    embedded=bool(reach_lower>0)
    ribbon=bool(embedded and reach_lower>width.hi and
                report.get('continuous_direction_regular_by_endpoint_formula',False))
    return {'schema':'warped-ruled-tube-v1','available':True,
            'nodes':nodes,'half_width':half_width_text,
            'center_curvature_absolute_upper':str(curvature),
            'near_arc_threshold_lower':str(near_arc_threshold),
            'near_normal_chord_radius_lower':str(curvature_radius),
            'total_arc_length_upper_from_cells':str(prefix[-1].hi),
            'near_cell_pair_count':near_count,'far_cell_pair_count':far_count,
            'far_cell_distance_lower':None if far_distance is None else str(far_distance),
            'limiting_far_cell_pair':far_pair,
            'centerline_embedding_proved':embedded,
            'centerline_reach_lower':str(reach_lower),
            'core_embedding_proved':ribbon,
            'normal_ribbon_injectivity_margin':str(DOWN.subtract(reach_lower,width.hi)),
            'whole_closed_surface_reach_proved':False,'round_collars_constructed':False,
            'task_complete':False,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


def synthetic_circle_certificate(nodes=48,double_cover=False):
    trig,cells=unit_enclosures(nodes)
    points=[];boxes=[];error=D(0)
    for ss,cc in trig:
        point,err=midpoint_with_error(cc,ss)
        points.append([*point,0.]);boxes.append([cc,ss,I(0)]);error=max(error,err)
    position=[[cc,ss,I(0)] for ss,cc in cells]
    derivative=[[-ss,cc,I(0)] for ss,cc in cells]
    if double_cover:
        # Two turns in the same 2*pi parameter period. This must fail the
        # parameter-injectivity certificate because distant cells coincide.
        points*=2;boxes*=2;position*=2
        derivative=[[2*x for x in row] for row in derivative]*2
        nodes*=2
    return {'vertices':np.array(points),'vertex_boxes':boxes,'vertex_error':error,
            'position_cells':position,'derivative_cells':derivative,
            'second_derivative_upper':D(4 if double_cover else 1),
            'report':{'nodes':nodes,'exact_center_closure_from_formula':True,
                      'exact_decimal_parameters':{'scale':'1'},
                      'sphere_geodesic_curvature_absolute_upper':'1',
                      'continuous_direction_regular_by_endpoint_formula':True}}


def check_only():
    circle=tube_audit(synthetic_circle_certificate(),'.1')
    twice=tube_audit(synthetic_circle_certificate(double_cover=True),'.1')
    expected=48*49//2
    passed=(circle['core_embedding_proved'] and D(circle['centerline_reach_lower'])>D('.5')
            and circle['near_cell_pair_count']+circle['far_cell_pair_count']==expected
            and not twice['centerline_embedding_proved'] and not twice['core_embedding_proved'])
    return {'schema':'warped-tube-synthetic-check-v1','check_only':True,
            'research_geometry_evaluated':False,'circle':circle,'double_cover':twice,
            'passed':bool(passed)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--warp-u',default='.6,.8,1,1.2')
    parser.add_argument('--warp-v',default='0')
    parser.add_argument('--scale',default='1')
    parser.add_argument('--half-width',default='.05')
    parser.add_argument('--nodes',type=int,default=1536)
    parser.add_argument('--check-only',action='store_true')
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if args.check_only:
        report=check_only()
    else:
        if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':
            parser.error('Run research candidates in this public repository GitHub Actions')
        report={'schema':'warped-ruled-tube-scan-v1','rows':[],
                'github_repository':os.environ.get('GITHUB_REPOSITORY'),
                'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID')}
        for u in args.warp_u.split(','):
            for v in args.warp_v.split(','):
                started=time.perf_counter()
                certificate=certified_centerline(u,v,args.scale,args.nodes)
                row={'warp_u':u,'warp_v':v,'continuous':certificate['report'],
                     'tube':tube_audit(certificate,args.half_width)}
                row['elapsed_seconds']=time.perf_counter()-started
                report['rows'].append(row)
                args.out.parent.mkdir(parents=True,exist_ok=True)
                args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
                print(json.dumps(row),flush=True)
    report['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    if args.check_only:
        print(json.dumps({'passed':report['passed'],'circle_reach_lower':report['circle']['centerline_reach_lower'],
                          'double_cover_reach_lower':report['double_cover']['centerline_reach_lower']}),flush=True)
        if not report['passed']:
            raise SystemExit(1)


if __name__=='__main__':
    main()
