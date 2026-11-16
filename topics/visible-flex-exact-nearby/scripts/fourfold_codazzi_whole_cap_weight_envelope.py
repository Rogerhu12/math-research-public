#!/usr/bin/env python3
"""New whole-physical-cap p=2/p=4 envelopes from completed RW and SC3 records.
No old producer, Gram, Hessian, profile integral, or signed97 model is evaluated.
"""
from __future__ import annotations
import argparse,copy,gzip,hashlib,json,os,platform,time
from fractions import Fraction
from pathlib import Path
import flint
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
KIND="actual_whole_cap_weight_envelope_p2_p4_v1"
MANIFEST_KIND="whole_cap_weight_envelope_public_inputs_v1"
RUNTIME=dict(python="3.12.14",python_flint="0.9.0")
CONTRACT="ff118cc75152796bf68de616b43e6e6fac0f6d1eb859ce0af2ef73f36ea40462"
PARAMETERS=json.loads("{\"arithmetic_bits\":320,\"physical_frequency_factor\":4,\"physical_angular_measure\":\"normalized full physical circle\",\"ordinary_radial_measure\":\"dr\",\"exact_cap_interval\":[\"9/10\",\"25/8\"],\"exact_cap_length\":\"89/40\",\"actual_cap_radius\":\"3/1000000\",\"actual_outer_C_nonmean_radius\":\"99/100000000000\",\"delta_half_width\":\"1/10000000000\",\"full_inner_gamma_radius\":\"1/1000000000\",\"tail_inner_gamma_radius\":\"1/128000000000\",\"normalized_outer_height_radius\":\"1/1152921504606846976\",\"known_selected_left_shift_factor\":10,\"nonlinear_pointwise_quadratic_factor\":13,\"weight_fractions\":[\"1/16\",\"1/8\",\"1/4\",\"3/8\",\"1/2\",\"3/4\"],\"integral_powers\":[2,4],\"same_physical_unknown\":\"y=W_star(gamma,f)-W_hat at ac1/440866; no body recentering\",\"candidate_sha256\":\"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413\",\"continuous_centre_definition_sha256\":\"440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47\",\"current_input_count\":11,\"expected_actual_gate_count\":22,\"new_weight_domain_pairs\":12,\"new_closed_integrals\":24,\"all_old_successful_scientific_calls_allowed\":0,\"new_old_Gram_or_Hessian_or_signed_model_evaluations_allowed\":0,\"complete_nonlinear_or_trace_gate_claimed\":false}")
OLD=json.loads("{\"RW\":{\"kind\":\"actual_true_cap_radial_weighted_and_left_receivers_v1\",\"science_sha256\":\"ec6e088f2d361b35c938eb94bfe78d284507376b4d859c7eadc44c2635316ca9\",\"science_bytes\":57702,\"source_sha256\":\"f8d97a14aa7c2ebac746a9732e7b9fd00bf939db95b2b610edcd47f22f9388bb\",\"manifest_sha256\":\"333bff731ec491b362feb665b54bcb2173bbbdc571f3459e03b63a63af72a3af\",\"process_sha256\":\"daabac142b01e886d7bf3e3f9f53820cb6fb7c053e44a78972d4313ac4bb66e6\",\"process_kind\":\"actual_public_radial_weighted_cap_receivers_process_v1\",\"run_id\":\"43729429382\",\"run_attempt\":\"1\",\"gates\":15},\"SC\":{\"kind\":\"actual_complete97_signed_radial_subtracted_cap_affine_v1\",\"science_sha256\":\"f0838341d4f661714328da407c9a45f7ef137c43e8ab1ca7f4adfc2b12e7893c\",\"science_bytes\":23672,\"source_sha256\":\"41b8f50cd7faafc438f37f3f4514caa24142af63d9921044d91ead67d6fcd1dd\",\"manifest_sha256\":\"cd28e23a13ef68281dd4813de793896e89b235926936d2668e64e7bfe6e22aa9\",\"execution_sha256\":\"9ce9955fade952563c6d2dc2ca7650b43a3752d3b10e9051a798ffd73fe2c5e9\",\"execution_kind\":\"actual_public_complete97_signed_cap_affine_execution_v1\",\"run_id\":\"43754452928\",\"run_attempt\":\"1\",\"gates\":20,\"helper_sha256\":\"6f868fafd82a62c7c7a3a04bebbb0da1363209c80097f218f086781d37f2efb4\",\"reader_sha256\":\"a7c099608ec6ef1504a1d30b9cabbe9232bdd1dfd0390e28bbfd9fc836772ad0\",\"actual_runtime\":{\"bits\":256,\"packages\":{\"numpy\":\"2.3.5\",\"python-flint\":\"0.9.0\"},\"python\":\"3.12.14\"}}}")
PINNED=json.loads("{\"RW_science\":\"ec6e088f2d361b35c938eb94bfe78d284507376b4d859c7eadc44c2635316ca9\",\"RW_process\":\"daabac142b01e886d7bf3e3f9f53820cb6fb7c053e44a78972d4313ac4bb66e6\",\"RW_source\":\"f8d97a14aa7c2ebac746a9732e7b9fd00bf939db95b2b610edcd47f22f9388bb\",\"SC_science\":\"f0838341d4f661714328da407c9a45f7ef137c43e8ab1ca7f4adfc2b12e7893c\",\"SC_execution\":\"9ce9955fade952563c6d2dc2ca7650b43a3752d3b10e9051a798ffd73fe2c5e9\",\"SC_source\":\"41b8f50cd7faafc438f37f3f4514caa24142af63d9921044d91ead67d6fcd1dd\",\"SA_contract\":\"85e07aba2d895c160be6c307da9ff0740fb817bbad6f3813d0acf3242e0f35d1\"}")

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)
def payload_sha(x):return hashlib.sha256(canonical(x).encode()).hexdigest()
def read(path):return json.loads(Path(path).read_bytes())
def save(path,x,compressed=False):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(canonical(x)+"\n").encode()
    body=gzip.compress(raw,mtime=0) if compressed else raw
    tmp=path.with_name(path.name+".tmp");tmp.write_bytes(body);tmp.replace(path)
def rb(x):
    if isinstance(x,arb):return x
    return arb(x["ball"] if isinstance(x,dict) else x)
def rat(x):
    q=Fraction(x);return arb(q.numerator)/q.denominator
def up(x):
    x=rb(x)
    if not x.is_finite() or x.lower()<0:
        raise ValueError("a complete nonnegative budget is not finite and nonnegative")
    return x.upper()
def positive_lower(x):
    x=rb(x)
    if not x.is_finite() or not x.lower()>0:
        raise ValueError("a required complete denominator has no strict positive lower bound")
    return x.lower()
def rec(x):return dict(ball=rb(x).str(60))
def sqrt_up(x):return up(up(x).sqrt())
def finite(x):
    if isinstance(x,dict):
        if "ball" in x:return rb(x).is_finite()
        return all(finite(v) for v in x.values())
    if isinstance(x,(list,tuple)):return all(finite(v) for v in x)
    if isinstance(x,arb):return x.is_finite()
    return True
def whole_choice(rows,field):
    entries=copy.deepcopy(rows)
    for row in entries:up(row[field])
    selected=min(range(len(entries)),key=lambda i:rb(entries[i][field]).upper())
    return dict(complete_candidate_records=entries,selected_complete_candidate=selected,
        complete_selected_record=copy.deepcopy(entries[selected]),
        complete_selected_upper=copy.deepcopy(entries[selected][field]),
        same_complete_object_and_domain=True,no_entrywise_mixing=True)
def persist(a,d):
    save(a.process_receipt,d);save(a.small_summary,d)

NEW_RESULT_FIELDS=("new_completed_weight_domain_rows","complete_new_whole_posterior_conclusion")

def decode_new_result_table(table):
    """Lossless plain-JSON column tables: null begins a list; an integer begins a dict row."""
    if not isinstance(table,dict) or table.get("encoding")!="lossless_named_column_tables_v1":
        raise ValueError("unrecognized complete new-result table encoding")
    schemas=table.get("object_fields")
    if not isinstance(schemas,list) or not all(isinstance(keys,list)
        and all(isinstance(k,str) for k in keys) and keys==sorted(set(keys)) for keys in schemas):
        raise ValueError("invalid complete named column schemas")
    def decode(value):
        if not isinstance(value,list):
            if isinstance(value,dict):
                raise ValueError("all nested new dictionaries must use a named column schema")
            return value
        if not value:
            raise ValueError("an encoded sequence needs its explicit type")
        if value[0] is None:
            return [decode(x) for x in value[1:]]
        index=value[0]
        if type(index) is not int or not 0<=index<len(schemas) or len(value)!=len(schemas[index])+1:
            raise ValueError("a complete new-result row does not match its named columns")
        return {k:decode(v) for k,v in zip(schemas[index],value[1:])}
    result=decode(table.get("value"))
    if not isinstance(result,dict) or set(result)!=set(NEW_RESULT_FIELDS):
        raise ValueError("the complete new-result table must retain both original collections")
    return result

def complete_scientific_document(value):
    """Expand only the two repeated new collections; all original scalar records remain verbatim."""
    if not isinstance(value,dict):
        raise ValueError("a complete scientific receipt must be an object")
    if "complete_new_result_field_table" not in value:
        return value
    if any(k in value for k in NEW_RESULT_FIELDS):
        raise ValueError("duplicate encoded and unencoded new-result collections")
    result=dict(value)
    table=result.pop("complete_new_result_field_table")
    result.update(decode_new_result_table(table))
    return result

def publication_document(value):
    """Keep every field and ball string while listing repeated column names only once."""
    result=copy.deepcopy(value);schemas=[];indices={}
    def encode(x):
        if isinstance(x,dict):
            keys=tuple(sorted(x))
            if keys not in indices:
                indices[keys]=len(schemas);schemas.append(list(keys))
            return [indices[keys]]+[encode(x[k]) for k in keys]
        if isinstance(x,list):
            return [None]+[encode(v) for v in x]
        return x
    original={k:result.pop(k) for k in NEW_RESULT_FIELDS}
    encoded=encode(original)
    result["complete_new_result_field_table"]=dict(
        encoding="lossless_named_column_tables_v1",object_fields=schemas,value=encoded)
    if decode_new_result_table(result["complete_new_result_field_table"])!=original:
        raise ValueError("the complete new-result table failed an exact JSON round trip")
    result["lossless_new_result_table_validated"]=True
    return result

def checked_inputs(a,d,gate):
    runtime=dict(python=platform.python_version(),python_flint=flint.__version__)
    d["runtime"]=runtime
    gate("only the new scalar envelope arithmetic runs in public Actions at the fixed runtime",
        os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==PUBLIC
        and runtime==RUNTIME and ctx.prec==320)
    m=read(a.manifest);paths={k:a.repo_root/Path(v) for k,v in m["input_paths"].items()}
    gate("eleven current small text inputs and all new mathematical parameters are fixed",
        m["kind"]==MANIFEST_KIND and m["public_repository"]==PUBLIC
        and m["source_sha256"]==m["scientific_source_sha256"]==sha(__file__)
        and m["contract_sha256"]==CONTRACT and m["mathematical_parameters"]==PARAMETERS
        and m["expected_actual_gate_count"]==22 and m["file_count"]==len(m["files"])==11
        and m["all_inputs_are_current_small_texts"] is True and m["legacy_artifact_inputs"]==[]
        and m["old_successful_scientific_calls_allowed"]==0
        and set(m["input_paths"].values())=={x["path"] for x in m["files"]})
    gate("every complete input size and SHA is checked without binary or archive restoration",
        all((a.repo_root/Path(x["path"])).stat().st_size==x["bytes"]
            and sha(a.repo_root/Path(x["path"]))==x["sha256"] and x["bytes"]<100000
            and Path(x["path"]).suffix in (".py",".md",".json")
            and not (a.repo_root/Path(x["path"])).read_bytes().startswith(b"\x1f\x8b")
            for x in m["files"])
        and all(sha(paths[k])==v for k,v in PINNED.items()) and sha(paths["contract"])==CONTRACT)
    rwsource=paths["RW_source"].read_text();scsource=paths["SC_source"].read_text()
    gate("the original complete rate and same physical posterior definitions are text evidence only",
        all(term in rwsource for term in
            ('def weighted_kernel(', '"lambda_max":exact(max(profile))',
             'OUT_RIGHT=Fraction(19,20)', 'if h<=OUT_RIGHT:'))
        and all(term in scsource for term in
            ('def posterior(', '(D+13*rho*Q)*row["Y"]',
             'unknown_y_remains_actual_cap_minus_repaired_centre=True',
             'ordinary_jet_order=3', 'known_shift=rat('))
        and all(term in paths["SA_contract"].read_text() for term in
            (r"\tag{SA.3}",r"\tag{SA.16}",r"\tag{SA.22}",
             r"|{\cal R}_Q(y)|\le13|y|_{\mathbb R^2}^2"))
        and all(term in paths["contract"].read_text() for term in
            (r"\tag{CEB.13}",r"\tag{CEB.22}",r"\tag{CEB.25}",r"\tag{CEB.27}"))
        and m["old_scientific_source_files_are_identity_evidence_not_imported"] is True)
    d["input_sha256"]={k:sha(paths[k]) for k in ("contract",*PINNED)}
    d["original_successful_small_receipts_read"]=4
    return paths

def accepted_records(paths,d,gate):
    rw=read(paths["RW_science"]);rp=read(paths["RW_process"])
    sc=read(paths["SC_science"]);se=read(paths["SC_execution"])
    ro=OLD["RW"];so=OLD["SC"]
    gate("RW is the original complete child0 fifteen-gate six-weight success",
        rw.get("kind")==ro["kind"] and rw.get("complete") is True
        and rw.get("failure") is None and rw.get("actual_returncode")==0
        and rw.get("source_sha256")==ro["source_sha256"]
        and rw.get("input_manifest_sha256")==ro["manifest_sha256"]
        and len(rw.get("gates",[]))==15 and all(x.get("passed") is True for x in rw["gates"])
        and rw.get("new_weighted_candidates_evaluated")==6
        and rw.get("new_weighted_posterior_cases_passed")==6
        and rp.get("kind")==ro["process_kind"] and rp.get("complete") is True
        and rp.get("run_id")==ro["run_id"] and rp.get("run_attempt")==ro["run_attempt"]
        and rp.get("actual_source_sha256")==ro["source_sha256"]
        and rp.get("input_manifest_sha256")==ro["manifest_sha256"]
        and len(rp.get("children",[]))==1 and rp["children"][0].get("actual_returncode")==0)
    gate("the complete RW small science and its process fields are exactly linked",
        rp.get("actual_scientific_summary_sha256")==ro["science_sha256"]
        and rp.get("actual_scientific_summary_bytes")==ro["science_bytes"]
        and rp.get("actual_scientific_complete") is True and rp.get("actual_scientific_failure") is None
        and rp.get("actual_scientific_gates")==rw["gates"]
        and rp.get("actual_parameters")==rw["parameters"]
        and rp.get("actual_weighted_candidate_count")==rp.get("actual_weighted_posterior_case_pass_count")==6
        and rw.get("candidate_sha256")==PARAMETERS["candidate_sha256"]
        and rw.get("derived_continuous_centre_definition_sha256")==PARAMETERS["continuous_centre_definition_sha256"])
    gate("all six complete whole-cap weighted solution priors keep both means and their original domains",
        list(rw["new_weighted_candidates"])==PARAMETERS["weight_fractions"]
        and rw["original_counts"]==dict(raw_complete_rows=7296,reference_rows=949,
             cap_residual_rows=1341,old_complete_intersections=1346)
        and rw["parameters"]["exact_cap_interval"]==PARAMETERS["exact_cap_interval"]
        and rw["parameters"]["right_body_output_interval"]==["9/10","19/20"]
        and rw["parameters"]["ordinary_radial_measure"]=="dr"
        and rw["parameters"]["physical_angular_measure"]=="normalized circle"
        and rw["parameters"]["full_mean_included"] is True
        and rw["parameters"]["actual_cap_radius"]==PARAMETERS["actual_cap_radius"]
        and rw["parameters"]["inner_curvature_radius"]==PARAMETERS["full_inner_gamma_radius"]
        and rw["parameters"]["tail_inner_curvature_radius"]==PARAMETERS["tail_inner_gamma_radius"]
        and rw["parameters"]["normalized_outer_height_radius"]==PARAMETERS["normalized_outer_height_radius"]
        and all(row["complete_weighted_posterior_applies"] is True
            and row["candidate_failure"] is None and row["both_mean_denominators_retained"] is True
            and row["input_gamma_is_physical_nonmean_curvature"] is True
            and row["all_M_in_4N_including_unbounded_frequency"] is True
            for row in rw["new_weighted_candidates"].values()))
    gate("SC3 is the completed original twenty-gate signed97 success with its exact runtime",
        sc.get("kind")==so["kind"] and sc.get("complete") is True and sc.get("failure") is None
        and sc.get("actual_returncode")==0 and sc.get("actual_new_signed_functional_complete") is True
        and sc.get("source_sha256")==so["source_sha256"]
        and sc.get("input_manifest_sha256")==so["manifest_sha256"]
        and sc.get("helper_sha256")==so["helper_sha256"] and sc.get("reader_sha256")==so["reader_sha256"]
        and sc.get("actual_runtime")==so["actual_runtime"]
        and sc.get("expected_gate_count")==20 and len(sc.get("gates",[]))==20
        and all(x.get("passed") is True for x in sc["gates"])
        and se.get("kind")==so["execution_kind"] and se.get("complete") is True
        and se.get("run_id")==so["run_id"] and se.get("run_attempt")==so["run_attempt"]
        and se.get("actual_returncode")==0 and se.get("actual_failure") is None
        and se.get("actual_new_scientific_processes")==1
        and se.get("source_sha256")==so["source_sha256"]
        and se.get("input_manifest_sha256")==so["manifest_sha256"]
        and se.get("actual_scientific_runtime")==so["actual_runtime"])
    identity=sc["scientific_identity"];receipt=se["scientific_conclusion"]
    gate("SC3 output SHA size full model identities and direct RW input links match the successful record",
        receipt.get("complete") is True and receipt.get("actual_returncode")==0
        and receipt.get("bytes")==so["science_bytes"] and receipt.get("sha256")==so["science_sha256"]
        and receipt.get("actual_gate_count")==receipt.get("actual_passed_gate_count")==20
        and receipt.get("original_result_printed_before_any_format_gate") is True
        and any(x.get("file")=="actual-scientific-conclusion.json"
            and x.get("bytes")==so["science_bytes"] and x.get("sha256")==so["science_sha256"]
            for x in se.get("output_hashes",[]))
        and identity["source_sha256"]==so["source_sha256"]
        and identity["input_sha256"]["candidate"]==rw["candidate_sha256"]
        and identity["input_sha256"]["RW_science"]==ro["science_sha256"]
        and identity["input_sha256"]["RW_process"]==ro["process_sha256"]
        and identity["input_sha256"]["SA_contract"]==PINNED["SA_contract"])
    cover=sc["complete_body_cover"];p=sc["parameters"];u=sc["unchanged_unknown_operator_bounds"]
    gate("the same complete physical body formal norms mean and continuous97 trial are retained",
        cover["exact_interval"]==PARAMETERS["exact_cap_interval"]
        and cover["groups"]==32 and cover["intersections"]==cover["quarters"]==7908
        and cover["original_pilot_rows"]==4 and cover["shared_slice_joins"]==31
        and cover["old_QR_target_Gram_or_residual_calls"]==0 and cover["true_first_Hermite_extension"] is True
        and p["body_HS_uppers_are_norms"] is True and p["endpoint_Gram_traces_are_squared"] is True
        and p["unknown_y_remains_actual_cap_minus_repaired_centre"] is True
        and p["Q_quadratic_value_factor"]==13 and p["orthonormal_inputs"]==97
        and p["physical_test_modes"]==128 and u["Hessian_Gram_added"] is False
        and u["internal_value_jump_norms_exactly_zero"] is True
        and sc["full_original_mean_and_same97_input_space_retained"] is True)
    acc=sc["complete_error_accounting"]
    gate("selected left changes known outer terms and gamma conditions never recenter the physical body",
        p["delta_half_width"]==PARAMETERS["delta_half_width"]
        and p["actual_cap_radius"]==PARAMETERS["actual_cap_radius"]
        and p["actual_outer_C_nonmean_radius"]==PARAMETERS["actual_outer_C_nonmean_radius"]
        and p["full_inner_gamma_radius"]==PARAMETERS["full_inner_gamma_radius"]
        and p["tail_inner_gamma_radius"]==PARAMETERS["tail_inner_gamma_radius"]
        and p["normalized_outer_height_radius"]==PARAMETERS["normalized_outer_height_radius"]
        and p["known_selected_physical_global_pair_sup_factor"]==10
        and acc["no_global_y_recentring_or_new_unknown_smallness"] is True
        and acc["independent_mean_height_lambda_waist_and_core_high_inputs_not_removed"] is True
        and acc["old_RW_weight_integrals_and_old_Gram_integrals_recomputed"]==0
        and sc["complete_numerical_error_scope"]["no_second_addition_of_embedded_errors"] is True
        and all(v==0 for v in sc["original_input_recomputation"].values())
        and all(sc[k] is False for k in
            ("new_core_selfmap_claimed","new_full_BVP_inverse_claimed",
             "new_global_surface_claimed","new_low_trace_gate_claimed")))
    rows=sc["complete_posterior_rows"]
    gate("both original complete posterior rows have their full domain and exact selected-trace condition",
        len(rows)==2 and [x["domain"] for x in rows]==
            ["full_original_cap_product","tail_inner_curvature_subdomain"]
        and all(x["complete_prior_candidates"]==7
            and x["same_true_input_gamma_must_equal_the_selected_physical_C_trace"] is True
            for x in rows))
    return rw,sc

def scalar_copies(rw,sc,d,gate):
    u=sc["unchanged_unknown_operator_bounds"];a=sc["complete_error_accounting"];p=sc["parameters"]
    saved=dict(D=copy.deepcopy(u["unweighted_formal_ordinary_norm"]),
        Q=copy.deepcopy(u["complete_q_star_norm"]),
        ELdelta=copy.deepcopy(a["selected_left_defect_norm"]),
        ER=copy.deepcopy(u["outer_nonmean_defect_norm"]),
        ZB=copy.deepcopy(u["outer_B_field_norm"]),Zm=copy.deepcopy(u["outer_Cmean_field_norm"]),
        known_uniform=copy.deepcopy(a["uniform_known_parameter_model_norm"]),
        known_outer=copy.deepcopy(a["complete_outer_omission_norm"]),
        selected_left_shift=copy.deepcopy(a["complete_selected_known_left_shift"]),
        LD=copy.deepcopy(p["true_outer_D_Lipschitz"]),Lm=copy.deepcopy(p["true_outer_Cmean_Lipschitz"]))
    weights={}
    for k,row in rw["new_weighted_candidates"].items():
        weights[k]=dict(X_affine=copy.deepcopy(row["posterior_bounds"]["Xw_affine"]),
            X_gamma=copy.deepcopy(row["posterior_bounds"]["Xw_gamma_gain"]),
            lambda_max=copy.deepcopy(row["complete_kernel_bounds"]["lambda_max"]),
            weight_R=copy.deepcopy(row["new_source_and_output_integrals"]["weight_R"]),
            lambda_min_read_verbatim=copy.deepcopy(row["complete_kernel_bounds"]["lambda_min"]))
    gate("eleven complete source endpoint and known records plus thirty weight records are finite and typed",
        len(saved)==11 and len(weights)==6 and finite(saved) and finite(weights)
        and all(rb(v).lower()>=0 for v in saved.values())
        and all(rb(w["X_affine"]).lower()>=0 and rb(w["X_gamma"]).lower()>=0
            and rb(w["lambda_min_read_verbatim"]).lower()>0
            and rb(w["lambda_max"]).lower()>=rb(w["lambda_min_read_verbatim"]).upper()
            and rb(w["weight_R"]).lower()>0 and rb(w["weight_R"]).upper()<=1
            for w in weights.values()))
    originals=dict(RW_complete_scope=copy.deepcopy(rw["scope"]),
        RW_original_counts=copy.deepcopy(rw["original_counts"]),
        SC_complete_body_cover=copy.deepcopy(sc["complete_body_cover"]),
        SC_complete_unknown_operator_bounds=copy.deepcopy(sc["unchanged_unknown_operator_bounds"]),
        SC_complete_error_accounting=copy.deepcopy(sc["complete_error_accounting"]),
        SC_complete_posterior_rows=copy.deepcopy(sc["complete_posterior_rows"]))
    d["complete_saved_scalar_records_read_verbatim"]=saved
    d["complete_saved_weight_records_read_verbatim"]=weights
    d["complete_old_objects_read_verbatim"]=originals
    d["complete_saved_scalar_payload_sha256"]=payload_sha(saved)
    d["complete_saved_weight_payload_sha256"]=payload_sha(weights)
    d["complete_old_object_payload_sha256"]=payload_sha(originals)
    d["saved_scalar_records_read"]=41
    d["original_complete_objects_read_verbatim"]=6
    d["complete_original_SC_signed97_model_sha256"]=payload_sha(sc["complete_signed97_parameter_model"])
    d["complete_original_SC_scientific_identity_sha256"]=payload_sha(sc["scientific_identity"])
    d["complete_original_SC_numerical_error_scope_sha256"]=payload_sha(sc["complete_numerical_error_scope"])
    d["old_whole_SC_posteriors_read_not_recomputed"]=True
    return saved,weights

def envelope_setup(rho,X,a,length,d):
    rho,X,a,length=map(up,(rho,X,a,length))
    audit=dict(rho_upper=rec(rho),X_upper=rec(X),lambda_upper=rec(a),length_upper=rec(length))
    if rho==0 or X==0 or length==0:branch="zero"
    elif a==0:branch="zero_rate"
    elif X>=rho:branch="capped_from_left"
    elif X<rho:
        tstar=(rho/X).log()/a
        if not tstar.is_finite() or tstar.lower()<0:
            raise ValueError("the new exact crossing time is not finite and nonnegative")
        d["new_crossing_logarithms_evaluated"]+=1
        audit["complete_crossing_time_ball"]=rec(tstar)
        if tstar.upper()<=length.lower():branch="crossing"
        elif tstar.lower()>=length.upper():branch="uncapped_whole_interval"
        else:branch="uncertain_crossing_use_complete_existence_ball"
        audit["crossing_decided_without_midpoints"]=True
    else:
        branch="uncertain_left_order_use_complete_existence_ball"
    audit["branch"]=branch
    return dict(rho=rho,X=X,a=a,length=length,
        tstar=tstar if "tstar" in locals() else None,branch=branch,audit=audit)

def closed_integral(power,env,d):
    if power not in (2,4):raise ValueError("only the new p2 and p4 complete targets are permitted")
    rho,X,a,length=(env[k] for k in ("rho","X","a","length"));branch=env["branch"]
    full=up((rho**power)*length)
    if branch=="zero":value=arb(0)
    elif branch=="zero_rate":value=up(length*min(rho,X)**power)
    elif branch in ("capped_from_left","uncertain_crossing_use_complete_existence_ball",
                    "uncertain_left_order_use_complete_existence_ball"):value=full
    elif branch=="crossing":
        t=env["tstar"]
        value=up(((rho**power)-(X**power))/(power*a)+(rho**power)*(length-t))
    elif branch=="uncapped_whole_interval":
        value=up((X**power)*((power*a*length).exp()-1)/(power*a))
        d["new_closed_integral_exponentials_evaluated"]+=1
    else:raise ValueError("unrecognized complete interval branch")
    d["new_closed_integrals_evaluated"]+=1
    candidates=[dict(kind="complete_closed_integral",upper=rec(value)),
        dict(kind="complete_existence_ball",upper=rec(full))]
    choice=whole_choice(candidates,"upper")
    return dict(power=power,branch=branch,
        complete_existence_ball_upper=rec(full),complete_integral_upper=choice["complete_selected_upper"],
        selected_integral_bound_kind=choice["complete_selected_record"]["kind"],
        ordinary_radial_measure="dr",full_interval_included=True,
        no_original_weight_profile_or_integral_recomputed=True)

def complete_weight_candidate(domain,gamma,k,w,saved,a,d):
    rho=rat(PARAMETERS["actual_cap_radius"])
    length=rat(PARAMETERS["exact_cap_length"])
    X=up(rb(w["X_affine"])+gamma*rb(w["X_gamma"]))
    d["new_affine_substitutions_evaluated"]+=1
    env=envelope_setup(rho,X,rb(w["lambda_max"]),length,d)
    partial=dict(domain=domain,weight=k,physical_gamma_A0_upper=rec(gamma),
        complete_same_weight_envelope=env["audit"],completed_integrals=[])
    d["current_new_candidate_checkpoint"]=partial
    d["stage"]="new_closed_integrals";persist(a,d)
    for p in (2,4):
        partial["completed_integrals"].append(closed_integral(p,env,d));persist(a,d)
    j2,j4=partial["completed_integrals"]
    Y2=sqrt_up(j2["complete_integral_upper"]);Yquad_raw=sqrt_up(j4["complete_integral_upper"])
    Yquad=Yquad_raw
    # A separate complete bound from m<=rho, never a subtraction of upper bounds.
    qchoices=[dict(kind="sqrt_integral_m4",upper=rec(Yquad)),
        dict(kind="rho_times_sqrt_integral_m2",upper=rec(up(up(rho)*Y2)))]
    qchoice=whole_choice(qchoices,"upper");Yquad=up(qchoice["complete_selected_upper"])
    YL=up(min(up(rho),X)+rb(saved["selected_left_shift"]))
    ZR=up(min(up(rat(PARAMETERS["actual_outer_C_nonmean_radius"])),
        up(X/positive_lower(w["weight_R"]))))
    formal=up(rb(saved["D"])*Y2)
    nonlinear=up(13*rb(saved["Q"])*Yquad)
    body=up(formal+nonlinear)
    left=up(rb(saved["ELdelta"])*YL)
    right=up((rb(saved["ER"])+rb(saved["LD"])*rb(saved["ZB"])
        +rb(saved["Lm"])*rb(saved["Zm"]))*ZR)
    unknown=up(body+left+right)
    total=up(rb(saved["known_uniform"])+rb(saved["known_outer"])+unknown)
    row=dict(domain=domain,weight=k,physical_gamma_A0_upper=rec(gamma),
        complete_same_weight_envelope=env["audit"],complete_integral_records=[j2,j4],
        sqrt_integral_m2_upper=rec(Y2),sqrt_integral_m4_upper=rec(Yquad_raw),
        complete_quadratic_L2_candidates=copy.deepcopy(qchoice["complete_candidate_records"]),
        selected_quadratic_L2_candidate=qchoice["selected_complete_candidate"],
        complete_selected_quadratic_L2_upper=rec(Yquad),
        complete_selected_left_Y=rec(YL),right_C_nonmean_Z=rec(ZR),
        formal_body_error=rec(formal),complete_nonlinear_body_error=rec(nonlinear),
        complete_formal_and_nonlinear_body_error=rec(body),
        complete_left_defect_error=rec(left),complete_outer_feedback_error=rec(right),
        complete_unknown_error=rec(unknown),complete_affine_97_norm_upper=rec(total),
        full_physical_pair_and_Cmean_retained=True,same_true_gamma_trace_condition_retained=True,
        selected_known_shift_only_at_left=True,original_Hessian_Gram_not_added=True,
        four_power_readout_is_square_root_of_integral_not_L4_norm=True)
    if not finite(row):raise ValueError("the complete new whole-weight candidate is not finite")
    return row

def render_conclusion(d):
    lines=["# R133 actual whole-cap p2/p4 scalar envelope","",
        "Same physical cap pair, all signed modes and C mean, full ordinary dr. Old RW and SC3 work is read only.","",
        f"Complete: {d.get('complete')}; proved: {d.get('proved')}; actual return: {d.get('actual_returncode')}.",
        f"Actual gates: {sum(x.get('passed') is True for x in d.get('gates',[]))}/{len(d.get('gates',[]))}.",
        f"Completed new weight/domain rows: {d.get('new_complete_weight_domain_rows',0)}; p-integrals: {d.get('new_closed_integrals_evaluated',0)}.",""]
    if d.get("complete") is True:
        for row in d["complete_new_whole_posterior_conclusion"]:
            choice=row["whole_complete_choice"]
            lines.extend([f"## {row['domain']}","",
                f"Whole selected kind: {choice['complete_selected_record']['kind']}.",
                f"Complete affine97 upper: {canonical(choice['complete_selected_upper'])}.",""])
        lines.extend(["The known signed97 model and complete outer omission are copied once.",
            "The physical unknown remains W_star minus the original repaired centre.",
            "Body uses D sqrt(J2) + 13 Q sqrt(J4); the selected known 10d shift stays at the left.",
            "Each weighted row is completed before a whole-row comparison with the original SC3 posterior.",
            "No new trace, core, full incoming, finite Schur or global surface conclusion is claimed.",""])
    else:
        lines.extend(["The complete new envelope target has not been proved.",
            "Any saved new partial row and all completed old input identities remain in the original JSON.",
            f"Failure: {canonical(d.get('failure'))}.",""])
    return "\n".join(lines)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo-root",type=Path,required=True)
    ap.add_argument("--manifest",type=Path,required=True)
    ap.add_argument("--temporary-output-dir",type=Path,required=True)
    ap.add_argument("--process-receipt",type=Path,required=True)
    ap.add_argument("--small-summary",type=Path,required=True)
    ap.add_argument("--result-markdown",type=Path,required=True)
    a=ap.parse_args();ctx.prec=320;started=time.monotonic()
    d=dict(kind=KIND,complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        source_sha256=sha(__file__),input_manifest_sha256=sha(a.manifest),arithmetic_bits=320,
        mathematical_parameters=PARAMETERS,public_repository=PUBLIC,
        run_id=os.environ.get("GITHUB_RUN_ID",""),run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT",""),
        workflow_event_commit=os.environ.get("GITHUB_SHA",""),
        actual_scientific_checkout_commit=os.environ.get("SCIENTIFIC_CHECKOUT_COMMIT",""),
        stage="input_identity",original_successful_small_receipts_read=0,
        original_complete_objects_read_verbatim=0,saved_scalar_records_read=0,
        new_affine_substitutions_evaluated=0,new_crossing_logarithms_evaluated=0,
        new_closed_integral_exponentials_evaluated=0,new_closed_integrals_evaluated=0,
        new_complete_weight_domain_rows=0,new_complete_whole_posterior_choices=0,
        new_completed_weight_domain_rows=[],complete_new_whole_posterior_conclusion=[],
        old_RW_or_SC_scientific_evaluations=0,old_numerical_enclosures_recomputed=0,
        old_Gram_or_Hessian_or_known_model_recomputed=0,old_scientific_producer_imports=0,
        old_scientific_producer_calls=0,old_binary_or_archive_inputs_restored=0,
        original_input_bytes_modified=0,complete_whole_cap_envelope_consumer_paid=False,
        new_low_trace_gate_claimed=False,new_core_selfmap_claimed=False,
        full_physical_incoming_inverse_claimed=False,finite_Schur_inverse_claimed=False,
        full_return_R0_claimed=False,actual_nonlinear_background_claimed=False,
        temporary_native_is_not_published=True,reproducible_outputs_published_to_repository=False,
        reproducible_outputs_uploaded_to_Releases=False,new_reproducible_data_artifact_uploaded=False)
    def gate(label,ok):
        ok=bool(ok);d["gates"].append(dict(gate=label,passed=ok))
        if not ok:raise ValueError(label)
    try:
        paths=checked_inputs(a,d,gate)
        rw,sc=accepted_records(paths,d,gate)
        saved,weights=scalar_copies(rw,sc,d,gate)
        d["stage"]="complete_original_records_copied";persist(a,d)
        for domain,gamma_text in (("full_original_cap_product",PARAMETERS["full_inner_gamma_radius"]),
                ("tail_inner_curvature_subdomain",PARAMETERS["tail_inner_gamma_radius"])):
            gamma=rat(gamma_text)
            for k in PARAMETERS["weight_fractions"]:
                row=complete_weight_candidate(domain,gamma,k,weights[k],saved,a,d)
                d["new_completed_weight_domain_rows"].append(row)
                d["new_complete_weight_domain_rows"]+=1
                d.pop("current_new_candidate_checkpoint",None)
                d["stage"]="complete_new_weight_row";persist(a,d)
        gate("all twelve same-object weight-domain rows and twenty-four closed integrals are complete",
            d["new_affine_substitutions_evaluated"]==d["new_complete_weight_domain_rows"]==12
            and len(d["new_completed_weight_domain_rows"])==12
            and d["new_closed_integrals_evaluated"]==24
            and all([r["power"] for r in row["complete_integral_records"]]==[2,4]
                for row in d["new_completed_weight_domain_rows"]))
        gate("every new integral covers the full physical interval without midpoint branch selection",
            all(r["ordinary_radial_measure"]=="dr" and r["full_interval_included"] is True
                and r["no_original_weight_profile_or_integral_recomputed"] is True
                for row in d["new_completed_weight_domain_rows"] for r in row["complete_integral_records"])
            and all(row["four_power_readout_is_square_root_of_integral_not_L4_norm"] is True
                and row["full_physical_pair_and_Cmean_retained"] is True
                for row in d["new_completed_weight_domain_rows"]))
        for oldrow in sc["complete_posterior_rows"]:
            domain=oldrow["domain"]
            candidates=[dict(kind="original_SC3_complete_posterior_read_verbatim",
                complete_affine_97_norm_upper=copy.deepcopy(oldrow["complete_affine_97_norm_upper"]))]
            candidates.extend(dict(kind="new_complete_weight_"+row["weight"],
                complete_affine_97_norm_upper=copy.deepcopy(row["complete_affine_97_norm_upper"]))
                for row in d["new_completed_weight_domain_rows"] if row["domain"]==domain)
            choice=whole_choice(candidates,"complete_affine_97_norm_upper")
            d["complete_new_whole_posterior_conclusion"].append(dict(domain=domain,
                physical_gamma_A0_upper=copy.deepcopy(oldrow["physical_gamma_A0_upper"]),
                original_SC3_complete_row_read_verbatim=copy.deepcopy(oldrow),
                whole_complete_choice=choice,
                same_true_input_gamma_must_equal_selected_physical_C_trace=True))
            d["new_complete_whole_posterior_choices"]+=1
            persist(a,d)
        gate("two complete domain choices compare seven whole affine97 candidates each",
            d["new_complete_whole_posterior_choices"]==2
            and len(d["complete_new_whole_posterior_conclusion"])==2
            and all(len(row["whole_complete_choice"]["complete_candidate_records"])==7
                and row["whole_complete_choice"]["same_complete_object_and_domain"] is True
                and row["whole_complete_choice"]["no_entrywise_mixing"] is True
                for row in d["complete_new_whole_posterior_conclusion"]))
        gate("the unchanged known model outer mean and selected-left terms enter every completed new row once",
            all(row["selected_known_shift_only_at_left"] is True
                and row["original_Hessian_Gram_not_added"] is True
                and row["same_true_gamma_trace_condition_retained"] is True
                for row in d["new_completed_weight_domain_rows"])
            and d["complete_original_SC_signed97_model_sha256"]==payload_sha(sc["complete_signed97_parameter_model"]))
        gate("all old scalar weight and complete object payloads remain verbatim after new arithmetic",
            payload_sha(d["complete_saved_scalar_records_read_verbatim"])==d["complete_saved_scalar_payload_sha256"]
            and payload_sha(d["complete_saved_weight_records_read_verbatim"])==d["complete_saved_weight_payload_sha256"]
            and payload_sha(d["complete_old_objects_read_verbatim"])==d["complete_old_object_payload_sha256"])
        d["scope"]=dict(same_actual_physical_y_not_moving_Q=True,
            complete_physical_Cmean_and_original_reflection_retained=True,
            complete_cap_ordinary_dr_and_normalized_theta=True,
            no_local_RW_body_integral_extended_to_full_cap=True,
            same_original_rho_pointwise_rational_domain=True,
            same_selected_gamma_and_outer_height_domain=True,
            known_selected_shift_only_at_left=True,all_known_errors_already_embedded_kept_once=True,
            no_global_recentring_of_unknown_y=True,no_Hessian_Gram_added=True,
            original_exact_zero_trial_value_jumps_retained=True,
            quadratic_readout_is_sqrt_integral_m4_not_L4_norm=True,
            every_weight_completed_before_whole_posterior_minimum=True,
            all_original_low_trace_waist_core_high_and_finite_inputs_independent=True)
        gate("the complete physical scope retains every independent mean height waist and core input",
            all(d["scope"].values())
            and all(d[k] is False for k in ("new_low_trace_gate_claimed","new_core_selfmap_claimed",
                "full_physical_incoming_inverse_claimed","finite_Schur_inverse_claimed",
                "full_return_R0_claimed","actual_nonlinear_background_claimed")))
        gate("all successful old mathematics and original input bytes remain untouched",
            all(d[k]==0 for k in ("old_RW_or_SC_scientific_evaluations",
                "old_numerical_enclosures_recomputed","old_Gram_or_Hessian_or_known_model_recomputed",
                "old_scientific_producer_imports","old_scientific_producer_calls",
                "old_binary_or_archive_inputs_restored","original_input_bytes_modified")))
        gate("all complete retained and new directed ball records are finite",
            finite(d) and d["original_successful_small_receipts_read"]==4
            and d["saved_scalar_records_read"]==41 and d["original_complete_objects_read_verbatim"]==6)
        # Save complete mathematical output before the small-publication formatting guard.
        d["mathematical_target_complete_before_format_guard"]=True
        d["stage"]="complete_new_envelope_mathematics_saved";persist(a,d)
        gate("all complete mathematics is saved before any small-publication formatting guard",
            canonical(read(a.process_receipt))==canonical(d)
            and canonical(read(a.small_summary))==canonical(d))
        if len(d["gates"])!=22:raise ValueError("the exact22-gate envelope contract changed")
        d["complete"]=d["proved"]=d["complete_whole_cap_envelope_consumer_paid"]=True
        d["actual_returncode"]=0;d["stage"]="complete_whole_cap_weight_envelope_target"
    except Exception as error:
        d["failure"]=dict(type=type(error).__name__,message=str(error))
        d["complete"]=d["proved"]=d["complete_whole_cap_envelope_consumer_paid"]=False
        d["actual_returncode"]=1
    finally:
        d["actual_mathematical_wall_seconds"]=time.monotonic()-started
        a.temporary_output_dir.mkdir(parents=True,exist_ok=True)
        native=a.temporary_output_dir/"temporary-whole-cap-weight-envelope.json.gz"
        published=publication_document(d)
        save(native,published,True)
        published["temporary_native_sha256"]=sha(native);published["temporary_native_bytes"]=native.stat().st_size
        save(a.process_receipt,published);save(a.small_summary,published)
        print("COMPLETE_WHOLE_CAP_ENVELOPE_SCIENCE_BEGIN",flush=True)
        print(canonical(published),flush=True)
        print("COMPLETE_WHOLE_CAP_ENVELOPE_SCIENCE_END",flush=True)
        try:
            if len((canonical(published)+"\n").encode())>75000:
                raise ValueError("complete mathematical science saved but publication formatting exceeds75000 bytes")
            result=render_conclusion(d)
            if len(result.encode())>10000:raise ValueError("the complete small markdown exceeds10000 bytes")
            a.result_markdown.parent.mkdir(parents=True,exist_ok=True);a.result_markdown.write_text(result)
        except Exception as error:
            published["formatting_failure"]=dict(type=type(error).__name__,message=str(error))
            published["actual_scientific_returncode"]=d["actual_returncode"]
            save(a.process_receipt,published);save(a.small_summary,published)
            a.result_markdown.parent.mkdir(parents=True,exist_ok=True)
            a.result_markdown.write_text("# Complete science is retained in the original small JSON.\n\nFormatting failed; do not repeat the scientific evaluation.\n")
            raise
    raise SystemExit(d["actual_returncode"])

if __name__=="__main__":main()
