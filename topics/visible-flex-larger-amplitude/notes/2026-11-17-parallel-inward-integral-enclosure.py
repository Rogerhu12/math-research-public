#!/usr/bin/env python3
"""Exact interval certificate for the inward reference meridian integrals.

The mathematical profile is defined by exact curvature/position integrals.
This is not a floating Gauss evaluator certificate or a nonlinear tail solve.
Raw input/report remain outside the repository. All bounds use integers and
Fraction, including composite-midpoint remainders, arcsine and square roots.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import json
from math import comb, isqrt
from pathlib import Path

HELPER = Path(__file__).with_name('2026-11-17-parallel-geometry-inward-chord-cover.py')
HELPER_SHA = 'e480a2ca7ebd5911768cad04ef7b98319ff2cff1840cf71531eaf2b574b4211a'
PARENT_SHA = 'd6441e642b0bb0903915d42e0d4dd9fd564a2e0378e32070110fe6cc7922403f'
if hashlib.sha256(HELPER.read_bytes()).hexdigest() != HELPER_SHA:
    raise ValueError('The frozen outward integer trigonometric helper changed')
spec = importlib.util.spec_from_file_location('frozen_integer_trig', HELPER)
h = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h)
S = h.S


def box(low, high):
    return h.floor(Q(low)*S), h.ceil(Q(high)*S)


def subtract(a, b):
    return h.add(a, h.neg(b))


def divide(a, b):
    if b[0] <= 0:
        raise ArithmeticError('Positive denominator interval required')
    quotients = [Q(x*S, y) for x in a for y in b]
    return h.floor(min(quotients)), h.ceil(max(quotients))


def square_root(a):
    if a[0] < 0:
        raise ArithmeticError('Negative square-root interval')
    low = isqrt(a[0]*S)
    high = isqrt(a[1]*S)
    return low, high + int(high*high < a[1]*S)


def arcsine(a):
    low, high = Q(a[0], S), Q(a[1], S)
    if not 0 <= low <= high < 1:
        raise ArithmeticError('The positive arcsine series requires [0,1)')
    def partial(x):
        return sum((Q(comb(2*j, j), 4**j*(2*j+1))*x**(2*j+1)
                    for j in range(32)), Q(0))
    # Every remaining positive coefficient is <=1.
    remainder = high**65/(1-high*high)
    return h.floor(partial(low)*S), h.ceil((partial(high)+remainder)*S)


def enclosure(a):
    return dict(lower_exact=str(Q(a[0], S)), upper_exact=str(Q(a[1], S)),
                approximate=[float(Q(a[0], S)), float(Q(a[1], S))])


def contains(interval, value):
    return Q(interval[0], S) <= value <= Q(interval[1], S)


def main(args):
    raw = args.input.read_bytes()
    if hashlib.sha256(raw).hexdigest() != PARENT_SHA:
        raise ValueError('Require the declared accepted .995 parent bytes')
    parent = json.loads(gzip.decompress(raw))
    if not parent.get('success'):
        raise ValueError('The parent is not accepted')
    extension = parent['extension_scalar']
    nodal = parent['fixed_scalar_profile']['geometry']['knots'][-1]
    origin = Q.from_float(float(parent['analytic_extension_origin']))
    cut = Q.from_float(float(parent['mesh'][-1]))
    if origin != Q.from_float(float(nodal['s'])) or not origin < cut:
        raise ValueError('The analytic origin must equal the actual last scalar knot')
    # These boxes cover both exact stored nodal jets and the numerical
    # evaluator's slightly different recorded start constants.
    a0 = box('1.16660641061202', '1.16660641061204')
    v0 = box('.35794863891029', '.35794863891032')
    u0 = box('-2.01012061072760', '-2.01012061072757')
    for interval, node_key, saved_key in [(a0,'a','a0'), (v0,'ap','v0'), (u0,'app','u0')]:
        for value in (nodal[node_key], extension[saved_key]):
            if not contains(interval, Q.from_float(float(value))):
                raise ArithmeticError('A declared starting-jet box missed a source value')
    one = h.interval(Q(1))
    K = divide(h.neg(u0), square_root(subtract(one, h.multiply(v0, v0))))
    if not contains(K, Q.from_float(float(extension['angular_curvature']))):
        raise ArithmeticError('The recorded curvature is outside the exact jet-derived interval')
    if not Q(3,2) < Q(K[0],S) <= Q(K[1],S) < Q(2153,1000):
        raise ArithmeticError('The declared ramp derivative budget does not apply')
    alpha_origin = arcsine(v0)
    alpha0 = subtract(alpha_origin, h.scale(K, cut-origin))
    ac = h.add(a0, divide(subtract(h.sine_cosine(alpha0)[1],
                                  h.sine_cosine(alpha_origin)[1]), K))
    hin = Q.from_float(.02)
    hout = Q.from_float(.02)
    k1 = Q(3,2)
    pi = h.pi_interval()
    alpha1 = subtract(alpha0, h.scale(h.add(K,h.interval(k1)), hin/2))
    alpha2 = h.add(h.scale(pi, -Q(1,2)), h.interval(k1*hout/2))
    plateau = h.scale(subtract(alpha1,alpha2), 1/k1)
    if plateau[0] <= 0:
        raise ArithmeticError('The constant-curvature interval must be positive')
    length = h.add(plateau, h.interval(hin+hout))

    def primitive(u):
        return Q(5,2)*u**4-3*u**5+u**6

    def midpoint_transition(final):
        width = hout if final else hin
        sr, sz = (0,0), (0,0)
        for j in range(args.panels):
            u = Q(2*j+1, 2*args.panels)
            P = primitive(u)
            if final:
                angle = subtract(alpha2, h.interval(k1*width*(u-P)))
            else:
                drop = h.add(h.scale(K,width*(u-P)),h.interval(k1*width*P))
                angle = subtract(alpha0,drop)
            sn, cs = h.sine_cosine(angle)
            sr, sz = h.add(sr,sn), h.add(sz,cs)
        # |(sin alpha)''| and |(cos alpha)''| <= kappa^2+|kappa'|.
        # max smoothstep'=15/8; K<2.153 and K-1.5<.653.
        second = (k1*k1+k1*Q(15,8)/width if final else
                  Q(2153,1000)**2+Q(653,1000)*Q(15,8)/width)
        error = width**3*second/(24*args.panels**2)
        error_box = box(-error,error)
        return (h.add(h.scale(sr,width/args.panels),error_box),
                h.add(h.scale(sz,width/args.panels),error_box), error)

    rin, zin, error_in = midpoint_transition(False)
    rout, zout, error_out = midpoint_transition(True)
    sin1, cos1 = h.sine_cosine(alpha1)
    sin2, cos2 = h.sine_cosine(alpha2)
    rplateau = h.scale(subtract(cos2,cos1),1/k1)
    zplateau = h.scale(subtract(sin1,sin2),1/k1)
    radius = h.add(ac,h.add(rin,h.add(rplateau,rout)))
    height = h.add(zin,h.add(zplateau,zout))
    radius_target = box('.531878','.531880')
    length_lower = Q('1.289716')
    if not radius_target[0] < radius[0] <= radius[1] < radius_target[1]:
        raise ArithmeticError('R634 radius condition was not certified')
    if not Q(length[0],S) > length_lower:
        raise ArithmeticError('R634 length condition was not certified')
    result = dict(scope=__doc__, source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        helper_sha256=HELPER_SHA, parent_sha256=PARENT_SHA, panels_per_ramp=args.panels,
        input_boxes={k:enclosure(v) for k,v in [('a0',a0),('v0',v0),('u0',u0)]},
        origin_exact=str(origin), cut_exact=str(cut), ramp_in_exact=str(hin), ramp_out_exact=str(hout),
        curvature_exact=str(k1), initial_curvature=enclosure(K), initial_angle=enclosure(alpha0),
        cut_radius=enclosure(ac), plateau=enclosure(plateau), reference_length=enclosure(length),
        terminal_radius=enclosure(radius), reference_height_increment=enclosure(height),
        midpoint_error_in_exact=str(error_in), midpoint_error_out_exact=str(error_out),
        midpoint_error_total=float(error_in+error_out), R634_integral_conditions_certified=True,
        arithmetic='Python integers/Fraction; outward 10^-24 grid; exact midpoint remainder',
        binding='Exact integral reference profile; not finite-GL literal differentiation or a solved tail',
        nonlinear_tail_exists=False, closed_surface=False)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--panels',type=int,default=64)
    args=p.parse_args()
    if args.panels<1:
        raise ValueError('Positive midpoint panel count required')
    main(args)
