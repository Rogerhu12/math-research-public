#!/usr/bin/env python3
"""Original all-high root lower bound and finite-receiver coefficients.

New public Actions scalar target only. Whole axis, mean, X and signed 96/97
results are admitted without rerunning any of their scientific targets.
A private angular quadrature supplies only the new complete coefficient
bounds. No old signed matrix entry, Z/P propagation or response primitive
is evaluated. Actual frame/position errors and full means remain explicit.
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

KIND = 'R138_same_Qrepair_original_high_root_lower_bound_v1'
CELLS = 32768
BITS = 320
HIGH_FREQUENCY = 388
NEAR_FREQUENCY = 194
DEFINITION_SHA = 'd152f31cef53c1d58099cf3d1f994d2dad9d31d6a75cb42a7d9e54a35c17ae79'
AXIS_SHA = 'b300ea209acb2239a93a87aa3f14d6d9c5f0ed3b5b88ea44b415e5078ea0cd92'
AXIS_EXECUTION_SHA = 'a8979dff609fd41e88be754e09e8fbb2a56528f101c729208e5e54a9ef1de73f'
MEAN_SHA = 'de3a14606aa432fbd1f7707c277a33110f81ce6ca23fdfc6bfdf7e9d497623b4'
MEAN_EXECUTION_SHA = '25d6e66fade5f838a33e62da0f502152115a34c5c572c662471b6c9acad38cb5'
X_SHA = '1259c3687cea0af523dd52055e88d5ee9a7b77094c218101835b6c38dfbbc7ec'
X_EXECUTION_SHA = '999555eafb3c443266f1a8fed98056c9d4f448c0131ef5ffff93941b35040c92'
TWO_MODE_SHA = '95c80fdeeb3cf75327f028b1020db5aeda0fa3502aa6c0b3546c17ac6d2258c2'
TWO_MODE_EXECUTION_SHA = 'f66a976a0433204c9c043ab977d58439f091d2304b6cd9ef1df13eac0ae2c0f2'
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

    axis = read(args.axis, AXIS_SHA)
    mean_result = read(args.mean, MEAN_SHA)
    old_x = read(args.physical_budget, X_SHA)
    two_mode = read(args.two_mode, TWO_MODE_SHA)
    receipts = [read(args.axis_execution, AXIS_EXECUTION_SHA),
                read(args.mean_execution, MEAN_EXECUTION_SHA),
                read(args.physical_execution, X_EXECUTION_SHA),
                read(args.two_mode_execution, TWO_MODE_EXECUTION_SHA)]
    for receipt, run_id, science_sha in zip(receipts,
            ('44730968113', '44733403315', '44737045152', '44745192261'),
            (AXIS_SHA, MEAN_SHA, X_SHA, TWO_MODE_SHA)):
        execution_admission(receipt, run_id, science_sha)
    require(all(d.get('complete') is True and d.get('proved') is True
                and d.get('failure') is None for d in (axis, mean_result, old_x, two_mode)),
            'all four original whole conclusions are complete and proved')
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

    require(two_mode['completed_cells'] == 32768
        and two_mode['nonlocal_completed_cells'] == 32768
        and two_mode['scope']['signed_two_mode_form_complete'] is True
        and two_mode['scope']['negative_two_mode_direction_proved'] is True
        and two_mode['scope']['actual_positive_boundary_problem_singular'] is False
        and two_mode['scope']['positive_inverse_proved'] is False
        and two_mode['scope']['final_topic_complete'] is False
        and all(two_mode[k] == 0 for k in ('old_axis_targets_called',
            'old_mean_targets_called', 'old_X_targets_called', 'old_geometry_targets_called'))
        and two_mode['whole_original_references'] == dict(axis=axis,
            mean=mean_result, physical_budget=old_x),
        'whole completed signed two-mode result and all nested originals retained')
    require(two_mode['identity']['candidate_sha256'] == definition.CANDIDATE_SHA
        and two_mode['identity']['germ_sha256'] == definition.GERM_SHA
        and two_mode['identity']['exact_root_interval'] == root_interval
        and two_mode['identity']['repair_definition_sha256'] == definition.REPAIR_DEFINITION_SHA
        and two_mode['identity']['fixed_point'] == '(0,0,1/2)',
        'old signed form is exactly the same object and complete true root')
    # Reuse its complete old axis balls; this is admission, not a new axis target.
    axis_q = unpack(two_mode['complete_axis_q_ball'])
    axis_s = unpack(two_mode['complete_axis_s_ball'])
    axis_error = unpack(axis['complete_axis_error']).upper()
    require(axis_q.contains(unpack(axis['nominal_q'])+arb(0, axis_error))
        and axis_s.contains(unpack(axis['nominal_s'])+arb(0, axis_error)),
        'old complete signed-form axis balls contain the uncut original axis ball')
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
    two_pi = 2*arb.pi()
    width = two_pi/CELLS
    local_time = arb(0).union(width.upper())
    inverse_D_bound = rat(Fraction(20, 17))
    paid_G0 = rat(Fraction(222, 125))
    paid_sigma = rat(Fraction(2, 5))

    def minimum_upper(first, second):
        first, second = first.upper(), second.upper()
        return first if first < second else second

    def maximum_lower(first, second):
        first, second = first.lower(), second.lower()
        return first if first > second else second

    def negative_part(value):
        candidate = -value.lower()
        return candidate.upper() if candidate > 0 else arb(0)

    def with_vector_error(vector, error):
        radius = mag(error)
        return [x+arb(0, radius) for x in vector]

    identity = dict(kind=KIND, source_sha256=sha(__file__),
        definition_source_sha256=DEFINITION_SHA,
        prior_axis_sha256=AXIS_SHA, prior_axis_execution_sha256=AXIS_EXECUTION_SHA,
        prior_mean_sha256=MEAN_SHA, prior_mean_execution_sha256=MEAN_EXECUTION_SHA,
        prior_physical_budget_sha256=X_SHA, prior_physical_execution_sha256=X_EXECUTION_SHA,
        prior_two_mode_sha256=TWO_MODE_SHA,
        prior_two_mode_execution_sha256=TWO_MODE_EXECUTION_SHA,
        candidate_sha256=definition.CANDIDATE_SHA, germ_sha256=definition.GERM_SHA,
        object_sha256=definition.OBJECT_SHA,
        repair_definition_sha256=definition.REPAIR_DEFINITION_SHA,
        eta=str(definition.ETA), actual_nu=str(definition.NU), exact_alpha=str(alpha),
        exact_root_interval=root_interval, complete_angular_interval='[0,2*pi]',
        cells=CELLS, arithmetic_bits=BITS, original_low_modes=[1,96],
        original_high_modes='j>=97', minimum_high_frequency=HIGH_FREQUENCY,
        primitive_near_frequency=NEAR_FREQUENCY,
        congruence='S=P_low*N+P_high*N^(1/3); original low1..96/high97..infinity',
        actual_periodic_frame_C0_fee=str(FRAME_FEE), actual_position_C0_fee=str(POSITION_FEE),
        fixed_point='(0,0,1/2)', frame_at_zero='X=e_z,Y=e_y,n=e_x',
        projection_vector='ell=X(root,0)=local e_z',
        paid_actual_support_lower='2/5', paid_actual_position_norm_upper='222/125',
        all_high_principal_factor='2^(1/6)/32 * 388^(-4/3)',
        exact_old_signed_entries_are_read_only=True)
    document = dict(identity=identity, complete=False, proved=False, failure=None,
        stage='complete-new-original-high-root-scalar-enclosure', completed_cells=0,
        old_axis_targets_called=0, old_mean_targets_called=0, old_X_targets_called=0,
        old_two_mode_matrix_entries_recomputed=0, old_ZP_propagations_called=0,
        old_geometry_targets_called=0, published_arrays=False,
        whole_original_references=dict(two_mode=two_mode),
        scope=dict(same_Qrepair_true_root=True,
            original_root_low96_and_all_high_rows_preserved=True,
            independent_mean_eliminated_with_actual_saved_denominator=True,
            original_high_compression_lower_bound_complete=False,
            original_high_compression_positive=False, receiver_neumann_inverse_paid=False,
            actual_positive_boundary_problem_singular=False,
            positive_inverse_proved=False, final_topic_complete=False),
        seconds=time.monotonic()-started,
        private_geometry_only_for_new_scalar_targets=True,
        old_signed_two_mode_scope_preserved=True)
    save(args.output, document)

    scalar_names = ('principal_a_second_upper', 'A_qq_negative_upper',
        'A_RR_negative_upper', 'A_TT_negative_upper', 'A_Rq_absolute_upper',
        'A_qT_absolute_upper', 'A_RT_absolute_upper', 'k_0_upper', 'b_0_upper',
        'c_0_upper', 'b_1_upper', 'b_2_upper', 'c_1_upper', 'g_m_0_upper',
        'G_0_upper', 'G_1_upper')
    suprema = {name: arb(0) for name in scalar_names}
    receiver_names = ('chi_0_upper', 'chi_1_upper', 'V_0_upper', 'V_1_upper', 'X_1_upper')
    receiver_suprema = {name: arb(0) for name in receiver_names}
    principal_lower = None
    chi_q0_squared_integral = arb(0)
    frame = [[arb(0),arb(0),arb(1)], [arb(0),arb(1),arb(0)], [arb(1),arb(0),arb(0)]]
    position = [arb(0),arb(0),arb(0)]
    frame_error, position_error = arb(0), arb(0)

    def retain_upper(destination, name, value):
        require(value.is_finite(), 'finite complete new coefficient bound: '+name)
        candidate = value.upper()
        require(candidate >= 0, 'nonnegative complete upper bound: '+name)
        destination[name] = destination[name].union(candidate).upper()

    for cell in range(CELLS):
        left, right = two_pi*cell/CELLS, two_pi*(cell+1)/CELLS
        phi = left.lower().union(right.upper())
        u, v, up, vp, upp, vpp, primitive = arb(0), m, arb(0), arb(0), arb(0), arb(0), arb(0)
        for j in range(1,33):
            n = 4*j
            sine, cosine = (n*phi).sin(), (n*phi).cos()
            u += us[j-1]*sine
            v += vc[j]*cosine
            up += n*us[j-1]*cosine
            vp -= n*vc[j]*sine
            upp -= n*n*us[j-1]*sine
            vpp -= n*n*vc[j]*cosine
            primitive += vc[j]*sine/n
        require(v < 0, 'entire new root coefficient cell retains the actual inverse gap')
        jacobian, jacobian_prime = v/m, vp/m
        omega = [bzero*jacobian, rho*u, rho]
        omega_prime = [bzero*jacobian_prime, rho*up, arb(0)]
        centre = [x.mid() for x in omega]
        connection_error = norm([x.rad() for x in omega])
        local_frame_error = (frame_error+width.upper()*connection_error).upper()
        rotation, integral = rotation_and_integral(centre, local_time)
        ideal_frame = mm(frame, rotation)
        actual_frame = [[x+arb(0, local_frame_error+rat(FRAME_FEE)) for x in row]
                        for row in ideal_frame]
        speed, speed_prime = rho*v, rho*vp
        speed_centre, speed_error = speed.mid(), speed.rad()
        local_position_error = (position_error+width.upper()*
            (local_frame_error*mag(speed)+speed_error)).upper()
        partial_position = mv(mm(frame, integral), [arb(0),speed_centre,arb(0)])
        base_position = [position[k]+partial_position[k]+
            arb(0,local_position_error+rat(POSITION_FEE)) for k in range(3)]
        G = add(base_position,[axis_s,arb(0),axis_q])
        om, omp = skew(omega), skew(omega_prime)
        actual_first = [with_vector_error(row,mag(jacobian)*z0)
                        for row in mm(actual_frame,om)]
        second_a, second_b = mm(actual_first,om), mm(actual_frame,omp)
        second_fee = mag(jacobian_prime)*z0+mag(jacobian)**2*z1
        actual_second = [with_vector_error(add(second_a[i],second_b[i]),second_fee)
                         for i in range(3)]
        X,Y,normal = ([row[j] for row in actual_frame] for j in range(3))
        Xp,Yp,npv = ([row[j] for row in actual_first] for j in range(3))
        Xpp,Ypp,npp = ([row[j] for row in actual_second] for j in range(3))
        vector_T = add(X,scale(Y,-u))
        vector_V = add(Y,scale(X,u))
        vector_Vp = add(add(Yp,scale(X,up)),scale(Xp,u))
        M = 1+u*u
        M_upper = 1+mag(u)**2
        sqrt_M = M_upper.sqrt().upper()
        G0 = minimum_upper(norm(G),paid_G0)
        Gp = with_vector_error(scale(Y,speed),mag(jacobian)*p0)
        Gpp = with_vector_error(add(scale(Y,speed_prime),scale(Yp,speed)),
                               mag(jacobian_prime)*p0+mag(jacobian)**2*p1)
        G1 = minimum_upper(norm(Gp),mag(speed)+mag(jacobian)*p0)
        sigma = dot(G,normal)
        sigma_lower = maximum_lower(sigma.lower(),paid_sigma)
        sigma_prime = dot(Gp,normal)+dot(G,npv)
        sigma_second = dot(Gpp,normal)+2*dot(Gp,npv)+dot(G,npp)
        cell_a_lower = (2*rho*rho*sigma_lower/(-v)).lower()
        require(cell_a_lower > 0, 'same actual support gives positive complete principal coefficient')
        principal_lower = cell_a_lower if principal_lower is None else principal_lower.union(cell_a_lower).lower()
        a_second = -2*rho*rho*(sigma_second/v-2*sigma_prime*vp/(v*v)
                       -sigma*vpp/(v*v)+2*sigma*vp*vp/(v*v*v))

        kval = scale(vector_T,rho/v)
        bval,bprime = scale(Y,rho),scale(Yp,rho)
        # c=-(rho/m)[b_geom(Y+uX)+(Z_X-uZ_Y)] exactly.
        # Its angular derivative uses only Z_theta and actual frame C1.
        cval = with_vector_error(scale(vector_V,-rho*bzero/m),mag(rho/m)*sqrt_M*z0)
        cprime = with_vector_error(scale(vector_Vp,-rho*bzero/m),
                    mag(rho/m)*(mag(jacobian)*sqrt_M*z1+mag(up)*z0))
        qzero = -primitive/m
        mean_a = 1/v-qzero*vp/(v*v)
        mean_b = -u*mean_a-qzero*up/v
        gm0 = mag(rho)*(mag(mean_a)**2+mag(mean_b)**2).sqrt()
        V1 = ((mag(up-jacobian*bzero)**2+mag(u*jacobian*bzero)**2
               +mag(rho*M)**2).sqrt()+mag(jacobian)*sqrt_M*z0).upper()
        X1 = ((mag(jacobian*bzero)**2+mag(rho*u)**2).sqrt()+mag(jacobian)*z0).upper()
        b1 = (mag(rho)*((mag(jacobian*bzero)**2+mag(rho)**2).sqrt()
                       +mag(jacobian)*z0)).upper()
        w1,w2,w3 = omega
        b2_closed = mag(rho)*((mag(omega_prime[0]+w3*w2)**2
             +mag(w1*w1+w3*w3)**2+mag(w1*w2)**2).sqrt()
             +mag(jacobian)*(mag(w1)**2+mag(w3)**2).sqrt()*z0
             +mag(jacobian_prime)*z0+mag(jacobian)**2*z1)
        b2 = minimum_upper(mag(rho)*norm(Ypp),b2_closed)
        c0 = mag(rho/m)*sqrt_M*(mag(bzero)+z0)
        c1 = mag(rho/m)*(mag(bzero)*V1+mag(jacobian)*sqrt_M*z1+mag(up)*z0)
        k0 = mag(rho/v)*sqrt_M

        # HP.13 retains the actual Z defect before taking the signed negative part.
        Aqq_centre = rho*rho/(v*v)*(jacobian*bzero*M+up)*sigma
        Aqq_fee = mag(rho*rho/(v*v))*mag(jacobian)*G0*M_upper*z0
        Aqq = Aqq_centre+arb(0,Aqq_fee)
        ARR = -triple(G,bval,bprime)
        ATT = -triple(G,cval,cprime)
        ARq = -triple(Gp,kval,bval)-2*triple(G,bval,cval)
        AqT = -triple(Gp,kval,cval)
        ART = triple(Gp,bval,cval)+2*triple(G,bprime,cval)
        current = dict(principal_a_second_upper=mag(a_second),
            A_qq_negative_upper=negative_part(Aqq),A_RR_negative_upper=negative_part(ARR),
            A_TT_negative_upper=negative_part(ATT),A_Rq_absolute_upper=mag(ARq),
            A_qT_absolute_upper=mag(AqT),A_RT_absolute_upper=mag(ART),
            k_0_upper=k0,b_0_upper=mag(rho),c_0_upper=c0,b_1_upper=b1,b_2_upper=b2,
            c_1_upper=c1,g_m_0_upper=gm0,G_0_upper=G0,G_1_upper=G1)
        for name,value in current.items():
            retain_upper(suprema,name,value)
        chi = up/v
        chi_prime = upp/v-up*vp/(v*v)
        current_receiver = dict(chi_0_upper=mag(chi),chi_1_upper=mag(chi_prime),
            V_0_upper=sqrt_M,V_1_upper=V1,X_1_upper=X1)
        for name,value in current_receiver.items():
            retain_upper(receiver_suprema,name,value)
        chi_q0_squared_integral += mag(chi*qzero)**2/CELLS

        # Private geometry is only an intermediate of these new scalar bounds.
        # No old signed entry, old mean target, or old X propagation is evaluated.
        end_rotation,end_integral = rotation_and_integral(centre,width)
        advanced_frame = mm(frame,end_rotation)
        advanced_position = add(position,mv(mm(frame,end_integral),[arb(0),speed_centre,arb(0)]))
        frame_error = (local_frame_error+norm([x.rad() for row in advanced_frame for x in row])).upper()
        position_error = (local_position_error+norm([x.rad() for x in advanced_position])).upper()
        frame = [[x.mid() for x in row] for row in advanced_frame]
        position = [x.mid() for x in advanced_position]
        require(frame_error < 1 and position_error < 1, 'new private quadrature enclosure remains finite')
        if (cell+1)%1024 == 0 or cell+1 == CELLS:
            document.update(completed_cells=cell+1,seconds=time.monotonic()-started)
            save(args.output,document)
            print(json.dumps(dict(stage=document['stage'],completed_cells=cell+1,cells=CELLS)),flush=True)

    # Publish the complete new coefficient balls first. Every subsequent scalar
    # uses the appropriate endpoint of this actual saved-file readback.
    new_bounds = {name:recorded(value.upper()) for name,value in suprema.items()}
    new_bounds['principal_a_minimum_lower'] = recorded(principal_lower.lower())
    receiver_coefficients = {name:recorded(value.upper()) for name,value in receiver_suprema.items()}
    receiver_coefficients.update(
        chi_q0_L2_upper=recorded(chi_q0_squared_integral.sqrt().upper()),
        m_absolute_upper=recorded(mag(m)),rho_inverse_upper=recorded(mag(m/a)))
    document.update(complete_new_scalar_bounds=new_bounds,
        complete_receiver_coefficients=receiver_coefficients,
        stage='complete-new-original-high-root-coefficients-before-comparison')
    save(args.output,document)
    saved=json.loads(args.output.read_text())
    sb={name:unpack(value).upper() for name,value in saved['complete_new_scalar_bounds'].items()
        if name!='principal_a_minimum_lower'}
    a_min=unpack(saved['complete_new_scalar_bounds']['principal_a_minimum_lower']).lower()
    rb={name:unpack(value).upper() for name,value in saved['complete_receiver_coefficients'].items()}
    n=arb(HIGH_FREQUENCY)
    qH=n**rat(Fraction(-1,3));rH=n**rat(Fraction(-2,3));tH=n**rat(Fraction(-4,3))
    YH=sb['k_0_upper']*qH+sb['b_0_upper']*rH+sb['c_0_upper']*tH
    EH=sb['b_1_upper']*rH+sb['c_1_upper']*tH
    mean_b=minimum_upper(sb['b_1_upper']*rH,sb['b_2_upper']*n**rat(Fraction(-5,3)))
    LH=inverse_D_bound*(mean_b+sb['c_1_upper']*tH)
    VH=EH+sb['g_m_0_upper']*LH
    near=arb(NEAR_FREQUENCY)
    far=minimum_upper(sb['b_1_upper'],arb(2).sqrt()*sb['b_2_upper']/(n-near))
    primitive_b=rH*((sb['b_1_upper']/near)**2+far*far).sqrt()
    IH=minimum_upper(VH,primitive_b+sb['c_1_upper']*tH+sb['g_m_0_upper']*LH)
    eps_pr=arb(2)**rat(Fraction(1,6))/32*tH*sb['principal_a_second_upper']
    eps_local=(sb['A_qq_negative_upper']*qH*qH+sb['A_RR_negative_upper']*rH*rH
        +sb['A_TT_negative_upper']*tH*tH+sb['A_Rq_absolute_upper']*rH*qH
        +sb['A_qT_absolute_upper']*qH*tH+sb['A_RT_absolute_upper']*rH*tH)
    eps_mean=2*sb['G_0_upper']*sb['g_m_0_upper']*LH*YH
    eps_primitive=sb['G_0_upper']*IH*VH+sb['G_1_upper']*IH*YH
    lower_terms=dict(Y_H_upper=YH,E_H_upper=EH,L_H_upper=LH,V_H_upper=VH,I_H_upper=IH,
        principal_error_upper=eps_pr,signed_local_error_upper=eps_local,
        mean_rank_error_upper=eps_mean,complete_primitive_error_upper=eps_primitive)
    document['complete_high_lower_bound_terms']={name:recorded(value.upper())
                                               for name,value in lower_terms.items()}
    receiver_coefficients['kappa_upper']=recorded((n**rat(Fraction(-2,3))*rb['chi_0_upper']).upper())
    document['complete_receiver_coefficients']=receiver_coefficients
    save(args.output,document)
    saved=json.loads(args.output.read_text())
    terms={name:unpack(value).upper() for name,value in saved['complete_high_lower_bound_terms'].items()}
    lambda_H=a_min-terms['principal_error_upper']-terms['signed_local_error_upper']\
        -terms['mean_rank_error_upper']-terms['complete_primitive_error_upper']
    document['complete_actual_high_lower_bound']=recorded(lambda_H.lower())
    saved_kappa=unpack(saved['complete_receiver_coefficients']['kappa_upper']).upper()

    # These are the complete F.2 source coefficients for the later relative
    # low96 receiver. They do not assert an all-root-data C_* bound.
    CV0=arb(2)**rat(Fraction(1,6))+inverse_D_bound*sb['g_m_0_upper']
    CV13=arb(2)**rat(Fraction(1,3))+inverse_D_bound*arb(2)**rat(Fraction(1,6))*sb['g_m_0_upper']
    MG13=sb['G_0_upper']**rat(Fraction(2,3))*(sb['G_0_upper']+sb['G_1_upper'])**rat(Fraction(1,3))
    source_factor=sb['G_1_upper']*CV0+2*inverse_D_bound*sb['G_0_upper']*sb['g_m_0_upper']
    low_mean=inverse_D_bound*minimum_upper(sb['b_1_upper'],sb['b_2_upper']/4)
    low_omega=sb['b_0_upper']+sb['b_1_upper']+sb['g_m_0_upper']*low_mean
    high_omega=terms['Y_H_upper']+terms['I_H_upper']
    source_coefficients=dict(C_omega_L_upper=low_omega,C_omega_H_upper=high_omega,
        C_L_upper=source_factor*low_omega,C_H_cross_upper=source_factor*high_omega,
        C_quad_upper=MG13*CV13+inverse_D_bound*sb['G_0_upper']*sb['g_m_0_upper']*CV0)
    document['complete_nonhomogeneous_source_coefficients']={name:recorded(value.upper())
        for name,value in source_coefficients.items()}
    save(args.output,document)
    final_saved=json.loads(args.output.read_text())
    positive=bool(unpack(final_saved['complete_actual_high_lower_bound']).lower()>0)
    neumann=bool(unpack(final_saved['complete_receiver_coefficients']['kappa_upper']).upper()<1)
    require(neumann == bool(saved_kappa<1),'same complete saved kappa gate after final readback')
    document.update(complete=True,proved=True,failure=None,
        stage='complete-new-original-high-root-lower-bound',
        high_lower_bound_positive=positive,receiver_neumann_gate=neumann,
        strict_gates_use_complete_saved_decimal_balls=True,seconds=time.monotonic()-started)
    document['scope'].update(original_high_compression_lower_bound_complete=True,
        original_high_compression_positive=positive,receiver_neumann_inverse_paid=neumann)
    save(args.output,document)
    print(json.dumps(dict(complete=True,original_high_compression_positive=positive,
        receiver_neumann_inverse_paid=neumann,output=str(args.output))),flush=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for flag in ('definition_source','candidate','germ','axis','axis_execution','mean','mean_execution',
                 'physical_budget','physical_execution','two_mode','two_mode_execution','output'):
        parser.add_argument('--'+flag.replace('_','-'),type=Path,required=True)
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
