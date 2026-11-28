"""Only the immutable carriers needed by the one new DCP particular.

The old IR96 matrix, DWT96 row matrix, Theta96x2240 matrix and all old
residual/norm/pairing producers are deliberately outside this restoration.
Each necessary original byte sequence is accepted only at its whole SHA.
"""
from __future__ import annotations
import ast
import hashlib
import json
from pathlib import Path

ROW_RESTORE_SHA = "515529d0bcb063d4a2632c3ca0b1998b36f01df7a6a767082a24cd48ad584ec4"
W_PREFIX_BYTES = 5723
W_PREFIX_SHA = "1bd75fd8ccfe159eb711f98f06c5dae31955aaaf32ee6b8447dfb78110c9a09d"
W_STOP = "    phase_text = (phase-omega).str(90)\n"
W_RETURN = '''    return pairs, {
        "kind": "DCP_same_complete_DWTB_w_only_restoration_v1", "complete": True,
        "unit_disk_input": expected, "signed_w_trial": expected_w,
        "whole_original_SHA_required": True,
        "old_row_trial_materialized": False, "old_DWT_BR_scalar_targets_called": 0}
'''


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                       allow_nan=False)+"\n").encode()


def parse(raw):
    return json.loads(raw, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def needed_w_source(whole_original_source):
    require(sha(whole_original_source) == ROW_RESTORE_SHA, "the entire immutable original w/row restoration source")
    text = whole_original_source.decode()
    tree = ast.parse(text)
    nodes = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "restore"]
    require(len(nodes) == 1, "the one original whole carrier function")
    node = nodes[0]
    function = "".join(text.splitlines(keepends=True)[node.lineno-1:node.end_lineno])
    require(function.count(W_STOP) == 1, "the explicit boundary before the unnecessary old96 row selection")
    prefix = function[:function.index(W_STOP)]
    require(len(prefix.encode()) == W_PREFIX_BYTES and sha(prefix.encode()) == W_PREFIX_SHA
            and "choose_trial_bytes" not in prefix and "private_row_trial_receipt" not in prefix,
            "the entire original disk/w prefix and no old row reconstruction")
    result = prefix+W_RETURN
    ast.parse(result)
    return result


def restore_needed_w(api, bnc, whole_grid_raw, destination, progress):
    original = bnc["row_restore"]
    raw = Path(original.__file__).read_bytes()
    namespace = dict(original.__dict__)
    exec(compile(needed_w_source(raw), "_DCP_original_complete_w_only_prefix", "exec"), namespace)
    pairs, receipt = namespace["restore"](None, api, bnc["DW_context"], bnc["parents"]["DW"]["actual"],
                                             whole_grid_raw, destination, progress)
    require(len(pairs) == 2048 and receipt["complete"] is True
            and receipt["whole_original_SHA_required"] is True and receipt["old_row_trial_materialized"] is False,
            "the entire necessary w input only")
    return pairs, receipt


def restore_IR_grid_only(api, old, original_owner, destination, progress):
    pure, actual = old["IR_math"], old["IR"]["actual"]
    for name in ("fft_tables", "complete_directed_dft", "complete_global_bounds", "complete_kernels",
                 "complete_column_bounds", "entire_signed_head", "complete_residual_norms",
                 "complete_joint_residual", "CompletePrimitiveSampleFactory"):
        setattr(pure, name, original_owner.forbidden)
    old["IR"]["owner"].main = original_owner.forbidden
    old["IR"]["owner"].choose_complete_dyadic_trial_bytes = original_owner.forbidden
    grid = pure.exact_compound_grid(api, old["states"][1], old["prior"]["K_sines"], old["prior"]["K_cosines"])
    raw = encode({"kind": "R149_complete_original_inverse_lift_grid_v1", "complete_count": len(grid),
                  "all_balls": [value.str(80) for value in grid]})
    path = Path(destination)/"complete-original-IR-grid.json"
    original_owner.verify_private(path, raw, actual["private_grid_receipt"])
    formal = [api.arb(text) for text in parse(path.read_bytes())["all_balls"]]
    require(len(formal) == 4096 and all(a.contains(b) for a, b in zip(formal, grid)),
            "every complete original IR node under its original whole SHA")
    progress("same_complete_IR_grid_only_restored", {"nodes": 4096, "old_IR96_trial_restored": False})
    return formal, {"kind": "DCP_same_complete_IR_grid_only_restoration_v1", "complete": True,
        "grid": actual["private_grid_receipt"], "old_IR96_trial_restored": False,
        "old_IR_scientific_targets_called": 0, "whole_original_SHA_required": True}


def restore_BFP_reference(np, flint, api, bfp_context, whole_bfp_actual, original_owner,
                          bnc, whole_grid_raw, whole_w_pairs, destination, progress, atomic):
    """Restore exactly BFP's finite proposal and true target coordinates.

    Every intermediate private BFP byte stream is checked. No old forward
    image, pullback square, norm, scalar error, or Theta pairing is entered.
    """
    carriers, pure = bfp_context["carriers"], bfp_context["pure"]
    for name in list(vars(pure)):
        if name.startswith("complete_") and name != "complete_projected_target_coordinates":
            setattr(pure, name, original_owner.forbidden)
    pure.CompletePullbackPolynomial = original_owner.forbidden
    root = Path(destination)
    root.mkdir(parents=True, exist_ok=True)
    expected = whole_bfp_actual["new_carrier_receipts"]
    receipts = {}

    def old_file(name, body):
        raw = encode(body)
        original_owner.verify_private(root/name, raw, expected[name])
        receipts[name] = expected[name]
        return parse((root/name).read_bytes())

    coefficients, np_receipt = carriers.original_physical_coefficients(
        np, flint, api, bnc, root, progress, atomic)
    require(np_receipt == whole_bfp_actual["NP_restoration"], "the entire same NP waist restoration")
    body = old_file("complete-physical-source-coefficients.json", {
        "kind": "BFP_complete_original_physical_nu_source_v1", "positive_modes": 96, "exact_mean": "0",
        "all_positive_balls": [value.str(110) for value in coefficients], "negative_modes_are_real_conjugates": True})
    coefficients = [api.arb(text) for text in body["all_positive_balls"]]
    points, identity = carriers.complete_physical_points(api, bnc, coefficients, whole_grid_raw, progress)
    body = old_file("complete-pullback-input-points.json", {"kind": "BFP_complete_f_G_Gprime_grid_v1",
        "complete_nodes": 8192, "original_grid_sha256": sha(whole_grid_raw), **identity,
        "all_triples": [[f.str(110), g.str(110), gp.str(110)] for f, g, gp in points]})
    points = [tuple(api.arb(text) for text in triple) for triple in body["all_triples"]]
    trial, selection = carriers.choose_forward_trial(np, whole_w_pairs, points)
    require(selection == whole_bfp_actual["trial_proposal"], "the entire original finite proposal identity")
    body = old_file("complete-forward-trial.json", {"kind": "BFP_complete_forward_dyadic_trial_v1",
        "positive_modes": 512, "exact_mean": "0", "all_positive_exact_pairs": trial,
        "negative_modes_are_exact_conjugates": True, "proposal": selection})
    trial = body["all_positive_exact_pairs"]
    true_a = api.arb(bnc["parents"]["DW"]["actual"]["complete_true_phase_a_ball"])
    coordinates = pure.complete_projected_target_coordinates(api, trial, true_a)
    body = old_file("complete-forward-target-coordinates.json", {
        "kind": "BFP_all_true_phase_target_coordinates_v1", "complete_modes": 512,
        "whole_true_a": true_a.str(110), "all_balls": [value.str(110) for value in coordinates]})
    coordinates = [api.arb(text) for text in body["all_balls"]]
    progress("same_complete_BFP512_reference_restored", {"all_four_original_private_SHA_matched": True})
    return coordinates, {"kind": "DCP_same_complete_BFP512_reference_restoration_v1", "complete": True,
        "NP_restoration": np_receipt, "private_receipts": receipts,
        "whole_original_true_phase_retained": True, "old_BFP_targets_called": 0,
        "old_BFP_2560_image_or_Theta96_pairings_restored": False, "whole_original_SHA_required": True}


def restore_original_model(api, old, original_owner, ot_actual, destination):
    alpha = old["AS"]["actual"]
    glob = alpha["global_bounds"]
    omega = api.arb(glob["complete_exact_rotation_ball"])
    source_b = api.arb(glob["complete_original_source_phase_ball"])
    mu = original_owner.whole_ball(api, alpha["copied_original_records"]["complete_signed_mu"])
    native = old["CYA"]["complete_original_scalar_input_conclusion"]["original_gap_coefficient_record_read_verbatim"]
    require(original_owner.whole_ball(api, native).contains(-mu/4), "the same entire native infinite Cayley qualification")
    modes = []
    for n in range(1, 2241):
        phase = 2*n*source_b+api.arb.pi()/4
        if n <= 96:
            denominator, reciprocal, kind = api.one, api.one, "original_Llow_reference"
        else:
            theta = 2*n*omega+api.arb.pi()/4
            denominator = theta.cos()-(-mu/2)*theta.sin()/(4*n)
            require(not denominator.contains(0), "the entire original signed model denominator")
            reciprocal, kind = 1/denominator, "original_Mnu_high_reciprocal"
        modes.append({"mode": n, "kind": kind, "signed_denominator": denominator.str(90),
                      "signed_reciprocal": reciprocal.str(90), "true_source_phase": phase.str(90)})
    raw = encode({"kind": "OT_complete_original_model_multipliers_v1", "complete_modes": 2240, "all_modes": modes})
    path = Path(destination)/"complete-original-model-multipliers.json"
    original_owner.verify_private(path, raw, ot_actual["private_model_multipliers_receipt"])
    formal = parse(path.read_bytes())["all_modes"]
    require([value["mode"] for value in formal] == list(range(1, 2241)), "all2240 original model entries")
    return [api.arb(value["signed_reciprocal"]) for value in formal], source_b, ot_actual["private_model_multipliers_receipt"]
