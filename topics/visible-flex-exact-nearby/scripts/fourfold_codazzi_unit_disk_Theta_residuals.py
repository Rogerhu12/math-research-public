"""UDR: new unit-disk phase residuals contracted with original96 Theta rows.

No imports, IO or old producer. api midpoint functions return exact dyadic
points, and every bound is directed. Old alpha/IR/OT carriers stay fixed.
The new natural outputs are joint products and full original row errors.
"""

GRID = 8192
MODES = 2048
PRODUCT_ORDER = ["complete_unit_disk_alpha_finite_Linf_product_upper",
    "complete_unit_disk_alpha_finite_L2_product_upper",
    "complete_unit_disk_alpha_inverse_error_Linf_product_upper",
    "complete_unit_disk_alpha_inverse_error_L2_product_upper"]


def require(ok, message):
    if not ok:
        raise ValueError(message)


def up(value):
    require(value.is_finite() and value.lower() >= 0, "one complete nonnegative directed bound")
    return value.upper()


def conjugate(api, value):
    return api.acb(value.real, -value.imag)


class UnitDiskPhaseInput:
    """Every original grid node, new dyadic centers, complete disk recurrence.

    The old rectangular WholeQuadrature is not called or altered. The
    original entire alpha trial is supplied separately to the residual.
    """
    def __init__(self, api, whole_original_grid):
        require(len(whole_original_grid) == GRID, "every original raw192/G grid entry")
        self.api, self.next_n = api, 1
        self.u, self.uabs, self.s, self.tau = [], [], [], []
        raw_radius = api.zero
        for raw, phase in whole_original_grid:
            require(raw.is_finite() and phase.is_finite(), "each complete saved original real grid ball")
            u = api.midpoint_real(raw)
            step = api.acb((4*phase).cos(), -(4*phase).sin())
            s = api.midpoint_complex(step)
            require(u.is_exact() and s.real.is_exact() and s.imag.is_exact(), "exact new dyadic point centers")
            self.u.append(u)
            self.uabs.append(abs(u).upper())
            self.s.append(s)
            self.tau.append(abs(step-s).upper())
            raw_radius = raw_radius+abs(raw-u).upper()
        self.raw_radius = (raw_radius/GRID).upper()
        self.centers = [api.acb(1) for _ in range(GRID)]
        self.radii = [api.zero for _ in range(GRID)]

    def next(self):
        api = self.api
        require(1 <= self.next_n <= MODES, "all2048 new complete modes in natural order")
        quadrature, radial_error = api.acb(0), api.zero
        for m in range(GRID):
            product = self.centers[m]*self.s[m]
            center = api.midpoint_complex(product)
            require(center.real.is_exact() and center.imag.is_exact(), "the next point is an exact dyadic")
            rho = abs(product-center).upper()
            old = up(self.radii[m])
            radius = (old+(1+old)*up(self.tau[m])+rho).upper()
            self.centers[m], self.radii[m] = center, radius
            quadrature = quadrature+self.u[m]*center
            radial_error = radial_error+self.uabs[m]*radius
        quadrature = quadrature/GRID
        center = api.midpoint_complex(quadrature)
        radius = (self.raw_radius+radial_error/GRID+abs(quadrature-center).upper()).upper()
        require(radius.is_finite() and center.real.is_exact() and center.imag.is_exact(),
                "one whole new finite quadrature disk, with all point and summation errors")
        self.next_n += 1
        return {"center": center, "radius": radius,
                "complete_grid_points": GRID, "complete_positive_mode": self.next_n-1}


def complete_same_trial_mode_residual(api, n, disk, original_alpha_trial, *,
                                      omega, source_phase, source_columns,
                                      original_T, original_EH, original_G1, original_m):
    """UDR.7--8: new kernel residual to an unchanged old signed coefficient.

    All four old source columns/global bounds are copied complete records.
    No old ASR scalar/norm/cohomology-target reducer is invoked.
    """
    require(type(n) is int and 1 <= n <= MODES and len(source_columns) == 4
            and disk["complete_grid_points"] == GRID and disk["complete_positive_mode"] == n,
            "every complete new natural mode uses every original input")
    radius = up(disk["radius"])
    enclosure = api.acb(disk["center"].real+api.arb(0, radius),
                        disk["center"].imag+api.arb(0, radius))
    theta, phase = 4*n*omega, 4*n*source_phase
    q, t = api.acb(theta.cos(), -theta.sin()), api.acb(phase.cos(), -phase.sin())
    denominator = q-1
    lower = abs(denominator).lower()
    require(lower > 0, "the original complete quadratic cohomological divisor is bounded away from zero")
    reference = (q*enclosure+t*conjugate(api, enclosure))/denominator
    sigma = api.rational(1, 128)
    T, EH, G1 = map(up, (original_T, original_EH, original_G1))
    require(original_m.is_finite() and original_m.lower() > 0,
            "the complete original positive imaginary-order lower bound")
    m = original_m.lower()
    source = min((up(value)/(4*n)**r).upper() for r, value in enumerate(source_columns))
    a = (-4*sigma*GRID).exp().upper()
    require(a < 1, "the full original trapezoid alias series converges")
    aliases = (2*T*(4*n*G1*sigma).exp()*a/(1-a)).upper()
    model = (4*n*EH*T*(-4*n*m*sigma).exp()).upper()
    finite = abs(reference-original_alpha_trial).upper()
    residual = (finite+2*(source+model+aliases)/lower).upper()
    require(residual.is_finite(), "all same-trial phase, source, model, aliases and disk errors are retained")
    return {"complete_signed_trial_residual_upper": residual,
            "new_finite_disk_to_old_trial_upper": finite, "complete_source_upper": source,
            "complete_model_upper": model, "complete_alias_upper": aliases,
            "complete_original_divisor_lower": lower}


class WholeContractedProducts:
    """Save whole weighted residual prefixes; output four new operator products.

    No replacement unweighted alpha-error scalar target is produced. The
    exact original2048-mode carrier and every actual tail remain unchanged.
    """
    def __init__(self, api, *, saved_G_HS, saved_G_positive_W, saved_IR_H, saved_IR_L2):
        self.api = api
        self.J, self.W, self.H, self.e0 = map(up, (saved_G_HS, saved_G_positive_W, saved_IR_H, saved_IR_L2))
        self.S = (api.rational(51, 50)*(self.e0+api.rational(10, 9)*self.H)).upper()
        self.next_n = 1
        self.finf = self.f2square = self.einf = self.e2square = api.zero

    def append(self, n, saved_complete_mode_residual):
        require(n == self.next_n and n <= MODES, "the whole2048-mode contracted prefix has no gap")
        delta = up(saved_complete_mode_residual)
        self.finf = (self.finf+2*delta*self.J).upper()
        self.f2square = (self.f2square+4*delta*delta*self.W*self.W).upper()
        self.einf = (self.einf+delta*self.H).upper()
        self.e2square = (self.e2square+2*delta*delta*self.S*self.S/9).upper()
        self.next_n += 1

    def finish(self, saved_original_whole_tail_Linf, saved_original_whole_tail_L2):
        require(self.next_n == MODES+1, "no head prefix substitutes for the complete joint residual")
        tail0, tail2 = map(up, (saved_original_whole_tail_Linf, saved_original_whole_tail_L2))
        return {
            PRODUCT_ORDER[0]: (self.finf+tail0*self.J).upper(),
            PRODUCT_ORDER[1]: (self.f2square+2*tail2*tail2*self.W*self.W).sqrt().upper(),
            PRODUCT_ORDER[2]: (self.einf+tail0*self.H/2).upper(),
            PRODUCT_ORDER[3]: (self.e2square+tail2*tail2*self.S*self.S/9).sqrt().upper(),
        }


def complete_original_row_errors(api, *, saved_original_alpha_trial_W,
                                saved_IR_H, saved_IR_L2, saved_finite_product,
                                saved_inverse_error_product, saved_whole_model_rounding,
                                original_whole_model_one_loss_norm):
    A, H, e0, Pf, Pe, rounding, KG = map(up, (saved_original_alpha_trial_W, saved_IR_H,
        saved_IR_L2, saved_finite_product, saved_inverse_error_product,
        saved_whole_model_rounding, original_whole_model_one_loss_norm))
    S = (api.rational(51, 50)*(e0+api.rational(10, 9)*H)).upper()
    multiplication = (A*H/2+Pf+Pe).upper()
    L2 = (H/2+multiplication/4).upper()
    H1 = (api.rational(21, 20)*(S+multiplication)).upper()
    return {"complete_unit_disk_original_VQ_joint_L2_error_upper": L2,
            "complete_unit_disk_original_VQ_joint_H1_error_upper": H1,
            "complete_unit_disk_original_Theta_joint_L2_error_upper": (KG*H1+rounding).upper()}


def complete_original_low_Theta_error(api, saved_whole_VQ_error, saved_whole_low_model_rounding):
    return (up(saved_whole_VQ_error)+up(saved_whole_low_model_rounding)).upper()
