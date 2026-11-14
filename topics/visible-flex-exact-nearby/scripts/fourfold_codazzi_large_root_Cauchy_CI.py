#!/usr/bin/env python3
"""Public worker for only new scalar Cauchy budgets from completed original data."""
from __future__ import annotations
import argparse,json,shutil,signal,subprocess,sys
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import REPO
from fourfold_native_lossless_parts import restore
REL="topics/visible-flex-exact-nearby/"
SELF=REL+"scripts/fourfold_codazzi_large_root_Cauchy_CI.py"
SOURCE=REL+"scripts/fourfold_codazzi_large_root_Cauchy_budget.py"
FOLDER=REL+"notes/large_root_Cauchy_ci/"
NAME="full-real-large-root-Cauchy-two-windows.json.gz"
LABEL="actual_full_real_large_root_Cauchy_scalar_consumer"
KIND="actual_full_real_large_root_Cauchy_two_windows_v1"

def small(path,doc):
    data=(json.dumps(doc,ensure_ascii=False,indent=2)+"\n").encode()
    if len(data)>60000:raise ValueError("new plaintext exceeds60000 bytes; keep complete native")
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(data)

def hydrate(a):
    if digest(a.manifest)!=a.manifest_sha or digest(a.rules)!=a.rules_sha:
        raise ValueError("the exact reviewed manifest and rules are required")
    d=read(a.manifest)
    if d["files"].get(SELF)!=digest(__file__):raise ValueError("the exact worker identity changed")
    paths=set(d["files"])|{"README.md",REL+"README.md",FOLDER,
        str(a.manifest.relative_to(REPO)),str(a.rules.relative_to(REPO))}
    subprocess.run(["git","-c","safe.directory="+str(REPO),"sparse-checkout","set","--no-cone","--stdin"],
        cwd=REPO,input="\n".join("/"+p for p in sorted(paths))+"\n",text=True,check=True)
    print(json.dumps({"exact_paths":len(paths),"old_large_arrays_not_hydrated":True}))

class LargeRootCauchyWorker(ReviewedBodyWorker):
    def __init__(self,a):
        super().__init__(a)
        self.name=f"run-{self.run_label}-full-real-large-root-Cauchy"
        self.dest=REPO/FOLDER/self.name;self.reused_complete=False
        self.state.update(kind="actual_public_full_real_large_root_Cauchy_process_v1",
            worker_source_sha256=digest(__file__),original_root_run=43616813816,
            original_intrinsic_parts_run=43583838026,
            original_target_candidate_response_and_angular_coefficients_recomputed=0,
            full_low_high_Schur_inverse_proved=False,complete_infinite_BVP_inverse_proved=False,
            true_parameter_Schur_proved=False,actual_PDE_branch_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get("kind")!="full_real_large_root_Cauchy_original_receipts_inputs_v1":
            raise ValueError("the exact independent scalar consumer manifest is required")

    def original_inputs(self):
        root=self.args.root_artifact.resolve()
        native=root/"consumers"/"piecewise-real-root-fold-resumed-v2.json.gz"
        process=root/"consumers"/"process.json"
        if not native.exists() or not process.exists():
            raise ValueError("the original full root native and actual child process are required")
        if digest(native)!="dbaaf9f7866fceae9583d6cb639441365a64b3ac0d381291fa6d1a5afe247212":
            raise ValueError("the original root native differs")
        shared=self.science/self.manifest["shared_intrinsic_manifest"]
        inputs={"root-native":digest(native),"root-process":digest(process),"shared":digest(shared)}
        for spec in read(shared)["parts"]:
            path=self.args.body_artifacts/spec["artifact"]/spec["inner_path"]
            if digest(path)!=spec["sha256"]:raise ValueError("an original body part differs")
            inputs[spec["artifact"]+"/"+spec["inner_path"]]=digest(path)
        shutil.copyfile(process,self.evidence/"original-piecewise-root-child-process.json")
        self.state["actual_original_input_sha256"]=inputs
        return native,process,shared,inputs

    def exact_native(self,root,p,entry):
        path=root/"native"/NAME
        if not path.exists():
            if "lossless_manifest" not in entry:raise ValueError("a saved actual prefix is absent")
            path=self.work/("restored-"+entry["sha256"]+".json.gz")
            if not path.exists():restore(root/entry["lossless_manifest"],path)
        if digest(path)!=entry["sha256"] or path.stat().st_size!=entry["bytes"]:
            raise ValueError("actual saved prefix bytes changed")
        return path

    def prefix(self,inputs):
        root=REPO/FOLDER
        if not root.exists():return None
        found=[]
        for pp in sorted(root.glob("*/process.json")):
            p=read(pp)
            if p.get("repository")!="Rogerhu12/math-research-public":continue
            entries=[e for e in p.get("native_files",[]) if e.get("logical_file")=="native/"+NAME]
            if len(entries)!=1:continue
            path=self.exact_native(pp.parent,p,entries[0]);d=read(path)
            if (d.get("kind")!=KIND or d.get("source_sha256")!=self.manifest["files"][SOURCE]
                or d.get("input_sha256")!=inputs or not d.get("rows")):continue
            complete=bool(d.get("complete") and not d.get("failure")
                and d.get("gates") and all(g["passed"] for g in d["gates"]))
            if complete and not any(c.get("label")==LABEL and c.get("actual_returncode")==0 for c in p.get("children",[])):
                continue
            found.append((complete,len(d["rows"]),pp,path))
        return max(found,key=lambda x:(x[0],x[1])) if found else None

    def execute(self,label,command):
        try:return super().execute(label,command)
        finally:
            path=self.cache/NAME
            if path.exists():
                d=read(path)
                out=dict(complete=d.get("complete"),failure=d.get("failure"),
                    gates=d.get("gates",[]),native_sha256=digest(path),
                    complete_common_rows=len(d.get("rows",[])),
                    original_complete_native_reused=self.reused_complete)
                small(self.evidence/"actual-latest-Cauchy-outcome.json",out)
                print(json.dumps(out),flush=True)
                if d.get("failure") and self.log.exists():print(self.log.read_text()[-16000:],flush=True)

    def prepare(self):
        root,process,shared,inputs=self.original_inputs()
        path=self.cache/NAME
        command=[sys.executable,"-u",str(self.science/SOURCE),
            "--root-native",str(root),"--root-process",str(process),"--shared",str(shared),
            "--body-artifacts",str(self.args.body_artifacts.resolve()),"--out",str(path)]
        previous=self.prefix(inputs)
        if previous:
            complete,count,pp,native=previous;self.reused_complete=complete
            command+=["--resume",str(native)]
            shutil.copyfile(pp,self.evidence/"original-Cauchy-prefix-process.json")
            small(self.evidence/"exact-Cauchy-prefix-reuse.json",dict(
                original_process_sha256=digest(pp),original_native_sha256=digest(native),
                original_process_complete=read(pp).get("complete"),
                complete_new_common_rows_reused=count,native_complete=complete,
                exact_scientific_source_and_all_inputs_verified=True))
        self.publish();self.execute(LABEL,command)
        d=read(path)
        if (d.get("kind")!=KIND or not d.get("complete") or d.get("failure")
            or d.get("source_sha256")!=self.manifest["files"][SOURCE] or d.get("input_sha256")!=inputs
            or not d.get("gates") or not all(g["passed"] for g in d["gates"])
            or len(d.get("cases",[]))!=6 or not all(c.get("passed") for c in d["cases"])
            or d.get("selected",{}).get("exact_radius")!="1/50"
            or not d.get("same_full_real_family_root_Cauchy_estimate_proved")
            or not d.get("all_frequencies_and_independent_even_mean_retained")
            or d.get("old_target_candidate_response_coefficients_recomputed")!=0
            or d.get("positive_side_lower_source_window_proved")
            or d.get("complex_parameter_Hilbert_energy_claimed")
            or d.get("numerical_full_return_strong_norm_or_cutoff_proved")
            or d.get("complete_infinite_BVP_inverse_proved") or d.get("true_parameter_Schur_proved")):
            raise ValueError("the complete two-window energy result failed or changed scope")
        summary={k:v for k,v in d.items() if k!="rows"}
        summary.update(native_sha256=digest(path),native_bytes=path.stat().st_size,
            complete_original_native_retained=True,original_complete_native_reused=self.reused_complete,
            actual_new_scalar_rows_in_this_child=0 if self.reused_complete else d["new_common_rows_in_this_child"])
        small(self.evidence/"full-real-large-root-Cauchy-summary.json",summary)
        self.state.update(complete=True,complete_native_sha256=digest(path),
            actual_scientific_gates=len(d["gates"]),complete_new_common_rows=len(d["rows"]),
            actual_new_scalar_rows_in_this_child=summary["actual_new_scalar_rows_in_this_child"],
            selected_radius=d["selected"]["exact_radius"],selected_bounds=d["selected"]["bounds"],
            same_full_real_family_root_Cauchy_estimate_proved=True)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--mode",choices=("hydrate","run"),required=True)
    for name in ("manifest","rules"):p.add_argument("--"+name,type=Path,required=True)
    for name in ("manifest-sha","rules-sha","driver-sha"):p.add_argument("--"+name,required=True)
    for name in ("work","artifact-dir","root-artifact","body-artifacts"):p.add_argument("--"+name,type=Path)
    p.add_argument("--compute-minutes",type=int,default=30)
    p.add_argument("--checkpoint-minutes",type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    if a.mode=="hydrate":hydrate(a);return
    if any(getattr(a,n) is None for n in ("work","artifact_dir","root_artifact","body_artifacts")):
        p.error("all owned paths and original artifact directories are required")
    a.kind="full-real-large-root-Cauchy";a.mode="prepare";a.first=0;a.end=0
    a.recovery_manifest=None;a.recovery_sha=None
    worker=LargeRootCauchyWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,"interrupted",True))
    worker.run_cap()
if __name__=="__main__":main()
