#!/usr/bin/env python3
"""Exact endpoint boxes and rational upper integrals for R635's meridian gate.

Input is the accepted finite prefix, never a regenerated solver field. All
proof comparisons use Fraction and integer square roots. Decimal displays
and the closed-form integral are informational only. Output belongs outside
the repository. No NumPy/SciPy dependency or sampled surface extremum.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from math import asin, floor, isqrt, sqrt
from pathlib import Path


def sqrt_bounds(value, denominator=10**18):
    """Rational enclosure of sqrt(value), including exact-square cases."""
    if value < 0:
        raise ValueError('Negative square root')
    n = isqrt(value.numerator * denominator**2 // value.denominator)
    lo = Q(n, denominator)
    hi = lo if lo * lo == value else Q(n + 1, denominator)
    assert lo * lo <= value <= hi * hi
    return lo, hi


def decimal_box(value, denominator=10**12):
    n = value.numerator * denominator // value.denominator
    return Q(n, denominator), Q(n + 1, denominator)


def text_q(value):
    return str(value.numerator) + '/' + str(value.denominator)


def box_report(box):
    return dict(lower=text_q(box[0]), upper=text_q(box[1]),
                lower_decimal=float(box[0]), upper_decimal=float(box[1]))


def exact_axis_data(data, node):
    m = data['M']
    y = [Q(v) for v in data['states'][node]]
    ys = [Q(v) for v in data['rhs'][node]]
    x = sum(y[:m+1]); z = sum(y[2*m+1:])
    vx = sum(ys[:m+1]); vz = sum(ys[2*m+1:])
    if min(x, vx, vz) <= 0:
        raise ValueError('Expected an outward/upward major reflection axis')
    p = sqrt_bounds(vz*vz/(vx*vx+vz*vz), 10**12)
    minor_radius = sum((-1)**j*v for j, v in enumerate(y[:m+1]))
    minor_height = sum((-1)**j*v for j, v in enumerate(y[2*m+1:]))
    if minor_radius <= 0:
        raise ValueError('Expected a positive minor-axis radius')
    return dict(x=decimal_box(x), z=decimal_box(z), p=p,
                minor_radius=decimal_box(minor_radius),
                minor_height=decimal_box(minor_height))


def f_upper(p):
    return sqrt_bounds((1-p)/(1+p))[1]


def integral_upper(left, right, panels):
    """f(p)=sqrt((1-p)/(1+p)) is decreasing; left sums are upper bounds."""
    if not -1 < left <= right < 1:
        raise ValueError('Integral outside the strict positive projection range')
    step = (right-left)/panels
    return step*sum(f_upper(left+j*step) for j in range(panels))


def gate(axis, radius, height_upper, curvature, panels, radius_tolerance):
    rlo, rhi = radius-radius_tolerance, radius+radius_tolerance
    xhi = rhi-axis['x'][0]
    plo = axis['p'][0]
    if curvature*xhi < plo:
        return dict(flatten_radius_impossible=True)
    pstar = (plo-curvature*xhi)/2
    if pstar <= -1:
        return dict(integral_gate_applicable=False,
                    reason='Envelope can reach negative vertical tangent')
    # I increases with X and decreases with p0.  Hence these endpoint boxes
    # bound the exact integral for every actual x0,p0,R in the prescribed box.
    upper_i = (integral_upper(pstar, plo, panels)
               +integral_upper(pstar, Q(0), panels))/curvature
    major_upper = height_upper-axis['z'][0]+upper_i
    minor_horizontal_lower = rlo-axis['minor_radius'][1]
    if major_upper <= 0 or minor_horizontal_lower <= 0:
        raise ValueError('This numeric report expects positive lengths')
    e_floor = ((minor_horizontal_lower**2-major_upper**2)
               /(minor_horizontal_lower**2+major_upper**2))
    epsilon = Q(1, 10**6)
    excluded = ((1-epsilon)*minor_horizontal_lower**2
                > (1+epsilon)*major_upper**2)
    pf, xf, kf = float(plo), float(xhi), float(curvature)
    pm = (pf-kf*xf)/2
    primitive = lambda v: asin(v)+sqrt(1-v*v)
    numerical_i = (primitive(pf)+1-2*primitive(pm))/kf
    return dict(integral_gate_applicable=True,
                radius_box=box_report((rlo,rhi)),
                height_upper=text_q(height_upper), curvature=text_q(curvature),
                pstar_lower=text_q(pstar), integral_upper=text_q(upper_i),
                integral_upper_decimal=float(upper_i),
                closed_form_informational=numerical_i,
                major_length_upper=text_q(major_upper),
                major_length_upper_decimal=float(major_upper),
                minor_horizontal_lower=text_q(minor_horizontal_lower),
                minor_horizontal_lower_decimal=float(minor_horizontal_lower),
                relative_metric_error_floor=text_q(e_floor),
                relative_metric_error_floor_decimal=float(e_floor),
                excludes_epsilon_1e_6=excluded)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--prefix',type=Path,required=True)
    p.add_argument('--case',action='append',required=True,
                   help='node_index,R,H_upper,K; repeat for independent gates')
    p.add_argument('--panels',type=int,default=1024)
    p.add_argument('--radius-tolerance',default='0.000000000001')
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args(); raw=a.prefix.read_bytes()
    data=json.loads(gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw)
    if not data.get('success'):
        raise ValueError('An accepted finite parent is required')
    rows=[]
    for case in a.case:
        node,r,h,k=case.split(','); node=int(node)
        axis=exact_axis_data(data,node);curvature=Q(k)
        rmin=(axis['x'][0]+axis['p'][0]/curvature,
              axis['x'][1]+axis['p'][1]/curvature)
        row=dict(node=node,s=data['mesh'][node],
                 axis={name:box_report(value) for name,value in axis.items()},
                 minimum_flat_radius=box_report(rmin))
        row.update(gate(axis,Q(r),Q(h),curvature,a.panels,Q(a.radius_tolerance)))
        rows.append(row)
    report=dict(scope=__doc__,parent_sha256=hashlib.sha256(raw).hexdigest(),
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                rational_upper_sum_panels=a.panels, rows=rows)
    a.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(output_sha256=hashlib.sha256(a.out.read_bytes()).hexdigest(),
                          rows=[{key:val for key,val in row.items()
                                 if key.endswith('_decimal') or key in ('node','s','excludes_epsilon_1e_6')}
                                for row in rows])))


if __name__=='__main__':
    main()
