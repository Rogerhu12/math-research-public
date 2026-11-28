"""One full particular density receiver, in the original C/A/model order.

This is a new signed C-dagger action and complete opposite-sign leakage,
not an evaluation of the old IR96 residuals or old Theta row products.
The owner must admit successful whole BFP/UACT receipts and restore the
unchanged private carriers before calling any numerical function here.
"""
from fractions import Fraction

ROWS, INPUT_MODES, ALPHA_MODES, MODES = 96, 512, 2048, 2560
GRID, LEAK_HEAD, MODEL_MODES = 8192, 2048, 2240
TARGETS = [
    "complete_particular_p_hat_complex_derivative_perturbation_upper",
    "complete_particular_v_L2_upper",
    "complete_particular_v_D1_L2_upper",
    "complete_particular_v_positive_primitive_Wiener_upper",
    "complete_particular_v_lower_strip_primitive_upper",
    "complete_particular_model_primitive_L2_upper",
    "complete_particular_model_positive_primitive_Wiener_upper",
    "complete_particular_alpha_Linf_source_product_upper",
    "complete_particular_alpha_L2_source_product_upper",
    "complete_particular_opposite_leakage_head_energy_upper",
    "complete_particular_opposite_leakage_infinite_tail_energy_upper",
    "complete_particular_true_p_map_energy_error_upper",
    "complete_particular_full_true_opposite_leakage_energy_upper",
    "complete_particular_source_Theta_pairing_joint_radius_upper",
    "complete_particular_finite_Theta_joint_error_upper",
    "complete_signed_particular_finite_Theta_column",
    "complete_particular_true_Theta_nu_joint_error_upper",
    "complete_signed_particular_true_Theta_nu_column",
]


def require(ok, message):
    if not ok:
        raise ValueError(message)


def up(value):
    require(value.is_finite() and value.upper() >= 0, "one entire finite nonnegative upper")
    return value.upper()


def complete_p_hat_strip(api, terminal_side, K_sines, K_cosines):
    """Entire original 129+48+48 coefficients, including the real mean.

    A real derivative lower on an entire complex strip proves that both
    lifts send its upper half into the upper half. No sampled imaginary
    positivity, real-axis derivative bound, or missing constant is used.
    """
    require(len(terminal_side) == 129 and len(K_sines) == len(K_cosines) == 48
            and Fraction(terminal_side[64][1]) == 0,
            "the complete original terminal side, real mean and postcomposition")
    sigma = api.rational(1, 256)
    a1 = api.zero
    for n, (a, b) in enumerate(terminal_side[65:], 1):
        value = api.acb(api.rational(Fraction(a)), api.rational(Fraction(b)))
        a1 += 8*n*abs(value).upper()*(4*n*sigma).exp()
    a1 = up(a1)
    image_width = up(sigma*(1+a1))
    k1 = api.zero
    for n, (s, c) in enumerate(zip(K_sines, K_cosines), 1):
        value = api.acb(api.rational(Fraction(c)), -api.rational(Fraction(s)))
        k1 += 4*n*abs(value).upper()*(4*n*image_width).exp()
    k1 = up(k1)
    eta = up(a1+(1+a1)*k1)
    require(eta < 1, "the complete original finite compound preserves the upper half-strip")
    return {"terminal_derivative_perturbation": a1, "terminal_image_width": image_width,
            "post_derivative_perturbation": k1, "compound_derivative_perturbation": eta,
            "compound_image_width": up(sigma*(1+eta))}


def complete_model_source(api, whole_target_coordinates, whole_model_multipliers, whole_source_phase):
    require(len(whole_target_coordinates) == INPUT_MODES
            and len(whole_model_multipliers) == MODEL_MODES
            and whole_source_phase.is_finite()
            and all(x.is_finite() for x in whole_target_coordinates+whole_model_multipliers),
            "all512 actual target coordinates and the original whole2240 model carrier")
    root2, result = api.rational(2).sqrt(), []
    for n, (beta, gamma) in enumerate(zip(whole_target_coordinates, whole_model_multipliers), 1):
        phase = 2*n*whole_source_phase+api.arb.pi()/4
        result.append(beta*gamma*api.acb(phase.cos(), -phase.sin())/root2)
    require(len(result) == INPUT_MODES, "the complete finite source Gbar Xhat in the true b basis")
    return result


def complete_v_coefficients(api, whole_model_source, whole_alpha_exact_pairs):
    """vhat=(Id-T_alphahat I)Gbar Xhat, all2560 outputs, minus sign.

    The positive output contains only positive input indices. Inserting
    negative inputs would change the original same-sign normalizer.
    """
    require(len(whole_model_source) == INPUT_MODES and len(whole_alpha_exact_pairs) == ALPHA_MODES,
            "all original positive coefficients, no high modes silently dropped")
    alpha = [api.acb(api.rational(Fraction(a)), api.rational(Fraction(b)))
             for a, b in whole_alpha_exact_pairs]
    result = []
    for n in range(1, MODES+1):
        value = whole_model_source[n-1] if n <= INPUT_MODES else api.acb(0)
        for ell, coefficient in enumerate(whole_model_source, 1):
            difference = n-ell
            if difference == 0 or abs(difference) > ALPHA_MODES:
                continue
            a = alpha[abs(difference)-1]
            if difference < 0:
                a = api.acb(a.real, -a.imag)
            value -= a*coefficient/api.acb(0, 4*ell)
        require(value.is_finite(), "one whole finite same-sign source coefficient")
        result.append(value)
    return result


def complete_source_norms(api, whole_v, saved_compound_derivative_perturbation):
    require(len(whole_v) == MODES and all(v.is_finite() for v in whole_v),
            "every one of the2560 source coefficients")
    eta = up(saved_compound_derivative_perturbation)
    require(eta < 1, "the complete upper-half-strip certificate")
    width = api.rational(1, 256)*(1+eta)
    n0, n1, wp, lower = api.zero, api.zero, api.zero, api.zero
    for n, coefficient in enumerate(whole_v, 1):
        a = abs(coefficient).upper()
        n0 += 2*a*a
        n1 += 2*(4*n)**2*a*a
        wp += a/(4*n)
        lower += a*(4*n*width).exp()/(4*n)
    return {TARGETS[1]: n0.sqrt().upper(), TARGETS[2]: n1.sqrt().upper(),
            TARGETS[3]: wp.upper(), TARGETS[4]: lower.upper()}


def complete_model_primitive_norms(api, whole_source):
    require(len(whole_source) == INPUT_MODES and all(v.is_finite() for v in whole_source),
            "all512 finite source modes with their true phase and multiplier")
    l2, wp = api.zero, api.zero
    for n, coefficient in enumerate(whole_source, 1):
        a = abs(coefficient).upper()/(4*n)
        l2 += 2*a*a
        wp += a
    return {TARGETS[5]: l2.sqrt().upper(), TARGETS[6]: wp.upper()}


def complete_alpha_source_products(api, original_IR_H, original_IR_L2,
                                    whole_original_inverse_Linf_product,
                                    whole_original_inverse_L2_product,
                                    saved_model_primitive_L2,
                                    saved_model_positive_primitive_W):
    """Use known positive coefficients of the old complete UACT products.

    This compares the saved-bound weights H/2>.07 and S/3>1/5. It
    does not infer a lower bound on the unknown original inverse error.
    """
    H, e0 = up(original_IR_H), up(original_IR_L2)
    require(H > api.rational(14, 100) and e0 > api.rational(435, 1000),
            "the same two entire original saved-bound coefficients")
    S = api.rational(51, 50)*(e0+api.rational(10, 9)*H)
    require(S > api.rational(3, 5), "the fixed positive UACT product weight")
    return {
        TARGETS[7]: (api.rational(100, 7)*up(whole_original_inverse_Linf_product)
                     *up(saved_model_primitive_L2)).upper(),
        TARGETS[8]: (5*api.rational(2).sqrt()*up(whole_original_inverse_L2_product)
                     *up(saved_model_positive_primitive_W)).upper(),
    }


def complete_new_grid(api, whole_original_IR_grid, terminal_side, K_sines, K_cosines):
    require(len(whole_original_IR_grid) == 4096 and len(terminal_side) == 129
            and len(K_sines) == len(K_cosines) == 48 and Fraction(terminal_side[64][1]) == 0,
            "every original node, coefficient and true terminal mean")
    terminal = [api.acb(api.rational(Fraction(a)), api.rational(Fraction(b)))
                for a, b in terminal_side[65:]]
    post = [api.acb(api.rational(Fraction(c)), -api.rational(Fraction(s)))
            for s, c in zip(K_sines, K_cosines)]
    mean = api.rational(Fraction(terminal_side[64][0]))

    def horner(q, coefficients):
        value = api.acb(0)
        for coefficient in reversed(coefficients):
            value = q*(coefficient+value)
        return value

    grid = []
    for j in range(GRID):
        if j % 2 == 0:
            value = whole_original_IR_grid[j//2]
        else:
            x = api.arb.pi()*j/(2*GRID)
            q = api.acb((4*x).cos(), (4*x).sin())
            a = x+mean+2*horner(q, terminal).real
            qa = api.acb((4*a).cos(), (4*a).sin())
            value = a+horner(qa, post).real
        require(value.is_finite(), "one full finite compound value")
        grid.append(value)
    return grid


class CompletePrimitiveSamples:
    """New single-column action with complete unit-disk phase residuals."""
    def __init__(self, api, whole_grid):
        require(len(whole_grid) == GRID and all(v.is_finite() for v in whole_grid),
                "all8192 saved/read original-compound inputs")
        self.api, self.next_n = api, 1
        self.steps, self.tau = [], []
        for value in whole_grid:
            exact_phase = api.acb((4*value).cos(), (4*value).sin())
            center = api.midpoint_complex(exact_phase)
            require(center.real.is_exact() and center.imag.is_exact(), "an exact dyadic phase center")
            self.steps.append(center)
            self.tau.append(abs(exact_phase-center).upper())
        self.powers = [api.acb(1) for _ in range(GRID)]
        self.radii = [api.zero for _ in range(GRID)]
        self.values = [api.acb(0) for _ in range(GRID)]
        self.value_radii = [api.zero for _ in range(GRID)]

    def append(self, mode, whole_coefficient):
        require(mode == self.next_n and 1 <= mode <= MODES and whole_coefficient.is_finite(),
                "every full signed source coefficient1..2560 in natural order")
        api = self.api
        coefficient = whole_coefficient/api.acb(0, 4*mode)
        magnitude = abs(coefficient).upper()
        for j in range(GRID):
            product = self.powers[j]*self.steps[j]
            center = api.midpoint_complex(product)
            require(center.real.is_exact() and center.imag.is_exact(), "one exact power center")
            old = up(self.radii[j])
            radius = (old+(1+old)*up(self.tau[j])+abs(product-center).upper()).upper()
            self.powers[j], self.radii[j] = center, radius
            self.values[j] += coefficient*center
            self.value_radii[j] = (self.value_radii[j]+magnitude*radius).upper()
        self.next_n += 1

    def complete(self):
        require(self.next_n == MODES+1, "the entire2560-mode new source action")
        api = self.api
        return [api.acb(value.real+api.arb(0, radius), value.imag+api.arb(0, radius))
                for value, radius in zip(self.values, self.value_radii)]


def complete_fft(api, whole_samples):
    require(len(whole_samples) == GRID and all(v.is_finite() for v in whole_samples),
            "all8192 complete new primitive samples saved/read")
    bits, permutation = GRID.bit_length()-1, []
    for j in range(GRID):
        source, target = j, 0
        for unused in range(bits):
            target, source = (target << 1) | (source & 1), source >> 1
        permutation.append(target)
    work = [api.acb(whole_samples[j]) for j in permutation]
    width = 2
    while width <= GRID:
        angle = 2*api.arb.pi()/width
        step, power, roots = api.acb(angle.cos(), -angle.sin()), api.acb(1), []
        for unused in range(width//2):
            roots.append(power)
            power *= step
        for start in range(0, GRID, width):
            for k, root in enumerate(roots):
                left, right = work[start+k], root*work[start+k+width//2]
                work[start+k], work[start+k+width//2] = left+right, left-right
        width *= 2
    return work


def complete_signed_heads(api, whole_transform, saved_upper_half_primitive, saved_lower_half_primitive):
    require(len(whole_transform) == GRID and all(v.is_finite() for v in whole_transform),
            "the entire new directed transform")
    plus, minus = up(saved_upper_half_primitive), up(saved_lower_half_primitive)
    sigma = api.rational(1, 256)
    qN = (-4*GRID*sigma).exp()

    def coefficient(k):
        # Positive Fourier coefficients use the lower analytic half-strip;
        # negative coefficients use the upper half-strip. Both alias rays
        # are retained, including positive aliases of a negative frequency.
        alias = (minus*(-4*(GRID+k)*sigma).exp()
                 +plus*(-4*(GRID-k)*sigma).exp())/(1-qN)
        alias = alias.upper()
        value = whole_transform[k % GRID]/GRID
        enclosure = api.acb(value.real+api.arb(0, alias), value.imag+api.arb(0, alias))
        return api.acb(0, 4*k)*enclosure

    positive = [coefficient(k) for k in range(1, ROWS+1)]
    opposite = [coefficient(-k) for k in range(1, LEAK_HEAD+1)]
    return positive, opposite


def complete_leakage_head(api, whole_opposite_head):
    require(len(whole_opposite_head) == LEAK_HEAD and all(v.is_finite() for v in whole_opposite_head),
            "all2048 opposite-sign density coefficients saved/read")
    square = sum((2*abs(value).upper()**2/(4*k)
                  for k, value in enumerate(whole_opposite_head, 1)), api.zero)
    return square.sqrt().upper()


def complete_leakage_tail(api, saved_upper_half_primitive):
    q = (-8*api.rational(1, 256)).exp().upper()
    require(q > 0 and q < 1, "one complete infinite opposite-sign geometric series")
    start = LEAK_HEAD+1
    first_moment = q**start*(start/(1-q)+q/(1-q)**2)
    return (up(saved_upper_half_primitive)*(8*first_moment).sqrt()).upper()


def complete_true_map_energy_error(api, whole_Ep, saved_v_L2, saved_v_D1):
    # Both true p and finite phat, and the real homotopy, have these SAME
    # actual derivative bounds. The sign blocks are orthogonal.
    m, M = api.rational(9749, 10000), api.rational(10251, 10000)
    sigma = api.rational(1, 256)
    return (up(whole_Ep)*(up(saved_v_L2)/sigma+M*up(saved_v_D1))/(2*m.sqrt())).upper()


def complete_true_leakage(saved_head, saved_tail, saved_true_map_error):
    return ((up(saved_head)**2+up(saved_tail)**2).sqrt()+up(saved_true_map_error)).upper()


def complete_readout_centers(api, whole_positive_head):
    require(len(whole_positive_head) == ROWS and all(v.is_finite() for v in whole_positive_head),
            "all96 complete true-root readout coefficients")
    # Dplus^-1 multiplies the positive coefficient by exp(+i pi/4).
    # Pairing with sqrt2 cos(4jx) is exactly Re((1+i)*coefficient).
    balls = [value.real-value.imag for value in whole_positive_head]
    centers = [api.midpoint_real(value) for value in balls]
    require(all(value.is_exact() for value in centers), "all exact signed dyadic centers")
    radius = sum((abs(value-center).upper()**2 for value, center in zip(balls, centers)), api.zero).sqrt().upper()
    return balls, centers, radius


def complete_finite_Theta_error(api, saved_true_leakage, saved_map_error,
                                saved_whole_alpha_product, saved_pair_radius):
    return ((api.rational(384).sqrt()
             *(api.rational(4, 25)*up(saved_true_leakage)+up(saved_map_error)
               +up(saved_whole_alpha_product)/2))+up(saved_pair_radius)).upper()


def complete_full_true_nu_error(saved_finite_Theta_error, original_Theta_trial_norm,
                                whole_global_Theta_error, whole_BFP_target_error):
    return (up(saved_finite_Theta_error)
            +(up(original_Theta_trial_norm)+up(whole_global_Theta_error))*up(whole_BFP_target_error)).upper()
