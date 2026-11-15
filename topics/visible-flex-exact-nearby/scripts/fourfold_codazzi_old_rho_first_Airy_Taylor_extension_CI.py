#!/usr/bin/env python3
"""Execute only missing old-radial Airy Taylor degrees and retain both inventories."""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,subprocess,sys,time
from pathlib import Path

PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
SOURCE=TOPIC/"scripts/fourfold_codazzi_old_rho_first_Airy_Taylor_extension.py"
NATIVE="complete-old-rho-first-Airy-Taylor-through-twelve.json.gz"
OLD_SOURCE="e4ccbf4b343623d74d089f79b6605a0601975c6ea5c1d2e113bad568fe60167d"
OLD_MANIFEST="226e5acac42026431acbd166f92d423b6292ba6f73e65f58f808647d4701f1ad"

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    path=Path(path);raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix==".gz" else raw)
def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(value,indent=2,allow_nan=False)+"\n").encode()
    if path.suffix==".gz":raw=gzip.compress(raw,mtime=0)
    temp=path.with_name(path.name+".partial");temp.write_bytes(raw);temp.replace(path)
def short(value):
    if isinstance(value,list):return [short(v) for v in value]
    if isinstance(value,dict):
        if set(value)=={"ball"}:return value["ball"]
        return {k:short(v) for k,v in value.items()}
    return value
def size(value):return len((json.dumps(value,indent=2,allow_nan=False)+"\n").encode())

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ("repo","manifest","out-dir","prepared"):
        parser.add_argument("--"+name,type=Path,required=True)
    parser.add_argument("--manifest-sha",required=True)
    parser.add_argument("--resume",type=Path);parser.add_argument("--resume-sha")
    args=parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("all new mathematics requires this public repository Actions")
    if sha(args.manifest)!=args.manifest_sha:raise ValueError("the pinned manifest changed")
    manifest=read(args.manifest)
    if manifest["public_repository"]!=PUBLIC:raise ValueError("wrong repository")
    repo,out=args.repo.resolve(),args.out_dir.resolve()
    if out.exists() and any(out.iterdir()):raise FileExistsError("preserve each original outcome")
    out.mkdir(parents=True,exist_ok=True)
    native=out/NATIVE;process=out/"process.json"
    state=dict(kind="actual_public_append_only_old_rho_Airy_Taylor_through_twelve",
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),manifest_sha256=args.manifest_sha,
        complete=False,failure=None,actual_returncode=None,
        original_successful_mathematics_recomputed=False,
        complete_strong_return_or_full_inverse_claimed=False)
    def checkpoint():
        if size(state)>60000:raise ValueError("the readable actual process exceeds60000 bytes")
        save(process,state)
    checkpoint();code=1
    try:
        for item in manifest["files"]:
            path=repo/item["path"]
            if not path.is_file() or path.stat().st_size!=item["bytes"] or sha(path)!=item["sha256"]:
                raise ValueError("an exact original input changed: "+item["path"])
        state["verified_input_file_count"]=len(manifest["files"])
        state["all_verified_input_pins_preserved_in_manifest"]=True
        expected=next(v["sha256"] for v in manifest["files"] if v["path"]==str(SOURCE))
        command=[sys.executable,"-u",str(repo/SOURCE),"--repo-root",str(repo),
            "--manifest",str(args.manifest),"--out",str(native)]
        if args.resume:
            if not args.resume_sha or sha(args.resume)!=args.resume_sha:
                raise ValueError("an exact accepted new prefix changed")
            command+=["--resume",str(args.resume)]
            state["original_prefix_native_sha256"]=args.resume_sha
        state.update(command=command,mathematical_source_sha256=expected);checkpoint()
        started=time.monotonic()
        with (out/"complete-old-rho-first-Airy-Taylor-through-twelve.stdout.log").open("wb") as stream:
            child=subprocess.Popen(command,cwd=repo,stdout=stream,stderr=subprocess.STDOUT)
            try:child.wait(timeout=2700)
            except subprocess.TimeoutExpired:
                state["actual_timeout_seconds"]=2700;child.terminate()
                try:child.wait(timeout=10)
                except subprocess.TimeoutExpired:child.kill();child.wait()
        state.update(actual_returncode=child.returncode,mathematical_wall_seconds=time.monotonic()-started)
        if native.is_file():
            doc=read(native)
            if doc.get("source_sha256")!=expected or doc.get("input_manifest_sha256")!=args.manifest_sha:
                raise ValueError("the actual new native changed its scientific identity")
            state.update(native_sha256=sha(native),native_bytes=native.stat().st_size,
                mathematical_complete=doc.get("complete"),mathematical_proved=doc.get("proved"),
                mathematical_failure=doc.get("failure"),mathematical_gates=doc.get("gates",[]))
            runtime={k:manifest["runtime"][k] for k in ("python","python_flint","numpy","scipy")}
            if doc.get("runtime")!=runtime:raise ValueError("the actual numerical runtime changed")
            if sha(repo/manifest["input_paths"]["append_contract"])!=doc.get("contract_sha256"):
                raise ValueError("the actual consumer contract changed")
            keys=("kind","runtime","algebra_sha256","original_Taylor_native_sha256",
                "original_Taylor_process_sha256","original_Taylor_source_sha256",
                "original_Taylor_manifest_sha256","higher_intrinsic_native_sha256","higher_intrinsic_process_sha256",
                "higher_intrinsic_source_sha256","complete_larger_fold_native_sha256","complete_larger_fold_process_sha256","contract_sha256",
                "background_definition_sha256","explicit_direction_definition_sha256",
                "actual_intrinsic_parameter","exact_fixed_intrinsic_parameter","exact_complex_delta_radius",
                "exact_root_interval","exact_original_physical_piece_interval","old_product_domain",
                "leading_Taylor_order","forcing_Taylor_order","first_correction_Taylor_order",
                "complete_non_circular_Fourier_algebra","physical_angle_frequency_multiplier",
                "original_target_FFT_or_high_root_stages_recomputed",
                "original_auxiliary_fold_forcing_or_domain_stages_recomputed",
                "original_completed_Taylor_stages_recomputed","new_finite_algebra_stages",
                "reused_finite_algebra_stages","new_supporting_stages","reused_supporting_stages",
                "new_fold_degrees","new_forcing_degrees","new_first_correction_degrees",
                "new_Fourier_norm_rows","original_complete_stage_count",
                "complete_branch_identity","complete_Fourier_coefficient_support",
                "old_circle_I_J_or_independent_even_mean_budget_paid",
                "complete_strong_return_or_cutoff97_inverse_claimed",
                "all_original_physical_seams_and_independent_mean_equations_retained",
                "last_attempted_stage","preserved_actual_extension_prefix","original_prefix_audit",
                "accepted_original_natural_stage_count","accepted_new_natural_stage_count",
                "all_original_and_new_complete_Fourier_arrays_retained","all_original_and_new_natural_prefix_files_verified")
            state["scientific_metadata"]={k:short(doc[k]) for k in keys if k in doc}
            for key,value in doc.items():
                if (key.startswith(("new_","reused_","original_")) and
                    isinstance(value,(str,bool,int,float,type(None)))):
                    state["scientific_metadata"][key]=value
            originals=doc.get("original_stages",{});new=doc.get("stages",{})
            if set(originals)&set(new):raise ValueError("a new stage replaces an accepted original name")
            old_input=read(repo/manifest["input_paths"]["old_native"])
            expected_old=old_input["stages"]
            if any(name not in expected_old or entry!=expected_old[name] for name,entry in originals.items()):
                raise ValueError("an accepted original stage receipt was changed")
            inventories={"original":[],"new":[]};seen=set()
            for role,entries in (("original",originals),("new",new)):
                for name,entry in entries.items():
                    relative=Path(entry["file"])
                    if relative.is_absolute() or ".." in relative.parts or relative.parts[0]!="stages":
                        raise ValueError("a natural stage leaves its actual output directory")
                    if str(relative) in seen:raise ValueError("two stages overwrite the same natural file")
                    seen.add(str(relative));path=native.parent/relative
                    if not path.is_file() or path.stat().st_size!=entry["bytes"] or sha(path)!=entry["sha256"]:
                        raise ValueError("a complete natural stage changed bytes: "+name)
                    value=read(path)
                    names=[value[k] for k in ("stage","name") if k in value]
                    want_source=OLD_SOURCE if role=="original" else expected
                    want_manifest=OLD_MANIFEST if role=="original" else args.manifest_sha
                    if (not names or any(v!=name for v in names) or value.get("complete") is not True
                        or value.get("source_sha256")!=want_source
                        or value.get("input_manifest_sha256")!=want_manifest):
                        raise ValueError("a complete natural stage changed scientific identity: "+name)
                    inventories[role].append(dict(name=name,**entry))
            inventory=out/"complete-natural-stage-inventory.json.gz";save(inventory,inventories)
            state["complete_stage_inventory"]=dict(file=inventory.name,bytes=inventory.stat().st_size,sha256=sha(inventory),
                original_count=len(inventories["original"]),new_count=len(inventories["new"]),
                original_and_new_bytes_separately_verified=True)
            state["original75_stage_bytes_unchanged"]=len(originals)==75 and originals==expected_old
            state["all_available_natural_stage_files_verified"]=True
            state["complete_new_stage_files"]={name:dict(bytes=entry["bytes"],sha256=entry["sha256"])
                for name,entry in new.items()}
            reports=[]
            for row in doc.get("first_correction_derivative_budgets",[]):
                table={k:{kind:short(v[kind]) for kind in ("strip_sup","Wiener")}
                    for k,v in row["first_amplitude_budgets"].items()}
                reports.append(dict(exact_output_phi_width=row["exact_output_phi_width"],
                    first_amplitude_budgets=table,
                    complete_normalized_local_L0_w1_sup_bounds=short(row["complete_normalized_local_L0_w1_sup_bounds"]),
                    unnormalized_local_operator_sup_bounds=short(row["unnormalized_local_operator_sup_bounds"]),
                    complete_finite_and_infinite_parts_retained_in_native=True))
            state["new_degree_twelve_derivative_budgets"]=reports
            state["complete_all_original_and_new_arrays_and_scalar_records_retained"]=True
        good=(state["actual_returncode"]==0 and state.get("mathematical_complete") is True
            and state.get("mathematical_proved") is True and state.get("mathematical_failure") is None
            and state.get("mathematical_gates") and all(g["passed"] for g in state["mathematical_gates"])
            and state.get("original75_stage_bytes_unchanged") is True
            and state.get("all_available_natural_stage_files_verified") is True
            and len(state.get("new_degree_twelve_derivative_budgets",[]))==3)
        state["complete"]=bool(good);code=0 if good else 1
    except BaseException as error:
        state["failure"]=dict(type=type(error).__name__,message=str(error));code=1
    finally:
        if size(state)>60000:
            full=out/"complete-process-before-readable-summary.json"
            save(full,state)
            state["original_full_process"]=dict(file=full.name,bytes=full.stat().st_size,sha256=sha(full))
            state.pop("complete_new_stage_files",None)
            state["all_new_receipts_preserved_in_complete_inventory"]=True
        checkpoint()
        print(json.dumps(dict(complete=state["complete"],actual_returncode=state["actual_returncode"],
            failure=state["failure"],process_sha256=sha(process)),allow_nan=False),flush=True)
    raise SystemExit(code)
if __name__=="__main__":main()
