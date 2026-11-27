"""ASR: whole source192 signed carrier for the ORIGINAL alpha=v_i-w.

Pure directed formulas. No imports, IO, transport, old norm or cohomology
producer. The owner admits complete SN/W/SEI receipts and rematerializes
the exact original two-branch endpoint with its whole SHA before use.
"""

RAW_MODES = 192
MODES = 2048
GRID = 8192
STRIP_DENOMINATOR = 128
KIND = "R149_original_source_alpha_carrier_formulas_v1"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def up(value):
    require(value.is_finite() and value.lower() >= 0, "one complete nonnegative bound")
    return value.upper()


def conjugate(api, value):
    return api.acb(value.real, -value.imag)


def horner(api, point, coefficients):
    value = api.acb(0)
    for coefficient in reversed(coefficients):
        value = point*(coefficient+value)
    return value


def original_grid(api, positive_t, mean_t, Hs, Hc, Ks, Kc):
    """All raw finite t values and G=K48 o H24 values on the same grid."""
    require(len(Hs) == len(Hc) == 24 and len(Ks) == len(Kc) == 48,
            "all original H24 and K48 pairs, without a phase reset")
    require(len(positive_t) == RAW_MODES and mean_t.is_finite(), "whole raw SN trial including its mean")
    h = [api.acb(api.rational(c), -api.rational(s)) for s, c in zip(Hs, Hc)]
    k = [api.acb(api.rational(c), -api.rational(s)) for s, c in zip(Ks, Kc)]
    result = []
    for index in range(GRID):
        x = api.arb.pi()*index/(2*GRID)
        point = api.acb((4*x).cos(), (4*x).sin())
        finite_h = x+horner(api, point, h).real
        hp = api.acb((4*finite_h).cos(), (4*finite_h).sin())
        finite_g = finite_h+horner(api, hp, k).real
        raw_t = mean_t+2*horner(api, point, positive_t).real
        require(raw_t.is_finite() and finite_g.is_finite(), "complete finite signed grid entry")
        result.append((raw_t, finite_g))
    return result


def raw_trial_strip_norm(api, positive_t, mean_t):
    """One NEW finite raw carrier norm; no old qG or transport norm."""
    require(len(positive_t) == RAW_MODES and mean_t.is_finite(),
            "all192 raw source modes and its complete mean")
    sigma = api.rational(1, STRIP_DENOMINATOR)
    result = abs(mean_t).upper()
    for n, value in enumerate(positive_t, 1):
        result = result+2*abs(value).upper()*(4*n*sigma).exp()
    return result.upper()


def source_error_columns(api, original_SN_errors, raw_radius_columns,
                         original_density_matrix, original_sqrt_j):
    require(len(original_SN_errors) == len(raw_radius_columns) == 4
            and len(original_density_matrix) == 4
            and all(len(row) == 4 for row in original_density_matrix),
            "all four original SN columns and the full true-density matrix")
    raw = [up(a)+up(b) for a, b in zip(original_SN_errors, raw_radius_columns)]
    return [(up(original_sqrt_j)*sum(
        (up(original_density_matrix[q][k])*raw[k] for k in range(q+1)), api.zero)).upper()
        for q in range(4)]


def complete_analytic_data(api, Tstrip, old_EH, old_G1, old_H1):
    T, EH, G1, H1 = map(up, (Tstrip, old_EH, old_G1, old_H1))
    m = api.rational(2)-max(G1, H1)
    require(m.lower() > 0, "both complete degree-one maps preserve vertical imaginary order")
    sigma = api.rational(1, STRIP_DENOMINATOR)
    q = (-4*m.lower()*sigma).exp().upper()
    alias_q = (-4*sigma*GRID).exp().upper()
    require(q < 1 and alias_q < 1, "all analytic geometric tails converge")
    return {"T": T, "EH": EH, "G1": G1, "m": m.lower(),
            "sigma": sigma, "q": q, "alias_q": alias_q}


class WholeQuadrature:
    """Same saved complete grid, successive full n integrals; no cutoff in t."""
    def __init__(self, api, saved_grid):
        require(len(saved_grid) == GRID, "the entire saved grid")
        self.api = api
        self.values = [t for t, g in saved_grid]
        self.steps = [api.acb((4*g).cos(), -(4*g).sin()) for t, g in saved_grid]
        self.powers = list(self.steps)
        self.next_n = 1

    def next(self):
        require(1 <= self.next_n <= MODES, "one complete new mode in order")
        value = sum((t*z for t, z in zip(self.values, self.powers)), self.api.acb(0))/GRID
        require(value.is_finite(), "whole directed quadrature is finite")
        self.powers = [z*q for z, q in zip(self.powers, self.steps)]
        self.next_n += 1
        return value


def original_rotation_and_phase(api, saved_G0, old_EH):
    omega = api.arb.pi()*(api.rational(5831714953207175)+api.rational(5).sqrt())/42424436542040780
    b = 2*saved_G0+omega+api.arb(0, 2*up(old_EH))
    require(omega.is_finite() and b.is_finite(), "original exact quadratic rotation and full source phase")
    return omega, b


def complete_mode_reference(api, n, saved_integral, omega, b):
    """Only the finite signed reference: allows later carrier-only restoration."""
    require(type(n) is int and 1 <= n <= MODES and saved_integral.is_finite(),
            "one complete original finite mode")
    theta, phase = 4*n*omega, 4*n*b
    qn = api.acb(theta.cos(), -theta.sin())
    tn = api.acb(phase.cos(), -phase.sin())
    denominator = qn-1
    lower = abs(denominator).lower()
    require(lower > 0, "one original nonzero divisor with a genuine lower endpoint")
    coefficient = (qn*saved_integral+tn*conjugate(api, saved_integral))/denominator
    require(coefficient.is_finite(), "one whole original phase/reference coefficient")
    return coefficient, lower


def complete_mode_data(api, n, saved_integral, source_columns, analytic, omega, b):
    """AS.10--12; return an unrounded whole coefficient ball and error fee."""
    require(type(n) is int and 1 <= n <= MODES and len(source_columns) == 4,
            "one complete natural positive mode and four error columns")
    candidates = [(up(value)/(4*n)**q).upper() for q, value in enumerate(source_columns)]
    source = min(candidates).upper()
    T, EH, sigma, aq = [analytic[key] for key in ("T", "EH", "sigma", "alias_q")]
    alias = (2*T*(4*n*analytic["G1"]*sigma).exp()*aq/(1-aq)).upper()
    model = (4*n*EH*T*(-4*n*analytic["m"]*sigma).exp()).upper()
    coefficient, lower = complete_mode_reference(api, n, saved_integral, omega, b)
    fee = (2*(source+model+alias)/lower).upper()
    require(coefficient.is_finite() and fee.is_finite(), "whole signed alpha coefficient enclosure")
    return {"coefficient": coefficient, "extra_error": fee,
            "source_candidates": candidates, "source": source,
            "model": model, "aliases": alias, "divisor_lower": lower}


def complete_tail(api, analytic, third_source_error):
    """AS.13--14: complete analytic part plus the entire Sobolev source tail."""
    q, T, K = analytic["q"], analytic["T"], MODES
    analytic_tail = (272*T*q**(K+1)*(K+1-K*q)/(1-q)**2).upper()
    E3 = up(third_source_error)
    transport_W = (api.rational(17, 8)*E3*api.rational(2, 3*K**3).sqrt()).upper()
    transport_L2 = (api.rational(17, 8)*E3/(K+1)**2).upper()
    return {"analytic_tail": analytic_tail, "source_Linf_tail": transport_W,
            "source_L2_tail": transport_L2,
            "complete_Linf_tail": (analytic_tail+transport_W).upper(),
            "complete_L2_tail": (analytic_tail+transport_L2).upper()}


def complete_errors(api, saved_head_W, saved_head_L2_square, saved_tail):
    W, square = up(saved_head_W), up(saved_head_L2_square)
    tail_W, tail_L2 = map(up, (saved_tail["complete_Linf_tail"], saved_tail["complete_L2_tail"]))
    return {"complete_alpha_trial_Linf_error_upper": (W+tail_W).upper(),
            "complete_alpha_trial_L2_error_upper": (square+tail_L2*tail_L2).sqrt().upper()}
