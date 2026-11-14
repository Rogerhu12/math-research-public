#!/usr/bin/env python3
"""Exact arithmetic for the conditional R37 bottleneck distance cover.

The program checks supplied rational pair inequalities, not their geometric
premises. It does not infer continuous enclosures, a complete cover, curvature,
embedding, or reach from samples. Position errors are Euclidean ball radii;
path bounds must be lengths of actual surface paths for every covered pair.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse
import hashlib
import json
from root_reach_patch_bounds import sqrt_upper


def number(value):
    return value if isinstance(value, Q) else Q(value)


def arctan_bounds(x, even_terms):
    """Exact alternating-series bounds for 0<x<1 and an even truncation."""
    x = number(x)
    if not 0 < x < 1 or even_terms < 2 or even_terms % 2:
        raise ValueError('Expected 0<x<1 and a positive even truncation')
    lower = sum(((-1)**k*x**(2*k+1)/Q(2*k+1)
                 for k in range(even_terms)), Q(0))
    upper = lower+x**(2*even_terms+1)/Q(2*even_terms+1)
    return lower, upper


def pi_bounds():
    a_lo, a_hi = arctan_bounds(Q(1, 5), 12)
    b_lo, b_hi = arctan_bounds(Q(1, 239), 4)
    # Machin: tan(4 atan(1/5))=120/119 and subtracting atan(1/239)
    # gives tangent one in (0,pi/2), hence pi=16 atan(1/5)-4 atan(1/239).
    return 16*a_lo-4*b_hi, 16*a_hi-4*b_lo


def dot(x, y):
    return sum((a*b for a, b in zip(x, y)), Q(0))


def cross(x, y):
    return [x[1]*y[2]-x[2]*y[1], x[2]*y[0]-x[0]*y[2],
            x[0]*y[1]-x[1]*y[0]]


def vectors(row):
    p = list(map(number, row['center_p']))
    q = list(map(number, row['center_q']))
    if len(p) != 3 or len(q) != 3:
        raise ValueError('Three-dimensional centers are required')
    ep, eq = number(row['radius_p']), number(row['radius_q'])
    if min(ep, eq) < 0:
        raise ValueError('Position enclosure radii must be nonnegative')
    return p, q, ep+eq


def static_distance_margin(row, tau):
    p, q, error = vectors(row)
    d = [b-a for a, b in zip(p, q)]
    return dot(d, d)-(2*tau+error)**2


def rotating_fixed_distance_margin(row, tau):
    p, q, error = vectors(row)
    x, y = p[:2], q[:2]
    jx = [-x[1], x[0]]
    A = dot(x, x)+dot(y, y)+(q[2]-p[2])**2
    B, C = dot(y, x), dot(y, jx)
    return A-2*sqrt_upper(B*B+C*C)-(2*tau+error)**2


def normal_exclusion_margins(row):
    """Exclude a double normal from continuous position and unit-normal balls.

    Each supplied error bounds |n-n0| for the actual unit normals. n0 itself
    need not be unit. The same certificate is invariant under joint rotations;
    it is not valid for relative rotating-fixed motion without a phase bound.
    """
    supplied=[side for side in ('p','q') if 'normal_center_'+side in row]
    if not supplied:
        return {}
    if row.get('motion','static') not in ('static','both-rotate'):
        raise ValueError('Normal balls need a separate all-phase bound for relative motion')
    p,q,error=vectors(row);d=[b-a for a,b in zip(p,q)]
    length_upper=sqrt_upper(dot(d,d));margins={}
    for side in supplied:
        normal=list(map(number,row['normal_center_'+side]))
        normal_error=number(row['normal_error_'+side])
        if len(normal)!=3 or normal_error<0:
            raise ValueError('Expected a three-dimensional normal center and nonnegative error')
        product=cross(d,normal)
        margins[side]=dot(product,product)-(error+length_upper*normal_error)**2
    return margins


def show(value):
    return dict(exact=str(value), decimal=float(value))


def certify_pair(row, K, tau, pi_lower):
    result = dict(label=row['label'], short_path_paid=False,
                  separation_paid=False, no_double_normal_paid=False,
                  accepted_inequality=False)
    if 'intrinsic_path_upper' in row:
        length = number(row['intrinsic_path_upper'])
        if length < 0:
            raise ValueError('Path length must be nonnegative')
        margin = pi_lower-K*length
        result.update(short_path_margin=show(margin),
                      short_path_paid=margin > 0,
                      R16_half_window_paid=2*K*length < pi_lower)
    if 'center_p' in row:
        kind = row.get('motion', 'static')
        if kind == 'static' or kind == 'both-rotate':
            margin = static_distance_margin(row, tau)
        elif kind == 'rotating-fixed':
            margin = rotating_fixed_distance_margin(row, tau)
        else:
            raise ValueError('Unknown relative motion')
        result.update(separation_squared_margin=show(margin),
                      separation_paid=margin >= 0, motion=kind)
        margins=normal_exclusion_margins(row)
        if margins:
            result.update(normal_exclusion_squared_margins={
                side:show(value) for side,value in margins.items()},
                no_double_normal_paid=any(value>0 for value in margins.values()))
    result['accepted_inequality'] = (result['short_path_paid'] or
        result['separation_paid'] or result['no_double_normal_paid'])
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.input:
        data = json.loads(args.input.read_text())
        input_record = dict(file=str(args.input),
                           sha256=hashlib.sha256(args.input.read_bytes()).hexdigest())
    else:
        data = dict(curvature_bound='33/4', reach_target='3/25', pairs=[
            dict(label='short-path beyond the older half-window',
                 intrinsic_path_upper='1/3'),
            dict(label='separated position balls', motion='static',
                 center_p=[0, 0, 0], center_q=['3/10', 0, 0],
                 radius_p='1/10000', radius_q='1/10000'),
            dict(label='all phases against a fixed position ball',
                 motion='rotating-fixed', center_p=[2, 0, 0],
                 center_q=[1, 1, '1/2'], radius_p='1/1000', radius_q='1/1000'),
            dict(label='nearby blocks excluded by one continuous normal ball',
                 center_p=[0,0,0], center_q=['1/5',0,0],
                 radius_p='1/1000', radius_q='1/1000',
                 normal_center_p=[0,0,1], normal_error_p='1/100')])
        input_record = dict(kind='exact arithmetic demonstration; no candidate data')
    K, tau = number(data['curvature_bound']), number(data['reach_target'])
    if K <= 0 or tau <= 0 or K*tau > 1:
        raise ValueError('The R37 theorem requires K>0, tau>0 and K*tau<=1')
    lo, hi = pi_bounds()
    rows = [certify_pair(row, K, tau, lo) for row in data['pairs']]
    output = dict(scope=__doc__, input=input_record,
        curvature_bound=show(K), reach_target=show(tau), curvature_product=show(K*tau),
        pi_lower=show(lo), pi_upper=show(hi),
        pi_interval_proof='Machin identity and explicit alternating rational series',
        pairs=rows, all_supplied_pair_inequalities_paid=all(r['accepted_inequality'] for r in rows),
        full_surface_certified=False,
        missing_premises=['closed embedded C2 surface', 'continuous curvature bound',
                          'complete pair cover', 'true position and optional unit-normal enclosures',
                          'uniform surface paths'],
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        square_root_source_sha256=hashlib.sha256(Path(__file__).with_name(
            'root_reach_patch_bounds.py').read_bytes()).hexdigest())
    args.out.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(dict(output=str(args.out), supplied_pairs=len(rows),
        all_supplied_pair_inequalities_paid=output['all_supplied_pair_inequalities_paid'],
        full_surface_certified=False)), flush=True)


if __name__ == '__main__':
    main()
