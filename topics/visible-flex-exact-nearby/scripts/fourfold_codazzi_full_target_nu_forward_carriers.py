"""Complete BFP carrier operations, separate from all scalar/error targets.

Numerical functions are called only by the declared public owner. Original
carriers must retain their whole SHA; new forward trials are arbitrary exact
dyadic polynomials whose full residual is certified by the BFP formulas.
"""
from __future__ import annotations
from fractions import Fraction
from pathlib import Path
import gzip
import hashlib
import importlib.util
import json
import math


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                       allow_nan=False)+"\n").encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def midpoint_fraction(value):
    require(value.is_finite(), "one entire finite original coefficient")
    a, e = map(int, value.mid().man_exp())
    return Fraction(a*(1 << e)) if e >= 0 else Fraction(a, 1 << (-e))


def restore_original_alpha_from_saved_grid(api, old, original_owner, grid_raw, destination, progress):
    """The original AS carrier suffix, reusing its entire already restored grid.

    No old norm, error bound or cohomological certificate is reevaluated.
    Only the original exact finite coefficients needed by the OT carrier are
    reproduced, and every byte must match the successful original receipt.
    """
    actual, pure = old["AS"]["actual"], old["AS_math"]
    expected = actual["private_grid_receipt"]
    require(len(grid_raw) == expected["bytes"] and sha(grid_raw) == expected["sha256"],
            "the entire original AS grid is reused, not recomputed")
    body = json.loads(grid_raw)
    formal_grid = [(api.arb(t), api.arb(g)) for t, g in body["all_pairs"]]
    require(body["complete_count"] == len(formal_grid) == 8192, "all original grid records")
    # Recreate the original arithmetic expression. Reading the display-phase
    # ball back would change its midpoint and therefore the original dyadics.
    EH = original_owner.whole_upper(api, actual["global_bounds"]["complete_original_H_minus_G_upper"])
    omega, phase = pure.original_rotation_and_phase(api, formal_grid[0][1], EH)
    require(omega.str(90) == actual["global_bounds"]["complete_exact_rotation_ball"]
            and phase.str(90) == actual["global_bounds"]["complete_original_source_phase_ball"],
            "the same complete original rotation and source-phase expressions")
    factory = pure.WholeQuadrature(api, formal_grid)
    alpha_pairs = []
    for n in range(1, 2049):
        integral = factory.next()
        formal = api.acb(api.arb(integral.real.str(90)), api.arb(integral.imag.str(90)))
        coefficient, unused = pure.complete_mode_reference(api, n, formal, omega, phase)
        alpha_pairs.append([str(midpoint_fraction(coefficient.real)), str(midpoint_fraction(coefficient.imag))])
        if n % 64 == 0:
            progress("restoring_original_OT_alpha_carrier_without_old_targets", {"complete_modes": n})
    trial = {"kind": "AS_complete_original_alpha_dyadic_trial_v1", "positive_modes": 2048,
             "all_positive_exact_pairs": alpha_pairs, "exact_mean": "0",
             "negative_modes_are_exact_conjugates": True}
    raw = canonical(trial)
    original_owner.verify_private(Path(destination)/"complete-original-AS-alpha-trial.json", raw,
                                  actual["private_alpha_trial_receipt"])
    return {"kind": "BFP_same_original_alpha_from_whole_saved_grid_v1", "complete": True,
            "grid": expected, "alpha_trial": actual["private_alpha_trial_receipt"],
            "original_grid_reconstructed_again": False, "old_scalar_error_norm_targets_run": 0,
            "whole_original_SHA_required": True}


def original_physical_coefficients(np, flint, api, context, private, progress, atomic):
    """Same complete NP trial and same true selected waist algebra as BNC."""
    parents = context["parents"]
    npm, actual = parents["NP"]["manifest"], parents["NP"]["actual"]
    paths, raws, helper = context["paths_by_path"], context["raws_by_path"], context["row_inputs"]
    roles = npm["roles"]
    original_body = json.loads(raws[roles["old_body_manifest"]])
    rows, part_receipts = helper.admit_all_rows(
        [paths[item["path"]] for item in npm["historical_inputs"] if item["role"].startswith("original_rows_")],
        {"old_body_manifest": original_body, "NW": {"difference": context["NP_SB"]["prior"]["D"]}})
    waist, scalars, receipt = context["NP_restore"].restore(np, flint, npm, actual, raws, paths,
        helper, rows, part_receipts, Path(private)/"same-complete-NP", progress, atomic)
    core = load(paths[roles["trial_math"]], "_BFP_original_physical_waist_algebra")
    backend, unused = helper.directed_backend(np, flint, raws[roles["box_math"]], raws[roles["fft_math"]])
    c = core.DirectedContext(np, api.arb, backend["Box"], backend["CBox"], backend["zeros"],
        backend["arb_box"], backend["reduce_box"], backend["DirectedFFT"]())

    def ball(record):
        return context["DW_context"]["carrier"].whole_ball(api, record)

    row0 = rows[0]
    left, right = map(Fraction, row0["interval"])
    field = core.scalar_taylor(c, row0["intrinsic_midpoint_jets"], row0["intrinsic_whole_third_jets"],
                              "K", *row0["interval"], left, right, ball)
    require(field.degree == 0 and left == 0, "the complete original field at the actual waist")
    kbox = core.trial_value(c, field.coefficients, c.box(-1))[0, 0]
    radius = float(np.max(field.error.hi))
    kbox = kbox+c.Box(-radius, radius)
    K0 = api.arb(float(kbox.lo)).union(api.arb(float(kbox.hi)))
    mean = ball(actual["new_records"]["complete_signed_strict_nu_waist_column"]["whole_selected_waist_mean_enclosure"])
    require(K0.upper() < 0 and mean.upper() < 0 and scalars["waist_a"].lower() > 0,
            "the same true implicit selected physical denominators")
    q, ng = (-K0).sqrt(), scalars["waist_a"]**2/(mean*mean)
    coefficients = context["math"].physical_positive_coefficients(api, waist, q, ng)
    require(len(coefficients) == 96 and all(x.is_finite() for x in coefficients), "all original physical source coefficients")
    return coefficients, receipt


def complete_physical_points(api, context, coefficients, grid_raw, progress):
    """All f, original G and exact analytic-chain G' at the 8192 nodes."""
    npm = context["parents"]["NP"]["manifest"]
    raws, roles = context["raws_by_path"], npm["roles"]
    hdoc = json.loads(gzip.decompress(raws[roles["RW_H_native"]]))
    kdoc = json.loads(gzip.decompress(raws[roles["RW_K_native"]]))
    Hs, Hc = hdoc["exact_H_sine_coefficients"], hdoc["exact_H_cosine_coefficients"]
    Ks, Kc = kdoc["exact_postcomposition_sine_coefficients"], kdoc["exact_postcomposition_cosine_coefficients"]
    require(len(Hs) == len(Hc) == 24 and len(Ks) == len(Kc) == 48, "all original lift coefficients")
    h = [api.acb(api.rational(Fraction(c)), -api.rational(Fraction(s))) for s, c in zip(Hs, Hc)]
    k = [api.acb(api.rational(Fraction(c)), -api.rational(Fraction(s))) for s, c in zip(Ks, Kc)]
    hd = [api.acb(0, 4*n)*z for n, z in enumerate(h, 1)]
    kd = [api.acb(0, 4*n)*z for n, z in enumerate(k, 1)]

    def horner(point, values):
        result = api.acb(0)
        for value in reversed(values):
            result = point*(value+result)
        return result

    original = json.loads(grid_raw)["all_pairs"]
    require(len(original) == 8192, "the entire original G grid")
    points = []
    for j, unused_gpair in enumerate(original):
        phi = api.arb.pi()*j/(2*8192)
        z = api.acb((4*phi).cos(), (4*phi).sin())
        H = phi+horner(z, h).real
        Hp = 1+horner(z, hd).real
        hz = api.acb((4*H).cos(), (4*H).sin())
        G = H+horner(hz, k).real
        Gp = Hp*(1+horner(hz, kd).real)
        original_G = api.arb(original[j][1])
        require(G.overlaps(original_G) and Gp.lower() > 0, "same complete original lift and positive analytic Jacobian")
        f = 2*horner(z, coefficients).real
        points.append((f, original_G, Gp))
        if (j+1) % 512 == 0:
            progress("forming_complete_new_pullback_f_G_Gprime_grid", {"complete_points": j+1})
    return points, {"original_H_source_sha256": sha(raws[roles["RW_H_native"]]),
                    "original_K_source_sha256": sha(raws[roles["RW_K_native"]]),
                    "analytic_chain_rule_not_grid_differences": True}


def choose_forward_trial(np, original_w_pairs, whole_point_triples):
    """A floating proposal only; all512 outputs become exact dyadic inputs.

    Periodic inverse resampling is used, so no old192 certified observation
    target is repeated. All accuracy comes later from the full residual.
    """
    require(len(original_w_pairs) == 2048 and len(whole_point_triples) == 8192,
            "entire finite proposal inputs")
    period = math.pi/2
    x = np.arange(8192, dtype=np.float64)*(period/8192)
    g = np.array([float(p[1].mid()) for p in whole_point_triples], dtype=np.float64)
    values = np.array([float((p[0]/p[2]).mid()) for p in whole_point_triples], dtype=np.float64)
    samples = np.interp(x, g, values, period=period)
    source = (np.fft.fft(samples)/8192)[1:513]
    w = [complex(float(Fraction(a)), float(Fraction(b))) for a, b in original_w_pairs]
    matrix = np.eye(512, dtype=np.complex128)
    for i in range(512):
        for j in range(512):
            difference = i-j
            if difference:
                coefficient = w[abs(difference)-1]
                if difference < 0:
                    coefficient = coefficient.conjugate()
                matrix[i, j] += coefficient/complex(0, 4*(j+1))
    status = "finite_floating_positive_block_proposal"
    try:
        solution = np.linalg.solve(matrix, source)
        if not bool(np.isfinite(solution).all()):
            solution = np.zeros(512, dtype=np.complex128)
            status = "nonfinite_proposal_replaced_by_explicit_exact_zero_trial"
    except np.linalg.LinAlgError:
        solution = np.zeros(512, dtype=np.complex128)
        status = "singular_proposal_replaced_by_explicit_exact_zero_trial"
    pairs = [[str(Fraction.from_float(float(z.real))), str(Fraction.from_float(float(z.imag)))] for z in solution]
    return pairs, {"status": status, "positive_modes": 512, "exact_mean": "0",
                   "negative_modes_are_exact_conjugates": True,
                   "floating_proposal_is_not_a_certified_solve": True,
                   "old_BNC_certified_observations_evaluated": 0}
