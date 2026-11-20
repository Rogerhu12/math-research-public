#!/usr/bin/env python3
"""Complete signed true-root 96/97 form; new public Actions target only.

The accepted axis, mean denominator and X geometry defects are read whole.
No completed target is called. Original candidate materialization is only a
definition helper. One new full-circle coefficient enclosure and two new
response primitives are private intermediates of the three signed entries.
Only scalar balls, counts, hashes and the checked conclusion are published.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import time

KIND = 'R138_same_Qrepair_true_root_complete_signed_96_97_form_v1'
CELLS = 32768
BITS = 320
MODES = (96, 97)
DEFINITION_SHA = 'd152f31cef53c1d58099cf3d1f994d2dad9d31d6a75cb42a7d9e54a35c17ae79'
AXIS_SHA = 'b300ea209acb2239a93a87aa3f14d6d9c5f0ed3b5b88ea44b415e5078ea0cd92'
AXIS_EXECUTION_SHA = 'a8979dff609fd41e88be754e09e8fbb2a56528f101c729208e5e54a9ef1de73f'
MEAN_SHA = 'de3a14606aa432fbd1f7707c277a33110f81ce6ca23fdfc6bfdf7e9d497623b4'
MEAN_EXECUTION_SHA = '25d6e66fade5f838a33e62da0f502152115a34c5c572c662471b6c9acad38cb5'
X_SHA = '1259c3687cea0af523dd52055e88d5ee9a7b77094c218101835b6c38dfbbc7ec'
X_EXECUTION_SHA = '999555eafb3c443266f1a8fed98056c9d4f448c0131ef5ffff93941b35040c92'
FRAME_FEE = Fraction(11, 10**7)
POSITION_FEE = Fraction(1, 25000)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read(path, expected):
    require(sha(path) == expected, 'whole saved input hash differs: '+Path(path).name)
    return json.loads(Path(path).read_text())


def save(path, document):
    raw = (json.dumps(document, ensure_ascii=False, indent=2, allow_nan=False)+'\n').encode()
    temporary = Path(str(path)+'.partial')
    temporary.write_bytes(raw)
    temporary.replace(path)
    require(path.read_bytes() == raw, 'complete scalar output byte readback')


def execution_admission(document, run_id, scientific_sha):
    require(document.get('complete') is True and document.get('run_id') == run_id
        and str(document.get('run_attempt')) == '1'
        and document.get('actual_child_returncode') == 0
        and document.get('original_scientific_complete') is True
        and document.get('original_scientific_failure') is None
        and document.get('old_completed_targets_recomputed') == 0
        and document.get('old_numerical_producers_called') == 0
        and document.get('scientific_children') == 1,
        'complete successful original execution scope')
    require(any(row.get('sha256') == scientific_sha
                for row in document.get('scientific_files', [])),
            'original execution identifies the whole accepted science file')


def run(args):
    require(os.environ.get('GITHUB_ACTIONS') == 'true'
        and os.environ.get('GITHUB_REPOSITORY') == 'Rogerhu12/math-research-public',
        'new scientific execution requires the repository public Actions')
    require(not args.output.exists(), 'preserve the existing completed or failed new target')
    require(sha(args.definition_source) == DEFINITION_SHA, 'pure definition helper identity')
    spec = importlib.util.spec_from_file_location('root_definition_only', args.definition_source)
    definition = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(definition)
    from flint import arb, ctx
    import numpy as np
    ctx.prec = BITS
    started = time.monotonic()
    args.output.parent.mkdir(parents=True, exist_ok=True)

    def rat(value):
        value = Fraction(value)
        return arb(value.numerator)/value.denominator

    def mag(value):
        return abs(value).upper()

    def norm(values):
        return sum((mag(x)**2 for x in values), arb(0)).sqrt().upper()

    def unpack(record):
        if 'ball' in record:
            return arb(record['ball'])
        require(record.get('kind') == 'complete_decimal_ball_v1', 'complete saved scalar kind')
        exponent = int(record['decimal_exponent'])
        scale = rat(10**exponent) if exponent >= 0 else rat(Fraction(1, 10**(-exponent)))
        mid = rat(int(record['midpoint_integer']))*scale
        rad = rat(int(record['radius_integer']))*scale
        require(rad >= 0, 'nonnegative complete scalar radius')
        return (mid-rad).lower().union((mid+rad).upper())

    def recorded(value):
        require(value.is_finite(), 'finite whole signed scalar')
        m, r, e = value.mid_rad_10exp(75)
        record = dict(kind='complete_decimal_ball_v1', midpoint_integer=str(int(m)),
                      radius_integer=str(int(r)), decimal_exponent=str(int(e)))
        require(int(r) >= 0 and unpack(record).contains(value),
                'complete saved signed scalar contains the entire original ball')
        return record

    def add(a, b):
        return [x+y for x, y in zip(a, b)]

    def scale(a, scalar):
        return [scalar*x for x in a]

    def dot(a, b):
        return sum((x*y for x, y in zip(a, b)), arb(0))

    def cross(a, b):
        return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]

    def triple(a, b, c):
        return dot(a, cross(b, c))

    def mm(a, b):
        return [[sum((a[i][k]*b[k][j] for k in range(3)), arb(0))
                 for j in range(3)] for i in range(3)]

    def mv(a, b):
        return [dot(row, b) for row in a]

    def skew(w):
        w1, w2, w3 = w
        return [[arb(0), -w1, -w2], [w1, arb(0), -w3], [w2, w3, arb(0)]]

    def rotation_and_integral(w, elapsed):
        matrix = skew(w)
        squared = mm(matrix, matrix)
        speed = dot(w, w).sqrt()
        require(speed > 0, 'the nonzero original a/m skew speed remains separated')
        angle = elapsed*speed
        sine, cosine = angle.sin(), angle.cos()
        aa, bb = sine/speed, (1-cosine)/(speed*speed)
        cc = (angle-sine)/(speed**3)
        rotation = [[arb(int(i == j))+aa*matrix[i][j]+bb*squared[i][j]
                     for j in range(3)] for i in range(3)]
        integral = [[elapsed*arb(int(i == j))+bb*matrix[i][j]+cc*squared[i][j]
                     for j in range(3)] for i in range(3)]
        return rotation, integral

    # Every private float pair is validated against its entire Arb source.
    # This is an internal cache representation, never a published array.
    def pack(value):
        midpoint = float(value.mid())
        require(math.isfinite(midpoint), 'finite private midpoint')
        radius = math.nextafter(float(mag(value-arb(midpoint))), math.inf)
        require(math.isfinite(radius) and radius >= 0, 'finite private radius')
        enclosing = arb(midpoint, radius)
        require(enclosing.contains(value), 'private mid64/rad64 contains original whole ball')
        return midpoint, radius

    def packed(values):
        return np.array([pack(x) for x in values], dtype=np.float64)

    def unpacked(values):
        return [arb(float(m), float(r)) for m, r in values]

    axis = read(args.axis, AXIS_SHA)
    mean_result = read(args.mean, MEAN_SHA)
    old_x = read(args.physical_budget, X_SHA)
    receipts = [read(args.axis_execution, AXIS_EXECUTION_SHA),
                read(args.mean_execution, MEAN_EXECUTION_SHA),
                read(args.physical_execution, X_EXECUTION_SHA)]
    for receipt, run_id, science_sha in zip(receipts,
            ('44730968113', '44733403315', '44737045152'),
            (AXIS_SHA, MEAN_SHA, X_SHA)):
        execution_admission(receipt, run_id, science_sha)
    require(all(d.get('complete') is True and d.get('proved') is True
                and d.get('failure') is None for d in (axis, mean_result, old_x)),
            'all three original whole conclusions are complete and proved')
    require(axis['completed_original_rows'] == 4650
        and axis['old_target_or_primitive_calls'] == 0 and axis['old_geometry_ODE_calls'] == 0
        and mean_result['completed_cells'] == 8192
        and mean_result['original_scientific_calls'] == 0
        and mean_result['old_axis_target_calls'] == 0
        and mean_result['old_geometry_target_calls'] == 0
        and old_x['completed_closed_cells'] == 4651
        and old_x['old_scientific_target_calls'] == 0
        and old_x['old_primitive_calls'] == 0 and old_x['old_geometry_ODE_calls'] == 0,
        'complete original covers and zero old target scopes')
    require(axis['identity']['source_sha256'] == DEFINITION_SHA
        and axis['identity']['candidate'] == definition.CANDIDATE_SHA
        and axis['identity']['germ'] == definition.GERM_SHA
        and axis['identity']['fixed_point'] == '(0,0,1/2)'
        and mean_result['identity']['candidate_sha256'] == definition.CANDIDATE_SHA
        and mean_result['identity']['germ_sha256'] == definition.GERM_SHA
        and old_x['identity']['original_candidate_sha256'] == definition.CANDIDATE_SHA
        and old_x['identity']['original_germ_sha256'] == definition.GERM_SHA
        and old_x['identity']['fixed_point'] == '(0,0,1/2)',
        'same repaired candidate, same physical anchor and same fixed point')
    root_interval = [str(definition.ROOT_LO), str(definition.ROOT_HI)]
    require(axis['identity']['exact_root_interval'] == root_interval
        and mean_result['identity']['exact_root_interval'] == root_interval
        and old_x['identity']['exact_true_root_interval'] == root_interval,
        'the entire same true root interval')

    axis_error = unpack(axis['complete_axis_error']).upper()
    axis_q = unpack(axis['nominal_q'])+arb(0, axis_error)
    axis_s = unpack(axis['nominal_s'])+arb(0, axis_error)
    denominator = unpack(mean_result['actual_mean_denominator'])
    require(denominator > rat(Fraction(17, 20)), 'whole saved actual mean denominator >17/20')
    inverse_denominator = 1/denominator
    root_defect = old_x['actual_root_physical_defect']
    z0, z1, p0, p1 = [unpack(root_defect[k]).upper()
                       for k in ('Z', 'Z_theta', 'P', 'P_theta')]

    germ = definition.read(args.germ, definition.GERM_SHA)
    candidate, nodes, cc = definition.load_candidate(args.candidate)
    alpha = Fraction(candidate['metadata']['exact_float_amplitude'])
    require(germ['complete'] and germ['proved'] and germ['failure'] is None
        and germ['candidate_sha256'] == definition.CANDIDATE_SHA
        and germ['object_sha256'] == definition.OBJECT_SHA
        and Fraction(germ['exact_amplitude']) == alpha
        and Fraction(germ['actual_fixed_nu']) == definition.NU
        and Fraction(germ['exact_center_parameter']) == definition.ETA
        and germ['whole_affine_parameter_interval']
        and tuple(map(Fraction, germ['root_interval'])) ==
            (definition.ROOT_LO, definition.ROOT_HI)
        and germ['actual_candidate_piece'] == 2549
        and germ['compact_bump_identically_zero_on_entire_actual_germ'],
        'same-object original root germ')
    radial = tuple(map(Fraction, germ['complex_radial_rectangle']['real_interval']))
    scalar = tuple(map(Fraction, germ['original_scalar_germ']))
    require(nodes[2549] <= definition.ROOT_LO < definition.ROOT_HI <= nodes[2550]
        and radial[0] <= definition.ROOT_LO < definition.ROOT_HI <= radial[1]
        and scalar[0] <= definition.ROOT_LO < definition.ROOT_HI <= scalar[1],
        'whole true root remains in its original candidate and scalar germs')
    background = definition.private_root_angular_definition(germ, candidate, nodes, cc, arb)
    del cc, nodes
    a, bzero, m = background['a'], background['b0'], background['mean_v']
    us, vc = background['u_sine'], background['v_cosine']
    require(a > 0 and m < 0 and len(us) == 32 and len(vc) == 33,
            'entire repaired root degree32 definition with signed mean')
    rho = a/m
    two_pi, sqrt2 = 2*arb.pi(), arb(2).sqrt()
    width = two_pi/CELLS
    local_time = arb(0).union(width.upper())
    frequencies = (384, 388)
    high_third = arb(388)**rat(Fraction(1, 3))
    fs = (arb(384), high_third)
    qs = (arb(0), 1/high_third)
    rs = (arb(1), 1/(high_third*high_third))
    ts = (arb(0), 1/(388*high_third))
    pairs = ((0, 0), (0, 1), (1, 1))
    zero = [arb(0), arb(0), arb(0)]
    ez, ex = [arb(0), arb(0), arb(1)], [arb(1), arb(0), arb(0)]

    identity = dict(kind=KIND, source_sha256=sha(__file__),
        definition_source_sha256=DEFINITION_SHA,
        prior_axis_sha256=AXIS_SHA, prior_axis_execution_sha256=AXIS_EXECUTION_SHA,
        prior_mean_sha256=MEAN_SHA, prior_mean_execution_sha256=MEAN_EXECUTION_SHA,
        prior_physical_budget_sha256=X_SHA, prior_physical_execution_sha256=X_EXECUTION_SHA,
        candidate_sha256=definition.CANDIDATE_SHA, germ_sha256=definition.GERM_SHA,
        object_sha256=definition.OBJECT_SHA,
        repair_definition_sha256=definition.REPAIR_DEFINITION_SHA,
        eta=str(definition.ETA), actual_nu=str(definition.NU), exact_alpha=str(alpha),
        exact_root_interval=root_interval, complete_angular_interval='[0,2*pi]',
        cells=CELLS, arithmetic_bits=BITS, physical_modes=list(MODES),
        physical_frequencies=list(frequencies), scalar_normalization='sqrt(2)*sin(4j*phi)',
        congruence='S=P_low*N+P_high*N^(1/3); original low1..96/high97..infinity',
        actual_periodic_frame_C0_fee=str(FRAME_FEE), actual_position_C0_fee=str(POSITION_FEE),
        fixed_point='(0,0,1/2)', frame_at_zero='X=e_z,Y=e_y,n=e_x',
        projection_vector='ell=X(root,0)=local e_z')
    document = dict(identity=identity, complete=False, proved=False, failure=None,
        stage='complete-new-root-two-mode-coefficient-enclosure', completed_cells=0,
        old_axis_targets_called=0, old_mean_targets_called=0, old_X_targets_called=0,
        old_geometry_targets_called=0, published_arrays=False,
        private_cache_representation='mid64/rad64 with complete Arb containment checked at every write',
        whole_original_references=dict(axis=axis, mean=mean_result, physical_budget=old_x),
        scope=dict(same_Qrepair_true_root=True, original_root_low96_and_all_high_rows_preserved=True,
            independent_mean_eliminated_with_actual_saved_denominator=True,
            signed_two_mode_form_complete=False, negative_two_mode_direction_proved=False,
            all_root_data_nonnegative_form_excluded=False,
            actual_positive_boundary_problem_singular=False,
            positive_inverse_proved=False, final_topic_complete=False))
    save(args.output, document)

    # 27 vector entries + 6 source integrals + 6 source moments + 3 gm
    # integrals + 3 gm moments =45 complete private scalar balls per cell.
    cache = np.empty((CELLS, 45, 2), dtype=np.float64)
    prefix_cache = np.empty((CELLS, 6, 2), dtype=np.float64)
    local_grams = [[arb(0) for _ in pairs] for _ in range(3)]
    mean_functionals = [[arb(0), arb(0)] for _ in range(3)]
    e_integral = [[arb(0) for _ in range(3)] for _ in range(2)]
    frame = [[arb(0), arb(0), arb(1)],
             [arb(0), arb(1), arb(0)],
             [arb(1), arb(0), arb(0)]]
    position = [arb(0), arb(0), arb(0)]
    frame_error, position_error = arb(0), arb(0)
    maximum_frame_error, maximum_position_error = arb(0), arb(0)

    def wave_integral(kind, frequency, left, right):
        if frequency == 0:
            return right-left if kind == 'cos' else arb(0)
        if kind == 'cos':
            return ((frequency*right).sin()-(frequency*left).sin())/frequency
        return ((frequency*left).cos()-(frequency*right).cos())/frequency

    def integrate_coefficient(coefficient, exact_integral, supremum, elapsed):
        return coefficient.mid()*exact_integral+arb(0, coefficient.rad()*mag(elapsed)*supremum)

    def wave(coefficient, kind, mode, weight, left, right):
        if not weight:
            return arb(0)
        return integrate_coefficient(coefficient,
            sqrt2*weight*wave_integral(kind, frequencies[mode], left, right),
            sqrt2*mag(weight), right-left)

    def product(coefficient, kind_i, kind_j, i, j, weight, left, right):
        if not weight:
            return arb(0)
        ni, nj = frequencies[i], frequencies[j]
        if kind_i == 'sin' and kind_j == 'sin':
            exact = wave_integral('cos', ni-nj, left, right)-wave_integral('cos', ni+nj, left, right)
        elif kind_i == 'cos' and kind_j == 'cos':
            exact = wave_integral('cos', ni-nj, left, right)+wave_integral('cos', ni+nj, left, right)
        elif kind_i == 'cos':
            exact = wave_integral('sin', ni+nj, left, right)+wave_integral('sin', nj-ni, left, right)
        else:
            exact = wave_integral('sin', ni+nj, left, right)+wave_integral('sin', ni-nj, left, right)
        return integrate_coefficient(coefficient, weight*exact, 2*mag(weight), right-left)

    for cell in range(CELLS):
        left, right = two_pi*cell/CELLS, two_pi*(cell+1)/CELLS
        phi = left.lower().union(right.upper())
        u, v, up, vp, upp, vpp, primitive = arb(0), m, arb(0), arb(0), arb(0), arb(0), arb(0)
        for j in range(1, 33):
            n = 4*j
            sine, cosine = (n*phi).sin(), (n*phi).cos()
            u += us[j-1]*sine
            v += vc[j]*cosine
            up += n*us[j-1]*cosine
            vp -= n*vc[j]*sine
            upp -= n*n*us[j-1]*sine
            vpp -= n*n*vc[j]*cosine
            primitive += vc[j]*sine/n
        require(v < 0, 'whole root angular cell keeps its actual physical inverse gap')
        jacobian, jacobian_prime = v/m, vp/m
        omega = [bzero*v/m, a*u/m, rho]
        omega_prime = [bzero*vp/m, a*up/m, arb(0)]
        centre = [x.mid() for x in omega]
        connection_error = norm([x.rad() for x in omega])
        local_frame_error = (frame_error+width.upper()*connection_error).upper()
        rotation, integral = rotation_and_integral(centre, local_time)
        ideal_frame = mm(frame, rotation)
        actual_frame = [[x+arb(0, local_frame_error+rat(FRAME_FEE)) for x in row]
                        for row in ideal_frame]
        speed = rho*v
        speed_centre = speed.mid()
        speed_error = speed.rad()
        local_position_error = (position_error+width.upper()*
            (local_frame_error*mag(speed)+speed_error)).upper()
        partial_position = mv(mm(frame, integral), [arb(0), speed_centre, arb(0)])
        base_position = [position[k]+partial_position[k]+
                         arb(0, local_position_error+rat(POSITION_FEE)) for k in range(3)]
        om, omp = skew(omega), skew(omega_prime)
        actual_first = [[x+arb(0, mag(jacobian)*z0) for x in row]
                        for row in mm(actual_frame, om)]
        second_base_a, second_base_b = mm(actual_first, om), mm(actual_frame, omp)
        second_fee = mag(jacobian_prime)*z0+mag(jacobian)**2*z1
        actual_second = [[second_base_a[i][j]+second_base_b[i][j]+arb(0, second_fee)
                          for j in range(3)] for i in range(3)]
        X, Y = [row[0] for row in actual_frame], [row[1] for row in actual_frame]
        Xp, Yp = [row[0] for row in actual_first], [row[1] for row in actual_first]
        Xpp, Ypp = [row[0] for row in actual_second], [row[1] for row in actual_second]
        vector_T = add(X, scale(Y, -u))
        vector_Tp = add(add(Xp, scale(Y, -up)), scale(Yp, -u))
        vector_A = add(Xp, scale(Yp, -u))
        vector_Ap = add(add(Xpp, scale(Yp, -up)), scale(Ypp, -u))
        kval = scale(vector_T, rho/v)
        kprime = scale(add(scale(vector_Tp, 1/v), scale(vector_T, -vp/(v*v))), rho)
        bval, bprime = scale(Y, rho), scale(Yp, rho)
        cval = scale(vector_A, -rho/v)
        cprime = scale(add(scale(vector_Ap, 1/v), scale(vector_A, -vp/(v*v))), -rho)
        qzero = -primitive/m
        mean_a = 1/v-qzero*vp/(v*v)
        mean_b = -u*mean_a-qzero*up/v
        gm = scale(add(scale(X, mean_a), scale(Y, mean_b)), rho)
        Gprime = [speed*Y[k]+arb(0, mag(jacobian)*p0) for k in range(3)]
        vectors = (kval, kprime, bval, bprime, cval, cprime, gm, base_position, Gprime)

        for geometry_index, G in enumerate((base_position, ez, ex)):
            Gp = Gprime if geometry_index == 0 else zero
            coefficients = (
                2*triple(G, kval, bval),
                triple(G, kval, kprime)+2*triple(G, kval, cval),
                -triple(G, bval, bprime),
                -triple(G, cval, cprime),
                -triple(Gp, kval, bval)-2*triple(G, bval, cval),
                -triple(Gp, kval, cval),
                triple(Gp, bval, cval)+2*triple(G, bprime, cval))
            a0, aqq, arr, att, arq, aqt, art = coefficients
            for entry, (i, j) in enumerate(pairs):
                val = product(a0, 'sin', 'sin', i, j, (fs[i]*qs[j]+qs[i]*fs[j])/2, left, right)
                val += product(aqq, 'sin', 'sin', i, j, qs[i]*qs[j], left, right)
                val += product(arr, 'cos', 'cos', i, j, rs[i]*rs[j], left, right)
                val += product(att, 'cos', 'cos', i, j, ts[i]*ts[j], left, right)
                val += product(arq, 'cos', 'sin', i, j, rs[i]*qs[j]/2, left, right)
                val += product(arq, 'sin', 'cos', i, j, qs[i]*rs[j]/2, left, right)
                val += product(aqt, 'sin', 'cos', i, j, qs[i]*ts[j]/2, left, right)
                val += product(aqt, 'cos', 'sin', i, j, ts[i]*qs[j]/2, left, right)
                val += product(art, 'cos', 'cos', i, j, (rs[i]*ts[j]+ts[i]*rs[j])/2, left, right)
                local_grams[geometry_index][entry] += val/two_pi
            for i in range(2):
                mean_functionals[geometry_index][i] += (
                    wave(triple(G, kval, gm), 'sin', i, qs[i], left, right)
                    -wave(triple(G, bval, gm), 'cos', i, rs[i], left, right)
                    -wave(triple(G, cval, gm), 'cos', i, ts[i], left, right))/two_pi

        eint, emoment = [], []
        for i in range(2):
            n = frequencies[i]
            moment_cos = ((n*left).cos()-(n*right).cos())/(n*n)-width*(n*left).sin()/n
            for component in range(3):
                ev = wave(bprime[component], 'cos', i, rs[i], left, right)
                ev += wave(cprime[component], 'cos', i, ts[i], left, right)
                eint.append(ev)
                e_integral[i][component] += ev
                em = integrate_coefficient(bprime[component], sqrt2*rs[i]*moment_cos,
                    sqrt2*mag(rs[i]), width*width/2)
                em += integrate_coefficient(cprime[component], sqrt2*ts[i]*moment_cos,
                    sqrt2*mag(ts[i]), width*width/2)
                emoment.append(em)
        gm_int, gm_moment = scale(gm, width), scale(gm, width*width/2)
        all_values = [x for vector in vectors for x in vector]+eint+emoment+gm_int+gm_moment
        require(len(all_values) == 45, 'complete private cell representation')
        cache[cell] = packed(all_values)

        end_rotation, end_integral = rotation_and_integral(centre, width)
        advanced_frame = mm(frame, end_rotation)
        advanced_position = add(position, mv(mm(frame, end_integral), [arb(0), speed_centre, arb(0)]))
        frame_error = (local_frame_error+norm([x.rad() for row in advanced_frame for x in row])).upper()
        position_error = (local_position_error+norm([x.rad() for x in advanced_position])).upper()
        frame = [[x.mid() for x in row] for row in advanced_frame]
        position = [x.mid() for x in advanced_position]
        maximum_frame_error = maximum_frame_error.union(frame_error).upper()
        maximum_position_error = maximum_position_error.union(position_error).upper()
        require(frame_error < 1 and position_error < 1, 'finite new root comparison guards')
        if (cell+1) % 1024 == 0 or cell+1 == CELLS:
            document.update(completed_cells=cell+1,
                current_frame_error_upper=recorded(frame_error),
                current_position_error_upper=recorded(position_error), seconds=time.monotonic()-started)
            save(args.output, document)
            print(json.dumps(dict(stage=document['stage'], completed_cells=cell+1, cells=CELLS)), flush=True)

    ell = [inverse_denominator*e_integral[i][2]/two_pi for i in range(2)]
    ell_records = [recorded(x) for x in ell]
    ell = [unpack(x) for x in ell_records]
    document.update(stage='complete-new-root-two-response-primitives',
        complete_new_mean_functional=ell_records,
        maximum_new_ideal_frame_error_upper=recorded(maximum_frame_error),
        maximum_new_ideal_position_error_upper=recorded(maximum_position_error))
    save(args.output, document)
    prefix = [[arb(0) for _ in range(3)] for _ in range(2)]
    integral_prefix = [[arb(0) for _ in range(3)] for _ in range(2)]
    for cell in range(CELLS):
        values = unpacked(cache[cell])
        eint, emoment, gmint, gmmoment = values[27:33], values[33:39], values[39:42], values[42:45]
        prefix_cache[cell] = packed([x for vector in prefix for x in vector])
        for i in range(2):
            for component in range(3):
                integral_prefix[i][component] += (width*prefix[i][component]
                    +emoment[3*i+component]-ell[i]*gmmoment[component])
                prefix[i][component] += eint[3*i+component]-ell[i]*gmint[component]
    require(all(x.contains(0) for vector in prefix for x in vector),
            'complete two actual mean-eliminated response integrals contain their exact periodic zero')
    primitive_mean = [[x/two_pi for x in vector] for vector in integral_prefix]
    document.update(complete_response_primitive_mean=[recorded(x) for vector in primitive_mean for x in vector],
        complete_response_periodicity_check=True, stage='complete-new-root-two-mode-nonlocal-form')
    save(args.output, document)
    # Use readback records for the completed mean subtraction.
    readback_means = [unpack(x) for x in document['complete_response_primitive_mean']]
    primitive_mean = [readback_means[:3], readback_means[3:]]
    nonlocal_grams = [[arb(0) for _ in pairs] for _ in range(3)]
    for cell in range(CELLS):
        left, right = two_pi*cell/CELLS, two_pi*(cell+1)/CELLS
        phi = left.lower().union(right.upper())
        values = unpacked(cache[cell])
        vectors = [values[3*i:3*i+3] for i in range(9)]
        kval, kprime, bval, bprime, cval, cprime, gm, base_position, Gprime = vectors
        start_values = unpacked(prefix_cache[cell])
        primitives = []
        for i in range(2):
            n = frequencies[i]
            partial_cos = ((n*phi).sin()-(n*left).sin())/n
            vector = []
            for component in range(3):
                partial_e = integrate_coefficient(bprime[component], sqrt2*rs[i]*partial_cos,
                    sqrt2*mag(rs[i]), width)
                partial_e += integrate_coefficient(cprime[component], sqrt2*ts[i]*partial_cos,
                    sqrt2*mag(ts[i]), width)
                partial_gm = gm[component].mid()*local_time+arb(0, gm[component].rad()*width.upper())
                vector.append(start_values[3*i+component]+partial_e-ell[i]*partial_gm
                              -primitive_mean[i][component])
            primitives.append(vector)

        for geometry_index, G in enumerate((base_position, ez, ex)):
            Gp = Gprime if geometry_index == 0 else zero

            def primitive_pair(i, j):
                Vi = primitives[i]
                out = wave(triple(G, Vi, bprime), 'cos', j, rs[j], left, right)
                out += wave(triple(G, Vi, cprime), 'cos', j, ts[j], left, right)
                out -= ell[j]*width*triple(G, Vi, gm)
                out -= wave(triple(Gp, Vi, kval), 'sin', j, qs[j], left, right)
                out += wave(triple(Gp, Vi, bval), 'cos', j, rs[j], left, right)
                out += wave(triple(Gp, Vi, cval), 'cos', j, ts[j], left, right)
                return out/two_pi

            for entry, (i, j) in enumerate(pairs):
                nonlocal_grams[geometry_index][entry] += (primitive_pair(i, j)+primitive_pair(j, i))/2
        if (cell+1) % 2048 == 0 or cell+1 == CELLS:
            document.update(nonlocal_completed_cells=cell+1, seconds=time.monotonic()-started)
            save(args.output, document)
            print(json.dumps(dict(stage=document['stage'], completed_cells=cell+1, cells=CELLS)), flush=True)

    affine = [[arb(0) for _ in pairs] for _ in range(3)]
    for geometry_index in range(3):
        for entry, (i, j) in enumerate(pairs):
            affine[geometry_index][entry] = (local_grams[geometry_index][entry]
                -ell[i]*mean_functionals[geometry_index][j]
                -ell[j]*mean_functionals[geometry_index][i]
                +nonlocal_grams[geometry_index][entry])
    document.update(complete_affine_signed_form={name: [recorded(x) for x in vector]
        for name, vector in zip(('constant', 'axis_q', 'axis_s'), affine)},
        complete_axis_q_ball=recorded(axis_q), complete_axis_s_ball=recorded(axis_s),
        private_cache_sha256=hashlib.sha256(cache.tobytes()).hexdigest(),
        private_response_prefix_sha256=hashlib.sha256(prefix_cache.tobytes()).hexdigest(),
        private_cache_bytes=int(cache.nbytes+prefix_cache.nbytes),
        stage='complete-new-root-two-mode-signed-form-before-comparison')
    save(args.output, document)
    saved = json.loads(args.output.read_text())
    affine = [[unpack(x) for x in saved['complete_affine_signed_form'][name]]
              for name in ('constant', 'axis_q', 'axis_s')]
    axis_q, axis_s = unpack(saved['complete_axis_q_ball']), unpack(saved['complete_axis_s_ball'])
    signed = [affine[0][i]+axis_q*affine[1][i]+axis_s*affine[2][i] for i in range(3)]
    document['complete_actual_signed_two_mode_matrix'] = [recorded(x) for x in signed]
    save(args.output, document)
    signed = [unpack(x) for x in json.loads(args.output.read_text())['complete_actual_signed_two_mode_matrix']]
    aa, ab, bb = signed
    determinant = aa*bb-ab*ab
    determinant_record = recorded(determinant)
    determinant = unpack(determinant_record)
    trial_directions = [(Fraction(1), Fraction(0)), (Fraction(0), Fraction(1))]
    if not bb.contains(0):
        slope = Fraction(float((-ab.mid()/bb.mid()))).limit_denominator(2**16)
        trial_directions.append((Fraction(1), slope))
    for denominator_power in range(0, 7):
        trial_directions.extend((Fraction(1), Fraction(sign, 2**denominator_power)) for sign in (-1, 1))
    witness = None
    for first, second in trial_directions:
        value = rat(first)**2*aa+2*rat(first)*rat(second)*ab+rat(second)**2*bb
        record = recorded(value)
        if unpack(record) < 0:
            witness = dict(exact_z_coefficients=[str(first), str(second)],
                           complete_signed_value=record,
                           strict_upper_negative_after_complete_saved_ball_readback=True)
            break
    document.update(complete=True, proved=True, failure=None,
        stage='complete-new-root-two-mode-signed-form',
        complete_actual_signed_determinant=determinant_record,
        determinant_strictly_negative=bool(determinant < 0), negative_witness=witness,
        strict_sign_uses_complete_saved_decimal_balls=True,
        seconds=time.monotonic()-started)
    negative = witness is not None or bool(determinant < 0)
    document['scope'].update(signed_two_mode_form_complete=True,
        negative_two_mode_direction_proved=negative,
        all_root_data_nonnegative_form_excluded=negative)
    save(args.output, document)
    print(json.dumps(dict(complete=True, negative_two_mode_direction_proved=negative,
        rational_witness=witness is not None, output=str(args.output))), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for flag in ('definition_source', 'candidate', 'germ', 'axis', 'axis_execution',
                 'mean', 'mean_execution', 'physical_budget', 'physical_execution', 'output'):
        parser.add_argument('--'+flag.replace('_', '-'), type=Path, required=True)
    args = parser.parse_args()
    try:
        run(args)
    except Exception as error:
        if args.output.exists():
            document = json.loads(args.output.read_text())
            if not document.get('complete'):
                document['failure'] = dict(type=type(error).__name__, message=str(error))
                save(args.output, document)
        raise


if __name__ == '__main__':
    main()
