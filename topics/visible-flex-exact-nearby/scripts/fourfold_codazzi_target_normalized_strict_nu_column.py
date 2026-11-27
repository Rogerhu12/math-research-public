"""BNC: first complete B-normalized strict-parameter96 signed column.

Pure formulas only. The actual owner supplies whole NP/PO/ASB/JC and
successful DWTB records, plus exact original row and NP carriers. No old
norm, residual, cohomology, observation inverse or pairing is called.
"""
from fractions import Fraction

ROWS, MODES, SOURCE_MODES, GRID = 96, 192, 96, 8192
COMPONENT_ORDER = [
    "complete_target_B_row_error_on_NP_trial_upper",
    "complete_target_B_receiver_on_NP_PDE_error_upper",
    "complete_target_B_trial_compound_error_upper",
    "complete_target_B_trial_quadrature_alias_upper",
    "complete_target_B_trial_quadrature_rounding_upper",
]
TARGETS = COMPONENT_ORDER+[
    "complete_target_normalized_strict_nu_column_error_upper",
    "complete_signed_target_normalized_strict_nu_column",
]


def require(ok, message):
    if not ok:
        raise ValueError(message)


def up(value):
    require(value.is_finite() and value.lower() >= 0,
            "one whole finite nonnegative directed upper")
    return value.upper()


def physical_positive_coefficients(api, whole_waist193, complete_q, complete_ng):
    """BNC.4: all96 real positive Fourier coefficients; zero mean is exact.

    The193-vector is the original normalized sqrt2 sine/mean/cosine basis.
    The denominator balls enclose the implicit selected physical member.
    """
    require(len(whole_waist193) == 193
            and all(value.is_finite() for value in whole_waist193)
            and complete_q.is_finite() and complete_q.lower() > 0
            and complete_ng.is_finite() and complete_ng.lower() > 0,
            "all original waist coordinates and full positive selected scalars")
    root_q = complete_q.sqrt()
    return [-complete_ng*whole_waist193[n-1]/(8*n*root_q)
            for n in range(1, SOURCE_MODES+1)]


class CompletePhysicalQuadrature:
    """All8192 new inputs followed by each of the192 new complete modes.

    Every exact center/radius must be saved and read by the Actions owner
    before it becomes the input to the next stage. The exact unit-circle
    recurrence, rather than a growing rectangular power ball, pays phase
    and arithmetic uncertainty. No old alpha quadrature target is called.
    """
    def __init__(self, api, whole_physical_grid):
        require(len(whole_physical_grid) == GRID,
                "all8192 full physical polynomial/G input pairs")
        self.api, self.next_n = api, 1
        self.u, self.s, self.tau = [], [], []
        whole_raw_radius = api.zero
        for raw, phase in whole_physical_grid:
            require(raw.is_finite() and phase.is_finite(),
                    "every whole original physical grid ball")
            u = api.midpoint_real(raw)
            value = api.acb((4*phase).cos(), -(4*phase).sin())
            s = api.midpoint_complex(value)
            require(u.is_exact() and s.real.is_exact() and s.imag.is_exact(),
                    "all new point centers are exact dyadics")
            self.u.append(u)
            self.s.append(s)
            self.tau.append(abs(value-s).upper())
            whole_raw_radius = whole_raw_radius+abs(raw-u).upper()
        self.raw_radius = (whole_raw_radius/GRID).upper()
        self.centers = [api.acb(1) for _ in range(GRID)]
        self.radii = [api.zero for _ in range(GRID)]

    def next(self):
        api = self.api
        require(1 <= self.next_n <= MODES, "the full natural192-mode order")
        total, radius = api.acb(0), api.zero
        for index in range(GRID):
            product = self.centers[index]*self.s[index]
            center = api.midpoint_complex(product)
            require(center.real.is_exact() and center.imag.is_exact(),
                    "one exact dyadic power center")
            old = up(self.radii[index])
            rho = (old+(1+old)*up(self.tau[index])
                   +abs(product-center).upper()).upper()
            self.centers[index], self.radii[index] = center, rho
            total = total+self.u[index]*center
            radius = radius+abs(self.u[index]).upper()*rho
        total = total/GRID
        center = api.midpoint_complex(total)
        radius = (self.raw_radius+radius/GRID+abs(total-center).upper()).upper()
        require(center.real.is_exact() and center.imag.is_exact()
                and center.is_finite() and radius.is_finite(),
                "one entire new observation disk with all rounding")
        result = {"mode": self.next_n, "complete_grid_points": GRID,
                  "center": center, "radius": radius}
        self.next_n += 1
        return result


def complete_exact_signed_pairings(whole_row_pairs, whole_observation_pairs):
    """BNC.10, exact rationals for all96 rows and all192 positive modes.

    Inputs are the full saved rational real/imaginary pairs. Both negative
    Fourier signs are supplied by the exact real-conjugacy identity.
    This is a new Actions target, never an old finite observation rerun.
    """
    require(len(whole_row_pairs) == ROWS
            and all(len(row) == MODES for row in whole_row_pairs)
            and len(whole_observation_pairs) == MODES,
            "every complete original row and every complete new observation")
    observations = []
    for pair in whole_observation_pairs:
        require(len(pair) == 2, "one whole exact complex observation")
        observations.append(tuple(Fraction(x) for x in pair))
    result = []
    for row in whole_row_pairs:
        total = Fraction(0)
        for pair, (x, y) in zip(row, observations):
            require(len(pair) == 2, "one whole original exact complex row coefficient")
            a, b = map(Fraction, pair)
            total += 2*(a*x+b*y)
        result.append(str(total))
    require(len(result) == ROWS, "the complete new signed96 column")
    return result


def complete_component_errors(api, *, saved_joint_B_row_error,
                              saved_trial_row_HS, saved_physical_N0,
                              saved_short_waist_density_error,
                              saved_BH, saved_EH, saved_G0,
                              saved_interpolation_lower,
                              whole_saved_observation_disks):
    """BNC.14: full row/PDE/composition/alias/rounding fees, independently.

    J is the already completed DWTB IY Hilbert-Schmidt norm, which equals
    the entire L2 norm of G_abs Y. No norm reducer for J or N0 is rerun.
    """
    eR, J, N0, D, BH, EH, G0 = map(up, (saved_joint_B_row_error,
        saved_trial_row_HS, saved_physical_N0, saved_short_waist_density_error,
        saved_BH, saved_EH, saved_G0))
    require(saved_interpolation_lower.is_finite()
            and saved_interpolation_lower.lower() > 0,
            "the whole original strict positive homotopy Jacobian lower")
    require(len(whole_saved_observation_disks) == MODES
            and all(d["mode"] == n and d["complete_grid_points"] == GRID
                    for n, d in enumerate(whole_saved_observation_disks, 1)),
            "all192 complete observations, never an incomplete prefix")
    square = api.zero
    for disk in whole_saved_observation_disks:
        radius = up(disk["radius"])
        square = square+2*radius*radius
    m, sigma = saved_interpolation_lower.lower(), api.rational(1, 128)
    exponent = 4*SOURCE_MODES*sigma+4*MODES*(sigma+G0)-4*GRID*sigma
    return {
        COMPONENT_ORDER[0]: (eR*BH*N0).upper(),
        COMPONENT_ORDER[1]: (api.rational(ROWS).sqrt()*BH*D
                             /api.rational(2).sqrt()).upper(),
        COMPONENT_ORDER[2]: (4*MODES*EH*J*N0/m.sqrt()).upper(),
        COMPONENT_ORDER[3]: (2*api.rational(SOURCE_MODES*MODES).sqrt()
                             *J*N0*exponent.exp()).upper(),
        COMPONENT_ORDER[4]: (J*square.sqrt()).upper(),
    }


def complete_column_error(api, saved_complete_components):
    require(set(saved_complete_components) == set(COMPONENT_ORDER),
            "every complete fee is saved before the whole true column error")
    return sum((up(saved_complete_components[name])
                for name in COMPONENT_ORDER), api.zero).upper()


def complete_signed_enclosures(api, exact_signed_rationals, saved_joint_error):
    """Convenient component balls plus an unchanged stronger joint l2 bound."""
    require(len(exact_signed_rationals) == ROWS,
            "all96 exact signed values before any enclosure is formed")
    error = up(saved_joint_error)
    symmetric = api.arb(0, error)
    return [api.rational(Fraction(value))+symmetric
            for value in exact_signed_rationals]
