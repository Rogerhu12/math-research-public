"""Three original signed physical columns through the actual target and low-coordinate recovery."""
import base64
from fractions import Fraction


def require(ok, message):
    if not ok:
        raise ValueError(message)


def norm(api, values):
    return sum((abs(v).upper()**2 for v in values), api.zero).sqrt().upper()


def exact(api, value):
    return api.rational(Fraction.from_float(float(value)))


def signed_vector(api, np, balls, radius):
    """Public payload contains the entire dyadic centre vector; its rounding has a joint cost."""
    require(len(balls) == 96, "all original real coordinates")
    points = np.asarray([float(v.mid()) for v in balls], dtype="<f8")
    require(np.all(np.isfinite(points)), "all dyadic centres finite")
    rounding = norm(api, [v-exact(api, a) for v,a in zip(balls,points)])
    total = (radius+rounding).upper()
    record = {"rows":96, "exact_dyadic_centres_f64_le":base64.b64encode(points.tobytes()).decode("ascii"),
              "joint_error_upper":total.str(74), "centre_rounding_upper":rounding.str(74)}
    require(api.arb(record["joint_error_upper"]).contains(total), "whole joint signed array error")
    return record


def measure_waists(api, c, batch, actual, pa, np_actual):
    import hashlib
    raw = base64.b64decode(actual["complete_suffix"]["lower_trace_f64_le_base64"], validate=True)
    require(len(raw) == 193*2*8 and hashlib.sha256(raw).hexdigest() == actual["complete_suffix"]["lower_trace_sha256"],
            "both entire original negative waist traces")
    data = c.np.frombuffer(raw, dtype="<f8").reshape(193,2)
    pb = pa["new_amplitude_input_receipts"]
    def original(record):
        return api.arb(record["ball"])
    a = original(pb["whole_waist_a"])
    q = (-original(pb["whole_waist_K"])).sqrt()
    m = original(np_actual["new_records"]["complete_signed_strict_nu_waist_column"]["whole_selected_waist_mean_enclosure"])
    require(a.lower()>0 and q.lower()>0 and m.upper()<0,"all physical selected denominators")
    ng = a*a/(m*m)
    means, coefficients, waist_sizes = [], [], []
    for j in range(2):
        v = [exact(api,x) for x in data[:,j]]
        coeff = [-ng*v[k-1]/(8*k*q.sqrt()) for k in range(1,97)]
        plus = ng*(q/2).sqrt()*v[96]
        means.append({"plus":plus, "minus":-plus})
        coefficients.append(coeff)
        # CFC's N0 is the physical half-sum f, before its change of coordinates.
        # Its generic carrier divides the supplied norm by sqrt(2).
        waist_sizes.append((2*norm(api,coeff)).upper())
    positive = c.CBox(batch.whole_real(c,[[coefficients[j][k] for j in range(2)] for k in range(96)]))
    errors = actual["new_records"][actual["completed_targets"][1]]["radii"]
    raw_errors = [exact(api,float.fromhex(x["raw_waist"])) for x in errors]
    return positive, means, waist_sizes, raw_errors


def original_source(api, dcp, common, ot, original, coordinates, directory, progress):
    """Recreate exactly both finite DCP strict carriers under their complete saved identities."""
    pure = dcp["pure"]
    def restored(name, kind, values):
        raw = dcp["carriers"].encode({"kind":kind,"complete_count":len(values),
                "all_balls":[[v.real.str(110),v.imag.str(110)] for v in values]})
        path = directory/name
        ot.verify_private(path,raw,original["new_carrier_receipts"][name])
        doc = dcp["carriers"].parse(path.read_bytes())
        formal = [api.acb(api.arb(a),api.arb(b)) for a,b in doc["all_balls"]]
        require(all(a.real.contains(b.real) and a.imag.contains(b.imag) for a,b in zip(formal,values)),
                "every certified original signed source coefficient")
        return formal
    z = restored("complete-new-model-source.json","DCP_complete_original_model_source512_v1",
                 pure.complete_model_source(api,coordinates,common["model2240"],common["source_b"]))
    v = restored("complete-new-normalized-source.json","DCP_complete_normalized_source2560_v1",
                 pure.complete_v_coefficients(api,z,common["alpha_pairs"]))
    progress("same_whole_signed_DCP_strict_inputs_restored", {"model":512,"source":2560})
    return z,v


def run(data, private, grid_raw, np, flint, api, c, io, state, progress, publish):
    batch, direct, dcp = (data[k] for k in ("batch","direct","dcp"))
    bfp = dcp["BFP_context"]
    bnc, uc = bfp["BNC"]["admitted"], bfp["UACT"]["admitted"]
    ot = uc["owner"]
    old = bfp["original_OT"]
    original = data["DCP_parent"]["actual"]
    common = data["carrier"].restore_compound_inputs(np,flint,api,dcp,grid_raw,private,progress,data["cfc"].atomic)
    state["carrier_restoration"]["compound"] = common["whole_receipts"]
    source = data["recover"].admit(data["root"], data["raw18"], data["DCP_parent"])
    inverse, receipt = data["recover"].restore_low_inverse(api,np,source,old,private,
                old["IR"]["owner"].choose_complete_dyadic_trial_bytes,common["source_b"])
    state["carrier_restoration"]["whole_UACT_low_inverse"] = receipt
    ba = dcp["BFP_actual"]
    bt = dcp["BFP_manifest"]["target_order"]
    copied = ba["copied_complete_input_records"]
    def up(record):
        return ot.whole_upper(api,record)
    bounds = {key:up(copied[key]) for key in ("EH","G1","H1","G0","w_Linf","w_L2")}
    bounds.update(m=ot.whole_ball(api,copied["m"]), B_inverse=up(ba["new_records"][bt[1]]), BH=api.one)
    # At this step the exact chosen waist trace has zero PDE input error.
    # ASQ23's actual prior raw error is received once after the physical forward and low solve.
    batch.COLS = 2
    coeff, means, waist_sizes, rawerr = measure_waists(api,c,batch,data["ASQ23"],data["PA"],data["NP"])
    bundle = {**common,"c":c,"api":api,"BFP_math":bfp["pure"],"bounds":bounds,
              "physical_coefficients":coeff,"waist_trial_norms":waist_sizes,"waist_errors":[api.zero]*2}
    forward = batch.complete_batch_forward(bundle,io,progress)
    coords = [[batch.box_ball(c,forward["coordinates"][n,j]) for n in range(512)] for j in range(2)]
    errors = list(forward["errors"])
    publish(0,{"complete_forward_errors":[v.str(74) for v in errors],
           "complete_two_raw_errors":[v.str(74) for v in rawerr],"original_raw_cross_Grams":data["ASQ23"]["complete_suffix"]["grams"],
           "whole_512_source_coordinates":io.receipts["complete_TC96_true_target_coordinates"]})
    # The old BFP restore forbids its own original target functions in its private module.
    # Both NEW forward applications have already finished. No BFP completed scientific target is entered.
    strict, receipt = dcp["carriers"].restore_BFP_reference(np,flint,api,bfp,ba,ot,bnc,grid_raw,
                  common["w_pairs"],private/"same-complete-BFP512",progress,data["cfc"].atomic)
    state["carrier_restoration"]["whole_BFP512"] = receipt
    coords.append(strict)
    errors.append(up(original["copied_complete_input_records"]["original_BFP_full_target_error"]))
    rawerr.append(api.zero)
    old_z,old_v = original_source(api,dcp,common,ot,original,strict,private,progress)
    eta = up(original["new_records"][original["completed_targets"][0]])
    ep = up(original["copied_complete_input_records"]["inverse_lift_error"])
    require(ep<=api.rational(Fraction("2.211e-7")) and 0<eta<1, "original true/approximate map bounds")
    matrix = direct.proposal_matrix(np,common["phat_grid"])
    def act(columns,stage,old_column=False):
        nnew = len(columns) - int(old_column)
        batch.COLS = nnew
        z = [dcp["pure"].complete_model_source(api,col,common["model2240"],common["source_b"])
             for col in columns[:nnew]]
        zb = direct.complex_rows(c,batch,[[col[n] for col in z] for n in range(512)])
        vb = batch.complete_same_sign_image(c,common["alpha_pairs"],zb,-1)
        values = batch.complex_columns(c,api,vb)
        if old_column:
            z.append(old_z)
            values.append(old_v)
        return direct.evaluate(c,api,batch,common["phat_grid"],eta,ep,z,values,matrix,io,stage,progress)
    def formal(v):
        if isinstance(v, dict):
            return {k:formal(x) for k,x in v.items()}
        if isinstance(v, list):
            return [formal(x) for x in v]
        return v.str(74)
    def finite_evaluations(output):
        return {"complete_head":output["complete_head"],"complete_source":output["complete_source"],
                "infinite_tail_paid":output["infinite_tail_paid"],"whole_upper_records":formal(output["whole_upper_records"]),
                "signed_grid_Gram":formal(output["signed_grid_Gram"])}
    full = act(coords,"full_direct_inverse",True)
    full_signed = []
    for j in range(3):
        radius=(full["whole_upper_records"][j]["inverse_radius"]+
              api.rational(Fraction("3.395"))*errors[j]+api.rational(Fraction(".456"))*rawerr[j]).upper()
        full_signed.append(signed_vector(api,np,full["signed_centres"][j],radius))
    publish(1,{"signed_columns":full_signed,"finite_direct_inverse":finite_evaluations(full)})
    # Get a proposal for the high-only coordinate correction using the same physical matrix.
    # Only the combined high-minus-low direct residual below is used as a certificate.
    high = [[api.zero]*96+col[96:] for col in coords]
    model = [dcp["pure"].complete_model_source(api,col,common["model2240"],common["source_b"]) for col in high]
    batch.COLS = 3
    zb = direct.complex_rows(c,batch,[[col[n] for col in model] for n in range(512)])
    vb = batch.complete_same_sign_image(c,common["alpha_pairs"],zb,-1)
    u,_ = direct.trial_from_matrix(c,matrix,batch.complex_columns(c,api,vb))
    proposal = np.ascontiguousarray(inverse @ (u.real.lo[:96,:]-u.imag.lo[:96,:]),dtype="<f8")
    require(proposal.shape==(96,3) and np.all(np.isfinite(proposal)), "three complete finite coordinate choices")
    io.real("ASQ25_original_coordinate_corrections",c.Box(proposal),exact=True)
    s = [[exact(api,v) for v in proposal[:,j]] for j in range(3)]
    difference = [[-v for v in g]+col[96:] for g,col in zip(s,coords)]
    actual = act(difference,"recovered_low_combined_residual")
    tnorm = api.rational(Fraction("2.694"))
    full_error_factor=(1+(tnorm*api.rational(Fraction("3.04")))**2).sqrt().upper()
    recovered = []
    for j in range(3):
        residual=norm(api,actual["signed_centres"][j])+actual["whole_upper_records"][j]["inverse_radius"]
        radius=(tnorm*residual+full_error_factor*errors[j]+api.rational(Fraction(".457"))*rawerr[j]).upper()
        recovered.append(signed_vector(api,np,[a+b for a,b in zip(coords[j][:96],s[j])],radius))
    publish(2,{"signed_recovered_columns":recovered,"combined_residual":finite_evaluations(actual),
               "all96_true_coordinates":True})
    physical_means = []
    for j in range(2):
        fee=(api.rational(Fraction(".681"))*rawerr[j]).upper()
        physical_means.append({k:(v+api.arb(0,fee)).str(74) for k,v in means[j].items()})
    publish(3,{"signed_negative_column_means":physical_means,
               "original_strict_independent_means":original["copied_complete_input_records"]["prior_two_independent_density_means"],
               "both_raw_residual_Grams":data["ASQ23"]["complete_suffix"]["grams"],
               "all_remaining_root_height_Robin_and_world_constraints_separate":True})
