"""CFC actual owner: full original TC96 normalized columns and physical rows.

Admission requires completed TC/SC, BFP/DCP, H96 and PWA96, not useful prefixes.
Original input reconstruction is separate from every completed scientific
target. This owner does not claim the independent remaining Schur blocks.
"""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util, json, os, platform, re
import subprocess, sys, textwrap, time, traceback
from pathlib import Path
from types import SimpleNamespace

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
KIND = "R149_complete_original_TC96_full_target_columns_v1"
MANIFEST_KIND = "R149_complete_original_TC96_full_target_columns_inputs_v1"
SOURCE = TOPIC+"/scripts/fourfold_codazzi_complete_finite_columns_owner.py"
MATH = TOPIC+"/scripts/fourfold_codazzi_complete_finite_columns_math.py"
CARRIERS = TOPIC+"/scripts/fourfold_codazzi_complete_finite_columns_carriers.py"
RUNTIME = {"python":"3.12.14", "packages":{"numpy":"2.3.5", "python-flint":"0.9.0"}}
PARAMETERS = {"arithmetic_bits":320, "original_columns":96, "target_trial_modes":512,
    "normalizer_modes":2048, "full_signed_image_modes":2560, "complete_grid":8192,
    "complete_opposite_head":2048, "private_disk_limit_bytes":12884901888,
    "maximum_scientific_wall_seconds":18000, "public_bytes":99000,
    "old_scientific_targets_called":0, "exact_unchanged_TC_source_coordinates":True,
    "whole_true_target_tail_zeroed":False, "whole_joint_error_method":"sum_of_all96_squares",
    "same_sign_forward_B_sign":"+", "same_sign_A_sign":"-",
    "phase_height_world_ports_independent":True,
    "complete_PWA96_same_rho_rows_and_receivers_required":True}
SCI_FIELDS = sorted(["kind","manifest_sha256","run_id","run_attempt","checkout","parameters",
    "runtime","complete","proved","actual_returncode","failure","stage","progress","wall_seconds",
    "completed_targets","new_records","private_objects","whole_batch_prefix","carrier_restoration",
    "result","old_scientific_targets_called","new_arrays_published"])


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                       allow_nan=False)+"\n").encode()


def parse(raw):
    return json.loads(raw, parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))


def atomic(path, raw):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name+".partial")
    with tmp.open("wb") as f:
        f.write(raw); f.flush(); os.fsync(f.fileno())
    os.replace(tmp, path)
    require(path.read_bytes() == raw, "one whole private/public byte readback")


def load(path, name):
    raw = Path(path).read_bytes(); ast.parse(raw)
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


def checked(root, spec):
    path = spec["path"]
    require(path.startswith(TOPIC+"/") and all(p not in ("", ".", "..") for p in path.split("/")),
            "one full safe original topic path")
    raw = (root/path).read_bytes()
    require(len(raw) == spec["bytes"] and sha(raw) == spec["sha256"], "whole input: "+path)
    if "git_blob_sha" in spec:
        require(hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest() == spec["git_blob_sha"],
                "whole original Git object: "+path)
    return raw


def closure(root, manifest):
    specs = {item["role"]:item for item in manifest["files"]+manifest.get("historical_inputs", [])}
    require(len(specs) == len(manifest["files"])+len(manifest.get("historical_inputs", [])),
            "all original closure roles retained")
    raws = {role:checked(root, spec) for role,spec in specs.items()}
    paths = {role:root/spec["path"] for role,spec in specs.items()}
    return specs, raws, paths


ASQ18_MATH = TOPIC + "/scripts/fourfold_codazzi_asq18_CFC_finite_reconstruction.py"
ASQ18_MATH_SHA = "e984f6cde3a0d36c0edccd96f763ec257a0d5559bd1b36311ef3922e58eff22d"
ASQ18_PROOF = TOPIC + "/results/R149-supplement-actual-signed-Theta-trial-and-finite-inverse-by-primitive-residual.md"
ASQ20_PROOF = TOPIC + "/results/R149-supplement-actual-low-coordinate-recovery-on-complete-physical-columns.md"
H96_RESUME_MANIFEST_SHA = "e730fd1e12b72356c88aa7718f8baa4e5e5c083e66a60a6612d71028d281ef69"
H96_RESUME_WORKER_SHA = "735b03dae67f035ca52464e5f4605c5b235479a1bbfedccfa095ff9164193b03"
H96_RESUME_OWNER_SHA = "538e9198a2b04fcb75389aefe95422ab6df909be3efbfe4a412f54aeab288981"


def original_public_validator(root, worker, definition, env):
    if env["args"].manifest_sha == H96_RESUME_MANIFEST_SHA:
        specs = env["by_role"]
        require(specs["worker"]["sha256"] == H96_RESUME_WORKER_SHA
                and specs["science"]["sha256"] == H96_RESUME_OWNER_SHA,
                "the whole first H96 suffix public and scientific definitions")
        funcs = [node for node in ast.walk(worker.build_adapter(root))
                 if isinstance(node, ast.FunctionDef) and node.name == "validate_output"]
        require(len(funcs) == 1, "the unique actual public H96 suffix validator")
        validator = ast.fix_missing_locations(ast.Module(body=funcs,type_ignores=[]))
        env.update(definitions=definition, PARENT=definition.PARENT_RUN)
    else:
        validator = textwrap.dedent(worker.VALIDATOR)
    exec(compile(validator, "<CFC whole original public validator>", "exec"), env)
    return env["validate_output"]


def height_context(height, hm, hraws, hpaths):
    owner = height["owner"]
    if sha(height["manifest_raw"]) != H96_RESUME_MANIFEST_SHA:
        return owner.admit(hm,hraws,hpaths)
    old, parent = owner.check_parent(hraws)
    actual = height["actual"]
    require(hm["resume"] == actual["resume"] == owner.RECEIPT
            and hm["problem_id"] == owner.PROBLEM and hm["historical_inputs"] == old["historical_inputs"]
            and actual["identity"]["run_id"] != owner.PARENT_RUN
            and actual["height_integral_prefix"]["complete_relative_cells"] == 2847
            and all(actual[key] == parent[key] for key in owner.CARRIERS)
            and all(any(all(new[k] == entry[k] for k in ("path","sha256","bytes","git_blob_sha"))
                        for new in hm["files"]) for entry in old["files"]),
            "the same complete original closure, cumulative height, and authentic all96 carrier lineage")
    path = hpaths[hm["roles"]["H96_original_science"]]
    original = owner.read_source(path, owner.ORIGINAL_SOURCE_SHA, "_CFC_whole_original_height_definition")
    return original.admit(old,hraws,hpaths)


def completed_parent(root, descriptor):
    """Validate a whole regular public-worker parent and its execution."""
    manifest_raw, actual_raw, execution_raw = (checked(root, descriptor[key])
                                               for key in ("manifest", "actual", "execution"))
    manifest, actual, execution = map(parse, (manifest_raw,actual_raw,execution_raw))
    specs, contents, paths = closure(root, manifest)
    worker = load(paths["worker"], "_CFC_whole_parent_validator_"+descriptor["actual"]["sha256"][:12])
    environment = {"require":require, "parse":parse, "manifest":manifest, "by_role":specs,
        "op":manifest["operation"], "args":SimpleNamespace(manifest_sha=sha(manifest_raw)),
        "run":execution["run_id"], "attempt":execution["run_attempt"], "snapshots":paths}
    owner = load(paths["science"], "_CFC_whole_parent_owner_"+descriptor["actual"]["sha256"][:12])
    validator = original_public_validator(root,worker,owner,environment)
    require(validator(actual_raw) == actual
            and actual["complete"] is actual["proved"] is execution["complete"] is True
            and actual["actual_returncode"] == execution["actual_child_returncode"] == 0
            and actual["failure"] is execution["failure"] is None
            and execution["manifest_sha256"] == sha(manifest_raw)
            and actual["completed_targets"] == manifest["target_order"]
            and actual["saved_record_count"] == len(manifest["target_order"])
            and actual["old_scientific_target_calls"] == execution["old_completed_targets_recomputed"] == 0,
            "one complete genuine original target group, no prefix")
    spec = descriptor["actual"]
    require([item for item in execution["scientific_files"] if item["path"] == spec["path"]] == [
        {key:spec[key] for key in ("path","bytes","sha256")}], "the successful parent saved its entire actual")
    return {"manifest":manifest,"actual":actual,"execution":execution,"owner":owner,
        "specs":specs,"contents":contents,"paths":paths,"manifest_raw":manifest_raw}


def admit(root, raw_manifest, manifest_sha, rows_index):
    root = Path(root)
    require(0 < len(raw_manifest) < 100000 and sha(raw_manifest) == manifest_sha,
            "one full concrete CFC manifest")
    manifest = parse(raw_manifest)
    require(manifest["repository"] == REPO and manifest["kind"] == MANIFEST_KIND
            and manifest["scientific_kind"] == KIND and manifest["parameters"] == PARAMETERS
            and manifest["runtime"] == RUNTIME, "the complete CFC definition")
    own = {item["role"]:item for item in manifest["files"]}
    own_raw = {role:checked(root,spec) for role,spec in own.items()}
    require(own["science"]["path"] == SOURCE and sha(Path(__file__).read_bytes()) == own["science"]["sha256"],
            "the exact whole actual new owner")
    math = load(root/own["math"]["path"], "_CFC_complete_new_math")
    carriers = load(root/own["carriers"]["path"], "_CFC_complete_new_carriers")
    require(math.TARGETS == manifest["target_order"] and len(math.TARGETS) == 10,
            "all new original96 natural targets")
    parents = manifest["parents"]
    sc_spec = parents["SC"]
    sm_raw = checked(root,sc_spec["manifest"]); sm = parse(sm_raw)
    ss, sr, sp = closure(root,sm)
    so = load(sp["science"], "_CFC_whole_SC_actual_owner")
    # Its unchanged preflight requires every original TC row and carrier
    # input, and accepts the complete TP 58/224/32 contract directly.
    sc = so.preflight(SimpleNamespace(input_root=str(root), manifest=str(root/sc_spec["manifest"]["path"]),
        manifest_sha=sha(sm_raw), rows_index=str(rows_index)))
    se, state = (parse(checked(root,sc_spec[key])) for key in ("execution","state"))
    require(state["complete"] is se["complete"] is True and state["failure"] is se["failure"] is None
            and state["actual_returncode"] == se["actual_child_returncode"] == 0
            and state["manifest_sha256"] == se["manifest_sha256"] == sha(sm_raw)
            and state["completed_targets"] == se["completed_natural_targets"] == so.TARGETS
            and state["old_completed_targets_recomputed"] == se["old_completed_targets_recomputed"] == 0,
            "the actual complete SC and all its original full TC/positive/negative inputs")
    for role,name in (("columns","columns"),("physical","physical_primitive96"),("incoming","declared_incoming_cosine96")):
        spec = sc_spec[role]; raw = checked(root,spec); value = parse(raw)
        so.validate_result(value,name,sha(sm_raw),state["whole_input_identity"])
        require([item for item in se["scientific_files"] if item["path"] == spec["path"]] == [
            {key:spec[key] for key in ("path","bytes","sha256")}], "whole original SC natural object")
        sc[role+"_actual"] = value
    require(sc["columns_actual"]["original_received_gains"] == sc["receiver_records"],
            "the exact fixed CR/CO/C2 coefficients used in the SC whole D_j formula")
    sc["execution"],sc["actual_state"] = se,state
    dcp = completed_parent(root,parents["DCP"])
    dc = dcp["owner"].admit_complete_inputs(dcp["contents"],dcp["specs"],dcp["manifest"],dcp["paths"])
    dc["completed_actual"] = dcp["actual"]
    require(own["ASQ18_math"]["sha256"] == ASQ18_MATH_SHA and own["ASQ18_math"]["path"] == ASQ18_MATH
            and own["ASQ18_proof"]["path"] == ASQ18_PROOF and own["ASQ20_proof"]["path"] == ASQ20_PROOF, "the exact ASQ18 finite and global CFC slots")
    receiver = load(root/ASQ18_MATH,"_CFC_whole_signed_ASQ18_receiver")
    slots = receiver.admit(root,own_raw["ASQ18_proof"],dcp)
    height = completed_parent(root,parents["H96"])
    hm = height["manifest"]
    hraws = {item["path"]:height["contents"][item["role"]] for item in hm["files"]+hm["historical_inputs"]}
    hpaths = {item["path"]:height["paths"][item["role"]] for item in hm["files"]+hm["historical_inputs"]}
    hc = height_context(height,hm,hraws,hpaths)
    require(hc["TC_state"]["proposal"] == sc["TC"]["state"]["proposal"]
            and hc["NP"] == dc["BFP_context"]["BNC"]["admitted"]["parents"]["NP"]["actual"]
            and height["actual"]["selected_member_identity"] == hc["P96"]["selected_member_identity"]
            and hc["P96"]["necessary_original_trial_receipts"]["complete_original_arrays"]
                == sc["TC"]["state"]["proposal"]["complete_endpoint_arrays"],
            "AP96/H96 and every true PDE error use the identical original96 columns")
    pwa=completed_parent(root,parents["PWA96"])
    pm=pwa["manifest"]
    praws={item["path"]:pwa["contents"][item["role"]] for item in pm["files"]}
    pc=pwa["owner"].admit(pm,praws)
    require(pc["H96"]==height["actual"] and pc["P96"]==hc["P96"]
        and pwa["actual"]["complete_original_TC_arrays"]==sc["TC"]["state"]["proposal"]["complete_endpoint_arrays"]
        and pwa["actual"]["selected_member_identity"]==height["actual"]["selected_member_identity"],
        "the whole sharper PWA row and shared-rho receiver use these exact same original96 columns")
    require(not any(name in sys.modules for name in ("numpy","flint","scipy")),
            "whole original input admission finishes before numerical import")
    return {"manifest":manifest,"SC":sc,"DCP":dc,"DCP_parent":dcp,"height":height,
        "height_context":hc,"PWA96":pwa,"math":math,"carriers":carriers,"own_inputs":own_raw,
        "ASQ18_math":receiver,"ASQ18_slots":slots}


class PrivateStore:
    """Every full array is read back; the public state receives only a chain."""
    def __init__(self, directory, c, api, state, save):
        self.path,self.c,self.api,self.state,self.save = Path(directory),c,api,state,save
        self.path.mkdir(parents=True,exist_ok=True)
        self.receipts,self.bytes,self.chain = {},0,sha(b"CFC complete private objects v1")

    def receipt(self,name,path,shape=None):
        require(name not in self.receipts,"one new complete private scientific object")
        digest=hashlib.sha256()
        with path.open("rb") as stream:
            for block in iter(lambda:stream.read(1<<20),b""):digest.update(block)
        item={"name":name,"bytes":path.stat().st_size,"sha256":digest.hexdigest()}
        if shape is not None:item["shape"]=list(shape)
        self.bytes+=item["bytes"]
        require(self.bytes<=PARAMETERS["private_disk_limit_bytes"],"retain the whole private disk budget")
        self.chain=sha(bytes.fromhex(self.chain)+encode(item));self.receipts[name]=item
        self.state["private_objects"]={"complete_count":len(self.receipts),"bytes":self.bytes,
            "whole_ordered_receipt_chain_sha256":self.chain,"last_complete_object":item}
        self.save();return item

    def real(self,name,value,exact=False):
        require(re.fullmatch(r"[A-Za-z0-9_]+",name),"one safe complete array name")
        c=self.c;c.finite(value)
        if exact:require(c.np.array_equal(value.lo,value.hi),"every coordinate is an exact dyadic")
        path=self.path/(name+".npy");require(not path.exists(),"no completed private object overwritten")
        with path.open("wb") as stream:c.np.save(stream,c.np.stack((value.lo,value.hi)),allow_pickle=False)
        with path.open("rb") as stream:formal=c.np.load(stream,allow_pickle=False)
        require(formal.dtype==c.np.dtype("float64") and formal.shape==(2,)+value.lo.shape
            and c.np.array_equal(formal[0],value.lo) and c.np.array_equal(formal[1],value.hi),
            "all complete directed endpoints survive whole readback")
        self.receipt(name,path,value.lo.shape);return c.Box(formal[0],formal[1])

    def complex(self,name,value,exact=False):
        return self.c.CBox(self.real(name+"_real",value.real,exact),self.real(name+"_imag",value.imag,exact))

    def json(self,name,value):
        raw=encode(value);path=self.path/(name+".json")
        require(not path.exists(),"one fresh full JSON object")
        atomic(path,raw);self.receipt(name,path);return parse(path.read_bytes())

    def real_vector(self,name,values):
        body=self.json(name,{"complete_count":len(values),"all_balls":[v.str(110) for v in values]})
        formal=[self.api.arb(v) for v in body["all_balls"]]
        require(all(a.contains(b) for a,b in zip(formal,values)),"every whole scalar survives serialization")
        return formal

    def complex_vector(self,name,values):
        body=self.json(name,{"complete_count":len(values),"all_pairs":[[v.real.str(110),v.imag.str(110)] for v in values]})
        formal=[self.api.acb(self.api.arb(a),self.api.arb(b)) for a,b in body["all_pairs"]]
        require(all(a.real.contains(b.real) and a.imag.contains(b.imag) for a,b in zip(formal,values)),
                "every signed complex coefficient survives serialization")
        return formal

    def checkpoint(self,stage,metadata,**values):
        suffix="_%04d"%metadata["complete_modes"]
        first=len(self.receipts)
        for name,value in values.items():
            stem=stage+suffix+"_"+name
            if hasattr(value,"real") and hasattr(value.real,"lo"):self.complex(stem,value)
            else:self.real(stem,value)
        self.state["whole_batch_prefix"]={"stage":stage,**metadata,
            "new_complete_private_objects":len(self.receipts)-first,
            "whole_private_receipt_chain_sha256":self.chain,"complete_target":False}
        self.save()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ("manifest","input-root","rows-index","output"):
        parser.add_argument("--"+name,type=Path,required=True)
    parser.add_argument("--manifest-sha",required=True);parser.add_argument("--checkout",required=True)
    parser.add_argument("--preflight-only",action="store_true")
    parser.add_argument("--carrier-mode",choices=("GRID",))
    parser.add_argument("--carrier-directory",type=Path);parser.add_argument("--carrier-receipt",type=Path)
    args=parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==REPO
        and os.environ.get("GITHUB_RUN_ATTEMPT")=="1","one first actual public CFC job")
    data=admit(args.input_root,args.manifest.read_bytes(),args.manifest_sha,args.rows_index)
    if args.preflight_only:
        print(encode({"complete":True,"parent_groups":["SC","DCP","H96","PWA96"],"old_targets_called":0}).decode());return 0
    dcp=data["DCP"];bfp=dcp["BFP_context"];bnc=bfp["BNC"]["admitted"];uc=bfp["UACT"]["admitted"]
    if args.carrier_mode:
        bfp["BNC"]["owner"].carrier_child(args,bnc);return 0
    require(not args.output.exists(),"preserve every previous actual result or failed prefix")
    private=args.output.parent/"private-complete-TC96-columns";private.mkdir()
    began=time.monotonic()
    state={"kind":KIND,"manifest_sha256":args.manifest_sha,"run_id":os.environ["GITHUB_RUN_ID"],
        "run_attempt":"1","checkout":args.checkout,"parameters":PARAMETERS,"runtime":None,
        "complete":False,"proved":False,"actual_returncode":None,"failure":None,
        "stage":"all_complete_original_parents_admitted","progress":{},"wall_seconds":0,
        "completed_targets":[],"new_records":{},"private_objects":None,"whole_batch_prefix":None,
        "carrier_restoration":{},"result":None,"old_scientific_targets_called":0,"new_arrays_published":0}
    require(sorted(state)==SCI_FIELDS==data["manifest"]["allowed_scientific_fields"],"whole CFC scientific field contract")
    def save():
        state["wall_seconds"]=time.monotonic()-began
        raw=encode(state);require(len(raw)<PARAMETERS["public_bytes"],"whole small CFC actual")
        atomic(args.output,raw)
    def progress(stage,details):
        state["stage"],state["progress"]=stage,details;save()
        require(state["wall_seconds"]<PARAMETERS["maximum_scientific_wall_seconds"],"whole CFC prefix saved before wall budget")
        print(encode({"stage":stage,**details}).decode(),end="",flush=True)
    save()
    try:
        grid_dir,grid_receipt=private/"same-original-AS",private/"same-original-AS-receipt.json"
        command=[sys.executable,str(Path(__file__).resolve()),"--manifest",str(args.manifest.resolve()),
            "--manifest-sha",args.manifest_sha,"--input-root",str(args.input_root.resolve()),
            "--rows-index",str(args.rows_index.resolve()),"--output",str(args.output.resolve()),
            "--checkout",args.checkout,"--carrier-mode","GRID","--carrier-directory",str(grid_dir.resolve()),
            "--carrier-receipt",str(grid_receipt.resolve())]
        env=dict(os.environ);env.pop("OPENBLAS_CORETYPE",None)
        with (private/"original-AS.log").open("wb") as stream:
            child=subprocess.Popen(command,stdout=stream,stderr=subprocess.STDOUT,env=env)
            last=0.0
            try:
                while child.poll() is None:
                    if time.monotonic()-last>45:progress("necessary_original_AS_grid_only",{});last=time.monotonic()
                    time.sleep(1)
            finally:
                if child.poll() is None:
                    child.terminate()
                    try:child.wait(timeout=20)
                    except subprocess.TimeoutExpired:child.kill();child.wait()
        receipt=parse(grid_receipt.read_bytes());state["carrier_restoration"]["AS"]=receipt
        require(child.returncode==0 and receipt["complete"] is True and receipt["failure"] is None,
                "one whole genuine original AS grid restoration")
        import numpy as np
        import flint
        from importlib.metadata import version
        runtime={"python":platform.python_version(),"packages":{name:version(name) for name in RUNTIME["packages"]}}
        require(runtime==RUNTIME and os.environ.get("OPENBLAS_CORETYPE")=="Haswell","the whole original fixed runtime")
        state["runtime"]=runtime;flint.ctx.prec,flint.ctx.cap=320,9
        ot=uc["owner"];api=ot.directed_api(flint)
        api.midpoint_real=lambda v:v.mid();api.midpoint_complex=lambda v:api.acb(v.real.mid(),v.imag.mid())
        c,coefficients,means,receipt=data["carriers"].restore_TC_waist(np,flint,args.input_root,private/"same-TC",data["SC"],progress)
        state["carrier_restoration"]["TC"]=receipt
        choose_ir=bfp["original_OT"]["IR"]["owner"].choose_complete_dyadic_trial_bytes
        common=data["carriers"].restore_compound_inputs(np,flint,api,dcp,
            (grid_dir/"complete-original-AS-grid.json").read_bytes(),private,progress,atomic)
        state["carrier_restoration"]["compound"]=common["whole_receipts"]
        io=PrivateStore(private/"new-complete-carriers",c,api,state,save)
        coefficients=io.complex("complete_TC96_physical_source",coefficients)
        means=io.real("complete_TC96_original_stored_means",means)
        def ball(value):return ot.whole_ball(api,value)
        def up(value):return ot.whole_upper(api,value)
        sc=data["SC"];ba=dcp["BFP_actual"];da=data["DCP_parent"]["actual"]
        bt=dcp["BFP_manifest"]["target_order"];dt=data["DCP_parent"]["manifest"]["target_order"]
        copied=ba["copied_complete_input_records"];dcopied=da["copied_complete_input_records"]
        bounds={key:up(copied[key]) for key in ("EH","G0","G1","H1","w_Linf","w_L2")}
        bounds.update(m=ball(copied["m"]),BH=up(sc["receiver_records"]["BH"]),
            CR=ball(sc["receiver_records"]["CR"]),B_inverse=up(ba["new_records"][bt[1]]),
            Theta_trial_norm=up(ba["new_records"][bt[15]]),
            Theta_global_error=data["ASQ18_math"].whole_global(api,data["ASQ18_slots"]),
            phat_derivative_perturbation=up(da["new_records"][dt[0]]),
            IR_H=up(dcopied["IR_H"]),IR_L2=up(dcopied["IR_L2"]),Ep=up(dcopied["inverse_lift_error"]),
            UACT_inverse_Linf_product=up(dcopied["whole_UACT_inverse_error_Linf_product"]),
            UACT_inverse_L2_product=up(dcopied["whole_UACT_inverse_error_L2_product"]))
        phase=data["height_context"]["P96"];height=data["PWA96"]["actual"]
        pt=data["height_context"]["P96_manifest"]["target_order"];ht=data["PWA96"]["manifest"]["target_order"]
        rows={"phase":{"centers":phase["new_records"][pt[4]]["exact_dyadic_centres"],
                       "joint_radius":up(phase["new_records"][pt[5]])}}
        for name,index in (("height",0),("reduced_phase",3)):
            rows[name]={"centers":height["new_records"][ht[index]]["exact_dyadic_centres"],
                "joint_radius":api.arb(height["new_records"][ht[index+1]]["balls"][0]).upper()}
        pparameters=data["PWA96"]["manifest"]["parameters"]
        receivers={"phase":[api.rational(value) for value in pparameters["complete_PRN_negative_receiver4"]],
            "height":[api.rational(value) for value in pparameters["complete_PWA_height_negative_receiver4"]],
            "reduced_phase":[api.arb(value).upper() for value in height["new_records"][ht[5]]["balls"]]}
        bundle={**common,"c":c,"api":api,"BFP_math":bfp["pure"],"DCP_math":dcp["pure"],
            "bounds":bounds,"physical_coefficients":coefficients,"stored_means":means,"saved_rows":rows,
            "row_receivers":receivers,
            "waist_errors":[up(sc["columns_actual"]["complete_column_error_records"]["column_%03d"%j]) for j in range(1,97)],
            "root_errors":[up(sc["columns_actual"]["complete_root_error_records"]["column_%03d"%j]
                              ["complete_physical_root_error_upper"]) for j in range(1,97)],
            "waist_trial_norms":[up(sc["TC"]["matrix"]["complete_waist_trial_norms"]["column_%03d"%j]) for j in range(1,97)],
            "negative_root":[up(sc["TC"]["negative"]["complete_source_records"]["column_%03d"%j]["negative_root"]) for j in range(1,97)],
            "negative_strict":[up(sc["TC"]["negative"]["complete_source_records"]["column_%03d"%j]["negative_strict"]) for j in range(1,97)]}
        pure=data["math"]
        def scalar(v):
            point=v.upper();text=point.str(60);require(api.arb(text).contains(point),"full directed scalar saved")
            return {"ball":text,"bound":"upper"}
        def scientific(value):
            if isinstance(value,dict):return {key:scientific(v) for key,v in value.items()}
            if isinstance(value,list):return [scientific(v) for v in value]
            if isinstance(value,(str,int,bool)) or value is None:return value
            return value.str(110)
        def publish(index,record):
            require(index==len(state["completed_targets"]),"new whole natural target order")
            name=pure.TARGETS[index];state["new_records"][name]=record;state["completed_targets"].append(name);save()
            require(parse(args.output.read_bytes())["new_records"][name]==record,"the entire natural conclusion read back")
        forward=pure.complete_batch_forward(bundle,io,progress)
        io.json("complete_TC96_forward_column_error_ledger",scientific(forward["complete_column_records"]))
        publish(0,{"complete_count":96,"bounds":[scalar(v) for v in forward["finite_residuals"]]})
        publish(1,{"complete_count":96,"bounds":[scalar(v) for v in forward["errors"]],
                   "finite_trial_modes":512,"true_tail_set_to_zero":False})
        publish(2,{"whole_joint_L2_error":scalar(forward["joint"]),"all96_squared_column_errors_used":True})
        row=pure.complete_scalar_rows(bundle,io)
        publish(3,{"stored_rows":2,"physical_mean_rank":1,"complete_columns":96,
            "whole_joint_error":scalar(row["means"]["whole_joint_error"]),"two_free_mean_unknowns_claimed":False,
            "carrier":io.receipts["complete_TC96_stored_mean_pair_centers"]})
        for index,name in ((4,"phase"),(5,"height"),(6,"reduced_phase")):
            publish(index,{"complete_count":96,"whole_joint_error":scalar(row[name]["whole_joint_error"]),
                "source_row_carrier":io.receipts["complete_TC96_"+name+"_exact_centers"],
                "all96_PDE_correction_bounds":[scalar(v) for v in row[name]["new_PDE_correction_bounds"]],
                "independent_Yb_Kb_and_raw_chart_ports_retained":True})
        theta=pure.complete_batch_Theta(bundle,forward,io,progress)
        io.json("complete_TC96_Theta_column_error_ledger",scientific(theta["complete_column_records"]))
        for index,key in ((7,"finite_joint"),(8,"true_joint")):
            publish(index,{"rows":96,"columns":96,"signed_entry_count":9216,
                "whole_joint_error":scalar(theta[key]),"whole_signed_center_carrier":io.receipts["complete_TC96_Theta_exact_centers"],
                "same_original_model_phase_and_C_inverse":True,"complete_opposite_head_and_tail_retained":True})
        interface={"complete_original_TC_columns":96,"whole_target_modes_in_trial":512,
            "complete_infinite_target_error":scalar(forward["joint"]),
            "original_root_boundary_basis_is_identity96":True,"physical_target_basis_is_true_a":True,
            "stored_mean_pair_rank":1,"phase_and_height_rows_PDE_corrected":True,
            "original_Theta_shape":[96,2240],"original_UACT_coordinate_inverse_retained":True,
            "strict_nu_particular_is_separate_complete_BFP_DCP_input":True,
            "direct_nu_normalizer_and_boundary_columns_remain_independent":True,
            "full_nu_column_assembled":False,
            "same_PWA_phase_height_ratio_record":height["new_records"][ht[2]],
            "same_PWA_negative_receiver4":height["new_records"][ht[5]],
            "independent_PWA_world_receiver2":height["new_records"][ht[6]],
            "missing_independent_signed_blocks":["PH_inverse_PKQ","PH_inverse_PU","PH_inverse_Pg",
                "PH_inverse_Pf_for_same_rhs","complete_nonmean_chart_and_world_parameter_columns",
                "independent_physical_mean_equation_and_geometric_period_rows"],
            "physical_square_assembled":False,"full_Schur_inverse_proved":False,
            "auxiliary96_observation_matrix_promoted_to_full_square":False,"topic_completion_proved":False}
        interface["complete_ASQ18_finite_coordinate_recovery"]=data["ASQ18_math"].recovered_columns(
            api,np,data["ASQ18_slots"],theta,io.receipts["complete_TC96_Theta_exact_centers"],scalar,
            bfp["original_OT"],private,choose_ir,common["source_b"],io)
        publish(9,interface)
        state["result"]=interface;state["complete"]=state["proved"]=True;state["actual_returncode"]=0
        progress("complete_original_TC96_full_target_columns_and_rows",{"complete_targets":10})
        return 0
    except BaseException as exc:
        state["failure"]={"type":type(exc).__name__,"message":str(exc),"traceback":traceback.format_exc()[-7000:]}
        state["actual_returncode"]=1;state["complete"]=state["proved"]=False;save();raise


if __name__=="__main__":
    sys.exit(main())
