"""P96 full signed phase row on the original finite TC trial columns.

All Fourier products constructing the adjoint row are complete. Only its
pairing with the known degree96 trial is projected to96. Eight exact radial
moments replace96 separate angular FFT calculations. Old scientific targets
are not evaluated; the implicit true root and its omitted transport sliver
are retained explicitly.
"""
from fractions import Fraction as F

STOP = F('1249886203106135147/5242880000000000000')
ROOT_UPPER = F('2383968743003/10000000000000')
OUTPUT_ORDER = (
    'complete_original_TC_phase_trial_row96',
    'complete_original_TC_negative_trial_L1_L2_upper96',
    'complete_original_TC_negative_phase_field_L1_upper96',
    'complete_true_root_phase_sliver_upper96',
    'complete_same_selected_TC_phase_row96',
    'complete_same_selected_TC_phase_joint_radius_upper',
)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def saved_scalar_comparisons():
    """Only new rational consequences of already completed complete bounds."""
    eps, dK, qm, qM = F('2e-9'), F('1.048e-7'), F('.5338'), F('1.03')
    field_difference = 2*(eps+qM*qM*eps+4*dK)+F('4e-10')*qM+7*dK/(2*qm)
    root_receiver = 2*F(11,10)**2*(2*qM*qM*7+7*qM)
    label_square_error = F('1.6e-5')*(2*F(11,10)+F('1.6e-5'))
    checks = {
        'whole_selected_state_field_change': field_difference<F('1.535e-6'),
        'complete_true_root_sliver_receiver': root_receiver<54,
        'whole_squared_label_difference': label_square_error<F('3.521e-5'),
        'entire_old_transport_to_true_root_sliver_width': ROOT_UPPER-STOP<F('2.34e-10'),
    }
    require(all(checks.values()), 'all new exact saved-scalar phase bounds')
    return checks


def balls(c, value):
    value = c.finite(value)
    require(value.lo.shape == value.hi.shape == (96,), 'one whole vector of96 directed values')
    return [c.arb(float(a)).union(c.arb(float(b))) for a, b in zip(value.lo, value.hi)]


def upper_balls(c, value):
    return [x.upper() for x in balls(c, c.upper(value))]


def scalar_model(c, core, model, name, left, right, read_ball):
    """Full old degree7 value polynomial plus its entire uniform remainder."""
    a, b = map(F, model['interval'])
    require(a <= left < right <= b, 'same whole original scalar-model interval')
    item = model['models'][name]
    coefficients = [c.box(F(x)) for x in item['exact_centered_polynomial']]
    require(len(coefficients) == 8, 'every original scalar coefficient')
    midpoint, half = (left+right)/2, (right-left)/2
    cs = c.affine_polynomial(coefficients, midpoint-F(model['center']), half)
    error = read_ball(item['complete_uniform_remainder']).upper()
    return core.BatchRadialFourier.scalar(c, cs, c.arb_box(error).hi)


def odd_part(c, core, value):
    z = value.Fourier()
    opposite = (-c.np.arange(core.GRID)) % core.GRID
    odd = (z-z[opposite])/2
    return core.BatchRadialFourier.from_fourier(
        c, odd, value.degree, value.error, value.error_degree)


def complete_raw_row_coefficients(c, ell1, ell2):
    """Exact orthonormal193 coefficients; full ell was formed first."""
    za, zb = ell1.Fourier(), ell2.Fourier()
    degree = max(za.real.lo.shape[1], zb.real.lo.shape[1])
    out = []
    root2 = 2*c.sqrt_half
    for k in range(degree):
        row = c.Box(c.np.zeros((193, 1)))
        def place(index, value):
            value = c.finite(value)
            require(value.lo.shape == value.hi.shape == (), 'one complete real row coefficient')
            row.lo[index, 0], row.hi[index, 0] = value.lo, value.hi
        if k < za.real.lo.shape[1]:
            for j in range(1, 97):
                place(j-1, -root2*za.imag[j, k, 0])
        if k < zb.real.lo.shape[1]:
            place(96, zb.real[0, k, 0])
            for j in range(1, 97):
                place(96+j, root2*zb.real[j, k, 0])
        out.append(c.finite(row))
    return out


def trial_uniform_L2(c, coefficients):
    """Full raw pair with both means, using its original orthonormal basis."""
    require(len(coefficients) == 8
            and all(x.lo.shape == (193, 96) for x in coefficients),
            'the complete original true-root septic for every column')
    terms = []
    for coefficient in coefficients:
        absolute = c.absolute(coefficient)
        squares = c.reduce_box(absolute*absolute, axis=0)
        terms.append(c.sqrt_upper(c.upper(squares)))
    return c.add_upper(*terms)


def signed_row_integral(c, row_coefficients, trial_coefficients, length):
    """Integrate all angular/radial products exactly, with directed arithmetic."""
    total = c.Box(c.np.zeros(96))
    for k, coefficient in enumerate(trial_coefficients):
        moment = c.Box(c.np.zeros((193, 1)))
        for j, row in enumerate(row_coefficients):
            if (j+k) % 2 == 0:
                moment = moment+row*c.box(length/F(j+k+1))
        total = total+c.reduce_box(moment*coefficient, axis=0)
    return c.finite(total)


class Integrator:
    def __init__(self, c, core, helper, phase_math, base_math,
                 base, offsets, definition, plan, jets, read_ball):
        self.c, self.core, self.helper = c, core, helper
        self.phase_math, self.base_math = phase_math, base_math
        self.base, self.offsets = base, offsets
        self.definition, self.plan, self.jets = definition, plan, jets
        self.read_ball = read_ball
        self.position, self.cursor, self.cells = 0, F(0), 0
        self.last_trial, self.trial_coefficients = None, None
        self.signed = c.Box(c.np.zeros(96))
        self.trial_L1 = c.Box(c.np.zeros(96))
        self.field_L1 = c.Box(c.np.zeros(96))
        self.sliver = c.Box(c.np.zeros(96))
        self.sliver_cells = 0
        self.max_row_degree = 0

    def trial(self, item, left, right):
        c, core = self.c, self.core
        piece = item['trial_piece']
        if piece != self.last_trial:
            tl, tr, length = self.helper.true_interval(c, self.definition, piece)
            self.true_left, self.true_length = tl, length
            self.trial_coefficients = core.hermite_coefficients(
                c, [c.Box(x[piece]) for x in self.jets],
                [c.Box(x[piece+1]) for x in self.jets], length)
            self.last_trial = piece
        return core.restrict_trial_coefficients(c, self.trial_coefficients,
                    self.true_left, self.true_length, left, right)

    def consume(self, phase_left, phase_right, polynomial, model, base_piece):
        c, core = self.c, self.core
        require(phase_left == self.cursor and phase_right <= STOP,
                'one complete chronological original phase step')
        phase = self.phase_math.exact_phase_derivative(c, core, polynomial)
        left = phase_left
        while left < phase_right:
            while F(self.plan[self.position]['interval'][1]) <= left:
                self.position += 1
            item = self.plan[self.position]
            pl, pr = map(F, item['interval'])
            require(item['side'] == 'negative' and pl <= left < pr,
                    'same original full negative TC certificate partition')
            right = min(pr, phase_right)
            cs = self.trial(item, left, right)
            H = trial_uniform_L2(c, cs)
            scalar = {name: scalar_model(c, core, model, name, left, right, self.read_ball)
                      for name in ('beta', 'K', 'gamma', 'q', 's')}
            u, v = self.base_math.base_background(c, core, self.base, self.offsets,
                                                  base_piece, left, right, scalar['s'])
            a = self.phase_math.restrict_phase(
                c, core, phase, phase_left, phase_right, left, right)
            W = a*a
            A, M = odd_part(c, core, W).primitive(), W.mean()
            ell1 = -4*scalar['beta']*u*A
            ell2 = -4*scalar['beta']*scalar['K']*v*A-2*scalar['gamma']*scalar['q']*M
            require(ell1.degree <= 160 and ell2.degree <= 160,
                    'the entire adjoint row precedes its justified finite pairing')
            row = complete_raw_row_coefficients(c, ell1, ell2)
            term = signed_row_integral(c, row, cs, right-left)
            uniform_error = c.add_upper(ell1.error, ell2.error)
            error = c.mul_upper(c.box(right-left), c.mul_upper(uniform_error, H))
            self.signed = self.signed+term+c.Box(-error.hi, error.hi)
            length_H = c.mul_upper(c.box(right-left), H)
            self.trial_L1 = c.add_upper(self.trial_L1, length_H)
            beta, K, gamma, q = (c.absolute(scalar[n].scalar_range()) for n in ('beta','K','gamma','q'))
            U, V = c.add_upper(u.norm, u.error), c.add_upper(v.norm, v.error)
            coefficient = c.add_upper(c.mul_upper(beta, c.add_upper(U, c.mul_upper(K, V))),
                                      c.mul_upper(gamma, q))
            self.field_L1 = c.add_upper(self.field_L1, c.mul_upper(coefficient, length_H))
            self.max_row_degree = max(self.max_row_degree, ell1.degree, ell2.degree)
            self.cells += 1
            left = right
        self.cursor = phase_right

    def root_sliver(self):
        c = self.c
        require(self.cursor == STOP, 'all3095 original phase polynomials precede the root sliver')
        left = STOP
        while left < ROOT_UPPER:
            while F(self.plan[self.position]['interval'][1]) <= left:
                self.position += 1
            item = self.plan[self.position]
            pl, pr = map(F, item['interval'])
            require(item['side'] == 'negative' and pl <= left < pr,
                    'the same true-root negative polynomial, including its certified extension')
            right = min(pr, ROOT_UPPER)
            H = trial_uniform_L2(c, self.trial(item, left, right))
            self.sliver = c.add_upper(self.sliver, c.mul_upper(c.box(54*(right-left)), H))
            self.sliver_cells += 1
            left = right
        return upper_balls(c, self.sliver)

    def prefix(self, record):
        def vector(values, bound):
            return {'complete_count': 96, 'bound': bound,
                    'balls': [record(x, bound)['ball'] for x in values]}
        return {'kind': 'P96_complete_new_phase_germ_prefix_v1',
                'exact_interval': ['0', str(self.cursor)],
                'complete_new_intersections': self.cells,
                'maximum_complete_row_degree': self.max_row_degree,
                'signed_original_trial_row96': vector(balls(self.c, self.signed), 'signed_enclosure'),
                'complete_trial_L1_L2_upper96': vector(upper_balls(self.c, self.trial_L1), 'upper'),
                'complete_field_L1_upper96': vector(upper_balls(self.c, self.field_L1), 'upper'),
                'all96_columns_and_all_old_scalar_remainders_retained': True,
                'all_eight_exact_radial_moments_retained': True}


def finish(c, integrator, publish):
    require(integrator.cursor == STOP, 'the entire original169 phase interval')
    trial = publish(OUTPUT_ORDER[0], balls(c, integrator.signed), 'signed96')
    H = publish(OUTPUT_ORDER[1], upper_balls(c, integrator.trial_L1), 'upper96')
    F0 = publish(OUTPUT_ORDER[2], upper_balls(c, integrator.field_L1), 'upper96')
    tail = publish(OUTPUT_ORDER[3], integrator.root_sliver(), 'upper96')
    weight_error, amplitude, difference = map(c.exact, [F('3.521e-5'), F(11,10), F('1.535e-6')])
    errors = [(2*weight_error*f+2*amplitude*amplitude*difference*h+t).upper()
              for h, f, t in zip(H, F0, tail)]
    true = [x+c.arb(0,e) for x,e in zip(trial, errors)]
    restored = publish(OUTPUT_ORDER[4], true, 'signed96_with_centres')
    require(len(restored) == 96, 'all96 entire true signed balls read back')
    radius2 = c.arb(0)
    for value in restored:
        centre = c.arb(float(value.mid()))
        radius = max(abs((value-centre).lower()), abs((value-centre).upper()))
        radius2 += radius*radius
    publish(OUTPUT_ORDER[5], radius2.sqrt().upper(), 'upper')
