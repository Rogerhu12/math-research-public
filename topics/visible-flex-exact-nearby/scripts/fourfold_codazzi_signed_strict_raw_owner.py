"""One new complete signed strict coefficient/J-window target in public Actions.

The old TCXV entry is used ONLY for its complete original raw-input admission.
No TC trial, residual, matrix or completed source-window target is callable.
The new raw whole-cell coefficient arrays are saved privately in complete
chunks, read back in full, hashed, and THEN used for the new global reductions.
Only the entire small conclusion and exact private-carrier receipts are public.
"""
from __future__ import annotations
import argparse, ast, gzip, hashlib, importlib.util, json, math, os, platform
import struct, sys, time, traceback
from fractions import Fraction
from pathlib import Path
from types import SimpleNamespace

TOPIC = "topics/visible-flex-exact-nearby"
REPOSITORY = "Rogerhu12/math-research-public"
SOURCE = TOPIC+"/scripts/fourfold_codazzi_signed_strict_raw_owner.py"
PARENT_MANIFEST = TOPIC+"/notes/2026-11-28-true-root-trial-complete2677-inputs.json"
PARENT_MANIFEST_SHA = "6b82d09170ed4ec780eccd0910cb69df98615390ef2f73237ed324d1e3f2c692"
PARENT_OWNER = TOPIC+"/scripts/fourfold_codazzi_true_root_parallel_vector_trial_owner.py"
PARENT_OWNER_SHA = "2408b84e7aa820ec6942dcd6255b77583cd776072c09fb6f521866930fcb7200"
JWS_PROOF_SHA = "52944b39487cb34690c733529b88e45b964b0028d5fd5c487ec4a73c630dfa09"
LAURENT_SHA = "217a91e25ec7bb6cad5c115ddc4749f4d714c5ca47601e8ad8dd540e69ed1718"
KIND = "R149_complete_signed_strict_raw_coefficients_and_same_J_windows_v1"
MANIFEST_KIND = "R149_complete_signed_strict_raw_inputs_v1"
TARGET = "complete_strict_signed_coefficients_and_same_J_windows"
RUNTIME = {"python":"3.12.14","packages":{"numpy":"2.3.5","python-flint":"0.9.0"}}
PARAMETERS = {
    "arithmetic_bits":320,"physical_frequency_factor":4,"physical_period":"pi/2",
    "strict_interval":["0","76285779072683/320000000000000"],
    "selected_parameter_absolute_upper":"4684129926501/50000000000000000000000",
    "base_coordinates":65,"direction_coordinates":193,"original_cubic_pieces":6144,
    "original_complete_scalar_rows":7721,"original_whole_parts":40,
    "true_radial_derivative_orders":[0,1,2,3],"derived_radial_derivative_orders":[0,1,2],
    "complete_derived_fields":["T0","rQ","V0","theta"],
    "derived_angular_norm_orders":[0,1,2,3,4],"new_exact_record_count":72,
    "new_whole_private_cell_chunk_size":128,"private_carrier_format":"RCS1-complete-cell-binary64-directed-boxes",
    "maximum_private_bytes":4294967296,"maximum_complete_cells":20000,
    "maximum_scientific_seconds":19500,"maximum_actual_bytes":95000,
    "old_scientific_target_calls":0,"whole_new_global_genuine_B_gap_proved_here":False,
    "uniform_high_response_proved_here":False,"full_physical_Schur_proved_here":False,
}
FIELDS = (
    "kind","identity","parameters","runtime","stage","complete","proved","failure",
    "actual_returncode","actual_mathematical_wall_seconds","completed_targets","saved_record_count",
    "new_records","full_saved_prefix","original_input_identity","necessary_raw_input_restoration",
    "original_angular_inverse_predecessor","complete_plan_identity","whole_private_carrier_receipts",
    "new_coefficient_cells_completed","old_scientific_target_calls","new_arrays_published",
    "new_artifacts","new_Releases","result",
)


def require(ok,message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),
                       ensure_ascii=False,allow_nan=False)+"\n").encode()


def atomic(path,raw):
    path = Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    candidate = path.with_name(path.name+".candidate")
    with candidate.open("wb") as stream:
        stream.write(raw);stream.flush();os.fsync(stream.fileno())
    require(candidate.read_bytes() == raw,"entire new object readback")
    candidate.replace(path)


def load(path,label):
    spec = importlib.util.spec_from_file_location(label,path)
    require(spec is not None and spec.loader is not None,"complete pinned Python source")
    module = importlib.util.module_from_spec(spec)
    sys.modules[label] = module
    spec.loader.exec_module(module)
    return module


def admit(root,raw,digest,rows_index):
    root = Path(root).resolve()
    require(0 < len(raw) < 100000 and sha(raw) == digest,"one entire concrete RCS manifest")
    manifest = json.loads(raw)
    require(manifest["kind"] == MANIFEST_KIND and manifest["scientific_kind"] == KIND
            and manifest["repository"] == REPOSITORY and manifest["parameters"] == PARAMETERS
            and manifest["runtime"] == RUNTIME and manifest["target_order"] == [TARGET]
            and manifest["allowed_scientific_fields"] == sorted(FIELDS),
            "same complete new signed target and exact scope")
    specs = {item["role"]:item for item in manifest["files"]}
    require(len(specs) == len(manifest["files"]),"one whole specification per role")
    for role,spec in specs.items():
        path = Path(spec["path"])
        require(not path.is_absolute() and ".." not in path.parts
                and str(path).startswith(TOPIC+"/"),"authorized complete topic input")
        body = (root/path).read_bytes()
        require(len(body) == spec["bytes"] and sha(body) == spec["sha256"],
                "entire immutable new input: "+role)
        require(len(body) < 100000,"complete current source below original file limit")
        if str(path).endswith(".py"):
            ast.parse(body,filename=str(path))
    require(specs["science"]["path"] == SOURCE
            and sha(Path(__file__).read_bytes()) == specs["science"]["sha256"],
            "entire actually executing RCS owner")
    require(specs["parent_manifest"]["path"] == PARENT_MANIFEST
            and specs["parent_manifest"]["sha256"] == PARENT_MANIFEST_SHA
            and specs["parent_owner"]["path"] == PARENT_OWNER
            and specs["parent_owner"]["sha256"] == PARENT_OWNER_SHA
            and specs["JWS_proof"]["sha256"] == JWS_PROOF_SHA
            and specs["laurent_math"]["sha256"] == LAURENT_SHA,
            "same original complete raw entry and complete new angular inverse proof")
    proof = (root/specs["JWS_proof"]["path"]).read_text()
    require(all(needle in proof for needle in ("7/5","3/8","JWS")),
            "the frozen whole proof contains both exact same-inverse slots")
    parent = json.loads((root/PARENT_MANIFEST).read_bytes())
    closure = parent["files"]+parent["historical_inputs"]
    require(manifest["whole_original_raw_closure"] == {
        "manifest_path":PARENT_MANIFEST,"manifest_bytes":specs["parent_manifest"]["bytes"],
        "manifest_sha256":PARENT_MANIFEST_SHA,"current_input_count":len(parent["files"]),
        "historical_input_count":len(parent["historical_inputs"]),
        "complete_descriptors_bytes":len(canonical(closure)),
        "complete_descriptors_sha256":sha(canonical(closure)),
        "all40_whole_original_native_parts_required":True,
        "old_worker_prefix_stops_before_target_reservation_and_science":True},
        "the complete original raw descriptor closure is inherited whole")
    old = load(root/PARENT_OWNER,"_RCS_complete_original_raw_admission")
    original = old.preflight(SimpleNamespace(repo=str(root),input_root=str(root),
        manifest=str(root/PARENT_MANIFEST),manifest_sha=PARENT_MANIFEST_SHA,
        rows_index=str(rows_index)))
    require(not any(name in sys.modules for name in ("numpy","flint","scipy")),
            "every full original native/source admission precedes numerical import")
    return manifest,specs,original


def validate(document,manifest):
    require(sorted(document) == sorted(FIELDS) and document["kind"] == KIND
            and document["parameters"] == manifest["parameters"]
            and document["old_scientific_target_calls"] == 0
            and all(document[name] == 0 for name in ("new_arrays_published","new_artifacts","new_Releases")),
            "complete RCS scientific shape and no old scientific target")
    count = document["saved_record_count"]
    require(count in (0,1) and document["completed_targets"] == [TARGET][:count]
            and set(document["new_records"]) == set(document["completed_targets"]),
            "one complete natural new conclusion, with its entire prefix retained")
    require(document["new_coefficient_cells_completed"] >= 0,"actual whole-cell count")
    if document["complete"]:
        require(count == 1 and document["proved"] is True and document["failure"] is None
                and document["actual_returncode"] == 0 and document["full_saved_prefix"] is None,
                "one actual complete successful target")
        body = document["new_records"][TARGET]
        require(len(body["complete_new_records"]) == 72
                and set(body["complete_new_records"]) == set(record_names())
                and body["all_true_original_cells_and_interfaces_retained"] is True
                and body["same_true_J_on_all_four_windows"] is True
                and body["ordinary_raw_partial_r_jets_not_differentiated_scalar_tails"] is True
                and body["uniform_genuine_high_response_proved"] is False,
                "every full signed coefficient and original-window slot")
        require(document["result"]["uniform_high_response_proved"] is False
                and document["result"]["full_physical_Schur_proved"] is False
                and document["result"]["topic_completion_proved"] is False,
                "the new coefficient/inverse input is not a whole high-response proof")
    return document


def record_names():
    names = ["%s_radial%d_angular%d_A0_upper"%(field,p,q)
        for field in PARAMETERS["complete_derived_fields"]
        for p in PARAMETERS["derived_radial_derivative_orders"]
        for q in PARAMETERS["derived_angular_norm_orders"]]
    names += ["complete_L_H"+s+"_upper" for s in ("minus5_3","minus1","minus2_3","0","1_3")]
    names += ["new_joint_J0_upper","selected_same_J0_upper",
        "same_J_Hminus2_to_Hminus1_upper","same_J_Hminus5_3_to_Hminus2_3_upper",
        "same_J_Hminus8_3_to_Hminus5_3_upper","eta_positive_lower","new_DJ_positive_lower"]
    require(len(names) == len(set(names)) == 72,"entire fixed new record ledger")
    return names


def raw_inputs(np,flint,admitted,root,private,progress):
    old_manifest,roles,raws,helper,prior,rows,identity = admitted
    backend,backend_receipts = helper.directed_backend(
        np,flint,raws[roles["box_math"]["path"]],raws[roles["fft_math"]["path"]])
    arb = flint.arb
    def exact(value):
        value = Fraction(value)
        return arb(value.numerator)/value.denominator
    # Only the three fields used by the exact original repair materializer.
    # No TC norm weights, finite trial, QR or source array is constructed.
    context = SimpleNamespace(np=np,arb_box=backend["arb_box"],exact=exact)
    reader,reader_receipt = helper.candidate_reader(np,raws[roles["candidate_reader"]["path"]])
    iterator,repair_receipt = helper.repair_iterator(raws[roles["repair_source"]["path"]])
    base = reader(root/roles["base_index"]["path"])
    direction = reader(root/roles["direction_index"]["path"])
    arrays = {}
    def allocate(name,shape):
        size = math.prod(shape)*8
        require(name not in arrays and sum(x["bytes"] for x in arrays.values())+size
                < PARAMETERS["maximum_private_bytes"],"necessary complete raw offset budget")
        path = private/(name+".f64")
        require(not path.exists(),"one fresh necessary same-definition offset array")
        array = np.memmap(path,dtype="<f8",mode="w+",shape=shape,order="C")
        arrays[name] = {"bytes":size,"path":path,"array":array}
        return array
    offsets,offset_receipts = helper.materialize_repairs(
        context,base,direction,iterator,prior,allocate,progress)
    for item in arrays.values():
        item["array"].flush();item["array"].flags.writeable=False
    receipt = {"candidate_reader":reader_receipt,"repair_reader":repair_receipt,
        "directed_backend":backend_receipts,"whole_exact_offset_chains":offset_receipts,
        "old_complete_trial_or_source_or_matrix_targets_called":0,
        "all7721_original_rows_reused_without_enclosure_recalculation":True}
    return base,direction,offsets,rows,receipt


def outward_four(value):
    require(value.is_finite(),"finite complete signed complex coefficient")
    answer = []
    for scalar in (value.real,value.imag):
        if scalar.is_zero():
            answer.extend((0.,0.));continue
        lower,upper = float(scalar.lower()),float(scalar.upper())
        require(math.isfinite(lower) and math.isfinite(upper),
                "directed binary64 private carrier has finite endpoints")
        answer.extend((math.nextafter(lower,-math.inf),math.nextafter(upper,math.inf)))
    return tuple(answer)


def write_cell(stream,cell,coefficients,windows,arb):
    """Save ALL new signed coefficients and ALL new joint-circle bounds."""
    header = dict(cell=cell,fields=[],windows={})
    arrays = []
    # Raw u/v/beta/eta accompany the derived fields, so the new same-circle
    # J target consumes exactly the same complete signed input carrier.
    for name in ("u","v","beta","eta",*PARAMETERS["complete_derived_fields"]):
        values = coefficients[name]
        retain = values.n if name in ("u","v","beta","eta") else 3
        require(values.n >= retain,"every actual normalized radial coefficient")
        for order in range(retain):
            polynomial = values.c[order]
            lower,upper = polynomial.lo,polynomial.hi
            if upper < lower:
                # A genuinely zero Laurent polynomial still has one full
                # explicit signed zero coefficient in this carrier format.
                lower = upper = 0
            header["fields"].append({"name":name,"radial_order":order,
                                     "mode_first":lower,"mode_last":upper})
            arrays.extend(outward_four(polynomial.coeff(k)) for k in range(lower,upper+1))
    for name,value in windows.items():
        if name == "complete_L_windows":
            header["windows"][name] = {key:record(val,"upper") for key,val in value.items()}
        elif isinstance(value,bool):
            header["windows"][name] = value
        else:
            header["windows"][name] = record(value,"lower" if name.endswith("lower") else "upper")
    raw = canonical(header)
    stream.write(struct.pack("<Q",len(raw)));stream.write(raw)
    for quadruple in arrays:
        stream.write(struct.pack("<4d",*quadruple))


def record(value,kind):
    require(kind in ("upper","lower") and value.is_finite(),"one whole directed new record")
    point = value.upper() if kind == "upper" else value.lower()
    if kind == "upper":
        require(point >= 0,"nonnegative complete upper")
    else:
        require(point > 0,"strict complete positive lower")
    text = point.str(70)
    # The printed ball is an enclosure; its directed endpoint is the output.
    return {"ball":text,"bound":kind}


def read_chunk(path,arb,acb,lp,jet,expected_cells):
    """Read complete bytes, parse every coefficient, and reject any trailing data."""
    raw = path.read_bytes()
    payload = gzip.decompress(raw)
    offset = 0
    decoded = []
    for expected in expected_cells:
        require(offset+8 <= len(payload),"complete private cell header length")
        length, = struct.unpack_from("<Q",payload,offset);offset += 8
        require(0 < length < 100000 and offset+length <= len(payload),"whole private header")
        header = json.loads(payload[offset:offset+length]);offset += length
        require(header["cell"] == expected,"entire exact original cell identity")
        fields = {}
        for entry in header["fields"]:
            name,p = entry["name"],entry["radial_order"]
            require(p == len(fields.setdefault(name,[])),"consecutive complete radial coefficients")
            lo,hi = entry["mode_first"],entry["mode_last"]
            require(type(lo) is type(hi) is int and -1000 <= lo <= hi <= 1000,
                    "the complete finite Fourier support")
            values = []
            for unused in range(lo,hi+1):
                require(offset+32 <= len(payload),"whole signed coefficient box")
                a,b,c,d = struct.unpack_from("<4d",payload,offset);offset += 32
                require(all(math.isfinite(x) for x in (a,b,c,d)) and a <= b and c <= d,
                        "finite ordered directed private endpoints")
                values.append(acb(arb(a).union(arb(b)),arb(c).union(arb(d))))
            fields[name].append(lp(values,lo))
        require(set(fields) == {"u","v","beta","eta",*PARAMETERS["complete_derived_fields"]},
                "all raw and derived fields in every complete private cell")
        decoded.append((header,{name:jet(values,lp) for name,values in fields.items()}))
    require(offset == len(payload),"no unconsumed private coefficient or missing cell")
    receipt = {"file":path.name,"bytes":len(raw),"sha256":sha(raw),
        "complete_uncompressed_bytes":len(payload),"complete_uncompressed_sha256":sha(payload),
        "first_cell":expected_cells[0]["index"],"last_cell_exclusive":expected_cells[-1]["index"]+1}
    return decoded,receipt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("repo","manifest","manifest-sha","rows-index","out","private","checkout"):
        parser.add_argument("--"+name,required=True)
    parser.add_argument("--preflight-only",action="store_true")
    args = parser.parse_args()
    root,output,private = Path(args.repo).resolve(),Path(args.out),Path(args.private)
    raw = Path(args.manifest).read_bytes()
    manifest,specs,original = admit(root,raw,args.manifest_sha,args.rows_index)
    if args.preflight_only:
        print(canonical({"kind":"RCS_complete_original_input_admission_v1",
            "manifest_sha256":args.manifest_sha,"original_input_identity":original[-1],
            "numerical_modules_imported":False}).decode(),end="",flush=True)
        return
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY
            and os.environ.get("GITHUB_RUN_ATTEMPT") == "1",
            "one first-attempt public execution of the complete new target")
    from importlib.metadata import version
    actual_runtime = {"python":platform.python_version(),
                      "packages":{name:version(name) for name in RUNTIME["packages"]}}
    require(actual_runtime == RUNTIME,"fixed complete actual arithmetic runtime")
    import numpy as np
    import flint
    flint.ctx.prec = PARAMETERS["arithmetic_bits"]
    arb,acb = flint.arb,flint.acb
    math_module = load(root/specs["signed_math"]["path"],"_RCS_new_signed_math")
    raw_module = load(root/specs["raw_math"]["path"],"_RCS_new_raw_math")
    laurent = load(root/specs["laurent_math"]["path"],"_RCS_original_complete_Laurent_arithmetic")
    lp,jet = laurent.LP,math_module.RadialJet
    private.mkdir(parents=True,exist_ok=True)
    require(not output.exists(),"no complete target or failed prefix is overwritten")
    state = {"kind":KIND,"identity":{"manifest_sha256":args.manifest_sha,
        "source_sha256":specs["science"]["sha256"],"signed_math_sha256":specs["signed_math"]["sha256"],
        "raw_math_sha256":specs["raw_math"]["sha256"],"run_id":os.environ["GITHUB_RUN_ID"],
        "run_attempt":"1","workflow_event_commit":os.environ["GITHUB_SHA"],
        "actual_scientific_checkout":args.checkout},"parameters":PARAMETERS,"runtime":actual_runtime,
        "stage":"original_inputs_admitted","complete":False,"proved":False,"failure":None,
        "actual_returncode":None,"actual_mathematical_wall_seconds":None,
        "completed_targets":[],"saved_record_count":0,"new_records":{},"full_saved_prefix":None,
        "original_input_identity":original[-1],"necessary_raw_input_restoration":None,
        "original_angular_inverse_predecessor":{"whole_JWS_proof_sha256":JWS_PROOF_SHA,
            "same_complete_J0_upper":"7/5","same_DJ_positive_lower":"3/8",
            "same_true_original_reflected_angular_inverse":True},
        "complete_plan_identity":None,"whole_private_carrier_receipts":[],
        "new_coefficient_cells_completed":0,"old_scientific_target_calls":0,
        "new_arrays_published":0,"new_artifacts":0,"new_Releases":0,"result":None}
    begin = time.monotonic()
    def save():
        state["actual_mathematical_wall_seconds"] = time.monotonic()-begin
        validate(state,manifest)
        body = canonical(state)
        require(len(body) <= PARAMETERS["maximum_actual_bytes"],"complete small new scientific conclusion")
        atomic(output,body)
    def progress(stage,values):
        print(json.dumps({"stage":stage,**values},sort_keys=True),flush=True)
    try:
        base,direction,offsets,rows,restoration = raw_inputs(
            np,flint,original,root,private,progress)
        state["necessary_raw_input_restoration"] = restoration
        nodes,plan = raw_module.strict_partition(rows,base["radial_nodes"])
        state["complete_plan_identity"] = {"complete_cells":len(plan),
            "canonical_plan_bytes":len(canonical(plan)),"canonical_plan_sha256":sha(canonical(plan)),
            "all_exact_scalar_and_cubic_seams_retained":True,
            "compact_support_endpoints_explicit":True,"same_strict_interval":PARAMETERS["strict_interval"]}
        require(len(plan) <= PARAMETERS["maximum_complete_cells"],"entire actual raw-cell workload")
        weights = {};global_bounds = {name:arb(0) for name in record_names()}
        lower_names = {"eta_positive_lower","new_DJ_positive_lower"}
        for name in lower_names:
            global_bounds[name] = None
        state["stage"] = "new_complete_signed_raw_cells"
        total_private = 0
        chunk_size = PARAMETERS["new_whole_private_cell_chunk_size"]
        for start in range(0,len(plan),chunk_size):
            require(time.monotonic()-begin < PARAMETERS["maximum_scientific_seconds"],
                    "new arithmetic time bound; preserve the whole accepted prefix")
            selected = plan[start:start+chunk_size]
            path = private/("signed-strict-cells-%05d-%05d.bin.gz"%(start,start+len(selected)))
            require(not path.exists(),"one fresh entire new private coefficient chunk")
            with path.open("wb") as raw_stream:
                with gzip.GzipFile(fileobj=raw_stream,mode="wb",mtime=0) as stream:
                    for cell in selected:
                        left,right = map(Fraction,cell["interval"])
                        raw_fields = raw_module.selected_fields(arb,acb,lp,jet,
                            rows[cell["original_row"]],base,direction,offsets,cell["piece"],left,right)
                        coefficients = math_module.complete_raw_coefficients(raw_fields)
                        windows = raw_module.joint_strict_J_windows(arb,coefficients,weights)
                        write_cell(stream,cell,coefficients,windows,arb)
            total_private += path.stat().st_size
            require(total_private <= PARAMETERS["maximum_private_bytes"],
                    "whole new private carrier budget, never a partial truncation")
            decoded,receipt = read_chunk(path,arb,acb,lp,jet,selected)
            for header,fields in decoded:
                for field in PARAMETERS["complete_derived_fields"]:
                    for p in PARAMETERS["derived_radial_derivative_orders"]:
                        polynomial = fields[field].c[p]
                        sums = [arb(0) for q in PARAMETERS["derived_angular_norm_orders"]]
                        for k in range(polynomial.lo,polynomial.hi+1):
                            magnitude = abs(polynomial.coeff(k)).upper()*math.factorial(p)
                            multiplier = 1
                            for q in PARAMETERS["derived_angular_norm_orders"]:
                                sums[q] += magnitude*multiplier;multiplier *= 4*abs(k)
                        for q,value in enumerate(sums):
                            key = "%s_radial%d_angular%d_A0_upper"%(field,p,q)
                            global_bounds[key] = max(global_bounds[key],value.upper())
                windows = header["windows"]
                for key in ("new_joint_J0_upper","selected_same_J0_upper",
                            "same_J_Hminus2_to_Hminus1_upper",
                            "same_J_Hminus5_3_to_Hminus2_3_upper",
                            "same_J_Hminus8_3_to_Hminus5_3_upper"):
                    value = arb(windows[key]["ball"]).upper()
                    global_bounds[key] = max(global_bounds[key],value)
                for s,label in (("-5/3","minus5_3"),("-1","minus1"),("-2/3","minus2_3"),
                                 ("0","0"),("1/3","1_3")):
                    key = "complete_L_H"+label+"_upper"
                    global_bounds[key] = max(global_bounds[key],arb(windows["complete_L_windows"][s]["ball"]).upper())
                for key in lower_names:
                    value = arb(windows[key]["ball"]).lower()
                    require(value > 0,"full serialized same-circle positive lower")
                    old = global_bounds[key]
                    global_bounds[key] = value if old is None else min(old,value)
            state["whole_private_carrier_receipts"].append(receipt)
            state["new_coefficient_cells_completed"] = start+len(selected)
            state["full_saved_prefix"] = {"next_cell":start+len(selected),
                "complete_new_records":{key:record(value,"lower" if key in lower_names else "upper")
                                         for key,value in global_bounds.items()},
                "all_completed_cells_are_whole":True,"previous_successful_targets_recomputed":0}
            save()
            progress("new_signed_strict_whole_chunk_complete",{
                "complete_cells":start+len(selected),"all_cells":len(plan),
                "complete_chunk_sha256":receipt["sha256"],"old_scientific_targets":0})
        body = {"complete_new_records":state["full_saved_prefix"]["complete_new_records"],
            "all_true_original_cells_and_interfaces_retained":True,
            "same_true_J_on_all_four_windows":True,
            "ordinary_raw_partial_r_jets_not_differentiated_scalar_tails":True,
            "all_complete_signed_Laurent_products_retained":True,
            "selected_intrinsic_and_direction_use_the_same_delta":True,
            "true_physical_second_row_mean_retained":True,
            "uniform_genuine_high_response_proved":False,
            "complete_private_carrier_index_bytes":len(canonical(state["whole_private_carrier_receipts"])),
            "complete_private_carrier_index_sha256":sha(canonical(state["whole_private_carrier_receipts"]))}
        state.update(stage="complete_new_signed_raw_and_same_J_target",complete=True,proved=True,
            actual_returncode=0,completed_targets=[TARGET],saved_record_count=1,
            new_records={TARGET:body},full_saved_prefix=None,
            result={"complete_new_signed_strict_raw_coefficient_carrier_proved":True,
                "same_true_global_strict_negative_J_windows_proved":True,
                "uniform_high_response_proved":False,"full_physical_Schur_proved":False,
                "topic_completion_proved":False})
        save()
    except Exception as exc:
        state.update(stage="failed_new_target_with_full_prefix",failure={"type":type(exc).__name__,
            "message":str(exc),"traceback":traceback.format_exc()},actual_returncode=1)
        save();raise


if __name__ == "__main__":
    main()
