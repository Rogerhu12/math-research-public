#!/usr/bin/env python3
"""R106: true subprincipal ray fields from already enclosed infinite geometry.

This module performs algebra only. Callers must supply actual whole-object balls
for all six geometric jets, K0, K0_r and (at the waist) the smooth ell quotient.
It does not create a geometric enclosure, a ray/J enclosure or an integral
certificate. No real projection or parameter midpoint is taken.

The reduced-density expression agrees with BulkTarget.density_values in
fourfold_phase_beta_bulk_interval.py; it is NOT pointwise Fcal/mu. R106 gives
the exact missing angular divergence and endpoint flux.

All derivatives below use the supplied physical radial and physical angular
coordinates. With normalized label x=4*eta, pass J=d(theta)/dx (e.g. Y_x);
the returned phase is then already the coefficient for normalized frequency j.
Do not divide that answer by 4 again. If J=d(theta)/d(eta) with physical eta,
the resulting physical phase must instead be pulled back as h(x/4)/4.
"""
from __future__ import annotations
from flint import acb


def _dot(a, b):
    return sum((a[k]*b[k] for k in range(3)), acb(0))


def _cross(a, b):
    return [a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0]]


def _positive_real(value, name):
    if not value.real > 0:
        raise ValueError("unproved actual denominator/branch: "+name)


def fields_from_true_geometry(*, F, Fr, Frr, Ftheta, Frtheta, Fthetatheta,
                              K0, K0_r, ell=None):
    """Return the full first-jet fields for the SAME R37 operator used by beta.

    ell is the actual smooth d_theta log(F_z/r)-d_theta log|F|.
    Away from the waist this is Ftheta_z/F_z-(F.Ftheta)/(F.F).
    At a point/box containing F_z=0 callers must supply a separately enclosed
    quotient; a nonzero-r point derivative is not substituted for the quotient.
    The reflected radial side is allowed; no positivity of F_z is assumed.
    """
    K0, K0_r = acb(K0), acb(K0_r)
    _positive_real(-K0, "-K0")
    normal = _cross(Ftheta, Fr)
    nra, nrb = _cross(Frtheta, Fr), _cross(Ftheta, Frr)
    nta, ntb = _cross(Fthetatheta, Fr), _cross(Ftheta, Frtheta)
    nr = [nra[k]+nrb[k] for k in range(3)]
    nt = [nta[k]+ntb[k] for k in range(3)]
    area2, radius2, support = _dot(normal, normal), _dot(F, F), _dot(normal, F)
    for value, name in ((area2, "area squared"), (radius2, "F.F"),
                        (support, "oriented support")):
        _positive_real(value, name)
    lraw, mraw, nraw = (_dot(normal, v) for v in (Frr, Frtheta, Fthetatheta))
    aa, bb, cc = -nraw/area2, mraw/area2, -lraw/area2
    _positive_real(aa, "zeta^2 a")
    curvature_actual = (lraw*nraw-mraw*mraw)/area2**2
    omega = (curvature_actual-K0)/aa
    c_fixed = (bb*bb+K0)/aa
    kappa = (-K0).sqrt(analytic=True)
    FX, FY = _dot(F, Fr), _dot(F, Ftheta)
    d0 = (aa*(_dot(Fr, Fr)-FX*FX/radius2)
          +2*bb*(_dot(Fr, Ftheta)-FX*FY/radius2)
          +cc*(_dot(Ftheta, Ftheta)-FY*FY/radius2))/radius2
    lzr = _dot(nr, F)/support-_dot(normal, nr)/area2-FX/radius2
    lzt = _dot(nt, F)/support-_dot(normal, nt)/area2-FY/radius2
    Lr, Lt = K0_r/(2*K0)-2*lzr, -2*lzt
    if ell is None:
        if not abs(F[2]) > 0:
            raise ValueError("supply the true smooth waist ell quotient")
        ell = Ftheta[2]/F[2]-FY/radius2
    else:
        ell = acb(ell)
    reduced = (d0+omega*(ell*ell+ell*Lt)
               -(aa*Lr*Lr+2*bb*Lr*Lt+c_fixed*Lt*Lt)/4)/kappa
    angular_flux = omega*ell/kappa
    radial_flux = (aa*Lr+bb*Lt)/kappa
    angular_log_flux = (bb*Lr+c_fixed*Lt)/kappa
    log_mu = (-K0).log()/2-2*support.log()+area2.log()+radius2.log()
    result = {
        "reduced_density": reduced,
        "angular_divergence_flux": angular_flux,
        "radial_log_mu_flux": radial_flux,
        "angular_log_mu_flux": angular_log_flux,
        "log_mu": log_mu,
        "log_mu_r": Lr,
        "log_mu_theta": Lt,
        "ray_drift": bb/aa,
        "ray_half_separation": kappa/aa,
        "sqrt_negative_target_curvature": kappa,
        "scaled_a": aa, "scaled_b": bb, "scaled_c_fixed": c_fixed,
        "omega": omega, "ell": ell,
    }
    if any(not value.is_finite() for value in result.values()):
        raise ValueError("nonfinite actual subprincipal field")
    return result


def ray_terms(fields, label_jacobian, sigma, dr_dt=1):
    """Two signed integrands plus an endpoint term; endpoints are not integrated.

    sigma follows R46: velocity=q-sigma*nu. Match a saved runner's branch
    by its actual formula, not by the name or sign of its branch field.
    J is the actual d(theta)/d(label), with its exact initial-label convention.
    dr_dt keeps the true radial orientation; replacing it by abs(dr_dt)
    changes the propagation convention and is not done here.
    """
    if sigma not in (-1, 1):
        raise ValueError("sigma must be +1 or -1")
    J, time_scale = acb(label_jacobian), acb(dr_dt)
    return {
        "angle_rhs": time_scale*(fields["ray_drift"]
                                 -sigma*fields["ray_half_separation"]),
        "primary_integrand": time_scale*J*fields["reduced_density"]/2,
        "angular_primitive_integrand": time_scale*fields["angular_divergence_flux"]/2,
        "endpoint_correction": -J*(fields["radial_log_mu_flux"]
                                  +sigma*fields["log_mu_theta"])/4,
    }


def phase_from_integrated_terms(primary_integral, angular_integral_label_derivative,
                                endpoint_start, endpoint_end):
    """The label derivative is of the COMPLETE signed angular integral."""
    return (primary_integral+angular_integral_label_derivative
            +endpoint_end-endpoint_start)


def root_counterterms_from_actual_R83(Y0_prime, h1):
    """Physical root label: c0=5*Y0'/16, c2=-Y0'*h1/16.

    This uses the exact R83 inward root convention and xi=rho+O(rho^2).
    For another root label pull back BOTH coefficients as one-forms.
    """
    return 5*Y0_prime/16, -Y0_prime*h1/16


def finite_part_from_regular_integral(regular_integral, c0, c2, sqrt_rho_cut):
    """Integral of the true continuous regularized density on [0,R]."""
    R = sqrt_rho_cut
    if not R > 0:
        raise ValueError("positive actual root cut required")
    return regular_integral-c0/(3*R**3)-c2/R


def root_finite_part_wiener_upper(R, fourth_derivative_bound,
                                c0_wiener_bound, c2_wiener_bound):
    """Conditional exact bound in one already certified common Wiener norm."""
    if not R > 0:
        raise ValueError("positive actual root cut required")
    return (R*fourth_derivative_bound/24
            +c0_wiener_bound/(3*R**3)+c2_wiener_bound/R)


def reduced_root_counterterms_from_actual_R83(Y0_prime, h1,
                                             log_density_coefficient_shear_derivative):
    """Counterterms for Dred, not for Fcal/mu.

    kappa_density=mu/sqrt(rho), in the SAME operator/height as Dred.
    It is not R83's radial target curvature coefficient K0/(r-t).
    """
    return (-Y0_prime/16,
            Y0_prime*(h1-4*log_density_coefficient_shear_derivative)/16)


def root_log_density_coefficient_label_derivative(*, F, Fr, Ftheta,
                                                  Frtheta, Fthetatheta,
                                                  label_jacobian):
    """Exact root d_label log(kappa_density) for the original R37 height.

    Here K0 is radial, so d_theta log(kappa_density)=-2*d_theta log(zeta).
    No division by K0 or F_z occurs; true root geometric balls are required.
    """
    normal = _cross(Ftheta, Fr)
    na, nb = _cross(Fthetatheta, Fr), _cross(Ftheta, Frtheta)
    nt = [na[k]+nb[k] for k in range(3)]
    area2, radius2, support = _dot(normal, normal), _dot(F, F), _dot(normal, F)
    for value, name in ((area2, "root area squared"), (radius2, "root F.F"),
                        (support, "root oriented support")):
        _positive_real(value, name)
    lzt = _dot(nt, F)/support-_dot(normal, nt)/area2-_dot(F, Ftheta)/radius2
    return -2*label_jacobian*lzt


def root_phase_from_reduced_terms(reduced_primary_finite_part,
                                 angular_integral_label_derivative,
                                 endpoint_at_cut,
                                 root_log_density_coefficient_label_derivative,
                                 sigma):
    """Retain the non-mean root endpoint constant; the old mean beta drops it."""
    if sigma not in (-1, 1):
        raise ValueError("sigma must be +1 or -1")
    return (reduced_primary_finite_part+angular_integral_label_derivative
            +endpoint_at_cut
            +sigma*root_log_density_coefficient_label_derivative/4)
