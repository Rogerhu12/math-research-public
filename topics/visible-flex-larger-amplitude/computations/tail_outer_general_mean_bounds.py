"""R64 complete mean and actual compatible-height residual, outside R33.

No small P/K ball is assumed. A finite exact quadratic angular average
plus a full positive-series tail bounds M(0). The real mean branch is
certified by its true monotone derivative and both endpoint signs.
The input Kbar_x MUST be the derivative of the same actual height.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
from flint import arb


def positive_series_remainder(q):
    """C1(q)-1/2 and C(q)-1, with no small-q subtraction."""
    if not 0 <= q < 1:
        raise ValueError("A positive binomial majorant below one is required")
    sd = (1-q).sqrt()
    return (q*(2+sd)/(2*sd*(1+sd)**2)).upper(), (q/(sd*(1+sd))).upper()


def general_mean_and_defect(H, Kbar, Kbarx, *, modes, weights,
                            radius, radius_x, w, log_w_x):
    r, rx, ell = radius, radius_x, log_w_x
    if not r > 0 or not rx > 0 or not w > 0:
        raise ValueError("A true regular source panel is required")
    if any(0 in field and not field[0] == 0 for field in (H, Kbar, Kbarx)):
        raise ValueError("All candidate inputs must have zero angular mean")
    for field in (H, Kbar, Kbarx):
        if any(not field[m].imag.contains(0) for m in modes):
            raise ValueError("This finite evaluator requires the stated real cosine height")
    z, E = (w*w).upper(), (1+w*w).upper()
    names = ("P", "K", "T", "U", "linear", "L", "physical_second_numerator")
    norms = [{key: arb(0) for key in names} for unused in range(2)]
    q0 = arb(0)
    for m in modes:
        h, k, kx = 2*H[m].real, 2*Kbar[m].real, 2*Kbarx[m].real
        p = -m*h/(r*w)
        t = m*p
        # E in this signed quadratic average is the same actual 1+w^2,
        # so retain its full interval rather than selecting its upper end.
        q0 += (k*k+(1+w*w)*p*p)/4+k*t/2
        values = dict(P=abs(p).upper(), K=abs(k).upper(), T=abs(t).upper(),
            U=abs(-m*k-p).upper(), linear=abs(kx+ell*(2*k+t)).upper(),
            L=abs(k+(1+w*w)*t).upper(),
            physical_second_numerator=abs(kx+ell*k).upper())
        for index, weight in enumerate((arb(1), weights[m])):
            for key in names:
                norms[index][key] += weight*values[key]
    norms = [{key:value.upper() for key,value in row.items()} for row in norms]
    zero, weighted = norms
    A0 = (2*zero["K"]+zero["K"]**2+E*zero["P"]**2).upper()
    U0, V0 = (z*A0).upper(), (z*zero["P"]**2).upper()
    if not U0 < 1 or not V0 < 1:
        return dict(gate=False, failure="The c=0 full-series majorant failed",
                    norms=norms, quadratic_mean=q0)
    f0, g0 = positive_series_remainder(U0)
    mean_tail = (A0*f0+(1+zero["K"])*zero["T"]*(g0+V0)/(1-V0)).upper()
    epsilon = (abs(q0).upper()+mean_tail).upper()

    def domain(cbound):
        U, V, aL = [], [], []
        for row in norms:
            kval = row["K"]+cbound
            U.append((z*(2*kval+kval*kval+E*row["P"]**2)).upper())
            V.append((z*row["P"]**2).upper())
            aL.append((1-cbound-row["L"]).lower())
        y = (1-cbound-zero["K"]).lower()
        if not all(u < 1 for u in U) or not all(v < 1 for v in V):
            return None
        N = (1-z*(1+cbound+zero["K"])*zero["T"]/(1-V[0])).lower()
        if not y > 0 or not N > 0 or not all(a > 0 for a in aL):
            return None
        mu = (aL[0]/(1+U[0])**(arb(3)/2)).lower()
        if not mu > 0:
            return None
        return dict(U=U, V=V, aL=aL, y=y, N=N, mu=mu)

    bracket, wide = None, None
    for exponent in range(-48, 0):
        d = arb(2)**exponent
        box = domain(d)
        if box is not None and epsilon < box["mu"]*d:
            bracket, wide = d, box
            break
    if bracket is None:
        return dict(gate=False, failure="No stated symmetric dyadic mean bracket passed the full sign/domain gates",
                    norms=norms, quadratic_mean=q0, mean_tail=mean_tail, mean_epsilon=epsilon)
    c = (epsilon/wide["mu"]).upper()
    tight = domain(c)
    if tight is None:
        raise ArithmeticError("The proved smaller mean interval lost its containing domain")
    ss, ellabs = (rx/r).upper(), abs(ell).upper()
    Nbound, residual = [], []
    for index, row in enumerate(norms):
        k = row["K"]+c
        nn = ((E*ss*row["U"]**2+ellabs*((k+row["T"])**2+
            z*(2*k*row["T"]+row["T"]**2+row["P"]**2)))/tight["aL"][index]).upper()
        Nbound.append(nn)
        residual.append((row["linear"]+nn).upper())
    power = ((1-tight["U"][0])**(-arb(3)/2)).upper()
    Wminus = ((c+zero["L"])*power+max(arb(0), (power-1).upper())).upper()
    scalar = (Wminus*residual[0]/tight["mu"]).upper()
    cx = (scalar+2*ellabs*c+Nbound[0]).upper()
    J = ((1+c+weighted["L"])*(residual[1]+scalar)).upper()
    result = dict(gate=True, norms=norms, quadratic_mean=q0,
        mean_tail=mean_tail, mean_epsilon=epsilon, mean_bracket=bracket,
        mean_sign_margin=(wide["mu"]*bracket-epsilon).lower(),
        mean_derivative_lower=tight["mu"], real_y_lower=tight["y"],
        real_N_lower=tight["N"], real_D_lower=(1-tight["U"][0]).lower(),
        real_S_lower=(1-tight["V"][0]).lower(),
        real_L_lower=tight["aL"][0], Wiener_L_lower=tight["aL"][1],
        bounds=dict(
            complete_mean_abs=c, complete_mean_source_derivative_abs=cx,
            finite_actual_linear_residual_W1=weighted["linear"],
            complete_nonlinear_source_W1=Nbound[1],
            complete_nonmean_source_residual_W1=residual[1],
            complete_scalar_mean_residual_abs=scalar, full_finite_J_W1=J,
            actual_Darboux_defect_abs=((w*w/(r*rx*(1+w*w)**2))*J).upper(),
            physical_nonmean_second_source_W1=((w/rx)*residual[1]).upper(),
            nonmean_physical_hrr_W1=((w/rx)*weighted["physical_second_numerator"]).upper(),
            mean_physical_hrr_minus_background_abs=((w/rx)*(cx+ellabs*c)).upper(),
            full_D_nonconstant_W1=tight["U"][1], full_weight_minus_one_W0=Wminus,
            P_theta_W1=weighted["T"], K_theta_minus_P_W1=weighted["U"]))
    return result
