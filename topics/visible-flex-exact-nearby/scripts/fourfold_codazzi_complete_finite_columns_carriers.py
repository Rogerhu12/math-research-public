"""CFC necessary original carriers; no completed SC/BFP/DCP target replay.

The whole SC restoration prefix ends immediately after the true waist
density. It neither restores the old96 RW rows nor evaluates either old
signed96 matrix. Its one complete original TC value-array SHA is required.
"""
from __future__ import annotations
import ast
import hashlib
import importlib.util
import json
from pathlib import Path

SC_RESTORE = "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_signed_finite_trial_carrier_restore.py"
SC_RESTORE_SHA = "709640e88ded0c7aa21dd545944885790ff21d3d4625315d2923438784f3c1a8"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def original_waist_prefix(module, raw):
    require(hashlib.sha256(raw).hexdigest() == SC_RESTORE_SHA,
            "the entire original SC carrier-restoration source")
    tree = ast.parse(raw)
    nodes = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "restore"]
    require(len(nodes) == 1, "one complete original restoration function")
    node = nodes[0]
    stop = [i for i, item in enumerate(node.body) if isinstance(item, ast.Assign)
        and len(item.targets) == 1 and isinstance(item.targets[0], ast.Name)
        and item.targets[0].id == "old"
        and ast.dump(item.value) == ast.dump(ast.parse("prior['RW_actual']", mode="eval").body)]
    require(len(stop) == 1 and stop[0] > 0, "the exact boundary before old RW carrier restoration")
    prefix = node.body[:stop[0]]
    require(isinstance(prefix[-1], ast.Assign) and isinstance(prefix[-1].targets[0], ast.Name)
            and prefix[-1].targets[0].id == "density", "the full selected waist algebra has finished")
    forbidden = {"ReflectedRowFactory", "real_signed_density_pairing", "density_norm_squared"}
    require(not any(isinstance(x, ast.Name) and x.id in forbidden for item in prefix for x in ast.walk(item)),
            "no prior row, matrix, or norm target is entered")
    tail = ast.parse("return dict(c=c, core=module, density=density, q=q0, ng=ng0, "
        "value_receipt=value_receipt, offset_receipts=offset_receipts, prefix_receipt=prefix_receipt, "
        "definition_sha256=definition_sha, original_definition=definition, original_trial=old_proposal)").body[0]
    node.body = prefix+[tail]
    fragment = ast.Module(body=[node], type_ignores=[])
    ast.fix_missing_locations(fragment)
    namespace = dict(module.__dict__)
    exec(compile(fragment, "<CFC same original TC waist prefix>", "exec"), namespace)
    return namespace["restore"], {"whole_source_sha256":SC_RESTORE_SHA,
        "complete_original_function_prefix":True, "stopped_before_original_RW_rows":True,
        "original_value_factory_arithmetic_changed":False, "old_norm_or_signed_matrix_targets_called":0}


def restore_TC_waist(np, flint, root, private, sc, progress):
    root, private = Path(root), Path(private)
    module = load(root/SC_RESTORE, "_CFC_original_SC_carrier_only")
    function, adapter = original_waist_prefix(module, (root/SC_RESTORE).read_bytes())
    restored = function(np, flint, root, private, sc["admitted_TC"],
                        sc["TC"]["state"], sc["TC"]["matrix"], progress)
    c, density = restored["c"], restored["density"]
    require(all(not np.any(p.error.hi) for p in density["primitive_pair"]+density["means"]),
            "all finite exact original waist fields, no uncharged tail")
    p, m = (v.Fourier() for v in density["primitive_pair"])
    total = (p+m)/2
    require(total.real.lo.shape == (1024, 1, 96)
            and np.all(total.imag.lo <= 0) and np.all(total.imag.hi >= 0),
            "the entire even real physical primitive sum and all96 columns")
    # The reflected odd raw first component has an exactly even primitive;
    # its positive coefficients are real. This is algebra, not thresholding.
    coefficients = c.CBox(total.real[1:97, 0, :])
    means_lo, means_hi = [], []
    for value in density["means"]:
        require(value.degree == 0 and len(value.coefficients) == 1,
                "both whole stored mean coordinates")
        means_lo.append(value.coefficients[0][0].lo.copy())
        means_hi.append(value.coefficients[0][0].hi.copy())
    means = c.Box(np.array(means_lo), np.array(means_hi))
    require(means.lo.shape == (2, 96), "both full stored means, no invented extra free mean")
    receipt = {"kind":"CFC_same_original_TC_whole_value_waist_restoration_v1", "complete":True,
        "complete_original_value_array":restored["value_receipt"],
        "complete_original_offset_receipts":restored["offset_receipts"],
        "original_value_prefix":restored["prefix_receipt"], "waist_prefix":adapter,
        "whole_definition_sha256":restored["definition_sha256"],
        "old_derivative_arrays_materialized":False, "old_RW_rows_or_SC_matrices_restored":False,
        "old_completed_scientific_targets_called":0, "new_trial_selected":False}
    return c, coefficients, means, receipt


def restore_compound_inputs(np, flint, api, dcp, grid_raw, private, progress, atomic):
    """One whole original AS grid feeds all unchanged w/alpha/grid inputs."""
    private = Path(private)
    bfp = dcp["BFP_context"]
    bnc, uc, old = bfp["BNC"]["admitted"], bfp["UACT"]["admitted"], bfp["original_OT"]
    ot_owner, ot_actual = uc["owner"], uc["actual"]
    carriers, pure = dcp["carriers"], dcp["pure"]
    w, wr = carriers.restore_needed_w(api, bnc, grid_raw, private/"same-original-w-only", progress)
    alpha_directory = private/"same-original-alpha-only"
    ar = bfp["carriers"].restore_original_alpha_from_saved_grid(
        api, old, ot_owner, grid_raw, alpha_directory, progress)
    alpha_body = json.loads((alpha_directory/"complete-original-AS-alpha-trial.json").read_bytes())
    alpha = alpha_body["all_positive_exact_pairs"]
    require(len(alpha) == len(w) == 2048, "the two whole original normalizer coefficient carriers")
    model, source_b, mr = carriers.restore_original_model(api, old, ot_owner, ot_actual, private)
    ir_grid, ir = carriers.restore_IR_grid_only(api, old, ot_owner, private, progress)
    phat = pure.complete_new_grid(api, ir_grid, old["states"][1], old["prior"]["K_sines"], old["prior"]["K_cosines"])
    body = {"kind":"DCP_complete_8192_inverse_density_grid_v1",
        "original4096_sha256":old["IR"]["actual"]["private_grid_receipt"]["sha256"],
        "all_balls":[value.str(110) for value in phat]}
    raw = carriers.encode(body)
    expected = dcp["completed_actual"]["new_carrier_receipts"]["complete-new-particular-grid.json"]
    ot_owner.verify_private(private/"complete-new-particular-grid.json", raw, expected)
    formal = [api.arb(value) for value in json.loads(raw)["all_balls"]]
    require(all(a.contains(b) for a,b in zip(formal,phat)), "all original DCP grid balls under the whole old SHA")
    phat = formal
    # Recreate only the original G and exact analytic Jacobian. The zero
    # argument is a harmless source slot; no old NP f, norm or proposal is run.
    points, pi = bfp["carriers"].complete_physical_points(
        api, bnc, [api.arb(0) for unused in range(96)], grid_raw, progress)
    G, Gprime = [p[1] for p in points], [p[2] for p in points]
    return {"w_pairs":w, "alpha_pairs":alpha, "model2240":model, "source_b":source_b,
        "G":G, "Gprime":Gprime, "phat_grid":phat,
        "true_a":api.arb(bnc["parents"]["DW"]["actual"]["complete_true_phase_a_ball"]),
        "whole_receipts":{"w":wr,"alpha":ar,"model":mr,"IR_grid":ir,
            "whole_DCP8192_grid":expected,"Gprime_identity":pi},
        "shared_original_AS_grid_sha256":hashlib.sha256(grid_raw).hexdigest()}
