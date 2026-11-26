"""TC one complete finite trial/residual/pairing target in public Actions.

The unknown full PDE inverse is neither imported nor consumed.  Every
published scalar concerns the exact finite trial defined here.  Whole
old row and intrinsic carriers are admitted before numerical imports.
"""
from __future__ import annotations
import argparse, ast, copy, hashlib, importlib.util, json, math, os
import platform, resource, sys, time, traceback
from fractions import Fraction
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby/"
SOURCE_PATH = TOPIC+"scripts/fourfold_codazzi_true_root_trial_owner.py"
KIND = "R149_complete_true_root_finite_trial_residuals_v1"
PREFLIGHT_KIND = "R149_true_root_finite_trial_metadata_preflight_v1"
MANIFEST_KIND = "R149_true_root_finite_trial_complete_inputs_v1"
TARGETS = ["complete_signed_finite_trial_matrices_and_waist96",
           "complete_negative_finite_trial_sources96",
           "complete_positive_finite_trial_sources96"]
FILES = {
    "state":"actual-trial-state.json",
    "matrix":"complete-signed-trial-matrices.json",
    "negative":"complete-negative-trial-sources.json",
    "positive":"complete-positive-trial-sources.json",
    "prefix":"complete-radial-integration-prefix.json",
}
PARAMETERS = {
    "arithmetic_bits":320,"public_digits":50,"private_RW_digits":80,
    "new_private_matrix_digits":80,"head_modes":96,"real_state_dimension":193,
    "full_residual_angular_support":288,"directed_Fourier_grid":1024,
    "proposal_Fourier_grid":512,"proposal_exponential_Taylor_degree":24,
    "exact_alpha":"6890507429876859/9007199254740992",
    "exact_selected_delta_absolute_upper":"9368259853002/100000000000000000000000",
    "root_interval":["1191984371497/5000000000000","2383968743003/10000000000000"],
    "positive_cut":"1192029371497/5000000000000",
    "negative_cut":"2333968743003/10000000000000","outer":"25/8",
    "cutoff_start":"3","old_eta_half_width":"1/1000000000",
    "true_root_node_not_replaced_by_a_float":True,
    "proposal_only_delta":"0","proposal_only_Robin_slope":"13/80",
    "exact_root_even96":"identity","shared_positive_negative_root_value":True,
    "radial_trial_degree":7,"cap_trial_degree_after_cutoff":14,
    "ordinary_radial_measure":"dr","normalized_circle":True,
    "source_windows":{
        "positive_low":["L2","L2"],
        "positive_high_collar":["Hminus2over3","Hminus2over3"],
        "positive_high_body":["Hminus2over3","Hminus2over3"],
        "negative_root":["Hminus2over3","Hminus1"],
        "negative_strict":["Hminus1","Hminus1"]},
    "independent_density_means":2,"root_high_stable_error_exact":"0",
    "root_even96_error_exact":"0","all_outer_and_jump_errors_exact":"0",
    "new_actual_PDE_columns_or_inverse_claimed":False,
    "old_R142_P224_or_SC_true_column_target_called":False,
    "old_scalar_norm_target_calls":0,"new_artifact_or_Release_uploads":0,
    "maximum_trial_nodes":8000,"maximum_certificate_cells":9000,
    "maximum_private_live_array_bytes":8589934592,
    "maximum_scientific_seconds":16800,"complete_cell_checkpoint_stride":8,
    "floating_proposal_runtime_core":"Haswell","floating_proposal_threads":"1",
}
RUNTIME = {"python":"3.12.14","packages":{"numpy":"2.3.5","python-flint":"0.9.0"}}
SOURCE_HASHES = {
    "proof":"6313fc86c667e9e0c74675e9773bc7160bf3a555c2f326659bf54ad060e7d13f",
    "trial_math":"1131c70ad0f568a692321dd2aab9de76b194aa5abb3f160924ab3befa290771c",
    "proposal_math":"a50faff5db45a96cd2fb8ffa7b9e0881d7df992d1e67ae7b587efed7feb49025",
    "inputs_math":"4409dd3c8733972e3d9479ef6449ab85b39f2d2900cd5fe4376dda5cd335c826",
}
STATE_FIELDS = [
    "actual_checkout_commit","actual_returncode","complete","completed_targets",
    "continuation","failure","input_identity","kind","matrix_receipt",
    "negative_receipt","old_scientific_target_calls","parameters",
    "positive_receipt","prefix_receipt","preparation","private_arrays_published",
    "proposal","proved","run_attempt","run_id","runtime","stage","wall_seconds",
    "workflow_event_commit"]


def require(ok,message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),
                       ensure_ascii=False,allow_nan=False)+"\n").encode()


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def file_digest(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for part in iter(lambda:stream.read(1048576),b""):
            value.update(part)
    return value.hexdigest()


def atomic(path,raw):
    path = Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    temporary = path.with_name(path.name+".candidate")
    with temporary.open("wb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    require(temporary.read_bytes() == raw,"whole candidate bytes read back before formal rename")
    temporary.replace(path)
    require(path.read_bytes() == raw,"whole formal bytes read back")


def import_source(path,name):
    spec = importlib.util.spec_from_file_location(name,path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def role_map(manifest):
    all_specs = manifest["files"]+manifest["historical_inputs"]
    by_path = {item["path"]:item for item in all_specs}
    require(len(by_path) == len(all_specs),"each complete original file has one canonical spec")
    roles = {name:by_path[path] for name,path in manifest["roles"].items()}
    return all_specs,by_path,roles


def preflight(args):
    root = Path(args.repo).resolve()
    inputs_root = Path(args.input_root).resolve()
    raw = Path(args.manifest).read_bytes()
    require(0 < len(raw) < 100000 and digest(raw) == args.manifest_sha,
            "one complete exact new manifest")
    manifest = json.loads(raw)
    require(manifest["kind"] == MANIFEST_KIND and manifest["scientific_kind"] == KIND
            and manifest["repository"] == "Rogerhu12/math-research-public"
            and manifest["parameters"] == PARAMETERS and manifest["runtime"] == RUNTIME
            and manifest["target_order"] == TARGETS,
            "complete declared finite-trial target, windows, runtime and parameters")
    all_specs,by_path,roles = role_map(manifest)
    require(roles["owner"]["path"] == SOURCE_PATH
            and (root/SOURCE_PATH).resolve() == Path(__file__).resolve(),
            "the entire actual owner is this pinned source")
    raw_by_path = {}
    for spec in all_specs:
        rel = Path(spec["path"])
        require(not rel.is_absolute() and ".." not in rel.parts
                and str(rel).startswith(TOPIC),"every input stays in the same authorized topic")
        path = inputs_root/rel
        require(path.is_file() and path.stat().st_size == spec["bytes"]
                and file_digest(path) == spec["sha256"],"whole immutable input bytes: "+str(rel))
        if spec.get("encoding") != "gzip-npz":
            payload = path.read_bytes()
            if "git_blob_sha" in spec:
                actual_blob = hashlib.sha1(b"blob "+str(len(payload)).encode()+b"\0"+payload).hexdigest()
                require(actual_blob == spec["git_blob_sha"],"whole exact original Git blob identity")
            raw_by_path[spec["path"]] = payload
            if spec in manifest["files"]:
                require(0 < len(payload) < 100000,"each entire current UTF8 input is small")
                text = payload.decode("utf-8")
                if str(rel).endswith(".py"):
                    ast.parse(text,filename=str(rel))
    for role,want in SOURCE_HASHES.items():
        require(roles[role]["sha256"] == want,"fixed reviewed complete new source: "+role)
    require(digest(Path(__file__).read_bytes()) == roles["owner"]["sha256"],
            "entire owner bytes match the frozen manifest")
    helper = import_source(inputs_root/roles["inputs_math"]["path"],"_TC_complete_inputs")
    rwm = json.loads(raw_by_path[roles["RW_manifest"]["path"]])
    nwm = json.loads(raw_by_path[roles["NW_manifest"]["path"]])
    prior_specs = {item["path"]:item for old in (rwm,nwm)
                   for item in old["files"]+old.get("historical_inputs",[])}
    for path,item in prior_specs.items():
        got = by_path[path]
        require(all(got[key] == item[key] for key in ("path","bytes","sha256","git_blob_sha")),
                "every whole inherited original input retained: "+path)
    def owner(old,label):
        item = next(spec for spec in old["files"] if spec["role"] == "science")
        return import_source(inputs_root/item["path"],"_TC_readonly_"+label)
    prior = helper.admit_prior_bundles(raw_by_path,roles,owner(rwm,"RW"),owner(nwm,"NW"))
    rows_doc = json.loads(Path(args.rows_index).read_bytes())
    require(rows_doc["kind"] == "TC_restored_complete_original_40_parts_v1"
            and rows_doc["original_manifest_sha256"] == helper.PRIOR_SHA["old_body_manifest"],
            "whole original native restoration index")
    rows,part_receipts = helper.admit_all_rows(
        [Path(args.rows_index).parent/entry["file"] for entry in rows_doc["parts"]],prior)
    require(sorted(part_receipts,key=lambda x:x["indices"]) == rows_doc["part_receipts"],
            "all40 actual restored compressed payloads read and verified")
    require(not any(name in sys.modules for name in ("numpy","flint","scipy")),
            "all original whole-input admission completed before numerical import")
    identity = {
        "manifest_sha256":digest(raw),
        "complete_current_input_count":len(manifest["files"]),
        "complete_historical_input_count":len(manifest["historical_inputs"]),
        "complete_input_receipts_sha256":digest(canonical(all_specs)),
        "original_row_payload_sha256":helper.ROW_PAYLOAD,
        "complete_original_rows":7721,"complete_original_parts":40,
        "whole_original_part_receipts_sha256":digest(canonical(part_receipts)),
        "RW_actual_sha256":helper.PRIOR_SHA["RW_actual"],
        "RW_execution_sha256":helper.PRIOR_SHA["RW_execution"],
        "same_selected_family":prior["RW"]["family"],
        "scientific_sources":{name:roles[name]["sha256"] for name in
                ("owner","trial_math","proposal_math","inputs_math","box_math","fft_math",
                 "candidate_reader","repair_source","direction_source")},
        "new_true_column_inverse_used":False,
    }
    if manifest.get("continuation") is not None:
        admitted_prior = admit_prior_metadata(manifest,roles,raw_by_path,identity)
        require(manifest["new_target_order"] == admitted_prior["missing_targets"],
                "the new target list omits every formally completed prior conclusion")
    else:
        require(manifest["new_target_order"] == TARGETS,"the first launch has exactly the three new targets")
    return manifest,roles,raw_by_path,helper,prior,rows,identity



def whole_receipt(raw,spec,execution):
    require(any(item["path"] == spec["path"] and item["sha256"] == spec["sha256"]
                and item["bytes"] == spec["bytes"] for item in execution["scientific_files"])
            and len(raw) == spec["bytes"] and digest(raw) == spec["sha256"],
            "entire actual prior published object is bound by its execution receipt")


def validate_complete_result(document,name,proposal,manifest_sha,family):
    """Metadata only; formal objects were whole-readback validated before rename."""
    common = {"kind","complete","proved","trial_definition_sha256","proposal_identity",
              "input_manifest_sha256","same_selected_family","true_PDE_columns_or_inverse_proved"}
    require(document["complete"] is document["proved"] is True
            and document["proposal_identity"] == proposal
            and document["trial_definition_sha256"] == proposal["definition_sha256"]
            and document["input_manifest_sha256"] == manifest_sha
            and document["same_selected_family"] == family
            and document["true_PDE_columns_or_inverse_proved"] is False,
            "whole actual finite-trial result and exact prior qualification")
    names = {"column_%03d"%j for j in range(1,97)}
    def scalar(record):
        require(isinstance(record,dict) and set(record) == {"ball"}
                and isinstance(record["ball"],str),"entire saved scalar enclosure")
    if name == "matrix":
        extra = {"complete_rows","complete_columns","density_independent_mean_coordinates",
                 "original_RW_actual_sha256","original_RW_scalar_targets_recomputed",
                 "complete_waist_trial_norms","matrices"}
        require(set(document) == common|extra
                and document["kind"] == "R149_complete_signed_finite_trial_matrices_v1"
                and document["complete_rows"] == document["complete_columns"] == 96
                and document["density_independent_mean_coordinates"] == 2
                and document["original_RW_actual_sha256"]
                    == "b0faf218c059b6f7ee113a5f127a7518e78d2c87dc70b4dcf650ce97594c7fa4"
                and document["original_RW_scalar_targets_recomputed"] == 0
                and set(document["complete_waist_trial_norms"]) == names
                and set(document["matrices"]) == {"physical_primitive96","declared_incoming_cosine96"},
                "whole96 waist norms and both complete signed finite matrices")
        for record in document["complete_waist_trial_norms"].values():
            scalar(record)
        for matrix in document["matrices"].values():
            bounds = {"infinity_upper","one_upper","two_upper","Frobenius_upper"}
            require(set(matrix) == bounds|{"whole_private_carrier","rows","columns",
                        "complete_entries_read_back","true_PDE_matrix_claimed"}
                    and matrix["rows"] == matrix["columns"] == 96
                    and matrix["complete_entries_read_back"] == 9216
                    and matrix["true_PDE_matrix_claimed"] is False
                    and set(matrix["whole_private_carrier"]) == {"file","bytes","sha256"}
                    and type(matrix["whole_private_carrier"]["bytes"]) is int
                    and matrix["whole_private_carrier"]["bytes"] > 0
                    and len(matrix["whole_private_carrier"]["sha256"]) == 64,
                    "all signed entries saved and read back, with complete carrier identity")
            for key in bounds:
                scalar(matrix[key])
        return
    require(name in ("negative","positive"),"one complete declared source object")
    windows = (("negative_root","negative_strict") if name == "negative"
               else ("positive_low","positive_high_collar","positive_high_body"))
    extra = {"complete_columns","source_windows","ordinary_radial_measure","normalized_circle",
             "complete_original_coefficient_cover","complete_source_records","all_boundary_and_jump_errors_exact"}
    if name == "negative":
        extra |= {"complete_waist_trial_norms","waist_norms_copied_verbatim_from_same_new_matrix_result",
                  "independent_waist_mean_coordinates"}
    else:
        extra |= {"complete_original_14_ports_nonzero_indices","stable_high_root_and_even96_errors_exact"}
    require(set(document) == common|extra
            and document["kind"] == "R149_complete_"+name+"_finite_trial_sources96_v1"
            and document["complete_columns"] == 96
            and document["source_windows"] == {key:PARAMETERS["source_windows"][key] for key in windows}
            and document["ordinary_radial_measure"] == "dr" and document["normalized_circle"] is True
            and document["complete_original_coefficient_cover"] == 7721
            and document["all_boundary_and_jump_errors_exact"] == "0"
            and set(document["complete_source_records"]) == names,
            "all96 original-window source conclusions, full means and boundary/jump qualification")
    for row in document["complete_source_records"].values():
        require(set(row) == set(windows),"every declared source on every column")
        for record in row.values():
            scalar(record)
    if name == "negative":
        require(set(document["complete_waist_trial_norms"]) == names
                and document["independent_waist_mean_coordinates"] == 2,
                "complete original physical waist and both independent means")
        for record in document["complete_waist_trial_norms"].values():
            scalar(record)
    else:
        require(document["complete_original_14_ports_nonzero_indices"] == {
                    "1":"positive_high_collar","2":"positive_high_body","7":"positive_low"}
                and document["stable_high_root_and_even96_errors_exact"] == "0",
                "the exact original physical port indices, no hidden omitted root source")



def admit_prior_metadata(manifest,roles,raws,current_identity):
    """Entire actual predecessor; formal outputs cannot be omitted to replay them."""
    continuation = manifest["continuation"]
    require(isinstance(continuation,dict) and set(continuation) == {
                "kind","original_run_id","original_run_attempt"}
            and continuation["kind"] == "R149_same_exact_trial_complete_prefix_continuation_v1",
            "one explicit whole same-trial continuation")
    for role in ("prior_state","prior_execution","prior_manifest"):
        require(role in roles,"a continuation needs its entire actual "+role)
    previous = json.loads(raws[roles["prior_state"]["path"]])
    execution = json.loads(raws[roles["prior_execution"]["path"]])
    old_manifest = json.loads(raws[roles["prior_manifest"]["path"]])
    old_sha = roles["prior_manifest"]["sha256"]
    require(sorted(previous) == STATE_FIELDS
            and previous["kind"] == KIND and previous["parameters"] == PARAMETERS
            and previous["input_identity"]["scientific_sources"] == current_identity["scientific_sources"]
            and previous["input_identity"]["same_selected_family"] == current_identity["same_selected_family"]
            and previous["input_identity"]["manifest_sha256"] == old_sha
            and previous["old_scientific_target_calls"] == previous["private_arrays_published"] == 0
            and previous["run_id"] == continuation["original_run_id"]
            and previous["run_attempt"] == continuation["original_run_attempt"] == "1",
            "entire unchanged predecessor state, exact science owner and same selected member")
    require(old_manifest["kind"] == MANIFEST_KIND and old_manifest["scientific_kind"] == KIND
            and old_manifest["parameters"] == PARAMETERS and old_manifest["runtime"] == RUNTIME
            and old_manifest["target_order"] == TARGETS
            and old_manifest["allowed_scientific_fields"] == STATE_FIELDS
            and old_manifest["roles"]["owner"] == roles["owner"]["path"]
            and any(item["path"] == roles["owner"]["path"] and item["sha256"] == roles["owner"]["sha256"]
                    and item["bytes"] == roles["owner"]["bytes"] for item in old_manifest["files"]),
            "whole immediately preceding manifest binds this identical owner definition")
    require(execution["kind"] == "R149_complete_true_root_finite_trial_execution_v1"
            and execution["repository"] == "Rogerhu12/math-research-public"
            and execution["run_id"] == previous["run_id"] and execution["run_attempt"] == "1"
            and execution["manifest_sha256"] == old_sha
            and execution["scientific_children"] == 1
            and type(execution["actual_child_returncode"]) is int
            and execution["scientific_started_utc"]
            and execution["old_numerical_producers_called"] == 0
            and execution["old_completed_targets_recomputed"] == 0
            and execution["new_arrays_published"] == 0,
            "actual predecessor numerical child and complete unchanged execution evidence")
    whole_receipt(raws[roles["prior_state"]["path"]],roles["prior_state"],execution)
    base = old_manifest["operation"]["output_base"]+"/run-"+previous["run_id"]+"-1/"
    formal = {}
    for name,filename in FILES.items():
        matches = [item for item in execution["scientific_files"] if item["path"] == base+filename]
        require(len(matches) <= 1,"unique entire formal object in prior execution")
        if not matches:
            require(name == "state" or "prior_"+name not in roles,
                    "no fabricated prior mathematical object absent from actual execution")
            continue
        role = "prior_"+name
        require(role in roles and all(roles[role][key] == matches[0][key]
                                     for key in ("path","bytes","sha256")),
                "every actual formal prior object must be supplied whole; no completed target may be replayed")
        whole_receipt(raws[roles[role]["path"]],roles[role],execution)
        formal[name] = json.loads(raws[roles[role]["path"]])
    require(set(item["path"] for item in execution["scientific_files"])
                == {base+FILES[name] for name in formal} and "state" in formal,
            "all original scientific publications are admitted, not a selected subset")
    available,origins = [],{}
    for name,target in zip(("matrix","negative","positive"),TARGETS):
        if name not in formal:
            require(target not in previous["completed_targets"],
                    "every old marked complete target retains its whole actual object")
            continue
        doc = formal[name]
        origin = doc["input_manifest_sha256"]
        spec = roles["prior_"+name]
        if origin != old_sha:
            require(old_manifest.get("continuation") is not None
                    and "prior_"+name in old_manifest["roles"]
                    and any(item["path"] == old_manifest["roles"]["prior_"+name]
                            and item["bytes"] == spec["bytes"] and item["sha256"] == spec["sha256"]
                            for item in old_manifest["files"]),
                    "verbatim inherited origin through the identical owner's complete prior input binding")
        validate_complete_result(doc,name,previous["proposal"],origin,
                                 current_identity["same_selected_family"])
        available.append(target)
        origins[name] = origin
    require(available == TARGETS[:len(available)]
            and previous["completed_targets"] == TARGETS[:len(previous["completed_targets"])]
            and set(previous["completed_targets"]).issubset(available),
            "formal complete conclusions can lead the old marker, never contradict it")
    require(len(available) < 3,
            "all three actual formal mathematical conclusions are complete; no new science target exists")
    require("negative" not in formal or ("matrix" in formal and "prefix" in formal),
            "a complete negative conclusion retains both preceding complete objects")
    require("positive" not in formal or ("negative" in formal and "prefix" in formal),
            "a complete positive conclusion retains the entire prior source chain")
    if "prefix" in formal:
        prefix = formal["prefix"]
        require(prefix["scientific_sources"] == current_identity["scientific_sources"]
                and prefix["proposal_identity"] == previous["proposal"]
                and prefix["complete_cells_have_all_declared_sources"] is True
                and "matrix" in formal,
                "whole formal prefix of the exact same residual owner and saved trial")
    return {"completed_targets":available,"missing_targets":[x for x in TARGETS if x not in available],
            "formal_names":sorted(formal),"original_producer_manifest_sha256":origins}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("repo","manifest","manifest-sha","input-root","rows-index","out","private"):
        parser.add_argument("--"+name,required=True)
    parser.add_argument("--preflight-only",action="store_true")
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"
            and os.environ.get("GITHUB_RUN_ATTEMPT") == "1",
            "one public first-attempt science run")
    manifest,roles,raws,helper,prior,rows,input_identity = preflight(args)
    if args.preflight_only:
        print(canonical({"kind":PREFLIGHT_KIND,"complete":True,
                         "input_identity":input_identity,"new_scientific_calls":0}).decode(),end="")
        return 0
    output,private = Path(args.out),Path(args.private)
    output.mkdir(parents=True,exist_ok=True)
    private.mkdir(parents=True,exist_ok=True)
    require(not any((output/name).exists() for name in FILES.values()),
            "never overwrite an existing complete or failed new outcome")
    started = time.perf_counter()
    state = {
        "kind":KIND,"complete":False,"proved":False,"actual_returncode":None,
        "failure":None,"stage":"whole_original_inputs_admitted",
        "run_id":os.environ["GITHUB_RUN_ID"],"run_attempt":"1",
        "workflow_event_commit":os.environ["GITHUB_SHA"],
        "actual_checkout_commit":os.environ["ACTUAL_CHECKOUT_COMMIT"],
        "parameters":copy.deepcopy(PARAMETERS),"input_identity":input_identity,
        "runtime":None,"wall_seconds":0.,"preparation":{},
        "proposal":None,"matrix_receipt":None,"negative_receipt":None,
        "positive_receipt":None,"prefix_receipt":None,"completed_targets":[],
        "continuation":None,"old_scientific_target_calls":0,"private_arrays_published":0}
    require(sorted(state) == STATE_FIELDS,"complete exact scientific state schema")
    def receipt(path):
        path = Path(path)
        return {"file":path.name,"bytes":path.stat().st_size,"sha256":file_digest(path)}
    def save_state():
        state["wall_seconds"] = time.perf_counter()-started
        payload = canonical(state)
        require(len(payload) <= manifest["operation"]["maximum_state_bytes"],
                "whole scientific state fits its declared natural-object budget")
        atomic(output/FILES["state"],payload)
    def budget():
        require(time.perf_counter()-started <= PARAMETERS["maximum_scientific_seconds"],
                "finite-trial wall budget reached; complete saved radial prefix retained")
    def progress(name,record):
        budget()
        state["preparation"][name] = record
        save_state()
        print(canonical({"stage":name,**record}).decode(),end="",flush=True)
    save_state()
    try:
        require(os.environ.get("OPENBLAS_CORETYPE") == PARAMETERS["floating_proposal_runtime_core"]
                and all(os.environ.get(key) == PARAMETERS["floating_proposal_threads"] for key in
                        ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS",
                         "BLIS_NUM_THREADS","VECLIB_MAXIMUM_THREADS")),
                "one explicit deterministic floating-proposal BLAS branch and thread count")
        import numpy as np
        import flint
        from importlib.metadata import version
        runtime = {"python":platform.python_version(),
                   "packages":{name:version(name) for name in RUNTIME["packages"]}}
        require(runtime == RUNTIME and sys.byteorder == "little" and platform.machine() == "x86_64",
                "the entire declared scientific runtime and private float representation")
        flint.ctx.prec = PARAMETERS["arithmetic_bits"]
        arb = flint.arb
        state["runtime"] = {**runtime,"architecture":platform.machine(),
            "byteorder":sys.byteorder,"OPENBLAS_CORETYPE":os.environ["OPENBLAS_CORETYPE"],
            "floating_threads":1,"directed_bits":flint.ctx.prec}
        inputs_root = Path(args.input_root)
        module = import_source(inputs_root/roles["trial_math"]["path"],"_TC_directed_residual")
        proposal_module = import_source(inputs_root/roles["proposal_math"]["path"],"_TC_float_proposal")
        backend,backend_receipts = helper.directed_backend(np,flint,
            raws[roles["box_math"]["path"]],raws[roles["fft_math"]["path"]])
        context = module.DirectedContext(np,arb,backend["Box"],backend["CBox"],backend["zeros"],
            backend["arb_box"],backend["reduce_box"],backend["DirectedFFT"]())
        c = context
        state["preparation"]["pure_backend_AST_receipts"] = backend_receipts
        reader,reader_receipt = helper.candidate_reader(np,raws[roles["candidate_reader"]["path"]])
        iterator,repair_receipt = helper.repair_iterator(raws[roles["repair_source"]["path"]])
        base = reader(inputs_root/roles["base_index"]["path"])
        direction = reader(inputs_root/roles["direction_index"]["path"])
        state["preparation"]["old_reader_AST_receipts"] = [reader_receipt,repair_receipt]
        def read_ball(record):
            require(isinstance(record,dict),"entire saved original directed scalar record")
            if "lower" in record and "upper" in record:
                value = arb(record["lower"]).lower().union(arb(record["upper"]).upper())
            else:
                value = arb(record["ball"])
            require(value.is_finite(),"finite original complete directed scalar ball")
            return value
        arrays = {}
        def allocate(name,shape):
            require(name not in arrays and all(type(n) is int and n > 0 for n in shape),
                    "one complete declared private array")
            live = sum(info["bytes"] for info in arrays.values())
            size = math.prod(shape)*8
            require(live+size <= PARAMETERS["maximum_private_live_array_bytes"],
                    "declared complete private-array memory/disk bound")
            path = private/(name+".f64")
            require(not path.exists(),"private exact proposal array cannot be overwritten")
            value = np.memmap(path,dtype="<f8",mode="w+",shape=shape,order="C")
            arrays[name] = {"path":path,"shape":shape,"bytes":size,"array":value}
            return value
        def release(name):
            info = arrays.pop(name)
            info["array"].flush()
            del info["array"]
            info["path"].unlink()
        offsets,offset_receipts = helper.materialize_repairs(c,base,direction,iterator,
                                      prior,allocate,progress)
        state["preparation"]["same_exact_signed_offset_chains"] = offset_receipts
        definition,proposal_nodes,plan = helper.complete_plan(rows,base["radial_nodes"])
        require(len(proposal_nodes) <= PARAMETERS["maximum_trial_nodes"]
                and len(plan) <= PARAMETERS["maximum_certificate_cells"]
                and len(plan) > 0,"whole exact certificate plan within its explicit work bound")
        definition_sha = digest(canonical(definition))
        plan_sha = digest(canonical(plan))
        atomic(private/"complete-trial-definition.json",canonical(definition))
        atomic(private/"complete-certificate-plan.json",canonical(plan))
        reference = proposal_module.FloatingCentreReference(np,rows,base,
                         offsets["base"]["midpoint"],helper.ALPHA,read_ball)
        state["stage"] = "selecting_complete_new_finite_dyadic_trial"
        save_state()
        proposal_module.choose_all_columns(np,reference,proposal_nodes,
                            definition["root_index"],allocate,release,progress)
        saved_arrays,proposal_receipts = [],[]
        for name in ("trial_value","trial_derivative_1","trial_derivative_2","trial_derivative_3"):
            info = arrays[name]
            info["array"].flush()
            before = file_digest(info["path"])
            reopened = np.memmap(info["path"],dtype="<f8",mode="r",
                                 shape=info["shape"],order="C")
            for start in range(0,len(reopened),32):
                require(np.all(np.isfinite(reopened[start:start+32])),
                        "all entries of the saved whole proposal are finite")
            require(info["path"].stat().st_size == info["bytes"]
                    and file_digest(info["path"]) == before,
                    "complete saved private array was read back byte for byte")
            item = {"name":name,"shape":list(info["shape"]),
                    "bytes":info["bytes"],"sha256":before,
                    "encoding":"little-endian binary64 row-major exact dyadics"}
            proposal_receipts.append(item)
            saved_arrays.append(reopened)
        require(np.array_equal(saved_arrays[0][definition["root_index"],97:,:],np.eye(96)),
                "saved/readback true-root even96 block exactly identity")
        proposal_identity = {
            "definition_sha256":definition_sha,"certificate_plan_sha256":plan_sha,
            "complete_trial_nodes":len(proposal_nodes),"complete_certificate_cells":len(plan),
            "root_index":definition["root_index"],"root_node":"true_root",
            "proposal_root_dyadic":definition["proposal_root_dyadic"],
            "complete_endpoint_arrays":proposal_receipts,
            "source_sha256":roles["proposal_math"]["sha256"],
            "private_arrays_saved_and_completely_read_back":True,
            "exact_radial_derivative_in_certificate":"differentiate TC.7 with TRUE h",
            "trial_selection_is_not_a_numerical_certificate":True}
        state["proposal"] = proposal_identity
        state["stage"] = "complete_exact_trial_saved_and_read_back"
        save_state()

        def public_upper(value):
            require(value.is_finite() and value.upper() >= 0,"finite directed new scalar upper")
            point = value.upper()
            record = {"ball":point.str(PARAMETERS["public_digits"])}
            require(arb(record["ball"]).is_finite() and arb(record["ball"]).contains(point),
                    "whole serialized upper includes its directed value")
            return record,point
        def common(kind):
            return {"kind":kind,"complete":False,"proved":False,
                "trial_definition_sha256":definition_sha,"proposal_identity":proposal_identity,
                "input_manifest_sha256":args.manifest_sha,
                "same_selected_family":input_identity["same_selected_family"],
                "true_PDE_columns_or_inverse_proved":False}
        def save_result(name,document,originals):
            raw = canonical(document)
            require(len(raw) <= manifest["operation"]["maximum_"+name+"_bytes"],
                    "whole natural mathematical result fits its declared byte budget")
            candidate = output/(FILES[name]+".complete-candidate")
            atomic(candidate,raw)
            read = json.loads(candidate.read_bytes())
            require(read == document,"whole mathematical candidate readback")
            for location,value in originals:
                found = read
                for key in location:
                    found = found[key]
                require(arb(found["ball"]).contains(value),
                        "every complete saved scalar encloses its actual directed upper")
            validate_complete_result(read,name,proposal_identity,args.manifest_sha,
                                     input_identity["same_selected_family"])
            # Only an already whole-readback-validated natural object may have
            # the formal name.  It can legally lead the later state marker.
            candidate.replace(output/FILES[name])
            require((output/FILES[name]).read_bytes() == raw,"whole formal complete-result readback")
            return receipt(output/FILES[name])

        continuation = manifest.get("continuation")
        copied = {}
        initial_acc = {name:c.Box(np.zeros(96)) for name in module.NORM_NAMES}
        next_cell = 0
        if continuation is not None:
            previous = json.loads(raws[roles["prior_state"]["path"]])
            execution = json.loads(raws[roles["prior_execution"]["path"]])
            old_manifest = json.loads(raws[roles["prior_manifest"]["path"]])
            old_manifest_sha = roles["prior_manifest"]["sha256"]
            require(set(continuation) == {"kind","original_run_id","original_run_attempt"}
                    and continuation["kind"] == "R149_same_exact_trial_complete_prefix_continuation_v1"
                    and continuation["original_run_id"] == previous["run_id"]
                    and continuation["original_run_attempt"] == previous["run_attempt"] == "1"
                    and sorted(previous) == STATE_FIELDS
                    and previous["kind"] == KIND and previous["parameters"] == PARAMETERS
                    and previous["runtime"] == state["runtime"]
                    and previous["proposal"] == proposal_identity
                    and previous["input_identity"]["scientific_sources"] == input_identity["scientific_sources"]
                    and previous["input_identity"]["same_selected_family"] == input_identity["same_selected_family"]
                    and previous["input_identity"]["manifest_sha256"] == old_manifest_sha
                    and previous["old_scientific_target_calls"] == previous["private_arrays_published"] == 0
                    and previous["completed_targets"] == TARGETS[:len(previous["completed_targets"])],
                    "entire unchanged prior owner state and actual exact trial qualification")
            require(old_manifest["kind"] == MANIFEST_KIND and old_manifest["scientific_kind"] == KIND
                    and old_manifest["repository"] == "Rogerhu12/math-research-public"
                    and old_manifest["parameters"] == PARAMETERS and old_manifest["runtime"] == RUNTIME
                    and old_manifest["target_order"] == TARGETS
                    and old_manifest["roles"]["owner"] == roles["owner"]["path"]
                    and any(item["path"] == roles["owner"]["path"] and item["sha256"] == roles["owner"]["sha256"]
                            and item["bytes"] == roles["owner"]["bytes"] for item in old_manifest["files"]),
                    "whole prior manifest binds the identical original numerical owner")
            require(execution["kind"] == "R149_complete_true_root_finite_trial_execution_v1"
                    and execution["repository"] == "Rogerhu12/math-research-public"
                    and execution["run_id"] == previous["run_id"]
                    and execution["run_attempt"] == previous["run_attempt"]
                    and execution["manifest_sha256"] == old_manifest_sha
                    and execution["scientific_children"] == 1
                    and type(execution["actual_child_returncode"]) is int
                    and execution["scientific_started_utc"]
                    and execution["old_completed_targets_recomputed"] == 0
                    and execution["old_numerical_producers_called"] == 0
                    and execution["new_arrays_published"] == 0,
                    "whole actual prior execution, including its unchanged failed/finished branch")
            whole_receipt(raws[roles["prior_state"]["path"]],roles["prior_state"],execution)
            if "prior_prefix" in roles:
                prefix = json.loads(raws[roles["prior_prefix"]["path"]])
                whole_receipt(raws[roles["prior_prefix"]["path"]],roles["prior_prefix"],execution)
                fields = {"kind","run_id","run_attempt","proposal_identity","certificate_plan_sha256",
                    "scientific_sources","next_cell","complete_cell_count","total_cells",
                    "complete_cells_have_all_declared_sources","last_complete_cell",
                    "squared_norm_upper_exact_binary64","all96_columns_and_all_declared_source_components_retained",
                    "arbitrary_midpoint_not_used_as_an_upper","whole_mathematical_target_complete"}
                next_cell = prefix["next_cell"]
                require(set(prefix) == fields and prefix["kind"] == "R149_true_root_residual_full_cell_prefix_v1"
                        and prefix["run_id"] == previous["run_id"] and prefix["run_attempt"] == "1"
                        and prefix["proposal_identity"] == proposal_identity
                        and prefix["certificate_plan_sha256"] == plan_sha
                        and prefix["scientific_sources"] == input_identity["scientific_sources"]
                        and type(next_cell) is int and 0 <= next_cell <= len(plan)
                        and prefix["complete_cell_count"] == next_cell
                        and prefix["total_cells"] == len(plan)
                        and prefix["last_complete_cell"] == (None if next_cell == 0 else plan[next_cell-1])
                        and prefix["complete_cells_have_all_declared_sources"] is True
                        and prefix["all96_columns_and_all_declared_source_components_retained"] is True
                        and prefix["arbitrary_midpoint_not_used_as_an_upper"] is True
                        and prefix["whole_mathematical_target_complete"] is (next_cell == len(plan))
                        and set(prefix["squared_norm_upper_exact_binary64"]) == set(module.NORM_NAMES),
                        "entire exact formal whole-cell prefix, which may lead the old state marker")
                for name in module.NORM_NAMES:
                    values = prefix["squared_norm_upper_exact_binary64"][name]
                    require(len(values) == 96 and all(isinstance(value,str) for value in values),
                            "all96 prior complete source accumulators")
                    vector = np.array([float.fromhex(value) for value in values])
                    require(np.all(np.isfinite(vector)) and np.all(vector >= 0)
                            and [float(x).hex() for x in vector] == values,
                            "exact canonical nonnegative binary64 prior directed sums")
                    initial_acc[name] = c.Box(vector)
            for name,target in (("matrix",TARGETS[0]),("negative",TARGETS[1]),("positive",TARGETS[2])):
                role = "prior_"+name
                if role not in roles:
                    require(target not in previous["completed_targets"],
                            "every old marked complete natural object must be supplied whole")
                    continue
                spec = roles[role]
                whole_receipt(raws[spec["path"]],spec,execution)
                old = json.loads(raws[spec["path"]])
                origin_manifest_sha = old["input_manifest_sha256"]
                if origin_manifest_sha != old_manifest_sha:
                    # A verbatim copied conclusion keeps its original producer
                    # manifest forever.  The immediately preceding manifest
                    # pins these identical bytes as its prior natural object;
                    # the identical owner validated them before formal copy.
                    prior_role = "prior_"+name
                    require(old_manifest.get("continuation") is not None
                            and prior_role in old_manifest["roles"]
                            and any(item["path"] == old_manifest["roles"][prior_role]
                                    and item["bytes"] == spec["bytes"]
                                    and item["sha256"] == spec["sha256"]
                                    for item in old_manifest["files"]),
                            "whole unchanged inherited natural-object origin bound by the preceding manifest")
                validate_complete_result(old,name,proposal_identity,origin_manifest_sha,
                                         input_identity["same_selected_family"])
                # The formal complete mathematical object is authoritative;
                # a kill before the subsequent old state write does not erase it.
                atomic(output/FILES[name],raws[spec["path"]])
                copied[name] = old
                state[name+"_receipt"] = receipt(output/FILES[name])
                state["completed_targets"].append(target)
            require(state["completed_targets"] == TARGETS[:len(copied)],
                    "complete copied natural objects retain the original target order")
            require(not (len(copied) == 3),"all old natural targets are already complete; no new science target exists")
            require(not next_cell or "matrix" in copied,
                    "every nonempty accepted radial prefix retains the preceding complete matrix target")
            last_negative = max(i for i,item in enumerate(plan) if item["side"] == "negative")
            require("negative" not in copied or (next_cell > last_negative and "matrix" in copied),
                    "complete negative sources require the entire qualified negative integration prefix")
            require("positive" not in copied or next_cell == len(plan),
                    "complete positive sources require the entire qualified integration prefix")
            if "negative" in copied:
                require(copied["negative"]["complete_waist_trial_norms"]
                            == copied["matrix"]["complete_waist_trial_norms"],
                        "whole copied negative and matrix targets share the identical waist conclusion")
            state["continuation"] = {
                "whole_previous_run":previous["run_id"]+"/"+previous["run_attempt"],
                "completed_cells_copied_without_reintegration":next_cell,
                "complete_prior_targets_copied":list(state["completed_targets"]),
                "original_prior_completed_target_marker_retained":previous["completed_targets"],
                "formal_object_may_precede_original_marker":True,
                "original_producer_manifest_sha256_by_complete_object":{
                    name:doc["input_manifest_sha256"] for name,doc in copied.items()},
                "prior_whole_state_sha256":roles["prior_state"]["sha256"],
                "prior_whole_prefix_sha256":None if "prior_prefix" not in roles else roles["prior_prefix"]["sha256"],
                "prior_whole_execution_sha256":roles["prior_execution"]["sha256"],
                "prior_whole_manifest_sha256":old_manifest_sha}
            save_state()

        def scalar_inputs(row,left,right):
            scalar = {name:module.scalar_taylor(c,row["intrinsic_midpoint_jets"],
                row["intrinsic_whole_third_jets"],name,*row["interval"],
                left,right,read_ball) for name in ("beta","K","gamma","s")}
            active = Fraction(left) < helper.CONTROL[1] and Fraction(right) > helper.CONTROL[0]
            require(not active or helper.CONTROL[0] <= Fraction(left) < Fraction(right) <= helper.CONTROL[1],
                    "compact metric seam is in the complete certification partition")
            return module.selected_intrinsic_fees(c,scalar,row["intrinsic_whole_third_jets"],
                                                  helper.DELTA,active,read_ball)
        def scalar_point(field,coordinate):
            require(field.degree == 0,"whole angular scalar at the actual waist")
            value = module.trial_value(c,field.coefficients,c.box(coordinate))[0,0]
            error = float(np.max(field.error.hi))
            value = value+c.Box(-error,error)
            return arb(float(value.lo)).union(arb(float(value.hi)))

        if "matrix" not in copied:
            state["stage"] = "new_whole_signed_finite_trial_matrices"
            save_state()
            row0 = rows[0]
            left,right = map(Fraction,row0["interval"])
            scalar = scalar_inputs(row0,left,right)
            background = helper.selected_background(c,base,direction,offsets,
                row0["pieces"]["background"],left,right,scalar["s"],module)
            K0 = scalar_point(scalar["K"],-1)
            mean0 = scalar_point(background[1].mean(),-1)
            a0 = read_ball(row0["intrinsic_whole_third_jets"]["a"])
            require(K0.upper() < 0 and mean0.upper() < 0 and a0.lower() > 0,
                    "whole true selected waist q and physical density denominator")
            q0 = (-K0).sqrt()
            ng0 = a0*a0/(mean0*mean0)
            density = module.full_waist_density(c,c.Box(saved_arrays[0][0]),q0,ng0)
            waist_upper = c.sqrt_upper(module.density_norm_squared(c,density))
            matrix_doc = common("R149_complete_signed_finite_trial_matrices_v1")
            matrix_doc.update(complete_rows=96,complete_columns=96,
                density_independent_mean_coordinates=2,
                original_RW_actual_sha256=helper.PRIOR_SHA["RW_actual"],
                original_RW_scalar_targets_recomputed=0,
                complete_waist_trial_norms={},matrices={})
            originals = []
            for j,x in enumerate(waist_upper.hi,1):
                record,value = public_upper(arb(float(x)))
                matrix_doc["complete_waist_trial_norms"]["column_%03d"%j] = record
                originals.append((("complete_waist_trial_norms","column_%03d"%j),value))
            old = prior["RW_actual"]
            rw_math_path = inputs_root/prior["RW_specs"]["row_math"]["path"]
            rw_math = import_source(rw_math_path,"_TC_readonly_exact_RW_carrier")
            pp = prior["RW"]
            factory = rw_math.ReflectedRowFactory(flint,pp["H_sines"],pp["H_cosines"],
                pp["K_sines"],pp["K_cosines"],
                H_constant=pp["zero_translation_qualification"]["H_constant"],
                K_constant=pp["zero_translation_qualification"]["K_constant"])
            def old_carrier(filename,kind,values,extra,expected):
                values = list(values)
                document = {"kind":kind,"definition_sha256":old["definition_sha256"],
                    **extra,"all_real_balls":[value.str(PARAMETERS["private_RW_digits"]) for value in values]}
                raw = canonical(document)
                require(len(raw) == expected["bytes"] and digest(raw) == expected["sha256"]
                        and len(values) == expected["complete_real_count"],
                        "same whole already-defined RW carrier, no new row choice")
                atomic(private/filename,raw)
                restored = [arb(value) for value in json.loads((private/filename).read_bytes())["all_real_balls"]]
                require(all(value.contains(original) for value,original in zip(restored,values)),
                        "whole RW necessary input carrier read back")
                return restored
            grid = factory.materialize_whole_compound_grid()
            grid = old_carrier("same-RW-grid.json",
                "R149_complete_exact_compound_cosine_grid_carrier_v1",grid,
                {"grid_points":4096},old["private_grid_receipt"])
            factory.base_cosines = grid
            factory.previous = [arb(1) for _ in grid]
            factory.current = list(grid)
            matrices = {"physical_primitive96":[],"declared_incoming_cosine96":[]}
            for index in range(1,97):
                j,coefs = factory.next_complete_row()
                require(j == index,"same complete sequential exact RW row")
                coefs = old_carrier("same-RW-row-%03d.json"%j,
                    "R149_complete_exact_DFT_real_row_carrier_v1",coefs,
                    {"mode":j,"nonnegative_modes":[0,1024],
                     "negative_modes":"equal by exact evenness, not selected by midpoint"},
                    old["new_records"]["row_%03d"%j]["carrier"])
                for name,incoming in (("physical_primitive96",False),
                                      ("declared_incoming_cosine96",True)):
                    value = module.real_signed_density_pairing(c,coefs,density,incoming=incoming)
                    matrices[name].append([arb(float(a)).union(arb(float(b)))
                                           for a,b in zip(value.lo,value.hi)])
                if index % 16 == 0:
                    progress("same_RW_carriers_for_new_signed_pairings",{"complete_rows":index,"rows":96})
            for name,matrix in matrices.items():
                document = {"kind":"TC_complete_signed_finite_matrix_carrier_v1",
                    "name":name,"trial_definition_sha256":definition_sha,
                    "original_RW_definition_sha256":old["definition_sha256"],
                    "rows":96,"columns":96,
                    "all_signed_entry_balls":[[x.str(PARAMETERS["new_private_matrix_digits"]) for x in row]
                                               for row in matrix]}
                path = private/(name+".json")
                atomic(path,canonical(document))
                read = json.loads(path.read_bytes())
                restored = [[arb(value) for value in row] for row in read["all_signed_entry_balls"]]
                require(len(restored) == 96 and all(len(row) == 96 for row in restored)
                        and all(value.contains(original) for row,orig in zip(restored,matrix)
                                for value,original in zip(row,orig)),
                        "all9216 signed matrix entries saved and read back before norms")
                magnitude = [[abs(x).upper() for x in row] for row in restored]
                row_upper = max(sum(row,arb(0)).upper() for row in magnitude)
                column_upper = max(sum((magnitude[i][j] for i in range(96)),arb(0)).upper()
                                   for j in range(96))
                frobenius = sum((x*x for row in magnitude for x in row),arb(0)).upper().sqrt().upper()
                two = min((row_upper*column_upper).upper().sqrt().upper(),frobenius)
                result = {"whole_private_carrier":receipt(path),"rows":96,"columns":96,
                          "complete_entries_read_back":9216,"true_PDE_matrix_claimed":False}
                for key,value in (("infinity_upper",row_upper),("one_upper",column_upper),
                                  ("two_upper",two),("Frobenius_upper",frobenius)):
                    result[key],point = public_upper(value)
                    originals.append((("matrices",name,key),point))
                matrix_doc["matrices"][name] = result
            matrix_doc["complete"] = matrix_doc["proved"] = True
            state["matrix_receipt"] = save_result("matrix",matrix_doc,originals)
            state["completed_targets"].append(TARGETS[0])
            copied["matrix"] = matrix_doc
            save_state()

        accumulators = initial_acc
        def save_prefix(index):
            document = {
                "kind":"R149_true_root_residual_full_cell_prefix_v1",
                "run_id":state["run_id"],"run_attempt":"1",
                "proposal_identity":proposal_identity,"certificate_plan_sha256":plan_sha,
                "scientific_sources":input_identity["scientific_sources"],
                "next_cell":index,"complete_cell_count":index,"total_cells":len(plan),
                "complete_cells_have_all_declared_sources":True,
                "last_complete_cell":None if index == 0 else plan[index-1],
                "squared_norm_upper_exact_binary64":{
                    name:[float(x).hex() for x in accumulators[name].hi]
                    for name in module.NORM_NAMES},
                "all96_columns_and_all_declared_source_components_retained":True,
                "arbitrary_midpoint_not_used_as_an_upper":True,
                "whole_mathematical_target_complete":index == len(plan)}
            raw = canonical(document)
            require(len(raw) <= manifest["operation"]["maximum_prefix_bytes"],
                    "whole complete-cell norm prefix budget")
            atomic(output/FILES["prefix"],raw)
            require(json.loads((output/FILES["prefix"]).read_bytes()) == document,
                    "all saved exact-hex directed accumulators read back")
            state["prefix_receipt"] = receipt(output/FILES["prefix"])
            state["preparation"]["complete_certified_cells"] = index
            save_state()
        save_prefix(next_cell)

        def finish_sources(which):
            names = (("negative_root","negative_strict") if which == "negative"
                     else ("positive_low","positive_high_collar","positive_high_body"))
            doc = common("R149_complete_"+which+"_finite_trial_sources96_v1")
            doc.update(complete_columns=96,source_windows={name:PARAMETERS["source_windows"][name] for name in names},
                       ordinary_radial_measure="dr",normalized_circle=True,
                       complete_original_coefficient_cover=7721,
                       complete_source_records={},all_boundary_and_jump_errors_exact="0")
            if which == "negative":
                doc["complete_waist_trial_norms"] = copy.deepcopy(copied["matrix"]["complete_waist_trial_norms"])
                doc["waist_norms_copied_verbatim_from_same_new_matrix_result"] = state["matrix_receipt"]
                doc["independent_waist_mean_coordinates"] = 2
            else:
                doc["complete_original_14_ports_nonzero_indices"] = {"1":"positive_high_collar",
                           "2":"positive_high_body","7":"positive_low"}
                doc["stable_high_root_and_even96_errors_exact"] = "0"
            originals = []
            bounds = {name:c.sqrt_upper(accumulators[name]) for name in names}
            for j in range(96):
                key = "column_%03d"%(j+1)
                doc["complete_source_records"][key] = {}
                for name in names:
                    record,value = public_upper(arb(float(bounds[name].hi[j])))
                    doc["complete_source_records"][key][name] = record
                    originals.append((("complete_source_records",key,name),value))
            doc["complete"] = doc["proved"] = True
            state[which+"_receipt"] = save_result(which,doc,originals)
            copied[which] = doc
            state["completed_targets"].append(TARGETS[1 if which == "negative" else 2])
            save_state()
        last_negative = max(i for i,item in enumerate(plan) if item["side"] == "negative")
        if next_cell > last_negative and "negative" not in copied:
            finish_sources("negative")
        state["stage"] = "complete_true_selected_PDE_residual_integration"
        save_state()
        last_trial = None
        trial_coefficients = None
        for index in range(next_cell,len(plan)):
            budget()
            item = plan[index]
            row = rows[item["original_row"]]
            left,right = map(Fraction,item["interval"])
            piece = item["trial_piece"]
            if piece != last_trial:
                true_left,true_right,true_length = helper.true_interval(c,definition,piece)
                left_jets = [c.Box(array[piece]) for array in saved_arrays]
                right_jets = [c.Box(array[piece+1]) for array in saved_arrays]
                trial_coefficients = module.hermite_coefficients(c,left_jets,right_jets,true_length)
                last_trial = piece
            restricted = module.restrict_trial_coefficients(c,trial_coefficients,true_left,true_length,left,right)
            trial = module.reflection_polynomial(c,restricted)
            scale = c.exact(Fraction(2,1)/(right-left))
            radial = tuple(p.radial_derivative(scale) for p in trial)
            if item["side"] == "positive":
                chi,chir = module.cutoff_scalar(c,left,right)
                radial = tuple(chir*p+chi*dp for p,dp in zip(trial,radial))
                trial = tuple(chi*p for p in trial)
            scalar = scalar_inputs(row,left,right)
            background = helper.selected_background(c,base,direction,offsets,
                          row["pieces"]["background"],left,right,scalar["s"],module)
            operator = module.prepare_operator(background,scalar)
            residual = module.complete_residual(operator,trial,radial)
            contributions = {}
            for name in item["norms"]:
                subset = "low" if name == "positive_low" else "high" if name.startswith("positive_high") else "all"
                contributions[name] = module.pair_cell_norm_squared(
                    c,residual,right-left,PARAMETERS["source_windows"][name],subset)
                require(contributions[name].hi.shape == (96,)
                        and np.all(np.isfinite(contributions[name].hi)),
                        "complete finite directed cell fee for every one of96 columns")
            # All source components for this cell are formed BEFORE any
            # accumulator or complete-cell index can advance.
            updated = {name:c.add_upper(accumulators[name],value)
                       for name,value in contributions.items()}
            accumulators.update(updated)
            if (index+1) % PARAMETERS["complete_cell_checkpoint_stride"] == 0 or index in (last_negative,len(plan)-1):
                save_prefix(index+1)
                print(canonical({"complete_radial_cells":index+1,"total":len(plan),
                                 "complete_columns_per_cell":96,"side":item["side"]}).decode(),end="",flush=True)
            if index == last_negative and "negative" not in copied:
                finish_sources("negative")
        if "positive" not in copied:
            finish_sources("positive")
        require(set(state["completed_targets"]) == set(TARGETS)
                and all((output/FILES[name]).is_file() for name in ("matrix","negative","positive","prefix")),
                "every complete declared finite matrix and full positive/negative source target")
        state["completed_targets"] = list(TARGETS)
        state["complete"] = state["proved"] = True
        state["actual_returncode"] = 0
        state["stage"] = "complete_finite_trial_only_mathematics"
        save_state()
        print(canonical({"complete":True,"proved_finite_trial_only":True,
            "true_PDE_inverse_proved":False,"complete_columns":96,"complete_new_scalar_records":584,
            "output_receipts":{name:state[name+"_receipt"] for name in ("matrix","negative","positive","prefix")}}).decode(),
              end="",flush=True)
        return 0
    except BaseException as error:
        state["complete"] = state["proved"] = False
        state["actual_returncode"] = 1
        state["failure"] = {"type":type(error).__name__,"message":str(error)[:2000],
                            "traceback":traceback.format_exc()[-6000:]}
        state["stage"] = "failed_with_whole_exact_trial_and_complete_cell_prefix_retained"
        save_state()
        print(traceback.format_exc(),flush=True)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
