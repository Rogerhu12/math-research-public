"""BFP full forward B-normalized strict-nu column and whole Theta consumer.

All functions are pure. Public Actions owns actual parent admission,
exact carrier restoration, trial selection and complete save/read steps.
No old norm/residual/cohomology/CYA-gap/BNC-pairing producer is called.
"""
from fractions import Fraction

ROWS, TRIAL_MODES, W_MODES = 96, 512, 2048
IMAGE_MODES, SOURCE_MODES, GRID, THETA_MODES = 2560, 96, 8192, 2240
TARGETS = [
    "complete_forward_nu_w_trial_Wiener_upper",
    "complete_forward_nu_true_B_inverse_L2_upper",
    "complete_forward_nu_trial_L2_upper",
    "complete_forward_nu_primitive_L2_upper",
    "complete_forward_nu_positive_primitive_Wiener_upper",
    "complete_forward_nu_pullback_quadrature_square_upper",
    "complete_forward_nu_pullback_alias_square_upper",
    "complete_forward_nu_finite_B_residual_L2_upper",
    "complete_forward_nu_w_Linf_product_upper",
    "complete_forward_nu_w_L2_product_upper",
    "complete_forward_nu_H_minus_G_density_L2_upper",
    "complete_forward_nu_true_PDE_density_error_upper",
    "complete_forward_nu_true_B_residual_L2_upper",
    "complete_forward_nu_true_target_column_L2_error_upper",
    "complete_forward_nu_finite_model_preimage_L2_upper",
    "complete_original_Theta_trial_Frobenius_upper",
    "complete_forward_nu_Theta_pairing_rounding_upper",
    "complete_forward_nu_true_Theta_column_error_upper",
    "complete_signed_forward_nu_true_Theta_column",
]


def require(ok, message):
    if not ok:
        raise ValueError(message)


def upper(value):
    require(value.is_finite() and value.lower() >= 0,
            "one complete finite nonnegative saved upper")
    return value.upper()


def pairs(whole_pairs, length):
    require(len(whole_pairs) == length and all(len(value) == 2 for value in whole_pairs),
            "every complete positive coefficient and both exact rational components")
    return [tuple(Fraction(component) for component in value) for value in whole_pairs]


def complex_values(api, whole_pairs, length):
    return [api.acb(api.rational(a), api.rational(b)) for a, b in pairs(whole_pairs, length)]


def complete_exact_forward_image(whole_original_w_pairs, whole_new_trial_pairs):
    """BFP.8: every signed output1..2560; forward PLUS, not Bdagger."""
    w = pairs(whole_original_w_pairs, W_MODES)
    z = pairs(whole_new_trial_pairs, TRIAL_MODES)
    result = []
    for n in range(1, IMAGE_MODES+1):
        real, imag = z[n-1] if n <= TRIAL_MODES else (Fraction(0), Fraction(0))
        for ell, (a, b) in enumerate(z, 1):
            k = n-ell
            if k == 0 or abs(k) > W_MODES:
                continue
            u, v = w[abs(k)-1]
            if k < 0:
                v = -v
            real += (u*b+v*a)/(4*ell)
            imag += (v*b-u*a)/(4*ell)
        result.append([str(real), str(imag)])
    require(len(result) == IMAGE_MODES, "the whole real finite forward image")
    return result


def complete_new_w_Wiener(api, whole_original_w_pairs):
    values = complex_values(api, whole_original_w_pairs, W_MODES)
    return (2*sum((abs(value).upper() for value in values), api.zero)).upper()


def complete_true_B_inverse_L2(saved_new_w_Wiener, saved_whole_w_Linf_error):
    """The SAME WBP.9 full-space inverse, not a new finite inverse."""
    return (1+(upper(saved_new_w_Wiener)+upper(saved_whole_w_Linf_error))/4).upper()


def complete_new_trial_norms(api, whole_new_trial_pairs):
    values = complex_values(api, whole_new_trial_pairs, TRIAL_MODES)
    x2, i2, iw = api.zero, api.zero, api.zero
    for n, value in enumerate(values, 1):
        a = abs(value).upper()
        x2 = x2+2*a*a
        b = a/(4*n)
        i2 = i2+2*b*b
        iw = iw+b
    return {TARGETS[2]: x2.sqrt().upper(),
            TARGETS[3]: i2.sqrt().upper(), TARGETS[4]: iw.upper()}


class CompletePullbackPolynomial:
    """New full r(G) polynomial values with exact unit-circle disk control.

    Whole point tuples are (full f ball, same original G ball, complete
    analytic chain Gprime ball). All8192 are saved/read before construction.
    The owner appends every exact forward coefficient in natural1..2560
    order and saves the full resulting scalar point records before norm use.
    """
    def __init__(self, api, whole_point_triples):
        require(len(whole_point_triples) == GRID, "all8192 full source/G/Gprime inputs")
        self.api, self.next_n = api, 1
        self.f, self.gprime, self.steps, self.tau = [], [], [], []
        for point in whole_point_triples:
            require(len(point) == 3 and all(x.is_finite() for x in point)
                    and point[2].lower() > 0, "every full value and positive whole Jacobian")
            f, g, gp = point
            step = api.acb((4*g).cos(), (4*g).sin())
            center = api.midpoint_complex(step)
            require(center.real.is_exact() and center.imag.is_exact(), "one exact dyadic phase center")
            self.f.append(f)
            self.gprime.append(gp)
            self.steps.append(center)
            self.tau.append(abs(step-center).upper())
        self.centers = [api.acb(1) for _ in range(GRID)]
        self.radii = [api.zero for _ in range(GRID)]
        self.values = [api.zero for _ in range(GRID)]
        self.polynomial_radii = [api.zero for _ in range(GRID)]

    def append(self, mode, complete_exact_coefficient_pair):
        require(mode == self.next_n and 1 <= mode <= IMAGE_MODES,
                "every new finite forward mode1..2560 in natural order")
        api = self.api
        a, b = pairs([complete_exact_coefficient_pair], 1)[0]
        coefficient = api.acb(api.rational(a), api.rational(b))
        magnitude = abs(coefficient).upper()
        for j in range(GRID):
            product = self.centers[j]*self.steps[j]
            center = api.midpoint_complex(product)
            require(center.real.is_exact() and center.imag.is_exact(),
                    "one exact dyadic power center")
            old = upper(self.radii[j])
            radius = (old+(1+old)*upper(self.tau[j])+abs(product-center).upper()).upper()
            self.centers[j], self.radii[j] = center, radius
            self.values[j] = self.values[j]+2*(coefficient*center).real
            self.polynomial_radii[j] = (
                self.polynomial_radii[j]+2*magnitude*radius).upper()
        self.next_n += 1

    def whole_point_integrands(self):
        """Return every complete nonnegative-real integrand ball, no reduction."""
        require(self.next_n == IMAGE_MODES+1, "all2560 finite image modes completed")
        api, result = self.api, []
        for j in range(GRID):
            value = self.values[j]+api.arb(0, upper(self.polynomial_radii[j]))
            residual = value*self.gprime[j]-self.f[j]
            integrand = residual*residual/self.gprime[j]
            require(integrand.is_finite() and integrand.upper() >= 0,
                    "one full pullback square divided by the true positive Gprime")
            result.append(integrand)
        return result


def complete_pullback_square_upper(api, whole_saved_point_integrands):
    require(len(whole_saved_point_integrands) == GRID
            and all(x.is_finite() and x.upper() >= 0 for x in whole_saved_point_integrands),
            "all8192 complete saved/read point integrands")
    return (sum((x.upper() for x in whole_saved_point_integrands), api.zero)/GRID).upper()


def complete_analytic_alias_square(api, whole_saved_image_pairs,
                                    whole_f_positive_coefficients,
                                    saved_G0, saved_G1):
    """BFP.11--13: every finite coefficient, full nonlinear Fourier tail."""
    image = complex_values(api, whole_saved_image_pairs, IMAGE_MODES)
    require(len(whole_f_positive_coefficients) == SOURCE_MODES
            and all(x.is_finite() for x in whole_f_positive_coefficients),
            "all96 whole physical source coefficients")
    G0, G1, sigma = upper(saved_G0), upper(saved_G1), api.rational(1, 128)
    require(G1 < 2 and G1 >= 1, "the full original Wiener derivative and exact mean1")
    Ar, Af = api.zero, api.zero
    for n, value in enumerate(image, 1):
        Ar = Ar+2*abs(value).upper()*(4*n*(sigma+G0)).exp()
    for n, value in enumerate(whole_f_positive_coefficients, 1):
        Af = Af+2*abs(value).upper()*(4*n*sigma).exp()
    Ar, Af = Ar.upper(), Af.upper()
    total = ((-4*GRID*sigma).exp()*(G1*Ar+Af)**2/(2-G1)).upper()
    return {"whole_image_weighted_Wiener_upper": Ar,
            "whole_source_weighted_Wiener_upper": Af,
            TARGETS[6]: total}


def complete_finite_forward_residual(saved_square, saved_alias_square):
    return (upper(saved_square)+upper(saved_alias_square)).sqrt().upper()


def complete_whole_w_products(api, saved_w_Linf_error, saved_w_L2_error,
                               saved_trial_primitive_L2, saved_trial_positive_primitive_Wiener):
    return {
        TARGETS[8]: (upper(saved_w_Linf_error)*upper(saved_trial_primitive_L2)).upper(),
        TARGETS[9]: (api.rational(2).sqrt()*upper(saved_w_L2_error)
                    *upper(saved_trial_positive_primitive_Wiener)).upper(),
    }


def choose_whole_w_product(saved_Linf_product, saved_L2_product):
    candidates = {TARGETS[8]: upper(saved_Linf_product), TARGETS[9]: upper(saved_L2_product)}
    selected = min(candidates, key=candidates.__getitem__)
    return selected, candidates[selected]


def complete_whole_flow_density_error(api, saved_EH, saved_N0,
                                       saved_G1, saved_H1, saved_homotopy_lower):
    """BFP.6, physical f degree96; all Jacobian and second-lift terms kept."""
    EH, N0, G1, H1 = map(upper, (saved_EH, saved_N0, saved_G1, saved_H1))
    require(saved_homotopy_lower.is_finite() and saved_homotopy_lower.lower() > 0
            and G1 >= 1 and H1 >= 1,
            "the complete original homotopy lower and derivative means1")
    m, sigma = saved_homotopy_lower.lower(), api.rational(1, 128)
    B2 = ((max(G1, H1)-1)/sigma).upper()
    N1 = 4*SOURCE_MODES*N0
    return (EH*(N1+N0/sigma+B2*N0/m)/(m*m.sqrt())).upper()


def complete_true_PDE_density_error(api, saved_BH, saved_short_waist_error):
    return (upper(saved_BH)*upper(saved_short_waist_error)/api.rational(2).sqrt()).upper()


def complete_true_forward_residual(saved_finite_residual, saved_w_product,
                                    saved_flow_error, saved_PDE_error):
    return sum(map(upper, (saved_finite_residual, saved_w_product,
                           saved_flow_error, saved_PDE_error))).upper()


def complete_true_target_column_error(saved_B_inverse_L2, saved_full_B_residual):
    return (upper(saved_B_inverse_L2)*upper(saved_full_B_residual)).upper()


def complete_projected_target_coordinates(api, whole_new_trial_pairs, whole_true_a):
    require(whole_true_a.is_finite(), "the complete original true a=2H(0), never its center")
    values = complex_values(api, whole_new_trial_pairs, TRIAL_MODES)
    root2, result = api.rational(2).sqrt(), []
    for n, value in enumerate(values, 1):
        phase = 2*n*whole_true_a
        result.append(root2*(value.real*phase.cos()-value.imag*phase.sin()))
    return result


def complete_finite_model_preimage(api, whole_saved_target_coordinates,
                                    whole_original_model_multipliers):
    require(len(whole_saved_target_coordinates) == TRIAL_MODES
            and len(whole_original_model_multipliers) == THETA_MODES
            and all(x.is_finite() for x in whole_saved_target_coordinates)
            and all(x.is_finite() for x in whole_original_model_multipliers)
            and all(x == 1 for x in whole_original_model_multipliers[:ROWS]),
            "all512 new coordinates and the entire original2240 model with its exact low96 reference")
    total = api.zero
    for n, beta in enumerate(whole_saved_target_coordinates):
        value = beta*whole_original_model_multipliers[n]
        total = total+abs(value).upper()**2
    return total.sqrt().upper()


def admit_entire_Theta_trial(whole_original_trial):
    require(len(whole_original_trial) == ROWS
            and all(len(row) == THETA_MODES for row in whole_original_trial)
            and all(value.is_finite() and value.is_exact()
                    for row in whole_original_trial for value in row),
            "the entire same original96x2240 exact dyadic Theta carrier after its original SHA")


def complete_original_Theta_trial_Frobenius(api, whole_original_trial):
    """A NEW norm of the complete Theta carrier, not a GY/IR/OT old target."""
    admit_entire_Theta_trial(whole_original_trial)
    total = api.zero
    for row in whole_original_trial:
        for value in row:
            total = total+value*value
    return total.sqrt().upper()


def complete_true_phase_Theta_pairings(api, whole_original_trial,
                                       whole_saved_target_coordinates):
    admit_entire_Theta_trial(whole_original_trial)
    require(len(whole_saved_target_coordinates) == TRIAL_MODES
            and all(x.is_finite() for x in whole_saved_target_coordinates),
            "every projected coordinate with its full true phase ball")
    return [sum((row[n]*whole_saved_target_coordinates[n] for n in range(TRIAL_MODES)), api.zero)
            for row in whole_original_trial]


def complete_pairing_centers_and_joint_radius(api, whole_saved_signed_pairings):
    require(len(whole_saved_signed_pairings) == ROWS
            and all(x.is_finite() for x in whole_saved_signed_pairings),
            "all96 whole signed values saved/read before radii")
    centers, square = [], api.zero
    for value in whole_saved_signed_pairings:
        center = value.mid()
        require(center.is_exact(), "one exact dyadic signed center")
        radius = abs(value-center).upper()
        centers.append(center)
        square = square+radius*radius
    return centers, square.sqrt().upper()


def complete_true_Theta_column_error(saved_Theta_trial_norm, saved_global_Theta_error,
                                      saved_true_target_column_error, saved_VQ_L2_error,
                                      saved_model_preimage, saved_model_rounding_error,
                                      saved_new_trial_L2, saved_pairing_rounding):
    BTheta = upper(saved_Theta_trial_norm)+upper(saved_global_Theta_error)
    return (BTheta*upper(saved_true_target_column_error)
            +upper(saved_VQ_L2_error)*upper(saved_model_preimage)
            +upper(saved_model_rounding_error)*upper(saved_new_trial_L2)
            +upper(saved_pairing_rounding)).upper()
