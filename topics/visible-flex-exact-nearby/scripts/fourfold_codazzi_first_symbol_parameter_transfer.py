#!/usr/bin/env python3
"""Transfer the complete first-symbol finite part to the actual R31 parameter.

Only saved full scalar Taylor identities and completed public certificates
are consumed. No phase, intrinsic germ, candidate, response, or root Newton
step is regenerated. Numerical execution is restricted to public Actions.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import time

import flint
from flint import acb, arb, ctx

PUBLIC = "Rogerhu12/math-research-public"
CANDIDATE = "ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
CENTRE = "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
DIRECTION = "6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
NU = Fraction(-2572625729470897, 72057594037927936)
RADIUS = Fraction(1, 100000000)
ROOT_RADIUS = Fraction(1, 100000)
CUT = Fraction(76285779072683, 320000000000000)
WIDTH_GOAL = Fraction(1, 10000)
PINS = {
    "finite_part": "cd9ffed6d8c9e107eaac2b50f1846219d8ec90a130555bb91859d465c9bab202",
    "scalar_cover": "94492bbafda1e5efb30b129e534171c9fc305524a2d972064e34e8894948bad3",
    "t_cache": "ab5e8156fbaf50c80e944a15d68858d29419229e7ae10665b432cd1af593587d",
    "direction": "87ed2f618bcaf77b0649abf561daea7225c9b7d667edc22afb91d86255da8f88",
    "root_budget": "10ff6db82cece6c72ae8a6726c07c188922cf6b307f5af5f50a691ade0abb33f",
    "root_germ": "397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864",
    "strip_proof": "dfb2a174a010d399775240b2bd07a0f547dfee5fc137e12141be9fd8a46e3854",
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith(".gz") else raw)


def save(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(data, indent=2, allow_nan=False)+"\n").encode()
    if str(path).endswith(".gz"):
        raw = gzip.compress(raw, mtime=0)
    temporary = path.with_name(path.name+".tmp")
    temporary.write_bytes(raw)
    os.replace(temporary, path)


def exact(value):
    value = Fraction(value)
    return arb(value.numerator)/value.denominator


def interval(left, right):
    return exact(left).union(exact(right))


def box(saved):
    # The serialized lower/upper strings may themselves contain Arb
    # display radii. Consume them outward; never use a saved float.
    return arb(saved["lower"]).lower().union(arb(saved["upper"]).upper())


def upper(saved):
    return arb(saved["upper"]).upper()


def lower(saved):
    return arb(saved["lower"]).lower()


def up(value):
    return abs(value).upper()


def record(value):
    value = arb(value)
    return dict(ball=value.str(60), lower=value.lower().str(60),
                upper=value.upper().str(60))


def restrict(row, name, left, right, derivative=0):
    """Differentiate the saved complete degree-seven Taylor identity."""
    a, b = map(Fraction, row["interval"])
    center = Fraction(row["center"])
    j = int(derivative)
    if not a <= left <= right <= b or not 0 <= j <= 7:
        raise ValueError("a scalar restriction leaves its original full cell")
    model = row["models"][name]
    c = list(map(Fraction, model["exact_centered_polynomial"]))
    point = [box(z) for z in model["point_jets"]]
    whole7 = box(model["whole_final_derivative"])
    if len(c) != 8 or len(point) != 7:
        raise ValueError("the complete degree-seven identity is required")
    h = exact(max(abs(left-center), abs(right-center)))
    fee = sum((math.factorial(k)//math.factorial(k-j)
               *abs(point[k]-exact(c[k]))*h**(k-j)
               for k in range(j, 7)), arb(0))
    fee += abs(whole7-math.factorial(7)*exact(c[7]))*h**(7-j)/math.factorial(7-j)
    coefficients = [Fraction(math.factorial(k), math.factorial(k-j))*c[k]
                    for k in range(j, 8)]
    x, value = interval(left-center, right-center), arb(0)
    for coefficient in reversed(coefficients):
        value = value*x+exact(coefficient)
    return value+arb(0, fee.upper())


def bump_bounds(left, right):
    a, b = Fraction(1, 20), Fraction(9, 50)
    if right <= a or left >= b:
        return False, arb(0), arb(0), arb(0)
    if not a <= left < right <= b:
        raise ValueError("an accepted scalar cell crosses a true bump endpoint")
    t = interval((left-a)/(b-a), (right-a)/(b-a))
    # w<=1 is the exact polynomial maximum on [0,1].
    w = arb(1)
    wp = exact(Fraction(24576)/(b-a))*t**5*(1-t)**5*(1-2*t)
    wpp = (exact(Fraction(24576)/(b-a)**2)*t**4*(1-t)**4
           *(5*(1-2*t)**2-2*t*(1-t)))
    return True, w, wp, wpp


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topic", type=Path, required=True)
    for key in PINS:
        parser.add_argument("--"+key.replace("_", "-"), type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != PUBLIC):
        raise RuntimeError("run mathematics only in the public repository Actions")
    runtime = dict(python=platform.python_version(),
                   python_flint=str(flint.__version__))
    if runtime != dict(python="3.12.14", python_flint="0.9.0"):
        raise RuntimeError("the declared exact Python/Arb runtime is required")
    ctx.prec = 256
    started = time.monotonic()
    report = dict(
        kind="complete_first_symbol_finite_part_parameter_transfer",
        complete=False, transfer_enclosure_complete=False, runtime=runtime,
        source_sha256=sha(__file__), public_repository=PUBLIC,
        public_run_id=os.environ.get("GITHUB_RUN_ID"),
        public_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        candidate_sha256=CANDIDATE, continuous_background_definition_sha256=CENTRE,
        explicit_direction_definition_sha256=DIRECTION,
        actual_affine_parameter="eta_0", exact_affine_offset="0",
        whole_original_eta=False, exact_nu=str(NU),
        exact_complex_parameter_radius=str(RADIUS),
        exact_strict_cut=str(CUT), requested_transfer_fee_goal=str(WIDTH_GOAL),
        original169_scalar_germs_recomputed=False,
        original3146_strict_integrals_recomputed=False,
        original_two_root_Newton_steps_recomputed=False,
        original_phase_transport_or_full_response_recomputed=False,
        only_complete_parameter_derivative_bounds_are_new=True,
        full193_direction_and_independent_even_mean_retained=True,
        finite_part_subtractions_differentiated_before_integrating=True,
        full_return_beta_identification_not_claimed=True,
        root_two_row_matching_or_strong_return_remainder_not_paid=True,
        actual_PDE_background_transfer_and_full_inverse_not_paid=True,
        inputs={}, gates=[], rows=[], scalar_inputs=[], failure=None)

    def checkpoint(stage):
        report.update(stage=stage, seconds=time.monotonic()-started)
        save(args.out, report)

    def check(name, passed):
        passed = bool(passed)
        report["gates"].append(dict(name=name, passed=passed))
        if not passed:
            raise ArithmeticError(name)

    checkpoint("started")
    try:
        docs = {}
        for key, expected in PINS.items():
            path = getattr(args, key)
            if sha(path) != expected:
                raise ValueError("a completed exact public input changed: "+key)
            docs[key] = read(path)
            report["inputs"][key] = dict(path=str(path), sha256=expected,
                                         bytes=path.stat().st_size)
        fp, cover, tc, direction, rb, germ, strip = (
            docs[key] for key in ("finite_part", "scalar_cover", "t_cache",
                                 "direction", "root_budget", "root_germ", "strip_proof"))
        check("the completed same-centre v2 finite part and its full3146 partition are reused",
              fp["complete"] and fp["finite_part_enclosure_complete"]
              and str(fp["public_run_id"]) == "43591721337"
              and fp["source_sha256"] == "851a86d3b7745d45246adbc52060287126e1eb99733e73c498c2ba01b0547a4c"
              and fp["candidate_sha256"] == CANDIDATE
              and fp["continuous_centre_definition_sha256"] == CENTRE
              and fp["actual_affine_parameter"] == "eta_0"
              and fp["exact_affine_offset"] == "0"
              and Fraction(fp["exact_nu"]) == NU
              and fp["explicit_family_parameter_delta"] == "0"
              and Fraction(fp["exact_strict_cut"]) == CUT
              and len(fp["rows"]) == fp["accepted_strict_rows"] == 3146
              and fp["original_root_newton_steps_reused"] == 2)
        check("the original169 complete scalar germs and all220 compact T models have the same identity",
              cover["complete"] and cover["exact_affine_offset"] == "0"
              and Fraction(cover["configuration"]["exact_nu"]) == NU
              and len(cover["germs"]) == 169 and cover["accepted_cell_count"] == 626
              and tc["complete"] and tc["compact_T_complete"]
              and tc["cover_sha256"] == PINS["scalar_cover"]
              and tc["exact_affine_offset"] == "0"
              and tc["compact_T_exact_interval"] == ["1/20", "9/50"]
              and len(tc["compact_T_models"]) == 220)
        check("the complete repaired explicit direction retains all193 components and the independent mean",
              direction["complete"] and direction["candidate_sha256"] == CANDIDATE
              and direction["background_definition_sha256"] == CENTRE
              and direction["derived_direction_definition_sha256"] == DIRECTION
              and direction["scalar_cover_sha256"] == PINS["scalar_cover"]
              and direction["actual_affine_parameter"] == "eta_0"
              and direction["exact_affine_offset"] == "0"
              and len(direction["complete_negative_interval_direction_coefficient_suprema"]) == 193
              and len(direction["exact_complete_repair_coefficient_suprema"]) == 193
              and Fraction(direction["exact_phase_interval"][0]) == 0
              and Fraction(direction["exact_phase_interval"][1]) >= CUT)
        check("the actual public root budget covers the full complex parameter disk and the same repaired centre",
              rb["complete"] and rb["proved"]
              and str(rb["public_run_id"]) == "43594466882"
              and rb["source_sha256"] == "4a3ee217b21cabda6ae3dea052f27ff82f03b4218294145dc2f812891688e03e"
              and rb["candidate_sha256"] == CANDIDATE
              and rb["background_definition_sha256"] == CENTRE
              and rb["explicit_direction_definition_sha256"] == DIRECTION
              and rb["actual_intrinsic_parameter"] == "eta_0"
              and Fraction(rb["exact_complex_parameter_radius"]) == RADIUS
              and Fraction(rb["exact_outer_radial_radius"]) == ROOT_RADIUS
              and Fraction(rb["exact_moving_Wiener_strip"]) == Fraction(1, 1024)
              and len(rb["response_repaired_complete_coefficient_upper"]) == 193)
        parameter = upper(strip["selected"]["parameter_change"])
        check("the actual selected true R31 parameter lies inside this exact explicit-family disk",
              strip["complete"] and strip["true_explicit_family_parameter_conjugacy_proved"]
              and str(strip["public_run_id"]) == "43588332723"
              and strip["selected"]["actual_R31_gates_passed"]
              and strip["root_contract_sha256"] == "1910bdc2ee84cd23a7a92d94689d8cd90a3a5c25cf56caa3cc585159a9c5af43"
              and parameter > 0 and parameter < exact(RADIUS))
        rootlo, roothi = map(Fraction, fp["actual_eta0_root_enclosure"])
        oldlo, oldhi = map(Fraction, germ["root_interval"])
        check("the unchanged unique root and exact compact support justify the whole root homotopy",
              germ["complete"] and germ["compact_bump_identically_zero_on_entire_actual_germ"]
              and germ["domain_contains_disks_about_every_true_parameter_root"]
              and list(map(Fraction, fp["original_unique_root_enclosure"])) == [oldlo, oldhi]
              and oldlo <= rootlo < roothi <= oldhi
              and Fraction(9, 50) < CUT < rootlo
              and roothi-CUT < ROOT_RADIUS/2)
        radius = exact(RADIUS)
        norm = direction["complete_joint_Wiener_homogeneous_angular_derivative_norms"]["1/64"]
        Zu, Zu1 = (upper(norm[str(j)]["direction_xi"]) for j in (0, 1))
        Zv, Zv1 = (upper(norm[str(j)]["direction_zeta"]) for j in (0, 1))
        U, U1 = ((upper(norm[str(j)]["base_u"])+radius*z).upper()
                  for j, z in ((0, Zu), (1, Zu1)))
        V, V1 = ((upper(norm[str(j)]["base_v"])+radius*z).upper()
                  for j, z in ((0, Zv), (1, Zv1)))
        Zm = upper(direction["complete_direction_mean_abs_upper"])
        M = (lower(direction["complete_base_mean_abs_lower"])-radius*Zm).lower()
        check("the full complex strict-interval mean is separated and all field norms are finite",
              M > 0 and all(x.is_finite() for x in (U, U1, V, V1, Zu, Zu1, Zv, Zv1, Zm)))
        report["strict_complete_global_field_bounds"] = {
            k: record(v) for k, v in dict(U=U, U1=U1, V=V, V1=V1,
                Zu=Zu, Zu1=Zu1, Zv=Zv, Zv1=Zv1, Zm=Zm, mean_gap=M).items()}
        scalar_rows = []
        scalar_cursor = Fraction(0)
        topic = args.topic.resolve()
        for index, entry in enumerate(cover["germs"]):
            path = (topic/entry["path"]).resolve()
            if (not path.is_relative_to(topic) or sha(path) != entry["sha256"]
                    or entry["germ_index"] != index):
                raise ValueError("an original chronological scalar germ changed")
            doc = read(path)
            if not doc["complete"] or doc["configuration"] != cover["configuration"]:
                raise ValueError("an original scalar germ is not the complete fixed configuration")
            for row in doc["rows"]:
                left, right = map(Fraction, row["interval"])
                if left != scalar_cursor or not left < right:
                    raise ValueError("the complete626 scalar partition has a gap")
                scalar_rows.append((left, right, entry["sha256"], row))
                scalar_cursor = right
            report["scalar_inputs"].append(dict(germ_index=index, path=entry["path"],
                                                 sha256=entry["sha256"], bytes=path.stat().st_size))
        check("all169 original scalar files give the complete chronological626 cells",
              len(scalar_rows) == 626
              and scalar_cursor == Fraction(cover["exact_complete_interval"][1])
              and scalar_cursor > CUT)
        Trows = {tuple(map(Fraction, row["interval"])): row for row in tc["compact_T_models"]}
        if len(Trows) != 220:
            raise ValueError("duplicate complete compact T cells")
        Tcursor = Fraction(1, 20)
        for left, right in sorted(Trows):
            if left != Tcursor or not left < right:
                raise ValueError("the complete compact T partition has a gap")
            Tcursor = right
        if Tcursor != Fraction(9, 50):
            raise ValueError("the compact T partition misses its exact endpoint")
        cursor, scalar_index, used_T = Fraction(0), 0, set()
        Lstrict, min_w = arb(0), None
        for index, old in enumerate(fp["rows"]):
            left, right = map(Fraction, old["interval"])
            if left != cursor or not left < right <= CUT:
                raise ValueError("the original3146 accepted integral partition changed")
            while scalar_index < len(scalar_rows) and scalar_rows[scalar_index][1] <= left:
                scalar_index += 1
            a, b, scalar_sha, row = scalar_rows[scalar_index]
            if not a <= left < right <= b or old["scalar_native_sha256"] != scalar_sha:
                raise ValueError("an accepted integral lost its exact scalar-germ membership")
            K = restrict(row, "K", left, right)
            Q, Q1 = -K, up(restrict(row, "K", left, right, 1))
            beta = up(restrict(row, "beta", left, right))
            gamma = restrict(row, "gamma", left, right)
            Qlo, Qhi, gamma_gap = Q.lower(), Q.upper(), gamma.lower()
            supported, H0, wp, wpp = bump_bounds(left, right)
            if supported:
                tr = Trows[(a, b)]
                if tr["scalar_native_sha256"] != scalar_sha:
                    raise ValueError("the complete compact T row changed scalar identity")
                T, T1 = restrict(tr, "T", left, right), restrict(tr, "T", left, right, 1)
                kappa0, kappa1 = up(T*wp), up(T1*wp+T*wpp)
                H1, H2 = up(wp), up(wpp)
                used_T.add((a, b))
            else:
                H1 = H2 = kappa0 = kappa1 = arb(0)
            Wlo, Whi = (Qlo-radius*kappa0).lower(), (Qhi+radius*kappa0).upper()
            if not Qlo > 0 or not gamma_gap > 0 or not Wlo > 0:
                raise ArithmeticError("a true complete strict square-root or gamma gap was lost")
            min_w = Wlo if min_w is None or Wlo < min_w else min_w
            exponential = (radius*H0).exp()
            qplus = (radius*H0/2).exp()*Whi.sqrt()
            Qdelta = exponential*Whi
            Qdot = exponential*(kappa0+H0*Whi)
            Lambda = radius*H1/4+(Q1+radius*kappa1)/(4*Wlo)
            Lambdadot = H1/4+(kappa0*Q1+kappa1*Qhi)/(4*Wlo**2)
            L = Lambda+beta*(1+U**2+Qdelta*V**2)
            Ldot = Lambdadot+beta*(2*U*Zu+Qdot*V**2+2*Qdelta*V*Zv)
            J = 1/(gamma_gap*M*Wlo.sqrt())
            jlog = Zm/M+kappa0/(2*Wlo)
            ratio = exponential*Whi.sqrt()/(gamma_gap*M)
            rlog = H0+kappa0/(2*Wlo)+Zm/M
            qlog = (H0+kappa0/Wlo)/2
            cross = U*V1+V*U1
            crossdot = Zu*V1+U*Zv1+Zv*U1+V*Zu1
            first = J*(2*L*Ldot+L**2*jlog)
            second = 4*beta**2*ratio*(U**2*V**2*rlog+2*U*Zu*V**2+2*U**2*V*Zv)
            third = 2*beta*qplus*(crossdot+qlog*cross)
            derivative = (first+second+third).upper()
            contribution = (exact(right-left)*derivative).upper()
            if not derivative.is_finite() or not contribution.is_finite():
                raise ArithmeticError("a complete strict parameter derivative is not finite")
            Lstrict += contribution
            report["rows"].append(dict(
                original_accepted_integral_index=index, interval=[str(left), str(right)],
                scalar_native_sha256=scalar_sha, original_scalar_interval=[str(a), str(b)],
                compact_support=supported, complete_W_positive_gap=record(Wlo),
                complete_gamma_positive_gap=record(gamma_gap),
                complete_kappa_abs_upper=record(kappa0), complete_kappa_prime_abs_upper=record(kappa1),
                complete_bump_prime_abs_upper=record(H1), complete_bump_second_abs_upper=record(H2),
                first_term_parameter_derivative=record(first.upper()),
                second_term_parameter_derivative=record(second.upper()),
                third_term_parameter_derivative_no_eta_denominator=record(third.upper()),
                full_parameter_derivative_A0=record(derivative),
                integrated_complete_parameter_derivative=record(contribution)))
            cursor = right
            if index % 128 == 0 or index+1 == len(fp["rows"]):
                report.update(completed_strict_rows=len(report["rows"]),
                              exact_completed_strict_prefix=str(cursor),
                              complete_strict_parameter_derivative=record(Lstrict.upper()))
                checkpoint("strict-parameter-prefix")
                print(dict(stage="strict-parameter", rows=index+1,
                           derivative_integral=Lstrict.str(16)), flush=True)
        Lstrict = Lstrict.upper()
        check("all3146 accepted intervals and all220 supported T cells are fully consumed",
              cursor == CUT and len(report["rows"]) == 3146 and len(used_T) == 220)
        report["minimum_complete_strict_W_gap"] = record(min_w)
        intrinsic = germ["complex_intrinsic_coefficients"]
        K1 = acb(box(intrinsic["K1"]["real"]), box(intrinsic["K1"]["imag"]))
        kgap = lower(intrinsic["K1"]["real"])
        kmax = upper(intrinsic["K1"]["modulus_upper"])
        Mk = up(K1-60)
        rootU, rootU1 = (upper(rb["full_family_U_angular_norms"][j]) for j in (0, 1))
        rootV, rootV1 = (upper(rb["full_family_V_angular_norms"][j]) for j in (0, 1))
        rootZu, rootZu1 = (upper(rb["direction_angular_norms_u"][j]) for j in (0, 1))
        rootZv, rootZv1 = (upper(rb["direction_angular_norms_v"][j]) for j in (0, 1))
        rootZm = upper(rb["response_repaired_complete_coefficient_upper"][96])
        rootM = lower(rb["full_complex_mean_abs_lower"])
        eta_inverse = upper(rb["eta_inverse_abs_upper"])
        beta = upper(rb["beta_abs_upper"])
        zlog = rootZm/rootM
        rootcrossdot = rootZu*rootV1+rootU*rootZv1+rootZv*rootU1+rootV*rootZu1
        Hlo, Hhi = exact(rootlo-CUT).lower(), exact(roothi-CUT).upper()
        check("the complete root analytic gaps remain positive on every candidate Cauchy disk",
              kgap > 0 and rootM > 0 and Hlo > 0 and Hhi < exact(ROOT_RADIUS/2)
              and all(x.is_finite() for x in (Mk, kmax, eta_inverse, zlog, rootcrossdot)))
        candidates = []
        for factor in (Fraction(1, 2), Fraction(3, 4), Fraction(7, 8), Fraction(15, 16)):
            R0 = exact(ROOT_RADIUS*factor)
            cauchy_k_derivative = Mk/exact(ROOT_RADIUS*(1-factor))
            astar = cauchy_k_derivative/(4*kgap)+beta*(1+rootU**2+R0*kmax*rootV**2)
            adot = 2*beta*(rootU*rootZu+R0*kmax*rootV*rootZv)
            MA = eta_inverse*zlog/(16*kgap.sqrt())
            MB = eta_inverse*(adot+astar*zlog)/(2*kgap.sqrt())
            MC = eta_inverse*(2*astar*adot+astar**2*zlog)/kgap.sqrt()
            MD = (4*beta**2*kmax.sqrt()*eta_inverse
                  *(rootU**2*rootV**2*zlog+2*rootU*rootZu*rootV**2
                    +2*rootU**2*rootV*rootZv)
                  +2*beta*kmax.sqrt()*rootcrossdot)
            # The second term in MD has no eta^{-1}.
            ratio = Hhi/R0
            if not ratio < 1:
                raise ArithmeticError("a root Cauchy remainder exceeds its true analytic disk")
            Afee = MA*(2/(3*Hlo*Hlo.sqrt())+2/(R0*Hlo.sqrt())
                       +2*Hhi.sqrt()/(R0**2*(1-ratio)))
            Bfee = MB*(2/Hlo.sqrt()+2*Hhi.sqrt()/(R0*(1-ratio)))
            Cfee = 2*MC*Hhi.sqrt()
            Dfee = 2*MD*Hhi*Hhi.sqrt()/3
            bound = (Afee+Bfee+Cfee+Dfee).upper()
            candidates.append(dict(exact_radial_radius=str(ROOT_RADIUS*factor),
                exact_outer_radius=str(ROOT_RADIUS),
                complete_k_rho_Cauchy_bound=record(cauchy_k_derivative.upper()),
                complete_a0_bound=record(astar.upper()), complete_a0_parameter_bound=record(adot.upper()),
                complete_parameter_derivative_envelopes={
                    k: record(v.upper()) for k, v in dict(A=MA, B=MB, C=MC, D=MD).items()},
                finite_part_subtraction_and_remainder_fees={
                    k: record(v.upper()) for k, v in dict(A=Afee, B=Bfee, C=Cfee, D=Dfee).items()},
                complete_root_finite_part_parameter_derivative=record(bound)))
        selected = min(range(len(candidates)),
                       key=lambda index: upper(candidates[index]["complete_root_finite_part_parameter_derivative"]))
        Lroot = upper(candidates[selected]["complete_root_finite_part_parameter_derivative"])
        total = (Lstrict+Lroot).upper()
        fee = (parameter*total).upper()
        X0 = box(fp["complete_signed_first_symbol_finite_part"])
        transferred = X0+arb(0, fee)
        report.update(
            exact_root_enclosure=list(map(str, (rootlo, roothi))),
            root_to_cut_interval=[str(rootlo-CUT), str(roothi-CUT)],
            root_complete_K1_minus60=record(Mk),
            root_complete_k_real_gap=record(kgap), root_complete_k_modulus=record(kmax),
            root_complete_direction_mean=record(rootZm),
            root_complete_mean_gap=record(rootM),
            root_Cauchy_candidates=candidates, selected_root_Cauchy_index=selected,
            complete_strict_parameter_derivative=record(Lstrict),
            complete_root_parameter_derivative=record(Lroot),
            complete_total_parameter_derivative=record(total),
            actual_selected_R31_parameter_abs_upper=record(parameter),
            selected_parameter_complete_transfer_fee=record(fee),
            original_delta0_complete_finite_part=record(X0),
            complete_selected_parameter_finite_part=record(transferred),
            minus_quarter_of_selected_finite_part_with_no_full_return_identification=record(-transferred/4),
            transfer_enclosure_complete=True)
        check("the actual complete finite-part homotopy and all derivative bounds are finite",
              total.is_finite() and fee.is_finite() and transferred.is_finite())
        goal = bool(fee < exact(WIDTH_GOAL))
        report["requested_transfer_fee_goal_met"] = goal
        report["gates"].append(dict(
            name="the complete selected-parameter transfer fee is below the declared one-ten-thousandth goal",
            passed=goal))
        report["complete"] = all(g["passed"] for g in report["gates"])
        checkpoint("complete" if report["complete"] else "complete-valid-transfer-misses-goal")
        print(dict(complete=report["complete"], derivative_bound=total.str(24),
                   selected_transfer_fee=fee.str(24), finite_part=transferred.str(28),
                   full_return_identification_still_open=True), flush=True)
        if not goal:
            raise ArithmeticError("the valid complete transfer misses its requested fee goal")
    except Exception as exc:
        report["failure"] = dict(type=type(exc).__name__, message=str(exc))
        checkpoint("failed-prefix-preserved")
        raise


if __name__ == "__main__":
    main()
