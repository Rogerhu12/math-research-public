#!/usr/bin/env python3
"""Exact rational curvature corollary of the closed R136 scalar packet.

This does not run an ODE, resample a profile, or recertify R136's interval
construction. It consumes that immutable proved packet and checks the extra
algebraic inequalities needed for the whole round delta=0 reference.
"""
from __future__ import annotations

import argparse
from decimal import Decimal
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time


CANDIDATE_SHA = '7c3f31de4b230e8d98b99c3e3914d65ae69daa3cb5c54ae22f585a36a888bfd1'
PACKET_SHA = '3c9fa775b8cb94b93c1a39fc7ab68814c0efa271812271d3e5183d030b7d3695'
PACKET_SOURCE_SHA = 'a33c214dffc98dd2b5c09a5d3d1d130726d1ff8abb997162a9d70b59cacbe5ae'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def scalar(value):
    return F.from_float(value) if isinstance(value, float) else F(value)


def interval(packet):
    return F(packet['lower_exact']), F(packet['upper_exact'])


def absolute_upper(pair):
    return max(abs(pair[0]), abs(pair[1]))


def number(value):
    return dict(exact=str(value), display=float(value))


def run_encoding(encoding, candidate):
    if not (encoding['radius_lower_proved']
            and encoding['exact_radius_lower'] == '4/5'
            and encoding['exact_shared_Hermite_two_jets']
            and encoding['hermite_velocity_nonnegative_and_less_than_one']
            and encoding['phase_sign_pattern_proved']):
        raise ValueError('Required inherited R136 hypotheses were not proved')
    rows = encoding['hermite_rows']
    velocity = max(F(r['velocity_upper_exact']) for r in rows)
    acceleration = max(max(abs(F(r['acceleration_control_lower_exact'])),
                           abs(F(r['acceleration_control_upper_exact']))) for r in rows)
    # b=sqrt(1-v^2), |l|=|a_ss|/b.  Compare squares, without a
    # floating square-root or a rounded bound on b.
    hermite_passed = (0 <= velocity < 1 and
                     acceleration**2 < 4*(1-velocity**2))
    definitions = {r['label']: r for r in candidate['segments']}
    phase_checks = []
    bridge_bounds = []
    turn_bounds = []
    brake_bound = None
    for row in encoding['phase_rows']:
        definition = definitions[row['label']]
        kind = definition['kind']
        length = F(row['L_exact'])
        p0, p1 = interval(row['start_phase']), interval(row['end_phase'])
        if length <= 0:
            raise ValueError('Nonpositive inherited phase length')
        if kind == 'phase_bridge':
            v0, v1 = scalar(definition['ps0']), scalar(definition['ps1'])
            delta = (p1[0]-p0[1], p1[1]-p0[0])
            if row['label'] == 'cut_second_jet_brake':
                if (v0 != 0 or v1 != 0 or
                        definition.get('exact_endpoint_phase') != '-pi/2'):
                    raise ValueError('The accurate zero-slope pi endpoint is absent')
                # phi=p0+(p1-p0)(3t^2-2t^3), max 6t(1-t)=3/2.
                bound = 3*absolute_upper(delta)/(2*length)
                passed = bound < 7
                brake_bound = bound
                method = 'zero-end-slope cubic derivative; 6t(1-t)<=3/2'
            else:
                # Quadratic Bernstein controls of d(phi)/ds.
                middle = (3*delta[0]/length-v0-v1,
                          3*delta[1]/length-v0-v1)
                bound = max(abs(v0), abs(v1), absolute_upper(middle))
                passed = bound < F(7, 2)
                bridge_bounds.append(bound)
                method = 'convex hull of quadratic Bernstein derivative controls'
        elif kind == 'turn':
            if not definition.get('length_from_turn_rate'):
                raise ValueError('Turn length is not defined from the peak rate')
            bound = abs(scalar(definition['K']))
            passed = bound < F(7, 2)
            turn_bounds.append(bound)
            method = 'R136 exact soft-turn normalization; ramp in [0,1]'
        elif kind == 'coast':
            bound, passed = F(0), True
            method = 'constant phase'
        else:
            raise ValueError(f'Unexpected phase-row kind: {kind}')
        phase_checks.append(dict(label=row['label'], kind=kind,
                                 absolute_phi_s_upper=number(bound),
                                 method=method, passed=passed))
    deep = interval(encoding['derived_deep_coast'])
    passed = bool(hermite_passed and all(r['passed'] for r in phase_checks)
                  and deep[0] > 0 and brake_bound is not None)
    return dict(
        encoding=encoding['encoding'], passed=passed,
        inherited_radius_lower='4/5', inherited_phase_range='[-pi/2,3/10]',
        hermite_count=len(rows), hermite_velocity_upper=number(velocity),
        hermite_acceleration_absolute_upper=number(acceleration),
        hermite_squared_margin_for_abs_l_lt_2=number(4*(1-velocity**2)-acceleration**2),
        hermite_abs_l_strict_upper='2', phase_checks=phase_checks,
        central_and_derived_deep_coast_abs_l='0',
        azimuthal_curvature_absolute_upper='5/4',
        terminal_brake_abs_l_upper=number(brake_bound),
        global_principal_curvature_absolute_strict_upper='7',
        exact_flat_annulus_extension_curvature='0')


def main():
    root = Path(__file__).resolve().parent.parent
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate', type=Path, default=root/'notes/2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json')
    ap.add_argument('--packet', type=Path, default=root/'notes/2026-11-12-fd2d-peak-spacer34-radius-certificate-02.json')
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists():
        raise FileExistsError(args.out)
    started = time.monotonic()
    if digest(args.candidate) != CANDIDATE_SHA or digest(args.packet) != PACKET_SHA:
        raise ValueError('This corollary is bound to the named immutable candidate and packet')
    packet = json.loads(args.packet.read_text())
    if (not packet['passed'] or packet['candidate_sha256'] != CANDIDATE_SHA
            or packet['source_sha256'] != PACKET_SOURCE_SHA):
        raise ValueError('The inherited certificate identity or result differs')
    candidate_binary = json.loads(args.candidate.read_text())
    candidate_decimal = json.loads(args.candidate.read_text(), parse_float=Decimal)
    encodings = []
    for e in packet['encodings']:
        if e['encoding'] == 'exact binary64 numerical data':
            definition = candidate_binary
        elif e['encoding'] == 'exact written decimal numerical data':
            definition = candidate_decimal
        else:
            raise ValueError('Unrecognized inherited arithmetic semantics')
        encodings.append(run_encoding(e, definition))
    result = dict(
        schema='fd2d-whole-round-prefix-curvature-rational-corollary-v1',
        actual_execution=True, candidate_sha256=CANDIDATE_SHA,
        inherited_packet_sha256=PACKET_SHA,
        inherited_packet_source_sha256=PACKET_SOURCE_SHA,
        consumer_source_sha256=digest(__file__),
        encodings=encodings, passed=all(e['passed'] for e in encodings),
        seconds=time.monotonic()-started,
        scope='Whole accurate surface-of-revolution prefix for the immutable base delta=0 metric, with zero-control flat annulus extension. A corollary of the closed R136 scalar packet. No new ODE, BVP, noncircular branch, nonlocal reach, held-point or strong-target certificate.')
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(passed=result['passed'], seconds=result['seconds'],
        encodings=[dict(encoding=e['encoding'],
            hermite_abs_l_strict_upper=e['hermite_abs_l_strict_upper'],
            terminal_brake_abs_l_upper=e['terminal_brake_abs_l_upper']['display'],
            global_principal_curvature_absolute_strict_upper=e['global_principal_curvature_absolute_strict_upper'])
            for e in encodings]), allow_nan=False))
    if not result['passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
