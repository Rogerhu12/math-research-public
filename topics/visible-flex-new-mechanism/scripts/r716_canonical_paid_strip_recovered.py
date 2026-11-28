"""Shared C2 centerline and whole finite strip from the existing R705 paid NPZ.

Independent recovery implementation. The original frozen source had SHA256
487928256cdc0bffd2aef6b5259dbb546e54dc604e4779032ba3ec4e5837f869.
"""
from bisect import bisect_left, bisect_right
from fractions import Fraction as F
from math import isqrt
import re

import numpy as np

from r688_actual_r664_window_collars import require_public
from r709_paid_physical_spline_strip_bound import derivative, down, hull_abs, norm_upper, up


ZERO = (F(0), F(0))
EX = (F(1), F(0))
TAU = F(5, 52)
H = max(F(1, 5000), F.from_float(.0002))


def q(x):
    return F.from_float(float(x))


def root_bounds(x):
    if x < 0:
        raise ValueError('Negative squared norm')
    scale = 1 << 64
    i = isqrt((x.numerator * scale * scale) // x.denominator)
    a = F(i, scale)
    return a, a if a*a == x else F(i+1, scale)


def bounds_text(x):
    # Integer multiples of 1e-20 bracket the exact rational result.
    scale = 10**20
    p = x.numerator * scale
    return {'lower_units_1e-20': str(p // x.denominator),
            'upper_units_1e-20': str(-((-p) // x.denominator))}


def add(a, b):
    return tuple(x+y for x, y in zip(a, b, strict=True))


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b, strict=True))


def mul(r, a):
    return tuple(r*x for x in a)


def upper_norm(a):
    return root_bounds(sum(x*x for x in a))[1]


def differences(b, span):
    return [mul(F(len(b)-1, 1)/span, sub(y, x)) for x, y in zip(b, b[1:])]


def jets(b, span):
    d = differences(b, span)
    return [b, d, differences(d, span)]


def far_value(z):
    cuts, left, right, old, coeff = (z['line_'+k] for k in ('breaks', 't_old', 't', 'y_old', 'F'))
    n = len(left)
    if n == 0 or cuts.shape != (n+1,) or right.shape != (n,) or old.shape != (n,3) or coeff.shape != (n,7,3):
        raise ValueError('Expected the actual three-coordinate DOP853 dense data')
    if (cuts[-1] != 1 or cuts[0] != -1 or not np.all(cuts[1:] > cuts[:-1])
            or not np.array_equal(cuts[:-1], left) or not np.array_equal(cuts[1:], right)):
        raise ValueError('DOP853 terminal selector differs')
    y = np.add(old[-1], coeff[-1,0])
    if not np.all(np.isfinite(y)):
        raise ValueError('Nonfinite actual terminal data')
    return tuple(q(x) for x in y[1:])


def split(b, u):
    if not 0 <= u <= 1:
        raise ValueError('Bad Bernstein subdivision label')
    row, left, right = list(b), [b[0]], [b[-1]]
    while len(row) > 1:
        row = [add(mul(1-u, a), mul(u, c)) for a, c in zip(row, row[1:])]
        left.append(row[0])
        right.append(row[-1])
    return left, list(reversed(right))


def restrict(b, lo, hi, a, c):
    if not lo <= a < c <= hi:
        raise ValueError('Common span outside its paid polynomial')
    row = b
    if c < hi:
        row = split(row, (c-lo)/(hi-lo))[0]
    if a > lo:
        row = split(row, (a-lo)/(c-lo))[1]
    return row


def elevated_line(p, r):
    return [add(mul(F(9-i,9),p), mul(F(i,9),r)) for i in range(10)]


def trace(pieces, knots, v, direction, order):
    if direction == 'left':
        k = max(0, bisect_left(knots, v)-1)
    elif direction == 'right':
        k = min(len(pieces)-1, bisect_right(knots, v)-1)
    else:
        # The original cartesian() overrides BPoly at either exterior join.
        side = 'left' if v == knots[1] else 'right'
        return trace(pieces, knots, v, side, order)
    b = pieces[k][order]
    if v == knots[k]:
        return b[0]
    if v == knots[k+1]:
        return b[-1]
    return split(b, (v-knots[k])/(knots[k+1]-knots[k]))[0][-1]


def symtrace(pieces, knots, v, side, order):
    other = {'left':'right', 'right':'left', 'selected':'selected'}[side]
    return mul(F(1,2), sub(trace(pieces,knots,v,side,order),
               mul((-1)**order,trace(pieces,knots,-v,other,order))))


def canonical_data(z):
    k, arr = z['physical_centerline_knots'], z['physical_centerline_bernstein']
    if (k.ndim != 1 or len(k) < 2 or arr.shape != (10,len(k)-1,2)
            or not np.isfinite(arr).all() or not np.isfinite(k).all()
            or not np.all(k[1:] > k[:-1]) or k[0] != -.93 or k[-1] != .93):
        raise ValueError('Unexpected actual degree-nine physical centerline')
    x = [q(v) for v in k]
    far = far_value(z)
    raw = [[tuple(q(t) for t in pt) for pt in arr[:,i]] for i in range(len(x)-1)]
    jraw = [jets(b,hi-lo) for b,lo,hi in zip(raw,x,x[1:])]
    shared = [[(x[0],F(0)),EX,ZERO]]
    for left, right in zip(jraw,jraw[1:]):
        shared.append([mul(F(1,2),add(a[-1],b[0])) for a,b in zip(left,right,strict=True)])
    shared.append([add(far,(x[-1]-1,F(0))),EX,ZERO])
    canonical = []
    delta = [F(0)]*3
    for i, old in enumerate(raw):
        d = x[i+1]-x[i]
        b = list(old)
        for end, inc, (p,vel,acc) in ((0,1,shared[i]),(9,-1,shared[i+1])):
            h = mul(inc*d/9,vel)
            b[end], b[end+inc], b[end+2*inc] = p, add(p,h), add(add(p,mul(2,h)),mul(d*d/72,acc))
        new = jets(b,d)
        for j in range(3):
            if new[j][0] != shared[i][j] or new[j][-1] != shared[i+1][j]:
                raise ArithmeticError('Exact canonical endpoint mismatch')
            delta[j] = max(delta[j],*(upper_norm(sub(a,c)) for a,c in zip(new[j],jraw[i][j],strict=True)))
        canonical.append(new)
    left = jets(elevated_line((F(-1),F(0)),shared[0][0]),x[0]+1)
    right = jets(elevated_line(shared[-1][0],far),1-x[-1])
    return [F(-1),*x,F(1)], [left,*jraw,right], [left,*canonical,right], delta


def component_range(b, i):
    vals = [p[i] for p in b]
    return min(vals), max(vals)


def product_interval(a, b):
    vals = [x*y for x in a for y in b]
    return min(vals), max(vals)


def curve_bounds(z):
    x, old, new, delta = canonical_data(z)
    cuts = sorted(set(x) | {-t for t in x})
    ay = proj = speed = None
    slope = accel = curvature = F(0)
    mismatch = [F(0)]*3
    for a,b in zip(cuts,cuts[1:]):
        center = (a+b)/2
        i,j = bisect_right(x,center)-1,bisect_right(x,-center)-1
        rows = []
        for d in (1,2):
            left = restrict(new[i][d],x[i],x[i+1],a,b)
            right = restrict(new[j][d],x[j],x[j+1],-b,-a)
            rows.append([mul(F(1,2),sub(p,mul((-1)**d,r))) for p,r in zip(left,reversed(right),strict=True)])
        vel,acc = rows
        vy,vz = component_range(vel,0),component_range(vel,1)
        low_y = vy[0]
        if low_y <= 0:
            raise ArithmeticError('Positive Y-speed on the finite curve not established')
        low_p = min((15*p[0]+8*p[1])/17 for p in vel)
        low_zabs = max(F(0),vz[0],-vz[1])
        low_speed = root_bounds(low_y**2+low_zabs**2)[0]
        if low_speed <= 0:
            raise ArithmeticError('Positive geometric speed not established')
        ay = low_y if ay is None else min(ay,low_y)
        proj = low_p if proj is None else min(proj,low_p)
        speed = low_speed if speed is None else min(speed,low_speed)
        slope = max(slope,max(map(abs,vz))/low_y)
        accel = max(accel,*map(upper_norm,acc))
        p = product_interval(vy,component_range(acc,1))
        r = product_interval(vz,component_range(acc,0))
        curvature = max(curvature,abs(p[0]-r[1])/low_speed**3,abs(p[1]-r[0])/low_speed**3)
    # At reflected coincident knots both original branch choices need individual checks.
    for v in cuts[1:-1]:
        for d in range(3):
            chosen = symtrace(old,x,v,'selected',d)
            for side in ('left','right'):
                mismatch[d] = max(mismatch[d],upper_norm(sub(chosen,symtrace(old,x,v,side,d))))
    return ay,proj,speed,slope,accel,curvature,delta,mismatch,len(cuts)-1


def check_axis(knots, lo, hi):
    if (knots.ndim != 1 or len(knots)<12 or not np.isfinite(knots).all()
            or np.any(knots[1:] < knots[:-1]) or knots[5] > lo or knots[-6] < hi):
        raise ValueError('Required closed physical support not covered')
    vals, counts = np.unique(knots,return_counts=True)
    if len(vals)<2 or counts[0]!=6 or counts[-1]!=6 or np.any(counts[1:-1]>3):
        raise ValueError('Quintic tensor spline lacks the required clamping or C2 knot multiplicity')


def strip_component(z, key, lo, hi, h):
    kt,kv,c = (z[key+'_'+str(i)] for i in range(3))
    check_axis(kt,0,h)
    check_axis(kv,lo,hi)
    if c.ndim!=1 or c.size!=(len(kt)-6)*(len(kv)-6) or not np.isfinite(c).all():
        raise ValueError('Actual position-spline coefficient order or size differs')
    low = high = c.reshape(len(kt)-6,len(kv)-6)
    dt = dv = 5
    for _ in range(3):
        low,high,kt,dt = derivative(low,high,kt,dt,0)
    values = [hull_abs(low,high,kt,kv,dt,dv,lo,hi,h)]
    for _ in range(2):
        low,high,kv,dv = derivative(low,high,kv,dv,1)
        values.append(hull_abs(low,high,kt,kv,dt,dv,lo,hi,h))
    return values


def consume_arrays(z, phase, sha256):
    """Caller supplies the open object returned by the R705 hash-verifying PaidArchive."""
    require_public()
    if not re.fullmatch('[0-9a-f]{64}',sha256) or float(z['phase']) != phase:
        raise ValueError('Missing actual phase or verified object identity')
    ay,proj,speed,slope,accel,curvature,delta,mismatch,n = curve_bounds(z)
    far = far_value(z)
    h_exact = mul(F(1,2),add(far,(F(-1),F(0))))
    original_center = (np.asarray([float(v) for v in far],dtype=np.float64)+np.array([-1.,0.]))/2
    center_gap = upper_norm(sub(h_exact,tuple(q(v) for v in original_center)))
    world_delta = [delta[0]+center_gap,delta[1],delta[2]]
    h = up(float(H))
    grids = []
    for grid in range(2):
        bands = []
        for j,(lo,hi) in enumerate(((-.909,-.611),(.611,.909))):
            comps = [strip_component(z,f'grid{grid}_pulse{j}_field{k}',down(lo),up(hi),h) for k in (2,3,4)]
            bands.append([q(norm_upper(row)) for row in zip(*comps,strict=True)])
        m30,m31,m32 = map(max,zip(*bands,strict=True))
        b = H**3*m30/6
        rt,rv = H**2*m30/2,H**3*m31/6
        e1 = rt+rv+235*b
        c = min(F(1),proj)-e1
        tt,tv,vv = H*m30,H**2*m31/2+235*rt,accel+H**3*m32/6+470*rv+94000*b
        hess = max(tt+tv,tv+vv)
        area = rt+(1+rt)*rv/speed
        transfer = H+b+2*TAU*area
        sep = F(2,5)/root_bounds(1+slope*slope)[1]-2*b
        cap_sheet = ay>0 and speed>=F(99,100) and curvature<=F(211,50)
        metric = 2*delta[1]/c+(delta[1]/c)**2 if c>0 else None
        vals = {'c_lower':c,'hessian_upper':hess,'X_minus_B_upper':b,'DE_upper':e1,
                'opposite_distance_lower':sep,'area_error_upper':area,'cap_transfer_upper':transfer}
        grids.append(dict(grid=grid, bounds={k:bounds_text(v) for k,v in vals.items()},
            pulse_M30_M31_M32=[[bounds_text(v) for v in row] for row in bands],
            canonical_metric_relative_change_upper=bounds_text(metric) if metric is not None else None,
            canonical_same_sheet=bool(c>0 and TAU*hess<=c*c), canonical_opposite_sheet=bool(sep>2*TAU),
            canonical_registered_true_caps_to_sheet=bool(cap_sheet),
            canonical_registered_true_caps_to_strip=bool(cap_sheet and area<1 and transfer<F(1,1000))))
    return dict(actual_npz_sha256=sha256,phase=phase,common_bernstein_spans=n,
                curve_bounds={k:bounds_text(v) for k,v in zip(('Y_speed_lower','projection_lower',
                     'speed_lower','abs_Z_slope_upper','acceleration_upper','curvature_upper'),
                     (ay,proj,speed,slope,accel,curvature),strict=True)},
                centered_raw_to_canonical_orders_012=[bounds_text(v) for v in delta],
                world_raw_to_canonical_orders_012=[bounds_text(v) for v in world_delta],
                exact_center_minus_R705_binary_center_norm_upper=bounds_text(center_gap),
                actual_selected_to_one_sided_orders_012=[bounds_text(v) for v in mismatch],
                grids=grids,canonical_shared_C2=True,
                raw_original_C2_claimed=False,original_source_target_same_metric_claimed=False,
                all_phase_or_unknown_window_claimed=False)
