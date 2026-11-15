#!/usr/bin/env python3
"""Merge accepted root-subtracted derivatives into all complete exterior sources.

Only the 1036 accepted derivative refinements are consumed by the unchanged
complete same-order matrix words and the unchanged six Airy profiles. Every
other complete source row is copied verbatim. Old local integrals, root means,
actual forcing jumps, all-output projections and all original failures remain.
"""
from __future__ import annotations
import argparse,copy,gzip,json,os,shutil,sys,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy as np
from flint import arb,ctx
import fourfold_codazzi_strict_exterior_first_Airy_complete_sources as full

PUBLIC=full.PUBLIC
CUTOFF=97
H=Q(9,10**6)
DELTA=Q(1,10**8)
SIGMA=Q(1,512)
RADII=full.RADII
FULL_RUN="43660841558"
FULL_NATIVE="17112d96633634d463059cab37efcd1d4a71dbdbc956e2ac8ddeded63378790c"
FULL_SOURCE="d4ea7d15874d602a833cf23c3ff48739974e41f2ca922a62da7ca2563ee9f768"
FULL_MANIFEST="6456b7fb5a3313b38f73e6e97116b023804778ee88cce5fec20f6a5f9dc17cba"
BSTAR_RUN="43663147595"
BSTAR_NATIVE="d61f42392f65463282585dfb59fae26ec25549b064bd8ef7d551c2a202d4637b"
BSTAR_SOURCE="3e3bd6b66a90c1244c9b97f0e07d6cd5e15845780f80c87aee8912a41008f139"
BSTAR_MANIFEST="5158bc631e1cbf3eddea6b6ad1a2e28ac2e782eea1f94da5970f1ac7c3e1c426"
sha=full.sha
payload_sha=full.payload_sha
read=full.read
save=full.save
receipt=full.receipt
checked_stage=full.checked_stage
decode=full.decode
encode=full.encode
up=full.up
box=full.box
record=full.record
ipow=full.ipow
WORD_NAMES=full.WORD_NAMES
TERM_NAMES=full.TERM_NAMES
MEAN_NAMES=("direct_u_h","complete_uJ_gd","complete_uJL_h","complete_uJB_w",
            "complete_curvature_v_nonmean_w")

def successful(index,process,index_path,run,source,manifest,gates,native):
    return (str(index.get("run_id"))==str(process.get("run_id"))==run
        and index.get("source_sha256")==process.get("mathematical_source_sha256")==source
        and index.get("input_manifest_sha256")==process.get("manifest_sha256")==manifest
        and index.get("complete") is True and index.get("proved") is True
        and index.get("failure") is None and process.get("actual_returncode")==0
        and process.get("mathematical_complete") is True
        and process.get("mathematical_proved") is True
        and process.get("mathematical_failure") is None
        and index.get("gates")==process.get("mathematical_gates")
        and len(index["gates"])==gates and all(v["passed"] for v in index["gates"])
        and sha(index_path)==process.get("native_sha256")==native
        and index_path.stat().st_size==process.get("native_bytes"))

def intersect_complete_operators(fresh,old):
    """Both candidates bound precisely the same complete all-output operator."""
    newops=fresh["complete_operators"];oldops=old["complete_operators"]
    if set(newops)!=set(oldops):
        raise ValueError("different complete first-correction operator families were paired")
    for name,value in newops.items():
        if not (value["full_mean_and_all_outputs_retained"]
                and oldops[name]["full_mean_and_all_outputs_retained"]):
            raise ValueError("a full output or mean was removed from a source operator")
        before=copy.deepcopy(value["bound"])
        value["bound"]=record(min(up(box(before)),up(box(oldops[name]["bound"]))).upper())
        value["new_complete_bound_before_intersection"]=before
        value["original_complete_bound_reused"]=copy.deepcopy(oldops[name]["bound"])
        value["intersection_of_two_complete_estimates_of_the_same_operator"]=True
    fresh["original_complete_operator_evidence_payload_sha256"]=payload_sha(old)
    return fresh

def merge_bounds(c,z,operators,oldbounds,local_record):
    fresh=full.nonlocal_constants(c,z,operators,local_record)
    for key,names in (("complete_nine_nonlocal_terms",TERM_NAMES),
                      ("complete_five_independent_even_mean_terms",MEAN_NAMES)):
        if set(fresh[key])!=set(oldbounds[key]) or set(fresh[key])!=set(names):
            raise ValueError("a complete source word or independent mean term was lost")
        fresh[key]=encode({name:min(up(box(fresh[key][name])),
                                   up(box(oldbounds[key][name]))).upper()
                           for name in names})
    if (fresh["final_old_J_Hminus5over3_to_Hminus2over3"]
            !=oldbounds["final_old_J_Hminus5over3_to_Hminus2over3"]
        or fresh["independent_even_mean_factor"]!=oldbounds["independent_even_mean_factor"]):
        raise ValueError("the original whole old-circle J or even-mean conversion changed")
    terms=decode(fresh["complete_nine_nonlocal_terms"])
    means=decode(fresh["complete_five_independent_even_mean_terms"])
    first=(c["C_J_scalar"]*sum(terms.values(),arb(0))).upper()
    mean=(c["exact_nonlocal_even_mean_row_factor"]*sum(means.values(),arb(0))).upper()
    first=min(first,up(box(oldbounds["first_nonlocal_singular_envelope"]))).upper()
    mean=min(mean,up(box(oldbounds["independent_even_mean_singular_envelope"]))).upper()
    local=up(box(local_record))
    squared=((first+local)*(first+local)+mean*mean).upper()
    squared=min(squared,up(box(oldbounds["complete_squared_vector_envelope"]))).upper()
    fresh.update(first_nonlocal_singular_envelope=record(first),
        independent_even_mean_singular_envelope=record(mean),
        complete_squared_vector_envelope=record(squared),
        original_local_unnormalized_numerator_recomputed=False,
        both_complete_estimates_use_the_same_first_correction=True)
    if not full.ensure_nonnegative([first,mean,local,squared,*terms.values(),*means.values()]):
        raise ValueError("a complete source intersection is invalid")
    return fresh

def complete_new_row(oldrow,bstar,accepted,real,z,profile):
    amps=full.source_amplitudes(bstar,accepted,real,profile)
    amps=intersect_complete_operators(amps,oldrow["complete_amplitude_operator_evidence"])
    bounds=merge_bounds(real,z,amps["complete_operators"],oldrow["source_bounds"],
        bstar["actual_first_row_local_source_singular_envelope"])
    if oldrow["radial_weight_integral"]!=bstar["radial_weight_integral"]:
        raise ValueError("an actual one-sided radial weight changed")
    weight=up(box(oldrow["radial_weight_integral"]))
    if not weight>0:raise ValueError("a complete radial source cell lost its positive weight")
    sep=dict(first_nonlocal=record((weight*ipow(up(box(bounds["first_nonlocal_singular_envelope"])),2)).upper()),
        independent_even_mean=record((weight*ipow(up(box(bounds["independent_even_mean_singular_envelope"])),2)).upper()),
        original_first_local=copy.deepcopy(bstar["complete_first_row_local_squared_source_integral"]))
    for key in ("first_nonlocal","independent_even_mean"):
        sep[key]=record(min(up(box(sep[key])),
            up(box(oldrow["separate_squared_source_integrals"][key]))).upper())
    squared=min((weight*up(box(bounds["complete_squared_vector_envelope"]))).upper(),
        up(box(oldrow["complete_squared_source_integral"]))).upper()
    item=copy.deepcopy(oldrow)
    item.update(complete_amplitude_operator_evidence=amps,source_bounds=bounds,
        original_radial_weight_reused_without_recomputation=True,
        original_local_source_integral_reused_without_recomputation=True,
        separate_squared_source_integrals=sep,complete_squared_source_integral=record(squared),
        actual_root_subtracted_derivative_row_payload_sha256=payload_sha(bstar),
        original_complete_source_row_payload_sha256=payload_sha(oldrow),
        root_subtraction_changes_the_bound_but_not_the_trial=True,
        full_nine_nonlocal_and_five_even_mean_terms_retained=True)
    return item

def dominant_rows(case):
    """New diagnostics of accepted envelopes, never a substitute for an integral."""
    out={}
    for side in ("negative","positive"):
        selected=[v for v in case["rows"] if v["side"]==side]
        data={}
        for key in ("original_first_local","first_nonlocal","independent_even_mean"):
            top=max(selected,key=lambda v:up(box(v["separate_squared_source_integrals"][key])))
            names=top["source_bounds"]["complete_nine_nonlocal_terms"]
            largest=max(names,key=lambda n:up(box(names[n])))
            data[key]=dict(serial=top["serial"],common_row=top["common_row"],
                interval=top["interval"],original_piece=top["original_piece"],
                squared_radial_contribution=copy.deepcopy(top["separate_squared_source_integrals"][key]),
                largest_first_row_nonlocal_word=largest)
        out[side]=data
    return out

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ("repo-root","manifest","prepared","out"):
        parser.add_argument("--"+key,type=Path,required=True)
    parser.add_argument("--resume",type=Path)
    args=parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("all new complete source mathematics requires the public Actions runner")
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),
                 flint=flint.__version__,numpy=np.__version__)
    if runtime!=dict(python="3.12.14",flint="0.9.0",numpy="2.3.5"):
        raise ValueError("the pinned interval runtime changed")
    if args.out.exists():raise FileExistsError("preserve every accepted or failed actual prefix")
    ctx.prec=320;start=time.monotonic()
    doc=dict(kind="complete_root_value_subtracted_first_Airy_old_circle_source_merge",
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),input_manifest_sha256=sha(args.manifest),runtime=runtime,
        complete=False,proved=False,failure=None,gates=[],cases=[],case_stages=[],
        original_complete_exterior_native_sha256=FULL_NATIVE,
        original_complete_exterior_source_sha256=FULL_SOURCE,
        original_complete_exterior_manifest_sha256=FULL_MANIFEST,
        original_bstar_native_sha256=BSTAR_NATIVE,
        original_bstar_source_sha256=BSTAR_SOURCE,
        original_bstar_manifest_sha256=BSTAR_MANIFEST,
        fixed_intrinsic_parameter="eta_0",exact_real_delta_radius=str(DELTA),
        exact_complete_inner_radius=str(H),input_cutoff=CUTOFF,physical_frequency="4 abs(j)",
        actual_first_correction_density="n^(1/6)",exact_amplitude_output_phi_width=str(SIGMA),
        source_window="H^-4/3 input -> ordinary radial L2(H^-2/3 pair); second row is the independent even mean",
        original_target_FFT_intrinsic_fold_Taylor_coefficient_or_derivative_stages_recomputed=0,
        original_complete_matrix_words_recomputed=0,original_same_order_matrix_conversions_recomputed=0,
        original_Airy_phase_profiles_recomputed=0,original_local_source_integrals_recomputed=0,
        original_root_norms_or_divided_forcing_or_seam_normalizations_recomputed=0,
        new_complete_operator_rows=0,reused_new_complete_operator_rows=0,
        copied_original_complete_source_rows=0,reused_copied_original_complete_source_rows=0,
        new_complete_source_integrals=0,new_radius_source_summaries=0,
        original_failed_path_gates_and_every_physical_seam_retained=True,
        all_fourier_outputs_old_projections_and_independent_mean_retained=True,
        artificial_interface_source_introduced=False,
        complete_first_corrected_trial_seam_sources_paid=False,
        positive_weighted_port_conversion_claimed=False,
        full_high_feedback_strong_return_cutoff97_inverse_or_PDE_branch_claimed=False)
    def gate(name,condition):
        value=bool(condition);doc["gates"].append(dict(name=name,passed=value))
        if not value:raise ValueError("complete root-subtracted source gate failed: "+name)
    def checkpoint():
        doc["seconds"]=time.monotonic()-start;save(args.out,doc)
    def saved(path,value):
        save(path,value);return receipt(path,args.out.parent)
    try:
        m=read(args.manifest)
        gate("the exact complete root-subtracted source manifest has the original physical windows",
            m["public_repository"]==PUBLIC
            and m["mathematical_parameters"]["input_cutoff"]==CUTOFF
            and m["mathematical_parameters"]["new_phi_width"]==str(SIGMA)
            and m["mathematical_parameters"]["exact_inner_radius"]==str(H))
        for entry in m["files"]:
            path=args.repo_root/entry["path"]
            if not path.is_file() or path.stat().st_size!=entry["bytes"] or sha(path)!=entry["sha256"]:
                raise ValueError("a pinned complete scientific input changed: "+entry["path"])
        paths={k:args.repo_root/v for k,v in m["input_paths"].items()}
        external={v["name"]:args.prepared/v["prepared_path"] for v in m["external_completed_natives"]}
        for entry in m["external_completed_natives"]:
            path=external[entry["name"]]
            if not path.is_file() or path.stat().st_size!=entry["bytes"] or sha(path)!=entry["sha256"]:
                raise ValueError("an immutable complete original artifact file changed")
        old,op,bn,bp,ext,ep=[read(paths[k]) for k in
            ("complete_index","complete_process","bstar_index","bstar_process","exterior_index","exterior_process")]
        gate("both original complete source runs retain their exact actual zero-return receipts and every gate",
            successful(old,op,paths["complete_index"],FULL_RUN,FULL_SOURCE,FULL_MANIFEST,11,FULL_NATIVE)
            and successful(bn,bp,paths["bstar_index"],BSTAR_RUN,BSTAR_SOURCE,BSTAR_MANIFEST,9,BSTAR_NATIVE))
        gate("the same complete old local source object underlies both successful refinements",
            old["original_exterior_native_sha256"]==bn["original_exterior_native_sha256"]
                ==sha(paths["exterior_index"])==ep["native_sha256"]
            and old["original_exterior_source_sha256"]==bn["original_exterior_source_sha256"]
                ==ext["source_sha256"]==full.EXT_SOURCE
            and ext["complete"] and ext["proved"] and ext["failure"] is None
            and ep["actual_returncode"]==0 and ext["gates"]==ep["mathematical_gates"]
            and all(g["passed"] for g in ext["gates"])
            and len(old["case_stages"])==len(bn["case_stages"])==len(ext["case_stages"])==6)
        gate("the full real delta disk fixed eta0 true root and physical inner interval are unchanged",
            old["fixed_intrinsic_parameter"]==bn["fixed_intrinsic_parameter"]=="eta_0"
            and Q(old["exact_real_delta_radius"])==Q(bn["exact_real_delta_radius"])==DELTA
            and old["exact_root_interval"]==bn["exact_root_interval"]==ext["exact_root_interval"]
            and old["exact_physical_inner_interval"]==bn["exact_physical_inner_interval"]
                ==ext["exact_physical_inner_interval"]
            and old["exact_cover"]==bn["exact_cover"]==ext["exact_cover"]
            and old["fixed_positive_body_cut"]==bn["fixed_positive_body_cut"]==ext["fixed_positive_body_cut"]
            and old["input_cutoff"]==bn["input_cutoff"]==CUTOFF)
        doc.update(exact_root_interval=copy.deepcopy(old["exact_root_interval"]),
            exact_physical_inner_interval=copy.deepcopy(old["exact_physical_inner_interval"]),
            exact_cover=copy.deepcopy(old["exact_cover"]),
            fixed_positive_body_cut=old["fixed_positive_body_cut"],
            original_complete_exterior_process_sha256=sha(paths["complete_process"]),
            original_bstar_process_sha256=sha(paths["bstar_process"]),
            original_exterior_local_native_sha256=sha(paths["exterior_index"]),
            original_complete_moment_native_sha256=sha(paths["moment_native"]),
            original_complete_directed_native_sha256=full.DIRECTED,
            original_complete_root_native_sha256=full.ROOT,
            original_complete_seam_native_sha256=sha(paths["seam_native"]),
            original_bstar_domain_results=copy.deepcopy(bn["cases"]),
            original_actual_complete_source_results=copy.deepcopy(old["cases"]),
            original_complete_source_stage_receipts=copy.deepcopy([old["coefficient_stage"],*old["case_stages"]]),
            original_bstar_stage_receipts=copy.deepcopy([bn["root_stage"],*bn["case_stages"]]))
        coefficient=checked_stage(paths["exterior_index"].parent,ext["coefficient_stage"])
        norm=read(paths["moment_native"]);cr=coefficient["rows"];nr=norm["coefficient_rows"]
        cp=external["complete_conversions"]
        converted=read(cp)
        gate("all1328 original complete same-order conversions and coefficient rows are preserved verbatim",
            sha(cp)==old["coefficient_stage"]["sha256"]
            and cp.stat().st_size==old["coefficient_stage"]["bytes"]
            and converted["complete"] and converted["source_sha256"]==FULL_SOURCE
            and converted["input_manifest_sha256"]==FULL_MANIFEST
            and coefficient["complete"] and coefficient["source_sha256"]==full.EXT_SOURCE
            and sha(paths["moment_native"])==full.NORM
            and norm["complete"] and norm["proved"] and norm["failure"] is None
            and all(g["passed"] for g in norm["gates"])
            and len(cr)==len(nr)==len(converted["rows"])==1328
            and all(c["common_row"]==n["common_row"]==z["common_row"]==i
                and c["interval"]==n["interval"]==z["interval"]
                and c["original_root_row"]==n["original_root_row"]==z["original_root_row"]
                and z["original_moment_row_payload_sha256"]==payload_sha(n)
                and set(z["matrix_conversion"]["costs"])==set(WORD_NAMES)
                for i,(c,n,z) in enumerate(zip(cr,nr,converted["rows"]))))
        gate("the successful root subtraction preserved its full mean all forcing jumps and every fallback",
            bn["new_refined_derivative_rows"]+bn["reused_refined_derivative_rows"]==1036
            and bn["original_fallback_rows"]+bn["reused_original_fallback_rows"]==3323
            and bn["original_complete_physical_seams_reused"]==1079
            and bn["new_seam_normalizations"]+bn["reused_seam_normalizations"]==653
            and bn["exact_root_mean_and_all_old_fourier_outputs_retained"]
            and bn["true_physical_seam_sources_unchanged"])
        doc.update(reused_complete_same_order_matrix_rows=1328,
            original_complete_physical_seams_retained=1079,
            original_complete_normalized_seam_rows_retained=653,
            original_complete_root_norm_stage=copy.deepcopy(bn["root_stage"]))
        if args.resume:
            previous=read(args.resume)
            keys=("public_repository","source_sha256","input_manifest_sha256","runtime",
                "original_complete_exterior_native_sha256","original_complete_exterior_source_sha256",
                "original_complete_exterior_manifest_sha256","original_bstar_native_sha256",
                "original_bstar_source_sha256","original_bstar_manifest_sha256",
                "original_complete_exterior_process_sha256","original_bstar_process_sha256",
                "original_exterior_local_native_sha256","original_complete_moment_native_sha256",
                "exact_root_interval","exact_physical_inner_interval")
            gate("every accepted new prefix has exactly the same source manifest runtime and complete input objects",
                all(previous.get(k)==doc.get(k) for k in keys))
            full.copy_resume_stages(args.resume,previous,args.out)
            doc["case_stages"]=copy.deepcopy(previous.get("case_stages",[]))
            doc["cases"]=copy.deepcopy(previous.get("cases",[]))
            doc["preserved_actual_prefix"]=dict(native_sha256=sha(args.resume),
                native_bytes=args.resume.stat().st_size,complete=previous["complete"],
                proved=previous["proved"],failure=previous["failure"],gates=previous["gates"])
        checkpoint()
        for ci,radius in enumerate(RADII):
            oldpath=external["complete_case_"+str(ci)]
            original=read(oldpath);star=checked_stage(paths["bstar_index"].parent,bn["case_stages"][ci])
            if not (sha(oldpath)==old["case_stages"][ci]["sha256"]
                and oldpath.stat().st_size==old["case_stages"][ci]["bytes"]
                and original["complete"] and original["source_sha256"]==FULL_SOURCE
                and original["input_manifest_sha256"]==FULL_MANIFEST
                and star["complete"] and star["source_sha256"]==BSTAR_SOURCE
                and star["input_manifest_sha256"]==BSTAR_MANIFEST
                and original["exact_radius"]==star["exact_radius"]==str(radius)
                and original["exact_cover"]==star["exact_cover"]
                and original["exact_inner_interval"]==doc["exact_physical_inner_interval"]
                and original["original_exterior_case_sha256"]==star["original_case_sha256"]
                    ==ext["case_stages"][ci]["sha256"]):
                raise ValueError("a complete original physical case changed identity")
            bst={r["original_exterior_serial"]:r for r in star["rows"]}
            if not (len(bst)==len(star["rows"])==len(original["rows"])
                and set(bst)==set(range(len(original["rows"])))):
                raise ValueError("the actual outward b-star order is not a bijection of the complete exterior cover")
            for serial,oldrow in enumerate(original["rows"]):
                sr=bst[serial]
                if not (oldrow["serial"]==serial
                    and all(oldrow[k]==sr[k] for k in
                        ("common_row","interval","side","original_root_row","original_piece"))
                    and oldrow["radial_weight_integral"]==sr["radial_weight_integral"]):
                    raise ValueError("a complete source row lost its original physical identity")
                if sr["new_root_subtracted_derivatives"] and not star["profile"]["usable_"+sr["side"]]:
                    raise ValueError("a new derivative escaped its actual accepted path gate")
            profile=original["complete_new_profile"]
            if not (profile["complete"] and profile["payload_sha256"]==payload_sha(profile["payload"])
                and profile["payload"]["exact_old_phi_width"]==str(SIGMA)
                and profile["payload"]["exact_input_cutoff"]==CUTOFF):
                raise ValueError("an original complete all-output Airy profile changed")
            p=decode(profile["payload"]["numeric"])
            path=args.out.parent/"cases"/("radius-"+str(radius.numerator)+"-"+str(radius.denominator)+".json.gz")
            if ci<len(doc["case_stages"]):
                case=checked_stage(args.out.parent,doc["case_stages"][ci])
                if not (case["source_sha256"]==sha(__file__) and case["input_manifest_sha256"]==sha(args.manifest)
                    and case["original_complete_case_sha256"]==sha(oldpath)
                    and case["original_bstar_case_sha256"]==bn["case_stages"][ci]["sha256"]
                    and case["exact_radius"]==str(radius)):
                    raise ValueError("a resumed complete source case changed scientific identity")
            else:
                case=dict(kind="complete_root_subtracted_first_Airy_source_radius",
                    source_sha256=sha(__file__),input_manifest_sha256=sha(args.manifest),
                    original_complete_case_sha256=sha(oldpath),
                    original_bstar_case_sha256=bn["case_stages"][ci]["sha256"],
                    complete=False,exact_radius=str(radius),exact_cover=copy.deepcopy(original["exact_cover"]),
                    exact_inner_interval=copy.deepcopy(original["exact_inner_interval"]),
                    complete_new_profile=copy.deepcopy(profile),original_complete_profile_recomputed=False,
                    original_bstar_profile=copy.deepcopy(star["profile"]),
                    original_normalized_seam_ledger=copy.deepcopy(star["seam_normalizations"]),
                    original_complete_outward_states=copy.deepcopy(star["traversal_states"]),
                    original_root_mean_norm_stage=copy.deepcopy(bn["root_stage"]),
                    rows=[],row_consumption=[])
                doc["case_stages"].append(saved(path,case));checkpoint()
            if len(case["rows"])!=len(case["row_consumption"]) or len(case["rows"])>len(original["rows"]):
                raise ValueError("an accepted complete source prefix is inconsistent")
            prefix=len(case["rows"])
            for serial in range(prefix):
                rr=case["row_consumption"][serial];new=bst[serial]["new_root_subtracted_derivatives"]
                if not (rr["serial"]==serial and rr["original_complete_row_payload_sha256"]==payload_sha(original["rows"][serial])
                    and rr["original_bstar_row_payload_sha256"]==payload_sha(bst[serial])
                    and rr["new_complete_source_operator_evaluation"]==new):
                    raise ValueError("an accepted new row changed one of its two complete original inputs")
                if not new and case["rows"][serial]!=original["rows"][serial]:
                    raise ValueError("an unchanged complete source row was not copied verbatim")
            newcount=sum(v["new_complete_source_operator_evaluation"] for v in case["row_consumption"])
            doc["reused_new_complete_operator_rows"]+=newcount
            doc["reused_copied_original_complete_source_rows"]+=prefix-newcount
            if case["complete"]:
                if prefix!=len(original["rows"]):raise ValueError("a completed source case is missing rows")
                summary=case["complete_case_summary"]
                if ci==len(doc["cases"]):doc["cases"].append(copy.deepcopy(summary))
                elif doc["cases"][ci]!=summary:raise ValueError("a completed source summary changed")
                checkpoint();continue
            for serial in range(prefix,len(original["rows"])):
                oldrow=original["rows"][serial];sr=bst[serial];idx=sr["common_row"]
                ident=dict(serial=serial,original_complete_row_payload_sha256=payload_sha(oldrow),
                    original_bstar_row_payload_sha256=payload_sha(sr),
                    new_complete_source_operator_evaluation=sr["new_root_subtracted_derivatives"])
                doc["last_attempted_row"]=dict(radius=str(radius),serial=serial,common_row=idx);checkpoint()
                if sr["new_root_subtracted_derivatives"]:
                    real=decode(nr[idx]["bounds"]);accepted=decode(cr[idx]["bounds"])
                    z=decode(converted["rows"][idx]["matrix_conversion"]["costs"])
                    item=complete_new_row(oldrow,sr,accepted,real,z,p)
                    doc["new_complete_operator_rows"]+=1;doc["new_complete_source_integrals"]+=1
                else:
                    item=copy.deepcopy(oldrow)
                    doc["copied_original_complete_source_rows"]+=1
                case["rows"].append(item);case["row_consumption"].append(ident)
                doc.pop("last_attempted_row",None);doc["case_stages"][ci]=saved(path,case);checkpoint()
                if serial%128==0:
                    print(json.dumps(dict(radius=str(radius),accepted_rows=len(case["rows"]),
                        total_rows=len(original["rows"]),seconds=time.monotonic()-start)),flush=True)
            newcount=sum(v["new_complete_source_operator_evaluation"] for v in case["row_consumption"])
            if newcount:
                summary_source=dict(exact_cover=original["exact_cover"],
                    exact_inner_interval=original["exact_inner_interval"],
                    actual_negative_source_to_primitive_L2_gain=original["complete_case_summary"][
                        "original_actual_negative_source_to_primitive_L2_gain"])
                summary=full.summarize_case(case,summary_source)
                diagnostics=dominant_rows(case);doc["new_radius_source_summaries"]+=1
            else:
                summary=copy.deepcopy(original["complete_case_summary"])
                diagnostics=None
                if case["rows"]!=original["rows"]:
                    raise ValueError("a complete failed-path fallback case changed its original source rows")
            case.update(complete=True,complete_case_summary=summary,
                complete_dominant_accepted_row_diagnostics=diagnostics,
                accepted_new_derivative_rows=newcount,
                original_complete_source_rows_copied_verbatim=len(case["rows"])-newcount,
                original_complete_summary_reused_verbatim=newcount==0,
                all_original_physical_seam_sources_retained=True,
                complete_first_corrected_trial_seam_sources_paid=False,
                no_artificial_inner_interface_source=True)
            doc["case_stages"][ci]=saved(path,case);checkpoint()
            if ci==len(doc["cases"]):doc["cases"].append(copy.deepcopy(summary))
            elif doc["cases"][ci]!=summary:raise ValueError("a completed summary index changed")
            checkpoint()
        gate("all six radii retain every4359 source row with exactly1036 new and3323 unchanged complete rows",
            len(doc["case_stages"])==len(doc["cases"])==6
            and sum(c["complete_exterior_rows"] for c in doc["cases"])==4359
            and doc["new_complete_operator_rows"]+doc["reused_new_complete_operator_rows"]==1036
            and doc["copied_original_complete_source_rows"]+doc["reused_copied_original_complete_source_rows"]==3323
            and all(c["complete"] and Q(c["exact_radius"])==RADII[i] for i,c in enumerate(doc["cases"])))
        gate("all original successful targets matrices profiles local integrals and true seams were reused",
            all(doc[k]==0 for k in
                ("original_target_FFT_intrinsic_fold_Taylor_coefficient_or_derivative_stages_recomputed",
                 "original_complete_matrix_words_recomputed","original_same_order_matrix_conversions_recomputed",
                 "original_Airy_phase_profiles_recomputed","original_local_source_integrals_recomputed",
                 "original_root_norms_or_divided_forcing_or_seam_normalizations_recomputed"))
            and doc["all_fourier_outputs_old_projections_and_independent_mean_retained"]
            and not doc["complete_first_corrected_trial_seam_sources_paid"]
            and not doc["positive_weighted_port_conversion_claimed"]
            and not doc["full_high_feedback_strong_return_cutoff97_inverse_or_PDE_branch_claimed"])
        doc["complete"]=True;doc["proved"]=True
    except BaseException as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error));raise
    finally:
        checkpoint()
        print(json.dumps(dict(complete=doc["complete"],proved=doc["proved"],failure=doc["failure"],
            new_complete_operator_rows=doc["new_complete_operator_rows"],
            copied_original_complete_source_rows=doc["copied_original_complete_source_rows"],
            complete_cases=len(doc["cases"]),native_sha256=sha(args.out),seconds=doc["seconds"]),
            allow_nan=False),flush=True)
if __name__=="__main__":main()
