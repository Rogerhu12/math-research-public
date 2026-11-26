"""Complete finite-trial residuals and signed physical-column certificates.

Pure definitions: no IO, numerical imports, old computation, or execution.
The trial is finite Fourier.  The actual solution controlled by the complete
positive inverse and negative two-source theorem has no Fourier cutoff.

Use NumericalAPI from the admitted public owner.  A complex coefficient is
a pair (real Arb, imaginary Arb); dictionaries contain ALL finite Fourier
coefficients with physical frequencies 4*j.  Absent keys mean exact zero.
The owner must prove that its true background is the complete degree96
Q_delta and bind all original source, interval, physical, and receiver data.
"""

BACKGROUND_DEGREE = 96
HIGH_START = 97
ROOT_SECOND_FULL_SOURCE_DOMAIN = 'L2_dr_Hminus2over3_first_Hminus1_second'
RAW_PAIR_SOURCE_DOMAIN = 'ordinary_L2_dr_normalized_L2_phi_full_moving_pair'


def require(ok, message):
    if not ok:
        raise ValueError(message)


def upper(api, value):
    require(value.is_finite() and api.lower(value) >= 0,
            'finite nonnegative directed quantity')
    return value.upper()


def maximum(api, values):
    values = list(values)
    require(values, 'nonempty complete maximum')
    result = api.zero
    for value in values:
        value = upper(api, value)
        if bool(value > result):
            result = value
    return result


def _zero(api):
    return (api.zero, api.zero)


def _cadd(a, b):
    return (a[0]+b[0], a[1]+b[1])


def _cmul(a, b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def _cscale(scalar, value):
    return (scalar*value[0], scalar*value[1])


def validate_polynomial(poly):
    require(isinstance(poly, dict), 'whole finite Fourier dictionary')
    for j, value in poly.items():
        require(type(j) is int and isinstance(value, (tuple, list))
                and len(value) == 2
                and all(x.is_finite() for x in value),
                'complete finite signed complex coefficient')


def add(api, *polynomials):
    result = {}
    for poly in polynomials:
        validate_polynomial(poly)
        for j, value in poly.items():
            result[j] = _cadd(result.get(j, _zero(api)), value)
    return result


def scale(api, scalar, poly):
    require(scalar.is_finite(), 'finite signed scalar multiplier')
    validate_polynomial(poly)
    return {j: _cscale(scalar, value) for j, value in poly.items()}


def multiply(api, left, right):
    """Full convolution: no truncation, projection, aliasing, or abs first."""
    validate_polynomial(left)
    validate_polynomial(right)
    result = {}
    for j, a in left.items():
        for k, b in right.items():
            result[j+k] = _cadd(result.get(j+k, _zero(api)), _cmul(a, b))
    return result


def derivative(api, poly):
    validate_polynomial(poly)
    return {j: (-4*j*value[1], 4*j*value[0])
            for j, value in poly.items()}


def primitive(api, poly):
    """The exact I=d_phi^-1 (1-Pi), including its exact zero constant."""
    validate_polynomial(poly)
    return {j: (value[1]/(4*j), -value[0]/(4*j))
            for j, value in poly.items() if j != 0}


def constant(api, value):
    require(value.is_finite(), 'finite real constant')
    return {0: (value, api.zero)}


def validate_pair(pair):
    require(isinstance(pair, (tuple, list)) and len(pair) == 2,
            'complete two-component moving pair')
    for poly in pair:
        validate_polynomial(poly)


def pair_add(api, *pairs):
    for pair in pairs:
        validate_pair(pair)
    return tuple(add(api, *(pair[k] for pair in pairs)) for k in range(2))


def pair_scale(api, scalar, pair):
    validate_pair(pair)
    return tuple(scale(api, scalar, poly) for poly in pair)


def reflection_pair(api, odd_normalized, even_normalized, moving_mean):
    """sqrt(2) sin/cos coefficients -> both complex signs, mean weight one.

    The radial polynomial coefficients can be exact dyadics in this real
    normalized basis.  sqrt(1/2) is kept as a ball, NOT its upper endpoint.
    """
    require(len(odd_normalized) == len(even_normalized),
            'both complete nonmean reflection lists have the same cutoff')
    half_root = api.sqrt(api.rational(1, 2))
    odd, even = {}, constant(api, moving_mean)
    for j, (a, b) in enumerate(zip(odd_normalized, even_normalized), 1):
        require(a.is_finite() and b.is_finite(), 'complete signed real mode')
        odd[j] = (api.zero, -half_root*a)
        odd[-j] = (api.zero, half_root*a)
        even[j] = (half_root*b, api.zero)
        even[-j] = (half_root*b, api.zero)
    return odd, even


def moving_rhs(api, background, trial, beta, K, gamma):
    """Exact SC.9, at the UNSOLVED background; all means/nonlocal terms.

    background and trial are finite Fourier pairs, not projected solutions.
    K, beta and gamma are complete radial/parameter coefficient balls.
    """
    validate_pair(background)
    validate_pair(trial)
    require(all(abs(j) <= BACKGROUND_DEGREE
                for poly in background for j in poly),
            'the same complete degree96 background')
    require(all(value.is_finite() for value in (beta, K, gamma)),
            'whole true intrinsic coefficient balls')
    u, v = background
    a, b = trial
    mean_v = v.get(0, _zero(api))
    mean_b = b.get(0, _zero(api))
    require(bool(mean_v[1] == api.zero) and bool(mean_b[1] == api.zero),
            'the real independent moving means are retained')
    u2 = multiply(api, u, u)
    v2 = multiply(api, v, v)
    uv = multiply(api, u, v)
    S = add(api, u2, scale(api, K, v2))
    d = scale(api, -beta, primitive(api, S))
    up, vp = derivative(api, u), derivative(api, v)
    ap, bp = derivative(api, a), derivative(api, b)
    inner = add(api, multiply(api, u, a),
                scale(api, K, multiply(api, v, b)))
    inner_I = primitive(api, inner)
    one = constant(api, api.one)
    l11 = scale(api, -beta, add(api, one, scale(api, 3*api.one, u2),
                               scale(api, K, v2)))
    l12 = scale(api, -2*beta*K, uv)
    l21 = scale(api, -2*beta, uv)
    l22 = scale(api, beta, add(api, one, scale(api, -api.one, u2),
                               scale(api, -3*K, v2)))
    speed = gamma*mean_v[0]
    rhs1 = add(api, multiply(api, d, ap), scale(api, speed*K, bp),
               multiply(api, l11, a), multiply(api, l12, b),
               scale(api, -2*beta, multiply(api, up, inner_I)),
               scale(api, gamma*mean_b[0]*K, vp))
    rhs2 = add(api, multiply(api, d, bp), scale(api, -speed, ap),
               multiply(api, l21, a), multiply(api, l22, b),
               scale(api, -2*beta, multiply(api, vp, inner_I)),
               scale(api, -gamma*mean_b[0], up))
    degree = max([abs(j) for poly in trial for j in poly] + [0])
    require(all(abs(j) <= degree+2*BACKGROUND_DEGREE
                for poly in (rhs1, rhs2) for j in poly),
            'the complete M+192 output, including both signs and every mean')
    return rhs1, rhs2


def complete_residual(api, background, trial, radial_derivative,
                      ordinary_source, beta, K, gamma):
    """h_app,r - A_Q h_app - f; missing nonfinite-source tails are NOT zero."""
    validate_pair(radial_derivative)
    validate_pair(ordinary_source)
    rhs = moving_rhs(api, background, trial, beta, K, gamma)
    return pair_add(api, radial_derivative,
                    pair_scale(api, -api.one, rhs),
                    pair_scale(api, -api.one, ordinary_source))


def polynomial_value_derivative(api, coefficients, x):
    """One common radial scalar, exact derivative before interval evaluation.

    coefficients[k] is the COMPLETE finite Fourier pair multiplying x**k.
    """
    require(coefficients and x.is_finite(), 'whole declared radial polynomial')
    for coefficient in coefficients:
        validate_pair(coefficient)
    value = coefficients[-1]
    deriv = ({}, {})
    for coefficient in reversed(coefficients[:-1]):
        deriv = pair_add(api, pair_scale(api, x, deriv), value)
        value = pair_add(api, pair_scale(api, x, value), coefficient)
    return value, deriv


def endpoint_conforming_trial(api, coefficients, x, true_length,
                              endpoint_value=None):
    """p*(1-x), or endpoint_value+p*(1-x), and its TRUE radial derivative.

    x=(r-r_left)/true_length is the same physical affine coordinate in all
    terms.  At x=1 this trial equals endpoint_value EXACTLY.  With no value
    supplied it is zero at the true outer endpoint; for negative continuation
    use the positive trial's exact root value as endpoint_value and x=r/r*.
    """
    require(true_length.is_finite() and api.lower(true_length) > 0,
            'positive whole true affine length, never a displayed midpoint')
    value, deriv = polynomial_value_derivative(api, coefficients, x)
    state = pair_scale(api, api.one-x, value)
    if endpoint_value is not None:
        state = pair_add(api, endpoint_value, state)
    radial = pair_scale(api, api.one/true_length, pair_add(
        api, pair_scale(api, -api.one, value),
        pair_scale(api, api.one-x, deriv)))
    return state, radial


def _weight_squared(api, j, window):
    """Lambda_j^(2s), with exact named s and directed Arb arithmetic."""
    base = api.rational(1+16*j*j)
    if window == 'L2':
        return api.one
    if window == 'Hminus1':
        return api.one/base
    require(window == 'Hminus2over3', 'explicit proved source Sobolev window')
    return api.exp(api.rational(-2, 3)*base.log())


def angular_squared_upper(api, polynomial, window='L2', modes=None):
    """Full Parseval upper after signed residual formation.

    modes optionally selects an actual Fourier projection, e.g. abs(j)<97.
    It never truncates the underlying residual or silently deletes a tail.
    """
    validate_polynomial(polynomial)
    total = api.zero
    for j, value in polynomial.items():
        if modes is not None and not modes(j):
            continue
        ar, ai = (api.magnitude(x) for x in value)
        total += _weight_squared(api, j, window)*(ar*ar+ai*ai)
    return upper(api, total)


def pair_squared_upper(api, pair, windows=('L2', 'L2'), modes=None):
    validate_pair(pair)
    require(len(windows) == 2, 'both source windows, including the second row')
    return upper(api, sum((angular_squared_upper(api, pair[k], windows[k], modes)
                           for k in range(2)), api.zero))


def whole_radial_norm_upper(api, boxes, windows=('L2', 'L2'), modes=None):
    """SC.12 on the COMPLETE cover; no midpoint, sampling, or omitted box.

    Each box contains length_upper and complete_residual.  The public owner
    verifies its true closed cover and coefficient identities before calling.
    A conservative overlap is allowed; a gap is not.
    """
    require(boxes, 'complete nonempty true radial cover')
    total = api.zero
    for box in boxes:
        mass = upper(api, box['length_upper'])
        total += mass*pair_squared_upper(
            api, box['complete_residual'], windows, modes)
    return upper(api, api.sqrt(upper(api, total)))


def root_mixed_upper(api, pair, modes=None):
    return upper(api, api.sqrt(pair_squared_upper(
        api, pair, ('Hminus2over3', 'Hminus1'), modes)))


def low_even96_root_error(api, trial_root, prescribed_even_normalized):
    """The actual prescribed c* error; no trace of an arbitrary L2 function."""
    validate_pair(trial_root)
    require(len(prescribed_even_normalized) == 96,
            'all96 actual independent physical root coordinates')
    zeros = [api.zero]*96
    target = reflection_pair(api, zeros, prescribed_even_normalized, api.zero)
    difference = add(api, trial_root[1], scale(api, -api.one, target[1]))
    return upper(api, api.sqrt(angular_squared_upper(
        api, difference, 'L2', lambda j: 1 <= abs(j) <= 96)))


def conservative_zero_stable_residual(api, positive_trial_root):
    """SC.15: only when the true independent high-stable datum is zero."""
    z = root_mixed_upper(api, positive_trial_root,
                         lambda j: abs(j) >= HIGH_START)
    return upper(api, api.rational(153, 16)*z)


def continuous_zero_outer_root96_ports(
        api, stable_residual_Y, high_collar_source, high_body_source,
        raw_low_source, physical_root_even96_error):
    """SC.16 for the exact SC.13 homogeneous-column/continuity construction.

    All five values have their original source units.  The proof of zero
    outer/height/mean/jump residuals belongs to this explicit construction,
    not to a norm observation or an arbitrary supplied source packet.
    """
    values = [api.zero]*14
    for index, value in zip((0, 1, 2, 7, 9),
                           (stable_residual_Y, high_collar_source,
                            high_body_source, raw_low_source,
                            physical_root_even96_error)):
        values[index] = upper(api, value)
    return values


def complete_positive_root_error(api, ports, read_saved_224_upper):
    """Same complete14 source vector -> actual physical root-error bound.

    The owner must have admitted the true completed original224 table.
    Stored high_root_mixed ALREADY contains the output factor9 and both
    stable/unstable high components.  All97 low-root coordinates are read.
    """
    require(len(ports) == 14, 'all14 actual positive input slots')
    inputs = [upper(api, x) for x in ports]
    d = sum((upper(api, read_saved_224_upper(k, 'low_root97'))*inputs[k]
             for k in range(14)), api.zero)
    z = sum((upper(api, read_saved_224_upper(k, 'high_root_mixed'))*inputs[k]
             for k in range(14)), api.zero)
    d, z = upper(api, d), upper(api, z)
    c = inputs[9]
    return {
        'physical_root_even96_error_upper': c,
        'physical_root_odd96_mean_error_upper': d,
        'high_root_mixed_error_upper': z,
        'complete_physical_root_error_upper': upper(
            api, api.sqrt(upper(api, c*c+d*d+z*z))),
    }


def complete_negative_trial_error(api, root_error, root_source,
                                  strict_source, CR, CO, C2,
                                  root_impulse_sum, strict_impulse_sum, C1):
    """SC.5/19. Full root source H^-2/3 x H^-1; full strict source H^-1 pair.

    Every impulse is separate.  For the continuous homogeneous-column
    construction the two impulse arguments are exact proved zeros.
    """
    vals = [upper(api, x) for x in (
        root_error, root_source, strict_source, CR, CO, C2,
        root_impulse_sum, strict_impulse_sum, C1)]
    er, fr, fs, cr, co, c2, jr, js, c1 = vals
    return upper(api, cr*(er+jr)+co*fr+c2*fs+c1*js)


def complete_waist_density(api, raw_trial, q, ng):
    """Exact finite SC.20 at the true waist, keeping BOTH physical means."""
    validate_pair(raw_trial)
    require(q.is_finite() and ng.is_finite()
            and api.lower(q) > 0 and api.lower(ng) > 0,
            'actual positive waist q and density scale, not a root value')
    a, b = raw_trial
    scalar = ng/api.sqrt(2*q)
    waves = (
        scale(api, scalar, add(api, a, scale(api, q, b))),
        scale(api, scalar, add(api, a, scale(api, -q, b))),
    )
    means = [poly.get(0, _zero(api)) for poly in waves]
    require(all(bool(value[1] == api.zero) for value in means),
            'real physical density means')
    return {
        'primitive_pair': tuple(primitive(api, poly) for poly in waves),
        'both_physical_means': tuple(value[0] for value in means),
    }


def density_squared_upper(api, density):
    pair = density['primitive_pair']
    means = density['both_physical_means']
    require(len(means) == 2, 'both physical density means')
    return upper(api, pair_squared_upper(api, pair)
                 +sum((api.magnitude(z)**2 for z in means), api.zero))


def complete_real_density_pairing(api, row_trial, column_trial):
    """Signed real Hilbert pairing of COMPLETE finite primitive+two-mean data."""
    x = row_trial['primitive_pair']
    y = column_trial['primitive_pair']
    validate_pair(x)
    validate_pair(y)
    result = api.zero
    for a, b in zip(x, y):
        require(0 not in a and 0 not in b,
                'primitive has exact zero constant, means are separate')
        for j, left in a.items():
            right = b.get(j, _zero(api))
            # Re(conj(left)*right); no absolute values before summation.
            result += left[0]*right[0]+left[1]*right[1]
    zx = row_trial['both_physical_means']
    zy = column_trial['both_physical_means']
    require(len(zx) == len(zy) == 2, 'the complete physical mean pairing')
    return result+sum((a*b for a, b in zip(zx, zy)), api.zero)


def signed_entry_enclosure(api, row_trial, column_trial,
                           true_row_norm_upper, column_error_upper,
                           inverse_normalizer_upper,
                           complete_adjoint_row_residual_upper,
                           extra_evaluation_error_upper):
    """SC.24: actual signed centre + COMPLETE column/row/evaluation errors."""
    centre = complete_real_density_pairing(api, row_trial, column_trial)
    l, d, kw, er, ev = (upper(api, x) for x in (
        true_row_norm_upper, column_error_upper, inverse_normalizer_upper,
        complete_adjoint_row_residual_upper, extra_evaluation_error_upper))
    ynorm = upper(api, api.sqrt(density_squared_upper(api, column_trial)))
    radius = upper(api, l*d+kw*er*ynorm+ev)
    return {
        'signed_trial_pairing': centre,
        'complete_entry_error_upper': radius,
        'actual_signed_entry_ball': centre+api.interval(-radius, radius),
    }


def _validate_square(matrix):
    require(isinstance(matrix, (tuple, list)) and len(matrix) > 0
            and all(isinstance(row, (tuple, list)) and len(row) == len(matrix)
                    for row in matrix)
            and all(x.is_finite() for row in matrix for x in row),
            'entire finite signed square matrix, all rows and columns')


def _matrix_norm_bounds(api, matrix):
    _validate_square(matrix)
    n = len(matrix)
    row = maximum(api, [
        upper(api, sum((api.magnitude(x) for x in values), api.zero))
        for values in matrix])
    column = maximum(api, [
        upper(api, sum((api.magnitude(matrix[i][j]) for i in range(n)), api.zero))
        for j in range(n)])
    two = upper(api, api.sqrt(upper(api, row*column)))
    return row, column, two


def complete_weighted_signed_inverse_gate(
        api, entry_balls, exact_dyadic_trial_inverse,
        source_weights, target_weights):
    """SC.25--27, all entries formed SIGNED before complete row/column sums.

    Return values are unpersisted arithmetic, not a public success record.
    The owner saves/reads the whole scalar bounds and applies the strict gate
    again.  A physical96 subblock is not automatically the full bordered Schur.
    """
    _validate_square(entry_balls)
    _validate_square(exact_dyadic_trial_inverse)
    n = len(entry_balls)
    require(len(exact_dyadic_trial_inverse) == n
            and len(source_weights) == len(target_weights) == n,
            'complete compatible source and target finite coordinates')
    require(all(x.is_finite() and api.lower(x) > 0
                for x in list(source_weights)+list(target_weights)),
            'separate positive source and target normalization weights')
    require(all(x.lower() == x.upper()
                for row in exact_dyadic_trial_inverse for x in row),
            'one actual exact dyadic trial inverse, not a floating SVD bound')
    normalized = [
        [target_weights[i]*entry_balls[i][j]/source_weights[j]
         for j in range(n)] for i in range(n)]
    residual = []
    for i in range(n):
        row = []
        for j in range(n):
            signed_product = sum((
                exact_dyadic_trial_inverse[i][k]*normalized[k][j]
                for k in range(n)), api.zero)
            row.append((api.one if i == j else api.zero)-signed_product)
        residual.append(row)
    ri, r1, rho = _matrix_norm_bounds(api, residual)
    bi, b1, bn = _matrix_norm_bounds(api, exact_dyadic_trial_inverse)
    passed = bool(rho < api.one)
    result = {
        'complete_dimension': n,
        'complete_signed_residual_matrix': residual,
        'weighted_residual_infinity_upper': ri,
        'weighted_residual_one_upper': r1,
        'weighted_residual_two_upper': rho,
        'trial_inverse_infinity_upper': bi,
        'trial_inverse_one_upper': b1,
        'trial_inverse_two_upper': bn,
        'strict_unpersisted_finite_inverse_gate_passed': passed,
        'all_full_incoming_Schur_rows_present': False,
    }
    if passed:
        gap = (api.one-rho).lower()
        require(api.lower(gap) > 0, 'strict directed finite inverse gap')
        result['inverse_gap_lower'] = gap
        result['weighted_actual_inverse_two_upper'] = upper(api, bn/gap)
    return result
