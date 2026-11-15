#!/usr/bin/env python3
"""Execute and retain only missing true-root intrinsic derivative arithmetic."""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,subprocess,sys,time
from pathlib import Path

PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
SOURCE=TOPIC/"scripts/fourfold_codazzi_true_root_missing_intrinsic_jets.py"
NATIVE="true-root-missing-intrinsic-jets.json.gz"

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    path=Path(path);raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix==".gz" else raw)
def payload_sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def short(value):
    if isinstance(value,list):return [short(v) for v in value]
    if isinstance(value,dict):
        if "ball" in value:return value["ball"]
        return {k:short(v) for k,v in value.items()}
    return value

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ("repo","manifest","out-dir","prepared"):
        parser.add_argument("--"+name,type=Path,required=True)
    parser.add_argument("--manifest-sha",required=True)
    parser.add_argument("--resume",type=Path);parser.add_argument("--resume-sha")
    args=parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("the authorized public Actions numerical environment is required")
    if sha(args.manifest)!=args.manifest_sha:raise ValueError("the independently pinned manifest changed")
    manifest=read(args.manifest)
    if manifest["public_repository"]!=PUBLIC:raise ValueError("another public repository was supplied")
    repo,out=args.repo.resolve(),args.out_dir.resolve()
    if out.exists() and any(out.iterdir()):raise FileExistsError("preserve every actual outcome")
    out.mkdir(parents=True,exist_ok=True)
    native=out/NATIVE;process=out/"process.json"
    state=dict(kind="actual_public_missing_true_root_intrinsic_jet_execution",
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),manifest_sha256=args.manifest_sha,
        complete=False,failure=None,actual_returncode=None,
        original_successful_mathematics_recomputed=False,
        higher_Airy_Taylor_or_full_inverse_claimed=False)
    def checkpoint():
        raw=(json.dumps(state,indent=2,allow_nan=False)+"\n").encode()
        if len(raw)>60000:raise ValueError("the readable actual process exceeds60000 bytes")
        temp=process.with_name(process.name+".partial");temp.write_bytes(raw);temp.replace(process)
    checkpoint()
    code=1
    try:
        for item in manifest["files"]:
            path=repo/item["path"]
            if not path.is_file() or sha(path)!=item["sha256"] or path.stat().st_size!=item["bytes"]:
                raise ValueError("an immutable complete source or native changed: "+item["path"])
        state["verified_input_file_count"]=len(manifest["files"])
        state["all_verified_input_pins_preserved_in_manifest"]=True
        expected=next(v["sha256"] for v in manifest["files"] if v["path"]==str(SOURCE))
        command=[sys.executable,"-u",str(repo/SOURCE),"--repo-root",str(repo),
            "--manifest",str(args.manifest),"--out",str(native)]
        if args.resume is not None:
            if not args.resume_sha or sha(args.resume)!=args.resume_sha:
                raise ValueError("the exact accepted new prefix changed")
            command+=["--resume",str(args.resume)]
            state["original_prefix_native_sha256"]=args.resume_sha
        state.update(command=command,mathematical_source_sha256=expected);checkpoint()
        started=time.monotonic()
        with (out/"true-root-missing-intrinsic-jets.stdout.log").open("wb") as stream:
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
                raise ValueError("the actual native changed source or manifest identity")
            state.update(native_sha256=sha(native),native_bytes=native.stat().st_size,
                mathematical_complete=doc.get("complete"),mathematical_proved=doc.get("proved"),
                mathematical_failure=doc.get("failure"),mathematical_gates=doc.get("gates",[]))
            keys=("runtime","original_high_native_sha256","original_high_process_sha256",
                "original_high_source_sha256","original_high_manifest_sha256","object_sha256",
                "root_germ_sha256","auxiliary_native_sha256","auxiliary_process_sha256","contract_sha256",
                "actual_intrinsic_parameter","exact_root_interval","original_scalar_germ",
                "exact_original_physical_piece_interval","exact_fixed_intrinsic_parameter",
                "original_parameter_half_width_used_for_outward_enclosure",
                "finite_primitive_derivative_count","energy_derivative_count","ordinary_intrinsic_derivative_count",
                "new_supporting_stages","reused_supporting_stages","new_scalar_derivative_rows",
                "new_finite_Fourier_columns","new_finite_primitive_columns","new_complete_error_orders",
                "new_finite_component_norms","new_mean_products","new_energy_orders",
                "new_intrinsic_derivative_values","accepted_total_new_scalar_rows",
                "accepted_total_new_finite_columns","accepted_total_new_error_orders",
                "accepted_total_new_mean_products","accepted_total_new_energy_orders",
                "accepted_total_new_intrinsic_values","original_successful_finite_columns_recomputed",
                "original_successful_scalar_derivatives_recomputed",
                "original_successful_error_or_mean_or_energy_or_intrinsic_rows_recomputed",
                "original_successful_auxiliary_domains_recomputed","original_infinite_tail_evaluator_calls",
                "exact_original_finite_point_and_low_order_records_preserved",
                "original_finite_point_payload_sha256","original_comparison_record_payload_sha256",
                "original_reference_payload_hashes","denominator_gaps","last_attempted_stage",
                "preserved_actual_prefix","higher_Airy_Taylor_coefficients_computed",
                "smaller_Taylor_remainder_strong_return_or_full_inverse_claimed",
                "all_original_physical_seams_and_independent_means_retained")
            state.update({k:short(doc[k]) for k in keys if k in doc})
            receipts=[]
            for name,entry in doc.get("stages",{}).items():
                relative=Path(entry["file"])
                if relative.is_absolute() or ".." in relative.parts or relative.parts[0]!="stages":
                    raise ValueError("a natural stage leaves its actual output directory")
                path=native.parent/relative
                if not path.is_file() or sha(path)!=entry["sha256"] or path.stat().st_size!=entry["bytes"]:
                    raise ValueError("a complete actual supporting stage changed bytes")
                value=read(path)
                if not (value["complete"] and value["name"]==name
                    and value["source_sha256"]==expected
                    and value["input_manifest_sha256"]==args.manifest_sha
                    and value["payload_sha256"]==payload_sha(value["payload"])):
                    raise ValueError("a complete supporting stage changed scientific identity")
                receipts.append(dict(name=name,**entry,complete=True))
            state["all_complete_natural_stage_files"]=receipts
            state["all_available_natural_stage_files_verified"]=True
            state["complete_new_error_rows"]=short(doc.get("complete_errors",[])[12:])
            state["complete_new_energy_rows"]=short(doc.get("energy_jets",[])[11:])
            stage=doc.get("intrinsic_stage",{})
            state["complete_new_ordinary_intrinsic_jets"]={k:short(v[10:])
                for k,v in stage.get("ordinary_old_radial_jets",{}).items()}
            state["original54_comparison_records_retained"]=len(doc.get("original_low_order_identity_checks",[]))==54
            state["all_original_and_new_raw_arrays_and_scalar_records_retained_in_native"]=True
        good=(state["actual_returncode"]==0 and state.get("mathematical_complete") is True
            and state.get("mathematical_proved") is True and state.get("mathematical_failure") is None
            and state.get("mathematical_gates") and all(v["passed"] for v in state["mathematical_gates"])
            and state.get("all_available_natural_stage_files_verified") is True
            and state.get("exact_original_finite_point_and_low_order_records_preserved") is True)
        state["complete"]=bool(good);code=0 if good else 1
    except BaseException as error:
        state["failure"]=dict(type=type(error).__name__,message=str(error));code=1
    finally:
        checkpoint()
        print(json.dumps(dict(complete=state["complete"],actual_returncode=state["actual_returncode"],
            failure=state["failure"],process_sha256=sha(process)),allow_nan=False),flush=True)
    raise SystemExit(code)
if __name__=="__main__":main()
