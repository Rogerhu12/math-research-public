"""BW: first signed target w=vi-alpha carrier from whole completed ASR.

Pure new vi/w trial errors only. All original source columns, analytic
input bounds and alpha errors are copied from the complete ASR actual.
No old cohomology, alpha-mode norm, SN norm or transport target is called.
"""

MODES = 2048
GRID = 8192
STRIP_DENOMINATOR = 128
TARGETS = ["complete_incoming_vi_trial_Linf_error_upper", "complete_incoming_vi_trial_L2_error_upper",
           "complete_target_w_trial_Linf_error_upper", "complete_target_w_trial_L2_error_upper"]


def require(ok, message):
    if not ok:
        raise ValueError(message)


def up(value):
    require(value.is_finite() and value.lower() >= 0, "one complete nonnegative directed upper")
    return value.upper()


def complete_analytic_parameters(api, saved_T, saved_EH, saved_G1, saved_m):
    T, EH, G1 = map(up, (saved_T, saved_EH, saved_G1))
    require(saved_m.is_finite() and saved_m.lower() > 0, "the entire original true-map imaginary lower")
    m = saved_m.lower()
    sigma = api.rational(1, STRIP_DENOMINATOR)
    q = (-4*m*sigma).exp().upper()
    alias_q = (-4*sigma*GRID).exp().upper()
    require(q < 1 and alias_q < 1, "the two complete convergent analytic series")
    return dict(T=T, EH=EH, G1=G1, m=m, sigma=sigma, q=q, alias_q=alias_q)


def complete_vi_mode_error(api, n, original_quadrature, exact_vi_trial, saved_source_columns, analytic):
    require(type(n) is int and 1 <= n <= MODES and len(saved_source_columns) == 4
            and original_quadrature.is_finite() and exact_vi_trial.is_finite(),
            "one complete natural mode and all four original source-error columns")
    candidates = [(up(value)/(4*n)**q).upper() for q, value in enumerate(saved_source_columns)]
    source = min(candidates).upper()
    T, EH, G1, sigma, aq, m = [analytic[key] for key in ("T", "EH", "G1", "sigma", "alias_q", "m")]
    alias = (2*T*(4*n*G1*sigma).exp()*aq/(1-aq)).upper()
    model = (4*n*EH*T*(-4*n*m*sigma).exp()).upper()
    radius = abs(original_quadrature-exact_vi_trial).upper()
    return {"complete_vi_coefficient_error_upper": (source+alias+model+radius).upper(),
            "all_source_candidates": candidates, "complete_source_error_upper": source,
            "complete_alias_error_upper": alias, "complete_true_map_error_upper": model,
            "complete_quadrature_rounding_radius_upper": radius}


def complete_vi_tail(api, analytic, saved_third_source_error):
    q, T, K = analytic["q"], analytic["T"], MODES
    analytic_tail = (2*T*q**(K+1)/(1-q)).upper()
    E3 = up(saved_third_source_error)
    source_Linf = (E3*api.rational(2, 5*K**5).sqrt()/64).upper()
    source_L2 = (E3/(4*(K+1))**3).upper()
    return {"complete_analytic_vi_tail_upper": analytic_tail,
            "complete_source_vi_Linf_tail_upper": source_Linf,
            "complete_source_vi_L2_tail_upper": source_L2,
            "complete_vi_Linf_tail_upper": (analytic_tail+source_Linf).upper(),
            "complete_vi_L2_tail_upper": (analytic_tail+source_L2).upper()}


def complete_vi_errors(api, saved_head_Linf, saved_head_L2_square, saved_tail):
    head, square = map(up, (saved_head_Linf, saved_head_L2_square))
    tail0, tail2 = map(up, (saved_tail["complete_vi_Linf_tail_upper"], saved_tail["complete_vi_L2_tail_upper"]))
    return {TARGETS[0]: (head+tail0).upper(), TARGETS[1]: (square+tail2*tail2).sqrt().upper()}


def complete_w_errors(saved_vi_Linf, saved_vi_L2, saved_alpha_Linf, saved_alpha_L2):
    vi0, vi2, a0, a2 = map(up, (saved_vi_Linf, saved_vi_L2, saved_alpha_Linf, saved_alpha_L2))
    return {TARGETS[2]: (vi0+a0).upper(), TARGETS[3]: (vi2+a2).upper()}
