"""Read-only admission for the complete WEJ posterior calculation.
This file never imports an old scientific producer. Complete old files are
checked by their immutable bytes and Git blob identities before JSON decoding.
The scientific consumer uses exact retained ball strings, including the
original nonuniform wrappers and the original local-process display fields.
"""
from __future__ import annotations
import copy, hashlib, json
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
PUBLIC = "Rogerhu12/math-research-public"

def compact(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),
                       ensure_ascii=False,allow_nan=False)+"\n").encode()

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def require(test, message):
    if not test:
        raise ValueError(message)

def at(value, path):
    for key in path:
        value=value[key]
    return value

def finite_shape(value, shape):
    """Pure JSON shape/literal check; no mathematical evaluation."""
    if isinstance(shape,dict) and set(shape)=={"ball"}:
        if shape["ball"].startswith("__NEW_"):
            return (isinstance(value,dict) and set(value)=={"ball"} and
                    isinstance(value["ball"],str) and bool(value["ball"]))
    if isinstance(shape,str) and shape.startswith("__TYPE_"):
        kind=shape[7:-2]
        return {"STRING":isinstance(value,str),"INTEGER":type(value) is int,
                "NUMBER":type(value) in (int,float),
                "BOOLEAN":type(value) is bool}[kind]
    if isinstance(shape,dict):
        return (isinstance(value,dict) and set(value)==set(shape) and
                all(finite_shape(value[k],v) for k,v in shape.items()))
    if isinstance(shape,list):
        return (isinstance(value,list) and len(value)==len(shape) and
                all(finite_shape(x,y) for x,y in zip(value,shape)))
    if type(shape) in (int,float):
        return type(value) in (int,float) and value==shape
    return type(value)==type(shape) and value==shape

def ball_count(value):
    if isinstance(value,dict):
        if set(value)=={"ball"} and isinstance(value["ball"],str):
            return 1
        return sum(ball_count(v) for v in value.values())
    if isinstance(value,list):
        return sum(ball_count(v) for v in value)
    return 0

def read_current_inputs(repository, manifest):
    root=Path(repository)
    docs={}; receipts=[]; complete_bindings={}
    for spec in manifest["files"]:
        relative=spec["path"]
        path=Path(relative)
        require(not path.is_absolute() and ".." not in path.parts and
                relative.startswith(TOPIC+"/"),"input left the exact topic")
        raw=(root/path).read_bytes()
        require(len(raw)==spec["bytes"] and digest(raw)==spec["sha256"],
                "complete current input bytes differ: "+spec["role"])
        blob=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
        require(blob==spec["git_blob_sha"],"complete current Git blob differs")
        text=raw.decode("utf-8")
        require(len(raw)<100000,"one current complete small input reaches100KB")
        receipts.append({k:spec[k] for k in
                         ("role","path","bytes","sha256","git_blob_sha")})
        if spec.get("read_as_json"):
            docs[spec["role"]]=json.loads(text)
        else:
            docs[spec["role"]]=text
    require(len(receipts)==manifest["expected_input_count"],
            "incomplete immutable current input closure")
    for spec in manifest["original_actual_inputs"]:
        role=spec["role"]; outer=docs[role]
        require(sorted(outer)==spec["outer_keys"],"old actual outer schema differs: "+role)
        science=at(outer,spec["scientific_root"])
        require(sorted(science)==spec["scientific_keys"],"old actual scientific schema differs")
        for check in spec["exact_checks"]:
            require(at(outer,check["path"])==check["value"],
                    "old actual identity/domain field differs: "+role+"/"+str(check["path"]))
        gates=at(outer,spec["gates_path"]) if spec["gates_path"] is not None else []
        if spec["gates_path"] is not None:
            require(gates==spec["complete_original_gates"] and
                    len(gates)==spec["gate_count"] and
                    all(g.get("passed") is True for g in gates),
                    "one complete original mathematical gate differs: "+role)
        require(spec["gate_count"]==len(gates),"original gate count differs")
        complete_bindings[role]={
            "original_file":next(copy.deepcopy(r) for r in receipts if r["role"]==role),
            "scientific_root":copy.deepcopy(spec["scientific_root"]),
            "complete_original_gates":copy.deepcopy(gates),
            "complete_exact_identity_and_domain_fields":[
                {"path":copy.deepcopy(c["path"]),"value":copy.deepcopy(at(outer,c["path"]))}
                for c in spec["exact_checks"]],
            "outer_schema_retained":True,"scientific_schema_retained":True,
            "original_complete_file_remains_at_immutable_public_identity":True}
    return docs,receipts,complete_bindings

def scientific(docs, role):
    value=docs[role]
    return value["actual_scientific_receipt"] if "actual_scientific_receipt" in value else value

def projected_ball(value):
    """Exact string projection only. Full original display object is retained separately."""
    if isinstance(value,str):
        return {"ball":value}
    require(isinstance(value,dict) and isinstance(value.get("ball"),str),
            "missing complete original ball string")
    return {"ball":value["ball"]}

def original_records_and_conclusions(docs, manifest):
    records={}; originals={}
    for spec in manifest["consumed_original_records"]:
        value=at(docs[spec["role"]],spec["path"])
        require(value==spec["original_value"],"one exact original consumed record differs")
        originals[spec["name"]]=copy.deepcopy(value)
        records[spec["name"]]=projected_ball(value)
        require(records[spec["name"]]["ball"]==spec["ball_string"],
                "an old ball was reformatted")
    conclusions={}
    for spec in manifest["complete_old_conclusions"]:
        key=spec["name"]
        conclusions[key]={"role":spec["role"],"path":copy.deepcopy(spec["path"]),
                         "complete_value":copy.deepcopy(at(docs[spec["role"]],spec["path"]))}
    return records,originals,conclusions

def verify_WGS_pair(docs):
    main=docs["WGS_main"]; copies=docs["WGS_original_inputs"]
    require(main["complete"] is True and main["proved"] is True and
            main["actual_returncode"]==0 and main["failure"] is None and
            copies["complete"] is True,"incomplete actual WGS pair")
    ref=main["complete_original_inputs_file"]
    require(set(ref)=={"filename","bytes","sha256"} and
            ref["filename"]=="complete-original-inputs.json" and
            ref["bytes"]==31632 and
            ref["sha256"]=="3c5588f13de4dc544f519b2fb99f372bba3200ccee79def665ce5bd1d3c3dd66",
            "WGS main's complete-input reference changed")
    require(digest(compact(copies))==ref["sha256"] and
            len(compact(copies))==ref["bytes"],"WGS complete copied inputs differ")
    for key in ("run_id","run_attempt","source_sha256","math_module_sha256",
                "input_manifest_sha256","actual_scientific_checkout_commit"):
        require(main[key]==copies[key],"WGS actual two-file identity differs")
    require(main["run_id"]=="43820816332" and main["run_attempt"]=="1",
            "different actual complete WGS run")
    require(len(main["gates"])==24 and all(g["passed"] is True for g in main["gates"]),
            "incomplete actual WGS gate set")
    require(main["new_scalar_slots"]==437 if "new_scalar_slots" in main else
            main["planned_shape"]["new_scalar_slots"]==437,
            "incomplete WGS finite-jet count")
    return True

def fixed_qualifications():
    return {
      "mean_bridge":{
        "FA2_full_24_gate_success":True,"cut_record_qualified_at_rc":True,
        "same_original_germ_2549":True,"same_real_family_and_intrinsic_parameter":True,
        "V10_ordinary_radial_covers_rc_to_root_plus":True,
        "eta_equals_minus_gamma_mean":True,"eta_log_r_is_eta1_over_em":True},
      "waist":{
        "same_selected_real_member":True,"same_original_root_cutoff_97_input":True,
        "complete_WGS_pair_admitted":False,
        "same_WES_waist_free_neighbourhood_minus_T_gt_L":True,
        "same_WZR_metric_beta_zero_at_waist":True,"same_N_actual_angular_operator":True,
        "ordinary_radial_amplitude_derivatives_retained":True,
        "complete_extended_first_amplitude_admitted":False,
        "same_SP_actual_waist_density_q_and_mean_records":True,
        "same_WT_Js_268435456_whole_forward_remainder":True,
        "same_SW_W_bound_before_waist_ng":True,
        "original_physical_means_and_transported_input_retained":True}}

def verify_analytic_admission(docs, records, api):
    """Only comparisons of already printed original bounds, no old target evaluation."""
    potential=scientific(docs,"potential"); case=potential["cases"][3]
    require(case["exact_complex_radial_radius"]=="1/6000" and
            case["exact_support_radius"]=="3/8000" and
            case["all_integer_modes_abs_j_at_least"]==97 and
            case["physical_mean_is_not_z_zero_limit"] is True and
            case["independent_even_mean_equation_retained"] is True,
            "different complete original potential domain")
    require(api.read_up(case["complete_modulus_upper"]["V"])<api.ex(276) and
            api.read_lower(case["reference_image"]["complete_image_disk_radius_lower"],
                           "old complete potential image")>api.ex(7)/api.ex(10000),
            "the old complete potential does not pay the new extension domain")
    reference=scientific(docs,"genuine_reference")["reference_columns"]
    require(reference["exact_real_T_interval"]==["-1/2000","1/2000"] and
            reference["both_independent_columns_retained"] is True and
            reference["both_carrier_signs_retained"] is True and
            reference["ordinary_two_source_rows_retained"] is True and
            reference["physical_mean_is_not_z_zero_limit"] is True,
            "different complete genuine reference")
    require(api.read_up(reference["negative_relative_basis_and_inverse_factor"])
            <api.ex(6)/api.ex(5),"old genuine signed profile constant not admitted")
    wt=scientific(docs,"WT")
    require(wt["complete_fixed_cutoff_results"][1]["J"]==268435456 and
            wt["complete_fixed_cutoff_results"][1]["inverse_on_both_windows_proved"] is True,
            "different whole waist normalizer")
    sp=scientific(docs,"SP")
    require(sp["complete_endpoint_readout_conclusion"]["exact_cut"]==
            "2333968743003/10000000000000" and
            sp["mathematical_parameters"]["original_strict_complete_rows"]==3071 and
            sp["mathematical_parameters"]["complete_mean_coordinates"]==2,
            "different complete PW reception or interface set")
    fa=scientific(docs,"FA2")
    require(fa["mathematical_parameters"]["physical_root_piece"]==2549 and
            fa["mathematical_parameters"]["exact_strict_cut"]==
            "76285779072683/320000000000000" and
            fa["mathematical_parameters"]["exact_root_interval"]==
            ["1191984371497/5000000000000","2383968743003/10000000000000"],
            "different full-germ mean bridge")
    wsp=scientific(docs,"WSP")
    prior=wsp["complete_prior_scientific_conclusion_read_verbatim"]
    require(digest(compact(prior))==
            "e2cb2aacc031532e3b4db92873b404e9550599da75427dbb3c6448b65120d88d"
            and len(compact(prior))==55533,
            "the complete original Calg/root-finite scientific result changed")
    require(wsp["complete_new_positive_correction"]["same_original_positive_operator"] is True
            and wsp["complete_new_positive_correction"]["physical_pair_and_two_means_retained"] is True,
            "different whole positive operator")
    require(scientific(docs,"WX")["complete_selected_H_coordinate_conclusion"][
            "only_same_selected_actual_conjugacy"] is True,
            "unqualified selected left coordinate")
    require(scientific(docs,"NIF")["complete_coordinate_conclusion"]["windows"][
            "-4/3"]["same_inverse_in_the_two_windows"] is True,
            "different fixed reflected right-input inverse")
    return fixed_qualifications()

def complete_input_documents(docs, receipts, bindings, originals, conclusions, manifest):
    admission={
      "kind":"complete_WEJ_original_actual_input_admission_v1","complete":True,
      "original_file_count":len(bindings),
      "complete_original_actual_bindings":bindings,
      "complete_current_file_receipts":receipts,
      "complete_scientific_parameter_contract":copy.deepcopy(manifest["parameters"]),
      "read_only_scope":"complete immutable current files; zero historical restoration and zero old producer calls",
      "same_selected_real_member_only":True,
      "WGS_geometry_and_amplitudes_are_sup_not_A0":True,
      "strict_d_A0_has_its_independent_original_Banach_product_and_primitive_proof":True,
      "all_old_successes_and_original_failure_qualifications_retained":True}
    consumed={
      "kind":"complete_WEJ_consumed_original_conclusions_v1","complete":True,
      "complete_original_consumed_record_objects":originals,
      "complete_old_conclusions":conclusions,
      "complete_WGS_original_files":{
          role:copy.deepcopy(next(r for r in receipts if r["role"]==role))
          for role in ("WGS_main","WGS_original_inputs")},
      "WGS_full_graphs_read_from_their_complete_immutable_original_files":True,
      "WGS_437_slots_and_all_66_plus_40_original_records_not_recomputed":True,
      "no_partial_or_truncated_source_conclusion_substituted":True,
      "all_false_scope_flags_in_selected_complete_conclusions_retained":True}
    return admission,consumed
