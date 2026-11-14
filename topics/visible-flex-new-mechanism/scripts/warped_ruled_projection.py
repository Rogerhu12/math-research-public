#!/usr/bin/env python3
"""Continuous filled-projection witnesses without a prior Jordan assumption.

The input is warped_ruled_core.certified_centerline(...).  Its ordered
binary64 polygon lies within a proved vertex/chord error of the exact
periodic curve.  An interval-certified escape ray proves that a rotated
central point is in the unbounded complementary component.  Only then is
its boundary distance used as a distance to the filled compact set.

Research geometry runs through warped_ruled_core.py in public Actions.
This module's --check-only performs small synthetic geometry checks only.
"""
from __future__ import annotations

import argparse
from decimal import Decimal as D
from fractions import Fraction
import hashlib
import json
from pathlib import Path

import numpy as np

from folded_reference_geometry import I, PI, UP, DOWN
from star_core_geometry import (F, down, up, dot2, norm2, square,
                                polygon_distance, polygon_diameter,
                                midpoint_with_error, unit_enclosures)


def cross2(x,y):
    return x[0]*y[1]-x[1]*y[0]


def select(x,mask):
    return F(x.lo[mask],x.hi[mask])


def point_segment_distances(point,vertices):
    """One outward interval per exact binary64 polygon edge."""
    following=np.roll(vertices,-1,axis=0)
    a=[F(vertices[:,j]) for j in range(2)]
    edge=[F(following[:,j])-a[j] for j in range(2)]
    offset=[F(point[j])-a[j] for j in range(2)]
    length2=dot2(edge,edge)
    good=length2.lo>0
    # A zero or unresolved edge is enclosed by its first endpoint plus its
    # full length; no division by an unresolved denominator is performed.
    base=norm2(offset)
    edge_size=norm2(edge)
    lo=np.maximum(0.,down(base.lo-edge_size.hi));hi=base.hi.copy()
    if np.any(good):
        t=(select(dot2(offset,edge),good)/select(length2,good)).clamp01()
        residual=[select(offset[j],good)-t*select(edge[j],good) for j in range(2)]
        distance=norm2(residual)
        lo[good],hi[good]=distance.lo,distance.hi
    return F(lo,hi)


def ray_polygon_clearance(point,direction,vertices):
    """Lower bound for distance from a whole closed ray to a polygon.

    Coordinates and direction are exact binary64 values.  Each edge is
    first proved disjoint from the ray by signed line coordinates.  For
    disjoint segments/rays the closest pair has at least one finite
    endpoint, so three point-to-edge/ray distances suffice.  An unresolved
    intersection contributes a zero lower bound, never a false positive.
    """
    point=np.asarray(point,float);direction=np.asarray(direction,float)
    vertices=np.asarray(vertices,float)
    if point.shape!=(2,) or direction.shape!=(2,) or vertices.ndim!=2 or vertices.shape[1]!=2:
        raise ValueError('expected a planar point/direction and ordered planar vertices')
    if not np.all(np.isfinite(np.r_[point,direction,vertices.ravel()])):
        raise ValueError('all binary64 geometric inputs must be finite')
    d=[F(direction[j]) for j in range(2)]
    dd=dot2(d,d)
    if float(dd.lo)<=0:
        raise ValueError('escape direction must be nonzero')
    following=np.roll(vertices,-1,axis=0)
    A=[F(vertices[:,j])-F(point[j]) for j in range(2)]
    B=[F(following[:,j])-F(point[j]) for j in range(2)]
    ca,cb=cross2(d,A),cross2(d,B)
    pa,pb=dot2(d,A),dot2(d,B)
    side=((ca.lo>0)&(cb.lo>0))|((ca.hi<0)&(cb.hi<0))
    behind=np.maximum(pa.hi,pb.hi)<0
    disjoint=side|behind
    denominator=ca-cb
    nonzero=(denominator.lo>0)|(denominator.hi<0)
    pending=(~disjoint)&nonzero
    if np.any(pending):
        den=select(denominator,pending)
        inverse=F(down(1/den.hi),up(1/den.lo))
        parameter=select(ca,pending)*inverse
        line_misses=(parameter.hi<0)|(parameter.lo>1)
        # If the intersection parameter lies in the segment, a negative
        # longitudinal coordinate puts that crossing behind the ray.
        clipped=parameter.clamp01()
        crossing=select(pa,pending)+clipped*(select(pb,pending)-select(pa,pending))
        disjoint[pending]=line_misses|(crossing.hi<0)

    def endpoint_to_ray(w,projection):
        t=projection/dd
        t=F(np.maximum(t.lo,0.),np.maximum(t.hi,0.))
        return norm2([w[j]-t*d[j] for j in range(2)])

    from_origin=point_segment_distances(point,vertices)
    from_a=endpoint_to_ray(A,pa);from_b=endpoint_to_ray(B,pb)
    edge_lower=np.minimum(np.minimum(from_origin.lo,from_a.lo),from_b.lo)
    edge_lower=np.where(disjoint,np.maximum(edge_lower,0.),0.)
    lower=D.from_float(float(np.min(edge_lower)))
    return {'polygon_ray_distance_lower':str(lower),
            'all_edges_disjoint_certified':bool(np.all(disjoint)),
            'unresolved_or_intersecting_edges':int(np.sum(~disjoint)),
            'all_vertices_strictly_behind_ray_origin':bool(np.all(behind)),
            'direction_exact_binary64':direction.tolist(),
            'roundoff_model':'IEEE-754 outward intervals for every elementary operation'}


def exact_polygon_winding(point,vertices):
    """Exact integer winding of a binary64 polygon, or None on its edges."""
    px,py=map(Fraction,point)
    values=[(Fraction(x)-px,Fraction(y)-py) for x,y in vertices]
    winding=0
    for (ax,ay),(bx,by) in zip(values,values[1:]+values[:1]):
        determinant=ax*by-ay*bx
        if determinant==0 and ax*bx+ay*by<=0:
            return None
        if ay<=0<by and determinant>0:
            winding+=1
        elif by<=0<ay and determinant<0:
            winding-=1
    return winding


def radial_graph_audit(certificate,curve_error):
    """Optional Jordan proof; positive angular speed alone is insufficient."""
    vertices=np.asarray(certificate['vertices'])[:,:2]
    origin_distance=polygon_distance(np.zeros(2),vertices)
    origin_margin=DOWN.subtract(origin_distance.lo,curve_error)
    winding=exact_polygon_winding((0.,0.),vertices)
    lower=None
    for x,v in zip(certificate['position_cells'],certificate['derivative_cells']):
        value=x[0]*v[1]-x[1]*v[0]
        lower=value.lo if lower is None else min(lower,value.lo)
    passed=origin_margin>0 and winding==1 and lower is not None and lower>0
    return {'radial_jordan_graph_certified':bool(passed),
            'continuous_origin_distance_lower':str(max(D(0),origin_margin)),
            'continuous_cross_c_cprime_lower':None if lower is None else str(lower),
            'exact_polygon_winding_about_origin':winding,
            'winding_transfer_avoids_origin_certified':origin_margin>0,
            'criterion':'positive cross(c,cprime), avoidance of origin, and winding exactly one'}


def rotated_point_box(vertex_box):
    """Exact pi/3 rotation; transcendental float trigonometry is not used."""
    x,y=vertex_box[:2]
    root3=I(3).sqrt()
    return (x/2-root3*y/2,root3*x/2+y/2)


def projection_audit(certificate,half_width_text,witness_count=12):
    """Consume the frozen certified_centerline API and return small JSON."""
    report=certificate['report'];vertices=np.asarray(certificate['vertices'],float)[:,:2]
    nodes=len(vertices)
    if nodes!=report['nodes'] or nodes<6:
        raise ValueError('inconsistent ordered centerline vertex count')
    if not report.get('exact_center_closure_from_formula',False):
        raise ValueError('a proved periodic central curve is required')
    if witness_count<1:
        raise ValueError('at least one finite witness is required')
    vertex_error=D(certificate['vertex_error'])
    step=2*PI/nodes
    chord_error=(I(certificate['second_derivative_upper'])*square(step)/8).hi
    curve_error=UP.add(vertex_error,chord_error)
    radial=radial_graph_audit(certificate,curve_error)
    polygon_D=polygon_diameter(vertices)
    Dxy=I(max(D(0),DOWN.subtract(polygon_D.lo,UP.multiply(D(2),vertex_error))),
          UP.add(polygon_D.hi,UP.multiply(D(2),curve_error)))
    # Selection is finite and is only an attempt to find a witness.  It
    # does not assert that the chosen vertex maximizes radius or distance.
    peak=int(np.argmax(np.sum(vertices*vertices,axis=1)))
    sector=max(1,nodes//3)
    indices=sorted(set([peak,*[int(j*sector/witness_count)%nodes for j in range(witness_count)]]))
    candidates=[]
    for index in indices:
        qbox=rotated_point_box(certificate['vertex_boxes'][index])
        point,point_error=midpoint_with_error(*qbox)
        boundary=polygon_distance(point,vertices)
        error=UP.add(curve_error,point_error)
        lower=max(D(0),DOWN.subtract(boundary.lo,error))
        upper=UP.add(boundary.hi,error)
        if np.any(point!=0):
            ray=ray_polygon_clearance(point,point,vertices)
            ray_margin=DOWN.subtract(D(ray['polygon_ray_distance_lower']),error)
        else:
            ray={'polygon_ray_distance_lower':'0','all_edges_disjoint_certified':False,
                 'unresolved_or_intersecting_edges':nodes,'direction_exact_binary64':[0.,0.]}
            ray_margin=-error
        outside=ray_margin>0
        method='escape_ray' if outside else None
        winding=None
        if not outside and radial['radial_jordan_graph_certified'] and lower>0:
            winding=exact_polygon_winding(point,vertices)
            if winding==0:
                outside=True;method='jordan_winding_zero'
        candidates.append({'central_vertex_index':index,
            'central_parameter':'2*pi*index/nodes','rotation_angle':'pi/3',
            'rotated_point_box':{'x':qbox[0].json(),'y':qbox[1].json()},
            'q_binary64_midpoint':point.tolist(),'q_midpoint_error_upper':str(point_error),
            'continuous_boundary_distance':I(lower,upper).json(),
            'escape_ray':ray,'continuous_escape_ray_clearance_lower':str(ray_margin),
            'exact_polygon_winding_about_q_if_used':winding,
            'q_in_unbounded_complementary_component_certified':outside,
            'outside_certificate_method':method,
            'filled_domain_distance':I(lower,upper).json() if outside else None})
    usable=[c for c in candidates if c['q_in_unbounded_complementary_component_certified']]
    best=max(usable,key=lambda c:D(c['filled_domain_distance']['lower'])) if usable else None
    w=I(half_width_text)
    if w.lo<0:
        raise ValueError('half width must be nonnegative')
    height=I(report['center_absolute_height_upper'])
    Dcore=(square(I(Dxy.hi)+2*w)+square(2*(height+w))).sqrt()
    conditional=None
    if best is not None:
        distance=I(max(D(0),DOWN.subtract(D(best['filled_domain_distance']['lower']),w.hi)))
        ratio=distance/I(Dcore.hi)
        conditional={'half_width':half_width_text,'projection_padding_upper':str(w.hi),
            'central_height_absolute_upper':str(height.hi),
            'total_z_span_upper':str((2*(height+w)).hi),
            'core_diameter_upper':str(Dcore.hi),'witness_distance_lower':str(distance.lo),
            'witness_over_D_lower':str(ratio.lo),'at_least_03':ratio.lo>=D('.3'),
            'full_surface_projection_contained_in_same_padded_fill_proved':False,
            'full_surface_height_bound_proved':False,'fixed_material_hold_constructed':False}
    necessary=None
    k_lower=report.get('core_max_principal_curvature_lower')
    if k_lower is not None and D(k_lower)>0 and Dxy.lo>0:
        necessary=str((I(1)/(I(k_lower)*I(Dxy.lo))).hi)
    return {'schema':'warped-ruled-filled-projection-v1',
            'filled_set_definition':'complement of the unbounded component of R2 minus the exact central projection',
            'jordan_or_radial_graph_assumed':False,'nodes':nodes,
            'vertex_error_upper':str(vertex_error),'chord_error_upper':str(chord_error),
            'continuous_curve_to_polygon_error_upper':str(curve_error),
            'full_continuous_projection_diameter':Dxy.json(),
            'radial_graph_audit':radial,'finite_witness_candidates':candidates,
            'selected_witness_vertex_index':None if best is None else best['central_vertex_index'],
            'filled_domain_witness_proved':best is not None,
            'selected_filled_domain_distance':None if best is None else best['filled_domain_distance'],
            'conditional_closed_surface_budget':conditional,
            'necessary_reach_over_D_upper_from_existing_core_curvature_lower':necessary,
            'core_embedding_proved':False,'global_reach_lower_proved':False,
            'task_complete':False,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


def check_only():
    # Synthetic squares and line segments: no warped-core parameter scan.
    square_vertices=np.array([[-1.,-1.],[1.,-1.],[1.,1.],[-1.,1.]])
    outside=ray_polygon_clearance(np.array([2.,0.]),np.array([1.,0.]),square_vertices)
    inward=ray_polygon_clearance(np.array([2.,0.]),np.array([-1.,0.]),square_vertices)
    inside=ray_polygon_clearance(np.array([0.,0.]),np.array([1.,0.]),square_vertices)
    behind_crossing=ray_polygon_clearance(np.array([0.,0.]),np.array([1.,0.]),
        np.array([[-2.,1.],[1.,-2.]]))
    collinear_behind=ray_polygon_clearance(np.array([0.,0.]),np.array([1.,0.]),
        np.array([[-2.,0.],[-1.,0.]]))
    collinear_ahead=ray_polygon_clearance(np.array([0.,0.]),np.array([1.,0.]),
        np.array([[1.,0.],[2.,0.]]))
    winding=[exact_polygon_winding(point,square_vertices) for point in [(0.,0.),(2.,0.),(1.,0.)]]
    # Exercise the full certificate API on an exact unit circle.  Rotation
    # preserves its filled disk, so no positive filled-distance witness
    # may be accepted even though an inscribed polygon has small gaps.
    circle_trig,circle_cells=unit_enclosures(16)
    circle_vertices=[];circle_boxes=[];circle_error=D(0)
    for ss,cc in circle_trig:
        point,error=midpoint_with_error(cc,ss)
        circle_vertices.append([*point,0.]);circle_boxes.append([cc,ss,I(0)])
        circle_error=max(circle_error,error)
    circle_cert={'vertices':np.array(circle_vertices),'vertex_boxes':circle_boxes,
        'vertex_error':circle_error,'second_derivative_upper':D(1),
        'position_cells':[[cc,ss,I(0)] for ss,cc in circle_cells],
        'derivative_cells':[[-ss,cc,I(0)] for ss,cc in circle_cells],
        'report':{'nodes':16,'exact_center_closure_from_formula':True,
                  'center_absolute_height_upper':'0','core_max_principal_curvature_lower':None}}
    circle_audit=projection_audit(circle_cert,'.01',3)
    checks={'outside_outward_ray':outside,'outside_inward_ray':inward,
            'inside_ray':inside,'line_crossing_behind_ray':behind_crossing,
            'collinear_segment_behind':collinear_behind,'collinear_segment_ahead':collinear_ahead,
            'exact_winding_inside_outside_boundary':winding,
            'exact_circle_api':{'radial_jordan_graph_certified':circle_audit['radial_graph_audit']['radial_jordan_graph_certified'],
                'filled_domain_witness_proved':circle_audit['filled_domain_witness_proved'],
                'candidate_count':len(circle_audit['finite_witness_candidates'])}}
    passed=(D(outside['polygon_ray_distance_lower'])>D('.999999999999') and
            D(inward['polygon_ray_distance_lower'])==0 and
            D(inside['polygon_ray_distance_lower'])==0 and
            D(behind_crossing['polygon_ray_distance_lower'])>D('.70710678118') and
            D(collinear_behind['polygon_ray_distance_lower'])>D('.999999999999') and
            D(collinear_ahead['polygon_ray_distance_lower'])==0 and winding==[1,0,None] and
            circle_audit['radial_graph_audit']['radial_jordan_graph_certified'] and
            not circle_audit['filled_domain_witness_proved'])
    return {'schema':'warped-projection-synthetic-check-v1','check_only':True,
            'research_geometry_evaluated':False,'checks':checks,'passed':bool(passed),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only',action='store_true',required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();result=check_only()
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'passed':result['passed'],'out':str(args.out)}),flush=True)
    if not result['passed']:
        raise SystemExit(1)


if __name__=='__main__':
    main()
