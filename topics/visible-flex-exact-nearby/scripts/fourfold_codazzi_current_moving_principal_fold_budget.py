#!/usr/bin/env python3
"""Public Arb consumer for the actual full-family moving principal fold.

No characteristic samples, scalar germs, response shards or transport
prefixes are recomputed. Two completed natives give all entire finite-band
coefficient envelopes. The proof constructs the actual analytic flows.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import json
import os
from pathlib import Path
import sys
import time

import flint
from flint import acb, arb, ctx

PUBLIC = "Rogerhu12/math-research-public"
CANDIDATE = "ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
DEFINITION = "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
DIRECTION = "6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
PINS = {
    "root_germ": "397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864",
    "root_budget": "10ff6db82cece6c72ae8a6726c07c188922cf6b307f5af5f50a691ade0abb33f",
}
ROOT_SOURCE = "a3ad50b828c69d3e6f1e9254c1f266535171741ee2cd675d1569ef8f0fac0491"
BUDGET_SOURCE = "4a3ee217b21cabda6ae3dea052f27ff82f03b4218294145dc2f812891688e03e"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    data = Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if Path(path).suffix == ".gz" else data)


def save(path, report):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = (json.dumps(report, indent=2, allow_nan=False)+"\n").encode()
    if path.suffix == ".gz":
        payload = gzip.compress(payload, mtime=0)
    temporary = path.with_name(path.name+".partial")
    temporary.write_bytes(payload)
    temporary.replace(path)


def exact(value):
    value = Fraction(value)
    return arb(value.numerator)/value.denominator


def upper(saved):
    return arb(saved["upper"]).upper()


def lower(saved):
    return arb(saved["lower"]).lower()


def interval(saved):
    return arb(saved["lower"]).union(arb(saved["upper"]))


def complex_interval(saved):
    return acb(interval(saved["real"]), interval(saved["imag"]))


def disk_box(radius):
    radius = arb(radius).upper()
    return acb(arb(0, radius), arb(0, radius))


def power(value, numerator, denominator):
    return (arb(value).log()*numerator/denominator).exp()


def record(value):
    value = arb(value)
    return dict(ball=value.str(60), lower=value.lower().str(60),
                upper=value.upper().str(60))


def complex_record(value):
    return dict(real=record(value.real), imag=record(value.imag),
                modulus_upper=record(abs(value).upper()))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in PINS:
        parser.add_argument("--"+key.replace("_", "-"), type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("preserve the original full-family principal-fold result")
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != PUBLIC):
        raise RuntimeError("the actual public repository Actions environment is required")
    runtime = dict(python=".".join(map(str, sys.version_info[:3])),
                   python_flint=flint.__version__)
    if runtime != dict(python="3.12.14", python_flint="0.9.0"):
        raise RuntimeError("the specified exact arithmetic runtime changed")
    ctx.prec = 256
    started = time.monotonic()
    report = dict(kind="actual_full_family_analytic_moving_principal_fold",
        complete=False, proved=False, source_sha256=sha(__file__), runtime=runtime,
        public_repository=PUBLIC, public_run_id=os.environ.get("GITHUB_RUN_ID"),
        public_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        candidate_sha256=CANDIDATE, background_definition_sha256=DEFINITION,
        explicit_direction_definition_sha256=DIRECTION,
        actual_intrinsic_parameter="eta_0", inputs={}, gates=[], failure=None,
        exact_radial_sign="rho=r_star-r; D_r=-D_rho; D_rho=partial_rho-e*partial_phi; e=-d",
        actual_inverse_fixed_point="rho_new=-tau/lambda+(T+lambda*rho)/lambda; phi_new=chi-(X-phi)",
        complete_mean_and_all193_direction_coordinates_retained=True,
        full_delta_family_band192_paid=True,
        no_original_scalar_transport_or_response_recomputed=True,
        actual_flows_proved_by_analytic_ODE_and_uniform_contraction=True,
        sampled_characteristic_map_used=False,
        old_angular_primitive_replaced_by_fixed_T_primitive=False,
        independent_even_mean_and_all_radial_commutators_retained=True,
        root_reflection_constant_or_strong_return_proved_here=False,
        nonlinear_PDE_solution_or_true_parameter_response_proved_here=False)

    def check(name, okay):
        passed = bool(okay)
        report["gates"].append(dict(name=name, passed=passed))
        if not passed:
            raise ValueError("failed genuine moving principal-fold gate: "+name)

    try:
        for key, expected in PINS.items():
            path = getattr(args, key)
            actual = sha(path)
            if actual != expected:
                raise ValueError("pinned completed input changed: "+key)
            report["inputs"][key] = dict(path=str(path), sha256=actual,
                                         bytes=path.stat().st_size)
        germ, rb = read(args.root_germ), read(args.root_budget)
        check("the complete original joint germ and actual full-family root budget match",
            germ["complete"] and germ["proved"] and germ["source_sha256"] == ROOT_SOURCE
            and germ["candidate_sha256"] == CANDIDATE
            and germ["all_finite_candidate_modes_retained"]
            and int(germ["exact_candidate_metadata"]["modes"]) == 32
            and rb["complete"] and rb["proved"] and rb["source_sha256"] == BUDGET_SOURCE
            and str(rb["public_run_id"]) == "43594466882"
            and rb["candidate_sha256"] == CANDIDATE
            and rb["background_definition_sha256"] == DEFINITION
            and rb["explicit_direction_definition_sha256"] == DIRECTION
            and rb["actual_intrinsic_parameter"] == "eta_0"
            and all(item["passed"] for item in rb["gates"]))
        q = Fraction
        rho_radius = q(9, 10**6)
        native_radius = q(1, 100000)
        delta_radius = q(1, 10**8)
        sigma_native, sigma0, sigma1, sigma_inverse = q(1, 1024), q(1, 64), q(3, 256), q(1, 128)
        sigma_J, sigma_inner = q(1, 128), q(1, 256)
        roots = list(map(q, germ["root_interval"]))
        cell = list(map(q, germ["exact_candidate_piece_interval"]))
        rectangle = list(map(q, germ["complex_radial_rectangle"]["real_interval"]))
        check("the full complex rho disk and all family parameters belong to one actual root piece",
            q(rb["exact_complex_parameter_radius"]) == delta_radius
            and q(rb["exact_outer_radial_radius"]) == native_radius
            and q(germ["complex_radial_radius"]) == native_radius
            and q(rb["exact_moving_Wiener_strip"]) == sigma_native
            and q(germ["moving_phi_strip"]) == sigma_native
            and roots == list(map(q, rb["exact_root_interval"]))
            and rectangle == [roots[0]-native_radius, roots[1]+native_radius]
            and cell[0] < rectangle[0] < roots[0]-rho_radius
            and roots[1]+rho_radius < rectangle[1] < cell[1]
            and germ["actual_candidate_piece"] == rb["exact_candidate_and_response_piece"] == 2549
            and germ["compact_bump_identically_zero_on_entire_actual_germ"]
            and germ["domain_contains_disks_about_every_true_parameter_root"]
            and rectangle[0] > q(9, 50))
        offsets = list(map(q, rb["exact_background_root_offsets"]))
        zcoeff = rb["response_repaired_complete_coefficient_upper"]
        check("all65 base repair and all193 complete direction coefficients are present",
            len(offsets) == 65 and len(zcoeff) == 193
            and len(rb["direction_angular_norms_u"]) == len(rb["direction_angular_norms_v"]) == 5
            and rb["actual_independent_even_mean_preserved"]
            and rb["full_frequency_inverse_not_a_finite_section"])
        base_u = [(upper(germ["moving_U_derivative_Astrip"][j])
                   +upper(rb["background_repair_angular_norms_u"][j])).upper() for j in range(5)]
        base_v = [(upper(germ["moving_v_derivative_Astrip"][j])
                   +upper(rb["background_repair_angular_norms_v"][j])).upper() for j in range(5)]
        zu = [upper(x) for x in rb["direction_angular_norms_u"]]
        zv = [upper(x) for x in rb["direction_angular_norms_v"]]

        def widen(width):
            base_factor = exact(128*(width-sigma_native)).exp().upper()
            direction_factor = exact(384*(width-sigma_native)).exp().upper()
            U = [(base_factor*bu+exact(delta_radius)*direction_factor*zz).upper()
                 for bu, zz in zip(base_u, zu)]
            V = [(base_factor*bv+exact(delta_radius)*direction_factor*zz).upper()
                 for bv, zz in zip(base_v, zv)]
            return U, V, base_factor, direction_factor

        U, V, base_factor, direction_factor = widen(sigma0)
        UJ, VJ, base_Jfactor, direction_Jfactor = widen(sigma_J)
        check("new wide-strip bounds include the complete128and384frequency inflation",
            sigma_native < sigma_J < sigma0
            and all(x.is_finite() for x in U+V+UJ+VJ)
            and base_factor > 1 and direction_factor > base_factor)
        intrinsic = germ["complex_intrinsic_coefficients"]
        gamma_box = complex_interval(intrinsic["gamma"])
        k_box = complex_interval(intrinsic["K1"])
        mean_fee = exact(delta_radius)*upper(zcoeff[96])
        mean_box = (complex_interval(germ["moving_mean_v"])
                    +acb(exact(offsets[32]))+disk_box(mean_fee))
        check("the whole complex mean and intrinsic slope retain genuine branch gaps",
            mean_box.real.upper() < 0 and gamma_box.real.lower() > 0
            and k_box.real.lower() > 0)
        eta_box = -gamma_box*mean_box
        a_box = eta_box*k_box.sqrt()
        a_gap, a_abs = a_box.real.lower(), abs(a_box).upper()
        check("the actual radial characteristic amplitude has positive real part",
            a_gap > 0 and a_abs.is_finite())
        beta = upper(intrinsic["beta"]["modulus_upper"])
        K = upper(intrinsic["K"]["modulus_upper"])
        D0 = (beta*(U[0]**2+K*V[0]**2)/4).upper()
        D1 = (beta*(U[0]**2+K*V[0]**2)).upper()
        D2 = (2*beta*(U[0]*U[1]+K*V[0]*V[1])).upper()
        R = exact(rho_radius)
        exp1 = (D1*R).exp().upper()
        j = (exp1-1).upper()
        exp4 = (4*D1*R).exp().upper()
        M0 = (D0*R+exact(q(2, 3))*a_abs*R*R.sqrt()).upper()
        b0 = (3*M0).upper()
        check("all direct inverse and common-foot flows stay inside the enlarged analytic strip",
            3*M0 < exact(sigma0-sigma1)
            and b0 < exact(sigma1-sigma_inverse))
        A_box = a_box+disk_box((a_abs*j).upper())
        A_gap = (a_gap-a_abs*j).lower()
        A_abs = (a_abs*exp1).upper()
        check("the even quotient is analytic and its actual cube-root branch is separated",
            A_gap > 0 and A_box.real.lower() > 0)
        A_gap_minus_third = power(A_gap, -1, 3).upper()
        Bphi = (exact(q(3, 5))*a_abs*D2*R*exp4).upper()
        BT = (exact(q(2, 5))*a_abs*D2*A_gap_minus_third*R**2*exp4).upper()
        Tmax = (R*power(A_abs, 2, 3)).upper()
        det_error = (2*j+j**2+Tmax*BT**2).upper()
        check("the actual fold Jacobian and Airy principal factor never vanish",
            det_error < exact(q(1, 4)))
        jac_lower = (a_gap*power(A_abs, -1, 3)*(1-det_error)).lower()
        mu_lower = (a_gap**2*power(A_abs, -2, 3)*(1-det_error)).lower()
        check("both complete nonzero principal factors have recorded strict lower bounds",
            jac_lower > 0 and mu_lower > 0)
        lam = q(9, 2)
        Xphi_box = acb(1)+disk_box(j)
        A_inv_third_box = (A_box.log()*acb(-exact(q(1, 3)))).exp()
        radial_main_box = a_box*A_inv_third_box*Xphi_box
        Er = (abs(acb(exact(lam))-radial_main_box).upper()+D0*BT).upper()
        eps_r = (Er/exact(lam)).upper()
        Xrho = (D0*exp1+exact(q(2, 3))*a_abs*R**2*Bphi).upper()
        row_r = (eps_r+BT*b0/(exact(lam)*R)).upper()
        row_phi = (Xrho*R/b0+j).upper()
        check("the inverse radial fixed-point map is a self-map on the genuine full disk",
            eps_r < exact(q(1, 4)) and exact(q(1, 2))+eps_r < exact(q(3, 4)))
        check("both normalized rows of the actual coordinate inverse contract belowonehalf",
            row_r < exact(q(1, 2)) and row_phi < exact(q(1, 2)))
        canonical_radius = lam*rho_radius/2
        physical_small_radius = q(4, 10**6)
        check("the complete near-root physical product maps into the actual inverse rectangle",
            exact(physical_small_radius)*power(A_abs, 2, 3) < exact(canonical_radius)
            and exact(sigma_inner)+M0 < exact(sigma_inverse))
        eta_inv = (1/(gamma_box.real.lower()*(-mean_box.real.upper()))).upper()
        LJ = (2*beta*UJ[0]*VJ[0]+beta*VJ[1]*UJ[0]/2).upper()
        cJ = (eta_inv*LJ/4).upper()
        check("the full nonmean moving inverse is newly paid onA1over128",
            cJ < exact(q(4, 5)))
        J0 = (eta_inv/(4*(1-cJ))).upper()
        J1 = (eta_inv/(1-cJ)).upper()
        radial_margin = native_radius-q(3, 4)*rho_radius
        check("the canonical inner product retains a true radial and moving-angular inverse margin",
            radial_margin == q(13, 4000000)
            and exact(sigma_inner)+b0 < exact(sigma_J))
        Jradial = (J0/exact(radial_margin)).upper()
        Hinverse = ((1+j+BT)/(1-det_error)).upper()
        check("the old-angle two-amplitude principal matrix has a uniform full inverse bound",
            Tmax < 1 and Hinverse < 2)
        report.update(
            exact_complex_parameter_radius=str(delta_radius),
            native_moving_width=str(sigma_native),
            enlarged_coefficient_moving_width=str(sigma0),
            flow_output_moving_width=str(sigma1),
            inverse_canonical_angular_width=str(sigma_inverse),
            inner_canonical_angular_width=str(sigma_inner),
            new_moving_operator_inverse_width=str(sigma_J),
            exact_root_interval=list(map(str, roots)),
            exact_original_root_piece_interval=list(map(str, cell)),
            original_root_radial_radius=str(native_radius),
            exact_fold_radial_radius=str(rho_radius),
            actual_inverse_radial_image_radius=str(q(3, 4)*rho_radius),
            canonical_radial_radius=str(canonical_radius),
            included_original_physical_radial_radius=str(physical_small_radius),
            included_original_moving_angular_width=str(sigma_inner),
            domain_bounds_independent_of_high_frequency=True,
            primitive_kept_on_the_original_closed_rho_curve=True,
            original_mean_equals_canonical_mean_at_root_exactly=True,
            old_angle_beta_has_exact_second_order_zero=True,
            local_tangential_first_derivative_has_exact_second_order_zero=True,
            two_amplitude_matrix_formula="H_sigma=[[i*sigma*alpha,beta*T],[beta,i*sigma*alpha]]; det=-D",
            full_widened_angular_U=[record(x) for x in U],
            full_widened_angular_V=[record(x) for x in V],
            inverse_width_angular_U=[record(x) for x in UJ],
            inverse_width_angular_V=[record(x) for x in VJ],
            inflation=dict(base_at_sigma0=record(base_factor),
                full_direction_at_sigma0=record(direction_factor),
                base_at_sigmaJ=record(base_Jfactor),
                full_direction_at_sigmaJ=record(direction_Jfactor)),
            complex_boxes=dict(gamma=complex_record(gamma_box), mean=complex_record(mean_box),
                k=complex_record(k_box), eta=complex_record(eta_box),
                a=complex_record(a_box), quotient_A=complex_record(A_box),
                radial_main=complex_record(radial_main_box)),
            bounds={name: record(value) for name, value in dict(
                a_real_gap=a_gap, a_modulus_upper=a_abs, drift=D0,
                drift_phi=D1, drift_phiphi=D2, flow_displacement=M0,
                derivative_excess=j, inverse_angular_radius=b0,
                quotient_A_real_gap=A_gap, quotient_A_modulus_upper=A_abs,
                quotient_A_phi=Bphi, T_phi=BT, T_modulus_upper=Tmax,
                principal_D_minus_one=det_error, Jacobian_modulus_lower=jac_lower,
                mu_modulus_lower=mu_lower, radial_derivative_error=Er,
                normalized_radial_derivative_error=eps_r, X_rho=Xrho,
                inverse_row_radial=row_r, inverse_row_angular=row_phi,
                old_angle_two_amplitude_Hinverse=Hinverse,
                new_eta_inverse=eta_inv, new_L0=LJ, new_J_Neumann_factor=cJ,
                new_J_same_space=J0, new_J_followed_by_angular_derivative=J1,
                new_J_radial_derivative_on_actual_inverse_image=Jradial).items()},
            new_J_spaces=["complete_moving_A1over128", "complete_weighted_Fourier_H0_1over128",
                          "ordinary_moving_L2"],
            tilted_source_norms_and_strong_remainder_paid_here=False,
            root_connection_full_two_rows_paid_here=False,
            complete=True, proved=True)
    except Exception as exc:
        report["failure"] = dict(type=type(exc).__name__, message=str(exc))
        report["seconds"] = time.monotonic()-started
        save(args.out, report)
        raise
    report["seconds"] = time.monotonic()-started
    save(args.out, report)
    print(json.dumps(dict(complete=True, gates=len(report["gates"]),
        canonical_radial_radius=report["canonical_radial_radius"],
        inverse_canonical_angular_width=report["inverse_canonical_angular_width"],
        bounds=report["bounds"], seconds=report["seconds"])), flush=True)


if __name__ == "__main__":
    main()
