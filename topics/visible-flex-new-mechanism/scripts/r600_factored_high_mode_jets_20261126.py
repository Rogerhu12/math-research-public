#!/usr/bin/env python3
"""New R600 modes with the exact common r**(j*j) factor kept logarithmic.

This module defines source only. Science belongs to the explicitly declared
public Actions run. It never changes the evaluator of a paid lower mode.
"""
from collections import defaultdict
import hashlib
import math
from pathlib import Path
import time

import numpy as np

BINDINGS = {
    "r576_finite_height_turning_20261126.py":
        "40d70b729664a8d59dc653ce30315ea356ce09c461bd4d108fc0a78d05517ad9",
    "r571_milder_seed_outer_jets_20261126.py":
        "ede50d8c4d362d77f9618b3481233d32e5ecc73842af7d84dddd8c78bb518970",
}
for filename, expected in BINDINGS.items():
    if hashlib.sha256(Path(__file__).with_name(filename).read_bytes()).hexdigest() != expected:
        raise RuntimeError("factored high-mode source binding differs: "+filename)

DECLARED_NEW_MODES = (18, 20, 22)
COUNTS = defaultdict(int)


class HighModeBudget(Exception):
    pass


def check(deadline):
    if time.monotonic() >= deadline:
        raise HighModeBudget("declared new-high-mode scientific clock")


def factored_jets(seed, u, state, mode):
    """Return all 13 original jets divided by r**mu, and mu*log(r).

    Subscripts on these hat quantities mean original derivatives divided by
    the common factor. They are not derivatives of the hat value itself.
    ODE jets are defined by the full original ODE, not by derivatives of a
    floating dense-interpolation polynomial.
    """
    seed.ANGULAR_MODE, seed.PHASE = int(mode), 0.
    r, eps, g, elog, gp = seed.coefficients(float(u))
    y, z = state
    yu = eps*z
    yuu = -g*yu-eps*y
    yuuu = -gp*yu-g*yuu-eps*elog*y-eps*yu
    ur = -u*u/seed.ELL
    urr = 2*u**3/seed.ELL**2
    urrr = -6*u**4/seed.ELL**3
    yr = yu*ur
    yrr = yuu*ur*ur+yu*urr
    yrrr = yuuu*ur**3+3*yuu*ur*urr+yu*urrr
    j, mu = int(mode), int(mode)**2
    f = y
    fr = mu*y/r+yr
    frr = mu*(mu-1)*y/(r*r)+2*mu*yr/r+yrr
    frrr = (mu*(mu-1)*(mu-2)*y/r**3
             +3*mu*(mu-1)*yr/(r*r)+3*mu*yrr/r+yrrr)
    sine, cosine = np.sin(u), np.cos(u)
    w = seed.AMP*np.exp(-(2-sine)*u)
    wr = w*((2-sine)*u*u-cosine*u**3)/seed.ELL
    # Exact cancellation of mu*y; no independently formed large difference.
    a = -w*r*yr/(mu-1)
    ar = w*fr
    arr = wr*fr+w*frr
    U = (mu-1)/j*a/r
    Ur = (mu-1)/j*(ar/r-a/(r*r))
    Urr = (mu-1)/j*(arr/r-2*ar/(r*r)+2*a/r**3)
    V = -j*f/r
    Vr = -j*(fr/r-f/(r*r))
    Vrr = -j*(frr/r-2*fr/(r*r)+2*f/r**3)
    COUNTS["factored_jet_queries"] += 1
    hats = np.asarray([f,fr,frr,frrr,a,ar,arr,U,Ur,Urr,V,Vr,Vrr],dtype=float)
    if not np.all(np.isfinite(hats)):
        raise ArithmeticError("nonfinite factored original high-mode jet")
    return hats, mu*math.log(float(r))


class FactoredFlatSeed:
    """The same finite-DtN approximation, now for only genuinely new modes."""

    def __init__(self, mode, args, base, deadline, preserve_minimum_radius):
        if int(mode) not in DECLARED_NEW_MODES:
            raise ValueError("only new modes 18,20,22 belong to this declared scope")
        self.mode, self.args, self.base = int(mode), args, base
        self.deadline, self.seed = deadline, base.seed
        self.started = time.monotonic()
        self.status = "new_inner_started"
        self.completed_inner_RHS = self.completed_outer_RHS = 0
        self.completed_inward_extension_RHS = 0
        COUNTS["new_modes_started"] += 1
        check(deadline)
        seed = self.seed
        seed.ANGULAR_MODE, seed.PHASE = self.mode, 0.
        inner = seed.inner_slope(args.M,args.rtol,args.atol,.1)
        self.inner = inner
        self.completed_inner_RHS = int(inner["nfev_inner"])
        base.COUNTS["seed_RHS"] += self.completed_inner_RHS
        COUNTS["new_inner_RHS"] += self.completed_inner_RHS
        COUNTS["new_inner_completed"] += 1
        self.alpha = float(inner["alpha_first"])
        self.true_first_peak_radius = base.RC+base.ELL/self.alpha
        requested = float(preserve_minimum_radius)
        if not (base.RC < requested <= base.R0):
            raise ValueError("invalid paid common inner-radius requirement")
        self.minimum_radius = min(requested,self.true_first_peak_radius)
        self.segments = []
        self.status = "new_dense_outer_started"
        initial = np.array([1.,inner["z_at_alpha_first"]])
        wanted_u = base.ELL/(self.minimum_radius-base.RC)
        self.inward_extension = None
        if wanted_u > self.alpha:
            # A genuinely new, short ODE continuation of this new mode's
            # paid-at-this-run Cauchy state. It preserves every old radial node
            # instead of deleting a paid first node when alpha_j shifts.
            check(deadline)
            sol = seed.integrate(self.alpha,wanted_u,initial,
                                 args.rtol,args.atol,.1,dense=True)
            n = int(sol.nfev)
            self.completed_inward_extension_RHS += n
            base.COUNTS["seed_RHS"] += n
            COUNTS["new_inward_extension_RHS"] += n
            self.segments.append((self.alpha,float(wanted_u),sol.sol,0.))
            self.inward_extension = {
                "u_from_true_alpha17":self.alpha,"u_to_paid_common_mouth":float(wanted_u),
                "preserved_paid_minimum_radius":requested,"new_RHS":n,
                "new_mode_only_no_old_DtN_replayed":True}
        last_u = base.ELL/(base.R0-base.RC)
        centers = np.pi/2+2*np.pi*np.arange(seed.FIRST_PEAK+1)
        breaks = np.r_[self.alpha,
            np.sort(centers[(centers < self.alpha)&(centers > last_u)])[::-1],last_u]
        state, log_scale = initial.copy(),0.
        for high,low in zip(breaks[:-1],breaks[1:]):
            check(deadline)
            seed.ANGULAR_MODE, seed.PHASE = self.mode,0.
            sol = seed.integrate(float(high),float(low),state,
                                 args.rtol,args.atol,.1,dense=True)
            n = int(sol.nfev)
            self.completed_outer_RHS += n
            base.COUNTS["seed_RHS"] += n
            COUNTS["new_outer_RHS"] += n
            self.segments.append((float(low),float(high),sol.sol,log_scale))
            outgoing = sol.y[:,-1]
            scale = float(np.max(np.abs(outgoing)))
            if not (scale > 0 and np.isfinite(scale)):
                raise ArithmeticError("new high-mode logarithmic transfer normalization failed")
            log_scale += math.log(scale)
            state = outgoing/scale
        hats,power_log = factored_jets(seed,float(last_u),state,self.mode)
        cauchy_norm = math.hypot(float(hats[0]),.08*float(hats[1]))
        if not (cauchy_norm > 0 and np.isfinite(cauchy_norm)):
            raise ArithmeticError("new high-mode original Cauchy norm vanished")
        self.display_log = log_scale+power_log+math.log(cauchy_norm)
        self.outer = base.scaled_values(hats,log_scale+power_log-self.display_log)
        self.status = "new_mode_dense_field_completed"
        COUNTS["new_modes_completed"] += 1
        self.finite_inner_data = {
            "mode":self.mode,"M":args.M,"terminal_peak_index":args.M+1,
            "terminal_condition":"rho_(M+1)=0; y(alpha_(M+1))=0",
            "alpha_first":self.alpha,"z_alpha_first":float(inner["z_at_alpha_first"]),
            "rho_first_plus_one":float(inner["rho_first_plus_one"]),
            "display_log_scale":self.display_log,
            "minimum_numerically_evaluated_radius":self.minimum_radius,
            "true_first_peak_radius":self.true_first_peak_radius,
            "preserve_paid_grid_inward_extension":self.inward_extension,
            "outer_jets":self.outer.tolist(),
            "proof":"R600, same mild tail with finite modes through32",
            "same_original_13_jets_with_common_power_only_factored":True,
            "power_factor_never_formed_before_display_scaling":True,
            "old_lower_mode_evaluators_changed":False,
            "exact_model_below_numerical_radius":"the infinite DtN flat germ, not a zero interval",
            "finite_DtN_ODE_and_core_transfer_errors_certified":False,
            "new_inner_RHS":self.completed_inner_RHS,
            "new_outer_RHS":self.completed_outer_RHS,
            "new_inward_extension_RHS":self.completed_inward_extension_RHS,
            "elapsed_seconds":time.monotonic()-self.started}

    def evaluate(self, r):
        check(self.deadline)
        r = np.asarray(r,dtype=float)
        if (np.any(r < self.minimum_radius*(1-1e-14))
                or np.any(r > self.base.R0*(1+1e-14))):
            raise ValueError("new high-mode seed query outside its declared numerical window")
        seed = self.seed
        seed.ANGULAR_MODE,seed.PHASE = self.mode,0.
        u = self.base.ELL/(r-self.base.RC)
        answer = np.zeros((r.size,13))
        assigned = np.zeros(r.size,dtype=bool)
        for low,high,dense,logarithm in self.segments:
            selected = (~assigned)&(u >= low-1e-12)&(u <= high+1e-12)
            for count,index in enumerate(np.flatnonzero(selected)):
                if count % 128 == 0:
                    check(self.deadline)
                hats,power_log = factored_jets(seed,float(u[index]),dense(float(u[index])),self.mode)
                answer[index] = self.base.scaled_values(hats,logarithm+power_log-self.display_log)
                assigned[index] = True
        if not np.all(assigned):
            raise ArithmeticError("new high-mode seed has an unassigned radial node")
        COUNTS["new_dense_radial_queries"] += int(r.size)
        return answer[:,:3]
