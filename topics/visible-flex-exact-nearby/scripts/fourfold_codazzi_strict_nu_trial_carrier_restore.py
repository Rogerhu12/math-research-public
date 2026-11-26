"""PA necessary input: restore the EXACT four already completed NP carriers.

The entire original deterministic recipe and every complete array receipt
are retained.  No residual cell, old pairing, old norm, QR or direction
target is invoked.  A hash mismatch is failure, never a new trial choice.
"""
from __future__ import annotations
from fractions import Fraction
import hashlib, importlib.util, json
from pathlib import Path


def require(ok,message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def load(path,name):
    spec = importlib.util.spec_from_file_location(name,path)
    module = importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


def restore(np,flint,manifest,actual,raws,paths,helper,rows,part_receipts,private,progress,atomic):
    """Return only the original full physical waist vector and small scalars.

    All four complete740x193 arrays are nevertheless rematerialized and
    matched to NP's actual full receipts before any new pairing is allowed.
    """
    roles = manifest["roles"];arb = flint.arb
    def ball(record):
        value = arb(record["ball"])
        if "lower" in record and "upper" in record:
            value = value.union(arb(record["lower"])).union(arb(record["upper"]))
        require(value.is_finite(),"whole finite original ball")
        return value
    core = load(paths[roles["trial_math"]],"_PA_original_directed_carrier_algebra")
    math = load(paths[roles["nu_math"]],"_PA_original_trial_grid_definition")
    proposal = load(paths[roles["nu_proposal"]],"_PA_original_frozen_trial_recipe")
    old_proposal = load(paths[roles["proposal_math"]],"_PA_original_centre_carrier")
    backend,_ = helper.directed_backend(np,flint,raws[roles["box_math"]],raws[roles["fft_math"]])
    c = core.DirectedContext(np,arb,backend["Box"],backend["CBox"],backend["zeros"],
        backend["arb_box"],backend["reduce_box"],backend["DirectedFFT"]())
    reader,_ = helper.candidate_reader(np,raws[roles["candidate_reader"]])
    iterator,_ = helper.repair_iterator(raws[roles["repair_source"]])
    base = reader(paths[roles["base_index"]])
    require(base["piece_coefficients"].shape == (4,6144,65),"all original centre coefficients")
    nodes,plan = math.complete_plan(rows,base["radial_nodes"])
    definition = {"kind":"NP_fixed_rational_septic_forced_nu_trial_v1",
        "node_labels":list(map(str,nodes)),"maximum_step":"1/4096",
        "terminal":"entire value and first three jets zero at9/50",
        "basis":manifest["parameters"]["trial_basis"],"selected_parameter_is_not_a_numeric_point":True}
    expected = actual["trial_definition"]
    require(sha(canonical(definition)) == expected["definition_sha256"]
        and sha(canonical(plan)) == expected["certificate_plan_sha256"]
        and len(nodes) == expected["complete_nodes"] == 740
        and len(plan) == expected["complete_certificate_cells"] == 2472
        and len(rows) == expected["complete_original_rows"] == 7721
        and sha(canonical(part_receipts)) == expected["original_full_part_receipts_sha256"],
        "same entire frozen NP definition, original complete inputs and exact endpoint grid")
    offsets = {key:np.zeros((6144,65)) for key in ("lower","upper","midpoint")}
    last_piece = max(item["background_piece"] for item in plan);offset_digest = hashlib.sha256()
    for piece,values,_ in iterator(base,math.ALPHA):
        if piece > last_piece:
            break
        offset_digest.update(canonical({"piece":piece,"physical_offset":list(map(str,values))}))
        for k,value in enumerate(values):
            converted = c.arb_box(c.exact(value))
            offsets["lower"][piece,k],offsets["upper"][piece,k] = float(converted.lo),float(converted.hi)
            offsets["midpoint"][piece,k] = float(value)
    require({"pieces":last_piece+1,"signed_offset_sequence_sha256":offset_digest.hexdigest(),
        "entire_scientific_domain":"[0,9/50]","all_preceding_interface_offsets_included":True}
        == expected["necessary_complete_centre_prefix"],"entire same required continuous centre prefix")
    ref = old_proposal.FloatingCentreReference(np,rows,base,offsets["midpoint"],math.ALPHA,ball)
    forced = proposal.ForcedCentreReference(np,ref,rows,ball)
    def restoring_progress(unused_stage,detail):
        progress("restoring_necessary_same_NP_frozen_trial_carriers",detail)
    jets,selection = proposal.choose_particular(np,forced,nodes,restoring_progress)
    require(selection == actual["trial_receipts"]["selection"],"same original deterministic recipe, not a new proposal")
    receipts = []
    for order,value in enumerate(jets):
        require(value.shape == (740,193) and np.all(np.isfinite(value)),"whole finite original endpoint array")
        payload = np.asarray(value,dtype='<f8').tobytes(order='C')
        receipt = {"derivative":order,"shape":[740,193],"bytes":len(payload),"sha256":sha(payload)}
        require(receipt == actual["trial_receipts"]["complete_arrays"][order],
                "same complete original NP array; mismatch cannot define a substitute trial")
        path = Path(private)/("original_NP_endpoint_derivative_%d.f64"%order);atomic(path,payload)
        require(path.read_bytes() == payload,"complete necessary original carrier readback")
        receipts.append(receipt)
        jets[order] = np.memmap(path,dtype='<f8',mode='r',shape=(740,193))
    require(actual["trial_receipts"]["shared_endpoint_jets_define_exact_C3_trial"] is True
        and actual["trial_receipts"]["complete_trial_state_jump_sum"] == "0", "original trial and all its exact jumps")
    # This exact binary64 vector is a chosen physical trial, not a numerical
    # selected state.  The original NP full selected error stays separate.
    waist = [arb(float(value)) for value in jets[0][0]]
    row0 = rows[0]
    require(Fraction(row0["interval"][0]) == 0,"the true waist is in the complete first original cell")
    whole = row0["intrinsic_whole_third_jets"]
    return waist,{"waist_K":ball(whole["K"]),"waist_a":ball(whole["a"])},{
        "complete_original_trial_definition_sha256":expected["definition_sha256"],
        "complete_original_array_receipts":receipts,"all_four_complete_arrays_read_back":True,
        "original_recipe_counters":selection,"old_residual_cells_evaluated":0,
        "old_signed_pairings_evaluated":0,"old_scientific_norm_targets_evaluated":0,
        "new_trial_selected":False,"only_necessary_original_trial_carriers_restored":True}

