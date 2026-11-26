"""IR: complete 96 inverse-density rows in Hdot^-1/2 and L2.

Pure directed finite operations. No IO, numerical imports or old producers.
The caller admits whole IL/W/DC/DB objects, supplies only saved/readback
trial coefficients and grid balls, and persists every complete new result.
Both signs, all aliases, infinite tails, true-map errors and frequency4 are
retained. The resulting rows are E96* Dplus^-1 C^-1, before the original A.
"""

DIMENSION = 96
TRIAL_MODES = 192
GRID_POINTS = 4096
OUTPUT_CUTOFF = 1024
PHYSICAL_FREQUENCY = 4
PHYSICAL_STRIP = "1/256"
KIND = "R149_complete_inverse_density_row_residual_formulas_v1"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def upper(api, value):
    require(value.is_finite() and value.lower() >= 0,
            "a complete finite nonnegative upper bound")
    return value.upper()


def positive(api, value):
    require(value.is_finite() and value.lower() > 0,
            "a complete strictly positive denominator")
    return value.lower()


def magnitude(api, value):
    require(value.is_finite(), "one whole finite real or complex coefficient")
    return abs(value).upper()


def horner_positive(api, q, coefficients):
    """Sum c_n*q^n, n=1..M, retaining every input coefficient."""
    value = api.acb(0)
    for coefficient in reversed(coefficients):
        value = q*(coefficient+value)
    return value


def exact_compound_grid(api, terminal_side, K_sines, K_cosines):
    """IL's exact second terminal lift composed with the whole original K48.

    There is no terminal refit, ODE, odd-part replacement or mean deletion.
    Returned Arb balls are unpersisted until the owner saves and reads them.
    """
    require(len(terminal_side) == 129 and len(K_sines) == len(K_cosines) == 48,
            "one whole original terminal side and all48 postcomposition pairs")
    require(terminal_side[64][1] == 0, "the exact real central phase mean")
    terminal = [api.acb(api.rational(a), api.rational(b))
                for a, b in terminal_side[65:]]
    post = [api.acb(api.rational(c), -api.rational(s))
            for s, c in zip(K_sines, K_cosines)]
    mean = api.rational(terminal_side[64][0])
    result = []
    for ell in range(GRID_POINTS):
        x = api.arb.pi()*ell/(2*GRID_POINTS)
        angle = 4*x
        q = api.acb(angle.cos(), angle.sin())
        a = x+mean+2*horner_positive(api, q, terminal).real
        qa = api.acb((4*a).cos(), (4*a).sin())
        p = a+horner_positive(api, qa, post).real
        require(p.is_finite(), "complete original finite compound grid point")
        result.append(p)
    return result


def fft_tables(api):
    length = GRID_POINTS
    bits = length.bit_length()-1
    permutation = []
    for index in range(length):
        source, target = index, 0
        for bit in range(bits):
            target = (target << 1) | (source & 1)
            source >>= 1
        permutation.append(target)
    stages = []
    width = 2
    while width <= length:
        angle = 2*api.arb.pi()/width
        step = api.acb(angle.cos(), -angle.sin())
        power, roots = api.acb(1), []
        for k in range(width//2):
            roots.append(power)
            power = power*step
        stages.append((width, roots))
        width *= 2
    return permutation, stages


def complete_directed_dft(api, samples, tables):
    """The whole negative-sign unnormalized COMPLEX DFT, all4096 outputs."""
    require(len(samples) == GRID_POINTS and all(v.is_finite() for v in samples),
            "all complete saved positive-primitive complex samples")
    permutation, stages = tables
    require(len(permutation) == GRID_POINTS, "whole Fourier permutation")
    work = [api.acb(samples[index]) for index in permutation]
    for width, roots in stages:
        require(len(roots) == width//2 and GRID_POINTS % width == 0,
                "all complete directed Fourier factors")
        half = width//2
        for start in range(0, GRID_POINTS, width):
            for k in range(half):
                left, right = work[start+k], roots[k]*work[start+k+half]
                work[start+k], work[start+k+half] = left+right, left-right
    require(all(v.is_finite() for v in work), "all4096 directed Fourier outputs")
    return work


class CompletePrimitiveSampleFactory:
    """All new positive primitives evaluated on the same saved exact grid.

    Matrix multiplication is merely a directed evaluation of finite sums.
    It supplies no inverse certificate, and the DFT still pays all aliases.
    """

    def __init__(self, api, grid, coefficient_columns):
        require(len(grid) == GRID_POINTS and len(coefficient_columns) == DIMENSION
                and all(len(c) == TRIAL_MODES for c in coefficient_columns),
                "whole saved grid and all96 full finite trials")
        self.api = api
        basis = api.acb_mat(GRID_POINTS, TRIAL_MODES)
        for ell, point in enumerate(grid):
            require(point.is_finite(), "whole formal grid point")
            q = api.acb((4*point).cos(), (4*point).sin())
            power = q
            for n in range(TRIAL_MODES):
                basis[ell, n] = power
                power = power*q
        coefficients = api.acb_mat(TRIAL_MODES, DIMENSION)
        for j, column in enumerate(coefficient_columns):
            for n, value in enumerate(column, 1):
                require(value.is_finite(), "one entire exact dyadic trial coefficient")
                coefficients[n-1, j] = value/api.acb(0, 4*n)
        self.samples = basis*coefficients
        require(self.samples.nrows() == GRID_POINTS and self.samples.ncols() == DIMENSION,
                "all96 positive primitives on the whole common grid")
        self.next_mode = 1

    def next_complete_samples(self):
        j = self.next_mode
        require(1 <= j <= DIMENSION, "every new row is evaluated once in order")
        result = [self.samples[ell, j-1] for ell in range(GRID_POINTS)]
        require(all(v.is_finite() for v in result), "whole positive primitive sample column")
        self.next_mode += 1
        return j, result


def complete_global_bounds(api, H1, saved_Ep, saved_trial_first):
    """IR.4/10, from whole original W and the complete saved IL result."""
    h1, error, p1 = [upper(api, v) for v in (H1, saved_Ep, saved_trial_first)]
    require(h1 >= api.one, "the whole degree-one Wiener derivative includes mean1")
    sigma = api.rational(1, 256)
    image = upper(api, api.rational(16, 15)*h1*sigma+error)
    true_lower = (api.rational(15, 16)*(2-h1)).lower()
    require(true_lower > 0, "the entire true inverse lift has positive derivative")
    homotopy = (true_lower-error/sigma).lower()
    return {"inverse_lift_error": error, "trial_first": p1,
            "physical_strip": sigma, "complete_image_width": image,
            "true_derivative_lower": true_lower, "homotopy_derivative_lower": homotopy,
            "real_model_bound_available": bool(homotopy > 0)}


def complete_kernels(api, DC, DB, global_bounds):
    sigma = global_bounds["physical_strip"]
    require(2*OUTPUT_CUTOFF < GRID_POINTS, "strict complete Fourier alias separation")
    aliases = [DC.complete_dft_alias(api, sigma, GRID_POINTS, k, api.one)
               for k in range(1, OUTPUT_CUTOFF+1)]
    return {"aliases": aliases,
            "tail_H": DC.analytic_primitive_derivative_tail(api, sigma, OUTPUT_CUTOFF, api.one)
                      ["complete_energy_tail_upper"],
            "tail_L2": DB.analytic_primitive_derivative_L2_tail(api, sigma, OUTPUT_CUTOFF, api.one)
                       ["complete_L2_tail_upper"],
            "model_H": DC.analytic_primitive_derivative_tail(api, sigma, 0, api.one)
                       ["complete_energy_tail_upper"],
            "model_L2": DB.analytic_primitive_derivative_L2_tail(api, sigma, 0, api.one)
                        ["complete_L2_tail_upper"]}


def complete_column_bounds(api, coefficients, global_bounds, kernels):
    require(len(coefficients) == TRIAL_MODES, "all192 exact finite trial coefficients")
    width = global_bounds["complete_image_width"]
    primitive_mass, derivative_mass, norm0_squared, norm1_squared = (
        api.zero, api.zero, api.zero, api.zero)
    for n, value in enumerate(coefficients, 1):
        mass = magnitude(api, value)
        frequency = api.rational(4*n)
        weight = (frequency*width).exp().upper()
        primitive_mass += mass*weight/frequency
        derivative_mass += mass*weight
        norm0_squared += 2*mass*mass
        norm1_squared += 2*frequency*frequency*mass*mass
    primitive_mass, derivative_mass = upper(api, primitive_mass), upper(api, derivative_mass)
    model_mass = upper(api, global_bounds["inverse_lift_error"]*derivative_mass)
    analytic_H = upper(api, model_mass*kernels["model_H"])
    analytic_L2 = upper(api, model_mass*kernels["model_L2"])
    model_H, model_L2, real_L2 = analytic_H, analytic_L2, None
    if global_bounds["real_model_bound_available"]:
        denominator = positive(api, global_bounds["homotopy_derivative_lower"].sqrt())
        norm0 = upper(api, upper(api, norm0_squared).sqrt())
        norm1 = upper(api, upper(api, norm1_squared).sqrt())
        real_L2 = upper(api, global_bounds["inverse_lift_error"]*(
            norm0/global_bounds["physical_strip"]+global_bounds["trial_first"]*norm1)/denominator)
        if real_L2 < model_L2:
            model_L2 = real_L2
        if real_L2/2 < model_H:
            model_H = upper(api, real_L2/2)
    return {"primitive_mass": primitive_mass,
            "tail_H": upper(api, primitive_mass*kernels["tail_H"]),
            "tail_L2": upper(api, primitive_mass*kernels["tail_L2"]),
            "analytic_model_H": analytic_H, "analytic_model_L2": analytic_L2,
            "real_model_L2": real_L2, "model_H": model_H, "model_L2": model_L2}


def entire_signed_head(api, mode, complete_DFT, bounds, kernels):
    """The complete signed residual head AFTER every analytic alias is paid."""
    require(1 <= mode <= DIMENSION and len(complete_DFT) == GRID_POINTS,
            "one complete new row with the whole exact DFT")
    result = []
    for k in range(1, OUTPUT_CUTOFF+1):
        centre = complete_DFT[k]/GRID_POINTS
        alias = upper(api, bounds["primitive_mass"]*kernels["aliases"][k-1])
        interval = (-alias).union(alias)
        full = api.acb(centre.real+interval, centre.imag+interval)
        residual = api.acb(0, 4*k)*full
        if k == mode:
            residual -= api.acb(2*mode, -2*mode)
        require(residual.is_finite(), "entire signed residual coefficient including alias")
        result.append(residual)
    return result


def complete_residual_norms(api, DC, DB, saved_signed_head, bounds):
    require(len(saved_signed_head) == OUTPUT_CUTOFF,
            "the entire saved positive head, with negative conjugates retained")
    head = {}
    for k, value in enumerate(saved_signed_head, 1):
        require(value.is_finite(), "one whole formal signed Fourier ball")
        head[k] = (value.real, value.imag)
        head[-k] = (value.real, -value.imag)
    energy = DC.complete_fourier_energy_residual(api, head, OUTPUT_CUTOFF,
                                                bounds["tail_H"], bounds["model_H"])
    l2 = DB.complete_L2_residual(api, head, OUTPUT_CUTOFF,
                               bounds["tail_L2"], bounds["model_L2"])
    return {"H": energy["complete_true_energy_residual_upper"],
            "L2": l2["complete_true_L2_residual_upper"],
            "analytic_model_H": bounds["analytic_model_H"],
            "analytic_model_L2": bounds["analytic_model_L2"],
            "real_model_L2": bounds["real_model_L2"]}


def complete_joint_residual(api, formal_columns):
    require(len(formal_columns) == DIMENSION,
            "all96 complete formal residual columns, never a prefix")
    out = {}
    for norm in ("H", "L2"):
        squared = sum((upper(api, column[norm])**2 for column in formal_columns), api.zero)
        out[norm] = upper(api, upper(api, squared).sqrt())
    out["complete_coordinate_row_L2_error"] = upper(api, out["H"]/2)
    return out
