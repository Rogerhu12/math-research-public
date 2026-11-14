#!/usr/bin/env python3
"""Sample actual C2 axisymmetric loop double-normal chord equations.

This examines the two loop turns and their connecting coast only. It is
neither a reach certificate nor a substitute for the complete nonaxis field.
"""
import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import numpy as np
from scipy.optimize import brentq

P = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('loop_bottleneck_flat', P/'alternative-neck-flatturn.py')
fl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fl)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--radius', type=float, default=.35)
    ap.add_argument('--ratio', type=float, default=1.1)
    ap.add_argument('--speed', type=float, default=.985)
    ap.add_argument('--curvature', type=float, default=7.5)
    ap.add_argument('--samples', type=int, default=2001)
    ap.add_argument('--out', type=Path, required=True)
    a = ap.parse_args()
    pmax = math.asin(a.speed)
    beta = math.sqrt(1-a.speed*a.speed)
    first = fl.turn(-pmax, pmax, a.curvature)
    second = fl.turn(pmax, -pmax, a.curvature)
    coast_length = (a.ratio-1)*a.radius/a.speed
    coast_height = coast_length*beta

    def at_phase(seg, p):
        if p == seg['p0']:
            u = 0.
        elif p == seg['p1']:
            u = 1.
        else:
            u = brentq(lambda v: float(fl.phase(seg, v))-p, 0, 1, xtol=1e-14)
        return seg['length']*np.array([float(fl.integral(seg, u)), float(fl.integral(seg, u, 'cos'))])

    def point1(p):
        return np.array([a.radius, 0.])+at_phase(first, p)

    def point2(p):
        return np.array([a.ratio*a.radius, first['dh']+coast_height])+at_phase(second, p)

    def same(p):
        d = point2(p)-point1(p)
        return float(d @ np.array([math.sin(p), math.cos(p)]))

    def opposite(p):
        x, y = point1(p), point2(-p)
        return float((y[1]-x[1])*math.cos(p)-(x[0]+y[0])*math.sin(p))

    grid = np.linspace(-pmax, pmax, a.samples)
    values = np.array([same(float(p)) for p in grid])
    roots = []
    for l, r, vl, vr in zip(grid[:-1], grid[1:], values[:-1], values[1:]):
        if vl*vr < 0:
            p = brentq(same, l, r, xtol=1e-13)
            chord = float(np.linalg.norm(point2(p)-point1(p)))
            roots.append(dict(phase=p, chord=chord, half_chord=chord/2))
    p = brentq(opposite, 0., pmax, xtol=1e-13)
    x, y = point1(p), point2(-p)
    opposite_chord = float(np.hypot(x[0]+y[0], y[1]-x[1]))
    # Parallel incoming/outgoing lines with velocity -speed. This separation
    # is only a local-loop candidate, not a full-surface lower bound.
    shift = np.array([(a.ratio-1)*a.radius, first['dh']+second['dh']+coast_height])
    parallel_separation = abs(float(shift @ np.array([-beta, -a.speed])))
    result = dict(scope=__doc__, parameters={k:v for k,v in vars(a).items() if k != 'out'},
                  turn1=first, turn2=second,
                  coast_length=coast_length, coast_height=coast_height,
                  same_angle_equation_sample_min=float(values.min()),
                  same_angle_equation_sample_max=float(values.max()),
                  same_angle_cross_turn_roots=roots,
                  opposite_angle_cross_turn=dict(phase=p, first_point=x.tolist(),
                                                  second_point=y.tolist(), chord=opposite_chord,
                                                  half_chord=opposite_chord/2),
                  parallel_descending_line_separation=parallel_separation,
                  parallel_descending_half_separation=parallel_separation/2,
                  local_background_curvature_radius=1/a.curvature,
                  statement='No cross-turn same-angle root was found on this grid. These partial background checks do not certify continuous reach or exclude other nonlocal bottlenecks.',
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    a.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
