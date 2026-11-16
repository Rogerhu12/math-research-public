"""Continue only the 30 unpaid records after public run 43827705714/1.
The complete old 23 graphs and all 39 partial records are immutable inputs.
No old scientific producer or completed target is imported or evaluated.
"""
from __future__ import annotations
import argparse,ast,copy,hashlib,importlib.metadata,importlib.util
import json,os,re,sys,time
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby"

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def write_atomic(path,document):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=compact(document);tmp=path.with_name(path.name+".partial")
    tmp.write_bytes(raw);tmp.replace(path)
    return raw

def emit_file(relative,raw):
    print("BEGIN_COMPLETE_WEJ_FILE "+relative,flush=True)
    sys.stdout.buffer.write(raw);sys.stdout.buffer.flush()
    if not raw.endswith(b"\n"):print("",flush=True)
    print("END_COMPLETE_WEJ_FILE "+relative,flush=True)

def load_remaining_math(path,expected):
    raw=Path(path).read_bytes()
    require(digest(raw)==expected,"remaining math source changed before import")
    spec=importlib.util.spec_from_file_location("new_WEJ_remaining_math",path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def checked(p,size,digest):
    p=Path(p)
    if not p.is_file() or p.stat().st_size!=size or sha(p)!=digest:
        raise ValueError("one complete pinned input differs: "+str(p))

def relpath(p):
    p=Path(p)
    if p.is_absolute() or ".." in p.parts or not str(p).startswith(str(TOPIC)+"/"):
        raise ValueError("one input left the authorized topic")
    return p

def compact(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,
                       allow_nan=False)+"\n").encode()



def require(test,message):
    if not test:raise ValueError(message)


def reject_constant(value):
    raise ValueError("nonfinite JSON token is not a complete saved scientific record: "+value)


def exact_json(raw):
    return json.loads(raw.decode("utf-8"),parse_constant=reject_constant)


def hex_string(value,size):
    return (isinstance(value,str) and len(value)==size
        and all(c in "0123456789abcdef" for c in value))


def finite_record(value):
    return (isinstance(value,dict) and set(value)=={"ball"}
        and isinstance(value["ball"],str) and 0<len(value["ball"])<=1024
        and any(c.isdigit() for c in value["ball"])
        and not any(x in value["ball"].lower() for x in ("nan","inf"))
        and re.fullmatch(r"[\[\]0-9eE+\-./ \t]+",value["ball"]) is not None)


def finite_number(value):
    return type(value) in (int,float) and value==value and abs(value)<float("inf")


def full_shape(value,expected):
    # This is a pure JSON check. No ball or old scientific producer is evaluated.
    if isinstance(expected,dict) and set(expected)=={"ball"}:
        token=expected["ball"]
        if isinstance(token,str) and token.startswith("__NEW_"):
            return finite_record(value)
    if isinstance(expected,str):
        if expected in ("#U","#L","__NEW_FINITE_NONNEGATIVE_RECORD__"):
            return finite_record(value)
        if expected.startswith("__TYPE_") and expected.endswith("__"):
            kind=expected[7:-2]
            if kind.startswith("OPTIONAL_"):
                if value is None:return True
                kind=kind[9:]
            kinds={"STRING":isinstance(value,str),"INTEGER":type(value) is int,
                   "NUMBER":finite_number(value),"BOOLEAN":type(value) is bool,
                   "OBJECT":isinstance(value,dict),"LIST":isinstance(value,list)}
            return kinds.get(kind,False)
    if isinstance(expected,dict):
        return (isinstance(value,dict) and set(value)==set(expected)
            and all(full_shape(value[k],v) for k,v in expected.items()))
    if isinstance(expected,list):
        return (isinstance(value,list) and len(value)==len(expected)
            and all(full_shape(x,y) for x,y in zip(value,expected)))
    if type(expected) in (int,float):
        return type(value) in (int,float) and value==expected
    return type(value) is type(expected) and value==expected


def json_equal(value,expected):
    if isinstance(expected,dict):
        return (isinstance(value,dict) and set(value)==set(expected)
                and all(json_equal(value[k],v) for k,v in expected.items()))
    if isinstance(expected,list):
        return (isinstance(value,list) and len(value)==len(expected)
                and all(json_equal(a,b) for a,b in zip(value,expected)))
    if type(expected) in (int,float):
        return type(value) in (int,float) and value==expected
    return type(value) is type(expected) and value==expected


def ball_count(value):
    if isinstance(value,dict):
        if set(value)=={"ball"} and isinstance(value["ball"],str):return 1
        return sum(ball_count(v) for v in value.values())
    if isinstance(value,list):return sum(ball_count(v) for v in value)
    return 0


def at(value,path):
    for key in path:value=value[key]
    return value


def reconstruct_partial_envelope(filename,descriptor,physical_files):
    require(isinstance(descriptor,dict) and set(descriptor)=={
        "kind","node_name","complete","original_envelope_fields",
        "original_envelope_identity","complete_field_files","reconstruction",
        "all_original_fields_and_record_order_retained","automatic_retry_authorized"},
        "partial descriptor schema differs")
    require(descriptor["kind"]==PARTIAL_DESCRIPTOR_KIND and descriptor["complete"] is False
            and descriptor["all_original_fields_and_record_order_retained"] is True
            and descriptor["automatic_retry_authorized"] is False
            and descriptor["reconstruction"]==
              "restore all three original fields, then sorted compact UTF8 JSON plus LF",
            "partial descriptor changed its preservation contract")
    node=descriptor["node_name"]
    require(filename=="graphs/"+node+".json","partial descriptor changed its scientific node")
    identity=descriptor["original_envelope_identity"]
    require(isinstance(identity,dict) and set(identity)=={"file","bytes","sha256"}
            and identity["file"]==filename and type(identity["bytes"]) is int
            and identity["bytes"]>0 and hex_string(identity["sha256"],64),
            "complete original partial identity missing")
    rest=descriptor["original_envelope_fields"]
    require(isinstance(rest,dict) and set(rest)==PARTIAL_NODE_FIELDS-set(PARTIAL_FIELD_FILES),
            "partial descriptor dropped an original envelope field")
    refs=descriptor["complete_field_files"]
    require(isinstance(refs,dict) and set(refs)==set(PARTIAL_FIELD_FILES),
            "partial field inventory is incomplete")
    envelope=dict(rest)
    for field,path in PARTIAL_FIELD_FILES.items():
        ref=refs[field]
        require(isinstance(ref,dict) and set(ref)=={"file","bytes","sha256"}
                and ref["file"]==path and type(ref["bytes"]) is int and ref["bytes"]>0
                and hex_string(ref["sha256"],64),"partial field reference differs")
        require(path in physical_files,"complete partial projection file missing")
        raw=physical_files[path]
        require(len(raw)==ref["bytes"] and hashlib.sha256(raw).hexdigest()==ref["sha256"],
                "complete partial projection byte identity differs")
        part=exact_json(raw)
        require(raw==compact(part) and isinstance(part,dict) and set(part)=={
            "kind","node_name","field","complete_field_value"}
            and part["kind"]==PARTIAL_FIELD_KIND and part["node_name"]==node
            and part["field"]==field,"complete partial projection schema differs")
        envelope[field]=part["complete_field_value"]
    require(envelope.get("kind")==ENVELOPE_KIND and envelope.get("node_name")==node
            and envelope.get("complete") is False and envelope.get("automatic_retry_authorized") is False,
            "reconstructed partial is a different scientific target")
    original=compact(envelope)
    require(len(original)==identity["bytes"]
            and hashlib.sha256(original).hexdigest()==identity["sha256"],
            "lossless partial reconstruction does not match its complete original SHA")
    return original


"""Pure JSON retained-prefix reconstruction, no entry and no scientific import.
Copy with the audited worker metadata helpers; all referenced constants follow.
"""
MANIFEST_KIND="complete_WEJ_remaining_current_input_manifest_v1"
INDEX_KIND="complete_remaining_WEJ_posterior_v1"
ENVELOPE_KIND="WEJ_complete_atomic_node_v1"
SCIENTIFIC_ROLES=("remaining_pipeline","remaining_math")
INDEX_FIELDS=(
 "kind","complete","proved","actual_returncode","failure","public_repository",
 "run_id","run_attempt","workflow_event_commit","actual_scientific_checkout_commit",
 "source_sha256","scientific_module_sha256","input_manifest_sha256",
 "parameters","parameters_sha256","mathematical_input_sha256","runtime",
 "arithmetic_bits","gates","node_receipts","original_input_files",
 "locked_attempted_nodes","active_node","stage","actual_progress",
 "actual_mathematical_wall_seconds","old_scientific_calls","old_binary_parts_restored",
 "new_reproducible_arrays_persisted","new_artifacts","new_Releases","retained_scope")
BINDING_FIELDS={"problem_id","parameters_sha256","mathematical_input_sha256",
                "scientific_module_sha256","direct_dependency_receipts"}
COMPLETE_NODE_FIELDS={"kind","node_name","binding","complete",
    "printed_record_event_count","all_printed_records_in_complete_conclusion",
    "conclusion","failure","automatic_retry_authorized"}
PARTIAL_NODE_FIELDS={"kind","node_name","binding","complete","printed_record_events",
    "conclusion","explicit_math_prefix","failure","automatic_retry_authorized"}
PARTIAL_DESCRIPTOR_KIND="WEJ_lossless_split_partial_envelope_v1"
PARTIAL_FIELD_KIND="WEJ_complete_partial_field_v1"
PARTIAL_FIELD_FILES={
 "conclusion":"partial-node-conclusion.json",
 "printed_record_events":"partial-node-record-events.json",
 "explicit_math_prefix":"partial-node-explicit-prefix.json"}
ORIGINAL_FILENAMES=("retained-prefix-admission.json",)
REMAINING_NODE_NAMES=(
 "complete_free_waist_Airy_and_Schur_map",
 "complete_four_waist_endpoint_contributions",
 "complete_same_physical_whole_and_reduced_error")
REMAINING_COMPLETE_RECORD_COUNTS=(52,8,15)
REMAINING_NEW_RECORD_COUNTS=(13,8,9)
RETAINED_RECORD_COUNTS={
 "complete_nodes":23,"complete_saved_slots":1609,"complete_new_records":1600,
 "complete_original_copy_slots":9,"partial_new_records":39,
 "allowed_remaining_new_records":30}

def complete_expected_original_documents(root,manifest,input_receipts):
    """Reconstruct retained JSON only; no original producer or ball is evaluated."""
    files={p["role"]:p for p in manifest["files"]};docs={};raws={};by_path={}
    keys=("role","path","bytes","sha256","git_blob_sha")
    receipts=[{k:r[k] for k in keys} for r in input_receipts]
    require([r["role"] for r in receipts]==[r["role"] for r in manifest["files"]],
            "complete current-input receipt order differs")
    byrole={r["role"]:r for r in receipts}
    for role in set(manifest["mathematical_input_roles"])|set(SCIENTIFIC_ROLES):
        require(byrole.get(role)=={k:files[role][k] for k in keys},
                "retained or remaining scientific input identity differs: "+role)
    for r in receipts:
        require(set(r)==set(keys) and isinstance(r["role"],str)
                and type(r["bytes"]) is int and 0<r["bytes"]<100000
                and hex_string(r["sha256"],64) and hex_string(r["git_blob_sha"],40),
                "invalid complete retained current receipt")
        relpath(r["path"])
    for role,spec in files.items():
        if not spec["read_as_json"]:continue
        path=root/relpath(spec["path"]);checked(path,spec["bytes"],spec["sha256"])
        raws[role]=path.read_bytes();docs[role]=exact_json(raws[role])
        by_path[spec["path"]]=role
    role=manifest["_resolved_output_contract"]["retained_prefix_contract_role"]
    require(role=="recovery_contract" and role in manifest["mathematical_input_roles"]
            and docs[role].get("kind")=="exact_preserved_WEJ_prefix_continuation_contract_v1",
            "one complete frozen continuation contract required")
    contract=docs[role];old=docs["prior_manifest"]
    index=docs["prior_index"];execution=docs["prior_execution"]
    for role,key in (("prior_index","original_index"),("prior_execution","original_execution"),
                     ("prior_manifest","original_manifest")):
        require({k:files[role][k] for k in keys[1:]}==contract[key],
                "the original failed execution identity differs")
    require(set(index)==set(INDEX_FIELDS)
            and index["kind"]=="complete_global_genuine_waist_error_posterior_v1"
            and index["complete"] is False and index["proved"] is False
            and type(index["actual_returncode"]) is int and index["actual_returncode"]==1
            and index["stage"]=="preserved_failure"
            and index["active_node"]==REMAINING_NODE_NAMES[0],
            "the complete original index lost its exact partial status")
    pairs=(("run_id","original_run_id"),("run_attempt","original_run_attempt"),
      ("workflow_event_commit","original_workflow_event_commit"),
      ("actual_scientific_checkout_commit","actual_scientific_checkout_commit"),
      ("failure","original_failure"),("gates","complete_original_gate_array"),
      ("locked_attempted_nodes","complete_original_attempted_node_locks"),
      ("node_receipts","complete_original_node_receipts"),
      ("parameters","complete_original_parameters"),
      ("mathematical_input_sha256","complete_original_mathematical_input_sha256"),
      ("scientific_module_sha256","complete_original_scientific_module_sha256"),
      ("retained_scope","scope"))
    require(all(json_equal(index[k],contract[v]) for k,v in pairs),
            "an original complete status, gate, binding, parameter or scope changed")
    require(len(index["gates"])==27 and all(g["passed"] is True for g in index["gates"])
            and len(index["node_receipts"])==23 and len(index["locked_attempted_nodes"])==24
            and index["parameters_sha256"]==hashlib.sha256(compact(index["parameters"])).hexdigest()
            and json_equal(index["parameters"],old["parameters"])
            and index["input_manifest_sha256"]==files["prior_manifest"]["sha256"]
            and index["source_sha256"]==old["source_sha256"]
            and index["runtime"]==manifest["scientific_runtime"] and index["arithmetic_bits"]==320,
            "incomplete original identity and parameter chain")
    oldreceipts=[{**{k:s[k] for k in keys},"origin":"exact_current_small_text"} for s in old["files"]]
    require(execution["actual_original_Git_input_receipts"]==oldreceipts
            and execution["actual_verified_Git_input_count"]==len(oldreceipts)
            and execution["actual_verified_Git_input_receipts_sha256"]==
                hashlib.sha256(compact(oldreceipts)).hexdigest(),
            "the full original Git-input receipt chain differs")
    require(execution["complete"] is False and execution["actual_returncode"]==1
            and type(execution["actual_returncode"]) is int
            and execution["actual_new_scientific_processes"]==1
            and execution["scientific_child_launch_attempted"] is True
            and execution["complete_original_input_receipt_available"] is True
            and execution["complete_mathematical_receipt_available"] is False
            and execution["automatic_scientific_retry_authorized"] is False,
            "original failure qualifications were changed")
    for a,b in (("run_id","run_id"),("run_attempt","run_attempt"),
        ("workflow_commit","workflow_event_commit"),
        ("actual_scientific_checkout_commit","actual_scientific_checkout_commit"),
        ("source_sha256","source_sha256"),("input_manifest_sha256","input_manifest_sha256"),
        ("actual_scientific_runtime","runtime"),("parameters","parameters"),
        ("mathematical_input_sha256","mathematical_input_sha256"),
        ("scientific_module_sha256","scientific_module_sha256"),("actual_failure","failure"),
        ("locked_attempted_nodes_read_verbatim","locked_attempted_nodes")):
        require(json_equal(execution[a],index[b]),"original execution/index mismatch: "+a)
    oldraw={}
    for ref in contract["all_original_published_scientific_file_receipts"]:
        role=by_path[ref["path"]];raw=raws[role]
        require(len(raw)==ref["bytes"] and hashlib.sha256(raw).hexdigest()==ref["sha256"],
                "one whole original scientific file differs")
        oldraw[ref["file"]]=raw
    refs=[{"file":n,"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest()} for n,raw in oldraw.items()]
    require(execution["scientific_files"]==refs
            and execution["scientific_index"]==refs[0]
            and execution["complete_original_input_files"]==index["original_input_files"],
            "the original execution does not bind every published file")
    old_byrole={r["role"]:{k:r[k] for k in keys} for r in oldreceipts}
    core=docs[by_path[next(s["path"] for s in old["files"]
                         if s["role"]=="posterior_admission_contract")]]
    require(core["kind"]=="complete_WEJ_original_actual_admission_contract_v1"
            and [s["role"] for s in core["original_actual_inputs"]]==old["old_actual_input_roles"]
            and len(core["original_actual_inputs"])==12
            and sum(s["gate_count"] for s in core["original_actual_inputs"])==212
            and sum(len(s["exact_checks"]) for s in core["original_actual_inputs"])==280
            and len(core["consumed_original_records"])==19
            and len(core["complete_old_conclusions"])==15,"prior admission counts differ")
    bindings={}
    for spec in core["original_actual_inputs"]:
        role=spec["role"];outer=docs[role];science=at(outer,spec["scientific_root"])
        require(byrole[role]==old_byrole[role],"original complete file receipt differs")
        require(isinstance(outer,dict) and sorted(outer)==spec["outer_keys"]
                and isinstance(science,dict) and sorted(science)==spec["scientific_keys"],
                "prior full schema mismatch: "+role)
        fields=[]
        for check in spec["exact_checks"]:
            value=at(outer,check["path"])
            require(json_equal(value,check["value"]),"prior identity or domain mismatch: "+role)
            fields.append({"path":check["path"],"value":value})
        gates=at(outer,spec["gates_path"]) if spec["gates_path"] is not None else []
        require(len(gates)==spec["gate_count"]
                and (spec["gates_path"] is None or
                     (json_equal(gates,spec["complete_original_gates"])
                      and all(g.get("passed") is True for g in gates))),
                "prior gate mismatch: "+role)
        bindings[role]={"original_file":old_byrole[role],"scientific_root":spec["scientific_root"],
          "complete_original_gates":gates,"complete_exact_identity_and_domain_fields":fields,
          "outer_schema_retained":True,"scientific_schema_retained":True,
          "original_complete_file_remains_at_immutable_public_identity":True}
    originals={}
    for spec in core["consumed_original_records"]:
        value=at(docs[spec["role"]],spec["path"])
        require(json_equal(value,spec["original_value"])
                and (value if isinstance(value,str) else value["ball"])==spec["ball_string"],
                "prior complete record changed")
        originals[spec["name"]]=value
    conclusions={spec["name"]:{"role":spec["role"],"path":spec["path"],
        "complete_value":at(docs[spec["role"]],spec["path"])}
        for spec in core["complete_old_conclusions"]}
    expected_admission={
      "kind":"complete_WEJ_original_actual_input_admission_v1","complete":True,
      "original_file_count":12,"complete_original_actual_bindings":bindings,
      "complete_current_file_receipts":[old_byrole[r["role"]] for r in oldreceipts],
      "complete_scientific_parameter_contract":old["parameters"],
      "read_only_scope":"complete immutable current files; zero historical restoration and zero old producer calls",
      "same_selected_real_member_only":True,"WGS_geometry_and_amplitudes_are_sup_not_A0":True,
      "strict_d_A0_has_its_independent_original_Banach_product_and_primitive_proof":True,
      "all_old_successes_and_original_failure_qualifications_retained":True}
    expected_consumed={
      "kind":"complete_WEJ_consumed_original_conclusions_v1","complete":True,
      "complete_original_consumed_record_objects":originals,"complete_old_conclusions":conclusions,
      "complete_WGS_original_files":{r:old_byrole[r] for r in ("WGS_main","WGS_original_inputs")},
      "WGS_full_graphs_read_from_their_complete_immutable_original_files":True,
      "WGS_437_slots_and_all_66_plus_40_original_records_not_recomputed":True,
      "no_partial_or_truncated_source_conclusion_substituted":True,
      "all_false_scope_flags_in_selected_complete_conclusions_retained":True}
    require(json_equal(exact_json(oldraw["original-inputs-admission.json"]),expected_admission)
            and json_equal(exact_json(oldraw["original-inputs-consumed-conclusions.json"]),
                           expected_consumed),"full original admission or consumed document differs")
    node_refs={};slots=0;events=0
    for spec,ref in zip(old["ordered_node_specs"][:23],index["node_receipts"]):
        name=spec["node_name"];filename=spec["relative_path"];payload=exact_json(oldraw[filename])
        receipt={"file":filename,"bytes":len(oldraw[filename]),
                 "sha256":hashlib.sha256(oldraw[filename]).hexdigest()}
        binding={"problem_id":old["problem_id"]+"/"+name,
            "parameters_sha256":index["parameters_sha256"],
            "mathematical_input_sha256":index["mathematical_input_sha256"],
            "scientific_module_sha256":index["scientific_module_sha256"],
            "direct_dependency_receipts":{n:node_refs[n] for n in spec["dependency_names"]}}
        require(ref=={"node_name":name,**receipt} and set(payload)==COMPLETE_NODE_FIELDS
                and payload["kind"]==ENVELOPE_KIND and payload["node_name"]==name
                and payload["binding"]==binding and payload["complete"] is True
                and payload["failure"] is None and payload["automatic_retry_authorized"] is False
                and payload["all_printed_records_in_complete_conclusion"] is True
                and type(payload["printed_record_event_count"]) is int
                and payload["printed_record_event_count"]==
                    {"mean_gamma_bridge":8,"same_angular_J_local":19,"negative_reception":32}.get(
                        name,spec["record_count"]),
                "a completed original node or original dependency binding changed")
        schema=docs[by_path[next(s["path"] for s in old["files"] if s["role"]==spec["schema_role"])]]
        shape=schema["complete_conclusion_shapes"][spec["conclusion_shape_key"]]
        require(full_shape(payload["conclusion"],shape)
                and ball_count(payload["conclusion"])==spec["record_count"],
                "one complete original scientific graph lost a field or record")
        node_refs[name]=receipt;slots+=spec["record_count"];events+=payload["printed_record_event_count"]
    require(slots==1609 and events==1600
            and index["actual_progress"]==[{"node_name":r["node_name"],"complete_file_saved":True}
                                           for r in index["node_receipts"]],
            "original complete node or event count differs")
    sv=execution["scientific_validation"]
    require(sv=={"complete":False,"original_inputs_valid":True,"index_valid":True,
            "complete_node_receipts":node_refs,"partial_nodes":[REMAINING_NODE_NAMES[0]],"errors":[]},
            "the complete original validation outcome changed")
    descriptor=docs["prior_partial_descriptor"]
    partial_raw=reconstruct_partial_envelope("graphs/"+REMAINING_NODE_NAMES[0]+".json",
                                              descriptor,oldraw)
    partial=exact_json(partial_raw)
    require(len(partial_raw)==13563 and hashlib.sha256(partial_raw).hexdigest()==
                contract["exact_preserved_prefix"]["original_partial_sha256"],
            "the exact failed prefix was not losslessly reconstructed")
    spec=old["ordered_node_specs"][23]
    require(partial["binding"]=={"problem_id":old["problem_id"]+"/"+spec["node_name"],
        "parameters_sha256":index["parameters_sha256"],
        "mathematical_input_sha256":index["mathematical_input_sha256"],
        "scientific_module_sha256":index["scientific_module_sha256"],
        "direct_dependency_receipts":{n:node_refs[n] for n in spec["dependency_names"]}},
        "the original partial dependency binding changed")
    prefix=partial["explicit_math_prefix"]["complete_scientific_document_prefix"]
    saved_events=partial["printed_record_events"]
    require(ball_count(prefix)==39 and len(saved_events)==39 and prefix["complete"] is False
            and partial["conclusion"] is None,
            "the whole 39-record prefix qualification differs")
    strings=[]
    def collect(value):
        if finite_record(value):strings.append(value["ball"])
        elif isinstance(value,dict):
            for item in value.values():collect(item)
        elif isinstance(value,list):
            for item in value:collect(item)
    collect(prefix)
    require(all(set(e)=={"direction","record"} and e["direction"] in ("upper","lower")
                and finite_record(e["record"]) for e in saved_events)
            and sorted(strings)==sorted(e["record"]["ball"] for e in saved_events),
            "one complete saved partial record or direction was lost")
    for path in contract["all_39_preserved_record_paths"]:
        value=prefix
        for key in path:
            if isinstance(value,list):
                require(isinstance(key,str) and key.isdigit() and int(key)<len(value),
                        "invalid retained array record index")
                key=int(key)
            value=value[key]
        require(finite_record(value),"one original saved record path disappeared")
    phase=docs["WGS_main"]["complete_strict_geometry_conclusion"]["complete_jets"]["phase_derivatives"]
    cert=docs["WGS_main"]["complete_derivative_request_certificate"]
    require(phase["shape"]==[15,3] and phase["value_omitted_for_lift"] is True
            and phase["group_upper"][0] is None and cert["fixed_degree_groups"][2]==[2,2],
            "the paid phase derivative qualification changed")
    phase_records={"phase_second_normalized_upper":phase["group_upper"][2],
        "phase_first_lower":docs["WGS_main"]["complete_higher_flow_and_cut_conclusion"]["strict_phase_lower"],
        "derivative_multi_index":[0,2],"ordinary_derivative_factorial":2,"lift_value_omitted":True}
    require(finite_record(phase_records["phase_second_normalized_upper"])
            and finite_record(phase_records["phase_first_lower"]),"missing complete paid derivative records")
    return ({"kind":"complete_WEJ_retained_prefix_input_admission_v1","complete":True,
        "complete_current_file_receipts":receipts,"complete_original_failed_index":index,
        "complete_original_failed_execution_file":byrole["prior_execution"],
        "complete_original_partial_envelope":partial,
        "complete_phase_derivative_record_qualification":phase_records,
        "preserved_record_counts":RETAINED_RECORD_COUNTS,
        "complete_scientific_parameter_contract":manifest["parameters"],
        "retained_scope":manifest["retained_scope"],
        "all_completed_records_are_read_verbatim":True,
        "all_old_successes_and_failed_prefix_qualifications_retained":True,
        "no_completed_target_reevaluated":True},)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo",type=Path,required=True)
    ap.add_argument("--manifest",type=Path,required=True)
    ap.add_argument("--manifest-sha",required=True)
    ap.add_argument("--bits",type=int,required=True)
    ap.add_argument("--out-dir",type=Path,required=True)
    args=ap.parse_args();started=time.monotonic()
    raw=args.manifest.read_bytes()
    require(digest(raw)==args.manifest_sha,"immutable remaining manifest changed")
    m=exact_json(raw)
    require(m["kind"]==MANIFEST_KIND and m["public_repository"]==PUBLIC,
            "wrong complete remaining-only manifest")
    require(os.environ.get("GITHUB_ACTIONS")=="true" and
            os.environ.get("GITHUB_REPOSITORY")==PUBLIC,"public own Actions only")
    require(args.bits==320 and m["parameters"]["arithmetic_bits"]==320,
            "different directed precision")
    runtime={"Python":sys.version.split()[0],
             "python_flint":importlib.metadata.version("python-flint")}
    require(runtime==m["scientific_runtime"],"different scientific runtime")
    require(m["historical_inputs"]==[] and m["legacy_artifact_inputs"]==[]
            and m["old_successful_scientific_calls_allowed"]==0,
            "remaining-only input or no-repetition policy changed")
    files={p["role"]:p for p in m["files"]}
    require(len(files)==len(m["files"])==m["expected_input_count"],
            "duplicate or incomplete input roles")
    root=args.repo.resolve();out=args.out_dir.resolve()
    out.mkdir(parents=True,exist_ok=True)
    require(all(p.is_file() and p.name in ("worker-process.json","new-scientific-child.stdout.log")
                for p in out.iterdir()),"no prior scientific output may be overwritten")
    code={};docs={};receipts=[];ast_roles=[]
    for role,spec in files.items():
        path=relpath(spec["path"]);rr=(root/path).read_bytes()
        require(0<len(rr)<100000 and len(rr)==spec["bytes"]
                and digest(rr)==spec["sha256"],"immutable current input differs: "+role)
        require(hashlib.sha1(b"blob "+str(len(rr)).encode()+b"\0"+rr).hexdigest()
                ==spec["git_blob_sha"],"immutable current Git blob differs: "+role)
        text=rr.decode("utf-8")
        if str(path).endswith(".py"):
            ast.parse(text,filename=str(path));ast_roles.append(role)
        code[role]=root/path
        docs[role]=exact_json(rr) if spec["read_as_json"] else text
        receipts.append({k:spec[k] for k in ("role","path","bytes","sha256","git_blob_sha")})
    require(set(ast_roles)==set(m["immutable_AST_roles"])
            and len(ast_roles)==m["expected_immutable_AST_files"],
            "incomplete remaining immutable AST closure")
    require(sha(__file__)==files["remaining_pipeline"]["sha256"]
            and m["source_sha256"]==files["remaining_pipeline"]["sha256"],
            "actual remaining driver source differs")
    contract=docs[m["output_contract_role"]]
    require(contract["kind"]=="complete_WEJ_remaining_output_contract_v1"
            and contract["retained_prefix_contract_role"]=="recovery_contract",
            "different remaining output contract")
    require(contract["ordered_node_specs"]==m["ordered_node_specs"],
            "remaining DAG differs between manifest and contract")
    m["_resolved_output_contract"]=contract
    specs=[]
    for spec in m["ordered_node_specs"]:
        require(spec["schema_role"]==m["output_contract_role"],
                "remaining node must use the complete frozen output shape")
        spec=copy.deepcopy(spec)
        spec["conclusion_shape"]=contract["complete_conclusion_shapes"][spec["conclusion_shape_key"]]
        specs.append(spec)
    require(tuple(s["node_name"] for s in specs)==REMAINING_NODE_NAMES
            and tuple(s["record_count"] for s in specs)==REMAINING_COMPLETE_RECORD_COUNTS
            and tuple(s["printed_record_event_count"] for s in specs)==REMAINING_NEW_RECORD_COUNTS
            and [s["dependency_names"] for s in specs]==
                [[],[REMAINING_NODE_NAMES[0]],[REMAINING_NODE_NAMES[1]]],
            "remaining-only complete node graph changed")
    byname={s["node_name"]:s for s in specs}
    gate_names=[g["name"] for g in contract["complete_index_shape"]["gates"]]
    require(len(gate_names)==9 and m["expected_final_gate_count"]==9,
            "remaining gate count differs")
    input_sha={role:files[role]["sha256"] for role in m["mathematical_input_roles"]}
    module_sha={role:files[role]["sha256"] for role in SCIENTIFIC_ROLES}
    params=copy.deepcopy(m["parameters"])
    state={
      "kind":INDEX_KIND,"complete":False,"proved":False,"actual_returncode":None,"failure":None,
      "public_repository":PUBLIC,"run_id":os.environ["GITHUB_RUN_ID"],
      "run_attempt":os.environ["GITHUB_RUN_ATTEMPT"],
      "workflow_event_commit":os.environ["GITHUB_SHA"],
      "actual_scientific_checkout_commit":os.environ["ACTUAL_CHECKOUT_COMMIT"],
      "source_sha256":files["remaining_pipeline"]["sha256"],
      "scientific_module_sha256":module_sha,
      "input_manifest_sha256":args.manifest_sha,
      "parameters":params,"parameters_sha256":digest(compact(params)),
      "mathematical_input_sha256":input_sha,"runtime":runtime,"arithmetic_bits":320,
      "gates":[],"node_receipts":[],"original_input_files":[],
      "locked_attempted_nodes":[],"active_node":None,"stage":"admission",
      "actual_progress":[],"actual_mathematical_wall_seconds":None,
      "old_scientific_calls":0,"old_binary_parts_restored":0,
      "new_reproducible_arrays_persisted":False,"new_artifacts":0,"new_Releases":0,
      "retained_scope":copy.deepcopy(m["retained_scope"])}
    require(set(state)==set(INDEX_FIELDS)
            and hex_string(state["actual_scientific_checkout_commit"],40),
            "remaining index or actual checkout identity differs")
    completed={};saved_documents={};bindings={};progress={}
    api=None
    def checkpoint(stage=None,emit=False):
        if stage is not None:state["stage"]=stage
        payload=write_atomic(out/"index.json",state)
        if emit:emit_file("index.json",payload)
    def gate(name):
        require(len(state["gates"])<len(gate_names)
                and name==gate_names[len(state["gates"])],"remaining gate order differs")
        state["gates"].append({"name":name,"passed":True})
        checkpoint()
    def binding_for(name):
        dependencies={}
        for dep in byname[name]["dependency_names"]:
            require(dep in completed,"unpaid remaining predecessor: "+dep)
            dependencies[dep]=copy.deepcopy(completed[dep])
        return {"problem_id":m["problem_id"]+"/"+name,
          "parameters_sha256":state["parameters_sha256"],
          "mathematical_input_sha256":copy.deepcopy(input_sha),
          "scientific_module_sha256":copy.deepcopy(module_sha),
          "direct_dependency_receipts":dependencies}
    def publish_envelope(name,payload):
        require(name==state["active_node"] and name in byname
                and name not in completed,"invalid remaining node publication")
        require(payload.get("kind")==ENVELOPE_KIND and payload.get("node_name")==name
                and payload.get("binding")==bindings[name],"remaining node binding differs")
        spec=byname[name];relative=spec["relative_path"]
        require(relative=="graphs/"+name+".json","different fixed scientific path")
        data=write_atomic(out/relative,payload);emit_file(relative,data)
        if payload["complete"] is True:
            # Preserve the entire mathematical result before every shape/size/count gate.
            completed[name]={"file":relative,"bytes":len(data),"sha256":digest(data)}
            saved_documents[name]=copy.deepcopy(payload["conclusion"])
            state["node_receipts"].append({"node_name":name,**completed[name]})
            state["actual_progress"].append({"node_name":name,"complete_file_saved":True})
            checkpoint()
            require(set(payload)==COMPLETE_NODE_FIELDS
                    and full_shape(payload["conclusion"],spec["conclusion_shape"]),
                    "complete remaining conclusion shape differs: "+name)
            require(ball_count(payload["conclusion"])==spec["record_count"]
                    and payload["printed_record_event_count"]==spec["printed_record_event_count"],
                    "remaining preserved or new record count differs: "+name)
            require(len(data)<=spec["publication_max_bytes"] and len(data)<100000,
                    "complete graph preserved before its publication size gate: "+name)
            gate("complete natural scientific node "+name)
        else:
            require(set(payload)==PARTIAL_NODE_FIELDS,"remaining partial envelope lost a field")
            checkpoint()
        saved=exact_json((out/relative).read_bytes())
        require(json_equal(saved,payload),"complete canonical atomic readback differs")
        return saved
    def begin_node(name):
        require(name not in state["locked_attempted_nodes"],"an attempted node cannot repeat")
        k=len(state["locked_attempted_nodes"])
        require(k<len(specs) and specs[k]["node_name"]==name,"remaining node order differs")
        bindings[name]=binding_for(name)
        state["active_node"]=name;state["locked_attempted_nodes"].append(name)
        checkpoint("evaluating "+name)
        publish_envelope(name,{"kind":ENVELOPE_KIND,"node_name":name,
          "binding":copy.deepcopy(bindings[name]),"complete":False,
          "printed_record_events":[],"conclusion":None,"explicit_math_prefix":None,
          "failure":None,"automatic_retry_authorized":False})
    def publishing_node(name,producer):
        begin_node(name)
        require(api._ACTIVE_RECORD_CAPTURE is None,"nested remaining record capture")
        capture={"records":[]};math_published=False
        def prefix(event=None,failure=None,returned=None):
            if name in completed:return
            publish_envelope(name,{"kind":ENVELOPE_KIND,"node_name":name,
              "binding":copy.deepcopy(bindings[name]),"complete":False,
              "printed_record_events":copy.deepcopy(capture["records"]),
              "conclusion":copy.deepcopy(returned),
              "explicit_math_prefix":copy.deepcopy(progress.get(name)),
              "failure":failure,"automatic_retry_authorized":False})
        capture["on_record"]=prefix;api._ACTIVE_RECORD_CAPTURE=capture
        def bare_callback(callback_name,doc):
            nonlocal math_published
            require(callback_name==name,"remaining producer changed its node")
            issued={e["record"]["ball"] for e in capture["records"]}
            require(issued.issubset(api.all_saved_ball_strings(doc)),
                    "computed new record missing from whole remaining graph")
            payload={"kind":ENVELOPE_KIND,"node_name":name,
              "binding":copy.deepcopy(bindings[name]),"complete":True,
              "printed_record_event_count":len(capture["records"]),
              "all_printed_records_in_complete_conclusion":True,
              "conclusion":copy.deepcopy(doc),"failure":None,
              "automatic_retry_authorized":False}
            saved=publish_envelope(name,payload);math_published=True
            return copy.deepcopy(saved["conclusion"])
        try:
            work,doc=producer(bare_callback)
            require(math_published and json_equal(saved_documents[name],doc),
                    "remaining producer did not preserve its complete graph")
        except BaseException as error:
            if name not in completed:
                prefix(failure={"type":type(error).__name__,"message":str(error)},
                       returned=locals().get("doc"))
            raise
        finally:
            api._ACTIVE_RECORD_CAPTURE=None
        state["active_node"]=None;checkpoint()
        return work
    try:
        checkpoint(emit=True)
        gate(gate_names[0])
        admitted,=complete_expected_original_documents(root,m,receipts)
        gate(gate_names[1])
        partial=admitted["complete_original_partial_envelope"]
        prefix=partial["explicit_math_prefix"]["complete_scientific_document_prefix"]
        phase_records=admitted["complete_phase_derivative_record_qualification"]
        require(admitted["preserved_record_counts"]==RETAINED_RECORD_COUNTS,
                "remaining exact preserved record counts differ")
        gate(gate_names[2])
        filename=ORIGINAL_FILENAMES[0]
        require(m["original_input_filenames"]==list(ORIGINAL_FILENAMES),
                "different retained-prefix admission document")
        payload=write_atomic(out/filename,admitted);emit_file(filename,payload)
        state["original_input_files"].append({"file":filename,"bytes":len(payload),
                                             "sha256":digest(payload)})
        checkpoint()
        require(len(payload)<100000 and
                len(payload)<=m["original_input_specs"][0]["publication_max_bytes"],
                "complete retained-prefix admission preserved before size gate")
        require(json_equal(exact_json((out/filename).read_bytes()),admitted),
                "retained-prefix admission atomic readback differs")
        gate(gate_names[3])
        from flint import ctx
        ctx.prec=320
        api=load_remaining_math(code["remaining_math"],files["remaining_math"]["sha256"])
        require(api.admit_phase_records(docs["WGS_main"])==phase_records,
                "remaining math changed the exact paid derivative qualification")
        original=docs["prior_original_consumed"]["complete_original_consumed_record_objects"]
        extension=docs["prior_extension"]["conclusion"]
        mean_union=docs["prior_mean_union"]["conclusion"]
        negative=docs["prior_negative"]["conclusion"]
        publishing_node(REMAINING_NODE_NAMES[0],
          lambda pub:api.complete_free_map_suffix(prefix,phase_records,extension,pub,progress))
        publishing_node(REMAINING_NODE_NAMES[1],
          lambda pub:api.complete_four_waist_endpoints(original,
              saved_documents[REMAINING_NODE_NAMES[0]],extension,mean_union,pub,progress))
        publishing_node(REMAINING_NODE_NAMES[2],
          lambda pub:api.complete_whole_error(original,negative,
              saved_documents[REMAINING_NODE_NAMES[1]],pub,progress))
        require(len(completed)==3
                and state["locked_attempted_nodes"]==list(REMAINING_NODE_NAMES),
                "remaining complete DAG was not saved")
        for role,spec in files.items():
            require(sha(root/spec["path"])==spec["sha256"],
                    "one immutable input changed during remaining mathematics")
        gate(gate_names[7])
        require(all(state["retained_scope"][k] is False for k in
          ("passing_high_cutoff_proved","finite_Schur_inverse_proved",
           "full_incoming_inverse_proved","full_nonlinear_background_proved","final_surface_proved")),
          "an unpaid scope was promoted")
        gate(gate_names[8])
        require(len(state["gates"])==9,"remaining structural gate count")
        state.update(complete=True,proved=True,actual_returncode=0,failure=None,stage="complete")
    except BaseException as error:
        state.update(complete=False,proved=False,actual_returncode=1,
          failure={"type":type(error).__name__,"message":str(error),
                   "active_node":state.get("active_node")},stage="preserved_failure")
        print("WEJ_REMAINING_PRESERVED_FAILURE "+
              json.dumps(state["failure"],ensure_ascii=False),flush=True)
    finally:
        state["actual_mathematical_wall_seconds"]=time.monotonic()-started
        checkpoint(emit=True)
    if not state["complete"]:raise SystemExit(1)

if __name__=="__main__":
    main()
