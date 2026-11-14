#!/usr/bin/env python3
"""R106 grounded strict-ray fields; use only where the true Y_z is nonzero.

The height is +Y_z or -Y_z according to the real component. This is the SAME
R37 operator with its exact Q_ell Y_z=0 identity, not a change of target metric.
The waist is excluded explicitly. No ray or integral enclosure is created.
"""
from __future__ import annotations
from flint import acb
from fourfold_subprincipal_ray_fields import fields_from_true_geometry, _dot


def grounded_fields_from_true_geometry(*, F, Fr, Frr, Ftheta, Frtheta,
                                      Fthetatheta, K0, K0_r):
    original = fields_from_true_geometry(F=F, Fr=Fr, Frr=Frr,
        Ftheta=Ftheta, Frtheta=Frtheta, Fthetatheta=Fthetatheta,
        K0=K0, K0_r=K0_r)
    radius2 = _dot(F,F)
    Ysquare = F[2]*F[2]/radius2
    if not Ysquare.real > 0 or not abs(F[2]) > 0:
        raise ValueError("unproved actual nonzero grounded height; the waist is excluded")
    yr = Fr[2]/F[2]-_dot(F,Fr)/radius2
    yt = Ftheta[2]/F[2]-_dot(F,Ftheta)/radius2
    Lr = original["log_mu_r"]+2*yr
    Lt = original["log_mu_theta"]+2*yt
    a,b,c = (original[key] for key in ("scaled_a","scaled_b","scaled_c_fixed"))
    k = original["sqrt_negative_target_curvature"]
    result = {
        "reduced_density": -(a*Lr*Lr+2*b*Lr*Lt+c*Lt*Lt)/(4*k),
        "angular_divergence_flux": acb(0),
        "radial_log_mu_flux": (a*Lr+b*Lt)/k,
        "angular_log_mu_flux": (b*Lr+c*Lt)/k,
        "log_mu": original["log_mu"]+Ysquare.log(),
        "log_mu_r": Lr, "log_mu_theta": Lt,
        "ray_drift": original["ray_drift"],
        "ray_half_separation": original["ray_half_separation"],
        "a_over_mu": a/k, "b_over_mu": b/k, "c_over_mu": c/k,
        "grounded_height_squared": Ysquare,
    }
    if any(not value.is_finite() for value in result.values()):
        raise ValueError("nonfinite actual grounded subprincipal field")
    return result


def grounded_root_counterterms(Yprime, s1, h1, logU_theta):
    """Exact R83 root label; logU=2 log(kappa_density_grounded)."""
    return {
        "full_phase_c0": 5*Yprime/16,
        "full_phase_c2": -Yprime*h1/16,
        "grounded_D_c0": -Yprime/16,
        "grounded_D_c2": Yprime*(h1-2*s1)/16,
        "grounded_root_endpoint_per_sigma": logU_theta/8,
        "grounded_log_density_shear_derivative": s1/2,
        "grounded_log_density_theta": logU_theta/2,
    }
