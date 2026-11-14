"""Full R44 mean derivative and Darboux residual from one compatible height.

The caller MUST supply the same R48 H,Kbar,Kbar_x, hence exact first-row
height compatibility. The complete small mean root exists by the paid
R33 domain. No finite mean projection or ODE substitution is performed.
The weighted mean identity recovers the missing scalar residual exactly.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
from flint import arb


def full_mean_residual_bounds(H, Kbar, Kbarx, *, modes, weights,
                              radius, radius_x, w, log_w_x, norms):
    r, rx, ell = radius, radius_x, log_w_x
    if not r > 0 or not rx > 0 or not w > 0 or not w <= arb(1)/2:
        raise ValueError("The same true regular source background is required")
    if any(0 in field and not field[0] == 0 for field in (H, Kbar, Kbarx)):
        raise ValueError("All three supplied candidate fields must be nonmean")
    Pn, Kn, Kxn = (norms[k] for k in ("P_tau", "K_tau", "Kx_tau"))
    R = (Pn+Kn).upper()
    if not R < arb(1)/32:
        raise ValueError("The complete mean small-root theorem is outside its domain")
    c = (4*R*R).upper()
    Tn, Un, linear = arb(0), arb(0), arb(0)
    for m in modes:
        h, k, kx = 2*H[m].real, 2*Kbar[m].real, 2*Kbarx[m].real
        # P=-m Hcos/(r w) sin; T=-m² Hcos/(r w) cos.
        T = -m*m*h/(r*w)
        U = -m*k+m*h/(r*w)
        Tn += weights[m]*abs(T).upper()
        Un += weights[m]*abs(U).upper()
        linear += weights[m]*abs(kx+ell*(2*k+T)).upper()
    Tn, Un, linear = Tn.upper(), Un.upper(), linear.upper()
    Lnonmean = norms["nonmean_L_tau"]
    aL = (1-c-Lnonmean).lower()
    if not aL > 0:
        raise ValueError("A full Wiener inverse for L must be certified")
    z, E, ss = (w*w).upper(), (1+w*w).upper(), (rx/r).upper()
    ellabs = abs(ell).upper()
    K = (Kn+c).upper()
    anorm = (2*K+K*K+E*Pn*Pn).upper()
    unorm = (z*anorm).upper()
    if not unorm < 1:
        raise ValueError("The full real/analytic D branch failed")
    numerator = (E*ss*Un*Un+ellabs*((K+Tn)**2+
                  z*(2*K*Tn+Tn*Tn+Pn*Pn))).upper()
    N = (numerator/aL).upper()
    # Rperp is the FULL nonmean source residual, including all modes of
    # the complete rational nonlinear term. The finite linear part is
    # evaluated from the actual Kbar_x of the single candidate height.
    Rperp = (linear+N).upper()
    inverse_D_power = ((1-unorm)**(-arb(3)/2)).upper()
    Wminus = ((c+Lnonmean)*inverse_D_power+
              max(arb(0), (inverse_D_power-1).upper())).upper()
    Mc = (aL/(1+unorm)**(arb(3)/2)).lower()
    if not Mc > 0:
        raise ValueError("The complete mean derivative denominator is not positive")
    # J/L=a+Rperp(theta), <Rperp>=0. Exact height compatibility and the
    # exact mean root imply <J D^-3/2>=0, hence
    # a=-<(L D^-3/2-1)Rperp>/<L D^-3/2>.
    a = (Wminus*Rperp/Mc).upper()
    # Taking the mean of J/L=c_x+Kbar_x+ell(2c+2Kbar+T)-N gives
    # c_x=a-2ell c+<N>, with NO angular projection approximation.
    cx = (a+2*ellabs*c+N).upper()
    Lnorm = (1+c+Lnonmean).upper()
    J = (Lnorm*(Rperp+a)).upper()
    physical_source = ((w/rx)*Rperp).upper()
    darboux = ((w*w/(r*rx*(1+w*w)**2))*J).upper()
    hrr = ((w/rx)*(Kxn+ellabs*Kn)).upper()
    mean_hrr_correction = ((w/rx)*(cx+ellabs*c)).upper()
    return dict(
        complete_mean_abs=c, complete_mean_source_derivative_abs=cx,
        finite_actual_linear_residual_W1=linear,
        complete_nonlinear_source_W1=N,
        complete_nonmean_source_residual_W1=Rperp,
        complete_scalar_mean_residual_abs=a,
        full_finite_J_W1=J,
        actual_Darboux_defect_abs=darboux,
        physical_nonmean_second_source_W1=physical_source,
        nonmean_physical_hrr_W1=hrr,
        mean_physical_hrr_minus_background_abs=mean_hrr_correction,
        full_D_nonconstant_W1=unorm,
        full_weight_minus_one_W1=Wminus,
        P_theta_W1=Tn, K_theta_minus_P_W1=Un)
