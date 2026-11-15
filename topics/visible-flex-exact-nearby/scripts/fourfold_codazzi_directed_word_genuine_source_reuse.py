#!/usr/bin/env python3
"""Reuse complete directed operator words in both genuine-source windows.

Only new positive bound-number comparisons and complete scalar combinations
are evaluated. The successful genuine rows, amplitudes, operator words and
radial integrals are never regenerated. Reproducible data stay temporary.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,platform,sys,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy,scipy
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby/"
KIND="actual_two_window_directed_word_reuse_for_genuine_sources_v1"
CONTRACT="9f4f5f9b225fe3981068c665c2326b39183449a7d2fa57debc51a9cea9f5c7e0"
C_EXEC="bca0f97d7c610f8f2572e61d1e1442a8b9c256a4c5429253682b6d803e3a21c3"
C_SOURCE="b0648a3bc244e6671176ac096c759b3e70e57d8c04b75bd4dd74442bfcaf95c0"
C_MANIFEST="8465759dfe9101bb7e20275cec1a5b98e23efb4dbe643e492fb8189250b005b9"
D_PROCESS="00afd54464db46f110ecff8c1968b158deedac719a363590fc366038b47fedb8"
D_SOURCE="f3a5d7b0caad97d65464e6b79e0884e3a50085cbc6b2d9bab35e9ab1e8a66b0d"
D_MANIFEST="29465d2a93165f40f42b2ea73c772374a882475fd59f44fdbce20b37ff4d402f"
D_CONTRACT="394068a9b18a47d5c1b9330f162c39b9b02a0d65db4b46ba5773c995adc6a52e"
OLD_NATIVE="7662350ac2cf5c0838e545fb6ba4994c118b985b5a133b869b3ca5486b70563c"
OLD_PROCESS="f888e47e69f41b4b5c73656ac9afd321289a806ce948816d9612111a045d99e4"
OLD_SOURCE="56b68983f36bb3d88e1427081ba9e60a8f6cf43dcd9578a0d925e1834292555d"
OLD_MANIFEST="7290cbb07293c15a239ffafb0e342e6c1b7ea812106f569e88bbe4d2502180df"
ROOT_SHA="dbaaf9f7866fceae9583d6cb639441365a64b3ac0d381291fa6d1a5afe247212"
FORCE_SHA="54a79bf80df641797b28f998fe547c93d64b58ea329b675f3d62d23d4f161d47"
ROOTS=(Q(1191984371497,5000000000000),Q(2383968743003,10000000000000))
PIECE=(Q(2147184947341121,9007199254740992),Q(4295308144604611,18014398509481984))
RUNTIME=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0")
WORD_MAP=dict(complete_SV="C_SV_directed",complete_SQ="C_SQ_directed",
    complete_RQ_J_g="C_RQJ_directed",complete_RQ_JL_h="C_RQJL_directed",
    complete_primitive="C_primitive_directed",complete_uJ_g="C_uJ_directed",
    complete_uJL_h="C_uJL_directed",complete_uJB_w="C_uJB_directed")
FIRST_KEYS=("complete_SV","complete_SQ","complete_RQ_J_g","complete_RQ_JL_h","complete_primitive")
MEAN_KEYS=("complete_uJ_g","complete_uJL_h","complete_uJB_w")

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def rb(v):
    if isinstance(v,arb):return v
    if isinstance(v,int):return arb(v)
    if isinstance(v,Q):return arb(v.numerator)/arb(v.denominator)
    if isinstance(v,str):return arb(v)
    return arb(v["ball"])
def up(v):return abs(rb(v)).upper()
def rec(v):return dict(ball=rb(v).str(64))
def read(p):
    p=Path(p);b=p.read_bytes()
    return json.loads(gzip.decompress(b) if p.suffix==".gz" else b)
def payload_sha(v):
    return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":"),
        ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def save(p,v,compressed=False):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
    t=p.with_name(p.name+".partial")
    t.write_bytes(gzip.compress(raw,mtime=0) if compressed else raw);t.replace(p)
def nonnegative(v,name):
    x=rb(v)
    if not x.is_finite() or x.lower()<0:raise ValueError("invalid accepted nonnegative bound: "+name)
    return x
def positive_budget_lower(c,key):
    return nonnegative(c[key],key).lower()

def denominator_lower(c,density,name):
    """A lower bound for the old positive algorithm coefficient, not a function."""
    L=lambda k:positive_budget_lower(c,k)
    j=L("C_J_new" if density==0 else "C_J_scalar")
    if name=="complete_SV":
        value=L("C_V")
        if density==1:value=value+L("C_R")*j*L("C_B")
    elif name=="complete_SQ":value=L("C_Q")
    elif name=="complete_RQ_J_g":value=L("C_R")*j
    elif name=="complete_RQ_JL_h":value=L("C_R")*j*L("C_L")
    elif name=="complete_primitive":value=L("cB")*L("m3_vphi")*L("C_I")
    elif name=="complete_uJ_g":value=L("m3_u")*j
    elif name=="complete_uJL_h":value=L("m3_u")*j*L("C_L")
    elif name=="complete_uJB_w":value=L("m3_u")*j*L("C_B")
    else:raise ValueError("an unproved directed word was requested")
    return value.lower()

def selected_rows(rows):
    left,right=PIECE[0],ROOTS[1];out=[];cursor=left;parts=0
    for row in rows:
        lo,hi=map(Q,row["interval"]);a=max(lo,left);b=min(hi,right)
        if not a<b:continue
        if a!=cursor:raise ValueError("the original rows no longer cover the actual physical interval")
        cuts=sorted(set([a,b]+[t for t in ROOTS if a<t<b]))
        parts+=len(cuts)-1;out.append(row);cursor=b
    if cursor!=right or not out:raise ValueError("incomplete actual negative cover")
    return out,parts

def comparison(selected,maxima,density,name,temporary,doc):
    k=up(nonnegative(maxima[WORD_MAP[name]],WORD_MAP[name]));ratios=[];valid=True
    evidence=[]
    for row in selected:
        beta=denominator_lower(row["bounds"],density,name)
        doc["new_bound_number_denominator_evaluations"]+=1
        if not beta.is_finite() or beta<0:raise ValueError("a positive-budget lower calculation is invalid")
        if beta>0:
            ratio=up(k/beta);ratios.append(ratio)
            evidence.append(dict(common_row=row["common_row"],positive_algorithm_budget_lower=rec(beta),
                complete_word_to_old_budget_ratio_upper=rec(ratio)))
        else:
            valid=False
            evidence.append(dict(common_row=row["common_row"],positive_denominator_unavailable=True))
    worst=max(ratios).upper() if valid else None
    q=min(arb(1),worst).upper() if worst is not None else arb(1)
    key="density"+str(density)+"_"+name
    temporary["row_budget_comparisons"][key]=evidence
    doc["new_complete_uniform_comparisons"]+=1
    return q,dict(source_term=key,density=density,complete_word=WORD_MAP[name],
        actual_original_case_word_bound=maxima[WORD_MAP[name]],
        uniform_comparison_upper=rec(q),
        untruncated_ratio_upper=None if worst is None else rec(worst),
        all_selected_positive_denominators=valid,selected_original_rows=len(selected),
        denominator_is_old_algorithm_bound_number_only=True,
        old_genuine_amplitude_and_radial_measure_not_evaluated=True,
        same_SV_in_second_window=(name=="complete_SV" and density==1),
        genuine_inverse_correction_remains_in_unchanged_amplitude=True)

def selected_total(old,candidate):
    candidate=up(candidate)
    if not candidate.is_finite():raise ValueError("nonfinite complete scalar combination")
    if candidate<rb(old).lower():return rec(candidate),True
    return old,False

def combine(original,terms,means):
    local=original["local_L2_upper"]
    nl_sum=sum((up(v) for k,v in terms.items() if not k.startswith("local_raw_")),arb(0))
    nl,nlnew=selected_total(original["nonlocal_total_L2_upper"],nl_sum)
    first,fnew=selected_total(original["first_L2_upper"],up(local)+up(nl))
    mean,mnew=selected_total(original["mean_L2_upper"],sum((up(v) for v in means.values()),arb(0)))
    pair,pnew=selected_total(original["combined_L2_upper"],(up(first)**2+up(mean)**2).sqrt())
    return dict(local_L2_upper=local,nonlocal_total_L2_upper=nl,first_L2_upper=first,
        mean_L2_upper=mean,combined_L2_upper=pair,
        complete_first_source_term_L2_upper=terms,complete_independent_mean_term_L2_upper=means,
        strictly_smaller_complete_aggregates=dict(nonlocal_total=nlnew,first=fnew,mean=mnew,combined=pnew),
        exact_negative_physical_cover=original["exact_negative_physical_cover"],
        actual_dr_measure=original["actual_dr_measure"],
        one_sided_uncertain_root_band_retained=original["one_sided_uncertain_root_band_retained"],
        both_density_windows_retained=True,
        total_squared_envelope_radial_weight_upper=original["total_squared_envelope_radial_weight_upper"],
        old_nine_word_and_five_physical_mean_counts=original["old_nine_word_and_five_physical_mean_counts"],
        first_output_window=original["first_output_window"],
        independent_even_mean_window=original["independent_even_mean_window"],
        input_window=original["input_window"],outer_J_window=original["outer_J_window"],
        complete_local_budget_read_unchanged=True,
        original_temporary_row_payload_sha256=original["temporary_complete_source_row_payload_sha256"],
        old_source_row_or_radial_integral_recomputed=False)

def render(doc):
    lines=["# Actual two-window directed-word reuse for genuine negative sources","",
        "Public Actions run "+str(doc.get("run_id"))+"/"+str(doc.get("run_attempt"))+".",
        "Source SHA256: "+doc["source_sha256"]+".",
        "Input manifest SHA256: "+doc["input_manifest_sha256"]+".",
        "Actual complete/proved: "+str(doc["complete"])+"/"+str(doc["proved"])+".",
        "Actual scientific return code: "+str(doc["actual_returncode"])+".","",
        "All original coefficient, directed-word, genuine amplitude, source-row and radial-integral evaluations are reused without regeneration.",
        "Only complete bound-number ratios and complete scalar norm combinations are new.",
        "The old complete K Lambda matrix provenance gives both negative source windows; the output mean and both signs remain.","",
        "## Actual work counts","",json.dumps({k:doc[k] for k in (
            "original_complete_coefficient_rows_read","original_selected_coefficient_rows_read",
            "original_complete_word_maxima_read","original_complete_genuine_source_terms_read",
            "new_bound_number_denominator_evaluations","new_complete_uniform_comparisons",
            "new_complete_scalar_recombinations","old_numerical_enclosures_recomputed",
            "old_genuine_source_rows_recomputed","old_radial_integrals_recomputed")},sort_keys=True)]
    con=doc.get("complete_source_conclusion")
    if con:
        lines+=["","## Complete two-row source norms","",
            "| Quantity | Directed complete upper ball |","|---|---|"]
        for key in ("local_L2_upper","nonlocal_total_L2_upper","first_L2_upper","mean_L2_upper","combined_L2_upper"):
            lines.append("| "+key+" | "+con[key]["ball"]+" |")
        lines+=["","Exact negative cover: "+repr(con["exact_negative_physical_cover"])+".",
            "The local budget and original physical radial measure were read unchanged. No difference of upper bounds is used.","",
            "## Complete uniform comparison factors","",
            "| Accepted source term | Full original directed word | Uniform factor |","|---|---|---|"]
        for e in doc["complete_comparison_conclusions"]:
            lines.append("| "+e["source_term"]+" | "+e["complete_word"]+" | "+e["uniform_comparison_upper"]["ball"]+" |")
        for label,key in (("Complete first-row terms","complete_first_source_term_L2_upper"),
                          ("Independent physical even-mean terms","complete_independent_mean_term_L2_upper")):
            lines+=["","## "+label,"","| Retained term | Complete ordinary radial L2 upper ball |","|---|---|"]
            for k,v in con[key].items():lines.append("| "+k+" | "+v["ball"]+" |")
        lines+=["","Definite complete aggregate improvements: "+json.dumps(con["strictly_smaller_complete_aggregates"],sort_keys=True)+".",
            "These are comparisons of proved upper bounds, not lower bounds for the actual residual."]
    lines+=["","## Scope","",json.dumps(doc.get("scope",{}),sort_keys=True),
        "","## Actual gates",""]+["- "+g["name"]+": "+str(g["passed"])+"." for g in doc["gates"]]
    lines+=["","Actual new scalar science seconds: "+repr(doc.get("actual_mathematical_wall_seconds"))+".",
        "Actual failure: "+str(doc.get("failure"))+".",
        "Temporary native SHA256: "+str(doc.get("temporary_native_sha256"))+".",
        "The complete row-comparison diagnostics stay temporary. No new data, artifact or Release is persisted.",
        "Physical-to-wave readout, actual seams, the positive affine graph and unknown full high inverse remain separate.",""]
    return "\n".join(lines)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo",type=Path,required=True);p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--manifest-sha",required=True);p.add_argument("--out-dir",type=Path,required=True)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new arithmetic requires actual public Actions")
    ctx.prec=320;ctx.cap=8
    runtime=dict(python=platform.python_version(),python_flint=flint.__version__,numpy=numpy.__version__,scipy=scipy.__version__)
    if runtime!=RUNTIME:raise ValueError("the exact scientific runtime changed")
    a.out_dir.mkdir(parents=True,exist_ok=True);source=sha(__file__);started=time.monotonic()
    doc=dict(kind=KIND,public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=source,input_manifest_sha256=a.manifest_sha,runtime=runtime,arithmetic_bits=320,
        complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        original_complete_coefficient_rows_read=0,original_selected_coefficient_rows_read=0,
        original_complete_word_maxima_read=0,original_complete_genuine_source_terms_read=0,
        new_bound_number_denominator_evaluations=0,new_complete_uniform_comparisons=0,
        new_complete_scalar_recombinations=0,old_numerical_enclosures_recomputed=0,
        old_directed_word_bounds_recomputed=0,old_genuine_source_rows_recomputed=0,
        old_amplitude_or_profile_bounds_recomputed=0,old_radial_integrals_recomputed=0,
        full_high_inverse_claimed=False,original_natural_stage_bytes_modified=0,
        reproducible_outputs_published_to_repository=False,reproducible_outputs_uploaded_to_Releases=False,
        new_reproducible_data_artifact_uploaded=False)
    temporary=dict(row_budget_comparisons={})
    def gate(name,condition):
        doc["gates"].append(dict(name=name,passed=bool(condition)))
        if not condition:raise ValueError(name)
    try:
        m=read(a.manifest)
        params=dict(cutoff_abs_j=97,physical_frequency="4j",physical_root_piece=2549,
            exact_negative_cover=[str(PIECE[0]),str(ROOTS[1])],
            exact_root_interval=list(map(str,ROOTS)),original_matrix_radius="1/1000",
            original_directed_word_run="43632464994/1",original_genuine_source_run="43702688640/1",
            input_window="H^(-4/3) both genuine columns and both signs",
            first_source_window="ordinary L2_r H^(-2/3)",independent_mean_window="ordinary L2_r constants",
            density_zero_word_window="H^(-8/3) -> H^(-5/3)",
            density_one_word_window="H^(-5/3) -> H^(-2/3)",
            actual_directed_matrix_right_gain_provenance=True,
            original_radial_integrations_recomputed=0,arithmetic_bits=320,
            fixed_intrinsic_parameter="eta_0",real_parameter_values_only=True)
        doc["mathematical_parameters"]=params
        gate("the new source, manifest, parameters and no-data execution identity are exact",
            sha(a.manifest)==a.manifest_sha and m["public_repository"]==PUBLIC
            and m["scientific_source_sha256"]==source and m["mathematical_parameters"]==params)
        pins={e["path"]:e for e in m["files"]}
        if len(pins)!=len(m["files"]):raise ValueError("duplicate immutable input")
        for e in m["files"]:
            rel=Path(e["path"])
            if rel.is_absolute() or ".." in rel.parts or not str(rel).startswith(TOPIC):raise ValueError("input outside topic")
            f=a.repo/rel
            if not f.is_file() or f.stat().st_size!=e["bytes"] or sha(f)!=e["sha256"]:
                raise ValueError("changed complete original input "+str(rel))
        paths={k:a.repo/v for k,v in m["input_paths"].items()}
        if any(v not in pins for v in m["input_paths"].values()):raise ValueError("unpinned input role")
        expected=dict(contract=CONTRACT,complete_genuine_execution=C_EXEC,
            complete_genuine_source=C_SOURCE,complete_genuine_manifest=C_MANIFEST,
            directed_process=D_PROCESS,directed_algorithm=D_SOURCE,directed_manifest=D_MANIFEST,
            directed_contract=D_CONTRACT,original_norm_native=OLD_NATIVE,original_norm_process=OLD_PROCESS)
        gate("all accepted complete source, full-word and original coefficient byte identities are fixed",
            all(sha(paths[k])==v for k,v in expected.items()))
        e=read(paths["complete_genuine_execution"]);g=e["actual_scientific_receipt"]
        gate("the complete genuine source is the original zero-return seventeen-gate result",
            e["complete"] and e["actual_returncode"]==0 and e["actual_failure"] is None
            and e["source_budget_source_sha256"]==C_SOURCE and e["input_manifest_sha256"]==C_MANIFEST
            and str(e["run_id"])=="43702688640" and str(e["run_attempt"])=="1"
            and g["complete"] and g["proved"] and g["actual_returncode"]==0 and g["failure"] is None
            and g["source_sha256"]==C_SOURCE and g["input_manifest_sha256"]==C_MANIFEST
            and g["runtime"]==RUNTIME and len(g["gates"])==17 and all(v["passed"] for v in g["gates"])
            and g["original_target_FFT_intrinsic_repair_fold_transport_Taylor_RF_profile_or_norm_recomputed"]==0
            and g["original_complete_output_enclosures_recomputed"]==0
            and g["full_physical_negative_volume_source_paid"] and not g["full_high_inverse_claimed"])
        con=g["complete_source_conclusion"];scope=g["scope"]
        gate("the accepted physical cover, all genuine signs, both inverse windows and true mean remain",
            con["exact_negative_physical_cover"]==[str(PIECE[0]),str(ROOTS[1])]
            and con["actual_dr_measure"] and con["one_sided_uncertain_root_band_retained"]
            and con["both_density_windows_retained"] and con["old_nine_word_and_five_physical_mean_counts"]==[9,5]
            and len(con["complete_first_source_term_L2_upper"])==21
            and len(con["complete_independent_mean_term_L2_upper"])==10
            and scope["original_fixed_intrinsic_parameter"]=="eta_0" and scope["same_original_real_explicit_family"]
            and scope["both_genuine_columns_and_both_carrier_signs"] and scope["all_input_abs_j_at_least97"]
            and scope["output_mean_and_complete_original_primitive_retained"]
            and scope["physical_J_only_on_its_proved_reflected_parity_domain"])
        d=read(paths["directed_process"])
        gate("the complete directed word maxima have their original eight-gate full-matrix provenance",
            d["complete"] and d["actual_returncode"]==0 and d["failure"] is None
            and d["mathematical_complete"] and d["mathematical_failure"] is None
            and str(d["run_id"])=="43632464994" and str(d["run_attempt"])=="1"
            and d["mathematical_source_sha256"]==D_SOURCE and d["manifest_sha256"]==D_MANIFEST
            and len(d["mathematical_gates"])==8 and all(v["passed"] for v in d["mathematical_gates"])
            and d["complete_coefficient_norm_rows"]==1328 and d["complete_radius_cases"]==6
            and d["original_completed_norm_native_sha256"]==OLD_NATIVE
            and d["root_native_sha256"]==ROOT_SHA and d["first_forcing_native_sha256"]==FORCE_SHA
            and d["exact_root_interval"]==list(map(str,ROOTS))
            and d["exact_real_delta_radius"]==str(Q(1,100000000))
            and d["old_mean_and_all_Fourier_outputs_retained"])
        dm=read(paths["directed_manifest"]);cm=read(paths["complete_genuine_manifest"])
        gate("the exact accepted source algorithms and every genuine input are retained verbatim",
            all(any(f==p for p in m["files"]) for f in cm["files"])
            and any(f["sha256"]==D_SOURCE and f["path"]==m["input_paths"]["directed_algorithm"] for f in dm["files"])
            and any(f["sha256"]==D_CONTRACT and f["path"]==m["input_paths"]["directed_contract"] for f in dm["files"]))
        case=next(v for v in d["cases"] if Q(v["exact_radius"])==Q(1,1000))
        ml,mr=map(Q,case["exact_cover"]);maxima=case["complete_case_operator_cost_maxima"]
        gate("all eight complete word maxima cover the entire original negative physical piece",
            case["complete"] and case["complete_original_rows"]==144
            and case["complete_original_matrix_widths"]==["1/16","1/32","1/64"]
            and ml<=PIECE[0]<ROOTS[0]<=ROOTS[1]<=mr
            and set(maxima)==set(WORD_MAP.values())
            and all(nonnegative(v,k).lower()>=0 for k,v in maxima.items()))
        old=read(paths["original_norm_native"]);op=read(paths["original_norm_process"])
        gate("the original complete moment rows and both J constants have their same successful identity",
            old["complete"] and old["proved"] and old["failure"] is None
            and old["source_sha256"]==OLD_SOURCE and old["input_manifest_sha256"]==OLD_MANIFEST
            and all(v["passed"] for v in old["gates"])
            and op["complete"] and op["actual_returncode"]==0 and op["failure"] is None
            and op["mathematical_complete"] and op["mathematical_failure"] is None
            and op["native_sha256"]==OLD_NATIVE and op["native_bytes"]==4837715
            and op["mathematical_source_sha256"]==OLD_SOURCE and op["manifest_sha256"]==OLD_MANIFEST
            and str(op["run_id"])=="43629465215" and str(op["run_attempt"])=="1"
            and old["root_native_sha256"]==ROOT_SHA and old["first_forcing_native_sha256"]==FORCE_SHA
            and all(v["passed"] for v in op["mathematical_gates"]))
        rows=old["coefficient_rows"]
        gate("all original common rows have their exact complete real-parameter cover and independent mean",
            len(rows)==1328 and [x["common_row"] for x in rows]==list(range(1328))
            and all(x["interval"][1]==y["interval"][0] for x,y in zip(rows,rows[1:]))
            and [rows[0]["interval"][0],rows[-1]["interval"][1]]==op["exact_cover"]
            and op["exact_root_interval"]==list(map(str,ROOTS))
            and old["exact_real_delta_radius"]==str(Q(1,100000000))
            and old["old_mean_and_all_Fourier_outputs_retained"])
        selected,parts=selected_rows(rows)
        gate("the exact same six accepted physical row intersections are used without integration",
            len(selected)==g["original_selected_coefficient_rows_read"]==6
            and parts==g["new_genuine_source_radial_integrals"]==con["temporary_complete_source_row_count"]==6
            and all(ml<=Q(v["interval"][0])<Q(v["interval"][1])<=mr for v in selected))
        doc["original_complete_coefficient_rows_read"]=1328
        doc["original_selected_coefficient_rows_read"]=len(selected)
        doc["original_complete_word_maxima_read"]=len(maxima)
        doc["original_complete_genuine_source_terms_read"]=31
        terms=dict(con["complete_first_source_term_L2_upper"]);means=dict(con["complete_independent_mean_term_L2_upper"])
        evidence=[];changed=0
        for density in (0,1):
            for name in FIRST_KEYS+MEAN_KEYS:
                q,record=comparison(selected,maxima,density,name,temporary,doc)
                key=record["source_term"];target=terms if name in FIRST_KEYS else means
                oldterm=target[key];newterm,isnew=selected_total(oldterm,up(q*up(oldterm)))
                target[key]=newterm;record["strictly_smaller_complete_term_bound"]=isnew
                record["accepted_complete_term_read"]=oldterm
                record["new_complete_term_bound"]=newterm
                evidence.append(record);changed+=int(isnew)
        doc["complete_comparison_conclusions"]=evidence
        doc["strictly_smaller_complete_term_bounds"]=changed
        combined=combine(con,terms,means)
        doc["new_complete_scalar_recombinations"]=4
        doc["complete_source_conclusion"]=combined
        doc["accepted_complete_local_vector_conclusion"]=g["complete_local_vector_conclusion"]
        doc["actual_original_directed_word_maxima"]=maxima
        gate("sixteen complete same-budget comparisons retain all source terms and common factors",
            doc["new_complete_uniform_comparisons"]==16
            and doc["new_bound_number_denominator_evaluations"]==16*len(selected)
            and len(terms)==21 and len(means)==10
            and all(rb(v["uniform_comparison_upper"]).lower()>=0 and up(v["uniform_comparison_upper"])<=1 for v in evidence)
            and combined["local_L2_upper"]==con["local_L2_upper"]
            and all(terms[k]==v for k,v in con["complete_first_source_term_L2_upper"].items()
                if k.startswith("local_raw_") or "_old_mean_" in k)
            and all(means[k]==v for k,v in con["complete_independent_mean_term_L2_upper"].items()
                if k.endswith("complete_u_h") or k.endswith("complete_K_vminus_w")))
        gate("all complete first-row, independent-mean and pair bounds remain finite in their exact source windows",
            all(nonnegative(combined[k],k).is_finite() for k in
                ("local_L2_upper","nonlocal_total_L2_upper","first_L2_upper","mean_L2_upper","combined_L2_upper"))
            and combined["both_density_windows_retained"] and combined["old_nine_word_and_five_physical_mean_counts"]==[9,5])
        doc["scope"]=dict(scope)
        doc["scope"].update(complete_directed_word_right_gain_reused=True,
            density_one_conversion_from_complete_matrix_not_isolated_Sobolev=True,
            current_genuine_amplitude_bounds_and_all_mean_factors_unchanged=True,
            coefficient_denominator_is_not_actual_operator_or_function_lower=True,
            original_complete_source_rows_or_integrals_recomputed=False,
            old_directed_Airy_source_integrals_transferred_to_genuine_trial=False,
            original_large_directed_native_not_downloaded=True)
        doc["full_physical_negative_volume_source_paid"]=True
        doc.update(complete=True,proved=True,actual_returncode=0)
    except BaseException as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error))
    finally:
        doc["actual_mathematical_wall_seconds"]=time.monotonic()-started
        doc["temporary_row_comparison_count"]=sum(map(len,temporary["row_budget_comparisons"].values()))
        doc["temporary_row_comparison_payload_sha256"]=payload_sha(temporary["row_budget_comparisons"])
        temporary.update(kind=KIND,source_sha256=source,input_manifest_sha256=a.manifest_sha,complete_conclusions=doc)
        native=a.out_dir/"temporary-directed-word-genuine-source-reuse.json.gz"
        save(native,temporary,True)
        doc["temporary_native_sha256"]=sha(native);doc["temporary_native_bytes"]=native.stat().st_size
        doc["temporary_native_is_not_published"]=True
        actual=doc["actual_returncode"]
        try:
            text=render(doc)
            raw=(json.dumps(doc,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
            if len(raw)>60000 or len(text.encode())>60000:raise ValueError("small final conclusion or process exceeded60000 bytes")
            save(a.out_dir/"process.json",doc);(a.out_dir/"conclusion.md").write_text(text)
        except BaseException as error:
            small={k:v for k,v in doc.items() if k not in ("complete_comparison_conclusions",
                "complete_source_conclusion","accepted_complete_local_vector_conclusion","actual_original_directed_word_maxima")}
            small["actual_scientific_returncode"]=actual
            small["formatting_failure"]=dict(type=type(error).__name__,message=str(error))
            small.update(complete=False,proved=False,actual_returncode=1)
            save(a.out_dir/"process.json",small)
            (a.out_dir/"conclusion.md").write_text("# Actual directed-word reuse formatting failure\n\n"
                "The original scientific return code is "+str(actual)+". Formatting is not reclassified as failed mathematics.\n"
                "Temporary native SHA256: "+doc["temporary_native_sha256"]+"\n")
            actual=1
        print(json.dumps(dict(complete=doc["complete"],actual_returncode=actual,
            old_numerical_enclosures_recomputed=0,old_radial_integrals_recomputed=0,
            new_complete_comparisons=doc["new_complete_uniform_comparisons"],
            reproducible_data_published=False)),flush=True)
    return actual
if __name__=="__main__":raise SystemExit(main())
