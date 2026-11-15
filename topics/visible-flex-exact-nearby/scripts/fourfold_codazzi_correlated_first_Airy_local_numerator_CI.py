#!/usr/bin/env python3
"""Run the exact new correlated local numerator and preserve every complete stage."""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,subprocess,sys,time
from pathlib import Path

PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
SOURCE=TOPIC/"scripts/fourfold_codazzi_correlated_first_Airy_local_numerator.py"
NATIVE="correlated-first-Airy-local-numerator.json.gz"
EXTENSION_NATIVE="758a2901d194e9d54ec10bb5004014ee34a972c35367589fd5c86afce3f30c9f"
FOLD_NATIVE="84e2bd1b7637299e94428b22cc19aba290d0b661f9dbe18dae918bf752f10077"

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
    state=dict(kind="actual_public_correlated_first_Airy_local_numerator",
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
        with (out/"correlated-first-Airy-local-numerator.stdout.log").open("wb") as stream:
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
            if doc.get("contract_sha256") is not None and sha(repo/manifest["input_paths"]["contract"])!=doc["contract_sha256"]:
                raise ValueError("the actual consumer contract changed")
            keys=("kind","runtime","algebra_sha256","original_extension_native_sha256",
                "original_extension_process_sha256","original_extension_source_sha256",
                "original_extension_manifest_sha256","original_larger_fold_native_sha256",
                "original_larger_fold_process_sha256","contract_sha256",
                "background_definition_sha256","explicit_direction_definition_sha256",
                "fixed_intrinsic_parameter","exact_fixed_intrinsic_parameter","exact_complex_delta_radius",
                "exact_root_interval","exact_original_physical_piece_interval","old_product_domain",
                "residual_Taylor_order","completed_first_correction_Taylor_order",
                "maximum_output_angular_derivative","physical_angle_frequency_multiplier",
                "complete_branch_identity","original_complete_branch_identity",
                "original_complete_amplitude_bounds","original_auxiliary_case_payload_sha256",
                "complete_mean_retained_before_any_projection","exact_old_D_order_retained",
                "principal_mu_uses_B_plus","no_principal_factor_division_in_actual_local_numerator",
                "all_original_physical_seams_and_independent_mean_equations_retained",
                "reconstructed_JP_Airy_operator_and_radial_integral_paid",
                "old_circle_nonlocal_and_independent_even_mean_terms_paid",
                "complete_strong_return_or_cutoff97_inverse_claimed",
                "accepted_new_natural_stage_count","all_original_selected_and_new_complete_Fourier_arrays_retained",
                "preserved_actual_prefix")
            state["scientific_metadata"]={k:short(doc[k]) for k in keys if k in doc}
            for key,value in doc.items():
                if (key.startswith(("new_","reused_","original_")) and
                    isinstance(value,(str,bool,int,float,type(None)))):
                    state["scientific_metadata"][key]=value
            originals=doc.get("original_selected_natural_stage_receipts",{})
            extension=read(repo/manifest["input_paths"]["extension_native"])
            expected_originals=dict(extension["original_stages"]);expected_originals.update(extension["stages"])
            pins={item["path"]:item for item in manifest["files"]}
            for name,entry in originals.items():
                if name not in expected_originals:
                    raise ValueError("an accepted original selected stage name changed")
                old=expected_originals[name]
                if any(entry.get(k)!=old[k] for k in ("file","bytes","sha256")):
                    raise ValueError("an accepted original selected stage receipt changed")
                path=(repo/manifest["input_paths"]["extension_native"]).parent/old["file"]
                relative=str(path.relative_to(repo))
                if relative not in pins or sha(path)!=old["sha256"] or path.stat().st_size!=old["bytes"]:
                    raise ValueError("an accepted input stage changed original complete bytes")
            state["original26_selected_stage_bytes_unchanged"]=(len(originals)==26)
            new=doc.get("stages",{});inventory=[];seen=set()
            for name,entry in new.items():
                relative=Path(entry["file"])
                if relative.is_absolute() or ".." in relative.parts or relative.parts[0]!="stages":
                    raise ValueError("a new natural stage leaves its actual output directory")
                if str(relative) in seen:raise ValueError("two stages overwrite the same natural file")
                seen.add(str(relative));path=native.parent/relative
                if not path.is_file() or path.stat().st_size!=entry["bytes"] or sha(path)!=entry["sha256"]:
                    raise ValueError("a complete new natural stage changed bytes: "+name)
                value=read(path)
                if (value.get("stage")!=name or value.get("complete") is not True
                    or value.get("source_sha256")!=expected
                    or value.get("input_manifest_sha256")!=args.manifest_sha
                    or value.get("runtime")!=runtime
                    or value.get("original_extension_native_sha256")!=EXTENSION_NATIVE
                    or value.get("original_larger_fold_native_sha256")!=FOLD_NATIVE
                    or value.get("algebra_sha256")!=doc["algebra_sha256"]):
                    raise ValueError("a complete new stage changed scientific identity: "+name)
                inventory.append(dict(name=name,**entry))
            ipath=out/"complete-natural-stage-inventory.json.gz"
            save(ipath,dict(original_selected=originals,new=inventory))
            state["complete_stage_inventory"]=dict(file=ipath.name,bytes=ipath.stat().st_size,sha256=sha(ipath),
                original_selected_count=len(originals),new_count=len(inventory),
                every_original_selected_and_new_stage_byte_identity_verified=True)
            state["all_available_natural_stage_files_verified"]=True
            state["complete_Fourier_coefficient_support_and_mean"]=short(
                doc.get("complete_Fourier_coefficient_support_and_mean",[]))
            reports=[]
            for row in doc.get("complete_correlated_Nraw_budgets",[]):
                part={}
                for norm,components in row["complete_finite_and_tail_parts"].items():
                    part[norm]={}
                    for name,derivatives in components.items():
                        part[norm][name]={k:{field:short(value[field]) for field in
                            ("complete_correlated_finite_Fourier_prefix",
                             "complete_infinite_radial_and_angular_tail")}
                            for k,value in derivatives.items()}
                reports.append(dict(exact_output_phi_width=row["exact_output_phi_width"],
                    exact_rho_Cauchy_radius=row["exact_rho_Cauchy_radius"],
                    exact_phi_Cauchy_width=row["exact_phi_Cauchy_width"],
                    exact_physical_rho_cover_radius=row["exact_physical_rho_cover_radius"],
                    residual_Taylor_order=row["residual_Taylor_order"],
                    complete_Nraw_derivative_budgets=short(row["complete_Nraw_derivative_budgets"]),
                    complete_finite_and_infinite_parts=part,
                    original_triangle_unnormalized_q0_bound=short(row["original_triangle_unnormalized_q0_bound"]),
                    independent_minimum_complete_q0_strip_bound=short(
                        row["independent_minimum_complete_q0_strip_bound"]),
                    new_correlated_q0_bound_no_larger_than_original=row[
                        "new_correlated_q0_bound_no_larger_than_original"],
                    complete_Fourier_arrays_and_all_tail_terms_preserved_in_native=True))
            state["new_complete_correlated_Nraw_budgets"]=reports
            state["all_selected_original_and_new_complete_arrays_and_scalar_records_retained"]=True
        good=(state["actual_returncode"]==0 and state.get("mathematical_complete") is True
            and state.get("mathematical_proved") is True and state.get("mathematical_failure") is None
            and state.get("mathematical_gates") and all(g["passed"] for g in state["mathematical_gates"])
            and state.get("original26_selected_stage_bytes_unchanged") is True
            and state.get("all_available_natural_stage_files_verified") is True
            and state.get("complete_stage_inventory",{}).get("new_count")==60
            and len(state.get("new_complete_correlated_Nraw_budgets",[]))==3)
        state["complete"]=bool(good);code=0 if good else 1
    except BaseException as error:
        state["failure"]=dict(type=type(error).__name__,message=str(error));code=1
    finally:
        if size(state)>60000:
            full=out/"complete-process-before-readable-summary.json";save(full,state)
            state["original_full_process"]=dict(file=full.name,bytes=full.stat().st_size,sha256=sha(full))
            state.pop("complete_Fourier_coefficient_support_and_mean",None)
            state["all_full_Fourier_support_and_mean_records_remain_in_native"]=True
        checkpoint()
        print(json.dumps(dict(complete=state["complete"],actual_returncode=state["actual_returncode"],
            failure=state["failure"],process_sha256=sha(process)),allow_nan=False),flush=True)
    raise SystemExit(code)
if __name__=="__main__":main()
