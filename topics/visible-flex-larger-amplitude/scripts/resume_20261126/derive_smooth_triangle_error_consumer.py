#!/usr/bin/env python3
"""Pure stdlib construction of the R713 complete actual-batch fee consumer."""
import argparse
import ast
import hashlib
from pathlib import Path


PARENT = '85e90f67a588f886f068532d76d678aa9fd8e24c1283f73e24d4f5e00ac172b9'
PINS = {
    '30ea80ec0673f3bdff3e59b97dfb5f7166a296aeb4b989fbca18b2feb5e9544c': '0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b',
    'bd9c0761e101679b10ff52d50f27a3dfb964687130c59878d756389b304ee771': 'f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917',
    'd788f4f07559b9375247874abbd57ec7d493a1cb4f543b8ab9f31f8dab3d128b': '3914004ac39b838c33411bd11660bb8fbec1372630c3569f3ea4ad5ae16c0f97',
    'e482428ee68aefa23da5b3b5c0a6b3363f047b0457f67a9193044ef151caec35': 'fd95d91abe9525cbfa34d55bd576be7dfba1fe25fcafb73bdaaea40e003ad65f',
}


def replace(text, old, new, count=1):
    if text.count(old) != count:
        raise ValueError(('complete-source replacement mismatch', old, text.count(old), count))
    return text.replace(old, new)


NEW_FUNCTIONS = r'''
@lru_cache(maxsize=32)
def _complete_absolute_profile_moments(delta, maximum_degree):
    """Exact Fraction moments of all twelve R711 pieces, with no quadrature.

    I5(u)=(5/2)u^4-3u^5+u^6.  Its nth power is advanced by exact
    polynomial convolution.  Both ramps and the complete linear middle of
    every quarter are included before the four-quarter symmetry is used.
    """
    delta = fraction(delta)
    if not 0 < delta < Fraction(1, 8):
        raise ValueError('Use the full R711 profile delta in (0,1/8)')
    if (isinstance(maximum_degree, bool) or not isinstance(maximum_degree, int)
            or maximum_degree < 0):
        raise ValueError('Use a nonnegative exact moment degree')
    c = Fraction(1, 4)-delta
    k = delta/c
    polynomial = [Fraction(1)]
    integrals = []
    for degree in range(maximum_degree+1):
        integrals.append(sum((value/Fraction(j+1)
                              for j, value in enumerate(polynomial)), Fraction(0)))
        if degree < maximum_degree:
            following = [Fraction(0)]*(len(polynomial)+6)
            for j, value in enumerate(polynomial):
                following[j+4] += Fraction(5, 2)*value
                following[j+5] -= 3*value
                following[j+6] += value
            polynomial = following
    moments = []
    for degree in range(maximum_degree+1):
        first_ramp = delta*k**degree*integrals[degree]
        last_ramp = delta*sum((Fraction((-1)**j*math.comb(degree, j))
                    *k**j*integrals[j] for j in range(degree+1)), Fraction(0))
        middle = c*((1-k/2)**(degree+1)-(k/2)**(degree+1))/Fraction(degree+1)
        moment = 4*(first_ramp+middle+last_ramp)
        if not 0 <= moment <= 1 or (degree == 0 and moment != 1):
            raise ValueError('The exact complete profile moment identity was not retained')
        moments.append(moment)
    return tuple(moments)


def complete_profile_moment_enclosures(seed, lambda_word, *, bits=160, series_order=48):
    """All three accurate A/A'/A'' boxes at this literal working amplitude.

    These are integrals of the exact R711 profile, not enclosures obtained by
    assuming the working 192-node moment quadrature is exact.  The full moment
    difference to those actual words is computed by the consuming function.
    """
    require_actions()
    if (seed.get('schema') != 'complete-supported-smooth-triangle-meridian-seed-reference-v1'
            or seed.get('source_sha256') != PROVIDER_SHA
            or seed.get('mean_kernel_source_sha256') != KERNEL_SHA
            or seed.get('mathematical_profile_piece_count') != 12
            or seed.get('mathematical_amplitude_interval') != '(0,pi)'):
        raise ValueError('Bind the complete independent R711 profile definition')
    delta = Fraction(seed['exact_profile_delta'])
    if (isinstance(series_order, bool) or not isinstance(series_order, int)
            or series_order < 2 or series_order % 2):
        raise ValueError('The complete simultaneous derivative series uses one even L>=2')
    if not isinstance(lambda_word, str):
        raise TypeError('Bind the actual canonical binary64 amplitude word')
    x = word(lambda_word)
    moments = _complete_absolute_profile_moments(delta, series_order+1)
    x_box = Interval(x, x, bits)
    x2 = x_box*x_box
    values = []
    remainders = []
    for derivative in range(3):
        first_even = 0 if derivative == 0 else 2
        total = Interval(0, 0, bits)
        for degree in range(series_order, first_even-1, -2):
            coefficient = (Fraction((-1)**(degree//2))*moments[degree]
                           /math.factorial(degree-derivative))
            total = total*x2+coefficient
        if derivative == 1:
            total = x_box*total
        power = series_order+1-derivative
        remainder = moments[series_order+1]*abs(x)**power/math.factorial(power)
        values.append(total+Interval(-remainder, remainder, bits))
        remainders.append(remainder)
    proof_identity = dict(exact_profile_delta=str(delta), maximum_absolute_moment_degree=series_order+1,
        absolute_moments=[str(value) for value in moments])
    return dict(intervals=values, derivative_orders=[0, 1, 2],
        exact_profile_delta=str(delta), actual_lambda_binary64_hex=lambda_word,
        even_series_order=series_order, precision_bits=bits,
        exact_absolute_moment_identity_sha256=canonical(proof_identity),
        exact_mass=moments[0], exact_remainder_moment=moments[series_order+1],
        exact_Taylor_remainder_upper=remainders,
        all_twelve_profile_pieces_in_exact_moments=True,
        exact_Fraction_polynomial_integrals=True,
        polynomial_evaluation_outward_dyadic=True,
        working_quadrature_or_trigonometric_accuracy_assumed=False,
        accurate_moment_enclosures_computed_here=True)


def central_profile_enclosures(t, delta, physical_length):
    """Exact-profile h and physical h_s on the supplied accurate t interval.

    The caller still owns the association of that interval to the declared
    actual node address; this function proves the profile evaluation itself.
    """
    require_actions()
    bits = t.bits
    delta = fraction(delta)
    if (not 0 < delta < Fraction(1, 8) or t.lo < 0 or t.hi > 1
            or physical_length.lo <= 0 or physical_length.bits != bits):
        raise ValueError('Use a complete positive R711 profile length and t subset [0,1]')
    a = Fraction(1, 4)
    c = a-delta
    values, derivatives, pieces = [], [], []

    def I5(u):
        return u**4*(Fraction(5, 2)+u*(-3+u))

    def S5(u):
        return u**3*(10+u*(-15+6*u))

    for quarter in range(4):
        left, right = quarter*a, (quarter+1)*a
        sign = 1 if quarter < 2 else -1
        orientation = 1 if quarter % 2 == 0 else -1
        edges = (left, left+delta, right-delta, right)
        for index in range(3):
            lo, hi = max(t.lo, edges[index]), min(t.hi, edges[index+1])
            if lo > hi:
                continue
            local = Interval(lo, hi, bits)
            x = local-left if orientation == 1 else right-local
            # The x-region is determined by the exact piece label, not by a
            # rounded interval comparison at a shared endpoint.
            x_piece = index if orientation == 1 else 2-index
            if x_piece == 0:
                u = (x/delta).intersect(0, 1)
                H, g = delta*I5(u)/c, S5(u)
            elif x_piece == 1:
                H, g = (x-delta/2)/c, Interval(1, 1, bits)
            else:
                u = ((a-x)/delta).intersect(0, 1)
                H, g = 1-delta*I5(u)/c, S5(u)
            H, g = H.intersect(0, 1), g.intersect(0, 1)
            values.append(sign*H)
            derivatives.append(sign*orientation*g/c)
            pieces.append(dict(quarter=quarter, piece=index, normalized_interval=[lo, hi]))
    if not pieces:
        raise ValueError('The full declared central coordinate has no profile piece')
    h = Interval(min(v.lo for v in values), max(v.hi for v in values), bits).intersect(-1, 1)
    ht = Interval(min(v.lo for v in derivatives), max(v.hi for v in derivatives), bits)
    return dict(h=h, normalized_derivative=ht, h_s=ht/physical_length,
        exact_profile_delta=str(delta), complete_intersecting_pieces=pieces,
        accurate_normalized_coordinate=t, accurate_physical_length=physical_length,
        profile_and_derivative_enclosures_computed_here=True,
        external_node_address_to_coordinate_association_verified=False)

'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    parent = args.repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261126/supported_unit_seed_angular_jet_error_bounds.py'
    text = parent.read_text()
    if hashlib.sha256(text.encode()).hexdigest() != PARENT:
        raise ValueError('The complete original R710 fee source changed')
    for old, new in PINS.items():
        text = replace(text, old, new)
    text = text.replace('supported-unit', 'supported-smooth-triangle')
    text = replace(text, 'read_supported_unit_normal_lift_so3_report.py',
                   'read_supported_smooth_triangle_normal_lift_so3_report.py')
    text = replace(text, 'Complete conditional R709 seed angular/node fees, using actual working words.',
                   'Complete R713 exact-profile moment fees and conditional actual-seed angular/node bounds.')
    text = replace(text, 'def exact_relative_lengths(seed, S, bits):',
                   NEW_FUNCTIONS+'\ndef exact_relative_lengths(seed, S, bits):')
    text = replace(text, '    epsilon = Fraction(seed["exact_profile_epsilon"])',
                   '    profile_delta = Fraction(seed["exact_profile_delta"])')
    text = replace(text, '        boundary_upper=(S*beta).hi, epsilon=epsilon,',
                   '        boundary_upper=(S*beta).hi, profile_delta=profile_delta,\n'
                   '        relative_central_intervals=[[left+beta/4, right-beta/4] for left, right in pieces],')
    text = replace(text, 'def mean_jet_bounds(seed, working, fees, *, bits=160, taylor_order=48):',
                   'def mean_jet_bounds(seed, working, fees, *, bits=160, taylor_order=48, profile_series_order=48):')
    text = replace(text,
        '    epsilon = length["epsilon"]\n'
        '    if not 0 < epsilon < min(Fraction(1, 8), rminus/4):\n'
        '        raise ValueError("This conditional central-profile existence bound is not paid")',
        '    profile_delta = length["profile_delta"]\n'
        '    if not 0 < profile_delta < Fraction(1, 8):\n'
        '        raise ValueError("The complete independent R711 profile delta is invalid")')
    text = replace(text, '    if not 0 < lam[0] < pi.lo/2:\n'
                   '        raise ValueError("Actual amplitude candidate is not proved inside (0,pi/2)")',
                   '    if not 0 < lam[0] < pi.lo:\n'
                   '        raise ValueError("Actual R711 amplitude candidate is not proved inside (0,pi)")')
    text = replace(text,
        '    plateau_floor = min(sinhat.lo, sqrt_bounds(1-rplus*rplus, bits)[0])\n'
        '    m = lower_dyadic((1-4*epsilon)*plateau_floor, bits)',
        '    full_branch_floor = min(sinhat.lo, sqrt_bounds(1-rplus*rplus, bits)[0],\n'
        '        2*rminus*sqrt_bounds(1-rminus*rminus, bits)[0])\n'
        '    m = lower_dyadic(full_branch_floor/3, bits)')
    text = replace(text,
        '    moment_fees = [nonnegative(q, "accurate profile-moment fee")\n'
        '        for q in fees["accurate_profile_moment_absolute_errors"]]\n'
        '    if len(moment_fees) != 3:\n'
        '        raise ValueError("Keep all three accurate moment errors at the actual amplitude candidate")\n'
        '    moments = [Interval(word(working[name])-error, word(working[name])+error, bits)\n'
        '        for name, error in zip(moment_names, moment_fees)]',
        '    moment_proof = complete_profile_moment_enclosures(seed, working["lambda"],\n'
        '        bits=bits, series_order=profile_series_order)\n'
        '    moments = moment_proof["intervals"]\n'
        '    moment_fees = [max(abs(v.lo-word(working[name])), abs(v.hi-word(working[name])))\n'
        '        for v, name in zip(moments, moment_names)]\n'
        '    moment_proof["actual_working_moment_binary64_hex"] = [working[name] for name in moment_names]\n'
        '    moment_proof["complete_working_moment_error_upper"] = moment_fees\n'
        '    moment_proof["external_profile_moment_error_inputs_used"] = False')
    text = replace(text, '    lboxes[0] = lboxes[0].intersect(0, pi.hi/2)',
                   '    lboxes[0] = lboxes[0].intersect(0, pi.hi)')
    text = replace(text, '        length_bounds=length, precision_bits=bits, taylor_order=taylor_order,',
                   '        length_bounds=length, accurate_S_interval=S,\n'
                   '        complete_central_profile_moment_proof=moment_proof,\n'
                   '        central_profile_moment_errors_certified_by_this_module=True,\n'
                   '        precision_bits=bits, taylor_order=taylor_order, profile_series_order=profile_series_order,')
    text = replace(text,
        '        h, hs = box(node["accurate_h"], bits), box(node["accurate_h_s"], bits)\n'
        '        if h.lo < -1 or h.hi > 1:\n'
        '            raise ValueError("Use the actual full profile enclosure within [-1,1]")',
        '        index = node["central_interval_index"]\n'
        '        if isinstance(index, bool) or not isinstance(index, int) or index not in (0, 1):\n'
        '            raise ValueError("Bind one actual complete central support interval")\n'
        '        left, right = mean["length_bounds"]["relative_central_intervals"][index]\n'
        '        t = box(node["accurate_normalized_central_coordinate"], bits)\n'
        '        profile = central_profile_enclosures(t, mean["length_bounds"]["profile_delta"],\n'
        '            mean["accurate_S_interval"]*(right-left))\n'
        '        h, hs = profile["h"], profile["h_s"]')
    text = replace(text, '        norm_error_upper=errors,\n        caller_same_field_node_binding=',
                   '        norm_error_upper=errors,\n'
                   '        complete_central_profile_enclosures=profile if region == "central" else None,\n'
                   '        caller_same_field_node_binding=')
    text = replace(text, '    parser.add_argument("--taylor-order", type=int, default=48)',
                   '    parser.add_argument("--taylor-order", type=int, default=48)\n'
                   '    parser.add_argument("--profile-series-order", type=int, default=48)')
    text = replace(text, '        taylor_order=args.taylor_order, results=[])',
                   '        taylor_order=args.taylor_order, profile_series_order=args.profile_series_order,\n'
                   '        exact_profile_moment_fees_computed_from_all_pieces=True,\n'
                   '        external_profile_moment_errors_used=False, results=[])')
    text = replace(text, '                bits=args.precision_bits, taylor_order=args.taylor_order)',
                   '                bits=args.precision_bits, taylor_order=args.taylor_order,\n'
                   '                profile_series_order=args.profile_series_order)')
    parsed = ast.parse(text)
    compile(parsed, str(args.output), 'exec')
    if any(line.rstrip() != line for line in text.splitlines()):
        raise ValueError('Trailing whitespace in complete output')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text)
    print(len(text.encode()), hashlib.sha256(text.encode()).hexdigest())


if __name__ == '__main__':
    main()
