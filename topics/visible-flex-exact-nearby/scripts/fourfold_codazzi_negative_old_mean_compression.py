#!/usr/bin/env python3
"""Consume the proved old-angle mean compression on completed negative source rows.

All six original scalar-jet tensors and profiles, all1328 coefficient rows,
all4377 radial weights, all positive rows and every independent even mean
are copied from completed exact natives. Only the new M0(gd) envelope and
its negative source integral are evaluated. Mathematics runs in public Actions.
"""
from __future__ import annotations
import argparse,copy,hashlib,json,os,sys,time
from pathlib import Path
import flint,numpy as np
from flint import arb,ctx
import fourfold_codazzi_exact_fold_cancelled_sources as old

PUBLIC=old.PUBLIC
FOLD_SHA="0ceafc2ba2adb8c1e14ab74c3059b0a0fde39446855df0889dec741f1cb61cfe"
FOLD_PROCESS="67bf926abf9066d8f09dd8fbb16cd439770203b5e551c2fa374ef42f9abfc3b8"
FOLD_SOURCE="52426ffbf1286f3ab06138879c03feb3795f5300a9e1f1e6625f6b1e2cf6a689"
FOLD_MANIFEST="c7c772e582a3d9197ab20e9df1c8efb1ad4ff0c881ea597c6e720e44fe85012d"
RADIAL_SHA=old.RADIAL_SHA
NORM_SHA=old.OLD_SHA
TERMS=old.CHANGED+old.UNCHANGED
RAW="old_mean_raw_D"
read,save,sha=old.read,old.save,old.sha
box,up,rec,compact,decode=old.box,old.up,old.rec,old.compact,old.decode
tensor_encode,tensor_decode=old.tensor_encode,old.tensor_decode

def payload_sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),
                                     allow_nan=False).encode()).hexdigest()

def compressed_mean_density(c,a,j):
    """Y1--7: only the new negative M0(gd), from the saved complete scalar jets."""
    D=c["D"];G,Gp=j["G"];Gpp=j["Gphi"][1]
    Z=[(j["Gr"]+D[0]*Gp+2*G*D[1]).upper(),
       (j["Grphi"]+D[1]*Gp+D[0]*Gpp+2*G*D[2]).upper()]
    pa=old.scalar_product(Z,j["B"])
    qa=old.scalar_product(j["Q"],j["T"],j["Gphi"],j["x"],j["y"])
    pb=old.scalar_product(Z,j["x"],j["y"])
    qb=old.scalar_product(j["Q"],j["G"],j["logAphi"],j["B"])
    rb=old.scalar_product(j["Q"],j["G"],j["y"],j["y"],j["y"])
    gd=[[(pa[p]+2*qa[p]).upper(),
         (2*pb[p]+qb[p]/2+rb[p]).upper()] for p in range(2)]
    # This is the new density derivative, not a call to the old source evaluator.
    density=old.mvjets(a["hi"],gd,1)[1]
    def profile(name):
        return sum((x*y for x,y in zip(a["profiles"][name],density)),arb(0)).upper()
    central=profile("central");negative=profile("negative")
    core=(central*central+4*negative*negative).sqrt().upper()
    MD=(a["composition"]*a["fourier"]*core).upper()
    # Retain the original complete scalar coefficient, including its mean.
    factor=(c["cB"]*c["V"][1]*c["V"][0]/4+c["m0_T0"]).upper()
    candidate=(factor*MD).upper()
    if not all(v.is_finite() and v.lower()>=0
               for v in (MD,factor,candidate,*density,*gd[0],*gd[1])):
        raise ValueError("the new complete mean density is not a finite nonnegative upper bound")
    evidence=dict(gd_first_angular_jets=tensor_encode(gd),
                  complete_mean_density_components=tensor_encode(density),
                  exact_old_mean_compressed_envelope=compact(MD),
                  unchanged_complete_raw_mean_factor=compact(factor),
                  new_complete_raw_mean_term=compact(candidate),
                  exact_identity="Pi D U(w)=Pi U(gd); Pi D T(w)=-Pi S(partial_phi(H^-1 gd))",
                  old_angle_and_input_density_unchanged=True,
                  leading_only_exact_gd_formula_not_assigned_to_w1=True)
    return candidate,evidence

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("repo-root","manifest","out"):p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--resume",type=Path)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new mean compression mathematics runs only in public repository Actions")
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),flint=flint.__version__,numpy=np.__version__)
    if runtime!=dict(python="3.12.14",flint="0.9.0",numpy="2.3.5"):
        raise ValueError("the exact previously successful runtime changed")
    if a.out.exists():raise FileExistsError("preserve every actual output and accepted prefix")
    ctx.prec=256;started=time.monotonic()
    result=dict(kind="actual_negative_old_mean_compression_from_complete_fold_sources_v1",
        public_repository=PUBLIC,public_run_id=os.environ.get("GITHUB_RUN_ID"),
        public_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),input_manifest_sha256=sha(a.manifest),runtime=runtime,
        complete=False,proved=False,failure=None,gates=[],cases=[],
        original_exact_fold_native_sha256=FOLD_SHA,
        original_exact_fold_process_sha256=FOLD_PROCESS,
        original_radial_reference_native_sha256=RADIAL_SHA,
        original_completed_norm_native_sha256=NORM_SHA,
        exact_real_delta_radius=str(old.DELTA),input_cutoff=old.CUTOFF,
        physical_frequency="4|j|",density_input_normalization="n^(7/6)",
        source_window="H^-4/3 -> ordinary radial L2(H^-2/3 x H^-2/3)",
        original_target_coefficient_ray_and_amplitude_solves_recomputed=0,
        old_completed_moment_rows_recomputed=0,old_completed_directed_rows_recomputed=0,
        old_completed_analytic_amplitude_cases_recomputed=0,
        old_completed_Airy_profiles_recomputed=0,old_completed_scalar_jet_cases_recomputed=0,
        original_radial_weights_or_split_integrals_recomputed=0,
        original_eight_other_source_terms_recomputed=0,
        original_independent_even_mean_rows_recomputed=0,
        original_positive_source_rows_recomputed=0,
        actual_new_mean_compression_rows=0,actual_new_negative_integral_rows=0,
        source_integral_rows_reused=0,source_integral_rows_copied_without_new_math=0,
        old_mean_and_all_Fourier_outputs_retained=True,
        original_global_seam_equations_and_fees_retained=True,
        exact_negative_mean_identity_only=True,
        first_correction_nonlocal_sources_paid=False,local_L0_w1_paid=False,
        positive_source_to_root_conversion_claimed=False,
        complete_strong_return_norm_evaluated=False,numerical_cutoff97_inverse_claimed=False,
        actual_PDE_branch_claimed=False)
    def check(name,truth):
        passed=bool(truth);result["gates"].append(dict(name=name,passed=passed))
        if not passed:raise ValueError("negative exact mean compression gate failed: "+name)
    def checkpoint():
        result["seconds"]=time.monotonic()-started;save(a.out,result)
    try:
        manifest=read(a.manifest)
        check("the exact mean consumer belongs to the one public repository",
              manifest["public_repository"]==PUBLIC)
        for f in manifest["files"]:
            path=a.repo_root/f["path"]
            if not path.is_file() or sha(path)!=f["sha256"] or path.stat().st_size!=f["bytes"]:
                raise ValueError("a complete immutable input changed: "+f["path"])
        paths={k:a.repo_root/v for k,v in manifest["input_paths"].items()}
        for name,digest,size in (
            ("exact_fold_native",FOLD_SHA,3180936),
            ("exact_fold_process",FOLD_PROCESS,36740),
            ("radial_reference_native",RADIAL_SHA,3434233),
            ("original_norm_native",NORM_SHA,4837715)):
            if sha(paths[name])!=digest or paths[name].stat().st_size!=size:
                raise ValueError("an exact completed original native or receipt changed: "+name)
        fold,receipt,radial,norm=[read(paths[k]) for k in
            ("exact_fold_native","exact_fold_process","radial_reference_native","original_norm_native")]
        check("the original actual exact_fold child completed all eight gates with its original native",
            receipt["actual_returncode"]==0 and receipt["complete"] is True
            and receipt["mathematical_complete"] is True and receipt["mathematical_proved"] is True
            and receipt["mathematical_failure"] is None and str(receipt["run_id"])=="43642808159"
            and receipt["native_sha256"]==FOLD_SHA and receipt["native_bytes"]==3180936
            and receipt["mathematical_source_sha256"]==FOLD_SOURCE
            and receipt["manifest_sha256"]==FOLD_MANIFEST
            and len(receipt["mathematical_gates"])==8 and all(g["passed"] for g in receipt["mathematical_gates"])
            and fold["source_sha256"]==FOLD_SOURCE and fold["input_manifest_sha256"]==FOLD_MANIFEST
            and fold["runtime"]==runtime and len(fold["gates"])==8)
        check("all three original natives retain their complete proof and no failure",
            all(d["complete"] and d["proved"] and d["failure"] is None
                and d["gates"] and all(g["passed"] for g in d["gates"])
                for d in (fold,radial,norm))
            and radial["source_sha256"]==old.RADIAL_SOURCE
            and radial["input_manifest_sha256"]==old.RADIAL_MANIFEST
            and norm["source_sha256"]==old.old.OLD_SOURCE
            and norm["input_manifest_sha256"]==old.old.OLD_MANIFEST)
        check("the original object root seams complete_delta and complete source norm are identical",
            fold["root_native_sha256"]==old.ROOT_SHA
            and fold["first_seam_native_sha256"]==old.SEAM_SHA
            and fold["original_completed_norm_native_sha256"]==NORM_SHA
            and fold["original_radial_reference_native_sha256"]==RADIAL_SHA
            and fold["source_window"]==result["source_window"]
            and fold["exact_real_delta_radius"]==result["exact_real_delta_radius"]
            and fold["input_cutoff"]==old.CUTOFF
            and fold["density_input_normalization"]=="n^(7/6)"
            and fold["exact_cover"]==radial["exact_cover"]
            and fold["exact_root_interval"]==radial["exact_root_interval"])
        rows=radial["coefficient_rows"]
        check("all1328 original coefficient and matrix rows have the same complete identities",
            len(rows)==len(norm["coefficient_rows"])==1328
            and all(r["common_row"]==i and norm["coefficient_rows"][i]["common_row"]==i
                and r["interval"]==norm["coefficient_rows"][i]["interval"]
                and r["original_root_row"]==norm["coefficient_rows"][i]["original_root_row"]
                for i,r in enumerate(rows))
            and payload_sha(rows)==fold["original_directed_table_sha256"]
            and all(x["interval"][1]==y["interval"][0] for x,y in zip(rows,rows[1:])))
        check("the six complete old scalar_jet tensors profiles and4377 source rows are exact",
            len(fold["cases"])==len(radial["cases"])==6
            and sum(len(c["rows"]) for c in fold["cases"])==4377
            and all(c["complete"] and c["complete_new_scalar_jets"]
                and c["exact_radius"]==r["exact_radius"] and c["exact_cover"]==r["exact_cover"]
                and len(c["rows"])==c["complete_original_rows"]
                and c["original_complete_analytic_amplitude_numeric"]==r["original_complete_analytic_amplitude_numeric"]
                and c["original_radial_reference_profiles_numeric"]==r["new_profiles_numeric"]
                and c["actual_negative_source_to_primitive_L2_gain"]==r["actual_negative_source_to_primitive_L2_gain"]
                for c,r in zip(fold["cases"],radial["cases"])))
        for key in ("fixed_positive_body_cut","positive_cut_receipt_sha256",
                    "actual_negative_Cauchy_native_sha256","exact_root_interval","exact_cover",
                    "original_directed_table_sha256"):
            result[key]=fold[key]
        result["original_completed_norm_rows_reused"]=1328
        result["original_completed_directed_rows_reused"]=1328
        result["original_completed_scalar_jet_cases_reused"]=6
        result["original_completed_analytic_amplitude_cases_reused"]=6
        result["original_completed_Airy_profile_cases_reused"]=6
        if a.resume:
            previous=read(a.resume)
            keys=("public_repository","source_sha256","input_manifest_sha256","runtime",
                "original_exact_fold_native_sha256","original_exact_fold_process_sha256",
                "original_radial_reference_native_sha256","original_completed_norm_native_sha256",
                "source_window","exact_real_delta_radius","input_cutoff","density_input_normalization")
            check("every accepted new mean prefix has the identical source runtime and all immutable inputs",
                  all(previous.get(k)==result.get(k) for k in keys))
            if len(previous["cases"])>6:raise ValueError("an accepted prefix has extra cases")
            result["cases"]=previous["cases"]
            result["original_prefix_audit"]=dict(native_sha256=sha(a.resume),
                native_bytes=a.resume.stat().st_size,complete=previous.get("complete"),
                proved=previous.get("proved"),failure=previous.get("failure"),gates=previous.get("gates"))
        checkpoint()
        fixed_case_keys=("exact_radius","exact_cover","complete_original_rows",
            "original_complete_analytic_amplitude_numeric","original_radial_reference_profiles_numeric",
            "new_scalar_jet_numeric","positive_complete_ordinary_L2_source",
            "positive_collar_complete_ordinary_L2_source","positive_body_complete_ordinary_L2_source",
            "actual_negative_source_to_primitive_L2_gain","original_complete_matrix_widths")
        for ci,accepted in enumerate(fold["cases"]):
            if ci<len(result["cases"]):
                out=result["cases"][ci]
                if any(out.get(k)!=accepted.get(k) for k in fixed_case_keys):
                    raise ValueError("a new prefix changed an old complete case tensor or bound")
                if out.get("original_complete_case_payload_sha256")!=payload_sha(accepted):
                    raise ValueError("a new prefix changed its exact input case")
                result["source_integral_rows_reused"]+=len(out["rows"])
                if out.get("complete"):continue
            else:
                out={k:copy.deepcopy(accepted[k]) for k in fixed_case_keys}
                out.update(complete=False,rows=[],new_negative_rows=0,
                    original_complete_case_payload_sha256=payload_sha(accepted),
                    original_positive_rows_and_split_integrals_copied=True,
                    all_original_scalar_jets_and_amplitude_tensors_copied=True)
                result["cases"].append(out)
            amplitude=tensor_decode(out["original_complete_analytic_amplitude_numeric"])
            amplitude["profiles"]=tensor_decode(out["original_radial_reference_profiles_numeric"])
            jets=tensor_decode(out["new_scalar_jet_numeric"])
            selected=accepted["rows"];prefix=len(out["rows"])
            if prefix>len(selected):raise ValueError("a saved row prefix exceeds the original case")
            neg=arb(0);raw_square=arb(0)
            for si,saved in enumerate(selected):
                idx=saved["common_row"]
                if rows[idx]["interval"]!=saved["interval"]:raise ValueError("an exact closed source row moved")
                if si<prefix:
                    item=out["rows"][si]
                    if item["common_row"]!=idx or item["interval"]!=saved["interval"]:
                        raise ValueError("an accepted new mean row changed its exact domain")
                else:
                    item=copy.deepcopy(saved)
                    oside=saved["negative"]
                    if oside.get("exact_zero_radial_part"):
                        result["source_integral_rows_copied_without_new_math"]+=1
                    else:
                        c=decode(norm["coefficient_rows"][idx]["bounds"]);c.update(decode(rows[idx]["bounds"]))
                        result["last_attempted_source_row"]=dict(case=ci,common_row=idx,interval=saved["interval"])
                        candidate,evidence=compressed_mean_density(c,amplitude,jets)
                        old_terms=oside["complete_scalar_nonlocal_terms"]
                        if set(old_terms)!=set(TERMS):raise ValueError("an original complete source term disappeared")
                        old_raw=up(box(old_terms[RAW]));new_raw=min(old_raw,candidate).upper()
                        term_values={k:up(box(v)) for k,v in old_terms.items()}
                        term_values[RAW]=new_raw
                        first_candidate=(c["C_J_scalar"]*sum(term_values.values(),arb(0))).upper()
                        first=min(first_candidate,up(box(oside["first_row_singular_envelope"]))).upper()
                        mean=up(box(oside["full_even_mean_singular_envelope"]))
                        weight=up(box(oside["radial_weight_integral"]))
                        if not weight>0:raise ValueError("an original nonzero radial weight lost positivity")
                        new_integral=(weight*(first*first+mean*mean)).upper()
                        old_integral=up(box(oside["squared_source_integral"]))
                        new_integral=min(new_integral,old_integral).upper()
                        nside=item["negative"]
                        nside["complete_scalar_nonlocal_terms"][RAW]=compact(new_raw)
                        nside["first_row_operator_term_envelopes"][RAW]=compact((c["C_J_scalar"]*new_raw).upper())
                        nside["first_row_singular_envelope"]=compact(first)
                        nside["squared_source_integral"]=compact(new_integral)
                        nside["exact_old_mean_compression"]=dict(**evidence,
                            original_complete_raw_mean_term=old_terms[RAW],
                            complete_term_choice=("new_exact_mean_identity" if candidate<old_raw else "original_complete_bound"),
                            original_complete_first_row=oside["first_row_singular_envelope"],
                            original_complete_squared_source_integral=oside["squared_source_integral"],
                            eight_other_complete_terms_copied=True,
                            independent_even_mean_copied=True,positive_rows_and_split_copied=True)
                        out["new_negative_rows"]+=1
                        result["actual_new_mean_compression_rows"]+=1
                        result["actual_new_negative_integral_rows"]+=1
                        result.pop("last_attempted_source_row",None)
                    out["rows"].append(item)
                if item["positive"]!=saved["positive"]:
                    raise ValueError("a completed positive source row or split was changed")
                ns=item["negative"];oside=saved["negative"]
                if ns.get("exact_zero_radial_part"):
                    if ns!=oside:raise ValueError("an exact zero radial source part changed")
                else:
                    if (ns["full_even_mean_singular_envelope"]!=oside["full_even_mean_singular_envelope"]
                        or ns["radial_weight_integral"]!=oside["radial_weight_integral"]
                        or any(ns["complete_scalar_nonlocal_terms"][k]!=oside["complete_scalar_nonlocal_terms"][k]
                               for k in TERMS if k!=RAW)
                        or any(ns["first_row_operator_term_envelopes"][k]!=oside["first_row_operator_term_envelopes"][k]
                               for k in TERMS if k!=RAW)):
                        raise ValueError("the new mean consumer changed an unrelated complete bound")
                    weight=up(box(ns["radial_weight_integral"]))
                    raw=up(box(ns["first_row_operator_term_envelopes"][RAW]))
                    raw_square+=weight*raw*raw
                neg+=box(ns["squared_source_integral"])
                if si%128==0:checkpoint()
            total=min(neg.sqrt().upper(),up(box(accepted["negative_complete_ordinary_L2_source"]))).upper()
            gain=up(box(accepted["actual_negative_source_to_primitive_L2_gain"]))
            primitive=min((gain*total).upper(),
                up(box(accepted["negative_leading_nonlocal_and_mean_component_Hminus4over3_to_primitive_L2"]))).upper()
            out["negative_complete_ordinary_L2_source"]=rec(total)
            out["negative_leading_nonlocal_and_mean_component_Hminus4over3_to_primitive_L2"]=rec(primitive)
            out["separate_first_row_term_L2_source_bounds"]=copy.deepcopy(accepted["separate_first_row_term_L2_source_bounds"])
            oldraw=up(box(accepted["separate_first_row_term_L2_source_bounds"]["negative"][RAW]))
            out["separate_first_row_term_L2_source_bounds"]["negative"][RAW]=compact(min(raw_square.sqrt().upper(),oldraw).upper())
            out["original_complete_negative_source_bound"]=accepted["negative_complete_ordinary_L2_source"]
            out["original_complete_negative_primitive_bound"]=accepted["negative_leading_nonlocal_and_mean_component_Hminus4over3_to_primitive_L2"]
            out["original_complete_source_bounds_not_overwritten"]=True
            out["first_correction_nonlocal_sources_paid"]=False
            out["complete"]=True;checkpoint()
        check("all six cases and all4377 original closed rows are retained",
            len(result["cases"])==6 and all(c["complete"] and len(c["rows"])==c["complete_original_rows"]
                for c in result["cases"]) and sum(len(c["rows"]) for c in result["cases"])==4377)
        check("every original positive row split independent_even_mean and eight other terms is unchanged",
            all(
                out["positive_complete_ordinary_L2_source"]==original["positive_complete_ordinary_L2_source"]
                and out["positive_collar_complete_ordinary_L2_source"]==original["positive_collar_complete_ordinary_L2_source"]
                and out["positive_body_complete_ordinary_L2_source"]==original["positive_body_complete_ordinary_L2_source"]
                and all(n["positive"]==o["positive"] and (
                    n["negative"].get("exact_zero_radial_part") or
                    n["negative"]["full_even_mean_singular_envelope"]==o["negative"]["full_even_mean_singular_envelope"])
                    for n,o in zip(out["rows"],original["rows"]))
                for out,original in zip(result["cases"],fold["cases"])))
        check("no completed target matrix profile scalar_jet weight positive or independent_mean computation was repeated",
            all(result[k]==0 for k in (
                "original_target_coefficient_ray_and_amplitude_solves_recomputed",
                "old_completed_moment_rows_recomputed","old_completed_directed_rows_recomputed",
                "old_completed_analytic_amplitude_cases_recomputed","old_completed_Airy_profiles_recomputed",
                "old_completed_scalar_jet_cases_recomputed","original_radial_weights_or_split_integrals_recomputed",
                "original_eight_other_source_terms_recomputed","original_independent_even_mean_rows_recomputed",
                "original_positive_source_rows_recomputed")))
        check("the exact mean compression remains only the original negative leading source window",
            result["exact_negative_mean_identity_only"] and not result["first_correction_nonlocal_sources_paid"]
            and not result["positive_source_to_root_conversion_claimed"]
            and not result["complete_strong_return_norm_evaluated"]
            and not result["numerical_cutoff97_inverse_claimed"] and not result["actual_PDE_branch_claimed"])
        result.update(complete=True,proved=True)
    except BaseException as error:
        result["failure"]=dict(type=type(error).__name__,message=str(error));raise
    finally:
        checkpoint()
        print(json.dumps(dict(complete=result["complete"],proved=result["proved"],failure=result["failure"],
            complete_cases=sum(bool(c.get("complete")) for c in result["cases"]),
            new_mean_rows=result["actual_new_mean_compression_rows"],
            new_negative_integrals=result["actual_new_negative_integral_rows"],
            reused_new_rows=result["source_integral_rows_reused"],seconds=result["seconds"]),allow_nan=False),flush=True)
if __name__=="__main__":main()
