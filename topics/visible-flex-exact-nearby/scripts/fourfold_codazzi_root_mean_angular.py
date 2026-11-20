#!/usr/bin/env python3
"""New full-circle root mean denominator; public Actions execution only.

The source imports no scientific package at module import. It reads only the
accepted root germ and original candidate definition. The existing axis source
is used as a pure input loader/definition helper; its axis target is never
called. No q/s axis value, old geometry trajectory, or completed scientific
target is recomputed.

On each of 8192 entire angular cells, complete trigonometric interval values
enclose the repaired skew connection and mean-direction coefficients. A
constant exact skew midpoint propagates the private nominal frame through
Rodrigues' formula. Its distance from the ideal orthogonal frame increases
only by h*||Omega-Omega_mid|| plus the directed nominal rounding radius.
Whole-cell frame enclosures, not endpoint samples, enclose the mean integral.
W.16 pays the separate ideal-to-actual periodic-frame fee 11/10^7.

Only scalar conclusions, counts, identities and scopes are published.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import time

DEFINITION_SHA = 'd152f31cef53c1d58099cf3d1f994d2dad9d31d6a75cb42a7d9e54a35c17ae79'
CELLS = 8192
BITS = 320
ACTUAL_FRAME_FEE = Fraction(11, 10**7)
KIND = 'R138_same_Qrepair_true_root_full_circle_mean_denominator_v1'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, value):
    raw = (json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False)+'\n').encode()
    temporary = Path(str(path)+'.partial')
    temporary.write_bytes(raw)
    temporary.replace(path)
    if path.read_bytes() != raw:
        raise OSError('complete scalar result failed exact byte readback')


def run(args):
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
        or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('new scientific execution requires the repository public Actions')
    if args.output.exists():
        raise FileExistsError('preserve this completed or failed new angular target')
    if sha(args.definition_source) != DEFINITION_SHA:
        raise ValueError('the pure original input/definition helper changed')
    spec = importlib.util.spec_from_file_location('root_definition_only', args.definition_source)
    definition = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(definition)
    from flint import arb, ctx
    ctx.prec = BITS
    started = time.monotonic()
    args.output.parent.mkdir(parents=True, exist_ok=True)

    def rat(value):
        value = Fraction(value)
        return arb(value.numerator)/value.denominator

    def magnitude(value):
        return abs(value).upper()

    def unpack(record):
        exponent = int(record['decimal_exponent'])
        scale = rat(10**exponent) if exponent >= 0 else rat(Fraction(1, 10**(-exponent)))
        midpoint = rat(int(record['midpoint_integer']))*scale
        radius = rat(int(record['radius_integer']))*scale
        return (midpoint-radius).lower().union((midpoint+radius).upper())

    def recorded(value):
        if not value.is_finite():
            raise ValueError('a new whole scalar enclosure is nonfinite')
        m, r, e = value.mid_rad_10exp(70)
        record = dict(kind='complete_decimal_ball_v1', midpoint_integer=str(int(m)),
                      radius_integer=str(int(r)), decimal_exponent=str(int(e)))
        if int(r) < 0 or not unpack(record).contains(value):
            raise ValueError('new decimal scalar did not enclose its entire original ball')
        return record

    def norm(values):
        return sum((magnitude(v)**2 for v in values), arb(0)).sqrt().upper()

    def mm(a, b):
        return [[sum((a[i][k]*b[k][j] for k in range(3)), arb(0))
                 for j in range(3)] for i in range(3)]

    def rotation(w, elapsed):
        """The exact exp(elapsed*Omega(w)), in complete directed balls."""
        w1, w2, w3 = w
        skew = [[arb(0),-w1,-w2],[w1,arb(0),-w3],[w2,w3,arb(0)]]
        squared = mm(skew, skew)
        speed = sum((x*x for x in w), arb(0)).sqrt()
        if not speed > 0:
            raise ValueError('the nonzero a/m skew speed was lost')
        sine = (elapsed*speed).sin()/speed
        cosine = (arb(1)-(elapsed*speed).cos())/(speed*speed)
        return [[arb(int(i==j))+sine*skew[i][j]+cosine*squared[i][j]
                 for j in range(3)] for i in range(3)]

    germ = definition.read(args.germ, definition.GERM_SHA)
    candidate, nodes, cc = definition.load_candidate(args.candidate)
    alpha = Fraction(candidate['metadata']['exact_float_amplitude'])
    if (not germ['complete'] or not germ['proved'] or germ['failure'] is not None
        or germ['candidate_sha256'] != definition.CANDIDATE_SHA
        or germ['object_sha256'] != definition.OBJECT_SHA
        or Fraction(germ['exact_amplitude']) != alpha
        or Fraction(germ['actual_fixed_nu']) != definition.NU
        or Fraction(germ['exact_center_parameter']) != definition.ETA
        or not germ['whole_affine_parameter_interval']
        or tuple(map(Fraction, germ['root_interval'])) != (definition.ROOT_LO, definition.ROOT_HI)
        or germ['actual_candidate_piece'] != 2549
        or not germ['compact_bump_identically_zero_on_entire_actual_germ']):
        raise ValueError('the accepted same-object true-root germ scope differs')
    radial = tuple(map(Fraction, germ['complex_radial_rectangle']['real_interval']))
    scalar = tuple(map(Fraction, germ['original_scalar_germ']))
    if (not nodes[2549] <= definition.ROOT_LO < definition.ROOT_HI <= nodes[2550]
        or not radial[0] <= definition.ROOT_LO < definition.ROOT_HI <= radial[1]
        or not scalar[0] <= definition.ROOT_LO < definition.ROOT_HI <= scalar[1]):
        raise ValueError('the whole true root interval leaves an original germ')
    # Private definition materialization; no array leaves this process.
    background = definition.private_root_angular_definition(germ, candidate, nodes, cc, arb)
    a, b0, mean = background['a'], background['b0'], background['mean_v']
    us, vc = background['u_sine'], background['v_cosine']
    if (not a > 0 or not mean < 0 or len(us) != 32 or len(vc) != 33
        or background['physical_frequency_factor'] != 4):
        raise ValueError('the complete genuine root Fourier definition differs')
    del cc, nodes

    identity = dict(kind=KIND, source_sha256=sha(__file__), definition_source_sha256=DEFINITION_SHA,
                    candidate_sha256=definition.CANDIDATE_SHA, germ_sha256=definition.GERM_SHA,
                    object_sha256=definition.OBJECT_SHA,
                    repair_definition_sha256=definition.REPAIR_DEFINITION_SHA,
                    eta=str(definition.ETA), actual_nu=str(definition.NU),
                    exact_root_interval=[str(definition.ROOT_LO),str(definition.ROOT_HI)],
                    complete_angular_interval='[0,2*pi]', cells=CELLS,
                    arithmetic_bits=BITS, actual_periodic_frame_fee=str(ACTUAL_FRAME_FEE),
                    frame_at_zero='X=e_z,Y=e_y,n=e_x; one proper ambient rotation',
                    projection_vector='ell=X(root,0)=local e_z')
    document = dict(identity=identity, complete=False, proved=False, failure=None,
                    completed_cells=0, current_target='whole_true_root_mean_integral',
                    original_scientific_calls=0, old_axis_target_calls=0,
                    old_geometry_target_calls=0, arrays_published=False,
                    scope=dict(same_Qrepair_actual_periodic_frame=True,
                               actual_mean_denominator_nonzero=False,
                               actual_mean_denominator_positive=False,
                               full_root_energy_positive=False,
                               positive_inverse_proved=False, final_topic_complete=False))
    save(args.output,document)
    two_pi = 2*arb.pi()
    width = two_pi/CELLS
    full_local_time = arb(0).union(width.upper())
    nominal = [[arb(0),arb(0),arb(1)],
               [arb(0),arb(1),arb(0)],
               [arb(1),arb(0),arb(0)]]
    frame_error = arb(0)
    integral = arb(0)
    coefficient_integral = arb(0)
    maximum_connection_error = arb(0)

    for index in range(CELLS):
        phi = (two_pi*index/CELLS).lower().union((two_pi*(index+1)/CELLS).upper())
        u, v, up, vp, primitive = arb(0), mean, arb(0), arb(0), arb(0)
        for j in range(1,33):
            sine, cosine = (4*j*phi).sin(), (4*j*phi).cos()
            u += us[j-1]*sine
            v += vc[j]*cosine
            up += (4*j)*us[j-1]*cosine
            vp -= (4*j)*vc[j]*sine
            primitive += vc[j]*sine/(4*j)
        if not v < 0:
            raise ValueError('a complete root angular cell lost the real v gap')
        q0 = -primitive/mean
        A0 = 1/v-q0*vp/(v*v)
        B0 = -u*A0-q0*up/v
        rho = a/mean
        omega = [b0*v/mean,a*u/mean,a/mean]
        centre = [x.mid() for x in omega]
        connection_error = norm([x.rad() for x in omega])
        maximum_connection_error = maximum_connection_error.union(connection_error).upper()
        # All phi in this whole cell, not merely its midpoint.
        enclosure = mm(nominal, rotation(centre,full_local_time))
        local_error = (frame_error+width.upper()*connection_error).upper()
        for row in enclosure:
            for j in range(3):
                row[j] += arb(0,local_error)
        mean_direction_z = rho*(A0*enclosure[2][0]+B0*enclosure[2][1])
        integral += mean_direction_z/CELLS
        coefficient_integral += (magnitude(rho)*norm([A0,B0]))/CELLS

        # Orthogonal comparison pays coefficient and arithmetic error once.
        advanced = mm(nominal,rotation(centre,width))
        arithmetic_error = norm([value.rad() for row in advanced for value in row])
        frame_error = (local_error+arithmetic_error).upper()
        nominal = [[value.mid() for value in row] for row in advanced]
        if not frame_error < 1:
            raise ValueError('complete new frame enclosure exceeded the declared finite guard')
        if (index+1) % 128 == 0 or index+1 == CELLS:
            document.update(completed_cells=index+1,
                            completed_integral_prefix=recorded(integral),
                            coefficient_integral_prefix_upper=recorded(coefficient_integral.upper()),
                            accumulated_frame_error_upper=recorded(frame_error),
                            seconds=time.monotonic()-started)
            save(args.output,document)
            print(json.dumps(dict(completed_cells=index+1,cells=CELLS)),flush=True)

    ideal_record = recorded(integral)
    coefficient_record = recorded(coefficient_integral.upper())
    ideal_saved = unpack(ideal_record)
    coefficient_saved = unpack(coefficient_record).upper()
    actual_fee = (rat(ACTUAL_FRAME_FEE)*coefficient_saved).upper()
    actual_record = recorded(ideal_saved+arb(0,actual_fee))
    actual_saved = unpack(actual_record)
    positive = bool(actual_saved > 0)
    negative = bool(actual_saved < 0)
    document.update(complete=True,proved=True,current_target=None,
                    ideal_mean_denominator=ideal_record,
                    complete_mean_direction_coefficient_upper=coefficient_record,
                    actual_frame_transfer_fee=recorded(actual_fee),
                    actual_mean_denominator=actual_record,
                    maximum_complete_cell_connection_error_upper=recorded(maximum_connection_error),
                    complete_frame_error_upper=recorded(frame_error),
                    strict_sign_uses_complete_saved_decimal_ball=True,
                    seconds=time.monotonic()-started)
    document['scope'].update(actual_mean_denominator_nonzero=positive or negative,
                             actual_mean_denominator_positive=positive)
    save(args.output,document)
    print(json.dumps(dict(complete=True,actual_denominator_positive=positive,
                          actual_denominator_nonzero=positive or negative,
                          output=str(args.output))),flush=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--definition-source',type=Path,required=True)
    parser.add_argument('--germ',type=Path,required=True)
    parser.add_argument('--candidate',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    try:
        run(args)
    except Exception as error:
        if args.output.exists():
            document=json.loads(args.output.read_text())
            if not document.get('complete'):
                document['failure']=dict(type=type(error).__name__,message=str(error))
                save(args.output,document)
        raise


if __name__=='__main__':
    main()
