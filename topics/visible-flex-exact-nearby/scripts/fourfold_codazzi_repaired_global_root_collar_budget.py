#!/usr/bin/env python3
"""Certify the exact M32 repair in the full-global-reference root collar.

Public Actions only. Consume three immutable completed natives; no
transport, cubic shard, positive-body target or response is recomputed.
All full-band, mean, ordinary-source and two-endpoint fees are retained.
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
from flint import arb, ctx

PUBLIC = "Rogerhu12/math-research-public"
CANDIDATE = "ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
DEFINITION = "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
PINS = {
    "root_germ": "397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864",
    "repair": "6ee8b07fe94a8d9f87865a9ebb6650266b7eca792d435136ba533be92b1959fc",
    "root_budget": "10ff6db82cece6c72ae8a6726c07c188922cf6b307f5af5f50a691ade0abb33f",
}
ROOT_SOURCE = "a3ad50b828c69d3e6f1e9254c1f266535171741ee2cd675d1569ef8f0fac0491"
BUDGET_SOURCE = "4a3ee217b21cabda6ae3dea052f27ff82f03b4218294145dc2f812891688e03e"
REPAIR_SOURCE = "51a3f7968991ed85211b74c23befae7021bb192796daf0ae2d12ec5a1d45329b"


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


def record(value):
    value = arb(value)
    return dict(ball=value.str(60), lower=value.lower().str(60),
                upper=value.upper().str(60))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in PINS:
        parser.add_argument("--"+name.replace("_", "-"), type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("preserve the original repaired root-collar result")
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != PUBLIC):
        raise RuntimeError("the actual public repository Actions environment is required")
    runtime = dict(python=".".join(map(str, sys.version_info[:3])),
                   python_flint=flint.__version__)
    if runtime != dict(python="3.12.14", python_flint="0.9.0"):
        raise RuntimeError("the pinned Python and Arb runtime changed")
    ctx.prec = 256
    started = time.monotonic()
    report = dict(kind="exact_M32_repaired_global_positive_root_collar",
        complete=False, proved=False, source_sha256=sha(__file__), runtime=runtime,
        public_repository=PUBLIC, public_run_id=os.environ.get("GITHUB_RUN_ID"),
        public_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        candidate_sha256=CANDIDATE, background_definition_sha256=DEFINITION,
        actual_intrinsic_parameter="eta_0", exact_direction_parameter="0",
        centre_degree=32, complete_operator_band=64, inputs={}, gates=[],
        complete_even_mean_and_source_rows_retained=True,
        full_frequency_inverse_not_a_finite_section=True,
        ordinary_source_has_no_radial_derivative=True,
        raw_reference_identified_with_repaired_reference=False,
        source_role="ordinary L2_radial H^(1/3)_moving_angle",
        no_transport_shard_response_or_body_target_recomputed=True,
        full_delta_band192_collar_certified=False,
        actual_body_speed_outside_root_certified_here=False,
        full_regular_boundary_graph_transferred_here=False,
        root_reflection_finite_constant_or_strong_return_proved_here=False,
        nonlinear_PDE_branch_or_true_parameter_response_proved_here=False,
        failure=None)

    def check(name, okay, **details):
        passed = bool(okay)
        report["gates"].append(dict(name=name, passed=passed, **details))
        if not passed:
            raise ValueError("failed repaired global root-collar gate: "+name)

    try:
        for name, expected in PINS.items():
            path = getattr(args, name)
            actual = sha(path)
            if actual != expected:
                raise ValueError("immutable native changed: "+name)
            report["inputs"][name] = dict(path=str(path), sha256=actual,
                                           bytes=path.stat().st_size)
        germ, repair, rb = [read(getattr(args, name))
                           for name in ("root_germ", "repair", "root_budget")]
        check("the exact original complete root and repaired background identities match",
            germ["complete"] and germ["proved"] and germ["source_sha256"] == ROOT_SOURCE
            and germ["candidate_sha256"] == CANDIDATE
            and germ["all_finite_candidate_modes_retained"]
            and int(germ["exact_candidate_metadata"]["modes"]) == 32
            and repair["complete"] and repair["source_sha256"] == REPAIR_SOURCE
            and repair["candidate_sha256"] == CANDIDATE
            and repair["derived_definition_sha256"] == DEFINITION
            and repair["definition"]["modes"] == 32)
        check("the actual completed public root budget is retained without recomputation",
            rb["complete"] and rb["proved"] and rb["source_sha256"] == BUDGET_SOURCE
            and str(rb["public_run_id"]) == "43594466882"
            and rb["candidate_sha256"] == CANDIDATE
            and rb["background_definition_sha256"] == DEFINITION
            and rb["actual_intrinsic_parameter"] == "eta_0"
            and rb["exact_candidate_and_response_piece"] == 2549
            and all(item["passed"] for item in rb["gates"]))
        q = Fraction
        one, h, sqrt_h, N, centre = q(1), q(9, 10**6), q(3, 1000), q(97), q(32)
        roots = list(map(q, germ["root_interval"]))
        radius = q(germ["complex_radial_radius"])
        width = q(germ["moving_phi_strip"])
        cell = list(map(q, germ["exact_candidate_piece_interval"]))
        rectangle = list(map(q, germ["complex_radial_rectangle"]["real_interval"]))
        cut = q(1192029371497, 5000000000000)
        expected_roots = [q(1191984371497, 5000000000000),
                          q(2383968743003, 10000000000000)]
        check("the complete root-to-body collar stays inside the actual joint germ and one piece",
            roots == expected_roots and roots == list(map(q, rb["exact_root_interval"]))
            and radius == q(1, 100000) and width == q(1, 1024)
            and rectangle == [roots[0]-radius, roots[1]+radius]
            and cell[0] < rectangle[0] < roots[0] < roots[1]+h < rectangle[1] < cell[1]
            and germ["actual_candidate_piece"] == 2549
            and roots[1] < cut <= roots[0]+h
            and cut-roots[1] > q(8999, 10**9)
            and sqrt_h**2 == h)
        check("the intrinsic root is independent of compact nu on the whole collar",
            germ["compact_bump_identically_zero_on_entire_actual_germ"]
            and germ["domain_contains_disks_about_every_true_parameter_root"]
            and rectangle[0] > q(9, 50))
        offsets = list(map(q, rb["exact_background_root_offsets"]))
        original_offsets = list(map(q,
            repair["special_piece_offsets"]["2549"]["physical_offset"]))
        check("all65 exact M32 root repair coefficients and the true mean agree",
            len(offsets) == 65 and offsets == original_offsets
            and list(map(q, repair["special_piece_offsets"]["2549"]["interval"])) == cell
            and repair["piecewise_radial_derivative_correction"] ==
                "exactly zero on every open original cubic piece"
            and len(rb["background_repair_angular_norms_u"]) == 5
            and len(rb["background_repair_angular_norms_v"]) == 5)
        U = [(upper(germ["moving_U_derivative_Astrip"][j])
              +upper(rb["background_repair_angular_norms_u"][j])).upper()
             for j in range(5)]
        V = [(upper(germ["moving_v_derivative_Astrip"][j])
              +upper(rb["background_repair_angular_norms_v"][j])).upper()
             for j in range(5)]
        check("all complete base angular envelopes are finite and use no nonzero-delta band",
            all(value.is_finite() for value in U+V))
        intrinsic = germ["complex_intrinsic_coefficients"]
        beta = upper(intrinsic["beta"]["modulus_upper"])
        gamma = upper(intrinsic["gamma"]["modulus_upper"])
        gamma_lo = lower(intrinsic["gamma"]["real"])
        mgap = (-upper(germ["moving_mean_v"]["real"])-exact(abs(offsets[32]))).lower()
        mmax = (upper(germ["moving_mean_v"]["modulus_upper"])
                +exact(abs(offsets[32]))).upper()
        a_lo, a_hi = (gamma_lo*mgap).lower(), (gamma*mmax).upper()
        kr_lo, kr_hi = q("59.74380437"), q("60.465470")
        kmax = q(61, 100000)
        check("the repaired optical speed and actual intrinsic root derivative are strict",
            gamma_lo > 0 and mgap > 0 and a_lo > exact(q(1, 2))
            and a_hi < exact(q(63, 50))
            and beta < exact(q(211, 1000))
            and lower(intrinsic["K1"]["real"]) > exact(kr_lo)
            and upper(intrinsic["K1"]["modulus_upper"]) < exact(kr_hi)
            and kr_hi*h < kmax and kmax < q(1, 1600)
            and kr_lo/q(63, 50) > 29 and kr_hi/q(1, 2) < 122)
        K = exact(kmax)
        S = (U[0]**2+K*V[0]**2).upper()
        d1 = (beta*S).upper()
        d0 = (d1/4).upper()
        A = (beta*(1+3*U[0]**2+K*V[0]**2)).upper()
        E = (beta*(1+U[0]**2+3*K*V[0]**2)).upper()
        B = (2*beta*U[0]*V[0]).upper()
        local = (A+E+(1+K)*B).upper()
        nonlocal_raw = (beta*(U[1]+V[1])*(U[0]+K*V[0])/2).upper()
        mean_rank = (gamma*(U[1]+K*V[1])).upper()
        dyad = ((U[1]+4*V[1])*(U[0]+V[0])).upper()
        report["fresh_coefficient_bounds"] = {name: record(value)
            for name, value in dict(mean_gap=mgap, mean_modulus=mmax,
                optical_speed_lower=a_lo, optical_speed_upper=a_hi, beta=beta,
                gamma=gamma, d=d0, dphi=d1, local_A=A, local_E=E,
                local_B_and_C=B, raw_local=local, full_primitive=nonlocal_raw,
                independent_mean_rank=mean_rank, global_frame_dyad=dyad).items()}
        report["base_angular_U"] = [record(value) for value in U]
        report["base_angular_V"] = [record(value) for value in V]
        check("new complete local reaction and drift satisfy the sharp M32 thresholds",
            A < exact(q(1, 2)) and E < exact(q(3, 10)) and B < exact(q(1, 2))
            and d1 < exact(q(9, 100)) and d0 < exact(q(11, 500)))
        check("full primitive and true mean rank plus global-frame dyad remain paid",
            local < 2 and nonlocal_raw < 1 and mean_rank < 3 and dyad < 34)
        right_mean_offset = abs(q(repair["exact_right_mean_offset"]))
        right_offset = list(map(q, repair["exact_right_physical_offset"]))
        check("the true repaired outer scalar reference lies strictly between1over8and1over5",
            len(right_offset) == 65 and abs(right_offset[32]) == right_mean_offset
            and q("5.84461145233") > right_mean_offset
            and (one-one/(2*800000**2))/(7+right_mean_offset) > q(1, 8)
            and one/(q("5.84461145233")-right_mean_offset) < q(1, 5))
        optical_min = h/2
        free_trial = q(20)+q(122, 6400)
        check("new global reference root variational trial gives66without any body-length fee",
            q(66) > free_trial and
            (q(66)-free_trial)**2 * 40 * q(8, 3) * optical_min > 1)
        check("both root Airy rows and all neighbouring-frequency constants are paid",
            q(3) < 67 and q(66)**2+3 < q(67)*67 and 67 < 81
            and N >= 2*centre and 4*N > 64
            and q(5, 3)**3 * 4 < 27 and q(5, 3)**3 * 32 < 216
            and 8 < 9 and 366 < 8**3 and q(21, 40) < 1)
        dA, reaction, FN, bmax = q(9, 100), q(33, 10), q(34), q(211, 1000)
        high_E = q(13, 2)*dA+2*reaction+24*centre*reaction/N+4*bmax*FN/(N-centre)
        check("new entire unbounded high operator closes strictly below1over3000",
            high_E < 34 and h*high_E < q(1, 3000))
        ih = q(3000, 2999)
        GH, PH, TH, QH = q(41, 500000), q(901, 100000), q(271, 10000), q(1061, 250)
        check("full high ordinary-source and incoming-port state bounds close",
            9*ih*h < GH and 3*ih*sqrt_h < PH)
        check("complete high incoming-and-outgoing raw trace bounds close",
            9*ih*sqrt_h < TH and 9*(1+ih**2) < QH**2)
        AHL, ALH, AHthird = q(23, 2), q(58, 5), q(207, 2)
        low_generator = 384*q(63, 50)+384*q(11, 500)+2+1+3
        check("entire M32 head-high crossings and all193 low coordinates are bounded",
            384*q(11, 500)+2+1 < AHL
            and 384*q(11, 500)+q(9, 100)+2+1 < ALH
            and 1+640**2 < 9**6 and 9*AHL == AHthird
            and low_generator < 500)
        EL = q(201, 200)
        check("actual radial head Cauchy operator has the stated all-radial Green bound",
            500*h < 1 and one/(one-500*h) < EL)
        GL, PL = h*EL, sqrt_h*EL
        loop = GL*ALH*GH*AHthird
        check("new complete193head and unbounded high feedback closes below1e-6",
            loop < q(1, 10**6))
        il = q(10**6, 10**6-1)
        ell = [il*GL, il*GL*ALH*GH, il*PL, il*GL*ALH*PH]
        high = [GH*AHthird*ell[0], GH*(1+AHthird*ell[1]),
                GH*AHthird*ell[2], PH+GH*AHthird*ell[3]]
        source_square = sum((row[j]**2 for row in (ell, high) for j in (0, 1)), q(0))
        port_square = sum((row[j]**2 for row in (ell, high) for j in (2, 3)), q(0))
        check("new complete all-frequency ordinary-source-to-state1over12000",
            source_square < q(1, 12000)**2)
        check("new complete all-frequency incoming-port-to-state1over100",
            port_square < q(1, 100)**2)
        low_trace = [sqrt_h*EL*(1+ALH*high[0]), sqrt_h*EL*ALH*high[1],
                     EL+sqrt_h*EL*ALH*high[2], sqrt_h*EL*ALH*high[3]]
        high_trace = [TH*AHthird*ell[0], TH*(1+AHthird*ell[1]),
                      TH*AHthird*ell[2], QH+TH*AHthird*ell[3]]
        left_trace = [q(0), q(0), q(1), q(0)]
        trace_source_square = sum((row[j]**2 for row in (left_trace, low_trace, high_trace)
                                   for j in (0, 1)), q(0))
        trace_port_square = sum((row[j]**2 for row in (left_trace, low_trace, high_trace)
                                 for j in (2, 3)), q(0))
        check("new complete two-end ordinary-source-to-trace1over36",
            trace_source_square < q(1, 36)**2)
        check("new both-end full-state incoming-port-to-trace9over2",
            trace_port_square < q(9, 2)**2)
        check("orders0to2 retain the same high inverse with full transport commutators",
            h*(34+2*dA) < q(1, 3000))
        C1, C21, C20 = 256*(34+dA/2), 512*(34+dA), 256**2*(34+dA/2)
        fresh_reaction = (A+E+5*B).upper()
        fresh_E = (exact(q(13, 2))*d1+2*fresh_reaction
                   +exact(24*centre/N)*fresh_reaction
                   +4*beta*dyad/exact(N-centre)).upper()
        report.update(
            exact_root_interval=list(map(str, roots)), exact_original_piece_interval=list(map(str, cell)),
            exact_root_to_body_cut=str(cut), exact_maximum_collar_length=str(h),
            exact_root_offsets=list(map(str, offsets)), exact_right_mean_offset=str(q(repair["exact_right_mean_offset"])),
            exact_moving_Wiener_strip=str(width), no_join_inside_actual_root_collar=True,
            fresh_full_high_remainder_upper=record(fresh_E),
            uniform_positive_extension_reference=dict(
                domain="[the true intrinsic root,25/8]", speed="new repaired -gamma*m on the actual root collar",
                allowed_outside_root="any positive bounded frequency-independent radial extension",
                forward_root_value="M^(-1/3)", backward_outer_value="q_*/(-m_R^0)",
                same_reference_at_body_cut=True, positive_body_speed_gate_is_separate=True,
                root_backward_value_upper="66 M^(-1/3)", both_root_Airy_rows_factor="9"),
            exact_rational_contract=dict(
                high_E_upper=str(high_E), high_contraction_upper=str(h*high_E),
                high_resolvent=str(ih), high_source_state=str(GH), high_port_state=str(PH),
                high_source_trace=str(TH), high_port_trace=str(QH),
                low_generator_upper=str(low_generator), low_propagator_upper=str(EL),
                low_Green_upper=str(GL), low_Poisson_upper=str(PL),
                low_to_high_L2=str(AHL), high_to_low_L2=str(ALH), low_to_high_Hthird=str(AHthird),
                complete_head_feedback=str(loop), full_head_resolvent=str(il),
                input_order=["source_low_L2", "source_high_Hthird", "low_root_Cauchy_ports", "high_two_incoming_ports"],
                state_response_matrix=[list(map(str, ell)), list(map(str, high))],
                trace_response_matrix=[list(map(str, row)) for row in (left_trace, low_trace, high_trace)],
                state_source_squared_Frobenius=str(source_square), state_port_squared_Frobenius=str(port_square),
                trace_source_squared_Frobenius=str(trace_source_square), trace_port_squared_Frobenius=str(trace_port_square),
                ordinary_source_to_full_state="1/12000", incoming_ports_to_full_state="1/100",
                ordinary_source_to_both_full_traces="1/36", incoming_ports_to_both_full_traces="9/2"),
            angular_bootstrap=dict(orders=[0, 1, 2], same_high_resolvent=str(ih),
                entire_absolute_kernel_bound="34", C1=str(C1), C21=str(C21), C20=str(C20),
                ordinary_source="H^(j+1/3) in moving angle; no radial derivative",
                full_head_forcing="(207/2)*641^j times the base full-head L2 norm",
                same_width_analytic_inverse_claimed=False, negative_Sobolev_root_inverse_claimed=False),
            complete=True, proved=True)
    except Exception as exc:
        report["failure"] = dict(type=type(exc).__name__, message=str(exc))
        report["seconds"] = time.monotonic()-started
        save(args.out, report)
        raise
    report["seconds"] = time.monotonic()-started
    save(args.out, report)
    print(json.dumps(dict(complete=True, gates=len(report["gates"]),
        fresh_full_high_remainder_upper=report["fresh_full_high_remainder_upper"],
        exact_rational_contract=report["exact_rational_contract"],
        seconds=report["seconds"])), flush=True)


if __name__ == "__main__":
    main()
