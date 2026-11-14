#!/usr/bin/env python3
"""Full-frequency moving root inverse, all means and explicit-family fees.

This is a small genuine public Actions consumer. It does not rerun the
169 scalar germs or the whole response. It consumes the proved complex
root envelope, pays the exact continuous repair, and evaluates all 193
coefficients of the original root response cubic on that same domain.
No matrix truncation or physical-local replacement proves the inverse.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import io
import json
import math
import os
from pathlib import Path
import sys
import time

import flint
from flint import acb, arb, ctx
import numpy as np


PUBLIC = "Rogerhu12/math-research-public"
CANDIDATE = "ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
DEFINITION = "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
DIRECTION_DEFINITION = "6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
OBJECT = "91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848"
PINS = {
    "root_germ": "397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864",
    "repair": "6ee8b07fe94a8d9f87865a9ebb6650266b7eca792d435136ba533be92b1959fc",
    "direction": "87ed2f618bcaf77b0649abf561daea7225c9b7d667edc22afb91d86255da8f88",
    "trial_index": "ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6",
    "trial_shard": "ce29c19c81e77cb2f2ea9b70edc59af96a869116fa96e2e5375ffa4d61927917",
    "strip_proof": "dfb2a174a010d399775240b2bd07a0f547dfee5fc137e12141be9fd8a46e3854",
}
ROOT_SOURCE = "a3ad50b828c69d3e6f1e9254c1f266535171741ee2cd675d1569ef8f0fac0491"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    data = Path(path).read_bytes()
    if Path(path).suffix == ".gz":
        data = gzip.decompress(data)
    return json.loads(data)


def save(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = (json.dumps(data, indent=2, allow_nan=False)+"\n").encode()
    if path.suffix == ".gz":
        payload = gzip.compress(payload, mtime=0)
    temporary = path.with_name(path.name+".partial")
    temporary.write_bytes(payload)
    temporary.replace(path)


def exact(value):
    value = Fraction(value)
    return arb(value.numerator)/value.denominator


def dyadic(value):
    return Fraction.from_float(float(value))


def up(value):
    return abs(value).upper()


def upper(saved):
    return arb(saved["upper"]).upper()


def lower(saved):
    return arb(saved["lower"]).lower()


def record(value):
    value = arb(value)
    return dict(ball=value.str(50), lower=value.lower().str(50),
                upper=value.upper().str(50), mid_float=float(value.mid()),
                radius_upper_float=float(value.rad().upper()))


def norms(values, frequencies, width, maximum_order=4):
    weights = [(exact(width)*frequency).exp().upper()
               for frequency in frequencies]
    return [sum((up(value)*weight*frequency**order
                 for value, weight, frequency in zip(values, weights, frequencies)),
                arb(0)).upper() for order in range(maximum_order+1)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in PINS:
        parser.add_argument("--"+key.replace("_", "-"), type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("preserve every original root scalarization consumption")
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != PUBLIC):
        raise RuntimeError("the genuine public repository Actions job is required")
    runtime = dict(python=".".join(map(str, sys.version_info[:3])),
                   numpy=np.__version__, python_flint=flint.__version__)
    if runtime != dict(python="3.12.14", numpy="2.3.5", python_flint="0.9.0"):
        raise RuntimeError("the specified exact arithmetic runtime changed")
    ctx.prec = 256
    started = time.monotonic()
    report = dict(kind="complete_moving_current_root_scalarization_operator_budget",
        complete=False, proved=False, source_sha256=sha(__file__), runtime=runtime,
        public_repository=PUBLIC, public_run_id=os.environ.get("GITHUB_RUN_ID"),
        public_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        inputs={}, gates=[], failure=None,
        candidate_sha256=CANDIDATE, background_definition_sha256=DEFINITION,
        explicit_direction_definition_sha256=DIRECTION_DEFINITION,
        no_full_phase_transport_or_response_recomputed=True,
        actual_nonlocal_operator_retained=True, complete_even_mean_retained=True,
        only_original_response_shard005_is_consumed=True,
        other_response_shards_rebuilt_or_revalidated_here=False,
        full_frequency_inverse_not_a_finite_section=True,
        ordinary_source_retained_in_divergence_form=True,
        root_two_row_matching_proved_here=False,
        positive_high_input_graph_or_full_inverse_proved_here=False,
        actual_nonlinear_PDE_branch_or_response_proved_here=False,
        strong_return_remainder_or_complete_beta_proved_here=False)

    def check(name, okay):
        okay = bool(okay)
        report["gates"].append(dict(name=name, passed=okay))
        if not okay:
            raise ValueError("failed root scalarization gate: "+name)

    try:
        for key, expected in PINS.items():
            path = getattr(args, key)
            actual = sha(path)
            if actual != expected:
                raise ValueError("a pinned complete root input changed: "+key)
            report["inputs"][key] = dict(path=str(path), sha256=actual,
                                         bytes=path.stat().st_size)
        germ, repair, direction, index, strip = [read(getattr(args, key))
            for key in ("root_germ", "repair", "direction", "trial_index", "strip_proof")]
        check("the original complete complex germ and candidate identity are retained",
            germ["complete"] and germ["proved"] and germ["source_sha256"] == ROOT_SOURCE
            and germ["candidate_sha256"] == CANDIDATE and germ["object_sha256"] == OBJECT
            and germ["all_finite_candidate_modes_retained"]
            and germ["domain_contains_disks_about_every_true_parameter_root"])
        check("the exact continuous background and complete direction identities match",
            repair["complete"] and repair["derived_definition_sha256"] == DEFINITION
            and repair["candidate_sha256"] == CANDIDATE
            and direction["complete"] and direction["candidate_sha256"] == CANDIDATE
            and direction["background_definition_sha256"] == DEFINITION
            and direction["derived_direction_definition_sha256"] == DIRECTION_DEFINITION
            and direction["original_trial_sha256"] == PINS["trial_index"]
            and direction["exact_affine_offset"] == "0"
            and direction["actual_affine_parameter"] == "eta_0")
        metadata = index["metadata"]
        check("all193 physical response states and the true mean are in the original shard",
            index["kind"] == "complete_lossless_radial_cubic_shards_v1"
            and index["coefficient_shape"] == [4, 6144, 193]
            and metadata["role"] == "response_full" and metadata["modes"] == 96
            and metadata["physical_frequency_factor"] == 4
            and metadata["background_candidate_sha256"] == CANDIDATE
            and metadata["finite_head_mean_was_not_removed_from_the_solve"]
            and metadata["original_fourth_Robin_row_retained"]
            and metadata["coordinates"] == "physical unnormalized moving variation; h1 sine(4j phi), h2 cosine(4j phi) including its true mean")
        part = index["parts"][5]
        check("one original lossless shard has its exact declared range and byte hash",
            part["first_interval"] == 2265 and part["last_interval_exclusive"] == 2718
            and part["sha256"] == PINS["trial_shard"]
            and part["bytes"] == args.trial_shard.stat().st_size
            and part["file"] == args.trial_shard.name)
        with np.load(io.BytesIO(gzip.decompress(args.trial_shard.read_bytes())),
                     allow_pickle=False) as shard:
            nodes = shard["radial_nodes"].copy()
            coefficients = shard["piece_coefficients"].copy()
        check("the original response polynomial contains every root component",
            nodes.shape == (454,) and coefficients.shape == (4, 453, 193)
            and np.isfinite(nodes).all() and np.isfinite(coefficients).all()
            and (np.diff(nodes) > 0).all())
        piece = 2549
        local = piece-part["first_interval"]
        cell = [dyadic(nodes[local]), dyadic(nodes[local+1])]
        radius = Fraction(germ["complex_radial_radius"])
        width = Fraction(germ["moving_phi_strip"])
        roots = list(map(Fraction, germ["root_interval"]))
        rectangle = list(map(Fraction, germ["complex_radial_rectangle"]["real_interval"]))
        imaginary_radius = Fraction(germ["complex_radial_rectangle"]["imaginary_half_width"])
        scalar_cell = list(map(Fraction, germ["original_scalar_germ"]))
        check("the whole complex root disk lies on the same exact scalar and response piece",
            piece == germ["actual_candidate_piece"]
            and cell == list(map(Fraction, germ["exact_candidate_piece_interval"]))
            and radius == Fraction(1, 100000) and width == Fraction(1, 1024)
            and imaginary_radius == radius
            and rectangle == [roots[0]-radius, roots[1]+radius]
            and cell[0] < rectangle[0] < rectangle[1] < cell[1]
            and scalar_cell[0] < rectangle[0] < rectangle[1] < scalar_cell[1])
        check("the compact metric and intrinsic root are exactly independent of nu here",
            germ["compact_bump_identically_zero_on_entire_actual_germ"]
            and rectangle[0] > Fraction(9, 50))
        delta_radius = Fraction(1, 100000000)
        check("the actual selected R31 parameter is in the declared explicit-family disk",
            strip["complete"] and strip["true_explicit_family_parameter_conjugacy_proved"]
            and str(strip["public_run_id"]) == "43588332723"
            and strip["selected"]["actual_R31_gates_passed"]
            and upper(strip["selected"]["parameter_change"]) < exact(delta_radius)
            and strip["root_contract_sha256"] == "1910bdc2ee84cd23a7a92d94689d8cd90a3a5c25cf56caa3cc585159a9c5af43")
        base_offsets = list(map(Fraction,
            repair["special_piece_offsets"][str(piece)]["physical_offset"]))
        direction_repair = list(map(Fraction,
            direction["exact_complete_repair_coefficient_suprema"]))
        check("the actual root background offsets and all193 direction repair fees remain",
            len(base_offsets) == 65 and len(direction_repair) == 193
            and all(x >= 0 for x in direction_repair)
            and list(map(Fraction, repair["special_piece_offsets"][str(piece)]["interval"])) == cell)
        radial = acb(exact(rectangle[0]).union(exact(rectangle[1])),
                     arb(0, exact(imaginary_radius)))
        x = radial-acb(exact(cell[0]))
        zraw, zfull = [], []
        for component in range(193):
            value = acb(0)
            for degree in range(4):
                value = value*x+acb(exact(dyadic(coefficients[degree, local, component])))
            raw_bound = up(value)
            zraw.append(raw_bound)
            zfull.append((raw_bound+exact(direction_repair[component])).upper())
        uf = [4*j for j in range(1, 33)]
        vf = [0]+uf
        zuf = [4*j for j in range(1, 97)]
        zvf = [0]+zuf
        bu = norms([exact(abs(x)) for x in base_offsets[:32]], uf, width)
        bv = norms([exact(abs(x)) for x in base_offsets[32:]], vf, width)
        zu = norms(zfull[:96], zuf, width)
        zv = norms(zfull[96:], zvf, width)
        U = [(upper(germ["moving_U_derivative_Astrip"][t])+bu[t]
              +exact(delta_radius)*zu[t]).upper() for t in range(5)]
        V = [(upper(germ["moving_v_derivative_Astrip"][t])+bv[t]
              +exact(delta_radius)*zv[t]).upper() for t in range(5)]
        check("full repaired explicit-family angular bounds through four are finite",
            all(a.is_finite() for a in U+V+zu+zv) and len(zfull) == 193)
        intrinsic = germ["complex_intrinsic_coefficients"]
        b = upper(intrinsic["beta"]["modulus_upper"])
        K = upper(intrinsic["K"]["modulus_upper"])
        gamma = upper(intrinsic["gamma"]["modulus_upper"])
        gamma_gap = lower(intrinsic["gamma"]["real"])
        mfee = (exact(abs(base_offsets[32]))+exact(delta_radius)*zfull[96]).upper()
        mgap = (-upper(germ["moving_mean_v"]["real"])-mfee).lower()
        mmax = (upper(germ["moving_mean_v"]["modulus_upper"])+mfee).upper()
        check("the complete complex mean and gamma stay nonzero on the whole family disk",
            mgap > 0 and gamma_gap > 0)
        eta_inverse = (1/(mgap*gamma_gap)).upper()
        L = []
        for t in range(4):
            local_L = 2*b*sum((math.comb(t, i)*U[i]*V[t-i]
                               for i in range(t+1)), arb(0))
            primitive_L = b/2*sum((math.comb(t, i)*V[i+1]*U[t-i]
                                   for i in range(t+1)), arb(0))
            L.append((local_L+primitive_L).upper())
        c = (eta_inverse*L[0]/4).upper()
        check("the complete angular Neumann factor is strictly below3over20",
              c < exact(Fraction(3, 20)))
        J0 = (eta_inverse/(4*(1-c))).upper()
        J1 = (eta_inverse/(1-c)).upper()
        h = [J0]
        for l in range(4):
            h.append((eta_inverse*(1+sum((math.comb(l, t)*L[l-t]*h[t]
                                         for t in range(l+1)), arb(0)))).upper())
        B = [sum((math.comb(k+1, l)*h[l]**2
                  for l in range(k+2)), arb(0)).sqrt().upper() for k in range(4)]
        fractional = {
            "Hminus5over3_to_Hminus2over3": ((B[0].log()+2*B[1].log())/3).exp().upper(),
            "Hminus3over2_to_Hminus1over2": (B[0]*B[1]).sqrt().upper(),
            "Hminus2over3_to_Hplus1over3": B[0],
        }
        S = (U[0]**2+K*V[0]**2).upper()
        moving_d = (b*S/4).upper()
        moving_d1 = (b*S).upper()
        moving_d2 = (2*b*(U[0]*U[1]+K*V[0]*V[1])).upper()
        radial_J = (2*J0/exact(radius)).upper()
        drift_J = (J1*(2*moving_d+moving_d1/4)).upper()
        commutator = (radial_J+drift_J).upper()
        E = (b*(1+3*U[0]**2+K*V[0]**2)+b*U[1]*U[0]/2).upper()
        Bop = (b*(1+U[0]**2+3*K*V[0]**2)+b*K*V[1]*V[0]/2).upper()
        Czero = (2*b*U[0]*V[0]+b*U[1]*V[0]/2).upper()
        mean_terms = dict(
            z_reaction=(b*(1+S+2*K*mmax**2)).upper(),
            h1_functional=(2*b*mmax*U[0]).upper(),
            f_functional=(2*b*mmax*K*V[0]).upper(),
            ordinary_g2_mean=arb(1))
        lower_terms = dict(E=E, B=Bop, C_plus_eta_partial=Czero,
            b2=(Bop+gamma*U[1]).upper(), b1=(K*(Czero+gamma*V[1])).upper())
        check("all inverse Sobolev windows and complete mean source fees are finite",
            all(a.is_finite() for a in B+list(fractional.values())
                +list(mean_terms.values())+list(lower_terms.values())+[commutator]))
        report.update(
            actual_intrinsic_parameter="eta_0", exact_intrinsic_parameter=germ["exact_center_parameter"],
            whole_original_intrinsic_parameter_family_claimed=False,
            exact_complex_parameter_radius=str(delta_radius),
            exact_outer_radial_radius=str(radius), exact_inner_radial_radius=str(radius/2),
            exact_moving_Wiener_strip=str(width), exact_root_interval=list(map(str, roots)),
            exact_radial_rectangle=germ["complex_radial_rectangle"],
            exact_candidate_and_response_piece=piece, exact_piece_interval=list(map(str, cell)),
            original_response_shard_range=[2265, 2718], original_response_local_piece=local,
            response_raw_complete_coefficient_upper=[record(a) for a in zraw],
            response_repaired_complete_coefficient_upper=[record(a) for a in zfull],
            direction_angular_norms_u=[record(a) for a in zu],
            direction_angular_norms_v=[record(a) for a in zv],
            exact_background_root_offsets=list(map(str, base_offsets)),
            background_repair_angular_norms_u=[record(a) for a in bu],
            background_repair_angular_norms_v=[record(a) for a in bv],
            full_family_U_angular_norms=[record(a) for a in U],
            full_family_V_angular_norms=[record(a) for a in V],
            full_complex_mean_abs_lower=record(mgap), full_complex_mean_abs_upper=record(mmax),
            gamma_abs_lower=record(gamma_gap), gamma_abs_upper=record(gamma),
            beta_abs_upper=record(b), K_abs_upper=record(K), eta_inverse_abs_upper=record(eta_inverse),
            L_derivative_commutator_bounds=[record(a) for a in L],
            Neumann_factor=record(c), inverse_same_space=record(J0),
            inverse_followed_by_angular_derivative=record(J1),
            integer_derivative_recursion=[record(a) for a in h],
            integer_one_gain_Sobolev_bounds={str(k): record(a) for k, a in enumerate(B)},
            fractional_one_gain_Sobolev_bounds={k: record(a) for k, a in fractional.items()},
            inverse_radial_derivative_same_space_inner_disk=record(radial_J),
            inverse_radial_derivative_integer_one_gain_inner_disk={
                str(k): record((2*a/exact(radius)).upper()) for k, a in enumerate(B)},
            moving_d_Astrip=record(moving_d), moving_d_phi_Astrip=record(moving_d1),
            moving_d_phiphi_Astrip=record(moving_d2),
            inverse_drift_commutator_same_space=record(drift_J),
            full_D0_inverse_commutator_same_space_inner_disk=record(commutator),
            complete_lower_operators={k: record(a) for k, a in lower_terms.items()},
            complete_independent_mean_row={k: record(a) for k, a in mean_terms.items()},
            same_space_norms=["complete_A_sigma", "complete_H0_sigma", "ordinary_L2"],
            Sobolev_norm="sum_j (1+16j^2)^s exp(8|j|sigma) |fhat_j|^2",
            angular_zero_mode_removed_only_in_A_inverse=True,
            actual_independent_even_mean_preserved=True,
            all_projected_radial_and_drift_commutators_paid=True,
            radial_derivative_requires_inner_half_disk=True,
            actual_R31_selected_parameter_included=True,
            no_actual_PDE_background_transfer_inferred=True,
            complete=True, proved=True)
    except Exception as exc:
        report["failure"] = dict(type=type(exc).__name__, message=str(exc))
        report["seconds"] = time.monotonic()-started
        save(args.out, report)
        raise
    report["seconds"] = time.monotonic()-started
    save(args.out, report)
    print(json.dumps(dict(complete=report["complete"], gates=len(report["gates"]),
        Neumann_factor=report["Neumann_factor"], inverse_same_space=report["inverse_same_space"],
        seconds=report["seconds"])), flush=True)


if __name__ == "__main__":
    main()
